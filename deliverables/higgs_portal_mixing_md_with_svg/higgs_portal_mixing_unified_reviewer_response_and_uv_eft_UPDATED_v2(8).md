# Higgs portal 模型：审稿意见回应、单圈混合与 UV–EFT 计算统一工作文档

> **整理版本：** 2026-10-18。此次更新主要调整导航、标题层级和章节顺序，不将阶段性推导升级为最终物理结论；原计算细节尽量保留。

> **文档目的**：将 `higgs_portal_mixing_merged_guide.md`（审稿回复路线与分步推导草稿）和 `UV_EFT匹配阶段性结果汇总_第114节原始Dirac迹独立核验.md`（独立复核与持续计算记录）合并为一个可持续更新的主文档。最终交付不是孤立地得到某个 Wilson 系数，而是**以可复核的场论计算回答审稿人的三个核心问题**。
>
> **重要阅读规则**：两份原文的结论并非全部一致。为避免把“拟议的审稿回复”误当作“已证明的结果”，本合并稿保留两份原文的实质内容，并在前面建立统一的证据等级和工作顺序。凡是尚未由完整 UV 拉氏量、匹配计算、极点分析及实验数据共同支持的强结论，均视为待验证，不得直接作为论文定论。

## 阅读地图与使用规则

本文件是项目主文档，不是已完成的审稿回复。为兼顾可读性与计算可追溯性，正文分为四层：

1. **研究目标与结论状态**：先看三条审稿问题、结论状态表和统一计算原则。
2. **审稿回复路线**：第 1 部分保留原 guide 的模型说明、推导路线与回复草稿；其中尚未核验的数字和强结论仅作待审计材料。
3. **计算审计记录**：后续计算章节保留逐步推导、数值测试、符号核验和 UV–EFT 匹配记录。该部分按研究过程积累，个别历史小节标题或编号可能沿用原始记录，不代表其结论已最终成立。
4. **原论文核验与执行计划**：补充核验章节记录 arXiv:2608.27258 的模型输入、完整标量势与门户重整化缺口；最后的执行计划给出当前优先级和停止条件。

### 快速定位

- [三条审稿问题](#核心目标需要回答的三条审稿意见)
- [统一结论状态表](#统一的结论状态表优先于后文任何未经核验的强表述)
- [审稿回复路线与分步推导](#第一部分审稿回复路线与分步推导草稿来自-guide)
- [独立复核与 UV–EFT 计算记录](#第二部分独立复核uv–eft-匹配与持续计算记录来自计算汇总)
- [原论文模型输入与审稿问题定位](#第128节原始论文模型输入与审稿问题定位arxiv260827258)
- [完整标量势与 portal 重整化条件](#第129节完整标量势与-higgs-portal-重整化条件)
- [最终执行计划与交付标准](#第三部分合并后的执行计划与最终交付标准)

### 阅读与引用约定

- **“原文明确给出”**：指可在论文正文/公式中定位的信息。
- **“已独立复核”**：指有独立推导或计算记录支持，但仍须遵守相应小节列明的符号和适用范围。
- **“阶段性结果”**：计算已推进，但匹配、反项、算符约化或独立交叉检查仍未全部完成。
- **“待验证/待定”**：不得直接写进正式审稿回复作为事实。
- 合并时保留计算历史以便追溯；若历史记录与文首状态表冲突，先按状态表处理，并在相应章节中完成复核后再更新状态。

---

## 核心目标：需要回答的三条审稿意见

### 问题 A：辐射修正是否产生 \(s\)–\(h\) 混合，大小是多少？

需要区分树级门户参数、轻子低能有效理论中的泡图、重矢量类轻子等 UV 自由度的阈值贡献，以及反项/重整化条件。只计算轻子泡图，不能自动代表完整 UV 模型的物理混合预测。

### 问题 B：\(m_s\simeq m_h\) 时是否会共振增强并违反 LHC 限制？

非简并近似中的 \(\theta\sim\Pi_{sh}/(m_h^2-m_s^2)\) 在简并附近不再足够。必须分析完整的复数二点函数矩阵、极点与可观测量；不能仅凭“粒子有非零宽度”就断言共振区一定安全，也不能在没有参数扫描与实验约束的情况下声称“完全无需微调”。

### 问题 C：低能现象学中忽略 \(s\) 是否合理？

“质量大于某个基准值”本身不等于退耦证明。应针对具体可观测量比较保留/移除 \(s\) 的结果，并明确外部动量、质量、耦合和误差容限的适用范围。若模型参数关系导致耦合随质量变化，还需区分 Appelquist–Carazzone 意义下的退耦与模型内的非退耦行为。

## 统一的结论状态表（优先于后文任何未经核验的强表述）

| 事项 | 当前状态 | 允许使用的表述 | 不能直接宣称的结论 |
|---|---|---|---|
| 低能轻子泡图的 Dirac 迹与参数积分结构 | 已做独立复核，但须连同符号约定阅读 | 可作为低能 EFT 图的计算起点 | 不等于完整 UV 预测 |
| guide 中从 \(12\Delta\) 变为 \(6\Delta\) 的系数变化 | 未解决 | 必须由 UV 图、EFT 图、反项及匹配差值解释 | 不能称为“仅减去 UV 极点自然得到” |
| 在壳积分与虚部 | 必须保留完整参数积分；阈值上可能出现虚部 | 可报告完整积分和约定 | 不能把单一对数近似称为精确在壳结果 |
| 门户反项/阈值匹配 | 尚未完成完整核验 | 需给定重整化方案和边界条件后计算 | 不能把某个低能泡图直接认作最终物理混合 |
| 简并区有限宽度处理 | 尚无足够依据证明普适安全 | 从完整复数传播子矩阵与可观测信号分析 | 不能断言宽度自动消除所有实验限制 |
| LHC 限制与共振窗口 | 需用具体质量、衰变道、混合定义及最新数据复核 | 作为待完成的现象学检验 | 不能直接沿用 guide 中概括性的上限/数值作为定论 |
| 忽略 \(s\) 的低能近似 | 需按实际目标观测量定量检验 | 给出近似成立条件和误差 | 不能只由“\(m_s\gtrsim10\,\mathrm{GeV}\)”推出普遍有效 |
| “无需微调” | 未被当前计算证明 | 可作为待检验假设 | 不可作为既定结论写进回复信 |
| \(C_{HS}^{(D)}\) 导数 Wilson 系数 | 现有记录中仍属阶段性计算 | 作为匹配与算符基底核验的子任务 | 不能将候选反项系数冒充最终约化后的 Wilson 系数或混合角 |

## 统一计算原则

1. 固定原论文的 UV 拉氏量、场基底、质量本征态、混合矩阵、规范荷、顶点符号和自能定义。
2. 分开记录裸圈图、重整化自能、UV–EFT 匹配差、质量混合项与动量依赖的动能混合项。
3. 所有系数都必须标注约定、重整化方案和匹配尺度；任何系数变化都要展示其来源。
4. 在阈值以上保留正确的 \(i0\) 处方和虚部，不以实数粗略对数替代完整振幅。
5. 先完成解析推导与极限检查，再进行数值积分；数值结果必须可追溯到明确公式和输入参数。
6. 现象学结论必须从物理极点/振幅及适用的实验约束得出，而不是直接把自能除以质量差当作全参数空间的混合角。
7. 原文草稿中的英文审稿回复仅作为模板；待核心计算、实验依据和适用边界全部核实后再最终定稿。

---

## 第一部分：审稿回复路线与分步推导草稿（来自 guide）

> 本部分尽量保留 guide 的原有推导和回复文本。凡与第二部分的独立复核结论存在张力之处，以“统一结论状态表”和后续核验为准；本部分中的数值估算、实验上限和“无需微调”等强结论均需逐项复核。

> **编辑说明：** 原 guide 在此处的 Executive Summary 是一段未完成的句子，原文在“单圈诱导的无量纲混合比在允许参数空间内”处中断。为避免把不完整论证当作结论，本合并稿不沿用该段的断句结论；请以文首“统一的结论状态表”和第 127–129 节的核验结果为准。

### 导论：审稿人质疑的三条核心逻辑链拆解

审稿人在第 3 条意见中针对正文公式 (34) 上方的假设（“选取标量退耦基准 $m_s \gtrsim 10\text{ GeV}$ 并假设希格斯门户混合可以忽略”）提出了三个层层递进的场论与唯象学问题，要求作者逐一回应：

1. **圈图辐射产生混合的不可避免性（要求一：计算单圈混合大小）**：即使在树图拉氏量中人为将希格斯门户耦合 $\lambda_{HS}|H|^2|S|^2$ 设为零，由于标量 $S$ 与标准模型希格斯 $h$ 均与 $\mu, \tau$ 耦合，通过 $\mu, \tau$（及紫外区的矢量类重轻子 $E_{\mu,\tau}$）的单圈费曼图必然在辐射修正水平生成 $s$–$h$ 质量混合项 $\delta m_{sh}^2$。需要写出该混合随 $m_s$ 变化的解析函数与定量结果。
2. **简并共振放大与 LHC 希格斯实验限制（要求二：对比实验限制、共振区与微调分析）**：双标量系统的混合角满足 $\tan(2\theta_{sh}) = \frac{2\delta m_{sh}^2}{m_h^2 - m_s^2}$。审稿人担心当 $m_s \to m_h \approx 125\text{ GeV}$ 时，分母趋于零导致混合角发生共振增强，进而使紫外完备理论受到现有 LHC 希格斯精确测量的强烈限制。需要对比实验上限、给出共振区宽度及微调程度。
3. **低能有效理论中 $m_s$ 的“非退耦（Non-decoupling）”疑问（要求三：澄清非退耦概念与划定适用范围）**：审稿人在双括号中质疑，由于 $m_s$ 在形式上不能退耦（cannot formally decouple），在低能有效理论中忽略标量 $s$ 的传播子效应是否合理，需要证明运动学压低机制并明确划定该近似的适用边界。

下文将原 LaTeX 备忘录的框架与零跳步分步推导完全去重整合，依次完成前置准备与三大阶段的完整演算。

### 前置准备阶段：从模型规范荷表到费曼规则的完整建立（Step 0.1 – Step 0.5）

在开始计算圈图之前，先把正文的规范荷分配表（Table）与公式 (34) 之间的数学桥梁一步步搭建出来。

#### Step 0.1：检验 $U_A(1)_{L_\mu-L_\tau}$ 规范不变性与直接汤川项的禁止

根据正文给出的场表，模型各场在 $SU(2)_L \times U(1)_Y \times U_A(1)_{L_\mu-L_\tau}$ 下的量子数如表 1 所示：

| 场 (Field) | $SU(2)_L$ | $U(1)_Y$ | $U_A(1)_{L_\mu-L_\tau}$ | 物理角色与手征性质 |
| :--- | :---: | :---: | :---: | :--- |
| $L_\mu = (\nu_\mu, \mu_L)^T$ | $\mathbf{2}$ | $-1/2$ | $+Q_\ell$ | 第二代左手轻子二重态 |
| $\mu_R$ | $\mathbf{1}$ | $-1$ | $-Q_\ell$ | 第二代右手带电轻子单态 |
| $E_\mu (E_{\mu L}, E_{\mu R})$ | $\mathbf{1}$ | $-1$ | $+Q_\ell$ | 缪子扇区矢量类重轻子（Dirac 质量 $M_{E_\mu}$） |
| $L_\tau = (\nu_\tau, \tau_L)^T$ | $\mathbf{2}$ | $-1/2$ | $-Q_\ell$ | 第三代左手轻子二重态 |
| $\tau_R$ | $\mathbf{1}$ | $-1$ | $+Q_\ell$ | 第三代右手带电轻子单态 |
| $E_\tau (E_{\tau L}, E_{\tau R})$ | $\mathbf{1}$ | $-1$ | $-Q_\ell$ | 陶子扇区矢量类重轻子（Dirac 质量 $M_{E_\tau}$） |
| $H$ | $\mathbf{2}$ | $+1/2$ | $0$ | 标准模型希格斯二重态（真空期望值 $v \approx 246.22\text{ GeV}$） |
| $S$ | $\mathbf{1}$ | $0$ | $Q_S = 2Q_\ell$ | 暗扇区复标量单态（真空期望值 $v_s$） |

1. **为什么标准模型直接汤川耦合被禁止**：
   在标准模型中，缪子和陶子通过算符 $\bar{L}_\mu H \mu_R$ 和 $\bar{L}_\tau H \tau_R$ 获得质量。但在本模型的轴矢量规范群 $U_A(1)_{L_\mu-L_\tau}$ 下，检查这两个算符的总轴荷 $Q_A$：
   $$Q_A(\bar{L}_\mu H \mu_R) = -Q_A(L_\mu) + Q_A(H) + Q_A(\mu_R) = -Q_\ell + 0 + (-Q_\ell) = -2Q_\ell \neq 0$$
   $$Q_A(\bar{L}_\tau H \tau_R) = -Q_A(L_\tau) + Q_A(H) + Q_A(\tau_R) = -(-Q_\ell) + 0 + Q_\ell = +2Q_\ell \neq 0$$
   因此，在 $U_A(1)_{L_\mu-L_\tau}$ 对称性未破缺时，树图水平的直接汤川耦合 $\bar{L}_\ell H \ell_R$ 被严格禁止。

2. **如何通过矢量类重轻子 $E_{\mu,\tau}$ 和复标量 $S$ 构造规范不变的紫外拉氏量**：
   由于 $E_\mu$ 的轴荷为 $+Q_\ell$（与 $L_\mu$ 相同），而 $S$ 的轴荷为 $+2Q_\ell$，我们可以构造以下算符并逐一检验其轴荷：
   - $\bar{L}_\mu H E_{\mu R}$ 的轴荷：$-Q_\ell + 0 + Q_\ell = 0$（规范不变）；
   - $\bar{E}_{\mu L} S \mu_R$ 的轴荷：$-Q_\ell + 2Q_\ell + (-Q_\ell) = 0$（规范不变）；
   - $\bar{E}_{\mu L} E_{\mu R}$ 的轴荷：$-Q_\ell + Q_\ell = 0$（允许裸 Dirac 质量项 $M_{E_\mu}$）；
   - $\bar{L}_\tau H E_{\tau R}$ 的轴荷：$+Q_\ell + 0 + (-Q_\ell) = 0$（规范不变）；
   - $\bar{E}_{\tau L} S^* \tau_R$ 的轴荷：$+Q_\ell + (-2Q_\ell) + Q_\ell = 0$（规范不变）；
   - $\bar{E}_{\tau L} E_{\tau R}$ 的轴荷：$+Q_\ell + (-Q_\ell) = 0$（允许裸 Dirac 质量项 $M_{E_\tau}$）。

   由此写出完整的、可重整化的紫外（UV）费米子质量与汤川相互作用拉氏量：
   $$-\mathcal{L}_{\text{UV}}^{\text{Yuk}} = y_{H\mu} \bar{L}_\mu H E_{\mu R} + y_{S\mu} \bar{E}_{\mu L} S \mu_R + M_{E_\mu} \bar{E}_{\mu L} E_{\mu R} + y_{H\tau} \bar{L}_\tau H E_{\tau R} + y_{S\tau} \bar{E}_{\tau L} S^* \tau_R + M_{E_\tau} \bar{E}_{\tau L} E_{\tau R} + \text{h.c.}$$

#### Step 0.2：积分掉重矢量类轻子 $E_{\mu,\tau}$ 导出 5 维有效算符

当重费米子质量远大于电弱与暗扇区破缺能标（$M_{E_\ell} \gg v, v_s$）时，在低能有效场论（EFT）中可以通过 $E_\ell$ 的经典运动方程将其积分掉（integrate out）。以 $\mu$ 扇区为例，对 $\bar{E}_{\mu L}$ 变分（忽略低能动量 $\not{p} \ll M_{E_\mu}$）：
$$\frac{\partial \mathcal{L}_{\text{UV}}}{\partial \bar{E}_{\mu L}} = 0 \implies M_{E_\mu} E_{\mu R} + y_{S\mu} S \mu_R = 0 \implies E_{\mu R} \simeq -\frac{y_{S\mu}}{M_{E_\mu}} S \mu_R$$
将该关系代回 $-\mathcal{L}_{\text{UV}}^{\text{Yuk}}$ 中的前两项（对 $\tau$ 扇区同理，其中 $E_{\tau R} \simeq -\frac{y_{S\tau}}{M_{E_\tau}} S^* \tau_R$）：
$$y_{H\mu} \bar{L}_\mu H E_{\mu R} + \left(y_{S\mu} \bar{E}_{\mu L} S \mu_R + M_{E_\mu} \bar{E}_{\mu L} E_{\mu R}\right) = y_{H\mu} \bar{L}_\mu H \left(-\frac{y_{S\mu}}{M_{E_\mu}} S \mu_R\right) + 0 = -\frac{y_{H\mu} y_{S\mu}}{M_{E_\mu}} (\bar{L}_\mu H \mu_R) S$$
（注：通过手征场相位重定义将有效威尔逊系数符号吸收为正。）于是得到 5 维有效汤川拉氏量：
$$-\mathcal{L}_{\text{eff}}^{(5)} = \frac{y_{H\mu} y_{S\mu}}{M_{E_\mu}} (\bar{L}_\mu H \mu_R) S + \frac{y_{H\tau} y_{S\tau}}{M_{E_\tau}} (\bar{L}_\tau H \tau_R) S^* + \text{h.c.}$$

#### Step 0.3：标量真空期望值展开与轴矢量规范玻色子质量 $m_{A'}$ 的导出

在幺正规范（Unitary Gauge）下，将标准模型希格斯二重态 $H$ 和暗扇区复标量单态 $S$ 围绕其真空期望值（VEV）$v \approx 246.22\text{ GeV}$ 和 $v_s$ 展开（其中 $S$ 的相位 Goldstone 分量已被规范玻色子 $A'$ 吸收）：
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ v + h(x) \end{pmatrix}, \qquad S = \frac{1}{\sqrt{2}} \big(v_s + s(x)\big)$$
考察复标量 $S$ 的规范协变动能项：
$$\mathcal{L}_{\text{kin}}^S = (D_\mu S)^* (D^\mu S), \qquad D_\mu S = \left(\partial_\mu - i g_X Q_S A'_\mu\right) S$$
将 $S = \frac{1}{\sqrt{2}}(v_s + s)$ 代入协变动能项：
$$\mathcal{L}_{\text{kin}}^S = \frac{1}{2} (\partial_\mu s)(\partial^\mu s) + \frac{1}{2} g_X^2 Q_S^2 (v_s + s)^2 A'_\mu A'^\mu = \frac{1}{2} (\partial_\mu s)^2 + \frac{1}{2} \left(g_X Q_S v_s\right)^2 A'_\mu A'^\mu + \dots$$
对比自旋为 1 的规范玻色子标准质量项 $\frac{1}{2} m_{A'}^2 A'_\mu A'^\mu$，并取正文的电荷归一化 $Q_\ell = 1 \implies Q_S = 2Q_\ell = 2$，立即得到：
$$m_{A'} = g_X Q_S v_s = 2 g_X v_s \implies v_s = \frac{m_{A'}}{2 g_X}$$
这就是正文公式 (34) 右侧关系式的完整推导。

#### Step 0.4：推导物理轻子质量 $m_\ell$ 与标量汤川耦合 $y_{h\ell\ell}, y_{s\ell\ell}$

将 $H = \frac{1}{\sqrt{2}}(0, v+h)^T$ 和 $S = \frac{1}{\sqrt{2}}(v_s + s)$ 代入 Step 0.2 的 5 维有效拉氏量 $-\mathcal{L}_{\text{eff}}^{(5)}$：
$$-\mathcal{L}_{\text{eff}}^{(5)} = \sum_{\ell=\mu,\tau} \frac{y_{H\ell} y_{S\ell}}{M_{E_\ell}} \left(\frac{v + h}{\sqrt{2}}\right) \left(\frac{v_s + s}{\sqrt{2}}\right) \bar{\ell}_L \ell_R + \text{h.c.} = \sum_{\ell=\mu,\tau} \left(\frac{y_{H\ell} y_{S\ell} v v_s}{2 M_{E_\ell}}\right) \left(1 + \frac{h}{v}\right)\left(1 + \frac{s}{v_s}\right) \bar{\ell}\ell$$
其中 $\bar{\ell}\ell = \bar{\ell}_L \ell_R + \bar{\ell}_R \ell_L$。将括号完全展开：
$$-\mathcal{L}_{\text{eff}}^{(5)} = \sum_{\ell=\mu,\tau} \underbrace{\left(\frac{y_{H\ell} y_{S\ell} v v_s}{2 M_{E_\ell}}\right)}_{=\, m_\ell} \left(1 + \frac{h}{v} + \frac{s}{v_s} + \frac{h s}{v v_s}\right) \bar{\ell}\ell$$
对比狄拉克费米子质量项 $-\mathcal{L}_{\text{mass}} = m_\ell \bar{\ell}\ell$，同时得到四个关键结果：
1. **带电轻子质量公式**：
   $$m_\ell = \frac{y_{H\ell} y_{S\ell} v v_s}{2 M_{E_\ell}} \qquad (\ell = \mu, \tau)$$
2. **希格斯 $h$ 与轻子的汤川耦合 $y_{h\ell\ell}$**（定义 $-\mathcal{L} \supset y_{h\ell\ell} h \bar{\ell}\ell$）：
   $$y_{h\ell\ell} = \frac{m_\ell}{v}$$
3. **暗标量 $s$ 与轻子的汤川耦合 $y_{s\ell\ell}$**（定义 $-\mathcal{L} \supset y_{s\ell\ell} s \bar{\ell}\ell$，并代入 Step 0.3 的 $v_s = \frac{m_{A'}}{2g_X}$）：
   $$y_{s\ell\ell} = \frac{m_\ell}{v_s} = \frac{2 g_X m_\ell}{m_{A'}}$$
   这严格证明了正文中指出的性质——$y_{s\mu\mu} = 2g_X m_\mu / m_{A'}$ 完全由轴矢量扇区参数 $(g_X, m_{A'})$ 决定，**与标量质量 $m_s$ 无关**。
4. **双标量-双费米子接触相互作用项（Contact term）**：
   $$-\mathcal{L}_{\text{contact}} = \sum_{\ell=\mu,\tau} \frac{m_\ell}{v v_s} h s \bar{\ell}\ell$$

#### Step 0.5：标量势展开、树图质量矩阵与公式 (34) 微扰论上限的导出

写出包含 $H$ 和 $S$ 的最一般规范不变可重整化标量势：
$$V(H, S) = -\mu_H^2 (H^\dagger H) + \lambda_H (H^\dagger H)^2 - \mu_S^2 (S^* S) + \lambda_S (S^* S)^2 + \lambda_{HS} (H^\dagger H)(S^* S)$$
代入 $H = \frac{1}{\sqrt{2}}(0, v+h)^T$ 和 $S = \frac{1}{\sqrt{2}}(v_s+s)$：
$$V(h, s) = -\frac{1}{2}\mu_H^2 (v+h)^2 + \frac{1}{4}\lambda_H (v+h)^4 - \frac{1}{2}\mu_S^2 (v_s+s)^2 + \frac{1}{4}\lambda_S (v_s+s)^4 + \frac{1}{4}\lambda_{HS}(v+h)^2(v_s+s)^2$$
1. **真空极小值条件（Tadpole conditions）**：
   $$\left.\frac{\partial V}{\partial h}\right|_{h=s=0} = v\left(-\mu_H^2 + \lambda_H v^2 + \frac{1}{2}\lambda_{HS} v_s^2\right) = 0 \implies \mu_H^2 = \lambda_H v^2 + \frac{1}{2}\lambda_{HS} v_s^2$$
   $$\left.\frac{\partial V}{\partial s}\right|_{h=s=0} = v_s\left(-\mu_S^2 + \lambda_S v_s^2 + \frac{1}{2}\lambda_{HS} v^2\right) = 0 \implies \mu_S^2 = \lambda_S v_s^2 + \frac{1}{2}\lambda_{HS} v^2$$
2. **树图质量平方矩阵 $\mathcal{M}_{\text{tree}}^2$**：
   计算二阶导数 $\left(\mathcal{M}_{\text{tree}}^2\right)_{ij} = \left.\frac{\partial^2 V}{\partial \phi_i \partial \phi_j}\right|_{h=s=0}$（其中 $\phi = (h, s)^T$），并代入上面的 $\mu_H^2, \mu_S^2$：
   $$\left(\mathcal{M}_{\text{tree}}^2\right)_{hh} = -\mu_H^2 + 3\lambda_H v^2 + \frac{1}{2}\lambda_{HS} v_s^2 = 2\lambda_H v^2$$
   $$\left(\mathcal{M}_{\text{tree}}^2\right)_{ss} = -\mu_S^2 + 3\lambda_S v_s^2 + \frac{1}{2}\lambda_{HS} v^2 = 2\lambda_S v_s^2$$
   $$\left(\mathcal{M}_{\text{tree}}^2\right)_{hs} = \left(\mathcal{M}_{\text{tree}}^2\right)_{sh} = \lambda_{HS} v v_s$$
   因此树图质量平方矩阵为：
   $$\mathcal{M}_{\text{tree}}^2 = \begin{pmatrix} 2\lambda_H v^2 & \lambda_{HS} v v_s \\ \lambda_{HS} v v_s & 2\lambda_S v_s^2 \end{pmatrix}$$
3. **导出正文公式 (34)**：
   在小混合下，暗标量的物理质量满足 $m_s^2 \simeq 2\lambda_S v_s^2 \implies m_s = \sqrt{2\lambda_S}\, v_s$。为了保证标量自相互作用满足微扰幺正性（Perturbative Unitarity），四次耦合必须满足 $\lambda_S < \lambda_S^{\max}$（通常取 $\lambda_S^{\max} = \pi$ 或 $4\pi$），从而得到正文公式 (34)：
   $$m_s < \sqrt{2\lambda_S^{\max}}\, v_s, \qquad v_s = \frac{m_{A'}}{2g_X}$$

### 第一阶段（对应审稿要求一）：一步步计算单圈 $s$–$h$ 混合大小（Step 1.1 – Step 1.8）

> **审稿人要求一**：写出通过 $\mu$、$\tau$ 圈图诱导出的 $S$-$h$ 混合矩阵元（或混合角 $\sin\theta$）随 $m_S$ 变化的解析估算式或数值曲线。

下面给出从费曼规则到重整化单圈非对角自能 $\Pi_{sh}(p^2)$ 的零跳步推导。

#### Step 1.1：写出单圈费米子气泡图的费曼积分

考虑外动量为 $p^\mu$、左侧外腿为实标量 $s$、右侧外腿为标准模型希格斯 $h$、圈内传播子为第 $\ell$ 代带电轻子（$\ell = \mu, \tau$）的单圈自能图 $-i\Pi_{sh}^{(\ell)}(p^2)$。
根据量子场论费曼规则：
- **费米子闭圈因子**：$-1$（来自费米子反对易关系）；
- **颜色因子**：轻子为 $SU(3)_c$ 单态，故 $N_c = 1$；
- **$s\bar{\ell}\ell$ 顶点**：$-i y_{s\ell\ell}$；
- **$h\bar{\ell}\ell$ 顶点**：$-i y_{h\ell\ell}$；
- **两条费米子传播子**（动量分别为 $k$ 和 $k+p$）：
  $$S_F(k) = \frac{i(\not{k} + m_\ell)}{k^2 - m_\ell^2 + i\epsilon}, \qquad S_F(k+p) = \frac{i(\not{k} + \not{p} + m_\ell)}{(k+p)^2 - m_\ell^2 + i\epsilon}$$

将这些因子组合并沿费米子圈求狄拉克迹（Trace），在 $d = 4 - 2\epsilon$ 维下引入重整化能标 $\mu^{2\epsilon}$：
$$-i \Pi_{sh}^{(\ell)}(p^2) = (-1) \mu^{2\epsilon} \int \frac{d^d k}{(2\pi)^d} \, \text{Tr}\left[ (-i y_{s\ell\ell}) \frac{i(\not{k} + m_\ell)}{k^2 - m_\ell^2 + i\epsilon} (-i y_{h\ell\ell}) \frac{i(\not{k} + \not{p} + m_\ell)}{(k+p)^2 - m_\ell^2 + i\epsilon} \right]$$

整理前面的虚数单位 $i$ 和正负号：
- 两个顶点和两个传播子给出 $(-i)^2 \cdot (i)^2 = (-1)\cdot(-1) = +1$；
- 连同费米子圈的 $(-1)$，右边整体符号为 $- y_{s\ell\ell} y_{h\ell\ell}$；
- 两边同除以 $-i$（注意 $\frac{-1}{-i} = -i$），得到：
$$\Pi_{sh}^{(\ell)}(p^2) = -i \, y_{s\ell\ell}\, y_{h\ell\ell} \, \mu^{2\epsilon} \int \frac{d^d k}{(2\pi)^d} \frac{\text{Tr}\big[(\not{k} + m_\ell)(\not{k} + \not{p} + m_\ell)\big]}{(k^2 - m_\ell^2 + i\epsilon)\big[(k+p)^2 - m_\ell^2 + i\epsilon\big]}$$

#### Step 1.2：逐步计算狄拉克 $\gamma$ 矩阵的迹

展开分子中的矩阵乘积：
$$(\not{k} + m_\ell)(\not{k} + \not{p} + m_\ell) = \not{k}(\not{k} + \not{p}) + m_\ell \not{k} + m_\ell(\not{k} + \not{p}) + m_\ell^2 \mathbf{1}_{4\times 4}$$
利用狄拉克 $\gamma$ 矩阵的求迹恒等式：
- $\text{Tr}[\mathbf{1}_{4\times 4}] = 4$；
- 奇数个 $\gamma$ 矩阵的迹恒为零：$\text{Tr}[\not{k}] = 0$，$\text{Tr}[\not{k} + \not{p}] = 0$；
- 两个 $\gamma$ 矩阵的迹：$\text{Tr}[\gamma^\mu \gamma^\nu] = 4 g^{\mu\nu} \implies \text{Tr}[\not{k}(\not{k} + \not{p})] = k_\mu (k+p)_\nu \text{Tr}[\gamma^\mu \gamma^\nu] = 4(k^2 + k\cdot p)$。

因此分子求迹结果为：
$$\text{Tr}\big[(\not{k} + m_\ell)(\not{k} + \not{p} + m_\ell)\big] = 4 \left( k^2 + k\cdot p + m_\ell^2 \right)$$

#### Step 1.3：费曼参数化（Feynman Parameterization）与圈动量平移

利用标准费曼参数公式合并分母：
$$\frac{1}{A B} = \int_0^1 dx \, \frac{1}{\big[x B + (1-x) A\big]^2}$$
令 $A = k^2 - m_\ell^2 + i\epsilon$，$B = (k+p)^2 - m_\ell^2 + i\epsilon$，计算分母线性组合：
$$x B + (1-x) A = x(k^2 + 2 k\cdot p + p^2 - m_\ell^2) + (1-x)(k^2 - m_\ell^2) + i\epsilon = k^2 + 2 x k\cdot p + x p^2 - m_\ell^2 + i\epsilon$$
对圈动量 $k$ 配方：定义平移后的圈动量 $q \equiv k + x p$（故 $k = q - x p$，且积分测度不变 $d^d k = d^d q$）：
$$k^2 + 2 x k\cdot p + x p^2 - m_\ell^2 = (q - x p)^2 + 2 x (q - x p)\cdot p + x p^2 - m_\ell^2 = q^2 - x^2 p^2 + x p^2 - m_\ell^2 = q^2 - \Delta + i\epsilon$$
其中定义了有效质量平方函数：
$$\Delta(x, p^2) \equiv m_\ell^2 - x(1-x) p^2$$

接下来，将分子中的 $k^2 + k\cdot p + m_\ell^2$ 用 $k = q - x p$ 代入展开：
$$\begin{aligned}
k^2 + k\cdot p + m_\ell^2 &= (q - x p)^2 + (q - x p)\cdot p + m_\ell^2 \\
&= q^2 - 2 x (q\cdot p) + x^2 p^2 + q\cdot p - x p^2 + m_\ell^2 \\
&= q^2 + (1 - 2x)(q\cdot p) + \big[ m_\ell^2 - x(1-x) p^2 \big]
\end{aligned}$$
由于分母 $(q^2 - \Delta + i\epsilon)^2$ 是关于 $q^\mu$ 的偶函数，积分对称性保证线性奇次项 $\int d^d q \, \frac{q\cdot p}{(q^2 - \Delta)^2} = 0$ 严格消失。因此分子简化为：
$$k^2 + k\cdot p + m_\ell^2 \;\longrightarrow\; q^2 + m_\ell^2 - x(1-x) p^2 = q^2 + \Delta$$

于是自能积分化为：
$$\Pi_{sh}^{(\ell)}(p^2) = -4 i \, y_{s\ell\ell}\, y_{h\ell\ell} \int_0^1 dx \, \mu^{2\epsilon} \int \frac{d^d q}{(2\pi)^d} \frac{q^2 + \Delta}{\left(q^2 - \Delta + i\epsilon\right)^2}$$

#### Step 1.4：威克转动（Wick Rotation）与维数正规化圈积分求值

对时间分量作威克转动至欧氏空间（Euclidean space）：
$$q^0 = i q_E^0 \implies q^2 = (q^0)^2 - \vec{q}^2 = -(q_E^0)^2 - \vec{q}_E^2 = -q_E^2, \qquad d^d q = i \, d^d q_E$$
代入积分式（注意 $(-4i) \cdot i = +4$，且分母 $(q^2 - \Delta)^2 = (-q_E^2 - \Delta)^2 = (q_E^2 + \Delta)^2$，分子 $q^2 + \Delta = -q_E^2 + \Delta$）：
$$\Pi_{sh}^{(\ell)}(p^2) = 4 \, y_{s\ell\ell}\, y_{h\ell\ell} \int_0^1 dx \, \mu^{2\epsilon} \int \frac{d^d q_E}{(2\pi)^d} \frac{-q_E^2 + \Delta}{\left(q_E^2 + \Delta\right)^2}$$

现在写出 $d = 4 - 2\epsilon$ 维欧氏空间中的两个标准维数正规化主积分公式：
1. **标量主积分 $I_0(\Delta)$**：
   $$I_0(\Delta) \equiv \mu^{2\epsilon} \int \frac{d^d q_E}{(2\pi)^d} \frac{1}{\left(q_E^2 + \Delta\right)^2} = \frac{1}{(4\pi)^{2-\epsilon}} \Gamma(\epsilon) \left(\frac{\mu^2}{\Delta}\right)^\epsilon = \frac{1}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} \right) + \mathcal{O}(\epsilon)$$
   其中定义了 $\overline{\text{MS}}$ 极点 $\frac{1}{\tilde{\epsilon}} \equiv \frac{1}{\epsilon} - \gamma_E + \ln(4\pi)$，$\mu_R$ 为 $\overline{\text{MS}}$ 重整化能标。
2. **分子含 $q_E^2$ 的主积分 $I_2(\Delta)$**：
   $$I_2(\Delta) \equiv \mu^{2\epsilon} \int \frac{d^d q_E}{(2\pi)^d} \frac{q_E^2}{\left(q_E^2 + \Delta\right)^2} = \frac{d}{2} \frac{1}{(4\pi)^{2-\epsilon}} \Gamma(\epsilon - 1) \Delta \left(\frac{\mu^2}{\Delta}\right)^\epsilon$$
   利用 $\Gamma(\epsilon - 1) = -\frac{\Gamma(\epsilon)}{1 - \epsilon} = -\Gamma(\epsilon)(1 + \epsilon + \dots)$ 以及 $\frac{d}{2} = 2 - \epsilon$：
   $$\frac{d}{2} \Gamma(\epsilon - 1) = -(2 - \epsilon)(1 + \epsilon)\Gamma(\epsilon) = -(2 + \epsilon)\Gamma(\epsilon) + \mathcal{O}(\epsilon^2)$$
   因此：
   $$I_2(\Delta) = -\frac{2\Delta}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} + \frac{1}{2} \right) + \mathcal{O}(\epsilon)$$

将 $I_2(\Delta)$ 和 $I_0(\Delta)$ 代入分子组合 $-I_2(\Delta) + \Delta I_0(\Delta)$：
$$\begin{aligned}
-I_2(\Delta) + \Delta I_0(\Delta) &= \frac{2\Delta}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} + \frac{1}{2} \right) + \frac{\Delta}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} \right) \\
&= \frac{3\Delta}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} + \frac{1}{3} \right)
\end{aligned}$$
再乘上前面的系数 $4 \, y_{s\ell\ell}\, y_{h\ell\ell}$，并代回 $\Delta = m_\ell^2 - x(1-x)p^2$（在实标量归一化下对应动能混合系数 $\int_0^1 dx\, 6x(1-x) = 1$）：
$$\Pi_{sh}^{(\ell)}(p^2) = \frac{y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} \int_0^1 dx \, \Big[ 12 m_\ell^2 - 12 x(1-x) p^2 \Big] \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{m_\ell^2 - x(1-x)p^2 - i\epsilon}{\mu_R^2} + \frac{1}{3} \right)$$

#### Step 1.5：紫外完备理论匹配（UV Matching）与树图抵消项的作用

现在回答审稿人最关心的场论自洽性问题：**既然上式含有紫外发散 $\frac{1}{\tilde{\epsilon}}$，作者假设“Higgs-portal 混合可忽略”在重整化场论中的严格定义是什么？**

1. **紫外完整理论（含重费米子 $E_\ell$，质量 $M_{E_\ell}$）中的截断机制**：
   在完整标量势 $V(H,S) \supset \lambda_{HS} (H^\dagger H)(S^* S)$ 中，树图非对角质量平方元为 $\left(\mathcal{M}_{\text{tree}}^2\right)_{sh} = \lambda_{HS} v v_s$。
   在能标 $\mu > M_{E_\ell}$ 的紫外完备理论中，轻子与重矢量类轻子通过 Step 0.1 的拉氏量耦合：$H$ 连接 $\bar{L}_\ell E_{\ell R}$（耦合 $y_{H\ell}$），$S$ 连接 $\bar{E}_{\ell L}\ell_R$（耦合 $y_{S\ell}$）。单圈图连接外腿 $s$ 与 $h$ 时，圈内上方传播子是重费米子 $E_\ell$（质量 $M_{E_\ell}$），下方传播子是轻子 $\ell$（质量 $m_\ell$）。
   根据可重整化量子场论的标准程序，裸参数 $\lambda_{HS}^0 = \lambda_{HS}(\mu_R) + \delta\lambda_{HS}$ 中的抵消项 $\delta\lambda_{HS}$ 严格吸收高动量区 $k \gtrsim M_{E_\ell}$ 的紫外发散，而低能有效理论的紫外对数截断能标自然固定在重费米子质量阈值 $\mu_R = M_{E_\ell}$。

2. **施加重整化条件（Renormalization Condition）**：
   当正文声明“假设希格斯门户混合可忽略（assume negligible Higgs-portal mixing）”时，其严格的场论含义是：**在紫外匹配能标 $\mu_R = M_{E_\ell}$ 处施加重整化条件 $\lambda_{HS}(\mu_R = M_{E_\ell}) = 0$，随后检验从 $\mu_R = M_{E_\ell}$ 演化到电弱能标 $\mu_R \sim m_h, m_s$ 时，由 $\tau, \mu$ 圈图辐射产生的有限重整化混合 $\delta m_{sh}^2(p^2)$ 是否真的足够小**：
   $$\delta m_{sh}^2(p^2) = \sum_{\ell=\mu,\tau} \frac{y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} \int_0^1 dx \, \Big[ 6 m_\ell^2 - 6 x(1-x) p^2 \Big] \ln\left(\frac{M_{E_\ell}^2}{m_\ell^2 - x(1-x)p^2 - i\epsilon}\right)$$

#### Step 1.6：分离出“静态手征质量项”与“在壳动量项”

利用积分公式 $\int_0^1 dx \, 1 = 1$ 和 $\int_0^1 dx \, 6 x(1-x) = 6 \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = 1$，并代入 Step 0.4 的汤川耦合乘积：
$$y_{s\ell\ell}\, y_{h\ell\ell} = \left(\frac{m_\ell}{v_s}\right) \left(\frac{m_\ell}{v}\right) = \frac{m_\ell^2}{v \, v_s}$$
我们将单圈诱导的 $s$–$h$ 混合拆分为两个物理层次的贡献：

1. **动量无关的静态手征质量混合项（$p^2 = 0$）**：
   $$\delta m_{sh}^2\big|_{p^2=0} = \sum_{\ell=\mu,\tau} \frac{6 \, y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} m_\ell^2 \ln\left(\frac{M_{E_\ell}^2}{m_\ell^2}\right) = \sum_{\ell=\mu,\tau} \frac{3}{8\pi^2} \frac{m_\ell^4}{v \, v_s} \ln\left(\frac{M_{E_\ell}^2}{m_\ell^2}\right)$$
   注意这里出现了 **$m_\ell^4$ 的四次方手征压低**。

2. **在壳动量项 / 波函数混合诱导项（$p^2 = m_h^2$ 或 $m_s^2$）**：
   当我们在希格斯质量壳 $p^2 = m_h^2 \gg m_\tau^2$ 处评估自能（这是产生最大可能混合的保守上限估计）时，被积函数中的 $-6x(1-x)p^2$ 积分给出 $-m_h^2$：
   $$\left|\delta m_{sh}^2(p^2 = m_h^2)\right| \simeq \sum_{\ell=\mu,\tau} \frac{y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} m_h^2 \ln\left(\frac{M_{E_\ell}^2}{m_h^2}\right) = \sum_{\ell=\mu,\tau} \frac{1}{16\pi^2} \frac{m_\ell^2}{v \, v_s} m_h^2 \ln\left(\frac{M_{E_\ell}^2}{m_h^2}\right)$$

#### Step 1.7：逐步代入物理常数计算 $\mu$ 圈与 $\tau$ 圈的具体数值

代入粒子物理标准常数（PDG 数值）：
- 缪子质量：$m_\mu = 0.10566\text{ GeV}$
- 陶子质量：$m_\tau = 1.77686\text{ GeV}$
- 电弱真空期望值：$v = (\sqrt{2} G_F)^{-1/2} = 246.22\text{ GeV}$
- 希格斯玻色子质量：$m_h = 125.25\text{ GeV} \implies m_h^2 = 15687.6\text{ GeV}^2$
- 单圈相空间因子：$16\pi^2 = 157.9137$

1. **比较 $\mu$ 圈与 $\tau$ 圈的相对大小**：
   $$\frac{\Pi_{sh}^{(\mu)}}{\Pi_{sh}^{(\tau)}} \simeq \left(\frac{m_\mu}{m_\tau}\right)^2 = \left(\frac{0.10566}{1.77686}\right)^2 = (0.05946)^2 = 3.536 \times 10^{-3}$$
   若按静态质量项 $m_\ell^4$ 比较，则 $\mu$ 圈与 $\tau$ 圈之比更是只有 $(m_\mu/m_\tau)^4 = 1.25 \times 10^{-5}$。因此，**$\tau$ 圈贡献了超过 $99.6\%$ 的混合效应**，$\mu$ 圈在定量上完全可以忽略。

2. **计算无量纲混合比 $\frac{|\delta m_{sh}^2|}{m_h^2}$ 的前置系数**：
   - 对于**在壳动量项**（保守最大估计）：
     $$\frac{1}{16\pi^2} \frac{m_\tau^2}{v \, v_s} = \frac{1}{157.9137} \times \frac{(1.77686\text{ GeV})^2}{246.22\text{ GeV} \times v_s} = \frac{3.15723\text{ GeV}^2}{38881.5\text{ GeV} \times v_s} = \frac{8.120 \times 10^{-5}\text{ GeV}}{v_s}$$
     设重矢量类轻子质量为典型能标 $M_{E_\tau} = 1\text{ TeV} = 1000\text{ GeV}$，则对数因子为：
     $$\ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) = 2 \ln\left(\frac{1000}{125.25}\right) = 2 \times 2.0774 = 4.155$$
     相乘得到在壳动量项的无量纲混合比：
     $$\frac{\left|\delta m_{sh}^2(m_h^2)\right|}{m_h^2} \approx \frac{3.37 \times 10^{-4}\text{ GeV}}{v_s} \left(\frac{\ln(M_{E_\tau}^2/m_h^2)}{4.155}\right)$$

   - 对于**静态手征质量项（$p^2 = 0$）**：
     $$\frac{6}{16\pi^2} \frac{m_\tau^4}{v \, v_s \, m_h^2} = 6 \times \left(\frac{8.120 \times 10^{-5}\text{ GeV}}{v_s}\right) \times \frac{(1.77686)^2}{(125.25)^2} = \frac{9.81 \times 10^{-8}\text{ GeV}}{v_s}$$
     乘以对数因子 $\ln(M_{E_\tau}^2/m_\tau^2) = 2\ln(1000/1.77686) = 12.66$，得到：
     $$\frac{\left|\delta m_{sh}^2(0)\right|}{m_h^2} \approx \frac{1.24 \times 10^{-6}\text{ GeV}}{v_s} \left(\frac{\ln(M_{E_\tau}^2/m_\tau^2)}{12.66}\right)$$

#### Step 1.8：结合公式 (34) 写出混合角 $\sin\theta_{sh}(m_s)$ 随 $m_s$ 变化的解析函数与数值表

根据正文公式 (34) 的微扰论条件：
$$m_s < \sqrt{2\lambda_S^{\max}}\, v_s \implies v_s > v_s^{\min}(m_s) \equiv \frac{m_s}{\sqrt{2\lambda_S^{\max}}}$$
把 $v_s > \frac{m_s}{\sqrt{2\lambda_S^{\max}}}$ 代入 Step 1.7 的公式，立即得到**在任意给定标量质量 $m_s$ 下，微扰论所允许的最大单圈诱导混合元**：
$$\left(\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2}\right)_{\max} = \frac{\sqrt{2\lambda_S^{\max}}}{16\pi^2} \frac{m_\tau^2}{v \, m_s} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx 8.46 \times 10^{-5} \left(\frac{10\text{ GeV}}{m_s}\right) \sqrt{\frac{\lambda_S^{\max}}{\pi}}$$

进而，双标量混合角 $\theta_{sh}$ 随 $m_s$ 变化的**显式解析上限函数**为：
$$\left|\sin\theta_{sh}(m_s)\right|_{\max} \simeq \left|\frac{\delta m_{sh}^2(m_h^2)}{m_h^2 - m_s^2}\right|_{\max} = \frac{\sqrt{2\lambda_S^{\max}}}{16\pi^2} \frac{m_\tau^2}{v \, m_s} \frac{m_h^2}{|m_h^2 - m_s^2|} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right)$$

**物理洞察（公式 34 的反相关保护机制 Anti-Correlation Protection）**：
观察上式中的因子 $\frac{1}{m_s |m_h^2 - m_s^2|}$：
- **在轻质量端（$m_s = 10\text{ GeV}$）**：虽然 $v_s$ 可以较小（$v_s^{\min} \approx 2.0\text{--}4.0\text{ GeV}$，$y_{s\tau\tau}$ 相对较大），但质量平方差 $|m_h^2 - m_s^2| \approx m_h^2$ 处于最大，因此混合角被大质量分母压低至 $|\sin\theta_{sh}| \lesssim 10^{-4}$；
- **在希格斯简并区（$m_s \to m_h = 125.25\text{ GeV}$）**：为了使 $m_s$ 能够达到 $125\text{ GeV}$ 而不破坏公式 (34) 的微扰论要求，**$v_s$ 必须同步成比例增大至 $25\text{--}50\text{ GeV}$ 以上**（取 $\lambda_S^{\max}=\pi$ 时 $v_s^{\min} \approx 49.97\text{ GeV}$；取 $\lambda_S^{\max}=4\pi$ 时 $v_s^{\min} \approx 24.98\text{ GeV}$），从而自动把汤川耦合压低至 $y_{s\tau\tau} = m_\tau/v_s \lesssim 0.035\text{--}0.071$，使圈图混合元在 $m_s \approx m_h$ 处反而进一步减小至 $(0.68\text{--}1.35)\times 10^{-5}$！

表 2 汇总了跨越 $m_s \in [10, 500]\text{ GeV}$ 全区间的逐点精确计算值与 LHC 实验上限对比（取 $\lambda_S^{\max} = \pi$，$M_{E_\tau} = 1\text{ TeV}$）：

| $m_s$ [GeV] | 最小允许 $v_s^{\min}$ [GeV] | 最大耦合 $y_{s\tau\tau}^{\max}$ | $\frac{\vert\delta m_{sh}^2(m_h^2)\vert}{m_h^2}$ (动量项) | $\frac{\vert\delta m_{sh}^2(0)\vert}{m_h^2}$ (静态项) | 最大混合角 $\vert\sin\theta_{sh}\vert$ (动量项) | 最大混合角 $\vert\sin\theta_{sh}\vert$ (静态项) | LHC 实验上限 $\vert\sin\theta_{\text{exp}}\vert$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **10** | $3.99$ | $0.445$ | $8.46 \times 10^{-5}$ | $3.11 \times 10^{-7}$ | $8.51 \times 10^{-5}$ | $3.13 \times 10^{-7}$ | $\lesssim 0.10\text{--}0.25$ |
| **20** | $7.98$ | $0.223$ | $4.23 \times 10^{-5}$ | $1.55 \times 10^{-7}$ | $4.34 \times 10^{-5}$ | $1.59 \times 10^{-7}$ | $\lesssim 0.10\text{--}0.25$ |
| **30** | $11.97$ | $0.148$ | $2.82 \times 10^{-5}$ | $1.04 \times 10^{-7}$ | $2.99 \times 10^{-5}$ | $1.10 \times 10^{-7}$ | $\lesssim 0.10\text{--}0.25$ |
| **40** | $15.96$ | $0.111$ | $2.11 \times 10^{-5}$ | $7.77 \times 10^{-8}$ | $2.35 \times 10^{-5}$ | $8.65 \times 10^{-8}$ | $\lesssim 0.10\text{--}0.25$ |
| **60** | $23.94$ | $0.074$ | $1.41 \times 10^{-5}$ | $5.18 \times 10^{-8}$ | $1.83 \times 10^{-5}$ | $6.72 \times 10^{-8}$ | $\lesssim 0.10\text{--}0.25$ |
| **80** | $31.92$ | $0.056$ | $1.06 \times 10^{-5}$ | $3.89 \times 10^{-8}$ | $1.79 \times 10^{-5}$ | $6.57 \times 10^{-8}$ | $\lesssim 0.15\text{--}0.30$ |
| **100** | $39.90$ | $0.045$ | $8.46 \times 10^{-6}$ | $3.11 \times 10^{-8}$ | $2.34 \times 10^{-5}$ | $8.59 \times 10^{-8}$ | $\lesssim 0.15\text{--}0.30$ |
| **120** | $47.87$ | $0.037$ | $7.05 \times 10^{-6}$ | $2.59 \times 10^{-8}$ | $8.62 \times 10^{-5}$ | $3.17 \times 10^{-7}$ | $\lesssim 0.15\text{--}0.30$ |
| **130** | $51.86$ | $0.034$ | $6.51 \times 10^{-6}$ | $2.39 \times 10^{-8}$ | $8.37 \times 10^{-5}$ | $3.08 \times 10^{-7}$ | $\lesssim 0.15\text{--}0.30$ |
| **150** | $59.84$ | $0.030$ | $5.64 \times 10^{-6}$ | $2.07 \times 10^{-8}$ | $1.30 \times 10^{-5}$ | $4.77 \times 10^{-8}$ | $\lesssim 0.15\text{--}0.30$ |
| **200** | $79.79$ | $0.022$ | $4.23 \times 10^{-6}$ | $1.55 \times 10^{-8}$ | $2.73 \times 10^{-6}$ | $1.00 \times 10^{-8}$ | $\lesssim 0.15\text{--}0.30$ |
| **500** | $199.47$ | $0.0089$ | $1.69 \times 10^{-6}$ | $6.22 \times 10^{-9}$ | $1.13 \times 10^{-7}$ | $4.16 \times 10^{-10}$ | $\lesssim 0.20\text{--}0.30$ |

### 第二阶段（对应审稿要求二）：一步步对比希格斯实验限制、共振区与微调分析（Step 2.1 – Step 2.5）

> **审稿人要求二**：在你们讨论的 $m_S$ 质量区间内，检查当前 LHC 对希格斯信号强度（Higgs signal strength）和标量混合角 $\sin\theta$ 的实验上限；如果在 $m_S \approx m_h$ 附近确实被排除，需要在参数空间图上挖掉（标出排除区）这一共振区域，或者说明需要多大程度的抵消项（counterterm）微调。

#### Step 2.1：全面梳理当前 LHC 对标量混合的三大实验限制

在 $m_s \gtrsim 10\text{ GeV}$ 的质量范围内，LHC 实验通过以下三条途径限制 $s$–$h$ 混合：

1. **希格斯信号强度全局拟合（Higgs Signal Strength Global Fit, 适用于所有 $m_s$）**：
   当物理希格斯态为 $h_{\text{phys}} = \cos\theta_{sh}\, h - \sin\theta_{sh}\, s$ 时，由于暗标量 $s$ 不与标准模型胶子、夸克和弱规范玻色子 $W/Z$ 直接耦合，125 GeV 希格斯在 LHC 上的产生截面与标准模型衰变宽度统一乘以 $\cos^2\theta_{sh}$。因此全局信号强度修改因子为：
   $$\mu_{\text{global}} = \cos^2\theta_{sh} = 1 - \sin^2\theta_{sh}$$
   根据 ATLAS 与 CMS Run 2 联合测量结果（$\mu = 1.05 \pm 0.06$），在 $95\%$ 置信水平（CL）下要求：
   $$\sin^2\theta_{sh} \lesssim 0.10 \implies \left|\sin\theta_{sh}\right|_{\text{exp}}^{\text{signal}} \lesssim 0.31$$
   即使采用重标量直接搜寻与高亮度 HL-LHC 的最严格预期值，实验灵敏度上限也在：
   $$\left|\sin\theta_{sh}\right|_{\text{exp}} \simeq 0.10\text{--}0.25$$

2. **希格斯奇异衰变 $h \to ss$（适用于轻质量区 $10\text{ GeV} \le m_s < m_h / 2 = 62.6\text{ GeV}$）**：
   当 $m_s < 62.6\text{ GeV}$ 时，125 GeV 希格斯可以实过程衰变为一对暗标量 $h \to ss$（随后 $s \to \tau^+\tau^-$ 或 $\mu^+\mu^-$）。当前 LHC 对未观测到的 BSM 希格斯分支比上限为 $\text{BR}(h \to \text{BSM}) < 0.12$（对特定专属道 $h \to ss \to 4\tau / 2\tau 2\mu$ 上限约为 $10^{-3}\text{--}10^{-4}$）。
   下面一步步计算**单圈 $\tau$ 圈图诱导的 $hss$ 三标量顶点 $g_{hss}^{\text{loop}}$ 及其分支比**：
   - 包含一个 $h\bar{\tau}\tau$ 顶点（耦合 $y_{h\tau\tau} = m_\tau/v$）和两个 $s\bar{\tau}\tau$ 顶点（耦合 $y_{s\tau\tau} = m_\tau/v_s$）的单圈三角形费米子图，由于需要奇数次手征质量翻转以保证狄拉克迹非零，其振幅正比于 $m_\tau y_{h\tau\tau} y_{s\tau\tau}^2$：
     $$g_{hss}^{\text{loop}} \simeq \frac{3 \, y_{h\tau\tau}\, y_{s\tau\tau}^2}{4\pi^2} m_\tau \ln\left(\frac{M_{E_\tau}^2}{m_\tau^2}\right) = \frac{3 m_\tau^4}{4\pi^2 v \, v_s^2} \ln\left(\frac{M_{E_\tau}^2}{m_\tau^2}\right)$$
   - 代入数值：$m_\tau^4 = (1.77686)^4 = 9.968\text{ GeV}^4$，$4\pi^2 v = 39.478 \times 246.22 = 9720.4\text{ GeV}$，$\ln(M_{E_\tau}^2/m_\tau^2) \approx 12.66$：
     $$g_{hss}^{\text{loop}} \approx \frac{3 \times 9.968 \times 12.66}{9720.4 \times v_s^2}\text{ GeV}^3 = \frac{0.0389\text{ GeV}^3}{v_s^2}$$
   - 取最极端的轻质量端 $m_s = 10\text{ GeV}$，由公式 (34) 知 $v_s^{\min} \approx 4.0\text{ GeV}$（即便取 $\lambda_S^{\max} = 4\pi$ 也有 $v_s^{\min} \approx 2.0\text{ GeV}$）。代入 $v_s = 4.0\text{ GeV}$ 得：
     $$g_{hss}^{\text{loop}} \le \frac{0.0389}{16.0}\text{ GeV} = 2.43 \times 10^{-3}\text{ GeV}$$
   - 计算 $h \to ss$ 的部分衰变宽度：
     $$\Gamma(h \to ss) = \frac{\left|g_{hss}^{\text{loop}}\right|^2}{32\pi m_h} \sqrt{1 - \frac{4 m_s^2}{m_h^2}} \le \frac{(2.43 \times 10^{-3})^2}{32\pi \times 125.25} \times 0.987 = 4.6 \times 10^{-10}\text{ GeV}$$
   - 除以标准模型希格斯总宽度 $\Gamma_h^{\text{SM}} = 4.1\times 10^{-3}\text{ GeV}$，得到单圈诱导分支比：
     $$\text{BR}(h \to ss)_{\text{loop}} = \frac{\Gamma(h \to ss)}{\Gamma_h^{\text{SM}}} \le 1.1 \times 10^{-7} \ll \text{BR}_{\text{exp}} \sim 10^{-4}\text{--}10^{-1}$$
     结论：**在 $10\text{ GeV} \le m_s < m_h/2$ 区间内，单圈诱导的 $h \to ss$ 衰变比实验上限小 $3\text{--}6$ 个数量级，完全可忽略。**

#### Step 2.2：逐步求解简并共振区（$m_s \to m_h$）的排除窗口宽度 $\Delta m_s$

双标量精确对角化公式为：
$$\tan(2\theta_{sh}) = \frac{2 \delta m_{sh}^2}{m_h^2 - m_s^2}$$
当混合角达到实验灵敏度阈值 $\theta_{\text{exp}}$（取严苛标准 $\sin\theta_{\text{exp}} = 0.10 \implies \tan(2\theta_{\text{exp}}) \approx 2\sin\theta_{\text{exp}} = 0.20$）时，对应的标量质量 $m_s$ 与 $m_h$ 的距离 $\Delta m_s \equiv |m_s - m_h|$ 满足：
$$\left|m_h^2 - m_s^2\right| = (m_h + m_s)|m_h - m_s| \simeq 2 m_h \Delta m_s \le \frac{2 \left|\delta m_{sh}^2\right|}{\tan(2\theta_{\text{exp}})} \simeq \frac{\left|\delta m_{sh}^2\right|}{\sin\theta_{\text{exp}}}$$
两边同除以 $2 m_h$，得到共振排除窗口的半宽度公式：
$$\Delta m_s = \left|m_s - m_h\right| \le \frac{m_h}{2 \sin\theta_{\text{exp}}} \left(\frac{\left|\delta m_{sh}^2\right|}{m_h^2}\right)$$

代入 $m_s = m_h = 125.25\text{ GeV}$ 处的单圈混合数值：
1. **第一步**：由公式 (34)，在 $m_s = 125.25\text{ GeV}$ 处：
   - 若取 $\lambda_S^{\max} = \pi$，则 $v_s > \frac{125.25}{\sqrt{2\pi}} = 49.97\text{ GeV}$，此时：
     $$\left.\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2}\right|_{\lambda_S^{\max}=\pi} = \frac{3.37 \times 10^{-4}\text{ GeV}}{49.97\text{ GeV}} = 6.75 \times 10^{-6}$$
   - 若取最极端的幺正性上限 $\lambda_S^{\max} = 4\pi$，则 $v_s > \frac{125.25}{\sqrt{8\pi}} = 24.98\text{ GeV}$，此时：
     $$\left.\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2}\right|_{\lambda_S^{\max}=4\pi} = \frac{3.37 \times 10^{-4}\text{ GeV}}{24.98\text{ GeV}} = 1.35 \times 10^{-5}$$
2. **第二步**：代入 $\Delta m_s$ 公式（取 $\sin\theta_{\text{exp}} = 0.10$）：
   - 对 $\lambda_S^{\max} = \pi$（在壳动量项）：
     $$\Delta m_s \le \frac{125.25\text{ GeV}}{2 \times 0.10} \times (6.75 \times 10^{-6}) = 4.23 \times 10^{-3}\text{ GeV} = 4.23\text{ MeV}$$
   - 对 $\lambda_S^{\max} = 4\pi$（在壳动量项）：
     $$\Delta m_s \le \frac{125.25\text{ GeV}}{2 \times 0.10} \times (1.35 \times 10^{-5}) = 8.45 \times 10^{-3}\text{ GeV} = 8.45\text{ MeV}$$
   - 若采用静态手征质量项 $\frac{|\delta m_{sh}^2(0)|}{m_h^2} \le \frac{1.24 \times 10^{-6}}{24.98} = 4.96 \times 10^{-8}$（或对 $\lambda_S^{\max}=\pi$ 为 $2.48 \times 10^{-8}$）：
     $$\Delta m_s \le \frac{125.25\text{ GeV}}{2 \times 0.10} \times (4.96 \times 10^{-8}) = 3.1 \times 10^{-5}\text{ GeV} = 31\text{ keV}$$

#### Step 2.3：计入有限衰变宽度（Finite-Width Regularization）证明共振奇点自动消除

当两粒子质量差 $|m_s - m_h| \lesssim 4\text{--}8\text{ MeV}$ 时，不能再使用零宽度的实数质量矩阵，因为任何不稳定粒子在共振区的传播子分母都包含虚部 $-i m \Gamma$（Breit-Wigner 宽度）：
1. **标准模型希格斯总衰变宽度**：
   $$\Gamma_h \approx 4.1\text{ MeV} \implies m_h \Gamma_h \approx 125.25 \times 0.0041 = 0.514\text{ GeV}^2$$
2. **标量 $s$ 在 $m_s = 125.25\text{ GeV}$ 处的衰变宽度 $\Gamma_s$**：
   $s$ 主要衰变到 $\tau^+\tau^-$，树图部分宽度为：
   $$\Gamma(s \to \tau^+\tau^-) = \frac{y_{s\tau\tau}^2 m_s}{8\pi} \left(1 - \frac{4m_\tau^2}{m_s^2}\right)^{3/2} \simeq \frac{m_\tau^2 m_s}{8\pi v_s^2}$$
   在 $v_s = 25\text{--}50\text{ GeV}$ 处：
   $$\Gamma_s \approx \frac{3.157 \times 125.25}{25.13 \times v_s^2}\text{ GeV} = \frac{15.73\text{ GeV}^3}{v_s^2} \approx 6.3\text{--}25.2\text{ MeV}$$
   对应的虚部为 $m_s \Gamma_s \approx 0.79\text{--}3.15\text{ GeV}^2$。
3. **复传播子矩阵的有效混合角**：
   在包含宽度的非厄米有效哈密顿量中，有效混合角由复分母的模控制：
   $$\left|\theta_{sh}^{\text{eff}}\right| \simeq \frac{\left|\delta m_{sh}^2\right|}{\sqrt{\left(m_h^2 - m_s^2\right)^2 + \left(m_h \Gamma_h - m_s \Gamma_s\right)^2}}$$
   即使在**严格简并点 $m_s = m_h$**（实部 $m_h^2 - m_s^2 = 0$），分母也由宽度差 $|m_h \Gamma_h - m_s \Gamma_s| \gtrsim 0.28\text{--}2.64\text{ GeV}^2$ 托底，而分子 $|\delta m_{sh}^2| \le (0.68\text{--}1.35)\times 10^{-5} m_h^2 = 0.11\text{--}0.21\text{ GeV}^2$。
   因此，在 $m_s = m_h$ 处的最大有效混合角为：
   $$\left|\theta_{sh}^{\text{eff}}\right|_{m_s = m_h} \lesssim \frac{0.11\text{ GeV}^2}{0.28\text{ GeV}^2} \sim \mathcal{O}(0.1)$$
   （若按静态质量项 $|\delta m_{sh}^2(0)| \approx 8\times 10^{-4}\text{ GeV}^2$ 计算，则在 $m_s = m_h$ 处有效混合角仅为 $|\theta_{sh}^{\text{eff}}| \approx 3\times 10^{-3} \ll 0.1$。）

#### Step 2.4：定量计算抵消项微调程度（Counterterm Fine-Tuning Analysis）

审稿人提到：“如果存在强限制，需要说明多大程度的抵消项（counterterm）微调”。可以通过标准 Barbieri-Giudice 自然性/微调判据来定量回答：
1. **单圈对四次门户耦合 $\lambda_{HS}$ 的辐射修正大小 $\delta\lambda_{HS}^{\text{loop}}$**：
   由 $\delta m_{sh}^2 = \delta\lambda_{HS}^{\text{loop}} v v_s$，将 Step 1.6 的公式两边除以 $v v_s$：
   - 若按动量项计：
     $$\delta\lambda_{HS}^{\text{loop}} \sim \frac{1}{16\pi^2} \frac{m_\tau^2 m_h^2}{v^2 v_s^2} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx \frac{0.21\text{ GeV}^2}{(246.22\text{ GeV}) \times v_s} \approx 3.4 \times 10^{-5} \left(\frac{25\text{ GeV}}{v_s}\right)$$
   - 若按紫外理论中四费米子盒图（Box diagram，带两个 $h$ 腿和两个 $s$ 腿）计算对 $|H|^2|S|^2$ 算符的直接跑动：
     $$\delta\lambda_{HS}^{\text{box}} \sim \frac{y_{h\tau\tau}^2 y_{s\tau\tau}^2}{16\pi^2} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) = \frac{1}{16\pi^2} \frac{m_\tau^4}{v^2 v_s^2} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx \frac{4.3 \times 10^{-6}\text{ GeV}^2}{v_s^2} \lesssim 10^{-7}$$
2. **实验允许的最大树图门户耦合 $\lambda_{HS}^{\text{exp}}$**：
   要保持混合角 $|\sin\theta_{sh}| < \sin\theta_{\text{exp}} \approx 0.1$，实验允许的非对角元为 $|\lambda_{HS}^{\text{exp}} v v_s| < 0.1 |m_h^2 - m_s^2|$，即：
   $$\lambda_{HS}^{\text{exp}}(m_s) = \frac{0.1 \, |m_h^2 - m_s^2|}{v \, v_s}$$
3. **微调参数 $\Delta_{\text{FT}} \equiv \left|\frac{\delta\lambda_{HS}^{\text{loop}}}{\lambda_{HS}^{\text{exp}}}\right|$**：
   $$\Delta_{\text{FT}} = \left|\frac{\delta m_{sh,\text{loop}}^2}{0.1 (m_h^2 - m_s^2)}\right| = \frac{|\sin\theta_{sh}^{\text{loop}}|}{0.1}$$
   - 在非简并区（$|m_s - m_h| \gtrsim 1\text{ GeV}$）：$\Delta_{\text{FT}} \lesssim 10^{-3} \ll 1$，**完全不需要任何抵消项微调（No fine-tuning at all）**。
   - 即便在距离 $m_h$ 仅 $1\text{ MeV}$ 的极端简并点，若不计宽度效应而直接用树图抵消项抵消到 $|\sin\theta_{sh}| < 0.1$，所需的微调程度也仅为 $\Delta_{\text{FT}} \sim \frac{8.5\text{ MeV}}{1\text{ MeV}} \sim \mathcal{O}(1\text{--}10)$。

#### Step 2.5：关于参数空间图（Parameter Space Plot）的修改操作指南

既然已经算清共振窗口半宽度 $\Delta m_s = |m_s - m_h| \lesssim 8.5\text{ MeV}$，不需要重画任何参数空间图，原因如下：
- 在横轴跨度为几十到几百 GeV 的参数图上，$2\Delta m_s \lesssim 17\text{ MeV}$ 的宽度占整张图宽度的比例不到 $10^{-4}$（远小于 PDF 矢量图上一条最细实线宽度的 $1/100$）。
- 只需要在正文中公式 (34) 下方（或对应图注中）加上一句定量说明：**“除 $|m_s - m_h| \lesssim \mathcal{O}(10\text{ MeV})$ 的极窄简并切片外，单圈诱导混合在整个参数空间均比 LHC 希格斯测量上限低 $3\text{--}4$ 个数量级。”**

### 第三阶段（对应审稿要求三）：一步步证明低能理论中忽略 $s$ 的合理性与适用边界（Step 3.1 – Step 3.4）

> **审稿人要求三**：解释非退耦问题——补充一段简短讨论，说明为什么在你们关注的能标或截面计算中忽略 $S$ 的传播子/质量效应是一个合理的近似（或者明确划定该近似失效的能标范围）。

#### Step 3.1：剖析审稿人为什么说“$m_s$ 不能形式退耦（cannot formally decouple）”

在量子场论中，Appelquist-Carazzone 退耦定理指出：如果一个重粒子的质量 $M$ 来自不依赖于对称性破缺的裸质量项（如矢量类费米子质量 $M_E$），那么当固定所有无量纲耦合常数并取形式极限 $M \to \infty$ 时，该重粒子在低能有效理论中的所有物理效应以 $1/M^2$ 趋于零。

然而，对于本模型中的实标量 $s$：
1. $s$ 是自发破缺 $U_A(1)_{L_\mu-L_\tau}$ 的径向激发态（Radial Higgs mode），其质量完全来自真空期望值 $v_s$：
   $$m_s = \sqrt{2\lambda_S}\, v_s, \qquad v_s = \frac{m_{A'}}{2 g_X}$$
2. 当我们在研究轴矢量规范玻色子 $A'$ 的唯象学时，通常是**固定 $(g_X, m_{A'})$**（即固定了 $v_s$）。
3. 在 $v_s$ 固定的前提下：
   - 标量与轻子的汤川耦合 $y_{s\ell\ell} = \frac{m_\ell}{v_s} = \frac{2g_X m_\ell}{m_{A'}}$ 是一个**与 $m_s$ 无关的常数**；
   - 若想取“形式退耦极限 $m_s \to \infty$”，唯一的办法是令标量四次自耦合 $\lambda_S = \frac{m_s^2}{2v_s^2} \to \infty$，但这会直接破坏微扰幺正性（违反公式 34：$m_s < \sqrt{2\lambda_S^{\max}}\, v_s$）。
4. **核心回应逻辑**：审稿人所说的“$m_s$ 不能形式退耦”，其实**正是正文公式 (34) 上方已经明确指出的物理事实**（原文：*“It does not, however, remove the intrinsic correlation between $m_s$ and the axial sector: $y_{s\mu\mu} = 2g_X m_\mu / m_{A'}$ remains independent of $m_s$, while perturbativity requires $m_s < \sqrt{2\lambda_S^{\max}} v_s$”*）。
   正文中所说的“scalar-decoupling benchmark $m_s \gtrsim 10\text{ GeV}$”，**并不是指取形式极限 $m_s \to \infty$**，而是指：**在满足公式 (34) 微扰论上限的参数空间内（即 $v_s > m_s/\sqrt{2\lambda_S^{\max}}$），当研究低能过程（动量转移 $|q^2| \ll m_s^2$）时，标量 $s$ 传播子带来的振幅相对于轴矢量 $A'$ 的振幅受到强烈的运动学压低（Kinematic suppression），从而可以在定量上忽略。**

#### Step 3.2：逐步推导四费米子散射中 $s$ 交换与 $A'$ 交换的精确振幅比

比较任意两个带电轻子流 $\ell_1 \bar{\ell}_1 \to \ell_2 \bar{\ell}_2$（其中 $\ell_1, \ell_2 \in \{\mu, \tau\}$，动量转移为 $q$）中，树图交换标量 $s$ 与交换轴矢量玻色子 $A'$ 的振幅大小：

1. **树图交换标量 $s$ 的振幅 $\mathcal{M}_s(q^2)$**：
   顶点为 $-i y_{s\ell\ell} = -i \frac{m_\ell}{v_s}$，标量传播子为 $\frac{i}{q^2 - m_s^2}$：
   $$i\mathcal{M}_s = \left(-i \frac{m_{\ell_1}}{v_s} \bar{u}_1 u_1\right) \frac{i}{q^2 - m_s^2} \left(-i \frac{m_{\ell_2}}{v_s} \bar{u}_2 u_2\right) \implies \mathcal{M}_s(q^2) = -\frac{m_{\ell_1} m_{\ell_2}}{v_s^2 (q^2 - m_s^2)} (\bar{u}_1 u_1)(\bar{u}_2 u_2)$$
   在低能过程 $|q^2| \ll m_s^2$ 下：
   $$\left|\mathcal{M}_s\right| \simeq \frac{m_{\ell_1} m_{\ell_2}}{v_s^2 \, m_s^2} \left|(\bar{u}_1 u_1)(\bar{u}_2 u_2)\right|$$

2. **树图交换轴矢量规范玻色子 $A'$ 的振幅 $\mathcal{M}_{A'}(q^2)$**：
   轴矢量耦合顶点为 $-i g_X Q_\ell \gamma^\mu \gamma_5$（其中 $|Q_\ell| = 1$），幺正规范下大质量规范玻色子传播子为：
   $$D_{\mu\nu}^{A'}(q) = \frac{-i}{q^2 - m_{A'}^2} \left( g_{\mu\nu} - \frac{q_\mu q_\nu}{m_{A'}^2} \right)$$
   代入振幅表达式：
   $$\mathcal{M}_{A'}(q^2) = \frac{g_X^2 Q_{\ell_1} Q_{\ell_2}}{q^2 - m_{A'}^2} \left[ (\bar{u}_1 \gamma^\mu \gamma_5 u_1)(\bar{u}_2 \gamma_\mu \gamma_5 u_2) - \frac{1}{m_{A'}^2} (\bar{u}_1 \not{q} \gamma_5 u_1)(\bar{u}_2 \not{q} \gamma_5 u_2) \right]$$
   利用在壳费米子的狄拉克方程 $\bar{u}(p') \not{q} \gamma_5 u(p) = \bar{u}(p')(\not{p}' - \not{p})\gamma_5 u(p) = 2 m_\ell \bar{u}(p')\gamma_5 u(p)$，以及公式 (34) 的 $m_{A'} = 2 g_X v_s \implies \frac{g_X^2}{m_{A'}^2} = \frac{1}{4 v_s^2}$：
   - **横向轴矢量流部分（Transverse axial-vector piece）**：
     在低动量转移 $|q^2| \ll m_{A'}^2$ 时，系数为：
     $$\left|C_{A'}^{\text{trans}}\right| = \frac{g_X^2}{m_{A'}^2} = \frac{1}{4 v_s^2}$$
   - **纵向赝标量流部分（Longitudinal Goldstone piece, $\propto q_\mu q_\nu / m_{A'}^2$）**：
     系数为：
     $$\left|C_{A'}^{\text{long}}\right| = \frac{g_X^2}{|q^2 - m_{A'}^2|} \frac{4 m_{\ell_1} m_{\ell_2}}{m_{A'}^2} = \frac{m_{\ell_1} m_{\ell_2}}{v_s^2 \, |q^2 - m_{A'}^2|}$$

3. **计算标量 $s$ 交换振幅与轴矢量 $A'$ 交换振幅的无量纲比值**：
   - **相对于横向轴矢量振幅（主导散射截面与不对称性）**：
     在低能散射中，旋量流 $|\bar{u}\gamma^\mu\gamma_5 u| \sim \mathcal{O}(E) \ge m_\ell$，因此标量交换与轴矢量交换的振幅比上限为：
     $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}^{\text{trans}}}\right| \lesssim \frac{m_{\ell_1} m_{\ell_2} / (v_s^2 m_s^2)}{1 / (4 v_s^2)} = \frac{4 m_{\ell_1} m_{\ell_2}}{m_s^2}$$
     这里的 **$v_s^2$ 严格消掉**，比值只取决于轻子质量与标量质量之比：
     - 对于**纯缪子过程（$\mu\mu \to \mu\mu$）**，当 $m_s \gtrsim 10\text{ GeV}$ 时：
       $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}}\right|_{\mu\mu} \le \frac{4 m_\mu^2}{m_s^2} = \frac{4 \times (0.10566)^2}{10^2} = 4.47 \times 10^{-4}$$
       对散射截面的相对修正更是低于 $\lesssim 10^{-7}$（若计及干涉项则低于 $4\times 10^{-4}$）。
     - 对于**缪子-陶子过程（$\mu\tau$）**，当 $m_s \gtrsim 10\text{ GeV}$ 时：
       $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}}\right|_{\mu\tau} \le \frac{4 m_\mu m_\tau}{m_s^2} = \frac{4 \times 0.10566 \times 1.77686}{10^2} = 7.51 \times 10^{-3} < 1\%$$
     - 对于**纯陶子过程（$\tau\tau$）**，当 $m_s \gtrsim 10\text{ GeV}$ 时：
       $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}}\right|_{\tau\tau} \le \frac{4 m_\tau^2}{m_s^2} \approx 0.126 \quad (\text{当 } m_s \ge 30\text{ GeV 时则 } \le 1.4\%)$$
   - **相对于纵向分量（在手征压低道 $\sqrt{\hat{s}} \ll m_s$）**：
     $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}^{\text{long}}}\right| = \frac{|q^2 - m_{A'}^2|}{|q^2 - m_s^2|} \simeq \frac{\max(|q^2|, m_{A'}^2)}{m_s^2} \ll 1 \qquad (\text{当 } m_{A'}, \sqrt{|q^2|} \ll m_s)$$

#### Step 3.3：逐步推导单圈轻子反常磁矩 $(g-2)_\mu$ 中 $s$ 圈与 $A'$ 圈的贡献比

若考察缪子反常磁矩 $\Delta a_\mu = \frac{1}{2}(g-2)_\mu$，单圈标量 $s$ 与单圈轴矢量 $A'$ 对 $\Delta a_\mu$ 的贡献比如下：
1. **单圈标量 $s$ 的贡献（Leveille 公式，在 $m_s \gg m_\mu$ 极限下）**：
   $$\Delta a_\mu^{(s)} = \frac{y_{s\mu\mu}^2}{8\pi^2} \frac{m_\mu^2}{m_s^2} \left[ \ln\left(\frac{m_s^2}{m_\mu^2}\right) - \frac{7}{6} \right] = \frac{1}{8\pi^2} \frac{m_\mu^2}{v_s^2} \frac{m_\mu^2}{m_s^2} \left[ \ln\left(\frac{m_s^2}{m_\mu^2}\right) - \frac{7}{6} \right]$$
2. **单圈轴矢量 $A'$ 的贡献**：
   - 在重质量区 $m_{A'} \gg m_\mu$：
     $$\Delta a_\mu^{(A')} \simeq -\frac{5 g_X^2}{12\pi^2} \frac{m_\mu^2}{m_{A'}^2} = -\frac{5}{48\pi^2} \frac{m_\mu^2}{v_s^2}$$
   - 在轻质量区 $m_{A'} \lesssim m_\mu$（此时由纵向 Goldstone 模式主导）：
     $$\Delta a_\mu^{(A')} \simeq -\frac{g_X^2}{8\pi^2} \frac{m_\mu^2}{m_{A'}^2} = -\frac{1}{32\pi^2} \frac{m_\mu^2}{v_s^2}$$
3. **两者之比（$v_s^2$ 再次严格约消）**：
   $$\left|\frac{\Delta a_\mu^{(s)}}{\Delta a_\mu^{(A')}}\right| \simeq \frac{6}{5} \frac{m_\mu^2}{m_s^2} \left[ \ln\left(\frac{m_s^2}{m_\mu^2}\right) - \frac{7}{6} \right]$$
   代入基准下限 $m_s = 10\text{ GeV}$：
   $$\left|\frac{\Delta a_\mu^{(s)}}{\Delta a_\mu^{(A')}}\right|_{m_s=10\text{ GeV}} = 1.2 \times \frac{(0.10566)^2}{10^2} \times \left[ \ln\left(\frac{100}{0.01116}\right) - 1.167 \right] = 1.34 \times 10^{-4} \times 7.93 = 1.06 \times 10^{-3} \approx 0.1\%$$
   结论：**在 $m_s \gtrsim 10\text{ GeV}$ 时，标量 $s$ 对 $(g-2)_\mu$ 的贡献不到轴矢量 $A'$ 贡献的千分之一（$0.1\%$）。**

#### Step 3.4：明确划定“忽略 $s$ 近似”成立与失效的精确边界表

将参数空间与能标范围的精确边界总结为表 3：

| 物理判据维度 | 近似完全成立的区域（可安全忽略 $s$） | 近似失效的区域（必须保留 $s$ 或被排除） | 物理原因与定量指标 |
| :--- | :--- | :--- | :--- |
| **1. 微扰幺正性边界** | $v_s = \frac{m_{A'}}{2g_X} > \frac{m_s}{\sqrt{2\lambda_S^{\max}}} \gtrsim 2\text{--}4\text{ GeV}$ | $v_s = \frac{m_{A'}}{2g_X} < \frac{10\text{ GeV}}{\sqrt{2\lambda_S^{\max}}}$ | 正文公式 (34)：若 $v_s$ 过小，$m_s$ 无法在不破坏微扰论的前提下达到 $10\text{ GeV}$ |
| **2. 过程动量转移 $q^2$** | 低能过程：$\sqrt{\vert q^2\vert} \ll m_s$（且 $m_{A'} \ll m_s$） | 高能对撞过程：$\sqrt{\hat{s}} \gtrsim m_s$ | 低能下 $\vert\mathcal{M}_s / \mathcal{M}_{A'}\vert \sim 4m_\ell^2/m_s^2 \ll 1$；当 $\sqrt{\hat{s}} \sim m_s$ 时 $s$ 传播子可共振激发 |
| **3. 紫外重整化混合** | 除 $\vert m_s - m_h\vert \lesssim 8\text{ MeV}$ 外的全部 $m_s \ge 10\text{ GeV}$ | 仅在无宽度近似下的极窄点 $\vert m_s - m_h\vert \lesssim 8\text{ MeV}$ | 单圈 $\tau$ 圈图混合 $\delta m_{sh}^2/m_h^2 \lesssim 10^{-5}\text{--}10^{-4}$，计入宽度后全区间安全 |

### 第四阶段：可直接复制粘贴的英文审稿回复信与论文修改段落

#### 1. 审稿回复信完整段落（Response to Referee Comment 3）

```latex
\textbf{Response to Comment 3:}

We thank the referee for raising these insightful questions regarding radiative $s$--$h$ mixing, the resonance behavior as $m_s \to m_h$, and the non-decoupling property of $m_s$. Following the referee's suggestions, we have explicitly calculated the one-loop $s$--$h$ mixing across the allowed $m_s$ range, compared it against LHC Higgs bounds, and clarified the regime of validity for neglecting $s$ in the revised manuscript. Our step-by-step findings are summarized below:

\textbf{1. Calculation of one-loop $s$--$h$ mixing as a function of $m_s$:}
In our UV completion (Table I), charged-lepton masses arise after both $H$ and $S$ acquire VEVs via the heavy vector-like leptons $E_{\mu,\tau}$, fixing the effective Yukawa couplings to $y_{h\ell\ell} = m_\ell / v$ and $y_{s\ell\ell} = m_\ell / v_s = 2 g_X m_\ell / m_{A'}$. While the tree-level portal coupling $\lambda_{HS}(H^\dagger H)(S^\dagger S)$ is a renormalized parameter that can be set to vanish at the UV matching scale $\mu_R = M_E$, one-loop fermion diagrams indeed generate an off-diagonal self-energy $\Pi_{sh}(p^2)$ at lower scales. Because $y_{s\ell\ell} y_{h\ell\ell} = m_\ell^2 / (v v_s)$, the $\tau$-loop dominates over the $\mu$-loop by $(m_\tau/m_\mu)^2 \approx 283$, yielding:
\begin{equation*}
\Pi_{sh}^{(\tau)}(p^2) = \frac{m_\tau^2}{16\pi^2 v \, v_s} \int_0^1 dx \, \big[ 6 m_\tau^2 - 6x(1-x)p^2 \big] \ln\left(\frac{M_{E_\tau}^2}{m_\tau^2 - x(1-x)p^2 - i\epsilon}\right).
\end{equation*}
Evaluating this at the Higgs mass shell $p^2 = m_h^2$ gives the conservative upper bound on the dimensionless radiative mixing parameter:
\begin{equation*}
\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2} \simeq \frac{1}{16\pi^2} \frac{m_\tau^2}{v \, v_s} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx \left(\frac{8.1 \times 10^{-5}\text{ GeV}}{v_s}\right) \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right),
\end{equation*}
whereas the momentum-independent chiral mass term $\delta m_{sh}^2(0)/m_h^2$ is further suppressed by $6 m_\tau^2 / m_h^2 \approx 1.2 \times 10^{-3}$.

Crucially, Eq.~(34) enforces a perturbative lower bound on $v_s$ for any given $m_s$, $v_s > m_s / \sqrt{2\lambda_S^{\max}}$. Substituting this bound yields the maximum loop-induced mixing angle as an explicit function of $m_s$:
\begin{equation*}
|\sin\theta_{sh}(m_s)|_{\max} \simeq \frac{\sqrt{2\lambda_S^{\max}}}{16\pi^2} \frac{m_\tau^2}{v \, m_s} \frac{m_h^2}{|m_h^2 - m_s^2|} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \lesssim 8.5 \times 10^{-5} \left(\frac{10\text{ GeV}}{m_s}\right) \frac{m_h^2}{|m_h^2 - m_s^2|}
\end{equation*}
(for $\lambda_S^{\max} = \pi$ and $M_{E_\tau} = 1\text{ TeV}$).

\textbf{2. Comparison with LHC Higgs bounds, $m_s \to m_h$ resonance, and fine-tuning:}
\begin{itemize}
    \item \emph{Away from $m_s \approx m_h$:} Across the entire range $m_s \gtrsim 10\text{ GeV}$, the loop-induced mixing angle is $|\sin\theta_{sh}| \lesssim 10^{-5}\text{--}10^{-4}$, which is three to four orders of magnitude below current LHC Higgs signal-strength and heavy-scalar search limits ($|\sin\theta_{\text{exp}}| \lesssim 0.1\text{--}0.3$). For $10\text{ GeV} \le m_s < m_h/2$, the one-loop induced trilinear coupling $g_{hss}^{\text{loop}} \sim (3 m_\tau^4 / 4\pi^2 v v_s^2)\ln(M_{E_\tau}^2/m_\tau^2) \lesssim 2\times 10^{-3}\text{ GeV}$ yields $\text{BR}(h \to ss) \lesssim 10^{-7}$, well below the experimental bound $\text{BR}(h \to \text{BSM}) < 0.12$.
    \item \emph{Resonance as $m_s \to m_h$:} Reaching $m_s \approx m_h = 125.25\text{ GeV}$ while satisfying Eq.~(34) requires $v_s > m_h / \sqrt{2\lambda_S^{\max}} \approx 25\text{--}50\text{ GeV}$, which automatically suppresses $y_{s\tau\tau} = m_\tau / v_s \lesssim 0.035\text{--}0.07$ and reduces $|\delta m_{sh}^2|/m_h^2$ to $(0.7\text{--}1.4)\times 10^{-5}$. Consequently, $|\sin\theta_{sh}|$ only exceeds $\sin\theta_{\text{exp}} \approx 0.1$ within an ultra-narrow mass window:
    \begin{equation*}
    \Delta m_s = |m_s - m_h| \lesssim \frac{m_h}{2\sin\theta_{\text{exp}}} \left(\frac{|\delta m_{sh}^2|}{m_h^2}\right) \lesssim 4\text{--}8\text{ MeV}
    \end{equation*}
    (or $\lesssim 30\text{ keV}$ using the static mass term). This window is comparable to the natural decay widths $\Gamma_h \approx 4.1\text{ MeV}$ and $\Gamma(s \to \tau^+\tau^-) \simeq m_\tau^2 m_s / (8\pi v_s^2) \approx 7\text{--}25\text{ MeV}$, which regularize the complex propagator denominator at exact degeneracy and prevent any unphysical enhancement. No counterterm fine-tuning ($\Delta_{\text{FT}} \ll 1$) is required.
\end{itemize}

\textbf{3. Clarification on the ``non-decoupling'' of $m_s$ and regime of validity:}
We fully agree with the referee that $m_s$ cannot formally decouple ($m_s \to \infty$) at fixed $(g_X, m_{A'})$ because $s$ is the radial Higgs mode of $U_A(1)_{L_\mu-L_\tau}$ breaking ($m_s = \sqrt{2\lambda_S} v_s$)—this is precisely why we highlighted the perturbative ceiling in Eq.~(34). By adopting the benchmark $m_s \gtrsim 10\text{ GeV}$, we do not take the formal limit $m_s \to \infty$, but rather work within the perturbatively allowed region $v_s > m_s/\sqrt{2\lambda_S^{\max}}$ at low momentum transfers $|q^2| \ll m_s^2$. In this kinematic regime, tree-level $s$-exchange is suppressed relative to $A'$-exchange by $|\mathcal{M}_s / \mathcal{M}_{A'}| \lesssim (y_{s\ell\ell}^2/m_s^2)/(g_X^2/m_{A'}^2) = 4 m_\ell^2 / m_s^2$ ($\le 4.5\times 10^{-4}$ for muons at $m_s \ge 10\text{ GeV}$), and the one-loop scalar contribution to $(g-2)_\mu$ is suppressed by $|\Delta a_\mu^{(s)} / \Delta a_\mu^{(A')}| \sim (m_\mu^2/m_s^2)\ln(m_s^2/m_\mu^2) \lesssim 10^{-3}$. This approximation only breaks down when $v_s = m_{A'}/(2g_X) < 10\text{ GeV}/\sqrt{2\lambda_S^{\max}}$ (which is already excluded by Eq.~(34)) or in high-energy processes with $\sqrt{\hat{s}} \gtrsim m_s$.
```

#### 2. 论文正文公式 (34) 下方可直接插入的修改段落

```latex
We note that although $\tau$ and $\mu$ loops radiatively generate $s$--$h$ mixing even when the renormalized tree-level portal coupling vanishes at the UV scale $M_E$, the resulting one-loop off-diagonal self-energy is strongly suppressed by the tau Yukawa coupling and loop factor, $|\delta m_{sh}^2|/m_h^2 \simeq (16\pi^2)^{-1} (m_\tau^2 / v v_s) \ln(M_E^2/m_h^2) \lesssim 10^{-4}$ for $m_s \gtrsim 10\text{ GeV}$. Because Eq.~(34) enforces $v_s > m_s/\sqrt{2\lambda_S^{\max}}$ (requiring $v_s \gtrsim 25\text{--}50\text{ GeV}$ near $m_s \approx m_h$), the loop-induced mixing angle remains $|\sin\theta_{sh}| \lesssim 10^{-4}$ across the allowed parameter space—three to four orders of magnitude below LHC Higgs signal-strength and $h \to ss$ bounds—except within an ultra-narrow degeneracy window $|m_s - m_h| \lesssim \mathcal{O}(10\text{ MeV})$ that is regularized by the natural scalar widths $\Gamma_{h,s}$. Furthermore, while $m_s$ cannot formally decouple ($m_s \to \infty$) at fixed $v_s$ due to Eq.~(34), choosing $m_s \gtrsim 10\text{ GeV}$ within the perturbative regime kinematically suppresses $s$-exchange relative to $A'$-exchange by $\sim 4m_\ell^2/m_s^2 \ll 1$ in low-energy observables ($|q^2| \ll m_s^2$).
```


---

## 第二部分：独立复核、UV–EFT 匹配与持续计算记录（来自计算汇总）

> 本部分保留原始阶段性计算记录，包括已经纠正的内容、候选结果、尚未完成的推导及每一阶段的核验边界。文中明确标为“候选”“条件性”“阶段性”或“未完成”的结果，不应在合并时升级为最终结论。

> **范围说明**：本报告依据用户提供的
> `higgs_portal_mixing_merged_guide.md`，独立复核其中可从所写低能有效
> Yukawa
> 耦合直接计算的费米子泡图，并检查重整化、匹配、简并区及唯象结论的逻辑。\
> **重要限制**：没有原论文完整 UV
> 拉氏量的全部质量本征态、混合矩阵、费曼规则和重整化条件，因而本文不会把低能有效理论的泡图计算冒充为完整
> UV 完备模型的最终预测。

### 1. 结论摘要

原文的研究路线有合理部分，但**当前数值结论不能直接作为论文结论或审稿回复使用**。独立复核后，最重要的结论如下：

1.  **圈图的 Dirac 迹正确**： 
$$

    `\mathrm{Tr}`{=tex}
$$
(`\slashed{k}`{=tex}+m)(`\slashed{k}`{=tex}+`\slashed `{=tex}p+m)
$$

    =4(k^2+k`\cdot `{=tex}p+m^2). 
$$

2.  在原文采用的自能定义下，单个轻子泡图经 Feynman
    参数化后的被积函数确实正比于 
$$

    `\Delta`{=tex}(x,p^2)=m\_`\ell`{=tex}^2-x(1-x)p\^2. 
$$
 但原文从 Step
    1.4 的 (12`\Delta`{=tex}) 跳到 Step 1.5 的
    (6`\Delta`{=tex}`\ln`{=tex}(M_E\^2/`\Delta`{=tex}))，**这不是单纯减去紫外极点就能推出的**。除非另有完整
    UV--EFT matching 计算解释，否则系数存在未解决的不一致。
3.  原文把 (p^2=m_h^2) 的积分近似为单个 (`\ln`{=tex}(M_E^2/m_h^2)) 乘以
    (`\int `{=tex}6x(1-x)dx=1)，**不是精确在壳积分**。由于
    (m_h\>2m\_`\tau`{=tex})，(`\Delta`{=tex})
    在积分区间内会变号，必须保留完整参数积分及其虚部。
4.  按原文 Step 1.5 所假设的
    (6`\Delta`{=tex}`\ln`{=tex}(M_E\^2/`\Delta`{=tex})) 公式，对
    (m\_`\tau=1.77686`{=tex}) GeV、(m_h=125.25) GeV、(M_E=1)
    TeV、(v=246.22) GeV、(v_s=50) GeV 做数值积分，得到 
$$

    \|`\delta`{=tex}`\Pi`{=tex}\_{sh}^{(`\tau`{=tex})}(m_h^2)\|`\simeq 0.168`{=tex} {`\rm GeV`{=tex}}\^2,
    `\qquad`{=tex} `\frac{|\delta\Pi_{sh}^{(\tau)}|}{m_h^2}`{=tex}
    `\simeq 1.07`{=tex}`\times10`{=tex}\^{-5}. 
$$

    这与原文的粗略单对数估算同数量级，但不是同一个数；而且它**只验证了所假设的低能匹配公式的数值积分，不验证该匹配公式本身**。
5.  **不能由"宽度非零"直接推出简并区必然安全**。原文使用的宽度差分母不是完整二态系统普适的混合角公式。需要从完整复数二点函数矩阵、极点和实际可观测信号出发分析。
6.  (h`\to `{=tex}ss) 的环图估算也不能自动排除树图门户耦合的贡献。只要
    (`\lambda`{=tex}\_{HS})
    是允许的可重整化参数，就必须说明其边界条件、阈值匹配及其对物理质量混合和三标量耦合的影响。

**总体判断**：非简并区的"轻子圈通常较小"可能是合理的数量级判断；但当前推导不足以证明"全参数空间都安全""有限宽度自动消除限制"或"完全无需微调"。

------------------------------------------------------------------------

### 2. 独立计算：低能轻子泡图

#### 2.1 输入耦合和圈图

按原文 Step 0.4 的有效相互作用定义 
$$

-`\mathcal `{=tex}L`\supset `{=tex}y\_{h`\ell`{=tex}`\ell`{=tex}}h`\bar`{=tex}`\ell`{=tex}`\ell`{=tex}+
y\_{s`\ell`{=tex}`\ell`{=tex}}s`\bar`{=tex}`\ell`{=tex}`\ell`{=tex}, 
$$

其中 
$$

y\_{h`\ell`{=tex}`\ell`{=tex}}=`\frac{m_\ell}{v}`{=tex},`\qquad`{=tex}
y\_{s`\ell`{=tex}`\ell`{=tex}}=`\frac{m_\ell}{v_s}`{=tex},`\qquad`{=tex}
y\_{h`\ell`{=tex}`\ell`{=tex}}y\_{s`\ell`{=tex}`\ell`{=tex}}=`\frac{m_\ell^2}{vv_s}`{=tex}.

$$

圈图中有两个标量 Yukawa 顶点、两条轻子传播子和一个闭合费米子圈。按原文的
(-i`\Pi`{=tex}\_{sh}) 约定，Dirac 迹为 
$$

```{=tex}
\begin{aligned}
T&=\mathrm{Tr}[(\slashed{k}+m_\ell)
(\slashed{k}+\slashed p+m_\ell)]\\
&=4(k^2+k\cdot p+m_\ell^2).
\end{aligned}
```

$$

引入 Feynman 参数并令 (q=k+xp)，得到 
$$

`\Delta`{=tex}(x,p^2)=m\_`\ell`{=tex}^2-x(1-x)p\^2, 
$$

以及对称积分后的分子 (q\^2+`\Delta`{=tex})。

在 (d=4-2`\epsilon`{=tex}) 维正规化中，按原文的积分约定，泡图结构为 
$$

`\Pi`{=tex}\_{sh}^{(`\ell`{=tex})}(p^2)=
`\frac{y_{s\ell\ell}y_{h\ell\ell}}{16\pi^2}`{=tex} `\int`{=tex}\_0\^1
dx,12`\Delta`{=tex} `\left[\frac{1}{\bar\epsilon}
-\ln\frac{\Delta-i0}{\mu_R^2}+\frac13\right]`{=tex}, 
$$
 这里展示的是原文
Step 1.4 所对应的**低能泡图表达式及其约定**。整体自能符号会随
(`\Pi`{=tex}) 的定义改变，但这不影响以下对系数一致性和积分大小的检查。

#### 2.2 (12`\Delta`{=tex}) 与 (6`\Delta`{=tex}) 的问题

原文 Step 1.4 给出 (12`\Delta`{=tex})；Step 1.5 却使用 
$$

`\delta `{=tex}m\_{sh}\^2=
`\frac{y_sy_h}{16\pi^2}`{=tex}`\int`{=tex}\_0\^1dx,
6`\Delta`{=tex}`\ln`{=tex}`\frac{M_E^2}{\Delta-i0}`{=tex}. 
$$

从前式减去 (1/`\bar`{=tex}`\epsilon`{=tex}) 极点，并把 (`\mu`{=tex}\_R)
取为 (M_E)，只会改变极点项和对数的表达，**不会自行把系数 12 变成
6**。另外，前式还包含有限常数项 (1/3)。若 UV 完备理论匹配后确实得到系数
6，必须展示 UV 图、EFT 图及反项的具体差值；目前文档没有给出这一证明。

因此，以下数值积分将分开报告： - **方案 A：** 按文档 Step 1.5 的
(6`\Delta`{=tex}`\ln`{=tex}(M_E\^2/`\Delta`{=tex}))
公式作条件性数值核验； - **方案 B：** 采用 Step 1.4 的
(12`\Delta`{=tex}) 系数，对相同对数积分作比较。

两者都不能取代完整 UV--EFT matching。

#### 2.3 在 (p^2=m_h^2) 处的完整数值积分

采用参数： 
$$

```{=tex}
\begin{aligned}
&m_\tau=1.77686\ {\rm GeV},\quad
m_\mu=0.10566\ {\rm GeV},\\
&m_h=125.25\ {\rm GeV},\quad
v=246.22\ {\rm GeV},\quad M_E=1000\ {\rm GeV}.
\end{aligned}
```

$$

积分对象取 
$$

I\_`\ell`{=tex}(p^2)=`\int`{=tex}*0\^1\ dx,\ `\Delta`{=tex}*`\ell`{=tex}(x,p^2)
`\ln`{=tex}`\frac{M_E^2}{\Delta_\ell(x,p^2)-i0}`{=tex}. 
$$

对 (p^2=m_h^2)，因为 (m_h^2\>4m\_`\ell`{=tex}^2)，中间一段参数区间满足
(`\Delta`{=tex}*`\ell`{=tex}\<0)。因此 
$$

`\ln`{=tex}`\frac{M_E^2}{\Delta-i0}`{=tex}
=`\ln`{=tex}`\frac{M_E^2}{|\Delta|}`{=tex}+i`\pi`{=tex}
`\quad`{=tex}(`\Delta`{=tex}\<0), 
$$

所以积分有虚部。这是物理阈值结构，不应把 (`\Delta`{=tex}) 直接替换为
(m*`\ell`{=tex}\^2) 或 (m_h\^2)。

数值积分结果为：

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  量                                                                               (`\tau`{=tex}) 圈                                   (`\mu`{=tex}) 圈
  ----------------------------------------------- -------------------------------------------------- --------------------------------------------------
  (`\mathrm{Re}`{=tex},I\_`\ell`{=tex}(m_h\^2))     (-1.52047`\times10`{=tex}^4 {`\rm GeV`{=tex}}^2)   (-1.52209`\times10`{=tex}^4 {`\rm GeV`{=tex}}^2)

  (`\mathrm{Im}`{=tex},I\_`\ell`{=tex}(m_h\^2))     (-8.20407`\times10`{=tex}^3 {`\rm GeV`{=tex}}^2)   (-8.21395`\times10`{=tex}^3 {`\rm GeV`{=tex}}^2)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

将耦合乘积 (m\_`\ell`{=tex}\^2/(vv_s)) 乘回去。取 (v_s=50) GeV：

  ------------------------------------------------------------------------------------------------------------------------
  条件性计算                  (`\tau`{=tex}) 圈 (                          `\delta`{=tex}`\Pi`{=tex}                     )
  -------------- -------------------------------- -------------------------------------------------- ---------------------
  方案 A：系数 6   (0.16835 {`\rm GeV`{=tex}}\^2)    (5.96`\times10`{=tex}^{-4} {`\rm GeV`{=tex}}^2)   (`\sim`{=tex}282.5)

  方案 B：系数     (0.33670 {`\rm GeV`{=tex}}\^2)   (1.192`\times10`{=tex}^{-3} {`\rm GeV`{=tex}}^2)   (`\sim`{=tex}282.5)
  12，仅对数项                                                                                       
  ------------------------------------------------------------------------------------------------------------------------

在方案 A 中， 
$$
 `\frac{|\delta\Pi_{sh}^{(\tau)}|}{m_h^2}`{=tex}
=`\frac{0.16835}{(125.25)^2}`{=tex}
`\simeq1.073`{=tex}`\times10`{=tex}\^{-5}. 
$$
 若 (v_s=25)
GeV，耦合正比于 (1/v_s)，结果加倍： 
$$

\|`\delta`{=tex}`\Pi`{=tex}\_{sh}^{(`\tau`{=tex})}\|`\simeq0.3367`{=tex} {`\rm GeV`{=tex}}^2,`\qquad`{=tex}
\|`\delta`{=tex}`\Pi`{=tex}\|/m_h^2`\simeq2.146`{=tex}`\times10`{=tex}^{-5}.

$$

这些结果说明：完整积分的数量级约为 (10\^{-5})（相对于
(m_h\^2)），但**结果依赖系数、匹配方案和重整化条件**。不能将该条件性结果直接当成完整模型预测。

#### 2.4 静态极限 (p\^2=0)

在 (p\^2=0) 时
(`\Delta`{=tex}=m\_`\ell`{=tex}\^2)，无阈值虚部。按文档方案 A： 
$$

`\delta`{=tex}`\Pi`{=tex}*{sh}\^{(`\ell`{=tex})}(0)=
`\frac{y_sy_h}{16\pi^2}`{=tex},6m*`\ell`{=tex}\^2
`\ln`{=tex}`\frac{M_E^2}{m_\ell^2}`{=tex}. 
$$

对 (`\tau`{=tex}) 圈，取 (v_s=50) GeV： 
$$

\|`\delta`{=tex}`\Pi`{=tex}\_{sh}\^{(`\tau`{=tex})}(0)\|
`\simeq3.897`{=tex}`\times10`{=tex}^{-4} {`\rm GeV`{=tex}}^2, 
$$
 
$$

`\frac{|\delta\Pi_{sh}^{(\tau)}(0)|}{m_h^2}`{=tex}
`\simeq2.484`{=tex}`\times10`{=tex}\^{-8}. 
$$
 取 (v_s=25) GeV
时，这两个值加倍。此处与原文的静态估算一致（在相同系数与参数下）。

但静态自能 (`\Pi`{=tex}(0)) 和希格斯极点处 (`\Pi`{=tex}(m_h\^2))
是不同量；不能用静态结果代表在壳混合。

------------------------------------------------------------------------

### 3. 为什么原文的在壳近似不够准确

原文把 
$$
 `\int`{=tex}\_0\^1dx,
$$
6m\_`\ell`{=tex}^2-6x(1-x)p^2
$$

`\ln`{=tex}`\frac{M_E^2}{m_\ell^2-x(1-x)p^2-i0}`{=tex} 
$$

近似为一个整体对数乘上 (m_h\^2)。但对数本身依赖 (x)，且在
(`\Delta=0`{=tex}) 处存在阈值结构。一般而言， 
$$
 `\int `{=tex}dx,
f(x)`\ln`{=tex}`\frac{M_E^2}{\Delta(x)}`{=tex}
`\ne `{=tex}`\left`{=tex}(`\int `{=tex}dx,f(x)`\right`{=tex})
`\ln`{=tex}`\frac{M_E^2}{m_h^2}`{=tex}. 
$$

所以该简化只能用于粗略数量级估算，不能称为精确在壳结果。独立数值积分显示，方案
A 的完整复数积分在 (v_s=50) GeV 时给出
(\|`\delta`{=tex}`\Pi`{=tex}\|`\simeq0.168`{=tex} {`\rm GeV`{=tex}}\^2)，而文档单对数估算约为
(0.1 {`\rm GeV`{=tex}}\^2) 量级；两者同量级，但并不相等。

------------------------------------------------------------------------

### 4. 还有一个关键问题：EFT 接触项

原文 Step 0.4 的有效质量算符展开为 
$$

-`\mathcal `{=tex}L\_{`\rm eff`{=tex}}`\supset`{=tex}
m\_`\ell`{=tex}`\left`{=tex}(1+`\frac `{=tex}hv+`\frac{s}{v_s}`{=tex}
+`\frac{hs}{vv_s}`{=tex}`\right`{=tex})`\bar`{=tex}`\ell`{=tex}`\ell`{=tex}.

$$
 因此 EFT 中除 (h`\bar`{=tex}`\ell`{=tex}`\ell`{=tex}) 与
(s`\bar`{=tex}`\ell`{=tex}`\ell`{=tex}) 外，还包含 
$$

-`\mathcal `{=tex}L`\supset `{=tex}`\frac{m_\ell}{vv_s}`{=tex}hs`\bar`{=tex}`\ell`{=tex}`\ell`{=tex}.

$$

这个 (hs`\bar`{=tex}`\ell`{=tex}`\ell`{=tex}) 接触项可产生带一个 (h,s)
外腿的费米子 tadpole
型图。文档的泡图计算没有清楚展示这一图在所用匹配方案中的处理方式。它不代表一定要把某个
tadpole
直接机械加到泡图上；正确做法是列出同一阶所有图，在同一重整化方案下进行
UV 与 EFT 匹配，避免漏项或重复计数。

更重要的是：EFT 中由维五算符导出的 Yukawa 耦合不是完整 UV 理论。只用 EFT
泡图，不能独自确定完整 UV 理论的有限阈值匹配系数。

------------------------------------------------------------------------

### 5. 混合角与简并区

#### 5.1 非简并区

对于实对称的常数质量矩阵，在 
$$

\|`\delta `{=tex}m\_{sh}^2\|`\ll`{=tex}\|m_h^2-m_s\^2\| 
$$
 时， 
$$

\|`\theta`{=tex}*{sh}\|`\simeq`{=tex}
`\frac{|\delta m_{sh}^2|}{|m_h^2-m_s^2|}`{=tex} 
$$

是合理的小混合近似。这里的 (`\delta `{=tex}m*{sh}\^2)
必须是与质量定义、重整化条件一致的非对角质量元；不能不加区分地把任意动量点的
(`\Pi`{=tex}\_{sh}(p\^2)) 直接当成常数质量矩阵元。

#### 5.2 简并区

当 (m_s`\simeq `{=tex}m_h)
时，上述近似的分母变小，不能据此得出混合角上限。对不稳定粒子，需要考虑完整的复数二点函数矩阵，例如

$$
 `\mathbf `{=tex}D^{-1}(p^2)=
```{=tex}
\begin{pmatrix}
p^2-m_{h,0}^2+\widehat\Pi_{hh}(p^2)&\widehat\Pi_{hs}(p^2)\\
\widehat\Pi_{sh}(p^2)&p^2-m_{s,0}^2+\widehat\Pi_{ss}(p^2)
\end{pmatrix}
```
, 
$$

具体正负号取决于自能约定。然后求复极点，并计算相关产生和衰变过程的可观测率。

原文使用 
$$
 `\sqrt{(m_h^2-m_s^2)^2+(m_h\Gamma_h-m_s\Gamma_s)^2}`{=tex}

$$

作为普适分母的做法并不充分。两个共振的宽度、混合自能虚部和干涉结构都可能重要；宽度差还可能因参数而部分抵消。因此，**不能只凭有限宽度就证明严格简并区必然低于
LHC 排除线**。

#### 5.3 "无需微调"结论

微调程度取决于采用的参数定义、树图门户项、环图修正及所选的微调度量。若
(`\lambda`{=tex}*{HS})
是允许的独立可重整化参数，令其在某个尺度为零是一项边界条件；要声称没有微调，需要解释该条件的理论来源或给出明确的稳定性分析。当前文档没有足够依据得出
(`\Delta`{=tex}*{`\rm FT`{=tex}}`\ll1`{=tex}) 这一普遍结论。

------------------------------------------------------------------------

### 6. (h`\to `{=tex}ss) 与 LHC 限制的注意事项

1.  (h`\to `{=tex}ss)
    的总三标量耦合一般包含树图门户势贡献以及量子修正。只计算一个轻子三角图，不能证明完整
    (g\_{hss}) 或 (`\mathrm{BR}`{=tex}(h`\to `{=tex}ss)) 必然极小。
2.  需要说明 (`\lambda`{=tex}\_{HS})
    在什么尺度、什么方案下被设为零，并把 UV 阈值匹配到低能参数。
3.  LHC
    的混合角限制依赖标量质量、衰变分支比、宽度与具体搜索道；(\|`\sin`{=tex}`\theta`{=tex}\|`\sim`{=tex}0.1`\text{--}`{=tex}0.3)
    只能作为粗略参照，不是所有质量区间统一适用的硬界限。
4.  当 (m_s\<m_h/2) 时，若 (h`\to `{=tex}ss)
    可开，必须将新增部分宽度纳入希格斯总宽度与信号强度拟合。

------------------------------------------------------------------------

### 7. 标量退耦与 ((g-2)\_`\mu`{=tex})

由 
$$
 m_s\^2`\simeq2`{=tex}`\lambda`{=tex}\_Sv_s\^2 
$$
 可见，固定 (v_s)
而任意增大 (m_s) 会要求 (`\lambda`{=tex}\_S)
变大并最终离开微扰范围。这个"不能在固定破缺尺度下无限退耦"的提醒合理。

但
(\|`\mathcal `{=tex}M_s/`\mathcal `{=tex}M\_{A'}\|`\sim`{=tex}4m\_`\ell`{=tex}^2/m_s^2)
不能作为任意过程的普适振幅比。它需要从指定过程的洛伦兹结构、动量转移和有效算符中推导。对
((g-2)\_`\mu`{=tex})，应在具体质量层级下分别使用标量和轴矢量的完整一圈函数；渐近表达式不能自动覆盖全部参数区间。

------------------------------------------------------------------------

### 8. 建议的重新计算流程

1.  从完整 UV
    拉氏量出发，写出重轻子与标准模型轻子的质量矩阵，并对角化，明确物理轻子和重轻子的混合。
2.  在完整 UV 理论中列出所有一圈 (h)--(s) 二点图及相应反项；不能仅将
    (M_E) 当作低能对数的截止。
3.  选定一致的重整化方案，明确 (`\lambda`{=tex}\_{HS}(`\mu`{=tex}\_0)=0)
    是假设还是 UV 对称性预言，并计算阈值匹配。
4.  在低能 EFT 中包括由维五算符导出的接触项及同阶贡献，确保与 UV
    计算匹配。
5.  对 (p^2=0)、(p^2=m_h^2)、(p^2=m_s\^2)
    分别计算完整复数自能，不以一个单对数替代参数积分。
6.  非简并区使用受控的小混合近似；简并区求完整复数二点函数矩阵的极点并计算实验可观测量。
7.  最后重算 (h`\to `{=tex}ss)、LHC 排除区和微调指标，再撰写审稿回复。

### 9. 可供当前阶段使用的谨慎结论

> 在低能有效理论中，(`\mu`{=tex}) 和 (`\tau`{=tex}) 的 Yukawa 耦合会产生
> (s)--(h) 二点函数。按给定的有效耦合和一种指定的有限对数匹配假设，完整
> Feynman 参数积分在 (p^2=m_h^2) 处给出
> (\|`\delta`{=tex}`\Pi`{=tex}\_{sh}\|/m_h^2`\sim`{=tex}10^{-5})
> 的数量级，且 (`\tau`{=tex}) 圈主导。然而，当前文档中
> (12`\Delta`{=tex}) 与 (6`\Delta`{=tex}) 的系数衔接尚未得到证明，EFT
> 接触项及完整 UV
> 阈值匹配也需核验。因此该数量级应视为条件性估算，而不是完整 UV
> 模型的最终预测。远离简并区时可在验证小混合条件后采用常规近似；在
> (m_s`\simeq `{=tex}m_h)
> 区域，则必须分析包含自能实部、虚部和干涉的完整复数传播子矩阵。现阶段不宜声称有限宽度自动保证整个简并区安全或无需微调。

------------------------------------------------------------------------

### 10. 最终判断

-   **可保留**：规范荷/有效 Yukawa 的总体思路、Dirac
    迹、静态极限的条件性数量级估算、标量质量与微扰性之间的关系。
-   **必须修正**：Step 1.4 到 Step 1.5
    的系数衔接、在壳单对数近似的表述、接触项和 UV--EFT matching 的处理。
-   **必须重做后才能下结论**：严格简并区的有限宽度分析、(h`\to `{=tex}ss)
    完整耦合、全参数空间 LHC 结论及"无需微调"的主张。

**建议：先不要直接复制原文中的英文审稿回复。** 应先完成完整 UV
模型的二点函数和阈值匹配；上述数值积分只能作为核验低能泡图公式的中间步骤。


------------------------------------------------------------------------

### 附录 A：数值积分的符号复核与工具执行记录

#### A.1 虚部符号更正

前文定义的积分为

$$

I_\ell(p^2)=\int_0^1 dx\,\Delta_\ell(x,p^2)
\ln\frac{M_E^2}{\Delta_\ell(x,p^2)-i0},\qquad
\Delta_\ell=m_\ell^2-x(1-x)p^2.

$$

当 $\Delta_\ell<0$ 时，按该处采用的 $i0$ 约定，

$$

\ln\frac{M_E^2}{\Delta_\ell-i0}
=\ln\frac{M_E^2}{|\Delta_\ell|}+i\pi.

$$

因此被积函数的虚部是 $\pi\Delta_\ell$，在该区间为负。故表中积分 $I_\ell$ 的虚部应为负值，而不是正值：

- $\tau$ 圈：$\operatorname{Im} I_\tau(m_h^2)=-8.20407\times10^3\,\mathrm{GeV}^2$；
- $\mu$ 圈：$\operatorname{Im} I_\mu(m_h^2)=-8.21395\times10^3\,\mathrm{GeV}^2$。

这里的符号是对上述**积分定义**而言。将积分换算为自能 $\Pi_{sh}$ 时，还必须与全篇采用的费曼规则、传播子和 $i\Pi$／$-i\Pi$ 定义保持一致；不能把积分虚部的符号直接当成所有约定下的自能虚部符号。此前报告中相应虚部的绝对值不变，但符号应按本节修正。

#### A.2 文件工具执行问题记录

在先前尝试将修订直接写回 Markdown 文件时，文件处理工具多次返回 `ChatGPTAgentToolRateLimitException`。该异常导致相应的写入步骤没有得到成功确认。它属于工具执行层面的失败，**不构成物理推导正确或错误的证据**。本次修订通过重新取得已保存的报告、在本地副本中修改并检查文件内容完成；原始资料中的模型假设和匹配缺口仍需按正文所列问题独立核验。

#### A.3 本报告的使用边界

1. 表中的数值是针对明确写出的低能积分定义和参数所做的条件性计算，不等同于完整 UV 模型的最终预测。
2. Step 1.4 与 Step 1.5 中系数从 $12\Delta$ 到 $6\Delta$ 的变化仍须由完整 UV--EFT 阈值匹配推导证明；不能仅以减去紫外极点解释。
3. 物理阈值以上的虚部必须保留，并在同一自能约定下统一符号；严格简并区则须分析完整复数传播子矩阵及可观测量。
4. 本报告未声称已经完成完整 UV 拉氏量、所有重粒子阈值、反项方案、树图门户贡献及整个参数空间的数值扫描。因此，未经这些步骤，不应把条件性数量级估算改写为“全参数空间均满足实验限制”的结论。


## 第二部分：UV–EFT 一圈匹配与双阈值 RG 的阶段性汇总

> **重要状态标记（请先读）**：本部分把此前对话中得到的 UV 自能、有效势阈值、EFT 接触图、导数算符和双阈值 RG 结果集中记录。它是可继续工作的计算笔记，不是已完成的最终匹配论文。此前对话中的若干候选公式尚未从原始 UV 质量矩阵到 EFT 反项矩阵完成独立闭环；因此凡标注“候选/待复核”的系数，不应直接作为正式论文结论。

### 11. 目标模型和约定

参考论文：L. Vietze et al.（前序低能泡图报告）以及当前讨论的 arXiv:2608.27258《An Axial $U_A(1)_{L_\mu-L_\tau}$: UV Completion and Experimental Searches》。本部分讨论的 UV 结构是每个轻味道对应一个矢量样重轻子 $E_\ell$，其 Yukawa 结构可写成

$$

-\mathcal L\supset y_\ell\bar L_\ell H E_{\ell R}
+\lambda_\ell S^{(*)}\bar E_{\ell L}\ell_R
+M_{E\ell}\bar E_{\ell L}E_{\ell R}+\mathrm{h.c.},

$$

其中 $\mu$ 扇区和 $\tau$ 扇区分别使用与规范荷相容的 $S$ 或 $S^*$。中性标量背景写为

$$

H^0=\frac{v_h+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2}.

$$

在单味道、实耦合的简化记号下，质量矩阵为

$$

\mathcal M_\ell=\begin{pmatrix}0&m_L\\m_R&M_E\end{pmatrix},\qquad
m_L=\frac{y_\ell v_h}{\sqrt2},\quad m_R=\frac{\lambda_\ell v_s}{\sqrt2}.

$$

大重质量极限给出 $m_\ell\simeq m_Lm_R/M_E$、$\theta_L\simeq m_L/M_E$、$\theta_R\simeq m_R/M_E$。完整计算必须固定左右旋转矩阵、轻态相位和所有标量耦合的同一套约定。

### 12. 完整 UV 自能的 PV 表达式（此前推导的候选形式）

令 $H_{ij}=(Y_h)_{ij}$、$S_{ij}=(Y_s)_{ij}$，并定义

$$

C_{ij}=H_{ij}S_{ij}+H_{ji}S_{ji},\qquad
D_{ij}=H_{ij}S_{ji}+H_{ji}S_{ij}.

$$

此前使用的通用 Dirac 迹结构是

$$

\mathrm{Tr}[(\slashed k+m_i)\Gamma_h(\slashed k+\slashed p+m_j)\Gamma_s]
=2C_{ij}\,k\cdot(k+p)+2m_im_jD_{ij}.

$$

对应的 PV 结构写作

$$

\Pi_{ij}(p^2)=\frac1{16\pi^2}\left\{
C_{ij}\left[A_0(m_i^2)+A_0(m_j^2)
+(m_i^2+m_j^2-p^2)B_0(p^2;m_i^2,m_j^2)\right]
+2m_im_jD_{ij}B_0(p^2;m_i^2,m_j^2)\right\}.

$$

**复核提醒：** 此式的整体符号、因子以及 $C,D$ 的定义依赖顶角的手征结构、$\Pi$ 的定义和 PV 归一化；应从完整费曼规则重算后再用于数值匹配，不能仅因它具有合理量纲就视为已最终验证。

若暂时采用论文展示的标量耦合矩阵

$$

Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix},

$$

其中 $a=m_L/v_h$、$b=m_R/v_s$，此前代数化简得到

$$

K=2ab\,c_Ls_Lc_Rs_R,\qquad Q=c_L^2c_R^2+s_L^2s_R^2,

$$

$$

C=\begin{pmatrix}K&-K\\-K&K\end{pmatrix},\qquad
D=\begin{pmatrix}K&-abQ\\-abQ&K\end{pmatrix}.

$$

在假定精确对角化恒等式 $K(m^2+M^2)=2abQmM$ 成立时，之前得到的紧凑形式是

$$

\Pi_{hs}^{UV}(p^2)=\frac{K}{16\pi^2}\Big[(4m^2-p^2)B_0(p^2;m^2,m^2)
+(4M^2-p^2)B_0(p^2;M^2,M^2)
+(2p^2-4m^2-4M^2)B_0(p^2;m^2,M^2)\Big].

$$

在该形式中，三个 $B_0$ 的 UV 极点系数相加为零。**这是此前推导中的代数检查，不代表完整模型所有图、反项和重整化条件均已核验。** 尤其需确认给定 $Y_h,Y_s$ 与原论文的本征态相位约定完全一致。

### 13. 大质量展开与局域 portal 阈值

此前使用的展开为

$$

B_0(p^2;M^2,M^2)=\Delta_\epsilon-\ln\frac{M^2}{\mu^2}
+\frac{p^2}{6M^2}+\cdots,

$$

$$

B_0(p^2;m^2,M^2)=\Delta_\epsilon+1-\ln\frac{M^2}{\mu^2}
+\mathcal O\!\left(\frac{m^2}{M^2}\ln\frac{M^2}{m^2},\frac{p^2}{M^2}\right).

$$

此前据此写出的静态极限领先项为

$$

\Pi_{hs}^{UV}(0)\simeq-\frac{KM^2}{4\pi^2},\qquad
KM^2\simeq\frac{|y_\ell|^2|\lambda_\ell|^2}{2}v_hv_s.

$$

在标量势约定 $V\supset+\lambda_{HS}(H^\dagger H)(S^\dagger S)$ 下，Coleman–Weinberg 重阈值展开给出的此前候选结果是

$$

\Delta\lambda_{HS}^{(\ell)}\simeq-
\frac{|y_\ell|^2|\lambda_\ell|^2}{8\pi^2}.

$$

两个味道在领先阶形式上相加：

$$

\Delta\lambda_{HS}\simeq-\frac1{8\pi^2}\left(
|y_\mu|^2|\lambda_\mu|^2+|y_\tau|^2|\lambda_\tau|^2\right).

$$

这里必须区分：Coleman–Weinberg 有效势可确定零外动量的势能项，但它不能单独确定导数 Wilson 系数。有限阈值还依赖明确的匹配方案、匹配尺度以及 portal 参数的边界条件。正式结果需从重质量本征值展开重新独立复核。

### 14. EFT 维数五算符与接触图规则

低能维数五算符在实耦合近似下可写成

$$

\mathcal L_{5d}\supset-
\frac{c_\ell}{M_E}S^{(*)}\bar L_\ell H\ell_R+\mathrm{h.c.}

$$

展开后有

$$

\mathcal L_{\rm EFT}\supset-
\frac{m_\ell}{v_h}h\bar\ell\ell-
\frac{m_\ell}{v_s}s\bar\ell\ell-
\frac{m_\ell}{v_hv_s}hs\bar\ell\ell.

$$

因此相应顶角（实 Yukawa、使用 $i\mathcal L_{\rm int}$ 规则）是

$$

V_{h\bar\ell\ell}=-i\frac{m_\ell}{v_h},\qquad
V_{s\bar\ell\ell}=-i\frac{m_\ell}{v_s},\qquad
V_{hs\bar\ell\ell}=-i\frac{m_\ell}{v_hv_s}.

$$

接触图是带闭合费米子环的 tadpole，不含外部动量，故它可影响局域常数项，但不会直接贡献外部 $p^2$ 系数。其整体符号必须同时考虑接触顶角、传播子和闭合费米子环的负号，不能先验假设它抵消泡图某一项。

### 15. 维数六导数算符：此前候选系数及一致性问题

选择算符基

$$

\mathcal O_D=\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S),\qquad
\mathcal L\supset C_D\mathcal O_D.

$$

在中性标量展开中，

$$

\mathcal O_D\supset v_hv_s\,\partial_\mu h\partial^\mu s.

$$

此前对话曾得到候选匹配系数

$$

C_D^{(\ell)}(\mu)=
\frac{|y_\ell|^2|\lambda_\ell|^2}{32\pi^2M_{E\ell}^2}
\left[\ln\frac{\mu^2}{M_{E\ell}^2}+\frac23\right],

$$

从而在 $\mu=M_{E\ell}$ 时

$$

C_D^{(\ell)}(M_{E\ell})=
\frac{|y_\ell|^2|\lambda_\ell|^2}{48\pi^2M_{E\ell}^2}.

$$

这一候选式等价于先前写出的
$\frac{|y|^2|\lambda|^2}{16\pi^2M^2}[\ln(\mu/M)+1/3]$。然而，前面对话中使用的 UV 振幅展开、EFT 泡图 $p^2$ 系数和极点归一化并未全部从原始矩阵重新推导；故该系数**仍是待独立验证的候选结果，不是最终认证值**。

验证必须按以下顺序完成：

1. 从原始 UV 质量矩阵对角化，推导所有 $h\bar\ell_i\ell_j$ 与 $s\bar\ell_i\ell_j$ 顶角；
2. 按同一 $i\Pi$ 约定计算全部 UV 图并作 $1/M_E^2$ 展开；
3. 在 EFT 中计算泡图、接触图和必要反项；
4. 检查 UV–EFT 差的轻粒子对数、阈值虚部和 IR 奇异项是否抵消；
5. 从局域 $p^2$ 差中提取 $C_D$，并通过独立 Green 函数检查算符基约化与波函数反项。

### 16. 反项和投影级 RG：此前候选推导

定义

$$

a_\ell=\frac{|y_\ell|^2|\lambda_\ell|^2}{32\pi^2M_{E\ell}^2}.

$$

此前按某个二点函数投影写出的候选反项为

$$

\delta C_{D,\ell}=a_\ell\Delta_\epsilon,

$$

对应固定耦合、固定重质量的投影 RG 方程

$$

\frac{dC_{D,\ell}}{d\ln\mu}=2a_\ell.

$$

它与上一节候选匹配式的显式对数导数一致：

$$

\frac{d}{d\ln\mu}\left[a_\ell\left(\ln\frac{\mu^2}{M_{E\ell}^2}+\frac23\right)\right]=2a_\ell.

$$

但是，**投影级 RG 一致性并不能证明反项矩阵完整**。完整算符混合矩阵还需要在固定且不冗余的维数六算符基中计算其他独立 Green 函数、波函数反项、维数五算符插入导致的发散和算符约化。此前对话中的“尺度抵消”仅应理解为给定候选系数与候选泡图对数之间的形式一致性检查。

### 17. 两个不同重质量的分步匹配（投影级公式）

设 $M_H>M_L$，并定义

$$

a_H=\frac{|y_H|^2|\lambda_H|^2}{32\pi^2M_H^2},\qquad
 a_L=\frac{|y_L|^2|\lambda_L|^2}{32\pi^2M_L^2}.

$$

若暂时采用上一节的投影 RG 方程，且忽略耦合运行和更高阶阈值修正，则

$$

C_D(M_H^+)=\frac23a_H,

$$

$$

C_D(M_L^-)=a_H\left[\ln\frac{M_L^2}{M_H^2}+\frac23\right],

$$

$$

C_D(M_L^+)=C_D(M_L^-)+\frac23a_L,

$$

最终在共同低能尺度 $\mu<M_L$ 有

$$

C_D(\mu)=a_H\left[\ln\frac{\mu^2}{M_H^2}+\frac23\right]
+a_L\left[\ln\frac{\mu^2}{M_L^2}+\frac23\right].

$$

这是对分步匹配结构的记录，并非完整的双阈值 RG 解。要把它升级为正式结果，必须求出完整算符混合矩阵、各 EFT 区间的 beta 函数、阈值处的有限匹配修正，并验证物理振幅对匹配尺度的独立性。

### 18. 本次汇总中的纠错和使用规则

1. 原低能报告中 $12\Delta\to6\Delta$ 的变化仍未由 UV–EFT 匹配证明；不能用“减去 UV 极点”作为解释。
2. 物理阈值以上必须保留 $i0$ 和虚部。对积分定义 $\ln[M_E^2/(\Delta-i0)]$，当 $\Delta<0$ 时该对数虚部为 $+i\pi$，乘上负的 $\Delta$ 后被积函数虚部为负；自能整体虚部仍需按统一费曼规则确定。
3. 接触图不含外部动量，因此不能用它任意调整导数算符的 $p^2$ 系数。
4. Coleman–Weinberg 有效势只给出无导数局域项，不能单独确定导数 Wilson 系数。
5. 两个阈值的显式对数形式只有在相应 beta 函数和反项矩阵正确时才代表物理尺度抵消；形式上求导相消并非完整验证。
6. 本文件的第一部分保留了早先的低能泡图数值积分和现象学注意事项；第二部分保留 UV 自能、portal 阈值、接触规则、导数算符和双阈值 RG 的阶段性结果。所有候选公式均应按本节使用边界处理。

### 19. 下一轮计算的最小核验清单

- [ ] 从原论文原始质量矩阵和标量耦合矩阵重新推导 UV 的完整 $\Pi_{hs}(p^2)$，检查符号、因子和 UV 极点。
- [ ] 独立计算 EFT 泡图与接触图，明确 $A_0$、$B_0$、有限常数和虚部。
- [ ] 对 UV 与 EFT 振幅分别作同一阶 $1/M_E^2$ 展开，并证明 IR/非解析部分逐项相消。
- [ ] 选定不冗余维数六算符基，计算完整反项矩阵及波函数、Yukawa 和标量势的相关反项。
- [ ] 从反项矩阵导出 beta 函数，逐段求解 $M_H\to M_L\to\mu$ 的 RG 演化。
- [ ] 用独立符号计算/数值积分核对 Wilson 系数，并检查匹配尺度变化只影响更高阶项。

### 20. 计算方法所依据的文献与各自用途

本节补充本报告的计算方法参考。请注意：下列文献主要提供**一圈积分、重整化、EFT 匹配与 RG 的通用方法**；它们不是本模型的现成计算答案。本文中的模型专属表达式仍需从目标模型的拉氏量、质量矩阵和费曼规则重新推导，并通过独立检查确认。

#### 20.1 目标模型的原始来源

1. **目标论文（模型定义与原始耦合）**：*An Axial* $U_A(1)_{L_\mu-L_\tau}$: *UV Completion and Experimental Searches*, arXiv:2608.27258, https://arxiv.org/abs/2608.27258 。
   - 用途：核对 UV 拉氏量、矢量类重轻子质量矩阵、轻重态混合、标量与费米子的耦合，以及论文对标量势和 portal 项的处理。
   - 使用边界：目标论文给出模型输入；本报告的自能与 Wilson 系数并非直接从该文照抄，必须按统一的费曼规则独立计算。

#### 20.2 一圈积分与 Passarino–Veltman 标量积分

2. **G. ’t Hooft and M. J. G. Veltman**, “Scalar One-Loop Integrals,” *Nuclear Physics B* **153** (1979) 365–401. DOI: https://doi.org/10.1016/0550-3213(79)90605-9 .
   - 用途：一圈标量积分的标准处理；用于理解和核对 $A_0$、$B_0$ 等积分的定义、发散结构及解析性质。

3. **G. Passarino and M. J. G. Veltman**, “One-Loop Corrections for e+e− Annihilation into μ+μ− in the Weinberg Model,” *Nuclear Physics B* **160** (1979) 151–207. DOI: https://doi.org/10.1016/0550-3213(79)90234-7 .
   - 用途：Passarino–Veltman 约化方法的经典来源之一。本文将张量/分子积分化为标量积分的思路用于组织费米子泡图；具体系数仍由本模型的 Dirac 迹和耦合决定。

4. **A. Denner**, “Techniques for the Calculation of Electroweak Radiative Corrections at the One-Loop Level and Results for W-Physics at LEP 200,” *Fortschritte der Physik* **41** (1993) 307–420. DOI: https://doi.org/10.1002/prop.2190410402 . 另见作者综述版本 arXiv:0709.1075：https://arxiv.org/abs/0709.1075 。
   - 用途：一圈振幅、重整化、反项和标量一圈积分的系统参考。本文检查 UV 极点、有限部分和自能符号时采用的也是这类标准计算框架。

#### 20.3 UV–EFT 一圈匹配、导数展开与 RG

5. **B. Henning, X. Lu, and H. Murayama**, “One-loop Matching and Running with Covariant Derivative Expansion,” *Journal of High Energy Physics* **01** (2018) 123, arXiv:1604.01019. DOI: https://doi.org/10.1007/JHEP01(2018)123 .
   - 用途：一圈 EFT 匹配、重场与轻场混合贡献的区分、导数展开以及 Wilson 系数 RG 的方法参考。
   - 与本文的关系：支持“比较 UV 与 EFT 振幅并提取局域差值”的整体策略；但本文当前使用的是具体两点函数投影，并未声称已经完成该文意义下的完整泛函匹配或完整 anomalous-dimension matrix。

6. **B. Henning, X. Lu, and H. Murayama**, “How to Use the Standard Model Effective Field Theory,” *Journal of High Energy Physics* **01** (2016) 023, arXiv:1412.1837. DOI: https://doi.org/10.1007/JHEP01(2016)023 .
   - 用途：把 UV 模型与低能 EFT、Wilson 系数和低能观测量连接起来的系统流程；用于说明匹配尺度、算符选择和低能演化必须保持一致。

7. **A. V. Manohar**, “Introduction to Effective Field Theories,” arXiv:1804.05863 (2018), https://arxiv.org/abs/1804.05863 .
   - 用途：EFT 的幂次计数、局域算符展开、匹配与重整化群的教学性综述，适合作为背景阅读。

#### 20.4 一圈有效势（仅在讨论 Coleman–Weinberg 部分时适用）

8. **S. R. Coleman and E. J. Weinberg**, “Radiative Corrections as the Origin of Spontaneous Symmetry Breaking,” *Physical Review D* **7** (1973) 1888–1910. DOI: https://doi.org/10.1103/PhysRevD.7.1888 .
   - 用途：一圈有效势的经典来源。有效势只依赖背景场，可用于提取无导数的局域势能项；它本身不能确定含外部动量的导数 Wilson 系数。

#### 20.5 本报告中各项计算与参考文献的对应关系

| 本报告的计算步骤 | 方法依据 | 不能据此直接推出的结论 |
|---|---|---|
| 从质量矩阵和标量耦合构造 UV 自能 | 目标模型原文；Denner 的一圈振幅与重整化方法 | 不能只凭通用文献确定本模型的混合角、相对符号或耦合因子 |
| 将费米子环路化为 $A_0$、$B_0$ | ’t Hooft–Veltman；Passarino–Veltman；Denner | 不能跳过 Dirac 迹和模型耦合，直接套用别的过程的数值系数 |
| 对重质量作 $p^2/M_E^2$ 展开 | 标量积分的 Feynman 参数表示与低能渐近展开；EFT 导数展开方法 | 不能把未验证的有限常数视为普适、与方案无关的结果 |
| UV–EFT 匹配 | Henning–Lu–Murayama (2018, 2016)；Manohar EFT 讲义 | 仅比较 $\Pi'_{hs}(0)$ 不等于完整匹配全部维数六算符 |
| portal 项及无导数局域项 | 目标模型的标量势；必要时参考 Coleman–Weinberg 有效势 | 有效势不能替代外动量依赖的 Green 函数匹配 |
| 阈值匹配与 RG | Henning–Lu–Murayama (2018)；Manohar EFT 讲义 | 不能在没有完整反项/算符混合矩阵时宣称得到完整 RG 解 |

#### 20.6 重要方法学声明与尚待核验事项

- 本报告采用的基本路线是：从模型拉氏量得到费曼规则 → 计算 UV 一圈两点函数 → 独立计算 EFT 图 → 在同一正则化、重整化约定下展开并比较 → 把解析的低能差值归入局域 Wilson 系数。
- $A_0$、$B_0$ 的具体定义（尤其是是否把 $\Delta_\epsilon$、$16\pi^2$ 因子吸收到函数中）必须在最终版本中固定。不同文献的记号不完全相同，不能混用。
- **本文件目前仍是阶段性报告。** 尤其第 17 节所记录的分步阈值表达式与前文部分候选导数系数的符号/有限常数约定，必须在统一的 $\Pi_{hs}$ 定义、拉氏量符号和匹配条件下重新逐项核对；参考文献本身不能替代这项模型专属复算。
- 在完成 IR 非解析项逐项抵消、portal 反项匹配、独立算符基底选择和完整反项矩阵之前，不能把候选 $C_D$ 或双阈值公式称为已经完全验证的最终结果。


---

### 21. 第二阶段：维数五算符的一圈 1PI Green 函数与维数六反项矩阵

> **状态声明：本节是可执行的计算框架和待核验清单，不代表全部 1PI 振幅及反项矩阵已经算完。** 在得到并核对各 Green 函数的 Dirac、群指标和动量系数之前，不应填写猜测的 anomalous-dimension matrix，也不应将下列“候选算符集合”称为最终不冗余基底。

#### 21.1 起点：未破缺相中的维数五算符

在重矢量类轻子被积分掉后，将有效相互作用写为

$$

\mathcal L_{\rm EFT}\supset C_{5,\ell}\,S_\ell\,\bar L_\ell H\ell_R+\mathrm{h.c.},
\qquad [C_{5,\ell}]=-1,

$$

其中按模型的规范荷约定，$S_\mu$ 与 $S_\tau$ 分别取 $S$ 或 $S^\dagger$；树级上通常有 $C_{5,\ell}\sim y_\ell\lambda_\ell/M_{E_\ell}$，但复共轭、整体符号和具体 flavor 标签必须由原始 UV 拉氏量逐项确定。

本阶段首先限定为 **一圈、两个 $O_5$ 插入、系数阶数 $C_5 C_5^*$、保留至维数六**。这是把问题变成有限且可复核计算的必要限定。若还要包含 $O_5$ 与所有规范、标量、Yukawa 相互作用的混合插入，必须另外列出耦合阶数并扩展图表，不能默认为已包括。

#### 21.2 在该阶数下优先计算的 1PI 外腿扇区

两个维数五顶点各含两个费米子场和两个标量场。对一圈、$C_5C_5^*$ 阶的四点函数，首先应计算下列扇区：

1. **四标量扇区**：$\Gamma^{(4)}_{H H^\dagger S S^\dagger}$，保留到外动量二阶。它是检验此前 $h$-$s$ 两点函数导数投影的关键补充，因为它直接约束含两个 $H$ 和两个 $S$ 场的规范不变导数算符组合。
2. **两费米子、两标量扇区**：所有由规范荷、手征性和 flavor 允许的 $\Gamma^{(4)}_{\bar L,\ell_R,H,S}$ 及其共轭/交叉排列。需保留外动量一次项，并检查是否产生带导数的费米子算符；通过运动方程约化时，必须把被消去的算符对 Yukawa、势能及四费米子算符的贡献一并带入。
3. **四费米子扇区**：$\Gamma^{(4)}_{\bar L,\ell_R,\bar\ell_R,L}$ 及规范荷允许的 flavor 变体。两个标量传播子连接两个 $O_5$ 顶点时可形成一圈图，因此不能只计算纯玻色子振幅后就声称得到完整的维数六反项集合。

若要得到严格规范协变的完整基底，还需根据上述算符的协变导数结构检查带外部规范场的 Green 函数，或使用背景场/泛函方法补齐规范协变结构。仅靠一个四标量振幅无法固定所有含导数算符及其冗余关系。

#### 21.3 四标量导数算符：先建候选集合，再做约化

在尚未使用分部积分（IBP）和运动方程（EOM）之前，四标量、两导数振幅可能投影到如下类型的规范不变结构：

$$

\begin{aligned}
Q_{HS}^{(1)}&=(H^\dagger H)(D_\mu S_\ell)^\dagger D^\mu S_\ell,\\
Q_{HS}^{(2)}&=(S_\ell^\dagger S_\ell)(D_\mu H)^\dagger D^\mu H,\\
Q_{HS}^{(3)}&=\partial_\mu(H^\dagger H)\,\partial^\mu(S^\dagger S),\\
Q_{HS}^{(4)}&=i(H^\dagger\overleftrightarrow{D_\mu}H)\,
                 i(S^\dagger\overleftrightarrow{D^\mu}S).
\end{aligned}

$$

这里的 $Q_{HS}^{(i)}$ **只是候选的过完备集合，不是已经证明独立的基底**。其中 $S$ 的协变导数必须使用目标 $U(1)_{L_\mu-L_\tau}$ 的规范场和正确电荷；若讨论低能破缺相，还需明确 Goldstone/径向模式的场参数化。

约化时至少执行以下操作：

- 对全导数做 IBP，并明确边界项不影响局域作用量；
- 用 $H$、$S$ 的经典 EOM 约化含 $D^2H$、$D^2S$ 的算符；
- 记录 EOM 替换所生成的势能、Yukawa/费米子以及四费米子算符；
- 检查复标量电流算符是否因规范荷、CP/共轭性质或模型的额外对称性而独立、消失或与其他算符联系；
- 固定场归一化、规范固定和算符基底约定后，才给每个独立算符编号。

特别注意：$\partial(H^\dagger H)\partial(S^\dagger S)$ 与 $(H^\dagger H)\Box(S^\dagger S)$ 可通过 IBP 互换；再使用 EOM 时会引入其他算符。因此不能同时把二者作为独立 Wilson 系数，也不能把破缺相二点函数得到的 $C_D$ 不加转换地认作某个唯一基底系数。

#### 21.4 1PI 振幅的统一提取步骤

对每一类外腿，采用同一套维数正规化和重整化约定：

1. 从完整未破缺相 EFT 的费曼规则生成所有拓扑和共轭图，注明每张图的 $C_5 C_5^*$、规范耦合、Yukawa 耦合及 flavor 因子。
2. 保留一般外动量。四标量扇区至少展开至 $p_i\cdot p_j$ 的一次项（总动量阶数二阶）；两费米子扇区保留所有独立的 $\slashed p_i$ 结构；四费米子扇区保留独立的 Lorentz/手征结构。
3. 对圈积分作 Dirac、规范群和 flavor 收缩；将张量积分约化为标量积分，明确写出 $1/\bar\epsilon$、有限部分和 $i0$ 规定。
4. 区分 UV 极点与 IR 极点。若用非零外动量或辅助质量分离 IR，必须在 UV 与 EFT 两边采用相同红外规约；不能把 IR 极点误认成 Wilson 系数的 UV 反项。
5. 将振幅的局域 UV 极点投影到选定的独立算符基底。投影前先做 IBP/EOM 约化，或先在过完备基底计算后显式施加约化矩阵；两种路线必须得到相同的物理结果。
6. 由局域极点读出反项矩阵，并用它导出 Wilson 系数的 RG 方程。对每个 flavor 分别计算后，再处理 $\mu$、$\tau$ 阈值不同的分段演化。

#### 21.5 反项矩阵的定义：先固定 convention

令选定的独立维数六算符列向量为 $\mathbf Q$，Wilson 系数为 $\mathbf C$。采用例如

$$

\mathbf Q^{\rm bare}=Z\,\mathbf Q^{\rm ren},\qquad
Z_{ij}=\delta_{ij}+\frac{1}{16\pi^2\bar\epsilon}\,z_{ij}^{(1)}+\cdots,

$$

并由 bare 拉氏量不依赖 $\mu$ 推导 $\mathbf C$ 的 RG 方程。注意有些文献把重整化矩阵定义在算符上，有些定义在 Wilson 系数上，矩阵转置和符号会随 convention 改变。因此正式结果必须同时报告：算符重整化约定、$Z$ 或 $\delta Z$ 的定义、$\bar\epsilon^{-1}$ 定义、算符基底顺序，以及是否已消去 EOM/evanescent operators。

若出现四费米子算符，还要说明所采用的 Dirac/Fierz 基底。若在 $d=4-2\epsilon$ 维使用 Fierz 恒等式，四维恒等式一般不能不加说明地直接用于发散部分；必要时应引入 evanescent operators 并说明其方案依赖性。

#### 21.6 与此前 $h$-$s$ 二点函数的交叉核验

完成未破缺相基底和反项矩阵后，才将结果代回

$$

H^0=(v_h+h)/\sqrt2,\qquad S=(v_s+s)/\sqrt2

$$

并对标量场做相同的规范化和场重定义。由独立算符基底导出的局域二点函数应具有

$$

\Pi_{hs}^{\rm local}(p^2)=A_{hs}^{\rm local}+B_{hs}^{\rm local}p^2+\cdots.

$$

然后分别核对：

- $A_{hs}$：与 portal 势能、质量参数重整化及其匹配条件相容；
- $B_{hs}$：与导数算符在同一基底下的 Wilson 系数相容；
- UV 与 EFT 的非解析/红外部分相同并在差值中抵消；
- 反项矩阵导出的显式 $\mu$ 依赖抵消低能圈图的尺度依赖，到所保留的阶数为止；
- 对不同的、但物理等价的 EOM/IBP 基底，最终的 on-shell 振幅一致。

这组检查比只对比一个 $\Pi'_{hs}(0)$ 更强：它能区分基底选择造成的系数变化与真正的物理不一致。

#### 21.7 方法参考文献（本阶段直接相关）

1. **R. Fang et al.**, “An Axial $U_A(1)_{L_\mu-L_\tau}$: UV Completion and Experimental Searches,” arXiv:2608.27258. https://arxiv.org/abs/2608.27258 。用于模型的 UV 拉氏量、规范荷和原始维数五相互作用；不是维数六反项矩阵的现成结果。
2. **B. Henning, X. Lu, and H. Murayama**, “One-loop Matching and Running with Covariant Derivative Expansion,” JHEP **01** (2018) 123, arXiv:1604.01019. https://arxiv.org/abs/1604.01019 。用于一圈匹配、重/轻场混合圈图区分和 anomalous-dimension/RG 的系统方法。
3. **A. Drozd, J. Ellis, J. Quevillon, and T. You**, “The Universal One-Loop Effective Action,” arXiv:1512.03003. https://arxiv.org/abs/1512.03003 。用于从重场积分得到维数六局域算符的一圈有效作用量方法；使用前须确认其适用条件是否覆盖当前含轻场的混合圈图。
4. **G. ’t Hooft and M. J. G. Veltman**, “Scalar One-Loop Integrals,” Nucl. Phys. B **153** (1979) 365–401. DOI: https://doi.org/10.1016/0550-3213(79)90605-9 。用于一圈标量积分及其发散/解析结构。
5. **A. V. Manohar**, “Introduction to Effective Field Theories,” arXiv:1804.05863. https://arxiv.org/abs/1804.05863 。用于 EFT 幂次计数、匹配、算符约化和 RG 的整体框架。

#### 21.8 本阶段交付物与完成判据

本阶段不能只交付一个矩阵。可复核的完整交付至少包括：

- [ ] 每个所需 1PI 扇区的图表清单和解析振幅；
- [ ] 每个振幅的 UV 极点、有限局域部分、IR 结构和 flavor 因子；
- [ ] 从候选过完备算符到独立基底的 IBP/EOM 约化关系；
- [ ] 明确 convention 的反项矩阵 $Z$ 或 $\delta Z$；
- [ ] 对应的 Wilson 系数 beta 函数和分段阈值演化；
- [ ] 从未破缺相维数六算符重建的 $h$-$s$ 两点函数，与此前 UV–EFT 投影结果逐项对照；
- [ ] 至少一个独立校验（符号计算、独立积分参数化或另一种匹配方法）。

在以上项目完成前，当前 $C_D$ 和双阈值 RG 表达式仍应标记为**两点函数投影下的候选结果**，不应升级为完整维数六匹配的最终结论。


#### 21.9 首个可显式计算的扇区：四标量 1PI 函数的 UV 极点

本节给出第一项具体的解析核验。把两个外标量先组合为复合源

$$

\Phi_{\ell i}\equiv S_\ell H_i,
\qquad \mathcal L_{\rm EFT}\supset -C_{5,\ell}\Phi_{\ell i}\bar L_{\ell i}\ell_R+\mathrm{h.c.}

$$

并在未破缺相、无质量轻费米子近似下计算 $\Phi_{\ell i}$-$\Phi_{\ell j}^\dagger$ 的一圈二点函数。这与原场变量中的四标量 1PI 振幅 $H S\to H S$ 是同一图，只是把两个外腿暂时视为复合源，便于提取动量结构。

每个 flavor 的 Dirac/手征迹为

$$

\mathrm{tr}\!\left[P_R\slashed k P_L(\slashed k+\slashed p)\right]
=2k\cdot(k+p).

$$

因此所需的标量积分分子可写为

$$

2k\cdot(k+p)=k^2+(k+p)^2-p^2.

$$

在维数正规化中，前两项给出无质量无尺度的 tadpole，因而为零；UV 极点来自最后一项：

$$

\left.\mu^{2\epsilon}\!\int\!\frac{d^dk}{(2\pi)^d}
\frac{2k\cdot(k+p)}{k^2(k+p)^2}\right|_{\rm UV}
=-\frac{i p^2}{16\pi^2\bar\epsilon},
\qquad d=4-2\epsilon.

$$

这里采用 $\int d^dk/(2\pi)^d$ 的 Minkowski 费曼积分约定，并定义 $1/\bar\epsilon=1/\epsilon-\gamma_E+\ln4\pi$。在顶点取 $-iC_{5,\ell}$ 的约定下，单 flavor 的 1PI 二点插入的 UV 极点为

$$

\left.i\Pi_{\Phi\Phi^\dagger}^{(\ell)}(p^2)\right|_{\rm UV}
=\frac{i|C_{5,\ell}|^2}{16\pi^2\bar\epsilon}\,p^2.

$$

故其所需局域反项在本节的符号约定下为

$$

\boxed{\delta\mathcal L_{\rm div}
=-\frac{1}{16\pi^2\bar\epsilon}
\sum_\ell |C_{5,\ell}|^2\,(D_\mu\Phi_{\ell i})^\dagger D^\mu\Phi_{\ell i},\qquad \Phi_{\ell i}=S_\ell H_i.}

$$

对 $i$ 求和是规范不变的双重态收缩；由于 $S_\mu$ 与 $S_\tau$ 可能分别为 $S$ 和 $S^\dagger$，两种 flavor 的交叉导数项符号须分别展开，不能不加区分地合并成同一个复合算符；$D_\mu\Phi_{\ell i}$ 必须使用 $S_\ell H_i$ 的总规范表示。这个结果给出了 **$C_5C_5^*$ 阶四标量导数扇区的首个 UV 极点**。它尚不是整个维数六反项矩阵，因为两费米子两标量和四费米子扇区还没有计算，也尚未把该组合约化到最终独立算符基底。

对每个 flavor，令 $S_\ell=S$ 或 $S^\dagger$（依原模型的规范荷约定）。展开相应复合算符可见它同时包含

$$

\begin{aligned}
(D_\mu(S_\ell H))^\dagger D^\mu(S_\ell H)={}&
(S_\ell^\dagger S_\ell)(D_\mu H)^\dagger D^\mu H
+(H^\dagger H)(D_\mu S_\ell)^\dagger D^\mu S_\ell\\
&+(D_\mu S_\ell)^\dagger S_\ell\,H^\dagger D^\mu H
+S_\ell^\dagger D_\mu S_\ell\,(D^\mu H)^\dagger H.
\end{aligned}

$$

这说明：如果只保留 $\partial(H^\dagger H)\partial(S^\dagger S)$ 这一项来拟合 $h$-$s$ 的 $p^2$ 系数，会漏掉同一规范不变组合中的对角动能项和交叉导数项。破缺相二点函数的投影必须在完整算符组合展开、波函数归一化和 EOM/IBP 约化之后再比较。

**核验边界：** 上述 UV 极点的整体符号依赖所声明的 $i\Pi$、顶点和 Minkowski 积分约定；在将它与既有文档中的 $\Pi_{hs}$ 公式比较前，必须把两边统一到同一 convention。有限部分还需保留外动量与 IR 规约，不能从该 UV 极点单独推断此前候选 Wilson 系数的有限常数 $-2/3$。

#### 21.10 四标量扇区的完整非局域动量依赖（本轮新增）

上一节只抽取了 UV 极点。现在保留外部复合动量，取非零、类空的 $p^2<0$ 以避免把无尺度积分中的 UV/IR 极点混在一起。定义

$$

B_0(p^2;0,0)=\frac{1}{\bar\epsilon}+2-\ln\!\frac{-p^2-i0}{\mu^2}+O(\epsilon),
\qquad \frac1{\bar\epsilon}=\frac1\epsilon-\gamma_E+\ln4\pi.

$$

使用分子恒等式

$$

2k\cdot(k+p)=k^2+(k+p)^2-p^2,

$$

前两项在维数正规化中为无尺度积分；于是完整的圈积分（而非只取 UV 部分）为

$$

\begin{aligned}
I(p^2)&=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{2k\cdot(k+p)}{(k^2+i0)((k+p)^2+i0)}\\
&=-\frac{i p^2}{16\pi^2}\left[\frac1{\bar\epsilon}+2-\ln\!\frac{-p^2-i0}{\mu^2}\right]+O(\epsilon).
\end{aligned}

$$

因此，在 21.9 已声明的顶点与 $i\Pi$ convention 下，复合源二点插入可写成

$$

\left.i\Pi_{\Phi\Phi^\dagger}^{(\ell)}(p^2)\right|_{C_5C_5^*}
=\frac{i|C_{5,\ell}|^2p^2}{16\pi^2}
\left[\frac1{\bar\epsilon}+2-\ln\!\frac{-p^2-i0}{\mu^2}\right],

$$

其中 flavor 和 SU(2) 指标的收缩按 $\Phi_{\ell i}=S_\ell H_i$ 理解。此式是该复合源通道的结果；若把它展开成原始四标量振幅，必须对外腿的排列/交叉通道逐一求导，不能把同一通道的表达式直接当成所有外腿排列的总振幅。

这个结果带来三个明确结论：

1. **UV 极点**正是 $p^2/\bar\epsilon$，与 21.9 的局域反项相符。
2. **有限非局域部分**包含 $-p^2\ln(-p^2/\mu^2)$。它属于轻场 EFT 圈图的动量依赖，不能整体吸收到局域 Wilson 系数中；匹配时应在 UV 与 EFT 的相同红外规约下相减。
3. **有限常数 2 不是此前候选系数中的 $-2/3$**。二者来自不同投影/积分问题，不能直接等同；必须将 UV 完整理论、EFT 图、局域算符基底及场重整化放到同一方案中，才能判断最终匹配常数。

#### 21.11 两费米子—两标量扇区：主积分的 UV 结构

接下来考虑两个 $O_5$ 顶点贡献的 $\bar L,\ell_R,H,S$ 四点函数。此处只讨论 $C_5C_5^*$ 阶、一个内部轻费米子线和一个内部标量线构成的一圈拓扑；规范相互作用插入、标准模型 Yukawa 插入以及其他耦合阶数暂不纳入。

按外腿排列，内部轻费米子传播子给出 $\slashed k$，内部无质量标量传播子给出 $1/(k+q)^2$。其向量主积分可由 Feynman 参数直接化简：

$$

\begin{aligned}
J^\mu(q)&=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{k^\mu}{(k^2+i0)((k+q)^2+i0)}\\
&=-q^\mu\int_0^1 dx\,x\,
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{1}{[\ell^2+x(1-x)q^2+i0]^2}\\
&=-\frac{i q^\mu}{32\pi^2}
\left[\frac1{\bar\epsilon}-\ln\!\frac{-q^2-i0}{\mu^2}+2\right]
+O(\epsilon),
\end{aligned}

$$

其中最后一行采用与 21.10 相同的积分 convention，并取 $q^2<0$。所以这一类图的局域 UV 张量必与外动量的一次项成正比，结构为 $\slashed q/\bar\epsilon$，对应维数六的带导数费米子—标量算符，而不是无导数的维数五算符重整化。

**本节暂不把该主积分单独写成最终算符反项系数。** 原因是完整四点函数还需要固定每种外腿排列的手征投影、内部线的动量流向、复共轭顶点的符号和组合因子；随后还要将 $\slashed q$ 结构投影到选定的费米子导数算符，并用 EOM/IBP 约化。仅凭一个张量主积分就宣称得到完整 $Z_{ij}$ 会是不严谨的。下一步应逐个画出允许的外腿排列，列出每个图的顶点因子与 flavor/规范荷，再汇总其 UV 极点。

#### 21.12 两费米子—两标量扇区：逐类内部收缩与局域结构

本节把 21.11 的主积分落实到可区分的内部收缩。写

$$

\mathcal L_5=-C_{5,\ell}\,\bar L_{\ell i}\ell_R\,H_iS_\ell+\text{h.c.},
\qquad S_\ell\in\{S,S^\dagger\},

$$

并只保留 $C_{5,\ell}C_{5,\ell}^*$ 阶。一个 $O_5$ 顶点与一个 $O_5^\dagger$ 顶点之间，各有两类可收缩的费米子线和两类可收缩的标量线：

- 费米子线：$\ell_R$--$\bar\ell_R$，或 $L$--$\bar L$；
- 标量线：$H$--$H^\dagger$，或 $S_\ell$--$S_\ell^\dagger$。

因此，忽略外腿交叉记号后，最小的拓扑清单有 $2\times2=4$ 类。每类图的积分都归结为 21.11 的向量泡积分；但它们的规范指标结构并不完全相同，不能只用一个 $(H^\dagger H)(\bar L i\slashed D L)$ 代表全部图。

##### A. 内部线收缩与外部局域结构

| 内部费米子线 | 内部标量线 | 剩余外部标量 | 剩余外部费米子 | 允许出现的导数结构（未约化） |
|---|---|---|---|---|
| $\ell_R$--$\bar\ell_R$ | $H$--$H^\dagger$ | $S_\ell,S_\ell^\dagger$ | $\bar L,L$ | $(S_\ell^\dagger S_\ell)\bar L\,i\slashed D L$ |
| $\ell_R$--$\bar\ell_R$ | $S_\ell$--$S_\ell^\dagger$ | $H,H^\dagger$ | $\bar L,L$ | $(\bar L_i H_i)\,i\slashed D\,(H_j^\dagger L_j)$ 及其 IBP 等价形式 |
| $L$--$\bar L$ | $H$--$H^\dagger$ | $S_\ell,S_\ell^\dagger$ | $\bar\ell_R,\ell_R$ | $(S_\ell^\dagger S_\ell)\bar\ell_R\,i\slashed D\ell_R$ |
| $L$--$\bar L$ | $S_\ell$--$S_\ell^\dagger$ | $H,H^\dagger$ | $\bar\ell_R,\ell_R$ | $(H^\dagger H)\bar\ell_R\,i\slashed D\ell_R$ |

这里的表是**拓扑和张量结构清单**，不是最终独立算符基底。尤其第二行保留了 $\bar L_i H_i H_j^\dagger L_j$ 的指标连接；在一般的 $SU(2)_L$ 算符约化中，不能在没有做指标恒等式和 EOM/IBP 分析前，擅自将它与单纯的 $(H^\dagger H)\bar L i\slashed D L$ 等同。

##### B. 每类图的 UV 主部

对每个内部轻费米子—无质量标量泡图，采用 21.11 的动量约定，积分张量为

$$

J^\mu(q)=
-\frac{iq^\mu}{32\pi^2}
\left[\frac1{\bar\epsilon}
-\ln\frac{-q^2-i0}{\mu^2}+2\right].

$$

故 UV 主部为

$$

J^\mu(q)\big|_{\rm UV}=-\frac{iq^\mu}{32\pi^2\bar\epsilon}.

$$

乘上内部费米子传播子的 $\gamma_\mu$ 后，每个拓扑的局域发散必然正比于

$$

\frac{|C_{5,\ell}|^2}{32\pi^2\bar\epsilon}\,
\bar\psi\,\slashed q\,\psi,

$$

其中 $\psi=L_\ell$ 或 $\ell_R$，而 $q$ 是由该图外腿动量流向决定的外部动量组合。这个结论固定了**动量阶数、圈因子及每个拓扑的主积分 UV 系数**；但完整振幅的整体符号仍须将每一图的两个顶点、两条传播子和费米子流向统一代入后确定，所以此处不把绝对值结构冒充成最终的 $\delta Z_{ij}$。

##### C. 为什么不能马上把它们写成最终 Wilson 系数

从 $\bar\psi\slashed q\psi$ 到局域算符时，$q$ 要拆成外部费米子与标量动量。于是同一图可产生形如

$$

(S_\ell^\dagger S_\ell)\bar L i\slashed D L,\qquad
(\bar L H)i\slashed D(H^\dagger L),\qquad
(H^\dagger H)\bar\ell_R i\slashed D\ell_R

$$

等项。它们可通过分部积分（IBP）、费米子运动方程（EOM）和场重定义相互转换；使用 EOM 时还会引入与其他 Yukawa 耦合相关的算符。因此必须先指定完整的独立算符基底及 EOM 约定，再谈矩阵元素的数值。

本阶段可确认的结果是：

1. $C_5C_5^*$ 阶确实产生两费米子—两标量的导数型局域 UV 发散；
2. 四种内部收缩在 $SU(2)_L$ 指标结构上至少要区分表中所列的两类左手结构和两类右手结构；
3. 主积分的 $1/\bar\epsilon$ 系数已知，但完整图的相对符号、外腿排列求和及基底约化尚未全部完成；
4. 因此尚不能据此报告完整反项矩阵或 anomalous-dimension 矩阵。

#### 21.13 本轮结论与下一项计算

本轮将 21.11 的积分推进到四类内部收缩，并明确列出了它们对应的未约化局域导数结构。下一步需要做的不是继续猜系数，而是固定一套完整的未破缺相维数六基底，逐图写出带规范指标的 1PI 振幅，求和后再用 IBP/EOM 约化。尤其需要保留 $S_\ell=S$ 与 $S_\ell=S^\dagger$ 的 flavor 区别；两者的模平方结构相同，但交叉导数和带电规范流项的展开不能直接混同。

**状态标记：** 四标量复合源通道的 UV 极点与泡积分已写出；两费米子—两标量通道已完成最小拓扑分类和主积分 UV 结构；完整四点振幅、四费米子扇区、不冗余基底、反项矩阵、RG 与有限匹配常数 $-2/3$ 的核验仍未完成。

#### 21.14 四费米子扇区：双标量泡图的 UV 极点

四费米子扇区比两费米子—两标量扇区更直接：在一个 $O_{5,\ell}$ 和一个 $O_{5,\ell}^\dagger$ 顶点上，将 $H$--$H^\dagger$ 与 $S_\ell$--$S_\ell^\dagger$ 分别收缩为两条内部标量线，四条费米子腿全部留在外部。该图是一个双标量泡图，圈积分为

$$

I_0(q^2)=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{1}{(k^2+i0)((k+q)^2+i0)}
=\frac{i}{16\pi^2}\left[
\frac1{\bar\epsilon}-\ln\frac{-q^2-i0}{\mu^2}
\right]+O(\epsilon),

$$

这里取 $q^2<0$ 以将 UV 极点与零外动量时可能混入的 IR 极点分开。

外部自旋结构由两个原始维数五顶点直接给出，因此局域四费米子结构是

$$

Q_{4f}^{(\ell)}=(\bar L_{\ell i}\ell_R)(\bar\ell_R L_{\ell i}),

$$

其规范指标由 $SU(2)_L$ 双重态指标 $i$ 收缩。每个顶点各带一个 $C_{5,\ell}$ 或其复共轭，故系数阶数为 $|C_{5,\ell}|^2$，维数为 $-2$，与维数六四费米子算符相匹配。

在不把费米子外腿重排、也不先做 Fierz 变换的原始标量流基底中，图的 UV 发散必然正比于

$$

\frac{|C_{5,\ell}|^2}{16\pi^2\bar\epsilon}
(\bar L_{\ell i}\ell_R)(\bar\ell_R L_{\ell i}).

$$

这里先只记录其**系数的 UV 极点大小与算符结构**。最终有效作用量反项的正负号必须和完整费曼规则、外部费米子排序以及 $i\mathcal M$ 的定义统一后再固定；若改用矢量流基底，还要明确 Fierz 约定。由于后续可能需要有限匹配，不能在 $d=4-2\epsilon$ 中无说明地把四维 Fierz 恒等式用于全部有限项；必要时应指定 evanescent-operator 方案。

此图还说明一个重要点：**两次维数五算符插入不只产生导数型算符，也会产生无导数四费米子维数六算符。** 因而如果只从 $h$--$s$ 二点函数反推 Wilson 系数，就不可能重建完整的维数六反项矩阵。

**本节边界：** 已提取双标量泡图的积分、UV 极点阶数及原始四费米子结构；尚未完成外部费米子置换的全套振幅、所有味道交叉项的选择规则、Fierz/evanescent 基底处理和与其他维数六算符的矩阵混合。因此这仍是四费米子扇区的首个拓扑结果，而不是完整 anomalous-dimension 矩阵。

### 22. 后续推进：四费米子双标量泡图的完整局域极点（条件性结果）

本节在固定约定下把上一节的待定因子推进一步。它只处理由两个维数五顶点产生的四费米子双标量泡图，不代表整个维数六反项矩阵已经完成。

#### 22.1 固定算符与费曼规则

对味道标签 $\alpha$，写

$$

\mathcal L_5\supset-C_{5,\alpha}S_\alpha H_i\bar L_{\alpha i}\ell_{\alpha R}+\mathrm{h.c.},

$$

并选定四费米子算符

$$

Q_{S,\alpha}=(\bar L_{\alpha i}\ell_{\alpha R})(\bar\ell_{\alpha R}L_{\alpha i}),
\qquad
\mathcal L_{\rm EFT}\supset C_{S,\alpha}Q_{S,\alpha}.

$$

约定每个维数五顶点为 $-iC_{5,\alpha}$ 及其共轭 $-iC^*_{5,\alpha}$，复标量传播子为 $i/(k^2+i0)$，且用

$$

\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{1}{(k^2+i0)((k+q)^2+i0)}
=\frac{i}{16\pi^2}\left[\frac1{\bar\epsilon}
-\ln\frac{-q^2-i0}{\mu^2}+2\right]+O(\epsilon)

$$

定义泡积分。这里取 $q^2\ne0$，避免把无尺度积分误判为没有 UV 发散。

#### 22.2 单一允许收缩的 UV 极点

在给定外腿排列 $(\bar L_{\alpha i},\ell_{\alpha R},\bar\ell_{\alpha R},L_{\alpha i})$ 下，两个顶点之间分别以 $H$-$H^\dagger$ 和 $S_\alpha$-$S_\alpha^\dagger$ 传播子连接。由于两条内部线是不同种类的复标量，该指定拓扑没有由交换两条相同内部线带来的额外 $1/2$ 因子。

两个顶点因子与两条传播子的 $i$ 因子相乘：

$$

(-iC_{5,\alpha})(-iC^*_{5,\alpha})\,i^2
=|C_{5,\alpha}|^2.

$$

再乘以上述环积分，得到这个固定外腿排列下的局域 UV 部分

$$

\left.i\mathcal M_{\rm bubble}\right|_{\rm UV}
=\frac{i|C_{5,\alpha}|^2}{16\pi^2\bar\epsilon}
\,Q_{S,\alpha},

$$

其中右侧的 $Q_{S,\alpha}$ 表示相应外部自旋量双线性乘积，而不是把算符本身再次当作额外顶点因子。按此明确约定，单个该拓扑的极点系数为正的 $+1$。

若反项拉氏量定义为 $\delta\mathcal L=\delta C_{S,\alpha}Q_{S,\alpha}$，则其四点顶点为 $i\delta C_{S,\alpha}$，抵消该图的极点要求

$$

\boxed{\delta C_{S,\alpha}\big|_{\text{该拓扑}}
=-\frac{|C_{5,\alpha}|^2}{16\pi^2\bar\epsilon}.}

$$

这个结论严格限定于上述拉氏量符号、外腿排序与指定收缩。若将算符换成矢量流基底，须先按 Fierz 关系变换算符和系数；不能把该系数原封不动地贴到另一个基底上。

#### 22.3 味道选择规则

更一般地，两个顶点 $O_{5,\alpha}$ 与 $O^\dagger_{5,\beta}$ 可产生形式为

$$

Q_{\alpha\beta}=(\bar L_{\alpha i}\ell_{\alpha R})
(\bar\ell_{\beta R}L_{\beta i})

$$

的四费米子结构，其耦合乘积为 $C_{5,\alpha}C^*_{5,\beta}$。但该图存在的必要条件是两个顶点所含的复标量字段能通过非零传播子配对。若定义 $S_\alpha=S$ 或 $S^\dagger$，则必须要求顶点一的 $S_\alpha$ 与顶点二共轭相互作用中的字段互为复共轭；若两端同为 $S$ 或同为 $S^\dagger$，在没有异常 $\langle SS\rangle$ 型传播子时，该收缩为零。Higgs 双重态也必须按 $H$-$H^\dagger$ 配对。

因此，不能在没有逐味道检查 $S_\alpha$ 定义的情况下，直接把所有 $C_{5,\alpha}C^*_{5,\beta}$ 都列入反项矩阵。上述选择规则只判断该双标量泡图是否允许，并不排除 UV 理论中由其他相互作用产生的交叉味道算符。

#### 22.4 Fierz 基底与有限项的边界

在四维物理算符空间中，

$$

Q_{S,\alpha}=-\frac12
(\bar L_{\alpha i}\gamma^\mu L_{\alpha i})
(\bar\ell_{\alpha R}\gamma_\mu\ell_{\alpha R}).

$$

因此，如果用右侧矢量流算符作为基底，反项系数须按同一关系变换。此处仅为单圈物理 UV 极点的基底转换提示；若要求有限匹配系数，必须进一步指定 $d=4-2\epsilon$ 下的 evanescent operators 和重整化方案，因为四维 Fierz 恒等式在 $d\ne4$ 时不能无条件作为完整算符恒等式使用。

#### 22.5 本节的核验边界

本节把单一四费米子双标量泡图在所声明约定下的相对因子固定为 1，并给出相应反项抵消条件；但仍需在完整计算中核对：

1. 论文原始 UV 拉氏量中的 $S$/$S^\dagger$ 及耦合共轭定义是否与本节记号完全一致；
2. 对所选 1PI 有效作用量外腿顺序，是否还有其他独立的非等价图或由同一有效作用量泛函导数产生的排列；
3. 完整基底中是否需要额外的规范不变四费米子算符，以及 EOM/Fierz 约化后它们的混合；
4. EFT 泡图与完整 UV 振幅的 IR 部分是否一致，并在匹配差值中抵消。

所以本节是**一个明确约定下的单拓扑结果**，不是最终 $Z_{ij}$、异常维数矩阵或有限阈值匹配。候选导数 Wilson 系数中的有限常数 $-2/3$ 仍未由本节验证。

## 22. 两费米子—两标量通道：Wick 收缩分类与统一基底投影（阶段性）

### 22.1 起点与计算范围

在未破缺相，对单一味道写

$$

O_{5,\ell}=C_{5,\ell}S_\ell H_i\bar L_{\ell i}\ell_R,
\qquad O_{5,\ell}^\dagger=C_{5,\ell}^*S_\ell^*H_i^*\bar\ell_R L_{\ell i}.

$$

本节只研究 $O_5 O_5^\dagger$ 阶数、无轻场质量插入的 1PI 图。由于每个顶点含一条左手和一条右手费米子腿，以及两种标量腿，产生“两费米子、两标量”外腿时，需要跨顶点收缩一条内部费米子线和一条内部标量线。以下分类是拓扑/场内容分类，不等同于已经完成所有动量依赖振幅的求和。

### 22.2 允许的外部费米子手征组合
在未破缺相、无左右手费米子质量插入时，传播子只能连接同一 Dirac 场的场与共轭场。因此，非零的两外部费米子选择为：

1. 外部 $\bar L_\ell,L_\ell$，内部费米子线由 $\ell_R,\bar\ell_R$ 收缩；
2. 外部 $\bar\ell_R,\ell_R$，内部费米子线由 $L_\ell,\bar L_\ell$ 收缩。

把一个顶点的 $\bar L$ 与另一个顶点的 $\bar\ell_R$ 同时作为外腿，会留下两个不构成质量less传播子的内部费米子场，故该简单收缩为零；若加入质量插入或额外相互作用，需另行计数，不能混入本节的无质量结果。

### 22.3 标量内部线的两种选择

每个顶点均含 $S_\ell$ 与 $H_i$。对每一种允许的外部费米子手征组合，有两种基本标量安排：

- 外部标量为 $H,H^\dagger$，内部标量为 $S_\ell,S_\ell^\dagger$；
- 外部标量为 $S_\ell,S_\ell^\dagger$，内部标量为 $H,H^\dagger$。

因此，按外部费米子手征结构与外部标量种类分类，得到四类基本 2f2s 通道。每一类仍须固定外腿动量、规范指标与费米子箭头方向，才能写出唯一的解析振幅。若不同味道使用 $S$ 与 $S^\dagger$，应从实际复标量传播子 $\langle S S^\dagger\rangle$ 判断是否允许收缩；不能把不匹配的复标量场直接连线。

### 22.4 对应的过完备导数算符

由场内容和维数可先列出以下候选结构（规范指标按需要收缩）：

$$

Q_{L H}=(H^\dagger H)\,\bar L_\ell i\!\not\!D L_\ell,
\qquad
Q_{L S}=(S_\ell^\dagger S_\ell)\,\bar L_\ell i\!\not\!D L_\ell,

$$

$$

Q_{R H}=(H^\dagger H)\,\bar\ell_R i\!\not\!D\ell_R,
\qquad
Q_{R S}=(S_\ell^\dagger S_\ell)\,\bar\ell_R i\!\not\!D\ell_R.

$$

这里的写法是用于组织投影的候选项，不代表它们在 EOM/IBP 约化后都是独立算符。尤其是 $Q_{LH}$、$Q_{RH}$ 可通过轻场运动方程与含 Higgs 的 Yukawa 结构发生联系；对 $Q_{LS}$、$Q_{RS}$ 的约化也必须在完整 EFT 相互作用和所选算符基底中完成。不能在尚未写出完整图的动量分子前，直接为这四项分别指定数值系数。

### 22.5 主积分只能固定积分结构，不能单独固定反项系数

代表性的向量积分为

$$

J^\mu(q)=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{k^\mu}{(k^2+i0)((k+q)^2+i0)}.

$$

洛伦兹协变性给出 $J^\mu(q)=q^\mu A(q^2)$。在此前的积分约定下，其 UV 部分正比于 $q^\mu/(32\pi^2\bar\epsilon)$，具体的 $i$ 与符号依赖积分定义。完整振幅还包含费米子传播子的 $\slashed k$、手征投影、顶点符号、外腿排列以及标量种类的组合因子；所以不能把 $J^\mu$ 的系数直接认作某个 $Q_{LH}$ 或 $Q_{RS}$ 的反项系数。

严谨提取流程是：对每一类收缩保留外部动量，先求分子并约化到 $\slashed p$ 结构；求和全部非等价图后抽取 UV 极点；再用 IBP/EOM 与场重定义映射到选定的不冗余基底。无尺度积分为零不能被解释为 UV 极点不存在，必须用非零外部动量或一致的 IR 调节分离 UV/IR。

### 22.6 与四费米子通道的统一投影

四费米子泡图的外腿场内容为 $(\bar L\ell_R)(\bar\ell_R L)$，而 2f2s 图产生带导数的费米子双线性。两者是不同的外腿扇区，应分别投影：

- 2f2s：投影到带导数的费米子—标量算符及其 EOM 等价项；
- 4f：投影到独立四费米子基底，并处理四维 Fierz 关系及维数正规化中的 evanescent operators。

两者可放入同一个全局重整化问题的算符清单和混合矩阵框架，但不存在把两个不同外腿扇区的 UV 极点直接相加成一个系数的步骤。只有当一个具体裸算符的反项确实从多个外腿扇区的 1PI 投影共同约束时，才按该算符的列/行组织相应矩阵元素。

### 22.7 本节结论与未完成项

本节完成了无质量 $O_5O_5^\dagger$ 阶数下 2f2s 外腿的基本手征/标量收缩分类，并列出待约化的导数算符候选集。**尚未完成**：逐图完整动量分子、全部图的相对符号和组合因子、IBP/EOM 不冗余基底、明确数值的反项矩阵以及 beta 函数。故本节不报告未经完整振幅支持的 Wilson 系数，也不把候选有限常数 $-2/3$ 当成已验证结果。

## 23. 两费米子—两标量通道：逐拓扑的动量积分与可确定的 UV 结构

本节继续推进 2f2s 扇区，但严格区分“积分的 UV 极点已算出”和“完整图的反项系数已确定”。当前 EFT 顶点取为

$$

\mathcal L_5=-C_{5,\ell}S_\ell H_i\bar L_{\ell i}\ell_R+\mathrm{h.c.}

$$

每个顶点含一个 $H$、一个 $S_\ell$ 和一条左、右手轻子线。对外部费米子为 $\bar L,L$ 的振幅，若外部两标量取 $H,H^\dagger$，则内部标量线是 $S_\ell,S_\ell^\dagger$；若外部两标量取 $S_\ell,S_\ell^\dagger$，则内部标量线是 $H,H^\dagger$。混合外部标量 $H,S$ 的这一类简单配对不能将剩余标量线互相收缩，因为它们不是同一种复标量场。右手外部费米子通道同理。

### 23.1 一般质量下的向量积分

取内部费米子无质量、内部标量质量为 $m_X$，定义

$$

J^\mu(q;m_X^2)=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{k^\mu}{(k^2+i0)((k+q)^2-m_X^2+i0)}.

$$

用 Feynman 参数

$$

\frac1{AB}=\int_0^1dx\,\frac1{[xA+(1-x)B]^2}

$$

并平移积分变量后，分子变为一个奇函数项加上与 $q^\mu$ 成正比的项。奇函数项在维数正规化下为零；UV 极点只需保留参数积分中的线性项：

$$

J^\mu\big|_{\rm UV}
=-q^\mu\int_0^1dx\,x\,
\left[\frac{i}{16\pi^2\bar\epsilon}\right]
=-\frac{i q^\mu}{32\pi^2\bar\epsilon}.

$$

这里使用的约定是传播子分母如上、积分测度为 $d^dk/(2\pi)^d$。如果将分母写成 $(k-q)^2-m_X^2$，则相应的外部动量方向和符号必须同步变换。UV 极点与 $m_X$ 无关；质量影响有限部分和红外行为。

### 23.2 费米子分子与局域动量结构

内部轻子传播子带来 $i\slashed{k}/(k^2+i0)$，因此上述向量积分在振幅中变成 $\slashed q$ 结构。对一个给定外腿排序，圈图的 UV 结构必为

$$

\mathcal A^{\rm UV}_{2f2s}
\sim \frac{|C_{5,\ell}|^2}{32\pi^2\bar\epsilon}
\,\bar u(p')\slashed q\,P_{L/R}u(p),

$$

其中 $P_{L/R}$ 由外部轻子手征性决定；此处的 $\sim$ 表示尚未包含顶点、传播子、外腿排序和可能的多重收缩带来的整体符号及组合因子。因此该式只确定局域发散的动量阶数与手征形式，不能直接作为最终 Wilson 系数。

相应的未约化局域结构可写成

$$

(H^\dagger H)\bar L i\!\not\!D L,\quad
(S_\ell^\dagger S_\ell)\bar L i\!\not\!D L,

$$

以及右手轻子对应项

$$

(H^\dagger H)\bar\ell_R i\!\not\!D\ell_R,\quad
(S_\ell^\dagger S_\ell)\bar\ell_R i\!\not\!D\ell_R.

$$

这些表达式是 EOM/IBP 约化前的候选结构。特别地，若轻子运动方程为

$$

i\!\not\!D L_\ell= y_\ell H\ell_R+\cdots,

$$

则 $(S^\dagger S)\bar L i\!\not\!D L$ 可与含 $(S^\dagger S)\bar L H\ell_R$ 的 Yukawa 型维数六算符联系；但 EOM 替换必须在完整的场内容、共轭约定和算符基底下进行，不能单独把某一个导数项设为零。

### 23.3 Wick 收缩计数的边界

对指定的外部场种类，每个顶点的标量腿必须分别满足：一条外部标量腿，以及一条与另一顶点同种类、共轭取向相容的内部标量腿。费米子腿则由 $O_5$ 与 $O_5^\dagger$ 的手征结构连接。交换两个外部标量标签可能只是同一振幅的外腿置换，不应自动当作新图再乘 2；反之，若外部动量/物种不同而产生非等价排列，则必须逐个保留。最终因子应从带标记外腿的 Wick 收缩直接计数。

本次已明确各类拓扑的内部标量选择，并求出一般内部标量质量下向量积分的 UV 极点；**尚未完成**带完整外腿标签的全部 Wick 收缩求和，故还没有给出四个候选导数结构的最终数值反项系数。后续应固定动量流、逐一写出费曼振幅，再将求和结果投影到 EOM/IBP 约化后的独立基底。

### 23.4 与四费米子扇区合并时的规则

2f2s 扇区的极点用于确定含两个费米子、两个标量的算符反项；4f 扇区的极点用于确定四费米子算符反项。它们是不同的外部场扇区，不能把数值极点相加。统一处理意味着将它们放入同一个算符清单，并在各自的 1PI 投影条件下求对应反项矩阵元素。有限匹配还需在 UV 与 EFT 两侧使用相同的 IR 方案、重整化方案以及四费米子 evanescent-operator 约定。

## 第 24 节：两费米子—两标量通道的动量路由与投影（阶段性）

### 24.1 先固定一个可复核的拓扑

从

$$

\mathcal L_5=-C_{5,\ell}S_\ell H_i\bar L_{\ell i}\ell_R+\mathrm{h.c.}

$$

取一个 $O_{5,\ell}$ 顶点和一个 $O_{5,\ell}^\dagger$ 顶点。若外腿为 $\bar L,L,H,H^\dagger$，则两条外部费米子腿为左手双重态，两个外部 Higgs 腿分别来自两个顶点；内部线是一个右手轻子传播子和一个 $S_\ell$-$S_\ell^\dagger$ 标量传播子。该拓扑的耦合因子为 $|C_{5,\ell}|^2$。若外腿为 $\bar L,L,S_\ell,S_\ell^\dagger$，则内部标量换成 Higgs 分量，内部费米子仍由右手轻子传播子连接。右手外部费米子通道则相应由内部左手轻子传播子连接。

混合外部标量 $H$ 与 $S$ 的情形不能仅用这两个顶点构成同样的单圈拓扑：两顶点剩余的内部标量种类不匹配，除非模型另有允许的标量混合/相互作用插入。因此不把它当作本阶自动存在的收缩。

### 24.2 带质量标量的向量积分：保留完整参数表达式

为避免只使用 UV 极点而丢失动量依赖，定义

$$

J^\mu(q;m_X^2)=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{k^\mu}{(k^2+i0)((k+q)^2-m_X^2+i0)}.

$$

使用 Feynman 参数并平移积分变量，可写成（与上面分母和动量路由一致）

$$

J^\mu(q;m_X^2)= -\frac{i q^\mu}{16\pi^2}
\int_0^1 dx\,(1-x)
\left[\frac1{\bar\epsilon}
-\ln\frac{(1-x)m_X^2-x(1-x)q^2-i0}{\mu^2}\right]
+O(\epsilon),

$$

其中有限部分的对数需按所采用的 Minkowski 积分约定解析延拓。积分 $\int_0^1(1-x)dx=1/2$，故

$$

J^\mu\big|_{\rm UV}=-\frac{i q^\mu}{32\pi^2\bar\epsilon}.

$$

这验证了先前得到的 UV 极点，并给出质量和外部动量进入有限部分的参数积分形式。若改用 $(k-q)^2-m_X^2$ 的分母，必须同步改动 $q$ 的定义；不能单独照搬符号。

### 24.3 四点振幅的分子结构与外部动量

内部无质量手征费米子传播子提供 $i\slashed{k}/(k^2+i0)$。因此在指定外腿排列下，圈积分的张量部分必化为 $\slashed q$ 乘以标量参数积分。对外部左手轻子通道，振幅可参数化为

$$

i\mathcal M_{\bar L L H H^\dagger}^{\rm 1PI}
=\mathcal N_{\ell}\,|C_{5,\ell}|^2\,
\bar u_L(p')\slashed q\,u_L(p)\,
\frac{1}{16\pi^2}
\left[\frac{1}{2\bar\epsilon}+\text{finite}(q^2,m_X^2)\right],

$$

其中 $\mathcal N_\ell$ 暂记顶点 $i$ 因子、费米子流方向、外腿排序及规范指标收缩带来的总符号/组合因子；在完成带标记外腿的全部 Wick 收缩前，不给它擅自赋值。右手通道有对应的手征投影。

重要的是，$q$ 不是独立可任意指定的物理量，而是由外部费米子和标量腿的动量守恒决定。把 $\slashed q$ 改写为外部费米子动量后，才能匹配到协变导数算符；若再使用轻子 EOM，结果会转成 Yukawa 型维数六算符及其他基底项。因此仅凭积分的 $q^\mu$ 系数，不能直接宣布 $(H^\dagger H)\bar L i\!\not D L$ 的最终 Wilson 系数。

### 24.4 当前可以确定与不能确定的结论

**可确定：**

1. 在 $O_5O_5^\dagger$ 阶，$\bar L,L,H,H^\dagger$ 通道有内部右手轻子和复标量的泡图；$\bar L,L,S,S^\dagger$ 通道则有内部右手轻子和 Higgs 分量的泡图。
2. 指定动量路由下，向量积分 UV 极点为 $-i q^\mu/(32\pi^2\bar\epsilon)$，不依赖内部标量质量。
3. 局域极点具有一个外部动量和一个手征费米子双线性的结构，属于导数型 2f2s 算符扇区；EOM/IBP 约化会影响其基底表达。

**尚不能确定：**

1. 所有带标记外腿排列求和后的整体符号与组合因子 $\mathcal N_\ell$。
2. 完整 1PI 四点函数投影后的数值反项系数。
3. EOM/IBP 约化后的独立算符系数、与四费米子扇区合并后的反项矩阵，以及 RG 方程。
4. UV–EFT 有限匹配系数及此前候选常数 $-2/3$。

后续计算应先明确目标论文 UV 拉氏量中的每个味道使用 $S$ 还是 $S^\dagger$、所有耦合的共轭约定和标量势，再按固定外腿顺序逐图求和；在此之前，任何未经验证的整体数值因子都应保留为待定量。

## 第 25 节：2f2s 算符基底的必要修正——不能只保留费米子动能型算符

### 25.1 为什么此前候选基底不够完整

第 22–24 节把

$$

(H^\dagger H)\bar L i\!\not\!D L,\qquad
(S^\dagger S)\bar L i\!\not\!D L

$$

及右手轻子对应项列作未约化候选结构。这些结构可以用于组织动量展开，但**不能据此认定它们构成完整的独立 2f2s 基底**。对四点函数而言，圈图的局域动量通常由外部标量动量和外部费米子动量的组合构成；把它写成协变导数后，再做 IBP/EOM 约化时，动量可以转移到标量流上。因此只投影到费米子动能型项会遗漏合法的流—流算符。

### 25.2 必须纳入投影的流—流算符

对于外腿 $\bar L,L,H,H^\dagger$，至少应检查与 SMEFT Warsaw 基底同型的结构

$$

Q_{HL}^{(1)}=(H^\dagger i\overleftrightarrow D_\mu H)
(\bar L\gamma^\mu L),

$$

$$

Q_{HL}^{(3)}=(H^\dagger i\overleftrightarrow D_\mu^{\,I}H)
(\bar L\tau^I\gamma^\mu L),

$$

其中

$$

H^\dagger i\overleftrightarrow D_\mu H
=iH^\dagger D_\mu H-i(D_\mu H)^\dagger H,

$$

而带指标 $I$ 的流包含 Pauli 矩阵 $\tau^I$。具体生成的单态/三重态组合及其相对系数，必须由弱同位旋指标的完整收缩决定，不能仅凭一个标量积分判断。

对于外腿 $\bar L,L,S,S^\dagger$，还必须检查

$$

Q_{SL}=(S^\dagger i\overleftrightarrow D_\mu S)
(\bar L\gamma^\mu L).

$$

右手轻子通道同样需要检查

$$

Q_{He}=(H^\dagger i\overleftrightarrow D_\mu H)
(\bar\ell_R\gamma^\mu\ell_R),\qquad
Q_{Se}=(S^\dagger i\overleftrightarrow D_\mu S)
(\bar\ell_R\gamma^\mu\ell_R),

$$

并根据完整模型的规范表示和所选算符约定纳入可能的其他允许结构。以上是应纳入检查的算符，而不是宣称每个系数都已由当前计算确定。

### 25.3 弱同位旋张量的投影不能省略

在 $\bar L_a,L_b,H_i,H_j^\dagger$ 外腿上，图的弱同位旋指标张量一般需要写成带外腿标签的 Kronecker delta 乘积。它可以通过 Pauli 矩阵完备关系分解到单态和三重态结构。因此，不能在尚未保留所有外部弱同位旋指标时，只计算一个固定分量就直接宣布得到 $Q_{HL}^{(1)}$ 或 $Q_{HL}^{(3)}$ 的单独系数。

同理，外部 $S,S^\dagger$ 的通道虽无 Higgs 双重态指标，但仍须保留复标量的规范荷和协变导数；如果只在零规范场背景下计算，得到的是普通导数部分，最终还需按规范协变性补齐对应的规范相互作用顶角，或用背景场方法验证。

### 25.4 当前 UV 极点结果的适用边界

第 23–24 节的一般向量积分

$$

J^\mu(q;m_X^2)=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{k^\mu}{(k^2+i0)((k+q)^2-m_X^2+i0)}

$$

及其 UV 极点

$$

J^\mu\big|_{\rm UV}=-\frac{i q^\mu}{32\pi^2\bar\epsilon}

$$

仍可作为指定分母和动量路由下的积分结果使用。但它本身不确定 $Q_{HL}^{(1,3)}$、$Q_{SL}$、$Q_{He}$、$Q_{Se}$ 的系数；还必须乘入完整的费米子分子、顶点与传播子因子、外腿排列、弱同位旋收缩，并将结果投影到固定的不冗余基底。

因此，对此前文档相关段落作如下状态修正：

- **保留**：主向量积分的 UV 极点以及圈图产生一个外部动量、带手征费米子双线性的结构判断。
- **修正**：此前候选导数算符清单仅为不完整的中间表示，不能当作最终算符基底。
- **尚未完成**：所有带标记外腿图的系数求和、单态/三重态投影、IBP/EOM 约化、独立算符的反项系数和异常维数矩阵。
- **仍未验证**：从 $h$-$s$ 二点函数提取的有限匹配常数 $-2/3$。它不能由当前 2f2s UV 极点单独确定。

后续实际计算顺序应为：先选定完整的维数六基底和规范约定；再为每种外腿组合保留所有动量与内部指标，逐图求和；最后统一进行 IBP/EOM 约化。只有在这个步骤完成后，才能把 2f2s 结果写进反项矩阵。

## 第 26 节：用原文 UV 拉氏量做的独立一致性检查

### 26.1 原文给出的味道结构与质量矩阵

核对 arXiv:2608.27258v1 的模型设定后，UV 相互作用确为

$$

- y_\mu\bar L_\mu H E_{\mu R}
-\lambda_\mu S\bar E_{\mu L}\mu_R
- y_\tau\bar L_\tau H E_{\tau R}
-\lambda_\tau S^*\bar E_{\tau L}\tau_R
- M_{E\alpha}\bar E_{\alpha L}E_{\alpha R}+\mathrm{h.c.},

$$

其中 $S$ 与 $S^*$ 的差异由 $U_A(1)_{L_\mu-L_\tau}$ 荷指派决定。每个味道的质量矩阵是

$$

\mathcal M_\alpha=\begin{pmatrix}0&m_{L\alpha}\\m_{R\alpha}&M_{E\alpha}\end{pmatrix},
\quad m_{L\alpha}=\frac{y_\alpha v_h}{\sqrt2},\quad
m_{R\alpha}=\frac{\lambda_\alpha v_s}{\sqrt2},

$$

但 $\tau$ 扇区的 $m_R$ 来自 $S^*$ 而非 $S$。后续计算涉及 CP-even 径向模 $s$ 时，这个共轭差异不会改变实参数下的径向耦合大小，但会影响规范协变导数、相位/Goldstone 相互作用和流算符的规范荷符号，不能把两味道的复标量约定混用。

### 26.2 一个可直接检验的 UV 极点消失条件

对单味道实参数，原始基底中的径向标量耦合矩阵（忽略整体拉氏量负号）可取为

$$

Y_h^{(0)}=a\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
Y_s^{(0)}=b\begin{pmatrix}0&0\\1&0\end{pmatrix},
\quad a=\frac{m_L}{v_h},\quad b=\frac{m_R}{v_s}.

$$

质量基底中 $Y_h=U_L^T Y_h^{(0)}U_R$、$Y_s=U_L^T Y_s^{(0)}U_R$。由于 $U_L,U_R$ 是正交矩阵，Frobenius 内积保持不变：

$$

\sum_{ij}(Y_h)_{ij}(Y_s)_{ij}
=\operatorname{Tr}(Y_h^T Y_s)
=\operatorname{Tr}\!\left[(Y_h^{(0)})^T Y_s^{(0)}\right]=0.

$$

而此前 PV 表达式中乘在 $-p^2B_0$ 前的组合为

$$

C_{ij}=(Y_h)_{ij}(Y_s)_{ij}+(Y_h)_{ji}(Y_s)_{ji},

$$

所以

$$

\sum_{ij}C_{ij}=2\sum_{ij}(Y_h)_{ij}(Y_s)_{ij}=0.

$$

因此完整质量本征态求和后，混合二点函数的 $p^2$ UV 极点必须消失。这是一个不依赖混合角显式展开的强检查：若直接逐图计算得到非零的 $p^2/\bar\epsilon$ 系数，说明遗漏了某个质量本征态组合、手征耦合项或相对符号。

### 26.3 这个检查能证明什么、不能证明什么

该内积恒等式只证明完整 renormalizable UV 理论中二点函数的 $p^2$ UV 极点应抵消；它**不**证明有限 $p^2$ 项为零，也不决定低能维数六算符的有限匹配系数。有限阈值来自不同质量的 $B_0(p^2;m_i^2,m_j^2)$ 的动量展开及 UV–EFT 差，必须保留轻—重、轻—轻和重—重态贡献，并使用相同 IR 规约相减。

此外，原文式 (2) 的简写把势能写为 $V(S)$，但规范对称性允许 $(H^\dagger H)(S^\dagger S)$ portal 项。若研究该 portal 的 radiative generation 或匹配，必须把其 renormalized boundary condition（例如某一尺度 $\lambda_{HS}(\mu_0)=0$）明确当作额外假设，而不能仅因模型展示式未写该项就认为它被对称性禁止。该边界条件会影响有限势能阈值；它不能替代导数算符的独立匹配。

**本节新增的已验证检查**：质量基底耦合矩阵的内积恒等式以及 $p^2$ UV 极点消失条件。**尚未完成**：按该条件逐项重算完整 PV 振幅、展开至 $p^2/M_E^2$，并与 EFT 泡图、接触图及所选维数六算符基底进行有限匹配。

## 第 27 节：对候选 PV 混合自能函数作独立的低动量导数展开（条件性结果）

本节只对第 21 节中记录的候选函数形式作代数核验。因为该函数的整体符号、耦合矩阵组合和与 EFT 的完整相减尚未从原始费曼规则重新推导，本节**不是最终 matching 结果**；用途是把容易出错的 PV 展开明确写出来，供后续逐图计算对照。

### 27.1 约定与基本积分

采用

$$

B_0(p^2;a,b)=\Delta-\int_0^1dx\,
\ln\!\frac{xa+(1-x)b-x(1-x)p^2-i0}{\mu^2},
\qquad \Delta=\frac1{\bar\epsilon},

$$

于是

$$

B_0'(0;a,b)=\int_0^1dx\,
\frac{x(1-x)}{xa+(1-x)b}.

$$

对等质量和混合质量情形，直接积分得到

$$

B_0'(0;m^2,m^2)=\frac1{6m^2},\qquad
B_0'(0;M^2,M^2)=\frac1{6M^2},

$$

以及

$$

B_0'(0;m^2,M^2)=
\frac{M^4-m^4-4M^2m^2\ln(M/m)}{2(M^2-m^2)^3}.

$$

这里假定 $m,M>0$；$m=M$ 时最后一式应取连续极限，等于 $1/(6m^2)$。注意 $B_0'$ 的质量维数是 $-2$。

### 27.2 候选函数的导数

把此前待复核的函数暂时记为

$$

\begin{aligned}
F(p^2)={}&(4m^2-p^2)B_0(p^2;m^2,m^2)\\
&+(4M^2-p^2)B_0(p^2;M^2,M^2)\\
&+(2p^2-4m^2-4M^2)B_0(p^2;m^2,M^2).
\end{aligned}

$$

对 $p^2$ 求导并在 $p^2=0$ 取值：

$$

\begin{aligned}
F'(0)={}&-B_0(0;m^2,m^2)+4m^2B_0'(0;m^2,m^2)\\
&-B_0(0;M^2,M^2)+4M^2B_0'(0;M^2,M^2)\\
&+2B_0(0;m^2,M^2)-4(m^2+M^2)B_0'(0;m^2,M^2).
\end{aligned}

$$

代入

$$

\begin{aligned}
B_0(0;m^2,m^2)&=\Delta-\ln\frac{m^2}{\mu^2},\\
B_0(0;M^2,M^2)&=\Delta-\ln\frac{M^2}{\mu^2},\\
B_0(0;m^2,M^2)&=\Delta+1-
\frac{M^2\ln(M^2/\mu^2)-m^2\ln(m^2/\mu^2)}{M^2-m^2},
\end{aligned}

$$

可见 $\Delta$ 完全抵消。整理后得到

$$

\boxed{
F'(0)=\frac{10}{3}
+\frac{M^2+m^2}{M^2-m^2}\ln\frac{m^2}{M^2}
-4(M^2+m^2)B_0'(0;m^2,M^2)
}.

$$

等价地，令 $r=m^2/M^2$，可写为

$$

\boxed{
F'(0)=\frac{10}{3}+\frac{1+r}{1-r}\ln r
-\frac{2(1+r)(1-r^2+2r\ln r)}{(1-r)^3}
}.

$$

该表达式无量纲，且在 $r\to1$ 时应以连续极限理解；显式的 $1-r$ 分母不是物理奇点。

### 27.3 小轻质量极限与解释边界

在 $r\ll1$ 时，

$$

F'(0)=\ln r+\frac43+O(r\ln r).

$$

因此该候选函数的单个质量组合在轻质量趋零时含 $\ln(m^2/M^2)$。这并不自动意味着 Wilson 系数含有红外对数：matching 中由低能 EFT 产生的相同轻质量/外动量依赖必须相减；只有 UV 与 EFT 的差才应被解释为硬区间阈值。

这一结果还说明，不能直接把 $F'(0)$ 的常数项 $4/3$ 认作之前候选匹配常数 $-2/3$ 的反证或证明。两者之间还隔着耦合矩阵权重、完整质量本征态求和、EFT 泡图/接触图相减、以及自能到算符系数的归一化转换。

### 27.4 本步状态记录

- **本步已完成（代数层面）**：在上述 PV 定义下，独立求出三个 $B_0'$ 积分，并对候选 $F(p^2)$ 求出 $F'(0)$；确认该组合的 $1/\bar\epsilon$ 极点抵消。
- **条件成立**：所有公式均以第 21 节候选 $F$ 的结构和当前 $B_0$ 约定为前提；如果从原始费曼规则得到不同的分子结构，必须重新计算。
- **尚未完成**：把完整 $h$-$s$ 自能逐图重建到该 $F$ 形式；对质量本征态求和；减去 EFT 红外部分；把硬部分映射到不冗余维数六算符基底。
- **不得声称已验证**：候选 $C_D(M)=-|y|^2|\lambda|^2/(48\pi^2M^2)$ 和有限常数 $-2/3$。

## 第 28 节：把原文质量基底标量耦合显式代入——耦合权重矩阵检查

本步沿用原文式 (13) 的单味道实参数耦合矩阵。令

$$

a=\frac{m_L}{v_h},\qquad b=\frac{m_R}{v_s},\qquad
K=ab\,c_Ls_Lc_Rs_R,

$$

则（省略味道标签）

$$

Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix}.

$$

对当前采用的实耦合约定，逐元素相乘得到

$$

P_{ij}\equiv (Y_h)_{ij}(Y_s)_{ij}
=K\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.

$$

若自能的动量依赖项按第 26 节所用的耦合组合

$$

C_{ij}=P_{ij}+P_{ji}

$$

组织，则

$$

\boxed{C=2K\begin{pmatrix}1&-1\\-1&1\end{pmatrix}},
\qquad \sum_{ij}C_{ij}=0.

$$

这直接核验了第 26 节用 Frobenius 内积得到的极点抵消条件，而且显示轻—轻、重—重、轻—重、重—轻四种质量标签的权重符号必须按 $(+,-,-,+)$ 的矩阵结构处理；不能只保留一个轻—重图。

如果且仅如果完整自能确实可以写成同一对称函数的加权和

$$

\Pi_{hs}(p^2)\propto\sum_{i,j}C_{ij}F(p^2;m_i,m_j),

$$

且 $F$ 就是第 27 节定义的候选函数，那么利用 $F(p^2;m,m)=F(p^2;M,M)=0$ 与 $F(p^2;m,M)=F(p^2;M,m)$，可进一步化简为

$$

\sum_{ij}C_{ij}F(p^2;m_i,m_j)=-4K F(p^2;m,M).

$$

这里“如果且仅如果”很重要：该化简只是在候选表达式成立时的代数后果，**不是**对完整费曼振幅结构的独立证明，也不能单凭它决定整体符号或归一化。

### 本步状态

- **已完成**：将原文式 (13) 的实耦合矩阵逐元素相乘，得到权重矩阵及其零和性质；确认 UV 动量极点的耦合权重抵消。
- **条件性代数结论**：若完整振幅具有第 27 节假定的 $\sum C_{ij}F(m_i,m_j)$ 结构，则质量求和化为单个轻—重函数的 $-4K$ 倍。
- **下一项必须完成**：从实际费米子环的两个标量顶点、两个费米子传播子和手征投影重新推导 $C_{ij}$ 及每个质量组合对应的 PV 分子，核对该候选加权和的整体因子与符号；再做 UV–EFT 相减。
- **未验证**：有限匹配常数 $-2/3$ 和最终 $C_D$。

## 第 29 节：从费米子环的 Dirac 迹重建一般质量基底分子

这是对第 27–28 节候选自能结构的下一步检查。先固定质量本征态指标，再做 Dirac 迹；这样可以分开动量分子与质量翻转分子，避免只凭最终的若干 $B_0$ 系数反推图的结构。

### 29.1 顶点和耦合组合

对实标量 $h,s$，在质量基底中写

$$

V^h_{ij}=(Y_h)_{ij}P_R+(Y_h)^*_{ji}P_L,\qquad
V^s_{ji}=(Y_s)_{ji}P_R+(Y_s)^*_{ij}P_L.

$$

这里的指标顺序对应一条从质量本征态 $j$ 到 $i$ 的费米子线；若选用相反的费米子流方向，所有指标必须一起交换。
定义

$$

C_{ij}=(Y_h)_{ij}(Y_s)^*_{ij}+(Y_h)^*_{ji}(Y_s)_{ji},

$$

$$

D_{ij}=(Y_h)_{ij}(Y_s)_{ji}+(Y_h)^*_{ji}(Y_s)^*_{ij}.

$$

对实耦合，$C_{ij}$ 正是第 28 节的对称耦合权重；而 $D_{ij}$ 是另一种、与质量翻转项相乘的组合，不能在一般情况下把它与 $C_{ij}$ 混为一谈。

### 29.2 Dirac 迹

忽略整体圈因子和顶点前的 $i$ 因子，分子迹为

$$

\begin{aligned}
T_{ij}={}&\operatorname{tr}\!\left[V^h_{ij}(\slashed k+m_j)V^s_{ji}(\slashed k+\slashed p+m_i)\right]\\
={}&2C_{ij}\,k\!\cdot\!(k+p)+2m_im_jD_{ij}.
\end{aligned}

$$

其中动量项来自相反手征投影的组合，质量翻转项来自相同手征投影。线性于单个质量、含奇数个 gamma 矩阵的交叉项迹为零。

用分母

$$

D_j=k^2-m_j^2+i0,\qquad D_i=(k+p)^2-m_i^2+i0

$$

可作精确的分子恒等式

$$

2k\cdot(k+p)=D_j+D_i+m_i^2+m_j^2-p^2.

$$

因此，在常用 PV 标量积分归一化下，单个 $(i,j)$ 拓扑的积分结构必须包含

$$

C_{ij}\left[A_0(m_j^2)+A_0(m_i^2)
+(m_i^2+m_j^2-p^2)B_0(p^2;m_j^2,m_i^2)\right]
+2m_im_jD_{ij}B_0(p^2;m_j^2,m_i^2),

$$

整体的 $i$ 因子、费米子圈负号和拉氏量顶点符号需在统一的 $i\Pi_{hs}$ 约定下另行放回。这里使用 $A_0$ 表示约化后的 tadpole 标量积分；若采用不同的 PV 定义，必须同步调整其归一化。

### 29.3 这对候选 $F$ 函数意味着什么

由上式可直接读出，动量分子产生的 $p^2B_0$ 项系数正比于 $-C_{ij}$。因此只要完整耦合权重满足 $\sum_{ij}C_{ij}=0$，该部分的整体 UV 极点就抵消，与第 26 节的矩阵恒等式一致。

但完整有限部分同时包含：

1. $C_{ij}$ 加权的 $A_0(m_i^2)$、$A_0(m_j^2)$ 和 $(m_i^2+m_j^2-p^2)B_0$；
2. 由 $D_{ij}$ 控制的质量翻转项 $2m_im_jB_0$；
3. 所有 $(i,j)$ 与共轭方向的图，以及按原始费曼规则确定的整体符号。

所以第 27 节的候选 $F(p^2)$ 只有在把这些项按原始耦合逐项求和、并证明 tadpole 与质量翻转项确实可化成该形式后才可使用。**当前尚未证明候选 $F$ 与这套一般迹公式完全等价**；第 27 节的 $F'(0)$ 应继续保留为条件性代数结果，不能直接作为物理自能的最终导数。

### 29.4 本步状态

- **已完成**：从手征顶点独立得到一般的 Dirac 迹结构，并用分母恒等式分离 $A_0$、$B_0$ 与质量翻转项。
- **已交叉核验**：动量相关 UV 极点与 $\sum C_{ij}=0$ 条件一致。
- **尚未完成**：把所有质量本征态的 $C_{ij}$ 与 $D_{ij}$ 逐项代入，确定完整 $\Pi_{hs}$ 的整体归一化与符号；再将其与 EFT 振幅相减。
- **修正状态说明**：第 27 节只计算了一个候选 PV 组合的导数；在本节完整分子结构约化前，不应把该候选组合称作已经由费曼规则推导出的 UV 自能。

## 第 30 节：把质量基底中的两类耦合权重同时代入——检查候选自能是否遗漏 portal 发散

本节继续使用第 29 节明确写出的质量基底顶点约定，并采用论文式 (13) 的实耦合矩阵。目的不是直接宣称得到了最终匹配，而是检查此前候选 PV 函数是否可能遗漏了质量翻转项，以及 UV 极点应按什么结构分类。

### 30.1 显式计算质量翻转权重矩阵

记

$$

a=\frac{m_L}{v_h},\qquad b=\frac{m_R}{v_s},\qquad
K=ab\,c_Ls_Lc_Rs_R,

$$

并定义另一个与第 29 节一致的组合

$$

J=ab\left(c_L^2c_R^2+s_L^2s_R^2\right).

$$

由

$$

Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix}

$$

以及第 29 节定义

$$

D_{ij}=(Y_h)_{ij}(Y_s)_{ji}+(Y_h)^*_{ji}(Y_s)^*_{ij}

$$

（当前为实耦合），逐项相乘得到

$$

\boxed{D=\begin{pmatrix}2K&-J\\-J&2K\end{pmatrix}.}

$$

因此一般情况下 $D$ 并不等于 $C$：第 28 节的动量权重为

$$

C=2K\begin{pmatrix}1&-1\\-1&1\end{pmatrix},

$$

而质量翻转项具有不同的非对角权重 $-J$。把质量翻转项直接并入同一个 $C_{ij}$ 权重会丢失独立的耦合组合。

### 30.2 在第 29 节积分约化式下做完整的有限态求和

继续采用第 29 节的约化结构

$$

\sum_{ij}\left\{C_{ij}\left[A_0(m_i^2)+A_0(m_j^2)
+(m_i^2+m_j^2-p^2)B_{ij}\right]
+2m_im_jD_{ij}B_{ij}\right\},

$$

其中 $B_{ij}=B_0(p^2;m_i^2,m_j^2)$，并令 $m_1=m$、$m_2=M$。由于 $C$ 的每一行和每一列都为零，所有 $A_0$ 项严格相消；同理，$\sum_{ij}C_{ij}(m_i^2+m_j^2)=0$。保留下来的标量积分组合为

$$

\begin{aligned}
\mathcal S(p^2)={}&K(8m^2-2p^2)B_{mm}
+K(8M^2-2p^2)B_{MM}\\
&+\left[-4K(m^2+M^2-p^2)-4JmM\right]B_{mM},
\end{aligned}

$$

其中已使用对称性 $B_{mM}=B_{Mm}$。这是在第 29 节所定的迹和权重约定下得到的求和式；完整 1PI 振幅还需要统一恢复费米子圈负号、顶点 $i$ 因子及拉氏量符号。

### 30.3 UV 极点检查：动量极点与质量极点必须分开

在

$$

B_0=\Delta+\text{有限部分},\qquad
\Delta=\frac1{\bar\epsilon}

$$

的约定下，$\mathcal S$ 的 UV 极点系数为

$$

\begin{aligned}
\mathcal S\big|_{\rm UV}/\Delta
={}&K(8m^2-2p^2)+K(8M^2-2p^2)\\
&-4K(m^2+M^2-p^2)-4JmM\\
={}&\boxed{4K(m^2+M^2)-4JmM}.
\end{aligned}

$$

这里 $p^2$ 项确实抵消，但在一般耦合和质量下，质量无关以外的常数型极点不必为零。其物理含义是：对 $h$-$s$ 二点函数，UV 发散不只可能对应动量依赖结构，还可能对应 $H^\dagger H\,S^\dagger S$ portal 的质量/混合参数反项。该 portal 是规范对称性允许的重整化算符；若模型把其重整化值设为零，也必须说明这是某一尺度上的边界条件，而不是把它当作对称性禁止的项。

这与第 26、28 节的结论相容，但修正了一个可能造成误读的地方：$\sum C_{ij}=0$ 只足以保证此处的 $p^2/\bar\epsilon$ 系数消失，不能单独推出整个自能的所有 UV 极点均消失。

### 30.4 对此前候选函数 $F(p^2)$ 的影响

第 27 节候选函数的三项系数之和为零，因此它会同时消掉其标量积分组合中的整体 UV 极点。可是按第 29 节的一般迹结构求和后，质量翻转权重 $D_{ij}$ 独立出现，而且质量型 UV 极点一般对应允许的 portal 反项。因此，**除非进一步证明特定参数关系使质量型极点抵消，或已把 portal 反项单独剥离，否则第 27 节的候选 $F$ 不能直接代表完整的 $h$-$s$ 自能**。

这也意味着不能把第 27 节的小质量展开常数、或先前提出的 $-2/3$，直接解释为 Wilson 系数。下一步应把完整 UV 自能分成：

1. 与 $p^2$ 成正比的动量项，检验其 UV 极点并做低动量展开；
2. 与 $p^2$ 无关的质量/portal 项，匹配到相应重整化参数；
3. 低能 EFT 中相同的红外贡献，采用相同 IR 规约相减。

### 30.5 本步状态

- **已完成（在第 29 节迹约定下）**：显式求得 $D$ 矩阵；完成所有两态质量指标的代数求和；分别检查动量型与质量型 UV 极点。
- **关键结论**：动量型 UV 极点抵消，不代表整个自能没有 UV 发散；允许的 portal 反项必须单独跟踪。
- **条件性结果**：$\mathcal S(p^2)$ 的整体归一化和符号仍依赖第 29 节的顶点/费米子流约定，必须由原始 Feynman rules 最终固定。
- **尚未完成**：从完整 UV 振幅减去 EFT 泡图和接触图；将动量部分映射到独立维数六算符；验证有限匹配常数 $-2/3$。

## 第 31 节：对完整两态求和式求导，提取动量项的候选有限部分

本节只对第 30 节的代数求和式 $\mathcal S(p^2)$ 做 $p^2=0$ 导数。由于第 30 节尚未最终固定整体费米子圈符号与顶点归一化，本节结果是**有条件的 PV 中间结果**，不是最终 Wilson 系数。

### 31.1 求导

第 30 节给出

$$

\begin{aligned}
\mathcal S(p^2)={}&K(8m^2-2p^2)B_{mm}
+K(8M^2-2p^2)B_{MM}\\
&+[-4K(m^2+M^2-p^2)-4JmM]B_{mM}.
\end{aligned}

$$

因此

$$

\begin{aligned}
\mathcal S'(0)={}&K\left[-2B_{mm}(0)+8m^2B'_{mm}(0)
-2B_{MM}(0)+8M^2B'_{MM}(0)\right]\\
&+4K B_{mM}(0)
-4\left[K(m^2+M^2)+JmM\right]B'_{mM}(0).
\end{aligned}

$$

使用

$$

B'_{mm}(0)=\frac1{6m^2},\qquad B'_{MM}(0)=\frac1{6M^2},

$$

以及

$$

B'_{mM}(0)=\frac{M^4-m^4-4M^2m^2\ln(M/m)}{2(M^2-m^2)^3},

$$

并记

$$

L_m=\ln\frac{m^2}{\mu^2},\qquad L_M=\ln\frac{M^2}{\mu^2},\qquad
R=\frac{M^2L_M-m^2L_m}{M^2-m^2},

$$

得到

$$

\boxed{
\begin{aligned}
\mathcal S'(0)={}&K\left[\frac{20}{3}+2L_m+2L_M-4R\right]\\
&-2\left[K(m^2+M^2)+JmM\right]
\frac{M^4-m^4-4M^2m^2\ln(M/m)}{(M^2-m^2)^3}.
\end{aligned}}

$$

这里的 $1/\bar\epsilon$ 极点已经抵消；导数中的对数仍可能包含低能红外信息，因此“UV 极点有限”不等于“已经完成 matching”。当 $m=M$ 时应对整个表达式取连续极限，不能直接代入含 $(M^2-m^2)^{-1}$ 的中间式。

### 31.2 结果的解释边界

1. 上式是第 30 节特定 $C,D$ 定义下的完整两态 PV 组合的导数，保留了质量翻转项 $JmM$。
2. 其中 $L_m$ 及当 $m\to0$ 时出现的轻质量对数属于需要与 EFT 低能振幅比较的部分，不能全部认作硬阈值。
3. 只有在 UV 与 EFT 使用相同的外动量、轻质量、IR 规约和重整化方案，并将 portal 的零动量反项与导数项分开后，差值才能用于维数六导数算符匹配。
4. 这条导数还必须乘上从完整费曼规则确定的整体圈因子；因此不能把盒中表达式直接等同于此前候选 $C_D$，也不能据此确认 $-2/3$。

### 31.3 本步状态

- **已完成（代数层面）**：对第 30 节两态求和式求导；代入三个 $B_0'$ 的解析表达式；显式展示 UV 极点抵消。
- **条件成立**：结果依赖第 29–30 节的顶点指标、$C,D$ 定义及 PV 约化约定，整体符号/因子仍待从原始费曼规则确认。
- **尚未完成**：EFT 泡图与接触图的同方案计算和相减；提取纯硬区间系数；从自能投影到独立算符的归一化转换；验证 $-2/3$。

## 第 32 节：在 seesaw 小混合极限下展开完整两态导数——分离低能对数与重尺度对数

本节沿用第 31 节的条件性 PV 导数表达式，只做一致的渐近展开。目的在于检查轻质量对数如何出现，以及它为什么必须由 EFT 侧复现并相减。这里仍不把结果宣称为最终 Wilson 系数，因为整体费曼规则因子与 EFT 全部图尚未完成核对。

### 32.1 小混合角下的参数关系

论文质量矩阵在

$$

M_E\gg m_L,m_R

$$

时给出

$$

m\simeq\frac{m_Lm_R}{M_E},\qquad
s_L\simeq\frac{m_L}{M_E},\qquad
s_R\simeq\frac{m_R}{M_E},\qquad c_L,c_R\simeq1.

$$

因此，第 30 节定义的组合满足

$$

K=\frac{m_L}{v_h}\frac{m_R}{v_s}c_Ls_Lc_Rs_R
\simeq\frac{m_L^2m_R^2}{v_hv_sM_E^2}
\simeq\frac{m^2}{v_hv_s},

$$

而

$$

J=\frac{m_L}{v_h}\frac{m_R}{v_s}(c_L^2c_R^2+s_L^2s_R^2)
\simeq\frac{m_Lm_R}{v_hv_s}.

$$

于是有一个重要的领先阶关系

$$

\boxed{JmM_E\simeq K M_E^2.}

$$

这不是任意参数空间中的精确恒等式，而是大重质量、小混合角近似下的关系；超出该近似时应使用精确质量与混合角重新计算。

### 32.2 混合二点积分的渐近展开

令

$$

r=\frac m{M_E}\ll1,\qquad L_m=\ln\frac{m^2}{\mu^2},\qquad L_M=\ln\frac{M_E^2}{\mu^2}.

$$

第 31 节中的函数满足

$$
R=\frac{L_M-r^2L_m}{1-r^2}=L_M+\mathcal O(r^2\ln r),

$$

以及

$$

B'_{mM}(0)=\frac1{2M_E^2}\left[1+\mathcal O(r^2\ln r)\right].

$$

将这些展开和 $JmM_E\simeq KM_E^2$ 代入第 31 节的表达式，得到领先阶结果

$$

\boxed{\mathcal S'(0)=K\left[\frac{14}{3}+2\ln\frac{m^2}{M_E^2}\right]
+\mathcal O\!\left(Kr^2\ln r\right).}

$$

这里用到了 $L_m-L_M=\ln(m^2/M_E^2)$，所以重整化尺度 $\mu$ 在该领先阶组合中消失。该式是对第 30 节特定 PV 组合的数学渐近展开，不包含尚待固定的整体圈因子。

### 32.3 这条展开能告诉我们什么、不能告诉我们什么

- **可以确认**：在此条件性组合中，轻质量对数以 $\ln(m^2/M_E^2)$ 出现；因此不能把整个 $\mathcal S'(0)$ 当作纯硬区间的阈值系数。
- **可以确认**：EFT 侧的轻自由度环图必须包含相同的低能非解析对数。UV 与 EFT 在相同外动量、轻质量和红外规约下相减后，低能对数才应消去或转入 EFT 的矩阵元/运行。
- **不能确认**：常数 $14/3$ 是最终 Wilson 系数中的有限常数。它仍可能受到完整图的归一化、接触图、算符投影与有限重整化方案影响。
- **不能确认**：此前提出的 $-2/3$ 已被支持或排除。两者来自不同层次的中间表达式；在 EFT 相减前不能比较为物理匹配结果。

### 32.4 本步状态

- **已完成**：将 seesaw 参数关系代入第 31 节的条件性导数，提取 $m/M_E\ll1$ 的领先阶渐近形式。
- **已核验**：领先阶结果中 $\mu$ 依赖通过 $L_m-L_M$ 合并为质量比对数。
- **尚未完成**：以完整费曼规则固定 UV 振幅整体因子；独立计算 EFT 泡图、接触图和可能的混合/反项贡献；相减并投影到规范不变、非冗余的维数六算符基底。

## 第 33 节：修正质量翻转权重矩阵的记号——非对角元不能逐元写成同一个 $-J$

重新检查第 30 节时，发现其文字把质量翻转权重矩阵直接写成对称矩阵

$$

D=\begin{pmatrix}2K&-J\\-J&2K\end{pmatrix}

$$

容易造成逐元层面的误读。严格按第 29 节的定义

$$

D_{ij}=(Y_h)_{ij}(Y_s)_{ji}+(Y_h)^*_{ji}(Y_s)^*_{ij}

$$

并使用论文式 (13) 的实耦合矩阵，逐项得到

$$

\boxed{D_{11}=2K,\quad D_{22}=2K,\quad
D_{12}=-2ab\,c_L^2c_R^2,\quad
D_{21}=-2ab\,s_L^2s_R^2,}

$$

其中 $a=m_L/v_h$、$b=m_R/v_s$。因此，除非参数满足特殊关系，严格的逐元矩阵并不对称。

不过，对当前两点函数的混合质量积分，$B_0(p^2;m^2,M_E^2)=B_0(p^2;M_E^2,m^2)$，且混合质量翻转项带有对称因子 $mM_E$。故两个非对角贡献只通过其和进入：

$$

D_{12}+D_{21}=-2ab(c_L^2c_R^2+s_L^2s_R^2)=-2J.

$$

这解释了为什么第 30 节对完整标量积分组合得到的 $-4JmM_E B_{mM}$ 仍然成立，尽管把 $D$ 本身逐元写成对称矩阵并不严格。

**状态修正：** 第 30 节的混合质量项求和式保留为条件性有效结果；其“$D$ 矩阵逐元对称”的表述由本节取代。今后在扩展到不对称质量、不同外腿或非对称传播子时，必须保留 $D_{12}$ 与 $D_{21}$ 的区别，不能提前将其合并。

## 第 34 节：匹配计算的独立一致性检查——不能把 UV 极点抵消与 EFT 极点直接等同

本节把目前最容易混淆的两件事分开：完整 UV 理论中的二点函数 UV 极点，以及截断 EFT 中维数五相互作用产生的维数六算符 UV 极点。它们必须在匹配方程和重整化群关系中一致，但不要求某个单独的 PV 系数逐项相等。

### 34.1 已知的 UV 动量极点检查

按第 29–30 节当前采用的耦合乘积权重，动量型项的系数矩阵为

$$

C_{ij}=2(Y_h)_{ij}(Y_s)_{ij}
=2K\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.

$$

因此

$$

\sum_{i,j}C_{ij}=2K-2K-2K+2K=0.

$$

若每一项的 $p^2$ UV 极点确实具有同一个质量无关系数（这是该求和成立所依赖的条件），则这个特定完整 UV 振幅中的 $p^2/\bar\epsilon$ 项相消。该结论只针对动量型极点，不能推出常数型极点也相消；后者仍须由质量项及允许的标量势反项处理。

**重要限制：** 上述代数求和验证的是已写出的权重矩阵，不是完整费曼振幅的独立推导。整体符号、圈因子、实/复标量归一化以及是否遗漏其他图，仍需从原始拉氏量逐一核验。因此文中“UV 动量极点相消”暂列为条件性检查，不列为最终物理结论。

### 34.2 EFT 维数五泡图的极点代表什么

在 EFT 中定义

$$

\Phi_{\ell i}=S_\ell H_i,\qquad
\mathcal L_5=-C_{5,\ell}\Phi_{\ell i}\bar L_{\ell i}\ell_R+\mathrm{h.c.}

$$

质量为零的轻费米子泡图在所用约定下产生正比于

$$

\frac{|C_{5,\ell}|^2}{16\pi^2\bar\epsilon}\,p^2

$$

的局部 UV 极点。其局部性要求 EFT 以含导数的复合场算符（或经分部积分、运动方程约化后的等价算符组合）吸收该极点。对复合场 $\Phi=SH$，有

$$

(D_\mu\Phi)^\dagger D^\mu\Phi
=(D_\mu S)^\dagger D^\mu S\,(H^\dagger H)
+(S^\dagger S)(D_\mu H)^\dagger D^\mu H
+\text{交叉导数项},

$$

其中“交叉导数项”不能在尚未指定分部积分、规范指标和算符基底之前任意丢弃。故仅保留 $(S^\dagger S)(D H)^\dagger D H$ 并不足以代表完整反项。

### 34.3 为什么两侧的极点不能直接逐项比较

EFT 泡图的 UV 极点是低能理论中局部算符的重整化；完整 UV 理论的重整化则受其可重整化拉氏量允许的反项约束。匹配时应比较相同外态、相同红外规约下的重整化振幅，并从 UV 振幅中减去 EFT 振幅：

$$

\mathcal A_{\rm match}=\mathcal A_{\rm UV}^{\rm ren}-\mathcal A_{\rm EFT}^{\rm ren}.

$$

这里的符号表示匹配差额，不是说两边裸图的每一个 UV 极点都必须在逐图层面相同。EFT 算符系数的尺度依赖应由其反项与 anomalous-dimension 矩阵描述；完整匹配结果必须在物理量中消除任意重整化尺度依赖。

尤其不能从“UV 振幅某个 $p^2/\bar\epsilon$ 系数为零”单独推断“EFT 导数算符的反项为零”，也不能仅凭 EFT 泡图存在极点就宣称 UV 理论必有同样的非重整化维数六反项。必须先明确匹配的是哪一个规范不变振幅/算符组合，以及低能图、硬区贡献和参数反项的分工。

### 34.4 下一步计算顺序（修订版）

1. **固定模型和场约定。** 从论文拉氏量确认 $S$ 是复标量还是在当前计算中取实分量，列出 $h,s$ 的规范归一化、质量基底费米子旋转矩阵，以及 Eq. (13) 中每个顶点的费米规则。
2. **独立列出 1PI 图。** 对外腿 $h,s$ 的二点函数，明确每个内部费米子质量本征态组合、两个 Yukawa 顶点的顺序、动量流与闭合费米子圈的负号；分别保留 $\slashed k$ 动量项和质量翻转项。
3. **先检查 UV 极点，再求有限项。** 对每个图写出 $A_0,B_0$ 表达式，独立求和并检查其 $1/\bar\epsilon$ 系数。只有通过这个检查后，才使用 $B_0$ 的有限部分与渐近展开。
4. **在 EFT 中用同一外态和规约重算。** 同时包含维数五泡图、由质量/真空期望值展开诱导的接触项，以及匹配该外态所需的其他图；所有图统一采用同一套 $i\mathcal M$ 和自能符号约定。
5. **指定完整算符基底并约化。** 将复合场导数结构投影到规范不变算符，再使用分部积分、运动方程和必要的 Fierz 恒等式约化；注明维数正规化下的算符方案。
6. **做匹配差并检查尺度。** 计算 UV−EFT 的硬区差额，确认低能对数消去或按预期进入 EFT 矩阵元；最后才定义 Wilson 系数并推导 RG 方程。

### 34.5 本节状态

- **已完成：** 区分完整 UV 理论反项与 EFT 维数六算符反项；明确复合场导数算符包含的结构；列出后续独立核验所需的最小步骤。
- **尚未完成：** 尚未从原始费曼规则重新推导 UV 振幅，也尚未完成 EFT 所有图的符号/组合因子核验。因此第 30–33 节所有依赖该 UV 振幅的有限常数与 Wilson 系数候选值仍为条件性结果。
- **当前禁止性结论：** 在完成第 1–6 步之前，不把 $14/3$、$-2/3$ 或其他单个有限常数报告为已确定的匹配系数。

## 第 35 节：回到论文原始模型，固定本次匹配所用的 UV 约定

本节根据论文 arXiv:2608.27258 的原始 HTML 版 Sec. II.1–II.2（Eqs. (2)–(15)）重新登记输入，避免后续计算沿用未核对的参数约定。

### 35.1 UV 拉氏量与质量参数

论文 Eq. (2) 的 muon sector 为

$$

\mathcal L_{UV}\supset-y_\mu\bar L_\mu H E_{\mu R}
-\lambda_\mu S\bar E_{\mu L}\mu_R
-M_{E\mu}\bar E_{\mu L}E_{\mu R}+\mathrm{h.c.}
+(D_\nu S)^\dagger(D^\nu S)-V(S).

$$

论文 Eq. (3) 给出的树级 EFT 系数满足

$$

\frac{c_\mu}{\Lambda}\simeq\frac{y_\mu\lambda_\mu}{M_{E\mu}},
\qquad \Lambda=M_{E\mu}.

$$

在论文采用的实参数约定下，

$$

H=\frac1{\sqrt2}\begin{pmatrix}0\\v_h+h\end{pmatrix},\qquad
S=\frac{v_s+s}{\sqrt2}\quad\text{（论文此处显示径向模）},

$$

$$

m_L=\frac{y_\mu v_h}{\sqrt2},\qquad
m_R=\frac{\lambda_\mu v_s}{\sqrt2},\qquad
\mathcal M_\mu=\begin{pmatrix}0&m_L\\m_R&M_{E\mu}\end{pmatrix}.

$$

因此，计算中若使用 $a=m_L/v_h$、$b=m_R/v_s$，应有

$$

a=\frac{y_\mu}{\sqrt2},\qquad b=\frac{\lambda_\mu}{\sqrt2},

$$

不能再额外重复引入一个 $1/\sqrt2$。

### 35.2 精确质量与混合角

论文 Eq. (8) 给出

$$

m_{\mu/E}^2=\frac12\left[m_L^2+m_R^2+M_E^2
\mp\sqrt{(m_L^2+m_R^2+M_E^2)^2-4m_L^2m_R^2}\right],

$$

其中负号对应轻本征态，正号对应重本征态。论文 Eq. (9) 的角度约定为

$$

\tan2\theta_L=\frac{2m_LM_E}{M_E^2+m_R^2-m_L^2},\qquad
\tan2\theta_R=\frac{2m_RM_E}{m_L^2+M_E^2-m_R^2}.

$$

在 $M_E\gg m_L,m_R$ 时，论文采用

$$

m_\mu^2\simeq\frac{m_L^2m_R^2}{M_E^2},\qquad
\theta_L\simeq\frac{m_L}{M_E},\qquad
\theta_R\simeq\frac{m_R}{M_E}.

$$

这些是角度的小角近似；如果要验证高阶的 $m/M_E$ 项，必须回到精确本征值和旋转矩阵，而不能把 $s_{L,R}$ 与 $\theta_{L,R}$ 在所有阶上混用。

### 35.3 质量基底标量耦合

论文 Eq. (13) 在质量基底给出的矩阵为

$$

Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix}.

$$

拉氏量结构是 $-h\bar\chi_LY_h\chi_R-s\bar\chi_LY_s\chi_R+\mathrm{h.c.}$。所以对每个实标量，完整费米顶点必须同时包含矩阵和其厄米共轭所对应的左右手投影：

$$

\Gamma_h\propto Y_hP_R+Y_h^\dagger P_L,\qquad
\Gamma_s\propto Y_sP_R+Y_s^\dagger P_L.

$$

在独立重算 1PI 图时，不能只保留 $Y_h$ 与 $Y_s$ 的一个手征部分；动量型项和质量翻转项应从完整 Dirac trace 分别提取，再与第 29–33 节的权重求和逐项比较。

### 35.4 对后续计算的直接影响

1. 先以以上精确质量本征值、旋转角定义为输入，重新生成所有 $h\bar\chi_i\chi_j$ 与 $s\bar\chi_i\chi_j$ 顶点。
2. 对每组内部质量 $(m_i,m_j)$ 单独写出完整迹，明确哪些项来自 $Y_hY_s$、哪些来自与厄米共轭相关的组合；不能只凭矩阵元素乘积的外观判断符号。
3. 将 Dirac trace 结果化成 $A_0$ 与 $B_0$ 后，再比较第 30 节的候选表达式。若任一系数不一致，应以原始拉氏量计算为准，并回头修订第 30–33 节，而不是强行保留旧式。
4. 论文把 $V(S)$ 简写为 singlet 自势，并不等价于宣称规范允许的 $(H^\dagger H)(S^\dagger S)$ 门户项必然为零。匹配标量二点函数时，需将所选树级参数条件和门户反项条件分开说明。

### 35.5 本节状态

- **已从原文确认：** UV 拉氏量的 Yukawa 结构、$m_L,m_R$ 的 $1/\sqrt2$ 归一化、质量矩阵、精确质量本征值、混合角定义以及 Eq. (13) 的质量基底耦合矩阵。
- **尚未完成：** 尚未把每一组内部费米子质量的完整 Dirac trace 全部重新积分并与第 30 节对照；因此本节固定了输入约定，但不宣称已独立验证旧的 $\mathcal S(p^2)$ 表达式。


## 第 36 节：UV 一圈混合自能的逐顶点 Dirac 迹——可复核的计算骨架

> **本节目的与状态。** 本节把“从原始费曼规则重算”落实为逐项可检查的代数步骤，并给出不依赖 PV 约化的 Dirac 迹结构。它是后续计算的明确起点，不表示第 30 节的候选总振幅已经被证实。由于顶点指标和自能整体符号对约定敏感，最终求和前必须先用同一条费米子流向固定所有指标。

### 36.1 先固定顶点的指标约定

令质量本征态为 Dirac 费米子 $\chi_i$，质量为 $m_i$。在实标量 $h,s$ 的拉氏量

$$

\mathcal L_{\rm int}=-h\,\bar\chi_i\left[(Y_h)_{ij}P_R+(Y_h)^*_{ji}P_L\right]\chi_j
-s\,\bar\chi_i\left[(Y_s)_{ij}P_R+(Y_s)^*_{ji}P_L\right]\chi_j

$$

中，定义顶点矩阵

$$

\Gamma_h^{ij}=(Y_h)_{ij}P_R+(Y_h)^*_{ji}P_L,\qquad
\Gamma_s^{ij}=(Y_s)_{ij}P_R+(Y_s)^*_{ji}P_L,

$$

其中 $P_{R,L}=(1\pm\gamma_5)/2$。这里的 $i,j$ 是顶点左、右 Dirac 场的指标；在闭合费米子圈中，相邻传播子的质量指标必须与相应顶点的指标收缩一致。不能在没有重写指标的情况下，把 $\Gamma_h^{ij}\Gamma_s^{ji}$ 简化成某两个矩阵元素的普通乘积。

传播子分子取

$$

S_i(k)=\slashed k+m_i,\qquad S_j(k+p)=\slashed k+\slashed p+m_j.

$$

为了避免动量流向导致的表面符号错误，本项目统一把一条指定费米子流上的圈积分写成

$$

T_{ij}(k,p)=\operatorname{Tr}\!\left[\Gamma_h^{ij}(\slashed k+m_j)\Gamma_s^{ji}(\slashed k+\slashed p+m_i)\right],

$$

并在写出实际费曼振幅时检查传播子顺序是否与该定义一致。若采用相反的传播子顺序，应整体重新写迹，而不能只交换一个质量标签。

### 36.2 用手征耦合把迹分解

为展示代数结构，暂时把两个顶点写成一般形式

$$

\Gamma_h=g_{hR}P_R+g_{hL}P_L,\qquad
\Gamma_s=g_{sR}P_R+g_{sL}P_L,

$$

这里的 $g$ 是对应于固定指标方向的耦合，未预先假定它们相等或实数。使用

$$

P_LP_R=P_RP_L=0,\quad P_{R,L}^2=P_{R,L},\quad
P_R\gamma^\mu=\gamma^\mu P_L

$$

以及 $\operatorname{Tr}(\gamma^\mu\gamma^\nu)=4g^{\mu\nu}$，迹只保留两类非零结构：

- **动量型项：** 两个传播子分子各取一个 $\slashed k$ 或 $\slashed k+\slashed p$，并要求相邻手征投影不令该项为零。它最终正比于 $k\cdot(k+p)$。
- **质量翻转项：** 两个传播子分子各取一个质量，贡献正比于 $m_im_j$。只有满足投影条件的耦合组合会留下。

在上述迹顺序下，直接展开并逐项使用投影恒等式，可把迹整理为与下列结构同型的形式：

$$

T_{ij}(k,p)=2\,G^{(k)}_{ij}\,k\cdot(k+p)
+2\,G^{(m)}_{ij}\,m_im_j,

$$

其中 $G^{(k)}_{ij}$ 与 $G^{(m)}_{ij}$ 分别是由相应左右手耦合相乘得到的组合。**具体组合的指标次序必须由本节 36.1 的实际顶点矩阵代入后确定**；不能脱离费米子流向，直接把它们认定为第 29–33 节中的 $K$ 或 $J$。这项约束是为了避免把正确的迹恒等式与错误的指标收缩混在一起。

一个便于检查的中间恒等式是

$$

k\cdot(k+p)=\frac12\left[k^2+(k+p)^2-p^2\right].

$$

因此动量型项可以改写成三个标量积分的线性组合。对相同质量传播子，移位积分变量后，两个 $A_0$ 项可直接识别；混合质量传播子则须保留对应的 $B_0(p^2;m_i^2,m_j^2)$。此处不能提前把 $A_0$ 项删去，因为它们可能参与质量型发散及参数反项。

### 36.3 从迹到 PV 函数：每一步保留来源

采用维数正规化 $d=4-2\epsilon$，并定义

$$

A_0(m^2)=\frac{(2\pi\mu)^{4-d}}{i\pi^2}\int d^dk\,\frac{1}{k^2-m^2+i0},

$$

$$

B_0(p^2;m_i^2,m_j^2)=\frac{(2\pi\mu)^{4-d}}{i\pi^2}\int d^dk\,
\frac{1}{(k^2-m_i^2+i0)((k+p)^2-m_j^2+i0)}.

$$

具体的整体 $i$ 与 $(16\pi^2)^{-1}$ 因子应在代入费曼规则时统一提取，不应一部分藏在积分定义、一部分藏在振幅前因子中。

利用分子恒等式，动量型积分可按如下顺序处理：

$$

\int\!\frac{d^dk\;k\cdot(k+p)}{D_iD_j}
=\frac12\left[
\int\!\frac{d^dk}{D_j}+\int\!\frac{d^dk}{D_i}
+(m_i^2+m_j^2-p^2)\int\!\frac{d^dk}{D_iD_j}
\right],

$$

其中 $D_i=k^2-m_i^2+i0$，$D_j=(k+p)^2-m_j^2+i0$。在平移不变的维数正规化下，前两项分别化成相应的单传播子积分；双传播子项给出 $ (m_i^2+m_j^2-p^2)B_0/2$。这两个质量平方项不能遗漏。若分子是 $k^2$ 而不是 $k\cdot(k+p)$，应先写

$$

k^2=D_i+m_i^2-i0,

$$

再约分并积分。这样可以明确看出每一个 $A_0$、$m_i^2B_0$、$m_j^2B_0$ 和 $p^2B_0$ 项从哪里产生。

质量翻转项则直接给出

$$

 m_im_j\int\!\frac{d^dk}{D_iD_j}
\quad\longrightarrow\quad m_im_j B_0(p^2;m_i^2,m_j^2),

$$

乘以从完整迹中提取的耦合系数。它与动量型项的 PV 结构不同，因此应先分别记录，再合并成每个 $(i,j)$ 通道的结果。

### 36.4 必须执行的逐通道审计表

后续计算对每一个允许的内部质量组合 $(i,j)$ 都应填满下表；任何一栏尚未确认时，不应把该通道并入总表达式。

| 项目 | 必须记录的内容 | 检查标准 |
|---|---|---|
| 顶点 | $\Gamma_h^{ij}$、$\Gamma_s^{ji}$ 的完整左右手结构 | 厄米共轭和指标方向一致 |
| 迹 | 动量型与质量翻转型的独立系数 | 从完整 Dirac 迹得到，而非猜测矩阵乘积 |
| 积分分子 | $k\cdot(k+p)$、$k^2$ 或常数质量项 | 明确使用的代数恒等式 |
| PV 约化 | 每个 $A_0$ 与 $B_0$ 的系数 | 量纲均为振幅所需的质量平方量纲 |
| UV 极点 | $1/\bar\epsilon$ 的动量项与质量项 | 在求和前后分别列出，禁止只检查总和 |
| 有限项 | 对数、阈值函数及虚部 | 与同一 $i0$ 约定一致 |
| 总和 | 对所有质量本征态组合求和 | 不遗漏交叉项、不重复计数厄米共轭 |

### 36.5 为什么此时不直接宣布旧公式正确

第 30 节的候选式把不同质量通道写成了若干 $B_0$ 项的组合；第 31–33 节进一步对其求导并取小质量比极限。但若某个通道的手征权重或质量翻转系数有误，求导本身再精确也不能修复原始振幅。因此，正确的验证顺序是：

1. 对每个 $(i,j)$ 通道独立计算完整迹；
2. 在通道级别核对 $A_0/B_0$ 系数；
3. 再对所有本征态求和并比较第 30 节；
4. 若不一致，保留差异表并修订旧章节，而不是用总和的某个极限反向调节权重；
5. 只有通过以上检查后，才重新计算 $\mathcal S'(0)$、有限阈值常数和 EFT 匹配差额。

### 36.6 本节结论与下一步

本节已把下一步的代数任务细化到顶点指标、手征迹、分子约化与逐通道审计四个层次。尚未完成的是把论文 Eq. (13) 的具体矩阵元素逐个代入，并为所有允许的 $(i,j)$ 通道列出经过验证的最终系数。因此，本节不给出新的数值 Wilson 系数，也不把第 30 节候选式升级为已验证结果。下一轮应直接完成这张逐通道表，先检查 UV 极点，再检查有限部分。

---

## 第 37 节：将质量基底耦合矩阵真正代入完整 Dirac 迹，并纠正质量翻转权重

> **本节状态：发现并纠正了前文一个重要的代数问题。** 在采用第 36.1 节明确写出的顶点指标约定时，质量翻转权重矩阵必须由定义逐项计算。此前第 33 节记录的非对角元逐元不相同的矩阵，与该定义不一致；不能继续使用。下文给出从顶点到矩阵元素的可复核推导。整体自能的整体符号和规范化仍需结合全篇统一的 1PI 约定确认。

### 37.1 固定拉氏量、顶点与传播子顺序

采用质量本征态 Dirac 费米子列向量 $\chi=(\chi_1,\chi_2)^T$，质量矩阵为实正对角矩阵 $M=\mathrm{diag}(m_1,m_2)$。相互作用写作

$$

\mathcal L_{\mathrm{int}}=-h\,\bar\chi_i\Gamma_h^{ij}\chi_j-s\,\bar\chi_i\Gamma_s^{ij}\chi_j,

$$

其中重复指标求和，并且

$$

\Gamma_h^{ij}=(Y_h)_{ij}P_R+(Y_h)^*_{ji}P_L,\qquad
\Gamma_s^{ij}=(Y_s)_{ij}P_R+(Y_s)^*_{ji}P_L.

$$

在外部 $h,s$ 两顶点之间，选取内部费米子质量为 $m_j,m_i$ 的有向通道。为固定指标，以下迹定义为

$$

T_{ij}(k,p)=\operatorname{Tr}\!\left[\Gamma_h^{ij}(\slashed k+m_j)\Gamma_s^{ji}(\slashed k+\slashed p+m_i)\right].

$$

若改用相反的环动量方向，必须同步交换传播子、顶点和指标；不能只交换某个矩阵下标。

记

$$

A=(Y_h)_{ij},\quad B=(Y_h)^*_{ji},\quad C=(Y_s)_{ji},\quad D=(Y_s)^*_{ij}.

$$

则

$$

\Gamma_h^{ij}=AP_R+BP_L,\qquad
\Gamma_s^{ji}=CP_R+DP_L.

$$

### 37.2 逐项展开迹

迹中共有四种投影组合：

$$

(AP_R+BP_L)(\slashed k+m_j)(CP_R+DP_L)(\slashed k+\slashed p+m_i).

$$

使用

$$

P_LP_R=P_RP_L=0,\quad P_{L,R}^2=P_{L,R},\quad
P_R\gamma^\mu=\gamma^\mu P_L,\quad P_L\gamma^\mu=\gamma^\mu P_R,

$$

以及

$$

\operatorname{Tr}(P_L)=\operatorname{Tr}(P_R)=2,\qquad
\operatorname{Tr}(\gamma^\mu\gamma^\nu P_{L,R})=2g^{\mu\nu},

$$

可以分开计算动量项和质量项。

**(a) 动量项。** 两个传播子分子均取动量时，$AP_R\cdots CP_R$ 与 $BP_L\cdots DP_L$ 的投影组合为零；非零组合分别正比于 $AD$ 和 $BC$。因此

$$

T_{ij}^{(k)}=2(AD+BC)\,k\cdot(k+p).

$$

代回定义得到

$$

AD+BC=(Y_h)_{ij}(Y_s)^*_{ij}+(Y_h)^*_{ji}(Y_s)_{ji}\equiv C_{ij}.

$$

故

$$

\boxed{T_{ij}^{(k)}=2C_{ij}\,k\cdot(k+p)}.

$$

**(b) 质量翻转项。** 两个传播子分子均取质量时，非零组合为 $AC$ 与 $BD$。利用 $\operatorname{Tr}P_{L,R}=2$，得到

$$

T_{ij}^{(m)}=2m_im_j(AC+BD).

$$

因此

$$

AC+BD=(Y_h)_{ij}(Y_s)_{ji}+(Y_h)^*_{ji}(Y_s)^*_{ij}\equiv D_{ij},

$$

并有

$$

\boxed{T_{ij}^{(m)}=2D_{ij}m_im_j}.

$$

交叉项只含一个传播子质量和一个 slashed momentum，迹中含奇数个伽马矩阵，故其迹为零。最终，在上述约定下，完整分子为

$$

\boxed{T_{ij}(k,p)=2C_{ij}\,k\cdot(k+p)+2D_{ij}m_im_j.}

$$

这一步确认了第 36 节给出的结构，但也说明权重矩阵必须严格按 $C_{ij},D_{ij}$ 的定义代入，不能凭直觉设定。

### 37.3 将论文中的矩阵元素逐项代入

使用论文质量基底耦合矩阵

$$

Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix},

$$

其中

$$

a=\frac{m_L}{v_h},\qquad b=\frac{m_R}{v_s},\qquad
K=ab\,c_Ls_Lc_Rs_R,

$$

并定义

$$

J=ab(c_L^2c_R^2+s_L^2s_R^2).

$$

此处先假定矩阵元素为实数；若参数为复数，必须保留上面的复共轭定义，不可直接沿用以下实数简化。

#### 37.3.1 动量型权重 $C_{ij}$

对角元：

$$

C_{11}=2(Y_h)_{11}(Y_s)_{11}
=2(ac_Ls_R)(bs_Lc_R)=2K,

$$

$$

C_{22}=2(Y_h)_{22}(Y_s)_{22}
=2(as_Lc_R)(bc_Ls_R)=2K.

$$

非对角元：

$$

\begin{aligned}
C_{12}&=(Y_h)_{12}(Y_s)_{12}+(Y_h)_{21}(Y_s)_{21}\\
&=(ac_Lc_R)(-bs_Ls_R)+(as_Ls_R)(-bc_Lc_R)\\
&=-2K,
\end{aligned}

$$

同理

$$

C_{21}=(Y_h)_{21}(Y_s)_{21}+(Y_h)_{12}(Y_s)_{12}=-2K.

$$

所以

$$

\boxed{C=2K\begin{pmatrix}1&-1\\-1&1\end{pmatrix}},\qquad
\sum_{i,j}C_{ij}=0.

$$

该求和为零只说明在相同 UV 极点系数下，动量型 $p^2/\bar\epsilon$ 项会抵消；它本身不证明质量型极点也抵消。

#### 37.3.2 质量翻转权重 $D_{ij}$：对角元

按定义

$$

D_{ij}=(Y_h)_{ij}(Y_s)_{ji}+(Y_h)^*_{ji}(Y_s)^*_{ij}.

$$

在实矩阵情况下，$D_{11}=2(Y_h)_{11}(Y_s)_{11}=2K$，并且 $D_{22}=2(Y_h)_{22}(Y_s)_{22}=2K$。

#### 37.3.3 质量翻转权重：非对角元的关键核查

直接代入而不是沿用旧矩阵：

$$

\begin{aligned}
D_{12}&=(Y_h)_{12}(Y_s)_{21}+(Y_h)_{21}(Y_s)_{12}\\
&=(ac_Lc_R)(-bc_Lc_R)+(as_Ls_R)(-bs_Ls_R)\\
&=-ab(c_L^2c_R^2+s_L^2s_R^2)\\
&=-J.
\end{aligned}

$$

交换 $1\leftrightarrow2$ 后，乘积的两个项只是互换次序，因此

$$

D_{21}=(Y_h)_{21}(Y_s)_{12}+(Y_h)_{12}(Y_s)_{21}=-J.

$$

由此得到

$$

\boxed{D=\begin{pmatrix}2K&-J\\-J&2K\end{pmatrix}}.

$$

**纠错：** 这与第 33 节先前记录的 $D_{12}=-2ab c_L^2c_R^2$、$D_{21}=-2ab s_L^2s_R^2$ 不同。后者既不符合当前定义的逐元代入，也破坏了在实耦合情形下由定义直接得到的 $D_{12}=D_{21}$。第 33 节中该非对角矩阵及依赖它的说明应视为已撤回；任何使用其逐元形式的中间推导都必须重新检查。

### 37.4 质量翻转项的求和与质量因子

虽然本约定下 $D$ 对称，但总振幅中的质量翻转部分含有传播子质量乘积 $m_im_j$：

$$

\sum_{i,j}2D_{ij}m_im_jB_0(p^2;m_j^2,m_i^2).

$$

明确展开为

$$

\begin{aligned}
\mathcal T_m(p^2)=2\big[&2K m_1^2 B_0(p^2;m_1^2,m_1^2)
+2K m_2^2 B_0(p^2;m_2^2,m_2^2)\\
&-Jm_1m_2 B_0(p^2;m_2^2,m_1^2)
-Jm_2m_1 B_0(p^2;m_1^2,m_2^2)\big].
\end{aligned}

$$

若 $B_0$ 定义对两个质量参数对称，则两项混合质量函数相等，于是

$$

\boxed{\mathcal T_m(p^2)=4K m_1^2B_{11}+4K m_2^2B_{22}-4Jm_1m_2B_{12}},

$$

其中 $B_{ii}=B_0(p^2;m_i^2,m_i^2)$，$B_{12}=B_0(p^2;m_1^2,m_2^2)$。注意这里的 $B$ 组合是**迹分子对应的部分**；闭合费米子圈的负号、两个顶点的 $-i$ 因子、传播子因子和整体 $i$ 仍须按统一 1PI 约定加入。因此不能只凭这条迹公式单独宣布完整自能的整体正负号。

### 37.5 动量型部分的 PV 约化：质量依赖必须逐通道保留

对每个 $(i,j)$ 通道，使用

$$

k\cdot(k+p)=\frac12\left[k^2+(k+p)^2-p^2\right],

$$

并令

$$

D_i=k^2-m_j^2+i0,\qquad D_j=(k+p)^2-m_i^2+i0.

$$

则

$$

k^2=D_i+m_j^2-i0,\qquad (k+p)^2=D_j+m_i^2-i0.

$$

在维数正规化的平移不变积分中，忽略只用于标示极点位置的无穷小项后，分子积分可写成

$$

\int\frac{d^dk\,k\cdot(k+p)}{D_iD_j}
=\frac12\left[\int\frac{d^dk}{D_j}+\int\frac{d^dk}{D_i}
+(m_i^2+m_j^2-p^2)\int\frac{d^dk}{D_iD_j}\right].

$$

因此，按本节 PV 定义，结构为

$$

\frac12\left[A_0(m_i^2)+A_0(m_j^2)+(m_i^2+m_j^2-p^2)B_0(p^2;m_j^2,m_i^2)\right],

$$

但实际自能表达式仍需乘回原始迹中的 $2C_{ij}$ 以及统一圈因子。特别地，不能将每个通道的 $A_0$ 项在求和前删除；是否相消必须从 $C_{ij}$ 与具体质量函数的乘积求和后判断。

### 37.6 对旧候选表达式的影响

这一纠错足以否定“第 33 节的非对角 $D_{ij}$ 逐元表达式已被确认”这一说法，但尚不足以单独判定第 30 节总候选式的所有系数都错。原因是：第 30 节还涉及动量分子约化、整体费曼规则因子，以及是否将对称的两个混合质量通道合并。必须把每一项从第 37.2 节的迹公式开始重新生成，才能判断总式。

后续重算应按以下次序进行：

1. 把 $C_{ij}$ 与 $D_{ij}$ 分别代入每个通道的迹；
2. 保留各通道的 $A_0$ 与 $B_0$ 项，建立尚未乘整体圈因子的振幅表；
3. 按闭合费米子圈和两个 Yukawa 顶点的 Feynman 规则恢复整体因子；
4. 对 UV 极点的常数项和 $p^2$ 项分别求和；
5. 只有完成前四步后，才重新计算 $p^2$ 导数及小混合角近似。

### 37.7 本节结论

本节从完整手征顶点出发，确认了迹分子

$$

T_{ij}=2C_{ij}k\cdot(k+p)+2D_{ij}m_im_j

$$

并通过论文给出的矩阵逐项算出

$$

C=2K\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
D=\begin{pmatrix}2K&-J\\-J&2K\end{pmatrix}

$$

（实耦合约定）。这里最重要的结果是纠正此前错误的非对角质量翻转权重。完整 UV 自能的整体符号、所有 UV 极点和有限阈值常数仍未最终确认；下一步必须把上述通道级结果与原始 Feynman 规则结合，独立重建整条 1PI 振幅。

## 第 38 节：四个质量通道的完整 PV 表、整体费曼因子与 UV 极点复核

本节从第 37 节修正后的矩阵重新开始，完整保留四个有序内部质量通道。这里的目标是把迹层级结果、PV 约化、原始费曼规则和 UV 极点拆分为可独立核查的步骤。除非另有说明，以下采用实耦合，并定义

$$

A_i\equiv A_0(m_i^2),\qquad
B_{ij}\equiv B_0(p^2;m_i^2,m_j^2),\qquad
S_m\equiv m_1^2+m_2^2.

$$

PV 函数采用标准维数正规化约定，极点记为 $\Delta=1/\bar\epsilon$：

$$

A_0(m^2)=m^2\left[\Delta+1-\ln\frac{m^2}{\mu^2}\right],\qquad
B_0(p^2;a,b)=\Delta+\text{有限部分}.

$$

若使用不同的 $A_0,B_0$ 归一化，整体 $i/(16\pi^2)$ 必须相应调整；以下固定使用

$$

\int\frac{d^dk}{(2\pi)^d}\frac{1}{k^2-m^2+i0}
=\frac{i}{16\pi^2}A_0(m^2),\quad
\int\frac{d^dk}{(2\pi)^d}\frac{1}{D_1D_2}
=\frac{i}{16\pi^2}B_0.

$$

### 38.1 从第 37 节迹公式到单通道 PV 核

第 37 节的完整迹为

$$

T_{ij}=2C_{ij}\,k\cdot(k+p)+2D_{ij}m_im_j.

$$

由

$$

\int\frac{d^dk}{(2\pi)^d}\frac{k\cdot(k+p)}{D_1D_2}
\longrightarrow \frac{i}{16\pi^2}\frac12
\left[A_i+A_j+(m_i^2+m_j^2-p^2)B_{ij}\right]

$$

以及双传播子积分的 PV 定义，单个有序通道在尚未乘完整图整体因子之前的 PV 核为

$$

\boxed{F_{ij}=C_{ij}\left[A_i+A_j+(m_i^2+m_j^2-p^2)B_{ij}\right]
+2D_{ij}m_im_jB_{ij}.}

$$

这里的 $F_{ij}$ 不包括 $i/(16\pi^2)$ 和闭合费米子圈的整体符号。该式的第二项有明确的因子 2，来自迹中的 $2D_{ij}m_im_j$，不能再额外重复乘一个 2。

第 37 节给出的矩阵为

$$

C_{ij}=2K\begin{pmatrix}1&-1\\-1&1\end{pmatrix}_{ij},\qquad
D_{ij}=\begin{pmatrix}2K&-J\\-J&2K\end{pmatrix}_{ij}.

$$

所以四个有序通道分别如下。

### 38.2 四通道完整表达式

#### (a) $(1,1)$ 通道

$$

\begin{aligned}
F_{11}&=2K\left[2A_1+(2m_1^2-p^2)B_{11}\right]
+4Km_1^2B_{11}\\
&=\boxed{4KA_1+K(8m_1^2-2p^2)B_{11}}.
\end{aligned}

$$

#### (b) $(2,2)$ 通道

$$

\boxed{F_{22}=4KA_2+K(8m_2^2-2p^2)B_{22}}.

$$

#### (c) $(1,2)$ 通道

$$

\boxed{F_{12}=-2K(A_1+A_2)
+\left[-2K(S_m-p^2)-2Jm_1m_2\right]B_{12}}.

$$

#### (d) $(2,1)$ 通道
由于 $B_{21}=B_{12}$，并且本节实耦合下 $C_{21}=C_{12}$、$D_{21}=D_{12}$，有

$$

\boxed{F_{21}=-2K(A_1+A_2)
+\left[-2K(S_m-p^2)-2Jm_1m_2\right]B_{12}}.

$$

这里 $(1,2)$ 与 $(2,1)$ 是两个有序指标通道；在按矩阵迹求和时两者都要计入。若把它们合并，必须将整项乘 2，而不能只将某一个系数乘 2。

### 38.3 求和与 $A_0$ 项抵消

将四个有序通道相加，先看单传播子函数：

$$

4K(A_1+A_2)-2K(A_1+A_2)-2K(A_1+A_2)=0.

$$

因此 $A_0$ 项在完整四通道求和后严格抵消。这是逐项求和的结果，不是预先删掉 tadpole 型积分的许可。

总 PV 核为

$$

\boxed{\begin{aligned}
F(p^2)={}&K(8m_1^2-2p^2)B_{11}
+K(8m_2^2-2p^2)B_{22}\\
&+\left[-4K(S_m-p^2)-4Jm_1m_2\right]B_{12}.
\end{aligned}}

$$

这个表达式与第 30 节曾提出的候选组合在代数形式上相同；但现在它是由第 37 节修正后的 $C,D$ 矩阵和四个通道逐项推导出来的。这个一致性只能确认 PV 核的系数结构，不能替代整体费曼规则和 EFT 相减。

### 38.4 恢复原始费曼规则的整体因子

取标量相互作用约定

$$

\mathcal L_{\rm int}=-h\,\bar\chi\Gamma_h\chi-s\,\bar\chi\Gamma_s\chi,

$$

所以两个标量顶点分别为 $-i\Gamma_h$、$-i\Gamma_s$，费米子传播子分别为

$$

\frac{i(\slashed k+m_j)}{k^2-m_j^2+i0},\qquad
\frac{i(\slashed k+\slashed p+m_i)}{(k+p)^2-m_i^2+i0}.

$$

一个闭合 Dirac 费米子圈贡献额外的 $-1$。乘积的整体因子是

$$

(-1)_{\rm loop}\times(-i)^2_{\rm vertices}\times i^2_{\rm propagators}=-1.
$$

按 38.1 节 PV 积分归一化，图的 1PI 插入若定义为 $i\Pi_{hs}$，则

$$

\boxed{i\Pi_{hs}^{\rm 1PI}(p^2)=-\frac{i}{16\pi^2}F(p^2),\qquad
\Pi_{hs}^{\rm 1PI}(p^2)=-\frac{1}{16\pi^2}F(p^2).}

$$

这个整体符号依赖已明示的 $\mathcal L_{\rm int}$ 和 $i\Pi$ 约定；若全文采用相反的自能插入定义，应整体转换定义，不能只翻转某一项。以上没有额外的 $1/2$ 对称因子：两个外标量是不同场 $h,s$，且本计算按有序内部指标对求和。

### 38.5 各通道的 UV 极点：先逐项算，再求和

使用

$$

A_i\big|_{\rm UV}=m_i^2\Delta,\qquad B_{ij}\big|_{\rm UV}=\Delta,

$$

每个通道分别给出

$$

\boxed{F_{11}\big|_{\rm UV}=(12Km_1^2-2Kp^2)\Delta,}

$$

$$

\boxed{F_{22}\big|_{\rm UV}=(12Km_2^2-2Kp^2)\Delta,}

$$

$$

\boxed{F_{12}\big|_{\rm UV}=\left[-4K S_m+2Kp^2-2Jm_1m_2\right]\Delta,}

$$

$$

\boxed{F_{21}\big|_{\rm UV}=\left[-4K S_m+2Kp^2-2Jm_1m_2\right]\Delta.}

$$

注意，对角通道的 $12Km_i^2$ 中有 $4Km_i^2$ 来自 $A_i$，另有 $8Km_i^2$ 来自 $B_{ii}$；若遗漏 $A_0$ 极点，就会错误地得到质量发散系数。

相加后

$$

\begin{aligned}
F\big|_{\rm UV}
&=\left[12KS_m-4Kp^2-8KS_m+4Kp^2-4Jm_1m_2\right]\Delta\\
&=\boxed{4\left[K(m_1^2+m_2^2)-Jm_1m_2\right]\Delta}.
\end{aligned}

$$

因此：

- $p^2$ 型极点严格抵消；这与动量型耦合权重的总和为零相一致，但这里是通过完整 PV 系数逐项验证的。
- 质量型极点一般不为零，系数为 $4[K(m_1^2+m_2^2)-Jm_1m_2]$。它对应混合标量质量参数的局域反项需求，除非再利用模型参数关系证明括号恒等于零，否则不能宣称该极点消失。
- 按本节的 $i\Pi$ 约定，实际插入的极点是 $-i/(16\pi^2)$ 乘以上述 $F$ 的极点。相应反项的符号须从 $i\delta\Pi$ 与所选拉氏量参数约定一致地确定。

### 38.6 独立重算 $p^2$ 导数和有限部分

从 38.3 节总核直接求导，不使用此前任何渐近展开：

$$

\boxed{\begin{aligned}
F'(0)={}&K\left[8m_1^2B'_{11}(0)+8m_2^2B'_{22}(0)
-2B_{11}(0)-2B_{22}(0)+4B_{12}(0)\right]\\
&-4\left[KS_m+Jm_1m_2\right]B'_{12}(0).
\end{aligned}}

$$

其中导数符号表示对外部 $p^2$ 求导。对等质量两点函数，

$$

B_{ii}(0)=\Delta-\ln\frac{m_i^2}{\mu^2},\qquad
B'_{ii}(0)=\frac{1}{6m_i^2}.

$$

对非简并的混合质量通道，记 $a=m_1^2,b=m_2^2$，则

$$

B_{12}(0)=\Delta+1-\frac{a\ln(a/\mu^2)-b\ln(b/\mu^2)}{a-b},

$$

$$

\boxed{B'_{12}(0)=\frac{a+b}{2(a-b)^2}-\frac{ab}{(a-b)^3}\ln\frac{a}{b}.}

$$

当 $a\to b$ 时，后一式的连续极限为 $1/(6a)$。

代入对角导数后，也可写成

$$

\boxed{\begin{aligned}
F'(0)={}&K\left[\frac83-2B_{11}(0)-2B_{22}(0)+4B_{12}(0)-4S_m B'_{12}(0)\right]\\
&-4Jm_1m_2B'_{12}(0).
\end{aligned}}

$$

有限性可以直接检查：组合 $-2B_{11}-2B_{22}+4B_{12}$ 的 $\Delta$ 系数为 $-2-2+4=0$，而 $B'_0(0)$ 本身 UV 有限。所以 $F'(0)$ 不含 UV 极点。上面精确表达式保留了完整质量比；尚未对 $m_1/m_2\ll1$ 做近似，也没有将 EFT 低能贡献从 UV 结果中减去。

在当前约定下，

$$

\boxed{\left.\frac{d\Pi_{hs}^{\rm 1PI}}{dp^2}\right|_{p^2=0}=-\frac{1}{16\pi^2}F'(0).}

$$

这只是完整 UV 费米子圈的导数，不等于匹配后的 Wilson 系数；匹配系数需要减去 EFT 中相同轻自由度的泡图、接触图，并统一反项方案。

### 38.7 本节结论、修正范围与尚待完成的 EFT 步骤

**本节已独立完成：**

1. 明确写出 $(1,1),(2,2),(1,2),(2,1)$ 四个通道的全部 $A_0,B_0$ 系数；
2. 按一个闭合费米子圈、两个 $-i\Gamma$ 顶点和两个费米子传播子的规则恢复整体因子；
3. 分别列出四通道的质量型与 $p^2$ 型 UV 极点，证明总 $p^2$ 极点抵消，并保留质量型极点；
4. 从总 PV 核直接求导，给出精确质量比下的 $F'(0)$、$B_0(0)$ 和 $B'_0(0)$ 公式。

**尚未完成、不能提前宣称的事项：**

- 尚未从模型精确质量本征值与混合角恒等式进一步化简 $K(m_1^2+m_2^2)-Jm_1m_2$，故质量型极点是否能在该特定 UV 参数化下继续简化仍待核查。
- 尚未独立重算 EFT 侧泡图与 $hs\bar\ell\ell$ 接触顶点 tadpole 的全部符号和计数；因此本节的 $F'(0)$ 不是最终匹配结果。
- 尚未指定完整的门户耦合重整化条件和反项方案；质量型极点只能先解释为所选 1PI 两点函数需要局域反项，不能直接当成某个已匹配 Wilson 系数。
- 之前的 $14/3$、$-2/3$ 等有限常数仍不能引用为最终结果。下一步必须在同一 $i\Pi$ 约定下独立计算 EFT 泡图、接触图与相应反项，做 UV--EFT 相减后才可讨论有限阈值。

## 第 39 节：精确混合角恒等式、EFT 泡图/接触图及 MS-bar 相减

> **本节修正并推进第 38 节。** 第 38.5 节暂时把质量型极点写成“通常不为零、仍待利用精确质量关系检查”。本节完成该检查：在论文给定的精确质量本征值和混合角定义下，这个括号实际上恒等于零。因此，按第 38 节的 PV 核，质量型极点与动量型极点都消失。接下来将 EFT 泡图、接触图和 MS-bar 局域反项放进同一个约定中，并显式相减。有限阈值结果仍依赖所选算符投影和 EFT 截断阶数。

### 39.1 用精确质量本征值证明质量型极点消失

记轻、重质量分别为

$$

m\equiv m_1=m_\mu,\qquad M\equiv m_2=m_E,\qquad
\mathcal D\equiv m_2^2-m_1^2>0,

$$

并将 UV 拉氏量中的矢量类轻子裸质量记作 $M_E$，避免把它与精确重本征值 $m_2$ 混淆。精确本征值满足

$$

m_1m_2=m_Lm_R,\qquad m_1^2+m_2^2=M_E^2+m_L^2+m_R^2.

$$

论文混合角约定给出

$$

\sin2\theta_L=\frac{2m_LM_E}{\mathcal D},\qquad
\sin2\theta_R=\frac{2m_RM_E}{\mathcal D},

$$

因而

$$

c_Ls_L=\frac{m_LM_E}{\mathcal D},\qquad
c_Rs_R=\frac{m_RM_E}{\mathcal D}.

$$

所以

$$

\begin{aligned}
K&=ab\,c_Ls_Lc_Rs_R\\
 &=ab\frac{m_Lm_RM_E^2}{\mathcal D^2}
 =ab\frac{m_1m_2M_E^2}{\mathcal D^2}.
\end{aligned}

$$

另一方面，利用

$$

\cos2\theta_L=\frac{M_E^2+m_R^2-m_L^2}{\mathcal D},\qquad
\cos2\theta_R=\frac{M_E^2+m_L^2-m_R^2}{\mathcal D},

$$

可得

$$

\begin{aligned}
c_L^2c_R^2+s_L^2s_R^2
&=\frac{1+\cos2\theta_L\cos2\theta_R}{2}\\
&=\frac{M_E^2(M_E^2+m_L^2+m_R^2)}{\mathcal D^2}\\
&=\frac{M_E^2(m_1^2+m_2^2)}{\mathcal D^2}.
\end{aligned}

$$

因此

$$

J=ab\frac{M_E^2(m_1^2+m_2^2)}{\mathcal D^2},

$$

并得到关键的**精确恒等式**

$$

\boxed{Jm_1m_2=K(m_1^2+m_2^2).}

$$

这不是小混合角近似，而是精确质量本征值和精确混合角关系的结果（假定第 35 节所用的实参数及角度符号约定）。

将其代入第 38.5 节的总极点：

$$

F\big|_{\rm UV}=4[K(m_1^2+m_2^2)-Jm_1m_2]\Delta=0.

$$

结合第 38 节已逐通道验证的 $p^2\Delta$ 系数也为零，可知**在这组 UV 费米子圈图的总和中，质量型与动量型 UV 极点均抵消**。因此，第 38.5 节中“质量型极点一般仍不为零”的暂定说法由本节结果取代。这里说的是该完整费米子圈总和的极点；它不意味着门户耦合在所有重整化方案中都不需要参数定义，也不排除模型其他图或其他耦合阶数的贡献。

### 39.2 EFT 破缺相耦合与计数约定

在最低阶维数五 EFT 的破缺相展开中，采用文档此前固定的耦合：

$$

\mathcal L_{\rm EFT}\supset
-g_hh\bar\ell\ell-g_ss\bar\ell\ell-g_{hs}hs\bar\ell\ell,

$$

其中

$$

g_h=\frac{m}{v_h},\qquad g_s=\frac{m}{v_s},\qquad
g_{hs}=\frac{m}{v_hv_s},\qquad g_hg_s=mg_{hs}\equiv g=\frac{m^2}{v_hv_s}.

$$

这里 $m=m_1$ 是 EFT 的轻费米子质量。树级 EFT 按 $1/M_E$ 展开时，$g$ 与 UV 质量基底的 $K$ 在领先阶相同；若保留有限混合角的高阶修正，必须同时改用匹配到同一阶的精确 EFT Yukawa 与接触耦合，不能只把某一个耦合替换成精确值。

统一沿用第 38 节的插入约定：每个图写为

$$

i\Pi^{\rm loop}=-\frac{i}{16\pi^2}F^{\rm loop}.

$$

PV 函数约定为

$$

A_0(m^2)=m^2\left[\Delta+1-\ln\frac{m^2}{\mu^2}\right],\qquad
B_0(p^2;m^2,m^2)=\Delta+\overline B_{mm}(p^2),

$$

其中 $\Delta=1/\bar\epsilon$，并定义有限部分

$$

\overline A_0(m^2)\equiv A_0(m^2)-m^2\Delta
=m^2\left(1-\ln\frac{m^2}{\mu^2}\right),

$$

$$

\overline B_{ij}(p^2)\equiv B_{ij}(p^2)-\Delta.

$$

### 39.3 EFT 泡图：从完整迹到 PV 核

两个 Yukawa 顶点分别给出 $-ig_h$ 与 $-ig_s$。闭合费米子圈负号、两个顶点和两个传播子的因子按第 38.4 节的顺序合并；Dirac 迹为

$$

\operatorname{Tr}[(\slashed k+m)(\slashed k+\slashed p+m)]
=4[k\cdot(k+p)+m^2].

$$

用

$$

\int\frac{d^dk}{(2\pi)^d}\frac{k\cdot(k+p)}{D_1D_2}
\longrightarrow \frac{i}{16\pi^2}\frac12
\left[2A_0(m^2)+(2m^2-p^2)B_0(p^2;m^2,m^2)\right]

$$

进行 PV 约化，泡图核为

$$

\boxed{F_{\rm bub}^{\rm EFT}(p^2)
=g\left[4A_0(m^2)+(8m^2-2p^2)B_{mm}(p^2)\right].}

$$

这条式子里的 $4A_0$ 来自动量分子约化，$8m^2B_0$ 同时包含动量分子和迹中的显式 $m^2$ 项；不能把二者混并或漏掉。

### 39.4 EFT 接触图：单传播子 tadpole

接触顶点为 $-ig_{hs}$，圈中只有一个轻费米子传播子。传播子分子取迹后

$$

\operatorname{Tr}(\slashed k+m)=4m,

$$

奇函数的 $\slashed k$ 项积分为零。按相同闭合圈与 Minkowski 积分约定，接触图给出

$$

\boxed{F_{\rm ct}^{\rm EFT}=4m g_{hs}A_0(m^2)=4gA_0(m^2).}

$$

接触图没有外部动量分子，所以对 $p^2$ 的导数为零。总 EFT 圈核为

$$

\boxed{F_{\rm EFT}^{\rm loop}(p^2)
=g\left[8A_0(m^2)+(8m^2-2p^2)B_{mm}(p^2)\right].}

$$

其极点为

$$

\boxed{F_{\rm EFT}^{\rm loop}\big|_{\rm UV}
=g(16m^2-2p^2)\Delta.}

$$

这说明在破缺相低能理论里，泡图和接触图各自都有局域发散；它们的质量型极点并不相互抵消。该发散必须由 EFT 的局域反项吸收。

### 39.5 EFT 反项与 MS-bar 重整化

在上述 $i\Pi=-iF/(16\pi^2)$ 约定下，EFT 圈图的极点插入是

$$

\left.i\Pi_{\rm EFT}^{\rm loop}\right|_{\rm UV}
=-\frac{i}{16\pi^2}g(16m^2-2p^2)\Delta.

$$

因此，反项图必须提供相反的插入：

$$

\boxed{i\Pi_{\rm EFT}^{\rm ct}\big|_{\rm pole}
=+\frac{i}{16\pi^2}g(16m^2-2p^2)\Delta.}

$$

在破缺相二点函数投影里，常数项由局域质量/门户型参数反项吸收，$p^2$ 项由动能混合或相应导数算符反项吸收。要写成未破缺相规范不变算符时，必须回到完整 $\Phi_{\ell i}=S_\ell H_i$ 的导数算符组合；不能只将 $p^2$ 极点任意归给某一个单独的 $(S^\dagger S)(D H)^\dagger D H$ 算符。

定义 MS-bar 去极点后的有限 PV 函数 $\overline A_0,\overline B_0$，则重整化 EFT 圈核为

$$

\boxed{F_{\rm EFT}^{\overline{\rm MS}}(p^2)
=g\left[8\overline A_0(m^2)+(8m^2-2p^2)\overline B_{mm}(p^2)\right].}

$$

这相当于从裸圈核中减去 $g(16m^2-2p^2)\Delta$。这里的反项符号是按 1PI 插入定义写的；若把反项写入拉氏量，必须同时说明二次项的 Fourier 与自能符号约定，不能把上式的插入符号直接当作拉氏量系数。

### 39.6 UV 与重整化 EFT 相减：有限硬部分

利用精确恒等式 $JmM=K(m^2+M^2)$，第 38.3 节 UV 核可重写为

$$

\begin{aligned}
F_{\rm UV}(p^2)=K\big[&(8m^2-2p^2)B_{mm}(p^2)
+(8M^2-2p^2)B_{MM}(p^2)\\
&+(-8(m^2+M^2)+4p^2)B_{mM}(p^2)\big].
\end{aligned}

$$

由于三项的 $B_0$ 极点系数相加为零，整个 UV 核有限。以最低阶 EFT 匹配 $g=K$ 并减去 MS-bar 重整化 EFT 泡图加接触图后，定义有限的硬匹配核

$$

F_{\rm hard}(p^2)\equiv F_{\rm UV}(p^2)-F_{\rm EFT}^{\overline{\rm MS}}(p^2),

$$

得到轻质量同通道的非局域项完全相消：

$$

\boxed{\begin{aligned}
F_{\rm hard}(p^2)=K\big[&(8M^2-2p^2)\overline B_{MM}(p^2)\\
&+(-8(m^2+M^2)+4p^2)\overline B_{mM}(p^2)
-8\overline A_0(m^2)\big].
\end{aligned}}

$$

这是在“破缺相标量二点函数投影、最低阶 EFT 耦合、MS-bar 去极点”这些明示条件下的有限差额。常数项属于局域门户/质量参数的阈值匹配；它不能在没有给出门户参数重整化条件时直接称为唯一可观测量。

### 39.7 硬部分的 $p^2$ 导数与小质量比极限

对上式求导，$A_0$ 项不依赖外动量，得到

$$

\boxed{\begin{aligned}
F'_{\rm hard}(0)=K\big[&-2\overline B_{MM}(0)+8M^2B'_{MM}(0)\\
&+4\overline B_{mM}(0)-8(m^2+M^2)B'_{mM}(0)\big].
\end{aligned}}

$$

这里

$$

\overline B_{MM}(0)=-\ln\frac{M^2}{\mu^2},\qquad
B'_{MM}(0)=\frac{1}{6M^2},

$$

以及

$$

\overline B_{mM}(0)=1-
\frac{m^2\ln(m^2/\mu^2)-M^2\ln(M^2/\mu^2)}{m^2-M^2},

$$

$$

B'_{mM}(0)=\frac{m^2+M^2}{2(m^2-M^2)^2}
-\frac{m^2M^2}{(m^2-M^2)^3}\ln\frac{m^2}{M^2}.

$$

对 $r=m^2/M^2\ll1$ 展开，

$$

\overline B_{mM}(0)=1-\ln\frac{M^2}{\mu^2}+O(r\ln r),\qquad
B'_{mM}(0)=\frac{1}{2M^2}+O\!\left(\frac{r\ln r}{M^2}\right).

$$

因此

$$

\boxed{F'_{\rm hard}(0)=K\left[\frac43-2\ln\frac{M^2}{\mu^2}\right]
+O(Kr\ln r).}

$$

在 $\mu=M$ 的 MS-bar 匹配尺度下，领先阶是 $F'_{\rm hard}(0)=\frac43K+O(Kr\ln r)$。按第 38 节插入约定，1PI 导数为 $\Pi'_{\rm hard}(0)=-F'_{\rm hard}(0)/(16\pi^2)$。这仍是指定投影下的硬差额；把它映射到未破缺相独立 Wilson 算符系数，还需完整算符基底、场重定义和波函数归一化。

### 39.8 结果边界与后续检查

1. **精确质量型 UV 极点已证明抵消。** 关键是 $Jm_1m_2=K(m_1^2+m_2^2)$，不应继续引用第 38.5 节原先“质量极点一般不为零”的暂定判断。
2. **EFT 泡图与接触图已在同一插入约定下重算。** 它们的合计极点是 $g(16m^2-2p^2)\Delta$，由相应局域反项消除。
3. **已给出 MS-bar 重整化后 UV–EFT 相减的有限表达式。** 在最低阶匹配 $g=K$ 下，轻轻通道的 $B_{mm}$ 非局域依赖被显式消掉。
4. **尚不能把该二点投影直接等同于唯一的维数六 Wilson 系数。** 还需要将导数结构约化到明确的规范不变算符基底，并把动能混合、门户参数和外场归一化的重整化条件一并固定。
5. 若后续采用精确有限混合角而非最低阶 EFT，需将 $g_h,g_s,g_{hs}$ 同步匹配到同一阶，再重新计算 EFT 相减；不能混用精确 UV 耦合和截断 EFT 接触项。

## 第 40 节：把破缺相二点函数导数投影到规范不变维数六算符——可确定的组合与不可过度解释的系数

### 40.1 本节目标与约定

第 39 节得到的是特定外态投影下的硬区差额，而不是自动等于某个唯一 Wilson 系数。本节把它与规范不变算符联系起来，同时区分：

- **由当前计算直接确定的量**：破缺相径向模的混合二点函数中，硬区局域项的 $p^2$ 系数；
- **在指定算符基底后才能定义的量**：各个独立维数六算符的 Wilson 系数；
- **仍需其他 Green 函数才能完成的量**：将所有导数算符、波函数重整化、参数重整化和场重定义统一后的完整匹配系数。

继续采用前文约定

$$

i\Pi_{hs}^{\rm hard}(p^2)=-\frac{i}{16\pi^2}F'_{\rm hard}(0)\,p^2+O(p^4),

$$

其中第 39 节的领先阶结果为

$$

F'_{\rm hard}(0)=K\left[\frac43-2\ln\frac{M^2}{\mu^2}\right]+O(Kr\ln r),\qquad r=\frac{m^2}{M^2}.

$$

注意：上式的符号是沿用第 38–39 节所声明的 1PI 插入约定；把它转成拉氏量局域项时必须继续使用同一约定，不能另行凭直觉翻转符号。

### 40.2 一个自然的规范不变维数六算符

定义复合场

$$

\Phi_i\equiv S_\ell H_i,

$$

其中 $S_\ell$ 按相应轻子 flavor 的规范荷选取为 $S$ 或 $S^\dagger$。一个自然的维数六导数算符是

$$

\boxed{\mathcal O_{\Phi D}=(D_\mu\Phi_i)^\dagger D^\mu\Phi_i.}

$$

其系数记为 $C_{\Phi D}/\Lambda^2$，故

$$

\Delta\mathcal L=\frac{C_{\Phi D}}{\Lambda^2}\mathcal O_{\Phi D}.

$$

这里 $C_{\Phi D}/\Lambda^2$ 的质量维数为 $-2$。该算符是规范不变的，但它不一定是完整维数六基底中唯一的导数算符；它只是一个方便的基底方向。

展开乘积导数：

$$

\begin{aligned}
\mathcal O_{\Phi D}={}&(S_\ell^\dagger S_\ell)(D_\mu H)^\dagger D^\mu H
+(H^\dagger H)(D_\mu S_\ell)^\dagger D^\mu S_\ell\\
&+(D_\mu S_\ell)^\dagger S_\ell\,H^\dagger D^\mu H
+S_\ell^\dagger D_\mu S_\ell\,(D^\mu H)^\dagger H.
\end{aligned}

$$

因此，不能只保留第一项并把剩余三项丢掉；那样既改变算符，也会改变破缺相中径向模的混合动能投影。

### 40.3 破缺相径向模展开与二点投影

为展示归一化，暂时忽略规范场并只取径向模，采用

$$

H^0=\frac{v_h+h}{\sqrt2},\qquad S_\ell=\frac{v_s+s}{\sqrt2}.

$$

则

$$

\Phi^0=\frac{(v_s+s)(v_h+h)}{2},

$$

从而

$$

\begin{aligned}
\partial_\mu\Phi^{0*}\partial^\mu\Phi^0
={}&\frac{v_s^2}{4}(\partial h)^2+\frac{v_h^2}{4}(\partial s)^2
+\frac{v_hv_s}{2}\,\partial_\mu h\,\partial^\mu s\\
&+\text{含三条或四条涨落场的项}.
\end{aligned}

$$

因此，如果在一个明确指定的算符基底/场定义中，$\mathcal O_{\Phi D}$ 是唯一贡献到该径向混合动能的局域算符方向，那么它的系数对 $hs$ 二点函数导数的贡献与 $C_{\Phi D}v_hv_s/(2\Lambda^2)$ 成正比。具体正负号要由第 40.1 节的 1PI 约定与二次拉氏量的 Fourier 规则一起固定。

但一般的维数六 EFT 还可能包含其他导数算符，例如

$$

\mathcal O_{H\Box S}=(H^\dagger H)\Box(S^\dagger S),\qquad
\mathcal O_{HS\partial}=\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S),

$$

以及按分部积分、运动方程和规范表示选取的等价算符。它们在破缺相可能对同一 $hs$ 的 $p^2$ 结构作出贡献。因此仅凭一个二点函数，通常只能确定这些系数的一个线性组合，而不能唯一分解出每个 Wilson 系数。

### 40.4 当前硬差额能确定到哪一步

第 39 节的结果给出

$$

\Pi_{hs,\rm hard}'(0)=-\frac{K}{16\pi^2}
\left[\frac43-2\ln\frac{M^2}{\mu^2}\right]+O(Kr\ln r).

$$

在匹配尺度 $\mu=M$ 时，

$$

\boxed{\Pi_{hs,\rm hard}'(0)=-\frac{K}{12\pi^2}+O(Kr\ln r).}

$$

这是一条无量纲的混合动能投影。若人为选择一个单算符投影，并定义局域二次项的符号使得

$$

\Pi_{hs,\rm local}'(0)=-\frac{C_{\Phi D}}{\Lambda^2}\frac{v_hv_s}{2},

$$

那么该**投影定义下**可写

$$

\boxed{\frac{C_{\Phi D}}{\Lambda^2}
=\frac{2K}{12\pi^2v_hv_s}+O\!\left(\frac{Kr\ln r}{v_hv_s}\right)
=\frac{K}{6\pi^2v_hv_s}+O\!\left(\frac{Kr\ln r}{v_hv_s}\right).}

$$

这个等式是对所定义的单算符投影的条件性翻译，**不是**完整 SMEFT/扩展标量 EFT 中已经唯一确定的 Wilson 系数。若所选基底中另有算符对同一二点函数有贡献，上式右侧对应的是其系数组合，而不是单独 $C_{\Phi D}$。

### 40.5 还必须完成的匹配检查

要把上述投影提升为完整 Wilson 系数，至少需要：

1. **固定算符基底**：列出所有在该 UV 场内容与对称性下允许、并在所需耦合阶数出现的维数六导数算符；声明分部积分与 EOM 约化规则。
2. **匹配更多外态振幅**：除 $hs\to hs$ 或混合二点函数外，至少计算能区分 $(S^\dagger S)(D H)^\dagger D H$、$(H^\dagger H)(D S)^\dagger D S$ 与交叉导数项的独立 Green 函数/外腿排列。
3. **统一场重整化**：明确 UV 与 EFT 的外场波函数重整化条件；若采用 on-shell 场定义或 $\overline{\rm MS}$ 场定义，UV 和 EFT 两侧必须一致。
4. **统一参数重整化**：将 $v_h,v_s,m,M_E$、混合角与 Yukawa 耦合的重整化定义固定到相同方案，避免把参数重整化贡献误计为新的导数 Wilson 系数。
5. **检查 IR 一致性**：UV 与 EFT 两侧使用相同轻场质量/外动量规约，逐项相减轻场非解析项；匹配系数只能来自硬区局域部分。
6. **回代验证**：用得到的系数组合预测另一个独立外态振幅；若无法重现，就说明基底不完整或场重定义/反项处理仍有遗漏。

### 40.6 本节结论

当前计算已将一圈 UV–EFT 差额推进到一个明确的破缺相混合动能投影，并展示了它如何嵌入规范不变的复合场导数算符。当前可报告的数值是 $\mu=M$ 时 $\Pi'_{hs,\rm hard}(0)=-K/(12\pi^2)+O(Kr\ln r)$。将它写成 $K/(6\pi^2v_hv_s)$ 的系数，只在本文明确声明的单算符投影约定下成立；不能把它误称为已经完成的唯一 Wilson 系数匹配。下一步应固定完整算符基底并计算能区分上述算符的独立振幅。

## 第 41 节：维数六导数算符的投影矩阵——二点函数只能确定线性组合

### 41.1 目的与约定

第 40 节已经说明，破缺相径向模的混合二点函数只提供一个动量结构系数。现在显式建立一组便于投影的规范不变算符，并计算其对该二点函数的贡献。除非另有说明，取复 singlet 标量 $S$、标准模型 Higgs 双重态 $H$，并采用

$$

H^0=\frac{v_h+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2}

$$

的实径向模约定；此处只为抽取二点投影而暂时令 Goldstone 和规范场为零。该简化不替代完整规范不变匹配。

### 41.2 一组方便的规范不变导数算符

在分部积分（IBP）关系尚未约化之前，考虑下列四个实算符方向：

$$

\begin{aligned}
\mathcal O_H&=(H^\dagger H)(D_\mu S)^\dagger D^\mu S,\\
\mathcal O_S&=(S^\dagger S)(D_\mu H)^\dagger D^\mu H,\\
\mathcal O_\partial&=\partial_\mu(H^\dagger H)\,\partial^\mu(S^\dagger S),\\
\mathcal O_J&=\big(H^\dagger i\overleftrightarrow D_\mu H\big)
                 \big(S^\dagger i\overleftrightarrow D^\mu S\big),
\end{aligned}

$$

其中 $X^\dagger i\overleftrightarrow D_\mu X\equiv iX^\dagger D_\mu X-i(D_\mu X)^\dagger X$。若 UV 理论的额外离散对称性排除某一方向，需根据完整拉氏量再删去；此处先保留它们，以免过早假定基底不完整。

各算符都具有质量维数六。它们不是在所有可能的 EOM/IBP 约化方案下都彼此独立；这里的用途是把不同外腿结构与径向二点投影分开记账，而不是宣称这已经是最终最小基底。

### 41.3 对 $h$–$s$ 二点函数的投影

在上述径向展开下，保留恰含一个 $h$、一个 $s$ 的双线性导数项：

- $\mathcal O_H$ 含 $v_h^2(\partial s)^2/4$，但没有 $\partial h\,\partial s$ 双线性项；
- $\mathcal O_S$ 含 $v_s^2(\partial h)^2/4$，但没有 $\partial h\,\partial s$ 双线性项；
- $\mathcal O_\partial$ 满足
  
$$

  \partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S)
  =v_hv_s\,\partial_\mu h\partial^\mu s+\cdots;
  
$$

- 对纯径向实背景，$H^\dagger i\overleftrightarrow D_\mu H$ 与 $S^\dagger i\overleftrightarrow D_\mu S$ 在令规范场和 Goldstone 为零后均不产生径向双线性项，因此 $\mathcal O_J$ 对该简化投影的贡献为零。

若拉氏量中含

$$

\Delta\mathcal L=\frac{1}{\Lambda^2}\left(C_H\mathcal O_H+C_S\mathcal O_S+C_\partial\mathcal O_\partial+C_J\mathcal O_J\right),

$$

则此径向二点投影的混合动能系数只读出

$$

\boxed{c_{hs}^{(\partial)}=\frac{v_hv_s}{\Lambda^2}C_\partial}

$$

（本节将拉氏量中的交叉项定义为 $+c_{hs}^{(\partial)}\partial h\partial s$）。因此，单靠这一二点函数无法测出 $C_H,C_S,C_J$；它只对 $C_\partial$ 在该未约化基底下的系数敏感。若通过 IBP、EOM 或场重定义把 $\mathcal O_\partial$ 换成其他算符，系数标签会改变，但物理振幅不变。

### 41.4 复合算符 $|D(SH)|^2$ 与此基底的关系

定义

$$

\mathcal O_{\Phi D}=\big[D_\mu(SH_i)\big]^\dagger D^\mu(SH_i),

$$

并对 $i$ 求和。展开可得

$$

\mathcal O_{\Phi D}=\mathcal O_H+\mathcal O_S+\mathcal O_{\rm cross},

$$

其中

$$

\mathcal O_{\rm cross}=(D_\mu S)^\dagger S\,H^\dagger D^\mu H
+S^\dagger D_\mu S\,(D^\mu H)^\dagger H.

$$

用 $a_\mu=S^\dagger D_\mu S$、$b_\mu=H^\dagger D_\mu H$，有

$$

\partial_\mu(S^\dagger S)=a_\mu+a_\mu^*,\qquad
S^\dagger i\overleftrightarrow D_\mu S=i(a_\mu-a_\mu^*),

$$

且对 $H$ 有相同恒等式。于是

$$

\boxed{\mathcal O_{\rm cross}=\frac12\mathcal O_\partial+\frac12\mathcal O_J.}

$$

所以

$$

\boxed{\mathcal O_{\Phi D}=\mathcal O_H+\mathcal O_S+
\frac12\mathcal O_\partial+\frac12\mathcal O_J.}

$$

这与径向展开直接一致：$\mathcal O_H$、$\mathcal O_S$ 不贡献 $hs$ 双线性混合动能，$\mathcal O_J$ 在纯径向投影下不贡献，而 $\frac12\mathcal O_\partial$ 给出 $v_hv_s\partial h\partial s/2$。因此第 40 节中的 $C_{\Phi D}v_hv_s/2$ 因子是正确的，但它只适用于 UV–EFT 差额确实匹配到 $\mathcal O_{\Phi D}$ 这一特定组合的情形。

### 41.5 从 1PI 导数到投影系数：符号与归一化

定义局域拉氏量的交叉项为

$$

\Delta\mathcal L_{\rm local}=c_{hs}\,\partial_\mu h\partial^\mu s.

$$

在动量空间，该项的二点插入为 $-ic_{hs}p^2$。因此若采用前文约定

$$

i\Pi_{hs}^{\rm hard}(p^2)=-i\,\Pi_{hs,\rm coeff}'(0)\,p^2+O(p^4),

$$

即把 $\Pi_{hs,\rm coeff}'(0)$ 定义为局域交叉动能系数，则

$$

\boxed{c_{hs}=\Pi_{hs,\rm coeff}'(0).}

$$

此处特意把“1PI 函数导数”和“拉氏量交叉动能系数”分别命名，避免将 $i\Pi$、$\Pi$ 与局域系数的符号混为一谈。若某一章节采用不同的 $i\Pi$ 定义，应先换算到这个定义，再作匹配。

按第 39 节当前的硬差额，

$$

\Pi_{hs,\rm coeff}'(0)=-\frac{K}{16\pi^2}
\left[\frac43-2\ln\frac{M^2}{\mu^2}\right]+O(Kr\ln r).

$$

于是，在此交叉动能定义下

$$

\boxed{\frac{C_\partial}{\Lambda^2}=
-\frac{K}{16\pi^2v_hv_s}
\left[\frac43-2\ln\frac{M^2}{\mu^2}\right]+O\!\left(\frac{Kr\ln r}{v_hv_s}\right).}

$$

这个等式只是在上述未约化算符基底、场定义与 1PI 符号约定下对 $C_\partial$ 的投影匹配。它不能与第 40 节中针对 $\mathcal O_{\Phi D}$ 的条件性系数不加转换地同时使用：若选择 $\mathcal O_{\Phi D}$ 作为基底方向，其对 $C_\partial$ 的贡献是 $C_{\Phi D}/2$，并且同时产生 $\mathcal O_H,\mathcal O_S,\mathcal O_J$ 项。

### 41.6 哪些独立振幅能区分这些算符

为了完成系数匹配，至少还要匹配以下外态结构：

1. $S H\to S H$ 的四标量振幅，保留一般外动量并分别投影 $p_H^2,p_S^2,p_H\cdot p_S$，可区分 $\mathcal O_H,\mathcal O_S,\mathcal O_\partial$ 的动量结构；
2. 含规范场外腿的相关振幅，或等价的规范协变背景场计算，以检查 $\mathcal O_J$ 与规范协变导数项；
3. 在选定 EOM/IBP 约化后，至少用一个独立 Green 函数验证该基底变换没有漏项。

单个径向 $hs$ 二点函数只给出一个系数，不足以求解所有维数六导数 Wilson 系数。完成上述独立振幅前，最终匹配结果应写成已确定的投影组合，而不是一个声称唯一的系数表。

### 41.7 本节结论与审计标记

- 本节给出了径向二点投影与算符基底关系；后续路径级盒图计算见第 60 节。

## 第 60 节：将具体 Yukawa 矩阵代入 16 条路径的平移后手征系数

本节把第 59 节的路径级规则实际代入第 37 节的两个 $2\times2$ Yukawa 矩阵。为了让结果可复核且不把不同路径的分母混在一起，先对每条路径分别计算手征系数，再用少量公共多项式压缩表格。这里的系数是**平移前分子迹的手征分解系数**；路径的 Feynman 参数权重仍由本路径自己的 $\Delta_{0,\rho}$ 决定。

### 60.1 系数定义

对路径 $\rho=(a,b,c,d)$，继续使用

$$
(u_1,u_2,u_3,u_4)=\big((Y_h)_{ab},(Y_s)_{bc},(Y_h)_{cd},(Y_s)_{da}\big),
$$
$$
(v_1,v_2,v_3,v_4)=\big((Y_h)_{ba},(Y_s)_{cb},(Y_h)_{dc},(Y_s)_{ad}\big),
$$
以及边质量 $\mu=(m_b,m_c,m_d,m_a)$。定义交替手征系数

$$
H_\rho=u_1v_2u_3v_4+v_1u_2v_3u_4,
$$
零斜线质量系数

$$
M_\rho=\mu_1\mu_2\mu_3\mu_4
(u_1u_2u_3u_4+v_1v_2v_3v_4),
$$
并对每一对动量斜线边 $i<j$ 定义

$$
C_{ij}^{(\rho)}=
\sum_{\substack{\sigma\in\{R,L\}^4\\
\text{转变边恰为 }\{i,j\}}}
\left(\prod_{r=1}^4 c_r(\sigma_r)\right)
\left(\prod_{r\notin\{i,j\}}\mu_r\right),
\quad c_r(R)=u_r,\ c_r(L)=v_r.
$$

则零外动量分子精确写为

$$
N_\rho^{(0)}(K)=2\left[K^4H_\rho+K^2\sum_{i<j}C_{ij}^{(\rho)}+M_\rho\right].
$$
平移后至二阶的分子修正中，两斜线项为 $2\sum_{i<j}C_{ij}^{(\rho)}t_i\cdot t_j$；四斜线项使用第 59.3 节的 $d$ 维平均式。完整振幅还必须加上 $-4\delta\Delta$ 乘以 $N_\rho^{(0)}$ 对应的五次分母项。

### 60.2 压缩记号

为列出具体矩阵代入结果，定义

$$
P=a^2b^2c_L^2c_R^2s_L^2s_R^2,
$$
$$
T=a^2b^2c_Lc_Rs_Ls_R(c_L^2c_R^2+s_L^2s_R^2),
$$
$$
W=a^2b^2m_1^2m_2^2(c_L^4c_R^4+s_L^4s_R^4),
$$
以及

$$
P_1=2Pm_1^2,\qquad P_2=2Pm_2^2,\qquad T_{12}=Tm_1m_2.
$$
质量系数表中的简写为

$$
M_{1111}=2Pm_1^4,\quad M_{\mathrm{mix}}=2Pm_1^2m_2^2,
\quad M_{2222}=2Pm_2^4,
$$
$$
M_{31}=-Tm_1^3m_2,\qquad M_{13}=-Tm_1m_2^3,
\quad M_{\mathrm{alt}}=W.
$$
注意 $M_{31}$ 和 $M_{13}$ 已包含负号。

### 60.3 16 条路径的精确系数表

表中 $H_\rho$ 是 $K^4$ 前的系数，$M_\rho$ 是不含 $K$ 的质量项系数，$C_{12},\ldots,C_{34}$ 按边对顺序排列。**每一行均须配上自己的参数分母**

$$
\Delta_{0,\rho}=x_1m_b^2+x_2m_c^2+x_3m_d^2+x_4m_a^2,
$$
而不能先把表中各行简单相加再套同一个积分核。

| 路径 $\rho$ | $H_\rho$ | $M_\rho$ | $C_{12}$ | $C_{13}$ | $C_{14}$ | $C_{23}$ | $C_{24}$ | $C_{34}$ |
|---|---:|---|---|---|---|---|---|---|
| 1111 | $+2P$ | $M_{1111}$ | $P_1$ | $P_1$ | $P_1$ | $P_1$ | $P_1$ | $P_1$ |
| 1112 | $-2P$ | $M_{31}$ | $-T_{12}$ | $-P_1$ | $-T_{12}$ | $-P_1$ | $-T_{12}$ | $-P_1$ |
| 1121 | $-2P$ | $M_{31}$ | $-P_1$ | $-T_{12}$ | $-T_{12}$ | $-P_1$ | $-P_1$ | $-T_{12}$ |
| 1122 | $+2P$ | $M_{\mathrm{mix}}$ | $T_{12}$ | $T_{12}$ | $P_2$ | $P_1$ | $T_{12}$ | $T_{12}$ |
| 1211 | $-2P$ | $M_{31}$ | $-P_1$ | $-P_1$ | $-P_1$ | $-T_{12}$ | $-T_{12}$ | $-T_{12}$ |
| 1212 | $+2P$ | $M_{\mathrm{alt}}$ | $T_{12}$ | $P_1$ | $T_{12}$ | $T_{12}$ | $P_2$ | $T_{12}$ |
| 1221 | $+2P$ | $M_{\mathrm{mix}}$ | $P_1$ | $T_{12}$ | $T_{12}$ | $T_{12}$ | $T_{12}$ | $P_2$ |
| 1222 | $-2P$ | $M_{13}$ | $-T_{12}$ | $-T_{12}$ | $-P_2$ | $-T_{12}$ | $-P_2$ | $-P_2$ |
| 2111 | $-2P$ | $M_{31}$ | $-T_{12}$ | $-T_{12}$ | $-P_1$ | $-T_{12}$ | $-P_1$ | $-P_1$ |
| 2112 | $+2P$ | $M_{\mathrm{mix}}$ | $P_2$ | $T_{12}$ | $T_{12}$ | $T_{12}$ | $T_{12}$ | $P_1$ |
| 2121 | $+2P$ | $M_{\mathrm{alt}}$ | $T_{12}$ | $P_2$ | $T_{12}$ | $T_{12}$ | $P_1$ | $T_{12}$ |
| 2122 | $-2P$ | $M_{13}$ | $-P_2$ | $-P_2$ | $-P_2$ | $-T_{12}$ | $-T_{12}$ | $-T_{12}$ |
| 2211 | $+2P$ | $M_{\mathrm{mix}}$ | $T_{12}$ | $T_{12}$ | $P_1$ | $P_2$ | $T_{12}$ | $T_{12}$ |
| 2212 | $-2P$ | $M_{13}$ | $-P_2$ | $-T_{12}$ | $-T_{12}$ | $-P_2$ | $-P_2$ | $-T_{12}$ |
| 2221 | $-2P$ | $M_{13}$ | $-T_{12}$ | $-P_2$ | $-T_{12}$ | $-P_2$ | $-T_{12}$ | $-P_2$ |
| 2222 | $+2P$ | $M_{2222}$ | $P_2$ | $P_2$ | $P_2$ | $P_2$ | $P_2$ | $P_2$ |

该表由逐路径枚举四个顶点的 $2^4$ 种手征赋值、筛选转变边数为 $0,2,4$，并代入第 37 节矩阵元后整理得到。它是矩阵元级系数表，不是积分后的振幅表。

### 60.4 符号交叉检查

逐项求和检查得到

$$
\sum_{\rho}H_\rho=0,\qquad
\sum_{\rho}C_{ij}^{(\rho)}=0\quad (\forall i<j),
$$
其中这里的路径求和是**不带不同质量分母权重的纯代数和**。这与最高 $K^4$ 系数的抵消一致，并对所有六个 $K^2t_i\cdot t_j$ 系数提供了额外的代数检查；但它**不**意味着真实有限振幅为零，因为每条路径的 $\Delta_{0,\rho}$ 不同，且 $M_\rho$ 与分母修正项仍然存在。另一个逐路径检查是：$C_{ij}^{(\rho)}$ 的质量维数为 2，$H_\rho$ 为无质量维数，$M_\rho$ 的质量维数为 4，与分子中 $K^4,K^2,M^4$ 三类项的维数一致。

### 60.5 下一步：系数表与参数积分核配对

现在可以对每条路径 $\rho$ 构造

$$
\mathcal A_\rho^{(2)}=6\int_{\mathrm{simplex}}d^4x\,\delta\!\left(1-\sum_i x_i\right)
\left[\frac{\langle\widetilde N_\rho^{[2]}\rangle_K}{(K^2+\Delta_{0,\rho})^4}
-4\delta\Delta\frac{\langle N_\rho^{[0]}\rangle_K}{(K^2+\Delta_{0,\rho})^5}\right]_{\!\int K},
$$

其中 $\langle\cdots\rangle_K$ 包含第 59 节的 $d$ 维角向平均，圈积分按 $I_r^{(4)}$ 与 $I_r^{(5)}$ 约化。下一步应把表中的 $H_\rho,M_\rho,C_{ij}^{(\rho)}$ 与每条路径的 $\Delta_{0,\rho}$ 配对，逐一提取 $q_i^2$、$q_i\cdot q_j$ 的参数积分系数；之后还需加入所有不等价外腿排列，并计算 EFT 同基底振幅作 UV–EFT 相减。

**结果边界：** 本节确实完成了 16 条路径的具体 Yukawa 矩阵代入和手征系数求和，但没有完成 Feynman 参数积分、完整盒图外腿排列求和、EFT 相减或最终 Wilson 系数提取。

## 第 61 节：将 16 路径系数表直接配对到六个二阶动量不变量的参数积分核

第 60 节已经得到每条路径的 $H_\rho,M_\rho,C_{ij}^{(\rho)}$。本节把它们与平移后的点积和 $I_r^{(n)}$ 配对，给出可以直接用于数值积分或进一步解析积分的六个系数核。这一步仍保留路径标签 $\rho$，所以不会把不同 $\Delta_{0,\rho}$ 的积分错误合并。

### 61.1 六个动量不变量与 $t_i\cdot t_j$ 系数

记六个独立不变量为
$$
(\mathcal Q_1,\ldots,\mathcal Q_6)=
(q_1^2,q_2^2,q_3^2,q_1\cdot q_2,q_1\cdot q_3,q_2\cdot q_3),
$$
并定义参数多项式向量 $f_{ij}$，使

$$
t_i\cdot t_j=\sum_{\alpha=1}^{6}f_{ij,\alpha}(x)\mathcal Q_\alpha.
$$
令 $A=x_2+x_3$，各向量按上述六个不变量的顺序排列：

$$
\begin{aligned}
f_{12}={}&\big(x_4^2,\ A(A-1),\ x_3^2,\ -x_4(2A-1),\ -2x_3x_4,\ x_3(2A-1)\big),\\
f_{13}={}&\big(x_4^2,\ A(A-1),\ x_3(x_3-1),\ -x_4(2A-1),\ -x_4(2x_3-1),\ 2x_2x_3-x_2+2x_3^2-2x_3\big),\\
f_{14}={}&\big(x_4(x_4-1),\ A^2,\ x_3^2,\ -A(2x_4-1),\ -x_3(2x_4-1),\ 2x_3A\big),\\
f_{23}={}&\big(x_4^2,\ (A-1)^2,\ x_3(x_3-1),\ -2x_4(A-1),\ -x_4(2x_3-1),\ (2x_3-1)(A-1)\big),\\
f_{24}={}&\big(x_4(x_4-1),\ A(A-1),\ x_3^2,\ -2x_4A+A+x_4-1,\ -x_3(2x_4-1),\ x_3(2A-1)\big),\\
f_{34}={}&\big(x_4(x_4-1),\ A(A-1),\ x_3(x_3-1),\ -2x_4A+A+x_4-1,\ -2x_3x_4+x_3+x_4-1,\ 2x_2x_3-x_2+2x_3^2-2x_3\big).
\end{aligned}
$$

这些多项式由第 59.1 节的 $t_i$ 直接点乘得到。一个快速检查是 $f_{ij}=f_{ji}$；此外每个分量至多二次于 Feynman 参数，且不含质量参数。

### 61.2 四斜线修正的系数向量

定义 $g_\alpha$ 为第 59.3 节四斜线平均括号

$$
\mathcal G_t=t_1\cdot t_2+t_3\cdot t_4-t_1\cdot t_3-t_2\cdot t_4+t_1\cdot t_4+t_2\cdot t_3
+\frac{2}{d}(t_1\cdot t_3+t_2\cdot t_4)
$$
在 $\mathcal Q_\alpha$ 前的系数。因而无需再独立展开长多项式，只需使用精确关系

$$
\boxed{g=f_{12}+f_{34}-f_{13}-f_{24}+f_{14}+f_{23}+\frac{2}{d}(f_{13}+f_{24})}.
$$
必须在这里保留 $d=4-2\epsilon$。例如，$g_1=x_4(d+2)(2x_4-1)/d$，$g_3=x_3(d+2)(2x_3-1)/d$；它们可用于核对向量公式的展开。

### 61.3 分母位移的六个系数

写成

$$
\delta\Delta=\sum_{\alpha=1}^6 d_\alpha(x)\mathcal Q_\alpha,
$$
则

$$
\begin{aligned}
(d_1,d_2,d_3,d_4,d_5,d_6)=\big(&x_4(1-x_4),\ A(1-A),\ x_3(1-x_3),\\
&2x_4A,\ 2x_3x_4,\ 2x_3(1-A)\big).
\end{aligned}
$$
这与第 58.7 节完全一致。特别地，混合不变量 $q_i\cdot q_j$ 的系数包含显式因子 2；不要把它与定义为 $2q_i\cdot q_j$ 的另一种基底混用。

### 61.4 每条路径、每个不变量的完整积分核

令

$$
S_\rho=\sum_{i<j}C_{ij}^{(\rho)},\qquad
\Delta_{0,\rho}=x_1m_b^2+x_2m_c^2+x_3m_d^2+x_4m_a^2.
$$
按第 49、58 节定义欧氏积分 $I_r^{(n)}(\Delta)$。在固定外腿顺序和当前整体迹归一化下，第 $\rho$ 条路径对 $\mathcal Q_\alpha$ 的系数核为

$$
\boxed{
\begin{aligned}
\mathcal K_{\rho,\alpha}(x)={}&2\left[\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}(x)\right]I_0^{(4)}(\Delta_{0,\rho})\\
&+2H_\rho g_\alpha(x)I_1^{(4)}(\Delta_{0,\rho})\\
&-8d_\alpha(x)\left[H_\rho I_2^{(5)}(\Delta_{0,\rho})+S_\rho I_1^{(5)}(\Delta_{0,\rho})+M_\rho I_0^{(5)}(\Delta_{0,\rho})\right].
\end{aligned}}
$$
因此固定 $(h,s,h,s)$ 排列的二阶系数可以写成

$$
\mathcal C_\alpha^{(hshs)}=6\sum_{\rho\in\{1,2\}^4}\int_{\mathrm{simplex}}d^4x\,\delta\!\left(1-\sum_i x_i\right)\mathcal K_{\rho,\alpha}(x).
$$
第一行来自两斜线分子的 $t_i\cdot t_j$；第二行来自四斜线迹的 $d$ 维角向平均；第三行是分母二阶位移乘以零阶完整迹。第三行系数为 $-8$，因为分母展开贡献 $-4\delta\Delta$，而零阶迹为 $2(HK^4+SK^2+M)$。这个因子检查很重要，不能误写成 $-4$。

### 61.5 量纲与极限检查

- $C_{ij}$ 的质量维数为 2，$f_{ij,\alpha}$ 无量纲；故第一行的积分核维数与 $q^2$ 系数相符。
- $H$ 无质量维数，$g_\alpha$ 无量纲；$I_1^{(4)}$ 与第一行具有相同的总质量维数。
- 第三行中 $H I_2^{(5)}$、$S I_1^{(5)}$ 和 $M I_0^{(5)}$ 的维数相同，因此可以相加。
- 在相同参数分母的纯代数高动量极限，$\sum_\rho H_\rho=0$ 和 $\sum_\rho C_{ij}^{(\rho)}=0$；但实际参数积分仍含不同的 $\Delta_{0,\rho}$，不允许把这些无权重恒等式误用于有限振幅抵消。

### 61.6 下一步与边界

本节已经把第 60 节的具体路径系数表配对到每个二阶外动量不变量，得到可直接数值积分的六个路径级核。下一步是对单纯形参数作解析或数值积分、对 $d=4-2\epsilon$ 的极点和有限项一致展开，再对全部不等价外腿排列求和。最后仍需在同一算符基底下计算 EFT 的一圈振幅并相减。

**当前结果边界：** $\mathcal K_{\rho,\alpha}$ 是固定 $(h,s,h,s)$ 外腿排列的路径级积分核；它不是完成所有排列和 EFT 相减后的 Wilson 系数。完整匹配前还需要统一顶点、传播子、闭环负号和外腿排列的 Feynman 规则整体归一化。

## 第 62 节：将路径级积分核化为四维有限的显式有理函数

第 61 节已经把每条路径的六个系数写成 $I_r^{(n)}(\Delta_{0,\rho})$ 的组合。本节对实际出现的五种积分逐一做维数正规化，并把结果代回路径核。这是一次真实的简化：不再把主积分留作未计算符号，同时检查二阶动量系数是否需要 UV 极点抵消。

### 62.1 主积分的通用表达式

采用欧氏约定

$$
I_r^{(n)}(\Delta)=\bar\mu^{2\epsilon}\int\frac{d^dK_E}{(2\pi)^d}\frac{(K_E^2)^r}{(K_E^2+\Delta)^n},\qquad d=4-2\epsilon,
$$

则

$$
I_r^{(n)}(\Delta)=\frac{\bar\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\frac{\Gamma(r+2-\epsilon)\Gamma(n-r-2+\epsilon)}
{\Gamma(2-\epsilon)\Gamma(n)}\Delta^{2+r-n-\epsilon}.
$$

对第 61 节所需的 $I_0^{(4)},I_1^{(4)},I_2^{(5)},I_1^{(5)},I_0^{(5)}$，Gamma 函数的第二个参数在 $\epsilon\to0$ 时均为正整数，因此这些积分在 UV 上有限，没有 $1/\epsilon$ 极点。故它们的有限部分可直接取 $d\to4$；但这一操作是在先确认各积分有限之后进行的，不应推广到含发散积分的其他振幅。

### 62.2 五种积分的四维结果

直接代入 Gamma 函数并使用 $\Gamma(n)=(n-1)!$，得到

$$
\begin{aligned}
I_0^{(4)}(\Delta)&=\frac{1}{16\pi^2}\frac{1}{6\Delta^2}+O(\epsilon),\\
I_1^{(4)}(\Delta)&=\frac{1}{16\pi^2}\frac{1}{3\Delta}+O(\epsilon),\\
I_2^{(5)}(\Delta)&=\frac{1}{16\pi^2}\frac{1}{4\Delta}+O(\epsilon),\\
I_1^{(5)}(\Delta)&=\frac{1}{16\pi^2}\frac{1}{12\Delta^2}+O(\epsilon),\\
I_0^{(5)}(\Delta)&=\frac{1}{16\pi^2}\frac{1}{12\Delta^3}+O(\epsilon).
\end{aligned}
$$

量纲逐项为 $-4,-2,-2,-4,-6$，分别与 $r-n$ 的积分量纲一致。这里的 $O(\epsilon)$ 仅表示有限积分的维数展开余项；因为没有 UV 极点与之相乘，不会产生额外的有限贡献。

### 62.3 代回每条路径的六个系数核

第 61.4 节的路径核为

$$
\begin{aligned}
\mathcal K_{\rho,\alpha}={}&2\left[\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}\right]I_0^{(4)}(\Delta_{0,\rho})
+2H_\rho g_\alpha I_1^{(4)}(\Delta_{0,\rho})\\
&-8d_\alpha\left[H_\rho I_2^{(5)}(\Delta_{0,\rho})+S_\rho I_1^{(5)}(\Delta_{0,\rho})+M_\rho I_0^{(5)}(\Delta_{0,\rho})\right].
\end{aligned}
$$

将上面五个积分逐项代入，化为

$$
\boxed{\begin{aligned}
\mathcal K_{\rho,\alpha}(x)=\frac{1}{16\pi^2}\bigg\{&
\frac{1}{3\Delta_{0,\rho}^{2}}\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}(x)
+\frac{2H_\rho}{3\Delta_{0,\rho}}g_\alpha(x)\\
&-d_\alpha(x)\left[\frac{2H_\rho}{\Delta_{0,\rho}}
+\frac{2S_\rho}{3\Delta_{0,\rho}^{2}}
+\frac{2M_\rho}{3\Delta_{0,\rho}^{3}}\right]\bigg\}.
\end{aligned}}
$$

这是固定 $(h,s,h,s)$ 外腿顺序下、路径 $\rho$ 的四维显式积分核。它只含已知 Yukawa 多项式、Feynman 参数多项式和 $\Delta_{0,\rho}$ 的幂，不再含未求值的圈动量积分。固定排列的系数仍为

$$
\mathcal C_\alpha^{(hshs)}=6\sum_{\rho\in\{1,2\}^4}\int_{x_i\ge0}d^4x\,\delta\!\left(1-\sum_i x_i\right)\mathcal K_{\rho,\alpha}(x),
$$

其中参数单纯形上的整体因子 $6=\Gamma(4)$ 已单独写出，不能再把它重复吸收到 $\mathcal K$ 中。

### 62.4 UV 有限性结论的适用范围

二阶外动量系数中出现的积分只有上述五种，均为 UV 收敛积分。因此，在固定外腿排列、已按第 61 节分子与分母展开的盒图部分中，$O(q^2)$ 系数本身不需要靠不同路径之间的 UV 极点抵消才能有限。这与零外动量 $K^4$ 项的对数极点讨论是两件不同的事：后者涉及 $I_2^{(4)}$ 一类对数发散积分，而这里出现的是 $I_2^{(5)}$ 等更高分母幂次的收敛积分。

这项结论只针对目前固定排列的盒图二阶系数，不自动证明完整 UV–EFT 匹配的其他图、波函数重整化或反项均已处理完毕。整体 Feynman 规则符号、其他不等价外腿排列以及 EFT 相减仍需另行完成。

### 62.5 下一步

现在可以把第 60 节的表逐行代入第 62.3 节，形成 16 项、每项六个分量的显式参数积分。因为 $\Delta_{0,\rho}$ 只依赖于参数中对应 $m_1^2$ 与 $m_2^2$ 的权重和，进一步的解析化简可以按路径中 $m_1,m_2$ 的出现位置进行分组；但不能仅按质量出现次数合并，因为 $f_{ij,\alpha}$ 与 $C_{ij}^{(\rho)}$ 还记住环边位置。

**结果边界：** 本节完成了路径级圈积分的解析执行与 UV 收敛性检查，但尚未完成 16 项参数积分、全部外腿排列求和、EFT 一圈振幅相减或最终 Wilson 系数提取。

## 第 63 节：圈积分标准公式的逐步推导与当前计算的完整性清单

本节把此前对话中解释的圈积分推导正式写入文档。需要先说明：本文件此前已有主积分公式、五种有限积分的结果和路径级积分核，但并没有把从 Schwinger 参数到 Gamma 函数的每一步都完整写出；而且完整的 UV–EFT 匹配仍未结束。

### 63.1 从多传播子分母到单一分母

对固定内部质量路径，设

$$
A_i=(k+r_i)^2+m_i^2,\qquad N=\sum_{i=1}^4\nu_i.
$$

Feynman 参数恒等式为

$$
\frac{1}{\prod_{i=1}^4 A_i^{\nu_i}}
=\frac{\Gamma(N)}{\prod_i\Gamma(\nu_i)}
\int_{x_i\ge0}d^4x\,\delta\!\left(1-\sum_i x_i\right)
\frac{\prod_i x_i^{\nu_i-1}}{(\sum_i x_i A_i)^N}.
$$

将平方项展开：

$$
\sum_i x_i A_i=k^2+2k\cdot R+\sum_i x_i(r_i^2+m_i^2),\qquad R=\sum_i x_i r_i.
$$

平移圈动量 $K=k+R$，于是

$$
\sum_i x_i A_i=K^2+\Delta,\qquad
\Delta=\sum_i x_i m_i^2+\sum_i x_i r_i^2-R^2.
$$

若只提取至外动量二阶，可写 $\Delta=\Delta_0+\delta\Delta$，其中

$$
\Delta_0=\sum_i x_i m_i^2,\qquad
\delta\Delta=\sum_i x_i r_i^2-R^2=O(q^2),
$$
并展开

$$
\frac{1}{(K^2+\Delta)^N}
=\frac{1}{(K^2+\Delta_0)^N}
-N\frac{\delta\Delta}{(K^2+\Delta_0)^{N+1}}+O(q^4).
$$

此式只展开分母；完整二阶振幅还要将平移后的分子展开至同阶，并保留分子与分母的乘积项。

### 63.2 Schwinger 参数与高斯动量积分

定义欧氏标量积分

$$
I_r^{(n)}(\Delta)=\bar\mu^{2\epsilon}\int\frac{d^dK_E}{(2\pi)^d}
\frac{(K_E^2)^r}{(K_E^2+\Delta)^n},\qquad d=4-2\epsilon.
$$

当积分可先在收敛区域定义、再解析延拓时，使用

$$
\frac{1}{(K_E^2+\Delta)^n}
=\frac{1}{\Gamma(n)}\int_0^\infty dt\,t^{n-1}e^{-t(K_E^2+\Delta)}.
$$

代入并交换积分次序：

$$
I_r^{(n)}=\frac{\bar\mu^{2\epsilon}}{\Gamma(n)}
\int_0^\infty dt\,t^{n-1}e^{-t\Delta}
\int\frac{d^dK_E}{(2\pi)^d}(K_E^2)^r e^{-tK_E^2}.
$$

高斯积分为

$$
\int\frac{d^dK_E}{(2\pi)^d}(K_E^2)^r e^{-tK_E^2}
=\frac{1}{(4\pi)^{d/2}}
\frac{\Gamma(r+d/2)}{\Gamma(d/2)}t^{-r-d/2}.
$$

因此

$$
I_r^{(n)}=\frac{\bar\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(r+d/2)}{\Gamma(d/2)\Gamma(n)}
\int_0^\infty dt\,t^{n-r-d/2-1}e^{-t\Delta}.
$$

最后使用 Gamma 积分

$$
\int_0^\infty dt\,t^{z-1}e^{-t\Delta}=\Gamma(z)\Delta^{-z},
\qquad z=n-r-d/2,
$$
得到

$$
\boxed{
I_r^{(n)}(\Delta)=\frac{\bar\mu^{2\epsilon}}{(4\pi)^{d/2}}
\frac{\Gamma(r+d/2)\Gamma(n-r-d/2)}
{\Gamma(d/2)\Gamma(n)}\Delta^{d/2+r-n}.
}
$$
对于 UV 发散积分，该表达式按维数正规化的解析延拓理解；不能把 Schwinger 参数积分在其原始收敛区间之外当作普通收敛积分。

### 63.3 五种有限积分的逐项代入

令 $d=4-2\epsilon$，故 $d/2=2-\epsilon$。对于下列五种积分，Gamma 函数在 $\epsilon\to0$ 时不产生极点，因此可以直接取四维极限：

$$
I_0^{(4)}:\quad \frac{\Gamma(2)\Gamma(2)}{\Gamma(2)\Gamma(4)}\Delta^{-2}
=\frac{1}{6\Delta^2},
$$

$$
I_1^{(4)}:\quad \frac{\Gamma(3)\Gamma(1)}{\Gamma(2)\Gamma(4)}\Delta^{-1}
=\frac{1}{3\Delta},
$$

$$
I_2^{(5)}:\quad \frac{\Gamma(4)\Gamma(1)}{\Gamma(2)\Gamma(5)}\Delta^{-1}
=\frac{1}{4\Delta},
$$

$$
I_1^{(5)}:\quad \frac{\Gamma(3)\Gamma(2)}{\Gamma(2)\Gamma(5)}\Delta^{-2}
=\frac{1}{12\Delta^2},
$$

$$
I_0^{(5)}:\quad \frac{\Gamma(2)\Gamma(3)}{\Gamma(2)\Gamma(5)}\Delta^{-3}
=\frac{1}{12\Delta^3}.
$$

每行均须乘上公共因子 $1/(16\pi^2)$。由此重得第 62 节的五个结果。它们分别具有质量维数 $-4,-2,-2,-4,-6$，与积分定义相符。

### 63.4 对数发散积分的例子：$I_2^{(4)}$

这里 $r=2,n=4$，因此

$$
I_2^{(4)}=\frac{\bar\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\frac{\Gamma(4-\epsilon)\Gamma(\epsilon)}
{\Gamma(2-\epsilon)\Gamma(4)}\Delta^{-\epsilon}.
$$

用

$$
\frac{\Gamma(4-\epsilon)}{\Gamma(2-\epsilon)\Gamma(4)}
=\frac{(3-\epsilon)(2-\epsilon)}{6}
=1-\frac56\epsilon+O(\epsilon^2),
$$
以及

$$
\Gamma(\epsilon)=\frac1\epsilon-\gamma_E+O(\epsilon),\qquad
\Delta^{-\epsilon}=1-\epsilon\ln\Delta+O(\epsilon^2),
$$
并按 MS-bar 组合尺度整理，可得

$$
\boxed{
I_2^{(4)}(\Delta)=\frac{1}{16\pi^2}
\left[\frac1{\bar\epsilon}-\ln\frac{\Delta}{\bar\mu^2}-\frac56\right]+O(\epsilon),
\qquad \frac1{\bar\epsilon}=\frac1\epsilon-\gamma_E+\ln4\pi.
}
$$
这说明对数极点来自 $\Gamma(\epsilon)$。不能把它与第 62 节中五种 UV 收敛积分的有限性混为一谈。

### 63.5 张量积分的约化与维数因子

在旋转对称的欧氏积分中，若被积函数只依赖 $K_E^2$，则

$$
\int d^dK_E\,K_E^\mu K_E^\nu F(K_E^2)
=\frac{\delta^{\mu\nu}}{d}\int d^dK_E\,K_E^2F(K_E^2).
$$

四阶张量对应

$$
\int d^dK_E\,K_E^\mu K_E^\nu K_E^\rho K_E^\sigma F(K_E^2)
=\frac{\delta^{\mu\nu}\delta^{\rho\sigma}+\delta^{\mu\rho}\delta^{\nu\sigma}+\delta^{\mu\sigma}\delta^{\nu\rho}}{d(d+2)}
\int d^dK_E\,(K_E^2)^2F(K_E^2).
$$

如果张量约化因子乘上发散标量积分，必须保留 $d=4-2\epsilon$ 到乘法完成后再展开，因为 $O(\epsilon)$ 乘 $1/\epsilon$ 会贡献有限项。对于第 62 节那五个已经确认有限的标量积分，取 $d\to4$ 不会因这一机制丢失有限项；但四斜线角向平均中的显式 $1/d$ 仍应在最终与其余项组合前保持一致。

### 63.6 Wick 转动和整体振幅符号的边界

以上 $I_r^{(n)}$ 是按欧氏定义的标量积分。它们本身不决定完整 Minkowski 振幅的整体 $i$ 因子或符号。要从原始振幅得到正确整体符号，仍需同时跟踪：每个费米子传播子的 $i(\slashed k+m)/(k^2-m^2+i0)$、每个标量传播子、每个顶点的 $i$ 因子、闭合费米子环的负号、积分测度的 Wick 转动，以及动量分子中每个 $k^2\to-K_E^2$ 的替换。故本节只验证标量积分值，不把它当成完整振幅符号的独立证明。

### 63.7 当前文档是否包含全部细节：明确清单

**已经写入文档的内容：**

1. 零外动量盒图的手征迹结构、质量路径分组和相关的 $A_n,Q_n,B_n$ 组织方式（第 46–50 节）。
2. 固定外腿路由下的分母二阶展开、Feynman 参数平移与 $\delta\Delta$（第 53、56–59 节）。
3. 16 条内部质量路径的 $H_\rho,M_\rho,C_{ij}^{(\rho)}$ 系数表（第 60 节）。
4. 六个外动量不变量的路径级积分核，以及五种 UV 收敛标量积分的四维结果（第 61–62 节）。
5. 本节给出的 Schwinger 参数推导、Gamma 函数公式、发散积分示例和张量积分恒等式。

**尚未完成或尚未在文档中逐项展开的内容：**

1. 从 UV 拉氏量的原始 Feynman 规则开始，对每一张不等价盒图逐个写出所有顶点、传播子、闭环符号和外腿排列因子。
2. 对 16 条路径、每条路径的六个不变量进行完整的参数积分；第 62 节目前给出的是待积的有理函数核，不是已算出的积分值。
3. 独立计算 EFT 一圈图、EFT 反项及相同动量路由下的振幅，并执行 UV–EFT 相减。
4. 把结果投影到指定的非冗余算符基底，处理分部积分、运动方程、场重定义和算符混合。
5. 对完整匹配结果进行重整化尺度与规范/基底一致性检查，并据此确认或否定早先的候选 Wilson 系数。

因此，本文件是**详细的阶段性推导记录，但不是完整的最终匹配计算**。特别是第 60–62 节虽有明确系数表与积分核，不能将它们误称为已完成的参数积分或最终 Wilson 系数。


## 第 64 节：16 条路径的参数积分解析化——从三维单纯形积分降为有限个超几何函数

本节开始执行第 62 节留下的实际参数积分。由于 $m_1,m_2$ 尚未指定数值，不能把结果诚实地写成单一数值；这里将每个参数积分精确化为有限个 Gauss 超几何函数 ${}_2F_1$ 的和。对本问题中整数参数的 ${}_2F_1$，还可进一步化成有理函数与 $\ln(m_1^2/m_2^2)$ 的组合。这样做既保留一般质量比，又把三维积分真正解析执行到一维特殊函数的闭式表达。

**重要边界：** 本节计算的是第 62 节定义的固定 $(h,s,h,s)$ 排列积分核。此前写出的整体因子 $6$ 暂按该核的定义保留；它是否与原始 Feynman 图的排列/对称因子相容，仍须在第 65 节从原始 Feynman 规则独立核实。因此，本节的参数积分是精确的，但尚不等同于完整物理振幅。

### 64.1 先把每个路径的核拆成三个标准分母幂次

把第 62.3 节的核重新排列，定义三个参数多项式

$$
\begin{aligned}
B_{\rho\alpha}^{(1)}(x)
&=H_\rho\left(\frac23g_\alpha(x)-2d_\alpha(x)\right),\\
B_{\rho\alpha}^{(2)}(x)
&=\frac13\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}(x)
-\frac23S_\rho d_\alpha(x),\\
B_{\rho\alpha}^{(3)}(x)
&=-\frac23M_\rho d_\alpha(x),
\qquad S_\rho=\sum_{i<j}C_{ij}^{(\rho)}.
\end{aligned}
$$

于是对每个路径 $\rho$ 和每个动量不变量 $\mathcal Q_\alpha$，

$$
\boxed{
\mathcal K_{\rho\alpha}(x)=\frac{1}{16\pi^2}
\left[
\frac{B_{\rho\alpha}^{(1)}(x)}{\Delta_{0,\rho}}
+\frac{B_{\rho\alpha}^{(2)}(x)}{\Delta_{0,\rho}^{\,2}}
+\frac{B_{\rho\alpha}^{(3)}(x)}{\Delta_{0,\rho}^{\,3}}
\right].
}
$$

这一步是逐项代数重排，不作近似。它也使量纲检查更直接：$B^{(1)}$ 的维数为 0，$B^{(2)}$ 的维数为 2，$B^{(3)}$ 的维数为 4，因此三个分式都具有质量维数 $-2$。

固定排列下第 $\alpha$ 个二阶动量系数为

$$
\mathcal C_\alpha^{(hshs)}
=\frac{6}{16\pi^2}\sum_{\rho}
\sum_{p=1}^{3}
\int_{\sum x_i=1,\,x_i\geq0}
d^4x\,\delta\!\left(1-\sum_i x_i\right)
\frac{B_{\rho\alpha}^{(p)}(x)}{\Delta_{0,\rho}^{\,p}}.
$$

这里的 $d^4x\,\delta(1-\sum x_i)$ 表示四个非负参数上的三维单纯形测度；不是四维独立体积积分。

### 64.2 对一般单项式积分作精确约化

对一条路径，传播子边质量按顺序为

$$
(\mu_1,\mu_2,\mu_3,\mu_4)=(m_b,m_c,m_d,m_a),
$$

因此

$$
\Delta_{0,\rho}=\sum_{i=1}^4x_i\mu_i^2.
$$

令 $I_\rho$ 为该路径上质量等于 $m_1$ 的参数指标集合，$k=|I_\rho|$。其余 $4-k$ 个边质量为 $m_2$。对任意四元非负整数指数 $n=(n_1,n_2,n_3,n_4)$，定义

$$
N=\sum_{i=1}^4n_i,\qquad N_1=\sum_{i\in I_\rho}n_i.
$$

需要的基本积分是

$$
J_p(n;I_\rho)=
\int_{\rm simplex}
\frac{x_1^{n_1}x_2^{n_2}x_3^{n_3}x_4^{n_4}}
{\left(\sum_i x_i\mu_i^2\right)^p}\,d^4x\,\delta\!\left(1-\sum_i x_i\right).
$$

#### 64.2.1 将单纯形分成两组参数

对 $0<k<4$，令

$$
z=\sum_{i\in I_\rho}x_i,\qquad
x_i=zu_i\ (i\in I_\rho),\qquad
x_j=(1-z)v_j\ (j\notin I_\rho),
$$

其中 $\sum_{i\in I_\rho}u_i=1$、$\sum_{j\notin I_\rho}v_j=1$。单纯形测度分解为

$$
d\mu_3=z^{k-1}(1-z)^{3-k}\,dz\,d\mu_{k-1}(u)\,d\mu_{3-k}(v).
$$

分母只依赖 $z$：

$$
\Delta_{0,\rho}=z\,m_1^2+(1-z)m_2^2.
$$

而两个内部单纯形积分分别是 Dirichlet 积分：

$$
\int d\mu_{k-1}(u)\prod_{i\in I_\rho}u_i^{n_i}
=\frac{\prod_{i\in I_\rho}\Gamma(n_i+1)}
{\Gamma(N_1+k)},
$$

$$
\int d\mu_{3-k}(v)\prod_{j\notin I_\rho}v_j^{n_j}
=\frac{\prod_{j\notin I_\rho}\Gamma(n_j+1)}
{\Gamma(N-N_1+4-k)}.
$$

把这些因子与剩余的 $z$ 积分合并，利用 Euler 积分表示，得到

$$
\boxed{
J_p(n;I_\rho)=
\frac{\prod_{i=1}^4 n_i!}{(N+3)!}
\frac{1}{(m_2^2)^p}
{}_2F_1\!\left(
p,N_1+k;N+4;1-\frac{m_1^2}{m_2^2}
\right),\quad 0<k<4.
}
$$

这个表达式是精确等式，不是近似。它对 $m_1,m_2>0$ 成立；当质量相等时，超几何函数的自变量为 0，因 ${}_2F_1(a,b;c;0)=1$，公式平滑退化到普通单纯形矩。

若 $k=0$，则分母恒为 $m_2^{2p}$；若 $k=4$，分母恒为 $m_1^{2p}$。两种端点情况直接为

$$
J_p(n;\varnothing)=\frac{\prod_i n_i!}{(N+3)!(m_2^2)^p},\qquad
J_p(n;\{1,2,3,4\})=\frac{\prod_i n_i!}{(N+3)!(m_1^2)^p}.
$$

这一步把原先的三维参数积分降为一个标准特殊函数。由于 $p=1,2,3$ 且 $N_1+k,N+4$ 都是整数，结果可通过递推或对 Euler 积分作多项式除法写成有理函数与对数的组合；保留 ${}_2F_1$ 形式则更紧凑，并更容易做数值稳定性检查。

### 64.3 每个路径、每个不变量的积分现在都成为有限求和

把三个多项式分别按四个参数展开：

$$
B_{\rho\alpha}^{(p)}(x)=
\sum_{n_1,n_2,n_3,n_4\geq0}
b_{\rho\alpha n}^{(p)}
x_1^{n_1}x_2^{n_2}x_3^{n_3}x_4^{n_4},
$$

其中只有有限多个系数 $b_{\rho\alpha n}^{(p)}$ 非零。代入上节的单项式积分公式，便得到

$$
\boxed{
\mathcal C_\alpha^{(hshs)}
=\frac{6}{16\pi^2}\sum_{\rho}\sum_{p=1}^3
\sum_{n_1,n_2,n_3,n_4}
b_{\rho\alpha n}^{(p)}J_p(n;I_\rho).
}
$$

这是 16 条路径和六个动量不变量各自的完整解析积分表达式。这里的 $b_{\rho\alpha n}^{(p)}$ 不需要猜测或拟合：它们由第 60 节路径表、第 61 节的 $f_{ij,\alpha},g_\alpha,d_\alpha$ 以及 64.1 节的定义唯一确定。因每个 $B^{(p)}$ 都是至多二次的参数多项式，有限和很短。

为了把实际展开规模明确列出来，以下给出符号展开后每个动量不变量中 $B^{(1)},B^{(2)},B^{(3)}$ 的非零单项式数。每格格式为“$n_1/n_2/n_3$”，不是数值积分结果；它用于核对多项式是否漏项。由于六个不变量只改变外动量多项式，路径表中的单项式数对 16 条路径相同：

| 动量不变量 | $B^{(1)}$ 单项式数 | $B^{(2)}$ 单项式数 | $B^{(3)}$ 单项式数 |
|---|---:|---:|---:|
| $q_1^2$ | 2 | 2 | 2 |
| $q_2^2$ | 6 | 6 | 5 |
| $q_3^2$ | 2 | 2 | 2 |
| $q_1\cdot q_2$ | 6 | 6 | 2 |
| $q_1\cdot q_3$ | 4 | 4 | 1 |
| $q_2\cdot q_3$ | 5 | 5 | 3 |

因此每条路径、每个 $\alpha$ 都只需要把表中对应数量的单项式逐项乘以 $J_p\)。对 16 条路径逐一套用同一公式，即已把原始的 $16\times6$ 个三维积分化成可机器精确求和的有限表达式。不同路径的质量指标集合 $I_\rho$ 不同，所以不能在代入 $J_p$ 前把路径系数先相加。

### 64.4 哪些路径能合并，哪些不能

单从分母看，16 条路径按质量 $m_1$ 出现于四条传播子边中的次数 $k$ 分为五类：

| $k$（$m_1$ 边数） | 路径数 | 分母的代表形式 |
|---:|---:|---|
| 0 | 1 | $m_2^2$ |
| 1 | 4 | $z m_1^2+(1-z)m_2^2$，其中 $z$ 对应一个参数 |
| 2 | 6 | $z m_1^2+(1-z)m_2^2$，其中 $z$ 对应两个参数之和 |
| 3 | 4 | $z m_1^2+(1-z)m_2^2$，其中 $z$ 对应三个参数之和 |
| 4 | 1 | $m_1^2$ |

因此，在**积分算法**层面，16 条路径确实可归入五种质量重数类；这正是上节超几何函数中只出现 $k$ 和 $N_1$ 的原因。但这不代表每一类的振幅可以直接乘以路径数：不同路径的 $B_{\rho\alpha}^{(p)}$ 把不同的 $C_{ij}^{(\rho)}$ 与不同的 $f_{ij,\alpha}$ 配对，必须先对每个路径按其 $I_\rho$ 和单项式指数求和，才可以判断某些有限项是否抵消。

更精确地说：

1. **可以共享的部分：** 相同 $p,N,N_1,k$ 的单项式积分 $J_p$ 完全相同。实现中可缓存该值，避免重复计算。
2. **只有同时置换参数及所有对应多项式时才可合并：** 若两个路径的质量指标集合可由参数置换互相映射，必须同时置换 $B_{\rho\alpha}^{(p)}(x)$ 中的 $x_i$ 和 $f_{ij,\alpha}$ 的边标签；不能只把分母替换成相同的代表分母。
3. **目前不能直接合并的部分：** 固定外腿排列下，六个外动量不变量是有标签的。任意置换参数不自动保持 $q_1^2,q_2^2,q_3^2,q_i\cdot q_j$ 的系数不变。故在未同时变换动量路由之前，不存在仅凭“质量相同个数相同”就把路径振幅合并的依据。
4. **可先作的精确简化：** 对每个 $\alpha$，先计算 $B_{\rho\alpha}^{(p)}$ 的单项式系数，再按键 $(p,n_1,n_2,n_3,n_4,I_\rho)$ 聚合相同 $J_p$。只有聚合后的系数严格为零，才能宣称发生了路径间抵消。

### 64.5 对第 60 节表的独立代数复核

我用符号代数按第 60.1 节的定义重新枚举了全部 $2^4=16$ 条路径。每条路径均重新从 $Y_h,Y_s$ 的矩阵元构造 $u_r,v_r$，并枚举四个顶点的 $2^4=16$ 种 $R/L$ 赋值；对两条动量斜线的项，只保留环上手征变化边恰为指定边对 $(i,j)$ 的赋值。所得结果给出以下独立检查：

$$
\sum_{\rho=1}^{16}H_\rho=0,\qquad
\sum_{\rho=1}^{16}C_{ij}^{(\rho)}=0\quad\text{对全部六个 }i<j.
$$

同时逐路径得到的 $H_\rho$ 与 $M_\rho$ 和第 60.3 节表一致；按定义重建的六个 $C_{ij}^{(\rho)}$ 也与该表的 $P_1,P_2,T_{12}$ 记号一致。因此，**第 60 节的代数系数表通过了这次独立枚举检查**。这个检查只验证路径系数定义及代数，不验证原始图的整体符号、图的对称因子或外腿排列总和。

复核的核心逻辑可概括为以下可复现伪代码：

```python
for path in product((1, 2), repeat=4):
    # 每条边的 Yukawa 矩阵元
    u = (Yh[a,b], Ys[b,c], Yh[c,d], Ys[d,a])
    v = (Yh[b,a], Ys[c,b], Yh[d,c], Ys[a,d])
    H = u[0]*v[1]*u[2]*v[3] + v[0]*u[1]*v[2]*u[3]
    M = product(edge_masses) * (product(u) + product(v))

    for i, j in combinations(range(4), 2):
        C[i,j] = 0
        for sigma in product(("R", "L"), repeat=4):
            transitions = {
                r for r in range(4)
                if sigma[r] != sigma[(r+1) % 4]
            }
            if transitions == {i, j}:
                C[i,j] += product(c_r(sigma[r]) for r in range(4)) \
                          * product(edge_masses[r] for r not in (i, j))
```

实际计算中，代码使用精确有理数与符号表达式而不是浮点近似。对最终积分，直接把 $B_{\rho\alpha}^{(p)}$ 展开成单项式并调用 64.2 节的 $J_p$ 公式即可；这也提供了一个独立于数值三维积分的检查途径。

### 64.6 本节结论与下一步

本节完成了此前缺失的核心步骤：**每条路径的六个动量系数不再停留在三维单纯形积分符号，而已被严格化为有限个、参数明确的超几何函数求和。** 质量重数类可以共享基本积分，但路径振幅只有在分子多项式及外动量标签一起正确变换后才能合并。

仍需明确区分三件事：

- **已完成：** 第 60 节 $H,M,C_{ij}$ 的独立代数复核；把 16 条路径、六个动量不变量的参数积分统一约化为精确有限和；明确五类分母及其可共享的积分核。
- **还需完成：** 将每个 $B_{\rho\alpha}^{(p)}$ 的有限单项式求和实际聚合成更紧凑的质量比函数，并在需要时将 ${}_2F_1$ 逐项化为有理函数与对数。
- **尚未进入最终匹配：** 原始 Feynman 规则下所有不等价外腿排列及整体因子、EFT 一圈振幅、UV–EFT 相减、非冗余算符基底投影与 Wilson 系数确认。

下一节应首先从 UV 拉氏量的原始 Feynman 规则重新确定完整盒图的排列与整体归一化，然后把第 64 节的精确积分和式作为每一排列的可复用计算模块。只有在这些排列全部求和并减去同基底 EFT 振幅后，才可报告最终 Wilson 系数。


## 第 65 节：第二种不等价盒图次序 $hhss$ 与外腿排列的计数

第 64 节完成的是顶点类型按环路顺序为 $(h,s,h,s)$ 的固定排列。本节处理另一个不能遗漏的环路类型：相邻两个 $h$ 顶点、再相邻两个 $s$ 顶点，即 $(h,h,s,s)$。这一步不能只把第 60 节的结果乘以 2，因为内部 Yukawa 矩阵乘积随顶点顺序变化。

### 65.1 为什么至少要分别计算交替型与相邻型

先只看标量类型，不区分同种外腿的动量标签。四个环路顶点有两个 $h$ 和两个 $s$。忽略环路的循环起点后，类型序列可分为：

- 交替型：$hshs$（循环旋转后也包括 $shsh$）；
- 相邻型：$hhss$（循环旋转后也包括 $hssh,sshh,shhs$）。

因此，类型序列层面有两个类别，而不是一个。对带有标签的外动量 $q_i$，同种外腿的交换还会把动量不变量互相置换；在最终四点函数中必须对这些 Bose 排列求和。类型序列的两个类别不等于完整的“带动量标签图”的总数。

### 65.2 对一般顶点序列的路径系数定义

令环路上的顶点序列为 $V=(V_1,V_2,V_3,V_4)$，其中每个 $V_r\in\{h,s\}$，相应的 Yukawa 矩阵为 $Y_{V_r}$. 对内部质量路径 $\rho=(a,b,c,d)$，定义

$$
\begin{aligned}
(u_1,u_2,u_3,u_4)
&=\big((Y_{V_1})_{ab},(Y_{V_2})_{bc},
(Y_{V_3})_{cd},(Y_{V_4})_{da}\big),\\
(v_1,v_2,v_3,v_4)
&=\big((Y_{V_1})_{ba},(Y_{V_2})_{cb},
(Y_{V_3})_{dc},(Y_{V_4})_{ad}\big),
\end{aligned}
$$

边质量仍为 $\mu=(m_b,m_c,m_d,m_a)$。然后沿用

$$
H_\rho(V)=u_1v_2u_3v_4+v_1u_2v_3u_4,
$$

$$
M_\rho(V)=\left(\prod_{r=1}^4\mu_r\right)
\left(\prod_{r=1}^4u_r+\prod_{r=1}^4v_r\right),
$$

以及

$$
C_{ij}^{(\rho)}(V)=
\sum_{\substack{\sigma\in\{R,L\}^4\\
\{r:\sigma_r\ne\sigma_{r+1}\}=\{i,j\}}}
\left(\prod_{r=1}^4c_r(\sigma_r)\right)
\left(\prod_{r\notin\{i,j\}}\mu_r\right),
\quad c_r(R)=u_r,\quad c_r(L)=v_r,
$$

其中 $\sigma_5\equiv\sigma_1$。这样，第 61–64 节的积分推导不必重做：只需把每条路径的 $H,M,C_{ij}$ 换成当前顶点序列的值；参数分母、$f_{ij,\alpha},g_\alpha,d_\alpha$ 由相同的外动量路由给出。

### 65.3 相邻型 $hhss$ 的 $H_\rho$ 逐路径结果

取 $V=(h,h,s,s)$，记

$$
Z=c_L^2c_R^2+s_L^2s_R^2,\qquad
P=a^2b^2c_L^2c_R^2s_L^2s_R^2,
$$

$$
U_L=a^2b^2c_L^2s_R^2 Z,\qquad
U_R=a^2b^2c_R^2s_L^2 Z.
$$

由 $H_\rho(V)$ 的定义直接代入矩阵元，16 条路径得到：

| 路径 $\rho$ | $H_\rho(hhss)$ |
|---|---:|
| 1111 | $+2P$ |
| 1112 | $+U_L$ |
| 1121 | $-2P$ |
| 1122 | $-U_L$ |
| 1211 | $+U_R$ |
| 1212 | $+2P$ |
| 1221 | $-U_R$ |
| 1222 | $-2P$ |
| 2111 | $-2P$ |
| 2112 | $-U_L$ |
| 2121 | $+2P$ |
| 2122 | $+U_L$ |
| 2211 | $-U_R$ |
| 2212 | $-2P$ |
| 2221 | $+U_R$ |
| 2222 | $+2P$ |

由此

$$
\sum_{\rho}H_\rho(hhss)=0.
$$

这只是未加分母权重的纯代数和；和交替型一样，它不能用于推断有限的动量展开振幅为零。

### 65.4 相邻型的两斜线系数出现不同的抵消结构

对 $C_{ij}^{(\rho)}(hhss)$ 也按第 65.2 节的定义逐路径枚举后，未加分母权重的和为

$$
\sum_\rho C_{12}^{(\rho)}(hhss)=
\sum_\rho C_{14}^{(\rho)}(hhss)=
\sum_\rho C_{23}^{(\rho)}(hhss)=
\sum_\rho C_{24}^{(\rho)}(hhss)=
\sum_\rho C_{34}^{(\rho)}(hhss)=0,
$$

但对相对的边对 $(1,3)$，

$$
\boxed{
\begin{aligned}
\sum_\rho C_{13}^{(\rho)}(hhss)
={}&a^2b^2(c_L^2+s_L^2)(c_R^2+s_R^2)\\
&\times\left[
(m_1^2+m_2^2)(c_L^2c_R^2+s_L^2s_R^2)
-4m_1m_2c_Lc_Rs_Ls_R
\right].
\end{aligned}}
$$

这里没有假定 $c_L^2+s_L^2=1$ 或 $c_R^2+s_R^2=1$；若它们来自正交混合矩阵，才可在确认约定后使用相应归一化关系。该结果说明：交替型第 60.4 节的“六个 $C_{ij}$ 无权重求和全为零”不能直接推广到相邻型。特别是 $C_{13}$ 的纯代数和非零，即便最后的积分仍可能因不同分母和其他分子项而产生额外抵消，也必须实际积分才能判断。

### 65.5 相邻型仍可直接使用第 64 节的精确积分公式

对每条相邻型路径，用当前的 $H_\rho(hhss),M_\rho(hhss),C_{ij}^{(\rho)}(hhss)$ 定义

$$
\begin{aligned}
B_{\rho\alpha}^{(1)}(hhss)
&=H_\rho(hhss)\left(\frac23g_\alpha-2d_\alpha\right),\\
B_{\rho\alpha}^{(2)}(hhss)
&=\frac13\sum_{i<j}C_{ij}^{(\rho)}(hhss)f_{ij,\alpha}
-\frac23S_\rho(hhss)d_\alpha,\\
B_{\rho\alpha}^{(3)}(hhss)
&=-\frac23M_\rho(hhss)d_\alpha.
\end{aligned}
$$

每项积分仍是

$$
\int_{\rm simplex}\frac{B_{\rho\alpha}^{(p)}(hhss)}
{\Delta_{0,\rho}^{\,p}}\,d\mu_3,
$$

把多项式展开后，逐个单项式套用第 64.2 节的 $J_p(n;I_\rho)$ 即可。因此，解析参数积分算法对两种类型通用；需要更新的是顶点序列对应的路径系数，以及每个带标签外腿排列的动量替换。

### 65.6 外腿排列必须怎样求和

完整的 $h h s s$ 四点振幅应先给四条外腿各自保留动量标签，再枚举与场类型相容的环路顶点排列。实际执行时必须分开记账：

1. **内部路径求和：** 每一种固定的外腿排列内，对 $(a,b,c,d)\in\{1,2\}^4$ 的 16 条质量路径求和；第 60 节和第 65 节分别提供两种顶点序列的系数规则。
2. **环路旋转：** 同一有向费米子迹的循环起点改变不应被重复计算；但在实际 Feynman 图的 Wick 收缩计数中，必须与原始图的对称因子一致，不能只凭迹的循环性随意乘除整数。
3. **环路反向：** 只有在反向后同时转置内部指标、反转矩阵次序并核实 Dirac 共轭后，才能认定它与正向图相同。实 Yukawa 矩阵本身不足以免除这一核查。
4. **同种外腿交换：** $h$ 的两个外动量和 $s$ 的两个外动量分别交换，会把六个不变量重新映射。对局域 $h^2s^2$ 算符作投影时，应先对带标签振幅求和，再化到一个独立不变量基底。
5. **整体归一化：** 第 64 节的参数积分保留了固定排列定义中的 $6=\Gamma(4)$。它是 Feynman 参数化因子，不等同于外腿排列数，也不等同于 Wick 收缩的对称因子。三者必须在最终振幅中分别来源明确。

### 65.7 当前进度边界

本节实际完成了相邻型的 $H_\rho$ 逐路径表，并重新核查了其 $C_{ij}$ 的未加权代数和；它证明相邻型不能通过“交替型结果乘一个整数”得到。两类拓扑的路径级参数积分现在都有统一的精确表达式。

**仍未宣称完成的部分：** 还没有从完整 UV 拉氏量的 Feynman 规则推导所有带标签外腿排列的总组合因子；也尚未把两种类型所有排列的 96 个动量系数全部实际聚合成最终质量比函数。之后还需要在相同外态、相同动量路由与相同重整化方案下计算 EFT 一圈振幅并作差。只有完成这些步骤，才能把盒图的 UV 局域展开识别为 UV–EFT 差额，而不是直接当作 Wilson 系数。

## 第 66 节：用可运行的 SymPy 枚举独立复核两种顶点次序，并固定下一步积分输入

本节不是重复第 64–65 节的结论，而是把路径系数的定义直接写成一段完整的 Python/SymPy 程序，实际运行并核验交替次序 $(h,s,h,s)$ 与相邻次序 $(h,h,s,s)$。这样做的目的，是在继续执行参数积分前，先排除“表格抄写正确但路径约定不一致”的风险。

### 66.1 程序采用的输入与索引约定

采用第 37 节的实 Yukawa 矩阵

$$
Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix}.
$$

路径 $(a_1,a_2,a_3,a_4)\in\{1,2\}^4$ 表示环上四条传播子交替连接相邻顶点。对顶点矩阵序列 $(V_1,V_2,V_3,V_4)$，正向矩阵元定义为

$$
u_r=(V_r)_{a_r a_{r+1}},\qquad a_5\equiv a_1,
$$

反向矩阵元定义为

$$v_r=(V_r)_{a_{r+1}a_r}.
$$

传播子质量按第 60 节约定为

$$
(\mu_1,\mu_2,\mu_3,\mu_4)=(m_{a_2},m_{a_3},m_{a_4},m_{a_1}).
$$

本节的 $C_{ij}$ 依照已定义的“手征变化边恰为 $\{i,j\}$”求和。此处 $i,j$ 是 0 起始的 Python 索引，打印时会转成论文中的 1 起始编号。

### 66.2 可直接运行的完整程序

保存以下代码为 `audit_path_coefficients.py`：

```python
from itertools import product, combinations
import sympy as sp

## Symbolic parameters: all algebra is exact; no floating-point values are used.
a, b, cL, cR, sL, sR, m1, m2 = sp.symbols(
    'a b c_L c_R s_L s_R m_1 m_2'
)
Yh = a * sp.Matrix([[cL*sR, cL*cR],
                     [sL*sR, sL*cR]])
Ys = b * sp.Matrix([[sL*cR, -sL*sR],
                     [-cL*cR, cL*sR]])
mass = {1: m1, 2: m2}


def audit(vertex_names):
    """Sum H, M and each C_ij over the 16 internal mass paths."""
    matrices = {'h': Yh, 's': Ys}
    V = [matrices[name] for name in vertex_names]
    pairs = list(combinations(range(4), 2))
    H_sum = sp.Integer(0)
    M_sum = sp.Integer(0)
    C_sum = {pair: sp.Integer(0) for pair in pairs}
    path_rows = []

    for path in product((1, 2), repeat=4):
        # Four vertices connect path[r] to path[(r+1) mod 4].
        u = [V[r][path[r]-1, path[(r+1) % 4]-1]
             for r in range(4)]
        v = [V[r][path[(r+1) % 4]-1, path[r]-1]
             for r in range(4)]
        mu = [mass[path[1]], mass[path[2]],
              mass[path[3]], mass[path[0]]]

        H = sp.expand(u[0]*v[1]*u[2]*v[3]
                      + v[0]*u[1]*v[2]*u[3])
        M = sp.expand(sp.prod(mu) * (sp.prod(u) + sp.prod(v)))
        H_sum += H
        M_sum += M

        C_row = {}
        for i, j in pairs:
            C = sp.Integer(0)
            for sigma in product((0, 1), repeat=4):
                # 0 denotes the u/R choice, 1 the v/L choice.
                transitions = {
                    r for r in range(4)
                    if sigma[r] != sigma[(r+1) % 4]
                }
                if transitions == {i, j}:
                    vertex_product = sp.prod(
                        u[r] if sigma[r] == 0 else v[r]
                        for r in range(4)
                    )
                    remaining_masses = sp.prod(
                        mu[r] for r in range(4) if r not in (i, j)
                    )
                    C += vertex_product * remaining_masses
            C = sp.expand(C)
            C_row[(i, j)] = C
            C_sum[(i, j)] += C

        path_rows.append((path, H, M, C_row))

    print('vertex order =', ''.join(vertex_names))
    print('sum H =', sp.factor(H_sum))
    print('sum M =', sp.factor(M_sum))
    for (i, j), value in C_sum.items():
        print(f'sum C_{{{i+1}{j+1}}} =', sp.factor(value))
    return path_rows, H_sum, M_sum, C_sum


if __name__ == '__main__':
    # Alternating and adjacent vertex orderings, respectively.
    audit(('h', 's', 'h', 's'))
    print()
    audit(('h', 'h', 's', 's'))
```

安装和运行：

```bash
python -m pip install sympy
python audit_path_coefficients.py
```

程序遍历两种排列各自的 16 条质量路径；每条路径再遍历四个顶点的 16 种手征选择。所有符号化简均由 SymPy 完成，结果是精确多项式恒等式。这个脚本不调用网络、不依赖外部数据，也不需要 Mathematica、FeynCalc 或 Package-X。

### 66.3 实际运行结果

对交替次序 $(h,s,h,s)$，程序得到

$$
\sum_\rho H_\rho=0,
$$

$$
\sum_\rho M_\rho=
2a^2b^2(c_Lc_Rm_1-m_2s_Ls_R)^2
(c_Lc_Rm_2-m_1s_Ls_R)^2,
$$

并且六个无权重系数和均为零：

$$
\sum_\rho C_{12}=\sum_\rho C_{13}=\sum_\rho C_{14}
=\sum_\rho C_{23}=\sum_\rho C_{24}=\sum_\rho C_{34}=0.
$$

对相邻次序 $(h,h,s,s)$，程序得到

$$
\sum_\rho H_\rho=0,
$$

而质量项之和为

$$
\boxed{\begin{aligned}
\sum_\rho M_\rho={}&-2a^2b^2
(c_Lc_Rm_1-m_2s_Ls_R)
(c_Lc_Rm_2-m_1s_Ls_R)\\
&\times(c_Lm_1s_R+c_Rm_2s_L)
(c_Lm_2s_R+c_Rm_1s_L).
\end{aligned}}
$$

相邻次序的 $C_{ij}$ 无权重求和是

$$
\sum_\rho C_{13}=
 a^2b^2(c_L^2+s_L^2)(c_R^2+s_R^2)
\left[(m_1^2+m_2^2)(c_L^2c_R^2+s_L^2s_R^2)
-4m_1m_2c_Lc_Rs_Ls_R\right],
$$

而另外五项满足

$$
\sum_\rho C_{12}=\sum_\rho C_{14}=\sum_\rho C_{23}
=\sum_\rho C_{24}=\sum_\rho C_{34}=0.
$$

这些结果与第 65.4 节给出的相邻次序 $C_{13}$ 公式一致，也再次表明两种顶点次序不可仅用一个整体倍数相互替代。特别要注意，以上都是**未加分母权重的系数和**；真实振幅中每条路径具有自己的 $\Delta_{0,\rho}$，因此这些恒等式本身并不等于积分后的振幅抵消。

### 66.4 对路径积分的实际含义

现在可以明确区分三类合并：

1. **可以直接合并的纯代数项：** 在固定顶点次序中，若某个系数的无权重总和恒等于零，则该纯代数和确实为零；但只有在分母也相同的特殊极限下，才可把它直接带入积分并令该部分消失。
2. **可以复用的积分核：** 对相同质量重数 $k$、相同单项式总次数 $N$、相同重质量指数和 $N_1$ 及相同分母幂 $p$ 的项，可缓存第 64.2 节的 $J_p$。这只是计算复用，不代表路径振幅相等。
3. **不能在积分前合并的路径：** 当参数单项式指数、质量指标集合或 $C_{ij}f_{ij,\alpha}$ 的配对不同，必须保留路径标签，除非显式完成参数置换并同步变换全部边标签与外动量不变量。

另一个值得保留的检查是 $\sum M_\rho$：它通常非零，所以即使 $\sum H_\rho=0$，完整零阶分子中的质量项仍不自动抵消。二阶动量系数还包含分母位移乘以零阶分子，不能从 $H$ 和 $C_{ij}$ 的无权重求和直接推断其值。

### 66.5 当前进度与下一步的具体执行顺序

本节已实际运行并记录两种顶点序列的完整符号枚举结果。接下来按以下顺序继续，避免将尚未核实的组合因子带入 Wilson 系数：

1. 把第 61.1–61.3 节的 $f_{ij,\alpha},g_\alpha,d_\alpha$ 作为精确多项式输入 SymPy，并对每条路径构造三个 $B_{\rho\alpha}^{(p)}$。
2. 对 $B_{\rho\alpha}^{(p)}$ 用 `sp.Poly(..., x1, x2, x3, x4).terms()` 生成有限单项式表；每一项按 $(p,n_1,n_2,n_3,n_4,I_\rho)$ 缓存 $J_p$，并使用第 64.2 节的超几何函数公式。输出应包括六个 $\alpha$ 的逐路径和、总和，以及每个积分项的质量维数检查。
3. 先在等质量极限 $m_1=m_2=M$ 检查程序：此时 $\Delta_{0,\rho}=M^2$ 与路径无关，参数积分退化为普通单纯形矩，能检验单项式系数、单纯形因子 $6$ 和整体质量幂次。
4. 再保留一般质量比 $r=m_1^2/m_2^2$，对各 $J_p$ 化简并检查 $r\to1$ 极限连续；随后才对所有外腿排列做带标签的置换求和。
5. 最后从原始 Feynman 规则确定环路方向、外腿排列与 Wick 收缩的组合因子，再在同一动量路由和重整化方案下计算 EFT 振幅并相减。

**尚未完成的事项在此明确标出：** 本节尚未执行第 66.5 节第 1–5 步中的参数积分聚合、外腿排列总和或 EFT 相减，因此没有给出最终 Wilson 系数。SymPy 在本节中只用于路径级精确符号枚举；不能把这个程序的成功误述为已完成圈图匹配。


## 第 67 节：等质量极限下实际完成六个动量系数的单纯形积分

本节不再停留在“下一步应积分”的计划层面，而是把第 61–66 节的路径系数与参数多项式代入，实际完成等质量极限的精确积分。它是对积分程序、单纯形归一化和质量幂次的基准测试；**不是一般质量比的最终匹配，也不是最终 Wilson 系数**。

### 67.1 计算条件与精确单项式矩

令所有内部费米子质量相等：

$$m_1=m_2=M>0.$$

于是每条路径的参数分母都退化为

$$\Delta_{0,\rho}=M^2,$$

路径标签不再影响分母。对于四个非负参数组成的单纯形，精确矩为

$$
\int_{x_i\geq0}d^4x\,\delta\!\left(1-\sum_{i=1}^4x_i\right)
\prod_{i=1}^4x_i^{n_i}
=\frac{\prod_i n_i!}{(n_1+n_2+n_3+n_4+3)!}.
$$

例如常数函数的积分为 $1/3!=1/6$。因此，对第 64 节固定排列表达式外面的 $6=\Gamma(4)$，程序只在最后乘一次 6；常数项的归一化结果恰为 1。没有把这个因子误当成额外的外腿排列数。

本节对六个不变量逐一计算

$$
\mathcal C_\alpha^{(V)}=\frac{6}{16\pi^2}\sum_{\rho=1}^{16}\sum_{p=1}^3
\frac{1}{M^{2p}}\int_{\rm simplex}d^4x\,\delta\!\left(1-\sum_i x_i\right)B_{\rho\alpha}^{(p)}(x),
$$

其中 $V=hshs$ 或 $hhss$。在 $B^{(p)}$ 中使用第 64 节的定义，并在有限的二阶动量系数中取 $d=4$，故 $2/d=1/2$。这是对已组合的有限参数积分核取四维极限；如果以后发现某个拆分项单独含有未抵消的 $1/\epsilon$ 极点，就必须回到 $d=4-2\epsilon$ 重新组合，不能逐项提前取极限。

### 67.2 实际执行的算法

程序使用精确有理数与 SymPy 多项式，不使用浮点数。对每个路径，它直接按第 65.2 节的定义生成 $H_\rho,M_\rho,C_{ij}^{(\rho)}$；然后构造 $B^{(1)},B^{(2)},B^{(3)}$。单纯形积分不调用数值积分器，而是把多项式展开成单项式，并对每项应用上面的阶乘公式。因此输出是符号精确结果。

完整可复现程序如下。保存为 `integrate_equal_mass.py`：

```python
from itertools import product, combinations
import sympy as sp
x1,x2,x3,x4=sp.symbols('x1 x2 x3 x4')
a,b,cL,cR,sL,sR,M=sp.symbols('a b c_L c_R s_L s_R M')
xs=[x1,x2,x3,x4]
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
mass={1:M,2:M}
A=x2+x3
f={
(0,1):[x4**2,A*(A-1),x3**2,-x4*(2*A-1),-2*x3*x4,x3*(2*A-1)],
(0,2):[x4**2,A*(A-1),x3*(x3-1),-x4*(2*A-1),-x4*(2*x3-1),2*x2*x3-x2+2*x3**2-2*x3],
(0,3):[x4*(x4-1),A**2,x3**2,-A*(2*x4-1),-x3*(2*x4-1),2*x3*A],
(1,2):[x4**2,(A-1)**2,x3*(x3-1),-2*x4*(A-1),-x4*(2*x3-1),(2*x3-1)*(A-1)],
(1,3):[x4*(x4-1),A*(A-1),x3**2,-2*x4*A+A+x4-1,-x3*(2*x4-1),x3*(2*A-1)],
(2,3):[x4*(x4-1),A*(A-1),x3*(x3-1),-2*x4*A+A+x4-1,-2*x3*x4+x3+x4-1,2*x2*x3-x2+2*x3**2-2*x3]
}
d=[x4*(1-x4),A*(1-A),x3*(1-x3),2*x4*A,2*x3*x4,2*x3*(1-A)]
g=[sp.expand(f[(0,1)][k]+f[(2,3)][k]-f[(0,2)][k]-f[(1,3)][k]+f[(0,3)][k]+f[(1,2)][k]+sp.Rational(1,2)*(f[(0,2)][k]+f[(1,3)][k])) for k in range(6)] # 2/d = 1/2 at d=4

def path_data(order):
 V=[{'h':Yh,'s':Ys}[z] for z in order]
 for path in product((1,2),repeat=4):
  u=[V[r][path[r]-1,path[(r+1)%4]-1] for r in range(4)]
  v=[V[r][path[(r+1)%4]-1,path[r]-1] for r in range(4)]
  mu=[M]*4
  H=sp.expand(u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3])
  MM=sp.expand(sp.prod(mu)*(sp.prod(u)+sp.prod(v)))
  C={}
  for i,j in combinations(range(4),2):
   val=0
   for sig in product((0,1),repeat=4):
    trans={r for r in range(4) if sig[r]!=sig[(r+1)%4]}
    if trans=={i,j}:
     val += sp.prod(u[r] if sig[r]==0 else v[r] for r in range(4))*sp.prod(mu[r] for r in range(4) if r not in (i,j))
   C[(i,j)]=sp.expand(val)
  yield H,MM,C

def simplex_integral(poly):
 # exact integral over x_i>=0, sum x_i=1: sum coeff prod(n_i!)/(N+3)!
 P=sp.Poly(sp.expand(poly),*xs)
 ans=0
 for powers,coef in P.terms():
  N=sum(powers)
  ans += coef*sp.prod(sp.factorial(n) for n in powers)/sp.factorial(N+3)
 return sp.factor(ans)

for order in [('h','s','h','s'),('h','h','s','s')]:
 print('ORDER', ''.join(order), flush=True)
 sums=[]
 for alpha in range(6):
  total=0
  for H,MM,C in path_data(order):
   S=sum(C.values())
   B1=sp.expand(H*(sp.Rational(2,3)*g[alpha]-2*d[alpha]))
   B2=sp.expand(sp.Rational(1,3)*sum(C[pair]*f[pair][alpha] for pair in C)-sp.Rational(2,3)*S*d[alpha])
   B3=sp.expand(-sp.Rational(2,3)*MM*d[alpha])
   # 6 overall arrangement factor, Delta=M^2, exact simplex moments
   total += 6*(simplex_integral(B1)/M**2 + simplex_integral(B2)/M**4 + simplex_integral(B3)/M**6)
  total=sp.factor(total/(16*sp.pi**2))
  sums.append(total)
  print(alpha+1, total, flush=True)

```

运行环境为 Python 3 与 SymPy。复现命令：

```bash
python -m pip install sympy
python integrate_equal_mass.py
```

程序无需联网、Mathematica、FeynCalc 或 Package-X。其实际输出如下。

### 67.3 实际积分结果：交替型 $hshs$

按不变量顺序

$$
(\mathcal Q_1,\ldots,\mathcal Q_6)
=(q_1^2,q_2^2,q_3^2,q_1\!\cdot q_2,q_1\!\cdot q_3,q_2\!\cdot q_3),
$$

程序得到

$$
\begin{aligned}
\mathcal C_1^{(hshs)}&=-\frac{a^2b^2(c_Lc_R-s_Ls_R)^4}{80\pi^2M^2},\\
\mathcal C_2^{(hshs)}&=-\frac{a^2b^2(c_Lc_R-s_Ls_R)^4}{60\pi^2M^2},\\
\mathcal C_3^{(hshs)}&=-\frac{a^2b^2(c_Lc_R-s_Ls_R)^4}{80\pi^2M^2},\\
\mathcal C_4^{(hshs)}&=-\frac{a^2b^2(c_Lc_R-s_Ls_R)^4}{60\pi^2M^2},\\
\mathcal C_5^{(hshs)}&=-\frac{a^2b^2(c_Lc_R-s_Ls_R)^4}{120\pi^2M^2},\\
\mathcal C_6^{(hshs)}&=-\frac{a^2b^2(c_Lc_R-s_Ls_R)^4}{60\pi^2M^2}.
\end{aligned}
$$

这是对当前固定路由、固定排列积分核的结果。特别注意，尽管第 66 节发现 $\sum_\rho H_\rho=0$ 且所有 $C_{ij}$ 的无权重路径和为零，积分后系数并不因此全部为零：$B^{(2)}$ 中的 $C_{ij}^{(\rho)}f_{ij,\alpha}(x)$ 是路径级相关的多项式，不能先把 $C_{ij}$ 的路径和提出来再积分；$M_\rho$ 项也必须保留。这是一个具体反例，说明无权重路径求和不能替代带参数权重的积分。

### 67.4 实际积分结果：相邻型 $hhss$

使用同一参数多项式和当前固定动量路由，程序得到

$$
\begin{aligned}
\mathcal C_1^{(hhss)}={}&-\frac{a^2b^2(c_Lc_R-s_Ls_R)^2}{240\pi^2M^2}\\
&\times\left(2c_L^2c_R^2-c_L^2s_R^2-6c_Lc_Rs_Ls_R-c_R^2s_L^2+2s_L^2s_R^2\right),\\[2mm]
\mathcal C_2^{(hhss)}={}&-\frac{a^2b^2(c_Lc_R-s_Ls_R)^2}{120\pi^2M^2}\\
&\times\left(3c_L^2c_R^2+c_L^2s_R^2-4c_Lc_Rs_Ls_R+c_R^2s_L^2+3s_L^2s_R^2\right),\\[2mm]
\mathcal C_3^{(hhss)}={}&-\frac{a^2b^2(c_Lc_R-s_Ls_R)^2}{160\pi^2M^2}\\
&\times\left(3c_L^2c_R^2+c_L^2s_R^2-4c_Lc_Rs_Ls_R+c_R^2s_L^2+3s_L^2s_R^2\right),\\[2mm]
\mathcal C_4^{(hhss)}={}&-\frac{a^2b^2(c_Lc_R-s_Ls_R)^2}{480\pi^2M^2}\\
&\times\left(7c_L^2c_R^2-c_L^2s_R^2-16c_Lc_Rs_Ls_R-c_R^2s_L^2+7s_L^2s_R^2\right),\\[2mm]
\mathcal C_5^{(hhss)}={}&-\frac{a^2b^2(c_Lc_R-s_Ls_R)^2}{480\pi^2M^2}\\
&\times\left(c_L^2c_R^2-3c_L^2s_R^2-8c_Lc_Rs_Ls_R-3c_R^2s_L^2+s_L^2s_R^2\right),\\[2mm]
\mathcal C_6^{(hhss)}={}&-\frac{a^2b^2(c_Lc_R-s_Ls_R)^2}{480\pi^2M^2}\\
&\times\left(17c_L^2c_R^2+9c_L^2s_R^2-16c_Lc_Rs_Ls_R+9c_R^2s_L^2+17s_L^2s_R^2\right).
\end{aligned}
$$

这里的 $hhss$ 结果只代表将第 65 节路径系数代入当前同一组 $f,g,d$ 参数核后得到的**固定路由积分结果**。在把它解释为完整四点函数之前，仍需显式重做带标签外腿的动量路由，并对同种外腿交换与环路收缩进行一致求和。不能仅凭这六个数式断言它们就是某个唯一局域算符的系数。

### 67.5 本次结果通过了哪些检查，尚未通过哪些检查

**已经实际完成：**

1. 对两类顶点次序的 16 条内部质量路径分别生成 $H,M,C_{ij}$，不依赖手抄系数表。
2. 对六个动量不变量的 $B^{(1)},B^{(2)},B^{(3)}$ 逐路径构造多项式。
3. 在 $m_1=m_2=M$ 时用精确单项式矩积分所有参数多项式，并包含一次固定排列因子 6。
4. 得到两种顶点次序共 12 个符号系数；它们均具有正确的 $M^{-2}$ 质量维数和一圈 $1/\pi^2$ 量级。

**仍未完成：**

1. 一般 $m_1\ne m_2$ 时的超几何函数有限和实际求值与化简。
2. 从 UV 原始 Feynman 规则独立核实整体符号、闭环符号、外腿排列和 Wick 收缩因子。
3. 对带标签外腿的所有排列统一动量路由，投影到非冗余算符基底。
4. 计算 EFT 同一外态下的一圈图、反项与算符混合，再执行 UV–EFT 相减。
5. 据此确认最终 Wilson 系数；本节没有完成这一步。

所以本节的成果是一个**实际算完的等质量积分基准**，不是一般质量比闭式结果，也不是已完成的 UV–EFT 匹配。后续最有价值的推进是先把一般质量比积分程序对单项式指数的超几何核实现，并用本节 $m_1=m_2$ 的结果作为逐项回归测试；再独立完成外腿排列与 EFT 相减。


## 第 68 节：一般质量比的超几何有限和——数值实现与连续性检查

本节推进第 67 节之后的下一步：不再令 $m_1=m_2$，而是把第 64.2 节的单项式积分公式实际用于 $m_1\ne m_2$。本次完成的是**一般质量比下的数值求值程序与若干测试点**，还没有把所有系数化简成统一的有理函数加对数的符号闭式，也没有完成 UV–EFT 相减。

### 68.1 计算公式与实现方式

对每个路径 $\rho$、每个动量不变量 $\alpha$，先将三个参数多项式展开为

$$
B_{\rho\alpha}^{(p)}(x)=\sum_n b_{\rho\alpha n}^{(p)}x_1^{n_1}x_2^{n_2}x_3^{n_3}x_4^{n_4}.
$$

令 $I_\rho$ 是质量为 $m_1$ 的传播子参数指标集合，$k=|I_\rho|$，$N=\sum_i n_i$，$N_1=\sum_{i\in I_\rho}n_i$。每个单项式的积分用

$$
J_p(n;I_\rho)=\frac{\prod_i n_i!}{(N+3)!}\frac{1}{(m_2^2)^p}
{}_2F_1\!\left(p,N_1+k;N+4;1-\frac{m_1^2}{m_2^2}\right)
$$

求值；$k=0$ 或 $4$ 时分别直接使用 $m_2^{-2p}$ 或 $m_1^{-2p}$。因此每个路径的三维参数积分成为有限多个超几何函数值的加权和。数值程序对相同的 $(p,n,I_\rho,m_1,m_2)$ 缓存 $J_p$，避免反复计算相同的超几何函数。

程序中的质量路径约定遵循文档第 64 节：路径标签记为 $(a,b,c,d)$，传播子质量顺序为 $(m_b,m_c,m_d,m_a)$。这个索引旋转是重要的；若把质量集合误设为 $(m_a,m_b,m_c,m_d)$，一般质量比结果会改变，虽然等质量测试仍可能通过。

### 68.2 实际测试设置

为了给一般质量比积分提供可复现的数值回归测试，取

$$
a=1,\quad b=0.7,\quad c_L=0.6,\quad s_L=0.8,\quad c_R=5/13,\quad s_R=12/13,
$$

并把 $m_2=1$ 作为质量单位，依次计算 $m_1/m_2=1,1.0001,2,0.5$。数值程序使用 Python 3、SymPy 与 mpmath；它按路径枚举 Yukawa 因子和 $H_\rho,M_\rho,C_{ij}^{(\rho)}$，把 $B_{\rho\alpha}^{(p)}$ 展开成单项式，再调用上面的超几何积分公式。脚本文件：`general_mass_ratio_integral.py`。

复现方式：

```bash
python -m pip install sympy mpmath
python general_mass_ratio_integral.py
```

脚本中的示例参数是数值测试点，不是模型拟合或物理约束。输出系数以 $m_2=1$ 为单位；若把两个质量同时乘以 $\lambda$，这些二阶动量系数应整体按 $\lambda^{-2}$ 缩放。

### 68.3 数值结果

六个分量按

$$
(q_1^2,q_2^2,q_3^2,q_1\!\cdot q_2,q_1\!\cdot q_3,q_2\!\cdot q_3)
$$
排序。下表列出超几何有限和的数值求值结果；仅保留约 6 位有效数字，避免把浮点输出误当成精确解析系数。

| $m_1/m_2$ | 排列 | $\mathcal C_1$ | $\mathcal C_2$ | $\mathcal C_3$ | $\mathcal C_4$ | $\mathcal C_5$ | $\mathcal C_6$ |
|---:|:---:|---:|---:|---:|---:|---:|---:|
| 1.0000 | $hshs$ | $-4.12296\times10^{-5}$ | $-5.49727\times10^{-5}$ | $-4.12296\times10^{-5}$ | $-5.49727\times10^{-5}$ | $-2.74864\times10^{-5}$ | $-5.49727\times10^{-5}$ |
| 1.0000 | $hhss$ | $1.20900\times10^{-5}$ | $-1.61612\times10^{-4}$ | $-1.21209\times10^{-4}$ | $-2.83130\times10^{-5}$ | $5.24929\times10^{-5}$ | $-2.94911\times10^{-4}$ |
| 1.0001 | $hshs$ | $-4.12254\times10^{-5}$ | $-5.49672\times10^{-5}$ | $-4.12254\times10^{-5}$ | $-5.49672\times10^{-5}$ | $-2.74836\times10^{-5}$ | $-5.49672\times10^{-5}$ |
| 1.0001 | $hhss$ | $1.20888\times10^{-5}$ | $-1.61596\times10^{-4}$ | $-1.21194\times10^{-4}$ | $-2.83079\times10^{-5}$ | $5.24899\times10^{-5}$ | $-2.94879\times10^{-4}$ |
| 2.0000 | $hshs$ | $3.19838\times10^{-5}$ | $4.19545\times10^{-5}$ | $3.19838\times10^{-5}$ | $4.19545\times10^{-5}$ | $2.20131\times10^{-5}$ | $4.19545\times10^{-5}$ |
| 2.0000 | $hhss$ | $-9.03227\times10^{-5}$ | $-1.51462\times10^{-4}$ | $-9.07910\times10^{-5}$ | $-1.44061\times10^{-4}$ | $-2.96522\times10^{-5}$ | $-1.51930\times10^{-4}$ |
| 0.5000 | $hshs$ | $1.27935\times10^{-4}$ | $1.67818\times10^{-4}$ | $1.27935\times10^{-4}$ | $1.67818\times10^{-4}$ | $8.80526\times10^{-5}$ | $1.67818\times10^{-4}$ |
| 0.5000 | $hhss$ | $-3.61291\times10^{-4}$ | $-6.05846\times10^{-4}$ | $-3.90891\times10^{-4}$ | $-6.03973\times10^{-4}$ | $-1.46336\times10^{-4}$ | $-6.35447\times10^{-4}$ |

### 68.4 结果核查与解释

**(i) 等质量回归检查。** 当 $m_1/m_2=1$ 时，超几何函数自变量为零，$\,{}_2F_1(a,b;c;0)=1$，因此每个单项式积分退化为第 67 节的阶乘矩。数值程序的等质量输出与第 67 节的符号结果在示例参数下相符。

**(ii) 连续性检查。** 从 $m_1/m_2=1$ 改成 $1.0001$ 后，12 个系数均连续变化，变化量与小质量比扰动的量级相称。这个检查能发现超几何自变量、质量幂次或路径分母处理中的明显错误，但不能独自证明整个 Feynman 振幅的整体符号和组合因子正确。

**(iii) 非等质量效应。** 在 $m_1/m_2=2$ 与 $0.5$ 时，部分系数的符号与等质量点不同。这说明不能把等质量极限下提取出的简单角度组合直接推广到一般质量比；必须保留路径分母和质量集合标签。

**(iv) 维数检查。** 此处把 $m_2=1$ 作为单位，所以输出是相应单位下的数值。恢复质量单位后，所有二阶动量系数的总质量维数应为 $-2$。程序的每个 $J_p$ 含质量维数 $-2p$，而 $B^{(p)}$ 的质量维数补偿与第 62–64 节定义一致；在进入 Wilson 系数解释前仍应再用显式单位检查整个振幅归一化。

### 68.5 当前结论与仍需完成的工作

本次真正完成的是：对两种顶点序列、每种 16 条内部路径、六个动量不变量，把一般质量比积分核按超几何有限和实际数值求值，并做了等质量回归和近等质量连续性测试。

仍未完成的关键事项：

1. 把这 12 个一般质量比系数进一步化简为统一的有理函数与 $\ln(m_1^2/m_2^2)$ 的解析表达，并独立检查 $m_1\leftrightarrow m_2$ 的变换性质。
2. 从原始 Feynman 规则重新核定传播子分子、环路方向、闭费米子环符号、顶点排列与 Wick 收缩因子。
3. 对外腿动量路由与所有必要排列做带标签求和，投影到非冗余 EFT 算符基底。
4. 计算 EFT 一圈振幅和反项，在相同正则化及重整化方案下进行 UV–EFT 相减。

所以这里的数值结果是一般质量比积分程序的阶段性验证，不是最终 Wilson 系数。尤其不能仅凭这些数值点宣称算符混合系数已经确定。

## 第 69 节：一般质量比解析化简的首个闭式结果与等质量极限核验

本节继续第 68 节中列出的第一项后续工作：把超几何有限和实际化简成质量比的有理函数与对数。为避免一次性展开全部 12 个系数造成难以审计的巨大表达式，本节先选取一个明确、可复现的基准：顶点序列 $hshs$ 的第一个动量系数，且采用第 68 节同一组有理混合参数。**这是一项真实完成的解析化简，但只覆盖一个固定参数点的一个系数，不代表已得到一般混合角下的全解析 Wilson 系数。**

### 69.1 计算设置

取

$$
a=1,\quad b=\frac{7}{10},\quad c_L=\frac35,\quad s_L=\frac45,\quad c_R=\frac5{13},\quad s_R=\frac{12}{13},\quad m_2=1,\quad r=\frac{m_1}{m_2}>0.
$$

对 $hshs$、$\mathcal Q_1=q_1^2$，将每条路径的 $B_{\rho 1}^{(p)}$ 展开成单项式，使用

$$
{}_2F_1(p,N_1+k;N+4;1-r^2)
$$
的整数参数解析化简，再把 16 条路径和 $p=1,2,3$ 的贡献相加。SymPy 将超几何函数化为有理函数与 $\log r$ 的组合；最终表达式如下：

$$
\begin{aligned}
\mathcal C^{(hshs)}_1(r)
={}&-\frac{3969}{28561000000\pi^2 r^2(r-1)^5(r+1)^5}\,P(r),\\[2pt]
P(r)={}&14080r^{12}-89920r^{11}-76933r^{10}+269760r^9\log r+674400r^9\\
&+59844r^8\log r+145538r^8-6204480r^7\log r+4361120r^7\\
&-255336r^6\log r-6204480r^5\log r-4361120r^5\\
&+59844r^4\log r-145538r^4+269760r^3\log r-674400r^3\\
&+76933r^2+89920r-14080.
\end{aligned}
$$

这里 $\mathcal C_1$ 是本文固定动量路由与归一化下的积分系数，尚未完成外腿排列总和或 UV–EFT 相减，因此不能直接认作最终 Wilson 系数。由于分子在 $r=1$ 有高阶零点，表达式表面上的 $(r-1)^{-5}$ 是可去奇点，不是物理发散。

### 69.2 极限与数值交叉核验

对上式直接求解析极限，得到

$$
\lim_{r\to1}\mathcal C^{(hshs)}_1(r)
=-\frac{58110129}{142805000000\pi^2}
\simeq -4.12295581519480\times10^{-5}.
$$

这个值与第 68 节的等质量数值结果一致。对非等质量点代入闭式表达式：

| $r=m_1/m_2$ | 解析闭式求值 | 第 68 节数值积分 | 核验 |
|---:|---:|---:|:---|
| $1$（取极限） | $-4.12295581519480\times10^{-5}$ | $-4.1229558151948\times10^{-5}$ | 一致 |
| $2$ | $3.19838438215421\times10^{-5}$ | $3.1983843821542\times10^{-5}$ | 一致 |
| $1/2$ | $1.27935375286168\times10^{-4}$ | $1.2793537528617\times10^{-4}$ | 一致 |
| $1.0001$ | $-4.12254326705778\times10^{-5}$ | $-4.1225432670578\times10^{-5}$ | 一致 |

因此，至少对这个系数，独立的超几何有限和求值与有理函数加对数的解析式相互吻合；同时也确认了 $r=1$ 的表观奇点可通过取极限消去。

### 69.3 复现程序与软件

新增文件 `closed_form_mass_ratio_C1.py`。环境为 Python 3、SymPy、mpmath；安装与运行：

```bash
python -m pip install sympy mpmath
python closed_form_mass_ratio_C1.py
```

程序会从路径枚举开始重新构造 $hshs$ 的 $\mathcal C_1$，对整数参数超几何函数调用 `sympy.hyperexpand`，汇总并因式分解表达式，最后输出 $r=1.0001,2,1/2$ 的数值核验。$r=1$ 点应对闭式取极限，不宜直接代入含 $(r-1)^{-5}$ 的未约分表达式，以免产生数值消去误差。

### 69.4 结论与下一步

本节完成了一项可核查的解析进展：一个一般质量比系数已从超几何有限和化为显式的有理函数与对数，并通过等质量极限和三个非等质量点交叉核验。下一步应使用相同方式处理其余五个 $hshs$ 系数，再处理 $hhss$；对每个系数都要保留可去奇点的极限检查。之后仍须回到原始 Feynman 规则，独立确认整体符号、外腿排列与组合因子，最后计算 EFT 图与反项并执行 UV–EFT 相减。

## 第 70 节：继续计算的独立复核——解析化简边界、原始费曼因子与相邻型路由纠错

本节记录对第 69 节之后四项任务的一次实际复核。重点是区分程序已经计算了什么、原始图规则能够独立确认什么，以及哪些旧数值在完成路由复核前不能作为物理振幅使用。

### 70.1 重新运行已有程序：已复现的内容

在当前运行环境重新执行：

```bash
python /mnt/data/closed_form_mass_ratio_C1.py
python /mnt/data/general_mass_ratio_integral.py
```

第一个程序在约 10 秒内重新生成 $hshs$ 的第一个系数，输出与第 69 节所列闭式完全一致；在 $r=2,1/2,1.0001$ 处分别得到

$$
3.19838438215421\times10^{-5},\quad
1.27935375286168\times10^{-4},\quad
-4.12254326705778\times10^{-5}.
$$

第二个程序重新输出了第 68 节所列的 $r=1$ 和 $r=1.0001$ 数值表。因此，这两项是**已复现的程序结果**。

我也尝试把 `hyperexpand` 的符号化简扩展到其余动量系数。当前实现对第一个系数有效，但在处理下一个系数时，单次符号化简在 300 秒时间限内未能完成。故本次没有得到其余 11 个系数的可信闭式，不能把它们写成“已解析化简”。下一版程序应先对相同超几何参数做分组、缓存并对积分核作对称化简，再逐个输出表达式与极限，而不是让大表达式一次性展开。

### 70.2 从原始 Feynman 规则核对整体因子

UV 相互作用约定为

$$
\mathcal L_{\rm int}=-h\bar\chi\Gamma_h\chi-s\bar\chi\Gamma_s\chi,
\qquad \Gamma_\phi=Y_\phi P_R+Y_\phi^\dagger P_L.
$$

对一个给定、带外腿标签的有向四顶点费米子盒图，原始规则给出：

- 每个 Yukawa 顶点为 $-i\Gamma_\phi$，四个顶点的因子乘积是 $(-i)^4=+1$；
- 每个内部 Dirac 传播子为 $i(\slashed k+m)/(k^2-m^2+i0)$，四条传播子的显式 $i$ 因子乘积为 $i^4=+1$；
- 每个闭合费米子环另有一个整体负号 $(-1)$；
- 外部标量腿没有额外的内部传播子因子。积分测度、Minkowski 到 Euclidean 的 Wick 转动、分子中 $k^2$ 的转号仍须与所采用的欧氏积分定义一起处理。

所以，在尚未吸收 Wick 转动符号的原始 Minkowski 记账中，顶点与传播子显式的 $i$ 因子并不会抵消闭环负号；它们留下的相对整体因子是 $-1$。当前 `general_mass_ratio_integral.py` 计算的是按第 61 节所定义的**欧氏参数积分核**，代码最后乘 $+6/(16\pi^2)$，没有在该层单独显示上述原始闭环负号。因此，不能直接把脚本输出的符号认作完整 Minkowski 1PI 振幅符号。最终符号须从未 Wick 转动的完整分子积分一次性推导，避免在核定义与圈积分中重复或漏掉负号。

### 70.3 参数化因子 6 与外腿组合因子不是同一个东西

对四个传播子使用 Feynman 参数恒等式时，分母幂次为四，系数是

$$
\frac{1}{D_1D_2D_3D_4}
=\Gamma(4)\int_{x_i\ge0}\!d^4x\,\delta\!\left(1-\sum_i x_i\right)
\frac{1}{(\sum_i x_iD_i)^4},\qquad \Gamma(4)=6.
$$

因此，在采用未归一化单纯形测度 $d^4x\,\delta(1-\sum x_i)$ 时，因子 6 确实来自 Feynman 参数化；例如常数函数的单纯形积分是 $1/6$，与这个 6 相乘后为 1。它**不是**同种外腿的排列数，也不是 Wick 收缩的对称因子。

对于已经给定四条不同外腿标签的一个盒图拓扑，不能再仅因为有两个 $h$ 和两个 $s$ 就额外乘 $2!2!$。但完整四点函数仍需枚举与场类型相容的不同带标签外腿循环次序，并确认环路反向是否已包含在迹和厄米共轭项中。当前文档尚未从完整 Wick 收缩推导这些不等价图的最终总数，所以整体图组合因子仍未封口。

### 70.4 一个实质性纠错：当前 $hhss$ 数值不是已核实的 $hhss$ 动量系数

第 68 节的程序把 $hhss$ 的路径级 Yukawa 系数换成相邻型，但仍使用为固定 $hshs$ 外腿路由推导的同一组 $f_{ij,\alpha}$、$g_\alpha$ 和 $d_\alpha$。这是一个**尚未验证的路由复用**：$f,g,d$ 不仅依赖传播子参数，还依赖每条外腿动量在四个顶点上的具体分配。改变顶点序列时，必须先把有标签的外动量重新分配到四个顶点，重做平移向量 $t_i$，再重新求出 $t_i\cdot t_j$ 与 $\delta\Delta$ 的系数。

因此，第 67–68 节中 $hhss$ 六个数值可以保留为“把相邻型路径系数代入交替型参数核所得的测试输出”，但**不能**当作正确的 $hhss$ 固定路由积分结果。其等质量连续性只说明这个代数程序在该核上连续，不是对正确 $hhss$ 路由的等质量极限验证。后续应先纠正路由，再重新计算六个系数并检查 $m_1=m_2$ 极限。

### 70.5 EFT 一圈图与 UV–EFT 相减：目前为什么还不能给最终数值

盒图 UV 展开与 EFT 振幅相减必须使用同一组外腿标签、相同的外动量路由、相同的正规化方案和同一个算符基底。当前计算尚未完成正确的 $hhss$ 路由与全部带标签图的组合计数；如果现在把 EFT 泡图或接触图的结果减到当前数值上，减法双方并非已证明对应同一个带标签 1PI 振幅。

此外，UV 拉氏量含有轻费米子与重费米子的混合，而低能 EFT 中有维数五 Yukawa 算符及其破缺相展开。EFT 的图必须按所匹配的 Green 函数逐个列出：维数五顶点构成的轻费米子环、由真空期望值产生的相关顶点，以及该外态下允许的局域反项。不能把此前针对混合二点函数的 EFT 泡图/接触图结果直接搬到四标量 $hhss$ 盒图投影。

故本节不报告 UV–EFT 差值或最终 Wilson 系数。需要先完成：

1. 从原始规则固定一个带标签外腿振幅，并独立确定闭环/Wick 转动的整体符号；
2. 分别重建 $hshs$ 与 $hhss$ 的平移向量及六个动量核；
3. 对每个不等价带标签图执行积分，并由 Wick 收缩推导图的总组合因子；
4. 在同一算符基底下计算 EFT 图、反项和重整化，再作 UV–EFT 相减。

### 70.6 本节状态

本节完成了已有程序的重跑、单个解析系数的复现，以及对闭合费米子环显式负号、Feynman 参数因子 6 和外腿组合因子的来源审计。它也识别出一个会影响结论的具体问题：现有 $hhss$ 数值沿用了尚未重新推导的 $hshs$ 动量核，必须降级为测试输出并重新计算。

**尚未完成：** $hshs$ 剩余系数的解析闭式、正确路由下 $hhss$ 的六个积分、完整带标签图计数，以及 EFT 一圈图/反项和 UV–EFT 相减。本节没有给出最终匹配结果。


## 第 71 节：交替型 $hshs$ 六个质量比系数的解析化简（固定混合参数点）

本节推进第 70 节的第一项任务。通过先把相同 $(p,n_1,n_2,n_3,n_4,I_\rho)$ 的单项式积分项分组，再对每个不同的超几何积分核做解析化简，避免了旧实现中直接展开总和时的表达式膨胀。**本节已实际得到 $hshs$ 六个系数在同一固定混合参数点下的全部闭式。** 这里的闭式仍然是固定路由、固定参数点的积分系数，不是一般混合角的公式，也不是已完成外腿排列和 UV–EFT 相减后的 Wilson 系数。

### 71.1 设置与计算策略

保持第 69 节的参数：

$$
a=1,\quad b=\frac7{10},\quad c_L=\frac35,\quad s_L=\frac45,\quad c_R=\frac5{13},\quad s_R=\frac{12}{13},\quad m_2=1,\quad r=\frac{m_1}{m_2}>0.
$$

优化步骤是先将全部 16 条内部质量路径产生的参数多项式项，按相同的 $p$、单项式指数 $(n_1,n_2,n_3,n_4)$ 和重质量指标集合 $I_\rho$ 聚合；然后才计算

$$
J_p=\frac{\prod_i n_i!}{(N+3)!}\,{}_2F_1\!\left(p,N_1+k;N+4;1-r^2\right),
$$
其中 $N=\sum_i n_i$、$k=|I_\rho|$、$N_1=\sum_{i\in I_\rho}n_i$。这一分组不改变积分，只减少重复超几何化简和中间表达式规模。程序使用 Python 与 SymPy 精确有理运算；数值交叉核验使用现有积分程序与 mpmath。

### 71.2 六个系数的闭式

为避免重复书写完全相同的多项式，定义共同分母

$$D(r)=r^2(r-1)^5(r+1)^5=r^2(r^2-1)^5.$$

第一个多项式为

$$
\begin{aligned}
P_1(r)={}&14080r^{12}-89920r^{11}-76933r^{10}+269760r^9\ln r+674400r^9\\
&+59844r^8\ln r+145538r^8-6204480r^7\ln r+4361120r^7\\
&-255336r^6\ln r-6204480r^5\ln r-4361120r^5\\
&+59844r^4\ln r-145538r^4+269760r^3\ln r-674400r^3\\
&+76933r^2+89920r-14080.
\end{aligned}
$$

第二个多项式为

$$
\begin{aligned}
P_2(r)={}&21760r^{12}-179840r^{11}+153600r^{10}\ln r-302479r^{10}\\
&+539520r^9\ln r+1348800r^9-153600r^8\ln r+1141112r^8\\
&-12408960r^7\ln r+8722240r^7-2405736r^6\ln r\\
&-12408960r^5\ln r-8722240r^5-153600r^4\ln r-1141112r^4\\
&+539520r^3\ln r-1348800r^3+153600r^2\ln r+302479r^2\\
&+179840r-21760.
\end{aligned}
$$

第五个多项式为

$$
\begin{aligned}
P_5(r)={}&10240r^{12}-44960r^{11}-76800r^{10}\ln r+35840r^{10}\\
&+134880r^9\ln r+337200r^9+166566r^8\ln r-352249r^8\\
&-3102240r^7\ln r+2180560r^7+819864r^6\ln r\\
&-3102240r^5\ln r-2180560r^5+166566r^4\ln r+352249r^4\\
&+134880r^3\ln r-337200r^3-76800r^2\ln r-35840r^2\\
&+44960r-10240.
\end{aligned}
$$

在当前固定混合参数点、当前 $hshs$ 路由及第 61–64 节的归一化下，六个结果为

$$
\boxed{\mathcal C_1=\mathcal C_3=-\frac{3969}{28561000000\pi^2}\frac{P_1(r)}{D(r)}}
$$

$$
\boxed{\mathcal C_2=\mathcal C_4=\mathcal C_6=-\frac{1323}{14280500000\pi^2}\frac{P_2(r)}{D(r)}}
$$

$$
\boxed{\mathcal C_5=-\frac{1323}{7140250000\pi^2}\frac{P_5(r)}{D(r)}}.
$$

这些等式中的系数相等是这次计算在该固定参数点下得到的解析恒等式；其背后的动量路由对称性仍需从带标签外腿置换独立说明，不能自动推广为完整四点函数的最终系数关系。

### 71.3 等质量极限与数值交叉核验

$P_i(r)/D(r)$ 在 $r=1$ 的表观奇点是可去奇点。解析取极限得到

$$
\begin{aligned}
\lim_{r\to1}\mathcal C_1=\lim_{r\to1}\mathcal C_3
&=-\frac{58110129}{142805000000\pi^2}\simeq-4.12295581519481\times10^{-5},\\
\lim_{r\to1}\mathcal C_2=\lim_{r\to1}\mathcal C_4=\lim_{r\to1}\mathcal C_6
&=-\frac{19370043}{35701250000\pi^2}\simeq-5.49727442025973\times10^{-5},\\
\lim_{r\to1}\mathcal C_5
&=-\frac{19370043}{71402500000\pi^2}\simeq-2.74863721012987\times10^{-5}.
\end{aligned}
$$

对非等质量点，闭式与原数值积分程序给出一致结果。例如：

| $r$ | $\mathcal C_1=\mathcal C_3$ | $\mathcal C_2=\mathcal C_4=\mathcal C_6$ | $\mathcal C_5$ |
|---:|---:|---:|---:|
| $1/2$ | $1.27935375286168\times10^{-4}$ | $1.67818170762747\times10^{-4}$ | $8.80525798095899\times10^{-5}$ |
| $0.7$ | $-9.37121410388819\times10^{-6}$ | $-1.51286838874434\times10^{-5}$ | $-3.61374432033296\times10^{-6}$ |
| $1.3$ | $-1.67745872299412\times10^{-5}$ | $-2.32434566350012\times10^{-5}$ | $-1.03057178248813\times10^{-5}$ |
| $2$ | $3.19838438215421\times10^{-5}$ | $4.19545426906868\times10^{-5}$ | $2.20131449523975\times10^{-5}$ |

还检查了质量标签交换的缩放关系。由于系数的质量维数为 $-2$，在同一个积分定义下，交换两质量应满足 $F(r)=r^{-2}F(1/r)$（这里 $m_2=1$ 且 $F(r)=\mathcal C(r)$）。在 $r=1.7$ 与 $r=1/1.7$ 的数值结果中，六个系数均满足该关系至当前数值精度。此检查是有用的回归测试，但不能替代完整 Feynman 振幅符号和组合因子的审计。

### 71.4 可复现文件与边界

新增 `optimized_closed_forms_mass_ratio.py`：按系数逐个计算，先聚合相同积分核，再输出解析表达式、$r\to1$ 极限以及 $r=1/2,0.7,1.3,2$ 的数值。运行示例：

```bash
python -m pip install sympy mpmath
python /mnt/data/optimized_closed_forms_mass_ratio.py --order hshs --alpha 2
```

其中 `--alpha` 取 1 到 6，分别对应 $\mathcal Q_1$ 到 $\mathcal Q_6$。另有 `verify_hshs_closed_forms.py` 用于独立重跑多个质量比下的数值积分并保存 JSON，输出文件名为 `hshs_closed_forms_verification.json`。为避免一次性符号化简偶发卡在单个超几何项上，闭式仍应通过 `optimized_closed_forms_mass_ratio.py --alpha N` 逐个生成；不应依赖一次批量符号运行。

**本节完成：** 在固定参数点下，$hshs$ 六个质量比系数的解析闭式均已得到，且用等质量极限和多个非等质量点核验。

**本节没有完成：** 一般混合角的通用闭式、正确路由下的 $hhss$ 六个系数、全部带标签外腿排列和 Wick 收缩因子、以及 EFT 一圈振幅/反项与 UV–EFT 相减。后续应先用相同聚合算法处理 $hhss$，但必须先重新推导该顶点次序的动量核，不能直接复用 $hshs$ 的 $f,g,d$。

## 第 72 节：相邻型 $hhss$ 六个系数的闭式、等质量极限与路由复核

本节完成相邻型的六个固定参数点闭式，并修正第 70.4 节中关于“不能复用 $hshs$ 动量核”的过强判断。这里的关键是先明确外腿动量的标签：若 $q_1,q_2,q_3,q_4$ 始终依次附着在顶点 $V_1,V_2,V_3,V_4$，则平移后的动量核只由这组动量路由决定，不依赖该顶点处的标量究竟是 $h$ 还是 $s$。所以在**相同带标签动量路由**下，$hshs$ 和 $hhss$ 可以使用同一组 $f_{ij},g,d$；改变的是路径 Yukawa 系数，而不是几何动量核。

### 72.1 显式重建外动量路由

取四条传播子的外动量偏移为

$$
r_1=0,\qquad r_2=-q_2,\qquad r_3=-q_2-q_3,\qquad r_4=q_1,
$$

并令 $q_4=-(q_1+q_2+q_3)$。这对应四个外腿按 $q_1,q_2,q_3,q_4$ 依次附着在四个顶点上。Feynman 参数平移量为

$$
R=\sum_i x_i r_i=x_4q_1-(x_2+x_3)q_2-x_3q_3.
$$

按 $K=k+R$ 定义平移后的四个向量 $t_i=r_i-R$，记 $A=x_2+x_3$，得到

$$
\begin{aligned}
t_1&=-x_4q_1+Aq_2+x_3q_3,\\
t_2&=-x_4q_1+(A-1)q_2+x_3q_3,\\
t_3&=-x_4q_1+(A-1)q_2+(x_3-1)q_3,\\
t_4&=(1-x_4)q_1+Aq_2+x_3q_3.
\end{aligned}
$$

直接点乘可恢复第 61.1 节列出的全部 $f_{ij,\alpha}$。同时

$$
\delta\Delta=\sum_i x_i r_i^2-R^2
$$

给出第 61.3 节的六个 $d_\alpha$；四斜线迹的角向平均则给出第 61.2 节的 $g_\alpha$。这证明这些核在当前**明确的动量标签约定**下是通用的，不会因为把顶点类型从 $hshs$ 改成 $hhss$ 就自动改变。

因此，第 70.4 节把现有 $hhss$ 输出整体降级为“错误路由结果”的说法需要更正：当前程序的 $hhss$ 系数与下文重新生成的闭式数值一致。更准确的边界是：这些结果对应上面明确给定的固定路由；若改用不同的外腿排列，必须同步置换 $q_i$、$f,g,d$ 和顶点类型，不能只置换 Yukawa 矩阵。

### 72.2 解析化简设置

继续采用第 69–71 节相同的固定参数点

$$
a=1,\quad b=\frac7{10},\quad c_L=\frac35,\quad s_L=\frac45,\quad c_R=\frac5{13},\quad s_R=\frac{12}{13},\quad m_2=1,\quad r=\frac{m_1}{m_2}>0.
$$

按与 $hshs$ 相同的优化方法，先聚合相同的 $(p,n_1,n_2,n_3,n_4,I_\rho)$，再将整数参数超几何函数化为有理函数与 $\ln r$。定义

$$D(r)=r^2(r-1)^5(r+1)^5.$$

为紧凑起见，把各系数写为 $-147P_\alpha/(N_\alpha\pi^2D)$，其中 $P_\alpha$ 如下。

$$
\begin{aligned}
P_1={}&190080r^{12}+138080r^{11}-1151959r^{10}-4470240r^9\ln r+4372400r^9\\
&-3594732r^8\ln r+9475610r^8-2640480r^7\ln r-6696880r^7\\
&-23778264r^6\ln r-2640480r^5\ln r+6696880r^5\\
&-3594732r^4\ln r-9475610r^4-4470240r^3\ln r-4372400r^3\\
&+1151959r^2-138080r-190080,
\end{aligned}
$$

$$
\begin{aligned}
P_2={}&391680r^{12}-533120r^{11}+1404438r^{10}\ln r-2443581r^{10}\\
&+1599360r^9\ln r-4113600r^9-44076r^8\ln r+612774r^8\\
&+60558720r^7\ln r-47151680r^7+9676668r^6\ln r\\
&+60558720r^5\ln r+47151680r^5-44076r^4\ln r-612774r^4\\
&+1599360r^3\ln r+4113600r^3+1404438r^2\ln r+2443581r^2\\
&+533120r-391680,
\end{aligned}
$$

$$
\begin{aligned}
P_3={}&760320r^{12}-1578240r^{11}+10476r^{10}\ln r-2979379r^{10}\\
&+4245120r^9\ln r+2123520r^9+8351484r^8\ln r-8276586r^8\\
&+20906880r^7\ln r-28218880r^7+26058096r^6\ln r+4531968r^6\\
&+55313280r^5\ln r+6428160r^5+8351484r^4\ln r+219754r^4\\
&+24888960r^3\ln r+18520320r^3+3031788r^2\ln r+6504243r^2\\
&+2725120r-760320,
\end{aligned}
$$

$$
\begin{aligned}
P_4={}&783360r^{12}+2211200r^{11}-222912r^{10}\ln r-2990755r^{10}\\
&-39571200r^9\ln r+27782720r^9-22818564r^8\ln r+39347742r^8\\
&+55242240r^7\ln r-114662720r^7-101817816r^6\ln r+4531968r^6\\
&+89648640r^5\ln r+92872000r^5-22818564r^4\ln r-47404574r^4\\
&-18927360r^3\ln r-7138880r^3+2798400r^2\ln r+6515619r^2\\
&-1064320r-783360,
\end{aligned}
$$

$$
\begin{aligned}
P_5={}&737280r^{12}+40320r^{11}-2798400r^{10}\ln r-2700053r^{10}\\
&-16834560r^9\ln r+27840320r^9-5939292r^8\ln r+28400306r^8\\
&-110772480r^7\ln r+39296960r^7-88408296r^6\ln r+4531968r^6\\
&-76366080r^5\ln r-61087680r^5-5939292r^4\ln r-36457138r^4\\
&+3809280r^3\ln r-7196480r^3+222912r^2\ln r+6224917r^2\\
&+1106560r-737280,
\end{aligned}
$$

$$
\begin{aligned}
P_6={}&783360r^{12}-3196800r^{11}+2819352r^{10}\ln r-3258705r^{10}\\
&+25324800r^9\ln r-23593280r^9+22642260r^8\ln r-44953478r^8\\
&+152586240r^7\ln r-95734720r^7+140524488r^6\ln r+4531968r^6\\
&+186992640r^5\ln r+73944000r^5+22642260r^4\ln r+36896646r^4\\
&+45968640r^3\ln r+44237120r^3+5840664r^2\ln r+6783569r^2\\
&+4343680r-783360.
\end{aligned}
$$

六个积分系数为

$$
\boxed{\begin{aligned}
\mathcal C_1^{(hhss)}&=-\frac{147}{14280500000\pi^2}\frac{P_1(r)}{D(r)},\\
\mathcal C_2^{(hhss)}&=-\frac{147}{28561000000\pi^2}\frac{P_2(r)}{D(r)},\\
\mathcal C_3^{(hhss)}&=-\frac{147}{57122000000\pi^2}\frac{P_3(r)}{D(r)},\\
\mathcal C_4^{(hhss)}&=-\frac{147}{57122000000\pi^2}\frac{P_4(r)}{D(r)},\\
\mathcal C_5^{(hhss)}&=-\frac{147}{57122000000\pi^2}\frac{P_5(r)}{D(r)},\\
\mathcal C_6^{(hhss)}&=-\frac{147}{57122000000\pi^2}\frac{P_6(r)}{D(r)}.
\end{aligned}}
$$

这些是固定混合参数、固定外腿路由下的解析积分系数。由于 $D(r)$ 在 $r=1$ 有五阶零点，等质量点必须通过解析极限计算，不应把 $r=1$ 直接代入未约分形式。

### 72.3 等质量极限

对六个闭式分别取 $r\to1$，得到

$$
\begin{aligned}
\mathcal C_1(1)&=\frac{8519973}{71402500000\pi^2}\simeq 1.20899653227935\times10^{-5},\\
\mathcal C_2(1)&=-\frac{113890161}{71402500000\pi^2}\simeq-1.61611791152080\times10^{-4},\\
\mathcal C_3(1)&=-\frac{341670483}{285610000000\pi^2}\simeq-1.21208843364060\times10^{-4},\\
\mathcal C_4(1)&=-\frac{79810269}{285610000000\pi^2}\simeq-2.83129824652266\times10^{-5},\\
\mathcal C_5(1)&=\frac{147970053}{285610000000\pi^2}\simeq 5.24929131108135\times10^{-5},\\
\mathcal C_6(1)&=-\frac{831311019}{285610000000\pi^2}\simeq-2.94910599838934\times10^{-4}.
\end{aligned}
$$

这些极限与第 67–68 节等质量数值结果一致。进一步在 $r=1/2,2$ 处，闭式数值也分别重现原积分程序的六个输出，例如 $\mathcal C_1(2)=-9.03227109231993\times10^{-5}$、$\mathcal C_2(2)=-1.51461546715154\times10^{-4}$、$\mathcal C_3(2)=-9.07910076075895\times10^{-5}$、$\mathcal C_4(2)=-1.44061399053701\times10^{-4}$、$\mathcal C_5(2)=-2.96521718156351\times10^{-5}$、$\mathcal C_6(2)=-1.51929843399544\times10^{-4}$。

### 72.4 本节完成与未完成的事项

**已完成：** (i) 从 $r_i$ 与 $R$ 明确推导了当前通用动量核；(ii) 解析化简 $hhss$ 六个质量比系数；(iii) 计算每个系数的等质量极限，并与原数值积分结果交叉核验；(iv) 更正了第 70.4 节过强的路由判断。

**仍未完成：** 上述结果还没有把全部带标签外腿排列求和，也没有从 Wick 收缩独立确定完整四点函数的总组合因子；闭合费米子环的整体符号和 Wick 转动仍需在原始 Minkowski 振幅中统一处理。最后还需要按同一 Green 函数、动量基底和重整化方案计算 EFT 一圈图与反项，再做 UV–EFT 相减。因此这些闭式是 UV 盒图固定排列的积分系数，不应直接标记为最终 Wilson 系数。

## 第 73 节：带标签 $hhss$ 四点函数的费米子行列式、Wick 收缩计数与动量投影

本节把“不能凭 $2!2!$ 猜测组合因子”转成可核验的计数。这里固定四条**不同标签**的外腿

$$
h_1(p_1),\quad h_2(p_2),\quad s_1(p_3),\quad s_2(p_4),\qquad p_1+p_2+p_3+p_4=0,
$$

并使用基底

$$
(Q_1,Q_2,Q_3,Q_4,Q_5,Q_6)=(p_1^2,p_2^2,p_3^2,p_1\!\cdot p_2,p_1\!\cdot p_3,p_2\!\cdot p_3).
$$

### 73.1 原始 Minkowski 费曼规则与完整手征迹

质量基底相互作用为

$$
\mathcal L_{\rm int}=-h\bar\chi_i\Gamma_h^{ij}\chi_j-s\bar\chi_i\Gamma_s^{ij}\chi_j,
$$

其中

$$
\Gamma_X^{ij}=(Y_X)_{ij}P_R+(Y_X)^*_{ji}P_L,\qquad P_{R,L}=\frac{1\pm\gamma_5}{2},\quad X\in\{h,s\}.
$$

一张给定方向、给定外腿次序的四顶点闭合费米子圈，其未积分分子必须从完整 Dirac 迹开始：

$$
\begin{aligned}
\mathcal N_{1234}(k)={}&\operatorname{tr}_{D,\mathrm{flavor}}\!\left[
\Gamma_{X_1}\,(\slashed k_1+m_{i_1})
\Gamma_{X_2}\,(\slashed k_2+m_{i_2})
\Gamma_{X_3}\,(\slashed k_3+m_{i_3})
\Gamma_{X_4}\,(\slashed k_4+m_{i_4})\right],\\
&k_r=k+r_r,\qquad X_r\in\{h,s\}.
\end{aligned}
$$

这里每个顶点矩阵的左右手投影都必须保留。使用 $P_RP_L=0$、$P_R\gamma^\mu=\gamma^\mu P_L$ 与 $P_L\gamma^\mu=\gamma^\mu P_R$ 展开后，才可把分子按四个、两个或零个外部/环动量 slash 归类；质量翻转项来自传播子分子中的 $m_{i_r}$。因此，第 66 节代码里的路径量 $H_\rho,C_{ij}^{(\rho)},M_\rho$ 只有在与这个完整迹的每一种非零手征序列逐项对应后，才能被视为已经独立验证的分子系数。本节固定了审计表达式，但**尚未声称已经用独立 Dirac-algebra 软件逐项重算全部 16 条路径**。

对原始 Feynman 规则，单个有向盒图的显式因子为：

- 闭合费米子环：$-1$；
- 四个 Yukawa 顶点：$(-i)^4=+1$；
- 四条 Dirac 传播子的显式 $i$：$i^4=+1$；
- 每条传播子分母均保留 $+i0$，不能在 Wick 转动前先把分母符号任意改写。

故在把传播子显式 $i$ 提出之后，未做 Wick 转动的图积分前因子是闭环的 $-1$。Wick 转动时 $d^4k=i\,d^4K_E$，每个被替换的 $k^2$ 还带来 $k^2\mapsto-K_E^2$；因此不能只给已经合并了不同分子幂次的欧氏系数机械地补一个统一负号。要封口最终符号，必须从上式完整分子与四个分母一起转动，并与程序采用的 $B^{(p)}_{\rho\alpha}$ 定义逐项比对。

### 73.2 用费米子行列式独立确定外腿组合计数

对费米子积分，取 Dirac 算符 $D=D_0-V$，其中 $V=h\Gamma_h+s\Gamma_s$。费米子有效作用量满足

$$
\Gamma_f=-i\,\mathrm{Tr}\ln(D_0-V)
=\text{const}+i\sum_{n\ge1}\frac1n\mathrm{Tr}[(D_0^{-1}V)^n].
$$

四阶项为

$$
\Gamma_f^{(4)}=\frac{i}{4}\,\mathrm{Tr}[(D_0^{-1}V)^4].
$$

对四条不同标签的外腿 $h_1,h_2,s_1,s_2$ 求四次泛函导数，先有 $4!$ 个插入顺序；迹的循环性把每组四个循环旋转视为同一项。因而不等价的**循环序列数为**

$$
\frac{4!}{4}=6.
$$

固定 $h_1$ 作为循环序列的书写起点，六类为

$$
\begin{array}{lll}
(h_1,h_2,s_1,s_2),&(h_1,h_2,s_2,s_1),&(h_1,s_1,h_2,s_2),\\
(h_1,s_1,s_2,h_2),&(h_1,s_2,h_2,s_1),&(h_1,s_2,s_1,h_2).
\end{array}
$$

其中两类是交替型，四类是相邻型（相邻包括循环首尾相接的情况）。这给出明确的组合结论：**不能把某一个固定盒图的积分结果直接乘 $2!2!$；也不能再额外乘一个独立的“环路反向 2”，除非能证明该项尚未被六个带标签循环类覆盖。** 费米子行列式的四阶展开已把循环迹的 $1/4$ 与四次插入的循环重复计数一并处理。

### 73.3 六类外腿序列的动量基底变换

把 $p_4=-(p_1+p_2+p_3)$ 代入每个循环类的三个独立入射动量。若某一类在其顶点顺序中的动量为 $(q'_1,q'_2,q'_3,q'_4)$，其六个不变量 $Q'_\alpha$ 必须先用动量守恒写成基准 $Q_\beta$ 的线性组合，再对系数向量作转置变换。不能只交换 $h/s$ 顶点标签而保持 $Q_\alpha$ 不变。

为了复现这个计数与变换，新增 `labeled_hhss_wick_audit.py`。它列出六个循环类、各类的 $Q'_\alpha$ 变换矩阵，并把第 71.3 与 72.3 节已计算的固定路由系数向量投影回基准 $Q$ 基底。运行方式：

```bash
python -m pip install sympy
python /mnt/data/labeled_hhss_wick_audit.py
```

在现有固定混合参数点、$m_2=1$ 的条件下，程序给出的**暂定排列聚合**为：

| 质量比 | $Q_1$ | $Q_2$ | $Q_3$ | $Q_4$ | $Q_5$ | $Q_6$ |
|---|---:|---:|---:|---:|---:|---:|
| $r=1$ | $-3.81503\times10^{-4}$ | $-3.81503\times10^{-4}$ | $-5.94781\times10^{-4}$ | $-1.68225\times10^{-4}$ | $-5.94781\times10^{-4}$ | $-5.94781\times10^{-4}$ |
| $r=2$ | $-4.19601\times10^{-4}$ | $-4.19601\times10^{-4}$ | $-2.79255\times10^{-4}$ | $-5.32219\times10^{-4}$ | $-2.79255\times10^{-4}$ | $-2.79255\times10^{-4}$ |

**这些数值只验证了当前已算固定路由积分系数的标签置换和不变量投影程序。** 它们还没有包含经完整 Minkowski 分子独立核验后的统一整体符号，也没有验证所有 $H,C,M$ 路径系数确实等于完整 Dirac 迹的结果，所以不能把它们报告为物理四点振幅或 Wilson 系数。

### 73.4 本节结论与下一步

本节实际完成了：(i) 写明原始四顶点 Dirac 迹和显式 Feynman 因子；(ii) 由费米子行列式推出六个带标签循环类，排除了无依据的额外 $2!2!$ 因子；(iii) 实现六类的外动量不变量变换，并对现有固定路由结果作了暂定聚合。

仍需完成的关键工作是：

1. 对每个内部质量路径逐项展开完整手征迹，并将 $H_\rho,C_{ij}^{(\rho)},M_\rho$ 与迹的非零项一一对应；
2. 在 Minkowski 分母下对完整分子做 Wick 转动，确定所有 $k^2$ 幂次和 $i$ 因子的统一符号；
3. 将经核验的路径系数重新积分并对六个循环类求和；
4. 针对**同一个带标签 $hhss$ 1PI Green 函数**，从维数五 EFT 拉氏量列全轻费米子环图、相应反项与重整化条件，再在同一动量基底中做 UV–EFT 相减。

因此，当前推进到“外腿循环计数与基底投影已可复现”，但完整 Minkowski 振幅和 EFT 相减仍未完成。

## 第 74 节：独立枚举四个手征投影——验证 $H_\rho,C_{ij}^{(\rho)},M_\rho$ 的组合结构

本节针对第 73.1 节留下的第一项任务，先独立验证“哪些 Yukawa 乘积应乘哪些传播子质量”的手征组合，而不把这一步误称为完整的 Dirac 动量迹验证。

### 74.1 手征转移规则

在相邻两个顶点投影之间，传播子分子有两种选择：

$$
P_{R,L}(\slashed k+m)P_{R,L}=mP_{R,L},\qquad
P_{R,L}\slashed k P_{R,L}=0,
$$

$$
P_R\slashed k=\slashed kP_L,\qquad P_L\slashed k=\slashed kP_R.
$$

所以若第 $i$ 条传播子选取 slash 分子，它会翻转相邻投影的手征标签；若选取质量分子 $m_i$，相邻标签必须相同。对环上四个顶点的投影标签 $\sigma_i\in\{L,R\}$，定义转移集合

$$
T(\sigma)=\{i\mid \sigma_i\ne\sigma_{i+1}\},\qquad \sigma_5\equiv\sigma_1.
$$

环上的转移数必为偶数，因此 16 种投影序列按转移数分为 $2$ 个零转移、$12$ 个双转移和 $2$ 个四转移序列。

### 74.2 精确枚举结果

令 $u_i$ 表示第 $i$ 个顶点选取 $P_R$ 时的 Yukawa 矩阵元，$v_i$ 表示选取 $P_L$ 时的共轭矩阵元。对全部 $2^4=16$ 个 $\sigma$ 逐一求和，得到：

- $|T|=4$ 时，只有两种交替投影，权重为

$$
H=u_1v_2u_3v_4+v_1u_2v_3u_4.
$$

- $|T|=0$ 时，两种全同投影的权重为

$$
M=m_1m_2m_3m_4\,(u_1u_2u_3u_4+v_1v_2v_3v_4).
$$

- $T=\{i,j\}$ 时，对应的双转移权重为

$$
C_{ij}=\sum_{\sigma:T(\sigma)=\{i,j\}}
\left(\prod_{r=1}^4 w_r(\sigma_r)\right)
\left(\prod_{r\notin\{i,j\}}m_r\right),
\quad w_r(0)=u_r,\quad w_r(1)=v_r.
$$

新增程序 `audit_chiral_path_structure.py` 用独立的 $2^4$ 枚举直接构造这些表达式，并用 SymPy 对一般符号 $u_i,v_i,m_i$ 做精确差值检验。运行输出为：

```text
PASS: H_enum == H_expected
PASS: M_enum == M_expected
PASS: all six C_ij transition-set sums reproduce the definitions
chirality patterns by number of slash transitions: {0: 2, 2: 12, 4: 2}
total patterns: 16
```

运行方式：

```bash
python -m pip install sympy
python /mnt/data/audit_chiral_path_structure.py
```

### 74.3 这项审计证明了什么、没有证明什么

**已独立验证：** 第 66 节 $H,C_{ij},M$ 的组合定义，作为四个顶点手征投影与传播子质量分子的分类规则，是与 $P_{R,L}$ 的翻转/保持规则一致的；16 种手征配置已被完整覆盖，没有漏掉或重复某个转移集合。

**尚未验证：** 这个枚举没有计算 $\operatorname{tr}(\gamma^\mu\gamma^\nu\cdots)$ 的 Lorentz 张量系数，也没有核验第 61 节 $f_{ij},g,d$ 与每个 Dirac 迹项的符号和 $d$ 维因子。因此，它不能单独证明 $B^{(1,2,3)}_{\rho\alpha}$ 的所有系数正确，更不能替代 Minkowski–Euclidean 整体符号审计。

下一步应把这 16 种手征项逐项乘上相应的 Dirac 迹：四个 slash 对应四阶迹、双 slash 对应二阶迹、零 slash 对应 $\operatorname{tr}\mathbf1=4$，再在 $d=4-2\epsilon$ 下完成张量约化，并与第 61–64 节的核逐项比对。只有这一层也通过，才能将固定路由积分送入最终六类外腿求和和 EFT 相减。

## 第 75 节：用显式 $4\times4$ Dirac 矩阵核验动量分子迹的标量结构

本节继续审计第 74 节的手征分类，把 gamma 矩阵迹与 $H,C_{ij},M$ 的动量结构连接起来。使用度规 $(+---)$，定义

$$
G(k_1,k_2,k_3,k_4)=(k_1\cdot k_2)(k_3\cdot k_4)
-(k_1\cdot k_3)(k_2\cdot k_4)
+(k_1\cdot k_4)(k_2\cdot k_3).
$$

四 slash 的两个交替投影迹分别具有 $2G$ 与一个相反符号的 Levi-Civita 项。由于两种 Yukawa 权重一般不相等，不能说这个奇宇称项在**未积分分子**中必然逐项抵消。但在当前四点函数中，$k_i=K+t_i$，而三个独立外动量受 $p_4=-(p_1+p_2+p_3)$ 约束；四向量 Levi-Civita 项平移后至多含一个 $K$，其余三个向量是外动量差。对平移后的 $K$ 做对称圈积分时，该奇函数积分为零。因此，积分后保留的偶宇称分子结构为

$$
\boxed{\mathcal N_{\rm even}=2H\,G(k_1,k_2,k_3,k_4)
+2\sum_{i<j}C_{ij}\,k_i\cdot k_j+2M.}
$$

这里 $C_{ij}$ 已含另外两条传播子的质量分子，$M$ 已含四条传播子的质量乘积；上式中的系数 2 来自每个手征投影迹的 Dirac 维数，而不是外腿组合因子。

新增 `audit_dirac_trace_numerator.py`，用显式 $4\times4$ Dirac 矩阵和非退化整数四动量逐项核验：

- 两个交替四 slash 投影迹的无权和等于 $4G$；
- 对六个双 slash 转移集合，两个相反手征序列的迹和等于 $4(k_i\cdot k_j)$；
- 两个零 slash 投影的迹和等于 $4$。

运行方式：

```bash
python -m pip install sympy
python /mnt/data/audit_dirac_trace_numerator.py
```

本次运行的三项检查均通过。这里的程序是 gamma 迹代数的独立数值测试；一般四 slash 项的奇宇称部分是通过“平移后奇函数积分为零”论证去掉，而不是声称它对任意 Yukawa 权重都在被积函数层面消失。

### 75.1 与现有 $B^{(p)}_{\rho\alpha}$ 核的关系与剩余审计

上面的分子结构支持按四 slash、双 slash、零 slash 三类组织路径权重；但仍需把 $k_i=K+t_i$ 代入完整 $G$，逐项执行 $d=4-2\epsilon$ 的张量约化，再用

$$
\frac{K^2}{(K^2+\Delta)^4},\quad
\frac{(K^2)^2}{(K^2+\Delta)^4},\quad
\frac{1}{(K^2+\Delta)^4}
$$

及相应的降幂恒等式，将结果整理到当前程序的 $\Delta^{-1},\Delta^{-2},\Delta^{-3}$ 基底。只有完成这一代数等式，才算独立核验第 61–64 节的 $g_\alpha,f_{ij,\alpha},d_\alpha$ 和 $B^{(p)}_{\rho\alpha}$ 的所有系数；当前尚未把这一步全部做完。Minkowski–Euclidean 的总 $i$ 与符号审计也仍需与此步骤同步封口。

## 第 76 节：从 Dirac 分子到 $B^{(p)}_{\rho\alpha}$ 的精确代数闭环

本节把第 75 节留下的核对做成一个可运行的符号恒等式检查。目标不是再做一次数值积分，而是检查三组几何多项式 $f_{ij,\alpha}$、$g_\alpha$、$d_\alpha$ 是否确实由同一套带标签路由产生，以及第 61 节的圈积分核是否逐项等价于第 64 节的 $B^{(p)}$ 表示。

### 76.1 从 $t_i$ 重新生成六个 $f_{ij}$

沿用第 72.1 节路由，令 $A=x_2+x_3$，并写成 $t_i=a_{i1}q_1+a_{i2}q_2+a_{i3}q_3$：

$$
\begin{aligned}
t_1&=-x_4q_1+Aq_2+x_3q_3,\\
t_2&=-x_4q_1+(A-1)q_2+x_3q_3,\\
t_3&=-x_4q_1+(A-1)q_2+(x_3-1)q_3,\\
t_4&=(1-x_4)q_1+Aq_2+x_3q_3.
\end{aligned}
$$

把 Gram 矩阵写成

$$
G_q=\begin{pmatrix}
q_1^2&q_1\cdot q_2&q_1\cdot q_3\\
q_1\cdot q_2&q_2^2&q_2\cdot q_3\\
q_1\cdot q_3&q_2\cdot q_3&q_3^2
\end{pmatrix},
$$
则 $t_i\cdot t_j=a_i^T G_q a_j$。程序直接用此矩阵重算六个点积，再逐分量与第 61.1 节的六个 $f_{ij}$ 比较。六组恒等式全部通过，故这里不是把旧表达式重新抄入程序后自我比较，而是从 $t_i$ 的系数向量和 Gram 矩阵重新构造点积。

### 76.2 四斜线迹的 $K^2$ 系数

定义

$$
G(k_1,k_2,k_3,k_4)=(k_1\cdot k_2)(k_3\cdot k_4)-(k_1\cdot k_3)(k_2\cdot k_4)+(k_1\cdot k_4)(k_2\cdot k_3),
$$
并代入 $k_i=K+t_i$。在对称圈积分中使用

$$
\langle(K\cdot a)(K\cdot b)\rangle=\frac{K^2}{d}\,a\cdot b,
$$
则 $G$ 的 $K^2$ 项为

$$
K^2\left[t_{12}+t_{34}-t_{13}-t_{24}+t_{14}+t_{23}+\frac{2}{d}(t_{13}+t_{24})\right],
$$
其中 $t_{ij}=t_i\cdot t_j$。因此它在六个外动量不变量前的系数正是

$$
\boxed{g=f_{12}+f_{34}-f_{13}-f_{24}+f_{14}+f_{23}+\frac{2}{d}(f_{13}+f_{24})}.
$$

这里 $d=4-2\epsilon$ 应先保留在张量约化中。由于本节讨论的二阶动量积分核已经由第 61 节列出的五类积分确认 UV 收敛，最终组合后取 $d\to4$ 不会从这些积分本身丢失 $O(\epsilon)\times1/\epsilon$ 的有限项；但这不应推广到未组合的对数发散零阶振幅。

### 76.3 分母位移多项式的独立重建

采用传播子偏移

$$
r_1=0,\qquad r_2=-q_2,\qquad r_3=-q_2-q_3,\qquad r_4=q_1,
$$
和 $R=\sum_i x_i r_i$，直接计算

$$
\delta\Delta=\sum_i x_i r_i^2-R^2.
$$

所得六个系数严格为

$$
(d_1,d_2,d_3,d_4,d_5,d_6)=\big(x_4(1-x_4),A(1-A),x_3(1-x_3),2x_4A,2x_3x_4,2x_3(1-A)\big),
$$
与第 61.3 节一致。混合不变量前的因子 $2$ 来自 $R^2$ 中的交叉项；若改用 $2q_i\cdot q_j$ 作为基底，系数会相应改变，不能混用两种约定。

### 76.4 从 $I$ 核逐项还原 $B^{(p)}$

第 61 节中使用的有限积分为

$$
\begin{aligned}
I_0^{(4)}&=\frac{1}{16\pi^2}\frac{1}{6\Delta^2},&
I_1^{(4)}&=\frac{1}{16\pi^2}\frac{1}{3\Delta},\\
I_2^{(5)}&=\frac{1}{16\pi^2}\frac{1}{4\Delta},&
I_1^{(5)}&=\frac{1}{16\pi^2}\frac{1}{12\Delta^2},\\
I_0^{(5)}&=\frac{1}{16\pi^2}\frac{1}{12\Delta^3}.
\end{aligned}
$$

将它们代入

$$
\begin{aligned}
\mathcal K_{\rho\alpha}={}&2\left(\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}\right)I_0^{(4)}
+2H_\rho g_\alpha I_1^{(4)}\\
&-8d_\alpha\left[H_\rho I_2^{(5)}+S_\rho I_1^{(5)}+M_\rho I_0^{(5)}\right],
\qquad S_\rho=\sum_{i<j}C_{ij}^{(\rho)},
\end{aligned}
$$

并逐个收集 $\Delta^{-1},\Delta^{-2},\Delta^{-3}$，得到

$$
\mathcal K_{\rho\alpha}=\frac{1}{16\pi^2}\left[\frac{B_{\rho\alpha}^{(1)}}{\Delta}+\frac{B_{\rho\alpha}^{(2)}}{\Delta^2}+\frac{B_{\rho\alpha}^{(3)}}{\Delta^3}\right],
$$
其中

$$
\begin{aligned}
B_{\rho\alpha}^{(1)}&=H_\rho\left(\frac23g_\alpha-2d_\alpha\right),\\
B_{\rho\alpha}^{(2)}&=\frac13\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}-\frac23S_\rho d_\alpha,\\
B_{\rho\alpha}^{(3)}&=-\frac23M_\rho d_\alpha.
\end{aligned}
$$

因此，第 61 节与第 64 节的两种核写法在代数上完全一致，三个分母幂次的系数分别为 $2/3,-2,-2/3$ 等预期值；没有发现额外的因子 $2$ 或符号差异。

### 76.5 可复现检查

新增脚本 `verify_numerator_to_B_kernel.py`，使用 SymPy 精确符号运算完成四组断言：

1. 从 $t_i$ 与 Gram 矩阵重建全部六个 $f_{ij}$；
2. 从四斜线迹的 $K^2$ 角向平均重建 $g$；
3. 从 $\sum x_i r_i^2-R^2$ 重建六个 $d_\alpha$；
4. 将五类 $I$ 积分代入 $\mathcal K$，验证其与 $B^{(p)}/\Delta^p$ 形式严格相等。

实际运行输出为：

```text
PASS: all six f_ij vectors reconstructed from t_i dot t_j
PASS: four-slash K^2 coefficient yields g = ...
PASS: delta Delta gives the six d_alpha polynomials
PASS: I-integral kernel converts exactly to B1/Delta + B2/Delta^2 + B3/Delta^3
```

运行方式：

```bash
python -m pip install sympy
python verify_numerator_to_B_kernel.py
```

### 76.6 本节结论与未封口事项

**本节已完成：** $f_{ij}$、$g$、$d_\alpha$ 的几何动量多项式与 $B^{(1,2,3)}$ 的分母幂次整理，通过独立符号恒等式检查；第 61 节的 $I$ 积分写法与第 64 节的 $B$ 写法在有限二阶动量核层面一致。

**本节没有证明：** 完整 Minkowski 振幅的整体 $i$ 与符号、所有不等价外腿排列的总组合因子、不同环路方向是否重复、EFT 图与反项，以及 UV–EFT 相减。当前核的代数内部一致性不能代替这些图论与重整化检查。

下一步应把整体 Minkowski 因子单独记账：按拉氏量约定逐个乘四个 Yukawa 顶点 $(-iY)$、四个费米子传播子 $i(\slashed k+m)/(k^2-m^2+i0)$、闭费米子环的 $-1$，再对 $I_r^{(n)}$ 使用与实际分子幂次相匹配的 Wick 转动关系。只有在这一张独立符号表完成后，才把固定路由的有限核与带标签外腿排列求和组合。

## 第 77 节：Minkowski–Euclidean Wick 符号审计——发现 $B^{(1)}$ 与 $B^{(3)}$ 的相对符号疑点

第 76 节证明了既有 $I$ 核与 $B$ 核在代数上互相一致，但尚未证明该核的每一项都正确地来自 Minkowski 振幅。本节单独追踪 Wick 转动因子。此处明确采用度规 $(+---)$、传播子分母 $(K_M^2-\Delta+i0)^n$，并把外动量不变量 $\mathcal Q_\alpha$ 暂按 Minkowski 点积定义；如果把外动量不变量整体改定义为 Euclidean 点积，必须另行一致变换 $f,g,d$。

### 77.1 标量积分的 Wick 关系

定义

$$
J_{M,r}^{(n)}(\Delta)=\int\frac{d^4K_M}{(2\pi)^4}\frac{(K_M^2)^r}{(K_M^2-\Delta+i0)^n},
$$
以及正的 Euclidean 积分

$$
I_{E,r}^{(n)}(\Delta)=\int\frac{d^4K_E}{(2\pi)^4}\frac{(K_E^2)^r}{(K_E^2+\Delta)^n}.
$$

由 $K_M^0=iK_E^0$、$K_M^2=-K_E^2$ 与 $(K_M^2-\Delta)^n=(-1)^n(K_E^2+\Delta)^n$，得到

$$
\boxed{J_{M,r}^{(n)}=i(-1)^{n+r}I_{E,r}^{(n)}.}
$$

因此相关五类积分的 Wick 因子如下：

| 分子/分母结构 | $(r,n)$ | $J_M/(iI_E)$ |
|---|---:|---:|
| $1/(K^2-\Delta)^4$ | $(0,4)$ | $+1$ |
| $K^2/(K^2-\Delta)^4$ | $(1,4)$ | $-1$ |
| $(K^2)^2/(K^2-\Delta)^5$ | $(2,5)$ | $-1$ |
| $K^2/(K^2-\Delta)^5$ | $(1,5)$ | $+1$ |
| $1/(K^2-\Delta)^5$ | $(0,5)$ | $-1$ |

这些因子不能用一个统一的 $i$ 乘数代替；不同 $r+n$ 的项会有不同相对符号。

### 77.2 对二阶动量核逐项应用

在 Minkowski 分子中，分子展开的相关项按第 61 节记号为：

- 两斜线的外动量项：$+2\sum_{i<j}C_{ij}f_{ij}$，对应 $(r,n)=(0,4)$，Wick 后系数不变；
- 四斜线角向平均项：$+2HgK^2$，对应 $(r,n)=(1,4)$，Wick 后相对变号；
- 分母位移项为 $-4\delta\Delta$ 乘零阶迹 $2(HK^4+SK^2+M)$。分别使用 $(2,5),(1,5),(0,5)$ 的 Wick 因子后，在提出共同 $i$ 后得到 $+8HdI_2^{(5)}-8SdI_1^{(5)}+8MdI_0^{(5)}$。

故在**尚未乘共同闭费米子环负号与外腿组合因子**的约定下，Wick 后的积分核应整理为

$$
\begin{aligned}
\widetilde{\mathcal K}_{\rho\alpha}={}&2\left(\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}\right)I_0^{(4)}
-2H_\rho g_\alpha I_1^{(4)}\\
&+8d_\alpha\left[H_\rho I_2^{(5)}-S_\rho I_1^{(5)}+M_\rho I_0^{(5)}\right].
\end{aligned}
$$

代入第 62 节的 Euclidean 积分值，得到相应的系数

$$
\begin{aligned}
\widetilde B_{\rho\alpha}^{(1)}&=H_\rho\left(-\frac23g_\alpha+2d_\alpha\right),\\
\widetilde B_{\rho\alpha}^{(2)}&=\frac13\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}-\frac23S_\rho d_\alpha,\\
\widetilde B_{\rho\alpha}^{(3)}&=+\frac23M_\rho d_\alpha.
\end{aligned}
$$

与第 64 节旧定义相比，$\widetilde B^{(2)}$ 一致，而 $\widetilde B^{(1)}$ 和 $\widetilde B^{(3)}$ 分别整体反号。共同的闭费米子环负号会把整个振幅整体乘以 $-1$，但不能消除这种**相对符号模式**。

### 77.3 当前判断的适用边界

这是一个需要优先解决的潜在不一致，而不是已经宣布最终物理结果错误。它依赖于以下约定同时成立：

1. $\mathcal Q_\alpha$、$f,g,d$ 均按文档中的 Minkowski 点积定义；
2. $I_r^{(n)}$ 是正的 Euclidean 积分；
3. $H,C_{ij},M$ 是 Minkowski 传播子分子迹展开后的系数；
4. 分母写作 $(K_M^2-\Delta+i0)^n$，并按上述方式 Wick 转动。

若旧推导在更早处已经把分子整体转换成 Euclidean gamma 矩阵形式，那么必须从那一步检查是否已将相应符号吸收进 $H,C,M$ 或 $f,g,d$；否则会发生重复或漏记 Wick 符号。下一步不能直接把 $\widetilde B$ 当成最终修正，而应从原始 Minkowski 盒图把每一项带着 $i$ 因子完整推到 Euclidean 表示，再与这里的表格逐项对照。

### 77.4 复现程序与结果

新增 `audit_minkowski_wick_signs.py`，运行输出逐项列出 $(r,n)$、Wick 因子和得到的系数，并确认：在上述明确约定下，旧 $B^{(1)}$ 与 $B^{(3)}$ 的符号模式和直接 Wick 转动不一致，$B^{(2)}$ 则一致。

```bash
python audit_minkowski_wick_signs.py
```

**本节结论：** 在继续外腿排列求和或 EFT 相减前，应先关闭这个符号问题。第 76 节的代数恒等式仍然成立，但它只是核的内部代数一致性；第 77 节指出了从 Minkowski 费曼积分到该核的转换可能没有逐项保持符号。完整匹配暂时不能宣称完成。

## 第 78 节：从原始 Minkowski 费曼规则记账——共同相位不能解释相对 Wick 符号

本节继续第 77 节提出的检查，先把原始图的共同费曼规则因子与各个积分项的 Wick 因子分开。这样可以确定一个重要边界：闭合费米子环的负号、四个顶点的 $i$ 因子以及四条传播子的 $i$ 因子只能给整个固定图一个共同因子，不能把 $B^{(1)}$、$B^{(2)}$、$B^{(3)}$ 之间的相对符号差异消掉。

### 78.1 固定有向环的共同费曼规则因子

对相互作用约定

$$
\mathcal L_{\rm int}=-\phi\,\bar\psi\,(Y_LP_L+Y_RP_R)\psi+\mathrm{h.c.},
$$

每个 Yukawa 顶点提供 $-i$ 乘相应的手征 Yukawa 矩阵；每条费米子传播子提供

$$
\frac{i(\slashed k+m)}{k^2-m^2+i0}.
$$

对一个固定的四顶点、四传播子闭合费米子环，单独看这些共同因子有

$$
(-i)^4=+1,\qquad i^4=+1,\qquad \text{closed fermion loop}=-1.
$$

因此，在尚未包含动量积分和外腿排列计数前，费曼规则的共同乘数是 $-1$。积分 Wick 转动又产生一个共同的 $i$，同时不同分子幂次产生不同的相对符号。共同的闭环负号不会改变这些相对符号。

需要强调：这里的 $(-i)^4$ 是对一个已指定顶点顺序和相应 Yukawa 矩阵乘积的记账；它**不**意味着所有外腿排列的组合因子已经确定，也不排除复共轭顶点的 Yukawa 矩阵顺序对路径系数的影响。

### 78.2 从 Minkowski 分子逐项转动

保留第 77 节的度规 $(+---)$、Minkowski 外动量点积，以及分母 $(K_M^2-\Delta+i0)^n$。在二阶外动量项中，按分子来源分组：

| 来源 | Minkowski 积分项（提出公共 $i$ 前） | $(r,n)$ | Wick 相对因子 | 提出公共 $i$ 后的项 |
|---|---|---:|---:|---|
| 双 slash 外动量项 | $+2\sum C_{ij}f_{ij}\,J_{M,0}^{(4)}$ | $(0,4)$ | $+1$ | $+2\sum C_{ij}f_{ij} I_{E,0}^{(4)}$ |
| 四 slash 的 $K^2q^2$ 项 | $+2Hg\,J_{M,1}^{(4)}$ | $(1,4)$ | $-1$ | $-2Hg I_{E,1}^{(4)}$ |
| 四 slash 零阶项乘分母位移 | $-8Hd\,J_{M,2}^{(5)}$ | $(2,5)$ | $-1$ | $+8Hd I_{E,2}^{(5)}$ |
| 双 slash 零阶项乘分母位移 | $-8Sd\,J_{M,1}^{(5)}$ | $(1,5)$ | $+1$ | $-8Sd I_{E,1}^{(5)}$ |
| 零 slash 项乘分母位移 | $-8Md\,J_{M,0}^{(5)}$ | $(0,5)$ | $-1$ | $+8Md I_{E,0}^{(5)}$ |

这里 $S=\sum_{i<j}C_{ij}$，而分母位移使用

$$
\Delta=\overline m^{\,2}-\delta\Delta,\qquad
\delta\Delta=\sum_i x_i r_i^2-\left(\sum_i x_i r_i\right)^2.
$$

故

$$
\frac{1}{(K_M^2-\overline m^{\,2}+\delta\Delta+i0)^4}
=\frac{1}{(K_M^2-\overline m^{\,2}+i0)^4}
-\frac{4\delta\Delta}{(K_M^2-\overline m^{\,2}+i0)^5}+O(q^4),
$$

解释了表中分母位移项的共同系数 $-4$。表中 $H,S,M$ 项分别再乘原始零阶分子 $2HK^4,2SK^2,2M$，于是系数依次为 $-8H,-8S,-8M$；之后才逐项使用 Wick 因子。这一步没有把所有项的符号预先合并。

### 78.3 对 $B$ 核的审计结论

用正 Euclidean 积分

$$
I_{E,0}^{(4)}=\frac{1}{16\pi^2}\frac{1}{6\Delta^2},\quad
I_{E,1}^{(4)}=\frac{1}{16\pi^2}\frac{1}{3\Delta},\quad
I_{E,2}^{(5)}=\frac{1}{16\pi^2}\frac{1}{4\Delta},
$$
$$
I_{E,1}^{(5)}=\frac{1}{16\pi^2}\frac{1}{12\Delta^2},\qquad
I_{E,0}^{(5)}=\frac{1}{16\pi^2}\frac{1}{12\Delta^3},
$$

可得在乘共同闭环因子之前的核

$$
\begin{aligned}
\widetilde B^{(1)}_{\rho\alpha}&=H_\rho\left(-\frac23g_\alpha+2d_\alpha\right),\\
\widetilde B^{(2)}_{\rho\alpha}&=\frac13\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}-\frac23S_\rho d_\alpha,\\
\widetilde B^{(3)}_{\rho\alpha}&=+\frac23M_\rho d_\alpha.
\end{aligned}
$$

所以原始费曼规则记账**没有消除**第 77 节发现的模式：相对于第 64 节旧核，$B^{(1)}$ 和 $B^{(3)}$ 反号，$B^{(2)}$ 不变。这个结论目前仍是对“指定 Minkowski 分子、指定外动量基底、指定正 Euclidean 积分”的条件性审计；如果前面的 $H,C,M$ 或外动量多项式在定义时已被转换成 Euclidean 约定，就必须对该转换进行追溯，不能直接把此结果称为最终 Wilson 系数。

### 78.4 复现程序与尚未完成的工作

新增 `audit_raw_minkowski_phase.py`，用于独立记账 $(-i)^4$、$i^4$、闭环负号和五类积分的 Wick 因子。运行：

```bash
python /mnt/data/audit_raw_minkowski_phase.py
```

脚本通过断言确认共同费曼规则因子与相对 Wick 因子分离，且在当前约定下 $B^{(1)}$、$B^{(3)}$ 相对旧核翻号、$B^{(2)}$ 不变。

**本节已完成：** 固定闭环的共同费曼规则相位记账；分母位移的 $-4\delta\Delta$ 展开；五类积分逐项 Wick 因子与核系数的对应。

**仍未完成：** (i) 从 UV 拉氏量逐顶点确定每个复 Yukawa 矩阵的方向、共轭和外腿标签；(ii) 把所有外腿排列及可能的反向环路统一计数；(iii) 回溯第 61–64 节的 $H,C,M$ 与 $\mathcal Q_\alpha$ 是否曾隐式采用 Euclidean 约定；(iv) 计算同一算符基底与重整化方案下的 EFT 一圈图和反项；(v) 完成 UV–EFT 相减。因此，当前最可靠的结论是“旧核存在一个必须在约定层面关闭的相对符号疑点”，而不是宣称匹配结果已经修正或完成。

## 第 79 节：计算程序依赖登记与符号链的可复现性边界

本节按用户要求，把本轮结论所依赖的计算程序、每个程序实际核验的对象、运行命令与未覆盖事项登记到主文档。**程序输出中的 PASS 只代表代码中写入的数学恒等式/断言成立；若输入的物理假设或待核对系数是手工给定的，PASS 不会独立验证这些输入。** 这一区分对第 77–78 节的 Wick 符号疑点尤其重要。

### 79.1 一键复现入口

新增程序：`/mnt/data/run_uv_eft_audit_suite.py`。在 Python 3 与 SymPy 可用的环境中执行：

```bash
python /mnt/data/run_uv_eft_audit_suite.py
```

程序依次运行下面五个审计脚本，捕获完整标准输出、退出码和各脚本 SHA-256，并将报告写到：

`/mnt/data/uv_eft_audit_suite_output.txt`

本次实际运行结果为 `SUITE_STATUS: PASS`，五个脚本的退出码均为 0。该结果只表示这五个程序成功运行，不表示完整 UV 振幅、所有外腿组合或最终 EFT 匹配已经通过。

### 79.2 本次结论所依赖的脚本清单

| 程序（均位于 `/mnt/data/`） | 计算/核验内容 | 实际通过的检查 | 明确不负责的内容 |
|---|---|---|---|
| `audit_chiral_path_structure.py` | 对四个顶点的 $2^4=16$ 种手征投影作精确符号枚举 | $H$、$M$ 与六个 $C_{ij}$ 的投影分类一致；转移数计数为 $2+12+2=16$ | 不核验完整顶点方向、所有复共轭约定或圈积分符号 |
| `audit_dirac_trace_numerator.py` | 使用显式 $4\times4$ Dirac 矩阵与固定非退化四动量测试迹恒等式 | 四 slash、六种双 slash、零 slash 迹结构通过 | 这是固定测试向量的矩阵代数测试；不独立计算完整带分母振幅，也不确定 Wick 转动和外腿组合因子 |
| `verify_numerator_to_B_kernel.py` | 用 SymPy 从当前路由重建 $f_{ij}$、$g$、$d_\alpha$，并检查积分核到旧 $B$ 核的代数化简 | 六个 $f_{ij}$、$g$、$d_\alpha$ 及旧 $B$ 核的代数转换通过 | **积分核到旧 $B$ 的转换是按脚本中写入的系数完成的；此脚本没有独立推导 Minkowski 到 Euclidean 的相对 Wick 符号** |
| `audit_minkowski_wick_signs.py` | 对给定的 $(r,n)$ 使用 $(-1)^{n+r}$ 逐项计算 Wick 因子，并比较新旧 $B$ 核 | 在给定约定下，$B^{(1)}$、$B^{(3)}$ 相对旧核反号，$B^{(2)}$ 不变 | 依赖脚本中预先列出的各项分子系数；不是从完整 UV 拉氏量自动生成分子 |
| `audit_raw_minkowski_phase.py` | 记录四顶点、四传播子和闭合费米子环的共同因子，并打印五类项的条件性 Wick 账本 | 共同因子与相对 Wick 因子在程序中分开；断言通过 | **名称中的 “raw Minkowski” 不应误读为完整原始振幅已自动推导：该脚本仍把五类项的分子前系数作为输入写死** |
| `derive_raw_minkowski_numerator.py` | 用显式 Minkowski Dirac 矩阵对一般手征顶点与四条传播子分子做 $2^4$ 种 slash/mass 掩码展开 | 全部 16 个掩码可计算；奇数 slash 掩码为零；偶数部分分别有 1 个零 slash、6 个双 slash、1 个四 slash 结构 | 尚未代入模型特定的 Yukawa 矩阵方向/复共轭，尚未作 $k_i=K+t_i$ 的外动量展开与 Wick 转动 |

辅助的既有数值积分程序还包括 `general_mass_ratio_integral.py`、`closed_form_mass_ratio_C1.py`、`optimized_closed_forms_mass_ratio.py`、`verify_hshs_closed_forms.py`；它们服务于质量比积分/固定参数点闭式的计算，不解决当前的原始 Minkowski 符号链，也不完成 EFT 相减。

### 79.3 复现日志摘要

一键运行生成的完整日志位于 `uv_eft_audit_suite_output.txt`。关键输出为：

```text
[audit_chiral_path_structure.py] EXIT_CODE: 0
PASS: H_enum == H_expected
PASS: M_enum == M_expected
PASS: all six C_ij transition-set sums reproduce the definitions

[audit_dirac_trace_numerator.py] EXIT_CODE: 0
PASS: the unweighted pair of alternating four-slash traces sums to 4*G
PASS: all six two-slash transition pairs sum to 4*(k_i dot k_j)
PASS: the two zero-slash projector traces sum to 4

[verify_numerator_to_B_kernel.py] EXIT_CODE: 0
PASS: all six f_ij vectors reconstructed from t_i dot t_j
PASS: explicit expansion of G(K+t1,...,K+t4) and angular averaging reproduces g
PASS: delta Delta gives the six d_alpha polynomials
PASS: I-integral kernel converts exactly to B1/Delta + B2/Delta^2 + B3/Delta^3

SUITE_STATUS: PASS
```

请注意：`verify_numerator_to_B_kernel.py` 中用于重构旧核的表达式是

$$
K_{\rm old}=\frac{2F}{6\Delta^2}+\frac{2Hg}{3\Delta}
-8d\left(\frac{H}{4\Delta}+\frac{S}{12\Delta^2}+\frac{M}{12\Delta^3}\right),
$$

它等价于

$$
B^{(1)}_{\rm old}=H\left(\frac23g-2d\right),\quad
B^{(2)}_{\rm old}=\frac13F-\frac23Sd,\quad
B^{(3)}_{\rm old}=-\frac23Md.
$$

所以该脚本证明的是**旧核内部代数一致**，并不独立证明其从 Minkowski 积分转换而来的符号正确。第 78 节的 Wick 账本则把不同 $(r,n)$ 的符号逐项加入，但其中分子前系数同样是输入假设。因此，两套程序在各自范围内都通过，却不能合并解读成“物理符号问题已经解决”。

### 79.4 下一步计算的明确任务与验收标准

下一步不再增加只复述既有输入系数的账本，而应编写一个真正从完整分子开始的符号程序：

1. 固定每个有标签顶点的 $\Gamma_{\phi_i}$，明确矩阵指标方向与复共轭；按环序构造
   $$
   \mathrm{Tr}\left[\Gamma_1(\slashed k_1+m_1)\Gamma_2(\slashed k_2+m_2)\Gamma_3(\slashed k_3+m_3)\Gamma_4(\slashed k_4+m_4)\right].
   $$
2. 用显式 Minkowski 度规 $(+---)$ 及 $k_i=K+t_i$ 展开到二阶外动量；把 $K^{2r}$ 的每个系数在 Wick 转动前保留。
3. 单独把外动量不变量定义为 Minkowski $Q_\alpha$，不在程序中静默改为 Euclidean 不变量；再对每个积分项施加 $J_{M,r}^{(n)}=i(-1)^{n+r}I_{E,r}^{(n)}$。
4. 将自动生成的五类系数与第 78 节手写账本逐项比较；若不一致，先修正账本或约定，再计算 $B$ 核。
5. 加入顶点方向/共轭与外腿循环类求和后，才进入 EFT 图、反项和 UV–EFT 相减。

**当前状态更新：** 几何动量核、手征路径分类和若干 Dirac 迹恒等式都有可运行的独立检查；但原始 Minkowski 分子到 Euclidean 积分的完整自动化追踪仍未完成。当前 $B^{(1)}$、$B^{(3)}$ 的反号差异继续列为待关闭的符号疑点，不能作为最终物理修正发布。


## 第 80 节：原始 Minkowski Dirac 分子的显式矩阵展开——完成第一层，尚未完成动量约化

为推进第 79.4 节的第一步，新增 `derive_raw_minkowski_numerator.py`。它直接构造度规 $(+---)$ 下的显式 $4\times4$ Dirac 矩阵，使用四个一般手征顶点

$$
\Gamma_i=u_iP_R+v_iP_L,
$$

以及四个传播子分子 $\slashed k_i+m_i$，按固定顺序计算

$$
\operatorname{tr}\left[\Gamma_1(\slashed k_1+m_1)\Gamma_2(\slashed k_2+m_2)\Gamma_3(\slashed k_3+m_3)\Gamma_4(\slashed k_4+m_4)\right].
$$

程序逐一展开 $2^4=16$ 个 slash/mass 掩码，而不是先把 $H,C_{ij},M$ 或五类积分系数写成输入。运行命令：

```bash
python /mnt/data/derive_raw_minkowski_numerator.py
```

本次输出：

```text
PASS: all 16 slash/mass masks evaluated with explicit Minkowski Dirac matrices
PASS: all odd-slash masks vanish
slash_count=0: masks=1, nonzero_traces=1
slash_count=2: masks=6, nonzero_traces=6
slash_count=4: masks=1, nonzero_traces=1
WROTE: /mnt/data/derive_raw_minkowski_numerator_output.txt
BOUNDARY: model-specific vertex orientations/conjugations and Wick rotation are not yet applied.
```

所有掩码的精确矩阵迹表达式保存在 `derive_raw_minkowski_numerator_output.txt`。该文件保留了 SymPy 矩阵运算展开后的表达式，体积较大、未做适合阅读的 Lorentz 不变量因式分解；它是可复现的中间产物，不应被当成最终的简洁解析结果。

### 80.1 这一层实际说明什么

1. 对一般手征顶点结构，奇数个 slash 分子的迹确实为零；非零的偶数结构分成零、双、四 slash 三类。
2. 双 slash 有六种位置组合，四 slash 只有一个全 slash 掩码；这与后续按传播子位置标记 $C_{ij}$ 和四 slash 结构的分类相容。
3. 这一步不再依赖 `audit_raw_minkowski_phase.py` 中预先写死的五类积分系数，因此补上了“显式矩阵迹能否按 16 个分子掩码展开”这一独立检查。

但它**还没有**证明第 78 节五类系数的符号，因为当前脚本没有把具体的 $Y_h,Y_s$ 质量本征态指标与复共轭顶点映射到 $u_i,v_i$，也没有代入 $k_i=K+t_i$、展开外动量到二阶、做角向平均或 Wick 转动。尤其是 $u_i,v_i$ 的循环顺序一旦映射错误，单独的矩阵迹程序不会替我们自动发现模型顶点标签错误。

### 80.2 更新后的程序依赖

一键入口仍为：

```bash
python /mnt/data/run_uv_eft_audit_suite.py
```

截至第 80 节，该入口运行六个脚本，其中新增 `derive_raw_minkowski_numerator.py`；第 81 节又加入 `audit_model_vertex_trace_mapping.py`，因此当前共运行七个脚本。完整输出与脚本 SHA-256 登记在 `uv_eft_audit_suite_output.txt`。本轮七个程序退出码均为 0。复现时应同时保存主文档、六个脚本与日志，不要只保存程序的 PASS 行。

### 80.3 下一步

下一步应把此处的 $u_i,v_i$ 直接绑定到具体有标签的 $Y_h,Y_s$ 或其复共轭矩阵元，并为 $hshs$ 与 $hhss$ 分别构造有向环。然后将每个 $k_i$ 替换为 $K+t_i$，保留外动量到二阶的全部项；再将自动得到的 $K^{2r}$ 系数逐项与第 78 节账本比较。只有这一对照通过，才可决定 $B^{(1)}$、$B^{(3)}$ 是否真的需要修正。

## 第 81 节：把具体 Yukawa 矩阵接入原始 Dirac 迹，并显式保留奇宇称项

本节推进第 80.3 节提出的第一步：不再只使用抽象的 $u_i,v_i$，而是将文档中采用的实质量基底 Yukawa 矩阵直接映射到带标签的四顶点环，并对 $hshs$ 与 $hhss$ 两类顶点次序逐条检查。新增程序为 `audit_model_vertex_trace_mapping.py`，并已加入一键审计入口 `run_uv_eft_audit_suite.py`。

### 81.1 固定的顶点与路径约定

采用当前文档的实 Yukawa 矩阵

$$
Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix},
$$

以及质量基底顶点约定

$$
V_{ij}^{(\phi)}=(Y_\phi)_{ij}P_R+(Y_\phi)_{ji}P_L
$$

（这里 Yukawa 矩阵取实；复耦合情形必须将第二项改为相应共轭矩阵元）。对路径 $\rho=(a_1,a_2,a_3,a_4)$，循环定义 $a_5=a_1$，程序直接设置

$$
u_r=(Y_{V_r})_{a_r a_{r+1}},\qquad v_r=(Y_{V_r})_{a_{r+1}a_r},$$

并按既定质量顺序

$$
(\mu_1,\mu_2,\mu_3,\mu_4)=(m_{a_2},m_{a_3},m_{a_4},m_{a_1})
$$

构造原始迹

$$
T_\rho=\operatorname{tr}\!\left[\Gamma_1(\slashed k_1+\mu_1)\Gamma_2(\slashed k_2+\mu_2)\Gamma_3(\slashed k_3+\mu_3)\Gamma_4(\slashed k_4+\mu_4)\right],
\quad \Gamma_r=u_rP_R+v_rP_L.
$$

这一步是从具体矩阵元到 Dirac 迹的映射检查，不涉及积分。

### 81.2 完整分子分解必须包含奇宇称 epsilon 项

本次审计中，若只拿 parity-even 的 $H,C_{ij},M$ 组合与单条路径的直接矩阵迹比较，$hhss$ 的路径 $(1,1,1,2)$ 会留下非零纯虚差额。这不是可忽略的数值误差，而是四个 slash 分子中含 $\gamma_5$ 的迹产生的 Levi-Civita 项。因而程序把分解写成

$$
\begin{aligned}
T_\rho={}&2H_\rho G+2\sum_{i<j}C_{ij}^{(\rho)}\,k_i\!\cdot k_j+2M_\rho\\
&+2i\,\varepsilon(k_1,k_2,k_3,k_4)\,H_{\rho,\mathrm{odd}},
\end{aligned}
$$

其中

$$
G=(k_1\!\cdot k_2)(k_3\!\cdot k_4)-(k_1\!\cdot k_3)(k_2\!\cdot k_4)+(k_1\!\cdot k_4)(k_2\!\cdot k_3),
$$

$$
H_{\rho,\mathrm{odd}}=u_1v_2u_3v_4-v_1u_2v_3u_4,
$$

而 $H_\rho=u_1v_2u_3v_4+v_1u_2v_3u_4$。程序用四个反变四动量分量构成的行列式实现 $\varepsilon(k_1,k_2,k_3,k_4)$；该符号约定与程序中 $\gamma^\mu$ 和 $\slashed k=\gamma^0k^0-\gamma^ik^i$ 的定义配套。若改变 $\epsilon^{0123}$ 或 $\gamma_5$ 约定，奇宇称项的单独符号会随之改变，parity-even 部分不受此影响。

### 81.3 运行结果

运行命令：

```bash
python /mnt/data/audit_model_vertex_trace_mapping.py
```

程序用一组满足 $c_L^2+s_L^2=c_R^2+s_R^2=1$ 的有理数混合参数、两种内部质量和四个非共线整数 Minkowski 动量，进行精确有理数矩阵迹检查；同时对一般符号混合参数单独进行路径耦合求和。实际输出：

```text
PASS: symbolic sum over 16 paths gives sum(H_odd)=sum(H)=0 for hshs
PASS: symbolic sum over 16 paths gives sum(H_odd)=sum(H)=0 for hhss
PASS: direct explicit Dirac trace equals the full projector decomposition, including the parity-odd epsilon term
PASS: hshs paths checked = 16
PASS: hhss paths checked = 16
```

这意味着：

1. 对程序使用的具体矩阵元方向和边质量约定，$hshs$ 与 $hhss$ 各自的 16 条路径，其直接 $4\times4$ 矩阵迹都与包含奇宇称项的手征投影分解一致（这是固定精确有理数测试点，不是对任意数值输入穷举）。
2. 对一般符号参数，固定顶点次序下对 16 条内部质量路径求和，程序严格得到 $\sum_\rho H_\rho=0$ 与 $\sum_\rho H_{\rho,\mathrm{odd}}=0$。因此，在**相同的带标签动量路由与同一组路径求和范围**下，四 slash 结构的 parity-even $H$ 权重和 parity-odd epsilon 权重都发生代数抵消。
3. 单条路径的 epsilon 项不能在构造原始迹时先行删除；它是在规定的完整内部路径求和之后才由上述恒等式抵消。若之后的计算只保留部分路径或给路径施加不同的路由/权重，必须重新检查该抵消条件。

### 81.4 本程序的依赖登记

| 项目 | 内容 |
|---|---|
| 程序 | `audit_model_vertex_trace_mapping.py` |
| 依赖 | Python 3、SymPy |
| 输入 | 文档中的 $Y_h,Y_s$、实顶点约定、路径 $\rho\in\{1,2\}^4$、边质量顺序、固定测试四动量 |
| 独立核验 | 直接矩阵迹 vs. $H,C_{ij},M$ 与 epsilon 项的解析分解；一般符号参数下 $\sum H=\sum H_{\rm odd}=0$ |
| 不覆盖 | Wick 转动、分母幂次符号、全部外腿排列/对称因子、EFT 图和反项、UV–EFT 相减 |
| SHA-256 | `48895e38b9f058185e79307a1bfc7da064eb9dfcfcb99ae2fec52f2ba5dcaf98` |

一键复现命令仍为：

```bash
python /mnt/data/run_uv_eft_audit_suite.py
```

本次已把新脚本加入审计入口，重新运行后 `SUITE_STATUS: PASS`。完整逐程序 stdout、退出码与 SHA-256 登记于 `uv_eft_audit_suite_output.txt`。这里的 PASS 只代表脚本在所声明的测试范围内通过，不代表完整匹配计算已完成。

### 81.5 对 Wick 符号疑点的影响与下一步

本节**没有**解决第 77–78 节的 $B^{(1)}$、$B^{(3)}$ 相对符号疑点。它解决的是更靠前的一层：当前矩阵元方向与路径约定下，原始 Dirac 迹的 parity-even/odd 分解能够复现，而且奇宇称项在完整 16 路径求和后按符号恒等式消失。

接下来应将每条路径的 $k_i$ 统一替换为 $K+t_i$，把本节的 $H,C,M$ 逐路径系数直接传给已核验的 $f_{ij},g,d$ 动量核，并让程序在 Wick 转动前输出每个 $K^{2r}$ 项的 Minkowski 系数；然后逐项施加积分转换公式，与第 78 节账本对照。该步骤必须保持 $\mathcal Q_\alpha$ 的 Minkowski 定义直到转换完成，不能在中途把 $f,g,d$ 静默解释为 Euclidean 外动量多项式。只有该自动化对照通过，才继续外腿排列和 EFT 相减。


## 第 82 节：逐路径耦合系数与候选 Wick 核的自动化对照

本节落实第 81.5 节的下一步：不再只验证单条路径的 Dirac 迹，而是把模型的 $Y_h,Y_s$ 矩阵映射到全部 16 条内部路径，逐路径构造 $H_\rho,C_{ij}^{(\rho)},M_\rho$，并把第 77 节提出的候选 $B^{(1)},B^{(2)},B^{(3)}$ 符号变化作为代数恒等式逐条检查。

### 82.1 新增程序与复现

程序：`audit_pathwise_wick_kernel.py`  
依赖：Python 3、SymPy。  
运行命令：

```bash
python /mnt/data/audit_pathwise_wick_kernel.py
```

SHA-256：`2444cd7d8198d216ce3b9c8029d3364ac26a685bee5f7f9e80b8549d6f039b00`

### 82.2 实际输出

```text
[hshs] paths=16
  sum H = 0
  sum M = 2*a**2*b**2*(c_L*c_R*m_1 - m_2*s_L*s_R)**2*(c_L*c_R*m_2 - m_1*s_L*s_R)**2
  nonzero path weights: H=16/16, M=16/16
[hhss] paths=16
  sum H = 0
  sum M = -2*a**2*b**2*(c_L*c_R*m_1 - m_2*s_L*s_R)*(c_L*c_R*m_2 - m_1*s_L*s_R)*(c_L*m_1*s_R + c_R*m_2*s_L)*(c_L*m_2*s_R + c_R*m_1*s_L)
  nonzero unweighted sum C(1, 3) = a**2*b**2*(c_L**2 + s_L**2)*(c_R**2 + s_R**2)*(c_L**2*c_R**2*m_1**2 + c_L**2*c_R**2*m_2**2 - 4*c_L*c_R*m_1*m_2*s_L*s_R + m_1**2*s_L**2*s_R**2 + m_2**2*s_L**2*s_R**2)
  nonzero path weights: H=16/16, M=16/16
PASS: all 32 path records satisfy the candidate B1/B3 sign flip and unchanged B2 algebraically
BOUNDARY: does not determine physical signs; does not include path-specific Delta denominators, full labeled external-leg sum, or EFT subtraction.
```

程序使用一般符号参数 $a,b,c_L,s_L,c_R,s_R,m_1,m_2$。对 $hshs$ 和 $hhss$ 各 16 条路径分别计算系数。可见两个顶点次序均有 $\sum_\rho H_\rho=0$，但这**不意味着** $H$ 项的积分贡献自动为零：每条路径的分母

$$
\Delta_\rho(x)=\sum_{i=1}^4x_i\mu_{i,\rho}^2-R^2(x)
$$

依赖该路径上的内部质量排列。一般而言，$\sum_\rho H_\rho=0$ 不推出 $\sum_\rho H_\rho/\Delta_\rho^p=0$。因此不能先无权重地把 $H$ 系数求和，再把该结果代入积分。

对 $M$ 项，程序复现了 $hshs$ 与 $hhss$ 的符号求和闭式；对 $C_{ij}$，$hhss$ 只有 $C_{13}$ 的无权重路径和一般非零。这里的“无权重路径和”仅用于对照系数，不等于完成了带路径依赖分母的环积分。

### 82.3 Wick 符号检查能证明什么、不能证明什么

程序逐路径验证了候选代数映射

$$
B^{(1)}_{\rm new}=-B^{(1)}_{\rm old},\qquad
B^{(2)}_{\rm new}=B^{(2)}_{\rm old},\qquad
B^{(3)}_{\rm new}=-B^{(3)}_{\rm old}.
$$

这项 `PASS` 只说明把第 77 节提出的候选新定义代入后，符号关系本身满足代数恒等式。它**不能决定哪套符号是物理正确的**，因为程序没有从未 Wick 转动的完整 Minkowski 被积函数自动推导这些系数，也没有逐项把路径特定的 $\Delta_\rho$、分母幂次和外动量不变量一起转换。

### 82.4 下一步的严格顺序

1. 对每条路径保留独立的 $\mu_{i,\rho}$ 与 $\Delta_\rho(x)$，不提前做无权重路径求和。
2. 从原始 Minkowski 分子 $T_\rho(K+t_i)$ 展开至外动量二阶，分别提取 $K^0,K^2,K^4$ 对应的系数。
3. 将每一项与其分母 $(K^2-\Delta_\rho+i0)^n$ 一起 Wick 转动；不得只转动分母而忽略 slash 分子中 $K_M^2\mapsto-K_E^2$ 的额外符号。
4. 在统一的 Minkowski 外动量不变量约定下，与 $f,g,d$ 核逐系数比较；如改用 Euclidean 外动量，必须在输出中显式转换全部 $\mathcal Q_\alpha$。
5. 只有该逐路径比较通过后，才进行带标签外腿排列与对称因子计数，之后计算 EFT 图和反项，最后作 UV–EFT 相减。

**当前状态：** 路径级耦合系数自动化核验已完成；物理 Wick 符号仍未关闭；路径加权积分、外腿排列、EFT 一圈匹配和最终 Wilson 系数均未完成。
## 第 83 节：从未平移传播子重新审计分母位移与 Wick 转动——发现此前 Euclidean 分母展开的符号不一致

本节沿第 82 节的下一步，先不做外腿求和或 EFT 相减，而是检查所有后续核公式的共同基础：Feynman 参数化后分母中的外动量二阶位移，在 Minkowski 与 Euclidean 约定之间究竟如何变号。这一检查发现，第 63 节所写的 Euclidean 分母 $4K_E^2+\Delta_0+\delta\Delta\u00024$ 与其前面的 Minkowski 传播子定义并不一致。该处必须更正；它会影响所有含 $d_\alpha$ 的项，因此此前的 Euclidean 核不能直接作为最终结果。

### 83.1 从原始传播子推导分母

取度规 $(+---)$，每条传播子分母为

$$
(k+r_i)^2-m_i^2+i0.
$$

引入 Feynman 参数 $x_i$，满足 $\sum_i x_i=1$，并定义

$$
R=\sum_i x_i r_i,\qquad K=k+R,
$$

以及

$$
\Delta_0=\sum_i x_i m_i^2,\qquad
\delta\Delta=\sum_i x_i r_i^2-R^2.
$$

则原始 Minkowski 分母的加权和严格为

$$
\begin{aligned}
\sum_i x_i[(k+r_i)^2-m_i^2]
&=K_M^2+\sum_i x_i r_i^2-R^2-\sum_i x_i m_i^2\\
&=K_M^2-\Delta_0+\delta\Delta.
\end{aligned}
$$

Wick 转动 $K_M^2\to-K_E^2$ 后，抽出整体负号，分母成为

$$
-(K_E^2+\Delta_0-\delta\Delta).
$$

因此对应的正 Euclidean 分母是

$$
\boxed{K_E^2+\Delta_0-\delta\Delta},
$$

而不是第 63 节中曾使用的 $K_E^2+\Delta_0+\delta\Delta$。由于 $\delta\Delta=O(q^2)$，对一般幂次 $n$ 的正确展开为

$$
\frac{1}{(K_E^2+\Delta_0-\delta\Delta)^n}
=\frac{1}{(K_E^2+\Delta_0)^n}
+n\frac{\delta\Delta}{(K_E^2+\Delta_0)^{n+1}}+O(q^4).
$$

对于此前主要使用的 $n=4$，线性项为 $+4\delta\Delta/(K_E^2+\Delta_0)^5$。相反，旧的加号分母会给出负的线性项。这不是单纯记号差异：这里的 $\delta\Delta$ 已经由传播子偏移 $r_i$ 定义，且其六个外动量系数就是第 76 节列出的 $d_\alpha$。

### 83.2 自动化核验程序

新增程序：`audit_denominator_wick_consistency.py`。依赖 Python 3 与 SymPy。程序直接把 Minkowski 分母代入 $K_M^2=-K_E^2$，并用符号级展开验证 $O(q^2)$ 项的正负号。

复现命令：

```bash
python /mnt/data/audit_denominator_wick_consistency.py
```

实际输出：

```text
PASS: Minkowski denominator after shift is K_M^2 - Delta_0 + deltaDelta.
PASS: Wick rotation gives Euclidean denominator K_E^2 + Delta_0 - deltaDelta.
PASS: correct Euclidean expansion has +4 deltaDelta/(K_E^2+Delta_0)^5 for the n=4 denominator.
PASS: the previously recorded K_E^2 + Delta_0 + deltaDelta convention has the opposite linear term.
CONSEQUENCE: the d_alpha sign in the Euclidean denominator expansion must be reconciled before accepting any B^(1), B^(2), B^(3) kernel.
BOUNDARY: does not recalculate the complete numerator, graph multiplicities, EFT subtraction, or Wilson coefficients.
```

SHA-256：`483d3f9a93d1f6d5ce8bca1a03f2fb56ae88f465cbaf1b44d9a8f07b24d8d594`（下次运行时可用 `sha256sum /mnt/data/audit_denominator_wick_consistency.py` 独立复核）。

### 83.3 对既有结果的影响范围

1. 第 76 节的 $f_{ij}$、$g$ 和 $d_\alpha$ 的纯代数重建仍然成立；本节没有发现这些多项式本身的代数错误。
2. 第 63 节的分母展开把 Euclidean 分母写成 $K_E^2+\Delta_0+\delta\Delta$，与原始 Minkowski 分母推导不一致，必须更正。
3. 第 77 节是从 Minkowski 分母 $K_M^2-\Delta+i0$ 和逐项积分 Wick 因子出发的独立账本；其候选 $B$ 核需要继续与修正后的 $\Delta_0-\delta\Delta$ 约定统一核对。不能仅因为第 63 节有误，就机械地把第 77 节全部反号；也不能把第 77 节的候选核直接宣布为最终 Wilson 系数。
4. 在把原始分子中 $K_M^{2r}$ 的系数、分母的 $n$ 次幂以及每条路径独立的 $\Delta_{0,\rho}$ 全部放在同一个表达式里之前，所有含 $d_\alpha$ 的 $B^{(p)}$ 都应标为“待重新统一约定”，而非已确认结果。
5. 本节没有计算全部外腿排列、组合/对称因子、EFT 一圈图、反项或 UV–EFT 差值，因此不提供最终匹配系数。

### 83.4 下一步

下一步将建立一个统一的逐项核：输入原始 Minkowski 分子中 $K_M^{2r}$ 的系数与分母幂次 $n$，以及 $\delta\Delta$ 的系数；程序同时执行分母位移展开和 Wick 规则 $J_{M,r}^{(n)}=i(-1)^{n+r}I_{E,r}^{(n)}$，自动生成 $\Delta^{-1},\Delta^{-2},\Delta^{-3}$ 各项，并与第 77 节账本逐项比较。然后再把模型每条路径的 $H_\rho,C_{ij}^{(\rho)},M_\rho$ 和路径质量插入，避免在路径加权积分前过早合并。只有该统一核一致后，才继续外腿排列与 EFT 相减。


## 第 84 节：在修正分母约定后，逐项从 Minkowski 核导出 Euclidean $B^{(p)}$

第 83 节确认正确的 Minkowski 分母为 $D_M=K_M^2-\Delta_0+\delta\Delta$。本节把 Wick 因子、分母展开与 Euclidean 积分值放进同一段可执行代数中，检查它们能否互相一致。新增程序 `derive_consistent_minkowski_to_euclidean_B.py`，依赖 Python 3 与 SymPy。

### 84.1 输入的 Minkowski 二阶核

在当前分子分解下，二阶外动量项在 Wick 转动前写为

$$
\frac{2F+2HgK_M^2}{(K_M^2-\Delta_0)^4}
-\frac{8\delta\Delta\,(HK_M^4+SK_M^2+M)}{(K_M^2-\Delta_0)^5}+O(q^4),
$$

其中 $F=\sum_{i<j}C_{ij}f_{ij,\alpha}$，$S=\sum_{i<j}C_{ij}$，$g=g_\alpha$，并将 $\delta\Delta=d\,\mathcal Q_\alpha$ 的单个不变量系数记作 $d$。这是本节程序的输入假设；模型特定的 $H,C,M$ 仍须逐路径提供，不能把它当作已完成的全振幅。

逐项使用

$$
J_{M,r}^{(n)}=i(-1)^{n+r}I_{E,r}^{(n)},
$$

并用

$$
I_0^{(4)}=\frac{1}{16\pi^2}\frac{1}{6\Delta^2},\quad
I_1^{(4)}=\frac{1}{16\pi^2}\frac{1}{3\Delta},\quad
I_2^{(5)}=\frac{1}{16\pi^2}\frac{1}{4\Delta},
$$

$$
I_1^{(5)}=\frac{1}{16\pi^2}\frac{1}{12\Delta^2},\quad
I_0^{(5)}=\frac{1}{16\pi^2}\frac{1}{12\Delta^3},
$$

程序得到

$$
\boxed{B^{(1)}=H\left(-\frac{2}{3}g+2d\right)},\qquad
\boxed{B^{(2)}=\frac13F-\frac23Sd},\qquad
\boxed{B^{(3)}=+\frac23Md}.
$$

这里的 $B^{(p)}$ 是将共同的 $1/(16\pi^2)$ 提取后的核系数。$d$ 项的符号来自 Minkowski 分母的 $+\delta\Delta$ 与 Wick 转动的联合处理，而不能仅从单独的 Euclidean 分母展开判断。

### 84.2 复现与实际输出

命令：

```bash
python /mnt/data/derive_consistent_minkowski_to_euclidean_B.py
```

程序输出包括五类积分项各自的 $(r,n)$、Wick 符号、转动后系数，以及最终的 $B^{(1)},B^{(2)},B^{(3)}$。末尾断言通过：

```text
PASS: termwise Minkowski expansion + Wick signs + Euclidean integral reduction reproduce the candidate B kernel.
BOUNDARY: assumes numerator decomposition stated in the script; does not derive model-specific numerator coefficients, sum external-leg permutations, or perform EFT subtraction.
```

SHA-256：`b4e45b0efc83210ec694439a8078d8a10975fc3e30ccbc280d796c16eaba8414`。

### 84.3 结果的正确解释

1. 在第 84.1 节明确列出的 Minkowski 二阶核假设下，候选核与逐项 Wick 转动、积分归约相容；这支持第 77 节的候选 $B^{(p)}$，而不是第 76 节由不一致的 Euclidean 分母位移约定得到的旧核。
2. 这不意味着此前的所有推导都自动正确。还必须从完整 Dirac 分子和模型顶点映射独立推导第 84.1 节输入核，确认 $F,H,S,M$ 各项的原始 Minkowski 系数与路由完全一致。
3. 当前核仍是每条内部路径的被积函数系数；路径质量决定的 $\Delta_{0,\rho}$ 必须逐路径保留。外腿排列/对称因子、EFT 图、反项、UV–EFT 相减以及最终 Wilson 系数仍未完成。

下一步将把第 81 节的模型特定路径系数、每条路径的质量排列与本节统一核拼接，输出逐路径六个 $\mathcal Q_\alpha$ 系数的参数积分表达式；同时独立检查全部带标签外腿排列，不能仅乘以猜测的排列数。

## 第 85 节：把修正后的 Wick 核逐路径接入模型 Yukawa 权重与质量分母

本节按第 81 节的路径约定，把模型 Yukawa 矩阵、每条内部路径的边质量、六个外动量不变量以及第 84 节的候选 Wick 核拼接成可复现的参数积分被积函数。新增脚本 `build_pathwise_matching_integrands.py`，输出机器可读表 `pathwise_candidate_integrands_32x6.csv`。本节的目标是**逐路径保留分母**，而不是把不同路径的 Yukawa 权重先求和后乘一个共同分母。

### 85.1 路径和质量分母

仍使用

$$
Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix}.
$$

对固定顶点序列 $V=(V_1,V_2,V_3,V_4)$ 和内部态路径 $\rho=(a_1,a_2,a_3,a_4)$，令 $a_5=a_1$，并定义

$$
u_r=(Y_{V_r})_{a_r a_{r+1}},\qquad
v_r=(Y_{V_r})_{a_{r+1}a_r},\qquad
\mu_r=m_{a_{r+1}}.
$$

其中 $u_r$、$v_r$ 分别是顶点的两个手征投影系数；边质量顺序为 $(m_{a_2},m_{a_3},m_{a_4},m_{a_1})$。每条路径的 Feynman 分母是

$$
\Delta_{0,\rho}(x)=\sum_{r=1}^4x_r\mu_r^2,\qquad x_r\ge0,\quad\sum_rx_r=1.
$$

不同路径一般具有不同的 $\Delta_{0,\rho}$。因此即使某些无权路径系数之和为零，也不能据此断言带分母积分的路径和为零。

### 85.2 六个不变量的逐路径核

取

$$
\mathcal Q_\alpha=(q_1^2,q_2^2,q_3^2,q_1\!\cdot q_2,q_1\!\cdot q_3,q_2\!\cdot q_3),
$$
并沿用第 72 节的固定路由 $r_1=0,r_2=-q_2,r_3=-q_2-q_3,r_4=q_1$。脚本从 $t_i=r_i-\sum_jx_jr_j$ 和 Gram 矩阵重新生成 $f_{ij,\alpha}$；$g_\alpha$ 按四斜线迹的 $K^2$ 项构造，在已经确认有限的二阶核中取 $d\to4$；$d_\alpha$ 则由 $\delta\Delta=\sum_i x_i r_i^2-R^2$ 直接生成。

对每条路径定义

$$
H_\rho=u_1v_2u_3v_4+v_1u_2v_3u_4,
$$
$$
C_{ij}^{(\rho)}=\sum_{\substack{\text{手征标签}\text{恰有两处转变为 }i,j}}
\left(\prod_{r=1}^4\text{对应的 }u_r\text{ 或 }v_r\right)
\left(\prod_{r\notin\{i,j\}}\mu_r\right),
\quad S_\rho=\sum_{i<j}C_{ij}^{(\rho)},
$$
$$
M_\rho=\left(\prod_{r=1}^4\mu_r\right)
\left(\prod_{r=1}^4u_r+\prod_{r=1}^4v_r\right),\qquad
F_{\rho\alpha}=\sum_{i<j}C_{ij}^{(\rho)}f_{ij,\alpha}.
$$

采用第 84 节的**候选**核，逐路径的三个系数为

$$
B_{\rho\alpha}^{(1)}=H_\rho\left(-\frac23g_\alpha+2d_\alpha\right),
$$
$$
B_{\rho\alpha}^{(2)}=\frac13F_{\rho\alpha}-\frac23S_\rho d_\alpha,\qquad
B_{\rho\alpha}^{(3)}=+\frac23M_\rho d_\alpha.
$$

于是单条路径、单个外动量不变量的候选被积函数写成

$$
\boxed{\mathcal I_{\rho\alpha}(x)=\frac{1}{16\pi^2}\left[
\frac{B_{\rho\alpha}^{(1)}}{\Delta_{0,\rho}(x)}+
\frac{B_{\rho\alpha}^{(2)}}{\Delta_{0,\rho}(x)^2}+
\frac{B_{\rho\alpha}^{(3)}}{\Delta_{0,\rho}(x)^3}\right].}
$$

固定路由下的参数积分为在四维单纯形上的积分。单纯形体积是 $1/6$；若采用归一化参数平均，才乘一次 $6$。不能在已按单纯形积分的表达式上再次重复乘该因子。脚本保存的是不含共同 $1/(16\pi^2)$ 的方括号部分，以便后续单独审计整体圈因子。

### 85.3 实现与运行结果

新增脚本：`build_pathwise_matching_integrands.py`。运行命令：

```bash
python /mnt/data/build_pathwise_matching_integrands.py
```

CSV 每行对应一个“顶点序列 × 内部路径 × 外动量不变量”，共 $2\times16\times6=192$ 行，列中包含边质量序列、$\Delta_{0,\rho}$、$H_\rho$、全部六个 $C_{ij}^{(\rho)}$、$S_\rho$、$F_{\rho\alpha}$、$g_\alpha$、$d_\alpha$ 和三个 $B$ 系数，以及组合后的被积函数。实际程序输出：

```text
PASS: generated 32 internal paths x 6 external invariants = 192 path-resolved rows.
PASS: both hshs and hhss retain path-specific Delta_0 = sum_i x_i m_edge_i^2.
Kernel per row: (1/16pi^2) * [B1/Delta0 + B2/Delta0^2 + B3/Delta0^3].
Parameter convention: x_i >= 0, sum_i x_i = 1; simplex volume = 1/6.
For normalized simplex average, multiply each fixed-ordering integral by 6 once; do not multiply twice.
BOUNDARY: fixed routing only; no sum over all six labeled external-leg cyclic orderings, no loop-combinatoric prefactor audit, and no EFT subtraction/counterterms.
```

CSV 的 SHA-256 为 `8251ebe1545e451f673ba9dad8133c2776df6bac5908ef67f4b6da5b3a2bdeae`。脚本的输入输出与符号变量均保留，便于独立复核。

### 85.4 当前能下的结论与不能下的结论

1. 已经把模型的两种顶点序列 $hshs$、$hhss$ 各自的 16 条内部态路径，逐一连接到正确的边质量排列和路径相关 $\Delta_{0,\rho}$；六个 $\mathcal Q_\alpha$ 的系数均已生成。
2. 该实现使用第 84 节的 Wick 核候选，因此是对**候选逐路径被积函数**的构造，不是对完整匹配结果的最终确认。分子核的模型映射、圈整体 $i$ 与符号、以及所有带标签外腿循环序列仍需在完整振幅中统一检查。
3. 当前只处理第 72 节明确写出的单一带标签路由，对 $hshs$ 和 $hhss$ 各生成一组路径数据。完整费米子行列式有 2 个 $hshs$ 和 4 个 $hhss$ 不等价带标签循环序列；不能把本节的单一路由结果简单乘以 $2$ 或 $4$，必须逐个重新映射 $q_i$ 与顶点类型后再求和。
4. 本节尚未计算 EFT 中对应的轻场圈图和反项，也没有完成 UV–EFT 差值、算符基底投影或最终 Wilson 系数。因此目前产物是下一步完整带标签振幅审计的输入数据，不应引用为已完成的一圈匹配系数。

### 85.5 下一步

下一步应将六个带标签循环序列逐一写出：每个序列都要把外动量 $q_1,q_2,q_3,q_4$ 映射到对应顶点，重新生成 $r_i,t_i,f_{ij},g,d$，并为每个内部路径建立独立的 $\Delta_{0,\rho}$。完成后才可对六个序列求和，并独立核查行列式展开的整体系数与圈反向关系；最后再计算 EFT 图和反项，形成 UV–EFT 差值。


## 第 86 节：可持续恢复与独立核验流程

本节把项目管理约定固化为可复用的恢复点，目的是在额度/会话中断后继续同一计算状态，并避免把候选结果误标成已完成匹配。新增文件 `UV_EFT_恢复点与核验清单.md` 作为精简恢复卡；新增 `audit_uv_eft_checkpoint.py` 用于核查文件、文档节号、CSV 结构与行数。该审计脚本只检查产物完整性，不证明物理推导正确。

### 86.1 当前状态分级

- **已验证的代数约定**：第 83 节中的 Minkowski 分母与 Wick 后 Euclidean 分母的符号关系，通过独立程序检查。
- **条件成立的候选核**：第 84 节的 $B^{(1,2,3)}$ 依赖显式列出的 Minkowski 二阶核假设；尚未从全部带标签的原始 UV 四点振幅独立导出。
- **固定路由候选数据**：第 85 节脚本成功生成 192 行数据，但只覆盖两类顶点类型序列的各一个固定外腿路由；不代表六种带标签循环序列之和。
- **尚未完成**：全外腿排列、圈反向与组合因子审计、EFT 图和反项、UV–EFT 相减、IR 抵消、算符基底投影及最终 Wilson 系数。

### 86.2 每次续算的最低交付标准

1. 记录本次使用的输入文件、脚本、符号约定和输出文件。
2. 对新旧结论分别标记“已验证、条件成立、待验证、已否定”。
3. 对每个程序断言说明其测试范围；不得把文件存在或测试通过等同于物理结论成立。
4. 更新恢复清单，保存脚本运行命令、关键输出和 SHA-256。
5. 先完成可独立验证的小任务，再进入下一个物理模块；最终匹配必须由 UV 原始振幅、EFT 图与反项在同一方案下相减得到。

### 86.3 当前恢复点与下一任务

当前恢复点为第 85 节固定路由候选核。下一任务是从原始 UV 四点振幅构造六种带标签外腿循环序列的映射表。逐一记录顶点类型、外腿动量、传播子偏移 $r_i$、内部态路径、质量序列和 $\Delta_{0,\rho}$；先检查动量守恒和顶点类型，再生成各自的 $f,g,d$。不得直接把已有路由结果乘以 2 或 4，也不得先把路径权重合并后套用共同分母。

复现命令：

```bash
python /mnt/data/audit_uv_eft_checkpoint.py
python /mnt/data/audit_denominator_wick_consistency.py
python /mnt/data/derive_consistent_minkowski_to_euclidean_B.py
python /mnt/data/build_pathwise_matching_integrands.py
```

其中第一条是产物完整性检查；后三条分别核查分母 Wick 符号、在既定核假设下的 Wick 积分归约、以及固定路由逐路径数据生成。它们都不能单独证明完整 UV–EFT 匹配正确。

另新增一键运行器 `run_uv_eft_checkpoint_suite.py`，依次执行上述四项检查并将标准输出、退出码和时间戳保存到 `uv_eft_checkpoint_run.log`。这使恢复点检查可重复执行，但不扩大任何程序的物理证明范围。

## 第 87 节：六种带标签外腿循环序列的路由映射与候选核投影

本节正式执行第 86.3 节任务：固定带标签外腿 $h_1(p_1),h_2(p_2),s_1(p_3),s_2(p_4)$，其中 $p_4=-(p_1+p_2+p_3)$，并固定基底

$$
Q=(p_1^2,p_2^2,p_3^2,p_1\cdot p_2,p_1\cdot p_3,p_2\cdot p_3).
$$

### 87.1 六个不等价循环类

保持 $h_1$ 为循环书写起点，六个循环类为：

| 循环序列 | 顶点类型 | 固定路由的动量标签 $(q_1,q_2,q_3,q_4)$ |
|---|---|---|
| $h_1,h_2,s_1,s_2$ | $hhss$ | $(p_1,p_2,p_3,p_4)$ |
| $h_1,h_2,s_2,s_1$ | $hhss$ | $(p_1,p_2,p_4,p_3)$ |
| $h_1,s_1,h_2,s_2$ | $hshs$ | $(p_1,p_3,p_2,p_4)$ |
| $h_1,s_1,s_2,h_2$ | $hssh$ | $(p_1,p_3,p_4,p_2)$ |
| $h_1,s_2,h_2,s_1$ | $hshs$ | $(p_1,p_4,p_2,p_3)$ |
| $h_1,s_2,s_1,h_2$ | $hssh$ | $(p_1,p_4,p_3,p_2)$ |

这里 $q_1,q_2,q_3$ 是固定路由所需的前三个顶点入射动量，$q_4=-(q_1+q_2+q_3)$。$hssh$ 虽然循环首尾相接处是 $hh$，在当前书写起点下仍应保留实际序列，不能误标成 $hshs$。

### 87.2 不变量基底变换

对每个循环类，程序用向量表示

$$
q_1=v_1^ap_a,\quad q_2=v_2^ap_a,\quad q_3=v_3^ap_a,
$$

并从基准 Gram 矩阵直接构造

$$
Q'=(q_1^2,q_2^2,q_3^2,q_1\cdot q_2,q_1\cdot q_3,q_2\cdot q_3)^T=TQ.
$$

若固定路由在 $Q'$ 基底中的系数向量是 $b'$, 则回投到统一基底的系数为 $b=T^Tb'$。六个循环类的变换矩阵行列式均为 $+1$；这验证每个所选的三动量基底是非退化的，并且变换保留六维不变量空间。程序还逐类检查了四个外腿动量之和为零。

### 87.3 逐路径数据生成

新增 `build_six_labeled_orderings.py`，运行命令：

```bash
python /mnt/data/build_six_labeled_orderings.py
```

输出文件 `six_labeled_orderings_candidate_kernels.csv` 共 576 行，即 $6$ 个带标签循环类 $	imes16$ 条内部质量路径 $	imes6$ 个统一基底不变量。每行保留循环标签、顶点类型、$q_i$ 对应外腿、内部边质量、路径相关的 $\Delta_{0,\rho}$、$H_\rho,S_\rho$、回投后的 $B^{(1,2,3)}$ 和候选被积函数。此版本没有把不同路径的分母合并。

程序输出的关键检查为：

```text
PASS: six inequivalent labeled cycles generated with h1 fixed as cycle start.
PASS: momentum conservation checked for each cycle; Q-prime basis transformed to base Q basis.
PASS: generated 576 rows = 6 cycles x 16 internal paths x 6 base invariants.
```

CSV 的 SHA-256：`f0cad821910f4d257909ec6b48c647d73c21a31e96a52eae0582f5f6ceb16655`。

### 87.4 解释边界与发现

1. 六类映射已从显式带标签动量构造，而不是把原来的固定路由结果机械乘以 2 或 4。
2. 变换矩阵的非退化性与动量守恒通过程序断言；候选 $B$ 核仍继承第 84 节的条件性假设。
3. 六类序列中的顶点矩阵按每个标签的 $h/s$ 类型重新排列；内部态路径的 $u_r,v_r$ 和边质量随顶点次序重新生成。
4. 仍未完成从完整原始 Minkowski Dirac 迹独立推导每个带标签循环类的动量分子。因此这 576 行是候选核在统一外动量基底中的逐路径映射，不是完整四点振幅，更不是最终 Wilson 系数。
5. 还未加入费米子行列式整体因子与圈反向的独立核算，亦未计算 EFT 图、反项或 UV–EFT 差值。

### 87.5 下一步

下一步不应立即对 576 行作物理求和。先选一个带标签循环类和一条非平凡内部路径，用显式 $4\times4$ Dirac 矩阵与符号外动量，直接展开

$$
\operatorname{tr}_D\left[\Gamma_{X_1}(\slashed k_1+m_1)\Gamma_{X_2}(\slashed k_2+m_2)\Gamma_{X_3}(\slashed k_3+m_3)\Gamma_{X_4}(\slashed k_4+m_4)\right]
$$

到外动量二阶，并逐项与 $H,C_{ij},M$ 及 $f,g,d$ 核对。该独立迹检查通过后，再对六类的候选核进行积分和组合因子审计，最后才开始 EFT 图与反项相减。

## 第 88 节：一个非平凡带标签路径的精确符号 Dirac 迹核验

第 87 节已建立六类外腿的动量映射，但尚未独立验证路径分子。为避免一次性处理过大的全模型表达式，本节选取一个明确的非平凡测试对象：带标签循环类 $h_1h_2s_1s_2$（顶点序列 $hhss$），内部态路径 $(1,2,1,2)$，对应传播子边质量 $(m_2,m_1,m_2,m_1)$。取满足 $c_L^2+s_L^2=c_R^2+s_R^2=1$ 的精确有理混合参数点，保留全部四动量分量为符号变量。

新增脚本 `audit_symbolic_dirac_trace_one_path.py`，运行：

```bash
python /mnt/data/audit_symbolic_dirac_trace_one_path.py
```

程序直接构造 $4\times4$ Dirac 矩阵并计算

$$
\operatorname{tr}_D\left[\Gamma_{X_1}(\slashed k_1+\mu_1)\Gamma_{X_2}(\slashed k_2+\mu_2)\Gamma_{X_3}(\slashed k_3+\mu_3)\Gamma_{X_4}(\slashed k_4+\mu_4)\right],
$$

再与含 parity-even $H,C_{ij},M$ 和 parity-odd $\epsilon$ 项的分解逐项比较。所有动量分量保持符号化；随后代入 $k_i=K+r_i-R$，再次精确检查恒等式，并显式截取外动量分量总次数不超过二次的多项式部分。

### 88.1 实际输出

```text
PASS: exact symbolic 4x4 Dirac trace equals the H/C/M decomposition plus parity-odd epsilon term.
PASS: identity remains exact after symbolic Feynman shift k_i = K + r_i - R.
Path: cycle h1-h2-s1-s2 (hhss), internal states 1-2-1-2, edge masses = [5, 2, 5, 2].
Maximum degree in loop momentum K after shift: 4.
External-component polynomial degree counts before truncation: {0: 1, 1: 12, 2: 78, 3: 256, 4: 276}.
PASS: direct trace and decomposed trace agree after retaining only external-momentum degree <= 2.
```

该测试为精确符号恒等式，不是浮点数近似。它验证所选路径在该精确有理模型参数点上，直接矩阵迹与 $H,C,M$ 加奇宇称项的分解一致；Feynman 平移后恒等式仍成立。

### 88.2 结论边界

- **已验证（局部）**：所选路径、所选精确混合参数点上的 Dirac 迹分解；符号外动量代入后仍一致；二阶外动量截断也一致。
- **尚未验证**：一般符号混合参数下的全路径恒等式；六个带标签循环类的全量 Dirac 分子；圈反向、费米子行列式总组合因子；完整 Wick 转动与积分；EFT 图、反项及 UV–EFT 相减。
- 因为这里选取的路径恰有 $H_{\rm odd}=0$，它不能单独证明 parity-odd 项在所有路径/循环类中都抵消。该项仍须在全量带标签求和中保留，直到显式证明其消失或确认目标算符不接收该贡献。

下一步应把该脚本推广为 16 条内部路径的精确/分块迹审计，并至少对两种顶点序列各选取具有非零 $H_{\rm odd}$ 的路径；只有完成奇宇称部分和全部路径分子核验后，才继续对六类候选核进行积分与整体因子审计。


## 第 89 节：三种顶点类型模式的全部内部路径 Dirac 迹审计

本节将第 88 节的单路径检查扩展到三种不同的顶点类型模式 $hhss$、$hshs$、$hssh$，每种模式枚举全部 $2^4=16$ 条内部态路径。六种带标签外腿循环序列在顶点类型层面只产生这三种模式；标签会改变外腿动量映射，但不改变 $h/s$ 顶点矩阵本身。因此，本节审计覆盖全部三种类型模式的原始 Dirac 分子恒等式，但尚未逐个代入六种路由后的外动量平移。

新增脚本 `audit_dirac_traces_all_paths_three_patterns.py`，运行：

```bash
python /mnt/data/audit_dirac_traces_all_paths_three_patterns.py
```

程序在一个满足混合角归一化条件的精确有理参数点上，使用符号 Minkowski 四动量，逐条比较直接的 $4\times4$ Dirac 矩阵迹与 $H,C_{ij},M$ 以及奇宇称 epsilon 项的解析分解。

### 89.1 实际输出

```text
PASS: 48 exact symbolic Dirac-trace identities verified (3 patterns x 16 paths).
PASS: all direct traces equal H/C/M plus parity-odd epsilon decomposition at the exact rational parameter point.
Nonzero H_odd paths: 16
```

共审计 48 条恒等式。该参数点中，$hhss$ 与 $hssh$ 各有 8 条路径的 $H_{\rm odd}\ne0$，而 $hshs$ 模式在该参数点的 16 条路径中均为零。非零路径及精确有理数值写入 `dirac_trace_all_paths_three_patterns.csv`，文件 SHA-256 为 `9c8ea7392253d12bec320b7e8f63cc817bfc30bc16810de5c3441d032ea98104`。

### 89.2 这项测试究竟证明什么

- **已验证（固定精确参数点）**：三种顶点类型模式的全部 16 条内部路径，其直接矩阵迹均等于相应的 $H/C/M+\epsilon$ 分解；这不是浮点抽样，而是符号四动量下的精确代数恒等式。
- **已验证（奇宇称覆盖）**：审计确实包含 $H_{\rm odd}\ne0$ 的路径，因此不再仅靠 $H_{\rm odd}=0$ 的路径检查 epsilon 项。
- **仍待验证**：混合角保持一般符号时的恒等式；六种带标签路由的完整 $k_i=K+r_i-R$ 代入和二阶展开；各路由分子与 $f,g,d$ 系数的逐项映射；圈反向与整体组合因子；积分、EFT 图、反项和 UV–EFT 相减。

注意，精确参数点足以检验程序是否能处理非零奇宇称结构，但不能替代一般混合参数下的证明。本节也没有证明奇宇称贡献在完整振幅求和后消失。

### 89.3 后续任务更新

下一步从“验证抽象迹分解”转向“验证实际路由后的二阶分子”：对六种带标签外腿序列逐一代入其 $r_i$，将直接 Dirac 迹与分解式都平移到 $k_i=K+r_i-R$，并比较 $K$ 次数及外动量次数不超过二阶的所有系数。随后独立计算圈反向与图组合因子，再开始 EFT 图和反项。


## 第 90 节：六种带标签路由的精确有理数点回归测试

在尝试对六种路由的全符号平移表达式逐项展开时，符号表达式增长过快，计算在本轮时限内未能完成。为避免把超时误报成通过，本节明确记录这一限制，并改用可完成的精确有理数点回归测试。该测试是数值点上的精确算术（不是浮点近似），用于检查六种外腿标签映射、Feynman 平移实现及迹分解程序之间的一致性；它不替代全符号系数证明。

新增脚本 `audit_six_routed_shifted_traces.py`，运行：

```bash
python /mnt/data/audit_six_routed_shifted_traces.py
```

对六种带标签循环序列分别采用其真实的外腿动量赋值和 $r=(0,-q_2,-q_2-q_3,q_1)$ 路由，在两个精确有理参数点上计算 $k_i=K+r_i-R$，比较直接 $4\times4$ Dirac 迹与 $H,C_{ij},M$ 加 epsilon 分解。

### 90.1 实际输出

```text
PASS: 12 exact rational routed trace evaluations passed (6 cycles x 2 points).
PASS: actual external-leg assignment and Feynman shift k_i=K+r_i-R were used in every case.
BOUNDARY: pointwise exact regression only; does not prove shifted polynomial coefficient identity, integrate the loop, determine diagram factors, perform EFT subtraction, or compute Wilson coefficients.
```

结果表为 `six_routed_shifted_trace_audit.csv`，共 12 行，SHA-256：`e09182818824a9b9327114ff149b8670e42d930bbd1d1b94bad9efc0e03d80c1`。

### 90.2 结论状态

- **已验证（回归测试）**：六种带标签路由、两组精确有理动量与 Feynman 参数点，直接迹和分解式一致。
- **未完成（符号层面）**：六种路由下的完整外动量二阶系数全符号逐项比较。直接尝试因符号表达式膨胀而超时，未产生可用证明。
- **未完成（物理匹配）**：循环方向与整体图因子、环积分、EFT 泡图/接触图/反项，以及 UV–EFT 相减。

下一步应避免一次性展开所有带标签的完整表达式；应先对单一路由按外动量次数和 $K$ 的次数分块，再将六种路由的系数表进行比较。完成前不能将当前候选核认定为最终匹配核。

## 第 91 节：非零奇宇称路径的系数级几何与 Wick 核审计

本节针对上一阶段明确的缺口，选择带标签循环 $h_1h_2s_1s_2$、顶点类型 $hhss$、内部态路径 $(1,1,1,2)$。在第 89 节使用的精确有理混合参数点上，该路径的奇宇称系数不为零，因此可检查不能由 $H_{\rm odd}=0$ 路径测试覆盖的结构。

新增脚本 `audit_one_odd_path_kernel.py`，运行：

```bash
python /mnt/data/audit_one_odd_path_kernel.py
```

日志为 `audit_one_odd_path_kernel.log`。

### 91.1 路径权重

在测试参数点上，程序得到

$$
H=\frac{117993024}{17850625},\qquad
H_{\rm odd}=\frac{96997824}{17850625},\qquad
M=\frac{107495424}{714025}.
$$

因此这条路径确实具有非零奇宇称结构，而不是退化的偶宇称特例。

### 91.2 独立几何核检查

程序从 $t_i$ 的系数向量与不变量 Gram 矩阵重新构造六个 $f_{ij,\alpha}$，再从四斜线结构

$$
G=(k_1\cdot k_2)(k_3\cdot k_4)
 -(k_1\cdot k_3)(k_2\cdot k_4)
 +(k_1\cdot k_4)(k_2\cdot k_3)
$$

显式展开 $k_i=K+t_i$。对圈动量作对称角平均，使用

$$
(K\cdot t_i)(K\cdot t_j)\longrightarrow
\frac{K^2}{d}\,t_i\cdot t_j,
$$

并丢弃奇次 $K$ 项后，独立恢复 $g_\alpha$；它与紧凑的 $f_{ij}$ 组合公式逐分量一致。另从

$$
\delta\Delta=\sum_i x_i r_i^2-R^2
$$

直接重建六个 $d_\alpha$，也与既有多项式逐项一致。

### 91.3 奇宇称项的积分

程序对四个平移后动量构成的行列式

$$
\det(k_1,k_2,k_3,k_4),\qquad k_i=K+r_i-R,
$$

进行符号展开，验证其关于平移圈动量 $K$ 的最高次数为一次，且 $K^0$ 项严格为零。原因是四个 $t_i=r_i-R$ 全部位于由三个独立外动量张成的子空间，故 $\det(t_1,t_2,t_3,t_4)=0$；多线性展开中含两个 $K$ 的项也因重复列而为零。余下项线性依赖 $K$，在平移不变的维数正规化和对称圈积分下积分为零。

这个结论说明：对当前四标量外腿、该盒图分子中的奇宇称 epsilon 结构，**其圈积分为零的理由可以由动量结构直接给出**，而不必先假设所有路径的 $H_{\rm odd}$ 相消。该论证依赖平移不变的正规化；若使用非平移不变的截断，必须另行处理路由伪项。

### 91.4 修正后的 Wick 核归约

程序再次检查修正后的分母约定和积分账本，得到候选核

$$
B^{(1)}_\alpha=H\left(-\frac23g_\alpha+2d_\alpha\right),\quad
B^{(2)}_\alpha=\frac13F_\alpha-\frac23S d_\alpha,\quad
B^{(3)}_\alpha=+\frac23M d_\alpha.
$$

这里 $F_\alpha=\sum_{i<j}C_{ij}f_{ij,\alpha}$。程序确认这些表达式与所声明的逐项 Wick 积分值代数一致。

### 91.5 结论边界与下一步

本节通过了：单条非零奇宇称路径的精确模型权重检查；六个 $f_{ij}$ 的独立 Gram 重建；四斜线 $g_\alpha$ 的显式展开与角平均；$\delta\Delta$ 的几何重建；奇宇称行列式的圈动量次数证明；以及修正 Wick 核的代数归约。

仍未完成：六种带标签循环序列的完整分子系数求和、费米子行列式整体符号和组合因子、UV 圈积分的整体归一化、EFT 泡图/接触图/反项，以及 UV–EFT 相减。因此本节强化了候选核的局部依据，但**不构成最终 Wilson 系数的证明**。

下一步应把六种带标签路由的外动量二阶系数按路由分块，并独立核算圈反向与整体图因子；随后才进入 EFT 图与反项。

## 第 92 节：六种带标签路由的 $f_{ij}$、$g_\alpha$、$d_\alpha$ 系数级几何审计

第 87 节的六路由候选表把固定路由的几何核经不变量基底变换后投影到统一基底。本节对这一操作做了独立反向核验：不先变换固定路由的结果，而是对每个带标签循环直接在公共基底 $(p_1,p_2,p_3)$ 中构造 $q_1,q_2,q_3$、传播子位移 $r_i$、Feynman 平移 $R$ 与 $t_i=r_i-R$，再从 Gram 矩阵重算全部几何系数。

新增脚本 `audit_six_route_geometry_coefficients.py`，运行：

```bash
python /mnt/data/audit_six_route_geometry_coefficients.py
```

### 92.1 核验方法

对每个循环 $c=(h_1,\ldots)$，程序直接使用该循环前三个外腿动量构造

$$
q'_\alpha=(q_1^2,q_2^2,q_3^2,q_1\cdot q_2,q_1\cdot q_3,q_2\cdot q_3)_\alpha
=T_{\alpha\beta}\,\mathcal Q_\beta,
$$

其中 $\mathcal Q=(p_1^2,p_2^2,p_3^2,p_1\cdot p_2,p_1\cdot p_3,p_2\cdot p_3)$。每条路由都直接重建六个 $f_{ij}$，再按 $d$ 维角平均重建 $g_\alpha$，并由 $\sum_i x_i r_i^2-R^2$ 重建 $d_\alpha$。最后比较直接重建值与参考路由经 $T^T$ 变换后的值。所有比较都在符号 Feynman 参数和符号 Gram 不变量下完成。

### 92.2 实际结果

```text
PASS: all six labeled cycles have exact invertible invariant transforms (determinant +1 or -1).
PASS: 288 coefficient comparisons passed: 6 cycles x (6 f_ij vectors + g + d) x 6 invariants.
PASS: direct route construction in the common p-basis matches transformed fixed-route f_ij, g_alpha, and d_alpha.
```

输出 `six_route_geometry_coefficients.csv` 共 288 行；日志为 `six_route_geometry_coefficients.log`。该检查是符号系数恒等式，不是参数点抽样。

### 92.3 结论边界

- **已验证（几何层）**：六种带标签路由的不变量基底变换、全部 $f_{ij}$、$g_\alpha$ 和 $d_\alpha$ 系数彼此一致；第 87 节的几何变换没有发现系数级错误。
- **仍待验证（振幅层）**：模型特定路径权重与每个路由的完整分子、六类的圈反向关系及整体费米子行列式组合因子。
- **仍待完成（匹配层）**：完整 UV 积分、EFT 泡图/接触图/反项以及 UV–EFT 相减。

因此，本节把“路由几何是否正确”从条件假设提升为已通过的符号审计，但没有把条件性候选 Wick 核升级为最终 Wilson 系数。

下一步应在几何已锁定的基础上，计算六个带标签循环类中每个路径的模型特定 $H,C_{ij},M$ 权重和分母，并独立核查循环方向与整体组合因子；随后开始 EFT 相减。

## 第 93 节：六个带标签循环类的路径权重账本与反向映射审计

本节执行第 92 节提出的下一步：把六个带标签循环类的全部内部态路径逐条展开为模型特定权重，不先合并不同路径的质量分母；同时用精确符号代数检查三个反向循环对之间的路径映射。

新增脚本 `build_six_cycle_path_weight_ledger.py`，运行：

```bash
python /mnt/data/build_six_cycle_path_weight_ledger.py
```

输出 `six_cycle_path_weight_ledger.csv`，每行对应一个“带标签循环类 × 内部态路径”，保留顶点类型、内部态路径、边质量顺序、$\Delta_{0,\rho}$、$H_\rho$、六个 $C_{ij}^{(\rho)}$、$S_\rho=\sum C_{ij}^{(\rho)}$ 和 $M_\rho$。

### 93.1 全部路径权重输出

实际运行结果：

```text
PASS: generated 96 exact symbolic path records = 6 labeled cycles x 16 internal paths.
PASS: each row retains H, all six C_ij, M, S, edge masses, and path-specific Delta_0.
PASS: reverse-cycle coupling/mass audit: 48 path pairs across 3 cycle-reversal pairs.
```

CSV 共 96 行，SHA-256：`569bcef38292cb8709bb7588493f5105921c4b7889f1bcb931d03446a60046e1`。这里的 96 行是权重账本记录数，不是 96 个独立 Feynman 图；它们对应 6 个外腿循环类中的 16 种内部质量路径。

### 93.2 三组反向循环对

固定 $h_1$ 为循环书写起点，反向配对为

$$
(h_1,h_2,s_1,s_2)\leftrightarrow(h_1,s_2,s_1,h_2),\\
(h_1,h_2,s_2,s_1)\leftrightarrow(h_1,s_1,s_2,h_2),\\
(h_1,s_1,h_2,s_2)\leftrightarrow(h_1,s_2,h_2,s_1).
$$

对原路径 $(a_1,a_2,a_3,a_4)$，反向路径映射取

$$
(a_1,a_2,a_3,a_4)\mapsto(a_2,a_1,a_4,a_3).
$$

逐条路径的精确符号检查确认：

- $H_\rho$ 不变；
- $M_\rho$ 不变；
- 边质量序列反序；
- $C_{ij}^{(\rho)}$ 映射到 $C_{3-i,3-j}^{(\rho')}$（指标按 $0,1,2,3$ 编号，映射后重新排序）；
- 在 Feynman 参数置换 $x_1\leftrightarrow x_4$、$x_2\leftrightarrow x_3$ 下，$\Delta_{0,\rho}$ 精确映射到反向路径的分母。

共通过 48 组路径配对检查（3 个循环反向对 × 16 条路径）。这证明模型权重与质量分母的反向映射账本内部一致；它本身还没有独立证明完整积分核在动量不变量变换后相等，后者仍须把 $f,g,d$ 和各自路由的外动量基底一起变换。

### 93.3 组合因子账本

从费米子行列式展开

$$
\Gamma_f^{(4)}=\frac{i}{4}\,\mathrm{Tr}[(D_0^{-1}V)^4]
$$

出发，对四个不同标签 $h_1,h_2,s_1,s_2$ 求四次泛函导数会产生 $4!$ 个插入顺序。迹的循环性把每四个循环旋转识别为同一循环类，故不等价循环类数为 $4!/4=6$。在这一行列式/有效作用量计数中，每个循环类的四次循环重复与显式 $1/4$ 相抵消。因此，**六类都应各自计入一次；不能在这六类之和之外再乘独立的“反向环路因子 2”**。反向循环已是六类中的三个配对。

这一结论只确定组合计数，不自动固定从有效作用量约定转换到具体 Minkowski 1PI 振幅的整体 $i$、闭费米子环符号与 Wick 后共同符号。那部分仍须与显式 Feynman 规则账本独立对照。

### 93.4 结论状态与剩余工作

- **已验证（路径权重账本）**：六类 × 16 条内部路径的 $H,C_{ij},M,\Delta_0$ 已逐条生成并保留分母。
- **已验证（反向映射层）**：三组循环反向配对的 48 条路径权重、质量次序和参数分母映射均通过精确符号检查。
- **已验证（组合计数）**：费米子行列式给出六个不等价带标签循环类；不得在六类求和外再无依据乘一个 2。
- **仍待验证（完整振幅）**：每类的完整 $f,g,d$ 分子核与反向路由一并变换后的积分等价性；Minkowski 总体 $i$ 与符号；完整参数积分。
- **仍未完成（匹配）**：EFT 泡图、接触图、反项、UV–EFT 相减、IR 抵消与最终 Wilson 系数。

下一步将选取一组反向循环对，直接对两边的完整候选参数被积函数作精确变量置换与不变量基底变换，检验积分前的逐路径等价；之后再把整体 Minkowski/Wick 因子与行列式计数合并成一张不重复计数的总账本。只有这两项关闭后，才进入 EFT 图和反项。

## 第 94 节：反向循环对的完整候选核逐系数等价性

在第 93 节已验证模型路径权重与质量分母的反向映射后，本节进一步直接比较六类候选核 CSV 中的 $\Delta_{0,\rho}$ 和 $B^{(1,2,3)}$。这一步不重新推导原始 Dirac 分子，而是检查已生成候选核在反向路径、Feynman 参数重命名和外动量不变量基底映射下是否自洽。

新增脚本 `audit_six_cycle_reverse_candidate_kernels.py`，运行：

```bash
python /mnt/data/audit_six_cycle_reverse_candidate_kernels.py
```

### 94.1 检验映射

对反向循环对使用

$$
(a_1,a_2,a_3,a_4)\mapsto(a_2,a_1,a_4,a_3),\qquad
(x_1,x_2,x_3,x_4)\mapsto(x_4,x_3,x_2,x_1).
$$

随后在统一的基准外动量不变量 $\mathcal Q=(p_1^2,p_2^2,p_3^2,p_1\cdot p_2,p_1\cdot p_3,p_2\cdot p_3)$ 下比较每个路径的 $\Delta_0$ 与六个不变量分量中的 $B^{(1)}$、$B^{(2)}$、$B^{(3)}$。化简时严格施加参数单纯形约束 $x_1+x_2+x_3+x_4=1$；不把只因单纯形约束才成立的关系误判为一般四变量恒等式。

### 94.2 实际结果

```text
PASS: 1152/1152 exact coefficient comparisons passed across 3 reverse-cycle pairs.
Compared Delta0, B1, B2, B3 for 3 reverse pairs x 16 internal paths x 6 base invariants x 4 coefficient objects.
RESULT: candidate kernels are reverse-cycle equivalent after the stated path, parameter and external-invariant mapping.
```

输出 `six_cycle_reverse_kernel_audit.csv` 共 1152 行，SHA-256：`2c349ee66484aeee6b42826cf4cac89de8e7b56cd76c96b12e8bd1822f2bb2b2`。

### 94.3 解释边界

- **已验证（候选核内部一致性）**：三组反向循环对中，所有路径、所有六个基准不变量的 $\Delta_0$ 和 $B^{(1,2,3)}$ 均在映射后逐系数一致。因此，在当前候选核中，每组反向对的两项积分可以通过变量重命名和外动量不变量变换互相对应；若积分区域为标准四参数单纯形，则参数置换的 Jacobian 绝对值为 1。
- **没有独立验证**：该测试的两侧都来自同一个候选核构造程序；它不是从原始 Minkowski Dirac 振幅独立推导两边。因此它证明的是“候选核没有在反向循环映射下自相矛盾”，而不是候选核的物理分子已被最终证明。
- **组合计数后果**：六个带标签循环类仍须各计一次。若为计算方便只显式积分三个代表循环并将每个乘 2，必须先把这里的反向核等价性、行列式的 $1/4$ 计数和全局振幅归一化合并核清楚；不能既求六类总和又额外乘 2。
- **仍未完成**：Minkowski 整体符号与 Wick 因子、所有循环类的绝对积分、EFT 泡图/接触图/反项、UV–EFT 相减与最终 Wilson 系数。

下一步将把有效作用量行列式计数与显式 Feynman 规则的 $(-1)_{\rm fermion\ loop}$、四个顶点因子、四个传播子因子和 Wick 积分账本放到同一张表中，确认共同的整体 $i$ 与符号。该总因子关闭后，才开始实际参数积分与 EFT 相减。

## 第 95 节：用 Mathematica / FeynCalc 独立完成 UV–EFT 一圈匹配的逐步操作手册

本节的目标不是把现有 Python 结果简单搬到 Mathematica，而是建立一条**可复现、可分块、能与现有计算交叉核对**的独立计算路线。读者应能按本节顺序安装软件、建立 notebook、复现一个简单 Dirac 迹、从原始顶点构造一条内部路径、做外动量展开、执行圈积分约化，并最终为 UV 与 EFT 两侧的匹配准备统一的数据结构。

> **重要边界：** Mathematica/FeynCalc 可以自动化符号代数，但不会替研究者决定模型的费曼规则、整体符号、算符基底、重整化方案或 EFT 中必须包含哪些图。本节中的代码是分阶段的工作模板；涉及模型特定的顶点矩阵、质量本征态旋转和整体归一化时，必须用本项目实际约定填入并单独审计。任何模板跑通都不等于 Wilson 系数已经得到。

### 95.1 软件选择与分工

建议按“先最小化安装、后按需扩展”的顺序操作：

1. **Mathematica / Wolfram Language**：符号表达式、矩阵、参数展开、精确有理数、文件输出和自动化测试的主环境。
2. **FeynCalc**：Dirac 代数、Lorentz 指标、迹、张量积分相关操作和圈积分表达式的辅助处理。优先安装稳定版本，先只用这一套包建立基准案例。
3. **FeynArts**：需要自动生成拓扑、费曼图和检查外腿排列时再安装。它不会自动理解未编码的自定义模型；自定义模型文件仍需正确提供。
4. **Package-X**：在一圈积分已化为其支持的标准形式后，辅助解析计算维数正规化的一圈积分。不要假定任意未展开的四传播子分母都能直接交给它。
5. **FORM**：当符号表达式过大，Mathematica 的内存或化简时间成为瓶颈时再考虑。它不是入门阶段的必要依赖。
6. **FeynRules**：如果要从拉格朗日量系统导出费曼规则、并与其他工具衔接，可以后续加入；当前项目可先手工编码顶点并做独立校验。

官方入口（安装步骤和函数接口可能随版本变化，执行前应查看对应版本文档）：

- FeynCalc 主页与安装：<https://feyncalc.github.io/>；安装手册：<https://feyncalc.github.io/FeynCalcBookDev/Extra/Install.html>。
- FeynArts：<https://feynarts.de/>。
- Package-X 论文：<https://arxiv.org/abs/1612.00009>；入门材料可从 Package-X 项目页面和作者 primer 查阅。
- FORM：<https://github.com/form-dev/form>。
- FeynRules：<https://cp3.irmp.ucl.ac.be/projects/feynrules>。

### 95.2 建立项目目录和版本记录

不要把所有计算放在一个巨大的 notebook 里。建议在本机建立如下目录（Windows 可把 `/` 换成合适路径；Mathematica 也可用 `FileNameJoin`）：

```text
UV_EFT_MMA/
  README.md
  notebooks/
    00_environment_test.nb
    01_dirac_trace_smoke_test.nb
    02_model_and_vertices.nb
    03_one_path_raw_numerator.nb
    04_routing_and_feynman_parameters.nb
    05_external_momentum_expansion.nb
    06_loop_integrals.nb
    07_six_cycles.nb
    08_EFT_amplitude.nb
    09_matching_and_operator_projection.nb
  src/
    model_parameters.wl
    vertex_matrices.wl
    routing.wl
    trace_helpers.wl
    integral_helpers.wl
  output/
    logs/
    csv/
    expressions/
  archive/
```

每个 notebook 开头都记录：日期、Mathematica 版本、FeynCalc 版本、使用的度规、外动量流向、传播子约定、重整化方案、运行输入和输出文件名。每次得到重要结果后保存 `.nb` 和纯文本 `.wl`/`.txt`；对可复现的表达式同时导出 CSV 或 Wolfram Language `InputForm`，并计算 SHA-256。不要只保存 notebook 的漂亮排版结果，因为它可能隐藏未求值表达式或依赖当前内核状态。

可在 Mathematica 中执行：

```wl
$Version
$SystemID
$UserBaseDirectory
$Path
```

这四个结果用于确认软件版本、操作系统和包搜索路径。

### 95.3 安装 FeynCalc：逐步执行

#### 95.3.1 在线安装

1. 启动 Mathematica 桌面版，新建 notebook。
2. 确认 Mathematica 可以访问 GitHub；若学校/机构网络屏蔽相关地址，优先使用官方手动安装方式，不要从不明镜像下载代码。
3. 在一个新的输入单元中执行官方主页当前给出的安装命令。官方常见流程是先载入安装脚本，再执行安装函数：

```wl
Import["https://raw.githubusercontent.com/FeynCalc/feyncalc/master/install.m"]
InstallFeynCalc[]
```

4. 如果安装器询问是否安装 FeynArts，可先选择不安装；当前第一目标是完成 FeynCalc 的单路径迹计算。
5. 等待安装结束，关闭并重新启动 Mathematica，避免旧内核中残留的包定义。
6. 新建 notebook，执行：

```wl
$FeynCalcStartupMessages = False;
<< FeynCalc`
```

7. 测试包是否加载：

```wl
Names["FeynCalc`DiracTrace"]
Names["FeynCalc`FCI"]
```

如果返回空列表或出现 `Get::noopen`，不要继续做物理计算；先修复安装或 `$Path`。

**安全提醒：** `Import` 会下载并执行远程安装脚本。只应从 FeynCalc 官方主页/官方仓库获取；若不希望直接执行网络代码，按官方手册下载压缩包并手动放入 `$UserBaseDirectory/Applications`。

#### 95.3.2 手动安装（在线安装失败时）

1. 打开官方安装手册，下载稳定版压缩包。
2. 在 Mathematica 中查看 `$UserBaseDirectory`，并确认 `FileNameJoin[{$UserBaseDirectory,"Applications"}]` 对应的目录。
3. 将解压后的 `FeynCalc` 目录放入该 `Applications` 目录。
4. 重新启动 Mathematica。
5. 执行 `<< FeynCalc`` 并运行本节 95.4 的测试。
6. 若仍无法加载，检查目录是否多套了一层，例如出现 `Applications/FeynCalc-master/FeynCalc.m` 而不是预期的 `Applications/FeynCalc/FeynCalc.m`；具体结构以当前版本安装手册为准。

### 95.4 第一项基准测试：先验证 Dirac 迹，不碰模型

先运行最小测试，以确认 FeynCalc 能计算简单迹。新建 `01_dirac_trace_smoke_test.nb`，执行：

```wl
$FeynCalcStartupMessages = False;
<< FeynCalc`

(* 一个简单的四维 Dirac 迹基准：Tr[gamma^mu gamma^nu] = 4 g^{mu nu} *)
trTest = DiracTrace[GA[mu] . GA[nu]];
trResult = DiracSimplify[trTest];

{trTest, trResult}
```

检查输出是否与 FeynCalc 当前版本的标准表示一致，并与恒等式

\[
\mathrm{Tr}(\gamma^\mu\gamma^\nu)=4g^{\mu\nu}
\]
一致。FeynCalc 的内部表示与普通 Mathematica 表达式不同，结果可能显示为 `Pair[...]` 等对象；不要仅因输出形式不同就认为错误。必要时查看 `?DiracTrace`、`?DiracSimplify`、`?GA` 的当前版本帮助。

接着测试一个带动量的迹：

```wl
Clear[p, q];
trPQ = DiracSimplify[DiracTrace[GS[p] . GS[q]]];
trPQ
```

应得到与 \(4p\cdot q\) 对应的 FeynCalc 内部表示。这个测试确认“迹计算接口可用”，并不涉及 \(\gamma_5\)、维数正规化或本模型顶点。

**验收条件：** 只有简单迹测试通过、输出能解释并且 notebook 已保存，才进入下一节。若不通过，记录完整错误信息、版本号和输入单元，不要继续把后续失败归因于物理模型。

### 95.5 固定本项目的约定：先写在 notebook 顶部

在 `02_model_and_vertices.nb` 的第一节写一张约定表。当前项目至少使用以下约定（若主文档后续修改，以最终审计后的统一约定为准）：

- Minkowski 度规：\((+---)\)。
- 传播子分母：\((k+r_i)^2-m_i^2+i0\)。
- Feynman 参数：\(x_i\ge0\)，\(\sum_i x_i=1\)。
- 平移变量：\(K=k+R\)，\(R=\sum_i x_i r_i\)。
- \(\Delta_0=\sum_i x_i m_i^2\)。
- \(\delta\Delta=\sum_i x_i r_i^2-R^2\)。
- 平移后的 Minkowski 分母：\(K_M^2-\Delta_0+\delta\Delta+i0\)。
- Wick 后 Euclidean 分母：\(K_E^2+\Delta_0-\delta\Delta\)。
- 六个外动量不变量按固定顺序保存：\((p_1^2,p_2^2,p_3^2,p_1\cdot p_2,p_1\cdot p_3,p_2\cdot p_3)\)。
- 四参数单纯形体积是 \(1/6\)；如果改成归一化平均，只允许在定义处乘一次 6。

建议将它们写成注释和一个独立的 `conventions` Association，不要靠记忆或不同 notebook 之间的隐含假设。

```wl
conventions = <|
  "Metric" -> "+---",
  "PropagatorDenominator" -> "(k+r_i)^2-m_i^2+i0",
  "FeynmanParameters" -> {x1, x2, x3, x4},
  "SimplexConstraint" -> x1 + x2 + x3 + x4 == 1,
  "Delta0" -> Sum[x[i] m[i]^2, {i, 1, 4}],
  "LoopMomentumShift" -> "K = k + Sum[x_i r_i]",
  "ExternalInvariantOrder" -> {p1^2, p2^2, p3^2, p1.p2, p1.p3, p2.p3}
|>;
```

这段 Association 只是保存元数据；它不会自动让 Mathematica 理解四动量或度规。实际计算仍须使用一致的符号表示和替换规则。

### 95.6 把 UV 模型编码成独立的数据层

当前 UV 相互作用包含

\[
\mathcal L_{UV}\supset -y_\mu\bar L_\mu H E_{\mu R}
-\lambda_\mu S\bar E_{\mu L}\mu_R
-M_E\bar E_{\mu L}E_{\mu R}+\mathrm{h.c.}
\]

质量矩阵为

\[
\mathcal M=\begin{pmatrix}0&m_L\\m_R&M_E\end{pmatrix},
\]

重质量极限下 \(m\simeq m_Lm_R/M_E\)、\(s_L\simeq m_L/M_E\)、\(s_R\simeq m_R/M_E\)。质量本征态的顶点矩阵应从已审计的旋转约定得到，而不能把某个近似混合矩阵随意当作精确矩阵。

操作步骤：

1. 在 `model_parameters.wl` 中定义符号参数，不要一开始代入小数：

```wl
Clear[yMu, lambdaMu, ME, mL, mR, sL, cL, sR, cR, a, b];
$Assumptions = Element[{yMu, lambdaMu, ME, mL, mR}, Reals] && ME > 0;
```

2. 在 `vertex_matrices.wl` 中按主文档给出的已确认约定录入矩阵：

\[
Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix}.
\]

```wl
Yh = a {{cL sR, cL cR}, {sL sR, sL cR}};
Ys = b {{sL cR, -sL sR}, {-cL cR, cL sR}};
```

3. 做矩阵维度、符号和近似阶数检查：

```wl
Dimensions /@ {Yh, Ys}
Det[Yh] // Factor
Det[Ys] // Factor
```

4. 若使用 \(c_L^2+s_L^2=1\)、\(c_R^2+s_R^2=1\)，把它们作为明确的替换规则或假设；不要让 `FullSimplify` 在没有这些假设时偷偷使用三角关系。
5. 把“精确旋转矩阵”和“重质量展开后的近似矩阵”分开存储，并在变量名中注明 `Exact` 或 `HeavyLimit`。
6. 逐一检查每个顶点的场种类、手征投影、共轭顶点和内部费米子态指标。矩阵元素的数值形式本身不能证明费曼规则中的整体 \(i\) 与负号正确。

### 95.7 Dirac 顶点编码：不要先把手征结构压扁

对于标量 Yukawa 顶点，通常会出现 \(P_L=(1-\gamma_5)/2\)、\(P_R=(1+\gamma_5)/2\)。但**具体是 \(Y P_L+Y^*P_R\) 还是其他排列，取决于拉格朗日量、外线方向和费米子流向**。本项目必须从原始拉格朗日量及其 Hermitian conjugate 推导，而不能只凭记忆录入。

推荐做法：

1. 先在纸面上对单个相互作用项写出费曼规则，明确场流入/流出和复共轭。
2. 为每种外标量分别定义一个“顶点矩阵生成函数”，输入内部态标签后返回相应的 Yukawa 元素与 Dirac 结构。
3. 在 notebook 中把“耦合常数/内部态矩阵元素”和“Dirac 矩阵部分”分开保存。
4. 对一个简单的两顶点或单路径极限做手算检查，确认共轭、手征投影和质量项没有互换。
5. 若采用四维 \(\gamma_5\) 迹，显式注明这一选择；若涉及 UV 极点并需在 \(D=4-2\epsilon\) 中处理，应重新检查所用 \(\gamma_5\) 方案和软件支持范围。不能把四维迹结果无条件当成全维数正规化的结果。

FeynCalc 相关函数的名称与用法应以当前安装版本文档为准。可在 notebook 中执行 `?GA`、`?GS`、`?DiracTrace`、`?DiracSimplify` 查看接口；常见内部表示包括 `GA[mu]`（伽马矩阵）和 `GS[p]`（与四动量收缩的 slash）。

### 95.8 从单条路径开始，不要一口气展开全部 96 条记录

先固定一个带标签循环序列，例如 \((h_1,h_2,s_1,s_2)\)，并选一条内部态路径 \((a_1,a_2,a_3,a_4)\)。把每条边的内部质量记为 \(m_i\)，每个顶点的内部态矩阵元记为 \(V_i\)。原始分子结构应从下式的实际顶点矩阵构造：

\[
N(k)=\mathrm{Tr}\!\left[V_1(\slashed k+\slashed r_1+m_1)
V_2(\slashed k+\slashed r_2+m_2)
V_3(\slashed k+\slashed r_3+m_3)
V_4(\slashed k+\slashed r_4+m_4)\right].
\]

此式是结构模板；真正实现时必须把每个 \(V_i\) 替换为模型对应的手征矩阵，并确认分子传播子顺序和分母路由一致。

#### 95.8.1 推荐的调试次序

1. 先不做 Feynman 参数化，只构造一个路径的原始迹。
2. 先不代入重质量近似，保持质量和混合参数符号化。
3. 用 `DiracTrace` 和 `DiracSimplify` 计算迹。
4. 对结果按圈动量 \(k\) 的次数分类，分别保留 \(k^0,k^1,k^2,k^3,k^4\) 等部分。
5. 对简单随机有理参数点做数值比较，但数值点只用于发现错误，不能替代符号证明。
6. 对同一路径用第二种独立表达方式（例如手动展开投影算符后计算，或与已有 Python 脚本比较）验证。
7. 只有单路径通过后，才自动遍历 16 条内部路径；只有单个循环类通过后，才遍历六个循环类。

#### 95.8.2 分块而不是整体展开

表达式过大时，避免立即执行对所有符号的 `Expand` 或 `FullSimplify`。推荐先按圈动量次数、质量次数、耦合常数单项式和外动量阶数分组。每一块分别保存、简化和比较。需要时用 `Coefficient`、`Collect` 或规则匹配提取指定变量的系数，但应先确认表达式已被表示成相应变量的多项式；若分母含这些变量，先明确要做的是级数展开还是有理函数分解。

### 95.9 路由与 Feynman 参数：符号映射要显式写出

当前固定路由之一为

\[
r_1=0,\quad r_2=-q_2,\quad r_3=-q_2-q_3,\quad r_4=q_1.
\]

它只是一个带标签路由，不应不加变换就复制给所有外腿排列。每一种循环顺序都需要单独建立：

- 四个顶点的标签顺序；
- 四个传播子的动量偏移 \(r_i\)；
- 内部质量序列 \(m_i\)；
- 外动量守恒关系；
- 从该路由基底到公共基底 \((p_1,p_2,p_3)\) 的线性变换。

对分母

\[
\prod_{i=1}^4[(k+r_i)^2-m_i^2+i0]^{-1}
\]

引入 \(x_i\) 后定义

\[
R=\sum_i x_i r_i,\quad
\Delta_0=\sum_i x_i m_i^2,\quad
\delta\Delta=\sum_i x_i r_i^2-R^2.
\]

必须按当前审计后的约定得到

\[
K_M^2-\Delta_0+\delta\Delta+i0,
\qquad K=k+R,
\]

Wick 后对应

\[
K_E^2+\Delta_0-\delta\Delta.
\]

因此在小外动量展开中

\[
(K_E^2+\Delta_0-\delta\Delta)^{-n}
=(K_E^2+\Delta_0)^{-n}
+n\,\delta\Delta(K_E^2+\Delta_0)^{-n-1}+O(p^4).
\]

这里 \(\delta\Delta=O(p^2)\)，所以保留到外动量二阶时只取一次线性项。旧版本中若写成欧氏分母的 `+ deltaDelta`，必须标记为旧错误，不得复制进新 notebook。

实现时建议将每种路由的 \(r_i\) 作为四维向量系数表，使用一个统一函数从表格自动计算 \(R,\Delta_0,\delta\Delta\)，并用精确代数检查：

1. \(R\) 是否与手算一致；
2. \(\Delta_0\) 是否不依赖外动量；
3. \(\delta\Delta\) 是否从二阶外动量开始；
4. 反向循环的参数置换是否将分母映射到对应路径；
5. 参数单纯形约束 \(\sum_i x_i=1\) 是在何处施加的。

不要把 \(x_4=1-x_1-x_2-x_3\) 提前代入所有中间表达式而不留原始四参数版本；保留两种表示便于追踪变量置换和单纯形关系。

### 95.10 外动量二阶展开：建立六个不变量的固定基底

对于四点标量振幅，在动量守恒后可用三个独立外动量，例如 \(p_1,p_2,p_3\)，构造六个二阶不变量：

\[
\mathcal Q=(p_1^2,p_2^2,p_3^2,p_1\cdot p_2,p_1\cdot p_3,p_2\cdot p_3).
\]

执行顺序：

1. 在每个循环序列内部，先用动量守恒消去 \(p_4\)，但保留一份未消元表达式作核对。
2. 把所有路由偏移写成 \(p_1,p_2,p_3\) 的线性组合。
3. 展开分子中外动量的次数至二阶；分母的外动量依赖则通过 \(\delta\Delta\) 的一致展开处理。
4. 将所有二阶项收集到上述六个不变量中，输出六个系数。
5. 对每种循环顺序分别完成该过程，再通过显式线性变换映射到公共基底。
6. 用零外动量极限、交换两个相同外标量的对称性以及反向循环映射做检查。

不能只检查最终表达式在一个随机点数值相等。至少要保留一份精确符号系数表，并检查所有六个系数。若 `FullSimplify` 不能证明等价，先确认是否遗漏了动量守恒关系、参数单纯形约束或外动量置换，而不是立即认定两式不同。

### 95.11 圈动量积分与 Wick 符号：单独维护积分账本

把分子先写成圈动量张量的线性组合，例如

\[
N(K,p)=N_0(p)+N_{1\mu}(p)K^\mu+N_{2\mu\nu}(p)K^\mu K^\nu+\cdots.
\]

在平移不变的维数正规化下，奇次圈动量积分通常因对称性为零；偶次张量积分需按 Lorentz/Euclidean 对称性约化。但这不意味着可以先删掉所有奇次项：必须先确认分母已通过平移化为只依赖 \(K^2\)，并且所用正则化允许该平移。

当前审计中使用的 Wick 记账规则为

\[
J_{M,r}^{(n)}=i(-1)^{n+r}I_{E,r}^{(n)},
\]

其中 \(r\) 表示分子中 \((K_M^2)^r\) 的幂次、\(n\) 表示对应分母幂次；使用前必须核对 \(J\) 与 \(I\) 的具体定义是否包含传播子分母的整体符号、测度因子和归一化常数。**不能把这个相对符号公式直接当成完整振幅的全局符号。**

建议在 `06_loop_integrals.nb` 中制作一张逐项表格，每行记录：

- 分子张量类型与圈动量次数；
- Minkowski 分母幂次；
- Wick 后来自测度的 \(i\)；
- 每个 \(K_M^2\to-K_E^2\) 引入的符号；
- 分母整体变换引入的符号；
- 欧氏积分的标准归一化；
- 是否含 Feynman 参数化的 \(\Gamma(n)\) 因子；
- 是否含四参数单纯形积分体积 \(1/6\)；
- 最终共同因子与该项相对因子。

用一个最简单的标量测试积分先验证测度和分母符号，再把规则应用于实际分子。显式 Feynman 图规则（闭费米子环的 \(-1\)、四个顶点因子、四个传播子因子）与有效作用量行列式展开必须分开计算后再对照。行列式展开的六循环计数已经吸收了循环旋转与显式 \(1/4\) 的关系；不可在六循环总和之外再机械乘一个 2。

### 95.12 Feynman 参数积分：先约化，再集成

四个分母的 Feynman 参数化常见结构包含 \(\Gamma(4)\) 和参数单纯形积分。具体系数取决于你把 \(1/(D_1D_2D_3D_4)\) 写成哪种标准公式、圈积分是否已包含 \(i\pi^{D/2}\) 或 \((2\pi)^{-D}\) 因子。不要只抄一个公式而忽略它的归一化约定。

建议分成两个层次：

**层次 A：先保持参数积分形式。** 将所有六个循环、16 条内部路径的结果整理成含 \(\Delta_0\)、\(\delta\Delta\)、模型耦合权重与六个外动量不变量系数的统一被积函数。此阶段先检查对称性和参数映射，不急于强行积分。

**层次 B：再进行参数积分。** 对 UV 极点和有限项分开处理，明确维数 \(D=4-2\epsilon\)、重整化尺度 \(\mu\) 和 \(\overline{\mathrm{MS}}\) 定义。先选一条路径或一个简化质量极限测试积分，再推广到完整求和。若积分不能解析完成，可保留可复现的参数积分表达式并数值验证；不要用数值拟合替代需要的 UV 极点解析系数。

Package-X 应用于已转成它支持的标准一圈积分表达式时更稳妥。若它不接受当前四传播子结构，按外动量展开后把结果化成标准标量/张量积分，或者直接保留 Feynman 参数积分。FeynCalc 和 Package-X 的输出格式不同，连接两者时应记录转换规则和版本。

### 95.13 FeynArts 何时加入

只有当手工建立的单路径振幅和整体因子已经稳定，才建议加入 FeynArts。其主要用途是从模型和外腿定义生成图、检查拓扑和反项图，而不是替代模型验证。

步骤：

1. 从官方页面安装 FeynArts，或在 FeynCalc 安装流程中选择安装其兼容版本。
2. 在一个独立测试模型中先生成最简单的树图，确认包可加载。
3. 再建立当前模型的粒子类别、混合费米子、标量和相互作用顶点。
4. 对每一种顶点检查粒子/反粒子、质量本征态和共轭规则。
5. 生成四标量外腿的 1PI 拓扑，并与手工枚举的六种带标签循环序列逐一对照。
6. 特别确认自动生成器的外腿排列、对称因子和费米子流向，与本项目采用的行列式展开计数一致。
7. 将 FeynArts 输出的振幅转换到 FeynCalc 可处理的表达式后，再与手工原始迹比较。

在模型文件没有经过检查之前，FeynArts 没生成某张图不能证明该图物理上不存在；它可能只是模型顶点或粒子类别没有正确编码。

### 95.14 EFT 侧：必须独立计算，不能只从 UV 结果反推

EFT 维数五相互作用为

\[
\mathcal L_5=-\frac{c_\mu}{\Lambda}S\bar L_\mu H\mu_R
-\frac{c_\tau}{\Lambda}S^\dagger\bar L_\tau H\tau_R+\mathrm{h.c.}
\]

在 EFT 侧，必须按照相同外腿、相同外动量路由和相同正则化方案，独立列出相关的泡图、接触图、反项图以及由算符插入产生的图。对每张图记录：耦合常数、图因子、内部质量、传播子分母、UV/IR 极点和所需反项。

匹配的核心是同一低能展开阶次下的

\[
\mathcal A_{\mathrm{match}}=\mathcal A_{UV}^{\mathrm{ren}}-\mathcal A_{EFT}^{\mathrm{ren}},
\]

而不是简单把 UV 的有限部分称作 Wilson 系数。两边必须使用相同的 IR 处理、相同的外态归一化和一致的算符基底；IR 敏感项应在匹配差中按理论预期抵消。若没有显式计算 EFT 图与反项，就不能宣称匹配已完成。

### 95.15 统一输出格式：让每个结果都能追溯

建议每条路径至少输出以下字段：

```text
cycle_label
internal_path
vertex_coupling_product
internal_mass_sequence
routing_id
r1, r2, r3, r4
Delta0
DeltaDelta
raw_trace_expression
trace_after_simplification
coefficient_of_each_external_invariant
Minkowski_prefactor
Wick_relative_sign
Euclidean_integrand
UV_pole
finite_part
EFT_subtraction_status
verification_status
notes
```

对每个重要中间结果同时保存：

- 原始未简化表达式；
- 简化后的表达式；
- 运行脚本或 notebook 单元；
- Mathematica 与包版本；
- 输入文件 SHA-256；
- 输出文件 SHA-256；
- 断言通过数/总数；
- 断言实际检验的数学命题；
- 没有检验的物理问题。

“程序通过”只能说明已编码断言通过。必须写清楚它是否验证了原始模型分子、是否包含所有循环、是否包括整体因子、是否计算了 EFT 图和反项。

### 95.16 建议的实际执行顺序与停止条件

按以下顺序执行，每一步都有明确的停止条件。若当前步骤未通过，不要跳到下一步：

#### 第 1 步：环境

- 安装 Mathematica 并记录版本。
- 安装稳定版 FeynCalc。
- 运行简单两伽马矩阵迹测试。
- 保存 `00_environment_test.nb` 和 `01_dirac_trace_smoke_test.nb`。
- **停止条件：** 包加载和简单迹测试均通过。

#### 第 2 步：模型顶点

- 将原始拉格朗日量、质量矩阵、混合旋转、质量本征态顶点写入 notebook。
- 明确每个顶点的手征结构、复共轭和费米子流向。
- 精确检查矩阵维度、混合矩阵正交性/幺正性和重质量展开阶数。
- **停止条件：** 顶点规则能逐项回溯到拉格朗日量，并有独立手算检查。

#### 第 3 步：单路径原始分子

- 选定一个循环序列和一条内部路径。
- 从实际顶点矩阵构造四传播子原始迹。
- 用 FeynCalc 计算并按圈动量次数分块。
- 与 Python 脚本或手算结果逐项比较。
- **停止条件：** 分子逐项一致；若只有数值点一致，仍不算通过。

#### 第 4 步：路由和参数化

- 对该路径建立 \(r_i\)、\(R\)、\(\Delta_0\)、\(\delta\Delta\)。
- 核对 Minkowski 平移后的分母和 Wick 后 Euclidean 分母。
- 验证参数置换与反向循环映射。
- **停止条件：** 所有分母符号、路由和参数约束一致。

#### 第 5 步：低动量展开

- 对分子和分母分别按正确规则展开到外动量二阶。
- 收集六个不变量的系数。
- 检查零动量极限、动量守恒和循环反向关系。
- **停止条件：** 六个系数都有可复现的符号表达式，且映射测试通过。

#### 第 6 步：圈积分和全局因子

- 先用一个标量测试积分校准 Wick 变换和归一化。
- 独立计算显式 Feynman 图因子和行列式展开因子。
- 对照 Feynman 参数公式中的 \(\Gamma\) 因子、\((2\pi)^D\)、\(i\) 和单纯形体积。
- **停止条件：** 有一张无重复计数的整体因子表，且每个符号都有来源。

#### 第 7 步：六个循环与所有内部路径

- 自动遍历六种带标签循环序列和 16 条内部态路径。
- 不要在已求和六循环之外再乘额外环反向因子 2。
- 先做精确代数测试，再做数值点回归测试。
- **停止条件：** 96 条路径权重、路由、分母、分子和系数记录完整；反向映射通过。

#### 第 8 步：EFT 图和反项

- 独立列出 EFT 泡图、接触图和必要反项。
- 使用相同正则化与低能展开计算。
- **停止条件：** UV 与 EFT 两边的图集完整，且每个发散项都有对应解释。

#### 第 9 步：匹配与算符投影

- 计算 UV 与 EFT 的重整化振幅之差。
- 验证 IR 项抵消，整理 UV 极点和有限部分。
- 用明确的算符基底与运动学投影矩阵求 Wilson 系数。
- 用第二个独立运动学结构或独立振幅交叉检查。
- **停止条件：** 系数对约定、方案和阶次的依赖均已记录，独立检查通过。

### 95.17 常见失败模式与排错表

| 现象 | 常见原因 | 排查方式 |
|---|---|---|
| `Get::noopen` 或找不到 FeynCalc | 包安装路径错误、内核未重启 | 检查 `$UserBaseDirectory`、`$Path` 和实际目录结构 |
| `DiracTrace` 没有化简 | 表达式仍是普通符号或 FeynCalc 内部形式不匹配 | 先确认 `<< FeynCalc`` 已执行，再查看 `?DiracTrace` 与内部表示教程 |
| `FullSimplify` 卡住 | 同时展开全部路径、质量和动量变量导致表达式膨胀 | 单路径、按圈动量次数和外动量次数分块；使用精确有理参数做测试 |
| 两个路由结果看似不同 | 外动量基底或 Feynman 参数未同步置换 | 显式构造路由变换矩阵并施加参数单纯形约束 |
| Wick 后符号不一致 | 混淆分子 \(K^2\)、分母幂次、测度 \(i\) 或整体振幅因子 | 先用独立标量积分校准，再逐项记账 |
| UV 极点不匹配 | UV 与 EFT 的 IR 处理、重整化方案或图集不一致 | 对每张图单独标记 UV/IR 极点，核查反项和匹配差 |
| Mathematica 与 Python 数值一致但符号不同 | 特殊数值点掩盖代数差异，或缺少约束 | 检查精确系数、多项式恒等式、动量守恒和参数单纯形约束 |
| 软件给出结果但无法解释 | 使用了黑箱函数或丢失归一化信息 | 保存原始振幅、函数输入、函数输出和包版本；逐层验证 |

### 95.18 最终验收清单

在声称得到 Wilson 系数之前，必须逐项勾选：

- [ ] 模型费曼规则从原始拉格朗日量独立推导并核验。
- [ ] 至少一个单路径原始 Dirac 分子由 FeynCalc 独立复算。
- [ ] 其余路径由同一规则自动生成，且抽样与完整结构检查通过。
- [ ] 六个带标签循环序列都已包含一次，组合因子无重复。
- [ ] 每条路由的质量次序、动量偏移、参数分母均明确。
- [ ] Minkowski 到 Euclidean 的分母符号与 Wick 因子独立校准。
- [ ] 四参数 Feynman 参数化的 \(\Gamma\) 因子和单纯形归一化无重复。
- [ ] UV 图、EFT 图、接触图和反项图集完整。
- [ ] UV 与 EFT 使用同一重整化方案并完成低能展开相减。
- [ ] IR 项按预期抵消，UV 极点与反项一致。
- [ ] 结果已投影到明确定义的算符基底。
- [ ] 至少有一个独立的解析/数值/运动学极限交叉检查。
- [ ] 文档记录了所有未解决假设、软件版本、输入输出与校验和。

只要任何一项未完成，就应把结果标为“条件成立”或“待验证”，而不是最终 Wilson 系数。

### 95.19 本节结论

最有效的路线不是把全部计算一次性交给 Mathematica，而是让 Mathematica/FeynCalc 从一个最小、可手工核验的 Dirac 迹开始，逐步接管符号迹、路由代数、外动量展开和部分积分约化。FeynArts 用于图与拓扑交叉检查，Package-X 用于它支持的标准一圈积分，FORM 则留给表达式规模过大的阶段。

对当前项目，下一项可执行任务应是：安装并验证 FeynCalc，然后在 `03_one_path_raw_numerator.nb` 中复现一条非零路径的原始四顶点 Dirac 迹。此结果必须在不把候选 $B^{(1,2,3)}$ 当作输入的前提下，与现有 Python 分块迹结果比较。只有原始分子这一关通过后，才继续路由、参数积分、全局因子以及 EFT 相减。


## 第 96 节：直接使用 FeynCalc 计算一圈图——从原始振幅到 UV–EFT 匹配的执行手册

本节在第 95 节 Mathematica/FeynCalc 总体路线基础上，专门回答“能不能直接用 FeynCalc 计算圈图”，并给出可按顺序执行的操作流程。官方手册说明：FeynCalc 使用 `FAD` / `FeynAmpDenominator` 表示传播子分母，`TID` 用于一圈张量积分约化；旧接口 `OneLoop` 已弃用，应优先采用 `TID` 工作流。参考：

- FeynCalc 一圈积分：<https://feyncalc.github.io/FeynCalcBookDev/OneLoop.html>
- FeynCalc loop objects 与 `TID`：<https://feyncalc.github.io/FeynCalcBookDev/Loops.html>
- `FAD`：<https://feyncalc.github.io/FeynCalcBook/FAD.html>
- `FeynAmpDenominatorExplicit` 的警告：<https://feyncalc.github.io/FeynCalcBook/FeynAmpDenominatorExplicit.html>

### 96.1 本节目标与边界

目标是让 FeynCalc 从**原始费曼振幅**出发，计算 Dirac 分子并处理圈积分，而不是把先前的候选核 $B^{(1,2,3)}$ 作为输入。计算按单路径、单循环开始，通过后才扩展到 6 个带标签循环类 × 16 条内部路径。

FeynCalc 能做的主要工作：

1. Dirac 代数与迹；
2. Lorentz 指标和标量积化简；
3. 将圈积分的传播子分母保存在正确的积分对象中；
4. 对适用的一圈张量积分使用 `TID` 约化为标量积分/Passarino–Veltman 系数；
5. 与其他 Mathematica 代数操作配合进行外动量展开、系数收集和结果导出。

它不会自动替研究者决定：完整模型的顶点约定、六循环是否重复计数、正确的 UV/EFT 图集、红外方案、反项、算符基底或最终 Wilson 系数。那些必须作为明确输入并独立审计。

### 96.2 最简工作流

建议严格按下面顺序推进，不要一开始就把 96 条路径全部交给 `FullSimplify`。

1. 安装 Mathematica 与 FeynCalc，重启内核，加载包并保存版本信息。
2. 跑一个只有两传播子的标准积分测试，确认 `FAD` 和 `TID` 正常工作。
3. 跑一个四传播子、无 Dirac 分子的标量积分对象测试，确认传播子路由与质量输入正确。
4. 对一条指定内部路径，从实际四个 Yukawa 顶点构造原始 Dirac 迹。
5. 在**保持圈动量积分对象**的情况下，把迹乘上四个 `FAD` 分母；先化简分子，不要先把分母展开成普通分式。
6. 先单独对分子做圈动量次数与外动量次数整理，再选择 `TID` 约化或 Feynman 参数化路线。
7. 与现有 Python 分块迹结果逐项比较；不一致就停止，先定位顶点、路径、动量路由或维数约定。
8. 单路径通过后，自动扩展至 16 条路径；再扩展至 6 个带标签循环类。
9. 统一全局费曼因子与 Wick 约定后，计算 EFT 振幅、接触图和反项。
10. 最后才做 UV–EFT 相减、IR 抵消检查和 Wilson 系数投影。

### 96.3 第一次启动：记录软件版本并运行最小测试

新建 `00_environment_test.wl`，将以下内容放进去并在 Mathematica 中运行：

```mathematica
(* 00_environment_test.wl *)
$HistoryLength = 20;
Get["FeynCalc`"];

Print["Mathematica version = ", $Version];
Print["FeynCalc directory = ", $FeynCalcDirectory];

Clear[q, p, m0, m1];
scalarBubble = FAD[{q, m0}, {q + p, m1}];
Print["Input bubble denominator:"];
Print[scalarBubble // FCE // StandardForm];

bubbleReduced = TID[scalarBubble, q];
Print["TID result:"];
Print[bubbleReduced // StandardForm];
```

检查：

- `Get["FeynCalc`"]` 不报错；
- `$FeynCalcDirectory` 返回安装目录；
- `FAD` 结果包含 $(q^2-m_0^2)^{-1}$ 与 $((q+p)^2-m_1^2)^{-1}$；
- `TID` 给出合法的约化结果（可能含标准标量积分或 PV 系数）。

这一步只验证包与接口，不是模型振幅，也不能据此声称已完成 UV–EFT 计算。保存输出到日志或 notebook。

### 96.4 四传播子分母：先保留正确的积分表示

本模型每条路径的分母结构可抽象写为

\[
D(k)=\prod_{j=1}^{4}\frac{1}{(k+r_j)^2-m_j^2+i0}.
\]

FeynCalc 中的基础输入模板如下：

```mathematica
(* 01_four_denominators.wl *)
Get["FeynCalc`"];
Clear[k, r2, r3, r4, m1, m2, m3, m4];

fourDen = FAD[
  {k, m1},
  {k + r2, m2},
  {k + r3, m3},
  {k + r4, m4}
];

fourDen // FCE // StandardForm
```

这里 `r2`、`r3`、`r4` 是动量表达式的占位符，实际计算时必须替换为相应外动量线性组合；它们不是可以任意选择的独立物理动量。应按当前循环序列逐条传播子记录真实的 $r_j$ 和 $m_j$。

**重要警告：** 不要在执行圈积分约化之前，对完整积分调用 `FeynAmpDenominatorExplicit`。官方手册明确警告：这会把特殊分母对象变成普通代数分母；圈积分函数可能因此不再识别这些分母为圈积分，并把积分错误地当作无分母/无尺度对象。只有在需要做树级代数或明确的非积分代数操作时，才考虑显式展开分母。

### 96.5 构造原始 Dirac 分子：禁止把候选核当输入

对给定路径 $a=(a_1,a_2,a_3,a_4)$，先按质量本征态顶点规则构造四个实际矩阵 $\Gamma_1,\ldots,\Gamma_4$。四个传播子分子是

\[
(\slashed{k}+m_1),\quad
(\slashed{k}+\slashed r_2+m_2),\quad
(\slashed{k}+\slashed r_3+m_3),\quad
(\slashed{k}+\slashed r_4+m_4).
\]
FeynCalc 原始迹的代码骨架：

```mathematica
(* 02_one_path_raw_trace.wl *)
Get["FeynCalc`"];
Clear[k, r2, r3, r4, m1, m2, m3, m4];

(* 必须把下面四个占位符替换成由模型和路径实际导出的顶点矩阵。 *)
(* V1 = ...; V2 = ...; V3 = ...; V4 = ...; *)

rawTrace = DiracTrace[
  V1 . (GSD[k] + m1) .
  V2 . (GSD[k + r2] + m2) .
  V3 . (GSD[k + r3] + m3) .
  V4 . (GSD[k + r4] + m4)
];

traceReduced = DiracSimplify[rawTrace];
traceReduced // StandardForm
```

这是**模板而不是可直接给出模型答案的完整脚本**：`V1`–`V4` 必须先由原始拉格朗日量、手征投影、质量本征态混合矩阵和指定路径生成。不能将它们直接替换成候选 $B^{(1,2,3)}$，也不能漏掉复共轭顶点的耦合常数。不同顶点若包含 $P_L/P_R$ 或复标量的共轭方向，必须分别编码。

推荐先将一个顶点矩阵单独打印出来，检查其手征投影与混合参数，再构造完整迹。若使用 $\gamma_5$，必须明确四维/维数正规化处理方案；不要在没有声明方案时把四维 Levi-Civita 恒等式随意推广到 $D=4-2\epsilon$。

### 96.6 把分子和传播子组合成一圈积分对象

确认 `traceReduced` 结构正确后，构造单路径的积分表达式：

```mathematica
rawLoopIntegrand = traceReduced * fourDen;
rawLoopIntegrand // FCE // StandardForm
```

此对象是“分子 × 四个传播子分母”的积分核，**仍未自动包含所有物理费曼因子**。不要把闭费米子环的 $-1$、四个顶点的 $(-i)$、传播子的 $i$、耦合常数、外腿排列数或积分测度误认为 `FAD` 自动处理的部分。把它们单独记在全局因子账本中，避免重复乘入或漏掉。

此处先执行下列局部审计：

1. 分子中是否正好有四个传播子分子；
2. 每个传播子的质量是否与对应内部态一致；
3. 每个 $r_j$ 是否与该循环的动量路由一致；
4. 顶点顺序是否与费米子流方向一致；
5. `FAD` 是否保留四个二次分母；
6. 是否在使用 FeynCalc 前就把分母错误地展开成普通分式。

### 96.7 先约化还是先低能展开？

本项目的目标是低能局部 Wilson 系数，而非任意外动量下的完整四点函数。对含四个不同质量传播子的四点一圈积分，完整 Passarino–Veltman 表达式可能很大；在质量和外动量结构复杂时，直接 `TID` 不一定是最省时路线。因此建议分成两个分支，并用最简单路径做对照：

#### 路线 A：先用 `TID` 做积分约化测试

```mathematica
(* 对一个已构造、已正确编码的测试积分核运行。 *)
(* tidResult = TID[rawLoopIntegrand, k]; *)
```

将注释行中的 `rawLoopIntegrand` 换成实际变量后再运行。检查输出是否含预期的标量积分/PV 系数，并确认 FeynCalc 仍识别传播子分母。若输出巨大、超时或引入难以控制的运动学分母，保留日志，不要强行对全表达式 `FullSimplify`；转路线 B。

#### 路线 B：先做 Feynman 参数化与低能展开

对本项目已建立的分母平移记号，定义

\[
R=\sum_i x_i r_i,\qquad \Delta_0=\sum_i x_i m_i^2,
\qquad \delta\Delta=\sum_i x_i r_i^2-R^2,
\]

并使用

\[
\frac{1}{D_1D_2D_3D_4}=\Gamma(4)\int_{x_i\ge0}\!\prod_i dx_i\,
\delta\!\left(1-\sum_i x_i\right)\frac{1}{[\sum_i x_iD_i]^4}
\]

的四分母参数化结构。随后将 $k$ 平移为 $K=k+R$，在 Minkowski 空间先核对分母，再执行 Wick 变换。按已审计的约定，平移后的 Minkowski 分母写成 $K_M^2-\Delta_0+\delta\Delta$，Wick 后 Euclidean 分母为 $K_E^2+\Delta_0-\delta\Delta$。展开符号必须和分母定义同步，不能把旧的 Euclidean $+\delta\Delta$ 写法重新引入。

这一路线通常更适合抽取低阶局部项，但 FeynCalc 不会自动替你决定应保留哪些外动量阶数，也不会替你确认此前候选分子分解正确。应将分子展开与分母展开分开保存，并与原始表达式做阶数截断核验。

### 96.8 低外动量展开的执行纪律

对目标算符的导数阶数先写清楚。当前目标是外动量二阶项时：

1. 为外动量建立独立的形式变量，不要一开始代入数值；
2. 先用动量守恒消去一个外动量，但保留映射记录；
3. 将分子按圈动量次数 $K^r$ 与外动量次数分组；
4. 将分母展开到能够贡献目标阶数的阶次；
5. 对每一项分别做张量积分/角平均；
6. 只保留目标阶数，按六个独立不变量收集系数；
7. 检查更高阶项确实被截断，而不是在化简过程中意外丢失目标项；
8. 对一组精确有理参数点做回归测试，但数值点测试只能作为补充，不能代替符号恒等式。

建议先对一个非零奇宇称路径与一个普通偶宇称路径分别做基准测试。若两者都通过，再扩展到 16 条路径。由于表达式膨胀，避免一次性对全部 96 条路径调用 `FullSimplify`。

### 96.9 `TID` 的适用范围与四传播子限制

`TID[expr, k]` 是 FeynCalc 的一圈张量积分约化接口。它可将许多积分化为标准标量积分或 PV 系数，但这不等于所有四点积分都会自动化成简单初等函数。具体可约化程度取决于：

- 分母拓扑是否被 FeynCalc 识别；
- 外动量与标量积是否已正确声明；
- 质量是否相同、是否存在无尺度子积分；
- 目标是否需要完整动量依赖还是只需低能展开；
- 是否需要额外的 IBP 工具处理更一般的积分族。

若 `TID` 返回 PV 系数，先保存该结果并检查其约定；若无法处理或表达式过大，优先对低能展开后的积分项分别处理，或转到本项目已有的 Feynman 参数积分路线。不要把一次 `TID` 成功运行等同于 UV 极点、有限项和最终 Wilson 系数均已算对。

### 96.10 全局费曼因子与积分归一化账本

为每张图单独建表，至少记录：

| 项目 | 必须记录的内容 |
|---|---|
| 闭费米子环 | 是否包含 $-1$，采用何种费曼规则约定 |
| 四个顶点 | 每个 $i$ 因子、耦合常数、共轭方向与顶点顺序 |
| 四个传播子 | 每条传播子的 $i$ 因子、分子与 $i0$ 约定 |
| 积分测度 | $d^Dk/(2\pi)^D$ 或其他约定 |
| 行列式展开 | $i/4\,\mathrm{Tr}[(D_0^{-1}V)^4]$ 的定义与顶点矩阵定义 |
| Wick 变换 | $d^4K_M=i\,d^4K_E$、$K_M^2\to-K_E^2$ 及各分子项符号 |
| Feynman 参数 | $\Gamma(4)$、参数单纯形体积与是否采用归一化平均 |
| 六循环求和 | 6 个带标签循环类各计一次；不得再无依据乘 2 |

显式费曼图计算与费米子行列式展开必须最终相互一致，但不能在没有把 $D_0$、$V$ 与费曼规则逐项对齐前，仅凭“闭环 $-1$、四顶点和四传播子”就宣布整体符号已经解决。整体 $i$ 的位置也可能随“有效作用量系数”与“1PI 振幅”的定义不同而变化。

### 96.11 与 Python 审计结果逐项比较

FeynCalc 独立结果应与现有 Python 审计的相同对象比较，而不是只比较最终数字。建议每条基准路径输出以下列：

- 循环类名称与内部态路径 $(a_1,a_2,a_3,a_4)$；
- 原始 Dirac 迹；
- 按圈动量次数分组后的系数；
- 外动量不变量系数；
- 分母质量序列与动量偏移序列；
- Wick 前后分母表达式；
- Feynman 参数核与参数约束；
- 软件版本、执行时间、警告与失败信息。

比较时先统一符号、度规、$D$ 维约定、动量路由和参数映射，再执行 `Together`/`Cancel` 等代数等价检查。若只在数值代入后相等，结果只能标记为“数值点通过”；若精确符号比较通过，才可标记为相应代数层面的通过。

### 96.12 扩展到全部路径与六个循环类

扩展顺序必须是：

1. 一个循环类的一条路径；
2. 同一循环类的 16 条内部路径；
3. 一个反向循环对的映射检查；
4. 六个带标签循环类全部 96 条路径；
5. 完整外腿排列求和；
6. 整体因子和 Wick 符号独立审计。

循环序列以第 87、93、94 节记录为准。反向映射需同时变换顶点顺序、内部路径、质量序列、传播子偏移、Feynman 参数和外动量不变量。不能只反转顶点名称而保持其余数据不变。

### 96.13 EFT 振幅与匹配：软件算完 UV 图后还差什么

完成 UV 图的低能展开后，仍必须在相同的规范、IR 处理、维数正规化与重整化约定下独立计算 EFT：

1. 列出 EFT 中同外腿、同量子数、同阶数的全部图；
2. 包含由低维相互作用插入产生的泡图、接触图及其他必要贡献；
3. 计算所需反项并明确 $\overline{\mathrm{MS}}$ 或其他方案；
4. 分别记录 UV 与 EFT 的 UV/IR 极点，检查红外结构按预期抵消；
5. 做 $\mathcal A_{\mathrm{UV}}-\mathcal A_{\mathrm{EFT}}$ 的低能匹配；
6. 将结果投影到明确定义、去冗余后的算符基底；
7. 用独立运动学结构或另一个振幅核对 Wilson 系数。

FeynCalc 可帮助处理 EFT 图的代数与积分，但不会自动知道你的 EFT 拉格朗日量里有哪些反项，也不会自动替你完成算符基底选择。

### 96.14 验收清单与停止条件

只有以下各项全部满足，才允许报告最终 Wilson 系数：

- [ ] FeynCalc 版本和输入文件已保存；
- [ ] `FAD` + `TID` 的最小测试通过；
- [ ] 四传播子质量和路由逐条核对；
- [ ] 一条路径的原始 Dirac 迹由实际顶点独立生成；
- [ ] 原始迹与 Python 分块迹符号比较通过；
- [ ] 低能展开顺序、阶数与六个不变量定义明确；
- [ ] Wick 符号、积分测度和参数化因子独立核对；
- [ ] 六个循环类与 16 条路径无漏计、无重复；
- [ ] UV 图、EFT 图、接触图和反项完整；
- [ ] IR 极点按预期抵消，UV 极点与反项一致；
- [ ] Wilson 系数已投影到明确算符基底；
- [ ] 至少一项独立解析/符号/运动学检查通过。

若任一项未完成，结论应标为“待验证”或“在列明假设下成立”。

### 96.15 本节最终建议

对当前项目，最短而稳健的执行路径是：

**FeynCalc 原始迹 → 单路径四分母积分核 → 低能展开/积分约化 → 与 Python 比较 → 全部路径和循环求和 → 全局因子审计 → EFT 图与反项 → UV–EFT 相减 → Wilson 系数投影。**

暂时不需要 FeynRules；当你想自动生成模型费曼规则、系统检查图拓扑时，再加入 FeynArts/FeynRules。Package-X 可在积分已经化成其支持的一圈标准形式时辅助求解析积分。不要把这些包当成自动决定物理约定的黑箱。


## 第 97 节：加入 FeynRules + FeynArts 的自动建模与圈图生成路线

本节补充一条比“手动逐项输入每个顶点和传播子”更自动化的工作流：**FeynRules 建模/导出 → FeynArts 生成拓扑并插入场 → FeynCalc 化简振幅和处理圈积分 → 独立 EFT 振幅与反项 → 匹配**。这是一条可逐步实现的自动化路线，但不是不经检查就能一键得到正确 Wilson 系数的黑箱。

### 97.1 先理解每个包负责什么

| 工具 | 负责的工作 | 不会自动替你决定的内容 |
|---|---|---|
| Mathematica | 运行环境、符号变量、批处理与结果导出 | 物理模型和匹配约定 |
| FeynRules | 从拉格朗日量生成费曼规则；将模型导出为受支持的格式 | 模型是否完整、场约定是否正确、目标 EFT 算符基底 |
| FeynArts | 生成指定圈数与外腿的图拓扑，插入模型场并构造振幅表达式 | 图是否符合你真正要匹配的外腿/耦合阶数；是否遗漏反项或重复计数 |
| FeynCalc | 转换/化简振幅、Dirac 与 Lorentz 代数、张量圈积分约化等 | 自动修复错误的模型文件、自动确定整体符号、自动完成所有 EFT 相减 |
| Package-X（可选） | 对其支持的一圈标准积分进行解析求值 | 任意形式的完整匹配流程 |

对当前模型而言，如果你已经确信质量本征态顶点规则且只想算一张已知图，直接 FeynCalc 通常更短。如果你希望软件系统地产生图、检查排列和将来扩展更多相互作用，再加 FeynRules/FeynArts 才更值得。

### 97.2 适用当前模型的推荐策略

模型的核心 UV 相互作用为

\[
\mathcal L_{UV}\supset -y_\mu\bar L_\mu H E_{\mu R}
-\lambda_\mu S\bar E_{\mu L}\mu_R
-M_E\bar E_{\mu L}E_{\mu R}+\mathrm{h.c.}
+(D_\nu S)^\dagger D^\nu S-V(S).
\]

质量矩阵、混合矩阵和质量本征态 Yukawa 顶点已在前文给出。建模时必须先明确：

1. 场是四分量 Dirac 费米子、Weyl 费米子还是 FeynRules 的两分量表示；
2. $S$ 是复标量，$S^\dagger$ 是独立共轭场，还是先在对称破缺后改用实标量分量；
3. 输入的是规范/相互作用本征态拉格朗日量，还是已经对角化的质量本征态拉格朗日量；
4. 外腿 $h_1,h_2,s_1,s_2$ 的场方向、共轭关系、动量流入约定；
5. 模型是否需要规范相互作用、Goldstone、ghost 或其他粒子。若目标振幅只涉及 Yukawa 四点闭费米子环，可以建立最小模型，但不得把可能贡献到同一目标算符的其他相互作用无依据地删掉。

**强烈建议先建立最小质量本征态模型作为第一版。** 这样可以先检验 FeynArts 是否生成预期的四 Yukawa 顶点费米子环。等该模型的图数、耦合乘积和简单极限都与手工拓扑清单一致后，再决定是否扩展成完整规范本征态模型。不要把同一套自由度的相互作用本征态与质量本征态费米子同时放入模型，否则可能双重计数。

### 97.3 安装与版本记录

1. 安装可运行的 Mathematica。
2. 按 FeynRules 官方安装说明安装 FeynRules，并记录版本号。
3. 安装 FeynArts，并确认 Mathematica 的 `$Path` 能找到其目录。
4. 安装 FeynCalc，并确认 `<< FeynCalc`` 能正常加载。
5. 如果使用 FeynRules 导出的 FeynArts 模型文件，确认该文件放在 FeynArts 能找到的模型目录中，或在调用时明确指定模型路径。
6. 将版本和路径写入项目记录，避免升级后结果发生难以追踪的变化。

官方入口：

- FeynRules：<https://cp3.irmp.ucl.ac.be/projects/feynrules>
- FeynArts：<https://feynarts.de/>
- FeynCalc：<https://feyncalc.github.io/>
- FeynCalc 安装手册：<https://feyncalc.github.io/FeynCalcBookDev/Extra/Install.html>

建议在新建的 Mathematica notebook 中分别运行并记录：

```mathematica
$Version
```

```mathematica
<< FeynArts`
```

```mathematica
<< FeynCalc`
```

FeynRules 常见安装方式会使用其包目录下的主入口文件；具体加载语句应以你下载版本的 README/安装文档为准。不要把网络文章中某个旧版本的路径硬编码后就认为安装成功。

### 97.4 第一步：写 FeynRules 模型文件

FeynRules 模型通常由粒子定义文件和拉格朗日量文件组成。不同版本的模板语法、粒子类定义和导出选项可能不同，先复制与你安装版本匹配的官方最小模型示例，再替换成自己的字段和参数，不建议从空文件开始猜语法。

#### 97.4.1 参数和粒子定义

至少要在模型文件中定义：

- 轻费米子与重费米子的场名、反粒子名、旋量类型、质量参数；
- 复标量 $S$ 及其共轭场；
- Higgs/外部标量 $H$ 或所需的质量本征态标量分量；
- $M_E,y_\mu,\lambda_\mu$ 以及混合角/矩阵元素；
- 所需的电荷、色表示和规范量子数；若只研究最小 Yukawa 子模型，仍要确认模型定义不会让 FeynRules 错误地把不同场识别为同一粒子。

如果采用质量本征态模型，顶点应与前文的 $Y_h,Y_s$ 矩阵一致。要将矩阵元素落实为 FeynRules 能识别的具体三点耦合，而不是仅把一整个矩阵写在说明文字中。检查共轭顶点的复共轭、费米子流向和左/右手投影。

#### 97.4.2 拉格朗日量输入与规则生成

将动能项、质量项和所需 Yukawa 项组成模型拉格朗日量。使用你安装版本的 FeynRules 语法载入模型并调用费曼规则推导函数。随后先查看输出的三点顶点：

- $h\bar\psi_i\psi_j$ 顶点的手征结构；
- $s\bar\psi_i\psi_j$ 与 $s^\dagger\bar\psi_i\psi_j$ 的方向区别；
- 质量对角项与非对角项是否正确；
- 共轭顶点是否使用了复共轭耦合；
- 是否意外产生不应存在的顶点。

不要在尚未通过这项检查时直接生成一圈图。若软件生成的顶点与前文 Yukawa 矩阵不一致，应先纠正模型文件，而不是在圈图结果里事后补符号。

### 97.5 第二步：将 FeynRules 模型导出给 FeynArts

使用当前安装版本 FeynRules 文档中的 FeynArts 导出函数（通常称为 `WriteFeynArtsOutput`）导出模型文件。函数选项会随版本变化，因此应从该版本文档/示例复制准确调用形式；不要盲目照抄不同版本的参数。

导出后检查生成文件是否包含：

- 粒子及反粒子声明；
- 质量与宽度参数；
- 三点 Yukawa 顶点；
- 需要的共轭和非对角顶点；
- 与本次计算无关的相互作用是否被有意排除；
- 文件名和模型名是否与后续 FeynArts 调用完全一致。

若导出模型中漏了 $s^\dagger$ 顶点或把复标量错误地当作实标量，后续生成的图即使能成功运行，也不代表物理模型正确。

### 97.6 第三步：用 FeynArts 生成四外腿一圈拓扑

FeynArts 的典型流程是 `CreateTopologies` → `InsertFields` → `CreateFeynAmp`。下面是**工作流骨架**；模型名、外腿粒子名、场类编号和排除规则必须替换为你导出模型里的真实名称，且需按安装版本核对选项：

```mathematica
<< FeynArts`

(* 1. 生成 1-loop、4 外腿的拓扑 *)
top = CreateTopologies[1, 4 -> 4];

(* 2. 将外腿插入为实际场。
   下方 In/Out 与 FieldClass 编号仅作占位示意，
   必须替换成模型中真实的粒子名称/场类。 *)
ins = InsertFields[
  top,
  {(* incoming external fields *)} -> {(* outgoing external fields *)},
  Model -> "YourExportedModel"
];

(* 3. 生成振幅表达式 *)
ampFA = CreateFeynAmp[ins];
```

注意：上面的外腿列表故意没有写成可直接运行的具体粒子名，因为当前模型的 FeynRules/FeynArts 场名和场类编号尚未在这段通用手册中确定。请从模型文件实际声明中填写。对于你要的 $h_1,h_2,s_1,s_2$ 振幅，需把四个外腿分别映射为正确的粒子/反粒子方向，并明确 FeynArts 的 incoming/outgoing 约定。

#### 97.6.1 生成图后先做拓扑审计

先不要马上进行积分。逐图导出或查看：

1. 图中是否恰好有四个目标 Yukawa 顶点；
2. 内部线是否是预期的轻/重费米子质量本征态；
3. 每张图的顶点顺序是否属于前文定义的六个带标签循环类；
4. 是否包含非目标拓扑，例如由标量传播子、规范相互作用或其他顶点产生的图；
5. 是否有同一物理图因外腿标签/对称因子而重复或遗漏；
6. 是否应包含反项图。反项通常需要单独定义和插入，不能假定 FeynArts 自动知道匹配方案。

FeynArts 的 `CreateTopologies[1, 4 -> 4]` 会生成广泛的四点一圈拓扑，不会自动只保留你想要的“四 Yukawa 顶点闭费米子环”。应使用适当的拓扑/场插入限制，并在结果中逐图筛选与核对。若软件版本支持特定过滤选项，先用官方示例验证该选项的含义。

### 97.7 第四步：生成振幅并转给 FeynCalc

在 FeynArts 端获得振幅后，通常可使用 FeynCalc 的 `FCFAConvert` 转换为 FeynCalc 表达式。不同版本在选项名称和外腿动量处理上可能不同，先按安装版本文档运行官方示例。

通用骨架如下：

```mathematica
<< FeynCalc`

(* ampFA 是 CreateFeynAmp 的结果；
   具体 IncomingMomenta、OutgoingMomenta、LoopMomenta、
   UndoChiralSplittings 等选项需依实际振幅与版本设置。 *)
ampFC = FCFAConvert[
  ampFA,
  IncomingMomenta -> {p1, p2},
  OutgoingMomenta -> {p3, p4},
  LoopMomenta -> {q},
  ChangeDimension -> D,
  List -> True,
  SMP -> True
];
```

这段是接口骨架而不是已针对本模型验证过的成品代码。要特别核对：

- FeynArts 的动量方向是否与 FeynCalc 转换后的分母一致；
- 外腿是否都按约定进入振幅，是否存在动量守恒替换；
- 手征分裂是否改变了费米子链的排列；
- 传播子分子与 $i$ 因子是否保留/移除得符合所选振幅约定；
- 内部质量参数是否正确映射；
- 转换后是否产生预期的四个传播子分母。

转成 FeynCalc 后，先对单张图执行 Dirac 化简和圈积分约化，再扩展到全图集。不要一开始对所有图执行高强度 `FullSimplify`，否则既慢，也不容易定位是哪张图造成表达式膨胀。

### 97.8 直接圈积分的两种分支

#### 分支 A：直接约化圈积分

若转换后的分子和分母适合 FeynCalc 约化，可先化简 Dirac 链，再对圈动量执行 `TID`。这条路线适合把结果表示为标准标量积分/Passarino–Veltman 系数。四传播子情形可能得到四点函数及其张量系数；若输出很大或遇到未约化对象，应记录具体失败表达式，改用分阶展开或参数化路线。

#### 分支 B：先做低能展开，再参数积分

对于局部 Wilson 系数，通常只需要外动量低阶的局部项。可先从原始振幅做一致的外动量展开，再约化所得积分；或者先合并分母、平移动量，再展开参数核。这两种顺序需要在红外安全的条件下比较。若 EFT 中有相同低能区域产生的 IR 项，不可简单把 UV 图的某一项单独展开后就宣称完成匹配。

当前项目已有手工构造的路径权重、分母和候选核。它们适合用于对照与诊断，但不能作为 FeynRules/FeynArts 生成的原始振幅的定义来源。正确的独立验证顺序是：从拉格朗日量生成顶点 → 从图生成振幅 → FeynCalc 计算原始分子 → 再与已有候选核比较。

### 97.9 如何避免“自动生成了图，但图不对”

为每张目标图建立机器可读的审计表，至少包括：

- 图的唯一标识和拓扑；
- 外腿标签与流入/流出方向；
- 四个顶点的场内容与耦合；
- 内部费米子质量序列；
- 对应的六循环类标签；
- FeynArts 对称因子/图权重；
- 闭费米子环负号在所用振幅接口中是否已计入；
- 转换到 FeynCalc 后的传播子数与动量偏移；
- 该图是否已包含、是否应排除，以及排除理由。

不能因为 FeynArts 生成了六张图就直接把它们认作前文六个循环类：图拓扑计数与固定外腿标签下的顶点循环顺序不是同一个概念。需要把生成图中的场序列映射到第 87、93、94 节的六类循环及内部态路径账本。

### 97.10 质量本征态模型与相互作用本征态模型：先选一个，不要混用

本项目已有质量矩阵与质量本征态 Yukawa 矩阵。实现上有两种选项：

**方案 A：质量本征态直接建模（推荐作为首个原型）**

- 把质量项写成对角形式；
- 把 $h$ 与 $s/s^\dagger$ 顶点直接编码为前文给出的质量本征态耦合；
- 内部线由 FeynArts 直接使用本征态质量；
- 用单个四 Yukawa 顶点闭费米子环测试顶点矩阵与路径求和。

优点是与当前路径权重表一一对应，便于验证。缺点是混合矩阵关系是手动编码进去的，FeynRules 不会自动替你证明质量对角化和耦合矩阵都正确。

**方案 B：从相互作用本征态拉格朗日量建模**

- 输入非对角质量矩阵和原始 Yukawa 相互作用；
- 明确对角化变换及左右混合矩阵；
- 根据 FeynRules 对旋量场变换的支持程度，手动执行或显式编码旋转；
- 检查旋转后的质量项和所有耦合与前文 $Y_h,Y_s$ 一致；
- 再导出 FeynArts 模型。

该方案更贴近 UV 拉格朗日量，但更容易因左右手旋转、复共轭和场重定义而引入错误。除非你确实要自动研究不同参数点下的混合结构，否则先做方案 A 更快。

### 97.11 反项与 EFT：FeynArts/FeynRules 不能代替匹配定义

FeynRules/FeynArts 能帮助处理已定义模型中的相互作用和图，但不会凭空生成你需要的 EFT 算符基底或决定重整化方案。若需要一圈反项图，必须把相应反项参数和顶点加入模型，或以明确的解析方式单独计算。

EFT 侧要单独建立相应模型，生成与 UV 相同外腿、相同规范/红外结构和匹配阶数的图。逐项核对：

1. UV 与 EFT 是否使用相同外腿归一化、动量方向和 $i\epsilon$；
2. 两侧是否采用相同的维数正规化与尺度约定；
3. IR 极点是否按预期一致并在匹配差中抵消；
4. UV 极点是否由相应反项吸收；
5. 最终局部多项式是否投影到无冗余的目标算符基底；
6. 是否存在 EOM、分部积分或场重定义导致的算符等价。

### 97.12 最简可执行里程碑

按下列里程碑推进，每一步通过后再做下一步：

- [ ] **M0 环境**：FeynRules、FeynArts、FeynCalc 均能加载，记录版本。
- [ ] **M1 顶点**：FeynRules 输出的质量本征态 Yukawa 顶点与 $Y_h,Y_s$ 逐项一致。
- [ ] **M2 导出**：FeynRules 导出的 FeynArts 模型可成功加载，粒子/反粒子与复标量共轭正确。
- [ ] **M3 拓扑**：FeynArts 能生成四点一圈拓扑，并能筛出目标闭费米子环。
- [ ] **M4 单图振幅**：只选一张图，生成振幅并通过 `FCFAConvert` 转换。
- [ ] **M5 原始分子**：FeynCalc 得到的分子与手工/现有 Python 原始迹在统一约定后逐项一致。
- [ ] **M6 单路径积分**：四传播子分母、质量序列和动量路由一致；完成低能展开或张量约化。
- [ ] **M7 图集**：生成图与六循环/16 路径账本完成映射，无遗漏、无重复。
- [ ] **M8 总因子**：独立核对闭环符号、图权重、顶点与传播子 $i$ 因子、积分测度、Wick 符号。
- [ ] **M9 EFT**：EFT 图和反项完整，UV/IR 极点结构一致。
- [ ] **M10 匹配**：UV–EFT 相减并投影到指定算符基底，独立复核 Wilson 系数。

如果 M1–M5 失败，停止扩展图集，先修模型文件或振幅转换。若 M6 的 `TID` 不便直接处理四点函数，则切换到第 96 节的低能展开/Feynman 参数路线，而不是把未约化输出当成错误答案。

### 97.13 常见故障及处理

| 现象 | 可能原因 | 处理方式 |
|---|---|---|
| FeynRules 不识别字段/拉格朗日量 | 模型语法与版本不匹配 | 从该版本官方最小模型复制，逐项增加字段和相互作用 |
| 导出后 FeynArts 找不到模型 | 模型目录或名称不正确 | 检查导出文件路径、`$ModelPath`/安装路径及调用中的模型名 |
| 生成图为零张或数量异常 | 外腿场类/共轭方向错误、筛选条件过严 | 先放宽筛选，用最小模型确认外腿插入，再逐项增加限制 |
| 出现大量无关拓扑 | `CreateTopologies` 生成范围太宽 | 先按拓扑和场内容筛选；不要把所有四点图都当目标图 |
| `FCFAConvert` 报错或输出不完整 | 选项与版本不匹配、未正确设置动量/手征处理 | 对照该版本官方示例，先转换最小的单图振幅 |
| FeynCalc 输出中分母数量不对 | 动量流向、模型传播子或转换选项不一致 | 对照 FeynArts 原图逐个检查传播子动量和质量 |
| 同一图似乎出现两次 | 外腿标签、共轭图或图对称因子理解错误 | 建立图标识与循环类映射表，逐图审计，不能随意除以 2 |
| 整体符号与手工计算不同 | 闭环负号、顶点约定、传播子 $i$ 因子或振幅定义不同 | 按第 96.10 节的因子账本逐项追踪，不做整体猜号 |
| 圈积分化简极慢 | 过早对所有图统一展开/`FullSimplify` | 先单图、先迹、再按外动量阶数分块，必要时改用参数积分 |

### 97.14 本节结论

对当前项目，建议采用**双路线交叉验证**：

- **短路线**：直接 FeynCalc 输入实际顶点与传播子，独立计算单路径原始振幅和积分核；
- **自动建模路线**：FeynRules 生成规则，FeynArts 生成图，FeynCalc 转换和约化振幅。

先让两条路线在同一张图、同一条内部态路径上得到相同的原始分子和分母，再逐步扩展到完整图集。这样 FeynRules/FeynArts 的价值在于自动化图和模型 bookkeeping，FeynCalc 的价值在于符号代数与圈积分处理，而物理上的整体符号、低能展开、EFT 反项、IR 抵消和 Wilson 系数定义仍必须显式验证。

## 第 98 节：FeynRules + FeynArts 路线的逐步执行清单与最小验收标准

本节将第 97 节的方案进一步改写成可以照着执行的操作清单。推荐顺序是先用最小模型跑通软件链，再逐项加入当前 UV 模型；不要第一次就把全部混合、复标量、所有图和 EFT 反项同时塞进模型文件。

### 98.1 先固定工作目录和版本记录

在 Mathematica 中建立独立项目目录，例如 `UV_EFT_FeynCalc_Project`，至少建立以下子目录：

```text
UV_EFT_FeynCalc_Project/
  model/          # FeynRules 模型文件、参数定义
  generated/      # 导出的 FeynArts 模型文件
  notebooks/      # Mathematica notebook 或 .wl 脚本
  amplitudes/     # 原始振幅与转换后的振幅
  results/        # 展开系数、日志、CSV
  checks/         # 与 Python/手算结果的差分检查
```

记录 Mathematica、FeynRules、FeynArts、FeynCalc 的版本号、加载路径、操作系统和运行日期。软件升级后先重跑最小测试，不要把不同版本生成的模型文件混用。

验收标准：新建一个干净的 Mathematica kernel 后，能重复加载所需软件；所有输出写到项目目录，而不是散落在默认工作目录。

### 98.2 从最小 FeynRules 模型开始

1. 先复制当前安装版本附带的最小可运行模型作为模板，不要凭记忆编写全部模型语法。
2. 定义场的自旋、质量、宽度、粒子/反粒子关系、规范量子数和参数符号。
3. 先只保留一组简单 Yukawa 相互作用，验证费曼规则导出；成功后再增加重费米子 $E$、复标量 $S$、Higgs 场以及轻重费米子混合。
4. 把质量本征态约定写在模型文件注释中，明确左右手混合角、质量本征态排序和场的相位。
5. 检查复标量 $S$ 与 $S^\dagger$ 是否被当作正确的共轭场；检查每个 Yukawa 项是否满足规范量子数守恒。
6. 让 FeynRules 输出顶点列表，并逐项与拉格朗日量求导得到的费曼规则比较，尤其检查顶点的 $i$、负号、手征投影和共轭顶点。

当前模型中需要重点核对的结构是

\[
-y_\mu\bar L_\mu H E_{\mu R}-\lambda_\mu S\bar E_{\mu L}\mu_R-M_E\bar E_{\mu L}E_{\mu R}+\mathrm{h.c.}
\]

以及质量对角化后 $h$、$s$ 与轻/重费米子的所有耦合。不要只核对轻轻耦合；目标四点圈图可能包含轻重混合顶点。

验收标准：导出的每一个目标顶点都能追溯到原始拉格朗日量中的一项；顶点列表中的场顺序、共轭、手征结构和系数有单独记录。

### 98.3 导出到 FeynArts 前，先做模型自检

1. 检查模型文件能在 FeynRules 中加载，无未定义参数和字段警告。
2. 输出所有与目标外腿 $h,h,s,s$ 相关的三点和四点顶点。
3. 检查质量本征态是否确实是传播子使用的态；如果 FeynRules 模型保留的是规范/相互作用本征态，不能直接把它当作已对角化模型。
4. 明确模型中是否包含 Goldstone、ghost、规范场或额外标量。若目标振幅只涉及 Yukawa 费米子环，也要确认筛选条件不会意外排除必要的相关图。
5. 将导出模型和参数文件复制到 `generated/`，保存原始导出日志。

验收标准：导出前后目标顶点数量、场内容和耦合表达式一致。若有任何场名或共轭方向变化，先解决映射问题，不要继续生成圈图。

### 98.4 用 FeynArts 先生成拓扑，再插入模型场

FeynArts 的常见工作顺序是先用 `CreateTopologies` 生成指定外腿数和圈数的拓扑，再用 `InsertFields` 将模型场插入拓扑，最后用 `CreateFeynAmp` 生成振幅表达式。具体选项须以本机安装版本的官方示例为准。

建议按以下顺序操作：

1. **树图烟雾测试**：先生成一个简单的树级顶点过程，确认导出模型被正确识别。
2. **一圈四点拓扑**：生成 1-loop、4-point 的拓扑；暂时不要用很严的过滤条件。
3. **插入外腿**：指定两个 $h$ 和两个 $s$ 的外腿，并明确它们是带标签的外腿还是同类未标记外腿。
4. **插入内部场**：先限制到模型中可能形成目标闭费米子环的费米子场，再逐步扩大到所有允许场，比较图数变化。
5. **生成振幅**：保存未筛选的拓扑、插场结果和振幅表达式；每一步都单独保存，便于定位图数异常的来源。
6. **筛选目标图**：按内部传播子种类、顶点耦合阶数和目标外腿筛选。不要仅凭图的外观手动删图。
7. **建立图账本**：给每张图分配稳定 ID，记录拓扑、内部场序列、外腿标签、对称因子和耦合乘积。

重要提醒：FeynArts 生成的图数不必与手工枚举的“6 个循环类 × 16 条内部路径”直接相等。FeynArts 的图是带场插入和对称因子的图对象；你的 96 条记录是“循环类 × 内部态路径”的权重账本。二者必须建立显式映射，不能仅比较总数就宣布一致。

验收标准：每一张保留图都能映射到路径账本中的循环类和内部态路径；任何未映射图、重复映射或多余对称因子都必须解释。

### 98.5 用 FeynCalc 转换振幅并逐图检查

1. 对单张目标图调用当前版本支持的 FeynArts-to-FeynCalc 转换接口（通常使用 `FCFAConvert`）；转换前先阅读该版本选项说明。
2. 显式设置外部动量名称、内部圈动量名称、维数约定和所需的费米子链处理选项。
3. 不要一开始就对所有图执行 `FullSimplify` 或大规模展开；先转换一张图并检查结果结构。
4. 对照原始 FeynArts 图检查：每个传播子是否保留、质量是否正确、动量方向是否一致、顶点顺序是否对应同一条费米子链。
5. 检查闭费米子环负号、顶点 $i$ 因子和传播子 $i$ 因子是由生成振幅的工具链自动带入，还是需要在你的约定中单独处理。不得既让软件带入又手动乘一次。
6. 对一张图提取分子和分母，和手工构造的原始迹比较；只有逐项一致后才批量转换。

验收标准：选定单图的 FeynCalc 表达式与手工原始振幅在相同场、动量和符号约定下相同。若只在整体 $i$ 或负号上不同，也必须追踪来源，不能用“物理上应该差一个号”作为修正。

### 98.6 从单图扩展到所有目标图

当单图通过后，编写批处理循环：对每张图执行转换、分母/分子提取、路径分类、低能展开或张量积分约化，并把结果写入单独文件。每张图都保留原始表达式，不要只保存最终合并结果。

建议输出一个 CSV 或 TSV 图账本，至少包括：

- `diagram_id`：图的稳定编号；
- `topology_id`：拓扑类型；
- `external_ordering`：带标签外腿顺序；
- `internal_state_path`：四个传播子的内部态；
- `propagator_masses`：四条边的质量序列；
- `coupling_product`：四个顶点的耦合乘积；
- `symmetry_factor`：图的对称因子；
- `fermion_loop_sign`：闭费米子环符号是否已包含；
- `momentum_routing`：内部动量路由；
- `feyncalc_status`：转换/化简状态；
- `comparison_status`：与现有 Python 结果的比较结果。

批处理时逐图记录错误，不要遇到一张失败图就静默跳过。最终必须检查：生成图集是否覆盖六种带标签循环类，内部态路径是否覆盖 16 种组合，以及是否出现同一物理贡献重复计数。

### 98.7 什么时候用 TID，什么时候用 Feynman 参数

- 如果 FeynCalc 将单图表达式顺利约化成标准 Passarino–Veltman 结构，可以先用 `TID` 路线。
- 如果四点函数在低能展开前表达式过大，或约化形式难以直接提取目标局部项，切换到先做外动量展开、再积分约化的路线。
- 若需要保留路径依赖的内部质量并直接构造局部系数，可使用 Feynman 参数化路线；但必须明确积分测度、单纯形归一化和 Wick 约定。
- 两条路线至少对一个非平凡单图做交叉检查。不要把某一条路线无法化简误判成物理振幅为零。

### 98.8 最终匹配之前必须完成的物理核验

FeynRules/FeynArts/FeynCalc 自动化只解决模型输入、图生成和部分代数，不会自动替你完成完整的 EFT matching。合并 UV 图之前逐项确认：

1. UV 图集完整且无重复；
2. 模型的质量本征态、顶点和共轭规则正确；
3. 闭费米子环、顶点和传播子的整体因子只计算一次；
4. Minkowski 与 Euclidean 约定一致；
5. 低能展开保留目标算符需要的动量阶数；
6. EFT 中同阶图、接触图及必要反项都已包括；
7. UV 与 EFT 使用一致的正规化和重整化方案；
8. UV/IR 极点已分别识别，不能把红外极点误认作 Wilson 系数的 UV 发散；
9. UV–EFT 相减后投影到明确的算符基底；
10. 最终结果通过独立极限、维数分析、对称性和至少一种独立计算路线的检查。

### 98.9 建议的实际执行顺序

- [ ] A：运行 FeynRules 官方示例并成功导出一个 FeynArts 模型。
- [ ] B：把当前模型逐项加进去，先验证质量本征态 Yukawa 顶点。
- [ ] C：FeynArts 生成目标一圈四点图，保存未筛选图集。
- [ ] D：选一张图用 FeynCalc 转换，逐项比较原始分子与分母。
- [ ] E：把这一张图计算到目标低能阶，并与现有 Python 单路径计算比较。
- [ ] F：建立图 ID 到六循环/16 路径账本的映射。
- [ ] G：批量计算所有目标图，保存每张图的原始表达式和日志。
- [ ] H：统一检查整体因子、积分约定和外腿排列。
- [ ] I：独立计算 EFT 图和反项。
- [ ] J：完成 UV–EFT 相减、算符投影和 Wilson 系数的独立复核。

若 A–E 任一步失败，暂停批量运行并修正最小案例。未通过 I 和 J 之前，任何候选系数都只能标记为“UV 振幅候选/未完成匹配”，不能称为最终 Wilson 系数。

## 第 99 节：整体 Minkowski/Wick 因子与参数归一化审计

### 99.1 审计目标与约定

本节不再把路径反向映射的一致性当作整体归一化证据，而是从原始四点费米子环的费曼规则重新列账。约定度规为 \((+---)\)，传播子分母为

\[
D_j=(k+r_j)^2-m_j^2+i0,
\]

振幅按 \(i\mathcal M\) 记，圈积分测度为 \(d^4k/(2\pi)^4\)。以下先假设四个标量 Yukawa 顶点的费曼规则均写成 \(-iY_j\)，四条费米子传播子写成 \(i(\slashed k+\slashed r_j+m_j)/D_j\)。若某个顶点使用了不同的共轭/符号定义，必须在模型顶点表中显式修正，不能在最后整体猜符号。

### 99.2 原始图的显式 \(i\) 因子

| 来源 | 因子 | 四点圈图合计 |
|---|---:|---:|
| 闭合费米子环 | 费米子环规则 | \(-1\) |
| 四个 Yukawa 顶点 | 每个 \(-iY_j\) | \((-i)^4=+1\)（耦合矩阵乘积另列） |
| 四个费米子传播子 | 每个 \(i(\slashed q+m)/D\) | \(i^4=+1\)（分子 \(\slashed q+m\) 另列） |
| 顶点与传播子显式 \(i\) 的乘积 |  | \(+1\) |
| 加上闭合费米子环 |  | **整体为 \(-1\)**，尚未包含圈积分与分子迹 |

因此，若此前的候选核只追踪了分子迹与 Wick 积分，而没有把闭合费米子环的 \(-1\) 放进去，则该负号必须乘在所有路径、所有循环排列的总和上一次。若它已包含在原始 determinant/trace 约定中，则不得重复乘入。两种记账方式只能选一种。

### 99.3 Wick 转动符号与积分系数

令

\[
R=\sum_{j=1}^4x_jr_j,\qquad K=k+R,\qquad
\Delta_0=\sum_jx_jm_j^2,
\]

\[
\delta\Delta=\sum_jx_jr_j^2-R^2.
\]

则 Minkowski 分母为 \(K_M^2-\Delta_0+\delta\Delta+i0\)，Wick 后的 Euclidean 分母为 \(K_E^2+\Delta_0-\delta\Delta\)。故

\[
\frac{1}{(K_E^2+\Delta_0-\delta\Delta)^n}
=\frac{1}{(K_E^2+\Delta_0)^n}
+\frac{n\,\delta\Delta}{(K_E^2+\Delta_0)^{n+1}}+O(p^4).
\]

对含 \((K_M^2)^r\) 的项，Wick 转动的符号为 \((-1)^{n+r}\)，其中 \(n\) 是当前分母幂次，\(r\) 是显式 Minkowski \(K_M^2\) 的幂次。这个符号不包括闭合费米子环的额外 \(-1\)。常用标量积分为

\[
\int\frac{d^4k}{(2\pi)^4}\frac{1}{(k^2-\Delta+i0)^n}
=\frac{i(-1)^n}{16\pi^2}\frac{\Gamma(n-2)}{\Gamma(n)}\Delta^{2-n},\quad n>2,
\]

以及

\[
\int\frac{d^4K_E}{(2\pi)^4}\frac{K_E^2}{(K_E^2+\Delta)^4}
=\frac{1}{16\pi^2}\frac{1}{3\Delta}.
\]

注意：对 \(n=4\) 的无分子幂标量积分，\(\Gamma(2)/\Gamma(4)=1/6\)；对 \(n=5\)，\(\Gamma(3)/\Gamma(5)=1/12\)。含 \(K_E^2\) 的积分有自己的 Gamma 函数比，不能把无分子幂公式直接套上去。

### 99.4 六类循环排列的组合计数

四个外腿标记为 \(h_1,h_2,s_1,s_2\)。闭合环的循环旋转等价，因此固定 \(h_1\) 在首位后，其余三腿有 \(3!=6\) 个有标记循环：

1. \(h_1-h_2-s_1-s_2\)；
2. \(h_1-h_2-s_2-s_1\)；
3. \(h_1-s_1-h_2-s_2\)；
4. \(h_1-s_1-s_2-h_2\)；
5. \(h_1-s_2-h_2-s_1\)；
6. \(h_1-s_2-s_1-h_2\)。

从 \(\Gamma_f= -i\,\mathrm{Tr}\log(D_0+V)\) 的四阶展开看，四阶项带 \(1/4\)，但每个有标记的循环在迹中有四个循环旋转表示；两者抵消后，每个有标记循环计一次。因此这里应求和六类循环各一次，**不能在六类循环求和后再乘一个额外的 2 来代表“反向环”**。反向循环若与某个已列循环相关，应通过其顶点/质量/参数重标记关系核对，而不是重复计数。

### 99.5 Feynman 参数归一化：必须明确的 6 与单纯形体积

四个传播子分母的标准恒等式是

\[
\frac{1}{D_1D_2D_3D_4}
=\Gamma(4)\int_{x_j\ge0}\!\!\prod_{j=1}^4dx_j\,
\delta\!\left(1-\sum_jx_j\right)
\frac{1}{[\sum_jx_jD_j]^4}
=6\int_{\text{simplex}}[dx]\frac{1}{[\sum_jx_jD_j]^4}.
\]

这里 \([dx]=\prod_jdx_j\,\delta(1-\sum_jx_j)\)，其三维单纯形体积为 \(1/6\)。若把参数积分写成未归一化的单纯形积分，必须保留 \(\Gamma(4)=6\)；若改写成归一化平均 \(\langle f\rangle=6\int_{\text{simplex}}[dx]f\)，则不再额外乘 6。二者不能混用。

| 步骤 | 原始约定中的因子 | 审计规则 |
|---|---:|---|
| 四分母合并 | \(\Gamma(4)=6\) | 必须出现一次，除非已吸收到归一化平均定义中 |
| 单纯形体积 | \(1/6\) | 仅用于积分常数/常数被积函数；不能把一般被积函数积分直接替换成体积 |
| \(n=4\) 圈积分 | \(\Gamma(2)/\Gamma(4)=1/6\) | 与参数合并的 6 在常数分子项中可能抵消，但要按每个分子结构分别算 |
| \(n=5\) 圈积分 | \(\Gamma(3)/\Gamma(5)=1/12\) | 不等于单纯形体积；还要追踪来自 \(\delta\Delta\) 展开的系数 \(n\) |
| 归一化参数平均 | 定义为 \(6\int[dx]\) | 使用后不能再乘 \(6\) |

### 99.6 将既有候选核放回统一因子账本

既有候选核为

\[
B^{(1)}_\alpha=H\left(-\frac23g_\alpha+2d_\alpha\right),\quad
B^{(2)}_\alpha=\frac13F_\alpha-\frac23S d_\alpha,\quad
B^{(3)}_\alpha=+\frac23M d_\alpha.
\]

此前逐项 Wick 审计所用的局部系数表如下。该表只核对“给定分子分解之后”的 Wick 符号和积分约化，不代表模型特定分子分解已经从原始迹独立推导完毕。

| 分子结构 | Wick 前局部系数 | \(n\) | \(r\) | Wick 符号 \((-1)^{n+r}\) | Wick 后局部系数（尚未乘闭环负号） |
|---|---:|---:|---:|---:|---:|
| \(F\) | \(2F\) | 4 | 0 | \(+1\) | \(+2F\) |
| \(Hg\) | \(2Hg\) | 4 | 1 | \(-1\) | \(-2Hg\) |
| \(Hd\) | \(-8Hd\) | 5 | 2 | \(-1\) | \(+8Hd\) |
| \(Sd\) | \(-8Sd\) | 5 | 1 | \(+1\) | \(-8Sd\) |
| \(Md\) | \(-8Md\) | 5 | 0 | \(-1\) | \(+8Md\) |

**重要审计发现：当前还不能宣布整体因子已关闭。** 必须把上表中的“局部系数”逐项追溯到原始四分母参数恒等式，确认 \(\Gamma(4)=6\) 是否已乘入、圈积分的 Gamma 函数比是否已乘入、以及候选 \(B^{(j)}\) 是否定义为未归一化单纯形被积函数还是归一化参数平均。仅从既有候选核的形式，不能证明这些约定已经一致。

### 99.7 关闭整体因子的最终判据

在写出最终 UV 振幅前，应为每个六循环、每条内部路径生成一行机器可读账本，至少含：

- 循环 ID、路径 ID、原始顶点矩阵乘积与原始 Dirac 迹；
- 闭环负号（一个布尔字段，确保恰好一次）；
- 四顶点 \((-i)^4\)、四传播子 \(i^4\)；
- 每个分子项的 \((n,r)\)、Wick 符号及对应 Euclidean Gamma 函数系数；
- 参数合并因子 \(\Gamma(4)=6\) 与积分测度类型（未归一化 simplex / 归一化平均）；
- 六循环计数权重（每类为 1）；
- 最终统一的 \(i\mathcal M\) 或 \(\mathcal M\) 约定。

通过标准：对一个明确的原始路径，从费曼规则直接得到的振幅与 determinant 展开得到的振幅逐项相同；把六循环求和后不得出现额外的 2；在同一参数积分定义下，所有 \(1/6\)、\(1/12\) 与 \(\Gamma(4)=6\) 都能追溯到唯一来源。随后才可将闭环负号乘入或确认它已包含在候选核中，并固定最终整体系数。

**本节状态：部分完成，尚未关闭。** 已明确闭环负号与 Wick 符号是不同来源，列出了六循环计数和标准参数恒等式，并发现参数归一化需要回溯。尚未完成的是：对每一条原始路径从未约化分子开始，把参数合并因子、所有积分 Gamma 系数和候选 \(B^{(j)}\) 的定义逐项自动化对账。因此，本节不授权把候选核称为已确定的最终 UV 振幅或 Wilson 系数。


## 第 100 节：四分母单路径的通用积分系数表（独立核算）

### 100.1 本节边界

本节不把候选 $B^{(j)}_\alpha$ 当作输入，而只核算任意一条四传播子路径在 Feynman 参数合并、平移动量、Wick 转动和标准积分之后的通用系数。它可以确定普适积分系数，但不能替代模型特定的原始 Dirac 迹，也不能单独确定最终 Wilson 系数。

沿用

\[
D_j=(k+r_j)^2-m_j^2+i0,\quad K=k+R,\quad
\Delta_0=\sum_jx_jm_j^2,\quad
\delta\Delta=\sum_jx_jr_j^2-R^2.
\]

四分母恒等式为

\[
\frac1{D_1D_2D_3D_4}=6\int[dx]\frac1{[K_M^2-\Delta_0+\delta\Delta+i0]^4},
\]

其中 $[dx]=\prod_jdx_j\,\delta(1-\sum_jx_j)$，单纯形体积为 $1/6$。Wick 后的分母为 $K_E^2+\Delta_0-\delta\Delta$，所以

\[
(K_E^2+\Delta_0-\delta\Delta)^{-4}
=(K_E^2+\Delta_0)^{-4}+4\delta\Delta(K_E^2+\Delta_0)^{-5}+O(p^4).
\]

### 100.2 独立积分系数

使用 $d=4$ 的标准欧氏积分

\[
\int\frac{d^4K_E}{(2\pi)^4}\frac1{(K_E^2+\Delta)^n}
=\frac1{16\pi^2}\frac{\Gamma(n-2)}{\Gamma(n)}\Delta^{2-n},
\]

以及

\[
\int\frac{d^4K_E}{(2\pi)^4}\frac{K_E^2}{(K_E^2+\Delta)^n}
=\frac1{16\pi^2}\frac{2\Gamma(n-3)}{\Gamma(n)}\Delta^{3-n}.
\]

注意第二式仅对此处使用的收敛积分 $n=4,5$ 直接应用；不能把它误写成第一式。

将四分母参数合并的 $6$ 乘入后，四种结构为：

| 移位后结构 | 欧氏积分（尚未乘参数合并的 6） | 乘 6 后 | 结果状态 |
|---|---:|---:|---|
| $1/(K_E^2+\Delta)^4$ | $\frac1{16\pi^2}\frac1{6\Delta^2}$ | $\frac1{16\pi^2}\frac1{\Delta^2}$ | 已确定 |
| $1/(K_E^2+\Delta)^5$ | $\frac1{16\pi^2}\frac1{12\Delta^3}$ | $\frac1{16\pi^2}\frac1{2\Delta^3}$ | 已确定 |
| $K_E^2/(K_E^2+\Delta)^4$ | $\frac1{16\pi^2}\frac1{3\Delta}$ | $\frac1{16\pi^2}\frac2{\Delta}$ | 已确定 |
| $K_E^2/(K_E^2+\Delta)^5$ | $\frac1{16\pi^2}\frac1{12\Delta^2}$ | $\frac1{16\pi^2}\frac1{2\Delta^2}$ | 已确定 |

因此，参数合并的 $6$ 与无分子幂 $n=4$ 积分中的 $1/6$ 抵消；对 $n=5$ 的无分子幂项，乘完后剩下 $1/2$；对 $K_E^2/(K_E^2+\Delta)^4$，乘完后是 $2/\Delta$。这三个结论不能互相替代。

### 100.3 将 Wick 符号与参数展开分开记账

按当前约定，含 $(K_M^2)^r$ 的原始 Minkowski 项相对相应欧氏积分给出 $(-1)^{n+r}$。将这个符号与上节的欧氏积分系数相乘，可得以下单路径通用账本（表中已包含参数合并因子 $6$，但尚未乘闭合费米子环的 $-1$）：

| 原始结构 | Wick 符号 | 参数展开来源 | 含参数合并的系数（相对 $i/(16\pi^2)$） |
|---|---:|---|---:|
| $1/D^4$ 的常数分子 | $+1$ | $\Delta_0^{-2}$ | $+\Delta_0^{-2}$ |
| $K_M^2/D^4$ | $-1$ | $K_E^2$ 积分 | $-2\Delta_0^{-1}$ |
| $1/D^4$ 的 $\delta\Delta$ 一阶项 | $+1$ | $4\delta\Delta/D_E^5$ | $+2\delta\Delta\,\Delta_0^{-3}$ |
| $K_M^2/D^4$ 的 $\delta\Delta$ 一阶项 | $-1$ | $4\delta\Delta K_E^2/D_E^5$ | $-2\delta\Delta\,\Delta_0^{-2}$ |

这里的 $D$ 仅代表参数合并前的传播子分母乘积结构；表格中的结果只用于相应的分子项。若分子本身还有外动量项、质量插入项或更高的 $K^2$ 幂次，必须逐项展开后分别归类，不能直接把整条路径压成表中某一行。

### 100.4 加入费曼规则的整体 $i$ 账本

若四个标量 Yukawa 顶点的规则均为 $-iY_j$，四个费米子传播子各为 $i(\slashed q_j+m_j)/D_j$，则

\[
(-1)_{\rm closed\ fermion\ loop}\times(-i)^4\times i^4=-1.
\]

标准 Minkowski 圈积分经 Wick 转动提供额外的 $i$。因此，在把 Dirac 迹、耦合乘积和参数积分系数均按前述定义分离后，图的贡献具有 $i\mathcal M$ 中的整体形式

\[
i\mathcal M_{\rm path}=(-1)_{\rm loop}\,i\,\frac{1}{16\pi^2}
\int[dx]\,\bigl[\text{已逐项 Wick 化的分子积分核}\bigr],
\]

即对本节表格列出的每一项，再乘闭环负号后，$i\mathcal M$ 的系数符号与表格的 Wick 后符号相反。这里没有额外加入循环排列计数：每个带标记循环的权重仍为 $1$，六类循环最后求和一次。

**约定提醒：** 上述结论以振幅记作 $i\mathcal M$、顶点写成 $-iY_j$、传播子分子写成 $i(\slashed q+m)$ 为前提。如果原文把某些共轭顶点写为 $+iY_j^*$，或此前的 determinant 推导已经把闭环负号纳入定义，则必须在原始规则表中相应调整，不能机械地再乘一次负号。

### 100.5 本节关闭了什么，尚未关闭什么

已独立确定：四分母参数合并系数；四种常用欧氏积分；$6$ 与 $1/6$、$1/12$、$1/3$ 的正确配对；$K_M^2$ 和 $\delta\Delta$ 展开项的通用 Wick 符号；在指定费曼规则下闭环负号与圈积分 $i$ 的位置。

尚未关闭：必须从具体一条 UV 路径的原始顶点矩阵乘积和未约化 Dirac 迹中，确认其每个项究竟落入哪种分子结构；再把这些项与候选 $B^{(1,2,3)}_\alpha$ 的定义逐项比对。现有文档里候选分解的局部系数尚不能仅由通用积分表反推出，因此不应声称已证明候选核的整体符号完全正确。下一步应选定一个明确循环与内部态路径，保存原始迹、移位后分子和逐项积分账本，再与 determinant 四阶项作独立比较。



## 第 102 节：圈动量展开与积分核

### 102.1 目标与核验边界

本节固定一条 `hhss` 外腿循环和内部态路径，整理圈动量路由、原始 Dirac 迹的候选分解、Feynman 参数分母展开，以及二阶外动量所需的欧氏积分核。这里的代数整理不自动等于完整 UV–EFT 匹配；在原始矩阵迹、Minkowski–Euclidean 符号映射和整体费曼规则因子逐项通过独立核验前，路径系数均标记为候选中间量。

### 102.2 路由、质量顺序与顶点

固定外腿循环为 `hhss`，内部态路径为
\[
\rho=(1,2,1,2),\qquad (\mu_1,\mu_2,\mu_3,\mu_4)=(m_2,m_1,m_2,m_1).
\]
采用路由
\[
r_1=0,\quad r_2=-q_2,\quad r_3=-q_2-q_3,\quad r_4=q_1,
\qquad k_i=K+r_i,
\]
并定义 \(R_{ij}=r_i\cdot r_j\)。Feynman 参数满足 \(x_i\geq0\)、\(\sum_i x_i=1\)。完成参数平移后，令
\[
\bar r=\sum_i x_i r_i,
\qquad t_i=r_i-\bar r,
\qquad k_i=K+t_i.
\]
因此
\[
\bar r=-x_2q_2-x_3(q_2+q_3)+x_4q_1.
\]

沿用的实标量顶点约定为
\[
\Gamma^{(\phi)}_{ij}=(Y_\phi)_{ij}P_R+(Y_\phi)_{ji}P_L,
\qquad P_{R,L}=\frac{1\pm\gamma_5}{2}.
\]
其中
\[
Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix}.
\]
对该路径，按 \(u_r=(Y_{\phi_r})_{a_ra_{r+1}}\)、\(v_r=(Y_{\phi_r})_{a_{r+1}a_r}\) 记号，有
\[
\begin{aligned}
u_1&=ac_Lc_R,&v_1&=as_Ls_R,\\
u_2&=as_Ls_R,&v_2&=ac_Lc_R,\\
u_3&=-bs_Ls_R,&v_3&=-bc_Lc_R,\\
u_4&=-bc_Lc_R,&v_4&=-bs_Ls_R.
\end{aligned}
\]

### 102.3 原始迹与候选分子分解

应直接核验的原始路径迹为
\[
T_\rho=\operatorname{tr}_D\!\left[\Gamma_1(\slashed k_1+\mu_1)\Gamma_2(\slashed k_2+\mu_2)
\Gamma_3(\slashed k_3+\mu_3)\Gamma_4(\slashed k_4+\mu_4)\right].
\]
此前使用的候选分解为
\[
T_\rho=2H_\rho G+2\sum_{i<j}C_{ij}^{(\rho)}k_i\cdot k_j+2M_\rho,
\]
其中
\[
G=(k_1\cdot k_2)(k_3\cdot k_4)-(k_1\cdot k_3)(k_2\cdot k_4)+(k_1\cdot k_4)(k_2\cdot k_3).
\]
手征组合给出的候选系数为
\[
H_\rho=u_1v_2u_3v_4+v_1u_2v_3u_4
=2a^2b^2c_L^2c_R^2s_L^2s_R^2,
\]
\[
M_\rho=\mu_1\mu_2\mu_3\mu_4\left(\prod_ru_r+\prod_rv_r\right)
=2a^2b^2c_L^2c_R^2s_L^2s_R^2m_1^2m_2^2.
\]
候选二质量系数为
\[
\begin{aligned}
C_{12}=C_{14}=C_{23}=C_{34}
&=a^2b^2c_Lc_Rs_Ls_Rm_1m_2(c_L^2c_R^2+s_L^2s_R^2),\\
C_{13}&=a^2b^2m_1^2(c_L^4c_R^4+s_L^4s_R^4),\\
C_{24}&=2a^2b^2c_L^2c_R^2s_L^2s_R^2m_2^2.
\end{aligned}
\]
令 \(S_\rho=\sum_{i<j}C_{ij}^{(\rho)}\)，则
\[
\begin{aligned}
S_\rho=a^2b^2\big[&m_1^2(c_L^4c_R^4+s_L^4s_R^4)\\
&+4m_1m_2c_Lc_Rs_Ls_R(c_L^2c_R^2+s_L^2s_R^2)\\
&+2m_2^2c_L^2c_R^2s_L^2s_R^2\big].
\end{aligned}
\]
**核验状态：** 上述 \(H_\rho,C_{ij}^{(\rho)},M_\rho\) 是由既有手征组合整理出的候选值，不能替代对原始 \(\gamma\) 矩阵迹的直接计算。对应脚本应检查原始迹、移位后的分子和本节公式是否逐项一致。

### 102.4 圈动量张量平均：必须使用平移后的偏移量

在完成 Feynman 参数化后，令
\[
K=\ell+\bar r,\qquad t_i=r_i-\bar r,\qquad k_i=K+t_i,
\qquad R_{ij}=t_i\cdot t_j.
\]
这里的 \(R_{ij}\) 是欧氏内积；特别地，虽然原始路由取 \(r_1=0\)，平移后通常有 \(t_1=-\bar r\ne0\)，因此一般不能令 \(R_{1j}=0\)。

对
\[
G_E=(k_1\cdot k_2)(k_3\cdot k_4)
-(k_1\cdot k_3)(k_2\cdot k_4)
+(k_1\cdot k_4)(k_2\cdot k_3)
\]
作四维欧氏角平均，使用
\[
\langle(K\cdot a)(K\cdot b)\rangle=\frac{K_E^2}{4}a\cdot b,
\]
得到
\[
\boxed{\langle G_E\rangle_K=K_E^4+A_xK_E^2+O(q^4),}
\]
其中完整的二阶系数为
\[
\boxed{A_x=R_{12}-\frac12R_{13}+R_{14}+R_{23}-\frac12R_{24}+R_{34}.}
\]
此前忽略 \(R_{12},R_{14},R_{13}\) 的简式不适用于平移后的 \(t_i\)，应以本式为准。

每个二动量结构满足
\[
\langle k_i\cdot k_j\rangle_K=K_E^2+R_{ij}.
\]
考虑 Minkowski 到 Euclidean 的 Wick 映射后，若把 Euclidean 分子定义为与该映射一致的约定，则候选迹分解给出
\[
\begin{aligned}
A_2&=2H_\rho, & A_1^{(0)}&=-2S_\rho,\\
A_1^{(2)}&=2H_\rho A_x, & A_0^{(2)}&=-2\sum_{i<j}C_{ij}^{(\rho)}R_{ij},\\
A_0^{(0)}&=2M_\rho,
\end{aligned}
\]
其中 \(S_\rho=\sum_{i<j}C_{ij}^{(\rho)}\)。这组符号依赖于上述 Euclidean 分子约定；整体圈图的 \(i\) 因子仍须在振幅层面单独核对。

### 102.5 Feynman 参数分母展开：统一符号约定

定义
\[
\Delta_0=\sum_i x_i\mu_i^2,\qquad
\delta\Delta=\sum_i x_i r_i^2-\bar r^2=\sum_i x_i t_i^2.
\]
因为完成平方后
\[
\sum_i x_i\big[(\ell+r_i)^2+\mu_i^2\big]
=K_E^2+\Delta_0+\delta\Delta,
\]
所以正确的二阶展开是
\[
\boxed{
\frac1{(K_E^2+\Delta_0+\delta\Delta)^4}
=\frac1{(K_E^2+\Delta_0)^4}
-\frac{4\delta\Delta}{(K_E^2+\Delta_0)^5}+O(q^4).
}
\]
这与把分母写成 \(K_E^2+\Delta_0-\delta\Delta\) 的旧写法不同；在当前定义下，后者符号错误。当前路由给出
\[
\begin{aligned}
\delta\Delta={}&x_2Q_2+x_3(Q_2+Q_3+2d_{23})+x_4Q_1\\
&-\big[x_4q_1-(x_2+x_3)q_2-x_3q_3\big]^2_E,
\end{aligned}
\]
其中 \(Q_i=q_i^2\) 且 \(d_{ij}=q_i\cdot q_j\) 均采用同一 Euclidean 约定。该式是 \(O(q^2)\) 量。

### 102.6 四维积分与修正后的二阶积分核

使用归一化单纯形平均
\[
\langle F\rangle_x=6\int_0^1\prod_{i=1}^4dx_i\,\delta\!\left(1-\sum_i x_i\right)F(x),
\]
四维 Euclidean 积分（尚未乘 Feynman 参数化给出的因子 6）为
\[
\begin{aligned}
I_{0,4}&=\frac1{16\pi^2}\frac1{6\Delta_0^2},&
I_{1,4}&=\frac1{16\pi^2}\frac1{3\Delta_0},\\
I_{1,5}&=\frac1{16\pi^2}\frac1{12\Delta_0^2},&
I_{2,5}&=\frac1{16\pi^2}\frac1{4\Delta_0}.
\end{aligned}
\]
若
\[
\mathcal N_E=A_2K_E^4+\big(A_1^{(0)}+A_1^{(2)}\big)K_E^2
+A_0^{(0)}+A_0^{(2)}+O(q^4),
\]
则由分子展开和分母展开的乘积，二阶积分核为
\[
\boxed{\begin{aligned}
\mathcal I^{(2)}=\frac1{16\pi^2}\Bigg[&\frac{2A_1^{(2)}}{\Delta_0}
+\frac{A_0^{(2)}}{\Delta_0^2}\\
&-\frac{6A_2\,\delta\Delta}{\Delta_0}
-\frac{2A_1^{(0)}\,\delta\Delta}{\Delta_0^2}\Bigg].
\end{aligned}}
\]
负号来自分母展开中的 \(-4\delta\Delta\)。将上述候选分子系数代入，得到单路径积分核
\[
\boxed{\begin{aligned}
\mathcal I_\rho^{(2)}=\frac1{16\pi^2}\Bigg[&\frac{4H_\rho A_x}{\Delta_0}
-\frac{2\sum_{i<j}C_{ij}^{(\rho)}R_{ij}}{\Delta_0^2}\\
&-\frac{12H_\rho\,\delta\Delta}{\Delta_0}
+\frac{4S_\rho\,\delta\Delta}{\Delta_0^2}\Bigg].
\end{aligned}}
\]
这里的四个项分别来自分子二阶 \(K_E^2\) 项、分子二阶常数项、分母修正乘零阶 \(K_E^4\) 项，以及分母修正乘零阶 \(K_E^2\) 项。归一化平均已吸收 \(\Gamma(4)=6\)，不可重复计数。

### 102.7 费曼规则整体因子与循环权重

在图形法约定下，四个顶点、四条费米子传播子、闭合费米子环负号和 Wick 转动产生的整体 \(i\) 必须分开记账。若改用费米子行列式展开，行列式中的传播子逆算符通常不带图形法传播子的显式 \(i\)；两种方法只能在统一约定后比较，不能将图形法的 \(i^4\) 再乘进行列式结果。四个不同标记外腿的循环类数为 \(4!/4=6\)，按循环等价类求和时不得再额外乘一个反向循环因子，除非原始定义明确要求。

### 102.8 当前状态与下一步

**本节已整理：** 路由和质量顺序、顶点耦合代入、候选迹系数、圈动量张量平均、Feynman 参数分母展开、四维欧氏积分，以及修正后的二阶积分核。

**尚未完成：**
1. 已在本轮用显式 Minkowski Dirac 矩阵对指定耦合路径作随机数值交叉检验，原始迹与候选分解在浮点精度内一致；仍需符号化/FeynCalc 核验，并检查整体振幅约定。
2. 逐项固定 Minkowski 到 Euclidean 的 Wick 映射，核对所有外动量项的符号。
3. 把分子各项按本节正确积分核重新投影，废弃未经过重新计算的旧候选 \(B^{(1,2,3)}\) 系数。
4. 对全部不等价外腿循环与内部态路径求和，并与行列式四阶展开交叉核验。
5. 独立计算 EFT 泡图、接触图与反项，在统一重整化方案下检查 UV 极点、尺度依赖和 IR 项抵消。

**结论：** 本节是可审计的中间计算记录，不是最终 Wilson 系数，也不表示 UV–EFT 匹配已闭合。


### 102.9 利用交替质量结构将四参数积分降为一维积分

该路径的质量顺序为 \((m_2,m_1,m_2,m_1)\)，因此
\[
\Delta_0=x_1m_2^2+x_2m_1^2+x_3m_2^2+x_4m_1^2.
\]
定义
\[
u=x_1+x_3,\qquad 1-u=x_2+x_4,
\]
以及分割变量 \(z,w\in[0,1]\)：
\[
x_1=uz,\quad x_3=u(1-z),\quad
x_2=(1-u)w,\quad x_4=(1-u)(1-w).
\]
参数单纯形测度变为
\[
6\,d^4x\,\delta\!\left(1-\sum_i x_i\right)
=6u(1-u)\,du\,dz\,dw,
\]
并且分母只依赖单一变量：
\[
\boxed{\Delta(u)=um_2^2+(1-u)m_1^2.}
\]
因此对任意多项式 \(F(x)\)，定义分割平均
\[
\overline F(u)=\int_0^1dz\int_0^1dw\,
F\big(uz,(1-u)w,u(1-z),(1-u)(1-w)\big),
\]
则
\[
\boxed{\langle F/\Delta_0^n\rangle_x
=6\int_0^1du\,u(1-u)\,\frac{\overline F(u)}{\Delta(u)^n}.}
\]
这一步严格成立，因为 \(\Delta_0\) 与 \(z,w\) 无关。对当前二阶核，所需的平均只有
\[
\overline{A_x}(u),\qquad
\overline{\delta\Delta}(u),\qquad
\overline{\sum_{i<j}C_{ij}^{(\rho)}R_{ij}}(u),
\]
而耦合和质量系数 \(H_\rho,S_\rho,C_{ij}^{(\rho)}\) 不依赖参数。于是
\[
\boxed{\begin{aligned}
\langle\mathcal I_\rho^{(2)}\rangle_x
=\frac6{16\pi^2}\int_0^1du\,u(1-u)\Bigg[&
\frac{4H_\rho\overline{A_x}(u)}{\Delta(u)}
-\frac{2\overline{\sum C_{ij}^{(\rho)}R_{ij}}(u)}{\Delta(u)^2}\\
&-\frac{12H_\rho\overline{\delta\Delta}(u)}{\Delta(u)}
+\frac{4S_\rho\overline{\delta\Delta}(u)}{\Delta(u)^2}\Bigg].
\end{aligned}}
\]
每个分割平均都是外动量二次型，且对 \(u\) 至多为二次多项式；因此全部外动量系数最终都归结为有限组
\[
J_{n,k}(m_1^2,m_2^2)=\int_0^1du\,
\frac{u^k(1-u)}{[um_2^2+(1-u)m_1^2]^n},
\qquad k=0,1,2,3,
\]
及其线性组合。对于 \(m_1^2\ne m_2^2\)，这些积分可通过代换 \(y=m_1^2+(m_2^2-m_1^2)u\) 化为有理函数与对数；等质量极限则应从积分表达式连续取极限，避免直接使用带 \((m_2^2-m_1^2)^{-p}\) 的闭式造成数值消减。

#### 102.9.1 分割变量平均的显式多项式

为把一维积分核完全写成可代入形式，定义 Euclidean 外动量不变量
\[
Q_i=q_i^2,\qquad d_{ij}=q_i\cdot q_j.
\]
对 \(z,w\) 积分后，张量项和分母修正项分别为
\[
\boxed{\begin{aligned}
\overline{A_x}(u)=\frac14\big[&Q_1(4u^2-5u+1)+Q_2(2u^2-2u+2)\\
&+Q_3(4u^2-3u)+d_{12}(2u^2-4u+3)\\
&+d_{13}(6u^2-6u-1)+d_{23}(2u^2+1)\big],
\end{aligned}}
\]
\[
\boxed{\begin{aligned}
\overline{\delta\Delta}(u)=-\frac16\big[&Q_1(2u^2-u-1)+Q_2(u^2-u-1)\\
&+Q_3(2u^2-3u)+d_{12}(u^2+u-2)\\
&+d_{13}(3u^2-3u)+d_{23}(u^2-3u)\big].
\end{aligned}}
\]

六个偏移内积的平均多项式为
\[
\begin{aligned}
\overline{R_{12}}=\frac16[&Q_1(2u^2-4u+2)+Q_2(u^2-u-1)+2Q_3u^2\\
&+d_{12}(u^2-2u+1)+d_{13}(3u^2-3u)+d_{23}u^2],\\[2pt]
\overline{R_{13}}=\frac16[&Q_1(2u^2-4u+2)+Q_2(u^2-u-1)+Q_3(2u^2-3u)\\
&+d_{12}(u^2-2u+1)+d_{13}(3u^2-6u+3)+d_{23}(u^2-3)],\\[2pt]
\overline{R_{14}}=\frac16[&Q_1(2u^2-u-1)+Q_2(u^2-u+2)+2Q_3u^2\\
&+d_{12}(u^2+u+1)+3d_{13}u^2+d_{23}(u^2+3u)],\\[2pt]
\overline{R_{23}}=\frac16[&Q_1(2u^2-4u+2)+Q_2(u^2-u+2)+Q_3(2u^2-3u)\\
&+d_{12}(u^2-5u+4)+d_{13}(3u^2-6u+3)+d_{23}(u^2-3u+3)],\\[2pt]
\overline{R_{24}}=\frac16[&Q_1(2u^2-u-1)+Q_2(u^2-u-1)+2Q_3u^2\\
&+d_{12}(u^2-2u-2)+3d_{13}u^2+d_{23}u^2],\\[2pt]
\overline{R_{34}}=\frac16[&Q_1(2u^2-u-1)+Q_2(u^2-u-1)+Q_3(2u^2-3u)\\
&+d_{12}(u^2-2u-2)+d_{13}(3u^2-3u-3)+d_{23}(u^2-3)].
\end{aligned}
\]
因此
\[
\overline{\sum_{i<j}C_{ij}^{(\rho)}R_{ij}}(u)
=\sum_{i<j}C_{ij}^{(\rho)}\overline{R_{ij}}(u),
\]
不再需要对 \(z,w\) 做任何数值积分。上列多项式由代入分割变量后对 \(z,w\in[0,1]\) 的多项式逐项积分得到；后续仍需用独立代码逐项复核，尤其要保证所有外动量内积使用同一 Euclidean 约定。

#### 102.9.2 基本质量比积分的闭式

令 \(a=m_1^2\)、\(b=m_2^2\)、\(d=b-a\ne0\)，并定义
\[
L_{n,j}=\int_0^1du\,\frac{u^j}{(a+du)^n}.
\]
代换 \(y=a+du\) 得
\[
\boxed{L_{n,j}=\frac1{d^{j+1}}\sum_{r=0}^{j}\binom jr(-a)^{j-r}\Phi_{r-n}(a,b),}
\]
其中
\[
\Phi_p(a,b)=\begin{cases}
\dfrac{b^{p+1}-a^{p+1}}{p+1},&p\ne-1,\\[4pt]
\ln\dfrac ba,&p=-1.
\end{cases}
\]
所需的基本积分于是为
\[
\boxed{J_{n,k}=L_{n,k}-L_{n,k+1}.}
\]
等质量极限 \(m_1=m_2=m\) 不应直接代入含 \(d^{-p}\) 的表达式，而应从原始积分取极限：
\[
\boxed{J_{n,k}(m^2,m^2)=\frac1{m^{2n}(k+1)(k+2)}.}
\]
这些公式给出了任意多项式分子与 \(\Delta(u)^{-n}\) 组合所需的解析积分基础。要得到最终 Wilson 系数，还须把每个外动量不变量的系数与六个循环类的权重合并，并完成 UV–EFT 差分。

**本小节进度边界：** 已将参数积分降为一维，并显式给出 \(\overline{A_x}\)、\(\overline{\delta\Delta}\)、六个 \(\overline{R_{ij}}\) 以及基本质量比积分的闭式。尚未完成六个外腿循环与内部态路径的总和、整体符号归一化和 EFT 侧减法，因此仍不报告最终 Wilson 系数。

## 第 103 节：单路径二阶积分核的系数投影与解析积分表达

### 103.1 对第 102.9.1 节参数平均多项式的交叉核验

将路由写成三维系数向量
\[
r_1=(0,0,0),\quad r_2=(0,-1,0),\quad
r_3=(0,-1,-1),\quad r_4=(1,0,0),
\]
其分量分别对应 \((q_1,q_2,q_3)\)，内积由 Gram 矩阵
\[
G_q=\begin{pmatrix}
Q_1&d_{12}&d_{13}\\
d_{12}&Q_2&d_{23}\\
d_{13}&d_{23}&Q_3
\end{pmatrix}
\]
计算。代入
\[
x_1=uz,\quad x_2=(1-u)w,\quad
x_3=u(1-z),\quad x_4=(1-u)(1-w),
\]
再对 \(z,w\in[0,1]\) 逐项积分，可独立得到第 102.9.1 节六个 \(\overline{R_{ij}}\) 多项式。核对发现，其中 \(\overline{R_{13}}\) 和 \(\overline{R_{34}}\) 的 \(d_{23}\) 项应分别为
\[
\boxed{\left.\overline{R_{13}}\right|_{d_{23}}
=\frac{d_{23}}6(u^2-3),\qquad
\left.\overline{R_{34}}\right|_{d_{23}}
=\frac{d_{23}}6(u^2-3).}
\]
不是旧稿中的 \(d_{23}(u^2-3u)/6\)。这两处现已在第 102.9.1 节直接修正。其余列出的 \(R_{ij}\) 系数与按上述 Gram 矩阵直接积分所得表达式一致。

将修正后的六个平均代回
\[
\overline{A_x}=\overline{R_{12}}-
\frac12\overline{R_{13}}+\overline{R_{14}}+
\overline{R_{23}}-\frac12\overline{R_{24}}+\overline{R_{34}},
\]
得到
\[
\boxed{\begin{aligned}
\overline{A_x}(u)=\frac14\big[&Q_1(4u^2-5u+1)
+Q_2(2u^2-2u+2)\\
&+Q_3(4u^2-3u)+d_{12}(2u^2-4u+3)\\
&+d_{13}(6u^2-6u-1)+d_{23}(2u^2+1)\big].
\end{aligned}}
\]
这与第 102.9.1 节的 \(\overline{A_x}\) 相符。分母修正项的平均为
\[
\boxed{\begin{aligned}
\overline{\delta\Delta}(u)=-\frac16\big[&Q_1(2u^2-u-1)
+Q_2(u^2-u-1)\\
&+Q_3(2u^2-3u)+d_{12}(u^2+u-2)\\
&+d_{13}(3u^2-3u)+d_{23}(u^2-3u)\big].
\end{aligned}}
\]

### 103.2 将积分核投影到独立外动量不变量

定义六个参数平均
\[
\mathcal R_C(u)=\sum_{i<j}C_{ij}^{(\rho)}\overline{R_{ij}}(u),
\]
并定义两个多项式
\[
P(u)=4H_\rho\overline{A_x}(u)-12H_\rho\overline{\delta\Delta}(u),
\]
\[
Q(u)=-2\mathcal R_C(u)+4S_\rho\overline{\delta\Delta}(u).
\]
则第 102.6 节的二阶积分核经过分割变量平均后，严格化为
\[
\boxed{\langle\mathcal I_\rho^{(2)}\rangle_x
=\frac6{16\pi^2}\int_0^1du\,u(1-u)
\left[\frac{P(u)}{\Delta(u)}+
\frac{Q(u)}{\Delta(u)^2}\right],}
\]
其中
\[
\Delta(u)=m_1^2+(m_2^2-m_1^2)u.
\]
由于 \(\overline{A_x}\)、\(\overline{\delta\Delta}\) 和所有 \(\overline{R_{ij}}\) 均至多为 \(u\) 的二次多项式，故可写成
\[
P(u)=\sum_{k=0}^2p_k u^k,\qquad
Q(u)=\sum_{k=0}^2q_k u^k,
\]
其中 \(p_k,q_k\) 仍是 \(Q_1,Q_2,Q_3,d_{12},d_{13},d_{23}\) 的线性组合，系数由上面给出的参数平均多项式和 \(H_\rho,S_\rho,C_{ij}^{(\rho)}\) 唯一确定。

因此定义
\[
J_{n,k}(m_1^2,m_2^2)=\int_0^1du\,
\frac{u^k(1-u)}{[m_1^2+(m_2^2-m_1^2)u]^n},
\]
即可把该路径的二阶积分核写成有限和：
\[
\boxed{\langle\mathcal I_\rho^{(2)}\rangle_x
=\frac6{16\pi^2}\sum_{k=0}^2
\left[p_kJ_{1,k}(m_1^2,m_2^2)+
q_kJ_{2,k}(m_1^2,m_2^2)\right].}
\]
这里 \(p_k,q_k\) 不包含 \(1/(16\pi^2)\) 或 Feynman 参数化因子 6；整体因子仅在框中出现一次。由于分子多项式次数为二，当前核只需要 \(k=0,1,2\)；第 102.9.2 节给出的一般 \(k\leq3\) 积分定义仍可作为更高次数项的通用基础。

对于 \(d=m_2^2-m_1^2\ne0\)，令 \(a=m_1^2\)、\(b=m_2^2\)，并定义
\[
L_{n,j}=\int_0^1du\,\frac{u^j}{(a+du)^n}
=\frac1{d^{j+1}}\sum_{r=0}^j\binom jr(-a)^{j-r}\Phi_{r-n}(a,b),
\]
\[
\Phi_p(a,b)=\begin{cases}
(b^{p+1}-a^{p+1})/(p+1),&p\ne-1,\\
\ln(b/a),&p=-1,
\end{cases}
\]
则
\[
\boxed{J_{n,k}=L_{n,k}-L_{n,k+1}.}
\]
等质量极限为
\[
\boxed{J_{n,k}(m^2,m^2)=\frac1{m^{2n}(k+1)(k+2)}.}
\]
这完成了**单条内部质量路径的二阶参数积分到有限个解析质量比积分的化简**，但还没有完成不同外腿循环、内部态路径、图形整体因子以及 EFT 侧减法的求和。因此此处仍不能将 \(p_k,q_k\) 解释为最终 Wilson 系数。

### 103.3 本节结论与后续计算顺序

1. 已用显式 Gram 矩阵和 \((u,z,w)\) 参数化独立核对参数平均，修正 \(\overline{R_{13}}\) 与 \(\overline{R_{34}}\) 中的两处 \(d_{23}\) 多项式。
2. 已把二阶积分核组织成 \(P(u)/\Delta+Q(u)/\Delta^2\)，并化为有限个 \(J_{n,k}\) 的组合。
3. 下一步应由符号代数程序显式展开 \(p_k,q_k\) 对六个外动量不变量的系数，再逐个循环和内部态路径求和；之后才可与 EFT 泡图、接触图和反项进行同一方案下的差分匹配。
4. 本节不将尚未核验的整体 Wick 符号或最终 Wilson 系数写成确定结论。



## 第 104 节：外动量不变量系数的显式投影

本节将第 103 节定义的 \(P(u)\)、\(Q(u)\) 完全展开为六个独立 Euclidean 外动量不变量的多项式系数。此处继续使用
\[
Q_i=q_i^2,\qquad d_{ij}=q_i\cdot q_j,
\]
以及
\[
P(u)=4H_\rho\overline{A_x}(u)-12H_\rho\overline{\delta\Delta}(u),\qquad
Q(u)=-2\sum_{i<j}C_{ij}^{(\rho)}\overline{R_{ij}}(u)+4S_\rho\overline{\delta\Delta}(u),
\]
其中 \(S_\rho=\sum_{i<j}C_{ij}^{(\rho)}\)。这里的 \(Q(u)\) 是积分核多项式，不是外动量平方 \(Q_i\)。

写成
\[
P(u)=p_0+p_1u+p_2u^2,\qquad Q(u)=q_0+q_1u+q_2u^2,
\]
则对 \(P\) 的显式展开为
\[
\boxed{\begin{aligned}
p_0&=-H_\rho(Q_1+d_{12}+d_{13}-d_{23}),\\
p_1&=-H_\rho(7Q_1+4Q_2+9Q_3+2d_{12}+12d_{13}+6d_{23}),\\
p_2&=4H_\rho(2Q_1+Q_2+2Q_3+d_{12}+3d_{13}+d_{23}).
\end{aligned}}
\]

为避免在 \(q_k\) 中重复书写 \(S_\rho\)，已使用其定义将它消去。得到
\[
\boxed{\begin{aligned}
q_0={}&Q_1(C_{14}+C_{24}+C_{34})
+Q_2(C_{12}+C_{13}+C_{24}+C_{34})\\
&+d_{12}(C_{12}+C_{13}+C_{14}+2C_{24}+2C_{34})\\
&+d_{13}(-C_{13}-C_{23}+C_{34})
+d_{23}(C_{13}-C_{23}+C_{34}),\\[3pt]
q_1={}&Q_1(2C_{12}+2C_{13}+C_{14}+2C_{23}+C_{24}+C_{34})\\
&+Q_2(C_{12}+C_{13}+C_{14}+C_{23}+C_{24}+C_{34})\\
&+Q_3(2C_{12}+3C_{13}+2C_{14}+3C_{23}+2C_{24}+3C_{34})\\
&+d_{12}(-C_{14}+C_{23})\\
&+d_{13}(3C_{12}+4C_{13}+2C_{14}+4C_{23}+2C_{24}+3C_{34})\\
&+d_{23}(2C_{12}+2C_{13}+C_{14}+3C_{23}+2C_{24}+2C_{34}),\\[3pt]
q_2={}&-(2Q_1+Q_2+2Q_3+d_{12}+3d_{13}+d_{23})S_\rho.
\end{aligned}}
\]
这里为简洁起见省略了 \((\rho)\) 上标，但所有 \(C_{ij}\) 均指同一内部路径的系数。

### 104.1 投影系数与质量比积分的最终组合

代入第 103 节定义的
\[
J_{n,k}(a,b)=\int_0^1du\,\frac{u^k(1-u)}{[a+(b-a)u]^n},\qquad a=m_1^2,\quad b=m_2^2,
\]
单路径积分核成为
\[
\boxed{
\langle\mathcal I_\rho^{(2)}\rangle_x
=\frac6{16\pi^2}\sum_{k=0}^{2}
\left[p_kJ_{1,k}(m_1^2,m_2^2)+q_kJ_{2,k}(m_1^2,m_2^2)\right].
}
\]
因此，对每一个独立外动量不变量，其系数都能直接由上面的 \(p_k,q_k\) 和解析 \(J_{n,k}\) 组合读出。等质量极限 \(m_1=m_2=m\) 时，
\[
J_{1,k}=\frac1{m^2(k+1)(k+2)},\qquad
J_{2,k}=\frac1{m^4(k+1)(k+2)}.
\]
这也提供了一个独立数值核验点：对一般质量比的解析式取 \(m_2\to m_1\) 极限，必须回到这两个表达式，而不能留下 \((m_2^2-m_1^2)^{-r}\) 的假奇点。

### 104.2 一致性检查与限制

1. **参数多项式检查：** 用显式向量 \(r_i=(0,0,0),(0,-1,0),(0,-1,-1),(1,0,0)\) 表示 \((q_1,q_2,q_3)\) 基底中的路由，并以 Gram 矩阵 \(G_q\) 计算 \(t_i\cdot t_j\)。逐项对 \(z,w\in[0,1]\) 积分后，六个 \(\overline{R_{ij}}\) 与第 102.9.1 节列出的多项式一致。
2. **角平均检查：** 对 \(G\) 的三个乘积项分别使用 \(\langle(K\cdot a)(K\cdot b)\rangle=K^2(a\cdot b)/4\)，合并后得到 \(A_x=R_{12}-R_{13}/2+R_{14}+R_{23}-R_{24}/2+R_{34}\)。这一步纠正了旧稿第 103.1 之后曾出现的过短表达式；本节投影系数均按此完整公式计算。
3. **次数检查：** \(P,Q\) 对 \(u\) 均为二次多项式，因此只需要 \(k=0,1,2\) 的 \(J_{n,k}\)。
4. **结论边界：** 当前完成的是一条内部质量路径的参数积分与外动量系数投影。还未将全部循环类、所有允许内部态路径、图形组合因子及 Wick 旋转统一求和，也未完成 EFT 侧泡图、接触图和反项的同方案相减。因此本节结果仍不是最终 Wilson 系数。


## 第 105 节：代入内部路径的耦合与质量因子

为使单路径结果可以直接用于后续循环求和，现将第 104 节的通用系数进一步代入路径 \(\rho=(1,2,1,2)\) 的具体耦合。定义简写
\[
A=c_Lc_R,\qquad B=s_Ls_R,
\]
以及
\[
\begin{aligned}
C_x&=a^2b^2m_1m_2AB(A^2+B^2),\\
C_y&=a^2b^2m_1^2(A^4+B^4),\\
C_z&=2a^2b^2m_2^2A^2B^2.
\end{aligned}
\]
则
\[
C_{12}=C_{14}=C_{23}=C_{34}=C_x,\qquad C_{13}=C_y,\qquad C_{24}=C_z,
\]
并且
\[
H_\rho=2a^2b^2A^2B^2,\qquad S_\rho=4C_x+C_y+C_z.
\]

由第 104 节结果直接得到
\[
\boxed{\begin{aligned}
q_0={}&Q_1(2C_x+C_z)+Q_2(2C_x+C_y+C_z)\\
&+d_{12}(4C_x+C_y+2C_z)-d_{13}C_y+d_{23}C_y,\\[3pt]
q_1={}&Q_1(6C_x+2C_y+C_z)+Q_2(4C_x+C_y+C_z)\\
&+Q_3(10C_x+3C_y+2C_z)\\
&+d_{13}(12C_x+4C_y+2C_z)\\
&+d_{23}(8C_x+2C_y+2C_z),\\[3pt]
q_2={}&-(4C_x+C_y+C_z)(2Q_1+Q_2+2Q_3+d_{12}+3d_{13}+d_{23}).
\end{aligned}}
\]
这里 \(d_{12}\) 在 \(q_1\) 中的系数恰好抵消，是该特定路径满足 \(C_{12}=C_{14}=C_{23}=C_{34}\) 后的代数结果；不应推广到其他路径。

相应的 \(p_k\) 为
\[
\boxed{\begin{aligned}
p_0&=-2a^2b^2A^2B^2(Q_1+d_{12}+d_{13}-d_{23}),\\
p_1&=-2a^2b^2A^2B^2(7Q_1+4Q_2+9Q_3+2d_{12}+12d_{13}+6d_{23}),\\
p_2&=8a^2b^2A^2B^2(2Q_1+Q_2+2Q_3+d_{12}+3d_{13}+d_{23}).
\end{aligned}}
\]
因此，本路径的完整投影积分仍是
\[
\boxed{
\langle\mathcal I_\rho^{(2)}\rangle_x
=\frac6{16\pi^2}\sum_{k=0}^{2}
\left[p_kJ_{1,k}(m_1^2,m_2^2)+q_kJ_{2,k}(m_1^2,m_2^2)\right],
}
\]
其中 \(p_k,q_k\) 已在本节显式给出。该表达式保留了六个独立外动量不变量，因此可以直接按目标 EFT 算符的动量结构投影，而无需再进行 \(z,w\) 参数积分。

### 105.1 本路径结果的交叉检查

- **耦合阶数：** \(H_\rho\) 与各 \(C_{ij}\) 均为 \(a^2b^2\) 阶，符合该四顶点闭合路径的耦合乘积。
- **质量维数：** \(H_\rho\) 无质量维数；\(C_x,C_y,C_z\) 的质量维数均为二。因此 \(p_k\) 具有质量维数二，\(q_k\) 具有质量维数四，使 \(p_kJ_{1,k}\) 与 \(q_kJ_{2,k}\) 均为无量纲。
- **等质量极限：** 令 \(m_2=m_1=m\)，应使用 \(J_{n,k}=1/[m^{2n}(k+1)(k+2)]\) 计算，而不要把 \(b-a=0\) 直接代入含 \((b-a)^{-r}\) 的中间表达式。
- **范围限制：** 以上仍只对应路径 \((1,2,1,2)\) 及当前固定路由。要得到物理振幅，仍需将外腿排列、内部质量路径、图形权重和 UV–EFT 差分在统一的 Minkowski/Wick 约定下求和。


## 第 106 节：向全部内部态路径推广时的分母分类

不能把第 105 节的一维质量比积分公式直接用于全部 16 条内部态路径。原因是只有当第一、第三条传播子的质量相同，且第二、第四条传播子的质量相同时，分母才仅依赖于分割变量 \(u=x_1+x_3\)。其余路径仍依赖 \(z,w\)，必须保留三维参数积分。

### 106.1 一般路径的分母

采用同一分割变量
\[
x_1=uz,\quad x_3=u(1-z),\quad
x_2=(1-u)w,\quad x_4=(1-u)(1-w),
\]
对一般传播子质量序列 \((\mu_1,\mu_2,\mu_3,\mu_4)\)，分母函数是
\[
\boxed{
\Delta(u,z,w)=u\big[z\mu_1^2+(1-z)\mu_3^2\big]
+(1-u)\big[w\mu_2^2+(1-w)\mu_4^2\big].
}
\]
它只在
\[
\mu_1^2=\mu_3^2,\qquad \mu_2^2=\mu_4^2
\]
时与 \(z,w\) 无关，进而降为
\[
\Delta(u)=u\mu_1^2+(1-u)\mu_2^2.
\]
因此一维 \(J_{n,k}\) 公式的适用条件是质量配对条件，而不是“所有四传播子圈图”都满足的普遍性质。

### 106.2 96 条记录中的一维可约子集

对已有六循环、每循环 16 条路径的质量账本逐条检查 \(\mu_1=\mu_3\) 与 \(\mu_2=\mu_4\)，结果是：每个循环类均有 4 条满足条件的路径，合计 \(6\times4=24\) 条；剩余 \(6\times12=72\) 条必须保留 \(u,z,w\) 三个参数。

以循环 \(h_1-h_2-s_1-s_2\) 为例：

| 内部路径 | 传播子质量序列 | 参数分母 |
|---|---|---|
| \((1,1,1,1)\) | \((m_1,m_1,m_1,m_1)\) | 仅依赖 \(u\)，等质量 |
| \((1,2,1,2)\) | \((m_2,m_1,m_2,m_1)\) | 仅依赖 \(u\)，可用第 103–105 节的 \(J_{n,k}\) |
| \((2,1,2,1)\) | \((m_1,m_2,m_1,m_2)\) | 仅依赖 \(u\)，可用交换 \(m_1\leftrightarrow m_2\) 后的形式 |
| \((2,2,2,2)\) | \((m_2,m_2,m_2,m_2)\) | 仅依赖 \(u\)，等质量 |
| 其余 12 条 | 至少一组 \(\mu_1\ne\mu_3\) 或 \(\mu_2\ne\mu_4\) | 一般依赖 \(u,z,w\) |

上述分类由质量账本中的 96 条路径记录逐项检查得到；它只分类分母的参数维数，不表示 24 条一维路径具有相同的分子权重或可以彼此合并。

### 106.3 一般三维积分核

对于任意路径，保持已核验的分子角平均结构，并定义路径相关的
\[
\begin{aligned}
P_\rho(u,z,w)&=4H_\rho A_x(u,z,w)-12H_\rho\delta\Delta(u,z,w),\\
Q_\rho(u,z,w)&=-2\sum_{i<j}C_{ij}^{(\rho)}R_{ij}(u,z,w)
+4S_\rho\delta\Delta(u,z,w).
\end{aligned}
\]
则其二阶积分核统一写为
\[
\boxed{
\mathcal I_\rho^{(2)}=\frac6{16\pi^2}
\int_0^1du\int_0^1dz\int_0^1dw\,u(1-u)
\left[\frac{P_\rho(u,z,w)}{\Delta(u,z,w)}
+\frac{Q_\rho(u,z,w)}{\Delta(u,z,w)^2}\right].
}
\]
这里 \(A_x\)、\(\delta\Delta\) 与 \(R_{ij}\) 必须由该循环的实际外动量路由计算，不能将 \(h_1-h_2-s_1-s_2\) 的不变量映射原样套到其他五个循环上。因子 6 来自四分母 Feynman 参数恒等式，参数平均的 Jacobian 是 \(u(1-u)\)；本式不应再重复乘以另一个 \(\Gamma(4)=6\)。

### 106.4 下一阶段计算顺序

1. 对每个循环类固定外腿顺序，构造其路由向量 \(r_i\) 和外动量 Gram 矩阵；逐项生成 \(R_{ij}\)、\(A_x\) 与 \(\delta\Delta\)。
2. 从原始顶点矩阵迹为每条路径计算 \(H_\rho,C_{ij}^{(\rho)},M_\rho\)，不从旧候选 \(B^{(1,2,3)}\) 反推这些系数。
3. 对 24 条分母可约路径使用一维解析积分；对 72 条一般路径保留三维积分，必要时用数值积分与解析极限互相验证。
4. 在所有 96 条 UV 路径完成后，再按六个循环类各计一次的规则求和，最后单独核验整体 Wick 因子，并计算 EFT 泡图、接触图与反项，进行 UV–EFT 差分。

**当前状态：** 已完成一条代表路径的显式系数投影，并明确了把它推广到 96 条路径时的积分维数分类。尚未完成全部路径的原始迹、三维积分和最终匹配；旧候选核 CSV 只能作为对照材料，不能直接替代本节修正后的核。

## 第 107 节：当前循环类中其余三条一维可约路径的显式积分核

本节继续处理循环顺序固定为 \(h_1-h_2-s_1-s_2\) 的路径。第 105 节已经给出路径 \(1212\) 的显式核；本节补齐 \(1111\)、\(2121\)、\(2222\)，使该循环类中满足质量配对条件的四条路径都具有可直接代入的一维表达式。以下仍是单路径积分核，尚未包含闭合费米子圈整体符号、外腿排列求和及 EFT 减法。

### 107.1 共用外动量投影

沿用第 104–105 节的路由与不变量
\[
Q_i=q_i^2,\qquad d_{ij}=q_i\cdot q_j,
\]
以及
\[
P=a^2b^2c_L^2c_R^2s_L^2s_R^2,
\qquad T=a^2b^2c_Lc_Rs_Ls_R(c_L^2c_R^2+s_L^2s_R^2).
\]
这四条可约路径均有 \(H_\rho=2P\)，因此 \(P(u)\) 的多项式系数相同：
\[
\begin{aligned}
p_0&=-2P(Q_1+d_{12}+d_{13}-d_{23}),\\
p_1&=-2P(7Q_1+4Q_2+9Q_3+2d_{12}+12d_{13}+6d_{23}),\\
p_2&=8P(2Q_1+Q_2+2Q_3+d_{12}+3d_{13}+d_{23}).
\end{aligned}
\]
差异来自 \(Q(u)\) 的系数以及每条路径自己的 \(\Delta(u)\)。这里 \(P\) 是耦合组合符号，不要与第 103 节的多项式 \(P(u)\) 混淆。

### 107.2 路径 \(1111\)：质量 \(m_1\) 的等质量路径

该路径的质量序列是 \((m_1,m_1,m_1,m_1)\)，并且
\[
C_{12}=C_{13}=C_{14}=C_{23}=C_{24}=C_{34}=C_1,
\qquad C_1=2Pm_1^2,
\]
故 \(S_\rho=6C_1\)，而 \(\Delta(u)=m_1^2\)。代入一般投影式，得到
\[
\begin{aligned}
q_0&=C_1(3Q_1+4Q_2+7d_{12}-d_{13}+d_{23}),\\
q_1&=3C_1(3Q_1+2Q_2+5Q_3+6d_{13}+4d_{23}),\\
q_2&=-6C_1(2Q_1+Q_2+2Q_3+d_{12}+3d_{13}+d_{23}).
\end{aligned}
\]
因此该路径的参数积分为
\[
\boxed{
\langle\mathcal I_{1111}^{(2)}\rangle_x
=\frac6{16\pi^2}\sum_{k=0}^2\left[
\frac{p_k}{m_1^2(k+1)(k+2)}+
\frac{q_k}{m_1^4(k+1)(k+2)}\right].
}
\]
这里使用了等质量极限 \(J_{n,k}=1/[m^{2n}(k+1)(k+2)]\)，未使用含 \((m_2^2-m_1^2)^{-r}\) 的非简并公式。

### 107.3 路径 \(2121\)：交替质量路径

该路径质量序列为 \((m_1,m_2,m_1,m_2)\)，所以
\[
\Delta(u)=u m_1^2+(1-u)m_2^2.
\]
从路径系数表读取
\[
C_{12}=C_{14}=C_{23}=C_{34}=C_x,\quad C_{13}=C_y,\quad C_{24}=C_z,
\]
其中本路径的具体系数是
\[
C_x=Tm_1m_2,\qquad C_y=2Pm_2^2,\qquad C_z=2Pm_1^2,
\qquad S_\rho=4C_x+C_y+C_z.
\]
因此其 \(Q(u)\) 系数为
\[
\begin{aligned}
q_0={}&2C_x(Q_1+Q_2+2d_{12})
+C_y(Q_1+Q_2+2d_{12})\\
&+C_z(Q_2+d_{12}-d_{13}+d_{23}),\\[2pt]
q_1={}&C_x(6Q_1+4Q_2+10Q_3+12d_{13}+8d_{23})\\
&+C_y(Q_1+Q_2+2Q_3+2d_{13}+2d_{23})\\
&+C_z(2Q_1+Q_2+3Q_3+4d_{13}+2d_{23}),\\[2pt]
q_2={}&-(4C_x+C_y+C_z)(2Q_1+Q_2+2Q_3+d_{12}+3d_{13}+d_{23}).
\end{aligned}
\]
其积分表达式为
\[
\boxed{
\langle\mathcal I_{2121}^{(2)}\rangle_x
=\frac6{16\pi^2}\sum_{k=0}^2\left[
 p_kJ_{1,k}(m_1^2,m_2^2)+q_kJ_{2,k}(m_1^2,m_2^2)
\right].
}
\]
注意质量次序与路径 \(1212\) 相反；同时 \(C_{13}\) 与 \(C_{24}\) 的质量平方也互换。不能只交换积分分母而保留第 105 节的 \(q_k\)。

### 107.4 路径 \(2222\)：质量 \(m_2\) 的等质量路径

该路径满足
\[
C_{12}=C_{13}=C_{14}=C_{23}=C_{24}=C_{34}=C_2,
\qquad C_2=2Pm_2^2,
\]
且 \(\Delta(u)=m_2^2\)。因此
\[
\begin{aligned}
q_0&=C_2(3Q_1+4Q_2+7d_{12}-d_{13}+d_{23}),\\
q_1&=3C_2(3Q_1+2Q_2+5Q_3+6d_{13}+4d_{23}),\\
q_2&=-6C_2(2Q_1+Q_2+2Q_3+d_{12}+3d_{13}+d_{23}),
\end{aligned}
\]
并有
\[
\boxed{
\langle\mathcal I_{2222}^{(2)}\rangle_x
=\frac6{16\pi^2}\sum_{k=0}^2\left[
\frac{p_k}{m_2^2(k+1)(k+2)}+
\frac{q_k}{m_2^4(k+1)(k+2)}
\right].
}
\]

### 107.5 本循环类的阶段性闭合与边界

对于固定循环 \(h_1-h_2-s_1-s_2\)，四条质量可约路径 \(1111,1212,2121,2222\) 现在均有显式的一维投影核；其中 \(1212\) 由第 105 节给出，其余三条由本节补齐。每条路径仍须与自身质量分母配对后积分，不能在积分前仅按耦合系数相加。

尚未完成的是该循环类另外 12 条三维积分路径，以及其余五个外腿循环类的独立路由、迹系数与参数核。故本节不能被解释为完整四点振幅或 Wilson 系数结果。

## 第 108 节：当前循环类剩余十二条三维路径的分母显式化

本节继续固定循环顺序 \(h_1-h_2-s_1-s_2\)。对尚未满足质量配对条件的十二条路径，先把三维参数分母逐条写成 \((u,z,w)\) 的显式形式。这一步不把一般三维积分错误地压成一维；分子系数仍按路径账本中的 \(H_\rho,C_{ij}^{(\rho)},S_\rho\) 逐条代入。

### 108.1 统一的显式核

沿用
\[
x_1=uz,\quad x_2=(1-u)w,\quad x_3=u(1-z),\quad x_4=(1-u)(1-w),
\]
并定义 \(\delta m^2=m_2^2-m_1^2\)。令 \(\chi_\rho(u,z,w)\) 为该路径中质量为 \(m_2\) 的传播子所对应 Feynman 参数之和，则
\[
\Delta_\rho=m_1^2+\delta m^2\,\chi_\rho.
\]
每条路径的修正后积分核为
\[
\mathcal I_\rho^{(2)}=\frac6{16\pi^2}\int_0^1du\int_0^1dz\int_0^1dw\,u(1-u)
\left[\frac{4H_\rho A_x-12H_\rho\delta\Delta}{\Delta_\rho}
+\frac{-2\sum_{i<j}C_{ij}^{(\rho)}R_{ij}+4S_\rho\delta\Delta}{\Delta_\rho^2}\right].
\]
这里 \(A_x\)、\(\delta\Delta\) 与 \(R_{ij}\) 使用第 102.9 节已核验的同一路由定义；路径只改变 \(\Delta_\rho,H_\rho,C_{ij}^{(\rho)},S_\rho\)，不改变该外腿循环的路由几何。参数积分测度中的 \(u(1-u)\) 和整体因子 6 均只出现一次。

### 108.2 十二条路径的分母

下表给出每条路径的 \(\chi_\rho\)，因此可直接构造其完整分母。表中路径数字依次对应四条传播子的内部态标签。

| 路径 \(\rho\) | \(\chi_\rho\) | \(\Delta_\rho(u,z,w)\) |
|---|---|---|
| \(1112\) | \(u(1-z)\) | \(m_1^2+\delta m^2 u(1-z)\) |
| \(1121\) | \((1-u)w\) | \(m_1^2+\delta m^2(1-u)w\) |
| \(1122\) | \((1-u)w+u(1-z)\) | \(m_1^2+\delta m^2[(1-u)w+u(1-z)]\) |
| \(1211\) | \(uz\) | \(m_1^2+\delta m^2 uz\) |
| \(1221\) | \(uz+(1-u)w\) | \(m_1^2+\delta m^2[uz+(1-u)w]\) |
| \(1222\) | \(uz+(1-u)w+u(1-z)\) | \(m_1^2+\delta m^2[uz+(1-u)w+u(1-z)]\) |
| \(2111\) | \((1-u)(1-w)\) | \(m_1^2+\delta m^2(1-u)(1-w)\) |
| \(2112\) | \(u(1-z)+(1-u)(1-w)\) | \(m_1^2+\delta m^2[u(1-z)+(1-u)(1-w)]\) |
| \(2122\) | \((1-u)w+u(1-z)+(1-u)(1-w)\) | \(m_1^2+\delta m^2[(1-u)w+u(1-z)+(1-u)(1-w)]\) |
| \(2211\) | \(uz+(1-u)(1-w)\) | \(m_1^2+\delta m^2[uz+(1-u)(1-w)]\) |
| \(2212\) | \(uz+u(1-z)+(1-u)(1-w)\) | \(m_1^2+\delta m^2[uz+u(1-z)+(1-u)(1-w)]\) |
| \(2221\) | \(uz+(1-u)w+(1-u)(1-w)\) | \(m_1^2+\delta m^2[uz+(1-u)w+(1-u)(1-w)]\) |

这些表达式也可通过 \(x_1+x_2+x_3+x_4=1\) 做等价化简。例如路径 \(1222\) 的 \(\chi=1-x_4\)，路径 \(2122\) 的 \(\chi=1-x_1\)，路径 \(2212\) 的 \(\chi=1-x_2\)，路径 \(2221\) 的 \(\chi=1-x_3\)。这些等价形式可用于数值实现中的独立一致性检查。

### 108.3 分子权重的路径代入规则

对表中任一路径，分子部分严格按以下替换构造：
\[
P_\rho=4H_\rho A_x-12H_\rho\delta\Delta,
\qquad
Q_\rho=-2(C_{12}R_{12}+C_{13}R_{13}+C_{14}R_{14}+C_{23}R_{23}+C_{24}R_{24}+C_{34}R_{34})+4S_\rho\delta\Delta.
\]
其中 \(H_\rho,S_\rho,C_{ij}^{(\rho)}\) 必须取路径账本中与同一个路径编号对应的行；不能将路径 \(1212\) 的系数沿用给其它路径。常数质量项 \(M_\rho\) 不直接出现在该二阶外动量核中，但在零阶振幅与完整振幅重建时仍须保留。

### 108.4 本节检查与尚未完成的计算

本节的独立检查包括：

1. 十二条路径恰好是当前循环类 16 条路径扣除 \(1111,1212,2121,2222\) 后的补集；
2. 每个 \(\chi_\rho\) 只含对应路径中标记为 \(m_2\) 的参数，且 \(\Delta_\rho\) 在参数单纯形上是四个传播子质量平方的凸组合；
3. 在 \(m_1=m_2=m\) 时，所有路径统一退化为 \(\Delta_\rho=m^2\)，与质量简并极限一致；
4. \(\chi_{1222}=1-x_4\)、\(\chi_{2122}=1-x_1\)、\(\chi_{2212}=1-x_2\)、\(\chi_{2221}=1-x_3\) 与参数和为 1 的恒等式一致。

**进度边界：** 本节完成的是当前循环类十二条一般路径的显式分母和可直接计算的三维积分核定义；尚未对这十二条路径完成三重参数积分，也尚未完成另外五个外腿循环类。当前仍不能据此给出总振幅或最终 Wilson 系数。


## 第 109 节：质量简并极限的三维积分核独立核验

本节对第 108 节的三维参数核做一个可复现的独立检验。取
\[
m_1=m_2=m,\qquad \Delta_\rho(u,z,w)=m^2,
\]
则分母与全部 Feynman 参数无关，三维积分可以先对 \(z,w\) 平均，再对 \(u\) 积分。这个极限适用于当前循环类的全部 16 条路径，且不要求其质量标签交替。

### 109.1 加权参数平均的解析结果

定义
\[
\mathscr A=\int_0^1du\,u(1-u)\overline{A_x}(u),\quad
\mathscr D=\int_0^1du\,u(1-u)\overline{\delta\Delta}(u),
\]
\[
\mathscr R_{ij}=\int_0^1du\,u(1-u)\overline{R_{ij}}(u).
\]
将第 102.9.1 节的多项式逐项积分，得到
\[
\boxed{\begin{aligned}
\mathscr A={}&-\frac{Q_1}{80}+\frac{Q_2}{15}-\frac{Q_3}{80}
+\frac{d_{12}}{15}-\frac{11d_{13}}{120}+\frac{d_{23}}{15},\\
\mathscr D={}&\frac{Q_1}{40}+\frac{Q_2}{30}+\frac{Q_3}{40}
+\frac{d_{12}}{30}+\frac{d_{13}}{60}+\frac{d_{23}}{30}.
\end{aligned}}
\]
六个偏移内积的加权平均为
\[
\boxed{\begin{aligned}
\mathscr R_{12}={}&\frac{Q_1}{60}-\frac{Q_2}{30}+\frac{Q_3}{60}
+\frac{d_{12}}{120}-\frac{d_{13}}{60}+\frac{d_{23}}{120},\\
\mathscr R_{13}={}&\frac{Q_1}{60}-\frac{Q_2}{30}-\frac{Q_3}{40}
+\frac{d_{12}}{120}+\frac{d_{13}}{40}-\frac{3d_{23}}{40},\\
\mathscr R_{14}={}&-\frac{Q_1}{40}+\frac{Q_2}{20}+\frac{Q_3}{60}
+\frac{d_{12}}{20}+\frac{d_{13}}{40}+\frac{d_{23}}{20},\\
\mathscr R_{23}={}&\frac{Q_1}{60}+\frac{Q_2}{20}-\frac{Q_3}{40}
+\frac{d_{12}}{20}+\frac{d_{13}}{40}+\frac{d_{23}}{20},\\
\mathscr R_{24}={}&-\frac{Q_1}{40}-\frac{Q_2}{30}+\frac{Q_3}{60}
-\frac{3d_{12}}{40}+\frac{d_{13}}{40}+\frac{d_{23}}{120},\\
\mathscr R_{34}={}&-\frac{Q_1}{40}-\frac{Q_2}{30}-\frac{Q_3}{40}
-\frac{3d_{12}}{40}-\frac{d_{13}}{10}-\frac{3d_{23}}{40}.
\end{aligned}}
\]
其中 \(Q_i=q_i^2\) 与 \(d_{ij}=q_i\cdot q_j\) 均按同一 Euclidean 约定定义。

### 109.2 任意路径在质量简并极限下的闭式核

记 \(S_\rho=\sum_{i<j}C_{ij}^{(\rho)}\)。代入统一二阶核并执行参数积分后，得到
\[
\boxed{
\mathcal I_{\rho,\,m_1=m_2}^{(2)}=
\frac{6}{16\pi^2}\left[
\frac{4H_\rho\mathscr A-12H_\rho\mathscr D}{m^2}
+\frac{-2\sum_{i<j}C_{ij}^{(\rho)}\mathscr R_{ij}+4S_\rho\mathscr D}{m^4}
\right].}
\]
该式是路径级积分核的质量简并极限，不包含尚待核验的全图整体符号、循环类求和因子或 EFT 减法。它可用作任意路径的连续性检查：先计算非简并参数积分，再令 \(m_2/m_1\to1\)，应趋近此表达式。

### 109.3 三维直接积分与平均后积分的数值交叉检查

使用独立数值脚本直接构造
\[
r_1=0,\quad r_2=-q_2,\quad r_3=-q_2-q_3,\quad r_4=q_1,
\]
从 \(t_i=r_i-\sum_jx_jr_j\) 计算 \(R_{ij}=t_i\cdot t_j\)、\(A_x\) 与 \(\delta\Delta\)，并在 \((u,z,w)\in[0,1]^3\) 上使用 14 点 Gauss–Legendre 张量积求积。测试向量取
\[
q_1=(0.7,-0.2,0.4),\quad q_2=(-0.3,0.8,0.1),\quad q_3=(0.2,0.5,-0.6),
\]
测试权重取
\[
(C_{12},C_{13},C_{14},C_{23},C_{24},C_{34})=(0.8,-0.4,1.2,0.3,-0.7,0.5).
\]
将直接三维积分与上节解析平均结果比较，所得差值为
\[
|\mathscr A_{\rm num}-\mathscr A_{\rm ana}|=6.94\times10^{-18},
\]
\[
|\mathscr D_{\rm num}-\mathscr D_{\rm ana}|=2.78\times10^{-17},
\]
\[
\left|\sum_{i<j}C_{ij}\mathscr R_{ij}^{\rm num}
-\sum_{i<j}C_{ij}\mathscr R_{ij}^{\rm ana}\right|=3.47\times10^{-17}.
\]
这些误差处于双精度舍入量级，支持参数平均多项式及其积分系数在该测试点上相互一致。该测试核验的是路由几何与参数平均，不是完整物理振幅的符号或归一化。

### 109.4 下一步与结论边界

下一步可对非简并质量比 \(m_2/m_1\ne1\) 的十二条三维路径进行数值积分，并将结果与质量简并极限连续性、路径标签交换关系交叉检查。数值积分必须对每条路径使用其自身的 \(\Delta_\rho,H_\rho,C_{ij}^{(\rho)}\)，不能只交换分母而保留其它路径的权重。

**本节完成：** 得到适用于任意路径的质量简并闭式核，并以独立三维求积核验参数平均。**本节未完成：** 非简并三维积分、其余五个外腿循环类、总振幅归一化，以及 UV–EFT 匹配和最终 Wilson 系数。


## 第 110 节：非简并质量下十二条三维路径的数值积分核验

本节对第 108 节当前循环类的十二条非可约路径进行直接三维数值积分。目标是检查积分实现、求积收敛和质量简并连续性；本节采用的参数是数值诊断点，不代表论文模型的物理基准点，也不用于宣称得到最终 Wilson 系数。

### 110.1 数值实现与输入

使用第 102 节的路由
\[
r_1=0,\quad r_2=-q_2,\quad r_3=-q_2-q_3,\quad r_4=q_1,
\]
以及
\[
x_1=uz,\quad x_2=(1-u)w,\quad x_3=u(1-z),\quad x_4=(1-u)(1-w).
\]
每个积分点直接计算
\[
\bar r=\sum_i x_ir_i,\quad t_i=r_i-\bar r,\quad R_{ij}=t_i\cdot t_j,
\]
\[
A_x=R_{12}-\frac12R_{13}+R_{14}+R_{23}-\frac12R_{24}+R_{34},
\quad \delta\Delta=\sum_i x_it_i^2.
\]
对每条路径分别构造
\[
\Delta_\rho=\sum_i x_i\mu_i^2,\quad P_\rho=4H_\rho A_x-12H_\rho\delta\Delta,
\]
\[
Q_\rho=-2\sum_{i<j}C_{ij}^{(\rho)}R_{ij}+4S_\rho\delta\Delta,
\]
并数值计算
\[
I_\rho^{(2)}=\frac6{16\pi^2}\int_0^1du\,dz\,dw\,u(1-u)
\left(\frac{P_\rho}{\Delta_\rho}+\frac{Q_\rho}{\Delta_\rho^2}\right).
\]
采用张量积 Gauss–Legendre 求积。用于测试的欧氏外动量为
\[
q_1=(0.7,-0.2,0.4),\quad q_2=(-0.3,0.8,0.1),\quad q_3=(0.2,0.5,-0.6),
\]
耦合/混合参数取 \(a=0.8,b=1.1,c_L=0.8,s_L=0.6,c_R=0.6,s_R=0.8\)，质量单位取 \(m_1=1\)。路径的 \(H_\rho,S_\rho,C_{ij}^{(\rho)}\) 均从路径账本按相同质量代入，而不是固定使用某一条路径的权重。

### 110.2 非简并质量比 \(m_2/m_1=1.7\) 的逐路径结果

下表给出上述数值诊断点、18 点张量积求积下的路径级积分核。数值单位随输入动量和质量单位而定；这些是积分核数值，不是已匹配的 Wilson 系数。

| 路径 | \(I_\rho^{(2)}\) |
|---|---:|
| 1112 | \( 3.55339859199\times10^{-3}\) |
| 1121 | \(-2.08688284820\times10^{-3}\) |
| 1122 | \(-2.67566681742\times10^{-3}\) |
| 1211 | \( 1.23910297364\times10^{-3}\) |
| 1221 | \(-9.01512245686\times10^{-4}\) |
| 1222 | \(-1.23165860758\times10^{-3}\) |
| 2111 | \(-2.09752880160\times10^{-3}\) |
| 2112 | \(-2.61113745632\times10^{-3}\) |
| 2122 | \( 2.12154349775\times10^{-3}\) |
| 2211 | \(-9.14028689383\times10^{-4}\) |
| 2212 | \(-1.21488977196\times10^{-3}\) |
| 2221 | \( 7.12643915086\times10^{-4}\) |

这十二条路径的数值和为
\[
\sum_{\rho\in\text{12 paths}}I_\rho^{(2)}=-6.10661625969\times10^{-3}.
\]
此和仅用于本节指定输入下的数值诊断；它不包括四条可约路径，也不包括其它五个外腿循环类。

### 110.3 求积阶数收敛

将每个参数方向的 Gauss–Legendre 节点数从 10 提高到 22，所得十二条路径的和及最大单路径绝对值为：

| 每维节点数 | 十二条路径之和 | 最大单路径绝对值 |
|---:|---:|---:|
| 10 | \(-6.106616259656656\times10^{-3}\) | \(3.553398591900735\times10^{-3}\) |
| 14 | \(-6.106616259694621\times10^{-3}\) | \(3.553398591986909\times10^{-3}\) |
| 18 | \(-6.106616259694627\times10^{-3}\) | \(3.553398591986915\times10^{-3}\) |
| 22 | \(-6.106616259694609\times10^{-3}\) | \(3.553398591986904\times10^{-3}\) |

在此测试点上，10 点与 22 点结果的和相差约 \(3.80\times10^{-14}\)，说明该平滑参数积分的数值求积已收敛到双精度精度范围。该收敛检验不替代对路径账本的代数核验，也不检查全图整体符号。

### 110.4 质量简并连续性检查

重新按各质量比代入路径系数，并对同一十二条路径积分，得到：

| \(m_2/m_1\) | 十二条路径之和 | 最大单路径绝对值 |
|---:|---:|---:|
| 1.0000 | \(-1.1679077967147\times10^{-2}\) | \(5.1907013187318\times10^{-3}\) |
| 1.0001 | \(-1.1677910125780\times10^{-2}\) | \(5.1904029179569\times10^{-3}\) |
| 1.0100 | \(-1.1562950055560\times10^{-2}\) | \(5.1609508325594\times10^{-3}\) |
| 1.7000 | \(-6.1066162596946\times10^{-3}\) | \(3.5533985919869\times10^{-3}\) |

从 \(m_2/m_1=1\) 到 1.0001，最大单路径结果变化约为 \(8.17\times10^{-7}\)，相对最大值约 \(1.57\times10^{-4}\)，与该有限质量偏移下的连续变化一致。由于路径权重本身也依赖质量，比较时已同步重新代入 \(H_\rho,S_\rho,C_{ij}^{(\rho)}\)，而不只是改变分母。

### 110.5 本节结论与边界

本节完成了当前外腿循环类十二条非简并三维路径的数值积分示例、求积阶数收敛检查，以及质量简并附近的连续性检查。它表明，在所列输入与当前积分核定义下，数值实现表现稳定。

仍有三项不能越过的边界：

1. 数值积分只检验当前循环类的十二条路径；四条可约路径应按其独立表达式一并合并后再比较。
2. 其余五个外腿循环类必须分别建立正确路由、Dirac 迹和路径权重，不能把当前循环类的 \(R_{ij}\) 直接复用。
3. 在完成全图组合因子、整体符号、EFT 泡图/接触图/反项及同一方案下的 UV–EFT 差分之前，不能将这些路径级积分核称为最终 Wilson 系数。


## 第 111 节：质量简并点合并全部 16 条路径的独立数值闭合检查

### 111.1 检查目标与固定输入

本节将第 110 节的十二条非可约路径与第 107 节的四条可约路径合并，在质量简并点重新逐路径计算当前循环类的全部 16 条路径。该检查专门验证路径划分和求和是否闭合，不将路径级核的和解释为完整物理振幅。

沿用第 110 节的欧氏外动量
\[
q_1=(0.7,-0.2,0.4),\quad q_2=(-0.3,0.8,0.1),\quad q_3=(0.2,0.5,-0.6),
\]
耦合参数
\[
a=0.8,\quad b=1.1,\quad c_L=0.8,\quad s_L=0.6,\quad c_R=0.6,\quad s_R=0.8,
\]
并取 \(m_1=m_2=1\)。逐路径的 \(H_\rho,C_{ij}^{(\rho)},S_\rho\) 从路径账本重新读取；在每个三维积分点直接构造 \(R_{ij},A_x,\delta\Delta\)，而不是用十二条路径之和反推四条可约路径。

### 111.2 逐路径结果

采用每个参数方向 14 点的 Gauss–Legendre 张量积求积，得到：

| 路径 | 质量类别 | \(I_\rho^{(2)}\) |
|---|---|---:|
| 1111 | 可约 | \(+2.919769491786661\times10^{-3}\) |
| 1112 | 三维 | \(+5.190701318731826\times10^{-3}\) |
| 1121 | 三维 | \(-2.919769491786661\times10^{-3}\) |
| 1122 | 三维 | \(-5.190701318731824\times10^{-3}\) |
| 1211 | 三维 | \(+1.642370339129995\times10^{-3}\) |
| 1212 | 可约 | \(+2.919769491786661\times10^{-3}\) |
| 1221 | 三维 | \(-1.642370339129995\times10^{-3}\) |
| 1222 | 三维 | \(-2.919769491786661\times10^{-3}\) |
| 2111 | 三维 | \(-2.919769491786661\times10^{-3}\) |
| 2112 | 三维 | \(-5.190701318731826\times10^{-3}\) |
| 2121 | 可约 | \(+2.919769491786661\times10^{-3}\) |
| 2122 | 三维 | \(+5.190701318731826\times10^{-3}\) |
| 2211 | 三维 | \(-1.642370339129995\times10^{-3}\) |
| 2212 | 三维 | \(-2.919769491786661\times10^{-3}\) |
| 2221 | 三维 | \(+1.642370339129995\times10^{-3}\) |
| 2222 | 可约 | \(+2.919769491786661\times10^{-3}\) |

### 111.3 两个子集与总和

十二条三维路径的和为
\[
\sum_{\rho\in\text{12 paths}}I_\rho^{(2)}
=-1.1679077967146644\times10^{-2}.
\]
四条可约路径的和为
\[
\sum_{\rho\in\text{4 paths}}I_\rho^{(2)}
=+1.1679077967146644\times10^{-2}.
\]
因此全部 16 条路径的合计为
\[
\boxed{\sum_{\rho=1}^{16}I_\rho^{(2)}\simeq 2.6\times10^{-18}\simeq0.}
\]
残差处于双精度数值舍入误差量级。逐路径结果还显示在这个简并测试点存在成对抵消，例如 \(I_{1111}^{(2)}+I_{1121}^{(2)}\simeq0\)、\(I_{1112}^{(2)}+I_{1122}^{(2)}\simeq0\)，以及其它相应路径对。

### 111.4 解释范围与后续检查

这是一个对当前固定路由、当前外动量、当前耦合参数和质量简并点的数值闭合检查。它确认了本次实现中“十二条三维路径 + 四条可约路径”确实覆盖了路径账本的 16 条路径，且在这个测试点总和抵消到数值误差范围。

但该抵消**不能直接推广到非简并质量，也不能单独证明完整 UV 振幅为零**：其它外腿循环类有各自的顶点顺序、路由与 Dirac 迹；整体图形因子、外腿排列求和及 EFT 减法也尚未全部核验。下一步应在非简并质量比下对全部 16 条路径做同样的合并检查，并独立检查内部态标签交换 \(m_1\leftrightarrow m_2\) 的变换关系，再转向第二个外腿循环类。


## 112. 独立重跑：非简并全路径积分与简并极限差异审计

### 112.1 本节目的与计算设置

本节直接从 `six_cycle_path_weight_ledger.csv` 读取当前外腿循环类 `h1-h2-s1-s2` 的 16 条路径系数，对每条路径重新执行三维参数积分；没有复用旧文件中的候选核函数表。数值测试参数为
\[
 a=0.8,\quad b=1.1,\quad c_L=0.8,\ s_L=0.6,\quad c_R=0.6,\ s_R=0.8,
\]
\[
q_1=(0.7,-0.2,0.4),\quad q_2=(-0.3,0.8,0.1),\quad q_3=(0.2,0.5,-0.6).
\]
因此外动量不变量为
\[
 Q_1=0.69,\quad Q_2=0.74,\quad Q_3=0.65,\quad
 d_{12}=-0.33,\quad d_{13}=-0.20,\quad d_{23}=0.28.
\]
采用当前文档定义的路由
\[
 r_1=0,\quad r_2=-q_2,\quad r_3=-q_2-q_3,\quad r_4=q_1,
\]
以及
\[
 x_1=uz,\quad x_2=(1-u)w,\quad x_3=u(1-z),\quad x_4=(1-u)(1-w).
\]
在每个积分点显式计算 \(\bar r=\sum_i x_i r_i\)、\(t_i=r_i-\bar r\)、\(R_{ij}=t_i\cdot t_j\)、\(\delta\Delta=\sum_i x_i r_i^2-\bar r^2\) 和
\[
 A_x=R_{12}-\frac12R_{13}+R_{14}+R_{23}-\frac12R_{24}+R_{34}.
\]
随后使用
\[
 P=4H A_x-12H\delta\Delta,\qquad
 Q=-2\sum_{i<j}C_{ij}R_{ij}+4S\delta\Delta,
\]
\[
 I_\rho^{(2)}=\frac6{16\pi^2}\int_0^1du\,dz\,dw\,u(1-u)
 \left(\frac{P}{\Delta}+\frac{Q}{\Delta^2}\right),\qquad
 \Delta=\sum_i x_i\mu_i^2.
\]
对三个参数使用相同阶数的一维 Gauss–Legendre 节点，形成张量积求积。以下结果仅是该核函数、账本系数和固定外动量点下的数值结果，不包含完整图形的整体因子，也不是匹配系数。

### 112.2 非简并质量比 \(m_2/m_1=1.7\)

取 \(m_1=1,\ m_2=1.7\)。全路径逐项积分如下：

| 路径 | \(I_\rho^{(2)}\) |
|---|---:|
| 1111 | \(+2.919769491786652\times10^{-3}\) |
| 1112 | \(+3.439335338107461\times10^{-3}\) |
| 1121 | \(-2.340868766025365\times10^{-3}\) |
| 1122 | \(-2.809428484506501\times10^{-3}\) |
| 1211 | \(+1.178726794473046\times10^{-3}\) |
| 1212 | \(+1.449858060226074\times10^{-3}\) |
| 1221 | \(-9.784707610512792\times10^{-4}\) |
| 1222 | \(-1.231764112818296\times10^{-3}\) |
| 2111 | \(-2.163891775065400\times10^{-3}\) |
| 2112 | \(-2.641083558714262\times10^{-3}\) |
| 2121 | \(+1.806518782419042\times10^{-3}\) |
| 2122 | \(+2.257644885504786\times10^{-3}\) |
| 2211 | \(-8.821199973162729\times10^{-4}\) |
| 2212 | \(-1.132994115627802\times10^{-3}\) |
| 2221 | \(+7.648403369812056\times10^{-4}\) |
| 2222 | \(+1.010300862209914\times10^{-3}\) |

求积阶数与总和：

| 每个参数方向的阶数 \(N\) | 16 条路径总和 |
|---:|---:|
| 10 | \(+6.463729795275569\times10^{-4}\) |
| 14 | \(+6.463729805829739\times10^{-4}\) |
| 18 | \(+6.463729805830115\times10^{-4}\) |
| 22 | \(+6.463729805830022\times10^{-4}\) |
| 28 | \(+6.463729805830007\times10^{-4}\) |

就当前实现而言，求积已稳定至所显示精度。注意这只能检验数值积分收敛，不能独立检验输入的 \(H,C_{ij},S\) 是否与原始 Dirac 迹完全一致。

### 112.3 内部质量标签交换的初步测试

把系数表达式中的 \(m_1,m_2\) 同时互换，并将每条路径对应的内部质量序列也互换，按相同求积方法计算，得到：

| 每个参数方向的阶数 \(N\) | 标签交换后的 16 路径总和 |
|---:|---:|
| 14 | \(+6.571588147474628\times10^{-4}\) |
| 22 | \(+6.571588147474888\times10^{-4}\) |
| 28 | \(+6.571588147474888\times10^{-4}\) |

该操作得到的数值与原始质量标签下的总和不同。**目前不能据此断言物理振幅违反内部态重标记不变性**：还需要确认标签交换是否同时正确置换了 Yukawa 矩阵的内部指标、路径索引及所有顶点系数。当前结果只表明“直接在账本公式中交换质量符号”的实现不是一个已验证的对称性测试。

### 112.4 与第 111 节简并结果不一致：必须解决的审计项

将同一程序设为 \(m_1=m_2=1\)，得到 16 条路径总和
\[
\sum_{\rho=1}^{16}I_\rho^{(2)}
=+1.820755943734792\times10^{-3},
\]
求积阶数从 14 增至 28 后稳定。这个值不等于第 111 节所记录的约 \(2.6\times10^{-18}\)；而且若干非 1111 路径的逐项值也与第 111 节表格不同。1111 路径本身复现为 \(+2.91976949178665\times10^{-3}\)，因此这不是一个对所有路径都相同的简单整体归一化差异。

由此必须把第 111 节的“全路径在简并点抵消”暂时降级为**尚未独立复现的旧结果**，不能继续用它作为已验证的闭合检查。优先排查顺序：

1. 将账本中每条路径的 \(H,C_{ij}\) 从原始 \(\Gamma_1(\slashed{k}_1+\mu_1)\cdots\Gamma_4(\slashed{k}_4+\mu_4)\) 重新做符号 Dirac 迹，并逐项对照账本；
2. 确认路径字符串 `1 2 1 2` 的内部指标序列和质量序列 \((\mu_1,\mu_2,\mu_3,\mu_4)\) 的映射定义一致；
3. 对四条 \(\mu_1=\mu_3,\mu_2=\mu_4\) 的可约路径，用独立的一维解析积分计算，与三维积分实现逐路径比较；
4. 核对旧第 109–111 节的数值是否使用了同一份路径系数、同一 \(A_x\) 和同一分母展开符号。

在上述差异消除前，不应把本节总和解释成 Wilson 系数，也不应继续推进其它循环类的最终求和。当前最可靠的结论仅是：本节三维积分数值本身已收敛，但路径系数/路径映射与既有简并核验之间存在实质性不一致，需先做代数层面的独立复核。

---

## 第 113 节：第 112.4 节差异的复核与更正

### 113.1 更正说明

第 112.4 节把一项错误的中间诊断写成了“简并点总和为非零”，并据此怀疑第 111 节的抵消结果。重新从 `six_cycle_path_weight_ledger.csv` 读取 16 条路径，统一使用路径记录中的传播子质量序列 `m_1/m_2`，并逐点构造同一套 \(R_{ij},A_x,\delta\Delta,\Delta,P,Q\) 后，**没有复现第 112.4 节所报的简并点差异**。因此，第 112.4 节关于“第 111 节简并抵消未能复现”的判断应撤回。

本次复算的数值实现采用向量化张量积 Gauss–Legendre 求积，并显式使用路径账本中的 `edge_masses` 列决定每条传播子的质量。固定输入仍为
\[
(a,b,c_L,c_R,s_L,s_R)=(0.8,1.1,0.8,0.6,0.6,0.8),
\]
\[
q_1=(0.7,-0.2,0.4),\quad q_2=(-0.3,0.8,0.1),\quad q_3=(0.2,0.5,-0.6).
\]
这里的数值只检查此前定义的单路径二阶核，不包含图形整体因子，也不构成 Wilson 系数。

### 113.2 质量简并与连续性检查

取每个参数方向的 Gauss–Legendre 阶数 \(N=22\)，16 条路径总和及单路径绝对值最大值为：

| \(m_1\) | \(m_2\) | 16 路径总和 | \(\max_\rho |I_\rho^{(2)}|\) |
|---:|---:|---:|---:|
| 1 | 1 | \(4.55\times10^{-18}\) | \(5.190701318732\times10^{-3}\) |
| 1 | 1.0001 | \(3.935670474416\times10^{-11}\) | \(5.190350168944\times10^{-3}\) |
| 1 | 1.01 | \(3.858230799903\times10^{-7}\) | \(5.155769429905\times10^{-3}\) |
| 1 | 1.7 | \(6.463729805830\times10^{-4}\) | \(3.439335338107\times10^{-3}\) |

在 \(m_1=m_2=1\) 时，逐路径结果与第 111.2 节的表格一致到所显示精度；全路径总和与零的差异为浮点舍入误差量级。质量比接近 1 时，总和连续趋近零。这纠正了第 112.4 节的错误诊断。

收敛性复核（16 路径总和）：

| 每个参数方向的阶数 \(N\) | \(m_1=1,m_2=1\) | \(m_1=1,m_2=1.7\) |
|---:|---:|---:|
| 10 | \(6.94\times10^{-18}\) | \(6.463729795276\times10^{-4}\) |
| 14 | \(2.60\times10^{-18}\) | \(6.463729805830\times10^{-4}\) |
| 18 | \(5.20\times10^{-18}\) | \(6.463729805830\times10^{-4}\) |
| 22 | \(4.55\times10^{-18}\) | \(6.463729805830\times10^{-4}\) |
| 28 | \(4.34\times10^{-18}\) | \(6.463729805830\times10^{-4}\) |

### 113.3 为什么简并点抵消不证明一般情形抵消

账本系数的符号求和显示 \(\sum_\rho H_\rho=0\)，且除 \(C_{13}\) 外的 \(\sum_\rho C_{ij}^{(\rho)}\) 在该循环类中为零。\(\sum_\rho C_{13}^{(\rho)}\) 一般并不恒等于零；其在本次测试点、简并质量下恰好消失，是因为所选角参数满足
\[
c_Lc_R=s_Ls_R=0.48.
\]
所以这里的简并抵消是**给定测试参数下的数值闭合检查**，不能提升为任意混合角、任意质量下的普遍恒等式。

质量互换测试也需谨慎解释。仅把数值输入中的 \(m_1,m_2\) 交换、而保持 Yukawa 矩阵元素和路径定义不变，并不是完整的内部态重标记变换；该操作下总和从 \(6.463729805830\times10^{-4}\) 变为约 \(6.571588147475\times10^{-4}\)，不能单凭这个差异宣称理论违反重标记不变性。真正的标签重标记还必须同时置换 Yukawa 矩阵的内部指标及路径标签。

### 113.4 当前状态与下一项核验

- **已更正：** 第 112.4 节关于简并点不一致的判断无效；第 111 节的简并点路径表可由当前统一实现复现。
- **已数值核验：** 本循环类的 16 路径总和在 \(m_2/m_1=1.7\) 时为 \(6.463729805830\times10^{-4}\)，且张量积求积收敛。
- **仍未完成：** 从原始 Dirac 矩阵迹独立重建每条路径的 \(H_\rho,C_{ij}^{(\rho)},M_\rho\)，并核对所有路径账本。当前积分复算沿用了已有账本系数，因此不能替代原始迹的独立代数审计。
- **仍未完成：** 完整 UV–EFT 匹配，包括所有外腿排列、图形整体因子、EFT 泡图与接触图、反项及指定算符基底投影。

后续应继续做原始 Dirac 迹逐路径核验，而不是把本节的数值积分结果直接解释为匹配系数。


## 第 114 节：原始 Dirac 迹的独立数值审计

### 114.1 审计方法

为避免继续只沿用路径账本，本节直接构造四维 Euclidean Clifford 矩阵 \(\gamma_\mu\)，并按
\[
\Gamma_r=(Y_{\phi_r})_{a_ra_{r+1}}P_R+(Y_{\phi_r})_{a_{r+1}a_r}P_L,
\qquad (\phi_1,\phi_2,\phi_3,\phi_4)=(h,h,s,s)
\]
计算
\[
T_\rho=\operatorname{tr}_D[\Gamma_1(\slashed k_1+\mu_1)\Gamma_2(\slashed k_2+\mu_2)\Gamma_3(\slashed k_3+\mu_3)\Gamma_4(\slashed k_4+\mu_4)].
\]
对每个路径取 100 组独立随机四维向量，直接计算矩阵迹，再将结果拟合到由四动量四次项、六个两两点积项、一个 Levi-Civita 项及常数项组成的线性基底。这样不需要调用账本中的 \(H_\rho,C_{ij}^{(\rho)},M_\rho\) 来生成迹本身；账本系数只在最后一步用于比较。

对每个测试参数组，检查当前循环类 `h1-h2-s1-s2` 的全部 16 条路径。三个参数组为：

| 测试组 | \((a,b)\) | \((c_L,s_L)\) | \((c_R,s_R)\) | \((m_1,m_2)\) |
|---|---|---|---|---|
| A | \((0.8,1.1)\) | \((0.8,0.6)\) | \((0.6,0.8)\) | \((1.0,1.7)\) |
| B | \((1.23,0.73)\) | \((0.8,0.6)\) | \((0.8,0.6)\) | \((0.63,1.41)\) |
| C | \((0.67,1.37)\) | \((0.6,0.8)\) | \((0.9,\sqrt{0.19})\) | \((1.8,0.92)\) |

三个测试组均满足 \(c_L^2+s_L^2=c_R^2+s_R^2=1\)。

### 114.2 审计结果

把拟合出的 \(H_\rho,C_{ij}^{(\rho)},M_\rho\) 与路径账本对应值比较，并使用相对缩放误差
\[
\epsilon_\text{fit}=\max_j\frac{|x_j^\text{fit}-x_j^\text{ledger}|}{1+|x_j^\text{ledger}|},
\]
得到全部 16 条路径上的最大误差：

| 测试组 | 16 条路径中的最大缩放误差 |
|---|---:|
| A | \(5.1\times10^{-16}\) |
| B | \(3.5\times10^{-16}\) |
| C | \(6.9\times10^{-16}\) |

这表明，在上述三组独立参数点上，账本的 \(H_\rho,C_{ij}^{(\rho)},M_\rho\) 系数与直接矩阵迹相符，达到双精度舍入误差量级。它是数值独立核验，不等同于已给出所有 96 条路径的符号证明；本节只审计了一个外部循环类的 16 条内部路径。

### 114.3 一个需要保留的细节：迹中还存在奇宇称 Levi-Civita 结构

对一般不对称的左右耦合，原始 Dirac 迹还可能包含
\[
T_\rho^{(\epsilon)}=E_\rho\,\epsilon_{\mu\nu\rho\sigma}
 k_1^\mu k_2^\nu k_3^\rho k_4^\sigma,
\]
所以若把“原始迹”严格写成只有 \(G\)、六个点积和常数的形式，会遗漏这个奇宇称项。独立矩阵迹拟合确实能在一般测试点检测到非零的 \(E_\rho\)。

不过在当前一圈四点图的 Feynman 参数路由下，\(k_i=\ell+r_i\)，且 \(r_i-r_1\) 由三个外部动量张成。于是
\[
\epsilon(k_1,k_2,k_3,k_4)
=\epsilon(\ell,r_2-r_1,r_3-r_1,r_4-r_1),
\]
右侧对移位后的循环动量是线性的；其余三条向量都处于外部动量张成的三维子空间。将循环动量移位为 \(K=\ell+\bar r\) 后，常数项因四个外部方向线性相关而为零，剩余项正比于 \(K\)，在对称 Euclidean 积分中消失。因此这一项不改变本节所用的已积分二阶核，但在原始未积分 Dirac 迹的严格分解中应明确注明，不能说它逐路径恒等于零。

### 114.4 结论与边界

1. 对当前循环类的 16 条内部路径，直接四维矩阵迹与账本的 \(H,C_{ij},M\) 系数在三组不同质量和混合角参数下符合到约 \(10^{-16}\)–\(10^{-15}\) 的数值精度。
2. 原始迹中可能有额外的奇宇称 Levi-Civita 结构；在当前一圈积分路由下它因循环动量奇性而不贡献已积分核。这一点应作为迹分解的限定条件。
3. 本节不构成其他五个外部循环类的核验，也没有验证全振幅的图形组合因子、EFT 侧泡图/接触图、反项或 Wilson 系数。因此下一步应将同一直接矩阵迹审计扩展到其余五个循环类，再做统一的 UV–EFT 相减。

## 第 115 节：其余五个外部循环类的原始 Dirac 迹审计

### 115.1 范围与方法

本节把第 114 节的直接矩阵迹审计扩展到全部六个外部循环类，总计 96 条内部路径。使用四维 Euclidean Clifford 矩阵直接计算
\[
T_\rho=\operatorname{tr}_D[\Gamma_1(\slashed k_1+\mu_1)\Gamma_2(\slashed k_2+\mu_2)\Gamma_3(\slashed k_3+\mu_3)\Gamma_4(\slashed k_4+\mu_4)],
\]
对每条路径取 80 组随机四维 \(k_i\)，并以最小二乘拟合提取 \(G\)、六个 \(k_i\cdot k_j\)、常数以及 Levi-Civita 结构的系数。拟合完成后，才将前八个系数与路径账本的 \(2H_\rho,2C_{ij}^{(\rho)},2M_\rho\) 比较。

统一测试参数为
\[
a=0.83,\quad b=1.17,\quad c_L=0.71,\quad s_L=\sqrt{1-0.71^2},
\]
\[
c_R=0.63,\quad s_R=\sqrt{1-0.63^2},\quad m_1=0.77,\quad m_2=1.39.
\]
这些参数满足两组混合角归一化条件。随机数种子固定为 823，以便复现本次数值审计。

### 115.2 逐循环类结果

误差定义为
\[
\epsilon_{\rm even}=\max_j\frac{|x_j^{\rm fit}-x_j^{\rm ledger}|}{1+|x_j^{\rm ledger}|},
\]
其中 \(x_j\) 遍历 \(H,C_{12},C_{13},C_{14},C_{23},C_{24},C_{34},M\) 对应的八个系数。Levi-Civita 项单独拟合，不错误地要求它为零。

| 外部循环类 | 路径数 | 最大 \(\epsilon_{\rm even}\) | 拟合到非零 Levi-Civita 系数的路径数 | 最大 \(|E_\rho|\) |
|---|---:|---:|---:|---:|
| `h1-h2-s1-s2` | 16 | \(1.84\times10^{-15}\) | 8 | 0.0567674 |
| `h1-h2-s2-s1` | 16 | \(1.24\times10^{-15}\) | 8 | 0.0567674 |
| `h1-s1-h2-s2` | 16 | \(2.45\times10^{-15}\) | 0 | \(2.92\times10^{-15}\) |
| `h1-s1-s2-h2` | 16 | \(7.57\times10^{-16}\) | 8 | 0.0567674 |
| `h1-s2-h2-s1` | 16 | \(2.18\times10^{-15}\) | 0 | \(1.66\times10^{-15}\) |
| `h1-s2-s1-h2` | 16 | \(1.42\times10^{-15}\) | 8 | 0.0567674 |

全部 96 条路径的偶宇称系数均与账本符合到双精度舍入误差量级。表中三组循环类的 \(E_\rho\) 为零到数值精度；另外三组中各有 8 条路径出现非零奇宇称系数。这里的路径数统计阈值为 \(|E_\rho|>10^{-9}\)。

### 115.3 Levi-Civita 项及积分后的含义

拟合中显式加入的奇宇称基底为
\[
\epsilon(k_1,k_2,k_3,k_4)=\det\begin{pmatrix}k_1^T\\k_2^T\\k_3^T\\k_4^T\end{pmatrix}.
\]
因此，非零 \(E_\rho\) 不是偶宇称系数拟合失败，而是原始迹中独立结构的真实存在。采用本问题的一圈路由 \(k_i=\ell+r_i\) 时，外部差向量 \(r_i-r_1\) 只张成至多三维子空间，故
\[
\epsilon(k_1,k_2,k_3,k_4)=\epsilon(K, r_2-r_1,r_3-r_1,r_4-r_1)
\]
在移位后的循环动量 \(K\) 上至多线性。其余分母只依赖 \(K^2\)，对称积分下 \(\int d^4K\,K^\mu f(K^2)=0\)，所以该项不贡献当前一圈积分后的标量核。此结论依赖对称的维数正规化/平移不变积分处方；若在未积分的被积函数层面工作，仍必须保留此项。

### 115.4 结论与尚未解决的问题

1. 当前六个外部循环类的 96 条内部路径，在一组非简并质量和非对称混合角参数下，直接矩阵迹提取的 \(H,C_{ij},M\) 系数均与账本相符，最大缩放误差约为 \(2.5\times10^{-15}\)。这是对账本的独立数值审计，而不是符号恒等式证明。
2. 原始迹中确实有部分路径带有 Levi-Civita 项；其在本问题的一圈对称循环积分下消失，但不能在未积分迹表达式中直接删掉。
3. 本节没有核验完整图形的整体符号、排列权重或 EFT 侧。下一阶段应从统一的有效作用量/费曼规则独立确定整体组合因子，再计算 EFT 泡图、接触图与反项，在同一 IR 方案和减除方案下相减。完成这些步骤之前，不应报告最终 Wilson 系数。

## 第 116 节：四阶行列式展开与费曼图整体因子的独立核对

### 116.1 四阶项与排列计数

采用 Minkowski 有效作用量约定
\[
\Gamma_f=-i\,\mathrm{Tr}\ln(A_0-V),
\]
其中 \(A_0\) 是自由 Dirac 算符，\(V\) 是 Yukawa 相互作用算符。忽略与外部标量无关的常数项，利用
\[
\ln(1-X)=-\sum_{n=1}^{\infty}\frac{X^n}{n}
\]
可得
\[
\Gamma_f= i\sum_{n=1}^{\infty}\frac1n\mathrm{Tr}[(A_0^{-1}V)^n].
\]
故四阶项为
\[
\boxed{\Gamma_f^{(4)}=\frac{i}{4}\mathrm{Tr}[(A_0^{-1}V)^4]}. 
\]

对四个带标签的外部插入 \(h_1,h_2,s_1,s_2\) 求四次泛函导数，会产生 \(4!=24\) 个有序排列。迹的循环性使每个循环类的四种循环移位等价，因此循环类数为
\[
\frac{4!}{4}=6.
\]
这六类应各计一次。这里的 \(1/4\) 正好与四种循环起始位置的重复计数抵消；将六个循环类列出后，不应再整体乘一次 \(1/4\)。这一计数以四个外腿均带不同标签为前提，即使 \(h_1,h_2\) 属于同一种标量场也仍可按不同外部动量标签处理。

### 116.2 闭合费米子环负号

在行列式方法中，闭合费米子环的负号已经编码在 Grassmann 积分产生的 \(-i\,\mathrm{Tr}\ln\) 中。因此使用上面的行列式展开时，不应再额外乘一次“闭合费米子环负号”。

用普通费曼规则独立核对时，若四个 Yukawa 顶角均按 \(-iV_j\) 书写，四条费米子传播子写成 \(i(\slashed k_j+\mu_j)/(k_j^2-\mu_j^2+i\epsilon)\)，则显式的顶角与传播子因子为
\[
(-i)^4 i^4=+1.
\]
再乘闭合费米子环的 \(-1\)，得到在尚未执行动量积分和 Wick 转动前的整体图形因子 \(-1\)：
\[
 i\mathcal M_{\rm loop}
 =-\int\frac{d^4\ell}{(2\pi)^4}
 \frac{T_\rho(\ell)}{\prod_{j=1}^4(k_j^2-\mu_j^2+i\epsilon)}
\]
这里公式只表示显式 Feynman 规则因子；分子 \(T_\rho\)、分母及后续 Wick 转动必须按同一约定处理。特别地，不能把这个显式 \(-1\) 再无条件乘到已由行列式方法得到的结果上。

### 116.3 两种方法如何比较

比较行列式方法和图形方法时，应把下列对象逐一对应，而不是只比较某个孤立的符号：

1. **循环排列：** 行列式展开的 \(1/4\) 与 24 个带标签排列合并为六个循环类；图形计算中也对这六类各计一次。
2. **费米子环符号：** 行列式法中已隐含；图形法中显式出现一次 \(-1\)。
3. **传播子约定：** 行列式法用代数逆算符 \(A_0^{-1}\)，不另带传播子的 \(i\)；图形法的每条传播子显式带 \(i\)。四条传播子给出 \(i^4=1\)。
4. **动量积分与 Wick 转动：** 两种方法都必须采用相同的 Minkowski 积分定义、分子继续约定与 Wick 转动方向。不能仅凭 \(i^4=1\) 就断言欧氏核的符号；动量分子中的时间分量和分母的 Wick 转动也会贡献符号与 \(i\)。
5. **Feynman 参数：** 四个分母合并使用 \(\Gamma(4)=6\)。若定义的 simplex 平均已经包含归一化因子 6，就不能再把同一个因子乘第二次。

### 116.4 本节能确定与不能确定的结论

可以解析确定的是：四阶行列式展开的系数为 \(i/4\)；对四个带标签外腿求导后得到 24 个排列；按循环性分组为六个循环类；闭合费米子环负号不能在行列式方法之外重复添加。普通图形方法的显式顶角/传播子因子为 \((-i)^4i^4=+1\)，另有一次闭合费米子环负号。

但这还不等于完整的欧氏积分核整体符号已经无歧义。要完成最后核验，仍须把所用的 Minkowski 分子迹逐项 Wick 转动，并与行列式表达式中 \(A_0^{-1}\) 的定义对照。此前各节采用的欧氏分子符号应在这一统一转换完成后再最终锁定。当前尚未计算 EFT 侧泡图、接触图及反项，也未得到可报告的最终 Wilson 系数。

## 第 117 节：从 Minkowski 图形到 Euclidean 核的 Wick 转动符号

### 117.1 固定图形约定

本节固定 Minkowski 度规为 \(g^{\mu\nu}=\mathrm{diag}(+,-,-,-)\)，费米子传播子为
\[
\frac{i(\slashed k_j+\mu_j)}{k_j^2-\mu_j^2+i\epsilon},
\]
四个标量 Yukawa 顶角分别为 \(-i\Gamma_j\)，并把闭合费米子环负号单独写出。于是带四个外部插入的单条有向循环路径满足
\[
 i\mathcal M_\rho=-\int\frac{d^4\ell}{(2\pi)^4}\,
 \frac{T_M(\ell)}{\prod_{j=1}^4(k_j^2-\mu_j^2+i\epsilon)}.
\]
此处的 \(T_M\) 是 Minkowski Dirac 迹，且分子中每个内部动量按 \(k_j=\ell+r_j\) 定义。

### 117.2 分母与测度的 Wick 转动

取 \(\ell^0=i\ell_E^4\)，空间分量不变，则每条传播子分母满足
\[
 k_j^2-\mu_j^2+i\epsilon\longrightarrow
 -(k_{jE}^2+\mu_j^2)\quad (\epsilon\to0^+).
\]
四个分母一共给出 \((-1)^4=+1\)，而积分测度给出
\[
 d^4\ell_M=i\,d^4\ell_E.
\]
因此，单条路径的图形振幅变为
\[
 i\mathcal M_\rho=-i\int\frac{d^4\ell_E}{(2\pi)^4}
 \frac{T_W(\ell_E)}{\prod_{j=1}^4(k_{jE}^2+\mu_j^2)},
\]
其中 \(T_W\) 明确定义为把 Minkowski 迹按上述 Wick 映射后所得的分子，而不是另行任意指定的 Euclidean 迹。按此定义，
\[
 \boxed{\mathcal M_\rho=-\int\frac{d^4\ell_E}{(2\pi)^4}
 \frac{T_W(\ell_E)}{\prod_j(k_{jE}^2+\mu_j^2)}}.
\]
也就是说，若前文的 \(\mathcal I_\rho\) 定义为右侧积分但不含前面的图形整体负号，则物理振幅的该路径贡献为 \(-\mathcal I_\rho\)。这一结论针对本节明确写出的 \(i\mathcal M\) 与传播子约定。

### 117.3 迹结构中的 Wick 符号

采用与前文一致的分解
\[
T_M=2H\,G_M+2\sum_{i<j}C_{ij}(k_i\!\cdot k_j)_M+2M,
\]
其中 \(G_M\) 是两个 Minkowski 标量积的乘积之差。Wick 转动后，每个标量积满足
\[
(k_i\cdot k_j)_M\to -(k_{iE}\cdot k_{jE})_E.
\]
因此，含两个标量积的 \(G_M\) 项整体不变号，而含一个标量积的 \(C_{ij}\) 项变号，质量项不变号：
\[
T_W=2H\,G_E-2\sum_{i<j}C_{ij}(k_{iE}\cdot k_{jE})_E+2M.
\]
这正是前文欧氏分子展开中 \(K_E^4\) 系数为 \(+2H\)、零阶动量双线性部分系数为 \(-2\sum C_{ij}\)、质量常数项为 \(+2M\) 的来源。这里的符号是分子变换的符号；它与 117.2 中振幅外部的整体负号是两件不同的事，不能互相抵消或重复计数。

### 117.4 参数化因子与最终约定

四个 Euclidean 分母的参数化为
\[
\frac1{D_1D_2D_3D_4}=6\int_{x_i\ge0}d^4x\,\delta\!\left(1-\sum_i x_i\right)
\frac1{(\sum_i x_iD_i)^4}.
\]
因此 \(6=\Gamma(4)\) 只出现一次。如果采用归一化单纯形平均
\[
\langle F\rangle_x=6\int d^4x\,\delta(1-\sum_i x_i)F,
\]
则积分表达式写成 \(\langle\cdots\rangle_x\) 后不能再额外乘 6。

### 117.5 本节结论及边界

在已明确的图形约定下，Wick 转动给出两项独立规则：一是分子中的单个 Minkowski 标量积变号、双标量积乘积不变号；二是由于测度的 \(i\) 因子，\(i\mathcal M_\rho\) 化为 \(-i\) 乘 Euclidean 积分，因此 \(\mathcal M_\rho\) 是该 Euclidean 积分的负值。四个分母的四个负号彼此抵消。

这锁定了图形计算一侧的 Wick 转动符号，但还不能单独锁定有效作用量展开与前文核函数之间的最终总号：必须确认 \(A_0^{-1}\) 在行列式表达式中究竟定义为代数逆算符，还是已吸收传播子 \(i\) 的 Green 函数，并用同一个定义比较四阶有效作用量的四次泛函导数与 \(i\mathcal M\)。因此本节不据此给出最终 Wilson 系数，也不把任何 UV 核单独解释为已匹配的物理振幅。

---

## 118. 费米子行列式与费曼图四点振幅的整体符号和组合因子对照

本节把第 116 节的行列式展开与第 117 节的图形 Wick 转动放在同一套约定下比较。目的仅是核对整体符号与排列计数；它不替代 EFT 侧的泡图、接触图和反项计算。

### 118.1 先固定二次算符的定义

取 Minkowski 费米子作用量
\[
S_F[\psi,\bar\psi;\phi]=\int d^4x\,\bar\psi\,A[\phi]\,\psi,
\qquad A[\phi]=A_0-V[\phi],
\]
其中例如 \(A_0=i\slashed\partial-M\)，而相互作用项按此定义写成 \(-\bar\psi V\psi\)。积分掉 Grassmann 费米子后，定义
\[
e^{i\Gamma_f[\phi]}=\det A[\phi],\qquad
\Gamma_f[\phi]=-i\operatorname{Tr}\ln A[\phi].
\]
这里 \(A_0^{-1}\) 是微分算符的**代数逆**，动量空间中按约定为
\[
A_0^{-1}(p)=(\slashed p-M)^{-1}
=\frac{\slashed p+M}{p^2-M^2+i\epsilon},
\]
它本身不额外包含传播子前面的 \(i\)。传播子是 \(iA_0^{-1}\)。若把这两个对象混为一谈，就会把传播子中的 \(i\) 重复计入。

### 118.2 四阶项及四个带标签外线的排列

从
\[
\begin{aligned}
\Gamma_f&=-i\operatorname{Tr}\ln A_0
-i\operatorname{Tr}\ln(1-A_0^{-1}V)\\
&=\text{常数}+i\sum_{n\ge1}\frac1n
\operatorname{Tr}\!\left[(A_0^{-1}V)^n\right]
\end{aligned}
\]
得到
\[
\Gamma_f^{(4)}=\frac{i}{4}\operatorname{Tr}\!\left[(A_0^{-1}V)^4\right].
\]
令四个外部标量插入分别带标签 \(1,2,3,4\)，对它们作四次泛函导数会产生 \(4!=24\) 个有序排列。迹的循环性把每个循环旋转等价类中的四个排列归为同一类，因此有
\[
\frac{4!}{4}=6
\]
个循环类。此处只除去循环旋转，**不**额外把反向次序自动视为同一类；反向排列一般仍是六类中的另一类，除非模型结构和积分另行证明它们相等。

设 \(\mathcal J_\rho\) 表示一个固定有序循环 \(\rho\) 的完整 Minkowski 环积分，包括该路径的矩阵顶角、分子迹和四个分母，但暂不包含行列式展开的显式系数 \(i/4\)。四次导数后，每个循环类由四个循环旋转代表，故有效作用量四点核为
\[
\frac{\delta^4\Gamma_f}{\delta\phi_1\delta\phi_2\delta\phi_3\delta\phi_4}
= i\sum_{[\rho]\,\in\,S_4/C_4}\mathcal J_\rho,
\]
其中等式中的 \(\mathcal J_\rho\) 应理解为在相应外动量约定下的积分核；循环旋转之间的环动量平移不改变积分。

### 118.3 与图形规则逐项对照

有效作用量四点核对应的 1PI 顶角因子还要乘一个 \(i\)，因此
\[
 i\,\Gamma_f^{(4)}\big|_{\text{四个外线求导}}
 =-\sum_{[\rho]\,\in\,S_4/C_4}\mathcal J_\rho.
\]
图形计算一侧，四个 Yukawa 顶角贡献 \((-i)^4=+1\)，四个费米子传播子贡献 \(i^4=+1\)，闭合费米子环另给一个 \(-1\)，所以在 Wick 转动之前
\[
 i\mathcal M_{\rm loop}=-\sum_{[\rho]\,\in\,S_4/C_4}\mathcal J_\rho.
\]
两式在相同的 \(A_0^{-1}\)、顶角定义、外动量标记和积分正则化下相符。这里的对照说明：行列式展开中的 \(i/4\)、四次求导的 24 个排列、循环性产生的因子 4，以及图形法中的闭环负号，必须作为一个整体核对；不能把行列式已经编码的闭环符号再额外乘一次，也不能把四个传播子的 \(i\) 塞进代数逆算符后又重复乘 \(i^4\)。

### 118.4 与第 117 节 Wick 结果的衔接

对上式每一个 \(\mathcal J_\rho\)，按第 117 节固定的 Minkowski 约定进行 Wick 转动，分母的四个负号相乘为正，测度给出一个 \(i\)，而分子中的单个标量积变号、双标量积乘积不变号。若记相应的 Euclidean 核为 \(\mathcal I_{\rho,E}\)，则在第 117 节的具体定义下
\[
\mathcal J_\rho=i\mathcal I_{\rho,E},\qquad
 i\mathcal M_{\rm loop}=-i\sum_{[\rho]}\mathcal I_{\rho,E}.
\]
这与第 117 节的 \(\mathcal M_\rho=-\mathcal I_{\rho,E}\) 一致。此处的关系依赖于 \(\mathcal I_{\rho,E}\) 已包含 Wick 后的分子符号变换，但不包含额外的闭环负号。

### 118.5 本节能确认什么、仍不能确认什么

**已完成的核对：**在上述明确定义下，行列式方法和费曼图方法给出相同的整体闭环符号和相同的六个循环类；参数化因子 \(\Gamma(4)=6\) 与排列计数的 6 是两种不同来源，不能互相替代，也不能因数值相同而合并或重复计入。

**尚未完成的核对：**这不等于 UV–EFT 匹配已经完成。还需在 EFT 侧用相同的外动量、红外调节、重整化方案和算符基底，独立计算泡图、接触图与反项，检验红外部分抵消，再从解析的局部动量展开中投影目标 Wilson 系数。尤其不能仅凭 UV 环图的有限数值或某个特定外动量点，直接断言 \(C_{HS}^{(D)}\) 的最终值。

---

## 119. EFT 侧四标量 \(hhss\) 振幅：先锁定图集与匹配阶次

本节开始下一阶段，但不把尚未逐图求值的 EFT 振幅写成已完成结果。关键是：此前文档中针对混合二点函数得到的泡图/接触图核，外腿数、拓扑和动量依赖都与当前的四标量 \(hhss\) 1PI 振幅不同，不能直接代入。

### 119.1 破缺相 EFT 顶点

采用前文实耦合、最低阶维数五算符展开的约定，记
\[
 g_h=\frac{m}{v_h},\qquad g_s=\frac{m}{v_s},\qquad
 g_{hs}=\frac{m}{v_hv_s},
\]
对应相互作用
\[
\mathcal L_{\rm int}=-g_hh\bar\ell\ell-g_ss\bar\ell\ell-g_{hs}hs\bar\ell\ell.
\]
这里的 \(h\bar\ell\ell\)、\(s\bar\ell\ell\) 是单标量顶点，而 \(hs\bar\ell\ell\) 是双标量接触顶点。要匹配四标量振幅，必须枚举能够把两条费米子线闭合、并且外腿恰好为两个带标签的 \(h\) 和两个带标签的 \(s\) 的 1PI 图。

### 119.2 与目标外腿相容的最低拓扑

在这个破缺相顶点记号下，至少要单独检查以下拓扑类别：

1. **四个单标量顶点的费米子环**：顶点多重集为 \(\{h,h,s,s\}\)，有四条内部费米子传播子。它对应四个单标量 Yukawa 顶点的组合，需保留全部不等价的带标签循环顺序。
2. **一个双标量接触顶点加两个单标量顶点**：顶点多重集为 \(\{hs,h,s\}\)，内部有三条费米子传播子。必须枚举接触顶点承载哪一个 \(h\) 标签与哪一个 \(s\) 标签；不能把接触顶点的外腿分配因子隐含地并入四单顶点图。
3. **两个双标量接触顶点**：顶点多重集为 \(\{hs,hs\}\)，内部有两条费米子传播子。两个接触顶点的外腿标签分配和泡图对称因子需单独处理。

以上是按已写出的破缺相顶点作图时需要检查的拓扑类别，并非声称三类在任意 EFT 截断或任意匹配阶次都必须同时保留。最终图集应由所匹配的未破缺相算符阶次、外腿标记和 EFT 幂计数共同决定；若采用严格的两次维数五算符插入计数，不能无说明地把更高阶插入的四单顶点环混入同一阶结果。

### 119.3 必须统一的计算账本

每一张 EFT 图都应记录：

- 四个外标量的标签及其流入动量；
- 每个顶点是单标量 Yukawa 还是 \(hs\bar\ell\ell\) 接触顶点；
- 内部费米子传播子的数量、质量和分子；
- 闭合费米子环负号、顶点因子、对称因子及外腿排列计数；
- 同一维数正规化与减除方案下的 UV 极点、IR 依赖和局部动量多项式；
- 与 UV 侧完全相同的外动量不变量基底，以及目标算符 \(\mathcal O_D=\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S)\) 的投影规则。

特别是 \(\mathcal O_D\) 在中性标量展开中含有 \(v_hv_s\,\partial_\mu h\partial^\mu s\)，因此不能只计算一个任意的 \(hhss\) 动量系数，就直接把它等同于 \(C_D\) 或 \(C_{HS}^{(D)}\)。必须先把完整四点局部多项式投影到选定的、无冗余的算符基底，并处理分部积分及运动方程等价关系。

### 119.4 本阶段结论与下一计算动作

目前完成的是 EFT 四标量图集的拓扑盘点与幂计数警告；尚未完成各图的 Dirac 迹、环积分、反项或 UV–EFT 差分。下一步应先从未破缺相的维数五算符拉氏量确定严格的插入阶次与带标签外腿，再为该阶次生成 EFT 图清单，逐图计算并与 UV 侧的同一 1PI Green 函数相减。未完成这一步前，不报告最终 \(C_{HS}^{(D)}\) 数值。

---

## 120. 目标导数算符在中性实标量展开中的四点投影核

本节先推导算符本身对局部四点振幅的动量结构，作为后续 EFT 图求值后的投影模板。它不假设 UV–EFT 差值已经求出。

### 120.1 场展开与四次项

采用明确的规范化约定
\[
H=\frac1{\sqrt2}\begin{pmatrix}0\\v_h+h\end{pmatrix},\qquad
S=\frac{v_s+s}{\sqrt2},
\]
其中只保留中性实标量方向。于是
\[
H^\dagger H=\frac12(v_h+h)^2,\qquad
S^\dagger S=\frac12(v_s+s)^2,
\]
并有
\[
\partial_\mu(H^\dagger H)=(v_h+h)\partial_\mu h,\qquad
\partial_\mu(S^\dagger S)=(v_s+s)\partial_\mu s.
\]
因此
\[
\mathcal O_D=\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S)
=(v_h+h)(v_s+s)\partial_\mu h\partial^\mu s.
\]
其中四标量项为
\[
\boxed{\mathcal O_D\big|_{hhss}=hs\,\partial_\mu h\,\partial^\mu s.}
\]
注意它是两个无导数场与两个带导数场的乘积，场数确为 \(h^2s^2\)。

### 120.2 带标签四点顶角的动量多项式

令两个流入的 \(h\) 动量为 \(p_1,p_2\)，两个流入的 \(s\) 动量为 \(p_3,p_4\)，并统一采用全流入约定
\[
p_1+p_2+p_3+p_4=0.
\]
若拉氏量中包含 \(\mathcal L\supset C_D\mathcal O_D\)，四次泛函导数会让任意一个 \(h\) 与任意一个 \(s\) 承担导数。因此该局部顶角的动量结构正比于
\[
\boxed{\mathcal P_D(p_i)=-C_D\sum_{i=1}^{2}\sum_{j=3}^{4}p_i\cdot p_j.}
\]
这里写的是乘上顶角整体因子 \(i\) 之前的局部多项式；整体的 \(i\) 取决于把振幅定义为 \(i\mathcal M\) 还是把 1PI 顶角函数定义为 \(\Gamma^{(4)}\)，后续必须与 UV/EFT 两侧一致。

利用动量守恒，交叉动量和可化为
\[
\sum_{i=1}^{2}\sum_{j=3}^{4}p_i\cdot p_j
=(p_1+p_2)\cdot(p_3+p_4)=-(p_1+p_2)^2,
\]
故在全流入约定下
\[
\boxed{\mathcal P_D(p_i)=C_D(p_1+p_2)^2.}
\]
等价地，它也等于 \(C_D(p_3+p_4)^2\)。这个等式是动量守恒的结果，不意味着可以在不同外腿标记或不同通道间任意替换单个点积。

### 120.3 如何用于 UV–EFT 差值

设同一套外腿标记下，完成重整化和 IR 一致处理后的局部四点差值为
\[
\Delta\mathcal A_{hhss}^{\rm local}=K\,(p_1+p_2)^2+\text{其他独立局部结构}.
\]
在所选算符基底中，只有在确认其他算符、分部积分和运动方程冗余均已处理后，才能将系数 \(K\) 与 \(C_D\) 对应。按本节上述场归一化及顶角约定，目标算符贡献的交叉动量多项式为 \(C_D(p_1+p_2)^2\)；若拉氏量写成 \(C_D/\Lambda^2\,\mathcal O_D\)，则相应系数应整体替换为 \(C_D/\Lambda^2\)。

本节给出的是**算符侧投影模板**，不是匹配结果。尚需完成 EFT 图的积分、反项与 UV 侧同一通道的局部差值，才能提取并核验 Wilson 系数。

## 121. EFT 四标量振幅的正确插入阶次：两次未破缺相维数五算符插入

本节把计算从破缺相的有效顶点图重新锚定到第 21 节规定的严格阶次：一圈、两个维数五算符插入，阶数为 \(C_{5,\ell}C^*_{5,\ell}\)，保留至维数六。这个约束会改变图集，不能把破缺相四个单标量 Yukawa 顶点的环图直接当作该阶 EFT 振幅。

### 121.1 外腿与拓扑

未破缺相的插入写为
\[
\mathcal L_5\supset C_{5,\ell}S_\ell\bar L_\ell H\ell_R+\mathrm{h.c.}
\]
两个共轭插入各带一条费米子双线以及两个标量场。对于 \(H,H^\dagger,S,S^\dagger\) 四个外标量腿，四个外腿可以分别接在两个插入顶点上；两条内部费米子传播子连接这两个顶点，形成一圈泡图。它是一张**两插入、两费米子传播子的四标量图**，而不是四个破缺相单标量顶点构成的四传播子盒图。

这一拓扑判断来自算符场内容与插入阶数，不依赖具体积分结果。若改用破缺相的 \(h,s\) 外态，应先将规范不变算符及其共轭展开，并对所有能给出相同外态的场分配求和；不能只保留某个方便的破缺相顶点图。

### 121.2 标量动量通道与 Dirac 分子

令两个维数五顶点间流过的外部总动量为 \(q\)。对质量可忽略的轻费米子，泡图的分母为
\[
 k^2+i0,\qquad (k+q)^2+i0.
\]
在固定手征投影且忽略额外内部指标的示意性 Dirac 迹中，分子具有
\[
\operatorname{tr}[P_R\slashed k P_L(\slashed k+\slashed q)]
=2\,k\cdot(k+q),
\]
其中使用 \(P_{L,R}=(1\mp\gamma_5)/2\)。真实模型的味指标、规范指标及顶点方向仍须按 \(C_{5,\ell}\) 与其共轭的原始拉氏量确认；此式只固定最基本的动量积分核。

### 121.3 二阶外动量的 UV 极点

在维数正规化下，分子恒等式为
\[
2k\cdot(k+q)=k^2+(k+q)^2-q^2.
\]
故
\[
\begin{aligned}
I(q)&=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{2k\cdot(k+q)}{(k^2+i0)((k+q)^2+i0)}\\
&=\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\left[\frac1{k^2+i0}+\frac1{(k+q)^2+i0}
-\frac{q^2}{(k^2+i0)((k+q)^2+i0)}\right].
\end{aligned}
\]
前两项是无尺度无质量 tadpole，在维数正规化中为零。因此二阶动量部分由最后一项控制。采用常见 Minkowski 积分约定，
\[
\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac1{(k^2+i0)((k+q)^2+i0)}
=\frac{i}{16\pi^2}\left[\frac1{\bar\epsilon}
-\ln\frac{-q^2-i0}{\mu^2}+2+O(\epsilon)\right],
\]
于是该 Dirac 分子核的 UV 极点部分为
\[
\boxed{I(q)\big|_{\rm UV}=-\frac{i q^2}{16\pi^2}\frac1{\bar\epsilon}.}
\]
这里 \(1/\bar\epsilon=1/\epsilon-\gamma_E+\ln4\pi\)。这个盒中结果仅指明量纲、动量通道和积分核的极点；**它还不是**完整四标量振幅的系数，因为尚未乘上具体顶点因子、闭环符号、味/规范指标、外腿场分配及可能的相同图组合因子。

### 121.4 本步的结论和下一项核验

这一步确认：在 \(C_5C_5^*\) 阶，四标量导数反项来自两次维数五插入的泡图，局部 UV 极点与通道动量平方 \(q^2\) 成正比。接下来必须从原始未破缺相拉氏量明确写出共轭顶点、规范与味指标，列全 \(H,H^\dagger,S,S^\dagger\) 外腿分配，并将所得各通道的 \(q^2\) 系数投影到经过 IBP/EOM 约化的算符集合。没有这些组合与基底信息，不能把上式直接识别为 \(C_{HS}^{(D)}\) 的 beta 函数或有限匹配系数。

## 122. 未破缺相四标量外腿的通道动量与目标算符投影核对

第 121 节已经得到单个两插入泡图的基本极点核正比于插入顶点间的总动量平方。这里进一步区分这个通道变量与目标导数算符的动量结构，避免把一个通道的 $q^2$ 直接等同于 $C_{HS}^{(D)}$。

### 122.1 四个带标签的复标量外腿

用全流入动量标记外腿
\[
H(p_H),\quad H^\dagger(p_{H^\dagger}),\quad
S(p_S),\quad S^\dagger(p_{S^\dagger}),
\qquad \sum p_i=0.
\]
若一端维数五插入承载 $H,S$，共轭端承载 $H^\dagger,S^\dagger$，则泡图的通道动量为
\[
q_{HS}=p_H+p_S=-(p_{H^\dagger}+p_{S^\dagger}),
\]
其极点核正比于 $q_{HS}^2$。若外腿分配或顶点取向不同，必须重新从顶点所承载的场确定 $q$；不能不加检查地把 $q_{HS}$ 替换为另一个 Mandelstam 变量。

### 122.2 目标算符的复场动量多项式

目标算符定义为
\[
\mathcal O_D=\partial_\mu(H^\dagger H)\,\partial^\mu(S^\dagger S).
\]
对四条带标签外腿作四次泛函导数时，第一项中的导数可以作用在 $H$ 或 $H^\dagger$ 上，第二项中的导数可以作用在 $S$ 或 $S^\dagger$ 上。将四种分配相加，其顶角多项式为
\[
\begin{aligned}
\mathcal P_D
&=-C_D(p_H+p_{H^\dagger})\cdot(p_S+p_{S^\dagger})\\
&=C_D(p_H+p_{H^\dagger})^2
=C_D(p_S+p_{S^\dagger})^2,
\end{aligned}
\]
其中最后一步使用总动量守恒。整体 $i$ 因子取决于采用的是作用量顶角还是振幅约定；上式只列出动量多项式。

因此，单一 $HS$ 通道的 $q_{HS}^2$ 与目标算符的 $(p_H+p_{H^\dagger})^2$ **不是同一个动量不变量**。要确定它们在匹配中的关系，必须将所有由原始算符允许的带标签外腿分配相加，再把完整局部振幅写成独立动量不变量的线性组合。随后还要考虑 IBP、EOM 以及可能的其他维数六算符；只匹配一个通道一般不足以分离 $\mathcal O_D$ 的系数。

### 122.3 可执行的匹配判据

后续计算应逐项保留如下账本：

1. 插入顶点的原始场内容及共轭方向；
2. 该顶点对外腿所贡献的动量和 $q$；
3. 该分配的规范、味和手征因子；
4. 泡图 UV 极点的 $q^2$ 系数及图的组合因子；
5. 所有分配相加后的局部多项式；
6. 选定的非冗余算符基底及投影矩阵。

在这份账本完成之前，$-i q^2/(16\pi^2\bar\epsilon)$ 只是一项基本积分核，不能单独决定反项矩阵或 $C_{HS}^{(D)}$。本节完成的是动量通道与目标算符之间的独立核对，尚未宣称已完成模型特定的规范/味求和。

## 123. 单一 \(HS\) 通道的 \(q^2\) 极点对应哪类维数六算符？

第 122 节指出，两插入泡图的基本局部结构是 \(q_{HS}^2\)，而目标算符 \(\mathcal O_D=\partial(H^\dagger H)\partial(S^\dagger S)\) 的四点投影是另一动量不变量。这里进一步把这个区别落实到算符层面。

### 123.1 由通道动量构造的算符

定义复场乘积 \(\Phi_i=S H_i\)。忽略规范场时，满足
\[
\partial_\mu\Phi_i=(\partial_\mu S)H_i+S\partial_\mu H_i.
\]
因此，泡图中与 \(q_{HS}^2\) 相联系的自然局域结构不是单独的 \(\mathcal O_D\)，而是
\[
\mathcal O_{\Phi D}=|\partial_\mu(SH_i)|^2
\]
（含规范相互作用时应将 \(\partial_\mu\) 替换为对应的协变导数）。它的二次导数作用于复合场 \(SH\)，所以其四点顶角直接产生 \((p_H+p_S)^2\) 通道。

### 123.2 展开及基底混合

对规范不变形式展开：
\[
\begin{aligned}
\mathcal O_{\Phi D}={}&(H^\dagger H)(D_\mu S)^\dagger D^\mu S
+(S^\dagger S)(D_\mu H)^\dagger D^\mu H\\
&+(D_\mu S)^\dagger S\,H^\dagger D^\mu H
+S^\dagger D_\mu S\,(D^\mu H)^\dagger H.
\end{aligned}
\]
按文档前述基底定义，交叉项可写为
\[
\mathcal O_{\rm cross}=\frac12\mathcal O_D+\frac12\mathcal O_J,
\]
其中
\[
\mathcal O_D=\partial_\mu(S^\dagger S)\partial^\mu(H^\dagger H),
\]
而 \(\mathcal O_J\) 是 Higgs 与 singlet 的反向导数流的乘积。故
\[
\boxed{\mathcal O_{\Phi D}=\mathcal O_H+\mathcal O_S+\frac12\mathcal O_D+\frac12\mathcal O_J}
\]
其中 \(\mathcal O_H=(S^\dagger S)(D_\mu H)^\dagger D^\mu H\)、\(\mathcal O_S=(H^\dagger H)(D_\mu S)^\dagger D^\mu S\)。这个等式说明：若两插入泡图只在某个通道中给出 \(q^2\)，其系数首先对应复合场导数结构；把它写成所选基底中的 \(C_D\) 时，会同时涉及 \(\mathcal O_H,\mathcal O_S,\mathcal O_J\) 的系数或其约化关系。

### 123.3 对匹配计算的实际约束

因此，不能将单个泡图的 \(q^2\) 极点直接标记为 \(C_{HS}^{(D)}\)。下一步必须先固定以下事项：

1. 维数六算符基底是否保留 \(\mathcal O_{\Phi D}\)，还是改用 \(\{\mathcal O_H,\mathcal O_S,\mathcal O_D,\mathcal O_J,\ldots\}\)；
2. 是否使用分部积分、运动方程或场重定义，以及对应的基底变换；
3. 泡图中 \(H,S\) 复场通道的 UV 极点在原始拉氏量中的规范指标与味指标系数；
4. 同一基底下 UV 侧局部展开与 EFT 侧反项的差额。

本节只建立通道算符与基底的关系，没有给出尚未计算的规范/味求和或 Wilson 系数数值。特别是，基底变换必须连同所有相关算符一起执行，不能只把 \(\mathcal O_{\Phi D}\) 的一部分交叉项单独抽出并称为完整匹配结果。

## 124. 两次维数五插入的四标量 EFT 极点：规范指标、味指标与算符投影

本节不再只列拓扑，而是把原始未破缺相算符的四标量泡图系数写明。采用本文第 21.9 节的 convention：
\[
\mathcal L_5=-\sum_\ell C_{5,\ell}\,S_\ell\,\bar L_{\ell i}H_i\ell_R+\mathrm{h.c.},\qquad S_\ell\in\{S,S^\dagger\},
\]
每个未共轭顶点规则为 $-iC_{5,\ell}$，共轭顶点为 $-iC^*_{5,\ell}$。忽略规范场背景但保留规范指标，且在圈内轻费米子无质量的近似下计算 $C_{5,\ell}C^*_{5,\ell}$ 阶。

### 124.1 原始顶点及指标收缩

未共轭顶点携带因子
\[
-iC_{5,\ell}\,\delta_{i i_{L}},
\]
其共轭顶点携带
\[
-iC^*_{5,\ell}\,\delta_{j i_{L}},
\]
这里 $i,j$ 是外部 $H,H^\dagger$ 的 $SU(2)_L$ 指标，$i_L$ 是内部双重态轻费米子的指标。内部双重态传播子给出 $\delta_{i_Lj_L}$，故规范因子为
\[
\delta_{ij}.
\]
内部另一条费米子线是 $\ell_R$ 单态传播子，不带 $SU(2)_L$ 指标。由于一个顶点含 $S_\ell,H$，另一个含 $S_\ell^\dagger,H^\dagger$，要得到外态 $H_i,S_\ell,H_j^\dagger,S_\ell^\dagger$，在该阶只有这对共轭插入；不能把它误数成四个单标量 Yukawa 顶点的盒图。每个 flavor 的耦合因子是 $|C_{5,\ell}|^2$，不同 flavor 的贡献在本阶按 flavor 对角相加；若模型存在 flavor 非对角 $C_5$，则需改用矩阵乘积而不是简单模平方求和。

### 124.2 圈积分及 UV 极点

以两个插入之间的总外动量 $q=p_H+p_{S_\ell}$ 为通道变量，Dirac 分子和分母为
\[
N(k,q)=\operatorname{tr}[P_R\slashed k P_L(\slashed k+\slashed q)]=2k\cdot(k+q),\qquad
D=k^2(k+q)^2.
\]
利用
\[
2k\cdot(k+q)=k^2+(k+q)^2-q^2,
\]
前两项是维数正规化下的无尺度积分；因此
\[
\left.\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}\frac{N(k,q)}{D}\right|_{\rm UV}
=-\frac{iq^2}{16\pi^2\bar\epsilon}.
\]
按第 21.9 节的顶点与自能插入约定，单 flavor 的局部发散由反项
\[
\boxed{\delta\mathcal L_{4\phi,\rm div}
=-\frac{|C_{5,\ell}|^2}{16\pi^2\bar\epsilon}
(D_\mu(S_\ell H_i))^\dagger D^\mu(S_\ell H_i)}
\]
抵消。这里 $i$ 求和；$D_\mu(S_\ell H_i)$ 是乘积场的总协变导数。这个结果已经包含基本泡积分的 $1/(16\pi^2)$、单 flavor 的 $|C_5|^2$ 和规范指标收缩 $\delta_{ij}$。在此场内容下没有额外的独立 $SU(2)$ 迹因子 2：外部 $H_i,H_j^\dagger$ 的 1PI 张量是 $\delta_{ij}$，只有在再对外部指标作迹时才会产生双重态维数。

### 124.3 投影到未约化维数六算符

先令规范场为零以显示导数结构，并定义
\[
\mathcal O_H=(S^\dagger S)(\partial_\mu H)^\dagger\partial^\mu H,\quad
\mathcal O_S=(H^\dagger H)(\partial_\mu S)^\dagger\partial^\mu S,
\]
\[
\mathcal O_D=\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S),
\quad
\mathcal O_J=[iS^\dagger\overleftrightarrow{\partial_\mu}S]
[ iH^\dagger\overleftrightarrow{\partial^\mu}H],
\]
其中 $\mathcal O_J$ 的定义采用使交叉项满足下列恒等式的流约定。对 $S_\ell=S$，直接展开得
\[
(D_\mu(SH))^\dagger D^\mu(SH)
=\mathcal O_H+\mathcal O_S+\frac12\mathcal O_D+\frac12\mathcal O_J.
\]
对 $S_\ell=S^\dagger$，singlet 流方向反转，因此
\[
(D_\mu(S^\dagger H))^\dagger D^\mu(S^\dagger H)
=\mathcal O_H+\mathcal O_S+\frac12\mathcal O_D-\frac12\mathcal O_J.
\]
因此若定义 $A_S=\sum_{\ell:S_\ell=S}|C_{5,\ell}|^2$、$A_{S^\dagger}=\sum_{\ell:S_\ell=S^\dagger}|C_{5,\ell}|^2$，则四标量扇区的未约化发散组合为
\[
\boxed{
\delta\mathcal L_{4\phi,\rm div}=-\frac1{16\pi^2\bar\epsilon}
\left[(A_S+A_{S^\dagger})(\mathcal O_H+\mathcal O_S+\tfrac12\mathcal O_D)
+\tfrac12(A_S-A_{S^\dagger})\mathcal O_J\right].
}
\]
这给出了该扇区在上述基底和符号约定下的显式系数关系。特别地，$\mathcal O_D$ 的**未约化反项分量**是
\[
\delta C_D\big|_{\rm unred}=-\frac{A_S+A_{S^\dagger}}{32\pi^2\bar\epsilon},
\]
但它不是任意最终非冗余基底中的完整 Wilson 系数：若基底约化会将 $\mathcal O_H,\mathcal O_S,\mathcal O_J$ 与其他算符混合，必须连同该变换一起处理。

### 124.4 与 UV 侧比较的边界

这一步确定了 EFT 四标量通道在给定约定下的 UV 极点与未约化算符分解，但尚未完成有限匹配。要得到 UV–EFT 差额，仍需从完整 UV 质量本征态及其耦合计算相同外腿的局部 $q^2$ 展开，并采用一致的红外规约、重整化尺度和外腿约定。只比较 UV 极点是不够的：在重整化可行的 UV 理论中，极点差必须由一致的算符反项吸收，而有限阈值还依赖完整振幅的低动量展开。

**本节完成项：**原始维数五顶点的规范指标收缩、单 flavor 的 $|C_5|^2$ 系数、泡图 UV 极点，以及 $S_\ell=S/S^\dagger$ 对应的未约化算符分解。

**尚未完成项：**EOM/IBP 约化后的完整非冗余反项矩阵、UV 侧同一四标量振幅的局部展开、UV–EFT 有限差额，以及最终 $C_{HS}^{(D)}$ 的方案一致匹配值。

## 125. UV 四点振幅的低动量展开：发散阶与有限导数阈值必须分开

本节把 EFT 侧已得到的 $q^2$ 极点与 UV 侧四传播子盒图的计算目标对齐，先确定哪些部分应当发散、哪些部分应当有限，避免把 EFT 的 $1/\bar\epsilon$ 直接当成 UV 的有限匹配系数。

### 125.1 UV 盒图的表面发散度

对一个四 Yukawa 顶点、四费米子传播子的 UV 盒图，环动量大时分子 Dirac 迹的最高阶为 $\ell^4$，四个传播子分母最高阶为 $(\ell^2)^4$。故零外动量项的径向积分按
\[
 d^4\ell\,\frac{\ell^4}{(\ell^2)^4}\sim d\ell\,\ell^{-1}
\]
呈对数表面发散；而二阶外动量项相对多出两个大动量分母幂次，径向行为为 $d\ell\,\ell^{-3}$，在 UV 收敛。因此：

- 四点振幅的零阶局部项可能需要与 renormalizable portal 耦合的重整化一起处理；
- 在完整 UV 理论中，$q^2$ 的局部导数项通常是有限阈值项；
- EFT 两次维数五插入产生的 $q^2$ 极点则由维数六算符反项吸收。二者并不矛盾：EFT 极点描述低能理论的运行，UV–EFT 的有限差额才决定指定匹配尺度下的阈值系数。

这只是逐图的幂次计数。若特定手征结构使 $\ell^4$ 的系数为零，UV 零阶发散会进一步降低；是否发生这种抵消必须由完整迹和所有允许路径的求和证明，不能只由表面发散度断言。

### 125.2 二阶局部项的提取规则

对固定的外腿标记，先将完整 UV 振幅写成
\[
\mathcal A_{\rm UV}(p_a)=\mathcal A_{\rm UV}^{(0)}
+\sum_{a,b}K_{ab}^{\rm UV}\,p_a\!\cdot p_b+O(p^4).
\]
这里 $K_{ab}^{\rm UV}$ 必须包含：全部内部质量本征态路径、相应 Yukawa 矩阵元、所有不等价外腿排列，以及每个图的闭合费米子环符号和组合因子。对于每条四传播子路径，Feynman 参数合并后应使用
\[
\frac1{D_1D_2D_3D_4}=6\int_{x_i\ge0}\!d^4x\,
\delta(1-\textstyle\sum_i x_i)\,
\frac1{[\sum_i x_iD_i]^4},
\]
并在移位环动量后，将分子和分母都展开至外动量二阶。$\Gamma(4)=6$ 只出现一次；不能在参数平均和积分核中重复计入。

完成路径求和后，再以同一外腿约定计算 $\mathcal A_{\rm EFT}$，并形成
\[
\Delta\mathcal A^{(2)}_{\rm local}=
\left[\mathcal A_{\rm UV}-\mathcal A_{\rm EFT}\right]_{p^2,\,\rm local}.
\]
这里 UV 与 EFT 必须采用相同的 IR 规约；若使用硬质量展开或区域法，EFT 软区与 UV 硬区应分别保留，不能把无质量 EFT 积分中的 IR 极点误当成 UV 极点。

### 125.3 当前能下的结论与不能下的结论

由第 124 节可确定 EFT 侧的未约化维数六极点结构。结合本节幂次计数，可以预期完整 UV 盒图的二阶动量系数是有限阈值的主要来源，但**尚不能写出其模型特定的数值或闭式系数**：还需把所有 UV 路径及外腿排列求和，并对相同规范不变算符基底做投影。此前数值路径积分只覆盖指定路由/迹核，不能替代这一完整求和。

因此当前的严格状态是：EFT 反项已得到；UV 侧 $q^2$ 系数的提取程序已明确；最终 UV–EFT 有限差额和 $C_{HS}^{(D)}$ 仍待计算。下一步应生成完整 UV $hhss$（或未破缺相 $HH^\dagger SS^\dagger$）外腿排列清单，并逐项计算其二阶局部系数。

## 第 126 节：用重传播子展开把 UV 盒图与两次维数五插入逐项对齐

本节把第 125 节的“UV–EFT 应相减”进一步落实为传播子层面的匹配关系。目的不是提前给出尚未完成的 Wilson 系数，而是明确 UV 四顶点图的低能软区怎样复现 EFT 泡图，以及有限导数阈值应从哪里提取。

### 126.1 重费米子传播子的手征投影

原始相互作用含有
\[
-y_\ell\bar L_\ell H E_{\ell R}
-\lambda_\ell S_\ell\bar E_{\ell L}\ell_R
-M_{E\ell}\bar E_{\ell L}E_{\ell R}+\mathrm{h.c.},
\]
其中 \(S_\ell=S\) 或 \(S^\dagger\)，具体由味道荷指派决定。沿着连接两个不同手征重费米子端点的重传播子，分子满足
\[
P_R(\slashed k+M_E)P_R=M_E P_R,
\qquad P_L(\slashed k+M_E)P_L=M_E P_L.
\]
因此该线的相关手征分量为
\[
\frac{iP_R(\slashed k+M_E)P_R}{k^2-M_E^2+i0}
=\frac{iM_E P_R}{k^2-M_E^2+i0},
\]
（另一方向相应使用 \(P_L\)）。在低动量区 \(|k^2|\ll M_E^2\) 下，
\[
\frac{M_E}{k^2-M_E^2+i0}
=-\frac1{M_E}\left(1+\frac{k^2}{M_E^2}+\cdots\right).
\]
领先项正是树级维数五系数 \(C_{5,\ell}\propto y_\ell\lambda_\ell/M_{E\ell}\) 的传播子来源；整体符号必须与所选顶点和有效拉氏量约定一致，不能只从比例式判断。

### 126.2 软区为什么复现 EFT 泡图

在 UV 四顶点图中，沿费米子环交替出现轻费米子线和重费米子线。对环动量处于低能区的部分，把两条重线分别按上一小节展开至领先阶，就得到
\[
\frac{y_\ell\lambda_\ell}{M_{E\ell}}
\frac{y_\ell^*\lambda_\ell^*}{M_{E\ell}}
\times
\frac{\text{轻费米子 Dirac 分子}}{k^2(k+q)^2},
\]
即与两次维数五插入相同的轻费米子泡图核，其耦合阶为
\[
|C_{5,\ell}|^2\sim
\frac{|y_\ell\lambda_\ell|^2}{M_{E\ell}^2}.
\]
这说明 EFT 泡图不是要从 UV 盒图中“额外减掉的一张无关图”；它是 UV 图的低能软区展开。使用区域法时，应将 UV 振幅拆成软区与硬区：软区与 EFT 振幅逐项匹配，硬区留下解析的局部项，后者才提供相应阶次的阈值贡献。若直接把完整 UV 积分的 Taylor 系数减去一个未经同一 IR 规约定义的 EFT 积分，可能把红外项或无质量积分的 UV/IR 混合极点误认为匹配差额。

### 126.3 可执行的差额定义

对给定外腿标签、味道 \(\ell\) 及动量通道，定义
\[
\mathcal A_{\rm UV}^{(\ell)}(p)=
\mathcal A_{\rm soft}^{(\ell)}(p)+
\mathcal A_{\rm hard}^{(\ell)}(p),
\]
其中区域分解应在同一维数正规化下进行。EFT 图满足
\[
\mathcal A_{\rm EFT}^{(\ell)}(p)
=\mathcal A_{\rm soft}^{(\ell)}(p)
\]
至本次匹配所保留的阶次；所以局部匹配项由
\[
\Delta\mathcal A_{\rm local}^{(2)}
=\sum_\ell\left[
\mathcal A_{\rm UV}^{(\ell)}-
\mathcal A_{\rm EFT}^{(\ell)}
\right]_{p^2,\,\mathrm{local}}
=\sum_\ell\left[\mathcal A_{\rm hard}^{(\ell)}\right]_{p^2,\,\mathrm{local}}
\]
确定。这个等式表达的是匹配定义；要把右边化成质量比函数，仍必须完成每个带标签循环类的完整 Dirac 分子、所有内线质量路径、外动量置换以及圈图整体符号的积分求和。

### 126.4 本节的结论与下一步

1. UV 四传播子盒图和 EFT 两维数五插入在耦合阶与低能软区上对应；不能将二者视作互不相关的贡献。
2. 软区的领先重传播子展开给出 \(C_5C_5^*\) 泡图；有限导数阈值来自 UV 振幅减去该软区/EFT 部分后的硬区局部展开。
3. 现有文档中的固定路由积分和暂定排列聚合还没有完成完整迹、Minkowski–Euclidean 符号与全部质量路径的共同核验。因此本节**没有**报告 \(C_{HS}^{(D)}\) 的数值或闭式结果。

下一步的计算应按如下顺序执行：固定一组带标签外腿和循环类；写出完整 Minkowski 被积函数；将重传播子作区域展开并独立核对软区是否复现第 124 节泡图；再对硬区二阶动量项积分；最后将六个循环类统一投影到同一规范不变算符基底。只有这一链条封闭后，才能报告最终匹配系数。

### 127. 研究目标重定位：以解决审稿人 Comment 3 为最终交付

#### 127.1 目标文件与审稿人实际要求

已检索资料库文件 `higgs_portal_mixing_merged_guide.md`。该文件将审稿人 Comment 3 拆成三个需要分别回答的问题：

1. **辐射诱导的 \(s\)–\(h\) 混合是否不可避免，量级多大？** 需要给出可重整化 UV 模型中的非对角二点函数 \(\Pi_{sh}(p^2)\)，说明重整化条件、阈值与尺度依赖，并在参数空间内给出可复核的数值。
2. **近简并区是否被 LHC 希格斯数据排除，是否需要抵消项微调？** 需要将一致定义的混合量与实际适用的实验约束比较；近简并区须用完整的混合传播子/复极点分析，而不能仅把非简并的小混合角公式外推到分母为零处。
3. **在低能唯象计算中忽略径向标量 \(s\) 是否合理？** 需要针对论文实际计算的过程，比较保留/忽略 \(s\) 后的振幅或可观测量，并写清动量区间与参数条件；“质量不能在固定 \(v_s\) 下形式退耦”与“低能过程中的贡献数值上很小”是两个不同命题。

因此，整个计算项目的最终交付不再是孤立地求出一个 Wilson 系数，而是形成一条可供审稿回复引用、每一步均可复核的证据链：

\[
\text{原始 UV 拉氏量}
\to \text{一致的重整化/匹配}
\to \Pi_{sh}(p^2)\text{ 与局部算符}
\to \text{物理混合传播子}
\to \text{实验比较与适用边界}
\to \text{逐条回复审稿人}.
\]
#### 127.2 现有 Wilson 系数计算在这条证据链中的位置

此前计算的 \(C_{HS}^{(D)}\) 是导数型维数六算符的匹配系数。它**不是**审稿人所问的 \(s\)–\(h\) 混合角本身，也不能单独证明 Higgs portal 混合可以忽略。只有在明确算符基底、经 IBP/EOM 化简并在 \(H=(0,(v+h)/\sqrt2)^T\)、\(S=(v_s+s)/\sqrt2\) 展开后，才能判断该系数是否给二点混合带来动量依赖贡献，以及它与质量型门户项 \(\lambda_{HS}(H^\dagger H)(S^\dagger S)\) 的关系。

因此，\(C_{HS}^{(D)}\) 的工作应保留为**匹配链中的一个子任务**，但优先级要服从审稿人问题：先得到定义清楚、重整化一致的 \(\Pi_{sh}(p^2)\) 与门户耦合阈值；只有当维数六导数项对所讨论的在壳振幅或低能过程达到相关精度时，才需要把它作为单独的数值结果突出报告。

#### 127.3 对资料库指南的审计：哪些内容不能直接当作最终答案

资料库指南提供了有用的审稿结构和初步估算，但其数字与论断必须经独立复核，不能原样当作已经证明的结论：

1. **低能轻子圈与完整 UV 匹配须分开。** 用 \(y_{h\ell\ell}=m_\ell/v\)、\(y_{s\ell\ell}=m_\ell/v_s\) 算出的轻子圈，只是低能自能的一部分。完整 UV 理论还包括重轻子与轻—重混合传播子贡献。若把 \(\lambda_{HS}(M_E)=0\) 作为边界条件，必须说明这是所选重整化方案下的边界条件，而不是与方案无关的预测；其阈值修正需要从完整 UV 振幅与 EFT 振幅之差得到。
2. **自能的迹、圈积分及有限部分必须从统一约定重新核验。** 指南中从 Dirac 迹、Wick 旋转到 \(\Pi_{sh}\) 的系数存在容易混淆的符号/因子问题；特别是自能的局部 \(p^2\) 项与动量无关质量项不是同一个物理量。后续数值必须从原始费曼积分推导，不能直接沿用指南的数值表。
3. **不能把普通实质量矩阵的小混合角公式用于严格简并点。** \(\sin\theta\simeq \delta m^2/(m_h^2-m_s^2)\) 在分母接近零时失效。加入宽度后也不能未经论证就以 \(|m_h\Gamma_h-m_s\Gamma_s|\) 作为必然非零的下限，因为两宽度项可能接近；应构造并分析完整的复数二点函数矩阵/复极点，并明确采用的重求和近似。
4. **实验界限需按具体质量区间和衰变道核实。** 单一的 \(|\sin\theta|<0.1\text{--}0.3\) 只能作为粗略量级，不应替代实际 LHC 约束。轻标量、近 125 GeV 简并区和 \(m_s>m_h/2\) 的约束来源不同；\(h\to ss\) 也取决于独立的三标量耦合，不能只凭混合角作结论。
5. **低能“可忽略”必须与实际观测量绑定。** 指南中 \(4m_\ell^2/m_s^2\) 的估算依赖所比较的标量流与轴矢量流、外部态和运动学。它不能不加说明地推广到所有过程，尤其不能用纯轻子散射的估算替代论文真正计算的过程。
6. **“微调程度很小”不是自动结论。** 必须先定义被调参数、重整化条件、观测限制和微调度量；近简并区还须用一致的混合传播子处理，不能只把非简并区的比值公式代入。

#### 127.4 后续工作的执行顺序与验收标准

**阶段 A：固定模型与约定。** 从论文正文/原始模型重新确认所有场的规范荷、UV Yukawa 项、\(S\) 或 \(S^\dagger\) 的味结构、质量矩阵、参数定义、符号约定及 \(\lambda_{HS}\) 的重整化条件。先解决任何场共轭或归一化不一致。

**阶段 B：独立计算非对角二点函数。** 在完整 UV 理论中列出所有一圈图（轻轻、轻重及重重传播子是否存在由实际顶点决定），写出完整 Dirac 分子与质量矩阵结构；提取 UV 极点和有限部分。再在 EFT 中计算同一外腿、同一动量和同一方案下的贡献，作 UV–EFT 差额，确认阈值与尺度依赖相消。

**阶段 C：将质量混合和动量混合分开。** 把二点函数写成
\[
\Gamma^{(2)}_{hs}(p^2)= -\delta m_{hs}^2 + p^2\,\delta Z_{hs}+\cdots,
\]
其中具体正负号依照最终拉氏量约定固定。质量型门户项、动量依赖混合以及维数六导数算符分别报告，不能将它们合并成一个未定义的“混合系数”。

**阶段 D：处理简并区与实验比较。** 先从完整逆传播子矩阵求复极点/传播子，再定义对物理产生和衰变振幅有效的混合量；对照按质量区间适用的实验分析。只有确认混合增强及其宽度处理后，才讨论是否排除或需要抵消项。

**阶段 E：检验低能近似。** 针对论文实际的低能过程，计算保留与删除 \(s\) 的振幅差或可观测量相对差，给出 \(|q^2|/m_s^2\)、相关耦合与质量比的控制参数，明确近似的失效区。

**阶段 F：交付审稿材料。** 输出（i）三条审稿意见逐项回应，（ii）正文建议新增/修改段落，（iii）计算附录中可复核的积分与数值，（iv）实验限制来源，（v）所有近似的有效范围。每个数字必须标明输入参数、重整化条件、误差/适用条件；未完成独立核验的内容标为待定，不写成定论。

#### 127.5 本节结论

后续计算以解决资料库指南所整理的审稿人 Comment 3 为最终目标。最优先任务是**重新核验完整 UV 模型中的 \(\Pi_{sh}(p^2)\)、门户耦合阈值和复传播子近简并行为**。先前的 \(C_{HS}^{(D)}\) 匹配工作并未作废，但只有在确认它如何进入二点函数或论文的目标观测量后，才应作为审稿回复中的必要证据。资料库指南中的定量结果暂作为待复核草稿，而不是已完成的证明。


---

---

## 补充核验：原论文模型输入与 Higgs portal 条件

## 第128节：原始论文模型输入与审稿问题定位（arXiv:2608.27258）

### 128.1 论文身份与来源

用户指定的论文为：

- **题目**：*An Axial \(U_A(1)_{L_\mu-L_\tau}\): UV Completion and Experimental Searches*
- **作者**：Rundong Fang, Jinhui Guo, Ming Li, Jia Liu, Xiao-Ping Wang, Yiheng Xiong
- **编号**：arXiv:2608.27258 [hep-ph]，v1 于 2026-08-27 提交。
- **公开页面**：<https://arxiv.org/abs/2608.27258>
- **HTML 全文**：<https://arxiv.org/html/2608.27258v1>

本节只记录与本项目的 \(s\)–\(h\) 混合、标量退耦假设及审稿回复直接相关的模型输入，不试图重写论文全部唯象学内容。上述元数据和下列方程来自 arXiv 页面及其 HTML 全文，后续若论文出现新版本，应重新核对版本差异。

### 128.2 原论文明确给出的 UV 场内容与电荷

论文第 II.1 节的电荷约定（原文 Table 1）为：

| 场 | \(U_A(1)_{L_\mu-L_\tau}\) 荷 |
|---|---:|
| \(L_\mu\) | \(+Q_\ell\) |
| \(\mu_R\) | \(-Q_\ell\) |
| \(E_{\mu L},E_{\mu R}\) | \(+Q_\ell\) |
| \(L_\tau\) | \(-Q_\ell\) |
| \(\tau_R\) | \(+Q_\ell\) |
| \(E_{\tau L},E_{\tau R}\) | \(-Q_\ell\) |
| \(H\) | \(0\) |
| \(S\) | \(Q_S=2Q_\ell\) |

电子扇区在该新规范对称性下不带荷。论文定义 \(g_X\equiv g_{A'}Q_\ell\)，并在基准情形取 \(Q_\ell=1\)。因此，物理上相关的是耦合与荷归一化的乘积，而非单独的荷归一化。

原论文列出的 UV 拉氏量中，与轻子质量生成相关的项为

\[
\begin{aligned}
\mathcal L_{\rm UV}\supset{}&-y_\mu\bar L_\mu H E_{\mu R}
-\lambda_\mu S\bar E_{\mu L}\mu_R
-M_{E\mu}\bar E_{\mu L}E_{\mu R}\\
&-y_\tau\bar L_\tau H E_{\tau R}
-\lambda_\tau S^*\bar E_{\tau L}\tau_R
-M_{E\tau}\bar E_{\tau L}E_{\tau R}+\mathrm{h.c.}
+(D_\nu S)^\dagger(D^\nu S)-V(S).
\end{aligned}
\]

积分掉重矢量类轻子后，论文给出的树级维数五算符是

\[
\mathcal L_{5d}=-\frac{c_\mu}{\Lambda}S\bar L_\mu H\mu_R
-\frac{c_\tau}{\Lambda}S^*\bar L_\tau H\tau_R+\mathrm{h.c.},
\qquad \frac{c_\alpha}{\Lambda}\simeq\frac{y_\alpha\lambda_\alpha}{M_{E\alpha}}.
\]

**对当前计算的意义：** UV 理论与低能 EFT 之间的匹配必须尊重 \(\mu\) 扇区使用 \(S\)、\(\tau\) 扇区使用 \(S^*\) 的区别。不能在两个味道的顶点中不加区分地把 \(S\) 和 \(S^*\) 替换为同一个复场；在对称性破缺后写成实标量 \(s\) 时，还必须从原始相互作用和场归一化重新导出费曼规则。

### 128.3 原论文给出的标量质量、规范玻色子质量与轻子 Yukawa 关系

论文第 II.1–II.3 节采用

\[
H=\frac1{\sqrt2}\begin{pmatrix}0\\v_h+h\end{pmatrix},
\qquad S=\frac{v_s+s}{\sqrt2}
\]

（这里按论文的写法省略了规范选择下的 Goldstone 模式），并给出

\[
V(S)=-\mu_S^2|S|^2+\lambda_S|S|^4,
\qquad m_s=\sqrt{2\lambda_S}\,v_s,
\]

\[
m_{A'}=2g_Xv_s,
\qquad v_s=\frac{m_{A'}}{2g_X},
\qquad y_{s\ell\ell}\simeq\frac{m_\ell}{v_s}
=\frac{2g_Xm_\ell}{m_{A'}},\quad \ell=\mu,\tau.
\]

在重轻子质量远大于混合质量项的 seesaw-like 极限，观测到的轻子质量恢复标准关系，且

\[
y_{h\ell\ell}\simeq\frac{m_\ell}{v_h}.
\]

所以低能轻子圈图的两个标量顶点乘积满足

\[
y_{h\ell\ell}y_{s\ell\ell}\simeq\frac{m_\ell^2}{v_hv_s}.
\]

这是计算低能 \(\ell\) 圈图的有用输入，但**不是完整 UV 的混合预测**：完整答案还依赖重矢量类轻子阈值、门户耦合的重整化条件、反项和所采用的匹配方案。只把这两个有效 Yukawa 代入轻子泡图，不能自动得到与重整化方案无关的物理混合角。

### 128.4 原论文的标量基准假设与公式 (34)

论文第 II.3 节先写出单独的 singlet 势 \(V(S)\)，并选取标量基准

\[
m_s\gtrsim10\ \mathrm{GeV},\qquad\text{negligible Higgs--portal mixing}.
\]

同节还说明，固定 \((m_{A'},g_X)\) 后，\(v_s=m_{A'}/(2g_X)\) 已被确定，而 \(m_s\) 由 \(\lambda_S\) 控制。论文公式 (34) 的约束为

\[
m_s<\sqrt{2\lambda_S^{\max}}\,v_s.
\]

若以该上界估算给定 \(m_s\) 所需的最小 \(v_s\)，则

\[
v_s>\frac{m_s}{\sqrt{2\lambda_S^{\max}}}.
\]

在 \(m_s\simeq125\ \mathrm{GeV}\) 时，取 \(\lambda_S^{\max}=4\pi\) 得 \(v_s\gtrsim25\ \mathrm{GeV}\)；取 \(\lambda_S^{\max}=\pi\) 得 \(v_s\gtrsim50\ \mathrm{GeV}\)。这些数值是对所选微扰性上限的条件性推论，不应误写成模型独立的实验下限。

论文的基准参数还包括：

- \(M_{E\mu}=M_{E\tau}\equiv M_E>10\ \mathrm{TeV}\)；
- 轻—重轻子混合角取 \(|\theta_{\mu L,R}|,|\theta_{\tau L,R}|\le10^{-2}\)；
- 取 \(y_{\mu\tau}=0\)；
- 在匹配尺度令规范动能混合为零，并在所采用的纯轴矢量、忽略轻—重混合修正的基准下讨论其低能行为；
- 以 \(m_s\gtrsim10\ \mathrm{GeV}\) 和可微扰的 \(\lambda_S\) 避开部分轻标量限制，并把 \(s\) 从后续 \(A'\) 主导的现象学中近似退耦。

**当前审稿工作的直接靶点由此确定：** 审稿意见不是要求重新证明整个轴矢量唯象学，而是质疑论文在公式 (34) 附近把 Higgs–singlet mixing 视为可忽略、并把 \(s\) 视为退耦的基准假设是否足够自洽。

### 128.5 必须明确的模型定义缺口：Higgs portal 的完整势与重整化条件

原论文在所列 UV 拉氏量中写出 \(V(S)\)，并在基准假设中写“negligible Higgs–portal mixing”；这不等同于已完整定义了含所有规范不变项的标量势。一般重整化模型允许

\[
V(H,S)\supset \lambda_{HS}(H^\dagger H)(S^\dagger S).
\]

因此后续计算前必须明确以下二者之一：

1. **模型输入为非零门户耦合：** 给定 \(\lambda_{HS}(\mu_R)\) 的边界条件或物理重整化条件，并将树级混合与圈级自能一起纳入质量矩阵；或
2. **采用零门户的重整化基准：** 明确写出例如 \(\lambda_{HS}(\mu_0)=0\) 的重整化条件、指定 \(\mu_0\)、重整化方案与匹配阈值，并计算从该条件演化到相关尺度后产生的有限混合。

不能仅因论文在基准中写了“negligible”就推断 \(\lambda_{HS}\) 在所有尺度严格为零，也不能把一个未指定重整化条件的低能泡图直接解释为唯一、物理且有限的混合角。

还需把下列对象分开记录：

\[
\Gamma^{(2)}_{hs}(p^2)=-\delta m_{hs}^2+p^2\delta Z_{hs}+\cdots,
\]

其中常数项、动量依赖项、门户反项和重阈值匹配分别承担不同作用。具体符号取决于有效作用量及自能的约定，后续必须先固定约定，再比较各项。

### 128.6 对现有 guide 中强结论的校准

原 guide 中出现了“简并处有限宽度本身即可正规化共振分母，因此全参数空间安全”“完全无需微调”“混合角始终低于实验排除线”等强表述。它们目前只能视为待检验的候选结论，原因如下：

1. 论文基准中的 \(m_s\gtrsim10\ \mathrm{GeV}\) 和公式 (34) 提供的是模型选择与微扰性条件，并不单独决定 \(\lambda_{HS}\) 的重整化值。
2. 仅以 \(\Gamma_h\) 和估计的 \(\Gamma_s\) 替换简并分母，不足以完整处理两个不稳定标量的混合。应使用一致的复数逆传播子矩阵，求复极点，并将其映射到实际信号强度或衰变率。
3. “微调程度很小”必须先定义被调参数、目标观测量及灵敏度度量；不能只凭某个圈图估算值小就得出结论。
4. LHC 的混合限制随 \(m_s\)、衰变分支比和产生/衰变道变化。不能用一个统一的 \(|\sin\theta|\) 数值代表整个质量区间，也不能把标量与矢量媒介的限制不加重算地互换。
5. “忽略 \(s\)”必须针对原论文真正计算的观测量验证误差。对低动量散射，传播子展开可给出 \(q^2/m_s^2\) 型运动学抑制，但耦合本身与 \(v_s\)、\(g_X\)、\(m_{A'}\) 的关系也必须保留；单凭 \(m_s>10\ \mathrm{GeV}\) 不能证明所有观测量都可忽略标量。

### 128.7 由原论文确定的后续计算顺序

1. **先固定完整拉氏量**：将 \(\lambda_{HS}(H^\dagger H)(S^\dagger S)\) 明确加入或说明其作为独立参数的处理；写出 \(H,S\) 展开、树级标量质量矩阵、\(hss\) 等相关顶角和全部符号约定。
2. **重新导出混合自能**：分别计算低能 \(\mu,\tau\) 图与 UV 重矢量类轻子图；核对手征投影、实/复标量归一化、味道对应的 \(S/S^*\)、Dirac 迹、闭合费米子圈符号及反项。
3. **完成 UV–EFT 一致匹配**：在相同外动量、重整化方案和 IR 处理下比较 UV 振幅与 EFT 振幅，分离软区复现项、硬阈值项和门户反项；未完成前不把任何单侧结果称作完整预测。
4. **求物理标量极点**：构造包含对角自能、非对角自能和衰变宽度的复数逆传播子矩阵；近简并时直接研究极点与可观测量，而不是继续使用非简并混合角公式。
5. **回到论文基准做数值扫描**：采用 \(m_s\gtrsim10\ \mathrm{GeV}\)、\(M_E>10\ \mathrm{TeV}\)、小轻—重混合角及公式 (34) 的条件，扫描 \((m_{A'},g_X,m_s,\lambda_{HS})\) 中真正独立的参数；若把门户耦合固定为零，须标出固定条件与尺度。
6. **定量检验标量退耦**：对论文实际使用的观测量，比较完整结果和忽略 \(s\) 的基准结果，给出相对误差及适用区间；随后才形成逐点英文回复。

### 128.8 可引用来源

- arXiv 摘要页（题目、作者、提交日期、摘要）：<https://arxiv.org/abs/2608.27258>
- HTML 全文，尤其第 II.1 节的电荷与 UV 拉氏量、第 II.2 节的质量基底耦合、第 II.3 节的标量基准与公式 (28)–(35)：<https://arxiv.org/html/2608.27258v1>

**本节结论：** 已将用户提供的论文身份、UV 电荷与相互作用、维数五 EFT、\(m_s\)–\(v_s\)–\(g_X\) 关系、公式 (34) 的微扰性约束和原文的标量退耦基准纳入主文档。下一步应以原论文的完整模型定义为准，先补齐 Higgs portal 的参数/重整化条件，再做完整的 UV–EFT 自能匹配；在这之前，不把 guide 中的简并安全性、无微调或全区间退耦结论当成已证实结果。

---

## 第129节：完整标量势与 Higgs-portal 重整化条件

### 129.1 原文明确写出的内容

已直接核对 arXiv:2608.27258v1 的 PDF 原文：

- 第 II.A 节式 (2) 将 UV 拉氏量写为包含 \,\(-V(S)\)，并将 \(V(S)\) 称为复标量 \(S\) 的自相互作用势；该式没有显式列出 \((H^\dagger H)(S^\dagger S)\) 项。
- 第 II.C 节式 (28) 明确给出
  \[
  V(S)=-\mu_S^2|S|^2+\lambda_S|S|^4,
  \]
  随后式 (29) 给出
  \[
  m_s=\sqrt{2\lambda_S}\,v_s,\qquad
  y_{s\ell\ell}\simeq\frac{m_\ell}{v_s}
  =\frac{2g_Xm_\ell}{m_{A'}}.
  \]
- 第 II.C 节在式 (34) 附近选择了 \(m_s\gtrsim10\,\mathrm{GeV}\) 且“negligible Higgs-portal mixing”的基准，并在式 (35) 将指定近似下的现象学参数化为 \((m_{A'},g_X)\)。
- 原文没有显式给出 \(\lambda_{HS}\) 的数值、边界条件、重整化尺度、重整化方案，或令其为零的匹配条件。全文文本检索也未找到 \(\lambda_{HS}\) 的显式定义。

这说明：**原论文确实采用了“门户混合可忽略”的现象学基准，但仅凭已写出的式 (2)、(28)、(34) 不能将其升级为“门户耦合在某一指定重整化尺度严格为零”的可复现重整化条件。** 也不能断言作者一定漏掉了该项；更谨慎的表述是，论文展示的模型/基准定义没有明确报告这项条件。

原文链接：
- 摘要及版本信息：<https://arxiv.org/abs/2608.27258>
- PDF 全文：<https://arxiv.org/pdf/2608.27258>

### 129.2 由规范对称性允许的最一般可重整化标量势

由于 \(H\) 是标准模型 Higgs 双重态、\(S\) 是标准模型单态，并且该模型中 \(H\) 在新增 \(U_A(1)_{L_\mu-L_\tau}\) 下不带荷，\(H^\dagger H\) 与 \(S^\dagger S\) 都是规范不变量。因此，若不额外施加原文未说明的对称性或参数条件，最一般的可重整化标量势包含

\[
\boxed{
V(H,S)=-\mu_H^2 H^\dagger H+\lambda_H(H^\dagger H)^2
-\mu_S^2 S^\dagger S+\lambda_S(S^\dagger S)^2
+\lambda_{HS}(H^\dagger H)(S^\dagger S).
}
\]

这里采用 \(+\lambda_{HS}\) 的势能符号约定。SM Higgs 势本身也没有在原文式 (2) 中完整重写，因此式 (2) 应理解为模型相互作用的展示，而不能仅凭该式判断完整标量势的全部项。

### 129.3 树级质量矩阵：门户项如何进入混合

取与原文一致的实真空期望值展开

\[
H=\frac{1}{\sqrt2}\begin{pmatrix}0\\v+h_0\end{pmatrix},\qquad
S=\frac{v_s+s_0}{\sqrt2},
\]
其中 \(h_0,s_0\) 是未对角化的 CP-even 场。在真空极小条件成立、并暂不计圈修正时，二次项为

\[
V^{(2)}=\frac12\begin{pmatrix}h_0&s_0\end{pmatrix}
\begin{pmatrix}
2\lambda_Hv^2 & \lambda_{HS}vv_s\\
\lambda_{HS}vv_s & 2\lambda_Sv_s^2
\end{pmatrix}
\begin{pmatrix}h_0\\s_0\end{pmatrix}.
\]

故树级非对角质量平方为

\[
\boxed{(M_0^2)_{hs}=\lambda_{HS}vv_s.}
\]

在非简并且 \(|\lambda_{HS}vv_s|\ll|m_{h,0}^2-m_{s,0}^2|\) 时，混合角的大小近似为

\[
|\theta|\simeq\left|\frac{\lambda_{HS}vv_s}{m_{h,0}^2-m_{s,0}^2}\right|,
\]
其中角度符号取决于旋转矩阵的定义。此近似在近简并区域失效，那里必须对完整质量矩阵或复数逆传播子矩阵对角化，不能把上式外推到分母接近零的区域。

这个关系直接说明：即使圈级非对角自能已算出，若 \(\lambda_{HS}\) 的树级输入/反项条件未知，仍不能唯一确定总的物理混合。

### 129.4 “忽略混合”应如何转化为可计算的重整化陈述

建议把论文中的基准至少补成以下两种明确选择之一。

**方案 A：指定重整化条件。** 例如在明确的方案和尺度 \(\mu_0\) 下规定 \(\lambda_{HS}(\mu_0)=0\)，并说明这是一项边界条件而非对所有尺度的恒等式。然后计算参数从 \(\mu_0\) 演化至相关尺度时的反项、阈值匹配和有限自能。

**方案 B：用物理混合条件定义参数。** 例如在指定外腿极点和重整化约定下，规定某个物理非对角二点函数满足给定条件；这需要把质量混合、动量依赖混合与场重整化的约定完整写明。

无论选哪一种，都不能将“negligible”直接替换成无尺度、无方案的 \(\lambda_{HS}=0\)。门户算符是规范允许的可重整化算符，因而其反项/重整化必须在完整量子理论中得到一致处理；重矢量类轻子与轻子 Yukawa 相互作用也可能给门户耦合带来圈级阈值或重整化贡献。其具体系数须由模型的完整图集、规范与重整化方案计算，当前不在没有推导的情况下预设数值。

### 129.5 与正在进行的 UV–EFT 计算如何衔接

后续混合计算必须把以下贡献分开，避免重复计数：

1. **树级门户项**：\(\lambda_{HS}(\mu)vv_s\) 产生的非对角质量项；
2. **完整 UV 自能**：重矢量类轻子、轻子及模型中其他相关自由度贡献的 \(\Pi^{\mathrm{UV}}_{hs}(p^2)\)；
3. **EFT 低能图**：维数五算符等低能自由度产生的 \(\Pi^{\mathrm{EFT}}_{hs}(p^2)\)；
4. **反项与匹配差**：在相同外动量、IR 处理和重整化方案下，UV 与 EFT 的差所确定的硬阈值贡献；
5. **物理极点**：将重整化后的非对角二点函数与两个对角传播子及宽度合并，求复数极点或目标观测量。

可统一写成

\[
\Gamma^{(2)}_{hs}(p^2)=-(M^2_{0})_{hs}
+\Pi^{\mathrm{ren}}_{hs}(p^2),
\]

但这里的符号需与后续选定的 1PI 自能和有效作用量约定一致。若采用 UV–EFT 匹配，则不能把 UV 与 EFT 中共同的软区贡献再次算进 Wilson 系数；也不能把未减去门户反项的单个圈图当成独立的有限物理混合角。

### 129.6 当前可确认与尚不可确认的结论

**可确认：** 原文式 (28) 的 \(V(S)\) 只写出 \(S\) 自相互作用；原文选取了 Higgs–singlet mixing 可忽略的现象学基准；规范对称性允许 \((H^\dagger H)(S^\dagger S)\) 项；若存在该项，树级非对角质量平方为 \(\lambda_{HS}vv_s\)。

**尚不可确认：** 作者实际采用的 \(\lambda_{HS}\) 数值或边界条件；该参数在何尺度、何方案下被设为可忽略；完整 UV 一圈阈值的有限部分；总混合角的数值；近简并区的排除或安全性；忽略混合对各实验观测量的定量误差。

### 129.7 下一步执行清单

1. 从原论文 TeX 源码和相关补充材料进一步核查是否存在正文未显式呈现的门户条件；若无，则把“论文未报告”作为结论，而不是猜测作者设定。
2. 固定势能符号、场展开、混合旋转矩阵、1PI 自能符号及重整化方案。
3. 以完整 UV 拉氏量计算门户耦合的相关反项/阈值，保留 \(y_\mu,y_\tau,\lambda_\mu,\lambda_\tau,M_{E_\mu},M_{E_\tau}\) 等实际模型参数，除非明确说明采用何种基准极限。
4. 对应计算 EFT 的同一 Green 函数，并做 UV–EFT 匹配，明确软区抵消与硬区差值。
5. 最后才将结果带入非简并和近简并的传播子分析，并对原论文的 \((m_{A'},g_X)\) 基准给出可复现数值扫描。

**本节结论：** 已从原论文直接核验出标量势和基准中未明确报告 \(\lambda_{HS}\) 的重整化条件，并推导了完整可重整化势及树级混合矩阵。当前最关键的缺口不是再估算一个孤立圈图，而是先固定门户参数的物理/重整化定义，再以一致的 UV–EFT 计算确定其圈级贡献。

---

## 第三部分：合并后的执行计划与最终交付标准

### 优先级 1：冻结模型输入

- 从原论文确认完整 UV 拉氏量、所有轻子/矢量类重轻子质量本征态、混合矩阵、标量势和门户项。
- 确认 \(s\) 与 \(h\) 的 Yukawa 耦合究竟是质量基底中的对角耦合还是近似表达式，并固定符号约定。
- 明确 \(\lambda_{HS}\) 的重整化边界条件：树级设为零、某尺度取零，或作为独立输入参数。这几种假设不等价。

### 优先级 2：完整计算 \(\Pi_{sh}(p^2)\)

- 分别计算低能轻子图与 UV 重态贡献，保留完整外动量依赖和复数部分。
- 统一 \(i\Pi\) 或 \(-i\Pi\) 的定义，独立核对费米子闭环符号、Dirac 迹、对称因子及 PV 积分约定。
- 给出重整化后的二点函数，并显式展示 UV–EFT 匹配差与尺度依赖的抵消。
- 把局域常数项和动量项分开，例如
  \[
  \Gamma^{(2)}_{hs}(p^2)=-\delta m_{hs}^2+p^2\delta Z_{hs}+\cdots.
  \]
  不能把 \(\delta Z_{hs}\) 直接等同于质量混合或混合角。

### 优先级 3：完成简并区分析

- 构造完整的复数二点函数/逆传播子矩阵，并求复极点。
- 说明“混合角”在近简并、不稳定粒子体系中的定义与适用范围。
- 对实际可观测信号计算信号强度或衰变率，并与质量相关的 LHC 约束逐点比较。
- 微调分析必须先定义被调参数、目标量和灵敏度度量，不能只根据分母很小或有限宽度非零作结论。

### 优先级 4：证明低能近似的适用范围

- 选定审稿人关心的具体观测量（例如指定的四费米子振幅或 \((g-2)_\mu\)）。
- 分别计算保留 \(s\) 与忽略 \(s\) 的结果，报告相对误差。
- 给出明确的质量/动量/耦合条件，并解释“形式上不能退耦”的模型参数来源。

### 优先级 5：生成审稿回复与论文修改

最终交付应包括：

1. 每条审稿意见的逐点英文回复；
2. 可直接加入正文的修订段落与公式；
3. 附录中的完整圈图和匹配推导；
4. 实验约束的可靠出处、参数适用范围和数据版本；
5. 数值代码/积分精度/输入参数表；
6. 明确的假设、误差和失效边界。

### 当前停止线

在完整 UV 拉氏量和门户重整化条件未确认、\(12\Delta\) 与 \(6\Delta\) 的系数差异未解决、UV–EFT 匹配未完成之前，不应把 guide 中“混合始终低于实验排除线”“有限宽度自动正规化共振”“完全无需微调”或“全低能范围均可忽略 \(s\)”写成已证明结论。可以把这些作为待检验的目标假设，但最终回复必须由计算结果决定。

---

# 145. EFT 的泡图与接触图：PV 表达式和发散结构

## 145.1 约定与相互作用

采用破缺相 EFT 相互作用
\[
\mathcal L_{\rm int}=-y_hh\bar\ell\ell-y_ss\bar\ell\ell-\kappa hs\bar\ell\ell,
\qquad y_h=\frac{m}{v_h},\quad y_s=\frac{m}{v_s},\quad \kappa=\frac{m}{v_hv_s},
\]
故 \(y_hy_s=\kappa m\)。定义
\[
A_0(m^2)=m^2\left(\Delta_\epsilon+1-\ln\frac{m^2}{\mu^2}\right),\qquad
B_0(p^2;m^2,m^2)=\Delta_\epsilon-\int_0^1dx\ln\frac{m^2-x(1-x)p^2-i0}{\mu^2}.
\]
这里的自能整体符号遵循本文此前采用的 1PI 约定；与其他文献比较时必须先统一 \(i\Pi\) 或 \(-i\Pi\) 的定义。

## 145.2 泡图

Dirac 迹为
\[
\operatorname{Tr}[(\slashed k+m)(\slashed k+\slashed p+m)]
=4[k\cdot(k+p)+m^2],
\]
并可化为
\[
4[k\cdot(k+p)+m^2]=2D_k+2D_{k+p}+(8m^2-2p^2),
\]
其中 \(D_k=k^2-m^2\)、\(D_{k+p}=(k+p)^2-m^2\)。据此，泡图写为
\[
\Pi_{hs}^{\rm bub}(p^2)=-\frac{y_hy_s}{16\pi^2}
\left[4A_0(m^2)+(8m^2-2p^2)B_0(p^2;m^2,m^2)\right].
\]

## 145.3 接触图与总和

由 \(\mathcal L_{\rm contact}=-\kappa hs\bar\ell\ell\)，接触图为
\[
\Pi_{hs}^{\rm ct}(p^2)=-\frac{4\kappa m}{16\pi^2}A_0(m^2)
=-\frac{4y_hy_s}{16\pi^2}A_0(m^2).
\]
所以
\[
\boxed{\Pi_{hs}^{\rm EFT}(p^2)=-\frac{y_hy_s}{16\pi^2}
\left[8A_0(m^2)+(8m^2-2p^2)B_0(p^2;m^2,m^2)\right]}
\]
以及
\[
\boxed{\Pi_{hs}^{\rm EFT}(p^2)\big|_{\rm UV}=-\frac{y_hy_s}{16\pi^2}(16m^2-2p^2)\Delta_\epsilon.}
\]
因此，EFT 圈图本身有常数型和动量型发散。前者需与标量势、参数、tadpole/VEV 等重整化统一处理；后者不能仅靠不含导数的 portal 势能反项消除。仅凭这两个图不能宣称匹配已完成。

# 146. 用单圈有效势独立核对 EFT 的零动量结果

## 146.1 场依赖质量与有效势

场依赖的费米子质量写为
\[
M(h,s)=m+y_hh+y_ss+\kappa hs,
\qquad \kappa=\frac{y_hy_s}{m}.
\]
对一个 Dirac 费米子，单圈有效势的有限部分为
\[
V_1(M)=-\frac{M^4}{16\pi^2}\left(\ln\frac{M^2}{\mu^2}-\frac32\right).
\]
令 \(L=\ln(m^2/\mu^2)\)，则
\[
V_1'(m)=-\frac{4m^3}{16\pi^2}(L-1),\qquad
V_1''(m)=-\frac{m^2}{16\pi^2}(12L-4).
\]
混合曲率必须同时包括 \(M\) 对两个场的一阶导数项，以及 \(M\) 中显式 \(hs\) 项产生的链式法则项：
\[
\begin{aligned}
\Pi_{hs}^{(V)}(0)
&=\left.\frac{\partial^2V_1}{\partial h\partial s}\right|_{h=s=0}\\
&=V_1''(m)y_hy_s+V_1'(m)\kappa\\
&=\boxed{-\frac{y_hy_sm^2}{16\pi^2}(16L-8)}.
\end{aligned}
\]
这里 \(\Pi_{hs}^{(V)}(0)\) 是有效势的混合曲率；它与某个具体逆传播子定义中的自能符号之间可能差一个整体符号，比较时必须固定 1PI 约定。

## 146.2 与泡图加接触图的比较

由第 145 节，
\[
\Pi_{hs}^{\rm EFT}(0)=-\frac{y_hy_s}{16\pi^2}
\left[8A_0(m^2)+8m^2B_0(0;m^2,m^2)\right].
\]
使用
\[
A_0(m^2)=m^2(\Delta_\epsilon+1-L),\qquad
B_0(0;m^2,m^2)=\Delta_\epsilon-L,
\]
得到
\[
\Pi_{hs}^{\rm EFT}(0)=-\frac{y_hy_sm^2}{16\pi^2}
\left[16\Delta_\epsilon+8-16L\right].
\]
有限部分为
\[
\Pi_{hs}^{\rm EFT}(0)\big|_{\rm finite}
=-\frac{y_hy_sm^2}{16\pi^2}(8-16L),
\]
与第 146.1 节的有效势曲率一致。**因此，零外动量的有限部分通过了独立交叉核对**，且泡图与接触图的相对归一化与有效势计算相容。

该结果的 UV 极点为
\[
\Pi_{hs}^{\rm EFT}(0)\big|_{\rm UV}
=-\frac{16y_hy_sm^2}{16\pi^2}\Delta_\epsilon.
\]
它需要由 EFT 反项和/或参数重整化贡献抵消，不要求未重整化的圈图自身有限。

## 146.3 动量型发散与规范不变算符

第 145 节的动量型极点为
\[
\Pi_{hs}^{\rm EFT}(p^2)\big|_{\rm UV}
\supset +\frac{2y_hy_sp^2}{16\pi^2}\Delta_\epsilon.
\]
一个可能产生混合动量二点结构的规范不变导数算符是
\[
\mathcal O_{\partial HS}=\partial_\mu(H^\dagger H)\,\partial^\mu(S^\dagger S).
\]
在 \(H^0=(v_h+h)/\sqrt2\)、\(S=(v_s+s)/\sqrt2\) 下，
\[
\mathcal O_{\partial HS}\supset v_hv_s\,\partial_\mu h\,\partial^\mu s.
\]
这说明导数算符可以提供所需的动量依赖局域结构。但这还不是完整反项证明：必须构造给定 EFT 阶数下的完整规范不变算符基底，并考虑分部积分、运动方程、场重定义以及可能的其他导数算符，才能判断独立反项的数目和系数。

## 146.4 结论边界与下一步

**已核对：** 泡图加接触图的 \(p^2=0\) 有限部分与单圈有效势曲率一致。

**尚未完成：**

1. 将自能符号统一到明确的逆传播子/1PI 约定；
2. 构造完整规范不变 EFT 反项基底，确定常数型与动量型极点的反项分配；
3. 纳入 Higgs/单态波函数重整化、费米子质量/Yukawa 重整化、tadpole 与 VEV 条件；
4. 在相同重整化方案、算符基底和外动量定义下，计算 UV 结果减去 EFT 软区后的有限阈值匹配。

完整 UV 理论中两态费米子路径求和的公共 UV 极点抵消，与 EFT 圈图具有非零极点并不矛盾。EFT 极点由 EFT 反项吸收；只有在两边采用一致的方案和算符基底后，才能比较有限匹配系数。当前不能宣称 UV–EFT 匹配已闭合。

---


# 147. 从二点函数极点到局域反项：常数项与动量项

## 147.1 先固定要抵消的 1PI 极点

沿用第 145–146 节的记号，EFT 圈图给出
\[
\Pi_{hs}^{\rm loop}(p^2)\big|_{\rm pole}
=-\frac{y_hy_s}{16\pi^2}(16m^2-2p^2)\Delta_\epsilon
=-\frac{16y_hy_sm^2}{16\pi^2}\Delta_\epsilon
+\frac{2y_hy_sp^2}{16\pi^2}\Delta_\epsilon.
\]
这里将 \(\Pi_{hs}\) 定义为前述计算采用的自能函数。为避免不同文献对逆传播子写成 \(p^2-M^2+\Pi\) 或 \(p^2-M^2-\Pi\) 所导致的符号歧义，本节把反项条件直接写成同一约定下的 1PI 核条件：
\[
\boxed{\Gamma^{(2)}_{hs,\,\rm ct}(p^2)\big|_{\rm pole}
=-\Pi_{hs}^{\rm loop}(p^2)\big|_{\rm pole}.}
\]
因此反项对二点核所需提供的极点结构是
\[
\Gamma^{(2)}_{hs,\,\rm ct}(p^2)\big|_{\rm pole}
=+\frac{16y_hy_sm^2}{16\pi^2}\Delta_\epsilon
-\frac{2y_hy_sp^2}{16\pi^2}\Delta_\epsilon.
\]
这条式子是当前符号约定下不依赖具体算符参数化的抵消条件。把它转换成拉格朗日量中某个 \(\delta\lambda_{HS}\) 或 \(\delta C_{\partial HS}\) 的符号时，必须从所采用的作用量和逆传播子定义重新展开，不能只凭直觉抄写符号。

## 147.2 常数型极点：portal 反项只是其中一个参数化

规范不变的标量势可以包含
\[
V(H,S)\supset \lambda_{HS}(H^\dagger H)(S^\dagger S),
\]
并在破缺后产生与 \(h s\) 成正比的二次项。若
\[
H^0=\frac{v_h+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2},
\]
则
\[
(H^\dagger H)(S^\dagger S)\supset v_hv_s\,hs.
\]
因此 portal 参数反项可为混合二点函数的常数部分提供局域贡献。不过，不能据此直接令其单独等于第 147.1 节的常数极点：在给定重整化条件下，混合二点函数还可能收到参数反项、VEV 反项、tadpole 方案以及场旋转/场归一化定义所诱导的贡献。只有把这些量放在同一个重整化方案中，才能求出可比较的 \(\delta\lambda_{HS}\)。

## 147.3 动量型极点：导数算符与二点核

一个可用来表示混合动量结构的规范不变维数六算符是
\[
\mathcal O_{\partial HS}=\partial_\mu(H^\dagger H)\,\partial^\mu(S^\dagger S),
\qquad
\delta\mathcal L=\frac{\delta C_{\partial HS}}{\Lambda^2}\mathcal O_{\partial HS}.
\]
在破缺后，双线性部分为
\[
\delta\mathcal L\supset
\frac{\delta C_{\partial HS}}{\Lambda^2}v_hv_s\,
\partial_\mu h\,\partial^\mu s.
\]
所以它确实能给混合二点核提供正比于 \(p^2\) 的局域项。若把破缺后动量混合反项的系数定义为 \(\delta Z_{hs}\)，使其在所选 1PI 约定下贡献为 \(\Gamma^{(2)}_{hs,\rm ct}\supset \delta Z_{hs}p^2\)，则第 147.1 节要求
\[
\boxed{\delta Z_{hs}\big|_{\rm pole}
=-\frac{2y_hy_s}{16\pi^2}\Delta_\epsilon.}
\]
这是对**破缺后二点核系数**的陈述，而不是尚未完成基底约化时对 \(\delta C_{\partial HS}\) 的最终匹配值。若仅由该算符贡献这一项，并按上述定义取其二点核系数为 \(\delta Z_{hs}=\delta C_{\partial HS}v_hv_s/\Lambda^2\)，则形式上需要
\[
\frac{\delta C_{\partial HS}}{\Lambda^2}v_hv_s\bigg|_{\rm pole}
=-\frac{2y_hy_s}{16\pi^2}\Delta_\epsilon.
\]
这一最后关系依赖于对该算符贡献的动量核符号约定；在将其用于论文前，必须从明确的度规、傅里叶变换和 1PI 定义重新核对符号。

## 147.4 为什么不能据此宣称已得到完整反项

1. \(\mathcal O_{\partial HS}\) 不是自动唯一的选择。分部积分、场重定义和运动方程可把某些导数结构转写为其他维数六算符；应在指定的非冗余规范不变基底中处理。
2. 两个维数五顶角的圈图在 EFT 中按相应阶数生成维数六局域结构。因此，若计算保留该阶的 \(p^2\) 极点，却在反项基底中只保留维数四标量势项，重整化一般不闭合。
3. 对常数极点，单个破缺后自能不能区分 portal 反项、参数/VEV 重整化和 tadpole 方案的贡献。要给出唯一系数，必须先写出完整裸参数替换并声明重整化条件。
4. 最终 UV–EFT 匹配应在同一算符基底与方案中进行。应先从 UV 振幅中减去 EFT 的软区贡献，再将剩余局域部分投影到 EFT 算符基底；不能把 UV 全理论圈图的极点抵消，直接当作 EFT 中每个算符系数的匹配结果。

## 147.5 本节结论与待办

本节已把 EFT 圈图极点转换为不依赖算符选择的二点核抵消条件，并识别了两类局域结构：常数型混合项与动量型混合项。动量型反项在上述定义下需要 \(\delta Z_{hs}|_{\rm pole}=-2y_hy_s\Delta_\epsilon/(16\pi^2)\)。但这还不是完整的规范不变反项推导；在得到非冗余维数六基底、场重定义规则和统一的参数/tadpole 重整化方案之前，不应把该结果解释成唯一的 \(\delta C_{\partial HS}\) 或 \(\delta\lambda_{HS}\) 匹配值。

**下一步计算顺序：** (i) 明确论文的完整 UV 拉格朗日量及其规范不变 EFT 基底；(ii) 固定 1PI/逆传播子、度规和傅里叶约定；(iii) 写出裸参数、场和 VEV 的反项替换；(iv) 计算维数六算符在所选基底中的混合与约化；(v) 计算 UV 振幅减去 EFT 软区后的有限局域部分，完成匹配。

# 148. 按 Wilson 系数阶数重新检查：动量极点是维数六，常数极点涉及更高阶背景场结构

> **对第 147.2 节的补充与限定。** 在破缺相的二点函数里，常数型极点可以形式上由一个混合质量反项抵消；但在未破缺的规范不变 EFT 中，不能仅凭破缺后的二点函数，就断言该极点应由维数四 portal 参数独自吸收。必须同时按 Wilson 系数的插入次数和算符维数做 power counting。

## 148.1 从维数五算符系数重新写出耦合

记
\[
C_5\equiv \frac{c_\ell}{\Lambda},\qquad [C_5]=-1,
\]
并沿用
\[
 m=\frac{C_5v_hv_s}{2},\qquad
 y_h=\frac{m}{v_h}=\frac{C_5v_s}{2},\qquad
 y_s=\frac{m}{v_s}=\frac{C_5v_h}{2}.
\]
于是
\[
\boxed{y_hy_s=\frac{C_5^2v_hv_s}{4}},\qquad
\boxed{y_hy_sm^2=\frac{C_5^4v_h^3v_s^3}{16}}.
\]
这里把 \(C_5\) 视为可能带相位的系数时，实际结果应写成与左右手耦合相乘的相应组合；以上实数表达式沿用前文实耦合约定。

## 148.2 动量型极点：与维数六导数算符的系数阶数一致

此前得到
\[
\Pi_{hs}^{\rm loop}(p^2)\big|_{p^2,\,\rm pole}
=+\frac{2y_hy_s}{16\pi^2}p^2\Delta_\epsilon
=+\frac{C_5^2v_hv_s}{2(16\pi^2)}p^2\Delta_\epsilon.
\]
同一 1PI 核约定下，反项必须贡献相反的极点。因此，若用
\[
\delta\mathcal L=\delta C_{\partial HS}\,
\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S)
\]
表示该导数结构（这里 \([\delta C_{\partial HS}]=-2\)，不再额外写 \(1/\Lambda^2\)），并且把其破缺后混合核定义为
\[
\Gamma^{(2)}_{hs,\rm ct}\supset
\delta C_{\partial HS}v_hv_s\,p^2,
\]
则该算符单独承接这一极点时所需的系数为
\[
\boxed{\delta C_{\partial HS}\big|_{\rm pole}
=-\frac{C_5^2}{2(16\pi^2)}\Delta_\epsilon.}
\]
这个关系的符号依赖本节明确声明的二点核约定；系数的阶数与维数则是稳健的：\(\delta C_{\partial HS}\sim C_5^2/(16\pi^2)\)，正是两个维数五算符插入所能产生的维数六反项阶数。完整基底中可能存在与该结构等价或混合的算符，故它是基底投影结果的候选表达，而非对任意基底都成立的唯一 Wilson 系数。

## 148.3 常数型极点：在未破缺 EFT 中不能只看成 portal 的重整化

常数极点为
\[
\begin{aligned}
\Pi_{hs}^{\rm loop}(0)\big|_{\rm pole}
&=-\frac{16y_hy_sm^2}{16\pi^2}\Delta_\epsilon\\
&=-\frac{C_5^4v_h^3v_s^3}{16\pi^2}\Delta_\epsilon.
\end{aligned}
\]
注意它在破缺后二点函数中含有 \(v_h^3v_s^3\)，并且按维数五系数计数是 \(C_5^4\) 阶，而不是 \(C_5^2\) 阶。其自然的未破缺 EFT 局域结构可以来自维数八势能算符，例如
\[
\mathcal O_8=(H^\dagger H)^2(S^\dagger S)^2,
\qquad [C_8]=-4,
\]
其中势能写作 \(V\supset C_8\mathcal O_8\)。在
\[
H^0=\frac{v_h+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2}
\]
下，\(\mathcal O_8\) 的 \(hs\) 二次项正比于 \(v_h^3v_s^3hs\)。因此，在只用这一算符承接该特定背景场结构、并将符号定义在同一 1PI 核约定下时，所需反项的量级为
\[
\boxed{\delta C_8\sim\frac{C_5^4}{16\pi^2}\Delta_\epsilon.}
\]
精确正负号应从 \(\delta V\)、\(\delta\mathcal L=-\delta V\) 和 1PI 二点核的定义统一推出；这里不把符号量级估计冒充成完整基底中的最终系数。

维数四 portal 算符 \((H^\dagger H)(S^\dagger S)\) 本身当然可以存在，也需要按模型和重整化方案处理。但其系数是独立的低维参数；仅把破缺后一个数值的常数极点吸收到 \(\delta\lambda_{HS}\) 中，并不能证明未破缺 EFT 的背景场依赖和 Wilson 系数阶数都已正确重整化。若按 EFT 阶数系统计算，必须考虑所有在该阶允许的局域算符、已有低维参数反项，以及 tadpole/VEV 定义。

## 148.4 这对后续匹配意味着什么

1. **维数六部分：** 两个 \(C_5\) 插入生成 \(C_5^2\) 阶的导数反项。应在选定的非冗余维数六基底中，计算 \(\mathcal O_{\partial HS}\) 与其他算符之间的约化/混合。
2. **常数部分：** 破缺后二点函数中的 \(C_5^4v_h^3v_s^3\) 极点提示，未破缺 EFT 的背景场展开可能需要维数八势能结构及同阶相关算符。不能仅靠一个破缺后混合质量反项来宣称规范不变 EFT 的重整化闭合。
3. **避免重复计数：** 如果在破缺相 EFT 中把 \(m\)、\(y_h\)、\(y_s\) 当作独立低能参数，常数极点可以在该参数化中由质量/混合反项吸收；但若要追溯到未破缺理论的 Wilson 系数，就必须恢复 \(m=C_5v_hv_s/2\) 的关系并按插入次数分类。
4. **匹配层次：** 应先声明目标是破缺相低能 EFT 的二点函数匹配，还是未破缺、规范不变 EFT 的 Wilson 系数匹配。两者的反项表述不必逐项相同，但物理振幅在一致截断阶数下必须一致。

## 148.5 更新后的结论

本次 power counting 给出更精细的解释：\(p^2\) 极点对应 \(C_5^2\) 阶、维数六导数结构；常数极点在使用 \(m=C_5v_hv_s/2\) 展开后对应 \(C_5^4v_h^3v_s^3\)，自然指向维数八背景场结构或破缺相参数反项。第 147.2 节关于 portal 反项的表述应理解为**破缺相二点核层面的可能参数化**，不能解读为未破缺规范不变 EFT 中由维数四 portal 单独吸收已经得到证明。

**下一项实质计算：** 在明确论文 EFT 的截断阶数后，先做未破缺背景场下的算符维数与 \(C_5\) 插入次数清单，再决定应计算到维数六还是维数八；随后在同一截断阶数下求圈图的局域极点并投影到选定算符基底。否则直接从破缺后 \(h-s\) 二点函数读出单个 Wilson 系数，会混淆不同 EFT 阶数。

# 149. 未破缺规范不变 EFT 的下一步：从场依赖质量识别算符结构

本节继续第 148 节，但先纠正一个容易导致基底不完整的简化：
\(\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S)\) 是可用的维数六导数结构之一，却不应在未做算符恒等式、分部积分和方程运动约化前，被视为费米子圈唯一生成的结构。更自然的起点是原始维数五算符所给出的场依赖质量。

## 149.1 场依赖质量与规范不变结构

考虑
\[
\mathcal L_5=-C_5 S\,\overline L H\ell_R+\mathrm{h.c.},
\qquad [C_5]=-1.
\]
在中性背景上，令
\[
H^0=\frac{v_h+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2},
\]
则费米子质量函数为
\[
M(H,S)=C_5 S H^0,
\qquad m=M(v_h,v_s)=\frac{C_5v_hv_s}{2},
\]
其中为简洁起见沿用实系数约定。圈图的局域 UV 结构可按场依赖质量及其导数分类：
\[
\text{无导数部分}\ \propto\ |M(H,S)|^4,
\qquad
\text{两导数部分}\ \propto\ \partial_\mu M^*\partial^\mu M.
\]
因此，无导数结构对应
\[
|M|^4\ \propto\ |C_5|^4(H^\dagger H)^2(S^\dagger S)^2,
\]
这是维数八势能结构，系数阶数为 \(|C_5|^4/(16\pi^2)\)。这与第 148 节从破缺后常数极点得到的 \(C_5^4v_h^3v_s^3\) 阶数相符。

## 149.2 两导数结构的规范协变完成

由于 \(S\) 是规范单态而 \(H\) 是 SU(2) 双重态，乘积 \(SH\) 仍是具有与 \(H\) 相同规范量子数的双重态。因而两导数结构应以规范协变形式组织，例如
\[
\mathcal O_{D,SH}=\big[D_\mu(SH)\big]^\dagger D^\mu(SH),
\qquad [\mathcal O_{D,SH}]=6.
\]
其系数阶数为 \(|C_5|^2/(16\pi^2)\)。展开可见它包含多种结构：
\[
\begin{aligned}
\mathcal O_{D,SH}={}&(S^\dagger S)(D_\mu H)^\dagger D^\mu H
+(H^\dagger H)\partial_\mu S^\dagger\partial^\mu S\\
&+(S^*\partial_\mu S)H^\dagger D^\mu H
+(S\partial_\mu S^*)(D^\mu H)^\dagger H.
\end{aligned}
\]
在破缺相中，这些项会共同贡献到标量动能混合、动能重整化及与规范场相关的相互作用。经过分部积分、场重定义和方程运动约化后，部分项可以改写为其他常用维数六基底算符；例如
\[
\partial_\mu(H^\dagger H)\,\partial^\mu(S^\dagger S)
\]
是一个允许的基底结构，但仅保留它未必能在任意基底中完整表示原始导数结构。

## 149.3 与破缺后二点函数的交叉核对

第 148 节的破缺相结果为
\[
\Pi_{hs}^{\rm loop}(p^2)\big|_{p^2,\mathrm{pole}}
=\frac{C_5^2v_hv_s}{2(16\pi^2)}p^2\Delta_\epsilon.
\]
这给出对完整规范不变导数算符组合的一个投影约束：在将全部相关维数六算符展开到 \(h,s\) 二次项后，其反项贡献必须抵消上式。它**不能单独决定每个维数六 Wilson 系数**，因为不同算符在破缺后可投影到同一个 \(p^2 hs\) 结构。

类似地，常数型极点约束维数八势能算符和破缺相参数反项的组合，而不自动单独决定 \((H^\dagger H)^2(S^\dagger S)^2\) 的系数。要提取该 Wilson 系数，必须在未破缺背景下计算有效作用量的场依赖极点，或等价地计算足够多外部标量腿的 1PI 函数，并将其投影到非冗余算符基底。

## 149.4 目前可以确定与尚不能确定的内容

**可以确定：**

1. 两个维数五插入所产生的两导数 UV 结构处于 \(|C_5|^2\) 阶，属于维数六算符组合。
2. 场依赖质量的四次结构处于 \(|C_5|^4\) 阶，包含维数八势能算符 \((H^\dagger H)^2(S^\dagger S)^2\)。
3. 破缺后二点函数只提供对相关 Wilson 系数组合的约束，不能无条件地唯一确定某个基底系数。

**尚不能宣称：**

- 已经得到完整维数六或维数八算符基底中的所有极点系数；
- 已经完成算符混合矩阵、EOM/分部积分约化或场重定义分析；
- 已经完成 UV 振幅与 EFT 软区的减法及有限匹配。

## 149.5 下一步的可执行计算顺序

1. 固定论文所用 EFT 截断：若仅保留维数五算符的一阶效应，则不应把由多次插入产生的高阶项混入同一阶匹配；若研究一圈且保留双插入，则至少检查维数六导数结构；若要解释上述常数极点的完整未破缺场依赖，则需扩展到相应的维数八阶。
2. 选定并写明非冗余的维数六、维数八算符基底及归一化。
3. 从 \(\mathrm{Tr}\log(i\slashed D-M(H,S))\) 的局域发散，或从等价的多外腿 1PI 函数，计算场依赖的导数项与势能项。
4. 用分部积分、规范恒等式及经典方程运动约化到所选基底，建立极点系数向量；单独标出场、参数、VEV 和 tadpole 反项。
5. 在相同截断、重整化方案和基底下计算 UV 理论的硬区贡献，并减去 EFT 对应软区贡献，最后才定义有限 Wilson 系数。

**阶段结论：** 现在已经明确了维数计数和规范协变的候选算符组合；下一步不应再从单个破缺后二点函数猜一个“唯一反项”，而应计算未破缺背景下的局域有效作用量并投影到明确定义的非冗余算符基底。

# 150. 未破缺背景下的局域一圈极点：场依赖质量的首轮投影

本节开始执行第 149.5 节的第 3 步。这里采用前文的 PV 极点约定，并用已经得到的破缺相二点函数极点校准局域泛函的系数。结论是**场依赖质量近似下的局域极点投影**，不是完整维数六/八算符基底的最终 anomalous-dimension 矩阵，也不是 UV–EFT 有限匹配。

## 150.1 从破缺相极点确定局域泛函的系数

此前 EFT 二点核的极点为
\[
\Pi_{hs}^{\rm EFT}(p^2)\big|_{\rm pole}
=-\frac{y_hy_s}{16\pi^2}(16m^2-2p^2)\Delta_\epsilon.
\]
因此
\[
\Pi_{hs}^{\rm EFT}(0)\big|_{\rm pole}
=-\frac{16y_hy_sm^2}{16\pi^2}\Delta_\epsilon,
\qquad
\Pi_{hs}^{\rm EFT}(p^2)\big|_{p^2,\rm pole}
=+\frac{2y_hy_s}{16\pi^2}p^2\Delta_\epsilon.
\]
用场依赖质量
\[
M(h,s)=m+y_hh+y_ss+\kappa hs,\qquad
\kappa=\frac{y_hy_s}{m},
\]
对候选无导数局域项 \(A M^4\) 求混合二阶导数。在背景点 \(h=s=0\)，有
\[
\frac{\partial^2 M^4}{\partial h\partial s}
=12m^2y_hy_s+4m^3\kappa
=16m^2y_hy_s.
\]
因此，与上述常数极点相容的局域势能极点为
\[
V_{\rm pole}^{\rm local}(M)
=-\frac{M^4}{16\pi^2}\Delta_\epsilon,
\]
这里的整体符号是按本文件所用的二点核约定校准的。它也说明接触顶角 \(\kappa hs\bar\ell\ell\) 不能漏掉：若只对线性质量项求导，会得到错误的 \(12\) 而不是 \(16\) 系数。

同样，将导数局域项写成 \(A_D\,\partial_\mu M^*\partial^\mu M\)，在实背景下其二次交叉项正比于 \(2A_D y_hy_s\partial h\partial s\)。与前述 \(p^2\) 极点相匹配给出结构系数
\[
A_D\big|_{\rm pole}=\frac{1}{16\pi^2}\Delta_\epsilon,
\]
其中将动能项转换为 1PI 核时的符号按前文约定理解。这个系数只由当前单个费米子通道及已定义的归一化固定；若改变 1PI 核或拉格朗日量的符号约定，书写的反项符号会随之变化，但极点抵消条件不变。

## 150.2 规范不变写法与维数计数

把中性背景推广回规范不变场，候选局域结构为
\[
\Gamma_{\rm pole}^{\rm local}\supset\int d^4x\left[
-\frac{|C_5|^4}{16\pi^2}(H^\dagger H)^2(S^\dagger S)^2
+\frac{|C_5|^2}{16\pi^2}[D_\mu(SH)]^\dagger D^\mu(SH)
\right]\Delta_\epsilon.
\]
此式的用途是记录由单一场依赖质量结构所提示的候选极点和插入阶数：

- \(|C_5|^2\) 项乘维数六算符，量纲为零；
- \(|C_5|^4\) 项乘维数八算符，量纲同样为零。

**重要限制：** 对一般复标量、完整电弱多重态及完整费米子内容，必须直接对规范不变背景计算行列式/热核系数，确认复数自由度、手征结构、规范场项以及算符归一化。上式不应在未经该核对时作为论文最终反项表格引用。特别是 \([D_\mu(SH)]^\dagger D^\mu(SH)\) 展开后对应一个算符组合；在非冗余基底中还需要把它约化到所选基底并记录 EOM/分部积分变换。

## 150.3 反项与圈图极点的关系

设 \(\Gamma_{\rm loop,pole}\) 表示圈图 1PI 泛函的极点，而 \(\Gamma_{\rm ct,pole}\) 表示反项泛函的极点。重整化要求
\[
\Gamma_{\rm loop,pole}+\Gamma_{\rm ct,pole}=0.
\]
因此，上述局域泛函系数首先描述的是按本节约定重建的**圈图局域极点结构**；写入反项拉格朗日量时应取相反号，并将该结构分配到选定基底中的 Wilson 系数反项。不能把圈图极点系数和 counterterm 系数不加区分地称为同一个量。

## 150.4 当前结果的交叉核对

1. **常数项：** \(V_{\rm pole}\propto M^4\) 的混合二阶导数同时包含 \(M_hM_s\) 与 \(M M_{hs}\) 两类项，复现 \(12+4=16\) 的系数；这核对了泡图与双标量接触顶角的相对贡献。
2. **动量项：** \(\partial M^*\partial M\) 的二次交叉项正比于 \(y_hy_s\partial h\partial s\)，具有所需的 \(|C_5|^2v_hv_s\,p^2\) 阶数，与维数六导数结构一致。
3. **维数：** \([C_5]=-1\)，所以 \(|C_5|^2\mathcal O_6\) 与 \(|C_5|^4\mathcal O_8\) 都是四维拉格朗日量中的维数四项。

## 150.5 尚未完成的必要步骤

这次计算没有证明上述两个结构构成完整的规范不变极点基底。完整计算仍须包含：

- 在一般 \(H,S\) 背景下对费米子行列式的直接计算，并核对复场/手征自由度因子；
- 所有与 \([D(SH)]^\dagger D(SH)\) 等价或相关的维数六算符，及其基底约化；
- 维数八势能及可能同时出现的其他独立规范不变算符；
- 参数、场、VEV、tadpole 反项的一致方案；
- UV 理论硬区振幅减去 EFT 软区振幅后的有限匹配。

**本节阶段结论：** 在已采用的破缺相二点核约定下，局域场依赖质量结构给出与已知极点相容的候选项 \(M^4\) 和 \(\partial M^*\partial M\)，并解释常数极点中的 \(16=12+4\)。接下来必须直接核对未破缺规范不变计算中的自由度和基底系数，才能把该候选投影升级为完整反项结果。

# 151. 将候选导数算符展开到规范不变结构：二点函数能确定什么？

本节把第 150 节中的
\[
\mathcal O_{D,SH}\equiv [D_\mu(SH)]^\dagger D^\mu(SH)
\]
展开为更细的规范不变结构。这里假设 \(S\) 是规范 singlet 复标量，\(H\) 是标准模型 Higgs 双重态；若论文对 \(S\) 的规范表示或算符归一化另有定义，应相应调整。

## 151.1 精确的乘积展开

因为 \(S\) 是规范 singlet，
\[
D_\mu(SH)=(\partial_\mu S)H+S D_\mu H.
\]
因此
\[
\begin{aligned}
\mathcal O_{D,SH}={}&(H^\dagger H)\,\partial_\mu S^*\partial^\mu S
+(S^\dagger S)(D_\mu H)^\dagger D^\mu H\\
&+S(\partial_\mu S^*)H^\dagger D^\mu H
+S^*(\partial_\mu S)(D_\mu H)^\dagger H.
\end{aligned}
\]
定义规范不变流
\[
J_S^\mu\equiv iS^\dagger\overleftrightarrow{\partial^\mu}S
=i(S^*\partial^\mu S-S\partial^\mu S^*),
\]
\[
J_H^\mu\equiv iH^\dagger\overleftrightarrow{D^\mu}H
=i[H^\dagger D^\mu H-(D^\mu H)^\dagger H].
\]
交叉项可以整理为
\[
S(\partial_\mu S^*)H^\dagger D^\mu H
+S^*(\partial_\mu S)(D^\mu H)^\dagger H
=\frac12\partial_\mu(S^\dagger S)\partial^\mu(H^\dagger H)
+\frac12 J_{S\mu}J_H^\mu.
\]
所以得到算符恒等式
\[
\boxed{
\begin{aligned}
\mathcal O_{D,SH}={}&(H^\dagger H)(\partial_\mu S^*\partial^\mu S)
+(S^\dagger S)(D_\mu H)^\dagger D^\mu H\\
&+\frac12\partial_\mu(S^\dagger S)\partial^\mu(H^\dagger H)
+\frac12 J_{S\mu}J_H^\mu.
\end{aligned}}
\]
这是一个算符组合，不是单独一个普适的“混合动能算符”。若采用包含右侧各项的非冗余基底，本次由场依赖质量得到的极点沿这四个结构的特定线性组合分布；还需结合分部积分、经典方程运动和场重定义，才能与指定基底的 Wilson 系数逐项对应。

## 151.2 破缺后径向二点函数的投影

取实径向背景
\[
H^0=\frac{v_h+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2},
\]
并暂时令 Goldstone/相位方向为零。此时在二次阶，
\[
|C_5|^2\,|\partial_\mu(SH^0)|^2
\supset \frac{|C_5|^2v_hv_s}{2}\,\partial_\mu h\,\partial^\mu s.
\]
另一方面
\[
y_h=\frac{|C_5|v_s}{2},\qquad y_s=\frac{|C_5|v_h}{2}
\]
（相位可通过场重定义选取；若保留复相位，应使用相应复共轭组合），故
\[
\frac{|C_5|^2v_hv_s}{2}=2y_hy_s.
\]
因此局域泛函中若含
\[
\frac{\Delta_\epsilon}{16\pi^2}|C_5|^2\mathcal O_{D,SH},
\]
其径向混合动能项的系数与此前二点核中的 \(p^2\) 极点阶数一致。这里仍沿用第 150 节的局域圈图泛函符号约定；反项泛函取相反号。

## 151.3 为什么一个径向二点函数不能确定所有系数

在实径向背景上，流 \(J_S^\mu\) 与 \(J_H^\mu\) 对纯径向涨落为零，因此 \(J_S\cdot J_H\) 的系数无法由 \(h-s\) 两点函数测出。其他导数算符也可能在给定真空处产生相同的 \(p^2\) 混合项。故二点函数只约束算符系数向量的一个投影，而不是整个维数六系数向量。

要确定完整基底中的系数，至少需要在未破缺背景下计算适当的多外腿 1PI 振幅，或直接计算一般复 \(H,S\) 背景下的局域有效作用量；之后再按指定的非冗余基底执行分部积分、EOM 与场重定义约化。

## 151.4 本节结论与下一步

1. 已把 \([D(SH)]^\dagger D(SH)\) 精确分解为四类规范不变维数六结构。
2. 破缺相径向二点函数与这组结构的特定组合相容，但无法分别测出全部 Wilson 系数。
3. 下一步应固定一套明确的非冗余基底，并计算能够区分这些结构的未破缺振幅；不能把第 150 节的组合系数直接报告成基底无关的单个 Wilson 系数。

**状态：** 本节完成了代数展开与二点函数投影分析；完整维数六算符混合矩阵、维数八反项表以及有限 UV–EFT 匹配仍未完成。

# 152. 将导数极点投影到显式算符集合，并设计可区分的振幅

本节把第 151 节的恒等式改写为 Wilson 系数向量，并说明需要哪些未破缺相位的振幅才能判断该组合是否真的是 UV 发散所选出的唯一结构。这里采用**冗余的张成集合**，不宣称它是已经完成 EOM/IBP 约化的非冗余 SMEFT/扩展 EFT 基底。

## 152.1 张成集合与系数向量

定义
\[
\begin{aligned}
O_1&=(H^\dagger H)(\partial_\mu S^*)(\partial^\mu S),\\
O_2&=(S^\dagger S)(D_\mu H)^\dagger D^\mu H,\\
O_3&=\partial_\mu(S^\dagger S)\,\partial^\mu(H^\dagger H),\\
O_4&=J_S^\mu J_{H\mu}.
\end{aligned}
\]
由第 151 节的逐项展开，严格有
\[
[D_\mu(SH)]^\dagger D^\mu(SH)
=O_1+O_2+\frac12O_3+\frac12O_4.
\]
因此，在第 150 节所采用的局域圈图极点符号约定下，候选发散泛函在这组**未约化**结构中的系数向量为
\[
\boxed{\vec C_{\rm pole}^{(6)}
=\frac{|C_5|^2}{16\pi^2}\Delta_\epsilon
\begin{pmatrix}1\\1\\1/2\\1/2\end{pmatrix}.}
\]
相应反项泛函取相反号。这个向量仅表示复合算符 \([D(SH)]^\dagger D(SH)\) 的代数展开；它不是在任意独立基底中都不变的 Wilson 系数列表。若做分部积分、使用经典运动方程或重定义场，系数会重新分配到其他导数算符、势算符以及 Yukawa 型算符中，而物理振幅不变。

## 152.2 为什么需要未破缺的四外腿振幅

在未破缺相位，考虑含两条 \(S,S^*\) 外腿与两条 Higgs 双重态外腿的局域四点振幅。四个结构的动量依赖具有不同的张量特征（以下只列结构，不包含整体的 \(i\)、对称因子和规范指标收缩）：

- \(O_1\)：导数作用在 \(S,S^*\) 上，产生与 \(p_S\!\cdot p_{S^*}\) 成正比的动量多项式；
- \(O_2\)：导数作用在两条 Higgs 腿上，产生与 \(p_H\!\cdot p_{H^*}\) 成正比的多项式；
- \(O_3\)：导数作用在两个双线性 \(S^\dagger S\) 和 \(H^\dagger H\) 上，产生两组双线性总动量的点积；
- \(O_4\)：由两个流相乘，动量结构对同一复场的粒子/反粒子腿交换呈反对称，且会探测 \(S\) 与 \(H\) 的相位/Goldstone 方向。

精确提取系数时必须固定所有外腿动量流入约定、复标量粒子/反粒子指认、规范指标收缩和整体振幅符号。还必须把所有能产生同样外态的树级 EFT 插入一并纳入：只对某个单独图的动量多项式拟合，可能把算符冗余误认成独立 Wilson 系数。

实用的投影方案是：

1. 在未破缺背景下，先算完整 UV 理论的 \(S S^* H_i H_j^*\) 一圈 1PI 四点振幅的局域 UV 极点；
2. 对同一外态计算 EFT 中维数五算符插入产生的全部一圈图，并使用同一正规化、规范和 IR 处方；
3. 作 UV 极点减 EFT 极点，得到硬区匹配的局域多项式；
4. 将该多项式投影到明确列出的独立动量张量，再通过指定的 IBP/EOM 规则约化到目标基底；
5. 用带有相位/Goldstone 外腿的相关振幅检查流算符方向，避免仅凭径向标量投影遗漏 \(O_4\) 或误判其系数。

## 152.3 对当前计算的含义

当前已知的 \(h-s\) 两点函数只提供零动量势方向和 \(p^2\) 导数方向的投影。第 150–152 节的局域表达式是与这些投影相容的候选规范不变结构；它尚不能证明完整 UV 理论的所有发散都由这一个组合吸收，也不能给出某个非冗余基底下的完整 anomalous-dimension/mixing 矩阵。

尤其需要区分：

- **反项闭合问题：** EFT 在选定截断阶数下是否必须加入所有由对称性允许、且实际被圈图产生的算符；
- **匹配问题：** UV 与 EFT 的同一振幅相减后，有限硬区部分给出哪些 Wilson 系数；
- **基底转换问题：** 这些系数经 IBP、EOM 和场重定义后如何映射到论文使用的参数与算符。

这三项不能由一个破缺相二点函数替代。下一步若要给出可以用于审稿回复的定量结论，必须实际完成 UV/EFT 四点振幅及其局域投影，而不是继续从同一个二点函数推断更多独立系数。

**状态更新：** 已明确写出候选导数极点在四算符张成集合中的系数向量，并给出区分其动量结构的匹配流程；UV 与 EFT 的四点圈图尚未计算，因此完整算符混合和有限匹配仍属未完成工作。

## 153. 四点振幅的动量多项式：哪些系数组合可被独立识别

本节把第 152 节的投影方案进一步具体化。目的不是声称已算出 UV 圈图，而是确定四个候选算符在指定外态上的树级局域顶角分别提供什么动量多项式，以及为什么必须选取足够多的运动学构型。

### 153.1 外腿与不变量约定

考虑过程的全入射记号
\[
S(p_1)+S^*(p_2)+H_i(p_3)+H_i^*(p_4)\to 0,
\qquad p_1+p_2+p_3+p_4=0.
\]
暂取外腿无质量以便展示独立动量结构，并定义
\[
s=(p_1+p_2)^2=(p_3+p_4)^2,\quad
 t=(p_1+p_3)^2,\quad
 u=(p_1+p_4)^2,
\]
所以 \(s+t+u=0\)。这只是算符投影的运动学简化；若匹配中存在非零外腿质量或红外敏感项，应在 UV 和 EFT 两侧使用完全相同的非零质量/红外处方，再作局域展开。

### 153.2 四个算符的顶角结构

对
\[
O_1=(H^\dagger H)(\partial_\mu S^*\partial^\mu S),\qquad
O_2=(S^\dagger S)(D_\mu H)^\dagger D^\mu H,
\]
在忽略规范场外腿时，导数直接落在各自的粒子—反粒子外腿上。因此它们的四点局域顶角分别正比于
\[
O_1:\ p_1\!\cdot p_2=\frac{s}{2},\qquad
O_2:\ p_3\!\cdot p_4=\frac{s}{2},
\]
整体正负号取决于将导数顶角、振幅 \(i\mathcal M\) 与拉氏量系数联系时采用的傅里叶变换约定。重要的是：在这组无质量外态上，二者都只给出 \(s\) 型结构，因而**单凭这一过程不能分别测出 \(C_1\) 与 \(C_2\)**。

对
\[
O_3=\partial_\mu(S^*S)\partial^\mu(H^\dagger H),
\]
两条复标量腿各自组成的双线性携带总动量。其顶角动量因子正比于
\[
(p_1+p_2)\!\cdot(p_3+p_4)=-s.
\]
因此，在上述四点、无质量、动量守恒的投影中，\(O_3\) 也落在同一个 \(s\) 型多项式方向。\(O_1,O_2,O_3\) 的系数在这个单一外态/运动学限制下存在投影简并；必须额外使用非零外腿质量、不同外态、带背景场的二点/三点函数，或先用明确的 IBP/EOM 规则约化算符基底，才能避免过度拟合。

最后，流算符
\[
O_4=J_S^\mu J_{H\mu}
\]
的四点顶角正比于粒子与反粒子动量之差的点积，可写成与
\[
(p_1-p_2)\!\cdot(p_3-p_4)=u-t
\]
成正比的结构（整体符号仍依流与傅里叶变换约定而定）。这给出与单纯 \(s\) 型项不同的交叉对称/角度依赖信息，因此适合用来检验流算符方向。若只计算径向背景或只保留一个特殊角度，可能会丢失这一独立信息。

### 153.3 投影矩阵与可识别性

在这个简化的四点投影中，可以把局域振幅写成
\[
\mathcal M_{\rm loc}(s,t,u)=A_s\,s+A_{tu}(u-t),
\]
其中 \(A_s\) 是 \(O_1,O_2,O_3\) 系数的某个线性组合，\(A_{tu}\) 则投影到 \(O_4\) 方向。该过程最多确定这两个组合，不能从两个数唯一反演四个系数。故完整匹配不能仅报告一条四点振幅的 \(s\) 项系数，并把它任意分摊给三个导数算符。

严格做法应先选定一个非冗余维数六基底（明确其是否使用分部积分、运动方程和场重定义），然后构造足够多的独立振幅/外态投影，使系数矩阵满列秩；若某些算符在所选外态上仍不可区分，就增加带规范/Goldstone 外腿的通道，或在基底约化时消去冗余方向。最终匹配系数应对基底约定和重整化方案作明确说明。

### 153.4 结论与边界

本节得到的是可识别性结论，而非新的圈图系数：在无质量 \(SS^*HH^*\) 单一通道中，三个候选标量导数结构都投影到 \(s\) 型方向，流算符投影到 \(u-t\) 型方向。因而至少需要两个独立运动学方向，且对前三个结构还需额外通道或基底约化。UV/EFT 一圈振幅、硬区差值、以及在论文目标基底中的数值 Wilson 系数仍未计算。

## 154. 用分部积分与标量运动方程检查导数算符冗余

第 153 节说明单一四点通道存在投影简并。本节进一步检查其中一个原因：候选集合中的
\[
O_3=\partial_\mu(S^\dagger S)\,\partial^\mu(H^\dagger H)
\]
并不必然是独立基底元素。它可通过分部积分改写成含标量运动方程的算符，从而与其他导数项、势算符及 EFT 源项发生关系。这里把关系写到足够明确的程度，但不在未指定完整标量势和 EOM 约定前，宣称已经得到最终非冗余基底。

### 154.1 分部积分恒等式

忽略边界项，令 \(A=S^\dagger S\)、\(B=H^\dagger H\)，则
\[
\boxed{\partial_\mu A\,\partial^\mu B\simeq -A\,\Box B\simeq -B\,\Box A.}
\]
这里 \(\simeq\) 表示在作用量中相差全导数，而不是逐点相等。另一方面，直接展开乘积的 d'Alembert 算符：
\[
\Box(S^\dagger S)=(\Box S^\dagger)S+S^\dagger\Box S+2\partial_\mu S^\dagger\partial^\mu S,
\]
因此有两条分别成立的等价关系
\[
\boxed{O_3\simeq -2O_1-(H^\dagger H)E_S,\qquad
O_3\simeq -2O_2-(S^\dagger S)E_H,}
\]
其中
\[
E_S=S^\dagger\Box S+(\Box S^\dagger)S,\qquad
E_H=H^\dagger D^2H+(D^2H)^\dagger H.
\]
注意这两条关系是分别由 \(O_3\simeq -(H^\dagger H)\Box(S^\dagger S)\) 与
\(O_3\simeq -(S^\dagger S)\Box(H^\dagger H)\) 得到的；不能把右侧两式直接相加后仍把左侧写成 \(O_3\)，否则会漏掉整体因子 \(1/2\)。余项可用相应运动方程改写，但必须保留 EOM 产生的势算符、其他相互作用算符和可能的费米子源项。

### 154.2 为什么不能在这里直接给出唯一的消元公式

要把上式进一步化成具体 Wilson 系数关系，至少需要固定以下信息：

1. 完整的标量势，例如 \(V(H,S)\) 中所有质量项、四次项及允许的混合项；
2. \(S\) 是复规范单态还是携带额外规范荷，以及其协变导数和规范相互作用；
3. 维数五 Yukawa 算符 \(C_5 S\bar L H\ell_R+\mathrm{h.c.}\) 是否属于当前 EOM 消元时保留的阶数；
4. 算符基底是否允许用经典 EOM 消去冗余项，以及采用何种场重定义约定。

尤其是，EOM 中的 \(\Box S\) 会带回标量势导数及 Yukawa 源项。若只保留 \(-2O_1\) 而丢掉其余项，就不是合法的基底转换，而是截断不一致。因此第 152–153 节四算符集合应继续理解为用于展开和诊断投影的**冗余张成集合**，而不是四个互相独立的物理 Wilson 系数。

### 154.3 对匹配计算的直接影响

正确顺序应是：

1. 先从 UV 与 EFT 振幅的差值提取一个明确的局域算符组合；
2. 把组合写入统一的冗余算符集合，核对其对各个所选外态振幅的投影；
3. 选定标量势与 EOM 约定，使用 IBP/EOM/场重定义映射到目标非冗余基底；
4. 在转换前后核对 on-shell 振幅不变，并记录所有被转移到势算符、Yukawa 算符或其他相互作用算符的系数。

这一步解释了为什么从一个 \(h-s\) 二点极点或一个 \(SS^*HH^*\) 四点振幅直接“读出”完整维数六混合矩阵并不可靠。

**本节状态：** 已推导 \(O_3\) 的 IBP 恒等式，并显示其与 \(O_1\) 及标量 EOM 项的关系；未指定完整势和目标基底，故尚未执行最终 EOM 消元，也未得到 UV/EFT 的一圈振幅差或有限匹配系数。

## 155. 导数算符的 IBP/EOM 约化：系数因子复核与修正版

本节把第 154 节的关系落实到复合算符
\[
O_{D,SH}=[D_\mu(SH)]^\dagger D^\mu(SH)
\]
并复核分部积分中容易遗漏的整体因子。这里假设 \(S\) 是规范单态复标量；若模型赋予 \(S\) 额外规范荷，必须相应替换协变导数并重新核对算符展开。

### 155.1 算符定义与代数恒等式

定义
\[
O_1=(H^\dagger H)(\partial_\mu S^\dagger\partial^\mu S),\quad
O_2=(S^\dagger S)(D_\mu H)^\dagger D^\mu H,
\]
\[
O_3=\partial_\mu(S^\dagger S)\partial^\mu(H^\dagger H),\quad
O_4=J_S^\mu J_{H\mu},
\]
其中
\[
J_S^\mu=iS^\dagger\overleftrightarrow{\partial^\mu}S,\qquad
J_H^\mu=iH^\dagger\overleftrightarrow{D^\mu}H.
\]
在上述约定下，复合导数结构的展开为
\[
\boxed{O_{D,SH}=O_1+O_2+\frac12O_3+\frac12O_4.}
\]
这是逐点成立的代数恒等式，不涉及运动方程或分部积分。

### 155.2 两条独立的 IBP 关系

令 \(A=S^\dagger S\)、\(B=H^\dagger H\)。忽略作用量中的全导数，
\[
O_3=\partial_\mu A\,\partial^\mu B\simeq -B\Box A\simeq -A\Box B.
\]
使用乘积求导恒等式
\[
\Box A=E_S+2\partial_\mu S^\dagger\partial^\mu S,
\qquad
\Box B=E_H+2(D_\mu H)^\dagger D^\mu H,
\]
其中
\[
E_S=S^\dagger\Box S+(\Box S^\dagger)S,\qquad
E_H=H^\dagger D^2H+(D^2H)^\dagger H,
\]
得到
\[
\boxed{O_3\simeq -2O_1-BE_S,\qquad
O_3\simeq -2O_2-AE_H.}
\]
两式各自成立，但不能把它们的右端直接相加后仍令左端等于 \(O_3\)。若取两式平均，正确结果是
\[
\boxed{O_3\simeq -O_1-O_2-\frac12(BE_S+AE_H).}
\]
这一步的整体因子是本节特别核验的重点。

### 155.3 对复合导数算符的约化表达

把第一条 IBP 关系代入代数恒等式，得到
\[
\boxed{O_{D,SH}\simeq O_2-\frac12(H^\dagger H)E_S+\frac12O_4.}
\]
使用第二条关系，也可写成
\[
\boxed{O_{D,SH}\simeq O_1-\frac12(S^\dagger S)E_H+\frac12O_4.}
\]
将两式平均则得到对称的等价表达
\[
\boxed{
O_{D,SH}\simeq \frac12O_1+\frac12O_2+\frac12O_4
-\frac14\left[(H^\dagger H)E_S+(S^\dagger S)E_H\right].
}
\]
这些关系在模去全导数的作用量中成立；它们还不是最终的非冗余基底 Wilson 系数。尤其不能在没有完整拉氏量时把 \(E_S,E_H\) 直接设为零：运动方程会把它们转成势算符、规范相互作用相关项和可能的 Yukawa 源项。

### 155.4 对径向二点投影的核验

对实径向背景
\[
H^0=\frac{v_h+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2},
\]
复合算符的导数部分给出
\[
|C_5|^2|\partial_\mu(SH^0)|^2
\supset \frac{|C_5|^2v_hv_s}{2}\,\partial_\mu h\partial^\mu s.
\]
用 \(m=C_5v_hv_s/2\)、\(y_h=m/v_h\)、\(y_s=m/v_s\)（实耦合约定）可写成系数 \(2y_hy_s\)。此径向投影只能核对二点函数中的动量结构；流算符 \(O_4\) 的相位/Goldstone 方向投影在纯径向背景上不可见，故单一 \(h-s\) 二点函数不能确定完整算符混合矩阵。

### 155.5 状态与未完成项

- [x] 复合导数结构的四项代数展开。
- [x] 分别推导 \(O_3\) 的两条 IBP 关系，并核对取平均时的整体因子。
- [x] 给出 \(O_{D,SH}\) 的三种等价 IBP 表示。
- [ ] 固定完整标量势、规范量子数、Yukawa 源项与 EFT 截断阶数。
- [ ] 选定明确的非冗余维数六基底，并构造 IBP/EOM 转换矩阵。
- [ ] 从原始 UV 拉氏量计算所需 1PI 振幅，与同一方案下的 EFT 泡图、接触图及反项作差。
- [ ] 区分 UV/IR 极点并检查 IR 抵消；提取非冗余 Wilson 系数、算符混合矩阵与 RG 方程。
- [ ] 用径向二点、Goldstone/相位外态、独立四点动量结构、简并质量极限和尺度抵消交叉核验。

**本节结论：** IBP/EOM 结构层面的代数关系已明确，并修正了把两条 IBP 关系相加时容易出现的因子错误；完整 UV–EFT 一圈匹配、有限 Wilson 系数和非冗余算符混合矩阵仍未完成。


## 156. 从 UV 背景场质量矩阵提取门户算符的单圈发散与有限有效势

### 156.1 目标与输入

本节直接从原论文 UV 质量矩阵开始，先检查该费米子扇区是否产生 \((H^\dagger H)(S^\dagger S)\) 的一圈加性 UV 极点，再建立可用于计算有限 \(h-s\) 混合的背景场有效势。这里使用的质量矩阵为

\[
\mathcal M_\ell(H,S)=
\begin{pmatrix}
0&y_\ell H^0\\
\lambda_\ell S_\ell&M_{E_\ell}
\end{pmatrix},\qquad S_\mu=S,\quad S_\tau=S^*.
\]

计算时暂不把背景场替换为真空期望值，并暂取 \(M_{E_\ell}\) 为实数；耦合可为复数。对单个味道简记
\[
a=y_\ell H^0,\qquad b=\lambda_\ell S_\ell,\qquad M=M_{E_\ell}.
\]

### 156.2 直接计算 \(\operatorname{Tr}[(\mathcal M^\dagger\mathcal M)^2]\)

首先
\[
\mathcal M^\dagger\mathcal M=
\begin{pmatrix}
|b|^2&b^*M\\
Mb&|a|^2+M^2
\end{pmatrix}.
\]
平方后取迹，得到
\[
\begin{aligned}
\operatorname{Tr}[(\mathcal M^\dagger\mathcal M)^2]
&=|b|^4+(|a|^2+M^2)^2+2M^2|b|^2\\
&=|a|^4+|b|^4+M^4+2M^2|a|^2+2M^2|b|^2.
\end{aligned}
\]

因此
\[
\begin{aligned}
\operatorname{Tr}[(\mathcal M_\ell^\dagger\mathcal M_\ell)^2]
={}&|y_\ell|^4|H^0|^4+|\lambda_\ell|^4|S|^4+M_{E_\ell}^4\\
&+2M_{E_\ell}^2|y_\ell|^2|H^0|^2
+2M_{E_\ell}^2|\lambda_\ell|^2|S|^2.
\end{aligned}
\]

**直接代数结论：** 这个迹中没有 \(|H^0|^2|S|^2\) 混合四次项。对标准模型 Higgs 双重态的背景方向而言，\(|H^0|^2\) 是 \(H^\dagger H\) 的中性背景分量；完整规范不变有效势的相应检验应使用完整双重态场依赖质量矩阵。当前迹的代数结构表明，在给定的这个费米子质量矩阵中，决定一圈费米子有效势 UV 极点的四次迹不含该混合项。

### 156.3 对门户反项的含义与边界

在维数正规化下，Dirac 费米子一圈有效势的 UV 发散部分正比于
\[
-\frac{1}{16\pi^2}\frac{1}{\bar\epsilon}
\operatorname{Tr}[(\mathcal M^\dagger\mathcal M)^2],\qquad
\frac1{\bar\epsilon}=\frac1\epsilon-\gamma_E+\ln4\pi,
\]
整体自由度计数应与质量本征态的 Dirac 简并度保持一致。由上一节迹的结果可得：
\[
\boxed{\left.\delta\lambda_{HS}\right|_{\text{该费米子扇区，一圈加性 UV 极点}}=0}
\]
该结论仅针对当前质量矩阵对应的费米子扇区和由它产生的一圈加性极点。它不意味着完整理论的 \(\lambda_{HS}\) 必须为零，也不排除有限阈值修正、其他扇区的贡献或门户耦合通过其他耦合的重整化群演化。

必须分别记录：

1. **UV 极点：** 当前迹结构没有门户四次混合项。
2. **有限阈值：** UV 极点抵消不等于有限有效势中的混合导数为零。
3. **完整 beta 函数：** 还需计算标量、规范及其他相关扇区，不能由该费米子迹单独推出。

### 156.4 背景场质量本征值与一圈有效势

质量平方本征值由 \(\mathcal M^\dagger\mathcal M\) 的迹和行列式给出：
\[
T=M^2+|a|^2+|b|^2,\qquad
\det(\mathcal M^\dagger\mathcal M)=|ab|^2,
\]
\[
\boxed{m_\pm^2=\frac{T\pm\sqrt{T^2-4|ab|^2}}{2}.}
\]
这里
\[
T=M_{E_\ell}^2+|y_\ell|^2|H^0|^2+|\lambda_\ell|^2|S|^2,
\quad |ab|^2=|y_\ell|^2|\lambda_\ell|^2|H^0|^2|S|^2.
\]
所以尽管四次迹的发散部分不含门户混合项，质量本征值仍同时依赖两个背景场，有限有效势不能由 UV 极点结构直接判定为无混合。

若该矩阵的两个奇异值分别对应两个 Dirac 质量本征态，则该味道的一圈 Coleman–Weinberg 有效势为
\[
V_1^{(\ell)}(H,S)=-\frac1{16\pi^2}\sum_{\sigma=\pm}m_{\ell,\sigma}^4(H,S)
\left[\ln\frac{m_{\ell,\sigma}^2(H,S)}{\mu^2}-\frac32\right].
\]
对 \(\ell=\mu,\tau\) 求和即得当前重轻子混合系统的费米子一圈有效势。该表达式假设每个奇异值对应一个 Dirac 费米子；若原始模型的独立态计数不同，必须按实际自由度修正，不能重复计数。

### 156.5 从有效势提取零动量混合

取径向背景
\[
H^0=\frac{v+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2}
\]
并暂不包含 Goldstone 方向。有效势诱导的零外动量混合核为
\[
\boxed{\Pi_{hs}^{\mathrm{eff}}(0)=
\left.\frac{\partial^2 V_1^{\mathrm{fermion}}}{\partial h\,\partial s}\right|_{h=s=0}.}
\]
这提供了一个独立于直接二点函数 PV 积分的核验路径。实际求导时，必须同时对 \(m_+^2(H,S)\)、\(m_-^2(H,S)\) 的显式背景依赖求导，并保留链式法则中的一阶、二阶导数项；不能只对对数因子求导。

有效势只能直接核验 \(p^2=0\) 的静态曲率。它不决定完整 \(p^2\)-依赖自能，也不能替代含有波函数/动能反项的二点函数计算。最终 UV–EFT 匹配仍须在相同重整化方案中比较 UV 1PI、EFT 泡图、双标量接触图和反项。

### 156.6 当前进度核验表

- [x] 从给定 UV 质量矩阵直接计算 \(\mathcal M^\dagger\mathcal M\)。
- [x] 展开 \(\operatorname{Tr}[(\mathcal M^\dagger\mathcal M)^2]\)，检查门户四次混合项。
- [x] 得到当前费米子扇区没有一圈加性门户 UV 极点的结论，并限定其适用范围。
- [x] 写出精确背景场质量平方本征值和一圈有效势。
- [ ] 显式计算 \(\partial_h\partial_s V_1|_{h=s=0}\)，给出可简化的有限表达式。
- [ ] 与 UV 二点函数在 \(p^2=0\) 的 PV 结果独立交叉核验。
- [ ] 计算一般 \(p^2\) 下的 UV 自能，并与 EFT 泡图、接触图、反项作差。
- [ ] 加入其余相关扇区，确定完整 \(\beta_{\lambda_{HS}}\)、阈值匹配和物理混合角。

**本节结论：** 已完成门户算符 UV 极点的迹检验，并构造了有限有效势的精确起点；有限混合导数和完整 UV–EFT 匹配尚未完成。不要将“当前费米子扇区的加性极点为零”写成“门户耦合或物理混合恒为零”。

## 157. 有限 Coleman–Weinberg 混合导数：显式链式求导公式

本节完成第 156 节清单中的第一项：把背景场一圈有效势的混合二阶导数写成可直接代入参数的解析公式。该结果是费米子 Coleman–Weinberg 有效势在零外动量下的贡献，不等同于一般外动量的完整 1PI 自能。

### 157.1 将背景场变量改写为两个非负不变量

对单个味道定义
\[
x=|H^0|^2,\qquad z=|S|^2,\qquad
u=|y_\ell|^2x,\qquad w=|\lambda_\ell|^2z,\qquad q=M_{E_\ell}^2.
\]
为避免把变量 \(u\) 与 Yukawa 参数混淆，以下将 \(\nu\) 简写为 \(U\)。于是
\[
T=q+U+w,\qquad Q=T^2-4Uw,\qquad R=\sqrt Q,
\]
\[
L_\sigma=m_{\ell,\sigma}^2=\frac{T+\sigma R}{2},\qquad \sigma=\pm1.
\]
一圈有效势写为
\[
G(U,w)=-\frac1{16\pi^2}\sum_{\sigma=\pm1}
L_\sigma^2\left(\ln\frac{L_\sigma}{\mu^2}-\frac32\right).
\]

### 157.2 所需的一阶和混合二阶导数

定义
\[
Q_U=2T-4w,\qquad Q_w=2T-4U.
\]
则
\[
R_U=\frac{Q_U}{2R},\qquad R_w=\frac{Q_w}{2R},
\]
以及
\[
R_{Uw}=-\frac1R-\frac{Q_UQ_w}{4R^3}.
\]
因此
\[
(L_\sigma)_U=\frac12\left(1+\sigma\frac{Q_U}{2R}\right),\qquad
(L_\sigma)_w=\frac12\left(1+\sigma\frac{Q_w}{2R}\right),
\]
\[
(L_\sigma)_{Uw}=\frac{\sigma}{2}R_{Uw}.
\]
令
\[
f(L)=-\frac{L^2}{16\pi^2}\left(\ln\frac{L}{\mu^2}-\frac32\right),
\]
则
\[
f'(L)=-\frac{2L}{16\pi^2}\left(\ln\frac{L}{\mu^2}-1\right),\qquad
f''(L)=-\frac{2}{16\pi^2}\ln\frac{L}{\mu^2}.
\]
由链式法则得到可直接计算的结果：
\[
\boxed{
G_{Uw}=\sum_{\sigma=\pm1}\left[
f''(L_\sigma)(L_\sigma)_U(L_\sigma)_w
+f'(L_\sigma)(L_\sigma)_{Uw}\right].
}
\]
这条表达式完全由本节定义的 \(T,Q,R,L_\sigma\) 和对数函数构成，不需要对本征值再做数值差分。若 \(R\to0\)，上述分项会出现表观的 \(1/R\) 奇点；原始谱函数的对称总和应取连续简并极限，不能把两个本征态的单独奇点解释为物理发散。

### 157.3 转回径向场并给出混合核

在实径向背景
\[
H^0=\frac{v+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2}
\]
下，真空处
\[
\frac{\partial U}{\partial h}=|y_\ell|^2v,\qquad
\frac{\partial w}{\partial s}=|\lambda_\ell|^2v_s,
\]
且 \(U\) 不显含 \(s\)、\(w\) 不显含 \(h\)。因此该味道对零动量混合的 Coleman–Weinberg 贡献为
\[
\boxed{
\left.\frac{\partial^2 V_{1,\ell}}{\partial h\,\partial s}\right|_0
=|y_\ell|^2|\lambda_\ell|^2vv_s\,G_{Uw}\bigg|_{U=|y_\ell|^2v^2/2,\;w=|\lambda_\ell|^2v_s^2/2}.
}
\]
对 \(\ell=\mu,\tau\) 求和即可得到这两个费米子混合系统的有效势贡献：
\[
\left.\Pi_{hs}^{\rm CW}(0)\right|_{\mu,\tau}
=\sum_{\ell=\mu,\tau}|y_\ell|^2|\lambda_\ell|^2vv_s\,G_{Uw}^{(\ell)}.
\]
量纲检查：\(G\) 的量纲为质量四次方，\(G_{Uw}\) 因对两个质量平方变量求导而为无量纲；乘以 \(vv_s\) 后结果具有质量平方量纲，符合混合质量核的量纲。

### 157.4 解释范围与独立核验

1. 该结果是背景场有效势的混合曲率，即零外动量、有效势近似下的贡献。
2. 它不是一般 \(p^2\) 的完整自能；动量依赖、场重整化以及其他 UV 扇区仍须单独计算。
3. 该公式不能单独决定物理混合角。还需要树级门户项、重整化条件、反项和完整质量矩阵。
4. 由于第 156 节的 UV 极点迹中没有门户混合四次项，当前费米子扇区的该项没有一圈加性门户 UV 极点；这并不要求上述有限混合曲率为零。
5. 下一步应将该解析结果在若干非简并参数点与对原始 \(V_1(H,S)\) 做符号/高精度数值二阶差分所得结果比较，再独立计算 UV 费米子自能在 \(p^2=0\) 的 PV 表达式。两者一致后，才可把该有效势结果作为交叉核验。

- [x] 将 \(\partial_h\partial_s V_1|_0\) 写成解析链式求导公式。
- [x] 完成量纲检查，并明确简并极限的处理原则。
- [ ] 用独立数值差分验证解析公式。
- [ ] 与完整 UV 1PI 自能在 \(p^2=0\) 的 PV 结果交叉核验。
- [ ] 计算一般 \(p^2\) 的自能，并完成 EFT 泡图、接触图、反项的 UV–EFT 相减。

## 158. Coleman–Weinberg 混合导数的独立数值交叉核验

本节对第 157 节的解析链式求导式做独立数值检验。检验只针对给定的背景质量矩阵及其一圈 Coleman–Weinberg 势，不替代完整 UV 1PI 自能的 PV 计算。

### 158.1 检验方法

直接从质量平方本征值
\[
L_\pm(h,s)=\frac{T(h,s)\pm\sqrt{T(h,s)^2-4U(h)w(s)}}2
\]
构造原始有效势
\[
V_1(h,s)=-\frac1{16\pi^2}\sum_{\sigma=\pm}L_\sigma(h,s)^2
\left[\ln\frac{L_\sigma(h,s)}{\mu^2}-\frac32\right].
\]
对称混合差分取为
\[
D_{hs}(\delta)=\frac{V_1(\delta,\delta)-V_1(\delta,-\delta)
-V_1(-\delta,\delta)+V_1(-\delta,-\delta)}{4\delta^2}.
\]
当 \(\delta\to0\) 时，该表达式收敛到 \(\partial_h\partial_sV_1|_0\)。这项检验直接对原始背景场有效势求值，而不是复用第 157 节中本征值对 \(U,w\) 的导数公式。

### 158.2 一组非简并测试点

采用一组仅用于代数检验的任意一致质量单位参数：
\[
M_E^2=2.7,\quad \mu^2=1.3,\quad y=0.7,\quad
\lambda=0.9,\quad v=1.1,\quad v_s=0.8.
\]
解析链式求导给出
\[
\left.\partial_h\partial_sV_1\right|_0
=-0.00350508165946515322595620720789.
\]
对原始 \(V_1(h,s)\) 做中心混合差分得到：

| \(\delta\) | 中心混合差分 \(D_{hs}(\delta)\) | 与解析值的绝对差 |
|---:|---:|---:|
| \(10^{-2}\) | \(-0.0035050092172359645\) | \(7.24\times10^{-8}\) |
| \(10^{-3}\) | \(-0.0035050809350333164\) | \(7.24\times10^{-10}\) |
| \(10^{-4}\) | \(-0.0035050816522208339\) | \(7.24\times10^{-12}\) |
| \(10^{-5}\) | \(-0.0035050816593927100\) | \(7.24\times10^{-14}\) |

差值随步长缩小按约 \(\delta^2\) 下降，与中心差分的截断误差预期一致。由此在该非简并测试点上，解析链式求导公式与直接对原始 Coleman–Weinberg 势做数值差分相符。

### 158.3 本次核验能说明什么、不能说明什么

- [x] 在一个非简并参数点上，以不同步长对原始背景场有效势进行中心混合差分；数值收敛到第 157 节解析结果。
- [x] 解析值与数值差分的偏差呈现二阶步长收敛，支持链式求导实现无明显代数错误。
- [ ] 仍需在多个随机非简并参数点及接近但不等于简并的点重复检验，以排除实现细节错误。
- [ ] 仍需独立计算 UV 费米子 1PI 混合自能在 \(p^2=0\) 的 Passarino–Veltman 表达式，并核对自由度、符号、重整化方案与有效势曲率之间的关系。
- [ ] 仍需计算一般 \(p^2\) 的 UV 自能，与 EFT 泡图、双标量接触图及反项相减；本节数值验证不能证明完整 UV–EFT 匹配已经完成。

**阶段结论：** 第 157 节的 Coleman–Weinberg 混合二阶导数通过了一组独立数值差分检验。下一项关键工作是从原始 UV 拉氏量和费米子混合顶角出发，独立建立 \(p^2=0\) 的 1PI/PV 结果并与该曲率核对；在完成该项前，不应宣称两种方法已经互相验证。

## 159. 多组非简并参数点的有效势导数复核

为避免第 158 节只依赖单个测试点，再选取四组非简并输入，对解析式与直接背景场中心差分作比较。各组均保持参数一致性：\(U=|y|^2v^2/2\)、\(w=|\lambda|^2v_s^2/2\)，并采用同一 \(\mu^2=1.17\)（任意一致质量单位）。中心差分步长为 \(\delta=10^{-4}\)。

| 测试点 | \(q=M_E^2\) | \(U\) | \(w\) | 解析混合曲率 | 直接中心差分 | 绝对差 |
|---|---:|---:|---:|---:|---:|---:|
| A | 3.4 | 0.21 | 0.37 | \(-0.00503680202894362336\) | \(-0.00503680201621768891\) | \(1.27\times10^{-11}\) |
| B | 1.9 | 0.05 | 0.61 | \(-0.000547997920250447728\) | \(-0.000547997919830504213\) | \(4.20\times10^{-13}\) |
| C | 4.2 | 0.72 | 0.11 | \(-0.0195182768643766553\) | \(-0.0195182767123491477\) | \(1.52\times10^{-10}\) |
| D | 2.1 | 0.33 | 0.29 | \(-0.00516157596939307215\) | \(-0.0051615759529230178\) | \(1.65\times10^{-11}\) |

四组结果均相符，差异与有限差分截断误差量级一致。结合第 158 节的步长收敛测试，可以认为：在所检验的非简并参数区域内，第 157 节解析混合导数公式通过了数值交叉核验。

**仍未解决的核心问题：** 这些测试只验证“解析求导公式是否正确实现了给定的 Coleman–Weinberg 势”，不验证质量矩阵是否完整代表原模型，也不验证 PV 自能、反项或 UV–EFT 匹配。下一步必须回到论文的完整 UV 拉氏量，确认手征基底和 Yukawa 顶角后，独立计算零外动量 1PI 自能；若要与有效势曲率逐项比较，还必须统一自能符号约定、自由度计数和重整化方案。

## 160. UV 1PI 自能的独立代数审计：修正质量基底迹系数并重算 PV 核

本节继续上一阶段的核心任务：在计算 UV 与 EFT 的匹配前，先从质量基底的完整手征顶点重新检查通道权重。审计发现，第 37–38 节在把 Yukawa 矩阵元素转换为迹系数时仍多出一个整体因子 2。以下从定义重新推导；本节给出的通道矩阵和 PV 核**取代第 37–38 节中相应的系数矩阵与总核**。整体 1PI 自能的最终正负号仍需与选定的有效作用量约定统一。

### 160.1 从完整手征顶点直接构造两个系数

实耦合下，定义
\[
(\Gamma_h)_{ij}=(Y_h)_{ij}P_R+(Y_h)_{ji}P_L,\qquad
(\Gamma_s)_{ji}=(Y_s)_{ji}P_R+(Y_s)_{ij}P_L.
\]
在迹
\[
\mathrm{Tr}[(\slashed k+m_i)(\Gamma_h)_{ij}
(\slashed k+\slashed p+m_j)(\Gamma_s)_{ji}]
=2C_{ij}\,k\cdot(k+p)+2D_{ij}m_im_j
\]
中，利用 \(P_{R,L}^2=P_{R,L}\)、\(P_RP_L=0\) 及标准 Dirac 迹，可得
\[
\boxed{C_{ij}=(Y_h)_{ij}(Y_s)_{ij}+(Y_h)_{ji}(Y_s)_{ji}},
\]
\[
\boxed{D_{ij}=(Y_h)_{ij}(Y_s)_{ji}+(Y_h)_{ji}(Y_s)_{ij}}.
\]
注意这里的 \(C,D\) 已经是上面迹公式中因子 2 以外的系数；不应再把矩阵元素的两个相加项额外乘 2。

代入论文 Eq. (13) 的实耦合矩阵
\[
Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix},
\]
并定义
\[
K=2ab\,c_Ls_Lc_Rs_R,\qquad J=ab(c_L^2c_R^2+s_L^2s_R^2),
\]
得到
\[
\boxed{C=K\begin{pmatrix}1&-1\\-1&1\end{pmatrix}},\qquad
\boxed{D=\begin{pmatrix}K&-J\\-J&K\end{pmatrix}}.
\]
因此第 37–38 节写成 \(C=2K\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\)、\(D_{11}=D_{22}=2K\) 的形式多了因子 2。这不是整体圈因子问题，而是通道迹系数定义处的代数错误。

### 160.2 重新求和四个有序通道

沿用第 38 节的 PV 约定，令
\[
A_i=A_0(m_i^2),\quad B_{ij}=B_0(p^2;m_i^2,m_j^2),\quad S_m=m_1^2+m_2^2.
\]
单个有序通道、尚未乘闭合费米子圈整体因子的核为
\[
F_{ij}=C_{ij}\left[A_i+A_j+(m_i^2+m_j^2-p^2)B_{ij}\right]
+2D_{ij}m_im_jB_{ij}.
\]
逐通道代入新的 \(C,D\) 矩阵：
\[
F_{11}=2KA_1+K(4m_1^2-p^2)B_{11},
\]
\[
F_{22}=2KA_2+K(4m_2^2-p^2)B_{22},
\]
\[
F_{12}=F_{21}=-K(A_1+A_2)
+\left[-K(S_m-p^2)-2Jm_1m_2\right]B_{12}.
\]
将两个非对角有序通道都计入后，\(A_0\) 项严格抵消，得到修正后的总 PV 核
\[
\boxed{\begin{aligned}
F_{\rm corr}(p^2)={}&K(4m_1^2-p^2)B_{11}
+K(4m_2^2-p^2)B_{22}\\
&+\left[-2K(S_m-p^2)-4Jm_1m_2\right]B_{12}.
\end{aligned}}
\]
这是迹与 PV 约化层级的结果；要变成 \(\Pi_{hs}^{\rm UV}\)，仍须按固定的 1PI 定义补上费米子圈、顶点和传播子的整体因子。

### 160.3 UV 极点核对与精确对角化恒等式

若质量矩阵对角化给出的恒等式为
\[
K S_m=2Jm_1m_2,
\]
则 \(F_{\rm corr}\) 的 UV 极点系数为
\[
K(4m_1^2)+K(4m_2^2)-2KS_m-4Jm_1m_2
=4KS_m-2KS_m-2KS_m=0.
\]
因此修正后的总核仍然具有 UV 极点抵消，但抵消是在正确的通道权重下得到的。将恒等式代入有限函数前，不能把各个 \(B_0\) 的有限部分删掉；极点抵消不意味着有限阈值为零。

在零外动量处，PV 核简化为
\[
\boxed{F_{\rm corr}(0)=4Km_1^2B_{11}(0)+4Km_2^2B_{22}(0)-4KS_mB_{12}(0)},
\]
其中已使用 \(4Jm_1m_2=2KS_m\)。这里的 \(B_{ij}(0)\) 仍包含其各自有限的对数质量依赖；共同 \(\Delta\) 极点因 \(4K(m_1^2+m_2^2)-4KS_m=0\) 抵消。

### 160.4 与 Coleman–Weinberg 曲率的关系及当前边界

对同一 UV 费米子系统，在一致的有效作用量约定下，零动量 1PI 混合二点函数应与一圈有效势的混合曲率相联系。但不能直接将上式的 \(F_{\rm corr}(0)\) 与第 157 节的曲率数值比较：前者尚未恢复完整图的整体符号/归一化，后者则由给定背景质量矩阵构造。接下来需要完成：

1. 从原始拉氏量逐项固定 \(i\Pi\) 或 \(\Pi\) 的定义，明确费米子圈负号、两个顶点的 \(-i\) 因子和传播子分子中的 \(i\) 因子；
2. 由精确质量矩阵和旋转矩阵数值生成 \(m_{1,2},c_{L,R},s_{L,R}\)，检查 \(KS_m=2Jm_1m_2\)；
3. 采用同一组参数直接比较 \(\partial_h\partial_s V_1|_0\) 与恢复整体因子后的 \(\Pi_{hs}^{\rm UV}(0)\)；
4. 然后才把 \(p^2\ne0\) 的 UV 结果与 EFT 泡图、双标量接触图及反项作差。

**状态更新：**
- [x] 从完整手征顶点重算 \(C_{ij},D_{ij}\)，发现并修正第 37–38 节多出的因子 2。
- [x] 用修正系数重新求和四个有序通道，并复核总核的 UV 极点抵消。
- [ ] 固定完整 1PI 整体因子，并与 Coleman–Weinberg 混合曲率作数值核验。
- [ ] 完成一般 \(p^2\) 下 UV–EFT 相减和规范不变反项匹配。

## 161. 零动量 UV 自能与 Coleman–Weinberg 曲率的数值交叉核验

本节完成第 160.4 节提出的第一项定量检查。目的不是宣称整个模型的匹配已完成，而是固定一个具体的非简并参数点，检验修正后的 PV 核在恢复整体因子后，是否与同一质量矩阵构造的一圈有效势混合曲率一致。

### 161.1 测试输入与质量基底

采用单味道、实参数背景质量矩阵
\[
\mathcal M(h,s)=\begin{pmatrix}0&m_L(1+h/v_h)\\m_R(1+s/v_s)&M_E\end{pmatrix},
\]
并取一致的任意质量单位
\[
M_E=5.0,\quad m_L=0.7,\quad m_R=0.4,\quad v_h=v_s=1,\quad \mu^2=1.3.
\]
通过对该矩阵作实奇异值分解得到正质量本征态，再用同一左右旋转将 \(\partial\mathcal M/\partial h\) 与 \(\partial\mathcal M/\partial s\) 转到质量基底。按第 160 节的定义构造 \(C,D\)，并将质量态按轻、重排序。该点的质量为
\[
m_1=0.0552891899604,\qquad m_2=5.06428110451.
\]
系数为
\[
K=0.00596098988320,\qquad J=0.273034625900,
\]
且数值验证
\[
K(m_1^2+m_2^2)=0.152899390504
=2Jm_1m_2
\]
（显示位数内一致）。因此本测试点满足第 160 节使用的精确对角化恒等式。

### 161.2 PV 有限部分

在零外动量，使用
\[
B_0(0;a,b)= -\int_0^1dx\,\ln\!\left(\frac{xa+(1-x)b}{\mu^2}\right)
\]
表示去掉共同 UV 极点后的有限部分，并代入第 160.3 节的修正核，得到
\[
F_{\rm corr}^{\rm fin}(0)=-0.610280342425.
\]
按当前 PV 归一化，恢复整体圈因子后
\[
\frac{F_{\rm corr}^{\rm fin}(0)}{16\pi^2}=-0.00386464541551.
\]

### 161.3 与有效势混合曲率比较

独立地直接从背景矩阵 \(\mathcal M(h,s)\) 计算 \(\mathcal M^\dagger\mathcal M\) 的两个本征值平方，并构造 Dirac 费米子的一圈 Coleman–Weinberg 势
\[
V_1(h,s)=-\frac1{16\pi^2}\sum_{i=1}^2m_i^4(h,s)\left[\ln\frac{m_i^2(h,s)}{\mu^2}-\frac32\right].
\]
用中心混合差分
\[
D_{hs}(\delta)=\frac{V_1(\delta,\delta)-V_1(\delta,-\delta)-V_1(-\delta,\delta)+V_1(-\delta,-\delta)}{4\delta^2}
\]
在 \(\delta=10^{-3}\) 时得到
\[
D_{hs}(10^{-3})=-0.00386464704683.
\]
与 PV 结果之差约为 \(1.63\times10^{-9}\)，相对差约为 \(4.2\times10^{-7}\)。该差异与中心差分的有限步长误差一致。更小步长在双精度下出现消减误差，因此不能仅凭双精度下步长继续缩小就期待误差单调改善。

### 161.4 本次交叉核验能说明什么

在这一组参数和所用约定下，修正后的 PV 核满足
\[
\boxed{\Pi_{hs}^{\rm UV}(0)=\frac{F_{\rm corr}(0)}{16\pi^2}}
\]
并与直接由有效势计算的混合曲率相符。这同时支持本节的整体归一化选择与第 160 节的零动量有限核；它比单纯检查 UV 极点抵消更强，因为这里还比较了质量依赖的有限部分。

但结论范围仍然有限：这是一个实参数、单味道、指定重整化尺度的数值点。正式完成还需要以高精度数值或解析二阶导数重复多个参数点，并将 \(p^2\ne0\) 的完整 UV 自能与 EFT 泡图、双标量接触图及反项作差。特别是，Coleman–Weinberg 曲率只检验零动量极限，不足以决定导数维数六算符的匹配系数。

**状态更新：**
- [x] 固定一个非简并参数点，数值生成质量本征值和质量基底顶角。
- [x] 检查精确对角化恒等式 \(K(m_1^2+m_2^2)=2Jm_1m_2\)。
- [x] 比较 PV 零动量有限核与直接 Coleman–Weinberg 混合曲率；两者在数值误差内一致。
- [ ] 用高精度或解析导数扩展至多个参数点。
- [ ] 完成一般 \(p^2\) 的 UV–EFT 相减、反项与规范不变算符匹配。

## 162. 多参数高精度交叉核验：零动量 PV 核与有效势混合曲率

本节完成第 161.4 节列出的多参数验证。为避免有限差分误差，采用高精度算术直接对 Coleman–Weinberg 势作混合二阶导数，并独立用质量基底的 PV 有限核计算 
\[
\Pi_{hs}^{\rm PV}(0)=\frac{F_{\rm corr}^{\rm fin}(0)}{16\pi^2}.
\]
每组参数均从背景矩阵
\[
\mathcal M(h,s)=\begin{pmatrix}0&m_L(1+h/v_h)\\m_R(1+s/v_s)&M_E\end{pmatrix}
\]
重新作实奇异值分解，计算质量基底的两个 Yukawa 矩阵，并据此构造第 160 节的 \(K,J\)。PV 有限部分使用
\[
B_0^{\rm fin}(0;m_i^2,m_j^2)=-\int_0^1dx\,\ln\!\frac{x m_i^2+(1-x)m_j^2}{\mu^2}.
\]
有效势二阶导数则由高精度微分直接求出，而不是通过有限步长差分估计。

### 162.1 数值结果

下表中所有质量和真空期望值均以同一任意质量单位表示。最后两列分别是两种独立方法的结果与其相对差；相对差按 \(|(\Pi_{\rm PV}-\Pi_{\rm CW})/\Pi_{\rm CW}|\) 定义。

| 点 | \((M_E,m_L,m_R,v_h,v_s,\mu^2)\) | \(\Pi_{\rm CW}(0)\) | \(\Pi_{\rm PV}(0)\) | 相对差 |
|---|---|---:|---:|---:|
| A | \((5,0.7,0.4,1,1,1.3)\) | \(-3.86464541551246031\times10^{-3}\) | \(-3.86464541551246455\times10^{-3}\) | \(1.10\times10^{-15}\) |
| B | \((3,0.8,0.25,2,1.4,2.1)\) | \(-6.68025273893232929\times10^{-4}\) | \(-6.68025273893232823\times10^{-4}\) | \(1.58\times10^{-16}\) |
| C | \((7,0.45,0.9,1.3,0.8,4.0)\) | \(-7.82040695330095988\times10^{-3}\) | \(-7.82040695330095395\times10^{-3}\) | \(7.58\times10^{-16}\) |
| D | \((2.5,0.3,0.6,1.1,1.7,0.9)\) | \(-8.12587188259217136\times10^{-4}\) | \(-8.12587188259216786\times10^{-4}\) | \(4.31\times10^{-16}\) |
| E | \((10,1.2,0.2,2.2,0.9,3.3)\) | \(-1.45210509949477940\times10^{-3}\) | \(-1.45210509949477749\times10^{-3}\) | \(1.31\times10^{-15}\) |

对每个点还独立检查了对角化恒等式
\[
K(m_1^2+m_2^2)-2Jm_1m_2=0.
\]
其残差均在约 \(10^{-16}\) 或更小的绝对量级，符合双精度 SVD 输入精度；有效势微分与 PV 积分本身采用高精度算术。

### 162.2 结论与解释边界

五组互不相同的参数点均显示，修正后的零动量 PV 有限核与由同一背景质量矩阵构造的 Coleman–Weinberg 混合曲率一致，相对差约为 \(10^{-16}\)–\(10^{-15}\)。这显著强于单点有限差分测试，支持以下有限结论：

1. 第 160 节的修正 PV 核与当前质量矩阵下的一圈有效势在 \(p^2=0\) 一致；
2. 使用的整体归一化 \(1/(16\pi^2)\) 与当前有效势约定相符；
3. 质量基底系数与精确对角化恒等式在多组非简并参数下相容。

但这**仍不是完整 UV–EFT 匹配的证明**。PV 核和有效势计算都使用了同一个背景质量矩阵和由它导出的顶角，因此它们之间的吻合不能验证该矩阵是否已完整包含原论文 UV 拉氏量的所有场依赖、规范结构或其他扇区。更重要的是，零动量曲率不决定 \(p^2\) 项的系数。

### 162.3 下一步的计算顺序

下一阶段应固定完整 1PI 自能的定义与符号约定，然后在低于轻态阈值的欧氏动量区间计算 \(F_{\rm corr}(p^2)\)，对 \(p^2\) 作解析或数值展开：
\[
\Pi_{hs}^{\rm UV}(p^2)=\Pi_{hs}^{\rm UV}(0)+p^2\,\Pi_{hs}^{\rm UV\prime}(0)+O(p^4).
\]
随后必须用同一质量、同一重整化方案计算 EFT 泡图和双标量接触图，并从 UV–EFT 差中分离局域常数项和 \(p^2\) 项。只有后者与规范不变算符基底及其 EOM/IBP 关系对应起来，才能确定导数算符的匹配系数。

**状态更新：**
- [x] 在五组参数点用高精度有效势微分与 PV 有限核交叉核验零动量混合曲率。
- [x] 在每组参数点检查质量基底恒等式及 UV 极点抵消关系。
- [ ] 从原论文完整 UV 拉氏量核实质量矩阵、旋转约定和所有相关顶角。
- [ ] 完成一般 \(p^2\) 的 UV 自能与 EFT 泡图、接触图及反项的相减。
- [ ] 将匹配出的动量项映射到规范不变算符基底，并检查 EOM/IBP 一致性。

## 163. 一般动量展开的下一步：EFT 自能斜率及 UV–EFT 相减的可执行表达式

本节继续第 162.3 节的计划，先把 EFT 侧的低动量斜率单独算清楚，再明确与 UV 侧比较时必须统一的约定。这里沿用文档前面定义的 EFT 一圈结果

\[
\Pi_{hs}^{\rm EFT}(p^2)=-\frac{y_hy_s}{16\pi^2}\left[8A_0(m^2)+(8m^2-2p^2)B_0(p^2;m^2,m^2)\right],
\]

以及

\[
A_0(m^2)=m^2\left(\Delta_\epsilon+1-\ln\frac{m^2}{\mu^2}\right),\qquad
B_0(p^2;m^2,m^2)=\Delta_\epsilon-\int_0^1 dx\ln\frac{m^2-x(1-x)p^2-i0}{\mu^2}.
\]

### 163.1 计算 EFT 的 \(p^2=0\) 斜率

对两点函数求导，注意 \(A_0\) 与外动量无关：

\[
\frac{d\Pi_{hs}^{\rm EFT}}{dp^2}=-\frac{y_hy_s}{16\pi^2}\left[-2B_0(p^2)+(8m^2-2p^2)B_0'(p^2)\right].
\]

由参数积分直接得到

\[
B_0(0;m^2,m^2)=\Delta_\epsilon-\ln\frac{m^2}{\mu^2},\qquad
B_0'(0;m^2,m^2)=\int_0^1dx\frac{x(1-x)}{m^2}=\frac{1}{6m^2}.
\]

所以

\[
\boxed{\left.\Pi_{hs}^{{\rm EFT}\prime}(p^2)\right|_{0}=-\frac{y_hy_s}{16\pi^2}\left[-2\Delta_\epsilon+2\ln\frac{m^2}{\mu^2}+\frac43\right].}
\]

这与先前的 EFT 自能极点
\(\Pi_{hs}^{\rm EFT}(p^2)|_{\rm pole}=-(y_hy_s/16\pi^2)(16m^2-2p^2)\Delta_\epsilon\)
一致：对 \(p^2\) 求导后，其极点为 \(+2y_hy_s\Delta_\epsilon/(16\pi^2)\)。这是对 EFT 斜率极点符号的直接交叉检查。

### 163.2 UV 侧斜率与 EFT 侧斜率的相减规则

定义 UV 侧完整 1PI 两点函数为

\[
\Pi_{hs}^{\rm UV}(p^2)=\Pi_{hs}^{\rm UV}(0)+p^2\Pi_{hs}^{{\rm UV}\prime}(0)+O(p^4),
\]

并以相同外场归一化、相同 \(i\Pi\) 符号约定和相同重整化方案定义 EFT 侧。则局域低能匹配应由

\[
\boxed{\Delta\Pi_{hs}'(0)=\Pi_{hs}^{{\rm UV}\prime}(0)-\Pi_{hs}^{{\rm EFT}\prime}(0)}
\]

提取，而不能直接把 UV 的 \(F'(0)\) 当作 Wilson 系数。文档前面的 UV PV 推导给出一个候选有限组合 \(F'(0)\)，但第 160 节明确指出它还依赖整体因子和约定；在这些信息统一前，不应把两者相减后报出数值系数。

此外，\(\Delta\Pi_{hs}'(0)\) 本身是背景径向场的二点函数斜率。要把它映射为规范不变维数六算符系数，还必须在同一 EFT 基底中包括可能的场重定义、波函数重整化、EOM/IBP 等价算符，以及其它会贡献到相同二点结构的算符。单个混合二点函数一般不足以唯一确定所有 Wilson 系数。

### 163.3 本节结论与未完成事项

- [x] 从 EFT 泡图加双标量接触图表达式解析求得 \(\Pi_{hs}^{{\rm EFT}\prime}(0)\)。
- [x] 由 \(B_0'(0)=1/(6m^2)\) 核验 EFT 斜率的 UV 极点符号。
- [ ] 由原论文完整 UV 拉氏量确认质量基底 Yukawa 顶角和整体 1PI 符号。
- [ ] 将 UV 侧 \(F'(0)\) 恢复成与 EFT 同约定的 \(\Pi_{hs}^{{\rm UV}\prime}(0)\)，并逐项相减。
- [ ] 把所得动量项匹配到完整规范不变算符基底，检查波函数重整化、场重定义和 EOM/IBP。

因此，本节完成的是 EFT 斜率的解析推导与匹配公式的固定，而不是完整的 UV–EFT 数值匹配。下一步应先从原论文拉氏量核实 UV 顶角与归一化，再计算可比较的 UV–EFT 差。

## 164. 依据原论文 UV 拉氏量核实质量矩阵、标量顶角与门户发散结构

### 164.1 原论文拉氏量与场依赖矩阵

本节依据原论文 arXiv:2608.27258v1 第 II.1 节式 (2)–(6) 与第 II.2 节式 (13) 核对输入。相关 UV 相互作用为

\[
\mathcal L_{\rm UV}\supset -y_\mu\bar L_\mu H E_{\mu R}
-\lambda_\mu S\bar E_{\mu L}\mu_R
-M_{E\mu}\bar E_{\mu L}E_{\mu R}+\mathrm{h.c.},
\]

\[
\mathcal L_{\rm UV}\supset -y_\tau\bar L_\tau H E_{\tau R}
-\lambda_\tau S^*\bar E_{\tau L}\tau_R
-M_{E\tau}\bar E_{\tau L}E_{\tau R}+\mathrm{h.c.}.
\]

对单个味道块，质量矩阵在背景场下应写为

\[
\mathcal M_\ell(H,S)=\begin{pmatrix}0&a_\ell\\b_\ell&M_{E\ell}\end{pmatrix},\qquad
 a_\ell=y_\ell H^0,\quad
 b_\mu=\lambda_\mu S,\quad b_\tau=\lambda_\tau S^*.
\]

这里沿用论文的实参数约定进行显式代数计算；若耦合或质量带复相位，迹结果需用模平方表达。对径向实背景，\(H^0=(v_h+h)/\sqrt2\)，\(S=(v_s+s)/\sqrt2\)，于是

\[
\frac{\partial\mathcal M_\ell}{\partial h}
=\begin{pmatrix}0&y_\ell/\sqrt2\\0&0\end{pmatrix},\qquad
\frac{\partial\mathcal M_\ell}{\partial s}
=\begin{cases}\begin{pmatrix}0&0\\\lambda_\mu/\sqrt2&0\end{pmatrix},&\ell=\mu,\\[4pt]
\begin{pmatrix}0&0\\\lambda_\tau/\sqrt2&0\end{pmatrix},&\ell=\tau\text{，在实径向背景上}.
\end{cases}
\]

这与论文式 (13) 的规范基底顶角一致；质量基底顶角必须再分别施加左右手旋转，不能把单一的实正交旋转同时用于左右手扇区。

### 164.2 由矩阵不变量核验一圈 UV 极点

令 \(M=M_{E\ell}\)，则

\[
\mathcal M^\dagger\mathcal M=
\begin{pmatrix}
|b|^2&b^*M\\
Mb&|a|^2+M^2
\end{pmatrix},
\]

从而

\[
\boxed{\operatorname{Tr}[(\mathcal M^\dagger\mathcal M)^2]
=|a|^4+|b|^4+M^4+2M^2|a|^2+2M^2|b|^2.}
\]

该迹中没有 \(|a|^2|b|^2\) 项。因此，在这个费米子块的单圈有效势 UV 极点中，不产生 \((H^\dagger H)(S^\dagger S)\) 的加性发散。这个结论仅针对该质量矩阵给出的费米子一圈有效势发散部分；它**不**意味着完整理论的门户耦合恒为零，也不排除有限阈值、其他扇区贡献或高阶 RG 贡献。

质量平方本征值满足

\[
T=M^2+|a|^2+|b|^2,\qquad \det(\mathcal M^\dagger\mathcal M)=|ab|^2,
\]

\[
m_\pm^2=\frac12\left[T\pm\sqrt{T^2-4|ab|^2}\right].
\]

它们与论文式 (8) 在 \(a=m_L\)、\(b=m_R\) 的真空背景记号下相同。这里的迹恒等式也为 CW 有效势发散结构提供了不依赖质量本征态旋转角的检查。

### 164.3 对后续 UV–EFT 相减的影响

本节核实了原论文的场依赖质量矩阵和规范基底标量顶角，并重新确认费米子一圈有效势的门户四次发散缺项。但这**还没有**完成一般外动量下的 UV 自能斜率。有效势只决定零动量曲率；要得到 \(\Pi_{hs}^{{\rm UV}\prime}(0)\)，仍需用原论文式 (13) 的完整左右手质量基底顶角计算 1PI 两点图，逐个内部质量通道处理，并与第 163 节 EFT 结果采用一致的自能符号、外场归一化和重整化方案。

### 164.4 当前核验清单

- [x] 依据原论文式 (2)–(6) 核实单味道 UV 质量矩阵的场依赖结构。
- [x] 依据原论文式 (13) 核实规范基底中 \(h\) 与 \(s\) 的独立矩阵顶角，并确认质量基底需左右手分别旋转。
- [x] 从 \(\operatorname{Tr}[(\mathcal M^\dagger\mathcal M)^2]\) 独立核验该费米子扇区门户 UV 极点的缺项。
- [ ] 以明确的 1PI 费曼规则重新计算一般 \(p^2\) 下的 UV 自能及其导数，并固定整体符号和自由度因子。
- [ ] 与 EFT 泡图、双标量接触图及反项逐项相减。
- [ ] 将匹配差映射至完整规范不变算符基底，并检查波函数重整化、EOM/IBP 与场重定义。

## 165. UV 1PI 两点图：先固定手征迹与内部味道求和，不预设整体符号

本节把第 164 节的质量基底顶角改写成可直接用于一圈自能的形式。这里先独立固定**分子迹与味道指标**；在没有把传播子、顶角的所有因子及 自能定义统一之前，不把这个分子结果直接称作最终的 \(\Pi_{hs}\) 或 Wilson 系数。

### 165.1 顶角与指标约定

在质量基底中写

\[
\mathcal L_{\rm scalar}=-h\,\bar\chi(Y_hP_R+Y_h^\dagger P_L)\chi
-s\,\bar\chi(Y_sP_R+Y_s^\dagger P_L)\chi,
\]

其中 \(Y_h,Y_s\) 是论文式 (13) 的两个实矩阵（若参数取实）。对矩阵迹中的一条有序内部通道，令传播子质量分别为 \(m_j\) 与 \(m_i\)，并记

\[
h_{ij}=(Y_h)_{ij},\qquad s_{ij}=(Y_s)_{ij}.
\]

取未积分分子

\[
N_{ij}(k,q)=\operatorname{tr}_{D}\!\left[
(h_{ij}P_R+h_{ji}^{*}P_L)(\slashed k+m_j)
(s_{ji}P_R+s_{ij}^{*}P_L)(\slashed k+\slashed q+m_i)
\right].
\]

这里第二个顶角的指标按闭合费米子味道迹反向排列；这点很重要，不能把 \(s_{ji}\) 和 \(s_{ij}\) 任意互换。

### 165.2 手征迹的直接结果

使用

\[
P_{R,L}=\frac{1\pm\gamma_5}{2},\quad
P_R\gamma^\mu=\gamma^\mu P_L,\quad
\operatorname{tr}(P_{R,L}\gamma^\mu\gamma^\nu)=2g^{\mu\nu},
\]

并注意含奇数个伽马矩阵的项迹为零，得到

\[
\boxed{
\begin{aligned}
N_{ij}(k,q)={}&2k\!\cdot\!(k+q)
\left(h_{ij}s_{ij}^{*}+h_{ji}^{*}s_{ji}\right)\\
&+2m_im_j\left(h_{ij}s_{ji}+h_{ji}^{*}s_{ij}^{*}\right).
\end{aligned}}
\]

对论文所用的实参数矩阵，动量项和质量项一般涉及不同的耦合组合：

\[
C^{(p)}_{ij}=h_{ij}s_{ij}+h_{ji}s_{ji},\qquad
C^{(m)}_{ij}=h_{ij}s_{ji}+h_{ji}s_{ij},
\]
\[
N_{ij}(k,q)=2C^{(p)}_{ij}k\!\cdot\!(k+q)+2m_im_jC^{(m)}_{ij}.
\]

一个局部检查是对单一对角通道 \(i=j\)，若两个顶角退化为实标量耦合 \(h_{ii},s_{ii}\)，上式给出 \(N_{ii}=4h_{ii}s_{ii}[k\cdot(k+q)+m_i^2]\)，与标准 Dirac 标量环的迹一致。这个检查核验了 Dirac 迹中的因子 2；它尚未核验闭合费米子环的整体负号、顶角的 \(i\) 因子或积分归一化。

### 165.3 分子约化与当前可确定的内容

分子中的动量结构可用恒等式

\[
k\cdot(k+q)=\frac12\left[k^2+(k+q)^2-q^2\right]
\]

改写。对分母
\[
D_{ij}=(k^2-m_j^2+i0)((k+q)^2-m_i^2+i0),
\]

有

\[
\frac{k\cdot(k+q)}{D_{ij}}=\frac12\left[
\frac{1}{(k+q)^2-m_i^2+i0}
+\frac{1}{k^2-m_j^2+i0}
+\frac{m_i^2+m_j^2-q^2}{D_{ij}}
\right].
\]

因此每个通道的分子积分只涉及两个 tadpole 型积分和一个二点标量积分；一般外动量依赖中的 \(-q^2\) 项来自最后一项。这给出了从 Dirac 迹到 PV 积分的简化路径，但尚不能独自固定最终自能的正负号。

### 165.4 本节边界与下一步

- [x] 从完整手征顶角直接计算单个有序内部质量通道的 Dirac 分子迹，并区分动量项与质量项的耦合组合。
- [x] 明确闭合味道迹中的 \(ij/ji\) 指标排列，并用对角通道检查因子 2。
- [x] 将动量分子约化为 tadpole 与 \(B_0\) 型积分的组合。
- [ ] 将论文的左右手旋转矩阵逐项代入 \(C_{ij}\)，分别核验轻–轻、轻–重、重–轻、重–重通道是否有重复计数。
- [ ] 按明确的费曼规则计算整体 \(i\) 因子、费米子环负号和 PV 归一化，得到与第 163 节同一约定下的 \(\Pi_{hs}^{\rm UV}(q^2)\)。
- [ ] 求 \(d\Pi_{hs}^{\rm UV}/dq^2|_{q^2=0}\)，再与 EFT 泡图及双标量接触图相减；在完成这一步前，不报告最终 Wilson 系数。

**审计提醒：** 这里得到的是分子迹层面的独立进展，不等同于完成 UV–EFT 匹配。后续应优先核验味道求和与整体归一化，避免把历史 PV 组合中的因子 2 或符号差异带入最终结果。


### 165.5 重要的内部一致性检查：动量项的发散必须抵消

重新按矩阵指标核对后，动量项的耦合组合应为 \(C^{(p)}_{ij}=h_{ij}s_{ij}+h_{ji}s_{ji}\)，而不是质量项中的 \(C^{(m)}_{ij}\)。这一区别是关键：对实正交的左右手旋转，Frobenius 内积保持不变，故

\[
\sum_{i,j}C^{(p)}_{ij}=2\sum_{i,j}h_{ij}s_{ij}=2\operatorname{Tr}(Y_h^T Y_s)
=2\operatorname{Tr}(A_h^T A_s)=0,
\]

其中规范基底的两个顶角矩阵分别正比于 \(A_h=egin{pmatrix}0&1\0&0\end{pmatrix}\) 与 \(A_s=egin{pmatrix}0&0\1&0\end{pmatrix}\)，所以其逐元素内积为零。因而 UV 自能中与 \(q^2 B_0\) 成正比的整体极点应当抵消，这与可重整 UV 拉氏量中不存在独立的 \(\partial_\mu h\partial^\mu s\) 维数四反项相符。若在显式代入旋转角后得不到此抵消，优先检查手征投影和矩阵指标，而不是引入新的反项。

这项检查也暴露出本节初稿中曾把动量项的 \(s_{ij}\) 与 \(s_{ji}\) 互换的指标错误；上文已按直接手征迹修正。质量项的组合 \(C^{(m)}_{ij}\) 不受该修正影响。后续应在 PV 组合中分别使用 \(C^{(p)}\) 和 \(C^{(m)}\)，不能用一个统一的 \(C_{ij}\) 乘整个分子。

把论文式 (13) 的矩阵显式代入，记 \(a=m_L/v_h\)、\(b=m_R/v_s\)、\(X=ab\,c_Ls_Lc_Rs_R\)、\(Z=ab(c_L^2c_R^2+s_L^2s_R^2)\)，得到

\[
C^{(p)}=\begin{pmatrix}2X&-2X\\-2X&2X\end{pmatrix},\qquad
C^{(m)}=\begin{pmatrix}2X&-Z\\-Z&2X\end{pmatrix}.
\]

所以 \(\sum_{ij}C^{(p)}_{ij}=0\) 是逐项显式成立的；而质量项的总权重为 \(\sum_{ij}C^{(m)}_{ij}=4X-2Z\)，通常不必为零。后者乘上 \(m_im_j\) 及不同质量通道的 PV 函数，控制的是非导数项，不能拿它去替代动量项的求和。这个矩阵结果比仅用单个对角通道检查更强，但仍只核验了分子耦合结构；下一步还需把各通道的 \(A_0/B_0\) 组合按统一约定组装。

## 166. UV 自能斜率：先完成通道级 PV 化简，再固定整体约定

本节继续第 165 节的分子迹计算。为避免把尚未统一的整体费曼规则符号伪装成已确定结果，先给出与整体乘法因子无关的通道级代数结构；最终 **整体符号和归一化仍须由选定的 1PI 定义固定**。

### 166.1 每个有序质量通道的积分核

沿用第 165 节的分子
\[
N_{ij}=2C^{(p)}_{ij} k\!\cdot\!(k+q)+2m_im_jC^{(m)}_{ij},
\]
以及分母 \(D_{ij}=(k^2-m_j^2+i0)((k+q)^2-m_i^2+i0)\)。在维数正规化下，忽略对斜率无贡献的、与外动量无关的 tadpole 项，通道级的 \(q^2\) 依赖可写成
\[
\mathcal K_{ij}(q^2)=C^{(p)}_{ij}(m_i^2+m_j^2-q^2)B_0(q^2;m_j^2,m_i^2)
+2m_im_jC^{(m)}_{ij}B_0(q^2;m_j^2,m_i^2),
\]
其中整体公因子取决于自能定义与环积分约定。这里不能把 \(C^{(p)}_{ij}\) 和 \(C^{(m)}_{ij}\) 合并：它们乘的是不同质量结构。

因此通道级导数核为
\[
\boxed{
\mathcal K'_{ij}(0)=C^{(p)}_{ij}\left[-B_{0,ij}(0)+(m_i^2+m_j^2)B'_{0,ij}(0)\right]
+2m_im_jC^{(m)}_{ij}B'_{0,ij}(0)}.
\]
这里 \(B'_{0,ij}(0)\equiv \partial B_0(q^2;m_j^2,m_i^2)/\partial q^2|_{q^2=0}\)。

### 166.2 对任意正质量，斜率积分是有限的

采用
\[
B_0(q^2;m_j^2,m_i^2)=\Delta_\epsilon-\int_0^1 dx\,
\ln\!\left(\frac{x m_i^2+(1-x)m_j^2-x(1-x)q^2-i0}{\mu^2}\right),
\]
可得
\[
B'_{0,ij}(0)=\int_0^1 dx\,
\frac{x(1-x)}{x m_i^2+(1-x)m_j^2}.
\]
该积分在 \(m_i^2,m_j^2>0\) 时有限，且量纲为质量的负二次方。等质量极限给出
\[
B'_0(0;m^2,m^2)=\frac{1}{6m^2},
\]
这可作为后续数值实现的单元测试。另一方面，\(B_{0,ij}(0)\) 含有 \(\Delta_\epsilon\)，但其极点与质量无关；因此它在求和后乘以 \(\sum_{ij}C^{(p)}_{ij}=0\) 而抵消。于是通道求和的导数核可等价写成有限形式
\[
\boxed{
\sum_{ij}\mathcal K'_{ij}(0)=\sum_{ij}
\left[C^{(p)}_{ij}(m_i^2+m_j^2)+2m_im_jC^{(m)}_{ij}\right]B'_{0,ij}(0)
-\sum_{ij}C^{(p)}_{ij}B_{0,ij}^{\rm fin}(0)}.
\]
其中 \(B_{0,ij}^{\rm fin}(0)=-\int_0^1dx\ln([xm_i^2+(1-x)m_j^2]/\mu^2)\)。最后一项一般不能仅凭 \(\sum C^{(p)}=0\) 删除，因为不同通道的有限对数不同；只能删除其共同的 UV 极点部分。

### 166.3 重要限定：有限斜率不等于匹配系数已确定

上述结果把 UV 斜率约化为有限的一维参数积分，明确分离了：

1. 可由 \(\sum C^{(p)}_{ij}=0\) 保证抵消的共同 UV 极点；
2. 依赖质量比的有限 \(B_0^{\rm fin}(0)\) 项；
3. 由 \(B'_{0,ij}(0)\) 控制的质量加权项。

但从 \(\mathcal K'\) 转换为实际 \(\Pi'_{hs}(0)\)，仍需统一闭合费米子环负号、两个顶角的 \(-i\) 因子、维数正规化积分的 \(i/(16\pi^2)\) 约定，以及论文定义的自能是 1PI 振幅中的 \(i\Pi\) 还是 \(-i\Pi\)。这些因素一旦固定，才能把此处结果与第 163 节 EFT 斜率按同一约定相减。

### 166.4 本轮核验状态

- [x] 给出每个有序质量通道对 \(q^2\) 导数的 PV 结构。
- [x] 写出 \(B'_{0,ij}(0)\) 的有限参数积分及等质量检验值 \(1/(6m^2)\)。
- [x] 说明共同 UV 极点为何随 \(\sum C^{(p)}_{ij}=0\) 抵消。
- [ ] 独立核对原论文左右手旋转的符号约定与完整费曼规则，固定从 \(\mathcal K'\) 到 \(\Pi'\) 的整体因子。
- [ ] 对轻–轻、轻–重、重–轻、重–重四通道做可复现的数值求和，并检查质量简并极限。
- [ ] 与 EFT 泡图及 \(hs\bar\ell\ell\) 接触图斜率逐项相减，确定匹配系数。

**本节结论：** UV 斜率的有限通道级积分表示已经建立，但最终整体符号、归一化及 Wilson 系数仍未确定。不能把本节的 \(\mathcal K'\) 直接当成物理自能导数或最终匹配结果。

## 167. 固定一圈振幅的整体因子：与 \(i\Pi\) 约定对齐

本节采用以下明确约定：标量–费米子相互作用写作
\[
\mathcal L_{\rm int}=-h\,\bar\Psi\Gamma_h\Psi-s\,\bar\Psi\Gamma_s\Psi,
\qquad \Gamma_a=Y_aP_R+Y_a^\dagger P_L,
\]
故顶角为 \(-i\Gamma_a\)，传播子为 \(i(\slashed k+m)/(k^2-m^2+i0)\)，闭合 Dirac 费米子环另有因子 \(-1\)。并定义 1PI 二点振幅为 \(i\Pi_{hs}(q^2)\)。在此约定下，两个顶角、两条传播子与费米子环的乘积给出整体负号；使用
\[
\int\frac{d^dk}{(2\pi)^d}\frac{1}{k^2-m^2+i0}
=\frac{i}{16\pi^2}A_0(m^2),\qquad
\int\frac{d^dk}{(2\pi)^d}\frac{1}{D_{ij}}
=\frac{i}{16\pi^2}B_0(q^2;m_j^2,m_i^2),
\]
便得到
\[
\boxed{
\Pi_{hs}^{\rm UV}(q^2)=-\frac{1}{16\pi^2}\sum_{i,j}
\left\{C^{(p)}_{ij}\left[A_0(m_i^2)+A_0(m_j^2)
+(m_i^2+m_j^2-q^2)B_{0,ij}(q^2)\right]
+2m_im_jC^{(m)}_{ij}B_{0,ij}(q^2)\right\}.}
\]
这里 \(A_0\) 与 \(B_0\) 的定义沿用第 163 节。上式的 tadpole 项具体如何按动量平移后的积分变量标记并不影响 \(q^2\) 导数；对斜率而言它们严格为零。

求导后，UV 侧斜率为
\[
\boxed{
\Pi_{hs}^{{\rm UV}\prime}(0)=-\frac{1}{16\pi^2}\sum_{i,j}
\left\{C^{(p)}_{ij}\left[-B_{0,ij}(0)
+(m_i^2+m_j^2)B'_{0,ij}(0)\right]
+2m_im_jC^{(m)}_{ij}B'_{0,ij}(0)\right\}.}
\]
由于 \(\sum_{ij}C^{(p)}_{ij}=0\)，\(B_0\) 的共同 \(\Delta_\epsilon\) 极点在通道求和后抵消，斜率有限。注意这不表示有限的 \(B_{0,ij}^{\rm fin}(0)\) 项也自动消失。

### 167.1 与 EFT 结果相减时的注意事项

第 163 节记录的 EFT 结果采用同一形式的 \(i\Pi\) 约定时，EFT 侧斜率包含维数六局部导数反项所需的极点。UV 侧的维数四 \(hs\) 动能混合极点抵消，而低能 EFT 中出现的局部 \(q^2\) 极点由 EFT 算符基底中的反项吸收；二者并不矛盾，因为 EFT 已将重自由度积分掉，且维数五 Yukawa 算符的低能环图会要求高维局部算符反项。

因此匹配应写为同一重整化方案下的有限差：
\[
\Delta\Pi'_{hs}(0)=\Pi_{hs}^{{\rm UV}\prime}(0)
-\Pi_{hs}^{{\rm EFT}\prime}(0),
\]
并把它映射到事先声明的维数六算符基底。**在明确算符归一化、场重定义/EOM 约简规则和质量基底旋转后，才能将这个差识别为特定 Wilson 系数。** 单独一个自能斜率差通常首先对应低能二点函数中的导数结构，不应未经算符匹配就直接命名为 \(C_{HS}^{(D)}\)。

### 167.2 本轮结论

已在明确的 \(i\Pi\) 约定下固定 UV 自能的整体 \(-1/(16\pi^2)\) 因子，并给出 UV 侧斜率的通道求和表达式。仍待完成的关键工作是把原论文具体质量与混合角代入，数值/解析计算四个通道，独立复核第 163 节 EFT 斜率的接触图符号，再将有限差映射到指定算符基底。尚未宣称最终 Wilson 系数已求出。

## 168. 二点积分斜率的闭式表达式与简并极限

为方便后续将 UV 四个质量通道直接代入计算，令 \(a=m_i^2\)、\(b=m_j^2\)。第 166 节的一维积分可解析积分为
\[
\boxed{
B'_0(0;a,b)=\frac{\frac12(a^2-b^2)-ab\ln(a/b)}{(a-b)^3},\qquad a\ne b.
}
\]
这里 \(a,b\) 表示质量平方，不是质量本身。表达式在交换 \(a\leftrightarrow b\) 后不变，符合 \(B_0(q^2;a,b)=B_0(q^2;b,a)\) 的对称性。直接代数形式在 \(a\approx b\) 时会发生相消，数值代码应在近简并区域改用积分形式或级数展开。

当 \(a=b=m^2\) 时，取连续极限得到
\[
\lim_{b\to a}B'_0(0;a,b)=\frac{1}{6a}=\frac{1}{6m^2},
\]
与第 166 节的 Feynman 参数积分一致。若两质量正且差异不大，可令 \(b=a(1-\varepsilon)\)，则
\[
B'_0(0;a,b)=\frac1a\left(\frac16+\frac{\varepsilon}{12}+\frac{\varepsilon^2}{20}+O(\varepsilon^3)\right),
\]
可用作数值稳定性检查。

这一闭式表达式完成的是标量积分层面的解析化简；还没有把四个通道与具体 \(C^{(p,m)}_{ij}\) 的质量加权和化成最终 Wilson 系数。尤其 \(B_{0,ij}^{\rm fin}(0)\) 的质量比对数项仍需保留，不能只计算 \(B'_0\) 项。

## 169. 将 UV 斜率的四个质量通道显式求和

本节只在第 165–168 节所定义的耦合矩阵和 \(i\Pi_{hs}\) 约定下做代数求和。它的作用是把四个有序通道压缩为一个可直接数值评估的有限表达式；不把这个结果提前认定为最终 Wilson 系数。

### 169.1 四通道求和

记
\[
a=m_1^2,\qquad b=m_2^2,\qquad
B_{11}=B_0^{\rm fin}(0;a,a),\quad
B_{22}=B_0^{\rm fin}(0;b,b),\quad
B_{12}=B_0^{\rm fin}(0;a,b),
\]
并把 \(B'_{ij}\) 简写为 \(D_{ij}=B'_0(0;m_i^2,m_j^2)\)。采用第 165.5 节的矩阵
\[
C^{(p)}=\begin{pmatrix}2X&-2X\\-2X&2X\end{pmatrix},\qquad
C^{(m)}=\begin{pmatrix}2X&-Z\\-Z&2X\end{pmatrix},
\]
代入第 167 节的斜率公式。共同的 \(B_0\) 极点已由 \(\sum C^{(p)}_{ij}=0\) 抵消，留下
\[
\begin{aligned}
\mathcal S'_{\rm UV}
={}&-2X(B_{11}+B_{22}-2B_{12})\\
&+8X\left[m_1^2D_{11}+m_2^2D_{22}\right]\\
&-4\left[X(m_1^2+m_2^2)+Zm_1m_2\right]D_{12}.
\end{aligned}
\]
这里 \(\Pi_{hs}^{{\rm UV}\prime}(0)=-\mathcal S'_{\rm UV}/(16\pi^2)\)。这个整体符号只对应第 167 节已声明的 \(i\Pi\) 约定；若改变二点函数定义，必须同时改变 EFT 侧约定。

由等质量积分 \(D_{11}=1/(6m_1^2)\)、\(D_{22}=1/(6m_2^2)\)，可化为
\[
\boxed{
\mathcal S'_{\rm UV}
=-2X(B_{11}+B_{22}-2B_{12})
+\frac{8X}{3}
-4\left[X(m_1^2+m_2^2)+Zm_1m_2\right]B'_0(0;m_1^2,m_2^2).
}
\]
若使用质量矩阵对角化关系
\[
X(m_1^2+m_2^2)=Zm_1m_2,
\]
则进一步简化为
\[
\boxed{
\mathcal S'_{\rm UV}
=-2X(B_{11}+B_{22}-2B_{12})
+\frac{8X}{3}
-8Zm_1m_2B'_0(0;m_1^2,m_2^2).
}
\]
在用于最终匹配之前，应从论文采用的左右手旋转约定独立核验上述质量恒等式；不能仅因它在先前推导中出现就默认成立。

### 169.2 有限 \(B_0\) 组合的显式形式

采用第 163 节的 PV 约定，
\[
B_{11}=-\ln\frac{m_1^2}{\mu^2},\qquad
B_{22}=-\ln\frac{m_2^2}{\mu^2},
\]
而非简并时
\[
B_{12}=1-
\frac{m_1^2\ln(m_1^2/\mu^2)-m_2^2\ln(m_2^2/\mu^2)}
{m_1^2-m_2^2}.
\]
因此组合
\[
B_{11}+B_{22}-2B_{12}
\]
与 \(\mu\) 无关；对 \(\mu\) 的公共对数依赖严格抵消。写成显式质量比形式，
\[
\boxed{
B_{11}+B_{22}-2B_{12}
=-2+\frac{m_1^2+m_2^2}{m_1^2-m_2^2}
\ln\frac{m_1^2}{m_2^2}.
}
\]
当 \(m_1^2\to m_2^2\) 时，该组合趋于零，符合三项 \(B_0^{\rm fin}\) 在简并点相等时的结果。故也可写成
\[
\boxed{
\mathcal S'_{\rm UV}
=2X\left[
2-\frac{m_1^2+m_2^2}{m_1^2-m_2^2}
\ln\frac{m_1^2}{m_2^2}
\right]
+\frac{8X}{3}
-8Zm_1m_2B'_0(0;m_1^2,m_2^2),
}
\]
其中最后一步使用了前述质量恒等式。注意这个显式式子在简并极限中各项之间可能有显著抵消，数值实现应对对数比使用 `log1p` 或级数展开，而不是直接计算接近 1 的对数比。

### 169.3 本节结论和仍需独立验证的项目

四通道求和现已约化到质量本征值、\(X,Z\) 及一个已知的二点积分斜率函数。共同 UV 极点和公共重整化尺度对数均已显式消去，这是可检查的内部一致性结果。

仍未完成的内容：
- 从原论文的对角化约定独立推导并验证 \(X(m_1^2+m_2^2)=Zm_1m_2\)；
- 对简并质量极限作稳定的级数展开，并以独立数值积分核对闭式表达式；
- 独立复核 EFT 侧泡图与 \(hs\\bar\\ell\\ell\) 接触图的相对符号和归一化；
- 将 UV–EFT 有限差映射到明确的维数六算符基底，并考虑 IBP/EOM 与场重定义。

因此，本节完成了 UV 侧四通道的代数合并，但仍**没有**报告最终 \(C_{HS}^{(D)}\)。

## 170. 对第 168–169 节的积分公式作独立数值核验

为避免只用代数重排验证自身，本节分别对 Feynman 参数积分做数值积分，再与闭式表达式比较。检验的是标量积分公式，不是完整 UV 振幅或 UV–EFT 匹配。

### 170.1 二点积分斜率

直接数值积分
\[
D(a,b)=\int_0^1dx\,\frac{x(1-x)}{xa+(1-x)b}
\]
并与
\[
D(a,b)=\frac{\tfrac12(a^2-b^2)-ab\ln(a/b)}{(a-b)^3}
\]
比较，得到以下代表性测试：

| \((a,b)\) | 参数积分 | 闭式表达式 | 绝对差 |
|---|---:|---:|---:|
| \((4,1)\) | 0.07240083538964584 | 0.07240083538964584 | 小于 \(10^{-15}\) |
| \((1.01,1)\) | 0.1658383002363233 | 0.16583830023120205 | \(5.2\times10^{-12}\) |
| \((25,1)\) | 0.016748271439402124 | 0.016748271439402124 | 小于 \(10^{-15}\) |
| \((1,9)\) | 0.039501911726511754 | 0.03950191172651177 | \(1.4\times10^{-17}\) |

这里 \(a,b\) 是质量平方，并以同一任意质量单位计量。接近简并的 \((1.01,1)\) 已显现闭式公式的相消误差；正式数值代码应在近简并区使用参数积分、专门的级数或高精度算术。

### 170.2 有限 \(B_0\) 组合

独立计算
\[
Q(a,b)=B_0^{\rm fin}(0;a,a)+B_0^{\rm fin}(0;b,b)-2B_0^{\rm fin}(0;a,b)
\]
并与
\[
Q(a,b)=-2+\frac{a+b}{a-b}\ln\frac{a}{b}
\]
比较，测试点 \((a,b)=(4,1),(1.01,1),(25,1),(1,9)\) 的数值分别为
\[
0.310490601866484\,,\quad
1.6501486784\times10^{-5}\,,\quad
1.48711547694055\,,\quad
0.746530721670275,
\]
两种计算在双精度下相符；近简并点的相对精度仍受相消影响。令 \(a=b(1+\delta)\)，可用展开
\[
Q(a,b)=\frac{\delta^2}{6}-\frac{\delta^3}{6}+\frac{3\delta^4}{20}+O(\delta^5)
\]
稳定地处理 \(|\delta|\ll1\)。

### 170.3 本节能证明什么、不能证明什么

- [x] 独立数值积分核验 \(B'_0(0;a,b)\) 的闭式公式。
- [x] 独立数值核验有限组合 \(B_{11}+B_{22}-2B_{12}\) 的质量比表达式。
- [x] 确认公共重整化尺度 \(\mu\) 在该有限组合中消失。
- [ ] 尚未将论文给出的完整参数点与质量本征态混合角代入 UV 四通道求和。
- [ ] 尚未独立重新推导 EFT 泡图与双标量接触图的整体符号。
- [ ] 尚未完成维数六算符基底映射及最终 Wilson 系数。

所以本节是对两个 PV 标量函数的独立数值测试，不能解读为完整匹配的数值验证。

## 171. 从原始质量矩阵独立推导质量恒等式，并限定其用途

第 169 节使用了
\[
 m_1c_Lc_R=m_2s_Ls_R.
\]
本节不把它当作额外假设，而是从原始质量矩阵及论文所用旋转约定重新推导。

### 171.1 由矩阵重构直接得到恒等式

对单个味道扇区，原始质量矩阵写为
\[
\mathcal M=\begin{pmatrix}0&a\\ b&M_E\end{pmatrix},
\]
并采用与论文式 (13) 一致的实正交旋转约定
\[
U_L=\begin{pmatrix}c_L&s_L\\-s_L&c_L\end{pmatrix},\qquad
U_R=\begin{pmatrix}c_R&-s_R\\s_R&c_R\end{pmatrix},
\]
使得
\[
U_L^T\mathcal M U_R=\operatorname{diag}(m_1,m_2).
\]
反向重构即
\[
\mathcal M=U_L\operatorname{diag}(m_1,m_2)U_R^T.
\]
取左上角元素：
\[
\mathcal M_{11}=m_1c_Lc_R-m_2s_Ls_R.
\]
而原始矩阵给出 \(\mathcal M_{11}=0\)，因此
\[
\boxed{m_1c_Lc_R=m_2s_Ls_R}.
\]
这不是近似关系；在该实旋转约定、对角质量取正且矩阵左上元素严格为零时，它是精确恒等式。若采用不同的旋转符号、复相位或不同的质量本征态排序，公式中的符号/相位应随约定调整，不能机械照搬。

### 171.2 对 Yukawa 矩阵的交叉检查

径向 Higgs 顶角由质量矩阵对 \(v_h\) 的导数给出，规范基底导数只含非零的 \((1,2)\) 元素。变换到质量基底后得到
\[
Y_h=\frac{a}{v_h}
\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},
\]
与论文式 (13) 的矩阵结构一致。由此也确认，上述重构使用的左右旋转方向与本工作此前采用的 Higgs 顶角约定相容。对 \(S\) 的导数则应根据 \(b\propto S\) 或 \(S^*\) 的味道约定分别处理；不能仅凭 Higgs 顶角的核对就宣称所有 \(Y_s\) 的相位已独立验证。

### 171.3 这项恒等式能支持什么

恒等式可以用于化简第 169 节的质量加权通道求和，并检验混合角参数化是否与原始质量矩阵一致。它本身不能验证：

- 1PI 自能整体符号与因子归一化；
- UV 端所有有限项的表达式；
- EFT 接触图与泡图的相对符号；
- 将自能斜率映射到某个指定维数六算符的基底变换。

因此，至此可以把质量恒等式从“待核验”改为“在上述旋转约定下已解析推导”；但完整匹配和最终 Wilson 系数仍未完成。

### 171.4 下一项应做的独立计算

后续不再重复推导此恒等式，而应把注意力转向 EFT 的独立费曼规则核验：从
\[
\mathcal L_5=-C_5S\bar L H\ell_R+\mathrm{h.c.}
\]
展开出 \(h\bar\ell\ell\)、\(s\bar\ell\ell\) 以及 \(hs\bar\ell\ell\) 三种顶角，逐一写出 1PI 图的 \(i\) 因子与闭合费米子环负号，再将泡图和接触图分别约化到同一 PV 约定。只有这一步完成后，才能可靠地与 UV 斜率相减。


## 172. 从 EFT 拉氏量逐图重建轻子环的符号与归一化

本节独立从维数五算符的背景场展开重算 EFT 两点函数，重点检查此前公式中的泡图、双标量接触图、闭合费米子环负号及整体归一化。约定 
\[
\mathcal L_5=-C_5S\bar L H\ell_R+\mathrm{h.c.},\qquad
H^0=\frac{v_h+h}{\sqrt2},\quad S=\frac{v_s+s}{\sqrt2},
\]
并取单味道实质量参数。定义
\[
m=\frac{C_5v_hv_s}{2},\qquad y_h=\frac{m}{v_h},\quad y_s=\frac{m}{v_s},\quad y_{hs}=\frac{m}{v_hv_s}=\frac{y_hy_s}{m}.
\]
于是
\[
\mathcal L_5\supset -m\bar\ell\ell-y_hh\bar\ell\ell-y_ss\bar\ell\ell-y_{hs}hs\bar\ell\ell.
\]
相应费曼规则为 \(-iy_h\)、\(-iy_s\) 和 \(-iy_{hs}\)。本节把 1PI 二点振幅定义为 \(i\Pi_{hs}(q^2)\)，并使用
\[
\int\frac{d^dk}{(2\pi)^d}\frac{1}{(k^2-m^2)[(k+q)^2-m^2]}
=\frac{i}{16\pi^2}B_0(q^2;m^2,m^2),
\]
以及同一 PV 约定下的 tadpole 积分 \(iA_0(m^2)/(16\pi^2)\)。

### 172.1 泡图：两个单标量 Yukawa 顶角

闭合费米子环提供一个负号。两个顶角和两条传播子的因子给出
\[
(-1)(-iy_h)(-iy_s)i^2=-y_hy_s,
\]
乘以 Dirac 分子迹
\[
\operatorname{tr}[(\slashed k+m)(\slashed k+\slashed q+m)]
=4[k\cdot(k+q)+m^2].
\]
利用恒等式
\[
k\cdot(k+q)=\frac12\{(k^2-m^2)+[(k+q)^2-m^2]+2m^2-q^2\},
\]
泡图的 PV 结果为
\[
\boxed{\Pi_{hs}^{\rm bub}(q^2)
=-\frac{y_hy_s}{16\pi^2}\left[4A_0(m^2)+(8m^2-2q^2)B_0(q^2;m^2,m^2)\right].}
\]
这里的 \(4A_0\) 来自分子中的两个约消传播子项；不能在没有重新核对 PV 积分定义时任意将其改为 \(8A_0\)。

### 172.2 双标量接触图：一个 \(hs\bar\ell\ell\) 顶角

接触顶角是 \(-iy_{hs}\)，只含一条闭合费米子传播子。振幅为
\[
(-1)(-iy_{hs})\int\frac{d^dk}{(2\pi)^d}
\frac{\operatorname{tr}(\slashed k+m)}{k^2-m^2}.
\]
奇函数项 \(\operatorname{tr}\slashed k\) 积分为零，而 \(\operatorname{tr}(m)=4m\)，因此
\[
\boxed{\Pi_{hs}^{\rm ct}
=-\frac{4my_{hs}}{16\pi^2}A_0(m^2)
=-\frac{y_hy_s}{16\pi^2}4A_0(m^2).}
\]
接触图与泡图中的 tadpole 项同号，二者相加得到此前使用的总结果：
\[
\boxed{\Pi_{hs}^{\rm EFT}(q^2)
=-\frac{y_hy_s}{16\pi^2}\left[8A_0(m^2)+(8m^2-2q^2)B_0(q^2;m^2,m^2)\right].}
\]
因此，按本节明确的顶角和积分约定，历史文档第 163 节所列总 EFT 自能的系数与符号得到逐图复核。

### 172.3 极点与斜率的再核验

取
\[
A_0(m^2)\big|_{\rm pole}=m^2\Delta_\epsilon,\qquad
B_0(q^2;m^2,m^2)\big|_{\rm pole}=\Delta_\epsilon,
\]
则
\[
\Pi_{hs}^{\rm EFT}(q^2)\big|_{\rm pole}
=-\frac{y_hy_s}{16\pi^2}(16m^2-2q^2)\Delta_\epsilon.
\]
又因为
\[
B_0(0;m^2,m^2)=\Delta_\epsilon-\ln\frac{m^2}{\mu^2},\qquad
B'_0(0;m^2,m^2)=\frac{1}{6m^2},
\]
所以
\[
\boxed{\Pi_{hs}^{{\rm EFT}\prime}(0)
=-\frac{y_hy_s}{16\pi^2}\left[-2\Delta_\epsilon+2\ln\frac{m^2}{\mu^2}+\frac43\right].}
\]
其中导数是对 \(q^2\) 求导。此结果与第 163 节一致，说明在当前约定下 EFT 的动量斜率极点为 \(+2y_hy_s\Delta_\epsilon/(16\pi^2)\)。

### 172.4 本次复核的边界

- [x] 从背景场展开重建三个 EFT 顶角。
- [x] 分别计算泡图与双标量接触图，明确闭合费米子环负号。
- [x] 重新得到总 EFT 自能、极点与零动量斜率。
- [ ] 尚未证明 UV 侧使用完全相同的 \(i\Pi\) 约定及质量基底顶角归一化；UV 总符号仍须用原始 Feynman 规则逐项统一。
- [ ] 尚未完成 UV–EFT 相减、EOM/IBP 算符映射及最终 Wilson 系数。

因此，本节确认的是 EFT 侧逐图结果，而不是最终匹配系数。下一步应把 UV 侧也改写成同一 \(i\Pi_{hs}\) 约定，先比较两边的 \(q^2\) 极点，再比较有限斜率，并明确指定维数六算符基底与规范化。

## 173. UV–EFT 斜率差的解析化简与重质量展开（中间结果）

本节记录当前推导得到的 UV 斜率组合、PV 积分的显式表达式，以及在重质量极限下与 EFT 结果相减的中间式。重要限定：本节沿用第 169 节的 UV 通道求和公式和第 172 节的 EFT 自能约定；由于 UV 总振幅的整体符号、顶角归一化及低能通道减法尚未完成逐图终审，以下结果是**条件性中间结果**，不能直接视为最终 Wilson 系数。

记
\[
a=m_1^2,\qquad b=m_2^2,
\]
其中通常将 \(m_1\) 视为轻质量、\(m_2\) 视为重质量。沿用此前定义的耦合组合 \(X,Z\)，以及质量恒等式
\[
X(a+b)=Zm_1m_2.
\]
第 169 节的 UV 斜率组合为
\[
\begin{aligned}
\mathcal S'_{\rm UV}
={}&-2X(B_{11}+B_{22}-2B_{12})+\frac{8X}{3}\\
&-4\big[X(a+b)+Zm_1m_2\big]B'_{12}(0),
\end{aligned}
\]
其中 \(B_{ij}=B_0(0;m_i^2,m_j^2)\)，而 \(B'_{12}(0)\) 表示对外动量平方求导。使用上述质量恒等式，得到
\[
\boxed{
\mathcal S'_{\rm UV}
=-2X(B_{11}+B_{22}-2B_{12})+\frac{8X}{3}
-8X(a+b)B'_{12}(0).
}
\]

### 173.1 PV 组合的显式形式

按本文使用的 PV 约定，
\[
B_0(0;a,b)=\Delta_\epsilon+1-
\frac{a\ln(a/\mu^2)-b\ln(b/\mu^2)}{a-b},
\]
而等质量极限为 \(B_0(0;a,a)=\Delta_\epsilon-\ln(a/\mu^2)\)。由此
\[
\boxed{
B_{11}+B_{22}-2B_{12}
=\frac{a+b}{a-b}\ln\frac ab-2.
}
\]
公共极点与重整化尺度在该组合中抵消。

参数积分给出
\[
B'_0(0;a,b)=\int_0^1dx\,
\frac{x(1-x)}{xa+(1-x)b}
=\frac{\frac12(a^2-b^2)-ab\ln(a/b)}{(a-b)^3},
\quad a\ne b.
\]
等质量极限为
\[
B'_0(0;m^2,m^2)=\frac{1}{6m^2}.
\]
因此，沿用第 169 节表达式，UV 斜率可写成
\[
\boxed{
\begin{aligned}
\mathcal S'_{\rm UV}
={}&-2X\left[\frac{a+b}{a-b}\ln\frac ab-2\right]+\frac{8X}{3}\\
&-8X(a+b)\frac{\frac12(a^2-b^2)-ab\ln(a/b)}{(a-b)^3}.
\end{aligned}
}
\]
在数值上接近 \(a=b\) 时，不宜直接计算含 \((a-b)^{-3}\) 的闭式式子，应使用参数积分或关于质量差的级数展开，以避免灾难性相消。

### 173.2 重质量极限

令 \(r=a/b=m_1^2/m_2^2\ll1\)。则
\[
\frac{a+b}{a-b}\ln\frac ab-2
=-\ln r-2+O(r\ln r),
\]
以及
\[
(a+b)B'_0(0;a,b)=\frac12+O(r\ln r).
\]
因此
\[
\boxed{
\mathcal S'_{\rm UV}
=2X\ln\frac{m_1^2}{m_2^2}+\frac{8X}{3}
+O\!\left(X\frac{m_1^2}{m_2^2}
\ln\frac{m_1^2}{m_2^2}\right).
}
\]
该展开仍继承本节开头对 UV 公式的限定条件。

### 173.3 与 EFT 斜率相减

令 \(g=y_hy_s\)。沿用第 172 节的 EFT 结果
\[
\Pi_{hs}^{{\rm EFT}\prime}(0)
=-\frac{g}{16\pi^2}\left[-2\Delta_\epsilon
+2\ln\frac{m_1^2}{\mu^2}+\frac43\right]
\]
及此前暂定的 UV 记号
\[
\Pi_{hs}^{{\rm UV}\prime}(0)=-\frac{\mathcal S'_{\rm UV}}{16\pi^2},
\]
定义差值 \(\Delta\Pi'(0)=\Pi_{hs}^{{\rm UV}\prime}(0)-\Pi_{hs}^{{\rm EFT}\prime}(0)\)。对 EFT 的显式极点作最小减除后，形式上得到
\[
\boxed{
\Delta\Pi'_{\rm sub}(0)=\frac{1}{16\pi^2}
\left[-\mathcal S'_{\rm UV}
+2g\ln\frac{m_1^2}{\mu^2}+\frac{4g}{3}\right].
}
\]
代入重质量展开：
\[
\boxed{
\begin{aligned}
\Delta\Pi'_{\rm sub}(0)
=\frac{1}{16\pi^2}\Bigg[
&2(g-X)\ln\frac{m_1^2}{\mu^2}
+2X\ln\frac{m_2^2}{\mu^2}\\
&+\frac{4g-8X}{3}\Bigg]
+O\!\left(\frac{Xr\ln r}{16\pi^2}\right).
\end{aligned}
}
\]
若在相应的领先阶近似中可取 \(g=X\)，则轻质量对数抵消，剩下
\[
\boxed{
\Delta\Pi'_{\rm sub}(0)
=\frac{X}{16\pi^2}
\left[2\ln\frac{m_2^2}{\mu^2}-\frac43\right]
+O\!\left(\frac{Xr\ln r}{16\pi^2}\right).
}
\]
这只是领先阶、给定减除约定下的阈值型中间表达式。若目标是完整维数六匹配，必须检查 \(g-X\) 的高阶差异是否进入同一阶；不能未经论证便令其为零。

### 173.4 为什么该差值尚非最终 Wilson 系数

1. UV 与 EFT 必须采用同一外动量、质量定义、场归一化及重整化方案，并确认轻–轻软区贡献在两边逐通道相消。
2. 背景场的 \(h\)-\(s\) 二点函数中的 \(q^2\) 项一般不能唯一识别单个规范不变维数六算符；需先指定完整算符基底。
3. 第 155 节已指出候选导数算符之间存在 IBP/EOM 关系。必须先约定约简规则和场重定义，再将二点函数投影到目标算符。
4. 必须从原始 UV 费曼规则重新确认总符号、混合角约定和通道计数，避免让同一组中间公式互相验证而掩盖共同错误。

例如，若
\[
O_{D,SH}=[D_\mu(SH)]^\dagger D^\mu(SH)
\]
在实背景下以系数 \(C_{D,SH}/\Lambda^2\) 出现在拉氏量中，则其展开包含交叉导数结构
\[
O_{D,SH}\supset \frac{v_hv_s}{2}
\partial_\mu h\,\partial^\mu s.
\]
但其他导数算符经 IBP/EOM 化简后也可能贡献相同的二点投影，所以单独的斜率差不足以唯一确定 \(C_{D,SH}\)。

**本节结论：** 已把沿用的 UV 斜率组合写成 PV 闭式形式，并得到重质量极限下的 UV–EFT 斜率差。该结果是后续匹配的中间检查点；最终 \(C_{HS}^{(D)}\) 仍未确定，需完成 UV 原始振幅复核、软区相减和算符基底投影。

## 174. 检查 \(g-X\) 的 EFT 阶数：轻质量对数在维数六匹配中是否保留

第 173 节的斜率差包含
\[
\Delta\Pi'_{\rm sub}(0)=\frac{1}{16\pi^2}\left[2(g-X)\ln\frac{m_1^2}{\mu^2}+2X\ln\frac{m_2^2}{\mu^2}+\frac{4g-8X}{3}\right]+O(Xr\ln r),
\]
其中 \(g=m_1^2/(v_hv_s)\)，\(X=(m_Lm_R/v_hv_s)c_Ls_Lc_Rs_R\)，且 \(r=m_1^2/m_2^2\)。本节检查 \(g-X\) 是否是维数六阶效应。

### 174.1 由行列式关系得到精确耦合关系

对于实质量矩阵
\[
\mathcal M=\begin{pmatrix}0&m_L\\m_R&M_E\end{pmatrix},
\]
其行列式满足 \(|\det\mathcal M|=|m_Lm_R|=m_1m_2\)。沿用第 171 节的旋转约定，质量恒等式为
\[
m_1c_Lc_R=m_2s_Ls_R.
\]
在与该旋转约定相容、使 \(m_Lm_R=m_1m_2\) 的符号约定下，
\[
\begin{aligned}
\frac{X}{g}
&=\frac{m_Lm_R}{m_1^2}c_Ls_Lc_Rs_R\\
&=\frac{m_2}{m_1}c_Lc_Rs_Ls_R\\
&=c_L^2c_R^2.
\end{aligned}
\]
所以得到精确关系
\[
\boxed{X=g\,c_L^2c_R^2},\qquad
\boxed{g-X=g(1-c_L^2c_R^2)}.
\]
若质量参数或本征态采用不同符号约定，应先统一相位/符号，再使用此式；不应将带符号的中间量与正本征质量混用。

### 174.2 重质量展开与算符维数

在 \(M_E\) 远大于 \(|m_L|,|m_R|\) 的解耦极限，混合角满足量级关系
\[
s_L=O(m_L/M_E),\qquad s_R=O(m_R/M_E),
\]
具体左右标签依论文旋转定义而定，但两者平方之和均为 \(O(M_E^{-2})\)。因此
\[
1-c_L^2c_R^2=s_L^2+s_R^2-s_L^2s_R^2
=O(M_E^{-2}),
\]
从而
\[
g-X=O(g/M_E^2).
\]
若固定 UV Yukawa 参数并作标准重质量展开，轻质量满足 \(m_1=O(M_E^{-1})\)，于是 \(g=O(M_E^{-2})\)，最终
\[
\boxed{g-X=O(M_E^{-4})}.
\]
因此，按 \(1/M_E\) 展开做维数六匹配时，\(g-X\) 是比领先维数六项高两个逆重质量幂的修正；对应的 \((g-X)\ln m_1^2\) 不应被单独保留为维数六系数的一部分。这个阶数判断依赖标准解耦展开；若参数随 \(M_E\) 非标准缩放，需重新计数。

### 174.3 维数六阶的斜率差

在标准重质量展开的维数六阶，可在第 173 节的中间式中令 \(g=X\)，得到
\[
\boxed{
\Delta\Pi'_{\rm sub}(0)=\frac{X}{16\pi^2}\left[2\ln\frac{m_2^2}{\mu^2}-\frac43\right]+O(M_E^{-4}\ln M_E)
}.
\]
这里 \(m_2=M_E+O(M_E^{-1})\)，故在该阶也可将对数中的 \(m_2\) 换成 \(M_E\)，差异属于更高阶修正。于是维数六阶的阈值型二点函数结果为
\[
\boxed{
\Delta\Pi'_{\rm sub}(0)=\frac{X}{16\pi^2}\left[2\ln\frac{M_E^2}{\mu^2}-\frac43\right]+O(M_E^{-4}\ln M_E)
}.
\]

### 174.4 解释边界

此结果支持维数六阶中轻质量对数的抵消，并给出按当前二点函数约定定义的有限阈值斜率。但它仍不是单独的 \(C_{HS}^{(D)}\)：还必须固定完整规范不变算符基底、EOM/IBP 约简与场重定义，并从原始 UV 费曼规则独立确认第 169 节的整体符号与通道计数。只有在这些约定固定后，才能把二点函数斜率转换为拉氏量中目标算符的 Wilson 系数。

## 175. 将二点函数斜率投影到导数算符：可确定的组合与基底依赖

本节继续做算符层面的计算。目的不是提前指定一个唯一 Wilson 系数，而是明确在实径向背景下，哪些规范不变维数六导数算符会贡献到 \(h\)-\(s\) 二点函数的 \(q^2\) 项。

采用
\[
H^0=\frac{v_h+h}{\sqrt2},\qquad S=\frac{v_s+s}{\sqrt2},
\]
并定义
\[
O_1=(H^\dagger H)(\partial_\mu S^\dagger\partial^\mu S),\quad
O_2=(S^\dagger S)(D_\mu H)^\dagger D^\mu H,
\]
\[
O_3=\partial_\mu(S^\dagger S)\,\partial^\mu(H^\dagger H),\quad
O_4=J_S^\mu J_{H\mu},
\]
以及
\[
O_{D,SH}=[D_\mu(SH)]^\dagger D^\mu(SH).
\]
以下只保留二次涨落且只取径向实背景；规范场和 Goldstone 涨落不写入本次二点投影。

### 175.1 逐个展开交叉导数项

有
\[
H^\dagger H=\frac{v_h^2}{2}+v_hh+O(h^2),\qquad
S^\dagger S=\frac{v_s^2}{2}+v_ss+O(s^2).
\]
因此
\[
O_1\supset \frac{v_h^2}{4}(\partial s)^2,
\qquad
O_2\supset \frac{v_s^2}{4}(\partial h)^2,
\]
二者在该背景下没有 \(\partial h\partial s\) 交叉项。对 \(O_3\)，
\[
\partial_\mu(S^\dagger S)=v_s\partial_\mu s+O(\text{二次涨落}),
\]
\[
\partial_\mu(H^\dagger H)=v_h\partial_\mu h+O(\text{二次涨落}),
\]
从而
\[
\boxed{O_3\supset v_hv_s\,\partial_\mu h\partial^\mu s.}
\]
对径向实场，标量流 \(J_S^\mu\) 与 \(J_H^\mu\) 的纯径向部分为零，故 \(O_4\) 在此投影中不贡献交叉动能项。

另一方面，令 \(SH=(v_s+s)(v_h+h)/2\)（忽略双重态指标的规范协变细节，仅对中性径向分量取背景），则
\[
\boxed{O_{D,SH}\supset \frac{v_hv_s}{2}\,\partial_\mu h\partial^\mu s.}
\]
这也与第 155 节的算符恒等式
\[
O_{D,SH}=O_1+O_2+\frac12O_3+\frac12O_4
\]
相容：交叉项仅由 \(O_3/2\) 产生。

### 175.2 斜率实际测量的是哪个系数组合

若拉氏量在某个未约简的算符表示中写作
\[
\mathcal L_6=\frac1{\Lambda^2}
(C_1O_1+C_2O_2+C_3O_3+C_4O_4+C_DO_{D,SH}),
\]
这里把 \(O_{D,SH}\) 同时列出只是为了显示投影，**该列表是过完备的**，因为 \(O_{D,SH}\) 与前四个算符满足上述恒等式，不能把五个系数当作五个独立参数。

在这个过完备写法中，径向二点函数交叉动能项的系数为
\[
\mathcal L_6\supset \frac{v_hv_s}{\Lambda^2}
\left(C_3+\frac{C_D}{2}\right)
\partial_\mu h\partial^\mu s.
\]
若选择 \(O_1,O_2,O_3,O_4\) 为表示基底并将 \(O_D\) 消去，则同一项由重新定义后的 \(C_3\) 表示；若只保留 \(O_D\) 作为该结构的代表，则交叉项系数是 \(C_Dv_hv_s/(2\Lambda^2)\)。这说明二点函数不能区分被 IBP/EOM 或算符恒等式重新分配的系数。

在把二点 1PI 插入定义为 \(i\Pi_{hs}(q^2)\)，且拉氏量交叉项为 \(+\kappa\partial h\partial s\) 的约定下，该局部项给出动量正比的插入 \(i\kappa q^2\)，即对应 \(\Pi'_{hs}(0)=\kappa\)。因此，如果人为选定“只有 \(O_D\) 代表该投影”的基底约定，形式上有
\[
\boxed{\frac{C_D}{\Lambda^2}=\frac{2}{v_hv_s}\,\Delta\Pi'_{\rm local}(0).}
\]
这里 \(\Delta\Pi'_{\rm local}\) 必须是已经完成 UV/EFT 软区相减、统一重整化方案、并按同一 1PI 符号约定定义的局部匹配差。把第 174 节的中间斜率差直接代入上式，只有在已证明其他独立算符对此投影没有贡献、且过完备算符已被明确约简时才成立；当前尚未证明这些条件，所以本式是投影规则而非最终系数。

### 175.3 目前可得的严格结论

1. \(O_1\) 与 \(O_2\) 在常数实背景的二次径向展开中只修正各自的对角动能，不直接产生 \(h\)-\(s\) 交叉动能。
2. \(O_3\) 的交叉项系数是 \(v_hv_s\)，而 \(O_{D,SH}\) 的交叉项系数是 \(v_hv_s/2\)。
3. \(O_4\) 的纯径向背景投影为零；若考虑相位、Goldstone 或规范场涨落，则需重新展开。
4. 单一二点函数斜率只确定所选算符基底中的一个线性组合，不能单独确定与之相关的所有 Wilson 系数。
5. 要给出目标系数，必须先选定独立算符基底，并说明是否以 EOM/IBP 约简后的 \(O_3\) 代表该交叉导数结构，还是以 \(O_{D,SH}\) 代表；二者不能同时作为独立系数。

**本节结论：** 已完成二点函数斜率到候选导数算符的背景投影。下一步应选定独立基底并将第 174 节的阈值差写入该基底，同时用独立的四点/背景场匹配检查是否存在其他算符对同一观测量的贡献。

## 176. 重要记号审计：UV 轻态耦合乘积与维数五 EFT 耦合乘积不能混称为同一个 \(g\)

本节对第 173–174 节中的耦合记号作必要澄清。此前将 \(g\equiv y_hy_s\) 用于 UV–EFT 斜率差，但 \(y_h,y_s\) 在前文有时指维数五 EFT 的低能耦合，有时又可能被理解为 UV 质量基底中的轻态对角 Yukawa。两者在有限重质量下并不严格相同。若不区分，会把高阶解耦修正错误地混入领先阶匹配。

### 176.1 UV 质量基底的轻态对角耦合

原论文式 (14) 给出
\[
y_{h\ell\ell}^{\rm UV}=\frac{m_L}{v_h}c_Ls_R,
\qquad
y_{s\ell\ell}^{\rm UV}=\frac{m_R}{v_s}s_Lc_R.
\]
因此二者的乘积按定义为
\[
\boxed{g_{\rm UV}\equiv y_{h\ell\ell}^{\rm UV}y_{s\ell\ell}^{\rm UV}
=\frac{m_Lm_R}{v_hv_s}c_Ls_Lc_Rs_R=X.}
\]
这是一条由耦合定义直接得到的等式，不需要先把轻态 Yukawa 近似为 \(m_\ell/v_h\) 与 \(m_\ell/v_s\)。原论文在 seesaw 极限下才写出这些近似关系；见原文式 (14)–(15)。

### 176.2 维数五 EFT 中的耦合乘积

若 EFT 仅保留
\[
\mathcal L_5=-\frac{C_5}{\Lambda}S\bar L H\ell_R+\mathrm{h.c.},
\]
并用该算符产生的质量参数 \(m_5=C_5v_hv_s/(2\Lambda)\) 定义其单标量 Yukawa，则
\[
y_h^{\rm EFT}=\frac{m_5}{v_h},\qquad
y_s^{\rm EFT}=\frac{m_5}{v_s},\qquad
g_{\rm EFT}=\frac{m_5^2}{v_hv_s}.
\]
在只做树级维数五匹配时，\(m_5\) 与 UV 轻态精确本征质量 \(m_1\) 只在领先的重质量展开阶一致；把 \(m_5\) 直接替换成精确 \(m_1\)，会把部分高阶逆重质量效应吸收到低维参数中。故一般不能把 \(g_{\rm EFT}\) 与 \(g_{\rm UV}\) 当成精确相等。

在此前使用的质量恒等式与实参数约定下，
\[
m_1c_Lc_R=m_2s_Ls_R,\qquad m_1m_2=m_Lm_R,
\]
可推出
\[
X=\frac{m_1^2}{v_hv_s}c_L^2c_R^2.
\]
若为便于比较暂以精确轻态质量定义 \(g_{\rm mass}\equiv m_1^2/(v_hv_s)\)，则
\[
\boxed{g_{\rm UV}=X=g_{\rm mass}c_L^2c_R^2,}
\]
从而
\[
\boxed{g_{\rm mass}-g_{\rm UV}
=g_{\rm mass}(s_L^2+s_R^2-s_L^2s_R^2).}
\]
这里 \(g_{\rm mass}\) 是用精确质量构造的方便记号，不应自动视作纯维数五 EFT 的精确匹配耦合。

### 176.3 对第 173–174 节斜率差的影响

第 173 节中 EFT 斜率的耦合应明确读作 \(g_{\rm EFT}\)（或在其近似计算中读作 \(g_{\rm mass}\)），而第 169 节 UV 斜率的对角轻态通道使用的是 \(g_{\rm UV}=X\)。在标准 seesaw 计数下，
\[
s_L^2,s_R^2=O(M_E^{-2}),\qquad g_{\rm mass}=O(M_E^{-2}),
\]
所以
\[
g_{\rm mass}-X=O(M_E^{-4}).
\]
这支持在**领先维数六阶**令 \(g_{\rm EFT}\simeq X\) 以检查软对数抵消，但不能将其提升为精确恒等式。若研究维数八阶、有限混合角修正，或使用吸收了高阶修正的物理质量输入，则必须保留这一区别并一致地重做匹配。

### 176.4 纠正后的计算约定

后续公式统一采用以下记号：
- \(X\)：UV 质量基底中两个轻态对角标量 Yukawa 的乘积，严格有 \(X=g_{\rm UV}\)。
- \(g_5\)：由纯维数五 EFT 系数定义的耦合乘积。
- \(g_{\rm mass}=m_1^2/(v_hv_s)\)：用精确轻态质量构造的辅助量；只在说明近似阶数时使用。

因此，第 173 节减极点斜率差中的 \(g\) 应解释为 EFT 侧耦合乘积，而非直接认作 \(X\)。第 174 节令 \(g=X\) 的步骤仅是领先重质量展开下的匹配近似。该澄清不改变领先阶中间表达式，但修正了此前可能造成的“精确相等”误读。

**本节结论：** 目前可以严格说的是 \(g_{\rm UV}=X\)，而 \(g_5\simeq X\) 仅在所声明的领先 seesaw/维数五近似下成立。接下来应在同一匹配方案下定义低能 EFT 参数，再核对 UV 与 EFT 的软区贡献；否则有限阈值常数虽然形式上可写出，却还不能被认定为独立基底中的最终 Wilson 系数。

## 177. 跨版本合并审计：将旧副本第 147–148 节与主版本第 169–176 节对齐

本节以 `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2.md` 为唯一主版本，对另一份恢复副本的第 147–148 节作交叉核对。为避免重复堆叠推导，本节只记录可核验的代数关系、近似条件与尚存问题；主版本原有第 1–176 节均保留不动。

### 177.1 三个剩余通道与主版本第 169 节的代数关系

记
\[
a=m_1^2,\qquad b=m_2^2,\qquad B_{ij}=B_0^{\rm fin}(0;m_i^2,m_j^2),\qquad D_{ij}=B'_0(0;m_i^2,m_j^2).
\]
主版本第 169 节给出的完整 UV 通道组合是
\[
\mathcal S'_{\rm UV}=-2X(B_{11}+B_{22}-2B_{12})+\frac{8X}{3}
-4\big[X(a+b)+Zm_1m_2\big]D_{12},
\]
其中使用了 \(D_{11}=1/(6a)\)、\(D_{22}=1/(6b)\)。在质量矩阵恒等式
\[
X(a+b)=Zm_1m_2
\]
成立时，化为
\[
\mathcal S'_{\rm UV}=-2X(B_{11}+B_{22}-2B_{12})+\frac{8X}{3}-8X(a+b)D_{12}.
\]

若从这个完整组合中减去轻轻通道的内部斜率组合
\[
\mathcal S'_{11}=2X[-B_{11}+2aD_{11}]+4Xm_1^2D_{11}
=-2XB_{11}+\frac{4X}{3},
\]
则剩余三个有序通道满足
\[
\boxed{\mathcal S'_{12+21+22}=4XB_{12}-2XB_{22}-8X(a+b)D_{12}+\frac{4X}{3}.}
\]
这与旧副本第 147.4 节括号内的表达式一致。这里的 \(\mathcal S'\) 是定义为 \(\Pi'=-\mathcal S'/(16\pi^2)\) 的内部组合；不要把 \(\mathcal S'\) 与 \(\Pi'\) 的符号混用。

**适用限制：** 上述一致性是建立在主版本第 165–169 节的通道矩阵、整体自能约定以及质量恒等式之上的代数核对。它不独立证明减去 EFT 轻态图后所得硬差值已经重整化。尤其主版本第 176 节已明确区分 \(X=g_{\rm UV}\) 与纯维数五 EFT 的 \(g_5\)；有限重质量下，不能无条件令 \(g_5=X\)。轻轻通道相消只可在声明的领先 seesaw/维数六匹配阶使用。

### 177.2 耦合矩阵的交叉核对

旧副本第 148 节从实 Yukawa 矩阵出发得到
\[
C^{(p)}_{ij}=(Y_h)_{ij}(Y_s)_{ij}+(Y_h)_{ji}(Y_s)_{ji},
\qquad
C^{(m)}_{ij}=(Y_h)_{ij}(Y_s)_{ji}+(Y_h)_{ji}(Y_s)_{ij},
\]
以及
\[
C^{(p)}=\begin{pmatrix}2X&-2X\\-2X&2X\end{pmatrix},\qquad
C^{(m)}=\begin{pmatrix}2X&-Z\\-Z&2X\end{pmatrix}.
\]
这些矩阵与主版本第 165.5、167、169 节采用的实耦合表达式一致。由于主版本已包含从手征顶角出发的推导，本次只将旧副本结果作为交叉核对，不重复复制整段证明。该简式依赖实参数及既定顶角方向；一般复耦合情形必须保留顶角中的复共轭。

### 177.3 极点陈述的边界

完整 UV 通道求和满足
\[
\sum_{i,j}C^{(p)}_{ij}=0,
\]
所以 UV 完整斜率中来自共同 \(B_0\) 极点的项相消。这一点与主版本第 167、169 节一致。但减去 EFT 轻态泡图后的匹配差值可以包含局部极点，需由所选 EFT 维数六算符基底中的反项以及参数/场重整化共同处理。因此，不能将完整 UV 极点相消误读为匹配差每一项都必须逐图有限，也不能把剩余极点单独视为 UV 矩阵错误的证据。

### 177.4 合并结论与当前状态

- **已核对：** 旧副本第 147.4 节的三通道代数式可由主版本第 169 节的完整通道和减去轻轻通道得到，前提是采用同一耦合矩阵、质量恒等式与整体符号约定。
- **已核对：** 旧副本第 148 节的实耦合矩阵与主版本已有表达式一致，无需将重复推导再复制进正文。
- **仍未完成：** 在有限重质量下统一定义并匹配 EFT 参数 \(g_5\)，从同一重整化方案计算局部反项，并投影到独立、非过完备的维数六算符基底。
- **因此不作过度结论：** 当前表达式还不是最终的 \(C_{HS}^{(D)}\) 或其他指定基底 Wilson 系数。第 175 节所述基底约简、EOM/IBP 与场重定义问题仍然有效。

**本节结论：** 已把旧副本第 147–148 节中可用的信息以交叉审计形式并入指定主版本；不复制平行章节，也不改写主版本既有内容。后续工作应直接从本主版本第 172–176 节继续，先固定 EFT 重整化与算符基底，再完成有限匹配。


## 178. EFT 斜率的局部反项：在既定自能约定下提取可确定的极点系数

本节继续第 172–177 节的计算，先处理不依赖有限阈值常数的部分：EFT 轻态环图的 UV 极点，以及它要求的局部导数反项。这里仅沿用文档已经声明的约定，**不**把该反项直接等同于完整 UV 匹配后的有限 Wilson 系数。

### 178.1 从 EFT 斜率读出极点

第 172 节给出的 EFT 斜率为
\[
\Pi_{hs}^{{\rm EFT}\prime}(0)
=-\frac{g_5}{16\pi^2}\left[-2\Delta_\epsilon+2\ln\frac{m_1^2}{\mu^2}+\frac43\right]
=\frac{g_5}{16\pi^2}\left[2\Delta_\epsilon-2\ln\frac{m_1^2}{\mu^2}-\frac43\right].
\]
因此，在此自能符号约定下，轻态环图的极点部分为
\[
\boxed{\left.\Pi_{hs}^{{\rm EFT}\prime}(0)\right|_{\rm pole}
=+\frac{2g_5}{16\pi^2}\Delta_\epsilon.}
\]
这与第 169 节完整 UV 通道和中公共的 \(B_0\) 极点抵消并不矛盾：前者是低能 EFT 的局部 UV 发散，后者是完整 UV 振幅中的通道求和性质。EFT 的发散必须由 EFT 局部算符反项消除。

### 178.2 交叉动能反项的符号

沿用第 175 节的定义：若局部拉氏量含有
\[
\mathcal L_{\rm loc}\supset \kappa\,\partial_\mu h\,\partial^\mu s,
\]
则按本文约定，该项对二点函数斜率的贡献为
\[
\Pi_{hs}^{{\rm CT}\prime}(0)=\kappa_{\rm CT}.
\]
要求 EFT 的重整化二点函数有限，便得到
\[
\left.\Pi_{hs}^{{\rm EFT}\prime}\right|_{\rm pole}
+\Pi_{hs}^{{\rm CT}\prime}\big|_{\rm pole}=0,
\]
即
\[
\boxed{\kappa_{\rm CT}\big|_{\rm pole}
=-\frac{2g_5}{16\pi^2}\Delta_\epsilon.}
\]
这里的负号来自第 172 节所用的 \(i\Pi_{hs}\) 与拉氏量交叉动能项约定。若改用相反的 1PI 自能定义或把动能混合项写成 \(-\kappa\partial h\partial s\)，必须同步改写此式，不能只翻转反项而保留其余公式。

### 178.3 对候选算符系数的条件性映射

若暂时采用“该交叉动能投影仅由 \(O_{D,SH}\) 表示”的基底约定，第 175 节给出的背景展开是
\[
\mathcal L_6\supset \frac{C_{D,SH}}{\Lambda^2}\,O_{D,SH}
\supset \frac{C_{D,SH}}{\Lambda^2}\frac{v_hv_s}{2}
\partial_\mu h\partial^\mu s.
\]
于是仅对这一投影有
\[
\kappa=\frac{C_{D,SH}v_hv_s}{2\Lambda^2},
\]
并对应
\[
\boxed{\left.\frac{C_{D,SH}}{\Lambda^2}\right|_{\rm CT,pole}
=-\frac{4g_5}{16\pi^2v_hv_s}\Delta_\epsilon.}
\]
此映射是**给定基底与归一化后的投影关系**，不是对任意非冗余 SMEFT/扩展 EFT 基底的普适 Wilson 系数。由于第 155、175 节已经证明 \(O_{D,SH}\) 可与其他导数结构通过代数恒等式、IBP 和 EOM 重新分配，只有在完整基底及约简规则固定后，才能把该投影反项解释为某个独立系数的反项。

### 178.4 本节确定了什么、还不能确定什么

- **确定：** 在第 172 节自能和交叉动能符号约定下，EFT 轻态环图斜率的极点为 \(+2g_5\Delta_\epsilon/(16\pi^2)\)，对应的局部交叉动能反项斜率为其相反数。
- **不确定：** 这并未单独确定完整 UV–EFT 匹配的有限阈值，也未给出指定非冗余算符基底中的最终 Wilson 系数。
- **下一步：** 需要把该反项嵌入明确的独立算符基底，列出同一基底中由场/参数重整化诱导的贡献，并用未破缺背景下的独立外腿振幅检验其是否只是一个投影组合。

**本节结论：** 已从 EFT 斜率明确提取局部极点及其反项符号，建立了后续算符混合计算的一个可检验锚点；有限匹配与独立基底中的 Wilson 系数仍待完成。

## 179. 阈值表达式的重整化尺度审计：对数项与有限常数的分离

本节只对第 173 节已经得到的领先重质量差值作代数与尺度审计，不引入新的 UV 振幅假设。采用
\[
\Delta\Pi'_{\rm sub}(0)
=\frac{X}{16\pi^2}\left[2\ln\frac{m_2^2}{\mu^2}-\frac43\right]
+O\!\left(\frac{Xr\ln r}{16\pi^2}\right),
\qquad r=\frac{m_1^2}{m_2^2}\ll1,
\]
其中已在领先阶取 \(g_5\simeq X\)，并沿用第 172–173 节的减除与自能符号约定。

### 179.1 在匹配尺度 \(\mu=m_2\) 处的简化

选择重质量匹配尺度 \(\mu=m_2\)，则大对数消失，得到
\[
\boxed{
\left.\Delta\Pi'_{\rm sub}(0)\right|_{\mu=m_2}
=-\frac{4X}{3(16\pi^2)}
+O\!\left(\frac{Xr\ln r}{16\pi^2}\right).
}
\]
这说明在当前领先阶表达式中，有限常数 \(-4/3\) 是选取 \(\mu=m_2\) 后留下的阈值项。它不是独立于方案的可观测量；有限局部项可随重整化方案和算符基底约定重新分配。

### 179.2 显式尺度导数及其含义

暂时把 \(X,m_2\) 当作固定参数，对显式对数求导：
\[
\frac{\partial}{\partial\ln\mu}
\Delta\Pi'_{\rm sub}(0)
=-\frac{4X}{16\pi^2}
+O\!\left(\frac{Xr\ln r}{16\pi^2}\right).
\]
这里使用
\(\partial_{\ln\mu}\ln(m_2^2/\mu^2)=-2\)。
因此该中间差值单独并不具有尺度不变性。正确的重整化群检验必须同时包括 Wilson 系数的跑动、耦合与质量参数的跑动，以及所选 EFT 基底中局部反项的贡献；不能要求这一个未完成匹配的二点函数差值自身满足 \(\mu\) 独立。

### 179.3 这个尺度检验能排除什么、不能证明什么

- 若后续推导在固定 \(X,m_2\) 的近似下得到显式对数项对 \(\ln\mu\) 的导数不是 \(-4X/(16\pi^2)\)，则应回查第 173 节 UV–EFT 相减时的对数符号或因子。
- 在 \(\mu=m_2\) 时得到 \(-4X/[3(16\pi^2)]\)，只验证当前公式的代数简化；它不能独立验证 UV 总振幅的整体符号，也不能证明该常数就是某个指定非冗余算符的 Wilson 系数。
- 要将其转化为目标算符系数，还需使用固定的算符归一化和场重定义约定，并把二点函数投影与未破缺背景下的独立振幅相互核验。

**本节结论：** 当前领先阶阈值式在 \(\mu=m_2\) 时化为有限常数项 \(-4X/[3(16\pi^2)]\)，其显式尺度导数为 \(-4X/(16\pi^2)\)。这构成后续重整化群和符号检查的简单基准，但不是最终 Wilson 系数。

## 180. UV–EFT 斜率相减的符号与归一化：逐项代数审计

本节不声称替代原始 UV 费曼规则的独立重算，而是把第 172–179 节已经写下的两侧公式放在同一符号约定中逐项相减，检查对数、有限常数和整体负号是否内部一致。这样能定位代数错误，但不能排除 UV 公式与其推导中共同存在的整体符号错误。

### 180.1 先固定两侧的定义

按第 172 节，EFT 斜率写为
\[
\Pi_{hs}^{{\rm EFT}\prime}(0)
=\frac{g_5}{16\pi^2}\left[2\Delta_\epsilon-2\ln\frac{a}{\mu^2}-\frac43\right],
\qquad a=m_1^2.
\]
按第 169、173 节的约定，UV 侧定义为
\[
\Pi_{hs}^{{\rm UV}\prime}(0)=-\frac{\mathcal S'_{\rm UV}}{16\pi^2},
\]
且重质量展开为
\[
\mathcal S'_{\rm UV}=2X\ln\frac{a}{b}+\frac{8X}{3}
+O\!\left(X\frac{a}{b}\ln\frac{a}{b}\right),\qquad b=m_2^2.
\]
因此
\[
\Pi_{hs}^{{\rm UV}\prime}(0)
=\frac{1}{16\pi^2}\left[-2X\ln\frac{a}{b}-\frac{8X}{3}\right]
+O\!\left(\frac{X}{16\pi^2}\frac{a}{b}\ln\frac{a}{b}\right).
\]
这里的负号来自已经声明的定义 \(\Pi'_{\rm UV}=-\mathcal S'_{\rm UV}/(16\pi^2)\)，不是在相减时另行添加的符号。

### 180.2 减除 EFT 极点后再相减

先从 EFT 表达式中减去其 MS 型极点项 \(2g_5\Delta_\epsilon/(16\pi^2)\)，则
\[
\Pi_{hs,\rm sub}^{{\rm EFT}\prime}(0)
=\frac{g_5}{16\pi^2}\left[-2\ln\frac{a}{\mu^2}-\frac43\right].
\]
据定义 \(\Delta\Pi'_{\rm sub}=\Pi_{\rm UV}'-\Pi_{\rm EFT,sub}'\)，代入上式得到
\[
\begin{aligned}
16\pi^2\Delta\Pi'_{\rm sub}(0)
={}&-2X\ln\frac{a}{b}-\frac{8X}{3}
+2g_5\ln\frac{a}{\mu^2}+\frac{4g_5}{3}\\
&+O\!\left(X\frac{a}{b}\ln\frac{a}{b}\right).
\end{aligned}
\]
将对数按 \(\ln(a/b)=\ln(a/\mu^2)-\ln(b/\mu^2)\) 展开，可写成
\[
\boxed{
\Delta\Pi'_{\rm sub}(0)=\frac{1}{16\pi^2}\left[
2(g_5-X)\ln\frac{a}{\mu^2}
+2X\ln\frac{b}{\mu^2}
+\frac{4g_5-8X}{3}\right]
+O\!\left(\frac{X}{16\pi^2}\frac{a}{b}\ln\frac{a}{b}\right).
}
\]
所以第 173 节的对数和有限常数，在当前定义下代数相容。只有在领先维数六展开允许 \(g_5=X+O(M_E^{-4})\) 时，轻质量对数才在该阶消失，并得到第 179 节的阈值式。

### 180.3 三项独立的符号检查

1. **EFT 极点：** \(\Pi_{\rm EFT}'|_{\rm pole}=+2g_5\Delta_\epsilon/(16\pi^2)\)。若把它减除，剩余有限部分的对数项必须是 \(-2g_5\ln(a/\mu^2)\)，而不是正号。
2. **UV 整体符号：** 由既定定义，UV 有限展开进入差值时是 \(-2X\ln(a/b)-8X/3\)。若改变 \(\Pi'_{\rm UV}\) 与 \(\mathcal S'_{\rm UV}\) 的相对符号，就会同时改变重质量对数和常数项；不能只翻转其中一项。
3. **重质量匹配阶：** 在 \(g_5=X\) 的领先阶近似下，\(2X\ln(a/\mu^2)-2X\ln(a/b)=2X\ln(b/\mu^2)\)，有限常数为 \(-8X/3+4X/3=-4X/3\)。这同时复现第 179 节的对数系数与常数。

### 180.4 审计结论及其边界

- **内部代数通过：** 第 172 节 EFT 斜率、第 173 节 UV 重质量展开及 UV–EFT 相减式，在统一采用 \(\Pi'_{\rm UV}=-\mathcal S'_{\rm UV}/(16\pi^2)\) 后，确实给出第 179 节的领先阈值表达式。
- **尚未独立验证：** 这不是对 UV 自能整体符号的第一性原理复核，因为该检查仍使用第 169 节已推导的 \(\mathcal S'_{\rm UV}\)。要独立验证整体符号，必须从原始拉氏量写出每个 UV 费曼规则，明确 \(i\Pi\) 的定义、费米子闭环负号、两个标量顶角的顺序、质量本征态旋转和有序内部态求和，再重算 \(q^2\) 系数。
- **归一化仍需闭合：** 斜率差是二点函数投影。它只有在 EFT 算符基底、交叉动能项定义、场重定义和反项约定全部固定后，才能映射到具体 Wilson 系数；不能直接将 \(-4X/[3(16\pi^2)]\) 宣称为最终 \(C_{HS}^{(D)}\)。

**本节结论：** 当前公式链的相减代数和领先阶归一化彼此一致；原始 UV 费曼规则的独立复核、完整反项体系和非冗余算符基底投影仍是开放任务。


## 181. 重质量展开的下一阶交叉检查：显式保留 \(r\ln r\) 项

本节只检查第 173 节使用的两个标量积分组合在 \(r=m_1^2/m_2^2\to0\) 时的渐近展开，并不重新假设或验证 UV 振幅的整体符号。其目的在于让误差项的阶数有明确来源，而不是只写成笼统的 \(O(r\ln r)\)。

令 \(a=rb\)，其中 \(b=m_2^2\)，并定义
\[
Q(r)=B_{11}+B_{22}-2B_{12},\qquad
F(r)=(a+b)B'_0(0;a,b).
\]
第 173 节已有的闭式表达式等价于
\[
Q(r)=\frac{1+r}{r-1}\ln r-2,
\]
以及
\[
F(r)=(1+r)\frac{\tfrac12(r^2-1)-r\ln r}{(r-1)^3}
=(1+r)\frac{\tfrac12(1-r^2)+r\ln r}{(1-r)^3}.
\]

### 181.1 展开到首个幂次修正

使用
\[
\frac{1+r}{1-r}=1+2r+2r^2+O(r^3),\qquad
\frac{1}{(1-r)^3}=1+3r+6r^2+O(r^3),
\]
得到
\[
\boxed{Q(r)=-\ln r-2-2r\ln r+O(r^2\ln r)}.
\]
对导数积分组合，先展开
\[
\frac{\tfrac12(1-r^2)+r\ln r}{(1-r)^3}
=\frac12+r\left(\frac32+\ln r\right)+O(r^2\ln r),
\]
再乘上 \(1+r\)，因此
\[
\boxed{F(r)=\frac12+r(2+\ln r)+O(r^2\ln r)}.
\]
这明确展示了此前所写 \(F(r)=\frac12+O(r\ln r)\) 中被省略的首项系数。

### 181.2 对 UV 斜率组合的影响

沿用第 173 节条件性表达式
\[
\mathcal S'_{\rm UV}=-2XQ(r)+\frac{8X}{3}-8XF(r),
\]
代入上面的展开可得
\[
\begin{aligned}
\mathcal S'_{\rm UV}
={}&2X\ln r+\frac{8X}{3}
-4Xr\ln r-16Xr
+O(Xr^2\ln r).
\end{aligned}
\]
所以领先项确为
\[
\mathcal S'_{\rm UV}=2X\ln r+\frac{8X}{3}+O(Xr\ln r),
\]
但更细的展开还含有非对数的 \(-16Xr\) 项。由于 \(r\to0\) 时 \(|r\ln r|\) 比 \(r\) 大，统一写作 \(O(r\ln r)\) 在渐近阶数上成立；若要给出数值误差或保留下一阶系数，则必须同时保留 \(r\ln r\) 与 \(r\) 两项。

### 181.3 对后续匹配的限制

1. 以上修正只来自标量积分函数的渐近展开；它没有纳入 \(g_5-X\) 的有限质量修正、耦合参数跑动或其他图的贡献。
2. 因此不能把 \(-4Xr\ln r-16Xr\) 直接解释成完整 Wilson 系数的下一阶修正。
3. 当用数值计算检验第 173 节公式时，应同时比较精确闭式、直接参数积分以及本节展开；近简并区应避免直接使用含 \((a-b)^{-3}\) 的公式，而重质量区则可用本节展开检查符号与阶数。

**本节结论：** 第 173 节的领先重质量展开通过了下一阶代数交叉检查。积分函数自身给出的首个修正为 \(-4Xr\ln r-16Xr\)，但这仍是对既有条件性 UV 公式的数学核验，不构成对原始 UV 费曼规则或最终 Wilson 系数的独立验证。

## 182. UV 一圈整体因子的逐项复核：闭合费米子环、顶角与传播子

本节从第 165 节写出的质量基底相互作用重新列出一圈振幅中的整体因子，目标是把“分子迹的结果”与“自能的整体符号”分开核验。这里采用的约定仍是：1PI 二点振幅定义为 \(i\Pi_{hs}(q^2)\)，相互作用项为
\[
\mathcal L_{\rm int}=-h\,\bar\chi\Gamma_h\chi-s\,\bar\chi\Gamma_s\chi,
\qquad \Gamma_a=Y_aP_R+Y_a^\dagger P_L,
\]
故标量顶角为 \(-i\Gamma_a\)，费米子传播子为 \(i(\slashed k+m)/(k^2-m^2+i0)\)。

### 182.1 整体因子的计数

对一条有序内部味道通道，振幅的非积分因子为
\[
(-1)_{\rm closed\ fermion\ loop}\,(-i)^2_{\rm vertices}\,i^2_{\rm propagators}.
\]
因为 \((-i)^2=-1\) 且 \(i^2=-1\)，两个顶角与两条传播子的乘积为 \(+1\)；再乘闭合费米子环的 \(-1\)，总因子为 \(-1\)。若采用
\[
\int\!\frac{d^dk}{(2\pi)^d}\frac{1}{(k^2-m_j^2+i0)((k+q)^2-m_i^2+i0)}
=\frac{i}{16\pi^2}B_0(q^2;m_j^2,m_i^2),
\]
则振幅应具有 \(-i/(16\pi^2)\) 的整体因子。由于 \(i\Pi_{hs}\) 是完整 1PI 振幅，得到
\[
\Pi_{hs}^{\rm UV}(q^2)=-\frac{1}{16\pi^2}\,\mathcal F(q^2),
\]
其中 \(\mathcal F\) 是把 Dirac 分子迹约化为 \(A_0\) 与 \(B_0\) 后的 PV 组合。这与第 167 节采用的整体约定一致。

### 182.2 分子约化与通道表达式

对实参数，采用第 165 节的迹结果
\[
N_{ij}=2C^{(p)}_{ij}\,k\!\cdot\!(k+q)+2m_im_jC^{(m)}_{ij},
\]
并使用
\[
k\!\cdot\!(k+q)=\frac12\left[k^2+(k+q)^2-q^2\right],
\]
将分母约化为两个单传播子项与一个二点函数项。按第 163、167 节的 \(A_0,B_0\) 归一化，单个有序通道贡献为
\[
\begin{aligned}
\Pi_{ij}(q^2)=-\frac{1}{16\pi^2}\bigg\{&C^{(p)}_{ij}\big[A_0(m_i^2)+A_0(m_j^2)\\
&+(m_i^2+m_j^2-q^2)B_0(q^2;m_j^2,m_i^2)\big]\\
&+2m_im_jC^{(m)}_{ij}B_0(q^2;m_j^2,m_i^2)\bigg\}.
\end{aligned}
\]
对 \(q^2\) 求导并在零动量处取值，得到
\[
\Pi'_{ij}(0)=-\frac{1}{16\pi^2}\left\{
C^{(p)}_{ij}\left[-B_{0,ij}(0)+(m_i^2+m_j^2)B'_{0,ij}(0)\right]
+2m_im_jC^{(m)}_{ij}B'_{0,ij}(0)\right\}.
\]
求导时 \(A_0\) 项为零；显式的 \(-q^2B_0\) 项给出 \(-B_0(0)\)，其符号不能遗漏。

### 182.3 复参数情形与实参数简化的边界

若耦合矩阵不是实矩阵，动量项与质量项的组合必须保留第 165.2 节直接迹出的共轭结构：
\[
C^{(p)}_{ij}=h_{ij}s_{ij}^{*}+h_{ji}^{*}s_{ji},\qquad
C^{(m)}_{ij}=h_{ij}s_{ji}+h_{ji}^{*}s_{ij}^{*}.
\]
不能把实参数下的矩阵
\(C^{(p)}=\begin{pmatrix}2X&-2X\\-2X&2X\end{pmatrix}\)
和
\(C^{(m)}=\begin{pmatrix}2X&-Z\\-Z&2X\end{pmatrix}\)
直接推广到一般复参数而不重新处理相位与厄米共轭。本文后续的四通道闭式求和明确限于相应实参数约定。

### 182.4 审计结论与尚存风险

- **整体因子计数通过：** 在本节声明的 \(i\Pi\) 约定下，闭合费米子环、两个标量顶角与两条传播子的乘积给出负号，因而 \(\Pi=-\mathcal F/(16\pi^2)\)，与第 167 节一致。
- **通道斜率通过：** 对 \(q^2\) 求导时，\(-q^2B_0\) 产生 \(-B_0(0)\)；其共同 UV 极点在完整求和中由 \(\sum_{ij}C^{(p)}_{ij}=0\) 抵消。
- **尚未独立验证全部模型约定：** 以上计数依赖第 165 节的味道指标排列和给定的相互作用拉氏量。若原论文的旋转矩阵、Dirac/Majorana 自由度或场归一化与此处不同，必须先修正这些输入，不能仅靠整体因子计数排除模型约定差异。
- **匹配仍未闭合：** 该节只复核 UV 振幅的符号与 PV 结构，不替代 EFT 局部反项、参数/场重整化或非冗余算符基底投影；因此仍不能据此报告最终 \(C_{HS}^{(D)}\)。

**本节结论：** 在本文当前采用的实参数 Dirac 费米子与 \(i\Pi\) 约定下，UV 一圈整体负号和斜率核与第 167 节一致。后续应把这套规则应用于明确的质量与混合角数值点，并用独立的 Feynman 参数积分检查四通道和式；Wilson 系数的最终识别仍需完整 EFT 基底匹配。

## 183. 独立 Feynman 参数积分检验：标量积分闭式与四通道组合

本节对第 169、170、181 节所用的标量积分组合进行数值独立检查。检查对象是参数积分与闭式表达式之间的一致性；它不重新推导耦合矩阵，也不独立验证第 182 节的 UV 整体符号。为避免把同一个闭式公式代入自身，本节直接数值积分 Feynman 参数表示，再与解析式比较。

令
\[
r=\frac{a}{b}=\frac{m_1^2}{m_2^2}>0,
\qquad a=m_1^2,\quad b=m_2^2.
\]
采用与前文一致的 PV 约定，定义
\[
Q(r)=B_0(0;a,a)+B_0(0;b,b)-2B_0(0;a,b),
\]
\[
F(r)=(a+b)B'_0(0;a,b).
\]
两者中的共同 UV 极点及任意公共重整化尺度项均在组合中抵消。

### 183.1 独立积分表示

对零动量二点函数，Feynman 参数形式给出
\[
B_0(0;a,b)=\Delta_\epsilon-\int_0^1 dx\,
\ln\frac{xa+(1-x)b}{\mu^2}.
\]
因此在令 \(b\) 为质量平方单位、\(a=rb\) 后，
\[
\boxed{
Q(r)=-\ln r+2\int_0^1 dx\,\ln\bigl[xr+(1-x)\bigr]
}
\]
以及
\[
\boxed{
F(r)=(1+r)\int_0^1 dx\,
\frac{x(1-x)}{xr+(1-x)}
}.
\]
直接积分可与第 169、181 节的闭式逐项比较：
\[
Q_{\rm cl}(r)=\frac{1+r}{r-1}\ln r-2,
\]
\[
F_{\rm cl}(r)=(1+r)\frac{\tfrac12(1-r^2)+r\ln r}{(1-r)^3}.
\]
在 \(r=1\) 处，闭式应使用连续极限，而不是直接代入产生的 \(0/0\)：
\[
Q(1)=0,\qquad F(1)=\frac13.
\]

### 183.2 数值积分对照

下表将上述参数积分直接数值求积，并与闭式表达式比较。数值取 \(b=1\)，故 \(r=a/b\) 是唯一输入；表中数值为无量纲组合。

| \(r\) | \(Q_{\rm integral}\) | \(Q_{\rm closed}\) | \(F_{\rm integral}\) | \(F_{\rm closed}\) |
|---:|---:|---:|---:|---:|
| \(10^{-4}\) | 7.212182624276 | 7.212182624276 | 0.499278637472 | 0.499278637472 |
| \(10^{-2}\) | 2.698203927119 | 2.698203927119 | 0.472470116038 | 0.472470116038 |
| \(0.1\) | 0.814270669215 | 0.814270669215 | 0.399472756887 | 0.399472756887 |
| \(0.5\) | 0.079441541680 | 0.079441541680 | 0.341116916640 | 0.341116916640 |
| \(0.99\) | 0.000016834847 | 0.000016834847 | 0.3333350168 | 0.3333350168 |

在这些测试点上，直接求积与闭式数值相符；使用双精度自适应求积时，差异在约 \(10^{-11}\) 或更小的数值误差范围内。接近简并点时，\(Q_{\rm cl}\) 与 \(F_{\rm cl}\) 的显式表达式存在相消，数值实现应切换到连续极限或局部级数，以避免把浮点消去误判为物理偏差。

### 183.3 与重质量展开的交叉检查

对 \(r\ll1\)，直接积分结果应复现第 181 节的渐近形式：
\[
Q(r)=-\ln r-2-2r\ln r+O(r^2\ln r),
\]
\[
F(r)=\frac12+r(2+\ln r)+O(r^2\ln r).
\]
例如 \(r=10^{-4}\) 时，精确参数积分给出 \(Q\simeq7.21218\)、\(F\simeq0.499279\)，与小 \(r\) 的预期趋势一致。这里的“独立”指积分数值实现与闭式代数表达式使用不同计算路径；它仍然使用相同的 PV 定义，不能检验若两处共同采用了错误的自能符号或错误的费米子自由度计数。

### 183.4 审计结论与下一步

- **标量积分通过数值交叉检查：** 参数积分与闭式 \(Q(r)\)、\(F(r)\) 在所测重质量、一般质量比和近简并点相符。
- **未验证 UV 振幅整体约定：** 此检查只验证积分函数，不验证 \(\Pi'_{\rm UV}=-\mathcal S'_{\rm UV}/(16\pi^2)\) 的整体符号、耦合矩阵或各通道的组合系数。
- **下一步应检查完整通道和：** 将具体满足原始质量矩阵约束的 \((m_1,m_2,\theta_L,\theta_R)\) 参数点代入四通道求和，独立计算原始 Dirac 分子迹的参数积分，再与第 169 节完整解析式比较。参数点必须由质量矩阵本身生成，不能任意独立选取互不相容的质量与混合角。

**本节结论：** 第 169、181 节使用的两个标量积分组合已通过独立 Feynman 参数数值积分检查。该结果提高了积分闭式和渐近展开的可信度，但尚未完成 UV 全振幅、EFT 反项及非冗余算符基底的最终匹配；因此最终 \(C_{HS}^{(D)}\) 仍未确定。


## 184. 从原始质量矩阵生成五组参数：四通道斜率与约化闭式的数值核验

本节落实第 183.4 节提出的下一步。与直接指定质量本征值和混合角不同，这里从原始实质量矩阵
\[
\mathcal M=\begin{pmatrix}0&m_L\\m_R&M_E\end{pmatrix}
\]
出发，对每组输入作奇异值分解，得到正的轻、重质量本征值和左右奇异向量；再把
\[
\frac{\partial\mathcal M}{\partial h}=\begin{pmatrix}0&m_L/v_h\\0&0\end{pmatrix},\qquad
\frac{\partial\mathcal M}{\partial s}=\begin{pmatrix}0&0\\m_R/v_s&0\end{pmatrix}
\]
变换到质量基底，构造第 165 节的 \(C^{(p)}_{ij}\) 与 \(C^{(m)}_{ij}\)。因此质量、旋转和顶角并非互相独立地挑选，而是由同一原始矩阵生成。

### 184.1 直接四通道积分与闭式比较

对每个有序通道，直接使用第 166 节的有限斜率核
\[
\mathcal K'_{ij}(0)=C^{(p)}_{ij}\big[-B^{\rm fin}_{0,ij}(0)+(m_i^2+m_j^2)D_{ij}\big]
+2m_im_jC^{(m)}_{ij}D_{ij},
\]
其中不通过闭式公式，而以数值参数积分计算
\[
B^{\rm fin}_{0,ij}(0)=-\int_0^1dx\,\ln\frac{xm_i^2+(1-x)m_j^2}{\mu^2},\qquad
D_{ij}=\int_0^1dx\,\frac{x(1-x)}{xm_i^2+(1-x)m_j^2}.
\]
把四个有序通道 \((11),(12),(21),(22)\) 全部相加，得到 \(\mathcal S'_{\rm direct}\)。再独立地用第 169 节的约化表达式
\[
\mathcal S'_{\rm closed}=-2XQ+\frac{8X}{3}-4\big[X(m_1^2+m_2^2)+Zm_1m_2\big]D_{12},
\]
其中 \(Q=B_{11}^{\rm fin}+B_{22}^{\rm fin}-2B_{12}^{\rm fin}\)、\(X=C^{(p)}_{11}/2\)、\(Z=-C^{(m)}_{12}\)，计算同一数量。两种方法均采用第 167 节的核定义；本节比较的是 \(\mathcal S'\)，实际自能斜率仍为 \(\Pi'_{hs}(0)=-\mathcal S'/(16\pi^2)\)。

### 184.2 五组质量矩阵输入的结果

下表中所有参数均以共同的任意质量单位表示。\(\mu^2\) 只用于单个 \(B_0^{\rm fin}\) 的对数；在完整组合中应当抵消。相对差定义为
\( |(\mathcal S'_{\rm direct}-\mathcal S'_{\rm closed})/\mathcal S'_{\rm direct}| \)。

| 点 | \((M_E,m_L,m_R,v_h,v_s,\mu^2)\) | \(m_1\) | \(m_2\) | \(\mathcal S'_{\rm direct}\) | \(\mathcal S'_{\rm closed}\) | 相对差 |
|---|---|---:|---:|---:|---:|---:|
| A | \((5,0.7,0.4,1,1,1.3)\) | 0.05528919 | 5.06428110 | -0.04590108265087706 | -0.04590108265087706 | \(9.9\times10^{-18}\) |
| B | \((3,0.8,0.25,2,1.4,2.1)\) | 0.06422151 | 3.11422151 | -0.01758340636406695 | -0.01758340636406695 | \(1.9\times10^{-17}\) |
| C | \((7,0.45,0.9,1.3,0.8,4.0)\) | 0.05727037 | 7.07171974 | -0.05129052347086095 | -0.05129052347086096 | \(9.0\times10^{-17}\) |
| D | \((2.5,0.3,0.6,1.1,1.7,0.9)\) | 0.06956519 | 2.58750086 | -0.02852022056451442 | -0.02852022056451442 | \(8.6\times10^{-17}\) |
| E | \((10,1.2,0.2,2.2,0.9,3.3)\) | 0.02382441 | 10.07370004 | -0.006079521409304066 | -0.006079521409304066 | \(1.2\times10^{-17}\) |

对五组矩阵，直接从旋转后顶角计算出的系数均呈现预期结构
\[
C^{(p)}=\begin{pmatrix}2X&-2X\\-2X&2X\end{pmatrix},\qquad
C^{(m)}=\begin{pmatrix}2X&-Z\\-Z&2X\end{pmatrix},
\]
并且数值上满足
\[
X(m_1^2+m_2^2)-Zm_1m_2\simeq0.
\]
恒等式残差在本次双精度奇异值分解的数值精度范围内。表中直接四通道积分与约化式之间约 \(10^{-17}\)–\(10^{-16}\) 的相对差，主要反映数值表示精度；它不是物理误差估计，也不应理解为对原论文所有模型约定的独立验证。

### 184.3 这次测试的意义与边界

本节新增了比第 183 节更完整的一层检查：参数点由原始质量矩阵生成，顶角由同一组左右奇异向量变换得到；四个有序通道逐一用参数积分求值，再与解析约化式比较。它支持以下结论：

1. 对本文使用的实 Dirac 质量矩阵和旋转约定，四通道系数矩阵与第 169 节的约化斜率表达式在五组非简并参数点上数值一致；
2. 质量矩阵给出的关系 \(X(m_1^2+m_2^2)=Zm_1m_2\) 在这些点上成立；
3. 完整有限组合中的公共重整化尺度依赖应当抵消，且逐通道求和与闭式化简相容。

但该检查仍共享同一套手征迹公式与 PV 约定，因此不能独立排除它们共同存在的整体符号或自由度计数错误。它也没有计算 EFT 侧泡图、双标量接触图和局域反项，更没有把二点函数斜率投影到完整规范不变维数六算符基底。故当前结果仍不能作为最终 \(C_{HS}^{(D)}\)。

### 184.4 状态更新

- [x] 从五组原始质量矩阵生成轻、重质量和质量基底顶角。
- [x] 用参数积分直接计算四个有序通道的有限斜率核。
- [x] 与四通道约化闭式比较，并核验质量恒等式。
- [ ] 从原始拉氏量重新逐项计算 EFT 泡图和 \(hs\bar\ell\ell\) 接触图，独立确定相对符号和归一化。
- [ ] 在统一重整化方案下完成 UV–EFT 斜率相减，并将结果映射到明确的非冗余规范不变算符基底。

**本节结论：** UV 四通道求和及其闭式约化已通过五组由原始质量矩阵生成的数值点检查。EFT 侧独立计算与最终 Wilson 系数识别仍是未完成的关键步骤。

## 185. 统一自能约定下的 UV–EFT 斜率相减：极点、有限项与可匹配范围

本节把第 172 节逐图得到的 EFT 结果与第 173、182、184 节采用的 UV 斜率核放在同一套记号中，明确区分“环图减除后的二点函数斜率”与“某个独立维数六 Wilson 系数”。以下计算沿用实参数 Dirac 费米子、外动量平方变量 \(q^2\)，并定义 1PI 振幅为 \(i\Pi_{hs}(q^2)\)。UV 侧仍以第 169 节的通道核为输入；由于其模型顶角归一化尚未与原始拉氏量逐项对照，本节所有 UV–EFT 差值均明确标为条件性结果。

### 185.1 EFT 侧：先分别保留泡图与接触图

令 \(g_5=y_hy_s\)，轻态质量为 \(m\)。第 172 节的泡图为
\[
\Pi_{\rm bub}(q^2)=-\frac{g_5}{16\pi^2}\left[4A_0(m^2)+(8m^2-2q^2)B_0(q^2;m^2,m^2)\right],
\]
接触图为
\[
\Pi_{\rm ct}(q^2)=-\frac{g_5}{16\pi^2}4A_0(m^2).
\]
接触图是无外动量的 tadpole，因此对 \(q^2\) 的导数为零；但它不能从完整自能中删掉，因为它参与零动量自能及其局部质量反项。两图相加后
\[
\Pi_{\rm EFT}(q^2)=-\frac{g_5}{16\pi^2}\left[8A_0(m^2)+(8m^2-2q^2)B_0(q^2;m^2,m^2)\right].
\]
在 \(d=4-2\epsilon\) 的 PV 约定下，取
\[
A_0(m^2)=m^2\left(\Delta_\epsilon+1-\ln\frac{m^2}{\mu^2}\right),\quad
B_0(0;m^2,m^2)=\Delta_\epsilon-\ln\frac{m^2}{\mu^2},\quad
B'_0(0;m^2,m^2)=\frac{1}{6m^2},
\]
可得
\[
\Pi'_{\rm EFT}(0)=-\frac{g_5}{16\pi^2}\left[-2\Delta_\epsilon+2\ln\frac{m^2}{\mu^2}+\frac43\right]
=\frac{g_5}{16\pi^2}\left[2\Delta_\epsilon-2\ln\frac{m^2}{\mu^2}-\frac43\right].
\]
故斜率极点是 \(+2g_5\Delta_\epsilon/(16\pi^2)\)。这一结果来自泡图的动量依赖部分；接触图的斜率确为零。这里的结论依赖于第 172 节已声明的顶角和积分约定。

### 185.2 UV 侧：公共极点与有限斜率

按第 169 节的实参数通道求和，定义
\[
\Pi'_{\rm UV}(0)=-\frac{\mathcal S'_{\rm UV}}{16\pi^2},
\]
其中
\[
\mathcal S'_{\rm UV}=-2XQ+\frac{8X}{3}-4\big[X(a+b)+Zm_1m_2\big]D_{12},
\]
\[
Q=B_{11}(0)+B_{22}(0)-2B_{12}(0),\quad
D_{12}=B'_0(0;a,b),\quad a=m_1^2,\ b=m_2^2.
\]
由于四通道的动量系数满足 \(\sum_{ij}C^{(p)}_{ij}=0\)，共同的 \(B_0\) UV 极点在完整 UV 求和中抵消；\(Q\) 也是有限的。故在当前表达式中，UV 斜率没有与 EFT 斜率相同的显式 \(\Delta_\epsilon\) 极点。这个抵消只针对当前 UV 通道组合，并不单独证明原始模型的全部重整化条件均已满足。

利用质量矩阵关系 \(X(a+b)=Zm_1m_2\)，可以将 UV 核写为
\[
\mathcal S'_{\rm UV}=-2XQ+\frac{8X}{3}-8X(a+b)D_{12}.
\]
其中
\[
Q=\frac{a+b}{a-b}\ln\frac ab-2,\qquad
D_{12}=\int_0^1dx\,\frac{x(1-x)}{xa+(1-x)b}.
\]
这些式子为有限 UV 阈值核，不应与 EFT 侧的局部极点混为一谈。

### 185.3 在同一约定下相减

定义裸斜率差
\[
\Delta\Pi'(0)=\Pi'_{\rm UV}(0)-\Pi'_{\rm EFT}(0).
\]
代入两侧表达式，得到
\[
\Delta\Pi'(0)=\frac{1}{16\pi^2}\left[-\mathcal S'_{\rm UV}-2g_5\Delta_\epsilon+2g_5\ln\frac{m_1^2}{\mu^2}+\frac{4g_5}{3}\right].
\]
这里差值中的极点为 \(-2g_5\Delta_\epsilon/(16\pi^2)\)，与 EFT 斜率自身的正极点相反；局域交叉动能反项需抵消 EFT 侧的正极点，符号必须按所定义的差值方向保持一致。若采用最小减除并把该极点吸收到局部算符反项中，剩余的有限斜率差为
\[
\boxed{\Delta\Pi'_{\rm sub}(0)=\frac{1}{16\pi^2}\left[-\mathcal S'_{\rm UV}+2g_5\ln\frac{m_1^2}{\mu^2}+\frac{4g_5}{3}\right].}
\]
注意这里对数项的符号：在定义 \(\Delta\Pi\prime=\Pi\prime_{\rm UV}-\Pi\prime_{\rm EFT}\) 下，它为正号；这是从 EFT 斜率的有限部分直接相减得到的，不能仅凭 UV 的有限核来猜测。

在 \(r=m_1^2/m_2^2\ll1\) 时，第 181 节的展开给出
\[
\mathcal S'_{\rm UV}=2X\ln r+\frac{8X}{3}+O(Xr\ln r),
\]
所以
\[
\boxed{\Delta\Pi'_{\rm sub}(0)=\frac{1}{16\pi^2}\left[2(g_5-X)\ln\frac{m_1^2}{\mu^2}+2X\ln\frac{m_2^2}{\mu^2}+\frac{4g_5-8X}{3}\right]+O\!\left(\frac{Xr\ln r}{16\pi^2}\right).}
\]
只有在目标匹配阶次允许把 \(g_5=X\) 当作领先阶近似时，才可进一步化为
\[
\Delta\Pi'_{\rm sub}(0)=\frac{X}{16\pi^2}\left[2\ln\frac{m_2^2}{\mu^2}-\frac43\right]+O\!\left(\frac{Xr\ln r}{16\pi^2}\right).
\]
如果 \(g_5-X\) 本身是与目标维数六系数同阶的高阶量，那么 \((g_5-X)\ln(m_1^2/\mu^2)\) 不能被丢弃；必须先从精确质量矩阵关系推导 \(g_5-X\) 的阶次，再决定是否简化。

### 185.4 目前可确定的结果与不能越过的步骤

1. **EFT 逐图结果：** 泡图与双标量接触图的相对符号、接触图的零斜率以及 EFT 斜率极点，已在第 172 节的明确约定下得到；本节将它们用于相减。
2. **UV–EFT 差值：** 在沿用第 169 节 UV 核及 \(\Pi'_{\rm UV}=-\mathcal S'_{\rm UV}/(16\pi^2)\) 的条件下，MS 型减除后的有限斜率差如上式所示。
3. **仍待独立检查的核心：** UV 原始相互作用拉氏量中的左右手顶角、旋转矩阵、Dirac 自由度计数与第 165–169 节系数定义，尚需从模型原始拉氏量逐项核对。若该处有整体符号或归一化变化，有限差值也会相应改变。
4. **Wilson 系数尚未唯一确定：** 二点函数的 \(q^2\) 斜率只给出背景场交叉动能的一个投影。要得到指定的 \(C_{HS}^{(D)}\)，必须先列出完整非冗余规范不变算符基底，处理 IBP/EOM 关系、场重定义和参数重整化，再把这个投影匹配到基底系数。

**本节结论：** 在既定 UV 核与 EFT 费曼规则下，UV–EFT 斜率差已被显式写出，极点与有限部分分离清楚；它是可用于后续检查的条件性匹配结果，而不是最终 Wilson 系数。下一步应优先从原始 UV 拉氏量重新推导质量基底顶角，并独立确认 UV 核的整体符号和归一化，再开展完整算符基底投影。

## 186. 将 EFT 与 UV 费曼图显式画入文档：拓扑、动量流与逐图对应

本节补充图形化的费曼图，方便对照第 172、169、185 节中的解析式。图中实线表示轻费米子 \(\ell\) 或质量本征态费米子 \(\chi_i\)，外部波浪线仅作为标量外腿的示意（不代表规范玻色子）；为避免混淆，图注明确标出标量场。所有图均为 1PI 两点函数图，外腿分别为 \(h\) 与 \(s\)，外部动量取 \(q\) 与 \(-q\)。

### 186.1 EFT 泡图：两个单标量 Yukawa 顶角

```text
                    h(q)
                      |
                      ●  -i y_h
                    /   \
             ℓ(k)  /     \  ℓ(k+q)
                  |       |
                  \       /
                    ●  -i y_s
                      |
                    s(-q)

        两条内部线闭合成一条费米子环；图中把环在左右两侧展开画出。
```

更标准的拓扑读法是：沿闭合费米子环依次经过 \(-iy_h\) 与 \(-iy_s\) 两个顶角，两个内部传播子的动量可选为 \(k\) 和 \(k+q\)。相应分子迹与 PV 约化见第 172.1 节：
\[
\operatorname{tr}[(\slashed k+m)(\slashed k+\slashed q+m)]
=4[k\cdot(k+q)+m^2].
\]
其积分表达式为
\[
\Pi^{\rm bub}_{hs}(q^2)=-\frac{y_hy_s}{16\pi^2}
\left[4A_0(m^2)+(8m^2-2q^2)B_0(q^2;m^2,m^2)\right].
\]

### 186.2 EFT 双标量接触图：单个 \(hs\bar\ell\ell\) 顶角

```text
              h(q)       s(-q)
                 \       /
                  \     /
                   ●  -i y_hs
                   |
                 ┌─┴─┐
                 │ ℓ │   单条内部费米子线闭合为 tadpole
                 └───┘

          顶角来自 - y_hs h s \barℓℓ
```

此图是单传播子的费米子 tadpole，不含外部动量流入传播子分母，因此 \(\partial\Pi^{\rm ct}/\partial q^2=0\)。但它的自能贡献不是零：
\[
\Pi^{\rm ct}_{hs}=-\frac{4my_{hs}}{16\pi^2}A_0(m^2)
=-\frac{4y_hy_s}{16\pi^2}A_0(m^2),
\qquad y_{hs}=\frac{y_hy_s}{m}.
\]
泡图和接触图的 tadpole 项同号；总自能必须先相加，再进行局部质量反项与动量斜率分析。

### 186.3 UV 侧四个有序质量本征态通道

UV 图的拓扑与 EFT 泡图相同，但两个内部费米子传播子的质量可以不同。四个有序通道分别为 \((i,j)=(1,1),(1,2),(2,1),(2,2)\)：

```text
                        h(q)
                          |
                    ●  Γ^h_ij
                  /           \
      χ_i(k)  ---/             \--- χ_j(k+q)
                |               |
                 \             /
                    ●  Γ^s_ji
                          |
                        s(-q)

       对每个 (i,j) 分别求和；一般 m_i ≠ m_j。
```

这里 \(\Gamma^h_{ij}\) 与 \(\Gamma^s_{ji}\) 是质量本征态基底中的标量顶角，须按原始拉氏量及旋转矩阵计算，不能仅凭图形假设相等。四通道的解析求和与闭式积分见第 169、183、184 节。图的拓扑示意本身不确定整体符号；闭合费米子环负号、顶角因子、Dirac 迹和有序态求和仍必须统一在同一个 \(i\Pi_{hs}\) 约定下。

### 186.4 可编译的 TikZ 图形源代码

若需要在支持 TikZ 的 LaTeX 文档中生成正式矢量图，可将下列代码复制到独立 LaTeX 文件中编译。这里使用普通 TikZ，避免依赖额外的 `tikz-feynman` 包。该图是拓扑示意，费米子箭头和动量标签可按论文排版需要再细化。

```latex
\documentclass[tikz,border=6pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,calc}
\begin{document}
\begin{tikzpicture}[>=Latex,thick,scale=1.0]
  % EFT fermion bubble: circular fermion loop with h and s insertions
  \draw[->] (-2.4,1.7) -- (-1.05,0.95) node[midway,above left] {$h(q)$};
  \draw[->] (2.4,-1.7) -- (1.05,-0.95) node[midway,below right] {$s(-q)$};
  \draw[thick] (0,0) circle (1.35);
  \draw[fill=white] (-0.95,0.95) circle (0.055);
  \draw[fill=white] (0.95,-0.95) circle (0.055);
  \node[above left] at (-0.95,0.95) {$-iy_h$};
  \node[below right] at (0.95,-0.95) {$-iy_s$};
  \node[above] at (0,1.45) {$\ell(k+q)$};
  \node[below] at (0,-1.45) {$\ell(k)$};
  \node at (0,-2.25) {EFT bubble};
\end{tikzpicture}
\qquad
\begin{tikzpicture}[>=Latex,thick,scale=1.0]
  % EFT contact tadpole, drawn as a loop attached to one hs insertion
  \draw[->] (-2.4,1.0) -- (-0.45,0.15) node[midway,above] {$h(q)$};
  \draw[->] (2.4,1.0) -- (0.45,0.15) node[midway,above] {$s(-q)$};
  \fill (0,0) circle (0.06);
  \node[above] at (0,0.08) {$-iy_{hs}$};
  \draw (0,0) -- (0,-0.25);
  \draw[->] (0,-0.25) arc[start angle=90,end angle=450,radius=0.55];
  \node[right] at (0.7,-0.25) {$\ell(k)$};
  \node at (0,-1.25) {EFT contact tadpole};
\end{tikzpicture}
\end{document}
```

### 186.5 图与计算式的对应检查表

| 图 | 内部传播子 | 顶角 | 对 \(q^2\) 的斜率 | 解析式位置 |
|---|---|---|---|---|
| EFT 泡图 | 两条轻费米子线，动量 \(k,k+q\) | \(-iy_h,-iy_s\) | 非零 | §172.1、§185.1 |
| EFT 接触 tadpole | 一条轻费米子传播子 | \(-iy_{hs}\) | 零 | §172.2、§185.1 |
| UV 通道 \((i,j)\) | 两条质量本征态线，质量 \(m_i,m_j\) | \(\Gamma^h_{ij},\Gamma^s_{ji}\) | 一般非零 | §169、§183–184 |

**核对边界：** 文档中的 ASCII 图与 TikZ 源码用于明确拓扑和顶角归属；它们不能代替从原始拉氏量导出的费曼规则。下一步仍应把 UV 顶角矩阵显式写出，逐项计算 \(\Gamma^h_{ij}\Gamma^s_{ji}\) 的标量与手征分量，并用相同的动量流和 \(i\Pi_{hs}\) 定义重新推导 UV 环图。只有该步骤核实后，才能把第 185 节的条件性斜率差升级为可信的匹配结果。


## 187. 将费曼图导出为 SVG 并嵌入 Markdown 正文

为避免普通 Markdown 阅读器只显示 TikZ 源码，本节将三类核心拓扑另行绘制为独立 SVG 矢量图，并通过相对路径嵌入本文。若 SVG 与本文档保存在同一目录，支持 SVG 的 Markdown 阅读器会直接显示下图；SVG 可无损缩放。图中蓝色闭合线表示费米子环，外部实线表示标量外腿。

![EFT 泡图、EFT 双标量接触 tadpole 与 UV 质量本征态泡图](higgs_portal_mixing_feynman_diagrams.svg)

**图中顶角约定：** EFT 泡图使用 \(-iy_h\) 与 \(-iy_s\)；接触图使用 \(-iy_{hs}\)；UV 图使用质量本征态顶角 \(\Gamma^h_{ij}\) 与 \(\Gamma^s_{ji}\)。本图是拓扑与顶角标签示意，不替代原始 UV 拉氏量对顶角矩阵、手征结构、整体符号和组合因子的推导。

**文件说明：** SVG 源文件为 `higgs_portal_mixing_feynman_diagrams.svg`。如果阅读器不显示 SVG，请确认 SVG 文件与 Markdown 文件位于同一文件夹；也可以直接用浏览器打开 SVG 文件查看。
