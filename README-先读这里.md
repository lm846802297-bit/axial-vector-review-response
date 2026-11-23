# 审稿修订项目入口

更新日期：2026-11-24。

> **当前状态（2026-11-24）：** PR #140 已合并，B.13/B.16 首批整合进入 main。独立 Croon/Lai vector benchmark 正通过 PR [#123](https://github.com/lm846802297-bit/axial-vector-review-response/pull/123) 审查。PR #123 分支有 2,534 个 Git-tree 条目（2,369 个文件、165 个目录）、903 份 Markdown/text 文件（655 `.md`、248 `.txt`）和 140 个工作流。462 份基线文档已 disposition；441 份补充文档中 167 PASS_WITH_NOTES、6 HISTORICAL、268 PENDING，其中 26 份新增 Croon/C1 文档尚待逐项内容审查。140 个工作流均已登记，其中 15 个新工作流仍为 PENDING。C1 10 MeV 结果是纯矢量 benchmark，外层 25–100 km 半康普顿 opacity 未纳入，不是最终 SN1987A 排除曲线，也不是轴矢量约束。Fig. 7 +92.4284% 偏差仍未解决。详细状态以 [PROJECT_STATUS.md](PROJECT_STATUS.md) 顶部最新记录为准。

> **当前状态提示（2026-11-16）：** 本文件中带有 2026-11-06 日期的任务条目属于历史工作快照，不再代表当前 PR 或科学验收状态。最新状态请以根目录 [PROJECT_STATUS.md](PROJECT_STATUS.md) 和 [research 主索引](research/MAIN_RESEARCH_INDEX_2026-11-13.md) 为准。

## 分类索引

- [历史归档总索引](archive/README.md)、[Overleaf 源码归档说明](overleaf-source/README.md)、[审稿意见资料索引](审稿意见-gpt/README.md)。

- [仓库分类索引](仓库分类索引.md)：按权威入口、会议决策、回复信与 Diff、专题计算、脚本日志、历史归档和分支审计定位材料。
- [根目录迁移审查](docs/repository-management/ROOT_RELOCATION_AUDIT_2026-11-17.md)；[原始 24 文件审查基线](docs/repository-management/ROOT_FILE_AUDIT_REPORT_2026-11-14.md)：记录根目录文档、TeX、BibTeX、PDF 和构建依赖的审查结论及待办。

## 共享科研规范

本项目采用中央仓库共享规范，具体版本见 [research/standards-lock.yaml](research/standards-lock.yaml)。先阅读[中央科研规范索引](https://github.com/lm846802297-bit/high-energy-theory-research/blob/142267bc803c90aa681110293b66b73947bbcaa1/docs/governance/CENTRAL_STANDARDS_INDEX.md)；模型和审稿决策仍以本仓库的项目专属记录为准。

## 每次开展本项目工作前必读（轻量启动）

1. 仓库根目录 [AGENTS.md](AGENTS.md)：强制规则和按任务读取路径。
2. [中央规范锁](research/standards-lock.yaml)：本项目采用的中央规范精确版本。
3. [PROJECT_STATUS.md](PROJECT_STATUS.md)：当前项目阶段、权威文件、开放 PR、正文同步状态和下一步工作。
4. 本文件：仓库导航和专题入口。

根据任务再追加读取：
- 回复信任务：[审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md)、根目录当前权威 [回复 TeX](Replies_to_Referee_3_referee_facing_2026-11-04.tex) 与 [回复 PDF](Replies_to_Referee_3_referee_facing_2026-11-04.pdf)、[正文待同步清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)。PR #40 是 Major 3 历史修订；PR #56 已于 2026-11-12 合并 Major 4.4 固定剖面 EFT benchmark。当前 PDF 已于 2026-11-16完成同源构建及64页逐页视觉验收，详见 [正式回复信最终排版验收](docs/repository-management/REPLY_LETTER_FINAL_ACCEPTANCE_2026-11-16.md)。
- 物理研究任务：[研究决策与不可回退事项（动态登记表）](审稿意见-gpt/项目规范/研究决策与不可回退事项.md)及对应 v5.7 专题章节、原始推导和计算证据。
- 论文正文修改：正文清单、作者当前选定的活动源文件及依赖、对应技术证据。

研究决策登记表是可更新文档；作者最新明确观点优先于旧记录。不要每次完整读取全部会议文字稿、v5.7 或计算日志。

## 当前工作入口

- **2026-11-17 仓库审查快照（历史）：** 原始 462 份基线文档已全部审查，其中 7 条此前的 REVISION_REQUIRED 已在第九十轮按证据改为 PASS_WITH_NOTES；物理限制仍单独保留；另有 146 份后续新增 `.md`/`.txt` 文件已列入[补充登记表](docs/repository-management/SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv)，其中 140 份 PASS_WITH_NOTES、6 份 HISTORICAL、0 份 PENDING、0 份 REVISION_REQUIRED。当前 Git 树共 608 份 Markdown/text 文件（509 `.md`、99 `.txt`）；基线指纹状态为 372 MATCH_CURRENT、89 CONTENT_FINGERPRINT_DIFFERS、1 SIZE_METADATA_DIFFERS。118 个工作流中 103 个已静态审查、1 个为 ACTIVE、14 个保留为历史候选、0 个待审查。第七十八轮静态审查 4 个 B.2/B.16 工作流；第七十九轮再审查 4 个外层温度及缪子中微子敏感性工作流，第八十至八十七轮完成余下工作流的逐项静态审查，第八十八轮核对 15 个历史候选，其中当前 PR 回复信构建工作流改列 ACTIVE，另 14 个的运行历史已通过 GitHub Actions API 核对，共 499 次记录，候选状态因分支和手动触发仍有效而保留，覆盖 EOS 占据、C4 碰撞核、B.16 路径与剖面、Bollig/Caputo 来源、Fig. 7 数字化与收敛，以及 collider/vector-response 审计；记录了触发依赖缺项、分支守卫、权限范围和依赖锁定问题。第七十五轮将三个明确归档的历史变体从 REVISION_REQUIRED 调整为 HISTORICAL；第七十六轮确认 B.16 和 Fig. 7 10 MeV 交付尚缺；第九十轮补齐局域速率/相空间和归档证据，并明确 Fig. 7 的 +92.4284% 物理偏差仍未解决；第八十九轮更正 Global-02 报告计数并将其文档状态从 REVISION_REQUIRED 调整为 PASS_WITH_NOTES，未改变计算输出或全局验收结论；另有[已被第九十轮取代的七项历史行动表](docs/repository-management/REMAINING_BASELINE_REVISION_REQUIRED_ACTION_PLAN_2026-11-17.md)列出每项关闭证据；[最终集成审查](docs/repository-management/FINAL_INTEGRATION_REVIEW_2026-11-17.md)逐项说明保留理由并审查 PR 全部变更。第九十轮执行了受限的 10 MeV 局域速率/逃逸相空间与 PR52 归档完整性诊断；这些结果不等于生产轴矢量约束更新，Fig. 7 +92.4284% 偏差仍未解决。活动专题脚本迁移的路径、哈希和工作流边界见[迁移审查](docs/repository-management/ACTIVE_SCRIPT_RELOCATION_AUDIT_2026-11-17.md)。相关报告见[第七十七轮工作流审查](docs/repository-management/workflow-reviews/C4C4_WORKFLOW_REVIEW_2026-11-17.md)和[第七十八轮工作流审查](docs/repository-management/workflow-reviews/B2_PATH_WORKFLOW_REVIEW_2026-11-17.md)、[第七十九轮工作流审查](docs/repository-management/workflow-reviews/B16_OUTER_PROFILE_SENSITIVITY_WORKFLOW_REVIEW_2026-11-17.md)和[第八十轮工作流审查](docs/repository-management/workflow-reviews/B16_MUON_PROFILE_AND_NEUTRINO_BRANCH_WORKFLOW_REVIEW_2026-11-17.md)、[第七十四轮](docs/repository-management/SEVENTY_FOURTH_REVIEW_FINAL_RESEARCH_READMES_AND_MANIFESTS_2026-11-17.md)、[第七十五轮](docs/repository-management/SEVENTY_FIFTH_REVIEW_BASELINE_ARCHIVE_RECLASSIFICATION_2026-11-17.md)和[第七十六轮](docs/repository-management/SEVENTY_SIXTH_REVIEW_B16_ESCAPE_AND_FIG7_FOLLOW_UP_2026-11-17.md)和[第八十九轮](docs/repository-management/EIGHTY_NINTH_REVIEW_P1B_GLOBAL02_REPORT_COUNT_RECONCILIATION_2026-11-17.md)。

下面按日期保留历史工作快照；当前 PR 状态、科学验收状态和正式回复 PDF 状态均以根目录 [PROJECT_STATUS.md](PROJECT_STATUS.md) 顶部最新 live section 为准。

- **2026-11-06 历史快照：Major 4.4 / [PR #56](https://github.com/lm846802297-bit/axial-vector-review-response/pull/56)：** PR #56 已于 2026-11-12 合并，整合固定剖面轴矢量 EFT ballistic-cooling benchmark 和相关研究记录。合并不表示纯矢量 Blinov Fig. 7 10 MeV 强吸收端已复现（字面固定-ω 路径仍有约 +92.25% 差异），也不表示获得完整 SN1987A transport/exclusion。具体状态和适用边界以 [PROJECT_STATUS.md](PROJECT_STATUS.md) 及 [验证与正式自审记录](research/stellar-cooling-constraints-20261105/VALIDATION_AND_REVIEW.md) 为准。

- **正式回复信与参考文献：** [回复 TeX](Replies_to_Referee_3_referee_facing_2026-11-04.tex) 是可编辑源；[PDF](Replies_to_Referee_3_referee_facing_2026-11-04.pdf) 在本整理分支由该源编译，共 64 页、500,973 bytes，SHA-256 `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819`。依赖 `references.bib`、`Replies_to_Referee_3_stellar_references.bib`、`JHEP.bst` 与 Major 4.4 图；验收范围见 [最终排版验收报告](docs/repository-management/REPLY_LETTER_FINAL_ACCEPTANCE_2026-11-16.md)。

- **2026-11-04 Major 4.4 文献调查：** [轴矢量 stellar-cooling / SN1987A 文献适用性调查](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.4-轴矢量stellar-cooling文献适用性调查_2026-11-04.md)。区分一般轴矢量恒星冷却讨论、轴矢量核子耦合 SN 文献、常规矢量型 \(L_\mu-L_\tau\) 超新星计算，以及本文完全相同的中微子 coalescence 子过程；不将矢量模型完整曲线直接作为轴矢量 UV 模型排除。原论文单 VEV 模型的后续计算见 [PR #53](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53)；PR #53 已于 2026-11-12 合并；合并不构成已完成的超新星排除，当前验收边界以 PROJECT_STATUS.md 为准。

- **2026-11-04 Major 4.2 新修订：** [动能混合与暗光子限制对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-暗光子限制与论文修改对照_2026-11-04.md) 及[验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-验证记录_2026-11-04.md)，记录显式匹配边界 epsilon_ind(mu_match)=0、10/100/200/300 MeV 的 NA64 质量依赖视觉读取区间、300 MeV dimuon 分支比，以及 epsilon_eff=|epsilon|sqrt(Br_inv) 的 leading-yield 比较。

- **2026-11-04 Major 2 新修订：** [Fig. 2 参数范围与论文修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-Fig2参数范围与论文修改对照_2026-11-04.md) 及[验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-验证记录_2026-11-04.md)。低质量端以 g−2 主导约束线可继续延伸解释不扩图；修正实际纵轴上限为 1。此前 Major 3 的 PR #40 已合并。

- **2026-11-05 Major 1.3 / PR #49（已于 2026-11-05 合并）：** [P2-lite portal-induced scalar-loop 计算记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-05/Portal_induced_scalar_loop_power_counting_P2_lite_2026-11-05.md) 与[可复现脚本](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-05/portal_scalar_loop_power_counting_2026-11-05.py)。记录 CP-even radial-scalar bubble 子集、Goldstone 顶角、零动量相减和证据边界；正式回复只采用顶角结构与联合 loop counting，不把未闭合子集数值作为完整两圈物理预测。 正式回复信已补入等质量和非等质量 B0 差值的闭式解析表达式，并以 Simpson 积分独立交叉验证，最大相对误差低于 1e-14。

- **2026-11-05 回复信解析论证一致性修订 / [PR #50（已合并）](https://github.com/lm846802297-bit/axial-vector-review-response/pull/50)：** [审查与修订记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-05/回复信解析论证完整性审查与修订记录_2026-11-05.md)。修正 Minor 6.1 的 \(g_X\) 上限；补充 Major 4.4 的 Kahn et al. 轴矢量恒星冷却引用、轴矢量流散度和 Goldstone 等效纵向耦合，并限定 kinetic-mixing 比较的电磁过程适用范围。复核后已撤销最初拟议的 Major 1.3 三处文字精简，恢复 main 原有表述；PR #50 不修改 Major 1.3。未修改论文正文，也未开展新的 SN 输运计算。完整 PDF 尚未按当前 TeX 重编译。

- **模型一致性边界：** Major Point 3/4.1 的额外中微子完成机制只用于对应的专门中微子回复论证，不改变原论文的 `S+VLL` 单 VEV UV 模型。其他非中微子 Major/Minor 回答及其专题 PR 均以原论文模型为基准。
- **[PR #54（已合并）](https://github.com/lm846802297-bit/axial-vector-review-response/pull/54)：** 修正正式回复信与项目规范，明确 Major 3/4.1 的中微子完成机制只属于对应问题的回复论证；其他非中微子回答仍以原论文单 VEV 模型和原始规范流为基准。
- **2026-11-05 PR #30/#51 清洁替代 / [PR #53（已合并）](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53)：** 旧 #30 和错误采用双 VEV 映射的 #51 均已关闭、未合并。#53 从当前 main 创建，恢复原论文单 VEV 映射；半康普顿振幅和均匀局部热率计算保留。完整介质 T/L opacity 和 SN transport 仍未完成。
- **2026-11-05 PR #32 替代 / [PR #52（Closed，未合并）](https://github.com/lm846802297-bit/axial-vector-review-response/pull/52)：** 旧 #32 已关闭、未合并。#52 从当前 main 创建，严格使用原论文单 VEV 标量模型；保留 Belle II 来源台账、重铸协议、部分宽度框架和逐点分类规则。Belle II 数值数据提取、实验 benchmark 复现和 UV 重铸尚未完成；这些是独立后续研究，不是当前 Major Point 1 回复的前置条件。

日常推进使用 **[精简执行手册 v5.6](审稿意见-gpt/当前执行/审稿意见分析与执行手册_v5.6-主分析全任务映射与原子步骤版-20261019.md)** 的任务 ID、依赖和验收条件；其 §0.1 是 2026-10-27 历史状态快照，不再作为当前状态源。物理推导使用 **[v5.7 Markdown 技术参考](审稿意见-gpt/审稿意见分析v5.7-物理校核与专题连续阅读版.md)** 的相关章节。v5.7.1 LaTeX 仅用于查阅尚未回收到 Markdown 的历史细节。

- [当前执行目录说明](审稿意见-gpt/当前执行/README.md)
- [59 项原子审稿条目与 v5.6 任务映射](审稿意见-gpt/当前执行/审稿意见原子条目59项-v5.7.1至v5.6任务映射-20261026.md)
- [主分析 v4.1](审稿意见-gpt/当前执行/审稿意见分析-gpt-v4.1-公式复核与PMNS方案建议-主题整合重构版-原文恢复修正版-20261019.md)

- **当前任务状态：** 以根目录 [PROJECT_STATUS.md](PROJECT_STATUS.md) 为最新状态入口；v5.6 §0.1 仅保留 2026-10-27 的历史快照。专题研究记录和局部测试必须按实际证据判断，不能自动关闭整个任务。
- **当前模型基准与统一原则：** 原论文 \(S+\mathrm{VLL}\) 单 VEV UV 模型是所有非中微子审稿问题、推导和专题研究的默认基准。Major Point 3/4.1 可以在各自的中微子问题范围内讨论 \(\sigma+3N_R\) 等可选完成机制，但这不改变原论文场内容，也不得用于其他问题。执行时必须遵守 [DEC-15 统一模型适用范围与审稿一致性原则](审稿意见-gpt/项目规范/研究决策与不可回退事项.md) 和 [审稿回复写作原则 §2.1](审稿意见-gpt/写作规范/审稿回复写作原则.md)。Major 3 的扩展模型分析仅作回复论证/历史研究记录，不是论文已经加入该机制的证据；正文修改必须以实际选定源码为准。


## 面向研究者的阅读版

如果希望从物理问题本身连续阅读，而不是按 AI 技术任务和审计条目查找，请使用独立的**研究者完整版**：

- [研究者完整版：DW13678 审稿意见与论文修订工作手册](审稿意见-gpt/研究者阅读版/DW13678_论文修订与理论核查手册_研究者完整版.md)
- [轴矢量模型完整讲解与推导笔记（修订版）](审稿意见-gpt/研究者阅读版/axial_U1_LmuLtau_complete_explanation_revised.md)
  - 连续讲解 UV 模型、VLL universal-seesaw 质量生成、低能 EFT、标量扇区及模型适用边界；以原始投稿稿为事实基线，不替代原文或执行手册。

这份手册面向人类读者，重点解释物理原理、推导、计算方法、适用条件和审稿意见的处理逻辑。它是解释性阅读材料，不维护独立任务状态，也不替代 v5.6 执行手册或技术参考。

## 原始只读基线

- `archive/manuscript-baselines/axial_vector_model_building-v6.pdf`：当前存档论文基线，用于核对当前版本内部公式、符号与论证的一致性。
- `审稿意见-gpt/原始审稿材料/dw13678_report_1_a.pdf`：原始审稿报告。
- `审稿意见-gpt/原始审稿材料/dw13678_report_1_a.md`：审稿报告文本版；核对原文措辞时以原始 PDF 为准。

项目已确定：不再把审稿报告与当前存档 v6 在 Eq. (30)/(34) 上的表达差异作为追查实际送审 PDF 版本的任务；后续以当前 v6 内部一致的定义、归一化和推导为基准。除非作者明确重新开启该问题，不应将旧 PDF 版本差异列为阻塞。

## 技术参考的版本关系

- v5.7 Markdown 是当前可编辑的技术参考主线；v5.7.1 LaTeX 是后续扩充但尚未与 Markdown 逐项同步的历史快照。需要查找额外细节时可对照 LaTeX，但新修改先进入 Markdown；不能将 LaTeX 中尚未同步的旧任务指令当成当前状态。
- 按 Markdown-first 的维护约定，后续技术内容修订先在 v5.7 Markdown 中整合、核验；待研究内容稳定后，再把仍需保留的 LaTeX 独有内容合并进 Markdown，并统一生成 LaTeX/PDF。当前 v5.7.1 LaTeX 可用于查阅历史推导，但不应单独更新或作为第二套任务状态来源。
- 对 Eq. (30)/(34) 的项目决策已于 2026-10-26 明确：当前存档 v6 是执行基线，不再追查审稿人实际收到的 PDF 版本。该决策优先于 v5.7.1 LaTeX 中尚未同步的旧版指令；待最终 Markdown 主文档稳定后再统一转换和更新 TeX/PDF。
- 研究者完整版用于连续阅读；最新修改方案为 [PR #14 中的 Diff v2.4](https://github.com/lm846802297-bit/axial-vector-review-response/pull/14/files)，尚未正式验收，不代表主文已修改。 [Diff v2.2 历史归档](审稿意见-gpt/当前执行/axial_vectorv6-diff-v2.2-原子映射与证据双轴-BelleII与Fig2闭环-2026-10-23.md) 保留 T-00–T-14 的历史计划，不再维护当前状态；Diff v2.3 与 2026-10-23 一致性核查报告也仅作为历史材料。

## 工作纪律

执行任务状态以根目录 PROJECT_STATUS.md 为准；v5.6 §0.1 仅作为 2026-10-27 历史状态快照。技术内容的新增/修订维护在 v5.7 Markdown，v5.7.1 LaTeX 仅用于查阅尚未同步的历史细节；物理分析与未决判断查 v4.1，并对照研究者完整版及具体计算记录。原始论文和审稿报告作为只读事实材料。任何任务状态变化都应有可追溯证据；文档检查通过不等于物理结论已经验证。


## 历史归档与旧工作稿

- [DW13678 审稿修订工作手册 Markdown 主文件（2026-10-23 历史快照）](审稿意见-gpt/历史归档/2026-10-23/DW13678_审稿修订工作手册_Markdown主文件-历史快照.md)：保留自历史分支 `docs/dw13678-markdown-master-20261023`，用于追溯早期的专题结构、推导与任务安排。它不是当前状态入口；当前任务状态看根目录 PROJECT_STATUS.md，任务步骤看 v5.6 执行手册，当前技术参考看 v5.7 Markdown，研究者连续阅读使用“研究者完整版”。
- [分支成果核查与 main 同步记录（2026-10-27）](审稿意见-gpt/当前执行/分支成果核查与main同步记录_2026-10-27.md)：记录 13 个非 main 分支的文件核查、已同步成果、保留原因与未完成科研边界。
