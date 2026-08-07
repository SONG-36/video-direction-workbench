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

Runtime Reconnaissance Budget Gate approved; runtime task contract and RT-001 are not created.

## Current Goal

Create Runtime Task Contract before instantiating RT-001 for TT-17 Search by Keyword.

## Runtime Approval Status

| Item | Status |
|---|---|
| Observed Request Surface | Complete / committed |
| Runtime Reconnaissance Execution Plan | Approved / committed |
| Budget Gate | Approved |
| Runtime API Calls | Not Started |
| Runtime Task Contract | Not Created |
| RT-001 | Not Created |
| Next Step | Create `10_SCRAPE_CREATORS_RUNTIME_TASK_CONTRACT.md`, then instantiate RT-001 for TT-17 Search by Keyword. No API call should occur until the task contract and RT-001 pre-run checks are complete. |

Do not start Runtime API calls before the task contract and RT-001 pre-run checks are complete.

## Approved Decisions

- SIG-D-017: Approve and archive SIG System Blueprint V0.1, Business Question And Evidence Map V0.1, and Data Source Capability Map V0.1 as the Track C architecture and reconnaissance baseline.
- SIG-D-022: Require approved Campaign Budget And Safety Gate before live API calls.
- SIG-D-023: Successful positive case is required only when prerequisite, authorization, plan access, quota, and safe legal input are available.
- SIG-D-024: Replace binary repeated snapshot testing with Required / Conditional / Not Applicable plus rationale.
- SIG-D-025: Do not persist raw HTTP requests; persist canonical redacted request evidence only.
- SIG-D-026: Keep Test Status and Capability Verdict separate and require explicit legal mapping.
- SIG-D-028: Runtime reconnaissance uses dependency waves, differentiated test depth, shared Seed Registry, standardized eight-block findings, and a final cross-endpoint identity map.
- SIG-D-029: Approve the initial Scrape Creators Runtime Reconnaissance Campaign Budget Gate.

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
- Budget Gate approved with 2000-credit, 150-request, 5-request endpoint, 3-page pagination, 2-additional-snapshot, and 22000 remaining-credit stop limits.
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
- Runtime Task Contract is not created.
- RT-001 is not created.
- Runtime API calls must not begin until the task contract and RT-001 pre-run checks are complete.
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

1. Create `10_SCRAPE_CREATORS_RUNTIME_TASK_CONTRACT.md`.
2. Instantiate RT-001 for TT-17 Search by Keyword.
3. Complete RT-001 pre-run checks before any live call.
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
