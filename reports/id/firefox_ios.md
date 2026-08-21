# Firefox iOS l10n QA — id

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **Previous run** | 2026-08-21 @ `7e1ae61658ad` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,891 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for id: [android](android.md) · [firefox](firefox.md)

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
| Files | 95 |
| Strings | 1,891 |
| Missing strings | 19 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**19 strings** are not translated yet, concentrated in:

- `id/firefox-ios.xliff` — 14
- `id/firefox-ios.xliff` — 4
- `id/firefox-ios.xliff` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 4, `curly-single` 1 | **curly-double** |
| apostrophe | `typographic` 1 | **typographic** |
| ellipsis | `char` 20 | **char** |
| dash | `em` 2, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (91)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 40 |
| 3 | Degraded language (grammar, spelling, terminology) | 40 |
| 4 | Cosmetic (typography, spacing) | 11 |

### A. Functional, markup, variables & plurals

- `SentFromFirefox.SocialShare.ShareMessageA.Title.v137` — `id/firefox-ios.xliff` — The blank-line separation between the shared URL and the rest of the message is missing.
    - Current: `%1$@Dikirim dari %2$@ 🦊 Coba peramban seluler: %3$@`
    - Source: `%1$@  Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%1$@  Dikirim dari %2$@ 🦊 Coba peramban seluler: %3$@`
    - The source and the developer comment specify empty lines separating the first link parameter from the rest of the text; here the URL runs directly into the following word, breaking the shared message formatting (the parallel string ShareMessageB.Title.v137 keeps the line breaks).

### B. Mistranslation, reversed meaning, wrong names & brand

- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `id/firefox-ios.xliff` — "Post town" is translated as "Kode kota" (city code), not the town used for mail sorting.
    - Current: `Kode kota`
    - Source: `Post town`
    - Suggest: `Kota pos`
    - Source "Post town" is a town name used for mail sorting in the UK; "Kode kota" means "city code", a different concept and easily confused with the postal code field.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `id/firefox-ios.xliff` — "Townland" rendered as "Kota kecil" (small town), which is a different concept.
    - Current: `Kota kecil`
    - Source: `Townland`
    - Suggest: `Townland`
    - The developer comment states a townland is a rural land division, not a small town; "Kota kecil" means small town.
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `id/firefox-ios.xliff` — "save actions" (actions for saving) is mistranslated as "menyimpan tindakan" (saving actions).
    - Current: `hingga menyimpan tindakan`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `hingga tindakan penyimpanan`
    - The source lists menu capabilities ranging from private browsing to save actions; the Indonesian reverses the noun phrase into "saving actions", which says something different.
- `MainMenu.Account.SigningOut.Title.v154` — `id/firefox-ios.xliff` — "Signing out…" is translated as "Keluar…", which reads as the action "Sign out" rather than the in-progress state.
    - Current: `Keluar…`
    - Source: `Signing out…`
    - Suggest: `Sedang keluar…`
    - The developer comment says this is shown transiently while the user is being signed out, so the progressive state must be conveyed.
- `NativeErrorPage.Wayback.Error.LinkText.v155` — `id/firefox-ios.xliff` — Product name "Wayback Machine" was translated instead of kept as-is.
    - Current: `Mesin Wayback`
    - Source: `Wayback Machine`
    - Suggest: `Wayback Machine`
    - "Wayback Machine" is the Internet Archive's product name and is left untranslated elsewhere in this same file (Wayback.Error.Description, WaybackButtonA11yHint), creating an inconsistency.
- `Onboarding.Modern.BrandRefresh.Notification.Skip.Action.v148` — `id/firefox-ios.xliff` — "Not Now" is rendered as "Jangan Sekarang" ("Don't now"), which is not the Indonesian equivalent of "Not now".
    - Current: `Jangan Sekarang`
    - Source: `Not Now`
    - Suggest: `Nanti Saja`
    - "Not Now" means postponing; the standard Indonesian rendering is "Nanti Saja" or "Tidak Sekarang". "Jangan Sekarang" is an imperative prohibition and is not idiomatic.
- `Onboarding.Modern.BrandRefresh.Sync.Skip.Action.v148` — `id/firefox-ios.xliff` — "Not Now" is rendered as "Jangan Sekarang" ("Don't now"), which is not the Indonesian equivalent of "Not now".
    - Current: `Jangan Sekarang`
    - Source: `Not Now`
    - Suggest: `Nanti Saja`
    - "Not Now" means postponing; the standard Indonesian rendering is "Nanti Saja" or "Tidak Sekarang". "Jangan Sekarang" is an imperative prohibition and is not idiomatic.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `id/firefox-ios.xliff` — "won't sell you out" (betray you) is mistranslated as "tidak akan menjual Anda" (will not sell you).
    - Current: `tidak akan menjual Anda`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `tidak akan mengkhianati Anda`
    - "Sell you out" is an idiom meaning betray/give away your data, not literally selling the person.
- `Onboarding.Modern.BrandRefresh.Welcome.Skip.v148` — `id/firefox-ios.xliff` — "Not Now" is rendered as "Jangan Sekarang" ("Don't now"), which is not the Indonesian equivalent of "Not now".
    - Current: `Jangan Sekarang`
    - Source: `Not Now`
    - Suggest: `Nanti Saja`
    - "Not Now" means postponing; the standard Indonesian rendering is "Nanti Saja" or "Tidak Sekarang". "Jangan Sekarang" is an imperative prohibition and is not idiomatic.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `id/firefox-ios.xliff` — The sentence reverses the matching relation: the source has %@ (the app) match the device, the target tells the user to match %@ to the device but with an imperative addressed to the user.
    - Current: `atau cocokkan %@ dengan perangkat Anda`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `atau biarkan %@ menyesuaikan dengan perangkat Anda`
    - The source "have %@ match your device" means letting the app follow the device setting automatically; the translation makes it a manual user action.
- `Onboarding.Welcome.Close.AccessibilityLabel.v121` — `id/firefox-ios.xliff` — "onboarding" is rendered as "proses bergabung" (joining process), which misstates the app's onboarding/introduction flow.
    - Current: `Tutup dan keluar dari proses bergabung %@`
    - Source: `Close and exit %@ onboarding`
    - Suggest: `Tutup dan keluar dari pengenalan %@`
    - The en-US refers to the onboarding (introductory) screens, not a process of joining/membership.
- `PrivacyDashboard.TrackingContent.v155` — `id/firefox-ios.xliff` — "Tracking Content" is rendered with reversed head noun, meaning "Content Tracking" instead of content that tracks.
    - Current: `Pelacakan Konten`
    - Source: `Tracking Content`
    - Suggest: `Konten Pelacak`
    - Source refers to content that tracks (tracking content); the Indonesian reverses the head noun to say "tracking of content", parallel to the other entries like "Pelacak Media Sosial".
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `id/firefox-ios.xliff` — The prompt reverses the meaning: it asks whether to open the app rather than allow the app to open the URL.
    - Current: `Izinkan %@ untuk dibuka?`
    - Source: `Allow %@ to open?`
    - Suggest: `Izinkan %@ untuk membuka?`
    - Source "Allow %@ to open?" asks permission for the app (%@) to open the scanned URL; "untuk dibuka" (passive) means allowing the app itself to be opened.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `id/firefox-ios.xliff` — The word "perangkat" (device) is misplaced at the end, making the navigation path read as "Settings > Notifications > %2$@ device" instead of "device Settings > Notifications > %2$@".
    - Current: `Aktifkan dengan membuka Setelan > Notifikasi > %2$@ perangkat`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Aktifkan dengan membuka Setelan perangkat > Notifikasi > %2$@`
    - In en-US "device" modifies "Settings" (the first item of the path); placing "perangkat" after the app-name placeholder corrupts the settings path instruction.
- `Settings.Search.Suggest.ShowSponsoredSuggestions.Description.v124` — `id/firefox-ios.xliff` — "occasional" is mistranslated as "sesaat" (momentary/brief) instead of "sesekali/kadang-kadang".
    - Current: `saran bersponsor sesaat`
    - Source: `Support %@ with occasional sponsored suggestions`
    - Suggest: `saran bersponsor sesekali`
    - en-US "occasional sponsored suggestions" means suggestions shown from time to time; "sesaat" means brief/momentary, which changes the meaning.
- `Summarizer.Error.MissingPageContent.Message.v142` — `id/firefox-ios.xliff` — "hit summarize" is rendered as a verb phrase instead of referring to the Summarize control.
    - Current: `lalu tekan meringkas`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `lalu tekan Ringkas`
    - The source instructs the user to press the "summarize" button; "tekan meringkas" reads as "press summarizing" and does not name the control.
- `WorldCup.HomepageWidget.FTLabel.v151` — `id/firefox-ios.xliff` — "Full Time" (end of match) rendered as "Penuh Waktu" (full-time as in employment/word order reversed).
    - Current: `(Penuh Waktu)`
    - Source: `(Full Time)`
    - Suggest: `(Waktu Penuh)`
    - The label indicates the match has ended; Indonesian "Penuh Waktu" is a calque with reversed head-modifier order and does not convey end of match.
- `WorldCup.HomepageWidget.FTNoParenthesisLabel.v151` — `id/firefox-ios.xliff` — "Full Time" (end of match) rendered as "Penuh Waktu", wrong word order/meaning in Indonesian.
    - Current: `Penuh Waktu`
    - Source: `Full Time`
    - Suggest: `Waktu Penuh`
    - The label indicates the match has ended; "Penuh Waktu" reverses Indonesian head-modifier order and reads as "full-time" in the employment sense.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `id/firefox-ios.xliff` — "Match" (a football game) is mistranslated as "kecocokan" (a match/fit), inconsistent with "pertandingan" used elsewhere.
    - Current: `Info kecocokan tidak tersedia saat ini.`
    - Source: `Match info is not available right now. Try refreshing in a few minutes.`
    - Suggest: `Info pertandingan tidak tersedia saat ini.`
    - The source refers to World Cup match data; other strings in the same file translate "match" as "pertandingan". "Kecocokan" means compatibility/similarity.
- `WorldCup.HomepageWidget.RoundPhase.ThirdPlaceLabel.v151` — `id/firefox-ios.xliff` — "THIRD PLACE" (ranking) translated literally as "TEMPAT KETIGA" (third location).
    - Current: `TEMPAT KETIGA`
    - Source: `THIRD PLACE`
    - Suggest: `PERINGKAT KETIGA`
    - In a tournament context the source means third-place finisher; "tempat" means a physical place in Indonesian, not a ranking position.
- `This action will clear all of your private data, including history from your synced devices.` — `id/firefox-ios.xliff` — The translation drops "your" from "your synced devices", omitting the reference to the user's own devices.
    - Current: `termasuk riwayat dari perangkat yang tersinkronisasi`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `termasuk riwayat dari perangkat Anda yang tersinkronisasi`
    - Source says "history from your synced devices"; the possessive is dropped, making it ambiguous which devices are meant.
- `DefaultBrowserOnboarding.Screenshot` — `id/firefox-ios.xliff` — "Default Browser App" is rendered with wrong word order/meaning as "App Browser Default".
    - Current: `App Browser Default`
    - Source: `Default Browser App`
    - Suggest: `Aplikasi Peramban Baku`
    - The source refers to the iOS setting "Default Browser App"; the Indonesian word order makes "Default" modify "Browser App" incorrectly and mixes untranslated English. Also inconsistent with "Peramban Baku" used in Settings.DefaultBrowserMenuItem.
- `LibraryPanel.History.Title.v138` — `id/firefox-ios.xliff` — "other browsing data" is translated as just "data lainnya", dropping "browsing".
    - Current: `kuki, dan data lainnya`
    - Source: `Deletes history (including synced history from other devices), cookies, and other browsing data.`
    - Suggest: `kuki, dan data penjelajahan lainnya`
    - The source says "cookies, and other browsing data"; the translation drops the qualifier "browsing".
- `Added page to Reading List` — `id/firefox-ios.xliff` — The translation omits "page" and uses "Daftar Baca" instead of the consistent "Daftar Bacaan".
    - Current: `Ditambahkan ke Daftar Baca`
    - Source: `Added page to Reading List`
    - Suggest: `Halaman ditambahkan ke Daftar Bacaan`
    - Source is "Added page to Reading List"; "page" is dropped, and "Reading List" is elsewhere translated "Daftar Bacaan" (see 'Add to Reading List').
- `Could not add page to Reading List. Maybe it’s already there?` — `id/firefox-ios.xliff` — The object "page" is dropped, so the Indonesian reads "Could not add Reading List" instead of "Could not add page to Reading List".
    - Current: `Tidak dapat menambahkan Daftar Baca.`
    - Source: `Could not add page to Reading List. Maybe it’s already there?`
    - Suggest: `Tidak dapat menambahkan laman ke Daftar Baca.`
    - Source says the page could not be added to the Reading List; the translation omits "laman ke", changing the meaning.
- `ErrorPages.AdvancedWarning2.Text` — `id/firefox-ios.xliff` — The translation adds "hanya" (only) and "siap menanggung" which is not in the source.
    - Current: `Lanjutkan hanya jika Anda siap menanggung risikonya.`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `Lanjutkan jika Anda menerima potensi risikonya.`
    - Source is "Proceed if you accept the potential risk." — no "only" restriction and "potential" is dropped.
- `ErrorPages.CertWarning.Description` — `id/firefox-ios.xliff` — "To protect your information from being stolen" is rendered as "to protect the theft of your information", reversing the meaning.
    - Current: `Untuk melindungi pencurian informasi Anda`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `Untuk melindungi informasi Anda dari pencurian`
    - The source says Firefox protects your information from being stolen; the Indonesian literally says it protects the theft of your information.
- `Menu.AddPin.Confirm2` — `id/firefox-ios.xliff` — Confirmation toast "Added to Shortcuts" is translated as an imperative "Add to Shortcuts" instead of a completed-action statement.
    - Current: `Tambahkan ke Pintasan`
    - Source: `Added to Shortcuts`
    - Suggest: `Ditambahkan ke Pintasan`
    - The source is a toast confirming the item has been added (passive past), matching sibling toasts "Ditambahkan ke Daftar Bacaan" and "Dihapus dari Pintasan". "Tambahkan ke Pintasan" is the imperative button label used for Menu.AddToShortcuts.v99.
- `Menu.TrackingProtectionBlockedContent.Title` — `id/firefox-ios.xliff` — "Tracking content" is rendered as "Pelacakan konten" (tracking of content) instead of "Konten pelacak".
    - Current: `Pelacakan konten`
    - Source: `Tracking content`
    - Suggest: `Konten pelacak`
    - The source means content that contains trackers; the Indonesian reverses the head noun, saying "content tracking" instead of "tracking content".
- `Search.ThirdPartyEngines.DuplicateErrorMessage` — `id/firefox-ios.xliff` — Error message about a duplicate search engine is translated as a success message ("berhasil ditambahkan") and the title/URL scope is misplaced.
    - Current: `Mesin pencari dengan judul ini atau URL telah berhasil ditambahkan.`
    - Source: `A search engine with this title or URL has already been added.`
    - Suggest: `Mesin pencari dengan judul atau URL ini sudah pernah ditambahkan.`
    - The source says a search engine with this title or URL 'has already been added' — an error. 'telah berhasil ditambahkan' means 'was successfully added', reversing the meaning of an error dialog.
- `Settings.Siri.SectionDescription` — `id/firefox-ios.xliff` — "quickly open Firefox" mistranslated as "membuat Firefox" (make Firefox) instead of "membuka Firefox" (open Firefox).
    - Current: `untuk membuat Firefox dengan cepat`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `untuk membuka Firefox dengan cepat`
    - The source says "to quickly open Firefox"; "membuat" means "to make/create", reversing the meaning.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `id/firefox-ios.xliff` — "ad tracking" is rendered as "pelacak" (trackers), dropping the ad-tracking meaning.
    - Current: `Mengizinkan beberapa pelacak agar situs web berfungsi dengan baik.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Mengizinkan beberapa pelacakan iklan agar situs web berfungsi dengan baik.`
    - The source says "Allows some ad tracking"; the translation says "allows some trackers", losing the "ad" qualifier and changing the meaning.
- `ShareExtension.LoadInBackgroundAction.Title` — `id/firefox-ios.xliff` — "Load in Background" translated as "Muat di Belakang" (load at the back/behind) instead of background loading.
    - Current: `Muat di Belakang`
    - Source: `Load in Background`
    - Suggest: `Muat di Latar Belakang`
    - "di Belakang" means physically behind; the intended sense is background loading, which in Indonesian is "latar belakang".
- `TabTray.Title` — `id/firefox-ios.xliff` — "Open Tabs" (noun phrase, title of the tab tray) is translated as an imperative "Buka Tab" ("Open a tab").
    - Current: `Buka Tab`
    - Source: `Open Tabs`
    - Suggest: `Tab Terbuka`
    - The developer comment says this is the title for the tab tray, i.e. the list of currently open tabs, not a command to open a tab.
- `TranslationToastHandler.PromptTranslate.Title` — `id/firefox-ios.xliff` — The translation drops "to" so it reads "Translate %2$@" instead of "Translate to %2$@", and "appears to be in" is rendered as "appears in".
    - Current: `Laman ini muncul dalam bahasa %1$@. Terjemahkan %2$@ dengan %3$@?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `Laman ini tampaknya dalam bahasa %1$@. Terjemahkan ke %2$@ dengan %3$@?`
    - %2$@ is the target language; without "ke" the sentence says to translate the language itself, changing the meaning.
- `fxa.signin.use-email-instead` — `id/firefox-ios.xliff` — "Use Email Instead" is rendered as "Gunakan Surel Saja" ("Use email only"), changing the meaning.
    - Current: `Gunakan Surel Saja`
    - Source: `Use Email Instead`
    - Suggest: `Gunakan Surel Saja Gantinya`
    - "Instead" means using email as an alternative to the camera/QR sign-in, not "only". Indonesian "saja" means "only/just", which is a different meaning; a correct rendering is e.g. "Gunakan Surel Saja" → "Gunakan Surel" / "Gunakan Surel sebagai gantinya".
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `id/firefox-ios.xliff` — "any of your history or cookies" rendered as "semua riwayat atau kuki" which reads as "all history or cookies" and weakens/changes the negation scope.
    - Current: `tidak akan mengingat semua riwayat atau kuki`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `tidak akan mengingat riwayat atau kuki apa pun`
    - "tidak akan mengingat semua" is ambiguous/implies "will not remember all", whereas the source states none of the history or cookies will be remembered.
- `Off` — `id/firefox-ios.xliff` — Accessibility value "Off" is translated as the imperative verb "Nonaktifkan" (deactivate) instead of the state "Nonaktif".
    - Current: `Nonaktifkan`
    - Source: `Off`
    - Suggest: `Nonaktif`
    - The developer comment says this is a toggled OFF accessibility value, i.e. a state, not an action.
- `On` — `id/firefox-ios.xliff` — Accessibility value "On" is translated as the imperative verb "Aktifkan" (activate) instead of the state "Aktif".
    - Current: `Aktifkan`
    - Source: `On`
    - Suggest: `Aktif`
    - The developer comment says this is a toggled ON accessibility value, i.e. a state, not an action.

### C. Grammar, agreement & spelling

- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `id/firefox-ios.xliff` — "Save submenu" is rendered with wrong word order and a misspelled compound, saying "Save the submenu" instead of naming the Save submenu.
    - Current: `Simpan sub menu`
    - Source: `Save submenu`
    - Suggest: `Submenu Simpan`
    - In Indonesian the head noun comes first, so "Simpan sub menu" reads as the imperative "save the submenu"; the parallel string Tools submenu is correctly "Sub menu alat". Also "submenu" is written as one word.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `id/firefox-ios.xliff` — "submenu" is spelled as two words.
    - Current: `Sub menu alat`
    - Source: `Tools submenu`
    - Suggest: `Submenu Alat`
    - Indonesian standard spelling joins the prefix: "submenu", not "sub menu".
- `NativeErrorPage.BadCertDomain.ProceedButton.v149` — `id/firefox-ios.xliff` — Misspelling of "Berisiko".
    - Current: `Berrisiko`
    - Source: `Proceed to %@ (Risky)`
    - Suggest: `Berisiko`
    - The correct Indonesian spelling is "berisiko" (one r), not "berrisiko".
- `Onboarding.Modern.Sync.Description.v145` — `id/firefox-ios.xliff` — Possessive "Anda" is misplaced, attaching only to "sandi" instead of the whole list.
    - Current: `Markah, sandi Anda, dan lainnya disinkronkan`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `Markah, sandi, dan lainnya milik Anda disinkronkan`
    - Source is "Your bookmarks, passwords, and more" — the possessive covers the whole list, not just passwords.
- `Onboarding.Modern.TermsOfService.Description.v145` — `id/firefox-ios.xliff` — Word order makes "nirlaba" modify the company name placeholder awkwardly/incorrectly.
    - Current: `Dipersembahkan oleh %@ nirlaba`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Dipersembahkan oleh %@, organisasi nirlaba`
    - Source is "Brought to you by the non-profit %@"; in Indonesian "%@ nirlaba" reads as if the company name is a common noun being modified, which is ungrammatical for a proper name.
- `Settings.AIControls.HeaderCard.Message.v151` — `id/firefox-ios.xliff` — Awkward/ungrammatical rendering of "whether to use" using "jikalau akan".
    - Current: `Itu termasuk jikalau akan menggunakan fitur yang ditingkatkan dengan AI.`
    - Source: `That includes whether to use features enhanced with AI.`
    - Suggest: `Itu termasuk apakah akan menggunakan fitur yang ditingkatkan dengan AI.`
    - "whether" in this context is "apakah"; "jikalau" means "if/in case" and produces an ungrammatical sentence.
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `id/firefox-ios.xliff` — Missing relative pronoun makes the phrase read as a clause instead of "trackers blocked on this page".
    - Current: `Nama host pelacak diblokir di laman ini`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `Nama host pelacak yang diblokir di laman ini`
    - The source is a noun phrase "Hostnames of trackers blocked on this page"; without "yang" the Indonesian reads as a sentence "Tracker hostnames are blocked on this page".
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `id/firefox-ios.xliff` — The final clause "melihat apa yang Anda daring" is missing the verb, leaving an incomplete sentence.
    - Current: `melihat apa yang Anda daring`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `melihat apa yang Anda lakukan daring`
    - Source is "see what you do online"; the translation dropped the verb "lakukan", making it ungrammatical.
- `Tabs %@ to %@ of %@` — `id/firefox-ios.xliff` — English plural "Tabs" left untranslated/uninflected instead of Indonesian "Tab".
    - Current: `Tabs %1$@ hingga %2$@ dari %3$@`
    - Source: `Tabs %1$@ to %2$@ of %3$@`
    - Suggest: `Tab %1$@ hingga %2$@ dari %3$@`
    - Indonesian does not use the English plural -s; the sibling string "Tab %1$@ dari %2$@" uses "Tab", making this inconsistent.
- `Search Input Field` — `id/firefox-ios.xliff` — "Bidan" (midwife) is a typo for "Bidang" (field).
    - Current: `Bidan Isian Pencarian`
    - Source: `Search Input Field`
    - Suggest: `Bidang Isian Pencarian`
    - The source is "Search Input Field"; "Bidan" means midwife, the correct word is "Bidang".

### D. Terminology, register & consistency

- `Bookmarks.Menu.EditBookmarkMobileBookmarksLabel.v154` — `id/firefox-ios.xliff` — "Bookmarks" is rendered as "BOOKMARK" here while the parallel header and the rest of the file use "Markah".
    - Current: `BOOKMARK SELULER`
    - Source: `MOBILE BOOKMARKS`
    - Suggest: `MARKAH SELULER`
    - The sibling header Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136 uses "MARKAH DESKTOP", and all other strings in this file translate "bookmark(s)" as "markah"; using "BOOKMARK" on the same screen is inconsistent.
- `MainMenu.Account.AccessibilityLabels.BackButton.v132` — `id/firefox-ios.xliff` — The navigation "Back" button is rendered as "Mundur" instead of the standard "Kembali".
    - Current: `Mundur`
    - Source: `Back`
    - Suggest: `Kembali`
    - In Firefox UI the back navigation control is consistently "Kembali" in Indonesian; "Mundur" (move backwards/reverse) is not the established term for this accessibility label.
- `MainMenu.SiteProtection.Protections.Title.v153` — `id/firefox-ios.xliff` — "Protections" is translated as "Proteksi" while the adjacent protection-state strings on the same menu use "Perlindungan".
    - Current: `Proteksi`
    - Source: `Protections`
    - Suggest: `Perlindungan`
    - MainMenu.SiteProtection.ProtectionsOn/Off use "Perlindungan" for the same source term on the same top-of-menu area; the term should be consistent.
- `MainMenu.Submenus.Save.AccessibilityLabels.SaveToReadingList.Subtitle.v132` — `id/firefox-ios.xliff` — "Reading List" rendered as "Daftar Baca" while the visible label counterpart uses "Daftar Bacaan".
    - Current: `Daftar Baca`
    - Source: `Reading List`
    - Suggest: `Daftar Bacaan`
    - The corresponding visible string MainMenu.Submenus.Save.SaveToReadingList.Subtitle.v131 uses "Daftar Bacaan"; the accessibility label should match the visible term.
- `MainMenu.Submenus.Save.AccessibilityLabels.SaveToReadingList.Title.v132` — `id/firefox-ios.xliff` — "Reading List" rendered as "Daftar Baca" while the visible label counterpart uses "Daftar Bacaan".
    - Current: `Simpan ke Daftar Baca`
    - Source: `Save to Reading List`
    - Suggest: `Simpan ke Daftar Bacaan`
    - The corresponding visible string MainMenu.Submenus.Save.SaveToReadingList.Title.v131 uses "Daftar Bacaan"; inconsistent term for the same feature on the same screen.
- `MainMenu.Submenus.Save.RemoveFromReadingList.Title.v131` — `id/firefox-ios.xliff` — "Reading List" is rendered as "Daftar Baca" here but as "Daftar Bacaan" in the sibling Save submenu strings on the same screen.
    - Current: `Hapus dari Daftar Baca`
    - Source: `Remove from Reading List`
    - Suggest: `Hapus dari Daftar Bacaan`
    - Within the same Save submenu group, MainMenu.Submenus.Save.SaveToReadingList.Title/Subtitle use "Daftar Bacaan"; the same source term must be consistent on the same screen.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `id/firefox-ios.xliff` — "Turn off" is rendered as "Matikan" while the parallel Night Mode off string uses "Nonaktifkan", creating inconsistency within the same submenu.
    - Current: `Matikan Tampilan Pembaca`
    - Source: `Turn off Reader View`
    - Suggest: `Nonaktifkan Tampilan Pembaca`
    - MainMenu.Submenus.Tools.NightMode.Off.Title.v131 translates "Turn off" as "Nonaktifkan"; the same term should be used consistently in the same Tools submenu.
- `MainMenu.Submenus.Tools.Zoom.Title.v131` — `id/firefox-ios.xliff` — The noun "Zoom" is rendered as the verb "Perbesar" while the parallel subtitle uses the noun "Perbesaran".
    - Current: `Perbesar (%@)`
    - Source: `Zoom (%@)`
    - Suggest: `Perbesaran (%@)`
    - The string labels the current zoom level (a noun), and MainMenu.Submenus.Tools.Zoom.Subtitle.v131 translates "Zoom" as "Perbesaran".
- `MainMenu.ToolsSection.AccessibilityLabels.PageZoom.Title.v142` — `id/firefox-ios.xliff` — "Page Zoom" is translated as "Pembesaran Laman" here but "Zum Laman" in the other Page Zoom string.
    - Current: `Pembesaran Laman`
    - Source: `Page Zoom`
    - Suggest: `Zum Laman`
    - MainMenu.Submenus.Tools.PageZoomV2.Title.v141 renders the same source term "Page Zoom" as "Zum Laman"; the two labels refer to the same feature and must match.
- `MainMenu.ToolsSection.AccessibilityLabels.ReaderView.v150` — `id/firefox-ios.xliff` — "Reader View" is translated as "Tampilan Baca" here but "Tampilan Pembaca" elsewhere in the same file.
    - Current: `Tampilan Baca`
    - Source: `Reader View`
    - Suggest: `Tampilan Pembaca`
    - MainMenu.Submenus.Tools.ReaderView.Subtitle.v131 and the On/Off titles use "Tampilan Pembaca" for the same source term "Reader View".
- `Onboarding.Customization.Toolbar.Bottom.Action.v123` — `id/firefox-ios.xliff` — "Bottom" as a toolbar position is rendered "Dasar" (base/basic) instead of "Bawah".
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The source refers to placing the toolbar at the bottom of the screen; Indonesian for that position is "Bawah". "Dasar" means base/foundation/basic and is misleading here.
- `Onboarding.Customization.Toolbar.Top.Action.v123` — `id/firefox-ios.xliff` — "Top" as a toolbar position is rendered "Puncak" (summit/peak) instead of "Atas".
    - Current: `Puncak`
    - Source: `Top`
    - Suggest: `Atas`
    - The source refers to placing the toolbar at the top of the screen; the standard Indonesian term for that position is "Atas". "Puncak" means summit/peak and is wrong in a UI position control.
- `Onboarding.Modern.Customization.Toolbar.Bottom.Action.v140` — `id/firefox-ios.xliff` — "Bottom" as a toolbar position is translated as "Dasar" (base/basic) instead of the positional term "Bawah".
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The developer comment says this sets the toolbar at the bottom of the screen; Indonesian uses "Bawah" for that position, and "Dasar" also commonly means "basic", which is misleading.
- `Onboarding.Modern.Customization.Toolbar.Bottom.Action.v145` — `id/firefox-ios.xliff` — "Bottom" as a toolbar position is translated as "Dasar" (base/basic) instead of the positional term "Bawah".
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The developer comment says this sets the toolbar to the bottom of the screen; Indonesian uses "Bawah" for that position.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v140` — `id/firefox-ios.xliff` — "Top" as a toolbar position is translated as "Puncak" (summit/peak) instead of the positional term "Atas".
    - Current: `Puncak`
    - Source: `Top`
    - Suggest: `Atas`
    - The developer comment says this sets the toolbar at the top of the screen; Indonesian uses "Atas" for that position, while "Puncak" means a summit.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v145` — `id/firefox-ios.xliff` — "Top" as a toolbar position is translated as "Puncak" (summit/peak) instead of the positional term "Atas".
    - Current: `Puncak`
    - Source: `Top`
    - Suggest: `Atas`
    - The developer comment says this sets the toolbar to the top of the screen; Indonesian uses "Atas" for that position.
- `PrivacyDashboard.Fingerprinters.v155` — `id/firefox-ios.xliff` — "Fingerprinters" is translated literally as "Penyidik jari" (finger investigator), not the established privacy term.
    - Current: `Penyidik jari`
    - Source: `Fingerprinters`
    - Suggest: `Pengambil Sidik Jari Digital`
    - In Firefox privacy UI, "fingerprinters" are scripts that fingerprint the browser; "penyidik jari" is a literal, incorrect rendering and is also inconsistent with the title-case style of the sibling labels.
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `id/firefox-ios.xliff` — "email mask" is rendered "topeng surel" here while other strings in the same file use "masker surel".
    - Current: `topeng surel gratis`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `masker surel gratis`
    - The same feature term must be consistent within the RelayMask screen; the file otherwise uses "masker surel" (e.g. Masker Surel, Gunakan masker surel).
- `RelayMask.RelayEmailMaskInsertedA11yAnnouncement.v147` — `id/firefox-ios.xliff` — "Email mask" rendered as "Topeng surel", inconsistent with "masker surel" used elsewhere in the same file.
    - Current: `Topeng surel dimasukkan`
    - Source: `Email mask inserted`
    - Suggest: `Masker surel dimasukkan`
    - Terminology inconsistency within the RelayMask feature strings, which elsewhere use "masker surel".
- `RelayMask.RelayEmailMaskSettingsDetailInfo.v147` — `id/firefox-ios.xliff` — "email masks" rendered as "topeng surel", inconsistent with "masker surel" used elsewhere in the same file.
    - Current: `tidak mendukung topeng surel`
    - Source: `Hide your real email to protect your inbox from spam. Some sites don’t support email masks.`
    - Suggest: `tidak mendukung masker surel`
    - Terminology inconsistency within the same feature/screen; the settings title is "Masker Surel".
- `Settings.Browsing.AdBlocker.LearnMore.v155` — `id/firefox-ios.xliff` — "Learn more" is translated inconsistently within the same file ("Pelajari selengkapnya" vs "Pelajari lebih lanjut").
    - Current: `Pelajari lebih lanjut`
    - Source: `Learn more`
    - Suggest: `Pelajari selengkapnya`
    - Settings.AIControls.HeaderCard.Link.v151 in the same file renders the identical source "Learn more" as "Pelajari selengkapnya"; Firefox id standard is "Pelajari selengkapnya".
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `id/firefox-ios.xliff` — "Notifications" is rendered as "pemberitahuan" and "Notifikasi" within the same string and screen.
    - Current: `Anda menonaktifkan semua pemberitahuan %1$@. Aktifkan dengan membuka Setelan > Notifikasi > %2$@ perangkat`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Anda menonaktifkan semua notifikasi %1$@. Aktifkan dengan membuka Setelan perangkat > Notifikasi > %2$@`
    - Other strings in the Notifications settings section consistently use "Notifikasi"; using two different terms in one string is inconsistent.
- `Summarizer.HostedBrand.Label.v142` — `id/firefox-ios.xliff` — "Summarized by" is translated as "Diringkas oleh" here but as "Dirangkum oleh" in the parallel Apple Intelligence label on the same screen.
    - Current: `Diringkas oleh %@`
    - Source: `Summarized by %@`
    - Suggest: `Dirangkum oleh %@`
    - Summarizer.AppleBrand.Label.v142 uses "Dirangkum oleh Apple Intelligence" for the identical source phrase "Summarized by"; the two labels appear in the same summary report and must match.
- `TermsOfUse.TitleValue1.v147` — `id/firefox-ios.xliff` — "Terms of Use" is rendered as "Syarat Penggunaan" here but as "Ketentuan Penggunaan" in all other strings of the same screen.
    - Current: `Syarat Penggunaan`
    - Source: `Terms of Use`
    - Suggest: `Ketentuan Penggunaan`
    - TermsOfUse.Link.TermsOfUse.v142, TermsOfUse.Description.v142 and TermsOfUse.TermsOfUseHasOpened.v142 all use "Ketentuan Penggunaan" for the same source term on the same sheet; this variant title is inconsistent.
- `DefaultBrowserOnboarding.Description2` — `id/firefox-ios.xliff` — iOS Settings item is rendered with untranslated English terms "App Browser Default" instead of the Indonesian iOS wording, and the word order is wrong.
    - Current: `2. Ketuk App Browser Default`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. Ketuk Aplikasi Peramban Baku`
    - The rest of this file consistently translates "default browser" as "peramban baku"; "App Browser Default" is neither English nor correct Indonesian word order.
- `Display Settings` — `id/firefox-ios.xliff` — "Settings" is rendered as "Setelan" here while all other strings in this file use "Pengaturan".
    - Current: `Setelan Tampilan`
    - Source: `Display Settings`
    - Suggest: `Pengaturan Tampilan`
    - Inconsistent terminology: CoverSheet.v24.ETP.Settings.Button, ContextualHints.SearchBarPlacement.CallToAction and others use "Pengaturan" for Settings.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `id/firefox-ios.xliff` — "Fingerprinters" translated as "Sidik jari" (fingerprints) rather than the agent term used elsewhere ("Pelacak Sidik").
    - Current: `Sidik jari mengumpulkan berbagai pengaturan unik ini`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `Pelacak sidik jari mengumpulkan berbagai pengaturan unik ini`
    - The source refers to the trackers (fingerprinters), not fingerprints; the sibling title string uses "Pelacak Sidik", so this is inconsistent and factually wrong.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `id/firefox-ios.xliff` — "Reading List" is rendered "Daftar Baca" here but "Daftar Bacaan" elsewhere in the same file.
    - Current: `Daftar Baca`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Daftar Bacaan`
    - Inconsistent with 'Reading list' → 'Daftar bacaan' and 'Remove from Reading List' → 'Hapus dari Daftar Bacaan' in the same screen group.
- `Settings.Homepage.Shortcuts.ToggleOff.v100` — `id/firefox-ios.xliff` — "Off" and "On" pair is rendered inconsistently as "Mati"/"Aktif" instead of the matching pair "Nonaktif"/"Aktif".
    - Current: `Mati`
    - Source: `Off`
    - Suggest: `Nonaktif`
    - The two toggle-state strings appear on the same settings screen; "Aktif" is used for On, so the opposite state should be "Nonaktif" for a consistent pair.
- `PzSrmZ-2GqvPe` — `id/firefox-ios.xliff` — "Go to Copied Link" is rendered inconsistently with the same command elsewhere in the widget strings.
    - Current: `Buka Tautan Tersalin`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `Buka Tautan yang Disalin`
    - String 2GqvPe in the same file translates the identical menu item "Go to Copied Link" as "Buka Tautan yang Disalin"; the confirmation label must quote the same wording.

### E. Typography, punctuation & spacing

- `NativeErrorPage.BadCertDomain.AdvancedInfo.v149` — `id/firefox-ios.xliff` — Missing final period present in the source sentence.
    - Current: `tidak valid untuk %2$@`
    - Source: `%1$@ doesn’t trust this site because the certificate found isn’t valid for %2$@.`
    - Suggest: `tidak valid untuk %2$@.`
    - The en-US string ends with a period; the translation drops the sentence-final punctuation.
- `ScanQRCode.PermissionError.Message.v100` — `id/firefox-ios.xliff` — Closing single quotation marks are rendered as opening quotes (‘Pengaturan‘, ‘Firefox‘).
    - Current: `Buka ‘Pengaturan‘ perangkat > ‘Firefox‘.`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Buka ‘Pengaturan’ perangkat > ‘Firefox’.`
    - The source uses ‘…’ pairs; the target repeats the left quote U+2018 as the closing mark instead of U+2019.
- `Settings.ShowLinkPreviews.StatusV2` — `id/firefox-ios.xliff` — Sentence-case source rendered with title-case capitalization, unlike the source "When long-pressing links".
    - Current: `Ketika Menekan-lama Tautan`
    - Source: `When long-pressing links`
    - Suggest: `Ketika menekan-lama tautan`
    - The v2 string deliberately uses sentence case (contrast with Settings.ShowLinkPreviews.Status which is title case); the translation keeps title case.
- `TopSites.RemovePage.Button` — `id/firefox-ios.xliff` — Em dash in the source replaced with a hyphen.
    - Current: `Hapus halaman - %@`
    - Source: `Remove page — %@`
    - Suggest: `Hapus halaman — %@`
    - The source uses an em dash (—) as separator; the translation uses a plain hyphen.
- `PzSrmZ-2GqvPe` — `id/firefox-ios.xliff` — Closing quotation mark is a left single quote instead of a right single quote.
    - Current: `‘Buka Tautan Tersalin‘`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `‘Buka Tautan Tersalin’`
    - The en-US uses ‘…’ (U+2018/U+2019); the target closes with U+2018 again.
- `PzSrmZ-eHmH1H` — `id/firefox-ios.xliff` — Closing quotation mark is a left single quote instead of a right single quote.
    - Current: `‘Bersihkan Tab Pribadi‘`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `‘Bersihkan Tab Pribadi’`
    - The en-US uses ‘…’ (U+2018/U+2019); the target closes with U+2018 again.
- `PzSrmZ-scEmjs` — `id/firefox-ios.xliff` — Closing quotation mark is a left single quote instead of a right single quote.
    - Current: `‘Pencarian Pribadi Baru‘`
    - Source: `Just to confirm, you wanted ‘New Private Search’?`
    - Suggest: `‘Pencarian Pribadi Baru’`
    - The en-US uses ‘…’ (U+2018/U+2019); the target closes with U+2018 again.
- `PzSrmZ-xRJbBP` — `id/firefox-ios.xliff` — Closing quotation mark is a left single quote instead of a right single quote.
    - Current: `‘Pencarian Baru‘`
    - Source: `Just to confirm, you wanted ‘New Search’?`
    - Suggest: `‘Pencarian Baru’`
    - The en-US uses ‘…’ (U+2018/U+2019); the target closes with U+2018 again.
- `fi3W24-2GqvPe` — `id/firefox-ios.xliff` — Closing quotation mark is a left single quote (‘) instead of the right single quote (’) used in the source.
    - Current: `‘Buka Tautan Tersalin‘`
    - Source: `There are ${count} options matching ‘Go to Copied Link’.`
    - Suggest: `‘Buka Tautan Tersalin’`
    - The en-US source uses ‘...’; the translation closes with an opening quote character.
- `fi3W24-eHmH1H` — `id/firefox-ios.xliff` — Closing quotation mark is a left single quote (‘) instead of the right single quote (’) used in the source.
    - Current: `‘Bersihkan Tab Pribadi‘`
    - Source: `There are ${count} options matching ‘Clear Private Tabs’.`
    - Suggest: `‘Bersihkan Tab Pribadi’`
    - The en-US source uses ‘...’; the translation closes with an opening quote character.
- `fi3W24-scEmjs` — `id/firefox-ios.xliff` — Closing quotation mark is a left single quote (‘) instead of the right single quote (’) used in the source.
    - Current: `‘Pencarian Pribadi Baru‘`
    - Source: `There are ${count} options matching ‘New Private Search’.`
    - Suggest: `‘Pencarian Pribadi Baru’`
    - The en-US source uses ‘...’; the translation closes with an opening quote character.

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

### Resolved to date (0)

_Nothing resolved yet._
