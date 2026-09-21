# Firefox l10n QA — hu

| | |
|---|---|
| **Generated** | 2026-09-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `3f7b6c3c060f` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `749ea3a23fef` |
| **Previous run** | 2026-09-14 @ `e44f1369fb6d` |
| **Mode** | incremental |
| **Strings reviewed this run** | 11 of 16,170 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for hu: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 325 |
| Strings | 16,170 |
| Missing strings | 63 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 8 |

### Completeness

**63 strings** are not translated yet, concentrated in:

- `toolkit/toolkit/about/aboutPDF.ftl` — 20
- `browser/browser/newtab/newtab.ftl` — 13
- `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — 6
- `devtools/client/debugger.properties` — 4
- `dom/chrome/security/security.properties` — 3
- `browser/browser/genai.ftl` — 3
- `dom/chrome/dom/dom.properties` — 2
- `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — 2
- `devtools/client/components.properties` — 1
- `devtools/client/perftools.ftl` — 1
- `devtools/client/sourceeditor.properties` — 1
- `browser/browser/migrationWizard.ftl` — 1

**Files absent from the locale:**

- `toolkit/toolkit/about/pdfFeaturesNotification.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 792, `straight-double` 33, `german-double` 2, `curly-single` 1 | **polish-double** |
| apostrophe | `typographic` 1, `straight` 1 | _mixed_ |
| ellipsis | `char` 389, `ascii` 4 | **char** |
| dash | `em` 2, `en` 130 | **en** |
| nbsp | `total` 6, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (243)

> **Reads as a deliberate edit (2).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `ip-protection-site-rules-button` — `browser/browser/ipProtection.ftl` — The description reverses who needs the extra privacy, asserting that the sites must provide privacy rather than that the user wants extra privacy on them.
    - Current: `Állítson be szabályokat azokhoz a webhelyekhez, amelyeknek fokozott adatvédelmet kell biztosítaniuk, vagy ki kell kapcsolni a VPN-t.`
    - Source: `description: Set rules for sites that need extra privacy or VPN turned off. label: Manage website rules`
    - Suggest: `Állítson be szabályokat azokhoz a webhelyekhez, amelyeknél fokozott adatvédelemre van szükség, vagy amelyeknél ki kell kapcsolni a VPN-t.`
    - en-US "sites that need extra privacy or VPN turned off" means sites for which the user needs extra privacy; the Hungarian says the sites are obliged to provide extra privacy.
- `autofill-delete-payment-method-os-prompt-windows` — `toolkit/toolkit/formautofill/formAutofill.ftl` — "delete stored payment method information" was rendered as "akar használni" (wants to use) instead of "törölni akarja" (wants to delete).
    - Current: `A { -brand-short-name } tárolt fizetésimód-információkat akar használni.`
    - Source: `{ -brand-short-name } is trying to delete stored payment method information. Confirm access to this Windows account below.`
    - Suggest: `A { -brand-short-name } törölni akarja a tárolt fizetésimód-információkat.`
    - The en-US says the browser is trying to delete the stored payment method information; the Hungarian says it wants to use it, which misstates the action being authorized (and is inconsistent with the sibling -other/-macos strings).

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 26 |
| 2 | Wrong content (says something other than the English) | 113 |
| 3 | Degraded language (grammar, spelling, terminology) | 75 |
| 4 | Cosmetic (typography, spacing) | 25 |

### A. Functional, markup, variables & plurals

- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — The singular branches say “passwords” instead of “password”.
    - Current: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszavakat az összes szinkronizált eszközéről.`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices. This will also remove any breach alerts that appear here. You cannot undo this action. [other] This will remove al…`
    - Suggest: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszót az összes szinkronizált eszközéről.`
    - en-US [1] reads “This will remove the password saved to …”; the plural noun makes the one-item case wrong and indistinguishable from the *[other] branch.
- `smartbar-mentions-list-recent-tabs-label` — `browser/browser/aiWindow.ftl` — “Recent tabs” is translated as “Recent tags”.
    - Current: `Legújabb címkék`
    - Source: `Recent tabs`
    - Suggest: `Legutóbbi lapok`
    - en-US “Recent tabs” labels the list of recently used tabs; “címkék” means tags, a different concept already used for tag chips.
- `action-log-searching-history` — `browser/browser/aiWindowContent.ftl` — “Searching history” (verb) is rendered as the noun phrase “search history”.
    - Current: `Keresés előzményei`
    - Source: `Searching history`
    - Suggest: `Előzmények keresése`
    - The action log describes an ongoing action; the completed counterpart action-log-searched-history correctly uses “Előzmények keresve”.
- `smart-window-opened-tabs-summary-group` — `browser/browser/aiWindowContent.ftl` — The action is attributed to the user rather than reported as completed by the assistant.
    - Current: `Létrehozta a(z) „{ $label }” csoportot, és megnyitott { $count } lapot.`
    - Source: `{$count ->} [other] Created the group “{ $label }” and opened { $count } tabs.`
    - Suggest: `A(z) „{ $label }” csoport létrehozva és { $count } lap megnyitva.`
    - en-US “Created the group … and opened … tabs.” reports what the assistant did; the Hungarian second-person-formal reading says the user did it, and it contradicts the parallel smart-window-grouped-tabs-summary which uses the passive.
- `smart-window-restore-success-summary` — `browser/browser/aiWindowContent.ftl` — The plural variant is worded in the singular.
    - Current: `*[other] Lap bezárva, majd helyreállítva.`
    - Source: `{$count ->} [one] Tab closed, then restored. [other] Tabs closed, then restored.`
    - Suggest: `*[other] Lapok bezárva, majd helyreállítva.`
    - en-US distinguishes “Tab closed, then restored.” from “Tabs closed, then restored.”; the Hungarian plural branch keeps the singular noun.
- `appmenu-update-available2` — `browser/browser/appMenuNotifications.ftl` — Access key `D` of `appmenu-update-available2` is not present in its label
    - Current: `D`
    - Source: `buttonaccesskey: D buttonlabel: Download label: Update available secondarybuttonaccesskey: m secondarybuttonlabel: Dismiss`
    - The label is “Letöltés”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `appmenu-search-history` — `browser/browser/appmenu.ftl` — “Search history” (verb + object) is rendered as the noun “search history”.
    - Current: `Keresés előzményei`
    - Source: `label: Search history`
    - Suggest: `Előzmények keresése`
    - The developer comment says “This allows to search through the browser's history”, i.e. Search is a verb here.
- `fxa-menu-device-recent-tabs-panel` — `browser/browser/appmenu.ftl` — The synced-device panel title “Recent tabs” is translated as “Recent tags”.
    - Current: `Legújabb címkék`
    - Source: `title: Recent tabs`
    - Suggest: `Legutóbbi lapok`
    - The developer comment states this is the panel of recent tabs on a synced device; “címkék” (tags) names the wrong thing.
- `default-browser-notification-privacy-body-text` — `browser/browser/backgroundtasks/defaultagent.ftl` — “built-in privacy and protection” shortened to “built-in privacy”.
    - Current: `Térjen vissza a { -brand-short-name }hoz a beépített adatvédelemhez.`
    - Source: `Your default changed. Come back to { -brand-short-name } for built-in privacy and protection.`
    - Suggest: `Térjen vissza a { -brand-short-name }hoz a beépített adatvédelemért és védelemért.`
    - The second benefit named by en-US (protection) is dropped from the notification body.
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — “Search Actions” rendered as the noun phrase “search actions”.
    - Current: `Keresési műveletek`
    - Source: `Search Actions`
    - Suggest: `Műveletek keresése`
    - The group comment states “In these actions ‘Search’ is a verb, followed by where the search is performed”; the neighbouring entries use “Könyvjelzők keresése”, “Előzmények keresése”, “Lapok keresése”.
- `customkeys-shortcut-unassigned` — `browser/browser/customkeys.ftl` — “Add shortcut” is translated as “Add launcher icon”.
    - Current: `Indítóikon hozzáadása`
    - Source: `placeholder: Add shortcut`
    - Suggest: `Gyorsbillentyű hozzáadása`
    - In this file “shortcut” means a keyboard shortcut (“gyorsbillentyű”), not a desktop/launcher icon.
- `taskbar-tabs-email-callout-subtitle-v3` — `browser/browser/featureCallout.ftl` — The email taskbar-tab callout says “chat sites” instead of “email sites”.
    - Current: `Indítsa el csevegőoldalait alkalmazásként`
    - Source: `Launch your email sites like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `Indítsa el e-mail-oldalait alkalmazásként`
    - en-US reads “Launch your email sites like an app”; the Hungarian duplicates the chat variant’s wording, so the message contradicts its own title about the inbox.
- `firefoxview-search-text-box-history` — `browser/browser/firefoxView.ftl` — Search placeholder rendered as the noun “search history” instead of “search the history”.
    - Current: `Keresés előzményei`
    - Source: `placeholder: Search history`
    - Suggest: `Előzmények keresése`
    - The developer comment marks “search” as a verb, and all sibling placeholders in the same file use the “X keresése” pattern.
- `menu-help-exit-troubleshoot-mode` — `browser/browser/menubar.ftl` — Reversed meaning: the item that turns Troubleshoot Mode off is labelled as turning it on.
    - Current: `Hibakeresési mód bekapcsolása`
    - Source: `accesskey: M label: Turn Troubleshoot Mode Off`
    - Suggest: `Hibaelhárítási mód kikapcsolása`
    - en-US is “Turn Troubleshoot Mode Off”; the Hungarian says “Turn … Mode On”. It also uses “Hibakeresési” where the sibling string menu-help-enter-troubleshoot-mode2 and safeMode.ftl use “Hibaelhárítási”.
- `menu-history-search` — `browser/browser/menubar.ftl` — “Search History” rendered as the noun phrase “history of searches” instead of the action “search in history”.
    - Current: `Keresés előzményei`
    - Source: `label: Search History`
    - Suggest: `Előzmények keresése`
    - The developer comment states “Search” is a verb, as in “Search in History”. Compare menu-bookmarks-search, correctly rendered “Könyvjelzők keresése”.
- `annotations-make-default-pdf-handler-title` — `browser/browser/newtab/asrouter.ftl` — "Default PDF editor" translated as default PDF viewer.
    - Current: `alapértelmezett PDF-megjelenítője`
    - Source: `Make { -brand-short-name } your default PDF editor?`
    - Suggest: `alapértelmezett PDF-szerkesztője`
    - The message is about editing/signing PDFs; "megjelenítő" is the term used for the PDF viewer (policy-PDFjs), so it understates and confuses the two features.
- `fxa-menu-message-mobile-primary-text` — `browser/browser/newtab/asrouter.ftl` — Imperative CTA "Send tabs to your phone" turned into a third-person statement.
    - Current: `Lapokat küld a telefonjára`
    - Source: `Send tabs to your phone`
    - Suggest: `Küldjön lapokat a telefonjára`
    - "Lapokat küld" reads as "it sends tabs"; the neighbouring primary texts in the same group use imperatives ("Szinkronizálja…", "Készítsen…", "Tartsa…").
- `newtab-privacy-message-info-11` — `browser/browser/newtab/newtab.ftl` — "more private" rendered as "more securely".
    - Current: `hogyan segíti elő, hogy biztonságosabban böngésszen`
    - Source: `Find out how { -brand-short-name } helps keep your browsing more private.`
    - Suggest: `hogyan segít abban, hogy bizalmasabban böngésszen`
    - The source is about privacy, not security; the same widget renders "more private" as "bizalmasabban" (newtab-privacy-message-promo-vpn-3, promo-private-window-1).
- `newtab-section-following-button` — `browser/browser/newtab/newtab.ftl` — "Following" (state) rendered identically to "Follow" (action).
    - Current: `Követés`
    - Source: `Following`
    - Suggest: `Követve`
    - newtab-section-follow-button is also "Követés", so the followed state is indistinguishable from the follow action; the state label should be "Követve" (cf. newtab-section-blocked-button = "Blokkolva").
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — "Loading more matches" translated as loading more search results.
    - Current: `További találatok betöltése…`
    - Source: `Loading more matches…`
    - Suggest: `További mérkőzések betöltése…`
    - "matches" here means sports matches ("mérkőzés"), which is the term used throughout the sports widget; "találat" means a search hit.
- `newtab-sports-widget-watch` — `browser/browser/newtab/newtab.ftl` — "Watch" (view a live stream) translated as "Follow", colliding with the widget's follow-teams action.
    - Current: `Követés`
    - Source: `label: Watch title: Watch live`
    - Suggest: `Megtekintés`
    - The dev comment says "Watch is a verb (as in watch matches online)". "Követés" is the term the same widget uses for following teams (newtab-sports-widget-follow-teams), so the button now reads as a different, existing action.
- `newtab-topsites-add-shortcut-header` — `browser/browser/newtab/newtab.ftl` — "Shortcut" translated as "quick search" instead of the term used everywhere else.
    - Current: `Új gyorskereső`
    - Source: `New Shortcut`
    - Suggest: `Új indítóikon`
    - Top Sites shortcuts are rendered "indítóikon" throughout the file (newtab-topsites-add-shortcut-label, newtab-custom-shortcuts-title); "gyorskereső" means quick-search and misdescribes the dialog.
- `newtab-topsites-edit-shortcut-header` — `browser/browser/newtab/newtab.ftl` — "Edit Shortcut" translated as editing a quick search.
    - Current: `Gyorskereső szerkesztése`
    - Source: `Edit Shortcut`
    - Suggest: `Indítóikon szerkesztése`
    - Same inconsistency as newtab-topsites-add-shortcut-header; the rest of the file uses "indítóikon" for shortcut.
- `newtab-wallpaper-category-title-celestial` — `browser/browser/newtab/newtab.ftl` — "Celestial" rendered with the religious sense the developer comment explicitly warns against.
    - Current: `Mennyei`
    - Source: `Celestial`
    - Suggest: `Égi`
    - The comment says the word means astronomical/sky-related and is "Not to be confused with religious definition of the word." Hungarian "mennyei" means heavenly/divine (and colloquially 'delicious'); the astronomy sense is "égi".
- `appearance-browser-icon-requirement` — `browser/browser/preferences/browserIcon.ftl` — "Complete" rendered as "fill out (a form)".
    - Current: `Töltse ki, és oldjon fel további rókás ikonokat`
    - Source: `message: Complete and unlock bonus fox icons to personalize { -brand-short-name }.`
    - Suggest: `Teljesítse a feltételeket, és oldjon fel további rókás ikonokat`
    - en-US: "Complete and unlock bonus fox icons" refers to completing the requirements (default browser + pinned to taskbar). "Töltse ki" means filling in a form and makes the sentence unintelligible in context.
- `cookie-banner-blocker-description` — `browser/browser/preferences/preferences.ftl` — "refuses for you" rendered as "rejects you".
    - Current: `a { -brand-short-name } automatikusan elutasítja Önt`
    - Source: `When a site asks if they can use cookies in private browsing mode, { -brand-short-name } automatically refuses for you. Only on supported sites.`
    - Suggest: `a { -brand-short-name } automatikusan elutasítja Ön helyett`
    - en-US: "{ -brand-short-name } automatically refuses for you". The Hungarian says the browser rejects the user, not that it declines the cookie request on the user's behalf.
- `open-external-link-next-to-active-tab` — `browser/browser/preferences/preferences.ftl` — Modifier attached to the wrong noun, changing the meaning.
    - Current: `Hivatkozások megnyitása az aktív lap melletti alkalmazásokból`
    - Source: `label: Open links from apps next to your active tab`
    - Suggest: `Alkalmazásokból származó hivatkozások megnyitása az aktív lap mellett`
    - en-US: "Open links from apps next to your active tab" — the links open next to the active tab. The Hungarian reads "open links from the apps that are next to the active tab", which is not what the preference does.
- `sidebar-history-sort-option-date-and-site` — `browser/browser/sidebar.ftl` — Sort option says “Date and time” instead of “Date and site”.
    - Current: `Dátum és idő`
    - Source: `label: Date and site`
    - Suggest: `Dátum és webhely`
    - en-US is “Date and site”; the adjacent option sidebar-history-sort-option-site is correctly “Webhely”, so the sort criterion is misnamed.
- `tab-context-separate-split-view` — `browser/browser/tabbrowser.ftl` — Verb “Separate” rendered as the adverb “apart”, so the menu item reads as a state, not an action.
    - Current: `Külön osztott nézet`
    - Source: `accesskey: t label: Separate Split View`
    - Suggest: `Osztott nézet szétválasztása`
    - The developer comment says “Separate” is a verb; split-view-menuitem-separate-tabs correctly uses “Lapok szétválasztása”.
- `text-recognition-modal-searching-title` — `browser/browser/textRecognition.ftl` — Subject and object are swapped: says “searching for an image by text” instead of “searching the image for text”.
    - Current: `Kép keresése szöveg alapján…`
    - Source: `Searching image for text…`
    - Suggest: `Szöveg keresése a képen…`
    - en-US “Searching image for text…” means scanning the image to find text; the Hungarian states the opposite relationship.
- `webrtc-allow-share-screen-and-microphone-unsafe-delegation` — `browser/browser/webrtcIndicator.ftl` — Permission prompt names the camera instead of the microphone.
    - Current: `hozzáférjen a kamerájához és lássa a képernyőjét?`
    - Source: `Allow { $origin } to give { $thirdParty } access to your microphone and see your screen?`
    - Suggest: `hozzáférjen a mikrofonjához, és lássa a képernyőjét?`
    - en-US: “give { $thirdParty } access to your microphone and see your screen?”. The prompt grants microphone + screen access, so naming the camera misinforms the user about what is being granted.
- `edit-controls.tooltiptext2` — `browser/chrome/browser/customizableui/customizableWidgets.properties` — The noun phrase “Edit controls” is rendered as the command “Edit the controls”.
    - Current: `Vezérlőelemek szerkesztése`
    - Source: `Edit controls`
    - Suggest: `Szerkesztésvezérlők`
    - This tooltip names the cut/copy/paste widget group, as the sibling label edit-controls.label correctly renders it (“Szerkesztésvezérlők”); the tooltip instead promises that the controls themselves can be edited.
- `dialogTitleEditBookmarkFolder` — `browser/chrome/browser/places/bookmarkProperties.properties` — “Edit bookmark folder” translated as “Add bookmark folder”.
    - Current: `Könyvjelző mappa hozzáadása`
    - Source: `Edit bookmark folder`
    - Suggest: `Könyvjelző mappa szerkesztése`
    - The dialog title for editing is identical to dialogTitleAddBookmarkFolder; en-US is “Edit bookmark folder” and the parallel string dialogTitleEditBookmarksFolder correctly uses “szerkesztése”.
- `clientSocketMisconfiguration` — `browser/chrome/overrides/appstrings.properties` — “doesn’t know how to communicate” rendered as “doesn’t know whether to communicate”.
    - Current: `A Firefox nem tudja, hogy kommunikáljon a kiszolgálóval.`
    - Source: `Firefox doesn’t know how to communicate with the server.`
    - Suggest: `A Firefox nem tudja, hogyan kommunikáljon a kiszolgálóval.`
    - Without “hogyan”, the clause reads as uncertainty about whether to communicate, not about the manner; the manner is what en-US states.
- `LicenseTextRB` — `browser/installer/override.properties` — "select the first option below" became "choose from the options below".
    - Current: `válasszon az alábbi lehetőségek közül`
    - Source: `Please review the license agreement before installing $BrandFullNameDA. If you accept all terms of the agreement, select the first option below. $_CLICK`
    - Suggest: `válassza az alábbi első lehetőséget`
    - The English tells the user which specific radio button to pick; the Hungarian drops "first", so the instruction no longer identifies the accept option.
- `about-debugging-browser-version-too-recent` — `devtools/client/aboutdebugging.ftl` — An extra sentence was added: the message tells the user twice to update, once about the wrong browser.
    - Current: `Frissítse a csatlakoztatott böngészőt. Frissítse a Firefoxot.`
    - Source: `The connected browser is more recent ({ $runtimeVersion }, buildID { $runtimeID }) than your { -brand-shorter-name } ({ $localVersion }, buildID { $localID }). This is an unsupported setup and may cause DevTools to fail…`
    - Suggest: `Frissítse a Firefoxot.`
    - en-US has only "Please update Firefox." here; instructing the user to update the connected (remote) browser contradicts the message, which says the connected browser is newer.
- `about-debugging-runtime-profile-button2` — `devtools/client/aboutdebugging.ftl` — "Profile performance" (verb phrase) rendered as the noun phrase "Performance of the profile".
    - Current: `about-debugging-runtime-profile-button2 = Profil teljesítménye`
    - Source: `Profile performance`
    - Suggest: `about-debugging-runtime-profile-button2 = Teljesítmény profilozása`
    - The comment says this is the button that opens the performance profiler panel; "Profil teljesítménye" states a property of a profile instead of the action.
- `about-debugging-worker-fetch-not-listening` — `devtools/client/aboutdebugging.ftl` — Negation dropped: the "not listening for fetch events" state is translated identically to the "listening" state.
    - Current: `.value = Fetch események figyelése`
    - Source: `label: Fetch value: Not listening for fetch events`
    - Suggest: `.value = Nem figyeli a Fetch eseményeket`
    - en-US: "Not listening for fetch events" vs. the sibling string "Listening for fetch events"; the Hungarian value is identical for both keys, so the UI reports the opposite state.
- `accessibility-text-label-issue-optgroup-label2` — `devtools/client/accessibility.ftl` — "label attribute" rendered as "label element".
    - Current: `Használja a <code>label</code> elemet, hogy címkét adjon a <span>optgroup</span> elemnek.`
    - Source: `Use a <code>label</code> attribute to label an <span>optgroup</span>. <a>Learn more</a>`
    - Suggest: `Használja a <code>label</code> attribútumot, hogy címkét adjon az <span>optgroup</span> elemnek.`
    - en-US says "Use a label attribute"; an optgroup is labelled by its label attribute, not by a label element, and the parallel key in devtools/shared/accessibility.properties says "attribútumot".
- `manifest-item-identity` — `devtools/client/application.ftl` — Manifest "Identity" section header translated as "User".
    - Current: `manifest-item-identity = Felhasználó`
    - Source: `Identity`
    - Suggest: `manifest-item-identity = Azonosság`
    - The section shows the web app manifest's identity fields (name, short_name); "Felhasználó" means "user" and names the wrong thing.
- `boxmodel.offsetParent.title` — `devtools/client/boxmodel.properties` — "Offset parent of the selected element" turned into "Offset of the selected element's parent".
    - Current: `boxmodel.offsetParent.title = A kiválasztott elem szülőjének eltolása`
    - Source: `Offset parent of the selected element`
    - Suggest: `boxmodel.offsetParent.title = A kiválasztott elem eltolási szülője`
    - The comment says the previewed DOM node is the offset parent of the positioned element; the Hungarian describes an offset belonging to the parent instead.
- `callStack.group.collapseTooltip` — `devtools/client/debugger.properties` — Call-stack "frames" translated as "képkockák" (video frames).
    - Current: `callStack.group.collapseTooltip = %S képkockák összecsukása`
    - Source: `Collapse %S frames`
    - Suggest: `callStack.group.collapseTooltip = %S keretek összecsukása`
    - Same defect as callStack.group.expandTooltip; "keret" is used for stack frames elsewhere in this file (restartFrame, callStack.group.collapseTooltipWithSelectedFrame).
- `callStack.group.expandTooltip` — `devtools/client/debugger.properties` — Call-stack "frames" translated as "képkockák" (video frames).
    - Current: `callStack.group.expandTooltip = %S képkockák megjelenítése`
    - Source: `Show %S frames`
    - Suggest: `callStack.group.expandTooltip = %S keretek megjelenítése`
    - These are stack frames in the Call Stack pane; the neighbouring string callStack.group.collapseTooltipWithSelectedFrame correctly uses "keret".
- `outline.placeholder.functions` — `devtools/client/debugger.properties` — "Filter functions" (verb + object) read as a compound noun "filter functions".
    - Current: `outline.placeholder.functions = Szűrőfüggvények`
    - Source: `Filter functions`
    - Suggest: `outline.placeholder.functions = Függvények szűrése`
    - This is the placeholder of a filter input; "Szűrőfüggvények" names functions that do filtering. The sibling key outline.placeholder.atRules correctly uses "@-szabályok szűrése". The same wrong value is also in outline.placeholder.
- `layout.displayLineNumbers` — `devtools/client/layout.properties` — Grid "line numbers" rendered as "number of lines".
    - Current: `layout.displayLineNumbers = Sorok számának megjelenítése`
    - Source: `Display line numbers`
    - Suggest: `layout.displayLineNumbers = Vonalszámok megjelenítése`
    - The option displays the numbers of the CSS grid lines in the overlay, not a count of rows; "Sorok száma" means how many rows there are.
- `toolbar.view.census` — `devtools/client/memory.properties` — "Aggregate" view rendered as "Összetett" (composite/complex).
    - Current: `toolbar.view.census = Összetett`
    - Source: `Aggregate`
    - Suggest: `toolbar.view.census = Összesített`
    - The view aggregates objects into groups; toolbar.pop-view.label already translates "aggregates" as "összesítés", so "Összetett" is both wrong and inconsistent (also used in snapshot.state.saving-census.full).
- `charts.cacheDisabled` — `devtools/client/netmonitor.properties` — The chart label "Empty cache" rendered as the action "Emptying the cache".
    - Current: `charts.cacheDisabled = Gyorsítótár ürítése`
    - Source: `Empty cache`
    - Suggest: `charts.cacheDisabled = Üres gyorsítótár`
    - This labels a chart series describing the empty-cache case, parallel to charts.cacheEnabled = "Feltöltött gyorsítótár"; a verbal noun reads as a command to clear the cache.
- `netmonitor.custom.postBody.placeholder` — `devtools/client/netmonitor.properties` — Request body "payload" translated as "hasznos forgalom" (useful traffic).
    - Current: `netmonitor.custom.postBody.placeholder = hasznos forgalom`
    - Source: `payload`
    - Suggest: `netmonitor.custom.postBody.placeholder = tartalom`
    - The placeholder sits in the request body textarea; "forgalom" means network traffic, which is not what a request body is.
- `netmonitor.headers.requestPriority` — `devtools/client/netmonitor.properties` — "Request Priority" rendered as "Requesting priority".
    - Current: `netmonitor.headers.requestPriority = Prioritás kérése`
    - Source: `Request Priority`
    - Suggest: `netmonitor.headers.requestPriority = Kérés prioritása`
    - The label identifies the priority of the request (comment: "identifying the request priority"); "Prioritás kérése" means asking for priority.
- `requestHeadersFromUpload` — `devtools/client/netmonitor.properties` — "Request headers from upload stream" turned into the action "Requesting headers from the upload stream".
    - Current: `requestHeadersFromUpload = Fejlécek kérése a feltöltési adatfolyamból`
    - Source: `Request headers from upload stream`
    - Suggest: `requestHeadersFromUpload = Kérésfejlécek a feltöltési adatfolyamból`
    - This is a section label identifying request headers taken from the POST body upload stream, not an action; compare requestHeaders = "Kérés fejlécei".
- `traceFunctionReturn` — `devtools/client/startup.properties` — "Trace function returns" (a menu action) rendered as the statement "The tracing function returns".
    - Current: `traceFunctionReturn = A nyomkövetési függvény visszatér`
    - Source: `Trace function returns`
    - Suggest: `traceFunctionReturn = Függvény-visszatérések nyomkövetése`
    - The comment says this menu item enables logging when a function call returns; the Hungarian parses "trace" as an adjective and "returns" as a verb, making it a sentence instead of a command.
- `toolbox.parentProcessBrowserToolboxTitle` — `devtools/client/toolbox.properties` — Reversed head noun: "the parent process of the Browser Toolbox" instead of "Parent process Browser Toolbox".
    - Current: `toolbox.parentProcessBrowserToolboxTitle = A böngésző eszköztár szülőfolyamata`
    - Source: `Parent process Browser Toolbox`
    - Suggest: `toolbox.parentProcessBrowserToolboxTitle = Szülőfolyamati böngésző eszköztár`
    - The comment says this is the title of the Browser Toolbox scoped to the parent process, not a name for a process; compare toolbox.multiProcessBrowserToolboxTitle, which keeps the correct head noun.
- `inactive-css-resize` — `devtools/client/tooltips.ftl` — "elements with an overflow value other than visible" reduced to "elements with an overflowing value".
    - Current: `csak a túlcsorduló értékkel rendelkező elemekre`
    - Source: `<strong>{ $property }</strong> has no effect on this element since it can only be applied to elements with an overflow value other than visible, and to certain replaced elements, such as textareas.`
    - Suggest: `csak a <strong>visible</strong> értéktől eltérő overflow értékkel rendelkező elemekre`
    - en-US restricts the rule to elements whose overflow is not visible; the Hungarian drops the property name and the exclusion, changing the stated condition.
- `whypaused-assert` — `devtools/shared/debugger-paused-reasons.ftl` — "Paused on assertion" translated as "Paused on evaluation".
    - Current: `whypaused-assert = Várakoztatás kiértékeléskor`
    - Source: `Paused on assertion`
    - Suggest: `whypaused-assert = Várakoztatás állításkor`
    - "kiértékelés" means evaluation; the pause reason is an assertion failure, and evaluation is a distinct concept used elsewhere in DevTools ("Kiértékelés eredménye").
- `webconsole.input.selector.top` — `devtools/shared/webconsole.properties` — "Top" (the top-level execution context) rendered as the direction "Up".
    - Current: `webconsole.input.selector.top = Fel`
    - Source: `Top`
    - Suggest: `webconsole.input.selector.top = Legfelső`
    - Same defect as in devtools/client/webconsole.properties: the comment says this names the primary thread of execution, not a direction.
- `ManifestImageRepeatedPurposes` — `dom/chrome/dom/dom.properties` — “repeated purpose(s)” became “contains several purposes”, which is not an error condition.
    - Current: `elem több célt is tartalmaz: %3$S.`
    - Source: `%1$S item at index %2$S includes repeated purpose(s): %3$S.`
    - Suggest: `elem ismétlődő célo(ka)t tartalmaz: %3$S.`
    - en-US: “%1$S item at index %2$S includes repeated purpose(s): %3$S.” Multiple distinct purposes are legal; only repetition is warned about.
- `PointerLockDeniedSandboxed` — `dom/chrome/dom/dom.properties` — Adds “by user preference”, which the source does not say; the restriction comes from the sandbox.
    - Current: `mert a felhasználói beállításokban a mutatózárolási API-t homokozó korlátozza`
    - Source: `Request for pointer lock was denied because Pointer Lock API is restricted via sandbox.`
    - Suggest: `mert a mutatózárolási API-t homokozó korlátozza`
    - en-US: “…because Pointer Lock API is restricted via sandbox.” The added clause was copied from PointerLockDeniedDisabled and names the wrong cause.
- `RewriteYouTubeEmbedPathParams` — `dom/chrome/dom/dom.properties` — The middle sentence says the query was invalid and stripped from the URL, not that params were unsupported and converted.
    - Current: `A lekérdezés érvénytelen volt, és el lett távolítva a webcímből.`
    - Source: `Rewriting old-style YouTube Flash embed (%S) to iframe embed (%S). Params were unsupported by iframe embeds and converted. Please update page to use iframe instead of embed/object, if possible.`
    - Suggest: `A paramétereket az iframe-beágyazás nem támogatta, ezért át lettek alakítva.`
    - en-US: “Params were unsupported by iframe embeds and converted.” The translation states a different action (removal) on a different object.
- `PEPRSyntaxFieldExpectedPipe` — `dom/chrome/layout/css.properties` — The “pipe” character is translated as “csővezeték” (pipeline/plumbing).
    - Current: `melyek nincsenek csővezetékkel elválasztva`
    - Source: `@property syntax descriptor ‘%S’ contains components without a pipe between them.`
    - Suggest: `melyeket nem választ el függőleges vonal (\|)`
    - en-US “contains components without a pipe between them” refers to the “\|” character; “csővezeték” means a physical pipe and gives no clue about the syntax error.
- `CookieRejectedInvalidPath` — `netwerk/necko.properties` — The path-rejection message says “invalid prefix” instead of “invalid path”, duplicating the neighbouring prefix string.
    - Current: `A(z) „%1$S” süti elutasítva az érvénytelen előtag miatt.`
    - Source: `Cookie “%1$S” has been rejected for invalid path.`
    - Suggest: `A(z) „%1$S” süti elutasítva az érvénytelen útvonal miatt.`
    - en-US: “Cookie “%1$S” has been rejected for invalid path.” As translated it is identical to CookieRejectedInvalidPrefix, so developers get the wrong diagnosis.
- _…and 31 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `ip-protection-site-rules-button` — `browser/browser/ipProtection.ftl` — The description reverses who needs the extra privacy, asserting that the sites must provide privacy rather than that the user wants extra privacy on them.
    - Current: `Állítson be szabályokat azokhoz a webhelyekhez, amelyeknek fokozott adatvédelmet kell biztosítaniuk, vagy ki kell kapcsolni a VPN-t.`
    - Source: `description: Set rules for sites that need extra privacy or VPN turned off. label: Manage website rules`
    - Suggest: `Állítson be szabályokat azokhoz a webhelyekhez, amelyeknél fokozott adatvédelemre van szükség, vagy amelyeknél ki kell kapcsolni a VPN-t.`
    - en-US "sites that need extra privacy or VPN turned off" means sites for which the user needs extra privacy; the Hungarian says the sites are obliged to provide extra privacy.
- `newtab-recent-searches-widget-menu-button` — `browser/browser/newtab/newtab.ftl` — "Recent searches options" mistranslated as "recent search options" (options of the widget, not options for searching).
    - Current: `aria-label: Legutóbbi keresési lehetőségek`
    - Source: `aria-label: Recent searches options`
    - Suggest: `aria-label: Legutóbbi keresések beállításai`
    - The source names the options/menu of the "Recent searches" widget; the Hungarian reads as "recent search possibilities", changing the meaning.
- `onboarding-refresh-data-collection-link` — `browser/browser/newtab/onboarding.ftl` — "Manage" translated as "módosítása" (change) instead of "kezelése" (manage).
    - Current: `Adatgyűjtési beállítások módosítása`
    - Source: `Manage data collection settings`
    - Suggest: `Adatgyűjtési beállítások kezelése`
    - en-US "Manage data collection settings"; the established Hungarian term for Manage is "kezelése".
- `onboarding-refresh-terms-of-use-with-links` — `browser/browser/newtab/onboarding.ftl` — "interaction data" is rendered as "használati adatok" (usage data) instead of interaction data.
    - Current: `diagnosztikai és használati adatokat`
    - Source: `By continuing, you agree to the <a data-l10n-name="terms_of_use">{ -brand-product-name } Terms of Use</a> and our <a data-l10n-name="privacy_notice">Privacy Notice</a>. To help improve the browser, { -brand-product-name…`
    - Suggest: `diagnosztikai és interakciós adatokat`
    - en-US says "diagnostic and interaction data"; "használati" means usage, a different data category in Mozilla's privacy terminology.
- `containers-site-container-label` — `browser/browser/preferences/containers.ftl` — Singular "Container" label rendered as plural "Konténerek".
    - Current: `label: Konténerek`
    - Source: `label: Container`
    - Suggest: `label: Konténer`
    - The en-US source is the singular field label "Container" for a single-select field; the Hungarian uses the plural form.
- `autofill-address-department` — `browser/browser/preferences/formAutofill.ftl` — Administrative division rendered as an organizational "department".
    - Current: `Részleg`
    - Source: `Department`
    - Suggest: `Megye (departamento)`
    - The developer comment states this is the primary administrative division used in Nicaragua and Colombia. "Részleg" means a section/unit of a company or institution, not a territorial division.
- `autofill-address-parish` — `browser/browser/preferences/formAutofill.ftl` — Civil division rendered with the religious term.
    - Current: `Egyházközség`
    - Source: `Parish`
    - Suggest: `Kerület (parish)`
    - The comment states this is primary address information (1 level below the country) in Barbados and Jamaica; "egyházközség" denotes a church congregation, not a civil administrative unit.
- `autofill-address-post-town` — `browser/browser/preferences/formAutofill.ftl` — "Post town" rendered as "post station".
    - Current: `Postaállomás`
    - Source: `Post town`
    - Suggest: `Postaváros`
    - The comment marks this as secondary address information for GB/NO/SE — the town used for postal routing, not a postal facility ("postaállomás").
- `fxa-menu-signed-out-title` — `browser/browser/sync.ftl` — "Sign in to sync" is rendered as "Sign in to Sync" treating sync as the product name, and the brand is inflected oddly.
    - Current: `Jelentkezzen be a Syncbe`
    - Source: `Sign in to sync`
    - Suggest: `Jelentkezzen be a szinkronizáláshoz`
    - The en-US uses the verb "sync" (to synchronize), not the capitalized Sync feature brand; the Hungarian asserts signing in *into* Sync.
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — “Beta” translated as “Béta” although the developer comment forbids translating it.
    - Current: `Próbálja ki a privát fordításokat a { -brand-shorter-name }ban – Béta`
    - Source: `tooltiptext: Try private translations in { -brand-shorter-name } - Beta`
    - Suggest: `Próbálja ki a privát fordításokat a { -brand-shorter-name }ban – Beta`
    - The comment immediately above the string says “Beta” should not be translated because it mirrors the un-localized BETA icon.
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — “Beta” translated as “Béta” although the developer comment forbids translating it.
    - Current: `Oldal lefordítása – Béta`
    - Source: `tooltiptext: Translate this page - Beta`
    - Suggest: `Oldal lefordítása – Beta`
    - The comment states: “Note that here "Beta" should not be translated, as it is a reflection of the un-localized BETA icon that is in the panel.”
- `serviceworker-empty-suggestions2` — `devtools/client/application.ftl` — "service worker" misspelled as "server worker" twice in the same string.
    - Current: `server workernek`
    - Source: `If the current page should have a service worker, you could look for errors in the <a>Console</a> or step through your service worker registration in the <span>Debugger</span>.`
    - Suggest: `service workernek`
    - The technology name is "service worker" and is spelled correctly everywhere else in this file (serviceworker-empty-intro2, serviceworker-worker-debug).
- `inspector-emulation-panel-reduced-motion-no-preference` — `devtools/client/inspector.ftl` — The aria-label reverses the meaning: "Enable no preference for reduced motion emulation" is rendered as "turn off" the setting.
    - Current: `aria-label: A mozgáscsökkentés-emuláció beállításának kikapcsolása`
    - Source: `(value): No preference aria-label: Enable no preference for reduced motion emulation`
    - Suggest: `aria-label: A „nincs beállítva” mozgáscsökkentés-emuláció engedélyezése`
    - The en-US enables the "no preference" option of the reduced-motion emulation; the Hungarian says the setting is being disabled (kikapcsolása), which is the opposite action.
- `about-sync-log-page-header` — `toolkit/services/aboutSyncLog.ftl` — Heading "Sync logs" rendered as "Naplók szinkronizálása" ("Synchronizing logs").
    - Current: `heading: Naplók szinkronizálása`
    - Source: `description: Diagnostic logs written by sync. heading: Sync logs`
    - Suggest: `heading: Szinkronizálási naplók`
    - "Sync logs" names logs written by Sync (per the same string's description), not the act of synchronizing logs; also inconsistent with "szinkronizálási naplók" used in about-sync-log-empty.
- `about-sync-log-title` — `toolkit/services/aboutSyncLog.ftl` — "Sync logs" (noun phrase) rendered as "Naplók szinkronizálása" ("Synchronizing logs"), an action rather than the logs of Sync.
    - Current: `Naplók szinkronizálása`
    - Source: `Sync logs`
    - Suggest: `Szinkronizálási naplók`
    - The en-US is a noun phrase naming the logs written by Sync (see about-sync-log-page-header description); the Hungarian turns it into a verbal phrase meaning "syncing the logs".
- `autofill-delete-payment-method-os-prompt-windows` — `toolkit/toolkit/formautofill/formAutofill.ftl` — "delete stored payment method information" was rendered as "akar használni" (wants to use) instead of "törölni akarja" (wants to delete).
    - Current: `A { -brand-short-name } tárolt fizetésimód-információkat akar használni.`
    - Source: `{ -brand-short-name } is trying to delete stored payment method information. Confirm access to this Windows account below.`
    - Suggest: `A { -brand-short-name } törölni akarja a tárolt fizetésimód-információkat.`
    - The en-US says the browser is trying to delete the stored payment method information; the Hungarian says it wants to use it, which misstates the action being authorized (and is inconsistent with the sibling -other/-macos strings).
- `btp-warning-tracker-classified` — `toolkit/toolkit/global/antiTracking.ftl` — "bounce tracker" was translated although the developer comment forbids it.
    - Current: `visszapattanás-követőnek lett besorolva`
    - Source: `{$gracePeriodSeconds ->} [other] “{ $siteHost }” has been classified as a bounce tracker. If it does not receive user activation within the next { $gracePeriodSeconds } seconds it will have its state purged.`
    - Suggest: `„bounce tracker”-nek lett besorolva`
    - The comment directly above the string states: 'Do not translate "bounce tracker".'
- `btp-warning-tracker-purged` — `toolkit/toolkit/global/antiTracking.ftl` — "bounce tracker" was translated although the developer comment forbids it.
    - Current: `visszapattanás-követőként észlelték`
    - Source: `The state of “{ $siteHost }” was recently purged because it was detected as a bounce tracker.`
    - Suggest: `„bounce tracker”-ként észlelték`
    - The comment directly above the string states: 'Do not translate "bounce tracker".'

### C. Grammar, agreement & spelling

- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — Missing hyphen before the suffix attached to the brand term placeholder.
    - Current: `Ossza meg a { -brand-product-name }ot`
    - Source: `Want to help? <label data-l10n-name="helpus-donateLink">Make a donation</label>, <label data-l10n-name="helpus-shareFirefoxLink">share { -brand-product-name }</label>, or <label data-l10n-name="helpus-getInvolvedLink">g…`
    - Suggest: `Ossza meg a { -brand-product-name }-ot`
    - In Hungarian, suffixes appended to a brand name rendered from a placeholder are joined with a hyphen (e.g. „a Firefox-ot” style used for term placeholders); „{ -brand-product-name }ot” concatenates the suffix directly, producing „Firefoxot” without the required separation and is inconsistent with the other referral strings that avoid suffixing the placeholder.
- `about-private-browsing-cookie-banners-promo-body` — `browser/browser/aboutPrivateBrowsing.ftl` — Wrong case on the quantifier: “kevesebbet nyomkövetést”.
    - Current: `így kevesebbet nyomkövetést kap`
    - Source: `We now automatically refuse many cookie banners so you can get tracked less and go back to distraction-free browsing.`
    - Suggest: `így kevesebb nyomkövetést kap`
    - “kevesebb” must be uninflected when modifying the accusative noun; “kevesebbet nyomkövetést” doubles the accusative marking.
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — A leftover verb makes the sentence ungrammatical.
    - Current: `akkor vegye kapcsolja ki a „Tanulás…” lehetőségeket`
    - Source: `Existing memories will be deleted. If you don’t want any new memories created, uncheck the options to “Learn from…” in { -smart-window-brand-name } settings.`
    - Suggest: `akkor kapcsolja ki a „Tanulás…” lehetőségeket`
    - “vegye” is stray editing residue before “kapcsolja ki”; two conflicting imperatives cannot stand together.
- `smartbar-placeholder-hint-1` — `browser/browser/aiWindow.ftl` — Indefinite verb form used with a definite object.
    - Current: `A @ használatával említhet meg a legutóbbi lapokat…`
    - Source: `Use @ to mention recent tabs…`
    - Suggest: `A @ használatával említheti meg a legutóbbi lapokat…`
    - “a legutóbbi lapokat” is a definite object, requiring the definite conjugation “említheti”.
- `identity-etsi` — `browser/browser/browser.ftl` — Misspelling of “rendeletben”.
    - Current: `Az (EU) 2024/1183 rendeleteben meghatározottak szerint.`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Az (EU) 2024/1183 rendeletben meghatározottak szerint.`
    - The inessive of “rendelet” is “rendeletben”; “rendeleteben” is not a valid form.
- `urlbar-result-dismissal-acknowledgment-market` — `browser/browser/browser.ftl` — Wrong definite article before a consonant-initial word.
    - Current: `Többé nem fogja látni az pénzpiaci javaslatokat.`
    - Source: `Thanks for your feedback. You won’t see market suggestions anymore.`
    - Suggest: `Többé nem fogja látni a pénzpiaci javaslatokat.`
    - “az” is only used before vowel-initial words; “pénzpiaci” begins with a consonant.
- `content-sharing-modal-no-shareable-links` — `browser/browser/contentSharing.ftl` — The heading is ungrammatical and does not convey “No shareable links included”.
    - Current: `Nincs tartalmaz megosztható hivatkozásokat`
    - Source: `heading: No shareable links included message: Only links to web content can be shared.`
    - Suggest: `Nem tartalmaz megosztható hivatkozásokat`
    - “Nincs tartalmaz” combines a negative existential with a finite verb and is not a valid Hungarian clause.
- `customize-mode-touchbar-cmd` — `browser/browser/customizeMode.ftl` — “Touch Bar” is misspelled as “Érintősár”.
    - Current: `Érintősár testreszabása…`
    - Source: `label: Customize Touch Bar…`
    - Suggest: `Érintősáv testreszabása…`
    - The intended word is “Érintősáv” (Touch Bar); “Érintősár” is a typo with no meaning.
- `genai-prompts-explain` — `browser/browser/genai.ftl` — Wrong verbal prefix in the prompt body: “Magyarázza le”.
    - Current: `Magyarázza le a kulcsfogalmakat a kijelölésben`
    - Source: `label: Explain this value: Please explain the key concepts in this selection, using simple words. Also, use examples.`
    - Suggest: `Magyarázza el a kulcsfogalmakat a kijelölésben`
    - “megmagyarázni/elmagyarázni” is the correct form; the label of the same message correctly uses “Magyarázza el”.
- `genai-settings-chat-claude-links` — `browser/browser/genai.ftl` — Last item of the enumeration is not in the accusative required by “elfogadja”.
    - Current: `és az <a data-l10n-name="link3">Adatvédelmi irányelvek</a>`
    - Source: `By choosing Anthropic Claude, you agree to the Anthropic <a data-l10n-name="link1">Consumer Terms of Service</a>, <a data-l10n-name="link2">Usage Policy</a>, and <a data-l10n-name="link3">Privacy Policy</a>.`
    - Suggest: `és az <a data-l10n-name="link3">Adatvédelmi irányelveit</a>`
    - The other two coordinated objects are accusative (“feltételeit”, “irányelveket”); the third one is left in the nominative.
- `ipprotection-feature-introduction-link-text-privacy-1` — `browser/browser/ipProtection.ftl` — The definite article is duplicated before the link text.
    - Current: `A <a data-l10n-name="learn-more-vpn">A { -brand-product-name } beépített VPN-je</a>`
    - Source: `<a data-l10n-name="learn-more-vpn">{ -brand-product-name }’s built-in VPN</a> helps protect your browsing. Choose from several locations to keep where you browse more private.`
    - Suggest: `<a data-l10n-name="learn-more-vpn">A { -brand-product-name } beépített VPN-je</a>`
    - The article appears both outside and inside the link, producing “A A Firefox beépített VPN-je”; the -2 variant of the same string has it only once.
- `newtab-wallpaper-remove-image-numbered` — `browser/browser/newtab/newtab.ftl` — Missing ordinal period after the number in the tooltip.
    - Current: `title: { $number } kép eltávolítása`
    - Source: `aria-label: Remove image { $number } title: Remove image { $number }`
    - Suggest: `title: { $number }. kép eltávolítása`
    - Same as the aria-label: Hungarian needs "{ $number }. kép" to mean "image N" rather than "N images".
- `newtab-wallpaper-remove-image-numbered` — `browser/browser/newtab/newtab.ftl` — Missing ordinal period after the number, inconsistent with the numbered-image string which uses "{ $number }. kép".
    - Current: `aria-label: { $number } kép eltávolítása`
    - Source: `aria-label: Remove image { $number } title: Remove image { $number }`
    - Suggest: `aria-label: { $number }. kép eltávolítása`
    - Hungarian ordinal numbering requires a period (as used in newtab-wallpaper-your-images-item-numbered: "{ $number }. kép"); without it the text reads as a count ("remove N images").
- `mr1-onboarding-theme-label-alpenglow` — `browser/browser/newtab/onboarding.ftl` — Theme name "Alpenglow" was translated although the developer comment forbids it.
    - Current: `Alpesi fény`
    - Source: `Alpenglow`
    - Suggest: `Alpenglow`
    - The dev comment states: "'Alpenglow' here is the name of the theme, and should be kept in English." The Hungarian renders it as a common noun, breaking the product name.
- `general-url` — `browser/browser/pageInfo.ftl` — “Address” and “Title” are both rendered “Cím:”, making two adjacent fields in the same panel indistinguishable.
    - Current: `Cím:`
    - Source: `value: Address:`
    - Suggest: `Webcím:`
    - general-title (“Title:”) is also “Cím:”. Elsewhere in the tree “URL/Address” is consistently “Webcím” (e.g. placesPrompts.ftl, reportBrokenSite.ftl), so the address row should use “Webcím:”.
- `maxTimersExceeded` — `devtools/shared/webconsole.properties` — console.time() timers called "óra" (clock) while every neighbouring string uses "időzítő".
    - Current: `maxTimersExceeded = Ezen az oldalon nem indítható el több óra.`
    - Source: `The maximum allowed number of timers in this page was exceeded.`
    - Suggest: `maxTimersExceeded = Ezen az oldalon nem indítható el több időzítő.`
    - Same defect as the client copy: the surrounding timer strings use "időzítő".
- `CSSContainerRuleSingleConditionWarning` — `dom/chrome/dom/dom.properties` — The do-not-translate identifier CSSContainerRule is misspelled as CSSSContainerRule twice.
    - Current: `A CSSSContainerRule.containerName és a CSSContainerRule.containerQuery nem támogat több feltételt. Használja helyette a CSSSContainerRule.conditions mezőt.`
    - Source: `CSSContainerRule.containerName and CSSContainerRule.containerQuery don’t support multiple conditions. Use CSSContainerRule.conditions instead.`
    - Suggest: `A CSSContainerRule.containerName és a CSSContainerRule.containerQuery nem támogat több feltételt. Használja helyette a CSSContainerRule.conditions mezőt.`
    - The comment says do not translate CSSContainerRule.containerName / .containerQuery / .conditions; a triple S makes the suggested API name non-existent for developers copying it.
- `MediaStreamTrackAudioSourceNodeCrossOrigin` — `dom/chrome/dom/dom.properties` — The API name MediaStreamTrack was replaced by MediaStream, although the developer comment says not to translate it.
    - Current: `A createMediaStreamTrackSource-nak átadott MediaStream egy cross-origin erőforrás`
    - Source: `The MediaStreamTrack passed to createMediaStreamTrackSource is a cross-origin resource, the node will output silence.`
    - Suggest: `A createMediaStreamTrackSource-nak átadott MediaStreamTrack egy cross-origin erőforrás`
    - en-US: “The MediaStreamTrack passed to createMediaStreamTrackSource is a cross-origin resource”. The note says “Do not translate MediaStreamTrack and createMediaStreamTrackSource”; the message now names a different interface than the one the error is about.
- `NavigationChangeFloodingPrevented` — `dom/chrome/dom/dom.properties` — Case agreement error: "navigálására" should be "navigálásra" in this construction.
    - Current: `túl sok kísérlet történt az előzményekben való navigálására vagy azok módosítására`
    - Source: `Too many attempts to navigate or modify history within a short timeframe.`
    - Suggest: `túl sok kísérlet történt az előzményekben való navigálásra vagy azok módosítására`
    - "kísérlet történt" requires the sublative -ra/-re without possessive suffix; "navigálására" has a stray possessive ending that does not agree with anything.
- `UseSendBeaconDuringUnloadAndPagehideWarning` — `dom/chrome/dom/dom.properties` — The do-not-translate event name “unload” is written as “unlode”, with a wrong article.
    - Current: `a unlode és pagehide folyamatokban`
    - Source: `Use of navigator.sendBeacon instead of synchronous XMLHttpRequest during unload and pagehide improves user experience.`
    - Suggest: `az unload és a pagehide folyamatokban`
    - The comment says do not translate unload or pagehide; “unlode” is not the event name, and Hungarian requires “az” before a vowel-initial word.
- `CSPEvalScriptViolation` — `dom/chrome/security/csp.properties` — The single quotes that are part of the CSP keyword 'unsafe-eval' were replaced by Hungarian quotation marks.
    - Current: `(hiányzó „unsafe-eval”)`
    - Source: `The page’s settings blocked a JavaScript eval (%2$S) from being executed because it violates the following directive: “%1$S” (Missing 'unsafe-eval')`
    - Suggest: `(hiányzó 'unsafe-eval')`
    - The comment says “Don't translate/change "'unsafe-eval'", including the single quote”; the quotes are part of the source-expression syntax the developer must type. Same change in CSPROEvalScriptViolation and the Wasm variants.
- `BlockFileScriptWithWrongMimeType` — `dom/chrome/security/security.properties` — The “file:” scheme is dropped and the quotation mark is placed inside the parenthesis.
    - Current: `Parancsfájl betöltése: az URI „(%1$S”) blokkolva lett`
    - Source: `Loading script from file: URI (“%1$S”) was blocked because its MIME type (“%2$S”) is not a valid JavaScript MIME type.`
    - Suggest: `A file: URI-ról („%1$S”) történő parancsfájl-betöltés blokkolva lett`
    - en-US: “Loading script from file: URI (“%1$S”) was blocked…”, with the note “Do not translate "file: URI"”. The scheme is missing and the quote/paren order is inverted.
- `BlockRedirectToDataURI` — `dom/chrome/security/security.properties` — The “data:” URI scheme was translated into “az adatokhoz:”, although the comment forbids translating it.
    - Current: `Átirányítás az adatokhoz: az URI-hoz navigálás nem engedélyezett`
    - Source: `Redirecting to data: URI not allowed (Blocked loading of: “%1$S”)`
    - Suggest: `Átirányítás a data: URI-ra nem engedélyezett`
    - en-US: “Redirecting to data: URI not allowed”, with the note “Do not translate "data: URI"”. The scheme name is lost and the sentence no longer parses.
- `CookieRejectedNonRequiresSecure2` — `netwerk/necko.properties` — The do-not-localize token SameSite=None is written with a lowercase “none”.
    - Current: `a „SameSite=none” attribútum lett megadva`
    - Source: `Cookie “%1$S” rejected because it has the “SameSite=None” attribute but is missing the “secure” attribute.`
    - Suggest: `a „SameSite=None” attribútum lett megadva`
    - The comment says do not localize “SameSite=None”; CookieSameSiteValueInvalid2 in the same file keeps the capitalised “None”.
- `SaveVideoTitle` — `toolkit/chrome/global/contentAreaCommands.properties` — "Videó" spelled without its accent.
    - Current: `SaveVideoTitle = Video mentése`
    - Source: `Save Video`
    - Suggest: `SaveVideoTitle = Videó mentése`
    - The standalone Hungarian noun is "videó" (cf. "Videó kipattintása" in videocontrols.ftl); the unaccented form only occurs as a compound prefix.
- `url-classifier-content-classifier-col-important` — `toolkit/toolkit/about/url-classifier.ftl` — "Important" is translated although the developer comment forbids translating it.
    - Current: `Fontos`
    - Source: `Important`
    - Suggest: `Important`
    - Developer comment: "'Important' should not be translated as it refers to technical syntax." It names the `important` filter-syntax option, so the localized "Fontos" no longer matches the syntax keyword it labels.
- `autofill-clear-form-label` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Adjective used where an adverb is required.
    - Current: `Automatikus kitöltött űrlap ürítése`
    - Source: `Clear Autofill Form`
    - Suggest: `Automatikusan kitöltött űrlap ürítése`
    - "Automatikus" cannot modify the participle "kitöltött"; the adverbial "automatikusan" is required.
- `wallet-custom-scheme-warning-heading` — `toolkit/toolkit/global/handlerDialog.ftl` — The heading has no verb, so it does not say what the site is being allowed to do.
    - Current: `Engedélyezi az oldal számára a digitális tárcáját?`
    - Source: `heading: Allow this site to open your digital wallet?`
    - Suggest: `Engedélyezi az oldal számára, hogy megnyissa a digitális tárcáját?`
    - en-US: "Allow this site to open your digital wallet?" All sibling permission-dialog strings in this file use the "…számára, hogy megnyissa…" pattern; here the verb is missing and the sentence is ungrammatical.
- `profiledowngrade-nosync` — `toolkit/toolkit/global/profileDowngrade.ftl` — Missing accusative ending on the object of "hozzon létre".
    - Current: `hozzon létre egy új profil a { -brand-short-name } ezen telepítéséhez`
    - Source: `Using an older version of { -brand-product-name } can corrupt bookmarks and browsing history already saved to an existing { -brand-product-name } profile. To protect your information, create a new profile for this insta…`
    - Suggest: `hozzon létre egy új profilt a { -brand-short-name } ezen telepítéséhez`
    - "létrehoz" takes a direct object; "profil" must be "profilt".
- `profiledowngrade-sync2` — `toolkit/toolkit/global/profileDowngrade.ftl` — Missing accusative ending on the object of "hozzon létre".
    - Current: `hozzon létre egy új profil a { -brand-short-name } ezen telepítéséhez`
    - Source: `Using an older version of { -brand-product-name } can corrupt bookmarks and browsing history already saved to an existing { -brand-product-name } profile. To protect your information, create a new profile for this insta…`
    - Suggest: `hozzon létre egy új profilt a { -brand-short-name } ezen telepítéséhez`
    - "létrehoz" takes a direct object; "profil" must be "profilt".
- `rosetta-translated-message` — `toolkit/toolkit/global/rosettaNotification.ftl` — A stray "s" left in the sentence.
    - Current: `A { -brand-short-name } s Rosettával fut`
    - Source: `{ -brand-short-name } is running using Rosetta, which can reduce performance and battery life.`
    - Suggest: `A { -brand-short-name } a Rosettával fut`
    - en-US: "{ -brand-short-name } is running using Rosetta". The isolated "s" is a typo and makes the sentence ungrammatical.
- `region-name-nr` — `toolkit/toolkit/intl/regionNames.ftl` — Country name written in lowercase.
    - Current: `region-name-nr = nauru`
    - Source: `Nauru`
    - Suggest: `region-name-nr = Nauru`
    - Every other region name in the file is capitalized, and Hungarian orthography capitalizes country names.
- `region-name-re` — `toolkit/toolkit/intl/regionNames.ftl` — Réunion is missing its accent.
    - Current: `region-name-re = Reunion`
    - Source: `Réunion`
    - Suggest: `region-name-re = Réunion`
    - en-US is "Réunion"; the Hungarian form also carries the accent, and other entries in the file keep diacritics (Curaçao, Saint Barthélemy).
- `region-name-ss` — `toolkit/toolkit/intl/regionNames.ftl` — "Dél-Szudán" is missing its hyphen.
    - Current: `region-name-ss = Dél Szudán`
    - Source: `South Sudan`
    - Suggest: `region-name-ss = Dél-Szudán`
    - Hungarian spells this compound country name with a hyphen, as the file itself does in "Dél-Afrikai Köztársaság" and "Dél-Korea".
- `region-name-st` — `toolkit/toolkit/intl/regionNames.ftl` — São Tomé és Príncipe is written without any of its diacritics.
    - Current: `region-name-st = Sao Tome és Principe`
    - Source: `São Tomé and Príncipe`
    - Suggest: `region-name-st = São Tomé és Príncipe`
    - en-US: "São Tomé and Príncipe"; other entries in the same file preserve diacritics.
- `sec-error-bad-nickname` — `toolkit/toolkit/neterror/nsserrors.ftl` — The article "A" was typed as the conjunction "Ha", turning the sentence into a dangling conditional.
    - Current: `Ha tanúsítvány neve már használatban van.`
    - Source: `Certificate nickname already in use.`
    - Suggest: `A tanúsítvány neve már használatban van.`
    - en-US: "Certificate nickname already in use." There is no conditional in the source and the clause has no main clause.
- `sec-error-old-krl` — `toolkit/toolkit/neterror/nsserrors.ftl` — Wrong definite article before a consonant and missing comma before "mint".
    - Current: `Az KRL régebbi mint a jelenlegi.`
    - Source: `New KRL is not later than the current one.`
    - Suggest: `Az új KRL nem újabb, mint a jelenlegi.`
    - "KRL" is pronounced with a consonant, so it takes "a", not "az"; Hungarian also requires a comma before "mint". en-US: "New KRL is not later than the current one."
- `ssl-error-bad-cert-status-response-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — Misspelling of "partner".
    - Current: `Az SSL-patner nem kapott OCSP-választ a tanúsítványára.`
    - Source: `SSL peer was unable to get an OCSP response for its certificate.`
    - Suggest: `Az SSL-partner nem kapott OCSP-választ a tanúsítványára.`
    - Every neighbouring string spells it "SSL-partner".
- `ssl-error-internal-error-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — Verb typo: "jelet" instead of "jelez".
    - Current: `A partner saját belső hibát jelet.`
    - Source: `Peer reports it experienced an internal error.`
    - Suggest: `A partner saját belső hibát jelez.`
    - en-US: "Peer reports it experienced an internal error." "jelet" is the accusative of the noun "jel", leaving the sentence verbless.
- `ssl-error-ssl2-disabled` — `toolkit/toolkit/neterror/nsserrors.ftl` — Subject carries an accusative ending, making the sentence ungrammatical.
    - Current: `A partnert csak az SSL 2-es verzióját támogatja`
    - Source: `Peer only supports SSL version 2, which is locally disabled.`
    - Suggest: `A partner csak az SSL 2-es verzióját támogatja`
    - en-US: "Peer only supports SSL version 2, which is locally disabled." "A partnert" is the object form of the subject.

### D. Terminology, register & consistency

- `aiwindow-applied-memories-list` — `browser/browser/aiWindowContent.ftl` — “Memories” is translated as “Emlékek” here while the rest of the feature uses “Memóriák”.
    - Current: `Emlékek`
    - Source: `aria-label: Memories`
    - Suggest: `Memóriák`
    - Every other Memories string in aiWindow.ftl, aiWindowContent.ftl and aiFeatures.ftl uses “Memóriák”, including the sibling popover label in the same block.
- `confirmation-hint-pin-tab-description` — `browser/browser/confirmationHints.ftl` — “tab” rendered as “fül” although the tree consistently uses “lap”.
    - Current: `kattintson a fülre jobb egérgombbal`
    - Source: `Right-click the tab to unpin it.`
    - Suggest: `kattintson a lapra jobb egérgombbal`
    - Every other tab-related string in this partition uses “lap”; “fül” is an isolated inconsistency in the same UI surface.
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — Keyboard “key” is translated as “kulcs” (cryptographic/lock key) instead of “billentyű”.
    - Current: `A kulcs nem használható`
    - Source: `Key cannot be used`
    - Suggest: `A billentyű nem használható`
    - The whole file is about keyboard shortcuts and elsewhere uses “billentyű” (customkeys-new-key: “Nyomja meg az új billentyűt”); “kulcs” names the wrong object.
- `splitview-onboarding-callout-subtitle-1` — `browser/browser/featureCallout.ftl` — `splitview-onboarding-callout-subtitle-1` quotes “Hozzáadás osztott nézethez” but the string it names, `customkeys-view-add-split-view`, reads “Osztott nézet hozzáadása”
    - Current: `Kattintson jobb gombbal erre a lapra, és válassza a „Hozzáadás osztott nézethez” lehetőséget, hogy egyszerre két lapot lásson.`
    - Source: `Right-click this tab and choose “Add Split View” to see two tabs at once.`
    - Suggest: `Osztott nézet hozzáadása`
    - In the source this string quotes “Add Split View”, which is exactly the value of `customkeys-view-add-split-view` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `menu-application-hide-other` — `browser/browser/menubar.ftl` — “A több elrejtése” is not grammatical; the pronoun for “others” is “a többi”.
    - Current: `A több elrejtése`
    - Source: `label: Hide Others`
    - Suggest: `A többi elrejtése`
    - en-US “Hide Others”. “több” means “more”; the correct pronoun is “többi”.
- `menu-application-touch-bar` — `browser/browser/menubar.ftl` — Typo: “Érintősár” instead of “Érintősáv” (Touch Bar).
    - Current: `Érintősár testreszabása…`
    - Source: `label: Customize Touch Bar…`
    - Suggest: `Érintősáv testreszabása…`
    - “sár” means mud; the intended word is “sáv” (bar).
- `migration-chrome-windows-password-import-step1` — `browser/browser/migrationWizard.ftl` — Wrong definite article before a vowel-initial word.
    - Current: `és ugorjon a Automatikus kitöltés és jelszavak`
    - Source: `Open the main menu <img data-l10n-name="chrome-icon-3dots"/> and go to Passwords and Autofill > Google Password Manager.`
    - Suggest: `és ugorjon az Automatikus kitöltés és jelszavak`
    - “a” must become “az” before a word starting with a vowel.
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — Thousands written with a period, which is the decimal separator in Hungarian.
    - Current: `átlagosan 3.000 nyomkövetőt`
    - Source: `Every month, { -brand-short-name } blocks an average of over 3,000 trackers per user. Because nothing, especially privacy nuisances like trackers, should stand between you and the good internet.`
    - Suggest: `átlagosan 3000 nyomkövetőt`
    - Hungarian uses no separator for four-digit numbers (or a space), and the period marks decimals, so "3.000" reads as three; july-jam-body in the same file correctly writes "3000".
- `home-prefs-mission-message-learn-more-link-srd` — `browser/browser/newtab/newtab.ftl` — Missing comma before the subordinate clause.
    - Current: `Tudja meg hogyan`
    - Source: `Find out how`
    - Suggest: `Tudja meg, hogyan`
    - Hungarian requires a comma before a subordinating conjunction; the same file writes "Tudja meg, hogyan működik…" (newtab-privacy-modal-link).
- `newtab-widget-section-feedback` — `browser/browser/newtab/newtab.ftl` — Missing comma before the subordinate clause.
    - Current: `Mondja el nekünk mit gondol`
    - Source: `Tell us what you think`
    - Suggest: `Mondja el nekünk, mit gondol`
    - A comma is obligatory before the embedded question "mit gondol".
- `fx-backup-opt-in-filepath-label` — `browser/browser/newtab/onboarding.ftl` — Wrong vowel-harmony suffix on "OneDrive".
    - Current: `például a OneDrive-re`
    - Source: `Pick a place you plan to transfer to a new device, like OneDrive.`
    - Suggest: `például a OneDrive-ra`
    - "Drive" is pronounced with a back vowel in Hungarian, so it takes -ra; create-backup-screen-1-backup-body in the same file correctly writes "OneDrive-ra".
- `onboarding-genai-sidebar-subtitle` — `browser/browser/newtab/onboarding.ftl` — Ungrammatical, garbled rendering of "draft messages".
    - Current: `írjon összes piszkozatokat`
    - Source: `Summarize web content, brainstorm ideas, draft messages — all as you browse. Choose from multiple providers. Switch anytime. <a data-l10n-name="learn-more">Learn more</a>`
    - Suggest: `írjon üzenetpiszkozatokat`
    - "összes piszkozatokat" is not grammatical Hungarian (mismatched quantifier and plural accusative) and does not convey "draft messages".
- `onboarding-sign-up-description` — `browser/browser/newtab/onboarding.ftl` — Misspelling of "egyebek".
    - Current: `egyeket`
    - Source: `Sign up for an account and all of your important info — passwords, bookmarks, and more — will be securely stored and available when you sign in to any device.`
    - Suggest: `egyebek`
    - "egyeket" is not a word; the intended form in the list "jelszavak, könyvjelzők és egyebek" is "egyebek".
- `managed-bookmarks` — `browser/browser/places.ftl` — Verb stem used instead of the participle: “Menedzsel könyvjelzők”.
    - Current: `Menedzsel könyvjelzők`
    - Source: `label: Managed bookmarks`
    - Suggest: `Felügyelt könyvjelzők`
    - en-US “Managed bookmarks”; “menedzsel” is a finite verb form and cannot modify a noun. A participle (e.g. “felügyelt” / “menedzselt”) is required.
- `policy-DisablePasswordReveal` — `browser/browser/policies/policies-descriptions.ftl` — Misspelling: "mentet" instead of "mentett".
    - Current: `a mentet bejelentkezésekben`
    - Source: `Do not allow passwords to be revealed in saved logins.`
    - Suggest: `a mentett bejelentkezésekben`
    - Past participle of "ment" is "mentett" with a double t; "mentet" is a different (causative) form.
- `policy-EnableTrackingProtection` — `browser/browser/policies/policies-descriptions.ftl` — Misspelling: "válaszható" instead of "választható".
    - Current: `válaszható módon`
    - Source: `Enable or disable Content Blocking and optionally lock it.`
    - Suggest: `választható módon`
    - The word for "optionally" is "választható" (from választ); "válaszható" is a typo, cf. policy-Homepage which spells it correctly.
- `policy-EncryptedMediaExtensions` — `browser/browser/policies/policies-descriptions.ftl` — Misspelling: "válaszható" instead of "választható".
    - Current: `válaszható módon`
    - Source: `Enable or disable Encrypted Media Extensions and optionally lock it.`
    - Suggest: `választható módon`
    - Same typo as in policy-EnableTrackingProtection; policy-Homepage spells it "választható".
- `policy-OverrideFirstRunPage` — `browser/browser/policies/policies-descriptions.ftl` — Duplicated article "a az".
    - Current: `ha le akarja tiltani a az első indítás oldalt`
    - Source: `Override the first run page. Set this policy to blank if you want to disable the first run page.`
    - Suggest: `ha le akarja tiltani az első indítás oldalt`
    - Two stacked definite articles; only "az" belongs before "első".
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — Missing case suffix makes the sentence ungrammatical.
    - Current: `Állítsa üres ezt a házirendet`
    - Source: `Override the post-update “What’s New” page. Set this policy to blank if you want to disable the post-update page.`
    - Suggest: `Állítsa üresre ezt a házirendet`
    - "Állít" requires the sublative -re on the resulting state; cf. the parallel policy-OverrideFirstRunPage which uses "Állítsa üres értékre".
- `containers-site-invalid-error` — `browser/browser/preferences/containers.ftl` — "website" rendered as "weboldalt" while the surrounding container strings consistently use "webhely".
    - Current: `Adjon meg egy érvényes, biztonságos weboldalt`
    - Source: `Enter a valid, secure website`
    - Suggest: `Adjon meg egy érvényes, biztonságos webhelyet`
    - The same en-US term "website" is translated "webhely" in containers-site-label, containers-site-window and containers-site-duplicate-error; this string breaks that consistency.
- `browser-language-heading` — `browser/browser/preferences/preferences.ftl` — Misspelling "menüijeinek".
    - Current: `menüijeinek`
    - Source: `description: Choose the language used to display menus, messages, and notifications from { -brand-short-name }. label: Browser language`
    - Suggest: `menüinek`
    - The possessive plural of "menü" is "menüinek"; "menüijeinek" is not a word.
- `preferences-data-migration-group` — `browser/browser/preferences/preferences.ftl` — Verb misspelled: "Hozzá át" instead of "Hozza át".
    - Current: `Hozzá át a könyvjelzőit`
    - Source: `description: Bring your bookmarks, passwords, history, extensions, and autofill data from another browser. label: Import browser data`
    - Suggest: `Hozza át a könyvjelzőit`
    - "Hozzá" is not an imperative form; the imperative of "hoz" is "hozza". Visible in the Import browser data group description.
- `preferences-doh-description2` — `browser/browser/preferences/preferences.ftl` — "lássak" (1sg) should be "lássák" (3pl).
    - Current: `hogy lássak, hogy melyik weboldalakat éri el`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access.`
    - Suggest: `hogy lássák, hogy mely weboldalakat éri el`
    - The subject is "mások" (others), so the verb must be third person plural "lássák".
- `privacy-segmentation-section-description` — `browser/browser/preferences/preferences.ftl` — Number agreement: plural subject with singular verb.
    - Current: `amelyek az Ön adatait használja`
    - Source: `When we offer features that use your data to give you a more personal experience:`
    - Suggest: `amelyek az Ön adatait használják`
    - The relative pronoun "amelyek" is plural (referring to "funkciókat"), so the verb must be "használják".
- `search-results-empty-message2` — `browser/browser/preferences/preferences.ftl` — "Elnézését" should be "Elnézést".
    - Current: `Elnézését, nincs találat`
    - Source: `Sorry! There are no results in Settings for “<span data-l10n-name="query"></span>”.`
    - Suggest: `Elnézést, nincs találat`
    - The fixed apologetic phrase is "Elnézést"; "Elnézését" (a possessive accusative) is ungrammatical here.
- `security-privacy-status-update-needed-description` — `browser/browser/preferences/preferences.ftl` — Typo "sebességbelii".
    - Current: `sebességbelii`
    - Source: `Update for the latest speed, stability, and security updates.`
    - Suggest: `sebességbeli`
    - Doubled final "i"; the correct adjective is "sebességbeli".
- `settings-tabs-show-image-in-preview` — `browser/browser/preferences/preferences.ftl` — "fülé" should be "fölé" (over/above).
    - Current: `ha az egérmutatót egy lap fülé húzza`
    - Source: `accessKey: h label: Show an image preview when you hover on a tab`
    - Suggest: `ha az egérmutatót egy lap fölé húzza`
    - en-US: "when you hover on a tab". "fülé" means "to his/her ear"; the postposition meaning "over" is "fölé".
- `sitedata-delete-on-close-private-browsing4` — `browser/browser/preferences/preferences.ftl` — Wrong definite article "az" before a consonant-initial word.
    - Current: `törli a sütiket és az webhelyadatokat`
    - Source: `heading: History won’t be saved. message: { -brand-short-name } clears cookies and site data from your session when you close the browser.`
    - Suggest: `törli a sütiket és a webhelyadatokat`
    - "webhelyadatokat" starts with a consonant, so the article must be "a", not "az".
- `update-setting-write-failure-message2` — `browser/browser/preferences/preferences.ftl` — "szükségesen" should be the predicate "szükséges".
    - Current: `írási engedély szükségesen a lenti fájlon`
    - Source: `{ -brand-short-name } encountered an error and didn’t save this change. Note that changing this update setting requires permission to write to the file below. You or a system administrator may be able to resolve the err…`
    - Suggest: `írási engedély szükséges a lenti fájlra`
    - en-US: "requires permission to write to the file below". "szükségesen" is an adverb and makes the clause ungrammatical.
- `site-data-settings-description` — `browser/browser/preferences/siteDataSettings.ftl` — Missing accusative ending on "oldaladatok".
    - Current: `tárolnak sütiket és oldaladatok a számítógépén`
    - Source: `The following websites store cookies and site data on your computer. { -brand-short-name } keeps data from websites with persistent storage until you delete it, and deletes data from websites with non-persistent storage…`
    - Suggest: `tárolnak sütiket és oldaladatokat a számítógépén`
    - The object of "tárolnak" must be accusative: "oldaladatokat", matching the preceding "sütiket".
- `preonboarding-manage-and-read-header` — `browser/browser/preonboarding.ftl` — Case mismatch between the two coordinated objects of “elolvasása”.
    - Current: `a felhasználási feltételeinket és az adatvédelmi nyilatkozat elolvasása`
    - Source: `Manage data collection settings and read our Terms of Use and Privacy Notice`
    - Suggest: `a felhasználási feltételeink és az adatvédelmi nyilatkozat elolvasása`
    - With the possessive noun phrase “… elolvasása”, both coordinated members must be nominative; “feltételeinket” is accusative and does not agree with “nyilatkozat”.
- `preonboarding-privacy-notice-header-button-title` — `browser/browser/preonboarding.ftl` — “felolvasása” means “reading aloud”, not “reading”.
    - Current: `Adatvédelmi nyilatkozat felolvasása`
    - Source: `Read our Privacy Notice`
    - Suggest: `Adatvédelmi nyilatkozat elolvasása`
    - en-US “Read our Privacy Notice”; the parallel button preonboarding-terms-of-use-header-button-title correctly uses “elolvasása”.
- `fingerprinter-tab-content` — `browser/browser/protections.ftl` — Wrong definite article (“A” before a vowel) and missing accusative on “Ön”.
    - Current: `A ujjlenyomat-készítők beállításokat gyűjtenek a böngészőjéből és számítógépéből, hogy profilt hozzanak létre Önről. A digitális ujjlenyomat használatával követhetik Ön a különböző webhelyek között.`
    - Source: `Fingerprinters collect settings from your browser and computer to create a profile of you. Using this digital fingerprint, they can track you across different websites. <a data-l10n-name="learn-more-link">Learn more</a>`
    - Suggest: `Az ujjlenyomat-készítők beállításokat gyűjtenek a böngészőjéből és számítógépéből, hogy profilt hozzanak létre Önről. A digitális ujjlenyomat használatával követhetik Önt a különböző webhelyek között.`
    - “A” must be “az” before a vowel-initial word, and the object of “követhetik” requires the accusative “Önt”.
- `graph-week-summary-private-window` — `browser/browser/protections.ftl` — Relative pronoun does not agree in number with the plural antecedent.
    - Current: `Követők, melyet a { -brand-short-name } blokkolt a héten`
    - Source: `Trackers { -brand-short-name } blocked this week`
    - Suggest: `Követők, amelyeket a { -brand-short-name } blokkolt a héten`
    - “Követők” is plural, so the accusative relative pronoun must be “amelyeket/melyeket”.
- `monitor-partial-breaches-motivation-description` — `browser/browser/protections.ftl` — Sentence ends with a bare brand term missing its case suffix, so it is ungrammatical.
    - Current: `Oldja meg a többi adatvédelmi incidenst a { -monitor-brand-short-name }.`
    - Source: `Resolve the rest of your breaches on { -monitor-brand-short-name }.`
    - Suggest: `Oldja meg a többi adatvédelmi incidenst a { -monitor-brand-short-name }on.`
    - en-US “Resolve the rest of your breaches on { -monitor-brand-short-name }.”; every other string in this file attaches “on” to the brand term (e.g. monitor-resolve-breaches-link tooltip).
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — Missing accusative: “követik Ön” instead of “követik Önt”.
    - Current: `Ezek a sütik követik Ön oldalról oldalra`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
    - Suggest: `Ezek a sütik követik Önt oldalról oldalra`
    - The direct object of “követik” must be in the accusative.
- `protections-panel-fingerprinters` — `browser/browser/protectionsPanel.ftl` — Wrong definite article (“A” before a vowel) and missing accusative on “Ön”.
    - Current: `A ujjlenyomat-készítők beállításokat gyűjtenek a böngészőjéből és számítógépéből, hogy profilt hozzanak létre Önről. A digitális ujjlenyomat használatával követhetik Ön a különböző webhelyek között.`
    - Source: `Fingerprinters collect settings from your browser and computer to create a profile of you. Using this digital fingerprint, they can track you across different websites.`
    - Suggest: `Az ujjlenyomat-készítők beállításokat gyűjtenek a böngészőjéből és számítógépéből, hogy profilt hozzanak létre Önről. A digitális ujjlenyomat használatával követhetik Önt a különböző webhelyek között.`
    - Same two errors as in protections.ftl: “az” is required before a vowel, and “követhetik” takes the accusative “Önt”.
- `report-broken-site-panel-description2` — `browser/browser/reportBrokenSite.ftl` — Indefinite conjugation used with a definite object: “Adjon meg a lépéseket”.
    - Current: `Adjon meg a lépéseket a probléma reprodukálásához.`
    - Source: `placeholder: What happened? What did you expect to happen? Please provide steps to reproduce the issue.`
    - Suggest: `Adja meg a lépéseket a probléma reprodukálásához.`
    - “a lépéseket” is a definite object, so the verb must take the definite conjugation “adja meg”.
- `safeb-blocked-harmful-page-error-desc-no-override` — `browser/browser/safebrowsing/blockedSite.ftl` — Missing accusative ending (and missing space) before the link: “oldal” should be “oldalt”.
    - Current: `oldal<a data-l10n-name='error_desc_link'>ártalmas szoftvert tartalmazóként jelentették</a>`
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing a potentially harmful application</a>.`
    - Suggest: `oldalt <a data-l10n-name='error_desc_link'>ártalmas szoftvert tartalmazóként jelentették</a>`
    - Same defect as the -override variant: “jelentették” requires the accusative “oldalt”, and the noun is glued to the opening link tag.
- `safeb-blocked-harmful-page-error-desc-override` — `browser/browser/safebrowsing/blockedSite.ftl` — Missing accusative ending (and missing space) before the link: “oldal” should be “oldalt”.
    - Current: `oldal<a data-l10n-name='error_desc_link'>ártalmas szoftvert tartalmazóként jelentették</a>`
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing a potentially harmful application</a>. You can <a data-l10n-name='ignore_warning_link'>ignore the…`
    - Suggest: `oldalt <a data-l10n-name='error_desc_link'>ártalmas szoftvert tartalmazóként jelentették</a>`
    - “jelentették” takes an accusative object, so it must be “oldalt”, as in the parallel phishing strings (“A(z) … oldalt … megtévesztő oldalként jelentették”). The word also runs into the link with no space.
- `protections-not-blocking-fingerprinters` — `browser/browser/siteProtections.ftl` — Compound misspelled with a plural first member: “ujjlenyomatok-készítőket”.
    - Current: `Nem blokkolja az ujjlenyomatok-készítőket`
    - Source: `title: Not Blocking Fingerprinters`
    - Suggest: `Nem blokkolja az ujjlenyomat-készítőket`
    - Everywhere else in this file and in protections.ftl the term is “ujjlenyomat-készítő”; the first element of the compound must be singular.
- `tab-groups-list-empty-description` — `browser/browser/tabbrowser.ftl` — Missing accusative ending on the object of “Húzzon”.
    - Current: `Húzzon egy lap egy másikra`
    - Source: `Drag one tab onto another or right-click a tab to start organizing. We’ll save your groups here so they’re easy to find later.`
    - Suggest: `Húzzon egy lapot egy másikra`
    - en-US “Drag one tab onto another”; the object requires the accusative “lapot”.
- `existing-user-tou-message` — `browser/browser/termsofuse.ftl` — Object of “frissítettük” is left in the nominative instead of the accusative.
    - Current: `frissítettük az <a data-l10n-name="privacy-notice-link">Adatvédelmi nyilatkozat</a>`
    - Source: `<strong>Update</strong> We’ve introduced a { -brand-short-name } <a data-l10n-name="terms-of-use-link">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice-link">Privacy Notice</a>. Please take a moment to…`
    - Suggest: `frissítettük az <a data-l10n-name="privacy-notice-link">Adatvédelmi nyilatkozatot</a>`
    - The sibling string existing-user-privacy-notice-update-message correctly uses the accusative “Adatvédelmi nyilatkozatot”.
- `unblockInsecure2` — `browser/chrome/browser/downloads/downloads.properties` — Case-agreement error: accusative subject with a passive predicate.
    - Current: `annak ellenére, hogy az aktuális dokumentumot biztonságos HTTPS-kapcsolaton keresztül lett kézbesítve`
    - Source: `The download is offered over HTTP even though the current document was delivered over a secure HTTPS connection. If you proceed, the download may be corrupted or tampered with during the download process.`
    - Suggest: `annak ellenére, hogy az aktuális dokumentum biztonságos HTTPS-kapcsolaton keresztül lett kézbesítve`
    - “az aktuális dokumentumot” is accusative but “lett kézbesítve” requires a nominative subject; the clause is ungrammatical.
- `CONTEXT_OPTIONS` — `browser/installer/custom.properties` — "Options" rendered as a verbal noun "setting it up" instead of the settings noun.
    - Current: `$BrandShortName &beállítása`
    - Source: `$BrandShortName &Options`
    - Suggest: `$BrandShortName &beállításai`
    - This is a shortcut context-menu entry naming the Options/Settings screen; "beállítása" reads as the act of configuring it, while the UI item is "beállításai".
- `accessibility-text-label-issue-dialog` — `devtools/client/accessibility.ftl` — Spelling error: "párbeszablakokat" instead of "párbeszédablakokat".
    - Current: `A párbeszablakokat címkézni kell.`
    - Source: `Dialogs should be labeled. <a>Learn more</a>`
    - Suggest: `A párbeszédablakokat címkézni kell.`
    - The same message in devtools/shared/accessibility.properties (accessibility.text.label.issue.dialog) is spelled "párbeszédablakokat".
- `accessibility.enable.disabledTitle` — `devtools/client/accessibility.properties` — Truncated word: "akadálymentesít szolgáltatások" is missing its ending.
    - Current: `az akadálymentesít szolgáltatások adatvédelmi beállításán keresztül`
    - Source: `Accessibility service can not be turned on. It is turned off via accessibility services privacy preference.`
    - Suggest: `az akadálymentesítési szolgáltatások adatvédelmi beállításán keresztül`
    - "akadálymentesít" is a verb form; the noun modifier used consistently elsewhere in this file is "akadálymentesítési".
- `timeline.pausedButtonTooltip` — `devtools/client/animationinspector.properties` — Missing space between the two words: "Animációkfolytatása".
    - Current: `timeline.pausedButtonTooltip = Animációkfolytatása`
    - Source: `Resume the animations`
    - Suggest: `timeline.pausedButtonTooltip = Animációk folytatása`
    - Two words are run together; the parallel strings (timeline.resumedButtonTooltip, timeline.rewindButtonTooltip) are correctly spaced.
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “Töréspont…” but the string it names, `watchpoints.submenu`, reads “Szüneteltetés…”
    - Current: `Kattintson a jobb gombbal egy elemre a Vizsgálóban, és válassza a „Töréspont…” lehetőséget`
    - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
    - Suggest: `Szüneteltetés…`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `emptyPresetList` — `devtools/client/filterwidget.properties` — Typo: "előbeállítáokat" is missing an "s".
    - Current: `Tárolhat szűrő-előbeállítáokat`
    - Source: `You don’t have any saved presets. You can store filter presets by choosing a name and saving them. Presets are quickly accessible and you can reuse them with ease.`
    - Suggest: `Tárolhat szűrő-előbeállításokat`
    - The correct accusative plural is "előbeállításokat", as used in presetsToggleButton/newPresetPlaceholder.
- `markupView.scrollableBadge.interactive.tooltip` — `devtools/client/inspector.properties` — Case agreement error: "azokat az elemek" instead of "azokat az elemeket".
    - Current: `hogy felfedje azokat az elemek, melyek a túlcsordulást okozzák`
    - Source: `This element has scrollable overflow. Click to reveal elements that are causing the overflow.`
    - Suggest: `hogy felfedje azokat az elemeket, amelyek a túlcsordulást okozzák`
    - The object of "felfedje" must be accusative; the demonstrative is accusative but the noun is not.
- `responsive.reloadConditions.userAgent` — `devtools/client/responsive.properties` — Missing adjectival suffix: "felhasználó ügynök" instead of "felhasználói ügynök".
    - Current: `responsive.reloadConditions.userAgent = Újratöltés, ha a felhasználó ügynök megváltozik`
    - Source: `Reload when user agent is changed`
    - Suggest: `responsive.reloadConditions.userAgent = Újratöltés, ha a felhasználói ügynök megváltozik`
    - The rest of the file uses "felhasználói ügynök" (responsive.customUserAgent, responsive.userAgentList); "felhasználó ügynök" is ungrammatical.
- `inactive-css-border-image` — `devtools/client/tooltips.ftl` — The sentence ends with a dangling, uninflected "szülő táblázatelem", losing the "on the parent table element" relation.
    - Current: `<strong>collapse</strong> értékre van állítva szülő táblázatelem.`
    - Source: `<strong>{ $property }</strong> has no effect on this element since it cannot be applied to internal table elements where <strong>border-collapse</strong> is set to <strong>collapse</strong> on the parent table element.`
    - Suggest: `<strong>collapse</strong> értékre van állítva a szülő táblázatelemen.`
    - en-US: "…where border-collapse is set to collapse on the parent table element"; the Hungarian leaves the noun phrase unattached and unmarked.
- `inactive-text-overflow-when-no-overflow` — `devtools/client/tooltips.ftl` — Ungrammatical clause: "mivel nem megadva az overflow:hidden".
    - Current: `mivel nem megadva az <strong>overflow:hidden</strong>`
    - Source: `<strong>{ $property }</strong> has no effect on this element since <strong>overflow:hidden</strong> is not set.`
    - Suggest: `mivel nincs megadva az <strong>overflow:hidden</strong>`
    - "nem megadva" is not a valid predicate here; the negated existential form is "nincs megadva".
- `screenshotFileManual` — `devtools/shared/screenshot.properties` — Broken clause: the subject "a képernyőkép" is paired with "mentse a fájlt".
    - Current: `Igaz, ha a képernyőkép akkor is mentse a fájlt, ha más beállítások is be vannak kapcsolva`
    - Source: `True if the screenshot should save the file even when other options are enabled (eg. clipboard).`
    - Suggest: `Igaz, ha a képernyőképet fájlba is menteni kell, akkor is, ha más beállítások be vannak kapcsolva`
    - The nominative subject cannot govern the subjunctive "mentse" with the accusative object "a fájlt"; the sentence is ungrammatical as written.
- `errNonSpaceAfterBody` — `dom/chrome/layout/htmlparser.properties` — Spelling error: “tözs” instead of “törzs”.
    - Current: `Nem szóköz karakter a tözs után.`
    - Source: `Non-space character after body.`
    - Suggest: `Nem szóköz karakter a törzs után.`
    - “tözs” is not a Hungarian word; the intended word for “body” is “törzs”.
- `CORSDisabled` — `dom/chrome/security/security.properties` — The reason marker “Ok:” is truncated to “O:”.
    - Current: `(O: a CORS kikapcsolva)`
    - Source: `Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at %1$S. (Reason: CORS disabled).`
    - Suggest: `(Ok: a CORS kikapcsolva)`
    - All the other CORS* strings in this file use “(Ok: …)” for en-US “(Reason: …)”; this one lost the “k”.
- `CookieRejectedAttributeExpiryOversize` — `netwerk/necko.properties` — Wrong definite article “az” before the consonant-initial word “lejáratidátum-attribútuma”.
    - Current: `mert az lejáratidátum-attribútuma túl nagy`
    - Source: `Cookie “%1$S” has been rejected because its expiration date is over the limit.`
    - Suggest: `mert a lejáratidátum-attribútuma túl nagy`
    - Hungarian uses “a” before a consonant; “az lejárat…” is ungrammatical.
- `SEC_ERROR_BAD_NICKNAME` — `security/manager/chrome/pipnss/nsserrors.properties` — The sentence starts with the conjunction “Ha” (if) instead of the article “A”.
    - Current: `Ha tanúsítvány neve már használatban van.`
    - Source: `Certificate nickname already in use.`
    - Suggest: `A tanúsítvány neve már használatban van.`
    - en-US: “Certificate nickname already in use.” As written the string is a dangling conditional clause, not a statement.
- `SEC_ERROR_OLD_KRL` — `security/manager/chrome/pipnss/nsserrors.properties` — Wrong article “Az” before “KRL”, and the “new” KRL is not identified.
    - Current: `Az KRL régebbi mint a jelenlegi.`
    - Source: `New KRL is not later than the current one.`
    - Suggest: `Az új KRL nem újabb, mint a jelenlegi.`
    - en-US: “New KRL is not later than the current one.” Hungarian uses “a” before the consonant-initial “KRL”, and the sentence needs a comma before “mint”.
- _…and 13 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `newtab-sports-widget-message-wallpapers-semifinals-body` — `browser/browser/newtab/newtab.ftl` — Informal second-person imperative in a file that consistently uses the formal address.
    - Current: `Készítsd elő a színteret a világbajnokság legnagyobb mérkőzéseire!`
    - Source: `Set the stage for the World Cup’s biggest matches.`
    - Suggest: `Készítse elő a színteret a világbajnokság legnagyobb mérkőzéseire.`
    - Every other imperative in this file uses the formal Ön form (e.g. "Válassza", "Kövesse", "Vigyen"); "Készítsd" is the informal te form.
- `onboarding-refresh-terms-of-use-with-links` — `browser/browser/newtab/onboarding.ftl` — Stray space before the closing anchor tag creates a space before the period in the rendered sentence.
    - Current: `Adatvédelmi nyilatkozatunkat </a>.`
    - Source: `By continuing, you agree to the <a data-l10n-name="terms_of_use">{ -brand-product-name } Terms of Use</a> and our <a data-l10n-name="privacy_notice">Privacy Notice</a>. To help improve the browser, { -brand-product-name…`
    - Suggest: `Adatvédelmi nyilatkozatunkat</a>.`
    - The en-US has no space before </a>; the extra space produces "nyilatkozatunkat ." visually in the link text/punctuation boundary.
- `fonts-langgroup-latin` — `browser/browser/preferences/fonts.ftl` — Script name lowercased while every other entry in the list is capitalized.
    - Current: `latin`
    - Source: `label: Latin`
    - Suggest: `Latin`
    - All sibling labels in the same dropdown (Arab, Örmény, Cirill, Görög…) start with a capital letter; only this one does not.
- `permissions-site-local-network-window` — `browser/browser/preferences/permissions.ftl` — Missing space after the en dash in the window title.
    - Current: `Beállítások –Helyi hálózati eszközök`
    - Source: `style: { permissions-window2.style } title: Settings - Local Network Devices`
    - Suggest: `Beállítások – Helyi hálózati eszközök`
    - Every other title in this file uses "Beállítások – X" with spaces on both sides of the dash.
- `privacy-segmentation-radio-off` — `browser/browser/preferences/preferences.ftl` — Missing space between the article and the brand placeholder.
    - Current: `A{ -brand-product-name } javaslatainak használata`
    - Source: `label: Use { -brand-product-name } recommendations`
    - Suggest: `A { -brand-product-name } javaslatainak használata`
    - Renders as "AFirefox javaslatainak használata"; every other string in the file separates the article from the term with a space.
- `fxa-menu-signed-out-description` — `browser/browser/sync.ftl` — A sentence-final period was added where the en-US short status line has none.
    - Current: `Ön kijelentkezett.`
    - Source: `You’re signed out`
    - Suggest: `Ön kijelentkezett`
    - The source "You’re signed out" has no terminal punctuation; this is a short card/menu status label.
- `keywordURIFixup.goTo` — `browser/chrome/browser/browser.properties` — Informal second-person address in a UI button, breaking the locale's formal register.
    - Current: `Igen, vigyél ide: %S`
    - Source: `Yes, take me to %S`
    - Suggest: `Igen, vigyen ide: %S`
    - Everything else in this file and the tree addresses the user formally (Ön / “Engedélyezi…”, “Válasszon…”). “vigyél” is the informal imperative addressed to the browser/user in tegező form, inconsistent with the established formal address.
- `Strings.InfoText` — `browser/updater/updater.ini` — `Strings.InfoText` uses three dots where this locale uses …
    - Current: `A %MOZ_APP_DISPLAYNAME% telepíti a frissítéseket, és pár pillanat múlva elindul...`
    - Source: `%MOZ_APP_DISPLAYNAME% is installing your updates and will start in a few moments…`
    - The tree uses … 389 times against 4 ASCII runs.
- `heading` — `dom/chrome/accessibility/AccessFu.properties` — “heading” is translated as “fejléc”, the same word used for “header”, collapsing two distinct roles.
    - Current: `heading = fejléc`
    - Source: `heading`
    - Suggest: `heading = címsor`
    - The same file already has “header = fejléc”, and dom/chrome/accessibility/mac/accessible.properties translates the ARIA heading role as “címsor”; a screen reader would announce headers and headings identically.
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
    - Current: `A billentyűesemény nem érhető el GTK2 alatt: key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `polish-double` (792 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
    - Current: `A billentyűesemény nem érhető el egyes billentyűzetkiosztások esetén: key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `polish-double` (792 occurrences).
- `TooLargeDashedRadius` — `dom/chrome/layout/css.properties` — `TooLargeDashedRadius` uses straight double quotes
    - Current: `A szegélysugár túl nagy a "dashed" stílushoz (a korlát 100000px). Megjelenítés tömörként.`
    - Source: `Border radius is too large for ‘dashed’ style (the limit is 100000px). Rendering as solid.`
    - The locale's quote convention is `polish-double` (792 occurrences).
- `TooLargeDottedRadius` — `dom/chrome/layout/css.properties` — `TooLargeDottedRadius` uses straight double quotes
    - Current: `A szegélysugár túl nagy a "dotted" stílushoz (a korlát 100000px). Megjelenítés tömörként.`
    - Source: `Border radius is too large for ‘dotted’ style (the limit is 100000px). Rendering as solid.`
    - The locale's quote convention is `polish-double` (792 occurrences).
- `crashreporter-button-details` — `toolkit/crashreporter/crashreporter.ftl` — `crashreporter-button-details` uses three dots where this locale uses …
    - Current: `Részletek...`
    - Source: `Details…`
    - The tree uses … 389 times against 4 ASCII runs.
- `crashreporter-resubmit-status` — `toolkit/crashreporter/crashreporter.ftl` — `crashreporter-resubmit-status` uses three dots where this locale uses …
    - Current: `A korábban sikertelenül elküldött bejelentések újraküldése...`
    - Source: `Resending reports that previously failed to send…`
    - The tree uses … 389 times against 4 ASCII runs.
- `crashreporter-submit-in-progress` — `toolkit/crashreporter/crashreporter.ftl` — `crashreporter-submit-in-progress` uses three dots where this locale uses …
    - Current: `Bejelentés elküldése...`
    - Source: `Submitting your report…`
    - The tree uses … 389 times against 4 ASCII runs.
- `about-webrtc-consecutive-frames` — `toolkit/toolkit/about/aboutWebrtc.ftl` — Video "frames" rendered as "keretek" (borders) instead of "képkockák" used elsewhere in the file.
    - Current: `Egymást követő keretek`
    - Source: `Consecutive Frames`
    - Suggest: `Egymást követő képkockák`
    - This is in the video frame statistics block, where the same file consistently uses "képkocka" (about-webrtc-dropped-frames-label, about-webrtc-frames, about-webrtc-first-frame-timestamp). "keret" means a frame/border, not a video frame.
- `neterror-dns-not-found-offline-hint-reconnect` — `toolkit/toolkit/neterror/netError.ftl` — "Wi-Fi" written with an en dash instead of a hyphen.
    - Current: `kapcsolódjon újra a Wi–Fi-hez`
    - Source: `Disconnect and reconnect to Wi-Fi.`
    - Suggest: `kapcsolódjon újra a Wi-Fi-hez`
    - fp-neterror-offline-what-can-you-do-body in the same file writes "Wi-Fi" with a plain hyphen, as does the en-US source.
- `backgroundupdate-task-description` — `toolkit/toolkit/updates/backgroundupdate.ftl` — Stray space before a comma.
    - Current: `frissítéseit , ha`
    - Source: `The Background Update task checks for updates to { -brand-short-name } when { -brand-short-name } is not running. This task is installed automatically by { -brand-short-name }, and is reinstalled when { -brand-short-nam…`
    - Suggest: `frissítéseit, ha`
    - A space must not precede a comma in Hungarian; the en-US source has no such gap.

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

### Fixed to date (5)

- `pdfjs-editor-undo-bar-message-multiple` — `toolkit/toolkit/pdfviewer/viewer.ftl` — fixed 2026-09-14
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — fixed 2026-09-01
- `onboarding-new-user-survey-legal-link-label` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-09-01
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — fixed 2026-09-01
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — fixed 2026-09-01
