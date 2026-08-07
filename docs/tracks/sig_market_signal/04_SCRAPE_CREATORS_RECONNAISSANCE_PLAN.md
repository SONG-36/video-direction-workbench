# Scrape Creators Reconnaissance Plan

- Version: V0.1
- Status: Draft
- Authority: Detailed Test Plan
- Scope: Complete reconnaissance campaign plan for all currently observed Scrape Creators TikTok, TikTok Shop, and TikTok Ad Library endpoints before any live API testing.
- Depends On: [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md), [02_DATA_SOURCE_CAPABILITY_MAP.md](02_DATA_SOURCE_CAPABILITY_MAP.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Pending Andy Review

## 1. Purpose

This document defines a complete Scrape Creators reconnaissance campaign before any API call. It ensures every currently observed endpoint is tested, blocked with evidence, rejected with a reason, or deferred by explicit human decision.

## 2. Business Context

Track C SIG uses market and business signals to support human research decisions. Scrape Creators may provide public TikTok, TikTok Shop, and TikTok Ad Library data, but endpoint names alone do not prove fields, parameters, pagination, pricing, ranking, metric semantics, or business usefulness.

## 3. Complete Campaign Scope

The complete campaign covers all 29 currently observed endpoints, not only the four SIG-P0 core candidates.

Complete Coverage ≠ Unlimited Requests. A complete campaign means every endpoint receives an evidence-backed final status and business capability verdict; it does not mean unlimited requests, uncontrolled cost, or identical test depth for every endpoint.

Completion cannot be claimed by testing only:

- Search by Keyword
- Search by Hashtag
- Video Info
- Transcript

These four may run first because they seed P0, but the campaign remains incomplete until every endpoint has final evidence-backed status.

## 3A. Campaign Budget And Safety Gate

Live API testing must stay within the approved budget, request, page, quota, and stop-limit values. The execution authority for the approved runtime budget is [09_SCRAPE_CREATORS_RUNTIME_RECONNAISSANCE_EXECUTION_PLAN.md](09_SCRAPE_CREATORS_RUNTIME_RECONNAISSANCE_EXECUTION_PLAN.md).

| field | current value | note |
|---|---|---|
| campaign_currency_budget_max | Unknown / Not Observable | Real currency ceiling is not observable from current evidence. |
| campaign_credit_budget_max | 2000 Scrape Creators credits | Campaign credit-spend ceiling. |
| campaign_request_budget_max | 150 actual HTTP API requests | Total campaign request ceiling. This is a ceiling, not a target. |
| default_endpoint_request_cap | 5 actual HTTP requests per endpoint | Default per-endpoint cap unless human-approved task override exists. |
| default_pagination_page_cap | 3 pages | Default pagination reconnaissance cap, not full dataset collection. |
| repeated_snapshot_request_cap | 2 additional requests | Maximum repeats beyond the initial observation when repeated snapshots are required or approved. |
| minimum_remaining_quota_threshold | 22000 Scrape Creators credits | Remaining-credit hard stop. |
| additional_budget_requires_human_approval | true | Any extra budget requires explicit human approval before additional calls. |

Stop immediately or pause the affected endpoint when any approved budget, request, pagination, quota, account-risk, legal, or plan boundary is reached. Budget exhaustion is a valid evidence-backed endpoint or campaign stop reason; it does not permit uncontrolled retries.

## 4. Endpoint Families

TikTok endpoints:

1. Profile
2. Profile Region
3. User's Audience Demographics
4. Collection Videos
5. Profile Videos
6. Video Info
7. Transcript
8. Live
9. Live Info
10. Comments
11. Comment Replies
12. Following
13. Followers
14. Search Users
15. Search Suggestions
16. Search by Hashtag
17. Search by Keyword
18. Top Search
19. Get popular creators
20. Get Song Details
21. TikToks using Song
22. Trending Feed

TikTok Shop endpoints:

23. Shop Search
24. Shop Products
25. Product Details
26. Product Reviews
27. User Showcase

TikTok Ad Library endpoints:

28. Ad Library Search
29. Ad Library Ad

Newly observed endpoints require a new test matrix version. Current documents must not infer real capability from endpoint names.

## 5. Test Objectives

- Verify actual callable status, authorization needs, and plan boundaries.
- Capture canonical redacted request evidence and immutable raw response evidence.
- Observe real response fields, field types, missingness, identity fields, time fields, metrics, pagination, and errors.
- Determine business interpretation limits.
- Decide whether each endpoint should be Adopt For P0, Adopt For Future Stage, Research Only, Reject, or Blocked Pending Access.

## 6. Test Evidence Principles

- All request parameters, fields, limits, and semantics must come from real calls, real exports, official explanation, or other reviewable evidence.
- Raw HTTP requests must not be persisted. Only canonical redacted request evidence may be saved.
- Raw response evidence must be preserved unchanged.
- Redacted copies are used for review.
- Every claim must trace to `endpoint_test_run_id` and artifact paths.
- No API key, Authorization header, Cookie, session token, or account-takeover material may be recorded.

## 7. Test Data Strategy

Main business context:

- Platform: TikTok
- Primary market candidate: US
- Primary language candidate: English
- Product context: car vacuum / portable car vacuum
- Adjacent context: car cleaning
- Scenario context: seat gap cleaning
- Pain point context: pet hair car
- Hashtag candidate: public hashtags related to this context, verified only during execution

The test phase must prepare and document:

- one legal public user
- one legal public video
- one video with usable transcript
- one video with unavailable transcript
- one video with comments
- one video with no comments or restricted comments
- one comment and one reply
- one legal song
- one video using that song
- one verifiable live case or evidence that live is unavailable
- one public shop
- one public product
- one product with reviews
- one user showcase case
- one public ad
- one no-result query
- one invalid ID
- one unavailable or expired object

This document does not invent concrete IDs.

## 8. Dependency Order

- Search by Keyword / Search by Hashtag can seed video IDs.
- Video Info verifies video identity and metrics.
- Profile / Profile Videos verify user and video relationships.
- Comments can seed comment IDs.
- Comment Replies depends on comment ID.
- Get Song Details depends on song ID.
- TikToks using Song depends on song identity.
- Shop Products depends on shop identity.
- Product Details / Product Reviews depend on product identity.
- Ad Library Ad depends on ad identity from Ad Library Search.
- Live Info depends on usable live identity.
- Missing prerequisites do not remove endpoints from the matrix.

## 9. Common Test Dimensions

Every endpoint must be evaluated across:

- happy path
- missing / invalid input
- pagination
- time semantics
- identity
- missingness
- market / language / region
- cost / quota / rate limit
- business interpretation

## 10. Positive Cases

Each endpoint needs at least one successful positive case only when prerequisite, authorization, plan access, quota, and safe legal input are available within the approved Campaign Budget And Safety Gate.

If a positive case cannot be run because of missing prerequisite, authorization, plan or quota boundary, unavailable endpoint, unsafe legal input, or explicit human deferral, the endpoint can still complete current reconnaissance with an evidence-backed blocked, unavailable, not applicable, or deferred status. The report must record the status, reason, evidence, remaining unknowns, and allowed Capability Verdict mapping.

## 11. Negative Cases

When safe and low risk, test missing required input, invalid ID, nonexistent object, empty query, no-result query, unauthorized object, deleted object, or inaccessible object. Do not run destructive, abusive, policy-violating, or account-risk tests.

## 12. Edge Cases

Observe null fields, absent fields, empty strings, zero values, type variation, unavailable transcripts, disabled comments, inaccessible videos, private or deleted objects, and non-English or mixed-language results.

## 13. Pagination And Volume

Test first page, next page, cursor or page token, end page, repeated page, expired cursor, missing pagination fields, maximum retrievable count, and hard upper limits where safe and within the approved budget gate.

## 14. Time And Metric Snapshot Semantics

Verify whether `published_at`, `collected_at`, `updated_at`, metric snapshot time, time window support, timezone, and repeated-fetch metric changes exist. Do not assume a metric timestamp from a generic response time. Repeated snapshot testing follows each endpoint's `snapshot_retest_requirement` and `snapshot_retest_rationale` from the test matrix.

## 15. Identity And Linking

Verify stability and cross-endpoint usability of video ID, user ID, comment ID, reply ID, song ID, live ID, shop ID, product ID, ad ID, and source URL.

## 16. Market / Language / Region Semantics

If an endpoint supports market, region, locale, or language inputs, test whether those controls actually affect returned results. Parameter names do not prove semantics.

## 17. Missing And Dirty Data

Record absent fields, null, empty string, zero, type changes, missing nested objects, unavailable transcripts, disabled comments, restricted objects, and duplicate or irrelevant results.

## 18. Cost / Quota / Rate Limit

Record whether a request appears billable, billing unit if visible, quota, response headers, rate limits, 429-like behavior, retry advice, and plan-gated fields. Do not intentionally flood endpoints or attempt to trigger bans.

Live testing must stop or pause when approved request caps, page caps, currency budget, repeated snapshot cap, or minimum remaining quota threshold would be exceeded.

## 19. Compliance And Terms

Testing must stay low risk, use only allowed access, avoid secrets in artifacts, avoid destructive operations, and preserve enough evidence for review without exposing account-control material.

## 20. Raw Evidence Retention

Raw responses are immutable. Redacted copies are separate. Canonical redacted request evidence and response evidence must be linked by `endpoint_test_run_id` and hashed where possible.

## 21. Result Status Model

Endpoint Test Status values:

- Not Run
- Passed
- Partially Passed
- Failed
- Blocked By Prerequisite
- Blocked By Authorization
- Blocked By Plan Or Quota
- Endpoint Unavailable
- Not Applicable
- Deferred By Human Decision

`Blocked` does not mean unavailable. `Failed` does not mean permanent lack of support. `Endpoint Unavailable` requires call or documentation evidence. `Not Applicable` requires business reason. `Deferred By Human Decision` requires explicit human decision. Future Stage is not a reason to skip reconnaissance.

## 22. Completion Criteria

The campaign is complete only when:

1. All 29 endpoints appear in the matrix.
2. Every endpoint has final status.
3. No unexplained Not Run remains.
4. Every actual call preserves canonical redacted request evidence and raw response.
5. Every endpoint has a field list or evidence-backed block.
6. Every endpoint has a parameter list or evidence-backed unknown.
7. Every endpoint has pagination conclusion.
8. Every endpoint has identity conclusion.
9. Every endpoint has time semantics conclusion.
10. Every endpoint has missingness observation.
11. Every endpoint has cost / quota observation or explicit unknown.
12. Every endpoint has business-use judgment.
13. Every endpoint has interpretation boundary.
14. Every endpoint has final verdict: Adopt For P0, Adopt For Future Stage, Research Only, Reject, or Blocked Pending Access.
15. Raw evidence traces to test records.
16. Final report separates verified results from unknowns.
17. API names or UI labels are not used as capability proof.

## 23. Stop Conditions

Stop or pause testing when credentials, plan status, legal permission, account risk, quota risk, unclear terms, or unsafe negative case behavior creates unacceptable risk. Paused endpoints remain in the matrix with a status and reason.

Budget stop gates also stop or pause testing when the approved currency budget, total request budget, per-endpoint request cap, pagination page cap, repeated snapshot cap, or minimum remaining quota threshold is reached.

## 24. Explicit Non-Goals

- No API call in this documentation round.
- No API key use.
- No real campaign creation.
- No downloaded response.
- No test script.
- No Python.
- No Pydantic Schema.
- No database.
- No UI.
- No CLI.
- No ResearchTask, K-P0, N03, N17, or N18 development.

## 25. Campaign Deliverables

- Complete endpoint test matrix.
- Canonical redacted request evidence records.
- Immutable raw responses.
- Redacted response copies.
- Field observation records.
- Endpoint result records.
- Final reconnaissance report.
- Capability map change recommendations.
