# 研究记录

语言：简体中文。英文原版：[README.md](README.md)。

本目录包含实质性研究任务的活跃 Scientific Diff 记录。每条记录都区分已经执行的计算、实际运行过的检查，以及仍未解决的物理主张。

**项目层级：** 当前这些记录描述的是父项目 `axial-vector-model-building` 下的 `vll-higgs-singlet-uv-eft` 工作流。该工作流不是独立的顶层项目。参见[项目注册表中文说明](../projects/README.zh-CN.md)。RC-001 仍然是研究变更/记录 ID；规范子图记录是与之关联的子记录。第一阶段有意保持所有现有路径不变。

## 活跃记录

| ID | 研究任务 | 状态 | 当前结论 |
|---|---|---|---|
| [RC-001](RC-001-vll-higgs-singlet-uv-eft.md) | VLL–Higgs–Singlet UV–EFT 单圈匹配：基线与证据链整合 | 验证进行中 | 已记录指定 EFT bubble-plus-contact 子集的精确质量基底 h–s 核及局域极点反项。核函数脚本通过 15 项符号检查；与源记录 `252 对齐的非壳层/EOM 复现通过 46 项精确有理数检查；`301 系数审计通过 5 项检查。对于指定 Yukawa 箱图扇区，二点结果与旧版壳层四点代表式之间历史上的 4/3 差异，已通过主源 v153 的 `252 及 `301.1–301.4 中的非壳层/EOM 补全得到协调。完整模型层级的 Wilson 系数向量闭合、更高维 EFT 软图/源插入，以及 dimension-eight 硬匹配仍未完成。主源纯势能代表式将 `(C_5^2)` 软势能常数极点归入 `(X^2Y^2)`，本记录中也已独立核查；这并不等于完整的 dimension-eight Wilson 系数向量。主源 `243.4 表明，在固定 VEV 条件下，`(Q_{LD},Q_{RD})` 的 VEV 波函数插入对受限 `(C_5^2)` 气泡的贡献从 `O(M_E^{-4})` 开始，但其他耦合扇区及潜在 IR 增强仍需检查。独立图级验证也尚未完成。扩展后的 [EFT 软拓扑清单](RC-001-eft-soft-topology-census.md)对 26 类候选标量、费米子、电流/源项及 dimension-eight 拓扑家族进行分类，其中包括交叉的 C5 C5* 双费米子/双标量与四费米子通道，以及同阶 Q6 加四次耦合/规范修正。解析软圈笔记 [RC-001-dim6-soft-loop-integrals-and-checks.md](RC-001-dim6-soft-loop-integrals-and-checks.md) 与 SymPy 交叉核查脚本 [calculations/RC-001-dim6-soft-loop-crosscheck.py](../calculations/RC-001-dim6-soft-loop-crosscheck.py) 目前记录 41 项精确检查，其中包括对交叉电流和 Q6 加四次耦合硬系数的独立 Feynman 参数复现、交叉电流及四费米子硬/软抵消，以及 Q6 加四次耦合的 EOM 核。这仍然只是积分层级证据：外部图计算软件包验证、完整规范/反项集合、统一算符基底中的 EOM/源项向量，以及完整 dimension-eight 硬/软匹配仍未完成。参见 [RC-001 主张—证据矩阵](RC-001-claim-evidence-matrix.md)。 |
| [RC-001-GAUGE-SUBGRAPHS](RC-001-gauge-subgraph-change-record.md) | 对 `Q_{LD}`、`Q_{RD}` 和电流/源算符的 dimension-six 规范修正 | 验证进行中 | 已记录重线及部分标量主积分子模块、加性 `B-A'` 阈值、全部四个共轭 Yukawa 顶点的带符号电荷因子，以及完整纯轻粒子顶点子族在 `O(M_E^{-2})` 阶的抵消。另行记录了一个有条件的混合 `B-A'` 输入参数反项子模块，并将其与完整混合规范振幅区分开来。包含重粒子的 FF/FS Yukawa 顶点硬子模块现已完成求值；交叉箱图、完整 UV–EFT 减法、Ward 恒等式以及统一算符基底中的 EOM/源项约化仍未完成。这是 RC-001 的子记录，不是已闭合的匹配结果。 |

## 规则

- 每条记录都应绑定到不可变基线和可识别的产物。
- 使用稳定的主张 ID，并维护主张—证据矩阵。
- 将实时主张条目保存在项目专属矩阵中；通用模板不得包含项目专属主张。
- 不要将 Mathematica 符号检查计作 FeynArts/FeynCalc 图级验证。
- 未完成剩余匹配和可观测量层级步骤前，不得将有条件成立或固定扇区的结果提升为完整模型主张。
