# Docs Navigation

- Version: V0.1
- Status: Draft
- Authority: Documentation Index
- Scope: Documentation map, authority levels, conflict handling, and current implementation boundaries.
- Depends On: [00_BUSINESS_FLOW.md](00_BUSINESS_FLOW.md), [01_NODE_CONTRACTS.md](01_NODE_CONTRACTS.md), [02_GUIDED_IMPLEMENTATION_PLAN.md](02_GUIDED_IMPLEMENTATION_PLAN.md), [03_PARALLEL_DEVELOPMENT_TRACKS.md](03_PARALLEL_DEVELOPMENT_TRACKS.md), [04_KNOWLEDGE_CATALOG_CONTRACT.md](04_KNOWLEDGE_CATALOG_CONTRACT.md), [05_MARKET_SIGNAL_TOOL_CONTRACT.md](05_MARKET_SIGNAL_TOOL_CONTRACT.md), [06_CROSS_TRACK_MESSAGE_CONTRACTS.md](06_CROSS_TRACK_MESSAGE_CONTRACTS.md)
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Pending Andy Review

## Purpose

This page is the navigation entry for the `docs/` directory. It explains which documents define business facts, which documents define development method and architecture contracts, and where Track C SIG Market & Business Signal System designs live.

It does not replace the business sources. It only summarizes document responsibilities and provides links.

## Documentation Authority Levels

| Level | Authority | Documents | Role |
|---|---|---|---|
| Level 1 | Business Sources | [00_BUSINESS_FLOW.md](00_BUSINESS_FLOW.md), [01_NODE_CONTRACTS.md](01_NODE_CONTRACTS.md) | Define N01-N18 order, fallback paths, human gates, node inputs, outputs, decision rights, and acceptance criteria. |
| Level 2 | Development Method / Architecture Contracts | [02_GUIDED_IMPLEMENTATION_PLAN.md](02_GUIDED_IMPLEMENTATION_PLAN.md), [03_PARALLEL_DEVELOPMENT_TRACKS.md](03_PARALLEL_DEVELOPMENT_TRACKS.md), [04_KNOWLEDGE_CATALOG_CONTRACT.md](04_KNOWLEDGE_CATALOG_CONTRACT.md), [05_MARKET_SIGNAL_TOOL_CONTRACT.md](05_MARKET_SIGNAL_TOOL_CONTRACT.md), [06_CROSS_TRACK_MESSAGE_CONTRACTS.md](06_CROSS_TRACK_MESSAGE_CONTRACTS.md) | Define implementation discipline, parallel track boundaries, catalog contracts, signal tool contract, and cross-track message formats. |
| Level 3 | Track Detailed Designs | [tracks/sig_market_signal/README.md](tracks/sig_market_signal/README.md) and related Track C design files | Preserve Track C detailed design and SIG-P0 contract framework without changing higher-level business meaning. |
| Level 4 | Working Records | [context_packs/TRACK_C_SIGP0_CONTEXT.md](context_packs/TRACK_C_SIGP0_CONTEXT.md), [tracks/sig_market_signal/DECISION_LOG.md](tracks/sig_market_signal/DECISION_LOG.md), [tracks/sig_market_signal/CURRENT_STATUS.md](tracks/sig_market_signal/CURRENT_STATUS.md), unapproved discussion notes | Record current work state, provisional decisions, and review history. Working records cannot override formal contracts. |

## Existing Core Documents

| Document | Responsibility | Authority Type |
|---|---|---|
| [00_BUSINESS_FLOW.md](00_BUSINESS_FLOW.md) | Defines the N01-N18 business sequence, fallback paths, human gates, support layers, and key invariants. | Business Source |
| [01_NODE_CONTRACTS.md](01_NODE_CONTRACTS.md) | Defines each N01-N18 node's input, processing, output, decision rights, MVP mode, and acceptance criteria. | Business Source |
| [02_GUIDED_IMPLEMENTATION_PLAN.md](02_GUIDED_IMPLEMENTATION_PLAN.md) | Defines visual review-driven implementation method, roles, review format, and slice discipline. | Development Method |
| [03_PARALLEL_DEVELOPMENT_TRACKS.md](03_PARALLEL_DEVELOPMENT_TRACKS.md) | Defines Track A, Track B, and Track C boundaries and parallel development rules. | Architecture Contract |
| [04_KNOWLEDGE_CATALOG_CONTRACT.md](04_KNOWLEDGE_CATALOG_CONTRACT.md) | Defines K-P0 knowledge catalog fields, refs, version rules, and manual approval rules. | Architecture Contract |
| [05_MARKET_SIGNAL_TOOL_CONTRACT.md](05_MARKET_SIGNAL_TOOL_CONTRACT.md) | Defines SIG-P0 market signal tool scope, L1-L4 signal layers, P0 fields, and interpretation boundaries. | Architecture Contract |
| [06_CROSS_TRACK_MESSAGE_CONTRACTS.md](06_CROSS_TRACK_MESSAGE_CONTRACTS.md) | Defines cross-track references and message formats such as `knowledge_ref`, `signal_report_ref`, `ResearchBasis`, and `MarketSignalReport P0`. | Architecture Contract |

## Track C Entry

Track C documents live under [tracks/sig_market_signal/](tracks/sig_market_signal/).

Recommended entry point:

1. [tracks/sig_market_signal/README.md](tracks/sig_market_signal/README.md)
2. [tracks/sig_market_signal/00_SIG_SYSTEM_BLUEPRINT.md](tracks/sig_market_signal/00_SIG_SYSTEM_BLUEPRINT.md)
3. [tracks/sig_market_signal/01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](tracks/sig_market_signal/01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md)
4. [tracks/sig_market_signal/02_DATA_SOURCE_CAPABILITY_MAP.md](tracks/sig_market_signal/02_DATA_SOURCE_CAPABILITY_MAP.md)
5. [tracks/sig_market_signal/03_SIG_P0_DETAILED_CONTRACT.md](tracks/sig_market_signal/03_SIG_P0_DETAILED_CONTRACT.md)
6. [tracks/sig_market_signal/04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](tracks/sig_market_signal/04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md)
7. [tracks/sig_market_signal/05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](tracks/sig_market_signal/05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md)
8. [tracks/sig_market_signal/06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md](tracks/sig_market_signal/06_SCRAPE_CREATORS_RESULT_RECORDING_CONTRACT.md)
9. [tracks/sig_market_signal/08_SCRAPE_CREATORS_REQUEST_SURFACE_BASELINE.md](tracks/sig_market_signal/08_SCRAPE_CREATORS_REQUEST_SURFACE_BASELINE.md)
10. [tracks/sig_market_signal/09_SCRAPE_CREATORS_RUNTIME_RECONNAISSANCE_EXECUTION_PLAN.md](tracks/sig_market_signal/09_SCRAPE_CREATORS_RUNTIME_RECONNAISSANCE_EXECUTION_PLAN.md)
11. [tracks/sig_market_signal/07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md](tracks/sig_market_signal/07_SCRAPE_CREATORS_RECONNAISSANCE_REPORT.md)
12. [tracks/sig_market_signal/DECISION_LOG.md](tracks/sig_market_signal/DECISION_LOG.md)
13. [tracks/sig_market_signal/CURRENT_STATUS.md](tracks/sig_market_signal/CURRENT_STATUS.md)

The request surface baseline records observed request-side provider evidence for all 29 Scrape Creators endpoints before runtime API reconnaissance.

The runtime reconnaissance execution plan defines dependency waves, differentiated test depth, Seed Registry, standardized result blocks, and cross-endpoint identity mapping before any live API campaign.

Approved Track C V0.1 archive:

- [archive/tracks/sig_market_signal/v0.1/ARCHIVE_MANIFEST.md](archive/tracks/sig_market_signal/v0.1/ARCHIVE_MANIFEST.md)
- [archive/tracks/sig_market_signal/v0.1/00_SIG_SYSTEM_BLUEPRINT.md](archive/tracks/sig_market_signal/v0.1/00_SIG_SYSTEM_BLUEPRINT.md)
- [archive/tracks/sig_market_signal/v0.1/01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md](archive/tracks/sig_market_signal/v0.1/01_BUSINESS_QUESTION_AND_EVIDENCE_MAP.md)
- [archive/tracks/sig_market_signal/v0.1/02_DATA_SOURCE_CAPABILITY_MAP.md](archive/tracks/sig_market_signal/v0.1/02_DATA_SOURCE_CAPABILITY_MAP.md)

The archive is an immutable approval snapshot. The current maintained Track C documents remain under [tracks/sig_market_signal/](tracks/sig_market_signal/), and maintenance changes must not silently overwrite archived versions.

## Working Records vs Formal Contracts

Working records preserve context, active decisions, parked work, and review notes. They are useful for continuity across conversations, but they cannot redefine business facts, node contracts, or approved architecture contracts.

Formal contracts define stable boundaries and are higher authority than working records. `CURRENT_STATUS.md` can summarize current work, but it must not override [05_MARKET_SIGNAL_TOOL_CONTRACT.md](05_MARKET_SIGNAL_TOOL_CONTRACT.md), [06_CROSS_TRACK_MESSAGE_CONTRACTS.md](06_CROSS_TRACK_MESSAGE_CONTRACTS.md), or any Level 1 business source.

## Conflict Handling

If two documents conflict:

1. Higher authority wins over lower authority.
2. Lower-level documents must not silently change higher-level business meaning.
3. If Level 1 business sources conflict with each other, development stops for the affected topic.
4. Prompt text, code, schema, tests, and Track detailed designs must not become the new highest business source.
5. Conflicts that require Andy's decision must be listed in the completion report or the relevant working record.

## Document Status Meaning

| Status | Meaning |
|---|---|
| Draft | Written for review; not approved. |
| Under Review | Actively being reviewed by Andy. |
| Approved | Approved by Andy and usable as the current contract at its authority level. |
| Superseded | Replaced by a newer document or decision. |
| Working Note | Operational note or status record; cannot override contracts. |

## Current Implementation Scope vs Whole-System Blueprint

The whole-system blueprint may describe future stages so the project does not lose direction. That does not mean those stages are approved for implementation.

Current code must still implement one approved minimal slice at a time. A Preliminary Design is not an approved development scope. Track C SIG-P0 can prepare a detailed contract framework, but SIG-P1 through SIG-P6 remain future design unless explicitly approved later.
