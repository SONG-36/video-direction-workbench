# TRACK C SIGP0 CONTEXT

## Project Path

`/Volumes/server-data/projects/andy/0803/video-direction-workbench`

## Current Task

SIG-P0 Market Signal Tool.

## Signal Layers

- L1 Content Supply Signals
- L2 Content Performance Signals
- L3 Commercial Conversion Signals
- L4 Own Business Validation Signals

Current SIG-P0 only covers L1/L2. L3/L4 are future extensions.

## Allowed Scope

- Developer script or experiment entry
- Scrape Creators API adapter or exported data reader
- raw response saving
- normalized video signal output
- deduplication
- basic field normalization
- simple rule classification using K-P0 tags
- basic statistics
- MarketSignalReport P0 output
- limitations output

## Forbidden

- Automatically modifying ResearchTask
- Automatically approving audience/scenario/lens
- Formal UI
- Formal productized CLI
- Database
- Formal SearchPlan generation
- Video structured analysis
- Creative direction
- Script generation
- Automatic knowledge base update

## MarketSignalReport P0 Output Fields

- report_id
- generated_at
- provider
- platform
- market
- language
- time_window
- source_queries
- knowledge_catalog_version
- signal_layers_covered
- raw_data_path
- normalized_data_path
- sample_size
- unique_video_count
- duplicate_count
- scenario_tag_counts
- audience_context_counts
- pain_point_counts
- content_type_counts
- product_reference_type_counts
- basic_performance_summary
- top_video_refs
- dirty_sample_notes
- recommended_research_basis_summary
- limitations

## Relationship With K-P0/N02A/N18

- SIG-P0 can read K-P0 tag definitions.
- SIG-P0 outputs MarketSignalReport P0.
- N02A references reports through `ResearchBasis.supporting_signal_refs`.
- N18 controls official updates to signal interpretation rules.

## Minimal Verification Direction

Use a small Scrape Creators export or fixture-like raw JSON to produce normalized video signals and a MarketSignalReport P0, while documenting sample limitations.

## Do Not Automatically Modify ResearchTask

SIG-P0 must never automatically edit or approve ResearchTask.
