# AGENTS.md

## Business sources

- 业务顺序、回退路径和人工闸门以 `docs/00_BUSINESS_FLOW.md` 为准。
- 节点输入、处理、输出、决策权和验收标准以 `docs/01_NODE_CONTRACTS.md` 为准。
- 两者冲突时停止开发，不得自行裁决。

## Current scope

当前只完成最小 Python 工程骨架。未经明确任务，不得：

- 修改 N01—N18；
- 实现后续业务节点；
- 引入 Agent Framework、RAG 或向量数据库；
- 绕过人工决策节点；
- 在 UI、Prompt 或 Adapter 中隐藏业务规则；
- 为未来需求提前创建目录和依赖。

## Git safety

未经用户明确批准，不得执行：

- `git add`
- `git commit`
- `git push`
- `git tag`
- destructive Git commands

## Guided implementation mode

本项目采用教学型结对开发。

每个任务开始前必须明确：

- 本轮业务目标。
- 本轮学习目标。
- Codex 负责内容。
- Andy 负责内容。
- 明确保留的 TODO。
- 本轮不做什么。
- 验收标准。

Codex 必须提供：

- 一个完整示范。
- 带上下文的代码骨架。
- 精确 TODO。
- 测试约束。
- 代码审查。

Codex 不得一次性完成 Andy 负责的关键业务逻辑。

Andy 每轮至少亲自完成：

- 一段关键业务逻辑。
- 一个正常测试。
- 一个失败测试。
- 对六个系统问题的说明。

第一次测试失败时，Codex 只能提供解释和提示。

只有 Andy 明确要求时，Codex 才可以提供最小修复补丁。

不得通过删除测试、放宽规则或吞掉异常让测试通过。

每次只实现一个最小教学切片。

未经人工批准，不得进入下一切片。

详细开发方法以 `docs/02_GUIDED_IMPLEMENTATION_PLAN.md` 为准。
