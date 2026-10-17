# Firefox iOS l10n QA — sv-SE

| | |
|---|---|
| **Generated** | 2026-10-17 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `09d125f6a298` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `09d125f6a298` |
| **Previous run** | 2026-10-16 @ `8c3a631663df` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sv-SE: [android](android.md) · [firefox](firefox.md)

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
| Files | 97 |
| Strings | 1,927 |
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
| quotes | `straight-double` 10, `curly-double` 2, `curly-single` 2 | **straight-double** |
| apostrophe | `typographic` 2 | **typographic** |
| ellipsis | `char` 28 | **char** |
| dash | `em` 3, `en` 3 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (49)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 17 |
| 3 | Degraded language (grammar, spelling, terminology) | 31 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `Settings.AppIconSelection.AppIconNames.Pixelated.Title.v136` — `sv-SE/firefox-ios.xliff` — "Avpixlat" reads as "de-pixelated", the opposite of "Pixelated".
    - Current: `Avpixlat`
    - Source: `Pixelated`
    - Suggest: `Pixlad`
    - The comment describes a pixelated version of the icon. In Swedish, "pixla" means to pixelate and the prefix "av-" means removing it, so "avpixlat" says the reverse.
- `Logins.PaymentMethods.DevicePasscodeRequired.Message.v124.v2` — `sv-SE/firefox-ios.xliff` — The Apple feature names Face ID and Touch ID are wrongly hyphenated, which also makes them inconsistent with the sibling passcode string.
    - Current: `Face-ID, Touch-ID`
    - Source: `To save and autofill credit cards, enable Face ID, Touch ID, or a device passcode.`
    - Suggest: `Face ID, Touch ID`
    - Face ID and Touch ID are Apple product names written without a hyphen. Logins.DevicePasscodeRequired.Message.v122 in the same file uses the correct form.
- `Addresses.EditAddress.AutofillAddressDepartment.v129` — `sv-SE/firefox-ios.xliff` — Administrative "Department" is translated as "Avdelning", which means a department in an organisation.
    - Current: `Avdelning`
    - Source: `Department`
    - Suggest: `Departement`
    - The comment says this is the administrative division used in France and Colombia. In Swedish that is "departement". "Avdelning" means a section of a company or organisation.
- `Addresses.EditAddress.AutofillAddressPin.v129` — `sv-SE/firefox-ios.xliff` — "Pin" (India's Postal Index Number) is translated as the verb "Fäst" (to pin/attach).
    - Current: `Fäst`
    - Source: `Pin`
    - Suggest: `PIN-kod`
    - The developer comment says this is the PIN postal code field used in India. "Fäst" means to pin or fasten something, which is the wrong sense for an address field.
- `Menu.EnhancedTrackingProtection.Certificates.SubjectAltNames.v131` — `sv-SE/firefox-ios.xliff` — "Subject Alt Names" (the certificate's alternative subject names) is translated as "Ämne eller namn", which means "Subject or name".
    - Current: `Ämne eller namn`
    - Source: `Subject Alt Names`
    - Suggest: `Alternativa ämnesnamn`
    - In the source, "Alt" is short for "Alternative", as in the certificate's Subject Alternative Name field. The Swedish reads "Alt" as "or" and renders it as "eller", so it no longer names that field. The neighbouring string uses "Ämnesnamn" for Subject Name, so "Alternativa ämnesnamn" would match it.
- `Menu.EnhancedTrackingProtection.ClearData.ToastMessage.v128` — `sv-SE/firefox-ios.xliff` — The toast uses the present passive ("are being removed") where the source reports a completed removal.
    - Current: `Kakor och webbplatsdata tas bort`
    - Source: `Cookies and site data removed`
    - Suggest: `Kakor och webbplatsdata har tagits bort`
    - The en-US "Cookies and site data removed" confirms that the removal is done. The Swedish "tas bort" reads as in progress or about to happen, so the confirmation says something different.
- `Onboarding.Modern.BrandRefresh.TermsOfUse.Description.v148` — `sv-SE/firefox-ios.xliff` — "won't sell you out" (won't betray you / sell your data) is rendered as "won't expose you".
    - Current: `kommer inte att avslöja dig`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `säljer inte ut dig`
    - "Sell you out" means betray, here alluding to not selling user data; "avslöja dig" means reveal/expose you, which is a different claim.
- `Onboarding.Welcome.Description.TreatementA.v120` — `sv-SE/firefox-ios.xliff` — "non-profit backed browser" is translated as "non-profit browser", which drops the meaning that the browser is backed by a non-profit.
    - Current: `Vår icke-vinstdrivande webbläsare`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `Vår webbläsare, som stöds av en ideell organisation,`
    - The en-US says the browser is backed by a non-profit, not that the browser itself is non-profit. The Swedish describes the product as non-profit.
- `Onboarding.Welcome.Description.v120` — `sv-SE/firefox-ios.xliff` — "non-profit backed browser" is translated as "non-profit browser", which drops the meaning that the browser is backed by a non-profit.
    - Current: `Vår icke-vinstdrivande webbläsare`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `Vår webbläsare, som stöds av en ideell organisation,`
    - The en-US says the browser is backed by a non-profit, not that the browser itself is non-profit. The Swedish describes the product as non-profit.
- `Settings.Summarize.FooterTitle.v142` — `sv-SE/firefox-ios.xliff` — "sammanfattningssidor" means "summary pages" instead of "summarizing pages".
    - Current: `Ger tillgång till sammanfattningssidor.`
    - Source: `Provides access to summarize pages.`
    - Suggest: `Ger tillgång till att sammanfatta sidor.`
    - The en-US says the setting gives access to summarizing pages, which is what the Summarize feature does. The Swedish compound "sammanfattningssidor" names a kind of page ("summary pages") and does not describe the action.
- `WebCompatReporter.Preview.ScreenshotAccessibilityLabel.v154` — `sv-SE/firefox-ios.xliff` — 'Double tap' is translated as 'Dubbelklicka' (double-click) in a touch accessibility hint.
    - Current: `Dubbelklicka för att visa helskärm.`
    - Source: `Screenshot of the page you are reporting. Double tap to view full screen.`
    - Suggest: `Dubbeltryck för att visa helskärm.`
    - On iOS the gesture is a tap, and Swedish iOS/VoiceOver calls it 'dubbeltryck'; 'dubbelklicka' refers to a mouse.
- `WebCompatReporter.SubOption.CaptionsMissing.v154` — `sv-SE/firefox-ios.xliff` — Video captions rendered as 'Bildtexter' (image captions) instead of subtitles/captions for video.
    - Current: `Bildtexter saknas`
    - Source: `Captions are missing`
    - Suggest: `Undertexter saknas`
    - The option sits under 'Video or audio does not play'; captions here are video subtitles ('undertexter'), whereas 'bildtexter' means captions under pictures.
- `ContextMenu.DownloadLinkButtonTitle` — `sv-SE/firefox-ios.xliff` — The action "Download Link" is translated as the noun "Nedladdningslänk" (a download link) instead of as a command.
    - Current: `Nedladdningslänk`
    - Source: `Download Link`
    - Suggest: `Ladda ner länk`
    - The developer comment calls this a context menu item for downloading a link URL, so it is an action. "Nedladdningslänk" means "a download link" and reads as a label, not a command, unlike the other menu items ("Kopiera länk", "Dela länk").
- `Display Settings` — `sv-SE/firefox-ios.xliff` — "Display" is translated as a physical monitor (bildskärm), but the comment says it means presentation.
    - Current: `Bildskärmsinställningar`
    - Source: `Display Settings`
    - Suggest: `Visningsinställningar`
    - The developer comment says this is the reader-mode display settings button and that 'Display' means presentation, not monitor. 'Bildskärm' means a physical screen or monitor.
- `FxA.ManageAccount` — `sv-SE/firefox-ios.xliff` — Singular "Account" is rendered as plural "konton".
    - Current: `Hantera konton & enheter`
    - Source: `Manage Account & Devices`
    - Suggest: `Hantera konto & enheter`
    - The source means the user's single Firefox Account ("Manage Account & Devices"). "konton" means "accounts" (plural).
- `Menu.TrackingProtectionDescription.CryptominersNew` — `sv-SE/firefox-ios.xliff` — The word "secretly" from the source is missing in the Swedish.
    - Current: `Kryptogrävare använder ditt systems datakraft`
    - Source: `Cryptominers secretly use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `Kryptogrävare använder i hemlighet ditt systems datakraft`
    - The en-US says cryptominers "secretly use" your computing power. The Swedish drops "i hemlighet", so it loses the point that the mining happens without the user knowing.
- `Settings.Home.Option.Wallpaper.Accessibility.TwilightHillsWallpaper.v100` — `sv-SE/firefox-ios.xliff` — "Twilight hills" is rendered as "beach hills at twilight" (strandkullar), which adds a beach that is not in the source.
    - Current: `mönster med strandkullar i skymning`
    - Source: `Firefox wallpaper, twilight hills pattern.`
    - Suggest: `mönster med kullar i skymning`
    - The en-US says "twilight hills pattern", with no beach. "strand" seems to have been copied from the BeachHills string, so this wallpaper is described wrongly and is easy to confuse with the beach hills one.
- `Settings.Passwords.OnboardingMessage.v103` — `sv-SE/firefox-ios.xliff` — Apple feature names Face ID and Touch ID are altered with hyphens.
    - Current: `Face-ID, Touch-ID`
    - Source: `Your passwords are now protected by Face ID, Touch ID or a device passcode.`
    - Suggest: `Face ID, Touch ID`
    - Face ID and Touch ID are Apple product names and Apple's Swedish localization keeps them unhyphenated; brand names should not be modified.
- `read` — `sv-SE/firefox-ios.xliff` — The accessibility label for a read article uses the imperative "läs" instead of the participle "läst".
    - Current: `läs`
    - Source: `read`
    - Suggest: `läst`
    - The developer comment says "read" is a past participle used as an adjective, the counterpart of "unread" (translated "oläst"). "läs" is the command form ("read!"), so VoiceOver would announce an instruction instead of the article's status.
- `Menu.DownloadPDF.Confirm.v129` — `sv-SE/firefox-ios.xliff` — The toast is an unfinished relative clause ("the PDF file that was downloaded") rather than a confirmation that the download succeeded.
    - Current: `PDF-filen som hämtats`
    - Source: `Successfully Downloaded PDF`
    - Suggest: `PDF-filen har hämtats`
    - The en-US "Successfully Downloaded PDF" confirms a completed download. The Swedish only names the file in a clause with no main verb, so it confirms nothing.

### C. Grammar, agreement & spelling

- `AddressToolbar.PrivacyAndSecuriySettings.A11y.Label.v128` — `sv-SE/firefox-ios.xliff` — The first part of the compound that shares its second half is missing its hyphen ("Sekretess-").
    - Current: `Sekretess & säkerhetsinställningar`
    - Source: `Privacy & Security Settings`
    - Suggest: `Sekretess- & säkerhetsinställningar`
    - In Swedish, when two compounds share an ending, the first one keeps a hyphen to show the shared part ("sekretess- och säkerhetsinställningar"). Without it, the label reads as "Privacy" plus "security settings" instead of "Privacy & Security Settings".
- `Bookmarks.Menu.SavedBookmarkToastDefaultFolderLabel.v136` — `sv-SE/firefox-ios.xliff` — Participle does not agree with the neuter noun "bokmärke" that the toast refers to.
    - Current: `Sparad i`
    - Source: `Saved in “Bookmarks”`
    - Suggest: `Sparat i`
    - The toast reports that a bookmark (ett bokmärke, neuter) was saved, so the participle should be the neuter form "sparat".
- `Bookmarks.Menu.SavedBookmarkToastLabel.v136` — `sv-SE/firefox-ios.xliff` — Participle does not agree with the neuter noun "bokmärke" that the toast refers to.
    - Current: `Sparad i`
    - Source: `Saved in “%@”`
    - Suggest: `Sparat i`
    - The toast reports that a bookmark (ett bokmärke, neuter) was saved in a folder, so the neuter form "sparat" is required.
- `BrowserDataTransfer.Settings.SectionTitle.v160` — `sv-SE/firefox-ios.xliff` — Missing hyphen marking the shared first part of the compound in the coordinated compounds.
    - Current: `Dataimport och export`
    - Source: `Data Import and Export`
    - Suggest: `Dataimport och -export`
    - In Swedish, when two compounds share a first part that is written only once, the second compound needs a hyphen ("-export"). Without it, the text reads as "data import and export (in general)".
- `FirefoxHomepage.FeltDeletion.Link.v122` — `sv-SE/firefox-ios.xliff` — The participle doesn't agree with the plural noun phrase "Privata surfdata".
    - Current: `Privata surfdata raderad`
    - Source: `Private Browsing Data Erased`
    - Suggest: `Privata surfdata raderade`
    - "Privata" treats "surfdata" as plural, so the participle should also be plural ("raderade"), not the common-gender singular "raderad".
- `MainMenu.Submenus.Tools.WebsiteDarkMode.Title.v141` — `sv-SE/firefox-ios.xliff` — "Webbplats mörkt läge" copies the English noun-in-front order, which is ungrammatical in Swedish.
    - Current: `Webbplats mörkt läge`
    - Source: `Website Dark Mode`
    - Suggest: `Mörkt läge för webbplatser`
    - Swedish cannot put a bare noun before an adjective phrase like this. The meaning "Website Dark Mode" needs a prepositional phrase ("Mörkt läge för webbplatser") or a compound.
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Automatic.v148` — `sv-SE/firefox-ios.xliff` — Adjective uses common gender while the sibling theme options (Mörkt, Ljust) agree with neuter "tema".
    - Current: `Automatisk`
    - Source: `Automatic`
    - Suggest: `Automatiskt`
    - The three options all modify the same implied noun "tema" (neuter); Dark/Light are rendered "Mörkt"/"Ljust", so Automatic must be "Automatiskt" for agreement and consistency.
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `sv-SE/firefox-ios.xliff` — The pronoun "en" doesn't agree with the neuter noun "e-postalias" (ett alias).
    - Current: `vi valde ut en som du kan återanvända`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `vi valde ut ett som du kan återanvända`
    - "Alias" is a neuter noun, so the pronoun referring back to it must be "ett". The same file already treats it as neuter ("E-postalias infogat").
- `TermsOfUse.Description.v142` — `sv-SE/firefox-ios.xliff` — "ett användarvillkor" uses the singular, meaning one term of use, instead of the Terms of Use as a document.
    - Current: `introducerat ett användarvillkor för %@`
    - Source: `We’ve introduced a %@ Terms of Use and updated our Privacy Notice.`
    - Suggest: `infört användarvillkor för %@`
    - The source means the Terms of Use document. In Swedish that is the plural "användarvillkor" with no article, and "ett användarvillkor" reads as a single condition.
- `TermsOfUse.Link.TermsOfUse.v142` — `sv-SE/firefox-ios.xliff` — The capital A in "Användarvillkor" copies English title case, which Swedish doesn't use mid-phrase.
    - Current: `%@ Användarvillkor`
    - Source: `%@ Terms of Use`
    - Suggest: `Användarvillkor för %@`
    - Swedish doesn't capitalise common nouns after the product name. "%@ Användarvillkor" follows the English pattern, while "Användarvillkor för %@" (or "%@ användarvillkor") is correct.
- `WebCompatReporter.Preview.Data.TrackingProtectionSetting.v155` — `sv-SE/firefox-ios.xliff` — 'Förbättrad' modifies the setting rather than the feature name Enhanced Tracking Protection.
    - Current: `Förbättrad spårningsskyddsinställning`
    - Source: `Enhanced Tracking Protection setting for this site`
    - Suggest: `Inställning för förbättrat spårningsskydd`
    - The source means the setting of Enhanced Tracking Protection ('förbättrat spårningsskydd'), but the Swedish reads as 'an enhanced tracking-protection setting'.
- `ActivityStream.Library.Title` — `sv-SE/firefox-ios.xliff` — The section title uses the singular participle "sparad" where a heading for a list of saved items needs the plural.
    - Current: `Nyligen sparad`
    - Source: `Recently Saved`
    - Suggest: `Nyligen sparade`
    - "Recently Saved" heads a section listing multiple saved items; Swedish needs the plural "sparade", matching the parallel heading "Nyligen besökta".
- `FxHomepage.Wallpaper.ButtonLabel.v99` — `sv-SE/firefox-ios.xliff` — The compound noun is incorrectly split; it should be hyphenated as "Firefox-logotyp".
    - Current: `Firefox logotyp`
    - Source: `Firefox logo, change the wallpaper.`
    - Suggest: `Firefox-logotyp`
    - In Swedish, a brand name joined to a common noun forms a hyphenated compound. Writing it as two words is a split-compound (särskrivning) error.
- `Keyboard.Shortcuts.ShowFirstTab` — `sv-SE/firefox-ios.xliff` — "första flik" uses the indefinite form "flik" where Swedish needs the definite form "fliken".
    - Current: `Visa första flik`
    - Source: `Show First Tab`
    - Suggest: `Visa första fliken`
    - In Swedish, "första" needs the definite noun form ("första fliken"). The matching shortcut in the same overlay already says "Visa sista fliken", so the two labels are also inconsistent.
- `OpenURL.Error.Message` — `sv-SE/firefox-ios.xliff` — Pronoun "det" does not agree with the common-gender noun "sidan".
    - Current: `eftersom det har en ogiltig adress`
    - Source: `Firefox cannot open the page because it has an invalid address.`
    - Suggest: `eftersom den har en ogiltig adress`
    - "sida" is common gender (en sida), so the pronoun that refers back to it must be "den".
- `SendTo.Error.Message` — `sv-SE/firefox-ios.xliff` — The compound 'HTTP- och HTTPS-länkar' is wrongly split into separate words, which Swedish grammar does not allow (särskrivning).
    - Current: `HTTP och HTTPS länkar`
    - Source: `Only HTTP and HTTPS links can be shared.`
    - Suggest: `HTTP- och HTTPS-länkar`
    - In Swedish, an abbreviation joined to a noun is written with a hyphen. When two such compounds share the same final part, the first one takes a trailing hyphen. 'HTTP och HTTPS länkar' is a grammatical error.
- `Settings.Disconnect.Body` — `sv-SE/firefox-ios.xliff` — Agreement error: plural possessive "dina" used with the uncountable en-noun "webbinformation".
    - Current: `någon av dina webbinformation`
    - Source: `Firefox will stop syncing with your account, but won’t delete any of your browsing data on this device.`
    - Suggest: `någon av din webbinformation`
    - "Webbinformation" is a singular, uncountable common-gender noun, so "någon av dina webbinformation" is ungrammatical. It needs "din" to agree.
- `Settings.Home.Option.RecentlySaved` — `sv-SE/firefox-ios.xliff` — Singular participle "sparad" used for a section title that refers to multiple saved items.
    - Current: `Nyligen sparad`
    - Source: `Recently Saved`
    - Suggest: `Nyligen sparade`
    - The section lists recently saved items, so the participle should be plural. The sibling option "Nyligen besökta" correctly uses the plural.
- `Settings.ShowLoginsInAppMenu.Title` — `sv-SE/firefox-ios.xliff` — "appmenyer" is indefinite plural ("app menus"), but the source refers to the single application menu.
    - Current: `Visa i appmenyer`
    - Source: `Show in Application Menu`
    - Suggest: `Visa i appmenyn`
    - en-US "Show in Application Menu" refers to one specific menu; Swedish needs the definite singular "appmenyn".
- `%@ search` — `sv-SE/firefox-ios.xliff` — "%@ sök" is ungrammatical: "sök" is the imperative verb, not a noun meaning "a search".
    - Current: `%@ sök`
    - Source: `%@ search`
    - Suggest: `%@-sökning`
    - The label means "<engine> search" (for example "Google search"). Swedish needs the noun "sökning", joined with a hyphen after the name.
- `TodayWidget.MoreTabsLabel` — `sv-SE/firefox-ios.xliff` — "+%d Mer…" uses the uncountable "mer" with a capital letter for a count of extra tabs.
    - Current: `+%d Mer…`
    - Source: `+%d More…`
    - Suggest: `+%d fler…`
    - The label counts additional open tabs, which are countable, so Swedish needs "fler" (or "till"), not "mer". The capital M copies English title case, which Swedish does not use.

### D. Terminology, register & consistency

- `Settings.AppIconSelection.ScreenTitle.v136` — `sv-SE/firefox-ios.xliff` — The title spells the compound "App-ikon" with a hyphen, while the same screen uses "appikonen".
    - Current: `App-ikon`
    - Source: `App Icon`
    - Suggest: `Appikon`
    - The accessibility hint on the same screen uses the closed compound "appikonen". "Appikon" is the standard Swedish spelling, so the title should match.
- `DefaultBrowserPopup.SecondLabel.v114` — `sv-SE/firefox-ios.xliff` — The step names an iOS Settings item with wording that doesn't match the Swedish iOS label "Förvald webbläsarapp".
    - Current: `Förvald app för webbläsare`
    - Source: `2. Tap *Default Browser App*`
    - Suggest: `Förvald webbläsarapp`
    - The instruction tells users which item to tap in iOS Settings, so it should match the system's Swedish label. As I recall it, that label is "Förvald webbläsarapp". A different wording makes the item harder to find.
- `WebCompatReporter.SubOption.ItemsMisaligned.v154` — `sv-SE/firefox-ios.xliff` — 'Items' is rendered as 'Föremål' here but as 'Objekten' in a sibling option on the same form.
    - Current: `Föremålen är feljusterade`
    - Source: `Items are misaligned`
    - Suggest: `Objekten är feljusterade`
    - These are sibling sub-options under 'Design is broken'; ItemsOverlapped uses 'Objekten'. 'Föremål' means physical objects and fits page elements poorly. The same applies to ItemsNotVisible ('Föremål som inte är helt synliga').
- `WebCompatReporter.SubOption.MissingItems.v154` — `sv-SE/firefox-ios.xliff` — 'Items' is rendered as 'Föremål', inconsistent with 'Objekten' elsewhere in the same form.
    - Current: `Föremål saknas`
    - Source: `Missing items`
    - Suggest: `Objekt saknas`
    - The same source term should be consistent within the Report a Website Issue form, and 'föremål' denotes physical objects rather than page elements.
- `Address.Bar.ReadingList.v106` — `sv-SE/firefox-ios.xliff` — "Reading List" lacks the definite form here, which is inconsistent with "Lägg till i läslistan" for the same source in the same file.
    - Current: `Lägg till i läslista`
    - Source: `Add to Reading List`
    - Suggest: `Lägg till i läslistan`
    - The same feature name is rendered "läslistan" in "Add to Reading List" and "Added page to Reading List"; the bare indefinite form reads incomplete in Swedish.
- `Menu.AddToReadingList.Confirm` — `sv-SE/firefox-ios.xliff` — "Reading List" is rendered as "läsningslistan" here but as "Läslista"/"läslistan" in the other menu strings and toasts.
    - Current: `Tillagd till läsningslistan`
    - Source: `Added To Reading List`
    - Suggest: `Tillagd i läslistan`
    - Menu.ReadingList.Label uses "Läslista" and Menu.RemoveReadingList.Confirm.v99 uses "läslistan"; the same feature should have one name within this group.
- `TodayWidget.QuickActionGalleryDescription` — `sv-SE/firefox-ios.xliff` — The Home screen is called "startskärm" here but "hemskärm" in the neighbouring widget description.
    - Current: `startskärm`
    - Source: `Add a Firefox shortcut to your Home screen. After adding the widget, touch and hold to edit it and select a different shortcut.`
    - Suggest: `hemskärm`
    - TodayWidget.FirefoxShortcutGalleryDescription on the same widget gallery screen says "din hemskärm", and Apple's Swedish term for the iOS Home screen is "hemskärm". Using two terms on one screen is inconsistent.

### E. Typography, punctuation & spacing

- `Bookmarks.Menu.DeletedBookmark.v131` — `sv-SE/firefox-ios.xliff` — Uses English-style curly quotes instead of the locale's straight double quotes.
    - Current: `Tog bort “%@”`
    - Source: `Deleted “%@”`
    - Suggest: `Tog bort "%@"`
    - The sv-SE convention is straight double quotes, and sibling toasts in the same file use "…". The “…” pairing is English style and inconsistent here.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sv-SE/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
