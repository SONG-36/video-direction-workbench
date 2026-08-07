# Business Question And Evidence Map

- Version: V0.1
- Status: Approved
- Authority: Preliminary Design
- Scope: Map Track C business questions to evidence needs, signal layers, candidate data sources, answerability, allowed statements, and prohibited overclaims.
- Depends On: `docs/00_BUSINESS_FLOW.md`, `docs/01_NODE_CONTRACTS.md`, `docs/05_MARKET_SIGNAL_TOOL_CONTRACT.md`, `docs/tracks/sig_market_signal/00_SIG_SYSTEM_BLUEPRINT.md`
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Andy
- Approval Date: 2026-08-07

Approval Boundary: This approval covers the business question and evidence-layer framework only. It does not approve Scrape Creators real fields, parameters, pricing, pagination, ranking, metric semantics, SIG-P0 Implementation Ready status, code implementation, or endpoint suitability.

## Answerability Scale

| Value | Meaning |
|---|---|
| Answerable In P0 | Can be answered descriptively from SIG-P0 public video supply/performance samples if data source fields are verified. |
| Partially Answerable | Can be observed only as a limited signal and needs caveats or future data. |
| Future Stage | Not part of P0; belongs to a later SIG stage. |
| Requires Own Business Data | Needs N17 or own platform/business data. |
| Not Provable From Public Data Alone | Public data may help form hypotheses but cannot prove the claim. |

## Evidence Matrix

| question_id | business_question | decision_supported | required_signal_layers | minimum_evidence | candidate_data_sources | current_answerability | allowed_statement | prohibited_overclaim | target_stage |
|---|---|---|---|---|---|---|---|---|---|
| A01 | 市场上有多少相关内容？ | 判断某个关键词或产品方向是否有公开视频供给。 | L1 | Verified query, collection run, raw record count, deduped video count, dirty sample notes. | Search by Keyword, Search by Hashtag. | Answerable In P0 | 在本次查询样本中发现 N 条去重公开视频。 | 整个平台总内容量就是 N。 | SIG-P0 |
| A02 | 哪些查询词能搜到有效样本？ | 支持 ResearchBasis 和后续 N03 搜索策略准备。 | L1 | Configured queries, QueryExecution status, matched_queries, valid sample count, excluded sample reasons. | Search by Keyword, Search by Hashtag. | Answerable In P0 | 某些查询词在本次采集中返回更多有效样本。 | 这些词一定是平台用户真实搜索需求。 | SIG-P0 |
| A03 | 哪些场景、痛点、内容形式出现得多？ | 形成 audience/scenario/pain point/content form 研究假设。 | L1 | Normalized signals, classification rule version, evidence notes, tag counts. | Video captions, hashtags, transcript if available. | Answerable In P0 | 在样本中，某些标签出现频次较高。 | 高频标签就是真实购买动机。 | SIG-P0 |
| A04 | 内容供给是否集中于少数表达？ | 判断是否存在同质化表达和内容缺口假设。 | L1 | Tag distribution, query overlap, creator/video counts, sample limitation. | Search by Keyword, Search by Hashtag, Video Info. | Partially Answerable | 当前样本显示表达集中或分散的迹象。 | 市场已经被某种表达完全占领。 | SIG-P0 |
| B01 | 哪些公开视频在当前样本中表现相对较高？ | 选择值得人工观察的公开视频。 | L2 | View, like, comment, share metrics, snapshot time principle, valid denominators. | Video Info, search result exports if metrics exist. | Answerable In P0 | 某些视频在本次样本的公开视频指标中相对较高。 | 这些视频证明该创意必然成功。 | SIG-P0 |
| B02 | 不同内容形式的播放和互动分布如何？ | 比较样本内标签表现，支持研究假设。 | L1/L2 | Tag groups, valid sample size, median, percentiles, missing metric handling. | Video Info, Transcript, normalized classifications. | Answerable In P0 | 样本内某类内容形式的中位数或分位数表现较高。 | 某内容形式导致更高转化。 | SIG-P0 |
| B03 | 新旧视频是否需要区分？ | 避免历史累计指标误读。 | L2 | published_at, collected_at, metric snapshot principle, age bands. | Video Info. | Partially Answerable | 需要区分发布时间和采集时间来解释表现。 | 老视频和新视频可以直接用总播放量比较真实效率。 | SIG-P0 |
| B04 | 头部视频是否扭曲平均结果？ | 避免平均值被极端值主导。 | L2 | Mean, median, top percentile, max, valid sample count. | Video Info, normalized metrics. | Answerable In P0 | 头部视频可能显著影响平均值，应同时看中位数和分位数。 | 平均值单独代表整体市场机会。 | SIG-P0 |
| C01 | 内容是否集中在少数作者？ | 判断创作者生态是否集中。 | L1/L2 | Creator identity, video count per creator, performance by creator. | Profile, Profile Videos, Video Info. | Future Stage | 未来可观察样本内作者集中度。 | 少数作者集中证明真实渠道垄断。 | SIG-P1 |
| C02 | 高表现是否主要由大账号贡献？ | 判断高表现样本是否依赖账号体量。 | L1/L2 | Creator profile metrics, video metrics, creator size bands. | Profile, Profile Videos, Video Info. | Future Stage | 未来可比较样本内账号规模与公开视频表现。 | 大账号数据证明商品真实购买人群。 | SIG-P1 |
| C03 | 评论中出现哪些问题和疑虑？ | 支持痛点、反对理由和风险表达发现。 | L1/L2 | Comments, replies, theme classification, quoted evidence refs. | Comments, Comment Replies. | Future Stage | 评论可以作为公开用户反馈线索。 | 评论主题等于真实购买阻力比例。 | SIG-P1 |
| C04 | 平台用户如何表达相关搜索需求？ | 扩展查询词和内容研究语言。 | L1 | Search suggestions, top search terms, trend signals. | Search Suggestions, Top Search, Trending Feed. | Future Stage | 公开搜索表达可作为查询扩展线索。 | 搜索表达证明购买意图或成交需求。 | SIG-P1 |
| C05 | 公开可见的创作者受众估计能提供什么有限线索？ | 仅支持人工进一步研究，不自动批准 audience。 | L1/L2 auxiliary audience visibility | Verified source, method, coverage, time window, and limitation notes. | User's Audience Demographics. | Future Stage | 可观察数据源提供的创作者受众估计，但必须先验证其来源、算法、覆盖和时间范围。 | 不能将创作者受众估计解释为真实购买人群、真实商品购买者或 ResearchTask.primary_audience。 | SIG-P1 |
| D01 | 是否存在大量公开广告素材？ | 判断是否值得研究广告表达。 | L1/L2 | Ad search results, public ad count, ad metadata if verified. | Ad Library Search, Ad Library Ad. | Future Stage | 公开广告库可显示广告素材可见性。 | 公开广告数量证明投放规模或销售规模。 | SIG-P2 |
| D02 | 广告内容与自然内容表达是否不同？ | 支持内容结构对比假设。 | L1/L2 | Source type, content tags, public ad content, organic content comparison. | Ad Library, Search by Keyword, Profile Videos. | Future Stage | 公开素材可支持表达差异假设。 | 广告表达差异证明渠道因果效果。 | SIG-P2 |
| D03 | 是否存在达人、品牌、普通用户内容供给结构差异？ | 判断内容来源结构假设。 | L1/L2 | Creator/profile classification, video tags, verified source type evidence. | Profile, Profile Videos, Search Users, Video Info. | Future Stage | 可观察样本内不同公开来源的表达差异。 | 可证明真实达人带货贡献。 | SIG-P2 |
| D04 | 能否证明商品是广告驱动、达人驱动或自然流驱动？ | 防止错误归因。 | L1/L2/L3/L4 | Public signals plus private or own business validation would be required. | Ad Library, creator data, TikTok Shop visibility, own data. | Not Provable From Public Data Alone | 只能形成驱动结构假设。 | 公开视频和广告库证明真实 GMV 归因。 | SIG-P2/P5 |
| E01 | 平台上有哪些相关商品和店铺？ | 观察公开商品生态。 | Commercial Visibility / L3-adjacent | Shop/product search, product details, shop identity. | Shop Search, Shop Products, Product Details. | Future Stage | 可描述公开可见商品和店铺样本。 | 公开可见商品列表等于市场真实销售排行。 | SIG-P3 |
| E02 | 商品与公开视频是否存在公开关联？ | 观察公开视频与商品链接关系。 | Commercial Visibility / L3-adjacent | Video-product public link, showcase presence, source refs. | User Showcase, Product Details, Video Info. | Future Stage | 可记录公开关联是否存在。 | 公开关联证明点击、加购或成交。 | SIG-P3 |
| E03 | 商品评价中出现哪些问题？ | 发现商品层面问题和反对理由。 | Commercial Visibility / L3-adjacent | Product reviews, theme classification, source refs. | Product Reviews. | Future Stage | 公开评价可作为问题线索。 | 评价主题比例代表全市场真实购买反馈比例。 | SIG-P3 |
| E04 | 公开商品信息能否证明真实成交或真实转化率？ | 防止商业过度解释。 | L3/L4 | Requires verified platform metric semantics and own conversion data. | TikTok Shop, own business data. | Not Provable From Public Data Alone | 公开商品信息最多支持商业可见性观察。 | 公开商品信息证明真实成交或真实转化率。 | SIG-P3/P4 |
| F01 | 自有视频是否产生播放、停留、点击、加购和成交？ | 判断自己业务中的内容表现。 | L4 | Own account analytics, click/add-to-cart/order data, N17 review. | N17, own platform analytics, order data. | Requires Own Business Data | 自有数据可描述已发布内容的业务表现。 | 单次结果证明长期市场规律。 | SIG-P4 |
| F02 | 市场高表现内容在自有账号是否可以迁移？ | 判断市场信号是否对自己有效。 | L2/L4 | Public signal report, own content experiment, comparable direction and execution notes. | MarketSignalReport, N16 published content, N17 review. | Requires Own Business Data | 可以比较市场信号和自有测试结果是否一致。 | 市场爆款必然适用于自有账号。 | SIG-P4/P5 |
| F03 | 是方向问题、Hook 问题、制作问题还是商品问题？ | 支持复盘和下一轮实验设计。 | L4 | Script/direction refs, production notes, metrics, comments, human review. | N13-N17 records. | Requires Own Business Data | 可形成经人工判断的复盘结论。 | 指标自动判定唯一失败原因。 | SIG-P4 |
| F04 | 哪类内容真的对自有业务有效？ | 识别自有业务可复用规则候选。 | L4 | Multiple own tests, comparable metrics, N17 review, human approval. | N17, own analytics, comments, order data. | Requires Own Business Data | 可形成自有业务有效性候选结论。 | 少量测试自动成为正式规则。 | SIG-P4/P6 |
| G01 | 哪些市场信号被自有数据验证？ | 支持证据对照和规则候选。 | L1/L2/L4 | Public report, own validation report, comparable tags and directions. | SIG-P0/P1/P2 reports, N17. | Future Stage | 可记录被自有数据支持的市场信号。 | 一次验证证明普遍规律。 | SIG-P5 |
| G02 | 哪些市场信号与自有结果冲突？ | 识别风险、误读或执行差异。 | L1-L4 | Public signal, own result, human review of execution and product fit. | SIG reports, N17 review. | Future Stage | 可记录冲突并要求人工判断原因。 | 冲突自动说明市场信号错误。 | SIG-P5 |
| G03 | 下一轮应该研究什么或测试什么？ | 支持 ResearchBasis 和实验候选。 | L1-L4 | Evidence comparison, gaps, limitations, human operating judgment. | SIG-P5 reports, ResearchBasis, N17. | Future Stage | 可提出待人工确认的研究或实验候选。 | 系统自动批准下一轮研究任务。 | SIG-P5 |
| G04 | 哪些规则可以提交 N18 人工更新？ | 支持受控知识回流。 | L1-L4 | Validated case evidence, review notes, proposed rule diff, approval status. | SIG-P5, N17, N18. | Future Stage | 可提交 N18 审查的规则候选。 | SIG 自动更新正式知识库。 | SIG-P6 |

## Core Interpretation Boundary

P0 can describe public content supply and performance within a defined sample. It cannot prove true buying audience, true conversion rate, ad attribution, creator GMV attribution, or guaranteed creative success.
