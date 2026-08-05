# TRACK A N02A CONTEXT

## Project Path

`/Volumes/server-data/projects/andy/0803/video-direction-workbench`

## Current Task

N02A ResearchTask Domain Contract.

## Completed N01A State

N01A ProductBrief 已完成：

- SourceReference
- ConfirmedFact
- UnknownItem
- ProhibitedClaim
- ProductBrief 聚合校验
- 真实车载无线吸尘器 ProductBrief JSON 样例

## Allowed Objects

- ProductBriefReference
- ResearchBasis
- ResearchIntent
- ResearchScope
- AudienceAndScenarioFrame
- ContentReferenceFrame
- ResearchLensSelection
- ResearchQuestion
- ExclusionRule
- ResearchTask

## Forbidden

- K-P0 implementation
- SIG-P0 implementation
- Scrape Creators API
- 市场数据采集
- 统计分析
- 自动推荐
- SearchPlan
- 视频抓取
- 视频分析
- 创意方向
- 脚本
- N03

## Required Documents

- `docs/01_NODE_CONTRACTS.md`
- `docs/02_GUIDED_IMPLEMENTATION_PLAN.md`
- `docs/03_PARALLEL_DEVELOPMENT_TRACKS.md`
- `docs/06_CROSS_TRACK_MESSAGE_CONTRACTS.md`

## Input / Output Boundary

Input: ProductBrief + 人工运营判断 + optional knowledge_refs + optional supporting_signal_refs.

Output: ResearchTask P0.

ResearchTask must reference ProductBrief; it must not copy ProductBrief sources, confirmed_facts, unknown_items, or prohibited_claims.

## Minimal Verification

- Load `sample_data/products/car_vacuum_yd_592c.product_brief.json`.
- Create TikTok US ResearchTask.
- Verify ProductBriefReference matches ProductBrief product_id, product_name, revision.
- Verify ResearchBasis has basis_type, summary, knowledge_refs, supporting_signal_refs, limitations.
- Verify ProductBrief counts are unchanged.

## Do Not Implement

Do not implement K-P0, SIG-P0, or N03 in this track.
