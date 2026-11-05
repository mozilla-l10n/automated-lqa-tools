# Firefox l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-11-05 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `324a294b9f2a` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9251d435ac24` |
| **Previous run** | 2026-11-05 @ `181c4859abf3` |
| **Mode** | incremental |
| **Strings reviewed this run** | 130 of 16,755 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fy-NL: [Firefox for Android](android.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (8)

- `inactive-css-at-position-try-not-supported` — `devtools/client/tooltips.ftl` — Translation inserts 'yn de folgjende browsers' (in the following browsers), which the source does not contain.
    - Current: `wurdt net stipe yn de folgjende browsers <strong>@position-try</strong>-regels.`
    - Source: `<strong>{ $property }</strong> is not supported in <strong>@position-try</strong> rules.`
    - Suggest: `wurdt net stipe yn <strong>@position-try</strong>-regels.`
    - The source says the property is not supported in @position-try rules. The Frisian says 'not supported in the following browsers @position-try rules', which is wrong and garbled.
- `addon-badge-line4` — `toolkit/toolkit/about/aboutAddons.ftl` — 'Firefox' added after 'Mozilla', though the developer comment says only 'Mozilla' is fixed so that forks don't show a different maker.
    - Current: `troch Mozilla Firefox boude`
    - Source: `title: Official extension built by Mozilla. Meets security and performance standards`
    - Suggest: `troch Mozilla boude`
    - The source says 'built by Mozilla'. The developer comment explains that 'Mozilla' is fixed text so forks don't display their own name. Adding 'Firefox' brings in a product brand the source deliberately left out.
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — Argument name written 'URLSTRING' in the explanation, which doesn't match 'URL_STRING' in the usage line.
    - Current: `argumint URLSTRING`
    - Source: `:block URL_STRING  Start blocking network requests    It accepts only one URL_STRING argument, an unquoted string which will be used to block all requests whose URL includes this string.   Use :unblock or the Network Mo…`
    - Suggest: `argumint URL_STRING`
    - The usage line and the source both name the argument URL_STRING. The explanation should refer to it the same way.
- `set-password-message` — `security/manager/security/pippki/pippki.ftl` — Typo 'reserverkopybestân' instead of 'reservekopybestân'.
    - Current: `reserverkopybestân`
    - Source: `The certificate backup password you set here protects the backup file that you are about to create. You must set this password to proceed with the backup.`
    - Suggest: `reservekopybestân`
    - The word for backup is 'reservekopy', which is spelled correctly earlier in the same string. The extra 'r' is a spelling error.
- `page-info-page` — `browser/browser/pageInfo.ftl` — 'Sydeynfo' uses 'syd' (side) instead of 'side' (page) for Page Info.
    - Current: `Sydeynfo`
    - Source: `title: Page Info — { $website }`
    - Suggest: `Side-ynfo`
    - In Frisian, 'page' is 'side', while 'syd' means side, as in 'sydbalke' (sidebar). 'Sydeynfo' is a misspelling of Page Info.
- `sidebar-callout-survey-features-question` — `browser/browser/featureCallout.ftl` — Preposition 'in' should be Frisian 'yn'.
    - Current: `produktiviteit in { -brand-short-name }`
    - Source: `The following are potential sidebar features. Which would improve your productivity in { -brand-short-name } the most?`
    - Suggest: `produktiviteit yn { -brand-short-name }`
    - The Frisian preposition for 'in' is 'yn', which is used correctly elsewhere in the batch. 'in' here is a spelling error.
- `taskbar-tabs-spotlight-subtitle` — `browser/browser/newtab/asrouter.ftl` — The adjective has the wrong ending: 'finster' is a neuter noun, so after 'in' the adjective takes no -e.
    - Current: `in ferienfâldige finster`
    - Source: `One click launches your most used sites in a streamlined window with all of { -brand-short-name }’s protections.`
    - Suggest: `in ferienfâldich finster`
    - In Frisian, 'finster' takes the article 'it', which makes it neuter. When a neuter noun follows the indefinite article 'in', the adjective before it has no -e ending (for example 'in grut finster'). So 'ferienfâldige' should be 'ferienfâldich'.
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — The word “major” is missing, so the Frisian says Firefox is the only browser of any kind backed by a non-profit.
    - Current: `de iennige browser dy’t stipe wurdt`
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
    - Suggest: `de iennige grutte browser dy’t stipe wurdt`
    - The en-US says “the only major browser backed by a non-profit”. Without “major” (grutte), the Frisian makes a broader factual claim than the source.

### ✅ Fixed since the last run (89)

- `confirm-discard-changes-dialog-title` — `browser/browser/aboutLogins.ftl` — Dizze wizigingen ferwerpe? → Net-bewarre wizigingen ferwerpe?
    - Current: `Dizze wizigingen ferwerpe?`
    - Source: `Discard unsaved changes?`
    - Suggest: `Net-bewarre wizigingen ferwerpe?`
- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — "or clear all of your data" is rendered as "and do not erase all your data", which in Frisian reads as if not all data is erased, but the negation placement changes the claim.
    - Current: `Se meitsje jo net anonym en wiskje al jo gegevens net.`
    - Source: `Private Windows help keep your browsing private from others on this device. They don’t make you anonymous or clear all of your data.`
    - Suggest: `Se meitsje jo net anonym en wiskje net al jo gegevens.`
    - The source says Private Windows do not make you anonymous or clear all of your data. Placing 'net' after 'al jo gegevens' yields the ambiguous/incorrect scope 'they do not erase all your data'; the negation should precede the quantifier.
- `default-browser-guidance-notification-info-page` — `browser/browser/defaultBrowserNotification.ftl` — Toane: → Sjen litte
    - Current: `Toane:`
    - Source: `Show me`
    - Suggest: `Sjen litte`
- `taskbar-tabs-spotlight-subtitle` — `browser/browser/newtab/asrouter.ftl` — The English word "streamlined" was left untranslated inside an otherwise Frisian sentence.
    - Current: `in streamlined finster`
    - Source: `One click launches your most used sites in a streamlined window with all of { -brand-short-name }’s protections.`
    - Suggest: `in ferienfâldige finster`
    - The rest of the sentence is translated, but the English adjective "streamlined" was left as is. Frisian readers won't recognise it, and the locale translates terms like this everywhere else.
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — meitjse → meitsje (letters transposed)
    - Current: `meitjse`
    - Source: `Upgrading to Windows 11? Let’s back up your { -brand-product-name } data.`
    - Suggest: `meitsje`
- `policy-BlockAboutProfiles2` — `browser/browser/policies/policies-descriptions.ftl` — The parentheses around about:profiles are missing.
    - Current: `Oer profilen about:profiles blokkearje`
    - Source: `Block access to About Profiles (about:profiles).`
    - Suggest: `Oer profilen (about:profiles) blokkearje`
    - The en-US puts the URL in parentheses, and the companion string policy-BlockAboutConfig2 keeps them. Without them the page name and the URL run together.
- `inactive-css-not-grid-or-flex-container-or-multicol-container-fix` — `devtools/client/tooltips.ftl` — CSS keyword garbled: colums:2 → columns:2
    - Current: `colums:2`
    - Source: `Try adding either <strong>display:grid</strong>, <strong>display:flex</strong>, or <strong>columns:2</strong>. { learn-more }`
    - Suggest: `columns:2`
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — CSS property translated inside <strong>: lettertypegrutte → font-size
    - Current: `lettertypegrutte`
    - Source: `Try changing the <strong>font-size</strong> of the ruby text. { learn-more }`
- `SVGUseInlineEventHandlerWarning` — `dom/chrome/dom/dom.properties` — The space between 'SVG' and '<use>' is missing.
    - Current: `SVG<use>-elemint`
    - Source: `Inline event handlers on elements cloned by an SVG <use> element are not interoperable. See https://github.com/w3c/svgwg/issues/1211`
    - Suggest: `SVG <use>-elemint`
    - The source has 'an SVG <use> element' with a space. Running 'SVG' and '<use>' together is a typo.
- `about-glean-button-dictionary-link` — `toolkit/toolkit/about/aboutGlean.ftl` — Comment: "Docs" = documentation. Dokuminten → Dokumintaasje
    - Current: `Dokuminten`
    - Source: `Docs`
    - Suggest: `Dokumintaasje`
- `app-basics-update-dir` — `toolkit/toolkit/about/aboutSupport.ftl` — Comment says "Update" is a noun. Map fernije → Fernijingsmap (both variants)
    - Current: `Map fernije`
    - Source: `{$sel_1 ->} [linux] Update Directory [other] Update Folder`
    - Suggest: `Fernijingsmap`
- `sec-error-ocsp-bad-signature` — `toolkit/toolkit/neterror/nsserrors.ftl` — OCSP response left in English; the file uses OCSP-antwurd
    - Current: `OCSP response`
    - Source: `OCSP response has an invalid signature.`
- `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Select the plus sign button above to add a password now. You can also <a data-l10n-name="import-browser-link">import passwords from another browser</a> or <a data-l10n-name="import-file-link">from a file</a>.`
- `about-unloads-last-updated` — `browser/browser/aboutUnloads.ftl` — Left in English: "Last updated: …"
    - Source: `Last updated: { $date }`
- `appmenuitem-monitor-description2` — `browser/browser/appmenu.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Get alerts about data breaches`
- `profiler-popup-presets-networking-with-logs-description` — `browser/browser/appmenu.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Preset for investigating networking bugs in { -brand-shorter-name }, including networking logs. These logs may contain sensitive information such as the URLs you visit.`
- `filepicker-blocked-infobar` — `browser/browser/browser.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Your organization has blocked access to local files on this computer`
- `quickactions-cmd-manageai` — `browser/browser/browser.ftl` — Also: quickactions-cmd-manageai (browser/browser/browser.ftl) lists ai útskeakelje, ai útskeakelje, ai beheare — the first keyword is duplicated, so one of en-US's three search keywords ("off ai") is unreachable.
    - Source: `disable ai, off ai, manage ai`
- `default-browser-guidance-notification-info-page` — `browser/browser/defaultBrowserNotification.ftl` — Added: import-source-page-title · findbar-fast-find-links.placeholder · app-basics-disk-available · detail-rating.value · default-browser-guidance-notification-info-page · inactive-css-at-position-try-not-supported.
    - Source: `Show me`
- `bookmark-overlay-tags-empty-description` — `browser/browser/editBookmarkOverlay.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `placeholder: Separate tags with commas`
- `sidebar-callout-survey-features-question` — `browser/browser/featureCallout.ftl` — in { -brand-short-name } → yn { -brand-short-name }
    - Current: `in { -brand-short-name }`
    - Source: `The following are potential sidebar features. Which would improve your productivity in { -brand-short-name } the most?`
    - Suggest: `yn { -brand-short-name }`
- `firefox-relay-and-fxa-popup-notification-second-sentence-with-domain-and-value-prop` — `browser/browser/firefoxRelay.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `First, sign up or sign in to your account to use an email mask.`
- `genai-chatbot-summarize-footer-generic-subtitle` — `browser/browser/genai.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Add an AI chatbot to the { -brand-short-name } sidebar to quickly summarize pages.`
- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `description: Get extra privacy by hiding your location while browsing. label: Built-in VPN`
- `ipprotection-feature-introduction-link-text-privacy-3` — `browser/browser/ipProtection.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Get <a data-l10n-name="learn-more-vpn">extra privacy</a> by choosing from multiple locations to hide where you browse.`
- `ipprotection-site-settings-callout-subtitle` — `browser/browser/ipProtection.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Turn VPN off for a specific site and we’ll remember it next time you visit.`
- `home-mode-choice-custom-srd` — `browser/browser/newtab/newtab.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `label: Custom URLs…`
- `newtab-widget-lists-menu-delete` — `browser/browser/newtab/newtab.ftl` — website-remove-language-button.aria-label and .title (en-US: "Remove { $locale }") · newtab-widget-lists-menu-delete (en-US: "Delete this list") · delete-ca-cert-confirm (en-US is declarative).
    - Source: `Delete this list`
    - Suggest: `.title`
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Upgrading to Windows 11? Let’s back up your { -brand-product-name } data.`
- `mr1-onboarding-theme-description-dark` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `aria-description: Use a dark theme for buttons, menus, and windows.`
    - Suggest: `‘Root Certs‘`
- `mr1-onboarding-theme-description-light` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `aria-description: Use a light theme for buttons, menus, and windows.`
    - Suggest: `‘Root Certs‘`
- `mr1-onboarding-theme-tooltip-dark` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `title: Use a dark theme for buttons, menus, and windows.`
    - Suggest: `‘Root Certs‘`
- `mr1-onboarding-theme-tooltip-light` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `title: Use a light theme for buttons, menus, and windows.`
    - Suggest: `‘Root Certs‘`
- `onboarding-gratitude-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Thank you for using { -brand-short-name }, backed by the Mozilla Foundation. With your support, we’re working to make the internet safer and more accessible for everyone.`
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
- `onboarding-refresh-import-title` — `browser/browser/newtab/onboarding.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Make { -brand-short-name } feel more like home`
- `page-info-frame` — `browser/browser/pageInfo.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
    - Source: `title: Frame Info — { $website }`
- `page-info-page` — `browser/browser/pageInfo.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
    - Source: `title: Page Info — { $website }`
- `policy-DefaultDownloadDirectory` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Set the default download directory.`
- `policy-DisableThirdPartyModuleBlocking` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Prevent the user from blocking third-party modules that get injected into the { -brand-short-name } process.`
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Configure default application handlers.`
- `policy-LegacyProfiles` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Disable the feature enforcing a separate profile for each installation.`
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `label: { $locale } [{ $code }]`
- `confirm-browser-language-change-description` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Restart { -brand-short-name } to apply these changes`
- `forms-master-pw-fips-desc` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Password Change Failed`
- `home-mode-choice-custom` — `browser/browser/preferences/preferences.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `label: Custom URLs…`
- `home-prefs-weather-description` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Today’s forecast at a glance`
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `To add a site, open the <img data-l10n-name="translations-icon"/> translation panel, select <img data-l10n-name="settings-icon"/> translation settings, then choose “Never translate this site”`
- `website-remove-language-button` — `browser/browser/preferences/preferences.ftl` — website-remove-language-button.aria-label and .title (en-US: "Remove { $locale }") · newtab-widget-lists-menu-delete (en-US: "Delete this list") · delete-ca-cert-confirm (en-US is declarative).
    - Source: `aria-label: Remove { $locale } title: Remove { $locale }`
    - Suggest: `.title`
- `monitor-header-content-signed-in` — `browser/browser/protections.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `{ -monitor-brand-name } warns you if your info has appeared in a known data breach.`
- `add-engine-button` — `browser/browser/search.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
    - Source: `Add Custom Engine`
- `spotlight-focus-promo-subtitle` — `browser/browser/spotlight.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Scan the QR code to download.`
- `protocolhandler-mailto-handler-set` — `browser/browser/webProtocolHandler.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `Use <strong>{ -brand-short-name } to open { $url }</strong> every time you click a link that opens your email?`
    - Suggest: `‘Root Certs‘`
- `perftools-presets-networking-with-logs-description` — `devtools/client/perftools.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Preset for investigating networking bugs in { -brand-shorter-name }, including networking logs. These logs may contain sensitive information such as the URLs you visit.`
- `storage-cookie-create-error` — `devtools/client/storage.ftl` — storage-cookie-create-error, storage-cookie-edit-error (devtools/client/storage.ftl) · toolbox-meatball-menu-pseudo-locale-accented (devtools/client/toolbox.ftl).
    - Source: `Cookie could not be created: “{ $errorString }”.`
- `storage-cookie-edit-error` — `devtools/client/storage.ftl` — storage-cookie-create-error, storage-cookie-edit-error (devtools/client/storage.ftl) · toolbox-meatball-menu-pseudo-locale-accented (devtools/client/toolbox.ftl).
    - Source: `Cookie could not be updated: “{ $errorString }”.`
- `toolbox-meatball-menu-pseudo-locale-accented` — `devtools/client/toolbox.ftl` — storage-cookie-create-error, storage-cookie-edit-error (devtools/client/storage.ftl) · toolbox-meatball-menu-pseudo-locale-accented (devtools/client/toolbox.ftl).
    - Source: `Enable “accented” locale`
- `inactive-css-at-position-try-not-supported` — `devtools/client/tooltips.ftl` — Text from the browser-compat message spliced in: "…net stipe yn de folgjende browsers @position-try-regels:"
    - Source: `<strong>{ $property }</strong> is not supported in <strong>@position-try</strong> rules.`
- `inactive-css-at-position-try-not-supported` — `devtools/client/tooltips.ftl` — Added: import-source-page-title · findbar-fast-find-links.placeholder · app-basics-disk-available · detail-rating.value · default-browser-guidance-notification-info-page · inactive-css-at-position-try-not-supported.
    - Source: `<strong>{ $property }</strong> is not supported in <strong>@position-try</strong> rules.`
- `inactive-css-first-letter-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `<strong>{ $property }</strong> is not supported on ::first-letter pseudo-elements.`
- _…and 29 more._

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
| Files | 331 |
| Strings | 16,755 |
| Missing strings | 105 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 1 |

### Completeness

**105 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/onboarding.ftl` — 22
- `toolkit/toolkit/about/aboutProcesses.ftl` — 19
- `browser/browser/tabContextMenu.ftl` — 14
- `browser/browser/appExtensionFields.ftl` — 11
- `toolkit/toolkit/downloads/downloadUI.ftl` — 10
- `browser/browser/contextual-manager.ftl` — 8
- `browser/browser/preferences/preferences.ftl` — 5
- `browser/browser/newtab/newtab.ftl` — 4
- `browser/browser/tabbrowser.ftl` — 3
- `dom/chrome/security/security.properties` — 2
- `toolkit/toolkit/firefoxlabs/features.ftl` — 2
- `browser/browser/genai.ftl` — 2

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 814, `straight-double` 26, `curly-double` 16 | **curly-single** |
| apostrophe | `typographic` 1518 | **typographic** |
| ellipsis | `char` 402 | **char** |
| dash | `em` 12, `en` 86 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (402)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 4 |
| 2 | Wrong content (says something other than the English) | 118 |
| 3 | Degraded language (grammar, spelling, terminology) | 252 |
| 4 | Cosmetic (typography, spacing) | 28 |

### A. Functional, markup, variables & plurals

- `error-try-again` — `browser/browser/aboutRobots.ftl` — .label2 left in English while the value is translated
    - Source: `(value): Try Again label2: Please do not press this button again.`
- `styleeditor-pretty-print-button` — `devtools/client/styleeditor.ftl` — Left in English ("Stylesheet Pretty Print") while both siblings are translated
    - Source: `title: Pretty print style sheet`
- `styleeditor-save-button` — `devtools/client/styleeditor.ftl` — Access key `s` of `styleeditor-save-button` is not present in its label
    - Current: `s`
    - Source: `(value): Save accesskey: S tooltiptext: Save this style sheet to a file`
    - The label is “Bewarje”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `url-classifier-content-classifier-loading-url` — `toolkit/toolkit/about/url-classifier.ftl` — URL lade (imperative) → Ladende URL (noun label, per comment)
    - Current: `URL lade`
    - Source: `Loading URL`
    - Suggest: `Ladende URL`
- `url-classifier-content-classifier-loading-url-enabled` — `toolkit/toolkit/about/url-classifier.ftl` — Laden fan URL ynskeakelje → Ladende URL ynskeakelje
    - Current: `Laden fan URL ynskeakelje`
    - Source: `Enable loading URL`
    - Suggest: `Ladende URL ynskeakelje`

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-import-report-page-title` — `browser/browser/aboutLogins.ftl` — Gearfettend rapport ymportearje → Rapport ymportgearfetting
    - Current: `Gearfettend rapport ymportearje`
    - Source: `Import Summary Report`
    - Suggest: `Rapport ymportgearfetting`
- `restart-required-multiple-instances-answer` — `browser/browser/aboutRestartRequired.ftl` — "the open one" (the open profile/instance) is rendered as "de iepen ferzje" (the open version).
    - Current: `kin de iepen ferzje op in âldere ferzje hâlden wurde`
    - Source: `If one profile or instance updates while another is still open, the open one can be left on an older version. Restarting keeps everything on the same version.`
    - Suggest: `kin dejinge dy’t iepen is op in âldere ferzje bliuwe`
    - The source refers to the still-open profile or instance, not to a "version"; the translation also repeats "ferzje" nonsensically.
- `restart-required-multiple-instances-question` — `browser/browser/aboutRestartRequired.ftl` — "Why" is rendered as "Hoe" (how).
    - Current: `Hoe kin dit barre by meardere profilen`
    - Source: `Why can this happen with multiple profiles or { -brand-short-name } instances?`
    - Suggest: `Wêrom kin dit barre by meardere profilen`
    - The source asks "Why can this happen…"; the Frisian asks "How can this happen".
- `restart-required-unsaved-work-answer` — `browser/browser/aboutRestartRequired.ftl` — "inside webpages" translated as "binnen websites" (inside websites).
    - Current: `net-bewarre wurk binnen websites`
    - Source: `Possibly, and we know that’s frustrating. { -brand-short-name } will reopen your tabs, but unsaved work inside webpages, like text in a form, may not be restored. Private Windows won’t reopen to protect your privacy.`
    - Suggest: `net-bewarre wurk binnen websiden`
    - en-US says "webpages"; fy-NL uses "websiden" for pages, "websites" for sites.
- `restore-page-list-header` — `browser/browser/aboutSessionRestore.ftl` — Skermen en ljepblêden → Finsters en ljepblêden
    - Current: `Skermen en ljepblêden`
    - Source: `label: Windows and Tabs`
    - Suggest: `Finsters en ljepblêden`
- `restore-page-window-label` — `browser/browser/aboutSessionRestore.ftl` — Skerm #{ $windowNumber } → Finster { $windowNumber }
    - Current: `Skerm #{ $windowNumber }`
    - Source: `Window { $windowNumber }`
    - Suggest: `Finster { $windowNumber }`
- `addon-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — de ferwachte add-on { -brand-short-name } → de add-on dy’t { -brand-short-name } ferwachte
    - Current: `de ferwachte add-on { -brand-short-name }`
    - Source: `The add-on could not be installed because it does not match the add-on { -brand-short-name } expected.`
    - Suggest: `de add-on dy’t { -brand-short-name } ferwachte`
- `addon-local-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — de ferwachte add-on { -brand-short-name } → de add-on dy’t { -brand-short-name } ferwachte
    - Current: `de ferwachte add-on { -brand-short-name }`
    - Source: `This add-on could not be installed because it does not match the add-on { -brand-short-name } expected.`
    - Suggest: `de add-on dy’t { -brand-short-name } ferwachte`
- `profiler-popup-presets-ml-description` — `browser/browser/appmenu.ftl` — masineoersettingsbugs → masinaal-learenbugs (ML ≠ MT)
    - Current: `masineoersettingsbugs`
    - Source: `Preset for investigating machine learning bugs in { -brand-shorter-name }.`
- `backup-file-how-to-restore-header` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
    - Current: `reparearje`
    - Source: `How to restore:`
    - Suggest: `werstelle`
- `backup-file-title` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
    - Current: `reparearje`
    - Source: `Restore { -brand-short-name }`
    - Suggest: `werstelle`
- `backup-folder-name` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
    - Current: `reparearje`
    - Source: `Restore { -brand-product-name }`
    - Suggest: `werstelle`
- `restore-from-backup-header` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
    - Current: `reparearje`
    - Source: `Restore your data`
    - Suggest: `werstelle`
- `browser-window-restore-down-button` — `browser/browser/browser.ftl` — Omleech opnij ynstelle → Ferlytsje
    - Current: `Omleech opnij ynstelle`
    - Source: `tooltiptext: Restore Down`
    - Suggest: `Ferlytsje`
- `identity-https-only-info-no-upgrade` — `browser/browser/browser.ftl` — HTTP-ferbining net fernije → ferbining net opwurdearje fan HTTP
    - Current: `HTTP-ferbining net fernije`
    - Source: `Unable to upgrade connection from HTTP.`
    - Suggest: `ferbining net opwurdearje fan HTTP`
- `identity-weak-encryption` — `browser/browser/browser.ftl` — swakke befeiliging → swakke fersifering
    - Current: `swakke befeiliging`
    - Source: `This page uses weak encryption.`
    - Suggest: `swakke fersifering`
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — Sykaksjes → Sykje yn aksjes / Aksjes trochsykje ("Search" is a verb)
    - Current: `Sykaksjes`
    - Source: `aria-label: Search actions placeholder: Enter search terms`
    - Suggest: `Sykje yn aksjes`
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — Sykaksjes → Sykje yn aksjes / Aksjes trochsykje ("Search" is a verb)
    - Current: `Sykaksjes`
    - Source: `Search Actions`
    - Suggest: `Sykje yn aksjes`
- `urlbar-search-tips-onboard` — `browser/browser/browser.ftl` — Sykje nei { $engineName } → Sykje mei { $engineName }
    - Current: `Sykje nei { $engineName }`
    - Source: `Type less, find more: Search { $engineName } right from your address bar.`
    - Suggest: `Sykje mei { $engineName }`
- `urlbar-searchmode-no-keyword2` — `browser/browser/browser.ftl` — Sykje nei trefwurden → Sykjen mei trefwurden
    - Current: `Sykje nei trefwurden`
    - Source: `title: Keyword search is disabled`
    - Suggest: `Sykjen mei trefwurden`
- `main-context-menu-stop` — `browser/browser/browserContext.ftl` — Beëinigje → Stopje
    - Current: `Beëinigje`
    - Source: `accesskey: S aria-label: Stop`
    - Suggest: `Stopje`
- `customize-mode-overflow-list-description` — `browser/browser/customizeMode.ftl` — hjirnei ta → hjirhinne
    - Current: `hjirnei ta`
    - Source: `Drag and drop items here to keep them within reach but out of your toolbar…`
    - Suggest: `hjirhinne`
- `customkeys-dev-storage` — `browser/browser/customkeys.ftl` — Unthâld-ynspektor → Opslach-ynspektor
    - Current: `Unthâld-ynspektor`
    - Source: `Storage Inspector`
- `sidebar-callout-survey-neutral` — `browser/browser/featureCallout.ftl` — Gemiddeld → Neutraal
    - Current: `Gemiddeld`
    - Source: `Neutral`
    - Suggest: `Neutraal`
- `genai-input-ask-smart-window` — `browser/browser/genai.ftl` — Fragen… → Freegje…
    - Current: `Fragen…`
    - Source: `placeholder: Ask…`
    - Suggest: `Freegje…`
- `genai-menu-ask-smart-window` — `browser/browser/genai.ftl` — Fragen… → Freegje…
    - Current: `Fragen…`
    - Source: `accesskey: z label: Ask…`
    - Suggest: `Freegje…`
- `genai-more-actions-all-off-notice` — `browser/browser/genai.ftl` — The settings path 'Tabs and browsing' is reduced to 'en blêdzje', and the string says to show 'the page' again instead of the menu.
    - Current: `en blêdzje om de side opnij te toanen`
    - Source: `You won’t see this menu when you select text. Visit Settings <span data-l10n-name="chevron"></span> Tabs and browsing to show it again.`
    - Suggest: `Ljepblêden en sneupe om it opnij te toanen`
    - en-US names the settings section 'Tabs and browsing', but the Frisian drops 'Tabs', so the path no longer matches the section. It also refers to 'de side' (the page), when the source means the menu ('it').
- `genai-more-actions-all-off-notice` — `browser/browser/genai.ftl` — The negation is missing, so the notice says the user will see the menu when selecting text.
    - Current: `Jo sjogge dit menu as jo tekst selektearje.`
    - Source: `You won’t see this menu when you select text. Visit Settings <span data-l10n-name="chevron"></span> Tabs and browsing to show it again.`
    - Suggest: `Jo sjogge dit menu net mear as jo tekst selektearje.`
    - en-US 'You won't see this menu when you select text' is negative; the Frisian says 'You see this menu when you select text'.
- `genai-page-warning` — `browser/browser/genai.ftl` — is dit foar in part de gearfetting → is dit in dielgearfetting
    - Current: `is dit foar in part de gearfetting`
    - Source: `message: Since the page is long, this is a partial summary.`
    - Suggest: `is dit in dielgearfetting`
- `genai-prompts-summarize-page` — `browser/browser/genai.ftl` — "webpage" is translated as "website", so the prompt asks for a summary of the whole site instead of the single page.
    - Current: `Gearfetsje de website op { $url }`
    - Source: `Please summarize the webpage at { $url } using precise and concise language. Use headers and bulleted lists in the summary, to make it scannable. Maintain the meaning and factual accuracy.`
    - Suggest: `Gearfetsje de webside op { $url }`
    - The source and the developer comment both refer to a single webpage at the given URL. In Frisian "website" means the whole site and "webside" means one page, and this prompt is sent to the AI chatbot as it stands.
- `genai-shortcut-button-3` — `browser/browser/genai.ftl` — "Ask about this text" is rendered as a noun phrase "Questions about this text" instead of the imperative verb.
    - Current: `aria-label: Fragen oer dizze tekst`
    - Source: `aria-label: Ask about this text tooltiptext: Ask about this text`
    - Suggest: `aria-label: Freegje oer dizze tekst`
    - The source is an imperative action label; "Fragen oer dizze tekst" reads as "Questions about this text".
- `menu-history-undo-window-menu` — `browser/browser/menubar.ftl` — Koartlyn sluten skermen → … finsters
    - Current: `Koartlyn sluten skermen`
    - Source: `label: Recently Closed Windows`
    - Suggest: `… finsters`
- `newtab-privacy-message-streak` — `browser/browser/newtab/newtab.ftl` — "op rige" dropped in the singular variant only
    - Source: `{$count ->} [one] You’ve been protected { $count } day in a row. [other] You’ve been protected { $count } days in a row.`
- `newtab-section-following-button` — `browser/browser/newtab/newtab.ftl` — Folgjend ("next") → Folge ("following")
    - Current: `Folgjend`
    - Source: `Following`
    - Suggest: `Folge`
- `newtab-section-unfollow-button-label` — `browser/browser/newtab/newtab.ftl` — Folgjend ("next") → Folge ("following")
    - Current: `Folgjend`
    - Source: `aria-label: Following: Unfollow { $topic }`
    - Suggest: `Folge`
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — foar de hân → by de hân
    - Current: `foar de hân`
    - Source: `Your favorites at your fingertips`
    - Suggest: `by de hân`
- `newtab-wallpaper-your-images-folder` — `browser/browser/newtab/newtab.ftl` — The accessible name changes "Your images, wallpapers that you have saved" into "Your saved images and wallpapers", turning an appositive description into two separate categories.
    - Current: `Jo bewarre ôfbyldingen en eftergrûnen`
    - Source: `aria-label: Your images, wallpapers that you have saved`
    - Suggest: `Jo ôfbyldingen, eftergrûnen dy’t jo bewarre hawwe`
    - The en-US names one thing — the "Your images" folder — and explains it as wallpapers the user saved; the Frisian lists images and wallpapers as two things, losing the link to the "Jo ôfbyldingen" label.
- `mr2022-onboarding-pin-private-image-alt` — `browser/browser/newtab/onboarding.ftl` — út in ferskine — the noun hoed is missing
    - Current: `út in ferskine`
    - Source: `aria-label: Magic wand makes { -brand-product-name } private browsing logo appear out of a hat`
    - Suggest: `hoed`
- `onboarding-easy-setup-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — troch in non-profitorganisaasje browser — stipe missing, bedriuwen duplicated
    - Current: `troch in non-profitorganisaasje browser`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `stipe`
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — The word “major” is missing, so the Frisian says Firefox is the only browser of any kind backed by a non-profit.
    - Current: `de iennige browser dy’t stipe wurdt`
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
    - Suggest: `de iennige grutte browser dy’t stipe wurdt`
    - The en-US says “the only major browser backed by a non-profit”. Without “major” (grutte), the Frisian makes a broader factual claim than the source.
- `onboarding-refresh-tou-pin-unchecked` — `browser/browser/newtab/onboarding.ftl` — "a click away" is rendered as "ien klik fuort", which in Frisian/Dutch idiom says the browser is one click *away/gone* rather than within one click's reach.
    - Current: `Hâld de iennige grutte ûnôfhinklike browser ien klik fuort`
    - Source: `Keep the only major independent browser a click away`
    - Suggest: `Hâld de iennige grutte ûnôfhinklike browser op ien klik ôfstân`
    - The en-US means keeping the browser easily reachable (one click away); "ien klik fuort" reads as removing/keeping it away.
- `policy-Backup` — `browser/browser/policies/policies-descriptions.ftl` — reparearje → weromsette (restore, not repair)
    - Current: `reparearje`
    - Source: `Disable backup or restore of profile data.`
    - Suggest: `weromsette`
- `policy-DisableSecurityBypass` — `browser/browser/policies/policies-descriptions.ftl` — befeiligingsynstellingen → befeiligingswarskôgingen
    - Current: `befeiligingsynstellingen`
    - Source: `Prevent the user from bypassing certain security warnings.`
    - Suggest: `befeiligingswarskôgingen`
- `policy-DisableThirdPartyModuleBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — The page name 'Third-party Module Information' is rendered as 'external information about modules', so 'third-party' wrongly describes the information instead of the modules.
    - Current: `eksterne ynformaasje oer modulen`
    - Source: `Prevent the user from using Third-party Module Information (about:third-party) to block third-party modules injected into the { -brand-short-name } process.`
    - Suggest: `Ynformaasje oer modulen fan tredden`
    - In en-US, 'Third-party Module Information' is the title of the about:third-party page and means information about third-party modules. The Frisian says the information itself is external, which is wrong, and it doesn't match 'modulen fan tredden' later in the same sentence.
- `policy-OfferToSaveLoginsDefault` — `browser/browser/policies/policies-descriptions.ftl` — Spurious ôftwingje carried over from policy-OfferToSaveLogins
    - Current: `ôftwingje`
    - Source: `Set the default value for allowing { -brand-short-name } to offer to remember saved logins and passwords. Both true and false values are accepted.`
- `policy-PasswordManagerEnabled2` — `browser/browser/policies/policies-descriptions.ftl` — The internal page URL is given as about:login instead of about:logins.
    - Current: `(about:login)`
    - Source: `Enable or disable saving passwords to the password manager. If disabled, Passwords (about:logins) is also blocked.`
    - Suggest: `(about:logins)`
    - The en-US names the page about:logins. about:login is not the Passwords page, so the identifier must be kept exactly.
- `appearance-window-density-touch` — `browser/browser/preferences/preferences.ftl` — lykas klikdoelen → en klikdoelen
    - Current: `lykas klikdoelen`
    - Source: `description: Larger window elements and click targets, optimized for touch screens label: Touch`
    - Suggest: `en klikdoelen`
- `data-collection-run-studies` — `browser/browser/preferences/preferences.ftl` — in keur oan brûkers → willekeurich brûkers ("randomly" lost)
    - Current: `in keur oan brûkers`
    - Source: `description: { -brand-short-name } randomly selects users to test features, which helps improve quality for everyone. label: Allow { -brand-short-name } to run feature studies`
    - Suggest: `willekeurich brûkers`
- `search-one-click-header2` — `browser/browser/preferences/preferences.ftl` — Fluchkeppelingen sykje (imperative) → Sykfluchkeppelingen (noun heading)
    - Current: `Fluchkeppelingen sykje`
    - Source: `Search Shortcuts`
    - Suggest: `Sykfluchkeppelingen`
- `windows-launch-on-login-disabled` — `browser/browser/preferences/preferences.ftl` — Link text Apps → Opstart-apps (Windows "Startup Apps")
    - Current: `Apps`
    - Source: `This preference has been disabled in Windows. To change, visit <a data-l10n-name="startup-link">Startup Apps</a> in System settings.`
- `windows-passkey-settings-label` — `browser/browser/preferences/preferences.ftl` — Wachtwurden beheare → Tagongskaaien beheare (passkeys ≠ passwords)
    - Current: `Wachtwurden beheare`
    - Source: `Manage passkeys in system settings`
    - Suggest: `Tagongskaaien beheare`
- `profiles-pink-theme-title` — `browser/browser/profiles.ftl` — Rôze → Rôs (its own label is Rôs)
    - Current: `Rôze`
    - Source: `title: Apply pink theme`
    - Suggest: `Rôs`
- `etp-card-title-always` — `browser/browser/protections.ftl` — beskerming tsjin befeiliging → beskerming tsjin folgjen
    - Current: `beskerming tsjin befeiliging`
    - Source: `Enhanced Tracking Protection: Always On`
    - Suggest: `beskerming tsjin folgjen`
- `protections-panel-not-found-label` — `browser/browser/protectionsPanel.ftl` — Gjin detektearre → Neat detektearre
    - Current: `Gjin detektearre`
    - Source: `None Detected`
    - Suggest: `Neat detektearre`
- `item-offline-apps` — `browser/browser/sanitize.ftl` — Bewarre websitegegevens → Offline websitegegevens
    - Current: `Bewarre websitegegevens`
    - Source: `accesskey: O label: Offline website data`
    - Suggest: `Offline websitegegevens`
- `sanitize-button-clearing` — `browser/browser/sanitize.ftl` — Wiskje (identical to sanitize-button-ok2) → Dwaande mei wiskjen…
    - Source: `label: Clearing`
    - Suggest: `Dwaande mei wiskjen…`
- `tab-context-close-multiple-tabs` — `browser/browser/tabContextMenu.ftl` — Mear ljepblêden slute → Meardere ljepblêden slute
    - Current: `Mear ljepblêden slute`
    - Source: `accesskey: M label: Close Multiple Tabs`
    - Suggest: `Meardere ljepblêden slute`
- `edit-controls.label` — `browser/chrome/browser/customizableui/customizableWidgets.properties` — "Edit controls" (the noun phrase naming the cut/copy/paste widget) is translated as the imperative "Edit the controls".
    - Current: `Betsjinningen bewurkje`
    - Source: `Edit controls`
    - Suggest: `Bewurkingsbetsjinningen`
    - In customizableWidgets, 'Edit controls' is the name of the toolbar widget containing Cut/Copy/Paste ('edit' is an attributive noun), not an instruction to edit controls.
- `network-menu-summary-finish` — `devtools/client/netmonitor.ftl` — Foltôgje: (imperative) → Klear: (noun label)
    - Current: `Foltôgje:`
    - Source: `Finish: { $formattedTime }`
    - Suggest: `Klear:`
- `jsonlScopeName` — `devtools/client/netmonitor.properties` — "JSON Lines" is a format name that should not be translated.
    - Current: `JSON-regels`
    - Source: `JSON Lines`
    - Suggest: `JSON Lines`
    - The developer comment explains this is the JSON Lines (JSONL/NDJSON) format name displayed as the payload type; it is a format identifier, not descriptive text.
- _…and 63 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `settings-update-unsupported` — `browser/browser/aboutDialog.ftl` — fernijngen → fernijingen
    - Current: `fernijngen`
    - Source: `You can not perform further updates on this system. <a data-l10n-name="unsupported-link">Learn more</a>`
    - Suggest: `fernijingen`
- `update-unsupported` — `browser/browser/aboutDialog.ftl` — fernijngen → fernijingen
    - Current: `fernijngen`
    - Source: `You can not perform further updates on this system. <label data-l10n-name="unsupported-link">Learn more</label>`
    - Suggest: `fernijingen`
- `about-logins-confirm-delete-all-sync-dialog-message` — `browser/browser/aboutLogins.ftl` — The particle is missing from the separable verb, so "smyt it fan" does not mean "deletes it from".
    - Current: `Dit smyt it fan`
    - Source: `{$count ->} [1] This deletes it from { -brand-short-name } on every device that syncs your passwords. You can’t undo this. [other] This deletes them from { -brand-short-name } on every device that syncs your passwords.…`
    - Suggest: `Dit smyt it út`
    - Without "út" or "fuort", "smite" does not mean "delete". The parallel string about-logins-confirm-delete-dialog-message correctly uses "smyt it út". The same fix applies to the plural form ("smyt se út").
- `login-list-intro-description` — `browser/browser/aboutLogins.ftl` — Wannear jo → Wannear’t jo
    - Current: `Wannear jo`
    - Source: `When you save a password in { -brand-product-name }, it will show up here.`
    - Suggest: `Wannear’t jo`
- `about-private-browsing-nova-info-subheader2` — `browser/browser/aboutPrivateBrowsing.ftl` — al jo priveefinster → al jo priveefinsters
    - Current: `al jo priveefinster`
    - Source: `We’ll erase every search and sign-in when you close all your Private Windows. { -brand-short-name }’s built-in protections are on here too, like blocking trackers.`
    - Suggest: `al jo priveefinsters`
- `restart-required-single-instance-answer-2` — `browser/browser/aboutRestartRequired.ftl` — "wykst" is a misspelling of "wylst" (while/during).
    - Current: `Dit kin barre wykst in lange navigaasjesesje`
    - Source: `This can happen during a long browsing session, or when your operating system updates { -brand-short-name }. Restarting keeps { -brand-short-name } secure and working normally.`
    - Suggest: `Dit kin barre by in lange navigaasjesesje`
    - The en-US says "during a long browsing session"; "wykst" is not a Frisian word (typo for "wylst").
- `welcome-back-restore-some-label` — `browser/browser/aboutSessionRestore.ftl` — dy’t jo winske (past) → dy’t jo winskje
    - Current: `dy’t jo winske`
    - Source: `Restore only the ones you want`
    - Suggest: `dy’t jo winskje`
- `about-unloads-column-sortweight` — `browser/browser/aboutUnloads.ftl` — ôflaad → ôflaat
    - Current: `ôflaad`
    - Source: `(value): Secondary Weight title: If available, tabs are sorted by this value after being sorted by the base weight. The value derives from tab’s memory usage and the count of processes.`
    - Suggest: `ôflaat`
- `about-unloads-column-weight` — `browser/browser/aboutUnloads.ftl` — alteart → allearst; ôflaad → ôflaat
    - Current: `alteart`
    - Source: `(value): Base Weight title: Tabs are first sorted by this value, which derives from some special attributes such as playing a sound, WebRTC, etc.`
    - Suggest: `allearst`
- `addon-install-full-screen-blocked` — `browser/browser/addonNotifications.ftl` — Add-on-installaasje → Add-on-ynstallaasje
    - Source: `Add-on installation is not allowed while in or before entering fullscreen mode.`
- `aiwindow-starter-browsing-compare` — `browser/browser/aiWindow.ftl` — ljeplêden → ljepblêden
    - Current: `ljeplêden`
    - Source: `Compare tabs`
    - Suggest: `ljepblêden`
- `smartbar-placeholder` — `browser/browser/aiWindow.ftl` — in URL type → in URL typje
    - Current: `in URL type`
    - Source: `placeholder: Ask, search, or type a URL`
    - Suggest: `in URL typje`
- `smart-window-opened-tabs-row-label` — `browser/browser/aiWindowContent.ftl` — ljeplêden → ljepblêden
    - Current: `ljeplêden`
    - Source: `Opened tabs`
    - Suggest: `ljepblêden`
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — Dangling hokker ljepblêden at the end
    - Source: `If you still want to group tabs, choose <strong>Retry</strong> and select which ones in the card that opens.`
- `appmenu-remote-tabs-tabsnotsyncing` — `browser/browser/appmenu.ftl` — ljepblêdsyngroanisaasje → ljepblêdsyngronisaasje
    - Current: `ljepblêdsyngroanisaasje`
    - Source: `Turn on tab syncing to view a list of tabs from your other devices.`
    - Suggest: `ljepblêdsyngronisaasje`
- `smartwindow-group-tabs-all-sorted` — `browser/browser/autoTabGrouping.ftl` — 'ljeplêden' is misspelled; it should be 'ljepblêden' (tabs).
    - Current: `ljeplêden`
    - Source: `Nice work organizing your tabs`
    - Suggest: `ljepblêden`
    - The locale's term for tabs is 'ljepblêden', which every other string in the file uses. Here the 'b' is missing.
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — Two occurrences of wannear → wannear’t
    - Current: `wannear`
    - Source: `The Default Browser Agent task checks when the default changes from { -brand-short-name } to another browser. If the change happens under suspicious circumstances, it will prompt users to change back to { -brand-short-n…`
    - Suggest: `wannear’t`
- `data-reporting-notification-message` — `browser/browser/browser.ftl` — ferstjoerd → ferstjoert
    - Current: `ferstjoerd`
    - Source: `{ -brand-short-name } automatically sends some data to { -vendor-short-name } so that we can improve your experience.`
    - Suggest: `ferstjoert`
- `decoder-doctor-decode-error-message` — `browser/browser/browser.ftl` — "wylst" is a conjunction but is followed by a noun phrase, which makes the sentence ungrammatical.
    - Current: `wylst it dekodearjen fan in mediaboarne`
    - Source: `An error occurred while decoding a media resource.`
    - Suggest: `by it dekodearjen fan in mediaboarne`
    - Frisian "wylst" means "while" as a conjunction and needs a full clause after it. Before a noun phrase the preposition "by" is needed ("by it dekodearjen" = "while decoding").
- `decoder-doctor-decode-warning-message` — `browser/browser/browser.ftl` — "wylst" is a conjunction but is followed by a noun phrase, which makes the sentence ungrammatical.
    - Current: `wylst it dekodearjen fan in mediaboarne`
    - Source: `A recoverable error occurred while decoding a media resource.`
    - Suggest: `by it dekodearjen fan in mediaboarne`
    - Frisian "wylst" needs a full clause after it. Before a noun phrase the preposition "by" is needed.
- `onboarding-aw-finish-setup-button` — `browser/browser/browser.ftl` — Ynstellen { -brand-short-name } → Ynstellen fan { -brand-short-name }
    - Current: `Ynstellen { -brand-short-name }`
    - Source: `label: Finish setup tooltiptext: Finish setting up { -brand-short-name }`
    - Suggest: `Ynstellen fan { -brand-short-name }`
- `contextual-manager-passwords-remove-all-message` — `browser/browser/contextual-manager.ftl` — wachtwurd dy’t → wachtwurd dat (neuter) in the [one] variants
    - Current: `wachtwurd dy’t`
    - Source: `{$total ->} [1] This will remove your password saved to { -brand-short-name } and any breach alerts. You cannot undo this action. [other] This will remove the passwords saved to { -brand-short-name } and any breach aler…`
    - Suggest: `wachtwurd dat`
- `customize-mode-downloads-button-autohide` — `browser/browser/customizeMode.ftl` — wannear leech → wannear’t dizze leech is
    - Current: `wannear leech`
    - Source: `label: Hide button when empty`
    - Suggest: `wannear’t dizze leech is`
- `default-browser-prompt-message-pin` — `browser/browser/defaultBrowserNotification.ftl` — hantberik → hânberik
    - Current: `hantberik`
    - Source: `Keep { -brand-short-name } at your fingertips — make it your default browser and pin it to your taskbar.`
    - Suggest: `hânberik`
- `downloads-blocked-potentially-insecure` — `browser/browser/downloads.ftl` — The infinitive 'downloaden' is used where the past participle 'download' is needed, so the message reads as 'do not download the file' instead of 'file not downloaded'.
    - Current: `Bestân net downloaden`
    - Source: `File not downloaded: Potential security risk.`
    - Suggest: `Bestân net download`
    - The en-US 'File not downloaded' is a past participle. The locale itself uses the participle 'download' elsewhere ('wurdt net faak download'), and the infinitive changes the sense to an instruction.
- `downloads-unblock-insecure` — `browser/browser/downloads.ftl` — 'wylst' is a conjunction and can't come before a noun phrase; a preposition such as 'tidens' is needed here.
    - Current: `wylst it downloadproses`
    - Source: `The download is offered over HTTP even though the current document was delivered over a secure HTTPS connection. If you proceed, the download may be corrupted or tampered with during the download process.`
    - Suggest: `tidens it downloadproses`
    - The en-US says 'during the download process'. That needs a preposition in Frisian, but 'wylst' ('while') has to introduce a clause, so this is ungrammatical.
- `bookmarks-toolbar-callout-2b-title` — `browser/browser/featureCallout.ftl` — blêdwizerakbalke → blêdwizerarkbalke
    - Current: `blêdwizerakbalke`
    - Source: `Keep your bookmarks toolbar open?`
    - Suggest: `blêdwizerarkbalke`
- `sidebar-callout-survey-features-question` — `browser/browser/featureCallout.ftl` — Preposition 'in' should be Frisian 'yn'.
    - Current: `produktiviteit in { -brand-short-name }`
    - Source: `The following are potential sidebar features. Which would improve your productivity in { -brand-short-name } the most?`
    - Suggest: `produktiviteit yn { -brand-short-name }`
    - The Frisian preposition for 'in' is 'yn', which is used correctly elsewhere in the batch. 'in' here is a spelling error.
- `vertical-tabs-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — Doubled fluch
    - Source: `Try our new vertical tabs layout to quickly scan your list of tabs. Early testers report this layout helps them feel more organized. Switch anytime.`
- `vertical-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — list mei ljeppers → list mei ljepblêden
    - Current: `list mei ljeppers`
    - Source: `This layout makes it easy to quickly scan your list of tabs. Plus, you can adjust the width to see more or less of your tab titles.`
    - Suggest: `list mei ljepblêden`
- `windows-10-eos-sync-split-dismiss-button-show-fewer-option` — `browser/browser/featureCallout.ftl` — Minder oanrekommandearre toane → Minder oanrekommandaasjes toane
    - Current: `Minder oanrekommandearre toane`
    - Source: `label: Show fewer recommendations`
    - Suggest: `Minder oanrekommandaasjes toane`
- `windows-10-eos-sync-urgency-subtitle-1` — `browser/browser/featureCallout.ftl` — -ynstelling → -ynstellingen
    - Current: `-ynstelling`
    - Source: `Sync now to keep your { -brand-short-name } bookmarks, passwords, and settings safe and easy to restore.`
    - Suggest: `-ynstellingen`
- `firefox-relay-get-reusable-masks-failed` — `browser/browser/firefoxRelay.ftl` — Stray nij: gjin nij opnij brûkbere maskers
    - Current: `nij`
    - Source: `{ -relay-brand-name } could not find reusable masks. HTTP error code: { $status }.`
    - Suggest: `gjin nij opnij brûkbere maskers`
- `firefoxview-opentabs-header` — `browser/browser/firefoxView.ftl` — ljeplêden → ljepblêden
    - Current: `ljeplêden`
    - Source: `Open tabs`
    - Suggest: `ljepblêden`
- `firefoxview-opentabs-nav` — `browser/browser/firefoxView.ftl` — ljeplêden → ljepblêden
    - Current: `ljeplêden`
    - Source: `(value): Open tabs title: Open tabs`
    - Suggest: `ljepblêden`
- `genai-prompts-proofread` — `browser/browser/genai.ftl` — krekten → krektens
    - Current: `krekten`
    - Source: `label: Proofread value: Please proofread the selection for spelling and grammar errors. Identify any mistakes and provide a corrected version of the text. Maintain the meaning and factual accuracy and output the list of…`
    - Suggest: `krektens`
- `ipprotection-button-turn-vpn-off-1` — `browser/browser/ipProtection.ftl` — "Utskeakelje" is missing the accent on Ú.
    - Current: `Utskeakelje`
    - Source: `Turn off`
    - Suggest: `Útskeakelje`
    - The Frisian word is "út", so this verb is spelled "útskeakelje". The capital needs the accent too.
- `ipprotection-connection-status-blocked-error-description-1` — `browser/browser/ipProtection.ftl` — Comma splits subject from verb
    - Source: `Local laws and restrictions limit where you can use VPN. <a data-l10n-name="learn-more-link">Learn more</a>`
- `ipprotection-connection-status-network-error-description` — `browser/browser/ipProtection.ftl` — dernei → dêrnei
    - Current: `dernei`
    - Source: `Connect to the internet, then try turning VPN on.`
    - Suggest: `dêrnei`
- `ipprotection-locations-subview-recommended-description` — `browser/browser/ipProtection.ftl` — Fyn (imperative) → Fynt
    - Current: `Fyn`
    - Source: `Finds the fastest location`
    - Suggest: `Fynt`
- `site-rules-inclusion-prompt` — `browser/browser/ipProtection.ftl` — "ynkseakelje" is a typo for "ynskeakelje".
    - Current: `ynkseakelje`
    - Source: `heading: Always turn on VPN for { $website }? message: Update your rules anytime in settings.`
    - Suggest: `ynskeakelje`
    - The letters are swapped. Elsewhere in the same file the word is correctly spelled "Ynskeakelje".
- `menu-application-hide-other` — `browser/browser/menubar.ftl` — Oare ferstopje → Oaren ferstopje
    - Current: `Oare ferstopje`
    - Source: `label: Hide Others`
    - Suggest: `Oaren ferstopje`
- `migration-list-autofill-label` — `browser/browser/migrationWizard.ftl` — gegevens automatysk ynfolje → gegevens foar automatysk ynfoljen
    - Current: `gegevens automatysk ynfolje`
    - Source: `autofill data`
    - Suggest: `gegevens foar automatysk ynfoljen`
- `july-jam-body` — `browser/browser/newtab/asrouter.ftl` — feilich en flugge tagong → feilige en flugge tagong
    - Current: `feilich en flugge tagong`
    - Source: `Every month, { -brand-short-name } blocks an average of 3,000+ trackers per user, giving you safe, speedy access to the good internet.`
    - Suggest: `feilige en flugge tagong`
- `nova-early-access-infobar-title` — `browser/browser/newtab/asrouter.ftl` — úterlik → uterlik (spurious accent)
    - Current: `úterlik`
    - Source: `<strong>{ -brand-product-name } is getting a new look.</strong> You’re previewing an early, unpolished version before the launch later this year.`
    - Suggest: `uterlik`
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — Untfang flugger sneupe → … sneupen
    - Current: `Untfang flugger sneupe`
    - Source: `{$sel_1 ->} [macos] Make it your default and keep it in your Dock. [other] Get faster browsing and automatic privacy protection.`
    - Suggest: `… sneupen`
- `spotlight-public-wifi-vpn-body` — `browser/browser/newtab/asrouter.ftl` — wylst it navigearjen → wylst jo navigearje
    - Current: `wylst it navigearjen`
    - Source: `To hide your location and browsing activity, consider a Virtual Private Network. It will help keep you protected when browsing in public places like airports and coffee shops.`
    - Suggest: `wylst jo navigearje`
- `taskbar-tabs-spotlight-subtitle` — `browser/browser/newtab/asrouter.ftl` — The adjective has the wrong ending: 'finster' is a neuter noun, so after 'in' the adjective takes no -e.
    - Current: `in ferienfâldige finster`
    - Source: `One click launches your most used sites in a streamlined window with all of { -brand-short-name }’s protections.`
    - Suggest: `in ferienfâldich finster`
    - In Frisian, 'finster' takes the article 'it', which makes it neuter. When a neuter noun follows the indefinite article 'in', the adjective before it has no -e ending (for example 'in grut finster'). So 'ferienfâldige' should be 'ferienfâldich'.
- `windows-10-eos-challenger-pin-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — jo it nedich binne → jo it nedich hawwe
    - Current: `jo it nedich binne`
    - Source: `Pin { -brand-shorter-name } to your taskbar so the browser you chose is always there when you need it.`
    - Suggest: `jo it nedich hawwe`
- `newtab-empty-section-topstories-generic` — `browser/browser/newtab/newtab.ftl` — Kin jo net wachtsje? → Kinne jo net wachtsje?
    - Current: `Kin jo net wachtsje?`
    - Source: `You’ve caught up. Check back later for more stories. Can’t wait? Select a popular topic to find more great stories from around the web.`
    - Suggest: `Kinne jo net wachtsje?`
- `newtab-picture-header-date` — `browser/browser/newtab/newtab.ftl` — "Ofbylding" is missing the circumflex; the Frisian spelling is "Ôfbylding".
    - Current: `Ofbylding fan de dei`
    - Source: `Picture of the day: { $date }`
    - Suggest: `Ôfbylding fan de dei`
    - The Frisian word is "ôfbylding", and the circumflex stays on the capital letter. The same batch writes "ôfbylding" in newtab-picture-set-wallpaper2 and newtab-picture-menu-hide-photo2.
- `newtab-picture-menu-show-photo2` — `browser/browser/newtab/newtab.ftl` — "Ofbylding" is missing the circumflex; the Frisian spelling is "Ôfbylding".
    - Current: `Ofbylding toane`
    - Source: `Show picture`
    - Suggest: `Ôfbylding toane`
    - The Frisian word is "ôfbylding", and the circumflex stays on the capital letter. The same batch writes "ôfbylding" in other strings.
- `newtab-picture-show-button2` — `browser/browser/newtab/newtab.ftl` — "Ofbylding" is missing the circumflex in the aria-label and title; the Frisian spelling is "Ôfbylding".
    - Current: `Ofbylding toane`
    - Source: `aria-label: Show picture title: Show picture`
    - Suggest: `Ôfbylding toane`
    - The Frisian word is "ôfbylding", and the circumflex stays on the capital letter. The same batch writes "ôfbylding" in other strings.
- `newtab-picture-widget-open-menu-button` — `browser/browser/newtab/newtab.ftl` — Mistranslated/misparsed compound: "Ofbylding fan it dei-menu" means "the day menu's picture" instead of "picture of the day menu"; also missing diacritic on "Ôfbylding".
    - Current: `aria-label: Ofbylding fan it dei-menu iepenje`
    - Source: `aria-label: Open picture of the day menu title: Open picture of the day menu`
    - Suggest: `aria-label: Menu Ôfbylding fan de dei iepenje`
    - Source means the menu of the "picture of the day" widget; the Frisian attaches "menu" to "dei", and the Frisian word is spelled "Ôfbylding".
- `newtab-privacy-message-promo-monitor-1` — `browser/browser/newtab/newtab.ftl` — foar komme → foarkomme
    - Current: `foar komme`
    - Source: `Find out if your personal info shows up in a data breach.`
    - Suggest: `foarkomme`
- `newtab-privacy-message-promo-relay-1` — `browser/browser/newtab/newtab.ftl` — reagistraasjes → registraasjes
    - Current: `reagistraasjes`
    - Source: `Save your real email for people you trust; use an email mask for sign-ups.`
    - Suggest: `registraasjes`
- `newtab-section-unblock-topic` — `browser/browser/newtab/newtab.ftl` — Blokkearring { $topic } opheffe → Blokkearring fan { $topic } opheffe
    - Current: `Blokkearring { $topic } opheffe`
    - Source: `aria-label: Unblock { $topic }`
    - Suggest: `Blokkearring fan { $topic } opheffe`
- `newtab-sports-widget-message-wallpapers-semifinals-body` — `browser/browser/newtab/newtab.ftl` — Meitsje ien dekôr → Meitsje it dekôr
    - Current: `Meitsje ien dekôr`
    - Source: `Set the stage for the World Cup’s biggest matches.`
    - Suggest: `Meitsje it dekôr`
- `newtab-wallpaper-abstract-purple-green` — `browser/browser/newtab/newtab.ftl` — Pears en griene → Pearze en griene
    - Current: `Pears en griene`
    - Source: `Purple and green light gradient`
    - Suggest: `Pearze en griene`
- `newtab-wallpaper-light-landscape` — `browser/browser/newtab/newtab.ftl` — Berch lânskip → Berchlânskip
    - Current: `Berch lânskip`
    - Source: `Blue mist mountain landscape`
    - Suggest: `Berchlânskip`
- _…and 172 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `navbar-home` — `browser/browser/browser.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `label: Home tooltiptext: { -brand-short-name } Home Page`
    - Suggest: `Begjinside`
- `newtab-stocks-watchlist-full` — `browser/browser/newtab/newtab.ftl` — "Remove" is translated as "Ferwiderje" here while the sibling watchlist strings use "fuortsmite".
    - Current: `Ferwiderje ien om in oare ta te foegjen.`
    - Source: `{$limit ->} [one] You can add up to { $limit } stock. Remove one to add another. [other] You can add up to { $limit } stocks. Remove one to add another.`
    - Suggest: `Smyt ien fuort om in oare ta te foegjen.`
    - Same surface (stocks watchlist) uses "fuortsmite" for Remove in newtab-stocks-remove-from-watchlist and -removed-from-watchlist; "Ferwiderje" is inconsistent and not the Frisian standard term.
- `home-homepage-title` — `browser/browser/preferences/preferences.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `label: Homepage`
    - Suggest: `Begjinside`
- `permissions-block-popups2` — `browser/browser/preferences/preferences.ftl` — Third-party redirects — three renderings: permissions-block-popups-exceptions-button4.description (trochliedingen), permissions-block-popups2 (omliedingen), permissions.ftl (trochferwizingen).
    - Source: `accesskey: B label: Block pop-ups and third-party redirects`
    - Suggest: `trochliedingen`
- `preferences-doh-overview-custom` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
    - Current: `Feilige DNS`
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior. label: Custom`
    - Suggest: `Befeilige DNS`
- `preferences-doh-overview-default` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
    - Current: `Feilige DNS`
    - Source: `description: Use secure DNS in regions where it’s available. label: Default protection`
    - Suggest: `Befeilige DNS`
- `preferences-doh-radio-custom` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
    - Current: `Feilige DNS`
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior label: Custom`
    - Suggest: `Befeilige DNS`
- `preferences-doh-radio-default` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
    - Current: `Feilige DNS`
    - Source: `description: Use secure DNS in regions where it’s available label: Default`
    - Suggest: `Befeilige DNS`
- `preferences-web-appearance-choice-light2` — `browser/browser/preferences/preferences.ftl` — Appearance — útstrieling vs uterlik: preferences-web-appearance-choice-light2, -dark2, -tooltip-light, -tooltip-dark.
    - Current: `útstrieling`
    - Source: `label: Light title: Use a light appearance for website backgrounds and content.`
    - Suggest: `uterlik`
- `search-show-suggestions-url-bar-option` — `browser/browser/preferences/preferences.ftl` — Search suggestions — sykfoarstellen vs syksuggestjes: search-show-suggestions-option, search-suggestions-option, search-show-suggestions-url-bar-option, addressbar-locbar-showtrendingsuggestions-option.
    - Current: `sykfoarstellen`
    - Source: `accesskey: l label: Show search suggestions in address bar results`
    - Suggest: `syksuggestjes`
- `security-privacy-issue-warning-doh` — `browser/browser/preferences/preferences.ftl` — Network provider — netwurkbehearder (administrator) vs ynternetoanbieder: security-privacy-issue-warning-doh, security-privacy-issue-warning-ech (vs their -doh2/-ech2 variants).
    - Current: `netwurkbehearder`
    - Source: `description: DNS over HTTPS hides what sites you visit from your network provider. label: DNS over HTTPS is disabled`
    - Suggest: `ynternetoanbieder`
- `security-privacy-issue-warning-ech` — `browser/browser/preferences/preferences.ftl` — Network provider — netwurkbehearder (administrator) vs ynternetoanbieder: security-privacy-issue-warning-doh, security-privacy-issue-warning-ech (vs their -doh2/-ech2 variants).
    - Current: `netwurkbehearder`
    - Source: `description: Encrypted Client Hello hides what sites you visit from your network provider. label: Encrypted Client Hello is disabled`
    - Suggest: `ynternetoanbieder`
- `PermissionsPolicyUnsupportedFeatureName` — `dom/chrome/security/security.properties` — "Permissions Policy" is rendered as "Machtigingenbelied" here but as "machtigingsbelied" in dom.properties, an inconsistent term for the same spec name.
    - Current: `Machtigingenbelied`
    - Source: `Permissions Policy: Skipping unsupported feature name “%S”.`
    - Suggest: `Machtigingsbelied`
    - Same en-US term "Permissions Policy" rendered two different ways across related console messages.
- `addon-detail-homepage-label` — `toolkit/toolkit/about/aboutAddons.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `Homepage`
    - Suggest: `Begjinside`

### E. Typography, punctuation & spacing

- `about-logins-import-report-description2` — `browser/browser/aboutLogins.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Passwords imported to { -brand-short-name }.`
- `about-logins-import-report-error` — `browser/browser/aboutLogins.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `{$count ->} [other] <div data-l10n-name="count">{ $count }</div> <div data-l10n-name="details">Errors</div> <div data-l10n-name="not-imported">(not imported)</div>`
- `popup-show-popup-menuitem` — `browser/browser/browser.ftl` — rights-webservices-term-4 ("as-is") · protections-vpn-banner-content (TechRadar quote in "…") · popup-show-popup-menuitem.label (uses “…” where the adjacent popup-trigger-redirect-menuitem uses ‘…’).
    - Source: `label: Show “{ $popupURI }”`
    - Suggest: `"as-is"`
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `{$popupCount ->} [0] { -brand-short-name } prevented this site from redirecting. [1] { -brand-short-name } prevented this site from opening a pop-up window and redirecting. [other] { -brand-short-name } prevented this s…`
- `main-context-menu-bookmark-page` — `browser/browser/browserContext.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
    - Source: `accesskey: m aria-label: Bookmark Page… tooltiptext: Bookmark page`
- `main-context-menu-bookmark-page-2` — `browser/browser/browserContext.ftl` — Tooltip text has an ellipsis that the source does not have.
    - Current: `tooltiptext: Blêdwizer foar side meitsje…`
    - Source: `aria-label: Bookmark Page… tooltiptext: Bookmark page`
    - Suggest: `tooltiptext: Blêdwizer foar side meitsje`
    - en-US tooltiptext is "Bookmark page" without ellipsis; only the aria-label has one.
- `main-context-menu-edit-bookmark` — `browser/browser/browserContext.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
    - Source: `accesskey: m aria-label: Edit Bookmark… tooltiptext: Edit bookmark`
- `main-context-menu-edit-bookmark-2` — `browser/browser/browserContext.ftl` — Tooltip adds an ellipsis that the source does not have.
    - Current: `tooltiptext: Blêdwizer bewurkje…`
    - Source: `aria-label: Edit Bookmark… tooltiptext: Edit bookmark`
    - Suggest: `tooltiptext: Blêdwizer bewurkje`
    - The en-US tooltiptext is "Edit bookmark" without ellipsis (only the aria-label has one).
- `sidebar-customization-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `The { -brand-product-name } sidebar gives you quick access to your browsing history, tabs from other devices, and an AI chatbot — all without leaving your main view.`
- `splitview-onboarding-callout-subtitle-2` — `browser/browser/featureCallout.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `No extra windows. No tab flipping. Right-click this tab and choose “Add Split View.”`
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — ipprotection-locations-subview-promo.message (mear as300) · support-remote-experiments-see-about-studies (missing space before the placeable) · about-logging-unknown-error (bard :) · download-ui-confirm-quit-cancel-downloads-mac (stopje ,) · about-httpsonly-explanation-continue (útskeakele .) · experimental-features-custom-wallpaper-description (Nij-ljepblêdside .) · plus the 47 doubled-space str…
    - Source: `heading: Take protection further with { -mozilla-vpn-brand-name } message: Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `mear as300`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `heading: Getting close to your VPN limit message: You have { $usageLeft } GB of { $maxUsage } GB left this month.`
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `accesskey: S label: Share Ideas and Feedback…`
- `migration-chrome-windows-password-import-step1` — `browser/browser/migrationWizard.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Open the main menu <img data-l10n-name="chrome-icon-3dots"/> and go to Passwords and Autofill > Google Password Manager.`
- `migration-safari-password-import-step2` — `browser/browser/migrationWizard.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Select the <img data-l10n-name="safari-icon-3dots"/> button and choose “Export All Passwords”`
- `newtab-label-source-read-time` — `browser/browser/newtab/newtab.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `{ $source } · { $timeToRead } min`
- `no-page-title` — `browser/browser/pageInfo.ftl` — Dropped: no-page-title.value.
    - Source: `value: Untitled Page:`
- `choose-language-description` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Choose your preferred language for displaying pages`
- `download-always-ask-where2` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `accesskey: A label: Ask where to save files before downloading`
- `extension-controlled-enable` — `browser/browser/preferences/preferences.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `To enable the extension go to <img data-l10n-name="addons-icon"/> Add-ons in the <img data-l10n-name="menu-icon"/> menu.`
- `forms-master-pw-change` — `browser/browser/preferences/preferences.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `accesskey: M label: Change Master Password…`
- `preferences-doh-status-item-not-active` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `message: DNS over HTTPS is not working because we encountered an error ({ $reason }) while trying to use the provider { $name }`
- `preferences-doh-status-item-not-active-local` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `message: DNS over HTTPS is not working because we encountered an error ({ $reason }) while trying to use the local provider { $name }`
- `sync-mobile-promo` — `browser/browser/preferences/preferences.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Download Firefox for <img data-l10n-name="android-icon"/> <a data-l10n-name="android-link">Android</a> or <img data-l10n-name="ios-icon"/> <a data-l10n-name="ios-link">iOS</a> to sync with your mobile device.`
- `tab-group-menu-closed-tab-group` — `browser/browser/tabbrowser.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
    - Source: `label: { $tabGroupName } title: { $tabGroupName } — Closed`
- `third-party-tag-background` — `toolkit/toolkit/about/aboutThirdParty.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `(value): Background title: This module did not block the application because it was loaded in the background.`
- `fp-neterror-offline-intro-2` — `toolkit/toolkit/neterror/netError.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `{ -brand-short-name } can’t connect to the server at <strong>{ $hostname }</strong>.`
- `sec-error-no-key` — `toolkit/toolkit/neterror/nsserrors.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `The private key for this certificate cannot be found in key database`

---

## 4. Appendix

### Dismissed by hand (14)

- `aboutdialog-update-downloading` — `browser/browser/aboutDialog.ftl` — auto-suggest (2026-11-05): The translation uses the en dash (–), which is the measured fy-NL house dash (en 95 vs em 26).
- `add-exception-valid-long` — `security/manager/security/certificates/certManager.ftl` — auto-suggest (2026-11-05): The double space between sentences is also present in the en-US source.
- `autofill-delete-payment-method-os-prompt-windows` — `toolkit/toolkit/formautofill/formAutofill.ftl` — auto-suggest (2026-11-05): "bewarre betellingsgegevens" is an adequate rendering of "stored payment method information"; no meaning is changed.
- `expand-sidebar-on-hover` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `fxa-menu-sync-status-off` — `browser/browser/appmenu.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The original was probably already fine: the capitalised "Ut" follows the title-case "Off" in the source, and this tree writes capital Ú without its accent elsewhere ("Utwreidingen"), so lowercasing it to "út" wasn't wanted.
- `more-from-moz-solo-description` — `browser/browser/preferences/moreFromMozilla.ftl` — auto-suggest (2026-11-05): Here 'fergees' is used adverbially ('keppelje fergees'), where the uninflected form is correct; 'fergese' is the attributive inflected form.
- `opensearch-error-duplicate-desc` — `browser/browser/search.ftl` — auto-suggest (2026-11-05): The source itself says 'an engine', which 'in masine' renders faithfully.
- `opensearch-error-format-title` — `browser/browser/search.ftl` — auto-suggest (2026-11-05): 'Net falide formaat' correctly means 'invalid format'; the suggestion is just a synonym.
- `permissions-block-popups-exceptions-button4` — `browser/browser/preferences/preferences.ftl` — auto-suggest (2026-11-05): This string already uses 'trochliedingen', which is the suggested term.
- `popup-trigger-redirect-menuitem` — `browser/browser/browser.ftl` — auto-suggest (2026-11-05): Curly single quotes are the measured fy-NL quote convention (875 uses).
- `protections-vpn-banner-content` — `browser/browser/protections.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `sidebar-context-menu-unpin-extension` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `sidebar-open-tools-from-sidebar` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `sidebar-resize-splitter` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)

_One line each in `locales/fy-NL/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (61)

- `addon-confirm-install-some-unsigned-message` — `browser/browser/addonNotifications.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `genai-shortcuts-selected-warning-generic` — `browser/browser/genai.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `firefoxview-spotlight-promo-primarybutton` — `browser/browser/newtab/asrouter.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `fxa-menu-message-sync-devices-secondary-text2` — `browser/browser/newtab/asrouter.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `mr2022-onboarding-pin-image-alt` — `browser/browser/newtab/onboarding.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `places-locked-prompt` — `browser/browser/places.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `security-browsing-protection` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `safeb-blocked-addon-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `safeb-blocked-unwanted-page-title` — `browser/browser/safebrowsing/blockedSite.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `screenshots-generic-error-title` — `browser/browser/screenshots.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `tabbrowser-confirm-caretbrowsing-message` — `browser/browser/tabbrowser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `tabbrowser-empty-private-tab-title` — `browser/browser/tabbrowser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `about-debugging-setup-intro` — `devtools/client/aboutdebugging.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `css-compatibility-default-message` — `devtools/client/tooltips.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `inactive-css-not-grid-or-flex-container-or-multicol-container` — `devtools/client/tooltips.ftl` — raised by `legacy`, withdrawn 2026-09-03

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (366)

- `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl` — fixed 2026-11-05
- `confirm-discard-changes-dialog-title` — `browser/browser/aboutLogins.ftl` — fixed 2026-11-05
- `about-private-browsing-spotlight-basics-subtitle` — `browser/browser/aboutPrivateBrowsing.ftl` — fixed 2026-11-05
- `about-unloads-last-updated` — `browser/browser/aboutUnloads.ftl` — fixed 2026-11-05
- `appmenuitem-monitor-description2` — `browser/browser/appmenu.ftl` — fixed 2026-11-05
- `profiler-popup-presets-networking-with-logs-description` — `browser/browser/appmenu.ftl` — fixed 2026-11-05
- `filepicker-blocked-infobar` — `browser/browser/browser.ftl` — fixed 2026-11-05
- `quickactions-cmd-manageai` — `browser/browser/browser.ftl` — fixed 2026-11-05
- `default-browser-guidance-notification-info-page` — `browser/browser/defaultBrowserNotification.ftl` — fixed 2026-11-05
- `default-browser-guidance-notification-info-page` — `browser/browser/defaultBrowserNotification.ftl` — fixed 2026-11-05
- `bookmark-overlay-tags-empty-description` — `browser/browser/editBookmarkOverlay.ftl` — fixed 2026-11-05
- `sidebar-callout-survey-features-question` — `browser/browser/featureCallout.ftl` — fixed 2026-11-05
- `firefox-relay-and-fxa-popup-notification-second-sentence-with-domain-and-value-prop` — `browser/browser/firefoxRelay.ftl` — fixed 2026-11-05
- `genai-chatbot-summarize-footer-generic-subtitle` — `browser/browser/genai.ftl` — fixed 2026-11-05
- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — fixed 2026-11-05
- `ipprotection-feature-introduction-link-text-privacy-3` — `browser/browser/ipProtection.ftl` — fixed 2026-11-05
- `ipprotection-site-settings-callout-subtitle` — `browser/browser/ipProtection.ftl` — fixed 2026-11-05
- `taskbar-tabs-spotlight-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-11-05
- `home-mode-choice-custom-srd` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-05
- `newtab-widget-lists-menu-delete` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-05
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `mr1-onboarding-theme-description-dark` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `mr1-onboarding-theme-description-light` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `mr1-onboarding-theme-tooltip-dark` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `mr1-onboarding-theme-tooltip-light` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `onboarding-gratitude-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `onboarding-refresh-import-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-05
- `page-info-frame` — `browser/browser/pageInfo.ftl` — fixed 2026-11-05
- `page-info-page` — `browser/browser/pageInfo.ftl` — fixed 2026-11-05
- `policy-BlockAboutProfiles2` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-05
- `policy-DefaultDownloadDirectory` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-05
- `policy-DisableThirdPartyModuleBlocking` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-05
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-05
- `policy-LegacyProfiles` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-05
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — fixed 2026-11-05
- `confirm-browser-language-change-description` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-05
- `forms-master-pw-fips-desc` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-05
- `home-mode-choice-custom` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-05
