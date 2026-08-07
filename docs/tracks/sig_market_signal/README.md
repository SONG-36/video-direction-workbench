# Track C SIG Market Signal

- Version: V0.1
- Status: Draft
- Authority: Documentation Index
- Scope: Track C navigation, scope boundaries, stage overview, active work, and parked work.
- Depends On: [../../00_BUSINESS_FLOW.md](../../00_BUSINESS_FLOW.md), [../../01_NODE_CONTRACTS.md](../../01_NODE_CONTRACTS.md), [../../03_PARALLEL_DEVELOPMENT_TRACKS.md](../../03_PARALLEL_DEVELOPMENT_TRACKS.md), [../../05_MARKET_SIGNAL_TOOL_CONTRACT.md](../../05_MARKET_SIGNAL_TOOL_CONTRACT.md), [../../06_CROSS_TRACK_MESSAGE_CONTRACTS.md](../../06_CROSS_TRACK_MESSAGE_CONTRACTS.md), [../../context_packs/TRACK_C_SIGP0_CONTEXT.md](../../context_packs/TRACK_C_SIGP0_CONTEXT.md)
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Pending Andy Review

## Business Position

Track C is the SIG Market & Business Signal System. It is responsible for market and business signals that can support operating decisions, research basis selection, search planning, and later controlled knowledge feedback.

SIG does not replace `ProductBrief`. SIG does not automatically modify `ResearchTask`. SIG does not automatically approve audience, scenario, pain point, or lens choices. SIG does not generate formal `SearchPlan`, creative directions, or scripts.

## Current And Future Scope

Current Track C work only builds the documentation framework and whole-system blueprint. There is no SIG source code, no API call, no schema implementation, no database, no UI, and no CLI in this round.

SIG-P0 currently covers:

- L1 Content Supply Signals
- L2 Content Performance Signals

Future stages may cover:

- L3 Commercial Conversion Signals
- L4 Own Business Validation Signals
- Cross-layer evidence support
- Controlled knowledge and rule feedback through N18

## Document Navigation

| Document | Responsibility | Authority |
|---|---|---|
| [00_SIG_SYSTEM_BLUEPRINT.md](00_SIG_SYSTEM_BLUEPRINT.md) | Whole SIG-0 to SIG-P6 system blueprint and maturity map. | Preliminary Design |
| [01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md) | Maps business questions to evidence, signal layers, allowed statements, and prohibited overclaims. | Preliminary Design |
| [02_DATA_SOURCE_CAPABILITY_MAP.md](02_DATA_SOURCE_CAPABILITY_MAP.md) | Maps observed Scrape Creators endpoint names to candidate purposes and verification needs without inventing fields. | Preliminary Design |
| [03_SIG_P0_DETAILED_CONTRACT.md](03_SIG_P0_DETAILED_CONTRACT.md) | Draft detailed contract framework for SIG-P0 review. | Detailed Contract |
| [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md) | Complete 29-endpoint reconnaissance campaign plan before API testing. | Detailed Test Plan |
| [05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md) | Endpoint-by-endpoint test matrix for all observed Scrape Creators endpoints. | Test Matrix |
| [06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md](06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md) | Evidence recording, redaction, hashing, and verdict contract for later tests. | Evidence Recording Contract |
| [07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md) | Final report template for the full reconnaissance campaign. | Working Test Report |
| [DECISION_LOG.md](DECISION_LOG.md) | Track C decision history and provisional decisions. | Working Record |
| [CURRENT_STATUS.md](CURRENT_STATUS.md) | Current Track C work state and next review. | Working Record |

## SIG-0 To SIG-P6 Stage Overview

| Stage | Purpose | Signal Layer | Current Maturity | Current / Future |
|---|---|---|---|---|
| SIG-0 | Business question and data source map. | Cross-layer planning | Preliminary Design | Current design foundation |
| SIG-P0 | Public content supply and performance foundation. | L1/L2 | Detailed Contract In Progress - Structural Rework | Current contract framework |
| SIG-P1 | Public content ecosystem expansion. | L1/L2 | Preliminary Design | Future |
| SIG-P2 | Public ad and driver structure hypotheses. | L1/L2 plus driver hypotheses | Preliminary Design | Future |
| SIG-P3 | Public commercial visibility signals. | Commercial Visibility / L3-adjacent | Preliminary Design | Future |
| SIG-P4 | Own business validation. | L4 | Preliminary Design | Future |
| SIG-P5 | Cross-layer evidence and decision support. | L1-L4 comparison | Concept / Preliminary Design | Future |
| SIG-P6 | Controlled knowledge and rule feedback. | N18-governed feedback | Concept / Preliminary Design | Future |

## Current Maturity

| Area | Maturity | Notes |
|---|---|---|
| Whole SIG Blueprint | Approved V0.1 | Preserves full direction, not implementation approval. |
| Business Question & Evidence Map | Approved V0.1 | Approved evidence-layer framework. |
| Data Source Capability Map | Approved Reconnaissance Framework V0.1 | Endpoint names are observed; details are Unverified. |
| SIG-P0 Detailed Contract | Draft | Framework only; not Implementation Ready. |
| Scrape Creators Reconnaissance Plan | Draft — Final Governance Review | Covers all 29 currently observed endpoints. |
| Endpoint Test Matrix | Draft, Pending Review | All 29 endpoints start as Not Run. |
| Result Recording Contract | Draft, Pending Review | Defines request, raw response, redacted evidence, hash, and verdict records. |
| Reconnaissance Report | Not Run | Cannot be complete until all 29 endpoints have final evidence-backed status. |
| SIG code | Not Started | Not in this round. |
| Scrape Creators API integration | Not Started | Not in this round. |

## Relationship With Other Tracks And Nodes

| Related Area | Relationship |
|---|---|
| Track A N02A | Uses `signal_report_ref` inside `ResearchBasis.supporting_signal_refs`; Track C must not edit or approve `ResearchTask`. |
| Track B K-P0 | Provides read-only tag definitions and `knowledge_refs`; Track C must not modify K-P0. |
| N03 | May use `MarketSignalReport P0` as support for search strategy, but SIG does not generate formal `SearchPlan`. |
| N17 | Provides own business performance and review data for future L4 validation. |
| N18 | Controls official knowledge and rule feedback with human approval. SIG cannot update rules directly. |

## Active Work

Final reconnaissance governance rework.

CollectionRun, QueryExecution, and ProcessingRun have different responsibilities and must not be collapsed into one generic run object.

Later live testing must cover all 29 currently observed endpoints. Tests may execute in dependency order, but testing only the four P0 core endpoints is not complete reconnaissance.

A complete 29-endpoint campaign means every endpoint receives an evidence-backed final status and business capability verdict; it does not mean unlimited requests or identical test depth for every endpoint.

## Parked Work

- Track A N02A
- Track B full K-P0 design
- N03
- SIG source code implementation
- Scrape Creators API integration
- Database
- UI
- Agent orchestration

## Reading Order

1. Start with this README.
2. Review the whole-system blueprint.
3. Review the business question and evidence map.
4. Review the data source capability map.
5. Review the SIG-P0 detailed contract framework.
6. Check the decision log and current status.

## Non-Goals

- No code implementation.
- No Scrape Creators API calls.
- No SIG-P0 field final freeze.
- No N02A, K-P0, N03, N17, or N18 development.
- No ResearchTask modification.
- No knowledge base update.
- No automatic approval of audiences, scenarios, pain points, lenses, or rules.
