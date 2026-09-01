# Firefox iOS l10n QA — pl

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `117165baae4c` |
| **Previous run** | 2026-08-24 @ `a2ecb0a822be` |
| **Mode** | incremental |
| **Strings reviewed this run** | 2 of 1,912 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


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
| Files | 95 |
| Strings | 1,912 |
| Missing strings | 6 |
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

**6 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en.lproj/GoogleLens.strings` — 2
- `pl/firefox-ios.xliff` — 2
- `pl/firefox-ios.xliff` — 1
- `pl/firefox-ios.xliff` — 1

**Files absent from the locale:**

- `Shared/Supporting Files/en.lproj/GoogleLens.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 22 | **polish-double** |
| ellipsis | `char` 20 | **char** |
| dash | `em` 6, `en` 1 | **em** |
| nbsp | `total` 431, `before-punctuation` 9 | **total** |
| register | `informal` 11 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (45)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 32 |
| 3 | Degraded language (grammar, spelling, terminology) | 9 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Bookmarks.Menu.DeletedBookmark.v131` — `pl/firefox-ios.xliff` — Toast confirming a deletion is translated as an imperative command "Delete" instead of the past-tense "Deleted".
    - Current: `Usuń „%@”`
    - Source: `Deleted “%@”`
    - Suggest: `Usunięto „%@”`
    - The source "Deleted “%@”" is a toast shown after a bookmark was deleted; "Usuń" is the imperative "Delete", reversing the meaning to an action prompt.
- `Settings.CustomizeFirefoxHome.PrivacyReport.v153` — `pl/firefox-ios.xliff` — "Privacy Report" is rendered as "Informacja o prywatności" (privacy notice/information) instead of a report.
    - Current: `Informacja o prywatności`
    - Source: `Privacy Report`
    - Suggest: `Raport prywatności`
    - The source refers to a Privacy Report (tracker blocker summary), not a privacy notice/statement; "Informacja o prywatności" suggests a privacy policy notice.
- `Addresses.EditAddress.AutofillAddressVillageTownship.v129` — `pl/firefox-ios.xliff` — "Township" is left untranslated in the Polish label for the village/township field.
    - Current: `Wioska lub township`
    - Source: `Village or Township`
    - Suggest: `Wieś lub gmina`
    - The en-US "Village or Township" names two administrative units; "township" is an untranslated English word that Polish users will not recognize as an address field label.
- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `pl/firefox-ios.xliff` — Analytics trackers row is translated as "Treści z elementami śledzącymi" (tracking content), not matching the analytics/tracking-content label consistently.
    - Current: `Treści z elementami śledzącymi: %@`
    - Source: `Tracking content: %@`
    - Suggest: `Elementy śledzące analizujące: %@`
    - The developer comment says this counts analytics trackers; "Treści z elementami śledzącymi" means "tracking content", a different ETP category.
- `Menu.EnhancedTrackingProtection.SwitchOn.Text.v128` — `pl/firefox-ios.xliff` — "try turning it off" refers to the protection, but the Polish "spróbuj ją wyłączyć" grammatically refers to the site (witryna).
    - Current: `Jeśli coś na tej witrynie nie działa, spróbuj ją wyłączyć.`
    - Source: `If something looks broken on this site, try turning it off.`
    - Suggest: `Jeśli coś na tej witrynie nie działa, spróbuj wyłączyć ochronę.`
    - In the source "it" is the enhanced tracking protection switch; in Polish the feminine pronoun "ją" attaches to "witrynę", telling users to turn off the site.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `pl/firefox-ios.xliff` — The translation reverses the meaning: the source says Firefox should match the device theme, and the added clause "putting you in control" is dropped.
    - Current: `lub dopasuj przeglądarkę %@ do swojego urządzenia.`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `lub pozwól przeglądarce %@ dopasować się do urządzenia — to Ty decydujesz.`
    - en-US: "have %@ match your device, putting you in control" — Firefox matches the device; the Polish imperative tells the user to adapt the browser and omits "putting you in control".
- `PasswordGenerator.Description.v132` — `pl/firefox-ios.xliff` — Singular "your account" rendered as plural "swoje konta".
    - Current: `Chroń swoje konta za pomocą`
    - Source: `Protect your account by using a strong, randomly generated password.`
    - Suggest: `Chroń swoje konto za pomocą`
    - The source says "Protect your account" (singular), referring to the account being created; the Polish plural "konta" changes the meaning.
- `RelayMask.RelayEmailMaskAvailableCFR.v146` — `pl/firefox-ios.xliff` — Product name "Firefox Relay" split so the placeholder no longer forms the product name.
    - Current: `Maski dla adresu e-mail %@ Relay są teraz dostępne`
    - Source: `New! %@ Relay email masks are now available on mobile.`
    - Suggest: `Maski dla adresu e-mail %@ Relay są teraz dostępne na urządzeniach mobilnych.`
    - "on mobile" was rendered as "na telefonie" (on the phone), narrowing the meaning to phones only; the product is available on mobile devices generally.
- `Settings.AIControls.BlockAIEnhancementsDescription.v151` — `pl/firefox-ios.xliff` — "or pop-ups about them" is mistranslated as "czy nawet informacji o nich" ("or even information about them").
    - Current: `czy nawet informacji o nich`
    - Source: `Blocking means you won’t see new or current AI enhancements in %@, or pop-ups about them.`
    - Suggest: `ani wyskakujących okien na ich temat`
    - The source says the user won't see pop-ups about the AI enhancements; the Polish drops "pop-ups" and adds "even", changing the meaning.
- `Settings.AIControls.HeaderCard.Message.v151` — `pl/firefox-ios.xliff` — The message renders "whether to use" as "in using", losing the choice/whether-or-not meaning.
    - Current: `Także w korzystaniu z funkcji ulepszonych za pomocą sztucznej inteligencji.`
    - Source: `That includes whether to use features enhanced with AI.`
    - Suggest: `Dotyczy to również tego, czy korzystać z funkcji ulepszonych za pomocą sztucznej inteligencji.`
    - en-US: "That includes whether to use features enhanced with AI." — the choice is whether or not to use the features, not merely "in using" them.
- `Settings.Studies.Title.v148` — `pl/firefox-ios.xliff` — "Allow Feature Studies" is rendered as "Zezwól na badanie korzystania z funkcji", which means "allow studying feature usage" rather than allowing feature studies (experiments).
    - Current: `Zezwól na badanie korzystania z funkcji`
    - Source: `Allow Feature Studies`
    - Suggest: `Zezwól na badania funkcji`
    - The source refers to studies (experiments) that test features, not to monitoring how the user uses features; the developer comment confirms this is the opt-in/out toggle for studies.
- `SuggestedSites.X.Title.v131` — `pl/firefox-ios.xliff` — The brand name "X" is rendered as the former name "Twitter".
    - Current: `Twitter`
    - Source: `X`
    - Suggest: `X`
    - The source is the brand name "X" (formerly Twitter); brand names must not be replaced with the outdated name.
- `ContextualHints.Summarize.Description.v142` — `pl/firefox-ios.xliff` — "Touch and hold for Reader View" is mistranslated as "hold to improve its readability", dropping the Reader View feature name.
    - Current: `Przytrzymaj, by poprawić jej czytelność.`
    - Source: `Tap to summarize this page. Touch and hold for Reader View.`
    - Suggest: `Przytrzymaj, aby otworzyć widok do czytania.`
    - The source refers to the Reader View feature; the Polish says "to improve its readability", which names no feature and changes the meaning.
- `Summarizer.Error.UnsafeWebsite.Message.v142` — `pl/firefox-ios.xliff` — "Limited content detected" is mistranslated as "Inappropriate content detected".
    - Current: `Wykryto nieodpowiednią treść.`
    - Source: `Limited content detected. This page may be restricted or mostly visual.`
    - Suggest: `Wykryto ograniczoną treść.`
    - The source says content is limited (little text), not that it is unsafe/inappropriate for the user.
- `Toolbar.NewTab.Button.v142` — `pl/firefox-ios.xliff` — Reader view accessibility label mistranslated as an instruction to improve readability.
    - Current: `Popraw czytelność. Dostępne jest streszczenie strony.`
    - Source: `Summarize page`
    - Suggest: `Widok czytnika. Dostępne jest streszczenie strony.`
    - Placeholder finding removed
- `BreachAlerts.Description` — `pl/firefox-ios.xliff` — "since you last changed your password" is translated as "od czasu ostatniej zmiany danych logowania" (login credentials) instead of password.
    - Current: `Od czasu ostatniej zmiany danych logowania`
    - Source: `Passwords were leaked or stolen since you last changed your password. To protect this account, log in to the site and change your password.`
    - Suggest: `Od czasu ostatniej zmiany hasła`
    - The source says password, not login credentials.
- `ContextMenu.DownloadLinkButtonTitle` — `pl/firefox-ios.xliff` — "Download Link" (an action: download the linked file) is rendered as the noun phrase "Odnośnik pobierania" (download link).
    - Current: `Odnośnik pobierania`
    - Source: `Download Link`
    - Suggest: `Pobierz odnośnik`
    - The context menu item is an action to download the target of the link, not a label naming a link; other items in the same menu use imperative verbs (Kopiuj, Zapisz, Udostępnij).
- `ErrorPages.AdvancedWarning1.Text` — `pl/firefox-ios.xliff` — Translation drops "to this website" from the warning text.
    - Current: `nie można potwierdzić bezpieczeństwa połączenia.`
    - Source: `Warning: we can’t confirm your connection to this website is secure.`
    - Suggest: `nie można potwierdzić bezpieczeństwa połączenia z tą witryną.`
    - en-US specifies "your connection to this website is secure"; the reference to the website is omitted.
- `ErrorPages.CertWarning.Title` — `pl/firefox-ios.xliff` — "This Connection is Untrusted" is rendered as "connection is not secure", changing trust to security.
    - Current: `Połączenie nie jest bezpieczne`
    - Source: `This Connection is Untrusted`
    - Suggest: `To połączenie nie jest zaufane`
    - The source says the connection is untrusted (certificate trust), not insecure; Firefox uses "niezaufane" for untrusted.
- `FirefoxHomepage.JumpBackIn.TabPickup.v104` — `pl/firefox-ios.xliff` — "Tab pickup" is a section label, not an action, but it is translated as the imperative "Odbierz kartę" (Pick up the tab).
    - Current: `Odbierz kartę`
    - Source: `Tab pickup`
    - Suggest: `Karta z innego urządzenia`
    - The developer comment states this label points out the cell showing a synced tab from another device; an imperative verb phrase misrepresents a section label.
- `Hotkeys.Forward.DiscoveryTitle` — `pl/firefox-ios.xliff` — "Forward" translated as "Następna strona" while the developer comment says it switches to a subsequent tab.
    - Current: `Następna strona`
    - Source: `Forward`
    - Suggest: `Dalej`
    - Source is the navigation command "Forward"; "Następna strona" (next page) names something else and conflicts with the shortcut's meaning.
- `Keyboard.Shortcuts.ClearRecentHistory` — `pl/firefox-ios.xliff` — "Clear Recent History" is rendered as "Wyczyść historię przeglądania", dropping the "recent" qualifier.
    - Current: `Wyczyść historię przeglądania`
    - Source: `Clear Recent History`
    - Suggest: `Wyczyść ostatnią historię`
    - The source specifies recent history; the translation says "browsing history", which implies clearing all history and omits "recent".
- `Keyboard.Shortcuts.ShowFirstTab` — `pl/firefox-ios.xliff` — "Show First Tab" translated as "Otwórz pierwszą kartę" (Open first tab) instead of "show/switch to".
    - Current: `Otwórz pierwszą kartę`
    - Source: `Show First Tab`
    - Suggest: `Wyświetl pierwszą kartę`
    - The shortcut switches to an existing tab, it does not open a new one; other "Show ... Tab" strings in the same group use "Wyświetl".
- `Keyboard.Shortcuts.ShowLastTab` — `pl/firefox-ios.xliff` — "Show Last Tab" translated as "Otwórz ostatnią kartę" (Open last tab) instead of "show/switch to".
    - Current: `Otwórz ostatnią kartę`
    - Source: `Show Last Tab`
    - Suggest: `Wyświetl ostatnią kartę`
    - The shortcut switches to the last existing tab; "Otwórz" implies opening a new tab and is inconsistent with "Wyświetl następną/poprzednią kartę" in the same overlay.
- `Okay` — `pl/firefox-ios.xliff` — "Okay" is rendered as "Przywróć" (Restore) instead of an affirmative acknowledgement.
    - Current: `Przywróć`
    - Source: `Okay`
    - Suggest: `OK`
    - The source is the generic affirmative "Okay"; "Przywróć" means "Restore", which says something different from the source.
- `Open articles in Reader View by tapping the book icon when it appears in the title bar.` — `pl/firefox-ios.xliff` — "title bar" mistranslated as "pasku adresu" (address bar).
    - Current: `kiedy pojawi się w pasku adresu`
    - Source: `Open articles in Reader View by tapping the book icon when it appears in the title bar.`
    - Suggest: `kiedy pojawi się na pasku tytułu`
    - The en-US says "title bar", not address bar.
- `Search.ThirdPartyEngines.AddMessage` — `pl/firefox-ios.xliff` — Translation adds content not present in the source about managing the engine through settings.
    - Current: `Nowa wyszukiwarka pojawi się na pasku szybkiego wyszukiwania i będzie można nią zarządzać poprzez ustawienia.`
    - Source: `The new search engine will appear in the quick search bar.`
    - Suggest: `Nowa wyszukiwarka pojawi się na pasku szybkiego wyszukiwania.`
    - The en-US source only says "The new search engine will appear in the quick search bar."; the clause "i będzie można nią zarządzać poprzez ustawienia" is invented.
- `SentTab_TabArrivingNotification_WithDevice_title` — `pl/firefox-ios.xliff` — %@ is a device name, but the translation says "from the program %@".
    - Current: `Przychodząca karta z programu %@`
    - Source: `Tab received from %@`
    - Suggest: `Przychodząca karta z urządzenia %@`
    - The developer comment states %@ is the placeholder for the device name, not an application name.
- `Settings.AddCustomEngine.SaveButtonText` — `pl/firefox-ios.xliff` — "Save" is translated as "Gotowe" (Done) instead of "Zapisz".
    - Current: `Gotowe`
    - Source: `Save`
    - Suggest: `Zapisz`
    - The developer comment says this is the Save button for saving a custom search engine; "Gotowe" means "Done", which is a different label (Polish for Save is "Zapisz").
- `Settings.Passwords.FingerPrintReason.v103` — `pl/firefox-ios.xliff` — "Use your fingerprint" was rendered as "Use Touch ID", changing the source meaning.
    - Current: `Użyj Touch ID, by uzyskać dostęp do haseł.`
    - Source: `Use your fingerprint to access passwords now.`
    - Suggest: `Użyj odcisku palca, aby uzyskać teraz dostęp do haseł.`
    - The en-US says "Use your fingerprint to access passwords now." — it refers to the fingerprint, not the branded Touch ID feature, and the word "now" is also dropped.
- `Settings.ShowLinkPreviews.Title` — `pl/firefox-ios.xliff` — "Show Link Previews" is translated as "podgląd strony" (page preview) instead of link previews.
    - Current: `Wyświetlanie podglądu strony`
    - Source: `Show Link Previews`
    - Suggest: `Wyświetlanie podglądu odnośników`
    - The source and the companion status string refer to previews of links (odnośników), not of a page; the target says "page preview".
- `SyncState.Offline.Title` — `pl/firefox-ios.xliff` — Translation drops the reference to Sync being offline.
    - Current: `Poza siecią`
    - Source: `Sync is offline`
    - Suggest: `Synchronizacja jest w trybie offline`
    - Source is "Sync is offline" — a Sync status message; the Polish only says "Offline" with no mention of Sync.

### C. Grammar, agreement & spelling

- `Microsurvey.Survey.RadioButton.Unselected.AccessibilityLabel.v129` — `pl/firefox-ios.xliff` — "Nie zaznaczone" should be written as one word in modern Polish orthography.
    - Current: `Nie zaznaczone`
    - Source: `Unselected`
    - Suggest: `Niezaznaczone`
    - Polish spelling rules require the negation particle "nie" to be joined with adjectival participles: "niezaznaczone".
- `Onboarding.Modern.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v140` — `pl/firefox-ios.xliff` — Case agreement error: "sposobu" should be "sposobie" to match the locative series after "o".
    - Current: `Informacje o Twoim urządzeniu, konfiguracji sprzętowej i sposobu korzystania`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `Informacje o Twoim urządzeniu, konfiguracji sprzętowej i sposobie korzystania`
    - The enumeration governed by the preposition "o" requires the locative case (urządzeniu, konfiguracji, sposobie); "sposobu" is genitive and ungrammatical.
- `Onboarding.TermsOfService.PrivacyPreferences.SendTechnicalDataDescription.v135` — `pl/firefox-ios.xliff` — Case mismatch in the coordinated list: "sposobu korzystania" should be locative "sposobie korzystania".
    - Current: `Informacje o Twoim urządzeniu, konfiguracji sprzętowej i sposobu korzystania`
    - Source: `Data about your device, hardware configuration, and how you use %1$@ helps improve features, performance, and stability for everyone. %2$@`
    - Suggest: `Informacje o Twoim urządzeniu, konfiguracji sprzętowej i sposobie korzystania`
    - The preposition "o" governs the locative case for all coordinated nouns (urządzeniu, konfiguracji, sposobie), so "sposobu" is a grammatical error.
- `Onboarding.Wallpaper.SelectorTitle.v114` — `pl/firefox-ios.xliff` — Wrong case after "Wypróbuj" — should be genitive singular "odrobiny koloru" is used but the phrase reads ungrammatically.
    - Current: `Wypróbuj odrobiny koloru`
    - Source: `Try a splash of color`
    - Suggest: `Wypróbuj odrobinę koloru`
    - "Wypróbuj" takes the accusative: "odrobinę koloru". "Wypróbuj odrobiny koloru" is grammatically incorrect.
- `DefaultBrowserCard.BetterInternet.Description.v108` — `pl/firefox-ios.xliff` — Wrong case after "jako": should be instrumental "domyślną przeglądarką" (or accusative matching "ustawienie ... na"), not accusative "domyślną przeglądarkę" with the verbal noun.
    - Current: `Ustawienie Firefoksa jako domyślną przeglądarkę`
    - Source: `Making Firefox your default browser is a vote for an open, accessible internet.`
    - Suggest: `Ustawienie Firefoksa jako domyślnej przeglądarki`
    - With the verbal noun "ustawienie" the phrase "jako" takes the case of the governed noun "Firefoksa" (genitive), so it must be "jako domyślnej przeglądarki"; the accusative form is ungrammatical here.
- `FxAPush_DeviceDisconnected_body` — `pl/firefox-ios.xliff` — Wrong preposition: "odłączone do synchronizacji" should be "odłączone od synchronizacji".
    - Current: `Urządzenie „%@” zostało odłączone do synchronizacji`
    - Source: `%@ has been successfully disconnected.`
    - Suggest: `Urządzenie „%@” zostało odłączone od synchronizacji`
    - The source says the device has been disconnected; "odłączone do" is ungrammatical and reverses the sense, as the parallel strings use "odłączone od synchronizacji".
- `Settings.Tabs.CustomizeTabsSection.InactiveTabsDescription.v101` — `pl/firefox-ios.xliff` — Missing comma closing the relative clause before "są przenoszone".
    - Current: `Karty, których nie odwiedzono od dwóch tygodni są przenoszone`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `Karty, których nie odwiedzono od dwóch tygodni, są przenoszone`
    - Polish punctuation requires the subordinate clause to be closed with a comma on both sides.

### D. Terminology, register & consistency

- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `pl/firefox-ios.xliff` — "device passcode" is translated as "hasło urządzenia" here but as "kod urządzenia" in the parallel string in the same file.
    - Current: `hasło urządzenia`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `kod urządzenia`
    - Logins.DevicePasscodeRequired.Message.v122 in the same file renders the identical source phrase "a device passcode" as "kod urządzenia"; the inconsistency mislabels the iOS passcode as a password.
- `MainMenu.ToolsSection.AccessibilityLabels.Save.v133` — `pl/firefox-ios.xliff` — "Save submenu" is rendered as "Podmenu Zachowaj" while the Save item itself is translated "Zapisz" elsewhere in the same menu.
    - Current: `Podmenu Zachowaj`
    - Source: `Save submenu`
    - Suggest: `Podmenu Zapisz`
    - The Save submenu title (MainMenu.ToolsSection.SaveSubmenu.Title.v131) and the Save accessibility label (…Save.v132) both use "Zapisz"; using "Zachowaj" for the same source term on the same screen is inconsistent.

### E. Typography, punctuation & spacing

- `Oops! Firefox crashed` — `pl/firefox-ios.xliff` — Emoticon ":(" added that is not in the source, and the "Oops!" interjection is dropped.
    - Current: `Firefox uległ awarii :(`
    - Source: `Oops! Firefox crashed`
    - Suggest: `O nie! Firefox uległ awarii`
    - The en-US title is "Oops! Firefox crashed"; the Polish drops the interjection and substitutes a text emoticon, which is not standard UI typography.
- `Open articles in Reader View by tapping the book icon when it appears in the title bar.` — `pl/firefox-ios.xliff` — Missing comma before the adverbial participle clause "stukając".
    - Current: `widoku poprawionej czytelności stukając ikonę`
    - Source: `Open articles in Reader View by tapping the book icon when it appears in the title bar.`
    - Suggest: `widoku poprawionej czytelności, stukając ikonę`
    - Polish punctuation requires a comma before an imiesłowowy równoważnik zdania ("stukając…").
- `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.` — `pl/firefox-ios.xliff` — Missing comma before the adverbial participle clause "stukając".
    - Current: `Zachowuj strony w czytelni stukając ikonę`
    - Source: `Save pages to your Reading List by tapping the book plus icon in the Reader View controls.`
    - Suggest: `Zachowuj strony w czytelni, stukając ikonę`
    - Polish punctuation requires a comma before an imiesłowowy równoważnik zdania ("stukając…").
- `The page could not be displayed in Reader View.` — `pl/firefox-ios.xliff` — Missing sentence-final period present in the source.
    - Current: `Strona nie może zostać wyświetlona w widoku poprawionej czytelności`
    - Source: `The page could not be displayed in Reader View.`
    - Suggest: `Strona nie może zostać wyświetlona w widoku poprawionej czytelności.`
    - The en-US string ends with a period; the Polish translation drops the final punctuation.

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
