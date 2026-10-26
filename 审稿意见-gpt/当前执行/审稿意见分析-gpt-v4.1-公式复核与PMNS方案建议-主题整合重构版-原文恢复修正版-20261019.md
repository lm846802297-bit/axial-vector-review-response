# DW13678 审稿意见分析、物理核查与逐条修订方案

> **v4.1 主文档｜主题整合重构·前置原文恢复修正版｜2026-10-19。** 这是对原“v4.1 统一更新版”的**结构性重编**，不是在末尾再加第十七章。原 v4.1 的第十三至十六章原先用于追加公式复核、物理状态与 38 项索引；现已将实质内容分配到对应的第 2–6 章，各章开头保留审稿人英文原文摘录，附录 A 另保留完整原文，公式/版本证据保留在附录 B，完整 38 项核对索引保留在附录 C。**审稿意见的解释看相应主题章，任务执行看 v5.4 手册，原文与版本冲突看附录。**
>
> **事实基线：** `dw13678_report_1_a.pdf`（原始审稿意见）、`axial_vector_model_building-v6.pdf`（当前存档的最终投稿稿）。不得将其他分析文件中的方案或模板冒充物理验证。审稿人实际收到的版本未获投稿系统确认；但按 2026-10-26 项目决策，不再追查该 PDF 版本作为阻塞项。报告-v6 的边界表达差异作为来源/表达差异记录，后续以当前 v6 内部一致的定义和归一化为基准。
>
> **物理状态简要提醒：** v6 Eq. (30)/(34) 彼此一致；最小场内容的 PMNS 残余分块是结构性障碍；带奇荷标量/右手中微子只是待验证的扩展；Higgs portal、近简并区、动能混合、标量允许窗口、$A'$ 恒星限制仍待独立核查。任何下文“应计算/建议增加”都是**未完成任务**，不能变成 rebuttal 中的完成时陈述。

## 一、审稿意见总体总结

### 1.1 核心问题

以下四类问题是整理者对原始报告的归纳，并非审稿人逐字原话。对应英文原文按原始编号先在相关主题章摘录，再由附录 A 完整归档（来源：资料库文件 `dw13678_report_1_a.pdf`）。当前需要重点处理四类主要问题：

1. **标量扇区的现象学分析不够完整。** 需要进一步讨论额外标量的质量范围、与标准模型 Higgs 的混合、Higgs portal 相互作用、可能的环图诱导混合，以及标量质量接近 Higgs 质量时的特殊情况。
2. **EFT 参数范围及 UV–EFT 一致性需要更充分的解释。** 需要说明扫描范围的物理依据、EFT 的适用条件，以及低能有效理论参数与紫外模型参数之间的对应关系。
3. **中微子振荡与 PMNS 混合矩阵的兼容性需要明确论证。** 需要根据模型的场内容、荷分配和中微子质量矩阵，判断模型能否产生观测到的中微子质量谱和混合角。
4. **部分实验和天体物理约束可能不够完整。** 需要检查中微子振荡、动能混合、有限质量矢量样轻子（VLL）引起的残余矢量耦合，以及恒星冷却等约束。

此外，还需要修正若干表述不清楚的问题，包括质量扫描范围、纯轴矢量极限的定义、VLL 质量与混合角限制、保守基准点的含义，以及未来 μ 子对撞机部分的分析深度。

### 1.2 修改优先级

| 优先级 | 工作内容 | 原因 |
|---|---|---|
| P0 | 中微子质量矩阵与 PMNS 兼容性 | 关系到模型本身是否具有理论自洽性 |
| P0 | UV–EFT 匹配与参数范围 | 关系到参数扫描结果能否被正确解释 |
| P1 | 标量扇区与 Higgs 混合 | 可能改变允许参数空间和主要结论 |
| P1 | 动能混合、有限 VLL 质量修正及额外约束 | 影响模型的完整现象学分析 |
| P2 | 图表、术语和公式附近的解释 | 提高论文可读性与论证严谨性 |
| P2 | μ 子对撞机部分的取舍 | 确保预测的深度与证据相匹配 |

**建议顺序：先做版本和 PMNS 理论决策（P0），同时启动可复现的标量窗口与基础参数表（P0）；再联合完成 portal、动能混合、VLL 和实验筛查（P1），最后统一正文、图表和回复信（提交前 P0）。P0 中“做决定”并不等于“解决模型”。**

---

### 1.3 本文如何使用：一个主题只在一个位置裁定物理状态

| 内容类型 | 现行权威位置 | 说明 |
|---|---|---|
| 标量不可退耦、质量范围、portal、Higgs 约束 | **第 2 章** | §2.1 解释三项要求，§2.2 处理机制，§2.6–2.7 处理质量区间、实验与验收 |
| EFT 与 UV 同点实现 | **第 3 章** | 扫描域、参数表、图的颜色/图注以及扩展场对原图的影响 |
| 中微子与 PMNS | **第 4 章** | 最小场内容结构性分块、候选扩展与必须做出的作者决策 |
| 动能混合、有限矢量耦合、恒星与开放性约束 | **第 5 章** | 对象、 benchmark、适用性、复核与额外的条件性筛查 |
| Minor Points：VLL、benchmark、对撞机与术语 | **第 6 章** | 与第 2–5 章交叉引用，不以“已提过”代替原编号答复 |
| 审稿人原文、推导与出处 | **第 2–6 章前置引文；附录 A/B** | 各主题的审稿人引文放在相应分析之前；附录 A 备查完整原文，附录 B 记录 Eq. (30)/(34) 与引用编号核对事实 |
| 38 项逐条勾稽 | **附录 C** | 索引，**不是另一套物理解释或新章节的重复分析** |
| 分工、交付与验收 | **v5.4 执行手册** | 只有证据归档、独立复核和最终修稿落点齐全才标已完成 |

**统一证据等级：**“已核对的 v6 稿件事实”、“有前提的结构性推导”、“条件性数值”、“候选扩展／待拟合”、“待文献查验／待独立复核”、“未解决”、“过时历史结论”。**38/38 表示要求可追溯，不表示 38/38 科研结果完成。** 审稿原文与 v6 若不同，标记为待确认版本差异，不以某份分析文件出现较晚就替代证据。

**记号约定：** 在旧报告、中文讨论中经常笼统称“标量 $S$”，但 $S$ 是破缺前的复标量场，其破缺后的径向物理态在 v6 中记作 $s$（质量 $m_s$）。本文保留用户熟悉的“$S$ 的现象学／$m_S$ 窗口”的统称；讨论 $s\to A\prime A\prime$、$h\to ss$ 或粒子寿命时，指实际径向质量本征态。若有 Higgs 混合，必须再改用物理质量本征态定义，不能把复场 $S$、径向态 $s$ 与混合态当作三种独立粒子。

### 1.4 原始编号、内部语义单元与 G 标签的关系

原始报告保留 Major 1–4、Minor 1–6（含 Minor 6 的六个子项）、Recommendation；内部拆为 38 个可追踪单元：`A` 5 项开篇/优点评价、`B` 7 项标量、`C` 3 项参数、`D` 4 项 PMNS、`E` 5 项约束、`F` 13 项 Minor、`H` 1 项 Recommendation。**G-1/G-2/G-3 并非审稿人原始编号**，只是旧表的未定义工作包标签：G-1 → B-3/E-1（连带 B-1/B-2/B-7/F-10），G-2 → B-4/B-5/B-6，G-3 → D-2/D-3/D-4（连带 E-2）。今后正文按真实主题展开，附录 C 和独立对照表仍使用上述 A/B/C/D/E/F/H 单元追踪。

## 二、主要意见一：补充标量扇区的现象学分析

### 2.1 审稿意见究竟要求什么：不可任意退耦的标量及论文定位

**审稿人原文（Major Point 1，节选；完整原文见附录 A.1）：**

> “Phenomenology of the $S$ scalar. The second half of the paper reviews a set of experimental bounds on only an effective theory of the $A'$ axially coupled to the $L_{\mu-\tau}$ current. This leaves a major gap between these two parts of the paper: the authors show that their UV theory requires a scalar $S$ that cannot be arbitrarily decoupled from the low-energy dynamics, e.g. from (34) which states that $m_S^2 < 4\pi(m_{A'}/2g_X)^2$.”

**审稿人原文（Major Point 1.1–1.3，关键句节选）：**

> “It is thus an odd choice to exclude the scalar from the phenomenology of the effective theory: if the $S$ is unavoidable at phenomenologically relevant scales, shouldn't one of the main points of the paper be that the only known UV completion of an axial $L_{\mu-\tau}$ gauge boson has a prediction for a scalar particle in a mass range that can be probed by colliders?”
>
> “What is the range of phenomenologically allowed $S$ mass including perturbativity limits on $\lambda$ and a motivated range of $m_{A'}$ and $g_X$.”
>
> “Above (34): the authors ‘assume negligible Higgs-portal mixing.’ Is this interaction not generated at loop level?”

以上引文反映的是审稿人的疑问与判断，不应直接当作已经验证的物理结论。


**原始意见及内部编号：Major 1 总述、1.1、1.2、1.3（追踪单元 B-1–B-7）；另关联 Minor 5、Minor 6.3。** 上面已原样恢复旧版 §2.1 的前置英文引文，附录 A.1 另保留完整原文与段落上下文。审稿人并非只要求增加一句“考虑了标量”，而是指出 UV 模型必有破缺标量 $S$，但后半论文主要讨论仅含轴矢量 $A'$ 的二维 EFT：**模型构造与唯象学之间存在可检验性缺口**。

#### 2.1.1 为什么 $S$ 无法仅靠调重而任意退耦（B-1）

对当前 v6 **最小场内容**（$Q_S=2$）和其 VEV 归一化，有

\[
 m_{A'}=2g_Xv_S,\qquad m_S^2=2\lambda_Sv_S^2,\qquad
 \frac{m_S}{m_{A'}}=\frac{\sqrt{2\lambda_S}}{2g_X}.
\]

对一般新荷 `q_S`，用约定 `m_{A'}=g_X|q_S|v_S`，比值为 `sqrt(2 λ_S)/(g_X |q_S|)`；这里只在**归一化一致**时可使用。给定 $m_{A'}$、`g_X>0`、有限的 `λ_S^max`，由

\[
  m_S\leq \sqrt{2\lambda_S^{\max}}\,\frac{m_{A'}}{2g_X}
\]

得到的是**该切片上的理论上界**，不是单凭微扰性就得到完整的“实验允许上下界”；不能说所有 $m_S$ 都已被 collider 覆盖。若采用额外破缺 VEV（如 PMNS 扩展中的奇荷标量），必须先重推 $m_{A'}$ 与 VEV 的关系，不能机械套用式 (34)。

**公式核对：** v6 Eq. (30) 的根号为 `sqrt(λ_S^max/2)`，与 Eq. (34) 及 Fig. 2 的 $v_S=2\,\mathrm{GeV}$ 示例一致；报告引用的 $m_S^2<4\pi v_S^2$ 与 v6 在 $\lambda_S^{\max}=4\pi$ 时的 $m_S^2<8\pi v_S^2$ 不是同一边界，差异按项目决策作为报告-v6 表达差异登记（详见附录 B.1），不再追查实际送审 PDF；不应把该差异解释为 v6 内部计算错误。

#### 2.1.2 第一项要求：考虑将 $S$ 纳入论文核心物理主张（B-2）

合并版增补 A1 的合理内容是**论文定位建议**：若 $S$ 在可实现参数范围内产生了有判别力的实验信号，正文应把它从“仅用于自发破缺的附属自由度”提升为 UV 模型的现象学预言之一，并将标量检验与仅有 $A'$ 的 EFT 搜索对照。

然而，审稿人的提议不是作者可照抄的现成结论。尤其不能把“only known UV completion”“一定可被对撞机探测”“$S$ 已被排除”写成作者已证明的事实。应先完成 §2.6–§2.7 的可实现质量窗口、衰变、Higgs portal、直接搜索、LLP/稀有衰变与现有数据比较，再按结果决定摘要、结论和新增标量现象学节的篇幅。审稿人对 $S$ 不可形式退耦的怀疑，**要求定量辩护**，但不等于某个质量区间已经排除。

#### 2.1.3 第二项要求：给出含微扰性和实验约束的 $m_S$ 允许窗口（B-3）

必须**同时**规定 $m_{A'}$ 与 $g_X$ 的选择依据、$v_S=m_{A\prime}/(2g_X)$ 的映射、$\lambda_S$ 的扰动判据、标量势稳定性、有关 Yukawa 与重 VLL 质量/混合的实现条件，并核对适用的 $A'$ 和 $S$ 实验限制。质量范围应分成“理论可实现”“在已检查实验下仍允许”“实验排除”“EFT 近似不适用”“未评估”几种；不得把一个已画出的 $m_S$ 微扰性上界当作实验允许窗口。具体计算步骤、表格模板和结果验收见 §2.6–§2.7，并与 §3 的 UV–EFT 联合参数扫描相互引用。

#### 2.1.4 第三项要求：不能未经量化就令 Higgs portal 可忽略（B-4–B-7）

报告询问树级 portal 设置、`μ/τ` 圈级产生、$m_S\simeq m_h$ 附近的增强、Higgs 测量能否对 UV 完备模型给出主导限制，以及**如果忽略这些约束，理由是什么**。在此模型中 `|H|²|S|²` **本身是规范允许的可重整项**；设 `λ_HS=0` 是边界/参数假设而非由新规范对称性自动禁止。重 VLL 同时关联 `H` 和 $S$，圈图来源不能只按轻 `μ/τ` 粗略估算。§2.2 明确计算对象，§2.6 规定按质量区间的实验映射。比较完数据前，不能声称“portal 无关”或“Higgs 数据一定最强”。

### 2.2 需要补充的理论工作

#### 工作 A：整理完整的标量势

首先写出模型允许的标量势，例如一般形式可以包含

\[
V(H,S)=
-\mu_H^2 H^\dagger H
+\lambda_H(H^\dagger H)^2
+\mu_S^2 S^\dagger S
+\lambda_S(S^\dagger S)^2
+\lambda_{HS}(H^\dagger H)(S^\dagger S),
\]

其中 \(H\) 是标准模型 Higgs 双重态，\(S\) 是额外标量场。

以上仅是示意形式。实际写入论文时，必须根据模型的规范荷、离散对称性及拉格朗日量确定哪些项确实允许，不能直接假设所有项都存在。

**对当前模型的直接判断：** 由 Table I 的荷分配可知，$H$ 在新 $U(1)$ 下中性，而复标量 $S$ 带荷。因此 $(H^\dagger H)|S|^2$ 是规范不变且可重整的 Higgs-portal 项；它不是“可能存在、也可能被对称性禁止”的一般性问题。当前文稿只写出 $V(S)$ 的自相互作用时，应说明这是忽略或设定 portal 耦合的边界条件，而不是完整标量势。由于重 VLL 同时耦合 $H$ 和 $S$，还须检查其阈值修正与重整化群演化是否会再生该耦合。不能只笼统归因于轻 $\mu/\tau$ 环。

具体任务：

1. 列出所有允许的标量势项。
2. 明确每个参数的定义和量纲。
3. 说明哪些参数由对称性限制。
4. 推导真空期望值和质量矩阵。
5. 检查标量势的稳定性和真空结构。

#### 工作 B：推导标量质量本征态

如果模型允许 Higgs 与新标量混合，应写出质量矩阵：

\[
\mathcal M^2=
\begin{pmatrix}
m_{hh}^2 & m_{hs}^2\\
m_{hs}^2 & m_{ss}^2
\end{pmatrix}.
\]

通过对角化得到物理质量本征态及混合角。

需要说明：

- 混合角由哪些模型参数决定；
- 采用了什么近似；
- 混合角是否受到实验限制；
- 是否存在质量简并或近简并区域；
- 近简并区域是否需要重新处理混合和衰变。

如果模型的对称性禁止树图混合，也应明确说明，并进一步判断环图是否可能诱导相关效应。

对本文而言，portal 在树图层面已经允许；需要量化的是其取值及其辐射稳定性，而不是仅判断其“是否允许”。当 (m_S\simeq m_h) 时，应从完整的重整化质量矩阵（必要时含自能与宽度）处理近简并混合，避免把远离简并时的微扰混合角公式直接外推。这里宜称为“近简并导致的混合增强”，不宜未经计算称为新的物理共振。

#### 工作 C：检查 Higgs portal 和实验限制

根据模型实际情况，评估以下约束：

- 标准模型 Higgs 的信号强度；
- Higgs 的额外衰变道；
- 轻标量的直接搜索；
- 新标量对可见衰变或不可见衰变的贡献；
- 与模型相关的低能实验和天体物理限制。

每项约束都应注明其适用的质量范围、耦合假设和参数依赖。

#### 工作 D：Higgs portal 与近简并区的同一 UV–EFT 计算口径（B-4/B-5/B-6）

将合并版中原先分散的 A2、现有 v4.1 的单圈提示合并到本节，统一按照以下次序计算。

1. **模型与边界：** 在同一套 `H,S,VLL,μ,τ` 规范荷、质量本征态与归一化下写出全 UV 拉氏量。明确树级 `λ_HS(μ_0)` 是自由输入、被设为零的重整化条件，还是另有可证明的限制；写出所用反项、匹配尺度和 RGE 方案。
2. **匹配而非拼接：** 将重 VLL 阈值、轻轻子 EFT 自能、相应 EFT 接触项与反项按同阶重整化/匹配。现存资料中 `δm^2_hs∝M^2` 的候选阈值结果与一个示例低能自能 `|δΠ_hs|≈0.168 GeV²`（`v_S=50 GeV`，固定外动量的条件性计算）**定义不一且未统一复核**；不能相加、二选一或当作自然性/混合角的最终结论。
3. **常规二态对角化：** 在势含 `λ_HS|H|²|S|²` 且 `H=(0,(v+h)/√2)^T`、`S=(v_S+s)/√2` 的常用归一化下，树级非对角元可写为 `δm²_hs=λ_HS v v_S`，
   \[
   \tan(2\theta_{hs})=\frac{2\delta m_{hs}^2}{m_{S,0}^2-m_{h,0}^2}.
   \]
   远离简并且混合很小时可用 `θ_hs≈δm²_hs/(m_S²−m_h²)`，但符号、极角和自能重整化由实际模型约定决定；**近简并时不得外推小角公式**。
4. **近简并可观测量：** 在 $m_S\simeq m_h$ 处使用恰当的质量矩阵/复数二点函数、极点、总宽度与相干/非相干产生率，比较实测 Higgs 信号强度及适用的直接搜索。混合增强不自动意味着“新共振”或固定宽度排除带。
5. **竞争衰变：** $s\to A'A'$ 的两体道在 $m_S>2m_{A'}$ 时可能开放；经 Higgs 混合出现的 $s\to f\bar f,WW,ZZ,hh$ 分别需满足相应阈值及耦合。$h\to ss$ 若 $m_S<m_h/2$ 且实际三标量顶角非零，须与 Higgs exotic-decay 限制比较。还须计算 total width、BR 与寿命，进而区分 prompt、位移与 invisible 搜索。列为“可检查通道”不等于这些过程在全部参数点有可观测率。
6. **输出：** 给出 $m_S$ 分段的 `θ_hs` 或物理率、适用 Higgs/标量搜索原始引用、实验假设与重铸方法；标记已验证点与未评估点。只有在这些结果证明某区域效应小之后，才有理由保留 negligible portal benchmark。

**当前状态：未完成，需同一 UV 基准独立复核。** 不得使用合并版中的示意圈图系数、任何固定宽度“共振排除带”、任意 $h\to ss$ 上限或尚无模拟支持的全空间安全判断。

### 2.3 具体执行路径

1. 从原始拉格朗日量中提取标量势。
2. 推导真空条件和标量质量矩阵。
3. 明确质量本征态、混合角及其参数依赖。
4. 整理适用的实验限制和文献来源。
5. 判断这些限制是否覆盖原文参数扫描区域。
6. 必要时重新进行数值扫描。
7. 更新参数空间图及图注。
8. 在正文讨论新增约束对主要结论的影响。

### 2.4 论文中应新增的内容

建议在模型部分补充标量势和质量矩阵，在现象学部分补充标量约束，在数值结果部分展示约束叠加后的参数空间。

### 2.5 英文回复模板

> **Response:** We thank the referee for pointing out that the scalar-sector phenomenology requires a more explicit discussion. In the revised manuscript, we have clarified the scalar potential, the relevant mass parameters, and the conditions under which scalar mixing can arise. We have also examined the applicable constraints on the scalar mass range considered in our analysis and clarified the treatment of the region in which the additional scalar mass approaches the SM Higgs mass. The corresponding discussion and results have been added in Sec. [X] and Fig. [Y]. The impact on our main conclusions is [provide the actual quantitative result].

**注意：** 如果尚未完成相关环图计算或数值扫描，不应在回复中声称已经完成。应先完成工作，再将实际结果写入回复信。

### 2.6 补充：中间标量质量区域的定义与约束

**对应审稿意见：Major Point 1.2；Minor Point 6.3。Minor Point 1 关于 $m_{A'}$、$g_X$ 的目标范围及 “light” 的定义，另在 §6.1 单独处理；不将其误当作“中间标量质量区间”的专属意见。**

#### 2.6.1 审稿人真正关心的问题

审稿人要求说明标量的允许质量范围，并指出如果某个低质量区域受到很强的实验限制，应明确给出相关限制，再讨论剩余允许区域。

审稿人还指出，论文中“intermediate scalar-mass region cannot simply be assumed unconstrained”这句话不够清楚：所谓“中间质量”具体指什么？作者是在报告某项实际约束，还是只是在提醒读者不能忽略约束？

因此，本项工作不能仅仅把“intermediate”换成另一个形容词，而需要给出明确的质量区间、适用约束及其结论。

**对当前稿件可先作出的具体澄清（数值端点待逐篇核实）：** 现有整理把 B 工厂相关标量搜索概括为约 $0.04$ GeV 至 $6.5$–$7$ GeV；这只是不同分析范围的工作性概括，不应被写成一条统一、已核实的实验区间。文稿还提及约 $9$–$10$ GeV 的四轻子共振搜索，但其公开诠释采用自旋一媒介子假设。因而不能据此声称整个质量段已被排除。应逐篇记录搜索的实际质量端点、标量产生机制、接受度和 $S\to A'A'$ 等分支比，并判断是否需要重新诠释。任何排除结论都应针对相应耦合、产生率和分支比组合，而不是单独给出普适的 $m_S$ 或 $g_X$ 上限。

#### 2.6.2 具体执行步骤

**任务 A：定义质量区间**

1. 以标量质量 \(m_S\) 为主变量，结合相关实验搜索的适用范围，将研究区域分段。
2. 分段边界应来自实际的物理阈值、实验搜索覆盖范围、衰变模式变化或约束强度变化，而不是随意指定。
3. 对每个区间，注明主要衰变模式和影响实验可见度的关键参数。
4. 如果某个区间没有明确的物理分界，应直接使用数值范围描述，而不要继续使用含糊的“低质量”“中间质量”或“高质量”。
5. 将现有整理中约 $0.04$–$7$ GeV 的 B 工厂搜索范围单列为待核查项；逐篇核对其实际端点和假设。约 $9$–$10$ GeV 的自旋一四轻子结果须先判断能否针对标量重铸，不能直接作为本文的排除线。

建议使用下表作为整理模板：

| 标量质量区域 | 划分依据 | 主要衰变模式 | 相关实验限制 | 当前判断 |
|---|---|---|---|---|
| 区域 I | 待确定 | 待计算或查证 | 待核查 | 待确定 |
| 区域 II | 待确定 | 待计算或查证 | 待核查 | 待确定 |
| 区域 III | 待确定 | 待计算或查证 | 待核查 | 待确定 |

这里的区域 I、II、III 仅是工作标签，并非预先确定的物理质量区间。

**任务 B：建立实验约束与参数的对应关系**

对每项可能相关的实验约束，记录：

1. 约束的具体物理过程。
2. 所适用的标量质量范围。
3. 对混合角、产生截面、分支比或其他相关参数的假设。
4. 实验结果是排除某个参数区域，还是只对特定模型假设成立。
5. 该限制是否可以直接用于本文的 UV 完成。

不能仅凭某个搜索覆盖了相应的质量范围，就声称该区域已被排除；需要将实验灵敏度与本文模型预测的信号强度联系起来。

**任务 C：区分理论允许与实验允许**

建议把参数空间中的结论分成以下类别：

- **实验排除**：有适用于本文模型的实验结果支持。
- **理论不一致**：违反微扰性、稳定性或其他明确的理论条件。
- **EFT 适用范围之外**：不满足所采用 EFT 的有效性条件，但不等于完整 UV 模型被排除。
- **未分析区域**：当前没有足够计算或实验信息得出结论。
- **在已检查假设下允许**：满足已纳入的实验和理论条件，但不代表通过所有可能的约束。

特别注意：不能把“尚未检查”写成“允许”，也不能把“EFT 不适用”写成“UV 模型被实验排除”。

**任务 D：与 Higgs 门户混合分析统一**

将中间质量区域与 Major Point 1.3 的混合分析结合：

1. 在每个质量区域计算或估计 Higgs–标量混合。
2. 比较混合结果与相关 Higgs 实验约束。
3. 单独检查 \(m_S\simeq m_h\) 附近的近简并区域，因为混合角的简单近似可能在此失效。
4. 如果忽略 Higgs 门户混合，应给出可检验的理由，例如混合被定量证明足够小，而不是只陈述“假设混合可以忽略”。

对于近简并情况，应从完整的二阶标量质量矩阵或适当的自能修正出发分析；不能将远离简并时的微扰表达式直接外推到分母接近零的区域。

#### 2.6.3 论文中应增加什么

- 明确的标量质量区间定义。
- 每个区间对应的实验约束、理论条件及其适用假设。
- 对中间质量区域是否受限的明确结论。
- 对近简并区域的独立说明。
- 一张质量—耦合或质量—混合角图，区分已排除、理论不允许、未分析和在已检查条件下允许的区域。

如果没有足够数据制作完整参数空间图，至少增加一张汇总表，并在正文中明确说明尚未检查的部分。

#### 2.6.4 完成判据

- "intermediate scalar-mass region"有可复现的定义。
- 每项实验约束都注明适用条件。
- 论文不再暗示尚未分析的区域自动不受限制。
- 低质量、中间质量及近简并区域的讨论与标量混合分析一致。

#### 2.6.5 英文回复模板

> **Response to Major Point 1.2 and Minor Points 1 and 6.3:**
>
> We have replaced the qualitative description of the scalar-mass regions with an explicit classification based on the relevant physical thresholds and experimental coverage. For each region, we identify the applicable constraints and their assumptions, and distinguish experimentally excluded regions from theoretically inconsistent regions and parameter space that has not yet been fully analyzed. We have also clarified the treatment of the region near \(m_S \simeq m_h\), where the usual perturbative mixing approximation may require special care.

---

#### 2.6.6 将合并版中“标量相关实验线索”落到可核查的物理通道

不能只列“有实验约束”或照搬不同自旋的 exclusion plot。应逐条核对以下通道：

| 物理对象／过程 | 最低触发前提 | 必须记录的数据 | 与审稿问题关系 |
|---|---|---|---|
| $s\to A'A'$ | 实际规范顶角存在且 $m_S>2m_{A'}$ | 部分宽度、BR、$A'$ 后续衰变、接受度 | 直接决定 $S$ 寿命与可见搜索 |
| $s\to f\bar f,WW,ZZ,hh$ | $S$–Higgs 混合及相应阈值 | 有效耦合、宽度、BR、prompt/displaced 条件 | 直接标量搜索、Higgs 类比约束 |
| $h\to ss$ | $2m_S<m_h$ 且三标量耦合非零 | `hSS` 顶角、BR、Higgs 总宽度 | Higgs exotic-decay 约束 |
| Higgs 信号强度／质量附近双态 | 非零混合、相关质量区间 | 物理极点、宽度、信号率、所用组合数据 | $m_S\simeq m_h$ 是否受强限 |
| B 工厂、稀有介子衰变 | 有相应产生机制、衰变模式与质量覆盖 | 质量端点、接受度、寿命、原始实验论文 | “intermediate scalar mass” 具体是否受限 |
| 固定靶／束流打靶、LLP、位移顶点 | 生产截面与衰变长度匹配 | 衰变长度、探测器几何、背景、效率 | 不得把未检查区域说成允许 |
| LEP/LHC/未来 Higgs factory | 相应生产通道真实存在 | 混合角、截面、BR、能量/亮度 | 论文的可探测性主张 |
| $A'$ 的现有搜索及天体界限 | 新规范玻色子电流结构匹配 | $m_{A'}$, $g_A$, $g_V$, `ε` 与分支比 | 与 $S$ 排除分别计算；详见 §5.4、§5.8 |

合并版曾将 B 工厂相关工作概括为约 `0.04–7 GeV`，另讨论约 `9–10 GeV` 四轻子分析；前者必须逐篇查实际上下端点与实验假设，后者包含自旋一模型的公开解释，**不能直接视为对标量 $S$ 的排除**。这两组数字在本主文档仅作**文献核查线索**，不能画成已确认的通用区间。

#### 2.6.7 由“可忽略 S”转为可验收判断（B-7）

在至少一个明确的 UV 可实现 benchmark 下，列出 $S$ 产生和主要衰变、理论质量上界、已适用的限制、尚未评估的限制。然后在 **有数据覆盖** 的参数点比较“包含 $S$”与“只有轴矢量 EFT”产生的实验解释差异。如果差异在经评估域内不足以影响文章主要结论，可保留限定性的 EFT 近似；否则须将 $S$ 现象学加入正文并回归修订 Fig. 2。**不能把狭窄 benchmark 的结论外推为对整个 UV 完备模型的声明。**

### 2.7 $m_S$ 允许窗口的可复现扫描与交付格式（B-3/E-1）

**这一小节吸收合并版 §2.1(2) 的“微扰性、$g_X$、$v_S$、其他标量耦合、$A'$ 与 $S$ 约束”五项要求。** 任务是生成数值窗口，而不是填入凭空猜测的质量端点。

1. **锁定输入：** 对每个扫描点登记 `{m_{A'},g_X,λ_S,m_S,v_S,λ_HS,M_VLL,θ_L,θ_R,其他 Yukawa}`，以及电荷、VEV 归一化、RGE 截止尺度和相关稳定性/微扰性判据；明确哪些固定、哪些边缘化、哪些来自 benchmark。`g_X=0` 不可代入 $v_S=m_{A\prime}/(2g_X)$。
2. **先验理论筛选：** 计算 $v_S=m_{A\prime}/(2g_X)$ 与 `λ_S=2g_X²m_S²/m_{A'}²`；分别核对 $\lambda_S$ 微扰性、稳定性、树级 portal 输入、VLL/Yukawa 关系和适用 EFT 条件。若扩展破缺部门则重推质量映射，不沿用最小模型的 Fig. 2 线。
3. **物理通道计算：** 在各 $m_S$ 区间明确 $s\to A'A'$、混合诱导可见末态、可能的 Higgs exotic decay、寿命与探测器尺度；计算信号所需的截面或分支比，而不是仅列候选实验名字。
4. **实验重铸：** 建立实验名称、原始论文/数据版本、质量/耦合适用区间、spin/production、寿命、BR、置信水平、重铸关系、状态的登记表。$S$、$A'$ 的限制分开；必要时包含 Higgs signal strengths、B factory、固定靶、LLP、直接标量搜索以及条件性天体约束。
5. **合并可行域：** 输出“理论允许且已检查实验允许”、“理论不可实现”、“实验排除”、“未评估”、“纯 EFT 近似不适用”五类区域，分清不同层次。至少给 benchmark 表与一个标清假设的 `(m_{A'},g_X)` 切片，最好补 `(m_S,λ_HS)` 的 Higgs/标量约束图。
6. **结案条件：** 提供公式脚本、原始输入、可重现结果、每条引用及修订正文位置；有独立复核。未经这些交付，不得写“已获得完整的 $S$ 实验允许质量窗口”。

| 交付文件（建议） | 必备字段／验收要求 | 当前状态 |
|---|---|---|
| `scalar_benchmark_and_window.csv` | 每点 UV 输入、理论判据、$m_S$ 区间、判定依据 | 待计算 |
| `scalar_constraint_registry.md` | 各实验的对象、通道、假设、质量段、来源和适用性 | 待文献核查 |
| `portal_matching_and_near_degenerate.md` | 同一 UV–EFT 定义、圈级/反项、极点、可观测率 | 待独立复核 |
| `figure_UV_EFT_scalar_overlay.*` | 标签区分允许/排除/未评估/EFT 外，复现实验源 | 待作图 |

## 三、主要意见二：解释 EFT 参数范围与 UV–EFT 一致性

### 3.1 审稿意见的核心

**审稿人原文（Major Point 2，逐字引用）：**

> “Motivating the range of effective theory parameters. To further aid in the comparison between the UV theory and the two-parameter low-energy theory, it would be useful to explicitly state in one place (perhaps in a table or a figure like Fig. 2) the range of the effective model parameters that are feasible. The main phenomenological results are in Fig. 2, but it was not clear why this range of couplings and $A'$ masses were chosen: are values outside this range not allowed? What, if anything, does the perturbativity of the UV theory impose on the effective parameters?”

以下为整理者对这条原文的归纳，具体处理须回到上述原文及附录 A.2：

论文需要更清晰地解释：

- EFT 参数范围为什么这样选择；
- EFT 的适用条件是什么；
- EFT 参数如何由 UV 模型参数决定；
- 哪些区域受到实验排除；
- 哪些区域不满足理论条件；
- 哪些区域只是没有被扫描。

这几个概念必须严格区分。

### 3.2 需要补充的工作

#### 工作 A：列出参数扫描范围

按本文实际定义建立两张参数表，不使用未在论文中定义的通用 $m_X$ 或 $c_i$ 扫描变量。

**低能现象学参数：**

| 参数 | 物理意义 | 数值范围/基准 | 选择依据与约束 | 状态 |
|---|---|---|---|---|
| $m_{A'}$ | 新规范玻色子质量 | 按原文 Fig. 2 与正文逐项抄录 | 实验覆盖范围、目标现象学及 UV 一致性 | 待按指定版本核对 |
| $g_X$ | 新规范耦合 | 按原文 Fig. 2 与正文逐项抄录 | 实验限制、微扰性与 UV 可实现性 | 待按指定版本核对 |

**UV 完成参数及其关系：**

| 参数/关系 | 物理意义 | 应登记的内容 | 注意事项 |
|---|---|---|---|
| $v_S=m_{A'}/(2g_X)$ | 新 $U(1)$ 破缺尺度 | 对每个 $(m_{A'},g_X)$ 网格点计算 | 明确采用论文的荷归一化与质量关系 |
| $m_S,\lambda_S$ | 新标量质量与自耦合 | 标量质量 benchmark、Eq. (30)/(34) 的筛选条件 | 区分理论微扰性与实验排除 |
| $M_{E_\mu},M_{E_\tau}$ | 矢量样轻子质量 | 质量假设、简并/分裂情况与适用实验限制 | 不把质量下限直接当作混合角上限 |
| $\theta_{\mu L,R},\theta_{\tau L,R}$ | 轻–重轻子混合角 | 论文采用的 benchmark 及推导关系 | 区分严格纯轴极限与有限质量近似 |
| $c_\alpha/\Lambda\simeq y_\alpha\lambda_\alpha/M_{E_\alpha}$ | Eq. (3) 的维五算符树图匹配 | 说明匹配尺度、算符阶数及近似条件 | 这条匹配关系不等于 $(m_{A'},g_X)$ 平面的完整 UV 可实现性条件 |

具体数值须从本次锁定的论文版本抄录并核对，不在本工作计划中猜测或补造。

#### 工作 B：推导 UV–EFT 匹配关系

从 UV 拉格朗日量出发，明确说明：

1. 哪些重粒子被积分掉；
2. 采用了什么能标层级；
3. 保留了有效算符的哪一阶；
4. 每个 EFT 系数依赖哪些 UV 参数；
5. 哪些 EFT 参数组合无法由当前 UV 模型实现。

**对当前文稿应使用的匹配关系：** 本文并非只有抽象的两参数 EFT。Eq. (3) 已明确给出积分出 $E_\mu,E_\tau$ 后的维五算符，树图层面
\[
\frac{c_\alpha}{\Lambda}\simeq\frac{y_\alpha\lambda_\alpha}{M_{E_\alpha}},\qquad \alpha=\mu,\tau.
\]
修订时应说明 $M_{E_\alpha}$ 是被积分掉的 VLL 质量尺度，明确保留的算符阶数及 $M_{E_\alpha}$ 相对于过程能标的层级。不要引入与本文没有对应定义的一般 $c_i$ 扫描表，也不要把仍作为动力学自由度保留的 $A'$ 两参数现象学描述笼统称为“EFT 失效”。必须分开两类映射：A）Eq. (3) 的带电轻子质量算符匹配；B）给定 $(m_{A'},g_X)$ 后，是否存在满足 VLL 质量、混合角、标量自耦合微扰性及本文其他假设的 UV 参数组合。后者才直接回应 Major Point 2 对“feasible”参数范围的疑问。

如果 EFT 是通过重粒子交换产生的，应展示相应的匹配公式，并说明忽略高阶算符的条件。

#### 工作 C：检查 EFT 的适用范围

一般而言，EFT 要求过程能标低于被积分掉的新物理质量尺度，并且高阶项的忽略是合理的。

需要逐项检查：

- 被积分掉的粒子是否确实足够重；
- 过程能标是否接近 EFT 截断尺度；
- 耦合常数是否处于采用近似所需的范围；
- 是否存在高阶算符不可忽略的区域；
- 是否需要对接近 EFT 失效边界的结果作出限定。

不能仅凭某个参数值较大或较小，就不加说明地将相应区域称为有效或无效。

#### 工作 D：重新定义参数空间图例

建议将参数空间明确区分为：

- **Experimentally excluded**：被明确的实验或观测排除；
- **Theoretically inconsistent**：违反理论条件、微扰性要求或模型假设；
- **Outside the EFT validity range**：不满足当前 EFT 近似的适用条件；
- **Not scanned**：本文没有计算的区域；
- **Allowed within the assumptions of this analysis**：在本文采用的假设及纳入的约束下仍允许的区域。

特别注意：**未扫描区域不等于被排除区域。**

对 Fig. 2 而言，优先做法是叠加或单列说明 **UV-consistency overlay**：它应包含 Eq. (30)/(34) 的 \(\lambda_S\) 微扰性条件、所选 \(m_S\) benchmark、VLL 解耦层级及 portal 假设。这样能避免把低能图中未覆盖的区域误标为一般的“EFT 无效区”。

#### 工作 E：合并版 §2.3 的参数总表与联合 UV 实现性检验（C-1–C-3）

审稿人并不只要求给 $m_{A'}$、$g_X$ 两个范围；还要求判断这些 EFT 点**能否同时由同一组 UV 参数实现**。不能只列各参数单独满足的上限。拟添加到论文的总表应至少包括：

| 类别 | 参数 | 需说明的内容 | 判定状态 |
|---|---|---|---|
| 低能扫描 | $m_{A'}$, $g_X$ 或 $g_A$ | 研究上下限、扫描方式、动机；是否只是 Fig. 2 切片 | 待登记 |
| 标量/破缺 | $v_S$,$m_S$,$\lambda_S$,$\lambda_{HS}$ | Eq. (30)/(34) 映射、稳定性、Higgs 限制；是否有额外 VEV | 待联合筛选 |
| 重 VLL | `M_E,M_L` 等实际独立质量 | 模型质量本征态、直接搜索、质量简并假设 | 待核查 |
| 轻子质量/混合 | `θ_{ℓL}`, `θ_{ℓR}`, Yukawa | 同一质量矩阵生成 SM 轻子质量，满足 EW/CLFV | 待核查 |
| 非纯轴修正 | $g_V$, $\epsilon_{\mathrm{kin}}$ | 由该 benchmark 推导而非另行设定，比较实验 | 待计算 |
| 中微子扩展（若选） | 新荷、新 VEV、新质量矩阵 | 改变 $m_{A'}$、标量谱与 LFV，原扫描需要回归 | 待作者决策 |

建议把 Fig. 2 每个网格点分为：仅用于 EFT 展示 / 能被**某个** UV 参数集合实现 / 在检查的 UV 与实验限制下允许 / 不满足理论条件 / 尚未评估。若某点超出本文“研究兴趣范围”，不应自动标为理论排除。

合并版曾给出以 `2m_μ`、`O(1–10) GeV`、`10 GeV` 划分 `light A'` 的示例。它**不是经验证的普适分段**：轴/矢量电流、动能混合、可见与不可见衰变、寿命均影响通道。只可把明确的运动学阈值（例如 `2m_μ`）作为阈值提示，切勿直接推断阈值下“只能经圈图衰变到 `e⁺e⁻`”或“特定实验必然主导”。最终区间依论文实际 benchmark 和原始实验范围确定，并与 Minor 1、Minor 6.1 联动修改。

### 3.3 具体执行路径

1. 建立完整的参数定义表。
2. 推导 UV 参数与 EFT 系数的对应关系。
3. 说明 EFT 的能标层级和截断条件。
4. 对扫描点实施理论一致性筛选。
5. 分别标记实验排除区、理论无效区和未扫描区。
6. 重新绘制参数空间图。
7. 在正文中说明各类区域的物理意义。
8. 检查论文摘要和结论是否过度概括了 EFT 结果。

### 3.4 英文回复模板

> **Response:** We agree that the rationale for the EFT parameter ranges and their relation to the UV completion should be stated more clearly. We have added the relevant matching relations between the UV parameters and the EFT coefficients, together with an explanation of the scale hierarchy and theoretical criteria used in the analysis. We have also revised the parameter-space plots and captions to distinguish experimentally excluded regions from theoretically inconsistent regions and regions that were not scanned. These changes are presented in Sec. [X], Eqs. [Y–Z], and Fig. [N].

---

## 四、主要意见三：检查中微子振荡与 PMNS 混合矩阵的兼容性

### 4.1 审稿意见的核心

**审稿人原文（Major Point 3，关键句逐字引用；完整原文见附录 A.3）：**

> “Are neutrino oscillations possible?”
>
> “In this model, $U_A(1)_{L_\mu-L_\tau}$ invariance allows Weinberg operators for each generation. However, it appears that both the Yukawa matrices and neutrino masses must be aligned and therefore a non-trivial PMNS matrix does not appear to be possible.”
>
> “Thus it is not obvious to me how neutrino oscillations can be included in this framework.”

这几句是审稿人的原话；关于 Weinberg 算符是否允许以及质量矩阵的实际结构，仍须按本文荷分配独立核对，不能仅凭引文本身认定审稿人的技术判断完全正确。

模型的荷分配和场内容是否能够产生符合实验观测的中微子质量和混合，需要给出明确论证。

这是一个潜在的理论一致性问题，不能只靠增加一段定性说明解决。

### 4.2 需要补充的工作

#### 先澄清当前模型能够与不能够说明什么

当前拉格朗日量未包含右手中微子、Weinberg 算符或其他中微子质量生成项，因此它本身尚未给出中微子质量机制；Sec. III F 使用太阳中微子振荡的实验 flavor fractions，不能替代对模型内 PMNS 的推导。

按 Table I 的荷分配 $Q(L_\mu)=+1$、$Q(L_\tau)=-1$、$Q(S)=+2$（以 $Q_\ell=1$ 归一化），维五 Weinberg 算符不是“每一代各自允许”：$ee$ 与 $\mu\tau$ 结构可允许，而 $\mu\mu$、$\tau\tau$ 结构需伴随 $S^{(*)}$ 插入。准确的真空表述是：标准模型 Higgs 双重态 $H$ 也获得 VEV，但它在新 $U(1)$ 下中性；$S$ 是获得非零 VEV 的新 $U(1)$ 带荷标量。若没有其他带奇数新 $U(1)$ 荷的标量或破缺 VEV，$S$ 的 VEV 保留残余 $Z_2$，电子扇区与 $\mu,\tau$ 扇区之间的混合仍不能产生。因此，在不引入额外带合适荷的新场或破缺结构的前提下，最小内容不能展示完整的观测 PMNS 矩阵。此处应先给出该结构性判断，再决定采用扩展模型或收窄论文主张；若引入右手中微子，还要重新核对规范与引力异常抵消。

**可直接写入的结构性证明：** 在最小模型中，$S$ 是获得 VEV 的新 $U(1)$ 带荷标量，且 $Q(S)=2Q_\ell$；标准模型 Higgs $H$ 也获得 VEV，但在新 $U(1)$ 下中性。因此，$U_A(1)$ 自发破缺后保留残余 $Z_2$。电子扇区为偶，$\mu,\tau$ 及其 VLL 扇区为奇；因此所有规范不变算符都不能把 $e$ 与 $\mu,\tau$ 连接起来。等价地，对 $(L_iH)(L_jH)S^n(S^\dagger)^m$，$ee$、$\mu\tau$、$\mu\mu$、$\tau\tau$ 条目可由偶数荷补偿，而 $e\mu$、$e\tau$ 需要奇数荷补偿、对任意整数 $n,m$ 均无解。带电轻子矩阵也具有相同的 $\{e\}\oplus\{\mu,\tau\}$ 分块结构。

在这一结构下，若要求与观测到的非零质量平方差相容、相关质量本征态不发生使混合角失去物理可辨识性的精确简并，则 PMNS 矩阵（忽略不影响混合结构的相位，并允许质量本征态重新排序）必然包含一个纯电子味的质量本征态列；这与观测到的 PMNS 混合结构不相容。若把该纯电子味本征态按特定约定标记为 $\nu_1$，可写成 $\theta_{12}=\theta_{13}=0$，但这两个角的具体写法依赖质量本征态编号，不能作为与排序无关的结论。正文应展示显式分块矩阵，并在允许的质量排序下检验结论。以上判断的前提是没有其他奇荷标量或额外破缺 VEV。

#### 工作 A：明确中微子质量机制

首先确认模型采用哪一种机制：

- Dirac 中微子质量；
- Majorana 中微子质量；
- seesaw 机制；
- 其他扩展机制。

然后根据模型中的场和荷分配，列出所有允许的质量项与 Yukawa 相互作用。

#### 工作 B：构造中微子质量矩阵

根据实际拉格朗日量推导

\[
M_\nu.
\]

分析矩阵结构，包括：

- 哪些元素被对称性强制为零；
- 哪些元素可以独立变化；
- 矩阵的秩是否受到限制；
- 是否存在简并质量本征态；
- 是否能够产生非零的混合角。

如果模型强制中微子质量矩阵为对角形式，或只能产生受限的混合结构，就必须正面处理这个问题。

#### 工作 C：检验 PMNS 兼容性

如果模型声称可以解释中微子振荡数据，应证明其能够与观测到的质量平方差和混合角相容。

可以采用以下方式：

1. 解析推导允许的混合结构；
2. 给出满足观测约束的参数点；
3. 如果自由参数较多，则进行数值拟合；
4. 报告参数范围、拟合条件及采用的数据；
5. 说明是否存在额外的质量纹理或参数关系。

不能仅因为模型中存在中微子质量项，就认定其自动满足 PMNS 混合。

#### 工作 D：如果最小模型不兼容

若荷分配和最小场内容无法产生所需的混合，需要在以下路径中作出选择：

**方案一：最小扩展。**

增加必要的场或相互作用，使质量矩阵能够产生非平凡混合。一个可进一步研究的最小候选是引入带奇数 $U_A(1)$ 荷的标量，以打破上述残余 $Z_2$；它不是唯一可能的修复，也不能仅凭此就声称已得到可行 PMNS。随后必须检查新增自由度是否改变 $A'$ 质量—VEV 关系、标量势与 Higgs 混合、异常抵消、以及由带电轻子非对角结构引起的 LFV（例如 $\mu\to3e$ 和 $\mu$–$e$ 转换）。只有给出 PMNS 拟合点和这些约束的检验后，才能称该扩展与原有现象学相容。

**方案二：收窄论文主张。**

如果论文研究重点不是完整的中微子质量模型，可以明确说明本文只研究某个有效模型或现象学部门，并将完整中微子质量生成机制列为尚未解决的问题。

但必须确保论文其他部分没有暗示当前最小模型已经解释了全部中微子振荡数据。

#### 工作 E：当前 v6 最小场内容的结构性 PMNS 障碍与正式决策（D-2–D-4/E-2）

**模型事实：** 采用 v6 Table I 的 `Q(L_e)=0`、`Q(L_μ)=+1`、`Q(L_τ)=−1`、`Q(H)=0`、`Q(S)=+2`，且不加入其他带奇荷的破缺 VEV。在 $S$ 及 `S*` 插入后，偶数荷能得到补偿，电子味对 `μ/τ` 的奇数荷差不能被任何整数次 $S$ 插入消除。因此，允许的 Weinberg / 对应质量结构在电子味与 `μ–τ` 味之间分块。以不引入额外破缺的假设为前提，可写

\[
 M_\nu=\begin{pmatrix}a&0&0\\0&b&c\\0&c&d\end{pmatrix}.
\]

`μ–τ` 子块仍可混合，所以**不能泛称所有定义下 `U_PMNS=I`**；核心问题是缺乏观测所需的电子—其他味混合。仅添加带常规荷的右手中微子并不能自动破坏剩余 `Z₂` 分块。要做的是显式列出带电轻子矩阵、$m_D$,$M_R$,$M_\nu$、可允许算符及质量本征态，而不是只援引其他荷指派的文献。

**两个必须明确选择的方向：**

- **路线 A：扩展并证明。** 带奇荷且有 VEV 的 $\sigma/\Phi$，以及可能配套 `N_{eR},N_{μR},N_{τR}`（荷 `0,+1,−1`）是**候选模型设计**。可研究由奇荷 VEV 生成 `N_e–N_μ/N_τ` 交叉 Majorana 项，打破分块；但需真的写出完整规范不变拉氏量、$m_D$ 与 $M_R$，计算 $M_\nu$，检查矩阵秩/零元素、数值 PMNS 拟合、轻子味变、异常抵消、标量谱/portal、破缺真空与宇宙学条件。若新场荷为 1，候选质量映射 `m_{A'}²=g_X²(4v_S²+v_σ²)`；须按实际约定重推，并回归 §2–§3 的 Fig. 2 与质量窗口。
- **路线 B：限定并承认。** 保留带电轻子和轴矢量 EFT 的主要分析，但在正文清楚写明现有最小模型没有解释 PMNS 的质量部门，太阳中微子味比例只是实验输入，完整理论需要额外的中微子结构；**这是论文章节范围选择，不是物理问题已解决**，审稿人可能仍不接受。

无论哪条路线，Major 4.1 要用其原始编号再单独回应；数值拟合或明确限制范围之后才允许标记科研结案。其他 `L_μ−L_τ` 文献、带不同标量荷或 seesaw 结构的实验拟合结论，仅可作比较与文献线索，不得代替本文荷结构推导。

### 4.3 具体执行路径

1. 列出所有相关场的规范荷和额外 U(1) 荷。
2. 根据对称性写出允许的中微子质量项。
3. 构造完整的中微子质量矩阵。
4. 分析其秩、零元素和本征态结构。
5. 判断能否产生非平凡 PMNS 混合。
6. 若可行，给出解析条件或数值拟合。
7. 若不可行，考虑最小扩展或收窄论文主张。
8. 同步修改摘要、模型部分、现象学部分和结论。

### 4.4 英文回复模板：模型兼容时

> **Response:** We thank the referee for raising the question of compatibility with neutrino oscillation data. We have derived the neutrino mass matrix implied by the field content, charge assignments, and interactions of the model, and analyzed its mixing structure. We find that [state the verified result]. The derivation and the relevant parameter constraints have been added in Sec. [X] and Eqs. [Y–Z].

### 4.5 英文回复模板：最小模型不兼容时

> **Response:** We agree that the neutrino-mixing issue requires a more careful qualification. Our analysis indicates that the minimal field content and charge assignments considered here [state the verified limitation]. We have therefore revised the relevant claims and explicitly clarified this limitation in Sec. [X]. We also discuss the additional ingredients that would be required to address the observed mixing pattern, while leaving a complete analysis of the extended model beyond the scope of the present work.

---

## 五、主要意见四：补充实验与天体物理约束

### 5.1 审稿意见的核心

**审稿人原文（Major Point 4，节选）：**

> “Is this the full set of experimental constraints? The second half of the manuscript presents a set of experimental bounds on the two-parameter effective $A'$ model. It is not obvious if this is the full set of constraints on the model. [...] The following experimental bounds seem like they could be relevant. It would be helpful to either include them or justify why they are subdominant to the experiments presented.”

原文中的四个子项分别是 Major 4.1 中微子振荡、Major 4.2 动能混合、Major 4.3 有限 VLL 质量下的残余矢量耦合，以及 Major 4.4 恒星冷却。Major 4.1 的原文是：

> “Neutrino oscillation observations. See point #3 above. It appears that this model predicts a unit PMNS matrix, which is inconsistent with neutrino oscillations.”

完整原文见附录 A.4；下文编号沿用原始报告，不把 Major 4.1 因与 Major 3 重叠而省略。

需要确认论文是否完整处理了以下问题：

1. 中微子振荡与质量结构；
2. 额外 U(1) 规范玻色子与超荷之间的动能混合；
3. 有限质量 VLL 导致的残余矢量耦合；
4. 纯轴矢量近似的适用条件；
5. 恒星冷却等天体物理限制。

这些约束的适用性取决于具体模型参数，不能不加区分地套用。

### 5.2 动能混合

**审稿人原文（Major Point 4.2，节选）：**

> “There is no quantitative estimate of the amount of kinetic mixing generated with the ‘benchmark’ choices of $\theta\leq10^{-2}$.”
>
> “It would be useful to have parametric estimates of the amount of kinetic mixing one expects so that readers may compare to experimental bounds.”

对于两个 U(1) 规范场，可能存在形式为

\[
\mathcal L_{\mathrm{mix}}
=
-\frac{\epsilon}{2}F_{\mu\nu}F'^{\mu\nu}
\]

的动能混合项。

需要检查：

- 模型对称性是否允许该项；
- 是否在某个能标将其设为零；
- 带有相关荷的粒子是否通过环图诱导混合；
- 诱导混合是否影响新规范玻色子的有效耦合；
- 相关实验限制是否会改变原参数空间。

若选择在某一尺度将混合参数设为零，应说明这是特定边界条件，而非自动成立的普遍结论。

### 5.3 有限 VLL 质量与残余矢量耦合

**审稿人原文（Major Point 4.3，节选）：**

> “Since the authors focus on the phenomenology in the axial limit, one wants to make sure that any small-but-finite vector interaction isn't significant because the constraints on the coupling are orders-of-magnitude larger than the axial coupling.”

如果正文使用纯轴矢量耦合或某个简化极限，需要确认这一近似在有限 VLL 质量下是否仍成立。

具体工作：

1. 从完整拉格朗日量推导相关费米子质量矩阵。
2. 对角化并求出物理本征态的耦合。
3. 计算有限 VLL 质量下的矢量和轴矢量耦合。
4. 与大质量极限或其他简化极限比较。
5. 判断残余矢量耦合是否改变相关实验限制。
6. 明确近似的适用范围。

如果有限质量修正不显著，也应给出定量依据，而不是只写"可以忽略"。

### 5.4 恒星冷却约束

**审稿人原文（Major Point 4.4，逐字引用）：**

> “Are stellar cooling bounds not relevant? See e.g. 2511.09619 for a recent paper on this. If they are not, then this is certainly worth justifying.”

恒星冷却限制通常依赖粒子的质量、耦合强度、产生率及其在恒星环境中的传播行为。

需要逐项确认：

- 相关粒子能否在恒星内部产生；
- 粒子是否能够逃逸并携带能量；
- 所用约束适用于哪一质量和耦合区间；
- 约束依赖哪些天体物理假设；
- 是否存在适用性边界或理论不确定性。

不应把只适用于特定质量范围或特定耦合结构的界限，直接解释为对整个参数空间的排除。

**需与标量约束分开处理：** 当前文稿的 Table II 主要汇总轻标量 $s$ 的冷却与紧致星约束；审稿人 Major Point 4.4 所引 2511.09619 讨论的是亚 GeV $L_\mu-L_\tau$ **规范玻色子 $A'$** 的束流倾倒与超新星/冷却问题。因此需要独立检查 $A'$ 在超新星中的产生、俘获与逃逸区。常规矢量 $L_\mu-L_\tau$ 的结果不能在未核对轴矢量电流、纵向模、有限 $g_V$ 及动能混合贡献前直接套用；反之，也不能用 Table II 的标量限制代替这一检查。

**补充核查（E-5；合并版 §2.6 A6）：** 原报告点名 arXiv:2511.09619，但任何该文中的天体排除域都必须先判断其 $A'$ 的自旋/电流、质量、纵向模、核/轻子产生与俘获/逃逸机制是否适用于本文的轴矢量和有限 $g_V$,`ε` benchmark。v6 Table II 是针对**标量 $S$** 的限制，不能替代审稿人询问的**$A'$ 恒星冷却/超新星限制**。对两者分开建表：对象、介质、产生道、质量窗、寿命/逃逸、是否重铸、原文对应图号；若不适用必须说明模型或物理条件，不得只用“GeV 重所以无关”一句结案。

### 5.5 具体执行路径

1. 整理全部可能相关的实验与天体物理约束。
2. 为每项约束记录文献、质量范围、耦合依赖和适用假设。
3. 检查动能混合的树图与环图来源。
4. 推导有限 VLL 质量下的有效耦合。
5. 检查纯轴矢量近似的条件。
6. 根据适用范围评估恒星冷却界限。
7. 更新约束汇总表和参数空间图。
8. 在论文中说明未纳入的约束及原因。

### 5.6 英文回复模板

> **Response:** We thank the referee for emphasizing the need to clarify the additional constraints and the approximations used in the effective couplings. We have expanded the discussion of kinetic mixing, finite-VLL-mass effects, and the applicable stellar-cooling constraints. We now state explicitly the parameter ranges and assumptions under which each constraint applies. The finite-mass correction is [summarize the verified result], and the corresponding discussion has been added in Sec. [X] and Fig. [Y].

### 5.7 补充：动能混合的定量估计与实验意义

**对应审稿意见：Major Point 4.2。**

#### 5.7.1 审稿人真正关心的问题

审稿人认可纯轴矢量极限下动能混合可以消失这一点，但指出论文所选的 benchmark 对应有限的矢量样轻子质量，因此一般不能仅凭纯轴矢量极限就断定动能混合为零。

审稿人明确建议：提供预期动能混合大小的参数估计，使读者能够将其与实验限制比较；相关圈图的参数表达式可以从文献中获得。

**核心任务不是只证明动能混合在理论上可能存在，而是判断它在本文的 benchmark 和参数范围内有多大，以及是否影响论文结论。**

#### 5.7.2 具体执行步骤

**任务 A：确认动能混合的来源与定义**

从模型拉格朗日量出发，明确动能混合项的规范不变定义，例如：

\[
\mathcal L_{\mathrm{kin}}
\supset
-\frac{\epsilon}{2}B_{\mu\nu}X^{\mu\nu},
\]

其中 \(B_{\mu\nu}\) 和 \(X_{\mu\nu}\) 分别代表相应的规范场强张量；具体符号应与论文保持一致。

接下来：

1. 确认纯轴矢量极限对应哪些参数关系。
2. 确认在该极限下动能混合为零是精确结果、某阶近似结果，还是只对特定粒子谱成立。
3. 检查有限 VLL 质量和相关质量分裂是否会产生非零贡献。
4. 查找与本文粒子内容、规范荷及质量层次一致的圈图计算文献。

**本文 benchmark 的已知起点：** Eq. (22) 取 $M_{E_\mu}=M_{E_\tau}$，两者具有相同超荷、相反新 $U(1)$ 荷，因此其一圈阈值项在严格简并时相消；作者又在匹配尺度设 $\epsilon$ 为零。需要补充计算的并非重复这一结论，而是质量分裂、轻–重混合以及低于 VLL 阈值后的混合抑制项首次在何阶出现、数值有多大。这样才能区分“严格为零”“非零但可忽略”与“需要加入约束图”三种情形。

不要在未检查规范荷求和及抵消条件前，直接套用一个通用的一圈估计式。

**任务 B：获得可靠的参数表达式**

1. 从适用文献中取得动能混合的圈级表达式，或在模型内自行推导。
2. 明确公式使用的重整化方案、重整化尺度及粒子阈值。
3. 检查不同粒子的规范荷贡献是否抵消。
4. 若领先项抵消，应说明首个非零贡献出现在哪个阶次，或由何种质量分裂、对称性破缺或阈值效应产生。
5. 若使用近似对数表达式，明确其适用的质量层次和近似条件。

最终公式必须与模型的粒子内容和规范荷相匹配；不能仅凭形式相似就认定适用。

**任务 C：在 benchmark 下计算数值**

对论文所选 benchmark：

1. 列出参与动能混合计算的质量、耦合及其他必要输入。
2. 代入经过核实的表达式。
3. 给出 \(\epsilon\) 的数值或可信范围，并报告主要参数的不确定性。
4. 检查结果是否依赖重整化尺度、质量分裂或对消项。
5. 若论文扫描了多个 benchmark，应给出随关键参数变化的结果，而不只展示单个数值。

**需要填入的结果：**

| 项目 | 结果 |
|---|---|
| 所采用的动能混合表达式及来源 | 待查证 |
| benchmark 输入参数 | 待整理 |
| 计算得到的 \(\epsilon\) | 待计算 |
| 理论不确定性及近似条件 | 待评估 |
| 对实验限制的影响 | 待比较 |

这里不预填 \(\epsilon\) 的数量级，因为目前不能仅从审稿意见确定其具体值。

**任务 D：与实验限制比较**

1. 确定非零动能混合后，规范场的耦合结构如何改变。
2. 识别因此新增或增强的实验限制，并确认这些限制与本文的质量和耦合假设相容。
3. 将 benchmark 下的预测与适用实验限制进行定量比较。
4. 判断动能混合是否会改变原有参数空间、实验排除结论或纯轴矢量近似的有效性。
5. 若影响很小，给出数量级比较作为忽略它的依据；若影响不可忽略，应更新相应的约束图或结论。

**任务 E：解释与纯轴矢量极限的关系**

最终讨论必须明确区分：

- **严格纯轴矢量极限**：在论文定义的参数关系下，动能混合是否精确消失。
- **有限 VLL 质量的 benchmark**：是否存在非零的圈级贡献。
- **实验上可忽略的贡献**：即使不严格为零，是否足够小而不会改变论文结论。

这三个判断不能混为一谈。

#### 5.7.3 论文中应增加什么

- 动能混合的定义及适用的圈级表达式。
- 该表达式的可靠文献来源或推导。
- 在 benchmark 下的数值估计。
- 与适用实验限制的比较。
- 对纯轴矢量极限与有限质量情形的区别说明。

#### 5.7.4 完成判据

- 给出参数依赖，而不只是定性地说动能混合“非零”。
- 数值结果可以由列出的输入复现。
- 实验比较采用与模型假设相容的限制。
- 论文明确说明动能混合是否实质性改变主要结论。

#### 5.7.5 英文回复模板

> **Response to Major Point 4.2:**
>
> We have expanded the discussion of kinetic mixing beyond the strict axial limit. Using the relevant loop expression for the particle content and charge assignments of our model, we now provide a parametric estimate and evaluate it for the benchmark used in the phenomenological analysis. We compare the resulting contribution with the applicable experimental constraints and clarify whether it modifies the parameter space or conclusions presented in the original analysis. We also distinguish the exact axial-limit statement from the finite-mass benchmark considered in the paper.

---

### 5.8 原始 Major 4 与合并版约束线索的分层筛查（E-1–E-5）

合并版 §2.6 的约束清单不能作为“已排除”的总表，必须把**明确审稿要求**与**为保证完整性而额外筛查**的项目分开。前者：中微子振荡（§4）、benchmark 动能混合（§5.2、§5.7）、有限 VLL 导致残余矢量耦合（§5.3、§6.3）及 $A'$ 恒星冷却（§5.4）；此外 Major 1 已单独要求 $S$ 与 Higgs 数据（§2）。

| ID | 附加完整性筛查（不是审稿人逐字提出的独立点） | 启动门槛 | 只有什么证据才能纳入最终稿 |
|---|---|---|---|
| CS-1 | 若扩展 PMNS 后的 `μ→eγ`,`μ→3e`,`μ-e` 转换等 LFV | 新模型出现非对角耦合 | 由新拉氏量导出的率与对应原始实验数据 |
| CS-2 | APV、PVES/Møller 等宇称破坏实验 | 存在该实验敏感的电子/夸克轴-矢耦合组合 | 可适配电流、传播子和质量区间的约束映射 |
| CS-3 | 其他 $A'$ / $S$ 可见、不可见或 exotic decay | 真正存在相应顶角且运动学开放 | 宽度、BR、重铸与探测器接受度 |
| CS-4 | B 工厂、稀有介子衰变、固定靶、束流打靶 | 产生与衰变模式匹配、实验覆盖 | 信号预测与搜索假设逐项核对 |
| CS-5 | 长寿命标量 $S$、位移顶点/beam-dump | 寿命与探测器几何匹配 | 衰变长度、接受度、效率的可复核计算 |
| CS-6 | Higgs-factory 的 $S$ 搜索与 $h\to ss$ | 存在生产/三标量顶角并满足阈值 | 截面/BR、背景与实验灵敏度，未算只能作展望 |
| CS-7 | $S$ 与 $A'$ 的恒星/超新星分别筛查 | 分别满足介质产生和逃逸条件 | 两张独立的限制适用性登记表 |
| CS-8 | $(g-2)_\mu$ 的轴矢量与有限矢量贡献 | 相应顶角与积分适用于扫描质量段 | 按 v6 耦合定义计算符号/大小，再与实验及其他限制比较 |

**CS-8 吸收合并版中的额外线索 A10：** 对纯轴耦合不能不经计算就声称解释正的 `a_μ` 偏差；也不能因为某理论极限可能有相反符号就宣称它全参数空间必然是“最强限制”。核对 v6 已有的 $(g-2)_\mu$ 内容，**避免重复计入同一限制**；需要实验数值、理论输入以及采用的置信区间。CS-8 属于编辑性完整性筛查，非审稿人专门新增评论。

**具体交付与判定：** `constraint_registry.md` 每行应有“原始编号/CS 编号、对象 $S$ 或 $A'$、过程、模型顶角、质量范围、实验原文、采用假设、是否纳入、结果及复核状态”。对于不适用的实验给出明确原因；`未知/未核查` 不得标为 `安全`。避免把 $\epsilon_{\mathrm{kin}}$（与电磁/超荷场的动能混合）与有限 VLL 的直接 $g_V$ 混为同一修正。

## 六、次要意见及逐项处理建议

### 6.1 "Light"的定义与扫描范围

**审稿人原文（Minor Point 1，节选）：**

> “The word ‘light’ on page 2 has no reference scale.”
>
> “It would be very helpful if the authors decide on a range of $m_{A'}$ and $g_X$ of interest.”

**需要处理的问题：**

"Light"属于相对概念，需要结合模型质量尺度或实验范围明确含义。

**建议修改：**

- 在首次使用时给出定量定义；
- 明确扫描的质量上下限；
- 解释范围选择的物理依据；
- 在图注中标明固定参数和扫描参数。

**英文回复模板：**

> We have clarified the meaning of "light" and explicitly stated the mass range and the rationale for the scan in Sec. [X] and the caption of Fig. [Y].

### 6.2 Eq. (12) 附近的纯轴矢量极限

**审稿人原文（Minor Point 2，逐字引用）：**

> “Defining the pure-axial limit. Equation (12) gives the coupling of the $A'$ to the mass-basis fields. It is here that the ‘pure axial coupling’ limit is defined? i.e. $\theta_{\mu R}\to0$? If that is the case, it would help to define this as the pure-axial limit, a phrase which is used below (36) but not otherwise quantified.”

**需要处理的问题：**

需要说明纯轴矢量耦合是精确结果，还是仅在某些参数条件下成立的近似。

**建议修改：**

- 明确矢量耦合与轴矢量耦合的定义；
- 写出纯轴矢量极限所需的条件；
- 讨论有限 VLL 质量和混合修正；
- 说明该近似对数值结果的影响。

**应写入的模型专属关系：** 由 Eq. (16)，
\[
g_V=g_X\sin^2\theta_{\mu R},\qquad g_A=-g_X\cos^2\theta_{\mu R}.
\]
因此在本文所写的 μ 子扇区关系下，严格纯轴矢量点要求 $\theta_{\mu R}=0$。由于 $m_\mu\simeq\theta_{\mu L}\theta_{\mu R}M_{E_\mu}\neq0$，有限 $M_{E_\mu}$ 时不能同时令该混合严格为零；本文采用的是 VLL 解耦下的近似纯轴极限。修订时还应按 Eq. (12) 对 τ 子扇区写出对应的矢量/轴矢量耦合，并核对其符号与荷约定；在对应的纯轴极限下也需明确 $\theta_{\tau R}\to0$ 的条件。不得只给出 μ 子扇区条件而让“pure axial”一词覆盖整篇模型。

**英文回复模板：**

> We have clarified the conditions under which the pure axial-vector limit around Eq. (12) is obtained and stated the approximations involved. We have also discussed possible finite-mass corrections in Sec. [X].

### 6.3 VLL 质量下限、混合角限制与 Eq. (27)

**审稿人原文（Minor Point 3，节选）：**

> “Because the mixing angles scale inversely with the vectorlike lepton masses, it would be helpful to present lower limits on these masses. This, in turn, gives an upper limit on the $\theta_{(\mu,\tau)R}$ mixing angles which then gives an upper limit on the $A'$ vectorlike coupling to $L_{\mu-\tau}$. How do these bounds compare with the $\theta_{(\mu,\tau)(L,R)}$ bounds in equation (27)?”

**需要处理的问题：**

需要区分直接搜索给出的质量下限、模型依赖的混合角限制，以及它们与相关公式之间的关系。

**建议修改：**

- 说明质量下限来自何种实验；
- 说明限制是否依赖衰变模式和产生机制；
- 明确混合角限制的假设；
- 解释 Eq. (27) 的适用范围；
- 必要时给出质量和混合参数的联合限制。

**英文回复模板：**

> We have expanded the discussion of the VLL mass and mixing constraints, including the assumptions underlying these bounds and their relation to Eq. (27). The relevant parameter dependence is now stated explicitly in Sec. [X].

**补入合并版 §2.7 的完整传递链（F-3/F-4；与 E-4 联动）：** 在固定质量矩阵与其他 Yukawa 时，轻重混合角的近似量级常为 `θ∼ y v/M_VLL`，但使用这一近似前须写出哪些 `y`、`v` 和质量本征态参与。实验直接搜寻提供的 VLL 质量下限取决于 SU(2) 表示、衰变 BR 与寿命，**不可不经重铸就把任意实验数值当成当前模型下限**。

对 v6 的特定 benchmark，Eq. (21) 的关系 `m_τ≈θ_{τL}θ_{τR}M_E` 联合 Eq. (27) 两角 `≤10⁻²` 的选择，**条件性**给出 `M_E≳17.8 TeV`；这不等于新发现的 LHC 直接质量限，也不应笼统写成“Eq. (22) 的 10 TeV 自相矛盾”。同理 Eq. (16) `g_V=g_X sin²θ_{μR}`、`g_A=−g_X cos²θ_{μR}` 给出 `|g_V/g_A|=tan²θ_{μR}≲10⁻⁴`（此 benchmark 内）。这是**耦合大小推论，不是矢量敏感实验的最终安全证明**；必须与实际的 $\epsilon_{\mathrm{kin}}$、耦合对象和实验限制比较。见 §5.8、§6.7。

### 6.4 "Conservative benchmark"的含义

**审稿人原文（Minor Point 4，逐字引用）：**

> “Conservative benchmark. Equation (27) is presented as a ‘conservative benchmark.’ What does this mean? A benchmark point would be a choice of this mixing angles. A constraint is an upper bound. Eq. (27) is written as an upper bound, but is described as a benchmark. This is not simply semantic: readers would want to understand if $10^{-2}$ is an experimental upper limit or simply a convenient choice.”

**需要处理的问题：**

"Conservative"需要明确指出究竟在哪个方面保守。

**建议修改：**

- 说明该基准点在参数取值、实验约束、理论近似还是其他方面保守；
- 如果没有明确依据，应改用中性描述；
- 如条件允许，可比较不同基准点下的结果。

**对 Eq. (27) 的具体核查：** 文稿先由 $Z\to\mu^+\mu^-$ 宽度得到左手混合约为数个百分点的示意限制，又指出某些 global VLL fits 可达到 per-mille，随后统一选取 $\mu,\tau$ 左右手混合都不超过 $10^{-2}$。因此“conservative”并非自动成立：它可能相对单一 LEP 宽度估计更严格，却未必相对适用的 global fit 更保守；而右手混合的约束来源也不能直接照搬左手结果。建议给出所采用 fit、表示和置信水平；若未完成此核对，应改称“illustrative decoupling benchmark”。

**英文回复模板：**

> We have clarified what is meant by the "conservative benchmark" and specified the assumptions supporting this characterization. Where the term was not sufficiently justified, we have revised the wording.

### 6.5 μ 子对撞机部分的篇幅与深度

**审稿人原文（Minor Point 5，关键段落节选；完整原文见附录 A.9）：**

> “What is the purpose of including muon collider bounds? The second half of the paper focuses on existing experimental bounds on the effective theory. It is a strange change in tone to include hypothetical muon collider bounds for future reach.”
>
> “The authors simply focus on the forward-backward asymmetry. Why not also include polarization asymmetries? Or would there be asymmetries in the $ee$ versus $\tau\tau$ final states?”
>
> “Given the first half of the paper, though, it seems that the real ‘smoking gun’ for this UV completion is the physics of the $S$ particle which should be tested in any Higgs-factory phase of a future lepton collider.”

**需要处理的问题：**

如果论文没有系统的信号与背景分析，却给出较强的未来对撞机结论，论证可能不充分。

**建议修改：**

若仅提供定性讨论：

- 缩短该部分；
- 将其定位为未来研究展望；
- 避免使用未经计算支持的定量结论。

若保留定量预测，则需要明确：

- 对撞机能量；
- 积分亮度；
- 信号产生过程；
- 主要背景；
- 事件选择；
- 探测效率；
- 统计分析方法；
- 主要系统误差。

**英文回复模板：**

> We have revised the muon-collider discussion to better match the level of quantitative analysis presented in this work. Specifically, we have [shortened the discussion to an outlook / added the assumptions and estimates described in Sec. X].

### 6.6 "Representative bounds"及其他模糊表述

**审稿人原文（Minor Point 6，按原始子编号摘录）：**

1. “The word ‘light’ on page 2 has no reference scale.”
2. “At the bottom of page 11, when referring to Table II, the authors write ‘representative bounds.’ What does representative mean? Does it mean these are the most stringent bounds? Are these ‘some’ bounds? Is the list ‘complete’ in any sense?”
3. “Between page 12-13: ‘...do not provide a universal $g_X$ bound, but they show that the intermediate scalar-mass region cannot simply be assumed unconstrained.’ What does intermediate mass mean? It is also not clear what the intended content of this statement is: are the authors presenting a bound? Why would the reader assume that a new particle in this range would be unconstrained?”
4. “Below (34): ‘we impose Eq. (34) point by point’, it's not clear what is meant by ‘point.’”
5. “Page 21, first paragraph of Section E. What is the ‘parameter region of interest’? This wasn't clearly defined anywhere.”
6. “Page 21, end of section D: What's the significance of the $v_S=2$ GeV line? What does it mean that $y_{s\mu\mu}$ ‘becomes large’ (nonperturbative)? Why plot it? Is it a perturbativity bound?”

以上均为审稿人原文；中文解释和下方建议属于整理者的分析。完整上下文见附录 A.10。

**需要处理的问题：**

以下表述需要更明确的定义：

- Table II 中的 "representative bounds"；
- 中间标量质量区域的约束；
- Eq. (34) 附近的 "point by point"；
- Sec. E 中的 "parameter region of interest"；
- Sec. D 中曲线 "becomes large" 的含义。

**建议修改：**

1. 说明 "representative bounds" 是否指代表性约束，还是当前最强约束。
2. 对中间质量区域，解释是否存在实验灵敏度空档或不同衰变模式。
3. 对 "point by point"，明确比较的参数、映射关系和判断标准。
4. 对 "parameter region of interest"，给出可复现的定义。
5. 对 "becomes large"，给出定量判据，并检查是否意味着微扰性失效。

**可直接替换的具体说明：**

- “intermediate scalar-mass region”应给出可复现的数值定义。现有整理中的 B 工厂约 $0.04$–$7$ GeV 范围须逐篇核实；可见标量搜索需结合产生机制、接受度和分支比判断是否可重铸。约 $9$–$10$ GeV 的公开四轻子自旋一诠释不能不加修改地套用到标量。
- “point by point”应明确为“对每个 $(m_{A'},g_X)$ 网格点，以 $v_S=m_{A'}/(2g_X)$ 代入 Eq. (34) 检查微扰性条件”。
- “parameter region of interest”应改为满足本文所假定即时衰变、质量阈值和分支比的明确参数范围。
- Fig. 2 的 $v_S=2$ GeV 灰虚线是恒定 $v_S$ 的引导线；在 $m_S=10$ GeV、$\lambda_S\le4\pi$ benchmark 下，它对应 Eq. (34) 的标量自耦合微扰性边界。它不是 $y_{s\mu\mu}$ 的非微扰边界：按本文 $y_{s\mu\mu}=m_\mu/v_S$，该线上约为 $0.053$。因此应将“becomes large”分别量化为哪一个耦合变大，不能把这条线误说成缪子 Yukawa 失去微扰性。

**英文回复模板：**

> We have revised the relevant wording to make the definitions and criteria more precise. In particular, we now clarify the meanings of "representative bounds," "point by point," and the "parameter region of interest," and quantify the behavior discussed in Sec. [X].

**合并版 §3.6 的逐句回归要求：** `light A'` 必须在引言首次使用处给参照尺度与目标范围（不是直接采用旧文随意分成“低于 2m_μ 只能衰变 e⁺e⁻”）；`representative bounds` 明确是 *non-exhaustive*、本工作纳入还是某质量段的主导限制；`intermediate scalar mass` 必须指认实验质量端点、物理参数与模型假设；`point by point` 明确是 Fig. 2 中每一 `(m_{A'},g_X)` 网格点且如何映射 $v_S$；`parameter region of interest` 要在首次出现与图注给出具体条件；Fig. 2 $v_S=2\,\mathrm{GeV}$ 线是指定 `m_S,λ_S^max` benchmark 下的**标量自耦合微扰性边界**，不能写成缪子 Yukawa 的非微扰界。按 v6 耦合归一化 `y_{sμμ}=m_μ/v_S`；含 `√2` 的历史旧表达须回 v6 核对，不能照搬。

### 6.7 补充：矢量样轻子（VLL）约束的定量传递链

**对应审稿意见：Minor Point 3；同时关联 Major Point 4.3 和 Eq. (27)。**

#### 6.7.1 审稿人真正关心的问题

审稿人指出，矢量样轻子的混合角通常与其质量有关。在有限的 VLL 质量下，混合角可能受到直接搜索限制；这些限制进一步影响矢量耦合。因此，不能只给出一个所谓“保守基准值”，却不解释它与实验上限的关系。

需要建立的逻辑链是：

\[
\boxed{
\text{VLL 质量限制}
\longrightarrow
\text{混合角限制}
\longrightarrow
\text{矢量耦合限制}
\longrightarrow
\text{与 Eq. (27) 比较}
}
\]

#### 6.7.2 具体执行步骤

**任务 A：确定质量下限的来源**

1. 列出模型中的 VLL 粒子及其电荷、表示和相关混合参数。
2. 查找与这些粒子的产生及衰变模式相匹配的直接搜索结果。
3. 核实实验限制所依赖的衰变分支比、粒子寿命、混合假设和质量简并情况。
4. 只有在模型假设相容时才使用相应的质量下限；不能将某一种衰变模式的限制无条件套用到所有 VLL。

记录表：

| 粒子 | 实验质量下限 | 适用的衰变假设 | 采用的混合假设 | 来源 |
|---|---|---|---|---|
| \(E_\mu\) | 待查证 | 待查证 | 待查证 | 待补 |
| \(E_\tau\) | 待查证 | 待查证 | 待查证 | 待补 |

如果模型中的粒子并不对应实验搜索所假设的信号，应重新评估限制，而不是直接引用其质量下限。

**任务 B：从质量推导混合角限制**

1. 从模型拉格朗日量和质量矩阵中写出相关轻子混合关系。
2. 在与论文一致的近似下，推导混合角对 VLL 质量及 Yukawa 耦合的依赖。
3. 将任务 A 中经过核实的质量下限与 Yukawa 耦合、轻子质量关系共同使用，计算或约束混合角。
4. 若关系只在小混合近似下成立，应说明适用条件，并在必要时使用完整质量矩阵对角化。

不要直接套用一个通用的 \(1/M_{\rm VLL}\) 标度作为最终结论，也不要把质量下限误当成混合角上限。对本文的关系 \(m_\ell\simeq\theta_{\ell L}\theta_{\ell R}M_{E_\ell}\)，质量限制只约束左右混合角的乘积；各自的上限还依赖 Yukawa 取值及电弱精确测量。具体标度取决于模型的质量项和混合结构。

**任务 C：将混合角限制传递到矢量耦合**

1. 从模型的规范相互作用项出发，写出质量本征态下的矢量耦合。
2. 明确该耦合对混合角、规范耦合和 VLL 质量的依赖。
3. 将任务 B 的限制代入，获得在所采用假设下的耦合上限。
4. 检查有限的矢量耦合 \(g_V\neq 0\) 是否会显著改变论文的实验约束。

如果混合角与矢量耦合之间还依赖其他自由参数，就应给出这些参数的范围或扫描结果，而不是给出唯一的上限数值。

**任务 D：与 Eq. (27) 比较**

必须澄清 Eq. (27) 的基准点究竟属于以下哪一类：

- 实验给出的上限；
- 理论上允许的最大值；
- 为展示现象学结果而选择的代表性 benchmark；
- 在某组参数假设下得到的估计值。

如果它只是 benchmark，就不能称为实验上限。建议将基准点与约束范围分开呈现，并解释为什么所选参数是保守的或具有代表性。

#### 6.7.3 论文中应增加什么

- VLL 质量下限及适用假设的简表。
- 从质量到混合角、再到矢量耦合的公式或定量关系。
- 对 Eq. (27) 中 benchmark 性质的明确说明。
- 必要时增加有限 \(g_V\) 下的约束比较；若其效应可以忽略，应给出支持这一判断的数值或参数范围。

#### 6.7.4 完成判据

- 每一个采用的质量下限都能追溯到适用的实验分析。
- 混合角及耦合限制由模型关系推导，而非凭经验假定。
- Eq. (27) 的基准值与实验上限不再混淆。
- 论文清楚说明有限 VLL 质量是否改变原有 EFT 约束。

#### 6.7.5 英文回复模板

> **Response to Minor Point 3:**
>
> We have clarified the constraints on the vector-like leptons and their implications for the mixing angles and effective vector couplings. The revised discussion identifies the experimental assumptions underlying the adopted mass limits and derives the corresponding parameter restrictions within our model. We also clarify the status of the benchmark in Eq. (27), distinguishing it from an experimental upper bound. Where relevant, we discuss the impact of finite vector-like lepton masses and nonzero vector couplings on the phenomenological constraints.

### 6.8 补充：μ 子对撞机研究的必要性、可观测量与额外标量信号

**对应审稿意见：Minor Point 5；同时关联 Major Point 1。**

#### 6.8.1 审稿人真正关心的问题

审稿人对论文中突然引入假想未来 μ 子对撞机的实验限制提出了疑问，主要包括：

1. 为什么需要讨论 μ 子对撞机约束？该部分与前文模型研究的关系是什么？
2. 相关分析与审稿版本所称的相关文献相比，有什么新的内容？（审稿报告原文写的是 Ref. 83；本分析此前记录的 arXiv:2608.27258 v1 对应编号为 Ref. [62]；本轮核对的最终投稿稿 `axial_vector_model_building-v6.pdf` 中，对应的 μ 子对撞机文献为 Ref. [85]。三个编号属于不同版本的编号映射，不应混用。）
3. 论文只研究前后向不对称性（forward-backward asymmetry），是否遗漏了偏振不对称性及不同末态的其他不对称性？
4. 完整 UV 模型包含额外标量。未来轻子对撞机，特别是 Higgs 工厂阶段，是否能够探测这一标量？

**修改目标：** 使 μ 子对撞机部分不再只是额外的限制曲线，而是明确说明它如何检验纯轴矢量 EFT、UV 完成及其独有预测。

#### 6.8.2 具体执行步骤

**任务 A：核对审稿版本所称的相关文献，明确本文的增量**

1. 以本轮最终投稿稿为基准，μ 子对撞机相关文献列为 Ref. [85]；v1 版本记录为 Ref. [62]，审稿报告原文写 Ref. 83。最终稿 Ref. [85] 的题名为 “Gauged $L_\mu-L_\tau$ at a muon collider”。应以当前稿件参考文献表为准，并将其他版本编号仅作为历史映射记录。比较时提取对撞机能量、信号过程、观测量、参数假设和统计方法。
2. 将本文的设置逐项与该文献比较。
3. 列出真正新增的内容，例如不同的耦合极限、不同的参数空间、额外的可观测量或 UV 模型解释。
4. 如果本文没有实质性的新增计算，应缩短该部分，将其定位为现有结果在本模型中的应用，而不要声称提出了新的对撞机分析。

建议建立比较表：

| 比较维度 | 审稿报告所称的相关文献（报告写 Ref 83；arXiv v1 为 Ref. [62]） | 本文 | 需要采取的行动 |
|---|---|---|---|
| 对撞机能量与亮度 | 待核查 | 待核查 | 统一或解释差异 |
| 信号过程与末态 | 待核查 | 待核查 | 指出新增过程 |
| 耦合及参数范围 | 待核查 | 待核查 | 说明模型特有部分 |
| 可观测量 | 待核查 | 前后向不对称性等 | 评估新增观测量 |
| UV 完成的额外标量 | 待核查 | 待核查 | 明确是否覆盖 |

**任务 B：评估其他对撞机可观测量**

在现有前后向不对称性的基础上，判断以下观测量是否适用于论文的过程与实验设定：

- **偏振不对称性**：在具有相应束流偏振能力的设定下，评估左右手耦合对截面和不对称性的影响。
- **不同末态的不对称性**：检查不同末态的角分布及不对称性是否能区分模型参数或背景过程。
- **总截面与角分布**：判断是否能提供比单一不对称性更直接或互补的约束。
- **参数可辨识性**：检验不同观测量能否打破耦合之间的退化。

执行时需要：

1. 明确过程、末态、束流能量、亮度和偏振假设。
2. 给出对应的可观测量定义。
3. 对照参考文献，确定是否需要重新计算，还是只需讨论已有结果。
4. 只有在新增分析能形成可靠结果时才加入数值图；否则将其列为未来工作，不要将未完成的分析描述为本文成果。

**任务 C：把 UV 标量与未来轻子对撞机联系起来**

这一任务与 Major Point 1 相互关联。额外标量的探测前景不能只根据“模型中存在标量”作判断。

1. 先确定允许的标量质量范围、相关耦合及其主要衰变道。
2. 检查标量是否可通过 Higgs 混合、与新规范玻色子的相互作用或其他模型允许的过程产生。
3. 对各质量区域，判断对应的产生过程、衰变产物和现有实验限制是否支持可探测性分析。
4. 区分现有实验限制与未来对撞机预期灵敏度。
5. 若没有完成信号与背景分析，只给出有明确假设的定性讨论，不宣称已经证明可探测。

对审稿人点名的 Higgs-factory 阶段，应单独说明候选信号的前提：$e^+e^-\to Zs$ 依赖 Higgs–$S$ 混合；$h\to ss$ 依赖三标量耦合与 $m_S<m_h/2$；其他产生道取决于模型允许的耦合。它们可作为待评估的互补路径，而不是在尚未完成 portal 匹配、分支比和背景分析前就宣称的发现前景。

#### 6.8.3 论文中应增加什么

- 一段解释未来 μ 子对撞机研究动机的文字。
- 一张与当前修订稿中对应的 μ 子对撞机文献的比较表，或者一段明确的创新点说明。
- 对偏振不对称性、不同末态及额外标量探测前景的简要评估。
- 若新增计算确实完成，再增加相应的参数空间图或不对称性曲线。

#### 6.8.4 完成判据

- 读者能够理解为什么这一节属于本文，而不是与主线无关的补充。
- 本文相对于当前修订稿中对应文献的增量被明确说明。
- 已完成的计算与建议开展的未来分析被清楚区分。
- UV 标量的探测前景与 Major Point 1 的标量质量、耦合和混合分析保持一致。

#### 6.8.5 英文回复模板

> **Response to Minor Point 5:**
>
> We have revised the discussion of the future muon collider to clarify its motivation and its relation to the existing analysis in Ref. [current number]. We now explicitly distinguish the results reproduced from the literature from the aspects specific to our model. We have also discussed the potential complementarity of polarization and final-state asymmetries, subject to the relevant collider assumptions. Finally, we have clarified how the additional scalar predicted by the UV completion could provide complementary signatures at future lepton colliders. We have restricted quantitative claims to analyses supported by the stated assumptions and calculations.

---

> 这是检查 v6 **已经写了什么** 的证据表，不代表剩余实验工作已完成；具体策略仍由 §6.1–6.8 决定。

### 6.9 最终稿 v6 的 Minor Points 逐项核对（事实复查表）

| 原始编号 | v6 中的处理 | 当前判断 | 剩余问题 |
|---|---|---|---|
| Minor 1：参数范围与 “light” | 摘要说明 \(A'\) 的研究质量范围从 MeV 到 TeV，并给出 Fig. 2 参数平面 | **部分处理** | 引言中 “light neutral spin-one bosons” 仍需要明确参照尺度；应区分论文目标范围与模型普适允许范围。
| Minor 2：纯轴矢量极限 | Eq. (16) 给出有限混合的矢量/轴矢量耦合，Eq. (36) 说明后续约束采用 pure-axial limit | **大体处理，建议再明确** | 严格纯轴极限对应右手混合趋于零；有限 VLL 质量下的实际 benchmark 是近似纯轴，而非自动精确为纯轴。
| Minor 3：VLL 质量下限与混合角 | Eqs. (21)–(27) 讨论质量、混合角、LEP 宽度与 global fits | **部分处理** | 缺少适用的直接搜索质量下限清单及衰变假设；需把条件性推导与实验限额分开。
| Minor 4：“conservative benchmark” | 正文给出 LEP 估计、global fit 量级并采用 \(10^{-2}\) 混合角 benchmark | **部分处理** | “conservative”是否相对全部适用约束成立尚未证明；若未完成比较，应考虑用 “illustrative decoupling benchmark”。
| Minor 5：μ 子对撞机 | Sec. IV、Fig. 3、Eqs. (65)–(67) 给出角分布和前后向不对称性示例，并明确 detector-level simulation 超出本文范围 | **部分处理** | 仍缺少完整探测器级限制、偏振不对称性及 UV 标量/Higgs 工厂的系统分析；新增贡献应按现有计算范围表述。
| Minor 6.1：“light” | 摘要给出质量范围 | **部分处理** | 首次使用时仍需定义参照尺度。
| Minor 6.2：“representative bounds” | Table II 说明数值是 order-of-magnitude、继承原文假设的代表性上限 | **基本处理** | 不应进一步宣称 Table II 是完整或总是最强的限制集。
| Minor 6.3：“intermediate scalar mass” | Sec. II.C 讨论 BaBar/Belle 的约 \(0.04\)–\(6.5\)–\(7\) GeV 标量搜索，并指出约 \(9\)–\(10\) GeV 的 Belle II 解释是自旋一结果，不能直接套给标量 | **基本处理** | 如要声称某一区间允许或排除，仍须核查具体产生机制、接受度与分支比。
| Minor 6.4：“point by point” | Eq. (35) 明确 \(v_s=m_{A'}/(2g_X)\)，正文说逐点施加 Eq. (34) | **部分处理** | Eq. (30)/(34) 在 v6 中一致；应说明按 $v_s=m_{A\prime}/(2g_X)$ 对每个网格点检查 Eq. (34)，并核对审稿报告所用版本。
| Minor 6.5：“parameter region of interest” | Sec. III.E 说明四轻子产生、衰变和重质量下 rate-level recast 的适用范围 | **部分处理** | 没有把 prompt decay 对应到明确的寿命/参数判据，也没有覆盖所有模型参数。
| Minor 6.6：\(v_s=2\) GeV 与 “becomes large” | Fig. 2 图注把该线解释为特定 \(m_s\) benchmark 下的标量微扰性边界，不是实验排除线 | **部分处理** | 该线与 Eq. (30)、Eq. (34) 一致；不得把它说成缪子 Yukawa 的非微扰边界。

## 七、推荐的科研执行路线

### 阶段 A：锁定理论结构

**目标：** 确认模型本身的假设和理论关系。

执行任务：

1. 整理完整拉格朗日量。
2. 汇总场内容与荷分配。
3. 推导标量质量矩阵和混合角。
4. 推导中微子质量矩阵。
5. 检查有限 VLL 质量下的耦合结构。
6. 核查动能混合项是否允许。
7. 整理所有近似条件。

**阶段交付物：**

- 理论推导笔记；
- 参数定义表；
- 近似条件表；
- 中微子质量矩阵分析。

### 阶段 B：核查 UV–EFT 对应关系

**目标：** 说明数值扫描所覆盖的区域是否属于模型有效范围。

执行任务：

1. 整理 UV 参数和 EFT 系数。
2. 推导匹配关系。
3. 检查能标层级。
4. 检查微扰性与理论一致性。
5. 区分实验排除、理论无效和未扫描区域。
6. 更新图例与参数空间图。

**阶段交付物：**

- UV–EFT 匹配公式；
- 理论一致性筛选条件；
- 更新后的参数空间图；
- 解释参数范围的正文段落。

### 阶段 C：补充现象学约束

**目标：** 确认主要结果是否受到遗漏约束影响。

执行任务：

1. 整理 Higgs 和标量相关限制。
2. 检查动能混合。
3. 计算有限 VLL 质量修正。
4. 评估恒星冷却等适用约束。
5. 对约束进行联合检查。
6. 根据结果决定是否重新扫描。

**阶段交付物：**

- 约束汇总表；
- 更新后的数值结果；
- 修订后的图表；
- 对主要结论影响的说明。

### 阶段 D：修改论文和回复信

**目标：** 让每一条审稿意见都能在修订稿中找到对应修改。

执行任务：

1. 按审稿人原始编号逐条引用。
2. 对每一条意见直接作答。
3. 说明新增了哪些理论、计算或文字内容。
4. 标注修改位置。
5. 解释修改对结论的影响。
6. 检查摘要、引言、正文和结论的一致性。
7. 在最终排版后核对页码、行号和图表编号。

**阶段交付物：**

- 修订稿；
- 逐点回复信；
- 最终检查清单。

---

**模板保护规则（适用于全文所有英文示例）：** `We have added/calculated/excluded` 属于未来有证据时才可使用的回复措辞；未完成任务只能作为占位草案。若修订模型使 Eq. (30)/(34)、Fig. 2 等定义变化，须重新核算所有交叉引用，不允许简单复用历史结论。

## 八、逐点回复信的标准结构

每条回复建议包含五个部分。

### 8.1 引用审稿意见

完整引用审稿人的英文原文，保留原有 Major/Minor 编号与子编号；不要把整理者的中文归纳放进引号冒充审稿人原话。若只引用部分句子，应使用省略号明确标示删节，并保证上下文和原意不变。可参照本文件各节引文及附录 A。

### 8.2 直接回答问题

第一段应直接回应审稿人的核心疑问，而不是只写感谢。

### 8.3 说明实际完成的工作

明确指出新增了哪些内容，例如：

- 理论推导；
- 数值扫描；
- 文献核查；
- 约束比较；
- 图表更新；
- 文字澄清。

### 8.4 指出修改位置

填写准确的章节、公式、图表、页码和行号。

### 8.5 说明对结论的影响

明确说明新增分析是否改变结论。如果结论没有改变，应提供实际依据。

### 8.6 总体回复开头模板

> We thank the referee for the careful reading of our manuscript and for the constructive comments. We have revised the manuscript to clarify the theoretical assumptions, strengthen the discussion of the scalar sector and the UV–EFT correspondence, examine the compatibility with neutrino-mixing requirements, and make the scope of the phenomenological constraints more explicit. Below, we respond to each comment point by point. All page and line numbers refer to the revised manuscript.

**重要：** 只有实际完成相应修改后，才可以在回复信中使用 “we have revised,” “we have added,” 或 “we have shown” 等表达。

---

## 九、最终提交前检查清单

### 理论结构

- [ ] 所有场的规范荷和额外 U(1) 荷已核对。
- [ ] 标量势包含所有允许且相关的项。
- [ ] 标量质量矩阵和混合角推导正确。
- [ ] 中微子质量矩阵与模型荷分配一致。
- [ ] 已准确说明 $H$ 与 $S$ 都获得 VEV，但 $H$ 在新 $U(1)$ 下中性、$S$ 是带荷标量；已说明残余 $Z_2$ 的成立条件，并展示 PMNS 分块结构及质量本征态排序的限定。
- [ ] 已对 PMNS 兼容性作出有依据的结论。
- [ ] 若采用中微子扩展，已重新检查新增 VEV 对 $A'$ 质量、标量混合、异常抵消及 LFV 的影响。
- [ ] 纯轴矢量近似的适用条件明确。
- [ ] 已检查有限 VLL 质量修正。
- [ ] 已讨论动能混合的来源和处理方式。

### EFT 与参数扫描

- [ ] 每个参数的扫描范围及依据已说明。
- [ ] UV–EFT 匹配关系已给出。
- [ ] EFT 的适用条件明确。
- [ ] 实验排除区、理论无效区和未扫描区域已区分。
- [ ] 参数空间图例与正文解释一致。

### 现象学约束

- [ ] 标量与 Higgs 相关限制已核查。
- [ ] B 工厂相关标量搜索的质量端点已逐篇核对；约 $9$–$10$ GeV 自旋一结果已按产生率、衰变道和分支比的适用性判断能否重铸。
- [ ] 中微子振荡相关问题已处理。
- [ ] 动能混合相关限制已评估。
- [ ] 恒星冷却约束仅在适用条件满足时使用。
- [ ] 所有新增约束均标注来源、假设和适用范围。
- [ ] 已评估新增分析对主要结论的影响。

### 表达与回复信

- [ ] "light" 等术语定义清楚。
- [ ] "conservative benchmark" 有明确依据。
- [ ] "representative bounds"等表述准确。
- [ ] 已准确说明 Fig. 2 的 $v_S=2$ GeV 线是标量自耦合微扰性条件的引导线，而非缪子 Yukawa 的非微扰界。
- [ ] μ 子对撞机部分与实际分析深度相符。
- [ ] 每条审稿意见均有独立回复。
- [ ] 每项回复都能在修订稿中找到对应修改。
- [ ] 页码、行号、公式编号和图表编号均已核对。
- [ ] 没有将尚未完成的工作写成已经完成的结果。

---

## 十、最重要的策略建议

这轮修改不应仅被视为语言润色。审稿人关注的重点包括模型理论自洽性、EFT 的适用范围以及现象学分析的完整性。

建议按照以下顺序投入时间：

1. **先判断模型能否满足中微子质量与 PMNS 混合要求。** 如果这一点存在结构性问题，应先解决，避免在不完整的模型上投入大量数值工作。
2. **再建立 UV–EFT 参数映射并检查扫描范围。** 这是解释结果是否具有物理意义的基础。
3. **随后补充标量扇区和其他约束。** 根据新增分析判断是否需要重新扫描。
4. **最后处理术语、图表、μ 子对撞机展望和逐点回复信。**

对于每个主要问题，都应形成完整的论证链：

**审稿人提出的问题 → 理论推导或定量计算 → 论文修改 → 实际结果 → 对原结论的影响 → 回复信中的明确回答。**

不要先预设计算结果，也不要为了回应审稿人而加入没有充分依据的结论。对于无法在当前论文范围内解决的问题，应明确说明假设、局限和后续工作，而不是模糊处理。

---

## 十一、四项补充内容的优先级与验收清单

本章汇总 §2.6、§5.7、§6.7、§6.8 四项补充任务的交付要求与当前状态。

| 优先级 | 补充任务 | 对应章节 | 需要交付的结果 | 状态 |
|---|---|---|---|---|
| 高 | 中间标量质量区域 | §2.6 | 明确分区、适用约束、允许性判断 | 待完成 |
| 高 | 动能混合 | §5.7 | 圈级表达式、benchmark 数值、实验比较 | 待完成 |
| 高 | VLL 限制 | §6.7 | 质量—混合角—耦合的定量链条 | 待完成 |
| 中 | μ 子对撞机分析 | §6.8 | 与当前修订稿中对应文献的比较、观测量评估、标量探测前景 | 待完成 |

### 11.1 补充任务的验收判据

- **中间标量质量区域**：质量分区可复现，每项约束注明适用条件，不把“尚未检查”写成“允许”，近简并区 \(m_S\simeq m_h\) 单独处理。
- **动能混合**：给出参数依赖的表达式与 benchmark 数值，结果可由列出的输入复现，明确区分严格轴矢量极限、有限质量贡献与实验可忽略性。
- **VLL 限制**：质量下限可追溯到具体实验分析，混合角与耦合限制由模型关系推导，Eq. (27) 的 benchmark 性质与实验上限不再混淆。
- **μ 子对撞机**：与当前修订稿中对应文献的增量被明确说明，已完成计算与展望性讨论严格区分，UV 标量探测前景与 §2.6 的质量、耦合、混合分析一致。

> **执行原则：** 先完成会影响模型一致性与实验限制的计算（中间标量质量区域、动能混合、VLL 限制），再决定是否扩展对撞机现象学（μ 子对撞机）。若某项分析最终证明影响很小，应在文稿中给出定量依据；若尚未完成，应明确标为未分析或未来工作，而不是提前作出肯定结论。
---

## 十二、审稿意见追踪矩阵与最终状态管理

本章是整个修订工作的总控表，覆盖主要意见、次要意见和跨章节一致性检查。第十一章只汇总四项专项补充任务；本章则用于跟踪**所有审稿意见从问题识别到最终回复的闭环**。表内状态是初始管理建议，不代表相关理论推导、文献核查或数值计算已经完成。

### 12.1 先锁定输入材料与版本

在开始正式修改前，先建立唯一的修订基线，避免不同版本的公式编号、文献编号和审稿意见编号混用。

- [ ] 保存当前存档 v6 PDF、原始审稿报告及其可用校验值；实际送审 PDF 版本不作为本轮阻塞输入。
- [ ] 保存每位审稿人的完整原文意见，保留原始编号和逐条分段。
- [ ] 将本文档中“Major Point / Minor Point”的归并编号逐项映射回原始意见；提交前不得只凭本计划中的编号回复。
- [x] 已以当前存档稿 v6 PDF 核对 Eq. (12)、Eq. (27)、Eq. (30)/(34)、Fig. 2、Table I/II 及 μ 子对撞机文献编号。编号映射为：审稿报告写 Ref. 83；v1 记录为 Ref. [62]；当前 v6 中对应文献为 Ref. [85]。公式放大复核确认 Eq. (30) 与 Eq. (34) 内部一致；原始审稿报告引用的边界形式不同，按项目决策不追查实际送审版本，继续以当前 v6 为基准。
- [ ] 对每个用于定量排除的实验结果保存原始论文或官方分析链接，并记录发布日期、质量范围、置信水平、产生模式和衰变假设。
- [ ] 建立修订稿、计算脚本、输入参数、图表和回复信的版本记录；任何数值更新都应能追溯到对应输入和代码版本。

**输入材料未锁定前，不要最终定稿文献编号、页码、行号或回复信中的具体修改位置。**

### 12.2 状态定义

| 状态 | 使用条件 |
|---|---|
| 待核对输入 | 尚未确认原稿、审稿意见或原始文献的准确版本。 |
| 待决策 | 需要在扩展模型、收窄论文主张或调整分析范围之间作出明确选择。 |
| 待理论推导 | 需要从拉格朗日量、荷分配或质量矩阵推导，尚无可复核结果。 |
| 待文献核查 | 已识别相关限制，但尚未核实原始来源及适用假设。 |
| 待数值计算 | 公式和输入尚未代入，或结果尚未独立复现。 |
| 待修改正文 | 分析已有结论，但尚未写入修订稿或更新图表。 |
| 待最终验收 | 正文已修改，但交叉引用、复现性或回复信尚未核验。 |
| 已完成 | 有明确的推导、计算文件、原始文献或修订稿位置作为证据，且验收条件已满足。 |
| 不适用 | 说明该项为何不适用于本文，并提供模型或实验依据；不能仅因工作量大而标为不适用。 |

### 12.3 总体追踪矩阵

> **编号说明：** 下表保留原始报告的 Major Point 1–4、Minor Point 1–6 及子项编号。Major 4.1 与 Major 3 在科学内容上重叠，但必须在追踪矩阵和回复信中分别标记；对应英文原文见附录 A。

| 意见/工作包 | 核心问题与依赖关系 | 最低交付证据 | 验收条件 | 初始状态 |
|---|---|---|---|---|
| 输入基线（前置门槛） | 原稿、审稿意见和文献版本是否一致 | 版本清单、原始意见编号映射表、引用清单 | 所有编号和修改位置均能追溯到指定版本 | 待核对输入 |
| Major 1：标量扇区；相关 Minor 1、6.3 | 依赖完整拉格朗日量、荷分配和标量势；涉及 Higgs portal、质量混合、质量近简并与实验搜索 | 完整势、真空条件、质量矩阵、混合参数、稳定性条件、约束来源表；必要时更新扫描图 | 每个质量区间有明确定义；约束假设可追溯；近简并区单独处理；结论与计算一致 | 待理论推导/文献核查 |
| Major 2：UV–EFT 一致性 | 依赖 UV 拉格朗日量、Eq. (3) 匹配关系和扫描参数定义 | UV–EFT 匹配推导、能标层级、参数表、理论筛选结果和更新图例 | 清楚区分实验排除、理论不一致、EFT 近似不适用和未扫描区域 | 待理论推导/数值计算 |
| Major 3：PMNS 兼容性 | 依赖场内容、规范荷、允许的质量项和残余对称性；是模型扩展与否的决策门槛 | 显式中微子质量矩阵、带电轻子矩阵、分块结构证明；若扩展则给出拟合和新增约束 | 明确选择“扩展模型”或“收窄主张”；不能只以实验 flavor fractions 替代模型内 PMNS 分析 | 待决策/理论推导 |
| Major 4（总体）：实验约束是否完整 | 统领标量 $S$、中微子振荡、动能混合、有限矢量耦合和恒星冷却等约束；与 Major 1、3 交叉引用 | 约束完整性表，逐项列出已纳入、被论证为次要及尚未检查的限制 | 每项未纳入的约束都有明确理由；不得把“代表性约束”写成“完整约束集” | 待文献核查 |
| Major 4.1：中微子振荡 | 与 Major 3 重叠，但必须保留独立追踪编号 | 质量矩阵/PMNS 结构证明，或指向 Major 3 的同一结论和证据 | 在回复信中明确回应 Major 4.1，不因与 Major 3 重复而遗漏 | 待理论推导/正文修改 |
| Major 4.2：动能混合 | 依赖规范荷、VLL 质量谱、混合结构及匹配边界条件 | 适用圈级表达式、重整化尺度与阈值说明、benchmark 数值及实验比较 | 区分严格为零、非零但可忽略和会改变约束三种结论；数值可复现 | 待文献核查/数值计算 |
| Major 4.3、Minor Point 3：VLL 约束 | 依赖粒子表示、衰变模式、直接搜索假设及轻–重混合关系 | 原始实验来源、质量下限、混合角关系、有限质量下的 $g_V/g_A$ 及与 Eq. (27) 的比较 | 质量下限与混合角上限不混淆；benchmark 不冒充实验上限；有限质量影响有定量判断 | 待文献核查/数值计算 |
| Major 4.4：恒星/超新星等约束 | 必须区分轻标量 $s$ 与规范玻色子 $A'$，并检查产生、俘获和逃逸条件 | 按粒子种类分开的来源表、适用质量与耦合范围、对本文电流结构的适用性判断 | 不把标量限制代替 $A'$ 限制；不将常规矢量结果未经核对地用于轴矢量情形 | 待文献核查 |
| Minor 2：Eq. (12) 纯轴矢量极限 | 依赖有限 VLL 质量下的左右混合关系和耦合定义 | $g_V$、$g_A$ 定义、纯轴极限条件及有限质量修正说明 | 明确严格极限与本文 benchmark 近似的区别 | 待理论核对/正文修改 |
| Minor 4：Eq. (27) conservative benchmark | 依赖所采用的电弱精确测量、global fit 和置信水平 | 约束来源、左右混合的独立假设、benchmark 选择理由 | 若没有比较证据，改为中性术语，如 illustrative decoupling benchmark | 待文献核查 |
| Minor 5：μ 子对撞机 | 依赖当前修订稿对应文献、对撞机设定以及 UV 标量分析 | 文献比较表、能量/亮度/信号与背景假设、观测量适用性说明 | 明确本文新增贡献；没有完成的定量分析只能作为展望；标量探测论述与 portal 结果一致 | 待文献核查/取舍决策 |
| Minor 6 及相关模糊术语 | 涉及 “light”、“representative bounds”、“point by point”、“parameter region of interest”、“becomes large” 等 | 每个术语的定量定义、参数映射或约束来源 | 术语能由读者复现；不把定性形容词当作定量结论 | 待正文修改 |
| 跨章节一致性 | 摘要、引言、正文、图表、结论和回复信可能使用不同假设或旧结果 | 交叉引用表、图表清单、结论变更记录 | 新增约束若改变结果，摘要和结论同步更新；所有编号均对应最终稿 | 待最终验收 |

### 12.4 定量结论与文献证据登记表

每一项用于支持“排除”“允许”“可忽略”“微扰”或“结论不变”的判断，都应登记证据。没有证据记录的结论不得直接进入最终回复信。

| 结论 ID | 要支持的具体结论 | 推导/原始来源 | 适用假设与范围 | 输入参数与结果文件 | 对应正文/图表 | 状态 |
|---|---|---|---|---|---|---|
| C-01 | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 | 待核查 |
| C-02 | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 | 待核查 |
| C-03 | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 | 待核查 |

登记要求：

1. 理论结论应链接到推导或方程；数值结论应记录输入、代码/版本和输出文件；实验结论应链接到原始论文或官方结果。
2. 若使用文献中的排除线，应记录其置信水平、产生过程、衰变模式、分支比假设和质量覆盖范围。
3. 若将文献结果重铸到本文模型，应保留从实验可观测量到本文参数的映射过程。
4. 若某项结论依赖 benchmark，应列出全部固定参数，不能只写一个最终数值。
5. 若分析最终证明某项效应可忽略，应同时给出其数量级、与相关实验灵敏度的比较以及忽略它的适用范围。

### 12.5 阶段门槛与依赖关系

**Gate 0：输入材料锁定。** 完成原稿、审稿报告、文献版本和编号映射。未完成时，不冻结回复信编号及页码行号。

**Gate 1：模型结构决策。** 优先完成 PMNS 分块结构判断、是否需要扩展模型的决策，以及完整标量势的推导。若决定扩展模型，先检查新增 VEV 对规范玻色子质量、异常抵消、标量混合和带电轻子味变约束的影响。

**Gate 2：UV–EFT 与有限质量效应。** 完成匹配、能标层级、微扰性筛选、动能混合及 VLL 有限质量修正。只有当输入和公式确定后，才开展依赖这些输入的数值扫描。

**Gate 3：约束联合检查与结果更新。** 核查标量、规范玻色子、VLL、恒星/超新星等适用约束；判断是否必须重扫参数空间，并记录每一项约束对原结果的影响。

**Gate 4：论文与回复信定稿。** 先更新正文和图表，再写逐点回复；最后统一核对摘要、结论、图注、公式编号、文献编号、页码和行号。

### 12.6 最终验收规则

- [ ] 每条原始审稿意见均映射到追踪矩阵中的一行，且没有遗漏或重复回复。
- [ ] 每条主要意见均有“问题—方法—证据—结果—对原结论的影响—正文位置—回复信”的完整链条。
- [ ] 所有数值、排除区间和实验界限均能追溯到计算输入或原始来源。
- [ ] 所有“已完成”状态均附有可检查的证据；未完成事项没有被写成已完成成果。
- [ ] 对无法在本稿范围内解决的问题，明确写出模型假设、局限和处理方式，而不是模糊地称其为允许区域。
- [ ] 若新增分析改变了模型主张或参数空间，摘要、引言、图表、结论和回复信均已同步更新。
- [ ] 最终回复信的每个修改位置都在最终排版稿中逐项核实。

> **总原则：** 追踪矩阵用于管理研究任务，不替代物理推导、实验文献核查或数值计算。只有在证据登记、正文修改和验收条件全部满足后，才将任务状态更新为“已完成”。


---

## 附录 A：原始审稿意见英文原文（按原始编号）

**来源：** 资料库文件 `dw13678_report_1_a.pdf`，标题为 “Report for DW13678 Fang”，共 4 页。以下保留审稿报告的英文措辞、编号、拼写及标点；为便于阅读，仅将 PDF 的换行合并为段落，并将公式符号转写为 LaTeX。引文中的技术判断属于审稿人的意见，不自动等于经独立验证的结论。

### A.1 Major Point 1 — Phenomenology of the scalar

> **1. Phenomenology of the $S$ scalar.** The second half of the paper reviews a set of experimental bounds on only an effective theory of the $A'$ axially coupled to the $L_{\mu-\tau}$ current. This leaves a major gap between these two parts of the paper: the authors show that their UV theory requires a scalar $S$ that cannot be arbitrarily decoupled from the low-energy dynamics, e.g. from (34) which states that $m_S^2<4\pi(m_{A'}/2g_X)^2$.
>
> **1.1** It is thus an odd choice to exclude the scalar from the phenomenology of the effective theory: if the $S$ is unavoidable at phenomenologically relevant scales, shouldn't one of the main points of the paper be that the only known UV completion of an axial $L_{\mu-\tau}$ gauge boson has a prediction for a scalar particle in a mass range that can be probed by colliders?
>
> **1.2** What is the range of phenomenologically allowed $S$ mass including perturbativity limits on $\lambda$ and a motivated range of $m_{A'}$ and $g_X$. For example: perhaps the authors imagine a range of $m_{A'}$ below some benchmark mass where certain experimental constraints on $g_X$ become very strong. Then with that set of constraints (which should be stated clearly, see minor point #1 below), one may give a range of $m_S$ and comment on the experimental constraints.
>
> **1.3** Above (34): the authors “assume negligible Higgs-portal mixing.” Is this interaction not generated at loop level? It seems that $S$-$h$ mixing cannot be avoided due to $\mu$ and $\tau$ loops. In turn, this seems like it would lead to strong experimental bounds on the UV completion. In fact, once there is mixing, is there not a resonance where the mixing becomes large as $m_S\to m_h$? It would be useful to quantify the size of this mixing over the allowed range of $m_S$. Existing Higgs measurements may set the strongest bounds on the UV completion. If these bounds are obviously negligible (though again, I expect this to be strongly constrained as $m_S\to m_h$), then the authors should present this as the justification for ignoring $S$ in the low-energy theory. ((Though I am still skepticial that the $S$ can be ignored since it cannot formally decouple.))

### A.2 Major Point 2 — Motivating the range of effective theory parameters

> **2. Motivating the range of effective theory parameters.** To further aid in the comparison between the UV theory and the two-parameter low-energy theory, it would be useful to explicitly state in one place (perhaps in a table or a figure like Fig. 2) the range of the effective model parameters that are feasible. The main phenomenological results are in Fig. 2, but it was not clear why this range of couplings and $A'$ masses were chosen: are values outside this range not allowed? What, if anything, does the perturbativity of the UV theory impose on the effective parameters?

### A.3 Major Point 3 — Neutrino oscillations

> **3. Are neutrino oscillations possible?** The Standard Model is defined with only left-handed neutrinos because of the possibility that neutrinos are their own antiparticle. In such a case neutrino masses are generated through, e.g. through the Weinberg operator.
>
> **3.1** In this model, $U_A(1)_{L_\mu-L_\tau}$ invariance allows Weinberg operators for each generation. However, it appears that both the Yukawa matrices and neutrino masses must be aligned and therefore a non-trivial PMNS matrix does not appear to be possible.
>
> **3.2** Perhaps a full model would require right-handed neutrinos. These would now be charged under $U_A(1)_{L_\mu-L_\tau}$, which likely means the second and third generation must appear as vectorlike combinations. However, it seems to me that mixing between generations is prohibited by $U_A(1)_{L_\mu-L_\tau}$.
>
> Thus it is not obvious to me how neutrino oscillations can be included in this framework. If there is a simple solution, the authors should include it. If there is a known less-simple solution in the literature, the authors should cite this. Otherwise, at best this will be a confusing point. At worst, it would make the construction inconsistent with neutrino oscillation experiments.

### A.4 Major Point 4 — Completeness of experimental constraints

> **4. Is this the full set of experimental constraints?** The second half of the manuscript presents a set of experimental bounds on the two-parameter effective $A'$ model. It is not obvious if this is the full set of constraints on the model. (See also point #1 above: I would have liked to see a section discussing the bounds on the $S$ within this model since it cannot be decoupled.) The following experimental bounds seem like they could be relevant. It would be helpful to either include them or justify why they are subdominant to the experiments presented.
>
> **4.1** Neutrino oscillation observations. See point #3 above. It appears that this model predicts a unit PMNS matrix, which is inconsistent with neutrino oscillations.
>
> **4.2** There is no quantitative estimate of the amount of kinetic mixing generated with the “benchmark” choices of $\theta\leq10^{-2}$. The authors make the insightful point that kinetic mixing goes to zero in the axial limit, but because this limit is tied to the size of the mixing (the mass of the vectorlike leptons), for the above benchmark there is non-zero kinetic mixing. It would be useful to have parametric estimates of the amount of kinetic mixing one expects so that readers may compare to experimental bounds. One could invoke parametric expressions in the literature for the relevant loop diagrams.
>
> **4.3** Another way of reframing the above point: the bounds presented are in the pure axial limit. Since the authors present a UV model that only realizes the axial coupling in a decoupling limit, it would be useful to comment on possible experimental bounds on the small vector-like coupling in a model with non-infinite vectorlike fermion masses. If these bounds are always small compared to the axial bounds, this should be stated and justified. The importance of this point is as follows: often bounds are sensitive to the chiral structure of interactions. Sometimes a vector interaction is more tightly constrained than its axial counterpart. Since the authors focus on the phenomenology in the axial limit, one wants to make sure that any small-but-finite vector interaction isn't significant because the constraints on the coupling are orders-of-magnitude larger than the axial coupling.
>
> **4.4** Are stellar cooling bounds not relevant? See e.g. 2511.09619 for a recent paper on this. If they are not, then this is certainly worth justifying.

### A.5 Minor Point 1 — Range of parameters

> **1. Range of parameters.** The general cosntruction of the model is clearly written, but it is difficult for the reader to envision the mass and coupling range that the authors are targeting. It would be very helpful if the authors decide on a range of $m_{A'}$ and $g_X$ of interest. For example: is there a range of masses where experimental or theoretical limits are less constraining? Is there some set of phenomenology that the authors week to realize with a “light” $A'$? If so, they should define “light.” (see, e.g. the first word of the introduction, which is not defined with respect to any reference mass scale.)

### A.6 Minor Point 2 — Defining the pure-axial limit

> **2. Defining the pure-axial limit.** Equation (12) gives the coupling of the $A'$ to the mass-basis fields. It is here that the “pure axial coupling” limit is defined? i.e. $\theta_{\mu R}\to0$? If that is the case, it would help to define this as the pure-axial limit, a phrase which is used below (36) but not otherewise quantified.

### A.7 Minor Point 3 — Bounds on the vectorlike leptons

> **3. Bounds on the vectorlike leptons.** Because the mixing angles scale inversely with the vectorlike lepton masses, it would be helpful to present lower limits on these masses. This, in turn, gives an upper limit on the $\theta_{(\mu,\tau)R}$ mixing angles which then gives an upper limit on the $A'$ vectorlike coupling to $L_{\mu-\tau}$. How do these bounds compare with the $\theta_{(\mu,\tau)(L,R)}$ bounds in equation (27)?

### A.8 Minor Point 4 — Conservative benchmark

> **4. Conservative benchmark.** Equation (27) is presented as a “conservative benchmark.” What does this mean? A benchmark point would be a choice of this mixing angles. A constraint is an upper bound. Eq. (27) is written as an upper bound, but is described as a benchmark. This is not simply semantic: readers would want to understand if $10^{-2}$ is an experimental upper limit or simply a convenient choice.

### A.9 Minor Point 5 — Muon collider bounds

> **5. What is the purpose of including muon collider bounds?** The second half of the paper focuses on existing experimental bounds on the effective theory. It is a strange change in tone to include hypothetical muon collider bounds for future reach. The authors do not justify why a future muon collider is the way to test this model in the future and the section feels like it is tacked on. Most of the section emphasizes that the muon collider search would be a “standard” follow up of existing work (Ref 83) and so this section does not seem particularly novel. The authors simply focus on the forward-backward asymmetry. Why not also include polarization asymmetries? Or would there be asymmetries in the $ee$ versus $\tau\tau$ final states? Given the first half of the paper, though, it seems that the real “smoking gun” for this UV completion is the physics of the $S$ particle which should be tested in any Higgs-factory phase of a future lepton collider. I feel that this section either adds too little and should be downplayed as an example of future tests, or otherwise should have its own full fledged exploration (which may be a separate paper).

### A.10 Minor Point 6 — Terminology

> **6. Terminology**
>
> **6.1** The word “light” on page 2 has no reference scale.
>
> **6.2** At the bottom of page 11, when referring to Table II, the authors write “representative bounds.” What does representative mean? Does it mean these are the most stringent bounds? Are these “some” bounds? Is the list “complete” in any sense?
>
> **6.3** Between page 12-13: “...do not provide a universal $g_X$ bound, but they show that the intermediate scalar-mass region cannot simply be assumed unconstrained.” What does intermediate mass mean? It is also not clear what the intended content of this statement is: are the authors presenting a bound? Why would the reader assume that a new particle in this range would be unconstrained?
>
> **6.4** Below (34): “we impose Eq. (34) point by point”, it's not clear what is meant by “point.”
>
> **6.5** Page 21, first paragraph of Section E. What is the “parameter region of interest”? This wasn't clearly defined anywhere.
>
> **6.6** Page 21, end of section D: What's the significance of the $v_S=2$ GeV line? What does it mean that $y_{s\mu\mu}$ “becomes large” (nonperturbative)? Why plot it? Is it a perturbativity bound?

### A.11 Recommendation

> In its current form, the paper is not ready for publication. The major points above must be addressed. It's entirely possible that I have misinterpreted some of these points, but if that is the case then they at least indicate ideas that must be clarified before the manuscript merits publication. I strongly encourage the authors to further address the minor points.
>
> The paper can be a useful addition to the model building literature. However, the question of whether this class of model can be consistent with neutrino oscillations is critical. I also feel that dismissing the physics of the scalar $S$ ignores the actual predictions of the UV model—otherwise the authors are simply justifying the phenomenology of the effective axial theory.

---

## 附录 B：最终稿事实、公式与跨版本差异（查证库）

> 本附录只提供**可回溯的 v6 核对依据**，不取代第 2–6 章的任务判断；报告引用式与 v6 不同的原因仍待确认。

### B.1 更正后的公式核对：Eq. (30)、Eq. (34) 与 Fig. 2 一致

**更正说明：** v4 曾将 Eq. (30) 的根号范围误读为 $\sqrt{\lambda_S^{\max}}/2$，据此错误地报告了与 Eq. (34) 的内部矛盾。对最终投稿稿 PDF 放大检查后，Eq. (30) 实际写的是 $\sqrt{\lambda_S^{\max}/2}$。因此，最终稿内部不存在此前所称的因子 $\sqrt{2}$ 不一致；v4 的相关判断应撤回。

**稿件事实（v6，正文印刷页码 p. 11–13，Eqs. (28)–(30)、(34)）：**

\[
V(S)=-\mu_S^2|S|^2+\lambda_S|S|^4,\qquad
m_s^2=2\lambda_S v_s^2,\qquad
v_s=\frac{m_{A'}}{2g_X}.
\]

Eq. (30) 给出

\[
\lambda_S=\frac{2g_X^2m_s^2}{m_{A'}^2},\qquad
 g_X<\sqrt{\frac{\lambda_S^{\max}}{2}}\,\frac{m_{A'}}{m_s}.
\tag{30}
\]

从 $\lambda_S\leq\lambda_S^{\max}$ 直接推导：

\[
\frac{2g_X^2m_s^2}{m_{A'}^2}\leq\lambda_S^{\max}
\quad\Longrightarrow\quad
 g_X\leq\sqrt{\frac{\lambda_S^{\max}}{2}}\,\frac{m_{A'}}{m_s}.
\]

这与 Eq. (30) 相符。将 $m_{A'}=2g_Xv_s$ 代入，也得到

\[
 m_s\leq\sqrt{2\lambda_S^{\max}}\,v_s,
\tag{34}
\]

与最终稿 Eq. (34) 一致。严格边界处可用 $\leq$；正文使用 $<$ 只反映排除边界的记号约定，不改变这里的因子关系。

**与 Fig. 2 的交叉核对：** 对 $m_s\geq10\,\mathrm{GeV}$、$\lambda_S^{\max}=4\pi$，有

\[
 v_s\geq\frac{10\,\mathrm{GeV}}{\sqrt{8\pi}}\simeq1.995\,\mathrm{GeV}.
\]

因此，Fig. 2 中 $v_s=2\,\mathrm{GeV}$ 的线与 Eq. (34) 的标量微扰性边界一致。无需为解决所谓内部矛盾而修改最终稿 Eq. (30)、Eq. (34) 或 Fig. 2。

**与原始审稿报告的差异：** 审稿报告引用 $m_s^2<4\pi v_s^2$，而当前存档 v6 在 $\lambda_S^{\max}=4\pi$ 时给出 $m_s^2<8\pi v_s^2$。报告形式对应更严格的边界（等效于采用 $\lambda_S^{\max}=2\pi$），并非当前 v6 Eq. (30)/(34) 的写法。确切历史原因不再追查；按项目决策，将其记录为报告-v6 的表达差异，不断言当前 v6 内部矛盾，也不归咎于审稿人。

**后续处理建议：** 保留当前存档稿 v6 公式。回复时简洁展示从 $m_s^2=2\lambda_Sv_s^2$ 与 $m_{A'}=2g_Xv_s$ 推出的关系，并说明当前 v6 的 Eq. (30) 与 Eq. (34) 内部一致；不再追查实际送审 PDF，也不要声称需要修正当前 v6 的内部矛盾。


### B.2 参考文献编号：以最终稿为准

μ 子对撞机部分的相关文献编号必须按稿件版本记录：

- 原始审稿报告的 Minor Point 5 写的是 Ref. 83。
- v3 文档此前记录的 arXiv v1 对应编号是 Ref. [62]。
- 最终投稿稿 `axial_vector_model_building-v6.pdf` 中，Sec. IV 所述 “Gauged \(L_\mu-L_\tau\) at a muon collider” 为 **Ref. [85]**；v6 的 Ref. [83] 是关于 massive vectors 与 \(g-2\) 的另一篇文献。

这属于版本间编号变化。后续回复信应引用最终稿的 Ref. [85]，并只在需要解释版本沿革时附注 v1 的 Ref. [62] 与审稿报告中的 Ref. 83。不要再使用 v3 旧文中“当前没有证据支持 Ref. [85]”的说法。


### B.3 四项 Major Points 的最终稿状态

| 原始编号 | v6 中可确认的内容 | 当前判断 | 仍需处理的核心缺口 |
|---|---|---|---|
| Major 1：标量 \(S\) 的现象学 | Sec. II.C 已含 Eqs. (28)–(34)、Table II、标量低质量约束、中间质量区间搜索讨论、\(S\to A'A'\) 衰变与微扰性条件 | **部分处理** | Higgs portal/混合只以“可忽略”作为基准假设；未见其环图诱导贡献、\(m_s\simeq m_h\) 区域的定量分析；未系统研究 Higgs 工厂对 \(S\) 的探测。
| Major 2：EFT 参数范围与 UV 一致性 | Eqs. (20)–(27)、(35) 定义 benchmark；正文说明 Fig. 2 是完整 UV 参数空间中的条件性二维切片 | **部分处理** | 参数选择的部分动机已说明，但完整的可行区域分类和 UV-consistency overlay 仍不完整；Eq. (30)/(34) 本身一致，但审稿报告引用的边界形式需要按稿件版本核对。
| Major 3：中微子振荡与 PMNS | 场内容及荷分配见 Table I；正文没有提供完整的中微子质量矩阵或 PMNS 拟合 | **未解决** | 太阳中微子传播中的实验味分数不是模型自身的中微子质量生成机制。需扩展模型并检查新约束，或明确收窄本文主张。
| Major 4（总体）：约束是否完整 | Fig. 2 汇总若干 \(A'\) 限制；Table II 汇总轻标量限制；另有太阳中微子背景场分析 | **部分处理** | 仍需区分已纳入、被证明次要和未评估的限制；不能把 Table II 的标量限制当作 \(A'\) 恒星冷却限制。
| Major 4.1：中微子振荡 | 与 Major 3 同一结构性问题 | **未解决** | 必须在回复信中独立编号回应，不能因与 Major 3 重叠而省略。
| Major 4.2：动能混合 | Eq. (22)–(23) 说明简并 VLL 的相反新荷使一圈阈值贡献抵消，并在匹配尺度设定零动能混合 | **部分处理** | 有限混合角引起的剩余修正被忽略，但未给出 benchmark 数值或实验影响的定量比较。
| Major 4.3：有限 VLL 质量的残余矢量耦合 | Eq. (16) 给出 \(g_V=g_X\sin^2\theta_{\mu R}\)、\(g_A=-g_X\cos^2\theta_{\mu R}\)；Eq. (27) 采用混合角 benchmark | **部分处理** | 未系统比较对矢量耦合更敏感的实验限制；Eq. (27) 是采用的 benchmark，不应自动称为普适实验上限。
| Major 4.4：恒星冷却 | Table II 有标量 \(s\) 的恒星/紧致星限制 | **未充分处理** | 审稿人所问的 \(A'\) 恒星冷却/超新星限制需独立核查；不能用标量表格代替。

## 附录 C：原始审稿意见的 38 项完整覆盖索引

> **使用方式：** 表内“主文档落点”均指第 1–12 章的**已整合主题讨论**；不是指一章额外的补漏堆栈。此附录保证 38/38 项逐条可查，后续科研和回复信是否完成仍由证据与 v5.4 手册的验收条件决定。开篇优点评价共 5 项也在统计内；`CS-1–CS-8` 为条件性附加筛查，不属于 38 项原始审稿单元。

### C.1 全部 38 项（原始编号、当前落点和待做事项）

以下“原始报告位置”表示来源层级，而“审稿意见的实质含义”为中文归纳，**不是逐字翻译/英文原话**；核对英文表述请回到附录 A 与原始报告。

#### 总评／Merits（5项；主要供开篇致谢和整体定位）

| ID | 原始报告位置 | 审稿意见的实质含义（中文工作归纳） | 已有主文分析位置 | 文档/科研状态 | 必需下一步与结案证据 |
|---|---|---|---|---|---|
| **A-1** | 总评／优点（非独立技术质疑） | 报告开头：模型构造与纯轴矢 EFT 现象学的关系 | §1.1；§1.3；附录 A | 已识别 | 回复开头应承认 UV 模型与低能 EFT 之间需要说明的联系；最终措辞须与实际修订稿一致。 |
| **A-2** | 总评／优点（非独立技术质疑） | 报告开头：Major Points 必须实质回应 | §1.2–1.4；§7；§12.6 | 已识别 | 最终回复逐条回答，不用总体致谢替代技术回应。 |
| **A-3** | 总评／优点（非独立技术质疑） | 优点：模型构造清楚，组合已有模型成分 | §1.1；附录 A | 已识别 | 可以简短致谢；不要无文献依据地扩张为“唯一已知 UV completion”。 |
| **A-4** | 总评／优点（非独立技术质疑） | 优点：现象学动机总体合理但有待澄清 | §1.1；§1.3；附录 A | 已识别 | 将正文修改落点与实际结果对应。 |
| **A-5** | 总评／优点（非独立技术质疑） | 优点：对 model-building 社区有价值 | §1.1；§8；附录 A | 已识别 | 简短致谢即可，不能替代 Major/Minor 的逐条回应。 |

#### Major Point 1：不可退耦的标量 S（7项）

| ID | 原始报告位置 | 审稿意见的实质含义（中文工作归纳） | 已有主文分析位置 | 文档/科研状态 | 必需下一步与结案证据 |
|---|---|---|---|---|---|
| **B-1** | Major 1（总述） | Major 1 总述：S 不能任意退耦，UV 与 EFT 叙事存在缺口 | §2.1.1；附录 B.1 | 部分覆盖 | v6 的 Eq. (30)/(34) 内部一致；与审稿报告引用的边界不同，按项目决策将其作为报告-v6 表达差异记录，不追查实际送审版本。 |
| **B-2** | Major 1．1 | Major 1.1：S 是否应成为 UV 模型的可探测预测 | §2.1.2；§2.4；§6.5 | 部分覆盖 | 论文定位需由实际标量窗口与实验可探测性结果支持，不能只靠叙事判断。 |
| **B-3** | Major 1．2 | Major 1.2：给出含微扰性、m_A′/g_X 基准和 S 自身实验限制的 m_S 窗口 | §2.1.3；§2.6；§2.7；§3.2 | 待计算/文献核查 | 建立可复现的 benchmark、微扰性筛选和 S 约束登记表；区分理论可行域、实验允许域与未评估区。 |
| **B-4** | Major 1．3 | Major 1.3：Higgs portal 是否由 μ、τ 等圈图产生 | §2.1.4；§2.2 工作 A/D | 待独立复核 | 统一完整 UV 拉格朗日量、树级 portal 边界、阈值、反项、重整化与 EFT 匹配；不得把两份不同计算直接拼接。 |
| **B-5** | Major 1．3 | Major 1.3：m_S 接近 m_h 时混合是否增强，要求在允许范围内定量 | §2.2 工作 D；§2.6.6 | 待独立复核/重算 | 对近简并区研究完整复数二点函数、极点与可观测率；未完成前不宣称已有固定宽度排除带或全范围混合曲线。 |
| **B-6** | Major 1．3 | Major 1.3：Higgs 测量是否对 UV completion 施加强限制 | §2.2 工作 C/D；§2.6.6 | 待定量比较 | 评估适用的 Higgs 信号强度、h→ss、近简并区和其他标量搜索；比较后才能称“最强限制”。 |
| **B-7** | Major 1．3 | Major 1.3 结尾：若认为 S 约束可忽略，须给理由；审稿人对此存疑 | §2.1.4；§2.6.7；§2.7 | 未结案 | 不得直接采用“可忽略”模板；必须用质量窗口和适用约束支持，或明确收窄论文主张。 |

#### Major Point 2：EFT 扫描范围与 UV 一致性（3项）

| ID | 原始报告位置 | 审稿意见的实质含义（中文工作归纳） | 已有主文分析位置 | 文档/科研状态 | 必需下一步与结案证据 |
|---|---|---|---|---|---|
| **C-1** | Major 2 | Major 2：在一处说明可行 EFT 参数范围 | §3.1–3.2 工作 A/E | 部分覆盖 | 整合 m_A′、g_X、m_S、VLL 质量、混合角、微扰性和扫描范围，标注固定/扫描参数。 |
| **C-2** | Major 2 | Major 2：解释为何选择当前质量/耦合范围，范围外是否不允许 | §3.2 工作 A/E；§6.1 | 部分覆盖 | 明确“本文兴趣范围”与“理论/实验允许范围”的区别，分类范围外区域。 |
| **C-3** | Major 2 | Major 2：说明 UV 微扰性对 EFT 参数的限制 | §3.2 工作 B/E；§2.7；附录 B.1 | 部分覆盖 | 给出统一参数映射与判据，并判断多个约束是否能同时满足；不要只列符号不列判据。 |

#### Major Point 3：中微子与 PMNS（4项）

| ID | 原始报告位置 | 审稿意见的实质含义（中文工作归纳） | 已有主文分析位置 | 文档/科研状态 | 必需下一步与结案证据 |
|---|---|---|---|---|---|
| **D-1** | Major 3（背景） | Major 3 背景：左手中微子与 Weinberg 算符质量机制 | §4.1；§4.2；附录 A.3 | 已识别 | 准确说明 v6 没有提供完整中微子质量生成机制。 |
| **D-2** | Major 3．1 | Major 3.1：允许算符、Yukawa 对齐与 PMNS 非平凡混合 | §4.2 工作 E；§4.3 | 结构性分析已覆盖，科研问题未解决 | 显式给出共同分块矩阵和质量本征态论证；不要将其简化成所有约定下 PMNS 必然等于单位矩阵。 |
| **D-3** | Major 3．2 | Major 3.2：右手中微子的荷、vectorlike 组合与代际混合 | §4.2 工作 B/E | 部分覆盖 | 若扩展，需显式构造 m_D、M_R、M_ν 并检查异常；单独加 N_R 不自动解除残余 Z_2。 |
| **D-4** | Major 3（结论） | Major 3 结尾：提供简单方案、引用适用的已知方案，或明确一致性问题 | §4.2 工作 D/E；§4.3–4.5 | 待作者决策 | 必须选择并诚实执行“验证扩展模型”或“收窄本文主张”；σ 与 σ+3N_R 仅是候选，不是已验证解。 |

#### Major Point 4：约束完整性（5项）

| ID | 原始报告位置 | 审稿意见的实质含义（中文工作归纳） | 已有主文分析位置 | 文档/科研状态 | 必需下一步与结案证据 |
|---|---|---|---|---|---|
| **E-1** | Major 4（总述） | Major 4 总述：约束是否完整，特别是不可任意退耦的 S | §5.1；§5.8；§2.6–2.7 | 部分覆盖 | 建立按粒子/质量区间分类的约束登记表；将 S 与 A′ 的天体物理限制分开。 |
| **E-2** | Major 4．1 | Major 4.1：中微子振荡与 PMNS | §4.2 工作 E；§5.1 | 已识别但仍未结案 | 回复信须保留独立的 Major 4.1 编号，并交叉引用 Major 3 的同一组证据。 |
| **E-3** | Major 4．2 | Major 4.2：benchmark 下动能混合的定量估算与文献参数化 | §5.2；§5.7；§5.8 | 待独立复核/文献核查 | 取得适用的圈图参数化文献或自行推导，统一荷、阈值、匹配尺度和重整化条件后重算；当前两个候选数值均不是最终值。 |
| **E-4** | Major 4．3 | Major 4.3：有限 VLL 质量的残余矢量耦合是否受到更强实验限制 | §5.3；§6.2–6.4；§6.7 | 部分覆盖 | 关系式已给出；仍需按适用的矢量敏感实验逐项比较，且区分 benchmark 与实验上限。 |
| **E-5** | Major 4．4 | Major 4.4：恒星冷却限制是否相关，审稿人点名 2511.09619 | §5.4；§5.8 | 待文献核查 | 核对 A′ 的质量、电流结构、产生/俘获/逃逸条件；不能由 Table II 的 S 限制替代，也不能先验宣称适用或不适用。 |

#### Minor Points：可读性与现象学细项（13项）

| ID | 原始报告位置 | 审稿意见的实质含义（中文工作归纳） | 已有主文分析位置 | 文档/科研状态 | 必需下一步与结案证据 |
|---|---|---|---|---|---|
| **F-1** | Minor 1 | Minor 1：给出 m_A′、g_X 兴趣范围并定义 “light” | §6.1；§3.2 工作 E | 部分覆盖 | 首次出现处需有参照尺度；解释扫描上下限和选择动机。 |
| **F-2** | Minor 2 | Minor 2：Eq. (12) 的 pure-axial limit 是否对应 θ_μR→0 | §6.2；§5.3 | 关系式已给，正文闭环未完成 | 明确严格极限与有限 VLL benchmark 的差别，并核对 τ 扇区及符号约定。 |
| **F-3** | Minor 3 | Minor 3：VLL 质量下限→混合角→矢量耦合，与 Eq. (27) 比较 | §6.3；§6.7 | 部分覆盖 | 补直接搜索来源、衰变假设，并将实验质量下限与条件性质量矩阵推论分开。 |
| **F-4** | Minor 4 | Minor 4：Eq. (27) 的 “conservative benchmark” 是实验上限还是方便选值 | §6.4；§6.3 | 部分覆盖 | 核对 global fits、表示和置信水平；未证明“保守”时改用 “illustrative decoupling benchmark”。 |
| **F-5** | Minor 5 | Minor 5 前半：μ 子对撞机的动机、新颖性、极化/末态不对称 | §6.5；§6.8 | 部分覆盖 | 决定压缩为 outlook 还是补完整分析；若保留定量结论，需说明能量、亮度、背景、探测和系统误差。 |
| **F-6** | Minor 5 | Minor 5 中段：Higgs-factory 阶段测试 S | §6.5；§6.8；§2.6.6 | 已识别，定量工作待定 | 说明适用产生/衰变通道及前提；如不展开，明确列为 future work，不预设通道一定存在。 |
| **F-7** | Minor 5 | Minor 5 结尾：压缩为示例或开展完整独立研究 | §6.5；§6.8 | 待作者决策 | 最终稿的篇幅与预测强度须与实际计算深度一致。 |
| **F-8** | Minor 6．1 | Minor 6.1：“light” 缺少参考尺度 | §6.1；§6.6 | 部分覆盖 | 与 Minor 1 交叉引用，但在最终正文首次出现处仍需修改并核对。 |
| **F-9** | Minor 6．2 | Minor 6.2：“representative bounds” 是否指最强/部分/完整约束 | §6.6；§5.8 | 部分覆盖 | 明确 Table II 的范围和筛选标准，不称其为完整或总是最强的约束集合。 |
| **F-10** | Minor 6．3 | Minor 6.3：“intermediate scalar-mass region” 的定义、依据和所限参数 | §2.6；§6.6 | 部分覆盖 | 找出原句对应的具体实验约束，并明确限制 m_S、g_X 还是其他参数；无证据则删除或重写。 |
| **F-11** | Minor 6．4 | Minor 6.4：“point by point” 的 point 是什么 | §6.6；§3.2；附录 B.1 | 部分覆盖 | 在正文明确每个 (m_A′,g_X) 网格点如何映射 v_S 并检查 Eq. (34)。 |
| **F-12** | Minor 6．5 | Minor 6.5：“parameter region of interest” 未定义 | §6.6；§3.2 工作 E | 部分覆盖 | 给出可复现的质量、耦合、衰变/寿命和 benchmark 条件。 |
| **F-13** | Minor 6．6 | Minor 6.6：v_S=2 GeV 线、y_sμμ “becomes large” 与绘图意义 | §6.6；§2.1.1；附录 B.1 | 主文已有校正说明，仍需正文/图注回归检查 | 按 v6 归一化核对 y_sμμ=m_μ/v_S；该线对应特定 m_S、λ_S 条件下的标量自耦合微扰性边界，不是缪子 Yukawa 非微扰线。 |

#### Recommendation（1项）

| ID | 原始报告位置 | 审稿意见的实质含义（中文工作归纳） | 已有主文分析位置 | 文档/科研状态 | 必需下一步与结案证据 |
|---|---|---|---|---|---|
| **H-1** | Recommendation | Recommendation：PMNS 一致性是关键问题，且不能忽略 S 的 UV 预言 | §1.2；§2.1–2.7；§4.2；§7 | 优先级已覆盖，核心问题未结案 | 最终回复必须正面处理 PMNS 与 S；不能仅以 Minor 文案或总体感谢结案。 |


### C.2 条件性筛查与证据边界

条件性 `CS-1–CS-8` 全部在 §5.8；`CS-8 (g−2)_μ` 是合并版 A10 的额外完整性核查，并非审稿人单列项。正式回复必须保留 Major/Minor/Recommendation 原编号；内部 38 项仅帮助避免把一段多项诉求合并遗漏。