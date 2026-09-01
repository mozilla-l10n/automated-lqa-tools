# Android l10n QA — id

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f39118d70d88` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f39118d70d88` |
| **Previous run** | 2026-08-24 @ `e8622a909368` |
| **Mode** | incremental |
| **Strings reviewed this run** | 103 of 2,586 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for id: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (5)

- `mozac_feature_summarize_feedback_state_submitted` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-in/strings.xml` — "Rating submitted" is translated as "Peringkat dikirim", which means "ranking sent" rather than the user's rating/feedback being submitted.
    - Current: `Peringkat dikirim`
    - Source: `Rating submitted`
    - Suggest: `Penilaian terkirim`
    - In this context "rating" is the user's thumbs up/down feedback ("penilaian"), not a rank/position ("peringkat"). Related strings use "menilai ringkasan", so "penilaian" is the consistent term.
- `preferences_show_search_optimization_cards` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Retrieve suggestions from Mozilla as you type" is rendered with "Dapatkan" (get/obtain) instead of the retrieval action; acceptable meaning shift is minor but the imperative changes who acts.
    - Current: `Dapatkan saran dari Mozilla saat Anda mengetik`
    - Source: `Retrieve suggestions from Mozilla as you type`
    - Suggest: `Ambil saran dari Mozilla saat Anda mengetik`
    - Source describes the app retrieving suggestions from Mozilla; "Dapatkan" reads as the user obtaining them.
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Navigate back" rendered as "Navigasi balik", which is not the standard Indonesian wording for a back navigation control.
    - Current: `Navigasi balik`
    - Source: `Navigate back`
    - Suggest: `Navigasi kembali`
    - "balik" means flip/turn over in this register; the established term for going back is "kembali". Screen readers will announce an odd phrase.
- `ip_protection_toolbar_pill_label` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "VPN on" rendered with "hidup" while the parallel badge strings use "Nyala"/"Mati", creating inconsistent terminology on the same surface.
    - Current: `VPN hidup`
    - Source: `VPN on`
    - Suggest: `VPN nyala`
    - preferences_ip_protection_on translates "On" as "Nyala" and the paired label ip_protection_toolbar_pill_label_off uses "mati"; "hidup" is inconsistent for the same on/off state term.
- `ip_protection_get_started` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Button label "Get started" translated as the gerund/progressive "Memulai" instead of an imperative button label.
    - Current: `Memulai`
    - Source: `Get started`
    - Suggest: `Mulai`
    - The developer comment says this is a button label that starts a flow; Indonesian button labels use the imperative "Mulai", as with other imperative labels in this batch (Buka, Unduh, Cetak).

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (10)

- `add_custom_autocomplete_label` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "Add link to autocomplete" (add the link to the autocomplete list) is rendered as "add link to be autocompleted".
    - Current: `Tambahkan tautan untuk dilengkapi secara otomatis`
    - Suggest: `Tambahkan tautan ke pelengkapan otomatis`
    - The developer comment says the button quick-adds the current URL to the custom autocomplete list; the target instead says the link will be autocompleted.
- `cookie_banner_report_a_site_snackbar_label` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "Request to support site" is rendered as "Permintaan bantuan situs" (request for site help), reversing the meaning of the user requesting that the site be supported.
    - Current: `Permintaan bantuan situs telah diajukan.`
    - Suggest: `Permintaan dukungan untuk situs ini telah diajukan.`
    - The source means a request was submitted asking the team to add support for the site, not a request for help from the site.
- `cookie_banner_the_site_was_reported` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "Request to support site" is rendered as "Permintaan bantuan situs" (request for site help), reversing the meaning of the user requesting that the site be supported.
    - Current: `Permintaan bantuan situs telah diajukan.`
    - Suggest: `Permintaan dukungan untuk situs ini telah diajukan.`
    - The source means a request was submitted asking the team to add support for the site, not a request for help from the site.
- `firstrun_privacy_text` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "default browser" is rendered as "peramban utama" while "default" is rendered "baku" elsewhere in the same onboarding flow.
    - Current: `sebagai peramban utama Anda`
    - Suggest: `sebagai peramban baku Anda`
    - The neighbouring string firstrun_search_text translates "default search engine" as "mesin pencari baku"; "default" should be consistently "baku".
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — `firstrun_shortcut_text` quotes “Tambahkan ke layar Beranda” but the string it names, `menu_add_to_home_screen`, reads “Tambahkan ke Beranda”
    - Current: `Kembali ke situs favorit Anda di %1$s dengan cepat. Cukup pilih "Tambahkan ke layar Beranda" dari menu %1$s.`
    - Suggest: `Tambahkan ke Beranda`
    - In the source this string quotes “Add to Home screen”, which is exactly the value of `menu_add_to_home_screen` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preference_autocomplete_custom_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Word order makes the phrase mean "custom autocomplete URLs" incorrectly; the modifier attaches to the wrong noun.
    - Current: `Tambahkan dan kelola lengkapi-otomatis URL ubahsuai.`
    - Suggest: `Tambahkan dan kelola URL lengkapi-otomatis ubahsuai.`
    - Source is "Add and manage custom autocomplete URLs"; the Indonesian head noun should be URL, not "lengkapi-otomatis".
- `preference_open_new_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Meaning reversed: the source says switch to the link's new tab immediately, target says move the link to a new tab.
    - Current: `Alihkan tautan langsung ke tab baru`
    - Suggest: `Langsung beralih ke tautan di tab baru`
    - Per the developer comment the preference is about switching to a new tab immediately after opening; the target instead reads as moving/redirecting the link to a new tab.
- `tab_crash_report_title` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "Tab Crashed" translated as "Tab Mogok", an unusual term for a software crash.
    - Current: `Tab Mogok`
    - Suggest: `Tab Mengalami Kegagalan`
    - "Mogok" means to break down/strike and is not the established Indonesian term for an application crash; Mozilla id normally uses "macet"/"gagal".
- `tip_disable_tips2` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Adds "ini" (this/these) not present in the source.
    - Current: `Nonaktifkan tips ini pada layar mulai`
    - Suggest: `Nonaktifkan tips pada layar mulai`
    - Source is "Turn off tips on the start screen" — no demonstrative; the translation says "these tips".
- `tip_disable_tracking_protection` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "Try turning off" is rendered as an imperative "Matikan", dropping the tentative "Try".
    - Current: `Matikan Perlindungan Pelacakan`
    - Suggest: `Coba matikan Perlindungan Pelacakan`
    - The source suggests trying to turn off Tracking Protection; the translation is a plain command, losing "Try".

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 43 |
| Strings | 2,586 |
| Missing strings | 149 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 1 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**149 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — 141
- `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — 8

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 11, `straight-double` 5 | _mixed_ |
| ellipsis | `char` 20 | **char** |
| dash | `em` 3 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (160)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 91 |
| 3 | Degraded language (grammar, spelling, terminology) | 65 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_engine_system_alert_title` — `mozilla-mobile/android-components/components/browser/engine-system/src/main/res/values-in/strings.xml` — "The page at %1$s says:" is rendered as "Laman dari %1$s menjelaskan:", which changes the meaning and preposition.
    - Current: `Laman dari %1$s menjelaskan:`
    - Source: `The page at %1$s says:`
    - Suggest: `Laman di %1$s mengatakan:`
    - The source means the page located at the URL says something; "dari" (from) and "menjelaskan" (explains) misrepresent it, and the parallel string mozac_browser_engine_system_auth_message uses "mengatakan".
- `mozac_browser_errorpages_content_crashed_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "website owners" is translated as "pengguna situs Web" (website users) instead of owners.
    - Current: `Silakan hubungi pengguna situs Web untuk mengabarkan masalah ini kepada mereka.`
    - Source: `{ <p> }The page you are trying to view cannot be shown because an error in the data transmission was detected.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } { </ul> }`
    - Suggest: `Silakan hubungi pemilik situs web untuk mengabarkan masalah ini kepada mereka.`
    - The source says to contact the website owners; "pengguna" means users, which is the wrong party.
- `mozac_browser_errorpages_httpsonly_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — The coordinating conjunction "and" is rendered as the adversative "tetapi" (but).
    - Current: `untuk keamanan yang ditingkatkan tetapi versi HTTPS`
    - Source: `You’ve enabled HTTPS-Only Mode for enhanced security, and a HTTPS version of { <em> }%1$s{ </em> } is not available.`
    - Suggest: `untuk keamanan yang ditingkatkan, dan versi HTTPS`
    - The source joins the two clauses with "and"; "tetapi" adds a contrast not present in the source.
- `mozac_browser_errorpages_invalid_content_encoding_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "website owners" is translated as "pengguna situs Web" (website users) instead of owners.
    - Current: `Silakan hubungi pengguna situs Web untuk mengabarkan masalah ini kepada mereka.`
    - Source: `{ <p> }The page you are trying to view cannot be shown because it uses an invalid or unsupported form of compression.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } {…`
    - Suggest: `Silakan hubungi pemilik situs web untuk mengabarkan masalah ini kepada mereka.`
    - The source says to contact the website owners; "pengguna" means users, which is the wrong party.
- `mozac_browser_errorpages_malformed_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "The provided address" is translated as "Laman yang diberikan" (the provided page).
    - Current: `Laman yang diberikan tidak dalam format yang dikenali.`
    - Source: `{ <p> }The provided address is not in a recognized format. Please check the location bar for mistakes and try again.{ </p> }`
    - Suggest: `Alamat yang diberikan tidak dalam format yang dikenali.`
    - The source refers to the address (URL), not the page; the title of the same error page uses "Alamat".
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "Is your device or network protected by a firewall or proxy?" renders "device" as "komputer".
    - Current: `Apakah jaringan atau komputer Anda dilindungi firewall atau proxy?`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `Apakah jaringan atau perangkat Anda dilindungi firewall atau proxy?`
    - The source refers to the user's device, not a computer.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "device" is translated as "komputer" (computer) in a mobile browser string.
    - Current: `Apakah komputer terhubung pada jaringan aktif?`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `Apakah perangkat terhubung pada jaringan aktif?`
    - The source says "Is the device connected to an active network?"; "komputer" names the wrong thing on a mobile app.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "your device" is translated as "komputer Anda" (your computer).
    - Current: `bukan masalah pada komputer Anda`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `bukan masalah pada perangkat Anda`
    - The source says "not your device"; the target says computer.
- `mozac_browser_errorpages_security_bad_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "connected to this server successfully in the past" loses "to this server".
    - Current: `Jika Anda pernah tersambung dengan baik`
    - Source: `{ <ul> } { <li> }This could be a problem with the server’s configuration, or it could be someone trying to impersonate the server.{ </li> } { <li> }If you have connected to this server successfully in the past, the erro…`
    - Suggest: `Jika Anda pernah berhasil tersambung ke server ini sebelumnya`
    - The source specifies connecting to this server in the past; the target drops the object, making the sentence vague.
- `mozac_browser_errorpages_security_ssl_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "authenticity" is translated as "otentikasi" (authentication).
    - Current: `karena otentikasi data yang diterima tidak dapat diverifikasi`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because the authenticity of the received data could not be verified.{ </li> } { <li> }Please contact the website owners to inform them of this problem.{ <…`
    - Suggest: `karena keaslian data yang diterima tidak dapat diverifikasi`
    - The source says "the authenticity of the received data"; "otentikasi" means authentication, a different concept.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "for assistance" is dropped from the last bullet.
    - Current: `Tanyakan pada administrator jaringan Anda atau Penyedia Jasa Layanan Internet (Internet Service Provider).`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Tanyakan pada administrator jaringan Anda atau Penyedia Jasa Layanan Internet (Internet Service Provider) untuk mendapatkan bantuan.`
    - The source ends with "for assistance", which is present in the parallel string mozac_browser_errorpages_proxy_connection_refused_message but omitted here.
- `mozac_feature_addons_permissions_browsing_data_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — "recent" is attached to the wrong noun, changing the meaning from "recent browsing history" to "recent related data".
    - Current: `Bersihkan riwayat penjelajahan, kuki, dan data terkait terkini.`
    - Source: `Clear recent browsing history, cookies, and related data.`
    - Suggest: `Bersihkan riwayat penjelajahan terkini, kuki, dan data terkait.`
    - The source is "Clear recent browsing history, cookies, and related data." — "recent" modifies "browsing history". The sibling string mozac_feature_addons_permissions_browser_data_description correctly renders it as "riwayat penjelajahan terbaru, kuki, dan data terkait".
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — "Extend developer tools to access your data" is rendered as "Perpanjang akses alat pengembang" (extend the access of dev tools), altering the meaning and using "perpanjang" (prolong in time) instead of "perluas".
    - Current: `Perpanjang akses alat pengembang ke data Anda di dalam tab terbuka`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `Perluas alat pengembang untuk mengakses data Anda di tab terbuka`
    - The source means extending the developer tools so they can access your data; the parallel string mozac_feature_addons_permissions_devtools_description_for_update correctly uses "Perluas alat pengembang untuk mengakses data Anda di tab terbuka."
- `mozac_feature_addons_permissions_notifications_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — "Display notifications to you" is rendered as "Tampilkan notifikasi untuk Anda", but the phrasing loses the sense of showing notifications to the user; more importantly it reads as "show notifications for you".
    - Current: `Tampilkan notifikasi untuk Anda.`
    - Source: `Display notifications to you.`
    - Suggest: `Tampilkan notifikasi kepada Anda.`
    - "to you" is the recipient of the notifications; Indonesian "kepada Anda" conveys the recipient, while "untuk Anda" means "on your behalf/for your benefit".
- `mozac_feature_addons_permissions_one_extra_domain_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — Adds "lagi" ("more/again"), which is not in the source "Access your data on another domain".
    - Current: `Akses data Anda di domain lain lagi`
    - Source: `Access your data on another domain`
    - Suggest: `Akses data Anda di domain lain`
    - The source has no additional "another/more" intensifier; "domain lain lagi" means "yet another domain" and also mismatches the parallel *_for_update string which correctly reads "di domain lain".
- `mozac_feature_addons_permissions_one_extra_site_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — Adds "lagi" ("more/again"), which is not in the source "Access your data on another site".
    - Current: `Akses data Anda di situs lain lagi`
    - Source: `Access your data on another site`
    - Suggest: `Akses data Anda di situs lain`
    - The source says simply "another site"; the parallel *_for_update string is correctly "di situs lain" without "lagi".
- `mozac_feature_addons_permissions_privacy_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — "Read" is translated as "Melihat" (view) instead of "Membaca", inconsistent with the sibling update string which uses "Baca".
    - Current: `Melihat dan mengubah pengaturan privasi`
    - Source: `Read and modify privacy settings`
    - Suggest: `Membaca dan mengubah pengaturan privasi`
    - Source says "Read and modify privacy settings"; the parallel _for_update string correctly uses "Baca".
- `mozac_feature_addons_supported_checker_notification_content_more_than_two` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — "Add them" is rendered without the object, losing the reference to the add-ons.
    - Current: `Tambahkan ke %1$s`
    - Source: `Add them to %1$s`
    - Suggest: `Tambahkan mereka ke %1$s`
    - Source is "Add them to %1$s", referring to the newly supported add-ons; the target drops "them" and reads as an incomplete "Add to Firefox".
- `mozac_feature_autofill_popup_unlock_application` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-in/strings.xml` — "Unlock %1$s" is translated as "Buka %1$s" (Open), losing the unlock meaning.
    - Current: `Buka %1$s`
    - Source: `Unlock %1$s`
    - Suggest: `Buka kunci %1$s`
    - The comment states the browser app needs to be unlocked; "Buka" means merely "open", not "unlock".
- `mozac_feature_contextmenu_download_link` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-in/strings.xml` — "Download link" (an action to save the link) is rendered as the noun phrase "Tautan unduhan" (download link/URL).
    - Current: `Tautan unduhan`
    - Source: `Download link`
    - Suggest: `Unduh tautan`
    - The developer comment says this is a context menu item to save / download the link, i.e. an imperative action, but the translation reads as a noun "the download's link".
- `mozac_feature_downloads_time_remaining` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-in/strings.xml` — Temporal "in %1$s" (time remaining) is translated as the locative "di" instead of the temporal "dalam".
    - Current: `di %1$s`
    - Source: `in %1$s`
    - Suggest: `dalam %1$s`
    - The developer comment says %1$s is the estimated time remaining, so "in" is temporal ("in 5 minutes"); Indonesian "di" means "at/in (a place)" and gives the wrong meaning.
- `mozac_feature_prompts_identity_credentials_privacy_policy_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-in/strings.xml` — "Use %1$s as a login provider" is translated as "Pilih" (choose) instead of "Gunakan" (use), and "login provider" is rendered inconsistently with the sibling string.
    - Current: `Pilih %1$s sebagai penyedia info masuk`
    - Source: `Use %1$s as a login provider`
    - Suggest: `Gunakan %1$s sebagai penyedia log masuk`
    - Source verb is "Use", not "Choose"; the related string mozac_feature_prompts_identity_credentials_choose_provider renders "login provider" as "penyedia log masuk".
- `search_widget_content_description` — `mozilla-mobile/android-components/components/feature/search/src/main/res/values-in/strings.xml` — Translation says "Open in a new Firefox tab" instead of "Open a new Firefox tab".
    - Current: `Buka di tab %1$s baru`
    - Source: `Open a new %1$s tab`
    - Suggest: `Buka tab %1$s baru`
    - The source is "Open a new %1$s tab"; the added preposition "di" changes the meaning to opening something in a tab rather than opening a new tab.
- `mozac_feature_summarize_feedback_state_submitted` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-in/strings.xml` — "Rating submitted" is translated as "Peringkat dikirim", which means "ranking sent" rather than the user's rating/feedback being submitted.
    - Current: `Peringkat dikirim`
    - Source: `Rating submitted`
    - Suggest: `Penilaian terkirim`
    - In this context "rating" is the user's thumbs up/down feedback ("penilaian"), not a rank/position ("peringkat"). Related strings use "menilai ringkasan", so "penilaian" is the consistent term.
- `mozac_lib_send_crash_report_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-in/strings.xml` — Progress notification "Sending crash report" is translated as an imperative "Kirim" (Send), identical to the checkbox label instead of the ongoing action.
    - Current: `Kirim laporan mogok ke %1$s`
    - Source: `Sending crash report to %1$s`
    - Suggest: `Mengirim laporan mogok ke %1$s`
    - The developer comment says this is a notification showing the crash report service is running; the source is the progressive "Sending…", parallel to "Mengumpulkan data mogok" for "Gathering…". "Kirim" is a command, matching "Send crash report" (the checkbox string) rather than "Sending".
- `about_crashes` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Crashes" (crash reports) is rendered as "Mogok", which in Indonesian means "strike/breakdown", not application crashes.
    - Current: `Mogok`
    - Source: `Crashes`
    - Suggest: `Kerusakan`
    - The link lists past application crashes (like about:crashes). "Mogok" means a labor strike or a stalled vehicle and does not convey software crashes; Mozilla id uses "Kerusakan"/"Laporan kerusakan".
- `addresses_pin` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Pin" (Postal Index Number, an Indian postal code field) is translated as the verb "Sematkan" (to pin/attach).
    - Current: `Sematkan`
    - Source: `Pin`
    - Suggest: `PIN`
    - The developer comment states this is the PIN (Postal Index Number) address field used in India, not the action of pinning something.
- `alternative_app_icon_option_gradient_blue_hour` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Blue Hour" is translated as "Nuansa Biru" (blue shade), dropping the "hour" time-of-day sense while the parallel "Golden Hour" keeps it.
    - Current: `Nuansa Biru`
    - Source: `Blue Hour`
    - Suggest: `Jam Biru`
    - Per the comment, "Blue Hour" refers to the time just after sunset/before sunrise; the sibling string "Golden Hour" was rendered as "Waktu Emas", so the time reference is inconsistently dropped here.
- `alternative_app_icon_option_pixelated` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Pixelated" is rendered as "Berkotak-kotak" (checkered/square-patterned), not the pixel-art meaning.
    - Current: `Berkotak-kotak`
    - Source: `Pixelated`
    - Suggest: `Piksel`
    - The developer comment says the icon features a pixel-art, retro 8-bit style; "berkotak-kotak" means checkered/plaid, which names a different visual style.
- `certificate_warning_homepage_card_hcr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "stop working properly" rendered as "berhenti bekerja" (stop working), dropping "properly".
    - Current: `menyebabkan versi Firefox Anda berhenti bekerja.`
    - Source: `A root certificate will expire, causing your version of Firefox to stop working properly.`
    - Suggest: `menyebabkan versi Firefox Anda berhenti berfungsi dengan semestinya.`
    - The source says Firefox will stop working properly, not stop working entirely; the parallel string hcw3 correctly uses "dengan semestinya".
- `close_tabs_manually` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Never" is translated as "Secara manual" (manually) instead of "Tidak pernah".
    - Current: `Secara manual`
    - Source: `Never`
    - Suggest: `Tidak pernah`
    - The source option label is "Never" (never auto-close tabs); the target says "Manually", which is the wording of the separate summary string close_tabs_manually_summary.
- `create_tab_group_name_label` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Label "Name" is expanded to "Nama grup tab" instead of simply "Nama".
    - Current: `Nama grup tab`
    - Source: `Name`
    - Suggest: `Nama`
    - The source label is just "Name" for the tab group name field; the translation adds words not present in the source.
- `credit_cards_expiration_date_year` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Expiration Date Year" is rendered as "Tanggal Tahun Kedaluwarsa", swapping the word order so it reads "Expiration Year Date".
    - Current: `Tanggal Tahun Kedaluwarsa`
    - Source: `Expiration Date Year`
    - Suggest: `Tahun Tanggal Kedaluwarsa`
    - The parallel string credit_cards_expiration_date_month uses "Bulan Tanggal Kedaluwarsa"; the year label should be "Tahun Tanggal Kedaluwarsa" for consistency and correct meaning.
- `customize_toggle_pocket_sponsored` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Sponsored stories" translated as "Konten bersponsor" (sponsored content), inconsistent with "Stories" = "Cerita".
    - Current: `Konten bersponsor`
    - Source: `Sponsored stories`
    - Suggest: `Cerita bersponsor`
    - The source says "stories", which is rendered "Cerita" in customize_toggle_pocket_3; "Konten" means content, changing the term.
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "selected locale" mistranslated as "pelokalan yang dipilih" (selected localization).
    - Current: `pelokalan yang dipilih`
    - Source: `Add new address for selected locale`
    - Suggest: `locale yang dipilih`
    - "Locale" here is the locale setting, translated as "Locale" in debug_drawer_addresses_debug_locales_header; "pelokalan" means localization (the process).
- `debug_drawer_regin_tools_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "home and current region" is rendered with untranslated "home" and "region" and misparses the phrase.
    - Current: `Menimpa sementara nilai home dan region saat ini untuk pengujian.`
    - Source: `Temporarily overrides the home and current region values for testing.`
    - Suggest: `Menimpa sementara nilai wilayah asal dan wilayah saat ini untuk pengujian.`
    - The source refers to the home region and the current region; other strings in the same feature use "wilayah asal" and "wilayah saat ini". Leaving "home" and "region" in English is inconsistent and changes the meaning.
- `default_device_name_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "on" (device) is translated as "dalam" instead of "di".
    - Current: `%1$s dalam %2$s %3$s`
    - Source: `%1$s on %2$s %3$s`
    - Suggest: `%1$s di %2$s %3$s`
    - The pattern is "Firefox on <manufacturer> <model>", i.e. the app running on a device; Indonesian uses "di", not "dalam".
- `download_navigate_back_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Navigate back" is rendered as "Arahkan kembali" ("point/aim back"), not the navigation action.
    - Current: `Arahkan kembali`
    - Source: `Navigate back`
    - Suggest: `Navigasi kembali`
    - The source is the content description for the toolbar back button; "Arahkan" means to direct/aim something, which does not convey going back. The sibling string download_navigate_settings_description correctly uses "Navigasikan ke".
- `etp_cookies_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "the site you’re on" is mistranslated as "situs yang Anda inginkan" (the site you want).
    - Current: `situs yang Anda inginkan`
    - Source: `Total Cookie Protection isolates cookies to the site you’re on so trackers like ad networks can’t use them to follow you across sites.`
    - Suggest: `situs yang sedang Anda buka`
    - Source means the site the user is currently on, not the site the user wants.
- `etp_known_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Known Fingerprinters" (entities that fingerprint users) is translated as "Sidik Jari yang Dikenal" (known fingerprints).
    - Current: `Sidik Jari yang Dikenal`
    - Source: `Known Fingerprinters`
    - Suggest: `Pengambil Sidik Jari yang Dikenal`
    - The developer comment states this is a category of trackers (fingerprinters), i.e. actors, not the fingerprints themselves.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Redirect Trackers" is rendered as an imperative verb phrase "Alihkan Pelacak" (Redirect the trackers) instead of a noun phrase naming the tracker category.
    - Current: `Alihkan Pelacak`
    - Source: `Redirect Trackers`
    - Suggest: `Pelacak Pengalihan`
    - The developer comment says this is a category of trackers (redirect trackers); the translation reads as a command "redirect trackers", reversing the head noun and meaning.
- `etp_suspected_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "stop suspected fingerprinters" is translated as stopping suspected fingerprints rather than the fingerprinting actors.
    - Current: `menghentikan sidik jari yang dicurigai`
    - Source: `Enables fingerprinting protection to stop suspected fingerprinters.`
    - Suggest: `menghentikan pengambil sidik jari yang dicurigai`
    - Source refers to fingerprinters (entities), consistent with the category title; the translation drops the actor.
- `etp_suspected_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Suspected Fingerprinters" (suspected fingerprinting actors) is translated as "Sidik Jari yang Dicurigai" (suspected fingerprints).
    - Current: `Sidik Jari yang Dicurigai`
    - Source: `Suspected Fingerprinters`
    - Suggest: `Pengambil Sidik Jari yang Dicurigai`
    - Fingerprinters are the entities performing fingerprinting; the translation names the fingerprints instead.
- `etp_tracking_content_title` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Tracking Content" is translated as "Pelacakan Konten" (content tracking) instead of "Konten Pelacak" (content that tracks).
    - Current: `Pelacakan Konten`
    - Source: `Tracking Content`
    - Suggest: `Konten Pelacak`
    - Head noun is inverted: the category names content containing tracking code, not the tracking of content.
- `history_search_hint` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Search history" (verb + object) is translated as the noun phrase "Riwayat pencarian" (search history/history of searches), reversing the meaning.
    - Current: `Riwayat pencarian`
    - Source: `Search history`
    - Suggest: `Cari riwayat`
    - The developer comment says this is placeholder text in the search bar for searching history, i.e. an imperative "Search history", not the noun "search history".
- `inactive_tabs_delete_all` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Close all inactive tabs" is rendered as "Hapus" (delete) instead of "Tutup" (close), inconsistent with other close-tab strings.
    - Current: `Hapus semua tab nonaktif`
    - Source: `Close all inactive tabs`
    - Suggest: `Tutup semua tab nonaktif`
    - Source says "Close", and elsewhere in the batch "close" is translated as "tutup" (e.g. inactive_tabs_auto_close_message_action).
- `locale_search_hint` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Search language" (verb + object, a search field hint) rendered as the noun phrase "search language".
    - Current: `Bahasa pencarian`
    - Source: `Search language`
    - Suggest: `Cari bahasa`
    - Developer comment says it is placeholder text in a search bar for finding a language; "Bahasa pencarian" means "the language of the search", reversing the meaning.
- `login_detail_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Login" (saved credential) translated as the verb "masuk".
    - Current: `Menu detail masuk`
    - Source: `Login detail menu`
    - Suggest: `Menu detail info masuk`
    - Here "login" is a noun referring to the stored login/password entry, not the action of signing in; "detail masuk" reads as "entry detail/detail of signing in".
- `logins_biometric_prompt_message_pin` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Unlock your device" translated as "Buka perangkat Anda" (open your device), losing "unlock".
    - Current: `Buka perangkat Anda`
    - Source: `Unlock your device`
    - Suggest: `Buka kunci perangkat Anda`
    - The source says unlock; other strings in the same batch correctly use "Buka kunci" for Unlock.
- `microsurvey_prompt_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "It only takes a minute" translated as "beberapa menit" (several minutes).
    - Current: `Hanya butuh beberapa menit`
    - Source: `Help make search in Firefox better. It only takes a minute`
    - Suggest: `Hanya butuh satu menit`
    - The source says it takes only a minute (singular), not several minutes; the translation overstates the time.
- `microsurvey_prompt_sync_title` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "It only takes a minute" translated as "beberapa menit" (several minutes).
    - Current: `Hanya butuh beberapa menit`
    - Source: `Help make sync in Firefox better. It only takes a minute`
    - Suggest: `Hanya butuh satu menit`
    - The source says it only takes a minute, not several minutes.
- `never_translate_site_toolbar_title_preference` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Plural "these sites" rendered as singular "situs ini" without plural marker.
    - Current: `Jangan pernah terjemahkan situs ini`
    - Source: `Never translate these sites`
    - Suggest: `Jangan pernah terjemahkan situs-situs ini`
    - Source title refers to a list of sites ("these sites"); the translation reads identically to the single-site menu item "Jangan terjemahkan situs ini", conflating the two surfaces.
- `nova_onboarding_marketing_body_4` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Meaning lost: "inform the platform you came from that you use Firefox" became "inform the platform where you use Firefox".
    - Current: `menginformasikan platform tempat Anda menggunakan Firefox`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `memberi tahu platform asal Anda bahwa Anda menggunakan Firefox`
    - The source means Mozilla tells the originating platform that the user uses Firefox; the translation drops the "that you use Firefox" clause and changes "platform you came from" into "platform where you use Firefox".
- `nova_onboarding_marketing_body_5` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Meaning lost: "inform the platform you came from that you use Firefox" became "inform the platform where you use Firefox".
    - Current: `menginformasikan platform tempat Anda menggunakan Firefox`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `memberi tahu platform asal Anda bahwa Anda menggunakan Firefox`
    - Same as body_4: the originating-platform meaning and the "that you use Firefox" clause are lost.
- `nova_onboarding_marketing_body_6` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — The translation drops "you came from", changing the meaning to "the platform where you use Firefox".
    - Current: `menginformasikan platform tempat Anda menggunakan Firefox`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `memberi tahu platform asal Anda bahwa Anda menggunakan Firefox`
    - Source says Mozilla informs the platform the user came from that they use Firefox; the target says the platform where you use Firefox, losing both the origin and the "that you use Firefox" clause.
- `nova_onboarding_marketing_body_7` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — The translation drops "you came from", changing the meaning to "the platform where you use Firefox".
    - Current: `menginformasikan platform tempat Anda menggunakan Firefox`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `memberi tahu platform asal Anda bahwa Anda menggunakan Firefox`
    - Source says Mozilla informs the platform the user came from that they use Firefox; the target says the platform where you use Firefox, losing both the origin and the "that you use Firefox" clause.
- `nova_onboarding_marketing_body_line_two` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "proudly independent and dedicated to defending" is rendered as "proudly dedicated and independent in defending", misattributing the adverb and merging the two predicates.
    - Current: `Firefox dengan bangga berdedikasi dan independen dalam membela web terbuka`
    - Source: `Firefox is proudly independent and dedicated to defending the open web against tech monopolies.`
    - Suggest: `Firefox dengan bangga bersifat independen dan berdedikasi untuk membela web terbuka`
    - The source states Firefox is independent (proudly) and dedicated to defending the open web; the target reverses the structure so that independence becomes a manner of defending.
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "won’t sell you out" is translated literally as "tidak akan menjual Anda" (will not sell you).
    - Current: `tidak akan menjual Anda`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `tidak akan mengkhianati Anda`
    - "Sell you out" means betray/give away your data, not literally selling the user; the literal rendering conveys a different meaning.
- `open_all_warning_confirm` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Confirm button label translated as a noun phrase "open tabs" instead of the imperative action "Open tabs".
    - Current: `Tab terbuka`
    - Source: `Open tabs`
    - Suggest: `Buka tab`
    - The developer comment says this is the dialog button for confirming opening all tabs; "Tab terbuka" means "opened tabs" (a state), not the action command.
- `open_tabs_menu` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Open tabs menu" (the menu of open tabs) rendered as the imperative "Buka menu tab".
    - Current: `Buka menu tab`
    - Source: `Open tabs menu`
    - Suggest: `Menu tab terbuka`
    - Per the developer comment this content description names the open-tabs menu; the Indonesian reads as a command to open a "tab menu".
- _…and 35 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_engine_system_auth_no_realm_message` — `mozilla-mobile/android-components/components/browser/engine-system/src/main/res/values-in/strings.xml` — Mid-sentence verb is incorrectly capitalized after the placeholder.
    - Current: `%1$s Meminta nama pengguna dan kata sandi Anda.`
    - Source: `%1$s is requesting your username and password.`
    - Suggest: `%1$s meminta nama pengguna dan kata sandi Anda.`
    - The source has lowercase "is requesting"; the sibling string uses "%2$s meminta" lowercase. Capital M mid-sentence is a spelling/grammar error.
- `mozac_browser_errorpages_corrupted_content_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — Ungrammatical "ada terdeteksi" and missing sentence-final period.
    - Current: `karena ada terdeteksi galat pada pengiriman data`
    - Source: `{ <p> }The page you are trying to view cannot be shown because an error in the data transmission was detected.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } { </ul> }`
    - Suggest: `karena terdeteksi galat pada pengiriman data.`
    - "ada terdeteksi" is not grammatical Indonesian, and the source sentence ends with a period.
- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — Misspelled words "kesaalhan keitk" (should be "kesalahan ketik") and the question is negated relative to the source.
    - Current: `Apa tidak ada kesalahan ejaan, huruf besar, atau { <em> }kesaalhan keitk{ </em> } lainnya pada penulisan alamat?`
    - Source: `{ <ul> } { <li> }Could the item have been renamed, removed, or relocated?{ </li> } { <li> }Is there a spelling, capitalization, or other typographical error in the address?{ </li> } { <li> }Do you have sufficient access…`
    - Suggest: `Apakah ada kesalahan ejaan, huruf besar, atau { <em> }kesalahan ketik{ </em> } lainnya pada penulisan alamat?`
    - The source asks "Is there a ... typographical error in the address?"; the target's spelling of "kesalahan ketik" is garbled and "Apa tidak ada" reverses the question.
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "adminstrator" is misspelled.
    - Current: `adminstrator`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `administrator`
    - Spelling error; the correct Indonesian word is "administrator".
- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — The relative clause "normally used for purposes other than Web browsing" is not linked to the port, producing an ungrammatical sentence.
    - Current: `biasanya digunakan untuk keperluan`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `yang biasanya digunakan untuk keperluan`
    - Without "yang", the clause reads as a separate main clause and the sentence loses its structure relative to the source.
- `mozac_browser_errorpages_security_bad_hsts_cert_techInfo2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — Misspelling: "keaman" should be "keamanan".
    - Current: `kebijakan keaman yang disebut`
    - Source: `{ <label> } { <b> }%1$s{ </b> } has a security policy called HTTP Strict Transport Security (HSTS), which means that { <b> }%2$s{ </b> } can only connect to it securely. You can’t add an exception to visit this site. {…`
    - Suggest: `kebijakan keamanan yang disebut`
    - "keaman" is not a word; the correct Indonesian noun for "security" is "keamanan".
- `mozac_feature_addons_status_softblocked_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — Misspelling of "berisiko" as "berrisiko".
    - Current: `berrisiko`
    - Source: `This extension is restricted and has been disabled. You can enable it, but this may be risky.`
    - Suggest: `berisiko`
    - Indonesian spelling is "berisiko" (ber- + risiko); "berrisiko" is not a valid form.
- `mozac_feature_addons_status_softblocked_re_enabled_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — Misspelling of "berisiko" as "berrisiko".
    - Current: `berrisiko`
    - Source: `This extension is restricted. Using it may be risky.`
    - Suggest: `berisiko`
    - Indonesian spelling is "berisiko"; the doubled r is a typo.
- `mozac_feature_relay_email_masks_cfr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-in/strings.xml` — Word order places the brand placeholder before the noun, producing ungrammatical Indonesian.
    - Current: `Baru! %s topeng surel kini tersedia di perangkat seluler.`
    - Source: `New! %s email masks are now available on mobile.`
    - Suggest: `Baru! Topeng surel %s kini tersedia di perangkat seluler.`
    - %s is the service name "Firefox Relay"; in Indonesian the modifier follows the noun, so "topeng surel %s" is required.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-in/strings.xml` — Awkward/ungrammatical rendering: "menerima mereka" uses the animate pronoun "mereka" for notifications.
    - Current: `Anda akan perlu mengizinkan notifikasi di %1$s untuk menerima mereka dari situs web ini.`
    - Source: `You’ll need to allow notifications in %1$s to receive them from this website.`
    - Suggest: `Anda perlu mengizinkan notifikasi di %1$s untuk menerimanya dari situs web ini.`
    - In Indonesian "mereka" refers to people; the pronoun for inanimate plural objects should be the suffix -nya, so "menerima mereka" is grammatically wrong for "receive them" (notifications).
- `add_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Navigate back" is translated as "Navigasi balik", which is ungrammatical/unidiomatic Indonesian.
    - Current: `Navigasi balik`
    - Source: `Navigate back`
    - Suggest: `Navigasi kembali`
    - "balik" here is colloquial and wrong in register; the standard rendering of "back" in navigation contexts is "kembali".
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Item Menu" left partly untranslated/miscapitalized instead of Indonesian "Menu item".
    - Current: `Item Menu untuk %s`
    - Source: `Item Menu for %s`
    - Suggest: `Menu item untuk %s`
    - The source "Item Menu for %s" means the overflow menu of an item; Indonesian word order requires "Menu item", and mid-sentence capitalization of "Menu" is incorrect.
- `bookmark_moved_single_item` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Awkward/incorrect word order for the snackbar message; the passive verb should follow the moved item's name.
    - Current: `Dipindahkan %1$s ke %2$s`
    - Source: `Moved %1$s to %2$s`
    - Suggest: `%1$s dipindahkan ke %2$s`
    - Source "Moved %1$s to %2$s" states the item %1$s was moved to folder %2$s; Indonesian requires the subject before the passive verb, otherwise the sentence is ungrammatical.
- `browser_menu_default_banner_title` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Jadikan %1$s baku Anda" is ungrammatical/incomplete in Indonesian.
    - Current: `Jadikan %1$s baku Anda`
    - Source: `Make %1$s your default`
    - Suggest: `Jadikan %1$s peramban baku Anda`
    - "Make %1$s your default" needs a noun in Indonesian; "baku Anda" alone is not a valid noun phrase.
- `change_file_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Misspelling of "berisiko".
    - Current: `berrisiko`
    - Source: `This might open the file in a different app and be risky for your device.`
    - Suggest: `berisiko`
    - Indonesian spelling is "berisiko" (ber- + risiko); "berrisiko" is not a valid form.
- `credit_cards_biometric_prompt_message_pin` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Unlock your device" translated as "Buka perangkat Anda" (open your device) instead of "Buka kunci perangkat Anda".
    - Current: `Buka perangkat Anda`
    - Source: `Unlock your device`
    - Suggest: `Buka kunci perangkat Anda`
    - "Unlock" is rendered "Buka kunci" in the neighbouring strings; "Buka" alone means "open" and loses the unlock meaning.
- `etp_cryptominers_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Translation reverses the meaning: it says scripts "that can access" instead of preventing scripts from gaining access, and contains ungrammatical "mengakses ke".
    - Current: `Mencegah skrip berbahaya yang dapat mengakses ke perangkat Anda untuk menambang mata uang digital.`
    - Source: `Prevents malicious scripts gaining access to your device to mine digital currency.`
    - Suggest: `Mencegah skrip berbahaya mengakses perangkat Anda untuk menambang mata uang digital.`
    - Source: "Prevents malicious scripts gaining access to your device" — the prevention applies to the access, not to scripts that already can access; also "mengakses ke" is ungrammatical.
- `likert_scale_option_i_plan_to_keep_using` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Misspelling of "berencana".
    - Current: `berrencana`
    - Source: `I plan to keep using Firefox`
    - Suggest: `berencana`
    - Indonesian spelling is "berencana"; "berrencana" with double r is a typo.
- `preferences_enable_autocomplete_urls` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Autocomplete URLs" is rendered as a noun phrase "URL lengkapi-otomatis" with reversed word order instead of the verb phrase.
    - Current: `URL lengkapi-otomatis`
    - Source: `Autocomplete URLs`
    - Suggest: `Lengkapi otomatis URL`
    - The source is a verb+object ("Autocomplete URLs"); the Indonesian word order makes it an ungrammatical noun phrase.
- `review_prompt_negative_button` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Saya punya masalah" is colloquial/ungrammatical for the app's register; should be "Saya mengalami masalah".
    - Current: `Saya punya masalah`
    - Source: `I’m having issues`
    - Suggest: `Saya mengalami masalah`
    - The source "I’m having issues" refers to experiencing problems with the app; Indonesian idiom uses "mengalami masalah", matching the related string review_prompt_feedback_header which uses "mengalami masalah".
- `search_add_custom_engine_search_string_example` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Typo: "kueir" should be "kueri".
    - Current: `Ganti kueir dengan`
    - Source: `Replace query with “%s”. Example: https://www.google.com/search?q=%s`
    - Suggest: `Ganti kueri dengan`
    - "query" is rendered as "kueir", a misspelling of the Indonesian "kueri".
- `setup_checklist_subtitle_3_steps_completed_state` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Ungrammatical word order "semua 3 langkah".
    - Current: `Anda telah menyelesaikan semua 3 langkah.`
    - Source: `You’ve completed all 3 steps. Enjoy the speed, privacy, and security of %1$s.`
    - Suggest: `Anda telah menyelesaikan ketiga langkah.`
    - In Indonesian, "semua" cannot precede a numeral this way; the natural forms are "ketiga langkah" or "semua langkah".
- `stories_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Navigate back" is rendered as the ungrammatical "Navigasi balik" instead of a proper back-navigation phrase.
    - Current: `Navigasi balik`
    - Source: `Navigate back`
    - Suggest: `Navigasi kembali`
    - The source is an action content description meaning "go back"; Indonesian uses "kembali" for back navigation, "balik" is incorrect/colloquial here.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Duplicated word "menyamar menyamar" and missing preposition in the Indonesian sentence.
    - Current: `Seseorang mungkin berusaha menyamar menyamar laman ini`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `Seseorang mungkin berusaha menyamar sebagai situs ini`
    - Source reads "Someone could be trying to impersonate the site"; the target repeats "menyamar" and lacks the preposition, producing ungrammatical text.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — English plural "URLs" left in Indonesian text where plurality is not marked with -s.
    - Current: `Hapus URLs ubahsuai`
    - Source: `Remove custom URLs`
    - Suggest: `Hapus URL ubahsuai`
    - Indonesian does not form plurals with -s; other strings in the same screen use "URL ubahsuai".
- `preference_autocomplete_user_list_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Missing "agar" makes the sentence read "Enable %s" instead of "Enable to have %s autocomplete...".
    - Current: `Aktifkan %s melengkapi otomatis URL favorit Anda.`
    - Source: `Enable to have %s autocomplete your favorite URLs.`
    - Suggest: `Aktifkan agar %s melengkapi otomatis URL favorit Anda.`
    - The parallel string preference_autocomplete_topsite_summary2 correctly uses "Aktifkan agar %s melengkapi otomatis..."; without "agar" the clause is ungrammatical.

### D. Terminology, register & consistency

- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — "proxy" is left untranslated here while the sibling strings use "proksi".
    - Current: `server proxy tidak bisa ditemukan`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `server proksi tidak bisa ditemukan`
    - The same term is rendered "proksi" in mozac_browser_errorpages_proxy_connection_refused_message and in the title of this very error page ("Server Proksi Tidak Ditemukan"), creating an inconsistency on the same surface.
- `mozac_feature_addons_permissions_data_collection_authenticationInfo_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — "otentikasi" is inconsistent with "autentikasi" used in the corresponding long description and is the non-standard spelling.
    - Current: `informasi otentikasi`
    - Source: `authentication information`
    - Suggest: `informasi autentikasi`
    - The long description for the same permission uses "informasi autentikasi"; KBBI standard form is "autentikasi".
- `mozac_feature_addons_permissions_pkcs11_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — Uses "otentikasi kriptografis" while the sibling string uses "autentikasi kriptografi" for the same source text.
    - Current: `Menyediakan layanan otentikasi kriptografis.`
    - Source: `Provide cryptographic authentication services.`
    - Suggest: `Menyediakan layanan autentikasi kriptografi.`
    - Same source phrase "Provide cryptographic authentication services" is rendered inconsistently; "autentikasi" is the standard KBBI form used in mozac_feature_addons_permissions_pkcs11_description.
- `mozac_feature_addons_successfully_installed` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-in/strings.xml` — "installed" translated as "menginstal" instead of the standard "memasang" used elsewhere (e.g. "dipasang").
    - Current: `Berhasil menginstal %1$s`
    - Source: `Successfully installed %1$s`
    - Suggest: `Berhasil memasang %1$s`
    - The same file uses "dipasang" for install (mozac_feature_addons_soft_blocked_2), so "menginstal" is inconsistent terminology.
- `mozac_feature_downloads_paused_notification_text` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-in/strings.xml` — "Download paused" rendered as "Unduhan ditunda" (postponed) instead of "dijeda" (paused).
    - Current: `Unduhan ditunda`
    - Source: `Download paused`
    - Suggest: `Unduhan dijeda`
    - "Pause" is translated as "Jeda" elsewhere (mozac_feature_media_notification_action_pause); "ditunda" means postponed/delayed, not paused.
- `mozac_lib_crash_no_crashes` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-in/strings.xml` — "crash reports" rendered as "laporan kerusakan" while all other strings in the same file use "laporan mogok".
    - Current: `Tidak ada laporan kerusakan yang pernah dikirim.`
    - Source: `No crash reports have been submitted.`
    - Suggest: `Tidak ada laporan mogok yang pernah dikirim.`
    - Same source term "crash report" is translated "laporan mogok" in mozac_lib_crash_dialog_checkbox and mozac_lib_send_crash_report_in_progress in the same surface; "kerusakan" is inconsistent.
- `browser_menu_read` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Reader view" is rendered as "Tampilan baca" while the related strings use "Tampilan Pembaca"/"tampilan pembaca".
    - Current: `Tampilan baca`
    - Source: `Reader view`
    - Suggest: `Tampilan pembaca`
    - browser_menu_customize_reader_view_2 and browser_menu_read_close translate "Reader view" as "Tampilan Pembaca"/"tampilan pembaca"; the same term on the same menu surface should be consistent.
- `credit_cards_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Navigate back" is rendered as "Navigasi balik" here but "Navigasi mundur" in the equivalent debug drawer string, and "balik" is colloquial.
    - Current: `Navigasi balik`
    - Source: `Navigate back`
    - Suggest: `Navigasi mundur`
    - Same source string "Navigate back" for the same kind of back button; debug_drawer_back_button_content_description uses "Navigasi mundur". "balik" is informal/ambiguous (also means "flip").
- `delete_history_prompt_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "devices" is rendered as "perangkat" while the batch elsewhere uses "peranti".
    - Current: `riwayat yang disinkronkan dari perangkat lain`
    - Source: `Removes history (including history synced from other devices)`
    - Suggest: `riwayat yang disinkronkan dari peranti lain`
    - default_locale_text translates "device" as "peranti"; the same term should be consistent on the same surface.
- `edit_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Navigate back" rendered as "Navigasi balik", inconsistent with "Arahkan kembali" used for the same source string elsewhere.
    - Current: `Navigasi balik`
    - Source: `Navigate back`
    - Suggest: `Arahkan kembali`
    - Same source string "Navigate back" is translated "Arahkan kembali" in etp_back_button_content_description; "Navigasi balik" is also unnatural Indonesian.
- `ip_protection_get_started` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Button label "Get started" translated as the gerund/progressive "Memulai" instead of an imperative button label.
    - Current: `Memulai`
    - Source: `Get started`
    - Suggest: `Mulai`
    - The developer comment says this is a button label that starts a flow; Indonesian button labels use the imperative "Mulai", as with other imperative labels in this batch (Buka, Unduh, Cetak).
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Navigate back" rendered as "Navigasi balik", which is not the standard Indonesian wording for a back navigation control.
    - Current: `Navigasi balik`
    - Source: `Navigate back`
    - Suggest: `Navigasi kembali`
    - "balik" means flip/turn over in this register; the established term for going back is "kembali". Screen readers will announce an odd phrase.
- `ip_protection_toolbar_pill_label` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "VPN on" rendered with "hidup" while the parallel badge strings use "Nyala"/"Mati", creating inconsistent terminology on the same surface.
    - Current: `VPN hidup`
    - Source: `VPN on`
    - Suggest: `VPN nyala`
    - preferences_ip_protection_on translates "On" as "Nyala" and the paired label ip_protection_toolbar_pill_label_off uses "mati"; "hidup" is inconsistent for the same on/off state term.
- `login_details_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Navigate back" rendered as "Navigasi balik", an unidiomatic term inconsistent with "Kembali" used elsewhere.
    - Current: `Navigasi balik`
    - Source: `Navigate back`
    - Suggest: `Navigasi kembali`
    - The standard Indonesian rendering of "back" navigation is "kembali"; "balik" is colloquial and inconsistent with logins_navigate_back_button_content_description.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — `never_translate_site_header_preference` quotes “Jangan terjemahkan situs ini” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Jangan pernah terjemahkan situs ini”
    - Current: `Untuk menambahkan situs baru: Kunjungi dan pilih “Jangan terjemahkan situs ini” dari menu terjemahan.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Jangan pernah terjemahkan situs ini`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `notification_pbm_delete_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "private tabs" rendered "tab privat" while the sibling notification strings use "tab pribadi".
    - Current: `Tutup tab privat`
    - Source: `Close private tabs`
    - Suggest: `Tutup tab pribadi`
    - notification_erase_text_android_14 and notification_erase_title_android_14 use "tab pribadi" for the same term on the same surface; inconsistent terminology.
- `nova_onboarding_toolbar_selection_bottom_label` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Bottom" for toolbar position is translated as "Dasar" (basic/base) instead of "Bawah".
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The option refers to placing the address bar at the bottom of the screen; Indonesian uses "Bawah". "Dasar" reads as "basic/foundation" and conflicts with "baku" usage elsewhere.
- `nova_onboarding_toolbar_selection_top_label` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Top" for toolbar position is translated as "Puncak" (summit/peak) instead of "Atas".
    - Current: `Puncak`
    - Source: `Top`
    - Suggest: `Atas`
    - The option refers to placing the address bar at the top of the screen; Indonesian UI uses "Atas". "Puncak" means peak/summit and is wrong here.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "font" left untranslated here while the related titles use "fon", creating inconsistent terminology on the same settings screen.
    - Current: `Ukuran font akan sesuai dengan pengaturan Android Anda. Nonaktifkan untuk mengelola ukuran font di sini.`
    - Source: `Font size will match your Android settings. Disable to manage font size here.`
    - Suggest: `Ukuran fon akan sesuai dengan pengaturan Android Anda. Nonaktifkan untuk mengelola ukuran fon di sini.`
    - preference_accessibility_auto_size_2 and preference_accessibility_font_size_title use "fon"; the summary directly beneath uses "font".
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "default" is rendered "bawaan" here while the parallel string preference_doh_off_summary uses "baku" for the same phrase.
    - Current: `Gunakan resolver DNS bawaan Anda jika ada masalah dengan penyedia DNS aman`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `Gunakan resolver DNS baku Anda jika ada masalah dengan penyedia DNS aman`
    - Same source term "your default DNS resolver" is translated inconsistently on the same DNS-over-HTTPS settings surface ("baku" in preference_doh_off_summary, "Perlindungan Baku" in preference_doh_default_protection).
- `preference_doh_increased_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "default DNS resolver" uses "bawaan" whereas the same phrase elsewhere in the DoH settings uses "baku".
    - Current: `Hanya gunakan resolver DNS bawaan Anda jika ada masalah dengan DNS aman`
    - Source: `Only use your default DNS resolver if there is a problem with secure DNS`
    - Suggest: `Hanya gunakan resolver DNS baku Anda jika ada masalah dengan DNS aman`
    - Inconsistent rendering of "default" on the same surface; preference_doh_off_summary uses "baku".
- `preference_enhanced_tracking_protection_custom` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Custom" is rendered "Ubahsuai" here but "ubahan" in preference_doh_provider_custom_dialog_title on the same settings surface.
    - Current: `Ubahsuai`
    - Source: `Custom`
    - Suggest: `Ubahan`
    - The same source term "Custom" is inconsistently translated across adjacent settings strings.
- `preferences_category_engines_in_search_menu` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Engines" (search engines) is rendered as "Mesin peramban" (browser engines) instead of "Mesin pencari".
    - Current: `Mesin peramban terlihat di menu pencarian`
    - Source: `Engines visible on the search menu`
    - Suggest: `Mesin pencari yang terlihat di menu pencarian`
    - The preference category concerns search engines shown in the search menu; elsewhere in the same file "search engine" is translated "mesin pencari" (see preferences_category_select_private_search_engine). "Mesin peramban" means browser engine.
- `preferences_passwords_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Exceptions" is rendered "Kekecualian" here but "pengecualian" in the related remove-all string on the same screen.
    - Current: `Kekecualian`
    - Source: `Exceptions`
    - Suggest: `Pengecualian`
    - Terminology inconsistency on the same surface: preferences_passwords_exceptions_remove_all uses "pengecualian", the standard form.
- `preferences_passwords_save_logins_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Passwords" rendered "kata sandi" while the adjacent strings use "sandi".
    - Current: `Simpan kata sandi`
    - Source: `Save passwords`
    - Suggest: `Simpan sandi`
    - preferences_passwords_logins_and_passwords_2, preferences_logins_add_login_2 and the exceptions descriptions all use "sandi" for password; this string is inconsistent on the same settings surface.
- `saved_logins_add_new_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "login" rendered as "log masuk", inconsistent with "info masuk" used elsewhere for the same term.
    - Current: `Tambahkan log masuk baru`
    - Source: `Add new login`
    - Suggest: `Tambahkan info masuk baru`
    - saved_login_duplicate translates "login" as "info masuk"; the same noun on the same surface should be consistent.
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "passwords" rendered as "kata sandi" while neighbouring strings use "sandi".
    - Current: `Menu urutkan kata sandi`
    - Source: `Sort passwords menu`
    - Suggest: `Menu urutkan sandi`
    - saved_login_hide_password, saved_logins_copy_password etc. use "sandi" for "password"; the same term should be consistent on the logins surface.
- `settings_search_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Settings" is rendered "pengaturan" here while the rest of the batch consistently uses "Setelan".
    - Current: `Tombol pencarian pengaturan`
    - Source: `Settings search button`
    - Suggest: `Tombol pencarian setelan`
    - settings, settings_title and search_settings_menu_item all use "Setelan"; using "pengaturan" for the same term on the same surface is inconsistent.
- `sync_add_new_device_message` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Device" is translated as "Perangkat" here while the surrounding sync strings consistently use "peranti".
    - Current: `Tidak Ada Perangkat Terhubung`
    - Source: `No Devices Connected`
    - Suggest: `Tidak Ada Peranti Terhubung`
    - Neighbouring strings (sync_add_new_device_title, sync_connect_device, sync_send_to_all) all render "device" as "peranti"; this one is inconsistent on the same surface.
- `terms_of_use_prompt_title_option_a` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Terms of Use" is rendered as "Syarat Penggunaan" here but as "Ketentuan Penggunaan" in the related link string on the same prompt.
    - Current: `Syarat Penggunaan`
    - Source: `Terms of Use`
    - Suggest: `Ketentuan Penggunaan`
    - terms_of_use_prompt_link_terms_of_use translates the same source term "Terms of Use" as "Ketentuan Penggunaan"; both appear in the same terms-of-use prompt surface, so the term must be consistent.
- `translation_option_bottom_sheet_switch_never_translate_site_description` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "settings" translated as "pengaturan" while the parallel error string uses "setelan" for the same term on the same surface.
    - Current: `Menimpa semua pengaturan lainnya`
    - Source: `Overrides all other settings`
    - Suggest: `Menimpa semua setelan lainnya`
    - Terminology inconsistency for "settings" within the same translation options sheet (cf. translation_option_bottom_sheet_error_warning_text "Beberapa setelan").
- `webcompat_reporter_preview_bottom_sheet_header` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — "Preview" is translated as "Pratinjauan" here but as "Pratinjau" in the sibling string webcompat_reporter_preview_report.
    - Current: `Pratinjauan Laporan`
    - Source: `Report Preview`
    - Suggest: `Pratinjau Laporan`
    - Same term "Preview Report"/"Report Preview" on the same surface must use one form; the standard Firefox term is "Pratinjau".
- `analytics` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Tracker category "Analytics" rendered with the adjective "Analitis" instead of the noun "Analitik".
    - Current: `Analitis`
    - Source: `Analytics`
    - Suggest: `Analitik`
    - The string is a tracker category name (a noun, parallel to "Periklanan", "Konten"); "analitis" is the adjective "analytical".
- `cfr_for_toolbar_shield_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Informal second-person "memata-mataimu" breaks the formal "Anda" address used elsewhere in the app.
    - Current: `memata-mataimu`
    - Source: `Got ‘em! We stopped this site from spying on you. Tap the shield any time to see what we’re blocking.`
    - Suggest: `memata-matai Anda`
    - Other Focus strings (e.g. cfr_for_start_browsing, biometric_prompt_subtitle) consistently use the formal "Anda"; the -mu clitic is an informal register violation.
- `preference_category_search` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Category heading "Search" translated as the verb "Cari" instead of the noun "Pencarian".
    - Current: `Cari`
    - Source: `Search`
    - Suggest: `Pencarian`
    - This is a preference category title (a noun), so the noun form "Pencarian" is required rather than the imperative verb "Cari".

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_connection_failure_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-in/strings.xml` — Stray space before the period after "sibuk".
    - Current: `terlalu sibuk . Cobalah`
    - Source: `{ <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If you are unable to load any pages, check your device’s data or Wi-Fi connection.{ </li> } { </ul> }`
    - Suggest: `terlalu sibuk. Cobalah`
    - The source has no space before the full stop; this is a spacing/punctuation error.
- `browser_menu_open_app_link` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Unnecessary capitalization of "Aplikasi" mid-sentence, inconsistent with other menu labels using sentence case.
    - Current: `Buka di Aplikasi`
    - Source: `Open in app`
    - Suggest: `Buka di aplikasi`
    - Source is "Open in app" (sentence case); other menu items in this batch use lowercase for common nouns (e.g. "Buka di %1$s", "Simpan ke koleksi").
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Straight quotes used where the source has curly quotes and the locale convention is curly double quotes.
    - Current: `"Keluar"`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“Keluar”`
    - Source uses “Quit” with curly quotes; the id tree's detected convention is curly-double.
- `top_sites_max_limit_confirmation_button` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — Added exclamation mark not present in the source button label.
    - Current: `Oke, Paham!`
    - Source: `OK, Got It`
    - Suggest: `Oke, Paham`
    - The source "OK, Got It" has no exclamation mark; punctuation should mirror the source.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/id/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (1)

- `preferences_delete_browsing_data_cookies_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-in/strings.xml` — fixed 2026-08-24
