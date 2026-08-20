# Firefox l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b95608d528c8` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `d411ef0407f1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,001 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

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
| Strings | 18,001 |
| Missing strings | 162 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 1 |
| Plural variants (dead or missing forms) | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 27 |

### Completeness

**162 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 46
- `browser/browser/ipProtection.ftl` — 14
- `toolkit/toolkit/neterror/netError.ftl` — 12
- `toolkit/toolkit/about/url-classifier.ftl` — 10
- `browser/browser/firefoxView.ftl` — 9
- `browser/browser/featureCallout.ftl` — 8
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/preferences/preferences.ftl` — 7
- `browser/browser/appmenu.ftl` — 6
- `browser/browser/newtab/onboarding.ftl` — 5
- `toolkit/toolkit/about/aboutAddons.ftl` — 4
- `toolkit/toolkit/global/theme-picker.ftl` — 4

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 670, `curly-single` 166, `straight-double` 29 | **curly-double** |
| apostrophe | `typographic` 952, `straight` 50 | **typographic** |
| ellipsis | `char` 459 | **char** |
| dash | `em` 72, `en` 2 | **em** |
| nbsp | `total` 9, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 2, `formal` 58 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 27 strings** — 27 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
  - Affected: `BadOpaqueRedirectInterceptionWithURL`, `BlockAutoplayWebAudioStartError`, `InterceptedErrorResponseWithURL`, `InterceptedUsedResponseWithURL`, `LenientThisWarning`, `ManifestIdIsInvalid`, `MediaEMENoCodecsDeprecatedWarning`, `NavigatorGetUserMediaWarning`, `PEDisallowedImportRule`, `PushMessageBadCryptoError`, `PushMessageBadSalt`, `RewriteYouTubeEmbedPathParams` …and 15 more

---

## 3. Open findings (194)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 4 |
| 2 | Wrong content (says something other than the English) | 62 |
| 3 | Degraded language (grammar, spelling, terminology) | 88 |
| 4 | Cosmetic (typography, spacing) | 40 |

### A. Functional, markup, variables & plurals

- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — `fxa-signout-dialog-body-aiwindow` calls `-smart-window-brand-name` with ['plural-form'], but that term selects on ['form']
  - Current: `Eşitlenen veriler hesabınızda kalmaya devam edecek. Açık olan { -smart-window-brand-name } klasik pencerelere dönüşecek.`
  - en-US: `{ -smart-window-brand-name(form: "lowercase-plural") }`
  - The term falls back to its catch-all variant, so the intended form is never selected.
- `autofill-address-country` — `browser/browser/preferences/formAutofill.ftl` — "Ülke" for en "Country or Region"; "or Region" dropped, and it now collides with autofill-address-country-only = "Ülke".
- `autofill-address-county` — `browser/browser/preferences/formAutofill.ftl` — "İlçe", already used by autofill-address-district (District). County is a first-level division listed next to Province/State.
- `autofill-address-name` — `browser/browser/preferences/formAutofill.ftl` — "Ad", identical to autofill-address-given-name (First Name) → "Ad soyad".
  - en-US: `"Ad soyad".`

### B. Mistranslation, reversed meaning, wrong names & brand

- `extension-colorways-bold-name` — `browser/browser/appExtensionFields.ftl` — developer comment not followed. The comment states "Bold" is used in the sense of bravery. Current "Koyu" means dark and duplicates extension-firefox-compact-dark-name. → "Cesur".
  - en-US: `"Cesur".`
- `popup-warning-exceeded-message` — `browser/browser/browser.ftl` — "more than" dropped; sibling popup-warning-exceeded-with-redirect-message includes "en az".
- `urlbar-result-weather-title` — `browser/browser/browser.ftl` — city and region swapped: { $region }, { $city } → { $city }, { $region } (cf. urlbar-result-weather-title-with-country).
  - Current: `{ $region }, { $city }`
  - en-US: `{ $city }, { $region }`
- `mr2022-background-update-toast-title` — `browser/browser/newtab/asrouter.ftl` — the fourth sentence "No compromises." is dropped entirely.
- `windows-10-eos-challenger-callout-title` — `browser/browser/newtab/asrouter.ftl` — "gereksiz özelliklerle dolu halde gelmez" ≠ en "isn't preloaded like other Big Tech browsers" (= not pre-installed on the device). The second sentence "That's the point." is also dropped.
- `media-count` — `browser/browser/pageInfo.ftl` — "Sayaç" (counter/meter) → "Sayı" (en "Count" is a quantity column).
  - en-US: `"Sayı"`
- `fonts-langgroup-header` — `browser/browser/preferences/fonts.ftl` — "Karakter kümesi" (character set) ≠ en "Fonts for" (a language-group selector).
- `more-from-moz-mozilla-monitor-us-description` — `browser/browser/preferences/moreFromMozilla.ftl` — "Automatically" dropped.
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — "Form düğmeleri" ≠ en "form controls"; also uses descriptive "kullanabilirsiniz" where every other checkbox in the pane uses the imperative.
- `content-blocking-cross-site-tracking-cookies-plus-isolate` — `browser/browser/preferences/preferences.ftl` — "takip kodları ve" added; en lists only "Cross-site tracking cookies".
- `preferences-ai-controls-on-device-group` — `browser/browser/preferences/preferences.ftl` — the condition "if you use the feature" dropped, implying unconditional downloads.
- `settings-keyboard-shortcuts-group` — `browser/browser/preferences/preferences.ftl` — "kolaylaştırın" (make it easier) ≠ en "Control how you move around and interact with".
- `should-restart-ok` — `browser/browser/preferences/preferences.ftl` — "now" dropped; the OK button is now byte-identical to should-restart-title.
- `sitedata-total-size` — `browser/browser/preferences/preferences.ftl` — "cookies" dropped from "Your stored cookies, site data, and cache".
- `set-background-stretch` — `browser/browser/setDesktopBackground.ftl` — "Genişlet", identical to set-background-span; two distinct wallpaper modes collide. → "Uzat".
  - en-US: `"Uzat".`
- `webrtc-sharing-menu` — `browser/browser/webrtcIndicator.ftl` — subject/object inverted. "Sekme paylaşan cihazlar" → "Cihaz paylaşan sekmeler" (en "Tabs sharing devices"; the menu lists tabs).
  - en-US: `"Cihaz paylaşan sekmeler"`
- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — the token inside <code> is the HTML title attribute name and must stay English. Current <code>başlığı</code> → <code>title</code>.
- `storage-table-type-cache-hint` — `devtools/client/storage.ftl` — en "View and delete the cache storage entries by selecting a storage"; both the object and the verb are wrong.
- `inactive-css-at-position-try-not-supported` — `devtools/client/tooltips.ftl` — { $property } is a CSS property, called a "kural" (rule) here.
- `inactive-css-no-principal-box` — `devtools/client/tooltips.ftl` — wrong subject: the tr says the property does not create a principal box / is a ruby element; en says the element is.
- `inactive-css-ruby-element` — `devtools/client/tooltips.ftl` — wrong subject: the tr says the property does not create a principal box / is a ruby element; en says the element is.
- `console-stacktrace` — `mobile/android/mobile/android/geckoViewConsole.ftl` — missing ablative for en "Stack trace from { $filename }".
- `cert-format-base64-chain` — `security/manager/security/certificates/certManager.ftl` — "with chain" dropped; each is now byte-identical to its non-chain sibling, so the two export formats cannot be told apart.
- `cert-format-pkcs7-chain` — `security/manager/security/certificates/certManager.ftl` — "with chain" dropped; each is now byte-identical to its non-chain sibling, so the two export formats cannot be told apart.
- `exception-mgr-supplemental-warning` — `security/manager/security/certificates/certManager.ftl` — "Legitimate" dropped; the whole point of the warning is that legitimate sites never ask this.
- `pk11-bad-password` — `security/manager/security/certificates/certManager.ftl` — "Geçerli parola girişi hatalı" introduces a "current password" notion absent from en "The password entered was incorrect."
- `devmgr-button-unload` — `security/manager/security/certificates/deviceManager.ftl` — "Boşalt" (empty/pour out) → "Kaldır" (en "Unload" a PKCS#11 module).
  - en-US: `"Kaldır"`
- `load-device` — `security/manager/security/certificates/deviceManager.ftl` — "PKCS #11" with a space; en and the file's own load-device-modname-default / load-pk11-module-file-picker-title use "PKCS#11".
- `pippki-pw-change2empty-in-fips-mode` — `security/manager/security/pippki/pippki.ftl` — adds "ana" (Primary) where en says only "a non-empty password"; this is the security-device password dialog.
- `details-notification-soft-blocked-other-disabled` — `toolkit/toolkit/about/aboutAddons.ftl` — this is the add-on ("other") variant but says "Uzantıyı"; …-disabled2 correctly says "Eklentiyi".
- `plugins-openh264-description` — `toolkit/toolkit/about/aboutAddons.ftl` — stale http://www.openh264.org/; en specifies https://.
- `place-database-stats-count` — `toolkit/toolkit/about/aboutSupport.ftl` — "Sayaç" (counter/meter) → "Sayı" (en "Count" is a quantity column).
  - en-US: `"Sayı"`
- `processes-count` — `toolkit/toolkit/about/aboutSupport.ftl` — "Sayaç" (counter/meter) → "Sayı" (en "Count" is a quantity column).
  - en-US: `"Sayı"`
- `about-webauthn-auth-info-max-rpids-for-set-min-pin-length` — `toolkit/toolkit/about/aboutWebauthn.ftl` — "relying" dropped from "relying party IDs", leaving "taraf kimliği" ambiguous.
- `about-webauthn-auth-info-preferred-platform-uv-attempts` — `toolkit/toolkit/about/aboutWebauthn.ftl` — parses as "platform user's verification" instead of "platform user verification".
- `profile-directory-explanation` — `toolkit/toolkit/global/createProfileWizard.ftl` — "yer imleriniz ve parolalarınız" is not in en ("preferences and other user-related data").
- `csp-error-illegal-protocol` — `toolkit/toolkit/global/cspErrors.ftl` — the colon belongs to { $scheme }: "yasaklı bir { $scheme } içeriyor: protokol kaynağı" → "yasaklı bir { $scheme }: protokol kaynağı içeriyor".
  - Current: `{ $scheme }`
  - en-US: `"yasaklı bir { $scheme }: protokol kaynağı içeriyor".`
- `language-name-ab` — `toolkit/toolkit/intl/languageNames.ftl` — Abkhazian — Abazaca — Abhazca — Abaza (abq) is a different language.
- `language-name-gd` — `toolkit/toolkit/intl/languageNames.ftl` — Scottish Gaelic — İskoçça — İskoç Gaelcesi — "İskoçça" is Scots — already language-name-sco.
- `language-name-gl` — `toolkit/toolkit/intl/languageNames.ftl` — Galician — Galce — Galiçyaca — "Galce" is Welsh — and is already language-name-cy. Two languages, one name.
- `language-name-jv` — `toolkit/toolkit/intl/languageNames.ftl` — Javanese — Cava dili — Cava Dili — every other "… Dili" entry is capitalized.
- `language-name-kab` — `toolkit/toolkit/intl/languageNames.ftl` — Kabyle — Berberice — Kabilce — "Berberice" names the whole Berber family.
- `language-name-nn` — `toolkit/toolkit/intl/languageNames.ftl` — Norwegian Nynorsk — Norveççe (Nynorsk) — Norveççe Nynorsk — sibling -nb is "Norveççe Bokmål", no parentheses.
- `language-name-se` — `toolkit/toolkit/intl/languageNames.ftl` — Northern Sami — Nord Sami — Kuzey Samicesi — "Nord" is not Turkish.
- `language-name-si` — `toolkit/toolkit/intl/languageNames.ftl` — Sinhala — Seylanca — Sinhalaca — outdated exonym from "Ceylon".
- `region-name-bl` — `toolkit/toolkit/intl/regionNames.ftl` — Saint Barthélemy — Saint Barthelemy — Saint Barthélemy — diacritic dropped.
- `region-name-cy` — `toolkit/toolkit/intl/regionNames.ftl` — Cyprus — Güney Kıbrıs Rum Kesimi — Kıbrıs — en is the plain ISO 3166 country name; the current string names a different political entity.
- `region-name-nr` — `toolkit/toolkit/intl/regionNames.ftl` — Nauru — Nauruca — Nauru — "Nauruca" is the language, already language-name-na.
- `region-name-re` — `toolkit/toolkit/intl/regionNames.ftl` — Réunion — Reunion — Réunion — diacritic dropped (present in en).
- `region-name-to` — `toolkit/toolkit/intl/regionNames.ftl` — Tonga — Tongaca — Tonga — "Tongaca" is the language, already language-name-to.
- `region-name-xu` — `toolkit/toolkit/intl/regionNames.ftl` — Johnston Atoll — Johnston Atoll — Johnston Atolü — untranslated; the parallel region-name-xl is "Palmyra Atolü".
- `sec-error-ocsp-bad-http-response` — `toolkit/toolkit/neterror/nsserrors.ftl` — sec-error-ocsp-bad-http-response, sec-error-ocsp-unknown-response-status — "aldı"/"karşılaştı" → "döndürdü" (en "returned").
  - en-US: `"döndürdü"`
- `sec-error-ocsp-unknown-response-status` — `toolkit/toolkit/neterror/nsserrors.ftl` — sec-error-ocsp-bad-http-response, sec-error-ocsp-unknown-response-status — "aldı"/"karşılaştı" → "döndürdü" (en "returned").
  - en-US: `"döndürdü"`
- `sec-error-unsupported-ec-point-form` — `toolkit/toolkit/neterror/nsserrors.ftl` — sec-error-unsupported-elliptic-curve, sec-error-unsupported-ec-point-form — "oval eğri" → "eliptik eğri".
  - en-US: `"eliptik eğri".`
- `sec-error-unsupported-elliptic-curve` — `toolkit/toolkit/neterror/nsserrors.ftl` — sec-error-unsupported-elliptic-curve, sec-error-unsupported-ec-point-form — "oval eğri" → "eliptik eğri".
  - en-US: `"eliptik eğri".`
- `ssl-error-bad-client` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-bad-client, ssl-error-bad-server — locative for en "from the client/server": "istemcide" → "istemciden gelen".
  - en-US: `"istemciden gelen".`
- `ssl-error-bad-server` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-bad-client, ssl-error-bad-server — locative for en "from the client/server": "istemcide" → "istemciden gelen".
  - en-US: `"istemciden gelen".`
- `ssl-error-handshake-failure-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — "kabul edilebilir sayıda güvenlik değişkeniyle" ≠ en "an acceptable set of security parameters".
- `ssl-error-md5-digest-failure` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-md5-digest-failure, ssl-error-sha-digest-failure — "derleme" (compilation) → "özet" (en "digest"); sec-error-digest-not-found already uses "özet".
- `ssl-error-sha-digest-failure` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-md5-digest-failure, ssl-error-sha-digest-failure — "derleme" (compilation) → "özet" (en "digest"); sec-error-digest-not-found already uses "özet".
- _…and 2 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `about-logins-confirm-remove-all-sync-dialog-title` — `browser/browser/aboutLogins.ftl` — the singular variant reads "{ $count } hesap hepsi tüm cihazlardan kaldırılsın mı?"; "hepsi" is copied from the plural variant and is ungrammatical here.
- `backup-folder-name` — `browser/browser/backupSettings.ftl` — Geri Yukleme — Geri Yükleme
- `callout-firefox-view-tab-pickup-title` — `browser/browser/featureCallout.ftl` — Sekma taşıma — Sekme taşıma
- `firefox-relay-must-login-to-fxa` — `browser/browser/firefoxRelay.ftl` — kullanak için — kullanmak için
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — Favorileri siteleriniz — Favori siteleriniz
- `newtab-sports-widget-message-survey-body` — `browser/browser/newtab/newtab.ftl` — Dünya Kupaları sona erdi — Dünya Kupası sona erdi (singular; verb disagrees)
- `newtab-weather-menu-temperature-option-celsius` — `browser/browser/newtab/newtab.ftl` — Celcius — Celsius
- `onboarding-refresh-import-subtitle` — `browser/browser/newtab/onboarding.ftl` — "geçmişinizi ve ve diğer" — "…ve diğer"
- `pane-experimental-description4` — `browser/browser/preferences/preferences.ftl` — oldıkları — oldukları
- `preferences-copy-profile-header` — `browser/browser/preferences/preferences.ftl` — parolarar — parolalar
- `preferences-etp-advanced-settings-group` — `browser/browser/preferences/preferences.ftl` — "çoğu takip kodunu olarak engelleyerek" — "…otomatik olarak engelleyerek" (word dropped)
- `space-alert-over-5gb-message2` — `browser/browser/preferences/preferences.ftl` — kulllanılabilen — kullanılabilen
- `space-alert-under-5gb-message2` — `browser/browser/preferences/preferences.ftl` — kulllanılabilen … deneyimi içi — kullanılabilen … için
- `site-data-settings-description` — `browser/browser/preferences/siteDataSettings.ftl` — "bilgisayarınızda ve çerez ve site verisi" — stray "ve"
- `restored-profile-page-learn-more` — `browser/browser/profiles.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
- `monitor-partial-breaches-motivation-description` — `browser/browser/protections.ftl` — ihallerinizi — ihlallerinizi
- `protections-panel-description-shim-allowed-learn-more` — `browser/browser/protectionsPanel.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
- `report-broken-site-panel-intro-text` — `browser/browser/reportBrokenSite.ftl` — extra "için" after a dative that is already the complement of "yardımcı oluyor".
- `existing-user-tou-learn-more` — `browser/browser/termsofuse.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
- `translations-panel-learn-more-link` — `browser/browser/translations.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
- `webrtc-reason-for-no-permanent-allow-audio` — `browser/browser/webrtcIndicator.ftl` — paylacağınızı — paylaşacağınızı
- `styleeditor-filter-input` — `devtools/client/styleeditor.ftl` — Stil dosyalarını filtrelere — …filtrele
- `whypaused-breakpoint` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
- `whypaused-event-breakpoint` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
- `whypaused-promise-rejection` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
- `file-browse-pkcs12-spec` — `security/manager/security/certificates/certManager.ftl` — PKSC12 — PKCS12
- `profiles-rename` — `toolkit/toolkit/about/aboutProfiles.ftl` — değiștir (U+0219, Romanian s-comma) — değiştir (U+015F)
- `rights-webservices-term-7` — `toolkit/toolkit/about/aboutRights.ftl` — ihtilafi — ihtilafı
- `media-capabilities-title` — `toolkit/toolkit/about/aboutSupport.ftl` — Çoku ortam — Çoklu ortam
- `place-database-last-integrity-corruption-date` — `toolkit/toolkit/about/aboutSupport.ftl` — sütünlük — bütünlük
- `privacy-spoof-english` — `toolkit/toolkit/global/resistFingerPrinting.ftl` — değştirmek — değiştirmek
- `sec-error-not-fortezza-issuer` — `toolkit/toolkit/neterror/nsserrors.ftl` — "zinciri has FORTEZZA olmayan" — stray English word "has"
- `ssl-error-cert-kea-mismatch` — `toolkit/toolkit/neterror/nsserrors.ftl` — anahtar değiş algoritması — anahtar değişim algoritması
- `elevation-error-manual` — `toolkit/toolkit/updates/elevation.ftl` — "ziyaretip edip" — "ziyaret edip"

### D. Terminology, register & consistency

- `reset-pbm-panel-description` — `browser/browser/browser.ftl` — "özel sekmeleri" vs "gizli" used for "private" everywhere, including reset-pbm-panel-description2 right above.
- `contextual-manager-password-login-line-with-alert` — `browser/browser/contextual-manager.ftl` — "(Dikkat)" vs "(Uyarı)" in the two parallel strings.
- `menu-application-set-as-default` — `browser/browser/menubar.ftl` — "saptanmış tarayıcı"; every other string in the locale uses "varsayılan".
- `migration-wizard-safari-permissions-sub-header` — `browser/browser/migrationWizard.ftl` — "yer işaretleri"; the only occurrence in the whole locale — everywhere else bookmarks are "yer imleri".
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — "saptanmış tarayıcı"; every other string in the locale uses "varsayılan".
- `newtab-clock-widget-input-nickname` — `browser/browser/newtab/newtab.ftl` — ".label = Ad" for en "Nickname"; newtab-clock-widget-edit-item-with-nickname uses "takma adı", and plain "Ad" collides with a real name field (the dev comment warns about this).
- `newtab-sports-widget-match-aria-label-upcoming-suspended` — `browser/browser/newtab/newtab.ftl` — "ara verildi" vs the status string newtab-sports-widget-suspended "Askıya alındı".
- `places-view-sortby-name` — `browser/browser/places.ftl` — "İsme göre sırala" vs places-sortby-name "Ada göre sırala" for the same en string in the same file.
- `add-engine-dialog` — `browser/browser/preferences/addEngine.ftl` — see also S4.
- `autofill-add-new-address-title` — `browser/browser/preferences/formAutofill.ftl` — see also S4.
- `autofill-addresses-add-button` — `browser/browser/preferences/preferences.ftl` — see also S4.
- `preferences-ai-controls-translations-control` — `browser/browser/preferences/preferences.ftl` — "Çeviri" vs "Çeviriler" everywhere else.
- `preferences-text-zoom-override-warning2` — `browser/browser/preferences/preferences.ftl` — quotes the option as "Yalnızca metni yakınlaştır" but its actual label preferences-zoom-text-only is "Sadece metni yakınlaştır".
- `remove-engine-remove` — `browser/browser/preferences/preferences.ftl` — "Sil" vs the triggering control search-remove-engine "Kaldır".
- `security-privacy-issue-warning-safe-browsing` — `browser/browser/preferences/preferences.ftl` — "yanıltıcı" vs "aldatıcı" used for en "deceptive" in security-enable-safe-browsing, security-browsing-protection, browsing-protection-group2.
- `profiles-cyan-theme-title` — `browser/browser/profiles.ftl` — tooltip says "Cyan temayı uygula" but the theme's own label profiles-cyan-theme is "Açık mavi".
- `safeb-blocked-unwanted-page-learn-more` — `browser/browser/safebrowsing/blockedSite.ftl` — "kötü amaçlı yazılım" vs "zararlı yazılım" in the three sibling strings.
- `add-engine-dialog2` — `browser/browser/search.ftl` — see also S4.
- `styleeditor-filter-input` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
- `styleeditor-new-button` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
- `styleeditor-save-button` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
- `styleeditor-stylesheet-all-filtered` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
- `styleeditor-visibility-toggle` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
- `styleeditor-visibility-toggle-system` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
- `options-context-triggers-page-refresh-persists` — `devtools/client/toolbox-options.ftl` — "(sayfayı tazeler)" vs "sayfayı yeniden yükler" in the two sibling strings.
- `options-stylesheets-in-the-debugger-label` — `devtools/client/toolbox-options.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
- `xslt-call-to-key-not-allowed` — `dom/dom/xslt.ftl` — "işlev" vs "fonksiyon" used in xpath-unknown-function, xpath-bad-argument-count, xpath-bad-extension-function; also "the key function" is the XSLT key() function name, not a generic "anahtar işlev".
- `add-exception-valid-long` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
- `delete-ssl-override-confirm` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
- `delete-ssl-override-impact` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
- `delete-ssl-override-title` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
- `exception-mgr` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
- `exception-mgr-extra-button` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
- `exception-mgr-permanent` — `security/manager/security/certificates/certManager.ftl` — "ayrıcalık" (privilege) for en "exception", while certmgr-add-exception and certmgr-server use "istisna".
- `fips-nonempty-primary-password-required` — `security/manager/security/certificates/deviceManager.ftl` — "güvenlik cihazı" vs "güvenlik aygıtı" used in devmgr-window, unable-to-toggle-fips, pkcs12-dup-data, certmgr-token-name, change-password-token.
- `protected-auth-prompt` — `security/manager/security/pippki/pippki.ftl` — "güvenlik cihazı" vs "güvenlik aygıtı" used in devmgr-window, unable-to-toggle-fips, pkcs12-dup-data, certmgr-token-name, change-password-token.
- `about-glean-about-data-header` — `toolkit/toolkit/about/aboutGlean.ftl` — see also S4.
- `about-glean-category-about-data` — `toolkit/toolkit/about/aboutGlean.ftl` — see also S4.
- `about-glean-label-for-tag-pings` — `toolkit/toolkit/about/aboutGlean.ftl` — "pinglerinizi"; every other occurrence in the file uses "ping'ler" with an apostrophe.
- `main-thread-no-omtc` — `toolkit/toolkit/about/aboutSupport.ftl` — "(işlem) parçacığı" for thread; bare "parçacık" means particle. The locale's term elsewhere (aboutProcesses.ftl) is "iş parçacığı".
- `about-telemetry-slow-sql-main` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "(işlem) parçacığı" for thread; bare "parçacık" means particle. The locale's term elsewhere (aboutProcesses.ftl) is "iş parçacığı".
- `about-telemetry-slow-sql-other` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "(işlem) parçacığı" for thread; bare "parçacık" means particle. The locale's term elsewhere (aboutProcesses.ftl) is "iş parçacığı".
- `about-telemetry-slow-sql-statement` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "İfade" vs the section heading about-telemetry-slow-sql-section "Deyimleri".
- `certificate-viewer-given-name` — `toolkit/toolkit/about/certviewer.ftl` — "Adı", identical to certificate-viewer-name; the two certificate fields become indistinguishable → "Ön adı".
  - en-US: `"Ön adı".`
- `webext-perms-update-text2` — `toolkit/toolkit/global/extensions.ftl` — quotes the Cancel button as "İptal", but it is labelled webext-perms-cancel = "Vazgeç"; webext-perms-update-text gets it right.
- `wizard-macos-button-next` — `toolkit/toolkit/global/wizard.ftl` — "İleri" for the macOS "Continue" variant, while profile-creation-explanation-4 tells macOS users to press "Devam düğmesine".
- `pdfjs-editor-alt-text-button-label` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Alternatif metin" in 4 strings vs "Alt metin" in ~20.
- `pdfjs-editor-alt-text-settings-create-model-description` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Görme engelli kişilere" narrows en "people who can't see the image"; pdfjs-editor-alt-text-dialog-description renders the same source correctly.
- `pdfjs-editor-new-alt-text-description` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Görme engelli kişilere" narrows en "people who can't see the image"; pdfjs-editor-alt-text-dialog-description renders the same source correctly.
- `pdfjs-editor-undo-bar-message-stamp` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Görsel silindi" vs "Resim" used in every other image string.
- `margin-group-label-inches` — `toolkit/toolkit/printing/printDialogs.ftl` — "Kenarlar" (edges) vs printui-margins "Kenar boşlukları".
- `margin-group-label-metric` — `toolkit/toolkit/printing/printDialogs.ftl` — "Kenarlar" (edges) vs printui-margins "Kenar boşlukları".
- `print-setup` — `toolkit/toolkit/printing/printDialogs.ftl` — "Sayfa Yapısı" vs the menu item that opens it, printpreview-page-setup "Sayfa düzeni…".
- `printui-sheets-count` — `toolkit/toolkit/printing/printUI.ftl` — "{ $sheetCount } sayfa" for en "sheets of paper", while "sayfa" is already page; printui-pages-per-sheet uses "yaprak".

### E. Typography, punctuation & spacing

- `reader-view-enter-button` — `browser/browser/browser.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `pin-tabs-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `menu-view-enter-readerview` — `browser/browser/menubar.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `import-safari-permissions-string` — `browser/browser/migration.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `mr2022-onboarding-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `tab-groups-onboarding-create-group-title-3` — `browser/browser/newtab/onboarding.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `tab-groups-onboarding-saved-groups-title-3` — `browser/browser/newtab/onboarding.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `tab-groups-onboarding-session-restore-title-2` — `browser/browser/newtab/onboarding.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `policy-DisableSafeMode` — `browser/browser/policies/policies-descriptions.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `policy-FirefoxHome2` — `browser/browser/policies/policies-descriptions.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — serial comma before "ve" carried over from English: "127.0.0.1/8, ve ::1" → "127.0.0.1/8 ve ::1".
- `permissions-block-popups-exceptions-button4` — `browser/browser/preferences/preferences.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `set-password-reminder` — `security/manager/security/pippki/pippki.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `about-glean-label-for-tag-pings-with-requirements` — `toolkit/toolkit/about/aboutGlean.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `about-logging-invalid-output` — `toolkit/toolkit/about/aboutLogging.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `about-logging-unknown-logging-preset` — `toolkit/toolkit/about/aboutLogging.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `about-logging-unknown-option` — `toolkit/toolkit/about/aboutLogging.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `about-logging-unknown-profiler-preset` — `toolkit/toolkit/about/aboutLogging.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `profiles-delete-profile-confirm` — `toolkit/toolkit/about/aboutProfiles.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `profiles-opendir` — `toolkit/toolkit/about/aboutProfiles.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `rights-intro-point-3` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `rights-intro-point-4` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `rights-webservices-term-1` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `rights-webservices-term-3` — `toolkit/toolkit/about/aboutRights.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `rights-webservices-term-4` — `toolkit/toolkit/about/aboutRights.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `rights-webservices-term-5` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `show-dir-label` — `toolkit/toolkit/about/aboutSupport.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `about-telemetry-data-details-current` — `toolkit/toolkit/about/aboutTelemetry.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `about-telemetry-data-details-current` — `toolkit/toolkit/about/aboutTelemetry.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `about-webrtc-save-page-dialog-title` — `toolkit/toolkit/about/aboutWebrtc.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `experimental-features-link-previews-description-no-ai` — `toolkit/toolkit/firefoxlabs/features.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `experimental-features-media-jxl-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
- `csp-xfo-blocked-long-desc` — `toolkit/toolkit/neterror/certError.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
- `neterror-net-offline` — `toolkit/toolkit/neterror/netError.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
- `neterror-unknown-socket-type-psm-installed` — `toolkit/toolkit/neterror/netError.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (91)

- `settings-update-other-instance-handling-updates` — `browser/browser/aboutDialog.ftl` — fixed 2026-07-30
- `update-otherInstanceHandlingUpdates` — `browser/browser/aboutDialog.ftl` — fixed 2026-07-30
- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — fixed 2026-07-30
- `bookmarks-tools-toolbar-visibility-menuitem` — `browser/browser/browser.ftl` — fixed 2026-07-30
- `content-sharing-modal-too-many-pages` — `browser/browser/contentSharing.ftl` — fixed 2026-07-30
- `bookmark-overlay-folders-expander-hide` — `browser/browser/editBookmarkOverlay.ftl` — fixed 2026-07-30
- `bookmark-overlay-tags-expander-hide` — `browser/browser/editBookmarkOverlay.ftl` — fixed 2026-07-30
- `firefoxview-search-text-box-history` — `browser/browser/firefoxView.ftl` — fixed 2026-07-30
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — fixed 2026-07-30
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — fixed 2026-07-30
- `ip-protection-site-exceptions-all-sites-button` — `browser/browser/ipProtection.ftl` — fixed 2026-07-30
- `cfr-doorhanger-video-support-header` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-30
- `set-default-menu-message-row-layout-title-variant` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-30
- `spotlight-better-internet-header` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-30
- `newtab-widget-lists-name-label-checklist` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-30
- `newtab-widget-timer-label-play` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-30
- `onboarding-many-tabs-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-07-30
- `onboarding-refresh-sync-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-07-30
- `policy-FirefoxHome2` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-07-30
- `policy-PopupBlocking` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-07-30
- `fonts-langgroup-latin` — `browser/browser/preferences/fonts.ftl` — fixed 2026-07-30
- `autofill-address-department` — `browser/browser/preferences/formAutofill.ftl` — fixed 2026-07-30
- `permissions-exceptions-cookie-desc` — `browser/browser/preferences/permissions.ftl` — fixed 2026-07-30
- `containers-disable-alert-cancel-button` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-30
- `feature-disable-requires-restart` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-30
- `performance-limit-content-process-blocked-desc` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-30
- `preferences-doh-description` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-30
- `preferences-doh-description2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-30
- `sitedata-option-block-all` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-30
- `custom-avatar-crop-view` — `browser/browser/profiles.ftl` — fixed 2026-07-30
- `graph-week-summary` — `browser/browser/protections.ftl` — fixed 2026-07-30
- `lockwise-header-content-logged-in` — `browser/browser/protections.ftl` — fixed 2026-07-30
- `monitor-breaches-unresolved-description` — `browser/browser/protections.ftl` — fixed 2026-07-30
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — fixed 2026-07-30
- `set-background-center` — `browser/browser/setDesktopBackground.ftl` — fixed 2026-07-30
- `sync-account-in-use-description-merge` — `browser/browser/sync.ftl` — fixed 2026-07-30
- `tab-context-send-to-device2` — `browser/browser/tabContextMenu.ftl` — fixed 2026-07-30
- `about-debugging-runtime-profile-button2` — `devtools/client/aboutdebugging.ftl` — fixed 2026-07-30
- `about-debugging-worker-fetch-listening` — `devtools/client/aboutdebugging.ftl` — fixed 2026-07-30
- `perftools-request-to-stop-profiler` — `devtools/client/perftools.ftl` — fixed 2026-07-30
