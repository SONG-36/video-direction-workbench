# Scrape Creators Request Surface Baseline

- Version: V0.1
- Status: Draft
- Authority: Observed Request Evidence Baseline
- Scope: Observed request-side API routes, UI descriptions, parameter surfaces, required markers, enums, explicit cost notes, and unresolved runtime questions for all 29 currently observed Scrape Creators endpoints.
- Evidence Date: 2026-08-07
- Evidence Source: Andy's direct observation of Scrape Creators API Playground UI plus manually transcribed redacted curl routes.
- Depends On:
  - 02_DATA_SOURCE_CAPABILITY_MAP.md
  - 04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md
  - 05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md
  - 06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Pending Andy Review

## Purpose And Boundary

This document records UI and curl request-surface observations from the Scrape Creators API Playground.

It is not:

- response contract
- runtime verification
- official provider documentation
- formal SIG-P0 schema
- implementation code

Runtime reconnaissance may supersede or refine this observed request-side baseline, but discrepancies must be recorded as provider-surface changes or runtime discrepancies rather than silently rewriting the evidence history.

## Global Observed Request-Side Facts

| Field | Observed Value |
|---|---|
| Provider | Scrape Creators |
| Observed API Families | TikTok; TikTok Shop; TikTok Ad Library |
| Observed endpoint count | 29 |
| Base Host | `https://api.scrapecreators.com` |
| Observed request method | GET |
| Method evidence | User-provided 29 curl routes did not specify another HTTP method; curl default behavior is GET. |
| Method verification status | Observed From Provided Curl Surface |
| Auth Pattern | Header: `x-api-key: <redacted>` |
| Real API key handling | The real API key is intentionally excluded from this baseline and must never enter Git documentation. |
| Credit System observation | Scrape Creators UI shows API requests consume shared credits and all API keys share the same credit balance. |
| Observed available credits at collection time | 24,343 credits |
| Credit snapshot boundary | This is a 2026-08-07 UI-time observation, not a permanent account balance. |

## API Version Distribution

### v3

| endpoint_id | endpoint_name | path |
|---|---|---|
| TT-05 | Profile Videos | `/v3/tiktok/profile/videos` |

### v2

| endpoint_id | endpoint_name | path |
|---|---|---|
| TT-06 | Video Info | `/v2/tiktok/video` |

### v1

The remaining 27 currently observed endpoints use `/v1/...` paths in the supplied request surface evidence.

Do not build the future adapter by assuming every TikTok endpoint lives under `/v1/tiktok/`. Future implementation must use the full observed endpoint path as provider request-contract evidence. Do not normalize or collapse provider API versions.

## Endpoint Record Structure

Each endpoint below uses the same record structure:

- API Family
- Observed Description
- HTTP Method
- API Version
- Endpoint Path
- Auth Pattern
- Observed UI Parameters
- Observed Required Markers
- Observed Enum Values
- Observed UI Example Values / Type Hints
- Explicit Provider Notes
- Explicit Credit Observation
- Candidate Prerequisite Entity
- Request Surface Verification Status
- Runtime Verification Status
- Response Verification Status
- Known Interpretation Boundary
- Runtime Questions To Verify
- Canonical Redacted Request Surface

Observed Required Markers only records parameters with a visible `*` in the supplied UI evidence. If no `*` was observed, this document says no required marker was observed. That does not mean the parameter is verified optional.

Observed Enum Values only records values captured in supplied evidence. If a selector was visible but not fully captured, the endpoint is marked as partial observed enum with full provider-supported enum still runtime/documentation unknown.

Canonical Redacted Request Surface examples are request-surface templates, not runtime-validated legal parameter combinations. They do not include a real API key and do not claim successful execution.

## TT-01 Profile

- API Family: TikTok
- Observed Description: Scrapes a public TikTok profile.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/profile`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - handle
  - user_id
  - cache_max_age
- Observed Required Markers:
  - No required marker observed for handle/user_id in supplied evidence.
- Observed Enum Values:
  - cache_max_age: `1d`, `3d`, `7d`, `14d`, `30d`
- Observed UI Example Values / Type Hints:
  - handle: string username-like
  - user_id: numeric-like string ID
  - cache_max_age: bounded enum
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: public user
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Creator profile cannot prove buyer demographics or sales.
- Runtime Questions To Verify:
  - handle and user_id whether either/or
  - whether both can be provided together
  - which identity field has priority
  - cache behavior
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/profile?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-02 Profile Region

- API Family: TikTok
- Observed Description: Gets the region/country code for a TikTok profile.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/profile/region`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - handle
- Observed Required Markers:
  - handle
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - handle: string username-like
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: public user
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Creator profile region does not equal audience market or buyer market.
- Runtime Questions To Verify:
  - region field source
  - profile identity linkage
  - missing region behavior
  - whether region is platform-declared, inferred, or provider-derived
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/profile/region?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-03 User's Audience Demographics

- API Family: TikTok
- Observed Description: Get the audience demographics of a TikTok user. Right now you can only get the audience countries.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/user/audience`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - handle
- Observed Required Markers:
  - handle
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - handle: string username-like
- Explicit Provider Notes:
  - Right now only audience countries are available.
- Explicit Credit Observation: 26 credits/request, Observed From UI
- Candidate Prerequisite Entity: public creator account
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Must not be interpreted as true buying audience, actual product buyers, or `ResearchTask.primary_audience`.
- Runtime Questions To Verify:
  - response structure
  - country percentage semantics
  - source and method
  - freshness
  - coverage
  - suppressed or missing segments
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/user/audience?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-04 Collection Videos

- API Family: TikTok
- Observed Description: Scrapes the videos in a public TikTok collection. Pass cursor to get more videos.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/collection/videos`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - url
  - cursor
- Observed Required Markers:
  - url
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - url: TikTok full URL
  - cursor: numeric/string-like continuation value depending endpoint
- Explicit Provider Notes:
  - Pass cursor to get more videos.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: collection identity
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Collection membership is not market demand.
- Runtime Questions To Verify:
  - cursor type
  - cursor end state
  - collection identity
  - duplicate behavior
  - video object structure
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/collection/videos?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-05 Profile Videos

- API Family: TikTok
- Observed Description: Scrapes videos from a TikTok profile. Pass cursor to get more videos. If a profile should have videos but returns none, try `region=US` or another relevant region.
- HTTP Method: GET
- API Version: v3
- Endpoint Path: `/v3/tiktok/profile/videos`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - handle
  - user_id
  - sort_by
  - max_cursor
  - region
  - trim
- Observed Required Markers:
  - handle
- Observed Enum Values:
  - sort_by: selector observed; full enum not captured.
- Observed UI Example Values / Type Hints:
  - handle: string username-like
  - user_id: numeric-like string ID
  - sort_by: endpoint-specific enum, not fully captured
  - max_cursor: large numeric-like continuation value
  - region: country/market code-like, e.g. US / GB
  - trim: boolean checkbox
- Explicit Provider Notes:
  - Pass cursor to get more videos.
  - A profile returning no videos may require `region=US` or another relevant region.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: public user
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: High performance may reflect account size rather than content structure.
- Runtime Questions To Verify:
  - handle/user_id relationship
  - sort_by enum
  - max_cursor meaning
  - region semantics
  - trim output difference
  - pagination behavior
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v3/tiktok/profile/videos?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-06 Video Info

- API Family: TikTok
- Observed Description: Scrapes data from a TikTok video.
- HTTP Method: GET
- API Version: v2
- Endpoint Path: `/v2/tiktok/video`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - url
  - get_transcript
  - region
  - trim
  - download_media
  - cache_max_age
- Observed Required Markers:
  - url
- Observed Enum Values:
  - cache_max_age: `1d`, `3d`, `7d`, `14d`, `30d`
- Observed UI Example Values / Type Hints:
  - url: TikTok full URL
  - get_transcript: boolean checkbox
  - region: country/market code-like, e.g. US / GB
  - trim: boolean checkbox
  - download_media: boolean checkbox
  - cache_max_age: bounded enum
- Explicit Provider Notes:
  - Use `download_no_watermark_addr` when present, or `play_addr` when `has_watermark` is false.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: video URL
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Public metrics cannot prove conversion or creative causality.
- Runtime Questions To Verify:
  - video ID returned
  - author ID
  - metrics
  - published time
  - metric snapshot semantics
  - get_transcript behavior
  - download_media behavior
  - trim effect
  - region effect
  - cache behavior
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v2/tiktok/video?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-07 Transcript

- API Family: TikTok
- Observed Description: Scrapes transcript from a TikTok video.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/video/transcript`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - url
  - language
  - use_ai_as_fallback
- Observed Required Markers:
  - url
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - url: TikTok full URL
  - language: language-code-like, e.g. en
  - use_ai_as_fallback: boolean-like
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: video URL
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Missing transcript does not mean irrelevant video.
- Runtime Questions To Verify:
  - official vs generated transcript
  - AI fallback trigger
  - segment timestamps
  - multilingual behavior
  - unavailable transcript response
  - translated vs original text
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/video/transcript?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-08 Live

- API Family: TikTok
- Observed Description: Scrapes a TikTok user's live stream.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/user/live`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - handle
- Observed Required Markers:
  - handle
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - handle: string username-like
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: public user or live context
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Live visibility does not prove sales.
- Runtime Questions To Verify:
  - current live discovery or known-user lookup
  - live ID
  - zero-live behavior
  - live state
  - metrics
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/user/live?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-09 Live Info

- API Family: TikTok
- Observed Description: Gets info for a TikTok live room, including like count.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/live`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - room_id
  - user_id
- Observed Required Markers:
  - room_id
  - user_id
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - room_id: numeric-like ID
  - user_id: numeric-like string ID
- Explicit Provider Notes:
  - Response includes or concerns live-room information including like count.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: live room ID and user ID
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Live metrics are volatile and not conversion proof.
- Runtime Questions To Verify:
  - room/user ID relationship
  - viewer metrics
  - start/end/status time
  - ended-live behavior
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/live?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-10 Comments

- API Family: TikTok
- Observed Description: Scrapes comments from a TikTok video.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/video/comments`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - url
  - cursor
  - trim
- Observed Required Markers:
  - url
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - url: TikTok full URL
  - cursor: numeric/string-like continuation value depending endpoint
  - trim: boolean checkbox
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: video URL
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Comments are public feedback signals, not representative buyer research.
- Runtime Questions To Verify:
  - comment ID
  - pagination
  - sorting
  - trim
  - comments-disabled behavior
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/video/comments?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-11 Comment Replies

- API Family: TikTok
- Observed Description: Scrapes replies to a TikTok comment.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/video/comment/replies`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - comment_id
  - url
  - cursor
- Observed Required Markers:
  - comment_id
  - url
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - comment_id: numeric-like ID
  - url: TikTok full URL
  - cursor: numeric/string-like continuation value depending endpoint
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: comment ID and video URL
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Reply threads can overrepresent disputes or jokes.
- Runtime Questions To Verify:
  - whether both comment_id and url are truly required
  - parent-child identity
  - pagination
  - deleted parent behavior
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/video/comment/replies?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-12 Following

- API Family: TikTok
- Observed Description: Scrapes accounts that a TikTok user follows.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/user/following`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - handle
  - min_time
  - trim
- Observed Required Markers:
  - handle
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - handle: string username-like
  - min_time: numeric timestamp-like, semantic unknown
  - trim: boolean checkbox
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: public user
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Following graph does not prove commercial relationship.
- Runtime Questions To Verify:
  - min_time semantics
  - pagination behavior
  - completeness/sampling
  - trim effect
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/user/following?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-13 Followers

- API Family: TikTok
- Observed Description: Scrapes followers of a TikTok account.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/user/followers`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - handle
  - user_id
  - min_time
  - trim
- Observed Required Markers:
  - No required marker observed for handle/user_id in supplied evidence.
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - handle: string username-like
  - user_id: numeric-like string ID
  - min_time: numeric timestamp-like, semantic unknown
  - trim: boolean checkbox
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: public user
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Followers are not buyers or verified audience.
- Runtime Questions To Verify:
  - handle/user_id relationship
  - min_time semantics
  - completeness/sampling
  - pagination
  - privacy restrictions
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/user/followers?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-14 Search Users

- API Family: TikTok
- Observed Description: Scrapes TikTok users matching a search query.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/search/users`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - query
  - cursor
  - trim
- Observed Required Markers:
  - query
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - query: text
  - cursor: numeric/string-like continuation value depending endpoint
  - trim: boolean checkbox
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: query text
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Search rank is not creator relevance proof.
- Runtime Questions To Verify:
  - search ranking
  - pagination
  - identity fields
  - trim
  - market behavior if any
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/search/users?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-15 Search Suggestions

- API Family: TikTok
- Observed Description: Gets TikTok autocomplete search suggestions for a query.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/search/suggestions`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - query
  - region
- Observed Required Markers:
  - query
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - query: text
  - region: country/market code-like, e.g. US / GB
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: query prefix
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Search suggestions do not prove purchase intent.
- Runtime Questions To Verify:
  - region effect
  - personalization
  - freshness
  - stable ordering
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/search/suggestions?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-16 Search by Hashtag

- API Family: TikTok
- Observed Description: Scrapes TikTok videos by hashtag.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/search/hashtag`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - hashtag
  - region
  - cursor
  - trim
- Observed Required Markers:
  - hashtag
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - hashtag: text
  - region: country/market code-like, e.g. US / GB
  - cursor: numeric/string-like continuation value depending endpoint
  - trim: boolean checkbox
- Explicit Provider Notes:
  - TikTok can return duplicate results for this search.
  - Scrape Creators states this appears to be TikTok-side behavior.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: hashtag
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Hashtag use does not equal topic or user intent.
- Runtime Questions To Verify:
  - region effect
  - cursor
  - hard cap
  - ranking semantics
  - video ID
  - duplicate frequency
  - metrics
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/search/hashtag?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-17 Search by Keyword

- API Family: TikTok
- Observed Description: Scrapes TikTok videos matching a keyword.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/search/keyword`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - query
  - date_posted
  - sort_by
  - region
  - cursor
  - trim
- Observed Required Markers:
  - query
- Observed Enum Values:
  - date_posted: `yesterday`, `this-week`, `this-month`, `last-3-months`, `last-6-months`, `all-time`
  - sort_by: `relevance`, `most-liked`, `date-posted`
- Observed UI Example Values / Type Hints:
  - query: text
  - date_posted: bounded enum
  - sort_by: endpoint-specific enum
  - region: country/market code-like, e.g. US / GB
  - cursor: numeric/string-like continuation value depending endpoint
  - trim: boolean checkbox
- Explicit Provider Notes:
  - TikTok can return duplicate results for this search.
  - Scrape Creators states this appears to be TikTok-side behavior.
  - Keyword Search only returns Videos.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: query text
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Search result sample does not represent total market size.
- Runtime Questions To Verify:
  - date_posted effect
  - sort_by effect
  - region effect
  - cursor
  - ranking
  - duplicates
  - metric fields
  - time fields
  - result hard cap
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/search/keyword?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-18 Top Search

- API Family: TikTok
- Observed Description: There is a 'Top' Search in TikTok. It can return Photo Carousels and Videos. Keyword Search only returns Videos.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/search/top`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - query
  - publish_time
  - sort_by
  - region
  - cursor
- Observed Required Markers:
  - query
- Observed Enum Values:
  - publish_time: `yesterday`, `this-week`, `this-month`, `last-3-months`, `last-6-months`, `all-time`
  - sort_by: `relevance`, `most-liked`, `date-posted`
- Observed UI Example Values / Type Hints:
  - query: text
  - publish_time: bounded enum
  - sort_by: endpoint-specific enum
  - region: country/market code-like, e.g. US / GB
  - cursor: numeric/string-like continuation value depending endpoint
- Explicit Provider Notes:
  - TikTok can return duplicate results for this search.
  - Top Search can return Videos and Photo Carousels.
  - Keyword Search only returns Videos.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: query text
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Top Search does not prove purchase or conversion. Do not modify `NormalizedVideoSignal` for Carousel support until runtime response reconnaissance exists.
- Runtime Questions To Verify:
  - response entity discriminator
  - carousel identity
  - video vs carousel field differences
  - duplicate behavior
  - ranking
  - pagination
  - region
  - publish_time
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/search/top?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-19 Get popular creators

- API Family: TikTok
- Observed Description: Get popular creators from TikTok. Filter by follower count, creator country, audience country, and sort by engagement, follower count, or average views.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/creators/popular`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - page
  - sortBy
  - followerCount
  - creatorCountry
  - audienceCountry
- Observed Required Markers:
  - No required marker observed in supplied UI evidence.
- Observed Enum Values:
  - sortBy: `engagement`, `follower`, `avg_views`
  - followerCount: `10K-100K`, `100K-1M`, `1M-10M`, `10M+`
  - creatorCountry partial observed enum: `AU`, `BR`, `CA`, `EG`, `FR`, `DE`, `ID`, `IL`
  - audienceCountry: selector observed; full enum not captured.
- Observed UI Example Values / Type Hints:
  - page: integer-like
  - sortBy: provider camelCase enum
  - followerCount: provider camelCase bounded enum
  - creatorCountry: country selector
  - audienceCountry: country selector
- Explicit Provider Notes:
  - Do not rename provider parameters.
  - Partial observed enum. Full provider-supported country list was not captured.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: category or market context
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Popular creators may not match product demand.
- Runtime Questions To Verify:
  - full country lists
  - audienceCountry semantics
  - ranking definition
  - pagination/page size
  - actual metrics returned
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/creators/popular?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-20 Get Song Details

- API Family: TikTok
- Observed Description: Scraping details from the song detail.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/song`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - clipId
- Observed Required Markers:
  - clipId
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - clipId: numeric-like ID
- Explicit Provider Notes:
  - Parameter spelling must remain `clipId`.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: song ID
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Sound popularity does not prove product demand.
- Runtime Questions To Verify:
  - sound/song identity
  - original vs catalog sound
  - usage metrics
  - availability
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/song?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-21 TikToks using Song

- API Family: TikTok
- Observed Description: Get the TikToks using a song.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/song/videos`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - clipId
  - cursor
- Observed Required Markers:
  - No required marker observed for clipId in supplied evidence.
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - clipId: numeric-like ID
  - cursor: numeric/string-like continuation value depending endpoint
- Explicit Provider Notes:
  - Parameter spelling must remain `clipId`.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: song ID
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Shared sound does not imply shared business intent.
- Runtime Questions To Verify:
  - whether clipId is actually required
  - cursor
  - result completeness
  - ranking
  - duplicates
  - song-video linkage
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/song/videos?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## TT-22 Trending Feed

- API Family: TikTok
- Observed Description: Get the trending feed from TikTok.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/get-trending-feed`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - region
  - trim
- Observed Required Markers:
  - region
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - region: country/market code-like, e.g. US / GB
  - trim: boolean checkbox
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: market or feed context
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Trending feed may be personalized or volatile.
- Runtime Questions To Verify:
  - region semantics
  - personalization
  - freshness/window
  - result volatility
  - trim effect
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/get-trending-feed?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## SHOP-01 Shop Search

- API Family: TikTok Shop
- Observed Description: Scrape TikTok Shop Products from a search!
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/shop/search`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - query
  - page
  - region
- Observed Required Markers:
  - query
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - query: text
  - page: integer-like
  - region: country/market code-like, e.g. US / GB
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: shop query
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Public shop visibility does not prove sales.
- Runtime Questions To Verify:
  - page semantics
  - region scope
  - shop vs product result identity
  - ranking
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/shop/search?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## SHOP-02 Shop Products

- API Family: TikTok Shop
- Observed Description: Get the products from a TikTok Shop.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/shop/products`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - url
  - cursor
  - sort_by
  - region
- Observed Required Markers:
  - url
- Observed Enum Values:
  - sort_by: `top`, `new_releases`
- Observed UI Example Values / Type Hints:
  - url: TikTok full URL
  - cursor: numeric/string-like continuation value depending endpoint
  - sort_by: endpoint-specific enum
  - region: country/market code-like, e.g. US / GB
- Explicit Provider Notes:
  - Use the cursor from the response to paginate through results.
  - Non-US shop catalog coverage depends on TikTok exposing that shop in the selected region.
- Explicit Credit Observation: 1 credit/request, Observed From UI
- Candidate Prerequisite Entity: shop URL
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Product listing is public Commercial Visibility / L3-adjacent, not transaction proof.
- Runtime Questions To Verify:
  - cursor
  - shop identity
  - product identity
  - variants
  - region effect
  - product fields
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/shop/products?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## SHOP-03 Product Details

- API Family: TikTok Shop
- Observed Description: Get the details of a TikTok Shop Product.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/product`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - url
  - region
- Observed Required Markers:
  - url
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - url: TikTok full URL
  - region: country/market code-like, e.g. US / GB
- Explicit Provider Notes:
  - This endpoint currently supports US TikTok Shop products only.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: product URL
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Does not replace Andy's ProductBrief.
- Runtime Questions To Verify:
  - product ID returned
  - shop ID
  - variants
  - price
  - rating
  - public sales-like values if any
  - behavior for non-US product
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/product?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## SHOP-04 Product Reviews

- API Family: TikTok Shop
- Observed Description: Get a product's reviews.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/shop/product/reviews`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - url
  - product_id
  - region
  - page
- Observed Required Markers:
  - No required marker observed for url/product_id in supplied evidence.
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - url: TikTok full URL
  - product_id: numeric-like ID
  - region: country/market code-like, e.g. US / GB
  - page: integer-like
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: product URL or product ID
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Reviews are public feedback signals, not the full buyer population.
- Runtime Questions To Verify:
  - url alone
  - product_id alone
  - whether either/or
  - page semantics
  - review completeness
  - reviewer identity
  - translations
  - market
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/shop/product/reviews?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## SHOP-05 User Showcase

- API Family: TikTok Shop
- Observed Description: Gets public user's showcase products.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/user/showcase`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - handle
  - region
  - cursor
- Observed Required Markers:
  - handle
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - handle: string username-like
  - region: country/market code-like, e.g. US / GB
  - cursor: numeric/string-like continuation value depending endpoint
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: public user or showcase identity
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Showcase presence does not prove clicks, add-to-cart, or sales.
- Runtime Questions To Verify:
  - creator-product identity
  - region
  - cursor
  - current vs historical showcase products
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/user/showcase?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## AD-01 Ad Library Search

- API Family: TikTok Ad Library
- Observed Description: Search TikTok's public Ads Library by advertiser name or keyword.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/ad-library/search`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - query
  - cursor
- Observed Required Markers:
  - query
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - query: text
  - cursor: numeric/string-like continuation value depending endpoint
- Explicit Provider Notes:
  - None observed in supplied UI evidence.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: ad query
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Public ad visibility does not prove spend or sales attribution.
- Runtime Questions To Verify:
  - advertiser identity
  - ad identity
  - cursor
  - date/status fields
  - ranking
  - market scope
  - metrics if any
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/ad-library/search?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## AD-02 Ad Library Ad

- API Family: TikTok Ad Library
- Observed Description: Gets details for a TikTok ad from either Creative Center Top Ads or TikTok's public Ads Library.
- HTTP Method: GET
- API Version: v1
- Endpoint Path: `/v1/tiktok/ad-library/ad`
- Auth Pattern: Header `x-api-key: <redacted>`
- Observed UI Parameters:
  - ad_id
- Observed Required Markers:
  - ad_id
- Observed Enum Values:
  - None observed in supplied UI evidence.
- Observed UI Example Values / Type Hints:
  - ad_id: numeric-like ID
- Explicit Provider Notes:
  - Ad details may come from either Creative Center Top Ads or TikTok's public Ads Library.
- Explicit Credit Observation: Unknown
- Candidate Prerequisite Entity: ad ID
- Request Surface Verification Status: Observed From UI / Redacted Curl Surface
- Runtime Verification Status: Not Tested
- Response Verification Status: Not Tested
- Known Interpretation Boundary: Does not prove spend, clicks, conversion, or GMV.
- Runtime Questions To Verify:
  - ad identity compatibility across Creative Center / Public Ads Library
  - advertiser ID
  - creative URLs
  - run dates
  - status
  - public metrics if any
- Canonical Redacted Request Surface:

```bash
curl "https://api.scrapecreators.com/v1/tiktok/ad-library/ad?<observed-query-parameters>" \
  -H "x-api-key: <redacted>"
```

This is a request-surface template, not a runtime-validated legal parameter combination.

## Unified Parameter Type Hints

These are UI type hints, not formal Python, JSON Schema, or implementation types.

| Parameter | Observed Type Hint | Verification |
|---|---|---|
| handle | string username-like | UI example only |
| user_id | numeric-like string ID | UI example only |
| url | TikTok full URL | Observed |
| query | text | Observed |
| hashtag | text | Observed |
| cursor | numeric/string-like continuation value depending endpoint | Runtime Unknown |
| max_cursor | large numeric-like continuation value | Runtime Unknown |
| page | integer-like | Observed UI |
| region | country/market code-like, e.g. US / GB | Observed UI |
| language | language-code-like, e.g. en | Observed UI |
| trim | boolean checkbox | Observed UI |
| get_transcript | boolean checkbox | Observed UI |
| download_media | boolean checkbox | Observed UI |
| use_ai_as_fallback | boolean-like | Observed UI |
| min_time | numeric timestamp-like | Semantic Unknown |
| room_id | numeric-like ID | Observed UI |
| comment_id | numeric-like ID | Observed UI |
| clipId | numeric-like ID | Observed UI |
| product_id | numeric-like ID | Observed UI |
| ad_id | numeric-like ID | Observed UI |
| cache_max_age | bounded enum | Observed |
| date_posted | bounded enum | Observed |
| publish_time | bounded enum | Observed |
| sort_by | endpoint-specific enum | Partially Observed |
| sortBy | provider camelCase enum | Observed |
| followerCount | provider camelCase bounded enum | Observed |
| creatorCountry | country selector | Partial Observed |
| audienceCountry | country selector | Selector Observed / enum incomplete |

## Explicit Credit Observations

| Endpoint | Observed Credit Cost | Evidence Status |
|---|---:|---|
| TT-03 User's Audience Demographics | 26 credits/request | Observed From UI |
| SHOP-02 Shop Products | 1 credit/request | Observed From UI |
| Other 27 endpoints | Unknown | Not yet observed / runtime not tested |

Current available credit snapshot: 24,343 credits.

Evidence date: 2026-08-07.

This balance is a UI-time observation, not a constant configuration.

## Duplicate Observations

Scrape Creators UI explicitly warned about TikTok-side duplicate results for at least:

- TT-16 Search by Hashtag
- TT-17 Search by Keyword
- TT-18 Top Search

This provider-side UI observation supports the existing SIG design that raw duplicate evidence must be retained and deduplication must occur in a later processing layer.

This document records the evidence relationship only. It does not modify [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md).

## Keyword Search vs Top Search

| Feature | Search by Keyword | Top Search |
|---|---|---|
| Endpoint | TT-17 | TT-18 |
| Content types observed in provider description | Videos only | Videos + Photo Carousels |
| Time filter | date_posted | publish_time |
| Sort parameter | sort_by | sort_by |
| Duplicate warning | Yes | Yes |
| Runtime response contract | Not Tested | Not Tested |

Top Search Carousel support is an observed provider UI description fact. Do not modify `NormalizedVideoSignal` to support Carousel now. Wait for real response reconnaissance.

## Request Surface Maturity

### Complete / Observed

- 29/29 endpoint names
- 29/29 endpoint paths
- API family mapping
- API version mapping
- GET request surface
- x-api-key auth pattern
- 29/29 UI parameter surfaces
- visible required markers
- captured enums
- captured provider descriptions
- captured explicit provider cost notes
- captured provider support limitations

### Not Runtime Verified

- actual legal parameter combinations
- complete required/optional rules
- response fields
- response field types
- pagination behavior
- ID cross-endpoint compatibility
- missing/null/zero semantics
- errors
- rate limits
- credit cost for most endpoints
- metric snapshot semantics
- search ranking
- region effectiveness
- cache behavior
- trim behavior
- runtime response shape

Final maturity label:

```text
Observed Request Surface Complete
Runtime Response Reconnaissance Not Started
```

## Reuse Rule

The following content has been completed and should not be recollected from scratch in future chats or development rounds:

- endpoint count
- endpoint names
- endpoint path list
- API versions
- auth pattern
- currently observed UI parameter names
- currently visible required markers
- captured enums
- observed cost notes
- US-only Product Details note
- duplicate warnings
- Keyword vs Top Search content-type distinction

Create a new request-surface revision only when:

- Scrape Creators UI clearly changes
- API paths change
- parameters change
- a new endpoint appears

Do not silently overwrite V0.1.

## Runtime Evidence Authority

This baseline should be reused as request-side evidence during runtime reconnaissance. Runtime evidence has higher authority for actual callable behavior, response fields, errors, pagination, identity linking, cost deltas, and business capability verdicts.
