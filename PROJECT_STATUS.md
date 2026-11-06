# PROJECT_STATUS — Axial-vector paper revision and referee response

**状态快照日期：** 2026-11-06（PR #38–#50 已合并；PR #54 已合并；PR #55 Open / 未合并；PR #52 Closed / 未合并且保留研究分支；PR #53 Open / Draft）

**本状态快照的初始核验基线：** 243b0e62d9c3912525d1144971a1e81c2af84db7（PR #36 合并前）  
**项目启动机制合并提交：** [9b4e17519230e9eef65b34b643d3a1f8c19f46a2](https://github.com/lm846802297-bit/axial-vector-review-response/commit/9b4e17519230e9eef65b34b643d3a1f8c19f46a2)  
**用途：** 每次启动项目时快速恢复当前阶段、权威文件和下一步工作。本文件是可更新的状态快照，不替代物理推导、原始论文、计算证据或作者最新指示。

> **更新原则：** 任务完成、作者改变观点、PR 合并、论文基线更换或计算结论更新后，应检查并更新本文件。尚未重新核验的内容标为“待核验”，不得沿用旧状态作确定陈述。

## 2026-11-06 更新：PR #55 Minor Points 论证扩充与长期写作规范

[PR #55](https://github.com/lm846802297-bit/axial-vector-review-response/pull/55) 继续更新正式回复信及其写作规范，当前保持 Open、未合并。工作分支为 review/response-point-conclusions-20261106。

- **正式回复信：** 在此前 Major 3、Major 4.2、Major 4.3 和 Minor 6.5 结尾修订基础上，进一步扩充 Minor 1–5、6.1、6.2、6.4、6.5、6.6；Minor 6.3 经核对保持不变。所有非中微子问题继续采用原论文单 VEV \(S+\mathrm{VLL}\) 模型。
- **后续最小纠错：** Major 3 明确原始 \(S\)-only 模型与可选 \(\sigma+3N_R\) seesaw 的区别；Major 4.3 统一 \(\mu/\tau\) 的带符号耦合并将 small-mixing 统一称为 condition/domain；Minor 3 澄清带符号耦合与绝对值；Minor 4 澄清四个混合角分别受同一数值上限约束而非彼此相等。另补充 Major 2 的 VLL Yukawa 微扰性依赖、Major 4.2 的保守不等式和 Major 4.4 的完整超新星输运限定。Major 1.3 的局部扫描边界保持不变。
- **新增物理论证：** Minor 5 增加 \(A_{\rm LR}^\mu\)、\(P_\tau\) 的手征振幅解析投影、\(A'\) 总宽度部分道分解、\(ee\) 通道高动量 kinetic-mixing 适用性以及 \(e^+e^-\to Zs\) 的 Higgsstrahlung 缩放关系；Minor 6.5 从两个活性 chiral-neutrino 道推导寿命上界、boost 后飞行距离和 dimuon 阈值抑制。没有加入未经复核的 collider reach 数值。
- **长期规范：** 在审稿回复写作原则新增强制 §2.2「论证充分性原则：从结论陈述到可复核的物理论证」，并同步 §5、§6、§6.1、§7。覆盖物理原因、公式来源、benchmark/近似/数值意义、实验适用性映射和多子问题逐项回答；强调不机械增加篇幅。
- **内部记录：** Minor Points 论证扩充与复核记录、全信结尾修订审查记录均已写入 2026-11-06 目录。
- **静态验收：** 78 次引用出现、39 个唯一 citation keys 全部解析；LaTeX 环境配对、花括号、标签和交叉引用检查通过；Minor 6.3 与 main 原段落逐字一致。
- **完整 LaTeX/PDF 验收：** 已通过 GitHub Actions Run [#3](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42146091113) 对 PR 分支源码完成 `latexmk -g -pdf -bibtex` 编译；最终 PDF 为 59 页 A4，根目录文件为 [Replies_to_Referee_3_referee_facing_2026-11-04.pdf](Replies_to_Referee_3_referee_facing_2026-11-04.pdf)，生成提交为 `8c21ff02a216e636e1655ddb0d1c38488ec6714b`。最终 LaTeX `.log` 无未解析引用/交叉引用，BibTeX `.blg` 无缺失条目或数据库错误；59 页均以 150 dpi 渲染并完成人工页面预览检查。未发现公式/表格裁切、缺字、溢出页边距、空白页或异常分页。仅有一处非阻塞 `Underfull \\hbox`（badness 1199，TeX 第 555–557 行），未发现 `Overfull`。
- **本轮未涉及：** 论文正文、图表和 BibTeX 数据库均未修改；完整数值脚本 clean-environment 重跑、detector-level collider 模拟和全仓库测试套件仍未执行。Actions 仅用于正式回复信编译、引用检查和页面渲染。

**下一步：** 作者审阅 PR #55 的实际 TeX diff 与已编译 PDF，再决定是否合并。仅用于视觉检查的临时页面预览文件已在审阅后清理。PR #55 保持 Open、未合并。

## 2026-11-05 更新：模型范围纠正与研究 PR 替代关系

PR #50 已于 2026-11-05 Squash Merge 至 main，合并提交为 [51a245b0a36703f40c24ca469d6969e70abc8954](https://github.com/lm846802297-bit/axial-vector-review-response/commit/51a245b0a36703f40c24ca469d6969e70abc8954)。本次进一步纠正研究范围：Major Point 3/4.1 的额外中微子完成机制只属于对应问题的专门回复论证，不改变原论文 UV 场内容，也不改变其他审稿问题的模型基准。

**2026-11-05 统一原则（DEC-15）：** 原论文单 VEV 模型是所有非中微子问题的默认基准；Major 3/4.1 可独立讨论中微子机制；不同模型公式和实验限制不得未经重新推导或 matching 直接混用；回复信讨论扩展不代表论文已采用；每个问题必须明确模型、场内容、理论输入、参数关系、近似、适用范围和证据来源。目标是回应原论文的审稿质疑，而不是逐步把论文扩展成另一个 UV 模型。详见研究决策登记表 DEC-15 与审稿回复写作原则 §2.1。

- **旧 PR #30：** 已关闭且未合并；其错误采用双 VEV 映射的 PR #51 也已关闭且未合并。现由 [PR #53](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) 替代。PR #53 从当前 main 创建，严格使用原论文单 VEV 模型 \(m_{A'}=2|g_X|v_s\)、\(G=a_s\)，保留通用电流半康普顿振幅和局部热率计算。六项单 VEV 映射测试通过；介质静止系 T/L opacity、trapping、SN profile 和最终 SN1987A/LESN 曲线仍未完成。
- **旧 PR #32：** 已关闭且未合并；现由 [PR #52](https://github.com/lm846802297-bit/axial-vector-review-response/pull/52) 替代。PR #52 从当前 main 创建，研究原论文的单 VEV 径向标量，保留 Belle II 来源台账、重铸协议、逐点分类框架和部分宽度计算器。Belle II 逐质量补充数据提取、实验 benchmark 复现、完整宽度/分支比/寿命、产生率、接受度和质量扫描仍未完成。
- **PR #52：** 已 Closed、未合并；其研究分支 \`research/radial-scalar-original-model-belleii-20261105\` 仍保留，研究成果未合并、未删除。
- **PR #53：** 保持 Open / Draft；其研究分支 \`research/stellar-cooling-original-uv-model-20261105\` 独立保留。
- PR #52/#53 均不修改论文正文或正式回复信，也不是当前审稿回复的前置条件。旧 PR 的讨论和提交保留作历史溯源，不合并其错误模型范围的提交。

- **PR #54：** 已合并至 \`main\`，合并提交为 [\`0f3816e3e62dd7668fca1d4aee5e8749708f99f2\`](https://github.com/lm846802297-bit/axial-vector-review-response/commit/0f3816e3e62dd7668fca1d4aee5e8749708f99f2)。该 PR 修正正式回复信中 Major 1、2、4.2、4.4 对 Major 3 扩展的跨问题引用，并将中微子完成机制限定为 Major 3/4.1 专门回复内容。

**统一模型边界：** 除 Major Point 3/4.1 的专门中微子回复段落外，所有非中微子审稿回复和专题研究均以原论文 \(S+\mathrm{VLL}\) 单 VEV UV 模型为准。不得将 Major Point 3/4.1 中讨论的可选扩展机制作为原论文已经采用的场内容。
## 2026-11-05 更新：PR #53 原论文单 VEV 轴矢量恒星冷却计算（Draft）

[PR #53](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) 从当前 main 的 \`d3c8c573e0b219dbcb4be62dc57f77fdc04c4f96\` 创建，替代旧 PR #30 及错误采用双 VEV 映射的 PR #51；两者均关闭且未合并。

- **原论文模型映射：** \(S=(v_s+s+ia_s)/\sqrt2\)、\(Q_X(S)=2\)、\(m_{A'}=2|g_X|v_s\)、\(G=a_s\)。在小 VLL 混合 benchmark 下 \(y_{s\ell\ell}=m_\ell/v_s\)，Goldstone/current 关系为 \(m_\ell/v_s=2|g_A^\ell|m_\ell/m_{A'}\)（\(|g_A^\ell|=|g_X|\)）。
- **保留的计算：** 显式 Dirac 旋量半康普顿振幅、EM Ward identity、实验室系/CM 截面对照、Klein–Nishina 对照、轴矢量纵向标度、均匀介质局部热产生率及积分阶数/截断扫描。
- **原模型中微子规范流边界：** \(A'\to\nu\bar\nu\) 仅使用原论文 \(L_\mu-L_\tau\) 活性味规范流（无质量近似下的 \(\nu_\mu,\nu_\tau\)，电子味不耦合）；不引入额外中微子态或质量完成机制。
- **本地验收：** 单 VEV 映射测试 6/6 通过；通用电流半康普顿振幅的 Ward residual 分别为 \(2.252\times10^{-9}\)、\(2.159\times10^{-9}\)；热率 order 10→12 的率和发射率变化分别为 0.0108% 和 0.0202%。详细数值见 PR #53 的 validation record。
- **分支比口径：** PR #53 的 \(\mathrm{BR}_{\nu\bar\nu}\) 数值仅为保留 \(\nu\bar\nu+\mu^+\mu^-\) 的两通道近似；动能混合诱导的 \(e^+e^-\) 及其他开放道未纳入，不能当作完整物理分支比。
- **未完成：** 介质静止系 T/L 分辨吸收、opacity、trapping、SN profile、diffusion 和最终 SN1987A/LESN 曲线；不声称已得到超新星排除。
- **范围：** PR #53 保持 Open / Draft；不修改论文正文或正式回复信。

## 2026-11-05 更新：Major Point 1.3 公式链条与近极点诊断补强（PR #49，已合并）

[PR #49](https://github.com/lm846802297-bit/axial-vector-review-response/pull/49) 的基准为 main SHA 4abcf13c45789f75deee27a4b6a3cc9480639448，分支为 review/major1.3-higgs-portal-higgs-strength-20261104，已于 2026-11-05 合并至 main。本轮仅修改回复信及其内部证据/同步文档，不修改论文正文。

- **P0：** 正式回复补入 \(2\times2\) charged-lepton/VLL 质量矩阵、规范基底 \(h,s\) Yukawa 顶角、质量本征态旋转、\(C,D,K\) 定义和完整质量本征态一圈费米子自能公式。
- **P0：** 补入 exact full-minus-light EFT subtraction、保留的 bubble-plus-contact soft 子集，以及 hard/soft 数值分解。将结果记为 \(\Pi_{hs}^{\mathrm{ret}}\)，并明确该 soft 子集不是完整同阶 EFT soft/counterterm 集，避免把条件性数值写成完整 UV pole 预测。
- **P0：** 修正“zero-tree-level-mixing”歧义：\(\lambda_{HS}^{\mathrm{EFT}}(M_E)=0\) 是匹配 EFT 的局域混合边界；对应 \(\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E}\ne0\)。补充 portal-induced mass entry 与 loop counting。
- **P0：** 将 \(\mu_h^{\mathrm{pole}}\) 改为 \(\delta\mu_h^{(\mathrm{mix,LO})}\)，明确它是 mixing-only leading rate diagnostic，而不是完整物理 pole signal strength。
- **P1：** 明确 \(m_s\) 是未混合对角质量输入；补充 \(\Gamma_s(s\to A'A',\mu^+\mu^-,\tau^+\tau^-)\) 公式及 Benchmark B 的开闭道条件、宽度和非简并极点位置。
- **P1：** 补充 \(\lambda_S\le4\pi\) 对应的 \(m_s^{\max}=\sqrt{8\pi}v_s\)：Benchmark A 为 \(355.4\) GeV，B 为 \(1579.2\) GeV。明确 \(10\)--\(150\) GeV 是 Higgs 极点附近局部诊断窗口，不是整个微扰性区间的扫描。
- **近极点数值：** Plan-C-lite 脚本新增 \(125.20\)--\(125.30\) GeV、\(0.1\) MeV 步长的复数极点局部扫描。相同 1001 点算法已在 in-session Python 环境独立复现；A/B 的 1001 个点均收敛。更新后的仓库脚本尚未在干净容器中整文件重跑，验证记录明确区分了这两类证据。
- **P2-lite：** 已新增 CP-even radial-scalar 三类 bubble 图的解析表达式和可复现数值脚本；正式回复信现直接包含等质量与非等质量 \(\Delta\bar B_0\) 的闭式表达式、Feynman 参数表示及代表性函数值。\(m_s=100\) GeV 与 \(m_s=m_h\) 两点的零动量相减子集数值仍只作为内部诊断：\(m_s=100\) GeV 时子集模长为 A: \(24.7547\) GeV\(^2\)、B: \(0.641797\) GeV\(^2\)，分别为当前保留费米子 \(|\Pi_{hs}^{ret}|\) 的 57.77 和 6.656 倍。闭式结果与 8,000 区间 Simpson 积分对全部 12 个 benchmark/质量/拓扑组合的最大相对差为 \(9.97\times10^{-15}\)，2k/4k/8k/16k 收敛检查通过。该比值只说明不能单凭形式 loop counting 断言标量项相对有限费米子结果必然很小；此子集不是完整两圈 UV--EFT 匹配，不能直接加到 \(\Pi_{hs}^{ret}\) 或作为物理极点修正。Goldstone 顶角已解析列出，但其数值贡献需与 gauge/ghost、混合 VLL--scalar 图及 tadpole/VEV 反项一起处理；近简并区继续标为未评估。详见 2026-11-05/Portal_induced_scalar_loop_power_counting_P2_lite_2026-11-05.md。
- **低能 EFT 交叉核查：** 补充 \(q^2\ll m_s^2,m_{A'}^2\) 下的 scalar four-lepton operator 与 \(A'\)-exchange 系数尺度比较：\(|C_{\mu\mu}^{(s)}/C^{(A')}|\sim4m_\mu^2/m_s^2\leq4.5\times10^{-4}\)（\(m_s\geq10\) GeV），而 \(\tau\tau\) 在 \(m_s=10\) GeV 时仍可达约 \(0.13\)。该比较仅是不同 Lorentz 结构的系数量级，不是过程级率比；不据此忽略 tau-sensitive scalar processes。
- **范围：** Major 1.3 继续只讨论原始单标量 \(S+\mathrm{VLL}\) 两态系统，不混入 \(\sigma,N_R,\mathrm{PMNS}\) 或三态标量势；近简并区不赋予 allowed/excluded 状态。

**验证边界：** 没有运行 CI；没有对更新后的 Plan-C-lite 脚本做干净容器整文件执行；回复信 PDF 尚未按 PR #49 的 TeX 重编译或视觉检查。main 根目录现有 48 页 PDF 仍是 PR #49 修改前的旧版，不包含 PR #49 的 TeX 修改。PR #49 已于 2026-11-05 合并。

## 2026-11-05 更新：回复信解析论证一致性修订（PR #50，已合并）

[PR #50](https://github.com/lm846802297-bit/axial-vector-review-response/pull/50) 已 Squash Merge，合并提交为 [51a245b0a36703f40c24ca469d6969e70abc8954](https://github.com/lm846802297-bit/axial-vector-review-response/commit/51a245b0a36703f40c24ca469d6969e70abc8954)；分支为 review/response-analytic-consistency-20261105。正式回复信的本轮修改限于以下内容：

- **Minor Point 6.1：** 将 \(g_X\) 上限从旧值 \(10^{-1}\) 修正为实际 Fig. 2 展示窗口的 \(1\)，与 Major Point 2 和 Minor Point 1 一致。
- **Major Point 4.4：** 引入 Kahn et al. (2017) 的轴矢量恒星冷却讨论；用 \(O(10^{-10})\) 表示 Wang--Zhang 矢量参考的 SN1987A 灵敏度；明确 neutrino coalescence 与不可见宽度使用原论文 active-flavor \(L_\mu-L_\tau\) 规范流；不引入额外中微子态、active--heavy mixing 或 Major Point 3 的可选完成机制。
- **Major Point 4.4：** 新增矢量流守恒、轴矢量流散度及 Goldstone 等效纵向耦合关系，解释矢量 semi-Compton 产生率不能直接移植；将低动量 kinetic-mixing 抑制限定为电磁流介导过程，不用于 neutrino coalescence 或直接轴矢量 semi-Compton。
- **Major Point 1.3：** 本轮复核后撤销最初拟议的三处文字精简，恢复 PR #50 修改前 `main` 的原有表述；PR #50 最终不修改该部分，完整保留闭式泡图表达式、UV--EFT 匹配、benchmark 数值、数值验证精度及各子集的适用范围和未完成项。
- 新增 [解析论证完整性审查与修订记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-05/回复信解析论证完整性审查与修订记录_2026-11-05.md)。

**验证边界：** TeX 花括号、环境配对、标签唯一性和 citation-key 静态核查通过；36 个唯一引用键均可解析。新增公式片段通过独立 pdflatex 编译。完整回复信 PDF 尚未重编译或逐页视觉检查；未运行 CI；没有新增超新星输运计算；论文正文未修改。根目录现有 PDF 仍是 2026-11-04-r2 历史编译件，不包含 PR #49/#50 的 TeX 更新。

## 2026-11-04 更新：Major 4.4 轴矢量 stellar-cooling 文献调查（PR #46）

PR #46 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 [b453e9be09a4f67d00cb90dfb85435c07472c5b4](https://github.com/lm846802297-bit/axial-vector-review-response/commit/b453e9be09a4f67d00cb90dfb85435c07472c5b4)。新增文档 [Major 4.4 轴矢量 stellar-cooling 文献适用性调查](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.4-轴矢量stellar-cooling文献适用性调查_2026-11-04.md)，并更新 README 导航与 DEC-09。

调查确认：Kahn et al. 2017 已明确讨论轴矢量 \(U(1)\) 的 stellar cooling，但没有本文模型的 SN1987A 数值曲线；EPS-HEP 2019 有轴矢量核子耦合 SN 报告；Bell et al. 2024 对轴矢量核子流使用的是 vector SN proxy。对本文最直接的定量映射是与常规 \(L_\mu-L_\tau\) 完全相同的中微子 coalescence 与不可见中微子宽度。常规矢量 \(L_\mu-L_\tau\) 的完整 SN 曲线不能直接移植，因为轴矢量缪子 semi-Compton、纵向模式、\(\mu^+\mu^-\) 阈值宽度和 LESN 能量沉积不同。

- 保留“stellar cooling 对 sub-GeV 区域相关”的判断，不把矢量模型曲线作为本文轴矢量模型的完整排除。
- 文档区分直接轴矢量文献、矢量 \(L_\mu-L_\tau\) SN 参考、相同的中微子子过程，以及尚需模型特定计算的部分。
- 不修改回复信 TeX 正文或论文源码；本次仅修复回复信的 BibTeX 构建依赖并补全三条文献元数据，不声称完成新的 SN luminosity、opacity、trapping、LESN 或 WD emissivity 计算。
- 未运行 LaTeX 编译、PDF 视觉检查或 CI；这些状态不作通过声明。
 
### 回复信参考文献与 BibTeX 问号核查（2026-11-04）

作者指出回复信 PDF 中多处引用显示为 `[?]`。对当前根目录权威 TeX 与两份 BibTeX 数据库进行了静态核查：

- 找到 **45 条引用命令、72 次 citation-key 出现、34 个唯一 citation keys**；34 个键全部存在于两份 `.bib` 数据库中。
- 未发现重复 citation keys；两份 BibTeX 文件的花括号静态平衡检查通过；TeX 源码没有 `[?]` 或 `??` 字面占位符。
- 因此，当前源码证据不支持“34 个引用键缺失”的判断。更可能的问题是 BibTeX 生成/读取环节，而不是正文的 `\cite` 键没有对应条目。
- 定位到关键构建隐患：回复信位于仓库根目录，使用 `\bibliographystyle{JHEP}`；原 `JHEP.bst` 仅位于 `overleaf-source/axial-vector-model-building-v6/`。本地 BibTeX 路径测试表明，默认样式搜索不会递归发现任意项目子目录中的 `.bst`。现已将原文件逐字节复制到仓库根目录；其 Git blob SHA-1 与原文件相同：`d39cbe846e531ed7be07eebb11be0bd72d675579`。
- 补全三条被引用文献的元数据：`NA64:2023lightDM` 加入 PRL 131 (2023) 161801 与 DOI；`geiregat1990first` 加入 DOI；`He:2024twoSingletHNL` 加入 arXiv:2401.14687。2026 年的 `Fiorillo:2026wso` 与 `Wang:2026supernova` 仍为预印本，未虚构期刊或 DOI。
- 最新可恢复包为 [2026-11-04-r2 manifest](archive/reply-letter/snapshots/2026-11-04-r2/manifest.md)，包括回复信 TeX、两份 BibTeX 数据库和 `JHEP.bst`。
- **回复信 PDF 已按要求完成重编译与视觉检查（2026-11-04）。** 以源码基线 `edce6a37a162e9fe97b5162bd2107656f50865db` 执行 `pdflatex → bibtex → pdflatex → pdflatex`；BibTeX 成功读取两份数据库及根目录 `JHEP.bst`，生成 34 条文献。最终 PDF 共 48 页，未发现未解析引用/交叉引用或 `[?]`/`??` 标记，所有字体均已嵌入。检查了全篇缩略图及表格、公式、参考文献页；未见裁切、重叠或不可读内容。编译日志保留一条 `Overfull \hbox (44.0084pt too wide)`，对应源码第 757–774 行的 NA64 六列表格（PDF 第 29 页）；该表在视觉检查中仍完整可读。正式 PDF 已提交到仓库根目录。此项没有运行 CI.

 
### 同步补充：正式回复信不可变源码备份

PR #46 同时加入正式回复信归档结构 `archive/reply-letter/`。根目录 TeX 仍是唯一可编辑权威版本；归档目录中的 `.snapshot` 文件只用于恢复，不作为第二份工作稿。

- 源版本固定为 main commit `d9b262798f80c0f109f328b1b0019191e99d5437`。
- 已保存回复信 TeX、两份 BibTeX 输入文件及根目录 `JHEP.bst`；最新 r2 快照的四份归档文件均记录 Git blob SHA-1。
- 归档说明和 manifest 记录原始路径、blob SHA-1、恢复步骤及 GitHub 按 commit SHA 下载完整仓库快照的链接。
- TeX 静态扫描未发现 `\input`、`\include` 或 `\includegraphics` 依赖；`JHEP.bst` 已作为仓库根目录构建依赖保存，LaTeX packages 仍属于编译环境依赖。正式 PDF 已在后续提交 `a9edb509dc47932b872465b5d0dd1263bd1c26da` 中编译并上传；编译来源与 PDF SHA-1 见 [2026-11-04-r2 manifest](archive/reply-letter/snapshots/2026-11-04-r2/manifest.md)。
- Git tag `reply-letter-2026-11-04` 尚未创建。Tag 是 Git ref，不能作为文件纳入 PR diff；建议 PR 合并后将该 annotated tag 指向上述固定源 commit，而不是后续 main HEAD。



## 2026-11-04 更新：Major 4.3 有限矢量耦合与小混合参数域（PR #45）

PR #45 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 `bc2a1c20e277d51ef2d6add68c84b1c5af1c533b`（[GitHub commit](https://github.com/lm846802297-bit/axial-vector-review-response/commit/bc2a1c20e277d51ef2d6add68c84b1c5af1c533b)）。修改前重新阅读了 `AGENTS.md`、`README-先读这里.md`、强制写作规范、main 正式回复信、正文同步清单、DEC-08 和 2026-10-23 第三段会议文字稿。

正式回复 Major 4.3 明确将本文轴矢量现象学限定在有限 VLL 质量下的 `|theta_lL|, |theta_lR| <= 1e-2` 小混合域，并用 `m_l ≃ theta_lL theta_lR M_E` 说明该域对应有限的多 TeV VLL 质量。新增 vector-specific 与 axial 限制映射条件：
`tan^2(theta_lR) < gV_lim(mA')/gA_lim(mA')`，
并说明在角度上限处，矢量专属耦合限制必须比同质量、同假设下的轴矢量限制严格约四个数量级，才可能产生更强的共同 `g_X` 限制。回复保留 trident 与 `(g-2)_mu` 过程贡献比，明确它们不是独立实验排除限；增加 BaBar/Belle II/CMS 四缪子 FSR 在远离阈值区的 vector/axial 同阶 reach 对照；新增 dimuon 阈值的宽度比及质量依赖角度条件，避免将小混合结论推广到阈值敏感衰变或所有实验。

- 修改正式回复信 Major 4.3；新增内部专项推导记录；同步论文正文待修改清单、DEC-08 和本状态文件。
- 不修改论文源码，不新增矢量排除图，不进行全 UV 扫描或 collider recast。
- 静态核验覆盖 TeX 花括号、环境配对、方程标签、公式与现有 benchmark 的一致性；具体结果见 PR 描述。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些验证通过。

## 2026-11-04 更新：Major 3 / 4.1 中微子记号与 S-only 条件性表述（PR #44）

PR #44 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 `e78ae8a4b26a9b595e64ad0eaf52e7e836e50751`。正式回复信统一以 `y^nu_alpha` 表示中微子 Dirac Yukawa 耦合，并保留 `y_e, y_mumu, y_mutau, ...` 作为带电轻子 Yukawa 参数。Major 3 的 `m_D` 定义和 Major 4.1 的重复定义均已同步。

Major 4.1 将 S-only 纹理明确限定为：只有原电荷二标量 S 提供残余 Z2 破缺、没有其他破缺来源时，允许的中微子质量纹理保持 `e ⊕ (mu,tau)` 分块。文字同时明确该纹理是条件性对称性结论，不是原始带电轻子构造已经给出的中微子质量预测。Major 3 的 EFT 段落也统一为相同条件表述。

- 修改文件：正式回复信 TeX、Major 3 专项修改对照、论文正文待同步修改清单。
- 保留原 charged-lepton Yukawa 记号，避免将 `y_e` 等重新解释为中微子 Yukawa。
- 静态检查：中微子 Dirac 项和两处 `m_D` 均使用 `y^nu_alpha`；S-only 条件措辞一致；方程标签唯一；TeX 花括号及环境配对通过。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些检查通过；论文正文未修改。

## 2026-11-04 更新：Major 4.1 PMNS 论证强化（PR #43）

[PR #43](https://github.com/lm846802297-bit/axial-vector-review-response/pull/43) 已于 2026-11-04 通过 Squash Merge 合并至 main，合并提交为 9889beff08d827ede166f196f47fbb94db4a26f8。该修订严格按《审稿回复写作原则》处理 Major 4.1：先精确说明 S-only 残余 Z2 所给出的 U_PMNS = diag(1, U_23) 结构（允许非平凡 μ–τ 旋转，但缺少电子味混合，因此“严格单位矩阵”并不准确）；再给出保留 S、增加电荷一 σ 与三个 N_R 的可重整化完成机制；随后用 seesaw、含 U_L 的 PMNS 关系和 M_R = −m_D^T M_ν^−1 m_D 逆构造展示一般三味混合的构造性实现；最后核对新增单态中微子的异常抵消及双 VEV 的 A′ 质量关系。

- 正式回复只增加面向审稿人的物理论证；没有把分支、PR、内部任务或正文同步状态写入回复信。
- 内部[论文正文待同步修改清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)已同步记录 Major 4.1 的论证结构；论文源码、references 和 PDF 未修改。
- 已做静态检查：TeX 花括号平衡、begin/end 环境配对、无重复 equation label，Major 3 的方程引用和文献键存在。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些检查通过。

## 2026-11-04 更新：Major 4.2 动能混合与 NA64 质量依赖比较

Major 4.2 已补充有限轻子混合产生的非零动能混合、四态矢量耦合/真空极化、物理重态简并与共同裸质量下的残余阈值，并明确重 VLL 匹配尺度边界条件 \(\epsilon_{\rm ind}(\mu_{\rm match})=0\)。该条件只约束独立局域项，不令完整动量依赖物理混合函数为零。

[PR #42](https://github.com/lm846802297-bit/axial-vector-review-response/pull/42) 已于 2026-11-04 通过 Squash Merge 合并至 `main`，合并提交为 `de036d3cbb0fbf654055f5a0d14c67e81bc3061c`。回复 TeX 已扩展 NA64 Fig. 3 的 10、100、200、300 MeV 四点视觉读取区间；300 MeV 计入 dimuon 宽度并使用 `epsilon_eff = |epsilon_gammaA'| sqrt(Br_inv)`。读图区间约有 0.2--0.3 dex 不确定度，明确不是官方机器可读数据或 detector-level recast。按作者决定，本轮未重新编译完整回复 PDF；仓库中的 45 页 PDF 仍是本轮 TeX 更新前的历史快照，不应作为最新回复信使用。CI 状态检查为空。

- [Major 4.2 论证与论文修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-暗光子限制与论文修改对照_2026-11-04.md) 包含 K-01–K-05 正文同步建议、原始文献位置、四点 NA64 对照和适用条件。
- [计算入口](计算脚本/Major42_kinetic/check_kinetic_dark_photon.py) 与 [JSON](计算脚本/Major42_kinetic/outputs/kinetic_dark_photon_2026-11-04.json) 保存四点积分、Br_inv、epsilon_eff、NA64 视觉区间及比值。独立 mpmath 计算在 35/55 位精度下复核；仓库脚本尚未在仓库运行环境直接执行。
- [Major 4.2 验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-验证记录_2026-11-04.md) 记录当前源文件哈希和验证边界。
- **PDF 状态：** 当前 45 页回复 PDF 是本轮扩展前的编译快照，尚未根据最新 TeX 重新编译，不能作为本轮最终 PDF；需要重新编译并逐页检查。
- 原论文源码、bibliography 和 Fig. 2 未改；正文待按清单同步。Major 2/3 的核验哈希作为各自历史快照保留。

## 2026-11-04 已合并：Major 2 参数窗口

本轮基于 PR #40 合并提交 `f3d54dc9ec3c89bb6b8cbd22ecab6a92c4c83c3e`，按作者最新说明修改 Major 2：低质量端 g−2 已在图示实验室约束中主导，其渐近直线可继续延伸，扩图主要重复该区间；高质量端所用现有实验灵敏度减弱。天体物理适用条件与 UV 微扰性解释保留。

[PR #41](https://github.com/lm846802297-bit/axial-vector-review-response/pull/41) 已合并，合并提交 `49edfcee028717de3a315d76b6aad3e10a268e83`。正式回复和 PDF 已完成本轮核验：42 页，34 个引用键可解析，27 段审稿人引文及 Major 3 原文保持不变。

- 核对实际 Fig. 2 后，将回复 Major 2、Minor 1 和 DEC-06 的耦合上限从误写的 0.1 改为图中的 **1**；原图未改。
- [Major 2 修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-Fig2参数范围与论文修改对照_2026-11-04.md) 记录作者思路、推导、文献与 R-01–R-06 正文修改建议；[验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-验证记录_2026-11-04.md) 记录实际检查结果。
- 原论文源码和图文件不在本次修改范围；正文需按清单后续同步。两个作者本地原始 PDF 继续保留，不上传。
- 当前回复 PDF 随本轮更新；Major 3 验证记录的哈希保留为 PR #40 历史快照，避免与同名新 PDF 混淆。

## 2026-11-04 已合并：Major 3 中微子完成机制

作者已明确要求采用本轮文献调查结果修改回复并提交 PR。[PR #40](https://github.com/lm846802297-bit/axial-vector-review-response/pull/40) 已按作者要求合并，合并提交 `f3d54dc9ec3c89bb6b8cbd22ecab6a92c4c83c3e`。该工作原基于 GitHub main `613bca12`；GitHub 是同步到本地的基准，不将旧本地工作稿回推覆盖主线。以下为 PR #40 的成果与验证快照。

- 正式回复 Major 3/4.1 专门讨论双单态 type-I seesaw、详细算符/质量矩阵/PMNS/异常论证；该扩展仅属于中微子回复，不改变原论文场内容。Major 1、2、4.2–4.4 及其他非中微子回答继续使用原论文单 VEV (S+\mathrm{VLL}) 模型。
- 新增回复专用文献文件 `Replies_to_Referee_3_neutrino_references.bib`；归档论文 `main-v6.tex` 和 `references.bib` 未改。
- **原论文需要修改。** [N-01–N-14 修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major3-中微子完成机制与论文修改对照_2026-11-04.md) 列明位置、前后差异及条件；状态为待正文修改。
- 研究决策 DEC-01/02 已按作者新指示更新并保留旧立场；最小 S-only 的分块定理继续成立。
- 作者指定的两份 `审稿意见-gpt/专题研究/2026-11-04-*` 调查/候选稿一并归档；正式回复仍以根目录 TeX 为准。
- 本地两个原始 PDF 按作者要求保留，不纳入本次提交；其余仓库内容从 GitHub 主线更新并跟踪本次 PR 分支。
- 本轮 TeX 完整编译成功（41 页）；32 个引用键和 4 个标签均可解析，27 段审稿人引文与 main 一致。全文缩略图和新增关键页面已检查，详见 [Major 3 验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major3-验证记录_2026-11-04.md)。该记录以源文件 SHA-256 标识核验对象。
- 回复信 PDF 已随 PR #40 一并提交，路径为 [2026-11-04 编译版](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Replies_to_Referee_3_referee_facing_2026-11-04.pdf)，可与同目录的修改对照、验证记录直接比较。
- NuFIT 6.1 中心值上的 seesaw 构造脚本已复跑；完整输入/矩阵/耦合/残差 JSON 和运行入口见 [PMNS 重构结果](计算脚本/PMNS_Major3/outputs/pmns_tree_level_reconstruction_2026-11-04.json) 与 [PMNS 研究更新](审稿意见-gpt/当前执行/PMNS_Major3路线决策与扩展模型解析核查_2026-10-27.md)。该点是树级存在性示例，不是统计拟合或全参数约束结论。

以下为本轮前已合并工作的状态记录；若与本节的中微子路线冲突，以本节和最新决策登记表为准。

## 1. 项目当前阶段

当前项目处于**正式回复信主线已形成、Major/Minor 一致性审查已完成；PR #38、PR #39 均已合并；PR #39 已统一标量约束相关回复并归档 Table II 的详细论文修改方案；论文源码与 bibliography 尚未修改，待后续按清单同步**的阶段。

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

### Table II 回复信修订与论文修改方案（PR #39 已合并）
- [PR #39：Revise referee response and add Table II manuscript revision plan](https://github.com/lm846802297-bit/axial-vector-review-response/pull/39)（已合并，squash commit `76268abf`）：统一 Major Point 1、Minor Point 6.2 和 Summary 的标量约束数值、文献来源及物理适用条件；保留详细的未来论文修改清单。回复信不包含标量约束图；是否在论文中加入配套图留待后续决定。
- PR #39 仅修改正式回复信和内部清单/核查文档；未修改 main-v6.tex 或 references.bib。论文 Table II、正文解释和 Fiorillo v2 的 BibTeX 更新留待后续正文修订。回复信 TeX 尚未编译，PDF 视觉验收尚未完成。

### 已合并
- [PR #33](https://github.com/lm846802297-bit/axial-vector-review-response/pull/33)：按会议决策整理完整回复信。
- [PR #34](https://github.com/lm846802297-bit/axial-vector-review-response/pull/34)：Major/Minor 最终一致性审查；统一 Major 3/4.1 的 PMNS 结论及 Major 1/Minor 5 的 portal 假设。
- [PR #35](https://github.com/lm846802297-bit/axial-vector-review-response/pull/35)：回复信写作规范和项目级读取规则。
- [PR #36](https://github.com/lm846802297-bit/axial-vector-review-response/pull/36)：项目启动读取机制、PROJECT_STATUS 和可修改的研究决策登记表。

### 仍开放的专题研究 PR
| PR | 状态 | 当前已知边界 |
|---|---|---|
| [#53 原论文单 VEV 轴矢量恒星冷却/半康普顿计算](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) | Open / Draft；2026-11-05 新建 | 原论文单 VEV 映射与局部振幅/热率已验收；完整介质 T/L opacity 和 SN 输运未完成 |
| [#54 Major 3/4.1 回复范围隔离与原论文模型一致性](https://github.com/lm846802297-bit/axial-vector-review-response/pull/54) | Open / Draft；2026-11-05 新建 | Major 3/4.1 扩展仅限中微子回复论证；Major 1/2/4.2/4.4 恢复原论文单 VEV/原始 active-flavor current；静态检查通过，完整编译与视觉检查未做 |
| [#52 原论文单 VEV 标量 Belle II 后续研究](https://github.com/lm846802297-bit/axial-vector-review-response/pull/52) | Open / Draft；2026-11-05 新建 | 保留来源台账、重铸协议和部分宽度框架；Belle II 补充数据提取、benchmark 复现和 UV 重铸尚未完成 |

两个开放 PR 是独立研究工作流，不是正式回复信已完成的证据。继续前应重新检查 head、分支内容和验证记录；PR 仍开放不代表仍在持续推进。

## 5. 正式回复信与论文正文的状态边界

### 正式回复信
- 当前 main 权威回复信为根目录 `Replies_to_Referee_3_referee_facing_2026-11-04.tex`；PR #38 已合并，保留 PR #33/#34 的既有回复主线。
- 本次合并补入 Eq. (33) 的 s→A′A′ 与 s→ℓ⁺ℓ⁻ 偏宽度、visible-branching-ratio 论证；限定 Belle 1 GeV 数值映射只在 m_A′ > 0.5 GeV 时直接适用；并纠正 Belle II 两篇 scalar-specific 搜索的描述。
- 本轮 Major 3 修订版已完整编译并作全文缩略图及关键页面检查，见顶部更新及验证记录；此前未编译状态已由本次验证替代。
- PR #31 生成的 PDF 位于 2026-10-28 历史目录，文件名为 Replies_to_Referee_3_referee_facing_2026-10-28.pdf；它不是当前 2026-11-03 回复信的最终编译件。
- 当前编译件位于本地被忽略的 work/neutrino/latex-build/；未将历史 PDF 当作本轮验证证据。最终对外提交前仍须与已修订论文作整套一致性验收。

### 论文正文
- 仓库保存原始 v6 PDF 和 Overleaf v6 源码归档。
- 2026-11-03 内部清单记录 Introduction、Eq. (27)、Table II、PMNS/Weinberg 算符、Higgs portal、kinetic mixing、有限 vector component、Muon Collider 和 Conclusion 等同步事项。
- 清单中的“待修改”“待决定/修改”“待核对”状态仍应按实际源文件复核。
- **待确认：** 作者当前选定的 Overleaf 工作版本是否与 v6 归档相同。确认前不得将 v6 归档当作活动稿件覆盖式编辑。

## 6. 当前建议的工作顺序

1. 审阅本轮 Major 3 回复与 N-01–N-14 正文修改对照；本轮回复编译和关键页面检查已有验证记录。
2. PR #39 已合并。下一步另行确认作者当前使用的 Overleaf 正文基线，再按已归档清单实施论文修改；不得把未实施的正文修改写成已完成。
3. 优先核对影响主要物理主张的 PMNS、标量约束、portal/mixing 和参数范围；完成后更新清单中的实际正文位置和状态。
4. PR #52（已关闭、未合并但保留研究分支）与 PR #53（Open / Draft）均作为基于原论文单 VEV 模型的独立后续研究；只有在研究本身值得继续时推进，不作为当前回复信的前置条件。未完成工作不得写成已得到的排除结论。
5. 关键 PR 合并、作者改变路线、正文基线更新或专题验收后，更新本文件和相关决策条目。

## 7. 状态可信度约定

- **已核验：** 本次直接检查 main 文件、PR 元数据或可追溯证据。
- **已有记录，需复核：** 历史文档/PR 描述有记录，但本轮未重新执行计算或测试。
- **待确认：** 缺少当前源文件、作者选择或必要证据。
- **未完成：** 当前证据明确表明工作尚未闭环。

本文件是项目管理状态快照，不是物理结果的独立证明。物理结论以模型定义、可复核推导、实际计算和原始实验文献为准。
