# 《商品参考视频 → 视频方向》节点契约表

- Version: V0.4
- Status: Draft Business Source
- Change Reason: Define three-track architecture, knowledge catalogs, signal evidence layers, and cross-track contract boundaries.
- Pending Approval: Andy

## 文档职责

本文件定义 N01—N18 每个业务节点的输入、核心处理、标准输出、最终决策权、MVP 实现方式和验收标准。

业务节点的顺序、回退路径、人工闸门和数据回流，以 [docs/00_BUSINESS_FLOW.md](docs/00_BUSINESS_FLOW.md) 为准。

当两个业务事实源发生冲突时，不得由开发人员或 AI 自行裁决，必须停止相关开发并提交人工确认。

| 编号 | 业务节点 | 输入 | 核心处理 | 标准输出 | 最终决策权 | MVP 实现方式 | 节点验收标准 |
|---|---|---|---|---|---|---|
| N01 | 建立商品事实卡 | 商品图片、说明书、包装信息、已确认参数、运营补充信息 | 区分“已确认、未知、禁止声称”；整理功能、卖点、场景、配件、目标用户 | `ProductBrief` 商品事实卡 | 人工 | 人工录入，AI 辅助整理 | 所有卖点均有事实来源；未知参数不推断；禁用表达明确 |
| N02 | 定义内容研究任务 | 商品事实卡、目标平台、目标市场、目标语言、内容面、K01/K02 知识库、MarketSignalReport（可选）、人工运营判断 | 明确本轮研究目的、选择依据、平台、市场、语言、内容面、面向人群、使用场景、痛点、参考产品范围、研究视角、样本范围、排除规则和业务问题 | `ResearchTask` 内容研究任务合同，包含 `ResearchBasis` | 人工 | 人工定义，知识库和市场信号辅助；当前 N02A 不做 UI、AI、数据库、API 和 CLI | 研究目的明确；选择依据明确；平台、市场、语言和内容面明确；人群场景是研究假设而非已验证购买结论；参考产品范围明确；研究视角明确；排除规则明确；本轮问题能够指导后续搜索策略 |
| N03 | 制定搜索策略 | 商品事实卡、研究任务、K01/K02 知识库、MarketSignalReport（可选） | 基于研究任务和可用市场信号生成产品词、场景词、痛点词、效果词、竞品词、相邻产品词、内容形式词、排除词和搜索组合 | `SearchPlan` 搜索计划 | 人工确认 | AI 生成建议，人工修改和批准；当前 N02A 不实现本节点 | 搜索策略能回溯到 ResearchTask 的人群、场景、参考产品范围、研究视角、选择依据和排除规则；不只依赖单一商品名称；明确要搜什么和排除什么 |
| N04 | 收集候选视频 | 搜索计划、人工发现的视频、外部工具结果 | 导入视频链接或文件，记录来源、作者、发布时间、基础数据 | `CandidateVideoPool` 候选视频池 | 人工 | 第一版人工导入；后续接搜索 API | 每条视频有唯一编号、来源和可访问的视频内容 |
| N05 | 视频清洗与初筛 | 候选视频池、商品事实卡、研究任务 | 去重；判断产品相关性、场景相关性、市场匹配度、内容完整性 | `ScreenedVideoPool` 有效视频池＋淘汰记录 | 人工 | 规则初筛＋AI 建议，人工确认 | 每条淘汰视频都有明确原因；有效样本不存在明显重复 |
| N06 | 判断样本覆盖度 | 有效视频池、研究任务 | 检查是否覆盖不同目标、场景、结构、卖点和表现层级 | `CoverageReport` 样本覆盖报告 | 人工 | AI 生成覆盖分析，人工判断是否补充搜索 | 能明确指出“已覆盖什么、缺什么、是否继续搜索” |
| N07 | 单条视频结构化拆解 | 单条视频、商品事实卡、分析规则 | 提取视频目标、Hook、场景、镜头、动作、卖点、证明方式、CTA、制作形式、制作难度 | `VideoAnalysis` 单条视频分析记录 | AI 初判，人工可改 | 多模态模型结构化输出 | 每个关键结论能回指具体画面、字幕或时间点；不凭空补充 |
| N08 | 人工校正视频分析 | AI 分析记录、原视频 | 修正分类、补充业务判断、标记可借鉴点、不可借鉴点和不确定项 | `ReviewedVideoAnalysis` 已审核分析记录 | 人工 | 可编辑表单＋审核状态 | 分析记录具有“AI 原始值、人工修改值、审核状态” |
| N09 | 跨视频归纳分析 | 多条已审核的视频分析记录 | 汇总高频 Hook、场景、卖点、证明方式；识别内容聚类、同质化区域和内容缺口 | `PatternReport` 跨视频模式报告 | 人工确认 | AI 归纳，必须附视频证据 | 每项结论至少回指相关视频编号；不能只输出泛泛营销结论 |
| N10 | 分类维度校验 | 跨视频模式报告、分类规则 | 分开判断视频目标、内容结构、流量来源和表现结果 | `ClassificationSummary` 分类汇总 | 人工 | 规则＋模型混合处理 | “引流/转化”属于目标；“演示/对比”属于结构；“爆款”只属于表现结果 |
| N11 | 生成视频方向候选 | 商品事实卡、模式报告、分类汇总、K03 创意操作符库、K04 成功失败案例库 | 根据产品匹配度、内容机会、差异化、可拍性、创意操作符和案例证据生成多个方向 | `DirectionCandidates` 3 个候选方向 | AI 生成，人工决策 | AI 生成结构化候选方案 | 每个方向包含目标用户、视频目标、Hook、卖点、证明方式、参考证据、风险和制作难度 |
| N12 | 人工评审视频方向 | 候选方向、商品事实卡、团队资源、合规要求 | 判断产品匹配度、差异化、执行成本、合规风险和团队可拍性 | `DirectionDecision` 方向决策记录 | 人工 | 人工批准、拒绝或要求修改 | 选中和拒绝的方向都有原因；未批准方向不得进入脚本生成 |
| N13 | 生成脚本方案 | 已批准方向、商品事实卡、参考视频证据、K03 创意操作符库、K04 案例库 | 在 ProductBrief 商品事实约束下，生成 Hook、镜头顺序、动作、字幕、口播、卖点证明、CTA、时长和节奏 | `ScriptDraft` 脚本草案 | 人工审核 | AI 生成 | 脚本只使用已确认商品事实；内容方向与批准方案一致 |
| N14 | 生成拍摄与素材清单 | 脚本草案、已有素材、团队资源 | 拆解实拍镜头、产品特写、道具、场景、人员、AI 辅助素材和设备需求 | `ProductionPlan` 拍摄计划 | 人工 | AI 拆解，人工调整 | 每个脚本镜头都能对应具体素材来源或拍摄任务 |
| N15 | 生产前审核 | 脚本、拍摄计划、商品事实卡、合规规则 | 检查真实性、可拍性、外观一致性、成本、时间和平台风险 | `ApprovedProductionPack` 批准生产包 | 人工 | 人工闸门 | 未确认参数、虚假效果、错误配件和不可执行镜头全部被拦截 |
| N16 | 内容制作与发布 | 批准生产包、实拍素材、AI 辅助素材 | 拍摄、剪辑、审核、发布，并关联商品、方向、脚本和参考视频 | `PublishedContentRecord` 发布记录 | 人工 | 第一版系统只记录，不自动发布 | 每条发布视频能追溯到对应方向、脚本和参考视频 |
| N17 | 数据回收与复盘 | 发布视频、平台可获得数据、评论反馈 | 汇总播放、停留、完播、互动、点击、加购、成交；区分方向问题和执行问题 | `PerformanceReview` 表现复盘 | 人工判断 | 后续版本接入数据；第一版人工录入 | 不以单一播放量判断成败；能说明可能是方向、Hook、脚本或制作执行导致 |
| N18 | 更新业务规则 | 复盘结果、人工修正记录、成功与失败案例、平台变化、内容表现数据、MarketSignalReport、自有账号表现数据 | 更新搜索词、分类规则、研究视角、平台内容规则、创意操作符、信号解释规则、正反案例、方向模板、脚本模板和风险清单 | `BusinessKnowledgeVersion` 新版业务知识 | 人工批准 | 版本化文件管理，暂不自动学习 | 所有规则更新都有案例依据、修改原因和版本记录；不得根据单次模型输出、单一视频或单一信号报告自动更新正式规则 |

## Three Parallel Tracks

| Track | 名称 | 输出 | 边界 |
|---|---|---|---|
| Track A | N02A ResearchTask Domain Contract | `ResearchTask` | 关键连接对象是 `ResearchBasis`；只负责定义本轮研究任务合同 |
| Track B | K-P0 Knowledge Catalog | Knowledge Catalog files / knowledge refs | 覆盖 K01-K04；只负责标签、规则、研究视角、创意操作符和案例引用口径 |
| Track C | SIG-P0 Market Signal Tool | `MarketSignalReport P0` | 主要覆盖 L1/L2；可使用 Scrape Creators 或导出数据；只负责市场内容信号，不自动修改 ResearchTask |

## Knowledge Support Layer

K01 Operational Research Lens Catalog：用于 N02/N03/N07/N09，定义研究视频时的观察视角。

K02 Platform & Content Rules Library：用于 N02/N03/N15/N18，定义平台内容面、风险表达和平台规则。

K03 Creative Operator Library：用于 N11/N13，定义创意发散操作符，例如场景迁移、冲突放大、反差、拟人化、误导开头、生活事故。

K04 Success / Failure Case Library：用于 N07/N09/N11/N13/N18，沉淀成功案例、失败案例、违规案例、自有发布案例和参考视频案例。

## Signal Evidence Layers

L1 Content Supply Signals：公开视频数量、关键词覆盖、场景分布、内容供给密度。

L2 Content Performance Signals：播放、点赞、评论、分享、发布时间、互动率、播放速度等。

L3 Commercial Conversion Signals：点击、加购、成交、达人带货、TikTok Shop 商品表现、广告转化。

L4 Own Business Validation Signals：自有账号发布后的播放、停留、完播、点击、加购、成交、评论和复盘判断。

SIG-P0 第一版主要覆盖 L1/L2。L3/L4 是未来扩展，不得伪装成当前能力。

## N02A ResearchTask 契约边界

ResearchTask 是内容研究任务合同，必须表达：

1. ProductBriefReference
2. ResearchBasis
3. ResearchIntent
4. ResearchScope
5. AudienceAndScenarioFrame
6. ContentReferenceFrame
7. ResearchLensSelection
8. ResearchQuestion
9. ExclusionRule

ResearchBasis 记录本轮 ResearchTask 的选择依据，用于说明为什么选择某些人群、场景、痛点、参考产品范围、研究视角和业务问题。

ResearchBasis 当前最小字段：

1. basis_type
2. summary
3. knowledge_refs
4. supporting_signal_refs
5. limitations

basis_type 可用字符串，例如：

1. human_judgement
2. default_assumption
3. market_signal_supported
4. own_data_supported
5. mixed

knowledge_refs 引用 K01-K04 中的知识项。supporting_signal_refs 引用 MarketSignalReport P0 或未来数据报告。ResearchTask 不得复制完整知识库条目，不得复制完整 MarketSignalReport，只能保留引用和摘要。limitations 必须记录当前选择依据的局限性。

ResearchTask 不得包含：

1. 搜索关键词结果
2. 搜索组合结果
3. 候选视频
4. 视频分析
5. 跨视频归纳
6. 创意方向
7. 脚本
8. AI 输出结果
9. ResearchResult
10. 原始 API 响应
11. 原始视频列表
12. MarketSignalReport 完整内容
13. 自动推荐结果

ResearchTask 只通过 ResearchBasis.supporting_signal_refs 引用外部报告。

## Parallel Market Signal Track

Parallel Market Signal Track 是可以与 N02A 并行开发的独立工具线，不属于 N02A 内部实现。

SIG-P0 目标：

1. 调用 Scrape Creators 或读取其导出数据。
2. 获取 TikTok 公开视频内容信号。
3. 标准化视频基础字段。
4. 粗分类人群语境、使用场景、痛点表达和视频类型。
5. 统计样本数量、表现数据、内容类型分布和脏样本问题。
6. 输出 MarketSignalReport P0。

MarketSignalReport P0 可用于支撑：

1. ResearchBasis
2. primary_audience 选择
3. secondary_audiences 选择
4. use_scenarios 选择
5. pain_points 选择
6. reference products 选择
7. selected_lenses 选择
8. exclusion_rules 设计
9. N03 搜索策略

但必须明确：

1. SIG-P0 不自动修改 ResearchTask。
2. SIG-P0 不自动批准 audience/scenario/lens。
3. SIG-P0 不替代 ProductBrief。
4. SIG-P0 不证明真实购买人群或转化率。
5. 自动推荐如果后续实现，必须进入人工确认流程。

## 跨节点约束

1. 所有 AI 结论必须区分事实、推断和未知。
2. 关键分析结论必须携带证据引用。
3. 人工修改必须保留 AI 原始输出。
4. 未审核数据不得伪装成已审核数据。
5. 失败、拒绝和淘汰原因必须可追踪。
6. 人工闸门必须具有明确状态。
7. 进入下一节点的对象必须满足前序节点验收标准。
8. 模型不得自行补充商品功能、参数、配件或效果。
9. 视频方向和脚本必须能够回溯商品事实与参考视频。
10. 正式业务规则更新必须人工批准并保留版本记录。
11. ResearchTask 只能定义研究任务边界，不得包含搜索结果、视频结果、AI 分析结果、创意方向或研究结论。
12. 运营研究视角库和平台内容规则库是知识库支撑层，不得替代 ProductBrief 的商品事实边界。
13. ResearchTask 可以引用 ProductBrief，但不得复制 ProductBrief 的 confirmed_facts、unknown_items、prohibited_claims 和 sources。
14. N03 的搜索策略必须能回溯到 N02 的人群、场景、参考产品范围、研究视角和排除规则。
15. N11/N13 才负责视频方向候选和脚本生成，N02A 不生成创意方向和脚本。
16. N18 更新知识库必须有案例依据和人工批准，不得由模型自动学习后直接覆盖正式规则。
17. AudienceAndScenarioFrame 是本轮研究观察假设，不等同于已验证购买人群结论。
18. ResearchBasis 必须说明当前研究任务选择依据和局限性。
19. 如果 ResearchTask 使用 MarketSignalReport 支撑，必须通过 supporting_signal_refs 引用，不得复制完整报告内容。
20. Market Signal 支撑层可以并行开发，但不得污染 N02A 合同对象。
21. 市场内容信号不能替代 ProductBrief 的商品事实边界。
22. 外部公开视频数据不能单独证明真实购买人群或真实转化率。
23. N02A 当前不得实现 Scrape Creators API、市场数据采集、统计分析、自动推荐或 dashboard。
24. SIG-P0 可以实现开发者脚本或实验入口，但不得伪装成正式 UI/CLI 产品。
25. N18 更新知识库不得依据单次模型输出、单一视频或单一信号报告自动覆盖正式规则。
26. ResearchBasis 如果引用 Knowledge Catalog，必须使用 knowledge_refs。
27. ResearchBasis 如果引用 MarketSignalReport，必须使用 supporting_signal_refs。
28. SIG-P0 不得自动修改 ResearchTask。
29. K-P0 不得替代 ProductBrief 的商品事实边界。
30. MarketSignalReport 不得替代 ProductBrief 的商品事实边界。
31. 公开视频数据不能单独证明真实购买人群、真实转化率或某个创意一定成功。
32. N18 更新知识库必须保留案例依据、修改原因和版本记录。

## 状态流转

```text
Draft
→ AI Processed
→ Pending Human Review
→ Human Revised
→ Approved / Rejected
→ Used In Next Step
```

补充说明：

1. 并非所有业务对象都必须经历全部状态。
2. 需要人工闸门的节点，不得从 AI Processed 直接进入 Approved。
3. Rejected 对象不得进入下一正式节点。
4. 重新处理后必须保留版本或修订记录。
5. 人工修订后的值不得覆盖并删除 AI 原始值。

## 变更纪律

1. N01—N18 的编号和业务含义不得由开发者自行修改。
2. 新增、删除、合并或拆分节点必须先修改业务事实源并经人工批准。
3. Prompt、Schema、代码、UI 和测试不得成为新的业务事实源。
4. 两个业务事实源冲突时必须停止开发。
5. 本文档变更必须记录版本、原因和批准人。
6. 禁止系统根据单次模型输出自动修改正式规则。
7. K01/K02 作为知识库支撑层出现时，不视为新增 N01—N18 主流程节点。
8. 当前 N02A 开发不得因为知识库概念而提前实现知识库管理、数据库、UI、CLI 或 AI 生成。
9. K03 创意操作符库和 K04 成功失败案例库已经作为知识库支撑层纳入架构事实源，但当前不进入 N02A 代码实现；如果要创建正式知识库条目、代码结构或接入 N11/N13，必须另行提交实现计划并经人工批准。
10. Parallel Market Signal Track 是独立工具线，不代表 N02A 负责数据采集。
11. ResearchBasis 属于当前 N02A 合同对象；MarketSignalReport P0 属于并行信号工具输出。
12. 任何外部数据源正式接入业务主链，都必须另行提交节点契约和实现计划。
13. N02A、K-P0 和 SIG-P0 可以并行开发，但必须分别评审、分别测试、分别提交。
