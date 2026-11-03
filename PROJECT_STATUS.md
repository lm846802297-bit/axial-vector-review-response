# PROJECT_STATUS — Axial-vector paper revision and referee response

**状态快照日期：** 2026-11-04（PR #38 已合并；PR #39 已提交待审查）  
**本状态快照的初始核验基线：** 243b0e62d9c3912525d1144971a1e81c2af84db7（PR #36 合并前）  
**项目启动机制合并提交：** [9b4e17519230e9eef65b34b643d3a1f8c19f46a2](https://github.com/lm846802297-bit/axial-vector-review-response/commit/9b4e17519230e9eef65b34b643d3a1f8c19f46a2)  
**用途：** 每次启动项目时快速恢复当前阶段、权威文件和下一步工作。本文件是可更新的状态快照，不替代物理推导、原始论文、计算证据或作者最新指示。

> **更新原则：** 任务完成、作者改变观点、PR 合并、论文基线更换或计算结论更新后，应检查并更新本文件。尚未重新核验的内容标为“待核验”，不得沿用旧状态作确定陈述。

## 1. 项目当前阶段

当前项目处于**正式回复信主线已形成、Major/Minor 一致性审查已完成；PR #38 已合并；PR #39 正在修订正式回复信并归档 Table II 的详细论文修改方案；论文源码与 bibliography 不在本 PR 修改范围内，仍待后续同步**的阶段。

已完成：
- 完整回复信主线按会议决策整理并合并（PR #33）。
- 回复信最终一致性审查并合并（PR #34）。
- 正式回复信与内部论文修改清单的职责规范已合并（PR #35）。
- 本轮建立项目启动读取机制和可修改的研究决策登记表。

不能据此声称：
- 论文正文已完成所有同步修改；
- 当前 2026-11-03 回复信 TeX 已重新编译并完成 PDF 视觉验收；
- 标量的完整 collider recast 或全质量范围允许区间已经得到；
- 轴矢量模型完整 SN1987A/LESN 输运与排除曲线已经完成。

## 2. 每次启动的最小读取集合

每次开始项目任务，先读：
1. [AGENTS.md](AGENTS.md)：强制规则和任务路由。
2. 本文件：当前项目状态。
3. [README-先读这里.md](README-先读这里.md)：仓库导航。

随后按任务追加读取，不要无差别加载全部历史文件：

| 任务 | 追加读取 |
|---|---|
| 回复信撰写/审查 | [审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md)、[当前回复信](Replies_to_Referee_3_referee_facing_2026-11-03.tex)、[正文待同步清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)，以及对应审稿原文/会议证据 |
| 论文正文修改 | 正文清单、作者选定的活动源文件及依赖、v6 只读基线、相关物理证据 |
| 物理推导/数值研究 | [研究决策动态登记表](审稿意见-gpt/项目规范/研究决策与不可回退事项.md)、v5.7 相关章节、原始模型公式、专题计算账本和原始文献 |
| GitHub/文档维护 | AGENTS、目标目录 README、实际 PR/分支状态和相关验证说明 |

不要每次完整读取 v5.7、所有会议文字稿或全部计算日志；先定位专题，再按需读取证据。

## 3. 当前权威文件

| 文件 | 用途 | 状态 |
|---|---|---|
| [正式回复信 TeX（当前 main 版本）](Replies_to_Referee_3_referee_facing_2026-11-04.tex) | 当前唯一权威回复信 | PR #38 已合并；包含标量偏宽度、可见分支比、Belle 数值阈值条件及 Belle II spin-0 文献修正 |
| [正文待同步清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md) | 内部正文修改追踪 | Table II 专项修改清单已在 PR #39 分支整理；论文正文尚未修改，其他项目仍待核对 |
| [审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md) | 回复信与内部清单的长期规范 | 已合并 |
| [研究决策与不可回退事项](审稿意见-gpt/项目规范/研究决策与不可回退事项.md) | 当前研究立场及变更历史 | 动态文档，允许作者随最新观点修改 |
| [原始论文 v6 PDF](axial_vector_model_building-v6.pdf) | 归档论文事实基线 | 根目录只读归档 |
| [Overleaf v6 源码归档](overleaf-source/axial-vector-model-building-v6/) | v6 源码、文献和图表 | 不能自动假定等于作者当前 Overleaf 工作版本 |
| [原始审稿报告](dw13678_report_1_a.pdf) | 审稿原文 | 核对原文措辞优先使用 PDF |
| [2026-10-23 会议观点总结](审稿意见-gpt/会议记录/2026-10-23/会议观点总结_2026-10-23.md) | 会议决策历史 | 不替代物理核验或作者最新指示 |
| [v5.6 执行手册](审稿意见-gpt/当前执行/审稿意见分析与执行手册_v5.6-主分析全任务映射与原子步骤版-20261019.md) | 任务 ID、依赖、步骤和验收框架 | §0.1 是 2026-10-27 状态快照，不再是最新状态源 |
| [v5.7 技术参考](审稿意见-gpt/审稿意见分析v5.7-物理校核与专题连续阅读版.md) | 物理推导和专题技术参考 | 2026-10-20 版本，按需读取 |

## 4. GitHub 工作状态（本次核验）

### 正式回复信修订（已合并）
- [PR #38：Add scalar partial widths and correct Belle II scalar interpretations](https://github.com/lm846802297-bit/axial-vector-review-response/pull/38)：已于 2026-11-04 合并，Squash commit 为 [f1dec3b9a0142a13444749ea1dfda432287e8b81](https://github.com/lm846802297-bit/axial-vector-review-response/commit/f1dec3b9a0142a13444749ea1dfda432287e8b81)。当前正式回复信为根目录 `Replies_to_Referee_3_referee_facing_2026-11-04.tex`。
- 已补入 s→A′A′、s→ℓ⁺ℓ⁻ 的偏宽度和可见分支比论证，限定 Belle 1 GeV 数值映射的 m_A′ > 0.5 GeV 条件，并纠正 Belle-II:2023ydz 与 Belle-II:2024wtd 的 scalar-specific interpretation 分类。
- 内部正文待同步清单和 2026-11-04 Belle II 文献核查记录已同步更新；论文源码没有修改。

### Table II 回复信修订与论文修改方案（待审查）
- [PR #39：Revise referee response and add Table II manuscript revision plan](https://github.com/lm846802297-bit/axial-vector-review-response/pull/39)：统一 Major Point 1、Minor Point 6.2 和 Summary 的标量约束数值、文献来源及物理适用条件；保留详细的未来论文修改清单。
- PR #39 修改正式回复信和内部清单/核查文档；不修改 main-v6.tex 或 references.bib。论文 Table II、正文解释和 Fiorillo v2 的 BibTeX 更新留待后续正文修订。回复信 TeX 尚未编译，PDF 视觉验收尚未完成。

### 已合并
- [PR #33](https://github.com/lm846802297-bit/axial-vector-review-response/pull/33)：按会议决策整理完整回复信。
- [PR #34](https://github.com/lm846802297-bit/axial-vector-review-response/pull/34)：Major/Minor 最终一致性审查；统一 Major 3/4.1 的 PMNS 结论及 Major 1/Minor 5 的 portal 假设。
- [PR #35](https://github.com/lm846802297-bit/axial-vector-review-response/pull/35)：回复信写作规范和项目级读取规则。
- [PR #36](https://github.com/lm846802297-bit/axial-vector-review-response/pull/36)：项目启动读取机制、PROJECT_STATUS 和可修改的研究决策登记表。

### 仍开放的专题研究 PR
| PR | 状态 | 当前已知边界 |
|---|---|---|
| [#32 标量对撞机重铸与质量分类](https://github.com/lm846802297-bit/axial-vector-review-response/pull/32) | Open / Draft；最后记录更新 2026-10-28 | 有文献台账和部分宽度计算框架；未完成 Belle II 标量重铸或完整标量质量分类 |
| [#30 轴矢量恒星冷却/超新星映射](https://github.com/lm846802297-bit/axial-vector-review-response/pull/30) | Open；最后记录更新 2026-10-28 | 有解析宽度、产生机制和部分半康普顿研究；完整介质 T/L 分辨吸收、输运、trapping 和 SN1987A/LESN 曲线未闭环 |

两个开放 PR 是独立研究工作流，不是正式回复信已完成的证据。继续前应重新检查 head、分支内容和验证记录；PR 仍开放不代表仍在持续推进。

## 5. 正式回复信与论文正文的状态边界

### 正式回复信
- 当前 main 权威回复信为根目录 `Replies_to_Referee_3_referee_facing_2026-11-04.tex`；PR #38 已合并，保留 PR #33/#34 的既有回复主线。
- 本次合并补入 Eq. (33) 的 s→A′A′ 与 s→ℓ⁺ℓ⁻ 偏宽度、visible-branching-ratio 论证；限定 Belle 1 GeV 数值映射只在 m_A′ > 0.5 GeV 时直接适用；并纠正 Belle II 两篇 scalar-specific 搜索的描述。
- 尚未重新编译当前 TeX，也尚未进行对应 PDF 视觉验收；历史 PDF 不能代替当前版本的编译件。
- PR #31 生成的 PDF 位于 2026-10-28 历史目录，文件名为 Replies_to_Referee_3_referee_facing_2026-10-28.pdf；它不是当前 2026-11-03 回复信的最终编译件。
- **待核验：** 当前 TeX 是否在 PR #34 合并后重新编译、逐页检查并形成对应 PDF。不能用 PR #31 的旧 PDF 代替。

### 论文正文
- 仓库保存原始 v6 PDF 和 Overleaf v6 源码归档。
- 2026-11-03 内部清单记录 Introduction、Eq. (27)、Table II、PMNS/Weinberg 算符、Higgs portal、kinetic mixing、有限 vector component、Muon Collider 和 Conclusion 等同步事项。
- 清单中的“待修改”“待决定/修改”“待核对”状态仍应按实际源文件复核。
- **待确认：** 作者当前选定的 Overleaf 工作版本是否与 v6 归档相同。确认前不得将 v6 归档当作活动稿件覆盖式编辑。

## 6. 当前建议的工作顺序

1. 对当前 2026-11-04 回复信 TeX 编译 PDF，检查引用、公式、分页和图表，并逐页视觉验收。
2. 审查并决定是否合并 PR #39（回复信修订 + 论文修改清单）；之后另行确认作者当前使用的 Overleaf 正文基线，再按清单实施论文修改；不得把未实施的正文修改写成已完成。
3. 优先核对影响主要物理主张的 PMNS、标量约束、portal/mixing 和参数范围；完成后更新清单中的实际正文位置和状态。
4. 若作者决定继续，分别推进 PR #32 标量重铸和 PR #30 轴矢量超新星输运；不将未完成工作写成已得到的排除结论。
5. 关键 PR 合并、作者改变路线、正文基线更新或专题验收后，更新本文件和相关决策条目。

## 7. 状态可信度约定

- **已核验：** 本次直接检查 main 文件、PR 元数据或可追溯证据。
- **已有记录，需复核：** 历史文档/PR 描述有记录，但本轮未重新执行计算或测试。
- **待确认：** 缺少当前源文件、作者选择或必要证据。
- **未完成：** 当前证据明确表明工作尚未闭环。

本文件是项目管理状态快照，不是物理结果的独立证明。物理结论以模型定义、可复核推导、实际计算和原始实验文献为准。
