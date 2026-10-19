# Firefox l10n QA — sk

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `ba8eba5819d0` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `2d5e7eb1f225` |
| **Previous run** | 2026-10-16 @ `db2cfca9d18c` |
| **Mode** | incremental |
| **Strings reviewed this run** | 65 of 16,520 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sk: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (1)

- `migration-no-permissions-instructions-step2-2` — `browser/browser/migrationWizard.ftl` — The macOS variant tells the user to choose “Vybrať” (Select) when the source says “Open”.
    - Current: `V dialógovom okne na výber súborov zvoľte “Vybrať”`
    - Source: `{$sel_1 ->} [macos] In the file picker, choose “Open” [other] In the file picker, navigate to <code>{ $permissionsPath }</code> and choose “Select”`
    - Suggest: `V dialógovom okne na výber súborov zvoľte “Otvoriť”`
    - On macOS the en-US says to choose “Open”. Only the other variant says “Select”. With the wrong button name, the instruction points to a label that doesn't match the macOS picker.

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
| Files | 328 |
| Strings | 16,520 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 87 |
| Text quoting a UI label that no longer matches | 4 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 42 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 521, `curly-single` 79, `straight-double` 78, `german-double` 9 | **curly-double** |
| apostrophe | `typographic` 89, `straight` 54 | _mixed_ |
| ellipsis | `char` 401 | **char** |
| dash | `em` 27, `en` 67 | _mixed_ |
| nbsp | `total` 110, `before-punctuation` 3, `space-before-punctuation` 7 | **total** |

---

## 2. Systemic items (decisions, not line items)

- **plurals — 87 strings** — 87 strings. The locale's plural variants differ from what the rest of its tree does. At this scale it is a convention to settle once, not a defect per string.
    - Affected: `about-processes-active-threads`, `about-processes-inactive-threads`, `about-processes-profile-process`, `about-processes-tab-count`, `about-sync-log-clear-confirm-message`, `about-sync-log-count`, `about-telemetry-histogram-stats`, `about-webrtc-channels`, `about-webrtc-frames`, `about-webrtc-lost-label`, `about-webrtc-received-label`, `about-webrtc-sent-label` …and 75 more
- **typography — 42 strings** — 42 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `CookieAttributeIgnored`, `ImageMapCircleNegativeRadius`, `ImageMapCircleWrongNumberOfCoords`, `ImageMapPolyOddNumberOfCoords`, `ImageMapPolyWrongNumberOfCoords`, `ImageMapRectBoundsError`, `LenientThisWarning`, `MediaLoadSourceMissingSrc`, `MediaLoadUnsupportedMimeType`, `MediaLoadUnsupportedTypeAttribute`, `MimeNotCss`, `MimeNotCssWarn` …and 30 more

---

## 3. Open findings (220)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 152 |
| 2 | Wrong content (says something other than the English) | 68 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

- `about-logins-confirm-remove-all-dialog-confirm-button-label` — `browser/browser/aboutLogins.ftl` — For a single password the button says “Remove all”.
    - Current: `Odstrániť všetky`
    - Source: `{$count ->} [1] Remove [other] Remove All`
    - Suggest: `[1] Odstrániť`
    - en-US has [1] “Remove” vs [other] “Remove All”; the sk uses “Odstrániť všetky” in every variant, so a one-password dialog offers to remove all.
- `smart-window-model-personal` — `browser/browser/aiFeatures.ftl` — “Most tailored answers” rendered as “most accurate answers”.
    - Current: `Osobný: najpresnejšie odpovede`
    - Source: `description: Model { $model } by { $ownerName } label: Personal: Most tailored answers`
    - Suggest: `Osobný: najprispôsobenejšie odpovede`
    - “najpresnejšie” claims accuracy rather than personalization; the same en-US phrase is rendered “Najprispôsobenejšie odpovede” in aiWindow.ftl (aiwindow-firstrun-model-personal-body), so the surface is also inconsistent.
- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — “Open Smart Windows” (adjective) was read as a verb, so the sk says opening them causes the switch.
    - Current: `prepnete na klasické okná`
    - Source: `Synced data will remain in your account. Open { -smart-window-brand-name } will switch to Classic Windows.`
    - Suggest: `Otvorené { -smart-window-brand-name(plural-form: "true") } sa prepnú na klasické okná.`
    - en-US states that currently open Smart Windows will switch to Classic Windows; the sk tells the user that by opening Smart Windows they will switch to Classic Windows, which is a different behaviour.
- `sharing-warning-window` — `browser/browser/browser.ftl` — Warning claims others will see the content of every tab, not that they can see when you switch tabs.
    - Current: `uvidia obsah každej karty, ktorú otvoríte`
    - Source: `You are sharing { -brand-short-name }. Other people can see when you switch to a new tab.`
    - Suggest: `uvidia, keď prepnete na novú kartu`
    - en-US: “Other people can see when you switch to a new tab.” The same wording is also used in sharing-warning-screen; the sk asserts a broader disclosure than the source states.
- `contextual-manager-passwords-remove-all-confirm-button` — `browser/browser/contextual-manager.ftl` — For a single password the button says “Remove all”.
    - Current: `Odstrániť všetky`
    - Source: `{$total ->} [1] Remove [other] Remove all`
    - Suggest: `[1] Odstrániť`
    - en-US has [1] “Remove” vs [other] “Remove all”; the sk uses “Odstrániť všetky” in all variants.
- `ip-protection-bandwidth-left-mb-1` — `browser/browser/ipProtection.ftl` — The monthly quota unit was changed from GB to MB.
    - Current: `z { $maxUsage } MB`
    - Source: `<span data-l10n-name="usage">{ $usageLeft } MB</span> of { $maxUsage } GB left`
    - Suggest: `z { $maxUsage } GB`
    - The comment says $maxUsage is in GB and en-US reads “of { $maxUsage } GB left”; the sibling strings ip-protection-bandwidth-left-mb and -this-month-mb correctly use GB.
- `ip-protection-bandwidth-warning-infobar-message-90-mb` — `browser/browser/ipProtection.ftl` — The remaining-data amount is labelled GB although the variable is in MB.
    - Current: `<strong>Blížite sa k vášmu limitu pre dáta VPN.</strong> Zostáva vám { $usageLeft } GB.`
    - Source: `<strong>You’re almost out of VPN data.</strong> You have { $usageLeft } MB left. Once you use it all, your VPN will pause until your data resets on the first of next month.`
    - Suggest: `<strong>Takmer ste minuli dáta VPN.</strong> Zostáva vám { $usageLeft } MB.`
    - The developer comment states $usageLeft is in MB and en-US reads “You have { $usageLeft } MB left”; showing MB values as GB misstates how much data is left.
- `ipp-activator-breakage-turn-off-warning` — `browser/browser/ipProtection.ftl` — The “turn off” warning was translated as the “sign in” variant, adding an instruction the source does not give.
    - Current: `Skúste sa prihlásiť alebo vypnúť VPN počas používania tejto webovej stránky.`
    - Source: `<strong>This website may not work with a VPN.</strong> Try turning VPN off while you use this website.`
    - Suggest: `Skúste vypnúť VPN počas používania tejto webovej stránky.`
    - en-US for this id is only “Try turning VPN off while you use this website.”; the sign-in suggestion belongs to ipp-activator-breakage-sign-in-warning, so both sk strings are now identical.
- `cfr-doorhanger-doh-body` — `browser/browser/newtab/asrouter.ftl` — The hedge "whenever possible" is dropped, turning a conditional routing claim into an unconditional one.
    - Current: `teraz posiela vaše požiadavky DNS na partnerskú službu v záujme vašej ochrany zabezpečene`
    - Source: `Your privacy matters. { -brand-short-name } now securely routes your DNS requests whenever possible to a partner service to protect you while you browse.`
    - Suggest: `teraz vždy, keď je to možné, bezpečne posiela vaše požiadavky DNS partnerskej službe, aby vás chránil pri prehliadaní`
    - The en-US says requests are routed securely "whenever possible"; without that limit the sk asserts that all DNS requests always go to the partner service.
- `home-prefs-support-firefox-header-srd` — `browser/browser/newtab/newtab.ftl` — "Support Firefox" (a call to support the product) is rendered as "Support for Firefox", i.e. technical assistance.
    - Current: `Podpora pre { -brand-product-name(case: "acc") }`
    - Source: `label: Support { -brand-product-name }`
    - Suggest: `Podporiť { -brand-product-name }`
    - The section carries the sponsors/mission message, so "Support" is a verb; the matching newtab-promo-card-title in the same file correctly uses "Podporiť".
- `newtab-custom-close-menu-button` — `browser/browser/newtab/newtab.ftl` — The screen-reader label for "Close menu" reads as "the menu named Close".
    - Current: `Ponuka Zavrieť`
    - Source: `aria-label: Close menu title: Close`
    - Suggest: `Zavrieť ponuku`
    - In the en-US the .aria-label is the action "Close menu" (verb + object); the sk inverts it into a noun phrase naming a menu called "Close".
- `newtab-sports-widget-world-cup-champions` — `browser/browser/newtab/newtab.ftl` — "2026 World Cup Champions" is rendered as just the name of the tournament, dropping "Champions".
    - Current: `Majstrovstvá sveta vo futbale 2026`
    - Source: `2026 World Cup Champions`
    - Suggest: `Majstri sveta vo futbale 2026`
    - The string labels the winning team on a result card; the sk says only "2026 FIFA World Cup". The sibling short label is correctly "Šampióni 2026".
- `newtab-widget-lists-celebration-subhead` — `browser/browser/newtab/newtab.ftl` — "All clear" (a celebration that nothing is left to do) is rendered as the command "Clear everything".
    - Current: `Vymazať všetko`
    - Source: `All clear`
    - Suggest: `Všetko hotovo`
    - The string is a celebration subhead shown under "Dobrá práca" after the list is finished, not an action; "Vymazať všetko" reads as a button that deletes the list.
- `onboarding-focused-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — "tabs on the top" is translated as "bookmarks on the top".
    - Current: `Alebo to ponechajte klasické so záložkami navrchu.`
    - Source: `For a streamlined view that can help you stay focused, try your tabs on the side. Or keep it classic with tabs on the top. Switch anytime.`
    - Suggest: `Alebo to ponechajte klasické s kartami navrchu.`
    - Same defect as in onboarding-many-tabs-subtitle: the tab-layout choice is described with "záložky" (bookmarks) instead of "karty" (tabs).
- `onboarding-many-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — "tabs on the top" is translated as "bookmarks on the top".
    - Current: `Alebo to ponechajte klasické so záložkami navrchu.`
    - Source: `Keep a lot of tabs open? Try your tabs on the side for a more streamlined view. Or keep it classic with tabs on the top. Switch anytime.`
    - Suggest: `Alebo to ponechajte klasické s kartami navrchu.`
    - The screen chooses between tabs on the side and tabs on top; "záložky" means bookmarks. The adjacent label onboarding-new-horizontal-tabs-label correctly uses "Karty v hornej časti".
- `panic-button-delete-history` — `browser/browser/panicButton.ftl` — "Delete Recent History" drops "recent", claiming the browsing history is cleared.
    - Current: `vymažete <strong>históriu</strong> prehliadania`
    - Source: `Delete Recent <strong>History</strong>`
    - Suggest: `vymažete nedávnu <strong>históriu</strong> prehliadania`
    - The parallel item panic-button-delete-cookies keeps "nedávno vytvorené"; here the time-limited scope is dropped, so the line states the whole browsing history will be deleted.
- `fonts-langgroup-canadian` — `browser/browser/preferences/fonts.ftl` — “Unified Canadian Syllabary” rendered as a bare adjective with the noun dropped.
    - Current: `Jednotné kanadské`
    - Source: `label: Unified Canadian Syllabary`
    - Suggest: `Jednotné kanadské slabičné písmo`
    - Other entries in the list are self-standing script names; “Jednotné kanadské” leaves a dangling adjective and the user cannot tell what script is meant.
- `fonts-langgroup-other` — `browser/browser/preferences/fonts.ftl` — “Other Writing Systems” rendered as “Other font types”, naming the wrong thing in a list of scripts/languages.
    - Current: `Iné typy písma`
    - Source: `label: Other Writing Systems`
    - Suggest: `Iné systémy písma`
    - This entry is the last item of the language/script group list (Arabic, Armenian, … Tibetan, Unified Canadian Syllabary). “Iné typy písma” means “other font types”, which is a different category from a writing system, and conflicts with the purpose of the dropdown (choosing fonts *for* a script).
- `autofill-address-neighborhood` — `browser/browser/preferences/formAutofill.ftl` — “Neighborhood” as an administrative sublocality rendered as “Susedstvo”.
    - Current: `Susedstvo`
    - Source: `Neighborhood`
    - Suggest: `Štvrť`
    - The developer comment says this is a sublocality (civil entity below a locality) used in Iran and Mexico; Slovak “susedstvo” denotes neighbourliness/vicinity, not a named city district, which is “štvrť”.
- `more-from-moz-mozilla-monitor-card` — `browser/browser/preferences/moreFromMozilla.ftl` — “Find out where your personal info has been exposed online” becomes “find out whether your data was in a breach”.
    - Current: `zistite, či boli vaše osobné údaje súčasťou úniku údajov`
    - Source: `description: Find out where your personal info has been exposed online with a free scan. label: { -mozmonitor-brand-name }`
    - Suggest: `zistite, kde boli vaše osobné údaje zverejnené online`
    - The source promises to show *where* the data was exposed; the Slovak reduces it to a yes/no answer about a breach, describing a different service output.
- `more-from-moz-thunderbird-card` — `browser/browser/preferences/moreFromMozilla.ftl` — Card description adds a sentence about filtering and organizing that the source does not contain.
    - Current: `Filtrujte a usporiadajte ich tak, ako chcete.`
    - Source: `description: Access your email, calendars, and contacts in one fast app. label: { -thunderbird-brand-name }`
    - Suggest: `(odstrániť – zdroj uvádza len „Access your email, calendars, and contacts in one fast app.“)`
    - en-US description is a single sentence; the extra sentence asserts a product capability that the string does not claim.
- `home-prefs-highlights-option-most-recent-download` — `browser/browser/preferences/preferences.ftl` — Singular “Most recent download” rendered as a plural “Recent downloads”.
    - Current: `Nedávne sťahovania`
    - Source: `label: Most recent download`
    - Suggest: `Posledné stiahnutie`
    - The option shows only the single most recent download; the plural changes what the row claims to display.
- `home-prefs-recommended-by-option-sponsored-stories` — `browser/browser/preferences/preferences.ftl` — “Sponsored stories” translated as “Sponsored sites”, inconsistent with the Stories section it belongs to.
    - Current: `Sponzorované stránky`
    - Source: `label: Sponsored stories`
    - Suggest: `Sponzorované príbehy`
    - The adjacent strings render “stories” as “príbehy” (home-prefs-stories-header = Príbehy, home-prefs-recommended-by-header-generic = Odporúčané príbehy), and “Sponzorované stránky” duplicates the separate shortcuts option (home-prefs-shortcuts-by-option-sponsored = Sponzorované skratky) by naming sites instead of stories.
- `preferences-doh-overview-custom` — `browser/browser/preferences/preferences.ftl` — Custom DoH description asserts the DNS is not controlled by your provider instead of saying you control the provider and fallback.
    - Current: `Vždy sa použije zabezpečené DNS, ktoré nie je kontrolované vaším poskytovateľom.`
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior. label: Custom`
    - Suggest: `Vždy sa použije zabezpečené DNS s možnosťou zvoliť si poskytovateľa a záložné správanie.`
    - en-US: “Always use secure DNS with control over your provider and fallback behavior.” The Slovak drops the user-control point and instead makes a claim about who does not control the resolver, which is a different statement about how the mode behaves.
- `preferences-doh-radio-custom` — `browser/browser/preferences/preferences.ftl` — Same wrong description on the Custom DoH radio option.
    - Current: `Vždy sa použije zabezpečené DNS, ktoré nie je kontrolované vaším poskytovateľom`
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior label: Custom`
    - Suggest: `Vždy sa použije zabezpečené DNS s možnosťou zvoliť si poskytovateľa a záložné správanie`
    - en-US: “Always use secure DNS with control over your provider and fallback behavior”. The Slovak states the provider does not control the DNS, which is not what the source says and misdescribes the setting.
- `preferences-web-appearance-link` — `browser/browser/preferences/preferences.ftl` — Points users to the Add-ons Manager window instead of “Extensions & Themes”.
    - Current: `môžete spravovať v okne Správcu doplnkov`
    - Source: `label: Manage { -brand-short-name } themes in Extensions & Themes`
    - Suggest: `môžete spravovať v časti Rozšírenia a témy`
    - en-US says “Manage { -brand-short-name } themes in Extensions & Themes”, which is the name used elsewhere in this file (addons-button-label2 = Rozšírenia a témy vzhľadu); naming a different UI surface misdirects the user.
- `protection-report-page-summary` — `browser/browser/protections.ftl` — The hedged "can protect" is rendered as a flat assertion that Firefox is protecting the user, even though this string is shown only when all protections are off.
    - Current: `{ -brand-short-name } chráni vaše súkromie počas prehliadania.`
    - Source: `{ -brand-short-name } can protect your privacy behind the scenes while you browse. This is a personalized summary of those protections, including tools to take control of your online security.`
    - Suggest: `{ -brand-short-name } dokáže chrániť vaše súkromie počas prehliadania.`
    - The developer comment states explicitly: "This message shows when all privacy protections are turned off, which is why we use the word 'can'". The sk text is word-for-word identical to protection-report-page-summary-default, so the deliberate distinction between "can protect" (nothing on) and "protects" (actively protecting) is lost and the product claims protection it is not performing.
- `protections-panel-smartblock-desc-label` — `browser/browser/protectionsPanel.ftl` — "blocks tracking content" is rendered as "blocks the tracking of content".
    - Current: `blokuje sledovanie obsahu`
    - Source: `{ -brand-short-name } blocks tracking content while you’re on this site unless you allow it.`
    - Suggest: `blokuje sledovací obsah`
    - "sledovanie obsahu" reverses the head of the phrase (tracking of content) instead of naming the blocked object, tracking content, which the same file renders as "Sledovací obsah".
- `protections-blocking-cookies-trackers` — `browser/browser/siteProtections.ftl` — "Cross-Site Tracking Cookies Blocked" is rendered as "third-party trackers blocked", dropping "cookies".
    - Current: `Sledovacie prvky tretích strán boli zablokované`
    - Source: `title: Cross-Site Tracking Cookies Blocked`
    - Suggest: `Sledovacie cookies tretích strán boli zablokované`
    - This is the heading of the cookies sub-view; the same file renders the identical en term correctly as "Sledovacie cookies tretích strán" (content-blocking-cookies-blocking-trackers-label). As written it names trackers in general and is indistinguishable from the tracking-content category. The same loss affects protections-not-blocking-cross-site-tracking-cookies.
- `protections-blocking-tracking-content` — `browser/browser/siteProtections.ftl` — "Tracking Content Blocked" is rendered as "trackers blocked" rather than "tracking content".
    - Current: `Sledovacie prvky boli zablokované`
    - Source: `title: Tracking Content Blocked`
    - Suggest: `Sledovací obsah bol zablokovaný`
    - "Tracking Content" is consistently "Sledovací obsah" in this surface (protections-panel-content-blocking-tracking-protection, tracker-tab-title); rendering it as the generic "sledovacie prvky" collides with the other categories in the same panel. protections-not-blocking-tracking-content has the same problem.
- `tabbrowser-tab-label-tab-split-view-right` — `browser/browser/tabbrowser.ftl` — The noun phrase "Split view right" is rendered with the verb "Rozdeliť" (to split).
    - Current: `Rozdeliť zobrazenie vpravo`
    - Source: `{ $label }, Split view right`
    - Suggest: `Rozdelené zobrazenie vpravo`
    - This tooltip labels the right tab of a split view, exactly parallel to tabbrowser-tab-label-tab-split-view-left, which correctly reads "Rozdelené zobrazenie vľavo". As written it reads as a command to split the view.
- `webrtc-share-screen-warning` — `browser/browser/webrtcIndicator.ftl` — "browse as you" is rendered as "track your browsing", changing what a deceptive site is said to be able to do.
    - Current: `Zdieľanie môže umožniť klamlivým stránkam sledovať vaše prehliadanie a ukradnúť vaše osobné údaje.`
    - Source: `Only share screens with sites you trust. Sharing can allow deceptive sites to browse as you and steal your private data.`
    - Suggest: `Zdieľanie môže umožniť klamlivým stránkam prehliadať web vo vašom mene a ukradnúť vaše osobné údaje.`
    - "browse as you" means impersonating the user in their session, not observing their browsing; the sk understates the described risk. webrtc-share-browser-warning repeats the same clause.
- `newTabAlwaysContainer.tooltip` — `browser/chrome/browser/browser.properties` — "Select container to open a new tab" translated as "Opens a new container tab"
    - Current: `Otvorí novú kontajnerovú kartu`
    - Source: `Select container to open a new tab`
    - Suggest: `Vyberte kontajner, v ktorom sa otvorí nová karta`
    - The en-US instructs the user to pick a container; the sk states the button opens a container tab, dropping the selection step. It also duplicates the second line of newTabContainer.tooltip, losing the distinction between the two tooltips.
- `safebrowsing.reportedAttackSite` — `browser/chrome/browser/browser.properties` — "Reported Attack Site!" and "Reported Harmful Site!" both rendered identically
    - Current: `Nahlásená škodlivá stránka!`
    - Source: `Reported Attack Site!`
    - Suggest: `Nahlásená útočiaca stránka!`
    - safebrowsing.reportedAttackSite and safebrowsing.reportedHarmfulSite are two distinct en-US warnings but have exactly the same sk text, so the attack-site warning no longer says what the source says (cf. the same confusion in safebrowsing.notAnAttackButton.label).
- `unblockTypeMalware` — `browser/chrome/browser/downloads/downloads.properties` — "will harm your computer" weakened to "may harm your computer"
    - Current: `ktorý môže poškodiť váš počítač`
    - Source: `This file contains a virus or other malware that will harm your computer.`
    - Suggest: `ktorý poškodí váš počítač`
    - The en-US states the malware will harm the computer; the sk only says it may, which also erases the deliberate contrast with blockedPotentiallyUnwanted ("may harm your computer" / "môže poškodiť váš počítač").
- `malwareBlocked` — `browser/chrome/overrides/appstrings.properties` — "attack site" rendered as "deceptive site", making it identical to deceptiveBlocked
    - Current: `Stránka %S bola označená ako podvodná a na základe nastavení zabezpečenia bola zablokovaná.`
    - Source: `The site at %S has been reported as an attack site and has been blocked based on your security preferences.`
    - Suggest: `Stránka %S bola nahlásená ako útočiaca stránka a na základe nastavení zabezpečenia bola zablokovaná.`
    - en-US distinguishes "reported as an attack site" (malwareBlocked) from "reported as a deceptive site" (deceptiveBlocked); the sk text for both is word-for-word the same, so the malware/attack warning tells the user something different from what the source says.
- `unsafeContentType` — `browser/chrome/overrides/appstrings.properties` — "a file type that may not be safe to open" narrowed to "an archive file"
    - Current: `pretože sa nachádza v archívnom súbore, ktorého otvorenie nemusí byť bezpečné`
    - Source: `The page you are trying to view cannot be shown because it is contained in a file type that may not be safe to open. Please contact the website owners to inform them of this problem.`
    - Suggest: `pretože je obsiahnutá v type súboru, ktorého otvorenie nemusí byť bezpečné`
    - The en-US makes a general statement about an unsafe file type; the sk asserts specifically that the content is inside an archive, which is a different (and often untrue) fact about why the page was blocked.
- `accessibility-keyboard-issue-focusable` — `devtools/client/accessibility.ftl` — “Interactive elements must be focusable” narrowed to form elements.
    - Current: `Prvky formulára musia byť dosiahnuteľné klávesnicou.`
    - Source: `Interactive elements must be focusable. <a>Learn more</a>`
    - Suggest: `Interaktívne prvky musia byť dosiahnuteľné klávesnicou.`
    - The en-US says “Interactive elements”; the same string in devtools/shared/accessibility.properties is correctly “Interaktívne prvky”, so this one states a narrower, wrong rule.
- `accessibility-text-label-issue-figure` — `devtools/client/accessibility.ftl` — “Figures” (HTML <figure> elements) rendered as “Čísla” (numbers).
    - Current: `Čísla s voliteľnými titulkami by mali byť označené štítkom.`
    - Source: `Figures with optional captions should be labeled. <a>Learn more</a>`
    - Suggest: `Obrázky (figure) s voliteľnými popismi by mali byť označené štítkom.`
    - The en-US refers to <figure> elements; “Čísla” means numerals, so the accessibility check names the wrong thing entirely.
- `accessibility.role` — `devtools/client/accessibility.properties` — Accessibility “Role” column header rendered as “Postavenie” (status/standing).
    - Current: `Postavenie`
    - Source: `Role`
    - Suggest: `Rola`
    - The comment says the column represents the accessible element role (ARIA role); “Postavenie” means position/standing and does not convey the role concept.
- `timeline.scriptanimation.nameLabel` — `devtools/client/animationinspector.properties` — “Script Animation” rendered as “animation's script” (reversed head noun).
    - Current: `%S - skript animácie`
    - Source: `%S — Script Animation`
    - Suggest: `%S – skriptová animácia`
    - The label names an animation generated by a script; “skript animácie” names the script of an animation, labelling the wrong object in the timeline tooltip (same in timeline.scriptanimation.unnamedLabel).
- `boxmodel.offsetParent.title` — `devtools/client/boxmodel.properties` — “Offset parent of the selected element” rendered as “offset of the parent”.
    - Current: `Posunutie rodiča vybratého prvku`
    - Source: `Offset parent of the selected element`
    - Suggest: `Posunutý rodič (offsetParent) vybratého prvku`
    - The tooltip labels a DOM node that *is* the offset parent; the sk reads as the offset belonging to the parent, inverting what the previewed node is.
- `scopes.block` — `devtools/client/debugger.properties` — “Block” (a block of code) translated as the verb “to block”.
    - Current: `Blokovať`
    - Source: `Block`
    - Suggest: `Blok`
    - The developer comment says it refers to a block of code in the Scopes pane; “Blokovať” is the imperative verb “block (something)”, which reads as an action in a scope list.
- `labelDragTooltipText` — `devtools/client/filterwidget.properties` — Drag directions and increase/decrease pairing reversed.
    - Current: `Hodnotu zväčšíte/zmenšíte posúvaním doľava/doprava`
    - Source: `Drag left or right to decrease or increase the value`
    - Suggest: `Hodnotu zmenšíte/zväčšíte posúvaním doľava/doprava`
    - en-US: drag left to decrease, right to increase. The sk pairs left with increase and right with decrease, so the instruction tells the user the wrong direction.
- `colorpicker-tooltip-alpha-slider-title` — `devtools/client/inspector.ftl` — “Opacity” rendered as “Priehľadnosť” (transparency), the inverse quantity.
    - Current: `Priehľadnosť`
    - Source: `Opacity`
    - Suggest: `Nepriehľadnosť`
    - The alpha slider shows opacity; transparency is its inverse, so the slider's higher values are described backwards.
- `inspector-emulation-panel-reduced-motion-no-preference` — `devtools/client/inspector.ftl` — Added negation: “Enable no preference …” became “Do not enable …”.
    - Current: `Nepovoliť žiadnu preferenciu pre emuláciu redukovaného pohybu`
    - Source: `(value): No preference aria-label: Enable no preference for reduced motion emulation`
    - Suggest: `Povoliť emuláciu možnosti „žiadna preferencia“ pre redukovaný pohyb`
    - This aria-label is for the radio button that enables the “no preference” emulation value; the sk says the option does not enable anything, reversing what the control does.
- `inspector.breadcrumbs.label` — `devtools/client/inspector.properties` — “Breadcrumbs” rendered as “consistent navigation”.
    - Current: `Konzistentná navigácia`
    - Source: `Breadcrumbs`
    - Suggest: `Navigačná cesta (drobčeková navigácia)`
    - This aria-label names the breadcrumb trail container; “Konzistentná navigácia” means “consistent navigation” and does not identify the widget for screen-reader users.
- `charts.cacheDisabled` — `devtools/client/netmonitor.properties` — “Empty cache” rendered as “saved to cache”.
    - Current: `Uložené do vyrovnávacej pamäte`
    - Source: `Empty cache`
    - Suggest: `Prázdna vyrovnávacia pamäť`
    - In the performance-analysis chart this label marks the empty-cache case; rendering it as “stored to cache” makes both chart labels claim caching and mislabels the measurement.
- `netmonitor.search.toolbar.inputPlaceholder` — `devtools/client/netmonitor.properties` — “Find in resources…” rendered as “search in addresses”.
    - Current: `Hľadať v adresách…`
    - Source: `Find in resources…`
    - Suggest: `Hľadať v zdrojoch…`
    - The search panel searches request/response resource contents, not URLs; the placeholder tells the user it only matches addresses.
- `storage-table-empty-text` — `devtools/client/storage.ftl` — “for selected host” rendered as “for the current page”.
    - Current: `Pre aktuálnu stránku nie sú dostupné žiadne údaje`
    - Source: `No data present for selected host`
    - Suggest: `Pre vybraný server nie sú dostupné žiadne údaje`
    - The hint concerns the host selected in the storage tree (rendered as “server” in the neighbouring hints), not the current page.
- `accessibility.text.label.issue.figure` — `devtools/shared/accessibility.properties` — “Figures” rendered as “Čísla” (numbers) in the shared audit string too.
    - Current: `Čísla s voliteľnými titulkami by mali byť označené štítkom.`
    - Source: `Figures with optional captions should be labeled.`
    - Suggest: `Obrázky (figure) s voliteľnými popismi by mali byť označené štítkom.`
    - Same defect as in accessibility.ftl: a <figure> element is not a number, so the audit message points at the wrong element type.
- `whypaused-assert` — `devtools/shared/debugger-paused-reasons.ftl` — “Paused on assertion” rendered as “paused on an expression”.
    - Current: `Pozastavené na výraze`
    - Source: `Paused on assertion`
    - Suggest: `Pozastavené na aserciu`
    - An assertion is a specific pause reason; “výraz” (expression) names a different, much broader construct, and “expression” is used elsewhere in the debugger strings for watch expressions.
- `heading` — `dom/chrome/accessibility/mac/accessible.properties` — The ARIA "heading" role is spoken as "hlavička" (header/head area).
    - Current: `heading = hlavička`
    - Source: `heading`
    - Suggest: `heading = nadpis`
    - The comment identifies this as the spoken role description for the WAI-ARIA heading role; "hlavička" means a header/head section (used for <head> in htmlparser.properties), while AccessFu.properties correctly uses "nadpis" for heading. Screen-reader users hear the wrong role.
- `malwareBlocked` — `dom/chrome/appstrings.properties` — "attack site" rendered as "deceptive site", duplicating deceptiveBlocked.
    - Current: `Stránka %S bola označená ako podvodná a na základe nastavení zabezpečenia bola zablokovaná.`
    - Source: `The site at %S has been reported as an attack site and has been blocked based on your security preferences.`
    - Suggest: `Stránka %S bola nahlásená ako útočiaca stránka a na základe nastavení zabezpečenia bola zablokovaná.`
    - en-US distinguishes "an attack site" (malwareBlocked) from "a deceptive site" (deceptiveBlocked); the sk uses "podvodná" for both, so the two different blocking reasons become indistinguishable and malware is reported as fraud.
- `FullscreenExitWindowFocus` — `dom/chrome/dom/dom.properties` — Causality reversed: "preto" (therefore) used instead of "pretože" (because).
    - Current: `Režim Na celú obrazovku bol ukončený, preto v popredí je práve okno.`
    - Source: `Exited fullscreen because a window was focused.`
    - Suggest: `Režim Na celú obrazovku bol ukončený, pretože okno získalo zameranie.`
    - en-US: "Exited fullscreen because a window was focused." The sk reverses cause and effect, claiming the window is in the foreground as a result of leaving fullscreen.
- `ManifestStartURLOutsideScope` — `dom/chrome/dom/dom.properties` — Says the start URL is invalid, where en-US says the scope is invalid.
    - Current: `Začiatok URL adresy je mimo rozsah, a tým je neplatný.`
    - Source: `The start URL is outside the scope, so the scope is invalid.`
    - Suggest: `Úvodná adresa URL je mimo rozsahu, takže rozsah je neplatný.`
    - en-US: "The start URL is outside the scope, so the scope is invalid." The sk attributes the invalidity to the start URL instead of the scope, and renders "start URL" (the start_url member) as "the beginning of the URL".
- `WebExtensionUncheckedLastError` — `dom/chrome/dom/dom.properties` — "was not checked" rendered as "was not ticked (checkbox)".
    - Current: `Hodnota browser.runtime.lastError nebola začiarknutá: %S`
    - Source: `browser.runtime.lastError value was not checked: %S`
    - Suggest: `Hodnota browser.runtime.lastError nebola skontrolovaná: %S`
    - "začiarknuť" means to tick a checkbox; here the en-US means the value was not examined by the code.
- `PESelectorGroupExtraCombinator` — `dom/chrome/layout/css.properties` — CSS "combinator" rendered as "hyphen".
    - Current: `Nesprávne umiestnený spojovník.`
    - Source: `Dangling combinator.`
    - Suggest: `Nesprávne umiestnený kombinátor.`
    - "spojovník" means hyphen; the en-US "Dangling combinator" refers to a CSS selector combinator (>, +, ~), so the message points the author at the wrong construct.
- `errNotSemicolonTerminated` — `dom/chrome/layout/htmlparser.properties` — "semicolon" translated as "colon".
    - Current: `Menná referencia znaku nebola ukončená dvojbodkou`
    - Source: `Named character reference was not terminated by a semicolon. (Or “&” should have been escaped as “&amp;”.)`
    - Suggest: `Menná referencia znaku nebola ukončená bodkočiarkou`
    - "dvojbodka" is a colon; the en-US says semicolon, and the sibling string errCharRefLacksSemicolon correctly uses "bodkočiarkou". The message tells the author to add the wrong character.
- `couldNotParseReportURI` — `dom/chrome/security/csp.properties` — Says the report could not be processed, not the report URI parsed.
    - Current: `Nebolo možné spracovať správu: %1$S`
    - Source: `couldn’t parse report URI: %1$S`
    - Suggest: `Nebolo možné spracovať adresu URI správy: %1$S`
    - The placeholder is the report URI (see the developer comment); the sk drops "URI" so the message blames the report itself.
- _…and 41 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `migration-no-permissions-instructions-step2-2` — `browser/browser/migrationWizard.ftl` — The macOS variant tells the user to choose “Vybrať” (Select) when the source says “Open”.
    - Current: `V dialógovom okne na výber súborov zvoľte “Vybrať”`
    - Source: `{$sel_1 ->} [macos] In the file picker, choose “Open” [other] In the file picker, navigate to <code>{ $permissionsPath }</code> and choose “Select”`
    - Suggest: `V dialógovom okne na výber súborov zvoľte “Otvoriť”`
    - On macOS the en-US says to choose “Open”. Only the other variant says “Select”. With the wrong button name, the instruction points to a label that doesn't match the macOS picker.
- `newtab-clock-city-br-brasilia` — `browser/browser/newtab/newtab.ftl` — The Brazilian capital Brasília is rendered with the Slovak name of the country Brazil.
    - Current: `Brazília`
    - Source: `Brasília`
    - Suggest: `Brasília`
    - Slovak distinguishes the country (Brazília) from the capital city (Brasília). In a list of world-clock cities this names a country instead of the city the clock is for.
- `newtab-clock-city-ec-guayaquil` — `browser/browser/newtab/newtab.ftl` — Guayaquil is given its full ceremonial name, which clashes with the neighbouring "Santiago" (Chile) entry.
    - Current: `Santiago de Guayaquil`
    - Source: `Guayaquil`
    - Suggest: `Guayaquil`
    - The comment asks for the locale's usual spelling of the city; the usual Slovak name is simply "Guayaquil", and the added "Santiago de" duplicates the Chilean capital listed nearby.

### C. Grammar, agreement & spelling

- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — Plural variants use the singular verb “odstráni” with a plural noun.
    - Current: `Týmto sa odstráni heslá uložené vo`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices. This will also remove any breach alerts that appear here. You cannot undo this action. [other] This will remove al…`
    - Suggest: `Týmto sa odstránia heslá uložené vo { -brand-short-name(case: "loc") }…`
    - In the [few]/[many]/[other] variants the verb stayed singular (“sa odstráni”) while the noun is plural (“heslá”); the non-sync sibling message correctly uses “sa odstránia”.
- `restart-required-single-instance-answer-2` — `browser/browser/aboutRestartRequired.ftl` — “bezpečený” is not a Slovak word.
    - Current: `bezpečený`
    - Source: `This can happen during a long browsing session, or when your operating system updates { -brand-short-name }. Restarting keeps { -brand-short-name } secure and working normally.`
    - Suggest: `zabezpečený`
    - en-US “Restarting keeps { -brand-short-name } secure”; the correct form is “zabezpečený” (or “bezpečný”).
- `addon-confirm-install-unsigned-message` — `browser/browser/addonNotifications.ftl` — The [one] variant uses the indicative “Pokračujete” instead of the imperative.
    - Current: `Pokračujete na vlastné riziko.`
    - Source: `{$addonCount ->} [1] Caution: This site would like to install an unverified add-on in { -brand-short-name }. Proceed at your own risk. [other] Caution: This site would like to install { $addonCount } unverified add-ons…`
    - Suggest: `Pokračujte na vlastné riziko.`
    - en-US “Proceed at your own risk.” is an imperative, and the other variants of this message (and addon-confirm-install-some-unsigned-message, which has the same slip in [one]) use “Pokračujte”.
- `aiwindow-firstrun-default-title` — `browser/browser/aiWindow.ftl` — Wrong case form “svojim” instead of instrumental “svojím”.
    - Current: `svojim obľúbeným nástrojom`
    - Source: `Make { -smart-window-brand-name } your go-to`
    - Suggest: `svojím obľúbeným nástrojom`
    - The instrumental singular of “svoj” is “svojím”; “svojim” is the dative plural.
- `smart-window-ungroup-success-summary` — `browser/browser/aiWindowContent.ftl` — The [one] variant uses the plural/genitive “karty” with singular participles.
    - Current: `{ $count } karty zoskupená a potom oddelená zo skupiny.`
    - Source: `{$count ->} [one] { $count } tab grouped, then ungrouped. [other] { $count } tabs grouped, then ungrouped.`
    - Suggest: `{ $count } karta zoskupená a potom oddelená zo skupiny.`
    - For count 1 the noun must be nominative singular “karta” to agree with “zoskupená… oddelená”.
- `smartwindow-nl-thinking` — `browser/browser/aiWindowContent.ftl` — Missing reflexive “sa” makes the status read “They search matching tabs”.
    - Current: `Hľadajú zodpovedajúce karty…`
    - Source: `Looking for matching tabs…`
    - Suggest: `Hľadajú sa zodpovedajúce karty…`
    - en-US “Looking for matching tabs…” is impersonal; without “sa” the sk sentence has an unexpressed third-person plural subject.
- `other-backup-files-founds` — `browser/browser/backupSettings.ftl` — The singular variant is grammatically broken (plural verb/noun with singular modifier).
    - Current: `boli nájdený { $numberOfOtherBackupsFound } ďalší súbory zálohy`
    - Source: `{$numberOfOtherBackupsFound ->} [one] <b>Note:</b> { $numberOfOtherBackupsFound } other backup file found [other] <b>Note:</b> { $numberOfOtherBackupsFound } other backup files found`
    - Suggest: `bol nájdený { $numberOfOtherBackupsFound } ďalší súbor zálohy`
    - en-US [one] is “{ $n } other backup file found”; the sk [one] mixes “boli nájdený” (plural aux + singular participle) with the plural noun “súbory”.
- `urlbar-microphone-blocked` — `browser/browser/browser.ftl` — Typo “v vášmu” instead of “k vášmu”.
    - Current: `prístup v vášmu mikrofónu`
    - Source: `tooltiptext: You have blocked your microphone for this website.`
    - Suggest: `prístup k vášmu mikrofónu`
    - The parallel strings (camera, canvas, MIDI) all read “prístup k…”; “v vášmu” is not a valid preposition/case pairing.
- `customkeys-conflict-unusable-body` — `browser/browser/customkeys.ftl` — Sentence has no subject and uses “kľúč” (key as in lock/crypto) instead of “kláves”.
    - Current: `Tento kľúč už používa pre akciu`
    - Source: `This key is already used by “{ $conflict }” and cannot be used.`
    - Suggest: `Tento kláves už používa skratka pre „{ $conflict }“ a nemožno ho použiť.`
    - en-US: “This key is already used by “{ $conflict }” and cannot be used.” The sk reads “This key already uses for the action…”, and the rest of the file consistently calls a keyboard key “kláves”.
- `genai-chatbot-summarize-footer-generic-subtitle` — `browser/browser/genai.ftl` — Missing conjunction between two adverbs.
    - Current: `rýchlo jednoducho vytvárať súhrny stránok`
    - Source: `Add an AI chatbot to the { -brand-short-name } sidebar to quickly summarize pages.`
    - Suggest: `rýchlo a jednoducho vytvárať súhrny stránok`
    - Two coordinated adverbs need “a”; as written the phrase is ungrammatical.
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Third list item is in the nominative instead of the instrumental required by “súhlas so”.
    - Current: `a <a data-l10n-name="link3">Upozornenie o ochrane osobných údajov v aplikáciách Gemini</a>`
    - Source: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
    - Suggest: `a <a data-l10n-name="link3">Upozornením o ochrane osobných údajov v aplikáciách Gemini</a>`
    - The sentence “vyjadrujete súhlas so Zmluvnými podmienkami…, Pravidlami… a Upozornenie…” requires “Upozornením”, as the two preceding items show.
- `ip-protection-bandwidth-warning-infobar-message-90` — `browser/browser/ipProtection.ftl` — “minulé” (past) is written where “minuté” (used up) is meant, making the sentence nonsense.
    - Current: `Takmer máte minulé dáta VPN.`
    - Source: `<strong>You’re almost out of VPN data.</strong> You have { $usageLeft } GB left. Once you use it all, your VPN will pause until your data resets on the first of next month.`
    - Suggest: `Takmer ste minuli dáta VPN.`
    - en-US is “You’re almost out of VPN data.”; “máte minulé dáta” literally reads “you have past data” and does not convey running out.
- `ipprotection-location-selection-callout-description-1` — `browser/browser/ipProtection.ftl` — Duplicated pronoun “vám … pre vás”.
    - Current: `Alebo vám vyberieme pre vás tú najrýchlejšiu.`
    - Source: `<a data-l10n-name="learn-more-vpn">{ -brand-product-name }’s built-in VPN</a> lets you choose from several browsing locations, or let us pick the fastest one for you.`
    - Suggest: `Alebo vám vyberieme tú najrýchlejšiu.`
    - en-US “or let us pick the fastest one for you” has one beneficiary; the sk repeats it twice, which is ungrammatical.
- `ipprotection-summer-promo-offramp-generic-description` — `browser/browser/ipProtection.ftl` — Wrong case “pri prehliadanie” and misplaced pronoun.
    - Current: `aby bolo pri prehliadanie webu vás ťažšie vysledovať`
    - Source: `Use your { $maxUsage } GB and 6 locations for extra privacy to make your browsing harder to trace back to you.`
    - Suggest: `aby vás bolo pri prehliadaní webu ťažšie vysledovať`
    - “pri” requires the locative “prehliadaní”; the same broken phrase also appears in ipprotection-summer-promo-offramp-generic-description-default-browser-users-no-upgrade.
- `sidebar-button.tooltiptext2` — `browser/chrome/browser/customizableui/customizableWidgets.properties` — Missing accent: "bočne" instead of the adjective "bočné"
    - Current: `Zobrazí bočne panely`
    - Source: `Show sidebars`
    - Suggest: `Zobrazí bočné panely`
    - "bočne" is the adverb; the plural accusative adjective agreeing with "panely" is "bočné" (as in sidebar-button.label "Bočné panely").
- `permission.speaker.label` — `browser/chrome/browser/sitePermissions.properties` — Permission label rendered as an imperative verb instead of a noun phrase
    - Current: `Vyberte reproduktory`
    - Source: `Select speakers`
    - Suggest: `Výber reproduktorov`
    - Every other permission label in this file is a verbal noun ("Použitie kamery", "Prístup k sériovým portom"); the imperative "Vyberte" addresses the user and reads as a command rather than as the name of a permission.
- `basicHttpAuthDisabled` — `browser/chrome/overrides/appstrings.properties` — Case mismatch in the coordinated list: nominative items followed by an accusative one
    - Current: `ako je vaše používateľské meno, heslo alebo e‑mailovú adresu`
    - Source: `Someone pretending to be the site could try to steal things like your username, password, or email.`
    - Suggest: `ako je vaše používateľské meno, heslo alebo e‑mailová adresa`
    - The list after "ako je" is nominative ("meno, heslo"), so "e‑mailovú adresu" in the accusative does not agree with the other coordinated members.
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — CSS property name font-size translated despite the do-not-translate comment.
    - Current: `Skúste zmeniť <strong>veľkosť písma</strong> textu prvku ruby.`
    - Source: `Try changing the <strong>font-size</strong> of the ruby text. { learn-more }`
    - Suggest: `Skúste zmeniť <strong>font-size</strong> textu prvku ruby.`
    - The section comment states CSS properties and values inside <strong> must not be translated; the same applies to inactive-css-ruby-element-fix-1, which has the identical issue.
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — Argument identifier URL_STRING written as URLSTRING in the usage text.
    - Current: `Prijíma iba jeden parameter URLSTRING`
    - Source: `:block URL_STRING  Start blocking network requests    It accepts only one URL_STRING argument, an unquoted string which will be used to block all requests whose URL includes this string.   Use :unblock or the Network Mo…`
    - Suggest: `Prijíma iba jeden parameter URL_STRING`
    - The usage line above it and the command itself use the identifier URL_STRING; dropping the underscore misnames the argument in help output.
- `EditorFileDropFailed` — `dom/chrome/dom/dom.properties` — Verb does not agree with the masculine subject "Prenos".
    - Current: `Prenos súboru do prvku s upraviteľným obsahom zlyhalo`
    - Source: `Dropping a file into a contenteditable element failed: %S.`
    - Suggest: `Prenos súboru do prvku s upraviteľným obsahom zlyhal`
    - "Prenos" is masculine, so the past tense must be "zlyhal", not the neuter "zlyhalo".
- `FullscreenDeniedMouseEventOnlyLeftBtn` — `dom/chrome/dom/dom.properties` — Verb and participle do not agree with the feminine subject "metóda".
    - Current: `metóda Element.requestFullscreen() bol volaný z vnútra obslužnej rutiny`
    - Source: `Request for fullscreen was denied because Element.requestFullscreen() was called from inside a mouse event handler not triggered by left mouse button.`
    - Suggest: `metóda Element.requestFullscreen() bola volaná z vnútra obslužnej rutiny`
    - "metóda" is feminine; "bol volaný" is masculine agreement.
- `MediaLoadExhaustedCandidates` — `dom/chrome/dom/dom.properties` — Wrong case after the verbal noun "Načítavanie".
    - Current: `Načítavanie médiá bolo pozastavené.`
    - Source: `All candidate resources failed to load. Media load paused.`
    - Suggest: `Načítavanie média bolo pozastavené.`
    - "Načítavanie" requires the genitive ("média"/"médií"); "médiá" is nominative/accusative plural.
- `PEPseudoClassArgNotIdent` — `dom/chrome/layout/css.properties` — The word "parameter" is duplicated.
    - Current: `Očakávaný identifikátor pre parameter pseudotriedy parameter, ale bol nájdený '%1$S'.`
    - Source: `Expected identifier for pseudo-class parameter but found ‘%1$S’.`
    - Suggest: `Očakávaný identifikátor pre parameter pseudotriedy, ale bol nájdený '%1$S'.`
    - Leftover duplicate word in the sentence.
- `errNestedComment` — `dom/chrome/layout/htmlparser.properties` — Number agreement between noun and relative clause.
    - Current: `Pravdepodobne ide o vnorený komentár, ktoré nie sú povolené.`
    - Source: `Saw “<!--” within a comment. Probable cause: Nested comment (not allowed).`
    - Suggest: `Pravdepodobne ide o vnorený komentár, ktorý nie je povolený.`
    - Singular "komentár" followed by plural "ktoré nie sú" is ungrammatical.
- `errUnquotedAttributeLt` — `dom/chrome/layout/htmlparser.properties` — Wrong participle form "uzatvárací" instead of "uzatvárajúci".
    - Current: `Pravdepodobne chýba znak “>” uzatvárací túto značku.`
    - Source: `“<” in an unquoted attribute value. Probable cause: Missing “>” immediately before.`
    - Suggest: `Pravdepodobne chýba znak “>” uzatvárajúci túto značku.`
    - The adjective "uzatvárací" cannot take the accusative object "túto značku"; the active participle "uzatvárajúci" is required. The same error appears in errUnquotedAttributeStartLt.
- `CompositorAnimationWarningHasCurrentColor` — `dom/chrome/layout/layout_errors.properties` — The main verb is missing, leaving the sentence incomplete.
    - Current: `Animáciu vlastnosti ‘background-color’ nie je možné v kompozitore s aktuálne nastaveným kľúčovým rámcom ‘current-color’.`
    - Source: `Animations of ‘background-color’ cannot be run on the compositor with ‘current-color’ keyframe.`
    - Suggest: `Animáciu vlastnosti ‘background-color’ nie je možné spustiť v kompozitore s kľúčovým rámcom ‘current-color’.`
    - "nie je možné" has no infinitive; the sibling strings all end with "spustiť".
- `ignoreSrcForDirective` — `dom/chrome/security/csp.properties` — Misspelling "Ingoruje".
    - Current: `Ingoruje sa src pre direktívu '%1$S'`
    - Source: `Ignoring srcs for directive ‘%1$S’`
    - Suggest: `Ignoruje sa src pre direktívu '%1$S'`
    - Typo: letters transposed in "Ignoruje".
- `ignoringReportOnlyDirective` — `dom/chrome/security/csp.properties` — Misspelling "sandobxu".
    - Current: `Ignorovanie direktívy sandobxu`
    - Source: `Ignoring sandbox directive when delivered in a report-only policy ‘%1$S’`
    - Suggest: `Ignorovanie direktívy sandboxu`
    - Typo in "sandboxu".
- `invalidRequireTrustedTypesForDirectiveValue` — `dom/chrome/security/csp.properties` — Truncated word "očaká sa".
    - Current: `očaká sa ‘script‘`
    - Source: `Received an invalid token for the ‘require-trusted-types-for‘ directive: %1$S; expected ‘script‘`
    - Suggest: `očakáva sa ‘script‘`
    - "očaká sa" is not a word; the verb is "očakáva sa".
- `BlockTopLevelDataURINavigation` — `dom/chrome/security/security.properties` — Misspelling "zablokovavné".
    - Current: `bolo zablokovavné`
    - Source: `Navigation to toplevel data: URI not allowed (Blocked loading of: “%1$S”)`
    - Suggest: `bolo zablokované`
    - Typo: extra syllable in "zablokované".
- `CORSAllowHeaderFromPreflightDeprecation` — `dom/chrome/security/security.properties` — Wrong case in the opening phrase.
    - Current: `Upozornenie požiadavku cross-origin:`
    - Source: ``Cross-Origin Request Warning: The Same Origin Policy will disallow reading the remote resource at %1$S soon. (Reason: When the `Access-Control-Allow-Headers` is `*`, the `Authorization` header is not covered. To include…``
    - Suggest: `Upozornenie na požiadavku cross-origin:`
    - "Upozornenie" requires "na" plus accusative; as written the two nouns do not combine grammatically.
- `STSCouldNotSaveState` — `dom/chrome/security/security.properties` — Participle does not agree and the clause is ungrammatical.
    - Current: `vyskytla sa chyba označujúce stránku ako hostiteľa`
    - Source: `Strict-Transport-Security: An error occurred noting the site as a Strict-Transport-Security host.`
    - Suggest: `vyskytla sa chyba pri označovaní stránky ako hostiteľa`
    - "chyba" (feminine) cannot be modified by the neuter "označujúce"; en-US is "An error occurred noting the site as a … host".
- `xslt-aborted` — `dom/dom/xslt.ftl` — Acronym XSLT misspelled as XSTL.
    - Current: `<xsl:message> ukončil transformáciu XSTL.`
    - Source: `XSLT transformation was terminated by <xsl:message>.`
    - Suggest: `<xsl:message> ukončil transformáciu XSLT.`
    - Transposed letters in the technology name XSLT.
- `xslt-bad-recursion` — `dom/dom/xslt.ftl` — Acronym XSLT misspelled as XSTL.
    - Current: `Šablóna so štýlmi XSTL (pravdepodobne) obsahuje rekurziu.`
    - Source: `XSLT Stylesheet (possibly) contains a recursion.`
    - Suggest: `Šablóna so štýlmi XSLT (pravdepodobne) obsahuje rekurziu.`
    - XSLT is a technology name and must be spelled correctly; the letters are transposed.
- `xslt-bad-value` — `dom/dom/xslt.ftl` — Acronym XSLT misspelled as XSTL.
    - Current: `Hodnota atribútu je v XSTL 1.0 nepovolená.`
    - Source: `Attribute value illegal in XSLT 1.0.`
    - Suggest: `Hodnota atribútu je v XSLT 1.0 nepovolená.`
    - Transposed letters in the technology name XSLT.
- `CookieRejectedHttpOnlyButFromScript` — `netwerk/necko.properties` — Missing space before the quoted cookie name.
    - Current: `Súbor cookie“%1$S” bol odmietnutý`
    - Source: `Cookie “%1$S” has been rejected because there is already an HTTP-Only cookie but script tried to store a new one.`
    - Suggest: `Súbor cookie “%1$S” bol odmietnutý`
    - The space between "cookie" and the opening quote is missing, so the rendered message runs the words together. Every sibling string in the file has the space.
- `SEC_ERROR_OCSP_OLD_RESPONSE` — `security/manager/chrome/pipnss/nsserrors.properties` — Relative pronoun does not agree with its antecedent.
    - Current: `Odozva OCSP obsahuje údaj, ktoré platnosť už uplynula.`
    - Source: `The OCSP response contains out-of-date information.`
    - Suggest: `Odozva OCSP obsahuje údaje, ktorých platnosť už uplynula.`
    - "údaj" (singular) with "ktoré" (plural nominative) is ungrammatical; the possessive genitive "ktorého/ktorých" is required.
- `SSL_ERROR_FEATURE_NOT_SUPPORTED_FOR_VERSION` — `security/manager/chrome/pipnss/nsserrors.properties` — Missing copula "je".
    - Current: `Funkcia SSL nie podporovaná pre danú verziu protokolu.`
    - Source: `SSL feature not supported for the protocol version.`
    - Suggest: `Funkcia SSL nie je podporovaná pre danú verziu protokolu.`
    - Ungrammatical: the verb "je" is missing.
- `delete-ca-cert-confirm` — `security/manager/security/certificates/certManager.ftl` — Stray preposition and wrong case: "zrušiť od dôveryhodnosť".
    - Current: `Naozaj chcete certifikáty odstrániť resp. zrušiť od dôveryhodnosť?`
    - Source: `You have requested to delete these CA certificates. For built-in certificates all trust will be removed, which has the same effect. Are you sure you want to delete or distrust?`
    - Suggest: `Naozaj chcete certifikáty odstrániť, resp. zrušiť ich dôveryhodnosť?`
    - "od" does not belong there and "dôveryhodnosť" does not agree with it; the question is ungrammatical in a confirmation dialog.
- `pkcs12-info-no-smartcard-backup` — `security/manager/security/certificates/certManager.ftl` — Wrong preposition "s" instead of "z".
    - Current: `zálohovať certifikáty s hardvérového bezpečnostného zariadenia`
    - Source: `It is not possible to back up certificates from a hardware security device such as a smart card.`
    - Suggest: `zálohovať certifikáty z hardvérového bezpečnostného zariadenia`
    - Backing up "from" a device requires "z"; "s" plus genitive is incorrect here.
- `glean-debug-ping-viewer-brand-name` — `toolkit/toolkit/about/aboutGlean.ftl` — The Glean Debug Ping Viewer product name is translated.
    - Current: `Zobrazovač pingu ladenia v nástroji { -glean-brand-name }`
    - Source: `{ -glean-brand-name } Debug Ping Viewer`
    - Suggest: `{ -glean-brand-name } Debug Ping Viewer`
    - The message id marks it as a brand name and it names an external Mozilla tool (the GDPV web app); translating it means the page links users to a product under a name it is not published under.
- `about-service-workers-title` — `toolkit/toolkit/about/aboutServiceWorkers.ftl` — “Service Workers” is translated although the file comment forbids it.
    - Current: `Čo je skript typu worker`
    - Source: `About Service Workers`
    - Suggest: `Čo je Service Workers`
    - The file-level comment states: “The term 'Service Workers' and 'Workers' should not be translated”. The sk renders it as “skript typu worker” here and in about-service-workers-main-title, -warning-not-enabled, -warning-no-service-workers and unregister-error, dropping “Service” entirely.
- `experimental-features-newtab-widget-lists-and-timer-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — Person/number disagreement in the final clause.
    - Current: `aby ste si pripomenul dobitie batérií`
    - Source: `Keep your to-do list top-of-mind when you open a new tab. From packing lists to shopping lists, make your plans in { -brand-product-name }. Set a timer to keep you focused, nudge you to stay on track, or remind you to r…`
    - Suggest: `aby ste si pripomenuli, že si treba dobiť batérie`
    - “aby ste … pripomenul” mixes the 2nd person plural with a masculine singular participle; the rest of the string uses the plural polite form.
- `fp-certerror-self-signed-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — Feminine participle refers to the masculine noun “certifikát”.
    - Current: `Nebola vydaná uznávanou certifikačnou autoritou`
    - Source: `Because there’s an issue with the site’s certificate. Sites use certificates issued by a certificate authority to prove they’re really who they say they are. This site’s certificate is self-signed. It wasn’t issued by a…`
    - Suggest: `Nebol vydaný uznávanou certifikačnou autoritou`
    - The subject is “Certifikát tejto stránky” in the preceding sentence, which is masculine; “Nebola vydaná” does not agree with it.
- `sec-error-ocsp-old-response` — `toolkit/toolkit/neterror/nsserrors.ftl` — Agreement error between noun and relative pronoun.
    - Current: `Odozva OCSP obsahuje údaj, ktoré platnosť už uplynula.`
    - Source: `The OCSP response contains out-of-date information.`
    - Suggest: `Odozva OCSP obsahuje údaje, ktorých platnosť už uplynula.`
    - “údaj, ktoré platnosť” mismatches number and case; the sentence does not parse in Slovak.
- `ssl-error-feature-not-supported-for-version` — `toolkit/toolkit/neterror/nsserrors.ftl` — Missing copula “je”.
    - Current: `Funkcia SSL nie podporovaná pre danú verziu protokolu.`
    - Source: `SSL feature not supported for the protocol version.`
    - Suggest: `Funkcia SSL nie je podporovaná pre danú verziu protokolu.`
    - “nie podporovaná” is ungrammatical; the parallel strings in the same file use “nie je podporovaná”.
- `ssl-error-unknown-ca-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — Negation dropped from the second verb, so the sentence says the peer trusts the CA.
    - Current: `Partner nerozpoznáva a dôveruje CA, ktorý vydal váš certifikát.`
    - Source: `Peer does not recognize and trust the CA that issued your certificate.`
    - Suggest: `Partner nerozpoznáva a nedôveruje certifikačnej autorite, ktorá vydala váš certifikát.`
    - en-US: “Peer does not recognize and trust the CA…”. Slovak requires the negative on both verbs; as written it reads “does not recognize and trusts”.
- `backgroundupdate-task-description` — `toolkit/toolkit/updates/backgroundupdate.ftl` — Missing preposition “v” before “čase”.
    - Current: `aj čase, keď`
    - Source: `The Background Update task checks for updates to { -brand-short-name } when { -brand-short-name } is not running. This task is installed automatically by { -brand-short-name }, and is reinstalled when { -brand-short-nam…`
    - Suggest: `aj v čase, keď`
    - “aj čase, keď aplikácia nie je spustená” is ungrammatical; the locative requires “v”.

### D. Terminology, register & consistency

- `about-logins-import-dialog-items-modified2` — `browser/browser/aboutLogins.ftl` — “Existing entries updated” rendered as “Updated passwords”.
    - Current: `Aktualizované heslá:`
    - Source: `{$count ->} [other] <span>Existing entries updated:</span> <span data-l10n-name="count">{ $count }</span>`
    - Suggest: `Aktualizované existujúce záznamy:`
    - The parallel report string about-logins-import-report-modified2 correctly uses “záznam/záznamy”; the dialog and the report now name the same count differently.
- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — `backup-file-moz-browser-restore-step-2-1` quotes “Obnoviť údaje” but the string it names, `restore-from-backup-header`, reads “Obnovte svoje údaje”
    - Current: `Kliknite na “Obnoviť údaje” a vyberte tento súbor`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Obnovte svoje údaje`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — `backup-file-other-browser-restore-step-3-1` quotes “Obnoviť údaje” but the string it names, `restore-from-backup-header`, reads “Obnovte svoje údaje”
    - Current: `Kliknite na “Obnoviť údaje” a vyberte tento súbor`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Obnovte svoje údaje`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `trustpanel-etp-description-disabled` — `browser/browser/browser.ftl` — “trackers” rendered as “sledovacích zariadení” (tracking devices).
    - Current: `zablokujeme čo najviac sledovacích zariadení`
    - Source: `{ -brand-product-name } thinks companies should follow you less. We block as many trackers as we can when you turn on protections.`
    - Suggest: `zablokujeme čo najviac sledovacích prvkov`
    - Throughout browser.ftl the term “tracker” is “sledovací prvok”; “zariadenie” means a physical device.
- `urlbar-trending-dismissal-acknowledgment` — `browser/browser/browser.ftl` — First-person singular “Ďakujem” where the product elsewhere speaks as “we”.
    - Current: `Ďakujem za spätnú väzbu.`
    - Source: `Thanks for your feedback. You won’t see trending searches anymore.`
    - Suggest: `Ďakujeme za vašu spätnú väzbu.`
    - All sibling acknowledgment strings in the same surface (urlbar-feedback-acknowledgment, urlbar-result-dismissal-acknowledgment-*) use “Ďakujeme”.
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — “Key” translated as “kľúč” instead of “kláves” for a keyboard key.
    - Current: `Kľúč nie je možné použiť`
    - Source: `Key cannot be used`
    - Suggest: `Kláves nie je možné použiť`
    - The rest of the file uses “kláves” for keyboard keys (customkeys-new-key, customkeys-conflict-confirm); “kľúč” means a physical/crypto key.
- `firefoxview-syncedtabs-adddevice-header-3` — `browser/browser/firefoxView.ftl` — Informal second person (tykanie) used where the locale consistently addresses the user formally.
    - Current: `Volajú tvoje karty. Sú v tvojom telefóne.`
    - Source: `Your tabs called. They’re on your phone.`
    - Suggest: `Volajú vaše karty. Sú vo vašom telefóne.`
    - Every other string in this file and the surrounding tree uses the formal “vy/vaše” form (e.g. the adjacent firefoxview-syncedtabs-adddevice-description-3 uses “Naskenujte… vaše”).
- `annotations-default-pdf-handler-body` — `browser/browser/newtab/asrouter.ftl` — Ungrammatical phrase: the adverb "nabudúce" is used to modify a noun.
    - Current: `na nabudúce použitie`
    - Source: `Draw, type, or upload your signature, then place it exactly where you want. Save your go-to signatures for next time.`
    - Suggest: `na budúce použitie`
    - "nabudúce" is an adverb and cannot premodify "použitie"; the correct form is "na budúce použitie" (or "na nabudúce").
- `root-certificate-windows-background-notification-subtitle` — `browser/browser/newtab/asrouter.ftl` — Agreement error between possessive and noun.
    - Current: `naše najnovšiu ochranu a funkcie`
    - Source: `Parts of the browser will stop working soon if you don’t update. Now is a great time to get our latest protections and features.`
    - Suggest: `našu najnovšiu ochranu a funkcie`
    - "ochranu" is feminine accusative singular, so the possessive must be "našu", not the neuter/plural "naše".
- `newtab-download-mobile-highlight-body-variant-b` — `browser/browser/newtab/newtab.ftl` — Indicative "Synchronizujete" used where an imperative is required.
    - Current: `Synchronizujete svoje karty, heslá a ďalšie položky.`
    - Source: `Pick up where you left off when you sync your tabs, passwords, and more.`
    - Suggest: `Synchronizujte svoje karty, heslá a ďalšie položky.`
    - As written the sentence states "you are syncing your tabs" rather than inviting the user to sync; the surrounding highlight strings all use the imperative.
- `newtab-stocks-watchlist-full` — `browser/browser/newtab/newtab.ftl` — Typo in the [one] variant: "obstrániť" instead of "odstrániť".
    - Current: `musíte jednu obstrániť`
    - Source: `{$limit ->} [one] You can add up to { $limit } stock. Remove one to add another. [other] You can add up to { $limit } stocks. Remove one to add another.`
    - Suggest: `musíte jednu odstrániť`
    - "obstrániť" is not a Slovak word; the other plural variants of the same message correctly use "odstrániť".
- `mr2-onboarding-default-theme-label` — `browser/browser/newtab/onboarding.ftl` — Missing preposition after "Pozrite sa".
    - Current: `Pozrite sa predvolené témy vzhľadu`
    - Source: `Explore default themes.`
    - Suggest: `Pozrite sa na predvolené témy vzhľadu`
    - "pozrieť sa" requires the preposition "na" with its object; as written the sentence is ungrammatical.
- `mr2022-language-mismatch-subtitle` — `browser/browser/newtab/onboarding.ftl` — "zatiaľ čo" written as one word.
    - Current: `zatiaľčo`
    - Source: `Thanks to our community, { -brand-short-name } is translated in over 90 languages. It looks like your system is using { $systemLanguage }, and { -brand-short-name } is using { $appLanguage }.`
    - Suggest: `zatiaľ čo`
    - The Slovak conjunction is spelled as two words, "zatiaľ čo".
- `smartwindow-onboarding-title` — `browser/browser/newtab/onboarding.ftl` — Wrong case form of the possessive: dative plural "svojim" where instrumental singular "svojím" is required.
    - Current: `svojim obľúbeným nástrojom`
    - Source: `Make { -smart-window-brand-name } your go-to`
    - Suggest: `svojím obľúbeným nástrojom`
    - "Urobiť si niečo svojím obľúbeným nástrojom" takes the instrumental singular, which is written with a long í.
- `connection-proxy-autologin-checkbox` — `browser/browser/preferences/connection.ftl` — Tooltip has “prihlasovanie údaje” instead of “prihlasovacie údaje”.
    - Current: `ak má preň uložené prihlasovanie údaje`
    - Source: `accesskey: i label: Do not prompt for authentication if password is saved tooltiptext: This option silently authenticates you to proxies when you have saved credentials for them. You will be prompted if authentication f…`
    - Suggest: `ak má preň uložené prihlasovacie údaje`
    - “prihlasovanie” is a noun; the attribute of “údaje” must be the adjective “prihlasovacie”. The same phrase is spelled correctly elsewhere in the tree (e.g. pane-privacy-passwords-header searchkeywords).
- `fonts-langgroup-malayalam` — `browser/browser/preferences/fonts.ftl` — Malayalam misspelled as “Malajamské”.
    - Current: `Malajamské`
    - Source: `label: Malayalam`
    - Suggest: `Malajálamske`
    - The Slovak name of the Malayalam language/script is malajálamčina / malajálamske; “Malajamské” drops a syllable and is not a word.
- `more-from-moz-solo-card-1` — `browser/browser/preferences/moreFromMozilla.ftl` — Ungrammatical “V priebehu chvíľku”.
    - Current: `V priebehu chvíľku si vytvorte`
    - Source: `description: Create your website instantly and connect your own custom domain for free. label: { -solo-ai-brand-name }`
    - Suggest: `Za chvíľku si vytvorte`
    - “v priebehu” requires the genitive (“chvíľky”); “chvíľku” is accusative, so the phrase is ungrammatical as written.
- `content-blocking-etp-standard-tcp-rollout-description` — `browser/browser/preferences/preferences.ftl` — Nonstandard plural “sledovači” for trackers.
    - Current: `takže sledovači ich nemôžu použiť`
    - Source: `Total Cookie Protection contains cookies to the site you’re on, so trackers can’t use them to follow you between sites.`
    - Suggest: `takže sledovacie prvky ich nemôžu použiť`
    - The rest of the file consistently uses “sledovacie prvky”; “sledovači” is an animate-masculine plural form that is neither standard nor used elsewhere in this surface.
- `extension-controlled-enable` — `browser/browser/preferences/preferences.ftl` — Wrong case: “v ponuku” instead of locative “v ponuke”.
    - Current: `Doplnky v ponuku`
    - Source: `To enable the extension go to <img data-l10n-name="addons-icon"/> Add-ons in the <img data-l10n-name="menu-icon"/> menu.`
    - Suggest: `Doplnky v ponuke`
    - The preposition “v” with a static location takes the locative (“v ponuke”); “v ponuku” is accusative and ungrammatical.
- `forms-breach-alerts` — `browser/browser/preferences/preferences.ftl` — Incorrect collocation “prišlo k úniku” instead of “došlo k úniku”.
    - Current: `na ktorých prišlo k úniku dát`
    - Source: `accesskey: b label: Show alerts about passwords for breached websites`
    - Suggest: `na ktorých došlo k úniku dát`
    - Standard Slovak uses “dôjsť k niečomu” for an event occurring; “prísť k úniku” is a calque and is not correct here.
- `payment-moz-box-item-security-code-only` — `browser/browser/preferences/preferences.ftl` — Gender disagreement: “CVV je uložené” vs “CVV je uložený” in the sibling string.
    - Current: `CVV je uložené`
    - Source: `description: CVV saved label: { $cardNumber }`
    - Suggest: `CVV je uložený`
    - payment-moz-box-item-with-security-code in the same list renders the same en-US phrase “CVV saved” as “CVV je uložený”; one of the two agreements must be wrong, and the neuter form does not match the masculine treatment used there.
- `preferences-copy-profile-header` — `browser/browser/preferences/preferences.ftl` — Case mismatch in the coordinated subject list: “históriu” among nominatives.
    - Current: `skopírujú vaše nastavenia, doplnky, históriu a uložené údaje`
    - Source: `description: The new profile will copy your settings, add-ons, history, and saved data like bookmarks and passwords — but not your account or sync info. label: Copy an existing profile`
    - Suggest: `skopírujú vaše nastavenia, doplnky, história a uložené údaje`
    - With the reflexive passive “sa skopírujú”, the listed items are the grammatical subject and must be nominative (nastavenia, doplnky, história, údaje); “históriu” is accusative and breaks agreement.
- `security-privacy-status-pending-trackers-label` — `browser/browser/preferences/preferences.ftl` — Wrong case/number: “sledovacích prvok” instead of “sledovacích prvkov”.
    - Current: `koľko sledovacích prvok`
    - Source: `Looking up how many trackers { -brand-short-name } blocked over the last month`
    - Suggest: `koľko sledovacích prvkov`
    - Genitive plural after “koľko” requires “prvkov”; “prvok” is nominative singular and does not agree with the adjective “sledovacích”.
- `update-history-2` — `browser/browser/preferences/preferences.ftl` — Genitive plural misspelled: “aktualizácii” should be “aktualizácií”.
    - Current: `Zobraziť históriu aktualizácii`
    - Source: `accesskey: p label: Show update history`
    - Suggest: `Zobraziť históriu aktualizácií`
    - “história” governs the genitive plural “aktualizácií” (long í); “aktualizácii” is the singular locative/dative form.
- `update-setting-write-failure-message2` — `browser/browser/preferences/preferences.ftl` — Wrong demonstrative form “toho nastavenia” instead of “tohto nastavenia”.
    - Current: `upravenie toho nastavenia vyžaduje`
    - Source: `{ -brand-short-name } encountered an error and didn’t save this change. Note that changing this update setting requires permission to write to the file below. You or a system administrator may be able to resolve the err…`
    - Suggest: `upravenie tohto nastavenia vyžaduje`
    - Genitive singular neuter of “tento” is “tohto”; “toho” is the form of “ten” and is ungrammatical here.
- `preonboarding-subtitle` — `browser/browser/preonboarding.ftl` — Wrong form of the preposition "s" before a word beginning with z-.
    - Current: `súhlas s Zmluvnými podmienkami`
    - Source: `By continuing, you agree to the { -brand-product-name } Terms of Use and our Privacy Notice. To help improve the browser, { -brand-product-name } sends diagnostic and interaction data to { -vendor-short-name }.`
    - Suggest: `súhlas so Zmluvnými podmienkami`
    - Slovak vocalizes "s" to "so" before words starting with s, z, š, ž; "s Zmluvnými" is ungrammatical.
- `screenshots-too-large-error-details` — `browser/browser/screenshots.ftl` — Missing "ako" in the comparative, leaving the sentence ungrammatical.
    - Current: `jej celková plocha je menej 124 900 000 pixelov`
    - Source: `Try selecting a region that’s smaller than 32,700 pixels on its longest side or 124,900,000 pixels total area.`
    - Suggest: `jej celková plocha je menej ako 124 900 000 pixelov`
    - Slovak comparison requires "menej ako"; without "ako" the clause is broken. The first half of the same sentence uses "menšia ako" correctly.
- `opensearch-error-download-desc` — `browser/browser/search.ftl` — Misspelling of "stiahnuť".
    - Current: `sťiahnuť`
    - Source: `{ -brand-short-name } could not download the search plugin from: { $location-url }`
    - Suggest: `stiahnuť`
    - "sťiahnuť" is not a Slovak word; the infinitive is "stiahnuť" (no caron on t, as used correctly elsewhere in the tree).
- `show-sidebars` — `browser/browser/sidebar.ftl` — Missing accent in the adjective: "bočne" instead of "bočné".
    - Current: `Zobrazí bočne panely`
    - Source: `label: Sidebars tooltiptext: Show sidebars`
    - Suggest: `Zobrazí bočné panely`
    - The plural accusative adjective is "bočné"; "bočne" is an adverb and does not agree with "panely". The same message's .label correctly reads "Bočné panely".
- `sync-disconnect-dialog-body` — `browser/browser/sync.ftl` — Wrong instrumental form of the possessive, and a missing comma before the contrastive "ale".
    - Current: `ukončí synchronizáciu s vašim účtom ale neodstráni`
    - Source: `{ -brand-product-name } will stop syncing your account but won’t delete any of your browsing data on this device.`
    - Suggest: `ukončí synchronizáciu s vaším účtom, ale neodstráni`
    - The instrumental singular of "váš" is "vaším" ("vašim" is the dative plural), and Slovak requires a comma before the coordinating conjunction "ale".
- `STATUS_UNINSTALL_MAIN` — `browser/installer/custom.properties` — Non-standard verb form "Odinštalováva sa".
    - Current: `Odinštalováva sa $BrandShortName…`
    - Source: `Uninstalling $BrandShortName…`
    - Suggest: `Odinštalúva sa $BrandShortName…`
    - The Slovak imperfective of "odinštalovať" is "odinštalúvať" (odinštalúva sa); "odinštalováva" follows the Czech pattern.
- `accessibility.checks.empty2` — `devtools/client/accessibility.properties` — Wrong genitive form “uzlu” instead of “uzla”.
    - Current: `Žiadne kontroly tohto uzlu.`
    - Source: `No checks for this node.`
    - Suggest: `Žiadne kontroly tohto uzla.`
    - The genitive singular of “uzol” is “uzla”; the rest of the tree consistently uses “uzla”.
- `settings.showPausedOverlay.label` — `devtools/client/debugger.properties` — Misspelling “Prí” instead of “Pri”.
    - Current: `Prí pozastavení zobrazovať prekrytie`
    - Source: `Show paused overlay`
    - Suggest: `Pri pozastavení zobrazovať prekrytie`
    - “Prí” is not a Slovak word; the preposition is “pri”.
- `diffing.prompt.selectComparison` — `devtools/client/memory.properties` — Wrong preposition “zo” instead of “so”.
    - Current: `Vyberte záznam na porovnanie zo základným`
    - Source: `Select the snapshot to compare to the baseline`
    - Suggest: `Vyberte záznam na porovnanie so základným`
    - The instrumental “základným” takes “so” (from s); “zo” is the form of “z” and is wrong here.
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “Lokálneho režimu” but the string it names, `options-local-mode-label`, reads “Lokálny režim”
    - Current: `Tento dokument je možné načítať aj z “{ $url }” pomocou “Lokálneho režimu” vo Vývojárskych nástrojoch, ktorý je možné povoliť v paneli nastavení.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Lokálny režim`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `inactive-css-not-table-cell` — `devtools/client/tooltips.ftl` — Case error: “bunku tabuľku” instead of “bunku tabuľky”.
    - Current: `pretože nejde o bunku tabuľku`
    - Source: `<strong>{ $property }</strong> has no effect on this element since it’s not a table cell.`
    - Suggest: `pretože nejde o bunku tabuľky`
    - “tabuľky” must be genitive as the modifier of “bunku”; “tabuľku” repeats the accusative and is ungrammatical.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — Ungrammatical “z dôvodu zapnúť predvoľby” (infinitive instead of participle).
    - Current: `z dôvodu zapnúť predvoľby “Protokol natrvalo”`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `z dôvodu zapnutej predvoľby “Protokol natrvalo”`
    - “z dôvodu” requires a noun phrase in the genitive; the infinitive “zapnúť” makes the sentence ungrammatical.
- `InterceptionFailedWithURL` — `dom/chrome/dom/dom.properties` — The API name ServiceWorker is translated despite an explicit do-not-translate comment.
    - Current: `Skript typu worker zachytil požiadavku`
    - Source: `Failed to load ‘%S’. A ServiceWorker intercepted the request and encountered an unexpected error.`
    - Suggest: `ServiceWorker zachytil požiadavku`
    - The developer comment says "Do not translate 'ServiceWorker'". The locale renders it as "skript typu worker" here and in roughly twenty further strings (CorsResponseForSameOriginRequest, ServiceWorker* registration errors, PushMessage* etc.), which also loses the distinction from the plain Worker API that the same phrase is used for.
- `colorway-removal-notice-message` — `toolkit/toolkit/about/aboutAddons.ftl` — `colorway-removal-notice-message` quotes “Uložené témy” but the string it names, `theme-disabled-heading2`, reads “Uložené témy vzhľadu”
    - Current: `heading: Vaše farebné témy boli odstránené. message: { -brand-product-name } aktualizoval svoju kolekciu farebných tém. Starú verziu (verzie) sme odstránili zo zoznamu „Uložené témy“. Nové verzie nájdete na stránke s do…`
    - Source: `heading: Your colorway theme(s) were removed. message: { -brand-product-name } updated its colorways collection. We removed the old version(s) from your “Saved Themes” list. Get new versions on the add-ons site.`
    - Suggest: `Uložené témy vzhľadu`
    - In the source this string quotes “Saved Themes”, which is exactly the value of `theme-disabled-heading2` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `plugins-widevine-description` — `toolkit/toolkit/about/aboutAddons.ftl` — Typo “požívané” (consumed) for “používané” (used).
    - Current: `Šifrované médiá sú typicky požívané`
    - Source: `This plugin enables playback of encrypted media in compliance with the Encrypted Media Extensions specification. Encrypted media is typically used by sites to protect against copying of premium media content. Visit http…`
    - Suggest: `Šifrované médiá sú typicky používané`
    - “požívať” means to consume/ingest; the intended verb for “used by sites” is “používať”.
- `about-glean-label-for-controls-submit` — `toolkit/toolkit/about/aboutGlean.ftl` — Verb mood/person mismatch: indicative “označíte” coordinated with imperative “odošlite”.
    - Current: `a odošlite vybratý ping`
    - Source: `Press the preceding button to tag all { -glean-brand-name } pings with your tag and submit the selected ping. (All pings submitted from then until you restart the application will be tagged with <code>{ $debug-tag }</co…`
    - Suggest: `a odošlete vybratý ping`
    - The sentence describes what pressing the button does (“Stlačením tohto tlačidla označíte…”), so the coordinated verb must be the indicative “odošlete”, not the imperative “odošlite”.
- `about-logging-upload-question` — `toolkit/toolkit/about/aboutLogging.ftl` — Pronoun does not agree with its antecedent “údaje” (plural).
    - Current: `Chcete ho uložiť alebo nahrať?`
    - Source: `The profile data has been captured. Do you want to save or upload it?`
    - Suggest: `Chcete ich uložiť alebo nahrať?`
    - The preceding sentence is “Údaje profilu boli zaznamenané” (plural neuter); the referring pronoun must be “ich”, not the masculine singular “ho”.
- `profiles-in-use-profile` — `toolkit/toolkit/about/aboutProfiles.ftl` — Agreement/spelling error: “používaní” instead of “používaný”.
    - Current: `Tento profil je používaní inou aplikáciou`
    - Source: `This profile is in use in another application and it cannot be deleted.`
    - Suggest: `Tento profil je používaný inou aplikáciou`
    - The passive participle must agree with the masculine singular subject “profil”: “používaný”. “používaní” is the masculine animate plural form.
- `crashes-time-hours` — `toolkit/toolkit/about/aboutSupport.ftl` — Typo “pre hodinou” in the [one] variant.
    - Current: `pre hodinou`
    - Source: `{$hours ->} [one] { $hours } hour ago [other] { $hours } hours ago`
    - Suggest: `pred hodinou`
    - The preposition is “pred” (ago), as used in the other variants of the same message (“pred { $hours } hodinami”).
- `media-device-channels` — `toolkit/toolkit/about/aboutSupport.ftl` — Non-standard plural “Kanále”.
    - Current: `Kanále`
    - Source: `Channels`
    - Suggest: `Kanály`
    - The standard Slovak nominative plural of “kanál” is “kanály”, as used elsewhere in the tree (e.g. about-webrtc-channels “{ $channels } kanály”).
- `startup-cache-wrote-to-disk-cache` — `toolkit/toolkit/about/aboutSupport.ftl` — Wrong case after “do”: “pamäti” instead of genitive “pamäte”.
    - Current: `Zapísané do vyrovnávacej pamäti na disku`
    - Source: `Wrote to Disk Cache`
    - Suggest: `Zapísané do vyrovnávacej pamäte na disku`
    - The preposition “do” governs the genitive (“pamäte”); “pamäti” is the locative/dative form, correctly used in the neighbouring string “Cesta k vyrovnávacej pamäti”.
- `third-party-detail-occurrences` — `toolkit/toolkit/about/aboutThirdParty.ftl` — “koľko krát” should be written as one word.
    - Current: `koľko krát`
    - Source: `(value): Occurrences title: How many times this module was loaded.`
    - Suggest: `koľkokrát`
    - Slovak orthography writes the adverb as a single word, “koľkokrát”.
- `third-party-tag-shellex` — `toolkit/toolkit/about/aboutThirdParty.ftl` — Missing preposition makes the tooltip ungrammatical.
    - Current: `systémové dialógové okno prácu so súbormi`
    - Source: `(value): Shell Extension title: This type of module is loaded when you open the system file dialog.`
    - Suggest: `systémové dialógové okno pre prácu so súbormi`
    - “dialógové okno” and “prácu so súbormi” are juxtaposed with no preposition or case link; a preposition such as “pre/na” is required.
- `settings-pp-erased-ok` — `toolkit/toolkit/preferences/preferences.ftl` — Primary Password called “primárne heslo” where the whole file uses “hlavné heslo”.
    - Current: `Odstránili ste svoje primárne heslo.`
    - Source: `You have deleted your Primary Password. Stored passwords and certificate private keys managed by { -brand-short-name } will not be protected.`
    - Suggest: `Odstránili ste svoje hlavné heslo.`
    - Every other string in this dialog renders “Primary Password” as “hlavné heslo”; the odd term makes it look like a different setting.

### E. Typography, punctuation & spacing

- `newtab-widget-timer-celebration-heading-break` — `browser/browser/newtab/newtab.ftl` — Uses informal second person singular where the whole tree uses the formal form.
    - Current: `Tvoja prestávka sa skončila`
    - Source: `Your break is over`
    - Suggest: `Vaša prestávka sa skončila`
    - The identical message newtab-widget-timer-notification-break uses "Vaša prestávka sa skončila"; the locale consistently addresses the user with the formal "vy" form.
- `preferences-doh-radio-off` — `browser/browser/preferences/preferences.ftl` — “DNS resolver” left in English where the same term is translated elsewhere in the file.
    - Current: `Použite predvolený DNS resolver`
    - Source: `description: Use your default DNS resolver label: Off`
    - Suggest: `Použije sa predvolený prekladač DNS`
    - The same en-US term is rendered “prekladač DNS” (preferences-doh-off-desc) and “nástroj na prekladanie DNS” (preferences-doh-default-detailed-desc-2) in the same surface; the untranslated “resolver” is the outlier.
- `space-alert-over-5gb-message2` — `browser/browser/preferences/preferences.ftl` — Menu path cites “Možnosti” where the UI (and this file) calls it “Nastavenia”.
    - Current: `v ponuke Možnosti > Súkromie a bezpečnosť`
    - Source: `<strong>{ -brand-short-name } is running out of disk space.</strong> Website contents may not display properly. You can clear stored data in Settings > Privacy & Security > Cookies and Site Data.`
    - Suggest: `v ponuke Nastavenia > Súkromie a bezpečnosť`
    - en-US reads “Settings > Privacy & Security”, and settings-page-title in this same file is “Nastavenia”; the stale “Možnosti” names a menu item that no longer exists.
- `sparkle-single-avatar-tooltip` — `browser/browser/profiles.ftl` — Informal second-person singular imperative in a surface that otherwise uses the infinitive/formal form.
    - Current: `Použi trblietavý avatar`
    - Source: `tooltiptext: Apply sparkle avatar`
    - Suggest: `Použiť trblietavý avatar`
    - Every other avatar tooltip in this file uses the infinitive "Použiť" (a few use the formal plural "Použite"); "Použi" addresses the user with the familiar singular, which the locale does not use elsewhere.
- `contextMenuSearch` — `browser/chrome/browser/browser.properties` — Straight ASCII quotes where the rest of the file uses typographic quotes
    - Current: `Vyhľadať "%2$S" na webe pomocou %1$S`
    - Source: `Search %1$S for “%2$S”`
    - Suggest: `Vyhľadať „%2$S“ na webe pomocou %1$S`
    - The parallel string gnomeSearchProviderSearchWeb in the same file uses “%S”, and the en-US source uses curly quotes here too.
- `geolocation.shareWithSiteUnsafeDelegation2` — `browser/chrome/browser/browser.properties` — Double space inside the visible sentence
    - Current: `aby umožnila  prístup`
    - Source: `Allow %1$S to give %2$S permission to access your location?`
    - Suggest: `aby umožnila prístup`
    - Two consecutive spaces between words appear in the rendered prompt text.
- `dialogTitleEdit` — `browser/chrome/browser/places/bookmarkProperties.properties` — Straight ASCII quotes where the file and locale use typographic quotes
    - Current: `Vlastnosti "%S"`
    - Source: `Properties for “%S”`
    - Suggest: `Vlastnosti „%S“`
    - The adjacent dialogTitleEditBookmark uses curly quotes (“%S”), as does the en-US source here; the straight quotes in this string are inconsistent within the same dialog family.
- `storage-table-type-localstorage-hint` — `devtools/client/storage.ftl` — “local storage” rendered as “Miestne úložisko” while the tree label uses “Lokálne úložisko”.
    - Current: `Miestne úložisko môžete zobraziť a upraviť zvolením servera.`
    - Source: `View and edit the local storage by selecting a host. <a data-l10n-name="learn-more-link">Learn more</a>`
    - Suggest: `Lokálne úložisko môžete zobraziť a upraviť zvolením servera.`
    - storage-tree-labels-local-storage and startup.properties use “Lokálne úložisko”; the hint for the same storage type uses a different term in the same panel.
- `inactive-css-not-floated` — `devtools/client/tooltips.ftl` — “floated elements” rendered as “pohyblivé prvky” (movable) instead of “plávajúce”.
    - Current: `pretože sa vzťahuje iba na pohyblivé prvky`
    - Source: `<strong>{ $property }</strong> has no effect because it only applies to floated elements.`
    - Suggest: `pretože sa vzťahuje iba na plávajúce prvky`
    - inactive-css-not-display-block-on-floated-2 in the same file uses “plávajúci” for float; “pohyblivé” means movable and does not denote CSS float.
- `download-cert-view-text` — `security/manager/security/pippki/pippki.ftl` — CA rendered as "certifikačná agentúra" instead of "certifikačná autorita".
    - Current: `Preskúmať certifikát certifikačnej agentúry`
    - Source: `Examine CA certificate`
    - Suggest: `Preskúmať certifikát certifikačnej autority`
    - Every other string in this file and in certManager.ftl uses "certifikačná autorita" for CA; "agentúra" is not the established term and names a different kind of body.
- `available-updates-heading` — `toolkit/toolkit/about/aboutAddons.ftl` — Plural heading “Available Updates” rendered as a singular sentence.
    - Current: `K dispozícii je aktualizácia`
    - Source: `Available Updates`
    - Suggest: `Dostupné aktualizácie`
    - This heading sits above the list of all available add-on updates and the matching sidebar entry addon-category-available-updates is already “Dostupné aktualizácie”; the singular “An update is available” contradicts the list it heads.
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — Glean pings described as the “ping command”.
    - Current: `vyberte príkaz ping, v ktorom sa nachádza vaša inštrumentácia`
    - Source: `Select from the preceding list the ping your instrumentation is in. If it’s in a <a data-l10n-name="custom-ping-link">custom ping</a>, choose that one. Otherwise, the default for <code>event</code> metrics is the <code>…`
    - Suggest: `vyberte ping, v ktorom sa nachádza vaša inštrumentácia`
    - A Glean ping is a data payload; “príkaz ping” (the ping command) is a different thing, and the rest of the file correctly uses “ping/pingy” as a noun.
- `about-processes-cpu-almost-idle` — `toolkit/toolkit/about/aboutProcesses.ftl` — Decimal separator inconsistent between the two “< 0.1%” cells of the same table.
    - Current: `< 0.1%`
    - Source: `(value): < 0.1% title: Total CPU time: { $total }{ $unit }`
    - Suggest: `< 0,1 %`
    - about-processes-tab-cpu-almost-idle was localized to “< 0,1 %” with the Slovak decimal comma, while this adjacent CPU cell keeps the English “< 0.1%”, so the same value is formatted two ways in one view.
- `about-processes-shutdown-process` — `toolkit/toolkit/about/aboutProcesses.ftl` — “Unload tabs and kill process” uses different verbs than the dedicated unload/kill tooltips on the same table.
    - Current: `Zavrieť karty a zrušiť proces`
    - Source: `title: Unload tabs and kill process`
    - Suggest: `Uvoľniť karty a ukončiť proces`
    - In the same tooltip group about-processes-unload-tab renders “Unload tab” as “Uvoľniť kartu”, about-processes-shutdown-tab renders “Close tab” as “Zavrieť kartu”, and about-processes-kill-process renders “Kill process” as “Ukončiť proces”; here “unload” becomes “close” and “kill” becomes “cancel”, so the icons no longer match their descriptions.
- `about-telemetry-show-archived-ping-data` — `toolkit/toolkit/about/aboutTelemetry.ftl` — “ping” treated as a command (“príkaz ping”) although the page otherwise uses it as a data payload.
    - Current: `Archivované údaje príkazu ping`
    - Source: `Archived ping data`
    - Suggest: `Archivované údaje pingu`
    - A Telemetry ping is a data submission, not the network “ping” command; every other string in the file uses it as a noun (“Typ pingu”, “Zvoľte ping”), so this rendering is both wrong and inconsistent.
- `about-webauthn-auth-info-remaining-discoverable-credentials` — `toolkit/toolkit/about/aboutWebauthn.ftl` — “Credentials” is rendered “poverenia” in some rows and “prihlasovacie údaje” in others on the same page.
    - Current: `Zostávajúce zistiteľné poverenia`
    - Source: `Remaining discoverable credentials`
    - Suggest: `Zostávajúce zistiteľné prihlasovacie údaje`
    - about-webauthn-credential-management-section-title, -credential-list-subsection-title, -auth-option-credmgmt and -auth-info-max-credential-count-in-list all use “prihlasovacie údaje”, while this row and -auth-option-credentialmgmtpreview / -auth-info-max-cred-blob-length use “poverenia”, so one security-token page names the same object two ways.
- `about-webrtc-aec-logging-unavailable-sandbox` — `toolkit/toolkit/about/aboutWebrtc.ftl` — AEC logs called “denníky” while the AEC controls above call the same thing “záznam”.
    - Current: `export denníkov AEC`
    - Source: `The environment variable MOZ_DISABLE_CONTENT_SANDBOX=1 is required to export AEC logs. Only set this variable if you understand the possible risks.`
    - Suggest: `export záznamov AEC`
    - The same page uses “Záznam AEC” for “AEC Logging” and “Zachytené záznamy” for the captured logs; introducing a third word (“denník”, alongside “protokol” in about-webrtc-log-clear) for the same artefact makes the controls hard to match.
- `url-classifier-disable-sbjs-log` — `toolkit/toolkit/about/url-classifier.ftl` — The Safe Browsing JS log is called “denník” here and “protokol” in the row it controls.
    - Current: `Zakázať denník JS služby Safe Browsing`
    - Source: `Disable Safe Browsing JS Log`
    - Suggest: `Zakázať protokol JS služby Safe Browsing`
    - url-classifier-debug-sbjs-modules renders the same “Safe Browsing JS log” as “Protokol JS pre službu Safe Browsing”, and every other log string in the file uses “protokol”; the toggle and the row it affects therefore read as different features.
- `findbar-match-diacritics` — `toolkit/toolkit/main-window/findbar.ftl` — Tooltip's parenthesis is opened but never closed.
    - Current: `(napríklad pri hľadaní slova “diéta” nebude ponúknuté slovo “dieťa”.`
    - Source: `accesskey: i label: Match Diacritics tooltiptext: Distinguish between accented letters and their base letters (for example, when searching for “resume”, “résumé” will not be matched)`
    - Suggest: `(napríklad pri hľadaní slova “diéta” nebude ponúknuté slovo “dieťa”).`
    - The example clause opens with “(” and ends with a period, leaving the parenthesis unbalanced in text the user reads.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sk/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
