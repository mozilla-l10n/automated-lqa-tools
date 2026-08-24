# Firefox iOS l10n QA — cs

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `a2ecb0a822be` |
| **Previous run** | 2026-08-22 @ `112744e9d020` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,910 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for cs: [android](android.md) · [firefox](firefox.md)

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
| Strings | 1,910 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
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
| ellipsis | `char` 20 | **char** |
| dash | `em` 1, `en` 2 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (65)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 42 |
| 3 | Degraded language (grammar, spelling, terminology) | 19 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Logins.DevicePasscodeRequired.Message.v122` — `cs/firefox-ios.xliff` — "passwords" translated as "přihlašovacích údajů" (login credentials).
    - Current: `automatické vyplňování přihlašovacích údajů`
    - Source: `To save and automatically fill passwords, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `automatické vyplňování hesel`
    - The source says "passwords"; the rest of the feature strings use "hesla", and "přihlašovací údaje" corresponds to logins/credentials.
- `Addresses.EditAddress.AutofillAddressNeighborhood.v129` — `cs/firefox-ios.xliff` — "Neighborhood" as an address field is mistranslated as "Sousedství" (the abstract concept of neighbourliness/proximity), not a city district.
    - Current: `Sousedství`
    - Source: `Neighborhood`
    - Suggest: `Čtvrť`
    - The field asks for the name of a neighbourhood/district within a city; Czech uses "Čtvrť" (or "Městská část"). "Sousedství" means proximity/neighbourliness and is not an address component.
- `Addresses.EditAddress.AutofillAddressOrganization.v129` — `cs/firefox-ios.xliff` — "Organization" is rendered as "Společnost" (company), narrowing the meaning.
    - Current: `Společnost`
    - Source: `Organization`
    - Suggest: `Organizace`
    - The comment says the field holds the organization's name, which may be any organization, not only a commercial company; Czech has the direct equivalent "Organizace".
- `Menu.EnhancedTrackingProtection.Certificates.IssuerOrganization.v131` — `cs/firefox-ios.xliff` — "Organization" translated as "Společnost" (company) instead of "Organizace".
    - Current: `Společnost`
    - Source: `Organization`
    - Suggest: `Organizace`
    - The certificate field is the issuer Organization (O); the Czech term is "Organizace", not "Společnost" (company).
- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNamesDNSName.v131` — `cs/firefox-ios.xliff` — "DNS Name" translated as "Záznam DNS" (DNS record).
    - Current: `Záznam DNS`
    - Source: `DNS Name`
    - Suggest: `Název DNS`
    - The certificate field is a DNS name of the subject, not a DNS record; "Záznam" means record.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `cs/firefox-ios.xliff` — "Tracking content" is translated as "Sledující obsah" (content that tracks/watches) instead of the standard Firefox term "Sledovací obsah".
    - Current: `Sledující obsah: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Sledovací obsah: %@`
    - The active participle "sledující" means "watching"; the established Czech Firefox term for tracking content is "sledovací obsah", consistent with "sledovací prvky" used elsewhere in this file.
- `FirefoxHomepage.FeltPrivacyUI.Title.v122` — `cs/firefox-ios.xliff` — The translation drops "on this device" and changes the imperative to a third-person statement.
    - Current: `Nezanechá stopy`
    - Source: `Leave no traces on this device`
    - Suggest: `Nezanechávejte na tomto zařízení žádné stopy`
    - Source is "Leave no traces on this device"; the Czech omits "on this device" and renders it as "(It) leaves no traces".
- `CloseTab.ArrivingNotification.title.v133` — `cs/firefox-ios.xliff` — The notification title is mistranslated: %1$@ is the app name, and the Czech turns it into the app closing tabs rather than "tabs closed in <app>: <count>".
    - Current: `%1$@ zavřel panely: %2$@`
    - Source: `%1$@ tabs closed: %2$@`
    - Suggest: `Panely zavřené v prohlížeči %1$@: %2$@`
    - Source "%1$@ tabs closed: %2$@" means tabs were closed in the named app (%1$@ = app name, %2$@ = number of tabs); the Czech reads "Firefox closed tabs: <number>" attributing the action to the app and losing the count relation.
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `cs/firefox-ios.xliff` — "save actions" (actions for saving) is mistranslated as "ukládání akcí" (saving of actions).
    - Current: `od anonymního prohlížení po ukládání akcí`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `od anonymního prohlížení po akce ukládání`
    - The source lists features from private browsing to save actions (i.e. actions that save content); the Czech genitive reverses the relation and says "saving actions".
- `MainMenu.SettingsSection.AccessibilityLabels.CustomizeHomepage.v132` — `cs/firefox-ios.xliff` — "Customize Homepage" is rendered only as "Přizpůsobit", dropping the object of the accessibility label.
    - Current: `Přizpůsobit`
    - Source: `Customize Homepage`
    - Suggest: `Přizpůsobit domovskou stránku`
    - The accessibility label must state the target (Customize Homepage); "Přizpůsobit" alone means merely "Customize" and loses the content.
- `MainMenu.Submenus.Tools.AccessibilityLabels.Zoom.Subtitle.v132` — `cs/firefox-ios.xliff` — "Zoom" (page zoom) is translated as "Zvětšit okno" (enlarge window), which names the wrong object and conflicts with the related Zoom strings.
    - Current: `Zvětšit okno`
    - Source: `Zoom`
    - Suggest: `Zvětšení stránky`
    - The developer comment states this is the Zoom tool that applies zoom on a page, not a window; other strings in the same submenu use "Zvětšení stránky".
- `MainMenu.Submenus.Tools.Zoom.Subtitle.v131` — `cs/firefox-ios.xliff` — "Zoom" is rendered as "Zvětšit okno" (enlarge window) instead of page zoom, inconsistent with the sibling Zoom title strings.
    - Current: `Zvětšit okno`
    - Source: `Zoom`
    - Suggest: `Zvětšení stránky`
    - The comment says this subtitle is for the Zoom tool (zoom on a page); "okno" (window) is the wrong object and the same screen uses "Zvětšení stránky".
- `Onboarding.IntroDescriptionPart1.v114` — `cs/firefox-ios.xliff` — "For good." is rendered as "Navždy." (forever), losing the intended "for the good of all / for good causes" meaning.
    - Current: `Nezávislý. Neziskový. Navždy.`
    - Source: `Indie. Non-profit. For good.`
    - Suggest: `Nezávislý. Neziskový. Pro dobrou věc.`
    - In the source "For good." pairs with "Indie. Non-profit." and means acting for the common good, not "forever".
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `cs/firefox-ios.xliff` — %2$@ is the company name (Mozilla), but the Czech calls it "aplikace" (the app).
    - Current: `s marketingovými partnery aplikace %2$@`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `s marketingovými partnery společnosti %2$@`
    - The developer comment states %2$@ is the company name (e.g. Mozilla); labelling it as an application is wrong content.
- `Onboarding.Modern.Customization.Toolbar.Top.Action.v140` — `cs/firefox-ios.xliff` — "Top" (position of the toolbar) is rendered as directional "Nahoru" (upwards) instead of locative "Nahoře" (at the top).
    - Current: `Nahoru`
    - Source: `Top`
    - Suggest: `Nahoře`
    - The option describes where the toolbar is placed; the parallel option is "Dole" (at the bottom) and the v145 variant of the same string correctly uses "Nahoře". "Nahoru" means "upwards" (direction).
- `Onboarding.Modern.Sync.Title.v145` — `cs/firefox-ios.xliff` — "on all your browsing adventures" is reduced to "za dobrodružstvím", dropping "all your browsing".
    - Current: `Vydejte se s aplikací %@ za dobrodružstvím`
    - Source: `Take %@ on all your browsing adventures`
    - Suggest: `Vydejte se s aplikací %@ za všemi svými dobrodružstvími při prohlížení`
    - The source emphasizes taking the app along on all browsing adventures; the translation omits both "all" and "browsing".
- `Onboarding.Modern.TermsOfService.Description.v145` — `cs/firefox-ios.xliff` — "trusted for over 20 years" is rendered as "které důvěřujete" (which you have trusted), changing the meaning and attributing trust to the individual user.
    - Current: `Přináší nezisková organizace %@, které důvěřujete již více než 20 let`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `Přináší nezisková organizace %@, které se důvěřuje již více než 20 let`
    - The source says the non-profit has been trusted (generally, by people) for over 20 years, not that the reader personally has trusted it for 20 years.
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `cs/firefox-ios.xliff` — "Manage settings" is translated as just "Nastavení" (Settings), dropping the verb.
    - Current: `Nastavení`
    - Source: `Manage settings`
    - Suggest: `Spravovat nastavení`
    - The v145 source changed from "Manage" to "Manage settings"; the Czech only says "Settings", losing the manage action.
- `Onboarding.Wallpaper.Description.v114` — `cs/firefox-ios.xliff` — "a wallpaper that speaks to you" mistranslated as "tapetu, která vás vyjadřuje" (a wallpaper that expresses you).
    - Current: `Vyberte si tapetu, která vás vyjadřuje.`
    - Source: `Choose a wallpaper that speaks to you.`
    - Suggest: `Vyberte si tapetu, která vás osloví.`
    - The English means a wallpaper that appeals to/resonates with the user; "která vás vyjadřuje" says the wallpaper expresses the user, which is a different statement and ungrammatical in sense.
- `Onboarding.Welcome.Link.Action.v114` — `cs/firefox-ios.xliff` — "privacy notice" (singular document) rendered as plural "oznámeních o ochraně osobních údajů", inconsistent with the term used elsewhere in the same file.
    - Current: `Další informace naleznete v našich oznámeních o ochraně osobních údajů`
    - Source: `Learn more in our privacy notice`
    - Suggest: `Další informace naleznete v našich zásadách ochrany osobních údajů`
    - The source refers to one document, the Privacy Notice; the same file translates "Privacy Notice" as "Zásady ochrany osobních údajů" (Onboarding.TermsOfService.PrivacyNoticeLink.v135). The plural "oznámeních" is both wrong in number and terminologically inconsistent.
- `PrivacyDashboard.CrossSiteTrackers.v155` — `cs/firefox-ios.xliff` — "Cross-Site" is dropped, so the label no longer distinguishes cross-site tracking cookies.
    - Current: `Sledovací cookies`
    - Source: `Cross-Site Tracking Cookies`
    - Suggest: `Sledovací cookies mezi weby`
    - Source is "Cross-Site Tracking Cookies"; the Czech omits the cross-site qualifier, which is the key distinguishing part of this Privacy Dashboard category.
- `CreditCard.Settings.EmptyListTitle.v122` — `cs/firefox-ios.xliff` — Plural "Cards" rendered as singular "platební kartu" and "do aplikace" added.
    - Current: `Uložit platební kartu do aplikace %@`
    - Source: `Save Cards to %@`
    - Suggest: `Uložit platební karty do %@`
    - en-US "Save Cards to %@" is plural; the Czech says "save a payment card" (singular). Compare the parallel address string "Uložit adresy do %@".
- `Settings.Studies.Message.v148` — `cs/firefox-ios.xliff` — The translation says quality is improved "for it" (the app) rather than "for everyone", and the subject of testing is wrong.
    - Current: `%@ náhodně vybírá uživatele, aby otestoval nové funkce, s cílem zlepšit jeho kvalitu pro všechny.`
    - Source: `%@ randomly selects users to test features, which improves quality for everyone.`
    - Suggest: `%@ náhodně vybírá uživatele, aby otestovali nové funkce, což zlepšuje kvalitu pro všechny.`
    - Source: "randomly selects users to test features, which improves quality for everyone." The Czech singular "aby otestoval" makes the app the tester instead of the users, and "zlepšit jeho kvalitu" adds a possessive not in the source.
- `TabsTray.SyncTabs.SyncTabsButton.Title.v119` — `cs/firefox-ios.xliff` — "Sync Tabs" is rendered as just "Synchronizovat", dropping the object "tabs".
    - Current: `Synchronizovat`
    - Source: `Sync Tabs`
    - Suggest: `Synchronizovat panely`
    - The source button label is "Sync Tabs"; the Czech omits "panely", losing the specific meaning of syncing tabs.
- `Toolbar.NewTab.Button.v142` — `cs/firefox-ios.xliff` — The imperative action label "Summarize page" is translated as the noun "Shrnutí stránky" (page summary).
    - Current: `Shrnutí stránky`
    - Source: `Summarize page`
    - Suggest: `Shrnout stránku`
    - Source is a verb phrase describing the button action; Czech renders it as a noun, and it also collides with "Souhrn stránky" usage elsewhere.
- `WebCompatReporter.Preview.Data.IsTablet.v155` — `cs/firefox-ios.xliff` — "Whether or not your device is a tablet" mistranslated as "Bez ohledu na to, zda..." ("Regardless of whether...").
    - Current: `Bez ohledu na to, zda je vaše zařízení tablet`
    - Source: `Whether or not your device is a tablet`
    - Suggest: `Zda je vaše zařízení tablet`
    - The bullet lists the data sent: whether the device is a tablet. "Bez ohledu na to" means "regardless of", which changes the meaning.
- `WorldCup.HomepageWidget.RoundPhase.WinWorldCupLabel.v151` — `cs/firefox-ios.xliff` — "2026 WORLD CUP CHAMPIONS" is rendered as "MISTROVSTVÍ SVĚTA 2026" (World Cup 2026), dropping the "champions" meaning.
    - Current: `MISTROVSTVÍ SVĚTA 2026`
    - Source: `2026 WORLD CUP CHAMPIONS`
    - Suggest: `MISTŘI SVĚTA 2026`
    - The label marks the championship winner; the Czech text names the tournament instead of the champions.
- `This action will clear all of your private data, including history from your synced devices.` — `cs/firefox-ios.xliff` — "all of your private data" is translated as "všechna vaše data", dropping "private".
    - Current: `Tato akce smaže všechna vaše data, včetně historie prohlížení ze všech synchronizovaných zařízení.`
    - Source: `This action will clear all of your private data, including history from your synced devices.`
    - Suggest: `Tato akce smaže všechna vaše soukromá data, včetně historie prohlížení ze synchronizovaných zařízení.`
    - The source says "private data"; omitting it overstates the scope of the deletion.
- `DefaultBrowserCard.Button.v2` — `cs/firefox-ios.xliff` — "Learn How" is translated as "Zjistit více" (Learn more) instead of how to do it.
    - Current: `Zjistit více`
    - Source: `Learn How`
    - Suggest: `Zjistit jak`
    - The source and comment specify a button to learn how to set the default browser, not a generic "learn more".
- `DefaultBrowserCard.Description` — `cs/firefox-ios.xliff` — The Czech says links, e-mails and messages open in Firefox, but the source says links from websites, e-mails and Messages open in Firefox.
    - Current: `Nastavte si automatické otevírání odkazů, e-mailů a zpráv ve Firefoxu.`
    - Source: `Set links from websites, emails, and Messages to open automatically in Firefox.`
    - Suggest: `Nastavte si automatické otevírání odkazů z webových stránek, e-mailů a Zpráv ve Firefoxu.`
    - In the source, "from websites, emails, and Messages" modifies "links" — it is the source of the links, not three kinds of items being opened.
- `LibraryPanel.History.AllTimeOption.v138` — `cs/firefox-ios.xliff` — "All Time" as a time-range option is rendered "Po celý čas" (for the whole time) instead of "Vše"/"Od počátku".
    - Current: `Po celý čas`
    - Source: `All Time`
    - Suggest: `Vše`
    - The option is one of a list of time ranges (Last hour, Last 24 hours…); "Po celý čas" is not the Czech idiom for the all-time range.
- `Firefox.HomePage.Title` — `cs/firefox-ios.xliff` — "Firefox Home Page" translated as just "Výchozí" (Default), losing the meaning.
    - Current: `Výchozí`
    - Source: `Firefox Home Page`
    - Suggest: `Domovská stránka Firefoxu`
    - The source names the Firefox home page shown in the tab history list; "Výchozí" means "Default" and does not convey it.
- `FirefoxHomepage.JumpBackIn.TabPickup.OpenTab.A11y.v106` — `cs/firefox-ios.xliff` — Singular "synced tab" rendered as plural "synchronizované panely".
    - Current: `Otevřít synchronizované panely`
    - Source: `Open synced tab`
    - Suggest: `Otevřít synchronizovaný panel`
    - The accessibility action opens one specific synced tab; en-US is singular "Open synced tab".
- `Menu.AddToShortcuts.v99` — `cs/firefox-ios.xliff` — "Add to Shortcuts" is rendered as "Add shortcut", losing the target destination and breaking consistency with the "Přidáno do zkratek" toast.
    - Current: `Přidat zkratku`
    - Source: `Add to Shortcuts`
    - Suggest: `Přidat do zkratek`
    - The source says the page is pinned to the Shortcuts section; the confirmation toast Menu.AddPin.Confirm2 uses "Přidáno do zkratek".
- `Menu.CustomizeHomePage.v99` — `cs/firefox-ios.xliff` — "Customize Homepage" translated only as "Přizpůsobit", dropping the homepage object.
    - Current: `Přizpůsobit`
    - Source: `Customize Homepage`
    - Suggest: `Přizpůsobit domovskou stránku`
    - The source specifies what is being customized (the Firefox Home page); the Czech is a bare "Customize" with no object, and no length limit is noted in the comment.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `cs/firefox-ios.xliff` — "in the Reader View controls" mistranslated as "v ovládání seznamu ke čtení" (reading list controls).
    - Current: `v ovládání seznamu ke čtení`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `v ovládacích prvcích zobrazení čtečky`
    - The source says the icon is in the Reader View controls, not the reading list controls.
- `UIMenuItem.SearchWithFirefox` — `cs/firefox-ios.xliff` — The brand name Firefox is dropped from the text-selection menu item.
    - Current: `Vyhledat`
    - Source: `Search with Firefox`
    - Suggest: `Vyhledat pomocí Firefoxu`
    - en-US is "Search with Firefox"; the Czech only says "Search", losing the product name.
- `You don’t have any tabs open in Firefox on your other devices.` — `cs/firefox-ios.xliff` — Translation omits "in Firefox" from the error message.
    - Current: `Ve vašich zařízeních nejsou otevřené žádné panely.`
    - Source: `You don’t have any tabs open in Firefox on your other devices.`
    - Suggest: `Ve Firefoxu na vašich dalších zařízeních nejsou otevřené žádné panely.`
    - The source specifies tabs open in Firefox on your other devices; the Czech drops both "in Firefox" and "other".
- `Created %@` — `cs/firefox-ios.xliff` — "Created" is translated as "Uloženo" (Saved) instead of "Vytvořeno".
    - Current: `Uloženo %@`
    - Source: `Created %@`
    - Suggest: `Vytvořeno %@`
    - The label describes when the login was created; "Uloženo" means "Saved", a different notion than the source "Created".
- `Logins will be removed from all connected devices.` — `cs/firefox-ios.xliff` — "connected devices" rendered as "synchronizovaných zařízení" (synced devices).
    - Current: `ze všech synchronizovaných zařízení`
    - Source: `Logins will be removed from all connected devices.`
    - Suggest: `ze všech připojených zařízení`
    - The source says "all connected devices"; the Czech says "all synced devices", which is a different term (the separate synced-devices string exists in DeleteLoginAlert.Message.Synced.v122).
- `Website` — `cs/firefox-ios.xliff` — "Website" translated as "Server" instead of "Webová stránka".
    - Current: `Server`
    - Source: `Website`
    - Suggest: `Webová stránka`
    - The label sits above the website row in the login detail view; "Server" names a different thing than "Website".
- `TodayWidget.TopSitesGalleryDescription` — `cs/firefox-ios.xliff` — "frequently and recently visited sites" translated with "nebo" (or) instead of "a" (and).
    - Current: `často nebo nedávno navštěvované stránky`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `často a nedávno navštěvované stránky`
    - The source uses "and", the Czech uses "nebo" (or), changing the meaning.

### C. Grammar, agreement & spelling

- `Engagement.Notification.Title.v112` — `cs/firefox-ios.xliff` — Imperative "Start your first search" rendered as future indicative "Začnete" instead of imperative "Začněte".
    - Current: `Začnete své první vyhledávání`
    - Source: `Start your first search`
    - Suggest: `Začněte své první vyhledávání`
    - The en-US is an imperative call to action; "Začnete" is the 2nd person plural future indicative ("you will start"), a typo for the imperative "Začněte".
- `CloseTab.ViewAction.title.v133` — `cs/firefox-ios.xliff` — Action label rendered as a noun ("Zobrazení") instead of an imperative verb for a button action.
    - Current: `Zobrazení nedávno zavřených panelů`
    - Source: `View recently closed tabs`
    - Suggest: `Zobrazit nedávno zavřené panely`
    - The developer comment says this is a label for an action; en-US "View recently closed tabs" is a verb phrase, and Czech action labels use the infinitive/imperative.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `cs/firefox-ios.xliff` — Mismatched constructions: finite verb "Souhlasím" coordinated with infinitive "pokračovat".
    - Current: `Souhlasím a pokračovat`
    - Source: `Agree and continue`
    - Suggest: `Souhlasit a pokračovat`
    - Czech button labels must be grammatically consistent; "Souhlasím a pokračovat" mixes 1st-person indicative with an infinitive, which is ungrammatical.
- `CreditCard.SnackBar.UpdatedCardLabel.v122` — `cs/firefox-ios.xliff` — Subject–verb agreement error: "Informace" (plural) with singular verb form.
    - Current: `Informace o kartě byla aktualizována`
    - Source: `Card Information Updated`
    - Suggest: `Informace o kartě byly aktualizovány`
    - "Informace o kartě" is plural here; the predicate must agree: "byly aktualizovány".
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v134` — `cs/firefox-ios.xliff` — Inconsistent/incorrect participle form "Odeslané" instead of "Odesláno" as used in the parallel strings.
    - Current: `Odeslané z aplikace`
    - Source: `%1$@ Sent from %2$@ 🦊 %3$@`
    - Suggest: `Odesláno z aplikace`
    - The other "Sent from %2$@" strings use the impersonal "Odesláno"; "Odeslané" is an adjectival plural form that does not agree with anything here.
- `ContextualHints.Summarize.Description.v142` — `cs/firefox-ios.xliff` — Awkward duplication "zobrazíte zobrazení čtečky" and it repeats "Klepnutím" for "Touch and hold".
    - Current: `Klepnutím a podržením zobrazíte zobrazení čtečky.`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `Dotykem a podržením otevřete režim čtečky.`
    - The en-US "Touch and hold for Reader View" is rendered with a redundant repetition ("zobrazíte zobrazení"), degrading the language.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `cs/firefox-ios.xliff` — Missing comma before "nebo" in the correlative "buď … nebo" construction and clumsy wording.
    - Current: `Tato stránka je buď s omezením nebo se jedná převážně o vizuální stránku.`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `Tato stránka může být omezená, nebo se jedná převážně o vizuální obsah.`
    - Czech punctuation requires a comma before "nebo" in the "buď…, nebo…" pair; the phrase "je buď s omezením" is also ungrammatical.
- `CreditCard.RememberCard.SecondaryButtonTitle.v116` — `cs/firefox-ios.xliff` — Subject–predicate agreement error: plural "informace" takes plural verb form.
    - Current: `Informace o kartě byla aktualizována`
    - Source: `Card Information Updated`
    - Suggest: `Informace o kartě byly aktualizovány`
    - En-US "Card Information Updated" is rendered with the plural noun "informace" but a singular participle/verb; Czech requires "byly aktualizovány".
- `ReaderMode.Available.VoiceOverAnnouncement` — `cs/firefox-ios.xliff` — Gender agreement error: adjective "dostupný" does not agree with neuter noun "Zobrazení".
    - Current: `Je dostupný Zobrazení čtečky`
    - Source: `Reader Mode available`
    - Suggest: `Je dostupné zobrazení čtečky`
    - "Zobrazení" is neuter, so the predicate adjective must be "dostupné", not masculine "dostupný".
- `Tabs %@ to %@ of %@` — `cs/firefox-ios.xliff` — Plural noun rendered in singular: "Panel" should be "Panely" for a range of tabs.
    - Current: `Panel %1$@ až %2$@ ze %3$@`
    - Source: `Tabs %1$@ to %2$@ of %3$@`
    - Suggest: `Panely %1$@ až %2$@ z %3$@`
    - The source "Tabs %1$@ to %2$@ of %3$@" refers to multiple visible tabs; Czech uses the singular "Panel", which is grammatically wrong for a range.
- `Well, this is embarrassing.` — `cs/firefox-ios.xliff` — Ungrammatical rendering of "Well, this is embarrassing."
    - Current: `Ale toto je nepříjemné.`
    - Source: `Well, this is embarrassing.`
    - Suggest: `No, to je ale nepříjemné.`
    - "Ale toto je nepříjemné." is not idiomatic Czech word order for the interjection "Well,"; it reads as a broken sentence.
- `When Leaving Private Browsing` — `cs/firefox-ios.xliff` — Settings label starts with a lowercase letter although it is a standalone UI label.
    - Current: `po opuštění anonymního prohlížení`
    - Source: `When Leaving Private Browsing`
    - Suggest: `Po opuštění anonymního prohlížení`
    - The source "When Leaving Private Browsing" is a setting label displayed in Settings; Czech sentence capitalization requires an initial capital letter.

### D. Terminology, register & consistency

- `AddressToolbar.GoogleLens.A11yLabel.v153.v2` — `cs/firefox-ios.xliff` — Accessibility label is rendered as an imperative addressed to the user instead of a noun-style label describing the button.
    - Current: `Vyhledejte obrázek pomocí Google Lens`
    - Source: `Search image with Google Lens`
    - Suggest: `Vyhledat obrázek pomocí Google Lens`
    - The en-US "Search image with Google Lens" is a button label; other button labels in this file use the infinitive (e.g. "Pořídit fotografii"), not the 2nd-person imperative.
- `AddressToolbar.SearchEngine.A11y.Label.v128` — `cs/firefox-ios.xliff` — "Search Engine" is translated as "Vyhledávací modul" while the neighbouring string uses "vyhledávač".
    - Current: `Vyhledávací modul: %@`
    - Source: `Search Engine: %@`
    - Suggest: `Vyhledávač: %@`
    - AddressToolbar.SearchEngine.A11y.Hint.v133 in the same file renders "search engine" as "vyhledávač"; the same term on the same control should be consistent.
- `PrimaryButton.Label.v112` — `cs/firefox-ios.xliff` — Button uses "průzkum" while the body text of the same popup calls it "dotazník", an inconsistent term for "survey" on one screen.
    - Current: `Vyplnit průzkum`
    - Source: `Take Survey`
    - Suggest: `Vyplnit dotazník`
    - Body.Text.v112 translates "survey" as "dotazník"; the button on the same popup must use the same term.
- `TermsOfUse.Link.PrivacyNotice.v142` — `cs/firefox-ios.xliff` — "Privacy Notice" is translated as "Zásady ochrany osobních údajů" here but as "Oznámení o ochraně osobních údajů" in the description on the same sheet.
    - Current: `Zásady ochrany osobních údajů`
    - Source: `Privacy Notice`
    - Suggest: `Oznámení o ochraně osobních údajů`
    - The same source term "Privacy Notice" appears in TermsOfUse.Description.v142 as "Oznámení o ochraně osobních údajů"; the link label must match on the same screen.
- `TermsOfUse.TermsOfUseHasOpened.v142` — `cs/firefox-ios.xliff` — Uses "Podmínkami používání" while every other string in the same file uses "Podmínky použití".
    - Current: `Přehled s Podmínkami používání byl otevřen`
    - Source: `Terms of Use sheet opened`
    - Suggest: `Panel s Podmínkami použití byl otevřen`
    - Terminology inconsistency for "Terms of Use" within the same screen (cf. TermsOfUse.TitleValue1.v147 "Podmínky použití").
- `Enter passcode` — `cs/firefox-ios.xliff` — "passcode" is translated as "heslo" (password) instead of the device passcode term.
    - Current: `Zadejte heslo`
    - Source: `Enter passcode`
    - Suggest: `Zadejte kód`
    - The string refers to the numeric passcode, which is distinct from a password (heslo) elsewhere in the UI.
- `TodayWidget.PrivateTabButtonLabelV1` — `cs/firefox-ios.xliff` — "Private" is rendered as "Soukromé" instead of the consistently used "anonymní" terminology.
    - Current: `Soukromé vyhledávání`
    - Source: `Private Search`
    - Suggest: `Anonymní vyhledávání`
    - Throughout the batch (and Firefox cs) "private" in the private browsing context is translated as "anonymní" (Anonymní panely, Anonymní prohlížení, Anonymní režim); "Soukromé" is inconsistent terminology on the same widget screen that also uses "Zavřít anonymní panely".

### E. Typography, punctuation & spacing

- `Bookmarks.Menu.DeletedBookmark.v131` — `cs/firefox-ios.xliff` — Uses English-style straight/curly quotes instead of Czech quotation marks used elsewhere in the same file.
    - Current: `Smazáno “%@”`
    - Source: `Deleted “%@”`
    - Suggest: `Smazáno „%@“`
    - Other strings in the same file (Bookmarks.Menu.SavedBookmarkToastLabel.v136) correctly use Czech quotes „…“; here the English closing-style quotes are kept, which is inconsistent typography for cs.
- `ContextualHints.FeltDeletion.Body.v122` — `cs/firefox-ios.xliff` — Em dash from the source replaced with a hyphen surrounded by spaces.
    - Current: `soubory cookie - všechno.`
    - Source: `Tap here to start a fresh private session. Delete your history, cookies — everything.`
    - Suggest: `soubory cookie – všechno.`
    - Czech typography uses an en/em dash (–) for parenthetical breaks, matching the source's em dash; a plain hyphen is incorrect.
- `LiveActivity.Downloads.FileNameText.v138` — `cs/firefox-ios.xliff` — Straight/English quotation marks used instead of Czech quotes.
    - Current: `Stahuje se “%@”`
    - Source: `Downloading “%@”`
    - Suggest: `Stahuje se „%@“`
    - Czech typography requires „…“ quotation marks; the English style “…” was copied from the source.
- `TopSites.RemovePage.Button` — `cs/firefox-ios.xliff` — Em dash of the source replaced with a hyphen.
    - Current: `Odebrat stránku - %@`
    - Source: `Remove page — %@`
    - Suggest: `Odebrat stránku – %@`
    - Source uses an em dash separator; Czech typography requires an en/em dash, not a hyphen, between clauses.

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
