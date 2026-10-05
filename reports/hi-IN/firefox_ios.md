# Firefox iOS l10n QA — hi-IN

| | |
|---|---|
| **Generated** | 2026-10-05 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `ef278c60f343` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `ef278c60f343` |
| **Previous run** | 2026-09-28 @ `76fd90c3d050` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,950 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for hi-IN: [android](android.md)

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
| Files | 97 |
| Strings | 1,950 |
| Missing strings | 19 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**19 strings** are not translated yet, concentrated in:

- `hi-IN/firefox-ios.xliff` — 18
- `hi-IN/firefox-ios.xliff` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 4 | **curly-double** |
| apostrophe | `straight` 11 | **straight** |
| ellipsis | `char` 23 | **char** |
| dash | `em` 5 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (17)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 14 |
| 3 | Degraded language (grammar, spelling, terminology) | 3 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `CloseTab.ArrivingNotification.title.v133` — `hi-IN/firefox-ios.xliff` — "%1$@ tabs closed" is rendered as "tabs closed in %1$@", adding a locative meaning the source does not have.
    - Current: `%1$@ में बंद किए गए टैब: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `%1$@ के बंद किए गए टैब: %2$@`
    - The source names the app as the subject ('Firefox tabs closed'), not a location where tabs were closed; 'में' (in) changes the meaning.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `hi-IN/firefox-ios.xliff` — "won’t sell you out" (won't betray/sell your data) is rendered as the generic claim "is trustworthy".
    - Current: `तेज़, सुरक्षित और भरोसेमंद है।`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `तेज़, सुरक्षित और आपको धोखा नहीं देगा।`
    - The en-US promises specifically that the browser will not sell the user out; the Hindi replaces it with a vague self-description "is trustworthy".
- `PrivacyDashboard.HeaderLabelForNoTrackersBlocked.v155` — `hi-IN/firefox-ios.xliff` — "you’ll see them here" is translated as "आप उन्हें यहां देख सकते हैं" (you can see them here), turning a future statement into a present ability.
    - Current: `आप उन्हें यहां देख सकते हैं।`
    - Source: `%@ blocks trackers as you browse, you’ll see them here.`
    - Suggest: `आप उन्हें यहां देखेंगे।`
    - The source promises the user will see blocked trackers here in the future; the translation asserts they can already see them, though none have been blocked yet.
- `QuickAnswers.ContentView.Answering.v158` — `hi-IN/firefox-ios.xliff` — "Answering…" is rendered as "जवाब दिया जा रहा है…" (an answer is being given) rather than indicating the answer is being fetched/prepared; acceptable-ish but the passive completed sense misleads.
    - Current: `जवाब दिया जा रहा है…`
    - Source: `Answering…`
    - Suggest: `जवाब तैयार किया जा रहा है…`
    - The comment says this is a loading label while the answer is being fetched; "जवाब दिया जा रहा है" states the answer is already being delivered.
- `Settings.Notifications.SyncNotificationsStatus.v112` — `hi-IN/firefox-ios.xliff` — The translation says notifications are for signing in on another device, whereas the source says you get notified when you sign in on another device — actually the ordering reverses the meaning of "receive tabs".
    - Current: `टैब पाने और किसी अन्य डिवाइस पर साइन इन करने की सूचना पाने के लिए इसे चालू रखना ज़रूरी है।`
    - Source: `This must be turned on to receive tabs and get notified when you sign in on another device.`
    - Suggest: `टैब पाने और किसी अन्य डिवाइस पर साइन इन करने पर सूचना पाने के लिए इसे चालू रखना ज़रूरी है।`
    - "साइन इन करने की सूचना" reads as "notification of signing in" as a purpose; the source means notification when you sign in on another device. Minor but changes the sentence structure.
- `Settings.Rollouts.Message.v148` — `hi-IN/firefox-ios.xliff` — "%@ will improve features" is rendered as Firefox improving "its own features" and the sentence adds "between updates" as "between separate updates being given", altering the claim slightly.
    - Current: `अलग-अलग अपडेट दिए जाने के बीच %@ अपने फ़ीचर्स, प्रदर्शन और स्थिरता में सुधार करेगा।`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `%@ अपडेट के बीच फ़ीचर्स, प्रदर्शन और स्थिरता में सुधार करेगा।`
    - The source says improvements happen between updates; the Hindi's "अलग-अलग अपडेट दिए जाने के बीच" is a wordy re-reading, but the main issue is the awkward paraphrase; meaning is largely preserved.
- `Summarizer.Error.RateLimited.Message.v142` — `hi-IN/firefox-ios.xliff` — Rate-limit message says "cannot handle this" but source hedges with "at the moment" — the Hindi drops the temporal hedge into "अभी नहीं संभाल सकते" which is fine; however "इसे" loses reference to page.
    - Current: `इसे अभी नहीं संभाल सकते। बाद में फिर कोशिश करें!`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `इसे इस समय नहीं संभाल सकते। बाद में फिर कोशिश करें!`
    - Minor; the hedge "at the moment" is retained via "अभी".
- `ContextualHints.Toolbar.Bottom.Description.v107` — `hi-IN/firefox-ios.xliff` — "if that's more your style" is rendered as "if you like more", losing the meaning.
    - Current: `अगर आपको ज़्यादा पसंद हो, तो टूलबार को सबसे ऊपर ले जाएं।`
    - Source: `Move the toolbar to the top if that’s more your style.`
    - Suggest: `अगर आपको यह तरीका ज़्यादा पसंद हो, तो टूलबार को सबसे ऊपर ले जाएं।`
    - The source says "if that's more your style", i.e. if moving the toolbar to the top suits you better; the Hindi "अगर आपको ज़्यादा पसंद हो" has no referent and reads as an incomplete comparison.
- `ContextualHints.Toolbar.Top.Description.v107` — `hi-IN/firefox-ios.xliff` — "if that's more your style" is rendered as "if you like more", losing the referent.
    - Current: `अगर आपको ज़्यादा पसंद हो, तो टूलबार को सबसे नीचे ले जाएं।`
    - Source: `Move the toolbar to the bottom if that’s more your style.`
    - Suggest: `अगर आपको यह तरीका ज़्यादा पसंद हो, तो टूलबार को सबसे नीचे ले जाएं।`
    - The source says "if that's more your style"; the Hindi comparative lacks the referent and reads as an incomplete comparison.
- `Translations.AutoTranslatePrompt.Message.v151` — `hi-IN/firefox-ios.xliff` — Plural "pages" rendered as singular "पेज का" and the question is phrased as a command-like request rather than about automatic translation of pages generally.
    - Current: `उपलब्ध होने पर पेज का अपने आप अनुवाद करें?`
    - Source: `Automatically translate pages when available?`
    - Suggest: `उपलब्ध होने पर पेजों का अपने आप अनुवाद करें?`
    - The source asks about automatically translating pages (plural) when translation is available.
- `WebCompatReporter.Preview.Data.PageElements.v155` — `hi-IN/firefox-ios.xliff` — "have been known to cause site issues" is rendered as a flat statement that these elements cause site problems, dropping the hedge.
    - Current: `पेज के उन एलिमेंट की जानकारी जिनसे साइट में समस्याएं आती हैं`
    - Source: `Information about page elements that have been known to cause site issues`
    - Suggest: `पेज के उन एलिमेंट की जानकारी जिनसे साइट में समस्याएं आने की जानकारी मिली है`
    - The en-US says elements "have been known to cause" issues; the Hindi asserts they do cause issues, stating a certainty the source does not.
- `WorldCup.HomepageWidget.GroupPhase.RelatedMatchesLabel.v151` — `hi-IN/firefox-ios.xliff` — "Related matches" rendered as "similar matches".
    - Current: `मिलते-जुलते मैच`
    - Source: `Related matches`
    - Suggest: `संबंधित मैच`
    - "मिलते-जुलते" means 'similar/resembling', not 'related'; the section lists a team's other matches in the group phase.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `hi-IN/firefox-ios.xliff` — "might not work" is rendered as a definite "काम नहीं कर सकते" losing the hedge of possibility.
    - Current: `लेकिन कुछ बटन, फ़ॉर्म और लॉगिन फ़ील्ड काम नहीं कर सकते।`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `लेकिन कुछ बटन, फ़ॉर्म और लॉगिन फ़ील्ड काम न कर सकें।`
    - The English hedges with "might not work"; the Hindi 'काम नहीं कर सकते' reads as 'cannot work', a stronger claim about the product's behaviour.
- `Menu.TrackingProtectionDescription.ContentTrackers` — `hi-IN/firefox-ios.xliff` — "that contains hidden trackers" (possibility) is rendered as a definite statement that hidden trackers are present.
    - Current: `जिनमें छिपे हुए ट्रैकर होते हैं`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `जिनमें छिपे हुए ट्रैकर हो सकते हैं`
    - The source says websites may load content that contains hidden trackers; the Hindi asserts as fact that such content contains hidden trackers.

### C. Grammar, agreement & spelling

- `MainMenu.SiteProtection.AdBlocker.Title.v153` — `hi-IN/firefox-ios.xliff` — "Ad Blocker" transliterated as "ऐड ब्लॉकर" which reads as "add blocker"; the standard Hindi transliteration for advertisement is "विज्ञापन" or "ऐड्स" — here it should be "विज्ञापन ब्लॉकर".
    - Current: `ऐड ब्लॉकर`
    - Source: `Ad Blocker`
    - Suggest: `विज्ञापन ब्लॉकर`
    - The source refers to blocking advertisements; "ऐड" is ambiguous/incorrect transliteration and the established Hindi term is "विज्ञापन".
- `Onboarding.Modern.BrandRefresh.Welcome.Title.v148` — `hi-IN/firefox-ios.xliff` — Plural "trackers" rendered as singular ट्रैकर without plural marking.
    - Current: `पीछा करने वाले ट्रैकर को अलविदा कहें`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `पीछा करने वाले ट्रैकर्स को अलविदा कहें`
    - Source is plural "creepy trackers"; Hindi reads as singular.
- `Mark as Unread` — `hi-IN/firefox-ios.xliff` — Missing postposition makes the phrase ungrammatical compared with the parallel "Mark as Read" string.
    - Current: `अपठित मार्क करें`
    - Source: `Mark as Unread`
    - Suggest: `अपठित के रूप में मार्क करें`
    - "Mark as Unread" needs a marker such as 'के रूप में'; also 'अपठित' is a register mismatch with the colloquial 'पढ़ा हुआ' used in the sibling string.

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

_Nothing in this category._

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

### Fixed to date (79)

- `NSMicrophoneUsageDescription` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Bookmarks.DeleteFolderWarning.Title` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Send to Device` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Use your fingerprint to access Logins now.` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `This action will clear all of your private data, including history from your synced devices.` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `DefaultBrowserOnboarding.Description2` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Find in Page` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Next in-page result` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Previous in-page result` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `ActivityStream.ContextMenu.AddToShortcuts` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `ActivityStream.JumpBackIn.SectionTitle` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Added page to Reading List` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Bookmarks.NewFolder.Label` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `BreachAlerts.Link` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Changes color theme.` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Could not add page to Reading list` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `CoverSheet.v24.ETP.Description` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `CoverSheet.v24.ETP.Title` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Downloads.CancelDialog.Resume` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Enter your password to connect` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `ErrorPages.CertWarning.Description` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Forward` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `FxAPush_DeviceConnected_body` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `FxAPush_DeviceDisconnected_UnknownDevice_body` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `HistoryPanel.ClearHistoryMenuOptionTodayAndYesterday` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `HistoryPanel.EmptySyncedTabsPanelNotSignedInState.Description` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Hotkeys.Forward.DiscoveryTitle` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Hotkeys.ShowPreviousTab.DiscoveryTitle` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `LoginsList.Title` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Looks like Firefox crashed previously. Would you like to restore your tabs?` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Menu.ReadingList.Label` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Menu.ReloadWithoutTrackingProtection.Title` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Menu.TrackingProtectionDescription.ContentTrackers` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Menu.TrackingProtectionDescription.CryptominersNew` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Oops! Firefox crashed` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `Open Tabs` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `OpenURL.Error.Message` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `PhotoLibrary.FirefoxWouldLikeAccessMessage` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
- `PhotoLibrary.FirefoxWouldLikeAccessTitle` — `hi-IN/firefox-ios.xliff` — fixed 2026-09-28
