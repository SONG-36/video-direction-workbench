# Track C Decision Log

- Version: V0.1
- Status: Working Note
- Authority: Working Record
- Scope: Track C SIG decision history and provisional decision records.
- Depends On: [../../00_BUSINESS_FLOW.md](../../00_BUSINESS_FLOW.md), [../../01_NODE_CONTRACTS.md](../../01_NODE_CONTRACTS.md), [../../05_MARKET_SIGNAL_TOOL_CONTRACT.md](../../05_MARKET_SIGNAL_TOOL_CONTRACT.md), [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Pending Andy Review

## Authority Note

This log records decision history. It cannot override higher-level business sources or architecture contracts. Decisions not approved by Andy must remain marked `Provisional`. Later decisions must not delete old decisions; they should use `Supersedes` to replace earlier decisions.

## Template

```text
## SIG-D-XXX

- Date:
- Status:
- Decision:
- Context:
- Rationale:
- Alternatives Considered:
- Consequences:
- Affected Documents:
- Supersedes:
- Approved By:
```

## SIG-D-001

- Date: 2026-08-06
- Status: Provisional
- Decision: Establish the full SIG-0 to SIG-P6 system blueprint while keeping current implementation work as one minimal approved slice.
- Context: Track C needs a complete direction without turning future capabilities into current scope.
- Rationale: Preserving the full map prevents P0-only design drift.
- Alternatives Considered: Design only SIG-P0 now; postpone all future stages.
- Consequences: Future stages are visible but remain unapproved for implementation.
- Affected Documents: [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-002

- Date: 2026-08-06
- Status: Provisional
- Decision: SIG-P0 should first verify JSON / CSV export input; API adapter comes later, but both must share one normalization pipeline.
- Context: Data source fields and API behavior are not yet verified.
- Rationale: Export-first reduces integration risk and keeps the canonical pipeline stable.
- Alternatives Considered: Start with live API adapter; maintain separate API and export normalizers.
- Consequences: Later implementation must avoid duplicate normalization logic.
- Affected Documents: [02_DATA_SOURCE_CAPABILITY_MAP.md](02_DATA_SOURCE_CAPABILITY_MAP.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-003

- Date: 2026-08-06
- Status: Provisional
- Decision: Distinguish `CollectionRun`, `RawRecord`, `PlatformVideoIdentity`, and `NormalizedVideoSignal`.
- Context: Raw rows, platform identity, run snapshots, and normalized signals have different business meanings.
- Rationale: Clear object boundaries protect traceability and metric history.
- Alternatives Considered: Treat each raw row as the final video signal.
- Consequences: P0 implementation must preserve object relationships.
- Affected Documents: [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-004

- Date: 2026-08-06
- Status: Provisional
- Decision: Merge same-run records by platform video identity; preserve separate metric snapshots across runs.
- Context: The same video can appear under multiple queries or across different collection times.
- Rationale: Same-run merging avoids double counting; cross-run preservation protects historical metrics.
- Alternatives Considered: Always merge by video ID across all time; never merge duplicates.
- Consequences: P0 needs explicit run identity and snapshot semantics.
- Affected Documents: [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-005

- Date: 2026-08-06
- Status: Provisional
- Decision: Replace a single `query` assumption with `matched_queries` and preserve `raw_record_refs`.
- Context: One video can be found by multiple query terms in the same run.
- Rationale: Query overlap is both a dedupe concern and a retrieval coverage signal.
- Alternatives Considered: Keep only the first query; duplicate the video for each query.
- Consequences: Normalized signals must support multiple matched queries and record-level raw traceability.
- Affected Documents: [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-006

- Date: 2026-08-06
- Status: Provisional
- Decision: Distinguish `signal_id` from `platform_video_id`.
- Context: A platform video can have multiple SIG-P0 metric snapshots across runs.
- Rationale: Platform identity and signal snapshot identity answer different questions.
- Alternatives Considered: Use platform video ID as the only signal ID.
- Consequences: Reports can preserve time-specific snapshots without overwriting history.
- Affected Documents: [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-007

- Date: 2026-08-06
- Status: Provisional
- Decision: SIG-P0 covers only L1/L2; L3/L4 remain future stages.
- Context: P0 public video data cannot safely represent commercial conversion or own business validation.
- Rationale: Prevents schema and interpretation overreach.
- Alternatives Considered: Add public commerce and own business fields to P0.
- Consequences: L3 and L4 are designed in the blueprint but not included in P0 schema.
- Affected Documents: [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-008

- Date: 2026-08-06
- Status: Provisional
- Decision: SIG-P0 must not automatically modify or approve `ResearchTask`.
- Context: `ResearchTask` is human-owned through Track A and must preserve manual decision rights.
- Rationale: Market signals support `ResearchBasis`; they do not replace human judgment.
- Alternatives Considered: Let SIG-P0 recommend and write audience/scenario/lens choices directly.
- Consequences: SIG-P0 output can only be referenced through `signal_report_ref`.
- Affected Documents: [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md), [../../06_CROSS_TRACK_MESSAGE_CONTRACTS.md](../../06_CROSS_TRACK_MESSAGE_CONTRACTS.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-009

- Date: 2026-08-06
- Status: Provisional
- Decision: Public video data must not be interpreted as true buying audience, true conversion rate, true GMV attribution, or guaranteed creative success.
- Context: Public content data mainly supports supply and performance observation.
- Rationale: Prevents causal and commercial overclaiming.
- Alternatives Considered: Treat public performance as direct market proof.
- Consequences: Reports must include prohibited overclaims and limitations.
- Affected Documents: [01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-010

- Date: 2026-08-06
- Status: Provisional
- Decision: Complete the whole-system blueprint and P0 business contract before entering code implementation.
- Context: Current task is documentation only and not SIG-P0 implementation.
- Rationale: Contract review should happen before schema or adapter decisions become accidental facts.
- Alternatives Considered: Start code immediately and adjust documents later.
- Consequences: No SIG source code, API calls, schemas, tests, database, UI, or CLI are created in this round.
- Affected Documents: [CURRENT_STATUS.md](CURRENT_STATUS.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-011

- Date: 2026-08-06
- Status: Provisional
- Decision: Add `QueryExecution` as the per-query execution record inside a `CollectionRun`.
- Context: A zero-result query and a failed query must not be treated as the same business outcome.
- Rationale: P0 needs to know which endpoint and query actually ran, how many raw records were retrieved, and whether the execution succeeded, partially succeeded, failed, or was skipped.
- Alternatives Considered: Store only final normalized videos; store only the submitted query strings.
- Consequences: Later P0 design must preserve execution status and raw record traceability per query.
- Affected Documents: [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md), [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-012

- Date: 2026-08-06
- Status: Provisional
- Decision: Add `ProcessingRun` to separate data collection from normalization, deduplication, classification, statistics, and report generation.
- Context: The same raw dataset may be reprocessed under different rule versions without creating a fake new collection event.
- Rationale: Collection and processing answer different audit questions: what was collected versus which rule versions processed it.
- Alternatives Considered: Treat every reprocessing as a new `CollectionRun`; overwrite old normalized outputs.
- Consequences: `NormalizedVideoSignal` and `MarketSignalReport` must bind to a specific `ProcessingRun`.
- Affected Documents: [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md), [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Supersedes: SIG-D-003 partial extension. SIG-D-003 remains active, and SIG-D-012 extends its object system.
- Approved By: Pending Andy Review

## SIG-D-013

- Date: 2026-08-06
- Status: Provisional
- Decision: Separate input `queries`, execution-level `QueryExecution`, and derived `matched_queries`.
- Context: Submitted queries, execution outcomes, and video-level query hits are different business facts.
- Rationale: Final normalized results alone cannot prove which query ran successfully or failed.
- Alternatives Considered: Use `matched_queries` as both input and output; infer query execution only from normalized videos.
- Consequences: Candidate inputs keep `queries`; `matched_queries` remains a derived field on normalized video signals.
- Affected Documents: [01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md), [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md), [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Supersedes: SIG-D-005 partial extension. SIG-D-005 remains active for `matched_queries` and `raw_record_refs`, while SIG-D-013 clarifies input and execution semantics.
- Approved By: Pending Andy Review

## SIG-D-014

- Date: 2026-08-06
- Status: Provisional
- Decision: Treat SIG-P3 public shop/product/review/showcase data as `Commercial Visibility - L3-adjacent`, not verified L3 conversion evidence.
- Context: Public commercial surfaces do not automatically provide verified clicks, add-to-cart, transactions, sales volume, or ad conversion semantics.
- Rationale: This prevents public visibility from being mislabeled as commercial conversion proof.
- Alternatives Considered: Keep the earlier wording that treated public commercial surfaces too close to formal conversion evidence.
- Consequences: TikTok Shop visibility remains future SIG-P3 design until real conversion metric semantics are verified and approved.
- Affected Documents: [README.md](README.md), [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md), [02_DATA_SOURCE_CAPABILITY_MAP.md](02_DATA_SOURCE_CAPABILITY_MAP.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-015

- Date: 2026-08-06
- Status: Provisional
- Decision: Rename `recommended_research_basis_summary` to `research_basis_evidence_summary` to avoid automatic recommendation semantics.
- Context: P0 can summarize evidence but must not decide or approve `ResearchTask` fields.
- Rationale: The new name keeps the report in an evidence-support role.
- Alternatives Considered: Keep recommendation wording with caveats.
- Consequences: P0 reports should summarize observations, sample size, refs, limitations, and questions for human review.
- Affected Documents: [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-016

- Date: 2026-08-06
- Status: Provisional
- Decision: Keep Search Suggestions in Future SIG-P1 and separate User's Audience Demographics from creator-size analysis.
- Context: Search Suggestions helps future query discovery but is not a P0 core pipeline object; audience demographics can mislead creator-size analysis into audience claims.
- Rationale: P0 should not expand scope just because a source is useful for manual research, and audience estimates must not become buyer claims.
- Alternatives Considered: Keep earlier optional P0 wording for Search Suggestions; use audience demographic estimates in creator-size analysis.
- Consequences: Search Suggestions is Future P1, and User's Audience Demographics gets a separate limited-use C05 question.
- Affected Documents: [01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md), [02_DATA_SOURCE_CAPABILITY_MAP.md](02_DATA_SOURCE_CAPABILITY_MAP.md), [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-017

- Date: 2026-08-07
- Status: Approved
- Decision: Approve and archive SIG System Blueprint V0.1, Business Question And Evidence Map V0.1, and Data Source Capability Map V0.1 as the Track C architecture and reconnaissance baseline.
- Context: The three Track C V0.1 baseline documents have reached a stable review point for architecture direction, business question/evidence mapping, and data source reconnaissance framing.
- Rationale: Approved baselines need immutable archive snapshots before further reconnaissance documentation and later API testing.
- Alternatives Considered: Continue editing without archive; approve only the current live files without immutable snapshot.
- Consequences: The approved V0.1 baseline is archived, while maintained current documents remain under `docs/tracks/sig_market_signal/`.
- Affected Documents: [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md), [01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md), [02_DATA_SOURCE_CAPABILITY_MAP.md](02_DATA_SOURCE_CAPABILITY_MAP.md), [../../archive/tracks/sig_market_signal/v0.1/ARCHIVE_MANIFEST.md](../../archive/tracks/sig_market_signal/v0.1/ARCHIVE_MANIFEST.md)
- Supersedes: None
- Approved By: Andy
- Approval Date: 2026-08-07
- Approval Boundary: This approval does not include API real capability, API fields, API parameters, pricing, pagination, ranking, metric semantics, SIG-P0 implementation contract, or code implementation.

## SIG-D-018

- Date: 2026-08-06
- Status: Provisional
- Decision: The Scrape Creators reconnaissance campaign must cover all 29 currently observed endpoints across TikTok, TikTok Shop, and TikTok Ad Library.
- Context: Endpoint testing must not disappear simply because an endpoint is outside current SIG-P0 core candidates.
- Rationale: Complete reconnaissance requires a full capability map with evidence-backed status for every observed endpoint.
- Alternatives Considered: Test only P0 core candidates first and leave future endpoints out of the campaign.
- Consequences: Future-stage endpoints remain in the matrix and report.
- Affected Documents: [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md), [05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md), [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-019

- Date: 2026-08-06
- Status: Provisional
- Decision: The campaign may execute endpoints in dependency order, but completion requires a final evidence-backed status for every endpoint; testing only the four P0 core candidates is not complete reconnaissance.
- Context: Some endpoints depend on seed identities from other endpoints.
- Rationale: Dependency order is execution sequencing, not scope reduction.
- Alternatives Considered: Declare campaign complete after testing Search by Keyword, Search by Hashtag, Video Info, and Transcript.
- Consequences: Completion criteria require all 29 endpoint statuses and evidence-backed conclusions.
- Affected Documents: [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md), [05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md), [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-020

- Date: 2026-08-06
- Status: Provisional
- Decision: Every actual endpoint call must preserve redacted request evidence, immutable raw response evidence, hashes, field observations, limitations, and a capability verdict.
- Context: Later field and capability decisions must be auditable.
- Rationale: Evidence records prevent endpoint names, UI labels, or inferred behavior from becoming false facts.
- Alternatives Considered: Keep only summarized notes from manual testing.
- Consequences: Actual testing must produce request, response, hash, field observation, and verdict records.
- Affected Documents: [06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md](06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md), [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-021

- Date: 2026-08-06
- Status: Provisional
- Decision: Blocked, unavailable, rejected, and not-applicable endpoints remain part of the final report and must not be silently omitted.
- Context: Non-success outcomes are still business evidence for capability boundaries.
- Rationale: Omitted endpoints create false completeness and future integration risk.
- Alternatives Considered: Remove blocked or rejected endpoints from the final report.
- Consequences: Every endpoint remains visible with status, evidence, reason, and capability verdict.
- Affected Documents: [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md), [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-022

- Date: 2026-08-07
- Status: Approved
- Decision: Live Scrape Creators reconnaissance requires an approved Campaign Budget And Safety Gate before API calls begin.
- Context: Complete reconnaissance must not become unlimited requests or uncontrolled cost.
- Rationale: Budget, request, page, quota, and stop gates must be explicit before live testing.
- Alternatives Considered: Begin live testing and monitor manually without documented stop gates.
- Consequences: Live API testing remains blocked until real approved budget values are filled.
- Affected Documents: [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md), [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md), [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Supersedes: None
- Approved By: Andy
- Approval Date: 2026-08-07

## SIG-D-023

- Date: 2026-08-07
- Status: Approved
- Decision: A successful positive case is required only when prerequisite, authorization, plan access, quota, and safe legal input are available; otherwise evidence-backed blocked or unavailable status can complete current reconnaissance for that endpoint.
- Context: Some endpoints may require inaccessible seed entities, plan permissions, quota, or human approval.
- Rationale: Complete reconnaissance requires evidence-backed status for every endpoint, not forced unsafe or impossible calls.
- Alternatives Considered: Require at least one success call for every endpoint regardless of access boundaries.
- Consequences: Blocked, unavailable, not applicable, or deferred endpoints can complete current reconnaissance only with evidence, reason, remaining unknowns, and mapped verdict.
- Affected Documents: [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md), [05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md), [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md)
- Supersedes: None
- Approved By: Andy
- Approval Date: 2026-08-07

## SIG-D-024

- Date: 2026-08-07
- Status: Approved
- Decision: Replace binary repeated snapshot testing with Required / Conditional / Not Applicable and require an endpoint-specific rationale.
- Context: Repeated calls are not equally useful for every endpoint and must stay inside budget and quota limits.
- Rationale: Snapshot testing should be tied to metric volatility, live behavior, changing feeds, or first-response evidence.
- Alternatives Considered: Keep a mechanical Yes / No repeated snapshot field.
- Consequences: The endpoint matrix records `snapshot_retest_requirement` and `snapshot_retest_rationale` for all 29 endpoints.
- Affected Documents: [05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md), [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md)
- Supersedes: None
- Approved By: Andy
- Approval Date: 2026-08-07

## SIG-D-025

- Date: 2026-08-07
- Status: Approved
- Decision: Do not persist raw HTTP requests. Persist only canonical redacted request evidence; raw responses remain protected separately and must undergo sensitive-data review before any Git decision.
- Context: Requests can carry API keys, authorization headers, cookies, query-string secrets, signatures, and account-control material.
- Rationale: Audit value can be preserved through canonical redacted request evidence without storing secret-bearing raw requests.
- Alternatives Considered: Store raw requests and rely on later redaction.
- Consequences: Current contracts use `canonical_redacted_request_artifact_path` and `canonical_request_fingerprint`, while raw responses remain separate and protected.
- Affected Documents: [06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md](06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md), [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md)
- Supersedes: SIG-D-020 partial refinement. SIG-D-020 remains active for response evidence, hashes, field observations, limitations, and verdicts.
- Approved By: Andy
- Approval Date: 2026-08-07

## SIG-D-026

- Date: 2026-08-07
- Status: Approved
- Decision: Test Status and Capability Verdict remain separate and must follow an explicit legal mapping before the campaign can be marked complete.
- Context: Endpoint execution states and business capability decisions answer different questions.
- Rationale: Final capability verdicts must not contain temporary test or governance statuses such as Pending Test, Not Run, Endpoint Unavailable, Not Applicable, or Deferred.
- Alternatives Considered: Let report authors choose verdicts freely after testing.
- Consequences: The result recording contract defines allowed Test Status to Capability Verdict combinations, and the final report includes a consistency check.
- Affected Documents: [06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md](06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md), [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md), [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Supersedes: None
- Approved By: Andy
- Approval Date: 2026-08-07

## SIG-D-027

- Date: 2026-08-07
- Status: Provisional
- Decision: Establish `08_SCRAPE_CREATORS_REQUEST_SURFACE_BASELINE.md` as the canonical observed request-side evidence baseline for all 29 currently observed Scrape Creators endpoints.
- Context: Andy manually collected the provider endpoint routes, UI parameter surfaces, visible required markers, enums, descriptions, and selected cost/support notes before runtime API reconnaissance.
- Rationale: Future work should validate runtime behavior instead of repeatedly rediscovering provider request-surface facts.
- Alternatives Considered: Leave observed request-side facts spread across chat context and require recollection before runtime testing.
- Consequences: Runtime reconnaissance may supersede or refine observed request assumptions, but must record discrepancies rather than silently rewriting evidence history.
- Affected Documents: [08_SCRAPE_CREATORS_REQUEST_SURFACE_BASELINE.md](08_SCRAPE_CREATORS_REQUEST_SURFACE_BASELINE.md), [05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md), [README.md](README.md), [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Supersedes: None
- Approved By: Pending Andy Review

## SIG-D-028

- Date: 2026-08-07
- Status: Approved
- Decision: Runtime reconnaissance uses dependency waves, differentiated test depth, shared Seed Registry, standardized eight-block findings, and a final cross-endpoint identity map.
- Context: The request-side baseline is available, but live runtime testing still needs a concrete execution plan before any API campaign begins.
- Rationale: Dependency waves avoid fabricated seeds, differentiated depth limits cost and risk, standardized result blocks keep findings comparable, and the identity map makes cross-endpoint linkage reviewable.
- Alternatives Considered: Execute endpoints in flat numeric order; test every endpoint at identical depth; record free-form notes without a shared seed or identity map.
- Consequences: Runtime testing must follow the execution plan unless Andy explicitly approves a change, and campaign completion requires endpoint conclusions plus final identity and verdict artifacts.
- Affected Documents: [09_SCRAPE_CREATORS_RUNTIME_RECONNAISSANCE_EXECUTION_PLAN.md](09_SCRAPE_CREATORS_RUNTIME_RECONNAISSANCE_EXECUTION_PLAN.md), [05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md), [CURRENT_STATUS.md](CURRENT_STATUS.md), [README.md](README.md)
- Supersedes: None
- Approved By: Andy
- Approval Date: 2026-08-07

## SIG-D-029

- Date: 2026-08-07
- Status: Approved
- Decision: Approve the initial Scrape Creators Runtime Reconnaissance Campaign Budget Gate with campaign_credit_budget_max = 2000 credits, campaign_request_budget_max = 150 requests, default_endpoint_request_cap = 5 requests, default_pagination_page_cap = 3 pages, repeated_snapshot_request_cap = 2 additional requests, minimum_remaining_quota_threshold = 22000 credits, additional_budget_requires_human_approval = true, and campaign_currency_budget_max = Unknown / Not Observable.
- Context: The observed Scrape Creators balance snapshot on 2026-08-07 was 24,343 credits. Known endpoint prices are heterogeneous: TT-03 is explicitly shown as 26 credits/request and SHOP-02 as 1 credit/request, while most endpoint costs remain unknown.
- Rationale: The first full 29-endpoint reconnaissance requires enough budget for Level 1 coverage plus selective Level 2/3 testing while preventing uncontrolled credit consumption.
- Alternatives Considered: Keep Budget Gate pending; approve only request count without credit limits; use the historical 24,343-credit snapshot as runtime configuration.
- Consequences: The limits are ceilings, not targets. Tests must stop early when sufficient evidence is obtained. Any limit increase requires explicit Andy approval. Runtime must re-observe the actual starting credit balance. Campaign stops when either campaign budget, request budget, or minimum remaining-credit threshold is reached. Unexpected high-cost behavior requires human review.
- Affected Documents: [09_SCRAPE_CREATORS_RUNTIME_RECONNAISSANCE_EXECUTION_PLAN.md](09_SCRAPE_CREATORS_RUNTIME_RECONNAISSANCE_EXECUTION_PLAN.md), [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md), [06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md](06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md), [CURRENT_STATUS.md](CURRENT_STATUS.md), [README.md](README.md)
- Supersedes: None
- Approved By: Andy
- Approval Date: 2026-08-07
