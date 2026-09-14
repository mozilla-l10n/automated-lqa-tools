# Firefox iOS l10n QA — cs

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,906 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for cs: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (94)

- `This action will clear all of your private data, including history from your synced devices.` — `cs/firefox-ios.xliff` — "all of your private data" is rendered as "všechna vaše data", dropping "private"/soukromá.
    - Current: `Tato akce smaže všechna vaše data, včetně historie prohlížení ze všech synchronizovaných zařízení.`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `Tato akce smaže všechna vaše soukromá data, včetně historie prohlížení ze synchronizovaných zařízení.`
    - The source says "all of your private data"; the Czech says "all your data", which overstates what will be deleted (and the sibling string in ClearPrivateDataConfirm correctly uses "soukromá data").
- `DefaultBrowserCard.Description` — `cs/firefox-ios.xliff` — Translation says links, e-mails and messages will open in Firefox, instead of links from websites, e-mails and Messages.
    - Current: `Nastavte si automatické otevírání odkazů, e-mailů a zpráv ve Firefoxu.`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `Nastavte si, aby se odkazy z webových stránek, e-mailů a Zpráv automaticky otevíraly ve Firefoxu.`
    - The source is "Set links from websites, emails, and Messages to open automatically in Firefox" — the lists are sources of links, not items opened in Firefox.
- `DefaultBrowserCard.Button.v2` — `cs/firefox-ios.xliff` — "Learn How" translated as "Zjistit více" (Learn more).
    - Current: `Zjistit více`
    - Source: `Learn How`
    - Suggest: `Zjistit jak`
    - The developer comment says the button teaches the user how to set the default browser; "Zjistit více" corresponds to "Learn more", a different string.
- `Enter passcode` — `cs/firefox-ios.xliff` — "passcode" translated as "heslo" (password) instead of the device passcode term.
    - Current: `Zadejte heslo`
    - Source: `Enter passcode`
    - Suggest: `Zadejte kód`
    - The string refers to the app/device passcode, not a password; using "heslo" conflicts with password terminology used elsewhere (e.g. saved passwords).
- `Offline Website Data` — `cs/firefox-ios.xliff` — "Offline Website Data" rendered as "Offline obsah" (offline content), losing "website data".
    - Current: `Offline obsah`
    - Source: `Offline Website Data`
    - Suggest: `Offline data stránek`
    - The source and developer comment refer to website data stored offline, not generic offline content.
- `LibraryPanel.History.AllTimeOption.v138` — `cs/firefox-ios.xliff` — "All Time" (time range option for clearing history) is rendered as "Po celý čas" ("for the whole time"), not the standard Czech time-range label.
    - Current: `Po celý čas`
    - Source: `All Time`
    - Suggest: `Vše`
    - The option sits alongside "Poslední hodina", "Posledních 24 hodin" etc. and means the entire history range; "Po celý čas" is an adverbial phrase that does not read as a range option.
- `FirefoxHomepage.JumpBackIn.TabPickup.OpenTab.A11y.v106` — `cs/firefox-ios.xliff` — Singular "synced tab" rendered as plural "synchronizované panely".
    - Current: `Otevřít synchronizované panely`
    - Source: `Open synced tab`
    - Suggest: `Otevřít synchronizovaný panel`
    - The source is "Open synced tab" — an accessibility action that opens the one synced tab shown in the cell, not all synced tabs.
- `FirefoxHomepage.JumpBackIn.TabPickup.ShowAll.ButtonTitle.v104` — `cs/firefox-ios.xliff` — "See all synced tabs" drops "all".
    - Current: `Zobrazit synchronizované panely`
    - Source: `See all synced tabs`
    - Suggest: `Zobrazit všechny synchronizované panely`
    - The source explicitly says "See all synced tabs"; the Czech omits "all", which is the distinguishing part of this button.
- `Firefox.HomePage.Title` — `cs/firefox-ios.xliff` — "Firefox Home Page" translated as just "Výchozí", losing the meaning and the brand name.
    - Current: `Výchozí`
    - Source: `Firefox Home Page`
    - Suggest: `Domovská stránka Firefoxu`
    - The source names the Firefox home page shown in the tab history list; "Výchozí" means "Default" and does not convey a home page nor the product name.
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `cs/firefox-ios.xliff` — Accessibility label adds an invented instruction and mangles the subject.
    - Current: `Logo Firefox - klepnutím změní tapetu.`
    - Source: `Firefox logo, change the wallpaper.`
    - Suggest: `Logo Firefoxu, změnit tapetu.`
    - The source is "Firefox logo, change the wallpaper." — a simple VoiceOver label; the Czech adds "klepnutím" (by tapping) and uses a third-person verb with no subject, which is both ungrammatical and content the source never stated.
- `LibraryPanel.History.ClearHistoryMenuTitle.v100` — `cs/firefox-ios.xliff` — "other browsing data" translated as "související data" (related data), losing the meaning of browsing data.
    - Current: `cookies a související data`
    - Source: `Removes history (including history synced from other devices), cookies and other browsing data.`
    - Suggest: `cookies a další data o prohlížení`
    - The en-US says "cookies and other browsing data"; "související data" means "related data", which is not what the source says.
- `Logins.PasscodeRequirement.Warning` — `cs/firefox-ios.xliff` — The brand name Firefox is dropped from the warning message.
    - Current: `Pro používání funkce automatického vyplňování si na svém zařízení nastavte kód zámku.`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Pro používání funkce automatického vyplňování ve Firefoxu si na svém zařízení nastavte kód zámku.`
    - The source specifies "the AutoFill feature for Firefox"; the Czech omits the product name, making the statement apply to AutoFill in general.
- `Menu.Passwords.Label` — `cs/firefox-ios.xliff` — "Passwords" is rendered as "Přihlašovací údaje" (logins/credentials) while other strings in the same batch translate "password" as "heslo".
    - Current: `Přihlašovací údaje`
    - Source: `Passwords`
    - Suggest: `Hesla`
    - The source term is "Passwords"; nearby strings (Logins.WelcomeView.Title2, LoginsList.SelectPassword.Title) use "hesla", so this menu entry is inconsistent with the password terminology.
- `Menu.AddToShortcuts.v99` — `cs/firefox-ios.xliff` — "Add to Shortcuts" translated as "Přidat zkratku" (Add a shortcut) instead of "Přidat do zkratek".
    - Current: `Přidat zkratku`
    - Source: `Add to Shortcuts`
    - Suggest: `Přidat do zkratek`
    - The source says add the current site to Shortcuts; the confirmation toast uses "Přidáno do zkratek", so the action label should match.
- `LoginsList.NoMatchingResult.Subtitle` — `cs/firefox-ios.xliff` — Translation adds "přihlašovací údaje" (logins), while the source says generically "no results".
    - Current: `Vašemu vyhledávání neodpovídají žádné přihlašovací údaje.`
    - Source: `There are no results matching your search.`
    - Suggest: `Vašemu vyhledávání neodpovídají žádné výsledky.`
    - en-US: "There are no results matching your search." — the Czech narrows "results" to "logins".
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `cs/firefox-ios.xliff` — "Cross-Site Trackers" is rendered as the generic "Sledovací prvky" (trackers), losing the cross-site distinction and colliding with other tracker categories on the same panel.
    - Current: `Sledovací prvky`
    - Source: `Cross-Site Trackers`
    - Suggest: `Sledovací prvky mezi weby`
    - The en-US title specifies cross-site trackers; the Czech says only "trackers", which is ambiguous next to the other tracker categories (social, content) on the same tracking protection screen.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `cs/firefox-ios.xliff` — The translation drops "secretly" and the energy-bill consequence from the cryptominer description.
    - Current: `Těžba kryptoměn využívá výpočetní výkon vašeho zařízení k získávání digitálních měn. Běžící skripty vybíjí vaši baterii a vaše zařízení zpomalují.`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Těžaři kryptoměn tajně využívají výpočetní výkon vašeho zařízení k získávání digitálních měn. Těžební skripty vybíjí vaši baterii, zpomalují vaše zařízení a mohou zvýšit váš účet za elektřinu.`
    - en-US says cryptominers "secretly use" the computing power and that scripts "can increase your energy bill"; both elements are missing in Czech.
- `ReaderMode.Available.VoiceOverAnnouncement` — `cs/firefox-ios.xliff` — Gender agreement error: adjective "dostupný" does not agree with neuter noun "Zobrazení".
    - Current: `Je dostupný Zobrazení čtečky`
    - Source: `Reader Mode available`
    - Suggest: `Zobrazení čtečky je dostupné`
    - "Zobrazení" is neuter, so the predicate adjective must be "dostupné"; the current form is ungrammatical.
- `Send Feedback` — `cs/firefox-ios.xliff` — "Send Feedback" translated as "Odeslat hodnocení" (send a rating/review) instead of feedback.
    - Current: `Odeslat hodnocení`
    - Source: `Send Feedback`
    - Suggest: `Odeslat zpětnou vazbu`
    - The menu item opens a feedback submission page; "hodnocení" means rating/review, not feedback.
- `Settings.Home.Option.StartAtHome.Title` — `cs/firefox-ios.xliff` — "Opening screen" section title rendered as a verb phrase inconsistent with the related section header translated as "ÚVODNÍ OBRAZOVKA".
    - Current: `Po otevření aplikace zobrazit`
    - Source: `Opening screen`
    - Suggest: `Úvodní obrazovka`
    - The same source term "Opening screen" is translated as "ÚVODNÍ OBRAZOVKA" in Settings.Home.Option.Wallpaper.CollectionTitle, creating an inconsistency for the same setting title.
- `Settings.Home.Option.Wallpaper.Accessibility.ToggleButton` — `cs/firefox-ios.xliff` — The "wallpaper cycle" aspect of the toggle is dropped, so the label describes a generic wallpaper switch.
    - Current: `Přepínač tapety domovské stránky`
    - Source: `Homepage wallpaper cycle toggle`
    - Suggest: `Přepínač střídání tapet na domovské stránce`
    - Source is "Homepage wallpaper cycle toggle" — the toggle controls cycling through wallpapers, not the wallpaper itself.
- `Settings.NewTab.Option.FirefoxHome` — `cs/firefox-ios.xliff` — "Firefox Home" is rendered as "Výchozí domovskou stránku" (default homepage), dropping the Firefox brand name and conflicting with the separate "Homepage" option.
    - Current: `Výchozí domovskou stránku`
    - Source: `Firefox Home`
    - Suggest: `Domovskou stránku Firefoxu`
    - The source names the Firefox Home page; the brand must be kept and the option is distinct from the user-set "Homepage" option in the same screen.
- `Settings.SendUsage.Message` — `cs/firefox-ios.xliff` — Translation drops "only collect what we need to provide" and "for everyone", asserting a different claim about data collection.
    - Current: `Mozilla sbírá jenom informace potřebné pro vylepšování Firefoxu.`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `Mozilla se snaží sbírat jen data, která potřebuje k poskytování a vylepšování Firefoxu pro všechny.`
    - The en-US says Mozilla "strives to only collect what we need to provide and improve Firefox for everyone"; the Czech states as fact that it collects only info needed for improvement, changing what the product asserts about its data practices.
- `Settings.Passwords.OnboardingMessage.v103` — `cs/firefox-ios.xliff` — "are now protected" loses "now"; minor but the sentence also drops "device" from "device passcode".
    - Current: `Vaše hesla jsou chráněná pomocí Face ID, Touch ID nebo kódu zámku.`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `Vaše hesla jsou nyní chráněná pomocí Face ID, Touch ID nebo kódu zámku zařízení.`
    - The source specifies "now" and "a device passcode"; both qualifiers are omitted.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `cs/firefox-ios.xliff` — "haven't viewed" rendered as "neotevřeli" (haven't opened) instead of "nezobrazili/neprohlíželi".
    - Current: `které jste dva týdny neotevřeli`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `které jste si dva týdny nezobrazili`
    - Source says tabs you haven't viewed for two weeks; "neotevřeli" means not opened, which is a different condition (a tab can be open but not viewed).
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `cs/firefox-ios.xliff` — "some ad tracking" translated as "některé sledující reklamy" (some tracking ads).
    - Current: `Povoluje některé sledující reklamy pro správné fungování stránek.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Povoluje část sledování reklamami, aby stránky fungovaly správně.`
    - The source allows some ad tracking (the tracking activity), not certain ads themselves.
- `Settings.WebsiteData.SelectedConfirmPrompt` — `cs/firefox-ios.xliff` — "the selected items" rendered as "všechny vybrané položky" (all selected items), adding "all".
    - Current: `Tato akce smaže všechny vybrané položky`
    - Source: `This action will clear the selected items. It cannot be undone.`
    - Suggest: `Tato akce smaže vybrané položky`
    - Source says "the selected items"; the added "všechny" changes the scope of the confirmation dialog.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `cs/firefox-ios.xliff` — "Pages load faster, but some functionality may not work" mistranslated as "Zrychlí i načítání stránek, ale může omezit jejich fungování".
    - Current: `Zrychlí i načítání stránek, ale může omezit jejich fungování.`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `Stránky se načítají rychleji, ale některé funkce nemusí fungovat.`
    - The source says some functionality may not work; the Czech asserts the protection will limit page functioning, and adds "i" which the source does not have.
- `Settings.TrackingProtection.ProtectionCellFooter` — `cs/firefox-ios.xliff` — "helps stop advertisers from tracking" rendered as the absolute "zabrání inzerentům sledovat" (will prevent advertisers from tracking).
    - Current: `zabrání inzerentům sledovat vás na internetu`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `pomáhá zabránit inzerentům ve sledování vašeho prohlížení`
    - The source only claims it "helps stop" tracking; the Czech makes an unqualified promise about the product's behaviour.
- `Tabs %@ to %@ of %@` — `cs/firefox-ios.xliff` — Plural noun rendered as singular in the tab range announcement.
    - Current: `Panel %1$@ až %2$@ ze %3$@`
    - Source: `Tabs %1$@ to %2$@ of %3$@`
    - Suggest: `Panely %1$@ až %2$@ z %3$@`
    - Source is "Tabs %1$@ to %2$@ of %3$@" (a range, plural); the Czech uses the singular "Panel", inconsistent with the other tab-range strings.
- `TopSites.RemovePage.Button` — `cs/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `Odebrat stránku - %@`
    - Source: `Remove page — %@`
    - Suggest: `Odebrat stránku — %@`
    - The en-US string uses an em dash "Remove page — %@"; a plain hyphen surrounded by spaces is not correct Czech typography.
- `Tabs Tray` — `cs/firefox-ios.xliff` — "Tabs Tray" translated as "Lišta panelů" (tab bar) instead of the tab overview/panel grid.
    - Current: `Lišta panelů`
    - Source: `Tabs Tray`
    - Suggest: `Přehled panelů`
    - The accessibility label refers to the Tabs Tray view (the grid of open tabs), not a toolbar/bar; "lišta" names a different UI element.
- `UIMenuItem.SearchWithFirefox` — `cs/firefox-ios.xliff` — "Search with Firefox" is rendered only as "Vyhledat", dropping the Firefox brand name.
    - Current: `Vyhledat`
    - Source: `Search with Firefox`
    - Suggest: `Vyhledat pomocí Firefoxu`
    - The source names the product performing the search; the Czech omits it entirely.
- `You don’t have any tabs open in Firefox on your other devices.` — `cs/firefox-ios.xliff` — The Firefox brand reference is dropped from the message.
    - Current: `Ve vašich zařízeních nejsou otevřené žádné panely.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `Na vašich dalších zařízeních nemáte ve Firefoxu otevřené žádné panely.`
    - Source says "in Firefox on your other devices"; the Czech omits both "in Firefox" and "other".
- `Created %@` — `cs/firefox-ios.xliff` — "Created" is translated as "Uloženo" (Saved).
    - Current: `Uloženo %@`
    - Source: `Created %@`
    - Suggest: `Vytvořeno %@`
    - The developer comment says the label describes when the login was created, not saved.
- `Well, this is embarrassing.` — `cs/firefox-ios.xliff` — "Ale toto je nepříjemné." is an awkward, ungrammatical-sounding rendering of the idiom.
    - Current: `Ale toto je nepříjemné.`
    - Source: `Well, this is embarrassing.`
    - Suggest: `To je ale trapné.`
    - The Czech word order with "Ale toto" is not idiomatic for the English interjection "Well, this is embarrassing."
- `Logins will be removed from all connected devices.` — `cs/firefox-ios.xliff` — "connected devices" translated as "synchronizovaných zařízení" (synced devices).
    - Current: `Přihlašovací údaje budou odstraněny ze všech synchronizovaných zařízení.`
    - Source: `Logins will be removed from all connected devices.`
    - Suggest: `Přihlašovací údaje budou odstraněny ze všech připojených zařízení.`
    - The source says "all connected devices", not "synced devices"; the sibling string that does say "synced devices" uses the same Czech wording, losing the distinction.
- `Website` — `cs/firefox-ios.xliff` — "Website" rendered as "Server" instead of the website/web page term.
    - Current: `Server`
    - Source: `Website`
    - Suggest: `Webová stránka`
    - The label sits above the website row in Login Detail View; "Server" names a different concept than "Website".
- `ContextMenu.OpenInNewPrivateTabButtonTitle` — `cs/firefox-ios.xliff` — "New" is dropped: the source says open in a new private tab.
    - Current: `Otevřít v anonymním panelu`
    - Source: `Open in New Private Tab`
    - Suggest: `Otevřít v novém anonymním panelu`
    - en-US "Open in New Private Tab" specifies a new tab; the Czech omits "novém".
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `cs/firefox-ios.xliff` — "new bookmarks" rendered as "vytvořené záložky" and "any of your history" weakened.
    - Current: `ale vytvořené záložky budou uloženy`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `ale nové záložky budou uloženy`
    - Source says "new bookmarks will be saved"; "vytvořené" (created) is not the same qualifier.
- `When Leaving Private Browsing` — `cs/firefox-ios.xliff` — Setting label starts with a lowercase letter where the source is a capitalized label.
    - Current: `po opuštění anonymního prohlížení`
    - Source: `When Leaving Private Browsing`
    - Suggest: `Po opuštění anonymního prohlížení`
    - Displayed in Settings as a label under 'Close Private Tabs'; sentence-initial capitalization is expected.
- `TodayWidget.NewTabButtonLabelV1` — `cs/firefox-ios.xliff` — "New Search" translated as "Nový dotaz" (new query) instead of "Nové vyhledávání".
    - Current: `Nový dotaz`
    - Source: `New Search`
    - Suggest: `Nové vyhledávání`
    - Source is "New Search"; the sibling string uses "vyhledávání" for search, making this inconsistent.
- `TodayWidget.PrivateTabButtonLabelV1` — `cs/firefox-ios.xliff` — "Private" rendered as "Soukromé" instead of the established "anonymní".
    - Current: `Soukromé vyhledávání`
    - Source: `Private Search`
    - Suggest: `Anonymní vyhledávání`
    - All other strings in this group translate "private" as "anonymní" (Zavřít anonymní panely, Vyhledat v anonymním panelu); this one is inconsistent.
- `TodayWidget.QuickActionGalleryDescription` — `cs/firefox-ios.xliff` — The instruction to touch and hold the widget to edit it is garbled.
    - Current: `Pro úpravu nebo výběr jiné zkratky na widgetu podržte prst.`
    - Source: `Add a Firefox shortcut to your Home screen. After adding the widget, touch and hold to edit it and select a different shortcut.`
    - Suggest: `Po přidání widgetu na něm podržte prst, abyste ho mohli upravit a vybrat jinou zkratku.`
    - Source: "After adding the widget, touch and hold to edit it and select a different shortcut." The Czech drops "After adding the widget" and turns the sequence into an either/or.
- `Bookmarks.Menu.DeletedBookmark.v131` — `cs/firefox-ios.xliff` — Uses straight/English curly quotes instead of the Czech german-double quotes used elsewhere in the file.
    - Current: `Smazáno “%@”`
    - Source: `Deleted “%@”`
    - Suggest: `Smazáno „%@“`
    - The cs convention is german-double quotes („ “), as used in Bookmarks.Menu.SavedBookmarkToastLabel.v136 in the same file.
- `ContextualHints.FeltDeletion.Body.v122` — `cs/firefox-ios.xliff` — Em dash of the source replaced with a hyphen.
    - Current: `soubory cookie - všechno`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `soubory cookie – všechno`
    - The source uses a dash (—); a plain hyphen with spaces is not a valid dash in Czech typography.
- `Logins.DevicePasscodeRequired.Message.v122` — `cs/firefox-ios.xliff` — "passwords" is rendered as "přihlašovacích údajů" (login credentials) instead of "hesel".
    - Current: `Pro ukládání a automatické vyplňování přihlašovacích údajů`
    - Source: `To save and automatically fill passwords, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Pro ukládání a automatické vyplňování hesel`
    - The source says "To save and automatically fill passwords"; the Czech says login credentials, which is a different term than the passwords terminology used consistently elsewhere in this batch.
- `Engagement.Notification.Title.v112` — `cs/firefox-ios.xliff` — Imperative rendered as indicative future tense.
    - Current: `Začnete své první vyhledávání`
    - Source: `Start your first search`
    - Suggest: `Začněte své první vyhledávání`
    - The source "Start your first search" is an imperative call to action; "Začnete" is the 2nd person future indicative ("you will start"), not the imperative "Začněte". Other notifications in the same file use imperatives (Prohlížejte, Vyzkoušejte).
- `Menu.EnhancedTrackingProtection.Details.TrackersStandardModeFooterText.v150` — `cs/firefox-ios.xliff` — "you may see" translated with an impersonal/wrong subject, making the browser rather than the user the one who sees the count.
    - Current: `Může proto zaznamenat vyšší počet sledovacích prvků.`
    - Source: `Standard blocks common trackers after a page starts loading, so you may see a higher tracker count. %@`
    - Suggest: `Můžete proto zaznamenat vyšší počet sledovacích prvků.`
    - Source says "so you may see a higher tracker count" — the subject is the user (2nd person plural), not the blocking level.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `cs/firefox-ios.xliff` — "you may see" translated with the wrong subject, attributing the observation to the mode instead of the user.
    - Current: `Může tedy zaznamenat nižší počet sledovacích prvků.`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `Můžete tedy zaznamenat nižší počet sledovacích prvků.`
    - Source says "so you may see a lower tracker count" — the subject is the user (2nd person plural).
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `cs/firefox-ios.xliff` — "Tracking content" translated as "Sledující obsah" (content that watches) instead of the established "Sledovací obsah".
    - Current: `Sledující obsah: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Sledovací obsah: %@`
    - Elsewhere in this screen the adjective is consistently "sledovací" (sledovací prvky, sledovací cookies); "sledující" is an inconsistent and incorrect rendering of the standard term.
- `Menu.EnhancedTrackingProtection.Certificates.IssuerOrganization.v131` — `cs/firefox-ios.xliff` — "Organization" translated as "Společnost" (company).
    - Current: `Společnost`
    - Source: `Organization`
    - Suggest: `Organizace`
    - The certificate field is "Organization"; the Czech term for the certificate field is "Organizace", not "Společnost" (company), which narrows the meaning.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNamesDNSName.v131` — `cs/firefox-ios.xliff` — "DNS Name" translated as "Záznam DNS" (DNS record).
    - Current: `Záznam DNS`
    - Source: `DNS Name`
    - Suggest: `Název DNS`
    - The certificate field is the DNS name of the subject alt name, not a DNS record.
- `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `cs/firefox-ios.xliff` — Translation drops "on this device" and changes the imperative to a third-person statement.
    - Current: `Nezanechá stopy`
    - Source: `Leave no traces on this device`
    - Suggest: `Nezanechávejte na tomto zařízení žádné stopy`
    - The en-US title "Leave no traces on this device" addresses the user and specifies the device; the Czech says "It leaves no traces" without the device scope.
- `CloseTab.ArrivingNotification.title.v133` — `cs/firefox-ios.xliff` — The notification title mistranslates "%1$@ tabs closed: %2$@" as "Firefox closed tabs", turning the app name into the subject of a verb and losing the count structure.
    - Current: `%1$@ zavřel panely: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `Panely zavřené v %1$@: %2$@`
    - In en-US "%1$@ tabs closed: %2$@" means the number of tabs (%2$@) closed in the app (%1$@); the Czech reads as "Firefox closed the tabs: 3", asserting the app performed the closing rather than reporting a count.
- `CloseTab.ViewAction.title.v133` — `cs/firefox-ios.xliff` — Action label translated as a noun phrase ("Zobrazení") instead of an imperative/verb as required for an action button.
    - Current: `Zobrazení nedávno zavřených panelů`
    - Source: `View recently closed tabs`
    - Suggest: `Zobrazit nedávno zavřené panely`
    - The comment says this is a label for an action used to view recently closed tabs; "Zobrazení" is the noun "viewing", not the action "View".
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `cs/firefox-ios.xliff` — "save actions" mistranslated as "ukládání akcí" (saving actions).
    - Current: `od anonymního prohlížení po ukládání akcí`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `od anonymního prohlížení po akce pro ukládání`
    - The source "from private browsing to save actions" refers to save-related actions in the menu, not to "saving actions".
- `LiveActivity.Downloads.FileNameText.v138` — `cs/firefox-ios.xliff` — Straight/English-style quotes used instead of the Czech german-double quotes.
    - Current: `Stahuje se “%@”`
    - Source: `Downloading “%@”`
    - Suggest: `Stahuje se „%@“`
    - The locale convention is german-double quotes; the current string uses “ ” (English opening/closing pair).
- `MainMenu.Submenus.Tools.AccessibilityLabels.Zoom.Subtitle.v132` — `cs/firefox-ios.xliff` — "Zoom" (page zoom tool) is rendered as "Zvětšit okno" (enlarge window), which names the wrong thing and is inconsistent with the Zoom title string.
    - Current: `Zvětšit okno`
    - Source: `Zoom`
    - Suggest: `Zvětšení stránky`
    - The developer comment says this is the Zoom tool that applies zoom on a page; "okno" (window) is wrong and conflicts with the sibling string "Zvětšení stránky (%@)".
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `cs/firefox-ios.xliff` — "Unselected" (state of a radio button) is rendered as "Výběr zrušen" ("selection cancelled"), an action rather than a state.
    - Current: `Výběr zrušen`
    - Source: `Unselected`
    - Suggest: `Nevybráno`
    - The accessibility label states that the survey option is not selected; the Czech announces that a selection was cancelled, which is a different meaning.
- _…and 34 more._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (65)

- `AddressToolbar.GoogleLens.A11yLabel.v153.v2` — `Shared/Supporting Files/en.lproj/AddressToolbar.strings` — Accessibility label is rendered as an imperative addressed to the user instead of a noun-style label describing the button.
    - Current: `Vyhledejte obrázek pomocí Google Lens`
    - Suggest: `Vyhledat obrázek pomocí Google Lens`
    - The en-US "Search image with Google Lens" is a button label; other button labels in this file use the infinitive (e.g. "Pořídit fotografii"), not the 2nd-person imperative.
- `AddressToolbar.SearchEngine.A11y.Label.v128` — `Shared/Supporting Files/en.lproj/AddressToolbar.strings` — "Search Engine" is translated as "Vyhledávací modul" while the neighbouring string uses "vyhledávač".
    - Current: `Vyhledávací modul: %@`
    - Suggest: `Vyhledávač: %@`
    - AddressToolbar.SearchEngine.A11y.Hint.v133 in the same file renders "search engine" as "vyhledávač"; the same term on the same control should be consistent.
- `Bookmarks.Menu.DeletedBookmark.v131` — `Shared/Supporting Files/en.lproj/Bookmarks.strings` — Uses English-style straight/curly quotes instead of Czech quotation marks used elsewhere in the same file.
    - Current: `Smazáno “%@”`
    - Suggest: `Smazáno „%@“`
    - Other strings in the same file (Bookmarks.Menu.SavedBookmarkToastLabel.v136) correctly use Czech quotes „…“; here the English closing-style quotes are kept, which is inconsistent typography for cs.
- `ContextualHints.FeltDeletion.Body.v122` — `Shared/Supporting Files/en.lproj/ContextualHints.strings` — Em dash from the source replaced with a hyphen surrounded by spaces.
    - Current: `soubory cookie - všechno.`
    - Suggest: `soubory cookie – všechno.`
    - Czech typography uses an en/em dash (–) for parenthetical breaks, matching the source's em dash; a plain hyphen is incorrect.
- `Logins.DevicePasscodeRequired.Message.v122` — `Shared/Supporting Files/en.lproj/Credentials.strings` — "passwords" translated as "přihlašovacích údajů" (login credentials).
    - Current: `automatické vyplňování přihlašovacích údajů`
    - Suggest: `automatické vyplňování hesel`
    - The source says "passwords"; the rest of the feature strings use "hesla", and "přihlašovací údaje" corresponds to logins/credentials.
- `Addresses.EditAddress.AutofillAddressNeighborhood.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Neighborhood" as an address field is mistranslated as "Sousedství" (the abstract concept of neighbourliness/proximity), not a city district.
    - Current: `Sousedství`
    - Suggest: `Čtvrť`
    - The field asks for the name of a neighbourhood/district within a city; Czech uses "Čtvrť" (or "Městská část"). "Sousedství" means proximity/neighbourliness and is not an address component.
- `Addresses.EditAddress.AutofillAddressOrganization.v129` — `Shared/Supporting Files/en.lproj/EditAddress.strings` — "Organization" is rendered as "Společnost" (company), narrowing the meaning.
    - Current: `Společnost`
    - Suggest: `Organizace`
    - The comment says the field holds the organization's name, which may be any organization, not only a commercial company; Czech has the direct equivalent "Organizace".
- `Engagement.Notification.Title.v112` — `Shared/Supporting Files/en.lproj/EngagementNotification.strings` — Imperative "Start your first search" rendered as future indicative "Začnete" instead of imperative "Začněte".
    - Current: `Začnete své první vyhledávání`
    - Suggest: `Začněte své první vyhledávání`
    - The en-US is an imperative call to action; "Začnete" is the 2nd person plural future indicative ("you will start"), a typo for the imperative "Začněte".
- `Menu.EnhancedTrackingProtection.Certificates.IssuerOrganization.v131` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "Organization" translated as "Společnost" (company) instead of "Organizace".
    - Current: `Společnost`
    - Suggest: `Organizace`
    - The certificate field is the issuer Organization (O); the Czech term is "Organizace", not "Společnost" (company).
- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNamesDNSName.v131` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "DNS Name" translated as "Záznam DNS" (DNS record).
    - Current: `Záznam DNS`
    - Suggest: `Název DNS`
    - The certificate field is a DNS name of the subject, not a DNS record; "Záznam" means record.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "Tracking content" is translated as "Sledující obsah" (content that tracks/watches) instead of the standard Firefox term "Sledovací obsah".
    - Current: `Sledující obsah: %@`
    - Suggest: `Sledovací obsah: %@`
    - The active participle "sledující" means "watching"; the established Czech Firefox term for tracking content is "sledovací obsah", consistent with "sledovací prvky" used elsewhere in this file.
- `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `Shared/Supporting Files/en.lproj/FirefoxHomepage.strings` — The translation drops "on this device" and changes the imperative to a third-person statement.
    - Current: `Nezanechá stopy`
    - Suggest: `Nezanechávejte na tomto zařízení žádné stopy`
    - Source is "Leave no traces on this device"; the Czech omits "on this device" and renders it as "(It) leaves no traces".
- `CloseTab.ArrivingNotification.title.v133` — `Shared/Supporting Files/en.lproj/FxANotification.strings` — The notification title is mistranslated: %1$@ is the app name, and the Czech turns it into the app closing tabs rather than "tabs closed in <app>: <count>".
    - Current: `%1$@ zavřel panely: %2$@`
    - Suggest: `Panely zavřené v prohlížeči %1$@: %2$@`
    - Source "%1$@ tabs closed: %2$@" means tabs were closed in the named app (%1$@ = app name, %2$@ = number of tabs); the Czech reads "Firefox closed tabs: <number>" attributing the action to the app and losing the count relation.
- `CloseTab.ViewAction.title.v133` — `Shared/Supporting Files/en.lproj/FxANotification.strings` — Action label rendered as a noun ("Zobrazení") instead of an imperative verb for a button action.
    - Current: `Zobrazení nedávno zavřených panelů`
    - Suggest: `Zobrazit nedávno zavřené panely`
    - The developer comment says this is a label for an action; en-US "View recently closed tabs" is a verb phrase, and Czech action labels use the infinitive/imperative.
- `LiveActivity.Downloads.FileNameText.v138` — `Shared/Supporting Files/en.lproj/LiveActivity.strings` — Straight/English quotation marks used instead of Czech quotes.
    - Current: `Stahuje se “%@”`
    - Suggest: `Stahuje se „%@“`
    - Czech typography requires „…“ quotation marks; the English style “…” was copied from the source.
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "save actions" (actions for saving) is mistranslated as "ukládání akcí" (saving of actions).
    - Current: `od anonymního prohlížení po ukládání akcí`
    - Suggest: `od anonymního prohlížení po akce ukládání`
    - The source lists features from private browsing to save actions (i.e. actions that save content); the Czech genitive reverses the relation and says "saving actions".
- `MainMenu.SettingsSection.AccessibilityLabels.CustomizeHomepage.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Customize Homepage" is rendered only as "Přizpůsobit", dropping the object of the accessibility label.
    - Current: `Přizpůsobit`
    - Suggest: `Přizpůsobit domovskou stránku`
    - The accessibility label must state the target (Customize Homepage); "Přizpůsobit" alone means merely "Customize" and loses the content.
- `MainMenu.Submenus.Tools.AccessibilityLabels.Zoom.Subtitle.v132` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Zoom" (page zoom) is translated as "Zvětšit okno" (enlarge window), which names the wrong object and conflicts with the related Zoom strings.
    - Current: `Zvětšit okno`
    - Suggest: `Zvětšení stránky`
    - The developer comment states this is the Zoom tool that applies zoom on a page, not a window; other strings in the same submenu use "Zvětšení stránky".
- `MainMenu.Submenus.Tools.Zoom.Subtitle.v131` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Zoom" is rendered as "Zvětšit okno" (enlarge window) instead of page zoom, inconsistent with the sibling Zoom title strings.
    - Current: `Zvětšit okno`
    - Suggest: `Zvětšení stránky`
    - The comment says this subtitle is for the Zoom tool (zoom on a page); "okno" (window) is the wrong object and the same screen uses "Zvětšení stránky".
- `Onboarding.IntroDescriptionPart1.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "For good." is rendered as "Navždy." (forever), losing the intended "for the good of all / for good causes" meaning.
    - Current: `Nezávislý. Neziskový. Navždy.`
    - Suggest: `Nezávislý. Neziskový. Pro dobrou věc.`
    - In the source "For good." pairs with "Indie. Non-profit." and means acting for the common good, not "forever".
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — %2$@ is the company name (Mozilla), but the Czech calls it "aplikace" (the app).
    - Current: `s marketingovými partnery aplikace %2$@`
    - Suggest: `s marketingovými partnery společnosti %2$@`
    - The developer comment states %2$@ is the company name (e.g. Mozilla); labelling it as an application is wrong content.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Mismatched constructions: finite verb "Souhlasím" coordinated with infinitive "pokračovat".
    - Current: `Souhlasím a pokračovat`
    - Suggest: `Souhlasit a pokračovat`
    - Czech button labels must be grammatically consistent; "Souhlasím a pokračovat" mixes 1st-person indicative with an infinitive, which is ungrammatical.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v140` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Top" (position of the toolbar) is rendered as directional "Nahoru" (upwards) instead of locative "Nahoře" (at the top).
    - Current: `Nahoru`
    - Suggest: `Nahoře`
    - The option describes where the toolbar is placed; the parallel option is "Dole" (at the bottom) and the v145 variant of the same string correctly uses "Nahoře". "Nahoru" means "upwards" (direction).
- `Onboarding.Modern.Sync.Title.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "on all your browsing adventures" is reduced to "za dobrodružstvím", dropping "all your browsing".
    - Current: `Vydejte se s aplikací %@ za dobrodružstvím`
    - Suggest: `Vydejte se s aplikací %@ za všemi svými dobrodružstvími při prohlížení`
    - The source emphasizes taking the app along on all browsing adventures; the translation omits both "all" and "browsing".
- `Onboarding.Modern.TermsOfService.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "trusted for over 20 years" is rendered as "které důvěřujete" (which you have trusted), changing the meaning and attributing trust to the individual user.
    - Current: `Přináší nezisková organizace %@, které důvěřujete již více než 20 let`
    - Suggest: `Přináší nezisková organizace %@, které se důvěřuje již více než 20 let`
    - The source says the non-profit has been trusted (generally, by people) for over 20 years, not that the reader personally has trusted it for 20 years.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Manage settings" is translated as just "Nastavení" (Settings), dropping the verb.
    - Current: `Nastavení`
    - Suggest: `Spravovat nastavení`
    - The v145 source changed from "Manage" to "Manage settings"; the Czech only says "Settings", losing the manage action.
- `Onboarding.Wallpaper.Description.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "a wallpaper that speaks to you" mistranslated as "tapetu, která vás vyjadřuje" (a wallpaper that expresses you).
    - Current: `Vyberte si tapetu, která vás vyjadřuje.`
    - Suggest: `Vyberte si tapetu, která vás osloví.`
    - The English means a wallpaper that appeals to/resonates with the user; "která vás vyjadřuje" says the wallpaper expresses the user, which is a different statement and ungrammatical in sense.
- `Onboarding.Welcome.Link.Action.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "privacy notice" (singular document) rendered as plural "oznámeních o ochraně osobních údajů", inconsistent with the term used elsewhere in the same file.
    - Current: `Další informace naleznete v našich oznámeních o ochraně osobních údajů`
    - Suggest: `Další informace naleznete v našich zásadách ochrany osobních údajů`
    - The source refers to one document, the Privacy Notice; the same file translates "Privacy Notice" as "Zásady ochrany osobních údajů" (Onboarding.TermsOfService.PrivacyNoticeLink.v135). The plural "oznámeních" is both wrong in number and terminologically inconsistent.
- `PrivacyDashboard.CrossSiteTrackers.v155` — `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings` — "Cross-Site" is dropped, so the label no longer distinguishes cross-site tracking cookies.
    - Current: `Sledovací cookies`
    - Suggest: `Sledovací cookies mezi weby`
    - Source is "Cross-Site Tracking Cookies"; the Czech omits the cross-site qualifier, which is the key distinguishing part of this Privacy Dashboard category.
- `PrimaryButton.Label.v112` — `Shared/Supporting Files/en.lproj/ResearchSurface.strings` — Button uses "průzkum" while the body text of the same popup calls it "dotazník", an inconsistent term for "survey" on one screen.
    - Current: `Vyplnit průzkum`
    - Suggest: `Vyplnit dotazník`
    - Body.Text.v112 translates "survey" as "dotazník"; the button on the same popup must use the same term.
- `CreditCard.Settings.EmptyListTitle.v122` — `Shared/Supporting Files/en.lproj/Settings.strings` — Plural "Cards" rendered as singular "platební kartu" and "do aplikace" added.
    - Current: `Uložit platební kartu do aplikace %@`
    - Suggest: `Uložit platební karty do %@`
    - en-US "Save Cards to %@" is plural; the Czech says "save a payment card" (singular). Compare the parallel address string "Uložit adresy do %@".
- `Settings.Studies.Message.v148` — `Shared/Supporting Files/en.lproj/Settings.strings` — The translation says quality is improved "for it" (the app) rather than "for everyone", and the subject of testing is wrong.
    - Current: `%@ náhodně vybírá uživatele, aby otestoval nové funkce, s cílem zlepšit jeho kvalitu pro všechny.`
    - Suggest: `%@ náhodně vybírá uživatele, aby otestovali nové funkce, což zlepšuje kvalitu pro všechny.`
    - Source: "randomly selects users to test features, which improves quality for everyone." The Czech singular "aby otestoval" makes the app the tester instead of the users, and "zlepšit jeho kvalitu" adds a possessive not in the source.
- `CreditCard.SnackBar.UpdatedCardLabel.v122` — `Shared/Supporting Files/en.lproj/SnackBar.strings` — Subject–verb agreement error: "Informace" (plural) with singular verb form.
    - Current: `Informace o kartě byla aktualizována`
    - Suggest: `Informace o kartě byly aktualizovány`
    - "Informace o kartě" is plural here; the predicate must agree: "byly aktualizovány".
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v134` — `Shared/Supporting Files/en.lproj/SocialShare.strings` — Inconsistent/incorrect participle form "Odeslané" instead of "Odesláno" as used in the parallel strings.
    - Current: `Odeslané z aplikace`
    - Suggest: `Odesláno z aplikace`
    - The other "Sent from %2$@" strings use the impersonal "Odesláno"; "Odeslané" is an adjectival plural form that does not agree with anything here.
- `ContextualHints.Summarize.Description.v142` — `Shared/Supporting Files/en.lproj/Summarize.strings` — Awkward duplication "zobrazíte zobrazení čtečky" and it repeats "Klepnutím" for "Touch and hold".
    - Current: `Klepnutím a podržením zobrazíte zobrazení čtečky.`
    - Suggest: `Dotykem a podržením otevřete režim čtečky.`
    - The en-US "Touch and hold for Reader View" is rendered with a redundant repetition ("zobrazíte zobrazení"), degrading the language.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — Missing comma before "nebo" in the correlative "buď … nebo" construction and clumsy wording.
    - Current: `Tato stránka je buď s omezením nebo se jedná převážně o vizuální stránku.`
    - Suggest: `Tato stránka může být omezená, nebo se jedná převážně o vizuální obsah.`
    - Czech punctuation requires a comma before "nebo" in the "buď…, nebo…" pair; the phrase "je buď s omezením" is also ungrammatical.
- `TabsTray.SyncTabs.SyncTabsButton.Title.v119` — `Shared/Supporting Files/en.lproj/TabsTray.strings` — "Sync Tabs" is rendered as just "Synchronizovat", dropping the object "tabs".
    - Current: `Synchronizovat`
    - Suggest: `Synchronizovat panely`
    - The source button label is "Sync Tabs"; the Czech omits "panely", losing the specific meaning of syncing tabs.
- `TermsOfUse.Link.PrivacyNotice.v142` — `Shared/Supporting Files/en.lproj/TermsOfUse.strings` — "Privacy Notice" is translated as "Zásady ochrany osobních údajů" here but as "Oznámení o ochraně osobních údajů" in the description on the same sheet.
    - Current: `Zásady ochrany osobních údajů`
    - Suggest: `Oznámení o ochraně osobních údajů`
    - The same source term "Privacy Notice" appears in TermsOfUse.Description.v142 as "Oznámení o ochraně osobních údajů"; the link label must match on the same screen.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `Shared/Supporting Files/en.lproj/TermsOfUse.strings` — Uses "Podmínkami používání" while every other string in the same file uses "Podmínky použití".
    - Current: `Přehled s Podmínkami používání byl otevřen`
    - Suggest: `Panel s Podmínkami použití byl otevřen`
    - Terminology inconsistency for "Terms of Use" within the same screen (cf. TermsOfUse.TitleValue1.v147 "Podmínky použití").
- `Toolbar.NewTab.Button.v142` — `Shared/Supporting Files/en.lproj/Toolbar.strings` — The imperative action label "Summarize page" is translated as the noun "Shrnutí stránky" (page summary).
    - Current: `Shrnutí stránky`
    - Suggest: `Shrnout stránku`
    - Source is a verb phrase describing the button action; Czech renders it as a noun, and it also collides with "Souhrn stránky" usage elsewhere.
- `CreditCard.RememberCard.SecondaryButtonTitle.v116` — `Shared/Supporting Files/en.lproj/UpdateCard.strings` — Subject–predicate agreement error: plural "informace" takes plural verb form.
    - Current: `Informace o kartě byla aktualizována`
    - Suggest: `Informace o kartě byly aktualizovány`
    - En-US "Card Information Updated" is rendered with the plural noun "informace" but a singular participle/verb; Czech requires "byly aktualizovány".
- `WebCompatReporter.Preview.Data.IsTablet.v155` — `Shared/Supporting Files/en.lproj/WebCompatReporter.strings` — "Whether or not your device is a tablet" mistranslated as "Bez ohledu na to, zda..." ("Regardless of whether...").
    - Current: `Bez ohledu na to, zda je vaše zařízení tablet`
    - Suggest: `Zda je vaše zařízení tablet`
    - The bullet lists the data sent: whether the device is a tablet. "Bez ohledu na to" means "regardless of", which changes the meaning.
- `WorldCup.HomepageWidget.RoundPhase.WinWorldCupLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "2026 WORLD CUP CHAMPIONS" is rendered as "MISTROVSTVÍ SVĚTA 2026" (World Cup 2026), dropping the "champions" meaning.
    - Current: `MISTROVSTVÍ SVĚTA 2026`
    - Suggest: `MISTŘI SVĚTA 2026`
    - The label marks the championship winner; the Czech text names the tournament instead of the champions.
- `Enter passcode` — `Shared/en.lproj/AuthenticationManager.strings` — "passcode" is translated as "heslo" (password) instead of the device passcode term.
    - Current: `Zadejte heslo`
    - Suggest: `Zadejte kód`
    - The string refers to the numeric passcode, which is distinct from a password (heslo) elsewhere in the UI.
- `This action will clear all of your private data, including history from your synced devices.` — `Shared/en.lproj/ClearHistoryConfirm.strings` — "all of your private data" is translated as "všechna vaše data", dropping "private".
    - Current: `Tato akce smaže všechna vaše data, včetně historie prohlížení ze všech synchronizovaných zařízení.`
    - Suggest: `Tato akce smaže všechna vaše soukromá data, včetně historie prohlížení ze synchronizovaných zařízení.`
    - The source says "private data"; omitting it overstates the scope of the deletion.
- `DefaultBrowserCard.Button.v2` — `Shared/en.lproj/Default Browser.strings` — "Learn How" is translated as "Zjistit více" (Learn more) instead of how to do it.
    - Current: `Zjistit více`
    - Suggest: `Zjistit jak`
    - The source and comment specify a button to learn how to set the default browser, not a generic "learn more".
- `DefaultBrowserCard.Description` — `Shared/en.lproj/Default Browser.strings` — The Czech says links, e-mails and messages open in Firefox, but the source says links from websites, e-mails and Messages open in Firefox.
    - Current: `Nastavte si automatické otevírání odkazů, e-mailů a zpráv ve Firefoxu.`
    - Suggest: `Nastavte si automatické otevírání odkazů z webových stránek, e-mailů a Zpráv ve Firefoxu.`
    - In the source, "from websites, emails, and Messages" modifies "links" — it is the source of the links, not three kinds of items being opened.
- `LibraryPanel.History.AllTimeOption.v138` — `Shared/en.lproj/HistoryPanel.strings` — "All Time" as a time-range option is rendered "Po celý čas" (for the whole time) instead of "Vše"/"Od počátku".
    - Current: `Po celý čas`
    - Suggest: `Vše`
    - The option is one of a list of time ranges (Last hour, Last 24 hours…); "Po celý čas" is not the Czech idiom for the all-time range.
- `Firefox.HomePage.Title` — `Shared/en.lproj/Localizable.strings` — "Firefox Home Page" translated as just "Výchozí" (Default), losing the meaning.
    - Current: `Výchozí`
    - Suggest: `Domovská stránka Firefoxu`
    - The source names the Firefox home page shown in the tab history list; "Výchozí" means "Default" and does not convey it.
- `FirefoxHomepage.JumpBackIn.TabPickup.OpenTab.A11y.v106` — `Shared/en.lproj/Localizable.strings` — Singular "synced tab" rendered as plural "synchronizované panely".
    - Current: `Otevřít synchronizované panely`
    - Suggest: `Otevřít synchronizovaný panel`
    - The accessibility action opens one specific synced tab; en-US is singular "Open synced tab".
- `Menu.AddToShortcuts.v99` — `Shared/en.lproj/Localizable.strings` — "Add to Shortcuts" is rendered as "Add shortcut", losing the target destination and breaking consistency with the "Přidáno do zkratek" toast.
    - Current: `Přidat zkratku`
    - Suggest: `Přidat do zkratek`
    - The source says the page is pinned to the Shortcuts section; the confirmation toast Menu.AddPin.Confirm2 uses "Přidáno do zkratek".
- `Menu.CustomizeHomePage.v99` — `Shared/en.lproj/Localizable.strings` — "Customize Homepage" translated only as "Přizpůsobit", dropping the homepage object.
    - Current: `Přizpůsobit`
    - Suggest: `Přizpůsobit domovskou stránku`
    - The source specifies what is being customized (the Firefox Home page); the Czech is a bare "Customize" with no object, and no length limit is noted in the comment.
- `ReaderMode.Available.VoiceOverAnnouncement` — `Shared/en.lproj/Localizable.strings` — Gender agreement error: adjective "dostupný" does not agree with neuter noun "Zobrazení".
    - Current: `Je dostupný Zobrazení čtečky`
    - Suggest: `Je dostupné zobrazení čtečky`
    - "Zobrazení" is neuter, so the predicate adjective must be "dostupné", not masculine "dostupný".
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `Shared/en.lproj/Localizable.strings` — "in the Reader View controls" mistranslated as "v ovládání seznamu ke čtení" (reading list controls).
    - Current: `v ovládání seznamu ke čtení`
    - Suggest: `v ovládacích prvcích zobrazení čtečky`
    - The source says the icon is in the Reader View controls, not the reading list controls.
- `Tabs %@ to %@ of %@` — `Shared/en.lproj/Localizable.strings` — Plural noun rendered in singular: "Panel" should be "Panely" for a range of tabs.
    - Current: `Panel %1$@ až %2$@ ze %3$@`
    - Suggest: `Panely %1$@ až %2$@ z %3$@`
    - The source "Tabs %1$@ to %2$@ of %3$@" refers to multiple visible tabs; Czech uses the singular "Panel", which is grammatically wrong for a range.
- `TopSites.RemovePage.Button` — `Shared/en.lproj/Localizable.strings` — Em dash of the source replaced with a hyphen.
    - Current: `Odebrat stránku - %@`
    - Suggest: `Odebrat stránku – %@`
    - Source uses an em dash separator; Czech typography requires an en/em dash, not a hyphen, between clauses.
- `UIMenuItem.SearchWithFirefox` — `Shared/en.lproj/Localizable.strings` — The brand name Firefox is dropped from the text-selection menu item.
    - Current: `Vyhledat`
    - Suggest: `Vyhledat pomocí Firefoxu`
    - en-US is "Search with Firefox"; the Czech only says "Search", losing the product name.
- `Well, this is embarrassing.` — `Shared/en.lproj/Localizable.strings` — Ungrammatical rendering of "Well, this is embarrassing."
    - Current: `Ale toto je nepříjemné.`
    - Suggest: `No, to je ale nepříjemné.`
    - "Ale toto je nepříjemné." is not idiomatic Czech word order for the interjection "Well,"; it reads as a broken sentence.
- `You don’t have any tabs open in Firefox on your other devices.` — `Shared/en.lproj/Localizable.strings` — Translation omits "in Firefox" from the error message.
    - Current: `Ve vašich zařízeních nejsou otevřené žádné panely.`
    - Suggest: `Ve Firefoxu na vašich dalších zařízeních nejsou otevřené žádné panely.`
    - The source specifies tabs open in Firefox on your other devices; the Czech drops both "in Firefox" and "other".
- `Created %@` — `Shared/en.lproj/LoginManager.strings` — "Created" is translated as "Uloženo" (Saved) instead of "Vytvořeno".
    - Current: `Uloženo %@`
    - Suggest: `Vytvořeno %@`
    - The label describes when the login was created; "Uloženo" means "Saved", a different notion than the source "Created".
- _…and 5 more._

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
| quotes | `german-double` 13, `curly-double` 2 | **german-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (94)

> **Reads as a deliberate edit (4).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Modern.TermsOfService.Description.v145` — `cs/firefox-ios.xliff` — "trusted for over 20 years" is rendered as "which you have trusted for over 20 years", asserting the user's trust rather than general trust.
    - Current: `Přináší nezisková organizace %@, které důvěřujete již více než 20 let`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Přináší nezisková organizace %@, které se důvěřuje již více než 20 let`
    - The source states the non-profit is trusted (generally, by people) for over 20 years; the Czech asserts that the reader personally has trusted it for over 20 years.
- `This action will clear all of your private data, including history from your synced devices.` — `cs/firefox-ios.xliff` — "all of your private data" is rendered as "všechna vaše data", dropping "private"/soukromá.
    - Current: `Tato akce smaže všechna vaše data, včetně historie prohlížení ze všech synchronizovaných zařízení.`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `Tato akce smaže všechna vaše soukromá data, včetně historie prohlížení ze synchronizovaných zařízení.`
    - The source says "all of your private data"; the Czech says "all your data", which overstates what will be deleted (and the sibling string in ClearPrivateDataConfirm correctly uses "soukromá data").
- `Settings.SendUsage.Message` — `cs/firefox-ios.xliff` — Translation drops "only collect what we need to provide" and "for everyone", asserting a different claim about data collection.
    - Current: `Mozilla sbírá jenom informace potřebné pro vylepšování Firefoxu.`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `Mozilla se snaží sbírat jen data, která potřebuje k poskytování a vylepšování Firefoxu pro všechny.`
    - The en-US says Mozilla "strives to only collect what we need to provide and improve Firefox for everyone"; the Czech states as fact that it collects only info needed for improvement, changing what the product asserts about its data practices.
- `Settings.TrackingProtection.ProtectionCellFooter` — `cs/firefox-ios.xliff` — "helps stop advertisers from tracking" rendered as the absolute "zabrání inzerentům sledovat" (will prevent advertisers from tracking).
    - Current: `zabrání inzerentům sledovat vás na internetu`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `pomáhá zabránit inzerentům ve sledování vašeho prohlížení`
    - The source only claims it "helps stop" tracking; the Czech makes an unqualified promise about the product's behaviour.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 54 |
| 3 | Degraded language (grammar, spelling, terminology) | 35 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Logins.DevicePasscodeRequired.Message.v122` — `cs/firefox-ios.xliff` — "passwords" is rendered as "přihlašovacích údajů" (login credentials) instead of "hesel".
    - Current: `Pro ukládání a automatické vyplňování přihlašovacích údajů`
    - Source: `To save and automatically fill passwords, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Pro ukládání a automatické vyplňování hesel`
    - The source says "To save and automatically fill passwords"; the Czech says login credentials, which is a different term than the passwords terminology used consistently elsewhere in this batch.
- `Menu.EnhancedTrackingProtection.Certificates.IssuerOrganization.v131` — `cs/firefox-ios.xliff` — "Organization" translated as "Společnost" (company).
    - Current: `Společnost`
    - Source: `Organization`
    - Suggest: `Organizace`
    - The certificate field is "Organization"; the Czech term for the certificate field is "Organizace", not "Společnost" (company), which narrows the meaning.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNamesDNSName.v131` — `cs/firefox-ios.xliff` — "DNS Name" translated as "Záznam DNS" (DNS record).
    - Current: `Záznam DNS`
    - Source: `DNS Name`
    - Suggest: `Název DNS`
    - The certificate field is the DNS name of the subject alt name, not a DNS record.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `cs/firefox-ios.xliff` — "Tracking content" translated as "Sledující obsah" (content that watches) instead of the established "Sledovací obsah".
    - Current: `Sledující obsah: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Sledovací obsah: %@`
    - Elsewhere in this screen the adjective is consistently "sledovací" (sledovací prvky, sledovací cookies); "sledující" is an inconsistent and incorrect rendering of the standard term.
- `Menu.EnhancedTrackingProtection.Details.TrackersStandardModeFooterText.v150` — `cs/firefox-ios.xliff` — "you may see" translated with an impersonal/wrong subject, making the browser rather than the user the one who sees the count.
    - Current: `Může proto zaznamenat vyšší počet sledovacích prvků.`
    - Source: `Standard blocks common trackers after a page starts loading, so you may see a higher tracker count. %@`
    - Suggest: `Můžete proto zaznamenat vyšší počet sledovacích prvků.`
    - Source says "so you may see a higher tracker count" — the subject is the user (2nd person plural), not the blocking level.
- `Menu.EnhancedTrackingProtection.Details.TrackersStrictModeFooterText.v150` — `cs/firefox-ios.xliff` — "you may see" translated with the wrong subject, attributing the observation to the mode instead of the user.
    - Current: `Může tedy zaznamenat nižší počet sledovacích prvků.`
    - Source: `Strict blocks more trackers by stopping them before a page loads, so you may see a lower tracker count. %@`
    - Suggest: `Můžete tedy zaznamenat nižší počet sledovacích prvků.`
    - Source says "so you may see a lower tracker count" — the subject is the user (2nd person plural).
- `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `cs/firefox-ios.xliff` — Translation drops "on this device" and changes the imperative to a third-person statement.
    - Current: `Nezanechá stopy`
    - Source: `Leave no traces on this device`
    - Suggest: `Nezanechávejte na tomto zařízení žádné stopy`
    - The en-US title "Leave no traces on this device" addresses the user and specifies the device; the Czech says "It leaves no traces" without the device scope.
- `CloseTab.ArrivingNotification.title.v133` — `cs/firefox-ios.xliff` — The notification title mistranslates "%1$@ tabs closed: %2$@" as "Firefox closed tabs", turning the app name into the subject of a verb and losing the count structure.
    - Current: `%1$@ zavřel panely: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `Panely zavřené v %1$@: %2$@`
    - In en-US "%1$@ tabs closed: %2$@" means the number of tabs (%2$@) closed in the app (%1$@); the Czech reads as "Firefox closed the tabs: 3", asserting the app performed the closing rather than reporting a count.
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `cs/firefox-ios.xliff` — "save actions" mistranslated as "ukládání akcí" (saving actions).
    - Current: `od anonymního prohlížení po ukládání akcí`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `od anonymního prohlížení po akce pro ukládání`
    - The source "from private browsing to save actions" refers to save-related actions in the menu, not to "saving actions".
- `MainMenu.Submenus.Tools.AccessibilityLabels.Zoom.Subtitle.v132` — `cs/firefox-ios.xliff` — "Zoom" (page zoom tool) is rendered as "Zvětšit okno" (enlarge window), which names the wrong thing and is inconsistent with the Zoom title string.
    - Current: `Zvětšit okno`
    - Source: `Zoom`
    - Suggest: `Zvětšení stránky`
    - The developer comment says this is the Zoom tool that applies zoom on a page; "okno" (window) is wrong and conflicts with the sibling string "Zvětšení stránky (%@)".
- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `cs/firefox-ios.xliff` — "Unselected" (state of a radio button) is rendered as "Výběr zrušen" ("selection cancelled"), an action rather than a state.
    - Current: `Výběr zrušen`
    - Source: `Unselected`
    - Suggest: `Nevybráno`
    - The accessibility label states that the survey option is not selected; the Czech announces that a selection was cancelled, which is a different meaning.
- `NativeErrorPage.BadCertDomain.ViewCertificateLink.v149` — `cs/firefox-ios.xliff` — "site's certificate" translated as "certifikát serveru" (server's certificate) while the surrounding strings use "stránka/web" for site.
    - Current: `Zobrazit certifikát serveru`
    - Source: `View the site’s certificate`
    - Suggest: `Zobrazit certifikát stránky`
    - The source says the site's certificate; other strings on the same page translate "site" as "stránka"/"web", making "serveru" inconsistent.
- `Onboarding.IntroDescriptionPart1.v114` — `cs/firefox-ios.xliff` — "For good" (meaning for the common good/benefit) is rendered as "Navždy" (forever).
    - Current: `Nezávislý. Neziskový. Navždy.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Nezávislý. Neziskový. Pro dobro všech.`
    - The en-US "For good" in this Mozilla context means "for the benefit of people", not "permanently"; the Czech says "Forever".
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `cs/firefox-ios.xliff` — %2$@ is the company name (Mozilla), but the Czech calls it "aplikace" (app).
    - Current: `s marketingovými partnery aplikace %2$@`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `s marketingovými partnery společnosti %2$@`
    - The developer comment states %2$@ is the company name (e.g. Mozilla); calling it an application is wrong.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `cs/firefox-ios.xliff` — The source clause "putting you in control" is dropped from the translation.
    - Current: `Vyberte si svůj oblíbený vzhled nebo si nechte %@ nastavit tak, aby odpovídalo vašemu zařízení.`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `Vyberte si svůj oblíbený vzhled nebo si nechte %@ nastavit tak, aby odpovídal vašemu zařízení – máte to plně pod kontrolou.`
    - en-US ends with "putting you in control", which has no equivalent in the Czech text.
- `Onboarding.Modern.Sync.Title.v145` — `cs/firefox-ios.xliff` — "on all your browsing adventures" is reduced to "za dobrodružstvím", dropping the browsing reference and the sense of taking the app along everywhere.
    - Current: `Vydejte se s aplikací %@ za dobrodružstvím`
    - Source: `Take %@ on all your browsing adventures`
    - Suggest: `Vezměte si aplikaci %@ na všechna svá dobrodružství při prohlížení webu`
    - Source: "Take %@ on all your browsing adventures"; the Czech omits "all" and "browsing".
- `Onboarding.Modern.TermsOfService.Description.v145` — `cs/firefox-ios.xliff` — "trusted for over 20 years" is rendered as "which you have trusted for over 20 years", asserting the user's trust rather than general trust.
    - Current: `Přináší nezisková organizace %@, které důvěřujete již více než 20 let`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Přináší nezisková organizace %@, které se důvěřuje již více než 20 let`
    - The source states the non-profit is trusted (generally, by people) for over 20 years; the Czech asserts that the reader personally has trusted it for over 20 years.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `cs/firefox-ios.xliff` — "Manage settings" is translated only as "Nastavení" (Settings), dropping the action verb.
    - Current: `Nastavení`
    - Source: `Manage settings`
    - Suggest: `Spravovat nastavení`
    - The source is the link label "Manage settings"; the Czech says merely "Settings", losing the manage action.
- `Onboarding.Wallpaper.Description.v114` — `cs/firefox-ios.xliff` — "speaks to you" mistranslated as "expresses you" with reversed subject relation.
    - Current: `Vyberte si tapetu, která vás vyjadřuje.`
    - Source: `Choose a wallpaper that speaks to you.`
    - Suggest: `Vyberte si tapetu, která vás zaujme.`
    - The source says the wallpaper appeals to/resonates with the user; the Czech says the wallpaper expresses the user, which is a different claim and reads oddly.
- `Onboarding.Welcome.Link.Action.v114` — `cs/firefox-ios.xliff` — "privacy notice" (singular document) rendered as plural "oznámeních" and inconsistent with the term used elsewhere.
    - Current: `v našich oznámeních o ochraně osobních údajů`
    - Source: `Learn more in our privacy notice`
    - Suggest: `v našich zásadách ochrany osobních údajů`
    - The source refers to one Privacy Notice document, translated elsewhere in the same file as "Zásady ochrany osobních údajů"; the plural "oznámeních" is both a wrong number and inconsistent terminology.
- `PrivacyDashboard.CrossSiteTrackers.v155` — `cs/firefox-ios.xliff` — "Cross-Site Tracking Cookies" translated as just "Sledovací cookies", dropping the cross-site aspect.
    - Current: `Sledovací cookies`
    - Source: `Cross-Site Tracking Cookies`
    - Suggest: `Sledovací cookies mezi servery`
    - The source specifies cross-site tracking cookies; the Czech omits the cross-site qualifier, which is the distinguishing category name in the tracker list.
- `CreditCard.Settings.EmptyListTitle.v122` — `cs/firefox-ios.xliff` — Plural "Cards" rendered as singular "platební kartu".
    - Current: `Uložit platební kartu do aplikace %@`
    - Source: `Save Cards to %@`
    - Suggest: `Uložit platební karty do aplikace %@`
    - en-US "Save Cards to %@" is plural; the Czech says save a single card.
- `Settings.AIControls.AIPoweredFeaturesSection.TranslationSection.Message.v151` — `cs/firefox-ios.xliff` — The translation shifts "on your device" from where translation happens to describing the translations themselves.
    - Current: `Překlady na vašem zařízení zůstanou soukromé.`
    - Source: `Translations stay private on your device.`
    - Suggest: `Překlady zůstanou soukromé na vašem zařízení.`
    - The source says translations stay private on your device (i.e. processing remains local); the Czech word order makes "na vašem zařízení" modify "Překlady" (translations on your device), losing the privacy-on-device claim.
- `Settings.Studies.Message.v148` — `cs/firefox-ios.xliff` — The Czech says the app tests "new" features and improves "its" quality for everyone, whereas the source says users are selected to test features, improving quality for everyone.
    - Current: `%@ náhodně vybírá uživatele, aby otestoval nové funkce, s cílem zlepšit jeho kvalitu pro všechny.`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `%@ náhodně vybírá uživatele, kteří testují funkce, což zlepšuje kvalitu pro všechny.`
    - In the source it is the selected users who test the features; the Czech singular "aby otestoval" attributes the testing to the app, adds "nové" (new), and "jeho kvalitu" narrows "quality for everyone" to the app's own quality.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `cs/firefox-ios.xliff` — "This page may be restricted" is rendered as a definite statement, losing the hedge "may".
    - Current: `Tato stránka je buď s omezením nebo se jedná převážně o vizuální stránku.`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `Tato stránka může být omezená nebo převážně vizuální.`
    - The en-US uses "may be"; the Czech asserts it as fact, and also misses a comma before "nebo" in the "buď … nebo" construction.
- `TabsTray.SyncTabs.SyncTabsButton.Title.v119` — `cs/firefox-ios.xliff` — "Sync Tabs" translated as just "Synchronizovat" (Synchronize), dropping the object "tabs".
    - Current: `Synchronizovat`
    - Source: `Sync Tabs`
    - Suggest: `Synchronizovat panely`
    - The source is "Sync Tabs"; the Czech omits "panely", making the button ambiguous about what is synced.
- `WebCompatReporter.Preview.Data.IsTablet.v155` — `cs/firefox-ios.xliff` — "Whether or not your device is a tablet" is rendered as "Regardless of whether your device is a tablet", changing the meaning.
    - Current: `Bez ohledu na to, zda je vaše zařízení tablet`
    - Source: `Whether or not your device is a tablet`
    - Suggest: `Zda je vaše zařízení tablet, či nikoliv`
    - The bullet lists what data is sent: whether the device is a tablet. "Bez ohledu na to" means "regardless of", which is not the source meaning and makes the list item nonsensical.
- `WebCompatReporter.SubOption.ImagesNotLoaded.v154` — `cs/firefox-ios.xliff` — "Images not loaded" is rendered as an ongoing "images are not loading" instead of the completed state.
    - Current: `Obrázky se nenačítají`
    - Source: `Images not loaded`
    - Suggest: `Obrázky se nenačetly`
    - The source states the images did not load (completed action); the Czech imperfective present says they are not loading, changing the aspect.
- `WebCompatReporter.SubOption.NoVideo.v154` — `cs/firefox-ios.xliff` — "There is no video" is translated as "Video is not displayed", changing the meaning.
    - Current: `Video se nezobrazuje`
    - Source: `There is no video`
    - Suggest: `Není zde žádné video`
    - The source says no video exists/no video track, parallel to "There is no audio" which was translated as "Není slyšet žádný zvuk"; the Czech instead claims the video fails to display.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `cs/firefox-ios.xliff` — "Try refreshing in a few minutes" is translated as reloading the page rather than refreshing the widget data.
    - Current: `Zkuste stránku za chvíli znovu načíst.`
    - Source: `Match info is not available right now. Try refreshing in a few minutes.`
    - Suggest: `Zkuste to za pár minut znovu načíst.`
    - The source refers to refreshing the widget's match data, not a page; the Czech adds "stránku" (the page), which the source never says.
- `WorldCup.HomepageWidget.RoundPhase.ScrollIndicatorAccessibilityLabel.v151` — `cs/firefox-ios.xliff` — Accessibility label says "scroll the page" although the scrolling applies to the widget's match list.
    - Current: `Posuňte stránku a podívejte se`
    - Source: `Scroll to see previous or next matches`
    - Suggest: `Posunutím zobrazíte`
    - The source says "Scroll to see previous or next matches"; "stránku" (the page) is not in the source and misdescribes the control.
- `WorldCup.HomepageWidget.RoundPhase.WinWorldCupLabel.v151` — `cs/firefox-ios.xliff` — "2026 WORLD CUP CHAMPIONS" is rendered as just "MISTROVSTVÍ SVĚTA 2026" (World Cup 2026), losing the "champions" meaning.
    - Current: `MISTROVSTVÍ SVĚTA 2026`
    - Source: `2026 WORLD CUP CHAMPIONS`
    - Suggest: `MISTŘI SVĚTA 2026`
    - The source labels the championship winner; the Czech only names the tournament, not the champions.
- `This action will clear all of your private data, including history from your synced devices.` — `cs/firefox-ios.xliff` — "all of your private data" is rendered as "všechna vaše data", dropping "private"/soukromá.
    - Current: `Tato akce smaže všechna vaše data, včetně historie prohlížení ze všech synchronizovaných zařízení.`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `Tato akce smaže všechna vaše soukromá data, včetně historie prohlížení ze synchronizovaných zařízení.`
    - The source says "all of your private data"; the Czech says "all your data", which overstates what will be deleted (and the sibling string in ClearPrivateDataConfirm correctly uses "soukromá data").
- `Offline Website Data` — `cs/firefox-ios.xliff` — "Offline Website Data" rendered as "Offline obsah" (offline content), losing "website data".
    - Current: `Offline obsah`
    - Source: `Offline Website Data`
    - Suggest: `Offline data stránek`
    - The source and developer comment refer to website data stored offline, not generic offline content.
- `DefaultBrowserCard.Button.v2` — `cs/firefox-ios.xliff` — "Learn How" translated as "Zjistit více" (Learn more).
    - Current: `Zjistit více`
    - Source: `Learn How`
    - Suggest: `Zjistit jak`
    - The developer comment says the button teaches the user how to set the default browser; "Zjistit více" corresponds to "Learn more", a different string.
- `DefaultBrowserCard.Description` — `cs/firefox-ios.xliff` — Translation says links, e-mails and messages will open in Firefox, instead of links from websites, e-mails and Messages.
    - Current: `Nastavte si automatické otevírání odkazů, e-mailů a zpráv ve Firefoxu.`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `Nastavte si, aby se odkazy z webových stránek, e-mailů a Zpráv automaticky otevíraly ve Firefoxu.`
    - The source is "Set links from websites, emails, and Messages to open automatically in Firefox" — the lists are sources of links, not items opened in Firefox.
- `LibraryPanel.History.AllTimeOption.v138` — `cs/firefox-ios.xliff` — "All Time" (time range option for clearing history) is rendered as "Po celý čas" ("for the whole time"), not the standard Czech time-range label.
    - Current: `Po celý čas`
    - Source: `All Time`
    - Suggest: `Vše`
    - The option sits alongside "Poslední hodina", "Posledních 24 hodin" etc. and means the entire history range; "Po celý čas" is an adverbial phrase that does not read as a range option.
- `Firefox.HomePage.Title` — `cs/firefox-ios.xliff` — "Firefox Home Page" translated as just "Výchozí", losing the meaning and the brand name.
    - Current: `Výchozí`
    - Source: `Firefox Home Page`
    - Suggest: `Domovská stránka Firefoxu`
    - The source names the Firefox home page shown in the tab history list; "Výchozí" means "Default" and does not convey a home page nor the product name.
- `FirefoxHomepage.JumpBackIn.TabPickup.OpenTab.A11y.v106` — `cs/firefox-ios.xliff` — Singular "synced tab" rendered as plural "synchronizované panely".
    - Current: `Otevřít synchronizované panely`
    - Source: `Open synced tab`
    - Suggest: `Otevřít synchronizovaný panel`
    - The source is "Open synced tab" — an accessibility action that opens the one synced tab shown in the cell, not all synced tabs.
- `FirefoxHomepage.JumpBackIn.TabPickup.ShowAll.ButtonTitle.v104` — `cs/firefox-ios.xliff` — "See all synced tabs" drops "all".
    - Current: `Zobrazit synchronizované panely`
    - Source: `See all synced tabs`
    - Suggest: `Zobrazit všechny synchronizované panely`
    - The source explicitly says "See all synced tabs"; the Czech omits "all", which is the distinguishing part of this button.
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `cs/firefox-ios.xliff` — Accessibility label adds an invented instruction and mangles the subject.
    - Current: `Logo Firefox - klepnutím změní tapetu.`
    - Source: `Firefox logo, change the wallpaper.`
    - Suggest: `Logo Firefoxu, změnit tapetu.`
    - The source is "Firefox logo, change the wallpaper." — a simple VoiceOver label; the Czech adds "klepnutím" (by tapping) and uses a third-person verb with no subject, which is both ungrammatical and content the source never stated.
- `LibraryPanel.History.ClearHistoryMenuTitle.v100` — `cs/firefox-ios.xliff` — "other browsing data" translated as "související data" (related data), losing the meaning of browsing data.
    - Current: `cookies a související data`
    - Source: `Removes history (including history synced from other devices), cookies and other browsing data.`
    - Suggest: `cookies a další data o prohlížení`
    - The en-US says "cookies and other browsing data"; "související data" means "related data", which is not what the source says.
- `Logins.PasscodeRequirement.Warning` — `cs/firefox-ios.xliff` — The brand name Firefox is dropped from the warning message.
    - Current: `Pro používání funkce automatického vyplňování si na svém zařízení nastavte kód zámku.`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `Pro používání funkce automatického vyplňování ve Firefoxu si na svém zařízení nastavte kód zámku.`
    - The source specifies "the AutoFill feature for Firefox"; the Czech omits the product name, making the statement apply to AutoFill in general.
- `LoginsList.NoMatchingResult.Subtitle` — `cs/firefox-ios.xliff` — Translation adds "přihlašovací údaje" (logins), while the source says generically "no results".
    - Current: `Vašemu vyhledávání neodpovídají žádné přihlašovací údaje.`
    - Source: `There are no results matching your search.`
    - Suggest: `Vašemu vyhledávání neodpovídají žádné výsledky.`
    - en-US: "There are no results matching your search." — the Czech narrows "results" to "logins".
- `Menu.AddToShortcuts.v99` — `cs/firefox-ios.xliff` — "Add to Shortcuts" translated as "Přidat zkratku" (Add a shortcut) instead of "Přidat do zkratek".
    - Current: `Přidat zkratku`
    - Source: `Add to Shortcuts`
    - Suggest: `Přidat do zkratek`
    - The source says add the current site to Shortcuts; the confirmation toast uses "Přidáno do zkratek", so the action label should match.
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `cs/firefox-ios.xliff` — "Cross-Site Trackers" is rendered as the generic "Sledovací prvky" (trackers), losing the cross-site distinction and colliding with other tracker categories on the same panel.
    - Current: `Sledovací prvky`
    - Source: `Cross-Site Trackers`
    - Suggest: `Sledovací prvky mezi weby`
    - The en-US title specifies cross-site trackers; the Czech says only "trackers", which is ambiguous next to the other tracker categories (social, content) on the same tracking protection screen.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `cs/firefox-ios.xliff` — The translation drops "secretly" and the energy-bill consequence from the cryptominer description.
    - Current: `Těžba kryptoměn využívá výpočetní výkon vašeho zařízení k získávání digitálních měn. Běžící skripty vybíjí vaši baterii a vaše zařízení zpomalují.`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Těžaři kryptoměn tajně využívají výpočetní výkon vašeho zařízení k získávání digitálních měn. Těžební skripty vybíjí vaši baterii, zpomalují vaše zařízení a mohou zvýšit váš účet za elektřinu.`
    - en-US says cryptominers "secretly use" the computing power and that scripts "can increase your energy bill"; both elements are missing in Czech.
- `Send Feedback` — `cs/firefox-ios.xliff` — "Send Feedback" translated as "Odeslat hodnocení" (send a rating/review) instead of feedback.
    - Current: `Odeslat hodnocení`
    - Source: `Send Feedback`
    - Suggest: `Odeslat zpětnou vazbu`
    - The menu item opens a feedback submission page; "hodnocení" means rating/review, not feedback.
- `Settings.Home.Option.Wallpaper.Accessibility.ToggleButton` — `cs/firefox-ios.xliff` — The "wallpaper cycle" aspect of the toggle is dropped, so the label describes a generic wallpaper switch.
    - Current: `Přepínač tapety domovské stránky`
    - Source: `Homepage wallpaper cycle toggle`
    - Suggest: `Přepínač střídání tapet na domovské stránce`
    - Source is "Homepage wallpaper cycle toggle" — the toggle controls cycling through wallpapers, not the wallpaper itself.
- `Settings.NewTab.Option.FirefoxHome` — `cs/firefox-ios.xliff` — "Firefox Home" is rendered as "Výchozí domovskou stránku" (default homepage), dropping the Firefox brand name and conflicting with the separate "Homepage" option.
    - Current: `Výchozí domovskou stránku`
    - Source: `Firefox Home`
    - Suggest: `Domovskou stránku Firefoxu`
    - The source names the Firefox Home page; the brand must be kept and the option is distinct from the user-set "Homepage" option in the same screen.
- `Settings.Passwords.OnboardingMessage.v103` — `cs/firefox-ios.xliff` — "are now protected" loses "now"; minor but the sentence also drops "device" from "device passcode".
    - Current: `Vaše hesla jsou chráněná pomocí Face ID, Touch ID nebo kódu zámku.`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `Vaše hesla jsou nyní chráněná pomocí Face ID, Touch ID nebo kódu zámku zařízení.`
    - The source specifies "now" and "a device passcode"; both qualifiers are omitted.
- `Settings.SendUsage.Message` — `cs/firefox-ios.xliff` — Translation drops "only collect what we need to provide" and "for everyone", asserting a different claim about data collection.
    - Current: `Mozilla sbírá jenom informace potřebné pro vylepšování Firefoxu.`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `Mozilla se snaží sbírat jen data, která potřebuje k poskytování a vylepšování Firefoxu pro všechny.`
    - The en-US says Mozilla "strives to only collect what we need to provide and improve Firefox for everyone"; the Czech states as fact that it collects only info needed for improvement, changing what the product asserts about its data practices.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `cs/firefox-ios.xliff` — "haven't viewed" rendered as "neotevřeli" (haven't opened) instead of "nezobrazili/neprohlíželi".
    - Current: `které jste dva týdny neotevřeli`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `které jste si dva týdny nezobrazili`
    - Source says tabs you haven't viewed for two weeks; "neotevřeli" means not opened, which is a different condition (a tab can be open but not viewed).
- `Settings.TrackingProtection.ProtectionCellFooter` — `cs/firefox-ios.xliff` — "helps stop advertisers from tracking" rendered as the absolute "zabrání inzerentům sledovat" (will prevent advertisers from tracking).
    - Current: `zabrání inzerentům sledovat vás na internetu`
    - Source: `Reduces targeted ads and helps stop advertisers from tracking your browsing.`
    - Suggest: `pomáhá zabránit inzerentům ve sledování vašeho prohlížení`
    - The source only claims it "helps stop" tracking; the Czech makes an unqualified promise about the product's behaviour.
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `cs/firefox-ios.xliff` — "some ad tracking" translated as "některé sledující reklamy" (some tracking ads).
    - Current: `Povoluje některé sledující reklamy pro správné fungování stránek.`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Povoluje část sledování reklamami, aby stránky fungovaly správně.`
    - The source allows some ad tracking (the tracking activity), not certain ads themselves.
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `cs/firefox-ios.xliff` — "Pages load faster, but some functionality may not work" mistranslated as "Zrychlí i načítání stránek, ale může omezit jejich fungování".
    - Current: `Zrychlí i načítání stránek, ale může omezit jejich fungování.`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `Stránky se načítají rychleji, ale některé funkce nemusí fungovat.`
    - The source says some functionality may not work; the Czech asserts the protection will limit page functioning, and adds "i" which the source does not have.
- `Settings.WebsiteData.SelectedConfirmPrompt` — `cs/firefox-ios.xliff` — "the selected items" rendered as "všechny vybrané položky" (all selected items), adding "all".
    - Current: `Tato akce smaže všechny vybrané položky`
    - Source: `This action will clear the selected items. It cannot be undone.`
    - Suggest: `Tato akce smaže vybrané položky`
    - Source says "the selected items"; the added "všechny" changes the scope of the confirmation dialog.
- `Tabs Tray` — `cs/firefox-ios.xliff` — "Tabs Tray" translated as "Lišta panelů" (tab bar) instead of the tab overview/panel grid.
    - Current: `Lišta panelů`
    - Source: `Tabs Tray`
    - Suggest: `Přehled panelů`
    - The accessibility label refers to the Tabs Tray view (the grid of open tabs), not a toolbar/bar; "lišta" names a different UI element.
- `UIMenuItem.SearchWithFirefox` — `cs/firefox-ios.xliff` — "Search with Firefox" is rendered only as "Vyhledat", dropping the Firefox brand name.
    - Current: `Vyhledat`
    - Source: `Search with Firefox`
    - Suggest: `Vyhledat pomocí Firefoxu`
    - The source names the product performing the search; the Czech omits it entirely.
- `You don’t have any tabs open in Firefox on your other devices.` — `cs/firefox-ios.xliff` — The Firefox brand reference is dropped from the message.
    - Current: `Ve vašich zařízeních nejsou otevřené žádné panely.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `Na vašich dalších zařízeních nemáte ve Firefoxu otevřené žádné panely.`
    - Source says "in Firefox on your other devices"; the Czech omits both "in Firefox" and "other".
- _…and 7 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `Engagement.Notification.Title.v112` — `cs/firefox-ios.xliff` — Imperative rendered as indicative future tense.
    - Current: `Začnete své první vyhledávání`
    - Source: `Start your first search`
    - Suggest: `Začněte své první vyhledávání`
    - The source "Start your first search" is an imperative call to action; "Začnete" is the 2nd person future indicative ("you will start"), not the imperative "Začněte". Other notifications in the same file use imperatives (Prohlížejte, Vyzkoušejte).
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `cs/firefox-ios.xliff` — Mismatched verb forms: a finite verb coordinated with an infinitive.
    - Current: `Souhlasím a pokračovat`
    - Source: `Agree and continue`
    - Suggest: `Souhlasit a pokračovat`
    - "Souhlasím" (1st person) and "pokračovat" (infinitive) cannot be coordinated; the button label should use consistent forms for "Agree and continue".
- `CreditCard.SnackBar.UpdatedCardLabel.v122` — `cs/firefox-ios.xliff` — Agreement error: "Informace" (plural) with singular verb form "byla aktualizována".
    - Current: `Informace o kartě byla aktualizována`
    - Source: `Card Information Updated`
    - Suggest: `Informace o kartě byly aktualizovány`
    - "Card Information Updated"; in Czech "informace" here is plural and requires "byly aktualizovány".
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v134` — `cs/firefox-ios.xliff` — "Odeslané" should be "Odesláno" as in the parallel v137 string.
    - Current: `%1$@ Odeslané z aplikace %2$@`
    - Source: `%1$@ Sent from %2$@ 🦊 %3$@`
    - Suggest: `%1$@ Odesláno z aplikace %2$@`
    - The other variants of the same message use the correct impersonal form "Odesláno z aplikace"; "Odeslané" is an inconsistent, ungrammatical form here.
- `ContextualHints.Summarize.Description.v142` — `cs/firefox-ios.xliff` — Awkward repetition "zobrazíte zobrazení čtečky" for "Touch and hold for Reader View".
    - Current: `Klepnutím a podržením zobrazíte zobrazení čtečky.`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `Klepnutím a podržením zobrazíte čtečku.`
    - The Czech repeats the stem "zobrazíte zobrazení", a clumsy duplication; the source simply says "Touch and hold for Reader View".
- `CreditCard.RememberCard.SecondaryButtonTitle.v116` — `cs/firefox-ios.xliff` — Subject-verb agreement error: "Informace" (plural) with singular verb form "byla aktualizována".
    - Current: `Informace o kartě byla aktualizována`
    - Source: `Card Information Updated`
    - Suggest: `Informace o kartě byly aktualizovány`
    - "Card Information Updated" – Czech "informace" here is plural and requires "byly aktualizovány"; as written it mixes plural noun with singular predicate.
- `ReaderMode.Available.VoiceOverAnnouncement` — `cs/firefox-ios.xliff` — Gender agreement error: adjective "dostupný" does not agree with neuter noun "Zobrazení".
    - Current: `Je dostupný Zobrazení čtečky`
    - Source: `Reader Mode available`
    - Suggest: `Zobrazení čtečky je dostupné`
    - "Zobrazení" is neuter, so the predicate adjective must be "dostupné"; the current form is ungrammatical.
- `Tabs %@ to %@ of %@` — `cs/firefox-ios.xliff` — Plural noun rendered as singular in the tab range announcement.
    - Current: `Panel %1$@ až %2$@ ze %3$@`
    - Source: `Tabs %1$@ to %2$@ of %3$@`
    - Suggest: `Panely %1$@ až %2$@ z %3$@`
    - Source is "Tabs %1$@ to %2$@ of %3$@" (a range, plural); the Czech uses the singular "Panel", inconsistent with the other tab-range strings.
- `Well, this is embarrassing.` — `cs/firefox-ios.xliff` — "Ale toto je nepříjemné." is an awkward, ungrammatical-sounding rendering of the idiom.
    - Current: `Ale toto je nepříjemné.`
    - Source: `Well, this is embarrassing.`
    - Suggest: `To je ale trapné.`
    - The Czech word order with "Ale toto" is not idiomatic for the English interjection "Well, this is embarrassing."

### D. Terminology, register & consistency

- `CloseTab.ViewAction.title.v133` — `cs/firefox-ios.xliff` — Action label translated as a noun phrase ("Zobrazení") instead of an imperative/verb as required for an action button.
    - Current: `Zobrazení nedávno zavřených panelů`
    - Source: `View recently closed tabs`
    - Suggest: `Zobrazit nedávno zavřené panely`
    - The comment says this is a label for an action used to view recently closed tabs; "Zobrazení" is the noun "viewing", not the action "View".
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `cs/firefox-ios.xliff` — "your top sites" translated with the anglicism "top stránky".
    - Current: `své top stránky`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `své nejnavštěvovanější stránky`
    - "Top Sites" is rendered elsewhere in Czech Firefox as "Nejnavštěvovanější stránky"; "top stránky" is an inconsistent, colloquial rendering.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v140` — `cs/firefox-ios.xliff` — "Top" as a toolbar position is translated with the directional "Nahoru" instead of the locative "Nahoře", inconsistent with the paired "Dole" and with the v145 string.
    - Current: `Nahoru`
    - Source: `Top`
    - Suggest: `Nahoře`
    - The option describes where the toolbar is placed (position), paired with "Dole"; the v145 equivalent correctly uses "Nahoře".
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendCrashReportsDescription.v140` — `cs/firefox-ios.xliff` — "crash reports" is translated as "hlášení o selhání" here but "hlášení o pádech" in the title on the same screen.
    - Current: `Hlášení o selhání nám umožňují`
    - Source: `Crash reports allow us to diagnose and fix issues with the browser. %@`
    - Suggest: `Hlášení o pádech nám umožňují`
    - The same term must be consistent within the Manage Privacy Preferences screen; the switch title uses "hlášení o pádech".
- `Onboarding.TermsOfService.PrivacyPreferences.SendCrashReportsTitle.v135` — `cs/firefox-ios.xliff` — "crash reports" translated inconsistently within the same screen ("hlášení o pádech" vs "hlášení o selhání").
    - Current: `Automaticky odesílat hlášení o pádech`
    - Source: `Automatically send crash reports`
    - Suggest: `Automaticky odesílat hlášení o selhání`
    - The description string for the same switch uses "Hlášení o selhání"; the title uses "hlášení o pádech" for the same source term on the same screen.
- `PrimaryButton.Label.v112` — `cs/firefox-ios.xliff` — "survey" rendered as "průzkum" on the button but as "dotazník" in the body text on the same popup.
    - Current: `Vyplnit průzkum`
    - Source: `Take Survey`
    - Suggest: `Vyplnit dotazník`
    - Same source term "survey" is translated inconsistently within one screen (Body.Text.v112 uses "dotazníku").
- `Settings.Appearance.NavigationToolbar.SectionHeader.v145` — `cs/firefox-ios.xliff` — "Toolbar" is rendered as "nástrojová lišta" here but as "panel nástrojů" in the accompanying description on the same screen.
    - Current: `Tlačítko na nástrojové liště`
    - Source: `Toolbar Button`
    - Suggest: `Tlačítko na panelu nástrojů`
    - Settings.Appearance.NavigationToolbar.Description.v145 uses "panelu nástrojů" for the same source term "toolbar"; the section header and its description must be consistent.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `cs/firefox-ios.xliff` — "Terms of Use" rendered as "Podmínkami používání", inconsistent with "Podmínky použití" used elsewhere in the same file, and "sheet" rendered as "Přehled".
    - Current: `Přehled s Podmínkami používání byl otevřen`
    - Source: `Terms of Use sheet opened`
    - Suggest: `Panel s Podmínkami použití byl otevřen`
    - Other strings in this file use "Podmínky použití"; "sheet" is not an overview ("Přehled").
- `Menu.ZoomPage.CurrentZoomLevel.AccessibilityLabel.v113` — `cs/firefox-ios.xliff` — "Zoom Level" is rendered as "velikost stránky" here but as "úroveň přiblížení" in the sibling strings of the same panel.
    - Current: `Aktuální velikost stránky: %@`
    - Source: `Current Zoom Level: %@`
    - Suggest: `Aktuální úroveň přiblížení: %@`
    - Inconsistent terminology for the same source term within one screen (compare Increase/Decrease Zoom Level strings).
- `Enter passcode` — `cs/firefox-ios.xliff` — "passcode" translated as "heslo" (password) instead of the device passcode term.
    - Current: `Zadejte heslo`
    - Source: `Enter passcode`
    - Suggest: `Zadejte kód`
    - The string refers to the app/device passcode, not a password; using "heslo" conflicts with password terminology used elsewhere (e.g. saved passwords).
- `Menu.Passwords.Label` — `cs/firefox-ios.xliff` — "Passwords" is rendered as "Přihlašovací údaje" (logins/credentials) while other strings in the same batch translate "password" as "heslo".
    - Current: `Přihlašovací údaje`
    - Source: `Passwords`
    - Suggest: `Hesla`
    - The source term is "Passwords"; nearby strings (Logins.WelcomeView.Title2, LoginsList.SelectPassword.Title) use "hesla", so this menu entry is inconsistent with the password terminology.
- `Settings.Home.Option.StartAtHome.Title` — `cs/firefox-ios.xliff` — "Opening screen" section title rendered as a verb phrase inconsistent with the related section header translated as "ÚVODNÍ OBRAZOVKA".
    - Current: `Po otevření aplikace zobrazit`
    - Source: `Opening screen`
    - Suggest: `Úvodní obrazovka`
    - The same source term "Opening screen" is translated as "ÚVODNÍ OBRAZOVKA" in Settings.Home.Option.Wallpaper.CollectionTitle, creating an inconsistency for the same setting title.
- `TodayWidget.PrivateTabButtonLabelV1` — `cs/firefox-ios.xliff` — "Private" rendered as "Soukromé" instead of the established "anonymní".
    - Current: `Soukromé vyhledávání`
    - Source: `Private Search`
    - Suggest: `Anonymní vyhledávání`
    - All other strings in this group translate "private" as "anonymní" (Zavřít anonymní panely, Vyhledat v anonymním panelu); this one is inconsistent.

### E. Typography, punctuation & spacing

- `Bookmarks.Menu.DeletedBookmark.v131` — `cs/firefox-ios.xliff` — Uses straight/English curly quotes instead of the Czech german-double quotes used elsewhere in the file.
    - Current: `Smazáno “%@”`
    - Source: `Deleted “%@”`
    - Suggest: `Smazáno „%@“`
    - The cs convention is german-double quotes („ “), as used in Bookmarks.Menu.SavedBookmarkToastLabel.v136 in the same file.
- `ContextualHints.FeltDeletion.Body.v122` — `cs/firefox-ios.xliff` — Em dash of the source replaced with a hyphen.
    - Current: `soubory cookie - všechno`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `soubory cookie – všechno`
    - The source uses a dash (—); a plain hyphen with spaces is not a valid dash in Czech typography.
- `LiveActivity.Downloads.FileNameText.v138` — `cs/firefox-ios.xliff` — Straight/English-style quotes used instead of the Czech german-double quotes.
    - Current: `Stahuje se “%@”`
    - Source: `Downloading “%@”`
    - Suggest: `Stahuje se „%@“`
    - The locale convention is german-double quotes; the current string uses “ ” (English opening/closing pair).
- `TopSites.RemovePage.Button` — `cs/firefox-ios.xliff` — Em dash from the source replaced with a hyphen.
    - Current: `Odebrat stránku - %@`
    - Source: `Remove page — %@`
    - Suggest: `Odebrat stránku — %@`
    - The en-US string uses an em dash "Remove page — %@"; a plain hyphen surrounded by spaces is not correct Czech typography.
- `When Leaving Private Browsing` — `cs/firefox-ios.xliff` — Setting label starts with a lowercase letter where the source is a capitalized label.
    - Current: `po opuštění anonymního prohlížení`
    - Source: `When Leaving Private Browsing`
    - Suggest: `Po opuštění anonymního prohlížení`
    - Displayed in Settings as a label under 'Close Private Tabs'; sentence-initial capitalization is expected.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/cs/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
