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
