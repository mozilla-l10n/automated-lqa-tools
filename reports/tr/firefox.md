# Firefox l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `f2e9b7fce093` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `37560db2354a` |
| **Previous run** | 2026-08-21 @ `a9b9a116b725` |
| **Mode** | incremental |
| **Strings reviewed this run** | 4 of 18,001 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for tr: [android](android.md)

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
| Missing strings | 172 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 1 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 5 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 27 |

### Completeness

**172 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 47
- `browser/browser/ipProtection.ftl` — 14
- `toolkit/toolkit/neterror/netError.ftl` — 12
- `toolkit/toolkit/about/url-classifier.ftl` — 10
- `browser/browser/firefoxView.ftl` — 9
- `browser/browser/preferences/preferences.ftl` — 9
- `browser/browser/appmenu.ftl` — 8
- `browser/browser/featureCallout.ftl` — 8
- `browser/browser/preferences/containers.ftl` — 7
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

## 3. Open findings (199)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 4 |
| 2 | Wrong content (says something other than the English) | 67 |
| 3 | Degraded language (grammar, spelling, terminology) | 88 |
| 4 | Cosmetic (typography, spacing) | 40 |

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

- `extension-colorways-bold-name` — `browser/browser/appExtensionFields.ftl` — developer comment not followed. The comment states "Bold" is used in the sense of bravery. Current "Koyu" means dark and duplicates extension-firefox-compact-dark-name. → "Cesur".
    - Source: `{ $colorway-name } — Bold`
    - Suggest: `"Cesur".`
- `popup-warning-exceeded-message` — `browser/browser/browser.ftl` — "more than" dropped; sibling popup-warning-exceeded-with-redirect-message includes "en az".
    - Source: `{$popupCount ->} [other] { -brand-short-name } prevented this site from opening more than { $popupCount } pop-up windows.`
- `urlbar-result-weather-title` — `browser/browser/browser.ftl` — city and region swapped: { $region }, { $city } → { $city }, { $region } (cf. urlbar-result-weather-title-with-country).
    - Current: `{ $region }, { $city }`
    - Source: `<strong>{ $temperature }°{ $unit }</strong> in { $city }, { $region }`
    - Suggest: `{ $city }, { $region }`
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
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — "Form düğmeleri" ≠ en "form controls"; also uses descriptive "kullanabilirsiniz" where every other checkbox in the pane uses the imperative.
    - Source: `accesskey: t label: Use the tab key to move focus between form controls and links`
- `content-blocking-cross-site-tracking-cookies-plus-isolate` — `browser/browser/preferences/preferences.ftl` — "takip kodları ve" added; en lists only "Cross-site tracking cookies".
    - Source: `Cross-site tracking cookies, and isolate remaining cookies`
- `preferences-ai-controls-on-device-group` — `browser/browser/preferences/preferences.ftl` — the condition "if you use the feature" dropped, implying unconditional downloads.
    - Source: `description: These use small AI models that download to your device if you use the feature. This approach helps protect your privacy. label: On-device AI`
- `settings-keyboard-shortcuts-group` — `browser/browser/preferences/preferences.ftl` — "kolaylaştırın" (make it easier) ≠ en "Control how you move around and interact with".
    - Source: `description: Control how you move around and interact with { -brand-short-name }. label: Keyboard shortcuts`
- `should-restart-ok` — `browser/browser/preferences/preferences.ftl` — "now" dropped; the OK button is now byte-identical to should-restart-title.
    - Source: `Restart { -brand-short-name } now`
- `sitedata-total-size` — `browser/browser/preferences/preferences.ftl` — "cookies" dropped from "Your stored cookies, site data, and cache".
    - Source: `Your stored cookies, site data, and cache are currently using { $value } { $unit } of disk space.`
- `set-background-stretch` — `browser/browser/setDesktopBackground.ftl` — "Genişlet", identical to set-background-span; two distinct wallpaper modes collide. → "Uzat".
    - Source: `label: Stretch`
    - Suggest: `"Uzat".`
- `webrtc-sharing-menu` — `browser/browser/webrtcIndicator.ftl` — subject/object inverted. "Sekme paylaşan cihazlar" → "Cihaz paylaşan sekmeler" (en "Tabs sharing devices"; the menu lists tabs).
    - Source: `accesskey: d label: Tabs sharing devices`
    - Suggest: `"Cihaz paylaşan sekmeler"`
- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — the token inside <code> is the HTML title attribute name and must stay English. Current <code>başlığı</code> → <code>title</code>.
    - Source: `Documents must have a <code>title</code>. <a>Learn more</a>`
- `storage-table-type-cache-hint` — `devtools/client/storage.ftl` — en "View and delete the cache storage entries by selecting a storage"; both the object and the verb are wrong.
    - Source: `View and delete the cache storage entries by selecting a storage. <a data-l10n-name="learn-more-link">Learn more</a>`
- `inactive-css-at-position-try-not-supported` — `devtools/client/tooltips.ftl` — { $property } is a CSS property, called a "kural" (rule) here.
    - Source: `<strong>{ $property }</strong> is not supported in <strong>@position-try</strong> rules.`
- `inactive-css-no-principal-box` — `devtools/client/tooltips.ftl` — wrong subject: the tr says the property does not create a principal box / is a ruby element; en says the element is.
    - Source: `<strong>{ $property }</strong> has no effect on this element since it does not create a principal box.`
- `inactive-css-ruby-element` — `devtools/client/tooltips.ftl` — wrong subject: the tr says the property does not create a principal box / is a ruby element; en says the element is.
    - Source: `<strong>{ $property }</strong> has no effect on this element since it is a ruby element. Its size is determined by the font size of the ruby text.`
- `console-stacktrace` — `mobile/android/mobile/android/geckoViewConsole.ftl` — missing ablative for en "Stack trace from { $filename }".
    - Source: `Stack trace from { $filename }, function { $functionName }, line { $lineNumber }.`
- `cert-format-base64-chain` — `security/manager/security/certificates/certManager.ftl` — "with chain" dropped; each is now byte-identical to its non-chain sibling, so the two export formats cannot be told apart.
    - Source: `X.509 Certificate with chain (PEM)`
- `cert-format-pkcs7-chain` — `security/manager/security/certificates/certManager.ftl` — "with chain" dropped; each is now byte-identical to its non-chain sibling, so the two export formats cannot be told apart.
    - Source: `X.509 Certificate with chain (PKCS#7)`
- `exception-mgr-supplemental-warning` — `security/manager/security/certificates/certManager.ftl` — "Legitimate" dropped; the whole point of the warning is that legitimate sites never ask this.
    - Source: `Legitimate banks, stores, and other public sites will not ask you to do this.`
- `pk11-bad-password` — `security/manager/security/certificates/certManager.ftl` — "Geçerli parola girişi hatalı" introduces a "current password" notion absent from en "The password entered was incorrect."
    - Source: `The password entered was incorrect.`
- `devmgr-button-unload` — `security/manager/security/certificates/deviceManager.ftl` — "Boşalt" (empty/pour out) → "Kaldır" (en "Unload" a PKCS#11 module).
    - Source: `accesskey: U label: Unload`
    - Suggest: `"Kaldır"`
- `load-device` — `security/manager/security/certificates/deviceManager.ftl` — "PKCS #11" with a space; en and the file's own load-device-modname-default / load-pk11-module-file-picker-title use "PKCS#11".
    - Source: `title: Load PKCS#11 Device Driver`
- `pippki-pw-change2empty-in-fips-mode` — `security/manager/security/pippki/pippki.ftl` — adds "ana" (Primary) where en says only "a non-empty password"; this is the security-device password dialog.
    - Source: `You are currently in FIPS mode. FIPS requires a non-empty password.`
- `details-notification-soft-blocked-other-disabled` — `toolkit/toolkit/about/aboutAddons.ftl` — this is the add-on ("other") variant but says "Uzantıyı"; …-disabled2 correctly says "Eklentiyi".
    - Source: `message: This add-on is restricted for violating Mozilla’s policies and has been disabled. You can enable it, but this may be risky.`
- `plugins-openh264-description` — `toolkit/toolkit/about/aboutAddons.ftl` — stale http://www.openh264.org/; en specifies https://.
    - Source: `This plugin is automatically installed by Mozilla to comply with the WebRTC specification and to enable WebRTC calls with devices that require the H.264 video codec. Visit https://www.openh264.org/ to view the codec sou…`
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
- `profile-directory-explanation` — `toolkit/toolkit/global/createProfileWizard.ftl` — "yer imleriniz ve parolalarınız" is not in en ("preferences and other user-related data").
    - Source: `Your user settings, preferences and other user-related data will be stored in:`
- `csp-error-illegal-protocol` — `toolkit/toolkit/global/cspErrors.ftl` — the colon belongs to { $scheme }: "yasaklı bir { $scheme } içeriyor: protokol kaynağı" → "yasaklı bir { $scheme }: protokol kaynağı içeriyor".
    - Current: `{ $scheme }`
    - Source: `‘{ $directive }’ directive contains a forbidden { $scheme }: protocol source`
    - Suggest: `"yasaklı bir { $scheme }: protokol kaynağı içeriyor".`
- `language-name-ab` — `toolkit/toolkit/intl/languageNames.ftl` — Abkhazian — Abazaca — Abhazca — Abaza (abq) is a different language.
    - Source: `Abkhazian`
- `language-name-gd` — `toolkit/toolkit/intl/languageNames.ftl` — Scottish Gaelic — İskoçça — İskoç Gaelcesi — "İskoçça" is Scots — already language-name-sco.
    - Source: `Scottish Gaelic`
- `language-name-gl` — `toolkit/toolkit/intl/languageNames.ftl` — Galician — Galce — Galiçyaca — "Galce" is Welsh — and is already language-name-cy. Two languages, one name.
    - Source: `Galician`
- `language-name-jv` — `toolkit/toolkit/intl/languageNames.ftl` — Javanese — Cava dili — Cava Dili — every other "… Dili" entry is capitalized.
    - Source: `Javanese`
- `language-name-kab` — `toolkit/toolkit/intl/languageNames.ftl` — Kabyle — Berberice — Kabilce — "Berberice" names the whole Berber family.
    - Source: `Kabyle`
- `language-name-nn` — `toolkit/toolkit/intl/languageNames.ftl` — Norwegian Nynorsk — Norveççe (Nynorsk) — Norveççe Nynorsk — sibling -nb is "Norveççe Bokmål", no parentheses.
    - Source: `Norwegian Nynorsk`
- `language-name-se` — `toolkit/toolkit/intl/languageNames.ftl` — Northern Sami — Nord Sami — Kuzey Samicesi — "Nord" is not Turkish.
    - Source: `Northern Sami`
- `language-name-si` — `toolkit/toolkit/intl/languageNames.ftl` — Sinhala — Seylanca — Sinhalaca — outdated exonym from "Ceylon".
    - Source: `Sinhala`
- `region-name-bl` — `toolkit/toolkit/intl/regionNames.ftl` — Saint Barthélemy — Saint Barthelemy — Saint Barthélemy — diacritic dropped.
    - Source: `Saint Barthélemy`
- `region-name-cy` — `toolkit/toolkit/intl/regionNames.ftl` — Cyprus — Güney Kıbrıs Rum Kesimi — Kıbrıs — en is the plain ISO 3166 country name; the current string names a different political entity.
    - Source: `Cyprus`
- `region-name-nr` — `toolkit/toolkit/intl/regionNames.ftl` — Nauru — Nauruca — Nauru — "Nauruca" is the language, already language-name-na.
    - Source: `Nauru`
- `region-name-re` — `toolkit/toolkit/intl/regionNames.ftl` — Réunion — Reunion — Réunion — diacritic dropped (present in en).
    - Source: `Réunion`
- `region-name-to` — `toolkit/toolkit/intl/regionNames.ftl` — Tonga — Tongaca — Tonga — "Tongaca" is the language, already language-name-to.
    - Source: `Tonga`
- `region-name-xu` — `toolkit/toolkit/intl/regionNames.ftl` — Johnston Atoll — Johnston Atoll — Johnston Atolü — untranslated; the parallel region-name-xl is "Palmyra Atolü".
    - Source: `Johnston Atoll`
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
- `ssl-error-bad-client` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-bad-client, ssl-error-bad-server — locative for en "from the client/server": "istemcide" → "istemciden gelen".
    - Source: `The server has encountered bad data from the client.`
    - Suggest: `"istemciden gelen".`
- `ssl-error-bad-server` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-bad-client, ssl-error-bad-server — locative for en "from the client/server": "istemcide" → "istemciden gelen".
    - Source: `The client has encountered bad data from the server.`
    - Suggest: `"istemciden gelen".`
- `ssl-error-handshake-failure-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — "kabul edilebilir sayıda güvenlik değişkeniyle" ≠ en "an acceptable set of security parameters".
    - Source: `SSL peer was unable to negotiate an acceptable set of security parameters.`
- `ssl-error-md5-digest-failure` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-md5-digest-failure, ssl-error-sha-digest-failure — "derleme" (compilation) → "özet" (en "digest"); sec-error-digest-not-found already uses "özet".
    - Source: `MD5 digest function failed.`
- `ssl-error-sha-digest-failure` — `toolkit/toolkit/neterror/nsserrors.ftl` — ssl-error-md5-digest-failure, ssl-error-sha-digest-failure — "derleme" (compilation) → "özet" (en "digest"); sec-error-digest-not-found already uses "özet".
    - Source: `SHA-1 digest function failed.`
- _…and 2 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `about-logins-confirm-remove-all-sync-dialog-title` — `browser/browser/aboutLogins.ftl` — the singular variant reads "{ $count } hesap hepsi tüm cihazlardan kaldırılsın mı?"; "hepsi" is copied from the plural variant and is ungrammatical here.
    - Source: `{$count ->} [one] Remove { $count } login from all devices? [other] Remove all { $count } logins from all devices?`
- `backup-folder-name` — `browser/browser/backupSettings.ftl` — Geri Yukleme — Geri Yükleme
    - Source: `Restore { -brand-product-name }`
- `callout-firefox-view-tab-pickup-title` — `browser/browser/featureCallout.ftl` — Sekma taşıma — Sekme taşıma
    - Source: `Hop between devices with tab pickup`
- `firefox-relay-must-login-to-fxa` — `browser/browser/firefoxRelay.ftl` — kullanak için — kullanmak için
    - Source: `You must log in to { -fxaccount-brand-name } in order to use { -relay-brand-name }.`
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — Favorileri siteleriniz — Favori siteleriniz
    - Source: `Your favorites at your fingertips`
- `newtab-sports-widget-message-survey-body` — `browser/browser/newtab/newtab.ftl` — Dünya Kupaları sona erdi — Dünya Kupası sona erdi (singular; verb disagrees)
    - Source: `That’s a wrap on the World Cup. Share your feedback on the experience.`
- `newtab-weather-menu-temperature-option-celsius` — `browser/browser/newtab/newtab.ftl` — Celcius — Celsius
    - Source: `Celsius`
- `onboarding-refresh-import-subtitle` — `browser/browser/newtab/onboarding.ftl` — "geçmişinizi ve ve diğer" — "…ve diğer"
    - Source: `Bring over your passwords, bookmarks, history and more.`
- `pane-experimental-description4` — `browser/browser/preferences/preferences.ftl` — oldıkları — oldukları
    - Source: `Give our experimental features a try! They’re in development and evolving, which could impact how { -brand-short-name } works. We only receive data about your use of these features if you have <a data-l10n-name="data-co…`
- `preferences-copy-profile-header` — `browser/browser/preferences/preferences.ftl` — parolarar — parolalar
    - Source: `description: The new profile will copy your settings, add-ons, history, and saved data like bookmarks and passwords — but not your account or sync info. label: Copy an existing profile`
- `preferences-etp-advanced-settings-group` — `browser/browser/preferences/preferences.ftl` — "çoğu takip kodunu olarak engelleyerek" — "…otomatik olarak engelleyerek" (word dropped)
    - Source: `description: Sites use trackers to follow you online and show creepy ads. { -brand-short-name } shields you as you browse, blocking most trackers automatically so you’re in control of your digital trail. label: Advanced…`
- `space-alert-over-5gb-message2` — `browser/browser/preferences/preferences.ftl` — kulllanılabilen — kullanılabilen
    - Source: `<strong>{ -brand-short-name } is running out of disk space.</strong> Website contents may not display properly. You can clear stored data in Settings > Privacy & Security > Cookies and Site Data.`
- `space-alert-under-5gb-message2` — `browser/browser/preferences/preferences.ftl` — kulllanılabilen … deneyimi içi — kullanılabilen … için
    - Source: `<strong>{ -brand-short-name } is running out of disk space.</strong> Website contents may not display properly. Visit “Learn more” to optimize your disk usage for better browsing experience.`
- `site-data-settings-description` — `browser/browser/preferences/siteDataSettings.ftl` — "bilgisayarınızda ve çerez ve site verisi" — stray "ve"
    - Source: `The following websites store cookies and site data on your computer. { -brand-short-name } keeps data from websites with persistent storage until you delete it, and deletes data from websites with non-persistent storage…`
- `restored-profile-page-learn-more` — `browser/browser/profiles.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
    - Source: `Learn more`
- `monitor-partial-breaches-motivation-description` — `browser/browser/protections.ftl` — ihallerinizi — ihlallerinizi
    - Source: `Resolve the rest of your breaches on { -monitor-brand-short-name }.`
- `protections-panel-description-shim-allowed-learn-more` — `browser/browser/protectionsPanel.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
    - Source: `Learn more`
- `report-broken-site-panel-intro-text` — `browser/browser/reportBrokenSite.ftl` — extra "için" after a dative that is already the complement of "yardımcı oluyor".
    - Source: `Your report helps us understand and fix issues in { -brand-product-name } to make it better for everyone.`
- `existing-user-tou-learn-more` — `browser/browser/termsofuse.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
    - Source: `Learn more`
- `translations-panel-learn-more-link` — `browser/browser/translations.ftl` — "Learn more" rendered as the informal singular "Daha fazla bilgi al" where the locale otherwise uses "Daha fazla bilgi alın": protections-panel-description-shim-allowed-learn-more (browser/protectionsPanel.ftl), restored-profile-page-learn-more (browser/profiles.ftl), translations-panel-learn-more-link (browser/translations.ftl), existing-user-tou-learn-more (browser/termsofuse.ftl). (The locale…
    - Source: `Learn more`
- `webrtc-reason-for-no-permanent-allow-audio` — `browser/browser/webrtcIndicator.ftl` — paylacağınızı — paylaşacağınızı
    - Source: `{ -brand-short-name } can not allow permanent access to your tab’s audio without asking which tab to share.`
- `styleeditor-filter-input` — `devtools/client/styleeditor.ftl` — Stil dosyalarını filtrelere — …filtrele
    - Source: `placeholder: Filter style sheets`
- `whypaused-breakpoint` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
    - Source: `Paused on breakpoint`
- `whypaused-event-breakpoint` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
    - Source: `Paused on event breakpoint`
- `whypaused-promise-rejection` — `devtools/shared/debugger-paused-reasons.ftl` — the identical en pattern "Paused on X" takes three different verb forms in one file.
    - Source: `Paused on promise rejection`
- `file-browse-pkcs12-spec` — `security/manager/security/certificates/certManager.ftl` — PKSC12 — PKCS12
    - Source: `PKCS12 Files`
- `profiles-rename` — `toolkit/toolkit/about/aboutProfiles.ftl` — değiștir (U+0219, Romanian s-comma) — değiştir (U+015F)
    - Source: `Rename`
- `rights-webservices-term-7` — `toolkit/toolkit/about/aboutRights.ftl` — ihtilafi — ihtilafı
    - Source: `These terms are governed by the laws of the state of California, U.S.A., excluding its conflict of law provisions. If any portion of these terms is held to be invalid or unenforceable, the remaining portions will remain…`
- `media-capabilities-title` — `toolkit/toolkit/about/aboutSupport.ftl` — Çoku ortam — Çoklu ortam
    - Source: `Media Capabilities`
- `place-database-last-integrity-corruption-date` — `toolkit/toolkit/about/aboutSupport.ftl` — sütünlük — bütünlük
    - Source: `Last Integrity Corruption Date`
- `privacy-spoof-english` — `toolkit/toolkit/global/resistFingerPrinting.ftl` — değştirmek — değiştirmek
    - Source: `Changing your language setting to English will make you more difficult to identify and enhance your privacy. Do you want to request English language versions of web pages?`
- `sec-error-not-fortezza-issuer` — `toolkit/toolkit/neterror/nsserrors.ftl` — "zinciri has FORTEZZA olmayan" — stray English word "has"
    - Source: `Peer FORTEZZA chain has a non-FORTEZZA Certificate.`
- `ssl-error-cert-kea-mismatch` — `toolkit/toolkit/neterror/nsserrors.ftl` — anahtar değiş algoritması — anahtar değişim algoritması
    - Source: `The certificate provided cannot be used with the selected key exchange algorithm.`
- `elevation-error-manual` — `toolkit/toolkit/updates/elevation.ftl` — "ziyaretip edip" — "ziyaret edip"
    - Source: `You can update { -brand-short-name } manually by visiting this link and downloading the latest version:`

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
- `reset-pbm-panel-description` — `browser/browser/browser.ftl` — "özel sekmeleri" vs "gizli" used for "private" everywhere, including reset-pbm-panel-description2 right above.
    - Source: `Close all private tabs and delete history, cookies, and all other site data.`
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
- `newtab-clock-widget-input-nickname` — `browser/browser/newtab/newtab.ftl` — ".label = Ad" for en "Nickname"; newtab-clock-widget-edit-item-with-nickname uses "takma adı", and plain "Ad" collides with a real name field (the dev comment warns about this).
    - Source: `aria-label: Nickname (optional) label: Nickname (optional) placeholder: Add a nickname`
- `newtab-sports-widget-match-aria-label-upcoming-suspended` — `browser/browser/newtab/newtab.ftl` — "ara verildi" vs the status string newtab-sports-widget-suspended "Askıya alındı".
    - Source: `aria-label: { $homeTeam } vs. { $awayTeam }, suspended`
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Mobil cihazla eşitle” but the string it names, `sync-to-mobile-button-label`, reads “Mobil cihazla eşitleyin”
    - Current: `{ -brand-product-name } uygulamasını mobil cihazınıza indirmek için QR kodunu okutun. İndirdikten sonra parolalarınıza, yer imlerinize ve diğer bilgilerinize erişmek için “Mobil cihazla eşitle” seçeneğini seçin.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Mobil cihazla eşitleyin`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `places-view-sortby-name` — `browser/browser/places.ftl` — "İsme göre sırala" vs places-sortby-name "Ada göre sırala" for the same en string in the same file.
    - Source: `accesskey: N label: Sort by Name`
- `add-engine-dialog` — `browser/browser/preferences/addEngine.ftl` — see also S4.
    - Source: `buttonaccesskeyaccept: A buttonlabelaccept: Add Engine`
- `autofill-add-new-address-title` — `browser/browser/preferences/formAutofill.ftl` — see also S4.
    - Source: `Add New Address`
- `autofill-addresses-add-button` — `browser/browser/preferences/preferences.ftl` — see also S4.
    - Source: `Add new address`
- `preferences-ai-controls-translations-control` — `browser/browser/preferences/preferences.ftl` — "Çeviri" vs "Çeviriler" everywhere else.
    - Source: `description: Seamlessly browse the web in your preferred language. label: Translations`
- `preferences-text-zoom-override-warning2` — `browser/browser/preferences/preferences.ftl` — quotes the option as "Yalnızca metni yakınlaştır" but its actual label preferences-zoom-text-only is "Sadece metni yakınlaştır".
    - Source: `message: If “Zoom text only” is on and your default zoom isn’t 100%, some sites might not display content correctly.`
- `remove-engine-remove` — `browser/browser/preferences/preferences.ftl` — "Sil" vs the triggering control search-remove-engine "Kaldır".
    - Source: `Remove`
- `security-privacy-issue-warning-safe-browsing` — `browser/browser/preferences/preferences.ftl` — "yanıltıcı" vs "aldatıcı" used for en "deceptive" in security-enable-safe-browsing, security-browsing-protection, browsing-protection-group2.
    - Source: `description: Your exposure to scams and malware from websites is increased. label: Dangerous and deceptive content is not blocked`
- `profiles-cyan-theme-title` — `browser/browser/profiles.ftl` — tooltip says "Cyan temayı uygula" but the theme's own label profiles-cyan-theme is "Açık mavi".
    - Source: `title: Apply cyan theme`
- `safeb-blocked-unwanted-page-learn-more` — `browser/browser/safebrowsing/blockedSite.ftl` — "kötü amaçlı yazılım" vs "zararlı yazılım" in the three sibling strings.
    - Source: `Learn more about harmful and unwanted software at <a data-l10n-name='learn_more_link'>Unwanted Software Policy</a>. Learn more about { -brand-short-name }’s Phishing and Malware Protection at <a data-l10n-name='firefox_…`
- `add-engine-dialog2` — `browser/browser/search.ftl` — see also S4.
    - Source: `buttonaccesskeyaccept: A buttonlabelaccept: Add Engine buttonlabelextra1: Advanced`
- `styleeditor-filter-input` — `devtools/client/styleeditor.ftl` — "stil dosyası" vs "stil sayfası" for stylesheet in adjacent strings.
    - Source: `placeholder: Filter style sheets`
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
- `xslt-call-to-key-not-allowed` — `dom/dom/xslt.ftl` — "işlev" vs "fonksiyon" used in xpath-unknown-function, xpath-bad-argument-count, xpath-bad-extension-function; also "the key function" is the XSLT key() function name, not a generic "anahtar işlev".
    - Source: `Call to the key function not allowed.`
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
- `fips-nonempty-primary-password-required` — `security/manager/security/certificates/deviceManager.ftl` — "güvenlik cihazı" vs "güvenlik aygıtı" used in devmgr-window, unable-to-toggle-fips, pkcs12-dup-data, certmgr-token-name, change-password-token.
    - Source: `FIPS mode requires that you have a Primary Password set for each security device. Please set the password before trying to enable FIPS mode.`
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
- `webext-perms-update-text2` — `toolkit/toolkit/global/extensions.ftl` — quotes the Cancel button as "İptal", but it is labelled webext-perms-cancel = "Vazgeç"; webext-perms-update-text gets it right.
    - Source: `{ $extension } has been updated. You must approve new permissions before the updated version will install. Choosing “Cancel” will maintain your current extension version.`
- `wizard-macos-button-next` — `toolkit/toolkit/global/wizard.ftl` — "İleri" for the macOS "Continue" variant, while profile-creation-explanation-4 tells macOS users to press "Devam düğmesine".
    - Source: `accesskey: C label: Continue`
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
- `pin-tabs-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Drag a tab to the start of the tab strip to pin it. Or right-click and choose Pin Tab.`
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `To pin any tab, drag it to the start of the tab strip. Or right-click and choose Pin Tab.`
- `menu-view-enter-readerview` — `browser/browser/menubar.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `accesskey: R label: Enter Reader View`
- `import-safari-permissions-string` — `browser/browser/migration.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `macOS requires you to explicitly allow { -brand-short-name } to access Safari’s data. Click “Continue”, select the “Safari“ folder in the Finder dialog that appears and then click “Open”.`
- `mr2022-onboarding-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
- `tab-groups-onboarding-create-group-title-3` — `browser/browser/newtab/onboarding.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Find your tab groups in the List All Tabs menu anytime.`
- `tab-groups-onboarding-saved-groups-title-3` — `browser/browser/newtab/onboarding.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `When you close a tab group, reopen it from the List All Tabs menu anytime.`
- `tab-groups-onboarding-session-restore-title-2` — `browser/browser/newtab/onboarding.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Reopen your tab groups from the List All Tabs menu anytime.`
- `policy-DisableSafeMode` — `browser/browser/policies/policies-descriptions.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `Disable the feature to restart in Safe Mode. Note: the Shift key to enter Safe Mode can only be disabled on Windows using Group Policy.`
- `policy-FirefoxHome2` — `browser/browser/policies/policies-descriptions.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `Configure { -firefox-home-brand-name }.`
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `label: { $name } (Default) tooltiptext: Use the default URL for resolving DNS over HTTPS`
- `connection-proxy-noproxy-localhost-desc-2` — `browser/browser/preferences/connection.ftl` — serial comma before "ve" carried over from English: "127.0.0.1/8, ve ::1" → "127.0.0.1/8 ve ::1".
    - Source: `Connections to localhost, 127.0.0.1/8, and ::1 are never proxied.`
- `permissions-block-popups-exceptions-button4` — `browser/browser/preferences/preferences.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `accesskey: E description: Add websites that can open pop-ups and use third-party redirects. label: Manage exceptions searchkeywords: popups`
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `{$count ->} [other] Using the { -mozilla-vpn-brand-name } encrypts all your traffic and hides your location — on up to { $count } devices. Get the most from your subscription — add it from the <a data-l10n-name="playsto…`
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
- `set-password-reminder` — `security/manager/security/pippki/pippki.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `Important: If you forget your certificate backup password, you will not be able to restore this backup later. Please record it in a safe location.`
- `about-glean-label-for-tag-pings-with-requirements` — `toolkit/toolkit/about/aboutGlean.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `Set a memorable debug tag <span>(20 characters or fewer, alphanumerics and - only)</span> so you can recognize your pings later.`
- `about-logging-invalid-output` — `toolkit/toolkit/about/aboutLogging.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Invalid value “{ $v }“ for key “{ $k }“`
- `about-logging-unknown-logging-preset` — `toolkit/toolkit/about/aboutLogging.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Unknown logging preset “{ $v }“`
- `about-logging-unknown-option` — `toolkit/toolkit/about/aboutLogging.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Unknown about:logging option “{ $k }“`
- `about-logging-unknown-profiler-preset` — `toolkit/toolkit/about/aboutLogging.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Unknown profiler preset “{ $v }“`
- `profiles-delete-profile-confirm` — `toolkit/toolkit/about/aboutProfiles.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `Deleting a profile will remove the profile from the list of available profiles and cannot be undone. You may also choose to delete the profile data files, including your settings, certificates and other user-related dat…`
- `profiles-opendir` — `toolkit/toolkit/about/aboutProfiles.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
- `rights-intro-point-3` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `Some features in { -brand-short-name }, such as the Crash Reporter, give you the option to provide feedback to { -vendor-short-name }. By choosing to submit feedback, you give { -vendor-short-name } permission to use th…`
- `rights-intro-point-4` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `How we use your personal information and feedback submitted to { -vendor-short-name } through { -brand-short-name } is described in the <a data-l10n-name="mozilla-privacy-policy-link">{ -brand-short-name } Privacy Polic…`
- `rights-webservices-term-1` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{ -vendor-short-name } and its contributors, licensors and partners work to provide the most accurate and up-to-date Services. However, we cannot guarantee that this information is comprehensive and error-free. For exam…`
- `rights-webservices-term-3` — `toolkit/toolkit/about/aboutRights.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `You are welcome to use these Services with the accompanying version of { -brand-short-name }, and { -vendor-short-name } grants you its rights to do so. { -vendor-short-name } and its licensors reserve all other rights…`
- `rights-webservices-term-4` — `toolkit/toolkit/about/aboutRights.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `<strong>The Services are provided “as-is.” { -vendor-short-name }, its contributors, licensors, and distributors, disclaim all warranties, whether express or implied, including without limitation, warranties that the Se…`
- `rights-webservices-term-5` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `<strong>Except as required by law, { -vendor-short-name }, its contributors, licensors, and distributors will not be liable for any indirect, special, incidental, consequential, punitive, or exemplary damages arising ou…`
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{ -vendor-short-name } may update these terms as necessary from time to time. These terms may not be modified or canceled without { -vendor-short-name }’s written agreement.`
- `show-dir-label` — `toolkit/toolkit/about/aboutSupport.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `{$sel_1 ->} [macos] Show in Finder [windows] Open Folder [other] Open Directory`
- `about-telemetry-data-details-current` — `toolkit/toolkit/about/aboutTelemetry.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Each piece of information is sent bundled into “<a data-l10n-name="ping-link">pings</a>“. You are looking at the current data.`
- `about-telemetry-data-details-current` — `toolkit/toolkit/about/aboutTelemetry.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `Each piece of information is sent bundled into “<a data-l10n-name="ping-link">pings</a>“. You are looking at the current data.`
- `about-webrtc-save-page-dialog-title` — `toolkit/toolkit/about/aboutWebrtc.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `save about:webrtc as`
- `experimental-features-link-previews-description-no-ai` — `toolkit/toolkit/firefoxlabs/features.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `{$sel_1 ->} [macos] To learn more about a webpage before you click, hover over a link and press Shift (⇧) plus Option (⌥) or Alt. Previews can include details like title and reading time. <a data-l10n-name="connect">Sha…`
- `experimental-features-media-jxl-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — reader-view-enter-button.aria-label (browser/browser.ftl), menu-view-enter-readerview.label (browser/menubar.ftl), connection-dns-over-https-url-item-default.tooltiptext (browser/preferences/connection.ftl), policy-DisableSafeMode, policy-FirefoxHome2 (browser/policies/policies-descriptions.ftl), about-glean-label-for-tag-pings-with-requirements (toolkit/about/aboutGlean.ftl), profiles-opendir (t…
    - Source: `With this feature enabled, { -brand-short-name } supports the JPEG XL (JXL) format. This is an enhanced image file format that supports lossless transition from traditional JPEG files. See <a data-l10n-name="bugzilla">b…`
- `csp-xfo-blocked-long-desc` — `toolkit/toolkit/neterror/certError.ftl` — set-password-reminder (security/…/pippki.ftl), protections-vpn-header-content-subscribed (browser/protections.ftl), permissions-block-popups-exceptions-button4.description (browser/preferences/preferences.ftl), mr2022-onboarding-pin-primary-button-label [macos variant] (browser/newtab/onboarding.ftl), profiles-delete-profile-confirm (toolkit/about/aboutProfiles.ftl), rights-webservices-term-3, ri…
    - Source: `To protect your security, { $hostname } will not allow { -brand-short-name } to display the page if another site has embedded it. To see this page, you need to open it in a new window.`
- `neterror-net-offline` — `toolkit/toolkit/neterror/netError.ftl` — pin-tabs-callout-1-subtitle, pin-tabs-callout-2-subtitle (browser/featureCallout.ftl); import-safari-permissions-string (browser/migration.ftl); tab-groups-onboarding-create-group-title-3, tab-groups-onboarding-saved-groups-title-3, tab-groups-onboarding-session-restore-title-2 (browser/newtab/onboarding.ftl); about-logging-invalid-output, about-logging-unknown-logging-preset, about-logging-unkno…
    - Source: `Press “Try Again” to switch to online mode and reload the page.`
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
