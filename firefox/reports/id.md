# Firefox l10n QA — id

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b95608d528c8` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 15,475 of 15,475 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (321)

- `account-tabs-closed-remotely` — `browser/browser/accounts.ftl` — `account-tabs-closed-remotely` has plural variant ['one'], which id does not have
  - Current: `{$closedCount ->} [one] { $closedCount } { -brand-short-name } tab ditutup [other] { $closedCount } { -brand-short-name } tabs ditutup`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `confirmation-hint-duplicate-tabs-closed` — `browser/browser/confirmationHints.ftl` — Post-action confirmation rendered as an imperative, plus untranslated "tabs"
  - Current: `Tutup { $tabCount } tabs`
  - en-US: `{ $tabCount } tab ditutup`
  - en-US "Closed { $tabCount } tabs" reports a completed action; "Tutup" is the imperative "Close". The English plural "tabs" is also left untranslated (Indonesian has no plural -s).
- `firefoxview-search-results-count` — `browser/browser/firefoxView.ftl` — `firefoxview-search-results-count` has plural variant ['one'], which id does not have
  - Current: `{$count ->} [one] { $count } situs [other] { $count } situs`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-new-bookmarks` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-new-bookmarks` has plural variant ['one'], which id does not have
  - Current: `{$newEntries ->} [one] { $newEntries } markah [other] { $newEntries } markah`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-bookmarks` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-bookmarks` has plural variant ['one'], which id does not have
  - Current: `{$quantity ->} [one] { $quantity } markah [other] { $quantity } markah`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-favorites` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-favorites` has plural variant ['one'], which id does not have
  - Current: `{$quantity ->} [one] { $quantity } favorit [other] { $quantity } favorit`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-extensions` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-extensions` has plural variant ['one'], which id does not have
  - Current: `{$quantity ->} [one] { $quantity } ekstensi [other] { $quantity } ekstensi`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `appmenu-help-not-deceptive` — `browser/browser/appmenu.ftl` — Access key `d` of `appmenu-help-not-deceptive` is not present in its label
  - Current: `d`
  - The label is “Ini bukan situs tipuan…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `bookmarks-toolbar` — `browser/browser/browser.ftl` — Access key `B` of `bookmarks-toolbar` is not present in its label
  - Current: `B`
  - The label is “Markah”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-forget-about-this-site` — `browser/browser/fxviewTabList.ftl` — Access key `F` of `fxviewtabrow-forget-about-this-site` is not present in its label
  - Current: `F`
  - The label is “Lupakan Situs Ini…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-move-tab` — `browser/browser/fxviewTabList.ftl` — Access key `V` of `fxviewtabrow-move-tab` is not present in its label
  - Current: `V`
  - The label is “Pindahkan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-move-tab-start` — `browser/browser/fxviewTabList.ftl` — Access key `S` of `fxviewtabrow-move-tab-start` is not present in its label
  - Current: `S`
  - The label is “Pindahkan ke Awal”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-move-tab-window` — `browser/browser/fxviewTabList.ftl` — Access key `W` of `fxviewtabrow-move-tab-window` is not present in its label
  - Current: `W`
  - The label is “Pindahkan ke Jendela Baru”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-pin-tab` — `browser/browser/fxviewTabList.ftl` — Access key `P` of `fxviewtabrow-pin-tab` is not present in its label
  - Current: `P`
  - The label is “Sematkan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-mute-tab` — `browser/browser/fxviewTabList.ftl` — Access key `M` of `fxviewtabrow-mute-tab` is not present in its label
  - Current: `M`
  - The label is “Senyapkan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-unmute-tab` — `browser/browser/fxviewTabList.ftl` — Access key `m` of `fxviewtabrow-unmute-tab` is not present in its label
  - Current: `m`
  - The label is “Bunyikan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `menu-help-not-deceptive` — `browser/browser/menubar.ftl` — Access key `d` of `menu-help-not-deceptive` is not present in its label
  - Current: `d`
  - The label is “Ini bukan situs tipuan…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `synced-tabs-context-manage-devices` — `browser/browser/syncedTabs.ftl` — Access key `D` of `synced-tabs-context-manage-devices` is not present in its label
  - Current: `D`
  - The label is “Kelola Perangkat…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `tabbrowser-context-unmute-selected-tabs` — `browser/browser/tabbrowser.ftl` — Access key `S` of `tabbrowser-context-unmute-selected-tabs` is not present in its label
  - Current: `S`
  - The label is “Bunyikan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `cfr-doorhanger-doh-secondary-button` — `browser/browser/newtab/asrouter.ftl` — Access key `D` of `cfr-doorhanger-doh-secondary-button` is not present in its label
  - Current: `D`
  - The label is “Nonaktifkan”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxa-sync-cfr-secondary` — `browser/browser/newtab/asrouter.ftl` — Access key `R` of `fxa-sync-cfr-secondary` is not present in its label
  - Current: `R`
  - The label is “Ingatkan saya nanti”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `safeb-palm-notdeceptive` — `browser/browser/safebrowsing/blockedSite.ftl` — Access key `d` of `safeb-palm-notdeceptive` is not present in its label
  - Current: `d`
  - The label is “Ini bukan situs tipuan…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `styleeditor-visibility-toggle` — `devtools/client/styleeditor.ftl` — Access key `S` of `styleeditor-visibility-toggle` is not present in its label
  - Current: `S`
  - The label is “Aktifkan/Nonaktifkan keterlihatan lembar gaya”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Malformed closing tag `</a >` in `genai-settings-chat-gemini-links`
  - Current: `Dengan memilih Google Gemini, Anda menyetujui <a data-l10n-name="link1">Persyaratan Layanan Google</a>, <a data-l10n-name="link2">Kebijakan Penggunaan Terlarang untuk AI Generatif</a >, dan <a data-l10n-name="link3">Pem…`
  - en-US: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
  - Whitespace inside a closing tag makes it render as literal text.
- `cfr-doorhanger-bookmark-fxa-close-btn-tooltip` — `browser/browser/newtab/asrouter.ftl` — The .title tooltip is the single letter “T” instead of a translation of “Close”.
  - Current: `.title = T`
  - en-US: `.title = Tutup`
  - en-US is “.title = Close”; the aria-label above it is correctly “Tombol tutup”. “T” appears to be a stray access-key-style fragment and renders as a meaningless one-letter tooltip.
- `policy-AutofillCreditCardEnabled` — `browser/browser/policies/policies-descriptions.ftl` — Transposed letters make the phrase nonsense: “osi ptomatis” instead of “isi otomatis”.
  - Current: `Aktifkan osi ptomatis untuk metode pembayaran.`
  - en-US: `Aktifkan isi otomatis untuk metode pembayaran.`
  - policy-AutofillAddressEnabled correctly uses “isi otomatis” for “autofill”; here the initial letters of the two words were swapped.
- `onboarding-live-language-installing` — `browser/browser/newtab/onboarding.ftl` — “Installing the language pack” is rendered as “Downloading”, duplicating the download string.
  - Current: `Mengunduh paket bahasa untuk { $negotiatedLanguage }…`
  - en-US: `Memasang paket bahasa untuk { $negotiatedLanguage }…`
  - en-US: “Installing the language pack for { $negotiatedLanguage }…”. The id text is identical to onboarding-live-language-button-label-downloading, so the install phase is reported as a download.
- `colorways-cfr-body` — `browser/browser/newtab/asrouter.ftl` — “shades” (colour shades) is translated as “bayangan” (shadows).
  - Current: `bayangan eksklusif { -brand-short-name }`
  - en-US: `corak warna eksklusif { -brand-short-name }`
  - The developer comment states that “shades” refers to the different colour options available in colorways, not to shadows.
- `newtab-empty-section-topstories` — `browser/browser/newtab/newtab.ftl` — “You’ve caught up.” is rendered as “Maaf Anda tercegat.” (“Sorry, you were intercepted.”).
  - Current: `Maaf Anda tercegat.`
  - en-US: `Anda sudah membaca semuanya.`
  - en-US “You’ve caught up.” means there is no more new content; “tercegat” (intercepted/blocked) conveys an unrelated and confusing meaning, and the added “Maaf” has no source.
- `newtab-discovery-empty-section-topstories-timed-out` — `browser/browser/newtab/newtab.ftl` — The sentence is self-contradictory and does not render “We almost loaded this section, but not quite.”
  - Current: `Ups! Kami belum selesai memuat bagian ini, tetapi ternyata belum.`
  - en-US: `Ups! Kami hampir selesai memuat bagian ini, tetapi belum berhasil.`
  - en-US says loading almost succeeded; the id text says “we have not finished loading this section, but apparently not yet”, which repeats the negation and reads as nonsense.
- `OPTIONS_SUMMARY` — `browser/installer/custom.properties` — The setup-type prompt is translated as a component-selection prompt.
  - Current: `Pilih komponen tambahan yang ingin Anda pasang, kemudian tekan Lanjut.`
  - en-US: `Pilih jenis pemasangan yang Anda inginkan, lalu klik Lanjut.`
  - en-US: “Choose the type of setup you prefer, then click Next.” The page offers Standard/Custom setup types, not a list of extra components.
- `OPTION_CUSTOM_RADIO` — `browser/installer/custom.properties` — “Custom” setup type is translated as “Kesukaan” (favourite/liking).
  - Current: `&Kesukaan`
  - en-US: `&Ubahsuai`
  - en-US “&Custom” pairs with “&Standard”; “Kesukaan” means “favourite/preference” and does not convey a custom installation. The tree uses “Ubahsuai”/“Khusus” for “custom” elsewhere (e.g. newtab-topsites-image-url-label “URL Gambar Khusus”).
- `CONTEXT_OPTIONS` — `browser/installer/custom.properties` — The “$BrandShortName Options” context-menu entry is rendered as “component options”.
  - Current: `&Pilihan komponen $BrandShortName`
  - en-US: `&Pilihan $BrandShortName`
  - en-US is “$BrandShortName &Options”, i.e. the browser's Options/preferences; “komponen” adds a meaning that is not in the source and misdescribes the command.
- `policy-DisplayMenuBar` — `browser/browser/policies/policies-descriptions.ftl` — “by default” is translated as “secara otomatis” (automatically).
  - Current: `Tampilkan Bilah Menu secara otomatis.`
  - en-US: `Tampilkan Bilah Menu secara baku.`
  - en-US: “Display the Menu Bar by default.” The immediately preceding policy-DisplayBookmarksToolbar correctly renders the same “by default” as “secara baku”.
- `policy-PopupBlocking` — `browser/browser/policies/policies-descriptions.ftl` — “by default” is translated as “secara otomatis” (automatically).
  - Current: `Izinkan situs tertentu untuk menampilkan pop-up secara otomatis.`
  - en-US: `Izinkan situs tertentu untuk menampilkan pop-up secara baku.`
  - en-US: “Allow certain websites to display popups by default.” The policy sets a default permission, it does not make popups appear automatically.
- `policy-EnableTrackingProtection` — `browser/browser/policies/policies-descriptions.ftl` — Uses the free pronoun “ia” as a direct object, which is ungrammatical in Indonesian.
  - Current: `kunci ia secara opsional`
  - en-US: `kuncilah secara opsional`
  - “ia” cannot function as an object; the enclitic “-nya” is required. Compare the parallel policy-EncryptedMediaExtensions, which has the same problem with “dia”.
- `policy-EncryptedMediaExtensions` — `browser/browser/policies/policies-descriptions.ftl` — Uses “dia” (a personal pronoun for people) to refer to a setting.
  - Current: `kunci dia secara opsional`
  - en-US: `kuncilah secara opsional`
  - “dia” refers to persons and cannot be used as an object pronoun for an inanimate setting; the enclitic “-nya” is required.
- `colorways-cfr-header-28days` — `browser/browser/newtab/asrouter.ftl` — “kedaluarsa” is misspelled; the standard form is “kedaluwarsa”.
  - Current: `kedaluarsa pada 16 Januari`
  - en-US: `kedaluwarsa pada 16 Januari`
  - KBBI spelling is “kedaluwarsa”, which the tree uses correctly elsewhere (newtab-report-content-outdated = “Kedaluwarsa”).
- `colorways-cfr-header-14days` — `browser/browser/newtab/asrouter.ftl` — “kedaluarsa” is misspelled; the standard form is “kedaluwarsa”.
  - Current: `kedaluarsa dalam dua minggu`
  - en-US: `kedaluwarsa dalam dua minggu`
  - KBBI spelling is “kedaluwarsa”, used correctly elsewhere in the tree.
- `colorways-cfr-header-7days` — `browser/browser/newtab/asrouter.ftl` — “kedaluarsa” is misspelled; the standard form is “kedaluwarsa”.
  - Current: `kedaluarsa minggu ini`
  - en-US: `kedaluwarsa minggu ini`
  - KBBI spelling is “kedaluwarsa”, used correctly elsewhere in the tree.
- `colorways-cfr-header-today` — `browser/browser/newtab/asrouter.ftl` — “kedaluarsa” is misspelled; the standard form is “kedaluwarsa”.
  - Current: `kedaluarsa hari ini`
  - en-US: `kedaluwarsa hari ini`
  - KBBI spelling is “kedaluwarsa”, used correctly elsewhere in the tree.
- `newtab-weather-menu-temperature-option-celsius` — `browser/browser/newtab/newtab.ftl` — The temperature unit is misspelled “Celcius”.
  - Current: `Celcius`
  - en-US: `Celsius`
  - The Indonesian spelling of the unit, like the English source, is “Celsius”; “Celcius” is a common misspelling.
- `newtab-weather-menu-change-temperature-units-celsius` — `browser/browser/newtab/newtab.ftl` — The temperature unit is misspelled “Celcius”.
  - Current: `Beralih ke Celcius`
  - en-US: `Beralih ke Celsius`
  - Same misspelling as newtab-weather-menu-temperature-option-celsius; the correct form is “Celsius”.
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — The quoted button name does not match the actual translated button label.
  - Current: `pilih “Sinkronkan ke seluler”`
  - en-US: `pilih “Sinkronkan ke ponsel”`
  - The quoted string refers to sync-to-mobile-button-label, which is translated as “Sinkronkan ke ponsel”; users are told to look for a control that does not exist under that name.
- `MUI_TEXT_FINISH_SUBTITLE` — `browser/installer/mui.properties` — “Setup was completed successfully.” is rendered as “Setup was successfully installed.”
  - Current: `Setup telah berhasil dipasang.`
  - en-US: `Penyiapan berhasil diselesaikan.`
  - en-US says the setup process finished; the id text says the setup program itself was installed, which is not what happened.
- `newtab-wallpaper-category-title-colors` — `browser/browser/newtab/newtab.ftl` — “Solid colors” is rendered as “Warna-warni rata” (assorted/multicoloured flat colours).
  - Current: `Warna-warni rata`
  - en-US: `Warna solid`
  - The reduplicated “warna-warni” means “multicoloured/assorted”, the opposite of the single solid colours this category contains.
- `mr2022-onboarding-mobile-download-image-alt` — `browser/browser/newtab/onboarding.ftl` — “lily pads” is translated as “bunga bakung” (lily flowers).
  - Current: `Katak melompat melintasi bunga bakung`
  - en-US: `Katak melompat melintasi daun teratai`
  - Lily pads are the floating leaves of a water lily (“daun teratai”), not the “bakung” lily flower; the alt text describes the wrong image for screen-reader users.
- `amo-picker-subtitle` — `browser/browser/newtab/onboarding.ftl` — “browser” is left in English twice where the file consistently uses “peramban”.
  - Current: `Ekstensi adalah seperti aplikasi untuk browser Anda`
  - en-US: `Ekstensi adalah seperti aplikasi untuk peramban Anda`
  - Every other occurrence of “browser” in this file is translated as “peramban” (e.g. mr1-return-to-amo-addon-title, mr2-onboarding-thank-you-text); leaving it untranslated here is inconsistent with the locale's established term.
- `newtab-pocket-cta-text` — `browser/browser/newtab/newtab.ftl` — The polite pronoun “Anda” is written in lowercase.
  - Current: `cerita yang anda sukai`
  - en-US: `cerita yang Anda sukai`
  - Indonesian orthography (and the rest of this file, including the second half of this same string) capitalises “Anda”.
- `site-data-settings-description` — `browser/browser/preferences/siteDataSettings.ftl` — "The following websites" rendered as "this website" (singular, deictic)
  - Current: `Situs web ini menyimpan kuki dan data situs pada komputer Anda.`
  - en-US: `Situs web berikut menyimpan kuki dan data situs pada komputer Anda.`
  - en-US is "The following websites store cookies and site data on your computer" — it introduces the list below. "Situs web ini" means "this website", pointing at nothing and losing the reference to the list.
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — "resolving DNS" mistranslated as "troubleshooting DNS problems"
  - Current: `Gunakan URL baku untuk memecahkan masalah DNS atas HTTPS`
  - en-US: `Gunakan URL baku untuk meresolusi DNS lewat HTTPS`
  - "Resolving DNS over HTTPS" is DNS name resolution, not troubleshooting; "memecahkan masalah" means "solve a problem". The sibling string connection-dns-over-https-url-custom correctly uses "mendapatkan DNS lewat HTTPS".
- `autofill-address-post-town` — `browser/browser/preferences/formAutofill.ftl` — "Post town" rendered as "city code"
  - Current: `Kode kota`
  - en-US: `Kota pos`
  - "Post town" (GB/NO/SE) is the town name used in a postal address, not a numeric code; "Kode kota" means "city code" and collides conceptually with autofill-address-postal-code ("Kode Pos").
- `fonts-langgroup-simpl-chinese` — `browser/browser/preferences/fonts.ftl` — Country name "Tiongkok" used instead of the language/script name
  - Current: `Tiongkok Sederhana`
  - en-US: `Tionghoa Sederhana`
  - In Indonesian, "Tiongkok" is the country China; the language/script is "Tionghoa" (bahasa/aksara Tionghoa). The label names a font language group, so it must name the language, not the country.
- `fonts-langgroup-trad-chinese` — `browser/browser/preferences/fonts.ftl` — Country name "Tiongkok" used instead of the language/script name
  - Current: `Tiongkok Tradisional (Taiwan)`
  - en-US: `Tionghoa Tradisional (Taiwan)`
  - "Tiongkok" is the country China; the language/script name in Indonesian is "Tionghoa".
- `fonts-langgroup-trad-chinese-hk` — `browser/browser/preferences/fonts.ftl` — Country name "Tiongkok" used instead of the language/script name
  - Current: `Tiongkok Tradisional (Hong Kong)`
  - en-US: `Tionghoa Tradisional (Hong Kong)`
  - "Tiongkok" is the country China; the language/script name in Indonesian is "Tionghoa".
- `fonts-langgroup-thai` — `browser/browser/preferences/fonts.ftl` — Country "Thailand" used instead of the language name "Thai"
  - Current: `Thailand`
  - en-US: `Thai`
  - The entry names a font language group (Thai). In Indonesian the language is "bahasa Thai"; "Thailand" is the country, matching the wrong-name category (country instead of language).
- `fonts-langgroup-ethiopic` — `browser/browser/preferences/fonts.ftl` — Script name "Ethiopic" rendered as the country, spelled in English
  - Current: `Ethiopia`
  - en-US: `Etiopik`
  - "Ethiopic" is the writing system (Ge'ez script), not the country; additionally the Indonesian spelling of the country is "Etiopia", not the English "Ethiopia".
- `containers-name-text` — `browser/browser/preferences/containers.ftl` — "Masukan" (noun: input) used where the imperative verb "Masukkan" is required
  - Current: `Masukan nama kontainer`
  - en-US: `Masukkan nama kontainer`
  - The imperative of "memasukkan" is "masukkan" with double k; "masukan" is the noun "input/feedback". Other files in this partition use the correct form (e.g. permissions-doh-entry-field "Masukkan nama domain situs web").
- `fonts-allow-own` — `browser/browser/preferences/fonts.ftl` — "daripada" written as two words
  - Current: `dari pada menggunakan pilihan Anda di atas`
  - en-US: `daripada menggunakan pilihan Anda di atas`
  - In standard Indonesian orthography the comparative conjunction is written as one word, "daripada".
- `autofill-edit-card-password-prompt` — `browser/browser/preferences/formAutofill.ftl` — macOS variant adds a period the OS also appends
  - Current: `[macos] menampilkan informasi kartu kredit.`
  - en-US: `[macos] menampilkan informasi kartu kredit`
  - The developer comment states macOS prepends "Firefox is trying to " and adds a period at the end; en-US therefore has no final period. The localized variant ends with one, producing a double period in the OS dialog.
- _…and 261 more._

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
| Files | 353 |
| Strings | 15,475 |
| Missing strings | 2,688 |
| Obsolete strings | 0 |
| Files absent from the locale | 7 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 7 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 16 |
| Markup & `data-l10n-name` defects | 1 |
| Typography deviations from this locale's own norm | 98 |

### Completeness

**2,688 strings** are not translated yet, concentrated in:

- `browser/browser/preferences/preferences.ftl` — 423
- `browser/browser/newtab/newtab.ftl` — 409
- `browser/browser/aiWindow.ftl` — 159
- `browser/browser/ipProtection.ftl` — 146
- `browser/browser/newtab/onboarding.ftl` — 98
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 88
- `browser/browser/aiWindowContent.ftl` — 80
- `browser/browser/newtab/asrouter.ftl` — 79
- `browser/browser/browser.ftl` — 67
- `browser/browser/featureCallout.ftl` — 64
- `toolkit/toolkit/about/aboutAddons.ftl` — 61
- `browser/browser/profiles.ftl` — 56

**Files absent from the locale:**

- `browser/browser/aiFeatures.ftl`
- `browser/browser/aiWindow.ftl`
- `browser/browser/aiWindowContent.ftl`
- `browser/browser/ipProtection.ftl`
- `browser/browser/sharePanel.ftl`
- `toolkit/toolkit/global/mozPromo.ftl`
- `toolkit/toolkit/global/theme-picker.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 451, `straight-double` 134, `curly-single` 85 | **curly-double** |
| apostrophe | `typographic` 95, `straight` 42 | _mixed_ |
| ellipsis | `char` 412, `ascii` 10 | **char** |
| dash | `em` 76, `en` 1 | **em** |
| nbsp | `total` 8, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

- **typography — 98 strings** — 98 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
  - Affected: `AutomaticAuth`, `BlockMixedActiveContent`, `CSPROViolation`, `CSPROViolationWithURI`, `CSPViolationWithURI`, `CookieBlockedAll`, `CookieBlockedByPermission`, `CookieBlockedForeign`, `CookieBlockedTracker`, `CookieInvalidMaxAgeAttribute`, `CookiePartitionedForeign2`, `FeaturePolicyInvalidEmptyAllowValue` …and 82 more

---

## 3. Open findings (321)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 84 |
| 2 | Wrong content (says something other than the English) | 165 |
| 3 | Degraded language (grammar, spelling, terminology) | 54 |
| 4 | Cosmetic (typography, spacing) | 17 |

### A. Functional, markup, variables & plurals

- `account-tabs-closed-remotely` — `browser/browser/accounts.ftl` — `account-tabs-closed-remotely` has plural variant ['one'], which id does not have
  - Current: `{$closedCount ->} [one] { $closedCount } { -brand-short-name } tab ditutup [other] { $closedCount } { -brand-short-name } tabs ditutup`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `appmenu-help-not-deceptive` — `browser/browser/appmenu.ftl` — Access key `d` of `appmenu-help-not-deceptive` is not present in its label
  - Current: `d`
  - The label is “Ini bukan situs tipuan…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `appmenu-referrals` — `browser/browser/appmenu.ftl` — "Share Firefox" rendered as "Hide Firefox"
  - Current: `Sembunyikan { -brand-shorter-name }`
  - en-US: `Bagikan { -brand-shorter-name }`
  - en-US is "Share { -brand-shorter-name }" (dev comment: opens the referral page, "Share" means recommending the browser). "Sembunyikan" means "Hide", a completely different action; the sibling string appmenuitem-referrals correctly uses "Bagikan".
- `appmenu-search-history` — `browser/browser/appmenu.ftl` — "Search history" (verb) rendered as the noun "search history"
  - Current: `Riwayat pencarian`
  - en-US: `Cari riwayat`
  - The dev comment says "This allows to search through the browser's history", so "Search" is a verb. "Riwayat pencarian" means "history of searches", i.e. a different concept.
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — "Default Browser Agent" rendered as "Agen Peramban Baru" (New Browser Agent) instead of "Baku" (default).
  - Current: `Tugas Agen Peramban Baru bertugas memeriksa`
  - en-US: `Tugas Agen Peramban Baku bertugas memeriksa`
  - The task name is "Default Browser Agent"; the same string uses "peramban baku" correctly a few words later, so "Baru" names the wrong thing.
- `bookmarks-toolbar` — `browser/browser/browser.ftl` — Access key `B` of `bookmarks-toolbar` is not present in its label
  - Current: `B`
  - The label is “Markah”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `browser-tab-mute` — `browser/browser/browser.ftl` — Plural variant truncated to a single letter
  - Current: `*[other] S`
  - en-US: `*[other] SENYAPKAN { $count } TAB`
  - en-US is "MUTE { $count } TABS"; the localized default variant is just "S", so the tab tooltip shows a meaningless single character for any count other than 1.
- `browser-tab-unblock` — `browser/browser/browser.ftl` — Plural variant truncated to a single letter
  - Current: `*[other] P`
  - en-US: `*[other] PUTAR { $count } TAB`
  - en-US is "PLAY { $count } TABS"; the localized default variant is just "P".
- `browser-tab-unmute` — `browser/browser/browser.ftl` — Plural variant truncated to a single letter
  - Current: `*[other] U`
  - en-US: `*[other] SUARAKAN { $count } TAB`
  - en-US is "UNMUTE { $count } TABS"; the localized default variant is just "U".
- `trustpanel-list-label-tracking-content` — `browser/browser/browser.ftl` — Category label "Tracking content" turned into the verb phrase "tracking content"
  - Current: `Melacak konten`
  - en-US: `Konten pelacak`
  - en-US "Tracking content" is a noun phrase naming a blocked category, alongside "Kuki pelacak lintas situs" and "Pelacak media sosial". "Melacak konten" reads as the action "to track content".
- `urlbar-search-tips-redirect-2` — `browser/browser/browser.ftl` — "address bar" translated as "toolbar"
  - Current: `Mulai pencarian Anda di bilah alat`
  - en-US: `Mulai pencarian Anda di bilah alamat`
  - en-US says "Start your search in the address bar". "bilah alat" is the toolbar; the locale consistently uses "bilah alamat" for the address bar (e.g. urlbar-search-tips-onboard, bookmark-overlay-keyword-caption-label-2).
- `urlbar-web-authn-anchor` — `browser/browser/browser.ftl` — Imperative "Open … panel" turned into a statement
  - Current: `Panel Autentikasi Web Terbuka`
  - en-US: `Buka panel Autentikasi Web`
  - en-US is "Open Web Authentication panel"; the Indonesian reads "Web Authentication panel is open". All neighbouring anchors in the same block use "Buka panel …".
- `confirmation-hint-duplicate-tabs-closed` — `browser/browser/confirmationHints.ftl` — Post-action confirmation rendered as an imperative, plus untranslated "tabs"
  - Current: `Tutup { $tabCount } tabs`
  - en-US: `{ $tabCount } tab ditutup`
  - en-US "Closed { $tabCount } tabs" reports a completed action; "Tutup" is the imperative "Close". The English plural "tabs" is also left untranslated (Indonesian has no plural -s).
- `firefoxview-search-results-count` — `browser/browser/firefoxView.ftl` — `firefoxview-search-results-count` has plural variant ['one'], which id does not have
  - Current: `{$count ->} [one] { $count } situs [other] { $count } situs`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `firefoxview-search-text-box-history` — `browser/browser/firefoxView.ftl` — "Search history" (verb) rendered as the noun "search history"
  - Current: `Riwayat pencarian`
  - en-US: `Cari riwayat`
  - The dev comment explicitly states "search" is a verb; sibling placeholders correctly use "Cari markah", "Cari tab". The current text means "history of searches".
- `fxviewtabrow-forget-about-this-site` — `browser/browser/fxviewTabList.ftl` — Access key `F` of `fxviewtabrow-forget-about-this-site` is not present in its label
  - Current: `F`
  - The label is “Lupakan Situs Ini…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-move-tab` — `browser/browser/fxviewTabList.ftl` — Access key `V` of `fxviewtabrow-move-tab` is not present in its label
  - Current: `V`
  - The label is “Pindahkan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-move-tab-start` — `browser/browser/fxviewTabList.ftl` — Access key `S` of `fxviewtabrow-move-tab-start` is not present in its label
  - Current: `S`
  - The label is “Pindahkan ke Awal”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-move-tab-window` — `browser/browser/fxviewTabList.ftl` — Access key `W` of `fxviewtabrow-move-tab-window` is not present in its label
  - Current: `W`
  - The label is “Pindahkan ke Jendela Baru”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-mute-tab` — `browser/browser/fxviewTabList.ftl` — Access key `M` of `fxviewtabrow-mute-tab` is not present in its label
  - Current: `M`
  - The label is “Senyapkan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-pin-tab` — `browser/browser/fxviewTabList.ftl` — Access key `P` of `fxviewtabrow-pin-tab` is not present in its label
  - Current: `P`
  - The label is “Sematkan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxviewtabrow-unmute-tab` — `browser/browser/fxviewTabList.ftl` — Access key `m` of `fxviewtabrow-unmute-tab` is not present in its label
  - Current: `m`
  - The label is “Bunyikan Tab”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Malformed closing tag `</a >` in `genai-settings-chat-gemini-links`
  - Current: `Dengan memilih Google Gemini, Anda menyetujui <a data-l10n-name="link1">Persyaratan Layanan Google</a>, <a data-l10n-name="link2">Kebijakan Penggunaan Terlarang untuk AI Generatif</a >, dan <a data-l10n-name="link3">Pem…`
  - en-US: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
  - Whitespace inside a closing tag makes it render as literal text.
- `menu-help-not-deceptive` — `browser/browser/menubar.ftl` — Access key `d` of `menu-help-not-deceptive` is not present in its label
  - Current: `d`
  - The label is “Ini bukan situs tipuan…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `menu-history-search` — `browser/browser/menubar.ftl` — "Search History" (verb + object) is rendered as the noun phrase "search history".
  - Current: `Riwayat Pencarian`
  - en-US: `Cari Riwayat`
  - The developer comment states "Search" is a verb, as in "Search in History"; the parallel item menu-bookmarks-search is correctly "Cari Markah".
- `browser-data-passwords-checkbox` — `browser/browser/migration.ftl` — "Saved Logins and Passwords" is translated as "Login and Password History".
  - Current: `Riwayat Info Masuk dan Sandi`
  - en-US: `Info Masuk dan Sandi Tersimpan`
  - "Riwayat" means history, not saved; migrationWizard.ftl renders the same concept as "Info masuk dan sandi tersimpan".
- `browser-data-passwords-label` — `browser/browser/migration.ftl` — "Saved Logins and Passwords" is translated as "Login and Password History".
  - Current: `Riwayat Info Masuk dan Sandi`
  - en-US: `Info Masuk dan Sandi Tersimpan`
  - Same defect as the checkbox variant; "Riwayat" (history) is not "Saved".
- `import-safari-permissions-string` — `browser/browser/migration.ftl` — The user is told to pick the Safari "file" instead of the Safari folder.
  - Current: `pilih berkas “Safari“ dalam dialog Finder`
  - en-US: `pilih folder “Safari” dalam dialog Finder`
  - en-US says "select the “Safari“ folder"; migrationWizard.ftl correctly uses "folder Safari". Instructing users to select a file makes the step unfollowable.
- `migration-wizard-progress-success-bookmarks` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-bookmarks` has plural variant ['one'], which id does not have
  - Current: `{$quantity ->} [one] { $quantity } markah [other] { $quantity } markah`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-extensions` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-extensions` has plural variant ['one'], which id does not have
  - Current: `{$quantity ->} [one] { $quantity } ekstensi [other] { $quantity } ekstensi`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-favorites` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-favorites` has plural variant ['one'], which id does not have
  - Current: `{$quantity ->} [one] { $quantity } favorit [other] { $quantity } favorit`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `migration-wizard-progress-success-new-bookmarks` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-new-bookmarks` has plural variant ['one'], which id does not have
  - Current: `{$newEntries ->} [one] { $newEntries } markah [other] { $newEntries } markah`
  - id has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `cfr-doorhanger-bookmark-fxa-close-btn-tooltip` — `browser/browser/newtab/asrouter.ftl` — The .title tooltip is the single letter “T” instead of a translation of “Close”.
  - Current: `.title = T`
  - en-US: `.title = Tutup`
  - en-US is “.title = Close”; the aria-label above it is correctly “Tombol tutup”. “T” appears to be a stray access-key-style fragment and renders as a meaningless one-letter tooltip.
- `cfr-doorhanger-doh-secondary-button` — `browser/browser/newtab/asrouter.ftl` — Access key `D` of `cfr-doorhanger-doh-secondary-button` is not present in its label
  - Current: `D`
  - The label is “Nonaktifkan”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `colorways-cfr-body` — `browser/browser/newtab/asrouter.ftl` — “shades” (colour shades) is translated as “bayangan” (shadows).
  - Current: `bayangan eksklusif { -brand-short-name }`
  - en-US: `corak warna eksklusif { -brand-short-name }`
  - The developer comment states that “shades” refers to the different colour options available in colorways, not to shadows.
- `fxa-sync-cfr-secondary` — `browser/browser/newtab/asrouter.ftl` — Access key `R` of `fxa-sync-cfr-secondary` is not present in its label
  - Current: `R`
  - The label is “Ingatkan saya nanti”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `newtab-discovery-empty-section-topstories-timed-out` — `browser/browser/newtab/newtab.ftl` — The sentence is self-contradictory and does not render “We almost loaded this section, but not quite.”
  - Current: `Ups! Kami belum selesai memuat bagian ini, tetapi ternyata belum.`
  - en-US: `Ups! Kami hampir selesai memuat bagian ini, tetapi belum berhasil.`
  - en-US says loading almost succeeded; the id text says “we have not finished loading this section, but apparently not yet”, which repeats the negation and reads as nonsense.
- `newtab-empty-section-topstories` — `browser/browser/newtab/newtab.ftl` — “You’ve caught up.” is rendered as “Maaf Anda tercegat.” (“Sorry, you were intercepted.”).
  - Current: `Maaf Anda tercegat.`
  - en-US: `Anda sudah membaca semuanya.`
  - en-US “You’ve caught up.” means there is no more new content; “tercegat” (intercepted/blocked) conveys an unrelated and confusing meaning, and the added “Maaf” has no source.
- `newtab-wallpaper-category-title-colors` — `browser/browser/newtab/newtab.ftl` — “Solid colors” is rendered as “Warna-warni rata” (assorted/multicoloured flat colours).
  - Current: `Warna-warni rata`
  - en-US: `Warna solid`
  - The reduplicated “warna-warni” means “multicoloured/assorted”, the opposite of the single solid colours this category contains.
- `mr2022-onboarding-mobile-download-image-alt` — `browser/browser/newtab/onboarding.ftl` — “lily pads” is translated as “bunga bakung” (lily flowers).
  - Current: `Katak melompat melintasi bunga bakung`
  - en-US: `Katak melompat melintasi daun teratai`
  - Lily pads are the floating leaves of a water lily (“daun teratai”), not the “bakung” lily flower; the alt text describes the wrong image for screen-reader users.
- `onboarding-live-language-installing` — `browser/browser/newtab/onboarding.ftl` — “Installing the language pack” is rendered as “Downloading”, duplicating the download string.
  - Current: `Mengunduh paket bahasa untuk { $negotiatedLanguage }…`
  - en-US: `Memasang paket bahasa untuk { $negotiatedLanguage }…`
  - en-US: “Installing the language pack for { $negotiatedLanguage }…”. The id text is identical to onboarding-live-language-button-label-downloading, so the install phase is reported as a download.
- `security-view-privacy-viewpasswords` — `browser/browser/pageInfo.ftl` — The verb is dropped: the button label "View Saved Passwords" becomes the noun phrase "Saved Passwords".
  - Current: `Sandi Tersimpan`
  - en-US: `Lihat Sandi Tersimpan`
  - It is a button that opens the password manager; the sibling button security-view keeps its verb ("Tampilkan Sertifikat").
- `places-view-sortby-date` — `browser/browser/places.ftl` — "Sort by Most Recent Visit" is rendered as "Sort by The Newest & Visit".
  - Current: `Urut berdasarkan Yang Terbaru & Kunjungan`
  - en-US: `Urut berdasarkan Kunjungan Terakhir`
  - The ampersand turns one criterion into two; the matching column places-view-sort-col-most-recent-visit is correctly "Kunjungan Terakhir".
- `policy-DisplayMenuBar` — `browser/browser/policies/policies-descriptions.ftl` — “by default” is translated as “secara otomatis” (automatically).
  - Current: `Tampilkan Bilah Menu secara otomatis.`
  - en-US: `Tampilkan Bilah Menu secara baku.`
  - en-US: “Display the Menu Bar by default.” The immediately preceding policy-DisplayBookmarksToolbar correctly renders the same “by default” as “secara baku”.
- `policy-PopupBlocking` — `browser/browser/policies/policies-descriptions.ftl` — “by default” is translated as “secara otomatis” (automatically).
  - Current: `Izinkan situs tertentu untuk menampilkan pop-up secara otomatis.`
  - en-US: `Izinkan situs tertentu untuk menampilkan pop-up secara baku.`
  - en-US: “Allow certain websites to display popups by default.” The policy sets a default permission, it does not make popups appear automatically.
- `connection-dns-over-https-url-item-default` — `browser/browser/preferences/connection.ftl` — "resolving DNS" mistranslated as "troubleshooting DNS problems"
  - Current: `Gunakan URL baku untuk memecahkan masalah DNS atas HTTPS`
  - en-US: `Gunakan URL baku untuk meresolusi DNS lewat HTTPS`
  - "Resolving DNS over HTTPS" is DNS name resolution, not troubleshooting; "memecahkan masalah" means "solve a problem". The sibling string connection-dns-over-https-url-custom correctly uses "mendapatkan DNS lewat HTTPS".
- `autofill-address-post-town` — `browser/browser/preferences/formAutofill.ftl` — "Post town" rendered as "city code"
  - Current: `Kode kota`
  - en-US: `Kota pos`
  - "Post town" (GB/NO/SE) is the town name used in a postal address, not a numeric code; "Kode kota" means "city code" and collides conceptually with autofill-address-postal-code ("Kode Pos").
- `more-from-moz-mozilla-monitor-us-description` — `browser/browser/preferences/moreFromMozilla.ftl` — Description says "find out" instead of "automatically take back"
  - Current: `Ketahui info pribadi Anda yang telah dibobol`
  - en-US: `Ambil kembali info pribadi Anda yang terekspos secara otomatis`
  - en-US is "Automatically take back your exposed personal info." The Indonesian promises only discovery of breached info, dropping the removal action that is the product's selling point.
- `content-blocking-all-windows-tracking-content` — `browser/browser/preferences/preferences.ftl` — "Tracking content" (noun phrase) rendered as the verb "to track content"
  - Current: `Melacak konten di seluruh jendela`
  - en-US: `Konten pelacak di semua jendela`
  - Same defect as content-blocking-private-windows: the blocked-items list entry "Tracking content in all windows" becomes an action phrase in Indonesian.
- `content-blocking-private-windows` — `browser/browser/preferences/preferences.ftl` — "Tracking content" (noun phrase) rendered as the verb "to track content"
  - Current: `Melacak konten di Jendela Pribadi`
  - en-US: `Konten pelacak di Jendela Pribadi`
  - This is an item in the list of what { -brand-short-name } blocks. "Melacak konten" reads as the action "tracking content", implying the browser tracks content; the source means content that tracks. The related label content-blocking-tracking-content-label correctly uses a noun phrase ("Pelacakan konten").
- `site-data-settings-description` — `browser/browser/preferences/siteDataSettings.ftl` — "The following websites" rendered as "this website" (singular, deictic)
  - Current: `Situs web ini menyimpan kuki dan data situs pada komputer Anda.`
  - en-US: `Situs web berikut menyimpan kuki dan data situs pada komputer Anda.`
  - en-US is "The following websites store cookies and site data on your computer" — it introduces the list below. "Situs web ini" means "this website", pointing at nothing and losing the reference to the list.
- `delete-profile-tabs` — `browser/browser/profiles.ftl` — "Open tabs" (adjective + noun) is rendered as the command "Open tab".
  - Current: `Buka tab`
  - en-US: `Tab terbuka`
  - The developer comment says "Open is an adjective, as in browser tabs currently open".
- `delete-profile-windows` — `browser/browser/profiles.ftl` — "Open windows" (adjective + noun) is rendered as the command "Open window".
  - Current: `Buka jendela`
  - en-US: `Jendela terbuka`
  - The developer comment explicitly says "Open is an adjective, as in browser windows currently open"; the string is a data row in the delete-profile table, not an action.
- `graph-week-summary-private-window` — `browser/browser/protections.ftl` — Word order makes it read as "{brand}'s trackers blocked this week" instead of "Trackers {brand} blocked this week".
  - Current: `Pelacak { -brand-short-name } diblokir pekan ini`
  - en-US: `Pelacak yang diblokir { -brand-short-name } pekan ini`
  - In Indonesian a bare noun followed by a name reads as a possessive, attributing the trackers to the browser.
- `protections-panel-description-shim-allowed` — `browser/browser/protectionsPanel.ftl` — Meaning reversed: en-US says the trackers were partially *unblocked*, the Indonesian says they were partially *blocked*.
  - Current: `telah diblokir sebagian pada laman ini karena Anda berinteraksi dengan mereka`
  - en-US: `sebagian tidak diblokir pada laman ini karena Anda berinteraksi dengan mereka`
  - "partially unblocked" ≠ "diblokir sebagian"; the companion tooltip protections-panel-shim-allowed-indicator correctly says "sebagian tidak diblokir".
- `safeb-palm-notdeceptive` — `browser/browser/safebrowsing/blockedSite.ftl` — Access key `d` of `safeb-palm-notdeceptive` is not present in its label
  - Current: `d`
  - The label is “Ini bukan situs tipuan…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `protections-blocking-cookies-trackers` — `browser/browser/siteProtections.ftl` — "Cross-Site Tracking Cookies Blocked" drops "Situs", leaving the dangling "Lintas".
  - Current: `Kuki Pelacakan Lintas Diblokir`
  - en-US: `Kuki Pelacakan Lintas Situs Diblokir`
  - Same incomplete term as protections-not-blocking-cross-site-tracking-cookies; the full form is used in the labels above.
- `tracking-protection-icon-active` — `browser/browser/siteProtections.ftl` — "cross-site tracking cookies" loses "site": "kuki pelacakan lintas" is an incomplete term.
  - Current: `kuki pelacakan lintas`
  - en-US: `kuki pelacakan lintas situs`
  - "lintas" (across) needs its object; content-blocking-cookies-blocking-trackers-label in the same file correctly says "Kuki Pelacakan Lintas Situs".
- `fxa-menu-send-tab-to-device` — `browser/browser/sync.ftl` — The tab count is attached to the device: the label reads "Send tab to {$tabCount} devices" instead of "Send {$tabCount} tabs to device".
  - Current: `Kirim Tab ke { $tabCount } Peranti`
  - en-US: `Kirim { $tabCount } Tab ke Perangkat`
  - $tabCount is documented as the number of tabs, so the placement makes the label state a wrong number of devices.
- `synced-tabs-context-manage-devices` — `browser/browser/syncedTabs.ftl` — Access key `D` of `synced-tabs-context-manage-devices` is not present in its label
  - Current: `D`
  - The label is “Kelola Perangkat…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- _…and 95 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `contextual-manager-passwords-os-auth-dialog-caption` — `browser/browser/contextual-manager.ftl` — Brand term duplicated in OS auth dialog caption
  - Current: `{ -brand-full-name }{ -brand-full-name }`
  - en-US: `{ -brand-full-name }`
  - en-US contains a single { -brand-full-name }; the duplication makes the OS authentication dialog caption read "Mozilla FirefoxMozilla Firefox".
- `appearance-browser-icon-pride` — `browser/browser/preferences/browserIcon.ftl` — "Pride" translated as the emotion rather than kept as the name
  - Current: `Kebanggaan`
  - en-US: `Pride`
  - In this icon list "Pride" names the LGBTQ+ Pride (rainbow) icon, a proper name that is normally kept as "Pride" in Indonesian; "Kebanggaan" is the abstract feeling of pride and does not identify the icon.
- `fonts-langgroup-ethiopic` — `browser/browser/preferences/fonts.ftl` — Script name "Ethiopic" rendered as the country, spelled in English
  - Current: `Ethiopia`
  - en-US: `Etiopik`
  - "Ethiopic" is the writing system (Ge'ez script), not the country; additionally the Indonesian spelling of the country is "Etiopia", not the English "Ethiopia".
- `fonts-langgroup-simpl-chinese` — `browser/browser/preferences/fonts.ftl` — Country name "Tiongkok" used instead of the language/script name
  - Current: `Tiongkok Sederhana`
  - en-US: `Tionghoa Sederhana`
  - In Indonesian, "Tiongkok" is the country China; the language/script is "Tionghoa" (bahasa/aksara Tionghoa). The label names a font language group, so it must name the language, not the country.
- `fonts-langgroup-thai` — `browser/browser/preferences/fonts.ftl` — Country "Thailand" used instead of the language name "Thai"
  - Current: `Thailand`
  - en-US: `Thai`
  - The entry names a font language group (Thai). In Indonesian the language is "bahasa Thai"; "Thailand" is the country, matching the wrong-name category (country instead of language).
- `fonts-langgroup-trad-chinese` — `browser/browser/preferences/fonts.ftl` — Country name "Tiongkok" used instead of the language/script name
  - Current: `Tiongkok Tradisional (Taiwan)`
  - en-US: `Tionghoa Tradisional (Taiwan)`
  - "Tiongkok" is the country China; the language/script name in Indonesian is "Tionghoa".
- `fonts-langgroup-trad-chinese-hk` — `browser/browser/preferences/fonts.ftl` — Country name "Tiongkok" used instead of the language/script name
  - Current: `Tiongkok Tradisional (Hong Kong)`
  - en-US: `Tionghoa Tradisional (Hong Kong)`
  - "Tiongkok" is the country China; the language/script name in Indonesian is "Tionghoa".
- `autofill-address-townland` — `browser/browser/preferences/formAutofill.ftl` — Irish "townland" rendered as "small town"
  - Current: `Kota kecil`
  - en-US: `Townland`
  - Per the developer comment this is the Irish sublocality unit "townland", a rural land division, not a small town ("kota kecil"); it is normally kept as "Townland".
- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — The HTML element name inside <code> was translated.
  - Current: `<code>judul</code>`
  - en-US: `<code>title</code>`
  - en-US is "Documents must have a <code>title</code>"; the content of <code> is the literal HTML element/attribute name and must stay in English, as it is kept in all sibling strings (fieldset, legend, alt, optgroup).
- `network-menu-summary-tooltip-load` — `devtools/client/netmonitor.ftl` — The DOM event name "load" was translated as the common noun "beban" (burden).
  - Current: `peristiwa “beban”`
  - en-US: `peristiwa “load”`
  - en-US is "Time when “load” event occurred"; "load" is the literal event name, kept untranslated in the sibling string for “DOMContentLoaded”.
- `networkMenu.summary.tooltip.load` — `devtools/client/netmonitor.properties` — The DOM event name "load" was translated as "beban".
  - Current: `peristiwa “beban”`
  - en-US: `peristiwa “load”`
  - Same defect as the Fluent counterpart: "load" is an event identifier and must not be translated.
- `options-default-color-unit-rgb` — `devtools/client/toolbox-options.ftl` — The CSS color-function name RGB(A) was translated to MHB(A).
  - Current: `MHB(A)`
  - en-US: `RGB(A)`
  - This label selects the CSS output unit; "rgb()"/"rgba()" are code identifiers, and neighbouring units HSL(A) and HWB were correctly left untouched.
- `inactive-css-not-for-internal-table-elements-fix` — `devtools/client/tooltips.ftl` — The CSS value table-footer-group was partially translated to tabel-footer-group.
  - Current: `<strong>tabel-footer-group</strong>`
  - en-US: `<strong>table-footer-group</strong>`
  - CSS display values inside <strong> must not be translated (see file comment); the other values in the same list were left in English, so the advice is unusable as written.
- `inactive-css-not-multicol-container-fix` — `devtools/client/tooltips.ftl` — The CSS property names column-count and column-width were translated inside <strong>.
  - Current: `Coba tambahkan <strong>jumlah kolom</strong> atau <strong>lebar kolom</strong>.`
  - en-US: `Coba tambahkan <strong>column-count</strong> atau <strong>column-width</strong>.`
  - The section comment states CSS properties and values in <strong> tags must not be translated; inactive-css-column-span-fix in the same file keeps them in English.
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — The console command name :block was translated to :blokir.
  - Current: `:blokir URL_STRING`
  - en-US: `:block URL_STRING`
  - `:block` is a literal Web Console command the user must type; the same string later refers to `:unblock` untranslated, so the usage text now documents a command that does not exist.
- `webconsole-commands-usage-unblock` — `devtools/shared/webconsole-commands.ftl` — The console command name :unblock was translated to ":buka blokir".
  - Current: `:buka blokir URL_STRING`
  - en-US: `:unblock URL_STRING`
  - `:unblock` is a literal command name; ":buka blokir" is not a valid command and even contains a space, so it cannot be typed as shown.
- `language-name-lo` — `toolkit/toolkit/intl/languageNames.ftl` — Lao is rendered "Laothia", which is not an Indonesian word or language name.
  - Current: `Laothia`
  - en-US: `Laos`
  - en-US `language-name-lo = Lao`; Indonesian uses "bahasa Laos" (cf. region-name-la = Laos). "Laothia" names nothing.
- `language-name-sco` — `toolkit/toolkit/intl/languageNames.ftl` — The Scots language is named "Skotlandia", which is the country Scotland.
  - Current: `Skotlandia`
  - en-US: `Skots`
  - en-US `language-name-sco = Scots`. "Skotlandia" is the Indonesian name of the country, not of the Germanic language spoken there.
- `language-name-sg` — `toolkit/toolkit/intl/languageNames.ftl` — Sango is rendered "Sangro", which is not the language name.
  - Current: `Sangro`
  - en-US: `Sango`
  - en-US `language-name-sg = Sango`, the national language of the Central African Republic; "Sangro" names an Italian river.
- `language-name-su` — `toolkit/toolkit/intl/languageNames.ftl` — The Sundanese language is named "Sudan", which is a country, not the language.
  - Current: `Sudan`
  - en-US: `Sunda`
  - en-US `language-name-su = Sundanese`. In Indonesian the language is "Sunda"; "Sudan" is the African country (and is correctly used at region-name-sd).
- `language-name-zh` — `toolkit/toolkit/intl/languageNames.ftl` — Chinese (the language) is named with the country name "Tiongkok".
  - Current: `Tiongkok`
  - en-US: `Tionghoa`
  - en-US is `Chinese` (a language). "Tiongkok" is the country and is already used for region-name-cn; the language name in Indonesian is "Tionghoa" (or "Mandarin").
- `region-name-sx` — `toolkit/toolkit/intl/regionNames.ftl` — Sint Maarten (SX) is labelled "Saint Martin", duplicating the name given to MF.
  - Current: `Saint Martin`
  - en-US: `Sint Maarten`
  - en-US has `region-name-mf = Saint Martin` and `region-name-sx = Sint Maarten`; the locale gives both entries the same name, so the Dutch territory is mislabelled.

### C. Grammar, agreement & spelling

- `about-logins-import-file-picker-tsv-filter-title` — `browser/browser/aboutLogins.ftl` — macOS "TSV Document" rendered as "Berkas TSV" (File)
  - Current: `[macos] Berkas TSV`
  - en-US: `[macos] Dokumen TSV`
  - en-US distinguishes "TSV Document" (macOS) from "TSV File"; the CSV filter right above correctly uses "Dokumen CSV" vs "Berkas CSV", so the TSV macOS variant is wrong.
- `about-logins-menu-menuitem-remove-all-logins` — `browser/browser/aboutLogins.ftl` — "Logins" rendered as "Log Masuk" while the rest of the surface uses "Info Masuk"
  - Current: `Hapus Semua Log Masuk…`
  - en-US: `Hapus Semua Info Masuk…`
  - The adjacent menu items use "Info Masuk" (Export Logins → "Ekspor Info Masuk…"); "Log Masuk" is an inconsistent rendering of the same term in the same menu (also in about-logins-confirm-remove-all-dialog-checkbox-label).
- `pending-crash-reports-message` — `browser/browser/contentCrash.ftl` — "crash report" translated as "laporan kemacetan" instead of "laporan kerusakan"
  - Current: `laporan kemacetan yang belum terkirim`
  - en-US: `laporan kerusakan yang belum terkirim`
  - Every other crash-report string in the same file uses "laporan kerusakan"; "kemacetan" means congestion/jam and is wrong in this context.
- `contextual-manager-passwords-import-file-picker-tsv-filter-title` — `browser/browser/contextual-manager.ftl` — macOS "TSV Document" rendered as "Berkas TSV" (File)
  - Current: `[macos] Berkas TSV`
  - en-US: `[macos] Dokumen TSV`
  - en-US macOS variant is "TSV Document"; the CSV filter in the same file uses "Dokumen CSV" for macOS, so this variant is inconsistent and wrong.
- `firefoxview-opentabs-bookmarked-tab` — `browser/browser/firefoxView.ftl` — "Bookmarked" rendered as "Ditandai" instead of "Dimarkahi"
  - Current: `(Ditandai) { $url }`
  - en-US: `(Dimarkahi) { $url }`
  - The parallel tooltip firefoxview-opentabs-bookmarked-pinned-tab uses "(Dimarkahi)", and the locale consistently uses "markah" for bookmarks; "Ditandai" just means "marked".
- `genai-chatbot-summarize-footer-provider-subtitle` — `browser/browser/genai.ftl` — Quoted button name does not match the button translation
  - Current: `pilih "Ringkas halaman" di bagian bawah`
  - en-US: `pilih “Ringkas laman” di bagian bawah`
  - The dev comment requires consistency with genai-page-button-summarize, which is translated "Ringkas laman" (not "halaman").
- `genai-chatbot-summarize-sidebar-generic-subtitle` — `browser/browser/genai.ftl` — Menu name quoted here does not match the menu item translation
  - Current: `pilih "Ringkas Halaman"`
  - en-US: `pilih “Ringkaskan Laman”`
  - The dev comment requires this quoted command to match genai-menu-summarize-page, which is translated "Ringkaskan Laman"; the sibling string genai-chatbot-summarize-sidebar-provider-subtitle uses yet another form ("Ringkas Laman"), so users are told to look for a menu entry that does not exist.
- `amo-picker-subtitle` — `browser/browser/newtab/onboarding.ftl` — “browser” is left in English twice where the file consistently uses “peramban”.
  - Current: `Ekstensi adalah seperti aplikasi untuk browser Anda`
  - en-US: `Ekstensi adalah seperti aplikasi untuk peramban Anda`
  - Every other occurrence of “browser” in this file is translated as “peramban” (e.g. mr1-return-to-amo-addon-title, mr2-onboarding-thank-you-text); leaving it untranslated here is inconsistent with the locale's established term.
- `fingerprinter-tab-content` — `browser/browser/protections.ftl` — "browser" is left in English where the locale consistently uses "peramban".
  - Current: `pengaturan dari browser dan komputer Anda`
  - en-US: `pengaturan dari peramban dan komputer Anda`
  - The tree renders "browser" as "peramban" throughout (menubar.ftl, migration.ftl, protections.ftl mobile-app-card-content).
- `safeb-blocked-harmful-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — Misspelling of "informasi".
  - Current: `menghapus infomasi Anda`
  - en-US: `menghapus informasi Anda`
  - "infomasi" is a typo; the correct spelling "informasi" is used in the parallel malware string.
- `speech-dispatcher-open-fail` — `browser/browser/speechDispatcher.ftl` — The product name "Speech Dispatcher" is rendered as "Switch Dispatcher", although the file comment says the name must not be localized.
  - Current: `Switch Dispatcher tidak akan terbuka`
  - en-US: `Speech Dispatcher tidak akan terbuka`
  - All other strings in the file keep "Speech Dispatcher"; the header comment states the tool name shouldn't be localized.
- `blockedPotentiallyUnwanted` — `browser/chrome/browser/downloads/downloads.properties` — Misspelling of "mungkin".
  - Current: `Berkas ini meungkin dapat merusak komputer Anda.`
  - en-US: `Berkas ini mungkin dapat merusak komputer Anda.`
  - "meungkin" is not a word; the correct form "mungkin" is used throughout the rest of the file.
- `spread_odd.title` — `browser/pdfviewer/viewer.properties` — Misspelling of "halaman".
  - Current: `Gabungkan lembar lamanan mulai dengan halaman ganjil`
  - en-US: `Gabungkan lembar halaman mulai dengan halaman ganjil`
  - "lamanan" is not a word; the parallel string spread_even.title correctly reads "Gabungkan lembar halaman".
- `accessibility-keyboard-issue-action` — `devtools/client/accessibility.ftl` — Misspelling of "papan ketik".
  - Current: `menggunakan papam ketik`
  - en-US: `menggunakan papan ketik`
  - Typo; the identical string in devtools/shared/accessibility.properties reads "papan ketik".
- `accessibility-keyboard-issue-focus-visible` — `devtools/client/accessibility.ftl` — Ungrammatical double verb marking on "focusable".
  - Current: `Elemen yang diberi difokus`
  - en-US: `Elemen yang dapat difokus`
  - en-US is "Focusable element…"; the shared counterpart reads "Elemen yang dapat diberi fokus", so "diberi difokus" is a broken form.
- `accessibility-text-label-issue-toolbar` — `devtools/client/accessibility.ftl` — Stray capital letter inside the first word.
  - Current: `JIka ada lebih dari satu`
  - en-US: `Jika ada lebih dari satu`
  - Typo; the shared/accessibility.properties counterpart spells it "Jika".
- `serviceworker-empty-intro2` — `devtools/client/application.ftl` — Stray capital letter inside the first word.
  - Current: `TIdak ada service worker ditemukan`
  - en-US: `Tidak ada service worker ditemukan`
  - Typo in a top-level empty-state message.
- `expressions.placeholder` — `devtools/client/debugger.properties` — Two misspellings in the watch-expression placeholder.
  - Current: `Tambahkan Expresi Pantuan`
  - en-US: `Tambahkan ekspresi pemantau`
  - "Expresi" should be "ekspresi" and "Pantuan" is a typo for "pemantau/pantauan"; the same file spells it correctly in expressions.label and watchExpressions.header.
- `pauseOnAnyXHR` — `devtools/client/debugger.properties` — Duplicated word makes the checkbox label ungrammatical.
  - Current: `Jeda di URL semua URL`
  - en-US: `Jeda pada semua URL`
  - en-US is "Pause on any URL"; the Indonesian repeats "URL" and leaves a dangling preposition.
- `markupView.scrollableBadge.tooltip` — `devtools/client/inspector.properties` — The scrollable-badge tooltip is garbled and reverses the head noun.
  - Current: `Elemen ini memiliki scrollable bernilai overflow.`
  - en-US: `Elemen ini memiliki overflow yang dapat digulir.`
  - en-US is "This element has scrollable overflow."; the translation says the element has a "scrollable" whose value is overflow, and the correct wording already exists in markupView.scrollableBadge.interactive.tooltip.
- `clear-snapshots.tooltip` — `devtools/client/memory.properties` — Misspelled verb in the delete-all-snapshots tooltip.
  - Current: `Hapuse semua snapshot`
  - en-US: `Hapus semua snapshot`
  - "Hapuse" is not a word; the correct form "Hapus" is used in snapshot.io.delete.
- `networkMenu.summary.tooltip.transferred` — `devtools/client/netmonitor.properties` — Half-translated, mis-spaced tooltip.
  - Current: `Ukuran /transferred ukuran semua permintaan`
  - en-US: `Ukuran/ukuran yang ditransfer dari semua permintaan`
  - en-US is "Size/transferred size of all requests"; the English word "transferred" is left in the middle and the slash is detached, producing an unreadable string.
- `options-stylesheet-autocompletion-label` — `devtools/client/toolbox-options.ftl` — Misspelling of "Otomatis".
  - Current: `CSS Lengkapi-Otomasis`
  - en-US: `Lengkapi CSS Otomatis`
  - "Otomasis" is a typo; the tooltip immediately below spells it "otomatis".
- `inactive-css-not-grid-or-flex-container-or-multicol-container` — `devtools/client/tooltips.ftl` — Misspelling of "multi-kolom".
  - Current: `kontainer muli-kolom`
  - en-US: `kontainer multi-kolom`
  - The adjacent string inactive-css-not-multicol-container spells it "multi-kolom".
- `inactive-css-not-inline-or-tablecell` — `devtools/client/tooltips.ftl` — Misspelling of "sebaris".
  - Current: `elemen sebarus atau table-cell`
  - en-US: `elemen sebaris atau table-cell`
  - "sebarus" is a typo; "sebaris" is used throughout the tree for "inline".
- `inactive-scroll-padding-when-not-scroll-container` — `devtools/client/tooltips.ftl` — Missing conjunction makes the sentence ungrammatical.
  - Current: `tidak berpengaruh pada elemen ini tidak menggulir`
  - en-US: `tidak berpengaruh pada elemen ini karena tidak menggulir`
  - en-US is "…has no effect on this element since it doesn’t scroll"; the causal "karena" present in every sibling string is missing here.
- `table.iterationIndex` — `devtools/client/webconsole.properties` — Misspelling of "iterasi".
  - Current: `(indeks iterarsi)`
  - en-US: `(indeks iterasi)`
  - Typo in the console table column header (also present in devtools/shared/webconsole.properties).
- `webconsole.cssFilterButton.inactive.tooltip` — `devtools/client/webconsole.properties` — Garbled clause: "Refresh the page" became "Refresh safe".
  - Current: `Segarkan aman untuk juga melihat kesalahan`
  - en-US: `Segarkan laman untuk juga melihat kesalahan`
  - en-US is "Refresh the page to also see errors…"; "aman" means "safe" and leaves the sentence without an object (same defect in devtools/shared/webconsole.properties).
- `BadRedirectModeInterceptionWithURL` — `dom/chrome/dom/dom.properties` — "Response" and the RedirectMode value "follow" were translated despite the do-not-translate note.
  - Current: `mengirimkan Balasan pengalihan ke FetchEvent.respondWith() sementara RedirectMode tidak ‘mengikuti’`
  - en-US: `mengirimkan Response yang dialihkan ke FetchEvent.respondWith() sementara RedirectMode bukan ‘follow’`
  - The comment says do not translate "Response" ... or "follow"; both were localized, and ‘follow’ is a literal API value.
- `DOMNodeInsertedIntoDocumentWarning` — `dom/chrome/dom/dom.properties` — Message for DOMNodeInsertedIntoDocument names the wrong event identifier.
  - Current: `Penambahan listener untuk DOMCharacterDataModified sudah usang dan akan segera dihapus. Alih-alih MutationEvent, gunakan MutationObserver. https://developer.mozilla.org/docs/Web/API/MutationObserver`
  - en-US: `Penambahan listener untuk DOMNodeInsertedIntoDocument sudah usang dan akan segera dihapus. Alih-alih MutationEvent, gunakan MutationObserver. https://developer.mozilla.org/docs/Web/API/MutationObserver`
  - Comment says do not translate "DOMNodeInsertedIntoDocument"; the localization substitutes a different event name.
- `DOMNodeInsertedWarning` — `dom/chrome/dom/dom.properties` — Message for DOMNodeInserted names the wrong event identifier.
  - Current: `Penambahan listener untuk DOMCharacterDataModified sudah usang`
  - en-US: `Penambahan listener untuk DOMNodeInserted sudah usang`
  - The developer comment says do not translate "DOMNodeInserted"; the string instead repeats DOMCharacterDataModified, so the console warning points developers at the wrong API.
- `DrawWindowCanvasRenderingContext2DWarning` — `dom/chrome/dom/dom.properties` — Do-not-translate API name written as tab.captureTab.
  - Current: `API ekstensi tab.captureTab`
  - en-US: `API ekstensi tabs.captureTab`
  - The comment lists tabs.captureTab as untranslatable; the localized form names a nonexistent API.
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — The literal keys key=/modifiers= were localized despite the do-not-localize note.
  - Current: `kunci=“%S” modifier=“%S” id=“%S”`
  - en-US: `key=“%S” modifiers=“%S” id=“%S”`
  - The comment reads "do not localize key=“%S” modifiers=“%S” id=“%S”"; the same defect occurs in WinConflict2.
- `MathML_DeprecatedMunderNonExplicitAccentunderWarning` — `dom/chrome/dom/dom.properties` — Attribute name "accentunder" translated as "aksen di bawah".
  - Current: `atribut aksen di bawah eksplisit`
  - en-US: `atribut accentunder eksplisit`
  - The comment says do not translate accentunder; the same string keeps it untranslated earlier, so the sentence is also self-inconsistent.
- `PushMessageBadEncodingHeader` — `dom/chrome/dom/dom.properties` — Encoding token written with a space: ‘aesgcm 128‘.
  - Current: `‘aesgcm 128‘ diijinkan`
  - en-US: `‘aesgcm128‘ diizinkan`
  - The comment says do not translate "aesgcm128"; the inserted space makes it an invalid token (and "diijinkan" is a nonstandard spelling of "diizinkan").
- `SelectOptionsLengthAssignmentWarning` — `dom/chrome/dom/dom.properties` — Do-not-translate API name misspelled as HTMLOptionCollection.length.
  - Current: `HTMLOptionCollection.length`
  - en-US: `HTMLOptionsCollection.length`
  - The developer comment says do not translate "HTMLOptionsCollection.length"; the localized identifier is missing the "s" and does not exist.
- `WebExtContentScriptModuleSourceNotAllowed` — `dom/chrome/dom/dom.properties` — URL scheme miscapitalized as moz-Extension.
  - Current: `URL moz-Extension`
  - en-US: `URL moz-extension`
  - moz-extension is a protocol scheme and is case-significant as written in en-US; it must not be altered.
- `PEAtNSUnexpected` — `dom/chrome/layout/css.properties` — CSS at-rule @namespace corrupted to "qnamespace".
  - Current: `Token tak diharapkan dalam qnamespace:`
  - en-US: `Token tak diharapkan dalam @namespace:`
  - en-US names the at-rule @namespace; "qnamespace" is not a CSS construct and misleads authors debugging the rule.
- `errNestedComment` — `dom/chrome/layout/htmlparser.properties` — Comment delimiter written with an em dash instead of two hyphens.
  - Current: `Ada “<!—” dalam sebuah komentar.`
  - en-US: `Ada “<!--” dalam sebuah komentar.`
  - en-US quotes the literal markup “<!--”; the em dash makes the quoted token wrong for an author searching their source.
- `PrincipalWritingModePropagationWarning` — `dom/chrome/layout/layout_errors.properties` — Do-not-translate term truncated to "The Principal Writing Mod".
  - Current: `“The Principal Writing Mod”`
  - en-US: `“The Principal Writing Mode”`
  - The comment lists "The Principal Writing Mode" as a technical term that must be kept verbatim; the final "e" is missing.
- `CORSAllowHeaderFromPreflightDeprecation` — `dom/chrome/security/security.properties` — CORS header name corrupted to `Access-Control-Allow -Header`.
  - Current: ``Access-Control-Allow -Header``
  - en-US: ``Access-Control-Allow-Headers``
  - The comment lists Access-Control-Allow-Headers as do-not-translate; the localized form has a stray space and a singular "Header", so it names no real header.
- `SanitizerAllowElementIgnored2` — `dom/chrome/security/security.properties` — The API name "Sanitizer" was translated as "Pembersih".
  - Current: `Pembersih: Memanggil allowElement()`
  - en-US: `Sanitizer: Memanggil allowElement()`
  - The developer comment explicitly says do not translate Sanitizer.
- `XFrameOptionsDeny` — `dom/chrome/security/security.properties` — Header name written as "X-Frame-Option" (missing s).
  - Current: `direktif  “X-Frame-Option“`
  - en-US: `direktif “X-Frame-Options“`
  - The comment says do not translate "X-Frame-Options"; the sibling string XFrameOptionsInvalid spells it correctly.
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — Code identifier inside <code> tags translated: <code>metrik</code>.
  - Current: `ping <code>metrik</code>.`
  - en-US: `ping <code>metrics</code>.`
  - The developer comment says "Do not translate strings between <code> </code> tags"; <code>metrics</code> is the literal ping name. The sibling <code>events</code> was correctly left untranslated.
- `about-logging-preset-webcodecs-label` — `toolkit/toolkit/about/aboutLogging.ftl` — API name written "WebCodec" instead of "WebCodecs".
  - Current: `about-logging-preset-webcodecs-label = WebCodec`
  - en-US: `about-logging-preset-webcodecs-label = WebCodecs`
  - WebCodecs is the spec/API name and is kept correct in the accompanying description string in the same file.
- `about-webrtc-closed-peerconnection-disclosure-hide-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — "PeerConnections" translated as "Koneksi Peer" while the paired show-message keeps it untranslated.
  - Current: `about-webrtc-closed-peerconnection-disclosure-hide-msg = Sembunyikan Koneksi Peer Tertutup`
  - en-US: `about-webrtc-closed-peerconnection-disclosure-hide-msg = Sembunyikan PeerConnections Tertutup`
  - The file's developer comment states PeerConnection is a proper noun that should not normally be translated, and the matching show-message (…-show-msg) keeps "PeerConnections".
- `-mdn-brand-name` — `toolkit/toolkit/branding/brandings.ftl` — The MDN Web Docs brand name is translated despite the do-not-translate group comment.
  - Current: `Dokumen Web MDN`
  - en-US: `MDN Web Docs`
  - The section comment states these feature names must be treated as a brand and cannot be transliterated or translated; every other entry in the block is left in English.
- `btp-warning-tracker-classified` — `toolkit/toolkit/global/antiTracking.ftl` — "bounce tracker" is translated even though the developer comment forbids it.
  - Current: `pelacak pentalan`
  - en-US: `bounce tracker`
  - The comment above the string says 'Do not translate "bounce tracker"'. The sibling string btp-warning-tracker-purged correctly keeps "bounce tracker" in English, so the two console messages are also inconsistent.
- `neterror-dns-not-found-native-fallback-heuristic` — `toolkit/toolkit/neterror/netError.ftl` — The protocol name is given as HTTP instead of HTTPS.
  - Current: `DNS lewat HTTP telah dinonaktifkan pada jaringan Anda.`
  - en-US: `DNS lewat HTTPS telah dinonaktifkan pada jaringan Anda.`
  - en-US: "DNS over HTTPS has been disabled on your network." DoH is a protocol name; naming plain HTTP misidentifies the feature.

### D. Terminology, register & consistency

- `update-policy-disabled` — `browser/browser/aboutDialog.ftl` — Polite pronoun "Anda" written lowercase
  - Current: `Pembaruan dinonaktifkan oleh organisasi anda.`
  - en-US: `Pembaruan dinonaktifkan oleh organisasi Anda`
  - Indonesian orthography requires the polite pronoun "Anda" to be capitalized; every other string in the file uses "Anda". (Same issue in settings-update-policy-disabled.)
- `about-logins-login-intro-heading-logged-out2` — `browser/browser/aboutLogins.ftl` — Missing passive prefix: "yang simpan" instead of "yang tersimpan"
  - Current: `Mencari info masuk Anda yang simpan?`
  - en-US: `Mencari info masuk Anda yang tersimpan?`
  - en-US "Looking for your saved logins?" — the Indonesian is ungrammatical; the passive form "tersimpan" is required (as used in login-list-intro-title2 and elsewhere).
- `about-private-browsing-focus-promo-text` — `browser/browser/aboutPrivateBrowsing.ftl` — Typo "Aplkasi" for "Aplikasi"
  - Current: `Aplkasi seluler penjelajahan pribadi`
  - en-US: `Aplikasi seluler penjelajahan pribadi`
  - Simple misspelling of "Aplikasi" at the start of a user-visible promo sentence.
- `about-unloads-intro` — `browser/browser/aboutUnloads.ftl` — Typo "dibongkat" for "dibongkar"
  - Current: `Anda dapat memicu tab dibongkat secara manual`
  - en-US: `Anda dapat memicu tab dibongkar secara manual`
  - Misspelling of "dibongkar" (unloaded), the term used throughout the rest of the same paragraph.
- `appmenu-edit-pdf` — `browser/browser/appmenu.ftl` — Typo "Suntiing" for "Sunting"
  - Current: `Suntiing PDF …`
  - en-US: `Sunting PDF…`
  - Misspelling of "Sunting" (Edit) in a menu label; there is also a stray space before the ellipsis.
- `picture-in-picture-panel-body` — `browser/browser/browser.ftl` — Typo "dinginkan" for "diinginkan"
  - Current: `seperti yang dinginkan pengembang`
  - en-US: `seperti yang diinginkan pengembang`
  - en-US "as the developer intended". "dinginkan" means "cool it down"; the intended word is "diinginkan".
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — Typo "Masukan" for "Masukkan"
  - Current: `Masukan istilah pencarian`
  - en-US: `Masukkan istilah pencarian`
  - Same misspelling as in the neighbouring placeholders, which correctly use "Masukkan".
- `urlbar-placeholder-search-mode-other-bookmarks` — `browser/browser/browser.ftl` — Typo "Masukan" for "Masukkan"
  - Current: `Masukan istilah pencarian`
  - en-US: `Masukkan istilah pencarian`
  - "Masukan" is the noun "input/feedback"; the imperative "Enter" is "Masukkan", as used in the sibling placeholders urlbar-placeholder-search-mode-other-engine and -other-tabs.
- `urlbar-placeholder-search-mode-other-history` — `browser/browser/browser.ftl` — Typo "Masukan" for "Masukkan"
  - Current: `Masukan istilah pencarian`
  - en-US: `Masukkan istilah pencarian`
  - Same misspelling as in the neighbouring placeholders, which correctly use "Masukkan".
- `urlbar-result-market-opt-in-description` — `browser/browser/browser.ftl` — Typo "kuiri" for "kueri"
  - Current: `data kuiri pencarian`
  - en-US: `data kueri pencarian`
  - "query" is spelled "kueri" in Indonesian and elsewhere in this tree (e.g. login-list.aria-label in aboutLogins.ftl); "kuiri" is not a word.
- `menu-tools-edit-pdf` — `browser/browser/menubar.ftl` — Spelling error in the menu label.
  - Current: `Suntiing PDF …`
  - en-US: `Sunting PDF…`
  - "Suntiing" is not a word; the correct form is "Sunting" (also, the space before the ellipsis is spurious).
- `migration-choose-to-import-from-file-button-label` — `browser/browser/migrationWizard.ftl` — A button action label is rendered in the passive/past form ("Imported from file") instead of an imperative.
  - Current: `Diimpor dari Berkas`
  - en-US: `Impor dari Berkas`
  - All neighbouring buttons use the imperative ("Impor", "Pilih Berkas"); "Diimpor" states a completed state rather than the action the button performs.
- `colorways-cfr-header-14days` — `browser/browser/newtab/asrouter.ftl` — “kedaluarsa” is misspelled; the standard form is “kedaluwarsa”.
  - Current: `kedaluarsa dalam dua minggu`
  - en-US: `kedaluwarsa dalam dua minggu`
  - KBBI spelling is “kedaluwarsa”, used correctly elsewhere in the tree.
- `colorways-cfr-header-28days` — `browser/browser/newtab/asrouter.ftl` — “kedaluarsa” is misspelled; the standard form is “kedaluwarsa”.
  - Current: `kedaluarsa pada 16 Januari`
  - en-US: `kedaluwarsa pada 16 Januari`
  - KBBI spelling is “kedaluwarsa”, which the tree uses correctly elsewhere (newtab-report-content-outdated = “Kedaluwarsa”).
- `colorways-cfr-header-7days` — `browser/browser/newtab/asrouter.ftl` — “kedaluarsa” is misspelled; the standard form is “kedaluwarsa”.
  - Current: `kedaluarsa minggu ini`
  - en-US: `kedaluwarsa minggu ini`
  - KBBI spelling is “kedaluwarsa”, used correctly elsewhere in the tree.
- `colorways-cfr-header-today` — `browser/browser/newtab/asrouter.ftl` — “kedaluarsa” is misspelled; the standard form is “kedaluwarsa”.
  - Current: `kedaluarsa hari ini`
  - en-US: `kedaluwarsa hari ini`
  - KBBI spelling is “kedaluwarsa”, used correctly elsewhere in the tree.
- `newtab-pocket-cta-text` — `browser/browser/newtab/newtab.ftl` — The polite pronoun “Anda” is written in lowercase.
  - Current: `cerita yang anda sukai`
  - en-US: `cerita yang Anda sukai`
  - Indonesian orthography (and the rest of this file, including the second half of this same string) capitalises “Anda”.
- `newtab-weather-menu-change-temperature-units-celsius` — `browser/browser/newtab/newtab.ftl` — The temperature unit is misspelled “Celcius”.
  - Current: `Beralih ke Celcius`
  - en-US: `Beralih ke Celsius`
  - Same misspelling as newtab-weather-menu-temperature-option-celsius; the correct form is “Celsius”.
- `newtab-weather-menu-temperature-option-celsius` — `browser/browser/newtab/newtab.ftl` — The temperature unit is misspelled “Celcius”.
  - Current: `Celcius`
  - en-US: `Celsius`
  - The Indonesian spelling of the unit, like the English source, is “Celsius”; “Celcius” is a common misspelling.
- `places-maintenance-button` — `browser/browser/places.ftl` — Stray single low-quotation character at the end of the tooltip.
  - Current: `Impor dan cadangkan markah Anda‚`
  - en-US: `Impor dan cadangkan markah Anda`
  - The trailing "‚" (U+201A) is not punctuation in the source and appears verbatim in the tooltip; same defect in places-maintenance-button-mac.
- `policy-AutofillCreditCardEnabled` — `browser/browser/policies/policies-descriptions.ftl` — Transposed letters make the phrase nonsense: “osi ptomatis” instead of “isi otomatis”.
  - Current: `Aktifkan osi ptomatis untuk metode pembayaran.`
  - en-US: `Aktifkan isi otomatis untuk metode pembayaran.`
  - policy-AutofillAddressEnabled correctly uses “isi otomatis” for “autofill”; here the initial letters of the two words were swapped.
- `policy-EnableTrackingProtection` — `browser/browser/policies/policies-descriptions.ftl` — Uses the free pronoun “ia” as a direct object, which is ungrammatical in Indonesian.
  - Current: `kunci ia secara opsional`
  - en-US: `kuncilah secara opsional`
  - “ia” cannot function as an object; the enclitic “-nya” is required. Compare the parallel policy-EncryptedMediaExtensions, which has the same problem with “dia”.
- `policy-EncryptedMediaExtensions` — `browser/browser/policies/policies-descriptions.ftl` — Uses “dia” (a personal pronoun for people) to refer to a setting.
  - Current: `kunci dia secara opsional`
  - en-US: `kuncilah secara opsional`
  - “dia” refers to persons and cannot be used as an object pronoun for an inanimate setting; the enclitic “-nya” is required.
- `containers-name-text` — `browser/browser/preferences/containers.ftl` — "Masukan" (noun: input) used where the imperative verb "Masukkan" is required
  - Current: `Masukan nama kontainer`
  - en-US: `Masukkan nama kontainer`
  - The imperative of "memasukkan" is "masukkan" with double k; "masukan" is the noun "input/feedback". Other files in this partition use the correct form (e.g. permissions-doh-entry-field "Masukkan nama domain situs web").
- `fonts-allow-own` — `browser/browser/preferences/fonts.ftl` — "daripada" written as two words
  - Current: `dari pada menggunakan pilihan Anda di atas`
  - en-US: `daripada menggunakan pilihan Anda di atas`
  - In standard Indonesian orthography the comparative conjunction is written as one word, "daripada".
- `autofill-edit-card-password-prompt` — `browser/browser/preferences/formAutofill.ftl` — macOS variant adds a period the OS also appends
  - Current: `[macos] menampilkan informasi kartu kredit.`
  - en-US: `[macos] menampilkan informasi kartu kredit`
  - The developer comment states macOS prepends "Firefox is trying to " and adds a period at the end; en-US therefore has no final period. The localized variant ends with one, producing a double period in the OS dialog.
- `autofill-creditcard-os-dialog-message` — `browser/browser/preferences/preferences.ftl` — macOS variant adds a period the OS also appends
  - Current: `[macos] mengubah setelan metode pembayaran.`
  - en-US: `[macos] mengubah setelan metode pembayaran`
  - The developer comment says the macOS string is preceded by "Firefox is trying to " and the OS supplies the sentence-final punctuation; en-US has no trailing period, so the added one duplicates it.
- `home-homepage-custom-url` — `browser/browser/preferences/preferences.ftl` — Three periods used instead of the ellipsis character
  - Current: `Tempel URL...`
  - en-US: `Tempel URL…`
  - en-US is "Paste a URL…" with an ellipsis character, and the rest of the localized file uses … consistently.
- `permissions-autoplay-settings` — `browser/browser/preferences/preferences.ftl` — Three periods used instead of the ellipsis character
  - Current: `Pengaturan...`
  - en-US: `Pengaturan…`
  - Every other "Settings…"-type label in this file (permissions-xr-settings, permissions-speaker-settings, history-clear-on-close-settings, …) uses the ellipsis character …, matching en-US.
- `startup-windows-launch-on-login-profile-disabled` — `browser/browser/preferences/preferences.ftl` — Closing curly quotes typed as opening quotes
  - Current: `“{ profile-manager-use-selected.label }“ di jendela “Pilih Profil Pengguna“`
  - en-US: `“{ profile-manager-use-selected.label }” di jendela “Pilih Profil Pengguna”`
  - Both quoted phrases close with the left double quotation mark “ instead of the right one ”; en-US and the rest of the file use properly paired “…”.
- `windows-launch-on-login-profile-disabled` — `browser/browser/preferences/preferences.ftl` — Closing curly quotes typed as opening quotes
  - Current: `“{ profile-manager-use-selected.label }“ di jendela “Pilih Profil Pengguna“`
  - en-US: `“{ profile-manager-use-selected.label }” di jendela “Pilih Profil Pengguna”`
  - Same mismatched quotation marks as in startup-windows-launch-on-login-profile-disabled; the closing mark must be ”.
- `bar-tooltip-cryptominer` — `browser/browser/protections.ftl` — Missing spaces around the label in the screen-reader string.
  - Current: `{ $count }Penambang Kripto({ $percentage }%)`
  - en-US: `{ $count } Penambang Kripto ({ $percentage }%)`
  - All sibling aria-labels in the same section keep spaces around the count and the percentage.
- `cryptominer-tab-content` — `browser/browser/protections.ftl` — Capitalization errors: "Komputer" capitalized mid-sentence and the polite pronoun "Anda" written lowercase.
  - Current: `membuat Komputer anda lambat`
  - en-US: `memperlambat komputer Anda`
  - Indonesian capitalizes the honorific "Anda" and not common nouns mid-sentence; the rest of the file consistently writes "komputer Anda".
- `sidebar-history-context-menu-bookmark-page` — `browser/browser/sidebar.ftl` — Spelling error in the context-menu label.
  - Current: `Markahl Laman…`
  - en-US: `Markahi Laman…`
  - "Markahl" is a typo of "Markahi", the form used everywhere else (places.ftl, tabContextMenu.ftl).
- `tabbrowser-confirm-close-tabs-with-key-checkbox` — `browser/browser/tabbrowser.ftl` — Wrong preposition makes the checkbox read "Confirm before quitting from Ctrl+Q".
  - Current: `Konfirmasi sebelum keluar dari { $quitKey }`
  - en-US: `Konfirmasi sebelum keluar dengan { $quitKey }`
  - en-US is "quitting with {$quitKey}"; the parallel string tabbrowser-ask-close-tabs-with-key-checkbox correctly uses "dengan".
- `webrtc-item-microphone` — `browser/browser/webrtcIndicator.ftl` — Spelling error: "mikrofone" instead of "mikrofon".
  - Current: `mikrofone`
  - en-US: `mikrofon`
  - Every other string in the same file spells it "mikrofon".
- `protections.blocking.cookies.trackers.title` — `browser/chrome/browser/browser.properties` — "Cross-Site Tracking Cookies" shortened to "Kuki Pelacakan Lintas", dropping "Situs".
  - Current: `Kuki Pelacakan Lintas Diblokir`
  - en-US: `Kuki Pelacakan Lintas Situs Diblokir`
  - Inconsistent with contentBlocking.cookiesView.trackers2.label in the same panel, and "Lintas" without a noun is incomplete.
- `protections.notBlocking.crossSiteTrackingCookies.title` — `browser/chrome/browser/browser.properties` — "Cross-Site Tracking Cookies" shortened to "Kuki Pelacakan Lintas", dropping "Situs".
  - Current: `Tidak Memblokir Kuki Pelacakan Lintas`
  - en-US: `Tidak Memblokir Kuki Pelacakan Lintas Situs`
  - Same panel uses "Kuki Pelacakan Lintas Situs"; the shortened form is incomplete.
- `trackingProtection.icon.activeTooltip2` — `browser/chrome/browser/browser.properties` — "Cross-site tracking cookies" shortened to "kuki pelacakan lintas", dropping "situs".
  - Current: `kuki pelacakan lintas`
  - en-US: `kuki pelacakan lintas situs`
  - Elsewhere in the same panel the term is "Kuki Pelacakan Lintas Situs" (contentBlocking.cookies.blockingTrackers3.label); "lintas" alone is a preposition-like modifier with no noun and is not a valid rendering.
- `permission.midi-sysex.label` — `browser/chrome/browser/sitePermissions.properties` — "MIDI devices" rendered "Peranti MIDI" here but "Perangkat MIDI" in the adjacent permission.midi.label.
  - Current: `Mengakses Peranti MIDI dengan Dukungan SysEx`
  - en-US: `Mengakses Perangkat MIDI dengan Dukungan SysEx`
  - The two labels sit next to each other in the same list; the file otherwise uses "Perangkat" (e.g. permission.xr.label).
- `boxmodel.propertiesLabel` — `devtools/client/boxmodel.properties` — "Box Model" rendered with reversed word order compared with the panel title.
  - Current: `Properti Kotak Model`
  - en-US: `Properti Model Kotak`
  - boxmodel.title in the same file uses "Model Kotak"; "Kotak Model" means "model box" and is inconsistent within the same panel.
- `compatibility-issue-deprecated-prefixneeded` — `devtools/client/compatibility.ftl` — "deprecated" rendered two different ways in the same label group.
  - Current: `(tidak disarankan, prefiks dibutuhkan)`
  - en-US: `(usang, diperlukan prefiks)`
  - compatibility-issue-deprecated and compatibility-issue-deprecated-experimental use "usang" for the same en-US term in the same badge set, so the combined labels look like a different issue type.
- `settings.toggleSourceMaps.label` — `devtools/client/debugger.properties` — "Source Maps" rendered with reversed word order, inconsistent with the rest of the file.
  - Current: `Sumber Peta`
  - en-US: `Peta Sumber`
  - "Sumber Peta" means "map source"; the same file uses the correct "Peta Sumber" in sourceFooter.sourceMapButton.* and in settings.enableSourceMapIgnoreList.tooltip.
- `layout.toggleGridHighlighter` — `devtools/client/layout.properties` — "Grid" translated as "Kisi" in one string while the rest of the panel keeps "Grid".
  - Current: `Jungkitkan Penyorot Kisi`
  - en-US: `Aktifkan/Nonaktifkan Penyorot Grid`
  - layout.header, layout.overlayGrid, layout.gridDisplaySettings and layout.cannotShowGridOutline.title all keep "Grid"; the toggle wording also differs from flexbox.togglesFlexboxHighlighter2 ("Aktifkan/Nonaktifkan").
- `options-disable-http-cache-tooltip` — `devtools/client/toolbox-options.ftl` — "Service Workers" literally translated here but kept in English elsewhere in the same panel.
  - Current: `Layanan Pekerja tidak terpengaruh oleh opsi ini.`
  - en-US: `Service Worker tidak terpengaruh oleh opsi ini.`
  - options-enable-service-workers-http-label in the same file keeps "Service Worker"; "Layanan Pekerja" ("worker service") is not recognisable as the API name.
- `mathmltable` — `dom/chrome/accessibility/AccessFu.properties` — "table" left in English/misspelled where the file uses "tabel".
  - Current: `mathmltable = table matematika`
  - en-US: `mathmltable = tabel matematika`
  - Line 17 of the same file translates table as "tabel"; "table matematika" is a spelling error.
- `basicHttpAuthDisabled` — `dom/chrome/appstrings.properties` — Typo "tersebit".
  - Current: `situs tersebit`
  - en-US: `situs tersebut`
  - Misspelling of "tersebut" in a user-facing network error page.
- `UseOfReleaseEventsWarning` — `dom/chrome/dom/dom.properties` — Typo "usangi".
  - Current: `Penggunaan releaseEvents() sudah usangi.`
  - en-US: `Penggunaan releaseEvents() sudah usang.`
  - "usangi" is not a word; the parallel string UseOfCaptureEventsWarning correctly uses "sudah usang".
- `ImageTitleWithDimensions2` — `dom/chrome/layout/MediaDocument.properties` — The word "Image" is both translated and left in English.
  - Current: `(Gambar %S Image, %S × %S piksel)`
  - en-US: `(Gambar %S, %S × %S piksel)`
  - Same duplication as ImageTitleWithDimensions2AndFile; the other two entries in the file correctly use only "Gambar %S".
- `ImageTitleWithDimensions2AndFile` — `dom/chrome/layout/MediaDocument.properties` — The word "Image" is both translated and left in English.
  - Current: `%S (Gambar %S Image, %S × %S piksel)`
  - en-US: `%S (Gambar %S, %S × %S piksel)`
  - en-US is "%S (%S Image, ...)"; the localized title duplicates the noun, producing e.g. "Gambar PNG Image".
- `PEMQNoMinMaxWithoutValue` — `dom/chrome/layout/css.properties` — Typo "wajin".
  - Current: `wajin memiliki sebuah nilai`
  - en-US: `wajib memiliki sebuah nilai`
  - Misspelling of "wajib".
- `CompositorAnimationWarningHasCurrentColor` — `dom/chrome/layout/layout_errors.properties` — Typo "kompsitor".
  - Current: `tidak dapat dijalankan pada kompsitor`
  - en-US: `tidak dapat dijalankan pada kompositor`
  - Misspelling of "kompositor".
- `CompositorAnimationWarningOpacityFrameInactive` — `dom/chrome/layout/layout_errors.properties` — Typo "baigan".
  - Current: `tidak ditandai aktif pada baigan animasi ‘opacity’`
  - en-US: `tidak ditandai aktif pada bagian animasi ‘opacity’`
  - Misspelling of "bagian"; the parallel string CompositorAnimationWarningTransformFrameInactive spells it correctly.
- `writeError` — `dom/chrome/nsWebBrowserPersist.properties` — Typo "lokasi lainn".
  - Current: `Coba menyimpan di lokasi lainn.`
  - en-US: `Coba menyimpan di lokasi lain.`
  - Trailing extra "n" in a user-facing save error.
- `reportURInotInReportOnlyHeader` — `dom/chrome/security/csp.properties` — Typo "oatas".
  - Current: `melaporkan pelanggaran oatas kebijakan ini`
  - en-US: `melaporkan pelanggaran atas kebijakan ini`
  - Misspelling of "atas".
- `FeaturePolicyUnsupportedFeatureName` — `dom/chrome/security/security.properties` — Capitalization typo "FItur".
  - Current: `Kebijakan FItur:`
  - en-US: `Kebijakan Fitur:`
  - Stray capital I; the two adjacent FeaturePolicy strings spell it "Kebijakan Fitur".
- `username` — `mobile/android/chrome/passwordmgr.properties` — Typo "Name Pengguna".
  - Current: `username = Name Pengguna`
  - en-US: `username = Nama Pengguna`
  - English "Name" left in place of "Nama" in a login prompt label.
- `SSL_ERROR_INAPPROPRIATE_FALLBACK_ALERT` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo "menilah" for "menolak".
  - Current: `Server menilah handshake`
  - en-US: `Server menolak handshake`
  - "menilah" is not a word; en-US is "The server rejected the handshake".
- `pageInfo_WeakCipher` — `security/manager/chrome/pippki/pippki.properties` — Typo "leman".
  - Current: `menggunakan enkripsi leman`
  - en-US: `menggunakan enkripsi lemah`
  - Misspelling of "lemah" in a user-facing security warning.
- `pippki-pw-empty-warning` — `security/manager/security/pippki/pippki.ftl` — Duplicated auxiliary: "akan tidak akan dilindungi".
  - Current: `Sandi dan kunci pribadi yang Anda simpan akan tidak akan dilindungi.`
  - en-US: `Sandi dan kunci pribadi yang Anda simpan tidak akan dilindungi.`
  - Ungrammatical duplication of "akan".
- _…and 18 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — The quoted button name does not match the actual translated button label.
  - Current: `pilih “Sinkronkan ke seluler”`
  - en-US: `pilih “Sinkronkan ke ponsel”`
  - The quoted string refers to sync-to-mobile-button-label, which is translated as “Sinkronkan ke ponsel”; users are told to look for a control that does not exist under that name.
- `connection-dns-over-https-custom-label` — `browser/browser/preferences/connection.ftl` — "Custom" rendered two different ways in the same dialog
  - Current: `Ubahsuai`
  - en-US: `Khusus`
  - In the same Connection Settings dialog, connection-dns-over-https-url-custom translates "Custom" as "Khusus" (as does addEngine's "Tambahkan Mesin Khusus"); this label uses "Ubahsuai" for the very same control.
- `permissions-exceptions-https-only-window2` — `browser/browser/preferences/permissions.ftl` — "HTTPS-Only Mode" left in English in the title while the dialog body translates it
  - Current: `Pengecualian - Mode HTTPS-Only`
  - en-US: `Pengecualian - Mode Hanya HTTPS`
  - The two description strings in the same dialog use "Mode HTTPS-Saja", and preferences.ftl consistently uses "Mode Hanya HTTPS" (httpsonly-header and all httpsonly-radio-* strings). Leaving "HTTPS-Only" untranslated in the window title of the same surface is inconsistent.
- `preonboarding-subtitle` — `browser/browser/preonboarding.ftl` — "Terms of Use" is rendered "Persyaratan Penggunaan" while the buttons on the very same screen say "Ketentuan Penggunaan".
  - Current: `Persyaratan Penggunaan`
  - en-US: `Ketentuan Penggunaan`
  - termsofuse.ftl and the other preonboarding strings consistently use "Ketentuan Penggunaan" for the same legal document.
- `preonboarding-terms-of-use-header-button-title-b` — `browser/browser/preonboarding.ftl` — A third rendering of "Terms of Use" ("Syarat Penggunaan") on the same screen.
  - Current: `Syarat Penggunaan`
  - en-US: `Ketentuan Penggunaan`
  - The B-variant button sits in the same surface as preonboarding-terms-of-use-header-button-title ("Ketentuan Penggunaan").
- `bar-tooltip-fingerprinter` — `browser/browser/protections.ftl` — The graph tooltip names the fingerprint ("Sidik Jari") rather than the fingerprinters, and differs from "Pelacak Sidik" used for the same category in the same dashboard.
  - Current: `Sidik Jari`
  - en-US: `Pelacak Sidik Jari`
  - fingerprinter-tab-title in the same file uses "Pelacak Sidik"; "Sidik Jari" alone denotes the fingerprint, not the actor being counted.
- `protections-panel-content-blocking-tracking-protection` — `browser/browser/protectionsPanel.ftl` — "Tracking Content" is inverted to "content tracking", conflicting with the same term elsewhere in the protections UI.
  - Current: `Pelacakan Konten`
  - en-US: `Konten Pelacakan`
  - protections.ftl tracker-tab-title and siteProtections.ftl use "Konten Pelacak(an)" for the same category; "Pelacakan Konten" reverses head and modifier.
- `sidebar-context-menu-customize-sidebar` — `browser/browser/sidebar.ftl` — "Sidebar" is "Bilah Sisi" here but "Bilah Samping" in the adjacent item of the same context menu.
  - Current: `Ubahsuai Bilah Sisi`
  - en-US: `Ubahsuai Bilah Samping`
  - sidebar-context-menu-hide-sidebar, sidebarMenu.ftl and menubar.ftl all use "Bilah Samping"; the two terms alternate inside one menu.
- `sidebar-menu-open-ai-chatbot-tooltip-generic` — `browser/browser/sidebar.ftl` — "AI chatbot" is left as "chatbot AI" in the tooltips while the matching menu labels translate it as "Bot obrolan AI".
  - Current: `Buka chatbot AI`
  - en-US: `Buka bot obrolan AI`
  - sidebar-menu-genai-chat-label and menu-view-genai-chat in the same file use "Bot obrolan AI" for the identical item.
- `unpin-tab` — `browser/browser/tabContextMenu.ftl` — "Unpin Tab" uses a different metaphor ("Tab Permanen") than the neighbouring pin/unpin items.
  - Current: `Copot dari Tab Permanen`
  - en-US: `Lepas Sematan Tab`
  - pin-tab is "Sematkan Tab" and unpin-selected-tabs is "Lepas Sematan Tab" in the same menu.
- `tabbrowser-context-mute-selected-tabs` — `browser/browser/tabbrowser.ftl` — Mute/unmute use different verbs in the same context menu ("Senyapkan/Bunyikan" vs "Bisukan/Suarakan").
  - Current: `Senyapkan Tab`
  - en-US: `Bisukan Tab`
  - tabbrowser-context-mute-tab (shown in the same menu, and required by comment to share the access key) uses "Bisukan Tab".
- `history-panelmenu.tooltiptext2` — `browser/chrome/browser/customizableui/customizableWidgets.properties` — Missing space before the shortcut parenthesis.
  - Current: `Tampilkan riwayat Anda(%S)`
  - en-US: `Tampilkan riwayat Anda (%S)`
  - Every other shortcut tooltip in this file and in browser.properties places a space before "(%S)".
- `dialogTitleEdit` — `browser/chrome/browser/places/bookmarkProperties.properties` — Straight ASCII quotes used where en-US and every other quoted string in this file use curly quotes.
  - Current: `Properti untuk "%S"`
  - en-US: `Properti untuk “%S”`
  - dialogTitleEditBookmark in the same file uses “%S”; en-US uses curly quotes throughout.
- `about-networking-http-clear-cache-button` — `toolkit/toolkit/about/aboutNetworking.ftl` — "Cache" rendered "Singgahan" here but "Tembolok" in the adjacent DNS button.
  - Current: `about-networking-http-clear-cache-button = Bersihkan Singgahan HTTP`
  - en-US: `about-networking-http-clear-cache-button = Bersihkan Tembolok HTTP`
  - "Singgahan" occurs exactly once in the whole locale tree, while "Tembolok" is the established term (used in the very next line, about-networking-dns-clear-cache-button, and throughout aboutSupport/url-classifier).
- `text-copied` — `toolkit/toolkit/about/aboutSupport.ftl` — "clipboard" left in English where the same page uses "papan klip".
  - Current: `text-copied = Teks telah disalin ke clipboard`
  - en-US: `text-copied = Teks telah disalin ke papan klip`
  - The adjacent raw-data-copied string and the copy buttons in the same file all use "papan klip".
- `findbar-entire-word` — `toolkit/toolkit/main-window/findbar.ftl` — "Whole Words" is labelled "Seluruh Teks" while its own status string says "seluruh kata".
  - Current: `Seluruh Teks`
  - en-US: `Seluruh Kata`
  - findbar-entire-word-status in the same file reads "(Hanya seluruh kata)"; the label and the status text of the same toggle contradict each other, and the label version is the wrong one.
- `cert-error-symantec-distrust-description` — `toolkit/toolkit/neterror/certError.ftl` — "pewenang otoritas" is a garbled rendering of "certificate authorities".
  - Current: `pewenang otoritas`
  - en-US: `otoritas sertifikat`
  - en-US: "certificates, which are issued by certificate authorities". The rest of the file uses "otoritas sertifikat"; "pewenang otoritas" says "authority authority" and drops "certificate".

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
