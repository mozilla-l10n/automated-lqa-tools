# Firefox l10n QA — el

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `ba8eba5819d0` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `2d5e7eb1f225` |
| **Previous run** | 2026-10-16 @ `db2cfca9d18c` |
| **Mode** | incremental |
| **Strings reviewed this run** | 112 of 16,520 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for el: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (1)

- `permissions-site-app-links-desc` — `browser/browser/preferences/permissions.ftl` — "App links" is rendered as "συνδέσμων από εφαρμογές" (links from apps), which doesn't match the "συνδέσμων εφαρμογών" used in the window title and related strings.
    - Current: `το άνοιγμα συνδέσμων από εφαρμογές`
    - Source: `These sites are blocked from asking to open app links, like email (mailto:). Remove a site to allow it to ask again.`
    - Suggest: `το άνοιγμα συνδέσμων εφαρμογών`
    - App links are links that open an app (e.g. mailto:), not links that come from apps. The window title and permission strings use "συνδέσμων εφαρμογών". The "από" changes the meaning and makes the terminology inconsistent on the same surface.

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
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1013, `curly-single` 94, `straight-double` 25, `curly-double` 2 | **guillemet** |
| apostrophe | `typographic` 98, `straight` 5 | **typographic** |
| ellipsis | `char` 398, `ascii` 2 | **char** |
| dash | `em` 63, `en` 2 | **em** |
| nbsp | `total` 15, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (211)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 143 |
| 2 | Wrong content (says something other than the English) | 65 |
| 3 | Degraded language (grammar, spelling, terminology) | 1 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `smart-window-closed-tabs-summary` — `browser/browser/aiWindowContent.ftl` — Plural variant mixes a singular noun with a plural verb.
    - Current: `Αυτό ήταν! Η καρτέλα έκλεισαν.`
    - Source: `{$count ->} [one] Done! Tab closed. [other] Done! Tabs closed.`
    - Suggest: `Αυτό ήταν! Οι καρτέλες έκλεισαν.`
    - The [other] variant of “Done! Tabs closed.” keeps the singular subject «Η καρτέλα» from the [one] variant while using the plural verb «έκλεισαν», so the plural case reads ungrammatically and states the wrong number.
- `taskbar-tabs-gaming-callout-title-v3` — `browser/browser/featureCallout.ftl` — “taskbar” rendered as “toolbar” (γραμμή εργαλείων).
    - Current: `Επιστρέψτε στα παιχνίδια από τη γραμμή εργαλείων`
    - Source: `Get back to gaming from your taskbar`
    - Suggest: `Επιστρέψτε στα παιχνίδια από τη γραμμή εργασιών`
    - en-US is “Get back to gaming from your taskbar”. The matching subtitle and sibling strings use «γραμμή εργασιών»; «γραμμή εργαλείων» names the toolbar instead.
- `taskbar-tabs-media-callout-title` — `browser/browser/featureCallout.ftl` — “taskbar” rendered as “toolbar” (γραμμή εργαλείων) in a Taskbar Tabs callout.
    - Current: `Επιστρέψτε στη ροή από τη γραμμή εργαλείων`
    - Source: `Get back to streaming from your taskbar`
    - Suggest: `Επιστρέψτε στη ροή από τη γραμμή εργασιών`
    - en-US is “Get back to streaming from your taskbar”. Everywhere else in this file the locale renders taskbar as «γραμμή εργασιών»; «γραμμή εργαλείων» is the browser toolbar, pointing the user at the wrong UI element.
- `ipprotection-summer-promo-offramp-set-to-default-primary-button` — `browser/browser/ipProtection.ftl` — Button label is in the past tense, asserting the action already happened.
    - Current: `Ορίστηκε ως προεπιλογή`
    - Source: `Set to default`
    - Suggest: `Ορισμός ως προεπιλογή`
    - en-US “Set to default” is the action label of a button that sets Firefox as default. «Ορίστηκε» means “was set as default”, telling the user the change is already done. Other default-browser buttons in the tree use «Ορισμός ως προεπιλογή».
- `spotlight-public-wifi-vpn-body` — `browser/browser/newtab/asrouter.ftl` — "It will help keep you protected" becomes an unqualified promise that the VPN will protect the user.
    - Current: `Θα σας προστατεύει κατά την περιήγηση`
    - Source: `To hide your location and browsing activity, consider a Virtual Private Network. It will help keep you protected when browsing in public places like airports and coffee shops.`
    - Suggest: `Θα σας βοηθήσει να παραμείνετε προστατευμένοι κατά την περιήγηση`
    - The en-US hedge "will help keep you protected" is deliberate; «Θα σας προστατεύει» asserts protection outright, a guarantee the product does not give.
- `windows-10-eos-callout-addons-title` — `browser/browser/newtab/asrouter.ftl` — The positive "big impacts" is rendered with a word that in Greek denotes negative repercussions.
    - Current: `μεγάλες επιπτώσεις`
    - Source: `Try add-ons: simple upgrades, big impacts`
    - Suggest: `μεγάλα οφέλη`
    - «επιπτώσεις» is standardly used for adverse consequences, so the promotional headline "simple upgrades, big impacts" reads as "simple upgrades, big repercussions".
- `windows-10-eos-sync-callout-privacy-screen-2-subtitle` — `browser/browser/newtab/asrouter.ftl` — "your data and privacy settings" is collapsed into "data and privacy settings", dropping the data itself.
    - Current: `τις ρυθμίσεις δεδομένων και απορρήτου`
    - Source: `Backing up { -brand-shorter-name } makes it easy to bring your data and privacy settings with you.`
    - Suggest: `τα δεδομένα και τις ρυθμίσεις απορρήτου σας`
    - The en-US promises you can bring both your data and your privacy settings; the Greek genitive makes «δεδομένων» a modifier of «ρυθμίσεις», so only settings are carried over.
- `newtab-privacy-message-info-2` — `browser/browser/newtab/newtab.ftl` — The hedge "helps stop" is dropped, stating that tracker blocking prevents companies from following the user.
    - Current: `εμποδίζει την καταγραφή σας από εταιρείες`
    - Source: `Tracker blocking helps stop companies from following you online.`
    - Suggest: `βοηθά στο να μην σας καταγράφουν εταιρείες`
    - en-US "helps stop companies from following you online" is hedged, and neighbouring strings in the same widget keep the hedge («συμβάλλει», «βοηθά»); here it is removed.
- `newtab-privacy-message-info-6` — `browser/browser/newtab/newtab.ftl` — The hedged "but other browsers might" is turned into a flat assertion that other browsers do sell user data.
    - Current: `σε αντίθεση με άλλα προγράμματα περιήγησης`
    - Source: `Keep your data with { -brand-short-name }. We never sell it, but other browsers might.`
    - Suggest: `αλλά άλλα προγράμματα περιήγησης ίσως το κάνουν`
    - en-US says "We never sell it, but other browsers might" — a possibility about competitors. «σε αντίθεση με άλλα προγράμματα περιήγησης» ("unlike other browsers") states as fact that the others sell user data, an accusation the source does not make.
- `newtab-section-blocked-button` — `browser/browser/newtab/newtab.ftl` — The "Blocked" state label is translated identically to the "Block" action button, so the toggle gives no indication that the topic is already blocked.
    - Current: `newtab-section-blocked-button = Φραγή`
    - Source: `Blocked`
    - Suggest: `newtab-section-blocked-button = Αποκλεισμένο`
    - en-US distinguishes Block / Blocked / Unblock; el renders both newtab-section-block-button and newtab-section-blocked-button as «Φραγή». The sibling follow trio correctly distinguishes action from state («Ακολουθήστε» vs «Ακολουθείται»), so the blocked state should likewise be a state form, not the action noun.
- `fx-backup-confirmation-screen-all-data-item-text-2` — `browser/browser/newtab/onboarding.ftl` — "Saved to your device" is rendered in the past tense, telling the user the backup has already been written.
    - Current: `fx-backup-confirmation-screen-all-data-item-text-2 = Αποθηκεύτηκε στη συσκευή σας`
    - Source: `Saved to your device`
    - Suggest: `fx-backup-confirmation-screen-all-data-item-text-2 = Αποθήκευση στη συσκευή σας`
    - This screen confirms a scheduled backup («Η δημιουργία του αντιγράφου ασφαλείας σας έχει προγραμματιστεί», starting "in a few minutes"); the aorist «Αποθηκεύτηκε» says it has already happened, unlike the sibling bullets which stay in the present («Περιλαμβάνονται…»).
- `fx-backup-confirmation-screen-easy-setup-item-text-2` — `browser/browser/newtab/onboarding.ftl` — "Saved to your device" is rendered in the past tense, telling the user the backup has already been written.
    - Current: `fx-backup-confirmation-screen-easy-setup-item-text-2 = Αποθηκεύτηκε στη συσκευή σας`
    - Source: `Saved to your device`
    - Suggest: `fx-backup-confirmation-screen-easy-setup-item-text-2 = Αποθήκευση στη συσκευή σας`
    - Same defect as the all-data variant: the backup is only scheduled at this point, but «Αποθηκεύτηκε» states it is already saved.
- `places-by-day-and-site` — `browser/browser/places.ftl` — "By Date and Site" is rendered as "by date and page".
    - Current: `Κατά ημερομηνία και σελίδα`
    - Source: `accesskey: t label: By Date and Site`
    - Suggest: `Κατά ημερομηνία και ιστότοπο`
    - «σελίδα» means page, not site; the adjacent places-by-site in the same menu correctly uses «Κατά ιστότοπο» for "By Site".
- `policy-DisabledCiphers` — `browser/browser/policies/policies-descriptions.ftl` — "Disable ciphers" is rendered as "disable encryption", describing a far broader effect than the policy has.
    - Current: `policy-DisabledCiphers = Απενεργοποίηση κρυπτογράφησης.`
    - Source: `Disable ciphers.`
    - Suggest: `policy-DisabledCiphers = Απενεργοποίηση αλγορίθμων κρυπτογράφησης.`
    - The policy disables individual TLS ciphers, not encryption as such. Elsewhere in the tree "cipher" is rendered «αλγόριθμος κρυπτογράφησης» (toolkit/toolkit/neterror/nsserrors.ftl), so an administrator reading «Απενεργοποίηση κρυπτογράφησης» is told the policy turns encryption off.
- `connection-dns-over-https-url-custom` — `browser/browser/preferences/connection.ftl` — Tooltip says DNS resolution “instead of HTTPS” rather than “over HTTPS”.
    - Current: `Εισάγετε το προτιμώμενο URL σας για επίλυση DNS αντί HTTPS`
    - Source: `accesskey: C label: Custom tooltiptext: Enter your preferred URL for resolving DNS over HTTPS`
    - Suggest: `Εισαγάγετε το προτιμώμενο URL σας για επίλυση DNS μέσω HTTPS`
    - en-US is “Enter your preferred URL for resolving DNS over HTTPS”. “αντί HTTPS” means “instead of HTTPS”, reversing the feature; the sibling string connection-dns-over-https-url-item-default correctly uses “μέσω HTTPS”.
- `connection-proxy-socks` — `browser/browser/preferences/connection.ftl` — “SOCKS Host” rendered as “SOCKS system”.
    - Current: `Σύστημα SOCKS`
    - Source: `(value): SOCKS Host accesskey: C`
    - Suggest: `Διακομιστής SOCKS`
    - The field takes the SOCKS host name/address. “Σύστημα” means “system”, not “host”; the locale renders “hostname” as “όνομα κεντρικού υπολογιστή” elsewhere (permissions-invalid-uri-title).
- `autofill-address-department` — `browser/browser/preferences/formAutofill.ftl` — Administrative “Department” rendered as “Τμήμα” (an office department).
    - Current: `Τμήμα`
    - Source: `Department`
    - Suggest: `Διαμέρισμα`
    - The developer comment narrows this to the primary administrative division of Nicaragua/Colombia; «Τμήμα» means a department/section of an organisation, not a territorial division.
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — “form controls” narrowed to “form buttons”.
    - Current: `μετακίνηση της εστίασης μεταξύ κουμπιών φόρμας και συνδέσμων`
    - Source: `accesskey: t label: Use the tab key to move focus between form controls and links`
    - Suggest: `μετακίνηση της εστίασης μεταξύ στοιχείων ελέγχου φόρμας και συνδέσμων`
    - en-US “between form controls and links”; Tab moves focus between all form controls (text fields, checkboxes, selects), not just buttons.
- `containers-remove-alert-title` — `browser/browser/preferences/preferences.ftl` — Dialog title says “Remove container tab?” instead of “Remove this container?”
    - Current: `Αφαίρεση θεματικής καρτέλας;`
    - Source: `Remove This Container?`
    - Suggest: `Αφαίρεση θεματικής ενότητας;`
    - en-US “Remove This Container?”. The dialog removes the container itself, and the body/buttons of the same dialog correctly use “θεματική ενότητα” (containers-remove-ok-button). The title states a different object (a tab).
- `history-remember-option-never2` — `browser/browser/preferences/preferences.ftl` — “Never remember history” rendered as “Delete history”.
    - Current: `Διαγραφή ιστορικού`
    - Source: `description: Every window acts like a private window. When on, extensions need to be allowed. label: Never remember history`
    - Suggest: `Να μην διατηρείται ιστορικό`
    - The option makes every window behave like a private window so history is never recorded; the Greek label tells the user history will be deleted, which is a different action from what the setting does.
- `home-prefs-highlights-option-most-recent-download` — `browser/browser/preferences/preferences.ftl` — Singular “Most recent download” rendered as plural.
    - Current: `Πιο πρόσφατες λήψεις`
    - Source: `label: Most recent download`
    - Suggest: `Πιο πρόσφατη λήψη`
    - en-US is singular “Most recent download”; the option surfaces a single item.
- `set-background-span` — `browser/browser/setDesktopBackground.ftl` — The wallpaper "Span" option is rendered as «Διάστημα» (interval/space).
    - Current: `Διάστημα`
    - Source: `label: Span`
    - Suggest: `Επέκταση`
    - The comment asks to match Windows' own Desktop Background wording; «Διάστημα» means a gap or interval and does not describe a wallpaper stretched across multiple monitors.
- `sidebar-opentabs-sort-option-order` — `browser/browser/sidebar.ftl` — "Tab order" is rendered as "Tab sorting", which does not name the sort option.
    - Current: `Ταξινόμηση καρτελών`
    - Source: `label: Tab order`
    - Suggest: `Σειρά καρτελών`
    - The comment says this option lists tabs in the order they appear on the tab strip; it sits under the heading «Ταξινόμηση κατά», so repeating «Ταξινόμηση» as the option name states no criterion, while the source names the tab-strip order.
- `split-view-menuitem-separate-tabs` — `browser/browser/tabbrowser.ftl` — "Separate Tabs" (undo the split view) is rendered as "Διαχωρισμός καρτελών", which reads as "Split tabs" — the opposite action.
    - Current: `Διαχωρισμός καρτελών`
    - Source: `label: Separate Tabs`
    - Suggest: `Αναίρεση διαχωρισμού προβολής`
    - The developer comment states "Separate" is a verb, as in "separate the split view tabs and display them normally". The locale uses «διαχωρισμός προβολής» throughout this file for *creating* a split view (tab-context-add-split-view = «Έναρξη διαχωρισμού προβολής»), and uses «Αναίρεση διαχωρισμού προβολής» for the equivalent separate action (tab-context-separate-split-view). So «Διαχωρισμός καρτελώ…
- `unblockTypeMalware` — `browser/chrome/browser/downloads/downloads.properties` — Certain harm («will harm») weakened to possible harm («may harm»)
    - Current: `που ενδέχεται να βλάψει τον υπολογιστή σας`
    - Source: `This file contains a virus or other malware that will harm your computer.`
    - Suggest: `που θα βλάψει τον υπολογιστή σας`
    - The en-US asserts the malware will harm the computer; the Greek downgrades it to a possibility, which also makes it indistinguishable from the weaker blockedPotentiallyUnwanted warning.
- `ComponentsText` — `browser/installer/override.properties` — "uncheck the components you don’t want" is rendered as "remove those you don’t want".
    - Current: `καταργήστε αυτά που δεν θέλετε`
    - Source: `Check the components you want to install and uncheck the components you don’t want to install. $_CLICK`
    - Suggest: `αποεπιλέξτε αυτά που δεν θέλετε`
    - «καταργήστε» on its own means abolish/remove, not clear the checkbox; the instruction reads as deleting components rather than deselecting them.
- `about-debugging-runtime-profile-button2` — `devtools/client/aboutdebugging.ftl` — The “Profile performance” action button turned into the noun phrase “profile performance (of the profile)”.
    - Current: `Επιδόσεις προφίλ`
    - Source: `Profile performance`
    - Suggest: `Καταγραφή επιδόσεων`
    - In English this is a verb+object label for the button that opens the profiler; the Greek reads as “the profile’s performance”, so the button no longer names an action.
- `accessibility-text-label-issue-figure` — `devtools/client/accessibility.ftl` — “Figures” (<figure> elements) translated as “numbers”.
    - Current: `Οι αριθμοί με προαιρετικές λεζάντες`
    - Source: `Figures with optional captions should be labeled. <a>Learn more</a>`
    - Suggest: `Τα σχήματα/εικόνες με προαιρετικές λεζάντες`
    - The check is about <figure> elements with captions; «αριθμοί» means numerals, which makes the accessibility advice unintelligible.
- `accessibility.toolbar.displayTabbingOrder.label` — `devtools/client/accessibility.properties` — “Tabbing order” (keyboard Tab focus order) is rendered as the order of browser tabs.
    - Current: `Εμφάνιση σειράς καρτελών`
    - Source: `Show Tabbing Order`
    - Suggest: `Εμφάνιση σειράς εστίασης (Tab)`
    - “Tabbing order” is the sequence in which elements receive focus with the Tab key; «καρτέλες» are browser tabs. The tooltip repeats the error («σειράς καρτελών και του ευρετηρίου καρτελών»), so the whole a11y feature is described as being about tabs.
- `serviceworker-empty-suggestions2` — `devtools/client/application.ftl` — “step through your service worker registration in the Debugger” rendered as “log/record your service worker in the Debugger”.
    - Current: `να καταγράψετε το service worker σας στον <span>Έλεγχο σφαλμάτων</span>`
    - Source: `If the current page should have a service worker, you could look for errors in the <a>Console</a> or step through your service worker registration in the <span>Debugger</span>.`
    - Suggest: `να εκτελέσετε βήμα προς βήμα την εγγραφή του service worker σας στον <span>Έλεγχο σφαλμάτων</span>`
    - The source tells the user to step through the registration code in the debugger; «να καταγράψετε» means to record/log it, which is a different action and loses the word “registration”.
- `boxmodel.offsetParent.title` — `devtools/client/boxmodel.properties` — “Offset parent of the selected element” rendered as “offset of the parent of the selected element”.
    - Current: `Μετατόπιση γονέα επιλεγμένου στοιχείου`
    - Source: `Offset parent of the selected element`
    - Suggest: `Γονικό στοιχείο μετατόπισης (offset parent) του επιλεγμένου στοιχείου`
    - “Offset parent” is a single concept (the positioned ancestor); the Greek makes «μετατόπιση» the head noun, so the tooltip describes a displacement value rather than the previewed DOM node. The matching label uses yet another word («απόσταση»).
- `editor.addLogPoint` — `devtools/client/debugger.properties` — “Add log” (log point) rendered as “Add log file”.
    - Current: `Προσθήκη αρχείου καταγραφής`
    - Source: `Add log`
    - Suggest: `Προσθήκη καταγραφής`
    - The gutter item adds a log point / log message, not a log file; the same wrong «αρχείο καταγραφής» is used in editor.editLogPoint and the log point placeholder.
- `pauseOnCaughtExceptionsItem` — `devtools/client/debugger.properties` — “caught exceptions” rendered as “anticipated/expected exceptions”.
    - Current: `Παύση σε προβλεπόμενες εξαιρέσεις`
    - Source: `Pause on caught exceptions`
    - Suggest: `Παύση σε εξαιρέσεις που εντοπίζονται (caught)`
    - “Caught” means handled by a catch block; «προβλεπόμενες» (foreseen/expected) describes a different condition and misstates when the debugger will pause.
- `watchExpressions.header` — `devtools/client/debugger.properties` — “Watch expressions” rendered as “Watch exceptions”.
    - Current: `Παρακολούθηση εξαιρέσεων`
    - Source: `Watch expressions`
    - Suggest: `Εκφράσεις παρακολούθησης`
    - «εξαιρέσεις» = exceptions, not expressions; the sidebar pane header then names a completely different debugger concept, while related strings correctly use «έκφραση παρακολούθησης».
- `dropShadowPlaceholder` — `devtools/client/filterwidget.properties` — The drop-shadow value order is scrambled and “radius” becomes a genitive modifier of “color”.
    - Current: `χρώμα ακτίνας x y`
    - Source: `x y radius color`
    - Suggest: `x y ακτίνα χρώμα`
    - The placeholder documents the expected CSS argument order (x y radius color); the Greek reverses it and reads as “colour of radius x y”, so it tells the developer to type the values in the wrong order.
- `fontinspector.letterSpacingLabel` — `devtools/client/font-inspector.properties` — Letter spacing labelled «Διάστιχο», which means line spacing.
    - Current: `Διάστιχο`
    - Source: `Spacing`
    - Suggest: `Απόσταση χαρακτήρων`
    - The comment says this control changes letter spacing; «διάστιχο» is the typographic term for leading/line spacing and collides with the adjacent «Ύψος γραμμής» control.
- `eventsTooltip.Capturing` — `devtools/client/inspector.properties` — The DOM event “Capturing” phase rendered as “Recording/registration”.
    - Current: `Εγγραφή`
    - Source: `Capturing`
    - Suggest: `Σύλληψη`
    - Paired with «Διάδοση» for Bubbling, this labels the capture phase of event propagation; «Εγγραφή» means recording or registration and names a different concept.
- `inspectorCopyCSSSelector.label` — `devtools/client/inspector.properties` — “CSS Selector” rendered as “CSS selection/choice”.
    - Current: `Επιλογή CSS`
    - Source: `CSS Selector`
    - Suggest: `Επιλογέας CSS`
    - In the Copy submenu this item copies the element’s CSS selector; «Επιλογή CSS» reads as “Select CSS”. Other files use the correct «Επιλογέας CSS» (e.g. inspectNodeDesc, styleinspector.contextmenu.copySelector).
- `heapview.field.shallowSize` — `devtools/client/memory.properties` — “Shallow Size” rendered as “Shadow size”.
    - Current: `Μέγεθος σκιάς (Bytes)`
    - Source: `Shallow Size (Bytes)`
    - Suggest: `Ρηχό μέγεθος (Bytes)`
    - «σκιά» means shadow; the column shows the object’s own size (per its tooltip), so the header names a non-existent metric.
- `toolbar.viewing-individuals` — `devtools/client/memory.properties` — “individuals” (individual heap nodes) rendered as “persons”.
    - Current: `⁂ Προβολή ατόμων στην ομάδα`
    - Source: `⁂ Viewing individuals in group`
    - Suggest: `⁂ Προβολή μεμονωμένων κόμβων στην ομάδα`
    - «άτομα» means people; tree-item.view-individuals.tooltip in the same panel correctly uses «μεμονωμένων κόμβων».
- `netmonitor.custom.headers` — `devtools/client/netmonitor.properties` — “Request Headers” label rendered as “Response headers”.
    - Current: `Κεφαλίδες απόκρισης:`
    - Source: `Request Headers`
    - Suggest: `Κεφαλίδες αιτήματος:`
    - The comment says this label sits above the request headers entry of the custom request form; the Greek names the opposite side of the exchange.
- `netmonitor.custom.query` — `devtools/client/netmonitor.properties` — “Query String” rendered as “query thread”.
    - Current: `Νήμα ερώτησης`
    - Source: `Query String`
    - Suggest: `Συμβολοσειρά ερωτήματος`
    - “String” here is a character string, not a thread of execution; «νήμα» is the word used for threads elsewhere in DevTools, so the field label names an unrelated concept.
- `netmonitor.search.toolbar.clear` — `devtools/client/netmonitor.properties` — “Clear Search Results” rendered as “Close search results”.
    - Current: `Κλείσιμο αποτελεσμάτων αναζήτησης`
    - Source: `Clear Search Results`
    - Suggest: `Εκκαθάριση αποτελεσμάτων αναζήτησης`
    - The button clears the results list; rendering it as “close” makes it indistinguishable from the adjacent close-panel button, which is also «Κλείσιμο…».
- `netmonitor.toolbar.requestBlocking` — `devtools/client/netmonitor.properties` — “Request Blocking” inverted to “blocking requirement/request for blocking”.
    - Current: `Απαίτηση φραγής`
    - Source: `Request Blocking`
    - Suggest: `Φραγή αιτημάτων`
    - “Request” is the object being blocked, not a demand; the button tooltip now describes a requirement rather than the feature that blocks network requests.
- `netmonitor.toolbar.scheme` — `devtools/client/netmonitor.properties` — The URL “Scheme” column renamed “diagram/outline”.
    - Current: `Σχεδιάγραμμα`
    - Source: `Scheme`
    - Suggest: `Σχήμα (scheme)`
    - The column shows the URL scheme (http, https…); «σχεδιάγραμμα» means a sketch or diagram.
- `perftools-thread-timer` — `devtools/client/perftools.ftl` — “The thread handling timers” reversed into “the timers handling threads”.
    - Current: `Τα χρονόμετρα χειρισμού νημάτων (setTimeout, setInterval, nsITimer)`
    - Source: `title: The thread handling timers (setTimeout, setInterval, nsITimer)`
    - Suggest: `Το νήμα που χειρίζεται τα χρονόμετρα (setTimeout, setInterval, nsITimer)`
    - The head noun and the object are swapped, so the tooltip describes timers that manage threads instead of the thread that runs timers.
- `options-sourceeditor-tabsize-label` — `devtools/client/toolbox-options.ftl` — Editor “Tab size” rendered as “tab (browser tab) size”.
    - Current: `Μέγεθος καρτέλας`
    - Source: `Tab size`
    - Suggest: `Μέγεθος στηλοθέτη`
    - This setting controls the width of the Tab indentation character, not a browser tab; the adjacent tooltip repeats the error («χαρακτήρα καρτέλας»).
- `accessibility.text.label.issue.figure` — `devtools/shared/accessibility.properties` — “Figures” (<figure> elements) translated as “numbers”.
    - Current: `Οι αριθμοί με προαιρετικές λεζάντες πρέπει να φέρουν ετικέτα.`
    - Source: `Figures with optional captions should be labeled.`
    - Suggest: `Τα σχήματα με προαιρετικές λεζάντες πρέπει να φέρουν ετικέτα.`
    - Same defect as accessibility-text-label-issue-figure: <figure> elements are rendered as “numbers”.
- `whypaused-interrupted` — `devtools/shared/debugger-paused-reasons.ftl` — “Paused at Execution” rendered as “Paused on the exception”.
    - Current: `Έγινε παύση στην εξαίρεση`
    - Source: `Paused at Execution`
    - Suggest: `Έγινε παύση κατά την εκτέλεση`
    - The debugger overlay would tell the user it stopped on an exception when it actually paused at a JS execution point; it also duplicates whypaused-exception.
- `screenshotNoSelectorMatchWarning` — `devtools/shared/screenshot.properties` — “selector” rendered as “selection tool”.
    - Current: `Το εργαλείο επιλογής ‘%S’ δεν αντιστοιχεί σε κανένα στοιχείο της σελίδας.`
    - Source: `The ‘%S’ selector does not match any element on the page.`
    - Suggest: `Ο επιλογέας ‘%S’ δεν αντιστοιχεί σε κανένα στοιχείο της σελίδας.`
    - %S is the CSS selector the user passed; the same file renders “CSS selector” correctly as «Επιλογέας CSS» in inspectNodeDesc.
- `rule.selectorSpecificity.title` — `devtools/shared/styleinspector.properties` — CSS “Specificity” rendered as “Accuracy”.
    - Current: `Ακρίβεια: %S`
    - Source: `Specificity: %S`
    - Suggest: `Ειδικότητα: %S`
    - The tooltip shows the computed specificity triple of a selector; «ακρίβεια» means precision/accuracy and names a different property.
- `logpoint.title` — `devtools/shared/webconsole.properties` — “Logpoints” rendered as “connection points”.
    - Current: `Σημεία σύνδεσης από τον έλεγχο σφαλμάτων`
    - Source: `Logpoints from the debugger`
    - Suggest: `Σημεία καταγραφής από τον έλεγχο σφαλμάτων`
    - «σύνδεση» means connection; the tooltip identifies console output coming from debugger log points, so it names an unrelated concept.
- `press` — `dom/chrome/accessibility/mac/accessible.properties` — “Press” rendered as “long press”.
    - Current: `Παρατεταμένο πάτημα`
    - Source: `Press`
    - Suggest: `Πάτημα`
    - The accessibility action is a plain press; «Παρατεταμένο» adds a duration the source does not have and names a different gesture to screen-reader users.
- `press` — `dom/chrome/accessibility/unix/accessible.properties` — “Press” rendered as “long press”.
    - Current: `Παρατεταμένο πάτημα`
    - Source: `Press`
    - Suggest: `Πάτημα`
    - Same defect as in the mac/win variants: the action name describes a long press, not the press action the source names.
- `press` — `dom/chrome/accessibility/win/accessible.properties` — “Press” rendered as “long press”.
    - Current: `Παρατεταμένο πάτημα`
    - Source: `Press`
    - Suggest: `Πάτημα`
    - Same defect as in the mac/unix variants: «Παρατεταμένο» names a different gesture than the accessibility action “Press”.
- `RequestStorageAccessSandboxed` — `dom/chrome/dom/dom.properties` — A prohibition is rendered as a possibility.
    - Current: `Ενδέχεται να μην είναι δυνατή η κλήση του document.requestStorageAccess()`
    - Source: `document.requestStorageAccess() may not be called in a sandboxed iframe without allow-storage-access-by-user-activation in its sandbox attribute.`
    - Suggest: `Το document.requestStorageAccess() δεν μπορεί να κληθεί`
    - en-US “may not be called” is a prohibition, and every sibling string (RequestStorageAccessNested, RequestStorageAccessPermissionsPolicy) renders it as «δεν μπορεί να κληθεί»; here it reads as “it might not be possible”.
- `ScreenFingerprintingProtectionWarning` — `dom/chrome/dom/dom.properties` — “helps prevent” rendered as an unqualified “prevents”.
    - Current: `Αυτή η προστασία εμποδίζει τους ιστοτόπους από το να δημιουργήσουν ένα αποτύπωμα`
    - Source: `Fingerprinting Protection is altering screen.availWidth and screen.availHeight. These values may not match your actual screen dimensions. This protection helps prevent websites building a fingerprint that can be used to…`
    - Suggest: `Αυτή η προστασία συμβάλλει στο να εμποδίζονται οι ιστότοποι από τη δημιουργία ενός αποτυπώματος`
    - The source hedges (“helps prevent websites building a fingerprint”); the Greek states the protection does prevent it, a stronger guarantee about the product’s behaviour than Firefox makes.
- `PESelectorGroupExtraCombinator` — `dom/chrome/layout/css.properties` — “Dangling combinator” rendered as “wavering combination”.
    - Current: `Αμφιταλαντευόμενος συνδυασμός.`
    - Source: `Dangling combinator.`
    - Suggest: `Μετέωρος συνδυαστής.`
    - “Combinator” is a CSS grammar term (>, +, ~), not a “combination”, and “dangling” means left hanging, not «αμφιταλαντευόμενος» (vacillating).
- `PESelectorGroupNoSelector` — `dom/chrome/layout/css.properties` — “Selector” rendered as «διαλογέας» (sorter).
    - Current: `Αναμένεται διαλογέας.`
    - Source: `Selector expected.`
    - Suggest: `Αναμενόταν επιλογέας.`
    - Everywhere else in this file “selector” is «επιλογέας»; «διαλογέας» is a different word (sorting machine) and is not a CSS term.
- `EncSpeculationFailMeta` — `dom/chrome/layout/htmlparser.properties` — “encoding” rendered as “encryption”.
    - Current: `τη μεταετικέτα που δήλωσε την κρυπτογράφηση`
    - Source: `The start of the document was reparsed, because there were non-ASCII characters before the meta tag that declared the encoding. The meta should be the first child of head without non-ASCII comments before.`
    - Suggest: `τη μεταετικέτα που δήλωσε την κωδικοποίηση`
    - The whole string is about character encoding declarations («κωδικοποίηση» throughout the file); «κρυπτογράφηση» means encryption and is a different concept.
- _…and 38 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

- `appmenu-remote-tabs-turn-on-sync` — `browser/browser/appmenu.ftl` — “sync” left in English while the rest of the file translates it.
    - Current: `Ενεργοποίηση Sync…`
    - Source: `label: Turn on sync…`
    - Suggest: `Ενεργοποίηση συγχρονισμού…`
    - en-US “Turn on sync…” uses the common noun, not the brand. Every neighbouring string (appmenu-fxa-setup-sync, appmenu-sync-promo-turnonsync-cta, fxa-menu-sync-status-on) renders it as «συγχρονισμός».
- `main-context-menu-frame-add-bookmark` — `browser/browser/browserContext.ftl` — “Frame” rendered as «καρέ» (film frame) instead of «πλαίσιο».
    - Current: `Προσθήκη καρέ σε σελιδοδείκτη…`
    - Source: `accesskey: m label: Bookmark Frame…`
    - Suggest: `Προσθήκη πλαισίου σε σελιδοδείκτη…`
    - Every other frame string in the same context menu (main-context-menu-frame, -frame-open-tab, -frame-save-as, -frame-print, -frame-view-source) uses «πλαίσιο»; «καρέ» means a frame of film/video.
- `taskbar-tabs-email-callout-subtitle-v3` — `browser/browser/featureCallout.ftl` — “email” transliterated as «εμαιλ».
    - Current: `Εκκινήστε τους ιστοτόπους εμαιλ σας σαν εφαρμογή`
    - Source: `Launch your email sites like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `Εκκινήστε τους ιστοτόπους email σας σαν εφαρμογή`
    - The tree consistently keeps the Latin form “email” (see taskbar-tabs-email-callout-title/subtitle in this same file); «εμαιλ» is an ad-hoc transliteration that appears nowhere else.
- `migration-source-name-ie` — `browser/browser/migrationWizard.ftl` — Brand name "Internet Explorer" starts with a Greek capital iota (Ι) instead of Latin I.
    - Current: `Ιnternet Explorer`
    - Source: `Internet Explorer`
    - Suggest: `Internet Explorer`
    - A Cyrillic/Greek homoglyph inside an otherwise Latin brand name breaks search, sorting and screen-reader pronunciation; the neighbouring migration-wizard-migrator-display-name-ie uses the correct Latin spelling.
- `policy-NoDefaultBookmarks` — `browser/browser/policies/policies-descriptions.ftl` — Misspelling of «συμπεριλαμβάνονται».
    - Current: `συμπεριλαμβάνοται`
    - Source: `Disable creation of the default bookmarks bundled with { -brand-short-name }, and the Smart Bookmarks (Most Visited, Recent Tags). Note: this policy is only effective if used before the first run of the profile.`
    - Suggest: `συμπεριλαμβάνονται`
    - The verb form is missing its «ν»: «συμπεριλαμβάνοται» is not a Greek word.
- `site-storage-persistent` — `browser/browser/preferences/siteDataSettings.ftl` — “Persistent” storage rendered as “Επίμονο” instead of the “μόνιμη” used in the same dialog.
    - Current: `(Επίμονο)`
    - Source: `value: { site-storage-usage.value } (Persistent)`
    - Suggest: `(Μόνιμο)`
    - site-data-settings-description in the same dialog renders persistent storage as «μόνιμη αποθήκευση»; «Επίμονο» (“stubborn/insistent”) is not the storage term and is inconsistent on the same surface.
- `permission.persistent-storage.label` — `browser/chrome/browser/sitePermissions.properties` — «persistent storage» rendered «επίμονη αποθήκευση» instead of «μόνιμη αποθήκευση»
    - Current: `Αποθήκευση δεδομένων στην επίμονη αποθήκευση`
    - Source: `Store data in persistent storage`
    - Suggest: `Αποθήκευση δεδομένων στη μόνιμη αποθήκευση`
    - The same permission prompt in browser.properties (persistentStorage.allowWithSite2) uses «μόνιμη αποθήκευση»; «επίμονη» means insistent/stubborn and is the wrong sense of persistent for the same surface.
- `accessibility.disable.disabledTitle` — `devtools/client/accessibility.properties` — Ungrammatical phrase that also inverts the meaning of “used outside Developer Tools”.
    - Current: `Χρησιμοποιείται εκτός από των εργαλείων ανάπτυξης.`
    - Source: `Accessibility service can not be turned off. It is used outside Developer Tools.`
    - Suggest: `Χρησιμοποιείται εκτός των εργαλείων ανάπτυξης.`
    - «εκτός από» takes the accusative and means “apart from”, not “outside of”; combined with the genitive «των εργαλείων» the sentence is ungrammatical and reads as “besides the developer tools”.
- `manifest-loaded-error` — `devtools/client/application.ftl` — Wrong case after the preposition «κατά τη».
    - Current: `Προέκυψε σφάλμα κατά τη φόρτωσης της δήλωσης:`
    - Source: `There was an error while loading the manifest:`
    - Suggest: `Προέκυψε σφάλμα κατά τη φόρτωση της δήλωσης:`
    - «κατά τη» requires the accusative «φόρτωση»; «φόρτωσης» is genitive and ungrammatical.
- `eventsTooltip.toggleButton.label` — `devtools/client/inspector.properties` — «Κωδικός» (code number/PIN) used where source code «κώδικας» is meant.
    - Current: `Κωδικός ανίχνευσης συμβάντος «%S»`
    - Source: `“%S” event listener code`
    - Suggest: `Κώδικας ακροατή συμβάντος «%S»`
    - “Event listener code” is the listener’s source code; «κωδικός» is a passcode. The same error appears in eventsTooltip.codeIframeTitle.
- `shortest-paths.header` — `devtools/client/memory.properties` — Misspelling of «απορριμμάτων».
    - Current: `Διαδρομές διατήρησης (από τις ρίζες συλλογής απορριμάτων)`
    - Source: `Retaining Paths (from Garbage Collector Roots)`
    - Suggest: `Διαδρομές διατήρησης (από τις ρίζες συλλογής απορριμμάτων)`
    - «απορριμάτων» is missing a μ; the correct genitive plural is «απορριμμάτων».
- `netmonitor.actionbar.requestBlockingUsageNotice` — `devtools/client/netmonitor.properties` — Misspelled «αντίστοιχων».
    - Current: `για φραγή αντίστοιχεων αιτημάτων`
    - Source: `Add URL patterns here to block matching requests.`
    - Suggest: `για φραγή αντίστοιχων αιτημάτων`
    - The genitive plural of «αντίστοιχος» is «αντίστοιχων»; «αντίστοιχεων» is not a Greek form.
- `netmonitor.security.notAvailable` — `devtools/client/netmonitor.properties` — Stray Latin letter inside the placeholder text.
    - Current: `<Μη διαθέσιμοe>`
    - Source: `<Not Available>`
    - Suggest: `<Μη διαθέσιμο>`
    - A leftover “e” is displayed to the user in the certificate details.
- `clientSocketMisconfiguration` — `dom/chrome/appstrings.properties` — Missing conjunction makes the sentence ungrammatical.
    - Current: `Το πρόγραμμα-πελάτης δεν έχει ρυθμιστεί σωστά δεν γνωρίζει πώς να επικοινωνήσει με τον διακομιστή.`
    - Source: `The client is misconfigured and doesn’t know how to communicate with the server.`
    - Suggest: `Το πρόγραμμα-πελάτης δεν έχει ρυθμιστεί σωστά και δεν γνωρίζει πώς να επικοινωνήσει με τον διακομιστή.`
    - en-US joins the two clauses with “and”; the Greek runs two finite verbs together with no connective.
- `IIRFilterChannelCountChangeWarning` — `dom/chrome/dom/dom.properties` — Plural subject with singular verb.
    - Current: `Οι αλλαγές αριθμού καναλιών IIRFilterNode ενδέχεται να προκαλέσει δυσλειτουργίες ήχου.`
    - Source: `IIRFilterNode channel count changes may produce audio glitches.`
    - Suggest: `Οι αλλαγές αριθμού καναλιών IIRFilterNode ενδέχεται να προκαλέσουν δυσλειτουργίες ήχου.`
    - «Οι αλλαγές» is plural and requires «προκαλέσουν»; the same error is repeated in BiquadFilterChannelCountChangeWarning.
- `10` — `dom/chrome/layout/xmlparser.properties` — Accent on the monosyllable «Μη».
    - Current: `Μή έγκυρη παράμετρος στην αναφορά οντότητας`
    - Source: `illegal parameter entity reference`
    - Suggest: `Μη έγκυρη παράμετρος στην αναφορά οντότητας`
    - Monosyllabic «μη» takes no accent in modern Greek orthography; the rest of the tree writes «Μη έγκυρη».
- `InsecurePasswordsPresentOnIframe` — `dom/chrome/security/security.properties` — Duplicated article «μία ένα».
    - Current: `σε μία ένα μη ασφαλές iframe`
    - Source: `Password fields present on an insecure (http://) iframe. This is a security risk that allows user login credentials to be stolen.`
    - Suggest: `σε ένα μη ασφαλές iframe`
    - Two articles of different gender are stacked; only «ένα» agrees with «iframe».
- `network-connection-status-wrote` — `netwerk/netwerk/necko.ftl` — Status item rendered as a lowercase finite verb, unlike its siblings.
    - Current: `έγραψε { $host }`
    - Source: `Wrote { $host }`
    - Suggest: `Εγγραφή { $host }`
    - Every other item in this status list is a capitalised nominal phrase («Ανάγνωση», «Σύνδεση με…»); «έγραψε» is a third-person past verb starting in lowercase.
- `SEC_ERROR_PKCS11_DEVICE_ERROR` — `security/manager/chrome/pipnss/nsserrors.properties` — Stray accent character before «ότι».
    - Current: `πράγμα που σημαίνει ΄ότι`
    - Source: `A PKCS #11 module returned CKR_DEVICE_ERROR, indicating that a problem has occurred with the token or slot.`
    - Suggest: `πράγμα που σημαίνει ότι`
    - A loose acute-accent character precedes the already-accented «ότι», producing visible garbage in the error text.
- `SSL_ERROR_NEXT_PROTOCOL_DATA_INVALID` — `security/manager/chrome/pipnss/nsserrors.properties` — «άγκυρα» (anchor) typed for «άκυρα» (invalid).
    - Current: `Το SSL έλαβε άγκυρα δεδομένα επέκτασης NPN.`
    - Source: `SSL received invalid NPN extension data.`
    - Suggest: `Το SSL έλαβε άκυρα δεδομένα επέκτασης NPN.`
    - “invalid NPN extension data” requires «άκυρα»; «άγκυρα» is an unrelated word (anchor) and makes the sentence meaningless.
- `delete-ca-cert-confirm` — `security/manager/security/certificates/certManager.ftl` — Typo «τα τα» instead of «να τα».
    - Current: `Θέλετε τα τα διαγράψετε ή να άρετε την εμπιστοσύνη σας;`
    - Source: `You have requested to delete these CA certificates. For built-in certificates all trust will be removed, which has the same effect. Are you sure you want to delete or distrust?`
    - Suggest: `Θέλετε να τα διαγράψετε ή να άρετε την εμπιστοσύνη σας;`
    - The subjunctive particle «να» is replaced by a duplicated «τα», leaving the sentence ungrammatical.
- `delete-ca-cert-title` — `security/manager/security/certificates/certManager.ftl` — Misspelling of «πιστοποιητικών».
    - Current: `Διαγραφή ή άρση εμπιστοσύνης πιστοποητικών CA`
    - Source: `title: Delete or Distrust CA Certificates`
    - Suggest: `Διαγραφή ή άρση εμπιστοσύνης πιστοποιητικών CA`
    - A letter is missing («πιστοποητικών» → «πιστοποιητικών») in a dialog title.
- `restartMessageNoUnlocker2` — `toolkit/chrome/mozapps/profile/profileSelection.properties` — “να” is written where the article “ένα” is needed.
    - Current: `να χρησιμοποιήσετε να διαφορετικό προφίλ`
    - Source: `%S is already running, but is not responding. To use %S, you must first close the existing %S process, restart your device, or use a different profile.`
    - Suggest: `να χρησιμοποιήσετε ένα διαφορετικό προφίλ`
    - Typo producing an ungrammatical phrase in a startup error dialog.
- `delete-submitted-description` — `toolkit/crashreporter/aboutcrashes.ftl` — Participle does not agree in gender with the feminine noun.
    - Current: `τη λίστα των υποβληθέντων αναφορών κατάρρευσης`
    - Source: `This will remove the list of submitted crash reports but will not delete the submitted data. This cannot be undone.`
    - Suggest: `τη λίστα των υποβεβλημένων αναφορών κατάρρευσης`
    - “αναφορές” is feminine; “υποβληθέντων” is the masculine/neuter genitive plural participle.
- `url-classifier-content-classifier-col-important` — `toolkit/toolkit/about/url-classifier.ftl` — “Important” is translated although the developer comment says it must not be, since it is technical filter syntax.
    - Current: `Σημαντικό`
    - Source: `Important`
    - Suggest: `Important`
    - Comment: “"Important" should not be translated as it refers to technical syntax.” The column refers to the literal `important` filter option, so the translated label no longer identifies the syntax keyword.
- `contentanalysis-invalid-agent-signature-message-content` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — The verb is placed after the second placeholder, producing a broken sentence.
    - Current: `Η επαλήθευση υπογραφής για το { $agent }. { $content } απέτυχε`
    - Source: `Failed signature verification for { $agent }. { $content }`
    - Suggest: `Η επαλήθευση υπογραφής για το { $agent } απέτυχε. { $content }`
    - $content is a separate localized sentence (e.g. “Paste denied.”); appending “απέτυχε” after it yields “…for X. Paste denied. failed”, and the first clause loses its verb.
- `contentanalysis-slow-agent-dialog-body-clipboard-copy` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — Missing accent on “Αυτή”.
    - Current: `Αυτη η διαδικασία μπορεί να διαρκέσει λίγη ώρα.`
    - Source: `{ $agent } is reviewing what you copied against your organization’s data policies. This may take a moment.`
    - Suggest: `Αυτή η διαδικασία μπορεί να διαρκέσει λίγη ώρα.`
    - The word is written without its required accent, unlike every sibling string.
- `contentanalysis-slow-agent-dialog-body-dropped-text` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — Singular article with a plural noun.
    - Current: `ελέγχει το κείμενα που αποθέσατε`
    - Source: `{ $agent } is reviewing the text you dropped against your organization’s data policies. This may take a moment.`
    - Suggest: `ελέγχει το κείμενο που αποθέσατε`
    - en-US has the singular “the text you dropped”; “το κείμενα” mixes singular article with plural noun.
- `contentanalysis-slow-agent-dialog-body-file` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — Missing “να” before the verb.
    - Current: `Αυτή η διαδικασία ενδέχεται διαρκέσει λίγη ώρα.`
    - Source: `{ $agent } is reviewing “{ $filename }” against your organization’s data policies. This may take a moment.`
    - Suggest: `Αυτή η διαδικασία ενδέχεται να διαρκέσει λίγη ώρα.`
    - “ενδέχεται” requires “να”; the same omission also occurs in contentanalysis-slow-agent-dialog-body-clipboard, -dropped-text and -print, while the -file-and-more variants are correct.
- `experimental-features-link-previews-description-no-ai` — `toolkit/toolkit/firefoxlabs/features.ftl` — “reading time” contains a misspelling of “ανάγνωσης”.
    - Current: `τον χρόνο ανάνγωσης`
    - Source: `{$sel_1 ->} [macos] To learn more about a webpage before you click, hover over a link and press Shift (⇧) plus Option (⌥) or Alt. Previews can include details like title and reading time. <a data-l10n-name="connect">Sha…`
    - Suggest: `τον χρόνο ανάγνωσης`
    - Letters are transposed; the typo appears in both the macos and the default platform variant of this message.
- `profile-creation-intro` — `toolkit/toolkit/global/createProfileWizard.ftl` — Wrong verb form after “να”.
    - Current: `Μπορείτε να επιλέξτε το προεπιλεγμένο όνομα`
    - Source: `If you create several profiles you can tell them apart by the profile names. You may use the name provided here or use one of your own.`
    - Suggest: `Μπορείτε να επιλέξετε το προεπιλεγμένο όνομα`
    - The subjunctive after “να” requires “επιλέξετε”; “επιλέξτε” is the imperative.
- `webext-perms-description-proxy` — `toolkit/toolkit/global/extensionPermissions.ftl` — Permission label is in the accusative while all siblings are nominative.
    - Current: `Έλεγχο των ρυθμίσεων διακομιστή μεσολάβησης`
    - Source: `Control browser proxy settings`
    - Suggest: `Έλεγχος των ρυθμίσεων διακομιστή μεσολάβησης`
    - Every other webext-perms-description-* entry is a nominative noun phrase (“Ανάγνωση…”, “Πρόσβαση…”); “Έλεγχο” is a dangling accusative in the permission list.
- `webext-perms-extra-warning-userScripts-long` — `toolkit/toolkit/global/extensionPermissions.ftl` — Adjective is not in the genitive required by the noun.
    - Current: `η εκτέλεση επιβλαβή κώδικα`
    - Source: `Unverified scripts can pose security and privacy risks, such as running harmful code or tracking website activity. Only run scripts from extensions or sources you trust.`
    - Suggest: `η εκτέλεση επιβλαβούς κώδικα`
    - “κώδικα” here is genitive after “εκτέλεση”, so the adjective must be “επιβλαβούς”.
- `webext-colorway-theme-migration-notification-message` — `toolkit/toolkit/global/extensions.ftl` — A noun is used where the past-tense verb is needed.
    - Current: `Το { -brand-shorter-name } ενημέρωση τη συλλογή χρωματικών συνδυασμών.`
    - Source: `<b>Your colorway theme was removed.</b> { -brand-shorter-name } updated its colorways collection. You can find the latest versions on the add-ons site.`
    - Suggest: `Το { -brand-shorter-name } ενημέρωσε τη συλλογή χρωματικών συνδυασμών.`
    - “ενημέρωση” is the noun “update”; the sentence has no verb and does not parse as Greek.
- `wallet-custom-scheme-warning-host-app` — `toolkit/toolkit/global/handlerDialog.ftl` — “συνδέσμου” is written with a stray accent character inside the word.
    - Current: `Το άνοιγμα ενός συνδε΄σμου`
    - Source: `Opening a <strong>{ $scheme }</strong> link allows <strong>{ $host }</strong> to request your real identity with <strong>{ $appName }</strong>. Only continue if you trust this site.`
    - Suggest: `Το άνοιγμα ενός συνδέσμου`
    - A loose acute accent is inserted mid-word; the same corruption appears in wallet-custom-scheme-warning-app, -host and wallet-custom-scheme-warning.
- `videocontrols-status-picture-in-picture` — `toolkit/toolkit/global/videocontrols.ftl` — The article starts with a Latin “T” instead of Greek “Τ”.
    - Current: `Tο βίντεο αναπαράγεται`
    - Source: `This video is playing in Picture-in-Picture mode.`
    - Suggest: `Το βίντεο αναπαράγεται`
    - The initial character is U+0054 (Latin T) in an otherwise Greek word, a mixed-script defect.
- `region-name-fi` — `toolkit/toolkit/intl/regionNames.ftl` — Finland is misspelled.
    - Current: `Φιλανδία`
    - Source: `Finland`
    - Suggest: `Φινλανδία`
    - The correct Greek spelling is “Φινλανδία”; languageNames.ftl already uses “Φινλανδικά”.
- `region-name-hk` — `toolkit/toolkit/intl/regionNames.ftl` — Hong Kong is misspelled.
    - Current: `Χονγκ Κογκ`
    - Source: `Hong Kong`
    - Suggest: `Χονγκ Κονγκ`
    - A letter is missing from the second word of the place name.
- `region-name-za` — `toolkit/toolkit/intl/regionNames.ftl` — Adjective does not agree with the feminine noun.
    - Current: `Νότιος Αφρική`
    - Source: `South Africa`
    - Suggest: `Νότια Αφρική`
    - “Αφρική” is feminine and takes “Νότια”; cf. region-name-ss “Νότιο Σουδάν” (neuter) which is correct.
- `fp-certerror-invalid-cert-why-dangerous` — `toolkit/toolkit/neterror/certError.ftl` — Duplicated words make the sentence ungrammatical.
    - Current: `δεν έχει το έχει ρυθμίσει σωστά`
    - Source: `The owner of { $hostname } hasn’t set it up properly and a secure connection can’t be created.`
    - Suggest: `δεν το έχει ρυθμίσει σωστά`
    - “δεν έχει το έχει” repeats the auxiliary; the clause is unreadable as it stands.
- `sec-error-pkcs11-device-error` — `toolkit/toolkit/neterror/nsserrors.ftl` — A stray accent character precedes “ότι”.
    - Current: `πράγμα που σημαίνει ΄ότι`
    - Source: `A PKCS #11 module returned CKR_DEVICE_ERROR, indicating that a problem has occurred with the token or slot.`
    - Suggest: `πράγμα που σημαίνει ότι`
    - A loose acute-accent glyph is rendered before the word, visible to the user.
- `ssl-error-next-protocol-data-invalid` — `toolkit/toolkit/neterror/nsserrors.ftl` — “invalid” is misspelled as “anchor”.
    - Current: `άγκυρα δεδομένα`
    - Source: `SSL received invalid NPN extension data.`
    - Suggest: `άκυρα δεδομένα`
    - en-US: “SSL received invalid NPN extension data.” “άγκυρα” means “anchor”, a typo for “άκυρα”.
- `ssl-error-session-not-found` — `toolkit/toolkit/neterror/nsserrors.ftl` — The article starts with a Latin “T” instead of Greek “Τ”.
    - Current: `To ID συνεδρίας SSL`
    - Source: `Client’s SSL session ID not found in server’s session cache.`
    - Suggest: `Το ID συνεδρίας SSL`
    - The first character is U+0054 (Latin T), making the word a mixed-script string that breaks search, spell-check and screen-reader pronunciation.
- `pdfjs-editor-comments-sidebar-title` — `toolkit/toolkit/pdfviewer/viewer.ftl` — The singular plural-variant uses the plural noun.
    - Current: `[one] Σχόλια`
    - Source: `{$count ->} [one] Comment [other] Comments`
    - Suggest: `[one] Σχόλιο`
    - en-US has [one] Comment / [other] Comments; the Greek singular variant reads “Comments” when exactly one comment exists.
- `elevation-error-manual` — `toolkit/toolkit/updates/elevation.ftl` — Masculine article used for the (neuter) product name, plus a space before the full stop.
    - Current: `Μπορείτε να ενημερώσετε τον { -brand-short-name } χειροκίνητα .`
    - Source: `You can update { -brand-short-name } manually by visiting this link and downloading the latest version:`
    - Suggest: `Μπορείτε να ενημερώσετε το { -brand-short-name } χειροκίνητα.`
    - The locale consistently treats the brand as neuter (“το { -brand-short-name }”) everywhere else in this partition, and the space before the period is visible in the dialog text.

### D. Terminology, register & consistency

- `account-connection-disconnected` — `browser/browser/accounts.ftl` — Misspelling of «υπολογιστής».
    - Current: `Αυτός ο υπολογιστείς έχει αποσυνδεθεί.`
    - Source: `This computer has been disconnected.`
    - Suggest: `Αυτός ο υπολογιστής έχει αποσυνδεθεί.`
    - «υπολογιστείς» is not a word; the nominative is «υπολογιστής», as used in the neighbouring account-connection-connected-with strings.
- `ai-window-no-memories` — `browser/browser/aiFeatures.ftl` — Wrong article gender before «δραστηριότητά σας».
    - Current: `μαθαίνει από το δραστηριότητά σας`
    - Source: `description: As { -smart-window-brand-name } learns from your activity, you’ll see memories here. label: No memories yet`
    - Suggest: `μαθαίνει από τη δραστηριότητά σας`
    - «δραστηριότητα» is feminine, so the accusative article must be «τη», not «το». The parallel string ai-window-no-memories-learning-off has it right.
- `smart-window-model-custom-info` — `browser/browser/aiFeatures.ftl` — Latin capital “T” used instead of Greek «Τ» at the start of the sentence.
    - Current: `Tο { -smart-window-brand-name }`
    - Source: `message: When you use a custom model, { -smart-window-brand-name } may not work as expected.`
    - Suggest: `Το { -smart-window-brand-name }`
    - The article is written with the Latin letter T followed by a Greek ο, a homoglyph mix that breaks search, spell-check and screen-reader pronunciation.
- `appmenu-sync-promo-connectdevice` — `browser/browser/appmenu.ftl` — Stray accent character inside «τηλεφώνου».
    - Current: `Λάβετε τις καρτέλες του τηλεφ΄ώνου σας`
    - Source: `heading: Grab your mobile tabs`
    - Suggest: `Λάβετε τις καρτέλες του τηλεφώνου σας`
    - A standalone acute accent mark is embedded mid-word, producing «τηλεφ΄ώνου» instead of «τηλεφώνου».
- `default-browser-notification-privacy-body-text` — `browser/browser/backgroundtasks/defaultagent.ftl` — Redundant duplication of «προστασία» renders "privacy and protection" incorrectly
    - Current: `για ενσωματωμένη προστασία απορρήτου και προστασίας`
    - Source: `Your default changed. Come back to { -brand-short-name } for built-in privacy and protection.`
    - Suggest: `για ενσωματωμένο απόρρητο και προστασία`
    - "built-in privacy and protection" becomes "built-in protection of privacy and of protection"; the genitive «προστασίας» after «προστασία» is a dangling coordination, not a stylistic choice.
- `identity-description-weak-cipher-intro` — `browser/browser/browser.ftl` — Missing enclitic accent on «σύνδεσή σας».
    - Current: `Η σύνδεση σας με αυτόν τον ιστότοπο`
    - Source: `Your connection to this website uses weak encryption and is not private.`
    - Suggest: `Η σύνδεσή σας με αυτόν τον ιστότοπο`
    - «σύνδεση» is proparoxytone, so the following enclitic «σας» requires a second accent. Neighbouring strings (identity-connection-verified, identity-description-passive-loaded) correctly write «σύνδεσή σας».
- `trustpanel-fingerprinter-list-header` — `browser/browser/browser.ftl` — Duplicated «σας» makes the clause ungrammatical.
    - Current: `προσπαθούν να σας αναλύσουν το ψηφιακό σας αποτύπωμα`
    - Source: `These sites are trying to fingerprint you:`
    - Suggest: `προσπαθούν να αναλύσουν το ψηφιακό σας αποτύπωμα`
    - The sentence carries both an object clitic «σας» and a possessive «σας» for the same referent; only the possessive belongs here.
- `navbar-tooltip-instruction` — `browser/browser/browserContext.ftl` — Typo «προς στα κάτω» in the macOS variant.
    - Current: `Τραβήξτε προς στα κάτω για εμφάνιση του ιστορικού`
    - Source: `value: {$sel_1 ->} [macos] Pull down to show history [other] Right-click or pull down to show history`
    - Suggest: `Τραβήξτε προς τα κάτω για εμφάνιση του ιστορικού`
    - Two prepositions are stacked; the [other] variant of the same message correctly reads «τραβήξτε προς τα κάτω».
- `contextual-manager-passwords-remove-all-message` — `browser/browser/contextual-manager.ftl` — Misspelling «ειδοποιήσης» for «ειδοποιήσεις» in both variants.
    - Current: `καθώς και τυχόν ειδοποιήσης παραβίασης`
    - Source: `{$total ->} [1] This will remove your password saved to { -brand-short-name } and any breach alerts. You cannot undo this action. [other] This will remove the passwords saved to { -brand-short-name } and any breach aler…`
    - Suggest: `καθώς και τυχόν ειδοποιήσεις παραβίασης`
    - «ειδοποιήσης» is not a valid form; the plural accusative is «ειδοποιήσεις», as used in aboutLogins.ftl («τυχόν ειδοποιήσεις παραβιάσεων»).
- `contextual-manager-passwords-remove-all-message-sync` — `browser/browser/contextual-manager.ftl` — Misspelling «ειδοποιήσης» for «ειδοποιήσεις» in both variants.
    - Current: `καθώς και τυχόν ειδοποιήσης παραβίασης`
    - Source: `{$total ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices and remove any breach alerts. You cannot undo this action. [other] This will remove all passwords saved to { -brand…`
    - Suggest: `καθώς και τυχόν ειδοποιήσεις παραβίασης`
    - Same misspelling as in contextual-manager-passwords-remove-all-message; the plural accusative is «ειδοποιήσεις».
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — `default-browser-guidance-notification-body-instruction-win10` quotes “Πρόγραμμα περιήγησης Web” but the string it names, `desktop-entry-generic-name`, reads “Πρόγραμμα περιήγησης”
    - Current: `Βήμα 1: Μεταβείτε στις Ρυθμίσεις > Προεπιλεγμένες εφαρμογές Βήμα 2: Κάντε κύλιση προς τα κάτω στο «Πρόγραμμα περιήγησης Web» Βήμα 3: Επιλέξτε το { -brand-short-name }`
    - Source: `Step 1: Go to Settings > Default apps Step 2: Scroll down to “Web browser” Step 3: Select and choose { -brand-short-name }`
    - Suggest: `Πρόγραμμα περιήγησης`
    - In the source this string quotes “Web browser”, which is exactly the value of `desktop-entry-generic-name` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `taskbar-tabs-media-callout-subtitle-v3` — `browser/browser/featureCallout.ftl` — Missing «σαν» before «μια εφαρμογή».
    - Current: `Εκκινήστε τους ιστοτόπους πολυμέσων σας μια εφαρμογή`
    - Source: `Launch your media sites like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `Εκκινήστε τους ιστοτόπους πολυμέσων σας σαν εφαρμογή`
    - “Launch your media sites like an app” loses the comparative particle, leaving an ungrammatical sequence; the sibling -v3 subtitles all read «σαν εφαρμογή».
- `taskbar-tabs-value-prop-callout-subtitle-v3` — `browser/browser/featureCallout.ftl` — Wrong accusative form «οποιοδήποτε ιστότοπο».
    - Current: `Εκκινήστε οποιοδήποτε ιστότοπο`
    - Source: `Launch any site like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `Εκκινήστε οποιονδήποτε ιστότοπο`
    - «ιστότοπος» is masculine; the masculine accusative of «οποιοσδήποτε» is «οποιονδήποτε», not the neuter «οποιοδήποτε».
- `firefoxview-syncedtabs-adddevice-description-2` — `browser/browser/firefoxView.ftl` — Wrong accusative form «κάποιο άλλο υπολογιστή».
    - Current: `από κάποιο άλλο υπολογιστή`
    - Source: `Sign in to { -brand-product-name } on your phone or another computer to see tabs here. Learn how to <a data-l10n-name="url">connect additional devices</a>.`
    - Suggest: `από κάποιον άλλο υπολογιστή`
    - «υπολογιστής» is masculine, so the determiner must be «κάποιον» in the accusative.
- `ip-protection-bandwidth-warning-infobar-message-90-mb` — `browser/browser/ipProtection.ftl` — Unit “MB” written with Greek letters Μ and Β.
    - Current: `Σας απομένουν { $usageLeft } ΜΒ.`
    - Source: `<strong>You’re almost out of VPN data.</strong> You have { $usageLeft } MB left. Once you use it all, your VPN will pause until your data resets on the first of next month.`
    - Suggest: `Σας απομένουν { $usageLeft } MB.`
    - The unit symbol uses Greek capital Mu and Beta instead of Latin M and B; all other MB/GB occurrences in the file use Latin letters.
- `vpn-error-alert-body` — `browser/browser/ipProtection.ftl` — Wrong verb form «Δοκιμάσετε» instead of the imperative «Δοκιμάστε».
    - Current: `Δοκιμάσετε ξανά αργότερα.`
    - Source: `Try again later.`
    - Suggest: `Δοκιμάστε ξανά αργότερα.`
    - “Try again later.” is an imperative; «Δοκιμάσετε» is a subjunctive/indicative form that cannot stand alone. Every other instance in this file uses «Δοκιμάστε».
- `managed-bookmarks-subfolder` — `browser/browser/places.ftl` — Greek word written with a Latin capital Y homoglyph.
    - Current: `Yποφάκελος`
    - Source: `label: Subfolder`
    - Suggest: `Υποφάκελος`
    - The initial character is Latin U+0059 rather than Greek capital upsilon U+03A5, which breaks search and text-to-speech of an otherwise Greek word.
- `connection-proxy-option-wpad` — `browser/browser/preferences/connection.ftl` — Spelling error: “εεύρεσης”.
    - Current: `Χρήση ρύθμισης αυτόματης εεύρεσης διακομιστή μεσολάβησης ιστού`
    - Source: `accesskey: g label: Use system Web Proxy Auto-Discovery setting`
    - Suggest: `Χρήση ρύθμισης αυτόματης εύρεσης διακομιστή μεσολάβησης ιστού συστήματος`
    - “εεύρεσης” is a typo for “εύρεσης”.
- `permissions-site-app-links-desc` — `browser/browser/preferences/permissions.ftl` — "App links" is rendered as "συνδέσμων από εφαρμογές" (links from apps), which doesn't match the "συνδέσμων εφαρμογών" used in the window title and related strings.
    - Current: `το άνοιγμα συνδέσμων από εφαρμογές`
    - Source: `These sites are blocked from asking to open app links, like email (mailto:). Remove a site to allow it to ask again.`
    - Suggest: `το άνοιγμα συνδέσμων εφαρμογών`
    - App links are links that open an app (e.g. mailto:), not links that come from apps. The window title and permission strings use "συνδέσμων εφαρμογών". The "από" changes the meaning and makes the terminology inconsistent on the same surface.
- `content-blocking-baseline-exceptions-3` — `browser/browser/preferences/preferences.ftl` — Misspelled gerund “άροντας”.
    - Current: `άροντας τον αποκλεισμό μόνο των βασικών στοιχείων`
    - Source: `description: Helps load sites and features by unblocking only essential elements that may contain trackers. Covers most common problems. label: Fix major site issues (recommended)`
    - Suggest: `αίροντας τον αποκλεισμό μόνο των βασικών στοιχείων`
    - The gerund of «αίρω» is «αίροντας»; «άροντας» is not a Greek word.
- `content-blocking-convenience-exceptions-3` — `browser/browser/preferences/preferences.ftl` — Misspelled gerund “άροντας”.
    - Current: `άροντας τον αποκλεισμό των στοιχείων`
    - Source: `description: Restores things like videos in an article or comment sections by unblocking elements that may contain trackers. This can reduce site issues but offers less protection. Must be used with fixes for major issu…`
    - Suggest: `αίροντας τον αποκλεισμό των στοιχείων`
    - The gerund of «αίρω» is «αίροντας»; «άροντας» is not a Greek word.
- `feature-disable-requires-restart` — `browser/browser/preferences/preferences.ftl` — Sentence ends with a doubled full stop.
    - Current: `Θα πρέπει να γίνει επανεκκίνηση του { -brand-short-name } για απενεργοποίηση αυτής της λειτουργίας..`
    - Source: `{ -brand-short-name } must restart to disable this feature.`
    - Suggest: `Θα πρέπει να γίνει επανεκκίνηση του { -brand-short-name } για απενεργοποίηση αυτής της λειτουργίας.`
    - Typographic slip: two periods at the end, while the parallel string feature-enable-requires-restart has one.
- `history-dontremember-description4` — `browser/browser/preferences/preferences.ftl` — Missing second accent in “περιήγησής σας”.
    - Current: `δεν θα διατηρεί το ιστορικό περιήγησης σας`
    - Source: `aria-label: { history-group.label } description: { -brand-short-name } will use the same settings as private browsing, and will not remember any history as you browse the Web.`
    - Suggest: `δεν θα διατηρεί το ιστορικό περιήγησής σας`
    - A proparoxytone noun followed by the enclitic «σας» takes an additional accent on the final syllable; the rest of the file writes «περιήγησής σας» correctly.
- `permissions-block-popups2` — `browser/browser/preferences/preferences.ftl` — Case mismatch: second noun phrase not in the genitive required by “Φραγή”.
    - Current: `Φραγή αναδυόμενων παραθύρων και ανακατευθύνσεις τρίτων`
    - Source: `accesskey: B label: Block pop-ups and third-party redirects`
    - Suggest: `Φραγή αναδυόμενων παραθύρων και ανακατευθύνσεων τρίτων`
    - «Φραγή» governs the genitive; «ανακατευθύνσεις τρίτων» is nominative/accusative and does not agree with the coordinated «αναδυόμενων παραθύρων».
- `preferences-ai-controls-block-confirmation-key-points` — `browser/browser/preferences/preferences.ftl` — Label begins with a Latin capital “K” instead of Greek “Κ”.
    - Current: `Kύρια σημεία στις προεπισκοπήσεις συνδέσμων`
    - Source: `Key points in link previews`
    - Suggest: `Κύρια σημεία στις προεπισκοπήσεις συνδέσμων`
    - Same mixed-script defect: first character is U+004B LATIN CAPITAL LETTER K instead of Greek kappa.
- `preferences-ai-controls-key-points-control` — `browser/browser/preferences/preferences.ftl` — Label begins with a Latin capital “K” instead of Greek “Κ”.
    - Current: `Kύρια σημεία στις προεπισκοπήσεις συνδέσμων`
    - Source: `description: See a quick summary before opening a link. label: Key points in link previews`
    - Suggest: `Κύρια σημεία στις προεπισκοπήσεις συνδέσμων`
    - Mixed-script word: the first character is U+004B LATIN CAPITAL LETTER K, not U+039A GREEK CAPITAL LETTER KAPPA, which breaks search, sorting and screen-reader pronunciation.
- `profiles-cyan-theme-title` — `browser/browser/profiles.ftl` — Missing genitive ending: «θέμα» should be «θέματος».
    - Current: `Εφαρμογή κυανού θέμα`
    - Source: `title: Apply cyan theme`
    - Suggest: `Εφαρμογή κυανού θέματος`
    - Every other theme tooltip in the file uses the genitive «θέματος» after «Εφαρμογή» (e.g. «Εφαρμογή πράσινου θέματος»); the nominative «θέμα» here does not agree with «κυανού».
- `profiles-purple-theme-title` — `browser/browser/profiles.ftl` — «μoβ» is written with a Latin letter o instead of Greek omicron.
    - Current: `Εφαρμογή μoβ θέματος`
    - Source: `title: Apply purple theme`
    - Suggest: `Εφαρμογή μοβ θέματος`
    - The middle character is Latin U+006F, unlike profiles-purple-theme = «Μοβ» which uses the correct Greek omicron.
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — Wrong case after «έως και»: genitive «συσκευών» instead of accusative «συσκευές».
    - Current: `σε έως και { $count } συσκευών`
    - Source: `{$count ->} [other] Using the { -mozilla-vpn-brand-name } encrypts all your traffic and hides your location — on up to { $count } devices. Get the most from your subscription — add it from the <a data-l10n-name="playsto…`
    - Suggest: `σε έως και { $count } συσκευές`
    - The preposition «σε … έως και» requires the accusative; the singular variant of the same message correctly reads «έως και { $count } συσκευή».
- `safeb-blocked-phishing-page-learn-more` — `browser/browser/safebrowsing/blockedSite.ftl` — Adjective does not agree with its noun (missing final -ς)
    - Current: `σχετικά με τους παραπλανητικού ιστοτόπους`
    - Source: `Learn more about deceptive sites and phishing at <a data-l10n-name='learn_more_link'>www.antiphishing.org</a>. Learn more about { -brand-short-name }’s Phishing and Malware Protection at <a data-l10n-name='firefox_suppo…`
    - Suggest: `σχετικά με τους παραπλανητικούς ιστοτόπους`
    - Accusative plural requires «παραπλανητικούς»; «παραπλανητικού» is a genitive singular form and does not agree with «τους ιστοτόπους».
- `tab-context-close-duplicate-tabs2` — `browser/browser/tabContextMenu.ftl` — "Close Duplicates of This Tab" is rendered with a bare genitive «καρτέλας», which is ungrammatical and loses "this".
    - Current: `Κλείσιμο διπλότυπων καρτέλας`
    - Source: `accesskey: x label: Close Duplicates of This Tab`
    - Suggest: `Κλείσιμο διπλότυπων αυτής της καρτέλας`
    - A genitive noun without an article cannot follow «διπλότυπων» here; as written the label reads as a fragment and no longer says the duplicates are of the current tab.
- `translations-manage-error-remove` — `browser/browser/translations.ftl` — Article without the required final nu before a vowel: «τη αφαίρεση».
    - Current: `κατά τη αφαίρεση`
    - Source: `There was an error removing the language files. Please try again.`
    - Suggest: `κατά την αφαίρεση`
    - Greek requires «την» before a word beginning with a vowel; the parallel string translations-manage-error-download uses the correct form «κατά τη λήψη» (consonant) so the omission here is an error, not a convention.
- `geolocation.systemSettingsTitle` — `browser/chrome/browser/browser.properties` — Ungrammatical case after the preposition «για»
    - Current: `Σε αναμονή για άδειας τοποθεσίας`
    - Source: `Awaiting Location Permission`
    - Suggest: `Σε αναμονή για άδεια τοποθεσίας`
    - «για» requires the accusative («άδεια»); the genitive «άδειας» is a plain declension error in a user-visible dialog title.
- `copyFunction.label` — `devtools/client/debugger.properties` — JavaScript “function” rendered as «λειτουργία» (feature/operation) instead of «συνάρτηση».
    - Current: `Αντιγραφή λειτουργίας`
    - Source: `Copy function`
    - Suggest: `Αντιγραφή συνάρτησης`
    - Elsewhere in the same panel the debugger correctly uses «συνάρτηση» (outline.placeholder.functions, symbolSearch.search.functionsPlaceholder); «λειτουργία» makes the menu item read as “Copy operation”.
- `outline.noFunctions` — `devtools/client/debugger.properties` — “No functions” rendered with «λειτουργία» instead of «συνάρτηση».
    - Current: `Καμία λειτουργία`
    - Source: `No functions`
    - Suggest: `Καμία συνάρτηση`
    - The Outline pane filter directly above says «Φιλτράρισμα συναρτήσεων», so the empty state uses a different (and wrong) word for the same objects in the same surface.
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “Τοπικής λειτουργίας” but the string it names, `options-local-mode-label`, reads “Τοπική λειτουργία”
    - Current: `Μπορείτε επίσης να φορτώσετε αυτό το έγγραφο από το «{ $url }» μέσω της «Τοπικής λειτουργίας» των εργαλείων ανάπτυξης, η οποία μπορεί να ενεργοποιηθεί στον πίνακα ρυθμίσεων.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Τοπική λειτουργία`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `clientSendOOBTitle` — `devtools/shared/debugger.properties` — “Client” is «δέκτης» here but «πελάτης» in the paired dialog in the same file.
    - Current: `Αναγνώριση δέκτη`
    - Source: `Client Identification`
    - Suggest: `Αναγνώριση πελάτη`
    - serverReceiveOOBTitle in the same authentication flow uses «πελάτη» for the same actor, so the two dialogs appear to talk about different parties.
- `MediaStreamAudioSourceNodeCrossOrigin` — `dom/chrome/dom/dom.properties` — Wrong API name: createMediaElementSource instead of createMediaStreamSource.
    - Current: `Το MediaStream, που πέρασε στο createMediaElementSource`
    - Source: `The MediaStream passed to createMediaStreamSource has a cross-origin resource, the node will output silence.`
    - Suggest: `Το MediaStream, που πέρασε στο createMediaStreamSource`
    - The developer comment says “Do not translate MediaStream and createMediaStreamSource”; the Greek names the wrong (copy-pasted) API, sending developers to the wrong call site.
- `PEBadSelectorRSIgnored` — `dom/chrome/layout/css.properties` — “bad selector” rendered as “bad choice”.
    - Current: `Η ομάδα κανόνων αγνοήθηκε λόγω κακής επιλογής.`
    - Source: `Ruleset ignored due to bad selector.`
    - Suggest: `Η ομάδα κανόνων αγνοήθηκε λόγω εσφαλμένου επιλογέα.`
    - «επιλογή» means choice, not selector; the file elsewhere uses «επιλογέας». The same slip appears in PEBadSelectorKeyframeRuleIgnored.
- `CreateWrapperDenied` — `dom/chrome/security/caps.properties` — Half of the message is left in English.
    - Current: `Άρνηση πρόσβασης για τη δημιουργία wrapper for object of class %S`
    - Source: `Permission denied to create wrapper for object of class %S`
    - Suggest: `Άρνηση δικαιώματος για τη δημιουργία wrapper για το αντικείμενο της κλάσης %S`
    - The adjacent CreateWrapperDeniedForOrigin translates the same phrase fully; here “for object of class” remains English inside an otherwise Greek sentence.
- `load-module-help-root-certs-module-name` — `security/manager/security/certificates/deviceManager.ftl` — A do-not-translate literal was translated.
    - Current: `Το ‘Πιστοποιητικά Ρίζας‘ είναι δεσμευμένο`
    - Source: `value: ‘Root Certs‘ is reserved and cannot be used as the module name.`
    - Suggest: `Το ‘Root Certs‘ είναι δεσμευμένο`
    - The developer comment states “Do not translate 'Root Certs'”; it is the literal reserved module name the user must avoid typing, so the translated form tells them the wrong reserved string.
- `addon-updates-installed` — `toolkit/toolkit/about/aboutAddons.ftl` — Missing the required second accent on “πρόσθετα” before the enclitic “σας”.
    - Current: `Τα πρόσθετα σας ενημερώθηκαν.`
    - Source: `Your add-ons have been updated.`
    - Suggest: `Τα πρόσθετά σας ενημερώθηκαν.`
    - Greek orthography requires a second accent on a proparoxytone noun followed by an enclitic possessive; the tree writes “πρόσθετά σας” correctly elsewhere (e.g. blockedSite.ftl, aboutAddons line 111).
- `details-notification-incompatible2` — `toolkit/toolkit/about/aboutAddons.ftl` — The brand name takes a masculine article against the locale's neuter convention.
    - Current: `ασύμβατο με τον { -brand-short-name } { $version }`
    - Source: `message: { $name } is incompatible with { -brand-short-name } { $version }.`
    - Suggest: `ασύμβατο με το { -brand-short-name } { $version }`
    - The tree treats the brand as neuter (“το { -brand-short-name }”) in 267+ places; masculine “τον” occurs only 3 times tree-wide, including this one.
- `extensions-warning-update-security2` — `toolkit/toolkit/about/aboutAddons.ftl` — A double space appears between two words in the visible message.
    - Current: `ενημερώσεων  προσθέτων`
    - Source: `message: Add-on update security checking is disabled. You may be compromised by updates.`
    - Suggest: `ενημερώσεων προσθέτων`
    - Two consecutive spaces inside the user-visible warning text render as a visible gap.
- `list-empty-recent-updates` — `toolkit/toolkit/about/aboutAddons.ftl` — Missing the required second accent on “πρόσθετα” before the enclitic “σας”.
    - Current: `κάποιο από τα πρόσθετα σας`
    - Source: `value: You haven’t recently updated any add-ons`
    - Suggest: `κάποιο από τα πρόσθετά σας`
    - Same orthographic rule as addon-updates-installed; the enclitic “σας” requires the second accent.
- `about-telemetry-page-subtitle` — `toolkit/toolkit/about/aboutTelemetry.ftl` — The brand name takes a masculine article against the locale's neuter convention.
    - Current: `να βελτιώσουμε τον { -brand-full-name }`
    - Source: `This page shows the information about performance, hardware, usage and customizations collected by Telemetry. This information is submitted to { $telemetryServerOwner } to help improve { -brand-full-name }.`
    - Suggest: `να βελτιώσουμε το { -brand-full-name }`
    - Same agreement issue as aboutAddons: the locale consistently uses the neuter article with the brand name.
- `about-webauthn-ctap2-enroll-feedback-merge-failure` — `toolkit/toolkit/about/aboutWebauthn.ftl` — The sentence begins with a genitive “Αποτυχίας” where the nominative is required.
    - Current: `Αποτυχίας συγχώνευσης δείγματος.`
    - Source: `Sample merge failure.`
    - Suggest: `Αποτυχία συγχώνευσης δείγματος.`
    - en-US “Sample merge failure.” is a nominal phrase; the head noun must be nominative “Αποτυχία”, as in the neighbouring feedback strings.
- `about-webrtc-aec-logging-toggled-on-state-msg` — `toolkit/toolkit/about/aboutWebrtc.ftl` — “τον καλών” is an ungrammatical form for “the caller”.
    - Current: `μιλήστε με τον καλών`
    - Source: `AEC logging active (speak with the caller for a few minutes and then stop the capture)`
    - Suggest: `μιλήστε με τον συνομιλητή σας`
    - “καλών” is a nominative/genitive-plural form and cannot follow the accusative article “τον”; the accusative would be “τον καλούντα”.
- `about-webrtc-sdp-set-at-timestamp-local` — `toolkit/toolkit/about/aboutWebrtc.ftl` — “Ορισμός Τοπικό SDP” lacks case agreement after the noun “Ορισμός”.
    - Current: `Ορισμός Τοπικό SDP στη χρονική σήμανση`
    - Source: `Set Local SDP at timestamp { $timestamp }`
    - Suggest: `Ορισμός τοπικού SDP στη χρονική σήμανση`
    - A noun governing a complement requires the genitive (“Ορισμός τοπικού SDP”); the nominative/accusative “Τοπικό SDP” plus the mid-sentence capital is ungrammatical.
- `about-webrtc-sdp-set-at-timestamp-remote` — `toolkit/toolkit/about/aboutWebrtc.ftl` — “Ορισμός Απομακρυσμένο SDP” lacks case agreement after the noun “Ορισμός”.
    - Current: `Ορισμός Απομακρυσμένο SDP στη χρονική σήμανση`
    - Source: `Set Remote SDP at timestamp { $timestamp }`
    - Suggest: `Ορισμός απομακρυσμένου SDP στη χρονική σήμανση`
    - Same agreement error as the local-SDP header: the complement of “Ορισμός” must be genitive.
- `about-webrtc-user-modified-configuration-heading` — `toolkit/toolkit/about/aboutWebrtc.ftl` — The heading starts with a Latin capital “T” instead of the Greek “Τ”.
    - Current: `Tροποποιημένη διαμόρφωση WebRTC χρήστη`
    - Source: `User Modified WebRTC Configuration`
    - Suggest: `Τροποποιημένη διαμόρφωση WebRTC χρήστη`
    - The first character is U+0054 LATIN CAPITAL LETTER T inside a Greek word; it breaks search, sorting and may render with a different font. Verified by matching Latin letters adjacent to Greek letters in the file.

### E. Typography, punctuation & spacing

- `about-logins-menu-menuitem-export-logins2` — `browser/browser/aboutLogins.ftl` — `about-logins-menu-menuitem-export-logins2` uses three dots where this locale uses …
    - Current: `Εξαγωγή κωδικών πρόσβασης...`
    - Source: `Export Passwords…`
    - The tree uses … 398 times against 2 ASCII runs.
- `bar-tooltip-social` — `browser/browser/protections.ftl` — The plural variant of the aria-label is missing the opening parenthesis before the percentage.
    - Current: `ιχνηλάτες κοινωνικών δικτύων { $percentage }%)`
    - Source: `aria-label: {$count ->} [one] { $count } social media tracker ({ $percentage }%) [other] { $count } social media trackers ({ $percentage }%) title: Social Media Trackers`
    - Suggest: `ιχνηλάτες κοινωνικών δικτύων ({ $percentage }%)`
    - Every other variant and every other bar-tooltip-* message wraps the percentage in parentheses; here only the closing one is present, so the screen reader announces an unbalanced string.
- `monitor-partial-breaches-title` — `browser/browser/protections.ftl` — Missing space between the number placeholder and the following word in the plural variant.
    - Current: `{ $numBreachesResolved }από { $numBreaches } παραβιάσεις`
    - Source: `{$numBreaches ->} [other] { $numBreachesResolved } out of { $numBreaches } breaches marked as resolved`
    - Suggest: `{ $numBreachesResolved } από { $numBreaches } παραβιάσεις`
    - The rendered text runs the count into «από» (e.g. "3από 5 παραβιάσεις"); the singular variant in the same message has the space.
- `MUI_UNTEXT_WELCOME_INFO_TEXT` — `browser/installer/mui.properties` — Stray space between the brand variable and the full stop.
    - Current: `δεν εκτελείται το $BrandFullNameDA .`
    - Source: `This wizard will guide you through the uninstallation of $BrandFullNameDA.  Before starting the uninstallation, make sure $BrandFullNameDA is not running.  $_CLICK`
    - Suggest: `δεν εκτελείται το $BrandFullNameDA.`
    - The space before the period is visible in the uninstaller wizard text; en-US has no space there.
- `accessibility-text-label-issue-glyph` — `devtools/client/accessibility.ftl` — Missing space between the word and the element name.
    - Current: `για επισήμανση στοιχείων<span>mglyph</span>`
    - Source: `Use <code>alt</code> attribute to label <span>mglyph</span> elements. <a>Learn more</a>`
    - Suggest: `για επισήμανση στοιχείων <span>mglyph</span>`
    - The rendered sentence shows “στοιχείωνmglyph” with no space between two words.
- `MathML_DeprecatedMathVariantWarning` — `dom/chrome/dom/dom.properties` — Closing single quote dropped from the code literal.
    - Current: `Το «mathvariant='%S» σε στοιχεία MathML`
    - Source: `“mathvariant='%S'” on MathML elements is deprecated and will be removed at a future date.`
    - Suggest: `Το «mathvariant='%S'» σε στοιχεία MathML`
    - The source literal is “mathvariant='%S'”; the trailing apostrophe is missing, so the quoted attribute value shown to developers is malformed.
- `CompositorAnimationWarningContentTooLarge2` — `dom/chrome/layout/layout_errors.properties` — Period instead of comma between the two frame-size values.
    - Current: `(%1$S. %2$S)`
    - Source: `Animation cannot be run on the compositor because the frame size (%1$S, %2$S) is too large relative to the viewport (larger than (%3$S, %4$S)) or larger than the maximum allowed value (%5$S, %6$S)`
    - Suggest: `(%1$S, %2$S)`
    - The pair is a width/height tuple, printed as “(%1$S, %2$S)” in en-US and as “(%3$S, %4$S)” later in the same Greek string; the stray period makes the first pair read inconsistently.
- `about-networking-http-clear-cache-button` — `toolkit/toolkit/about/aboutNetworking.ftl` — “Cache” is translated two different ways on the same page.
    - Current: `Απαλοιφή προσωρινής μνήμης HTTP`
    - Source: `Clear HTTP Cache`
    - Suggest: `Απαλοιφή κρυφής μνήμης HTTP`
    - The adjacent DNS button and the rest of the page use “κρυφή μνήμη” for cache; the two renderings sit side by side in the same UI.
- `about-reader-character-spacing-label` — `toolkit/toolkit/about/aboutReader.ftl` — “Character spacing” uses “διάστιχο”, which specifically means line spacing.
    - Current: `Διάστιχο χαρακτήρων`
    - Source: `label: Character spacing`
    - Suggest: `Διάστημα χαρακτήρων`
    - “Διάστιχο” is the term for leading/line spacing and is correctly used for about-reader-line-spacing-label in the same menu; applying it to characters conflates two different controls.
- `about-reader-word-spacing-label` — `toolkit/toolkit/about/aboutReader.ftl` — “Word spacing” uses “διάστιχο”, which specifically means line spacing.
    - Current: `Διάστιχο λέξεων`
    - Source: `label: Word spacing`
    - Suggest: `Διάστημα λέξεων`
    - Same conflation as character spacing: “διάστιχο” denotes line spacing, already used for the line-spacing control in the same menu.
- `effective-content-sandbox-level` — `toolkit/toolkit/about/aboutSupport.ftl` — “Content Process” becomes “content processing/editing” and the word order garbles the term.
    - Current: `Αποτελεσματικό επίπεδο επεξεργασίας περιεχομένου sandbox`
    - Source: `Effective Content Process Sandbox Level`
    - Suggest: `Ισχύον επίπεδο sandbox διεργασίας περιεχομένου`
    - “επεξεργασία” means processing/editing, not “process” (“διεργασία”), which is how the adjacent content-sandbox-level renders the same term; the label as written does not name the content process.
- `media-codec-support-error` — `toolkit/toolkit/about/aboutSupport.ftl` — “Codec support information” becomes “encoding support information”, inconsistent with the heading on the same page.
    - Current: `Οι πληροφορίες υποστήριξης κωδικοποίησης δεν είναι διαθέσιμες.`
    - Source: `Codec support information unavailable. Try again after playing back a media file.`
    - Suggest: `Οι πληροφορίες υποστήριξης codec δεν είναι διαθέσιμες.`
    - media-codec-support-info on the same page renders the same term as “Πληροφορίες υποστήριξης codec”; the table covers both decoding and encoding, so “κωδικοποίησης” is wrong here.
- `about-telemetry-slow-sql-main` — `toolkit/toolkit/about/aboutTelemetry.ftl` — “Slow SQL statements” becomes “statements of slow SQL”, attaching “slow” to SQL instead of the statements.
    - Current: `Εντολές αργής SQL στο κύριο νήμα`
    - Source: `Slow SQL Statements on Main Thread`
    - Suggest: `Αργές εντολές SQL στο κύριο νήμα`
    - The section heading about-telemetry-slow-sql-section renders the same term correctly as “Αργές εντολές SQL”; here the adjective modifies the language rather than the statements.
- `third-party-detail-occurrences` — `toolkit/toolkit/about/aboutThirdParty.ftl` — “Module” is rendered as “add-on” in the tooltip, naming a different Firefox concept.
    - Current: `Αριθμός φορτώσεων αυτού του προσθέτου.`
    - Source: `(value): Occurrences title: How many times this module was loaded.`
    - Suggest: `Αριθμός φορτώσεων αυτής της μονάδας.`
    - The page is about third-party Windows modules (“λειτουργικές μονάδες”), not add-ons; the same substitution occurs in third-party-detail-duration, third-party-tag-ime and third-party-tag-shellex.
- `third-party-tag-background` — `toolkit/toolkit/about/aboutThirdParty.ftl` — “This module” is rendered as “this add-on” in the tooltip.
    - Current: `Αυτό το πρόσθετο δεν απέκλεισε την εφαρμογή`
    - Source: `(value): Background title: This module did not block the application because it was loaded in the background.`
    - Suggest: `Αυτή η μονάδα δεν απέκλεισε την εφαρμογή`
    - Same term error as third-party-detail-occurrences: “πρόσθετο” is Firefox's word for add-on, a different object from the injected module this row describes.
- `certificate-viewer-organization` — `toolkit/toolkit/about/certviewer.ftl` — The certificate field “Organization” is narrowed to “company”.
    - Current: `Εταιρεία`
    - Source: `Organization`
    - Suggest: `Οργανισμός`
    - The O field can hold any organization, not only a company, and the adjacent “Organizational Unit” is rendered with “οργανισμού”, so the same source term appears two ways in one panel.
- `unknowncontenttype-other` — `toolkit/toolkit/global/unknownContentType.ftl` — `unknowncontenttype-other` uses three dots where this locale uses …
    - Current: `Άλλο...`
    - Source: `label: Other…`
    - The tree uses … 398 times against 2 ASCII runs.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/el/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
