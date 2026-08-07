# Scrape Creators Endpoint Test Matrix

- Version: V0.1
- Status: Draft
- Authority: Test Matrix
- Scope: Complete test matrix for all 29 currently observed Scrape Creators endpoints.
- Depends On: [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md), [02_DATA_SOURCE_CAPABILITY_MAP.md](02_DATA_SOURCE_CAPABILITY_MAP.md), [06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md](06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md)
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Pending Andy Review

## Matrix Rules

All endpoints start with `current_test_status: Not Run` and `final_capability_verdict: Pending Test`. Future-stage endpoints remain in this matrix. Testing only SIG-P0 core candidates is not complete reconnaissance.

`positive_case_defined` means a success case is required only when prerequisite, authorization, plan access, quota, and safe legal input are available within the approved Campaign Budget And Safety Gate. If those conditions are not available, an evidence-backed blocked, unavailable, not applicable, or deferred status can complete current reconnaissance for that endpoint.

`snapshot_retest_requirement` values are limited to `Required`, `Conditional`, and `Not Applicable`.

- `Required`: repeated snapshot testing is needed to understand volatile metric, live, or changing feed behavior.
- `Conditional`: repeated snapshot testing depends on the first response fields, cost, quota, and whether a volatile field is actually returned.
- `Not Applicable`: repeated snapshot testing is not useful for the endpoint's current reconnaissance question.

`snapshot_retest_rationale` must explain the endpoint-specific reason. It must not be a mechanical Yes / No field. Raw evidence required means canonical redacted request evidence, raw response evidence, redacted response evidence, and field observations; raw HTTP requests must not be persisted.

## Overview Matrix

| endpoint_id | api_family | endpoint_name | candidate_stage | candidate_business_purpose | prerequisite_entity | required_auth_or_plan | positive_case_defined | negative_case_defined | pagination_test_required | snapshot_retest_requirement | snapshot_retest_rationale | market_language_test_required | cost_quota_test_required | raw_evidence_required | current_test_status | final_capability_verdict | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TT-01 | TikTok | Profile | SIG-P1 | Observe creator profile identity and public account indicators. | public user | Unknown | Yes | Yes | Yes | Conditional | Retest only if first response exposes volatile public counts or freshness fields. | If supported | Yes | Yes | Not Run | Pending Test | Seed for creator and profile-video links. |
| TT-02 | TikTok | Profile Region | SIG-P1 | Observe public region signal for a profile if available. | public user | Unknown | Yes | Yes | Unknown until tested | Not Applicable | Region lookup is a bounded identity/attribute check, not a metric snapshot question. | Yes | Yes | Yes | Not Run | Pending Test | Region is not buyer market. |
| TT-03 | TikTok | User's Audience Demographics | SIG-P1 | Observe creator audience estimate limits. | public user | Unknown | Yes | Yes | Unknown until tested | Conditional | Retest only if response includes dated estimates or unstable demographic coverage. | Yes | Yes | Yes | Not Run | Pending Test | Not for C02 creator-size analysis. |
| TT-04 | TikTok | Collection Videos | SIG-P1 | Observe videos exposed by a collection surface. | collection identity | Unknown | Yes | Yes | Yes | Conditional | Retest only if collection membership or ordering appears time-sensitive. | If supported | Yes | Yes | Not Run | Pending Test | Collection membership needs verification. |
| TT-05 | TikTok | Profile Videos | SIG-P1 | Collect public videos from a creator profile. | public user | Unknown | Yes | Yes | Yes | Conditional | Retest only if first response suggests changing inventory, pinned order, or metric snapshots. | If supported | Yes | Yes | Not Run | Pending Test | Useful for creator concentration. |
| TT-06 | TikTok | Video Info | SIG-P0 | Verify video identity, public metadata, and metrics. | video ID or URL | Unknown | Yes | Yes | Usually no, verify | Required | P0 needs metric snapshot semantics for public performance fields. | If supported | Yes | Yes | Not Run | Pending Test | P0 core candidate. |
| TT-07 | TikTok | Transcript | SIG-P0 | Retrieve transcript availability and text. | video ID | Unknown | Yes | Yes | Unknown until tested | Not Applicable | Transcript text availability is the target evidence; repeated metric snapshot testing is not relevant. | Language critical | Yes | Yes | Not Run | Pending Test | P0 core candidate. |
| TT-08 | TikTok | Live | SIG-P1 | Observe live discovery or live availability. | live context | Unknown | Yes | Yes | Yes | Required | Live availability and ranking can change quickly during reconnaissance. | If supported | Yes | Yes | Not Run | Pending Test | May be unavailable without live seed. |
| TT-09 | TikTok | Live Info | SIG-P1 | Retrieve public live metadata for known live identity. | live ID | Unknown | Yes | Yes | Usually no, verify | Required | Live metadata and viewer-like values are inherently volatile. | If supported | Yes | Yes | Not Run | Pending Test | Depends on live identity. |
| TT-10 | TikTok | Comments | SIG-P1 | Retrieve public comments for a video. | video ID | Unknown | Yes | Yes | Yes | Conditional | Retest only if comment count, ordering, or restriction state affects interpretation. | Language critical | Yes | Yes | Not Run | Pending Test | Comment availability can be restricted. |
| TT-11 | TikTok | Comment Replies | SIG-P1 | Retrieve public replies for a comment. | comment ID | Unknown | Yes | Yes | Yes | Conditional | Retest only if reply count or visibility changes affect relationship evidence. | Language critical | Yes | Yes | Not Run | Pending Test | Depends on Comments. |
| TT-12 | TikTok | Following | SIG-P1 | Observe profile following relationships if exposed. | public user | Unknown | Yes | Yes | Yes | Conditional | Retest only if social graph visibility or counts appear dynamic. | If supported | Yes | Yes | Not Run | Pending Test | Social graph is not commercial proof. |
| TT-13 | TikTok | Followers | SIG-P1 | Observe profile follower relationships if exposed. | public user | Unknown | Yes | Yes | Yes | Conditional | Retest only if follower list sampling, counts, or visibility are returned. | If supported | Yes | Yes | Not Run | Pending Test | Follower list may be unavailable or sampled. |
| TT-14 | TikTok | Search Users | SIG-P1 | Discover creators by text query. | query text | Unknown | Yes | Yes | Yes | Conditional | Retest only if ranking, personalization, or market controls need stability evidence. | Yes | Yes | Yes | Not Run | Pending Test | Search ranking semantics unknown. |
| TT-15 | TikTok | Search Suggestions | SIG-P1 | Observe search-expression suggestions. | query prefix | Unknown | Yes | Yes | Yes | Conditional | Retest only if suggestions appear personalized, regional, or rapidly changing. | Yes | Yes | Yes | Not Run | Pending Test | Future P1, not P0 core pipeline. |
| TT-16 | TikTok | Search by Hashtag | SIG-P0 | Collect candidate videos by hashtag. | hashtag | Unknown | Yes | Yes | Yes | Conditional | Retest if ranking, pagination, or metric snapshots are needed for P0 source stability. | Yes | Yes | Yes | Not Run | Pending Test | P0 core candidate. |
| TT-17 | TikTok | Search by Keyword | SIG-P0 | Collect candidate videos by keyword. | query text | Unknown | Yes | Yes | Yes | Conditional | Retest if search ranking, pagination, or market controls affect P0 collection reliability. | Yes | Yes | Yes | Not Run | Pending Test | P0 core candidate. |
| TT-18 | TikTok | Top Search | SIG-P1 | Observe top search expressions or results. | market or query context | Unknown | Yes | Yes | Yes | Conditional | Retest only if top results are time-windowed, trending, or market-sensitive. | Yes | Yes | Yes | Not Run | Pending Test | Top semantics must be verified. |
| TT-19 | TikTok | Get popular creators | SIG-P1 | Observe popular creator discovery. | category or market context | Unknown | Yes | Yes | Yes | Conditional | Retest only if popularity ranking or category membership appears volatile. | Yes | Yes | Yes | Not Run | Pending Test | Popularity may not match product category. |
| TT-20 | TikTok | Get Song Details | SIG-P1 | Retrieve public sound or song metadata. | song ID | Unknown | Yes | Yes | Usually no, verify | Conditional | Retest only if response includes usage counts, freshness, or changing availability. | If supported | Yes | Yes | Not Run | Pending Test | Seeds song-video relationship. |
| TT-21 | TikTok | TikToks using Song | SIG-P1 | Collect videos associated with a sound or song. | song ID | Unknown | Yes | Yes | Yes | Conditional | Retest only if song-video membership or ranking changes affect conclusions. | If supported | Yes | Yes | Not Run | Pending Test | Sound use is not product demand. |
| TT-22 | TikTok | Trending Feed | SIG-P1 | Observe trend feed sample and its limits. | market or feed context | Unknown | Yes | Yes | Yes | Conditional | Retest if first response indicates trend window, personalization, or feed rotation. | Yes | Yes | Yes | Not Run | Pending Test | Personalization risk must be checked. |
| SHOP-01 | TikTok Shop | Shop Search | SIG-P3 | Discover public shops. | shop query | Unknown | Yes | Yes | Yes | Conditional | Retest only if shop ranking or regional visibility affects commercial visibility interpretation. | Yes | Yes | Yes | Not Run | Pending Test | Commercial Visibility / L3-adjacent. |
| SHOP-02 | TikTok Shop | Shop Products | SIG-P3 | List public products for a shop. | shop ID | Unknown | Yes | Yes | Yes | Conditional | Retest only if product inventory, ordering, or availability changes are returned. | Yes | Yes | Yes | Not Run | Pending Test | Product listing is not transaction proof. |
| SHOP-03 | TikTok Shop | Product Details | SIG-P3 | Retrieve public product detail visibility. | product ID | Unknown | Yes | Yes | Usually no, verify | Conditional | Retest only if price, availability, review counts, or freshness fields are returned. | Yes | Yes | Yes | Not Run | Pending Test | Does not replace ProductBrief. |
| SHOP-04 | TikTok Shop | Product Reviews | SIG-P3 | Retrieve public product review signals. | product ID | Unknown | Yes | Yes | Yes | Conditional | Retest only if review count, ordering, or pagination changes are material. | Language critical | Yes | Yes | Not Run | Pending Test | Reviews are not full buyer population. |
| SHOP-05 | TikTok Shop | User Showcase | SIG-P3 | Observe public user-product showcase relationship. | user ID or showcase identity | Unknown | Yes | Yes | Yes | Conditional | Retest only if showcase membership or product visibility appears time-sensitive. | Yes | Yes | Yes | Not Run | Pending Test | Showcase does not prove clicks or sales. |
| AD-01 | TikTok Ad Library | Ad Library Search | SIG-P2 | Search public ad materials. | ad query | Unknown | Yes | Yes | Yes | Conditional | Retest only if ad search ranking, availability, or time window affects findings. | Yes | Yes | Yes | Not Run | Pending Test | Public ad visibility only. |
| AD-02 | TikTok Ad Library | Ad Library Ad | SIG-P2 | Retrieve public ad material details. | ad ID | Unknown | Yes | Yes | Usually no, verify | Conditional | Retest only if ad status, creative availability, or disclosed metadata changes. | Yes | Yes | Yes | Not Run | Pending Test | Does not prove spend or GMV. |

## Detailed Endpoint Tests

### TT-01 Profile

| Item | Plan |
|---|---|
| Endpoint ID | TT-01 |
| Endpoint Name | Profile |
| Candidate Business Purpose | Verify creator identity, public profile indicators, and account-level fields useful for creator concentration analysis. |
| Candidate Signal Layer | L1/L2 creator visibility. |
| Prerequisites | Legal public user discovered from search or known public profile. |
| Seed Data Source | Search Users, Search by Keyword, Profile Videos, or manual public URL. |
| Inputs To Verify | User identity input, URL handling, market or region options if present. |
| Positive Test Cases | Fetch a known public creator profile and record identity and public metric fields. |
| Negative Test Cases | Invalid user, unavailable user, private or restricted user if safe. |
| Edge Cases | Renamed handle, missing avatar/name fields, zero public counts. |
| Pagination Cases | Verify whether endpoint is single-object or paginated. |
| Identity Fields To Verify | User ID, handle, profile URL, display name stability. |
| Time Fields To Verify | Any profile update or collection time fields. |
| Metric Fields To Verify | Follower-like public counts only if actually returned. |
| Missingness Cases | Missing profile region, hidden metrics, null biography. |
| Market / Language Cases | Region fields are signals, not buyer market. |
| Cost / Quota Cases | Record per-profile cost and plan restrictions. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw response, redacted response, field observations. |
| Business Interpretation Risks | Creator profile cannot prove buyer demographics or sales. |
| Adoption Criteria | Stable public user identity and interpretable public fields. |
| Rejection Criteria | No stable identity, inaccessible endpoint, or unusable response. |
| Current Status | Not Run |
| Open Questions | Which identity field is stable across profile-related endpoints? |

### TT-02 Profile Region

| Item | Plan |
|---|---|
| Endpoint ID | TT-02 |
| Endpoint Name | Profile Region |
| Candidate Business Purpose | Check whether profile region is exposed and how it differs from target market or audience market. |
| Candidate Signal Layer | L1/L2 auxiliary region visibility. |
| Prerequisites | Public user with Profile result. |
| Seed Data Source | TT-01 Profile. |
| Inputs To Verify | User identity input and any region lookup mode. |
| Positive Test Cases | Fetch region for a public profile with known public context. |
| Negative Test Cases | Invalid user, user without region, restricted profile. |
| Edge Cases | Region absent, ambiguous, stale, or inconsistent with profile language. |
| Pagination Cases | Verify no pagination or document if present. |
| Identity Fields To Verify | User ID and profile reference used for lookup. |
| Time Fields To Verify | Region observation time or update fields if present. |
| Metric Fields To Verify | None expected unless returned; do not infer. |
| Missingness Cases | Missing region, null region, unknown region value. |
| Market / Language Cases | Region does not equal buyer market or audience region. |
| Cost / Quota Cases | Record whether region lookup is separately billed. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw response, redacted response, field observations. |
| Business Interpretation Risks | Misreading creator region as market demand. |
| Adoption Criteria | Region field exists, is traceable, and has clear limitations. |
| Rejection Criteria | No usable field or unclear identity link. |
| Current Status | Not Run |
| Open Questions | Is region platform-declared, inferred, or API-derived? |

### TT-03 User's Audience Demographics

| Item | Plan |
|---|---|
| Endpoint ID | TT-03 |
| Endpoint Name | User's Audience Demographics |
| Candidate Business Purpose | Determine whether creator audience estimates exist and what limited research questions they can support. |
| Candidate Signal Layer | L1/L2 auxiliary audience visibility. |
| Prerequisites | Public creator account and authorization or plan access if required. |
| Seed Data Source | TT-01 Profile or TT-19 Get popular creators. |
| Inputs To Verify | Creator identity input, market or time options if present. |
| Positive Test Cases | Fetch demographics for an eligible public creator. |
| Negative Test Cases | Creator without audience data, invalid user, plan-gated user. |
| Edge Cases | Small creator, partial demographics, conflicting percentages. |
| Pagination Cases | Verify whether demographics are single-object or segmented pages. |
| Identity Fields To Verify | User ID linkage to demographic output. |
| Time Fields To Verify | Demographic snapshot time or freshness fields. |
| Metric Fields To Verify | Only observed demographic measures; no buyer inference. |
| Missingness Cases | Hidden segments, null percentages, suppressed categories. |
| Market / Language Cases | Audience country or language fields require source verification. |
| Cost / Quota Cases | Likely plan-sensitive; record gating and cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw response, redacted response, field observations. |
| Business Interpretation Risks | Must not become true buying audience or `ResearchTask.primary_audience`. |
| Adoption Criteria | Clear source, method, coverage, and limitations. |
| Rejection Criteria | Opaque estimates that cannot be interpreted safely. |
| Current Status | Not Run |
| Open Questions | What source and algorithm produce the estimate? |

### TT-04 Collection Videos

| Item | Plan |
|---|---|
| Endpoint ID | TT-04 |
| Endpoint Name | Collection Videos |
| Candidate Business Purpose | Determine whether collection surfaces expose grouped video samples. |
| Candidate Signal Layer | L1/L2 content supply visibility. |
| Prerequisites | Legal public collection identity. |
| Seed Data Source | Manual public collection URL or platform discovery. |
| Inputs To Verify | Collection ID or URL, count limit, pagination token. |
| Positive Test Cases | Fetch videos from an accessible collection. |
| Negative Test Cases | Invalid collection, private collection, empty collection. |
| Edge Cases | Removed videos, duplicate videos, mixed topics. |
| Pagination Cases | First page, next page, end page, repeated cursor. |
| Identity Fields To Verify | Collection ID, video IDs, creator IDs. |
| Time Fields To Verify | Video publish time and collection observation time. |
| Metric Fields To Verify | Video metrics if returned. |
| Missingness Cases | Missing collection title, missing video fields. |
| Market / Language Cases | Collection language may not match target market. |
| Cost / Quota Cases | Record per-page cost and limits. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw pages, redacted pages, field observations. |
| Business Interpretation Risks | Collection membership is not market demand. |
| Adoption Criteria | Stable collection-video identities and pagination. |
| Rejection Criteria | Unavailable or opaque collection semantics. |
| Current Status | Not Run |
| Open Questions | What creates or defines a collection in this endpoint? |

### TT-05 Profile Videos

| Item | Plan |
|---|---|
| Endpoint ID | TT-05 |
| Endpoint Name | Profile Videos |
| Candidate Business Purpose | Collect videos from a creator to analyze creator concentration and account-level content supply. |
| Candidate Signal Layer | L1/L2 creator video visibility. |
| Prerequisites | Public user with videos. |
| Seed Data Source | TT-01 Profile or TT-14 Search Users. |
| Inputs To Verify | User ID or handle, pagination, count limit. |
| Positive Test Cases | Fetch first and next page for a public creator. |
| Negative Test Cases | Invalid user, creator with no videos, restricted profile. |
| Edge Cases | Pinned videos, reposts, deleted videos, zero metrics. |
| Pagination Cases | Cursor behavior, maximum retrievable count, end page. |
| Identity Fields To Verify | User ID, video ID, source URL. |
| Time Fields To Verify | Published time and collected time. |
| Metric Fields To Verify | Views, likes, comments, shares if returned. |
| Missingness Cases | Missing captions, hidden metrics, inaccessible videos. |
| Market / Language Cases | Creator language does not prove audience market. |
| Cost / Quota Cases | Record per-page usage. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw pages, redacted pages, field observations. |
| Business Interpretation Risks | High performance may reflect account size. |
| Adoption Criteria | Stable user-video link and clear pagination. |
| Rejection Criteria | No stable video IDs or unusable pagination. |
| Current Status | Not Run |
| Open Questions | Are reposts and original posts distinguishable? |

### TT-06 Video Info

| Item | Plan |
|---|---|
| Endpoint ID | TT-06 |
| Endpoint Name | Video Info |
| Candidate Business Purpose | Verify P0 video identity, public metadata, and metric snapshot semantics. |
| Candidate Signal Layer | L2 content performance. |
| Prerequisites | Public video ID or URL. |
| Seed Data Source | TT-16 Search by Hashtag, TT-17 Search by Keyword, TT-05 Profile Videos. |
| Inputs To Verify | Video ID versus URL, batch support if any. |
| Positive Test Cases | Fetch known public video and repeat later for metric changes. |
| Negative Test Cases | Invalid video, deleted video, inaccessible video. |
| Edge Cases | No caption, no metrics, very old video, new video. |
| Pagination Cases | Verify single-object behavior or pagination absence. |
| Identity Fields To Verify | Platform video ID, author ID, source URL. |
| Time Fields To Verify | Published time, collected time, metric snapshot time if present. |
| Metric Fields To Verify | View, like, comment, share, duration if returned. |
| Missingness Cases | Null metrics, zero metrics, missing caption. |
| Market / Language Cases | Video language and author region if exposed. |
| Cost / Quota Cases | Record per-video or per-request cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw response, redacted response, field observations. |
| Business Interpretation Risks | Public metrics cannot prove conversion or creative causality. |
| Adoption Criteria | Stable video identity and interpretable metric snapshot. |
| Rejection Criteria | Missing stable ID or unknown metric meaning. |
| Current Status | Not Run |
| Open Questions | Does response include true metric snapshot timestamp? |

### TT-07 Transcript

| Item | Plan |
|---|---|
| Endpoint ID | TT-07 |
| Endpoint Name | Transcript |
| Candidate Business Purpose | Determine transcript availability for classification support. |
| Candidate Signal Layer | L1 content expression. |
| Prerequisites | Public video ID with and without transcript. |
| Seed Data Source | TT-06 Video Info. |
| Inputs To Verify | Video ID, language options if present. |
| Positive Test Cases | Fetch transcript for a known transcript-available video. |
| Negative Test Cases | Video with no transcript, invalid video, restricted video. |
| Edge Cases | Auto captions, multilingual captions, partial transcript. |
| Pagination Cases | Verify segment pagination or single response. |
| Identity Fields To Verify | Video ID, transcript segment identity if any. |
| Time Fields To Verify | Segment timestamps and transcript generation time if present. |
| Metric Fields To Verify | None expected unless returned. |
| Missingness Cases | Transcript unavailable, empty transcript, null segments. |
| Market / Language Cases | Transcript language and translation behavior. |
| Cost / Quota Cases | Record per-transcript cost and limits. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw transcript response, redacted copy. |
| Business Interpretation Risks | Missing transcript does not mean irrelevant video. |
| Adoption Criteria | Clear availability rules and stable text/segment structure. |
| Rejection Criteria | Unreliable or opaque transcript extraction. |
| Current Status | Not Run |
| Open Questions | Are transcripts official, generated, translated, or inferred? |

### TT-08 Live

| Item | Plan |
|---|---|
| Endpoint ID | TT-08 |
| Endpoint Name | Live |
| Candidate Business Purpose | Determine whether public live discovery can produce live identities or live content signals. |
| Candidate Signal Layer | L1/L2 live visibility. |
| Prerequisites | Live discovery context or public live case. |
| Seed Data Source | Manual observation, Profile, or Trending Feed. |
| Inputs To Verify | User, keyword, market, or live discovery inputs. |
| Positive Test Cases | Fetch live result if a legal live case exists. |
| Negative Test Cases | No active live, invalid context, restricted live. |
| Edge Cases | Live ended during test, replay versus live, zero results. |
| Pagination Cases | Live list paging, cursor expiry, end page. |
| Identity Fields To Verify | Live ID, host user ID, live URL. |
| Time Fields To Verify | Live start time, collected time, ended time if present. |
| Metric Fields To Verify | Viewer-like public metrics only if observed. |
| Missingness Cases | Missing live ID, removed live, inaccessible replay. |
| Market / Language Cases | Market and language controls if supported. |
| Cost / Quota Cases | Record cost and volatility. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw live response, redacted response. |
| Business Interpretation Risks | Live visibility does not prove sales. |
| Adoption Criteria | Stable live identity and low-risk access. |
| Rejection Criteria | No usable public live data or unsafe testing. |
| Current Status | Not Run |
| Open Questions | Does endpoint discover live sessions or require a known live ID? |

### TT-09 Live Info

| Item | Plan |
|---|---|
| Endpoint ID | TT-09 |
| Endpoint Name | Live Info |
| Candidate Business Purpose | Inspect public metadata for a known live identity. |
| Candidate Signal Layer | L1/L2 live visibility. |
| Prerequisites | Live ID from TT-08 or manual public live case. |
| Seed Data Source | TT-08 Live. |
| Inputs To Verify | Live ID, host ID, URL handling. |
| Positive Test Cases | Fetch info for active or recently active live if allowed. |
| Negative Test Cases | Invalid live ID, ended live, inaccessible live. |
| Edge Cases | Live status changes between requests. |
| Pagination Cases | Verify single-object behavior or sub-resource pagination. |
| Identity Fields To Verify | Live ID, host user ID, source URL. |
| Time Fields To Verify | Start, end, update, collection times. |
| Metric Fields To Verify | Viewer or engagement metrics if returned. |
| Missingness Cases | Missing status, missing host, unavailable metrics. |
| Market / Language Cases | Host region and language if exposed. |
| Cost / Quota Cases | Record per-live lookup cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw response, redacted response. |
| Business Interpretation Risks | Live metrics are volatile and not conversion proof. |
| Adoption Criteria | Clear identity, status, and timestamp semantics. |
| Rejection Criteria | No stable live identity or unsafe volatility. |
| Current Status | Not Run |
| Open Questions | How are active and ended lives represented? |

### TT-10 Comments

| Item | Plan |
|---|---|
| Endpoint ID | TT-10 |
| Endpoint Name | Comments |
| Candidate Business Purpose | Capture public viewer questions, objections, and comment availability limits. |
| Candidate Signal Layer | L1/L2 public feedback. |
| Prerequisites | Public video with comments and another with restricted comments. |
| Seed Data Source | TT-06 Video Info. |
| Inputs To Verify | Video ID, sorting, pagination, count limit. |
| Positive Test Cases | Fetch comments for a public video with comments. |
| Negative Test Cases | Invalid video, comments disabled, inaccessible video. |
| Edge Cases | Deleted comments, pinned comments, emoji-only comments. |
| Pagination Cases | First page, next page, end page, repeated cursor. |
| Identity Fields To Verify | Comment ID, video ID, author ID. |
| Time Fields To Verify | Comment publish time and collected time. |
| Metric Fields To Verify | Comment like/reply counts if returned. |
| Missingness Cases | Null text, hidden author, missing reply count. |
| Market / Language Cases | Comment language and mixed-language results. |
| Cost / Quota Cases | Record per-page cost and limits. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw comments, redacted comments. |
| Business Interpretation Risks | Comments are not representative buyer research. |
| Adoption Criteria | Stable comment identity and pagination. |
| Rejection Criteria | No accessible comment text or identity. |
| Current Status | Not Run |
| Open Questions | Are comments sorted by recency, relevance, or popularity? |

### TT-11 Comment Replies

| Item | Plan |
|---|---|
| Endpoint ID | TT-11 |
| Endpoint Name | Comment Replies |
| Candidate Business Purpose | Observe public discussion threads under comments. |
| Candidate Signal Layer | L1/L2 public feedback. |
| Prerequisites | Comment ID with replies. |
| Seed Data Source | TT-10 Comments. |
| Inputs To Verify | Comment ID, video ID requirement, pagination. |
| Positive Test Cases | Fetch replies for a comment known to have replies. |
| Negative Test Cases | Comment with no replies, invalid comment, deleted comment. |
| Edge Cases | Nested replies, hidden author, removed parent. |
| Pagination Cases | Reply cursor, end page, cursor failure. |
| Identity Fields To Verify | Reply ID, parent comment ID, video ID, author ID. |
| Time Fields To Verify | Reply publish time and collected time. |
| Metric Fields To Verify | Reply likes if returned. |
| Missingness Cases | Missing parent, null text, hidden user. |
| Market / Language Cases | Reply language and mixed-language threads. |
| Cost / Quota Cases | Record per-thread cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw replies, redacted replies. |
| Business Interpretation Risks | Threads can overrepresent disputes or jokes. |
| Adoption Criteria | Stable parent-child linkage. |
| Rejection Criteria | Cannot link replies to parent comment. |
| Current Status | Not Run |
| Open Questions | Does endpoint require video ID plus comment ID? |

### TT-12 Following

| Item | Plan |
|---|---|
| Endpoint ID | TT-12 |
| Endpoint Name | Following |
| Candidate Business Purpose | Check whether public following relationships can be observed for ecosystem context. |
| Candidate Signal Layer | L1 creator relationship visibility. |
| Prerequisites | Public user with visible following list. |
| Seed Data Source | TT-01 Profile. |
| Inputs To Verify | User ID, pagination, privacy behavior. |
| Positive Test Cases | Fetch following list for public profile if visible. |
| Negative Test Cases | Private list, invalid user, no following. |
| Edge Cases | Hidden relationships, deleted users, duplicates. |
| Pagination Cases | Following pages, max count, end page. |
| Identity Fields To Verify | Source user ID, followed user IDs. |
| Time Fields To Verify | Collection time; relationship timestamp if present. |
| Metric Fields To Verify | None expected unless returned. |
| Missingness Cases | Hidden handles, null profile fields. |
| Market / Language Cases | Relationship graph does not define market. |
| Cost / Quota Cases | Record per-page cost and plan gating. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw relationship page, redacted copy. |
| Business Interpretation Risks | Following does not prove commercial partnership. |
| Adoption Criteria | Stable relationship IDs and safe access. |
| Rejection Criteria | Unavailable or privacy-risk data. |
| Current Status | Not Run |
| Open Questions | Is the returned list complete or sampled? |

### TT-13 Followers

| Item | Plan |
|---|---|
| Endpoint ID | TT-13 |
| Endpoint Name | Followers |
| Candidate Business Purpose | Check whether public follower relationships are observable and useful for ecosystem context. |
| Candidate Signal Layer | L1 creator relationship visibility. |
| Prerequisites | Public user with visible followers. |
| Seed Data Source | TT-01 Profile. |
| Inputs To Verify | User ID, pagination, privacy behavior. |
| Positive Test Cases | Fetch follower page for public profile if allowed. |
| Negative Test Cases | Private list, invalid user, no visible followers. |
| Edge Cases | Large account, sampled list, hidden profiles. |
| Pagination Cases | Follower pages, cursor expiry, hard cap. |
| Identity Fields To Verify | Target user ID, follower user IDs. |
| Time Fields To Verify | Collection time; follower timestamp if present. |
| Metric Fields To Verify | Follower counts if returned. |
| Missingness Cases | Hidden follower profile fields. |
| Market / Language Cases | Followers are not buyers or target market. |
| Cost / Quota Cases | Record per-page cost and restrictions. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw follower page, redacted copy. |
| Business Interpretation Risks | Follower visibility cannot prove demographics or purchase. |
| Adoption Criteria | Stable IDs and clear completeness limits. |
| Rejection Criteria | Opaque sampling or privacy constraints. |
| Current Status | Not Run |
| Open Questions | Are followers complete, sampled, or unavailable? |

### TT-14 Search Users

| Item | Plan |
|---|---|
| Endpoint ID | TT-14 |
| Endpoint Name | Search Users |
| Candidate Business Purpose | Discover creator accounts related to a query for ecosystem research. |
| Candidate Signal Layer | L1 search and creator visibility. |
| Prerequisites | Query text. |
| Seed Data Source | car vacuum / portable car vacuum context. |
| Inputs To Verify | Query, market, language, limit, pagination. |
| Positive Test Cases | Search product-adjacent creator query. |
| Negative Test Cases | Empty query, nonsense query, restricted query if safe. |
| Edge Cases | Duplicate accounts, brand accounts, unrelated celebrities. |
| Pagination Cases | First page, next page, ranking stability. |
| Identity Fields To Verify | User ID, handle, profile URL. |
| Time Fields To Verify | Collection time; profile freshness if present. |
| Metric Fields To Verify | Public profile metrics if returned. |
| Missingness Cases | Missing handle, missing counts. |
| Market / Language Cases | Verify locale effect if supported. |
| Cost / Quota Cases | Record per-search cost and limits. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw search response, redacted response. |
| Business Interpretation Risks | Search rank is not creator relevance proof. |
| Adoption Criteria | Useful creator seeds with clear ranking limits. |
| Rejection Criteria | No stable user identity or uncontrollable personalization. |
| Current Status | Not Run |
| Open Questions | What ranking does user search use? |

### TT-15 Search Suggestions

| Item | Plan |
|---|---|
| Endpoint ID | TT-15 |
| Endpoint Name | Search Suggestions |
| Candidate Business Purpose | Observe query-expansion language for future SIG-P1 research. |
| Candidate Signal Layer | L1 search expression visibility. |
| Prerequisites | Query prefix or seed term. |
| Seed Data Source | car vacuum, car cleaning, pet hair car contexts. |
| Inputs To Verify | Prefix, locale, market, language if supported. |
| Positive Test Cases | Fetch suggestions for product and scenario prefixes. |
| Negative Test Cases | Empty prefix, rare prefix, invalid characters if safe. |
| Edge Cases | Brand terms, adult/risky terms avoided, multilingual suggestions. |
| Pagination Cases | Verify whether suggestions are limited or paginated. |
| Identity Fields To Verify | Suggestion text identity; no video identity expected. |
| Time Fields To Verify | Collection time and freshness if present. |
| Metric Fields To Verify | Suggestion rank or volume only if observed. |
| Missingness Cases | No suggestions, null suggestion list. |
| Market / Language Cases | Verify locale and language effects. |
| Cost / Quota Cases | Record per-query cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw suggestions, redacted response. |
| Business Interpretation Risks | Suggestions do not prove purchase intent. |
| Adoption Criteria | Clear suggestion list and localization semantics. |
| Rejection Criteria | Personalized or opaque output without stable use. |
| Current Status | Not Run |
| Open Questions | Are suggestions personalized, global, or market-specific? |

### TT-16 Search by Hashtag

| Item | Plan |
|---|---|
| Endpoint ID | TT-16 |
| Endpoint Name | Search by Hashtag |
| Candidate Business Purpose | Collect P0 candidate videos from hashtag context. |
| Candidate Signal Layer | L1/L2 public video supply and performance. |
| Prerequisites | Public hashtag candidate. |
| Seed Data Source | Manual hashtag research from car cleaning context. |
| Inputs To Verify | Hashtag text or ID, market, language, limit, pagination. |
| Positive Test Cases | Search relevant public hashtag and save all returned videos. |
| Negative Test Cases | Empty hashtag, nonexistent hashtag, invalid format. |
| Edge Cases | Broad hashtag, ambiguous hashtag, spam-heavy results. |
| Pagination Cases | First page, next page, end page, hard cap. |
| Identity Fields To Verify | Hashtag identity, video ID, author ID, source URL. |
| Time Fields To Verify | Published time, collected time, metric snapshot if present. |
| Metric Fields To Verify | Video public metrics if returned. |
| Missingness Cases | Missing captions, missing metrics, duplicate videos. |
| Market / Language Cases | Verify whether region/language controls apply. |
| Cost / Quota Cases | Record per-page and per-query cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw search pages, redacted pages. |
| Business Interpretation Risks | Hashtag use does not equal topic or user intent. |
| Adoption Criteria | Stable video IDs, usable pagination, useful sample quality. |
| Rejection Criteria | No stable IDs or unusable noisy output. |
| Current Status | Not Run |
| Open Questions | Is hashtag ranking recency, popularity, or relevance? |

### TT-17 Search by Keyword

| Item | Plan |
|---|---|
| Endpoint ID | TT-17 |
| Endpoint Name | Search by Keyword |
| Candidate Business Purpose | Collect P0 candidate videos from product, scenario, and pain point queries. |
| Candidate Signal Layer | L1/L2 public video supply and performance. |
| Prerequisites | Query text. |
| Seed Data Source | car vacuum, portable car vacuum, car cleaning, seat gap cleaning, pet hair car. |
| Inputs To Verify | Query, market, language, limit, pagination, sort if present. |
| Positive Test Cases | Run product and scenario queries and preserve query execution records. |
| Negative Test Cases | Empty query, no-result query, invalid characters if safe. |
| Edge Cases | Query overlap, unrelated results, duplicate videos. |
| Pagination Cases | First page, next page, end page, cursor expiry. |
| Identity Fields To Verify | Query execution ID, video ID, author ID, source URL. |
| Time Fields To Verify | Published time, collected time, metric snapshot if present. |
| Metric Fields To Verify | Video metrics if returned. |
| Missingness Cases | Missing captions, missing metrics, null author fields. |
| Market / Language Cases | Verify market and language effect. |
| Cost / Quota Cases | Record per-query and per-page cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw search pages, redacted pages. |
| Business Interpretation Risks | Search result sample does not represent total market size. |
| Adoption Criteria | Stable video IDs and clear ranking/pagination limits. |
| Rejection Criteria | No usable IDs, opaque failures, or unsafe access. |
| Current Status | Not Run |
| Open Questions | How does keyword ranking behave? |

### TT-18 Top Search

| Item | Plan |
|---|---|
| Endpoint ID | TT-18 |
| Endpoint Name | Top Search |
| Candidate Business Purpose | Determine whether top search output can support future query trend observation. |
| Candidate Signal Layer | L1 search visibility. |
| Prerequisites | Market, category, or query context if required. |
| Seed Data Source | Product context and manual test inputs. |
| Inputs To Verify | Market, category, query, time window if present. |
| Positive Test Cases | Fetch top search data for relevant context. |
| Negative Test Cases | Unsupported market, empty context, invalid category if safe. |
| Edge Cases | Rapidly changing output, generic terms, unrelated trends. |
| Pagination Cases | Verify list limit, paging, and hard cap. |
| Identity Fields To Verify | Search term identity or result IDs if returned. |
| Time Fields To Verify | Time window, collection time, trend freshness. |
| Metric Fields To Verify | Rank or volume only if observed. |
| Missingness Cases | Missing rank, missing volume, empty list. |
| Market / Language Cases | Market and locale are central to this endpoint. |
| Cost / Quota Cases | Record per-request cost and plan gates. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw top search response, redacted response. |
| Business Interpretation Risks | Top search does not prove purchase or conversion. |
| Adoption Criteria | Clear time/market semantics and stable term fields. |
| Rejection Criteria | Unclear personalization or no interpretable scope. |
| Current Status | Not Run |
| Open Questions | What does "top" mean and over which time window? |

### TT-19 Get popular creators

| Item | Plan |
|---|---|
| Endpoint ID | TT-19 |
| Endpoint Name | Get popular creators |
| Candidate Business Purpose | Discover creators for future ecosystem mapping. |
| Candidate Signal Layer | L1/L2 creator visibility. |
| Prerequisites | Category, market, or discovery context if required. |
| Seed Data Source | Product category hypotheses or manual category tests. |
| Inputs To Verify | Category, market, language, limit, pagination. |
| Positive Test Cases | Fetch popular creators for a relevant category if supported. |
| Negative Test Cases | Unsupported category, unsupported market, invalid input. |
| Edge Cases | Creators unrelated to product, brand accounts, large accounts only. |
| Pagination Cases | Page through creator list and record hard caps. |
| Identity Fields To Verify | User ID, handle, profile URL. |
| Time Fields To Verify | Ranking snapshot time or collection time. |
| Metric Fields To Verify | Popularity metrics only if returned and defined. |
| Missingness Cases | Missing category, missing profile metrics. |
| Market / Language Cases | Verify market and language filtering. |
| Cost / Quota Cases | Record per-page cost and plan access. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw creators response, redacted response. |
| Business Interpretation Risks | Popular creators may not be relevant to product demand. |
| Adoption Criteria | Clear discovery scope and stable creator IDs. |
| Rejection Criteria | Opaque popularity or irrelevant results. |
| Current Status | Not Run |
| Open Questions | What popularity criteria are used? |

### TT-20 Get Song Details

| Item | Plan |
|---|---|
| Endpoint ID | TT-20 |
| Endpoint Name | Get Song Details |
| Candidate Business Purpose | Verify sound identity and metadata for song-linked video collection. |
| Candidate Signal Layer | L1 sound visibility. |
| Prerequisites | Song or sound ID. |
| Seed Data Source | Video Info, TikToks using Song, manual public sound URL. |
| Inputs To Verify | Song ID or URL. |
| Positive Test Cases | Fetch metadata for a public song used by a known video. |
| Negative Test Cases | Invalid song, removed sound, unavailable region. |
| Edge Cases | Original sound, commercial sound, renamed sound. |
| Pagination Cases | Verify single-object behavior. |
| Identity Fields To Verify | Song ID, sound URL, creator if present. |
| Time Fields To Verify | Created time or collection time if present. |
| Metric Fields To Verify | Usage count only if returned and defined. |
| Missingness Cases | Missing title, missing creator, unavailable sound. |
| Market / Language Cases | Regional sound availability if exposed. |
| Cost / Quota Cases | Record per-song lookup cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw song response, redacted response. |
| Business Interpretation Risks | Sound popularity does not prove product demand. |
| Adoption Criteria | Stable song identity and useful metadata. |
| Rejection Criteria | No stable ID or inaccessible sound data. |
| Current Status | Not Run |
| Open Questions | Are original sounds and catalog songs represented differently? |

### TT-21 TikToks using Song

| Item | Plan |
|---|---|
| Endpoint ID | TT-21 |
| Endpoint Name | TikToks using Song |
| Candidate Business Purpose | Collect videos associated with a sound for future content ecosystem analysis. |
| Candidate Signal Layer | L1/L2 sound-video visibility. |
| Prerequisites | Song ID. |
| Seed Data Source | TT-20 Get Song Details or Video Info sound fields. |
| Inputs To Verify | Song ID, pagination, market/language if present. |
| Positive Test Cases | Fetch videos using a public song. |
| Negative Test Cases | Invalid song, song with no videos, restricted sound. |
| Edge Cases | Viral non-product sound, duplicates, unrelated videos. |
| Pagination Cases | First page, next page, end page, max count. |
| Identity Fields To Verify | Song ID, video ID, author ID, source URL. |
| Time Fields To Verify | Video publish time, collection time. |
| Metric Fields To Verify | Video metrics if returned. |
| Missingness Cases | Missing captions, missing sound link, removed videos. |
| Market / Language Cases | Verify whether market filters sound videos. |
| Cost / Quota Cases | Record per-page cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw video pages, redacted pages. |
| Business Interpretation Risks | Shared sound does not imply shared intent. |
| Adoption Criteria | Stable song-video linkage and pagination. |
| Rejection Criteria | No stable linkage or excessive noise. |
| Current Status | Not Run |
| Open Questions | Does endpoint return all videos or ranked subset? |

### TT-22 Trending Feed

| Item | Plan |
|---|---|
| Endpoint ID | TT-22 |
| Endpoint Name | Trending Feed |
| Candidate Business Purpose | Observe trend-feed availability and personalization risk. |
| Candidate Signal Layer | L1/L2 trend visibility. |
| Prerequisites | Market or feed context if required. |
| Seed Data Source | Manual test context. |
| Inputs To Verify | Market, language, category, pagination, personalization controls. |
| Positive Test Cases | Fetch a trend feed sample under a documented context. |
| Negative Test Cases | Unsupported market, invalid category, no feed context. |
| Edge Cases | Personalized results, repeated request differences, irrelevant trends. |
| Pagination Cases | Feed pages, repeated page, cursor expiry. |
| Identity Fields To Verify | Feed item video ID, author ID, source URL. |
| Time Fields To Verify | Collection time, video publish time, trend freshness. |
| Metric Fields To Verify | Video metrics if returned. |
| Missingness Cases | Missing rank, missing metrics, removed videos. |
| Market / Language Cases | Central test dimension; verify actual effect. |
| Cost / Quota Cases | Record feed request cost and limits. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw feed pages, redacted pages. |
| Business Interpretation Risks | Trending feed may be personalized or volatile. |
| Adoption Criteria | Clear scope and stable enough interpretation. |
| Rejection Criteria | Personalization prevents business use. |
| Current Status | Not Run |
| Open Questions | Is feed global, market-specific, or account-personalized? |

### SHOP-01 Shop Search

| Item | Plan |
|---|---|
| Endpoint ID | SHOP-01 |
| Endpoint Name | Shop Search |
| Candidate Business Purpose | Discover public shops for Commercial Visibility / L3-adjacent analysis. |
| Candidate Signal Layer | Commercial Visibility / L3-adjacent. |
| Prerequisites | Shop query. |
| Seed Data Source | car vacuum / car cleaning commerce context. |
| Inputs To Verify | Query, market, language, pagination. |
| Positive Test Cases | Search relevant public shop context. |
| Negative Test Cases | Empty query, no-result query, unsupported market. |
| Edge Cases | Similar shop names, unrelated shops, unavailable shops. |
| Pagination Cases | First page, next page, end page, hard cap. |
| Identity Fields To Verify | Shop ID, shop URL, seller identity if present. |
| Time Fields To Verify | Collection time and update time if present. |
| Metric Fields To Verify | Shop metrics only if returned and defined. |
| Missingness Cases | Missing shop details, hidden metrics. |
| Market / Language Cases | Verify market-specific shop visibility. |
| Cost / Quota Cases | Record per-search cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw shop search pages, redacted pages. |
| Business Interpretation Risks | Public shop visibility does not prove sales. |
| Adoption Criteria | Stable shop IDs and clear market scope. |
| Rejection Criteria | No stable identity or ambiguous market. |
| Current Status | Not Run |
| Open Questions | Does ranking reflect relevance, popularity, or ads? |

### SHOP-02 Shop Products

| Item | Plan |
|---|---|
| Endpoint ID | SHOP-02 |
| Endpoint Name | Shop Products |
| Candidate Business Purpose | List public products under a shop. |
| Candidate Signal Layer | Commercial Visibility / L3-adjacent. |
| Prerequisites | Shop ID. |
| Seed Data Source | SHOP-01 Shop Search. |
| Inputs To Verify | Shop ID, pagination, product count limit. |
| Positive Test Cases | Fetch products for a public shop. |
| Negative Test Cases | Invalid shop, shop with no products, inaccessible shop. |
| Edge Cases | Out-of-stock products, duplicate listings, variants. |
| Pagination Cases | Product pages, end page, maximum count. |
| Identity Fields To Verify | Shop ID, product IDs, product URLs. |
| Time Fields To Verify | Product update time if present, collection time. |
| Metric Fields To Verify | Public product metrics only if returned. |
| Missingness Cases | Missing price, missing title, hidden product. |
| Market / Language Cases | Verify market and language effects. |
| Cost / Quota Cases | Record per-page cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw product pages, redacted pages. |
| Business Interpretation Risks | Product listing is not transaction proof. |
| Adoption Criteria | Stable shop-product linkage. |
| Rejection Criteria | No stable product IDs or unavailable data. |
| Current Status | Not Run |
| Open Questions | Are variants separate products or nested fields? |

### SHOP-03 Product Details

| Item | Plan |
|---|---|
| Endpoint ID | SHOP-03 |
| Endpoint Name | Product Details |
| Candidate Business Purpose | Inspect public product detail fields and limits. |
| Candidate Signal Layer | Commercial Visibility / L3-adjacent. |
| Prerequisites | Product ID. |
| Seed Data Source | SHOP-02 Shop Products or public product URL. |
| Inputs To Verify | Product ID or URL, market if required. |
| Positive Test Cases | Fetch details for a public product. |
| Negative Test Cases | Invalid product, unavailable product, unsupported market. |
| Edge Cases | Variants, missing price, unavailable product. |
| Pagination Cases | Verify single-object behavior or nested pages. |
| Identity Fields To Verify | Product ID, shop ID, product URL. |
| Time Fields To Verify | Update time, collection time, availability timestamp if present. |
| Metric Fields To Verify | Public sales/rating-like metrics only if verified. |
| Missingness Cases | Missing specs, null price, absent image list. |
| Market / Language Cases | Verify localized product fields. |
| Cost / Quota Cases | Record per-product cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw product response, redacted response. |
| Business Interpretation Risks | Does not replace Andy's ProductBrief facts. |
| Adoption Criteria | Stable product identity and safe field semantics. |
| Rejection Criteria | Unclear identity or unsafe commercial overclaim risk. |
| Current Status | Not Run |
| Open Questions | Which fields are public visibility versus conversion metrics? |

### SHOP-04 Product Reviews

| Item | Plan |
|---|---|
| Endpoint ID | SHOP-04 |
| Endpoint Name | Product Reviews |
| Candidate Business Purpose | Observe public product review themes and review-field limits. |
| Candidate Signal Layer | Commercial Visibility / L3-adjacent. |
| Prerequisites | Product ID with reviews. |
| Seed Data Source | SHOP-03 Product Details. |
| Inputs To Verify | Product ID, pagination, rating filters if present. |
| Positive Test Cases | Fetch reviews for product known to have reviews. |
| Negative Test Cases | Product with no reviews, invalid product, unavailable product. |
| Edge Cases | Empty text review, image review, translated review. |
| Pagination Cases | Review pages, end page, hard cap. |
| Identity Fields To Verify | Review ID, product ID, reviewer identity if exposed. |
| Time Fields To Verify | Review time and collection time. |
| Metric Fields To Verify | Rating, helpful count only if returned. |
| Missingness Cases | Missing text, hidden reviewer, null rating. |
| Market / Language Cases | Review language and market context. |
| Cost / Quota Cases | Record per-page cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw reviews, redacted reviews. |
| Business Interpretation Risks | Reviews are not full buyer population. |
| Adoption Criteria | Stable review IDs and interpretable text/rating fields. |
| Rejection Criteria | No review identity or inaccessible review text. |
| Current Status | Not Run |
| Open Questions | Are reviews filtered, sampled, or complete? |

### SHOP-05 User Showcase

| Item | Plan |
|---|---|
| Endpoint ID | SHOP-05 |
| Endpoint Name | User Showcase |
| Candidate Business Purpose | Observe public creator-product showcase relationships. |
| Candidate Signal Layer | Commercial Visibility / L3-adjacent. |
| Prerequisites | User or showcase identity. |
| Seed Data Source | Profile, Product Details, or public showcase URL. |
| Inputs To Verify | User ID, product ID, showcase ID, pagination. |
| Positive Test Cases | Fetch showcase for a public user with visible products. |
| Negative Test Cases | User without showcase, invalid user, restricted showcase. |
| Edge Cases | Removed products, duplicate products, regional products. |
| Pagination Cases | Showcase pages, end page, hard cap. |
| Identity Fields To Verify | User ID, product ID, shop ID, showcase URL. |
| Time Fields To Verify | Collection time and update time if present. |
| Metric Fields To Verify | Showcase metrics only if returned and defined. |
| Missingness Cases | Missing product details, hidden shop, unavailable product. |
| Market / Language Cases | Verify product market visibility. |
| Cost / Quota Cases | Record per-page cost and plan gates. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw showcase response, redacted response. |
| Business Interpretation Risks | Showcase presence does not prove clicks, add-to-cart, or sales. |
| Adoption Criteria | Stable creator-product linkage. |
| Rejection Criteria | No stable link or unclear public visibility scope. |
| Current Status | Not Run |
| Open Questions | Does showcase include current or historical products? |

### AD-01 Ad Library Search

| Item | Plan |
|---|---|
| Endpoint ID | AD-01 |
| Endpoint Name | Ad Library Search |
| Candidate Business Purpose | Search public ad materials for future ad expression hypotheses. |
| Candidate Signal Layer | L1/L2 public ad visibility. |
| Prerequisites | Ad query or advertiser context. |
| Seed Data Source | product and category query terms. |
| Inputs To Verify | Query, market, date range, advertiser, pagination if present. |
| Positive Test Cases | Search for public ads in relevant product context. |
| Negative Test Cases | Empty query, no-result query, unsupported market. |
| Edge Cases | Brand ads, irrelevant ads, expired ads. |
| Pagination Cases | Search pages, end page, max count. |
| Identity Fields To Verify | Ad ID, advertiser ID, creative URL if present. |
| Time Fields To Verify | Ad start/end, collection time, status time. |
| Metric Fields To Verify | Public ad metrics only if returned and defined. |
| Missingness Cases | Missing advertiser, missing creative, unavailable ad. |
| Market / Language Cases | Verify market and language filters. |
| Cost / Quota Cases | Record per-search cost and access limits. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw ad search pages, redacted pages. |
| Business Interpretation Risks | Public ad visibility does not prove spend or sales attribution. |
| Adoption Criteria | Stable ad IDs and clear public visibility semantics. |
| Rejection Criteria | No stable ad identity or opaque search scope. |
| Current Status | Not Run |
| Open Questions | What does ad library ranking represent? |

### AD-02 Ad Library Ad

| Item | Plan |
|---|---|
| Endpoint ID | AD-02 |
| Endpoint Name | Ad Library Ad |
| Candidate Business Purpose | Retrieve detail for a known public ad material. |
| Candidate Signal Layer | L1/L2 public ad visibility. |
| Prerequisites | Ad ID. |
| Seed Data Source | AD-01 Ad Library Search. |
| Inputs To Verify | Ad ID, market if required. |
| Positive Test Cases | Fetch detail for a known public ad. |
| Negative Test Cases | Invalid ad ID, removed ad, inaccessible market. |
| Edge Cases | Multiple creatives, inactive ad, missing advertiser. |
| Pagination Cases | Verify single-object behavior or nested creative pages. |
| Identity Fields To Verify | Ad ID, advertiser ID, creative IDs or URLs. |
| Time Fields To Verify | Ad run dates, status update time, collection time. |
| Metric Fields To Verify | Public ad metrics only if returned and defined. |
| Missingness Cases | Missing creative, missing landing data, unavailable media. |
| Market / Language Cases | Verify market-specific ad visibility. |
| Cost / Quota Cases | Record per-ad lookup cost. |
| Raw Artifacts Expected | Canonical redacted request evidence, raw ad detail, redacted response. |
| Business Interpretation Risks | Ad detail does not prove spend, clicks, conversion, or GMV. |
| Adoption Criteria | Stable ad identity and interpretable public fields. |
| Rejection Criteria | Unstable identity or no useful public detail. |
| Current Status | Not Run |
| Open Questions | Which ad fields are public metadata versus performance metrics? |
