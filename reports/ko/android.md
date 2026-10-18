# Android l10n QA — ko

| | |
|---|---|
| **Generated** | 2026-10-18 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `dd8ca757b7dd` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `dd8ca757b7dd` |
| **Previous run** | 2026-10-16 @ `4d7697d1b89b` |
| **Mode** | incremental |
| **Strings reviewed this run** | 44 of 2,802 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ko: [firefox_ios](firefox_ios.md)

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
| Files | 45 |
| Strings | 2,802 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 9, `straight-double` 4, `curly-single` 1 | _mixed_ |
| apostrophe | `typographic` 1, `straight` 1 | _mixed_ |
| ellipsis | `char` 21 | **char** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (95)

> **Reads as a deliberate edit (9).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `felt_privacy_desc_card_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Dropping 'on this device' widens the claim to leaving no traces anywhere.
    - Current: `흔적 남기지 않기`
    - Source: `Leave no traces on this device`
    - Suggest: `이 기기에 흔적 남기지 않기`
    - The source limits the claim to this device. Private browsing does not hide activity from websites or networks, so the unqualified Korean promises more than the product does.
- `firefox_labs_website_isolation_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — 'Helps protect your data' becomes a flat claim that the feature prevents data leakage between tabs.
    - Current: `탭 간 데이터 유출을 방지합니다`
    - Source: `An extra barrier between websites that helps protect your data across tabs. May affect performance, stability, website compatibility, and how browsing history is saved.`
    - Suggest: `탭 간 데이터를 보호하는 데 도움이 됩니다`
    - The source hedges ('helps protect'). The Korean asserts that leakage is prevented, a guarantee the product does not make.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "and that you use it" is rendered as "how you use it" (사용 방법), which claims usage details are shared.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용하고 있다는 사실을`
    - The source shares only the fact that the user uses Firefox, not how they use it. The Korean tells users that wider usage data goes to marketing partners.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "and that you use it" is rendered as "how you use it" (사용 방법), which claims usage details are shared.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용하고 있다는 사실을`
    - The source shares only the fact of use. The Korean claims the product shares how the user uses Firefox.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "that you use it" is translated as "how you use it" (사용 방법), which overstates the data shared with marketing partners.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용한다는 사실을`
    - The source shares only the fact that the user uses Firefox. The Korean says the user's way of using Firefox is shared, which is a claim about wider data sharing than the product makes.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "that you use it" is translated as "how you use it" (사용 방법), which overstates the data shared with marketing partners.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용한다는 사실을`
    - The source shares only the fact of use. The Korean claims usage behaviour is shared with Mozilla's marketing partners, and the developer comment stresses that data practices stay the same.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "will cause websites to break" is softened to "may break" (깨질 수 있음), copying the wording of the third-party cookies option.
    - Current: `웹 사이트가 깨질 수 있음`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `웹 사이트가 깨짐`
    - The source states that blocking all cookies will break websites, as a certainty. That is how it differs from the 'may cause websites to break' wording on the third-party option. The Korean now tells users it only might break sites.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "that you use it" is rendered as "사용 방법" (how you use it), which the developer comment explicitly rules out.
    - Current: `사용 방법을`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `사용 중이라는 사실을`
    - The comment says "that you use it" means only that the user keeps using Firefox after installing it, not that Firefox tracks how they use it. The Korean says usage details are shared with marketing partners.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "Strives to collect only" became a flat statement that Mozilla collects only the necessary information.
    - Current: `오직 필요한 정보만을 수집합니다`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `꼭 필요한 정보만 수집하기 위해 노력합니다`
    - The source only says Mozilla *strives* to collect only what it needs. The Korean drops 'strives' and states it as a certain fact about the product's data collection, which is a stronger guarantee than the source gives.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 44 |
| 3 | Degraded language (grammar, spelling, terminology) | 43 |
| 4 | Cosmetic (typography, spacing) | 8 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_net_timeout_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ko/strings.xml` — Both 'device' references are translated as 'computer' (컴퓨터).
    - Current: `컴퓨터의 네트워크 연결을 점검해 보십시오`
    - Source: `{ <p> }The requested site did not respond to a connection request and the browser has stopped waiting for a reply.{ </p> } { <ul> } { <li> }Could the server be experiencing high demand or a temporary outage? Try again l…`
    - Suggest: `기기의 네트워크 연결을 점검해 보십시오`
    - The source says 'the device’s network connection' and 'Is your device or network…'. The Korean says 컴퓨터 in both places, which is wrong on Android; elsewhere the same text uses 기기. The second occurrence, '사용자의 컴퓨터 또는 네트워크', should likewise be '사용자의 기기 또는 네트워크'.
- `mozac_browser_errorpages_no_internet_error_code` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ko/strings.xml` — The error code literal was changed from NS_ERROR_OFFLINE to NS_ERROR_OFFline.
    - Current: `NS_ERROR_OFFline`
    - Source: `Error Code: NS_ERROR_OFFLINE`
    - Suggest: `NS_ERROR_OFFLINE`
    - The error code is a fixed identifier and must match the source exactly.
- `mozac_browser_errorpages_no_internet_message_2` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ko/strings.xml` — 'Try connecting on a different device' was translated as 'try connecting to a different device'.
    - Current: `다른 기기에 연결해 보세요`
    - Source: `Try connecting on a different device. Check your modem or router. Disconnect and reconnect to Wi-Fi.`
    - Suggest: `다른 기기에서 연결해 보세요`
    - The source means connecting from another device. '기기에 연결' means connecting to a device.
- `mozac_browser_errorpages_unknown_protocol_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ko/strings.xml` — The Korean says protocols require software that the browser cannot recognize, not software needed before the browser can recognize the protocols.
    - Current: `어떤 프로토콜은 브라우저가 인식할 수 없는 제3자 소프트웨어 또는 플러그인을 요할 수 있습니다.`
    - Source: `{ <p> }The address specifies a protocol (e.g., { <q> }wxyz://{ </q> }) the browser does not recognize, so the browser cannot properly connect to the site.{ </p> } { <ul> } { <li> }Are you trying to access multimedia or…`
    - Suggest: `어떤 프로토콜은 브라우저가 인식하려면 제3자 소프트웨어 또는 플러그인이 필요할 수 있습니다.`
    - The source says third-party software or plugins may be needed before the browser can recognize the protocols. The translation makes the browser unable to recognize the software.
- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ko/strings.xml` — The word "additional" is missing, so the title reads as a first data-collection request rather than an extra one.
    - Current: `데이터 수집을 요청함`
    - Source: `%1$s requests additional data collection`
    - Suggest: `추가 데이터 수집을 요청함`
    - The source says "requests additional data collection". This dialog asks for optional permissions beyond those already granted. The sibling title keeps 추가 ("추가 설정을 요청함").
- `mozac_feature_addons_updater_notification_heading_data_collection_permissions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ko/strings.xml` — The translation adds "권한" (permission) after the placeholder, so it says the extension will collect permissions rather than the listed data.
    - Current: `%1$s 권한을 수집할`
    - Source: `New required data collection: The developer says the extension will collect %1$s.`
    - Suggest: `%1$s 데이터를 수집할`
    - The source says the extension will collect %1$s, which is the list of data types being collected. Adding "권한" makes it "collect the %1$s permission", which is wrong and makes no sense.
- `mozac_feature_listentopage_error_could_not_finish_playing_audio` — `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values-ko/strings.xml` — "Couldn't finish playing" is rendered as "cannot end/stop playback".
    - Current: `오디오 재생을 종료할 수 없습니다.`
    - Source: `Couldn’t finish playing audio. Try again.`
    - Suggest: `오디오 재생을 완료할 수 없습니다.`
    - The source and the developer comment describe an error partway through playback, so the audio could not be played to the end. 종료할 수 없습니다 means the playback could not be stopped, which is a different error.
- `mozac_feature_prompts_collapse_credit_cards_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ko/strings.xml` — The text says "saved passwords" (비밀번호) where the source says "saved cards".
    - Current: `저장된 비밀번호 접기`
    - Source: `Collapse saved cards`
    - Suggest: `저장된 카드 접기`
    - The source and the developer comment both refer to the saved card options in the card selection prompt. The Korean names passwords instead, so screen readers will read out the wrong control.
- `mozac_feature_prompts_expand_credit_cards_content_description_2` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ko/strings.xml` — The text says "saved passwords" (비밀번호) where the source says "saved cards".
    - Current: `저장된 비밀번호 펼치기`
    - Source: `Expand saved cards`
    - Suggest: `저장된 카드 펼치기`
    - The source and the developer comment both refer to expanding the saved card options. The Korean names passwords, which is the wrong thing and duplicates the login string.
- `mozac_summarize_download_progress_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ko/strings.xml` — The in-progress title "Setting up summaries" is rendered as the noun phrase "summary settings", so it no longer says setup is in progress.
    - Current: `요약 설정`
    - Source: `Setting up summaries`
    - Suggest: `요약 설정 중`
    - The comment says this is the title of the download-in-progress screen. "요약 설정" reads as "summary settings" (like a settings screen title), not as setup happening now.
- `mozac_lib_send_crash_report_in_progress` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-ko/strings.xml` — The in-progress notification is translated as an action label ("send crash report") instead of a progress status ("sending crash report").
    - Current: `%1$s에 충돌 보고서 보내기`
    - Source: `Sending crash report to %1$s`
    - Suggest: `%1$s에 충돌 보고서 보내는 중`
    - The source "Sending crash report to %1$s" and its developer comment describe a notification saying the crash report service is running. The Korean is identical to the checkbox label "Send crash report to %1$s" and reads as an action, not an ongoing status. The sibling progress notifications in this batch use "… 중".
- `add_to_exiting_tab_group_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The color name is rendered as a possessor of the tab group ("%3$s의") instead of a separate color attribute.
    - Current: `%2$d개 탭, %3$s의 %1$s 탭 그룹에 추가`
    - Source: `{$quantity ->} [one] Add to %1$s tab group, %2$d tab, color %3$s [other] Add to %1$s tab group, %2$d tabs, color %3$s`
    - Suggest: `%1$s 탭 그룹에 추가, 탭 %2$d개, 색상 %3$s`
    - The source lists the color as a separate attribute ("color %3$s"). "%3$s의 %1$s 탭 그룹" reads as "%3$s's %1$s tab group", so screen-reader users hear the color as if it owned the group.
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "Department" is translated as "부서", which means a department inside an organization, not a region of a country.
    - Current: `부서`
    - Source: `Department`
    - Suggest: `도`
    - The developer comment says this is the administrative division used in countries like Colombia and Nicaragua. "부서" means a department in a company or organization, so the address field label names the wrong thing. A territorial term such as "도" (or "주") is needed.
- `alternative_app_icon_option_pride` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "Pride" is translated as "자부심" (personal self-esteem), not as the LGBTQ+ Pride theme name.
    - Current: `자부심`
    - Source: `Pride`
    - Suggest: `프라이드`
    - The developer comment says this is the rainbow-colour icon supporting the LGBTQ+ community. "자부심" means personal pride or self-esteem and loses that meaning. Korean usually calls Pride "프라이드".
- `browser_menu_default_banner_subtitle_2` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "private" is rendered as "안전하며" (safe/secure) instead of conveying privacy.
    - Current: `안전하며`
    - Source: `Fast, private, and made for you.`
    - Suggest: `사생활을 보호하며`
    - The source says the browser is private, not secure. Elsewhere the locale renders private as 사생활 보호, so 안전 changes what quality the product claims.
- `certificate_warning_homepage_card_hcr1_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The title uses a noun phrase that can read as "the update before March 14" instead of telling the user to update.
    - Current: `3월 14일 이전 업데이트`
    - Source: `Update before March 14`
    - Suggest: `3월 14일 전에 업데이트하세요`
    - The developer comment says "Update" is a verb: the user is being told to update before March 14. The Korean noun phrase "3월 14일 이전 업데이트" is ambiguous and can be read as the name of an earlier update rather than a call to act. The related title already uses the imperative form ("Firefox를 업데이트하세요").
- `collection_open_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The button label "Open tabs" (open this collection's tabs) is translated as the noun phrase "tabs that are open".
    - Current: `열린 탭`
    - Source: `Open tabs`
    - Suggest: `탭 열기`
    - The developer comment says this is the button that opens the selected collection's tabs, so 'Open' is a verb. '열린 탭' means 'opened/open tabs', which reads as a list label, not an action.
- `etp_known_fingerprinters_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "Fingerprinters" (trackers) is rendered as "digital fingerprints" (the data itself).
    - Current: `알려진 디지털 지문`
    - Source: `Known Fingerprinters`
    - Suggest: `알려진 핑거프린터`
    - The comment says this is a category of trackers, meaning the agents that do the fingerprinting. 디지털 지문 names the fingerprint, not the tracker that collects it.
- `etp_redirect_trackers_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Category name 'Redirect Trackers' is rendered as 'tracker redirection' (an action), and uses 트래커 instead of the 추적기 used by sibling categories.
    - Current: `트래커 리디렉션`
    - Source: `Redirect Trackers`
    - Suggest: `리디렉션 추적기`
    - The source names a category of trackers (trackers that use redirects). '트래커 리디렉션' reads as 'redirecting trackers'. Sibling titles use 추적기 (소셜 미디어 추적기).
- `felt_privacy_desc_card_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Dropping 'on this device' widens the claim to leaving no traces anywhere.
    - Current: `흔적 남기지 않기`
    - Source: `Leave no traces on this device`
    - Suggest: `이 기기에 흔적 남기지 않기`
    - The source limits the claim to this device. Private browsing does not hide activity from websites or networks, so the unqualified Korean promises more than the product does.
- `firefox_labs_website_isolation_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — 'Helps protect your data' becomes a flat claim that the feature prevents data leakage between tabs.
    - Current: `탭 간 데이터 유출을 방지합니다`
    - Source: `An extra barrier between websites that helps protect your data across tabs. May affect performance, stability, website compatibility, and how browsing history is saved.`
    - Suggest: `탭 간 데이터를 보호하는 데 도움이 됩니다`
    - The source hedges ('helps protect'). The Korean asserts that leakage is prevented, a guarantee the product does not make.
- `ip_protection_settings_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "more private" is rendered as "더 안전하고" (safer), changing the claimed benefit from privacy to safety.
    - Current: `탐색을 더 안전하고`
    - Source: `Turn VPN on to make your browsing more private and harder to trace.`
    - Suggest: `탐색을 더 비공개로 보호하고`
    - The source says "more private and harder to trace". "안전" means safe/secure, which is a different benefit, and it doesn't match how the promo card renders the same phrase (사생활 보호).
- `link_sharing_toggle_body` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The 'invite your friends to try' meaning is lost; the Korean says sharing a link lets you make friends browse faster and safer with %1$s.
    - Current: `%1$s로 친구들을 더 빠르고 안전하게 탐색하게 할 수 있습니다.`
    - Source: `Invite your friends to try faster, safer browsing with %1$s every time you share a link on WhatsApp.`
    - Suggest: `친구들에게 %1$s로 더 빠르고 안전한 탐색을 경험해 보도록 초대하세요.`
    - The source invites friends to try faster, safer browsing with %1$s. The Korean drops both the invitation and the 'try', and instead says that the act of sharing makes friends browse faster and safer.
- `nova_onboarding_marketing_body` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "and that you use it" is rendered as "how you use it" (사용 방법), which claims usage details are shared.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold. %1$s`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용하고 있다는 사실을`
    - The source shares only the fact that the user uses Firefox, not how they use it. The Korean tells users that wider usage data goes to marketing partners.
- `nova_onboarding_marketing_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "and that you use it" is rendered as "how you use it" (사용 방법), which claims usage details are shared.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용하고 있다는 사실을`
    - The source shares only the fact of use. The Korean claims the product shares how the user uses Firefox.
- `nova_onboarding_marketing_body_4` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The direction is reversed: the Korean has the user tell Mozilla where they came from, but the source has Mozilla telling the referring platform that the user uses Firefox.
    - Current: `Firefox를 사용하는 플랫폼의 출처를 Mozilla에 알려주시면 더 많은 사람들에게 도움을 주실 수 있습니다.`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `Mozilla가 여러분이 거쳐 온 플랫폼에 여러분이 Firefox를 사용한다는 사실을 알릴 수 있도록 허용해 주시면 더 많은 사람들에게 다가가는 데 도움이 됩니다.`
    - The source and the developer comment say Mozilla informs the external platform the user came from. The Korean drops the third-party sharing and reverses who informs whom.
- `nova_onboarding_marketing_body_5` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "The platform you came from" became "the platform where you use Firefox", and what Mozilla informs is garbled.
    - Current: `여러분이 Firefox를 사용하는 플랫폼에 대해 Mozilla가 알릴 수 있도록`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox.`
    - Suggest: `Mozilla가 여러분이 거쳐 온 플랫폼에 여러분이 Firefox를 사용한다는 사실을 알릴 수 있도록`
    - Per the comment, the platform is the referring source, and Mozilla tells it that the user uses Firefox. The Korean says Mozilla informs about the platform where Firefox is used.
- `nova_onboarding_marketing_body_6` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "The platform you came from" became "the platform where you use Firefox", and what Mozilla informs is garbled.
    - Current: `여러분이 Firefox를 사용하는 플랫폼에 대해 Mozilla가 알릴 수 있도록`
    - Source: `Help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `Mozilla가 여러분이 거쳐 온 플랫폼에 여러분이 Firefox를 사용한다는 사실을 알릴 수 있도록`
    - Per the comment, the platform is the referring source, and Mozilla tells it that the user uses Firefox. The Korean says something different.
- `nova_onboarding_marketing_body_7` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The direction is reversed: the Korean has the user tell Mozilla where they came from, but the source has Mozilla telling the referring platform that the user uses Firefox.
    - Current: `Firefox를 사용하는 플랫폼의 출처를 Mozilla에 알려주시면 더 많은 사람들에게 도움을 주실 수 있습니다.`
    - Source: `You can help us reach more people by allowing Mozilla to inform the platform you came from that you use Firefox. %1$s`
    - Suggest: `Mozilla가 여러분이 거쳐 온 플랫폼에 여러분이 Firefox를 사용한다는 사실을 알릴 수 있도록 허용해 주시면 더 많은 사람들에게 다가가는 데 도움이 됩니다.`
    - The source and the developer comment say Mozilla informs the external platform the user came from. The Korean reverses who informs whom.
- `nova_onboarding_marketing_primary_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "Help Firefox" (a call to support Firefox) was translated as "Firefox 도움말", meaning Firefox help documentation.
    - Current: `Firefox 도움말`
    - Source: `Help Firefox`
    - Suggest: `Firefox 돕기`
    - The button asks the user to help Firefox by allowing data sharing. 도움말 means help pages or a manual.
- `nova_onboarding_set_to_default_title_2` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The Korean says "open all links that have built-in privacy protection", attaching the built-in privacy to the links instead of the browser.
    - Current: `개인 정보 보호 기능이 내장된 모든 링크 열기`
    - Source: `Open all your links with built-in privacy`
    - Suggest: `내장된 개인 정보 보호 기능으로 모든 링크 열기`
    - The source means opening all links with the browser's built-in privacy. The Korean relative clause modifies 링크 (links).
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "that you use it" is translated as "how you use it" (사용 방법), which overstates the data shared with marketing partners.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용한다는 사실을`
    - The source shares only the fact that the user uses Firefox. The Korean says the user's way of using Firefox is shared, which is a claim about wider data sharing than the product makes.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "that you use it" is translated as "how you use it" (사용 방법), which overstates the data shared with marketing partners.
    - Current: `Firefox를 발견한 방법과 사용 방법을`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `Firefox를 발견한 방법과 Firefox를 사용한다는 사실을`
    - The source shares only the fact of use. The Korean claims usage behaviour is shared with Mozilla's marketing partners, and the developer comment stresses that data practices stay the same.
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "will cause websites to break" is softened to "may break" (깨질 수 있음), copying the wording of the third-party cookies option.
    - Current: `웹 사이트가 깨질 수 있음`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `웹 사이트가 깨짐`
    - The source states that blocking all cookies will break websites, as a certainty. That is how it differs from the 'may cause websites to break' wording on the third-party option. The Korean now tells users it only might break sites.
- `preference_enhanced_tracking_protection_custom_known_fingerprinters` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "Known Fingerprinters" is rendered as "known digital fingerprints" instead of the trackers that collect fingerprints.
    - Current: `알려진 디지털 지문`
    - Source: `Known Fingerprinters`
    - Suggest: `알려진 핑거프린터`
    - The option blocks fingerprinters, which are scripts that collect digital fingerprints. '디지털 지문' names the fingerprint itself, not the tracker.
- `preferences_marketing_data_description_4` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "that you use it" is rendered as "사용 방법" (how you use it), which the developer comment explicitly rules out.
    - Current: `사용 방법을`
    - Source: `Share how you discovered Firefox and that you use it with Mozilla’s marketing technology partners.`
    - Suggest: `사용 중이라는 사실을`
    - The comment says "that you use it" means only that the user keeps using Firefox after installing it, not that Firefox tracks how they use it. The Korean says usage details are shared with marketing partners.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The title uses the noun phrase "검색 설정" (settings for search) where the source means the action of searching through settings.
    - Current: `검색 설정`
    - Source: `Search settings`
    - Suggest: `설정 검색`
    - The developer comment says "Search" is a verb here, so the title should mean searching the settings. In Korean, "검색 설정" reads as the settings for the search feature, which names a different screen.
- `tab_collection_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The deletion prompt calls the tab collection a "file" (파일), which the source never says.
    - Current: `%1$s 파일을 삭제하시겠습니까?`
    - Source: `Are you sure you want to delete %1$s?`
    - Suggest: `%1$s 컬렉션을 삭제하시겠습니까?`
    - The developer comment says %1$s is the collection name, and the source simply asks "Are you sure you want to delete %1$s?". A tab collection is not a file, so adding 파일 misdescribes what the user is about to delete.
- `terms_of_use_prompt_body_line_two_alternative` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Combined with the link text "자세히", the sentence reads "자세히에 대해 더 알아볼 수 있습니다" (learn more about 'details'), which is ungrammatical and loses the meaning "learn more here".
    - Current: `%1$s에 대해 더 알아볼 수 있습니다.`
    - Source: `You can learn more %1$s.`
    - Suggest: `%1$s에서 더 알아볼 수 있습니다.`
    - The comment says %1$s is the link text for "here" (localized as "자세히"). The source means "You can learn more here". The Korean frame treats the placeholder as a topic ("about X"), so the assembled sentence is nonsense. A locative frame with the link text "여기" would fix it.
- `webcompat_reporter_reason_site_is_deceptive` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "deceptive" is translated as "suspicious" (의심스러운).
    - Current: `의심스러운 사이트`
    - Source: `This site is deceptive`
    - Suggest: `사기성 사이트`
    - The reason option says the site is deceptive. 의심스러운 means only 'suspicious', a weaker and different claim. Firefox usually uses 사기 wording for deceptive sites.
- `about_content` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "%1$s puts you in control" is rendered as "you can use %1$s with various features".
    - Current: `%1$s를 여러 기능으로 사용할 수 있습니다.`
    - Source: `{ <p> }%1$s puts you in control.{ </p> } { <p> }Use it as a private browser: { <ul> } { <li> }Search and browse right in the app{ </li> } { <li> }Block trackers (or update settings to allow trackers){ </li> } { <li> }Er…`
    - Suggest: `%1$s로 직접 제어할 수 있습니다.`
    - The source says the app gives the user control. The Korean says the app can be used for many features, which is a different claim.
- `cfr_for_toolbar_shield_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The translation says the site itself was stopped, not that it was stopped from spying on the user.
    - Current: `사용자를 감시하는 이 사이트를 중지했습니다`
    - Source: `Got ‘em! We stopped this site from spying on you. Tap the shield any time to see what we’re blocking.`
    - Suggest: `이 사이트가 사용자를 감시하지 못하도록 막았습니다`
    - The source says 'We stopped this site from spying on you', meaning the tracking was blocked. The Korean reads as 'we stopped (halted) this site that spies on the user', which describes a different action.
- `preference_auto_battery_theme` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "절전 모드로 설정" means "set to battery saver mode", not "set by Battery Saver".
    - Current: `절전 모드로 설정`
    - Source: `Set by Battery Saver`
    - Suggest: `절전 모드에 따라 설정`
    - Per the comment, this option makes Battery Saver decide the dark or light theme. In Korean, '~로 설정' reads as switching something into power-saving mode.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "Strives to collect only" became a flat statement that Mozilla collects only the necessary information.
    - Current: `오직 필요한 정보만을 수집합니다`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `꼭 필요한 정보만 수집하기 위해 노력합니다`
    - The source only says Mozilla *strives* to collect only what it needs. The Korean drops 'strives' and states it as a certain fact about the product's data collection, which is a stronger guarantee than the source gives.
- `promote_search_widget_dialog_picture_content_description` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — 'Search widget' (a noun naming the widget) is translated as the action 'search for widgets'.
    - Current: `위젯 검색하기`
    - Source: `Search widget`
    - Suggest: `검색 위젯`
    - The developer comment says this describes a picture of the search widget. 위젯 검색하기 means 'search for a widget', so a screen reader would describe the image wrongly.

### C. Grammar, agreement & spelling

- `mozac_browser_engine_system_alert_title` — `mozilla-mobile/android-components/components/browser/engine-system/src/main/res/values-ko/strings.xml` — '메세지' is a misspelling of the standard form '메시지'.
    - Current: `메세지`
    - Source: `The page at %1$s says:`
    - Suggest: `메시지`
    - The standard spelling is 메시지, and the related auth dialog string already uses it.
- `mozac_feature_addons_permissions_web_navigation_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ko/strings.xml` — The dependent noun "중" should be spaced from the noun before it.
    - Current: `탐색중에`
    - Source: `Access browser activity during navigation`
    - Suggest: `탐색 중에`
    - Under standard Korean spacing rules, the dependent noun 중 is written with a space before it.
- `mozac_feature_addons_permissions_web_navigation_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ko/strings.xml` — The dependent noun "중" should be spaced from the noun before it.
    - Current: `탐색중에`
    - Source: `Access browser activity during navigation.`
    - Suggest: `탐색 중에`
    - Under standard Korean spacing rules, the dependent noun 중 is written with a space before it.
- `mozac_feature_downloads_again_dialog_title_with_unknown_size` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-ko/strings.xml` — Incorrect spacing in the verb "다운로드하다", which also differs from the sibling dialog title.
    - Current: `다운로드 하시겠습니까?`
    - Source: `Download file again?`
    - Suggest: `다운로드하시겠습니까?`
    - "다운로드하다" is one verb and is written without a space, as the matching string mozac_feature_downloads_again_dialog_title already does ("다운로드하시겠습니까?").
- `mozac_feature_downloads_file_not_supported2` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-ko/strings.xml` — The object has the topic marker 은 right after the subject's 는, and 다운로드할 is wrongly written with a space.
    - Current: `이 파일 형식은 다운로드 할 수 없습니다`
    - Source: `%1$s can’t download this file type`
    - Suggest: `이 파일 형식을 다운로드할 수 없습니다`
    - '파일 형식' is the object of 다운로드하다, so it should take 을. Using 은 here stacks a second topic marker after %1$s는, which reads awkwardly. The noun-derived verb 다운로드하다 also takes the adnominal ending as one word: 다운로드할, not 다운로드 할.
- `mozac_feature_media_sharing_camera` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-ko/strings.xml` — 켜저 is misspelled; the correct form is 켜져.
    - Current: `켜저 있음`
    - Source: `Camera is on`
    - Suggest: `켜져 있음`
    - 켜다 + -어 contracts to 켜져. The microphone string in the same file spells it correctly.
- `mozac_feature_media_sharing_camera_and_microphone` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-ko/strings.xml` — 켜저 is misspelled; the correct form is 켜져.
    - Current: `켜저 있음`
    - Source: `Camera and microphone are on`
    - Suggest: `켜져 있음`
    - 켜다 + -어 contracts to 켜져. The microphone string in the same file spells it correctly.
- `about_debug_menu_toast_progress` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The dependent noun "데" must be spaced: "활성화하는 데".
    - Current: `활성화하는데`
    - Source: `Debug menu: %1$d click(s) left to enable`
    - Suggest: `활성화하는 데`
    - Here "데" means "for/in order to" and is a dependent noun, so standard Korean spacing requires "활성화하는 데". Written together it becomes the connective ending -는데.
- `ai_controls_block_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Spacing error: the verb 해제하다 is split, giving "해제 할" instead of "해제할".
    - Current: `차단 해제 할 수 있습니다`
    - Source: `You won’t see new or current AI enhancements in %1$s, or pop-ups about them. Afterwards, you can unblock anything you want to keep using.  Blocking also affects extensions that use AI provided by %1$s.`
    - Suggest: `차단 해제할 수 있습니다`
    - 해제하다 is a single verb, so its conjugated form 해제할 must be written without a space under Korean spacing rules.
- `bookmark_cannot_edit_root` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Spacing error: "편집 할" should be written "편집할".
    - Current: `편집 할 수 없습니다`
    - Source: `Can’t edit default folders`
    - Suggest: `편집할 수 없습니다`
    - In the verb "편집하다", "하다" attaches to the noun. Korean spelling rules require "편집할 수".
- `browser_main_menu_content_description_navigation_header` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Non-standard spelling 네비게이션; the standard loanword spelling is 내비게이션.
    - Current: `네비게이션`
    - Source: `Navigation`
    - Suggest: `내비게이션`
    - The National Institute of Korean Language's standard spelling of 'navigation' is 내비게이션.
- `browser_menu_no_extensions_installed_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Spacing error: 사용중인 should be written 사용 중인.
    - Current: `사용중인`
    - Source: `No extensions enabled`
    - Suggest: `사용 중인`
    - 중 is a dependent noun and is written with a space under Korean orthography rules.
- `certificate_warning_homepage_card_hcw3_message` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Word-spacing error: '사용중인' needs a space before the bound noun '중'.
    - Current: `사용중인`
    - Source: `Your version of Firefox will stop working properly on March 14 because a root certificate is expiring.`
    - Suggest: `사용 중인`
    - In standard Korean spacing, the bound noun '중' is written apart from the word before it. The same batch spaces it correctly in pnw2_title ('사용 중입니다').
- `credit_cards_expiration_date_year` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Standalone noun for 'year' should be spelled '연', not '년', when it does not follow a number.
    - Current: `유효 기간 년`
    - Source: `Expiration Date Year`
    - Suggest: `유효 기간 연`
    - Under the initial-sound rule in Korean spelling (두음 법칙), '년' is written that way only directly after a number (e.g. 2025년). Used alone as the label for the 'Expiration Date Year' field, it should be '연'.
- `delete_language_all_languages_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Wrong object particle: '일부분' ends in a consonant, so it takes '을', not '를'.
    - Current: `언어 일부분를`
    - Source: `If you delete all languages, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `언어 일부분을`
    - Korean object particle after a final consonant (ㄴ) must be '을'; '일부분를' is ungrammatical.
- `delete_language_file_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Wrong object particle: '일부분' ends in a consonant, so it takes '을', not '를'.
    - Current: `언어 일부분를`
    - Source: `If you delete this language, %1$s will download partial languages to your cache as you translate.`
    - Suggest: `언어 일부분을`
    - Korean object particle after a final consonant (ㄴ) must be '을'; '일부분를' is ungrammatical.
- `download_rename_and_change_location_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "다운로드 하시겠습니까" has a space inside the single verb "다운로드하다", and the sibling string spells it without one.
    - Current: `다운로드 하시겠습니까?`
    - Source: `Download file? (%s)`
    - Suggest: `다운로드하시겠습니까?`
    - In Korean, 하다 attached to a noun forms one word and is written without a space. The sibling string download_rename_and_change_location_dialog_title_with_unknown_size has the same source text and correctly writes "다운로드하시겠습니까?".
- `email_masks_max_free_tier_reached` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Duplicated object particle in "마스크를 하나를".
    - Current: `마스크를 하나를 선택했습니다`
    - Source: `You’ve used your 5 free email masks, so we picked one for you to reuse.`
    - Suggest: `마스크를 하나 선택했습니다`
    - Two object markers (를) in a row are ungrammatical. The quantifier 하나 should have no particle.
- `exceptions_empty_message_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — '비활성화 할' should be written as one word, '비활성화할'.
    - Current: `비활성화 할 수`
    - Source: `Exceptions let you disable tracking protection for selected sites.`
    - Suggest: `비활성화할 수`
    - Under Korean spacing rules, '-하다' verbs stay attached to the adnominal ending: 비활성화할.
- `help_catch_trackers` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Wrong particle: 도와주다 takes the object marker 를, not 에.
    - Current: `추적기 잡기에 도와주세요`
    - Source: `Help catch trackers`
    - Suggest: `추적기 잡기를 도와주세요`
    - '잡기에 도와주세요' is ungrammatical. The correct form is '잡기를 도와주세요' or '잡는 데 도움을 주세요'.
- `ip_protection_onboarding_body_promo` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "탐색을 보다 사생활 보호하고" is ungrammatical because the noun-verb "사생활 보호하다" can't take "탐색을" as its object here.
    - Current: `탐색을 보다 사생활 보호하고`
    - Source: `Turn it on to make your browsing more private and harder to trace. Try it now to get unlimited bandwidth through %1$s. %2$s`
    - Suggest: `탐색을 더 비공개로 보호하고`
    - The source means "make your browsing more private". The Korean construction doesn't parse as "make browsing more private".
- `ip_protection_toolbar_pill_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "활성화 되어" should be written without a space as "활성화되어".
    - Current: `활성화 되어`
    - Source: `VPN is active.`
    - Suggest: `활성화되어`
    - Under standard Korean spacing rules, 되다 used as a suffix is attached to the noun (활성화되다).
- `nova_onboarding_marketing_secondary_button_text_2` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The negative answer is misspelled as 아니오. The standard form is 아니요, which the sibling string already uses.
    - Current: `아니오`
    - Source: `No`
    - Suggest: `아니요`
    - In standard Korean, the polite "No" answer is 아니요. 아니오 is the sentence-final form of 아니다, not an answer word.
- `preferences_delete_browsing_data_on_quit` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The dependent noun 시 is attached to 종료 when it should be spaced.
    - Current: `종료시`
    - Source: `Delete browsing data on quit`
    - Suggest: `종료 시`
    - Under standard Korean spacing rules, 시 meaning 'when' is a dependent noun and is written separately: 종료 시 탐색 데이터 삭제.
- `preferences_sync_category_summary` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — '동기화 할' has a space it shouldn't; standard Korean spelling attaches 할 to the 하다-verb stem: '동기화할'.
    - Current: `동기화 할`
    - Source: `Manage what syncs on all your connected devices`
    - Suggest: `동기화할`
    - 동기화하다 is a single verb, so its form 동기화할 is written without a space. The neighbouring string preferences_sync_category already spells it '동기화할'.
- `share_error_snackbar` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The verb 공유하다 is split by a space; it should be written 공유할.
    - Current: `공유 할 수 없음`
    - Source: `Cannot share to this app`
    - Suggest: `공유할 수 없음`
    - In Korean, the 하다 verb 공유하다 is written as one word, so its 할 form must stay attached: 공유할 수 없음.
- `shortcuts_update_error` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The dependent noun 데 needs a space before it: 업데이트하는 데.
    - Current: `업데이트하는데 실패했습니다`
    - Source: `Failed to update the app icon. Remove existing shortcuts and try again.`
    - Suggest: `업데이트하는 데 실패했습니다`
    - Here 데 is a dependent noun meaning 'in doing', not the connective ending -는데. Standard spelling puts a space before it: 업데이트하는 데 실패했습니다.
- `terms_of_use_prompt_message_1` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Wrong object particle: the substituted nouns "이용 약관" and "개인정보처리방침" end in a consonant and need "을", not "를".
    - Current: `%1$s %2$s를 도입하고 %3$s를 업데이트했습니다.`
    - Source: `We’ve introduced a %1$s %2$s and updated our %3$s.`
    - Suggest: `%1$s %2$s을 도입하고 %3$s을 업데이트했습니다.`
    - %2$s and %3$s are filled with "이용 약관" and "개인정보처리방침", which both end in a final consonant (관, 침). That produces the ungrammatical forms "이용 약관를" and "개인정보처리방침를".
- `translations_bottom_sheet_info_message` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The verb 이루어지다 is wrongly split into two words as "이루어 집니다".
    - Current: `이루어 집니다`
    - Source: `For your privacy, translations never leave your device. New languages and improvements coming soon! %1$s`
    - Suggest: `이루어집니다`
    - 이루어지다 is a single verb, so Korean spelling rules require it to be written as one word: 이루어집니다. The meaning still matches the source, since translations happening on the device means they never leave it.
- `unsubmitted_crash_requested_by_devs_dialog_never_button` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "다시 표시 않음" is ungrammatical; 않다 needs the -지 form of the verb.
    - Current: `다시 표시 않음`
    - Source: `Never show again`
    - Suggest: `다시 표시하지 않음`
    - Korean negation with 않다 needs a -지 form of the verb (표시하지 않음). Putting 않음 straight after the noun 표시 is a grammar error. The source is 'Never show again'.
- `webcompat_reporter_reason_checkout` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Wrong word spacing in 체크 아웃 and 쇼핑 할.
    - Current: `결제, 체크 아웃 또는 쇼핑 할 수 없음`
    - Source: `Can’t pay, check out or shop`
    - Suggest: `결제, 체크아웃 또는 쇼핑할 수 없음`
    - Under Korean spacing rules, 체크아웃 is a single loanword and 쇼핑하다 is one verb, so 쇼핑할 is written without a space.
- `find_in_page` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — Spacing error: the bound noun 내 must be written as a separate word.
    - Current: `페이지내 검색`
    - Source: `Find in Page`
    - Suggest: `페이지 내 검색`
    - Under standard Korean spacing rules, 내 (meaning 'within') is a bound noun and is written with a space after the noun it follows.
- `onboarding_first_screen_subtitle` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The subtitle ends sentences with full stops after a connective (-고) and a modifier (-는), so it reads as ungrammatical Korean.
    - Current: `빠르고. 사생활 보호되고. 방해 없는.`
    - Source: `Fast. Private. No distractions.`
    - Suggest: `빠름. 사생활 보호. 방해 없음.`
    - "Fast. Private. No distractions." is three short phrases that each stand alone. The Korean puts a full stop after word forms that need something to follow them: "빠르고" and "보호되고" end in "-고" ("and…"), and "없는" needs a noun after it. A noun-style ending (빠름 / 사생활 보호 / 방해 없음) keeps the three short phrases and is grammatical.
- `preference_category_cookies` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "데이타" is a non-standard spelling of "데이터".
    - Current: `데이타`
    - Source: `Cookies and Site Data`
    - Suggest: `데이터`
    - Standard Korean spelling of 'data' is 데이터. The locale uses it elsewhere too.
- `preference_category_data_choices` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — "데이타" is a non-standard spelling of "데이터".
    - Current: `데이타 선택`
    - Source: `Data Choices`
    - Suggest: `데이터 선택`
    - Standard Korean spelling of 'data' is 데이터.
- `preference_performance_block_javascript_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — Misspelling: "에상치" should be "예상치".
    - Current: `에상치 못한`
    - Source: `Pages may load faster, but may also behave unexpectedly`
    - Suggest: `예상치 못한`
    - The correct spelling of 'unexpected' is 예상치 못한; 에상치 is a typo.
- `preference_privacy_and_security_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — Non-standard spelling "데이타" instead of the standard "데이터".
    - Current: `데이타`
    - Source: `Tracking, cookies, data choices`
    - Suggest: `데이터`
    - Standard Korean orthography for 'data' is 데이터.
- `preference_privacy_should_block_cookies_third_party_tracker_cookies_option` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The particle 만 is wrongly separated from the noun it attaches to.
    - Current: `쿠키 만 차단`
    - Source: `Block 3rd-party tracker cookies only`
    - Suggest: `쿠키만 차단`
    - Under Korean spacing rules, particles such as 만 attach to the preceding noun. The sibling string also writes it as 쿠키만.
- `preference_privacy_stealth_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The negative adverb 못 needs a space before the verb: 못 찍게.
    - Current: `못찍게`
    - Source: `Hide webpages when switching apps and block taking screenshots.`
    - Suggest: `못 찍게`
    - Standard Korean spacing writes the adverb 못 apart from the verb it modifies.
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — Misspelling: 헤제 should be 해제 (unlock).
    - Current: `잠금 헤제에`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `잠금 해제에`
    - The correct Korean word for 'unlock/release' is 해제; 헤제 is a spelling error.
- `search_add_error_format` — `mozilla-mobile/focus-android/app/src/main/res/values-ko/strings.xml` — The connective ending '-는지' is wrongly split into '-는 지'.
    - Current: `일치하는 지`
    - Source: `Check that search string matches Example format`
    - Suggest: `일치하는지`
    - In '일치하는지', '-는지' is a connective ending for an indirect question ('whether it matches'), so Korean spelling rules write it attached. Spacing it as '는 지' is only correct when 지 is the bound noun for elapsed time, which is not the meaning here.

### D. Terminology, register & consistency

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ko/strings.xml` — 'device' was rendered as '컴퓨터' (computer) on a mobile error page.
    - Current: `네트워크에 컴퓨터가 연결되어`
    - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
    - Suggest: `네트워크에 기기가 연결되어`
    - The source says 'device', and other strings on these pages use '기기'. '컴퓨터' looks left over from desktop Firefox.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ko/strings.xml` — 'your device' was rendered as '컴퓨터' (computer).
    - Current: `컴퓨터의 문제가 아니라`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `기기의 문제가 아니라`
    - The source says 'not your device', and '기기' is used elsewhere on these pages.
- `mozac_browser_errorpages_unknown_proxy_host_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ko/strings.xml` — 'device' was rendered as '컴퓨터' (computer).
    - Current: `컴퓨터가 활성화된 네트워크에`
    - Source: `{ <p> }The browser is configured to use a proxy server, but the proxy could not be found.{ </p> } { <ul> } { <li> }Is the browser’s proxy configuration correct? Check the settings and try again.{ </li> } { <li> }Is the…`
    - Suggest: `기기가 활성화된 네트워크에`
    - The source asks whether the device is connected. '기기' is the term used elsewhere on these pages.
- `homepage_shortcuts_show_all_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — 'Shortcuts' is rendered as 단축키 (keyboard shortcut) instead of 바로 가기, the term used on the rest of this section.
    - Current: `모든 단축키 보기`
    - Source: `Show all shortcuts`
    - Suggest: `모든 바로 가기 보기`
    - The homepage shortcut tiles are called 바로 가기 in homepage_shortcuts_title and homepage_shortcuts_add_shortcut. 단축키 means a keyboard shortcut, which is the wrong concept for these tiles.
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "inactive" is rendered as "비활동" here but as "비활성" in the toggle title on the same screen.
    - Current: `비활동 섹션`
    - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
    - Suggest: `비활성 섹션`
    - The feature is labeled "비활성 탭" (preferences_inactive_tabs_toggle_title). The summary should use the same term so the section name matches what the user sees.

### E. Typography, punctuation & spacing

- `etp_known_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Missing space in "않도록합니다".
    - Current: `않도록합니다`
    - Source: `Stops uniquely identifiable data from being collected about your device that can be used for tracking purposes.`
    - Suggest: `않도록 합니다`
    - Standard Korean spacing separates the connective ending -도록 from the auxiliary verb 합니다.
- `preference_doh_title` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — The protocol name is capitalized as "DNS Over HTTPS", unlike the source and the summary string on the same screen.
    - Current: `DNS Over HTTPS`
    - Source: `DNS over HTTPS`
    - Suggest: `DNS over HTTPS`
    - The protocol's proper name is "DNS over HTTPS" with a lowercase "over". The source uses that form, and so does the Korean summary string (preference_doh_summary), so the title is inconsistent with it.
- `protection_panel_banner_protected_blocked_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — Double space between "추적기" and the tracker count in the visible text.
    - Current: `추적기  %1$d개`
    - Source: `{$quantity ->} [one] %1$d tracker blocked on this site. [other] %1$d trackers blocked on this site.`
    - Suggest: `추적기 %1$d개`
    - The doubled space is part of the text users read on the banner; a single space is correct.
- `unsubmitted_crash_dialog_body` — `mozilla-mobile/fenix/app/src/main/res/values-ko/strings.xml` — "해결하는데" needs a space before 데, which is a separate word here.
    - Current: `해결하는데 도움을`
    - Source: `Crash reports help us to diagnose and fix issues with the browser. Reports may include personal or sensitive data. %s`
    - Suggest: `해결하는 데 도움을`
    - In '~하는 데 도움을 주다', 데 is a separate word meaning 'for doing' and is normally written with a space before it.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ko/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._
