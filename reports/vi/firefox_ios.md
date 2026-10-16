# Firefox iOS l10n QA — vi

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8c3a631663df` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8c3a631663df` |
| **Previous run** | 2026-10-16 @ `8c3a631663df` |
| **Mode** | baseline |
| **Strings reviewed this run** | 1,887 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for vi: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (68)

- `Settings.Home.Option.ThoughtProvokingStories.v116` — `vi/firefox-ios.xliff` — "Thought-Provoking" is rendered as "kích động tư tưởng", which means inciting or agitating ideology.
    - Current: `Những câu chuyện kích động tư tưởng`
    - Source: `Thought-Provoking Stories`
    - Suggest: `Những câu chuyện gợi suy ngẫm`
    - "Thought-provoking" means stimulating reflection. "Kích động" in Vietnamese means to incite or stir up, and it carries a strongly negative sense. As a result the product describes its own recommended content as inflammatory, which the source never says.
- `BrowserDataTransfer.ImportedBookmarksFolder.Title.v160` — `vi/firefox-ios.xliff` — The folder name says "imported from %@", but %@ is the import date, not a source.
    - Current: `Đã nhập từ %@`
    - Source: `Imported %@`
    - Suggest: `Đã nhập ngày %@`
    - The developer comment says %@ is the date of the import. "Từ" (from) makes it read as if the bookmarks came from a source named by the date.
- `Addresses.EditAddress.AutofillAddressDepartment.v129` — `vi/firefox-ios.xliff` — "Department" is rendered as "Bộ phận" (a section of an organization), not the administrative division used in France or Colombia.
    - Current: `Bộ phận`
    - Source: `Department`
    - Suggest: `Tỉnh`
    - The developer comment says this field is the administrative division used in countries like France and Colombia. "Bộ phận" means a department of a company or office, so the label names the wrong thing in an address form. The Vietnamese term for a French département is "Tỉnh" (or "Khu hành chính").
- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `vi/firefox-ios.xliff` — Certificate 'Subject' is rendered as 'chủ đề' (topic/theme) instead of 'chủ thể' (the entity the certificate identifies).
    - Current: `Tên chủ đề`
    - Source: `Subject Name`
    - Suggest: `Tên chủ thể`
    - Here 'Subject Name' is the certificate subject, meaning the entity the certificate is issued to. 'Chủ đề' means a topic or theme, which is the wrong sense in this context.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNames.v131` — `vi/firefox-ios.xliff` — 'Subject Alt Names' uses 'chủ đề' (topic) instead of 'chủ thể' for the certificate subject.
    - Current: `Tên chủ đề thay thế`
    - Source: `Subject Alt Names`
    - Suggest: `Tên thay thế của chủ thể`
    - Same issue as Subject Name: the certificate subject is an entity, not a topic. Both strings on this screen should use the same correct term.
- `CreditCard.ErrorState.CardNumberSublabel.v112` — `vi/firefox-ios.xliff` — Typo: “thể” instead of “thẻ” (card).
    - Current: `số thể`
    - Source: `Enter a valid card number`
    - Suggest: `số thẻ`
    - Source is “card number”; “thể” is a misspelling of “thẻ”.
- `Menu.EnhancedTrackingProtection.Details.Trackers.SocialMedia.v129` — `vi/firefox-ios.xliff` — Missing word “dõi” in “trình theo dõi” (tracker).
    - Current: `Trình theo truyền thông xã hội`
    - Source: `Social media trackers: %@`
    - Suggest: `Trình theo dõi truyền thông xã hội`
    - “Trình theo” is incomplete; tracker is “trình theo dõi”, as used in sibling strings.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Fingerprinter.v129` — `vi/firefox-ios.xliff` — “Dấu vết” (traces) does not mean fingerprinters.
    - Current: `Dấu vết`
    - Source: `Fingerprinters: %@`
    - Suggest: `Trình lấy dấu vân tay`
    - The source refers to fingerprinting trackers; “Dấu vết” means traces/marks, not the trackers being counted.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `vi/firefox-ios.xliff` — “Tracking content” rendered as “content trackers”.
    - Current: `Trình theo dõi nội dung`
    - Source: `Tracking content: %@`
    - Suggest: `Nội dung theo dõi`
    - Source category is tracking content (content that tracks), not trackers of content; the noun phrase is inverted.
- `Menu.EnhancedTrackingProtection.Details.TrackersStandardModeFooterText.v150` — `vi/firefox-ios.xliff` — “Standard” mode name mistranslated as “the commonly used standard blocker”.
    - Current: `Trình chặn tiêu chuẩn thường được sử dụng sẽ chặn`
    - Source: `Standard blocks common trackers after a page starts loading, so you may see a higher tracker count. %@`
    - Suggest: `Chế độ tiêu chuẩn chặn`
    - “Standard” is the protection mode name (parallel to the Strict footer, rendered “Chế độ nghiêm ngặt”); “thường được sử dụng” (commonly used) is not in the source.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `vi/firefox-ios.xliff` — Word order makes the label read as the command "save the submenu" instead of naming the Save submenu.
    - Current: `Lưu menu phụ`
    - Source: `Save submenu`
    - Suggest: `Menu phụ Lưu`
    - The source names the Save submenu. In Vietnamese the head noun comes first, so "menu phụ" must lead. "Lưu menu phụ" reads as a verb phrase: save the submenu.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `vi/firefox-ios.xliff` — Word order gives "tools of the submenu" instead of "the Tools submenu".
    - Current: `Công cụ menu phụ`
    - Source: `Tools submenu`
    - Suggest: `Menu phụ Công cụ`
    - The source names the Tools submenu. In Vietnamese the modifier follows the head noun, so it should be "Menu phụ Công cụ". The current text means tools belonging to a submenu.
- `NativeErrorPage.BadCertDomain.AdvancedInfo.v149` — `vi/firefox-ios.xliff` — The verb phrase after the app name is wrongly capitalised mid-sentence ("Không").
    - Current: `%1$@ Không tin tưởng`
    - Source: `%1$@ doesn’t trust this site because the certificate found isn’t valid for %2$@.`
    - Suggest: `%1$@ không tin tưởng`
    - The app name is the sentence subject, so the word that follows it continues the sentence and should be lowercase, as in the en-US "doesn’t trust".
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `vi/firefox-ios.xliff` — The second shared item ("that you use it") is missing a word to turn it into a noun phrase, so the sentence can read as "you use it with the marketing partners".
    - Current: `và bạn sử dụng nó với`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `và việc bạn sử dụng nó, với`
    - The source shares two facts: how you discovered the app, and the fact that you use it. Without "việc", the clause "bạn sử dụng nó với các đối tác tiếp thị" reads as a separate statement, or as sharing how you use it, which is more than the source says.
- `Onboarding.MultiDay.NotificationCard.BodyText.v159` — `vi/firefox-ios.xliff` — The Vietnamese is garbled: it ends with the incomplete phrase "trình chống của %@" and no longer lists the three items the source lists.
    - Current: `Nhận thông tin cập nhật, mẹo và báo cáo về quyền riêng tư của bạn về trình chống của %@.`
    - Source: `Get %@ protection updates, tips, and your privacy report.`
    - Suggest: `Nhận thông tin cập nhật về tính năng bảo vệ của %@, mẹo và báo cáo quyền riêng tư của bạn.`
    - The source lists three things: %@ protection updates, tips, and your privacy report. In the translation, "trình chống" ("protector against…") has no object, and the sentence now says the updates, tips and report are all about that unfinished phrase. The meaning is wrong and the phrase is grammatically incomplete.
- `Onboarding.Welcome.Link.Action.v114` — `vi/firefox-ios.xliff` — "Privacy notice" is rendered as "thông báo bảo mật" (security notice), inconsistent with "Thông báo về quyền riêng tư" used for the same document elsewhere in the file.
    - Current: `thông báo bảo mật`
    - Source: `Learn more in our privacy notice`
    - Suggest: `thông báo về quyền riêng tư`
    - "Bảo mật" means security/confidentiality; the en-US refers to the Privacy Notice, which Onboarding.TermsOfService.PrivacyNoticeLink.v135 translates as "Thông báo về quyền riêng tư". Same document, same file, different terms.
- `QuickAnswers.ContentView.ListeningFollowUp.v160` — `vi/firefox-ios.xliff` — Misspelling: "thểm" should be "thêm".
    - Current: `thểm`
    - Source: `Listening, ask a follow-up…`
    - Suggest: `thêm`
    - "thểm" is not a Vietnamese word. The intended word is "thêm" (more/follow-up), and the related string FollowUpButton spells it correctly.
- `PrivacyDashboard.Fingerprinters.v155` — `vi/firefox-ios.xliff` — "Fingerprinters" is translated as "Dấu vết" (traces), which doesn't name the tracker category.
    - Current: `Dấu vết`
    - Source: `Fingerprinters`
    - Suggest: `Trình lấy dấu vân tay`
    - The label names a category of blocked trackers (fingerprinters). "Dấu vết" means "traces/marks", which loses both the fingerprinting concept and the sense that this is a kind of tracker.
- `PrivacyDashboard.TrackingContent.v155` — `vi/firefox-ios.xliff` — "Tracking Content" is rendered as "content tracker" because the noun order is reversed.
    - Current: `Trình theo dõi nội dung`
    - Source: `Tracking Content`
    - Suggest: `Nội dung theo dõi`
    - The source means content that tracks you. "Trình theo dõi nội dung" means "a tracker of content", which is a different thing.
- `QuickAnswers.Tip.Title.v158` — `vi/firefox-ios.xliff` — "Ask Out Loud" is rendered as "Hỏi rõ ràng" (ask clearly), and the feature name is given as "Câu trả lời nhanh chóng" instead of the established "Trả lời nhanh".
    - Current: `Hỏi rõ ràng để nhận Câu trả lời nhanh chóng`
    - Source: `Ask Out Loud for Quick Answers`
    - Suggest: `Hỏi bằng giọng nói để nhận Trả lời nhanh`
    - The source invites the user to ask by voice ("out loud"); "rõ ràng" means "clearly", which loses the voice meaning. The feature name "Quick Answers" is "Trả lời nhanh" everywhere else in this file, so "Câu trả lời nhanh chóng" doesn't match.
- `CreditCard.Settings.EmptyListDescription.v112` — `vi/firefox-ios.xliff` — "Check out" (complete a purchase) is mistranslated as "kiểm tra" (check/inspect).
    - Current: `để kiểm tra nhanh chóng cho lần sau`
    - Source: `Save your card information securely to check out faster next time.`
    - Suggest: `để thanh toán nhanh hơn vào lần sau`
    - In the en-US, "check out faster" means paying faster at checkout. "Kiểm tra" means to verify or inspect, so the sentence no longer talks about payment.
- `QuickAnswers.Settings.Footer.v158` — `vi/firefox-ios.xliff` — "Ask out loud" is rendered as "hỏi rõ ràng" (ask clearly), so the line no longer says the feature works by voice.
    - Current: `Hãy hỏi rõ ràng`
    - Source: `Ask out loud and get short answers. We don’t store your voice, questions, or answers.`
    - Suggest: `Hãy hỏi thành tiếng`
    - "Out loud" means speaking aloud, which is how this voice feature works (the next sentence mentions the voice). "Rõ ràng" means clearly, which changes the instruction.
- `Settings.AIControls.BlockedInformation.v151` — `vi/firefox-ios.xliff` — 'AI enhancements' is rendered as 'tính năng nâng cao AI' here but as 'cải tiến AI' in the toggle title and description on the same screen.
    - Current: `Các tính năng nâng cao AI mới và hiện tại`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Các cải tiến AI mới và hiện tại`
    - On the same AI Controls screen, 'Block AI Enhancements' is 'Chặn cải tiến AI' and the description uses 'cải tiến AI'. This message, shown once that toggle is on, switches to 'tính năng nâng cao AI' ('advanced AI features'), which doesn't match the term the toggle uses.
- `Settings.Search.GoogleLens.Title.v153` — `vi/firefox-ios.xliff` — The product name "Google Lens" is partly translated as "Google Ống kính".
    - Current: `Google Ống kính`
    - Source: `Google Lens`
    - Suggest: `Google Lens`
    - Google Lens is a third-party product name. It must keep its original form and be recognisable as the Google feature.
- `Settings.Search.EnginesSuggestions.Title.v124` — `vi/firefox-ios.xliff` — Invisible zero-width spaces after "từ" in the section title.
    - Current: `từ ​​công`
    - Source: `Suggestions from Search Engines`
    - Suggest: `từ công`
    - The text appears to contain stray U+200B characters, a common machine-translation artifact. They can affect line wrapping and text matching.
- `Settings.Search.PrivateSession.Description.v125` — `vi/firefox-ios.xliff` — Invisible zero-width spaces after "từ" in the description.
    - Current: `từ ​​công`
    - Source: `Show suggestions from search engines in private sessions`
    - Suggest: `từ công`
    - The text appears to contain the same stray U+200B characters as the section title, a common machine-translation artifact.
- `Settings.Summarize.FooterTitle.v142` — `vi/firefox-ios.xliff` — Translation says the setting gives access to 'summary pages' rather than the ability to summarize pages.
    - Current: `Cung cấp quyền truy cập vào các trang tóm tắt.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Cho phép tóm tắt các trang.`
    - The en-US means the toggle enables the feature to summarize pages. 'các trang tóm tắt' reads as 'the summary pages', i.e. pages that are summaries, which is a different meaning.
- `TermsOfUse.Description.v142` — `vi/firefox-ios.xliff` — "Terms" is misspelled: it says "diều khoản" (plain d) where it should say "điều khoản".
    - Current: `diều khoản`
    - Source: `We’ve introduced a %@ Terms of Use and updated our Privacy Notice.`
    - Suggest: `Điều khoản`
    - "Terms" is spelled "điều khoản", with đ. Other strings in this file use that spelling, e.g. "Điều khoản sử dụng của %@". The suggestion also capitalizes it, because it is the name of the Terms of Use document.
- `Upgrade.Welcome.Description.v114` — `vi/firefox-ios.xliff` — "people over profits" is rendered as "commitment to people for profit", reversing the mission statement.
    - Current: `Cùng cam kết với mọi người vì lợi nhuận.`
    - Source: `New colors. New convenience. Same commitment to people over profits.`
    - Suggest: `Vẫn cam kết đặt con người lên trên lợi nhuận.`
    - The source says Mozilla puts people before profits. "vì lợi nhuận" means "for profit", so the product now says it is driven by profit, the opposite of the source.
- `WebCompatReporter.AdditionalInfo.IncludeBlockedList.v154` — `vi/firefox-ios.xliff` — Ungrammatical stacking of two classifier nouns, "tính năng trình".
    - Current: `tính năng trình chống theo dõi`
    - Source: `Send list of items blocked by tracking protection`
    - Suggest: `tính năng chống theo dõi`
    - "tính năng" (feature) and "trình" (tool/program) are both head nouns. Putting them together gives an ungrammatical phrase for "tracking protection".
- `WebCompatReporter.Preview.ScreenshotAccessibilityLabel.v154` — `vi/firefox-ios.xliff` — Misplaced passive "được" makes the label read as the user being reported, not the user reporting the page.
    - Current: `trang bạn đang được báo cáo`
    - Source: `Screenshot of the page you are reporting. Double tap to view full screen.`
    - Suggest: `trang bạn đang báo cáo`
    - en-US 'the page you are reporting' is active. 'bạn đang được báo cáo' means 'you are being reported'.
- `WebCompatReporter.Preview.Data.UserAgent.v155` — `vi/firefox-ios.xliff` — "user agent" is rendered as generic "browser information", which loses what is actually sent.
    - Current: `Thông tin trình duyệt của bạn`
    - Source: `Your browser’s user agent, which includes your iOS version, %@ version, and browser engine version`
    - Suggest: `Chuỗi user agent của trình duyệt của bạn`
    - The source names the user agent specifically, and the developer comment stresses that the versions are sent only as tokens inside the user agent. 'Browser information' is vague and suggests separate data fields.
- `WebView.DocumentLoadingAccessibilityLabel.v137` — `vi/firefox-ios.xliff` — "Document" is translated as "trang" (page) instead of "tài liệu".
    - Current: `Đang tải trang`
    - Source: `Loading Document`
    - Suggest: `Đang tải tài liệu`
    - The comment says this is the custom document loading UI, so the source means a document, not a web page.
- `DefaultBrowserCard.NextLevel.Title.v108` — `vi/firefox-ios.xliff` — "Browsing" is rendered as "trình duyệt" (browser), so the title reads "Elevate the everyday browser".
    - Current: `Nâng cao trình duyệt hàng ngày`
    - Source: `Elevate Everyday Browsing`
    - Suggest: `Nâng cao trải nghiệm duyệt web hàng ngày`
    - The en-US "Everyday Browsing" refers to the activity of browsing (duyệt web), not the browser application (trình duyệt).
- `DefaultBrowserCard.PeaceOfMind.Title.v108` — `vi/firefox-ios.xliff` — "riêng tư" is used as a noun without "quyền", which is ungrammatical.
    - Current: `bảo vệ riêng tư của bạn`
    - Source: `Firefox Has Privacy Covered`
    - Suggest: `bảo vệ quyền riêng tư của bạn`
    - "Privacy" as a noun is "quyền riêng tư". This is also the term used elsewhere in the same file (e.g. PeaceOfMind.Description).
- `ActivityStream.TopSites.RowSettingFooter` — `vi/firefox-ios.xliff` — Spelling error: "Thết" should be "Thiết".
    - Current: `Thết lập hàng`
    - Source: `Set Rows`
    - Suggest: `Thiết lập hàng`
    - "Set Rows" is correctly rendered as "Thiết lập hàng"; "Thết" is not a Vietnamese word and is a typo of "Thiết".
- `ContextMenu.DownloadLinkButtonTitle` — `vi/firefox-ios.xliff` — The action "Download Link" was translated as a noun phrase meaning "a download link" instead of a command.
    - Current: `Liên kết tải xuống`
    - Source: `Download Link`
    - Suggest: `Tải xuống liên kết`
    - The developer comment says this is a context-menu item for downloading a link URL, so it must be a verb phrase. "Liên kết tải xuống" means "download link" as a noun, unlike the verb-first siblings "Sao chép liên kết" and "Chia sẻ liên kết".
- `Bookmarks.NewBookmark.Label` — `vi/firefox-ios.xliff` — "Bookmark" is rendered as "Đánh dấu" here, but as "dấu trang" in the rest of the bookmarks UI.
    - Current: `Đánh dấu mới`
    - Source: `New Bookmark`
    - Suggest: `Dấu trang mới`
    - The same screen uses "Dấu trang" for the noun bookmark ("Dấu trang", "Chỉnh sửa dấu trang"). "Đánh dấu" is the verb "to mark", so "Đánh dấu mới" can read as "mark anew".
- `CoverSheet.v24.ETP.Description` — `vi/firefox-ios.xliff` — "block even more trackers, ads, and popups" is rendered as "block many trackers, ads and popups, and more", which drops the comparison with Standard mode and adds a trailing "and more".
    - Current: `để chặn nhiều trình theo dõi, quảng cáo và cửa sổ bật lên và hơn nữa`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `để chặn nhiều trình theo dõi, quảng cáo và cửa sổ bật lên hơn nữa`
    - The en-US says Strict blocks even more trackers, ads and popups than the default mode. The Vietnamese loses that comparison and appends "và hơn nữa" ("and more"), an open-ended addition that isn't in the source.
- `FirefoxHome.Pocket.SectionTitle` — `vi/firefox-ios.xliff` — "kích động tư tưởng" means inciting/agitating ideas, a negative sense, rather than thought-provoking.
    - Current: `kích động tư tưởng`
    - Source: `Thought-Provoking Stories`
    - Suggest: `gợi suy ngẫm`
    - "Thought-Provoking" is praise: the stories make you think. In Vietnamese, "kích động" means incite or agitate, so the section title calls the stories inflammatory.
- `FirefoxHomepage.JumpBackIn.TabPickup.OpenTab.A11y.v106` — `vi/firefox-ios.xliff` — The translation is plural ("các thẻ", the tabs), but the action opens one synced tab.
    - Current: `Mở các thẻ đã đồng bộ hóa`
    - Source: `Open synced tab`
    - Suggest: `Mở thẻ đã đồng bộ hóa`
    - Both the source and the comment refer to opening the single synced tab shown in the cell, and "các" makes it plural.
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `vi/firefox-ios.xliff` — The word order turns "Reload Ignoring Cache" into "Skip reloading the cache".
    - Current: `Bỏ qua tải lại bộ nhớ đệm`
    - Source: `Reload Ignoring Cache`
    - Suggest: `Tải lại bỏ qua bộ nhớ đệm`
    - The shortcut reloads the tab and ignores the cache. The Vietnamese makes "bỏ qua" (skip) apply to the reload, so it reads as skipping a cache reload, which is not what the action does.
- `Menu.AddBookmark.Confirm` — `vi/firefox-ios.xliff` — "Bookmark" is rendered as "đánh dấu" here, while the same file uses "dấu trang" for bookmarks.
    - Current: `Đã thêm đánh dấu`
    - Source: `Bookmark Added`
    - Suggest: `Đã thêm dấu trang`
    - Menu.Bookmarks.Label and Menu.Toolbar.Bookmarks.AccessibilityLabel.v99 use "Dấu trang" for Bookmarks. "Đánh dấu" usually means "to mark", so the message is inconsistent with the rest of the menu and can be ambiguous.
- `Menu.RemoveBookmark.Confirm` — `vi/firefox-ios.xliff` — "Bookmark" is rendered as "đánh dấu" here, while the same file uses "dấu trang" for bookmarks.
    - Current: `Đã xóa đánh dấu`
    - Source: `Bookmark Removed`
    - Suggest: `Đã xóa dấu trang`
    - Menu.Bookmarks.Label and Menu.Toolbar.Bookmarks.AccessibilityLabel.v99 use "Dấu trang" for Bookmarks. "Đánh dấu" usually means "to mark", so the message is inconsistent with the rest of the menu and can be ambiguous.
- `Menu.TrackingProtectionFingerprintersBlocked.Title` — `vi/firefox-ios.xliff` — "Fingerprinters" is rendered as "Vân tay" (fingerprints), naming the data rather than the trackers.
    - Current: `Vân tay`
    - Source: `Fingerprinters`
    - Suggest: `Trình lấy dấu vân tay`
    - The source names a category of tracker that collects fingerprints. "Vân tay" just means "fingerprint", and it breaks the "Trình …" pattern used by the sibling tracker titles.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `vi/firefox-ios.xliff` — "Cryptomining scripts" is translated as "encryption scripts".
    - Current: `Các tập lệnh mã hóa`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Các tập lệnh đào tiền điện tử`
    - "mã hóa" means encryption. The source is about scripts that mine cryptocurrency.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `vi/firefox-ios.xliff` — "Reduces how much social media companies can see" became "reduces the number of social media companies that can see".
    - Current: `làm giảm số lượng công ty truyền thông xã hội có thể thấy`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `làm giảm mức độ mà các công ty truyền thông xã hội có thể thấy`
    - The source talks about how much the companies can see, not how many companies can see it.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `vi/firefox-ios.xliff` — The verb is missing in "những gì bạn trực tuyến".
    - Current: `những gì bạn trực tuyến`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `những gì bạn làm trực tuyến`
    - Without a verb the clause is ungrammatical. The intended meaning is "what you do online".
- `ReaderMode.Available.VoiceOverAnnouncement` — `vi/firefox-ios.xliff` — Reader mode is called "Chế độ đọc sách" here but "Chế độ đọc" in the same file.
    - Current: `Chế độ đọc sách`
    - Source: `Reader Mode available`
    - Suggest: `Chế độ đọc`
    - The Reader View button label and the tip both use "Chế độ đọc". The VoiceOver announcement should use the same term.
- `Settings.Disconnect.Body` — `vi/firefox-ios.xliff` — "không xóa mọi dữ liệu" reads as "won't delete all data" (implying some may be deleted) instead of "won't delete any data".
    - Current: `sẽ không xóa mọi dữ liệu duyệt web của bạn trên thiết bị này`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `sẽ không xóa bất kỳ dữ liệu duyệt web nào của bạn trên thiết bị này`
    - The en-US says Firefox won't delete any browsing data. In Vietnamese, "không … mọi" means "not all", which suggests some data may be deleted. "không … bất kỳ … nào" keeps the meaning that nothing is deleted.
- `Settings.Home.Option.Wallpaper.Accessibility.DefaultWallpaper.v99` — `vi/firefox-ios.xliff` — "Clear" (plain/no image) is rendered as "rõ ràng" (obvious/distinct).
    - Current: `Hình nền rõ ràng mặc định.`
    - Source: `Default clear wallpaper.`
    - Suggest: `Hình nền trơn mặc định.`
    - The default wallpaper is a plain one with no image. "rõ ràng" means clear in the sense of obvious, so the label doesn't make sense.
- `Settings.Home.Option.Wallpaper.Accessibility.BeachHillsWallpaper.v100` — `vi/firefox-ios.xliff` — "Pattern" is rendered as "mô hình" (model) instead of "mẫu", which sibling strings use.
    - Current: `mô hình đồi bãi biển`
    - Source: `Firefox wallpaper, beach hills pattern.`
    - Suggest: `mẫu đồi bãi biển`
    - "mô hình" means model, not pattern. The amethyst and cerulean labels on the same screen use "mẫu".
- `Settings.Home.Option.Wallpaper.Accessibility.SunriseWallpaper.v99` — `vi/firefox-ios.xliff` — "Pattern" is rendered as "mô hình" (model) instead of "mẫu", which sibling strings use.
    - Current: `mô hình mặt trời mọc`
    - Source: `Firefox wallpaper, sunrise pattern.`
    - Suggest: `mẫu mặt trời mọc`
    - "mô hình" means model, not pattern. The amethyst and cerulean labels on the same screen use "mẫu".
- `Settings.Home.Option.Wallpaper.Accessibility.TwilightHillsWallpaper.v100` — `vi/firefox-ios.xliff` — "Pattern" is rendered as "mô hình" (model) instead of "mẫu", which sibling strings use.
    - Current: `mô hình đồi hoàng hôn`
    - Source: `Firefox wallpaper, twilight hills pattern.`
    - Suggest: `mẫu đồi hoàng hôn`
    - "mô hình" means model, not pattern. The amethyst and cerulean labels on the same screen use "mẫu".
- `Settings.SendUsage.Message` — `vi/firefox-ios.xliff` — "strives to" is dropped, turning an aspiration into a flat claim that Mozilla only collects what it needs.
    - Current: `Mozilla chỉ thu thập những gì chúng tôi cần`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `Mozilla cố gắng chỉ thu thập những gì chúng tôi cần`
    - The en-US says Mozilla 'strives to only collect' what it needs. The Vietnamese says Mozilla only collects what it needs, which is a firmer privacy promise than the source makes.
- `Settings.Studies.Toggle.Message` — `vi/firefox-ios.xliff` — "from time to time" is rendered as "theo thời gian" (over time) instead of "occasionally".
    - Current: `theo thời gian`
    - Source: `Firefox may install and run studies from time to time.`
    - Suggest: `thỉnh thoảng`
    - 'From time to time' means occasionally. 'Theo thời gian' means over time or gradually, which changes the sense.
- `Settings.TrackingProtection.ProtectionCellFooter` — `vi/firefox-ios.xliff` — "tracking your browsing" is rendered as tracking "your browser" (the app) instead of your browsing activity.
    - Current: `theo dõi trình duyệt của bạn`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `theo dõi hoạt động duyệt web của bạn`
    - "trình duyệt" is the noun "browser"; the source refers to the user's browsing activity, not the browser application.
- `Tab %@ of %@` — `vi/firefox-ios.xliff` — "của" (possessive) is wrong for a positional "X of Y"; Vietnamese uses "trên".
    - Current: `Thẻ %1$@ của %2$@`
    - Source: `Tab %1$@ of %2$@`
    - Suggest: `Thẻ %1$@ trên %2$@`
    - The comment says this means tab 2 out of 5 tabs in total; "của" means belonging to, so the VoiceOver output reads as "tab 2 belonging to 5".
- `read` — `vi/firefox-ios.xliff` — The accessibility label for a read article is translated as the bare verb "đọc" instead of the adjective "đã đọc" (already read).
    - Current: `đọc`
    - Source: `read`
    - Suggest: `đã đọc`
    - The developer comment says this is a past participle used as an adjective (the article has been read). On its own, "đọc" reads as the verb or an instruction to read. The matching label "chưa đọc" (unread) shows that "đã đọc" is the right counterpart.
- `When Leaving Private Browsing` — `vi/firefox-ios.xliff` — "Private Browsing" is rendered as "trình duyệt riêng tư" (private browser) instead of the file's established "duyệt web riêng tư".
    - Current: `trình duyệt riêng tư`
    - Source: `When Leaving Private Browsing`
    - Suggest: `duyệt web riêng tư`
    - "trình duyệt" means "browser", not "browsing". The same file renders "Private Browsing" as "Duyệt web riêng tư", so this is inconsistent and slightly wrong.
- _…and 8 more._

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
| Strings | 1,927 |
| Missing strings | 0 |
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

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 5, `curly-double` 4 | _mixed_ |
| apostrophe | `typographic` 5 | **typographic** |
| ellipsis | `char` 28 | **char** |
| dash | `em` 3, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (68)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Settings.Home.Option.ThoughtProvokingStories.v116` — `vi/firefox-ios.xliff` — "Thought-Provoking" is rendered as "kích động tư tưởng", which means inciting or agitating ideology.
    - Current: `Những câu chuyện kích động tư tưởng`
    - Source: `Thought-Provoking Stories`
    - Suggest: `Những câu chuyện gợi suy ngẫm`
    - "Thought-provoking" means stimulating reflection. "Kích động" in Vietnamese means to incite or stir up, and it carries a strongly negative sense. As a result the product describes its own recommended content as inflammatory, which the source never says.
- `Upgrade.Welcome.Description.v114` — `vi/firefox-ios.xliff` — "people over profits" is rendered as "commitment to people for profit", reversing the mission statement.
    - Current: `Cùng cam kết với mọi người vì lợi nhuận.`
    - Source: `New colors. New convenience. Same commitment to people over profits.`
    - Suggest: `Vẫn cam kết đặt con người lên trên lợi nhuận.`
    - The source says Mozilla puts people before profits. "vì lợi nhuận" means "for profit", so the product now says it is driven by profit, the opposite of the source.
- `Settings.SendUsage.Message` — `vi/firefox-ios.xliff` — "strives to" is dropped, turning an aspiration into a flat claim that Mozilla only collects what it needs.
    - Current: `Mozilla chỉ thu thập những gì chúng tôi cần`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `Mozilla cố gắng chỉ thu thập những gì chúng tôi cần`
    - The en-US says Mozilla 'strives to only collect' what it needs. The Vietnamese says Mozilla only collects what it needs, which is a firmer privacy promise than the source makes.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 32 |
| 3 | Degraded language (grammar, spelling, terminology) | 29 |
| 4 | Cosmetic (typography, spacing) | 7 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `BrowserDataTransfer.ImportedBookmarksFolder.Title.v160` — `vi/firefox-ios.xliff` — The folder name says "imported from %@", but %@ is the import date, not a source.
    - Current: `Đã nhập từ %@`
    - Source: `Imported %@`
    - Suggest: `Đã nhập ngày %@`
    - The developer comment says %@ is the date of the import. "Từ" (from) makes it read as if the bookmarks came from a source named by the date.
- `Settings.Home.Option.ThoughtProvokingStories.v116` — `vi/firefox-ios.xliff` — "Thought-Provoking" is rendered as "kích động tư tưởng", which means inciting or agitating ideology.
    - Current: `Những câu chuyện kích động tư tưởng`
    - Source: `Thought-Provoking Stories`
    - Suggest: `Những câu chuyện gợi suy ngẫm`
    - "Thought-provoking" means stimulating reflection. "Kích động" in Vietnamese means to incite or stir up, and it carries a strongly negative sense. As a result the product describes its own recommended content as inflammatory, which the source never says.
- `Addresses.EditAddress.AutofillAddressDepartment.v129` — `vi/firefox-ios.xliff` — "Department" is rendered as "Bộ phận" (a section of an organization), not the administrative division used in France or Colombia.
    - Current: `Bộ phận`
    - Source: `Department`
    - Suggest: `Tỉnh`
    - The developer comment says this field is the administrative division used in countries like France and Colombia. "Bộ phận" means a department of a company or office, so the label names the wrong thing in an address form. The Vietnamese term for a French département is "Tỉnh" (or "Khu hành chính").
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `vi/firefox-ios.xliff` — “Tracking content” rendered as “content trackers”.
    - Current: `Trình theo dõi nội dung`
    - Source: `Tracking content: %@`
    - Suggest: `Nội dung theo dõi`
    - Source category is tracking content (content that tracks), not trackers of content; the noun phrase is inverted.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Fingerprinter.v129` — `vi/firefox-ios.xliff` — “Dấu vết” (traces) does not mean fingerprinters.
    - Current: `Dấu vết`
    - Source: `Fingerprinters: %@`
    - Suggest: `Trình lấy dấu vân tay`
    - The source refers to fingerprinting trackers; “Dấu vết” means traces/marks, not the trackers being counted.
- `Menu.EnhancedTrackingProtection.Details.TrackersStandardModeFooterText.v150` — `vi/firefox-ios.xliff` — “Standard” mode name mistranslated as “the commonly used standard blocker”.
    - Current: `Trình chặn tiêu chuẩn thường được sử dụng sẽ chặn`
    - Source: `Standard blocks common trackers after a page starts loading, so you may see a higher tracker count. %@`
    - Suggest: `Chế độ tiêu chuẩn chặn`
    - “Standard” is the protection mode name (parallel to the Strict footer, rendered “Chế độ nghiêm ngặt”); “thường được sử dụng” (commonly used) is not in the source.
- `Onboarding.MultiDay.NotificationCard.BodyText.v159` — `vi/firefox-ios.xliff` — The Vietnamese is garbled: it ends with the incomplete phrase "trình chống của %@" and no longer lists the three items the source lists.
    - Current: `Nhận thông tin cập nhật, mẹo và báo cáo về quyền riêng tư của bạn về trình chống của %@.`
    - Source: `Get %@ protection updates, tips, and your privacy report.`
    - Suggest: `Nhận thông tin cập nhật về tính năng bảo vệ của %@, mẹo và báo cáo quyền riêng tư của bạn.`
    - The source lists three things: %@ protection updates, tips, and your privacy report. In the translation, "trình chống" ("protector against…") has no object, and the sentence now says the updates, tips and report are all about that unfinished phrase. The meaning is wrong and the phrase is grammatically incomplete.
- `PrivacyDashboard.Fingerprinters.v155` — `vi/firefox-ios.xliff` — "Fingerprinters" is translated as "Dấu vết" (traces), which doesn't name the tracker category.
    - Current: `Dấu vết`
    - Source: `Fingerprinters`
    - Suggest: `Trình lấy dấu vân tay`
    - The label names a category of blocked trackers (fingerprinters). "Dấu vết" means "traces/marks", which loses both the fingerprinting concept and the sense that this is a kind of tracker.
- `PrivacyDashboard.TrackingContent.v155` — `vi/firefox-ios.xliff` — "Tracking Content" is rendered as "content tracker" because the noun order is reversed.
    - Current: `Trình theo dõi nội dung`
    - Source: `Tracking Content`
    - Suggest: `Nội dung theo dõi`
    - The source means content that tracks you. "Trình theo dõi nội dung" means "a tracker of content", which is a different thing.
- `QuickAnswers.Tip.Title.v158` — `vi/firefox-ios.xliff` — "Ask Out Loud" is rendered as "Hỏi rõ ràng" (ask clearly), and the feature name is given as "Câu trả lời nhanh chóng" instead of the established "Trả lời nhanh".
    - Current: `Hỏi rõ ràng để nhận Câu trả lời nhanh chóng`
    - Source: `Ask Out Loud for Quick Answers`
    - Suggest: `Hỏi bằng giọng nói để nhận Trả lời nhanh`
    - The source invites the user to ask by voice ("out loud"); "rõ ràng" means "clearly", which loses the voice meaning. The feature name "Quick Answers" is "Trả lời nhanh" everywhere else in this file, so "Câu trả lời nhanh chóng" doesn't match.
- `CreditCard.Settings.EmptyListDescription.v112` — `vi/firefox-ios.xliff` — "Check out" (complete a purchase) is mistranslated as "kiểm tra" (check/inspect).
    - Current: `để kiểm tra nhanh chóng cho lần sau`
    - Source: `Save your card information securely to check out faster next time.`
    - Suggest: `để thanh toán nhanh hơn vào lần sau`
    - In the en-US, "check out faster" means paying faster at checkout. "Kiểm tra" means to verify or inspect, so the sentence no longer talks about payment.
- `QuickAnswers.Settings.Footer.v158` — `vi/firefox-ios.xliff` — "Ask out loud" is rendered as "hỏi rõ ràng" (ask clearly), so the line no longer says the feature works by voice.
    - Current: `Hãy hỏi rõ ràng`
    - Source: `Ask out loud and get short answers. We don’t store your voice, questions, or answers.`
    - Suggest: `Hãy hỏi thành tiếng`
    - "Out loud" means speaking aloud, which is how this voice feature works (the next sentence mentions the voice). "Rõ ràng" means clearly, which changes the instruction.
- `Settings.Search.GoogleLens.Title.v153` — `vi/firefox-ios.xliff` — The product name "Google Lens" is partly translated as "Google Ống kính".
    - Current: `Google Ống kính`
    - Source: `Google Lens`
    - Suggest: `Google Lens`
    - Google Lens is a third-party product name. It must keep its original form and be recognisable as the Google feature.
- `Settings.Summarize.FooterTitle.v142` — `vi/firefox-ios.xliff` — Translation says the setting gives access to 'summary pages' rather than the ability to summarize pages.
    - Current: `Cung cấp quyền truy cập vào các trang tóm tắt.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Cho phép tóm tắt các trang.`
    - The en-US means the toggle enables the feature to summarize pages. 'các trang tóm tắt' reads as 'the summary pages', i.e. pages that are summaries, which is a different meaning.
- `Upgrade.Welcome.Description.v114` — `vi/firefox-ios.xliff` — "people over profits" is rendered as "commitment to people for profit", reversing the mission statement.
    - Current: `Cùng cam kết với mọi người vì lợi nhuận.`
    - Source: `New colors. New convenience. Same commitment to people over profits.`
    - Suggest: `Vẫn cam kết đặt con người lên trên lợi nhuận.`
    - The source says Mozilla puts people before profits. "vì lợi nhuận" means "for profit", so the product now says it is driven by profit, the opposite of the source.
- `WebCompatReporter.Preview.Data.UserAgent.v155` — `vi/firefox-ios.xliff` — "user agent" is rendered as generic "browser information", which loses what is actually sent.
    - Current: `Thông tin trình duyệt của bạn`
    - Source: `Your browser’s user agent, which includes your iOS version, %@ version, and browser engine version`
    - Suggest: `Chuỗi user agent của trình duyệt của bạn`
    - The source names the user agent specifically, and the developer comment stresses that the versions are sent only as tokens inside the user agent. 'Browser information' is vague and suggests separate data fields.
- `WebView.DocumentLoadingAccessibilityLabel.v137` — `vi/firefox-ios.xliff` — "Document" is translated as "trang" (page) instead of "tài liệu".
    - Current: `Đang tải trang`
    - Source: `Loading Document`
    - Suggest: `Đang tải tài liệu`
    - The comment says this is the custom document loading UI, so the source means a document, not a web page.
- `DefaultBrowserCard.NextLevel.Title.v108` — `vi/firefox-ios.xliff` — "Browsing" is rendered as "trình duyệt" (browser), so the title reads "Elevate the everyday browser".
    - Current: `Nâng cao trình duyệt hàng ngày`
    - Source: `Elevate Everyday Browsing`
    - Suggest: `Nâng cao trải nghiệm duyệt web hàng ngày`
    - The en-US "Everyday Browsing" refers to the activity of browsing (duyệt web), not the browser application (trình duyệt).
- `ContextMenu.DownloadLinkButtonTitle` — `vi/firefox-ios.xliff` — The action "Download Link" was translated as a noun phrase meaning "a download link" instead of a command.
    - Current: `Liên kết tải xuống`
    - Source: `Download Link`
    - Suggest: `Tải xuống liên kết`
    - The developer comment says this is a context-menu item for downloading a link URL, so it must be a verb phrase. "Liên kết tải xuống" means "download link" as a noun, unlike the verb-first siblings "Sao chép liên kết" and "Chia sẻ liên kết".
- `CoverSheet.v24.ETP.Description` — `vi/firefox-ios.xliff` — "block even more trackers, ads, and popups" is rendered as "block many trackers, ads and popups, and more", which drops the comparison with Standard mode and adds a trailing "and more".
    - Current: `để chặn nhiều trình theo dõi, quảng cáo và cửa sổ bật lên và hơn nữa`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `để chặn nhiều trình theo dõi, quảng cáo và cửa sổ bật lên hơn nữa`
    - The en-US says Strict blocks even more trackers, ads and popups than the default mode. The Vietnamese loses that comparison and appends "và hơn nữa" ("and more"), an open-ended addition that isn't in the source.
- `FirefoxHome.Pocket.SectionTitle` — `vi/firefox-ios.xliff` — "kích động tư tưởng" means inciting/agitating ideas, a negative sense, rather than thought-provoking.
    - Current: `kích động tư tưởng`
    - Source: `Thought-Provoking Stories`
    - Suggest: `gợi suy ngẫm`
    - "Thought-Provoking" is praise: the stories make you think. In Vietnamese, "kích động" means incite or agitate, so the section title calls the stories inflammatory.
- `FirefoxHomepage.JumpBackIn.TabPickup.OpenTab.A11y.v106` — `vi/firefox-ios.xliff` — The translation is plural ("các thẻ", the tabs), but the action opens one synced tab.
    - Current: `Mở các thẻ đã đồng bộ hóa`
    - Source: `Open synced tab`
    - Suggest: `Mở thẻ đã đồng bộ hóa`
    - Both the source and the comment refer to opening the single synced tab shown in the cell, and "các" makes it plural.
- `Keyboard.Shortcuts.RefreshWithoutCache.v108` — `vi/firefox-ios.xliff` — The word order turns "Reload Ignoring Cache" into "Skip reloading the cache".
    - Current: `Bỏ qua tải lại bộ nhớ đệm`
    - Source: `Reload Ignoring Cache`
    - Suggest: `Tải lại bỏ qua bộ nhớ đệm`
    - The shortcut reloads the tab and ignores the cache. The Vietnamese makes "bỏ qua" (skip) apply to the reload, so it reads as skipping a cache reload, which is not what the action does.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `vi/firefox-ios.xliff` — "Cryptomining scripts" is translated as "encryption scripts".
    - Current: `Các tập lệnh mã hóa`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Các tập lệnh đào tiền điện tử`
    - "mã hóa" means encryption. The source is about scripts that mine cryptocurrency.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `vi/firefox-ios.xliff` — "Reduces how much social media companies can see" became "reduces the number of social media companies that can see".
    - Current: `làm giảm số lượng công ty truyền thông xã hội có thể thấy`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `làm giảm mức độ mà các công ty truyền thông xã hội có thể thấy`
    - The source talks about how much the companies can see, not how many companies can see it.
- `Menu.TrackingProtectionFingerprintersBlocked.Title` — `vi/firefox-ios.xliff` — "Fingerprinters" is rendered as "Vân tay" (fingerprints), naming the data rather than the trackers.
    - Current: `Vân tay`
    - Source: `Fingerprinters`
    - Suggest: `Trình lấy dấu vân tay`
    - The source names a category of tracker that collects fingerprints. "Vân tay" just means "fingerprint", and it breaks the "Trình …" pattern used by the sibling tracker titles.
- `Settings.Disconnect.Body` — `vi/firefox-ios.xliff` — "không xóa mọi dữ liệu" reads as "won't delete all data" (implying some may be deleted) instead of "won't delete any data".
    - Current: `sẽ không xóa mọi dữ liệu duyệt web của bạn trên thiết bị này`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `sẽ không xóa bất kỳ dữ liệu duyệt web nào của bạn trên thiết bị này`
    - The en-US says Firefox won't delete any browsing data. In Vietnamese, "không … mọi" means "not all", which suggests some data may be deleted. "không … bất kỳ … nào" keeps the meaning that nothing is deleted.
- `Settings.Home.Option.Wallpaper.Accessibility.DefaultWallpaper.v99` — `vi/firefox-ios.xliff` — "Clear" (plain/no image) is rendered as "rõ ràng" (obvious/distinct).
    - Current: `Hình nền rõ ràng mặc định.`
    - Source: `Default clear wallpaper.`
    - Suggest: `Hình nền trơn mặc định.`
    - The default wallpaper is a plain one with no image. "rõ ràng" means clear in the sense of obvious, so the label doesn't make sense.
- `Settings.SendUsage.Message` — `vi/firefox-ios.xliff` — "strives to" is dropped, turning an aspiration into a flat claim that Mozilla only collects what it needs.
    - Current: `Mozilla chỉ thu thập những gì chúng tôi cần`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `Mozilla cố gắng chỉ thu thập những gì chúng tôi cần`
    - The en-US says Mozilla 'strives to only collect' what it needs. The Vietnamese says Mozilla only collects what it needs, which is a firmer privacy promise than the source makes.
- `Settings.Studies.Toggle.Message` — `vi/firefox-ios.xliff` — "from time to time" is rendered as "theo thời gian" (over time) instead of "occasionally".
    - Current: `theo thời gian`
    - Source: `Firefox may install and run studies from time to time.`
    - Suggest: `thỉnh thoảng`
    - 'From time to time' means occasionally. 'Theo thời gian' means over time or gradually, which changes the sense.
- `Settings.TrackingProtection.ProtectionCellFooter` — `vi/firefox-ios.xliff` — "tracking your browsing" is rendered as tracking "your browser" (the app) instead of your browsing activity.
    - Current: `theo dõi trình duyệt của bạn`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `theo dõi hoạt động duyệt web của bạn`
    - "trình duyệt" is the noun "browser"; the source refers to the user's browsing activity, not the browser application.
- `read` — `vi/firefox-ios.xliff` — The accessibility label for a read article is translated as the bare verb "đọc" instead of the adjective "đã đọc" (already read).
    - Current: `đọc`
    - Source: `read`
    - Suggest: `đã đọc`
    - The developer comment says this is a past participle used as an adjective (the article has been read). On its own, "đọc" reads as the verb or an instruction to read. The matching label "chưa đọc" (unread) shows that "đã đọc" is the right counterpart.
- `TodayWidget.TopSitesGalleryTitleV2` — `vi/firefox-ios.xliff` — "Website Shortcuts" is rendered as "shortcuts on a website" instead of "shortcuts to websites".
    - Current: `Lối tắt trên trang web`
    - Source: `Website Shortcuts`
    - Suggest: `Lối tắt trang web`
    - The widget gives home-screen shortcuts to top sites. "trên trang web" means located on a website, which is the wrong meaning.

### C. Grammar, agreement & spelling

- `Menu.EnhancedTrackingProtection.Details.Trackers.SocialMedia.v129` — `vi/firefox-ios.xliff` — Missing word “dõi” in “trình theo dõi” (tracker).
    - Current: `Trình theo truyền thông xã hội`
    - Source: `Social media trackers: %@`
    - Suggest: `Trình theo dõi truyền thông xã hội`
    - “Trình theo” is incomplete; tracker is “trình theo dõi”, as used in sibling strings.
- `CreditCard.ErrorState.CardNumberSublabel.v112` — `vi/firefox-ios.xliff` — Typo: “thể” instead of “thẻ” (card).
    - Current: `số thể`
    - Source: `Enter a valid card number`
    - Suggest: `số thẻ`
    - Source is “card number”; “thể” is a misspelling of “thẻ”.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `vi/firefox-ios.xliff` — Word order makes the label read as the command "save the submenu" instead of naming the Save submenu.
    - Current: `Lưu menu phụ`
    - Source: `Save submenu`
    - Suggest: `Menu phụ Lưu`
    - The source names the Save submenu. In Vietnamese the head noun comes first, so "menu phụ" must lead. "Lưu menu phụ" reads as a verb phrase: save the submenu.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `vi/firefox-ios.xliff` — Word order gives "tools of the submenu" instead of "the Tools submenu".
    - Current: `Công cụ menu phụ`
    - Source: `Tools submenu`
    - Suggest: `Menu phụ Công cụ`
    - The source names the Tools submenu. In Vietnamese the modifier follows the head noun, so it should be "Menu phụ Công cụ". The current text means tools belonging to a submenu.
- `NativeErrorPage.BadCertDomain.AdvancedInfo.v149` — `vi/firefox-ios.xliff` — The verb phrase after the app name is wrongly capitalised mid-sentence ("Không").
    - Current: `%1$@ Không tin tưởng`
    - Source: `%1$@ doesn’t trust this site because the certificate found isn’t valid for %2$@.`
    - Suggest: `%1$@ không tin tưởng`
    - The app name is the sentence subject, so the word that follows it continues the sentence and should be lowercase, as in the en-US "doesn’t trust".
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `vi/firefox-ios.xliff` — The second shared item ("that you use it") is missing a word to turn it into a noun phrase, so the sentence can read as "you use it with the marketing partners".
    - Current: `và bạn sử dụng nó với`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `và việc bạn sử dụng nó, với`
    - The source shares two facts: how you discovered the app, and the fact that you use it. Without "việc", the clause "bạn sử dụng nó với các đối tác tiếp thị" reads as a separate statement, or as sharing how you use it, which is more than the source says.
- `QuickAnswers.ContentView.ListeningFollowUp.v160` — `vi/firefox-ios.xliff` — Misspelling: "thểm" should be "thêm".
    - Current: `thểm`
    - Source: `Listening, ask a follow-up…`
    - Suggest: `thêm`
    - "thểm" is not a Vietnamese word. The intended word is "thêm" (more/follow-up), and the related string FollowUpButton spells it correctly.
- `TermsOfUse.Description.v142` — `vi/firefox-ios.xliff` — "Terms" is misspelled: it says "diều khoản" (plain d) where it should say "điều khoản".
    - Current: `diều khoản`
    - Source: `We’ve introduced a %@ Terms of Use and updated our Privacy Notice.`
    - Suggest: `Điều khoản`
    - "Terms" is spelled "điều khoản", with đ. Other strings in this file use that spelling, e.g. "Điều khoản sử dụng của %@". The suggestion also capitalizes it, because it is the name of the Terms of Use document.
- `WebCompatReporter.AdditionalInfo.IncludeBlockedList.v154` — `vi/firefox-ios.xliff` — Ungrammatical stacking of two classifier nouns, "tính năng trình".
    - Current: `tính năng trình chống theo dõi`
    - Source: `Send list of items blocked by tracking protection`
    - Suggest: `tính năng chống theo dõi`
    - "tính năng" (feature) and "trình" (tool/program) are both head nouns. Putting them together gives an ungrammatical phrase for "tracking protection".
- `WebCompatReporter.Preview.ScreenshotAccessibilityLabel.v154` — `vi/firefox-ios.xliff` — Misplaced passive "được" makes the label read as the user being reported, not the user reporting the page.
    - Current: `trang bạn đang được báo cáo`
    - Source: `Screenshot of the page you are reporting. Double tap to view full screen.`
    - Suggest: `trang bạn đang báo cáo`
    - en-US 'the page you are reporting' is active. 'bạn đang được báo cáo' means 'you are being reported'.
- `DefaultBrowserCard.PeaceOfMind.Title.v108` — `vi/firefox-ios.xliff` — "riêng tư" is used as a noun without "quyền", which is ungrammatical.
    - Current: `bảo vệ riêng tư của bạn`
    - Source: `Firefox Has Privacy Covered`
    - Suggest: `bảo vệ quyền riêng tư của bạn`
    - "Privacy" as a noun is "quyền riêng tư". This is also the term used elsewhere in the same file (e.g. PeaceOfMind.Description).
- `ActivityStream.TopSites.RowSettingFooter` — `vi/firefox-ios.xliff` — Spelling error: "Thết" should be "Thiết".
    - Current: `Thết lập hàng`
    - Source: `Set Rows`
    - Suggest: `Thiết lập hàng`
    - "Set Rows" is correctly rendered as "Thiết lập hàng"; "Thết" is not a Vietnamese word and is a typo of "Thiết".
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `vi/firefox-ios.xliff` — The verb is missing in "những gì bạn trực tuyến".
    - Current: `những gì bạn trực tuyến`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `những gì bạn làm trực tuyến`
    - Without a verb the clause is ungrammatical. The intended meaning is "what you do online".
- `Tab %@ of %@` — `vi/firefox-ios.xliff` — "của" (possessive) is wrong for a positional "X of Y"; Vietnamese uses "trên".
    - Current: `Thẻ %1$@ của %2$@`
    - Source: `Tab %1$@ of %2$@`
    - Suggest: `Thẻ %1$@ trên %2$@`
    - The comment says this means tab 2 out of 5 tabs in total; "của" means belonging to, so the VoiceOver output reads as "tab 2 belonging to 5".

### D. Terminology, register & consistency

- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNames.v131` — `vi/firefox-ios.xliff` — 'Subject Alt Names' uses 'chủ đề' (topic) instead of 'chủ thể' for the certificate subject.
    - Current: `Tên chủ đề thay thế`
    - Source: `Subject Alt Names`
    - Suggest: `Tên thay thế của chủ thể`
    - Same issue as Subject Name: the certificate subject is an entity, not a topic. Both strings on this screen should use the same correct term.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectName.v131` — `vi/firefox-ios.xliff` — Certificate 'Subject' is rendered as 'chủ đề' (topic/theme) instead of 'chủ thể' (the entity the certificate identifies).
    - Current: `Tên chủ đề`
    - Source: `Subject Name`
    - Suggest: `Tên chủ thể`
    - Here 'Subject Name' is the certificate subject, meaning the entity the certificate is issued to. 'Chủ đề' means a topic or theme, which is the wrong sense in this context.
- `Onboarding.Welcome.Link.Action.v114` — `vi/firefox-ios.xliff` — "Privacy notice" is rendered as "thông báo bảo mật" (security notice), inconsistent with "Thông báo về quyền riêng tư" used for the same document elsewhere in the file.
    - Current: `thông báo bảo mật`
    - Source: `Learn more in our privacy notice`
    - Suggest: `thông báo về quyền riêng tư`
    - "Bảo mật" means security/confidentiality; the en-US refers to the Privacy Notice, which Onboarding.TermsOfService.PrivacyNoticeLink.v135 translates as "Thông báo về quyền riêng tư". Same document, same file, different terms.
- `Settings.AIControls.BlockedInformation.v151` — `vi/firefox-ios.xliff` — 'AI enhancements' is rendered as 'tính năng nâng cao AI' here but as 'cải tiến AI' in the toggle title and description on the same screen.
    - Current: `Các tính năng nâng cao AI mới và hiện tại`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Các cải tiến AI mới và hiện tại`
    - On the same AI Controls screen, 'Block AI Enhancements' is 'Chặn cải tiến AI' and the description uses 'cải tiến AI'. This message, shown once that toggle is on, switches to 'tính năng nâng cao AI' ('advanced AI features'), which doesn't match the term the toggle uses.
- `Bookmarks.NewBookmark.Label` — `vi/firefox-ios.xliff` — "Bookmark" is rendered as "Đánh dấu" here, but as "dấu trang" in the rest of the bookmarks UI.
    - Current: `Đánh dấu mới`
    - Source: `New Bookmark`
    - Suggest: `Dấu trang mới`
    - The same screen uses "Dấu trang" for the noun bookmark ("Dấu trang", "Chỉnh sửa dấu trang"). "Đánh dấu" is the verb "to mark", so "Đánh dấu mới" can read as "mark anew".
- `Menu.AddBookmark.Confirm` — `vi/firefox-ios.xliff` — "Bookmark" is rendered as "đánh dấu" here, while the same file uses "dấu trang" for bookmarks.
    - Current: `Đã thêm đánh dấu`
    - Source: `Bookmark Added`
    - Suggest: `Đã thêm dấu trang`
    - Menu.Bookmarks.Label and Menu.Toolbar.Bookmarks.AccessibilityLabel.v99 use "Dấu trang" for Bookmarks. "Đánh dấu" usually means "to mark", so the message is inconsistent with the rest of the menu and can be ambiguous.
- `Menu.RemoveBookmark.Confirm` — `vi/firefox-ios.xliff` — "Bookmark" is rendered as "đánh dấu" here, while the same file uses "dấu trang" for bookmarks.
    - Current: `Đã xóa đánh dấu`
    - Source: `Bookmark Removed`
    - Suggest: `Đã xóa dấu trang`
    - Menu.Bookmarks.Label and Menu.Toolbar.Bookmarks.AccessibilityLabel.v99 use "Dấu trang" for Bookmarks. "Đánh dấu" usually means "to mark", so the message is inconsistent with the rest of the menu and can be ambiguous.
- `ReaderMode.Available.VoiceOverAnnouncement` — `vi/firefox-ios.xliff` — Reader mode is called "Chế độ đọc sách" here but "Chế độ đọc" in the same file.
    - Current: `Chế độ đọc sách`
    - Source: `Reader Mode available`
    - Suggest: `Chế độ đọc`
    - The Reader View button label and the tip both use "Chế độ đọc". The VoiceOver announcement should use the same term.
- `Settings.Home.Option.Wallpaper.Accessibility.BeachHillsWallpaper.v100` — `vi/firefox-ios.xliff` — "Pattern" is rendered as "mô hình" (model) instead of "mẫu", which sibling strings use.
    - Current: `mô hình đồi bãi biển`
    - Source: `Firefox wallpaper, beach hills pattern.`
    - Suggest: `mẫu đồi bãi biển`
    - "mô hình" means model, not pattern. The amethyst and cerulean labels on the same screen use "mẫu".
- `Settings.Home.Option.Wallpaper.Accessibility.SunriseWallpaper.v99` — `vi/firefox-ios.xliff` — "Pattern" is rendered as "mô hình" (model) instead of "mẫu", which sibling strings use.
    - Current: `mô hình mặt trời mọc`
    - Source: `Firefox wallpaper, sunrise pattern.`
    - Suggest: `mẫu mặt trời mọc`
    - "mô hình" means model, not pattern. The amethyst and cerulean labels on the same screen use "mẫu".
- `Settings.Home.Option.Wallpaper.Accessibility.TwilightHillsWallpaper.v100` — `vi/firefox-ios.xliff` — "Pattern" is rendered as "mô hình" (model) instead of "mẫu", which sibling strings use.
    - Current: `mô hình đồi hoàng hôn`
    - Source: `Firefox wallpaper, twilight hills pattern.`
    - Suggest: `mẫu đồi hoàng hôn`
    - "mô hình" means model, not pattern. The amethyst and cerulean labels on the same screen use "mẫu".
- `When Leaving Private Browsing` — `vi/firefox-ios.xliff` — "Private Browsing" is rendered as "trình duyệt riêng tư" (private browser) instead of the file's established "duyệt web riêng tư".
    - Current: `trình duyệt riêng tư`
    - Source: `When Leaving Private Browsing`
    - Suggest: `duyệt web riêng tư`
    - "trình duyệt" means "browser", not "browsing". The same file renders "Private Browsing" as "Duyệt web riêng tư", so this is inconsistent and slightly wrong.
- `TodayWidget.QuickViewGalleryDescriptionV2` — `vi/firefox-ios.xliff` — "shortcuts" is translated as "phím tắt" (keyboard shortcut), while the rest of the file uses "lối tắt".
    - Current: `Thêm phím tắt vào`
    - Source: `Add shortcuts to your open tabs.`
    - Suggest: `Thêm lối tắt vào`
    - "phím tắt" means a keyboard shortcut. The widget strings elsewhere use "lối tắt" for the same concept.
- `TodayWidget.TopSitesGalleryDescription` — `vi/firefox-ios.xliff` — "shortcuts" is translated as "phím tắt" (keyboard shortcut), while the rest of the file uses "lối tắt".
    - Current: `Thêm phím tắt cho`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `Thêm lối tắt cho`
    - This is inconsistent with "Lối tắt Firefox" and the other widget shortcut strings. "phím tắt" refers to keyboard keys.

### E. Typography, punctuation & spacing

- `Settings.Search.EnginesSuggestions.Title.v124` — `vi/firefox-ios.xliff` — Invisible zero-width spaces after "từ" in the section title.
    - Current: `từ ​​công`
    - Source: `Suggestions from Search Engines`
    - Suggest: `từ công`
    - The text appears to contain stray U+200B characters, a common machine-translation artifact. They can affect line wrapping and text matching.
- `Settings.Search.PrivateSession.Description.v125` — `vi/firefox-ios.xliff` — Invisible zero-width spaces after "từ" in the description.
    - Current: `từ ​​công`
    - Source: `Show suggestions from search engines in private sessions`
    - Suggest: `từ công`
    - The text appears to contain the same stray U+200B characters as the section title, a common machine-translation artifact.
- `PzSrmZ-2GqvPe` — `vi/firefox-ios.xliff` — Straight single quotes are used where the source and sibling strings use curly quotes.
    - Current: `'Đi đến liên kết đã sao chép'`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `‘Đi đến liên kết đã sao chép’`
    - The source uses ‘ ’ and the locale uses curly quotes elsewhere (e.g. fi3W24-2GqvPe).
- `PzSrmZ-eHmH1H` — `vi/firefox-ios.xliff` — Straight single quotes are used where the source and sibling strings use curly quotes.
    - Current: `'Xóa các thẻ riêng tư'`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `‘Xóa các thẻ riêng tư’`
    - The source uses ‘ ’ and the locale uses curly quotes elsewhere.
- `PzSrmZ-scEmjs` — `vi/firefox-ios.xliff` — Straight single quotes are used where the source and sibling strings use curly quotes.
    - Current: `'Tìm kiếm riêng tư mới'`
    - Source: `Just to confirm, you wanted ‘New Private Search’?`
    - Suggest: `‘Tìm kiếm riêng tư mới’`
    - The source uses ‘ ’ and the locale uses curly quotes elsewhere.
- `PzSrmZ-xRJbBP` — `vi/firefox-ios.xliff` — Straight single quotes are used where the source and sibling strings use curly quotes.
    - Current: `'Tìm kiếm mới'`
    - Source: `Just to confirm, you wanted ‘New Search’?`
    - Suggest: `‘Tìm kiếm mới’`
    - The source uses ‘ ’ and the locale uses curly quotes elsewhere.
- `fi3W24-scEmjs` — `vi/firefox-ios.xliff` — This string puts the action name in straight single quotes, but the source and its two sibling strings use curly quotes.
    - Current: `'Tìm kiếm riêng tư mới'`
    - Source: `There are ${count} options matching ‘New Private Search’.`
    - Suggest: `‘Tìm kiếm riêng tư mới’`
    - The en-US uses ‘New Private Search’ with curly quotes. The matching vi strings fi3W24-eHmH1H and fi3W24-xRJbBP use ‘…’, so this one breaks the pattern on the same screen.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/vi/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
