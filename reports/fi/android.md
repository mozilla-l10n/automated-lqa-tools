# Android l10n QA — fi

| | |
|---|---|
| **Generated** | 2026-10-18 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `dd8ca757b7dd` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `dd8ca757b7dd` |
| **Previous run** | 2026-10-16 @ `4d7697d1b89b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 9 of 2,800 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fi: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Files | 45 |
| Strings | 2,800 |
| Missing strings | 2 |
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

**2 strings** are not translated yet, concentrated in:

- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fi/strings.xml` — 1
- `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 9, `straight-double` 7 | _mixed_ |
| ellipsis | `char` 21 | **char** |
| dash | `en` 3 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (51)

> **Reads as a deliberate edit (5).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "and that you use it" is translated as "and how you use it", which widens what data is shared.
    - Current: `kuinka käytät sitä`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `että käytät sitä`
    - The source shares only the fact that the user uses Firefox. The Finnish says Mozilla shares how the user uses Firefox, which is a materially wider data-sharing claim.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "and that you use it" is translated as "and how you use it", which widens what data is shared.
    - Current: `kuinka käytät sitä`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `että käytät sitä`
    - The source shares only the fact that the user uses Firefox. The Finnish says usage details are shared with marketing partners.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `ja kuinka käytät sitä`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `ja että käytät sitä`
    - The source shares only how Firefox was found and the fact that the user uses it. The Finnish says the user shares how they use Firefox, which is a wider data-sharing claim made to marketing partners.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `ja kuinka käytät sitä`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `ja että käytät sitä`
    - The source shares only how Firefox was found and the fact that the user uses it. The Finnish says usage details are shared with marketing partners, and the comment stresses that the data practices are limited.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "miten löysit Firefoxin ja käytät sitä" reads as sharing how you use Firefox, not that you use it.
    - Current: `miten löysit Firefoxin ja käytät sitä`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `miten löysit Firefoxin ja että käytät sitä`
    - Without 'että', the word 'miten' (how) also covers 'käytät sitä', so the text says the user shares how they use Firefox. The developer comment says explicitly that 'that you use it' only means continuing to use Firefox after installing it, not tracking usage. The translation therefore claims usage data goes to marketing partners, which the source doesn't say.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 20 |
| 3 | Degraded language (grammar, spelling, terminology) | 25 |
| 4 | Cosmetic (typography, spacing) | 6 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fi/strings.xml` — "Device" is translated as "tietokoneen" (computer) on a mobile error page.
    - Current: `Onko tietokoneen verkkoyhteys toimintakykyinen?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `Onko laitteen verkkoyhteys toiminnassa?`
    - The source says "Is the device connected to an active network?". This text appears in Android apps, and the same sentence in the offline error page already uses "laitteen", so "tietokoneen" is wrong and inconsistent.
- `mozac_feature_addons_permissions_browser_data_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fi/strings.xml` — "recent" is dropped, so the permission reads as clearing all browsing history.
    - Current: `Tyhjennä selaushistoria`
    - Source: `Clear recent browsing history, cookies, and related data`
    - Suggest: `Tyhjennä viimeisin selaushistoria`
    - The source says "Clear recent browsing history". The Finnish omits "recent", which widens the scope, and the sibling _for_update string translates it as "viimeisin".
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "Department" as an administrative division is translated as "Osasto", which means a department of an organisation.
    - Current: `Osasto`
    - Source: `Department`
    - Suggest: `Departementti`
    - The comment says this is the administrative division used in Colombia and Nicaragua. In Finnish those are "departementti" (e.g. Kolumbian departementit). "Osasto" means an organisational unit or a store section.
- `addresses_parish` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "Parish" (an administrative division) is translated as "Kirkonkylä", which means a church village.
    - Current: `Kirkonkylä`
    - Source: `Parish`
    - Suggest: `Pitäjä`
    - The comment says parishes are used for local administration and addressing in Barbados and Jamaica. "Kirkonkylä" is a village around a church, not an administrative area. "Pitäjä" (or "seurakunta") is the correct term.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "Item Menu for %s" is rendered as "Valikkokohde %s" ("menu item %s"), which names the wrong thing.
    - Current: `Valikkokohde %s`
    - Source: `Item Menu for %s`
    - Suggest: `Kohteen %s valikko`
    - The source and the developer comment describe the overflow menu that belongs to a bookmark or folder. "Valikkokohde" means an entry inside a menu, so the screen reader would describe a different control.
- `locale_search_hint` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — Placeholder 'Search language' (search for a language) rendered as the noun 'Hakukieli' (the language used for search).
    - Current: `Hakukieli`
    - Source: `Search language`
    - Suggest: `Hae kieltä`
    - Per the comment this is search-bar placeholder text in the language picker, inviting the user to search for a language; 'Hakukieli' means 'search language' as in the language of searches, which names a different thing.
- `microsurvey_prompt_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — The subject of the survey (search) is dropped; the Finnish asks to help make Firefox better in general.
    - Current: `Auta tekemään Firefoxista entistä parempi.`
    - Source: `Help make search in Firefox better. It only takes a minute`
    - Suggest: `Auta parantamaan hakua Firefoxissa.`
    - Source says "Help make search in Firefox better"; the translation omits search entirely, unlike the parallel printing and sync prompts, so the user isn't told what the survey is about.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "and that you use it" is translated as "and how you use it", which widens what data is shared.
    - Current: `kuinka käytät sitä`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `että käytät sitä`
    - The source shares only the fact that the user uses Firefox. The Finnish says Mozilla shares how the user uses Firefox, which is a materially wider data-sharing claim.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "and that you use it" is translated as "and how you use it", which widens what data is shared.
    - Current: `kuinka käytät sitä`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `että käytät sitä`
    - The source shares only the fact that the user uses Firefox. The Finnish says usage details are shared with marketing partners.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `ja kuinka käytät sitä`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `ja että käytät sitä`
    - The source shares only how Firefox was found and the fact that the user uses it. The Finnish says the user shares how they use Firefox, which is a wider data-sharing claim made to marketing partners.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "and that you use it" is translated as "and how you use it", which describes sharing more data than the source does.
    - Current: `ja kuinka käytät sitä`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `ja että käytät sitä`
    - The source shares only how Firefox was found and the fact that the user uses it. The Finnish says usage details are shared with marketing partners, and the comment stresses that the data practices are limited.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "Websites that prevent this gesture" is rendered as "websites that do not support this gesture".
    - Current: `eivät tue tätä elettä`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `estävät tämän eleen`
    - The source means sites that actively block pinch-zoom, and the setting overrides that block. "Eivät tue" (do not support) says something else: that the sites lack the ability.
- `preference_doh_increased_protection_info_1` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — First-person possessive 'valitsemaani' ('that I select') used instead of second-person 'you select'.
    - Current: `valitsemaani`
    - Source: `Use the provider you select`
    - Suggest: `valitsemaasi`
    - Source 'Use the provider you select' refers to the provider the user chooses; 'valitsemaani' means 'which I select', changing who selects.
- `preference_doh_max_protection_info_1` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — First-person possessive 'valitsemaani' ('that I select') used instead of second-person 'you select'.
    - Current: `valitsemaani`
    - Source: `Only use the provider you select`
    - Suggest: `valitsemaasi`
    - Source 'Only use the provider you select' refers to the user's choice; 'valitsemaani' means 'which I select'.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "miten löysit Firefoxin ja käytät sitä" reads as sharing how you use Firefox, not that you use it.
    - Current: `miten löysit Firefoxin ja käytät sitä`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `miten löysit Firefoxin ja että käytät sitä`
    - Without 'että', the word 'miten' (how) also covers 'käytät sitä', so the text says the user shares how they use Firefox. The developer comment says explicitly that 'that you use it' only means continuing to use Firefox after installing it, not tracking usage. The translation therefore claims usage data goes to marketing partners, which the source doesn't say.
- `recent_tabs_synced_device_icon_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — Singular "Synced device" is translated as plural "Synkronoidut laitteet".
    - Current: `Synkronoidut laitteet`
    - Source: `Synced device`
    - Suggest: `Synkronoitu laite`
    - The source and the comment describe the icon for a single synced device, but the Finnish says "synced devices".
- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The second sentence changes 'You don't need to open the app or see what's running in your browser' into 'you don't need to open the app to see the information from your browser'.
    - Current: `Sinun ei tarvitse avata sovellusta nähdäksesi tiedot selaimestasi.`
    - Source: `Notifications let you erase your %1$s session with a tap. You don’t need to open the app or see what’s running in your browser.`
    - Suggest: `Sinun ei tarvitse avata sovellusta tai nähdä, mitä selaimessasi on auki.`
    - The source lists two things the user doesn't need to do: open the app, or see what's running in the browser. The Finnish makes 'see' a purpose clause ('to see the information from your browser'), so it suggests the notification shows browser data without opening the app. That is not what the source says.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The plural "custom URLs" is translated as the singular "mukautettu osoite".
    - Current: `Poista mukautettu osoite`
    - Source: `Remove custom URLs`
    - Suggest: `Poista mukautetut osoitteet`
    - The source title is "Remove custom URLs" (plural). The screen lets the user select and remove several URLs, as the matching content description "delete all selected custom autocomplete URLs" shows. The Finnish says only one address is removed.
- `preference_privacy_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The Finnish says "Block all cookies", but the source only says "Block cookies".
    - Current: `Estä kaikki evästeet`
    - Source: `Block cookies`
    - Suggest: `Estä evästeet`
    - The source "Block cookies" doesn't say "all". This setting has options (e.g. blocking third-party cookies only), so adding "kaikki" (all) suggests every cookie gets blocked, which is wrong.
- `preference_search_remove_title` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — Plural 'search engines' rendered as singular 'hakukone'.
    - Current: `Poista hakukone`
    - Source: `Remove search engines`
    - Suggest: `Poista hakukoneita`
    - Source title is 'Remove search engines' (plural, a screen for removing engines from the list); Finnish says 'Remove search engine'.

### C. Grammar, agreement & spelling

- `mozac_feature_addons_failed_to_translate` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fi/strings.xml` — "maa-asetustolle" is a misspelling of "maa-asetukselle".
    - Current: `maa-asetustolle`
    - Source: `Translation not found, for locale %1$s neither default language %2$s`
    - Suggest: `maa-asetukselle`
    - The allative form of "maa-asetus" is "maa-asetukselle". "asetustolle" is not a Finnish word.
- `mozac_feature_addons_migrated_from_a_previous_version_label` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fi/strings.xml` — Non-standard verb form "migratoitiin".
    - Current: `migratoitiin`
    - Source: `This add-on was migrated from a previous version of %1$s`
    - Suggest: `siirrettiin`
    - The standard Finnish verb is "migroida" (migroitiin), or plain "siirtää". "migratoida" is not a standard form.
- `mozac_feature_autofill_confirmation_authenticity` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-fi/strings.xml` — Misspelled genitive plural "kirjautumistietoijen".
    - Current: `kirjautumistietoijen`
    - Source: `%1$s could not verify the authenticity of the application. Do you want to proceed with autofilling the selected credentials?`
    - Suggest: `kirjautumistietojen`
    - The genitive plural of "kirjautumistiedot" is "kirjautumistietojen"; the extra "i" is a spelling error.
- `mozac_feature_downloads_cancel_active_downloads_warning_content_title` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fi/strings.xml` — "Perutetaanko" is misspelled; it isn't a valid Finnish verb form.
    - Current: `Perutetaanko`
    - Source: `Cancel private downloads?`
    - Suggest: `Peruutetaanko`
    - The passive interrogative of "peruuttaa" is "peruutetaanko". The passive of "perua" would be "perutaanko". "Perutetaanko" mixes the two and isn't a real word.
- `mozac_protections_dashboard_trackers_blocked_this_week_title` — `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values-fi/strings.xml` — Title uses the numeral-dependent partitive singular "seurainta" with no number and starts lowercase, reading as a truncated fragment.
    - Current: `seurainta estetty tällä viikolla`
    - Source: `Trackers blocked this week`
    - Suggest: `Seuraimia estetty tällä viikolla`
    - "Trackers blocked this week" is a standalone title with no count; "seurainta" is only grammatical after a numeral, so the plural partitive "Seuraimia" (capitalized) is required.
- `mozac_feature_summarize_feedback_bad_click_label` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-fi/strings.xml` — The object of 'arvioidaksesi' is in the wrong case: nominative 'yhteenveto' instead of accusative 'yhteenvedon'.
    - Current: `arvioidaksesi yhteenveto huonoksi`
    - Source: `rate summary as bad`
    - Suggest: `arvioidaksesi yhteenvedon huonoksi`
    - The total object of the transitive verb 'arvioida' needs the accusative (genitive-form) 'yhteenvedon'. With the nominative the label is ungrammatical.
- `mozac_feature_summarize_feedback_good_click_label` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-fi/strings.xml` — The object of 'arvioidaksesi' is in the wrong case: nominative 'yhteenveto' instead of accusative 'yhteenvedon'.
    - Current: `arvioidaksesi yhteenveto hyväksi`
    - Source: `rate summary as good`
    - Suggest: `arvioidaksesi yhteenvedon hyväksi`
    - The total object of the transitive verb 'arvioida' needs the accusative (genitive-form) 'yhteenvedon'. With the nominative the label is ungrammatical.
- `mozac_summarize_info_error_message` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-fi/strings.xml` — Verb is in the infinitive/3rd-person form instead of the imperative.
    - Current: `Yrittää myöhemmin uudelleen.`
    - Source: `Try again later.`
    - Suggest: `Yritä myöhemmin uudelleen.`
    - Source 'Try again later.' is an imperative addressed to the user; 'Yrittää' reads as 'to try'/'tries', which is ungrammatical here. The imperative is 'Yritä'.
- `etp_cookies_description` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — The infinitive has the wrong person ending: "kerätäksesi" (second person) should be "kerätäkseen", because the ones collecting are the ad networks and analytics companies.
    - Current: `kerätäksesi selaustietojasi`
    - Source: `Blocks cookies that ad networks and analytics companies use to compile your browsing data across many sites.`
    - Suggest: `kerätäkseen selaustietojasi`
    - The source says ad networks and analytics companies use the cookies to compile your browsing data. The second-person ending makes it read as though the user is the one collecting the data. Correct Finnish needs the third-person form "kerätäkseen".
- `notification_marketing_channel_name` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — Misspelling: "Markkintointi" should be "Markkinointi".
    - Current: `Markkintointi`
    - Source: `Marketing`
    - Suggest: `Markkinointi`
    - The Finnish word for marketing is "markkinointi"; the translation is missing an "n" and swaps letters, and it is shown in system notification settings.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — The wrong relative pronoun is used: "mitkä" where standard Finnish requires "jotka".
    - Current: `niillä sivustoilla mitkä`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `niillä sivustoilla, jotka`
    - In standard written Finnish, a relative clause that refers to a noun takes "jotka", and the comma before it is required. "Mitkä" is colloquial and not correct here.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — Ungrammatical construction 'vaikeuttaen muiden nähdä'; 'vaikeuttaa' requires an object.
    - Current: `vaikeuttaen muiden nähdä`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access. %1$s`
    - Suggest: `vaikeuttaen muiden mahdollisuutta nähdä`
    - 'vaikeuttaa' is transitive and cannot take a bare infinitive with a genitive subject; it needs an object noun such as 'mahdollisuutta'.
- `preference_expanded_toolbar` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "Laajennuttu" is a misspelling of the past participle "Laajennettu".
    - Current: `Laajennuttu`
    - Source: `Expanded`
    - Suggest: `Laajennettu`
    - The source "Expanded" calls for the passive past participle of "laajentaa", which is "laajennettu". "Laajennuttu" is not a valid Finnish form.
- `sign_in_create_account_text` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "Firefox" is missing its case ending as the object of "synkronoidaksesi".
    - Current: `synkronoidaksesi Firefox laitteiden välillä`
    - Source: `No account? { <u> }Create one{ </u> } to sync Firefox between devices.`
    - Suggest: `synkronoidaksesi Firefoxin laitteiden välillä`
    - The object of the verb "synkronoida" needs a case ending, so it should be "Firefoxin". The bare nominative is ungrammatical.
- `translations_bottom_sheet_translate_from` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — The source language takes the ablative "kieleltä" instead of the elative "kielestä".
    - Current: `Käännä kieleltä`
    - Source: `Translate from`
    - Suggest: `Käännä kielestä`
    - Finnish uses the elative case for translating from a language (kääntää englannista). The same dialog already does this in "Käännetty kielestä %1$s" and "Sivu käännetty kielestä %1$s", so the ablative here is both a case error and inconsistent with those strings.
- `uninstall_survey_option_6_v2` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — Misspelling: "turvallisuuhuolet" is missing an "s".
    - Current: `turvallisuuhuolet`
    - Source: `Privacy or security concerns`
    - Suggest: `turvallisuushuolet`
    - The compound is turvallisuus + huolet, so it should be spelled "turvallisuushuolet".
- `wallpaper_artist_series_title` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — The compound "Taiteilija-sarja" has a hyphen it shouldn't have.
    - Current: `Taiteilija-sarja`
    - Source: `Artist series`
    - Suggest: `Taiteilijasarja`
    - Finnish compounds are written as one word. A hyphen is only used where the same vowel meets at the join, and here "a" meets "s".
- `contextmenu_erased_images_note2` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The comma before the subordinate clause starting with 'kun' is missing.
    - Current: `{ </b> } kun`
    - Source: `Saved and shared images { <b> }will not be{ </b> } deleted when you erase %1$s history`
    - Suggest: `{ </b> }, kun`
    - Finnish punctuation rules require a comma before a subordinate clause introduced by 'kun' ('ei poisteta, kun tyhjennät…').
- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The object of 'käyttää' is the bare 'HTTPS' with no case ending, and the word 'connection' from the source is missing.
    - Current: `yrittää käyttää HTTPS aina kun`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `yrittää käyttää HTTPS-yhteyttä aina, kun`
    - The verb 'käyttää' needs its object in the partitive case, so an uninflected 'HTTPS' is ungrammatical. The source says 'an HTTPS connection', which is naturally 'HTTPS-yhteyttä'. Finnish also requires a comma before the 'kun' clause.

### D. Terminology, register & consistency

- `mozac_feature_addons_settings_allow_in_private_browsing_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fi/strings.xml` — "Private browsing" is translated as "yksityisessä selailussa" here, but as "yksityisessä selauksessa" in the neighbouring setting on the same add-on settings screen.
    - Current: `yksityisessä selailussa`
    - Source: `Allow extension to run in private browsing`
    - Suggest: `yksityisessä selauksessa`
    - Firefox in Finnish uses "yksityinen selaus" as its term for private browsing, and mozac_feature_addons_settings_run_in_private_browsing on the same screen uses "selauksessa". Using "selailussa" here makes the term inconsistent.
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — `never_translate_site_header_preference` quotes “Älä käännä koskaan tätä sivustoa” but the string it names, `translation_option_bottom_sheet_never_translate_site`, reads “Älä koskaan käännä sivustoa”
    - Current: `Uuden sivuston lisääminen: Käy sivustolla ja valitse käännösvalikosta “Älä käännä koskaan tätä sivustoa”.`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `Älä koskaan käännä sivustoa`
    - In the source this string quotes “Never translate this site”, which is exactly the value of `translation_option_bottom_sheet_never_translate_site` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `preference_gestures_dynamic_toolbar` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "Toolbar" is translated as "työkalurivi" here but as "työkalupalkki" in the next gesture setting on the same screen.
    - Current: `työkalurivin`
    - Source: `Scroll to hide toolbar`
    - Suggest: `työkalupalkin`
    - The same source term "toolbar" appears in neighbouring gesture preferences. preference_gestures_swipe_toolbar_show_tabs_2 uses "työkalupalkkia", so the terminology is inconsistent on one settings screen.
- `saved_login_duplicate` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "username" is rendered as "käyttäjänimi" here but as "käyttäjätunnus" in every other login string.
    - Current: `tällä käyttäjänimellä`
    - Source: `A login with that username already exists`
    - Suggest: `tällä käyttäjätunnuksella`
    - The login screens (saved_login_clear_username, saved_login_copy_username, saved_login_username_required_2) use "käyttäjätunnus" for username, so this string is inconsistent on the same surface.
- `shortcut_url_hint` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — "Shortcut" is rendered as "Oikotie" here but as "pikavalinta" in the sibling shortcut strings on the same edit screen.
    - Current: `Oikotien URL-osoite`
    - Source: `Shortcut URL`
    - Suggest: `Pikavalinnan URL-osoite`
    - The neighbouring string shortcut_name_hint uses "Pikavalinnan nimi", and the other shortcut strings also use "pikavalinta". "Oikotie" means a literal shortcut path, which is the wrong sense for this field.
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — eIDAS term 'qualified' rendered as 'kelvollinen' (valid) instead of the regulation's official Finnish term 'hyväksytty'.
    - Current: `kelvollinen`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `hyväksytty`
    - The comment explains this is the eIDAS 'qualified' certificate status; the Finnish version of the eIDAS regulation uses 'hyväksytty' (e.g. 'hyväksytty varmenne'), while 'kelvollinen' means valid/eligible.

### E. Typography, punctuation & spacing

- `mozac_feature_addons_failed_to_uninstall` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fi/strings.xml` — There is no space between "Lisäosan" and the add-on name placeholder.
    - Current: `Lisäosan%1$s`
    - Source: `Failed to uninstall %1$s`
    - Suggest: `Lisäosan %1$s`
    - Without the space, the add-on name runs straight into "Lisäosan" on screen. The sibling strings (failed_to_remove and others) all have a space here.
- `nova_onboarding_sync_title` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — The comma before the relative clause "mihin jäit" is missing.
    - Current: `Jatka siitä mihin jäit`
    - Source: `Instantly pick up where you left off`
    - Suggest: `Jatka siitä, mihin jäit`
    - Finnish punctuation rules require a comma before a relative clause.
- `preferences_screenshots_in_private_mode_disclaimer` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — There is no comma before the subordinate clause that starts with "kun".
    - Current: `näkyvissä kun useita`
    - Source: `If allowed, private tabs will also be visible when multiple apps are open`
    - Suggest: `näkyvissä, kun useita`
    - Finnish punctuation rules require a comma before a subordinate clause that starts with a conjunction such as "kun".
- `preferences_sync_category` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — Missing comma before the subordinate clause "mitä synkronoidaan".
    - Current: `Valitse mitä synkronoidaan`
    - Source: `Choose what to sync`
    - Suggest: `Valitse, mitä synkronoidaan`
    - Finnish punctuation requires a comma before a subordinate clause introduced by a question word; the sibling string preferences_sync_category_no_engine_selected_summary correctly writes "Valitse, mitä…".
- `preferences_sync_category_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fi/strings.xml` — Missing comma before the subordinate clause beginning with "mitä".
    - Current: `Hallitse mitä kaikille`
    - Source: `Manage what syncs on all your connected devices`
    - Suggest: `Hallitse, mitä kaikille`
    - Finnish punctuation requires a comma before a subordinate clause introduced by "mitä"; inconsistent with the sibling string that uses the comma.
- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-fi/strings.xml` — The full stop at the end of the mission sentence is missing before the line break.
    - Current: `avointa Internetiä{ <br/> }`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `avointa Internetiä.{ <br/> }`
    - The source sentence 'Our mission is to foster a healthy, open Internet.' ends with a period, and so do the other sentences in the Finnish text. This one runs straight into the 'Lue lisää' link without one.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fi/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
