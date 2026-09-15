# Android l10n QA — hi-IN

| | |
|---|---|
| **Generated** | 2026-09-15 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `96fcd0319e5c` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `96fcd0319e5c` |
| **Previous run** | 2026-09-14 @ `6e23dc94dd8f` |
| **Mode** | incremental |
| **Strings reviewed this run** | 101 of 2,665 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for hi-IN: [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (6)

- `mozac_browser_awesomebar_stock_suggestion_increase` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-hi-rIN/strings.xml` — Translation adds "साइज़" (size), which is not in the source about a stock price gain.
    - Current: `साइज़ %s प्रतिशत बढ़ा`
    - Source: `Gained %s percent`
    - Suggest: `%s प्रतिशत बढ़ा`
    - Source is "Gained %s percent" describing a stock increase; the paired decrease string is correctly "%s प्रतिशत गिरा" with no such word. "साइज़" (size) is invented and inconsistent.
- `mozac_feature_addons_permissions_one_site_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "Access your data for %1$s" is rendered so it reads as an instruction to the user rather than a permission the add-on requests, and drops "आपका" possessive consistency.
    - Current: `%1$s के लिए अपना डेटा एक्सेस करें।`
    - Source: `Access your data for %1$s.`
    - Suggest: `%1$s के लिए आपका डेटा एक्सेस करना।`
    - This is a permission description listing what the add-on will do; the imperative "एक्सेस करें" tells the user to access their own data, changing who performs the action.
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-hi-rIN/strings.xml` — "Continue browsing without VPN" is rendered as an imperative command instead of an offered option.
    - Current: `VPN के बिना ब्राउज़ करना जारी रखें या बंद करने के लिए टैब चुनें।`
    - Source: `VPN isn’t working right now so your location may be visible. Continue browsing without VPN, or choose tabs to close.`
    - Suggest: `आप VPN के बिना ब्राउज़ करना जारी रख सकते हैं या बंद करने के लिए टैब चुन सकते हैं।`
    - The source presents two choices to the user; the Hindi imperative instructs the user to keep browsing without VPN.
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "won't sell you out" is rendered as "is trustworthy", dropping the claim about not selling out users.
    - Current: `तेज़, सुरक्षित और भरोसेमंद है।`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `तेज़, सुरक्षित और आपको धोखा नहीं देगा।`
    - The source promises the browser will not sell the user out (i.e., not betray/sell their data); the Hindi merely says it is "trustworthy", which is a different, vaguer claim.
- `debug_drawer_tab_tools_tab_quantity_non_digits_error` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "positive integers" is rendered as "integers greater than 0" with an odd numeric phrasing; the source does not mention 0.
    - Current: `कृपया सिर्फ़ 0 से बड़ी पूर्ण संख्या डालें`
    - Source: `Please enter positive integers only`
    - Suggest: `कृपया सिर्फ़ धनात्मक पूर्णांक ही डालें`
    - The en-US says "Please enter positive integers only"; the translation introduces a specific numeric bound wording not in the source and is also singular where the source is plural.
- `preference_doh_exceptions_add_error` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Must be a valid domain" is rendered as "The domain must be correct", losing the requirement that the entry be a domain.
    - Current: `डोमेन सही होना चाहिए`
    - Source: `Must be a valid domain`
    - Suggest: `यह एक मान्य डोमेन होना चाहिए`
    - The source states the input must be a valid domain; the target asserts a domain must be correct, which shifts the meaning of the validation error.

### ✅ Fixed since the last run (81)

- `mozac_browser_errorpages_archive_retry` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Stray zero-width joiner character inside the word कोशिश.
    - Current: `फिर कोशिश‌ करें।`
    - Source: `Retry.`
    - Suggest: `फिर कोशिश करें।`
    - An invisible ZWJ appears after कोशिश, which is not part of the word and can affect rendering/search.
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
- `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Missing space between the URL example and the following word.
    - Current: `{ <strong> }http://www.example.com/{ </strong> }की तरह लिखे जाते हैं`
    - Source: `{ <ul> } { <li> }Web addresses are usually written like { <strong> }http://www.example.com/{ </strong> }{ </li> } { <li> }Make sure that you’re using forward slashes (i.e. { <strong> }/{ </strong> }).{ </li> } { </ul> }`
    - Suggest: `{ <strong> }http://www.example.com/{ </strong> } की तरह लिखे जाते हैं`
    - The word की runs directly into the closing markup after the URL, producing "...example.com/की तरह" with no space in the rendered text.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — Missing postposition makes the sentence say the app is not trusted by the site rather than the app not trusting the site.
    - Current: `%1$s को { <b> }%2$s{ </b> } भरोसा नहीं हो पा रहा है`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `%1$s को { <b> }%2$s{ </b> } पर भरोसा नहीं है`
    - Source: "%1$s does not trust %2$s". Without the postposition "पर" after the URL, the agent/object relation is ungrammatical and ambiguous.
- `mozac_browser_toolbar_content_description_autoplay_blocked` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-hi-rIN/strings.xml` — Gender agreement error: 'कंटेंट' takes masculine agreement, not 'ब्लॉक हो गई है'.
    - Current: `कुछ कंटेंट ब्लॉक हो गई है`
    - Source: `Some content has been blocked by the autoplay setting`
    - Suggest: `कुछ कंटेंट ब्लॉक हो गया है`
    - 'कंटेंट' is treated as masculine in Hindi localization; the feminine verb form is ungrammatical.
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
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-hi-rIN/strings.xml` — "Continue browsing without VPN" is rendered as an imperative command instead of an offered option.
    - Current: `VPN के बिना ब्राउज़ करना जारी रखें या बंद करने के लिए टैब चुनें।`
    - Source: `VPN isn’t working right now so your location may be visible. Continue browsing without VPN, or choose tabs to close.`
    - Suggest: `आप VPN के बिना ब्राउज़ करना जारी रख सकते हैं या बंद करने के लिए टैब चुन सकते हैं।`
    - The source presents two choices to the user; the Hindi imperative instructs the user to keep browsing without VPN.
- `mozac_feature_readerview_font_size_decrease_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-hi-rIN/strings.xml` — "Font size decrease" (an action description) rendered as "small font size", losing the action meaning.
    - Current: `फ़ॉन्ट का छोटा आकार`
    - Source: `Font size decrease`
    - Suggest: `फ़ॉन्ट का आकार घटाएं`
    - The developer comment says it is the accessible description for decreasing the font size; the target describes a small font size instead of the decrease action.
- `mozac_feature_readerview_font_size_increase_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-hi-rIN/strings.xml` — "Font size increase" (an action description) rendered as "large font size", losing the action meaning.
    - Current: `फ़ॉन्ट का बड़ा आकार`
    - Source: `Font size increase`
    - Suggest: `फ़ॉन्ट का आकार बढ़ाएं`
    - The developer comment says it is the accessible description for increasing the font size; the target describes a large font size instead of the increase action.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "नोटिफ़िकेश" is missing the final syllable of "नोटिफ़िकेशन".
    - Current: `इस वेबसाइट से नोटिफ़िकेश पाने के लिए`
    - Source: `You’ll need to allow notifications in %1$s to receive them from this website.`
    - Suggest: `इस वेबसाइट से नोटिफ़िकेशन पाने के लिए`
    - The word for "notifications" is misspelled (the correct form appears later in the same string).
- `mozac_feature_sitepermissions_option_microphone_one` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-hi-rIN/strings.xml` — Missing space between the word and the numeral in "माइक्रोफ़ोन1".
    - Current: `माइक्रोफ़ोन1`
    - Source: `Microphone 1`
    - Suggest: `माइक्रोफ़ोन 1`
    - Source is "Microphone 1" with a space; the target runs the label and number together.
- `mozac_lib_gathering_crash_data_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-hi-rIN/strings.xml` — Missing "जा" makes the passive construction ungrammatical.
    - Current: `क्रैश डेटा इकट्ठा किया रहा है`
    - Source: `Gathering crash data`
    - Suggest: `क्रैश डेटा इकट्ठा किया जा रहा है`
    - The parallel string mozac_lib_gathering_crash_telemetry_in_progress correctly uses "इकट्ठा किया जा रहा है"; here the auxiliary "जा" is dropped, producing broken Hindi.
- `mozac_open_tab_counter_tab_tray` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-hi-rIN/strings.xml` — Latin full stop used instead of the Devanagari danda used in the parallel strings.
    - Current: `%1$s. टैब स्विच करने के लिए टैप करें।`
    - Source: `Non-private Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `%1$s। टैब स्विच करने के लिए टैप करें।`
    - The sibling strings mozac_tab_counter_open_tab_tray and mozac_tab_counter_private use "%1$s। टैब स्विच…"; this one is inconsistent.
- `addon_failure_retry_action` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Stray zero-width non-joiner character inside "कोशिश‌ करें".
    - Current: `फिर कोशिश‌ करें`
    - Source: `Retry`
    - Suggest: `फिर कोशिश करें`
    - An invisible ZWNJ control character was inserted between "कोशिश" and the space, which does not belong in the user-visible text.
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
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Spurious comma after "कभी भी" and missing sentence-final danda/period present in the source.
    - Current: `%1$s कभी भी, इस भाषा की साइटों का अनुवाद करने की पेशकश नहीं करेगा`
    - Source: `%1$s will never offer to translate sites in this language.`
    - Suggest: `%1$s इस भाषा की साइटों का अनुवाद करने की पेशकश कभी नहीं करेगा।`
    - The source sentence ends with a period and contains no internal comma; the parallel string automatic_translation_option_offer_to_translate_summary_preference ends with "।".
- `browser_menu_library` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The word "लाइब्रे‌री" contains a stray zero-width non-joiner between characters.
    - Current: `लाइब्रे‌री`
    - Source: `Library`
    - Suggest: `लाइब्रेरी`
    - An invisible ZWNJ character is embedded in the word, which can break rendering/shaping of the Devanagari text; the plain spelling is लाइब्रेरी.
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
- `deleting_browsing_data_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Wrong verb agreement: plural "हैं" used with singular subject.
    - Current: `ब्राउज़िंग डेटा डिलीट किया जा रहा हैं…`
    - Source: `Deleting browsing data…`
    - Suggest: `ब्राउज़िंग डेटा डिलीट किया जा रहा है…`
    - "किया जा रहा" is singular and requires "है", not the plural "हैं".
- `ip_protection_location_recommended_label` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Recommended" (adjective label for the option) translated as the noun "सुझाव" (suggestion).
    - Current: `सुझाव`
    - Source: `Recommended`
    - Suggest: `सुझाई गई`
    - The developer comment says this labels the recommended automatic location option; other strings in the same screen use "सुझाई गई लोकेशन", so the noun "सुझाव" is both wrong and inconsistent.
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
- `microsurvey_uninstall_survey_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Ungrammatical rendering of "Why are you uninstalling?" with wrong verb agreement ("हैं" for singular "है") and odd "मन" phrasing.
    - Current: `आपका इसे अनइंस्टॉल करने का मन क्यों हैं?`
    - Source: `Your feedback matters. Why are you uninstalling?`
    - Suggest: `आप इसे अनइंस्टॉल क्यों कर रहे हैं?`
    - The source asks why the user is uninstalling; the Hindi asks why the user "feels like" uninstalling and has a subject-verb agreement error ("मन ... हैं" should be "है").
- `never_translate_site_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The quotation marks around the menu item name “Never translate this site” were dropped.
    - Current: `अनुवाद वाले मेन्यू से इस साइट का कभी अनुवाद न करें चुनें`
    - Source: `To add a new site: Visit it and select “Never translate this site” from the translation menu.`
    - Suggest: `अनुवाद वाले मेन्यू से “इस साइट का कभी अनुवाद न करें” चुनें`
    - The source quotes the menu label; without quotes the sentence is unreadable in Hindi.
- `no_site_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "No site exceptions" mistranslated as "no exceptions with sites".
    - Current: `साइट वाले कोई अपवाद नहीं हैं`
    - Source: `No site exceptions`
    - Suggest: `कोई साइट अपवाद नहीं`
    - The source is a label for the absence of site-specific exceptions; "साइट वाले" ("with sites") misrenders the noun phrase "site exceptions".
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — English possessive "'s" left attached to the brand name inside Hindi text, producing "Firefox’s की".
    - Current: `Firefox’s की ऑटोमैटिक सुरक्षा`
    - Source: `Start every search from your phone’s home screen and know Firefox’s automatic protections have your back.`
    - Suggest: `Firefox की ऑटोमैटिक सुरक्षा`
    - The source's possessive "Firefox’s" is already rendered by the Hindi postposition "की"; keeping the English apostrophe-s is a copy error and misspells the brand name.
- `nova_onboarding_marketing_body_line_three` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Added phrase "अपने इस लक्ष्य में" ("in this goal of yours") not present in the source.
    - Current: `अपने इस लक्ष्य में Firefox को जीतने में मदद करने के लिए, अनुमति देने पर विचार करें।`
    - Source: `Please consider allowing to help Firefox win.`
    - Suggest: `Firefox को जीतने में मदद करने के लिए अनुमति देने पर विचार करें।`
    - The source is simply "Please consider allowing to help Firefox win."; the translation invents a reference to the user's own goal.
- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Misspelling: "हमेशना" should be "हमेशा".
    - Current: `हमेशना अवगत रहें`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `हमेशा अवगत रहें`
    - "हमेशना" is not a word; the correct Hindi for "always" is "हमेशा".
- `nova_onboarding_set_to_default_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "spying on your clicks" is rendered as "spying on you", dropping the specific object.
    - Current: `कंपनियों को आपकी जासूसी करने से ऑटोमैटिक तौर पर ब्लॉक करते हैं`
    - Source: `We protect your data and automatically block companies from spying on your clicks.`
    - Suggest: `कंपनियों को आपके क्लिक की जासूसी करने से ऑटोमैटिक तौर पर ब्लॉक करते हैं`
    - The source says companies are blocked from spying on your clicks; the translation broadens it to spying on the user generally.
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
- `phone_feature_recommended` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Recommended" translated as the noun "सुझाव" (suggestion) rather than an adjective label.
    - Current: `सुझाव`
    - Source: `Recommended`
    - Suggest: `अनुशंसित`
    - The developer comment states this label indicates the option is the recommended one; "सुझाव" means "suggestion", not "recommended".
- `preference_doh_exceptions_add_error` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Duplicated word "होना" in the error message.
    - Current: `डोमेन सही होना होना चाहिए`
    - Source: `Must be a valid domain`
    - Suggest: `डोमेन सही होना चाहिए`
    - The word होना is repeated, which is a grammatical/typing error; source is "Must be a valid domain".
- `preference_doh_provider_custom_dialog_add` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — String begins with a stray zero-width non-joiner character before जोड़ें.
    - Current: `‌जोड़ें`
    - Source: `Add`
    - Suggest: `जोड़ें`
    - An invisible ZWNJ control character precedes the word, which is not part of the text and can affect rendering; source is simply "Add".
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
- _…and 21 more._

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
| Strings | 2,665 |
| Missing strings | 82 |
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
| Typography deviations from this locale's own norm | 1 |

### Completeness

**82 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — 79
- `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — 2
- `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 13, `straight-double` 1 | **curly-double** |
| apostrophe | `straight` 6 | **straight** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (65)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 35 |
| 3 | Degraded language (grammar, spelling, terminology) | 29 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_awesomebar_stock_suggestion_increase` — `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-hi-rIN/strings.xml` — Translation adds "साइज़" (size), which is not in the source about a stock price gain.
    - Current: `साइज़ %s प्रतिशत बढ़ा`
    - Source: `Gained %s percent`
    - Suggest: `%s प्रतिशत बढ़ा`
    - Source is "Gained %s percent" describing a stock increase; the paired decrease string is correctly "%s प्रतिशत गिरा" with no such word. "साइज़" (size) is invented and inconsistent.
- `mozac_feature_addons_permissions_one_site_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — "Access your data for %1$s" is rendered so it reads as an instruction to the user rather than a permission the add-on requests, and drops "आपका" possessive consistency.
    - Current: `%1$s के लिए अपना डेटा एक्सेस करें।`
    - Source: `Access your data for %1$s.`
    - Suggest: `%1$s के लिए आपका डेटा एक्सेस करना।`
    - This is a permission description listing what the add-on will do; the imperative "एक्सेस करें" tells the user to access their own data, changing who performs the action.
- `mozac_feature_applinks_link_from` — `mozilla-mobile/android-components/components/feature/app-links/src/main/res/values-hi-rIN/strings.xml` — "Link from %s" (origin domain) translated as "link that has %s".
    - Current: `%s वाला लिंक`
    - Source: `Link from %s`
    - Suggest: `%s से आया लिंक`
    - Per the developer comment %s is the domain the link was navigated from; 'वाला लिंक' conveys possession/containment, not origin.
- `mozac_feature_prompts_save_credit_card_prompt_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-hi-rIN/strings.xml` — Demonstrative "this" dropped from "Securely save this card?".
    - Current: `कार्ड को सुरक्षित ढंग से सेव करना है?`
    - Source: `Securely save this card?`
    - Suggest: `इस कार्ड को सुरक्षित ढंग से सेव करना है?`
    - Source says "this card"; the target omits "इस", making it generic.
- `search_widget_content_description` — `mozilla-mobile/android-components/components/feature/search/src/main/res/values-hi-rIN/strings.xml` — Translation says "Open a new tab in %1$s" instead of "Open a new %1$s tab"; minor but the postposition changes meaning slightly.
    - Current: `%1$s में एक नया टैब खोलें`
    - Source: `Open a new %1$s tab`
    - Suggest: `%1$s का एक नया टैब खोलें`
    - Source describes opening a new app-branded tab; the target's locative reading is different, though intelligible.
- `my_longest_fox_is` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-hi-rIN/strings.xml` — "My longest fox is %1$d" is rendered as "My high score is %1$d", losing the game-specific "longest fox" wording.
    - Current: `मेरा हाई-स्कोर %1$d है!`
    - Source: `My longest fox is %1$d! #longfox %2$s`
    - Suggest: `मेरी सबसे लंबी फ़ॉक्स %1$d है!`
    - The developer comment explains the shared text refers to the longest fox achievement (example: "My longest fox is 6! #longfox"); the target substitutes a generic "high score" phrase.
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
- `connection_security_panel_qualified_certificate` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "as specified in Regulation" mistranslated as "according to the information given in Regulation".
    - Current: `में दी गई जानकारी के अनुसार, योग्य है।`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `में निर्दिष्ट के अनुसार योग्य है।`
    - The source says the certificate is qualified as specified in the Regulation; "जानकारी" (information) is not in the source and the added comma breaks the sentence.
- `likert_scale_option_6` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Present tense "I don't use it" rendered as past/perfect "I have not used it".
    - Current: `मैंने इसका इस्तेमाल नहीं किया है`
    - Source: `I don’t use it`
    - Suggest: `मैं इसका इस्तेमाल नहीं करता/करती`
    - Source is present habitual ("I don’t use it"), not past perfect ("I haven't used it").
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "won't sell you out" is rendered as "is trustworthy", dropping the claim about not selling out users.
    - Current: `तेज़, सुरक्षित और भरोसेमंद है।`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `तेज़, सुरक्षित और आपको धोखा नहीं देगा।`
    - The source promises the browser will not sell the user out (i.e., not betray/sell their data); the Hindi merely says it is "trustworthy", which is a different, vaguer claim.
- `preference_doh_exceptions_add_error` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Must be a valid domain" is rendered as "The domain must be correct", losing the requirement that the entry be a domain.
    - Current: `डोमेन सही होना चाहिए`
    - Source: `Must be a valid domain`
    - Suggest: `यह एक मान्य डोमेन होना चाहिए`
    - The source states the input must be a valid domain; the target asserts a domain must be correct, which shifts the meaning of the validation error.
- `preference_option_phone_feature_ask_to_allow` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Ask to allow" rendered as "ask in order to allow" reversing who asks.
    - Current: `अनुमति देने के लिए पूछें`
    - Source: `Ask to allow`
    - Suggest: `अनुमति माँगें`
    - The source means the site must ask the user for permission; the Hindi instructs the user to ask in order to grant permission.
- `preferences_category_about` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "About" rendered as "About us", which is not what the category means.
    - Current: `हमारे बारे में`
    - Source: `About`
    - Suggest: `परिचय`
    - The preference category is 'About' (about the app/Fenix per the developer comment), not 'About us'.
- `preferences_delete_browsing_data_tabs_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Open tabs" (a noun phrase naming the item) is translated as an imperative "Open tabs" command.
    - Current: `टैब खोलें`
    - Source: `Open tabs`
    - Suggest: `खुले टैब`
    - Source is a title for the tabs item in Delete browsing data, i.e. the noun phrase 'open tabs', not an instruction to open tabs.
- `preferences_passwords_save_logins_ask_to_save` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Ask to save" mistranslated as "ask in order to save".
    - Current: `सेव करने के लिए पूछें`
    - Source: `Ask to save`
    - Suggest: `सेव करने से पहले पूछें`
    - The source means the browser should ask the user whether to save the password; "सेव करने के लिए पूछें" reads as "ask in order to save", reversing who asks and why.
- `preferences_pbm_lock_screen_summary_3` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "prevents screen capture and sharing" is rendered as "one can also avoid screen capture and sharing", losing the sense that the feature blocks them.
    - Current: `इसे चालू करने से, स्क्रीन कैप्चर और शेयरिंग से भी बचा जा सकता है।`
    - Source: `View tabs with your fingerprint, PIN, or face unlock. Turning this on also prevents screen capture and sharing.`
    - Suggest: `इसे चालू करने से स्क्रीन कैप्चर और शेयरिंग पर भी रोक लग जाती है।`
    - Source says turning this on prevents (blocks) screen capture and sharing; the Hindi says the user can "avoid" them, which weakens/changes the stated behaviour.
- `preferences_sync_tabs_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Open tabs" (a noun phrase naming the sync item) is translated as the imperative "Open tabs".
    - Current: `टैब खोलें`
    - Source: `Open tabs`
    - Suggest: `खुले टैब`
    - The preference lists what to sync; "Open tabs" is a noun phrase meaning currently open tabs, not a command to open tabs.
- `private_tab_cfr_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Question form is lost/altered: the source asks whether to use a screen lock, while the target reads as an imperative with a question mark.
    - Current: `प्राइवेट टैब छिपाने के लिए स्क्रीन लॉक इस्तेमाल करें?`
    - Source: `Use screen lock to hide private tabs?`
    - Suggest: `प्राइवेट टैब छिपाने के लिए स्क्रीन लॉक इस्तेमाल करें क्या?`
    - Minor, but the phrasing "इस्तेमाल करें?" is ambiguous; source is a yes/no prompt.
- `review_prompt_rate_header` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Got a second to spread the love with a rating?" is rendered as an imperative request with a question mark, losing the "do you have a second" meaning.
    - Current: `कृपया रेटिंग देकर अपनी पसंद जताएं?`
    - Source: `Thanks for loving %1$s. Got a second to spread the love with a rating?`
    - Suggest: `क्या आपके पास रेटिंग देकर अपनी पसंद जताने के लिए एक पल है?`
    - The source asks whether the user has a moment; the target is a command punctuated as a question.
- `saved_logins_menu_dropdown_chevron_icon_content_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Sort passwords menu" is rendered as an imperative "sort the passwords menu" instead of naming the menu.
    - Current: `पासवर्ड मेन्यू सॉर्ट करें`
    - Source: `Sort passwords menu`
    - Suggest: `पासवर्ड सॉर्ट करने का मेन्यू`
    - The source is a noun phrase naming the control (the menu for sorting passwords); the Hindi reads as a command to sort the menu itself, which misdescribes the control for screen-reader users.
- `search_settings_google_lens_description` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Descriptive statement about app behaviour turned into an imperative instruction to the user.
    - Current: `विज़ुअल सर्च के लिए, Google को इमेज और फ़ोटो भेजें।`
    - Source: `Sends images and photos to Google for visual search.`
    - Suggest: `विज़ुअल सर्च के लिए Google को इमेज और फ़ोटो भेजता है।`
    - The source "Sends images and photos to Google" describes what the toggle does; the Hindi imperative tells the user to send images, changing the meaning of the setting description.
- `sent_from_firefox_template` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The translation makes the shared link (%1$s) the sender instead of the app name (%2$s).
    - Current: `%1$s %2$s ने भेजा है`
    - Source: `%1$s  Sent from %2$s 🦊 Try the mobile browser: %3$s`
    - Suggest: `%1$s  %2$s से भेजा गया`
    - Source is "%1$s\n\nSent from %2$s": %1$s is the shared link and %2$s is the app name. Placing "%2$s ने भेजा है" directly after %1$s with no break, and using the agentive "ने", reads as if the link/app combination sent something; the sentence structure loses the "Sent from <app>" footer meaning.
- `sent_from_firefox_template_short` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Word order places the emoji between the app name and the verb, breaking the "Sent from %2$s" phrase.
    - Current: `%1$s %2$s 🦊 ने भेजा है %3$s`
    - Source: `%1$s  Sent from %2$s 🦊 %3$s`
    - Suggest: `%1$s  %2$s से भेजा गया 🦊 %3$s`
    - Source is "%1$s\n\nSent from %2$s 🦊 %3$s". In the target the emoji is inserted inside the phrase "%2$s ने भेजा है", splitting the app name from its verb, and the download link %3$s follows without separation, so the footer no longer reads as "Sent from <app>".
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Search settings" (verb) rendered as the noun phrase "सर्च सेटिंग" (search-related settings).
    - Current: `सर्च सेटिंग`
    - Source: `Search settings`
    - Suggest: `सेटिंग सर्च करें`
    - The developer comment states "Search" is a verb here — the title means to search through the settings. "सर्च सेटिंग" reads as "search settings" i.e. settings for search, the opposite parse.
- `sync_connect_device` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Connect" rendered as "जोड़ें" (add), inconsistent with sync_add_new_device_connect_button which uses "कनेक्ट करें" for the same source phrase.
    - Current: `अन्य डिवाइस जोड़ें`
    - Source: `Connect another device`
    - Suggest: `अन्य डिवाइस कनेक्ट करें`
    - Source "Connect another device" is identical to sync_add_new_device_connect_button, translated there as "अन्य डिवाइस कनेक्ट करें"; terminology should be consistent.
- `sync_send_tab_error_auth_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Translation adds "synced" which the source does not say.
    - Current: `सिंक किए गए डिवाइसों के बीच टैब भेजने के लिए, फिर से साइन इन करें`
    - Source: `Sign back in to send tabs between devices`
    - Suggest: `डिवाइसों के बीच टैब भेजने के लिए फिर से साइन इन करें`
    - Source is "Sign back in to send tabs between devices" — there is no "synced" qualifier.
- `sync_sign_in` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Sign in to Sync" mistranslated as "Sign in in order to sync", losing the reference to the Sync service.
    - Current: `सिंक करने के लिए साइन इन करें`
    - Source: `Sign in to Sync`
    - Suggest: `सिंक में साइन इन करें`
    - Source refers to signing in to the Sync service (capitalized "Sync"), not signing in for the purpose of syncing; compare sync_reconnect "Reconnect to Sync" → "सिंक में फिर से कनेक्ट करें".
- `tracking_protection_off` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — State label "Off" is translated as an imperative command "turn off" instead of the status "Off".
    - Current: `बंद करें`
    - Source: `Off`
    - Suggest: `बंद`
    - Per the developer comment this is the summary of the tracking protection preference showing its current state (Off), parallel to "Standard"/"Strict"/"Custom", not an action button; "बंद करें" means "turn off".
- `translation_settings_always_download` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Word order makes it read as "always download languages in data saving mode" as a restriction to that mode rather than "even when in data saving mode".
    - Current: `भाषाओं को हमेशा डेटा सेविंग मोड में डाउनलोड करें`
    - Source: `Always download languages in data saving mode`
    - Suggest: `डेटा सेविंग मोड में भी भाषाएं हमेशा डाउनलोड करें`
    - The source means downloads are permitted even while data saver is on; the Hindi placement of हमेशा before "in data saving mode" implies downloading always happens in data saving mode.
- `uninstall_survey_option_1_v2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "or" rendered as "and", changing the survey option's meaning.
    - Current: `यह धीमा है और भरोसेमंद नहीं है`
    - Source: `It’s slow or unreliable`
    - Suggest: `यह धीमा है या भरोसेमंद नहीं है`
    - Source is "It’s slow or unreliable" (either/or), but the Hindi asserts both conditions together with "और" (and).
- `webcompat_reporter_problem_description_placeholder_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — The last sentence invents "so it can be understood where the problem occurred" instead of "steps to reproduce the issue".
    - Current: `कृपया सिलसिलेवार ढंग से एक-एक चरण की जानकारी दें, ताकि समझा जा सके कि समस्या कहां पर आई।`
    - Source: `What happened? What did you expect to happen? Please provide steps to reproduce the issue.`
    - Suggest: `कृपया समस्या को दोहराने के चरण बताएँ।`
    - Source asks for steps to reproduce the issue; the target adds an unsourced purpose clause and drops the notion of reproducing the problem.
- `webcompat_reporter_reason_checkout` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — Negation dropped: the reason reads "payment, checkout or shopping is working" instead of "Can't pay, check out or shop".
    - Current: `पेमेंट, चेकआउट या खरीदारी हो पा रही है`
    - Source: `Can’t pay, check out or shop`
    - Suggest: `पेमेंट, चेकआउट या खरीदारी नहीं हो पा रही है`
    - Source is "Can’t pay, check out or shop"; the Hindi omits "नहीं", reversing the meaning of this broken-site reason option.
- `webcompat_reporter_screen_title` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — "Report broken site" rendered as "report the site being broken/damaged" rather than reporting a site that does not work properly.
    - Current: `साइट खराब होने की रिपोर्ट करें`
    - Source: `Report broken site`
    - Suggest: `खराब साइट की रिपोर्ट करें`
    - The source is a noun-phrase title 'Report broken site'; the translation shifts it to reporting the event of the site becoming broken.
- `preference_autocomplete_add_confirmation` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "custom URL" translated as "उपभोक्ता संशोधित URL" (consumer-modified URL), adding a meaning not in the source.
    - Current: `नया उपभोक्ता संशोधित URL जोड़ा गया।`
    - Source: `New custom URL added.`
    - Suggest: `नया कस्टम URL जोड़ा गया।`
    - The source says "New custom URL added."; "उपभोक्ता संशोधित" (consumer/user-modified) is not the meaning of "custom" here and is inconsistent with the add action string.
- `preference_autocomplete_add_error` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Double-check" rendered literally as "दोहरी जाँच" (a check that is double), losing the meaning "verify again".
    - Current: `आपके द्वारा दर्ज URL की दोहरी जाँच करें।`
    - Source: `Double-check the URL you entered.`
    - Suggest: `आपके द्वारा दर्ज किए गए URL की दोबारा जाँच करें।`
    - Source asks the user to re-verify the entered URL; "दोहरी जाँच" is a literal calque that does not convey "check again".
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Translation adds "उपभोक्ता" (consumer/user), which is not in the source "Remove custom URLs".
    - Current: `उपभोक्ता संशोधित URL हटाएँ`
    - Source: `Remove custom URLs`
    - Suggest: `मनपसंद URL हटाएँ`
    - The source says only "Remove custom URLs"; "उपभोक्ता संशोधित" (consumer-modified) introduces content not present and is inconsistent with preference_autocomplete_title_add.
- `preference_category_advanced` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Advanced" translated as "विस्तृत" (detailed/extensive) instead of the standard "उन्नत".
    - Current: `विस्तृत`
    - Source: `Advanced`
    - Suggest: `उन्नत`
    - The category is Advanced settings; "विस्तृत" means detailed/broad, not advanced. "उन्नत" is already used for Enhanced/Advanced elsewhere in the same file.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "provide and improve %1$s for everyone" is rendered as "make %1$s better and make it available to all", altering the meaning.
    - Current: `%1$s को बेहतर बनाने और सबको उपलब्ध कराने के लिए`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `सबके लिए %1$s को उपलब्ध कराने और बेहतर बनाने के लिए`
    - In the source, "for everyone" modifies both provide and improve; the translation splits it so that only availability applies to everyone, changing what Mozilla claims about data collection purpose.
- `preference_performance_block_webfonts` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "Web fonts" translated as "वेब लिपियों" (web scripts), not fonts.
    - Current: `वेब लिपियों को अवरुद्ध करें`
    - Source: `Block web fonts`
    - Suggest: `वेब फ़ॉन्ट अवरुद्ध करें`
    - en-US "web fonts" refers to fonts; "लिपि" means script/writing system (and is commonly read as 'script' i.e. code), which names the wrong thing.
- `preference_safe_browsing_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "potentially dangerous" rendered as plain "ख़तरनाक" and "deceptive" as "संदेहास्पद" (suspicious).
    - Current: `ख़तरनाक और संदेहास्पद साइटों को ब्लॉक करें`
    - Source: `Block potentially dangerous and deceptive sites`
    - Suggest: `संभावित रूप से ख़तरनाक और भ्रामक साइटों को ब्लॉक करें`
    - Source hedges with "potentially" and uses "deceptive" (भ्रामक, as translated in the related summary string); the target asserts sites are dangerous and merely 'suspicious', dropping meaning and breaking consistency with preference_safe_browsing_summary.
- `search_add_confirmation` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — "added" is rendered as "संकलित" (compiled/collected), not "जोड़ा गया".
    - Current: `नया खोज इंजन संकलित।`
    - Source: `New search engine added.`
    - Suggest: `नया खोज इंजन जोड़ा गया।`
    - The source says a new search engine was added; "संकलित" means compiled/collected, which is a different action.

### C. Grammar, agreement & spelling

- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — Typo in "अपेडट" (should be "अपडेट").
    - Current: `एड्रेस अपेडट करना है?`
    - Source: `%1$s requests additional data collection`
    - Suggest: `एड्रेस अपडेट करना है?`
    - The word for "Update" is misspelled as अपेडट instead of अपडेट.
- `mozac_summarize_info_error_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "नहींं" has a doubled anusvara/chandrabindu.
    - Current: `अभी सारांश नहींं बनाया जा सकता`
    - Source: `Can’t summarize right now`
    - Suggest: `अभी सारांश नहीं बनाया जा सकता`
    - The word for "not" is spelled नहीं; the target has an extra nasal mark producing "नहींं".
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
- `preference_show_search_suggestions_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Sentence structure garbles the meaning: "will send them to your search engine which you type in the address bar".
    - Current: `%1$s उन्हें आपके खोज इंजन में भेजेगा जिन्हें आप पता बार में टाइप करेंगे`
    - Source: `%1$s will send what you type in the address bar to your search engine`
    - Suggest: `%1$s आप पता बार में जो टाइप करेंगे उसे आपके खोज इंजन को भेजेगा`
    - The source says the app sends what you type in the address bar to your search engine; the Hindi puts the relative clause after the object pronoun, producing an ungrammatical/confusing sentence.
- `preference_switch_autocomplete_user_list` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Missing participle inflection in "जोड़े साइटों".
    - Current: `आपके द्वारा जोड़े साइटों के लिए`
    - Source: `For sites you add`
    - Suggest: `आपके द्वारा जोड़ी गई साइटों के लिए`
    - "For sites you add" requires a proper relative participle; "जोड़े साइटों" is ungrammatical.
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — The translation misrenders "never save and cannot restore" as "can never save and restore", breaking the verb agreement and the meaning of the first clause.
    - Current: `हम इस टैब को कभी भी सहेज तथा दुबारा प्राप्त नहीं कर सकते हैं।`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `हम इस टैब को कभी सहेजते नहीं हैं और इसे दुबारा प्राप्त नहीं कर सकते हैं।`
    - en-US states two facts: the browser never saves the tab, and it cannot restore it. The Hindi collapses them into "cannot ever save and restore", changing the first statement.
- `trackers_count_note` — `mozilla-mobile/focus-android/app/src/main/res/values-hi-rIN/strings.xml` — Spelling error: "अवरूद्ध" should be "अवरुद्ध".
    - Current: `%s से ट्रैकर अवरूद्ध`
    - Source: `Trackers blocked since %s`
    - Suggest: `%s से ट्रैकर अवरुद्ध`
    - The correct Hindi spelling uses short u (ु) in अवरुद्ध.

### D. Terminology, register & consistency

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — `mozac_browser_errorpages_offline_message` quotes “फिर से कोशिश करें” but the string it names, `mozac_browser_errorpages_page_refresh`, reads “फिर कोशिश करें”
    - Current: `{ <p> }ब्राउज़र ऑफ़लाइन मोड में चल रहा है और अनुरोध किए गए आइटम से कनेक्ट नहीं हो सकता है।{ </p> } { <ul> } { <li> }क्या डिवाइस किसी एक्टिव नेटवर्क से जुड़ा हुआ है?{ </li> } { <li> }ऑनलाइन मोड में जाने और पेज को फिर से लो…`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `फिर कोशिश करें`
    - In the source this string quotes “Try Again”, which is exactly the value of `mozac_browser_errorpages_page_refresh` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
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

- `add_login_hostname_invalid_text_3` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — `add_login_hostname_invalid_text_3` uses straight double quotes
    - Current: `वेब एड्रेस में "https://" या "http://" ज़रूर होना चाहिए`
    - Source: `Web address must contain “https://” or “http://”`
    - The locale's quote convention is `curly-double` (13 occurrences).

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

### Fixed to date (179)

- `mozac_browser_errorpages_archive_retry` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_errorpages_archive_unreachable` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_errorpages_file_not_found_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_errorpages_malformed_uri_message_alternative` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_browser_toolbar_content_description_autoplay_blocked` — `mozilla-mobile/android-components/components/browser/toolbar/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions_devtools_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions_devtools_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions_dialog_heading_optional_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions_extra_domains_description_plural_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions_extra_sites_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions_one_extra_domain_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions_one_extra_site_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_addons_permissions_one_site_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_extensions_manager_notification_title_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_autofill_confirmation_no` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_contextmenu_snackbar_link_text_copied` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_downloads_dialog_download_again` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_findindpage_input` — `mozilla-mobile/android-components/components/feature/findinpage/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_ipprotection_unavaliable_dialog_body` — `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_readerview_font_size_decrease_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_readerview_font_size_increase_desc` — `mozilla-mobile/android-components/components/feature/readerview/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_sitepermissions_option_microphone_one` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_feature_summarize_feedback_state_submitted` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_lib_gathering_crash_data_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `mozac_open_tab_counter_tab_tray` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `addon_failure_retry_action` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `addons_does_not_require_permissions` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `addons_permissions_required_data_collection_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `applinks_prompt_negative_button` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `automatic_translation_option_never_translate_summary_preference` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `browser_menu_library` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `browser_toolbar_url_copied_to_clipboard_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `certificate_warning_homepage_card_hcw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `connection_security_panel_issued_to` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `crash_reporting_snack_bar_message` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `debug_drawer_tab_tools_tab_quantity_non_digits_error` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
- `deleting_browsing_data_in_progress` — `mozilla-mobile/fenix/app/src/main/res/values-hi-rIN/strings.xml` — fixed 2026-09-15
