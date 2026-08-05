# Cross-Track Message Contracts

- Version: V0.1
- Status: Draft Architecture Document
- Scope: Message contracts across Track A, Track B, and Track C

## 1. 文档职责

本文档定义三轨之间的消息 / 数据格式，避免不同聊天框开发时接口对不上。

## 2. 消息契约总览表

| Contract | Producer | Consumer | Purpose |
|---|---|---|---|
| ProductBriefReference | Track A | ResearchTask | 引用 ProductBrief 修订版本 |
| knowledge_ref | Track B | Track A / Track C | 引用知识库条目 |
| signal_report_ref | Track C | Track A | 引用 MarketSignalReport |
| ResearchBasis | Track A | ResearchTask / Review | 记录研究任务选择依据 |
| ResearchTask P0 | Track A | N03 / review | 定义一轮内容研究任务 |
| NormalizedVideoSignal P0 | Track C | MarketSignalReport | 标准化视频信号 |
| MarketSignalReport P0 | Track C | Track A / N03 / N18 | 市场内容信号报告 |

## 3. ProductBriefReference 格式

```json
{
  "product_id": "car_vacuum_yd_592c",
  "product_name": "车载无线吸尘器",
  "revision": 1
}
```

## 4. knowledge_ref 格式

```json
{
  "ref_type": "research_lens",
  "ref_id": "problem_amplification",
  "version": "v0.1"
}
```

## 5. signal_report_ref 格式

```json
{
  "ref_type": "market_signal_report",
  "report_id": "market_signal_car_vacuum_tiktok_us_20260805_p0",
  "version": "p0"
}
```

## 6. ResearchBasis 格式

```json
{
  "basis_type": "mixed",
  "summary": "本轮研究任务依据人工判断、K01 研究视角和 MarketSignalReport P0 选择人群场景。",
  "knowledge_refs": [
    {
      "ref_type": "research_lens",
      "ref_id": "problem_amplification",
      "version": "v0.1"
    }
  ],
  "supporting_signal_refs": [
    {
      "ref_type": "market_signal_report",
      "report_id": "market_signal_car_vacuum_tiktok_us_20260805_p0",
      "version": "p0"
    }
  ],
  "limitations": [
    "公开视频数据只能说明内容供给和表现信号，不能证明真实购买人群或真实转化率。"
  ]
}
```

## 7. ResearchTask P0 格式

ResearchTask P0 应包含：

- task_id
- product_brief_ref
- research_basis
- intent
- scope
- audience_and_scenario
- content_reference
- lens_selection
- research_questions
- exclusion_rules
- notes

## 8. MarketSignalReport P0 格式

MarketSignalReport P0 应包含：

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

## 9. NormalizedVideoSignal P0 格式

NormalizedVideoSignal P0 应包含：

- video_id
- source_url
- source_platform
- query
- author_id
- author_name
- published_at
- collected_at
- caption
- hashtags
- transcript
- product_link_present
- view_count
- like_count
- comment_count
- share_count
- duration_seconds
- detected_audience_contexts
- detected_use_scenarios
- detected_pain_points
- detected_content_types
- detected_product_reference_type
- relevance_notes
- dirty_sample_flags

## 10. 跨轨引用规则

- 所有 `knowledge_ref` 必须包含 ref_type、ref_id、version。
- 所有 `signal_report_ref` 必须包含 ref_type、report_id、version。
- ResearchTask 只能引用 knowledge_refs 和 signal_report_refs。
- 所有跨轨引用必须可追踪到版本或报告 ID。

## 11. 禁止复制规则

- ResearchTask 不得复制完整知识库条目。
- ResearchTask 不得复制完整 MarketSignalReport。
- SIG-P0 不得自动修改 ResearchTask。
- K-P0 不得覆盖 ProductBrief。
- ProductBrief 是商品事实边界。

## 12. 版本规则

- Knowledge Catalog 使用 `v0.x` 版本。
- MarketSignalReport 使用 report_id + `p0` 版本。
- ProductBriefReference 使用 product_id + revision。
- 跨轨消息变更必须同步更新本文件。

## 13. 示例

```json
{
  "task_id": "research_task_car_vacuum_tiktok_us_001",
  "product_brief_ref": {
    "product_id": "car_vacuum_yd_592c",
    "product_name": "车载无线吸尘器",
    "revision": 1
  },
  "research_basis": {
    "basis_type": "mixed",
    "summary": "基于人工判断、问题放大研究视角和 MarketSignalReport P0 定义本轮任务。",
    "knowledge_refs": [
      {
        "ref_type": "research_lens",
        "ref_id": "problem_amplification",
        "version": "v0.1"
      }
    ],
    "supporting_signal_refs": [
      {
        "ref_type": "market_signal_report",
        "report_id": "market_signal_car_vacuum_tiktok_us_20260805_p0",
        "version": "p0"
      }
    ],
    "limitations": [
      "市场信号不能证明真实购买人群。"
    ]
  }
}
```
