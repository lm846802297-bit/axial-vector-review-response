# 第六十八轮文档审查：PMNS 范围、Higgs portal 数值记录与标量约束来源

- 审查日期：2026-11-16
- 审查基线：2484eb774d7c5a298007266b8a3ed5119dce1e52
- PR：[#115](https://github.com/lm846802297-bit/axial-vector-review-response/pull/115)
- 分支：maintenance/repository-organization-audit-20261114
- 状态源：PROJECT_STATUS.md 与「研究决策与不可回退事项」
- 范围：最新台账前六份 PENDING 文件
- 本轮仅新增审查报告、更新六条台账记录；不修改原始科研输出、论文正文、正式回复信或计算脚本。

## 1. 结论摘要

| 文档 | Git blob SHA | 结果 | 主要理由 |
|---|---|---|---|
| axial_vectorv6-diff-v2.4-PMNS-scope-2026-10-27.md | b0afe9d78ff424590c09e04d1d26e4f3b879ecb8 | HISTORICAL | 2026-10-27 工作包/回复口径快照；Route-B-only PMNS 文字早于 2026-11-05 response-only 可选 seesaw 决策。 |
| higgs_portal_exact_mass_eigenstate_one_loop_validation.txt | 92b5f4f0c360fdbfbf295d4b7fe09c6fd07d94a1 | PASS_WITH_NOTES | 对应脚本 blob 与当前分支一致，清洁运行和断言记录可追溯；仅限两个 benchmark 的一圈费米子自能。 |
| higgs_portal_planC_lite_clean_run_2026-10-27.txt | a9f014e7575435da22ca4e9ad61ff0f3c5d5c1ce | HISTORICAL | 只验证旧脚本 blob，不能证明后来 fine-scan/P2-lite 修改后的当前脚本已清洁运行。 |
| higgs_portal_planC_lite_validation.txt | c41ff8343245e5751f87698c569de340b29e35d8 | PASS_WITH_NOTES | 明确区分旧脚本 clean run、后续 in-session 复算、P2-lite 子集和未完成的完整匹配/极点计算。 |
| routeB_manuscript_revision_status_2026-10-27.md | 4e0ab618eb967c3be7e93876af1450076c9c77a0 | HISTORICAL | 是独立 Route B 修订副本的 35 页编译快照，不等于当前正式回复/主论文提交包。 |
| scalar_coupling_constraints_source_note_2026-10-28.md | d6d3e3a753a74edc704141effe4a8aebcaf0a20c | REVISION_REQUIRED | 多个表格行的 inline-math delimiter 使用双反斜杠，Markdown 数学渲染失效；需修复并检查配套 SVG 呈现。 |

本轮六份：2 PASS_WITH_NOTES、3 HISTORICAL、1 REVISION_REQUIRED。

## 2. PMNS：Diff v2.4 与当前回复/决策文件

Diff v2.4 明确是 2026-10-27 的内部研究计划。它说明原始 v6 与 PDF 不变，Route B 修订副本完成独立编译；T-01 的正文范围限定已同步，但 PMNS 本身仍未解决。其 Route B 适用于当时论文正文范围：保留原单 VEV S+VLL 模型，不向原论文增加新的中微子场；原模型的电子味与 (mu,tau) 扇区分块，不能产生观测所需的电子味混合。

当前动态决策登记表 DEC-01/DEC-01A（2026-11-05）进一步区分：
1. 原论文 UV 模型仍是单 VEV S+VLL，非中微子现象学仍使用 m_A'=2 g_X v_s。
2. Major 3/4.1 的专门回复可以讨论可选 sigma+3N_R 双单态 type-I seesaw 作为中微子质量完成机制。
3. 该扩展只属于中微子回复论证，不等于原论文已加入这些场，也不得把扩展的双 VEV 质量关系移用于 Major 1、2、4.2–4.4。

当前正式回复信确实把原始 S-only 结构的残余 Z2 限制，与独立的可选 seesaw 回复段分开；同时明确扩展没有改变原始 one-VEV benchmark 的非中微子现象学。它还说明扩展的矩阵构造是解析 texture-level construction，不是数值拟合或全局参数扫描。

因此，Diff v2.4 不是物理推导错误，而是早于 DEC-01A 的历史版本。其 Route-B manuscript build 仍可作为正文副本的可复现记录，但不能再作为当前 Major 3/4.1 回复全文口径的唯一来源。

**当前准确表述：** 原始最小模型不能产生观测所需的电子味混合；当前回复另讨论一个仅用于 Major 3/4.1 的可选扩展。不要把两者写成同一个模型，也不要声称原论文的最小模型已经解释 PMNS。

## 3. Exact mass-eigenstate one-loop validation

验证记录所指脚本 higgs_portal_exact_mass_eigenstate_one_loop.py：
- 记录中的 Git blob SHA：a2128e5ed9fe0065fc01e61972fdbfbe3f4859fb。
- 本轮从维护分支重新读取脚本得到相同 blob SHA。
- 因此该 validation record 对应的确切脚本字节与当前分支一致。

记录包含完整 charged-lepton/VLL mass-eigenstate 求和，覆盖 heavy-heavy、heavy-light、light-heavy 和 light-light 内部态。内部检查包括：
- 完整质量本征态求和后 p^2 UV 系数数值抵消；
- 剩余 local UV 系数在记录精度下与零一致；
- absorptive part 与 light-light cut 一致；
- hard momentum difference 与领先有限导数匹配结果相差约 6.11e-4；
- 零动量 hard comparator 与 leading-seesaw portal threshold 的相对残差约 1.79e-4。

两个 benchmark 的记录值为：
- A：Delta lambda_HS^E ≈ -0.210763976，Pi_hs^matched(m_h^2) ≈ (-0.413278 - 0.113174 i) GeV^2。
- B：Delta lambda_HS^E ≈ -0.0106733765，Pi_hs^matched(m_h^2) ≈ (-0.093003 - 0.025468 i) GeV^2。

这些数值依赖 M_E=20 TeV、指定 mixing angles、leading-seesaw Yukawa relation、RC/Plan-B 符号约定，以及 lambda_HS^EFT(M_E)=0 的匹配边界。该 EFT portal 条件需要非零 UV portal 抵消有限 VLL 阈值；它不是对称性预测，也不能与 lambda_HS^UV=0 混同。

该文件没有完成完整 pole-scheme、全部 diagonal self-energy/counterterm/tadpole/VEV 与物理输入重整化、完整 gauge/Goldstone/ghost 集合或模型专属 Higgs lineshape/直接搜索重铸。故判为 PASS_WITH_NOTES：脚本身份和所述数值检查通过，但证据只支持 benchmark-level one-loop fermion self-energy，不支持全参数空间混合结论。

## 4. Plan-C-lite 两份记录：clean-run 与后续更新必须分开

### 4.1 2026-10-27 clean-run

clean-run 记录验证的旧脚本 blob 为：
1ebfb28edce1d829e6d883dbe5c3ab36bc981d06。

本轮当前分支中的 Plan-C-lite 脚本 blob 已为：
df139e099853246501d2fbf9957dbba890014d14。

因此，旧 clean-run 的 exit code 0 只能证明旧版本脚本运行，不能为后来添加的 2026-11-05 fine scan、P2-lite 标量泡图和闭式函数代码背书。原始 stdout 保留为历史 provenance，状态标为 HISTORICAL。

### 4.2 后续 validation 文件

后续 validation 文件明确区分：
- 2026-10-27 clean execution 对应旧脚本 blob；
- 独立 equation-level reproduction 是同一组方程/benchmark 的另一数值实现；
- 2026-11-05 的 1001 点、0.1 MeV fine scan 是 in-session 独立复现，不是更新后完整仓库脚本的 clean-container run；
- 新增脚本函数只做过 AST/syntax 检查，未声称整文件重新执行；
- P2-lite CP-even scalar-bubble subset 的闭式函数与 8,000 区间 Simpson 积分在 12 个 benchmark/质量/拓扑组合上的最大相对差约 9.97e-15；
- 该 CP-even subset 不含完整同阶 mixed VLL-scalar matching、Goldstone/gauge/ghost 与 tadpole/VEV 反项，不能直接当成物理两圈自能或加入 fermion result。

故 validation 文件判为 PASS_WITH_NOTES：证据分层清楚，内部闭式函数交叉检查有价值，但更新后完整脚本 clean run、完整 UV-EFT 同阶闭合和 gauge-independent pole calculation 仍开放。

### 4.3 与 2026-11-15 quadrature warning 的关系

POLE_QUADRATURE_TOLERANCE_AUDIT_2026-11-15.md 检查的是另一个 driver：exact_momentum_fermion_pole_audit.py。其三档 QUADPACK 容差运行均出现四个 IntegrationWarning；pole mass/width/residue 对容差变化稳定，但仍要求独立积分方法或解析 B0 表示。

该警告应继续用于其对应的 exact-momentum pole note 和 cascade note；**不能在没有源码/算法对应关系证明时，把它自动转嫁成 Plan-C-lite 的数值失败。** 两套记录必须保留各自输入 SHA、积分器和证据边界。

## 5. Route-B manuscript build status

该文件记录的是 2026-10-27 用户提供 Source ZIP 后创建的独立修订副本：
- 输入 ZIP、原始 main-v6.tex、修订 main.tex 和 PDF 均有 SHA-256；
- 修订版 35 页，clean build exit code 0；
- 无 undefined refs/citations、duplicate labels 或新 warning signature；
- 原始 baseline 33 页，单独编译通过；
- Route B 仅同步到该副本的 Abstract、Introduction、模型段和 Conclusion；
- 原始 S-only 场内容仍不能产生观测 PMNS，原始稿件没有新增右手中微子或新标量；
- Fig. 2 仍是 conditional pure-axial EFT benchmark，不是全局 UV viability classification。

这些事实作为 2026-10-27 build provenance 有效，但不是当前 main 正式回复信或作者活动 Overleaf 稿件的编译验收。特别要避免把“论文副本未增加场”误读成“当前 Major 3/4.1 回复没有可选 seesaw 讨论”：当前回复信已经把 response-only extension 与原论文模型明确分开。

## 6. Scalar–muon Yukawa constraint source note

### 6.1 物理范围与来源交叉核对

该文件把约束统一写成 y_sμμ 对 m_s，而不是直接画成 A' 纯轴矢量排除。它区分 binary-pulsar periastron advance、neutron-star cooling、SN 1987A free-streaming cooling threshold、diffuse SN gamma-ray plateau，以及 fifth-force proton coupling 的 loop-induced UV translation。

本轮外部来源核对：
- Liu & Tang, arXiv:2501.10927 / PRD 112, 055021：binary-pulsar periastron advance 的主要质量窗口约 1e-17–2e-15 eV，灵敏度可达 O(1e-21)。来源：https://arxiv.org/abs/2501.10927
- Fiorillo et al., arXiv:2605.24094v2：其 Table 1 对 m_X≲1 keV 给出 scalar NS-cooling 7.4e-14、scalar SN 1987A cooling 4.2e-9。来源：https://arxiv.org/abs/2605.24094
- Caputo, Raffelt & Vitagliano, arXiv:2109.03244 / PRD 105, 035022：diffuse SN gamma-ray plateau g_phi≈0.4e-10，即约 4e-11，适用于 m_phi≳100 keV 的文中讨论区域。来源：https://arxiv.org/abs/2109.03244

这些数据的粒子过程、质量窗口和天体环境不同，不构成一个可随意拼接的全局 exclusion envelope。该 note 对此已有恰当限制。

### 6.2 UV 映射

该 note 使用 |y_sμμ|=2|g_X|m_mu/m_A' 把 source-level scalar-muon Yukawa bound 映射为给定单 VEV、mass-proportional scalar benchmark 下的条件性 g_X 上限。这不是直接实验对 A' 轴矢量流的限制，也不能自动转移到 m_s≳10 GeV 的 Fig. 2 参考 benchmark。

这与当前 DEC-03/DEC-14 一致：低质量标量来源限制单独讨论；m_s≳10 GeV 只是 Fig. 2 的 scalar reference benchmark，不是全局允许质量区间。

### 6.3 必须修复的 Markdown 数学格式

表格中 neutron-star cooling 和 SN 1987A cooling 两行的数学内容存在双反斜杠 delimiter，例如：
\\\\(|y_{s\\\\mu\\\\mu}|\\\\simeq7.4\\\\times10^{-14}\\\\)。

Markdown inline math 应使用单层 delimiter：
\\(|y_{s\\mu\\mu}|\\simeq7.4\\times10^{-14}\\)。

当前形式会使反斜杠被解释为普通字符/换行，而不是正确的数学起止标记，导致表格内数学排版不稳定。应逐行检查同类的双反斜杠 math delimiters 和命令转义，修复后重新渲染 Markdown，并检查 SVG 图中标签、质量区间、横向段线和图例是否与表格一致。

SVG 文件及相对路径已核实存在，但本轮没有进行浏览器级 SVG 视觉验收；不能宣称图形排版已通过。

## 7. 台账更新

第六十七轮后：
- PASS_WITH_NOTES：258
- PASS：2
- REVISION_REQUIRED：24
- HISTORICAL：118
- PENDING：60
- 已审查：402 / 462

第六十八轮后：
- PASS_WITH_NOTES：260
- PASS：2
- REVISION_REQUIRED：25
- HISTORICAL：121
- PENDING：54
- 已审查：408 / 462（88.3%）

本轮仅新增本报告，并更新六条台账；没有修改被审文档、正式回复信、论文源码或生产计算。

## 8. 下一轮

继续按台账顺序审查下一批六份 PENDING 文档。优先检查 scalar-source note 的相邻图表/来源文件，以及 2026-11-09 至 2026-11-15 新生成的 Major 1 pole、residue、Higgs-rate 和 gauge-completion 研究记录。

近极点数值需要分别验收：
- tolerance stability；
- integrator error certification；
- independent-method reproduction；
- complete gauge-independent pole prediction；
- detector-level Higgs lineshape recast。

这些是不同门槛，不得用“结果对容差稳定”替代“积分误差已认证”。


## 9. Post-review source and formatting verification (2026-11-16)

The three cited source values were checked against the current arXiv records:

- Liu & Tang, arXiv:2501.10927v2, reports the strongest periastron-advance sensitivity over approximately $10^{-17}$–$2\times10^{-15}$ eV and probes muonic couplings at $\mathcal O(10^{-21})$. The source note correctly labels $4\times10^{-16}$ eV as its best-sensitivity point, not a flat limit.
- Fiorillo et al., arXiv:2605.24094v2, Table 1 explicitly lists scalar NS-cooling $7.4\times10^{-14}$ and scalar SN 1987A cooling $4.2\times10^{-9}$ for $m_X\lesssim1$ keV. The abstract gives rounded order-of-magnitude summaries; the note correctly cites the exact table entries.
- Caputo, Raffelt & Vitagliano, arXiv:2109.03244v3, gives the diffuse-SN-gamma scalar plateau $g_\phi\lesssim0.4\times10^{-10}=4\times10^{-11}$ for $m_\phi\gtrsim100$ keV.

The Markdown math delimiter issue in `scalar_coupling_constraints_source_note_2026-10-28.md` has now been repaired: the neutron-star and SN 1987A table rows use single-backslash inline-math commands and delimiters. Current file blob SHA is `c44d5932521e474edf3f18a58ffc6cc62062a67b`. The companion SVG exists (blob `189b2873edf5b058f5c051905b4c3e9564f1dd6b`) and its embedded text labels agree with the source-note table. This was an XML/text-label inspection, not a browser-level visual rendering check; retain that as a non-blocking note.

The scalar source note is therefore now `PASS_WITH_NOTES`, with visual SVG rendering still to be checked. It remains a scalar-Yukawa source summary and conditional UV translation, not a direct pure-axial $A'$ constraint. The historical PMNS, Plan-C-lite and Route-B build dispositions in §§2–5 remain unchanged.
