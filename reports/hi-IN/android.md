# Android l10n QA — hi-IN

| | |
|---|---|
| **Generated** | 2026-09-10 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `6bf5ed95c626` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `6bf5ed95c626` |
| **Previous run** | 2026-09-10 @ `72345b324a06` |
| **Mode** | incremental |
| **Strings reviewed this run** | 303 of 2,668 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for hi-IN: [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (22)

- `mozac_feature_prompts_identity_credentials_choose_provider` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — Misspelling of "प्रोवाइडर" as "प्रोवाइर".
    - Current: `लॉगिन प्रोवाइर चुनें`
    - Source: `Choose a login provider`
    - Suggest: `लॉगिन प्रोवाइडर चुनें`
    - "provider" is transliterated as प्रोवाइडर elsewhere (see mozac_feature_prompts_identity_credentials_privacy_policy_title); here the 'ड' is missing.
- `tab_tray_add_new_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Imperative verb form is wrong: "जोड़े" should be "जोड़ें".
    - Current: `नया कलेक्शन जोड़े`
    - Source: `Add new collection`
    - Suggest: `नया कलेक्शन जोड़ें`
    - The polite imperative of जोड़ना is जोड़ें; जोड़े is an incorrect form here, inconsistent with चुनें in the neighbouring string.
- `customize_toggle_jump_back_in` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Jump back in" (resume recent tab) rendered as "वापस जाएं" meaning "go back".
    - Current: `वापस जाएं`
    - Source: `Jump back in`
    - Suggest: `वहीं से शुरू करें`
    - The source is a home-screen section header for resuming a recent tab, not a back-navigation action; "वापस जाएं" reads as the Back command.
- `collection_open_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Open tabs" here is a verb phrase (button that opens the collection's tabs) but is translated as the noun phrase "open tabs".
    - Current: `खुले हुए टैब`
    - Source: `Open tabs`
    - Suggest: `टैब खोलें`
    - Developer comment: "Text for the button to open tabs of the selected collection" — it is an action label, not a description of already-open tabs.
- `create_collection_name_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Name collection" (imperative: give the collection a name) is rendered as "collection of names".
    - Current: `नाम का कलेक्शन`
    - Source: `Name collection`
    - Suggest: `कलेक्शन को नाम दें`
    - The source is a step title instructing the user to name the collection, matching the sibling strings "Select tabs"/"Select collection" which are imperatives. "नाम का कलेक्शन" means "the collection named/of name", not an instruction to name it.
- `create_collection_default_name` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Collection %d" is rendered with reversed word order so it reads as "%d collections" instead of the collection's name/number.
    - Current: `%d कलेक्शन`
    - Source: `Collection %d`
    - Suggest: `कलेक्शन %d`
    - The source is a default collection name where %d is an ordinal-like number appended after the word (e.g. "Collection 3"). Putting the number first makes it read as a count of collections.
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Straight double quotes used instead of the locale's curly double quotes as in the source.
    - Current: `"बाहर निकलें"`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“बाहर निकलें”`
    - Source uses curly quotes “Quit”; hi-IN convention is curly-double quotes.
- `sync_connect_device_dialog` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Double space between words in the translation.
    - Current: `एक और  डिवाइस`
    - Source: `To send a tab, sign in to Firefox on at least one other device.`
    - Suggest: `एक और डिवाइस`
    - There is an extra space in the user-visible text that is not in the source.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "will cause websites to break" is rendered as the tentative "may cause", identical to the cookies_3 string.
    - Current: `सभी कुकीज़ (इससे शायद वेबसाइटें काम न करें)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `सभी कुकीज़ (इससे वेबसाइटें काम नहीं करेंगी)`
    - The source distinguishes "may cause websites to break" (cookies_3) from the certain "will cause websites to break" (cookies_4); the translation uses "शायद" (may) in both, weakening the warning.
- `etp_cryptominers_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "mine digital currency" is mistranslated as "detect/find digital currency".
    - Current: `डिजिटल करेंसी का पता लगाने वाली`
    - Source: `Prevents malicious scripts gaining access to your device to mine digital currency.`
    - Suggest: `डिजिटल करेंसी माइन करने वाली`
    - The source says the scripts mine (generate) digital currency using your device; "का पता लगाने" means "to detect/locate", which is a different action.
- `preference_enhanced_tracking_protection_custom_cookies_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Cookies from unvisited sites" is rendered as "cookies belonging to unvisited sites" with an incorrect relational form.
    - Current: `विज़िट न की गई साइटों वाली कुकीज़`
    - Source: `Cookies from unvisited sites`
    - Suggest: `विज़िट न की गई साइटों की कुकीज़`
    - The source means cookies originating from sites you have not visited; "साइटों वाली कुकीज़" is ungrammatical/ambiguous for the source relation.
- `deleting_browsing_data_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Wrong verb agreement: plural "हैं" used with singular subject.
    - Current: `ब्राउज़िंग डेटा डिलीट किया जा रहा हैं…`
    - Source: `Deleting browsing data…`
    - Suggest: `ब्राउज़िंग डेटा डिलीट किया जा रहा है…`
    - "किया जा रहा" is singular and requires "है", not the plural "हैं".
- `etp_cookies_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Wrong verb agreement: "करता हैं" mixes singular and plural forms.
    - Current: `ब्लॉक करता हैं`
    - Source: `Blocks cookies that ad networks and analytics companies use to compile your browsing data across many sites.`
    - Suggest: `ब्लॉक करता है`
    - "करता" is singular masculine and requires "है".
- `etp_social_media_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Missing sentence-final danda; the source sentence ends with a period.
    - Current: `लगाम लगाता है`
    - Source: `Limits the ability of social networks to track your browsing activity around the web.`
    - Suggest: `लगाम लगाता है।`
    - The en-US string is a full sentence ending in a period; other ETP descriptions in this batch end with "।".
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Stray space before the colon.
    - Current: `डीबग मेन्यू : चालू`
    - Source: `Debug menu: %1$d click(s) left to enable`
    - Suggest: `डीबग मेन्यू: चालू`
    - The source has no space before the colon; a space before punctuation is not a hi-IN convention.
- `search_engine_edit` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Spelling error: stray nukta on "ए" in "ए़डिट करें".
    - Current: `ए़डिट करें`
    - Source: `Edit`
    - Suggest: `एडिट करें`
    - The word should be "एडिट करें" as used consistently in other strings (e.g. search_engine_edit_custom_search_engine_title, credit_cards_edit_card); the nukta diacritic on ए is a typo.
- `browser_toolbar_url_copied_to_clipboard_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Passive construction is incomplete: missing "गया".
    - Current: `URL क्लिपबोर्ड पर कॉपी किया`
    - Source: `URL copied to clipboard`
    - Suggest: `URL क्लिपबोर्ड पर कॉपी किया गया`
    - Source "URL copied to clipboard" is a passive statement; Hindi requires "कॉपी किया गया" — "कॉपी किया" alone is ungrammatical/incomplete.
- `logins_username_copied` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Passive construction is incomplete: missing "गया".
    - Current: `यूज़रनेम क्लिपबोर्ड पर कॉपी किया`
    - Source: `Username copied to clipboard`
    - Suggest: `यूज़रनेम क्लिपबोर्ड पर कॉपी किया गया`
    - Source "Username copied to clipboard" is passive; Hindi needs "कॉपी किया गया".
- `preferences_passwords_save_logins_ask_to_save` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Ask to save" mistranslated as "ask in order to save".
    - Current: `सेव करने के लिए पूछें`
    - Source: `Ask to save`
    - Suggest: `सेव करने से पहले पूछें`
    - The source means the browser should ask the user whether to save the password; "सेव करने के लिए पूछें" reads as "ask in order to save", reversing who asks and why.
- `no_site_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "No site exceptions" mistranslated as "no exceptions with sites".
    - Current: `साइट वाले कोई अपवाद नहीं हैं`
    - Source: `No site exceptions`
    - Suggest: `कोई साइट अपवाद नहीं`
    - The source is a label for the absence of site-specific exceptions; "साइट वाले" ("with sites") misrenders the noun phrase "site exceptions".
- `inactive_tabs_auto_close_message_header` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Question "Auto-close after one month?" rendered as an imperative command rather than a question about the setting.
    - Current: `एक महीने बाद अपने आप बंद करें?`
    - Source: `Auto-close after one month?`
    - Suggest: `एक महीने बाद अपने आप बंद हो जाएं?`
    - The source asks whether tabs should auto-close after a month; the Hindi uses the imperative "बंद करें" (you close them), changing the actor and meaning.
- `download_language_file_dialog_message_all_languages` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "partial languages" translated as "आधी-अधूरी भाषाओं" (half-baked/incomplete languages), a pejorative claim about the download.
    - Current: `कुछ आधी-अधूरी भाषाओं को`
    - Source: `We download partial languages to your cache to keep translations private.`
    - Suggest: `भाषाओं के कुछ हिस्सों को`
    - The source means parts of language files are downloaded; "आधी-अधूरी" connotes shoddy/incomplete quality, making the product describe its own language data as half-baked.

### ✅ Fixed since the last run (58)

- `mozac_browser_errorpages_httpsonly_button` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — "Continue to HTTP Site" mistranslated as "Keep the HTTP site running/continue it".
    - Current: `HTTP साइट को जारी रखें`
    - Source: `Continue to HTTP Site`
    - Suggest: `HTTP साइट पर जाएं`
    - The button loads the site over HTTP; the Hindi "HTTP साइट को जारी रखें" means "continue the HTTP site" rather than "proceed to the HTTP site".
- `mozac_browser_menu2_button` — `mozilla-mobile/android-components/components/browser/menu2/src/main/res/values-hi-rIN/strings.xml` — "Menu" is rendered as "मेन्यू बटन" (Menu button), adding a word not in the source and diverging from the identical strings elsewhere.
    - Current: `मेन्यू बटन`
    - Source: `Menu`
    - Suggest: `मेन्यू`
    - Source is just "Menu"; the parallel strings mozac_browser_menu_button and mozac_browser_toolbar_menu_button are correctly translated as "मेन्यू".
- `mozac_feature_addons_permissions_required_data_collection_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — Wrong case marker: "इन चीज़ों का इकट्ठा करता है" should be "इन चीज़ों को इकट्ठा करता है".
    - Current: `इन चीज़ों का इकट्ठा करता है`
    - Source: `The developer says this extension collects: %1$s`
    - Suggest: `इन चीज़ों को इकट्ठा करता है`
    - The postposition का does not agree with the transitive verb इकट्ठा करता है; the object requires को (or no marker).
- `mozac_feature_contextmenu_share_image` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-hi-rIN/strings.xml` — "Share image" uses "चित्र साझा करें" while sibling context-menu strings use "इमेज" and "शेयर करें".
    - Current: `चित्र साझा करें`
    - Source: `Share image`
    - Suggest: `इमेज शेयर करें`
    - The same surface (context menu) renders "image" as "इमेज" (open/save image) and "share" as "शेयर करें" (share link, share email address); this string alone switches to चित्र/साझा, breaking terminology consistency.
- `mozac_feature_downloads_could_not_open_file` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-hi-rIN/strings.xml` — Gender agreement error: "फ़ाइल" is feminine but the verb is masculine.
    - Current: `फ़ाइल खोला नहीं जा सका`
    - Source: `Could not open file`
    - Suggest: `फ़ाइल खोली नहीं जा सकी`
    - "फ़ाइल" is a feminine noun in Hindi, so the passive verb must be "खोली नहीं जा सकी".
- `mozac_feature_downloads_dialog_cancel` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-hi-rIN/strings.xml` — "Cancel" rendered as "रद्द करें" while the other Cancel buttons in the same file use "कैंसिल करें".
    - Current: `रद्द करें`
    - Source: `Cancel`
    - Suggest: `कैंसिल करें`
    - mozac_feature_downloads_button_cancel and the cancel-downloads strings in the same downloads surface use "कैंसिल"; this string is inconsistent with them.
- `mozac_feature_media_sharing_camera_and_microphone_text` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-hi-rIN/strings.xml` — Sentence ends with a Latin full stop instead of the Devanagari danda used in the sibling strings in the same file.
    - Current: `टैप करें.`
    - Source: `Tap to open the tab that’s using your microphone and camera.`
    - Suggest: `टैप करें।`
    - The adjacent media-sharing notification strings all end with '।'; this one uses '.', an inconsistent terminator on the same surface.
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — "may not be saved" is rendered as "cannot be saved" (सहेजा नहीं जा सकता है), changing possibility to impossibility.
    - Current: `आपके द्वारा दर्ज किया गया डेटा सहेजा नहीं जा सकता है`
    - Source: `Do you want to leave this site? Data you have entered may not be saved`
    - Suggest: `हो सकता है कि आपके द्वारा दर्ज किया गया डेटा सेव न हो`
    - Source says data may not be saved (possibility); the Hindi asserts the data cannot be saved.
- `mozac_feature_prompts_expand_logins_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — Typo: "सेवा किए गए" instead of "सेव किए गए" (saved).
    - Current: `'सेवा किए गए पासवर्ड' को फैलाएं`
    - Source: `Expand saved passwords`
    - Suggest: `'सेव किए गए पासवर्ड' को फैलाएं`
    - Source is "Expand saved passwords"; "सेवा" means "service", not "saved". The parallel collapse string correctly uses "सेव किए गए पासवर्ड".
- `mozac_feature_prompts_identity_credentials_choose_provider` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — Misspelling of "प्रोवाइडर" as "प्रोवाइर".
    - Current: `लॉगिन प्रोवाइर चुनें`
    - Source: `Choose a login provider`
    - Suggest: `लॉगिन प्रोवाइडर चुनें`
    - "provider" is transliterated as प्रोवाइडर elsewhere (see mozac_feature_prompts_identity_credentials_privacy_policy_title); here the 'ड' is missing.
- `mozac_summarize_info_error_code` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — "Error" is transliterated as "ऐरर" here while the same term is translated as "गड़बड़ी" in the neighbouring error strings.
    - Current: `ऐरर कोड: %1$d`
    - Source: `Error code: %1$d`
    - Suggest: `गड़बड़ी कोड: %1$d`
    - mozac_summarize_download_error_title and _fallback_message render "Error" as गड़बड़ी; the transliteration ऐरर is inconsistent on the same surface.
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The translation loses the meaning "%1$d click(s) left", saying instead "press %1$d to enable".
    - Current: `डिबग मेन्यू : %1$d सक्षम करने के लिए दबायें`
    - Source: `Debug menu: %1$d click(s) left to enable`
    - Suggest: `डिबग मेन्यू: सक्षम करने के लिए %1$d बार और दबाएँ`
    - Source says the number of remaining clicks needed to enable the debug menu; the target reads as an instruction to press the number, dropping "left".
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Stray space before the colon.
    - Current: `डीबग मेन्यू : चालू`
    - Source: `Debug menu: %1$d click(s) left to enable`
    - Suggest: `डीबग मेन्यू: चालू`
    - The source has no space before the colon; a space before punctuation is not a hi-IN convention.
- `collection_open_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Open tabs" here is a verb phrase (button that opens the collection's tabs) but is translated as the noun phrase "open tabs".
    - Current: `खुले हुए टैब`
    - Source: `Open tabs`
    - Suggest: `टैब खोलें`
    - Developer comment: "Text for the button to open tabs of the selected collection" — it is an action label, not a description of already-open tabs.
- `create_collection_save_to_collection_tabs_selected` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Plural form for multiple tabs is identical to the singular string, using singular agreement.
    - Current: `%d टैब चुना गया`
    - Source: `%d tabs selected`
    - Suggest: `%d टैब चुने गए`
    - Source is "%d tabs selected" (plural), but the target uses the singular verb form identical to create_collection_save_to_collection_tab_selected ("%d tab selected").
- `create_collection_select_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Imperative verb form misspelled: "चुने" should be "चुनें".
    - Current: `संग्रह चुने`
    - Source: `Select collection`
    - Suggest: `संग्रह चुनें`
    - "Select collection" is an imperative; Hindi requires "चुनें" (as used correctly in other strings like "सभी चुनें").
- `credit_cards_biometric_prompt_message_pin` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Unlock your device" rendered as "अपना उपकरण खोलें" (open your device) instead of unlock, and uses inconsistent term for device.
    - Current: `अपना उपकरण खोलें`
    - Source: `Unlock your device`
    - Suggest: `अपना डिवाइस अनलॉक करें`
    - The source says "Unlock your device"; "खोलें" means open, and neighbouring strings use "डिवाइस"/"अनलॉक" consistently.
- `delete_browsing_data_quit_off` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Status summary "Off" translated as an imperative command "Turn off".
    - Current: `बंद करें`
    - Source: `Off`
    - Suggest: `बंद`
    - The source is a summary showing the preference's current state (Off), not an action button; "बंद करें" means "turn off".
- `delete_browsing_data_quit_on` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Status summary "On" translated as an imperative command "Turn on".
    - Current: `चालू करें`
    - Source: `On`
    - Suggest: `चालू`
    - The source is a summary showing the preference's current state (On), not an action; "चालू करें" means "turn on".
- `enhanced_tracking_protection_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Plural "these websites" rendered as singular "this site".
    - Current: `इस साइट के लिए उन्नत ट्रैकिंग सुरक्षा बंद है`
    - Source: `Enhanced Tracking Protection is off for these websites`
    - Suggest: `इन वेबसाइटों के लिए उन्नत ट्रैकिंग सुरक्षा बंद है`
    - Source says "for these websites" (plural, header for an exceptions list); the translation says "for this site" (singular).
- `etp_cookies_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Wrong verb agreement: "करता हैं" mixes singular and plural forms.
    - Current: `ब्लॉक करता हैं`
    - Source: `Blocks cookies that ad networks and analytics companies use to compile your browsing data across many sites.`
    - Suggest: `ब्लॉक करता है`
    - "करता" is singular masculine and requires "है".
- `etp_cryptominers_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "mine digital currency" is mistranslated as "detect/find digital currency".
    - Current: `डिजिटल करेंसी का पता लगाने वाली`
    - Source: `Prevents malicious scripts gaining access to your device to mine digital currency.`
    - Suggest: `डिजिटल करेंसी माइन करने वाली`
    - The source says the scripts mine (generate) digital currency using your device; "का पता लगाने" means "to detect/locate", which is a different action.
- `etp_social_media_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "your browsing activity" rendered as reflexive "अपनी", making the social networks the possessor.
    - Current: `वेब के आसपास अपनी ब्राउज़िंग गतिविधि को ट्रैक करने के लिए सामाजिक नेटवर्क की क्षमता को सीमित करता है।`
    - Source: `Limits the ability of social networks to track your browsing activity around the web.`
    - Suggest: `वेब पर आपकी ब्राउज़िंग गतिविधि को ट्रैक करने की सामाजिक नेटवर्क की क्षमता को सीमित करता है।`
    - In Hindi "अपनी" refers back to the subject (the social networks), so the sentence says networks track their own browsing activity instead of yours.
- `etp_tracking_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Garbled clause order and wrong agreement make the sentence say the tracking code blocks external content from loading.
    - Current: `जिसमें ट्रैकिंग कोड होता है उसे बाहरी विज्ञापन, वीडियो, और अन्य सामग्री लोड करने से रोकती है। कुछ वेबसाइट की कार्यक्षमता को प्रभावित करती हैं।`
    - Source: `Stops outside ads, videos, and other content from loading that contains tracking code. May affect some website functionality.`
    - Suggest: `ट्रैकिंग कोड वाले बाहरी विज्ञापन, वीडियो और अन्य सामग्री को लोड होने से रोकता है। इससे कुछ वेबसाइटों की कार्यक्षमता प्रभावित हो सकती है।`
    - Source: "Stops outside ads, videos, and other content from loading that contains tracking code. May affect some website functionality." The relative clause is misplaced and the second sentence drops the modal "May", asserting it does affect functionality.
- `exceptions_empty_message_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Translation states exceptions disable tracking protection, dropping "let you" (allow/enable to).
    - Current: `अपवाद आपको चयनित साइटों के लिए ट्रैकिंग सुरक्षा अक्षम करते हैं।`
    - Source: `Exceptions let you disable tracking protection for selected sites.`
    - Suggest: `अपवाद आपको चयनित साइटों के लिए ट्रैकिंग सुरक्षा अक्षम करने देते हैं।`
    - Source: "Exceptions let you disable tracking protection for selected sites." The Hindi says exceptions disable protection for you, losing the permissive meaning.
- `inactive_tabs_auto_close_message_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Number agreement error: singular subject with plural verb.
    - Current: `स्वत: बंद सक्षम हैं`
    - Source: `Auto-close enabled`
    - Suggest: `स्वत: बंद सक्षम है`
    - "Auto-close enabled" is singular; "हैं" is the plural form and disagrees with the subject.
- `logins_username_copied` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Passive construction is incomplete: missing "गया".
    - Current: `यूज़रनेम क्लिपबोर्ड पर कॉपी किया`
    - Source: `Username copied to clipboard`
    - Suggest: `यूज़रनेम क्लिपबोर्ड पर कॉपी किया गया`
    - Source "Username copied to clipboard" is passive; Hindi needs "कॉपी किया गया".
- `notification_pbm_delete_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "private tabs" rendered as "निजी टैब" here but "प्राइवेट टैब" in the parallel Android 14 string.
    - Current: `निजी टैब बंद करें`
    - Source: `Close private tabs`
    - Suggest: `प्राइवेट टैब बंद करें`
    - notification_erase_title_android_14 translates the same "private tabs" as "प्राइवेट टैब"; the same notification surface should use one term.
- `phone_feature_blocked_step_feature` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Instruction reworded so the ON target is lost: reads "toggle %1$s in order to turn on".
    - Current: `3. चालू करने के लिए { <b> }%1$s{ </b> } टॉगल करें`
    - Source: `3. Toggle { <b> }%1$s{ </b> } to ON`
    - Suggest: `3. { <b> }%1$s{ </b> } को चालू (ON) पर टॉगल करें`
    - Source is "Toggle %1$s to ON", i.e. set the named permission toggle to ON; the Hindi inverts it into "in order to turn on, toggle %1$s".
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Second sentence mistranslated: "Disable to manage font size here" became "unable to manage font size here".
    - Current: `यहां फ़ॉन्ट आकार प्रबंधित करने में अक्षम।`
    - Source: `Font size will match your Android settings. Disable to manage font size here.`
    - Suggest: `यहां फ़ॉन्ट आकार प्रबंधित करने के लिए इसे बंद करें।`
    - The source instructs the user to disable the setting in order to manage font size here; the Hindi states the app is unable to manage font size here, reversing the instruction.
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Gender/case agreement error: "आपका Android सेटिंग्स" should be "आपकी Android सेटिंग्स".
    - Current: `फ़ॉन्ट आकार आपका Android सेटिंग्स से मेल खाएगा`
    - Source: `Font size will match your Android settings. Disable to manage font size here.`
    - Suggest: `फ़ॉन्ट आकार आपकी Android सेटिंग्स से मेल खाएगा`
    - "सेटिंग्स" is feminine and requires "आपकी"; also the postposition requires the oblique form.
- `preference_enhanced_tracking_protection_custom_cookies_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Ungrammatical rendering of "Cookies from unvisited sites".
    - Current: `नहीं देखे साइट से कुकीज़`
    - Source: `Cookies from unvisited sites`
    - Suggest: `बिना देखी गई साइटों की कुकीज़`
    - "नहीं देखे साइट से" lacks agreement and a proper participle construction in Hindi.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Ungrammatical parenthetical: "(वेबसाइटों को तोड़ने के कारण होंगे)".
    - Current: `सभी कुकीज़ (वेबसाइटों को तोड़ने के कारण होंगे)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `सभी कुकीज़ (इससे वेबसाइटें काम करना बंद कर देंगी)`
    - The phrase is not grammatical Hindi and garbles "will cause websites to break".
- `preference_enhanced_tracking_protection_custom_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Imperative misspelled ("चुने" instead of "चुनें") and wrong agreement in "करना हैं".
    - Current: `चुने, कौन से ट्रैकर्स और स्क्रिप्ट को ब्लॉक करना हैं।`
    - Source: `Choose which trackers and scripts to block.`
    - Suggest: `चुनें कि कौन से ट्रैकर और स्क्रिप्ट ब्लॉक करने हैं।`
    - "चुने" is the wrong form for the polite imperative and "करना हैं" mixes singular verb with plural auxiliary.
- `preference_experiments_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Translation says "allows installing Mozilla and running studies" instead of allowing Mozilla to install and run studies.
    - Current: `Mozilla को संस्थापित करने और अध्ययन चलाने की अनुमति देता है`
    - Source: `Allows Mozilla to install and run studies`
    - Suggest: `Mozilla को अध्ययन संस्थापित करने और चलाने की अनुमति देता है`
    - In the source, Mozilla is the agent that installs and runs studies; the Hindi reads as though Mozilla itself is being installed.
- `preferences_delete_browsing_data_browsing_data_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Plural "%d addresses" rendered in singular form.
    - Current: `%d पता`
    - Source: `%d addresses`
    - Suggest: `%d पते`
    - The source is plural; Hindi should use the plural noun form 'पते'.
- `preferences_delete_browsing_data_cached_files` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Translation of "Cached images and files" is ungrammatical and misordered with wrong agreement.
    - Current: `चित्र और फाइलें सहेजा गया`
    - Source: `Cached images and files`
    - Suggest: `कैश किए गए चित्र और फ़ाइलें`
    - The source is a noun phrase 'cached images and files'; the target reads 'images and files was saved' with wrong gender/number agreement.
- `preferences_delete_browsing_data_cached_files_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Descriptive statement "Frees up storage space" rendered as an imperative.
    - Current: `संग्रहण जगह को खाली करें`
    - Source: `Frees up storage space`
    - Suggest: `संग्रहण जगह खाली करता है`
    - Source describes what deleting does, not a command to the user.
- `preferences_delete_browsing_data_on_quit` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "on quit" mistranslated as "निकासी पर" (on withdrawal/exit of money).
    - Current: `निकासी पर ब्राउज़िंग डेटा हटाएँ`
    - Source: `Delete browsing data on quit`
    - Suggest: `बाहर निकलने पर ब्राउज़िंग डेटा हटाएँ`
    - 'निकासी' means withdrawal/drainage, not quitting the app; it does not convey 'on quit'.
- `preferences_opening_screen` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Opening screen" (the screen shown when the app opens) is rendered as "when the screen opens".
    - Current: `स्क्रीन खुलने पर`
    - Source: `Opening screen`
    - Suggest: `शुरुआती स्क्रीन`
    - The developer comment says this is the title of a preference for choosing what screen to show after opening the app; "स्क्रीन खुलने पर" means "upon the screen opening", which reverses the noun phrase.
- `preferences_sync_remove_account` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Misspelled verb form "मिटायें" and wrong verb for "remove account".
    - Current: `खाता मिटायें`
    - Source: `Remove account`
    - Suggest: `खाता हटाएं`
    - "Remove account" should be हटाएं (remove), and the standard spelling is हटाएं/मिटाएं, not मिटायें; also inconsistent with the -एं endings used elsewhere in this batch.
- `qr_scanner_dialog_invalid` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Latin full stop used instead of the Devanagari danda used elsewhere in the file.
    - Current: `वेब पता वैध नहीं है.`
    - Source: `Web address not valid.`
    - Suggest: `वेब पता वैध नहीं है।`
    - Surrounding Hindi strings consistently end sentences with "।"; this one uses ".".
- `saved_login_copy_username` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Verb form is wrong: "कॉपी करे" instead of the imperative "कॉपी करें".
    - Current: `उपयोगकर्ता नाम कॉपी करे`
    - Source: `Copy username`
    - Suggest: `उपयोगकर्ता नाम कॉपी करें`
    - Source "Copy username" is an imperative label; Hindi requires "करें", and "करे" is an ungrammatical subjunctive form inconsistent with the other button descriptions in this batch.
- `saved_login_duplicate` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The translation drops "already" and reads "A login with this username exists", losing the duplicate-error meaning.
    - Current: `एक लॉगिन इस उपयोगकर्ता नाम के साथ मौजूद है`
    - Source: `A login with that username already exists`
    - Suggest: `इस उपयोगकर्ता नाम वाला लॉगिन पहले से मौजूद है`
    - Source is "A login with that username already exists"; "पहले से" (already) is missing.
- `search_add_custom_engine_search_string_example` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Replace query with “%s”" is translated using "प्रश्न" (question) and with a grammatically wrong verb form.
    - Current: `“%s” से प्रश्न बदले।`
    - Source: `Replace query with “%s”. Example: https://www.google.com/search?q=%s`
    - Suggest: `क्वेरी को “%s” से बदलें।`
    - "query" here is the search query parameter, not a "question"; also "बदले" should be the imperative "बदलें".
- `share_device_subheader` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Wrong case marker: "उपकरण को भेजें" means "send the device" rather than "send to device".
    - Current: `उपकरण को भेजें`
    - Source: `Send to device`
    - Suggest: `उपकरण पर भेजें`
    - Source "Send to device" means sending a link to a device; "उपकरण को भेजें" reads as sending the device itself.
- `tab_crash_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Number agreement error: singular verb form with plural auxiliary "हैं".
    - Current: `उस पृष्ठ को लोड नहीं कर सकता हैं।`
    - Source: `Sorry. %1$s can’t load that page.`
    - Suggest: `उस पृष्ठ को लोड नहीं कर सकता है।`
    - The subject is a single app name (%1$s), so the auxiliary must be singular "है", not plural "हैं".
- `tabs_menu_save_to_collection1` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "collection" rendered as "संग्रहण" (storage) instead of "संग्रह" used elsewhere for collection.
    - Current: `संग्रहण में टैब सहेजें`
    - Source: `Save tabs to collection`
    - Suggest: `टैब संग्रह में सहेजें`
    - The sibling string tab_tray_select_collection uses "संग्रह" for "collection"; "संग्रहण" means storage/collecting, an inconsistent and incorrect term on the same surface.
- `mozac_feature_prompts_identity_credentials_choose_provider` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — Misspelling of "प्रोवाइडर" as "प्रोवाइर".
    - Current: `लॉगिन प्रोवाइर चुनें`
    - Source: `Choose a login provider`
    - Suggest: `लॉगिन प्रोवाइडर चुनें`
    - "provider" is transliterated as प्रोवाइडर elsewhere (see mozac_feature_prompts_identity_credentials_privacy_policy_title); here the 'ड' is missing.
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Stray space before the colon.
    - Current: `डीबग मेन्यू : चालू`
    - Source: `Debug menu: %1$d click(s) left to enable`
    - Suggest: `डीबग मेन्यू: चालू`
    - The source has no space before the colon; a space before punctuation is not a hi-IN convention.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Curly typographic quotes in the source were replaced with straight ASCII quotes.
    - Current: `"https://" या "http://"`
    - Source: `Web address must contain “https://” or “http://”`
    - Suggest: `“https://” या “http://”`
    - The en-US string uses “ ” curly quotes around the URL schemes; the localization uses straight double quotes.
- `collection_open_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Open tabs" here is a verb phrase (button that opens the collection's tabs) but is translated as the noun phrase "open tabs".
    - Current: `खुले हुए टैब`
    - Source: `Open tabs`
    - Suggest: `टैब खोलें`
    - Developer comment: "Text for the button to open tabs of the selected collection" — it is an action label, not a description of already-open tabs.
- `create_collection_select_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Imperative verb form misspelled: "चुने" should be "चुनें".
    - Current: `टैब चुने`
    - Source: `Select Tabs`
    - Suggest: `टैब चुनें`
    - "Select Tabs" is an imperative; Hindi requires "चुनें", consistent with "सहेजने के लिए टैब चुनें".
- `download_language_file_dialog_message_all_languages` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "partial languages" translated as "आधी-अधूरी भाषाओं" (half-baked/incomplete languages), a pejorative claim about the download.
    - Current: `कुछ आधी-अधूरी भाषाओं को`
    - Source: `We download partial languages to your cache to keep translations private.`
    - Suggest: `भाषाओं के कुछ हिस्सों को`
    - The source means parts of language files are downloaded; "आधी-अधूरी" connotes shoddy/incomplete quality, making the product describe its own language data as half-baked.
- `etp_cookies_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Wrong verb agreement: "करता हैं" mixes singular and plural forms.
    - Current: `ब्लॉक करता हैं`
    - Source: `Blocks cookies that ad networks and analytics companies use to compile your browsing data across many sites.`
    - Suggest: `ब्लॉक करता है`
    - "करता" is singular masculine and requires "है".
- `etp_cryptominers_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "mine digital currency" is mistranslated as "detect/find digital currency".
    - Current: `डिजिटल करेंसी का पता लगाने वाली`
    - Source: `Prevents malicious scripts gaining access to your device to mine digital currency.`
    - Suggest: `डिजिटल करेंसी माइन करने वाली`
    - The source says the scripts mine (generate) digital currency using your device; "का पता लगाने" means "to detect/locate", which is a different action.
- `logins_username_copied` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Passive construction is incomplete: missing "गया".
    - Current: `यूज़रनेम क्लिपबोर्ड पर कॉपी किया`
    - Source: `Username copied to clipboard`
    - Suggest: `यूज़रनेम क्लिपबोर्ड पर कॉपी किया गया`
    - Source "Username copied to clipboard" is passive; Hindi needs "कॉपी किया गया".
- `tab_tray_close_tabs_banner_negative_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Button label "Dismiss" translated as a bare adjective/stem instead of a verb phrase.
    - Current: `खारिज`
    - Source: `Dismiss`
    - Suggest: `खारिज करें`
    - "खारिज" alone is not a grammatical action label in Hindi; other buttons in this batch use the verb form (e.g. "बंद करें", "विकल्प देखें").

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
| Strings | 2,668 |
| Missing strings | 81 |
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
| Typography deviations from this locale's own norm | 2 |

### Completeness

**81 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — 79
- `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — 1
- `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 10, `straight-double` 2 | **curly-double** |
| apostrophe | `typographic` 1, `straight` 4 | **straight** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (179)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "additional data collection" is rendered as "collect even more data", changing the meaning.
    - Current: `%1$s और भी डेटा को इकट्ठा करने का अनुरोध करता है`
    - Source: `%1$s requests additional data collection`
    - Suggest: `%1$s अतिरिक्त डेटा संग्रह का अनुरोध करता है`
    - The source asks for additional (optional) data collection permissions; the hi-IN wording "और भी डेटा" asserts the extension wants to collect even more data, a different claim than the neutral source.
- `likert_scale_option_slow_or_buggy` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "It’s slow or buggy" translated as "It is very slow and has some bugs", changing "or" to "and" and adding intensifiers.
    - Current: `बहुत धीमा है और इसमें कुछ बग हैं`
    - Source: `It’s slow or buggy`
    - Suggest: `यह धीमा है या इसमें बग हैं`
    - The source is a disjunction without "very" or "some"; the translation asserts both slowness and the presence of bugs about the product.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Translation adds a claim that the data is never sold, which the source does not contain, and mistranslates "that you use it" as "how you use it".
    - Current: `आपने Firefox के बारे में कैसे जाना और आप इसका इस्तेमाल कैसे करते हैं, यह जानकारी Mozilla के मार्केटिंग टेक्नोलॉजी पार्टनर्स के साथ शेयर करें। इस डेटा को कभी बेचा नहीं जाता है।`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `आपने Firefox के बारे में कैसे जाना और आप इसका इस्तेमाल करते हैं, यह जानकारी Mozilla के मार्केटिंग टेक्नोलॉजी पार्टनर्स के साथ शेयर करें।`
    - The source only says to share how you discovered Firefox and that you use it; the added sentence "इस डेटा को कभी बेचा नहीं जाता है।" (this data is never sold) is not in the source, and the developer comment explicitly warns that "that you use it" must not imply tracking of how it is used.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 74 |
| 3 | Degraded language (grammar, spelling, terminology) | 90 |
| 4 | Cosmetic (typography, spacing) | 15 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_invalid_content_encoding_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Negation dropped: "invalid ... form of compression" is rendered as "a compression method that is correct".
    - Current: `इसमें कम्प्रेशन का ऐसा तरीका इस्तेमाल किया गया है जो सही है या जिसे सपोर्ट हासिल नहीं है`
    - Source: `{ <p> }The page you are trying to view cannot be shown because it uses an invalid or unsupported form of compression.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } {…`
    - Suggest: `इसमें कम्प्रेशन का ऐसा तरीका इस्तेमाल किया गया है जो सही नहीं है या जिसे सपोर्ट हासिल नहीं है`
    - Source says the page uses an invalid or unsupported form of compression; the Hindi says the compression method "is correct", reversing the meaning.
- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — The instruction "Press 'Try Again' to switch to online mode and reload the page" is rendered as two alternatives ("press Try Again or reload the page"), changing the meaning.
    - Current: `ऑनलाइन मोड में जाने के लिए “फिर से कोशिश करें” दबाएं या पेज को फिर से लोड करें।`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `ऑनलाइन मोड में जाने और पेज को फिर से लोड करने के लिए “फिर से कोशिश करें” दबाएं।`
    - The source is a single action with two results; the Hindi uses "या" (or), presenting reloading as an alternative action.
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — "Does the proxy service allow connections from this network?" is mistranslated as allowing "some connection with this network".
    - Current: `क्या प्रॉक्सी सेवा इस नेटवर्क वाले किसी कनेक्शन को अनुमति देती है?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy refused a connection.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Does…`
    - Suggest: `क्या प्रॉक्सी सेवा इस नेटवर्क से आने वाले कनेक्शन की अनुमति देती है?`
    - Source asks whether the proxy permits connections originating from this network; the Hindi phrase "इस नेटवर्क वाले किसी कनेक्शन" distorts that.
- `mozac_browser_errorpages_security_bad_cert_back` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — "(Recommended)" rendered as "(सलाह)" meaning "(advice)" rather than "recommended".
    - Current: `पीछे जाएं (सलाह)`
    - Source: `Go Back (Recommended)`
    - Suggest: `पीछे जाएं (सुझाया गया)`
    - The source marks this option as the recommended one; "सलाह" simply means "advice" and does not convey "recommended".
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — "Check the site for extra requirements" is mistranslated as "go to the site for extra requirements".
    - Current: `अतिरिक्त शर्तों के लिए साइट पर जाएं।`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `अतिरिक्त ज़रूरतों के लिए साइट देखें।`
    - The source tells the user to check the site for additional requirements, not to visit it.
- `mozac_feature_addons_failed_to_uninstall` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "Failed to uninstall" is translated as "could not be installed", reversing the action.
    - Current: `%1$s इंस्टॉल नहीं किया जा सका`
    - Source: `Failed to uninstall %1$s`
    - Suggest: `%1$s अनइंस्टॉल नहीं किया जा सका`
    - Source says uninstall failed; the Hindi says install failed, which is the opposite operation and duplicates mozac_feature_addons_failed_to_install.
- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "additional data collection" is rendered as "collect even more data", changing the meaning.
    - Current: `%1$s और भी डेटा को इकट्ठा करने का अनुरोध करता है`
    - Source: `%1$s requests additional data collection`
    - Suggest: `%1$s अतिरिक्त डेटा संग्रह का अनुरोध करता है`
    - The source asks for additional (optional) data collection permissions; the hi-IN wording "और भी डेटा" asserts the extension wants to collect even more data, a different claim than the neutral source.
- `mozac_feature_addons_permissions_notifications_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "to you" is dropped, unlike the parallel _for_update string which keeps "आपको".
    - Current: `नोटिफ़िकेशन दिखाएं`
    - Source: `Display notifications to you`
    - Suggest: `आपको नोटिफ़िकेशन दिखाएं`
    - Source is "Display notifications to you"; the recipient is omitted here while the identical _for_update string translates it as "आपको नोटिफ़िकेशन दिखाएं", making the two inconsistent.
- `mozac_feature_addons_status_incompatible` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — The translation says the add-on "does not work" instead of "is not compatible with", losing the compatibility meaning.
    - Current: `%1$s आपके %2$s के वर्ज़न (वर्ज़न %3$s) के साथ काम नहीं करता है।`
    - Source: `%1$s is not compatible with your version of %2$s (version %3$s).`
    - Suggest: `%1$s आपके %2$s के वर्ज़न (वर्ज़न %3$s) के साथ संगत नहीं है।`
    - Source states incompatibility with the app version; "काम नहीं करता है" is a weaker/different claim.
- `mozac_feature_applinks_firefox_url` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-hi-rIN/strings.xml` — Label "URL if opening in %s" is rendered as a conditional clause instead of a field label.
    - Current: `अगर URL को %s में खोला जा रहा है`
    - Source: `URL if opening in %s`
    - Suggest: `%s में खोलने पर URL`
    - The source is a details-section label naming the URL used when opening in the browser; the Hindi reads as an incomplete 'if' sentence and loses the label meaning.
- `mozac_feature_applinks_link_from` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-hi-rIN/strings.xml` — "Link from %s" (origin domain) translated as "link that has %s".
    - Current: `%s वाला लिंक`
    - Source: `Link from %s`
    - Suggest: `%s से आया लिंक`
    - Per the developer comment %s is the domain the link was navigated from; 'वाला लिंक' conveys possession/containment, not origin.
- `mozac_feature_relay_email_masks_cfr` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — "New!" rendered as "नया अपडेट!" (New update!), adding a claim not in the source.
    - Current: `नया अपडेट!`
    - Source: `New! %s email masks are now available on mobile.`
    - Suggest: `नया!`
    - The source says only "New!"; the translation asserts there is a new update.
- `search_widget_content_description` — `mozilla-mobile/android-components/components/feature/search/src/main/res/values-hi-rIN/strings.xml` — Translation says "Open a new tab in %1$s" instead of "Open a new %1$s tab"; minor but the postposition changes meaning slightly.
    - Current: `%1$s में एक नया टैब खोलें`
    - Source: `Open a new %1$s tab`
    - Suggest: `%1$s का एक नया टैब खोलें`
    - Source describes opening a new app-branded tab; the target's locative reading is different, though intelligible.
- `mozac_summarize_download_consent_button_positive` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — "Download to summarize" rendered as "download to view the summary" instead of "to create/make a summary".
    - Current: `सारांश देखने के लिए डाउनलोड करें`
    - Source: `Download to summarize`
    - Suggest: `सारांश बनाने के लिए डाउनलोड करें`
    - The source means downloading the model in order to summarize; "देखने" (to view) changes the action and is inconsistent with mozac_summarize_fxa_sign_in_title which uses "सारांश बनाने के लिए".
- `my_longest_fox_is` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-hi-rIN/strings.xml` — "My longest fox is %1$d" is rendered as "My high score is %1$d", losing the game-specific "longest fox" wording.
    - Current: `मेरा हाई-स्कोर %1$d है!`
    - Source: `My longest fox is %1$d! #longfox %2$s`
    - Suggest: `मेरी सबसे लंबी फ़ॉक्स %1$d है!`
    - The developer comment explains the shared text refers to the longest fox achievement (example: "My longest fox is 6! #longfox"); the target substitutes a generic "high score" phrase.
- `addons_permissions_heading_optional_data_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Section heading turned into a sentence claim instead of the label "Optional data collection:".
    - Current: `यह डेटा इकट्ठा करना वैकल्पिक है:`
    - Source: `Optional data collection:`
    - Suggest: `वैकल्पिक डेटा संग्रह:`
    - The source is a noun-phrase heading introducing a list; the Hindi reads "This data collection is optional:", asserting something about specific data rather than labelling the section, and it is inconsistent with the parallel headings for permissions.
- `addons_permissions_heading_required_data_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Section heading turned into a sentence claim instead of the label "Required data collection:".
    - Current: `यह डेटा इकट्ठा करना ज़रूरी है:`
    - Source: `Required data collection:`
    - Suggest: `ज़रूरी डेटा संग्रह:`
    - The source is a noun-phrase heading introducing a list; the Hindi reads "This data collection is required:", inconsistent with the parallel "ज़रूरी अनुमतियां:" heading.
- `addresses_post_town` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Post town" rendered as "पोस्ट सिटी" (post city), an invented term.
    - Current: `पोस्ट सिटी`
    - Source: `Post town`
    - Suggest: `पोस्ट टाउन`
    - The developer comment identifies this as the UK/Norway/Sweden "Post town" address field; "सिटी" (city) is a different word and this field is elsewhere distinct from city.
- `addresses_village_township` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Township" translated as "शहर" (city).
    - Current: `गांव या शहर`
    - Source: `Village or Township`
    - Suggest: `गांव या कस्बा`
    - en-US "Village or Township"; "शहर" means city, not township. The comment notes this field is crucial for rural addresses.
- `ai_controls_banner_supporting_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The sentence structure reverses the meaning: source says the choice includes whether to use AI-enhanced features, target says "this is also included in it".
    - Current: `AI से बेहतर किए गए फ़ीचर्स का इस्तेमाल करना है या नहीं, इसमें यह भी शामिल है।`
    - Source: `That includes whether to use features enhanced with AI. %s`
    - Suggest: `इसमें यह भी शामिल है कि AI से बेहतर किए गए फ़ीचर्स का इस्तेमाल करना है या नहीं।`
    - en-US: "That includes whether to use features enhanced with AI." The subject of "includes" is the choice; the Hindi inverts subject and object, saying the choice is included in the AI features.
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "translate sites in this language" mistranslated as "translate sites into this language".
    - Current: `साइटों का इस भाषा में अनुवाद करने की पेशकश नहीं करेगा`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `इस भाषा की साइटों का अनुवाद करने की पेशकश नहीं करेगा`
    - Source means sites written in this language, i.e., the source language; the Hindi says translating sites into this language (target language), reversing the direction.
- `automatic_translation_option_offer_to_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "translate sites in this language" mistranslated as "translate sites into this language".
    - Current: `साइटों का इस भाषा में अनुवाद करने की पेशकश करेगा`
    - Source: `%1$s will offer to translate sites in this language.`
    - Suggest: `इस भाषा की साइटों का अनुवाद करने की पेशकश करेगा`
    - Source refers to sites in this language (source language) being offered for translation; the Hindi reverses the direction to translating into this language.
- `beta_feature` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "BETA" was transliterated although the developer comment says it must not be translated.
    - Current: `बीटा`
    - Source: `BETA`
    - Suggest: `BETA`
    - Developer comment: "here 'Beta' should not be translated, as it is used as an icon styled element."
- `bookmark_import_failure_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Try again." is rendered as "try again later", adding a time qualifier the source does not have.
    - Current: `बाद में फिर से कोशिश करें।`
    - Source: `Couldn’t import bookmarks. Try again.`
    - Suggest: `फिर से कोशिश करें।`
    - The en-US source is "Try again." with no "later"; "बाद में" adds meaning not present in the source.
- `certificate_warning_push_notification_pnr1_message` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Adds "अन्य" (other) not present in source.
    - Current: `ऐड-ऑन और कुछ अन्य फ़ीचर`
    - Source: `Add-ons and some features will stop working on March 14.`
    - Suggest: `ऐड-ऑन और कुछ फ़ीचर`
    - Source is "Add-ons and some features", not "some other features".
- `change_file_extension_confirm_button` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Yes, change it" translated as just "Yes", dropping the action.
    - Current: `जी हां`
    - Source: `Yes, change it`
    - Suggest: `हां, इसे बदलें`
    - The source confirm button states the action ("change it"); the target only says "Yes".
- `collections_migration_homepage_banner_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Collections are now groups" rendered as "Collections are now part of groups".
    - Current: `कलेक्शन अब ग्रुप्स का हिस्सा हैं`
    - Source: `Collections are now groups`
    - Suggest: `कलेक्शन अब ग्रुप बन गए हैं`
    - The source states collections have become groups, not that they are a part of groups.
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "as specified in Regulation" mistranslated as "according to the information given in Regulation".
    - Current: `में दी गई जानकारी के अनुसार, योग्य है।`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `में निर्दिष्ट के अनुसार योग्य है।`
    - The source says the certificate is qualified as specified in the Regulation; "जानकारी" (information) is not in the source and the added comma breaks the sentence.
- `create_collection_default_name` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Collection %d" is rendered with reversed word order so it reads as "%d collections" instead of the collection's name/number.
    - Current: `%d कलेक्शन`
    - Source: `Collection %d`
    - Suggest: `कलेक्शन %d`
    - The source is a default collection name where %d is an ordinal-like number appended after the word (e.g. "Collection 3"). Putting the number first makes it read as a count of collections.
- `create_collection_name_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Name collection" (imperative: give the collection a name) is rendered as "collection of names".
    - Current: `नाम का कलेक्शन`
    - Source: `Name collection`
    - Suggest: `कलेक्शन को नाम दें`
    - The source is a step title instructing the user to name the collection, matching the sibling strings "Select tabs"/"Select collection" which are imperatives. "नाम का कलेक्शन" means "the collection named/of name", not an instruction to name it.
- `customize_toggle_jump_back_in` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Jump back in" (resume recent tab) rendered as "वापस जाएं" meaning "go back".
    - Current: `वापस जाएं`
    - Source: `Jump back in`
    - Suggest: `वहीं से शुरू करें`
    - The source is a home-screen section header for resuming a recent tab, not a back-navigation action; "वापस जाएं" reads as the Back command.
- `debug_drawer_tab_tools_tab_quantity_non_digits_error` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Error message reworded and no longer states that only positive integers are allowed.
    - Current: `कृपया नंबर दर्ज करें (डेसिमल या नेगेटिव में न हों)`
    - Source: `Please enter positive integers only`
    - Suggest: `कृपया केवल धनात्मक पूर्णांक दर्ज करें`
    - Source says "Please enter positive integers only"; the target instead says "enter a number (not decimal or negative)", adding content the source does not have.
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "If you delete all languages" is translated as "if you delete this language", duplicating the single-language dialog message.
    - Current: `अगर आप यह भाषा डिलीट करते हैं`
    - Source: `If you delete all languages, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `अगर आप सभी भाषाएं डिलीट करते हैं`
    - Source says "If you delete all languages"; the target says "this language", which is the wording of delete_language_file_dialog_message.
- `download_in_progress_snackbar_action_details` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Button label "Details" translated as "ज़्यादा जानकारी" (more information).
    - Current: `ज़्यादा जानकारी`
    - Source: `Details`
    - Suggest: `जानकारी`
    - Source is simply "Details"; the added "ज़्यादा" (more) is not in the source and lengthens a snackbar action label.
- `download_languages_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "complete languages" mistranslated as "सभी भाषाएं" (all languages).
    - Current: `सभी भाषाएं डाउनलोड करें`
    - Source: `Download complete languages for faster translations and to translate offline. %1$s`
    - Suggest: `पूरी भाषाएं डाउनलोड करें`
    - The source instructs downloading complete (full) language packages, not all languages; "सभी भाषाएं" is the wording used for the separate "All languages" string.
- `fxa_tabs_closed_notification_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "%1$s tabs closed" is rendered as "tabs closed by %1$s", attributing the closure to the app rather than counting closed tabs in the app.
    - Current: `%1$s के बंद किए गए टैब: %2$d`
    - Source: `%1$s tabs closed: %2$d`
    - Suggest: `%1$s में बंद किए गए टैब: %2$d`
    - Per the comment, %1$s is the app name and %2$d the number of tabs the user closed from another device; the possessive "के बंद किए गए" wrongly says the app closed them.
- `glean_debug_tools_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The product name "Glean" has been transliterated instead of kept as-is.
    - Current: `ग्लीन डीबग टूल्स`
    - Source: `Glean Debug Tools`
    - Suggest: `Glean डीबग टूल्स`
    - Glean is a Mozilla product/library name and should not be translated or transliterated, consistent with other brand names such as Firefox and Google kept in Latin script in this file.
- `inactive_tabs_auto_close_message_header` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Question "Auto-close after one month?" rendered as an imperative command rather than a question about the setting.
    - Current: `एक महीने बाद अपने आप बंद करें?`
    - Source: `Auto-close after one month?`
    - Suggest: `एक महीने बाद अपने आप बंद हो जाएं?`
    - The source asks whether tabs should auto-close after a month; the Hindi uses the imperative "बंद करें" (you close them), changing the actor and meaning.
- `ip_protection_location_selection_reset_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Past-tense statement that the app already switched location is rendered as an imperative telling the user to switch.
    - Current: `सुझाई गई लोकेशन पर स्विच करें।`
    - Source: `Selected VPN location unavailable. Switched to the recommended location.`
    - Suggest: `सुझाई गई लोकेशन पर स्विच कर दिया गया है।`
    - Source "Switched to the recommended location." reports a completed action by the app; the Hindi imperative "स्विच करें" instructs the user to do it.
- `ip_protection_location_unavailable_recommended_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Connected to the recommended location." is rendered as an imperative asking the user to connect.
    - Current: `सुझाई गई लोकेशन से कनेक्ट करें।`
    - Source: `Selected VPN location unavailable. Connected to the recommended location.`
    - Suggest: `सुझाई गई लोकेशन से कनेक्ट कर दिया गया है।`
    - The source states that the app has already connected to the recommended location; the Hindi imperative tells the user to connect instead.
- `likert_scale_option_6` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Present tense "I don't use it" rendered as past/perfect "I have not used it".
    - Current: `मैंने इसका इस्तेमाल नहीं किया है`
    - Source: `I don’t use it`
    - Suggest: `मैं इसका इस्तेमाल नहीं करता/करती`
    - Source is present habitual ("I don’t use it"), not past perfect ("I haven't used it").
- `likert_scale_option_7` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Present tense "I don't use search on Firefox" rendered as past "I have not used search on Firefox".
    - Current: `मैंने Firefox पर सर्च का इस्तेमाल नहीं किया है`
    - Source: `I don’t use search on Firefox`
    - Suggest: `मैं Firefox पर सर्च का इस्तेमाल नहीं करता/करती`
    - Source is present habitual, not perfect/past.
- `likert_scale_option_8` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Present tense "I don't use sync" rendered as past "I have not used sync".
    - Current: `मैंने सिंक का इस्तेमाल नहीं किया है`
    - Source: `I don’t use sync`
    - Suggest: `मैं सिंक का इस्तेमाल नहीं करता/करती`
    - Source is present habitual, not perfect/past.
- `likert_scale_option_confusing_or_hard_to_use` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The source's "or" is rendered as "and", changing the meaning of the survey option.
    - Current: `यह उलझन-भरा है और इस्तेमाल करने में मुश्किल है`
    - Source: `It’s confusing or hard to use`
    - Suggest: `यह उलझन-भरा है या इस्तेमाल करने में मुश्किल है`
    - en-US is "It’s confusing or hard to use" — a disjunction, not a conjunction.
- `likert_scale_option_slow_or_buggy` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "It’s slow or buggy" translated as "It is very slow and has some bugs", changing "or" to "and" and adding intensifiers.
    - Current: `बहुत धीमा है और इसमें कुछ बग हैं`
    - Source: `It’s slow or buggy`
    - Suggest: `यह धीमा है या इसमें बग हैं`
    - The source is a disjunction without "very" or "some"; the translation asserts both slowness and the presence of bugs about the product.
- `micro_survey_prompt_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "It only takes a minute" translated as "एक सेकंड" (a second) instead of "एक मिनट".
    - Current: `इसमें बस एक सेकंड लगेगा।`
    - Source: `Help us make Firefox better. It only takes a minute.`
    - Suggest: `इसमें बस एक मिनट लगेगा।`
    - Source says "a minute"; the translation says "a second".
- `microsurvey_prompt_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "It only takes a minute" translated as "एक सेकंड" (a second).
    - Current: `इसमें बस एक सेकंड लगेगा`
    - Source: `Help make search in Firefox better. It only takes a minute`
    - Suggest: `इसमें बस एक मिनट लगेगा`
    - Source says "a minute", not "a sec" as in the printing variant; the numeric unit is wrong.
- `microsurvey_prompt_sync_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "It only takes a minute" translated as "एक सेकंड" (a second).
    - Current: `इसमें बस एक सेकंड लगेगा`
    - Source: `Help make sync in Firefox better. It only takes a minute`
    - Suggest: `इसमें बस एक मिनट लगेगा`
    - Source says "a minute"; the translation says "a second".
- `no_site_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "No site exceptions" mistranslated as "no exceptions with sites".
    - Current: `साइट वाले कोई अपवाद नहीं हैं`
    - Source: `No site exceptions`
    - Suggest: `कोई साइट अपवाद नहीं`
    - The source is a label for the absence of site-specific exceptions; "साइट वाले" ("with sites") misrenders the noun phrase "site exceptions".
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Added phrase "अपने इस लक्ष्य में" ("in this goal of yours") not present in the source.
    - Current: `अपने इस लक्ष्य में Firefox को जीतने में मदद करने के लिए, अनुमति देने पर विचार करें।`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Firefox को जीतने में मदद करने के लिए अनुमति देने पर विचार करें।`
    - The source is simply "Please consider allowing to help Firefox win."; the translation invents a reference to the user's own goal.
- `nova_onboarding_set_to_default_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "spying on your clicks" is rendered as "spying on you", dropping the specific object.
    - Current: `कंपनियों को आपकी जासूसी करने से ऑटोमैटिक तौर पर ब्लॉक करते हैं`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `कंपनियों को आपके क्लिक की जासूसी करने से ऑटोमैटिक तौर पर ब्लॉक करते हैं`
    - The source says companies are blocked from spying on your clicks; the translation broadens it to spying on the user generally.
- `open_tabs_menu` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Open tabs menu" (menu of open tabs) rendered as an imperative "open the tab menu", dropping "open tabs".
    - Current: `टैब मेन्यू खोलें`
    - Source: `Open tabs menu`
    - Suggest: `खुले हुए टैब का मेन्यू`
    - The developer comment says the control opens the menu for open tabs; the source noun phrase refers to the 'open tabs' menu, and the translation loses 'open tabs'.
- `past_explorations_show_all_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "past explorations" rendered as "history" instead of the source wording.
    - Current: `पिछली सारी हिस्ट्री दिखाएं`
    - Source: `Show all past explorations`
    - Suggest: `पिछली सारी खोजबीन दिखाएं`
    - Source says "Show all past explorations"; the target says "Show all past history", using a different term than the source's branded wording.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "DNS over HTTPS" translated as "Domain Name System (DNS) instead of HTTPS", reversing the meaning.
    - Current: `HTTPS के बजाय डोमेन नेम सिस्टम (DNS)`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access. %1$s`
    - Suggest: `HTTPS पर डोमेन नेम सिस्टम (DNS)`
    - The source says DNS requests are sent over HTTPS; "के बजाय" (instead of) states the opposite relationship.
- `preference_doh_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "DNS over HTTPS" is rendered as "DNS instead of HTTPS", reversing the technical meaning.
    - Current: `HTTPS के बजाय DNS`
    - Source: `DNS over HTTPS`
    - Suggest: `HTTPS पर DNS`
    - "over" here means the DNS query is carried over an HTTPS connection, not "instead of HTTPS"; "के बजाय" means "instead of".
- `preference_downloads_folder_permission_lost` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Try choosing a different one" is rendered as "please choose a folder", dropping "different".
    - Current: `कृपया कोई फ़ोल्डर चुनें।`
    - Source: `You don’t have permission to use this folder. Try choosing a different one.`
    - Suggest: `कोई दूसरा फ़ोल्डर चुनकर देखें।`
    - The source instructs the user to pick a different folder; the translation omits "different", losing the point of the message.
- `preference_enhanced_tracking_protection_allow_list_convenience_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Sentence restructured so it reads "must be used with the fix, for major issues" instead of "must be used together with fixes for major issues".
    - Current: `प्रमुख समस्याओं के लिए, समाधान के साथ इस्तेमाल किया जाना चाहिए।`
    - Source: `Must be used with fixes for major issues.`
    - Suggest: `इसे प्रमुख समस्याओं के समाधान के साथ ही इस्तेमाल किया जाना चाहिए।`
    - The source means this option requires the "fix major issues" option to be enabled; the comma placement changes the meaning.
- `preference_enhanced_tracking_protection_custom_cookies_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Cookies from unvisited sites" is rendered as "cookies belonging to unvisited sites" with an incorrect relational form.
    - Current: `विज़िट न की गई साइटों वाली कुकीज़`
    - Source: `Cookies from unvisited sites`
    - Suggest: `विज़िट न की गई साइटों की कुकीज़`
    - The source means cookies originating from sites you have not visited; "साइटों वाली कुकीज़" is ungrammatical/ambiguous for the source relation.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "will cause websites to break" is rendered as the tentative "may cause", identical to the cookies_3 string.
    - Current: `सभी कुकीज़ (इससे शायद वेबसाइटें काम न करें)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `सभी कुकीज़ (इससे वेबसाइटें काम नहीं करेंगी)`
    - The source distinguishes "may cause websites to break" (cookies_3) from the certain "will cause websites to break" (cookies_4); the translation uses "शायद" (may) in both, weakening the warning.
- `preference_gestures_swipe_toolbar_show_tabs_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Swipe toolbar vertically" translated as swipe upward only.
    - Current: `टूलबार में ऊपर की ओर स्वाइप करें`
    - Source: `Swipe toolbar vertically to see open tabs`
    - Suggest: `टूलबार पर ऊपर-नीचे स्वाइप करें`
    - Source says vertically (both directions), not just upward.
- _…and 32 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_archive_unreachable` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Ungrammatical verb form: "नहीं जोड़ पाए" (couldn't join something) instead of "couldn't connect to the archive service".
    - Current: `आर्काइव सेवा से नहीं जोड़ पाए।`
    - Source: `Couldn’t reach the archive service.`
    - Suggest: `आर्काइव सेवा से कनेक्ट नहीं हो पाए।`
    - जोड़ना is transitive ("to attach something"); the source means the service could not be reached/connected to.
- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Question missing the interrogative marker, reading as a statement instead of a question.
    - Current: `जिस आइटम का अनुरोध किया गया है, आपके पास उसे एक्सेस करने की पर्याप्त अनुमतियां हैं?`
    - Source: `{ <ul> } { <li> }Could the item have been renamed, removed, or relocated?{ </li> } { <li> }Is there a spelling, capitalization, or other typographical error in the address?{ </li> } { <li> }Do you have sufficient access…`
    - Suggest: `जिस आइटम का अनुरोध किया गया है, क्या आपके पास उसे एक्सेस करने की पर्याप्त अनुमतियां हैं?`
    - Source is a question ("Do you have sufficient access permissions...?"); the Hindi lacks क्या, unlike the parallel sibling items which use क्या/ऐसा तो नहीं.
- `mozac_browser_errorpages_proxy_connection_refused_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "अबभी" should be written as two words "अब भी".
    - Current: `समस्या अबभी बनी हुई है?`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy refused a connection.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Does…`
    - Suggest: `समस्या अब भी बनी हुई है?`
    - "अब भी" is two separate words in Hindi; "अबभी" is a misspelling.
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Number agreement error: singular subject "ज़रूरत" takes "हो सकती है", not "हो सकती हैं".
    - Current: `प्लग-इन की ज़रूरत हो सकती हैं।`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `प्लग-इन की ज़रूरत हो सकती है।`
    - Verb does not agree in number with the singular noun ज़रूरत.
- `mozac_feature_addons_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — Stray zero-width joiner inside the word "अनुमतियां".
    - Current: `अनुमति‌यां`
    - Source: `Permissions`
    - Suggest: `अनुमतियां`
    - The target contains a ZWJ character between "अनुमति" and "यां", which is not valid in the Hindi word for "Permissions" and can render incorrectly.
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "एक्टेंड" is a misspelling of the transliteration of "extend" (should be एक्सटेंड).
    - Current: `डेवलपर टूल्स को एक्टेंड करें`
    - Source: `Extend developer tools to access your data in open tabs`
    - Suggest: `डेवलपर टूल्स को एक्सटेंड करें`
    - Source "Extend developer tools"; the Hindi transliteration of "extend" is एक्सटेंड, not एक्टेंड.
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "एक्टेंड" is a misspelling of the transliteration of "extend" (should be एक्सटेंड).
    - Current: `डेवलपर टूल्स को एक्टेंड करें।`
    - Source: `Extend developer tools to access your data in open tabs.`
    - Suggest: `डेवलपर टूल्स को एक्सटेंड करें।`
    - Source "Extend developer tools"; the Hindi transliteration of "extend" is एक्सटेंड, not एक्टेंड.
- `mozac_feature_addons_permissions_dialog_heading_optional_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — The word अनुमति‌यां contains a stray zero-width joiner character breaking the spelling.
    - Current: `नई अनुमति‌यां:`
    - Source: `New permissions:`
    - Suggest: `नई अनुमतियां:`
    - An invisible ZWJ is inserted inside अनुमतियां; the parallel string mozac_feature_addons_permissions_dialog_heading_required_permissions spells it correctly as अनुमतियां.
- `mozac_feature_addons_permissions_extra_domains_description_plural_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "अन्य डोमेन वाला अपना डेटा" is ungrammatical/wrong; should express "on other domains".
    - Current: `अन्य डोमेन वाला अपना डेटा एक्सेस करें।`
    - Source: `Access your data on other domains.`
    - Suggest: `अन्य डोमेन पर अपना डेटा एक्सेस करें।`
    - Source is "Access your data on other domains."; the postposition वाला does not convey "on" and mismatches the parallel string which correctly uses पर.
- `mozac_feature_addons_permissions_extra_sites_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "दूसरी साइटों वाला अपना डेटा" is ungrammatical; should express "on other sites".
    - Current: `दूसरी साइटों वाला अपना डेटा एक्सेस करें।`
    - Source: `Access your data on other sites.`
    - Suggest: `अन्य साइटों में अपना डेटा एक्सेस करें।`
    - Source is "Access your data on other sites."; वाला does not convey "on" and is inconsistent with the parallel string mozac_feature_addons_permissions_extra_sites_description_2.
- `mozac_feature_addons_permissions_one_extra_domain_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "किसी दूसरे डोमेन वाला अपना डेटा" is ungrammatical/wrong; should mirror "किसी अन्य डोमेन पर अपना डेटा".
    - Current: `किसी दूसरे डोमेन वाला अपना डेटा एक्सेस करें।`
    - Source: `Access your data on another domain.`
    - Suggest: `किसी अन्य डोमेन पर अपना डेटा एक्सेस करें।`
    - Source "Access your data on another domain." uses a locative; the adjectival वाला construction with अपना डेटा is grammatically wrong and diverges from the non-update variant.
- `mozac_feature_addons_permissions_one_extra_site_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "दूसरी साइट वाला अपना डेटा" is ungrammatical and drops "another" indefiniteness; should mirror "किसी अन्य साइट में अपना डेटा".
    - Current: `दूसरी साइट वाला अपना डेटा एक्सेस करें।`
    - Source: `Access your data on another site.`
    - Suggest: `किसी अन्य साइट पर अपना डेटा एक्सेस करें।`
    - Source "Access your data on another site." uses a locative; the वाला construction with अपना डेटा is wrong and inconsistent with the non-update variant.
- `mozac_feature_addons_permissions_one_site_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "%1$s का अपना डेटा" is ungrammatical; should be "%1$s के लिए अपना डेटा" as in the non-update variant.
    - Current: `%1$s का अपना डेटा एक्सेस करें।`
    - Source: `Access your data for %1$s.`
    - Suggest: `%1$s के लिए अपना डेटा एक्सेस करें।`
    - Source is "Access your data for %1$s."; combining the genitive का with अपना is grammatically incorrect and inconsistent with mozac_feature_addons_permissions_one_site_description.
- `mozac_feature_contextmenu_snackbar_link_text_copied` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-hi-rIN/strings.xml` — Translation of "Link text copied to clipboard" has a spurious comma and an incomplete verb phrase.
    - Current: `लिंक वाला टेक्स्ट, क्लिपबोर्ड में कॉपी किया`
    - Source: `Link text copied to clipboard`
    - Suggest: `लिंक टेक्स्ट क्लिपबोर्ड में कॉपी हो गया`
    - The source is a simple confirmation; the comma is wrong Hindi punctuation and "कॉपी किया" lacks agreement/completion compared with the sibling strings "क्लिपबोर्ड में कॉपी हो गया".
- `mozac_feature_downloads_dialog_download_again` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "डाउनोलड" should be "डाउनलोड".
    - Current: `फिर से डाउनोलड करें`
    - Source: `Download again`
    - Suggest: `फिर से डाउनलोड करें`
    - The transliteration of "Download" is misspelled (letters transposed) compared to the correct "डाउनलोड" used in every other string in this file.
- `mozac_feature_findindpage_input` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-hi-rIN/strings.xml` — Missing anusvara/chandrabindu in "मे" and "ढूंढें" spelling inconsistent with sibling strings.
    - Current: `पेज मे ढूंढें`
    - Source: `Find in page`
    - Suggest: `पेज में खोजें`
    - "मे" must be "में"; also the sibling strings use "खोजें" for "find" (mozac_feature_findindpage_dismiss uses 'पेज में खोजें'), making this inconsistent.
- `mozac_feature_prompts_update_address_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "अपेडट" should be "अपडेट".
    - Current: `एड्रेस अपेडट करें?`
    - Source: `Update address?`
    - Suggest: `एड्रेस अपडेट करें?`
    - Typo in the transliteration of "Update"; other strings in the same file correctly use "अपडेट".
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "नोटिफ़िकेश" is missing the final syllable of "नोटिफ़िकेशन".
    - Current: `इस वेबसाइट से नोटिफ़िकेश पाने के लिए`
    - Source: `You’ll need to allow notifications in %1$s to receive them from this website.`
    - Suggest: `इस वेबसाइट से नोटिफ़िकेशन पाने के लिए`
    - The word for "notifications" is misspelled (the correct form appears later in the same string).
- `mozac_feature_summarize_feedback_state_submitted` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — "रेटिंग सबमिट की" is an incomplete active-voice phrase; the source is a passive state "Rating submitted".
    - Current: `रेटिंग सबमिट की`
    - Source: `Rating submitted`
    - Suggest: `रेटिंग सबमिट की गई`
    - The accessibility state should read as a completed passive state, not a truncated active verb phrase.
- `mozac_summarize_info_error_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "नहींं" has a doubled anusvara/chandrabindu.
    - Current: `अभी सारांश नहींं बनाया जा सकता`
    - Source: `Can’t summarize right now`
    - Suggest: `अभी सारांश नहीं बनाया जा सकता`
    - The word for "not" is spelled नहीं; the target has an extra nasal mark producing "नहींं".
- `mozac_lib_gathering_crash_data_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-hi-rIN/strings.xml` — Missing "जा" makes the passive construction ungrammatical.
    - Current: `क्रैश डेटा इकट्ठा किया रहा है`
    - Source: `Gathering crash data`
    - Suggest: `क्रैश डेटा इकट्ठा किया जा रहा है`
    - The parallel string mozac_lib_gathering_crash_telemetry_in_progress correctly uses "इकट्ठा किया जा रहा है"; here the auxiliary "जा" is dropped, producing broken Hindi.
- `addons_does_not_require_permissions` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Missing postposition "की" before "ज़रूरत" makes the sentence ungrammatical.
    - Current: `इस एक्सटेंशन के लिए किसी भी अनुमति ज़रूरत नहीं है।`
    - Source: `This extension doesn’t require any permissions.`
    - Suggest: `इस एक्सटेंशन के लिए किसी भी अनुमति की ज़रूरत नहीं है।`
    - Hindi requires the genitive postposition: "अनुमति की ज़रूरत नहीं है"; as written it is grammatically broken.
- `addons_permissions_required_data_collection_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Wrong postposition: "इन चीज़ों का इकट्ठा करता है" should be "इन चीज़ों को इकट्ठा करता है".
    - Current: `यह एक्सटेंशन इन चीज़ों का इकट्ठा करता है`
    - Source: `The developer says this extension collects: %1$s`
    - Suggest: `यह एक्सटेंशन इन चीज़ों को इकट्ठा करता है`
    - "इकट्ठा करता है" takes the accusative को, not का; the current form is ungrammatical.
- `applinks_prompt_negative_button` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Incorrect verb form "बनें रहें" instead of "बने रहें".
    - Current: `%1$s में बनें रहें`
    - Source: `Stay in %1$s`
    - Suggest: `%1$s में बने रहें`
    - The correct Hindi for "Stay in %1$s" uses the participle "बने", not the subjunctive form "बनें".
- `browser_menu_library` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The word "लाइब्रे‌री" contains a stray zero-width non-joiner between characters.
    - Current: `लाइब्रे‌री`
    - Source: `Library`
    - Suggest: `लाइब्रेरी`
    - An invisible ZWNJ character is embedded in the word, which can break rendering/shaping of the Devanagari text; the plain spelling is लाइब्रेरी.
- `browser_toolbar_url_copied_to_clipboard_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Passive construction is incomplete: missing "गया".
    - Current: `URL क्लिपबोर्ड पर कॉपी किया`
    - Source: `URL copied to clipboard`
    - Suggest: `URL क्लिपबोर्ड पर कॉपी किया गया`
    - Source "URL copied to clipboard" is a passive statement; Hindi requires "कॉपी किया गया" — "कॉपी किया" alone is ungrammatical/incomplete.
- `certificate_warning_homepage_card_hcw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Misspelling of "एक्सपायर" as "एक्सापयर".
    - Current: `एक्सापयर होने जा रहा है`
    - Source: `Your version of Firefox will stop working properly on March 14 because a root certificate is expiring.`
    - Suggest: `एक्सपायर होने जा रहा है`
    - The transliteration of "expiring" is misspelled; elsewhere in the same set it is correctly rendered "एक्सपायर".
- `connection_security_panel_issued_to` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Past-perfect "था" added where the source uses a simple present-perfect statement.
    - Current: `%s को जारी किया गया था`
    - Source: `Issued to %s`
    - Suggest: `%s को जारी किया गया`
    - "Issued to %s" is a static certificate label; the past-tense auxiliary "था" is inconsistent with the parallel string "%s द्वारा वेरिफ़ाई किया गया".
- `crash_reporting_snack_bar_message` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Report sent" translated with an incomplete verb form lacking the auxiliary.
    - Current: `रिपोर्ट भेजी`
    - Source: `Report sent`
    - Suggest: `रिपोर्ट भेजी गई`
    - "रिपोर्ट भेजी" is ungrammatical as a standalone confirmation; the passive requires "भेजी गई".
- `deleting_browsing_data_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Wrong verb agreement: plural "हैं" used with singular subject.
    - Current: `ब्राउज़िंग डेटा डिलीट किया जा रहा हैं…`
    - Source: `Deleting browsing data…`
    - Suggest: `ब्राउज़िंग डेटा डिलीट किया जा रहा है…`
    - "किया जा रहा" is singular and requires "है", not the plural "हैं".
- `download_item_paused_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "पॉज़ किया" is an incomplete verb form; the status should read as a state.
    - Current: `पॉज़ किया`
    - Source: `%1$s / %2$s • paused`
    - Suggest: `पॉज़ किया गया`
    - The source "paused" is a status label; the Hindi participle needs "गया" to be grammatical as a passive state description.
- `microsurvey_uninstall_survey_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Ungrammatical rendering of "Why are you uninstalling?" with wrong verb agreement ("हैं" for singular "है") and odd "मन" phrasing.
    - Current: `आपका इसे अनइंस्टॉल करने का मन क्यों हैं?`
    - Source: `Your feedback matters. Why are you uninstalling?`
    - Suggest: `आप इसे अनइंस्टॉल क्यों कर रहे हैं?`
    - The source asks why the user is uninstalling; the Hindi asks why the user "feels like" uninstalling and has a subject-verb agreement error ("मन ... हैं" should be "है").
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — English possessive "'s" left attached to the brand name inside Hindi text, producing "Firefox’s की".
    - Current: `Firefox’s की ऑटोमैटिक सुरक्षा`
    - Source: `Start every search from your phone’s home screen and know Firefox’s automatic protections have your back.`
    - Suggest: `Firefox की ऑटोमैटिक सुरक्षा`
    - The source's possessive "Firefox’s" is already rendered by the Hindi postposition "की"; keeping the English apostrophe-s is a copy error and misspells the brand name.
- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Misspelling: "हमेशना" should be "हमेशा".
    - Current: `हमेशना अवगत रहें`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `हमेशा अवगत रहें`
    - "हमेशना" is not a word; the correct Hindi for "always" is "हमेशा".
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Spelling error: doubled nasal consonant in "भरोसेमंंद".
    - Current: `भरोसेमंंद`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `भरोसेमंद`
    - The word contains a duplicated anusvara/nasal mark, a spelling error.
- `onboarding_preferences_dialog_usage_data_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Missing postposition makes the sentence read "Mozilla sends technical data" instead of "send data to Mozilla".
    - Current: `Mozilla टेक्निकल और इंटरैक्शन संबंधी डेटा भेजें`
    - Source: `Send technical and interaction data to Mozilla`
    - Suggest: `Mozilla को टेक्निकल और इंटरैक्शन संबंधी डेटा भेजें`
    - Source is "Send technical and interaction data to Mozilla"; Hindi requires the dative marker 'को' for the recipient, as done correctly in nova_onboarding_tou_body_line_3.
- `onboarding_redesign_customize_toolbar_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "कहां" is missing the required nasalization; should be "कहाँ".
    - Current: `आपका एड्रेस बार कहां पर रखना है?`
    - Source: `Where do you want your address bar?`
    - Suggest: `आपका एड्रेस बार कहाँ पर रखना है?`
    - Standard Hindi spelling requires the chandrabindu/anusvara nasalization in कहाँ; the same string also uses जहां-जहां elsewhere, but कहां without nasal mark is a spelling error.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "pinch" translated literally as "चुटकी" (a pinch of something), producing nonsense for the pinch-to-zoom gesture.
    - Current: `चुटकी और ज़ूम करने की अनुमति`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `पिंच और ज़ूम करने की अनुमति`
    - The source refers to the pinch-and-zoom gesture; "चुटकी" does not convey the touch gesture.
- `preference_doh_exceptions_add_error` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Duplicated word "होना" in the error message.
    - Current: `डोमेन सही होना होना चाहिए`
    - Source: `Must be a valid domain`
    - Suggest: `डोमेन सही होना चाहिए`
    - The word होना is repeated, which is a grammatical/typing error; source is "Must be a valid domain".
- `preference_enhanced_tracking_protection_explanation_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Ungrammatical phrase "सबसे आमतौर पर पाए जाने ट्रैकर्स" (missing वाले) and "many of" is dropped.
    - Current: `%s सबसे आमतौर पर पाए जाने ट्रैकर्स से आपकी रक्षा करता है`
    - Source: `%s protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `%s सबसे आम ट्रैकर्स में से कई से आपकी रक्षा करता है`
    - "पाए जाने" needs "वाले" to be grammatical, and the source's "many of the most common trackers" is rendered as all of them.
- `preferences_open_links_in_a_private_tab` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Misspelled postposition "मे" instead of "में".
    - Current: `लिंक को प्राइवेट टैब मे खोलें`
    - Source: `Open links in a private tab`
    - Suggest: `लिंक को प्राइवेट टैब में खोलें`
    - Hindi locative postposition is "में"; "मे" is a spelling error.
- `protection_panel_banner_not_secure_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "नही" should be "नहीं".
    - Current: `आपका कनेक्शन सुरक्षित नही है।`
    - Source: `Your connection is not secure.`
    - Suggest: `आपका कनेक्शन सुरक्षित नहीं है।`
    - The Hindi negation is spelled नहीं (with anusvara and long ii); नही is a misspelling.
- `protection_panel_permissions_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Stray zero-width joiner inside the word "अनुमतियां".
    - Current: `अनुमति‌यां`
    - Source: `Permissions`
    - Suggest: `अनुमतियां`
    - A zero-width non-joiner/joiner character is embedded between "अनुमति" and "यां", corrupting rendering of the word.
- `search_engine_add_custom_search_engine_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "ईंजन" instead of "इंजन".
    - Current: `खोज ईंजन जोड़ें`
    - Source: `Add search engine`
    - Suggest: `खोज इंजन जोड़ें`
    - "engine" is spelled इंजन elsewhere in the same file (e.g. search_engine_edit_custom_search_engine_title); "ईंजन" is a misspelling.
- `search_engine_edit` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Spelling error: stray nukta on "ए" in "ए़डिट करें".
    - Current: `ए़डिट करें`
    - Source: `Edit`
    - Suggest: `एडिट करें`
    - The word should be "एडिट करें" as used consistently in other strings (e.g. search_engine_edit_custom_search_engine_title, credit_cards_edit_card); the nukta diacritic on ए is a typo.
- `setup_checklist_subtitle_6_steps_fourth_step` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Missing subject "आप" makes the sentence ungrammatical/incomplete.
    - Current: `4 चरण तक पहुंच गए हैं।`
    - Source: `You’re 4 steps in. Only 2 more to go!`
    - Suggest: `आप 4 चरण तक पहुंच गए हैं।`
    - Source "You’re 4 steps in." has an explicit subject; the Hindi drops it, leaving a dangling verb phrase inconsistent with the other checklist subtitles which use "आपने/आप".
- `sign_in_create_account_text` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Misspelling of "अकाउंट" as "अकाउंंट" (doubled anusvara).
    - Current: `अकाउंंट { <u> }बनाएं{ </u> }`
    - Source: `No account? { <u> }Create one{ </u> } to sync Firefox between devices.`
    - Suggest: `अकाउंट { <u> }बनाएं{ </u> }`
    - The word is spelled correctly earlier in the same string as "अकाउंट"; here it has an extra anusvara.
- `tab_tray_add_new_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Imperative verb form is wrong: "जोड़े" should be "जोड़ें".
    - Current: `नया कलेक्शन जोड़े`
    - Source: `Add new collection`
    - Suggest: `नया कलेक्शन जोड़ें`
    - The polite imperative of जोड़ना is जोड़ें; जोड़े is an incorrect form here, inconsistent with चुनें in the neighbouring string.
- `unsubmitted_crash_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Ungrammatical sentence: postposition "से" plus comma leaves the subject and verb disagreeing.
    - Current: `क्रैश रिपोर्ट से, हमें ब्राउज़र से जुड़ी समस्याओं का पता लगाने और उन्हें ठीक करने में मदद करती है।`
    - Source: `Crash reports help us to diagnose and fix issues with the browser. Reports may include personal or sensitive data. %s`
    - Suggest: `क्रैश रिपोर्ट से हमें ब्राउज़र से जुड़ी समस्याओं का पता लगाने और उन्हें ठीक करने में मदद मिलती है।`
    - With "क्रैश रिपोर्ट से" the verb must be "मदद मिलती है", not "मदद करती है"; as written the sentence has no valid subject for "करती है".
- `download_snackbar_open` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Imperative verb form is misspelled/incorrect for the button label "Open".
    - Current: `खोले`
    - Source: `Open`
    - Suggest: `खोलें`
    - Hindi imperative should be खोलें; खोले is an incorrect form, inconsistent with other imperative labels in the file (जोड़ें, सहेजें).
- `firstrun_privacy_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Imperative verb form is wrong/incomplete for "Make privacy a habit".
    - Current: `गोपनीयता एक आदत बनाये`
    - Source: `Make privacy a habit`
    - Suggest: `गोपनीयता को एक आदत बनाएँ`
    - "बनाये" is not the correct polite imperative; the correct form is "बनाएँ", and the object marker is missing.
- `firstrun_search_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Gender agreement error: "खोज" is feminine, so the possessive should be "आपकी".
    - Current: `आपका खोज, आपका रास्ता`
    - Source: `Your search, your way`
    - Suggest: `आपकी खोज, आपका रास्ता`
    - "खोज" is a feminine noun in Hindi and requires "आपकी", not "आपका".
- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Wrong verb number: "स्वागत हैं" should be "स्वागत है".
    - Current: `%1$s में आपका स्वागत हैं`
    - Source: `Welcome to %1$s`
    - Suggest: `%1$s में आपका स्वागत है`
    - "स्वागत" is singular, so the copula must be "है", not the plural "हैं".
- `preference_advanced_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Misspelling of "डेवलपर".
    - Current: `डेवलेपर औज़ार`
    - Source: `Developer tools`
    - Suggest: `डेवलपर औज़ार`
    - "डेवलेपर" is a misspelling of the transliteration of "developer" (डेवलपर).
- `preference_mozilla_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Missing postposition/word order: "%1$s परिचय" is ungrammatical for "About %1$s".
    - Current: `%1$s परिचय, सहायता`
    - Source: `About %1$s, help`
    - Suggest: `%1$s के बारे में, सहायता`
    - Hindi requires "के बारे में" or "का परिचय"; a bare noun juxtaposition is grammatically incorrect.
- `preference_mozilla_telemetry2` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "उपयोगित" is not a valid Hindi word for "usage".
    - Current: `उपयोगित डेटा भेजें`
    - Source: `Send usage data`
    - Suggest: `उपयोग डेटा भेजें`
    - Source is "Send usage data"; "उपयोगित" is a malformed form, correct is "उपयोग" (or "उपयोग संबंधी").
- `preference_performance_block_webfonts_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Awkward/incorrect construction "के रूप में परिणाम हो सकता है" for "May result in".
    - Current: `अनुपस्थित प्रतीकों या छवियों के रूप में परिणाम हो सकता है`
    - Source: `May result in missing icons or images`
    - Suggest: `इससे प्रतीक या छवियाँ गायब हो सकती हैं`
    - Source means enabling this may cause icons or images to be missing; the literal "result in the form of" phrasing is ungrammatical in Hindi.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Case agreement error: "गतिविधियाँ" should be oblique "गतिविधियों को" as object of collect/analyze/measure.
    - Current: `टैपिंग और स्क्रॉलिंग जैसी गतिविधियाँ एकत्र, विश्लेषण और मापने के लिए उपयोग`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `टैपिंग और स्क्रॉलिंग जैसी गतिविधियों को एकत्र करने, उनका विश्लेषण करने और उन्हें मापने के लिए उपयोग किया जाता है`
    - The source is a passive clause with 'activities' as object; the Hindi leaves the noun in nominative plural and the verb chain incomplete.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Misspelling "दुसरे" (should be "दूसरे") and nonstandard "ऐप्प".
    - Current: `एक ऐप्प से दुसरे ऐप्प पर जाते समय`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `एक ऐप से दूसरे ऐप पर जाते समय`
    - "दुसरे" is a spelling error; the correct form is "दूसरे".
- `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Case agreement error: the coordinated objects are in nominative (साइटें) instead of oblique before "को ब्लॉक करें".
    - Current: `रिपोर्ट किये हुए भ्रामक तथा अटैक करने वाली साइटें, मैलवेयर वाली साइटें, तथा अवांछित सॉफ्टवेयर वाली साइटों को ब्लॉक करें।`
    - Source: `Block reported deceptive and attack sites, malware sites, and unwanted software sites.`
    - Suggest: `रिपोर्ट की गई भ्रामक तथा अटैक करने वाली साइटों, मैलवेयर वाली साइटों तथा अवांछित सॉफ़्टवेयर वाली साइटों को ब्लॉक करें।`
    - All three coordinated noun phrases share the postposition "को" and must be oblique (साइटों); the first two are left in the nominative plural, which is ungrammatical.
- _…and 4 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “फिर से कोशिश करें” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “फिर कोशिश करें”
    - Current: `{ <p> }ब्राउज़र ऑफ़लाइन मोड में चल रहा है और अनुरोध किए गए आइटम से कनेक्ट नहीं हो सकता है।{ </p> } { <ul> } { <li> }क्या डिवाइस किसी एक्टिव नेटवर्क से जुड़ा हुआ है?{ </li> } { <li> }ऑनलाइन मोड में जाने के लिए “फिर से कोशि…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `फिर कोशिश करें`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `ip_protection_location_recommended_label` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Recommended" (adjective label for the option) translated as the noun "सुझाव" (suggestion).
    - Current: `सुझाव`
    - Source: `Recommended`
    - Suggest: `सुझाई गई`
    - The developer comment says this labels the recommended automatic location option; other strings in the same screen use "सुझाई गई लोकेशन", so the noun "सुझाव" is both wrong and inconsistent.
- `phone_feature_recommended` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Recommended" translated as the noun "सुझाव" (suggestion) rather than an adjective label.
    - Current: `सुझाव`
    - Source: `Recommended`
    - Suggest: `अनुशंसित`
    - The developer comment states this label indicates the option is the recommended one; "सुझाव" means "suggestion", not "recommended".
- `qr_code_download_failure` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "QR Code" transliterated as क्यूआर कोड here while other QR strings keep the Latin "QR कोड".
    - Current: `क्यूआर कोड सेव नहीं हुआ`
    - Source: `Failed to save QR Code`
    - Suggest: `QR कोड सेव नहीं हुआ`
    - Inconsistent with qr_code_display_title and qr_code_display_instructions which use "QR कोड" on the same surface.
- `qr_code_download_success` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "QR Code" transliterated as क्यूआर कोड, inconsistent with other QR strings; also "Downloads" folder rendered ambiguously.
    - Current: `क्यूआर कोड डाउनलोड में सेव किया गया`
    - Source: `QR Code saved to Downloads`
    - Suggest: `QR कोड डाउनलोड में सेव किया गया`
    - Other strings in the same feature use "QR कोड"; the same source term should render consistently.
- `insecure_connection` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Connection" rendered as "संपर्क" (contact) instead of the standard "कनेक्शन"/"संबंध".
    - Current: `संपर्क सुरक्षित नहीं है`
    - Source: `Connection is not secure`
    - Suggest: `कनेक्शन सुरक्षित नहीं है`
    - In browser security UI, "connection" is a network connection; "संपर्क" means contact and is the wrong term.
- `preference_privacy_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Block" rendered inconsistently across cookie settings (बाधित/प्रतिबंधित/ब्लॉक/अवरुद्ध).
    - Current: `कुकीज़ बाधित करें`
    - Source: `Block cookies`
    - Suggest: `कुकीज़ ब्लॉक करें`
    - On the same settings screen, "Block" appears as बाधित करें, प्रतिबंधित करें and ब्लॉक करें; "बाधित" means obstruct/interrupt and is the weakest match for blocking cookies.
- `secure_connection` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Connection" is translated as "संपर्क" (contact) instead of the standard "कनेक्शन"/"संबंध".
    - Current: `संपर्क सुरक्षित है`
    - Source: `Connection is secure`
    - Suggest: `कनेक्शन सुरक्षित है`
    - The label indicates a secure network connection; "संपर्क" means contact and is not the established term for a network connection.

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_archive_retry` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Stray zero-width joiner character inside the word कोशिश.
    - Current: `फिर कोशिश‌ करें।`
    - Source: `Retry.`
    - Suggest: `फिर कोशिश करें।`
    - An invisible ZWJ appears after कोशिश, which is not part of the word and can affect rendering/search.
- `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Missing space between the URL example and the following word.
    - Current: `{ <strong> }http://www.example.com/{ </strong> }की तरह लिखे जाते हैं`
    - Source: `{ <ul> } { <li> }Web addresses are usually written like { <strong> }http://www.example.com/{ </strong> }{ </li> } { <li> }Make sure that you’re using forward slashes (i.e. { <strong> }/{ </strong> }).{ </li> } { </ul> }`
    - Suggest: `{ <strong> }http://www.example.com/{ </strong> } की तरह लिखे जाते हैं`
    - The word की runs directly into the closing markup after the URL, producing "...example.com/की तरह" with no space in the rendered text.
- `mozac_browser_errorpages_security_ssl_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Missing sentence-final danda/period at the end of the first list item.
    - Current: `प्राप्त डेटा की प्रामाणिकता वेरिफ़ाई नहीं की जा सकी{ </li> }`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because the authenticity of the received data could not be verified.{ </li> } { <li> }Please contact the website owners to inform them of this problem.{ <…`
    - Suggest: `प्राप्त डेटा की प्रामाणिकता वेरिफ़ाई नहीं की जा सकी।{ </li> }`
    - The source sentence ends with a period; the translation omits terminal punctuation, unlike the parallel item in the same string.
- `mozac_feature_extensions_manager_notification_title_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — Trailing full stop added to a notification title that has none in the source.
    - Current: `एक्सटेंशन को कुछ समय के लिए बंद किया गया है।`
    - Source: `Extensions are temporarily disabled`
    - Suggest: `एक्सटेंशन कुछ समय के लिए बंद किए गए हैं`
    - Source title "Extensions are temporarily disabled" has no terminal punctuation; the localized title adds a danda-equivalent period.
- `mozac_feature_autofill_confirmation_no` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-hi-rIN/strings.xml` — Button label contains a stray zero-width non-joiner after the word.
    - Current: `नहीं‌`
    - Source: `No`
    - Suggest: `नहीं`
    - The translation of "No" ends with an invisible ZWNJ character that is not part of the word.
- `mozac_feature_sitepermissions_option_microphone_one` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-hi-rIN/strings.xml` — Missing space between the word and the numeral in "माइक्रोफ़ोन1".
    - Current: `माइक्रोफ़ोन1`
    - Source: `Microphone 1`
    - Suggest: `माइक्रोफ़ोन 1`
    - Source is "Microphone 1" with a space; the target runs the label and number together.
- `mozac_open_tab_counter_tab_tray` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-hi-rIN/strings.xml` — Latin full stop used instead of the Devanagari danda used in the parallel strings.
    - Current: `%1$s. टैब स्विच करने के लिए टैप करें।`
    - Source: `Non-private Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `%1$s। टैब स्विच करने के लिए टैप करें।`
    - The sibling strings mozac_tab_counter_open_tab_tray and mozac_tab_counter_private use "%1$s। टैब स्विच…"; this one is inconsistent.
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `वेब एड्रेस में "https://" या "http://" ज़रूर होना चाहिए`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (10 occurrences).
- `addon_failure_retry_action` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Stray zero-width non-joiner character inside "कोशिश‌ करें".
    - Current: `फिर कोशिश‌ करें`
    - Source: `Retry`
    - Suggest: `फिर कोशिश करें`
    - An invisible ZWNJ control character was inserted between "कोशिश" and the space, which does not belong in the user-visible text.
- `etp_social_media_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Missing sentence-final danda; the source sentence ends with a period.
    - Current: `लगाम लगाता है`
    - Source: `Limits the ability of social networks to track your browsing activity around the web.`
    - Suggest: `लगाम लगाता है।`
    - The en-US string is a full sentence ending in a period; other ETP descriptions in this batch end with "।".
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The quotation marks around the menu item name “Never translate this site” were dropped.
    - Current: `अनुवाद वाले मेन्यू से इस साइट का कभी अनुवाद न करें चुनें`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `अनुवाद वाले मेन्यू से “इस साइट का कभी अनुवाद न करें” चुनें`
    - The source quotes the menu label; without quotes the sentence is unreadable in Hindi.
- `preference_doh_provider_custom_dialog_add` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — String begins with a stray zero-width non-joiner character before जोड़ें.
    - Current: `‌जोड़ें`
    - Source: `Add`
    - Suggest: `जोड़ें`
    - An invisible ZWNJ control character precedes the word, which is not part of the text and can affect rendering; source is simply "Add".
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — `preference_summary_delete_browsing_data_on_quit_2` uses straight double quotes
    - Current: `जब आप मेन मेन्यू से "बाहर निकलें" चुनते हैं, तो ब्राउज़िंग डेटा को अपने आप डिलीट कर देता है`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - The locale's quote convention is `curly-double` (10 occurrences).
- `preference_summary_delete_browsing_data_on_quit_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Straight double quotes used instead of the locale's curly double quotes as in the source.
    - Current: `"बाहर निकलें"`
    - Source: `Automatically deletes browsing data when you select “Quit” from the main menu`
    - Suggest: `“बाहर निकलें”`
    - Source uses curly quotes “Quit”; hi-IN convention is curly-double quotes.
- `sync_connect_device_dialog` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Double space between words in the translation.
    - Current: `एक और  डिवाइस`
    - Source: `To send a tab, sign in to Firefox on at least one other device.`
    - Suggest: `एक और डिवाइस`
    - There is an extra space in the user-visible text that is not in the source.

---

## 4. Appendix

### Dismissed by hand (1)

- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Text is to incite user to help

_One line each in `locales/hi-IN/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (52)

- `mozac_browser_errorpages_httpsonly_button` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_browser_menu2_button` — `mozilla-mobile/android-components/components/browser/menu2/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_feature_addons_permissions_required_data_collection_description_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_feature_contextmenu_share_image` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_feature_downloads_could_not_open_file` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_feature_downloads_dialog_cancel` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_feature_media_sharing_camera_and_microphone_text` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_feature_prompt_before_unload_dialog_body` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_feature_prompts_expand_logins_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_feature_prompts_identity_credentials_choose_provider` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `mozac_summarize_info_error_code` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `collection_open_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `create_collection_save_to_collection_tabs_selected` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `create_collection_select_collection` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `create_collection_select_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `credit_cards_biometric_prompt_message_pin` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `delete_browsing_data_quit_off` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `delete_browsing_data_quit_on` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `download_language_file_dialog_message_all_languages` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `enhanced_tracking_protection_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `etp_cookies_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `etp_cryptominers_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `etp_social_media_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `etp_tracking_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `exceptions_empty_message_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `inactive_tabs_auto_close_message_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `logins_username_copied` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `notification_pbm_delete_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `phone_feature_blocked_step_feature` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `preference_accessibility_auto_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `preference_enhanced_tracking_protection_custom_cookies_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `preference_enhanced_tracking_protection_custom_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `preference_experiments_summary_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `preferences_delete_browsing_data_browsing_data_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
- `preferences_delete_browsing_data_cached_files` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-10
