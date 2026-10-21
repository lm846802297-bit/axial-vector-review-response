# dw13678_report_1_a.md：审稿意见总结、补充工作计划与逐点回复方案

> **合并说明：** 本版已将《审稿意见修改计划：四项补充内容》并入主文档，插入位置如下——补充三（中间标量质量区域）并入第二章末，见 §2.6；补充四（动能混合）并入第五章末，见 §5.7；补充二（VLL 约束传递链）并入第六章末，见 §6.7；补充一（μ 子对撞机）并入第六章末，见 §6.8；四项补充的优先级与验收清单见第十一章。原有章节编号与公式引用（Eq. (12)、Eq. (27)、Eq. (34) 等）保持不变。文中所有数值结果、实验排除区间与理论结论均须在完成计算或查证后填写，不预先假定结论。

## 一、审稿意见总体总结

### 1.1 核心问题

根据此前整理的审稿意见，当前需要重点处理四类主要问题：

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

**建议顺序：先解决模型理论结构，再补充定量计算和约束，最后统一修改正文及回复信。**

---

## 二、主要意见一：补充标量扇区的现象学分析

### 2.1 审稿意见的核心

论文可能没有充分讨论额外标量带来的现象学影响。需要进一步澄清：

- 额外标量的质量范围如何确定；
- 标量与标准模型 Higgs 是否存在混合；
- Higgs portal 耦合是否允许或需要考虑；
- 是否存在环图诱导的标量混合或其他有效相互作用；
- 当额外标量质量接近标准模型 Higgs 质量时，现有近似是否仍然有效；
- 这些因素是否会改变论文展示的允许参数空间。

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

**对应审稿意见：Major Point 1.2；Minor Point 1；Minor Point 6.3。**

#### 2.6.1 审稿人真正关心的问题

审稿人要求说明标量的允许质量范围，并指出如果某个低质量区域受到很强的实验限制，应明确给出相关限制，再讨论剩余允许区域。

审稿人还指出，论文中“intermediate scalar-mass region cannot simply be assumed unconstrained”这句话不够清楚：所谓“中间质量”具体指什么？作者是在报告某项实际约束，还是只是在提醒读者不能忽略约束？

因此，本项工作不能仅仅把“intermediate”换成另一个形容词，而需要给出明确的质量区间、适用约束及其结论。

**对当前稿件可先作出的具体澄清：** 此处最自然的“中间质量区”是 B 工厂直接搜索所覆盖的约 $0.04$–$6.5$–$7$ GeV 区间；文稿还提及四轻子共振搜索可延伸至约 $9$–$10$ GeV，但其公布诠释采用自旋一媒介子假设。因而原句不能被写成“该区已普遍排除”，正确含义应为：该质量段存在需要按标量产生机制、接受度与 $S\to A'A'$ 等分支比重铸的搜索，不能自动视为无约束。该结论应同时说明它限制的是包含耦合与分支比假设的参数组合，而非单独、普适的 $m_S$ 或 $g_X$ 上限。

#### 2.6.2 具体执行步骤

**任务 A：定义质量区间**

1. 以标量质量 \(m_S\) 为主变量，结合相关实验搜索的适用范围，将研究区域分段。
2. 分段边界应来自实际的物理阈值、实验搜索覆盖范围、衰变模式变化或约束强度变化，而不是随意指定。
3. 对每个区间，注明主要衰变模式和影响实验可见度的关键参数。
4. 如果某个区间没有明确的物理分界，应直接使用数值范围描述，而不要继续使用含糊的“低质量”“中间质量”或“高质量”。
5. 将 B 工厂标量搜索的约 $0.04$–$7$ GeV 覆盖单列，并把约 $9$–$10$ GeV 的自旋一四轻子结果标为“需针对标量重铸”，不能直接作为本文的排除线。

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

## 三、主要意见二：解释 EFT 参数范围与 UV–EFT 一致性

### 3.1 审稿意见的核心

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

为每个参数建立表格：

| 参数 | 物理意义 | 扫描范围 | 选择依据 | 相关约束 |
|---|---|---|---|---|
| \(g_X\) | 新规范耦合 | [填写] | 微扰性、实验限制等 | [填写] |
| \(m_X\) | 新粒子质量 | [填写] | 模型适用范围 | [填写] |
| \(M_{\mathrm{VLL}}\) | VLL 质量 | [填写] | 模型假设与实验限制 | [填写] |
| \(\theta\) | 混合角 | [填写] | 理论关系与实验限制 | [填写] |
| \(c_i\) | EFT 系数 | [填写] | UV 匹配与有效理论条件 | [填写] |

表中的参数名称和具体范围必须根据论文实际模型修改，不能直接将示例当作论文的真实设定。

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
修订时应以这条关系为主线，说明 (M_E) 是匹配尺度、所保留的算符阶数及 (M_E) 相对于相关过程能标的层级。不要引入与本文没有对应定义的一般 (c_i) 扫描表，也不要把仍作为动力学自由度保留的 (A') 两参数模型笼统称为“EFT 失效”；更准确的说法是 UV 解耦/匹配近似或标量微扰性条件失效。

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

模型的荷分配和场内容是否能够产生符合实验观测的中微子质量和混合，需要给出明确论证。

这是一个潜在的理论一致性问题，不能只靠增加一段定性说明解决。

### 4.2 需要补充的工作

#### 先澄清当前模型能够与不能够说明什么

当前拉格朗日量未包含右手中微子、Weinberg 算符或其他中微子质量生成项，因此它本身尚未给出中微子质量机制；Sec. III F 使用太阳中微子振荡的实验 flavor fractions，不能替代对模型内 PMNS 的推导。

按 Table I 的荷分配 $Q(L_\mu)=+1$、$Q(L_\tau)=-1$、$Q(S)=+2$（以 $Q_\ell=1$ 归一化），维五 Weinberg 算符不是“每一代各自允许”：$ee$ 与 $\mu\tau$ 结构可允许，而 $\mu\mu$、$\tau\tau$ 结构需伴随 $S^{(*)}$ 插入。仅有当前的 $S$ 时，电子与 $\mu,\tau$ 扇区之间的混合仍不能自然产生。因此，在不引入额外带合适荷的新场或破缺结构的前提下，最小内容不能展示完整的观测 PMNS 矩阵。此处应先给出该结构性判断，再决定采用扩展模型或收窄论文主张；若引入右手中微子，还要重新核对规范与引力异常抵消。

**可直接写入的结构性证明：** 在仅有 $S$ 获得 VEV 的最小模型中，$Q(S)=2Q_\ell$ 使 $U_A(1)$ 自发破缺后保留残余 $Z_2$。电子扇区为偶，$\mu,\tau$ 及其 VLL 扇区为奇；因此所有规范不变算符都不能把 $e$ 与 $\mu,\tau$ 连接起来。等价地，对 $(L_iH)(L_jH)S^n(S^\dagger)^m$，$ee$、$\mu\tau$、$\mu\mu$、$\tau\tau$ 条目可由偶数荷补偿，而 $e\mu$、$e\tau$ 需要奇数荷补偿、对任意 $n,m$ 均无解。带电轻子矩阵也具有相同的 $\{e\}\oplus\{\mu,\tau\}$ 分块结构，故在这一最小场内容下
\[
\theta_{12}=\theta_{13}=0,
\]
与振荡数据不相容；$\theta_{23}$ 可以非零。这个论证比“矩阵可能对角”的定性表述更强，但其前提必须在正文中写清：没有其他奇荷标量或额外破缺 VEV。

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

需要确认论文是否完整处理了以下问题：

1. 中微子振荡与质量结构；
2. 额外 U(1) 规范玻色子与超荷之间的动能混合；
3. 有限质量 VLL 导致的残余矢量耦合；
4. 纯轴矢量近似的适用条件；
5. 恒星冷却等天体物理限制。

这些约束的适用性取决于具体模型参数，不能不加区分地套用。

### 5.2 动能混合

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

恒星冷却限制通常依赖粒子的质量、耦合强度、产生率及其在恒星环境中的传播行为。

需要逐项确认：

- 相关粒子能否在恒星内部产生；
- 粒子是否能够逃逸并携带能量；
- 所用约束适用于哪一质量和耦合区间；
- 约束依赖哪些天体物理假设；
- 是否存在适用性边界或理论不确定性。

不应把只适用于特定质量范围或特定耦合结构的界限，直接解释为对整个参数空间的排除。

**需与标量约束分开处理：** 当前文稿的 Table II 主要汇总轻标量 $s$ 的冷却与紧致星约束；审稿人 Major Point 4.4 所引 2511.09619 讨论的是亚 GeV $L_\mu-L_\tau$ **规范玻色子 $A'$** 的束流倾倒与超新星/冷却问题。因此需要独立检查 $A'$ 在超新星中的产生、俘获与逃逸区。常规矢量 $L_\mu-L_\tau$ 的结果不能在未核对轴矢量电流、纵向模、有限 $g_V$ 及动能混合贡献前直接套用；反之，也不能用 Table II 的标量限制代替这一检查。

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

## 六、次要意见及逐项处理建议

### 6.1 "Light"的定义与扫描范围

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
因此严格的纯轴矢量点要求 \(\theta_{\mu R}=0\)。但在有限 \(M_E\) 且保持 \(m_\mu\simeq\theta_{\mu L}\theta_{\mu R}M_E\neq0\) 的情形，\(\theta_{\mu R}\) 不能严格为零；本文所用的是 VLL 解耦下的近似纯轴极限。应把这一点直接写入正文和回复，以回应审稿人关于 finite-VLL correction 的核心疑问。

**英文回复模板：**

> We have clarified the conditions under which the pure axial-vector limit around Eq. (12) is obtained and stated the approximations involved. We have also discussed possible finite-mass corrections in Sec. [X].

### 6.3 VLL 质量下限、混合角限制与 Eq. (27)

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

### 6.4 "Conservative benchmark"的含义

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

- “intermediate scalar-mass region”应写成 B 工厂主要覆盖的约 $0.04$–$7$ GeV 标量质量段，并说明可见标量搜索需结合分支比重铸；约 $9$–$10$ GeV 的公开四轻子诠释不能不加修改地套用到标量。
- “point by point”应明确为“对每个 $(m_{A'},g_X)$ 网格点，以 $v_S=m_{A'}/(2g_X)$ 代入 Eq. (34) 检查微扰性条件”。
- “parameter region of interest”应改为满足本文所假定即时衰变、质量阈值和分支比的明确参数范围。
- Fig. 2 的 $v_S=2$ GeV 灰虚线是恒定 $v_S$ 的引导线；在 $m_S=10$ GeV、$\lambda_S\le4\pi$ benchmark 下，它对应 Eq. (34) 的标量自耦合微扰性边界。它不是 $y_{s\mu\mu}$ 的非微扰边界：按本文 $y_{s\mu\mu}=m_\mu/v_S$，该线上约为 $0.053$。因此应将“becomes large”分别量化为哪一个耦合变大，不能把这条线误说成缪子 Yukawa 失去微扰性。

**英文回复模板：**

> We have revised the relevant wording to make the definitions and criteria more precise. In particular, we now clarify the meanings of "representative bounds," "point by point," and the "parameter region of interest," and quantify the behavior discussed in Sec. [X].

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
2. 相关分析与审稿版本所称的相关文献相比，有什么新的内容？（提交前须核对修订稿中的实际编号；当前稿对应的 μ 子对撞机文献编号已变为 Ref. [85]。）
3. 论文只研究前后向不对称性（forward-backward asymmetry），是否遗漏了偏振不对称性及不同末态的其他不对称性？
4. 完整 UV 模型包含额外标量。未来轻子对撞机，特别是 Higgs 工厂阶段，是否能够探测这一标量？

**修改目标：** 使 μ 子对撞机部分不再只是额外的限制曲线，而是明确说明它如何检验纯轴矢量 EFT、UV 完成及其独有预测。

#### 6.8.2 具体执行步骤

**任务 A：核对审稿版本所称的相关文献，明确本文的增量**

1. 查阅当前修订稿中对应的 μ 子对撞机文献（提交前核实编号；当前稿为 Ref. [85]）的原文，提取其对撞机能量、积分亮度、信号过程、背景过程、参数假设和统计方法。
2. 将本文的设置逐项与该文献比较。
3. 列出真正新增的内容，例如不同的耦合极限、不同的参数空间、额外的可观测量或 UV 模型解释。
4. 如果本文没有实质性的新增计算，应缩短该部分，将其定位为现有结果在本模型中的应用，而不要声称提出了新的对撞机分析。

建议建立比较表：

| 比较维度 | 审稿版本所称的相关文献（当前稿中核对为 Ref. [85]） | 本文 | 需要采取的行动 |
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

对审稿人点名的 Higgs-factory 阶段，应单独说明候选信号的前提：$e^+e^-\to ZS$ 依赖 Higgs–$S$ 混合；$h\to SS$ 依赖三标量耦合与 $m_S<m_h/2$；其他产生道取决于模型允许的耦合。它们可作为待评估的互补路径，而不是在尚未完成 portal 匹配、分支比和背景分析前就宣称的发现前景。

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

## 八、逐点回复信的标准结构

每条回复建议包含五个部分。

### 8.1 引用审稿意见

完整引用审稿人的原文，保留原有编号。

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

**重要：** 只有实际完成相应修改后，才可以在回复信中使用 "we have revised""we have added" 或 "we have shown" 等表达。

---

## 九、最终提交前检查清单

### 理论结构

- [ ] 所有场的规范荷和额外 U(1) 荷已核对。
- [ ] 标量势包含所有允许且相关的项。
- [ ] 标量质量矩阵和混合角推导正确。
- [ ] 中微子质量矩阵与模型荷分配一致。
- [ ] 已写明仅有 $S$ 获得 VEV 时的残余 $Z_2$，并据此检验 $\theta_{12}$、$\theta_{13}$ 的结构性限制。
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
- [ ] B 工厂约 $0.04$–$7$ GeV 标量搜索与约 $9$–$10$ GeV 自旋一结果已按产生率和分支比的适用性区分。
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
