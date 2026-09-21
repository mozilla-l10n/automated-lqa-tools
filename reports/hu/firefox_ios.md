# Firefox iOS l10n QA — hu

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `26f50d4ce7b1` |
| **Previous run** | 2026-09-14 @ `e8592a898dc1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,922 |

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
| Files | 96 |
| Strings | 1,922 |
| Missing strings | 28 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**28 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings` — 22
- `hu/firefox-ios.xliff` — 6

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/QuickAnswers.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 14 | **polish-double** |
| ellipsis | `char` 25 | **char** |
| dash | `en` 6 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (94)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `hu/firefox-ios.xliff` — "that you use it" was rendered as "how you use it", making the product claim it shares usage details with marketing partners.
    - Current: `hogy miként fedezte fel, és hogyan használja a %1$@ot`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `hogy miként fedezte fel a %1$@ot, és hogy használja azt`
    - The en-US says only the fact that the user uses the app is shared ("and that you use it"), not how they use it; the Hungarian asserts that usage behaviour is shared with marketing partners.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `hu/firefox-ios.xliff` — "can be used to track you" rendered as a definite statement "használnak" (they use it), dropping the modality.
    - Current: `amelyet aztán a böngészése követésére használnak`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `amely aztán a böngészése követésére használható`
    - The en-US says the profile "can be used" to track; the Hungarian asserts that it is used, changing what the product states about tracking behaviour.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 40 |
| 3 | Degraded language (grammar, spelling, terminology) | 50 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.Menu.EditBookmarkSaveIn.v131` — `hu/firefox-ios.xliff` — "Save in" section label is translated as "Save elsewhere…" with an ellipsis, changing the meaning.
    - Current: `Mentés máshová…`
    - Source: `Save in`
    - Suggest: `Mentés ide`
    - The source is the label of the folder-selection section ("Save in"), not an action to save somewhere else; the added ellipsis also implies a further dialog.
- `Bookmarks.Menu.MoreOptionsA11yLabel.v136` — `hu/firefox-ios.xliff` — "More options" rendered as "További beállítások" (more settings) instead of more actions/options.
    - Current: `További beállítások`
    - Source: `More options`
    - Suggest: `További lehetőségek`
    - The button opens a modal with more actions, not settings; "beállítások" means settings.
- `ContextualHints.Toolbar.GoogleLens.Description.v154` — `hu/firefox-ios.xliff` — "search what you see" mistranslated as "search in what you see".
    - Current: `keressen abban, amit lát`
    - Source: `Use your camera or choose a photo to search what you see.`
    - Suggest: `keressen rá arra, amit lát`
    - The source means searching for the thing you see, not searching within it.
- `ContextualHints.Translations.Body.v145` — `hu/firefox-ios.xliff` — "when you are" is dropped from the translation.
    - Current: `Gyors, privát fordítások készen állnak.`
    - Source: `Fast, private translations are ready when you are.`
    - Suggest: `A gyors, privát fordítások készen állnak, amint Ön is.`
    - The en-US "ready when you are" phrase is omitted, losing part of the message.
- `Addresses.EditAddress.AutofillAddressNeighborhood.v129` — `hu/firefox-ios.xliff` — "Neighborhood" as an address field is rendered "Szomszédság" (the abstract state of being neighbours) instead of the district/quarter name.
    - Current: `Szomszédság`
    - Source: `Neighborhood`
    - Suggest: `Környék`
    - The comment says users input the name of their neighborhood as part of an address; Hungarian "Szomszédság" denotes neighbourliness/adjacency, not a named locality.
- `Addresses.EditAddress.AutofillAddressPin.v129` — `hu/firefox-ios.xliff` — "Pin" (PIN = Postal Index Number, India) is translated as "Rögzítés" (pinning/fixing).
    - Current: `Rögzítés`
    - Source: `Pin`
    - Suggest: `PIN-kód`
    - The developer comment states Pin is the Postal Index Number used in India, a postal code; "Rögzítés" means "pinning/attaching", which is a different concept entirely.
- `Addresses.EditAddress.AutofillAddressPostTown.v129` — `hu/firefox-ios.xliff` — "Post town" translated as "Postaállomás" (post station/office) instead of the town used for mail sorting.
    - Current: `Postaállomás`
    - Source: `Post town`
    - Suggest: `Postázási település`
    - The comment explains this is the post town used for mail sorting (a locality name), not a postal station/office facility.
- `Addresses.EditAddress.AutofillAddressState.v129` — `hu/firefox-ios.xliff` — "State" as an administrative division is translated as "Állapot" (condition/status) instead of "Állam".
    - Current: `Állapot`
    - Source: `State`
    - Suggest: `Állam`
    - The developer comment says this is the state field of an address (e.g. US states); Hungarian "Állapot" means status/condition, not a territorial state.
- `Addresses.EditAddress.AutofillAddressZip.v129` — `hu/firefox-ios.xliff` — The translation adds "(Amerikai Egyesült Államok)", content not present in the source "ZIP Code".
    - Current: `Irányítószám (Amerikai Egyesült Államok)`
    - Source: `ZIP Code`
    - Suggest: `Irányítószám`
    - The source label is simply "ZIP Code"; the added country qualifier is invented text that appears in the UI field label.
- `Menu.EnhancedTrackingProtection.On.Header.v128` — `hu/firefox-ios.xliff` — "If we spot something" is rendered as "Ha látunk valamit", losing the meaning of detecting a problem/tracker.
    - Current: `Ha látunk valamit, értesíteni fogjuk.`
    - Source: `You’re protected. If we spot something, we’ll let you know.`
    - Suggest: `Ha észlelünk valamit, értesíteni fogjuk.`
    - "spot" means detect/notice something suspicious; "látunk valamit" (we see something) is a weaker, odd rendering that in Hungarian suggests the browser is watching.
- `FirefoxHomepage.Pocket.Footer.Title.v116` — `hu/firefox-ios.xliff` — "Powered by %1$@" is rendered as an idiom about looking under the car hood, which does not convey the source meaning.
    - Current: `A motorháztető alatt: %1$@.`
    - Source: `Powered by %1$@. Part of the %2$@ family.`
    - Suggest: `Működteti: %1$@.`
    - The en-US says the feature is powered by Pocket; "A motorháztető alatt" ("under the hood") is a literal car metaphor that misstates the credit line.
- `Onboarding.Modern.BrandRefresh.Customization.Toolbar.Description.v148` — `hu/firefox-ios.xliff` — "your top sites" is translated as "kedvenc webhelyeit" (favorite sites) instead of the established term for Top Sites.
    - Current: `megtalálja a kedvenc webhelyeit`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `megtalálja a népszerű webhelyeit`
    - "Top sites" is a Firefox feature name rendered elsewhere in hu as "Népszerű webhelyek"; "kedvenc webhelyek" names a different concept.
- `Onboarding.Modern.BrandRefresh.Marketing.Description.v148` — `hu/firefox-ios.xliff` — "that you use it" was rendered as "how you use it", making the product claim it shares usage details with marketing partners.
    - Current: `hogy miként fedezte fel, és hogyan használja a %1$@ot`
    - Source: `Share how you discovered %1$@, and that you use it, with %2$@’s marketing partners. This data is never sold.`
    - Suggest: `hogy miként fedezte fel a %1$@ot, és hogy használja azt`
    - The en-US says only the fact that the user uses the app is shared ("and that you use it"), not how they use it; the Hungarian asserts that usage behaviour is shared with marketing partners.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `hu/firefox-ios.xliff` — "won't sell you out" is rendered as "nem adja el" ("doesn't sell it/you"), losing the sense of betrayal and reading as an incomplete clause.
    - Current: `Gyors, biztonságos, és nem adja el.`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `Gyors, biztonságos, és nem árulja el Önt.`
    - The en-US says the browser won't betray/sell out the user; "nem adja el" has a dangling object and means "doesn't sell (it)".
- `Onboarding.Modern.Customization.Toolbar.Description.v145` — `hu/firefox-ios.xliff` — "your top sites" is translated as "kedvenc webhelyeit" (favorite sites) instead of the established "top sites" term.
    - Current: `megtalálja a kedvenc webhelyeit`
    - Source: `Start typing to get search suggestions, your top sites, bookmarks, history and search engines – all in one place.`
    - Suggest: `megtalálja a népszerű webhelyeit`
    - "Top sites" is a distinct Firefox feature name; "kedvenc" suggests favorites/bookmarks, a different feature also named in the same sentence.
- `Onboarding.Modern.Sync.Description.v140` — `hu/firefox-ios.xliff` — "on any device" translated as "az összes eszközén" (on all your devices).
    - Current: `az összes eszközén`
    - Source: `Get your bookmarks, history, and passwords on any device.`
    - Suggest: `bármely eszközén`
    - The source says "any device", not "all devices"; the parallel string v145 correctly uses "bármely eszközén".
- `Onboarding.Modern.TermsOfService.Description.v145` — `hu/firefox-ios.xliff` — "trusted for over 20 years" rendered as an impersonal "people have trusted it for over 20 years" clause attached ambiguously.
    - Current: `A nonprofit %@ hozza el Önnek, amelyben több mint 20 éve megbíznak`
    - Source: `Automatic protection of your personal info Load sites fast and search smarter Brought to you by the non-profit %@, trusted for over 20 years`
    - Suggest: `A nonprofit %@ hozza el Önnek, amelyben több mint 20 éve megbíznak az emberek`
    - Minor, but the relative clause lacks a subject; the en-US states the organization is trusted. Low-risk rewording.
- `Onboarding.Wallpaper.SelectorTitle.v114` — `hu/firefox-ios.xliff` — "Try a splash of color" translated as "Próbáljon ki egy kis színt", which is an awkward literal rendering.
    - Current: `Próbáljon ki egy kis színt`
    - Source: `Try a splash of color`
    - Suggest: `Vigyen bele egy kis színt`
    - The source invites the user to add a splash of colour to the homepage; the Hungarian literally says "try out a bit of colour", which does not convey the meaning naturally.
- `Onboarding.Welcome.Action.v114` — `hu/firefox-ios.xliff` — "Get Started" rendered as a noun phrase "Kezdő lépések" ("First steps") instead of an action button label.
    - Current: `Kezdő lépések`
    - Source: `Get Started`
    - Suggest: `Kezdés`
    - The comment says this is on a button so the user can continue onboarding; "Kezdő lépések" means "first steps/getting-started guide", not the call to action "Get Started".
- `PasswordGenerator.Title.v132` — `hu/firefox-ios.xliff` — The question "Use a strong password?" is rendered as a statement-like question asking whether the user uses a strong password, not offering to use one.
    - Current: `Erős jelszót használ?`
    - Source: `Use a strong password?`
    - Suggest: `Erős jelszót használ inkább? / Használ erős jelszót?`
    - The source is a prompt offering the generated password. "Erős jelszót használ?" reads as asking about the user's habit; a suggestion like "Erős jelszó használata?" matches the offer.
- `Addresses.Settings.ListItemA11y.v130` — `hu/firefox-ios.xliff` — Singular "Address for %@" rendered as plural "Címek" (addresses).
    - Current: `Címek a következőhöz: %@`
    - Source: `Address for %@`
    - Suggest: `Cím a következőhöz: %@`
    - The source is singular (one address list item); the Hungarian plural says "addresses".
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `hu/firefox-ios.xliff` — "AI enhancements" was rendered as just "fejlesztéseit" (its improvements), dropping the AI qualifier.
    - Current: `nem fogja látni a %@ új vagy jelenlegi fejlesztéseit`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `nem fogja látni a %@ új vagy jelenlegi MI funkcióbővítéseit`
    - The source says "new or current AI enhancements in %@"; the Hungarian omits "AI", and the same term is translated as "MI funkcióbővítések" in the adjacent title and BlockedInformation strings.
- `Settings.AIControls.BlockedInformation.v151` — `hu/firefox-ios.xliff` — The second sentence adds "using the controls below" wording and changes "Unblock specific features below" into an instruction about controls not present in the source.
    - Current: `Egy adott funkció blokkolásának feloldásához használja az alábbi vezérlőket.`
    - Source: `New and current AI enhancements are blocked by default. Unblock specific features below.`
    - Suggest: `Az alábbiakban feloldhatja egyes funkciók blokkolását.`
    - en-US says "Unblock specific features below." — an imperative about unblocking features, not an instruction to use controls below.
- `Settings.Rollouts.Message.v148` — `hu/firefox-ios.xliff` — "Changes applied remotely" rendered with an unnatural/incorrect passive that also shifts the meaning.
    - Current: `A módosítások távolról vannak alkalmazva.`
    - Source: `%@ will improve features, performance, and stability between updates. Changes applied remotely.`
    - Suggest: `A módosítások távolról kerülnek alkalmazásra.`
    - Hungarian "vannak alkalmazva" is an incorrect passive construction (állapotú passzív), degrading the sentence; the source states changes are applied remotely.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `hu/firefox-ios.xliff` — Setting title translated as an imperative instruction instead of a feature name.
    - Current: `Görgessen a lap és címsáv elrejtéséhez`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Görgetés a lap és a címsáv elrejtéséhez`
    - The source is the title of a toggle option naming the feature ("Scroll to Hide Tab and Address Bar"), not a command to the user; Hungarian settings titles use nominal forms.
- `Settings.Summarize.GesturesSection.FooterTitle.v142` — `hu/firefox-ios.xliff` — Singular "a page" is translated as plural "a lapokat" (the pages).
    - Current: `hogy összegezze a lapokat`
    - Source: `Shake your device from side to side to summarize a page.`
    - Suggest: `hogy összegezze az oldalt`
    - The source says "to summarize a page" (one page); the Hungarian says summarize the pages, and also uses "lap" (tab) while the rest of the Summarize section uses "oldal" for page.
- `Settings.Translation.AutoTranslate.Footer.v151` — `hu/firefox-ios.xliff` — "your top preferred language" mistranslated as "the most often preferred language".
    - Current: `a legtöbbször előnyben részesített nyelvére`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `a listán első helyen álló előnyben részesített nyelvére`
    - "top preferred language" means the first/highest-ranked language in the preferred languages list, not the one preferred most often.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `hu/firefox-ios.xliff` — "Limited content detected" mistranslated as "Korlátozott tartalom észlelve" is acceptable, but the second sentence loses "may be restricted" nuance by repeating the same word ambiguously.
    - Current: `Korlátozott tartalom észlelve. Az oldal korlátozott vagy többnyire vizuális lehet.`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `Korlátozott tartalom észlelve. Lehet, hogy az oldal hozzáférése korlátozott, vagy többnyire vizuális tartalmat jelenít meg.`
    - The source distinguishes "limited content" from "restricted" page access; the Hungarian uses "korlátozott" for both, making the message circular.
- `TabTray.TabsSelectorSyncedTabsTitle.v140` — `hu/firefox-ios.xliff` — Source "Sync" is the title of the synced-tabs selector button; "Szinkronizálás" reads as the action of syncing rather than the synced-tabs section.
    - Current: `Szinkronizálás`
    - Source: `Sync`
    - Suggest: `Szinkronizált`
    - The developer comment says it is the title of the button to look at synced tabs, a tab-tray section label alongside "Lapok" (Tabs); the imperative/gerund noun "Szinkronizálás" labels an action instead.
- `TermsOfUse.RemindMeLaterButton.v142` — `hu/firefox-ios.xliff` — "Remind Me Later" translated as "Figyelmeztetés később" (warning later) instead of a reminder.
    - Current: `Figyelmeztetés később`
    - Source: `Remind Me Later`
    - Suggest: `Emlékeztessen később`
    - 'Remind' is 'emlékeztet' in Hungarian; 'figyelmeztetés' means warning, which is a different action.
- `TermsOfUse.Title.v142` — `hu/firefox-ios.xliff` — "We’ve got an update" translated as "Van egy hírünk" (We have some news), losing the reference to an update.
    - Current: `Van egy hírünk`
    - Source: `We’ve got an update`
    - Suggest: `Frissítettük a feltételeinket`
    - The comment states the title indicates there is an update to the terms of use; "hírünk" (news) does not convey 'update'.
- `TermsOfUse.TitleValue2.v147` — `hu/firefox-ios.xliff` — "A note from %@" rendered as "Jegyzet innen: %@", using 'note' in the sense of a written memo/location rather than a message from the app.
    - Current: `Jegyzet innen: %@`
    - Source: `A note from %@`
    - Suggest: `Üzenet a %@ csapatától`
    - %@ is the app name (e.g. Firefox); "Jegyzet innen:" reads as a note originating from a place, not a note from Firefox.
- `Translations.LanguagePicker.PageTranslatedTitle.v151` — `hu/firefox-ios.xliff` — "Page Translated to %@" drops the subject "page".
    - Current: `Lefordítva erre: %@`
    - Source: `Page Translated to %@`
    - Suggest: `Az oldal lefordítva erre: %@`
    - The source explicitly states that the page was translated to the given language; the Hungarian omits "oldal", leaving the subject unstated.
- `Translations.LanguagePicker.Title.v151` — `hu/firefox-ios.xliff` — "Translate Page to…" is rendered as "Oldal fordítása…", dropping the "to" and making it identical to the plain "Translate Page" title.
    - Current: `Oldal fordítása…`
    - Source: `Translate Page to…`
    - Suggest: `Oldal fordítása erre:…`
    - The source is the title of a language picker listing target languages; the "to" is essential and its omission makes the string collide with Translations.Sheet.TitleLabel ("Oldal fordítása") and with the loading label.
- `WorldCup.HomepageWidget.EliminatedTeamSection.Title.v151` — `hu/firefox-ios.xliff` — "Still want to Follow Along?" translated as "Még mindig követi?", changing the meaning from a future intention to a present-state question.
    - Current: `Még mindig követi?`
    - Source: `Still want to Follow Along?`
    - Suggest: `Továbbra is követni szeretné?`
    - The source asks whether the user still wants to follow along (after their team was eliminated); the Hungarian asks whether the user is still following, losing the volitional "want to".
- `WorldCup.HomepageWidget.RoundPhase.WinWorldCupLabel.v151` — `hu/firefox-ios.xliff` — "2026 WORLD CUP CHAMPIONS" drops "World Cup", rendering only "2026-OS VILÁGBAJNOKOK".
    - Current: `2026-OS VILÁGBAJNOKOK`
    - Source: `2026 WORLD CUP CHAMPIONS`
    - Suggest: `2026-OS VILÁGBAJNOKSÁG GYŐZTESEI`
    - The source names the World Cup explicitly; the translation omits the competition name.
- `WorldCup.HomepageWidget.SettingsButtonAccessibilityLabel.v151` — `hu/firefox-ios.xliff` — "More options" is translated as "További beállítások" (More settings).
    - Current: `További beállítások`
    - Source: `More options`
    - Suggest: `További lehetőségek`
    - The source says "More options", not "More settings"; the comment says the button shows more options related to the widget.
- `ErrorPages.CertWarning.Description` — `hu/firefox-ios.xliff` — Subject of "protect your information" is wrong: Hungarian says the site owner protects the user's data, while the source means Firefox protects it.
    - Current: `Hogy megvédje az információit az ellopásuktól, a Firefox nem kapcsolódott ehhez a webhelyhez.`
    - Source: `The owner of %@ has configured their website improperly. To protect your information from being stolen, Firefox has not connected to this website.`
    - Suggest: `Hogy megvédje az információit az ellopástól, a Firefox nem kapcsolódott ehhez a webhelyhez.`
    - The en-US states Firefox has not connected in order to protect the user's information; the Hungarian plural possessive "ellopásuktól" misattributes the theft and reads awkwardly.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `hu/firefox-ios.xliff` — "can be used to track you" rendered as a definite statement "használnak" (they use it), dropping the modality.
    - Current: `amelyet aztán a böngészése követésére használnak`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `amely aztán a böngészése követésére használható`
    - The en-US says the profile "can be used" to track; the Hungarian asserts that it is used, changing what the product states about tracking behaviour.
- `Search.ThirdPartyEngines.FailedMessage` — `hu/firefox-ios.xliff` — Past-tense failure statement rendered as a general present-tense possibility statement.
    - Current: `A keresési szolgáltató nem adható hozzá.`
    - Source: `The search provider could not be added.`
    - Suggest: `A keresési szolgáltatót nem sikerült hozzáadni.`
    - The source reports that adding the search provider failed ("could not be added"); the Hungarian states it cannot be added as a general rule.
- `SentTab.ViewAction.title` — `hu/firefox-ios.xliff` — "View" as an action label is translated as the noun "Nézet" (a view) instead of the verb "Megtekintés".
    - Current: `Nézet`
    - Source: `View`
    - Suggest: `Megtekintés`
    - The developer comment says it is a label for an action used to view tabs, so a verbal noun is required; "Nézet" means a display/view mode.
- `Settings.DisplayTheme.SystemTheme.SectionHeader` — `hu/firefox-ios.xliff` — "System Theme" translated as just "Rendszer" (System), dropping "Theme".
    - Current: `Rendszer`
    - Source: `System Theme`
    - Suggest: `Rendszertéma`
    - The source section title is "System Theme"; the translation omits "Theme", inconsistent with "Browser Theme" → "Böngészőtéma" in the same feature.
- `Settings.Home.Option.Wallpaper.Accessibility.TwilightHillsWallpaper.v100` — `hu/firefox-ios.xliff` — "twilight hills" translated as "napnyugtai dombok" (sunset hills) — but a separate sunrise wallpaper exists; twilight is "alkonyati".
    - Current: `napnyugtai dombok`
    - Source: `Firefox wallpaper, twilight hills pattern.`
    - Suggest: `alkonyati dombok`
    - en-US "twilight hills" means dusk/twilight, not sunset (napnyugta); the pattern name should render twilight.
- `Settings.Home.Option.Wallpaper.UpdatedToastButton` — `hu/firefox-ios.xliff` — "View" translated as the noun "Nézet" although the comment states it is a verb (the action of viewing the wallpaper).
    - Current: `Nézet`
    - Source: `View`
    - Suggest: `Megtekintés`
    - The developer comment explicitly says to consider View as a verb; "Nézet" is the noun "view/layout".
- `Settings.OpenWith.PageTitle` — `hu/firefox-ios.xliff` — "Open mail links with" is rendered as "E-mail-hivatkozások társítása" ("associating email links"), losing the "open with" meaning.
    - Current: `E-mail-hivatkozások társítása`
    - Source: `Open mail links with`
    - Suggest: `E-mail-hivatkozások megnyitása ezzel:`
    - The source is a settings page title asking which app to open mail links with; "társítása" means file/link association, not opening with a chosen app.
- `Settings.SendUsage.Message` — `hu/firefox-ios.xliff` — The Hungarian drops "for everyone" and reverses/alters "provide and improve" into "fejlesztéséhez és támogatásához" (development and support).
    - Current: `csak azt gyűjtse, ami a Firefox fejlesztéséhez és támogatásához szükséges`
    - Source: `Mozilla strives to only collect what we need to provide and improve Firefox for everyone.`
    - Suggest: `csak azt gyűjtse, ami a Firefox mindenki számára való biztosításához és továbbfejlesztéséhez szükséges`
    - en-US says "to provide and improve Firefox for everyone"; the target says "development and support" and omits "for everyone".
- `Swipe right or left with three fingers to close the tab.` — `hu/firefox-ios.xliff` — Direction order reversed: "right or left" rendered as "balra vagy jobbra" (left or right).
    - Current: `legyintsen balra vagy jobbra három ujjal`
    - Source: `Swipe right or left with three fingers to close the tab.`
    - Suggest: `legyintsen jobbra vagy balra három ujjal`
    - The en-US says "Swipe right or left"; the Hungarian reverses the order of the directions.
- `Wallpaper.Download.Error.Body.v106` — `hu/firefox-ios.xliff` — "your download" rendered as "a letöltésével" ("its download"), losing the second-person possessive and introducing a wrong referent.
    - Current: `Valami hiba történt a letöltésével.`
    - Source: `Something went wrong with your download.`
    - Suggest: `Valami hiba történt a letöltéssel.`
    - The en-US says "Something went wrong with your download." The Hungarian suffix -ével makes it "with its download", referring to some unnamed third thing rather than the user's download.
- `No logins found` — `hu/firefox-ios.xliff` — Translation drops "found": "Nincsenek bejelentkezések" means "There are no logins" rather than "No logins found".
    - Current: `Nincsenek bejelentkezések`
    - Source: `No logins found`
    - Suggest: `Nem találhatók bejelentkezések`
    - The label is shown after searching; the source says no logins were found, which the sibling string NoLoginsFound.Title.v122 renders as "Nem találhatók jelszavak".
- `TodayWidget.QuickViewGalleryDescriptionV2` — `hu/firefox-ios.xliff` — "Add shortcuts to your open tabs" translated as adding shortcuts onto the open tabs rather than shortcuts leading to them.
    - Current: `Indítóikonok hozzáadása a nyitott lapokhoz.`
    - Source: `Add shortcuts to your open tabs.`
    - Suggest: `Parancsikonok hozzáadása a nyitott lapjaihoz.`
    - Meaning is shortcuts pointing to open tabs; the Hungarian dative reads as adding icons to the tabs. Also inconsistent with the surrounding widget strings.

### C. Grammar, agreement & spelling

- `FirefoxHomepage.TrackerBlocker.TrackersBlocked.v153b` — `hu/firefox-ios.xliff` — Singular "Nyomkövető" used for a count label that shows a number of blocked trackers.
    - Current: `Nyomkövető blokkolva: %@`
    - Source: `Trackers Blocked: %@`
    - Suggest: `Blokkolt nyomkövetők: %@`
    - The source "Trackers Blocked: %@" is a plural count label; the Hungarian reads as a singular subject with no plural/possessive form, producing awkward output.
- `ContextualHints.MainMenu.NewMenu.Body.v132` — `hu/firefox-ios.xliff` — Missing comma before the subordinate clause "amire szüksége van".
    - Current: `Találja meg gyorsabban amire szüksége van`
    - Source: `Find what you need faster, from private browsing to save actions.`
    - Suggest: `Találja meg gyorsabban, amire szüksége van`
    - Hungarian requires a comma before a subordinate clause introduced by "amire".
- `NativeErrorPage.CellularDataRestricted.Description.v156` — `hu/firefox-ios.xliff` — Missing hyphen before the suffix attached to the app-name placeholder.
    - Current: `a %@hoz`
    - Source: `Connect to Wi-Fi or go to iOS Settings and turn on cellular data for %@.`
    - Suggest: `a %@-hoz`
    - In Hungarian, a suffix appended to a proper name/placeholder such as "Firefox" must be joined with a hyphen when written after a variable (%@-hoz); "%@hoz" is ungrammatical.
- `Onboarding.Modern.Sync.Title.v145` — `hu/firefox-ios.xliff` — Missing hyphen before the suffix attached to the app-name placeholder.
    - Current: `Vigye el a %@ot`
    - Source: `Take %@ on all your browsing adventures`
    - Suggest: `Vigye el a %@-ot`
    - In Hungarian, case suffixes appended to a proper/brand name placeholder must be joined with a hyphen (e.g. „Firefox-ot”); „%@ot” yields „Firefoxot” without the required hyphen and is inconsistent with the locale's placeholder-suffix handling.
- `Onboarding.Notification.Description.v120` — `hu/firefox-ios.xliff` — Missing hyphen before the case suffix appended to the app-name placeholder.
    - Current: `adatvédelmi funkciókat a %@ban`
    - Source: `Securely send tabs between your devices and discover other privacy features in %@.`
    - Suggest: `adatvédelmi funkciókat a %@-ban`
    - Hungarian requires a hyphen when a suffix is attached to a brand name placeholder whose ending is unknown; „%@ban” renders as „Firefoxban” without the hyphen used elsewhere in the locale.
- `Onboarding.Notification.Title.v120` — `hu/firefox-ios.xliff` — Missing hyphen before the case suffix appended to the app-name placeholder.
    - Current: `nagyobb biztonságban lehet %@szal`
    - Source: `Notifications help you stay safer with %@`
    - Suggest: `nagyobb biztonságban lehet a %@-szal`
    - The suffix „-szal” must be joined to the placeholder with a hyphen; „%@szal” produces „Firefoxszal” glued to the placeholder without the hyphen convention.
- `Addresses.Settings.Switch.Description.v124` — `hu/firefox-ios.xliff` — "Includes phone numbers and email addresses" translated as a noun phrase "belevétele" instead of a statement.
    - Current: `Telefonszámok és e-mail-címek belevétele`
    - Source: `Includes phone numbers and email addresses`
    - Suggest: `Tartalmazza a telefonszámokat és az e-mail-címeket`
    - The source is a descriptive statement under the toggle title saying the feature includes phone numbers and email addresses; the Hungarian nominal form reads as an action/option label, changing the meaning.
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v134` — `hu/firefox-ios.xliff` — Placeholder suffix attached without hyphen; Hungarian requires "-ból/-ből" with a hyphen after a placeholder/proper name ending in a non-Hungarian form.
    - Current: `%2$@ból 🦊 küldve`
    - Source: `%1$@ Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `%2$@-ból 🦊 küldve`
    - The app name is substituted at runtime (e.g. Firefox); Hungarian orthography requires a hyphen before the suffix after a foreign proper name ending in a silent/unusual letter, and the same pattern is used elsewhere with "a(z) %@".
- `SentFromFirefox.SocialShare.ShareMessageA.Title.v137` — `hu/firefox-ios.xliff` — Placeholder suffix attached without hyphen.
    - Current: `A %2$@ból 🦊 küldve`
    - Source: `%1$@  Sent from %2$@ 🦊 Try the mobile browser: %3$@`
    - Suggest: `A %2$@-ból 🦊 küldve`
    - The app name is substituted at runtime (e.g. Firefox); Hungarian requires a hyphen when attaching a case suffix to such a foreign proper name.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v134` — `hu/firefox-ios.xliff` — Placeholder suffix attached without hyphen.
    - Current: `%2$@ból 🦊 küldve`
    - Source: `%1$@ Sent from %2$@ 🦊 %3$@`
    - Suggest: `%2$@-ból 🦊 küldve`
    - The app name is substituted at runtime (e.g. Firefox); Hungarian requires a hyphen when attaching a case suffix to such a foreign proper name.
- `SentFromFirefox.SocialShare.ShareMessageB.Title.v137` — `hu/firefox-ios.xliff` — Placeholder suffix attached without hyphen.
    - Current: `A %2$@ból 🦊 küldve`
    - Source: `%1$@  Sent from %2$@ 🦊 %3$@`
    - Suggest: `A %2$@-ból 🦊 küldve`
    - The app name is substituted at runtime (e.g. Firefox); Hungarian requires a hyphen when attaching a case suffix to such a foreign proper name.
- `TermsOfUse.LearnMoreHere.v147` — `hu/firefox-ios.xliff` — Sentence built around the 'here' link is ungrammatical/incomplete in Hungarian and starts with the placeholder link mid-sentence.
    - Current: `%@ többet megtudhat.`
    - Source: `You can learn more %@.`
    - Suggest: `További tudnivalókat %@ talál.`
    - en-US "You can learn more %@." places the link ('here') inside a well-formed sentence; the Hungarian "%@ többet megtudhat." lacks an object/adverbial and does not form a correct sentence with the link text "Itt".
- `BreachAlerts.Description` — `hu/firefox-ios.xliff` — Duplicated article "a a" and dropped reference to "your password" in the first sentence.
    - Current: `ellopták őket a a legutóbbi megváltoztatása óta`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `ellopták őket a jelszava legutóbbi megváltoztatása óta`
    - The source says "since you last changed your password"; the Hungarian has a stray repeated article and no noun for what was changed.
- `Menu.TrackingProtectionDescription.CrossSiteNew` — `hu/firefox-ios.xliff` — Wrong case: "követik Ön oldalról oldalra" should use the accusative "Önt".
    - Current: `Ezek a sütik követik Ön oldalról oldalra`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `Ezek a sütik oldalról oldalra követik Önt`
    - "Follow you" requires the accusative object "Önt" in Hungarian; "követik Ön" is ungrammatical.
- `Menu.TrackingProtectionDescription.Fingerprinters` — `hu/firefox-ios.xliff` — Missing possessive suffix: "a böngészője és számítógép beállításai".
    - Current: `A böngészője és számítógép beállításai egyediek.`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `A böngészője és számítógépe beállításai egyediek.`
    - The source is "your browser and computer"; the second noun lacks the possessive suffix, making the phrase ungrammatical.
- `Search.ThirdPartyEngines.AddSuccess` — `hu/firefox-ios.xliff` — Typo: "zolgáltatás" is missing its initial letter.
    - Current: `Keresési zolgáltatás hozzáadva!`
    - Source: `Added Search engine!`
    - Suggest: `Keresési szolgáltatás hozzáadva!`
    - "szolgáltatás" is misspelled as "zolgáltatás".
- `Settings.DisplayTheme.SwitchSubtitle` — `hu/firefox-ios.xliff` — Misspelling of "fényességének".
    - Current: `a képernyő fényessének függvényében`
    - Source: `Switch automatically based on screen brightness`
    - Suggest: `a képernyő fényességének függvényében`
    - "fényessének" is a typo; the correct genitive form is "fényességének".
- `Tabs Tray` — `hu/firefox-ios.xliff` — "Lapok tálca" is an ungrammatical compound; should be "Lapok tálcája" or "Laptálca".
    - Current: `Lapok tálca`
    - Source: `Tabs Tray`
    - Suggest: `Lapok tálcája`
    - Hungarian noun-noun possessive construction requires the possessive suffix: "Lapok tálcája".
- `There was a problem accessing tabs from your other devices. Try again in a few moments.` — `hu/firefox-ios.xliff` — "your other devices" (plural) rendered as singular "más eszközről".
    - Current: `más eszközről történő elérésekor`
    - Source: `There was a problem accessing tabs from your other devices. Try again in a few moments.`
    - Suggest: `a többi eszközéről történő elérésekor`
    - The source refers to the user's other devices (plural, possessive); the Hungarian says "from another device", losing the plural and possessive.
- `TranslationToastHandler.PromptTranslate.Title` — `hu/firefox-ios.xliff` — Missing hyphen before the case suffix attached to the placeholder: "%2$@ra".
    - Current: `Lefordítja %2$@ra a következővel: %3$@?`
    - Source: `This page appears to be in %1$@. Translate to %2$@ with %3$@?`
    - Suggest: `Lefordítja a következő nyelvre: %2$@, ezzel: %3$@?`
    - A suffix glued directly to a placeholder is ungrammatical; Hungarian requires a hyphen (%2$@-ra) or a restructured sentence, as the vowel harmony and assimilation cannot be predicted.
- `Open & Fill` — `hu/firefox-ios.xliff` — Inconsistent possessive/infinitive agreement: "Megnyitás és kitöltése" mixes a nominal and a possessive form.
    - Current: `Megnyitás és kitöltése`
    - Source: `Open & Fill`
    - Suggest: `Megnyitás és kitöltés`
    - The source is "Open & Fill", two parallel actions; the Hungarian second element carries a possessive suffix (-e) that has no antecedent, breaking agreement with the first noun.
- `Turns private mode on or off` — `hu/firefox-ios.xliff` — Missing accusative case ending on "privát mód".
    - Current: `Ki- vagy bekapcsolja a privát mód`
    - Source: `Turns private mode on or off`
    - Suggest: `Ki- vagy bekapcsolja a privát módot`
    - The object of "bekapcsolja" must be in the accusative: "privát módot". As written the sentence is ungrammatical.
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

- `PrivacyDashboard.SocialTrackers.v155` — `hu/firefox-ios.xliff` — "Social Media Trackers" is translated as "Közösségimédia-követők" while the rest of the screen uses "nyomkövető" for tracker.
    - Current: `Közösségimédia-követők`
    - Source: `Social Media Trackers`
    - Suggest: `Közösségimédia-nyomkövetők`
    - Other rows on the same Privacy Dashboard use "nyomkövető" (Nyomkövető tartalom, nyomkövető sütik, Nyomkövető blokkolva); "követők" is inconsistent terminology on the same screen.
- `QRCode.Toolbar.Button.A11y.Title.v128` — `hu/firefox-ios.xliff` — Accessibility label for a toolbar button is rendered as an imperative sentence instead of a noun phrase label.
    - Current: `Olvassa le a QR-kódot`
    - Source: `Scan QR code`
    - Suggest: `QR-kód beolvasása`
    - The comment says this is the accessibility label of a button; Hungarian UI convention (and the sibling label "Oldal összegzése") uses a nominal form, not an imperative instruction to the user.
- `Settings.Studies.Title.v136` — `hu/firefox-ios.xliff` — "Studies" is rendered as "Tanulmányok" (written papers) instead of the Mozilla term for experiments.
    - Current: `Tanulmányok telepítése és futtatása`
    - Source: `Install and Run Studies`
    - Suggest: `Kísérletek telepítése és futtatása`
    - In Mozilla terminology "Studies" are experiments/trials installed in the browser, not documents; "Tanulmányok telepítése" is nonsensical and inconsistent with the description about trying out features.
- `Summarizer.RetryButton.Accessibility.Label.v145` — `hu/firefox-ios.xliff` — "summarize/summary" rendered as "összefoglalás" here while the rest of the file consistently uses "összegzés".
    - Current: `Weboldal összefoglalásának újrapróbálása`
    - Source: `Retry to summarize web page`
    - Suggest: `Weboldal összegzésének újrapróbálása`
    - Terminology inconsistency within the same screen/file, where "Summarize/Summary" is translated as "összegzés" everywhere else.
- `Summarizer.TabSnapshot.Accessibility.Label.v145` — `hu/firefox-ios.xliff` — "summary" rendered as "összefoglaló" while the rest of the file uses "összegzés".
    - Current: `az összefoglaló bezárásához`
    - Source: `Drag or tap the web page to close the summary`
    - Suggest: `az összegzés bezárásához`
    - Terminology inconsistency within the same feature; Summarizer.CloseButton.Accessibility.Label uses "Összegzés bezárása".
- `TermsOfUse.TermsOfUseHasOpened.v142` — `hu/firefox-ios.xliff` — The UI 'sheet' is translated as "lap", which is the term used for browser tabs elsewhere in this build.
    - Current: `A felhasználási feltételeket tartalmazó lap megnyitva`
    - Source: `Terms of Use sheet opened`
    - Suggest: `A felhasználási feltételek lapja megnyílt`
    - "lap" is consistently used for browser tabs (Lapok, Új lap); using it for the bottom sheet is confusing in an accessibility announcement.
- `Translations.Sheet.ToLabel.v145` — `hu/firefox-ios.xliff` — "To" is translated as "Cél:" while the paired "From" is "Forrásnyelv:", an inconsistent pair on the same sheet.
    - Current: `Cél:`
    - Source: `To`
    - Suggest: `Célnyelv:`
    - The From/To pair on the same bottom sheet should be parallel; "Forrásnyelv:" vs. "Cél:" is inconsistent terminology within one screen.
- `ActivityStream.ContextMenu.AddToShortcuts` — `hu/firefox-ios.xliff` — "Shortcuts" (the homepage Shortcuts section) is rendered as "indítóikonok" (launcher icons) instead of the established "Gyorslinkek/Parancsikonok" term.
    - Current: `Hozzáadás az indítóikonokhoz`
    - Source: `Add to Shortcuts`
    - Suggest: `Hozzáadás a parancsikonokhoz`
    - The source refers to the Firefox home screen "Shortcuts" section; "indítóikonok" names a different concept (home screen launcher icons).
- `Always Send` — `hu/firefox-ios.xliff` — Button label rendered as an imperative/subjunctive verb form instead of the action label "Always Send".
    - Current: `Mindig küldjön`
    - Source: `Always Send`
    - Suggest: `Mindig elküldi`
    - The source is a button label meaning the user chooses to always send crash reports; "Mindig küldjön" reads as telling the user to send, not as the action taken by the app.
- `FirefoxHome.Stories.Minutes.v140` — `hu/firefox-ios.xliff` — The developer comment requires an abbreviated form of "minutes" due to space constraints, but the translation spells out "perc".
    - Current: `%d perc`
    - Source: `min: %d`
    - Suggest: `%d p`
    - Comment: "Minutes should be abbreviated due to space constraints."
- `Open articles in Reader View by tapping the book icon when it appears in the title bar.` — `hu/firefox-ios.xliff` — "tapping" translated as "kattintva" (clicking) on a touch device.
    - Current: `a könyv ikonra kattintva`
    - Source: `Open articles in Reader View by tapping the book icon when it appears in the title bar.`
    - Suggest: `a könyv ikonra koppintva`
    - On iOS "tap" is "koppintás" in Hungarian; "kattintás" means mouse click.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `hu/firefox-ios.xliff` — "tapping" rendered as "kattintva" (clicking) instead of the touch term, and a spurious comma splits the sentence.
    - Current: `Mentse az oldalakat az olvasási listájára, a könyv plusz ikonra kattintva az olvasó nézet vezérlőelemei közt.`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Mentse az oldalakat az olvasási listájára a könyv plusz ikonra koppintva az olvasó nézet vezérlőelemei közt.`
    - On iOS "tap" is "koppintás", not "kattintás"; the inserted comma is also incorrect.
- `Settings.TrackingProtectionOption.BasicBlockList.Status` — `hu/firefox-ios.xliff` — "Standard" is rendered as "Szokásos" here but as "Normál" in the sibling option string on the same screen.
    - Current: `Szokásos`
    - Source: `Standard`
    - Suggest: `Normál`
    - Settings.TrackingProtectionOption.BasicBlockList translates "Standard (default)" as "Normál (alapértelmezett)"; the status label for the same option must use the same term.

### E. Typography, punctuation & spacing

- `Settings.Notifications.TipsAndFeaturesNotificationsStatus.v112` — `hu/firefox-ios.xliff` — Suffix attached to the app-name placeholder without a hyphen.
    - Current: `a legtöbbet a %@ból`
    - Source: `Learn about useful features and how to get the most out of %@.`
    - Suggest: `a legtöbbet a %@-ból`
    - In Hungarian, case suffixes appended to a proper/brand name placeholder require a hyphen (e.g. Firefoxból is written Firefox-ból when attached to a placeholder token); without it the word is misspelled.
- `Settings.Search.Suggest.ShowNonSponsoredSuggestions.Description.v124.v2` — `hu/firefox-ios.xliff` — Suffix attached to the app-name placeholder without a hyphen.
    - Current: `javaslatokat a %@tól`
    - Source: `Get suggestions from %@ related to your search`
    - Suggest: `javaslatokat a %@-tól`
    - A case suffix appended directly to a placeholder holding a brand name needs a hyphen in Hungarian orthography.
- `TermsOfUse.Link.HereText.v147` — `hu/firefox-ios.xliff` — Link text "here" is capitalized mid-sentence.
    - Current: `Itt`
    - Source: `here`
    - Suggest: `itt`
    - The link is inserted inside the sentence 'You can learn more here.', so Hungarian sentence-case rules require lowercase.
- `WorldCup.HomepageWidget.ErrorLabel.v151` — `hu/firefox-ios.xliff` — Missing comma after "Kérjük" in the Hungarian sentence.
    - Current: `Kérjük frissítse.`
    - Source: `We couldn’t load match data. Please refresh.`
    - Suggest: `Kérjük, frissítse.`
    - Hungarian orthography requires a comma after the introductory "Kérjük" before the imperative clause.
- `DefaultBrowserCard.Button.v2` — `hu/firefox-ios.xliff` — Missing comma before the subordinate clause in "Tudja meg hogyan".
    - Current: `Tudja meg hogyan`
    - Source: `Learn How`
    - Suggest: `Tudja meg, hogyan`
    - Hungarian orthography requires a comma before the clause-introducing "hogyan".
- `Settings.SendUsage.Link` — `hu/firefox-ios.xliff` — Final period of "Learn More." is missing, inconsistent with Settings.Studies.Toggle.Link which keeps it.
    - Current: `További tudnivalók`
    - Source: `Learn More.`
    - Suggest: `További tudnivalók.`
    - Source is "Learn More." with a period; the parallel string Settings.Studies.Toggle.Link translates it as "További tudnivalók."

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

### Fixed to date (0)

_Nothing fixed yet._
