# Firefox iOS l10n QA — cs

| | |
|---|---|
| **Generated** | 2026-09-14 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8f5aca68ae4b` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `8f5aca68ae4b` |
| **Previous run** | 2026-09-14 @ `e8592a898dc1` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 1,922 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

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

## 3. Open findings (93)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

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
| 2 | Wrong content (says something other than the English) | 53 |
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
- `Created %@` — `cs/firefox-ios.xliff` — "Created" is translated as "Uloženo" (Saved).
    - Current: `Uloženo %@`
    - Source: `Created %@`
    - Suggest: `Vytvořeno %@`
    - The developer comment says the label describes when the login was created, not saved.
- _…and 6 more; see `state/` for the full list._

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
