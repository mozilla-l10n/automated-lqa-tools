# Firefox iOS l10n QA — pl

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

Also for pl: [android](android.md) · [firefox](firefox.md)

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
| quotes | `polish-double` 22 | **polish-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 6, `en` 1 | **em** |
| nbsp | `total` 436, `before-punctuation` 9 | **total** |
| register | `informal` 11 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (71)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Settings.Studies.Title.v148` — `pl/firefox-ios.xliff` — "Allow Feature Studies" is rendered as "Zezwól na badanie korzystania z funkcji", which says the app studies how the user uses features rather than allowing feature studies (experiments).
    - Current: `Zezwól na badanie korzystania z funkcji`
    - Source: `Allow Feature Studies`
    - Suggest: `Zezwól na badania funkcji`
    - The source refers to Mozilla's studies/experiments of features, not to monitoring the user's feature usage; the Polish asserts the product observes how the user uses features.
- `Search.ThirdPartyEngines.AddMessage` — `pl/firefox-ios.xliff` — Translation adds a claim about managing the engine in settings that the source does not contain.
    - Current: `Nowa wyszukiwarka pojawi się na pasku szybkiego wyszukiwania i będzie można nią zarządzać poprzez ustawienia.`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `Nowa wyszukiwarka pojawi się na pasku szybkiego wyszukiwania.`
    - The en-US only says "The new search engine will appear in the quick search bar."; the Polish adds "and it will be possible to manage it through settings".

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 39 |
| 3 | Degraded language (grammar, spelling, terminology) | 28 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `NSSpeechRecognitionUsageDescription` — `pl/firefox-ios.xliff` — Permission description reworded from "This lets Firefox transcribe your audio" into a statement that Firefox uses it, altering the meaning.
    - Current: `Firefox używa tego do zamieniania głosu na tekst.`
    - Source: `This lets Firefox transcribe your audio.`
    - Suggest: `Pozwoli to Firefoksowi zamieniać głos na tekst.`
    - The source describes an enabling permission ("This lets Firefox…"), consistent with the other permission strings translated as "Pozwoli to…"; the Polish asserts that Firefox already does this.
- `Bookmarks.Menu.DeletedBookmark.v131` — `pl/firefox-ios.xliff` — Past-tense toast confirmation "Deleted" rendered as the imperative command "Usuń" (Delete).
    - Current: `Usuń „%@”`
    - Source: `Deleted “%@”`
    - Suggest: `Usunięto „%@”`
    - The source is a toast shown after a bookmark has been deleted; Polish uses the imperative "Usuń" (Delete), turning a confirmation into a command. Compare the parallel toast strings using "Zachowano".
- `Settings.CustomizeFirefoxHome.PrivacyReport.v153` — `pl/firefox-ios.xliff` — "Privacy Report" translated as "Informacja o prywatności" (privacy notice/information) instead of a report.
    - Current: `Informacja o prywatności`
    - Source: `Privacy Report`
    - Suggest: `Raport prywatności`
    - The source names a Privacy Report (tracker blocker module summary); "Informacja o prywatności" suggests a privacy notice/policy, which is a different thing.
- `Addresses.EditAddress.AutofillAddressVillageTownship.v129` — `pl/firefox-ios.xliff` — "Township" left untranslated in the Polish label for the village/township field.
    - Current: `Wioska lub township`
    - Source: `Village or Township`
    - Suggest: `Wieś lub gmina`
    - The source "Village or Township" is an ordinary address-field label; leaving the English word "township" in lowercase mid-sentence is untranslated and unintelligible to Polish users.
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `pl/firefox-ios.xliff` — "try turning it off" refers to the protection, but Polish "spróbuj ją wyłączyć" grammatically refers to the site (witryna).
    - Current: `Jeśli coś na tej witrynie nie działa, spróbuj ją wyłączyć.`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `Jeśli coś na tej witrynie nie działa, spróbuj wyłączyć ochronę.`
    - The feminine pronoun "ją" agrees with "witryna", so the text tells the user to turn off the site instead of the tracking protection.
- `CreditCard.ErrorState.NameOnCardSublabel.v112` — `pl/firefox-ios.xliff` — "Add a name" is rendered as "Dodaj imię i nazwisko" (add first and last name), adding a requirement not in the source.
    - Current: `Dodaj imię i nazwisko`
    - Source: `Add a name`
    - Suggest: `Dodaj nazwę`
    - The source only asks for a name on the card; the Polish demands both a given name and surname.
- `MainMenu.HeaderBanner.Subtitle.v142` — `pl/firefox-ios.xliff` — "Change anytime" is rendered as "You can undo it at any time", changing the meaning.
    - Current: `Możesz cofnąć w każdej chwili.`
    - Source: `Takes seconds. Change anytime.`
    - Suggest: `Możesz to zmienić w każdej chwili.`
    - The source says the setting can be changed at any time, not that the action can be undone/reverted.
- `NativeErrorPage.Wayback.Error.Description.v154` — `pl/firefox-ios.xliff` — The order of Wi-Fi and data connection is swapped relative to the source.
    - Current: `sprawdź połączenie z siecią komórkową lub Wi-Fi`
    - Source: `The site may be busy or unavailable. Try again later. If other pages won’t load, check your Wi-Fi or data connection. %@ can also search the Wayback Machine for an earlier version of this page.`
    - Suggest: `sprawdź połączenie Wi-Fi lub transmisję danych`
    - Source says "check your Wi-Fi or data connection"; the translation reverses the order of the two items.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `pl/firefox-ios.xliff` — The clause "putting you in control" is omitted from the translation.
    - Current: `Wybierz swój ulubiony motyw lub dopasuj przeglądarkę %@ do swojego urządzenia.`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `Wybierz swój ulubiony motyw lub dopasuj przeglądarkę %@ do swojego urządzenia — to Ty decydujesz.`
    - The en-US sentence ends with "putting you in control", which has no equivalent in the Polish text.
- `Onboarding.Modern.Sync.Description.v140` — `pl/firefox-ios.xliff` — "on any device" rendered as "na wszystkich urządzeniach" (on all devices) instead of "na dowolnym/każdym urządzeniu".
    - Current: `na wszystkich urządzeniach`
    - Source: `Get your bookmarks, history, and passwords on any device.`
    - Suggest: `na dowolnym urządzeniu`
    - The source says "on any device"; the Polish claims all devices, a different statement (and inconsistent with the v145 string which uses "na każdym urządzeniu").
- `Onboarding.Modern.TermsOfService.ManageLink.v145` — `pl/firefox-ios.xliff` — "Manage settings" is rendered as just "Ustawienia" (Settings), dropping the action verb.
    - Current: `Ustawienia`
    - Source: `Manage settings`
    - Suggest: `Zarządzaj ustawieniami`
    - The source is a link button "Manage settings"; the Polish only says "Settings", losing the "manage" action (the v140 equivalent correctly uses "Zarządzaj").
- `Onboarding.Modern.Welcome.Title.v145` — `pl/firefox-ios.xliff` — "creepy trackers" translated with an odd intensifier; "koszmarnymi" means "nightmarish" rather than "creepy".
    - Current: `Pożegnaj się z koszmarnymi elementami śledzącymi`
    - Source: `Say goodbye to creepy trackers`
    - Suggest: `Pożegnaj się z niepokojącymi elementami śledzącymi`
    - "Creepy" means unsettling/invasive, not "nightmarish"; the same wording is reused from the ads string.
- `RelayMask.RelayEmailMaskAvailableCFR.v146` — `pl/firefox-ios.xliff` — Placeholder for the app name is misplaced so the text reads "masks for the e-mail address Firefox Relay" instead of "Firefox Relay email masks".
    - Current: `Maski dla adresu e-mail %@ Relay są teraz dostępne na telefonie.`
    - Source: `New! %@ Relay email masks are now available on mobile.`
    - Suggest: `Maski dla adresów e-mail %@ Relay są teraz dostępne na telefonie.`
    - Source is "%@ Relay email masks"; the Polish word order attaches %@ Relay to "adresu e-mail", obscuring that Relay is the product providing the masks.
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `pl/firefox-ios.xliff` — "You've used your 5 free email masks" rendered as "5 free masks have already been created", changing the statement about the user's usage.
    - Current: `5 bezpłatnych masek dla adresu e-mail zostało już utworzonych, więc wybraliśmy jedną, którą można wykorzystać ponownie.`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `Wszystkie 5 bezpłatnych masek dla adresów e-mail zostało już wykorzystanych, więc wybraliśmy jedną, której można użyć ponownie.`
    - The source states the user has used up their free allowance; the Polish says masks were created, losing the meaning that the limit was reached.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `pl/firefox-ios.xliff` — "or pop-ups about them" is rendered as "czy nawet informacji o nich", adding "nawet" and dropping the notion of pop-ups.
    - Current: `czy nawet informacji o nich`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `ani wyskakujących okien na ich temat`
    - The source says the user won't see pop-ups about the enhancements; the Polish says "or even information about them", changing meaning and intensity.
- `Settings.AIControls.HeaderCard.Message.v151` — `pl/firefox-ios.xliff` — The sentence is rendered as a fragment that does not convey "That includes whether to use features enhanced with AI".
    - Current: `Także w korzystaniu z funkcji ulepszonych za pomocą sztucznej inteligencji.`
    - Source: `That includes whether to use features enhanced with AI.`
    - Suggest: `Dotyczy to również tego, czy korzystać z funkcji ulepszonych za pomocą sztucznej inteligencji.`
    - The source states that the choice includes whether to use AI-enhanced features; the Polish drops the "whether to" choice element and is an incomplete clause.
- `Settings.Studies.Title.v148` — `pl/firefox-ios.xliff` — "Allow Feature Studies" is rendered as "Zezwól na badanie korzystania z funkcji", which says the app studies how the user uses features rather than allowing feature studies (experiments).
    - Current: `Zezwól na badanie korzystania z funkcji`
    - Source: `Allow Feature Studies`
    - Suggest: `Zezwól na badania funkcji`
    - The source refers to Mozilla's studies/experiments of features, not to monitoring the user's feature usage; the Polish asserts the product observes how the user uses features.
- `Settings.Translation.AutoTranslate.Footer.v151` — `pl/firefox-ios.xliff` — "your top preferred language" is rendered as "preferowany język użytkownika", losing "top" (the highest-ranked preferred language).
    - Current: `na preferowany język użytkownika`
    - Source: `Translates pages to your top preferred language automatically.`
    - Suggest: `na najwyżej ustawiony preferowany język`
    - The source specifies the top-ranked language in the preferred languages list, which matters since several preferred languages can be added.
- `Settings.Translation.ToggleTitle.v145` — `pl/firefox-ios.xliff` — "Enable Translations" is translated only as "Tłumaczenia", dropping the verb for a toggle title.
    - Current: `Tłumaczenia`
    - Source: `Enable Translations`
    - Suggest: `Włącz tłumaczenia`
    - The source is an action-style toggle label "Enable Translations"; the Polish omits "Enable".
- `SuggestedSites.X.Title.v131` — `pl/firefox-ios.xliff` — Brand name "X" is rendered as "Twitter", the former name the source deliberately no longer uses.
    - Current: `Twitter`
    - Source: `X`
    - Suggest: `X`
    - The source is the brand name "X" (the comment notes it is "formerly Twitter"); brand names must not be substituted with the obsolete name.
- `ContextualHints.Summarize.Description.v142` — `pl/firefox-ios.xliff` — "Touch and hold for Reader View" is translated as "hold to improve its readability", dropping the Reader View feature name.
    - Current: `Przytrzymaj, by poprawić jej czytelność.`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `Przytrzymaj, by przejść do widoku do czytania.`
    - The source refers to the named feature "Reader View"; the Polish instead claims the gesture improves page readability, not that it opens Reader View.
- `Summarizer.Footnote.Label.v144` — `pl/firefox-ios.xliff` — The footnote about summarization making errors is narrowed to "the summary may contain errors" vs. source wording, acceptable? see rationale.
    - Current: `Uwaga: streszczenie może zawierać błędy.`
    - Source: `Note: Summarization can make errors.`
    - Suggest: `Uwaga: streszczanie może powodować błędy.`
    - Source: "Summarization can make errors" refers to the summarization process; the Polish states the summary contains errors. Meaning is close but shifts the claim.
- `Summarizer.HostedBrand.Label.v142` — `pl/firefox-ios.xliff` — Added word "aplikację" (application) is not in the source and may be wrong for a third-party service.
    - Current: `Streszczone przez aplikację %@`
    - Source: `Summarized by %@`
    - Suggest: `Streszczone przez %@`
    - The comment says %@ is a service/app name; inserting "aplikację" asserts it is an app, which the source does not.
- `TabsTray.Sync.SyncTabsDisabled.v116` — `pl/firefox-ios.xliff` — The Polish says "wyświetlić ich listę z innych urządzeń", attaching "from other devices" to the list of tabs ambiguously/incorrectly compared with "a list of tabs from your other devices".
    - Current: `Włącz synchronizację kart, by wyświetlić ich listę z innych urządzeń.`
    - Source: `Turn on tab syncing to view a list of tabs from your other devices.`
    - Suggest: `Włącz synchronizację kart, aby wyświetlić listę kart z innych urządzeń.`
    - The en-US refers to a list of tabs from your other devices; the Polish pronoun construction shifts the meaning so the list itself appears to come from other devices.
- `WebCompatReporter.Preview.Data.UserAgent.v155` — `pl/firefox-ios.xliff` — The source's "Your browser's user agent" is rendered as "Identyfikator programu" and the app-name placeholder is turned into "wersję przeglądarki %@", losing that %@ is the app name.
    - Current: `Identyfikator programu, który zawiera wersję systemu iOS, wersję przeglądarki %@ i wersję silnika przeglądarki`
    - Source: `Your browser’s user agent, which includes your iOS version, %@ version, and browser engine version`
    - Suggest: `Identyfikator przeglądarki (user agent), który zawiera wersję systemu iOS, wersję %@ i wersję silnika przeglądarki`
    - en-US says "Your browser's user agent, which includes your iOS version, %@ version, and browser engine version"; the comment notes %@ is the app name (e.g. Firefox), so "%@ version" means "wersja Firefoksa", not "wersję przeglądarki %@".
- `WebCompatReporter.SubOption.ImagesNotLoaded.v154` — `pl/firefox-ios.xliff` — "Images not loaded" (completed state) is rendered as an ongoing "images are not loading".
    - Current: `Obrazy się nie wczytują`
    - Source: `Images not loaded`
    - Suggest: `Obrazy nie zostały wczytane`
    - The source states the images were not loaded, not that they are continuously failing to load; the sibling option "Page not loading correctly" uses the progressive form, so the distinction is lost.
- `WorldCup.HomepageWidget.GetCustomWallpaperLabel.v151` — `pl/firefox-ios.xliff` — "Get custom wallpaper" is rendered as "Ustaw piłkarską tapetę" ("Set a football wallpaper"), adding a meaning not in the source.
    - Current: `Ustaw piłkarską tapetę`
    - Source: `Get custom wallpaper`
    - Suggest: `Pobierz własną tapetę`
    - The source says "custom wallpaper", not "football wallpaper"; the translation both changes the verb and invents a descriptor.
- `WorldCup.HomepageWidget.GroupPhase.RelatedMatchesLabel.v151` — `pl/firefox-ios.xliff` — "Related matches" translated as "Pozostałe mecze" ("Remaining/other matches").
    - Current: `Pozostałe mecze`
    - Source: `Related matches`
    - Suggest: `Powiązane mecze`
    - "Pozostałe" means remaining/other, which is a different set than "related" matches for the team's group.
- `WorldCup.HomepageWidget.OfflineLabel.v151` — `pl/firefox-ios.xliff` — "Check your internet connection" is translated as "Sprawdź poprawność połączenia" (check the correctness of the connection), altering the instruction.
    - Current: `Sprawdź poprawność połączenia i spróbuj ponownie.`
    - Source: `Looks like you’re offline. Check your internet connection and try again.`
    - Suggest: `Sprawdź połączenie z Internetem i spróbuj ponownie.`
    - The source asks the user to check the internet connection; the Polish asks to verify its "correctness" and drops "internet".
- `WorldCup.HomepageWidget.RoundPhase.Round16Label.v151` — `pl/firefox-ios.xliff` — "ROUND OF 16" is rendered as "Druga runda" (second round) instead of the established Polish term for the round of 16.
    - Current: `Druga runda`
    - Source: `ROUND OF 16`
    - Suggest: `1/8 finału`
    - The source names the knockout stage with 16 teams; Polish football terminology is "1/8 finału" (or "runda 1/8 finału"). "Druga runda" merely says "second round" and does not identify the stage.
- `WorldCup.HomepageWidget.RoundPhase.Round32Label.v151` — `pl/firefox-ios.xliff` — "ROUND OF 32" is rendered as "Pierwsza runda" (first round) instead of the round-of-32 stage name.
    - Current: `Pierwsza runda`
    - Source: `ROUND OF 32`
    - Suggest: `1/16 finału`
    - The source names the knockout stage with 32 teams; Polish uses "1/16 finału". "Pierwsza runda" says "first round", which is not the same stage designation.
- `Add to Bookmarks` — `pl/firefox-ios.xliff` — "Add to Bookmarks" translated as "Dodaj zakładkę" (Add bookmark), losing the target collection.
    - Current: `Dodaj zakładkę`
    - Source: `Add to Bookmarks`
    - Suggest: `Dodaj do zakładek`
    - The source names the Bookmarks collection; the paired string "Remove Bookmark" is "Usuń zakładkę", so the distinction is lost.
- `Use your fingerprint to access Logins now.` — `pl/firefox-ios.xliff` — "Use your fingerprint" is rendered as "Use Touch ID", naming a brand the source does not mention.
    - Current: `Użyj Touch ID, by uzyskać dostęp do danych logowania.`
    - Source: `Use your fingerprint to access Logins now.`
    - Suggest: `Użyj odcisku palca, by uzyskać dostęp do danych logowania.`
    - The en-US says "Use your fingerprint"; the Polish substitutes the Apple brand name Touch ID, which the source does not state.
- `Authentication required` — `pl/firefox-ios.xliff` — Title "Authentication required" is rendered as an instruction to enter username and password.
    - Current: `Podaj nazwę użytkownika i hasło`
    - Source: `Authentication required`
    - Suggest: `Wymagane uwierzytelnienie`
    - The en-US source is a prompt title stating that authentication is required, not a directive to provide a username and password.
- `ContextMenu.DownloadLinkButtonTitle` — `pl/firefox-ios.xliff` — "Download Link" (verb + object) is rendered as a noun phrase "Odnośnik pobierania" (download's link).
    - Current: `Odnośnik pobierania`
    - Source: `Download Link`
    - Suggest: `Pobierz odnośnik`
    - Source is a context-menu action meaning "download the linked target"; the other items in the same menu use imperative verbs (Kopiuj odnośnik, Udostępnij odnośnik). The current text reads as a noun label "link of the download".
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `pl/firefox-ios.xliff` — "Tab pickup" is a section/cell label (noun), but the Polish renders it as an imperative command "Odbierz kartę" (Pick up the tab).
    - Current: `Odbierz kartę`
    - Source: `Tab pickup`
    - Suggest: `Karta z innego urządzenia`
    - The developer comment says this label points out which cell inside the Jump Back In section shows the synced tab; it is a label, not an action button, so an imperative verb changes the meaning.
- `Keyboard.Shortcuts.ClearRecentHistory` — `pl/firefox-ios.xliff` — "Recent" is dropped and replaced with "przeglądania", changing the meaning from clearing recent history to clearing browsing history.
    - Current: `Wyczyść historię przeglądania`
    - Source: `Clear Recent History`
    - Suggest: `Wyczyść ostatnią historię`
    - Source is "Clear Recent History"; the Polish says "Clear browsing history", losing the "recent" scope.
- `Keyboard.Shortcuts.ShowFirstTab` — `pl/firefox-ios.xliff` — "Show First Tab" translated as "Otwórz" (Open), while other Show* shortcuts use "Wyświetl".
    - Current: `Otwórz pierwszą kartę`
    - Source: `Show First Tab`
    - Suggest: `Wyświetl pierwszą kartę`
    - The shortcut switches to the first existing tab, it does not open a new one; other "Show …" shortcuts in the same overlay use "Wyświetl".
- `Keyboard.Shortcuts.ShowLastTab` — `pl/firefox-ios.xliff` — "Show Last Tab" translated as "Otwórz" (Open), inconsistent with the other "Show …" shortcuts.
    - Current: `Otwórz ostatnią kartę`
    - Source: `Show Last Tab`
    - Suggest: `Wyświetl ostatnią kartę`
    - The shortcut switches to the last existing tab; other "Show …" shortcuts in the same overlay use "Wyświetl".
- `Last week` — `pl/firefox-ios.xliff` — "Last week" rendered as "Ostatnie 7 dni" (last 7 days), inconsistent with the sibling section label "Ostatni miesiąc".
    - Current: `Ostatnie 7 dni`
    - Source: `Last week`
    - Suggest: `Ostatni tydzień`
    - Source label is "Last week"; the neighbouring section "Last month" is translated literally as "Ostatni miesiąc", so this is inconsistent.
- `Logins.PasscodeRequirement.Warning` — `pl/firefox-ios.xliff` — "device passcode" rendered as "kod urządzenia", losing the sense of a device passcode/lock code.
    - Current: `musi być włączony kod urządzenia`
    - Source: `To use the AutoFill feature for Firefox, you must have a device passcode enabled.`
    - Suggest: `musi być włączony kod dostępu do urządzenia`
    - The source refers to the device passcode (screen-lock code); "kod urządzenia" is ambiguous and not the established term.
- `LoginsHelper.SaveLogin.Button` — `pl/firefox-ios.xliff` — "Save Login" is rendered as "Zachowaj hasło" (Save password) instead of the login/credentials term.
    - Current: `Zachowaj hasło`
    - Source: `Save Login`
    - Suggest: `Zachowaj dane logowania`
    - The source says "Save Login"; the pl file elsewhere renders "logins" as "dane logowania" (see LoginsList.Title). "hasło" is the translation of "password".
- `LoginsList.LoginsListSearchPlaceholder` — `pl/firefox-ios.xliff` — "Filter" is translated as "Szukaj" (Search).
    - Current: `Szukaj`
    - Source: `Filter`
    - Suggest: `Filtruj`
    - The source placeholder is "Filter", not "Search".
- `Menu.TrackingProtectionDescription.Fingerprinters` — `pl/firefox-ios.xliff` — "track you as you browse" translated as tracking "Twojej aktywności w Internecie" is acceptable, but "profile of you" rendered impersonally conflicts with informal address used elsewhere in the string.
    - Current: `profil użytkownika`
    - Source: `The settings on your browser and computer are unique. Fingerprinters collect a variety of these unique settings to create a profile of you, which can be used to track you as you browse.`
    - Suggest: `profil Ciebie`
    - The same string uses informal second person ("Twojej aktywności"), while "profile of you" is rendered as the third-person "profil użytkownika", an inconsistent form of address within one sentence.
- `Okay` — `pl/firefox-ios.xliff` — "Okay" is rendered as "Przywróć" (Restore) instead of a neutral affirmative.
    - Current: `Przywróć`
    - Source: `Okay`
    - Suggest: `OK`
    - The source is the generic affirmative "Okay"; the Polish substitutes a different verb ("Restore"), changing the button text from the source wording.
- `Search.ThirdPartyEngines.AddMessage` — `pl/firefox-ios.xliff` — Translation adds a claim about managing the engine in settings that the source does not contain.
    - Current: `Nowa wyszukiwarka pojawi się na pasku szybkiego wyszukiwania i będzie można nią zarządzać poprzez ustawienia.`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `Nowa wyszukiwarka pojawi się na pasku szybkiego wyszukiwania.`
    - The en-US only says "The new search engine will appear in the quick search bar."; the Polish adds "and it will be possible to manage it through settings".
- `SentTab_TabArrivingNotification_WithDevice_title` — `pl/firefox-ios.xliff` — %@ is a device name, but the Polish says "from the program %@".
    - Current: `Przychodząca karta z programu %@`
    - Source: `Tab received from %@`
    - Suggest: `Przychodząca karta z urządzenia %@`
    - The developer comment states %@ is the device name; "z programu" (from the app) names the wrong thing.
- `Settings.AddCustomEngine.SaveButtonText` — `pl/firefox-ios.xliff` — "Save" translated as "Gotowe" (Done).
    - Current: `Gotowe`
    - Source: `Save`
    - Suggest: `Zapisz`
    - The source is "Save" for the Save button when saving a custom search engine; "Gotowe" means "Done".
- `Settings.Passwords.FingerPrintReason.v103` — `pl/firefox-ios.xliff` — "Use your fingerprint" rendered as "Użyj Touch ID", naming a brand feature the source does not mention.
    - Current: `Użyj Touch ID, by uzyskać dostęp do haseł.`
    - Source: `Use your fingerprint to access passwords now.`
    - Suggest: `Użyj odcisku palca, by uzyskać teraz dostęp do haseł.`
    - The source says "Use your fingerprint to access passwords now."; the Polish substitutes the Touch ID brand name and drops "now".
- `Settings.ShowLinkPreviews.Title` — `pl/firefox-ios.xliff` — "Show Link Previews" translated as "Wyświetlanie podglądu strony" (page preview) instead of link previews.
    - Current: `Wyświetlanie podglądu strony`
    - Source: `Show Link Previews`
    - Suggest: `Wyświetlanie podglądu odnośników`
    - The source and the related status string refer to previews of links (odnośniki), not of a page; the other strings in the same group use "odnośnika".
- `Settings.TrackingProtection.ProtectionLevelStandard.Description` — `pl/firefox-ios.xliff` — "some ad tracking" rendered as "pewne reklamy śledzące" (some tracking ads) instead of ad tracking.
    - Current: `Dopuszcza pewne reklamy śledzące`
    - Source: `Allows some ad tracking so websites function properly.`
    - Suggest: `Dopuszcza pewne śledzenie reklamowe`
    - The source allows some ad tracking (the activity), not certain tracking ads.
- `SyncState.Offline.Title` — `pl/firefox-ios.xliff` — "Sync is offline" translated as just "Poza siecią", dropping the subject Sync.
    - Current: `Poza siecią`
    - Source: `Sync is offline`
    - Suggest: `Synchronizacja jest w trybie offline`
    - The source states that Sync is offline; the Polish only says "offline" without indicating what is offline.

### C. Grammar, agreement & spelling

- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `pl/firefox-ios.xliff` — "Nie zaznaczone" should be written as one word in Polish.
    - Current: `Nie zaznaczone`
    - Source: `Unselected`
    - Suggest: `Niezaznaczone`
    - In Polish, "nie" with an adjectival participle used as an attribute is written together: "niezaznaczone".
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `pl/firefox-ios.xliff` — Case agreement error in the coordinated noun phrase: "sposobu" should be "sposobie".
    - Current: `konfiguracji sprzętowej i sposobu korzystania`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `konfiguracji sprzętowej i sposobie korzystania`
    - "Informacje o" requires the locative case for all coordinated nouns (urządzeniu, konfiguracji, sposobie), but "sposobu" is genitive.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `pl/firefox-ios.xliff` — Case agreement error: "sposobu korzystania" should be "sposobie korzystania" in the coordinated locative list.
    - Current: `Informacje o Twoim urządzeniu, konfiguracji sprzętowej i sposobu korzystania`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `Informacje o Twoim urządzeniu, konfiguracji sprzętowej i sposobie korzystania`
    - The preposition "o" governs the locative for all coordinated items (urządzeniu, konfiguracji, sposobie); "sposobu" is genitive and ungrammatical here.
- `Onboarding.Wallpaper.SelectorTitle.v114` — `pl/firefox-ios.xliff` — Incorrect case/number after "Wypróbuj" — should be "odrobinę koloru".
    - Current: `Wypróbuj odrobiny koloru`
    - Source: `Try a splash of color`
    - Suggest: `Wypróbuj odrobinę koloru`
    - "Try a splash of color" is singular; the Polish verb "wypróbuj" requires the accusative singular "odrobinę", not the genitive/plural "odrobiny".
- `PasswordGenerator.Description.v132` — `pl/firefox-ios.xliff` — Singular "your account" rendered as plural "swoje konta", mismatching the singular context.
    - Current: `Chroń swoje konta za pomocą silnego, losowo wygenerowanego hasła.`
    - Source: `Protect your account by using a strong, randomly generated password.`
    - Suggest: `Chroń swoje konto za pomocą silnego, losowo wygenerowanego hasła.`
    - The en-US source says "Protect your account" (singular) — the popup refers to the single account being created.
- `FxAPush_DeviceDisconnected_body` — `pl/firefox-ios.xliff` — Wrong preposition: "odłączone do synchronizacji" instead of "od synchronizacji".
    - Current: `Urządzenie „%@” zostało odłączone do synchronizacji`
    - Source: `%@ has been successfully disconnected.`
    - Suggest: `Urządzenie „%@” zostało odłączone od synchronizacji`
    - The source says the device has been disconnected; Polish requires "odłączone od", and the parallel string FxAPush_DeviceDisconnected_UnknownDevice_body uses "od synchronizacji".
- `LibraryPanel.History.NoHistoryFound.v99` — `pl/firefox-ios.xliff` — "Nie odnaleziono historii" – missing search-result sense; should be "Nie znaleziono historii".
    - Current: `Nie odnaleziono historii`
    - Source: `No history found`
    - Suggest: `Nie znaleziono historii`
    - Standard Firefox wording for "No … found" in search results is "Nie znaleziono".
- `Open articles in Reader View by tapping the book icon when it appears in the title bar.` — `pl/firefox-ios.xliff` — Missing comma before the participial phrase "stukając".
    - Current: `czytelności stukając ikonę`
    - Source: `Open articles in Reader View by tapping the book icon when it appears in the title bar.`
    - Suggest: `czytelności, stukając ikonę`
    - Polish punctuation requires a comma before an adverbial participial clause (imiesłowowy równoważnik zdania).
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `pl/firefox-ios.xliff` — Missing comma closing the relative clause before the predicate.
    - Current: `Karty, których nie odwiedzono od dwóch tygodni są przenoszone`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `Karty, których nie odwiedzono od dwóch tygodni, są przenoszone`
    - Polish punctuation requires the subordinate clause to be closed with a comma before "są przenoszone".
- `Bookmarks Menu` — `pl/firefox-ios.xliff` — "Menu Zakładki" is ungrammatical for the folder name "Bookmarks Menu".
    - Current: `Menu Zakładki`
    - Source: `Bookmarks Menu`
    - Suggest: `Menu zakładek`
    - Polish requires the genitive: the folder containing desktop bookmarks in the menu is "Menu zakładek", matching the Firefox desktop terminology; "Menu Zakładki" reads as a nominative mismatch.

### D. Terminology, register & consistency

- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `pl/firefox-ios.xliff` — "device passcode" rendered as "hasło urządzenia" here but as "kod urządzenia" in the parallel string in the same file.
    - Current: `hasło urządzenia`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `kod urządzenia`
    - The sibling string Logins.DevicePasscodeRequired.Message.v122 translates the same source phrase "a device passcode" as "kod urządzenia"; inconsistent terminology within the same file/feature.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `pl/firefox-ios.xliff` — "Save" is rendered as "Zachowaj" here but as "Zapisz" in the parallel Save accessibility label, an inconsistency on the same menu.
    - Current: `Podmenu Zachowaj`
    - Source: `Save submenu`
    - Suggest: `Podmenu Zapisz`
    - MainMenu.ToolsSection.AccessibilityLabels.Save.v132 translates the same "Save" submenu name as "Zapisz"; the submenu label must use the same term as the menu item it names.
- `Settings.AIControls.BlockAIEnhancementsTitle.v151` — `pl/firefox-ios.xliff` — "AI" is abbreviated as "SI", which is inconsistent with the other strings on the same screen that use "sztuczna inteligencja".
    - Current: `Blokuj ulepszenia SI`
    - Source: `Block AI Enhancements`
    - Suggest: `Blokuj ulepszenia sztucznej inteligencji`
    - Within the same AI Controls screen, AI is rendered both as "sztuczna inteligencja" (section title, header card) and "SI"; the Polish standard abbreviation is "AI"/"sztuczna inteligencja", not "SI".
- `WorldCup.HomepageWidget.TemporaryView.Description.v151` — `pl/firefox-ios.xliff` — Formal capitalized "Cię" used where the locale convention is informal address without honorific capitalization.
    - Current: `Będziemy Cię informować`
    - Source: `We’ll keep you updated as the World Cup approaches`
    - Suggest: `Będziemy cię informować`
    - The pl locale uses informal register; capitalized "Cię" is the formal/courtesy form.

### E. Typography, punctuation & spacing

- `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` — `pl/firefox-ios.xliff` — Comma used instead of a conjunction, changing "Agree and continue" into two clauses.
    - Current: `Zgadzam się, kontynuuj`
    - Source: `Agree and continue`
    - Suggest: `Zgadzam się i kontynuuj`
    - Source is a coordinated button label "Agree and continue"; the comma version reads as an imperative telling the user to continue.
- `Oops! Firefox crashed` — `pl/firefox-ios.xliff` — Translation drops the "Oops!" interjection and adds an ASCII emoticon ":(" not present in the source.
    - Current: `Firefox uległ awarii :(`
    - Source: `Oops! Firefox crashed`
    - Suggest: `Firefox uległ awarii`
    - The en-US reads "Oops! Firefox crashed"; the Polish invents an emoticon instead, which is not source content and is not a Polish typographic convention.
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `pl/firefox-ios.xliff` — Missing comma before the adverbial participle clause "stukając".
    - Current: `Zachowuj strony w czytelni stukając ikonę książki`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Zachowuj strony w czytelni, stukając ikonę książki`
    - Polish punctuation requires a comma before an imiesłów przysłówkowy clause.
- `The page could not be displayed in Reader View.` — `pl/firefox-ios.xliff` — Missing final period present in the source sentence.
    - Current: `Strona nie może zostać wyświetlona w widoku poprawionej czytelności`
    - Source: `The page could not be displayed in Reader View.`
    - Suggest: `Strona nie może zostać wyświetlona w widoku poprawionej czytelności.`
    - The en-US string ends with a period; the Polish sentence omits it.
- `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.` — `pl/firefox-ios.xliff` — Sentence-final period is missing in the Polish translation.
    - Current: `Firefox nie zachowa historii przeglądania ani ciasteczek (dodane zakładki zostaną zachowane)`
    - Source: `Firefox won’t remember any of your history or cookies, but new bookmarks will be saved.`
    - Suggest: `Firefox nie zachowa historii przeglądania ani ciasteczek (dodane zakładki zostaną zachowane).`
    - The en-US source ends with a period; the Polish description drops the final punctuation.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/pl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
