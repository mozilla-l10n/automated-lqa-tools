# Firefox iOS l10n QA — hu

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7e1ae61658ad` |
| **Previous run** | 2026-08-21 @ `7e1ae61658ad` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,906 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for hu: [android](android.md) · [firefox](firefox.md)

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
| Strings | 1,906 |
| Missing strings | 4 |
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

**4 strings** are not translated yet, concentrated in:

- `hu/firefox-ios.xliff` — 4

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 14 | **polish-double** |
| ellipsis | `char` 23 | **char** |
| dash | `en` 6 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (80)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 40 |
| 3 | Degraded language (grammar, spelling, terminology) | 36 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Settings.AppIconSelection.AppIconNames.SystemAuto.Title.v139` — `hu/firefox-ios.xliff` — "System Theme" is rendered only as "Rendszer", dropping "Theme".
    - Current: `Rendszer`
    - Source: `System Theme`
    - Suggest: `Rendszertéma`
    - The source names the icon "System Theme"; the Hungarian omits the "Theme" part.
- `Bookmarks.Menu.EditBookmarkSaveIn.v131` — `hu/firefox-ios.xliff` — "Save in" section label is translated as "Save elsewhere…" with an ellipsis, changing the meaning.
    - Current: `Mentés máshová…`
    - Source: `Save in`
    - Suggest: `Mentés ide:`
    - The source is a section label "Save in" indicating the destination folder, not an action to save somewhere else; the trailing ellipsis also implies a further dialog.
- `Bookmarks.Menu.MoreOptionsA11yLabel.v136` — `hu/firefox-ios.xliff` — "More options" is rendered as "További beállítások" (more settings) instead of more actions/options.
    - Current: `További beállítások`
    - Source: `More options`
    - Suggest: `További lehetőségek`
    - The developer comment says the button opens a modal with more actions; "beállítások" means settings, which is a different concept.
- `ContextualHints.Toolbar.GoogleLens.Description.v154` — `hu/firefox-ios.xliff` — "search what you see" is mistranslated as "search in what you see".
    - Current: `és keressen abban, amit lát`
    - Source: `Use your camera or choose a photo to search what you see.`
    - Suggest: `és keressen rá arra, amit lát`
    - The source means searching for the thing you see (visual search), not searching within it.
- `Addresses.EditAddress.AutofillAddressDepartment.v129` — `hu/firefox-ios.xliff` — "Department" as an administrative division is translated as "Részleg" (organizational unit/department of a company).
    - Current: `Részleg`
    - Source: `Department`
    - Suggest: `Megye (département)`
    - The developer comment specifies an administrative division like in France or Colombia; "Részleg" means a section/unit of an organization, not a territorial division.
- `Addresses.EditAddress.AutofillAddressNeighborhood.v129` — `hu/firefox-ios.xliff` — "Neighborhood" as an address field is translated as "Szomszédság" (the abstract notion of being neighbors).
    - Current: `Szomszédság`
    - Source: `Neighborhood`
    - Suggest: `Városrész`
    - The comment describes a named district/quarter within a city; Hungarian "szomszédság" means proximity/neighborly relation, not a named urban district.
- `Addresses.EditAddress.AutofillAddressPin.v129` — `hu/firefox-ios.xliff` — "Pin" (Postal Index Number used in India) is translated as "Rögzítés" (pinning/fastening).
    - Current: `Rögzítés`
    - Source: `Pin`
    - Suggest: `PIN-kód (irányítószám)`
    - The developer comment states this is the PIN (Postal Index Number) field used in India, a postal code, not the act of pinning.
- `Addresses.EditAddress.AutofillAddressState.v129` — `hu/firefox-ios.xliff` — "State" (administrative division) is translated as "Állapot" (condition/status).
    - Current: `Állapot`
    - Source: `State`
    - Suggest: `Állam`
    - The developer comment says this is the state field of an address, especially in the USA. "Állapot" means status/condition, not a federal state.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `hu/firefox-ios.xliff` — The analytics tracker count label was translated as "Tracking content" instead of a wording matching the source's meaning.
    - Current: `Nyomkövető tartalom: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Analitikai követők: %@`
    - The developer comment says this shows how many analytics trackers were blocked; the Hungarian says "tracking content" which is a different tracker category shown separately in ETP.
- `FirefoxHomepage.Pocket.Footer.Title.v116` — `hu/firefox-ios.xliff` — "Powered by %1$@" is rendered as a literal "under the hood" phrase that does not convey the source meaning.
    - Current: `A motorháztető alatt: %1$@.`
    - Source: `Powered by %1$@. Part of the %2$@ family.`
    - Suggest: `Működteti: %1$@.`
    - The en-US "Powered by Pocket" means the content is provided/powered by Pocket; "A motorháztető alatt" ("under the bonnet") is a literal, misleading rendering.
- `MainMenu.Account.SyncError.Title.v131` — `hu/firefox-ios.xliff` — The source says sign back in to sync, not to sign in to a product called "Sync".
    - Current: `Jelentkezzen be újra a Syncbe`
    - Source: `Sign back in to sync`
    - Suggest: `Jelentkezzen be újra a szinkronizáláshoz`
    - en-US "Sign back in to sync" means signing in again so syncing resumes; the Hungarian turns "sync" into a destination product name, and elsewhere in this file "sync" is rendered "szinkronizálás".
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `hu/firefox-ios.xliff` — "your top sites" is translated as "kedvenc webhelyeit" (favorite sites) instead of "top sites" (leggyakoribb/leglátogatottabb webhelyeit).
    - Current: `megtalálja a kedvenc webhelyeit`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `megtalálja a leggyakrabban látogatott webhelyeit`
    - "Top sites" is an established Firefox feature term (Kiemelt/leggyakrabban látogatott oldalak), not "favorites"; "kedvenc" suggests bookmarks/favorites, which are listed separately in the same sentence.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `hu/firefox-ios.xliff` — "and that you use it" is rendered as "hogyan használja" (how you use it), changing the meaning.
    - Current: `hogy miként fedezte fel, és hogyan használja a %1$@ot`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `hogy miként fedezte fel a %1$@ot, és hogy használja azt`
    - The source only shares the fact that the user uses the app, not how they use it; the translation overstates the data shared.
- `Onboarding.Modern.BrandRefresh.Sync.Description.v148` — `hu/firefox-ios.xliff` — "on any device" mistranslated as "bármely eszközről" (from any device) instead of "bármely eszközön".
    - Current: `bármely eszközről`
    - Source: `Grab bookmarks, passwords, and more on any device in a snap. Your personal data stays safe and secure with encryption.`
    - Suggest: `bármely eszközön`
    - The source says bookmarks and passwords are available on any device, not retrieved from another device.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `hu/firefox-ios.xliff` — "won’t sell you out" rendered as "nem adja el" (won't sell it), losing the object/meaning of not betraying the user.
    - Current: `és nem adja el`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `és nem árulja el Önt`
    - The en-US means the browser will not betray/sell out the user; "nem adja el" without an object reads as "doesn't sell it" and loses the meaning.
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `hu/firefox-ios.xliff` — "your top sites" translated as "kedvenc webhelyeit" (favorite sites) instead of the established "leggyakoribb oldalak"/"top webhelyek" term.
    - Current: `megtalálja a kedvenc webhelyeit`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `megtalálja a leggyakoribb webhelyeit`
    - "Top sites" is a specific Firefox feature (most visited sites), not "favorites"; the translation also adds "megtalálja" which is not in the source.
- `Onboarding.Welcome.Action.v114` — `hu/firefox-ios.xliff` — "Get Started" rendered as a noun phrase "Kezdő lépések" (First steps) rather than a call to action.
    - Current: `Kezdő lépések`
    - Source: `Get Started`
    - Suggest: `Kezdés`
    - The developer comment says this is a button to continue onboarding; "Kezdő lépések" means "first steps/getting started guide", not the action "Get started".
- `PasswordGenerator.Title.v132` — `hu/firefox-ios.xliff` — "Use a strong password?" is translated as a statement-like question meaning "Are you using a strong password?" rather than offering to use one.
    - Current: `Erős jelszót használ?`
    - Source: `Use a strong password?`
    - Suggest: `Erős jelszót használ ehhez?`
    - The source offers the user the generated password; "Erős jelszót használ?" reads as asking whether the user currently uses a strong password, not as a proposal.
- `PrivacyDashboard.TotalTrackersBlockedSince.v155` — `hu/firefox-ios.xliff` — The footer translation replaces the meaning with "%1$@ pieces since %2$@", dropping the sense conveyed by the source's "since" footer wording.
    - Current: `%1$@ darab %2$@ óta 🎉`
    - Source: `%1$@ since %2$@ 🎉`
    - Suggest: `%1$@ %2$@ óta 🎉`
    - The source is "%1$@ since %2$@"; adding "darab" injects a word not in the source and reads oddly with a date-based footer.
- `Addresses.Settings.ListItemA11y.v130` — `hu/firefox-ios.xliff` — Singular "Address for %@" is rendered as plural "Címek" (addresses).
    - Current: `Címek a következőhöz: %@`
    - Source: `Address for %@`
    - Suggest: `Cím a következőhöz: %@`
    - The source is singular "Address for %@" — the accessibility label for one address list item; the Hungarian uses the plural "Címek".
- `Addresses.Settings.Switch.Description.v124` — `hu/firefox-ios.xliff` — "Includes phone numbers and email addresses" is translated as a nominal "inclusion of..." phrase rather than a statement that it includes them.
    - Current: `Telefonszámok és e-mail-címek belevétele`
    - Source: `Includes phone numbers and email addresses`
    - Suggest: `Tartalmazza a telefonszámokat és e-mail-címeket`
    - The source is a descriptive statement telling the user that the feature includes phone numbers and email addresses; the Hungarian reads like a toggle title "Including phone numbers and email addresses".
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `hu/firefox-ios.xliff` — The translation drops "AI" from "AI enhancements", saying only "new or current improvements".
    - Current: `nem fogja látni a %@ új vagy jelenlegi fejlesztéseit`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `nem fogja látni a %@ új vagy jelenlegi MI funkcióbővítéseit`
    - Source says "new or current AI enhancements in %@"; the Hungarian omits the AI qualifier, and other strings in this section render it as "MI funkcióbővítések".
- `Settings.AIControls.BlockedInformation.v151` — `hu/firefox-ios.xliff` — "Unblock specific features below" is expanded into an inaccurate instruction about "controls below".
    - Current: `Egy adott funkció blokkolásának feloldásához használja az alábbi vezérlőket.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Az egyes funkciók blokkolását alább oldhatja fel.`
    - The source is a short imperative "Unblock specific features below"; the translation adds "use the controls below", which is not in the source.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `hu/firefox-ios.xliff` — A toggle label describing a feature is rendered as an imperative instruction to the user.
    - Current: `Görgessen a lap és címsáv elrejtéséhez`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Görgetés a lap és a címsáv elrejtéséhez`
    - The source "Scroll to Hide Tab and Address Bar" is the title of a settings option (a feature name), not a command telling the user to scroll; Hungarian settings titles use the nominal form.
- `Settings.Summarize.GesturesSection.FooterTitle.v142` — `hu/firefox-ios.xliff` — Singular "a page" rendered as plural "lapokat" (pages).
    - Current: `hogy összegezze a lapokat`
    - Source: `Shake your device from side to side to summarize a page.`
    - Suggest: `hogy összegezzen egy oldalt`
    - Source says "to summarize a page" (singular); the Hungarian says "summarize the pages". Also the feature elsewhere in this file uses "oldal" (Oldalak összegzése), not "lap".
- `Settings.Translation.AutoTranslate.Footer.v151` — `hu/firefox-ios.xliff` — "top preferred language" mistranslated as "legtöbbször előnyben részesített" (most often preferred).
    - Current: `a legtöbbször előnyben részesített nyelvére`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `az első helyen előnyben részesített nyelvére`
    - "Top" here refers to the highest-ranked entry in the preferred languages list, not frequency of preference.
- `TabTray.TabsSelectorSyncedTabsTitle.v140` — `hu/firefox-ios.xliff` — The tab-tray selector title "Sync" (synced tabs section) is rendered as the action "Szinkronizálás".
    - Current: `Szinkronizálás`
    - Source: `Sync`
    - Suggest: `Szinkronizált`
    - The developer comment says it is the title of the button to look at synced tabs, a section label, not an action to perform syncing.
- `TermsOfUse.RemindMeLaterButton.v142` — `hu/firefox-ios.xliff` — "Remind Me Later" is translated as "Figyelmeztetés később" (Warning later) instead of a reminder.
    - Current: `Figyelmeztetés később`
    - Source: `Remind Me Later`
    - Suggest: `Emlékeztessen később`
    - 'Remind' is 'emlékeztet' in Hungarian; 'figyelmeztetés' means warning/alert, changing the meaning of the postpone button.
- `TermsOfUse.Title.v142` — `hu/firefox-ios.xliff` — "We've got an update" is rendered as "Van egy hírünk" (We have news), losing the meaning of an update.
    - Current: `Van egy hírünk`
    - Source: `We’ve got an update`
    - Suggest: `Van egy frissítésünk`
    - The developer comment says the title indicates that there is an update to the terms of use; the Hungarian says only that there is 'news'.
- `TermsOfUse.TitleValue2.v147` — `hu/firefox-ios.xliff` — "A note from %@" is translated as "Jegyzet innen: %@", using 'note' in the sense of a written memo/source location rather than a message from the app.
    - Current: `Jegyzet innen: %@`
    - Source: `A note from %@`
    - Suggest: `Üzenet a %@ csapatától`
    - The source means a short message from the product (e.g., Firefox); "Jegyzet innen:" reads as a note originating from a location and is misleading.
- `Translations.LanguagePicker.PageTranslatedTitle.v151` — `hu/firefox-ios.xliff` — "Page Translated to %@" is translated without the subject "page".
    - Current: `Lefordítva erre: %@`
    - Source: `Page Translated to %@`
    - Suggest: `Az oldal lefordítva erre: %@`
    - The source title states that the page has been translated to a language; the Hungarian omits "Page", leaving an ambiguous fragment as an action sheet title.
- `WorldCup.GroupPhase.GroupStageLabel.v151` — `hu/firefox-ios.xliff` — "Group Stage" is rendered with a plural noun, producing "Stage of the group rounds" instead of the singular phase name.
    - Current: `Csoportkörök szakasza`
    - Source: `Group Stage`
    - Suggest: `Csoportkör`
    - The source is a single phase label ("Group Stage"); the Hungarian plural genitive construction says "phase of the group rounds", which is not the same designation.
- `WorldCup.HomepageWidget.EliminatedTeamSection.Title.v151` — `hu/firefox-ios.xliff` — The question loses the "still want to" sense, asking "Are you still following?" instead of "Do you still want to follow along?".
    - Current: `Még mindig követi?`
    - Source: `Still want to Follow Along?`
    - Suggest: `Továbbra is követné?`
    - en-US asks whether the user still wants to follow along after their team was eliminated; the Hungarian states an ongoing action rather than the desire/intent.
- `WorldCup.HomepageWidget.SettingsButtonAccessibilityLabel.v151` — `hu/firefox-ios.xliff` — "More options" is translated as "További beállítások" (More settings) instead of options.
    - Current: `További beállítások`
    - Source: `More options`
    - Suggest: `További lehetőségek`
    - The source says "More options", not "More settings"; the panel is a more-options panel per the developer comment.
- `ExternalLink.AppStore.GenericConfirmationTitle` — `hu/firefox-ios.xliff` — The confirmation question is rendered as a statement-like phrasing that reverses the subject/word order used for questions, unlike the parallel App Store string.
    - Current: `Egy külső alkalmazásban nyitja meg ezt a hivatkozást?`
    - Source: `Open this link in external app?`
    - Suggest: `Megnyitja ezt a hivatkozást egy külső alkalmazásban?`
    - The source asks "Open this link in external app?"; the parallel string ExternalLink.AppStore.ConfirmationTitle uses "Megnyitja ezt a hivatkozást az App Store appban?". The current word order shifts the focus to "in an external app" rather than asking whether to open the link, and is inconsistent with the sibling string.
- `SentTab.ViewAction.title` — `hu/firefox-ios.xliff` — "View" as an action label is translated as the noun "Nézet" instead of the verb "Megtekintés".
    - Current: `Nézet`
    - Source: `View`
    - Suggest: `Megtekintés`
    - The developer comment states this is a label for an action used to view tabs, so a verbal noun is required, not "Nézet" (a view/layout).
- `Settings.Home.Option.Wallpaper.Accessibility.TwilightHillsWallpaper.v100` — `hu/firefox-ios.xliff` — "twilight hills" is rendered as "napnyugtai dombok" (sunset hills) instead of twilight/dusk.
    - Current: `napnyugtai dombok minta`
    - Source: `Firefox wallpaper, twilight hills pattern.`
    - Suggest: `alkonyati dombok minta`
    - The en-US says "twilight hills"; "napnyugta" means sunset, and the parallel wallpaper string already uses "napkelte" for sunrise, so twilight should be "alkonyat".
- `Settings.Home.Option.Wallpaper.UpdatedToastButton` — `hu/firefox-ios.xliff` — "View" translated as the noun "Nézet" although the comment states it is a verb (the action of seeing the wallpaper).
    - Current: `Nézet`
    - Source: `View`
    - Suggest: `Megtekintés`
    - The developer comment explicitly says to consider View as a verb — dismissing settings and seeing the wallpaper; "Nézet" is the noun "view/layout".
- `Settings.OpenWith.PageTitle` — `hu/firefox-ios.xliff` — "Open mail links with" is rendered as "E-mail-hivatkozások társítása" (associating mail links), losing the "open with" meaning.
    - Current: `E-mail-hivatkozások társítása`
    - Source: `Open mail links with`
    - Suggest: `E-mail-hivatkozások megnyitása ezzel`
    - The source is a title preceding the chosen mail app: "Open mail links with". "Társítása" means "associating", which is a different action.
- `Wallpaper.Download.Error.Body.v106` — `hu/firefox-ios.xliff` — "your download" was translated as "a letöltésével" (its download), losing the possessive reference to the user.
    - Current: `Valami hiba történt a letöltésével.`
    - Source: `Something went wrong with your download.`
    - Suggest: `Valami hiba történt a letöltéssel.`
    - The source says "Something went wrong with your download." The Hungarian third-person possessive suffix -ével makes it "with its download", which refers to nothing.
- `No logins found` — `hu/firefox-ios.xliff` — "No logins found" translated as "Nincsenek bejelentkezések", dropping the "found" (search result) meaning.
    - Current: `Nincsenek bejelentkezések`
    - Source: `No logins found`
    - Suggest: `Nem találhatók bejelentkezések`
    - The comment says the label is displayed when no logins are found after searching; the parallel string NoLoginsFound.Title.v122 correctly uses "Nem találhatók jelszavak".

### C. Grammar, agreement & spelling

- `ContextualHints.MainMenu.NewMenu.Body.v132` — `hu/firefox-ios.xliff` — Missing comma before the subordinate clause "amire szüksége van".
    - Current: `Találja meg gyorsabban amire szüksége van`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `Találja meg gyorsabban, amire szüksége van`
    - Hungarian orthography requires a comma before a subordinate clause introduced by "amire".
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `hu/firefox-ios.xliff` — Suffix attached to a placeholder without a hyphen: "%1$@ot" should be "%1$@-ot".
    - Current: `a %1$@ot`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `a %1$@-ot`
    - Hungarian orthography requires a hyphen when adding a case suffix to a proper name/placeholder whose form is unknown.
- `Onboarding.Modern.BrandRefresh.Notification.Title.v148` — `hu/firefox-ios.xliff` — Suffix appended directly to the app-name placeholder without a hyphen, producing e.g. "Firefoxszal" instead of the required "Firefoxszal"/"Firefox-szal" form and dropping the space.
    - Current: `%@szal`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `%@-szal`
    - In Hungarian, case suffixes attached to foreign/proper brand names in UI placeholders must be joined with a hyphen; "%@szal" also fails for any app name not ending in a consonant sound matching -szal (e.g. "Focus"). The en-US is "stay safer with %@".
- `Onboarding.Modern.Sync.Title.v145` — `hu/firefox-ios.xliff` — Missing hyphen before the case suffix attached to the app-name placeholder.
    - Current: `Vigye el a %@ot`
    - Source: `Take %@ on all your browsing adventures`
    - Suggest: `Vigye el a %@-ot`
    - In Hungarian, a suffix appended to a proper name/placeholder ending in a non-Hungarian form requires a hyphen (e.g. „Firefoxot” is written „%@-ot” when the name comes from a placeholder). Other strings in the same file avoid direct suffixing; here „%@ot” produces incorrect output such as „Firefoxot” only by accident and is orthographically wrong with a placeholder.
- `Onboarding.Notification.Description.v120` — `hu/firefox-ios.xliff` — Case suffix attached to the app-name placeholder without a hyphen.
    - Current: `a %@ban`
    - Source: `Securely send tabs between your devices and discover other privacy features in %@.`
    - Suggest: `a %@-ban`
    - A suffix added to a placeholder holding a brand name must be separated with a hyphen in Hungarian orthography.
- `Onboarding.Notification.Title.v120` — `hu/firefox-ios.xliff` — Missing hyphen before the instrumental suffix attached to the app-name placeholder.
    - Current: `%@szal`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `%@-szal`
    - In Hungarian, a suffix appended to a proper/brand name placeholder must be joined with a hyphen (e.g. „Firefox-szal”); „%@szal” produces „Firefoxszal” which is incorrect for a brand name and the pattern is inconsistent with other strings.
- `PrivacyDashboard.HeaderLabel.v155` — `hu/firefox-ios.xliff` — Plural header "Trackers blocked this week" is translated in singular form without agreement.
    - Current: `Nyomkövető blokkolva a héten`
    - Source: `Trackers blocked this week`
    - Suggest: `nyomkövető blokkolva a héten`
    - The label follows a bold number above it, so it should read as a continuation (lowercase, e.g. "12 / nyomkövető blokkolva a héten"); capitalized standalone "Nyomkövető" reads as an isolated singular noun.
- `Settings.Rollouts.Message.v148` — `hu/firefox-ios.xliff` — Awkward/incorrect passive construction "távolról vannak alkalmazva" for "Changes applied remotely".
    - Current: `A módosítások távolról vannak alkalmazva.`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `A módosítások távolról kerülnek alkalmazásra.`
    - The "van + -va/-ve" passive with a transitive verb is a grammatical error in Hungarian; the state-passive is not licensed here.
- `Settings.Translation.PreferredLanguages.Footer.v151` — `hu/firefox-ios.xliff` — "when translating" rendered as "fordítás közben" (during translation) instead of "fordításkor".
    - Current: `Válasszon a következő nyelvek közül fordítás közben.`
    - Source: `Choose from these languages when translating.`
    - Suggest: `Fordításkor ezek közül a nyelvek közül választhat.`
    - The source means the listed languages are the choices offered when a translation is performed; "fordítás közben" (while translating) shifts the meaning slightly and reads awkwardly.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v134` — `hu/firefox-ios.xliff` — Missing hyphen before the case suffix attached to the placeholder.
    - Current: `%1$@ %2$@ból 🦊 küldve.`
    - Source: `%1$@ Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%1$@ A(z) %2$@-ból 🦊 küldve.`
    - In Hungarian a case ending appended to a variable/proper name placeholder must be joined with a hyphen (e.g. %2$@-ból); writing "%2$@ból" is ungrammatical, and the vowel harmony is unpredictable for an unknown app name.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v137` — `hu/firefox-ios.xliff` — Missing hyphen before the case suffix attached to the placeholder.
    - Current: `A %2$@ból 🦊 küldve.`
    - Source: `%1$@  Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `A(z) %2$@-ból 🦊 küldve.`
    - A case ending appended to a placeholder must be joined with a hyphen in Hungarian; "%2$@ból" is ungrammatical.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v134` — `hu/firefox-ios.xliff` — Missing hyphen before the case suffix attached to the placeholder.
    - Current: `%1$@ %2$@ból 🦊 küldve.`
    - Source: `%1$@ Sent from %2$@ 🦊 %3$@`
    - Suggest: `%1$@ A(z) %2$@-ból 🦊 küldve.`
    - A case ending appended to a placeholder must be separated with a hyphen in Hungarian; "%2$@ból" is ungrammatical.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v137` — `hu/firefox-ios.xliff` — Missing hyphen before the case suffix attached to the placeholder.
    - Current: `A %2$@ból 🦊 küldve.`
    - Source: `%1$@  Sent from %2$@ 🦊 %3$@`
    - Suggest: `A(z) %2$@-ból 🦊 küldve.`
    - A case ending appended to a placeholder must be joined with a hyphen in Hungarian; "%2$@ból" is ungrammatical.
- `TermsOfUse.LearnMoreHere.v147` — `hu/firefox-ios.xliff` — The sentence built with the 'here' link renders as "Itt többet megtudhat." with a mid-sentence capitalized link and awkward word order.
    - Current: `%@ többet megtudhat.`
    - Source: `You can learn more %@.`
    - Suggest: `További tudnivalókat %@ talál.`
    - Source is "You can learn more %@." where %@ is the lowercase link word 'here'. The Hungarian places the link at sentence start, forcing the link text to be capitalized ("Itt"), which conflicts with the lowercase source link and produces an unnatural sentence.
- `BreachAlerts.Description` — `hu/firefox-ios.xliff` — Duplicated article "a a" in the Hungarian text.
    - Current: `ellopták őket a a legutóbbi megváltoztatása óta`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `ellopták őket a legutóbbi megváltoztatása óta`
    - Typo: the definite article "a" is repeated.
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `hu/firefox-ios.xliff` — Wrong case of the pronoun: "követik Ön" should be "követik Önt" (accusative).
    - Current: `Ezek a sütik követik Ön oldalról oldalra`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `Ezek a sütik oldalról oldalra követik Önt`
    - The object of "követik" must be in the accusative case (Önt); "követik Ön" is ungrammatical.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `hu/firefox-ios.xliff` — Missing possessive suffix: "a böngészője és számítógép beállításai" lacks agreement.
    - Current: `A böngészője és számítógép beállításai egyediek.`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `A böngészője és számítógépe beállításai egyediek.`
    - The source says "your browser and computer"; the possessive must apply to both nouns (számítógépe).
- `Search.ThirdPartyEngines.AddSuccess` — `hu/firefox-ios.xliff` — Missing initial letter in "szolgáltatás" (typo).
    - Current: `Keresési zolgáltatás hozzáadva!`
    - Source: `Added Search engine!`
    - Suggest: `Keresési szolgáltatás hozzáadva!`
    - "zolgáltatás" is a misspelling of "szolgáltatás".
- `Settings.DisplayTheme.SwitchSubtitle` — `hu/firefox-ios.xliff` — Misspelled word "fényessének" instead of "fényességének".
    - Current: `fényessének`
    - Source: `Switch automatically based on screen brightness`
    - Suggest: `fényességének`
    - "fényesség" + possessive suffix is "fényességének"; the current form is a typo.
- `Settings.ShowLinkPreviews.Title` — `hu/firefox-ios.xliff` — Missing compound-word hyphenation/joining in "Hivatkozás előnézetek".
    - Current: `Hivatkozás előnézetek megjelenítése`
    - Source: `Show Link Previews`
    - Suggest: `Hivatkozás-előnézetek megjelenítése`
    - In Hungarian a compound noun of two nouns must be written as one word or hyphenated, not as two separate words.
- `TranslationToastHandler.PromptTranslate.Title` — `hu/firefox-ios.xliff` — Missing hyphen before the suffix appended to the placeholder for the language name.
    - Current: `Lefordítja %2$@ra`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `Lefordítja %2$@-ra`
    - In Hungarian, a suffix attached directly to a variable/placeholder must be joined with a hyphen; "%2$@ra" renders as e.g. "magyarra" only by luck and is ungrammatical/unreadable for other values.
- `Open & Fill` — `hu/firefox-ios.xliff` — Inconsistent grammatical form: "Megnyitás és kitöltése" mixes a nominal form with a possessive-suffixed one.
    - Current: `Megnyitás és kitöltése`
    - Source: `Open & Fill`
    - Suggest: `Megnyitás és kitöltés`
    - The source is "Open & Fill", two parallel actions; the Hungarian second verb carries a 3rd-person possessive suffix (-e) with no antecedent, so the phrase is ungrammatical.
- `Turns private mode on or off` — `hu/firefox-ios.xliff` — Missing accusative case ending on the object "privát mód".
    - Current: `Ki- vagy bekapcsolja a privát mód`
    - Source: `Turns private mode on or off`
    - Suggest: `Ki- vagy bekapcsolja a privát módot`
    - The Hungarian direct object of "kapcsolja" requires the accusative suffix -ot; "a privát mód" is ungrammatical here.
- `fi3W24-2GqvPe` — `hu/firefox-ios.xliff` — Wrong definite article before a vowel-initial quoted phrase ("a Ugrás" instead of "az Ugrás").
    - Current: `a „Ugrás a másolt hivatkozáshoz”`
    - Source: `There are ${count} options matching ‘Go to Copied Link’.`
    - Suggest: `az „Ugrás a másolt hivatkozáshoz”`
    - Hungarian requires "az" before words starting with a vowel; the quoted item begins with "U".
- `fi3W24-scEmjs` — `hu/firefox-ios.xliff` — Wrong definite article before a vowel-initial quoted phrase ("a Új" instead of "az Új").
    - Current: `a „Új privát keresés”`
    - Source: `There are ${count} options matching ‘New Private Search’.`
    - Suggest: `az „Új privát keresés”`
    - Hungarian requires "az" before words starting with a vowel; the quoted item begins with "Ú".
- `fi3W24-xRJbBP` — `hu/firefox-ios.xliff` — Wrong definite article before a vowel-initial quoted phrase ("a Új" instead of "az Új").
    - Current: `a „Új keresés”`
    - Source: `There are ${count} options matching ‘New Search’.`
    - Suggest: `az „Új keresés”`
    - Hungarian requires "az" before words starting with a vowel; the quoted item begins with "Ú".

### D. Terminology, register & consistency

- `Settings.AppIconSelection.SectionNames.More.Title.v139` — `hu/firefox-ios.xliff` — Section heading "More" translated as "Több" (quantitative more) instead of "Egyéb"/"További".
    - Current: `Több`
    - Source: `More`
    - Suggest: `Egyéb`
    - The comment says this heading covers all other miscellaneous icon variants; Hungarian "Több" means "more (in quantity)" and is not used as a section heading for additional/other items.
- `LoginsHelper.PromptSavePassword.Title.v122` — `hu/firefox-ios.xliff` — Inconsistent phrasing with the parallel username prompt on the same screen.
    - Current: `Menti a jelszót?`
    - Source: `Save password?`
    - Suggest: `Jelszó mentése?`
    - The sibling string LoginsHelper.PromptSaveLogin.Title.v122 ("Save username?") uses the nominal form "Felhasználónév mentése?"; the same construction should be used for "Save password?", as is also done in the update prompts ("Jelszó frissítése?").
- `PrivacyDashboard.SocialTrackers.v155` — `hu/firefox-ios.xliff` — "Social Media Trackers" is rendered with "követők" while the other tracker labels on the same screen use "nyomkövető".
    - Current: `Közösségimédia-követők`
    - Source: `Social Media Trackers`
    - Suggest: `Közösségimédia-nyomkövetők`
    - On the same Privacy Dashboard screen, "trackers" is translated as "nyomkövető" (Webhelyek közötti nyomkövető sütik, Nyomkövető tartalom, Nyomkövető blokkolva a héten); "követők" is inconsistent and can read as "followers".
- `Summarizer.RetryButton.Accessibility.Label.v145` — `hu/firefox-ios.xliff` — Uses "összefoglalás" while the rest of the screen consistently uses "összegzés" for summary/summarize.
    - Current: `Weboldal összefoglalásának újrapróbálása`
    - Source: `Retry to summarize web page`
    - Suggest: `Weboldal összegzésének újrapróbálása`
    - All other Summarizer strings translate summary/summarize as "összegzés"; this inconsistent term appears on the same screen.
- `Summarizer.TabSnapshot.Accessibility.Label.v145` — `hu/firefox-ios.xliff` — Uses "összefoglaló" while the rest of the screen consistently uses "összegzés" for summary.
    - Current: `az összefoglaló bezárásához`
    - Source: `Drag or tap the web page to close the summary`
    - Suggest: `az összegzés bezárásához`
    - The same screen (e.g. Summarizer.CloseButton.Accessibility.Label) renders "summary" as "összegzés"; this term is inconsistent.
- `Translations.LanguagePicker.Title.v151` — `hu/firefox-ios.xliff` — The language picker title "Translate Page to…" is rendered identically to the "Translating page" loading labels, losing the "to…" target-language sense.
    - Current: `Oldal fordítása…`
    - Source: `Translate Page to…`
    - Suggest: `Oldal fordítása erre:…`
    - The source is "Translate Page to…", an action sheet title introducing a list of target languages; the Hungarian drops "to" and collides with Translations.Sheet.LoadingButton / Toolbar.Translation.LoadingButton which use the same wording for "Translating page".
- `Settings.TrackingProtectionOption.BasicBlockList.Status` — `hu/firefox-ios.xliff` — "Standard" is rendered as "Szokásos" here but as "Normál" in the sibling option string on the same screen.
    - Current: `Szokásos`
    - Source: `Standard`
    - Suggest: `Normál`
    - Settings.TrackingProtectionOption.BasicBlockList translates "Standard (default)" as "Normál (alapértelmezett)"; the status label for the same option must use the same term.
- `TodayWidget.QuickActionsGalleryTitleV2` — `hu/firefox-ios.xliff` — "Shortcuts" rendered as "indítóikonok" (launcher icons) instead of the standard "parancsikonok".
    - Current: `Firefox indítóikonok`
    - Source: `Firefox Shortcuts`
    - Suggest: `Firefox parancsikonok`
    - en-US "Firefox Shortcuts" refers to shortcuts, normally "parancsikonok" in Hungarian; "indítóikon" is a nonstandard term and is inconsistent with "Webhelyindítók" used for the same source word elsewhere in the same file.
- `TodayWidget.TopSitesGalleryTitleV2` — `hu/firefox-ios.xliff` — "Website Shortcuts" translated as "Webhelyindítók", inconsistent with the "indítóikonok"/"parancsikonok" term used for Shortcuts elsewhere in the file.
    - Current: `Webhelyindítók`
    - Source: `Website Shortcuts`
    - Suggest: `Webhely-parancsikonok`
    - The same source term "Shortcuts" is rendered three different ways in this file; "Webhelyindítók" (website launchers) does not convey "shortcuts".

### E. Typography, punctuation & spacing

- `Onboarding.Modern.BrandRefresh.TermsOfUse.ManagePreferenceAgreement.v148` — `hu/firefox-ios.xliff` — Superfluous comma between the adverbial phrase and the subject.
    - Current: `A böngésző fejlesztése érdekében, a %1$@`
    - Source: `To help improve the browser, %1$@ sends diagnostic and interaction data to %2$@. %3$@`
    - Suggest: `A böngésző fejlesztése érdekében a %1$@`
    - Hungarian punctuation does not place a comma after an introductory adverbial phrase like this; the comma is an anglicism.
- `TermsOfUse.Link.HereText.v147` — `hu/firefox-ios.xliff` — The inline link word 'here' is capitalized as "Itt" although it is inserted inside a sentence.
    - Current: `Itt`
    - Source: `here`
    - Suggest: `itt`
    - The developer comment states this is the link text for 'here' within the sentence 'You can learn more here.', so it should not be capitalized mid-sentence.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `hu/firefox-ios.xliff` — Missing comma after the interjection "Kérjük" in the Hungarian sentence.
    - Current: `Kérjük frissítse.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `Kérjük, frissítse.`
    - Hungarian punctuation requires a comma after "Kérjük" when it introduces a request clause.
- `DefaultBrowserCard.Button.v2` — `hu/firefox-ios.xliff` — Missing comma before the subordinate clause in "Tudja meg hogyan".
    - Current: `Tudja meg hogyan`
    - Source: `Learn How`
    - Suggest: `Tudja meg, hogyan`
    - Hungarian orthography requires a comma before the conjunction "hogyan" introducing the clause.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/hu/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._
