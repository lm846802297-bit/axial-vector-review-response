# 审稿修订项目：当前执行入口

更新日期：2026-11-14。

> **当前状态权威来源：** 根目录 [PROJECT_STATUS.md](../../PROJECT_STATUS.md)。本文件负责导航，不复制 PR 状态或科学验收结论。
>
> **研究专题权威入口：** [research 主索引](../../research/MAIN_RESEARCH_INDEX_2026-11-13.md)。旧日期文档中的“当前”“下一步”“已完成”均须按其记录日期理解，不能直接视为实时状态。

## 从哪里开始

1. [PROJECT_STATUS.md](../../PROJECT_STATUS.md)：当前 main、PR 合并状态、开放验收门槛。
2. [研究决策与不可回退事项](../项目规范/研究决策与不可回退事项.md)：原论文模型边界、作者决定及其变更历史。
3. [审稿回复写作原则](../写作规范/审稿回复写作原则.md)：正式回复信与内部正文同步清单的职责边界。
4. [仓库分类索引](../../仓库分类索引.md)：按 Major/Minor Point 和材料类型定位。
5. [逐文档审查登记表](../../docs/repository-management/DOCUMENT_AUDIT_REGISTER.csv)：查看文档是否经过逐份审查。

## 按任务读取

| 任务 | 建议阅读顺序 |
|---|---|
| 正式回复信 | PROJECT_STATUS → 研究决策登记表 → 写作规范 → 根目录当前权威 TeX / PDF → 对应 Major/Minor 的最新对照与验证记录 |
| 论文正文同步 | 正文待同步修改清单 → 当前活动 Overleaf 源码确认 → 对应物理证据 → 修改 Diff → 编译与视觉检查记录 |
| Major 1：Higgs–singlet | research/MAIN_RESEARCH_INDEX → research/major1-higgs-scalar-mixing-20261109/README.md → 对应子计算、反项/匹配与极点审计 |
| Major 3：中微子 | 研究决策登记表 → 当前回复信 Major 3/4.1 → 2026-11-04 回复对照和验证记录；旧 seesaw 候选笔记仅作历史，不代表原模型扩展 |
| Major 4.2/4.3 | 研究决策登记表 → 对应 kinetic-mixing / 有限矢量耦合计算和实验比较 → 当前回复信对应段落 |
| Major 4.4：恒星冷却 | research/MAIN_RESEARCH_INDEX → stellar-cooling-constraints README / VALIDATION_AND_REVIEW → collaborator archive STATUS_MATRIX / FIGURE_AUDIT → 原始文献和数值输入 |
| 计算复现 | 对应 research 工作流 README → 输入清单和 SHA-256 → 精确脚本/命令 → 测试与输出 → 独立验证报告 |

## 关键模型与科学边界

- 原论文是原始单 VEV UV 模型；双 VEV 工作必须作为独立扩展，不得把其质量关系、自由度或热过程默认为原论文内容。
- Major 3 回复中的可选中微子完成机制不自动意味着原论文模型已加入相应场内容，也不等于完成全局拟合或所有约束。
- Major 1 的 portal 阈值、轻子圈、有限导数项和局部极点诊断是不同层次的计算；不能把子计算通过写成完整物理极点与 Higgs 重铸已完成。
- Major 4.4 的局部速率、显式振幅、详细平衡、径向积分和完整输运是不同验收层次；CI 通过不等于 Blinov Fig. 7 物理基准通过。

## 历史材料使用规则

- v5.6 执行手册、v5.7 技术参考、会议记录、旧 PR 审计和 dated status 文件均保留其历史价值。
- 它们可用于恢复推导与决策过程，但不能覆盖作者最新明确决定或根目录实时状态。
- 不删除旧文件来“清理”状态；应标明历史角色，并由当前索引链接到权威版本。
