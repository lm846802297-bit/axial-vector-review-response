# DW13678 审稿意见分析与修改建议（修订版）

> **本文件是 `审稿意见分析-gpt.md` 的修订副本，原文件保持不动。**
> 修订依据：① 审稿报告 `dw13678_report_1_a.md` 原文；② 稿件本体 `axial_vector_model_building-v6.pdf`（*An Axial $U_A(1)_{L_\mu-L_\tau}$ UV Completion and Experimental Searches*，Fang, Guo, Li, Liu, Wang, Xiong）。
> 修订目标：① 每条意见都能对上审稿原文；② 每条都写清"稿件现在怎么说"；③ 每条都给出要做的工作。
>
> ⚠️ **文本抽取限制**：稿件的数学符号在文本层里有丢失（根号、$\pi$、希腊字母会变成方块或消失）。因此：
> - 凡带 `[待目视核对]` 的公式，请对着 PDF 原页确认后再引用。
> - 下文所有稿件引文中的**数学符号均为抽取还原**（例如把 `ms = 10 GeV and max S = 4` 还原为 $m_S=10$ GeV、$\lambda_S^{\max}=4\pi$），不是逐字形式；英文文字部分为逐字引用。
> - 还原的可靠性来自两处独立数值的交叉验证：正文例子（$m_S=10$ GeV、$\lambda_S^{\max}=4\pi$ ⇒ $v_S\gtrsim2.0$ GeV）与 Fig. 2 图注（$v_S=m_{A'}/(2g_X)=2$ GeV 的灰虚线），二者都指向 $m_S<\sqrt{2\lambda_S^{\max}}\,v_S$。

---

## 0. 本次修订改了什么

| # | 原文档的问题 | 本版的修改 |
|---|---|---|
| 1 | 式 (34) 被写成 $\lambda_\phi$ 形式，从未引用原式 | 补上稿件原式：$m_S<\sqrt{2\lambda_S^{\max}}\,v_S$、$v_S=m_{A'}/(2g_X)$（式 34），并附稿件的数值例子 |
| 2 | 把 Higgs 门户圈图来源写成"矢量样轻子 + 规范耦合圈" | 改为审稿人所说的 **$\mu,\tau$ 圈**，并给出正确的一圈主结果 |
| 3 | 纯轴矢极限的定义写成"$g_V=0$"，未回答 $\theta_{\mu R}\to0$ | 用稿件式 (16) 回答：$g_V=g_X\sin^2\theta_R$、$g_A=-g_X\cos^2\theta_R$；纯轴矢极限 ⇔ $\theta_R\to0$；显式声明在式 (36) |
| 4 | Major 1.2 只列了五个条件，缺构造路线与数字 | 补审稿人的构造路线 + 稿件式 (30)(31)、Table II、Fig. 2 的实际输入 |
| 5 | Major 4 的"$S$ 约束小节"只有一行 | 用稿件 Table II（$S$ 的低质量端约束）+ 式 (31)（转成 $g_X$ 限）+ B 工厂段落展开 |
| 6 | "引文献参数化"缺失 | 补：稿件已给出 $\epsilon\propto g_Yg_X\ln(M_E/M_{E'})$ 的参数化与文献引用 [1]，缺的是把它写显式 |
| 7 | Minor 3 / 4 被并进 major；Major 4.3 的前半段被放进 §2.4 | 全部按报告原编号重排（Major/Minor 各归各位） |
| 8 | Minor 6.3 / 6.6 各只答一半 | 用稿件的 B 工厂段与 Fig. 2 图注补全 |
| 9 | Minor 5 缺 Higgs factory 一半 | 补上，并给出可用的稿件素材（式 (34)、$S$ 的质量窗口） |
| 10 | "论文整体叙事清楚"这条表扬原文没有 | 删除，改回 Merits 的三条原话 |

---

## 1. 审稿人核心判断

**📎 原文｜¶1**
> "The authors construct an anomaly-free, renormalizable model in which an additional Abelian gauge field $A'$ has chiral couplings to muons and taus. This model realizes a limit where the $A'$ coupling to the $\mu$-$\tau$ current is axial. The second goal of the paper is to examine the phenomenology of this model in the axial limit."

**📎 原文｜Merits**
> "The model construction section is written clearly. While the key ingredients for constructing such a model already exist in the literature, the authors have put these ingredients together."
> "The phenomenology is reasonably well motivated (up to some of the points below) and are straightforward to follow."
> "The paper is presented in a way that will make it useful for model builders to implement into their own models."

**📎 原文｜¶2**
> "The paper presents results that are useful for the model building community. However, I have some significant reservations about key points that either should be included or otherwise justified in being excluded from the manuscript. … Revisions for these major points (even if only to clarify why they are not issues) are required before the paper is at the level of a PRD manuscript."

**提炼**：模型构造获认可（anomaly-free、可重整、手征耦合清楚、对 model builder 有用），但后半篇只研究了纯轴矢 $A'$ 的两参数 EFT，而前半篇的 UV 结构（标量 $S$、矢量样轻子、中微子）没有被带入唯象学——审查的重点就是"两半脱节"。

**判断**：审稿人正确。稿件引言自己写了（¶3 末）："a genuine axial gauge interaction is inseparable from its symmetry-breaking scalars and heavy-fermion sector … What remains missing is a unified axial $L_\mu-L_\tau$ treatment in which this UV structure and the experimental reinterpretation are developed together."——审稿人恰恰指出这个"unified treatment"没有做完整：$S$ 被剥离了。

**要做的工作**：把 §2「Major 1」的两项工作（$S$ 窗口 + Higgs 门户）作为全篇主轴，其余各条围绕它重排正文。

> ⚠️ 原稿第 1 节写的"论文整体叙事清楚"在报告里**没有对应表扬**（Merits 只有上面三条），已删除。

---

## 2. Major 1 ｜标量 $S$ 的唯象学

### 2.0 前言：两半脱节与式 (34)

**📎 原文｜Major 1 前言**
> "The second half of the paper reviews a set of experimental bounds on only an effective theory of the $A'$ axially coupled to the $L_{\mu-\tau}$ current. This leaves a major gap between these two parts of the paper: the authors show that their UV theory requires a scalar $S$ that cannot be arbitrarily decoupled from the low-energy dynamics, e.g. from (34) which states that $m_S^2<4\pi(m_{A'}/2g_X)^2$."

**🆕 稿件现状（必引）**

$$m_S<\sqrt{2\lambda_S^{\max}}\,v_S,\qquad v_S=\frac{m_{A'}}{2g_X}\tag{稿件 式 (34)}$$

> 稿件例子：*"For example, $m_S=10$ GeV and $\lambda_S^{\max}=4\pi$ require $v_S\gtrsim2.0$ GeV."*

代入验算：$\sqrt{8\pi}\times2.0=10.03\approx10$ ✔ 与稿件的 2.0 GeV 一致；连带确认 Figure 2 的灰虚线就是这条边界（见 Minor 6.6）。

$\lambda_S^{\max}$ 的来源（稿件 式 (28)(29)(30)）：

$$V(S)=-\mu_S^2|S|^2+\lambda_S|S|^4,\quad m_S=\sqrt{2\lambda_S}\,v_S,\quad y_{s\ell\ell}=\frac{m_\ell}{v_S}=\frac{2g_Xm_\ell}{m_{A'}}$$
$$\lambda_S=\frac{2g_X^2m_S^2}{m_{A'}^2},\qquad g_X<\frac{\sqrt{2\lambda_S^{\max}}\,m_{A'}}{2m_S}\ \ \texttt{[待目视核对]}$$

**⚠️ 修订**：审稿人引的是 $m_S^2<4\pi(m_{A'}/(2g_X))^2$，与稿件原式对照等价于取 $\lambda_S^{\max}=2\pi$（比稿件自用的 $4\pi$ 紧 $\sqrt2$ 倍）。回复时**用稿件原式并写明 $\lambda_S^{\max}$ 取值**，说明两种写法差一个 $\lambda_S^{\max}$ 的选择。

**要做的工作**
1. 在回复第一条就把式 (34) 原式抄上，并注明它与审稿人引的不等式之间差 $\lambda_S^{\max}$。
2. 在新增的 $S$ 一节开头放式 (34)，并交叉引用式 (29)(30)，说明"$m_S$ 由 $\lambda_S$ 控制、而 $\lambda_S$ 与 $(m_{A'},g_X)$ 绑定"。

---

### 2.1 $S$ 应成为论文的主张之一

**📎 原文｜Major 1.1**
> "It is thus an odd choice to exclude the scalar from the phenomenology of the effective theory: if the $S$ is unavoidable at phenomenologically relevant scales, shouldn't one of the main points of the paper be that the only known UV completion of an axial $L_{\mu-\tau}$ gauge boson has a prediction for a scalar particle in a mass range that can be probed by colliders?"

**🆕 稿件现状**：$S$ 目前只出现在 §II（式 28–34）与 §III 开头的一段说明里；结论（§V）**完全没有提 $S$**，只提了 $A'$ 的各类约束与 μ 子对撞机。

**要做的工作**
1. **先做文献核查**：稿件能不能支撑"the only known UV completion"。稿件引言只写了 "What remains missing is a unified axial $L_\mu-L_\tau$ treatment…"；若无法证明唯一性，回复里改用 "the minimal anomaly-free completion"——**不要沿用审稿人的措辞冒二轮风险**。
2. 摘要末句 + 引言末段各加一句：UV 完成必然给出一个质量被式 (34) 锁定的标量 $S$，其窗口可被对撞机检验。
3. 结论里补一段 $S$（现在的结论完全没有它）。
4. 新增小节「Phenomenology of the scalar $S$」，含：$m_S$ 窗口（2.2）、Higgs 门户与 Higgs 测量（2.3）、$S$ 的实验约束（5.0 的表）。

**回复要点**：`We agree: since S cannot be decoupled (Eq. 34), we have promoted it to one of the main results and added Sec. X + Fig. Y.`

---

### 2.2 $m_S$ 的允许质量范围

**📎 原文｜Major 1.2**
> "What is the range of phenomenologically allowed $S$ mass including perturbativity limits on $\lambda$ and a motivated range of $m_{A'}$ and $g_X$. For example: perhaps the authors imagine a range of $m_{A'}$ below some benchmark mass where certain experimental constraints on $g_X$ become very strong. Then with that set of constraints (which should be stated clearly, see minor point #1 below), one may give a range of $m_S$ and comment on the experimental constraints."

**🆕 稿件现状（这是本条的四个输入，原来一个都没用上）**

1. **式 (27) 的性质**（回答"constraints stated clearly"）：稿件 §II——
   > "The LEP leptonic-width measurements therefore constrain $|\varphi_L|$ at the few-percent level, approximately $|\varphi_L|\lesssim4\times10^{-2}$ at 95% confidence level. Global vector-like-lepton fits can further constrain … We therefore adopt the conservative benchmark $|\theta_{L,R}|,|\varphi_{L,R}|\lesssim10^{-2}$."
   → 式 (27) 是**由 LEP 轻子宽度 + VL 全局拟合推来的上限**，不是任取的 benchmark。
2. **$g_X$ 的上限来源**：Fig. 2 的各条排除线（PIENU、NA62、CCFR/CHARM II、$(g-2)_\mu$、NA64$\mu$、BaBar/Belle II/CMS 四 μ）——本条的"strongly constrained region"就在这里，逐质量段取最紧的那条。
3. **$S$ 自身的约束如何转成 $g_X$ 的限**（稿件 式 (31)，关键）：
   $$g_X\lesssim\frac{y_{s\ell\ell}^{\lim}(m_S)\,m_{A'}}{2m_\mu}\simeq4.7\times10^{-3}\,y^{\lim}_{s\ell\ell}(m_S)\,\frac{m_{A'}}{\rm MeV}$$
   配上 **Table II**（$S$ 低质量端 $\ell\ell$ 耦合上限）：

   | $m_S$ 区间 | 约束来源 | $y^{\lim}_{s\ell\ell}$ |
   |---|---|---|
   | $m_S<10^{-10}$ eV | 中子星双星 | $10^{-20}$ |
   | $m_S\gtrsim10^{-2}$ eV | 第五种力 | $10^{-16}$ |
   | $m_S\gtrsim100$ keV | 中子星冷却 | $1.2\times10^{-12}$ |
   | $m_S\gtrsim\mathcal{O}(10)$ MeV | SN 1987A | $4.2\times10^{-9}$ |
   | $100\ \text{keV}\lesssim m_S\lesssim\mathcal{O}(10)$ MeV | SN 1987A + 弥散 $\gamma$ | $5\times10^{-11}$ |

4. **$(g-2)_\mu$ 与 $m_S$ 的耦合**（稿件 §IVA 末，直接影响窗口的边界）：
   > "The black $(g-2)_\mu$ contour in Fig. 2 is therefore not valid for arbitrary $m_S$: it corresponds to the scalar-decoupling benchmark $m_S\gtrsim10$ GeV … For a light scalar, Eq. (57) must instead be used and the exclusion can weaken or disappear near the cancellation region."
   且 $m_S\gtrsim m_\mu$ 时标量贡献为正、量级是轴向项的 3 倍（式 58）：$\Delta a_\mu^{S}\simeq\frac{3g_X^2m_\mu^2}{4m_{A'}^2}$，与负的轴向项在 $m_S\sim\mathcal{O}(m_\mu)$ 附近**相消**。

**要做的工作**
1. **照审稿人给的路线走**：取 2–3 个 $m_{A'}$ benchmark（其中一个取在 $g_X$ 约束最强的质量点）→ 读该处 $g_X^{\max}$（Fig. 2）→ 由 $v_S=m_{A'}/(2g_X)$ 得 $v_S$ 区间 → 由式 (34) 得 $m_S^{\max}=\sqrt{2\lambda_S^{\max}}\,v_S$。
2. **$\lambda_S^{\max}$ 两档都给**：$4\pi$（稿件自用）与 $\pi$（审稿人引用形式对应的口径），并说明差别。
3. **下限**由三部分构成：$S$ 的直接约束（Table II 与式 31，注意 Table II 覆盖到 $10^{-10}$ eV）、B 工厂标量搜索（见 Minor 6.3）、以及 Higgs 测量（见 2.3）。
4. **把 $(g-2)_\mu$ 的 $m_S$ 依赖性画进去**：标量与轴向项在 $m_S\sim\mathcal{O}(m_\mu)$ 相消 ⇒ 该处 $(g-2)_\mu$ 的排除会减弱甚至消失——这正是"$m_S$ 窗口 + 实验约束"必须一起给的原因。
5. **产出**：正文新 §X.1 + 图 1（$m_S$ 窗口：横轴 $m_S$、纵轴 $g_X$，叠加式 (34) 线、Table II/式 (31) 的 $g_X$ 限、B 工厂区、Higgs 简并带）+ 表 1（每个 benchmark：$m_{A'}$、$g_X^{\max}$、$v_S$、$m_S^{\min}$、$m_S^{\max}$、主导约束）。

**回复要点**：`Taking m_S ≳ 10 GeV as before, Eq. (34) converts each (m_{A'}, g_X) point into a hard upper bound on m_S; conversely, the scalar bounds of Table II (via Eq. 31) bound g_X from below…`——**必须给数字**。

---

### 2.3 Higgs 门户混合必须定量

**📎 原文｜Major 1.3**
> "Above (34): the authors 'assume negligible Higgs-portal mixing.' Is this interaction not generated at loop level? It seems that $S$-$h$ mixing cannot be avoided due to $\mu$ and $\tau$ loops. In turn, this seems like it would lead to strong experimental bounds on the UV completion. In fact, once there is mixing, is there not a resonance where the mixing becomes large as $m_S\to m_h$? It would be useful to quantify the size of this mixing over the allowed range of $m_S$. Existing Higgs measurements may set the strongest bounds on the UV completion. If these bounds are obviously negligible …, then the authors should present this as the justification for ignoring $m_S$ … (Though I am still skeptical that the $m_S$ can be ignored since it cannot formally decouple.)"

**🆕 稿件现状（两处）**
- §II 末：*"working in the scalar-decoupling regime $m_S\gtrsim10$ GeV with negligible Higgs-singlet mixing"*——这正是审稿人质疑的假设，稿件只是声明，没有论证。
- 稿件**没有**给出 $\lambda_{HS}$ 的圈级估计，也没有简并区的讨论。

**⚠️ 修订**：原稿把圈图来源写成"带 Higgs 与 $U(1)'$ 耦合的矢量样轻子圈 + 规范耦合"，模板写成 $\frac{1}{16\pi^2}(\text{Yukawa}\times\text{gauge})\log\frac{\Lambda}{\mu}$。**审稿人说的是 $\mu$ 和 $\tau$ 圈**；用已完成的一圈实算替代：$\delta m^2_{Sh}=-\frac{(y_1y_2)^2}{8\pi^2}vv_S=-\frac{M^2m_\tau^2}{2\pi^2vv_S}$（$\tau$ 主导，$\mu$ 圈小 $(m_\mu/m_\tau)^2$，**无对数增强、非退耦**）。

**要做的工作**
1. 正文加一句概念澄清：$\lambda_{HS}|H|^2|S|^2$ 是**规范对称允许的可重整算符**，"可忽略"是参数选择而非对称性结论。
2. 给出 $\sin2\theta_{Sh}$ 在 $m_S$ 允许窗口上的**曲线/表**（审稿人明确要"over the allowed range of $m_S$"）。
3. 给出 $m_S\to m_h$ 的**排除带宽度**（近简并时混合趋于最大），并画进 2.2 的窗口图。
4. 给出 $m_S<m_h/2$ 时 $h\to SS$ 的约束——它同时给 $M_E$ 一个上限，可作为"Higgs 测量给最强限制"的答案。
5. **明确表态**：不再声称 $S$ 可忽略，而是把它作为 UV 完成的预言（与 2.1 一致）。

---

## 3. Major 2 ｜有效理论参数的可行域

**📎 原文｜Major 2**
> "To further aid in the comparison between the UV theory and the two-parameter low-energy theory, it would be useful to explicitly state in one place (perhaps in a table or a figure like Fig. 2) the range of the effective model parameters that are feasible. The main phenomenological results are in Fig. 2, but it was not clear why this range of couplings and $A'$ masses were chosen: are values outside this range not allowed? What, if anything, does the perturbativity of the UV theory impose on the effective parameters?"

**🆕 稿件现状**：稿件已有两处现成答案，只是分散——
- 式 (35) 与正文：*"Under these assumptions, the phenomenology considered below is described, to the stated accuracy, by two independent parameters $\{m_{A'},g_X\}$, $v_S=m_{A'}/(2g_X)$."*
- §II 末：*"Figure 2 therefore represents constraints on this conditional two-dimensional slice of the full parameter space; relaxing these assumptions, in particular toward a light scalar, would reintroduce additional mass-dependent constraints such as those summarized in Table II."*
- 质量范围（摘要）：*"$A'$ masses from the MeV scale to the TeV scale"*——这正好回答 Minor 1 的"light 指什么"。

**要做的工作**
1. 把"benchmark 假设"集中成一张表（$Q=1$；$y_\varphi=0$；$M_{E'}=M_E>10$ TeV 且匹配标度处动能混合为零；$|\theta_{L,R}|,|\varphi_{L,R}|\lesssim10^{-2}$（式 27）；$m_S\gtrsim10$ GeV + 可忽略 Higgs–$S$ 混合；逐点施加式 34）+ 四列：理论范围 / UV 可实现 / 实验允许 / 本文展示。
2. 把式 (27) 的来源（LEP + VL 拟合）写进这张表，回答"为什么取这个范围"。
3. 画一张 (m_{A'},g_X) 分区图：UV 可实现 / 被排除 / 微扰性外 / 本文展示，并标出 Fig. 2 的原边界。
4. 明确写"范围外不是没研究，而是被某条约束排除或非微扰"。

---

## 4. Major 3 ｜中微子振荡

### 4.0 前言

**📎 原文｜Major 3 前言**
> "The Standard Model is defined with only left-handed neutrinos because of the possibility that neutrinos are their own antiparticle. In such a case neutrino masses are generated through, e.g. through the Weinberg operator."

**🆕 稿件现状（关键！）**：**稿件全文没有处理中微子质量或 PMNS**。核对结果：引言里唯一提到中微子质量的一句是在介绍**常规矢量** $L_\mu-L_\tau$ 模型（"This economical structure has been connected to neutrino masses and mixing, a positive contribution to the muon anomalous magnetic moment…"），说的是别的模型；结论（§V）**完全没有**中微子、PMNS、Weinberg 算符。稿件只说 $U_A(1)_{L_\mu-L_\tau}$ 对带电轻子的电荷指派与 universal-seesaw 机制（见 §II 的 seesaw 段落与式 21 附近）；中微子只在“流”（trident、太阳中微子、不可见衰变）的意义上出现——引言明写 *"the neutrino current remains left-handed"*，全文目录里也没有中微子质量一节。

→ **这意味着 Major 3 不是"解释不清"，而是正文真的缺这一块**。回复必须给方案，不能只澄清。

### 4.1 Weinberg 算符与 Yukawa 的"对齐"

**📎 原文｜Major 3.1**
> "In this model, $U_A(1)$ invariance allows Weinberg operators for each generation. However, it appears that both the Yukawa matrices and neutrino masses must be aligned and therefore a non-trivial PMNS matrix does not appear to be possible."

**想做的工作**（原稿只写成条件句"如果带电轻子 Yukawa 也被迫对角"，没证明）：
1. 从稿件 Table I 的电荷表出发，逐条列出 Weinberg 算符 $(L_iH)(L_jH)$ 在 $U_A(1)$ 下的电荷，判定哪些条目允许。
2. 对带电轻子 Yukawa $\bar L_iH\ell_j$ 做同样的表。
3. 若两矩阵都被限制在同一分块结构上 ⇒ 同时对角化 ⇒ $U_{\rm PMNS}=\mathbf 1$；把**分块结构**写出来，而不是写"近似对角"。
4. 产出：正文新 §Y.1 + 张表（条目 / $U_A(1)$ 荷 / 允许或禁戒）。

### 4.2 右手中微子是否可行

**📎 原文｜Major 3.2**
> "Perhaps a full model would require right-handed neutrinos. These would now be charged under $U_A(1)$, which likely means the second and third generation must appear as vectorlike combinations. However, it seems to me that mixing between generations is prohibited by $U_A(1)$."

**要做的工作**：正面核验原文的两个断言——① 带 $U_A(1)$ 荷的 $N_R$ 是否被迫成矢量样对；② $\bar L_iHN_{Rj}$ 与 $N^cN$ 的非对角项是否被禁。写出允许/禁戒条目表，给结论（原文担心的"代际混合被禁"是否成立）。**不要只检查"是否引入新反常"**——那偏离了原文的关切。

### 4.3 给出方案，或引已知方案

**📎 原文｜Major 3 结尾**
> "Thus it is not obvious to me how neutrino oscillations can be included in this framework. If there is a simple solution, the authors should include it. If there is a known less-simple solution in the literature, the authors should cite this. Otherwise, at best this will be a confusing point. At worst, it would make the construction inconsistent with neutrino oscillation experiments."

**要做的工作**（这是全文工作量最大的一条，且稿件目前零基础）
1. 先写 no-go（4.1、4.2），让审稿人看到问题被认真对待。
2. **给修复方案**：引入带**奇** $U_A(1)$ 荷的标量以打开被禁戒的代际条目（$S$ 只提供偶数倍荷，补不出奇数倍），重新验证反常消除、Yukawa、质量矩阵、PMNS。
3. **做数值拟合**：3 个混合角 + 2 个 $\Delta m^2$ ⇒ 定出 Yukawa 组合，给 1–2 个 benchmark 点（不要只说"可通过额外右手中微子实现"）。
4. **检查修复的代价**：非对角 Yukawa 打开后 $A'$ 会有树级轻子味破坏（$\mu\to3e$、$\mu$–$e$ 转换），必须实算并给系数上限——**这是修中微子带来的新约束，稿件的 Fig. 2 与 Table II 都没有**。
5. 证明修复**不动轴向结构**（新标量不进入 $\mu,\tau$ 的规范耦合），否则后半篇全部要重做。
6. 若最终决定不扩展模型，则必须在正文明确写出"本模型的 UV 完备性覆盖规范扇区与带电轻子扇区，中微子扇区需要额外场内容"，并给出该扩展的轮廓——**不能只补一句引用**。

**🖊 我们自己的提醒**：原稿给的三条路线（A/B/C）只写了名字，没有取舍准则。建议明确写："优先 A，不可行则 B，C 只作为最后退路，因为审稿人把这条标为 critical。"

### 4.4 中微子振荡约束（与 Major 3 重复）

**📎 原文｜Major 4.1**
> "Neutrino oscillation observations. See point #3 above. It appears that this model predicts a unit PMNS matrix, which is inconsistent with neutrino oscillations."

**要做的工作**：不重复论证，在约束完备性表里占一行 + 一句 "See our reply to Major point 3."

---

## 5. Major 4 ｜实验约束是否完整

### 5.0 前言与 $S$ 约束小节

**📎 原文｜Major 4 前言**
> "It is not obvious if this is the full set of constraints on the model. (See also point #1 above: I would have liked to see a section discussing the bounds on the $S$ within this model since it cannot be decoupled.) The following experimental bounds seem like they could be relevant. It would be helpful to either include them or justify why they are subdominant to the experiments presented."

**🆕 稿件现状**：
- $A'$ 的约束在 **Fig. 2**（PIENU、NA62、CCFR/CHARM II、$(g-2)_\mu$、NA64$\mu$、BaBar/Belle II/CMS 四 μ）。
- $S$ 的约束在 **Table II**（低质量端，见 2.2 的表）与 §III 前的 B 工厂段（$0.04\ \text{GeV}\lesssim m_S\lesssim6.5$–7 GeV，Belle II 到 9–10 GeV）。**即：稿件已经有 $S$ 约束，但它们散落在 §II/§III 之间，没有独立小节。**
- 稿件的完备性声明：*"Figure 2 therefore represents constraints on this conditional two-dimensional slice… relaxing these assumptions, in particular toward a light scalar, would reintroduce additional mass-dependent constraints such as those summarized in Table II."*

**要做的工作**
1. **新增独立小节「Bounds on the scalar $S$」**：把 Table II + 式 (31) + B 工厂段 + $h\to SS$/简并带（见 2.3）合成一处。
2. 建"约束完备性表"（约束 / 是否纳入 / 主导质量段 / 若不纳入的定量理由），行至少含：中微子振荡、动能混合、$S$ 搜索、有限 $g_V$、恒星冷却、Higgs 数据、矢量样轻子直接搜索、$(g-2)_\mu$、轻子味破坏。
3. **完备性论证要有结构**：不是"我们列全了"，而是"在每个质量段，未列出的实验上限比列出的弱 $N$ 倍"。
4. 说明 Fig. 2 是**条件切片**（式 35 的 $\{m_{A'},g_X\}$），并指出放宽哪个假设会加回哪类约束——稿件已有这句话，要把它放到小标题下。
5. ⚠️ **稿件的 $(g-2)_\mu$ 等值线本身是 $m_S$ 相关的**（§IVA 末）：要在图注和正文都写清"该等值线对应 $m_S\gtrsim10$ GeV 的标量退耦 benchmark"。

---

### 5.1 动能混合的定量估计

**📎 原文｜Major 4.2**
> "There is no quantitative estimate of the amount of kinetic mixing generated with the 'benchmark' choices of $\theta\le10^{-2}$. The authors make the insightful point that kinetic mixing goes to zero in the axial limit, but because this limit is tied to the size of the mixing (the mass of the vectorlike leptons), for the above benchmark there is non-zero kinetic mixing. It would be useful to have parametric estimates … One could invoke parametric expressions in the literature for the relevant loop diagrams."

**🆕 稿件现状（审稿人要的"文献参数化表达式"稿件里已经有了）**：§II（式 22 之后）——
> "The degeneracy also controls hypercharge–$U_A(1)_{L_\mu-L_\tau}$ kinetic mixing. The two vector-like leptons have the same hypercharge and opposite $U_A(1)$ charges, so their one-loop threshold contributions cancel when $M_{E'}=M_E$. More generally, a mass splitting would generate a finite contribution proportional to $g_Yg_X\ln(M_E/M_{E'})$ [1]. We take the kinetic-mixing coefficient to vanish at the matching scale; below the heavy-lepton threshold, the pure-axial light-lepton charge assignment does not regenerate it at one loop, up to the mixing-suppressed corrections neglected in our benchmark."

以及 §IVA：*"the parity-even photon–$A'$ kinetic mixing vanishes at one loop in the pure-axial limit; any electronic coupling induced by the small vector admixture or by the heavy sector is benchmark dependent and suppressed."*

**判断**：
- 参数化形式 **已有**且带文献引用（[1]）：$\epsilon\propto g_Yg_X\ln(M_E/M_{E'})$——这正面回应了审稿人的 "one could invoke parametric expressions in the literature"。
- 但**关键的一步没写显式**：benchmark 取 $M_{E'}=M_E$，所以这个对数**恒为零**，剩下的只有 $\theta$-压低项。审稿人的担心（"θ 有限 ⇒ 动能混合非零"）恰恰指向这一项，而稿件只有一句"suppressed"。
- ⚠️ 另有一处待核：稿件主张"轻子扇区在单圈不重新生成"；若按 $m_\mu\neq m_\tau$ 的有限项会有残余，两说必须对齐后再写数字。

**要做的工作**
1. 把 $\epsilon\propto g_Yg_X\ln(M_E/M_{E'})$ 显式写成公式（引文献 [1]），并说明在 benchmark（$M_{E'}=M_E>10$ TeV）下它**严格为零**。
2. 给出**残余项**的估计：由 $\theta_{R}$ 压低的项 + 轻子扇区的有限项，量级用 $\epsilon\sim\frac{g_Yg_X}{16\pi^2}\times\mathcal{O}(\theta_R^2)$ 之类写清，并在 $g_X$ 网格上给数。
3. 与实验限（$\epsilon\lesssim10^{-3}$ 量级）比较，明确说"比限小 $N$ 个数量级"——**不要只写形容词**。
4. 说明残余**不随 $\theta_R\to0$ 自动消失**的部分（若确有）来自哪里。

---

### 5.2 残余 $g_V$ 与矢量限的比较

**📎 原文｜Major 4.3**
> "Another way of reframing the above point: the bounds presented are in the pure axial limit. Since the authors present a UV model that only realizes the axial coupling in a decoupling limit, it would be useful to comment on possible experimental bounds on the small vector-like coupling in a model with non-infinite vectorlike fermion masses. If these bounds are always small compared to the axial bounds, this should be stated and justified. … sometimes a vector interaction is more tightly constrained than its axial counterpart."

**🆕 稿件现状（答案的一半已在稿件里）**：§IVA——
> "With nonzero mixing, Eq. (16) gives $g_V=g_X\sin^2\theta_R$ and $g_A=-g_X\cos^2\theta_R$. Under Eq. (27), the induced vector term and vector-like-lepton loop effects are negligible."

**要做的工作**
1. 直接引用式 (16) 的 $g_V=g_X\sin^2\theta_R$，得 $g_V/g_A\simeq-\theta_R^2$；代入式 (27)（$\theta_R\lesssim10^{-2}$）⇒ $|g_V/g_A|\lesssim10^{-4}$。
2. 把 $|g_V|$ 与最敏感实验的 $g_V$ 上限（neutrino trident / Borexino / NA64$\mu$ / BaBar / beam dump）逐条对比，写成一张表。
3. 写一句判定式：在式 (27) 的 $\theta$ 上限下，残余矢量耦合比其实验限小 $N$ 个数量级（$N$ 要算出来）——这正是"stated and justified"。
4. 若发现某质量段矢量限更强 ⇒ **必须重画 Fig. 2 的排除区**（审稿人明说了）。
5. 把稿件现有的"Under Eq. (27) … negligible"这句从断言升级为带数字的论证。

> ⚠️ 原稿把这一条的前半段（"某些实验对矢量更敏感"）放进了 Major 4.2 的小节里，已按报告编号移回本条。

---

### 5.3 恒星冷却是否适用

**📎 原文｜Major 4.4**
> "Are stellar cooling bounds not relevant? See e.g. 2511.09619 for a recent paper on this. If they are not, then this is certainly worth justifying."

**🆕 稿件现状（与审稿人假设不同！）**
- 稿件的质量范围是 **MeV 到 TeV**（摘要），Fig. 2 的最低端由 PIENU（$\pi$ 衰变，$m_{A'}<33.9$ MeV）给出。
- $S$ 的约束则明确覆盖**极轻端**（Table II：从 $10^{-10}$ eV 到 $\mathcal{O}(10)$ MeV，含中子星冷却、SN 1987A）——即**恒星/超新星冷却对 $S$ 是纳入的，对 $A'$ 没有**。

**要做的工作**
1. **不要一刀切**。按质量段回答：对 $A'$，若所取 benchmark 在 GeV 以上，则写"超新星核心温度 30–50 MeV，热产生被 Boltzmann 压低；2511.09619 覆盖的是 sub-GeV 矢量耦合，与我们的区间不重叠"；若讨论到 MeV 端，则必须说明该文是否适用并给出阈值。
2. 对 $S$，直接引用 Table II 的对应行（中子星冷却 $1.2\times10^{-12}$、SN 1987A $4.2\times10^{-9}$）——**这里已经有了，不需要新算**，只需说明"我们把 $S$ 的冷却约束纳入了"。
3. 写出质量阈值与压制机制，不能只写"不适用"。

---

## 6. Minor Points

### m1 ｜参数范围与 "light" 的定义
**📎 原文｜Minor 1**：*"…difficult for the reader to envision the mass and coupling range that the authors are targeting … they should define 'light.' (see, e.g. the first word of the introduction, which is not defined with respect to any reference mass scale.)"*

**要做的工作**：用稿件自己的范围（MeV–TeV）锚定：给三段物理阈值分区（$m_{A'}<2m_\mu$；$2m_\mu\lesssim m_{A'}\lesssim10$ GeV；$m_{A'}\gtrsim10$ GeV），明确声明本文关注哪一段，并把引言第一个词改成带数值的形式或删掉。

### m2 ｜纯轴矢极限的定义（**本版已能确定回答**）
**📎 原文｜Minor 2**：*"Equation (12) gives the coupling of the $A'$ to the mass-basis fields. It is here that the pure axial coupling limit is defined? i.e. $\theta_{\mu R}\rightarrow 0$? … a phrase which is used below (36) but not otherwise quantified."*

**🆕 稿件现状**：式 (16) 给出 $g_V=g_X\sin^2\theta_R$、$g_A=-g_X\cos^2\theta_R$；式 (36) 的约化拉氏量里直接写 $g_V=0$、$g_A=g_X$（§IVA 亦重复此句）。

**答案**：**是的**——$\theta_R\to0$ 等价于 $g_V\to0$，且这个极限的显式声明位置在式 (36) 而不是式 (12)；定量关系 $g_V/g_A\simeq-\theta_R^2$。

**要做的工作**：在式 (12) 之后（或式 16 之后）加一句定义 + 在式 (36) 处交叉引用；回复里明确写"审稿人的猜测正确，我们把定义写进了正文 Eq. (X)"。

### m3 ｜矢量样轻子质量下限
**📎 原文｜Minor 3**：*"Because the mixing angles scale inversely with the vectorlike lepton masses, it would be helpful to present lower limits on these masses … How do these bounds compare with the $\theta_{(\mu,\tau)(L,R)}$ bounds in equation (27)?"*

**🆕 稿件现状**：稿件用的是 $M_{E'}=M_E>10$ TeV 的**退化 benchmark**（式 22），混合角的上限则由 LEP + VL 拟合给（式 27）。也就是说**顺序与审稿人设想的相反**：稿件不是从 $M$ 下限推 $\theta$ 上限，而是直接把 $\theta$ 限制在 $10^{-2}$。

**要做的工作**：补一段把两件事连起来——给出 $M_E$ 的直接搜索下限（LHC VL 轻子、LEP、电弱精确测量），由 $\theta\sim yv/M_E$ 换算成 $\theta^{\max}$，与式 (27) 的 $10^{-2}$ 比较，说明式 (27) 是否比直接搜索更紧。产出：一张小表。

### m4 ｜"conservative benchmark" 的含义（**本版已能确定回答**）
**📎 原文｜Minor 4**：*"Equation (27) is presented as a 'conservative benchmark.' What does this mean? … readers would want to understand if $10^{-2}$ is an experimental upper limit or simply a convenient choice."*

**🆕 稿件现状**：式 (27) 上一句已经说明来源——*"The LEP leptonic-width measurements therefore constrain $|\varphi_L|$ … approximately $|\varphi_L|\lesssim4\times10^{-2}$ at 95% CL. Global vector-like-lepton fits can further constrain …"* 因此它是**由实验推出的保守上限**。

**要做的工作**：把式 (27) 的措辞改为"an upper bound derived from LEP leptonic widths and global VL fits, adopted conservatively"，并在正文/图注/回复三处统一。**不需要新计算。**

### m5 ｜缪子对撞机一节去留
**📎 原文｜Minor 5**：*"…does not justify why a future muon collider is the way to test this model … Why not also include polarization asymmetries? Or would there be asymmetries in the $ee$ versus $\tau\tau$ final states? … the real 'smoking gun' for this UV completion is the physics of the $S$ particle which should be tested in any Higgs-factory phase of a future lepton collider. … either adds too little and should be downplayed …, or … its own full fledged exploration."*

**🆕 稿件现状**：稿件结论已经把 μ 子对撞机定位为"angular distribution / forward-backward asymmetry 才是判别量"，这与审稿人"只讲 total rate 不够"的意见同向；但**对 $S$ 的探测（尤其 Higgs factory）完全没有**。

**要做的工作**（二选一，建议"压缩 + 补 $S$"）
1. 压缩：保留"为什么 μ 子对撞机适合测 $\mu$ 耦合的 $A'$"、"角分布/前后不对称的判别力"、一句"future test 示例"；删掉与 Ref 83 重复的部分。
2. **补一段 $S$ 的探测**（这一步把本节与论文前半连起来）：Higgs factory 阶段的 $e^+e^-\to ZS$、$S$ 的稀有 Higgs 衰变（$h\to SS$）、以及在 μ 子对撞机上 $\mu^+\mu^-\to S$ 的窄共振——**$S$ 的质量与耦合由式 (34) 与 Table II 锁定，是最有判别力的预言**。
3. 保留审稿人点名的两项对比：polarization asymmetry、$ee$ vs $\tau\tau$ 末态。

**回复要点**：`We have downplayed the LO rate comparison as suggested and added a subsection on S production at a Higgs factory, since S is the actual prediction of the UV completion.`

### m6 ｜术语逐条替换

**📎 原文｜Minor 6**（六条）
> **6.1** "The word 'light' on page 2 has no reference scale."
> **6.2** "At the bottom of page 11, when referring to Table II, the authors write 'representative bounds.' What does representative mean? … Is the list 'complete' in any sense?"
> **6.3** "'…do not provide a universal $g_X$ bound, but they show that the intermediate scalar-mass region cannot simply be assumed unconstrained.' What does intermediate mass mean? It is also not clear what the intended content of this statement is: are the authors presenting a bound? Why would the reader assume that a new particle in this range would be unconstrained?"
> **6.4** "Below (34): 'we impose Eq. (34) point by point', it's not clear what is meant by 'point.'"
> **6.5** "Page 21, first paragraph of Section E. What is the 'parameter region of interest'? This wasn't clearly defined anywhere."
> **6.6** "Page 21, end of section D: What's the significance of the $v_S=2$ GeV line? What does it mean that $y_{s\mu\mu}$ 'becomes large' (nonperturbative)? Why plot it? Is it a perturbativity bound?"

**🆕 稿件现状（三条现在已有确定答案）**
- **6.3**：稿件原文的上下文是 B 工厂轻标量搜索——*"BaBar and Belle searched for $e^+e^-\to\mu^+\mu^-S$ followed by $S\to e^+e^-,\mu^+\mu^-$ for $0.04\ \text{GeV}\lesssim m_S\lesssim6.5$–$7$ GeV … Belle II four-lepton resonance searches reach approximately $9$–$10$ GeV, but their published interpretations assume a spin-one mediator … The $AA$ mode can dominate, in which case the visible leptophilic-scalar limits require a branching-ratio recast."* 所以"intermediate"=**B 工厂区（约 0.04–10 GeV）**；那句话的**内容**是"这一段有（需 BR 重铸的）标量约束，不能假设无约束"，且经式 (31) 会**转成对 $g_X$ 的限**。
- **6.6**：Fig. 2 图注已经写明——*"The gray dashed line marks $v_S=m_{A'}/(2g_X)=2$ GeV; for the benchmark $m_S\gtrsim10$ GeV with $\lambda_S\approx4\pi$, the region above this line does not satisfy perturbativity."* 即这条线是**式 (34) 的扰动性边界在 benchmark 下的等值线**；$y_{s\ell\ell}=m_\ell/v_S=2g_Xm_\ell/m_{A'}$ 变大是因为 $v_S$ 变小——"becomes large"就是**非微扰**，是。
- **6.5**：稿件的"parameter region of interest"出现在 §III E——*"In the parameter region of interest, the produced $A'$ promptly decays into a pair of charged leptons or neutrinos…"*，指 $A'$ **即时衰变**的那一段参数。

**替换表**

| # | 位置 | 改成 | 说明 |
|---|---|---|---|
| 6.1 | 引言首词 | "$A'$ with masses from the MeV to the TeV scale" 或删掉 "light" | 与摘要一致 |
| 6.2 | Table II 上方 | "a non-exhaustive selection of order-of-magnitude bounds; the completeness of the constraint set is discussed in Sec. Z" | Table II 是**标量**约束表，务必说明 |
| 6.3 | §II 末 | 明确：这是 B 工厂区（$0.04$–$10$ GeV）的标量约束，经式 (31) 转成 $g_X$ 的**下限/上限**；并说明为何该段此前被认为"unconstrained"（无普适的 published exclusion） | 回答"这句话在陈述什么" |
| 6.4 | 式 (34) 下方 | "at each point of the $(m_{A'},g_X)$ grid" | 消除歧义 |
| 6.5 | §III E 首段 | 直接写"$m_{A'}$ 满足 $A'\to$ 轻子即时衰变的那一段"，并在 Fig. 2 图注重复 | |
| 6.6 | §II 末 / 图注 | 保留图注，并在正文加一句：这条线即式 (34) 在 $m_S=10$ GeV、$\lambda_S=4\pi$ 下的等值线；越过它 $y_{s\ell\ell}$ 非微扰 | 给出"为什么画" |

---

## 7. 修改优先级

1. **P0｜中微子**（Major 3 全部 + Major 4.1）：正文零基础，必须新增方案、拟合与 LFV 检查。
2. **P0｜$S$ 的完整唯象学**（Major 1 全部）：$m_S$ 窗口（用式 30/31/34 + Table II + $(g-2)_\mu$ 的 $m_S$ 依赖）、Higgs 门户定量、$S$ 的约束小节。
3. **P1｜有限质量效应**（Major 4.2、4.3 + m2、m3）：动能混合显式化、$g_V$ 与矢量限对比、式 (16)/(27) 的说明。
4. **P1｜可行域与约束完备性**（Major 2、Major 4 前言 + m1、m6.x）。
5. **P2｜μ 子对撞机与措辞**（m5 + 全部术语替换）。

---

## 8. 回复结构与英文草稿

**结构**（每条六段）：① 感谢并复述问题；② 承认原稿哪里不清楚/缺失；③ 给出新增的物理内容；④ 说明对结论的影响；⑤ **给出坐标（节/式/图/表）**；⑥ 未纳入的给定量理由。

**语气规则**：用 "We have added / We now state / We agree"；说"不成立"时必须 "because … + 数字"；每条都给坐标。

**开头段（5 句）**
> We thank the referee for a careful report. We agree with the two central concerns: (i) the scalar $S$ cannot be decoupled (Eq. 34), and (ii) the minimal field content does not generate a non-trivial PMNS matrix. We have therefore added Sec. X on the scalar sector — its mass window from Eq. (34), the loop-induced Higgs mixing, and the bounds on $S$ (Table II, Eq. 31) — and Sec. Y on the neutrino sector, where we show the obstruction, identify its origin, and present a minimal extension that leaves the axial structure of the $A'$ couplings unchanged. All other points are addressed below in the order of the report.

**Major 1（要点版）**
> We agree that $S$ cannot be formally decoupled: Eq. (34), $m_S<\sqrt{2\lambda_S^{\max}}v_S$ with $v_S=m_{A'}/(2g_X)$, ties $m_S$ to $(m_{A'},g_X)$ … [填入窗口] … The Higgs–$S$ mixing is generated at one loop by $\tau$ (and $\mu$) loops; near $m_S\to m_h$ the two states become quasidegenerate and the mixing is maximal, excluding $|m_S-m_h|\lesssim[\cdots]$ GeV (Fig. Y).

**Major 3（要点版）**
> We thank the referee; the minimal field content indeed does not produce a non-trivial PMNS matrix. [列出电荷表与允许/禁戒条目] We find that [结构]，因此 $\theta_{12}=\theta_{13}=0$。We have therefore added [扩展方案]，which generates all entries and reproduces the observed angles [拟合]，and we verified that it does not modify the axial couplings of $\mu$ and $\tau$ … We have also checked the resulting $\mu\to3e$ and $\mu$–$e$ conversion limits.

**Major 4.2（要点版）**
> The parametric form is already given in Sec. II: a vector-like mass splitting generates $\epsilon\propto g_Yg_X\ln(M_E/M_{E'})$ [1]. In our benchmark $M_{E'}=M_E$, so the one-loop contribution vanishes identically; the residual is $O(\theta_R^2)$ [数值] and lies $N$ orders of magnitude below the experimental limit. The same holds for the $A'$–electron coupling induced by the small vector admixture.

---

## 9. 结论

这不是拒稿式意见（Recommendation：*"In its current form, the paper is not ready for publication… I strongly encourage the authors to further address the minor points."*），但有两条被审稿人点名"critical / 不能忽略"（中微子、标量）。修稿主线：

> 把论文从"轴矢量 $A'$ 有效理论的现象学"扩写为"$U_A(1)_{L_\mu-L_\tau}$ 轴矢量 UV 完成及其低能极限的完整分析"——明确区分纯 EFT 结果、UV 可实现区域（式 35 的条件切片）以及 $S$ 与有限质量效应。

动笔前必须完成两项内部工作：**① 中微子扇区的允许结构与修复方案；② $S$ 的质量窗口 + Higgs 门户混合的参数扫描。**

---

## 附录 A ｜稿件事实索引（可直接引用的坐标）

| 内容 | 坐标 | 要点 |
|---|---|---|
| 场内容与电荷表 | Table I | 轴向 $L_\mu-L_\tau$ 指派 |
| 质量基耦合 / 矢量混合 | 式 (16) | $g_V=g_X\sin^2\theta_R$、$g_A=-g_X\cos^2\theta_R$ |
| 轻子质量与混合角关系 | 式 (21) | $m_\tau\sim\theta_L\theta_RM_{E'}$ 等 |
| VL 退化 benchmark | 式 (22) | $M_{E'}=M_E>10$ TeV；控制动能混合 |
| 动能混合参数化 | §II（式 22 后）+ 文献 [1] | $\propto g_Yg_X\ln(M_E/M_{E'})$；退化时相消 |
| 混合角上限 | 式 (27) | $|\theta_{L,R}|,|\varphi_{L,R}|\lesssim10^{-2}$（LEP + VL 拟合） |
| 标量势与质量 | 式 (28)(29) | $m_S=\sqrt{2\lambda_S}v_S$，$y_{s\ell\ell}=m_\ell/v_S=2g_Xm_\ell/m_{A'}$ |
| 标量参数与扰动性 | 式 (30) | $\lambda_S=2g_X^2m_S^2/m_{A'}^2$ |
| 标量约束 → $g_X$ 限 | 式 (31) | $g_X\lesssim4.7\times10^{-3}y^{\lim}_{s\ell\ell}(m_S)m_{A'}/\text{MeV}$ |
| **$S$ 质量上限（扰动性）** | **式 (34)** | $m_S<\sqrt{2\lambda_S^{\max}}v_S$，$v_S=m_{A'}/(2g_X)$；例：$m_S=10$ GeV、$\lambda_S=4\pi$ ⇒ $v_S\gtrsim2$ GeV |
| 两参数切片 | 式 (35) | $\{m_{A'},g_X\}$，$v_S=m_{A'}/(2g_X)$ |
| 纯轴矢约化拉氏量 | 式 (36) | $g_V=0$、$g_A=g_X$；"pure-axial limit" 的显式声明处 |
| $S$ 的低质量约束 | **Table II** | $10^{-10}$ eV–$\mathcal{O}(10)$ MeV，$y^{\lim}$ 从 $10^{-20}$ 到 $4.2\times10^{-9}$ |
| $A'$ 的约束 | **Fig. 2** | PIENU、NA62、CCFR/CHARM II、$(g-2)_\mu$、NA64$\mu$、BaBar/Belle II/CMS；灰虚线 $v_S=2$ GeV |
| $(g-2)_\mu$ 的 $m_S$ 依赖 | §IVA + 式 (55)(57)(58) | 轴向为负；标量项 $+3g_X^2m_\mu^2/(4m_{A'}^2)$；$m_S\sim\mathcal{O}(m_\mu)$ 处相消；黑色等值线仅对 $m_S\gtrsim10$ GeV 有效 |
| $S$ 的 B 工厂区 | §II 末（p.12–13） | $0.04$–$6.5/7$ GeV（BaBar/Belle）、到 $9$–$10$ GeV（Belle II）；$AA$ 模式需 BR 重铸 |
| "parameter region of interest" | §III E | $A'$ 即时衰变的参数段 |
| 质量范围 | 摘要 | MeV–TeV |

---

## 附录 B ｜本次修订的完备性自检

| 报告条目 | 本版位置 | 原文 | 稿件现状 | 要做的工作 |
|---|---|---|---|---|
| ¶1、¶2、Merits | §1 | ✅ | ✅ | ✅（改写定位） |
| Major 前言 | §1 | ✅ | ✅ | ✅ |
| Major 1 前言 | §2.0 | ✅ | ✅ 式 (34) | ✅ |
| Major 1.1 | §2.1 | ✅ | ✅ | ✅ |
| Major 1.2 | §2.2 | ✅ | ✅ 式 (27)(31) + Table II + §IVA | ✅（四个输入全部给到） |
| Major 1.3 | §2.3 | ✅ | ⚠️ 稿件只有一句假设 | ✅ |
| Major 2 | §3 | ✅ | ✅ 式 (35) + §II 末 | ✅ |
| Major 3 前言 | §4.0 | ✅ | ⚠️ **正文零基础** | ✅ |
| Major 3.1 | §4.1 | ✅ | ⚠️ 同上 | ✅ |
| Major 3.2 | §4.2 | ✅ | ⚠️ 同上 | ✅ |
| Major 3 结尾 | §4.3 | ✅ | ⚠️ 同上 | ✅（含 LFV 新约束） |
| Major 4 前言 | §5.0 | ✅ | ✅ Table II / Fig. 2 / B 工厂段 | ✅（$S$ 独立小节） |
| Major 4.1 | §4.4 | ✅ | ⚠️ 同 Major 3 | ✅ |
| Major 4.2 | §5.1 | ✅ | ✅ 已有参数化 + 文献 | ✅ |
| Major 4.3 | §5.2 | ✅ | ✅ 式 (16) + (27) | ✅ |
| Major 4.4 | §5.3 | ✅ | ✅ Table II（对 $S$）；$A'$ 需分段 | ✅ |
| Minor 1 | m1 | ✅ | ✅ | ✅ |
| Minor 2 | m2 | ✅ | ✅ 式 (16)(36) | ✅（已能确定回答） |
| Minor 3 | m3 | ✅ | ✅ 式 (22)(27) | ✅ |
| Minor 4 | m4 | ✅ | ✅ 式 (27) 上一句 | ✅（不需新算） |
| Minor 5 | m5 | ✅ | ✅ 结论段 | ✅（补 Higgs factory） |
| Minor 6.1–6.6 | m6 | ✅ | ✅ 6.3/6.5/6.6 已有答案 | ✅ |
| Recommendation | §9 | ✅ | — | ✅ |

**仍需人工确认的（`[待目视核对]`）**：式 (30) 与式 (34) 的根号与 $\lambda_S^{\max}$ 数值、式 (12) 的显式耦合形式。文本抽取丢失了根号与希腊字母，上述结论由两处独立数值（正文例子 $v_S\gtrsim2.0$ GeV 与 Fig. 2 图注的 $v_S=2$ GeV 线）反推得到，引用前请对 PDF 原页确认。

**本版新增、原稿没有的工作项**：中微子修复与 LFV 限、$S$ 的独立约束小节、$(g-2)_\mu$ 的 $m_S$ 依赖性、动能混合残余项的显式估计、$g_V$ 与矢量限的对比表、Higgs factory 的 $S$ 探测段。
