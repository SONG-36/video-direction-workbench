# Market Signal Tool Contract

- Version: V0.1
- Status: Draft Architecture Document
- Scope: SIG-P0 Market Signal Tool

## 1. 文档职责

本文档定义 SIG-P0 市场信号工具契约，让 Scrape Creators / 导出数据分析工具可以独立开发，并通过 `MarketSignalReport P0` 支撑 ResearchTask 的选择依据。

## 2. SIG-P0 当前目标

SIG-P0 生成市场内容信号报告，帮助运营理解内容供给、内容表现、场景表达、痛点表达和样本限制。SIG-P0 不自动修改 ResearchTask，不自动批准研究任务。

## 3. L1-L4 四层数据定义

- L1 Content Supply Signals：内容供给信号，包括公开视频数量、关键词覆盖、场景分布、内容供给密度。
- L2 Content Performance Signals：内容表现信号，包括播放、点赞、评论、分享、发布时间、互动率、播放速度等。
- L3 Commercial Conversion Signals：商业转化信号，包括点击、加购、成交、达人带货、TikTok Shop 商品表现、广告转化。
- L4 Own Business Validation Signals：自有业务验证信号，包括自有账号发布后的播放、停留、完播、点击、加购、成交、评论和复盘判断。

## 4. SIG-P0 当前覆盖范围

当前覆盖：

- L1 Content Supply Signals
- L2 Content Performance Signals

未来扩展：

- L3 Commercial Conversion Signals
- L4 Own Business Validation Signals

## 5. SIG-P0 输入契约

最小字段：

- provider
- platform
- market
- language
- time_window
- queries
- limit_per_query
- knowledge_catalog_version

## 6. NormalizedVideoSignal P0 字段

最小字段：

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

## 7. MarketSignalReport P0 字段

最小字段：

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

## 8. 指标解释边界

- 中位数比平均值更稳。
- Top 10% 表现可以作为内容机会观察。
- 公开视频数据不能证明真实购买人群。
- 公开视频数据不能证明真实转化率。
- 公开视频数据不能证明某个创意必然成功。
- 样本受搜索词、时间范围、API 覆盖和去重逻辑影响。
- 不得把统计相关性伪装成因果结论。

## 9. 当前不做

- 自动修改 ResearchTask
- 自动批准 audience/scenario/lens
- 正式 UI
- 正式产品化 CLI
- 数据库
- N03 SearchPlan
- 视频结构化拆解
- 创意方向
- 脚本

## 10. 与 K-P0/N02A/N18 的交互方式

- SIG-P0 可以读取 K-P0 标签定义做简单规则分类。
- SIG-P0 输出 `MarketSignalReport P0`。
- N02A 通过 `ResearchBasis.supporting_signal_refs` 引用报告。
- N18 负责根据复盘结果和人工批准更新信号解释规则。
