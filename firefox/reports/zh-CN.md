# Firefox l10n QA — zh-CN

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `443328fa7930` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `443328fa7930` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,969 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 359 |
| Strings | 17,969 |
| Missing strings | 194 |
| Obsolete strings | 0 |
| Files absent from the locale | 1 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Access keys not in their label | _skipped for this locale_ |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 27 |

### Completeness

**194 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 35
- `devtools/client/toolbox-options.ftl` — 18
- `toolkit/toolkit/about/aboutNetworking.ftl` — 15
- `toolkit/toolkit/about/url-classifier.ftl` — 13
- `toolkit/toolkit/neterror/netError.ftl` — 13
- `browser/browser/sharePanel.ftl` — 12
- `dom/chrome/dom/dom.properties` — 9
- `browser/browser/aiWindow.ftl` — 7
- `browser/browser/ipProtection.ftl` — 7
- `browser/browser/preferences/containers.ftl` — 7
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 7
- `browser/browser/firefoxView.ftl` — 6

**Files absent from the locale:**

- `browser/browser/sharePanel.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 979, `straight-double` 46, `curly-single` 41 | **curly-double** |
| apostrophe | `typographic` 46, `straight` 20 | _mixed_ |
| ellipsis | `char` 439, `ascii` 13 | **char** |
| dash | `em` 78, `en` 2 | **em** |
| fullwidth | `punctuation` 9514 | **punctuation** |
| register | `informal` 15, `formal` 1742 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **typography — 27 strings** — 27 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
  - Affected: `CSPViolationWithURI`, `CookieSameSiteValueInvalid2`, `FullscreenDeniedContainerNotAllowed`, `ImageMapCircleNegativeRadius`, `ImageMapCircleWrongNumberOfCoords`, `ImageMapPolyOddNumberOfCoords`, `ImageMapPolyWrongNumberOfCoords`, `ImageMapRectBoundsError`, `MediaLoadSourceMissingSrc`, `MediaLoadUnsupportedMimeType`, `MimeNotCss`, `MimeNotCssWarn` …and 15 more

---

## 3. Open findings (61)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 6 |
| 2 | Wrong content (says something other than the English) | 12 |
| 3 | Degraded language (grammar, spelling, terminology) | 19 |
| 4 | Cosmetic (typography, spacing) | 24 |

### A. Functional, markup, variables & plurals

- `genai-settings-chat-localhost-links` — `browser/browser/genai.ftl` — genai-settings-chat-localhost-links (genai.ftl) — leftover English possessive: "{ -vendor-short-name }’s Innovation…" → drop the ’s.
  - en-US: `’s`
- `origin-controls-toolbar-button-permission-needed` — `browser/browser/originControls.ftl` — origin-controls-toolbar-button-permission-needed (originControls.ftl) — dev-comment: the second line is intentional; ZH dropped "Permission needed" → add second line 需要授权.
  - en-US: `add second line 需要授权.`
- `safeb-blocked-addon-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — stray trailing </p> not in source → remove.
  - en-US: `remove.`
- `plugins-openh264-description` — `toolkit/toolkit/about/aboutAddons.ftl` — plugins-openh264-description (aboutPlugins.ftl and aboutAddons.ftl) — http://www.openh264.org/ → https:// (matches source).
- `about-processes-inference-process` — `toolkit/toolkit/about/aboutProcesses.ftl` — about-processes-inference-process (aboutProcesses.ftl) — "推理进程{ $pid }" drops the pid parentheses used by all sibling process names → 推理（{ $pid }）.
  - en-US: `推理（{ $pid }）.`
- `about-processes-utility-actor-js-oracle` — `toolkit/toolkit/about/aboutProcesses.ftl` — about-processes-utility-actor-js-oracle (aboutProcesses.ftl) — "JavaScript Oracle" → "Oracle" (dropped "JavaScript") → restore JavaScript Oracle.
  - en-US: `"Oracle"`

### B. Mistranslation, reversed meaning, wrong names & brand

- `link-preview-onboarding-callout-title` — `browser/browser/featureCallout.ftl` — link-preview-onboarding-callout-title (featureCallout.ftl) — "预览连接" (connection) → SUGGEST: "预览链接" (link; the next string correctly uses 链接).
  - en-US: `"预览链接"`
- `newtab-privacy-across-sites` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-across-sites (newtab.ftl) — "Across { $count } sites" → "包含 { $count } 个网站" (includes) → SUGGEST: "涉及 { $count } 个网站" (blocked across).
  - en-US: `"包含 { $count } 个网站"`
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — newtab-sports-widget-loading-more (newtab.ftl) — sports "matches" → "匹配项" (search-style "matching items") → SUGGEST: "比赛".
  - en-US: `"匹配项"`
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — fxa-qrcode-pair-step2-signin (fxaPairDevice.ftl) — bold button "Sync and save data" → "登录同步服务" (Sign in to sync service) → SUGGEST: render "Sync and save data" (verify against the Firefox mobile string). Medium confidence.
  - en-US: `"登录同步服务"`
- `screenshots-overlay-preview-face-label` — `browser/browser/screenshots.ftl` — screenshots-overlay-preview-face-label (screenshots.ftl) — screenshot "region" → "此地区" (geographic) → SUGGEST: "此区域" (as elsewhere in the file).
  - en-US: `"此地区"`
- `synced-tabs-context-open-all-in-tabs` — `browser/browser/syncedTabs.ftl` — synced-tabs-context-open-all-in-tabs (syncedTabs.ftl) — "Open All in Tabs" → "打开标签页组" (open tab group) → SUGGEST: "全部打开" (dev-comment says match places.ftl).
  - en-US: `"打开标签页组"`
- `tab-note-preview-expand` — `browser/browser/tabbrowser.ftl` — tab-note-preview-expand (tabbrowser.ftl) — "Read more" (expand truncated note, per comment) → "详细了解" (Learn more) → SUGGEST: "阅读全文" / "展开".
  - en-US: `"详细了解"`
- `xpath-unknown-function` — `dom/dom/xslt.ftl` — en-US "Invalid XSLT/XPath function." rendered "XSLT/XPath 尝试调用位置函数。" (invents "attempted to call a position function") → SUGGEST: "无效的 XSLT/XPath 函数。"
- `delete-ca-cert-impact` — `security/manager/security/certificates/certManager.ftl` — delete-ca-cert-impact (certManager.ftl) — garbled word order: "删除或不信任证书一个颁发机构（CA）证书" → SUGGEST: "…一个证书颁发机构（CA）证书…".
  - en-US: `"…一个证书颁发机构（CA）证书…".`
- `client-auth-window` — `security/manager/security/pippki/pippki.ftl` — client-auth-window (pippki.ftl) — title "User Identification Request" → "使用确认请求" (usage-confirmation) → SUGGEST: "用户身份识别请求".
  - en-US: `"使用确认请求"`
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — about-glean-label-for-ping-names (aboutGlean.ftl) — the <code> ping token was changed from events to event, the word "ping" dropped, and the sentence garbled. Restore: the default ping for <code>event</code> metrics is the <code>events</code> ping.
- `certificate-viewer-modulus` — `toolkit/toolkit/about/certviewer.ftl` — certificate-viewer-modulus (certviewer.ftl) — RSA "Modulus" → "模块" (software module) → SUGGEST: "模数".
  - en-US: `"模块"`

### C. Grammar, agreement & spelling

- `protocolhandler-mailto-handler-set` — `browser/browser/webProtocolHandler.ftl` — protocolhandler-mailto-handler-set (webProtocolHandler.ftl) — duplicated verb: "…{ -brand-short-name }打开{ $url }…打开吗？" → remove the trailing 打开.
  - en-US: `remove the trailing 打开.`
- `import-email-cert-prompt` — `security/manager/security/certificates/certManager.ftl` — import-email-cert-prompt (certManager.ftl) — duplicated "包含": "请选择包含要导入的包含某人邮件证书的文件" → drop one 包含.
  - en-US: `drop one 包含.`
- `place-database-last-vacuum-date` — `toolkit/toolkit/about/aboutSupport.ftl` — place-database-last-vacuum-date (aboutSupport.ftl) — "上次 Vacumm 日期" → Vacuum.
  - en-US: `Vacuum.`
- `contentanalysis-block-dialog-body-clipboard` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — contentanalysis-block-dialog-body-clipboard (contentanalysis.ftl) — "您不无权粘贴此内容" (double negative) → 您无权粘贴此内容.
  - en-US: `您无权粘贴此内容.`

### D. Terminology, register & consistency

- `onboarding-many-tabs-title` — `browser/browser/newtab/onboarding.ftl` — onboarding-many-tabs-title (onboarding.ftl) — "你的标签，由你而定" → 您.
  - en-US: `您.`
- `browsing-protection-group2` — `browser/browser/preferences/preferences.ftl` — deceptive content: security-browsing-protection 欺诈内容 vs browsing-protection-group2 诈骗内容 — pick one.
- `do-not-track-removal3` — `browser/browser/preferences/preferences.ftl` — tracker/Do-Not-Track: do-not-track-removal3 uses 追踪 vs siblings' 跟踪 (请勿跟踪); preferences-etp-level-warning-message & security-privacy-issue-warning-fingerprinters use 追踪器 vs the file's dominant 跟踪器. Standardize on 跟踪 / 跟踪器.
- `preferences-etp-level-warning-message` — `browser/browser/preferences/preferences.ftl` — tracker/Do-Not-Track: do-not-track-removal3 uses 追踪 vs siblings' 跟踪 (请勿跟踪); preferences-etp-level-warning-message & security-privacy-issue-warning-fingerprinters use 追踪器 vs the file's dominant 跟踪器. Standardize on 跟踪 / 跟踪器.
- `security-browsing-protection` — `browser/browser/preferences/preferences.ftl` — deceptive content: security-browsing-protection 欺诈内容 vs browsing-protection-group2 诈骗内容 — pick one.
- `security-privacy-issue-warning-fingerprinters` — `browser/browser/preferences/preferences.ftl` — tracker/Do-Not-Track: do-not-track-removal3 uses 追踪 vs siblings' 跟踪 (请勿跟踪); preferences-etp-level-warning-message & security-privacy-issue-warning-fingerprinters use 追踪器 vs the file's dominant 跟踪器. Standardize on 跟踪 / 跟踪器.
- `custom-avatar-alt` — `browser/browser/profiles.ftl` — avatar: custom-avatar-alt (profiles.ftl) uses 头像 vs the file's 图标 → 图标.
  - en-US: `图标.`
- `cfr-protections-panel-body` — `browser/browser/protectionsPanel.ftl` — "你的数据只由你掌握。…可保护您…" mixes 你/您 → use 您 throughout.
  - en-US: `use 您 throughout.`
- `reload-tab` — `browser/browser/tabContextMenu.ftl` — reload: reload-tab / reload-tabs (tabContextMenu.ftl) use 刷新 vs 重新加载 elsewhere → 重新加载.
  - en-US: `重新加载.`
- `reload-tabs` — `browser/browser/tabContextMenu.ftl` — reload: reload-tab / reload-tabs (tabContextMenu.ftl) use 刷新 vs 重新加载 elsewhere → 重新加载.
  - en-US: `重新加载.`
- `inactive-css-not-grid-or-flex-container-or-multicol-container` — `devtools/client/tooltips.ftl` — multicolumn / flex / grid (devtools): inactive-css-not-grid-or-flex-container-or-multicol-container uses 多栏 + English "Flex 容器、Grid 容器" vs siblings' 多列 + 弹性/网格 → align to 多列 / 弹性容器 / 网格容器.
- `delete-user-cert-impact` — `security/manager/security/certificates/certManager.ftl` — delete-user-cert-impact (certManager.ftl) — "您将无法使用它来标识你自己" → 您自己.
  - en-US: `您自己.`
- `edit-trust-ca` — `security/manager/security/certificates/certManager.ftl` — Certificate Authority: download-cert-message 认证机构 vs download-cert-message-desc/edit-trust-ca 颁发机构 → 颁发机构.
  - en-US: `颁发机构.`
- `download-cert-message` — `security/manager/security/pippki/pippki.ftl` — Certificate Authority: download-cert-message 认证机构 vs download-cert-message-desc/edit-trust-ca 颁发机构 → 颁发机构.
  - en-US: `颁发机构.`
- `download-cert-message-desc` — `security/manager/security/pippki/pippki.ftl` — Certificate Authority: download-cert-message 认证机构 vs download-cert-message-desc/edit-trust-ca 颁发机构 → 颁发机构.
  - en-US: `颁发机构.`

### E. Typography, punctuation & spacing

- `appmenu-fxa-setup-sync` — `browser/browser/appmenu.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
  - Current: `...`
  - en-US: `…`
- `main-context-menu-video-take-snapshot` — `browser/browser/browserContext.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
  - Current: `...`
  - en-US: `…`
- `clear-data-for-site-cookies` — `browser/browser/clearDataForSite.ftl` — List-item terminal 。 — clear-data-for-site-cookies (clearDataForSite.ftl) carries a trailing 。 the sibling list items don't → drop for consistency. (minor)
  - en-US: `drop for consistency.`
- `firefox-relay-mask-generation-failed` — `browser/browser/firefoxRelay.ftl` — Stray space. options-enable-f12-tooltip (toolbox-options.ftl, space after 「，」); firefox-relay-mask-generation-failed (firefoxRelay.ftl, space after 「。」before HTTP).
- `ipprotection-come-back-title` — `browser/browser/ipProtection.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
- `cfr-doorhanger-bookmark-fxa-link-text` — `browser/browser/newtab/asrouter.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
  - Current: `...`
  - en-US: `…`
- `amo-picker-subtitle` — `browser/browser/newtab/onboarding.ftl` — Reversed / mismatched curly quotes (opening/closing swapped or mixed): load-module-help-root-certs-module-name (deviceManager.ftl, ”Root Certs“), amo-picker-subtitle (onboarding.ftl, ”小程序“), unified-extensions-item-open-menu (unifiedExtensions.ftl, ”{ $extensionName }”), profiles-delete-profile-confirm (aboutProfiles.ftl, curly “ opened, straight " closed) → use “…”.
  - en-US: `use “…”.`
- `performance-default-content-process-count` — `browser/browser/preferences/preferences.ftl` — Half-width parentheses / comma. performance-default-content-process-count "(默认)" → （默认）; about-mozilla-title-6-27/-from-6-27 "书, 6:27" → 书，.
- `speech-dispatcher-lib-too-old` — `browser/browser/speechDispatcher.ftl` — Wrong terminal punctuation. speech-dispatcher-lib-too-old (speechDispatcher.ftl) ends with 「，」→ 。.
  - en-US: `。.`
- `unified-extensions-item-open-menu` — `browser/browser/unifiedExtensions.ftl` — Reversed / mismatched curly quotes (opening/closing swapped or mixed): load-module-help-root-certs-module-name (deviceManager.ftl, ”Root Certs“), amo-picker-subtitle (onboarding.ftl, ”小程序“), unified-extensions-item-open-menu (unifiedExtensions.ftl, ”{ $extensionName }”), profiles-delete-profile-confirm (aboutProfiles.ftl, curly “ opened, straight " closed) → use “…”.
  - en-US: `use “…”.`
- `about-debugging-setup-usb-status-updating` — `devtools/client/aboutdebugging.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
  - Current: `...`
  - en-US: `…`
- `about-debugging-sidebar-item-connect-button-connecting` — `devtools/client/aboutdebugging.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
  - Current: `...`
  - en-US: `…`
- `options-enable-f12-tooltip` — `devtools/client/toolbox-options.ftl` — Stray space. options-enable-f12-tooltip (toolbox-options.ftl, space after 「，」); firefox-relay-mask-generation-failed (firefoxRelay.ftl, space after 「。」before HTTP).
- `xpath-bad-argument-count` — `dom/dom/xslt.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
- `xslt-parse-failure` — `dom/dom/xslt.ftl` — stylesheet term — 样式表单 (= 样式表+form) in xslt-parse-failure/-bad-recursion/-network-error/-load-recursion/-load-blocked-error/-loading-error (xslt.ftl) → 样式表 (6 strings).
  - en-US: `样式表`
- `devinfo-hwversion` — `security/manager/security/certificates/deviceManager.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
- `devmgr-button-enable-fips` — `security/manager/security/certificates/deviceManager.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
- `load-device-modname-default` — `security/manager/security/certificates/deviceManager.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
- `load-module-help-root-certs-module-name` — `security/manager/security/certificates/deviceManager.ftl` — Reversed / mismatched curly quotes (opening/closing swapped or mixed): load-module-help-root-certs-module-name (deviceManager.ftl, ”Root Certs“), amo-picker-subtitle (onboarding.ftl, ”小程序“), unified-extensions-item-open-menu (unifiedExtensions.ftl, ”{ $extensionName }”), profiles-delete-profile-confirm (aboutProfiles.ftl, curly “ opened, straight " closed) → use “…”.
  - en-US: `use “…”.`
- `about-mozilla-title-6-27` — `toolkit/toolkit/about/aboutMozilla.ftl` — Half-width parentheses / comma. performance-default-content-process-count "(默认)" → （默认）; about-mozilla-title-6-27/-from-6-27 "书, 6:27" → 书，.
- `profiles-delete-profile-confirm` — `toolkit/toolkit/about/aboutProfiles.ftl` — Reversed / mismatched curly quotes (opening/closing swapped or mixed): load-module-help-root-certs-module-name (deviceManager.ftl, ”Root Certs“), amo-picker-subtitle (onboarding.ftl, ”小程序“), unified-extensions-item-open-menu (unifiedExtensions.ftl, ”{ $extensionName }”), profiles-delete-profile-confirm (aboutProfiles.ftl, curly “ opened, straight " closed) → use “…”.
  - en-US: `use “…”.`
- `about-webrtc-aec-logging-unavailable-sandbox` — `toolkit/toolkit/about/aboutWebrtc.ftl` — CJK↔Latin spacing (missing space around Latin/acronyms, inconsistent with same file): devmgr-button-enable-fips/-disable-fips/load-device-modname-default + devinfo-hwversion/-fwversion (deviceManager.ftl, e.g. 启用FIPS → 启用 FIPS), xpath-bad-argument-count/-bad-extension-function (xslt.ftl), ipprotection-come-back-title (ipProtection.ftl, 内置VPN → 内置 VPN), about-webrtc-aec-logging-unavailable-sandbox…
- `printui-print-progress-indicator` — `toolkit/toolkit/printing/printUI.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
  - Current: `...`
  - en-US: `…`
- `printui-system-dialog-link` — `toolkit/toolkit/printing/printUI.ftl` — ASCII ... → …. appmenu-fxa-setup-sync (appmenu.ftl), main-context-menu-video-take-snapshot (browserContext.ftl), cfr-doorhanger-bookmark-fxa-link-text (asrouter.ftl), about-debugging-sidebar-item-connect-button-connecting / about-debugging-setup-usb-status-updating (aboutdebugging.ftl), printui-system-dialog-link / printui-print-progress-indicator (printUI.ftl).
  - Current: `...`
  - en-US: `…`

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Resolved to date (26)

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
- `url-classifier-search-result-list` — `toolkit/toolkit/about/url-classifier.ftl` — fixed 2026-07-28
- `profile-prompt` — `toolkit/toolkit/global/createProfileWizard.ftl` — fixed 2026-07-28
- `language-name-km` — `toolkit/toolkit/intl/languageNames.ftl` — fixed 2026-07-28
- `language-name-se` — `toolkit/toolkit/intl/languageNames.ftl` — fixed 2026-07-28
- `region-name-as` — `toolkit/toolkit/intl/regionNames.ftl` — fixed 2026-07-28
- `region-name-dm` — `toolkit/toolkit/intl/regionNames.ftl` — fixed 2026-07-28
- `region-name-na` — `toolkit/toolkit/intl/regionNames.ftl` — fixed 2026-07-28
