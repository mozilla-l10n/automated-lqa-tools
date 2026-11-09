# Firefox for Android l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `bf7b409a0435` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `bf7b409a0435` |
| **Previous run** | 2026-11-08 @ `c1a76afc1b60` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,601 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fy-NL: [Firefox](firefox.md) · [Focus for Android](focus_android.md)

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
| Files | 44 |
| Strings | 2,601 |
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
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 16 | **curly-single** |
| apostrophe | `typographic` 104 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 6 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (58)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 12 |
| 3 | Degraded language (grammar, spelling, terminology) | 45 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `about_crashes` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Crashes" (browser crashes, about:crashes) is rendered as "Ungelokken" (accidents), the wrong term, and it is also missing its diacritic.
    - Current: `Ungelokken`
    - Source: `Crashes`
    - Suggest: `Ûnderbrekkingen`
    - The developer comment says this links to a list of past crashes (about:crashes). "Ungelokken" means "accidents"; also the initial U should be Û ("Ûngelokken") in Frisian.
- `addresses_street_address` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Street Address" is translated as just "Adres", losing the street distinction and colliding with the generic address label.
    - Current: `Adres`
    - Source: `Street Address`
    - Suggest: `Strjitte en hûsnûmer`
    - The source specifically labels the street address line; rendering it as the generic "Adres" makes it indistinguishable from other address labels in the same form.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "extensions that use AI provided by %1$s" is rendered as "utwreidingen dy't AI troch %1$s brûke", which misconstrues the relation.
    - Current: `útwreidingen dy’t AI troch %1$s brûke`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `útwreidingen dy’t troch %1$s levere AI brûke`
    - The source means extensions using AI that Firefox provides; the current word order reads as "extensions that use AI by means of Firefox", changing the meaning.
- `browser_custom_tab_menu_handlebar_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Custom tab menu sheet" rendered as "Menublêd Ljepblêd oanpasse", turning the noun phrase into an imperative "customize tab".
    - Current: `Menublêd Ljepblêd oanpasse slute`
    - Source: `Close custom tab menu sheet`
    - Suggest: `Menublêd fan oanpast ljepblêd slute`
    - The source describes closing the menu sheet of a custom tab; the translation reads as "Customize tab menu sheet close", changing the meaning.
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Navigate back" translated as "Tebek blêdzje" (browse back) rather than navigating back within the drawer.
    - Current: `Tebek blêdzje`
    - Source: `Navigate back`
    - Suggest: `Tebek navigearje`
    - The developer comment says the control navigates back within the debug drawer, not page browsing; "blêdzje" implies web page navigation.
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Please consider allowing" is rendered as "think about permission", losing the request to grant permission.
    - Current: `Tink asjebleaft oer tastimming om Firefox te helpen winnen.`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Oerwaach asjebleaft om tastimming te jaan om Firefox winne te litten.`
    - The developer comment explains that "allowing" refers to granting permission via the "Allow and Continue" button; the current wording only says to think about permission and drops the act of allowing.
- `nova_onboarding_set_to_default_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Translation states companies do spy on your clicks instead of blocking them from spying.
    - Current: `blokkearje automatysk bedriuwen dy’t jo klikken bespionearje`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `foarkomme automatysk dat bedriuwen jo klikken bespionearje`
    - The source is "automatically block companies from spying on your clicks"; the relative clause presupposes the spying instead of preventing it.
- `phone_feature_blocked_intro` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "To allow it:" is rendered as the bare verb "Tastean:" losing the introductory meaning.
    - Current: `Tastean:`
    - Source: `To allow it:`
    - Suggest: `Om dit ta te stean:`
    - The source is a heading introducing the steps to allow the permission ("To allow it:"), not a command "Allow:".
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Sort passwords menu" (a menu for sorting passwords) is rendered as an imperative "sort the password menu".
    - Current: `Wachtwurdmenu sortearje`
    - Source: `Sort passwords menu`
    - Suggest: `Menu Wachtwurden sortearje`
    - The source is a noun phrase naming the menu used to sort passwords, not an instruction to sort a 'password menu'.
- `setup_checklist_group_essentials` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "essentials" is left untranslated in the compound "%1$s-essentials".
    - Current: `%1$s-essentials`
    - Source: `%1$s essentials`
    - Suggest: `%1$s-essinsjes`
    - "essentials" is an ordinary English noun, not a brand name, and should be rendered in Frisian (e.g. "basisynstellingen" / "essinsjes").
- `translations_bottom_sheet_translating_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Translating" (in-progress state) is translated as the infinitive "Oersette", identical to the "Translate" button, losing the progress meaning.
    - Current: `Oersette`
    - Source: `Translating`
    - Suggest: `Oersette…`
    - The developer comment states this is the inactive button text indicating a translation is currently in progress; rendering it identically to translations_bottom_sheet_positive_button ("Translate" = "Oersette") removes the distinction between the two states.
- `webcompat_reporter_reason_notsupported_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — The order of the two conditions is swapped relative to the source.
    - Current: `Browser wurdt net stipe of blokkearre`
    - Source: `Browser is blocked or unsupported`
    - Suggest: `Browser wurdt blokkearre of net stipe`
    - Source is “Browser is blocked or unsupported”; the translation reverses the order and reads as “not supported or blocked”, where “net” no longer applies to “blokkearre”.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_malformed_uri_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Unjildich".
    - Current: `Unjildich adres`
    - Source: `Invalid Address`
    - Suggest: `Ûnjildich adres`
    - The Frisian word is "ûnjildich" with a circumflex; the same prefix is written "ûnjildige" in mozac_browser_errorpages_invalid_content_encoding_message.
- `mozac_feature_downloads_file_failure_no_connection` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — The Frisian says the file "is not downloading" instead of the past "wasn’t downloaded".
    - Current: `%1$s is net downloaden.`
    - Source: `%1$s wasn’t downloaded.`
    - Suggest: `%1$s is net download.`
    - Source is past tense/perfect: the download failed. "is net downloaden" reads as an infinitive construction, not the completed-action past participle.
- `mozac_feature_listentopage_notification_playback_speed_1_25` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ofspylsnelheid"; should be "Ôfspylsnelheid".
    - Current: `Ofspylsnelheid 25 prosint flugger`
    - Source: `Playback rate 25 percent faster`
    - Suggest: `Ôfspylsnelheid 25 prosint flugger`
    - Frisian "ôf" carries a circumflex; inconsistent with "ôfspylsnelheid" used elsewhere in the same file.
- `mozac_feature_listentopage_notification_playback_speed_1_5` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ofspylsnelheid"; should be "Ôfspylsnelheid".
    - Current: `Ofspylsnelheid 50 prosint flugger`
    - Source: `Playback rate 50 percent faster`
    - Suggest: `Ôfspylsnelheid 50 prosint flugger`
    - Frisian "ôf" carries a circumflex; inconsistent with "ôfspylsnelheid" used elsewhere in the same file.
- `mozac_feature_listentopage_notification_playback_speed_1_75` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ofspylsnelheid"; should be "Ôfspylsnelheid".
    - Current: `Ofspylsnelheid 75 prosint flugger`
    - Source: `Playback rate 75 percent faster`
    - Suggest: `Ôfspylsnelheid 75 prosint flugger`
    - Frisian "ôf" carries a circumflex; inconsistent with "ôfspylsnelheid" used elsewhere in the same file.
- `mozac_feature_listentopage_notification_playback_speed_2` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ofspyljen"; should be "Ôfspyljen".
    - Current: `Ofspyljen ynsteld op dûbele snelheid`
    - Source: `Playback set to double speed`
    - Suggest: `Ôfspyljen ynsteld op dûbele snelheid`
    - Frisian "ôf-" requires the circumflex, as used in other strings of this file.
- `mozac_feature_listentopage_play` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ofspylje"; should be "Ôfspylje".
    - Current: `Ofspylje`
    - Source: `Play`
    - Suggest: `Ôfspylje`
    - Frisian "ôfspylje" is written with a circumflex, as in "ôfspylsnelheid" elsewhere in this file.
- `mozac_feature_media_notification_action_play` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-fy-rNL/strings.xml` — Missing accent on the initial 'Ô' in 'Ofspylje'.
    - Current: `Ofspylje`
    - Source: `Play`
    - Suggest: `Ôfspylje`
    - Frisian spelling is 'ôfspylje'; capitalised it is 'Ôfspylje', not 'Ofspylje'.
- `mozac_feature_prompts_expand_credit_cards_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — Superfluous infinitive marker "te" in the content description.
    - Current: `Bewarre kaarten te útklappe`
    - Source: `Expand saved cards`
    - Suggest: `Bewarre kaarten útklappe`
    - The parallel strings (expand saved addresses, collapse saved passwords) use the bare infinitive "Bewarre adressen útklappe" / "Bewarre wachtwurden ynklappe"; the added "te" is ungrammatical here and inconsistent.
- `mozac_feature_prompts_expand_logins_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — Superfluous infinitive marker "te" in the content description.
    - Current: `Bewarre wachtwurden te útklappe`
    - Source: `Expand saved passwords`
    - Suggest: `Bewarre wachtwurden útklappe`
    - Parallel string mozac_feature_prompts_collapse_logins_content_description_2 uses "Bewarre wachtwurden ynklappe" without "te"; the "te" is ungrammatical and inconsistent.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_settings_label` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-fy-rNL/strings.xml` — Unnecessary capitalisation of "Ynstellingen" mid-sentence in the button label.
    - Current: `Nei Ynstellingen`
    - Source: `Go to settings`
    - Suggest: `Nei ynstellingen`
    - Source is sentence case ("Go to settings"); Frisian does not capitalise common nouns.
- `mozac_lib_crash_activity_title` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Ûngelokrapporten".
    - Current: `Ungelokrapporten`
    - Source: `Crash Reports`
    - Suggest: `Ûngelokrapporten`
    - Frisian spells the word with a circumflex: ûngelok. The initial capital must keep the diacritic (Û).
- `addon_ga_message_button_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial U of "Utwreidingen".
    - Current: `Utwreidingen ferkenne`
    - Source: `Explore extensions`
    - Suggest: `Ûtwreidingen ferkenne`
    - Elsewhere the same word is spelled "útwreidingen" with a diacritic; capitalised it must be "Ú/Û" rather than plain "U".
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic: "Ofdieling" should be "Ôfdieling".
    - Current: `Ofdieling`
    - Source: `Department`
    - Suggest: `Ôfdieling`
    - In Frisian the word is spelled "ôfdieling"; capitalised it keeps the circumflex: "Ôfdieling". The current form drops the required diacritic.
- `bookmark_import_bookmarks_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Út" in "Ut bestân ymportearje".
    - Current: `Ut bestân ymportearje`
    - Source: `Import from file`
    - Suggest: `Út bestân ymportearje`
    - The Frisian preposition is "út"; capitalized it requires the accent "Ú".
- `bookmark_import_menu_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Út" in "Ut bestân ymportearje".
    - Current: `Ut bestân ymportearje`
    - Source: `Import from file`
    - Suggest: `Út bestân ymportearje`
    - The Frisian preposition is "út"; capitalized it requires the accent "Ú".
- `bookmark_invalid_url_error` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Unjildige".
    - Current: `Unjildige URL`
    - Source: `Invalid URL`
    - Suggest: `Ûnjildige URL`
    - The Frisian word is "ûnjildich"; capitalized it is "Ûnjildige".
- `browser_feature_desktop_site_off` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ut"; Frisian for "Off" is "Ût".
    - Current: `Ut`
    - Source: `Off`
    - Suggest: `Ût`
    - The Frisian word for "off" is spelled "út/Ût" with a circumflex/accent; the toggle label drops the diacritic.
- `credit_cards_biometric_prompt_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial capital of "Ûntskoattelje".
    - Current: `Untskoattelje om jo bewarre kaarten te besjen`
    - Source: `Unlock to view your saved cards`
    - Suggest: `Ûntskoattelje om jo bewarre kaarten te besjen`
    - The Frisian verb is "ûntskoattelje"; capitalised it is "Ûntskoattelje", not "Untskoattelje".
- `credit_cards_biometric_prompt_message_pin` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Word order is ungrammatical: the imperative with object should be "Untskoattelje jo apparaat" reversed to "Ûntskoattelje jo apparaat" — actual defect is the missing circumflex/accent on Û and wrong construction.
    - Current: `Untskoattelje jo apparaat`
    - Source: `Unlock your device`
    - Suggest: `Ûntskoattelje jo apparaat`
    - Frisian "ûntskoattelje" is written with û; the initial capital must be Û. The same error appears in the neighbouring credit_cards_biometric_prompt_* strings.
- `credit_cards_biometric_prompt_unlock_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex on the initial capital of "Ûntskoattelje".
    - Current: `Untskoattelje om bewarre betellingsmetoaden te brûken`
    - Source: `Unlock to use saved payment methods`
    - Suggest: `Ûntskoattelje om bewarre betellingsmetoaden te brûken`
    - The Frisian verb is "ûntskoattelje"; capitalised it is "Ûntskoattelje".
- `customize_addon_collection_user_hint` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Adjective/noun agreement error: "Eigener kolleksje" instead of "Eigener fan de kolleksje"/"Kolleksje-eigener".
    - Current: `Eigener kolleksje (brûkers-ID)`
    - Source: `Collection owner (User ID)`
    - Suggest: `Kolleksje-eigener (brûkers-ID)`
    - The source is "Collection owner" (owner of the collection); "Eigener kolleksje" is two juxtaposed nouns without a valid Frisian compound or genitive, giving ungrammatical text.
- `delete_browsing_data_quit_off` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Út" (Frisian for "Off").
    - Current: `Ut`
    - Source: `Off`
    - Suggest: `Út`
    - The Frisian word for "Off" is "Út" with an acute accent on the capital U; "Ut" is a spelling error.
- `download_content_type_filter_image` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing accent on "Ôfbyldingen".
    - Current: `Ofbyldingen`
    - Source: `Images`
    - Suggest: `Ôfbyldingen`
    - Frisian spells the word with a circumflex: Ôfbylding(en). The initial capital should keep the diacritic.
- `download_rename_error_cannot_rename_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Spelling error: "betân" should be "bestân".
    - Current: `Kin betân net omneame`
    - Source: `Can’t rename file`
    - Suggest: `Kin bestân net omneame`
    - The Frisian word for "file" is "bestân" (as used in the related strings); "betân" is a typo.
- `etp_cookies_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Stray preposition 'yn' makes the sentence ungrammatical.
    - Current: `isolearret cookies yn op de website`
    - Source: `Total Cookie Protection isolates cookies to the site you’re on so trackers like ad networks can’t use them to follow you across sites.`
    - Suggest: `isolearret cookies op de website`
    - The source says cookies are isolated to the site you are on; 'isolearret cookies yn op de website' contains a superfluous 'yn' that breaks the sentence.
- `firefox_labs_no_labs_available_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "No" appears misplaced/incorrect rendering of "right now".
    - Current: `No gjin eksperimintele funksjes om te probearjen`
    - Source: `No experimental features to try right now`
    - Suggest: `Op dit stuit gjin eksperimintele funksjes om te probearjen`
    - Source is "No experimental features to try right now"; the sentence-initial "No" reads as the English word and does not convey "right now" idiomatically.
- `ip_protection_onboarding_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Untfang" is missing the diacritic; should be "Ûntfang".
    - Current: `Untfang elke moanne fergees %2$d GB.`
    - Source: `%1$s by hiding your location, even on public Wi-Fi. Get %2$d GB free every month.`
    - Suggest: `Ûntfang elke moanne fergees %2$d GB.`
    - Frisian "ûntfange" requires the circumflex; the string elsewhere (ip_protection_onboarding_body_promo) correctly uses "ûntfang".
- `likert_scale_option_i_plan_to_keep_using` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Ungrammatical verb order/construction "om Firefox brûke te bliuwen".
    - Current: `Ik bin fan plan om Firefox brûke te bliuwen`
    - Source: `I plan to keep using Firefox`
    - Suggest: `Ik bin fan plan om Firefox te bliuwen brûken`
    - The source "I plan to keep using Firefox" requires a correct Frisian infinitive construction; "om Firefox brûke te bliuwen" is not grammatical.
- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Untdek".
    - Current: `Untdek`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `Ûntdek`
    - The Frisian imperative of "ûntdekke" is "Ûntdek"; the capital U must carry the circumflex.
- `onboarding_redesign_set_default_browser_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Untfang" (should be "Ûntfang").
    - Current: `Untfang standert automatyske beskerming tsjin folgjen`
    - Source: `Get automatic tracking protection by default`
    - Suggest: `Ûntfang standert automatyske beskerming tsjin folgjen`
    - Frisian "ûntfange" requires the circumflex on the initial u; the capitalised form is "Û".
- `onboarding_redesign_sync_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic in "Untfang" (should be "Ûntfang").
    - Current: `Untfang blêdwizers, ljepblêden en wachtwurden op elk apparaat.`
    - Source: `Get bookmarks, tabs, and passwords on any device. All protected with encryption.`
    - Suggest: `Ûntfang blêdwizers, ljepblêden en wachtwurden op elk apparaat.`
    - Frisian "ûntfange" requires the circumflex on the initial u; the capitalised form is "Û".
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Ofslute" is missing the accent on the initial O.
    - Current: `‘Ofslute’`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `‘Ôfslute’`
    - Frisian spelling requires "Ôfslute" with a circumflex on the initial vowel.
- `preferences_show_search_optimization_cards` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Verb form "type" should be the plural/polite form "type" → "typt" agreeing with "jo".
    - Current: `wylst jo type`
    - Source: `Retrieve suggestions from Mozilla as you type`
    - Suggest: `wylst jo type `
    - In Frisian the polite pronoun "jo" takes the -e/-je form depending on verb class; "typen" is a weak verb class II, so the correct form is "jo type" — however the standard form after "jo" for this verb is "typje".
- `sign_out_dialog_confirm_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ofmelde"; should be "Ôfmelde".
    - Current: `Ofmelde`
    - Source: `Sign out`
    - Suggest: `Ôfmelde`
    - Frisian "ôfmelde" is spelled with a circumflex on the ô.
- `sign_out_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing circumflex in "Ofmelde"; should be "Ôfmelde".
    - Current: `Ofmelde by jo account?`
    - Source: `Sign out of your account?`
    - Suggest: `Ôfmelde by jo account?`
    - Frisian "ôfmelde" is spelled with a circumflex on the ô.
- `startup_crash_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Ungrammatical passive/verb construction "moat opnij opstarte wurde" for "needs to restart".
    - Current: `%s moat opnij opstarte wurde`
    - Source: `%s needs to restart`
    - Suggest: `%s moat opnij starte wurde`
    - "opnij opstarte wurde" doubles the restart notion and mixes active/passive; the source simply says the app needs to restart.
- `sync_send_tab_empty_state_link` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Untdek" is missing the circumflex; the correct Frisian spelling is "Ûntdek".
    - Current: `Untdek`
    - Source: `Learn how to connect a device`
    - Suggest: `Ûntdek`
    - The Frisian verb ûntdekke is written with û, as in "ûntdutsen" elsewhere in this batch; "Untdek" is a misspelling.
- `tab_crash_send_report` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Missing diacritic on "Ûngelokrapport".
    - Current: `Ungelokrapport nei Mozilla ferstjoere`
    - Source: `Send crash report to Mozilla`
    - Suggest: `Ûngelokrapport nei Mozilla ferstjoere`
    - Frisian spelling requires the circumflex: "ûngelok", so the sentence-initial capital must be Û.
- `tab_indicator_media_playing` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Playing media" is rendered as an infinitive phrase ("to play media") instead of a descriptive state.
    - Current: `Media ôfspylje`
    - Source: `Playing media`
    - Suggest: `Media wurdt ôfspile`
    - The source is a content description for an indicator showing that media is currently playing; "Media ôfspylje" reads as the command/infinitive "play media", not the state.
- `wrex_widget_error_try_refreshing` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — Typo: 'Probeaje' should be 'Probearje'.
    - Current: `Probeaje`
    - Source: `Try refreshing or check back later.`
    - Suggest: `Probearje`
    - The Frisian verb is 'probearje', as used correctly in other strings in this batch.

### D. Terminology, register & consistency

- `mozac_feature_addons_permissions_browser_data_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — "browsing history" is rendered as "browserskiednis" here but as "sneupskiednis" in the parallel _for_update string.
    - Current: `Resinte browserskiednis, cookies en relatearre gegevens wiskje`
    - Source: `Clear recent browsing history, cookies, and related data`
    - Suggest: `Resinte sneupskiednis, cookies en relatearre gegevens wiskje`
    - The same source sentence ("Clear recent browsing history, cookies, and related data") is translated with two different terms on the same surface; fy-NL uses "sneup-" for browsing (cf. sneupaktiviteit for "browsing activity").
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — The update variant uses an imperative form and different wording/terminology than the non-update variant of the same permission description.
    - Current: `Wreidzje jo ûntwikkelark út foar tagong ta gegevens yn jo iepen ljepblêden.`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `Untwikkelersark útwreidzje om jo gegevens yn iepen ljepblêden te benaderjen.`
    - mozac_feature_addons_permissions_devtools_description translates the identical source as ‘Untwikkelersark útwreidzje om jo gegevens yn iepen ljepblêden te benaderjen’; the update string must match in style (infinitive) and term (ûntwikkelersark vs ûntwikkelark) since these appear on the same surface.
- `setup_checklist_subtitle_5_steps_completed_state` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "setup steps" translated as "ynstallaasjestappen" (installation steps) instead of setup/configuration steps.
    - Current: `ynstallaasjestappen`
    - Source: `You’ve completed all 5 setup steps. Enjoy the speed, privacy, and security of %1$s.`
    - Suggest: `ynstelstappen`
    - The checklist concerns setting up the app (ynstelle), not installing it; other strings in the same feature use "ynstelle".
- `setup_checklist_subtitle_6_steps_completed_state` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "setup steps" translated as "ynstallaasjestappen" (installation steps) instead of setup/configuration steps.
    - Current: `ynstallaasjestappen`
    - Source: `You’ve completed all 6 setup steps. Enjoy the speed, privacy, and security of %1$s.`
    - Suggest: `ynstelstappen`
    - The checklist concerns setting up the app (ynstelle), not installing it; other strings in the same feature use "ynstelle".
- `terms_of_use_prompt_title_option_a` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — "Terms of Use" is translated as "Gebrûksbetingsten" here but "Brûkersbetingsten" in terms_of_use_prompt_link_terms_of_use on the same prompt.
    - Current: `Gebrûksbetingsten`
    - Source: `Terms of Use`
    - Suggest: `Brûkersbetingsten`
    - The same source term on the same surface is rendered two different ways, creating terminology inconsistency.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (31)

- `firefox_suggest_header` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The reviewer also rejected the same change in ref 2, and both strings use "Firefox Suggestjes", so this looks like a deliberate local rendering of the feature name, not a mistake.
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `mozac_browser_errorpages_archive_check_button` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): "argivearre" is the regular past participle of the Frisian verb "argivearje" (to archive); the finding itself proposes the identical spelling.
- `mozac_cfr_dismiss_button_content_description` — `mozilla-mobile/android-components/components/compose/cfr/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): The Frisian verb "slute" (to close) is spelled without an accent; "slúte" is not the standard form.
- `mozac_feature_addons_permissions_dialog_heading_required_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `mozac_feature_addons_permissions_privacy_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `mozac_feature_downloads_open_not_supported1` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): 'om … mei te iepenjen' refers back to the app (an app to open the files with), a normal grammatical Frisian construction, like Dutch 'mee te openen'.
- `mozac_feature_listentopage_dropdown_expanded` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian orthography drops the accent on a capitalised sentence-initial 'út', giving 'Ut'.
- `mozac_feature_listentopage_notification_playback_speed_0_25` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian orthography drops the circumflex on a capitalised sentence-initial 'ôf', giving 'Of'; lowercase 'ôf' elsewhere is consistent.
- `mozac_feature_listentopage_notification_playback_speed_0_5` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian orthography drops the circumflex on a capitalised sentence-initial 'ôf', giving 'Of'.
- `mozac_feature_listentopage_notification_playback_speed_0_75` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian orthography drops the circumflex on a capitalised sentence-initial 'ôf', giving 'Of'.
- `phone_feature_blocked_step_permissions` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian nouns in -ing form their plural in -ingen (cf. ynstellingen), so 'Machtigingen' is correct Frisian.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): In Frisian subordinate clauses the infinitive precedes the finite verb, so 'hokker website jo besykje gean' is grammatical.
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05): Swapping the order of the two joined verbs does not change the meaning; both share and sell are translated.
- `preference_phone_feature_cross_origin_storage_access` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian (like Dutch) writes compounds closed; 'Cross-sitecookies' is the regular compound form.
- `preference_search_address_bar_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The reviewer also rejected the same change in ref 0, and both strings use "Firefox Suggestjes", so this looks like a deliberate local rendering of the feature name, not a mistake.
- `preferences_category_sync_controls` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian spells this word with g (syngronisaasje, syngronisearje); 'ch' is the Dutch spelling.
- `preferences_passwords_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): The finding contradicts itself: the spelling it says is correct is the original exactly, so the reviewer probably didn't accept that there was an error.
- `review_prompt_feedback_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): 'efterlitte' is the standard Frisian verb; 'achterlitte' is Dutch.
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05): "%s trochsykje" follows the standard Dutch/Frisian Mozilla pattern (cf. nl "%s doorzoeken") for searching with a named engine.
- `setup_checklist_group_helpful_tools` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): 'ark' is a neuter mass noun; without an article the adjective stays uninflected ('nuttich ark'), like Dutch 'nuttig gereedschap'.
- `tab_tray_close_tabs_banner_negative_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05): "Slute" (close) is an accepted rendering of "Dismiss" for a banner button, as in Dutch "Sluiten".
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05): "Syngronisearre iepen ljepblêden" correctly means synced open tabs; word order is only a stylistic difference.
- `tracking_protection_off` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian orthography omits the accent on capital U (Út → Ut, cf. 'Utein', 'Ut' used throughout fy-NL Firefox); 'Ut' is the standard capitalized form.
- `translation_error_language_not_supported_warning_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): 'fan it [taal] út' is the idiomatic Frisian circumposition for 'from (a language)' (like Dutch 'vanuit het Engels'); language names take the article 'it' in Frisian.
- `translation_in_progress_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-05): Infinitive plus ellipsis ("Oersette…") is the standard Dutch/Frisian way to express an in-progress action.
- `ungroup_tab_group_confirmation_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): 'degroepearje' follows the regular Frisian -earje verb form (groepearje); it is the other string ('Degroeperje') that deviates, so this one is correct.
- `webcompat_reporter_label_mandatory_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The original ("so that we can investigate it") already gets the meaning across correctly, so the more literal rewording was probably seen as an unnecessary style change.
- `webcompat_reporter_reason_content2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian orthography drops the circumflex on capital U (û → U), so 'Untbrekkende' is the standard capitalized spelling.
- `wrex_widget_match_postponed` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian orthography drops accents on capital U, so 'Utsteld' is the correct capitalized form of 'útsteld'.
- `wrex_widget_match_suspended` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — auto-suggest (2026-11-06): Frisian orthography drops the circumflex on capital U, so 'Underbrutsen' is the correct capitalized form of 'ûnderbrutsen'.

_One line each in `locales/fy-NL/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `search_suggestions_onboarding_text` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (74)

- `mozac_browser_errorpages_archive_description` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_connection_failure_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_safe_harmful_uri_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_failed_to_disable` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_permissions_data_collection_technicalAndInteraction_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_permissions_dialog_technical_and_interaction_data` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_permissions_management_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_addons_permissions_management_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_downloads_open_existing_file` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_prompt_folder_upload_confirm_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `mozac_feature_readerview_font_size_increase_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `addresses_eircode` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `ai_controls_blocked_info_banner` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `bookmark_menu_open_all_in_private_tabs_button` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `bookmark_save_in_label` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `close_tab_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `confirm_clear_permission_site` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `create_collection_default_name` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `create_collection_deselect_all` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `likert_scale_option_3` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `microsurvey_homepage_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `microsurvey_prompt_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preference_enhanced_tracking_protection_allow_list_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preference_gestures_swipe_toolbar_switch_tabs_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preference_search_learn_about_fx_suggest` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preferences_show_search_suggestions` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `preferences_sync_tabs_2` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `privacy_notice_updated_homepage_message` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `protection_panel_etp_disabled_no_trackers_blocked` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
- `search_suggestions_delete_history_item_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-fy-rNL/strings.xml` — fixed 2026-11-08
