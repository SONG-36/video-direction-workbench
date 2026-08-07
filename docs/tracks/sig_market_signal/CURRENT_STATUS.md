# Track C Current Status

- Version: V0.1
- Status: Working Note
- Authority: Working Record
- Scope: Current state of Track C SIG documentation work.
- Depends On: [README.md](README.md), [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md), [02_DATA_SOURCE_CAPABILITY_MAP.md](02_DATA_SOURCE_CAPABILITY_MAP.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md), [DECISION_LOG.md](DECISION_LOG.md)
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Pending Andy Review

## Current Track

Track C — SIG Market Signal Tool

## Active Work

Runtime Reconnaissance Execution Plan approved; live runtime work remains blocked by Budget Gate.

## Current Goal

Close the Budget Gate before creating runtime task contracts or executing Wave A.

## Runtime Approval Status

| Item | Status |
|---|---|
| Observed Request Surface | Complete / committed |
| Runtime Reconnaissance Execution Plan | Approved |
| Runtime API Calls | Not Started |
| Budget Gate | Pending Approval |
| Next Blocking Item | Budget Gate |
| Next Execution Stage | Create Runtime Task Contract and begin Wave A only after Budget Gate approval. |

Do not start Runtime API calls before Budget Gate approval.

## Approved Decisions

- SIG-D-017: Approve and archive SIG System Blueprint V0.1, Business Question And Evidence Map V0.1, and Data Source Capability Map V0.1 as the Track C architecture and reconnaissance baseline.
- SIG-D-028: Runtime reconnaissance uses dependency waves, differentiated test depth, shared Seed Registry, standardized eight-block findings, and a final cross-endpoint identity map.

## Provisional Decisions

- SIG-D-001: Establish full SIG-0 to SIG-P6 blueprint while keeping implementation to approved slices.
- SIG-D-002: Prefer JSON / CSV export entry before API adapter; both must share one normalization pipeline.
- SIG-D-003: Distinguish Collection Run, Raw Record, Platform Video Identity, and NormalizedVideoSignal.
- SIG-D-004: Merge same-run platform video duplicates; preserve cross-run metric snapshots.
- SIG-D-005: Use `matched_queries` and preserve `raw_record_refs`.
- SIG-D-006: Distinguish `signal_id` and `platform_video_id`.
- SIG-D-007: SIG-P0 covers L1/L2 only; L3/L4 are future stages.
- SIG-D-008: SIG-P0 must not automatically modify or approve ResearchTask.
- SIG-D-009: Public video data must not prove true buyers, conversion, GMV attribution, or guaranteed creative success.
- SIG-D-010: Finish blueprint and P0 contract review before code implementation.
- SIG-D-011: Add `QueryExecution` as the per-query execution record inside a `CollectionRun`.
- SIG-D-012: Add `ProcessingRun` to separate data collection from rule-versioned processing.
- SIG-D-013: Separate input `queries`, execution-level `QueryExecution`, and derived `matched_queries`.
- SIG-D-014: Treat SIG-P3 public shop/product/review/showcase data as Commercial Visibility / L3-adjacent.
- SIG-D-015: Rename the recommendation-style report summary field to `research_basis_evidence_summary`.
- SIG-D-016: Keep Search Suggestions in Future SIG-P1 and separate User's Audience Demographics from creator-size analysis.
- SIG-D-018: Cover all 29 currently observed Scrape Creators endpoints across TikTok, TikTok Shop, and TikTok Ad Library.
- SIG-D-019: Execute in dependency order if needed, but require final evidence-backed status for every endpoint.
- SIG-D-020: Preserve redacted request evidence, immutable raw response evidence, hashes, field observations, limitations, and capability verdicts.
- SIG-D-021: Keep blocked, unavailable, rejected, and not-applicable endpoints in the final report.
- SIG-D-022: Require approved Campaign Budget And Safety Gate before live API calls.
- SIG-D-023: Successful positive case is required only when prerequisite, authorization, plan access, quota, and safe legal input are available.
- SIG-D-024: Replace binary repeated snapshot testing with Required / Conditional / Not Applicable plus rationale.
- SIG-D-025: Do not persist raw HTTP requests; persist canonical redacted request evidence only.
- SIG-D-026: Keep Test Status and Capability Verdict separate and require explicit legal mapping.
- SIG-D-027: Establish 08 as the canonical observed request-side evidence baseline for all 29 currently observed Scrape Creators endpoints.

## Current Facts

- 29 endpoint routes observed.
- 29 UI parameter surfaces observed.
- v1/v2/v3 version distribution recorded.
- partial enums recorded.
- TT-03 = 26 credits/request observed.
- SHOP-02 = 1 credit/request observed.
- Product Details currently US-only observed.
- Keyword/Hashtag/Top Search duplicate warning observed.
- Runtime execution plan approved as 09 with Wave A-E ordering, Level 1-3 depth, Seed Registry, eight result blocks, and Cross-Endpoint Identity Map.
- Runtime API response reconnaissance not started.

## Open Questions

- What real fields and limits do the four P0 core Scrape Creators endpoints provide?
- What exact relationship should `QueryExecution` and `RawDataset` use?
- Should `ProcessingRun` produce exactly one `MarketSignalReport` or versioned multiple reports?
- How should `platform_video_id` absence be handled?
- Can `source_url` be used as a fallback dedupe key?
- What stable formats should `query_execution_id`, `processing_run_id`, `raw_record_ref`, `signal_id`, and `report_id` use?
- What formulas and thresholds should P0 statistics use?
- What is the minimum acceptable sample threshold for a report observation?
- What classification result structure should preserve evidence, uncertainty, and rule version?

## Blocked Items

- No live API testing yet.
- Live API testing remains blocked until Campaign Budget And Safety Gate receives real approved values.
- Runtime Task Contract and Wave A execution must not begin before Budget Gate approval.
- SIG-P0 implementation blocked until reconnaissance results are available.
- SIG-P0 field contract remains Draft.

## Parked Work

- SIG code implementation
- NormalizedVideoSignal Schema
- MarketSignalReport Schema
- N02A
- Full K-P0
- N03
- Database
- UI
- Agent orchestration

## Next Review

1. Close the Budget Gate with approved values before any live call.
2. Create Runtime Task Contract only after Budget Gate approval.
3. Begin Wave A only after Budget Gate approval and runtime task contract setup.
4. Do not recollect basic request-surface data already captured in 08 unless a runtime discrepancy is found.

## Current Non-Goals

- No SIG source code.
- No API calls.
- No schema implementation.
- No database.
- No UI.
- No CLI.
- No ResearchTask changes.
- No K-P0 changes.
- No N03 work.
- No unapproved Git commit.

## Last Updated

2026-08-07
