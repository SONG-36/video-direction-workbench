# Knowledge Catalog Contract

- Version: V0.1
- Status: Draft Architecture Document
- Scope: K-P0 Knowledge Catalog

## 1. 文档职责

本文档定义 K-P0 知识库契约，让知识库目录可以独立开发，并通过稳定 `knowledge_ref` 被 N02A、SIG-P0、N03、N11、N13 和 N18 引用。

## 2. K-P0 当前目标

K-P0 只建立知识项字段、稳定 ID、版本规则、人工批准规则和引用格式。不实现数据库、UI、自动学习或自动生成业务结果。

## 3. K01-K04 四库定义

- K01 Operational Research Lens Catalog：运营研究视角库。
- K02 Platform & Content Rules Library：平台与内容规则库。
- K03 Creative Operator Library：创意操作符库。
- K04 Success / Failure Case Library：成功失败案例库。

## 4. knowledge_ref 格式

```text
knowledge_ref = "<knowledge_type>:<knowledge_id>@<version>"
```

示例：

- `research_lens:problem_amplification@v0.1`
- `platform_rule:tiktok_shop_selling_content@v0.1`
- `creative_operator:scenario_transfer@v0.1`
- `case:car_vacuum_pet_hair_success_001@v0.1`

## 5. K01 Research Lens 最小字段

- lens_id
- version
- name
- description
- useful_for
- search_implications
- analysis_implications
- risks
- examples

## 6. K02 Platform Content Rule 最小字段

- rule_id
- version
- platform
- content_surface
- description
- applies_to
- risk_level
- prohibited_patterns
- allowed_patterns
- examples

## 7. K03 Creative Operator 最小字段

- operator_id
- version
- name
- description
- suitable_for
- transformation_pattern
- risks
- examples

## 8. K04 Case 最小字段

- case_id
- version
- case_type
- product_category
- platform
- market
- summary
- linked_video_refs
- observed_pattern
- result_signal
- lesson
- risks

## 9. 版本规则

- 每个知识项必须有稳定 ID 和 version。
- 内容变更必须产生新版本或保留修订记录。
- 正式知识项不得被模型输出自动覆盖。

## 10. 人工批准规则

- 新增、删除、合并、拆分知识项必须人工批准。
- 高风险平台规则必须记录来源和批准人。
- 成功/失败案例必须记录案例依据和适用边界。

## 11. 当前不做

- 数据库
- UI
- 自动学习
- 自动覆盖正式知识库
- 自动生成创意脚本
- 替代 ProductBrief 商品事实边界

## 12. 与 N02A/SIG-P0/N18 的交互方式

- N02A 通过 `ResearchBasis.knowledge_refs` 引用 K-P0。
- SIG-P0 可以读取 K-P0 标签定义做简单规则分类，但不得修改 K-P0。
- N18 负责受控更新知识库和信号解释规则。
- K-P0 不得替代 ProductBrief 的商品事实边界。
