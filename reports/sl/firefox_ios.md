# Firefox iOS l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `e8592a898dc1` |
| **Previous run** | 2026-09-07 @ `386c3ca4eca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 1,903 of 1,919 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [android](android.md) · [firefox](firefox.md)

---

## Changes in this run

### 🆕 New findings (87)

- `NSLocationWhenInUseUsageDescription` — `sl/firefox-ios.xliff` — "Websites you visit" is rendered as just "Spletne strani", dropping "you visit".
    - Current: `Spletne strani lahko zahtevajo vašo lokacijo.`
    - Source: `Websites you visit may request your location.`
    - Suggest: `Spletne strani, ki jih obiščete, lahko zahtevajo vašo lokacijo.`
    - The en-US limits the claim to websites the user visits; the translation drops that qualifier.
- `Enter passcode` — `sl/firefox-ios.xliff` — "passcode" translated as "geslo" (password) instead of a passcode term.
    - Current: `Vnesite geslo`
    - Source: `Enter passcode`
    - Suggest: `Vnesite geslo za dostop`
    - In this file "password" and "passcode" are distinct; "geslo" is the established rendering of "password", making the passcode/password distinction disappear.
- `Offline Website Data` — `sl/firefox-ios.xliff` — "Offline Website Data" translated as "Podatke pri delu brez povezave", dropping "Website".
    - Current: `Podatke pri delu brez povezave`
    - Source: `Offline Website Data`
    - Suggest: `Podatke spletnih strani brez povezave`
    - The source names data stored by websites for offline use; the translation says only "data when working offline", losing the website reference.
- `Scan QR Code` — `sl/firefox-ios.xliff` — QR code term inconsistent with "kode QR" used in NSCameraUsageDescription.
    - Current: `Skeniraj QR-kodo`
    - Source: `Scan QR Code`
    - Suggest: `Skeniraj kodo QR`
    - The same source term "QR code" is rendered "kode QR" elsewhere in the same file; one form should be used.
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `sl/firefox-ios.xliff` — "blocks" trackers translated as "zavrne" (rejects/declines) instead of "blokira/zablokira".
    - Current: `Firefox vsak mesec zavrne povprečno več kot 3000 sledilcev na uporabnika.`
    - Source: `Firefox blocks 3,000+ trackers per user each month on average. Make us your default browser for privacy peace of mind.`
    - Suggest: `Firefox vsak mesec blokira povprečno več kot 3000 sledilcev na uporabnika.`
    - The product's established term for blocking trackers is "blokira"; "zavrne" describes a different action.
- `ErrorPages.CertWarning.Title` — `sl/firefox-ios.xliff` — Title says "Your connection is not private" instead of "This Connection is Untrusted".
    - Current: `Vaša povezava ni zasebna`
    - Source: `This Connection is Untrusted`
    - Suggest: `Ta povezava ni zaupanja vredna`
    - The en-US says the connection is untrusted; the Slovenian asserts it is not private, a different claim.
- `FxA.FirefoxAccount` — `sl/firefox-ios.xliff` — "Firefox Račun" uses English word order; Slovenian requires "Račun Firefox".
    - Current: `Firefox Račun`
    - Source: `Firefox Account`
    - Suggest: `Račun Firefox`
    - Slovenian noun phrase order places the brand after the noun; also the common noun should not be capitalized mid-phrase.
- `FirefoxHome.Stories.Minutes.v140` — `sl/firefox-ios.xliff` — "minut" is not abbreviated although the comment requires an abbreviation due to space constraints.
    - Current: `minut: %d`
    - Source: `min: %d`
    - Suggest: `min: %d`
    - Developer comment states minutes should be abbreviated due to space constraints; the source uses "min".
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `sl/firefox-ios.xliff` — Misspelling of "Logotip" as "Logtip".
    - Current: `Logtip Firefoxa`
    - Source: `Firefox logo, change the wallpaper.`
    - Suggest: `Logotip Firefoxa`
    - The Slovenian word for "logo" is "logotip"; "Logtip" is a typo.
- `Hotkeys.Forward.DiscoveryTitle` — `sl/firefox-ios.xliff` — Ambiguous/wrong rendering: source "Forward" refers to navigating forward in session history, and the translation reads as "Next"; however per the comment context it should be navigation forward.
    - Current: `Naprej`
    - Source: `Forward`
    - Suggest: `Naprej (po zgodovini)`
    - The paired Back shortcut is "Nazaj"; "Naprej" is acceptable but the developer comment describes switching to a subsequent tab. Low-risk ambiguity.
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `sl/firefox-ios.xliff` — "Cross-Site Trackers" is rendered as "Spletni sledilci" (web trackers), losing the cross-site meaning.
    - Current: `Spletni sledilci`
    - Source: `Cross-Site Trackers`
    - Suggest: `Sledilci med spletnimi mesti`
    - The source specifies trackers that follow users across sites; "Spletni sledilci" just means "web trackers" and does not convey "cross-site".
- `Menu.TrackingProtectionDescription.ContentTrackers` — `sl/firefox-ios.xliff` — Translation drops "outside" ads and omits "login fields" from the list of things that might not work.
    - Current: `vendar nekateri gumbi in obrazci morda ne bodo delovali`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `vendar nekateri gumbi, obrazci in prijavna polja morda ne bodo delovali`
    - The en-US lists "buttons, forms, and login fields"; the Slovenian omits login fields.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `sl/firefox-ios.xliff` — "secretly use your system's computing power" loses "secretly", and "increase your energy bill" is rendered with the colloquial "zasolijo račun".
    - Current: `Kriptorudarji izrabljajo zmogljivost vašega računalnika za rudarjenje digitalnega denarja.`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Kriptorudarji na skrivaj izrabljajo računsko zmogljivost vašega sistema za rudarjenje digitalnega denarja.`
    - The source says cryptominers "secretly use your system’s computing power"; the omission of "secretly" drops meaning.
- `Menu.Share.v99` — `sl/firefox-ios.xliff` — "Share" translated as "Deli" (divide/share in the arithmetic sense) instead of the established "Deli z drugimi"/"Souporaba".
    - Current: `Deli`
    - Source: `Share`
    - Suggest: `Deli z drugimi`
    - In Mozilla sl terminology the share action is "Deli z drugimi"; bare "Deli" reads as the imperative of "divide".
- `Search.ThirdPartyEngines.AddMessage` — `sl/firefox-ios.xliff` — Typo: "isklanik" should be "iskalnik".
    - Current: `Novi isklanik se bo pojavil v vrstici za hitro iskanje.`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `Novi iskalnik se bo pojavil v vrstici za hitro iskanje.`
    - The Slovenian word for "search engine" is "iskalnik"; the letters are transposed.
- `ScanQRCode.PermissionError.Message.v100` — `sl/firefox-ios.xliff` — The instruction to go to the device settings is reduced to "Izberite" (Select), dropping "device".
    - Current: `Izberite "Nastavitve" > "Firefox".`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Pojdite v "Nastavitve" naprave > "Firefox".`
    - en-US says "Go to device ‘Settings’ > ‘Firefox’"; the reference to the device's Settings app is lost.
- `SentTab_TabArrivingNotification_WithDevice_title` — `sl/firefox-ios.xliff` — Wrong preposition/case for device name: "z %@" should be "iz naprave %@" or "z naprave %@" — but here the source says "from %@" meaning received from a device.
    - Current: `Zavihek prejet z %@`
    - Source: `Tab received from %@`
    - Suggest: `Zavihek prejet iz %@`
    - The placeholder holds a device name; "prejet z %@" is ungrammatical/ambiguous, standard Slovenian uses "iz" for origin from a device.
- `SendTo.NotSignedIn.Title` — `sl/firefox-ios.xliff` — Incorrect case and unnecessary possessive pronoun; also "Firefox Račun" should not be capitalized mid-phrase as two nouns.
    - Current: `Niste prijavljeni v vaš Firefox Račun.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `Niste prijavljeni v svoj račun Firefox.`
    - Slovenian requires the reflexive possessive "svoj", and the noun order/capitalization "Firefox Račun" is a calque of English; correct form is "račun Firefox".
- `SendTo.NoDevicesFound.Message` — `sl/firefox-ios.xliff` — "Firefox Računom" uses English-style capitalization and word order for "Firefox Account".
    - Current: `S tem Firefox Računom`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `S tem računom Firefox`
    - In Slovenian the generic noun is lowercase and follows the brand name: "račun Firefox".
- `Settings.ClearAllWebsiteData.Clear.Button` — `sl/firefox-ios.xliff` — "all website data" rendered with a singular noun phrase, so it reads "all data of the website".
    - Current: `Izbriši vse podatke spletne strani`
    - Source: `Clear All Website Data`
    - Suggest: `Izbriši vse podatke spletnih strani`
    - The source clears data for all websites; the singular genitive "spletne strani" restricts it to one site.
- `Settings.FxA.Title` — `sl/firefox-ios.xliff` — Brand-plus-noun compound needs Slovenian possessive form and lowercase noun.
    - Current: `Firefox Račun`
    - Source: `Firefox Account`
    - Suggest: `Firefoxov račun`
    - "Firefox Račun" is an ungrammatical calque of English title case; Slovenian requires "Firefoxov račun" (cf. "Firefoxova domača stran" used elsewhere in this batch).
- `Settings.BlockOpeningExternalApps.Title` — `sl/firefox-ios.xliff` — "Block" translated as "Zavrni" (reject/decline) instead of "Prepreči"/"Blokiraj".
    - Current: `Zavrni odpiranje zunanjih aplikacij`
    - Source: `Block Opening External Apps`
    - Suggest: `Prepreči odpiranje zunanjih aplikacij`
    - The setting blocks external apps from opening; "zavrni" implies a one-time refusal rather than a persistent block.
- `Settings.NoImageModeBlockImages.Label.v99` — `sl/firefox-ios.xliff` — "Block Images" translated as "Zavračaj slike" (reject images) instead of "Zavrni/Blokiraj slike".
    - Current: `Zavračaj slike`
    - Source: `Block Images`
    - Suggest: `Blokiraj slike`
    - The source means blocking images from loading; "zavračaj" (reject) is not the established term for blocking content in Firefox sl, which uses "blokiraj".
- `Settings.Siri.SectionDescription` — `sl/firefox-ios.xliff` — "Siri shortcuts" rendered as just "bližnjice", dropping Siri from the phrase.
    - Current: `Uporabi bližnjice za hitro odpiranje Firefoxa s Siri`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Uporabite bližnjice Siri za hitro odpiranje Firefoxa s Siri`
    - The source says "Use Siri shortcuts…"; the translation omits "Siri" as the qualifier of shortcuts.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `sl/firefox-ios.xliff` — "haven't viewed" is rendered as "niste odprli" (haven't opened) — different action.
    - Current: `ki jih dva tedna niste odprli`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `ki si jih dva tedna niste ogledali`
    - The source says tabs you haven't viewed for two weeks; opening and viewing are different actions.
- `Settings.TrackingProtection.Info.BlocksTitle` — `sl/firefox-ios.xliff` — "BLOCKS" (list of blocked sites/trackers) translated as "ZAVRNJENO" (rejected/declined) instead of "BLOKIRANO"/"ZAVRNJENI".
    - Current: `ZAVRNJENO`
    - Source: `BLOCKS`
    - Suggest: `BLOKIRANO`
    - The header labels a list of blocked websites; "zavrnjeno" means rejected, not blocked, and is inconsistent with the blocking terminology used elsewhere.
- `You don’t have any tabs open in Firefox on your other devices.` — `sl/firefox-ios.xliff` — Added word "drugih" changes the meaning to "no other tabs open".
    - Current: `V Firefoxu na drugih napravah nimate odprtih drugih zavihkov.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `V Firefoxu na drugih napravah nimate odprtih zavihkov.`
    - The source says the user has no tabs open; the translation says no *other* tabs are open, implying some tabs exist.
- `ContextMenu.OpenInNewPrivateTabButtonTitle` — `sl/firefox-ios.xliff` — "New" is dropped, so the option reads "Open in private tab" instead of "Open in New Private Tab".
    - Current: `Odpri v zasebnem zavihku`
    - Source: `Open in New Private Tab`
    - Suggest: `Odpri v novem zasebnem zavihku`
    - The source says "Open in New Private Tab"; the translation omits "New", changing the action's meaning (an existing vs. a new tab).
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `sl/firefox-ios.xliff` — Missing contrastive conjunction "vendar"/"a" before the second clause; two clauses are joined by a comma only.
    - Current: `Firefox ne bo hranil vaše zgodovine in piškotkov, novi zaznamki pa bodo shranjeni.`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `Firefox ne bo hranil vaše zgodovine in piškotkov, novi zaznamki pa bodo shranjeni`
    - Source contrasts with "but"; the Slovenian uses only "pa" which is acceptable, so this should not be reported.
- `Alerts.RestoreTabs.Message.v109` — `sl/firefox-ios.xliff` — "Sorry about that" is rendered as "Oprostite" (imperative "excuse me/forgive"), which reads as addressing the user rather than an apology.
    - Current: `Oprostite.`
    - Source: `Sorry about that. Restore tabs to pick up where you left off.`
    - Suggest: `Oprostite za nevšečnost.`
    - The source is an apology by the app for the crash; "Oprostite." alone is a bare imperative that does not convey the apology naturally.
- `Settings.AppIconSelection.Accessibility.AppIconSelectionHint.v136` — `sl/firefox-ios.xliff` — The placeholder (app name, e.g. Firefox) is given a Slovenian genitive suffix glued to it, producing "ikono Firefoxa" via "%@a" which mangles the brand name for other values.
    - Current: `Izberite ikono %@a`
    - Source: `Select the %@ app icon`
    - Suggest: `Izberite ikono aplikacije %@`
    - Appending the case ending directly to the placeholder alters the brand name string and breaks for any app name not ending in a consonant.
- `Bookmarks.Menu.SavedBookmarkToastDefaultFolderLabel.v136` — `sl/firefox-ios.xliff` — Uses curly double quotes instead of the locale's straight double quotes.
    - Current: `Shranjeno v mapo “Zaznamki”`
    - Source: `Saved in “Bookmarks”`
    - Suggest: `Shranjeno v mapo "Zaznamki"`
    - The sl convention is straight-double quotes; the sibling string Bookmarks.Menu.DeletedBookmark.v131 uses straight quotes.
- `Bookmarks.Menu.SavedBookmarkToastLabel.v136` — `sl/firefox-ios.xliff` — Uses curly double quotes instead of the locale's straight double quotes.
    - Current: `Shranjeno v mapo “%@”`
    - Source: `Saved in “%@”`
    - Suggest: `Shranjeno v mapo "%@"`
    - The sl convention is straight-double quotes; the sibling toast string uses straight quotes.
- `LoginsList.NoLoginsFound.Description.v122` — `sl/firefox-ios.xliff` — "All passwords you save are encrypted" is rendered as "all passwords are stored encrypted", dropping the restriction to saved passwords.
    - Current: `Vsa gesla so shranjena v šifrirani obliki.`
    - Source: `The passwords you save or sync to %@ will be listed here. All passwords you save are encrypted.`
    - Suggest: `Vsa gesla, ki jih shranite, so šifrirana.`
    - The source limits the claim to passwords the user saves; the translation asserts that all passwords are stored encrypted.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `sl/firefox-ios.xliff` — "Tracking content" is rendered as "Sledilna vsebina" but the developer comment identifies analytics trackers; more importantly the label is inconsistent with the other tracker rows which use the genitive count pattern.
    - Current: `Sledilna vsebina: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Sledilne vsebine: %@`
    - The other rows on the same screen (Piškotkov za sledenje..., Sledilcev prstnih odtisov..., Sledilcev družbenih omrežij...) use the genitive counting form; this row breaks the pattern on the same screen.
- `Menu.EnhancedTrackingProtection.ClearData.ToastMessage.v128` — `sl/firefox-ios.xliff` — "site data" is translated as "podatki spletnega mesta" here but as "podatke strani" in the related alert/button strings on the same screen.
    - Current: `Piškotki in podatki spletnega mesta odstranjeni`
    - Source: `Cookies and site data removed`
    - Suggest: `Piškotki in podatki strani odstranjeni`
    - Terminology inconsistency within the same feature: Menu.EnhancedTrackingProtection.ClearData.AlertTitle/ButtonTitle use "podatke strani".
- `Menu.EnhancedTrackingProtection.Details.Trackers.v128` — `sl/firefox-ios.xliff` — "Trackers blocked" is translated as "Zavrnjenih sledilcev" (rejected) instead of blocked.
    - Current: `Zavrnjenih sledilcev: %@`
    - Source: `Trackers blocked: %@`
    - Suggest: `Blokiranih sledilcev: %@`
    - The source says blocked; elsewhere in the same file "blocks" is translated as "blokira", so "zavrnjenih" is both inaccurate and inconsistent.
- `Menu.EnhancedTrackingProtection.Off.Header.v128` — `sl/firefox-ios.xliff` — "%@ is off-duty" is rendered as "%@ vas ne varuje" ("%@ does not protect you"), an absolute claim the source does not make.
    - Current: `%@ vas ne varuje.`
    - Source: `%@ is off-duty. We suggest turning protections back on.`
    - Suggest: `%@ trenutno počiva.`
    - The en-US says the app is temporarily off-duty because the user disabled protections; the Slovenian states flatly that Firefox does not protect the user.
- `CreditCard.ErrorState.CardExpirationDateSublabel.v112` — `sl/firefox-ios.xliff` — "expiration date" translated as "leto poteka" (expiration year).
    - Current: `Vnesite veljavno leto poteka`
    - Source: `Enter a valid expiration date`
    - Suggest: `Vnesite veljaven datum poteka`
    - The source asks for a valid expiration date, not year.
- `ExternalLink.ExternalMailLinkConfirmation.v136` — `sl/firefox-ios.xliff` — Translation drops "open email", saying only "open the default mail application".
    - Current: `Želite odpreti privzeto aplikacijo za e-pošto?`
    - Source: `Open email in the default mail application?`
    - Suggest: `Želite odpreti e-pošto v privzeti aplikaciji za e-pošto?`
    - Source is "Open email in the default mail application?"; the object of opening (the email) is lost.
- `ExternalLink.ExternalSmsLinkConfirmation.v136` — `sl/firefox-ios.xliff` — Translation drops "open sms", saying only "open an external messaging application".
    - Current: `Želite odpreti zunanjo aplikacijo za sporočila?`
    - Source: `Open sms in an external application?`
    - Suggest: `Želite odpreti sporočilo SMS v zunanji aplikaciji?`
    - Source is "Open sms in an external application?"; the object of opening (the SMS) is lost.
- `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153` — `sl/firefox-ios.xliff` — "Website URL" rendered as "Naslov spletne strani", omitting URL and using "spletna stran" instead of "spletno mesto".
    - Current: `Naslov spletne strani`
    - Source: `Website URL`
    - Suggest: `Naslov URL spletnega mesta`
    - The related alert description uses "naslov URL spletnega mesta" for the same concept; this placeholder is inconsistent with it.
- `MainMenu.HeaderBanner.Subtitle.v142` — `sl/firefox-ios.xliff` — "Kadarkoli" should be written as two words ("kadar koli") and the plural "seconds" is rendered as singular.
    - Current: `Vzame vam sekundo. Kadarkoli lahko spremenite.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Vzame le nekaj sekund. Kadar koli lahko spremenite.`
    - en-US says "Takes seconds" (plural, a few seconds); the Slovenian says "takes you a second". Also, Slovenian orthography requires "kadar koli" as two words.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `sl/firefox-ios.xliff` — Space inserted before the ellipsis character.
    - Current: `Prijavi nedelujočo stran …`
    - Source: `Turn off Reader View`
    - Suggest: `Prijavi nedelujočo stran…`
    - The en-US "Report Broken Site…" has no space before the ellipsis; Slovenian should follow the same typography.
- `NativeErrorPage.Wayback.Error.Checking.v155` — `sl/firefox-ios.xliff` — "Checking the Archive…" is rendered as "Iskanje po arhivu …" ("Searching the archive"), a noun phrase rather than the source's progress label, though meaning is close.
    - Current: `Iskanje po arhivu …`
    - Source: `Checking the Archive…`
    - Suggest: `Preverjanje arhiva …`
    - The source says "Checking the Archive…"; the Slovenian says "searching the archive", which duplicates the wording of the separate search string.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `sl/firefox-ios.xliff` — "your support team" is rendered as "IT-služba" (IT department), introducing a term the source does not use.
    - Current: `vam morda lahko več informacij nudi IT-služba`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `ima morda več informacij vaša služba za podporo`
    - The en-US refers generically to "your support team", not specifically an IT department.
- `Onboarding.IntroDescriptionPart1.v114` — `sl/firefox-ios.xliff` — "For good" (meaning "for the benefit of all/for good causes") is rendered as "Za vedno" ("forever").
    - Current: `Neodvisni. Neprofitni. Za vedno.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Neodvisni. Neprofitni. Za dobro vseh.`
    - The source describes Firefox as being for good (a good cause); "Za vedno" means "forever", a different claim.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `sl/firefox-ios.xliff` — "marketing partners" is rendered as "tehnološkim partnerjem ... za trženje", introducing "technology" that the source never mentions.
    - Current: `tehnološkim partnerjem organizacije %2$@ za trženje`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `trženjskim partnerjem organizacije %2$@`
    - The en-US says only "%2$@’s marketing partners"; the word "tehnološkim" (technology) is not in the source and changes who the data is shared with.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `sl/firefox-ios.xliff` — Informal imperative "nadaljuj" breaks the locale's formal register.
    - Current: `Strinjam se, nadaljuj`
    - Source: `Agree and continue`
    - Suggest: `Strinjam se in nadaljuj`
    - The sl locale uses the formal register; button text mixing first-person "Strinjam se" with informal imperative "nadaljuj" is inconsistent with the established address form used elsewhere ("Strinjam se in nadaljuj").
- `Onboarding.Modern.Sync.Description.v145` — `sl/firefox-ios.xliff` — "sync on any device" mistranslated as syncing "with any other device".
    - Current: `se sinhronizirajo s katerokoli drugo napravo`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `se sinhronizirajo na vseh vaših napravah`
    - The source says bookmarks, passwords and more sync on any device, not that they sync with some other single device; the added "drugo" (other) is not in the source and changes the meaning.
- `Onboarding.Modern.TermsOfService.Description.v145` — `sl/firefox-ios.xliff` — "trusted for over 20 years" is rendered as "ki ji zaupate že več kot 20 let" ("which you have trusted for over 20 years"), asserting something about the user.
    - Current: `Delo neprofitne organizacije %@, ki ji zaupate že več kot 20 let`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Delo neprofitne organizacije %@, ki ji zaupajo že več kot 20 let`
    - The source says the non-profit is trusted (generally); the Slovenian claims the individual user has personally trusted it for over 20 years.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `sl/firefox-ios.xliff` — "for everyone" is translated as "za uporabnike po vsem svetu" ("for users all over the world").
    - Current: `za uporabnike po vsem svetu`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `za vse`
    - The source says the data helps improve things for everyone, not specifically for users worldwide.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `sl/firefox-ios.xliff` — "Manage settings" is translated only as "Nastavitve" ("Settings"), dropping the verb.
    - Current: `Nastavitve`
    - Source: `Manage settings`
    - Suggest: `Upravljanje nastavitev`
    - The source is an action link "Manage settings"; the translation loses the "manage" part.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `sl/firefox-ios.xliff` — "for everyone" is rendered as "for users around the world", adding a claim the source does not make.
    - Current: `za uporabnike po vsem svetu`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `za vse`
    - The en-US says features, performance and stability improve "for everyone"; the Slovenian asserts "for users all over the world", which is not what the source says.
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `sl/firefox-ios.xliff` — "Limited Edition Wallpaper" translated without the word "wallpaper".
    - Current: `Omejena izdaja`
    - Source: `Limited Edition Wallpaper`
    - Suggest: `Ozadje omejene izdaje`
    - The source is an accessibility label describing the wallpaper type; the parallel string uses "Klasično ozadje", so dropping "ozadje" loses the object being described.
- `PrivacyDashboard.Fingerprinters.v155` — `sl/firefox-ios.xliff` — "Fingerprinters" is rendered as "Sledilci prstnih odtisov" (trackers of fingerprints) instead of the established Slovenian term for fingerprinters.
    - Current: `Sledilci prstnih odtisov`
    - Source: `Fingerprinters`
    - Suggest: `Sledilci prstnih odtisov naprav`
    - Firefox sl uses "Sledilci prstnih odtisov naprav"/"Jemalci prstnih odtisov" for fingerprinters; the literal phrase suggests trackers that follow fingerprints rather than scripts that fingerprint the device.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `sl/firefox-ios.xliff` — The translation reads "Allow opening of %@?" making the app the object being opened, instead of allowing the app to open (the scanned URL).
    - Current: `Dovoli odpiranje %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `Ali dovolite, da %@ odpre povezavo?`
    - Per the comment, %@ is the app name and the prompt asks permission for the app to open a URL from the scanned QR code; the Slovenian instead asks permission to open the app itself.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `sl/firefox-ios.xliff` — The qualifier "For on-device AI" is dropped, so the Slovenian states unconditionally that downloaded AI models will be removed.
    - Current: `Morebitni modeli UI, ki so se že prenesli na napravo, bodo odstranjeni.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Pri UI, ki se izvaja na napravi, bodo odstranjeni vsi preneseni modeli.`
    - en-US limits the model removal to on-device AI ("For on-device AI, any downloaded models are removed."); the translation makes it a general statement about the product's behaviour.
- `CreditCard.Settings.Yes.v122` — `sl/firefox-ios.xliff` — Inconsistent question/answer register: the prompt uses first person ("Posodobim kartico?") while other prompts use the formal second person ("Želite varno shraniti to kartico?").
    - Current: `Posodobim kartico?`
    - Source: `Update`
    - Suggest: `Želite posodobiti kartico?`
    - The locale convention is formal address; CreditCard.Settings.RememberThisCard.v122 on the same screen uses "Želite …", so "Posodobim kartico?" is inconsistent.
- `Settings.AIControls.BlockedInformation.v151` — `sl/firefox-ios.xliff` — "Unblock specific features below" is rendered as "Določene možnosti lahko posebej omogočite spodaj", adding "lahko ... posebej" and losing the imperative, but more importantly the sentence structure changes the instruction.
    - Current: `Določene možnosti lahko posebej omogočite spodaj.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Spodaj odblokirajte posamezne možnosti.`
    - The source is an imperative instruction "Unblock specific features below."; the translation turns it into a statement of possibility.
- _…and 27 more._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (70)

- `NSLocationWhenInUseUsageDescription` — `Client/en.lproj/InfoPlist.strings` — The translation drops "you visit" from the source.
    - Current: `Spletne strani lahko zahtevajo vašo lokacijo.`
    - Suggest: `Spletne strani, ki jih obiščete, lahko zahtevajo vašo lokacijo.`
    - en-US says "Websites you visit may request your location"; the qualifier "you visit" is omitted.
- `Scan QR Code` — `Client/en.lproj/InfoPlist.strings` — "QR code" is rendered inconsistently with the other InfoPlist string that uses "kode QR".
    - Current: `Skeniraj QR-kodo`
    - Suggest: `Skeniraj kodo QR`
    - NSCameraUsageDescription in the same file uses "kode QR"; the same term should be consistent within the screen/file.
- `Settings.AppIconSelection.Accessibility.AppIconSelectionHint.v136` — `Shared/Supporting Files/en.lproj/AppIconSelection.strings` — The placeholder (app name, e.g. "Firefox") is given a suffixed genitive ending "-a", which mangles the brand name in the accessibility hint.
    - Current: `Izberite ikono %@a`
    - Suggest: `Izberite ikono aplikacije %@`
    - Source is "Select the %@ app icon"; %@ is the app name. Appending an inflectional "a" directly to the placeholder produces forms like "Firefoxa" glued to the substituted brand string, altering the brand name and breaking for other app names (e.g. Klar, Focus).
- `Bookmarks.Menu.DeletedBookmark.v131` — `Shared/Supporting Files/en.lproj/Bookmarks.strings` — Straight ASCII quotes used instead of the typographic quotes of the source.
    - Current: `"%@" izbrisan`
    - Suggest: `»%@« izbrisan`
    - The source uses curly quotes “%@”; the translation uses straight ASCII quotes, inconsistent with the other toast strings in the same file which keep typographic quotes.
- `Menu.EnhancedTrackingProtection.ClearData.ToastMessage.v128` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "site data" is rendered as "podatki spletnega mesta" here but as "podatki strani" in the other clear-data strings on the same screen.
    - Current: `Piškotki in podatki spletnega mesta odstranjeni`
    - Suggest: `Piškotki in podatki strani odstranjeni`
    - The same source term "site data" appears in AlertTitle, ButtonTitle and AlertText as "podatki strani"; the toast uses a different rendering on the same screen.
- `Menu.EnhancedTrackingProtection.Off.Header.v128` — `Shared/Supporting Files/en.lproj/EnhancedTrackingProtection.strings` — "%@ is off-duty" rendered as "%@ does not protect you".
    - Current: `%@ vas ne varuje.`
    - Suggest: `%@ je na dopustu.`
    - The source's idiom means protections are currently paused/off-duty; the target asserts the app does not protect you at all.
- `CreditCard.ErrorState.CardExpirationDateSublabel.v112` — `Shared/Supporting Files/en.lproj/ErrorState.strings` — "expiration date" translated as "leto poteka" (expiration year).
    - Current: `Vnesite veljavno leto poteka`
    - Suggest: `Vnesite veljaven datum poteka`
    - The source asks for a valid expiration date, not just the year.
- `ExternalLink.ExternalMailLinkConfirmation.v136` — `Shared/Supporting Files/en.lproj/ExternalLink.strings` — Translation says "Open the default email application?" instead of "Open email in the default mail application?".
    - Current: `Želite odpreti privzeto aplikacijo za e-pošto?`
    - Suggest: `Želite odpreti e-pošto v privzeti aplikaciji za e-pošto?`
    - The object of "open" in the source is the email, opened in the default mail application; the target drops the email.
- `ExternalLink.ExternalSmsLinkConfirmation.v136` — `Shared/Supporting Files/en.lproj/ExternalLink.strings` — Translation says "Open an external application for messages?" instead of "Open sms in an external application?".
    - Current: `Želite odpreti zunanjo aplikacijo za sporočila?`
    - Suggest: `Želite odpreti SMS v zunanji aplikaciji?`
    - The source opens the SMS in an external app; the target drops the SMS object.
- `CloseTab.ArrivingNotification.title.v133` — `Shared/Supporting Files/en.lproj/FxANotification.strings` — The two placeholders are swapped in meaning: %1$@ is the app name and %2$@ the tab count, but the translation reads as if %1$@ were the number.
    - Current: `Zaprtih %1$@ zavihkov: %2$@`
    - Suggest: `%1$@ – zaprti zavihki: %2$@`
    - Per the developer comment %1$@ is the app name (e.g. Firefox) and %2$@ is the number of tabs; the Slovenian places the app name where a number belongs ("Zaprtih Firefox zavihkov: 5"), producing nonsense.
- `LiveActivity.Downloads.FileNameText.v138` — `Shared/Supporting Files/en.lproj/LiveActivity.strings` — Straight ASCII quotes used instead of the typographic quotation marks of the source.
    - Current: `Prenašanje "%@"`
    - Suggest: `Prenašanje „%@“`
    - The en-US source uses curly quotes “%@”; the Slovenian uses straight ASCII double quotes, deviating from the source typography.
- `MainMenu.HeaderBanner.Subtitle.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Takes seconds" (plural) is rendered as singular "Vzame vam sekundo" (takes one second).
    - Current: `Vzame vam sekundo.`
    - Suggest: `Vzame le nekaj sekund.`
    - The source says it takes seconds (a few seconds), not one second.
- `MainMenu.HeaderBanner.Subtitle.v142` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Kadarkoli" should be written as two words in standard Slovenian.
    - Current: `Kadarkoli lahko spremenite.`
    - Suggest: `Kadar koli lahko spremenite.`
    - Slovenian orthography writes indefinite pronoun/adverb + koli separately: 'kadar koli'.
- `MainMenu.ToolsSection.DesktopSite.Title.v141` — `Shared/Supporting Files/en.lproj/MainMenu.strings` — "Desktop Site" is rendered as "Stran za namizja" while the parallel switch actions in the same menu use "stran za računalnike".
    - Current: `Stran za namizja`
    - Suggest: `Stran za računalnike`
    - Within the same Tools section, MainMenu.ToolsSection.SwitchToDesktopSite.Title.v131 and its accessibility label translate "desktop site" as "stran za računalnike"; this string uses a different term for the same source concept.
- `Microsurvey.Prompt.LogoImage.AccessibilityLabel.v129` — `Shared/Supporting Files/en.lproj/Microsurvey.strings` — The declension suffix "a" is appended directly to the app-name placeholder, producing an incorrect form such as "Logotip Firefoxa" only by chance and breaking for other app names.
    - Current: `Logotip %@a`
    - Suggest: `Logotip %@`
    - %@ is substituted with the app name verbatim; appending a case ending to a placeholder is not valid and yields wrong output for names that do not take -a (e.g. Focus, Klar).
- `Onboarding.IntroDescriptionPart1.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "For good" (meaning 'for the benefit of all / for good causes') is rendered as "Za vedno" ("forever").
    - Current: `Za vedno.`
    - Suggest: `Za dobro vseh.`
    - En-US "For good." in this Mozilla context means acting for good/benefit, not 'permanently'; "Za vedno" reverses the sense to a time expression.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "marketing partners" is translated as "tehnološkim partnerjem ... za trženje", introducing "technology" which is not in the source.
    - Current: `tehnološkim partnerjem organizacije %2$@ za trženje`
    - Suggest: `trženjskim partnerjem organizacije %2$@`
    - The source says only "%2$@’s marketing partners"; "tehnološkim" (technology) adds content that is not in the English string.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManageLink.v148` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Manage settings" is rendered only as "Nastavitve", dropping the "manage" action.
    - Current: `Nastavitve`
    - Suggest: `Upravljanje nastavitev`
    - Source is "Manage settings", a link that takes the user to manage data collection preferences; the translation says just "Settings".
- `Onboarding.Modern.BrandRefresh.Welcome.TitleV3.v149` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — The word "all" from "Open all your links" is dropped, making it identical to the v2 string.
    - Current: `Odpirajte povezave z vgrajeno zasebnostjo`
    - Suggest: `Odpirajte vse povezave z vgrajeno zasebnostjo`
    - The en-US v149 title adds "all" ("Open all your links") compared to the v2 title; the translation omits it.
- `Onboarding.Modern.Sync.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "sync on any device" is rendered as syncing "with any other device", changing the meaning.
    - Current: `se sinhronizirajo s katerokoli drugo napravo`
    - Suggest: `se sinhronizirajo na vseh vaših napravah`
    - The source says your bookmarks and passwords sync on any device (they are available on all devices), not that they sync with some other single device.
- `Onboarding.Modern.TermsOfService.Description.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "trusted for over 20 years" is translated as "which you have trusted for over 20 years", addressing the individual user instead of general trust.
    - Current: `ki ji zaupate že več kot 20 let`
    - Suggest: `ki ji ljudje zaupajo že več kot 20 let`
    - The source states the non-profit has been trusted (by people generally) for over 20 years; the translation asserts the individual user has trusted it for 20 years.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "Manage settings" is translated only as "Nastavitve" (Settings), dropping the verb.
    - Current: `Nastavitve`
    - Suggest: `Upravljanje nastavitev`
    - The source is "Manage settings", a link to manage data collection preferences; the translation omits "Manage".
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — "for everyone" is mistranslated as "for users all over the world".
    - Current: `za uporabnike po vsem svetu`
    - Suggest: `za vse`
    - The source says the data helps improve features, performance and stability "for everyone", not "for users all over the world", which adds meaning not present in the en-US text.
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `Shared/Supporting Files/en.lproj/Onboarding.strings` — Accessibility label drops the word "Wallpaper" present in the source and in the parallel Classic string.
    - Current: `Omejena izdaja`
    - Suggest: `Ozadje omejene izdaje`
    - Source is "Limited Edition Wallpaper"; the sibling string "Classic Wallpaper" is translated as "Klasično ozadje", so this accessibility label should also state that it is a wallpaper.
- `PrivacyDashboard.Fingerprinters.v155` — `Shared/Supporting Files/en.lproj/PrivacyDashboard.strings` — "Fingerprinters" is rendered as "Sledilci prstnih odtisov" (trackers of fingerprints) instead of the established Slovenian term for fingerprinting scripts.
    - Current: `Sledilci prstnih odtisov`
    - Suggest: `Sledilci prstnih odtisov naprav`
    - In Firefox Slovenian the term for "Fingerprinters" is "Sledilci prstnih odtisov naprav"; the shortened form loses the meaning of device fingerprinting.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `Shared/Supporting Files/en.lproj/ScanQRCode.strings` — The translation reverses the roles: it says "Allow opening of %@" instead of allowing the app (%@) to open the URL.
    - Current: `Dovoli odpiranje %@?`
    - Suggest: `Ali dovolite, da %@ odpre povezavo?`
    - The developer comment states %@ is the app name (e.g. Firefox); the source asks permission for the app to open a URL. The Slovenian reads as permission to open the app itself.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — The qualifier "For on-device AI" is dropped, changing the scope of the second sentence.
    - Current: `Morebitni modeli UI, ki so se že prenesli na napravo, bodo odstranjeni.`
    - Suggest: `Pri UI, ki teče na napravi, bodo odstranjeni vsi preneseni modeli.`
    - The en-US restricts model removal to on-device AI ("For on-device AI, any downloaded models are removed."); the translation omits this condition.
- `Settings.AIControls.BlockedInformation.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Unblock specific features below" is rendered as "omogočite" (enable) losing the unblock sense and the wording adds "posebej".
    - Current: `Določene možnosti lahko posebej omogočite spodaj.`
    - Suggest: `Prepoved za posamezne možnosti lahko odpravite spodaj.`
    - Source says to unblock specific features; the section otherwise uses "prepoved/prepovedano" terminology, so "omogočite" is inconsistent with the block/unblock wording.
- `Settings.Rollouts.Message.v148` — `Shared/Supporting Files/en.lproj/Settings.strings` — The list "features, performance, and stability" is mistranslated; "features" is dropped and replaced by duplicated performance terms.
    - Current: `bo izboljševal zmogljivosti, zanesljivost in učinkovitost delovanja med posodobitvami`
    - Suggest: `bo izboljševal funkcije, zmogljivost in stabilnost med posodobitvami`
    - en-US lists features, performance and stability; the translation omits "features" and renders the remaining items inaccurately.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `Shared/Supporting Files/en.lproj/Settings.strings` — Setting title translated as an imperative sentence instead of a noun-phrase label.
    - Current: `Podrsajte, da skrijete vrstico z zavihki in naslovom`
    - Suggest: `Drsenje skrije vrstico z zavihki in naslovno vrstico`
    - The source is a settings option title ("Scroll to Hide Tab and Address Bar"), a label rather than an instruction addressed to the user; it also conflates the tab bar and address bar into one bar.
- `Settings.Search.Suggest.SearchBrowsingHistory.Title.v124` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Search Browsing History" is rendered as "search history" instead of "browsing history".
    - Current: `Iskanje po zgodovini iskanja`
    - Suggest: `Iskanje po zgodovini brskanja`
    - The source refers to browsing history (zgodovina brskanja), not search history (zgodovina iskanja).
- `Settings.Studies.Title.v148` — `Shared/Supporting Files/en.lproj/Settings.strings` — "Feature Studies" is rendered as "raziskave značilnosti" instead of the established term for features ("funkcije").
    - Current: `Dovoli raziskave značilnosti`
    - Suggest: `Dovoli raziskave funkcij`
    - Elsewhere in this same file "features" is translated as "funkcije" (e.g. Settings.Studies.Message.v136 "Preizkusite funkcije in ideje"); "značilnosti" is inconsistent and misleading here.
- `Settings.Summarize.GesturesSection.FooterTitle.v142` — `Shared/Supporting Files/en.lproj/Settings.strings` — The detail "from side to side" is dropped from the shake gesture description.
    - Current: `Potresite napravo, da povzamete vsebino strani.`
    - Suggest: `Napravo potresite z ene strani na drugo, da povzamete vsebino strani.`
    - en-US says "Shake your device from side to side"; the manner of the gesture is omitted in the translation.
- `Settings.Translation.AutoTranslate.Footer.v151` — `Shared/Supporting Files/en.lproj/Settings.strings` — "your top preferred language" is translated as merely "vaš izbrani jezik", losing the notion of the highest-ranked preferred language.
    - Current: `Samodejno prevede strani v vaš izbrani jezik.`
    - Suggest: `Samodejno prevede strani v vaš najbolj prednostni jezik.`
    - The source refers to the first/top language in the Preferred Languages list, not just any selected language.
- `SentFromFirefox.SocialShare.SettingsToggle.Subtitle.v134` — `Shared/Supporting Files/en.lproj/SocialShare.strings` — "Spread the word" is rendered as the literal calque "Širite besedo", which is not idiomatic Slovenian and does not convey the meaning.
    - Current: `Širite besedo o %1$@u`
    - Suggest: `Razširite glas o %1$@u`
    - en-US "Spread the word about %1$@" means to tell others about the app; "širite besedo" is a literal word-for-word calque that does not carry that meaning in Slovenian.
- `Summarizer.Error.RateLimited.Message.v142` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — The translation uses a first-person anthropomorphic voice ("ne morem narediti") absent from the source and against product register.
    - Current: `Tega trenutno ne morem narediti.`
    - Suggest: `Tega trenutno ni mogoče obdelati.`
    - en-US "Can’t handle this one at the moment." is impersonal; the Slovenian introduces a first-person "I can't", a register the app does not use elsewhere.
- `Summarizer.RetryButton.Accessibility.Label.v145` — `Shared/Supporting Files/en.lproj/Summarizer.strings` — The a11y label for the retry button uses a second-person plural imperative addressed to the user instead of an action label matching the button's own action.
    - Current: `Poskusite znova za povzetek spletne strani`
    - Suggest: `Poskusi znova povzeti spletno stran`
    - The visible button label (Summarizer.RetryButton.Label.v142) is "Poskusi znova"; the accessibility label for the same control should use the same imperative form for consistency.
- `TabTrayOneDayAgoTitle.v140` — `Shared/Supporting Files/en.lproj/TabsTray.strings` — "1 Day Ago" is rendered as "1 dneva", which is ungrammatical and drops the meaning of the time reference.
    - Current: `1 dneva`
    - Suggest: `1 dan`
    - The menu items follow "Zapri zavihke, starejše od …", so the correct genitive singular is "enega dne"/"1 dneva" is wrong agreement with numeral 1; as a standalone label it should read "1 dan" (or "pred 1 dnevom").
- `Upgrade.SyncSign.Description.v114` — `Shared/Supporting Files/en.lproj/Upgrade.strings` — Hyphen used instead of an en dash as a sentence-level dash.
    - Current: `končali - z zavihki`
    - Suggest: `končali – z zavihki`
    - Slovenian typography requires an en dash (–) with spaces for parenthetical/appositive dashes, not a hyphen.
- `ContextMenu.GoogleLensButtonTitle.v153` — `Shared/Supporting Files/en.lproj/WebContextMenu.strings` — Singular "Search Image" rendered as plural "Išči slike".
    - Current: `Išči slike z Google Lens`
    - Suggest: `Išči sliko z Google Lens`
    - The source refers to searching for a single image (the one right-clicked), not images in general.
- `WorldCup.CountryPicker.Close.AccessibilityLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "World Cup country picker" mistranslated as "country picker at the World Cup".
    - Current: `Zapri izbirnik držav na svetovnem prvenstvu`
    - Suggest: `Zapri izbirnik držav svetovnega prvenstva`
    - The English means the country picker belonging to the World Cup widget; "na svetovnem prvenstvu" states the picker is located at the championship.
- `WorldCup.HomepageWidget.EliminatedTeamSection.Description.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — Translation adds "progress of that team" and paraphrases rather than rendering "keep up with the World Cup".
    - Current: `Izberite še kakšno ekipo, katere napredek na svetovnem prvenstvu želite spremljati.`
    - Suggest: `Izberite drugo ekipo in ostanite na tekočem s svetovnim prvenstvom.`
    - en-US says "Choose another team to keep up with the World Cup"; the Slovenian shifts the object of following to the team's progress and renders "another" as "some other/one more".
- `WorldCup.HomepageWidget.EliminatedTeamSection.Title.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — The title drops the meaning of "follow along", leaving a vague question.
    - Current: `Vas še zanima?`
    - Suggest: `Želite še naprej spremljati dogajanje?`
    - en-US "Still want to Follow Along?" asks whether the user wants to keep following the World Cup; the translation only says "Are you still interested?", losing the follow/track meaning central to this widget.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "Please refresh." is rendered as "Refresh the widget", adding an object not in the source.
    - Current: `Osvežite pripomoček.`
    - Suggest: `Osvežite.`
    - The source says only "Please refresh." without specifying the widget; the added noun changes the instruction's content.
- `WorldCup.HomepageWidget.FollowTeamCard.Close.AccessibilityLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "updates" translated as "podatki" (data) instead of updates/news.
    - Current: `Skrij podatke o svetovnem prvenstvu`
    - Suggest: `Skrij novosti o svetovnem prvenstvu`
    - The source "Hide World Cup updates" refers to updates/news, not generic data.
- `WorldCup.HomepageWidget.FollowTeamCard.Description.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "live match updates" is mistranslated as receiving notifications "live".
    - Current: `V živo prejemajte obvestila o dogajanju na tekmah in še več.`
    - Suggest: `Prejemajte obvestila o dogajanju na tekmah v živo in še več.`
    - In the source "live" modifies the matches/updates, not the act of receiving; the Slovenian word order attaches "v živo" to the receiving.
- `WorldCup.HomepageWidget.MatchUnavailableLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — Singular "match info" rendered as plural "podatki o tekmah".
    - Current: `Podatki o tekmah ta trenutek niso na voljo.`
    - Suggest: `Podatki o tekmi trenutno niso na voljo.`
    - The source refers to the info of the displayed match (singular); the widget shows one match at a time.
- `WorldCup.HomepageWidget.RoundPhase.ScrollIndicatorAccessibilityLabel.v151` — `Shared/Supporting Files/en.lproj/WorldCup.strings` — "matches" is translated as "zadetki" (goals/hits) instead of "tekme" (matches).
    - Current: `Pomaknite se na prejšnje ali naslednje zadetke`
    - Suggest: `Pomaknite se na prejšnje ali naslednje tekme`
    - The source refers to navigating between matches in the widget; "zadetki" means goals or search hits, and the rest of the file uses "tekma" for match.
- `Offline Website Data` — `Shared/en.lproj/ClearPrivateData.strings` — Settings item is in the accusative case and mistranslates "Offline Website Data" as "data while working offline".
    - Current: `Podatke pri delu brez povezave`
    - Suggest: `Podatki spletnih strani brez povezave`
    - The en-US source is a noun-phrase settings item "Offline Website Data"; the Slovenian uses the accusative "Podatke" instead of the nominative and drops "website" entirely.
- `DefaultBrowserOnboarding.Description2` — `Shared/en.lproj/Default Browser.strings` — Uses straight ASCII double quotes around the iOS setting name and leaves it untranslated inconsistently with DefaultBrowserOnboarding.Screenshot.
    - Current: `2. Tapnite "Default Browser App"`
    - Suggest: `2. Tapnite „Privzeti brskalnik“`
    - Slovenian typography uses „ “ quotation marks, and the same iOS setting is rendered as "Privzet brskalnik" in DefaultBrowserOnboarding.Screenshot, making the two references inconsistent.
- `ErrorPages.CertWarning.Title` — `Shared/en.lproj/Localizable.strings` — Title says "Your connection is not private" instead of "This connection is untrusted".
    - Current: `Vaša povezava ni zasebna`
    - Suggest: `Ta povezava ni zaupanja vredna`
    - The en-US source is "This Connection is Untrusted", which is about trust, not privacy.
- `FxA.FirefoxAccount` — `Shared/en.lproj/Localizable.strings` — Improper capitalization/word order in "Firefox Račun".
    - Current: `Firefox Račun`
    - Suggest: `Račun Firefox`
    - Slovenian does not capitalize the common noun mid-phrase, and the standard rendering of "Firefox Account" is "Račun Firefox".
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `Shared/en.lproj/Localizable.strings` — Misspelling of "logotip" as "Logtip".
    - Current: `Logtip Firefoxa, spremeni ozadje.`
    - Suggest: `Logotip Firefoxa, spremeni ozadje.`
    - The source says "Firefox logo"; the Slovenian word is "logotip", not "Logtip".
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `Shared/en.lproj/Localizable.strings` — "Cross-Site Trackers" is rendered as "Spletni sledilci" (web trackers), losing the cross-site meaning.
    - Current: `Spletni sledilci`
    - Suggest: `Sledilci med spletnimi mesti`
    - The source specifies trackers that follow users across sites; "Spletni sledilci" just means "web trackers" and drops the cross-site distinction, which is the key differentiator from the other categories on the same screen.
- `ScanQRCode.PermissionError.Message.v100` — `Shared/en.lproj/Localizable.strings` — The word "device" is dropped from the instruction to go to the device Settings.
    - Current: `Izberite "Nastavitve" > "Firefox".`
    - Suggest: `Pojdite v "Nastavitve" naprave > "Firefox".`
    - en-US says "Go to device ‘Settings’ > ‘Firefox’", clarifying it is the iOS device settings, not the app's own settings.
- `Search.ThirdPartyEngines.AddMessage` — `Shared/en.lproj/Localizable.strings` — Misspelled "iskalnik" as "isklanik".
    - Current: `Novi isklanik se bo pojavil`
    - Suggest: `Novi iskalnik se bo pojavil`
    - "isklanik" is a typo; the correct Slovenian word for search engine is "iskalnik", as used in the neighbouring strings.
- `SendTo.NoDevicesFound.Message` — `Shared/en.lproj/Localizable.strings` — "Firefox Računom" incorrectly capitalizes and leaves untranslated-style the product term "Firefox Account".
    - Current: `S tem Firefox Računom`
    - Suggest: `S tem Računom Firefox`
    - In Slovenian the noun follows the brand name; "Firefox Računom" is an English word-order calque with wrong capitalization of the common noun.
- `SendTo.NotSignedIn.Title` — `Shared/en.lproj/Localizable.strings` — "v vaš Firefox Račun" uses English word order/capitalization and a redundant possessive.
    - Current: `Niste prijavljeni v vaš Firefox Račun.`
    - Suggest: `Niste prijavljeni v svoj Račun Firefox.`
    - Slovenian requires the reflexive possessive "svoj" and places the common noun before the brand name; "Firefox Račun" is an English calque.
- `Settings.ClearAllWebsiteData.Clear.Button` — `Shared/en.lproj/Localizable.strings` — "Website Data" is rendered in the singular genitive, contradicting "all" (plural sites).
    - Current: `Izbriši vse podatke spletne strani`
    - Suggest: `Izbriši podatke vseh spletnih strani`
    - en-US "Clear All Website Data" clears data for all sites; the Slovenian says "all data of the website" (one site).
- `Settings.Disconnect.Button` — `Shared/en.lproj/Localizable.strings` — "Disconnect Sync" translated without the Sync component, making it identical to the generic "Disconnect" button.
    - Current: `Prekini povezavo`
    - Suggest: `Prekini sinhronizacijo`
    - The source distinguishes "Disconnect Sync" from "Disconnect" (Settings.Disconnect.DestructiveButton); both are rendered identically, dropping the Sync reference.
- _…and 10 more._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 96 |
| Strings | 1,919 |
| Missing strings | 3 |
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

**3 strings** are not translated yet, concentrated in:

- `sl/firefox-ios.xliff` — 2
- `sl/firefox-ios.xliff` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 13, `curly-double` 2 | **straight-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 10 | **en** |
| register | `informal` 2, `formal` 64 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (91)

> **Reads as a deliberate edit (4).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Menu.EnhancedTrackingProtection.Off.Header.v128` — `sl/firefox-ios.xliff` — "%@ is off-duty" is rendered as "%@ vas ne varuje" ("%@ does not protect you"), an absolute claim the source does not make.
    - Current: `%@ vas ne varuje.`
    - Source: `%@ is off-duty. We suggest turning protections back on.`
    - Suggest: `%@ trenutno počiva.`
    - The en-US says the app is temporarily off-duty because the user disabled protections; the Slovenian states flatly that Firefox does not protect the user.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `sl/firefox-ios.xliff` — "marketing partners" is rendered as "tehnološkim partnerjem ... za trženje", introducing "technology" that the source never mentions.
    - Current: `tehnološkim partnerjem organizacije %2$@ za trženje`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `trženjskim partnerjem organizacije %2$@`
    - The en-US says only "%2$@’s marketing partners"; the word "tehnološkim" (technology) is not in the source and changes who the data is shared with.
- `Onboarding.Modern.TermsOfService.Description.v145` — `sl/firefox-ios.xliff` — "trusted for over 20 years" is rendered as "ki ji zaupate že več kot 20 let" ("which you have trusted for over 20 years"), asserting something about the user.
    - Current: `Delo neprofitne organizacije %@, ki ji zaupate že več kot 20 let`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Delo neprofitne organizacije %@, ki ji zaupajo že več kot 20 let`
    - The source says the non-profit is trusted (generally); the Slovenian claims the individual user has personally trusted it for over 20 years.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `sl/firefox-ios.xliff` — The qualifier "For on-device AI" is dropped, so the Slovenian states unconditionally that downloaded AI models will be removed.
    - Current: `Morebitni modeli UI, ki so se že prenesli na napravo, bodo odstranjeni.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Pri UI, ki se izvaja na napravi, bodo odstranjeni vsi preneseni modeli.`
    - en-US limits the model removal to on-device AI ("For on-device AI, any downloaded models are removed."); the translation makes it a general statement about the product's behaviour.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 42 |
| 3 | Degraded language (grammar, spelling, terminology) | 41 |
| 4 | Cosmetic (typography, spacing) | 8 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSLocationWhenInUseUsageDescription` — `sl/firefox-ios.xliff` — "Websites you visit" is rendered as just "Spletne strani", dropping "you visit".
    - Current: `Spletne strani lahko zahtevajo vašo lokacijo.`
    - Source: `Websites you visit may request your location.`
    - Suggest: `Spletne strani, ki jih obiščete, lahko zahtevajo vašo lokacijo.`
    - The en-US limits the claim to websites the user visits; the translation drops that qualifier.
- `Alerts.RestoreTabs.Message.v109` — `sl/firefox-ios.xliff` — "Sorry about that" is rendered as "Oprostite" (imperative "excuse me/forgive"), which reads as addressing the user rather than an apology.
    - Current: `Oprostite.`
    - Source: `Sorry about that. Restore tabs to pick up where you left off.`
    - Suggest: `Oprostite za nevšečnost.`
    - The source is an apology by the app for the crash; "Oprostite." alone is a bare imperative that does not convey the apology naturally.
- `LoginsList.NoLoginsFound.Description.v122` — `sl/firefox-ios.xliff` — "All passwords you save are encrypted" is rendered as "all passwords are stored encrypted", dropping the restriction to saved passwords.
    - Current: `Vsa gesla so shranjena v šifrirani obliki.`
    - Source: `The passwords you save or sync to %@ will be listed here. All passwords you save are encrypted.`
    - Suggest: `Vsa gesla, ki jih shranite, so šifrirana.`
    - The source limits the claim to passwords the user saves; the translation asserts that all passwords are stored encrypted.
- `Menu.EnhancedTrackingProtection.Details.Trackers.v128` — `sl/firefox-ios.xliff` — "Trackers blocked" is translated as "Zavrnjenih sledilcev" (rejected) instead of blocked.
    - Current: `Zavrnjenih sledilcev: %@`
    - Source: `Trackers blocked: %@`
    - Suggest: `Blokiranih sledilcev: %@`
    - The source says blocked; elsewhere in the same file "blocks" is translated as "blokira", so "zavrnjenih" is both inaccurate and inconsistent.
- `Menu.EnhancedTrackingProtection.Off.Header.v128` — `sl/firefox-ios.xliff` — "%@ is off-duty" is rendered as "%@ vas ne varuje" ("%@ does not protect you"), an absolute claim the source does not make.
    - Current: `%@ vas ne varuje.`
    - Source: `%@ is off-duty. We suggest turning protections back on.`
    - Suggest: `%@ trenutno počiva.`
    - The en-US says the app is temporarily off-duty because the user disabled protections; the Slovenian states flatly that Firefox does not protect the user.
- `CreditCard.ErrorState.CardExpirationDateSublabel.v112` — `sl/firefox-ios.xliff` — "expiration date" translated as "leto poteka" (expiration year).
    - Current: `Vnesite veljavno leto poteka`
    - Source: `Enter a valid expiration date`
    - Suggest: `Vnesite veljaven datum poteka`
    - The source asks for a valid expiration date, not year.
- `ExternalLink.ExternalMailLinkConfirmation.v136` — `sl/firefox-ios.xliff` — Translation drops "open email", saying only "open the default mail application".
    - Current: `Želite odpreti privzeto aplikacijo za e-pošto?`
    - Source: `Open email in the default mail application?`
    - Suggest: `Želite odpreti e-pošto v privzeti aplikaciji za e-pošto?`
    - Source is "Open email in the default mail application?"; the object of opening (the email) is lost.
- `ExternalLink.ExternalSmsLinkConfirmation.v136` — `sl/firefox-ios.xliff` — Translation drops "open sms", saying only "open an external messaging application".
    - Current: `Želite odpreti zunanjo aplikacijo za sporočila?`
    - Source: `Open sms in an external application?`
    - Suggest: `Želite odpreti sporočilo SMS v zunanji aplikaciji?`
    - Source is "Open sms in an external application?"; the object of opening (the SMS) is lost.
- `FirefoxHomepage.Shortcuts.AddShortcut.URLTextFieldPlaceholder.v153` — `sl/firefox-ios.xliff` — "Website URL" rendered as "Naslov spletne strani", omitting URL and using "spletna stran" instead of "spletno mesto".
    - Current: `Naslov spletne strani`
    - Source: `Website URL`
    - Suggest: `Naslov URL spletnega mesta`
    - The related alert description uses "naslov URL spletnega mesta" for the same concept; this placeholder is inconsistent with it.
- `NativeErrorPage.BadCertDomain.AdvancedWarning2.v149` — `sl/firefox-ios.xliff` — "your support team" is rendered as "IT-služba" (IT department), introducing a term the source does not use.
    - Current: `vam morda lahko več informacij nudi IT-služba`
    - Source: `If you’re on a corporate network, your support team might have more info.`
    - Suggest: `ima morda več informacij vaša služba za podporo`
    - The en-US refers generically to "your support team", not specifically an IT department.
- `NativeErrorPage.Wayback.Error.Checking.v155` — `sl/firefox-ios.xliff` — "Checking the Archive…" is rendered as "Iskanje po arhivu …" ("Searching the archive"), a noun phrase rather than the source's progress label, though meaning is close.
    - Current: `Iskanje po arhivu …`
    - Source: `Checking the Archive…`
    - Suggest: `Preverjanje arhiva …`
    - The source says "Checking the Archive…"; the Slovenian says "searching the archive", which duplicates the wording of the separate search string.
- `Onboarding.IntroDescriptionPart1.v114` — `sl/firefox-ios.xliff` — "For good" (meaning "for the benefit of all/for good causes") is rendered as "Za vedno" ("forever").
    - Current: `Neodvisni. Neprofitni. Za vedno.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Neodvisni. Neprofitni. Za dobro vseh.`
    - The source describes Firefox as being for good (a good cause); "Za vedno" means "forever", a different claim.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `sl/firefox-ios.xliff` — "marketing partners" is rendered as "tehnološkim partnerjem ... za trženje", introducing "technology" that the source never mentions.
    - Current: `tehnološkim partnerjem organizacije %2$@ za trženje`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `trženjskim partnerjem organizacije %2$@`
    - The en-US says only "%2$@’s marketing partners"; the word "tehnološkim" (technology) is not in the source and changes who the data is shared with.
- `Onboarding.Modern.Sync.Description.v145` — `sl/firefox-ios.xliff` — "sync on any device" mistranslated as syncing "with any other device".
    - Current: `se sinhronizirajo s katerokoli drugo napravo`
    - Source: `Your bookmarks, passwords, and more sync on any device. Everything’s protected with encryption, so only you can access it.`
    - Suggest: `se sinhronizirajo na vseh vaših napravah`
    - The source says bookmarks, passwords and more sync on any device, not that they sync with some other single device; the added "drugo" (other) is not in the source and changes the meaning.
- `Onboarding.Modern.TermsOfService.Description.v145` — `sl/firefox-ios.xliff` — "trusted for over 20 years" is rendered as "ki ji zaupate že več kot 20 let" ("which you have trusted for over 20 years"), asserting something about the user.
    - Current: `Delo neprofitne organizacije %@, ki ji zaupate že več kot 20 let`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Delo neprofitne organizacije %@, ki ji zaupajo že več kot 20 let`
    - The source says the non-profit is trusted (generally); the Slovenian claims the individual user has personally trusted it for over 20 years.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `sl/firefox-ios.xliff` — "Manage settings" is translated only as "Nastavitve" ("Settings"), dropping the verb.
    - Current: `Nastavitve`
    - Source: `Manage settings`
    - Suggest: `Upravljanje nastavitev`
    - The source is an action link "Manage settings"; the translation loses the "manage" part.
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `sl/firefox-ios.xliff` — "for everyone" is translated as "za uporabnike po vsem svetu" ("for users all over the world").
    - Current: `za uporabnike po vsem svetu`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `za vse`
    - The source says the data helps improve things for everyone, not specifically for users worldwide.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `sl/firefox-ios.xliff` — "for everyone" is rendered as "for users around the world", adding a claim the source does not make.
    - Current: `za uporabnike po vsem svetu`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `za vse`
    - The en-US says features, performance and stability improve "for everyone"; the Slovenian asserts "for users all over the world", which is not what the source says.
- `Onboarding.Wallpaper.Accessibility.LimitedEdition.v114` — `sl/firefox-ios.xliff` — "Limited Edition Wallpaper" translated without the word "wallpaper".
    - Current: `Omejena izdaja`
    - Source: `Limited Edition Wallpaper`
    - Suggest: `Ozadje omejene izdaje`
    - The source is an accessibility label describing the wallpaper type; the parallel string uses "Klasično ozadje", so dropping "ozadje" loses the object being described.
- `PrivacyDashboard.Fingerprinters.v155` — `sl/firefox-ios.xliff` — "Fingerprinters" is rendered as "Sledilci prstnih odtisov" (trackers of fingerprints) instead of the established Slovenian term for fingerprinters.
    - Current: `Sledilci prstnih odtisov`
    - Source: `Fingerprinters`
    - Suggest: `Sledilci prstnih odtisov naprav`
    - Firefox sl uses "Sledilci prstnih odtisov naprav"/"Jemalci prstnih odtisov" for fingerprinters; the literal phrase suggests trackers that follow fingerprints rather than scripts that fingerprint the device.
- `ScanQRCode.ConfirmOpenURL.Message.v129` — `sl/firefox-ios.xliff` — The translation reads "Allow opening of %@?" making the app the object being opened, instead of allowing the app to open (the scanned URL).
    - Current: `Dovoli odpiranje %@?`
    - Source: `Allow %@ to open?`
    - Suggest: `Ali dovolite, da %@ odpre povezavo?`
    - Per the comment, %@ is the app name and the prompt asks permission for the app to open a URL from the scanned QR code; the Slovenian instead asks permission to open the app itself.
- `Settings.AIControls.AIPoweredFeaturesSection.BlockedStatusDescriptionV2.v151` — `sl/firefox-ios.xliff` — The qualifier "For on-device AI" is dropped, so the Slovenian states unconditionally that downloaded AI models will be removed.
    - Current: `Morebitni modeli UI, ki so se že prenesli na napravo, bodo odstranjeni.`
    - Source: `**Blocked**: You won’t see and can’t use the feature. For on-device AI, any downloaded models are removed.`
    - Suggest: `Pri UI, ki se izvaja na napravi, bodo odstranjeni vsi preneseni modeli.`
    - en-US limits the model removal to on-device AI ("For on-device AI, any downloaded models are removed."); the translation makes it a general statement about the product's behaviour.
- `Settings.AIControls.AIPoweredFeaturesSection.Title.v151` — `sl/firefox-ios.xliff` — "AI-POWERED FEATURES" translated as "MOŽNOSTI UMETNE INTELIGENCE" (features of AI) instead of features powered by AI.
    - Current: `MOŽNOSTI UMETNE INTELIGENCE`
    - Source: `AI-POWERED FEATURES`
    - Suggest: `MOŽNOSTI Z UMETNO INTELIGENCO`
    - The source describes features enhanced/powered by AI, not features belonging to AI.
- `Settings.AIControls.BlockedInformation.v151` — `sl/firefox-ios.xliff` — "Unblock specific features below" is rendered as "Določene možnosti lahko posebej omogočite spodaj", adding "lahko ... posebej" and losing the imperative, but more importantly the sentence structure changes the instruction.
    - Current: `Določene možnosti lahko posebej omogočite spodaj.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Spodaj odblokirajte posamezne možnosti.`
    - The source is an imperative instruction "Unblock specific features below."; the translation turns it into a statement of possibility.
- `Settings.Rollouts.Message.v148` — `sl/firefox-ios.xliff` — "features" is mistranslated and the list of items does not match the source.
    - Current: `bo izboljševal zmogljivosti, zanesljivost in učinkovitost delovanja`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `bo izboljševal funkcije, učinkovitost delovanja in stabilnost`
    - The source lists features, performance and stability; the translation drops "features" and renders the list as performance/reliability/performance.
- `Settings.Search.Suggest.SearchBrowsingHistory.Title.v124` — `sl/firefox-ios.xliff` — "Search Browsing History" is rendered as "search history" instead of "browsing history".
    - Current: `Iskanje po zgodovini iskanja`
    - Source: `Search Browsing History`
    - Suggest: `Iskanje po zgodovini brskanja`
    - The source refers to browsing history (zgodovina brskanja), not search history.
- `Settings.Studies.Message.v148` — `sl/firefox-ios.xliff` — "features" translated as "novosti" (new things) rather than features.
    - Current: `za preizkušanje novosti`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `za preizkušanje funkcij`
    - The source says users are selected to test features; "novosti" means novelties/new items and is inconsistent with "funkcije" used elsewhere.
- `Settings.TechnicalData.Message.v136` — `sl/firefox-ios.xliff` — "hardware configuration" mistranslated as "nastavitvi strojne opreme" (hardware setting) and "features" dropped/merged.
    - Current: `nastavitvi strojne opreme in uporabi nam pomagajo izboljševati zmogljivosti, delovanje in zanesljivost`
    - Source: `Data about your device, hardware configuration, and usage helps us improve %@ features, performance and stability.`
    - Suggest: `nastavitvah strojne opreme in uporabi nam pomagajo izboljševati funkcije, zmogljivost in stabilnost`
    - The source lists "features, performance and stability"; the target lists "zmogljivosti, delovanje in zanesljivost", losing "features" and rendering "configuration" as a singular setting.
- `Summarizer.RetryButton.Accessibility.Label.v145` — `sl/firefox-ios.xliff` — The a11y label is translated as an instruction to the user instead of naming the button action.
    - Current: `Poskusite znova za povzetek spletne strani`
    - Source: `Retry to summarize web page`
    - Suggest: `Znova poskusi povzeti spletno stran`
    - Source "Retry to summarize web page" labels the button action; also inconsistent with the button label "Poskusi znova" (imperative 2nd person singular) for the same control.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `sl/firefox-ios.xliff` — "Terms of Use sheet opened" translated as "Stran s pogoji uporabe odprta" ("page" instead of the bottom sheet/panel).
    - Current: `Stran s pogoji uporabe odprta`
    - Source: `Terms of Use sheet opened`
    - Suggest: `Pogoji uporabe odprti`
    - The source refers to a bottom sheet, not a page; the app elsewhere uses "pogoji uporabe" without "stran".
- `WebCompatReporter.SubOption.MissingItems.v154` — `sl/firefox-ios.xliff` — "Missing items" translated as "Manjkajoči elementi strani", adding "strani" (of the page) not present in the source.
    - Current: `Manjkajoči elementi strani`
    - Source: `Missing items`
    - Suggest: `Manjkajoči elementi`
    - The source says only "Missing items"; "strani" adds information the source does not state.
- `ContextMenu.GoogleLensButtonTitle.v153` — `sl/firefox-ios.xliff` — "Search Image" (singular, the specific image) rendered as plural "slike", changing the meaning to searching for images generally.
    - Current: `Išči slike z Google Lens`
    - Source: `Search Image with Google Lens`
    - Suggest: `Išči sliko z Google Lens`
    - The source refers to searching for the selected image with Google Lens, not for images in general.
- `WorldCup.CountryPicker.Close.AccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "World Cup country picker" mistranslated as "country picker at the World Cup" instead of the picker belonging to the World Cup widget.
    - Current: `Zapri izbirnik držav na svetovnem prvenstvu`
    - Source: `Close World Cup country picker`
    - Suggest: `Zapri izbirnik držav svetovnega prvenstva`
    - The label closes the World Cup country picker; "na svetovnem prvenstvu" reads as being located at the championship.
- `WorldCup.HomepageWidget.EliminatedTeamSection.Description.v151` — `sl/firefox-ios.xliff` — "Choose another team" is rendered as "Choose some other team whose progress you want to follow", altering the meaning.
    - Current: `Izberite še kakšno ekipo, katere napredek na svetovnem prvenstvu želite spremljati.`
    - Source: `Choose another team to keep up with the World Cup.`
    - Suggest: `Izberite drugo ekipo, da boste v koraku s svetovnim prvenstvom.`
    - The source says to choose another team to keep up with the World Cup; the target says to choose yet another team whose progress at the World Cup you want to follow, which changes the meaning ("še kakšno" = one more, in addition).
- `WorldCup.HomepageWidget.EliminatedTeamSection.Title.v151` — `sl/firefox-ios.xliff` — "Still want to Follow Along?" is reduced to "Are you still interested?", dropping the sense of continuing to follow.
    - Current: `Vas še zanima?`
    - Source: `Still want to Follow Along?`
    - Suggest: `Bi radi še naprej spremljali dogajanje?`
    - The source asks whether the user wants to keep following along; the target's vague "Are you still interested?" loses that meaning.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `sl/firefox-ios.xliff` — "Please refresh." is translated as "Refresh the widget.", adding an object not in the source.
    - Current: `Osvežite pripomoček.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `Osvežite.`
    - The source is a generic "Please refresh." without specifying the widget.
- `WorldCup.HomepageWidget.FollowTeamCard.Close.AccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "updates" translated as "podatke" (data) instead of updates/news.
    - Current: `Skrij podatke o svetovnem prvenstvu`
    - Source: `Hide World Cup updates`
    - Suggest: `Skrij novosti o svetovnem prvenstvu`
    - The source refers to World Cup updates, not to data.
- `WorldCup.HomepageWidget.FollowTeamCard.Description.v151` — `sl/firefox-ios.xliff` — "live match updates" is rendered as "receive updates live", shifting "live" from the matches to the receiving.
    - Current: `V živo prejemajte obvestila o dogajanju na tekmah in še več.`
    - Source: `Get live match updates and more.`
    - Suggest: `Prejemajte obvestila o dogajanju na tekmah v živo in še več.`
    - In en-US "live" modifies the match updates; the Slovene word order attaches it to the act of receiving.
- `WorldCup.HomepageWidget.RoundPhase.ScrollIndicatorAccessibilityLabel.v151` — `sl/firefox-ios.xliff` — "matches" mistranslated as "zadetke" (goals/hits) instead of "tekme".
    - Current: `Pomaknite se na prejšnje ali naslednje zadetke`
    - Source: `Scroll to see previous or next matches`
    - Suggest: `Pomaknite se na prejšnje ali naslednje tekme`
    - The source refers to previous or next matches (tekme); "zadetki" means goals or search hits, not matches.
- `Offline Website Data` — `sl/firefox-ios.xliff` — "Offline Website Data" translated as "Podatke pri delu brez povezave", dropping "Website".
    - Current: `Podatke pri delu brez povezave`
    - Source: `Offline Website Data`
    - Suggest: `Podatke spletnih strani brez povezave`
    - The source names data stored by websites for offline use; the translation says only "data when working offline", losing the website reference.
- `DefaultBrowserCard.PeaceOfMind.Description.v108` — `sl/firefox-ios.xliff` — "blocks" trackers translated as "zavrne" (rejects/declines) instead of "blokira/zablokira".
    - Current: `Firefox vsak mesec zavrne povprečno več kot 3000 sledilcev na uporabnika.`
    - Source: `Firefox blocks 3,000+ trackers per user each month on average. Make us your default browser for privacy peace of mind.`
    - Suggest: `Firefox vsak mesec blokira povprečno več kot 3000 sledilcev na uporabnika.`
    - The product's established term for blocking trackers is "blokira"; "zavrne" describes a different action.
- `ErrorPages.CertWarning.Title` — `sl/firefox-ios.xliff` — Title says "Your connection is not private" instead of "This Connection is Untrusted".
    - Current: `Vaša povezava ni zasebna`
    - Source: `This Connection is Untrusted`
    - Suggest: `Ta povezava ni zaupanja vredna`
    - The en-US says the connection is untrusted; the Slovenian asserts it is not private, a different claim.
- `Hotkeys.Forward.DiscoveryTitle` — `sl/firefox-ios.xliff` — Ambiguous/wrong rendering: source "Forward" refers to navigating forward in session history, and the translation reads as "Next"; however per the comment context it should be navigation forward.
    - Current: `Naprej`
    - Source: `Forward`
    - Suggest: `Naprej (po zgodovini)`
    - The paired Back shortcut is "Nazaj"; "Naprej" is acceptable but the developer comment describes switching to a subsequent tab. Low-risk ambiguity.
- `Menu.TrackingProtectionCrossSiteTrackers.Title` — `sl/firefox-ios.xliff` — "Cross-Site Trackers" is rendered as "Spletni sledilci" (web trackers), losing the cross-site meaning.
    - Current: `Spletni sledilci`
    - Source: `Cross-Site Trackers`
    - Suggest: `Sledilci med spletnimi mesti`
    - The source specifies trackers that follow users across sites; "Spletni sledilci" just means "web trackers" and does not convey "cross-site".
- `Menu.TrackingProtectionDescription.ContentTrackers` — `sl/firefox-ios.xliff` — Translation drops "outside" ads and omits "login fields" from the list of things that might not work.
    - Current: `vendar nekateri gumbi in obrazci morda ne bodo delovali`
    - Source: `Websites may load outside ads, videos, and other content that contains hidden trackers. Blocking this can make websites load faster, but some buttons, forms, and login fields, might not work.`
    - Suggest: `vendar nekateri gumbi, obrazci in prijavna polja morda ne bodo delovali`
    - The en-US lists "buttons, forms, and login fields"; the Slovenian omits login fields.
- `Menu.TrackingProtectionDescription.CryptominersNew` — `sl/firefox-ios.xliff` — "secretly use your system's computing power" loses "secretly", and "increase your energy bill" is rendered with the colloquial "zasolijo račun".
    - Current: `Kriptorudarji izrabljajo zmogljivost vašega računalnika za rudarjenje digitalnega denarja.`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Kriptorudarji na skrivaj izrabljajo računsko zmogljivost vašega sistema za rudarjenje digitalnega denarja.`
    - The source says cryptominers "secretly use your system’s computing power"; the omission of "secretly" drops meaning.
- `ScanQRCode.PermissionError.Message.v100` — `sl/firefox-ios.xliff` — The instruction to go to the device settings is reduced to "Izberite" (Select), dropping "device".
    - Current: `Izberite "Nastavitve" > "Firefox".`
    - Source: `Go to device ‘Settings’ > ‘Firefox’. Allow Firefox to access camera.`
    - Suggest: `Pojdite v "Nastavitve" naprave > "Firefox".`
    - en-US says "Go to device ‘Settings’ > ‘Firefox’"; the reference to the device's Settings app is lost.
- `Settings.BlockOpeningExternalApps.Title` — `sl/firefox-ios.xliff` — "Block" translated as "Zavrni" (reject/decline) instead of "Prepreči"/"Blokiraj".
    - Current: `Zavrni odpiranje zunanjih aplikacij`
    - Source: `Block Opening External Apps`
    - Suggest: `Prepreči odpiranje zunanjih aplikacij`
    - The setting blocks external apps from opening; "zavrni" implies a one-time refusal rather than a persistent block.
- `Settings.NoImageModeBlockImages.Label.v99` — `sl/firefox-ios.xliff` — "Block Images" translated as "Zavračaj slike" (reject images) instead of "Zavrni/Blokiraj slike".
    - Current: `Zavračaj slike`
    - Source: `Block Images`
    - Suggest: `Blokiraj slike`
    - The source means blocking images from loading; "zavračaj" (reject) is not the established term for blocking content in Firefox sl, which uses "blokiraj".
- `Settings.Siri.SectionDescription` — `sl/firefox-ios.xliff` — "Siri shortcuts" rendered as just "bližnjice", dropping Siri from the phrase.
    - Current: `Uporabi bližnjice za hitro odpiranje Firefoxa s Siri`
    - Source: `Use Siri shortcuts to quickly open Firefox via Siri`
    - Suggest: `Uporabite bližnjice Siri za hitro odpiranje Firefoxa s Siri`
    - The source says "Use Siri shortcuts…"; the translation omits "Siri" as the qualifier of shortcuts.
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `sl/firefox-ios.xliff` — "haven't viewed" is rendered as "niste odprli" (haven't opened) — different action.
    - Current: `ki jih dva tedna niste odprli`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `ki si jih dva tedna niste ogledali`
    - The source says tabs you haven't viewed for two weeks; opening and viewing are different actions.
- `Settings.TrackingProtection.Info.BlocksTitle` — `sl/firefox-ios.xliff` — "BLOCKS" (list of blocked sites/trackers) translated as "ZAVRNJENO" (rejected/declined) instead of "BLOKIRANO"/"ZAVRNJENI".
    - Current: `ZAVRNJENO`
    - Source: `BLOCKS`
    - Suggest: `BLOKIRANO`
    - The header labels a list of blocked websites; "zavrnjeno" means rejected, not blocked, and is inconsistent with the blocking terminology used elsewhere.
- `You don’t have any tabs open in Firefox on your other devices.` — `sl/firefox-ios.xliff` — Added word "drugih" changes the meaning to "no other tabs open".
    - Current: `V Firefoxu na drugih napravah nimate odprtih drugih zavihkov.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `V Firefoxu na drugih napravah nimate odprtih zavihkov.`
    - The source says the user has no tabs open; the translation says no *other* tabs are open, implying some tabs exist.
- `ContextMenu.OpenInNewPrivateTabButtonTitle` — `sl/firefox-ios.xliff` — "New" is dropped, so the option reads "Open in private tab" instead of "Open in New Private Tab".
    - Current: `Odpri v zasebnem zavihku`
    - Source: `Open in New Private Tab`
    - Suggest: `Odpri v novem zasebnem zavihku`
    - The source says "Open in New Private Tab"; the translation omits "New", changing the action's meaning (an existing vs. a new tab).

### C. Grammar, agreement & spelling

- `Settings.AppIconSelection.Accessibility.AppIconSelectionHint.v136` — `sl/firefox-ios.xliff` — The placeholder (app name, e.g. Firefox) is given a Slovenian genitive suffix glued to it, producing "ikono Firefoxa" via "%@a" which mangles the brand name for other values.
    - Current: `Izberite ikono %@a`
    - Source: `Select the %@ app icon`
    - Suggest: `Izberite ikono aplikacije %@`
    - Appending the case ending directly to the placeholder alters the brand name string and breaks for any app name not ending in a consonant.
- `MainMenu.HeaderBanner.Subtitle.v142` — `sl/firefox-ios.xliff` — "Kadarkoli" should be written as two words ("kadar koli") and the plural "seconds" is rendered as singular.
    - Current: `Vzame vam sekundo. Kadarkoli lahko spremenite.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Vzame le nekaj sekund. Kadar koli lahko spremenite.`
    - en-US says "Takes seconds" (plural, a few seconds); the Slovenian says "takes you a second". Also, Slovenian orthography requires "kadar koli" as two words.
- `TabTrayOneDayAgoTitle.v140` — `sl/firefox-ios.xliff` — "1 Day Ago" rendered as "1 dneva", an ungrammatical number-noun agreement (should be "1 dan" / "1 dnevom").
    - Current: `1 dneva`
    - Source: `1 Day Ago`
    - Suggest: `1 dan`
    - In Slovenian the numeral 1 takes the nominative singular "dan", not the genitive/dual form "dneva"; the source is "1 Day Ago".
- `TabTrayOneMonthAgoTitle.v140` — `sl/firefox-ios.xliff` — "1 Month Ago" rendered as "1 meseca", wrong case/number agreement with the numeral 1.
    - Current: `1 meseca`
    - Source: `1 Month Ago`
    - Suggest: `1 mesec`
    - Numeral 1 requires singular nominative "mesec"; "meseca" is dual/genitive and is ungrammatical here.
- `TabTrayOneWeekAgoTitle.v140` — `sl/firefox-ios.xliff` — "1 Week Ago" rendered as "1 tedna", wrong case/number agreement with the numeral 1.
    - Current: `1 tedna`
    - Source: `1 Week Ago`
    - Suggest: `1 teden`
    - Numeral 1 requires singular nominative "teden"; "tedna" is dual/genitive and is ungrammatical here.
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `sl/firefox-ios.xliff` — Sentence "Captions are missing" rendered as a noun phrase "Manjkajoči napisi", inconsistent with the other sub-options which are full clauses.
    - Current: `Manjkajoči napisi`
    - Source: `Captions are missing`
    - Suggest: `Napisi manjkajo`
    - Source is a clause ("Captions are missing"), like the sibling options rendered as clauses ("Gumbi ali povezave ne delujejo").
- `FxA.FirefoxAccount` — `sl/firefox-ios.xliff` — "Firefox Račun" uses English word order; Slovenian requires "Račun Firefox".
    - Current: `Firefox Račun`
    - Source: `Firefox Account`
    - Suggest: `Račun Firefox`
    - Slovenian noun phrase order places the brand after the noun; also the common noun should not be capitalized mid-phrase.
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `sl/firefox-ios.xliff` — Misspelling of "Logotip" as "Logtip".
    - Current: `Logtip Firefoxa`
    - Source: `Firefox logo, change the wallpaper.`
    - Suggest: `Logotip Firefoxa`
    - The Slovenian word for "logo" is "logotip"; "Logtip" is a typo.
- `Search.ThirdPartyEngines.AddMessage` — `sl/firefox-ios.xliff` — Typo: "isklanik" should be "iskalnik".
    - Current: `Novi isklanik se bo pojavil v vrstici za hitro iskanje.`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `Novi iskalnik se bo pojavil v vrstici za hitro iskanje.`
    - The Slovenian word for "search engine" is "iskalnik"; the letters are transposed.
- `SendTo.NoDevicesFound.Message` — `sl/firefox-ios.xliff` — "Firefox Računom" uses English-style capitalization and word order for "Firefox Account".
    - Current: `S tem Firefox Računom`
    - Source: `You don’t have any other devices connected to this Firefox Account available to sync.`
    - Suggest: `S tem računom Firefox`
    - In Slovenian the generic noun is lowercase and follows the brand name: "račun Firefox".
- `SendTo.NotSignedIn.Title` — `sl/firefox-ios.xliff` — Incorrect case and unnecessary possessive pronoun; also "Firefox Račun" should not be capitalized mid-phrase as two nouns.
    - Current: `Niste prijavljeni v vaš Firefox Račun.`
    - Source: `You are not signed in to your Firefox Account.`
    - Suggest: `Niste prijavljeni v svoj račun Firefox.`
    - Slovenian requires the reflexive possessive "svoj", and the noun order/capitalization "Firefox Račun" is a calque of English; correct form is "račun Firefox".
- `SentTab_TabArrivingNotification_WithDevice_title` — `sl/firefox-ios.xliff` — Wrong preposition/case for device name: "z %@" should be "iz naprave %@" or "z naprave %@" — but here the source says "from %@" meaning received from a device.
    - Current: `Zavihek prejet z %@`
    - Source: `Tab received from %@`
    - Suggest: `Zavihek prejet iz %@`
    - The placeholder holds a device name; "prejet z %@" is ungrammatical/ambiguous, standard Slovenian uses "iz" for origin from a device.
- `Settings.ClearAllWebsiteData.Clear.Button` — `sl/firefox-ios.xliff` — "all website data" rendered with a singular noun phrase, so it reads "all data of the website".
    - Current: `Izbriši vse podatke spletne strani`
    - Source: `Clear All Website Data`
    - Suggest: `Izbriši vse podatke spletnih strani`
    - The source clears data for all websites; the singular genitive "spletne strani" restricts it to one site.
- `Settings.FxA.Title` — `sl/firefox-ios.xliff` — Brand-plus-noun compound needs Slovenian possessive form and lowercase noun.
    - Current: `Firefox Račun`
    - Source: `Firefox Account`
    - Suggest: `Firefoxov račun`
    - "Firefox Račun" is an ungrammatical calque of English title case; Slovenian requires "Firefoxov račun" (cf. "Firefoxova domača stran" used elsewhere in this batch).
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `sl/firefox-ios.xliff` — Missing contrastive conjunction "vendar"/"a" before the second clause; two clauses are joined by a comma only.
    - Current: `Firefox ne bo hranil vaše zgodovine in piškotkov, novi zaznamki pa bodo shranjeni.`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `Firefox ne bo hranil vaše zgodovine in piškotkov, novi zaznamki pa bodo shranjeni`
    - Source contrasts with "but"; the Slovenian uses only "pa" which is acceptable, so this should not be reported.

### D. Terminology, register & consistency

- `Scan QR Code` — `sl/firefox-ios.xliff` — QR code term inconsistent with "kode QR" used in NSCameraUsageDescription.
    - Current: `Skeniraj QR-kodo`
    - Source: `Scan QR Code`
    - Suggest: `Skeniraj kodo QR`
    - The same source term "QR code" is rendered "kode QR" elsewhere in the same file; one form should be used.
- `Menu.EnhancedTrackingProtection.ClearData.ToastMessage.v128` — `sl/firefox-ios.xliff` — "site data" is translated as "podatki spletnega mesta" here but as "podatke strani" in the related alert/button strings on the same screen.
    - Current: `Piškotki in podatki spletnega mesta odstranjeni`
    - Source: `Cookies and site data removed`
    - Suggest: `Piškotki in podatki strani odstranjeni`
    - Terminology inconsistency within the same feature: Menu.EnhancedTrackingProtection.ClearData.AlertTitle/ButtonTitle use "podatke strani".
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `sl/firefox-ios.xliff` — "Tracking content" is rendered as "Sledilna vsebina" but the developer comment identifies analytics trackers; more importantly the label is inconsistent with the other tracker rows which use the genitive count pattern.
    - Current: `Sledilna vsebina: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Sledilne vsebine: %@`
    - The other rows on the same screen (Piškotkov za sledenje..., Sledilcev prstnih odtisov..., Sledilcev družbenih omrežij...) use the genitive counting form; this row breaks the pattern on the same screen.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `sl/firefox-ios.xliff` — Informal imperative "nadaljuj" breaks the locale's formal register.
    - Current: `Strinjam se, nadaljuj`
    - Source: `Agree and continue`
    - Suggest: `Strinjam se in nadaljuj`
    - The sl locale uses the formal register; button text mixing first-person "Strinjam se" with informal imperative "nadaljuj" is inconsistent with the established address form used elsewhere ("Strinjam se in nadaljuj").
- `CreditCard.Settings.Yes.v122` — `sl/firefox-ios.xliff` — Inconsistent question/answer register: the prompt uses first person ("Posodobim kartico?") while other prompts use the formal second person ("Želite varno shraniti to kartico?").
    - Current: `Posodobim kartico?`
    - Source: `Update`
    - Suggest: `Želite posodobiti kartico?`
    - The locale convention is formal address; CreditCard.Settings.RememberThisCard.v122 on the same screen uses "Želite …", so "Posodobim kartico?" is inconsistent.
- `Settings.AIControls.BlockAIEnhancementsTitle.v151` — `sl/firefox-ios.xliff` — Abbreviation "UI" for AI is used here and in BlockedInformation, while other strings on the same screen spell out "umetne inteligence"; inconsistent terminology within one screen.
    - Current: `Prepovej izboljšave s pomočjo UI`
    - Source: `Block AI Enhancements`
    - Suggest: `Prepovej izboljšave z umetno inteligenco`
    - The same source term "AI" is rendered as both "umetna inteligenca" and "UI" on the same settings screen.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `sl/firefox-ios.xliff` — Setting label turned into an instruction addressed to the user instead of a noun-style toggle title.
    - Current: `Podrsajte, da skrijete vrstico z zavihki in naslovom`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Drsenje skrije vrstico z zavihki in naslovno vrstico`
    - En-US is a settings toggle title "Scroll to Hide Tab and Address Bar"; the Slovenian reads as a command telling the user to swipe, and merges the two bars into one.
- `Settings.Studies.Title.v148` — `sl/firefox-ios.xliff` — "Feature Studies" rendered as "raziskave značilnosti" instead of the established term for features ("funkcije").
    - Current: `Dovoli raziskave značilnosti`
    - Source: `Allow Feature Studies`
    - Suggest: `Dovoli raziskave funkcij`
    - Elsewhere in this file "features" is translated as "funkcije" (e.g. Settings.Studies.Message.v136: "Preizkusite funkcije in ideje"); "značilnosti" is inconsistent terminology for feature studies.
- `Summarizer.Error.RateLimited.Message.v142` — `sl/firefox-ios.xliff` — The impersonal source is rendered in the first person, making the app speak as "I".
    - Current: `Tega trenutno ne morem narediti.`
    - Source: `Can’t handle this one at the moment. Try again later!`
    - Suggest: `Tega trenutno ni mogoče narediti.`
    - The en-US "Can't handle this one at the moment." is impersonal; Slovenian UI convention avoids first-person app voice, and the rest of the file uses impersonal forms.
- `Summarizer.ToS.InfoPanel.Title.Label.v143` — `sl/firefox-ios.xliff` — "Summarize this page?" is rendered in the first person singular ("Shall I summarize").
    - Current: `Povzamem vsebino strani?`
    - Source: `Summarize this page?`
    - Suggest: `Želite povzeti vsebino strani?`
    - The source is a neutral question; the Slovenian first-person verb makes the app speak as "I", which conflicts with the formal, impersonal register used elsewhere.
- `WebCompatReporter.Toast.ReportSent.v155` — `sl/firefox-ios.xliff` — "Report" rendered as "Poročilo" here but as "prijava" in the other Report screens/buttons, breaking terminology consistency.
    - Current: `Poročilo poslano`
    - Source: `Report sent`
    - Suggest: `Prijava poslana`
    - Same source term "report" is translated "prijava" in WebCompatReporter.SendButton.Title and Preview.Title within the same feature.
- `Enter passcode` — `sl/firefox-ios.xliff` — "passcode" translated as "geslo" (password) instead of a passcode term.
    - Current: `Vnesite geslo`
    - Source: `Enter passcode`
    - Suggest: `Vnesite geslo za dostop`
    - In this file "password" and "passcode" are distinct; "geslo" is the established rendering of "password", making the passcode/password distinction disappear.
- `FirefoxHome.Stories.Minutes.v140` — `sl/firefox-ios.xliff` — "minut" is not abbreviated although the comment requires an abbreviation due to space constraints.
    - Current: `minut: %d`
    - Source: `min: %d`
    - Suggest: `min: %d`
    - Developer comment states minutes should be abbreviated due to space constraints; the source uses "min".
- `Menu.Share.v99` — `sl/firefox-ios.xliff` — "Share" translated as "Deli" (divide/share in the arithmetic sense) instead of the established "Deli z drugimi"/"Souporaba".
    - Current: `Deli`
    - Source: `Share`
    - Suggest: `Deli z drugimi`
    - In Mozilla sl terminology the share action is "Deli z drugimi"; bare "Deli" reads as the imperative of "divide".

### E. Typography, punctuation & spacing

- `Bookmarks.Menu.SavedBookmarkToastDefaultFolderLabel.v136` — `sl/firefox-ios.xliff` — Uses curly double quotes instead of the locale's straight double quotes.
    - Current: `Shranjeno v mapo “Zaznamki”`
    - Source: `Saved in “Bookmarks”`
    - Suggest: `Shranjeno v mapo "Zaznamki"`
    - The sl convention is straight-double quotes; the sibling string Bookmarks.Menu.DeletedBookmark.v131 uses straight quotes.
- `Bookmarks.Menu.SavedBookmarkToastLabel.v136` — `sl/firefox-ios.xliff` — Uses curly double quotes instead of the locale's straight double quotes.
    - Current: `Shranjeno v mapo “%@”`
    - Source: `Saved in “%@”`
    - Suggest: `Shranjeno v mapo "%@"`
    - The sl convention is straight-double quotes; the sibling toast string uses straight quotes.
- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `sl/firefox-ios.xliff` — Space inserted before the ellipsis character.
    - Current: `Prijavi nedelujočo stran …`
    - Source: `Turn off Reader View`
    - Suggest: `Prijavi nedelujočo stran…`
    - The en-US "Report Broken Site…" has no space before the ellipsis; Slovenian should follow the same typography.
- `Upgrade.SyncSign.Description.v114` — `sl/firefox-ios.xliff` — Hyphen used as a sentence dash instead of the house en dash.
    - Current: `kjer ste končali - z zavihki`
    - Source: `Pick up where you left off with tabs from other devices now on your homepage.`
    - Suggest: `kjer ste končali – z zavihki`
    - The locale convention is the en dash; a hyphen-minus is used here as a parenthetical dash.
- `PzSrmZ-2GqvPe` — `sl/firefox-ios.xliff` — Straight ASCII double quotes used instead of Slovenian quotation marks („ “).
    - Current: `"Pojdi na kopirano povezavo"`
    - Source: `Just to confirm, you wanted ‘Go to Copied Link’?`
    - Suggest: `„Pojdi na kopirano povezavo“`
    - The source uses typographic quotes ‘…’; Slovenian typography requires „…“ rather than straight ASCII quotes.
- `PzSrmZ-eHmH1H` — `sl/firefox-ios.xliff` — Straight ASCII double quotes used instead of Slovenian quotation marks („ “).
    - Current: `"Počisti zasebne zavihke"`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `„Počisti zasebne zavihke“`
    - The source uses typographic quotes ‘…’; Slovenian typography requires „…“ rather than straight ASCII quotes.
- `PzSrmZ-scEmjs` — `sl/firefox-ios.xliff` — Straight ASCII double quotes used instead of Slovenian quotation marks („ “).
    - Current: `"Novo zasebno iskanje"`
    - Source: `Just to confirm, you wanted ‘New Private Search’?`
    - Suggest: `„Novo zasebno iskanje“`
    - The source uses typographic quotes ‘…’; Slovenian typography requires „…“ rather than straight ASCII quotes.
- `PzSrmZ-xRJbBP` — `sl/firefox-ios.xliff` — Straight ASCII double quotes used instead of Slovenian quotation marks („ “).
    - Current: `"Novo iskanje"`
    - Source: `Just to confirm, you wanted ‘New Search’?`
    - Suggest: `„Novo iskanje“`
    - The source uses typographic quotes ‘…’; Slovenian typography requires „…“ rather than straight ASCII quotes.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
