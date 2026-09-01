# Android l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f39118d70d88` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f39118d70d88` |
| **Previous run** | 2026-08-24 @ `e8622a909368` |
| **Mode** | incremental |
| **Strings reviewed this run** | 19 of 2,735 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for tr: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (3)

- `recent_tabs_header_2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Continue" (continue browsing where you left off) rendered as "İleri" (Forward/Next).
    - Current: `İleri`
    - Source: `Continue`
    - Suggest: `Devam edin`
    - The header invites the user to continue browsing the most recent tab; "İleri" means "forward/next" and is the standard label for the forward navigation button, not "continue".
- `customize_toggle_continue` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Homescreen section title "Continue" translated as "İleri" (Forward/Next).
    - Current: `İleri`
    - Source: `Continue`
    - Suggest: `Devam edin`
    - Per the developer comment this names the section that lets users continue where they left off; "İleri" means "forward/next" and does not convey "continue".
- `pdf_tools_signature_placeholder` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative "yaz" breaks the locale's formal register.
    - Current: `İmzanızı yaz`
    - Source: `Type signature`
    - Suggest: `İmzanızı yazın`
    - The tr locale convention is formal address; other imperatives in this batch use the formal form. "yaz" is the informal singular imperative.

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (18)

- `sports_widget_confederation_concacaf` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The abbreviation CONCACAF is misspelled as "CONCCAF".
    - Current: `CONCCAF`
    - Suggest: `CONCACAF`
    - The developer comment states CONCACAF is the abbreviation for "Confederation of North, Central America and Caribbean Association Football"; the target drops a letter.
- `sports_widget_countdown_minutes` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The minutes abbreviation is rendered "D", which in Turkish reads as "dakika" but collides with the days label "G"… actually it conflicts with no other, yet "D" is not the standard Turkish abbreviation for minute.
    - Current: `D`
    - Suggest: `dk`
    - Turkish abbreviates minute as "dk"; a bare "D" is ambiguous (commonly read as "dakika" only in this context) and the 2-character limit allows "dk".
- `sports_widget_get_custom_wallpaper` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Get custom wallpaper" is translated as "download" rather than "get", and "custom" is rendered as "kişisel" (personal).
    - Current: `Kişisel duvar kâğıdını indir`
    - Suggest: `Özel duvar kâğıdını al`
    - The source says "Get custom wallpaper"; the target says "Download the personal wallpaper", changing the action and definiteness.
- `sports_widget_halftime` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Halftime" (the break between halves) is translated as "İlk yarı" (first half).
    - Current: `İlk yarı`
    - Suggest: `Devre arası`
    - The developer comment says the status is shown during halftime; "İlk yarı" means "first half", a different match phase, and conflicts with sports_widget_second_half ("İkinci yarı").
- `sports_widget_match_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "versus" is replaced by a dash, which a screen reader will not announce meaningfully.
    - Current: `%1$s - %2$s, %3$s`
    - Suggest: `%1$s - %2$s karşılaşması, %3$s`
    - This is a content description read aloud; the source word "versus" conveys the matchup and is lost as a silent hyphen.
- `sports_widget_page_position_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The "of" relation in "page %2$d of %3$d" is dropped, producing "sayfa 2 5".
    - Current: `%1$s, sayfa %2$d %3$d`
    - Suggest: `%1$s, sayfa %2$d / %3$d`
    - Source states page X of Y; the target juxtaposes two numbers with no connecting word, which is unintelligible when read aloud.
- `accessibility_dismiss_find_in_page` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Dismiss find in page" is translated as "Sayfa bulmayı kapat" (close finding the page) instead of referring to the "find in page" feature.
    - Current: `Sayfa bulmayı kapat`
    - Suggest: `Sayfada bul özelliğini kapat`
    - The source refers to dismissing the "find in page" UI; "Sayfa bulmayı" means "finding a page", which names the wrong feature.
- `accessibility_find_in_page_result` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — The result counter reads awkwardly and repeats "sonuç"; Turkish convention is "%1$d / %2$d" or "%2$d sonuçtan %1$d.".
    - Current: `%2$d sonuçtan %1$d sonuç`
    - Suggest: `%2$d sonuçtan %1$d. sonuç`
    - "%1$d out of %2$d" indicates the current position, not a count; "%2$d sonuçtan %1$d sonuç" states a quantity of results rather than the position the user is at.
- `cookie_banner_report_a_site_snackbar_label` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Request to support site submitted" is mistranslated as sending a request to a "support site".
    - Current: `Destek sitesine istek gönderildi.`
    - Suggest: `Bu siteyi destekleme isteği gönderildi.`
    - The source means a request was submitted asking that the site be supported by the cookie banner reducer; the Turkish says the request was sent to a support site.
- `cookie_banner_the_site_was_reported` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Request to support site submitted" is mistranslated as sending a request to a "support site".
    - Current: `Destek sitesine istek gönderildi.`
    - Suggest: `Bu siteyi destekleme isteği gönderildi.`
    - Per the developer comment this appears after the user reports a site where the cookie banner reducer failed; it means a request for the site to be supported was submitted, not that a request was sent to a support site.
- `external_app_prompt` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_app_prompt` uses a straight apostrophe
    - Current: `Bu bağlantıyı %2$s ile açmak için %1$s'tan çıkabilirsiniz.`
    - Suggest: `%1$s’tan çıkabilirsiniz.`
    - The tree uses ’ 160 times against 4 straight.
- `external_app_prompt_no_app` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_app_prompt_no_app` uses a straight apostrophe
    - Current: `Cihazınızdaki uygulamalar bu bağlantıyı açamıyor. %2$s mağazasında uygun bir uygulama aramak için %1$s'tan çıkabilirsiniz.`
    - Suggest: `%1$s’tan çıkabilirsiniz.`
    - The tree uses ’ 160 times against 4 straight.
- `external_multiple_apps_matched_exit` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `external_multiple_apps_matched_exit` uses a straight apostrophe
    - Current: `Gizli Gezinti'den çıkılsın mı?`
    - Suggest: `Gizli Gezinti’den çıkılsın mı?`
    - The tree uses ’ 160 times against 4 straight.
- `firstrun_defaultbrowser_text2` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Take private browsing to the next level" (user action/benefit) rendered as "We improved private browsing even further".
    - Current: `Gizli gezintiyi daha da geliştirdik.`
    - Suggest: `Gizli gezintiyi bir üst seviyeye taşıyın.`
    - The source addresses the user; the Turkish turns it into a first-person statement about the developers, changing the meaning.
- `firstrun_shortcut_text` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — `firstrun_shortcut_text` uses straight double quotes
    - Current: `%1$s’ta sevdiğiniz sitelere çabucak ulaşabilirsiniz. %1$s menüsünden "Ana ekrana ekle"yi seçmeniz yeterli.`
    - Suggest: `“Ana ekrana ekle”`
    - The locale's quote convention is `curly-double` (14 occurrences).
- `menu_trackers_blocked_title` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Label "Trackers blocked" rendered as the imperative "Block trackers".
    - Current: `Takip kodlarını engelle`
    - Suggest: `Engellenen takip kodları`
    - Per the developer comment this is a label above a count of blocked trackers, not a command; the Turkish imperative changes the meaning.
- `preference_open_new_tab` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Mistranslation: source means switching to the new tab immediately when a link opens in it, not "go to the link in the new tab".
    - Current: `Hemen yeni sekmedeki bağlantıya geç`
    - Suggest: `Bağlantı yeni sekmede açıldığında hemen o sekmeye geç`
    - "Switch to link in new tab immediately" describes automatically switching to the newly opened tab; the Turkish reads as "immediately go to the link in the new tab", altering the meaning of the preference.
- `tip_disable_tips2` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Stray zero-width/invisible character between "Başlangıç" and "ekranında".
    - Current: `Başlangıç ​​ekranında`
    - Suggest: `Başlangıç ekranında`
    - The string contains invisible zero-width space characters that do not belong in the text.

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 43 |
| Strings | 2,735 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 3 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 14, `straight-double` 2 | **curly-double** |
| apostrophe | `typographic` 151, `straight` 1 | **typographic** |
| ellipsis | `char` 21 | **char** |
| register | `informal` 2, `formal` 18 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (140)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 77 |
| 3 | Degraded language (grammar, spelling, terminology) | 57 |
| 4 | Cosmetic (typography, spacing) | 6 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — "düğmesine tıklayın" (click) is wrong for a touch UI; source says "Press".
    - Current: `“Yeniden dene” düğmesine tıklayın`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `“Yeniden dene” düğmesine basın`
    - Source is "Press “Try Again”"; on Android the action is tapping/pressing, not clicking.
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — The second half of the first bullet ("Check the site for extra requirements.") is omitted.
    - Current: `Çoklu ortam barındıran veya metin içermeyen bir hizmete bağlanmak istiyor olabilirsiniz.`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `Çoklu ortam barındıran veya metin içermeyen bir hizmete bağlanmak istiyor olabilirsiniz. Sitede ek gereksinimler olup olmadığını kontrol edin.`
    - Source bullet contains two sentences; the instruction to check the site for extra requirements is missing from the translation.
- `mozac_browser_errorpages_unsafe_content_type_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — The imperative request "Please contact the website owners" is rendered as a tentative suggestion ("you might consider notifying them").
    - Current: `Site sahipleriyle iletişim kurarak bu sorunu onlara bildirmeyi düşünebilirsiniz.`
    - Source: `{ <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } { </ul> }`
    - Suggest: `Lütfen bu sorunu bildirmek için site sahipleriyle iletişime geçin.`
    - Source is a direct request ("Please contact the website owners to inform them of this problem."); the Turkish weakens it to "you may consider notifying them", changing the meaning.
- `mozac_browser_awesomebar_remove_suggestion` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-tr/strings.xml` — "Remove suggestion" (remove from displayed results) is translated as "delete suggestion".
    - Current: `Öneriyi sil`
    - Source: `Remove suggestion`
    - Suggest: `Öneriyi kaldır`
    - The developer comment says the button removes the suggestion from the displayed results; "sil" (delete) implies permanent deletion, whereas "kaldır" matches "remove".
- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-tr/strings.xml` — "requests additional data collection" is rendered as the add-on itself wanting to collect data, changing the meaning of the permission request.
    - Current: `%1$s ek veriler toplamak istiyor`
    - Source: `%1$s requests additional data collection`
    - Suggest: `%1$s ek veri toplama izni istiyor`
    - The source asks the user to grant additional data collection permission; the Turkish drops the permission/request notion and also uses an ungrammatical plural object ("ek veriler toplamak" instead of "ek veri toplamak"), parallel to the sibling title string which uses "ek ayarlar istiyor".
- `mozac_feature_applinks_open_in` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-tr/strings.xml` — "Open in…" is translated as "Birlikte aç…" (Open with…), changing the meaning.
    - Current: `Birlikte aç…`
    - Source: `Open in…`
    - Suggest: `Şununla aç…`
    - The source is the title for a list of external apps to open the link in; "Birlikte aç" is a fragment meaning "open together/with" and does not convey "Open in…" correctly on its own.
- `mozac_feature_autofill_confirmation_authenticity` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-tr/strings.xml` — "authenticity" is rendered as "yetkinlik" (competence) instead of "gerçeklik/özgünlük" (authenticity).
    - Current: `uygulamanın yetkinliğini doğrulayamadı`
    - Source: `%1$s could not verify the authenticity of the application. Do you want to proceed with autofilling the selected credentials?`
    - Suggest: `uygulamanın gerçekliğini doğrulayamadı`
    - The source says the app's authenticity could not be verified; "yetkinlik" means competence/proficiency, which is a different concept. Turkish for authenticity here is "gerçeklik" or "özgünlük".
- `mozac_feature_findindpage_dismiss` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-tr/strings.xml` — "Dismiss find in page" is rendered as "close finding a page" instead of closing the find-in-page UI.
    - Current: `Sayfa bulmayı kapat`
    - Source: `Dismiss find in page`
    - Suggest: `Sayfada bul özelliğini kapat`
    - The source refers to dismissing the "find in page" feature, which is translated elsewhere in this file as "Sayfada bul"; "Sayfa bulmayı" means "finding a page".
- `mozac_feature_passwords_importer_dialog_description` — `mozilla-mobile/android-components/components/feature/password-importer/src/main/res/values-tr/strings.xml` — "It should only take a few seconds" is translated as a definite statement, dropping the hedge "should only".
    - Current: `İşlem birkaç saniye sürecek.`
    - Source: `Keep this screen open. It should only take a few seconds.`
    - Suggest: `İşlem yalnızca birkaç saniye sürmeli.`
    - The source expresses an estimate ("should only take"), not a certainty.
- `mozac_feature_prompts_identity_credentials_continue` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-tr/strings.xml` — "Continue" translated as "İleri" (Next) instead of "Devam".
    - Current: `İleri`
    - Source: `Continue`
    - Suggest: `Devam`
    - The source is the positive button "Continue"; "İleri" means "Next/Forward", a different action label.
- `mozac_feature_prompts_set_date` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-tr/strings.xml` — "Set" (button action) rendered as past participle "Ayarlandı" ("Set/Done" state) instead of an imperative.
    - Current: `Ayarlandı`
    - Source: `Set`
    - Suggest: `Ayarla`
    - The developer comment says this is the positive button label for selecting a date; it must be an action verb, not a statement that something was set.
- `mozac_feature_relay_email_masks_cfr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-tr/strings.xml` — The Turkish adds a literal "Relay" after the %s placeholder, which already holds the full service name "Firefox Relay", producing "Firefox Relay Relay".
    - Current: `Yeni! %s Relay e-posta maskelerini`
    - Source: `New! %s email masks are now available on mobile.`
    - Suggest: `Yeni! %s e-posta maskelerini`
    - The developer comment states %s is the name of the service, "Firefox Relay"; repeating "Relay" duplicates the brand name.
- `mozac_feature_sitepermissions_storage_access_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-tr/strings.xml` — "if it's not clear why" is rendered as "if you don't know why", changing the meaning.
    - Current: `bilmiyorsanız`
    - Source: `You may want to block access if it’s not clear why %s needs this data.`
    - Suggest: `belli değilse`
    - The source says the user may block access if it is not clear why the site needs the data; the Turkish shifts this to the user's own lack of knowledge.
- `mozac_summarize_download_nano_consent_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-tr/strings.xml` — "summaries that stay in your control" is mistranslated as "summaries that never leave your device".
    - Current: `cihazınızdan asla dışarı çıkmayan sayfa özetleri`
    - Source: `A one-time download lets %s create page summaries that stay in your control.`
    - Suggest: `denetiminizde kalan sayfa özetleri`
    - The source claims control over the summaries, not that they never leave the device; this adds a technical claim not in the en-US text.
- `mozac_summarize_shake_consent_off_device_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-tr/strings.xml` — The Turkish reverses the sentence structure so the app "creates" the summary in seconds instead of the user "getting" a summary from the app.
    - Current: `Cihazınızı sallayın, sayfanın özetini %1$s saniyeler içinde oluştursun.`
    - Source: `Shake your device, get a page summary from %1$s in seconds.`
    - Suggest: `Cihazınızı sallayın, saniyeler içinde %1$s tarayıcısından sayfa özeti alın.`
    - Source: "Shake your device, get a page summary from %1$s in seconds." — the imperative addressed to the user is "get a page summary"; the translation turns it into a wish that the app produce it.
- `mozac_lib_crash_background_process_notification_title` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-tr/strings.xml` — The apology "Sorry." from the source is dropped in the Turkish translation.
    - Current: `%1$s uygulamasında bir sorun oluştu.`
    - Source: `Sorry. A problem occurred in %1$s.`
    - Suggest: `Üzgünüz. %1$s uygulamasında bir sorun oluştu.`
    - Source is "Sorry. A problem occurred in %1$s."; the first sentence is missing from the target.
- `mozac_lib_gathering_crash_telemetry_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-tr/strings.xml` — "Gathering crash telemetry data" is translated identically to the plain crash-data string, dropping "telemetry".
    - Current: `Çökme verileri toplanıyor`
    - Source: `Gathering crash telemetry data`
    - Suggest: `Çökme telemetri verileri toplanıyor`
    - The source distinguishes telemetry data from crash data; the Turkish text is identical to mozac_lib_gathering_crash_data_in_progress and omits "telemetry".
- `add_login_hostname_invalid_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "hostname" rendered as "sunucu" (server) instead of host/hostname.
    - Current: `Geçerli bir sunucu gerekli`
    - Source: `Valid hostname required`
    - Suggest: `Geçerli bir sunucu adı gerekli`
    - The source refers to a hostname field; "sunucu" means server, dropping the "name" part of hostname.
- `addresses_district` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "District" is translated as "İl" (province), which is the wrong administrative level and duplicates the translation used for "Province".
    - Current: `İl`
    - Source: `District`
    - Suggest: `İlçe`
    - The source "District" denotes a sub-locality/secondary level below the country level; "İl" means province/state in Turkish and is already used for addresses_province, so the district field wrongly names a higher-level unit.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Afterwards, you can unblock anything you want to keep using" is rendered without the "afterwards" and as an ability statement, dropping part of the source meaning.
    - Current: `Kullanmaya devam etmek istediğiniz özelliklerin engelini kaldırabilirsiniz.`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `Daha sonra, kullanmaya devam etmek istediğiniz özelliklerin engelini kaldırabilirsiniz.`
    - The source says "Afterwards, you can unblock anything you want to keep using."; the temporal qualifier is dropped.
- `ai_controls_voice_search_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The service name "Google Speech Services" is rendered in the singular as "Google Speech Service".
    - Current: `Google Speech Service`
    - Source: `Audio is converted to text by Google Speech Services.`
    - Suggest: `Google Speech Services`
    - Product/service name must match the source brand name "Google Speech Services".
- `alternative_app_icon_option_gradient_twilight` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Twilight" (evening dusk) is translated as "Şafak", which means dawn/daybreak.
    - Current: `Şafak`
    - Source: `Twilight`
    - Suggest: `Alacakaranlık`
    - The developer comment describes the purple sky color during twilight (evening dusk); Turkish "Şafak" means dawn/sunrise, the opposite time of day. "Alacakaranlık" is the standard term for twilight.
- `bookmark_error_edit_bookmark` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Past-tense failure message rendered as present/ongoing "cannot be edited" instead of "could not be edited".
    - Current: `Yer imi düzenlenemiyor`
    - Source: `Could not edit bookmark`
    - Suggest: `Yer imi düzenlenemedi`
    - Source "Could not edit bookmark" reports a completed failure; parallel snackbars use the -emedi form ("Klasör eklenemedi", "Üst klasör değiştirilemedi").
- `bookmark_error_edit_folder` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Past-tense failure message rendered as present tense "cannot be edited".
    - Current: `Klasör düzenlenemiyor`
    - Source: `Could not edit folder`
    - Suggest: `Klasör düzenlenemedi`
    - Source "Could not edit folder" is a completed failure; inconsistent with "Klasör eklenemedi" and "Üst klasör değiştirilemedi" in the same snackbar set.
- `bookmark_sort_menu_newest` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Sort by newest" translated without the verb, unlike the sibling sort options.
    - Current: `Yeniden eskiye`
    - Source: `Sort by newest`
    - Suggest: `En yeniye göre sırala`
    - Source is "Sort by newest"; the other menu items are rendered as "... sırala", while this one drops the sorting verb and states a range "newest to oldest".
- `bookmark_sort_menu_oldest` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Sort by oldest" is rendered without the verb, unlike the parallel sort menu items.
    - Current: `Eskiden yeniye`
    - Source: `Sort by oldest`
    - Suggest: `Eskiden yeniye sırala`
    - The source is an action label "Sort by oldest"; the sibling string bookmark_sort_menu_z_to_a is translated as "Z’den A’ya sırala", so the missing "sırala" makes this inconsistent and drops the action.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Close custom tab menu sheet" loses the "sheet" element in the content description.
    - Current: `Özel sekme menüsünü kapat`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Özel sekme menüsü sayfasını kapat`
    - The source describes closing the bottom-sheet of the custom tab menu; the translation drops "sheet", which the screen reader description needs to identify the control.
- `browser_menu_recommended_extensions_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "More info" is rendered as an imperative "Get more info" instead of a noun phrase.
    - Current: `Daha fazla bilgi al`
    - Source: `More info`
    - Suggest: `Daha fazla bilgi`
    - The source is a noun phrase label/content description "More info"; "Daha fazla bilgi al" adds the verb "al" (get), changing it into a command.
- `browser_menu_try_a_recommended_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Singular "a recommended extension" is translated as plural "önerilen uzantıları".
    - Current: `Önerilen uzantıları deneyin`
    - Source: `Try a recommended extension`
    - Suggest: `Önerilen bir uzantıyı deneyin`
    - Source says "Try a recommended extension" (singular); the Turkish uses the plural definite object.
- `certificate_warning_homepage_card_hcr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Definite statement "will stop working properly" is weakened to "may not work properly".
    - Current: `Firefox sürümünüz artık düzgün çalışmayabilir`
    - Source: `A root certificate will expire, causing your version of Firefox to stop working properly.`
    - Suggest: `Firefox sürümünüz düzgün çalışmayacak`
    - The source states the version will stop working properly; "çalışmayabilir" expresses possibility, altering the meaning.
- `certificate_warning_homepage_card_hcw2_message` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "other Firefox features" is translated as "bazı Firefox özellikleri" (some Firefox features).
    - Current: `eklentiler ve bazı Firefox özellikleri`
    - Source: `On March 14, add-ons and other Firefox features will stop working because a root certificate is expiring.`
    - Suggest: `eklentiler ve diğer Firefox özellikleri`
    - The source says "add-ons and other Firefox features"; "bazı" means "some", not "other".
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The date meaning is changed: source says features stop working on March 14, translation says after March 14.
    - Current: `14 Mart’tan sonra çalışmayacak`
    - Source: `Add-ons and some features will stop working on March 14.`
    - Suggest: `14 Mart’ta çalışmayı durduracak`
    - en-US "will stop working on March 14" means on that date, not after it.
- `certificate_warning_push_notification_update_recommended_title` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Update recommended" (noun + past participle predicate) is rendered as the noun phrase "Recommended update".
    - Current: `Önerilen güncelleme`
    - Source: `Update recommended`
    - Suggest: `Güncelleme öneriliyor`
    - Source states that an update is recommended; the Turkish reads "the recommended update", changing the meaning.
- `customize_toggle_continue` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Homescreen section title "Continue" translated as "İleri" (Forward/Next).
    - Current: `İleri`
    - Source: `Continue`
    - Suggest: `Devam edin`
    - Per the developer comment this names the section that lets users continue where they left off; "İleri" means "forward/next" and does not convey "continue".
- `customize_toggle_jump_back_in` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Jump back in" is rendered as "Açık sekmeler" (Open tabs), which names a different homepage section.
    - Current: `Açık sekmeler`
    - Source: `Jump back in`
    - Suggest: `Kaldığınız yerden devam edin`
    - The source refers to the "Jump back in" section (recent tab), not "Open tabs"; the Turkish says something else.
- `customize_toggle_pocket_3` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Stories" translated as "Haberler" (News) instead of "Hikâyeler"/"Öyküler".
    - Current: `Haberler`
    - Source: `Stories`
    - Suggest: `Hikâyeler`
    - Pocket "Stories" are recommended articles, not news; the Turkish term changes the meaning.
- `customize_toggle_pocket_sponsored` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Sponsored stories" translated as "Sponsorlu haberler" (sponsored news).
    - Current: `Sponsorlu haberler`
    - Source: `Sponsored stories`
    - Suggest: `Sponsorlu hikâyeler`
    - "Stories" is not "haberler" (news); consistent with customize_toggle_pocket_3.
- `debug_drawer_add_new_address` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "selected locale" translated as "Seçili dil" (selected language) instead of locale.
    - Current: `Seçili dil için yeni adres ekle`
    - Source: `Add new address for selected locale`
    - Suggest: `Seçili yerel ayar için yeni adres ekle`
    - A locale is a language/region combination; in this debug tool addresses depend on region, so "dil" is inaccurate.
- `debug_drawer_addresses_debug_locales_header` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Debug locales to enable" translated as "Etkinleştirilebilen hata ayıklama dilleri" (enable-able debug languages), losing "locale" and altering the meaning.
    - Current: `Etkinleştirilebilen hata ayıklama dilleri`
    - Source: `Debug locales to enable`
    - Suggest: `Etkinleştirilecek hata ayıklama yerel ayarları`
    - Source lists locales to be enabled, not languages that can be enabled.
- `download_rename_error_cannot_rename_title` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Present-tense inability "Can't rename file" rendered as past tense "could not be renamed".
    - Current: `Dosya yeniden adlandırılamadı`
    - Source: `Can’t rename file`
    - Suggest: `Dosya yeniden adlandırılamıyor`
    - Source is "Can’t rename file" (present inability), matching the description string which uses "adı değiştirilemiyor"; the past tense changes the meaning and is inconsistent with the dialog body.
- `edit_tab_group_bottom_sheet_grabber_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "collapse drag handle" is rendered as "sürükleme tutamacını daralt", using "daralt" (narrow/shrink) instead of the UI sense of collapsing a sheet.
    - Current: `Yeni grup, sürükleme tutamacını daralt`
    - Source: `New group, collapse drag handle`
    - Suggest: `Yeni grup, sürükleme tutamacını kapat`
    - In the source the handle collapses the bottom sheet; Turkish "daralt" means to narrow, not collapse a sheet. Mozilla tr uses "daralt" for collapsing lists but here it is a sheet dismiss control; at minimum the current wording says the handle itself is narrowed.
- `etp_cookies_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The source says cookies are used to compile browsing data, but the translation says they are used to track your browsing.
    - Current: `farklı siteler arasındaki gezintilerinizi izlemek için kullandığı çerezleri engeller`
    - Source: `Blocks cookies that ad networks and analytics companies use to compile your browsing data across many sites.`
    - Suggest: `birçok sitedeki gezinti verilerinizi derlemek için kullandığı çerezleri engeller`
    - "compile your browsing data across many sites" means collecting/compiling data, not "izlemek" (to track).
- `history_multi_select_title` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — History multi-select title says "bookmarks selected" instead of just "selected".
    - Current: `%1$d yer imi seçildi`
    - Source: `%1$d selected`
    - Suggest: `%1$d seçildi`
    - Source is "%1$d selected" on the History screen; adding "yer imi" (bookmark) states wrong content for history items.
- `ip_protection_mozilla_vpn_upsell_body` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "up to 5 devices" rendered as "5 ayrı cihazdaki", dropping "up to".
    - Current: `5 ayrı cihazdaki tüm uygulamalarınızı koruyun`
    - Source: `Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `5 cihaza kadar tüm uygulamalarınızı koruyun`
    - The source says "up to 5 devices"; the translation states exactly 5 separate devices, losing the "up to" limit.
- `ip_protection_onboarding_body` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The unit "GB" is dropped from the monthly allowance sentence.
    - Current: `Her ay %2$d ücretsiz.`
    - Source: `%1$s by hiding your location, even on public Wi-Fi. Get %2$d GB free every month.`
    - Suggest: `Her ay %2$d GB ücretsiz.`
    - Source says "Get %2$d GB free every month"; the Turkish omits "GB", leaving a bare number with no unit.
- `micro_survey_prompt_title` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "It only takes a minute" mistranslated as "takes only a few minutes".
    - Current: `Yalnızca birkaç dakika sürer.`
    - Source: `Help us make Firefox better. It only takes a minute.`
    - Suggest: `Yalnızca bir dakikanızı alır.`
    - The source says one minute; the Turkish says "a few minutes", overstating the time required.
- `microsurvey_prompt_printing_title` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "It only takes a sec" is rendered as a promise "we will only take a few seconds of your time" in first person, changing meaning and voice.
    - Current: `Yalnızca birkaç saniyenizi alacağız`
    - Source: `Help make printing in Firefox better. It only takes a sec`
    - Suggest: `Yalnızca birkaç saniye sürer`
    - The source states the survey takes only a second; the sibling strings (search/sync) correctly use "Yalnızca birkaç dakika sürer". The verb "alacağız" (we will take) shifts subject and tense inconsistently.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "how you discovered Firefox, and that you use it" is mistranslated as "how you discovered and use Firefox", losing the second fact.
    - Current: `Firefox’u nasıl keşfettiğinizi ve kullandığınızı`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `Firefox’u nasıl keşfettiğinizi ve Firefox’u kullandığınızı`
    - The source shares two things: how the user discovered Firefox, and the fact that they use it — not how they use it.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "how you discovered Firefox, and that you use it" is mistranslated as "how you discovered and use Firefox", losing the second fact.
    - Current: `Firefox’u nasıl keşfettiğinizi ve kullandığınızı`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Firefox’u nasıl keşfettiğinizi ve Firefox’u kullandığınızı`
    - The source shares two things: how the user discovered Firefox, and the fact that they use it — not how they use it.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "This data is never sold" is rendered as "we never sell this data", changing the subject/meaning.
    - Current: `Bu verileri asla satmayız.`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Bu veriler asla satılmaz.`
    - The source is a passive statement about the data never being sold; the Turkish makes Mozilla the explicit seller-actor and changes the statement.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "This data is never sold" is rendered as "we never sell this data", changing the subject/meaning.
    - Current: `Bu verileri asla satmayız.`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Bu veriler asla satılmaz.`
    - The source uses a passive statement that the data is never sold; the translation shifts it to a first-person claim.
- `past_explorations_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — “all” is dropped from the translation.
    - Current: `Geçmiş keşifleri göster`
    - Source: `Show all past explorations`
    - Suggest: `Tüm geçmiş keşifleri göster`
    - Source is “Show all past explorations”; the button navigates to the full history, so “all” carries meaning.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The translation drops the meaning "even on websites that prevent this gesture", turning it into "only on websites that don't allow it".
    - Current: `Sıkıştırma ve yakınlaştırma hareketine izin vermeyen sitelerde bu hareketi etkinleştir.`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `Bu hareketi engelleyen sitelerde bile sıkıştırma ve yakınlaştırma hareketine izin vermek için etkinleştirin.`
    - Source says enabling allows pinch-and-zoom everywhere, even on sites that block the gesture; the Turkish limits it to sites that block it and omits the "enable to allow" framing.
- `preference_doh_max_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "security risk warning" is translated merely as "security warning" and the subject shifts.
    - Current: `Sistem DNS’inizi kullanmadan önce bir güvenlik uyarısı gösterir.`
    - Source: `%1$s will always use secure DNS. You’ll see a security risk warning before we use your system DNS.`
    - Suggest: `Sistem DNS’inizi kullanmadan önce size bir güvenlik riski uyarısı göstereceğiz.`
    - Source: "You’ll see a security risk warning before we use your system DNS." The word "risk" is dropped.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "will cause websites to break" is rendered as a possibility ("bozulabilir") limited to "some" sites.
    - Current: `Tüm çerezler (Bazı web siteleri bozulabilir.)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `Tüm çerezler (Web siteleri bozulur.)`
    - The source says all cookies WILL cause websites to break, unlike the previous option which says "may cause"; the translation weakens it and adds "bazı" (some), making the two options identical.
- `preferences_category_delete_or_remove_downloads` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The 'or remove' part of the source is dropped from the translation.
    - Current: `İndirmeleri silme`
    - Source: `Delete or remove downloads`
    - Suggest: `İndirmeleri silme veya kaldırma`
    - Source is "Delete or remove downloads"; the Turkish only says "deleting downloads".
- `preferences_google_lens_availability_caption` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The translation drops "while browsing" and renders "is your active search engine" as "is set as your active search engine", losing part of the source meaning.
    - Current: `Yalnızca yukarıdan Google etkinleştirildiğinde ve aktif arama motorunuz olarak ayarlandığında kullanılabilir.`
    - Source: `Available only when Google is enabled above and is your active search engine while browsing.`
    - Suggest: `Yalnızca yukarıdan Google etkinleştirildiğinde ve gezinirken aktif arama motorunuz olduğunda kullanılabilir.`
    - Source says "…and is your active search engine while browsing"; the phrase "while browsing" is omitted in the Turkish text.
- `preferences_passwords_autofill2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Autofill in %1$s" is rendered as "autofill with %1$s" instead of "in %1$s".
    - Current: `%1$s ile otomatik doldur`
    - Source: `Autofill in %1$s`
    - Suggest: `%1$s içinde otomatik doldur`
    - The source means autofilling inside the app (%1$s = app name); "ile" means "with", changing the meaning.
- `protection_panel_banner_protected_title` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "%s is on guard" is rendered as "%s is running", losing the protection meaning.
    - Current: `%s çalışıyor`
    - Source: `%s is on guard`
    - Suggest: `%s nöbette`
    - Source states the app is on guard (actively protecting); "çalışıyor" only means it is running.
- `qr_code_display_share_nearby` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Heading changes the perspective from "nearby" to "with people near me".
    - Current: `Bağlantıyı yakınımdakilerle paylaş`
    - Source: `Share link nearby`
    - Suggest: `Bağlantıyı yakındakilerle paylaş`
    - The source "Share link nearby" is neutral; the first-person "yakınımdakilerle" (with those near me) is inconsistent with the body text which uses "yakınınızdaki kişilerle" (formal second person).
- _…and 26 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_port_blocked_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — Possessive mismatch: "sizi korumak ve güvenliğini sağlamak" should be "güvenliğinizi".
    - Current: `sizi korumak ve güvenliğini sağlamak amacıyla`
    - Source: `{ <p> }The requested address specified a port (e.g., { <q> }mozilla.org:80{ </q> } for port 80 on mozilla.org) normally used for purposes { <em> }other{ </em> } than Web browsing. The browser has canceled the request fo…`
    - Suggest: `sizi korumak ve güvenliğinizi sağlamak amacıyla`
    - Source: "for your protection and security"; the 2nd person possessive is missing, making it read "its security".
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — "doğu" is a typo for "doğru" (correct).
    - Current: `sunucu doğu ara sertifikaları göndermiyor`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `sunucu doğru ara sertifikaları göndermiyor`
    - Source says "the server is not sending the correct intermediate certificates"; "doğu" (east) is a typo for "doğru".
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — "çalıştığınızı sayfa" is a typo for "çalıştığınız sayfa".
    - Current: `görüntülemeye çalıştığınızı sayfa gösterilemiyor`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because this website requires a secure connection.{ </li> } { <li> }The issue is most likely with the website, and there is nothing you can do to resolve…`
    - Suggest: `görüntülemeye çalıştığınız sayfa gösterilemiyor`
    - Accusative suffix on the relative clause is ungrammatical; should be "çalıştığınız sayfa" (the page you are trying to view).
- `mozac_feature_prompts_no_more_dialogs` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-tr/strings.xml` — Wrong case suffix: "oluşturmasının önle" should be accusative "oluşturmasını önle".
    - Current: `Bu sayfanın ek iletişim kutuları oluşturmasının önle`
    - Source: `Prevent this page from creating additional dialogs`
    - Suggest: `Bu sayfanın ek iletişim kutuları oluşturmasını önle`
    - The verb "önlemek" takes the accusative; the genitive "-nın" is a grammatical error.
- `mozac_support_ktx_menu_call_with` — `mozilla-mobile/android-components/components/support/ktx/src/main/res/values-tr/strings.xml` — "Bununla çağrı…" is ungrammatical/nonsensical for "Call with…".
    - Current: `Bununla çağrı…`
    - Source: `Call with…`
    - Suggest: `Şununla ara…`
    - The source is a verb phrase for choosing an app to place a call with; the Turkish uses a bare noun "çağrı" with "bununla", which is not grammatical Turkish for this action.
- `mozac_support_ktx_menu_email_with` — `mozilla-mobile/android-components/components/support/ktx/src/main/res/values-tr/strings.xml` — "Bununla e-posta…" lacks a verb, rendering "Email with…" ungrammatically.
    - Current: `Bununla e-posta…`
    - Source: `Email with…`
    - Suggest: `Şununla e-posta gönder…`
    - The source is an action for choosing an app to send email with; the Turkish is a bare noun phrase with no verb.
- `ip_protection_mozilla_vpn_upsell_body` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Missing word in "300’den fazla konum arasından istediğiniz seçin" — should be "istediğinizi seçin".
    - Current: `300’den fazla konum arasından istediğiniz seçin`
    - Source: `Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `300’den fazla konum arasından istediğinizi seçin`
    - The accusative object requires "istediğinizi"; as written the sentence is ungrammatical.
- `open_tabs_menu` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Missing accusative marker makes the content description ungrammatical.
    - Current: `Açık sekmeler menüsü aç`
    - Source: `Open tabs menu`
    - Suggest: `Açık sekmeler menüsünü aç`
    - Turkish requires the accusative case on the definite object: “menüsünü aç”. The source is “Open tabs menu”.
- `preference_enhanced_tracking_protection_custom_cookies_1` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Typo: "takip kodlrı" is missing a letter.
    - Current: `Siteler arası takip kodlrı ve sosyal medya takip kodları`
    - Source: `Cross-site and social media trackers`
    - Suggest: `Siteler arası takip kodları ve sosyal medya takip kodları`
    - "kodlrı" is a misspelling of "kodları".
- `preferences_passwords_save_logins_ask_to_save` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Ask to save" is mistranslated as "Kaydetmeyi sor", which is ungrammatical in Turkish.
    - Current: `Kaydetmeyi sor`
    - Source: `Ask to save`
    - Suggest: `Kaydetmeyi sor (Kaydetmek için sor)`
    - The option means the browser asks the user whether to save; "Kaydetmeyi sor" is not idiomatic Turkish for that prompt.
- `protection_panel_banner_not_protected_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — The app-name placeholder is turned into a possessive-less noun phrase, producing ungrammatical "%s korumaları kapalı" instead of stating that the app is off-duty.
    - Current: `%s korumaları kapalı.`
    - Source: `%s is off-duty. We suggest turning protections back on.`
    - Suggest: `%s görev başında değil.`
    - Source says the app itself is off-duty; the translation reads "%s protections off" without the required possessive suffix and changes the subject.
- `uninstall_survey_option_1_v2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Coordination is broken: "Yavaş veya stabil değil" reads as "slow or not stable" with mismatched predicates.
    - Current: `Yavaş veya stabil değil`
    - Source: `It’s slow or unreliable`
    - Suggest: `Yavaş veya kararsız`
    - Source is "It’s slow or unreliable"; the Turkish mixes an adjective with a negated predicate, and "stabil değil" also renders "unstable" rather than "unreliable".
- `webcompat_reporter_description_3` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Ungrammatical double construction "iyileştirmemize için" in the Turkish sentence.
    - Current: `herkes için iyileştirmemize için yardımcı oluyor`
    - Source: `Your report helps us understand and fix issues in %1$s to make it better for everyone. %2$s`
    - Suggest: `herkes için iyileştirmemize yardımcı oluyor`
    - "iyileştirmemize için" combines a dative nominalization with "için"; only one is grammatical.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Typo: "doğu" instead of "doğru".
    - Current: `sunucu doğu ara sertifikaları göndermiyor`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `sunucu doğru ara sertifikaları göndermiyor`
    - "correct intermediate certificates" should be "doğru ara sertifikalar"; "doğu" means "east" and is a misspelling.
- `preference_show_search_suggestions_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Mixed person: informal "yazdıklarını" with formal "arama motorunuza" in the same sentence.
    - Current: `%1$s, adres çubuğuna yazdıklarını arama motorunuza gönderecektir`
    - Source: `%1$s will send what you type in the address bar to your search engine`
    - Suggest: `%1$s, adres çubuğuna yazdıklarınızı arama motorunuza gönderecektir`
    - Source is "what you type"; the Turkish switches between informal and formal second person within one string, which is inconsistent and ungrammatical in agreement.
- `tool_tip_message` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Wrong case suffix: "ihtiyaçlarınızı göre" should be "ihtiyaçlarınıza göre".
    - Current: `ihtiyaçlarınızı göre`
    - Source: `These default settings offer strong protection. But it’s easy to tweak the settings to meet your specific needs.`
    - Suggest: `ihtiyaçlarınıza göre`
    - The postposition "göre" requires the dative case (-a/-e), not the accusative; "ihtiyaçlarınızı göre" is ungrammatical.

### D. Terminology, register & consistency

- `mozac_browser_errorpages_page_refresh` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — Informal imperative "dene" violates the locale's formal register.
    - Current: `Yeniden dene`
    - Source: `Try Again`
    - Suggest: `Yeniden deneyin`
    - The tr locale convention is formal address; other imperatives in this batch use the -in form.
- `mozac_feature_addons_permissions_management_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-tr/strings.xml` — "extension" is rendered as "eklenti" (add-on) here but as "uzantı" in the parallel _for_update string and elsewhere in the file.
    - Current: `Eklenti kullanımını izleme ve temaları yönetme`
    - Source: `Monitor extension usage and manage themes`
    - Suggest: `Uzantı kullanımını izleme ve temaları yönetme`
    - Source says "Monitor extension usage"; the identical string mozac_feature_addons_permissions_management_description_for_update uses "Uzantı", and "uzantı" is the established term for "extension" ("eklenti" = add-on).
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-tr/strings.xml` — "Upload" is rendered as "gönderilsin" in the dialog title but as "Karşıya yükle" in the confirm button and message of the same dialog.
    - Current: `Dosyalar gönderilsin mi?`
    - Source: `Upload files?`
    - Suggest: `Dosyalar karşıya yüklensin mi?`
    - Same source term "upload" in one dialog must use one term; the message and positive button use "karşıya yükle".
- `mozac_summarize_settings_shake_to_summarize` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-tr/strings.xml` — Imperative informal "salla" conflicts with the formal register used elsewhere in the same feature ("sallayın").
    - Current: `Özetlemek için salla`
    - Source: `Shake to summarize`
    - Suggest: `Özetlemek için sallayın`
    - The locale convention is formal address, and sibling strings use "sallayın"/"ayarlayın".
- `add_login_save_new_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "login" translated as "hesap" (account) while the surrounding add-login screen uses "parola" (password).
    - Current: `Yeni hesabı kaydet`
    - Source: `Save new login`
    - Suggest: `Yeni parolayı kaydet`
    - add_login_2 renders the same feature as "Parola ekle"; using "hesap" here is inconsistent terminology on the same surface.
- `bookmark_empty_list_guest_cta` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative used where the locale convention is formal address.
    - Current: `Eşitlemek için giriş yap`
    - Source: `Sign in to sync`
    - Suggest: `Eşitlemek için giriş yapın`
    - The tr locale uses the formal (-ın) imperative form, as in the surrounding strings ("Yeniden deneyin.", "Tüm yer imlerinizi bir arada tutun"); this button uses the informal "yap".
- `deleting_browsing_data_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "browsing data" is rendered as "Göz atma verileri" here while the same term is translated "gezinti verileri" in the related delete-browsing-data dialog string.
    - Current: `Göz atma verileri siliniyor…`
    - Source: `Deleting browsing data…`
    - Suggest: `Gezinti verileri siliniyor…`
    - delete_browsing_data_prompt_message_3 in the same surface uses “gezinti verileri” for "browsing data"; using a different term for the same feature is inconsistent.
- `edit_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Edit login" is translated as "Hesabı düzenle" (edit account) rather than the login/password entry term.
    - Current: `Hesabı düzenle`
    - Source: `Edit login`
    - Suggest: `Hesap bilgilerini düzenle`
    - The string refers to a saved login entry, not a user account; "Hesabı düzenle" suggests editing an account, which conflicts with the related password terminology (e.g. edit_2 "Parola düzenle").
- `exceptions_empty_message_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "tracking protection" rendered as "izlenme koruması" instead of the established "izleme koruması".
    - Current: `izlenme korumasını`
    - Source: `Exceptions let you disable tracking protection for selected sites.`
    - Suggest: `izleme korumasını`
    - Elsewhere in the same file "tracking" is rendered as "takip/izleme" (e.g. "Takip kodu", "Takip amaçlı içerikler"); "izlenme koruması" is inconsistent terminology for Tracking Protection.
- `exceptions_empty_message_learn_more_link` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative used where the locale convention is formal address.
    - Current: `Daha fazla bilgi al`
    - Source: `Learn more`
    - Suggest: `Daha fazla bilgi alın`
    - The tr locale uses the formal (plural) imperative, as in the surrounding strings ("Ayarlara git" aside, e.g. "telemetriyi etkinleştirin", "yeniden başlatın"); "al" is the informal singular form.
- `inactive_tabs_auto_close_message_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Auto-close" is translated as "Otomatik kapatma" here but as "kendiliğinden kapatılsın" in the related header string.
    - Current: `Otomatik kapatma açıldı`
    - Source: `Auto-close enabled`
    - Suggest: `Kendiliğinden kapatma açıldı`
    - The same auto-close feature on the same surface (inactive tabs auto-close message) uses two different terms; tr Firefox consistently uses "kendiliğinden" for auto-close.
- `ip_protection_onboarding_body_link_promo` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative "al" used where the locale convention is formal address.
    - Current: `Daha fazla bilgi al`
    - Source: `Learn more`
    - Suggest: `Daha fazla bilgi alın`
    - tr convention is the formal imperative; "al" is the informal singular form.
- `ip_protection_recommended_location` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Recommended" as an option label is rendered as the progressive "Öneriliyor" instead of "Önerilen".
    - Current: `Öneriliyor`
    - Source: `Recommended`
    - Suggest: `Önerilen`
    - The string labels the recommended server location option; Turkish uses the adjective "Önerilen", not "Öneriliyor" ("is being recommended").
- `lens_opt_out_title` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative "bul" used where the locale convention is formal address.
    - Current: `Google Lens ile bul`
    - Source: `Find it with Google Lens`
    - Suggest: `Google Lens ile bulun`
    - tr convention is the formal imperative; other strings in the same feature use the -in form.
- `lens_opt_out_try_it_now_button` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative used where the locale convention is formal address.
    - Current: `Hemen dene`
    - Source: `Try it now`
    - Suggest: `Hemen deneyin`
    - tr convention is the formal (plural) imperative, used in other buttons in this batch (e.g. "VPN’i açın", "deneyin").
- `nova_onboarding_marketing_body_link_text_1` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Link text uses informal imperative "al" instead of the established formal register.
    - Current: `Daha fazla bilgi al`
    - Source: `Learn More`
    - Suggest: `Daha fazla bilgi alın`
    - The locale's register convention is formal (siz); every other button/link in this batch uses the formal imperative ("Bildirimleri aç", "Temanızı seçin").
- `pdf_tools_signature_placeholder` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative "yaz" breaks the locale's formal register.
    - Current: `İmzanızı yaz`
    - Source: `Type signature`
    - Suggest: `İmzanızı yazın`
    - The tr locale convention is formal address; other imperatives in this batch use the formal form. "yaz" is the informal singular imperative.
- `preference_enhanced_tracking_protection_explanation_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative "al" violates the locale's formal register convention.
    - Current: `Daha fazla bilgi al`
    - Source: `Learn more`
    - Suggest: `Daha fazla bilgi alın`
    - The tr locale uses the formal (plural/polite) imperative; other strings in this batch use "bilgi alın" (preference_search_learn_about_fx_suggest).
- `saved_logins_add_new_login_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "login" translated as "hesap" (account), inconsistent with the password terminology used elsewhere in this surface.
    - Current: `Yeni hesap ekle`
    - Source: `Add new login`
    - Suggest: `Yeni parola ekle`
    - Other strings in the same logins/passwords screen use "parola" (e.g. "Parolaları sırala menüsü"); "hesap" (account) is a different concept from a saved login.
- `setup_checklist_subtitle_5_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Almost there!" is translated inconsistently as "Bitmek üzere!" here versus "Az kaldı!" in the parallel 3-step string.
    - Current: `Bitmek üzere!`
    - Source: `Almost there! You’re just 1 step away from the finish line.`
    - Suggest: `Az kaldı!`
    - The same source phrase "Almost there!" on the same setup-checklist surface is rendered two different ways (setup_checklist_subtitle_3_steps_second_step uses "Az kaldı!").
- `sign_in_with_email` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Imperative uses informal "yap" instead of the formal form used elsewhere in the same screen.
    - Current: `E-posta ile giriş yap`
    - Source: `Use email instead`
    - Suggest: `Bunun yerine e-posta kullanın`
    - Locale register is formal ("giriş yapın" is used in sign_in_with_camera and setup_checklist_task_account_sync); also the source is "Use email instead".
- `synced_tabs_sign_in_button` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Informal imperative "giriş yap" violates the locale's formal register.
    - Current: `Eşitlemek için giriş yap`
    - Source: `Sign in to sync`
    - Suggest: `Eşitlemek için giriş yapın`
    - The tr locale convention is formal address (second-person plural imperative), as used elsewhere (e.g. "Bu ekranı açık tutun").
- `translation_settings_control_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Learn more" link text uses the informal imperative "al", deviating from the locale's formal register.
    - Current: `Daha fazla bilgi al`
    - Source: `Learn more`
    - Suggest: `Daha fazla bilgi alın`
    - The tr locale convention is formal address; other imperative UI strings in this batch use the formal plural ("Dil seçin", "deneyin", "Kullanın").
- `translation_settings_control_title` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Translations" rendered in the singular here while the identical source term is plural ("Çeviriler") in translation_settings_toolbar_title on the same settings surface.
    - Current: `Çeviri`
    - Source: `Translations`
    - Suggest: `Çeviriler`
    - Source is "Translations" (plural); the sibling string translation_settings_toolbar_title on the same dialog uses "Çeviriler", making this inconsistent.
- `translations_bottom_sheet_info_message_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "Learn more" link text uses the informal imperative "al" instead of the formal form.
    - Current: `Daha fazla bilgi al`
    - Source: `Learn more`
    - Suggest: `Daha fazla bilgi alın`
    - The established tr register is formal; imperative verbs addressed to the user should take the formal plural ending.
- `translations_bottom_sheet_translate_from_unsupported_language` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Imperative "dene" is informal, contrary to the locale's formal register.
    - Current: `Başka bir kaynak dil dene`
    - Source: `Try another source language`
    - Suggest: `Başka bir kaynak dil deneyin`
    - The tr locale uses formal address for user-directed imperatives; compare "Yeniden dene"/"Dil seçin" conventions where formal plural is expected.
- `webcompat_reporter_etp_checkbox_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — "tracking protection" is rendered as "İzlenme koruması" instead of the established Turkish term "İzleyici koruması".
    - Current: `İzlenme koruması tarafından engellenen öğelerin listesini gönder`
    - Source: `Send list of items blocked by tracking protection`
    - Suggest: `İzleyici koruması tarafından engellenen öğelerin listesini gönder`
    - Mozilla tr consistently uses "izleyici koruması" (Gelişmiş İzleyici Koruması) for "tracking protection"; "izlenme koruması" is inconsistent with the rest of the product.
- `preference_autocomplete_menu_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Remove" is translated as "Sil" (delete) instead of "Kaldır".
    - Current: `Sil`
    - Source: `Remove`
    - Suggest: `Kaldır`
    - The source distinguishes Remove from Delete; Turkish standard for "Remove" is "Kaldır", and "Sil" means "Delete".
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Remove custom URLs" rendered with "sil" (delete) instead of "kaldır".
    - Current: `Özel adresleri sil`
    - Source: `Remove custom URLs`
    - Suggest: `Özel adresleri kaldır`
    - Source says "Remove"; Turkish equivalent is "kaldır", while "sil" corresponds to "delete".
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — First-person possessive "parmak izimi" breaks the formal second-person register used elsewhere.
    - Current: `Uygulama kilidini açmak için parmak izimi kullan`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `Uygulama kilidini açmak için parmak izini kullan`
    - The source is a neutral setting title ("Use fingerprint to unlock app"); the locale convention is formal address, not first-person "my fingerprint".
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — First-person "eklediysem" contradicts the second-person source and the formal register.
    - Current: `Kısayollar eklediysem veya %s tarayıcısında bir web sitesi açıksa kilidi parmak iziyle aç.`
    - Source: `Unlock using fingerprint if you’ve added Shortcuts or when a website is already open in %s.`
    - Suggest: `Kısayollar eklediyseniz veya %s tarayıcısında bir web sitesi açıksa kilidi parmak iziyle açın.`
    - The source uses second person ("if you’ve added Shortcuts"); the tr tree convention is formal second-person address.
- `preference_switch_autocomplete_user_list` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — First-person "Eklediğim" instead of second-person address used in the source.
    - Current: `Eklediğim sitelerde`
    - Source: `For sites you add`
    - Suggest: `Eklediğiniz sitelerde`
    - Source is "For sites you add"; the locale convention is formal second-person address, not first person.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_safe_phishing_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — Stray leading space before the placeholder.
    - Current: `{ <p> } %1$s web sayfasının`
    - Source: `{ <p> }This web page at %1$s has been reported as a deceptive site and has been blocked based on your security preferences.{ </p> }`
    - Suggest: `{ <p> }%1$s web sayfasının`
    - Extra space after the opening paragraph markup, inconsistent with the other error page strings.
- `mozac_lib_send_crash_report_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-tr/strings.xml` — `mozac_lib_send_crash_report_in_progress` uses a straight apostrophe
    - Current: `Çökme raporu %1$s'ya gönderiliyor`
    - Source: `Sending crash report to %1$s`
    - Suggest: `%1$s’ya`
    - The tree uses ’ 151 times against 1 straight.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `Web adresi "https://" veya "http://" içermelidir`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `Web adresi “https://” veya “http://” içermelidir`
    - The locale's quote convention is `curly-double` (14 occurrences).
- `ai_controls_block_dialog_what_will_be_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — Source is a statement label ending with a colon, but the translation turns it into a question with a question mark.
    - Current: `Neler engellenecek?`
    - Source: `What will be blocked:`
    - Suggest: `Engellenecekler:`
    - The developer comment says this is a label shown above the list of features; the en-US uses "What will be blocked:" with a colon, not a question.
- `onboarding_marketing_redesign_learn_more` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — A question mark is added to a statement-form link text.
    - Current: `Bu verileri nasıl kullanıyoruz?`
    - Source: `How we use the data`
    - Suggest: `Verileri nasıl kullanıyoruz`
    - The source "How we use the data" is a declarative link label with no question mark; the translation turns it into a question.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `Ana menüden "Çık"ı seçtiğinizde gezinti verilerini otomatik olarak siler`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“Çık”ı`
    - The locale's quote convention is `curly-double` (14 occurrences).

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

### Fixed to date (3)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-tr/strings.xml` — fixed 2026-08-22
- `bookmark_url_label` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — fixed 2026-08-22
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-tr/strings.xml` — fixed 2026-08-21
