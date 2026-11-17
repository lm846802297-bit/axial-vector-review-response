# 第六十五轮文档审查：V57、Higgs portal / UV–EFT 与 Major 3 中微子机制

- 审查日期：2026-11-16
- 审查基线：`8e419aaceb077763c963f9bcf267489fb80adfda`
- PR：[#115](https://github.com/lm846802297-bit/axial-vector-review-response/pull/115)
- 分支：`maintenance/repository-organization-audit-20261114`
- 本轮范围：最新台账中指定的六份 PENDING 文档
- 操作边界：只新增审查报告并更新台账；不修改生产物理计算代码、SN1987A 限制、轴矢量排除曲线或正式回复信正文

## 1. 本轮结果

| 文档 | 本轮状态 | 核心判断 |
|---|---|---|
| `work/v57_reconstructed_1007_final.md` | REVISION_REQUIRED | 相对原始版只修正一处重复文字，先前实质性审查意见仍未关闭 |
| `work/v57_reconstructed_1007_fixed.md` | REVISION_REQUIRED | 与 final 只有一处空格差异，不构成独立物理修订 |
| `审稿意见-gpt/higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(64).md` | HISTORICAL | 保留为累计研究档案；当前研究状态以 Major 1 专题 README 和专门审计记录为准 |
| `审稿意见-gpt/专题研究/2026-11-04-Major3-文献完成机制-候选英文回复.md` | HISTORICAL | 以可选 `sigma+3N_R` 扩展为前提的候选稿，已被根目录正式回复信取代 |
| `审稿意见-gpt/专题研究/2026-11-04-中微子-LmuLtau机制移植核查.md` | PASS_WITH_NOTES | 电荷、Majorana 质量纹理、seesaw 与残余 Z2 分析成立；没有进行全局拟合或完整约束扫描 |
| `审稿意见-gpt/会议记录/2026-10-23/01_文字稿_2026-10-23_20-15.md` | HISTORICAL | 早期 ASR 会议记录，含不确定公式、未采纳猜测及截断内容，只保留历史来源价值 |

本轮六份文档的状态分布：2 份 REVISION_REQUIRED、1 份 PASS_WITH_NOTES、3 份 HISTORICAL。

## 2. V57 final / fixed：逐行对照

### 2.1 文件身份

| 文件 | Git blob SHA | 登记大小 |
|---|---|---:|
| 原始 `v57_reconstructed_1007.md` | `8a0737bbd562a7c6467f336348fb0ea8c7f760bf` | 493,307 B |
| `v57_reconstructed_1007_final.md` | `5736a5f2cadc0486d17d1b0c29ef58e095feb9d3` | 493,303 B |
| `v57_reconstructed_1007_fixed.md` | `98706104fd34ad5de5b8dca4f78d4888d8b668c9` | 493,301 B |

三个文件均为 5,666 行。

### 2.2 差异结论

- final 与 fixed 仅在第 3,862 行存在一处空格差异。
- final 相对原始版也只在第 3,862 行发生变化：将“当前当前存档稿”改为“当前存档稿”。
- fixed 相对原始版同样只修正这一处重复文字。
- 因此，final 与 fixed 不是两轮独立物理修订；fixed 也没有比 final 多修复任何物理问题。

### 2.3 仍未关闭的第六十四轮意见

1. 引言使用 `\Delta_{hs}^{2}`，Work E 使用 `\Delta`；尚未明确给出二者的统一定义或在全文统一记号。
2. 交叉引用仍存在重复：例如同一条目重复列出 `§6.6`，以及重复列出附录 `G.15.6`。
3. 尚未补齐针对 `\Pi_{hs}` 的明确开阈值吸收部分说明：一般性的“虚部”“复极点”或其他物理过程的阈值说明，不能替代对本混合自能在开放轻子阈值上的具体说明。
4. 尚未形成对两个复极点附近动量依赖的明确验收记录。文中虽多次提及动量依赖和复极点，但没有给出所要求的双极点邻域核查结果。
5. 尚无清晰的版本来源清单，不能据文件名或单处空格差异认定 final/fixed 是经过独立物理验收的先后版本。

**处理决定：** 两份文件均保留，不覆盖原始版；两份均标为 REVISION_REQUIRED。不得将文件名中的 final 或 fixed 当作验收结论，也不得据此选择为 V57 唯一 canonical 版本。

## 3. Higgs portal 累计文档：历史档案与当前权威来源分离

### 3.1 文档身份与边界

目标文件 Git blob：

`f42b72c14c7bedbdee470ac4e6d297862c142979`

文件包含 30,723 行，登记大小 1,529,615 B。其前言标注整理版本为 2026-10-18，但后续已累积至第 260.12 节。因此它是跨阶段累计工作文档，不是单一日期的最终回复稿。

文档前部明确规定：统一结论状态表优先于后文历史 guide；未完成的 UV 匹配、有限宽度和近简并结论不得升级为已证明结果。该证据层级应继续保留。

### 3.2 已核对的模型与 portal 结论

第 128–129 节确认：

- 原始模型的 \(S\) 带电荷 \(+2\)，原论文采用单 VEV 关系 \(m_{A'}=2g_Xv_s\)。
- \((H^\dagger H)(S^\dagger S)\) 是规范允许的可重整门户项；\(H\) 对新 \(U(1)\) 中性并不禁止它。
- 原论文使用 negligible-portal benchmark，但没有明确给出 \(\lambda_{HS}\) 的数值、匹配尺度、方案或重整化边界。
- 在某个参考尺度把 portal 设为零是一个重整化/参数条件，不是规范对称性强制的结果。
- 近简并区不能仅凭非零宽度宣称自动安全；必须从完整传播子、极点和实际可观测量判断。

文档保留的早期 guide 文字中有比上述证据更强的历史性表述。应以文首状态表及后续独立核验为准，不应从旧 guide 直接复制“有限宽度已消除问题”“无需微调”或全区间实验结论。

### 3.3 与当前研究工作的关系

文档后部的第 250–260 节包含导数算符、规范 EOM、四费米子和 QLD8 相关材料。它们不能被直接当作 \(hh,hs,ss\) 标量二点函数已完成的证据。当前 Major 1 README 明确把 QLD8 导数算符工作与标量势 \(O_8\) 区分开来。

因此本文件按 HISTORICAL 处理并保留；当前 Major 1 状态以以下专门记录为准：

- [Major 1 当前研究 README](../../research/major1-higgs-scalar-mixing-20261109/README.md)
- [VLL 标量势、tadpole 与 EFT dimension-eight UV audit](../../research/major1-higgs-scalar-mixing-20261109/TADPOLE_VEV_AND_EFT_DIM8_UV_AUDIT_2026-11-09.md)
- [精确动量 pole quadrature tolerance audit](../../research/major1-higgs-scalar-mixing-20261109/POLE_QUADRATURE_TOLERANCE_AUDIT_2026-11-15.md)
- [双极点积分窗口审计](../../research/major1-higgs-scalar-mixing-20261109/SPECTRAL_WINDOW_AUDIT_2026-11-14.md)

本轮没有对累计文档中的每一条历史公式重新进行独立符号推导；本项审查针对其文档角色、证据等级、模型输入章节及与当前权威记录的一致性。

## 4. Higgs–singlet 一圈混合与 UV–EFT 回复的交叉核验

交叉核验对象：

- [当前正式回复信](../../Replies_to_Referee_3_referee_facing_2026-11-04.tex)，blob `d961ce9018ad9b92c0fc8c0d44a1c7301a6afd62`
- [Major 1 当前研究 README](../../research/major1-higgs-scalar-mixing-20261109/README.md)，blob `e118d1f3197d308985e54e02120d7794efffcddd`

### 4.1 三个不同对象不能混为一谈

1. \(\lambda_{HS}\)：四标量门户耦合，是无量纲参数，涉及重整化和匹配边界。
2. \(\Pi_{hs}(p^2)\)：动量相关的非对角二点自能，具有质量平方量纲，包含质量项、波函数项、反项及阈值虚部。
3. 物理混合角、复极点、残数与信号强度：必须从完整传播子及相应产生/衰变振幅确定，不能由单个自能图直接定义。

### 4.2 有限门户阈值与 UV 极点

当前参考条件为

\[
\lambda_{HS}^{\rm EFT}(M_E)=0,
\qquad
\lambda_{HS}^{\rm UV}(M_E)=-\Delta\lambda_{HS}^{E},
\]

其中

\[
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}
\sum_{\ell=\mu,\tau}|y_\ell|^2|\lambda_\ell|^2.
\]

这是选定的匹配 benchmark，不是原论文对 portal 的对称性预测，也不等于 UV portal 本身为零。

当前研究记录还区分了全理论一圈 VLL 行列式中的发散门户极点与有限阈值：前者在所计算的这一圈费米子行列式阶为零，不推出后者也为零。因此有限阈值与零发散极点并不矛盾。

### 4.3 UV–EFT 自能记账

正式回复采用的保留结构是

\[
\Pi_{hs}^{\rm ret}
=
\Pi_{\rm soft}^{\rm bubble+contact}
+\Delta\Pi_{\rm hard}.
\]

其中软区包含轻子 bubble 和维数五算符的 contact tadpole；硬区是全理论与精确 light contribution 的动量差。Plan-C soft 函数中的 contact 已经包含一次，不得重复添加。

已完成的范围包括：

- \(\mu,\tau\) 与 VLL 质量本征态费米子对 \(hh,hs,ss\) 的一圈子计算；
- 对应 VLL 势能、tadpole 和局域 UV 极点的核查；
- leading EFT5 bubble-plus-contact / \(O_8\) UV 结构；
- Plan-C 保留扇区的尺度导数抵消；
- 指定背景场和 MS 方案下的有限重 VLL 标量势匹配。

仍未完成的范围包括完整导数算符基底、全部 gauge/Goldstone/ghost/scalar 贡献、有限 tadpole/VEV 处方、完整同阶 hard-plus-soft 匹配，以及完整规范固定的物理传播子。

### 4.4 数值结果的使用边界

正式回复中 Benchmark B、\(m_s=100\) GeV 的

\[
\eta_{hs}
=
\left|\frac{\Pi_{hs}^{\rm ret}}{a-b}\right|
\simeq1.695\times10^{-5}
\]

是非简并点的质量插入诊断，不是独立计算的物理混合角，也不能外推为近简并区域的统一结论。

2026-11-15 的 pole quadrature audit 显示：三种积分容差设置仍各出现四个 IntegrationWarning。极点质量、宽度和 Higgs 通道残数对该容差变化稳定，但 QUADPACK 没有认证所请求的局部误差；仍需第二种积分方法或解析 \(B_0\) 表示独立核验。因此：

- 当前数值只能作为 first-pass complex-pole diagnostics；
- 不得称为已完成的物理极点/残数预测；
- 不得据此声称近简并区普遍安全、已排除或已有完整实验信号强度；
- 双极点积分窗口审计发现的旧窗口实现差异也必须保留在数值记录中，不能把原历史输出改写成实验结论。

### 4.5 一圈图种类的边界

原模型径向标量 \(s\) 没有直接的 \(sWW\) 或 \(s\bar t t\) 顶点。因此在当前保留阶，不能照搬会议记录中的 W/top 直接一圈 \(hs\) 图猜测。portal 诱导的相应贡献属于更高阶处理。正式回复对这一点作了区分。

**交叉核验结论：** 正式回复在概念上区分了门户阈值、动量相关自能与物理混合信息，并明确给出了条件性 benchmark 和未完成项，与当前 Major 1 研究状态相容。相容的前提是继续保留上述数值边界；不得将 first-pass 极点升级为已验收物理预测。

## 5. Major 3 中微子机制核查

### 5.1 原始最小模型

原模型的左手轻子双重态电荷为

\[
Q_X(L_e,L_\mu,L_\tau)=(0,+1,-1),
\]

原有 \(S\) 的电荷为 \(+2\)。仅 \(S\) 获得 VEV 时保留残余 \(Z_2\)，将电子味与 \(\mu,\tau\) 味分块。

因此一般允许的 PMNS 形式为

\[
U_{\rm PMNS}=\operatorname{diag}(1,U_{23}),
\]

而不是一般地严格等于单位矩阵。它可以容纳 \(\mu-\tau\) 混合，但不能产生观测到的电子味混合。原最小 UV 拉氏量也没有自行给出完整的中微子质量机制。

### 5.2 可选的双单态 type-I seesaw 扩展

候选机制增加

\[
Q_X(\sigma)=+1,\qquad
Q_X(N_{Re},N_{R\mu},N_{R\tau})=(0,+1,-1),
\]

并保留原有 \(Q_X(S)=+2\)。此时 \(\sigma\) 产生 \(e\mu,e\tau\) Majorana 项，\(S\) 产生 \(\mu\mu,\tau\tau\) 项，裸项允许 \(ee,\mu\tau\) 项。

一般的对称 \(M_R\) 与

\[
M_\nu\simeq-m_D M_R^{-1}m_D^T
\]

允许非平凡三味混合。对非奇异目标矩阵可使用

\[
M_R=-m_D^T M_\nu^{-1}m_D
\]

作纹理层面的反构造。这证明了质量矩阵结构的存在性，但不是数值拟合或扩展模型全局允许性证明。

新增 VEV 还会改变规范玻色子质量：

\[
m_{A'}^2=g_X^2(4v_s^2+v_\sigma^2),
\]

并允许新的标量势项及可能的带电轻子–VLL 相互作用。因此该方案只能作为独立的可选中微子扇区扩展，不能将其全部物理效应隐去后仍称为原始单 VEV 模型。

### 5.3 候选回复与正式回复

候选英文回复文件明确以采用 \(\sigma+3N_R\) 扩展为前提，不能用来证明原最小模型已经产生现实 PMNS 矩阵。

根目录正式回复信已经：

- 单独说明原始 \(S\)-only 模型的残余 \(Z_2\)；
- 给出 \(U_{\rm PMNS}=\operatorname{diag}(1,U_{23})\)；
- 将 \(\sigma+3N_R\) 明确标为可选扩展；
- 给出 \(m_D,M_R\)、seesaw 关系、Takagi 对角化及 PMNS 定义；
- 检查新增中微子场的线性与立方异常；
- 给出双 VEV 的规范玻色子质量关系和新增标量势；
- 声明扩展模型没有完成数值拟合或全局约束扫描。

**结论：** 中微子机制移植核查为 PASS_WITH_NOTES；候选英文回复与会议记录转为 HISTORICAL，正式回复信是当前使用版本。

## 6. 会议记录的历史边界

2026-10-23 会议文字稿是带有 ASR 校订和截断的记录，不是逐字可靠的场论推导。它保留了早期讨论中的：

- W/top 直接圈图猜测；
- 树级 portal 与一圈项相互抵消的临时建议；
- 对 \(m_s,v_s,g_X\) 理论范围的未核实口头判断；
- 尚未核对的公式和不确定术语。

这些内容不得作为已采纳的模型设定或计算结论。当前正式回复和 Major 1 研究记录已经明确区分实际允许的顶点、匹配边界和计算阶数。会议稿保留为历史来源，不进行物理结论引用。

## 7. 台账更新

第六十四轮基线：

| 状态 | 数量 |
|---|---:|
| PASS_WITH_NOTES | 255 |
| PASS | 2 |
| REVISION_REQUIRED | 22 |
| HISTORICAL | 105 |
| PENDING | 78 |
| 已审查 | 384 / 462 |

第六十五轮更新后：

| 状态 | 数量 |
|---|---:|
| PASS_WITH_NOTES | 256 |
| PASS | 2 |
| REVISION_REQUIRED | 24 |
| HISTORICAL | 108 |
| PENDING | 72 |
| 已审查 | 390 / 462 |

完成比例：

\[
\frac{390}{462}=84.4\%.
\]

本轮没有修改六份原始研究文档，没有更改正式回复信、生产计算代码、SN1987A 限制或轴矢量排除曲线。只提交本审查报告与台账状态更新。

## 8. 后续工作建议

1. V57：先修复 \(\Delta\) 记号、交叉引用、吸收部分/双极点动量依赖说明及版本来源，再决定是否保留唯一 canonical 版本。
2. Higgs portal：以 Major 1 README 和专门 UV/tadpole/pole audit 为唯一当前状态入口；先关闭 pole 积分独立验证，再讨论近简并物理结论。
3. Major 3：继续以根目录正式回复为准；若未来决定将可选扩展写入论文正文，必须同步处理双 VEV、标量谱、规范玻色子质量和带电轻子–VLL 新耦合。
4. 会议稿及候选英文稿只保留历史用途，不回填为当前物理结论。
