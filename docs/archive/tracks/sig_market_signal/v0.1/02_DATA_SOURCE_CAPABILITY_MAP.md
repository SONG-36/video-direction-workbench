# Data Source Capability Map

- Version: V0.1
- Status: Approved
- Authority: Preliminary Design
- Scope: Candidate data source capability map for observed Scrape Creators API families and endpoints without inventing unverified API details.
- Depends On: `docs/05_MARKET_SIGNAL_TOOL_CONTRACT.md`, `docs/tracks/sig_market_signal/00_SIG_SYSTEM_BLUEPRINT.md`, `docs/tracks/sig_market_signal/01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md`
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Andy
- Approval Date: 2026-08-07

Approval Boundary: This approval covers the data source reconnaissance framework only. It does not approve Scrape Creators real fields, parameters, pricing, pagination, ranking, metric semantics, SIG-P0 Implementation Ready status, code implementation, or endpoint suitability.

## Source Discipline

The endpoint names below come from current tool UI observation. Unless repository documents or real sample payloads provide evidence, this document does not define request parameters, response fields, pagination, time windows, ranking rules, limits, pricing, completeness, or metric definitions.

Default verification status for all listed endpoints is:

```text
Verification Status: Unverified
```

## Capability Table

| provider | api_family | endpoint | candidate_business_purpose | candidate_signal_layer | candidate_stage | possible_entity_granularity | verification_status | required_reconnaissance | known_interpretation_risk | current_scope_status |
|---|---|---|---|---|---|---|---|---|---|---|
| Scrape Creators | TikTok | Search by Keyword | Collect candidate public videos by text query. | L1/L2 | SIG-P0 | Query result, video candidate | Unverified | Verify inputs, ranking, pagination, returned IDs, metric fields, market/language semantics. | Search results are sample-dependent and cannot represent whole-market volume. | P0 Core Candidate |
| Scrape Creators | TikTok | Search by Hashtag | Collect candidate public videos by hashtag. | L1/L2 | SIG-P0 | Hashtag result, video candidate | Unverified | Verify hashtag matching, ranking, pagination, returned IDs, metrics. | Hashtag use may not equal content topic or user intent. | P0 Core Candidate |
| Scrape Creators | TikTok | Video Info | Retrieve public metadata and performance metrics for known videos. | L2 | SIG-P0 | Video | Unverified | Verify video ID input, metric fields, timestamps, unavailable videos, metric snapshot semantics. | Metric values may be snapshots and cannot prove conversions. | P0 Core Candidate |
| Scrape Creators | TikTok | Transcript | Retrieve transcript text if available. | L1 | SIG-P0 | Video transcript | Unverified | Verify transcript availability, language, timestamps, missing cases. | Transcript absence must not mean content is irrelevant. | P0 Core Candidate |
| Scrape Creators | TikTok | Profile | Observe creator profile information. | L1/L2 | SIG-P1 | Creator profile | Unverified | Verify profile fields, follower metrics, identity stability. | Creator profile does not prove buyer demographics. | Future P1 |
| Scrape Creators | TikTok | Profile Region | Observe public profile region if available. | L1/L2 | SIG-P1 | Creator profile | Unverified | Verify field source and reliability. | Region may not equal audience market or buyer market. | Future P1 |
| Scrape Creators | TikTok | User's Audience Demographics | Candidate creator audience visibility signal; not used for C02 creator-size analysis. | L1/L2 auxiliary audience visibility | SIG-P1 | Creator audience estimate | Unverified | Verify data source, calculation method, coverage, time window. | Must not be treated as true buying audience or written into `ResearchTask.primary_audience` automatically. | Requires Verification |
| Scrape Creators | TikTok | Collection Videos | Observe videos in a collection surface. | L1/L2 | SIG-P1 | Collection, video | Unverified | Verify collection identity, access, video fields, ordering. | Collection membership may not imply market demand. | Future P1 |
| Scrape Creators | TikTok | Profile Videos | Collect videos from a creator profile. | L1/L2 | SIG-P1 | Creator video | Unverified | Verify pagination, publication time, metric fields. | High performance may reflect creator size rather than content structure. | Future P1 |
| Scrape Creators | TikTok | Live | Observe live-related public availability. | L1/L2 | SIG-P1 | Live session | Unverified | Verify fields and whether historical data exists. | Live visibility cannot prove sales without validated commerce data. | Future P1 |
| Scrape Creators | TikTok | Live Info | Observe public live metadata. | L1/L2 | SIG-P1 | Live session | Unverified | Verify ID input, metrics, timestamps. | Live metrics may be volatile and context-specific. | Future P1 |
| Scrape Creators | TikTok | Comments | Collect public comments for videos. | L1/L2 | SIG-P1 | Comment | Unverified | Verify comment fields, pagination, moderation gaps, language. | Comments are public feedback signals, not statistically representative buyer research. | Future P1 |
| Scrape Creators | TikTok | Comment Replies | Collect public replies to comments. | L1/L2 | SIG-P1 | Comment reply | Unverified | Verify parent comment identity and pagination. | Reply threads can overrepresent disputes or jokes. | Future P1 |
| Scrape Creators | TikTok | Following | Observe accounts followed by a profile. | L1 | SIG-P1 | Creator relationship | Unverified | Verify availability, privacy limits, identity semantics. | Following graph does not prove commercial relationship. | Future P1 |
| Scrape Creators | TikTok | Followers | Observe public follower list or follower data if available. | L1 | SIG-P1 | Creator relationship | Unverified | Verify availability, sampling, privacy limits. | Follower data cannot prove buyer demographics. | Future P1 |
| Scrape Creators | TikTok | Search Users | Discover creator accounts by query. | L1 | SIG-P1 | User search result | Unverified | Verify ranking, returned fields, pagination. | Search rank does not equal creator relevance or performance. | Future P1 |
| Scrape Creators | TikTok | Search Suggestions | Discover platform search expression suggestions. | L1 | SIG-P1 | Search suggestion | Unverified | Verify input, locale, ranking semantics, freshness. | Suggestions do not prove purchase intent. | Future P1 |
| Scrape Creators | TikTok | Top Search | Observe top search expressions if available. | L1 | SIG-P1 | Search term | Unverified | Verify market/time semantics and fields. | Top search visibility does not prove conversion. | Future P1 |
| Scrape Creators | TikTok | Get popular creators | Discover popular creators by platform criteria. | L1/L2 | SIG-P1 | Creator | Unverified | Verify category, market, ranking, metrics. | Popular creator lists may be unrelated to target product category. | Future P1 |
| Scrape Creators | TikTok | Get Song Details | Observe public sound/song metadata. | L1 | SIG-P1 | Song/sound | Unverified | Verify fields and relationship to videos. | Sound popularity does not prove product demand. | Future P1 |
| Scrape Creators | TikTok | TikToks using Song | Collect videos using a sound/song. | L1/L2 | SIG-P1 | Song-video relationship | Unverified | Verify query inputs, ranking, pagination, metrics. | Shared sound does not imply shared business intent. | Future P1 |
| Scrape Creators | TikTok | Trending Feed | Observe trend feed samples. | L1/L2 | SIG-P1 | Feed video | Unverified | Verify market, personalization, ranking, time semantics. | Trending feed may be personalized or volatile. | Future P1 |
| Scrape Creators | TikTok Shop | Shop Search | Discover public shops. | Commercial Visibility / L3-adjacent | SIG-P3 | Shop search result | Unverified | Verify query, market, returned fields, ranking. | Public shop visibility does not prove real sales. | Future P3 |
| Scrape Creators | TikTok Shop | Shop Products | List public products for a shop. | Commercial Visibility / L3-adjacent | SIG-P3 | Shop product | Unverified | Verify shop ID, product fields, pagination. | Product listing does not prove transactions. | Future P3 |
| Scrape Creators | TikTok Shop | Product Details | Retrieve public product details. | Commercial Visibility / L3-adjacent | SIG-P3 | Product | Unverified | Verify fields, price semantics, availability, timestamps. | Public product details cannot replace ProductBrief facts for Andy's product. | Future P3 |
| Scrape Creators | TikTok Shop | Product Reviews | Retrieve public product reviews. | Commercial Visibility / L3-adjacent | SIG-P3 | Product review | Unverified | Verify review fields, rating, language, sampling. | Reviews are public feedback signals, not full buyer population proof. | Future P3 |
| Scrape Creators | TikTok Shop | User Showcase | Observe public creator/product showcase. | Commercial Visibility / L3-adjacent | SIG-P3 | User-product relationship | Unverified | Verify relationship fields and visibility rules. | Showcase presence does not prove clicks, add-to-cart, or sales. | Future P3 |
| Scrape Creators | TikTok Ad Library | Ad Library Search | Search public ad library materials. | L1/L2 public ad visibility | SIG-P2 | Ad search result | Unverified | Verify search inputs, fields, time range, ranking. | Public ad visibility does not prove spend or sales attribution. | Future P2 |
| Scrape Creators | TikTok Ad Library | Ad Library Ad | Retrieve public ad material details. | L1/L2 public ad visibility | SIG-P2 | Public ad | Unverified | Verify ad ID, creative fields, status, timestamps, metrics if any. | Public ad details cannot prove real GMV or ad-driven causality. | Future P2 |

## P0 Core Candidate Notes

P0 core candidates are Search by Keyword, Search by Hashtag, Video Info, and Transcript. They remain candidates until data source reconnaissance confirms inputs, fields, identity, metric semantics, and usable raw export availability.

The preferred first implementation entry is Scrape Creators JSON / CSV export, not a live API adapter. This is a provisional design direction pending Andy approval and data reconnaissance.

Search Suggestions can be observed during SIG-0 data source reconnaissance or manual research, but it is not part of the SIG-P0 formal collection, normalization, and reporting core pipeline. If it should be pulled into P0 later, that requires a separate business reason and contract change. Its usefulness for finding keywords does not automatically make it a P0 data object.

## User's Audience Demographics Boundary

`User's Audience Demographics` must not be treated as true buying audience. It must not automatically write to `ResearchTask.primary_audience`. Its data source, method, coverage, and semantics must be verified before any business interpretation. It is separated from C02 creator-size analysis because account size should rely on public profile and video performance indicators, not audience demographic estimates.

## P0 Data Source Reconnaissance Checklist

For each P0 core candidate endpoint, later reconnaissance must record:

| Checklist Item | Required Handling |
|---|---|
| Request Inputs | Record actual required and optional inputs from verified evidence. |
| Response Fields | Record actual returned fields from sample payloads or exports. |
| Pagination | Verify pagination rules and failure modes. |
| Search Ranking Semantics | Identify whether ordering is relevance, recency, popularity, personalized, or unknown. |
| Time Semantics | Identify publication time, collection time, and any time window controls. |
| Metric Snapshot Semantics | Determine when metrics are measured and whether they are point-in-time snapshots. |
| Video Identity | Confirm stable platform video identity fields. |
| Missing Fields | Record fields that may be absent and how absence appears. |
| Market / Language Semantics | Verify market, language, region, and localization behavior. |
| Cost / Quota | Verify pricing, request limits, and rate limits if available. |
| Raw Export Availability | Confirm JSON / CSV export format and raw retention path. |
| Terms / Compliance | Check usage limits and compliance boundaries. |
| Sample Payload Availability | Preserve sample payloads for contract review. |
| P0 Usefulness | Decide whether the endpoint can support L1/L2 P0 outputs. |
| Limitations | Record interpretation limits and dirty sample risks. |

This round does not call APIs and does not fill unverified answers.
