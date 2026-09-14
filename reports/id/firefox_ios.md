# Firefox iOS l10n QA — id

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,906 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for id: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (89)

- `This action will clear all of your private data, including history from your synced devices.` — `id/firefox-ios.xliff` — "your synced devices" rendered without the possessive "Anda", dropping whose devices are meant.
    - Current: `termasuk riwayat dari perangkat yang tersinkronisasi`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `termasuk riwayat dari perangkat Anda yang tersinkronisasi`
    - en-US says "from your synced devices"; the translation omits "your", making it ambiguous about which devices' history is cleared.
- `LibraryPanel.History.Title.v138` — `id/firefox-ios.xliff` — Translation drops "history" qualifier structure and renders "other browsing data" as just "other data".
    - Current: `Menghapus riwayat penjelajahan (termasuk yang tersinkron dari perangkat lain), kuki, dan data lainnya.`
    - Source: `Deletes history (including synced history from other devices), cookies, and other browsing data.`
    - Suggest: `Menghapus riwayat (termasuk riwayat tersinkron dari perangkat lain), kuki, dan data penjelajahan lainnya.`
    - The en-US says "other browsing data"; the Indonesian says only "other data", which is broader than the source, and moves "browsing" onto "riwayat".
- `DefaultBrowserOnboarding.Description2` — `id/firefox-ios.xliff` — "Browser" and "Default" left untranslated here while translated as "Peramban Baku" elsewhere in the same file.
    - Current: `2. Ketuk App Browser Default`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. Ketuk Aplikasi Peramban Baku`
    - Settings.DefaultBrowserMenuItem and DefaultBrowserCard.Title use "Peramban Baku"; this onboarding step uses untranslated "App Browser Default", an inconsistent terminology within the same screen/file.
- `Added page to Reading List` — `id/firefox-ios.xliff` — "Reading List" is rendered "Daftar Baca" here but "Daftar Bacaan" in the neighbouring reading-list strings.
    - Current: `Ditambahkan ke Daftar Baca`
    - Source: `Added page to Reading List`
    - Suggest: `Halaman ditambahkan ke Daftar Bacaan`
    - The same feature name "Reading List" is translated "Daftar Bacaan" in "Add to Reading List" and Address.Bar.ReadingList.v106; also "page" is dropped from the source.
- `Back` — `id/firefox-ios.xliff` — Accessibility label for the Back button translated as "Mundur" (move backwards) instead of the standard "Kembali".
    - Current: `Mundur`
    - Source: `Back`
    - Suggest: `Kembali`
    - The en-US "Back" for the toolbar back button is consistently "Kembali" in Indonesian Firefox; "Mundur" reads as "reverse/retreat".
- `Authentication required` — `id/firefox-ios.xliff` — "Otentikasi" is a non-standard spelling; the correct Indonesian form is "Autentikasi".
    - Current: `Otentikasi dibutuhkan`
    - Source: `Authentication required`
    - Suggest: `Autentikasi dibutuhkan`
    - KBBI/standard Indonesian technical term is "autentikasi".
- `Could not add page to Reading List. Maybe it’s already there?` — `id/firefox-ios.xliff` — The object "page" is dropped, so the Indonesian says "could not add the Reading List" instead of "could not add page to Reading List".
    - Current: `Tidak dapat menambahkan Daftar Baca.`
    - Source: `Could not add page to Reading List. Maybe it’s already there?`
    - Suggest: `Tidak dapat menambahkan laman ke Daftar Baca.`
    - en-US: "Could not add page to Reading List." The translation omits "laman ke", changing the meaning; the sibling string translates it correctly as "Tidak dapat menambahkan laman ke Daftar Baca".
- `ErrorPages.CertWarning.Description` — `id/firefox-ios.xliff` — "To protect your information from being stolen" is rendered as "to protect the theft of your information", reversing the meaning.
    - Current: `Untuk melindungi pencurian informasi Anda`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `Untuk melindungi informasi Anda dari pencurian`
    - The source says Firefox protects your information from being stolen; the Indonesian literally says it protects the theft of your information.
- `ErrorPages.AdvancedWarning2.Text` — `id/firefox-ios.xliff` — Adds "hanya jika" (only if), not present in the source's "Proceed if you accept the potential risk."
    - Current: `Lanjutkan hanya jika Anda siap menanggung risikonya.`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `Lanjutkan jika Anda menerima risiko yang mungkin terjadi.`
    - Source: "Proceed if you accept the potential risk." The added "hanya" (only) changes the condition stated to the user.
- `FirefoxHome.Pocket.Minutes.v99` — `id/firefox-ios.xliff` — Minutes not abbreviated despite the developer comment requiring abbreviation due to space constraints.
    - Current: `%d menit`
    - Source: `%d min`
    - Suggest: `%d mnt`
    - The comment states "Minutes should be abbreviated due to space constraints"; the related string FirefoxHome.Stories.Minutes.v140 uses "mnt".
- `Menu.AddPin.Confirm2` — `id/firefox-ios.xliff` — Confirmation toast translated as an imperative command instead of a completed action.
    - Current: `Tambahkan ke Pintasan`
    - Source: `Added to Shortcuts`
    - Suggest: `Ditambahkan ke Pintasan`
    - Source "Added to Shortcuts" is a toast confirming the item was added; "Tambahkan ke Pintasan" means "Add to Shortcuts" (imperative), identical to the button label Menu.AddToShortcuts.v99.
- `Logins.WelcomeView.TurnOnAutoFill` — `id/firefox-ios.xliff` — "AutoFill" rendered as "Isi-Auto" here but "Isi Otomatis" in the title on the same screen.
    - Current: `Aktifkan Isi-Auto`
    - Source: `Turn on AutoFill`
    - Suggest: `Aktifkan Isi Otomatis`
    - Logins.WelcomeView.Title2 on the same welcome screen uses "Isi Otomatis" for AutoFill; the inconsistent "Isi-Auto" is not the established term.
- `Menu.TrackingProtectionBlockedContent.Title` — `id/firefox-ios.xliff` — "Tracking content" translated as "Pelacakan konten" (tracking of content) instead of "Konten pelacak" (content that tracks).
    - Current: `Pelacakan konten`
    - Source: `Tracking content`
    - Suggest: `Konten pelacak`
    - The source refers to content containing trackers, not to the act of tracking content; the Indonesian reverses the head noun.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `id/firefox-ios.xliff` — "Fingerprinters" rendered as "Sidik jari" (fingerprints) here but as "Pelacak Sidik" in the corresponding title string.
    - Current: `Sidik jari mengumpulkan berbagai pengaturan unik ini`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `Pelacak sidik jari mengumpulkan berbagai pengaturan unik ini`
    - Fingerprinters are the actors collecting settings; "Sidik jari" means fingerprints and is inconsistent with Menu.TrackingProtectionFingerprintersBlocked.Title on the same screen.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `id/firefox-ios.xliff` — Missing verb: "apa yang Anda daring" drops "do" from "what you do online".
    - Current: `melihat apa yang Anda daring`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `melihat apa yang Anda lakukan daring`
    - The source says "what you do online"; the Indonesian omits the verb, leaving an ungrammatical clause.
- `Open Tabs` — `id/firefox-ios.xliff` — "Open Tabs" (noun, sync setting) translated as the imperative "Buka Tab" (open a tab).
    - Current: `Buka Tab`
    - Source: `Open Tabs`
    - Suggest: `Tab Terbuka`
    - The developer comment says this is a toggle for syncing open tabs, so "Open" is an adjective, not a command.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `id/firefox-ios.xliff` — "energy bill" narrowed to "tagihan listrik"... acceptable; but "increase your energy bill" is fine — instead flag none.
    - Current: `tagihan listrik Anda`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `tagihan energi Anda`
    - Source says energy bill; electricity bill is a plausible rendering but narrows the meaning.
- `Search.ThirdPartyEngines.DuplicateErrorMessage` — `id/firefox-ios.xliff` — Error message translated as a success ("has been successfully added") instead of stating the engine was already added.
    - Current: `Mesin pencari dengan judul ini atau URL telah berhasil ditambahkan.`
    - Source: `A search engine with this title or URL has already been added.`
    - Suggest: `Mesin pencari dengan judul atau URL ini sudah pernah ditambahkan.`
    - The source says a search engine with this title or URL "has already been added" — it is an error under the title "Failed". The Indonesian "telah berhasil ditambahkan" means "was successfully added", reversing the message into a success confirmation.
- `ScanQRCode.PermissionError.Message.v100` — `id/firefox-ios.xliff` — Closing single quotes are rendered as opening quotes (‘Pengaturan‘, ‘Firefox‘).
    - Current: `‘Pengaturan‘ perangkat > ‘Firefox‘`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `‘Pengaturan’ perangkat > ‘Firefox’`
    - The source uses ‘…’ with a proper closing quote; the target repeats the opening quote character as the closing one.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `id/firefox-ios.xliff` — "Reading List" rendered as "Daftar Baca" instead of the established "Daftar Bacaan".
    - Current: `Simpan laman ke Daftar Baca`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Simpan laman ke Daftar Bacaan`
    - Other strings in the same file translate "Reading List" as "Daftar Bacaan" (Reading list, Remove from Reading List); this is an inconsistent term for the same feature name.
- `Settings.Siri.SectionDescription` — `id/firefox-ios.xliff` — "quickly open Firefox" is translated as "membuat Firefox" (make/create Firefox) instead of "membuka Firefox" (open Firefox), and "Siri shortcuts" is left untranslated.
    - Current: `Gunakan Siri shortcuts untuk membuat Firefox dengan cepat lewat Siri`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Gunakan pintasan Siri untuk membuka Firefox dengan cepat lewat Siri`
    - Source says "to quickly open Firefox"; "membuat" means "to make/create", which is a different action.
- `Settings.ShowLinkPreviews.StatusV2` — `id/firefox-ios.xliff` — Sentence-case source "When long-pressing links" is rendered in title case, unlike the v2 source which deliberately lowercased it.
    - Current: `Ketika Menekan-lama Tautan`
    - Source: `When long-pressing links`
    - Suggest: `Ketika menekan-lama tautan`
    - The StatusV2 variant exists specifically to change capitalization from title case to sentence case; the translation keeps title case.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `id/firefox-ios.xliff` — "some ad tracking" is rendered as "beberapa pelacak" (some trackers), dropping the "ad tracking" meaning.
    - Current: `Mengizinkan beberapa pelacak agar situs web berfungsi dengan baik.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Mengizinkan beberapa pelacakan iklan agar situs web berfungsi dengan baik.`
    - The source says it allows some ad tracking, not some trackers.
- `ShareExtension.LoadInBackgroundAction.Title` — `id/firefox-ios.xliff` — "Load in Background" translated as "Muat di Belakang" (load at the back/behind) instead of background (latar belakang).
    - Current: `Muat di Belakang`
    - Source: `Load in Background`
    - Suggest: `Muat di Latar Belakang`
    - "Background" in the sense of running behind the foreground app is "latar belakang" in Indonesian; "di Belakang" means physically behind.
- `TabTray.Title` — `id/firefox-ios.xliff` — "Open Tabs" (title listing currently open tabs) is rendered as an imperative "Buka Tab" ("Open a tab").
    - Current: `Buka Tab`
    - Source: `Open Tabs`
    - Suggest: `Tab Terbuka`
    - The source is the tab tray title, a noun phrase meaning tabs that are open; "Buka Tab" reads as the command "open tab".
- `TopSites.RemovePage.Button` — `id/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `Hapus halaman - %@`
    - Source: `Remove page — %@`
    - Suggest: `Hapus halaman — %@`
    - The en-US uses an em dash separator; the localization uses a plain hyphen surrounded by spaces.
- `TranslationToastHandler.PromptTranslate.Title` — `id/firefox-ios.xliff` — "Translate to %2$@" lost the preposition, so the target language reads as the object being translated.
    - Current: `Terjemahkan %2$@ dengan %3$@?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `Terjemahkan ke %2$@ dengan %3$@?`
    - %2$@ is the local language to translate into; without "ke" the sentence says "translate %2$@" instead of "translate to %2$@".
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `id/firefox-ios.xliff` — "Try again" rendered as "Coba beberapa saat lagi", dropping the verb "lagi/ulang" sense of retrying.
    - Current: `Coba beberapa saat lagi.`
    - Source: `There was a problem accessing tabs from your other devices. Try again in a few moments.`
    - Suggest: `Coba lagi beberapa saat lagi.`
    - The source instructs the user to retry shortly; the translation reads only "try in a few moments" without conveying retry.
- `fxa.signin.use-email-instead` — `id/firefox-ios.xliff` — "Use Email Instead" is rendered as "Gunakan Surel Saja" ("Use only email") instead of "as an alternative".
    - Current: `Gunakan Surel Saja`
    - Source: `Use Email Instead`
    - Suggest: `Gunakan Surel Sebagai Gantinya`
    - "Instead" means to use email as an alternative to the QR sign-in; "Saja" means "only/just", changing the meaning.
- `Search Input Field` — `id/firefox-ios.xliff` — "Bidan" (midwife) is a typo for "Bidang" (field).
    - Current: `Bidan Isian Pencarian`
    - Source: `Search Input Field`
    - Suggest: `Bidang Isian Pencarian`
    - The source is "Search Input Field"; "Bidan" means midwife, the intended word is "Bidang" (field).
- `Off` — `id/firefox-ios.xliff` — Accessibility value "Off" is translated as an imperative command "Nonaktifkan" (turn off) instead of the state "Mati".
    - Current: `Nonaktifkan`
    - Source: `Off`
    - Suggest: `Mati`
    - The developer comment says this is a toggled OFF accessibility value, i.e. a state, not an action. "Nonaktifkan" means "deactivate/turn off" as a command.
- `On` — `id/firefox-ios.xliff` — Accessibility value "On" is translated as an imperative command "Aktifkan" (turn on) instead of the state "Nyala".
    - Current: `Aktifkan`
    - Source: `On`
    - Suggest: `Nyala`
    - The developer comment says this is a toggled ON accessibility value, i.e. a state, not an action. "Aktifkan" means "activate/turn on" as a command.
- `Turns private mode on or off` — `id/firefox-ios.xliff` — Accessibility hint describing behaviour is rendered as an imperative instruction instead of a description.
    - Current: `Aktifkan atau nonaktifkan mode pribadi`
    - Source: `Turns private mode on or off`
    - Suggest: `Mengaktifkan atau menonaktifkan mode pribadi`
    - The source "Turns private mode on or off" describes what the control does; the Indonesian imperative tells the user to do it.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `id/firefox-ios.xliff` — "won’t remember any of your history" is rendered as "tidak akan mengingat semua riwayat", which reads as "will not remember all history" (i.e. may remember some).
    - Current: `tidak akan mengingat semua riwayat atau kuki`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `tidak akan mengingat riwayat atau kuki apa pun`
    - In Indonesian "tidak akan ... semua" is ambiguous/partial negation; the source asserts none of the history or cookies is remembered.
- `Settings.AppIconSelection.AppIconNames.Pixelated.Title.v136` — `id/firefox-ios.xliff` — "Pixelated" is rendered as "Berkotak-kotak" (checkered/squared), not the pixel-art meaning.
    - Current: `Berkotak-kotak`
    - Source: `Pixelated`
    - Suggest: `Terpikselasi`
    - The comment says this is a pixelated version of the icon; "Berkotak-kotak" means checkered/box-patterned, which names a different visual.
- `Bookmarks.Menu.EditBookmarkMobileBookmarksLabel.v154` — `id/firefox-ios.xliff` — "BOOKMARKS" is rendered as "BOOKMARK" while the parallel DESKTOP BOOKMARKS header uses "MARKAH", creating inconsistent terminology on the same screen.
    - Current: `BOOKMARK SELULER`
    - Source: `MOBILE BOOKMARKS`
    - Suggest: `MARKAH SELULER`
    - The developer comment says this header is shown alongside the 'DESKTOP BOOKMARKS' header, which is translated "MARKAH DESKTOP"; the same term must be rendered consistently as "markah" throughout the Bookmarks file.
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `id/firefox-ios.xliff` — "Post town" is translated as "Kode kota" (city code), which is wrong; it should name the postal town, not a code.
    - Current: `Kode kota`
    - Source: `Post town`
    - Suggest: `Kota pos`
    - The source "Post town" is the town name used for mail sorting (UK), not a code. "Kode kota" means "city code" and also conflicts with "Kode Pos" (Postal Code) in the same form.
- `MainMenu.Account.AccessibilityLabels.BackButton.v132` — `id/firefox-ios.xliff` — "Back" navigation button rendered as "Mundur" (move backwards/retreat) instead of the standard "Kembali".
    - Current: `Mundur`
    - Source: `Back`
    - Suggest: `Kembali`
    - In iOS navigation UI, the Back button is consistently "Kembali" in Indonesian; "Mundur" means to reverse/retreat and is not the navigation term.
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `id/firefox-ios.xliff` — "save actions" (saving-related actions) mistranslated as "menyimpan tindakan" (saving actions/storing actions).
    - Current: `hingga menyimpan tindakan`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `hingga tindakan penyimpanan`
    - The source lists a range of menu items from private browsing to save actions; the Indonesian reverses the head noun and says "to save actions", which is not what the source means.
- `MainMenu.Account.SigningOut.Title.v154` — `id/firefox-ios.xliff` — "Signing out…" (an in-progress state) is rendered as the imperative/plain "Keluar…" (Sign out/Exit).
    - Current: `Keluar…`
    - Source: `Signing out…`
    - Suggest: `Keluar dari akun…`
    - The source is a transient progress message shown while the user is being signed out; "Keluar…" reads as the action label "Sign out", not the ongoing process ("Sedang keluar…").
- `MainMenu.SiteProtection.Protections.Title.v153` — `id/firefox-ios.xliff` — "Protections" is translated as "Proteksi" here while the other Protections strings on the same screen use "Perlindungan".
    - Current: `Proteksi`
    - Source: `Protections`
    - Suggest: `Perlindungan`
    - MainMenu.SiteProtection.ProtectionsOff/On use "Perlindungan" for the same source term on the same screen; the badge label should match.
- `MainMenu.Submenus.Save.AccessibilityLabels.SaveToReadingList.Subtitle.v132` — `id/firefox-ios.xliff` — "Reading List" is rendered as "Daftar Baca" here but "Daftar Bacaan" in the parallel v131 strings on the same menu.
    - Current: `Daftar Baca`
    - Source: `Reading List`
    - Suggest: `Daftar Bacaan`
    - Same source term "Reading List" on the same submenu is translated inconsistently (v131 Subtitle uses "Daftar Bacaan", and the RemoveFromReadingList accessibility label also uses "Daftar Bacaan").
- `MainMenu.Submenus.Save.AccessibilityLabels.SaveToReadingList.Title.v132` — `id/firefox-ios.xliff` — "Reading List" rendered "Daftar Baca" inconsistently with "Daftar Bacaan" used elsewhere in the same menu.
    - Current: `Simpan ke Daftar Baca`
    - Source: `Save to Reading List`
    - Suggest: `Simpan ke Daftar Bacaan`
    - The v131 counterpart of this same menu item uses "Daftar Bacaan"; inconsistent term for the same source string on the same screen.
- `MainMenu.Submenus.Save.RemoveFromReadingList.Title.v131` — `id/firefox-ios.xliff` — "Reading List" rendered "Daftar Baca" while the accessibility label for the same item uses "Daftar Bacaan".
    - Current: `Hapus dari Daftar Baca`
    - Source: `Remove from Reading List`
    - Suggest: `Hapus dari Daftar Bacaan`
    - Inconsistent rendering of "Reading List" within the same submenu; the v132 accessibility label for this item uses "Daftar Bacaan".
- `MainMenu.Submenus.Tools.AccessibilityLabels.Zoom.Title.v132` — `id/firefox-ios.xliff` — The zoom-level label uses the verb "Perbesar" instead of the noun "Perbesaran" used for the same Zoom term in the sibling subtitle.
    - Current: `Perbesar (%@)`
    - Source: `Zoom (%@)`
    - Suggest: `Perbesaran (%@)`
    - The comment says this label indicates the current zoom level (a noun); the sibling Zoom.Subtitle uses "Perbesaran", so "Perbesar" is both inconsistent and grammatically a verb.
- `MainMenu.Submenus.Tools.AccessibilityLabels.ReaderView.Off.Title.v132` — `id/firefox-ios.xliff` — "Turn off" is translated "Matikan" here while the parallel Night Mode off string uses "Nonaktifkan".
    - Current: `Matikan Tampilan Pembaca`
    - Source: `Turn off Reader View`
    - Suggest: `Nonaktifkan Tampilan Pembaca`
    - Inconsistent rendering of "Turn off" within the same Tools submenu (Night Mode Off uses "Nonaktifkan", and the corresponding "Turn on" strings both use "Aktifkan").
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `id/firefox-ios.xliff` — "Reader View" is rendered inconsistently as "Tampilan Pembaca" here but "Tampilan Baca" in the accessibility label on the same screen.
    - Current: `Matikan Tampilan Pembaca`
    - Source: `Turn off Reader View`
    - Suggest: `Matikan Tampilan Baca`
    - The same source term "Reader View" must be consistent within the MainMenu group; MainMenu.ToolsSection.AccessibilityLabels.ReaderView.v150 uses "Tampilan Baca".
- `MainMenu.Submenus.Tools.Zoom.Title.v131` — `id/firefox-ios.xliff` — The noun "Zoom (%@)" labeling the current zoom level is translated as the verb "Perbesar" (enlarge).
    - Current: `Perbesar (%@)`
    - Source: `Zoom (%@)`
    - Suggest: `Perbesaran (%@)`
    - The comment says this is the menu component that indicates the current zoom level, a noun; the related subtitle string uses the noun "Perbesaran".
- `MainMenu.ToolsSection.AccessibilityLabels.PageZoom.Title.v142` — `id/firefox-ios.xliff` — "Page Zoom" is translated as "Pembesaran Laman" here but "Zum Laman" in the menu title for the same feature.
    - Current: `Pembesaran Laman`
    - Source: `Page Zoom`
    - Suggest: `Zum Laman`
    - MainMenu.Submenus.Tools.PageZoomV2.Title.v141 renders the same source term "Page Zoom" as "Zum Laman"; the accessibility label should match the visible control.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `id/firefox-ios.xliff` — "submenu" is written as two words "sub menu" instead of the correct Indonesian "submenu".
    - Current: `Simpan sub menu`
    - Source: `Save submenu`
    - Suggest: `Submenu Simpan`
    - In Indonesian the prefix "sub-" is written closed ("submenu"), and the head noun should precede the modifier.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `id/firefox-ios.xliff` — "submenu" is written as two words "sub menu" instead of the correct Indonesian "submenu".
    - Current: `Sub menu alat`
    - Source: `Tools submenu`
    - Suggest: `Submenu alat`
    - In Indonesian the prefix "sub-" is written closed, giving "submenu".
- `NativeErrorPage.BadCertDomain.AdvancedInfo.v149` — `id/firefox-ios.xliff` — Missing final period present in the source sentence.
    - Current: `%1$@ tidak memercayai situs ini karena sertifikat yang ditemukan tidak valid untuk %2$@`
    - Source: `%1$@ doesn’t trust this site because the certificate found isn’t valid for %2$@.`
    - Suggest: `%1$@ tidak memercayai situs ini karena sertifikat yang ditemukan tidak valid untuk %2$@.`
    - The en-US string ends with a period; the translation drops the sentence-final punctuation.
- `NativeErrorPage.BadCertDomain.ProceedButton.v149` — `id/firefox-ios.xliff` — Misspelling of "Berisiko".
    - Current: `Berrisiko`
    - Source: `Proceed to %@ (Risky)`
    - Suggest: `Berisiko`
    - Indonesian spelling is "berisiko" (one r), not "berrisiko".
- `NativeErrorPage.Wayback.Error.LinkText.v155` — `id/firefox-ios.xliff` — "Wayback Machine" product name translated, and inconsistent with other strings in the same file that keep it in English.
    - Current: `Mesin Wayback`
    - Source: `Wayback Machine`
    - Suggest: `Wayback Machine`
    - Wayback Machine is a product name from the Internet Archive and is kept untranslated in the other strings of this file (e.g. Wayback.Error.Description, WaybackButtonA11yHint).
- `NativeErrorPage.Wayback.Error.FooterDescription.v155` — `id/firefox-ios.xliff` — "Internet Archive" translated as "Arsip Internet" while the rest of the file and the link placeholder treat these as product names.
    - Current: `dari Arsip Internet %2$@`
    - Source: `%1$@ can look for an earlier version of this page from the Internet Archive’s %2$@.`
    - Suggest: `dari %2$@ milik Internet Archive`
    - Internet Archive is an organization/brand name; source is "the Internet Archive’s %2$@" and the possessive relation is also lost in the current rendering.
- `Onboarding.Customization.Toolbar.Bottom.Action.v123` — `id/firefox-ios.xliff` — "Bottom" (toolbar placement at the bottom of the screen) is translated as "Dasar", which means "basic/base", not the bottom position.
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The developer comment says this option sets the toolbar at the bottom of the screen; Indonesian for that position is "Bawah". "Dasar" reads as "basic" and is also the word used for "Default" elsewhere.
- `Onboarding.Customization.Toolbar.Top.Action.v123` — `id/firefox-ios.xliff` — "Top" (toolbar placement at the top of the screen) is translated as "Puncak" (summit/peak) instead of "Atas".
    - Current: `Puncak`
    - Source: `Top`
    - Suggest: `Atas`
    - The developer comment says this option sets the toolbar at the top of the screen; the positional term in Indonesian is "Atas". "Puncak" means a summit/peak and is wrong for a UI position.
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Description.v148` — `id/firefox-ios.xliff` — "have %@ match your device" is rendered as an instruction for the user to match Firefox to the device, reversing the agent.
    - Current: `atau cocokkan %@ dengan perangkat Anda`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `atau biarkan %@ menyesuaikan dengan perangkat Anda`
    - The source says to let the app follow the device theme automatically, not to have the user perform the matching.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `id/firefox-ios.xliff` — "won't sell you out" (won't betray you) is rendered literally as "tidak akan menjual Anda" (won't sell you), changing the meaning.
    - Current: `tidak akan menjual Anda`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `tidak akan mengkhianati Anda`
    - The English idiom "sell you out" means to betray; the Indonesian literally says the browser will not sell you (as a person), which is not what the source says.
- `Onboarding.Modern.Customization.Toolbar.Bottom.Action.v140` — `id/firefox-ios.xliff` — "Bottom" as a screen position is translated as "Dasar" (basic/base), the wrong sense in Indonesian UI.
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The option sets the toolbar at the bottom of the screen; Indonesian uses "Bawah" for this. "Dasar" is also the established translation for "Default"/"basic", causing confusion.
- _…and 29 more._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (83)

- `Bookmarks.Menu.EditBookmarkMobileBookmarksLabel.v154` — `Shared/Supporting Files/en.lproj/Bookmarks.strings` — "Bookmarks" is rendered as "BOOKMARK" here while the parallel header and the rest of the file use "Markah".
    - Current: `BOOKMARK SELULER`
    - Suggest: `MARKAH SELULER`
    - The sibling header Bookmarks.Menu.EditBookmarkDesktopBookmarksLabel.v136 uses "MARKAH DESKTOP", and all other strings in this file translate "bookmark(s)" as "markah"; using "BOOKMARK" on the same screen is inconsistent.
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Post town" is translated as "Kode kota" (city code), not the town used for mail sorting.
    - Current: `Kode kota`
    - Suggest: `Kota pos`
    - Source "Post town" is a town name used for mail sorting in the UK; "Kode kota" means "city code", a different concept and easily confused with the postal code field.
- `Addresses.EditAddress.AutofillAddressTownland.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Townland" rendered as "Kota kecil" (small town), which is a different concept.
    - Current: `Kota kecil`
    - Suggest: `Townland`
    - The developer comment states a townland is a rural land division, not a small town; "Kota kecil" means small town.
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "save actions" (actions for saving) is mistranslated as "menyimpan tindakan" (saving actions).
    - Current: `hingga menyimpan tindakan`
    - Suggest: `hingga tindakan penyimpanan`
    - The source lists menu capabilities ranging from private browsing to save actions; the Indonesian reverses the noun phrase into "saving actions", which says something different.
- `MainMenu.Account.AccessibilityLabels.BackButton.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — The navigation "Back" button is rendered as "Mundur" instead of the standard "Kembali".
    - Current: `Mundur`
    - Suggest: `Kembali`
    - In Firefox UI the back navigation control is consistently "Kembali" in Indonesian; "Mundur" (move backwards/reverse) is not the established term for this accessibility label.
- `MainMenu.Account.SigningOut.Title.v154` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Signing out…" is translated as "Keluar…", which reads as the action "Sign out" rather than the in-progress state.
    - Current: `Keluar…`
    - Suggest: `Sedang keluar…`
    - The developer comment says this is shown transiently while the user is being signed out, so the progressive state must be conveyed.
- `MainMenu.SiteProtection.Protections.Title.v153` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Protections" is translated as "Proteksi" while the adjacent protection-state strings on the same menu use "Perlindungan".
    - Current: `Proteksi`
    - Suggest: `Perlindungan`
    - MainMenu.SiteProtection.ProtectionsOn/Off use "Perlindungan" for the same source term on the same top-of-menu area; the term should be consistent.
- `MainMenu.Submenus.Save.AccessibilityLabels.SaveToReadingList.Subtitle.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Reading List" rendered as "Daftar Baca" while the visible label counterpart uses "Daftar Bacaan".
    - Current: `Daftar Baca`
    - Suggest: `Daftar Bacaan`
    - The corresponding visible string MainMenu.Submenus.Save.SaveToReadingList.Subtitle.v131 uses "Daftar Bacaan"; the accessibility label should match the visible term.
- `MainMenu.Submenus.Save.AccessibilityLabels.SaveToReadingList.Title.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Reading List" rendered as "Daftar Baca" while the visible label counterpart uses "Daftar Bacaan".
    - Current: `Simpan ke Daftar Baca`
    - Suggest: `Simpan ke Daftar Bacaan`
    - The corresponding visible string MainMenu.Submenus.Save.SaveToReadingList.Title.v131 uses "Daftar Bacaan"; inconsistent term for the same feature on the same screen.
- `MainMenu.Submenus.Save.RemoveFromReadingList.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Reading List" is rendered as "Daftar Baca" here but as "Daftar Bacaan" in the sibling Save submenu strings on the same screen.
    - Current: `Hapus dari Daftar Baca`
    - Suggest: `Hapus dari Daftar Bacaan`
    - Within the same Save submenu group, MainMenu.Submenus.Save.SaveToReadingList.Title/Subtitle use "Daftar Bacaan"; the same source term must be consistent on the same screen.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Turn off" is rendered as "Matikan" while the parallel Night Mode off string uses "Nonaktifkan", creating inconsistency within the same submenu.
    - Current: `Matikan Tampilan Pembaca`
    - Suggest: `Nonaktifkan Tampilan Pembaca`
    - MainMenu.Submenus.Tools.NightMode.Off.Title.v131 translates "Turn off" as "Nonaktifkan"; the same term should be used consistently in the same Tools submenu.
- `MainMenu.Submenus.Tools.Zoom.Title.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — The noun "Zoom" is rendered as the verb "Perbesar" while the parallel subtitle uses the noun "Perbesaran".
    - Current: `Perbesar (%@)`
    - Suggest: `Perbesaran (%@)`
    - The string labels the current zoom level (a noun), and MainMenu.Submenus.Tools.Zoom.Subtitle.v131 translates "Zoom" as "Perbesaran".
- `MainMenu.ToolsSection.AccessibilityLabels.PageZoom.Title.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Page Zoom" is translated as "Pembesaran Laman" here but "Zum Laman" in the other Page Zoom string.
    - Current: `Pembesaran Laman`
    - Suggest: `Zum Laman`
    - MainMenu.Submenus.Tools.PageZoomV2.Title.v141 renders the same source term "Page Zoom" as "Zum Laman"; the two labels refer to the same feature and must match.
- `MainMenu.ToolsSection.AccessibilityLabels.ReaderView.v150` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Reader View" is translated as "Tampilan Baca" here but "Tampilan Pembaca" elsewhere in the same file.
    - Current: `Tampilan Baca`
    - Suggest: `Tampilan Pembaca`
    - MainMenu.Submenus.Tools.ReaderView.Subtitle.v131 and the On/Off titles use "Tampilan Pembaca" for the same source term "Reader View".
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Save submenu" is rendered with wrong word order and a misspelled compound, saying "Save the submenu" instead of naming the Save submenu.
    - Current: `Simpan sub menu`
    - Suggest: `Submenu Simpan`
    - In Indonesian the head noun comes first, so "Simpan sub menu" reads as the imperative "save the submenu"; the parallel string Tools submenu is correctly "Sub menu alat". Also "submenu" is written as one word.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "submenu" is spelled as two words.
    - Current: `Sub menu alat`
    - Suggest: `Submenu Alat`
    - Indonesian standard spelling joins the prefix: "submenu", not "sub menu".
- `NativeErrorPage.BadCertDomain.AdvancedInfo.v149` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — Missing final period present in the source sentence.
    - Current: `tidak valid untuk %2$@`
    - Suggest: `tidak valid untuk %2$@.`
    - The en-US string ends with a period; the translation drops the sentence-final punctuation.
- `NativeErrorPage.BadCertDomain.ProceedButton.v149` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — Misspelling of "Berisiko".
    - Current: `Berrisiko`
    - Suggest: `Berisiko`
    - The correct Indonesian spelling is "berisiko" (one r), not "berrisiko".
- `NativeErrorPage.Wayback.Error.LinkText.v155` — `Shared/Supporting Files/en.lproj/NativeErrorPage.strings` — Product name "Wayback Machine" was translated instead of kept as-is.
    - Current: `Mesin Wayback`
    - Suggest: `Wayback Machine`
    - "Wayback Machine" is the Internet Archive's product name and is left untranslated elsewhere in this same file (Wayback.Error.Description, WaybackButtonA11yHint), creating an inconsistency.
- `Onboarding.Customization.Toolbar.Bottom.Action.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Bottom" as a toolbar position is rendered "Dasar" (base/basic) instead of "Bawah".
    - Current: `Dasar`
    - Suggest: `Bawah`
    - The source refers to placing the toolbar at the bottom of the screen; Indonesian for that position is "Bawah". "Dasar" means base/foundation/basic and is misleading here.
- `Onboarding.Customization.Toolbar.Top.Action.v123` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Top" as a toolbar position is rendered "Puncak" (summit/peak) instead of "Atas".
    - Current: `Puncak`
    - Suggest: `Atas`
    - The source refers to placing the toolbar at the top of the screen; the standard Indonesian term for that position is "Atas". "Puncak" means summit/peak and is wrong in a UI position control.
- `Onboarding.Modern.BrandRefresh.Notification.Skip.Action.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Not Now" is rendered as "Jangan Sekarang" ("Don't now"), which is not the Indonesian equivalent of "Not now".
    - Current: `Jangan Sekarang`
    - Suggest: `Nanti Saja`
    - "Not Now" means postponing; the standard Indonesian rendering is "Nanti Saja" or "Tidak Sekarang". "Jangan Sekarang" is an imperative prohibition and is not idiomatic.
- `Onboarding.Modern.BrandRefresh.Sync.Skip.Action.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Not Now" is rendered as "Jangan Sekarang" ("Don't now"), which is not the Indonesian equivalent of "Not now".
    - Current: `Jangan Sekarang`
    - Suggest: `Nanti Saja`
    - "Not Now" means postponing; the standard Indonesian rendering is "Nanti Saja" or "Tidak Sekarang". "Jangan Sekarang" is an imperative prohibition and is not idiomatic.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "won't sell you out" (betray you) is mistranslated as "tidak akan menjual Anda" (will not sell you).
    - Current: `tidak akan menjual Anda`
    - Suggest: `tidak akan mengkhianati Anda`
    - "Sell you out" is an idiom meaning betray/give away your data, not literally selling the person.
- `Onboarding.Modern.BrandRefresh.Welcome.Skip.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Not Now" is rendered as "Jangan Sekarang" ("Don't now"), which is not the Indonesian equivalent of "Not now".
    - Current: `Jangan Sekarang`
    - Suggest: `Nanti Saja`
    - "Not Now" means postponing; the standard Indonesian rendering is "Nanti Saja" or "Tidak Sekarang". "Jangan Sekarang" is an imperative prohibition and is not idiomatic.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — The sentence reverses the matching relation: the source has %@ (the app) match the device, the target tells the user to match %@ to the device but with an imperative addressed to the user.
    - Current: `atau cocokkan %@ dengan perangkat Anda`
    - Suggest: `atau biarkan %@ menyesuaikan dengan perangkat Anda`
    - The source "have %@ match your device" means letting the app follow the device setting automatically; the translation makes it a manual user action.
- `Onboarding.Modern.Customization.Toolbar.Bottom.Action.v140` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Bottom" as a toolbar position is translated as "Dasar" (base/basic) instead of the positional term "Bawah".
    - Current: `Dasar`
    - Suggest: `Bawah`
    - The developer comment says this sets the toolbar at the bottom of the screen; Indonesian uses "Bawah" for that position, and "Dasar" also commonly means "basic", which is misleading.
- `Onboarding.Modern.Customization.Toolbar.Bottom.Action.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Bottom" as a toolbar position is translated as "Dasar" (base/basic) instead of the positional term "Bawah".
    - Current: `Dasar`
    - Suggest: `Bawah`
    - The developer comment says this sets the toolbar to the bottom of the screen; Indonesian uses "Bawah" for that position.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v140` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Top" as a toolbar position is translated as "Puncak" (summit/peak) instead of the positional term "Atas".
    - Current: `Puncak`
    - Suggest: `Atas`
    - The developer comment says this sets the toolbar at the top of the screen; Indonesian uses "Atas" for that position, while "Puncak" means a summit.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Top" as a toolbar position is translated as "Puncak" (summit/peak) instead of the positional term "Atas".
    - Current: `Puncak`
    - Suggest: `Atas`
    - The developer comment says this sets the toolbar to the top of the screen; Indonesian uses "Atas" for that position.
- `Onboarding.Modern.Sync.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Possessive "Anda" is misplaced, attaching only to "sandi" instead of the whole list.
    - Current: `Markah, sandi Anda, dan lainnya disinkronkan`
    - Suggest: `Markah, sandi, dan lainnya milik Anda disinkronkan`
    - Source is "Your bookmarks, passwords, and more" — the possessive covers the whole list, not just passwords.
- `Onboarding.Modern.TermsOfService.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Word order makes "nirlaba" modify the company name placeholder awkwardly/incorrectly.
    - Current: `Dipersembahkan oleh %@ nirlaba`
    - Suggest: `Dipersembahkan oleh %@, organisasi nirlaba`
    - Source is "Brought to you by the non-profit %@"; in Indonesian "%@ nirlaba" reads as if the company name is a common noun being modified, which is ungrammatical for a proper name.
- `Onboarding.Welcome.Close.AccessibilityLabel.v121` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "onboarding" is rendered as "proses bergabung" (joining process), which misstates the app's onboarding/introduction flow.
    - Current: `Tutup dan keluar dari proses bergabung %@`
    - Suggest: `Tutup dan keluar dari pengenalan %@`
    - The en-US refers to the onboarding (introductory) screens, not a process of joining/membership.
- `PrivacyDashboard.Fingerprinters.v155` — `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings` — "Fingerprinters" is translated literally as "Penyidik jari" (finger investigator), not the established privacy term.
    - Current: `Penyidik jari`
    - Suggest: `Pengambil Sidik Jari Digital`
    - In Firefox privacy UI, "fingerprinters" are scripts that fingerprint the browser; "penyidik jari" is a literal, incorrect rendering and is also inconsistent with the title-case style of the sibling labels.
- `PrivacyDashboard.TrackingContent.v155` — `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings` — "Tracking Content" is rendered with reversed head noun, meaning "Content Tracking" instead of content that tracks.
    - Current: `Pelacakan Konten`
    - Suggest: `Konten Pelacak`
    - Source refers to content that tracks (tracking content); the Indonesian reverses the head noun to say "tracking of content", parallel to the other entries like "Pelacak Media Sosial".
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `Shared/Supporting Files/en.lproj/RelayMask.strings` — "email mask" is rendered "topeng surel" here while other strings in the same file use "masker surel".
    - Current: `topeng surel gratis`
    - Suggest: `masker surel gratis`
    - The same feature term must be consistent within the RelayMask screen; the file otherwise uses "masker surel" (e.g. Masker Surel, Gunakan masker surel).
- `RelayMask.RelayEmailMaskInsertedA11yAnnouncement.v147` — `Shared/Supporting Files/en.lproj/RelayMask.strings` — "Email mask" rendered as "Topeng surel", inconsistent with "masker surel" used elsewhere in the same file.
    - Current: `Topeng surel dimasukkan`
    - Suggest: `Masker surel dimasukkan`
    - Terminology inconsistency within the RelayMask feature strings, which elsewhere use "masker surel".
- `RelayMask.RelayEmailMaskSettingsDetailInfo.v147` — `Shared/Supporting Files/en.lproj/RelayMask.strings` — "email masks" rendered as "topeng surel", inconsistent with "masker surel" used elsewhere in the same file.
    - Current: `tidak mendukung topeng surel`
    - Suggest: `tidak mendukung masker surel`
    - Terminology inconsistency within the same feature/screen; the settings title is "Masker Surel".
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `Shared/Supporting Files/en.lproj/ScanQRCode.strings` — The prompt reverses the meaning: it asks whether to open the app rather than allow the app to open the URL.
    - Current: `Izinkan %@ untuk dibuka?`
    - Suggest: `Izinkan %@ untuk membuka?`
    - Source "Allow %@ to open?" asks permission for the app (%@) to open the scanned URL; "untuk dibuka" (passive) means allowing the app itself to be opened.
- `Settings.AIControls.HeaderCard.Message.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — Awkward/ungrammatical rendering of "whether to use" using "jikalau akan".
    - Current: `Itu termasuk jikalau akan menggunakan fitur yang ditingkatkan dengan AI.`
    - Suggest: `Itu termasuk apakah akan menggunakan fitur yang ditingkatkan dengan AI.`
    - "whether" in this context is "apakah"; "jikalau" means "if/in case" and produces an ungrammatical sentence.
- `Settings.Browsing.AdBlocker.LearnMore.v155` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Learn more" is translated inconsistently within the same file ("Pelajari selengkapnya" vs "Pelajari lebih lanjut").
    - Current: `Pelajari lebih lanjut`
    - Suggest: `Pelajari selengkapnya`
    - Settings.AIControls.HeaderCard.Link.v151 in the same file renders the identical source "Learn more" as "Pelajari selengkapnya"; Firefox id standard is "Pelajari selengkapnya".
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `Shared/Supporting Files/en.lproj/Settings.strings` — The word "perangkat" (device) is misplaced at the end, making the navigation path read as "Settings > Notifications > %2$@ device" instead of "device Settings > Notifications > %2$@".
    - Current: `Aktifkan dengan membuka Setelan > Notifikasi > %2$@ perangkat`
    - Suggest: `Aktifkan dengan membuka Setelan perangkat > Notifikasi > %2$@`
    - In en-US "device" modifies "Settings" (the first item of the path); placing "perangkat" after the app-name placeholder corrupts the settings path instruction.
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Notifications" is rendered as "pemberitahuan" and "Notifikasi" within the same string and screen.
    - Current: `Anda menonaktifkan semua pemberitahuan %1$@. Aktifkan dengan membuka Setelan > Notifikasi > %2$@ perangkat`
    - Suggest: `Anda menonaktifkan semua notifikasi %1$@. Aktifkan dengan membuka Setelan perangkat > Notifikasi > %2$@`
    - Other strings in the Notifications settings section consistently use "Notifikasi"; using two different terms in one string is inconsistent.
- `Settings.Search.Suggest.ShowSponsoredSuggestions.Description.v124` — `Shared/Supporting Files/en.lproj/Settings.strings` — "occasional" is mistranslated as "sesaat" (momentary/brief) instead of "sesekali/kadang-kadang".
    - Current: `saran bersponsor sesaat`
    - Suggest: `saran bersponsor sesekali`
    - en-US "occasional sponsored suggestions" means suggestions shown from time to time; "sesaat" means brief/momentary, which changes the meaning.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v137` — `Shared/Supporting Files/en.lproj/SocialShare.strings` — The blank-line separation between the shared URL and the rest of the message is missing.
    - Current: `%1$@Dikirim dari %2$@ 🦊 Coba peramban seluler: %3$@`
    - Suggest: `%1$@  Dikirim dari %2$@ 🦊 Coba peramban seluler: %3$@`
    - The source and the developer comment specify empty lines separating the first link parameter from the rest of the text; here the URL runs directly into the following word, breaking the shared message formatting (the parallel string ShareMessageB.Title.v137 keeps the line breaks).
- `Summarizer.Error.MissingPageContent.Message.v142` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — "hit summarize" is rendered as a verb phrase instead of referring to the Summarize control.
    - Current: `lalu tekan meringkas`
    - Suggest: `lalu tekan Ringkas`
    - The source instructs the user to press the "summarize" button; "tekan meringkas" reads as "press summarizing" and does not name the control.
- `Summarizer.HostedBrand.Label.v142` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — "Summarized by" is translated as "Diringkas oleh" here but as "Dirangkum oleh" in the parallel Apple Intelligence label on the same screen.
    - Current: `Diringkas oleh %@`
    - Suggest: `Dirangkum oleh %@`
    - Summarizer.AppleBrand.Label.v142 uses "Dirangkum oleh Apple Intelligence" for the identical source phrase "Summarized by"; the two labels appear in the same summary report and must match.
- `TermsOfUse.TitleValue1.v147` — `Shared/Supporting Files/en.lproj/TermsOfUse.strings` — "Terms of Use" is rendered as "Syarat Penggunaan" here but as "Ketentuan Penggunaan" in all other strings of the same screen.
    - Current: `Syarat Penggunaan`
    - Suggest: `Ketentuan Penggunaan`
    - TermsOfUse.Link.TermsOfUse.v142, TermsOfUse.Description.v142 and TermsOfUse.TermsOfUseHasOpened.v142 all use "Ketentuan Penggunaan" for the same source term on the same sheet; this variant title is inconsistent.
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `Shared/Supporting Files/en.lproj/WebCompatReporter.strings` — Missing relative pronoun makes the phrase read as a clause instead of "trackers blocked on this page".
    - Current: `Nama host pelacak diblokir di laman ini`
    - Suggest: `Nama host pelacak yang diblokir di laman ini`
    - The source is a noun phrase "Hostnames of trackers blocked on this page"; without "yang" the Indonesian reads as a sentence "Tracker hostnames are blocked on this page".
- `WorldCup.HomepageWidget.FTLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "Full Time" (end of match) rendered as "Penuh Waktu" (full-time as in employment/word order reversed).
    - Current: `(Penuh Waktu)`
    - Suggest: `(Waktu Penuh)`
    - The label indicates the match has ended; Indonesian "Penuh Waktu" is a calque with reversed head-modifier order and does not convey end of match.
- `WorldCup.HomepageWidget.FTNoParenthesisLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "Full Time" (end of match) rendered as "Penuh Waktu", wrong word order/meaning in Indonesian.
    - Current: `Penuh Waktu`
    - Suggest: `Waktu Penuh`
    - The label indicates the match has ended; "Penuh Waktu" reverses Indonesian head-modifier order and reads as "full-time" in the employment sense.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "Match" (a football game) is mistranslated as "kecocokan" (a match/fit), inconsistent with "pertandingan" used elsewhere.
    - Current: `Info kecocokan tidak tersedia saat ini.`
    - Suggest: `Info pertandingan tidak tersedia saat ini.`
    - The source refers to World Cup match data; other strings in the same file translate "match" as "pertandingan". "Kecocokan" means compatibility/similarity.
- `WorldCup.HomepageWidget.RoundPhase.ThirdPlaceLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "THIRD PLACE" (ranking) translated literally as "TEMPAT KETIGA" (third location).
    - Current: `TEMPAT KETIGA`
    - Suggest: `PERINGKAT KETIGA`
    - In a tournament context the source means third-place finisher; "tempat" means a physical place in Indonesian, not a ranking position.
- `This action will clear all of your private data, including history from your synced devices.` — `Shared/en.lproj/ClearHistoryConfirm.strings` — The translation drops "your" from "your synced devices", omitting the reference to the user's own devices.
    - Current: `termasuk riwayat dari perangkat yang tersinkronisasi`
    - Suggest: `termasuk riwayat dari perangkat Anda yang tersinkronisasi`
    - Source says "history from your synced devices"; the possessive is dropped, making it ambiguous which devices are meant.
- `DefaultBrowserOnboarding.Description2` — `Shared/en.lproj/Default Browser.strings` — iOS Settings item is rendered with untranslated English terms "App Browser Default" instead of the Indonesian iOS wording, and the word order is wrong.
    - Current: `2. Ketuk App Browser Default`
    - Suggest: `2. Ketuk Aplikasi Peramban Baku`
    - The rest of this file consistently translates "default browser" as "peramban baku"; "App Browser Default" is neither English nor correct Indonesian word order.
- `DefaultBrowserOnboarding.Screenshot` — `Shared/en.lproj/Default Browser.strings` — "Default Browser App" is rendered with wrong word order/meaning as "App Browser Default".
    - Current: `App Browser Default`
    - Suggest: `Aplikasi Peramban Baku`
    - The source refers to the iOS setting "Default Browser App"; the Indonesian word order makes "Default" modify "Browser App" incorrectly and mixes untranslated English. Also inconsistent with "Peramban Baku" used in Settings.DefaultBrowserMenuItem.
- `LibraryPanel.History.Title.v138` — `Shared/en.lproj/HistoryPanel.strings` — "other browsing data" is translated as just "data lainnya", dropping "browsing".
    - Current: `kuki, dan data lainnya`
    - Suggest: `kuki, dan data penjelajahan lainnya`
    - The source says "cookies, and other browsing data"; the translation drops the qualifier "browsing".
- `Added page to Reading List` — `Shared/en.lproj/Localizable.strings` — The translation omits "page" and uses "Daftar Baca" instead of the consistent "Daftar Bacaan".
    - Current: `Ditambahkan ke Daftar Baca`
    - Suggest: `Halaman ditambahkan ke Daftar Bacaan`
    - Source is "Added page to Reading List"; "page" is dropped, and "Reading List" is elsewhere translated "Daftar Bacaan" (see 'Add to Reading List').
- `Could not add page to Reading List. Maybe it’s already there?` — `Shared/en.lproj/Localizable.strings` — The object "page" is dropped, so the Indonesian reads "Could not add Reading List" instead of "Could not add page to Reading List".
    - Current: `Tidak dapat menambahkan Daftar Baca.`
    - Suggest: `Tidak dapat menambahkan laman ke Daftar Baca.`
    - Source says the page could not be added to the Reading List; the translation omits "laman ke", changing the meaning.
- `Display Settings` — `Shared/en.lproj/Localizable.strings` — "Settings" is rendered as "Setelan" here while all other strings in this file use "Pengaturan".
    - Current: `Setelan Tampilan`
    - Suggest: `Pengaturan Tampilan`
    - Inconsistent terminology: CoverSheet.v24.ETP.Settings.Button, ContextualHints.SearchBarPlacement.CallToAction and others use "Pengaturan" for Settings.
- _…and 23 more._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 96 |
| Strings | 1,922 |
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
| quotes | `curly-double` 4, `curly-single` 1 | **curly-double** |
| apostrophe | `typographic` 1 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 2, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (97)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `id/firefox-ios.xliff` — "won't sell you out" (won't betray you) is rendered literally as "tidak akan menjual Anda" (won't sell you), changing the meaning.
    - Current: `tidak akan menjual Anda`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `tidak akan mengkhianati Anda`
    - The English idiom "sell you out" means to betray; the Indonesian literally says the browser will not sell you (as a person), which is not what the source says.
- `Search.ThirdPartyEngines.DuplicateErrorMessage` — `id/firefox-ios.xliff` — Error message translated as a success ("has been successfully added") instead of stating the engine was already added.
    - Current: `Mesin pencari dengan judul ini atau URL telah berhasil ditambahkan.`
    - Source: `A search engine with this title or URL has already been added.`
    - Suggest: `Mesin pencari dengan judul atau URL ini sudah pernah ditambahkan.`
    - The source says a search engine with this title or URL "has already been added" — it is an error under the title "Failed". The Indonesian "telah berhasil ditambahkan" means "was successfully added", reversing the message into a success confirmation.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `id/firefox-ios.xliff` — "won’t remember any of your history" is rendered as "tidak akan mengingat semua riwayat", which reads as "will not remember all history" (i.e. may remember some).
    - Current: `tidak akan mengingat semua riwayat atau kuki`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `tidak akan mengingat riwayat atau kuki apa pun`
    - In Indonesian "tidak akan ... semua" is ambiguous/partial negation; the source asserts none of the history or cookies is remembered.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 37 |
| 3 | Degraded language (grammar, spelling, terminology) | 48 |
| 4 | Cosmetic (typography, spacing) | 12 |

### A. Functional, markup, variables & plurals

- `SentFromFirefox.SocialShare.ShareMessageA.Title.v137` — `id/firefox-ios.xliff` — The two empty lines separating the shared URL from the rest of the message are missing, so the URL runs directly into the text.
    - Current: `%1$@Dikirim dari %2$@`
    - Source: `%1$@  Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%1$@  Dikirim dari %2$@`
    - The developer comment states the newline symbols denote empty lines separating the first link parameter from the rest of the text; the target concatenates them with no separation, unlike the parallel v137 ShareMessageB string.

### B. Mistranslation, reversed meaning, wrong names & brand

- `Settings.AppIconSelection.AppIconNames.Pixelated.Title.v136` — `id/firefox-ios.xliff` — "Pixelated" is rendered as "Berkotak-kotak" (checkered/squared), not the pixel-art meaning.
    - Current: `Berkotak-kotak`
    - Source: `Pixelated`
    - Suggest: `Terpikselasi`
    - The comment says this is a pixelated version of the icon; "Berkotak-kotak" means checkered/box-patterned, which names a different visual.
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `id/firefox-ios.xliff` — "Post town" is translated as "Kode kota" (city code), which is wrong; it should name the postal town, not a code.
    - Current: `Kode kota`
    - Source: `Post town`
    - Suggest: `Kota pos`
    - The source "Post town" is the town name used for mail sorting (UK), not a code. "Kode kota" means "city code" and also conflicts with "Kode Pos" (Postal Code) in the same form.
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `id/firefox-ios.xliff` — "save actions" (saving-related actions) mistranslated as "menyimpan tindakan" (saving actions/storing actions).
    - Current: `hingga menyimpan tindakan`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `hingga tindakan penyimpanan`
    - The source lists a range of menu items from private browsing to save actions; the Indonesian reverses the head noun and says "to save actions", which is not what the source means.
- `MainMenu.Account.SigningOut.Title.v154` — `id/firefox-ios.xliff` — "Signing out…" (an in-progress state) is rendered as the imperative/plain "Keluar…" (Sign out/Exit).
    - Current: `Keluar…`
    - Source: `Signing out…`
    - Suggest: `Keluar dari akun…`
    - The source is a transient progress message shown while the user is being signed out; "Keluar…" reads as the action label "Sign out", not the ongoing process ("Sedang keluar…").
- `MainMenu.Submenus.Tools.Zoom.Title.v131` — `id/firefox-ios.xliff` — The noun "Zoom (%@)" labeling the current zoom level is translated as the verb "Perbesar" (enlarge).
    - Current: `Perbesar (%@)`
    - Source: `Zoom (%@)`
    - Suggest: `Perbesaran (%@)`
    - The comment says this is the menu component that indicates the current zoom level, a noun; the related subtitle string uses the noun "Perbesaran".
- `NativeErrorPage.Wayback.Error.FooterDescription.v155` — `id/firefox-ios.xliff` — "Internet Archive" translated as "Arsip Internet" while the rest of the file and the link placeholder treat these as product names.
    - Current: `dari Arsip Internet %2$@`
    - Source: `%1$@ can look for an earlier version of this page from the Internet Archive’s %2$@.`
    - Suggest: `dari %2$@ milik Internet Archive`
    - Internet Archive is an organization/brand name; source is "the Internet Archive’s %2$@" and the possessive relation is also lost in the current rendering.
- `NativeErrorPage.Wayback.Error.LinkText.v155` — `id/firefox-ios.xliff` — "Wayback Machine" product name translated, and inconsistent with other strings in the same file that keep it in English.
    - Current: `Mesin Wayback`
    - Source: `Wayback Machine`
    - Suggest: `Wayback Machine`
    - Wayback Machine is a product name from the Internet Archive and is kept untranslated in the other strings of this file (e.g. Wayback.Error.Description, WaybackButtonA11yHint).
- `Onboarding.Customization.Toolbar.Bottom.Action.v123` — `id/firefox-ios.xliff` — "Bottom" (toolbar placement at the bottom of the screen) is translated as "Dasar", which means "basic/base", not the bottom position.
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The developer comment says this option sets the toolbar at the bottom of the screen; Indonesian for that position is "Bawah". "Dasar" reads as "basic" and is also the word used for "Default" elsewhere.
- `Onboarding.Customization.Toolbar.Top.Action.v123` — `id/firefox-ios.xliff` — "Top" (toolbar placement at the top of the screen) is translated as "Puncak" (summit/peak) instead of "Atas".
    - Current: `Puncak`
    - Source: `Top`
    - Suggest: `Atas`
    - The developer comment says this option sets the toolbar at the top of the screen; the positional term in Indonesian is "Atas". "Puncak" means a summit/peak and is wrong for a UI position.
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Description.v148` — `id/firefox-ios.xliff` — "have %@ match your device" is rendered as an instruction for the user to match Firefox to the device, reversing the agent.
    - Current: `atau cocokkan %@ dengan perangkat Anda`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `atau biarkan %@ menyesuaikan dengan perangkat Anda`
    - The source says to let the app follow the device theme automatically, not to have the user perform the matching.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `id/firefox-ios.xliff` — "won't sell you out" (won't betray you) is rendered literally as "tidak akan menjual Anda" (won't sell you), changing the meaning.
    - Current: `tidak akan menjual Anda`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `tidak akan mengkhianati Anda`
    - The English idiom "sell you out" means to betray; the Indonesian literally says the browser will not sell you (as a person), which is not what the source says.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `id/firefox-ios.xliff` — The source says let Firefox match your device; the target imperatively tells the user to match Firefox with the device, changing who acts.
    - Current: `atau cocokkan %@ dengan perangkat Anda`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `atau biarkan %@ menyesuaikan dengan perangkat Anda`
    - "have %@ match your device" means the app follows the device setting automatically, not an instruction to the user to match it.
- `PrivacyDashboard.Fingerprinters.v155` — `id/firefox-ios.xliff` — "Fingerprinters" is rendered as "Penyidik jari" (fingerprint investigators), not the established Firefox term "Pengambil sidik jari".
    - Current: `Penyidik jari`
    - Source: `Fingerprinters`
    - Suggest: `Pengambil Sidik Jari`
    - In privacy context "Fingerprinters" refers to scripts collecting device fingerprints; "penyidik jari" is not a valid Indonesian term (the word is "sidik jari"), and "penyidik" means investigator.
- `PrivacyDashboard.TrackingContent.v155` — `id/firefox-ios.xliff` — "Tracking Content" is translated as "Pelacakan Konten" (content tracking), reversing the head noun.
    - Current: `Pelacakan Konten`
    - Source: `Tracking Content`
    - Suggest: `Konten Pelacak`
    - The source names a category of blocked content (content that tracks), not the act of tracking content; the Indonesian reverses the modifier and head.
- `Settings.Notifications.SyncNotificationsTitle.v112` — `id/firefox-ios.xliff` — The Sync feature name is translated as "Penyelarasan" instead of kept as the product feature name "Sync".
    - Current: `Penyelarasan`
    - Source: `Sync`
    - Suggest: `Sync`
    - "Sync" here is the Firefox Sync feature name; related strings in the same group keep English feature names (e.g. Firefox Suggest).
- `Settings.Notifications.SystemNotificationsDisabledMessage.v112` — `id/firefox-ios.xliff` — "device Settings" is misplaced so the text reads as "Settings > Notifications > Firefox device" instead of the device's Settings app.
    - Current: `Aktifkan dengan membuka Setelan > Notifikasi > %2$@ perangkat`
    - Source: `You turned off all %1$@ notifications. Turn them on by going to device Settings > Notifications > %2$@`
    - Suggest: `Aktifkan dengan membuka Setelan perangkat > Notifikasi > %2$@`
    - In en-US the path is "device Settings > Notifications > %2$@"; the Indonesian appends "perangkat" after the app-name placeholder, breaking the navigation path.
- `Settings.Search.Suggest.ShowSponsoredSuggestions.Description.v124` — `id/firefox-ios.xliff` — "occasional" is mistranslated as "sesaat" (momentary/brief) instead of "sesekali" (occasional).
    - Current: `saran bersponsor sesaat`
    - Source: `Support %@ with occasional sponsored suggestions`
    - Suggest: `saran bersponsor sesekali`
    - en-US "occasional sponsored suggestions" means suggestions that appear now and then; "sesaat" means "for a moment/brief", which changes the meaning.
- `WorldCup.HomepageWidget.FTLabel.v151` — `id/firefox-ios.xliff` — "Full Time" (end of match) is rendered as "Penuh Waktu", a literal word-for-word rendering meaning "full-time (employment)", not the football term for the end of the match.
    - Current: `(Penuh Waktu)`
    - Source: `(Full Time)`
    - Suggest: `(Selesai)`
    - The developer comment says the label indicates the match has ended; the same concept is correctly translated as "Selesai" in WorldCup.HomepageWidget.FulltimePenaltiesScoreLabel.v151, making this both wrong and inconsistent.
- `WorldCup.HomepageWidget.FTNoParenthesisLabel.v151` — `id/firefox-ios.xliff` — "Full Time" (end of match) is rendered as "Penuh Waktu", which means full-time employment, not the end of a match.
    - Current: `Penuh Waktu`
    - Source: `Full Time`
    - Suggest: `Selesai`
    - The developer comment states the label indicates the match has ended; the same term is translated as "Selesai" in the penalties label, so this is wrong and inconsistent within the same screen.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `id/firefox-ios.xliff` — "Match info" (football match) mistranslated as "Info kecocokan" (compatibility/similarity match).
    - Current: `Info kecocokan tidak tersedia saat ini.`
    - Source: `Match info is not available right now. Try refreshing in a few minutes.`
    - Suggest: `Info pertandingan tidak tersedia saat ini.`
    - In the World Cup widget, "match" means a football game ("pertandingan", as used in the ScrollIndicator string), not "kecocokan" = compatibility/matching.
- `WorldCup.HomepageWidget.RoundPhase.ThirdPlaceLabel.v151` — `id/firefox-ios.xliff` — "THIRD PLACE" (ranking) rendered as "TEMPAT KETIGA" (third location/venue).
    - Current: `TEMPAT KETIGA`
    - Source: `THIRD PLACE`
    - Suggest: `PERINGKAT KETIGA`
    - The comment says this labels the third-place winner; "tempat" means a physical place, while a ranking position is "peringkat"/"posisi ketiga".
- `This action will clear all of your private data, including history from your synced devices.` — `id/firefox-ios.xliff` — "your synced devices" rendered without the possessive "Anda", dropping whose devices are meant.
    - Current: `termasuk riwayat dari perangkat yang tersinkronisasi`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `termasuk riwayat dari perangkat Anda yang tersinkronisasi`
    - en-US says "from your synced devices"; the translation omits "your", making it ambiguous about which devices' history is cleared.
- `LibraryPanel.History.Title.v138` — `id/firefox-ios.xliff` — Translation drops "history" qualifier structure and renders "other browsing data" as just "other data".
    - Current: `Menghapus riwayat penjelajahan (termasuk yang tersinkron dari perangkat lain), kuki, dan data lainnya.`
    - Source: `Deletes history (including synced history from other devices), cookies, and other browsing data.`
    - Suggest: `Menghapus riwayat (termasuk riwayat tersinkron dari perangkat lain), kuki, dan data penjelajahan lainnya.`
    - The en-US says "other browsing data"; the Indonesian says only "other data", which is broader than the source, and moves "browsing" onto "riwayat".
- `Back` — `id/firefox-ios.xliff` — Accessibility label for the Back button translated as "Mundur" (move backwards) instead of the standard "Kembali".
    - Current: `Mundur`
    - Source: `Back`
    - Suggest: `Kembali`
    - The en-US "Back" for the toolbar back button is consistently "Kembali" in Indonesian Firefox; "Mundur" reads as "reverse/retreat".
- `Could not add page to Reading List. Maybe it’s already there?` — `id/firefox-ios.xliff` — The object "page" is dropped, so the Indonesian says "could not add the Reading List" instead of "could not add page to Reading List".
    - Current: `Tidak dapat menambahkan Daftar Baca.`
    - Source: `Could not add page to Reading List. Maybe it’s already there?`
    - Suggest: `Tidak dapat menambahkan laman ke Daftar Baca.`
    - en-US: "Could not add page to Reading List." The translation omits "laman ke", changing the meaning; the sibling string translates it correctly as "Tidak dapat menambahkan laman ke Daftar Baca".
- `ErrorPages.AdvancedWarning2.Text` — `id/firefox-ios.xliff` — Adds "hanya jika" (only if), not present in the source's "Proceed if you accept the potential risk."
    - Current: `Lanjutkan hanya jika Anda siap menanggung risikonya.`
    - Source: `It may be a misconfiguration or tampering by an attacker. Proceed if you accept the potential risk.`
    - Suggest: `Lanjutkan jika Anda menerima risiko yang mungkin terjadi.`
    - Source: "Proceed if you accept the potential risk." The added "hanya" (only) changes the condition stated to the user.
- `ErrorPages.CertWarning.Description` — `id/firefox-ios.xliff` — "To protect your information from being stolen" is rendered as "to protect the theft of your information", reversing the meaning.
    - Current: `Untuk melindungi pencurian informasi Anda`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `Untuk melindungi informasi Anda dari pencurian`
    - The source says Firefox protects your information from being stolen; the Indonesian literally says it protects the theft of your information.
- `Menu.AddPin.Confirm2` — `id/firefox-ios.xliff` — Confirmation toast translated as an imperative command instead of a completed action.
    - Current: `Tambahkan ke Pintasan`
    - Source: `Added to Shortcuts`
    - Suggest: `Ditambahkan ke Pintasan`
    - Source "Added to Shortcuts" is a toast confirming the item was added; "Tambahkan ke Pintasan" means "Add to Shortcuts" (imperative), identical to the button label Menu.AddToShortcuts.v99.
- `Menu.TrackingProtectionBlockedContent.Title` — `id/firefox-ios.xliff` — "Tracking content" translated as "Pelacakan konten" (tracking of content) instead of "Konten pelacak" (content that tracks).
    - Current: `Pelacakan konten`
    - Source: `Tracking content`
    - Suggest: `Konten pelacak`
    - The source refers to content containing trackers, not to the act of tracking content; the Indonesian reverses the head noun.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `id/firefox-ios.xliff` — "energy bill" narrowed to "tagihan listrik"... acceptable; but "increase your energy bill" is fine — instead flag none.
    - Current: `tagihan listrik Anda`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `tagihan energi Anda`
    - Source says energy bill; electricity bill is a plausible rendering but narrows the meaning.
- `Open Tabs` — `id/firefox-ios.xliff` — "Open Tabs" (noun, sync setting) translated as the imperative "Buka Tab" (open a tab).
    - Current: `Buka Tab`
    - Source: `Open Tabs`
    - Suggest: `Tab Terbuka`
    - The developer comment says this is a toggle for syncing open tabs, so "Open" is an adjective, not a command.
- `Search.ThirdPartyEngines.DuplicateErrorMessage` — `id/firefox-ios.xliff` — Error message translated as a success ("has been successfully added") instead of stating the engine was already added.
    - Current: `Mesin pencari dengan judul ini atau URL telah berhasil ditambahkan.`
    - Source: `A search engine with this title or URL has already been added.`
    - Suggest: `Mesin pencari dengan judul atau URL ini sudah pernah ditambahkan.`
    - The source says a search engine with this title or URL "has already been added" — it is an error under the title "Failed". The Indonesian "telah berhasil ditambahkan" means "was successfully added", reversing the message into a success confirmation.
- `Settings.Siri.SectionDescription` — `id/firefox-ios.xliff` — "quickly open Firefox" is translated as "membuat Firefox" (make/create Firefox) instead of "membuka Firefox" (open Firefox), and "Siri shortcuts" is left untranslated.
    - Current: `Gunakan Siri shortcuts untuk membuat Firefox dengan cepat lewat Siri`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Gunakan pintasan Siri untuk membuka Firefox dengan cepat lewat Siri`
    - Source says "to quickly open Firefox"; "membuat" means "to make/create", which is a different action.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `id/firefox-ios.xliff` — "some ad tracking" is rendered as "beberapa pelacak" (some trackers), dropping the "ad tracking" meaning.
    - Current: `Mengizinkan beberapa pelacak agar situs web berfungsi dengan baik.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Mengizinkan beberapa pelacakan iklan agar situs web berfungsi dengan baik.`
    - The source says it allows some ad tracking, not some trackers.
- `ShareExtension.LoadInBackgroundAction.Title` — `id/firefox-ios.xliff` — "Load in Background" translated as "Muat di Belakang" (load at the back/behind) instead of background (latar belakang).
    - Current: `Muat di Belakang`
    - Source: `Load in Background`
    - Suggest: `Muat di Latar Belakang`
    - "Background" in the sense of running behind the foreground app is "latar belakang" in Indonesian; "di Belakang" means physically behind.
- `TabTray.Title` — `id/firefox-ios.xliff` — "Open Tabs" (title listing currently open tabs) is rendered as an imperative "Buka Tab" ("Open a tab").
    - Current: `Buka Tab`
    - Source: `Open Tabs`
    - Suggest: `Tab Terbuka`
    - The source is the tab tray title, a noun phrase meaning tabs that are open; "Buka Tab" reads as the command "open tab".
- `TranslationToastHandler.PromptTranslate.Title` — `id/firefox-ios.xliff` — "Translate to %2$@" lost the preposition, so the target language reads as the object being translated.
    - Current: `Terjemahkan %2$@ dengan %3$@?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `Terjemahkan ke %2$@ dengan %3$@?`
    - %2$@ is the local language to translate into; without "ke" the sentence says "translate %2$@" instead of "translate to %2$@".
- `fxa.signin.use-email-instead` — `id/firefox-ios.xliff` — "Use Email Instead" is rendered as "Gunakan Surel Saja" ("Use only email") instead of "as an alternative".
    - Current: `Gunakan Surel Saja`
    - Source: `Use Email Instead`
    - Suggest: `Gunakan Surel Sebagai Gantinya`
    - "Instead" means to use email as an alternative to the QR sign-in; "Saja" means "only/just", changing the meaning.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `id/firefox-ios.xliff` — "won’t remember any of your history" is rendered as "tidak akan mengingat semua riwayat", which reads as "will not remember all history" (i.e. may remember some).
    - Current: `tidak akan mengingat semua riwayat atau kuki`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `tidak akan mengingat riwayat atau kuki apa pun`
    - In Indonesian "tidak akan ... semua" is ambiguous/partial negation; the source asserts none of the history or cookies is remembered.
- `Off` — `id/firefox-ios.xliff` — Accessibility value "Off" is translated as an imperative command "Nonaktifkan" (turn off) instead of the state "Mati".
    - Current: `Nonaktifkan`
    - Source: `Off`
    - Suggest: `Mati`
    - The developer comment says this is a toggled OFF accessibility value, i.e. a state, not an action. "Nonaktifkan" means "deactivate/turn off" as a command.
- `On` — `id/firefox-ios.xliff` — Accessibility value "On" is translated as an imperative command "Aktifkan" (turn on) instead of the state "Nyala".
    - Current: `Aktifkan`
    - Source: `On`
    - Suggest: `Nyala`
    - The developer comment says this is a toggled ON accessibility value, i.e. a state, not an action. "Aktifkan" means "activate/turn on" as a command.
- `Turns private mode on or off` — `id/firefox-ios.xliff` — Accessibility hint describing behaviour is rendered as an imperative instruction instead of a description.
    - Current: `Aktifkan atau nonaktifkan mode pribadi`
    - Source: `Turns private mode on or off`
    - Suggest: `Mengaktifkan atau menonaktifkan mode pribadi`
    - The source "Turns private mode on or off" describes what the control does; the Indonesian imperative tells the user to do it.

### C. Grammar, agreement & spelling

- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `id/firefox-ios.xliff` — "submenu" is written as two words "sub menu" instead of the correct Indonesian "submenu".
    - Current: `Simpan sub menu`
    - Source: `Save submenu`
    - Suggest: `Submenu Simpan`
    - In Indonesian the prefix "sub-" is written closed ("submenu"), and the head noun should precede the modifier.
- `MainMenu.ToolsSection.AccessibilityLabels.Tools.v133` — `id/firefox-ios.xliff` — "submenu" is written as two words "sub menu" instead of the correct Indonesian "submenu".
    - Current: `Sub menu alat`
    - Source: `Tools submenu`
    - Suggest: `Submenu alat`
    - In Indonesian the prefix "sub-" is written closed, giving "submenu".
- `NativeErrorPage.BadCertDomain.ProceedButton.v149` — `id/firefox-ios.xliff` — Misspelling of "Berisiko".
    - Current: `Berrisiko`
    - Source: `Proceed to %@ (Risky)`
    - Suggest: `Berisiko`
    - Indonesian spelling is "berisiko" (one r), not "berrisiko".
- `Onboarding.Welcome.Link.Action.v114` — `id/firefox-ios.xliff` — Missing preposition makes the phrase ungrammatical/incomplete compared to "Learn more in our privacy notice".
    - Current: `Pelajari lebih lanjut pemberitahuan privasi kami`
    - Source: `Learn more in our privacy notice`
    - Suggest: `Pelajari lebih lanjut di pemberitahuan privasi kami`
    - The source says to learn more *in* our privacy notice; the Indonesian drops "di", turning it into "learn more about our privacy notice" and reading ungrammatically.
- `Settings.SearchZero.TrendingSearches.Toggle.v146` — `id/firefox-ios.xliff` — Incorrect capitalization of the relative pronoun "Yang" mid-phrase.
    - Current: `Tampilkan Pencarian Yang Sedang Tren`
    - Source: `Show Trending Searches`
    - Suggest: `Tampilkan Pencarian yang Sedang Tren`
    - Indonesian title case rules (PUEBI) require function words such as "yang" to remain lowercase unless in initial position; the source title case does not justify capitalizing it.
- `Settings.AIControls.AIPoweredFeaturesSection.Title.v151` — `id/firefox-ios.xliff` — "FITUR BERDAYA AI" is not idiomatic/grammatical Indonesian for "AI-POWERED FEATURES".
    - Current: `FITUR BERDAYA AI`
    - Source: `AI-POWERED FEATURES`
    - Suggest: `FITUR BERTENAGA AI`
    - "berdaya" means "having power/capability" of the subject itself, not "powered by"; the standard rendering is "bertenaga AI" or "didukung AI".
- `Settings.AIControls.HeaderCard.Message.v151` — `id/firefox-ios.xliff` — Awkward/ungrammatical rendering of "whether to use" using "jikalau akan".
    - Current: `Itu termasuk jikalau akan menggunakan fitur yang ditingkatkan dengan AI.`
    - Source: `That includes whether to use features enhanced with AI.`
    - Suggest: `Itu termasuk apakah akan menggunakan fitur yang ditingkatkan dengan AI.`
    - "whether to use" is "apakah akan menggunakan"; "jikalau" means "if/in case" and is ungrammatical in this indirect-question construction.
- `Summarizer.Error.MissingPageContent.Message.v142` — `id/firefox-ios.xliff` — "tekan meringkas" is ungrammatical; the source refers to pressing the Summarize button.
    - Current: `lalu tekan meringkas`
    - Source: `Page is still loading. Wait for it to finish, then hit summarize.`
    - Suggest: `lalu tekan Ringkas`
    - "hit summarize" refers to the Summarize control; "tekan meringkas" (press to-summarize) is not grammatical Indonesian.
- `WebCompatReporter.Preview.Data.BlockedTrackers.v155` — `id/firefox-ios.xliff` — Missing relative marker "yang" makes the phrase read as "Tracker hostnames blocked" ungrammatically.
    - Current: `Nama host pelacak diblokir di laman ini`
    - Source: `Hostnames of trackers blocked on this page`
    - Suggest: `Nama host pelacak yang diblokir di laman ini`
    - The source is a noun phrase "Hostnames of trackers blocked on this page"; without "yang" the Indonesian reads as a clause/sentence, and is inconsistent with the parallel string "daftar item yang diblokir oleh perlindungan pelacakan".
- `Authentication required` — `id/firefox-ios.xliff` — "Otentikasi" is a non-standard spelling; the correct Indonesian form is "Autentikasi".
    - Current: `Otentikasi dibutuhkan`
    - Source: `Authentication required`
    - Suggest: `Autentikasi dibutuhkan`
    - KBBI/standard Indonesian technical term is "autentikasi".
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `id/firefox-ios.xliff` — Missing verb: "apa yang Anda daring" drops "do" from "what you do online".
    - Current: `melihat apa yang Anda daring`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `melihat apa yang Anda lakukan daring`
    - The source says "what you do online"; the Indonesian omits the verb, leaving an ungrammatical clause.
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `id/firefox-ios.xliff` — "Try again" rendered as "Coba beberapa saat lagi", dropping the verb "lagi/ulang" sense of retrying.
    - Current: `Coba beberapa saat lagi.`
    - Source: `There was a problem accessing tabs from your other devices. Try again in a few moments.`
    - Suggest: `Coba lagi beberapa saat lagi.`
    - The source instructs the user to retry shortly; the translation reads only "try in a few moments" without conveying retry.
- `Search Input Field` — `id/firefox-ios.xliff` — "Bidan" (midwife) is a typo for "Bidang" (field).
    - Current: `Bidan Isian Pencarian`
    - Source: `Search Input Field`
    - Suggest: `Bidang Isian Pencarian`
    - The source is "Search Input Field"; "Bidan" means midwife, the intended word is "Bidang" (field).

### D. Terminology, register & consistency

- `Bookmarks.Menu.EditBookmarkMobileBookmarksLabel.v154` — `id/firefox-ios.xliff` — "BOOKMARKS" is rendered as "BOOKMARK" while the parallel DESKTOP BOOKMARKS header uses "MARKAH", creating inconsistent terminology on the same screen.
    - Current: `BOOKMARK SELULER`
    - Source: `MOBILE BOOKMARKS`
    - Suggest: `MARKAH SELULER`
    - The developer comment says this header is shown alongside the 'DESKTOP BOOKMARKS' header, which is translated "MARKAH DESKTOP"; the same term must be rendered consistently as "markah" throughout the Bookmarks file.
- `MainMenu.Account.AccessibilityLabels.BackButton.v132` — `id/firefox-ios.xliff` — "Back" navigation button rendered as "Mundur" (move backwards/retreat) instead of the standard "Kembali".
    - Current: `Mundur`
    - Source: `Back`
    - Suggest: `Kembali`
    - In iOS navigation UI, the Back button is consistently "Kembali" in Indonesian; "Mundur" means to reverse/retreat and is not the navigation term.
- `MainMenu.SiteProtection.Protections.Title.v153` — `id/firefox-ios.xliff` — "Protections" is translated as "Proteksi" here while the other Protections strings on the same screen use "Perlindungan".
    - Current: `Proteksi`
    - Source: `Protections`
    - Suggest: `Perlindungan`
    - MainMenu.SiteProtection.ProtectionsOff/On use "Perlindungan" for the same source term on the same screen; the badge label should match.
- `MainMenu.Submenus.Save.AccessibilityLabels.SaveToReadingList.Subtitle.v132` — `id/firefox-ios.xliff` — "Reading List" is rendered as "Daftar Baca" here but "Daftar Bacaan" in the parallel v131 strings on the same menu.
    - Current: `Daftar Baca`
    - Source: `Reading List`
    - Suggest: `Daftar Bacaan`
    - Same source term "Reading List" on the same submenu is translated inconsistently (v131 Subtitle uses "Daftar Bacaan", and the RemoveFromReadingList accessibility label also uses "Daftar Bacaan").
- `MainMenu.Submenus.Save.AccessibilityLabels.SaveToReadingList.Title.v132` — `id/firefox-ios.xliff` — "Reading List" rendered "Daftar Baca" inconsistently with "Daftar Bacaan" used elsewhere in the same menu.
    - Current: `Simpan ke Daftar Baca`
    - Source: `Save to Reading List`
    - Suggest: `Simpan ke Daftar Bacaan`
    - The v131 counterpart of this same menu item uses "Daftar Bacaan"; inconsistent term for the same source string on the same screen.
- `MainMenu.Submenus.Save.RemoveFromReadingList.Title.v131` — `id/firefox-ios.xliff` — "Reading List" rendered "Daftar Baca" while the accessibility label for the same item uses "Daftar Bacaan".
    - Current: `Hapus dari Daftar Baca`
    - Source: `Remove from Reading List`
    - Suggest: `Hapus dari Daftar Bacaan`
    - Inconsistent rendering of "Reading List" within the same submenu; the v132 accessibility label for this item uses "Daftar Bacaan".
- `MainMenu.Submenus.Tools.AccessibilityLabels.ReaderView.Off.Title.v132` — `id/firefox-ios.xliff` — "Turn off" is translated "Matikan" here while the parallel Night Mode off string uses "Nonaktifkan".
    - Current: `Matikan Tampilan Pembaca`
    - Source: `Turn off Reader View`
    - Suggest: `Nonaktifkan Tampilan Pembaca`
    - Inconsistent rendering of "Turn off" within the same Tools submenu (Night Mode Off uses "Nonaktifkan", and the corresponding "Turn on" strings both use "Aktifkan").
- `MainMenu.Submenus.Tools.AccessibilityLabels.Zoom.Title.v132` — `id/firefox-ios.xliff` — The zoom-level label uses the verb "Perbesar" instead of the noun "Perbesaran" used for the same Zoom term in the sibling subtitle.
    - Current: `Perbesar (%@)`
    - Source: `Zoom (%@)`
    - Suggest: `Perbesaran (%@)`
    - The comment says this label indicates the current zoom level (a noun); the sibling Zoom.Subtitle uses "Perbesaran", so "Perbesar" is both inconsistent and grammatically a verb.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `id/firefox-ios.xliff` — "Reader View" is rendered inconsistently as "Tampilan Pembaca" here but "Tampilan Baca" in the accessibility label on the same screen.
    - Current: `Matikan Tampilan Pembaca`
    - Source: `Turn off Reader View`
    - Suggest: `Matikan Tampilan Baca`
    - The same source term "Reader View" must be consistent within the MainMenu group; MainMenu.ToolsSection.AccessibilityLabels.ReaderView.v150 uses "Tampilan Baca".
- `MainMenu.ToolsSection.AccessibilityLabels.PageZoom.Title.v142` — `id/firefox-ios.xliff` — "Page Zoom" is translated as "Pembesaran Laman" here but "Zum Laman" in the menu title for the same feature.
    - Current: `Pembesaran Laman`
    - Source: `Page Zoom`
    - Suggest: `Zum Laman`
    - MainMenu.Submenus.Tools.PageZoomV2.Title.v141 renders the same source term "Page Zoom" as "Zum Laman"; the accessibility label should match the visible control.
- `Onboarding.Modern.Customization.Toolbar.Bottom.Action.v140` — `id/firefox-ios.xliff` — "Bottom" as a screen position is translated as "Dasar" (basic/base), the wrong sense in Indonesian UI.
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The option sets the toolbar at the bottom of the screen; Indonesian uses "Bawah" for this. "Dasar" is also the established translation for "Default"/"basic", causing confusion.
- `Onboarding.Modern.Customization.Toolbar.Bottom.Action.v145` — `id/firefox-ios.xliff` — "Bottom" as a screen position is translated as "Dasar" (base/basic), the wrong sense.
    - Current: `Dasar`
    - Source: `Bottom`
    - Suggest: `Bawah`
    - The action places the toolbar at the bottom of the screen; the correct Indonesian positional term is "Bawah".
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v140` — `id/firefox-ios.xliff` — "Top" as a screen position is translated as "Puncak" (summit/peak), the wrong sense.
    - Current: `Puncak`
    - Source: `Top`
    - Suggest: `Atas`
    - The option sets the toolbar at the top of the screen; Indonesian UI uses "Atas", not "Puncak" (mountain summit).
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v145` — `id/firefox-ios.xliff` — "Top" as a screen position is translated as "Puncak" (summit/peak), the wrong sense.
    - Current: `Puncak`
    - Source: `Top`
    - Suggest: `Atas`
    - The action places the toolbar at the top of the screen; the correct positional term is "Atas".
- `PasswordGenerator.A11yLabel.v132` — `id/firefox-ios.xliff` — "Password" is rendered as "Kata Sandi" here while the PasswordAutofill strings consistently use "sandi".
    - Current: `Pembuat Kata Sandi`
    - Source: `Password Generator`
    - Suggest: `Pembuat Sandi`
    - Terminology inconsistency: other password strings in this batch use "sandi" (Kelola sandi, Gunakan sandi tersimpan).
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `id/firefox-ios.xliff` — "email masks" is rendered "topeng surel" here while other strings in the same feature use "masker surel".
    - Current: `topeng surel`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `masker surel`
    - RelayMask.strings uses "masker surel" in RelayEmailMaskAvailableCFR, GenericErrorMessage, SettingsTitle, etc.; "topeng surel" is an inconsistent rendering of the same term on the same feature.
- `RelayMask.RelayEmailMaskInsertedA11yAnnouncement.v147` — `id/firefox-ios.xliff` — "Email mask" rendered "Topeng surel" instead of the feature's established "Masker surel".
    - Current: `Topeng surel dimasukkan`
    - Source: `Email mask inserted`
    - Suggest: `Masker surel dimasukkan`
    - Inconsistent with "masker surel" used throughout RelayMask.strings.
- `RelayMask.RelayEmailMaskSettingsDetailInfo.v147` — `id/firefox-ios.xliff` — "email masks" rendered "topeng surel" instead of the feature's established "masker surel".
    - Current: `topeng surel`
    - Source: `Hide your real email to protect your inbox from spam. Some sites don’t support email masks.`
    - Suggest: `masker surel`
    - Inconsistent with "masker surel" used in the settings title, toggle, and other strings on the same screen.
- `Summarizer.HostedBrand.Label.v142` — `id/firefox-ios.xliff` — "Summarized by" is rendered "Diringkas oleh" here but "Dirangkum oleh" in the parallel Apple Intelligence label on the same screen.
    - Current: `Diringkas oleh %@`
    - Source: `Summarized by %@`
    - Suggest: `Dirangkum oleh %@`
    - Summarizer.AppleBrand.Label.v142 uses "Dirangkum oleh" for the identical source phrase in the same summary report; the two labels must match.
- `TermsOfUse.TitleValue1.v147` — `id/firefox-ios.xliff` — "Terms of Use" is rendered as "Syarat Penggunaan" here but "Ketentuan Penggunaan" everywhere else in the same file.
    - Current: `Syarat Penggunaan`
    - Source: `Terms of Use`
    - Suggest: `Ketentuan Penggunaan`
    - The same source term "Terms of Use" is translated "Ketentuan Penggunaan" in TermsOfUse.Description.v142, TermsOfUse.Link.TermsOfUse.v142 and TermsOfUse.TermsOfUseHasOpened.v142; this variant title is inconsistent on the same sheet.
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `id/firefox-ios.xliff` — "Enhanced Tracking Protection" is not rendered with the established Indonesian product term "Perlindungan Pelacakan yang Ditingkatkan" word order used elsewhere—wrong feature name form.
    - Current: `Pengaturan Perlindungan Pelacakan yang Ditingkatkan untuk situs ini`
    - Source: `Enhanced Tracking Protection setting for this site`
    - Suggest: `Pengaturan Perlindungan Pelacakan Ditingkatkan untuk situs ini`
    - The feature name in Firefox id is "Perlindungan Pelacakan Ditingkatkan"; adding "yang" makes it a descriptive phrase rather than the product feature name.
- `WebCompatReporter.SubOption.ItemsNotVisible.v154` — `id/firefox-ios.xliff` — "Items" is translated as "Butir" here but as "Item" in the sibling sub-options on the same screen, and the relative clause form does not match the source's label style.
    - Current: `Butir yang tidak sepenuhnya terlihat`
    - Source: `Items not fully visible`
    - Suggest: `Item tidak sepenuhnya terlihat`
    - The other sub-options in the same 'Design is broken' group render "Items" as "Item" (ItemsMisaligned, ItemsOverlapped); the inconsistency plus the "yang" clause turns a label into a noun phrase.
- `WorldCup.HomepageWidget.RetryButtonLabel.v151` — `id/firefox-ios.xliff` — "Refresh" is translated inconsistently within the same widget: "Segarkan" elsewhere, "Muat ulang" here.
    - Current: `Muat ulang`
    - Source: `Refresh`
    - Suggest: `Segarkan`
    - The identical source term "Refresh" in WorldCup.HomepageWidget.MatchUnavailableRefreshButtonLabel is "Segarkan"; both are refresh buttons in the same widget error state.
- `DefaultBrowserOnboarding.Description2` — `id/firefox-ios.xliff` — "Browser" and "Default" left untranslated here while translated as "Peramban Baku" elsewhere in the same file.
    - Current: `2. Ketuk App Browser Default`
    - Source: `2. Tap Default Browser App`
    - Suggest: `2. Ketuk Aplikasi Peramban Baku`
    - Settings.DefaultBrowserMenuItem and DefaultBrowserCard.Title use "Peramban Baku"; this onboarding step uses untranslated "App Browser Default", an inconsistent terminology within the same screen/file.
- `Added page to Reading List` — `id/firefox-ios.xliff` — "Reading List" is rendered "Daftar Baca" here but "Daftar Bacaan" in the neighbouring reading-list strings.
    - Current: `Ditambahkan ke Daftar Baca`
    - Source: `Added page to Reading List`
    - Suggest: `Halaman ditambahkan ke Daftar Bacaan`
    - The same feature name "Reading List" is translated "Daftar Bacaan" in "Add to Reading List" and Address.Bar.ReadingList.v106; also "page" is dropped from the source.
- `FirefoxHome.Pocket.Minutes.v99` — `id/firefox-ios.xliff` — Minutes not abbreviated despite the developer comment requiring abbreviation due to space constraints.
    - Current: `%d menit`
    - Source: `%d min`
    - Suggest: `%d mnt`
    - The comment states "Minutes should be abbreviated due to space constraints"; the related string FirefoxHome.Stories.Minutes.v140 uses "mnt".
- `Logins.WelcomeView.TurnOnAutoFill` — `id/firefox-ios.xliff` — "AutoFill" rendered as "Isi-Auto" here but "Isi Otomatis" in the title on the same screen.
    - Current: `Aktifkan Isi-Auto`
    - Source: `Turn on AutoFill`
    - Suggest: `Aktifkan Isi Otomatis`
    - Logins.WelcomeView.Title2 on the same welcome screen uses "Isi Otomatis" for AutoFill; the inconsistent "Isi-Auto" is not the established term.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `id/firefox-ios.xliff` — "Fingerprinters" rendered as "Sidik jari" (fingerprints) here but as "Pelacak Sidik" in the corresponding title string.
    - Current: `Sidik jari mengumpulkan berbagai pengaturan unik ini`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `Pelacak sidik jari mengumpulkan berbagai pengaturan unik ini`
    - Fingerprinters are the actors collecting settings; "Sidik jari" means fingerprints and is inconsistent with Menu.TrackingProtectionFingerprintersBlocked.Title on the same screen.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `id/firefox-ios.xliff` — "Reading List" rendered as "Daftar Baca" instead of the established "Daftar Bacaan".
    - Current: `Simpan laman ke Daftar Baca`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Simpan laman ke Daftar Bacaan`
    - Other strings in the same file translate "Reading List" as "Daftar Bacaan" (Reading list, Remove from Reading List); this is an inconsistent term for the same feature name.
- `PzSrmZ-2GqvPe` — `id/firefox-ios.xliff` — "Go to Copied Link" is rendered inconsistently with the same command elsewhere in the widget strings.
    - Current: `Buka Tautan Tersalin`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `Buka Tautan yang Disalin`
    - String 2GqvPe in the same file translates the identical menu item "Go to Copied Link" as "Buka Tautan yang Disalin"; the confirmation label must quote the same wording.

### E. Typography, punctuation & spacing

- `NativeErrorPage.BadCertDomain.AdvancedInfo.v149` — `id/firefox-ios.xliff` — Missing final period present in the source sentence.
    - Current: `%1$@ tidak memercayai situs ini karena sertifikat yang ditemukan tidak valid untuk %2$@`
    - Source: `%1$@ doesn’t trust this site because the certificate found isn’t valid for %2$@.`
    - Suggest: `%1$@ tidak memercayai situs ini karena sertifikat yang ditemukan tidak valid untuk %2$@.`
    - The en-US string ends with a period; the translation drops the sentence-final punctuation.
- `ScanQRCode.PermissionError.Message.v100` — `id/firefox-ios.xliff` — Closing single quotes are rendered as opening quotes (‘Pengaturan‘, ‘Firefox‘).
    - Current: `‘Pengaturan‘ perangkat > ‘Firefox‘`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `‘Pengaturan’ perangkat > ‘Firefox’`
    - The source uses ‘…’ with a proper closing quote; the target repeats the opening quote character as the closing one.
- `Settings.ShowLinkPreviews.StatusV2` — `id/firefox-ios.xliff` — Sentence-case source "When long-pressing links" is rendered in title case, unlike the v2 source which deliberately lowercased it.
    - Current: `Ketika Menekan-lama Tautan`
    - Source: `When long-pressing links`
    - Suggest: `Ketika menekan-lama tautan`
    - The StatusV2 variant exists specifically to change capitalization from title case to sentence case; the translation keeps title case.
- `TopSites.RemovePage.Button` — `id/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `Hapus halaman - %@`
    - Source: `Remove page — %@`
    - Suggest: `Hapus halaman — %@`
    - The en-US uses an em dash separator; the localization uses a plain hyphen surrounded by spaces.
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

### Fixed to date (0)

_Nothing fixed yet._
