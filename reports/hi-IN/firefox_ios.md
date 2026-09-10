# Firefox iOS l10n QA — hi-IN

| | |
|---|---|
| **Generated** | 2026-09-10 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `4e8024d287e9` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `4e8024d287e9` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 602 of 602 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.




---

## Changes in this run

### 🆕 New findings (79)

- `NSMicrophoneUsageDescription` — `hi-IN/firefox-ios.xliff` — Microphone permission description translated as taking and uploading videos, omitting Firefox and the microphone/audio recording purpose.
    - Current: `यह आपको वीडियो लेने और अपलोड करने देता है।`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `Firefox ऑडियो रिकॉर्ड करने और अपलोड करने के लिए आपके माइक्रोफ़ोन का उपयोग करता है।`
    - en-US says "Firefox uses your microphone to record and upload audio." The target states it lets you take and upload video, which is a different permission purpose and drops the brand name.
- `Bookmarks.DeleteFolderWarning.Title` — `hi-IN/firefox-ios.xliff` — Number agreement error: singular subject with plural verb form.
    - Current: `यह फोल्डर खाली नहीं हैं।`
    - Source: `This folder isn’t empty.`
    - Suggest: `यह फोल्डर खाली नहीं है।`
    - "This folder isn’t empty" is singular; हैं is the plural form and should be है.
- `DefaultBrowserOnboarding.Description2` — `hi-IN/firefox-ios.xliff` — "Tap Default Browser App" mistranslated as "tap as default browser", losing the name of the settings item.
    - Current: `2. डिफ़ॉल्ट ब्राउज़र के रूप में टैप करें`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. तयशुदा ब्राउज़र ऐप पर टैप करें`
    - The source instructs the user to tap the iOS settings row named "Default Browser App"; the target says to tap "as default browser", which is not an instruction the user can follow.
- `Use your fingerprint to access Logins now.` — `hi-IN/firefox-ios.xliff` — "access Logins" rendered as "to log in", changing the meaning.
    - Current: `अब लॉगिन करने के लिए अपने फिंगरप्रिंट का उपयोग करें।`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `अब लॉगिन तक पहुँचने के लिए अपने फिंगरप्रिंट का उपयोग करें।`
    - The source refers to accessing the saved Logins list, not to performing a login.
- `Send to Device` — `hi-IN/firefox-ios.xliff` — "Device" translated as उपकरण here but as डिवाइस in the sibling string on the same screen.
    - Current: `उपकरण में भेजें`
    - Source: `Send to Device`
    - Suggest: `डिवाइस पर भेजें`
    - Menu.SendLinkToDevice in the same file uses डिवाइस ... पर भेजें; the inconsistent term and postposition on the same feature is a terminology inconsistency.
- `This action will clear all of your private data, including history from your synced devices.` — `hi-IN/firefox-ios.xliff` — Misspelling of निजी as निज़ी.
    - Current: `निज़ी`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `निजी`
    - The correct Hindi spelling is निजी (as used in the ClearPrivateDataConfirm string); the nukta form निज़ी is incorrect.
- `ActivityStream.ContextMenu.AddToShortcuts` — `hi-IN/firefox-ios.xliff` — "Add to Shortcuts" is translated as "Add to contacts".
    - Current: `संपर्क में जोड़ें`
    - Source: `Add to Shortcuts`
    - Suggest: `शॉर्टकट में जोड़ें`
    - The source refers to pinning a site to Shortcuts; "संपर्क" means contacts, which names the wrong feature.
- `Next in-page result` — `hi-IN/firefox-ios.xliff` — Postposition "मे" is misspelled (should be "में") and the phrase is garbled.
    - Current: `पृष्ठ परिणाम मे अगला`
    - Source: `Next in-page result`
    - Suggest: `पृष्ठ में अगला परिणाम`
    - en-US means "next result within the page"; the target reads "next in page results" with a misspelled postposition (मे instead of में).
- `Previous in-page result` — `hi-IN/firefox-ios.xliff` — Postposition "मे" is misspelled (should be "में") and the phrase is garbled.
    - Current: `पृष्ठ परिणाम मे पिछला`
    - Source: `Previous in-page result`
    - Suggest: `पृष्ठ में पिछला परिणाम`
    - en-US means "previous result within the page"; target uses misspelled मे and reverses the noun structure.
- `Find in Page` — `hi-IN/firefox-ios.xliff` — Misspelled postposition "मे" instead of "में".
    - Current: `पृष्ठ मे ढूंढें`
    - Source: `Find in Page`
    - Suggest: `पृष्ठ में ढूंढें`
    - Hindi locative postposition requires the anusvara: में.
- `Added page to Reading List` — `hi-IN/firefox-ios.xliff` — Misspelled postposition "मे" instead of "में".
    - Current: `पठन सूची मे पृष्ठ जोड़ दिया गया`
    - Source: `Added page to Reading List`
    - Suggest: `पठन सूची में पृष्ठ जोड़ दिया गया`
    - Hindi locative postposition requires the anusvara: में.
- `ActivityStream.JumpBackIn.SectionTitle` — `hi-IN/firefox-ios.xliff` — "Jump Back In" rendered literally as "go back inside", losing the meaning of resuming a recent tab.
    - Current: `वापस अंदर जायें`
    - Source: `Jump Back In`
    - Suggest: `वहीं से जारी रखें`
    - The section lets users resume recently viewed tabs; the literal "go back inside" conveys no such meaning.
- `BreachAlerts.Link` — `hi-IN/firefox-ios.xliff` — "Go to" rendered with the informal/imperative "जाओ", which breaks the polite register used elsewhere in the app.
    - Current: `जाओ`
    - Source: `Go to`
    - Suggest: `इस पर जाएं`
    - The en-US "Go to" leads to the breached website; other similar strings use the polite "जाएं" (e.g. ClipboardToast.GoToCopiedLink.Button). "जाओ" is the familiar/rude imperative form and is inconsistent with the app's register.
- `Changes color theme.` — `hi-IN/firefox-ios.xliff` — Accessibility hint translated as a noun phrase "रंग थीम परिवर्तन।" instead of the verb form used in the parallel string.
    - Current: `रंग थीम परिवर्तन।`
    - Source: `Changes color theme.`
    - Suggest: `रंग थीम बदलें।`
    - The source "Changes color theme." is a hint describing an action, and the parallel string "Changes font type." is translated as "फ़ॉन्ट प्रकार बदलें।"; the noun form is grammatically incomplete and inconsistent.
- `Bookmarks.NewFolder.Label` — `hi-IN/firefox-ios.xliff` — "फोल्डर" spelled without nukta, inconsistent with "फ़ोल्डर" used in the other folder strings.
    - Current: `नया फोल्डर`
    - Source: `New Folder`
    - Suggest: `नया फ़ोल्डर`
    - Bookmarks.Folder.Label and Bookmarks.EditFolder.Label use "फ़ोल्डर"; this string drops the nukta, creating a spelling/consistency error on the same screen.
- `Could not add page to Reading list` — `hi-IN/firefox-ios.xliff` — "मे" is misspelled; should be "में".
    - Current: `पृष्ठ को पठन सूची मे नहीं जोड़ा जा सकता है`
    - Source: `Could not add page to Reading list`
    - Suggest: `पृष्ठ को पठन सूची में नहीं जोड़ा जा सका`
    - The postposition is spelled "में"; also the source is past tense ("Could not add"), while the target uses present ability "जोड़ा जा सकता है".
- `CoverSheet.v24.ETP.Description` — `hi-IN/firefox-ios.xliff` — Misspelling of "अंतर्निहित" and gender/number agreement error in "आपका पीछा करने वाली विज्ञापनों".
    - Current: `अंतनिर्हित उन्नत ट्रैकिंग सुरक्षा आपका पीछा करने वाली विज्ञापनों को रोकने में मदद करता है`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `अंतर्निहित उन्नत ट्रैकिंग सुरक्षा आपका पीछा करने वाले विज्ञापनों को रोकने में मदद करती है`
    - "अंतनिर्हित" is a misspelling of "अंतर्निहित" (Built-in); "विज्ञापनों" is masculine plural so it needs "वाले", and "सुरक्षा" is feminine so the verb should be "करती है".
- `CoverSheet.v24.ETP.Title` — `hi-IN/firefox-ios.xliff` — "Ad Tracking" rendered as "विज्ञापन की निगरानी" (surveillance) instead of the app's established term for tracking.
    - Current: `विज्ञापन की निगरानी के विरुद्ध सुरक्षा`
    - Source: `Protection Against Ad Tracking`
    - Suggest: `विज्ञापन ट्रैकिंग के विरुद्ध सुरक्षा`
    - The related description string uses "ट्रैकिंग" and "ट्रैकर्स" for tracking; using "निगरानी" here is inconsistent terminology for the same feature screen.
- `ErrorPages.CertWarning.Description` — `hi-IN/firefox-ios.xliff` — "owner" is translated as "उत्तराधिकारी" (heir/successor) instead of "स्वामी/मालिक" (owner).
    - Current: `%@ के उत्तराधिकारी ने`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `%@ के स्वामी ने`
    - en-US says "The owner of %@"; उत्तराधिकारी means heir/successor, not owner.
- `Downloads.CancelDialog.Resume` — `hi-IN/firefox-ios.xliff` — "Resume" rendered as "पुनः चलाएं" (play again/restart) rather than resuming the download.
    - Current: `पुनः चलाएं`
    - Source: `Resume`
    - Suggest: `फिर शुरू करें`
    - The button declines cancellation and continues the download; "पुनः चलाएं" suggests restarting/playing again rather than resuming.
- `Forward` — `hi-IN/firefox-ios.xliff` — Toolbar Forward navigation button translated as "आगे बढ़ाएं" (to forward/advance something) instead of "आगे".
    - Current: `आगे बढ़ाएं`
    - Source: `Forward`
    - Suggest: `आगे`
    - The string is the accessibility label for the tab toolbar Forward navigation button; "आगे बढ़ाएं" is transitive (move something forward), not the navigation direction.
- `Enter your password to connect` — `hi-IN/firefox-ios.xliff` — Misspelling: "दर्ज़" should be "दर्ज".
    - Current: `दर्ज़ करें`
    - Source: `Enter your password to connect`
    - Suggest: `दर्ज करें`
    - The Hindi word is दर्ज, without nukta on ज.
- `FxAPush_DeviceConnected_body` — `hi-IN/firefox-ios.xliff` — The notification body reverses the direction of the connection.
    - Current: `Firefox सिंक %@ में जोड़ा गया`
    - Source: `Firefox Sync has connected to %@`
    - Suggest: `Firefox सिंक %@ से जुड़ गया है`
    - Source says Firefox Sync has connected to the named device; the Hindi says "Firefox Sync was added into %@", which states something different.
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `hi-IN/firefox-ios.xliff` — Ungrammatical verb form: intransitive subject with transitive causative construction.
    - Current: `एक उपकरण Firefox सिंक से डिस्कनेक्ट कर दिया है`
    - Source: `A device has disconnected from Firefox Sync`
    - Suggest: `एक उपकरण Firefox सिंक से डिस्कनेक्ट हो गया है`
    - Source is "A device has disconnected from Firefox Sync"; the Hindi "डिस्कनेक्ट कर दिया है" is grammatically incorrect for this subject.
- `HistoryPanel.EmptySyncedTabsPanelNotSignedInState.Description` — `hi-IN/firefox-ios.xliff` — Misattaches "from your other devices" to the sign-in action rather than to the tabs.
    - Current: `टैब की सूची देखने के लिए अपने दूसरे उपकरणों से साइन इन करें।`
    - Source: `Sign in to view a list of tabs from your other devices.`
    - Suggest: `अपने अन्य उपकरणों के टैब की सूची देखने के लिए साइन इन करें।`
    - Source: "Sign in to view a list of tabs from your other devices." The Hindi tells the user to sign in from their other devices, which is not what the source says.
- `HistoryPanel.ClearHistoryMenuOptionTodayAndYesterday` — `hi-IN/firefox-ios.xliff` — "कल" is ambiguous and here reads as tomorrow/yesterday without disambiguation.
    - Current: `आज और कल`
    - Source: `Today and Yesterday`
    - Suggest: `आज और बीता कल`
    - Source is "Today and Yesterday"; "कल" alone means both yesterday and tomorrow in Hindi, so for a clear-history range it must be disambiguated as past.
- `Hotkeys.Forward.DiscoveryTitle` — `hi-IN/firefox-ios.xliff` — "Forward" navigation rendered as a transitive "move forward/advance something" verb.
    - Current: `आगे बढ़ाएं`
    - Source: `Forward`
    - Suggest: `आगे`
    - Paired with "Back" (पीछे) as a navigation shortcut label; "आगे बढ़ाएं" means to advance/promote something else.
- `Hotkeys.ShowPreviousTab.DiscoveryTitle` — `hi-IN/firefox-ios.xliff` — "Previous Tab" translated as "previous page" instead of tab.
    - Current: `पिछला पृष्ठ दिखाएं`
    - Source: `Show Previous Tab`
    - Suggest: `पिछला टैब दिखाएँ`
    - Source says "Show Previous Tab"; टैब (tab) was rendered as पृष्ठ (page), inconsistent with the sibling string "अगला टैब दिखाएं".
- `LoginsList.Title` — `hi-IN/firefox-ios.xliff` — "SAVED LOGINS" (a plural list title) is rendered as singular "login saved", reading like a status message rather than a list heading.
    - Current: `लॉग इन सहेजा गया`
    - Source: `SAVED LOGINS`
    - Suggest: `सहेजे गए लॉगिन`
    - The source is a title for the list of logins (plural noun phrase), not a past-tense confirmation that a login was saved.
- `Looks like Firefox crashed previously. Would you like to restore your tabs?` — `hi-IN/firefox-ios.xliff` — "restore your tabs" is translated as "पूर्ववत करना" (undo), and "crashed" as "नष्ट हो गया" (was destroyed).
    - Current: `ऐसा लगता है जैसे कि Firefox पूर्व में नष्ट हो गया। क्या आप अपने टैब को पूर्ववत करना चाहेंगे?`
    - Source: `Looks like Firefox crashed previously. Would you like to restore your tabs?`
    - Suggest: `ऐसा लगता है कि Firefox पिछली बार क्रैश हो गया था। क्या आप अपने टैब पुनर्स्थापित करना चाहेंगे?`
    - "पूर्ववत करना" means to undo, not to restore tabs; "नष्ट हो गया" means destroyed, not crashed.
- `Menu.ReloadWithoutTrackingProtection.Title` — `hi-IN/firefox-ios.xliff` — "Reload" is rendered as just "लोड करें" (load), losing the "re-" and diverging from the parallel string.
    - Current: `ट्रैकिंग सुरक्षा के बिना लोड करें`
    - Source: `Reload Without Tracking Protection`
    - Suggest: `ट्रैकिंग सुरक्षा के बिना फिर से लोड करें`
    - The companion string Menu.ReloadWithTrackingProtection.Title uses "फिर से लोड करें" for Reload; here it says only "load".
- `Menu.ReadingList.Label` — `hi-IN/firefox-ios.xliff` — "Reading List" translated as "पाठ सूची" (text/lesson list), inconsistent with "पठन सूची" used in Menu.AddToReadingList.Confirm.
    - Current: `पाठ सूची`
    - Source: `Reading List`
    - Suggest: `पठन सूची`
    - Same source term rendered two different ways in the same menu group; "पाठ" means lesson/text, not reading.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `hi-IN/firefox-ios.xliff` — "Blocking this" translated as "इसे बाधित करने से" (obstructing/interrupting) instead of blocking.
    - Current: `इसे बाधित करने से`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `इसे अवरोधित करने से`
    - "Block" in tracking protection context should be "अवरोधित करना"; "बाधित" means obstruct/interrupt.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `hi-IN/firefox-ios.xliff` — "drain your battery" translated as "बैटरी को ख़राब करती है" (damages your battery).
    - Current: `आपकी बैटरी को ख़राब करती है`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `आपकी बैटरी खत्म करती है`
    - The source says the scripts drain the battery, not that they damage/spoil it.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `hi-IN/firefox-ios.xliff` — Subject-verb agreement error: plural "सोशल नेटवर्क" takes singular verb "रखता है".
    - Current: `सोशल नेटवर्क ट्रैकर को अन्य वेबसाइटों पर आपके पूर्ण और लक्षित प्रोफ़ाइल के निर्माण के लिए रखता है।`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `सोशल नेटवर्क आपकी अधिक पूर्ण और लक्षित प्रोफ़ाइल बनाने के लिए अन्य वेबसाइटों पर ट्रैकर रखते हैं।`
    - "Social networks place trackers" is plural in the source; the Hindi verb is singular and the possessive gender is wrong (प्रोफ़ाइल is feminine).
- `Oops! Firefox crashed` — `hi-IN/firefox-ios.xliff` — "crashed" is rendered as "नष्ट हो गया" (was destroyed), which is not the software sense of crashing.
    - Current: `उफ़! Firefox नष्ट हो गया`
    - Source: `Oops! Firefox crashed`
    - Suggest: `उफ़! Firefox क्रैश हो गया`
    - The source says the app crashed; "नष्ट हो गया" means it was destroyed/annihilated, telling the user the product destroyed itself rather than that it stopped unexpectedly.
- `Open Tabs` — `hi-IN/firefox-ios.xliff` — "Open Tabs" (a noun phrase naming the syncing category) is translated as the imperative "टैब खोलें" (Open the tabs).
    - Current: `टैब खोलें`
    - Source: `Open Tabs`
    - Suggest: `खुले टैब`
    - The developer comment says this is a toggle for the tabs syncing setting, so "Open Tabs" is the noun "tabs that are open", not a command.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `hi-IN/firefox-ios.xliff` — Ungrammatical phrase "अपने कैमरा रोल करने में" mangles "to your Camera Roll".
    - Current: `यह आपको अपने कैमरा रोल करने में चित्रों को सहेजने की अनुमति देता है।`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `यह आपको चित्रों को अपने कैमरा रोल में सहेजने की अनुमति देता है।`
    - The postposition sequence is broken; the source means saving the image to the Camera Roll.
- `OpenURL.Error.Message` — `hi-IN/firefox-ios.xliff` — Spelling/agreement errors: "नही" should be "नहीं" and "सकता हैं" should be "सकता है".
    - Current: `Firefox पृष्ठ को नही खोल सकता हैं`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `Firefox पृष्ठ को नहीं खोल सकता है`
    - "नही" is a misspelling of "नहीं", and the plural verb "हैं" does not agree with the singular subject.
- `PhotoLibrary.FirefoxWouldLikeAccessTitle` — `hi-IN/firefox-ios.xliff` — Verb agreement error: singular subject Firefox takes "चाहता है", not the plural "चाहेंगे".
    - Current: `Firefox आपके फ़ोटो को एक्सेस करना चाहेंगे`
    - Source: `Firefox would like to access your Photos`
    - Suggest: `Firefox आपकी फ़ोटो एक्सेस करना चाहता है`
    - "चाहेंगे" is plural/future and does not agree with the singular subject Firefox.
- `RecentlyClosedTabsPanel.Title` — `hi-IN/firefox-ios.xliff` — Translation adds "टैब" not present in the source "Recently Closed".
    - Current: `हाल ही में बंद किए टैब`
    - Source: `Recently Closed`
    - Suggest: `हाल ही में बंद किए गए`
    - The source title is just "Recently Closed"; the added noun changes the label and lengthens a panel title.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `hi-IN/firefox-ios.xliff` — "Reading List" is rendered "पाठ्य सूची", inconsistent with "पठन सूची" used elsewhere for the same term.
    - Current: `अपनी पाठ्य सूची में`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `अपनी पठन सूची में`
    - The same source term "Reading List" is translated "पठन सूची" in the Reading list and Remove from Reading List strings.
- `Reader View` — `hi-IN/firefox-ios.xliff` — "Reader View" rendered as "पाठक परिदृश्य" while another string uses "पाठक दृश्य" for the same term.
    - Current: `पाठक परिदृश्य`
    - Source: `Reader View`
    - Suggest: `पाठक दृश्य`
    - Inconsistent rendering of the same UI feature name within the same file (see "पाठक दृश्य" in the Reader View tip string).
- `Send Report` — `hi-IN/firefox-ios.xliff` — "Send Report" is translated as "Send details/description" instead of "report".
    - Current: `विवरण भेजें`
    - Source: `Send Report`
    - Suggest: `रिपोर्ट भेजें`
    - en-US "Send Report" refers to sending a crash report; "विवरण" means details/description, not a report.
- `Send a crash report so Mozilla can fix the problem?` — `hi-IN/firefox-ios.xliff` — Gender agreement error: "एक विवरण" with feminine "एक" plus wrong term for "report".
    - Current: `खराबी की एक विवरण भेजें`
    - Source: `Send a crash report so Mozilla can fix the problem?`
    - Suggest: `क्रैश रिपोर्ट भेजें`
    - "विवरण" is masculine so "एक विवरण" mismatches the feminine article usage, and "report" should be रिपोर्ट as in the button label; also keeps terminology consistent with the Send Report button.
- `Settings.AddCustomEngine` — `hi-IN/firefox-ios.xliff` — Misspelling of "इंजन" as "ईंजन".
    - Current: `खोज ईंजन जोड़ें`
    - Source: `Add Search Engine`
    - Suggest: `खोज इंजन जोड़ें`
    - The standard Hindi transliteration used elsewhere in this file (Search.ThirdPartyEngines.AddMessage) is "इंजन"; "ईंजन" is a spelling error and inconsistent.
- `Settings.AddCustomEngine.Title` — `hi-IN/firefox-ios.xliff` — Misspelling of "इंजन" as "ईंजन".
    - Current: `खोज ईंजन जोड़ें`
    - Source: `Add Search Engine`
    - Suggest: `खोज इंजन जोड़ें`
    - The standard Hindi spelling used elsewhere in this file is "इंजन"; "ईंजन" is misspelled and inconsistent.
- `Search.ThirdPartyEngines.AddSuccess` — `hi-IN/firefox-ios.xliff` — "Search engine" rendered as "सर्च इंजन" while the rest of the screen uses "खोज इंजन".
    - Current: `सर्च इंजन जोड़ा गया!`
    - Source: `Added Search engine!`
    - Suggest: `खोज इंजन जोड़ा गया!`
    - Neighbouring strings (AddMessage, DuplicateErrorMessage, Settings.AddCustomEngine) translate "search engine" as "खोज इंजन"; this transliteration is inconsistent on the same feature.
- `Settings.AddCustomEngine.URLPlaceholder` — `hi-IN/firefox-ios.xliff` — The instruction "Replace Query with %s" is reversed: the Hindi says "replace with %s" and drops the object "Query".
    - Current: `URL (%s के साथ बदलें)`
    - Source: `URL (Replace Query with %s)`
    - Suggest: `URL (क्वेरी को %s से बदलें)`
    - Source tells the user to replace the search query in the URL with the token %s; the translation omits "Query" and reads as an instruction to replace something unspecified with %s.
- `Settings.Disconnect.Title` — `hi-IN/firefox-ios.xliff` — "Disconnect Sync?" is rendered without "Sync".
    - Current: `डिस्कनेक्ट करें?`
    - Source: `Disconnect Sync?`
    - Suggest: `सिंक डिस्कनेक्ट करें?`
    - The source specifies disconnecting Sync; the translation drops the object, and is also identical to the plain "Disconnect" button string.
- `Settings.Disconnect.Button` — `hi-IN/firefox-ios.xliff` — "Disconnect Sync" is translated as just "Disconnect", losing "Sync".
    - Current: `डिस्कनेक्ट करें`
    - Source: `Disconnect Sync`
    - Suggest: `सिंक डिस्कनेक्ट करें`
    - Source is "Disconnect Sync"; the translation is identical to the separate "Disconnect" string and omits the Sync object.
- `Settings.Home.Option.StartAtHome.AfterFourHours` — `hi-IN/firefox-ios.xliff` — Word order makes the phrase ungrammatical in Hindi.
    - Current: `मुखपृष्ठ चार घंटे की निष्क्रियता के बाद`
    - Source: `Homepage after four hours of inactivity`
    - Suggest: `चार घंटे की निष्क्रियता के बाद मुखपृष्ठ`
    - Hindi postpositional phrases precede the noun; the English word order was copied literally, producing an ungrammatical label.
- `Settings.SendUsage.Message` — `hi-IN/firefox-ios.xliff` — Translation is ungrammatical and loses the meaning "to provide and improve Firefox for everyone".
    - Current: `तथा Firefox को सभी के लिए बेहतर बनता है।`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `तथा Firefox को सभी के लिए बेहतर बनाने के लिए ज़रूरी है।`
    - The source says Mozilla collects only what it needs to provide and improve Firefox for everyone; the target reads "...and Firefox becomes better for everyone" with the intransitive 'बनता है' not agreeing with 'Firefox को', making the sentence grammatically broken and changing the meaning.
- `Settings.SendUsage.Title` — `hi-IN/firefox-ios.xliff` — "उपयोगित" is not a valid Hindi word for "Usage".
    - Current: `उपयोगित डेटा भेजें`
    - Source: `Send Usage Data`
    - Suggest: `उपयोग डेटा भेजें`
    - "Send Usage Data" should be "उपयोग डेटा" or "उपयोग संबंधी डेटा"; "उपयोगित" is a misspelling/non-word.
- `Settings.Home.Option.StartAtHome.Title` — `hi-IN/firefox-ios.xliff` — Gender agreement error: स्क्रीन is feminine, so the modifier must be खुलती हुई.
    - Current: `खुलता हुआ स्क्रीन`
    - Source: `Opening screen`
    - Suggest: `प्रारंभिक स्क्रीन`
    - "Opening screen" — the adjective phrase does not agree with the feminine noun स्क्रीन; also the literal progressive rendering is wrong for the meaning of the initial screen shown at launch.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `hi-IN/firefox-ios.xliff` — Descriptive statement turned into an imperative command, changing the meaning.
    - Current: `कुछ विज्ञापन ट्रैकर्स को अनुमति दें ताकि वेबसाइटें सही तरह से कार्य कर सकें।`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `कुछ विज्ञापन ट्रैकिंग की अनुमति देता है ताकि वेबसाइटें सही तरह से कार्य कर सकें।`
    - The source is a description ('Allows some ad tracking so websites function properly'), not an instruction to the user; the sibling strict-level description correctly uses the descriptive 'ब्लॉक करता है'.
- `Settings.WebsiteData.ConfirmPrompt` — `hi-IN/firefox-ios.xliff` — Ungrammatical verb form: 'नहीं किया जा सके' instead of 'नहीं किया जा सकता'.
    - Current: `इसे पूर्ववत नहीं किया जा सके।`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `इसे पूर्ववत नहीं किया जा सकता।`
    - 'It cannot be undone' requires the indicative 'जा सकता', not the subjunctive 'जा सके', which is grammatically incorrect here.
- `TabTray.Title` — `hi-IN/firefox-ios.xliff` — 'Open Tabs' (noun phrase title) rendered as the command 'Open tabs'.
    - Current: `टैब खोलें`
    - Source: `Open Tabs`
    - Suggest: `खुले टैब`
    - The developer comment says this is the title for the tab tray, i.e. 'Open Tabs' meaning tabs currently open; the translation reads as an imperative 'open tabs'.
- `TopSites.RemovePage.Button` — `hi-IN/firefox-ios.xliff` — The em dash separator and word order are rearranged so the label reads as "<site> — remove page" instead of "Remove page — <site>".
    - Current: `%@ — पृष्ठ हटाएं`
    - Source: `Remove page — %@`
    - Suggest: `पृष्ठ हटाएं — %@`
    - Source is "Remove page — %@" where %@ is the site title appended after the dash; the translation puts the site title first, changing the label structure.
- `TranslationToastHandler.PromptTranslate.Title` — `hi-IN/firefox-ios.xliff` — "This page appears to be in %1$@" is rendered as "This page is displayed in %1$@".
    - Current: `यह पृष्ठ %1$@ में प्रदर्शित होता है।`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `यह पृष्ठ %1$@ में प्रतीत होता है।`
    - "appears to be in <language>" means the page seems to be in that language, not that it is displayed in it.
- _…and 19 more._

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
| Files | 23 |
| Strings | 602 |
| Missing strings | 1,320 |
| Obsolete strings | 0 |
| Files absent from the locale | 73 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**1,320 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en-US.lproj/Onboarding.strings` — 158
- `Shared/Supporting Files/en-US.lproj/MainMenu.strings` — 151
- `Shared/Supporting Files/en-US.lproj/Settings.strings` — 145
- `hi-IN/firefox-ios.xliff` — 135
- `Shared/Supporting Files/en-US.lproj/WorldCup.strings` — 73
- `Shared/Supporting Files/en-US.lproj/WebCompatReporter.strings` — 52
- `Shared/Supporting Files/en-US.lproj/EditAddress.strings` — 48
- `Shared/Supporting Files/en-US.lproj/EnhancedTrackingProtection.strings` — 43
- `Shared/Supporting Files/en-US.lproj/AppIconSelection.strings` — 42
- `Shared/Supporting Files/en-US.lproj/Bookmarks.strings` — 32
- `Shared/Supporting Files/en-US.lproj/NativeErrorPage.strings` — 32
- `Shared/Supporting Files/en-US.lproj/Translations.strings` — 31

**Files absent from the locale:**

- `Extensions/ActionExtension/en-US.lproj/InfoPlist.strings`
- `Shared/Supporting Files/en-US.lproj/ActivityStream.strings`
- `Shared/Supporting Files/en-US.lproj/AddressToolbar.strings`
- `Shared/Supporting Files/en-US.lproj/Alert.strings`
- `Shared/Supporting Files/en-US.lproj/Alerts.strings`
- `Shared/Supporting Files/en-US.lproj/AppIconSelection.strings`
- `Shared/Supporting Files/en-US.lproj/BiometricAuthentication.strings`
- `Shared/Supporting Files/en-US.lproj/Bookmarks.strings`
- `Shared/Supporting Files/en-US.lproj/BottomSheet.strings`
- `Shared/Supporting Files/en-US.lproj/Camera.strings`
- `Shared/Supporting Files/en-US.lproj/ContextualHints.strings`
- `Shared/Supporting Files/en-US.lproj/CredentialProvider.strings`
- `Shared/Supporting Files/en-US.lproj/Credentials.strings`
- `Shared/Supporting Files/en-US.lproj/CustomizeFirefoxHome.strings`
- `Shared/Supporting Files/en-US.lproj/DisplayCard.strings`
- `Shared/Supporting Files/en-US.lproj/Edit Card.strings`
- `Shared/Supporting Files/en-US.lproj/EditAddress.strings`
- `Shared/Supporting Files/en-US.lproj/EditCard.strings`
- `Shared/Supporting Files/en-US.lproj/EngagementNotification.strings`
- `Shared/Supporting Files/en-US.lproj/EnhancedTrackingProtection.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| ellipsis | `char` 5 | **char** |
| dash | `em` 1 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (79)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `NSMicrophoneUsageDescription` — `hi-IN/firefox-ios.xliff` — Microphone permission description translated as taking and uploading videos, omitting Firefox and the microphone/audio recording purpose.
    - Current: `यह आपको वीडियो लेने और अपलोड करने देता है।`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `Firefox ऑडियो रिकॉर्ड करने और अपलोड करने के लिए आपके माइक्रोफ़ोन का उपयोग करता है।`
    - en-US says "Firefox uses your microphone to record and upload audio." The target states it lets you take and upload video, which is a different permission purpose and drops the brand name.
- `Oops! Firefox crashed` — `hi-IN/firefox-ios.xliff` — "crashed" is rendered as "नष्ट हो गया" (was destroyed), which is not the software sense of crashing.
    - Current: `उफ़! Firefox नष्ट हो गया`
    - Source: `Oops! Firefox crashed`
    - Suggest: `उफ़! Firefox क्रैश हो गया`
    - The source says the app crashed; "नष्ट हो गया" means it was destroyed/annihilated, telling the user the product destroyed itself rather than that it stopped unexpectedly.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 33 |
| 3 | Degraded language (grammar, spelling, terminology) | 45 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSMicrophoneUsageDescription` — `hi-IN/firefox-ios.xliff` — Microphone permission description translated as taking and uploading videos, omitting Firefox and the microphone/audio recording purpose.
    - Current: `यह आपको वीडियो लेने और अपलोड करने देता है।`
    - Source: `Firefox uses your microphone to record and upload audio.`
    - Suggest: `Firefox ऑडियो रिकॉर्ड करने और अपलोड करने के लिए आपके माइक्रोफ़ोन का उपयोग करता है।`
    - en-US says "Firefox uses your microphone to record and upload audio." The target states it lets you take and upload video, which is a different permission purpose and drops the brand name.
- `Use your fingerprint to access Logins now.` — `hi-IN/firefox-ios.xliff` — "access Logins" rendered as "to log in", changing the meaning.
    - Current: `अब लॉगिन करने के लिए अपने फिंगरप्रिंट का उपयोग करें।`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `अब लॉगिन तक पहुँचने के लिए अपने फिंगरप्रिंट का उपयोग करें।`
    - The source refers to accessing the saved Logins list, not to performing a login.
- `DefaultBrowserOnboarding.Description2` — `hi-IN/firefox-ios.xliff` — "Tap Default Browser App" mistranslated as "tap as default browser", losing the name of the settings item.
    - Current: `2. डिफ़ॉल्ट ब्राउज़र के रूप में टैप करें`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. तयशुदा ब्राउज़र ऐप पर टैप करें`
    - The source instructs the user to tap the iOS settings row named "Default Browser App"; the target says to tap "as default browser", which is not an instruction the user can follow.
- `ActivityStream.ContextMenu.AddToShortcuts` — `hi-IN/firefox-ios.xliff` — "Add to Shortcuts" is translated as "Add to contacts".
    - Current: `संपर्क में जोड़ें`
    - Source: `Add to Shortcuts`
    - Suggest: `शॉर्टकट में जोड़ें`
    - The source refers to pinning a site to Shortcuts; "संपर्क" means contacts, which names the wrong feature.
- `ActivityStream.JumpBackIn.SectionTitle` — `hi-IN/firefox-ios.xliff` — "Jump Back In" rendered literally as "go back inside", losing the meaning of resuming a recent tab.
    - Current: `वापस अंदर जायें`
    - Source: `Jump Back In`
    - Suggest: `वहीं से जारी रखें`
    - The section lets users resume recently viewed tabs; the literal "go back inside" conveys no such meaning.
- `Downloads.CancelDialog.Resume` — `hi-IN/firefox-ios.xliff` — "Resume" rendered as "पुनः चलाएं" (play again/restart) rather than resuming the download.
    - Current: `पुनः चलाएं`
    - Source: `Resume`
    - Suggest: `फिर शुरू करें`
    - The button declines cancellation and continues the download; "पुनः चलाएं" suggests restarting/playing again rather than resuming.
- `ErrorPages.CertWarning.Description` — `hi-IN/firefox-ios.xliff` — "owner" is translated as "उत्तराधिकारी" (heir/successor) instead of "स्वामी/मालिक" (owner).
    - Current: `%@ के उत्तराधिकारी ने`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `%@ के स्वामी ने`
    - en-US says "The owner of %@"; उत्तराधिकारी means heir/successor, not owner.
- `Forward` — `hi-IN/firefox-ios.xliff` — Toolbar Forward navigation button translated as "आगे बढ़ाएं" (to forward/advance something) instead of "आगे".
    - Current: `आगे बढ़ाएं`
    - Source: `Forward`
    - Suggest: `आगे`
    - The string is the accessibility label for the tab toolbar Forward navigation button; "आगे बढ़ाएं" is transitive (move something forward), not the navigation direction.
- `FxAPush_DeviceConnected_body` — `hi-IN/firefox-ios.xliff` — The notification body reverses the direction of the connection.
    - Current: `Firefox सिंक %@ में जोड़ा गया`
    - Source: `Firefox Sync has connected to %@`
    - Suggest: `Firefox सिंक %@ से जुड़ गया है`
    - Source says Firefox Sync has connected to the named device; the Hindi says "Firefox Sync was added into %@", which states something different.
- `HistoryPanel.ClearHistoryMenuOptionTodayAndYesterday` — `hi-IN/firefox-ios.xliff` — "कल" is ambiguous and here reads as tomorrow/yesterday without disambiguation.
    - Current: `आज और कल`
    - Source: `Today and Yesterday`
    - Suggest: `आज और बीता कल`
    - Source is "Today and Yesterday"; "कल" alone means both yesterday and tomorrow in Hindi, so for a clear-history range it must be disambiguated as past.
- `HistoryPanel.EmptySyncedTabsPanelNotSignedInState.Description` — `hi-IN/firefox-ios.xliff` — Misattaches "from your other devices" to the sign-in action rather than to the tabs.
    - Current: `टैब की सूची देखने के लिए अपने दूसरे उपकरणों से साइन इन करें।`
    - Source: `Sign in to view a list of tabs from your other devices.`
    - Suggest: `अपने अन्य उपकरणों के टैब की सूची देखने के लिए साइन इन करें।`
    - Source: "Sign in to view a list of tabs from your other devices." The Hindi tells the user to sign in from their other devices, which is not what the source says.
- `Hotkeys.Forward.DiscoveryTitle` — `hi-IN/firefox-ios.xliff` — "Forward" navigation rendered as a transitive "move forward/advance something" verb.
    - Current: `आगे बढ़ाएं`
    - Source: `Forward`
    - Suggest: `आगे`
    - Paired with "Back" (पीछे) as a navigation shortcut label; "आगे बढ़ाएं" means to advance/promote something else.
- `Hotkeys.ShowPreviousTab.DiscoveryTitle` — `hi-IN/firefox-ios.xliff` — "Previous Tab" translated as "previous page" instead of tab.
    - Current: `पिछला पृष्ठ दिखाएं`
    - Source: `Show Previous Tab`
    - Suggest: `पिछला टैब दिखाएँ`
    - Source says "Show Previous Tab"; टैब (tab) was rendered as पृष्ठ (page), inconsistent with the sibling string "अगला टैब दिखाएं".
- `LoginsList.Title` — `hi-IN/firefox-ios.xliff` — "SAVED LOGINS" (a plural list title) is rendered as singular "login saved", reading like a status message rather than a list heading.
    - Current: `लॉग इन सहेजा गया`
    - Source: `SAVED LOGINS`
    - Suggest: `सहेजे गए लॉगिन`
    - The source is a title for the list of logins (plural noun phrase), not a past-tense confirmation that a login was saved.
- `Looks like Firefox crashed previously. Would you like to restore your tabs?` — `hi-IN/firefox-ios.xliff` — "restore your tabs" is translated as "पूर्ववत करना" (undo), and "crashed" as "नष्ट हो गया" (was destroyed).
    - Current: `ऐसा लगता है जैसे कि Firefox पूर्व में नष्ट हो गया। क्या आप अपने टैब को पूर्ववत करना चाहेंगे?`
    - Source: `Looks like Firefox crashed previously. Would you like to restore your tabs?`
    - Suggest: `ऐसा लगता है कि Firefox पिछली बार क्रैश हो गया था। क्या आप अपने टैब पुनर्स्थापित करना चाहेंगे?`
    - "पूर्ववत करना" means to undo, not to restore tabs; "नष्ट हो गया" means destroyed, not crashed.
- `Menu.ReloadWithoutTrackingProtection.Title` — `hi-IN/firefox-ios.xliff` — "Reload" is rendered as just "लोड करें" (load), losing the "re-" and diverging from the parallel string.
    - Current: `ट्रैकिंग सुरक्षा के बिना लोड करें`
    - Source: `Reload Without Tracking Protection`
    - Suggest: `ट्रैकिंग सुरक्षा के बिना फिर से लोड करें`
    - The companion string Menu.ReloadWithTrackingProtection.Title uses "फिर से लोड करें" for Reload; here it says only "load".
- `Menu.TrackingProtectionDescription.ContentTrackers` — `hi-IN/firefox-ios.xliff` — "Blocking this" translated as "इसे बाधित करने से" (obstructing/interrupting) instead of blocking.
    - Current: `इसे बाधित करने से`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `इसे अवरोधित करने से`
    - "Block" in tracking protection context should be "अवरोधित करना"; "बाधित" means obstruct/interrupt.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `hi-IN/firefox-ios.xliff` — "drain your battery" translated as "बैटरी को ख़राब करती है" (damages your battery).
    - Current: `आपकी बैटरी को ख़राब करती है`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `आपकी बैटरी खत्म करती है`
    - The source says the scripts drain the battery, not that they damage/spoil it.
- `Oops! Firefox crashed` — `hi-IN/firefox-ios.xliff` — "crashed" is rendered as "नष्ट हो गया" (was destroyed), which is not the software sense of crashing.
    - Current: `उफ़! Firefox नष्ट हो गया`
    - Source: `Oops! Firefox crashed`
    - Suggest: `उफ़! Firefox क्रैश हो गया`
    - The source says the app crashed; "नष्ट हो गया" means it was destroyed/annihilated, telling the user the product destroyed itself rather than that it stopped unexpectedly.
- `Open Tabs` — `hi-IN/firefox-ios.xliff` — "Open Tabs" (a noun phrase naming the syncing category) is translated as the imperative "टैब खोलें" (Open the tabs).
    - Current: `टैब खोलें`
    - Source: `Open Tabs`
    - Suggest: `खुले टैब`
    - The developer comment says this is a toggle for the tabs syncing setting, so "Open Tabs" is the noun "tabs that are open", not a command.
- `RecentlyClosedTabsPanel.Title` — `hi-IN/firefox-ios.xliff` — Translation adds "टैब" not present in the source "Recently Closed".
    - Current: `हाल ही में बंद किए टैब`
    - Source: `Recently Closed`
    - Suggest: `हाल ही में बंद किए गए`
    - The source title is just "Recently Closed"; the added noun changes the label and lengthens a panel title.
- `Send Report` — `hi-IN/firefox-ios.xliff` — "Send Report" is translated as "Send details/description" instead of "report".
    - Current: `विवरण भेजें`
    - Source: `Send Report`
    - Suggest: `रिपोर्ट भेजें`
    - en-US "Send Report" refers to sending a crash report; "विवरण" means details/description, not a report.
- `Settings.AddCustomEngine.URLPlaceholder` — `hi-IN/firefox-ios.xliff` — The instruction "Replace Query with %s" is reversed: the Hindi says "replace with %s" and drops the object "Query".
    - Current: `URL (%s के साथ बदलें)`
    - Source: `URL (Replace Query with %s)`
    - Suggest: `URL (क्वेरी को %s से बदलें)`
    - Source tells the user to replace the search query in the URL with the token %s; the translation omits "Query" and reads as an instruction to replace something unspecified with %s.
- `Settings.Disconnect.Button` — `hi-IN/firefox-ios.xliff` — "Disconnect Sync" is translated as just "Disconnect", losing "Sync".
    - Current: `डिस्कनेक्ट करें`
    - Source: `Disconnect Sync`
    - Suggest: `सिंक डिस्कनेक्ट करें`
    - Source is "Disconnect Sync"; the translation is identical to the separate "Disconnect" string and omits the Sync object.
- `Settings.Disconnect.Title` — `hi-IN/firefox-ios.xliff` — "Disconnect Sync?" is rendered without "Sync".
    - Current: `डिस्कनेक्ट करें?`
    - Source: `Disconnect Sync?`
    - Suggest: `सिंक डिस्कनेक्ट करें?`
    - The source specifies disconnecting Sync; the translation drops the object, and is also identical to the plain "Disconnect" button string.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `hi-IN/firefox-ios.xliff` — Descriptive statement turned into an imperative command, changing the meaning.
    - Current: `कुछ विज्ञापन ट्रैकर्स को अनुमति दें ताकि वेबसाइटें सही तरह से कार्य कर सकें।`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `कुछ विज्ञापन ट्रैकिंग की अनुमति देता है ताकि वेबसाइटें सही तरह से कार्य कर सकें।`
    - The source is a description ('Allows some ad tracking so websites function properly'), not an instruction to the user; the sibling strict-level description correctly uses the descriptive 'ब्लॉक करता है'.
- `TabTray.Title` — `hi-IN/firefox-ios.xliff` — 'Open Tabs' (noun phrase title) rendered as the command 'Open tabs'.
    - Current: `टैब खोलें`
    - Source: `Open Tabs`
    - Suggest: `खुले टैब`
    - The developer comment says this is the title for the tab tray, i.e. 'Open Tabs' meaning tabs currently open; the translation reads as an imperative 'open tabs'.
- `TopSites.RemovePage.Button` — `hi-IN/firefox-ios.xliff` — The em dash separator and word order are rearranged so the label reads as "<site> — remove page" instead of "Remove page — <site>".
    - Current: `%@ — पृष्ठ हटाएं`
    - Source: `Remove page — %@`
    - Suggest: `पृष्ठ हटाएं — %@`
    - Source is "Remove page — %@" where %@ is the site title appended after the dash; the translation puts the site title first, changing the label structure.
- `TranslationToastHandler.PromptTranslate.Title` — `hi-IN/firefox-ios.xliff` — "This page appears to be in %1$@" is rendered as "This page is displayed in %1$@".
    - Current: `यह पृष्ठ %1$@ में प्रदर्शित होता है।`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `यह पृष्ठ %1$@ में प्रतीत होता है।`
    - "appears to be in <language>" means the page seems to be in that language, not that it is displayed in it.
- `read` — `hi-IN/firefox-ios.xliff` — The past-participle adjective "read" is translated as the imperative verb "पढ़ें" (read it).
    - Current: `पढ़ें`
    - Source: `read`
    - Suggest: `पठित`
    - Developer comment states it is a past participle functioning as an adjective for a read article; the counterpart string uses "अपठित" (unread), so "पठित" is the correct pair.
- `Clear Search` — `hi-IN/firefox-ios.xliff` — "Clear Search" translated as "delete search" (खोज मिटाएं), the same verb used for Delete.
    - Current: `खोज मिटाएं`
    - Source: `Clear Search`
    - Suggest: `खोज साफ़ करें`
    - Clear means to empty the search field; मिटाएं is used elsewhere in this file for Delete, creating a terminology clash.
- `Enter Search Mode` — `hi-IN/firefox-ios.xliff` — "Enter Search Mode" translated as "enter/type the search mode" using दर्ज करें (to input text) rather than entering a mode.
    - Current: `खोज विधि दर्ज करें`
    - Source: `Enter Search Mode`
    - Suggest: `खोज मोड में जाएं`
    - दर्ज करें means to type/enter data; the source means to switch into search mode.
- `Search Input Field` — `hi-IN/firefox-ios.xliff` — "Search Input Field" is rendered as an imperative "search the input field" instead of the noun phrase naming the field.
    - Current: `इनपुट क्षेत्र खोजें`
    - Source: `Search Input Field`
    - Suggest: `खोज इनपुट क्षेत्र`
    - The source is an accessibility label naming the search input field; the translation reads as a command to search the input field.
- `Menu.NewPrivateTabAction.Title` — `hi-IN/firefox-ios.xliff` — "Open New Private Tab" translated only as "New Private Tab", dropping the verb.
    - Current: `नया निजी टैब`
    - Source: `Open New Private Tab`
    - Suggest: `नया निजी टैब खोलें`
    - The source is an action label including "Open"; the verb is missing in the translation.
- `Menu.NewTabAction.Title` — `hi-IN/firefox-ios.xliff` — "Open New Tab" translated only as "New Tab", dropping the verb.
    - Current: `नया टैब`
    - Source: `Open New Tab`
    - Suggest: `नया टैब खोलें`
    - The source is an action label including "Open"; the verb is missing in the translation.
- `Search Settings` — `hi-IN/firefox-ios.xliff` — "Search Settings" (settings for search) is rendered as an imperative "search the settings".
    - Current: `सेटिंग खोजें`
    - Source: `Search Settings`
    - Suggest: `खोज सेटिंग`
    - The source is a noun phrase labelling the button that opens search engine settings; "सेटिंग खोजें" means "Search the settings", reversing the head noun.
- `TodayWidget.QuickViewGalleryDescriptionV2` — `hi-IN/firefox-ios.xliff` — "Add shortcuts to your open tabs" mistranslated as adding shortcuts inside the open tabs.
    - Current: `अपने खुले टैब में शॉर्टकट जोड़ें।`
    - Source: `Add shortcuts to your open tabs.`
    - Suggest: `अपने खुले टैब के लिए शॉर्टकट जोड़ें।`
    - The source means creating shortcuts that lead to your open tabs; "खुले टैब में" says shortcuts are added into the tabs.
- `TodayWidget.TopSitesGalleryDescription` — `hi-IN/firefox-ios.xliff` — "Add shortcuts to ... sites" mistranslated as adding shortcuts onto the sites.
    - Current: `अक्सर और हाल ही में देखी गई साइट पर शॉर्टकट जोड़ें।`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `अक्सर और हाल ही में देखी गई साइट के लिए शॉर्टकट जोड़ें।`
    - The source means creating shortcuts pointing to frequently/recently visited sites; "साइट पर शॉर्टकट जोड़ें" says shortcuts are added on the sites.
- `eHmH1H` — `hi-IN/firefox-ios.xliff` — "Clear Private Tabs" translated as "Close Private Tabs".
    - Current: `निजी टैब बंद करें`
    - Source: `Clear Private Tabs`
    - Suggest: `निजी टैब साफ़ करें`
    - Source says Clear, not Close; the same target string is used for the separate "Close Private Tabs" label, losing the distinction.

### C. Grammar, agreement & spelling

- `Bookmarks.DeleteFolderWarning.Title` — `hi-IN/firefox-ios.xliff` — Number agreement error: singular subject with plural verb form.
    - Current: `यह फोल्डर खाली नहीं हैं।`
    - Source: `This folder isn’t empty.`
    - Suggest: `यह फोल्डर खाली नहीं है।`
    - "This folder isn’t empty" is singular; हैं is the plural form and should be है.
- `This action will clear all of your private data, including history from your synced devices.` — `hi-IN/firefox-ios.xliff` — Misspelling of निजी as निज़ी.
    - Current: `निज़ी`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `निजी`
    - The correct Hindi spelling is निजी (as used in the ClearPrivateDataConfirm string); the nukta form निज़ी is incorrect.
- `Find in Page` — `hi-IN/firefox-ios.xliff` — Misspelled postposition "मे" instead of "में".
    - Current: `पृष्ठ मे ढूंढें`
    - Source: `Find in Page`
    - Suggest: `पृष्ठ में ढूंढें`
    - Hindi locative postposition requires the anusvara: में.
- `Next in-page result` — `hi-IN/firefox-ios.xliff` — Postposition "मे" is misspelled (should be "में") and the phrase is garbled.
    - Current: `पृष्ठ परिणाम मे अगला`
    - Source: `Next in-page result`
    - Suggest: `पृष्ठ में अगला परिणाम`
    - en-US means "next result within the page"; the target reads "next in page results" with a misspelled postposition (मे instead of में).
- `Previous in-page result` — `hi-IN/firefox-ios.xliff` — Postposition "मे" is misspelled (should be "में") and the phrase is garbled.
    - Current: `पृष्ठ परिणाम मे पिछला`
    - Source: `Previous in-page result`
    - Suggest: `पृष्ठ में पिछला परिणाम`
    - en-US means "previous result within the page"; target uses misspelled मे and reverses the noun structure.
- `Added page to Reading List` — `hi-IN/firefox-ios.xliff` — Misspelled postposition "मे" instead of "में".
    - Current: `पठन सूची मे पृष्ठ जोड़ दिया गया`
    - Source: `Added page to Reading List`
    - Suggest: `पठन सूची में पृष्ठ जोड़ दिया गया`
    - Hindi locative postposition requires the anusvara: में.
- `Bookmarks.NewFolder.Label` — `hi-IN/firefox-ios.xliff` — "फोल्डर" spelled without nukta, inconsistent with "फ़ोल्डर" used in the other folder strings.
    - Current: `नया फोल्डर`
    - Source: `New Folder`
    - Suggest: `नया फ़ोल्डर`
    - Bookmarks.Folder.Label and Bookmarks.EditFolder.Label use "फ़ोल्डर"; this string drops the nukta, creating a spelling/consistency error on the same screen.
- `Changes color theme.` — `hi-IN/firefox-ios.xliff` — Accessibility hint translated as a noun phrase "रंग थीम परिवर्तन।" instead of the verb form used in the parallel string.
    - Current: `रंग थीम परिवर्तन।`
    - Source: `Changes color theme.`
    - Suggest: `रंग थीम बदलें।`
    - The source "Changes color theme." is a hint describing an action, and the parallel string "Changes font type." is translated as "फ़ॉन्ट प्रकार बदलें।"; the noun form is grammatically incomplete and inconsistent.
- `Could not add page to Reading list` — `hi-IN/firefox-ios.xliff` — "मे" is misspelled; should be "में".
    - Current: `पृष्ठ को पठन सूची मे नहीं जोड़ा जा सकता है`
    - Source: `Could not add page to Reading list`
    - Suggest: `पृष्ठ को पठन सूची में नहीं जोड़ा जा सका`
    - The postposition is spelled "में"; also the source is past tense ("Could not add"), while the target uses present ability "जोड़ा जा सकता है".
- `CoverSheet.v24.ETP.Description` — `hi-IN/firefox-ios.xliff` — Misspelling of "अंतर्निहित" and gender/number agreement error in "आपका पीछा करने वाली विज्ञापनों".
    - Current: `अंतनिर्हित उन्नत ट्रैकिंग सुरक्षा आपका पीछा करने वाली विज्ञापनों को रोकने में मदद करता है`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `अंतर्निहित उन्नत ट्रैकिंग सुरक्षा आपका पीछा करने वाले विज्ञापनों को रोकने में मदद करती है`
    - "अंतनिर्हित" is a misspelling of "अंतर्निहित" (Built-in); "विज्ञापनों" is masculine plural so it needs "वाले", and "सुरक्षा" is feminine so the verb should be "करती है".
- `Enter your password to connect` — `hi-IN/firefox-ios.xliff` — Misspelling: "दर्ज़" should be "दर्ज".
    - Current: `दर्ज़ करें`
    - Source: `Enter your password to connect`
    - Suggest: `दर्ज करें`
    - The Hindi word is दर्ज, without nukta on ज.
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `hi-IN/firefox-ios.xliff` — Ungrammatical verb form: intransitive subject with transitive causative construction.
    - Current: `एक उपकरण Firefox सिंक से डिस्कनेक्ट कर दिया है`
    - Source: `A device has disconnected from Firefox Sync`
    - Suggest: `एक उपकरण Firefox सिंक से डिस्कनेक्ट हो गया है`
    - Source is "A device has disconnected from Firefox Sync"; the Hindi "डिस्कनेक्ट कर दिया है" is grammatically incorrect for this subject.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `hi-IN/firefox-ios.xliff` — Subject-verb agreement error: plural "सोशल नेटवर्क" takes singular verb "रखता है".
    - Current: `सोशल नेटवर्क ट्रैकर को अन्य वेबसाइटों पर आपके पूर्ण और लक्षित प्रोफ़ाइल के निर्माण के लिए रखता है।`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `सोशल नेटवर्क आपकी अधिक पूर्ण और लक्षित प्रोफ़ाइल बनाने के लिए अन्य वेबसाइटों पर ट्रैकर रखते हैं।`
    - "Social networks place trackers" is plural in the source; the Hindi verb is singular and the possessive gender is wrong (प्रोफ़ाइल is feminine).
- `OpenURL.Error.Message` — `hi-IN/firefox-ios.xliff` — Spelling/agreement errors: "नही" should be "नहीं" and "सकता हैं" should be "सकता है".
    - Current: `Firefox पृष्ठ को नही खोल सकता हैं`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `Firefox पृष्ठ को नहीं खोल सकता है`
    - "नही" is a misspelling of "नहीं", and the plural verb "हैं" does not agree with the singular subject.
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `hi-IN/firefox-ios.xliff` — Ungrammatical phrase "अपने कैमरा रोल करने में" mangles "to your Camera Roll".
    - Current: `यह आपको अपने कैमरा रोल करने में चित्रों को सहेजने की अनुमति देता है।`
    - Source: `This allows you to save the image to your Camera Roll.`
    - Suggest: `यह आपको चित्रों को अपने कैमरा रोल में सहेजने की अनुमति देता है।`
    - The postposition sequence is broken; the source means saving the image to the Camera Roll.
- `PhotoLibrary.FirefoxWouldLikeAccessTitle` — `hi-IN/firefox-ios.xliff` — Verb agreement error: singular subject Firefox takes "चाहता है", not the plural "चाहेंगे".
    - Current: `Firefox आपके फ़ोटो को एक्सेस करना चाहेंगे`
    - Source: `Firefox would like to access your Photos`
    - Suggest: `Firefox आपकी फ़ोटो एक्सेस करना चाहता है`
    - "चाहेंगे" is plural/future and does not agree with the singular subject Firefox.
- `Send a crash report so Mozilla can fix the problem?` — `hi-IN/firefox-ios.xliff` — Gender agreement error: "एक विवरण" with feminine "एक" plus wrong term for "report".
    - Current: `खराबी की एक विवरण भेजें`
    - Source: `Send a crash report so Mozilla can fix the problem?`
    - Suggest: `क्रैश रिपोर्ट भेजें`
    - "विवरण" is masculine so "एक विवरण" mismatches the feminine article usage, and "report" should be रिपोर्ट as in the button label; also keeps terminology consistent with the Send Report button.
- `Settings.AddCustomEngine` — `hi-IN/firefox-ios.xliff` — Misspelling of "इंजन" as "ईंजन".
    - Current: `खोज ईंजन जोड़ें`
    - Source: `Add Search Engine`
    - Suggest: `खोज इंजन जोड़ें`
    - The standard Hindi transliteration used elsewhere in this file (Search.ThirdPartyEngines.AddMessage) is "इंजन"; "ईंजन" is a spelling error and inconsistent.
- `Settings.AddCustomEngine.Title` — `hi-IN/firefox-ios.xliff` — Misspelling of "इंजन" as "ईंजन".
    - Current: `खोज ईंजन जोड़ें`
    - Source: `Add Search Engine`
    - Suggest: `खोज इंजन जोड़ें`
    - The standard Hindi spelling used elsewhere in this file is "इंजन"; "ईंजन" is misspelled and inconsistent.
- `Settings.Home.Option.StartAtHome.AfterFourHours` — `hi-IN/firefox-ios.xliff` — Word order makes the phrase ungrammatical in Hindi.
    - Current: `मुखपृष्ठ चार घंटे की निष्क्रियता के बाद`
    - Source: `Homepage after four hours of inactivity`
    - Suggest: `चार घंटे की निष्क्रियता के बाद मुखपृष्ठ`
    - Hindi postpositional phrases precede the noun; the English word order was copied literally, producing an ungrammatical label.
- `Settings.Home.Option.StartAtHome.Title` — `hi-IN/firefox-ios.xliff` — Gender agreement error: स्क्रीन is feminine, so the modifier must be खुलती हुई.
    - Current: `खुलता हुआ स्क्रीन`
    - Source: `Opening screen`
    - Suggest: `प्रारंभिक स्क्रीन`
    - "Opening screen" — the adjective phrase does not agree with the feminine noun स्क्रीन; also the literal progressive rendering is wrong for the meaning of the initial screen shown at launch.
- `Settings.SendUsage.Message` — `hi-IN/firefox-ios.xliff` — Translation is ungrammatical and loses the meaning "to provide and improve Firefox for everyone".
    - Current: `तथा Firefox को सभी के लिए बेहतर बनता है।`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `तथा Firefox को सभी के लिए बेहतर बनाने के लिए ज़रूरी है।`
    - The source says Mozilla collects only what it needs to provide and improve Firefox for everyone; the target reads "...and Firefox becomes better for everyone" with the intransitive 'बनता है' not agreeing with 'Firefox को', making the sentence grammatically broken and changing the meaning.
- `Settings.SendUsage.Title` — `hi-IN/firefox-ios.xliff` — "उपयोगित" is not a valid Hindi word for "Usage".
    - Current: `उपयोगित डेटा भेजें`
    - Source: `Send Usage Data`
    - Suggest: `उपयोग डेटा भेजें`
    - "Send Usage Data" should be "उपयोग डेटा" or "उपयोग संबंधी डेटा"; "उपयोगित" is a misspelling/non-word.
- `Settings.WebsiteData.ConfirmPrompt` — `hi-IN/firefox-ios.xliff` — Ungrammatical verb form: 'नहीं किया जा सके' instead of 'नहीं किया जा सकता'.
    - Current: `इसे पूर्ववत नहीं किया जा सके।`
    - Source: `This action will clear all of your website data. It cannot be undone.`
    - Suggest: `इसे पूर्ववत नहीं किया जा सकता।`
    - 'It cannot be undone' requires the indicative 'जा सकता', not the subjunctive 'जा सके', which is grammatically incorrect here.
- `Welcome to your Reading List` — `hi-IN/firefox-ios.xliff` — Gender agreement error: "अपने पठन सूची" should be "अपनी पठन सूची" (सूची is feminine).
    - Current: `अपने पठन सूची में स्वागत है`
    - Source: `Welcome to your Reading List`
    - Suggest: `अपनी पठन सूची में स्वागत है`
    - सूची is a feminine noun and requires the feminine possessive form अपनी.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `hi-IN/firefox-ios.xliff` — Spelling error: "नही" should be "नहीं".
    - Current: `याद नही रखेगा`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `याद नहीं रखेगा`
    - The negation particle in Hindi is spelled नहीं with the anusvara/long i; "नही" is a misspelling.
- `TodayWidget.FirefoxShortcutGalleryDescription` — `hi-IN/firefox-ios.xliff` — Gender agreement error: "अपने होम स्क्रीन" should be "अपनी होम स्क्रीन".
    - Current: `अपने होम स्क्रीन पर`
    - Source: `Add Firefox shortcuts to your Home screen.`
    - Suggest: `अपनी होम स्क्रीन पर`
    - स्क्रीन is feminine in Hindi, requiring अपनी.
- `TodayWidget.QuickActionsGalleryTitle` — `hi-IN/firefox-ios.xliff` — Spelling error: "कारवाई" should be "कार्रवाई".
    - Current: `तुरंत कारवाई`
    - Source: `Quick Actions`
    - Suggest: `त्वरित कार्रवाई`
    - The Hindi word for action is कार्रवाई; "कारवाई" is a misspelling (also in the related Quick Action strings).
- `eV8mOT` — `hi-IN/firefox-ios.xliff` — Spelling error: "कारवाई" should be "कार्रवाई".
    - Current: `तुरंत कारवाई प्रकार`
    - Source: `Quick Action Type`
    - Suggest: `त्वरित कार्रवाई प्रकार`
    - The Hindi word for action is कार्रवाई; "कारवाई" is a misspelling.
- `eqyNJg` — `hi-IN/firefox-ios.xliff` — Spelling error: "कारवाई" should be "कार्रवाई".
    - Current: `तुरंत कारवाई`
    - Source: `Quick Action`
    - Suggest: `त्वरित कार्रवाई`
    - The Hindi word for action is कार्रवाई; "कारवाई" is a misspelling.
- `w9jdPK` — `hi-IN/firefox-ios.xliff` — Spelling error: "कारवाई" should be "कार्रवाई".
    - Current: `तुरंत कारवाई`
    - Source: `Quick Action`
    - Suggest: `त्वरित कार्रवाई`
    - The Hindi word for action is कार्रवाई; "कारवाई" is a misspelling.

### D. Terminology, register & consistency

- `Send to Device` — `hi-IN/firefox-ios.xliff` — "Device" translated as उपकरण here but as डिवाइस in the sibling string on the same screen.
    - Current: `उपकरण में भेजें`
    - Source: `Send to Device`
    - Suggest: `डिवाइस पर भेजें`
    - Menu.SendLinkToDevice in the same file uses डिवाइस ... पर भेजें; the inconsistent term and postposition on the same feature is a terminology inconsistency.
- `BreachAlerts.Link` — `hi-IN/firefox-ios.xliff` — "Go to" rendered with the informal/imperative "जाओ", which breaks the polite register used elsewhere in the app.
    - Current: `जाओ`
    - Source: `Go to`
    - Suggest: `इस पर जाएं`
    - The en-US "Go to" leads to the breached website; other similar strings use the polite "जाएं" (e.g. ClipboardToast.GoToCopiedLink.Button). "जाओ" is the familiar/rude imperative form and is inconsistent with the app's register.
- `CoverSheet.v24.ETP.Title` — `hi-IN/firefox-ios.xliff` — "Ad Tracking" rendered as "विज्ञापन की निगरानी" (surveillance) instead of the app's established term for tracking.
    - Current: `विज्ञापन की निगरानी के विरुद्ध सुरक्षा`
    - Source: `Protection Against Ad Tracking`
    - Suggest: `विज्ञापन ट्रैकिंग के विरुद्ध सुरक्षा`
    - The related description string uses "ट्रैकिंग" and "ट्रैकर्स" for tracking; using "निगरानी" here is inconsistent terminology for the same feature screen.
- `Menu.ReadingList.Label` — `hi-IN/firefox-ios.xliff` — "Reading List" translated as "पाठ सूची" (text/lesson list), inconsistent with "पठन सूची" used in Menu.AddToReadingList.Confirm.
    - Current: `पाठ सूची`
    - Source: `Reading List`
    - Suggest: `पठन सूची`
    - Same source term rendered two different ways in the same menu group; "पाठ" means lesson/text, not reading.
- `Reader View` — `hi-IN/firefox-ios.xliff` — "Reader View" rendered as "पाठक परिदृश्य" while another string uses "पाठक दृश्य" for the same term.
    - Current: `पाठक परिदृश्य`
    - Source: `Reader View`
    - Suggest: `पाठक दृश्य`
    - Inconsistent rendering of the same UI feature name within the same file (see "पाठक दृश्य" in the Reader View tip string).
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `hi-IN/firefox-ios.xliff` — "Reading List" is rendered "पाठ्य सूची", inconsistent with "पठन सूची" used elsewhere for the same term.
    - Current: `अपनी पाठ्य सूची में`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `अपनी पठन सूची में`
    - The same source term "Reading List" is translated "पठन सूची" in the Reading list and Remove from Reading List strings.
- `Search.ThirdPartyEngines.AddSuccess` — `hi-IN/firefox-ios.xliff` — "Search engine" rendered as "सर्च इंजन" while the rest of the screen uses "खोज इंजन".
    - Current: `सर्च इंजन जोड़ा गया!`
    - Source: `Added Search engine!`
    - Suggest: `खोज इंजन जोड़ा गया!`
    - Neighbouring strings (AddMessage, DuplicateErrorMessage, Settings.AddCustomEngine) translate "search engine" as "खोज इंजन"; this transliteration is inconsistent on the same feature.
- `Toasts.Undo` — `hi-IN/firefox-ios.xliff` — "Undo" is rendered inconsistently as "पहले जैसा" here but "पूर्ववत् करें" in Tabs.DeleteAllUndo.Button.
    - Current: `पहले जैसा`
    - Source: `Undo`
    - Suggest: `पूर्ववत् करें`
    - Same source term "Undo" for the same undo action button should use one consistent term; "पहले जैसा" is not an action label.

### E. Typography, punctuation & spacing

- `Menu.SharePageAction.Title` — `hi-IN/firefox-ios.xliff` — The trailing ellipsis of "Share Page With…" is moved to the front of the string.
    - Current: `… के साथ पृष्ठ साझा करें`
    - Source: `Share Page With…`
    - Suggest: `पृष्ठ इसके साथ साझा करें…`
    - The ellipsis indicates a follow-up dialog and belongs at the end of the label, not at the beginning.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/hi-IN/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
