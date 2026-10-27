# Firefox iOS l10n QA — th

| | |
|---|---|
| **Generated** | 2026-10-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7f349c067169` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7f349c067169` |
| **Previous run** | 2026-10-19 @ `ec61063c1c68` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,885 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for th: [android](android.md)

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
| Files | 96 |
| Strings | 1,885 |
| Missing strings | 88 |
| Obsolete strings | 0 |
| Files absent from the locale | 2 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**88 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en-US.lproj/VPN.strings` — 20
- `th/firefox-ios.xliff` — 18
- `th/firefox-ios.xliff` — 18
- `th/firefox-ios.xliff` — 12
- `Shared/Supporting Files/en-US.lproj/BrowserDataTransfer.strings` — 11
- `th/firefox-ios.xliff` — 2
- `th/firefox-ios.xliff` — 2
- `th/firefox-ios.xliff` — 2
- `th/firefox-ios.xliff` — 2
- `th/firefox-ios.xliff` — 1

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/BrowserDataTransfer.strings`
- `Shared/Supporting Files/en-US.lproj/VPN.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 6, `curly-double` 5 | _mixed_ |
| apostrophe | `typographic` 6 | **typographic** |
| ellipsis | `char` 25 | **char** |
| dash | `em` 1, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (36)

> **Reads as a deliberate edit (1).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `th/firefox-ios.xliff` — "and that you use it" is rendered as "and how you use it", which says more data is shared with marketing partners than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ %2$@`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้งานอยู่ ให้กับพันธมิตรด้านการตลาดของ %2$@`
    - The source shares only the fact that the user uses the app, not how they use it. The Thai says details of how the user uses it are shared with Mozilla's marketing partners. That is a wider data-sharing claim than the source makes.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 18 |
| 3 | Degraded language (grammar, spelling, terminology) | 11 |
| 4 | Cosmetic (typography, spacing) | 7 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.Menu.DeletedBookmark.v131` — `th/firefox-ios.xliff` — The toast confirming a completed deletion reads as the command "Delete …" because it has no completion marker.
    - Current: `ลบ “%@”`
    - Source: `Deleted “%@”`
    - Suggest: `ลบ “%@” แล้ว`
    - The en-US "Deleted" reports that the action is done. Without "แล้ว", Thai "ลบ" reads as a command or an action label. The sibling toasts in the same file ("บันทึกใน “%@” แล้ว") use "แล้ว" for completed actions.
- `Addresses.EditAddress.AutofillAddressPrefecture.v129` — `th/firefox-ios.xliff` — 'Prefecture' is translated as 'อำเภอ' (district), which is the wrong administrative level; Japanese prefectures are 'จังหวัด' in Thai.
    - Current: `อำเภอ`
    - Source: `Prefecture`
    - Suggest: `จังหวัด`
    - The comment describes prefectures as a major administrative division in Japan. In Thai these are called จังหวัด. อำเภอ is a lower-level district.
- `Addresses.EditAddress.AutofillAddressState.v129` — `th/firefox-ios.xliff` — 'State' as an address field is translated as 'สถานะ' (status/condition) instead of the territorial state 'รัฐ'.
    - Current: `สถานะ`
    - Source: `State`
    - Suggest: `รัฐ`
    - The developer comment says this is the state field of an address (e.g., USA). 'สถานะ' means status, not a political state.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Fingerprinter.v129` — `th/firefox-ios.xliff` — "Fingerprinters" is rendered as "digital fingerprints" rather than the trackers that collect them.
    - Current: `ลายนิ้วมือดิจิทัล`
    - Source: `Fingerprinters: %@`
    - Suggest: `ตัวเก็บลายนิ้วมือดิจิทัล`
    - The comment says the number counts fingerprinters, which are trackers. "ลายนิ้วมือดิจิทัล" names the fingerprint data itself, not the trackers. Thai Firefox uses "ตัวเก็บลายนิ้วมือดิจิทัล", which also fits the "ตัว…" pattern of "ตัวติดตาม" on the same screen.
- `LibraryPanel.Sections.LastSevenDays.v138` — `th/firefox-ios.xliff` — "7 วันที่แล้ว" reads as "7 days ago" rather than the range "Last 7 Days", unlike the sibling section titles.
    - Current: `7 วันที่แล้ว`
    - Source: `Last 7 Days`
    - Suggest: `7 วันที่ผ่านมา`
    - The comment describes a section covering history from the last 7 days, which is a range. "…ที่แล้ว" usually means a point in time ("7 days ago"). The sibling headings "4 สัปดาห์ที่ผ่านมา" and "24 ชั่วโมงที่ผ่านมา" use "ที่ผ่านมา" for the same pattern.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `th/firefox-ios.xliff` — The accessibility label reads as the action "save the submenu" instead of naming the Save submenu.
    - Current: `บันทึกเมนูย่อย`
    - Source: `Save submenu`
    - Suggest: `เมนูย่อยบันทึก`
    - The developer comment says this labels the submenu called Save. In Thai, บันทึกเมนูย่อย is a verb phrase meaning "save the submenu". With the noun first, as in the sibling label เมนูย่อยของเครื่องมือ (Tools submenu), it names the submenu correctly.
- `Onboarding.IntroDescriptionPart1.v114` — `th/firefox-ios.xliff` — "For good" is rendered as เพื่อความถูกต้อง ("for correctness"), which changes the meaning.
    - Current: `เพื่อความถูกต้อง`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `เพื่อสิ่งที่ดี`
    - "For good" in the slogan means for the greater good, i.e. doing good. ความถูกต้อง means correctness or rightness, which is a different idea.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `th/firefox-ios.xliff` — "and that you use it" is rendered as "and how you use it", which says more data is shared with marketing partners than the source does.
    - Current: `และคุณใช้มันอย่างไรกับพันธมิตรด้านการตลาดของ %2$@`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `และการที่คุณใช้งานอยู่ ให้กับพันธมิตรด้านการตลาดของ %2$@`
    - The source shares only the fact that the user uses the app, not how they use it. The Thai says details of how the user uses it are shared with Mozilla's marketing partners. That is a wider data-sharing claim than the source makes.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `th/firefox-ios.xliff` — "won’t sell you out" is translated as "won't abandon you" (ไม่ทอดทิ้งคุณ).
    - Current: `ไม่ทอดทิ้งคุณ`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `ไม่ขายข้อมูลของคุณ`
    - "Sell you out" means betray you or sell your data, which is a privacy promise. ทอดทิ้ง means abandon or desert, so the Thai loses the meaning.
- `Onboarding.Modern.TermsOfService.Subtitle.v140` — `th/firefox-ios.xliff` — "Automatic tracking protection" is rendered as "protect tracking automatically", which reverses the meaning.
    - Current: `ปกป้องการติดตามอัตโนมัติ`
    - Source: `Load sites lightning fast Automatic tracking protection Sync on all your devices`
    - Suggest: `ป้องกันการติดตามอัตโนมัติ`
    - In Thai, 'ปกป้องการติดตาม' means protecting the tracking itself. The source means protection against tracking, and the usual term for that is 'ป้องกันการติดตาม' (prevent tracking).
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `th/firefox-ios.xliff` — Translation says a new mask was picked for reuse, contradicting the source's reuse of an existing mask.
    - Current: `เราจึงเลือกตัวหนึ่งใหม่ให้คุณใช้ซ้ำ`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `เราจึงเลือกตัวหนึ่งให้คุณใช้ซ้ำ`
    - The source and developer comment say an existing mask is chosen at random for reuse. Adding 'ใหม่' (new) makes it read as a newly created/selected new mask, which is contradictory and misleading.
- `ContextualHints.Summarize.Description.v142` — `th/firefox-ios.xliff` — The Thai adds a sentence saying summarization can be inaccurate; the source contextual hint has no such sentence.
    - Current: `โปรดทราบ: การสรุปอาจเกิดความคลาดเคลื่อนได้`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - The source is only 'Tap to summarize this page. Touch and hold for Reader View.' The added 'Note: summarization can be inaccurate' looks carried over from the footnote string, and it puts an admission into this hint that the source never makes.
- `LibraryPanel.History.LastSevenDaysOption.v138` — `th/firefox-ios.xliff` — "Last 7 Days" is rendered as "7 วันที่แล้ว" ("7 days ago") rather than "the past 7 days".
    - Current: `7 วันที่แล้ว`
    - Source: `Last 7 Days`
    - Suggest: `7 วันที่ผ่านมา`
    - The option clears history for the past 7 days. "7 วันที่แล้ว" means "7 days ago", which points to one day in the past. It also doesn't match the sibling options "4 สัปดาห์ที่ผ่านมา" and "24 ชั่วโมงที่ผ่านมา" on the same action sheet.
- `LibraryPanel.History.SyncedHistory.v100` — `th/firefox-ios.xliff` — "ประวัติการซิงค์" means "history of sync operations", not "history that was synced from other devices".
    - Current: `ประวัติการซิงค์`
    - Source: `Synced History`
    - Suggest: `ประวัติที่ซิงค์`
    - The comment says this option shows the user's browsing history from synced tabs. "ประวัติการซิงค์" reads as a log of syncing activity. The same file already says "ประวัติที่ซิงค์" for synced history in LibraryPanel.History.ClearHistoryMenuTitle.v100.
- `Menu.RemovePin.Confirm2.v99` — `th/firefox-ios.xliff` — The confirmation toast has no completion marker, so it reads as the command "Remove from Shortcuts" instead of saying the item was removed.
    - Current: `ลบออกจากคำสั่งลัด`
    - Source: `Removed from Shortcuts`
    - Suggest: `ลบออกจากคำสั่งลัดแล้ว`
    - The source is a past-tense confirmation toast ("Removed from Shortcuts"). The Thai matches the button label Menu.RemovedFromShortcuts.v99 word for word and reads as an instruction. The other confirmation toasts in this file end with แล้ว (e.g. เพิ่มไปยังคำสั่งลัดแล้ว, เอาออกจากรายการอ่านแล้ว).
- `Menu.TrackingProtectionDescription.CryptominersNew` — `th/firefox-ios.xliff` — 'secretly' is left out, so the Thai no longer says the computing power is used without the user knowing.
    - Current: `ตัวขุดเหรียญคริปโตดิจิตอลใช้พลังการคำนวณ`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `ตัวขุดเหรียญคริปโตดิจิทัลแอบใช้พลังการคำนวณ`
    - The source says cryptominers 'secretly use' computing power. The Thai drops 'แอบ', so the covert part of the warning is lost.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `th/firefox-ios.xliff` — The Thai says blocking reduces the number of social media companies that can see your activity, not how much they can see.
    - Current: `จะช่วยลดจำนวนบริษัทสื่อสังคมออนไลน์ที่สามารถดูว่าคุณออนไลน์อะไรบ้าง`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `จะช่วยลดสิ่งที่บริษัทสื่อสังคมออนไลน์สามารถมองเห็นว่าคุณทำอะไรทางออนไลน์`
    - The source says blocking reduces how much social media companies can see. 'ลดจำนวนบริษัท' means 'reduces the number of companies', which is a different claim.
- `SendTo.NoDevicesFound.Message` — `th/firefox-ios.xliff` — The translation leaves out "other", so it says the user has no devices at all connected to the account.
    - Current: `คุณไม่มีอุปกรณ์ใด ๆ`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `คุณไม่มีอุปกรณ์อื่นใด ๆ`
    - The source says there are no *other* devices connected to this Firefox Account. Without อื่น, the Thai claims no devices are connected at all, which is false because the current device is connected.

### C. Grammar, agreement & spelling

- `Onboarding.Welcome.Close.AccessibilityLabel.v121` — `th/firefox-ios.xliff` — The app name is placed between "exit" and "onboarding", so the label reads like "close and exit Firefox, onboarding".
    - Current: `ออกจาก %@ การเริ่มต้นใช้งาน`
    - Source: `Close and exit %@ onboarding`
    - Suggest: `ออกจากการเริ่มต้นใช้งาน %@`
    - The source means exiting the app's onboarding. Thai puts the modifier after the noun (การเริ่มต้นใช้งาน %@). The current order splits the phrase and suggests exiting the app itself.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `th/firefox-ios.xliff` — The app name sits in front of the noun, so the Thai reads like 'turned off Firefox all notifications'.
    - Current: `คุณได้ปิด %1$@ การแจ้งเตือนทั้งหมดแล้ว`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `คุณได้ปิดการแจ้งเตือนทั้งหมดของ %1$@ แล้ว`
    - In Thai, a modifier like the app name comes after the noun 'การแจ้งเตือน' (notifications). Putting %1$@ before it is ungrammatical and misparses the source 'all %1$@ notifications'.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `th/firefox-ios.xliff` — 'ดิจิตอล' is a non-standard spelling and doesn't match 'ดิจิทัล', which appears later in the same sentence.
    - Current: `คริปโตดิจิตอล`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `คริปโตดิจิทัล`
    - The Royal Institute spelling is 'ดิจิทัล', and the rest of this string and the screen use that spelling.
- `Settings.Passwords.FingerPrintReason.v103` — `th/firefox-ios.xliff` — The nominalizer "การ" is wrongly placed before the noun "รหัสผ่าน", which makes the phrase ungrammatical.
    - Current: `เข้าถึงการรหัสผ่าน`
    - Source: `Use your fingerprint to access passwords now.`
    - Suggest: `เข้าถึงรหัสผ่าน`
    - The source says "access passwords". "การ" turns verbs into nouns and cannot go before a noun like "รหัสผ่าน", so "การรหัสผ่าน" is ungrammatical Thai.
- `Toasts.Undo` — `th/firefox-ios.xliff` — The sara am vowel is written as nikhahit plus sara aa (ํ + า) instead of the single character ำ.
    - Current: `เลิกทํา`
    - Source: `Undo`
    - Suggest: `เลิกทำ`
    - Thai spelling uses the single character U+0E33 (ำ). The two-character form (U+0E4D U+0E32) looks the same but is misspelled at the character level. It also doesn't match "เลิกทำ" in Tabs.DeleteAllUndo.Button, and it can break search, sorting and VoiceOver.

### D. Terminology, register & consistency

- `MainMenu.Submenus.Save.AccessibilityLabels.RemoveFromShortcuts.Title.v132` — `th/firefox-ios.xliff` — 'Shortcuts' is rendered as คำสั่งลัด here but as ทางลัด in the matching Add to Shortcuts accessibility labels.
    - Current: `ลบออกจากคำสั่งลัด`
    - Source: `Remove from Shortcuts`
    - Suggest: `ลบออกจากทางลัด`
    - The paired labels on the same menu use ทางลัด for the homepage shortcuts (เพิ่มทางลัด, subtitle ทางลัด). คำสั่งลัด names a different concept.
- `MainMenu.Submenus.Save.RemoveFromShortcuts.Title.v131` — `th/firefox-ios.xliff` — 'Shortcuts' is rendered as คำสั่งลัד here but as ทางลัด in the matching Add to Shortcuts strings on the same menu.
    - Current: `ลบออกจากคำสั่งลัด`
    - Source: `Remove from Shortcuts`
    - Suggest: `ลบออกจากทางลัด`
    - These are the homepage shortcuts, which the same Save submenu calls ทางลัด (เพิ่มทางลัด, subtitle ทางลัด). คำสั่งลัด suggests command shortcuts like iOS Shortcuts, which is a different feature.
- `Onboarding.Customization.Toolbar.Continue.Action.v123` — `th/firefox-ios.xliff` — "Browsing" is rendered as เรียกดู here but as ท่องเว็บ in the sibling "Start Browsing" button in the same flow.
    - Current: `เริ่มการเรียกดู`
    - Source: `Save and Start Browsing`
    - Suggest: `เริ่มการท่องเว็บ`
    - These are both buttons on the same onboarding customization cards. "Start Browsing" is เริ่มการท่องเว็บ, so "Save and Start Browsing" should use the same term.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendCrashReportsTitle.v140` — `th/firefox-ios.xliff` — "Crash reports" is translated differently in this toggle title and in its description on the same screen.
    - Current: `ส่งรายงานความผิดพลาดโดยอัตโนมัติ`
    - Source: `Automatically send crash reports`
    - Suggest: `ส่งรายงานข้อขัดข้องโดยอัตโนมัติ`
    - The description on the same Manage Privacy Preferences screen uses 'รายงานข้อขัดข้อง', which is the usual Firefox term for crash reports. The title switches to 'รายงานความผิดพลาด'.
- `Onboarding.TermsOfService.PrivacyPreferences.SendCrashReportsTitle.v135` — `th/firefox-ios.xliff` — On the same screen, "crash reports" is translated as "รายงานความผิดพลาด" in the switch title but as "รายงานข้อขัดข้อง" in its description.
    - Current: `ส่งรายงานความผิดพลาดโดยอัตโนมัติ`
    - Source: `Automatically send crash reports`
    - Suggest: `ส่งรายงานข้อขัดข้องโดยอัตโนมัติ`
    - The switch title and its description sit on the same Manage Privacy Preferences screen and refer to the same feature. "รายงานข้อขัดข้อง" is the established Firefox term, and the description already uses it. "ความผิดพลาด" means "error" rather than "crash".
- `TermsOfUse.TermsOfUseHasOpened.v142` — `th/firefox-ios.xliff` — "Terms of Use" is rendered as ข้อกำหนดการใช้งาน here but as เงื่อนไขการใช้งาน in the other Terms of Use strings in this file.
    - Current: `ข้อกำหนดการใช้งาน`
    - Source: `Terms of Use sheet opened`
    - Suggest: `เงื่อนไขการใช้งาน`
    - The same source term on the same sheet should use one rendering. The title and link label use เงื่อนไขการใช้งาน, so the accessibility announcement uses a different term from what the user sees.
- `Settings.Home.Option.Wallpaper.SwitchTitle.v99` — `th/firefox-ios.xliff` — "Wallpaper" is spelled วอลเปเปอร์ here but วอลล์เปเปอร์ in the other strings on the same wallpaper screen.
    - Current: `วอลเปเปอร์`
    - Source: `Change wallpaper by tapping Firefox homepage logo`
    - Suggest: `วอลล์เปเปอร์`
    - The accessibility strings on the same wallpaper customization screen all use วอลล์เปเปอร์, so the same term is spelled two ways on one screen.

### E. Typography, punctuation & spacing

- `ContextualHints.Toolbar.Navigation.Description.v132` — `th/firefox-ios.xliff` — The string ends with a run of about 16 invisible zero-width space characters.
    - Current: `ในประวัติของแท็บนี้​​​​​​​​​​​​​​​​`
    - Source: `Tap and hold the arrows to jump between pages in this tab’s history.`
    - Suggest: `ในประวัติของแท็บนี้`
    - The source has no trailing content. The run of trailing zero-width spaces looks like paste debris and can affect layout or screen-reader output.
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `th/firefox-ios.xliff` — Missing space between "Firefox" and "เปลี่ยน" runs the two parts of the label together.
    - Current: `โลโก้ Firefoxเปลี่ยนวอลเปเปอร์`
    - Source: `Firefox logo, change the wallpaper.`
    - Suggest: `โลโก้ Firefox เปลี่ยนวอลเปเปอร์`
    - The source separates 'Firefox logo' and 'change the wallpaper' with a comma. Thai uses a space as the phrase separator, but here there is none, so the brand name runs straight into the next phrase.
- `fi3W24-2GqvPe` — `th/firefox-ios.xliff` — Closing quotation mark is a left single quote instead of a right single quote.
    - Current: `‘ไปยังลิงก์ที่คัดลอก‘`
    - Source: `There are ${count} options matching ‘Go to Copied Link’.`
    - Suggest: `‘ไปยังลิงก์ที่คัดลอก’`
    - The source pairs ‘…’; the translation closes with an opening quote ‘, giving mismatched quotation marks.
- `fi3W24-eHmH1H` — `th/firefox-ios.xliff` — Closing quotation mark is a left single quote instead of a right single quote.
    - Current: `‘ล้างแท็บส่วนตัว‘`
    - Source: `There are ${count} options matching ‘Clear Private Tabs’.`
    - Suggest: `‘ล้างแท็บส่วนตัว’`
    - The source pairs ‘…’; the translation closes with an opening quote ‘, giving mismatched quotation marks.
- `fi3W24-scEmjs` — `th/firefox-ios.xliff` — Closing quotation mark is a left single quote instead of a right single quote.
    - Current: `‘การค้นหาส่วนตัวใหม่‘`
    - Source: `There are ${count} options matching ‘New Private Search’.`
    - Suggest: `‘การค้นหาส่วนตัวใหม่’`
    - The source pairs ‘…’; the translation closes with an opening quote ‘, giving mismatched quotation marks.
- `fi3W24-xRJbBP` — `th/firefox-ios.xliff` — The closing quotation mark is an opening single quote (‘) instead of a closing one (’).
    - Current: `‘การค้นหาใหม่‘`
    - Source: `There are ${count} options matching ‘New Search’.`
    - Suggest: `‘การค้นหาใหม่’`
    - The en-US source has a matched pair, ‘New Search’. The Thai uses ‘ on both sides, so the quote is never properly closed.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/th/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
