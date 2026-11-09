# Firefox l10n QA — ko

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `74047c5347bc` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcf134b6aeea` |
| **Previous run** | 2026-11-09 @ `3685bd005e67` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 16,875 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ko: [Firefox for Android](android.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Files | 331 |
| Strings | 16,875 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 4 |
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | _skipped for this locale_ |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 5 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 406, `straight-double` 207, `curly-single` 89 | _mixed_ |
| apostrophe | `typographic` 89, `straight` 91 | _mixed_ |
| ellipsis | `char` 394, `ascii` 5 | **char** |
| dash | `em` 44, `en` 1 | **em** |
| nbsp | `space-before-punctuation` 5 | **space-before-punctuation** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (295)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 159 |
| 2 | Wrong content (says something other than the English) | 124 |
| 3 | Degraded language (grammar, spelling, terminology) | 3 |
| 4 | Cosmetic (typography, spacing) | 9 |

### A. Functional, markup, variables & plurals

- `login-list-filtered-count2` — `browser/browser/aboutLogins.ftl` — `login-list-filtered-count2` has plural variant ['one'], which ko does not have
    - Current: `{$total ->} [one] { $count } / { $total } 비밀번호 [other] { $count } / { $total } 비밀번호`
    - Source: `{$total ->} [one] { $count } of { $total } password [other] { $count } of { $total } passwords`
    - ko has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `about-private-browsing-felt-privacy-v1-info-header` — `browser/browser/aboutPrivateBrowsing.ftl` — 'Leave no traces on this device' became an unqualified 'leave no traces'.
    - Current: `흔적 남기지 않기`
    - Source: `Leave no traces on this device`
    - Suggest: `이 기기에 흔적 남기지 않기`
    - Without 'on this device' the heading promises no traces anywhere. The product explicitly says sites, ISPs and employers can still see activity, so this is a privacy guarantee Firefox does not give.
- `welcome-back-restore-some-label` — `browser/browser/aboutSessionRestore.ftl` — 'Restore only the ones you want' became 'restore only the one (single item) you want'.
    - Current: `사용자가 원하는 하나만 복원`
    - Source: `Restore only the ones you want`
    - Suggest: `원하는 항목만 복원`
    - The en-US means the user picks any number of windows/tabs. 하나만 means 'only one', which wrongly limits restoring to a single item.
- `smart-window-model-custom-save-confirmation` — `browser/browser/aiFeatures.ftl` — An instruction to the user ('Start a new chat to test') became a claim that the product will start a new chat itself.
    - Current: `테스트를 위해 채팅을 새로 시작합니다.`
    - Source: `Model details saved. Start a new chat to test.`
    - Suggest: `테스트하려면 새 채팅을 시작하세요.`
    - en-US: 'Model details saved. Start a new chat to test.' The Korean says '(We) will start a new chat for testing', which describes an automatic action that doesn't happen.
- `aiwindow-feedback-disclaimer` — `browser/browser/aiWindow.ftl` — The Korean drops the fact that submitting sends your feedback and this chat to Mozilla. It only says the submission helps improve Smart Window.
    - Current: `의견 공유를 제출하면 { -brand-shorter-name }가 { -smart-window-brand-name }를 개선하는 데 도움이 됩니다.`
    - Source: `Submitting shares your feedback and this chat to help { -brand-shorter-name } improve { -smart-window-brand-name }. Your other chats stay private. <a data-l10n-name="learn-more">Learn more</a>`
    - Suggest: `제출하면 의견과 이 채팅이 공유되어 { -brand-shorter-name }가 { -smart-window-brand-name }를 개선하는 데 도움이 됩니다.`
    - The en-US says 'Submitting shares your feedback and this chat'. The Korean never says the current chat is sent. All that remains is 'other chats stay private', so the user cannot tell that this conversation leaves the device.
- `smart-window-default-promo-heading` — `browser/browser/aiWindow.ftl` — 'Make Smart Window your default?' became 'Set Smart Window as your default browser?'
    - Current: `기본 브라우저로 설정하시겠습니까?`
    - Source: `Make { -smart-window-brand-name } your default?`
    - Suggest: `기본으로 설정하시겠습니까?`
    - Smart Window is a window mode inside Firefox, not a browser. The message below it says Firefox will open in Smart Window, so 'default browser' misstates what the setting does.
- `extension-nova-lagoon-name` — `browser/browser/appExtensionFields.ftl` — 'Lagoon' is translated as 산호초 (coral reef).
    - Current: `산호초`
    - Source: `Lagoon`
    - Suggest: `석호`
    - The comment says the name refers to a sheltered body of water evoking medium blue. A coral reef is neither a body of water nor a blue-evoking image.
- `appmenu-remote-tabs-noclients` — `browser/browser/appmenu.ftl` — The direction is reversed: it asks about using this device's tabs on other devices, not seeing other devices' tabs here.
    - Current: `다른 기기에서도 여기에서 열린 탭을 사용하시겠습니까?`
    - Source: `Want to see your tabs from other devices here?`
    - Suggest: `다른 기기의 탭을 여기에서 보시겠습니까?`
    - en-US: 'Want to see your tabs from other devices here?' The Korean means 'Do you want to use the tabs open here on other devices too?'
- `full-screen-autohide` — `browser/browser/browser.ftl` — 'Hide Toolbars' is translated as 'Close toolbars'.
    - Current: `도구 모음 닫기`
    - Source: `accesskey: H label: Hide Toolbars`
    - Suggest: `도구 모음 숨기기`
    - The item auto-hides toolbars in full screen. Elsewhere the locale uses 숨기기 for 'hide' (featureCallout.ftl uses 도구 모음 숨기기).
- `main-context-menu-media-pause` — `browser/browser/browserContext.ftl` — 'Pause' is translated as 'Stop' (중지).
    - Current: `중지`
    - Source: `accesskey: P label: Pause`
    - Suggest: `일시 정지`
    - The media context menu item pauses playback. 중지 means stop, and the same word is used for the browser's Stop command. The tree uses 일시 정지 for pause (pictureinpicture.ftl).
- `actions-callout-subtitle` — `browser/browser/featureCallout.ftl` — The user is told to press (눌러) 'clear' instead of typing it in the address bar.
    - Current: `"지우기"를 눌러 기록을 지우세요`
    - Source: `Try typing an action like “print” to print a page, or “clear” to clear your history.`
    - Suggest: `"지우기"를 입력하여 기록을 지우세요`
    - The comment explains that the user types the keyword to make the action button appear. 'Press' gives a wrong instruction.
- `ip-protection-bandwidth-warning-infobar-message-75` — `browser/browser/ipProtection.ftl` — 'Getting close to your VPN limit' became 'You have reached your VPN limit'.
    - Current: `VPN 사용 한도에 도달했습니다.`
    - Source: `<strong>Getting close to your VPN limit.</strong> You have { $usageLeft } GB left. Your data will reset at the start of next month.`
    - Suggest: `VPN 사용 한도에 가까워지고 있습니다.`
    - This is the 75% warning, and the same message goes on to say GB remain. Saying the limit is already reached is wrong and contradicts the rest of the message.
- `ip-protection-description` — `browser/browser/ipProtection.ftl` — 'While browsing' is rendered as 'while searching' (검색하는 동안).
    - Current: `검색하는 동안`
    - Source: `description: Built-in VPN to enhance your privacy while browsing on { -brand-short-name }. label: VPN`
    - Suggest: `탐색하는 동안`
    - The locale consistently uses 탐색 for browsing and 검색 for search. The VPN protects all browsing, not just searches.
- `migration-imported-safari-reading-list` — `browser/browser/migrationWizard.ftl` — "Reading List" is translated as "subscription list" (구독 목록).
    - Current: `구독 목록 (Safari로부터)`
    - Source: `Reading List (From Safari)`
    - Suggest: `읽기 목록 (Safari로부터)`
    - Safari's Reading List feature is 읽기 목록 in Korean. 구독 means subscription, which names a different thing. The same error appears in migration-imported-edge-reading-list.
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — The macOS variant copies the other variant's 'faster browsing and automatic privacy protection' text instead of translating 'Make it your default and keep it in your Dock'.
    - Current: `[macos] 더 빠른 탐색과 자동으로 개인 정보를 보호해주는 기능을 이용하세요.`
    - Source: `{$sel_1 ->} [macos] Make it your default and keep it in your Dock. [other] Get faster browsing and automatic privacy protection.`
    - Suggest: `[macos] 기본 브라우저로 설정하고 독에 넣으세요.`
    - en-US macOS variant: 'Make it your default and keep it in your Dock.' The Korean macOS variant says something unrelated.
- `set-default-menu-message-split-layout-title` — `browser/browser/newtab/asrouter.ftl` — The macOS variant copies the 'Open all links with Firefox' text from the other variant instead of translating 'Keep Firefox at your fingertips'.
    - Current: `[macos] { -brand-short-name }로 모든 링크 열기`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } at your fingertips [other] Open all links with { -brand-short-name }`
    - Suggest: `[macos] { -brand-short-name }를 손쉽게 사용하세요`
    - en-US macOS variant: 'Keep { -brand-short-name } at your fingertips'. The Korean macOS variant says something different.
- `newtab-privacy-message-milestone-year` — `browser/browser/newtab/newtab.ftl` — 'That's a powerful year of protecting your privacy' became 'This is the year you must protect your privacy'.
    - Current: `개인 정보를 보호해야 하는 올해입니다.`
    - Source: `{$count ->} [one] { $count } tracker blocked this year. That’s a powerful year of protecting your privacy. [other] { $count } trackers blocked this year. That’s a powerful year of protecting your privacy.`
    - Suggest: `개인 정보를 든든하게 지켜 온 한 해입니다.`
    - The source celebrates a year of protection already done. The Korean turns it into an obligation ('must protect') and reads ungrammatically.
- `newtab-privacy-message-promo-relay-1` — `browser/browser/newtab/newtab.ftl` — Meaning reversed: 'Save your real email for people you trust' became 'don't save your real email address for people you trust'.
    - Current: `신뢰할 수 있는 사람들을 위해 실제 이메일 주소는 저장하지 마세요.`
    - Source: `Save your real email for people you trust; use an email mask for sign-ups.`
    - Suggest: `실제 이메일 주소는 신뢰하는 사람들을 위해 남겨 두세요.`
    - Here 'save' means 'keep in reserve': give your real address only to trusted people and use a mask for sign-ups. The Korean adds a prohibition the source does not have, so the advice is the opposite.
- `newtab-wallpaper-remove-image-numbered` — `browser/browser/newtab/newtab.ftl` — 'Remove image N' is rendered as 'Remove N images'.
    - Current: `이미지 { $number }개 제거`
    - Source: `aria-label: Remove image { $number } title: Remove image { $number }`
    - Suggest: `이미지 { $number } 제거`
    - $number is the image's position, not a quantity. With the counter 개 the button seems to remove several images.
- `newtab-wallpaper-your-images-item-numbered` — `browser/browser/newtab/newtab.ftl` — An image's position number is rendered as a count ('N images').
    - Current: `이미지 { $number }개`
    - Source: `Image { $number }`
    - Suggest: `이미지 { $number }`
    - The comment says $number is 'which saved image this is, counting from one'. That is an index, so the counter 개 makes screen readers say 'three images' instead of 'image 3'.
- `policy-DisabledCiphers` — `browser/browser/policies/policies-descriptions.ftl` — 'Disable ciphers' is translated as 'disable encryption'.
    - Current: `암호화를 사용 안 합니다.`
    - Source: `Disable ciphers.`
    - Suggest: `암호 알고리즘(cipher)을 사용 안 합니다.`
    - The policy turns off specific TLS cipher suites. It does not turn off encryption. 암호화 means encryption, which misleads admins about what the policy does.
- `appearance-browser-icon-pride` — `browser/browser/preferences/browserIcon.ftl` — The icon name 'Pride' (the LGBTQ+ Pride theme) is translated literally as 자부심, meaning personal self-esteem or pride in oneself.
    - Current: `자부심`
    - Source: `label: Pride`
    - Suggest: `프라이드`
    - Among the icon names, 'Pride' refers to the Pride theme. Korean usually writes this as 프라이드 (as in 프라이드 퍼레이드 or 퀴어 프라이드). 자부심 means personal pride, which is the wrong sense of the word.
- `autofill-address-department` — `browser/browser/preferences/formAutofill.ftl` — 'Department' (an administrative region in Colombia and Nicaragua) is translated as 부서, which means an organizational department or office.
    - Current: `부서`
    - Source: `Department`
    - Suggest: `주`
    - The comment says the field is primary address information one level below the country. 부서 means a section of a company or organization, which is the wrong sense for an address field. The other first-level regions in this file use administrative-region words (주, 현, 도/시).
- `containers-disable-alert-cancel-button` — `browser/browser/preferences/preferences.ftl` — 'Keep enabled' is translated as 'Enable'. That suggests an action rather than keeping the current state, and 활성화 하기 also has a spacing error.
    - Current: `활성화 하기`
    - Source: `Keep enabled`
    - Suggest: `활성화 유지`
    - This is the cancel button of a dialog asking whether to disable Container Tabs. The en-US means 'leave it on'. 활성화 하기 reads as 'turn on', which is confusing when the feature is already on. Standard spacing for the verb would also be 활성화하기.
- `content-blocking-etp-standard-tcp-rollout-description` — `browser/browser/preferences/preferences.ftl` — 'contains cookies to the site you're on' is translated as 'includes cookies for the site you're on'. The developer comment says 'contains' means 'isolates' or 'limits'.
    - Current: `사용자가 있는 사이트에 대한 쿠키가 포함되어 있으므로`
    - Source: `Total Cookie Protection contains cookies to the site you’re on, so trackers can’t use them to follow you between sites.`
    - Suggest: `쿠키를 현재 방문 중인 사이트로 제한하므로`
    - The comment says 'Contains' here means 'isolates', 'limits'. The Korean uses 포함 ('includes'), so Total Cookie Protection is described as including cookies. That does not explain why trackers can't use the cookies across sites, and it hides what the feature actually does, which is isolate them.
- `search-keyword-warning-title` — `browser/browser/preferences/preferences.ftl` — 'Duplicate Keyword' is translated as 'Copy Keyword'. The developer comment says 'Duplicate' is an adjective here.
    - Current: `키워드 복사`
    - Source: `Duplicate Keyword`
    - Suggest: `중복된 키워드`
    - This is the title of the warning shown when the chosen keyword is already in use. '복사' means the action of copying, so the title reads like a command to copy the keyword instead of a notice that it is a duplicate. The comment ('Duplicate' is an adjective) rules out the verb reading.
- `update-in-progress-message` — `browser/browser/preferences/preferences.ftl` — The question asks whether Firefox wants to continue the update, not whether the user wants Firefox to continue.
    - Current: `{ -brand-short-name }가 이 업데이트를 계속하길 원하십니까?`
    - Source: `Do you want { -brand-short-name } to continue with this update?`
    - Suggest: `{ -brand-short-name } 업데이트를 계속하시겠습니까?`
    - The en-US is 'Do you want Firefox to continue with this update?'. Here 가 makes the brand the subject of 원하십니까 ('want'), so the Korean literally asks 'Does Firefox want to continue this update?'. The person being asked has become Firefox instead of the user.
- `custom-avatar-alt` — `browser/browser/profiles.ftl` — The alt text "Custom avatar" is translated as the action "customize avatar".
    - Current: `아바타 사용자 지정`
    - Source: `alt: Custom avatar`
    - Suggest: `사용자 지정 아바타`
    - This is alt text describing an image, not an action. The matching tooltip custom-avatar already correctly uses 사용자 지정 아바타.
- `default-profile-name` — `browser/browser/profiles.ftl` — The default profile name "Profile { $number }" (Profile 1, Profile 2…) is translated as a count: "{ $number } profiles".
    - Current: `프로필 { $number }개`
    - Source: `Profile { $number }`
    - Suggest: `프로필 { $number }`
    - The comment says $number is the number of the profile, used as an ordinal-style name. The counter 개 makes it read "3 profiles" instead of "Profile 3".
- `delete-profile-autofill` — `browser/browser/profiles.ftl` — "Autofill data" is reversed into "data autofill" (데이터 자동 채우기), which reads as an action rather than a kind of data.
    - Current: `데이터 자동 채우기 (주소, 결제 수단)`
    - Source: `Autofill data (addresses, payment methods)`
    - Suggest: `자동 채우기 데이터 (주소, 결제 수단)`
    - The row lists data that will be deleted. The locale elsewhere uses 자동 채우기 데이터 (migrationWizard.ftl).
- `delete-profile-tabs` — `browser/browser/profiles.ftl` — "Open tabs" is translated as the command "open tabs". The comment says "Open" is an adjective.
    - Current: `탭 열기`
    - Source: `Open tabs`
    - Suggest: `열린 탭`
    - The comment reads: "Open is an adjective, as in 'browser tabs currently open'". The locale uses 열린 탭 for this meaning elsewhere (sidebar.ftl).
- `delete-profile-windows` — `browser/browser/profiles.ftl` — "Open windows" is translated as the command "open windows". The comment says "Open" is an adjective (windows currently open).
    - Current: `창 열기`
    - Source: `Open windows`
    - Suggest: `열린 창`
    - The comment reads: "Open is an adjective, as in 'browser windows currently open'". This row lists data that will be deleted. 창 열기 is an action label. The same file's sidebar strings use 열린 탭 for this meaning.
- `cryptominer-tab-content` — `browser/browser/protections.ftl` — "Cryptomining scripts" is translated as "decryption scripts" (암호 해독 스크립트).
    - Current: `암호 해독 스크립트는`
    - Source: `Cryptominers use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill. <a data-l10n-name="learn-more-link">Learn more</…`
    - Suggest: `암호화폐 채굴 스크립트는`
    - 암호 해독 means decryption or code-breaking, not cryptocurrency mining. The same paragraph correctly uses 암호화폐 채굴기 for cryptominers.
- `protections-panel-cryptominers` — `browser/browser/protectionsPanel.ftl` — "Cryptomining scripts" is translated as "decryption scripts" (암호 해독 스크립트).
    - Current: `암호 해독 스크립트는`
    - Source: `Cryptominers use your system’s computing power to mine digital money. Cryptomining scripts drain your battery, slow down your computer, and can increase your energy bill.`
    - Suggest: `암호화폐 채굴 스크립트는`
    - Same error as cryptominer-tab-content: 암호 해독 means decryption, not cryptocurrency mining.
- `recently-closed-window-panel-tooltip` — `browser/browser/recentlyClosed.ftl` — `recently-closed-window-panel-tooltip` has plural variant ['one'], which ko does not have
    - Current: `{$tabCount ->} [0] { $winTitle } [one] { $winTitle } (탭 { $tabCount }개, { $closedAt }에 닫음) [other] { $winTitle } ({ $tabCount } tabs, closed at { $closedAt })`
    - Source: `{$tabCount ->} [0] { $winTitle } [one] { $winTitle } ({ $tabCount } tab, closed at { $closedAt }) [other] { $winTitle } ({ $tabCount } tabs, closed at { $closedAt })`
    - ko has the categories ['other']. A variant whose category the language never produces is never selected, so the text written there never appears. Nothing is broken -- the catch-all is shown -- but the variant is dead.
- `sync-setup-verify-heading` — `browser/browser/sync.ftl` — "Sign in to sync" is translated as "sign up for Sync" (가입).
    - Current: `Sync에 가입하시겠습니까?`
    - Source: `Are you sure you want to sign in to sync?`
    - Suggest: `Sync에 로그인하시겠습니까?`
    - en-US: "Are you sure you want to sign in to sync?". The dialog is a merge warning for an existing account being signed in. The description says 로그인하면. 가입 means registering a new account.
- `webrtc-reason-for-no-permanent-allow-audio` — `browser/browser/webrtcIndicator.ftl` — The meaning is reversed. The English says Firefox cannot grant permanent tab-audio access without asking which tab to share. The Korean says Firefox will now access tab audio without asking which tab to share.
    - Current: `{ -brand-short-name }가 이제 어느 탭을 공유할지 더 이상 묻지 않고 탭의 소리에 접근합니다.`
    - Source: `{ -brand-short-name } can not allow permanent access to your tab’s audio without asking which tab to share.`
    - Suggest: `{ -brand-short-name }는 공유할 탭을 묻지 않고 탭 소리에 대한 영구적인 접근을 허용할 수 없습니다.`
    - en-US: "can not allow permanent access to your tab’s audio without asking which tab to share". The Korean turns a refusal (a safeguard) into a statement that the browser reads tab audio without asking. A user would believe Firefox captures audio without consent.
- `webrtc-reason-for-no-permanent-allow-screen` — `browser/browser/webrtcIndicator.ftl` — The Korean says Firefox can no longer access your screen. The English says Firefox cannot allow permanent access to your screen.
    - Current: `{ -brand-short-name }가 더 이상 당신의 화면에 접근할 수 없습니다.`
    - Source: `{ -brand-short-name } can not allow permanent access to your screen.`
    - Suggest: `{ -brand-short-name }는 화면에 대한 영구적인 접근을 허용할 수 없습니다.`
    - en-US: "can not allow permanent access to your screen". This explains why the 'remember' option is missing. The Korean drops the 'permanent' part and states something different.
- `confirmRepostPrompt` — `browser/chrome/overrides/appstrings.properties` — The first sentence is garbled: it says %S 'needs information it previously performed' instead of saying %S must resend information.
    - Current: `%S가 이전에 수행했던 정보가 필요합니다.`
    - Source: `To display this page, %S must send information that will repeat any action (such as a search or order confirmation) that was performed earlier.`
    - Suggest: `%S가 정보를 다시 보내야 하며, 이로 인해 이전에 수행했던 작업(검색 또는 주문 확인 등)이 반복됩니다.`
    - en-US: '%S must send information that will repeat any action...'. The Korean drops 'send' and joins 정보 (information) with 수행했던 (performed), which does not make sense. The next sentence then says the action is repeated, but never explains that resending the data is what causes it.
- `REG_APP_DESC` — `browser/installer/custom.properties` — 'Protection from online identity theft' became 'defense against online-specific attacks'.
    - Current: `온라인 고유의 공격으로부터의 방어`
    - Source: `$BrandShortName delivers safe, easy web browsing. A familiar user interface, enhanced security features including protection from online identity theft, and integrated search let you get the most out of the web.`
    - Suggest: `온라인 신원 도용으로부터의 보호`
    - The source names one specific threat, identity theft. The Korean names a vague, different one ('attacks unique to online').
- `WARN_RESTART_REQUIRED_UNINSTALL` — `browser/installer/custom.properties` — 'previous' is dropped, so the restart seems to be for the current uninstall rather than an earlier unfinished one.
    - Current: `$BrandShortName 제거를 완료하려면`
    - Source: `Your computer must be restarted to complete a previous uninstall of $BrandShortName. Do you want to reboot now?`
    - Suggest: `이전에 진행한 $BrandShortName 제거를 완료하려면`
    - en-US: 'to complete a previous uninstall of $BrandShortName'. The message appears because an earlier operation is still pending. Without 'previous' that context is lost.
- `WARN_RESTART_REQUIRED_UPGRADE` — `browser/installer/custom.properties` — 'previous' is dropped, so the restart seems to be for the current upgrade rather than an earlier unfinished one.
    - Current: `$BrandShortName 업그레이드를 완료하려면`
    - Source: `Your computer must be restarted to complete a previous upgrade of $BrandShortName. Do you want to reboot now?`
    - Suggest: `이전에 진행한 $BrandShortName 업그레이드를 완료하려면`
    - en-US: 'to complete a previous upgrade of $BrandShortName'. The context that an earlier operation is pending is lost.
- `MUI_UNTEXT_WELCOME_INFO_TEXT` — `browser/installer/mui.properties` — Negation dropped: the uninstaller tells the user to check that the browser IS running, when it should say to make sure it is NOT running.
    - Current: `$BrandFullNameDA가 실행되고 있는지 먼저 확인하세요`
    - Source: `This wizard will guide you through the uninstallation of $BrandFullNameDA.  Before starting the uninstallation, make sure $BrandFullNameDA is not running.  $_CLICK`
    - Suggest: `$BrandFullNameDA가 실행 중이 아닌지 먼저 확인하세요`
    - en-US: 'make sure $BrandFullNameDA is not running'. The Korean drops 'not', so the instruction is the opposite of what is needed before uninstalling.
- `pauseOnCaughtExceptionsItem` — `devtools/client/debugger.properties` — 'Pause on caught exceptions' loses 'caught' and reads as 'pause when an exception occurs'
    - Current: `예외 발생시 일시중지`
    - Source: `Pause on caught exceptions`
    - Suggest: `잡힌 예외에서 일시 중지`
    - This is a separate option from pauseOnExceptionsItem2 ('예외에서 일시중지'). Without 'caught', both checkboxes say practically the same thing, and users can't tell what the second one does.
- `variablesViewOptimizedOut` — `devtools/client/debugger.properties` — '(optimized away)' is rendered as 'cannot optimize'
    - Current: `(최적화할 수 없음)`
    - Source: `(optimized away)`
    - Suggest: `(최적화로 제거됨)`
    - en-US '(optimized away)' means the engine optimized the variable out, so its value is gone. The Korean says the variable cannot be optimized, which is a different fact.
- `layout.displayLineNumbers` — `devtools/client/layout.properties` — 'Display line numbers' is rendered as 'display the number of lines'
    - Current: `줄 수 표시`
    - Source: `Display line numbers`
    - Suggest: `줄 번호 표시`
    - The grid option shows the line numbers of grid lines. 줄 수 means a count of lines, which is a different thing.
- `individuals.state.error.full` — `devtools/client/memory.properties` — 'fetching individuals' is rendered as 'applying each'
    - Current: `이 그룹 안의 각각을 적용하는 데 오류가 발생함`
    - Source: `There was an error while fetching individuals in the group`
    - Suggest: `그룹 안의 개별 항목을 가져오는 중에 오류가 발생함`
    - en-US: 'There was an error while fetching individuals in the group'. 적용하다 means 'apply', not 'fetch'.
- `certmgr.certificateTransparency.status.notDiverseSCTS` — `devtools/client/netmonitor.properties` — 'Not diverse SCTs' is rendered as 'SCTs not delivered'
    - Current: `SCT 배달 안 됨`
    - Source: `Not diverse SCTs`
    - Suggest: `SCT 다양성 부족`
    - The comment says there are not enough diverse signed certificate timestamps. 배달 안 됨 ('not delivered') describes a different failure.
- `netmonitor.security.state.secure-custom-root` — `devtools/client/netmonitor.properties` — 'verified by a certificate issuer' is rendered as 'connected by a certificate issuer'
    - Current: `Mozilla에서 인식하지 못하는 인증서 발급자가 연결했습니다.`
    - Source: `The connection used to fetch this resource was verified by a certificate issuer that is not recognized by Mozilla.`
    - Suggest: `Mozilla에서 인식하지 못하는 인증서 발급자에 의해 확인되었습니다.`
    - en-US: 'The connection used to fetch this resource was verified by a certificate issuer that is not recognized by Mozilla.' The Korean says the issuer made the connection, which garbles the meaning.
- `perftools-thread-timer` — `devtools/client/perftools.ftl` — 'The thread handling timers' is rendered as 'thread-handling timers'
    - Current: `스레드 처리 타이머`
    - Source: `title: The thread handling timers (setTimeout, setInterval, nsITimer)`
    - Suggest: `타이머를 처리하는 스레드`
    - The source describes a thread that handles timers. The Korean noun phrase describes timers that handle threads, which reverses the relationship.
- `options-inspector-rules-focus-next-on-enter-tooltip` — `devtools/client/toolbox-options.ftl` — Garbled: the property name or value is made the thing that moves focus
    - Current: `선택기를 편집할 때 Enter 키를 누르면 속성 이름이나 값이 다음 입력으로 포커스를 이동합니다.`
    - Source: `title: When enabled, hitting the Enter key when editing a selector, a property name or value will move the focus to the next input.`
    - Suggest: `선택자, 속성 이름 또는 값을 편집할 때 Enter 키를 누르면 다음 입력으로 포커스가 이동합니다.`
    - en-US: 'hitting the Enter key when editing a selector, a property name or value will move the focus to the next input'. The Korean drops the list of three editable fields and makes 'property name or value' the subject. It also uses 선택기 where the rest of the Inspector uses 선택자.
- `inactive-css-resize` — `devtools/client/tooltips.ftl` — The CSS value 'visible' is translated as '표시', so the tooltip reads 'an overflow value other than display'
    - Current: `표시 이외의 오버플로 값이 있는 요소`
    - Source: `<strong>{ $property }</strong> has no effect on this element since it can only be applied to elements with an overflow value other than visible, and to certain replaced elements, such as textareas.`
    - Suggest: `overflow 값이 visible 이외인 요소`
    - en-US: 'elements with an overflow value other than visible'. Here 'visible' is the CSS keyword. The matching -fix string correctly keeps <strong>visible</strong> in English, so the two strings contradict each other.
- `rule.bezierSwatch.tooltip` — `devtools/shared/styleinspector.properties` — 'timing-function editor' is rendered as 'timing feature editor'
    - Current: `타이밍 기능 편집기`
    - Source: `Click to open the timing-function editor`
    - Suggest: `타이밍 함수 편집기`
    - 'timing-function' is the CSS timing function (cubic-bezier). 기능 means feature, not function. The animation inspector correctly uses '타이밍 함수'.
- `togglebutton` — `dom/chrome/accessibility/AccessFu.properties` — 'toggle button' rendered as 'conversion button'
    - Current: `변환 버튼`
    - Source: `toggle button`
    - Suggest: `토글 버튼`
    - 변환 means convert/transform. A toggle button switches between two states.
- `searchTextField` — `dom/chrome/accessibility/mac/accessible.properties` — Role 'search text field' rendered as the action 'search the text field'
    - Current: `텍스트 필드 검색`
    - Source: `search text field`
    - Suggest: `검색 텍스트 필드`
    - This is a role description for input type=search, not an action.
- `FormValidationNumberRangeUnderflow` — `dom/chrome/dom/dom.properties` — 'no less than' rendered as 'greater than', which excludes the minimum
    - Current: `%S보다 큰 값을 선택하세요.`
    - Source: `Please select a value that is no less than %S.`
    - Suggest: `%S 이상의 값을 선택하세요.`
    - en-US allows a value equal to %S. The Korean tells users that the minimum itself is invalid.
- `ImportMapNotAllowedMultiple` — `dom/chrome/dom/dom.properties` — 'import maps' rendered as 'map imports'; inconsistent with '가져오기 맵' used elsewhere
    - Current: `여러 개의 맵 가져오기는 허용되지 않습니다.`
    - Source: `Multiple import maps are not allowed.`
    - Suggest: `여러 개의 가져오기 맵은 허용되지 않습니다.`
    - The rest of the file translates Import Map as '가져오기 맵'. The same inversion is in ImportMapNotAllowedAfterModuleLoad.
- `ManifestInvalidType` — `dom/chrome/dom/dom.properties` — Mistranslated: 'member is needed to become %3$S'
    - Current: `%3$S가 되기 위해서는 %1$S의 %2$S 멤버가 필요합니다.`
    - Source: `Expected the %1$S’s %2$S member to be a %3$S.`
    - Suggest: `%1$S의 %2$S 멤버는 %3$S여야 합니다.`
    - en-US: 'Expected the manifest’s start_url member to be a string.'
- `PointerLockDeniedHidden` — `dom/chrome/dom/dom.properties` — 'not visible' rendered as 'not valid'
    - Current: `문서가 유효하지 않아서`
    - Source: `Request for pointer lock was denied because the document is not visible.`
    - Suggest: `문서가 보이지 않아서`
    - en-US: 'because the document is not visible.'
- `PointerLockDeniedMovedDocument` — `dom/chrome/dom/dom.properties` — Says the element moved the document, instead of the element moving to another document
    - Current: `요청한 요소가 문서를 이동시켜서`
    - Source: `Request for pointer lock was denied because the requesting element has moved document.`
    - Suggest: `요청한 요소가 다른 문서로 이동해서`
    - en-US: 'the requesting element has moved document.'
- _…and 107 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `newtab-widget-wrexhamafc-view-matches` — `browser/browser/newtab/newtab.ftl` — "Matches" (football games) is translated as "일치" (agreement/correspondence).
    - Current: `일치`
    - Source: `Matches`
    - Suggest: `경기`
    - In the Wrexham AFC widget, "Matches" is a view that lists games, next to Table and Fixtures. "일치" means things matching or corresponding, which is the wrong sense of the word here.
- `tab-context-close-duplicate-tabs-alt` — `browser/browser/tabContextMenu.ftl` — "Duplicate Tabs" (tabs that are duplicates, to be closed) is rendered as "탭 복제", meaning the action of duplicating a tab.
    - Current: `탭 복제`
    - Source: `accesskey: x label: Duplicate Tabs`
    - Suggest: `중복 탭`
    - The developer comment says this item sits under "Close Multiple" and closes the duplicate tabs of the selected tab. "탭 복제" reads as the command to duplicate a tab, which is a different action.
- `DocumentReleaseCaptureWarning` — `dom/chrome/dom/dom.properties` — The do-not-translate identifier "Element.releasePointerCapture()" has lost its "Element." prefix.
    - Current: `대신 releasePointerCapture()를 사용하세요`
    - Source: `Document.releaseCapture() is deprecated. Use Element.releasePointerCapture() instead. For more help https://developer.mozilla.org/docs/Web/API/Element/releasePointerCapture`
    - Suggest: `대신 Element.releasePointerCapture()를 사용하세요`
    - The developer comment says to keep "Element.releasePointerCapture()" exactly as written. The source names Element.releasePointerCapture(), and leaving out the interface name changes the API reference the developer is pointed to.
- `GamepadHapticActuatorsWarning` — `dom/chrome/dom/dom.properties` — The do-not-translate identifier Gamepad.hapticActuators is misspelled as Gamepad.haptricActuator.
    - Current: `Gamepad.haptricActuator는`
    - Source: `Gamepad.hapticActuators is non-standard and deprecated.`
    - Suggest: `Gamepad.hapticActuators는`
    - The comment says not to translate "Gamepad.hapticActuators". The target adds an 'r' and drops the final 's', so it names an API that doesn't exist.
- `ConnectionAllowlistReportOnlyRedirectBlocked` — `dom/chrome/security/security.properties` — The conditional "would block" of a report-only policy is translated as a plain statement that the redirect is blocked.
    - Current: `페이지 설정에서 %1$S의 리디렉션을 차단합니다.`
    - Source: `Connection-Allowlist: (Report-Only policy) The page’s settings would block a redirect of %1$S.`
    - Suggest: `페이지 설정에서 %1$S의 리디렉션을 차단했을 것입니다.`
    - Under a Report-Only policy nothing is actually blocked. The source says the settings 'would block' the redirect. The Korean says they block it, which misleads developers reading the console.
- `-mdn-brand-name` — `toolkit/toolkit/branding/brandings.ftl` — The brand 'MDN Web Docs' is partly translated as 'MDN 웹 문서'.
    - Current: `MDN 웹 문서`
    - Source: `MDN Web Docs`
    - Suggest: `MDN Web Docs`
    - The section header says these feature names must be treated as brands and cannot be translated or transliterated.
- `btp-warning-tracker-classified` — `toolkit/toolkit/global/antiTracking.ftl` — 'bounce tracker' is translated even though the comment says not to.
    - Current: `바운스 추적기로 분류되었습니다`
    - Source: `{$gracePeriodSeconds ->} [other] “{ $siteHost }” has been classified as a bounce tracker. If it does not receive user activation within the next { $gracePeriodSeconds } seconds it will have its state purged.`
    - Suggest: `bounce tracker로 분류되었습니다`
    - Developer comment: 'Do not translate "bounce tracker".'
- `btp-warning-tracker-purged` — `toolkit/toolkit/global/antiTracking.ftl` — 'bounce tracker' is translated even though the comment says not to.
    - Current: `바운스 추적기로 감지되어`
    - Source: `The state of “{ $siteHost }” was recently purged because it was detected as a bounce tracker.`
    - Suggest: `bounce tracker로 감지되어`
    - Developer comment: 'Do not translate "bounce tracker".'

### C. Grammar, agreement & spelling

- `addon-local-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — Spelling error: 다므르로 should be 다르므로.
    - Current: `다므르로`
    - Source: `This add-on could not be installed because it does not match the add-on { -brand-short-name } expected.`
    - Suggest: `다르므로`
    - Typo in the connective form of 다르다 ('to differ').
- `action-log-read-page` — `browser/browser/aiWindowContent.ftl` — A completed action is rendered as a nominal/imperative form ('read page content') instead of past tense.
    - Current: `페이지 내용 읽기`
    - Source: `Read page content`
    - Suggest: `페이지 내용 읽음`
    - The comment says 'Read is past tense, to indicate that the action has been completed'. Sibling strings use completed forms (검색됨, 확인됨).
- `genai-prompt-prefix-selection` — `browser/browser/genai.ftl` — Grammar error: the location particle 에서 is used with 있다 where it should be 에.
    - Current: `페이지에서 있습니다`
    - Source: `I’m on page “{ $tabTitle }” with “{ $selection }” selected.`
    - Suggest: `페이지에 있습니다`
    - 'I'm on page X' takes 에 with 있다. '에서 있습니다' is ungrammatical, and this text is sent to the chatbot as the prompt.
- `fox-doodle-pin-body` — `browser/browser/newtab/asrouter.ftl` — Grammar error: 있는다는 should be 있다는.
    - Current: `사용할 수 있는다는`
    - Source: `Here’s a quick reminder that you can keep your favorite indie browser just one click away.`
    - Suggest: `사용할 수 있다는`
    - The quotative form of the adjective 있다 is 있다는. 있는다는 is ungrammatical.
- `windows-10-eos-sync-callout-privacy-info-button` — `browser/browser/newtab/asrouter.ftl` — Word-spacing errors: 차단 된 should be one word, and 내용보기 should be two.
    - Current: `차단 된 내용보기`
    - Source: `See what’s blocked`
    - Suggest: `차단된 내용 보기`
    - Under standard Korean spacing rules, the suffix -되다 attaches to the noun (차단된), and 보기 is a separate word.
- `newtab-privacy-message-info-5` — `browser/browser/newtab/newtab.ftl` — Word-spacing error: 줄어 든다는 should be one word.
    - Current: `줄어 든다는`
    - Source: `Blocked trackers means fewer companies can follow you across sites.`
    - Suggest: `줄어든다는`
    - 줄어들다 is a single verb and is written without a space.
- `newtab-sports-widget-team-name-label-bih` — `browser/browser/newtab/newtab.ftl` — Country name misspelled: Herzegovina is written 헤르체코비나 instead of 헤르체고비나.
    - Current: `보스니아 헤르체코비나`
    - Source: `label: Bosnia and Herzegovina`
    - Suggest: `보스니아 헤르체고비나`
    - The standard Korean name is 보스니아 헤르체고비나.
- `newtab-sports-widget-team-name-label-civ` — `browser/browser/newtab/newtab.ftl` — Country name misspelled: Côte d'Ivoire is written 코트디브아르 instead of 코트디부아르.
    - Current: `코트디브아르`
    - Source: `label: Ivory Coast`
    - Suggest: `코트디부아르`
    - The standard Korean name is 코트디부아르.
- `newtab-stocks-ticker-status-down` — `browser/browser/newtab/newtab.ftl` — Wrong word for a falling stock price: 하강 (physical descent) is used instead of 하락.
    - Current: `당일 { $change } 하강`
    - Source: `{ $name }, down { $change }, { $price }`
    - Suggest: `당일 { $change } 하락`
    - In Korean, a falling price is 하락, the counterpart of 상승. 하강 means physical descent and is not used for prices.
- `hnt-card-extensions-body` — `browser/browser/newtab/onboarding.ftl` — "인기있는" is missing the required space; standard spelling is "인기 있는".
    - Current: `가장 인기있는`
    - Source: `Customize your browsing with our most loved extensions.`
    - Suggest: `가장 인기 있는`
    - Under Korean spacing rules, "인기 있다" is written as two words.
- `tab-groups-onboarding-session-restore-title-2` — `browser/browser/newtab/onboarding.ftl` — Word-spacing error: 다시열 should be two words.
    - Current: `다시열 수`
    - Source: `Reopen your tab groups from the List All Tabs menu anytime.`
    - Suggest: `다시 열 수`
    - 다시 is an adverb and is separated from 열. The sibling strings in the same file correctly write 다시 열 수.
- `set-as-my-default-browser-2` — `browser/browser/preferences/preferences.ftl` — The button label 'Make default' is translated as an incomplete fragment with no verb ('as default browser').
    - Current: `기본 브라우저로`
    - Source: `accesskey: D label: Make default`
    - Suggest: `기본 브라우저로 설정`
    - 기본 브라우저로 ends in the particle 로 and has no verb, so the button does not say what it does. Elsewhere in this partition the same action is written 기본으로 설정 (browserIcon.ftl).
- `safeb-blocked-phishing-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — Spelling error: 들어날 should be 드러날 (from 드러나다, 'to be revealed').
    - Current: `개인 정보가 들어날 수 있는`
    - Source: `{ -brand-short-name } blocked this page because it may trick you into doing something dangerous like installing software or revealing personal information like passwords or credit cards.`
    - Suggest: `개인 정보가 드러날 수 있는`
    - The standard spelling of 'to be revealed/exposed' is 드러나다. 들어나다 is a common misspelling.
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — "Beta" is translated even though the developer comment says it must not be.
    - Current: `사용해 보세요 - 베타`
    - Source: `tooltiptext: Try private translations in { -brand-shorter-name } - Beta`
    - Suggest: `사용해 보세요 - Beta`
    - The comment says "Beta" should not be translated because it mirrors the un-localized BETA icon.
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — "Beta" is translated even though the developer comment says it must not be.
    - Current: `페이지 번역 - 베타`
    - Source: `tooltiptext: Translate this page - Beta`
    - Suggest: `페이지 번역 - Beta`
    - The comment says "Beta" should not be translated because it mirrors the un-localized BETA icon in the panel.
- `sslv3Used` — `browser/chrome/overrides/appstrings.properties` — The translation uses 안정성 ('stability') where the en-US says 'safety', which is 안전성.
    - Current: `데이터의 안정성을`
    - Source: `Firefox cannot guarantee the safety of your data on %S because it uses SSLv3, a broken security protocol.`
    - Suggest: `데이터의 안전성을`
    - en-US: 'Firefox cannot guarantee the safety of your data'. 안정성 means stability, a different word from 안전성 (safety/security). As written, the warning says Firefox cannot guarantee the data's stability, not its safety from SSLv3 attacks.
- `netmonitor.context.saveResponseAs` — `devtools/client/netmonitor.properties` — 'Response' is rendered as '답변' here, but as '응답' everywhere else in the Network panel
    - Current: `다른 이름으로 답변 저장`
    - Source: `Save Response As`
    - Suggest: `다른 이름으로 응답 저장`
    - Every other HTTP response string in this file uses 응답 (응답 헤더, 응답 복사, 응답 페이로드). 답변 means a conversational reply, which is wrong for an HTTP response.
- `css-selector-warning-sibling-combinator-after-scope` — `devtools/client/tooltips.ftl` — The pseudo-class is capitalized as ':Scope'; the comment says ':scope' must not be translated
    - Current: `<strong>:Scope</strong>`
    - Source: `Sibling selectors after <strong>:scope</strong> will never match anything`
    - Suggest: `<strong>:scope</strong>`
    - The developer comment says ':scope should not be translated'. It is a lowercase CSS pseudo-class, so changing its case changes the identifier.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — 'Persist Logs' is left in English, but the comment says it must match the localized setting label '로그 유지'
    - Current: `"Persist Logs"로 인해`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `“로그 유지”로 인해`
    - The comment says: '"Persist Logs" should be kept in sync with webconsole.console.settings.menu.item.enablePersistentLogs.label', which is localized as '로그 유지'. As written, users can't find the setting the message names.
- `heading` — `dom/chrome/accessibility/mac/accessible.properties` — Non-standard spelling
    - Current: `머릿말`
    - Source: `heading`
    - Suggest: `머리말`
    - Standard Korean spelling is 머리말.
- `sslv3Used` — `dom/chrome/appstrings.properties` — 'safety' misspelled as 'stability'
    - Current: `안정성을 보장할 수 없습니다`
    - Source: `The safety of your data on %S could not be guaranteed because it uses SSLv3, a broken security protocol.`
    - Suggest: `안전성을 보장할 수 없습니다`
    - en-US 'safety of your data' is 안전성. 안정성 means stability.
- `ForbiddenHeaderWarning` — `dom/chrome/dom/dom.properties` — Typo
    - Current: `금지되 헤더`
    - Source: `Attempt to set a forbidden header was denied: %S`
    - Suggest: `금지된 헤더`
    - Missing final consonant.
- `ImportXULIntoContentWarning` — `dom/chrome/dom/dom.properties` — Leftover English word 'Importing'
    - Current: `Importing XUL 노드를`
    - Source: `Importing XUL nodes into a content document is deprecated. This functionality may be removed soon.`
    - Suggest: `XUL 노드를`
    - Untranslated fragment mixed into the Korean sentence.
- `InterceptedNonResponseWithURL` — `dom/chrome/dom/dom.properties` — Leftover English fragment duplicates the Korean
    - Current: `Failed to load '%1$S'를 읽지 못했습니다.`
    - Source: `Failed to load ‘%1$S’. A ServiceWorker passed a promise to FetchEvent.respondWith() that resolved with non-Response value ‘%2$S’.`
    - Suggest: `'%1$S'를 읽지 못했습니다.`
    - The English 'Failed to load' is left in front of its own Korean translation.
- `InterceptedUsedResponseWithURL` — `dom/chrome/dom/dom.properties` — Typo
    - Current: `여러면 접근하려면`
    - Source: `Failed to load ‘%S’. A ServiceWorker passed a used Response to FetchEvent.respondWith(). The body of a Response may only be read once. Use Response.clone() to access the body multiple times.`
    - Suggest: `여러 번 접근하려면`
    - '여러면' should be '여러 번'.
- `PointerLockDeniedFailedToLock` — `dom/chrome/dom/dom.properties` — Typo
    - Current: `떄문에`
    - Source: `Request for pointer lock was denied because the browser failed to lock the pointer.`
    - Suggest: `때문에`
    - Misspelling.
- `PushMessageBadCryptoKeyHeader` — `dom/chrome/dom/dom.properties` — Typo for 'public key'
    - Current: `공개기를`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. The ‘Crypto-Key‘ header must include a ‘dh‘ parameter containing the app server’s public key. See https://tools.ietf.org/html/draft-ietf-httpbis-encry…`
    - Suggest: `공개키를`
    - Misspelling.
- `PushMessageBadEncryptionHeader` — `dom/chrome/dom/dom.properties` — Duplicated syllable
    - Current: `포함함해야`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. The ‘Encryption’ header must include a unique ‘salt‘ parameter for each message. See https://tools.ietf.org/html/draft-ietf-httpbis-encryption-encodin…`
    - Suggest: `포함해야`
    - Typo.
- `PushMessageBadSenderKey` — `dom/chrome/dom/dom.properties` — Garbled parenthetical with duplicated number
    - Current: `(65 인코딩 되기 전 65 바이트)`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. The ‘dh‘ parameter in the ‘Crypto-Key‘ header must be the app server’s Diffie-Hellman public key, base64url-encoded (https://tools.ietf.org/html/rfc75…`
    - Suggest: `(인코딩 전 65 바이트)`
    - en-US: '(65 bytes before encoding)'.
- `PEAttSelUnexpected` — `dom/chrome/layout/css.properties` — Missing word makes the negation ungrammatical
    - Current: `적법하지 토큰`
    - Source: `Unexpected token in attribute selector: ‘%1$S’.`
    - Suggest: `적법하지 않은 토큰`
    - '않은' is missing.
- `TooLargeDashedRadius` — `dom/chrome/layout/css.properties` — Misspelling of 렌더링
    - Current: `solid로 랜더링합니다.`
    - Source: `Border radius is too large for ‘dashed’ style (the limit is 100000px). Rendering as solid.`
    - Suggest: `solid로 렌더링합니다.`
    - Standard spelling is 렌더링, which the locale uses elsewhere (e.g. layout_errors PrincipalWritingModePropagationWarning). The same misspelling is in TooLargeDottedRadius.
- `EncMetaUtf16` — `dom/chrome/layout/htmlparser.properties` — Misspelled verb ending
    - Current: `선언하으나`
    - Source: `A meta tag was used to declare the character encoding as UTF-16. This was interpreted as an UTF-8 declaration instead.`
    - Suggest: `선언했으나`
    - '선언하으나' is not valid Korean.
- `CompositorAnimationWarningNonScalingStroke` — `dom/chrome/layout/layout_errors.properties` — Stray space breaks the identifier
    - Current: `non-scaling- stroke`
    - Source: `Animations of ‘transform’ on content containing non-scaling-stroke elements cannot be run on the compositor`
    - Suggest: `non-scaling-stroke`
    - The keyword is non-scaling-stroke.
- `ScrollAnchoringDisabledInContainer` — `dom/chrome/layout/layout_errors.properties` — Conjugation error
    - Current: `작어서`
    - Source: `Scroll anchoring was disabled in a scroll container because of too many consecutive adjustments (%1$S) with too little total distance (%2$S px average, %3$S px total).`
    - Suggest: `작아서`
    - Correct conjugation of 작다 is 작아서.
- `SDAccessErrorCardMissing` — `dom/chrome/nsWebBrowserPersist.properties` — English source left appended to the Korean
    - Current: `다운로드 할 수 없습니다.Cannot download file because the SD card is missing.`
    - Source: `Cannot download file because the SD card is missing.`
    - Suggest: `다운로드할 수 없습니다.`
    - The en-US sentence is pasted after the translation.
- `SDAccessErrorCardReadOnly` — `dom/chrome/nsWebBrowserPersist.properties` — Typo
    - Current: `사용종이어서`
    - Source: `Cannot download file because the SD card is in use.`
    - Suggest: `사용 중이어서`
    - Misspelling of 사용 중.
- `CookieBlockedAll` — `netwerk/necko.properties` — Typo
    - Current: `떄문에`
    - Source: `Request to access cookie or storage on “%1$S” was blocked because we are blocking all storage access requests.`
    - Suggest: `때문에`
    - Misspelling.
- `CookieBlockedForeignByETP` — `netwerk/necko.properties` — 'third-party' misspelled; ETP feature name differs from the rest of the locale
    - Current: `모든 제3사 저장소 액세스 요청을 차단하고 있고 향상된 추적 보호가`
    - Source: `Request to access cookie or storage on “%1$S” was blocked because we are blocking all third-party storage access requests and Enhanced Tracking Protection is enabled.`
    - Suggest: `모든 제3자 저장소 액세스 요청을 차단하고 있고 향상된 추적 방지 기능이`
    - 제3자 is the term used elsewhere (e.g. CookieRejectedThirdParty). '향상된 추적 보호' appears only here; the rest of the tree uses '향상된 추적 방지'.
- `MOZILLA_PKIX_ERROR_CA_CERT_USED_AS_END_ENTITY` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo
    - Current: `있스니다`
    - Source: `The server uses a certificate with a basic constraints extension identifying it as a certificate authority. For a properly-issued certificate, this should not be the case.`
    - Suggest: `있습니다`
    - Misspelling.
- `MOZILLA_PKIX_ERROR_KEY_PINNING_FAILURE` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo
    - Current: `뮤효화`
    - Source: `The server uses key pinning (HPKP) but no trusted certificate chain could be constructed that matches the pinset. Key pinning violations cannot be overridden.`
    - Suggest: `무효화`
    - Misspelling.
- `SEC_ERROR_CERT_ADDR_MISMATCH` — `security/manager/chrome/pipnss/nsserrors.properties` — Misspelling of 'header'
    - Current: `메시지 해더`
    - Source: `Address in signing certificate does not match address in message headers.`
    - Suggest: `메시지 헤더`
    - Standard spelling is 헤더, used throughout the tree.
- `SEC_ERROR_USER_CANCELLED` — `security/manager/chrome/pipnss/nsserrors.properties` — Wrong verb form (passive instead of active)
    - Current: `사용자가 취소를 눌렸습니다.`
    - Source: `The user pressed cancel.`
    - Suggest: `사용자가 취소를 눌렀습니다.`
    - 눌렸습니다 is passive ('was pressed'), which is ungrammatical with a subject.
- `SSL_ERROR_EXPIRED_CERT_ALERT` — `security/manager/chrome/pipnss/nsserrors.properties` — Missing space between words
    - Current: `상대 측에서만료된`
    - Source: `SSL peer rejected your certificate as expired.`
    - Suggest: `상대 측에서 만료된`
    - The words run together.
- `certErrorMitM2` — `security/manager/chrome/pipnss/pipnss.properties` — Missing space between words
    - Current: `지원을받습니다`
    - Source: `%S is backed by the non-profit Mozilla, which administers a completely open certificate authority (CA) store. The CA store helps ensure that certificate authorities are following best practices for user security.`
    - Suggest: `지원을 받습니다`
    - Word spacing error in user-facing text.
- `getPKCS12FilePasswordMessage` — `security/manager/chrome/pippki/pippki.properties` — Wrong object particle
    - Current: `비밀번호을`
    - Source: `Please enter the password that was used to encrypt this certificate backup:`
    - Suggest: `비밀번호를`
    - After a vowel-final noun the particle is 를.
- `pippki-get-pkcs12-password-message` — `security/manager/security/pippki/pippki.ftl` — Wrong object particle
    - Current: `비밀번호을`
    - Source: `Please enter the password that was used to encrypt this certificate backup:`
    - Suggest: `비밀번호를`
    - After a vowel-final noun the particle is 를.
- `VK_UP` — `toolkit/chrome/global/keys.properties` — 위측 is not standard Korean; it should be 위쪽, matching 왼쪽/오른쪽 in the same block.
    - Current: `위측 화살표`
    - Source: `Up Arrow`
    - Suggest: `위쪽 화살표`
    - Non-standard word formation. VK_DOWN has the same problem (아래측 → 아래쪽).
- `delete-submitted-description` — `toolkit/crashreporter/aboutcrashes.ftl` — Typo: 충볼 should be 충돌.
    - Current: `전송된 충볼 보고서 목록`
    - Source: `This will remove the list of submitted crash reports but will not delete the submitted data. This cannot be undone.`
    - Suggest: `전송된 충돌 보고서 목록`
    - Spelling error.
- `delete-unsubmitted-description` — `toolkit/crashreporter/aboutcrashes.ftl` — Typo: 었습니다 should be 없습니다 ('cannot be undone').
    - Current: `되돌릴 수 었습니다.`
    - Source: `This will delete all unsubmitted crash reports and cannot be undone.`
    - Suggest: `되돌릴 수 없습니다.`
    - The typo removes the negation word from 'cannot be undone'.
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — The identifiers inside <code> tags were translated. The comment says not to translate them: event→이벤트, events→이벤트, metrics→메트릭.
    - Current: `<code>이벤트</code> 메트릭의 기본값은 <code>이벤트</code> 핑이고      다른 모든 메트릭의 기본값은 <code>메트릭</code> 핑입니다.`
    - Source: `Select from the preceding list the ping your instrumentation is in. If it’s in a <a data-l10n-name="custom-ping-link">custom ping</a>, choose that one. Otherwise, the default for <code>event</code> metrics is the <code>…`
    - Suggest: `<code>event</code> 메트릭의 기본값은 <code>events</code> 핑이고      다른 모든 메트릭의 기본값은 <code>metrics</code> 핑입니다.`
    - The comment says 'Do not translate strings between <code> </code> tags.' These are literal metric and ping type names that developers look up. The translation also merges 'event' and 'events' into one word, so the two different identifiers can no longer be told apart.
- `language-name-ee` — `toolkit/toolkit/intl/languageNames.ftl` — Ewe is mistransliterated as 이유어.
    - Current: `이유어`
    - Source: `Ewe`
    - Suggest: `에웨어`
    - en-US: Ewe. The standard Korean name is 에웨어.
- `language-name-io` — `toolkit/toolkit/intl/languageNames.ftl` — Ido is misspelled as 이다어.
    - Current: `이다어`
    - Source: `Ido`
    - Suggest: `이도어`
    - en-US: Ido.
- `language-name-kr` — `toolkit/toolkit/intl/languageNames.ftl` — Kanuri is misspelled as 카두리 and is missing the 어 suffix used everywhere else.
    - Current: `카두리`
    - Source: `Kanuri`
    - Suggest: `카누리어`
    - en-US: Kanuri.
- `language-name-pi` — `toolkit/toolkit/intl/languageNames.ftl` — Pali is misspelled as 파리어 (which reads as 'Paris language').
    - Current: `파리어`
    - Source: `Pali`
    - Suggest: `팔리어`
    - en-US: Pali.
- `region-name-ba` — `toolkit/toolkit/intl/regionNames.ftl` — Herzegovina is misspelled as 헤르체코비나.
    - Current: `보스니아 헤르체코비나`
    - Source: `Bosnia and Herzegovina`
    - Suggest: `보스니아 헤르체고비나`
    - Spelling error.
- `region-name-cg` — `toolkit/toolkit/intl/regionNames.ftl` — Brazzaville is misspelled as 프라차빌.
    - Current: `콩고-프라차빌`
    - Source: `Congo (Brazzaville)`
    - Suggest: `콩고-브라자빌`
    - en-US: Congo (Brazzaville).
- `region-name-et` — `toolkit/toolkit/intl/regionNames.ftl` — Ethiopia is misspelled as 에디오피아.
    - Current: `에디오피아`
    - Source: `Ethiopia`
    - Suggest: `에티오피아`
    - Spelling error.
- `region-name-me` — `toolkit/toolkit/intl/regionNames.ftl` — Montenegro is misspelled as 몬테니그로.
    - Current: `몬테니그로`
    - Source: `Montenegro`
    - Suggest: `몬테네그로`
    - Spelling error.
- `region-name-mg` — `toolkit/toolkit/intl/regionNames.ftl` — Madagascar is misspelled as 마다카스카르.
    - Current: `마다카스카르`
    - Source: `Madagascar`
    - Suggest: `마다가스카르`
    - Spelling error.
- `region-name-mm` — `toolkit/toolkit/intl/regionNames.ftl` — Myanmar is misspelled as 미안마.
    - Current: `미안마`
    - Source: `Burma`
    - Suggest: `미얀마`
    - Spelling error.
- _…and 3 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `fxa-adoption-passwords-title` — `browser/browser/featureCallout.ftl` — 'Password' is rendered as 암호, but the locale consistently uses 비밀번호.
    - Current: `암호가 저장되었습니다.`
    - Source: `Password saved. Let’s back it up.`
    - Suggest: `비밀번호가 저장되었습니다.`
    - Elsewhere the locale uses 비밀번호 for saved passwords (e.g. confirmation-hint-password-created '비밀번호 저장됨'), and the next string in this callout uses 비밀번호. 암호 is reserved for encryption here.
- `perplexity-callout-theme-1-subtitle-2` — `browser/browser/featureCallout.ftl` — The brand name Perplexity is misspelled as 'Perflexity'.
    - Current: `Perflexity를 사용해 보려면`
    - Source: `Ask questions. Get complete, well-cited answers. To try Perplexity, choose it from the search button.`
    - Suggest: `Perplexity를 사용해 보려면`
    - Brand misspelling. Sibling strings use Perplexity.
- `perplexity-callout-theme-2-title` — `browser/browser/featureCallout.ftl` — The brand name Perplexity is misspelled as 'Perflexity'.
    - Current: `Perflexity 사용해보기`
    - Source: `Try Perplexity: a new way to search`
    - Suggest: `Perplexity 사용해보기`
    - The brand is Perplexity, and the other strings in this group spell it correctly.
- `start-page-callout-primary-label` — `browser/browser/featureCallout.ftl` — The brand name Startpage is translated as 시작 페이지 on the button.
    - Current: `시작 페이지 사용해보기`
    - Source: `Try Startpage`
    - Suggest: `Startpage 사용해보기`
    - The comment forbids translating or transliterating Startpage.
- `start-page-callout-subtitle` — `browser/browser/featureCallout.ftl` — The brand name Startpage is translated as 시작 페이지 ('start page').
    - Current: `시작 페이지를 사용해 보세요.`
    - Source: `Try Startpage. It’s designed to keep your searches more private from the start.`
    - Suggest: `Startpage를 사용해 보세요.`
    - The group comment says Startpage is a brand name and must not be translated or transliterated. 시작 페이지 also reads as the browser's own start page.
- `hnt-card-wallpaper-header` — `browser/browser/newtab/onboarding.ftl` — "Wallpaper" is written "배경화면" here but "배경 화면" in the card body directly below and in the New Tab menu.
    - Current: `배경화면`
    - Source: `Pick a fresh wallpaper`
    - Suggest: `배경 화면`
    - The same term in the same card is written two different ways. hnt-card-wallpaper-body and newtab-widget-wrexhamafc-menu-wallpapers both use "배경 화면".
- `info-exposed-passwords-found` — `browser/browser/protections.ftl` — Spelling error: 걸처 should be 걸쳐.
    - Current: `걸처`
    - Source: `{$count ->} [one] Password exposed across all breaches [other] Passwords exposed across all breaches`
    - Suggest: `걸쳐`
    - The standard spelling of the connective form of 걸치다 is 걸쳐.
- `monitor-header-content-signed-in` — `browser/browser/protections.ftl` — Typo: 사용의 정보 should be 사용자의 정보 ("your info").
    - Current: `사용의 정보`
    - Source: `{ -monitor-brand-name } warns you if your info has appeared in a known data breach.`
    - Suggest: `사용자의 정보`
    - The syllable 자 is missing. 사용의 means "of use", which makes the sentence ungrammatical.
- `generated` — `devtools/client/debugger.properties` — Typo: '성성됨' should be '생성됨' (generated)
    - Current: `성성됨`
    - Source: `generated`
    - Suggest: `생성됨`
    - en-US 'generated' is the Source Map term for a generated source. '성성됨' is not a Korean word; it is a typo for 생성됨.
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “중단...” but the string it names, `watchpoints.submenu`, reads “중단…”
    - Current: `검사기에서 요소를 마우스 오른쪽 버튼으로 누르고 "중단..."을 선택하여 중단점 추가`
    - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
    - Suggest: `중단…`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `eyedropper.disabled.title` — `devtools/client/inspector.properties` — Typo: 'HTM' instead of 'HTML'
    - Current: `HTM이 아닌 문서에서 사용할 수 없음`
    - Source: `Unavailable in non-HTML documents`
    - Suggest: `HTML이 아닌 문서에서 사용할 수 없음`
    - en-US: 'Unavailable in non-HTML documents'. The 'L' of HTML is missing.
- `netmonitor.security.state.weak` — `devtools/client/netmonitor.properties` — The adjective is doubled: '약한 취약한 암호화'
    - Current: `약한 취약한 암호화`
    - Source: `This resource was transferred over a connection that used weak encryption.`
    - Suggest: `취약한 암호화`
    - en-US 'weak encryption'. Two adjectives with the same meaning sit side by side, which is ungrammatical. It looks like an edit that was never cleaned up.
- `netmonitor.toolbar.enablePersistentLogs.tooltip` — `devtools/client/netmonitor.properties` — Typo: '요정' (fairy) instead of '요청' (request)
    - Current: `요정 목록이 지워지지 않음`
    - Source: `If you enable this option the requests list will not be cleared each time you navigate to a new page`
    - Suggest: `요청 목록이 지워지지 않음`
    - en-US: 'the requests list will not be cleared'. 요정 means 'fairy'.
- `inactive-css-at-position-try-not-supported` — `devtools/client/tooltips.ftl` — The at-rule name is misspelled: '@position-tri' instead of '@position-try'
    - Current: `<strong>@position-tri</strong>`
    - Source: `<strong>{ $property }</strong> is not supported in <strong>@position-try</strong> rules.`
    - Suggest: `<strong>@position-try</strong>`
    - en-US names the CSS at-rule @position-try. It is a code identifier and must not be altered.
- `inactive-css-not-absolutely-positioned-item-fix` — `devtools/client/tooltips.ftl` — The CSS value is misspelled: 'position:absolve' instead of 'position:absolute'
    - Current: `<strong>position:absolve</strong>`
    - Source: `Try adding <strong>position:absolute</strong> to the element. { learn-more }`
    - Suggest: `<strong>position:absolute</strong>`
    - The comment says CSS properties and values in <strong> must not be translated. 'absolve' is not a valid CSS value, so a user who copies the fix gets broken CSS.
- `inactive-css-not-absolutely-positioned-item-fix-1` — `devtools/client/tooltips.ftl` — The CSS value is misspelled: 'position:absolve' instead of 'position:absolute'
    - Current: `<strong>position:absolve</strong>`
    - Source: `Try adding <strong>position:absolute</strong> to the element.`
    - Suggest: `<strong>position:absolute</strong>`
    - Same error as the -fix variant. 'absolve' is not a valid CSS value.
- `inactive-css-not-grid-or-absolutely-positioned-item-fix` — `devtools/client/tooltips.ftl` — The CSS value is misspelled: 'position:absolve' instead of 'position:absolute'
    - Current: `<strong>position:absolve</strong>`
    - Source: `Try adding <strong>position:absolute</strong> to the element, or <strong>display:grid</strong> or <strong>display:inline-grid</strong> to the element’s parent. { learn-more }`
    - Suggest: `<strong>position:absolute</strong>`
    - The CSS keyword must be kept verbatim. 'absolve' is invalid.
- `inactive-css-not-grid-or-absolutely-positioned-item-fix-1` — `devtools/client/tooltips.ftl` — The CSS value is misspelled: 'position:absolve' instead of 'position:absolute'
    - Current: `<strong>position:absolve</strong>`
    - Source: `Try adding <strong>position:absolute</strong> to the element, or <strong>display:grid</strong> or <strong>display:inline-grid</strong> to the element’s parent.`
    - Suggest: `<strong>position:absolute</strong>`
    - The CSS keyword must be kept verbatim. 'absolve' is invalid.
- `screenshotFileManual` — `devtools/shared/screenshot.properties` — Typo: 'ture' instead of 'true'
    - Current: `ture입니다`
    - Source: `True if the screenshot should save the file even when other options are enabled (eg. clipboard).`
    - Suggest: `true입니다`
    - The parameter takes the literal value true/false, as in the sibling strings '(true/false)'. 'ture' is a misspelling of the value the user must type.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — `preventedConsoleClear` quotes “Persist Logs” but the string it names, `webconsole.console.settings.menu.item.enablePersistentLogs.label`, reads “로그 유지”
    - Current: `console.clear()는 "Persist Logs"로 인해 차단되었습니다.`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `로그 유지`
    - In the source this string quotes “Persist Logs”, which is exactly the value of `webconsole.console.settings.menu.item.enablePersistentLogs.label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `CSSContainerRuleSingleConditionWarning` — `dom/chrome/dom/dom.properties` — API name casing changed
    - Current: `CSSContainerRule.containerquery는`
    - Source: `CSSContainerRule.containerName and CSSContainerRule.containerQuery don’t support multiple conditions. Use CSSContainerRule.conditions instead.`
    - Suggest: `CSSContainerRule.containerQuery는`
    - Do-not-translate identifier must match exactly.
- `EditContextCharacterBoundsWarning` — `dom/chrome/dom/dom.properties` — API name corrupted and DNT event name translated
    - Current: `캐릭터 바운드 업데이트 이벤트 리스너에서 AddContext.updateCharacterBounds()가`
    - Source: `EditContext.updateCharacterBounds() was not called synchronously in characterboundsupdate event listener. IME interface may move around unexpectedly for some users. More information: https://developer.mozilla.org/docs/W…`
    - Suggest: `characterboundsupdate 이벤트 리스너에서 EditContext.updateCharacterBounds()가`
    - The comment says do not translate EditContext.updateCharacterBounds() and characterboundsupdate. 'AddContext' is a wrong API name.
- `MozlockorientationDeprecatedWarning` — `dom/chrome/dom/dom.properties` — API name casing changed
    - Current: `mozlockOrientation()은`
    - Source: `mozLockOrientation() is deprecated. Use orientation.lock() instead.`
    - Suggest: `mozLockOrientation()은`
    - Do-not-translate identifier must match exactly.
- `ScreenFingerprintingProtectionWarning` — `dom/chrome/dom/dom.properties` — Property name casing changed
    - Current: `Screen.availwidth`
    - Source: `Fingerprinting Protection is altering screen.availWidth and screen.availHeight. These values may not match your actual screen dimensions. This protection helps prevent websites building a fingerprint that can be used to…`
    - Suggest: `screen.availWidth`
    - The property is screen.availWidth.
- `PEPRInheritsFieldInvalid` — `dom/chrome/layout/css.properties` — 'inherits' translated despite DNT note
    - Current: `'%S' @property 상속 설명자가`
    - Source: `@property inherits descriptor ‘%S’ does not match specified syntax.`
    - Suggest: `@property inherits 설명자 '%S'가`
    - The comment says do not translate 'inherits'.
- `PEPRInheritsFieldMissing` — `dom/chrome/layout/css.properties` — 'inherits' translated despite DNT note
    - Current: `@property 상속 설명자가 없습니다.`
    - Source: `@property inherits descriptor is missing.`
    - Suggest: `@property inherits 설명자가 없습니다.`
    - The comment says do not translate 'inherits' because it is a technical term.
- `CSPTrustedTypesPolicyViolation` — `dom/chrome/security/csp.properties` — 'Trusted Types' translated despite DNT note
    - Current: `신뢰할 수 있는 유형 정책 생성`
    - Source: `The page’s settings blocked creating a Trusted Types policy because it violates the following directive: “%1$S“`
    - Suggest: `Trusted Types 정책 생성`
    - The comment says do not translate 'Trusted Types' because it is a feature name. The same issue is in CSPROTrustedTypesPolicyViolation.
- `reportURINorReportToNotInReportOnlyHeader` — `dom/chrome/security/csp.properties` — Directive identifiers report-uri / report-to translated
    - Current: `보고-uri 지시문이나 보고 대상 지시문`
    - Source: `This site (%1$S) has a Report-Only policy without a report-uri directive nor a report-to directive. CSP will not block and cannot report violations of this policy.`
    - Suggest: `report-uri 지시자나 report-to 지시자`
    - These are literal CSP directive names that developers must type. The rest of the file keeps directive names in English and uses '지시자'.
- `BlockFileScriptWithWrongMimeType` — `dom/chrome/security/security.properties` — 'file: URI' translated and split
    - Current: `파일에서 스크립트 로드: URI (“%1$S”)의`
    - Source: `Loading script from file: URI (“%1$S”) was blocked because its MIME type (“%2$S”) is not a valid JavaScript MIME type.`
    - Suggest: `file: URI (“%1$S”)에서 스크립트 로드가`
    - The comment says do not translate 'file: URI'.
- `BlockRedirectToDataURI` — `dom/chrome/security/security.properties` — 'data: URI' translated; says 'not an allowed URI'
    - Current: `데이터로 리다이렉션: 허용된 URI가 아님`
    - Source: `Redirecting to data: URI not allowed (Blocked loading of: “%1$S”)`
    - Suggest: `data: URI로 리디렉션은 허용되지 않음`
    - The comment says do not translate 'data: URI'.
- `BlockTopLevelDataURINavigation` — `dom/chrome/security/security.properties` — 'data: URI' broken apart and translated; meaning garbled
    - Current: `최고 수준 데이터에 접근: URI 허용되지 않음`
    - Source: `Navigation to toplevel data: URI not allowed (Blocked loading of: “%1$S”)`
    - Suggest: `최상위 data: URI로의 탐색이 허용되지 않음`
    - The comment says do not translate 'data: URI'. Splitting it into '데이터에 접근: URI' makes the message unreadable.
- `WAICTManifestInvalidAnyHash` — `dom/chrome/security/security.properties` — Identifier any_hashes changed to all_hashes
    - Current: `“all_hashes”`
    - Source: `WAICT: Manifest has an invalid hash “%1$S” in “any_hashes”.`
    - Suggest: `“any_hashes”`
    - The comment says do not translate 'any_hashes'. The key name is wrong.
- `XFrameOptionsDeny` — `dom/chrome/security/security.properties` — Header name corrupted to X1-Frame-Options
    - Current: `“X1-Frame-Options”`
    - Source: `The loading of “%2$S” in a frame is denied by “X-Frame-Options“ directive set to “%1$S“.`
    - Suggest: `“X-Frame-Options”`
    - Do-not-translate header name has been altered.
- `certmgr-ca` — `security/manager/security/certificates/certManager.ftl` — 'certificate authorities' rendered as '인증 권한' instead of the locale's '인증 기관'
    - Current: `다음 인증 권한을 확인하는`
    - Source: `You have certificates on file that identify these certificate authorities`
    - Suggest: `다음 인증 기관을 확인하는`
    - The same tab is labelled '인증 기관', and the rest of the PSM strings use 인증 기관. 권한 means permission.
- `quitMenuitem.label` — `toolkit/chrome/global/fallbackMenubar.properties` — 'Quit' is rendered as 나가기, while the locale uses 종료 for Quit everywhere else.
    - Current: `나가기`
    - Source: `Quit`
    - Suggest: `종료`
    - Terminology inconsistency: for example profiledowngrade-quit, crashreporter-button-quit and flushFailExitButton all use 종료.
- `disabled-unsigned-devinfo` — `toolkit/toolkit/about/aboutAddons.ftl` — Misspelling: 메뉴얼 should be 매뉴얼, the standard loanword spelling of 'manual'.
    - Current: `메뉴얼`
    - Source: `Developers interested in getting their add-ons verified can continue by reading our <label data-l10n-name="learn-more">manual</label>.`
    - Suggest: `매뉴얼`
    - Standard Korean loanword orthography is 매뉴얼.
- `extensions-warning-imported-addons2` — `toolkit/toolkit/about/aboutAddons.ftl` — There is a double space inside the term 확장 기능.
    - Current: `확장  기능`
    - Source: `message: Please finalize the installation of extensions that were imported to { -brand-short-name }.`
    - Suggest: `확장 기능`
    - The stray space appears inside the visible message text.
- `about-logging-upload-question` — `toolkit/toolkit/about/aboutLogging.ftl` — Misspelling: 캡쳐 should be 캡처. aboutGlean and aboutWebrtc use 캡처.
    - Current: `캡쳐했습니다`
    - Source: `The profile data has been captured. Do you want to save or upload it?`
    - Suggest: `캡처했습니다`
    - The standard loanword spelling is 캡처, and the locale uses it elsewhere, for example '성능 프로필을 캡처'.
- `try-newer-driver` — `toolkit/toolkit/about/aboutSupport.ftl` — There is a double space between the two sentences.
    - Current: `차단되었습니다.  그래픽`
    - Source: `Blocked for your graphics driver version. Try updating your graphics driver to version { $driverVersion } or newer.`
    - Suggest: `차단되었습니다. 그래픽`
    - The extra space appears in the visible text.
- `webgl2-renderer` — `toolkit/toolkit/about/aboutSupport.ftl` — Misspelling: 랜더러 should be 렌더러, which is the spelling used in the WebGL 1 string just above.
    - Current: `WebGL2 드라이버 랜더러`
    - Source: `WebGL 2 Driver Renderer`
    - Suggest: `WebGL 2 드라이버 렌더러`
    - The standard loanword spelling is 렌더러, and webgl1-renderer uses it.
- `windows-messages-intro` — `toolkit/toolkit/about/aboutWindowsMessages.ftl` — Wrong object particle: 것 ends in a consonant, so it takes 을, not 를.
    - Current: `현재의 것를`
    - Source: `This page shows the most recent messages sent by Windows to the { -brand-short-name } browser windows. The bolded entry represents this window. Note that this page shows the most recent messages at the time the page was…`
    - Suggest: `현재의 것을`
    - This is a grammar error in user-visible text.

### E. Typography, punctuation & spacing

- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — `ai-window-delete-all-memories-message` uses three dots where this locale uses …
    - Current: `기존에 저장된 기억이 모두 삭제됩니다. 새로운 기억이 생성되는 것을 원치 않으시면 { -smart-window-brand-name } 설정에서 '...에서 학습' 옵션을 끄세요.`
    - Source: `Existing memories will be deleted. If you don’t want any new memories created, uncheck the options to “Learn from…” in { -smart-window-brand-name } settings.`
    - The tree uses … 394 times against 5 ASCII runs.
- `aiwindow-input-cta-menu-label-search-with` — `browser/browser/aiWindow.ftl` — `aiwindow-input-cta-menu-label-search-with` uses three dots where this locale uses …
    - Current: `다음으로 검색...`
    - Source: `Search with…`
    - The tree uses … 394 times against 5 ASCII runs.
- `aiwindow-input-model-select-menu-item-description` — `browser/browser/aiWindow.ftl` — The space between the owner name and the model name was dropped.
    - Current: `{ $ownerName }{ $model }`
    - Source: `{ $ownerName } { $model }`
    - Suggest: `{ $ownerName } { $model }`
    - en-US has '{ $ownerName } { $model }'. Without the space, the provider and model names merge into one word on screen.
- `smartbar-placeholder-hint-1` — `browser/browser/aiWindow.ftl` — `smartbar-placeholder-hint-1` uses three dots where this locale uses …
    - Current: `@로 최근 탭 지정...`
    - Source: `Use @ to mention recent tabs…`
    - The tree uses … 394 times against 5 ASCII runs.
- `crashed-subframe-title` — `browser/browser/contentCrash.ftl` — A space is missing between the two sentences.
    - Current: `손상되었습니다.{ -brand-product-name }`
    - Source: `title: Part of this page crashed. To let { -brand-product-name } know about this issue and get it fixed faster, please submit a report.`
    - Suggest: `손상되었습니다. { -brand-product-name }`
    - The visible tooltip text runs the sentences together. The comment says it should match crashed-subframe-message, which has the space.
- `sidebar-button-callout-vertical-tabs` — `browser/browser/featureCallout.ftl` — A stray space separates the noun from its object particle.
    - Current: `사이드바 버튼 을`
    - Source: `To show your tabs, select the sidebar button in the toolbar.`
    - Suggest: `사이드바 버튼을`
    - Korean particles attach directly to the noun. '버튼 을' is a visible spacing error.
- `genai-input-ask-provider` — `browser/browser/genai.ftl` — `genai-input-ask-provider` uses three dots where this locale uses …
    - Current: `{ $provider }에게 물어보기...`
    - Source: `placeholder: Ask { $provider }…`
    - The tree uses … 394 times against 5 ASCII runs.
- `more-from-moz-firefox-relay-button` — `browser/browser/preferences/moreFromMozilla.ftl` — The space between the brand name and 받기 is missing.
    - Current: `{ -relay-brand-short-name }받기`
    - Source: `Get { -relay-brand-short-name }`
    - Suggest: `{ -relay-brand-short-name } 받기`
    - Every other 'Get <brand>' label in the same file puts a space before 받기 ({ -monitor-brand-short-name } 받기, { -thunderbird-brand-short-name } 받기, { -relay-brand-short-name } 받기 in the box-link). Without the space, the brand name and the verb run together on screen.
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` uses three dots where this locale uses …
    - Current: `검사기에서 요소를 마우스 오른쪽 버튼으로 누르고 "중단..."을 선택하여 중단점 추가`
    - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
    - The tree uses … 394 times against 5 ASCII runs.
- `netmonitor.status.tooltip.cached` — `devtools/client/netmonitor.properties` — The space between status code and status text is missing
    - Current: `%1$S%2$S (캐시)`
    - Source: `%1$S %2$S (cached)`
    - Suggest: `%1$S %2$S (캐시)`
    - en-US '%1$S %2$S (cached)'. Without the space the code and text run together, e.g. '200OK'.
- `netmonitor.status.tooltip.simple` — `devtools/client/netmonitor.properties` — The space between status code and status text is missing
    - Current: `%1$S%2$S`
    - Source: `%1$S %2$S`
    - Suggest: `%1$S %2$S`
    - en-US '%1$S %2$S' renders as '200 OK'. Without the space the tooltip reads '200OK'. The sibling worker strings keep the space.
- `shortcuts-remove-button` — `toolkit/toolkit/about/aboutAddons.ftl` — 'Shortcut' is rendered as 바로 가기 here but as 단축키 in every other string in the shortcut-management UI.
    - Current: `바로 가기 제거`
    - Source: `aria-label: Remove shortcut`
    - Suggest: `단축키 제거`
    - The same surface uses 단축키 for keyboard shortcuts, for example '단축키 입력' and '중복 단축키'. 바로 가기 usually means a link or file shortcut.
- `about-glean-ping-list-optgroup-built-in` — `toolkit/toolkit/about/aboutGlean.ftl` — 'Pings' is left in English here, but the rest of the page, including the sibling optgroup, translates it as 핑.
    - Current: `내장 Ping`
    - Source: `label: Built-in Pings`
    - Suggest: `내장 핑`
    - The sibling label is '사용자 지정 핑', and the whole file uses 핑.
- `can-sandbox-content` — `toolkit/toolkit/about/aboutSupport.ftl` — 'Content' is spelled 콘텐트 here, while the rest of the file uses 콘텐츠.
    - Current: `콘텐트 프로세스 샌드박싱`
    - Source: `Content Process Sandboxing`
    - Suggest: `콘텐츠 프로세스 샌드박싱`
    - The neighbouring strings content-sandbox-level and content-win32k-lockdown-state use 콘텐츠.
- `about-webauthn-info-subsection-title` — `toolkit/toolkit/about/aboutWebauthn.ftl` — 'Authenticator' is rendered as 인증기 here and in the options heading, but as 인증자 in the config strings on the same page.
    - Current: `인증기 정보`
    - Source: `Authenticator info`
    - Suggest: `인증자 정보`
    - about-webauthn-auth-option-authnrcfg and uvacfg use 인증자. The page should use one term.
- `about-webrtc-raw-local-candidate` — `toolkit/toolkit/about/aboutWebrtc.ftl` — 'Local' is rendered as 지역 here but as 로컬 everywhere else on the page.
    - Current: `원시 지역 후보자`
    - Source: `Raw Local Candidate`
    - Suggest: `원시 로컬 후보자`
    - about-webrtc-local-candidate uses '로컬 후보자', and Local SDP is '로컬 SDP'. 지역 means 'regional'.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ko/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (0)

_Nothing closed by the fixer._

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/ko/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
