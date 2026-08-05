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

## Visual review-driven implementation mode

基础阶段默认由 Codex 完整实现当前批准的最小业务切片。

Codex 必须同时实现必要测试并运行验证。

不得故意留下 `pass`、`NotImplementedError` 或关键 TODO。

Andy 不需要机械手写重复样板。

Andy 负责：

- 业务规则确认。
- 新增业务对象理解。
- 对象关系审查。
- 代码、AI、人工责任边界审查。
- 当前能力边界审查。
- 一次小型验证。
- 最终批准。

每个业务切片必须输出 Visual Business Logic Review，包括：

- 真实业务 Mermaid。
- 四个核心问题的简明解释。
- Key Code Pointers。
- 一个小型验证任务。
- 当前剩余边界。

Mermaid 必须使用真实对象、字段、状态、引用关系、责任主体、校验结果和错误路径。

不得只画抽象的输入、处理、输出。

四个核心问题是：

- 新增了什么业务对象？
- 它和已有对象是什么关系？
- 代码、AI、人工分别负责什么？
- 当前系统能保证什么，不能保证什么？

Andy 重点审查对象、关系、责任和边界。

不得一次抛出大量代码问答。

Codex 不得因为完整实现而越过当前切片边界。

测试失败不得通过降低业务标准解决。

未经人工批准不得进入下一切片。

详细方法以 `docs/02_GUIDED_IMPLEMENTATION_PLAN.md` 为准。

N01A-1 保留已有人工实现。

新模式从 N01A-2 默认生效。
