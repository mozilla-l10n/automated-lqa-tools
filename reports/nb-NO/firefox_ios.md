# Firefox iOS l10n QA — nb-NO

| | |
|---|---|
| **Generated** | 2026-10-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7f349c067169` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefoxios-l10n` @ `7f349c067169` |
| **Previous run** | 2026-10-19 @ `ec61063c1c68` |
| **Mode** | incremental |
| **Strings reviewed this run** | 12 of 1,927 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.




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
| Missing strings | 46 |
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

**46 strings** are not translated yet, concentrated in:

- `Shared/Supporting Files/en-US.lproj/VPN.strings` — 20
- `nb-NO/firefox-ios.xliff` — 17
- `nb-NO/firefox-ios.xliff` — 7
- `nb-NO/firefox-ios.xliff` — 2

**Files absent from the locale:**

- `Shared/Supporting Files/en-US.lproj/VPN.strings`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 14 | **guillemet** |
| ellipsis | `char` 28 | **char** |
| dash | `em` 2, `en` 2 | _mixed_ |
| nbsp | `total` 1 | **total** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (34)

> **Reads as a deliberate edit (3).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `Onboarding.Welcome.Description.TreatementA.v120` — `nb-NO/firefox-ios.xliff` — 'helps stop' is rendered as 'forhindrer' (prevents), which makes an absolute promise the source does not make.
    - Current: `forhindrer selskaper i å spore`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `bidrar til å hindre selskaper i å spore`
    - The en-US says the browser only 'helps stop' companies from tracking. 'forhindrer' claims it prevents tracking outright.
- `Onboarding.Welcome.Description.v120` — `nb-NO/firefox-ios.xliff` — 'helps stop' is rendered as 'forhindrer' (prevents), which makes an absolute promise the source does not make.
    - Current: `forhindrer selskaper i å spore`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `bidrar til å hindre selskaper i å spore`
    - The en-US says the browser only 'helps stop' companies from tracking. 'forhindrer' claims it prevents tracking outright.
- `CoverSheet.v24.ETP.Description` — `nb-NO/firefox-ios.xliff` — The translation drops "helps", so a hedged claim about tracking protection becomes an absolute promise that it prevents ad tracking.
    - Current: `forhindrer reklame i å spore aktivitetene dine på nettet`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `bidrar til å hindre reklame i å følge deg rundt på nettet`
    - The en-US says protection "helps stop ads from following you around". The nb-NO "forhindrer" means "prevents", which promises full protection the product never claimed.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 8 |
| 3 | Degraded language (grammar, spelling, terminology) | 25 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `AddressToolbar.GoogleLens.A11yLabel.v153.v2` — `nb-NO/firefox-ios.xliff` — "Søk etter bilde" means "search for an image", but the button searches using an image.
    - Current: `Søk etter bilde med Google Lens`
    - Source: `Search image with Google Lens`
    - Suggest: `Søk med bilde i Google Lens`
    - The developer comment says the user takes or picks a photo to search with Google Lens, so the image is what you search with, not what you search for. The nb-NO label tells screen-reader users the button finds images.
- `Bookmarks.Menu.MoreOptionsA11yLabel.v136` — `nb-NO/firefox-ios.xliff` — "More options" is rendered as "Flere innstillinger" ("More settings"), but the button opens a list of more actions.
    - Current: `Flere innstillinger`
    - Source: `More options`
    - Suggest: `Flere alternativer`
    - The comment says this button opens a modal with more actions for the bookmark. "Innstillinger" means settings or preferences, which is not what this button opens.
- `Addresses.EditAddress.AutofillAddressCounty.v129` — `nb-NO/firefox-ios.xliff` — "County" is translated as "Land" (country), duplicating the Country field label.
    - Current: `Land`
    - Source: `County`
    - Suggest: `Fylke`
    - "Land" means country, not county. The Country field on the same screen also uses "Land", so the two fields can't be told apart. The usual Norwegian equivalent of county is "Fylke".
- `Addresses.EditAddress.AutofillAddressDepartment.v129` — `nb-NO/firefox-ios.xliff` — "Department" is translated as "Avdeling" (a department of an organisation) rather than the administrative region.
    - Current: `Avdeling`
    - Source: `Department`
    - Suggest: `Departement`
    - The developer comment says this is the administrative division used in France and Colombia. In Norwegian that is "departement". "Avdeling" means a department of a company or organisation.
- `Onboarding.Welcome.Description.TreatementA.v120` — `nb-NO/firefox-ios.xliff` — 'helps stop' is rendered as 'forhindrer' (prevents), which makes an absolute promise the source does not make.
    - Current: `forhindrer selskaper i å spore`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `bidrar til å hindre selskaper i å spore`
    - The en-US says the browser only 'helps stop' companies from tracking. 'forhindrer' claims it prevents tracking outright.
- `Onboarding.Welcome.Description.v120` — `nb-NO/firefox-ios.xliff` — 'helps stop' is rendered as 'forhindrer' (prevents), which makes an absolute promise the source does not make.
    - Current: `forhindrer selskaper i å spore`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `bidrar til å hindre selskaper i å spore`
    - The en-US says the browser only 'helps stop' companies from tracking. 'forhindrer' claims it prevents tracking outright.
- `CoverSheet.v24.ETP.Description` — `nb-NO/firefox-ios.xliff` — The translation drops "helps", so a hedged claim about tracking protection becomes an absolute promise that it prevents ad tracking.
    - Current: `forhindrer reklame i å spore aktivitetene dine på nettet`
    - Source: `Built-in Enhanced Tracking Protection helps stop ads from following you around. Turn on Strict to block even more trackers, ads, and popups.`
    - Suggest: `bidrar til å hindre reklame i å følge deg rundt på nettet`
    - The en-US says protection "helps stop ads from following you around". The nb-NO "forhindrer" means "prevents", which promises full protection the product never claimed.
- `Display Settings` — `nb-NO/firefox-ios.xliff` — "Skjerminnstillinger" means screen/monitor settings, but the comment says "display" here means presentation, not monitor.
    - Current: `Skjerminnstillinger`
    - Source: `Display Settings`
    - Suggest: `Visningsinnstillinger`
    - The developer comment says "Display in the meaning of presentation, not monitor." This button opens reader-mode settings for font, size and theme. "Skjerm" means the physical screen, so the translation uses exactly the sense the comment rules out.

### C. Grammar, agreement & spelling

- `Menu.EnhancedTrackingProtection.Details.Trackers.Analytics.v132` — `nb-NO/firefox-ios.xliff` — The Norwegian compound noun is wrongly split with a hyphen.
    - Current: `Sporings-innhold`
    - Source: `Tracking content: %@`
    - Suggest: `Sporingsinnhold`
    - In Norwegian, compounds are written as one word. A hyphen is only used in special cases such as abbreviations or numbers, so the correct form is "Sporingsinnhold".
- `Menu.EnhancedTrackingProtection.SwitchOff.Text.v129` — `nb-NO/firefox-ios.xliff` — Pronoun 'det' does not agree with the plural antecedent 'Beskyttelser'.
    - Current: `slår det på igjen`
    - Source: `Protections are OFF. We suggest turning them back on.`
    - Suggest: `slår dem på igjen`
    - The source 'turning them back on' refers to the plural 'Protections' ('Beskyttelser'), so the object pronoun must be plural 'dem', not singular neuter 'det'.
- `Onboarding.Customization.Theme.Dark.Action.v123` — `nb-NO/firefox-ios.xliff` — The adjective "Mørk" doesn't agree with the neuter "tema", and it doesn't match the neighbouring option "Lyst".
    - Current: `Mørk`
    - Source: `Dark`
    - Suggest: `Mørkt`
    - The theme options on the same card describe a neuter noun (tema). The Light option correctly uses the neuter "Lyst", but Dark uses the common-gender "Mørk". The v148 string for the same option correctly uses "Mørkt".
- `Onboarding.Modern.BrandRefresh.Customization.Theme.Description.v148` — `nb-NO/firefox-ios.xliff` — Compound favoritt+temaet is misspelled with a dropped consonant.
    - Current: `favorittemaet`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `favoritttemaet`
    - Under current Bokmål spelling rules, a compound keeps all three identical consonants where its parts join (or uses a hyphen: favoritt-temaet). The current form 'favorittemaet' is a misspelling.
- `Onboarding.Modern.Customization.Theme.Description.v145` — `nb-NO/firefox-ios.xliff` — Compound favoritt+temaet is misspelled with a dropped consonant.
    - Current: `favorittemaet`
    - Source: `Pick your favorite theme or have %@ match your device, putting you in control.`
    - Suggest: `favoritttemaet`
    - Under current Bokmål spelling rules, a compound keeps all three identical consonants where its parts join (or uses a hyphen: favoritt-temaet). The current form 'favorittemaet' is a misspelling.
- `Onboarding.Wallpaper.Title.v114` — `nb-NO/firefox-ios.xliff` — Wrong article gender: 'bakgrunnsbilde' is neuter and needs 'et', not 'en'.
    - Current: `Velg en %@-bakgrunnsbilde`
    - Source: `Choose a %@ Wallpaper`
    - Suggest: `Velg et %@-bakgrunnsbilde`
    - 'bilde' is a neuter noun in Bokmål, so it takes the indefinite article 'et'.
- `PrivacyDashboard.TrackingContent.v155` — `nb-NO/firefox-ios.xliff` — The Norwegian compound is wrongly written with a hyphen.
    - Current: `Sporings-innhold`
    - Source: `Tracking Content`
    - Suggest: `Sporingsinnhold`
    - In Norwegian, compounds like this are written as one word: "Sporingsinnhold", which is also the usual term in Firefox nb-NO. The hyphen here is a spelling error.
- `RelayMask.RelayEmailMaskFreeTierLimitReached.v147` — `nb-NO/firefox-ios.xliff` — Gender agreement error: "alias" is neuter, so the pronoun must be "ett", not "én".
    - Current: `så vi valgte én du kan bruke om igjen`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `så vi valgte ett du kan bruke om igjen`
    - "et alias" is a neuter noun in Bokmål; the pronoun that refers back to one e-postalias must agree in gender, so it should be "ett".
- `Search.EngineSection.Title.v108` — `nb-NO/firefox-ios.xliff` — A compound made of a name and a noun is written as two separate words; it needs a hyphen, as in "Google-søk".
    - Current: `%@ søk`
    - Source: `%@ search`
    - Suggest: `%@-søk`
    - In Norwegian, a compound of a proper name and a noun takes a hyphen. The same file already writes "Google-søk", so "%@ søk" is a split-compound (særskriving) error.
- `Settings.ScrollToHideTabAndAddressBar.Title.v138` — `nb-NO/firefox-ios.xliff` — "Skjul" has a capital letter in the middle of the sentence, which is wrong in Norwegian.
    - Current: `Rull til Skjul fane`
    - Source: `Scroll to Hide Tab and Address Bar`
    - Suggest: `Rull til skjul fane`
    - Norwegian doesn't use title case. The English title case shouldn't carry over to a word in the middle of a running phrase, and here the capital makes "Skjul" look like the name of a separate command.
- `DefaultBrowserCard.NextLevel.Description.v108` — `nb-NO/firefox-ios.xliff` — The Norwegian word for "speed" is misspelled as "fårt" instead of "fart".
    - Current: `få fårt`
    - Source: `Choose Firefox as your default browser to make speed, safety, and privacy automatic.`
    - Suggest: `få fart`
    - The source says "speed", which in Norwegian is "fart". "fårt" is not a Norwegian word.
- `Menu.TrackingProtectionBlockedContent.Title` — `nb-NO/firefox-ios.xliff` — Norwegian compound wrongly hyphenated.
    - Current: `Sporings-innhold`
    - Source: `Tracking content`
    - Suggest: `Sporingsinnhold`
    - Norwegian compounds are written as one word; the hyphen is a spelling error.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `nb-NO/firefox-ios.xliff` — Wrong word order in an indirect question.
    - Current: `hva gjør du på nettet`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `hva du gjør på nettet`
    - Indirect questions in Norwegian take subject-before-verb order; 'hva gjør du' is ungrammatical here. The en-US typo doesn't excuse the target grammar.
- `Menu.TrackingProtectionDescription.SocialNetworksNew` — `nb-NO/firefox-ios.xliff` — Indefinite noun after 'disse', and the term doesn't match 'sporere' used elsewhere.
    - Current: `disse sporfølgere`
    - Source: `Social networks place trackers on other websites to build a more complete and targeted profile of you. Blocking these trackers reduces how much social media companies can see what do you online.`
    - Suggest: `disse sporerne`
    - 'disse' requires the definite form, and the same sentence and screen render 'trackers' as 'sporere'.
- `ReopenAlert.Title` — `nb-NO/firefox-ios.xliff` — The adjective agreement is wrong: after "siste" the participle needs its definite form.
    - Current: `siste lukket fane`
    - Source: `Reopen Last Closed Tab`
    - Suggest: `sist lukkede fane`
    - In "siste lukket fane" the participle should take its definite (weak) form, "lukkede". The idiomatic phrase is "sist lukkede fane".
- `Reset text size` — `nb-NO/firefox-ios.xliff` — The imperative of "nullstille" is misspelled with a single l.
    - Current: `Nullstil`
    - Source: `Reset text size`
    - Suggest: `Nullstill`
    - The imperative of the verb "nullstille" is "nullstill", with a double l.
- `Send a crash report so Mozilla can fix the problem?` — `nb-NO/firefox-ios.xliff` — The infinitive "ordna" is the -a form used in Nynorsk; in Bokmål the infinitive ends in -e.
    - Current: `kan ordna problemet`
    - Source: `Send a crash report so Mozilla can fix the problem?`
    - Suggest: `kan ordne problemet`
    - In Bokmål the infinitive always ends in -e, so "ordna" is the wrong form here and doesn't match the rest of the nb-NO localization.
- `Settings.Home.Option.Wallpaper.Accessibility.SunriseWallpaper.v99` — `nb-NO/firefox-ios.xliff` — The compound "Firefox bakgrunnsbilde" is written as two words when it needs a hyphen, and the sibling wallpaper strings already use the hyphen.
    - Current: `Firefox bakgrunnsbilde`
    - Source: `Firefox wallpaper, sunrise pattern.`
    - Suggest: `Firefox-bakgrunnsbilde`
    - In Norwegian, a compound that starts with a proper name is joined with a hyphen. Writing it as two words is a spelling error (særskriving). The other wallpaper accessibility strings on the same screen all use "Firefox-bakgrunnsbilde".
- `Settings.NewTab.Option.FirefoxHome` — `nb-NO/firefox-ios.xliff` — The compound "Firefox startside" is written as two separate words; it needs a hyphen.
    - Current: `Firefox startside`
    - Source: `Firefox Home`
    - Suggest: `Firefox-startside`
    - In Norwegian, a compound noun whose first part is a proper name is joined with a hyphen. Writing it as two words (særskriving) is a spelling error. The same file already uses "Firefox-logoen".
- `Settings.TrackingProtection.ProtectionLevelStrict.Description` — `nb-NO/firefox-ios.xliff` — "sporerings-mekanismer" is misspelled and wrongly hyphenated; the correct compound is "sporingsmekanismer".
    - Current: `sporerings-mekanismer`
    - Source: `Blocks more trackers, ads, and popups. Pages load faster, but some functionality may not work.`
    - Suggest: `sporingsmekanismer`
    - "sporerings" is not a valid Norwegian form, and Norwegian compounds are written as one word without a hyphen.
- `TodayWidget.TopSitesGalleryDescription` — `nb-NO/firefox-ios.xliff` — "nylige" is the wrong form here. Modifying the participle "besøkte" needs the adverb "nylig".
    - Current: `ofte og nylige besøkte`
    - Source: `Add shortcuts to frequently and recently visited sites.`
    - Suggest: `ofte og nylig besøkte`
    - In "frequently and recently visited", both words are adverbs modifying "besøkte". The correct Bokmål form is "nylig", not the plural adjective "nylige".

### D. Terminology, register & consistency

- `MainMenu.Submenus.Tools.ReaderView.Off.Title.v131` — `nb-NO/firefox-ios.xliff` — Reader View is rendered "leservisning" here but "Lesevisning" in the subtitles of the same Tools submenu.
    - Current: `Slå av leservisning`
    - Source: `Turn off Reader View`
    - Suggest: `Slå av lesevisning`
    - The same feature name, Reader View, is spelled two different ways on the same menu screen. The subtitle strings use "Lesevisning", which I believe is the form used in other Firefox products, so the action titles should match it.
- `MainMenu.Submenus.Tools.ReaderView.On.Title.v131` — `nb-NO/firefox-ios.xliff` — Reader View is rendered "leservisning" here but "Lesevisning" in the subtitles of the same Tools submenu.
    - Current: `Slå på leservisning`
    - Source: `Turn on Reader View`
    - Suggest: `Slå på lesevisning`
    - The same feature name, Reader View, is spelled two different ways on the same menu screen. The subtitle strings use "Lesevisning", so the action titles should match it.
- `Settings.Search.Suggest.PrivateSession.Description.v125` — `nb-NO/firefox-ios.xliff` — Firefox Suggest is left in English here, but the rest of the Search settings screen calls it "Firefox-forslag".
    - Current: `Firefox Suggest`
    - Source: `Show suggestions from Firefox Suggest in private sessions`
    - Suggest: `Firefox-forslag`
    - Three other strings on the same screen use "Firefox-forslag": the section title, the link and its accessibility label. This string is the only one that keeps the English product name, so one feature shows up under two different names on the same page.
- `PzSrmZ-eHmH1H` — `nb-NO/firefox-ios.xliff` — The confirmation quotes the menu item as «Fjerne private faner», but the menu item itself is "Tøm private faner".
    - Current: `du vil «Fjerne private faner»?`
    - Source: `Just to confirm, you wanted ‘Clear Private Tabs’?`
    - Suggest: `du vil «Tøm private faner»?`
    - The quoted text should match the menu item name (eHmH1H "Tøm private faner"). The matching-options label fi3W24-eHmH1H already uses «Tøm private faner», so this string is inconsistent with both.

### E. Typography, punctuation & spacing

- `TopSites.RemovePage.Button` — `nb-NO/firefox-ios.xliff` — The separator dash is a plain hyphen instead of a dash.
    - Current: `Fjern side - %@`
    - Source: `Remove page — %@`
    - Suggest: `Fjern side – %@`
    - The en-US uses an em dash as a spaced separator. A hyphen is not a dash in nb-NO typography, where a spaced en dash is standard. The locale uses both en and em dashes elsewhere, never a hyphen in this role.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/nb-NO/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
