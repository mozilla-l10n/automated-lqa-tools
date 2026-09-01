# Firefox l10n QA — zh-CN

| | |
|---|---|
| **Generated** | 2026-09-01 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `38d706ee4004` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `4aab78fe6cf4` |
| **Previous run** | 2026-08-31 @ `67b14d26eb36` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,994 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for zh-CN: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 359 |
| Strings | 17,994 |
| Missing strings | 225 |
| Obsolete strings | 0 |
| Files absent from the locale | 3 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 11 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | _skipped for this locale_ |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 27 |

### Completeness

**225 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 45
- `toolkit/services/aboutSyncLog.ftl` — 26
- `devtools/client/toolbox-options.ftl` — 18
- `browser/browser/sharePanel.ftl` — 17
- `toolkit/toolkit/about/aboutNetworking.ftl` — 15
- `toolkit/toolkit/about/url-classifier.ftl` — 12
- `toolkit/toolkit/neterror/netError.ftl` — 12
- `dom/chrome/dom/dom.properties` — 9
- `browser/browser/preferences/preferences.ftl` — 8
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 7
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/ipProtection.ftl` — 6

**Files absent from the locale:**

- `browser/browser/sharePanel.ftl`
- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 980, `straight-double` 46, `curly-single` 41 | **curly-double** |
| apostrophe | `typographic` 46, `straight` 20 | _mixed_ |
| ellipsis | `char` 441, `ascii` 13 | **char** |
| dash | `em` 79, `en` 2 | **em** |
| fullwidth | `punctuation` 9534 | **punctuation** |
| register | `informal` 16, `formal` 1746 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 27 strings** — 27 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `CSPViolationWithURI`, `CookieSameSiteValueInvalid2`, `FullscreenDeniedContainerNotAllowed`, `ImageMapCircleNegativeRadius`, `ImageMapCircleWrongNumberOfCoords`, `ImageMapPolyOddNumberOfCoords`, `ImageMapPolyWrongNumberOfCoords`, `ImageMapRectBoundsError`, `MediaLoadSourceMissingSrc`, `MediaLoadUnsupportedMimeType`, `MimeNotCss`, `MimeNotCssWarn` …and 15 more

---

## 3. Open findings (54)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 4 |
| 2 | Wrong content (says something other than the English) | 8 |
| 3 | Degraded language (grammar, spelling, terminology) | 7 |
| 4 | Cosmetic (typography, spacing) | 35 |

### A. Functional, markup, variables & plurals

- `about-logins-confirm-remove-all-dialog-title` — `browser/browser/aboutLogins.ftl` — `about-logins-confirm-remove-all-dialog-title` has plural variant ['one'], which zh-CN does not have
    - Current: `{$count ->} [one] 确定要移除 { $count } 条登录信息吗？ [other] 确定要移除全部共 { $count } 条登录信息吗？`
    - Source: `{$count ->} [one] Remove { $count } login? [other] Remove all { $count } logins?`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `pending-crash-reports-message-new` — `browser/browser/contentCrash.ftl` — `pending-crash-reports-message-new` has plural variant ['one'], which zh-CN does not have
    - Current: `{$reportCount ->} [one] 您最近有一份未发送的崩溃报告 [other] 您最近有 { $reportCount } 份未发送的崩溃报告`
    - Source: `{$reportCount ->} [one] You have a recent unsent crash report [other] You have { $reportCount } recent unsent crash reports`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — `downloads-files-not-downloaded` has plural variant ['one'], which zh-CN does not have
    - Current: `{$num ->} [other] 未下载 { $num } 个文件。 [one] 未下载文件。`
    - Source: `{$num ->} [one] File not downloaded. [other] { $num } files not downloaded.`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `firefoxview-search-results-count` — `browser/browser/firefoxView.ftl` — `firefoxview-search-results-count` has plural variant ['one'], which zh-CN does not have
    - Current: `{$count ->} [one] { $count } 个网站 [other] { $count } 个网站`
    - Source: `{$count ->} [one] { $count } site [other] { $count } sites`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `genai-settings-chat-localhost-links` — `browser/browser/genai.ftl` — genai-settings-chat-localhost-links (genai.ftl) — leftover English possessive: "{ -vendor-short-name }’s Innovation…" → drop the ’s.
    - Source: `Bring your own private local chatbot such as <a data-l10n-name="link1">llamafile</a> from { -vendor-short-name }’s Innovation group.`
    - Suggest: `’s`
- `migration-wizard-progress-success-history` — `browser/browser/migrationWizard.ftl` — `migration-wizard-progress-success-history` has plural variant ['one'], which zh-CN does not have
    - Current: `{$maxAgeInDays ->} [one] 昨天以来的数据 [other] 过去 { $maxAgeInDays } 天内的数据`
    - Source: `{$maxAgeInDays ->} [one] From the last day [other] From the last { $maxAgeInDays } days`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `origin-controls-toolbar-button-permission-needed` — `browser/browser/originControls.ftl` — origin-controls-toolbar-button-permission-needed (originControls.ftl) — dev-comment: the second line is intentional; ZH dropped "Permission needed" → add second line 需要授权.
    - Source: `label: { $extensionTitle } tooltiptext: { $extensionTitle } Permission needed`
    - Suggest: `add second line 需要授权.`
- `general-meta-tags` — `browser/browser/pageInfo.ftl` — `general-meta-tags` (`.value`) has plural variant ['one'], which zh-CN does not have
    - Current: `{$tags ->} [one] 元信息（1 个标签） [other] 元信息（{ $tags } 个标签）`
    - Source: `value: {$tags ->} [one] Meta (1 tag) [other] Meta ({ $tags } tags)`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `media-animated-image-type` — `browser/browser/pageInfo.ftl` — `media-animated-image-type` (`.value`) has plural variant ['one'], which zh-CN does not have
    - Current: `{$frames ->} [one] { $type } 图像（动画，{ $frames } 帧） [other] { $type } 图像（动画，{ $frames } 帧）`
    - Source: `value: {$frames ->} [one] { $type } Image (animated, { $frames } frame) [other] { $type } Image (animated, { $frames } frames)`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `properties-general-size` — `browser/browser/pageInfo.ftl` — `properties-general-size` (`.value`) has plural variant ['one'], which zh-CN does not have
    - Current: `{$bytes ->} [one] { $kb } KB ({ $bytes } 字节) [other] { $kb } KB ({ $bytes } 字节)`
    - Source: `value: {$bytes ->} [one] { $kb } KB ({ $bytes } byte) [other] { $kb } KB ({ $bytes } bytes)`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `security-visits-number` — `browser/browser/pageInfo.ftl` — `security-visits-number` has plural variant ['one'], which zh-CN does not have
    - Current: `{$visits ->} [0] 否 [one] 是，1 次 [other] 是，{ $visits } 次`
    - Source: `{$visits ->} [0] No [one] Yes, once [other] Yes, { $visits } times`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `containers-disable-alert-desc` — `browser/browser/preferences/preferences.ftl` — `containers-disable-alert-desc` has plural variant ['one'], which zh-CN does not have
    - Current: `{$tabCount ->} [one] 如果您现在禁用身份标签页，将有 { $tabCount } 个容器标签页被关闭。您确实要禁用身份标签页吗？ [other] 如果您现在禁用身份标签页，将有 { $tabCount } 个容器标签页被关闭。您确实要禁用身份标签页吗？`
    - Source: `{$tabCount ->} [one] If you disable Container Tabs now, { $tabCount } container tab will be closed. Are you sure you want to disable Container Tabs? [other] If you disable Container Tabs now, { $tabCount } container tab…`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `containers-disable-alert-ok-button` — `browser/browser/preferences/preferences.ftl` — `containers-disable-alert-ok-button` has plural variant ['one'], which zh-CN does not have
    - Current: `{$tabCount ->} [one] 关闭 { $tabCount } 个身份标签页 [other] 关闭 { $tabCount } 个身份标签页`
    - Source: `{$tabCount ->} [one] Close { $tabCount } Container Tab [other] Close { $tabCount } Container Tabs`
    - zh-CN has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `about-processes-inference-process` — `toolkit/toolkit/about/aboutProcesses.ftl` — about-processes-inference-process (aboutProcesses.ftl) — "推理进程{ $pid }" drops the pid parentheses used by all sibling process names → 推理（{ $pid }）.
    - Source: `Inference ({ $pid })`
    - Suggest: `推理（{ $pid }）.`
- `about-processes-utility-actor-js-oracle` — `toolkit/toolkit/about/aboutProcesses.ftl` — about-processes-utility-actor-js-oracle (aboutProcesses.ftl) — "JavaScript Oracle" → "Oracle" (dropped "JavaScript") → restore JavaScript Oracle.
    - Source: `JavaScript Oracle`
    - Suggest: `"Oracle"`

### B. Mistranslation, reversed meaning, wrong names & brand

- `newtab-privacy-across-sites` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-across-sites (newtab.ftl) — "Across { $count } sites" → "包含 { $count } 个网站" (includes) → SUGGEST: "涉及 { $count } 个网站" (blocked across).
    - Source: `{$count ->} [one] Across { $count } site [other] Across { $count } sites`
    - Suggest: `"包含 { $count } 个网站"`
- `synced-tabs-context-open-all-in-tabs` — `browser/browser/syncedTabs.ftl` — synced-tabs-context-open-all-in-tabs (syncedTabs.ftl) — "Open All in Tabs" → "打开标签页组" (open tab group) → SUGGEST: "全部打开" (dev-comment says match places.ftl).
    - Source: `accesskey: O label: Open All in Tabs`
    - Suggest: `"打开标签页组"`
- `tab-note-preview-expand` — `browser/browser/tabbrowser.ftl` — tab-note-preview-expand (tabbrowser.ftl) — "Read more" (expand truncated note, per comment) → "详细了解" (Learn more) → SUGGEST: "阅读全文" / "展开".
    - Source: `Read more`
    - Suggest: `"详细了解"`
- `list-empty-get-extensions-promo` — `toolkit/toolkit/about/aboutAddons.ftl` — "improve focus, privacy and more" is rendered as "更专注、更隐私、更安全", inventing "security" in place of "and more".
    - Current: `更专注、更隐私、更安全`
    - Source: `heading: A few extensions go a long way message: We’ve got recommendations to help you improve focus, privacy and more.`
    - Suggest: `更专注、更好保护隐私等`
    - The en-US source lists focus, privacy and "more"; "更安全" (more secure) is content not present in the source.
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — about-glean-label-for-ping-names (aboutGlean.ftl) — the <code> ping token was changed from events to event, the word "ping" dropped, and the sentence garbled. Restore: the default ping for <code>event</code> metrics is the <code>events</code> ping.
    - Source: `Select from the preceding list the ping your instrumentation is in. If it’s in a <a data-l10n-name="custom-ping-link">custom ping</a>, choose that one. Otherwise, the default for <code>event</code> metrics is the <code>…`
- `certificate-viewer-modulus` — `toolkit/toolkit/about/certviewer.ftl` — certificate-viewer-modulus (certviewer.ftl) — RSA "Modulus" → "模块" (software module) → SUGGEST: "模数".
    - Source: `Modulus`
    - Suggest: `"模块"`
- `url-classifier-content-classifier-loading-url` — `toolkit/toolkit/about/url-classifier.ftl` — "Loading URL" is a noun phrase (the URL that loads the tested URL), but it is translated as the progress message "正在加载 URL".
    - Current: `正在加载 URL`
    - Source: `Loading URL`
    - Suggest: `加载方 URL`
    - Developer comment says this is the URL that loads the URL being tested (a frame's URL), i.e. a label, not a status message.
- `moz-box-link-opens-in-new-tab` — `toolkit/toolkit/global/mozBoxBase.ftl` — "a new tab" is translated as "新建窗口" (new window) instead of a new tab.
    - Current: `新建窗口打开`
    - Source: `Opens in a new tab`
    - Suggest: `在新标签页中打开`
    - en-US says "Opens in a new tab"; the translation says window, which is a different UI concept.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `onboarding-many-tabs-title` — `browser/browser/newtab/onboarding.ftl` — onboarding-many-tabs-title (onboarding.ftl) — "你的标签，由你而定" → 您.
    - Source: `Your tabs, your way`
    - Suggest: `您.`
- `browsing-protection-group2` — `browser/browser/preferences/preferences.ftl` — deceptive content: security-browsing-protection 欺诈内容 vs browsing-protection-group2 诈骗内容 — pick one.
    - Source: `description: Dangerous sites and downloads can put your data and device at risk. { -brand-short-name } automatically blocks them, and warns you about risky or unwanted software. label: Deceptive content and dangerous so…`
- `cfr-protections-panel-body` — `browser/browser/protectionsPanel.ftl` — "你的数据只由你掌握。…可保护您…" mixes 你/您 → use 您 throughout.
    - Source: `Keep your data to yourself. { -brand-short-name } protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `use 您 throughout.`
- `reload-tab` — `browser/browser/tabContextMenu.ftl` — reload: reload-tab / reload-tabs (tabContextMenu.ftl) use 刷新 vs 重新加载 elsewhere → 重新加载.
    - Source: `accesskey: R label: Reload Tab`
    - Suggest: `重新加载.`
- `reload-tabs` — `browser/browser/tabContextMenu.ftl` — reload: reload-tab / reload-tabs (tabContextMenu.ftl) use 刷新 vs 重新加载 elsewhere → 重新加载.
    - Source: `accesskey: R label: Reload Tabs`
    - Suggest: `重新加载.`
- `inactive-css-not-grid-or-flex-container-or-multicol-container` — `devtools/client/tooltips.ftl` — multicolumn / flex / grid (devtools): inactive-css-not-grid-or-flex-container-or-multicol-container uses 多栏 + English "Flex 容器、Grid 容器" vs siblings' 多列 + 弹性/网格 → align to 多列 / 弹性容器 / 网格容器.
    - Source: `<strong>{ $property }</strong> has no effect on this element since it’s not a flex container, a grid container, or a multi-column container.`
- `download-cert-message-desc` — `security/manager/security/pippki/pippki.ftl` — Certificate Authority: download-cert-message 认证机构 vs download-cert-message-desc/edit-trust-ca 颁发机构 → 颁发机构.
    - Source: `Before trusting this CA for any purpose, you should examine its certificate and its policy and procedures (if available).`
    - Suggest: `颁发机构.`

### E. Typography, punctuation & spacing

- `appmenu-fxa-setup-sync` — `browser/browser/appmenu.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
    - Current: `...`
    - Source: `label: Turn On Syncing…`
    - Suggest: `…`
- `main-context-menu-video-take-snapshot` — `browser/browser/browserContext.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
    - Current: `...`
    - Source: `accesskey: S label: Take Snapshot…`
    - Suggest: `…`
- `clear-data-for-site-cookies` — `browser/browser/clearDataForSite.ftl` — List-item terminal 。 — clear-data-for-site-cookies (clearDataForSite.ftl) carries a trailing 。 the sibling list items don't → drop for consistency. (minor)
    - Source: `Cookies and site data, which may sign you out of the site`
    - Suggest: `drop for consistency.`
- `firefox-relay-mask-generation-failed` — `browser/browser/firefoxRelay.ftl` — Stray space. options-enable-f12-tooltip (toolbox-options.ftl, space after 「，」); firefox-relay-mask-generation-failed (firefoxRelay.ftl, space after 「。」before HTTP).
    - Source: `{ -relay-brand-name } could not generate a new mask. HTTP error code: { $status }.`
- `ipprotection-come-back-title` — `browser/browser/ipProtection.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
    - Source: `Come back to try built-in VPN`
- `cfr-doorhanger-bookmark-fxa-link-text` — `browser/browser/newtab/asrouter.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
    - Current: `...`
    - Source: `Sync bookmarks now…`
    - Suggest: `…`
- `amo-picker-subtitle` — `browser/browser/newtab/onboarding.ftl` — Reversed / mismatched curly quotes (opening/closing swapped or mixed): load-module-help-root-certs-module-name (deviceManager.ftl, ”Root Certs“), amo-picker-subtitle (onboarding.ftl, ”小程序“), unified-extensions-item-open-menu (unifiedExtensions.ftl, ”{ $extensionName }”), profiles-delete-profile-confirm (aboutProfiles.ftl, curly “ opened, straight " closed) → use “…”.
    - Source: `Extensions are like apps for your browser, and they let you protect passwords, download videos, find deals, block annoying ads, change how your browser looks, and much more.`
    - Suggest: `use “…”.`
- `performance-default-content-process-count` — `browser/browser/preferences/preferences.ftl` — Half-width parentheses / comma. performance-default-content-process-count "(默认)" → （默认）; about-mozilla-title-6-27/-from-6-27 "书, 6:27" → 书，.
    - Source: `label: { $num } (default)`
- `speech-dispatcher-lib-too-old` — `browser/browser/speechDispatcher.ftl` — Wrong terminal punctuation. speech-dispatcher-lib-too-old (speechDispatcher.ftl) ends with 「，」→ 。.
    - Source: `You can’t use speech synthesis because Speech Dispatcher needs to be updated.`
    - Suggest: `。.`
- `unified-extensions-item-open-menu` — `browser/browser/unifiedExtensions.ftl` — Reversed / mismatched curly quotes (opening/closing swapped or mixed): load-module-help-root-certs-module-name (deviceManager.ftl, ”Root Certs“), amo-picker-subtitle (onboarding.ftl, ”小程序“), unified-extensions-item-open-menu (unifiedExtensions.ftl, ”{ $extensionName }”), profiles-delete-profile-confirm (aboutProfiles.ftl, curly “ opened, straight " closed) → use “…”.
    - Source: `aria-label: Open menu for { $extensionName }`
    - Suggest: `use “…”.`
- `about-debugging-setup-usb-status-updating` — `devtools/client/aboutdebugging.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
    - Current: `...`
    - Source: `Updating…`
    - Suggest: `…`
- `about-debugging-sidebar-item-connect-button-connecting` — `devtools/client/aboutdebugging.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
    - Current: `...`
    - Source: `Connecting…`
    - Suggest: `…`
- `options-enable-f12-tooltip` — `devtools/client/toolbox-options.ftl` — Stray space. options-enable-f12-tooltip (toolbox-options.ftl, space after 「，」); firefox-relay-mask-generation-failed (firefoxRelay.ftl, space after 「。」before HTTP).
    - Source: `title: Turning this option on will bind the F12 key to open or close the DevTools toolbox`
- `xpath-bad-argument-count` — `dom/dom/xslt.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
    - Source: `An XPath function was called with the wrong number of arguments.`
- `xslt-parse-failure` — `dom/dom/xslt.ftl` — stylesheet term — 样式表单 (= 样式表+form) in xslt-parse-failure/-bad-recursion/-network-error/-load-recursion/-load-blocked-error/-loading-error (xslt.ftl) → 样式表 (6 strings).
    - Source: `Parsing an XSLT stylesheet failed.`
    - Suggest: `样式表`
- `devinfo-hwversion` — `security/manager/security/certificates/deviceManager.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
    - Source: `label: HW Version`
- `devmgr-button-enable-fips` — `security/manager/security/certificates/deviceManager.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
    - Source: `accesskey: F label: Enable FIPS`
- `load-device-modname-default` — `security/manager/security/certificates/deviceManager.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
    - Source: `value: New PKCS#11 Module`
- `load-module-help-root-certs-module-name` — `security/manager/security/certificates/deviceManager.ftl` — Reversed / mismatched curly quotes (opening/closing swapped or mixed): load-module-help-root-certs-module-name (deviceManager.ftl, ”Root Certs“), amo-picker-subtitle (onboarding.ftl, ”小程序“), unified-extensions-item-open-menu (unifiedExtensions.ftl, ”{ $extensionName }”), profiles-delete-profile-confirm (aboutProfiles.ftl, curly “ opened, straight " closed) → use “…”.
    - Source: `value: ‘Root Certs‘ is reserved and cannot be used as the module name.`
    - Suggest: `use “…”.`
- `about-mozilla-title-6-27` — `toolkit/toolkit/about/aboutMozilla.ftl` — Half-width parentheses / comma. performance-default-content-process-count "(默认)" → （默认）; about-mozilla-title-6-27/-from-6-27 "书, 6:27" → 书，.
    - Source: `The Book of Mozilla, 6:27`
- `profiles-delete-profile-confirm` — `toolkit/toolkit/about/aboutProfiles.ftl` — Reversed / mismatched curly quotes (opening/closing swapped or mixed): load-module-help-root-certs-module-name (deviceManager.ftl, ”Root Certs“), amo-picker-subtitle (onboarding.ftl, ”小程序“), unified-extensions-item-open-menu (unifiedExtensions.ftl, ”{ $extensionName }”), profiles-delete-profile-confirm (aboutProfiles.ftl, curly “ opened, straight " closed) → use “…”.
    - Source: `Deleting a profile will remove the profile from the list of available profiles and cannot be undone. You may also choose to delete the profile data files, including your settings, certificates and other user-related dat…`
    - Suggest: `use “…”.`
- `about-webrtc-aec-logging-unavailable-sandbox` — `toolkit/toolkit/about/aboutWebrtc.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
    - Source: `The environment variable MOZ_DISABLE_CONTENT_SANDBOX=1 is required to export AEC logs. Only set this variable if you understand the possible risks.`
- `printui-print-progress-indicator` — `toolkit/toolkit/printing/printUI.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
    - Current: `...`
    - Source: `Printing…`
    - Suggest: `…`
- `printui-system-dialog-link` — `toolkit/toolkit/printing/printUI.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
    - Current: `...`
    - Source: `Print using the system dialog…`
    - Suggest: `…`

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/zh-CN/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (47)

- `link-preview-onboarding-callout-title` — `browser/browser/featureCallout.ftl` — fixed 2026-08-24
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — fixed 2026-08-24
- `do-not-track-removal3` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `preferences-etp-level-warning-message` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `security-browsing-protection` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `security-privacy-issue-warning-fingerprinters` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `custom-avatar-alt` — `browser/browser/profiles.ftl` — fixed 2026-08-24
- `safeb-blocked-addon-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — fixed 2026-08-24
- `screenshots-overlay-preview-face-label` — `browser/browser/screenshots.ftl` — fixed 2026-08-24
- `protocolhandler-mailto-handler-set` — `browser/browser/webProtocolHandler.ftl` — fixed 2026-08-24
- `xpath-unknown-function` — `dom/dom/xslt.ftl` — fixed 2026-08-24
- `delete-ca-cert-impact` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `delete-user-cert-impact` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `edit-trust-ca` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `import-email-cert-prompt` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `client-auth-window` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `download-cert-message` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `plugins-openh264-description` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-08-24
- `place-database-last-vacuum-date` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-08-24
- `contentanalysis-block-dialog-body-clipboard` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — fixed 2026-08-24
- `about-logins-import-report-description2` — `browser/browser/aboutLogins.ftl` — fixed 2026-07-28
- `spotlight-better-internet-body` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-07-28
- `newtab-sports-widget-message-survey-title` — `browser/browser/newtab/newtab.ftl` — fixed 2026-07-28
- `permissions-for` — `browser/browser/pageInfo.ftl` — fixed 2026-07-28
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-28
- `history-remember-option-never2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-28
- `update-application-version` — `browser/browser/preferences/preferences.ftl` — fixed 2026-07-28
- `accessibility-text-label-issue-form-visible` — `devtools/client/accessibility.ftl` — fixed 2026-07-28
- `styleeditor-no-stylesheet-tip` — `devtools/client/styleeditor.ftl` — fixed 2026-07-28
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — fixed 2026-07-28
- `xpath-unclosed-literal` — `dom/dom/xslt.ftl` — fixed 2026-07-28
- `delete-ca-cert-impact` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-28
- `exception-mgr-cert-location-url` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-07-28
- `change-password-token` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-07-28
- `about-logging-invalid-output` — `toolkit/toolkit/about/aboutLogging.ftl` — fixed 2026-07-28
- `touch-warning` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-07-28
- `wheel-warning` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-07-28
- `about-telemetry-stack-title` — `toolkit/toolkit/about/aboutTelemetry.ftl` — fixed 2026-07-28
- `abuse-report-policy-suggestions` — `toolkit/toolkit/about/abuseReports.ftl` — fixed 2026-07-28
