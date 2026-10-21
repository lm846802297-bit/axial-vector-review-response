# DW13678 审稿意见分析与修改建议

> 针对 `dw13678_report_1_a.pdf` 的整理与分析。
> 审稿人总体判断：模型构造清楚、对模型构造社区有用，但当前论文不能直接达到 PRD 发表水平，必须实质性回应若干关键物理问题。

---

## 📖 标注约定（本版新增）

本文档已逐条标注每个观点**在审稿报告中的出处**。三种标记：

| 标记 | 含义 |
|---|---|
| 📎 **原文·位置** | 该观点直接来自审稿人原文，英文引号内为**逐字引用**，位置按报告的小节号给出 |
| 🖊 **非原文** | 该内容是整理者补的（推导、表格、公式、方案），**审稿人没有写**；括号内注明依据或相关原文 |
| ⚠️ **对不上** | 该内容与原文有出入（措辞、位置或结论不一致），需要修正 |

**报告结构编号**（本版统一使用）：
`¶1–¶2`＝开头两段；`Merits 1–3`；`Major 1 前言 + 1.1/1.2/1.3`；`Major 2`；`Major 3 前言 + 3.1/3.2 + 结尾`；`Major 4 前言 + 4.1–4.4`；`Minor 1–6`（6 内含 6.1–6.6）；`Recommendation`；`Statement`。

> 本版**只增加标注，未改动任何原有文字**。文末 §8 附总表。

---

## 1. 审稿人核心判断

审稿人认可以下几点：

- 模型是 anomaly-free、可重整化的；
- 额外 Abelian 规范场 $Z'$ 与 $\mu,\tau$ 的手征耦合构造清楚；
- 轴矢量极限（axial limit）下的现象学分析有参考价值；
- 论文整体叙事清楚，对 model building 社区有用。

📎 **原文｜¶1（首段）**
> "The authors construct an anomaly-free, renormalizable model in which an additional Abelian gauge field $A^{\prime}$ has chiral couplings to muons and taus. This model realizes a limit where the $A^{\prime}$ coupling to the $\mu$-$\tau$ current is axial. The second goal of the paper is to examine the phenomenology of this model in the axial limit."

📎 **原文｜Merits 第 1 条**（对应上面第 2 条 bullet）
> "The model construction section is written clearly. While the key ingredients for constructing such a model already exist in the literature, the authors have put these ingredients together."

📎 **原文｜Merits 第 2 条**（对应第 3 条 bullet）
> "The phenomenology is reasonably well motivated (up to some of the points below) and are straightforward to follow."

📎 **原文｜Merits 第 3 条**（对应第 4 条 bullet）
> "The paper is presented in a way that will make it useful for model builders to implement into their own models."

⚠️ **对不上**：第 4 条 bullet"论文整体叙事清楚"在报告中**没有对应的表扬**。原文 Merits 只表扬了构造清楚、现象学动机尚可、对 model builder 有用；"叙事清楚"是整理者的转述，建议删掉或改成原文措辞。（第 1 条 bullet"anomaly-free、可重整化"来自 ¶1；"手征耦合构造清楚"来自 Merits 1。）

但他认为论文存在一个根本性叙事问题：

> 前半部分构造的是一个具体的 UV 完备模型；后半部分却主要研究一个只含轴矢量 $Z'$ 的两参数有效理论（EFT）。

⚠️ **非原文（整理者概括）**：上面这个块引用**不是**审稿人原句，而是整理者的总结。原文对应两处：

📎 **原文｜¶2**
> "The paper presents results that are useful for the model building community. However, I have some significant reservations about key points that either should be included or otherwise justified in being excluded from the manuscript. These are explained below. Revisions for these major points (even if only to clarify why they are not issues) are required before the paper is at the level of a PRD manuscript."

📎 **原文｜Major 1 前言（首句）**
> "The second half of the paper reviews a set of experimental bounds on only an effective theory of the $A^{\prime}$ axially coupled to the $L_{\mu-\tau}$ current. This leaves a major gap between these two parts of the paper ..."

在 UV 模型中，标量 $\phi$、矢量样轻子（vectorlike leptons）、有限质量效应、动能混合（kinetic mixing）、中微子质量结构都不是可以随意删去的。如果这些效应会改变实验约束，那么只研究“纯轴矢量 EFT”就不能代表前面构造的 UV 模型。

🖊 **非原文（整理者推断）**：这一段的"清单"是整理者把四处原文合并出来的，依据：
- 标量 $\phi$ → 📎 Major 1 前言 + 1.3 结尾（"it cannot formally decouple"）
- 矢量样轻子 / 有限质量效应 → 📎 Major 4.2、4.3
- 动能混合 → 📎 Major 4.2
- 中微子质量结构 → 📎 Major 3.1、3.2、4.1

---

## 2. 审稿人认为必须实质性回应的重大问题

### 2.1 标量 $\phi$ 不能只在模型构造中出现

这是审稿意见中最核心的第一点。

🖊 **非原文（整理者判断）**，但依据充分：📎 **Recommendation** 第 2 段——
> "I also feel that dismissing the physics of the scalar $S$ ignores the actual predictions of the UV model—otherwise the authors are simply justifying the phenomenology of the effective axial theory."

模型为了自发破缺额外 $U(1)$，需要标量 $\phi$。审稿人认为，根据论文式 (34)，$\phi$ 的质量 $m_\phi$ 与 $Z'$ 质量 $m_{Z'}$、规范耦合 $g'$ 以及标量自耦合 $\lambda_\phi$ 之间存在关系，因此 $\phi$ 并不是可以任意推到无穷重的附属粒子。

📎 **原文｜Major 1 前言**
> "... the authors show that their UV theory requires a scalar $S$ that cannot be arbitrarily decoupled from the low-energy dynamics, e.g. from (34) which states that $m_{S}^{2}<4\pi(m_{A^{\prime}}/2g_{X})^{2}$."

⚠️ **对不上**：原文引用的是**方根形式** $m_{S}^{2}<4\pi(m_{A^{\prime}}/2g_{X})^{2}$，整理者写的是"$m_\phi$ 与 $m_{Z'}$、$g'$、$\lambda_\phi$ 之间存在关系"——审稿人**没有提 $\lambda_\phi$**，$\lambda$ 是在 **Major 1.2** 才出现的（"perturbativity limits on $\lambda$"）。回复时必须原样引用式 (34)。

基本逻辑是：

$$
m_{Z'} \sim g' q_\phi v_\phi,
$$

$$
m_\phi^2 \sim 2\lambda_\phi v_\phi^2,
$$

于是

$$
\frac{m_\phi}{m_{Z'}}
\sim
\frac{\sqrt{2\lambda_\phi}}{g' q_\phi}.
$$

如果要求 $\lambda_\phi$ 和 $g'$ 保持微扰性（perturbativity），那么 $m_\phi/m_{Z'}$ 不能无限大。因此，给定 $m_{Z'}$ 和 $g'$，$\phi$ 会落在某个有限质量范围内。

🖊 **非原文（整理者推导）**：以上三段公式与推理**全部是整理者补写的**，审稿人只给了式 (34) 的方根形式。用途：把审稿人的不等式翻译成我们自己记号的推导链。⚠️ 定稿前必须核对归一化（$m_{A'}=2g_Xv_S$ 的因子 2、$q_\phi$ 是否显式出现），否则与稿件式 (34) 对不上。

审稿人因此提出三个具体要求：

#### （1）$\phi$ 应成为论文的主张之一

如果 $\phi$ 在现象学相关尺度上不可回避，那么论文应强调：

> 目前已知轴矢量 $Z'$ 规范玻色子的 UV 完备模型中，必然伴随一个标量 $\phi$，且其质量范围可以被对撞机检验。

📎 **原文｜Major 1.1（逐字）**
> "It is thus an odd choice to exclude the scalar from the phenomenology of the effective theory: if the $S$ is unavoidable at phenomenologically relevant scales, shouldn't one of the main points of the paper be that the only known UV completion of an axial $L_{\mu-\tau}$ gauge boson has a prediction for a scalar particle in a mass range that can be probed by colliders?"

⚠️ **对不上**：上面那个中文块引用把原文的反问**改写成了陈述句**，还丢掉了 "the only known" 这个限定。回复里应保留反问语气，并注意 "only known" 是需要文献支撑的强主张。

#### （2）给出 $m_\phi$ 的允许范围

需要结合以下条件给出 $m_\phi$ 范围：

- 微扰性上限；
- $g'$ 的允许范围；
- $v_\phi$ 的合理范围；
- 其它标量耦合的合理性；
- 对 $Z'$ 与 $\phi$ 的实验约束。

📎 **原文｜Major 1.2（逐字）**
> "What is the range of phenomenologically allowed $S$ mass including perturbativity limits on $\lambda$ and a motivated range of $m_{A^{\prime}}$ and $g_{X}$. For example: perhaps the authors imagine a range of $m_{A^{\prime}}$ below some benchmark mass where certain experimental constraints on $g_{X}$ become very strong. Then with that set of constraints (which should be stated clearly, see minor point #1 below), one may give a range of $m_S$ and comment on the experimental constraints."

⚠️ **对不上 / 遗漏**：五个 bullet 里只有前两条半来自原文。原文的**构造路线**没被写进本文档：① 先取一个 **benchmark 质量以下的 $m_{A'}$ 区间**（该区间内 $g_X$ 的某些实验约束变得很强）→ ② 用那组约束（明确写出，见 Minor 1）→ ③ 由此给出 $m_S$ 区间并讨论其实验约束。另外原文明确写了 "see minor point #1 below"，本节的 bullet 列表没有交叉引用。

#### （3）Higgs 门户混合必须定量分析

审稿人特别质疑论文在式 (34) 附近“假设 Higgs-portal mixing 可以忽略”的做法。

📎 **原文｜Major 1.3（首句，逐字）**
> "Above (34): the authors "assume negligible Higgs-portal mixing." Is this interaction not generated at loop level? It seems that $S$-$h$ mixing cannot be avoided due to $\mu$ and $\tau$ loops. In turn, this seems like it would lead to strong experimental bounds on the UV completion."

他指出，即使树级令

$$
\lambda_{H\phi} = 0,
$$

也可能被带有 Higgs 耦合和 $U(1)'$ 耦合的矢量样轻子圈图重新生成：

$$
\delta\lambda_{H\phi}
\sim
\frac{1}{16\pi^2}
\left(\text{相关 Yukawa 和规范耦合的组合}\right)
\log\frac{\Lambda}{\mu}.
$$

（括号内的「相关 Yukawa 和规范耦合的组合」指参与圈图的 Yukawa 耦合与规范耦合的乘积组合。）

⚠️ **对不上（重要）**：**审稿人没有给任何公式**，也没有说圈图来自"矢量样轻子 + 规范耦合"。原文只说了两件事：① 圈图必然产生混合；② 来源是 **$\mu$ 和 $\tau$ 圈**。上面这个 $\delta\lambda_{H\phi}$ 模板与"括号内解释"都是整理者自补的，而且**与已完成的一圈实算结论相反**（实算：$\delta m^2_{Sh}=-(y_1y_2)^2vv_S/(8\pi^2)\propto M^2$，**无对数增强**、$\tau$ 圈主导，见 `Higgs_portal_完整推导与验证-hy4.md`）。回复时必须换成实算结果。

物理 Higgs 混合角可估计为：

$$
\theta_{h\phi}
\simeq
\frac{\lambda_{H\phi} v v_\phi}
{m_\phi^2 - m_h^2}.
$$

因此在

$$
m_\phi^2 \simeq m_h^2
$$

附近可能出现共振增强（resonance enhancement）。

🖊 **非原文（整理者推导）**：混合角公式是整理者补的；原文只说：（📎 Major 1.3）"In fact, once there is mixing, is there not a resonance where the mixing becomes large as $m_{S}\rightarrow m_{h}$?"（注意：原文是**反问**，要的是"你承认有这个共振吗"）。⚠️ 该公式缺因子 2，规范写法为 $\sin2\theta\simeq2\lambda_{HS}vv_S/(m_h^2-m_S^2)$。

需要检查：

- 混合角大小；
- Higgs signal strength；
- exotic Higgs decays；
- 标量直接产生；
- 长寿命粒子搜索；
- 电弱精确测量。

⚠️ **部分对不上**：六项清单里只有前两项有原文依据——
📎 **Major 1.3**："It would be useful to quantify the size of this mixing over the allowed range of $m_{S}$. Existing Higgs measurements may set the strongest bounds on the UV completion."
其余四项（exotic Higgs decays、直接产生、长寿命、电弱精确测量）**原文全部没提**，是整理者补的。补得对，但回复时不能写成"审稿人要求了这六项"。

建议至少分析以下衰变道：

$$
\phi \to Z'Z',
$$

以及通过 Higgs mixing 后可能出现的：

$$
\phi \to f\bar f,\qquad
\phi \to WW,\qquad
\phi \to ZZ,\qquad
\phi \to hh.
$$

如果 $m_\phi \gt  2m_{Z'}$，$\phi\to Z'Z'$ 往往会成为重要衰变道；如果 $m_\phi \lt  2m_{Z'}$，则可能主要通过 Higgs mixing 或圈图衰变。不同质量区的实验约束和寿命差异很大，不能笼统地说“标量可以忽略”。

⚠️ **非原文（完全新增）**：审稿人**没有提到任何衰变道**。整段（$\phi\to Z'Z'/f\bar f/WW/ZZ/hh$ 与质量阈值讨论）都是整理者补的物理内容。这是补强，但**在回复中不能声称"应审稿人要求"**。最后半句"不能笼统地说标量可以忽略"则确实呼应 📎 Major 1.3 结尾。

📎 **原文｜Major 1.3（结尾，务必引用）**
> "If these bounds are obviously negligible (though again, I expect this to be strongly constrained as $m_{S}\rightarrow m_{h}$), then the authors should present this as the justification for ignoring $m_{S}$ in the low-energy theory. (Though I am still skepticial that the $m_{S}$ can be ignored since it cannot formally decouple.)"

---

### 2.2 中微子振荡是否相容（可能是致命问题）

审稿人的第二个核心关切是：模型是否能与中微子振荡实验相容。

🖊 **非原文（整理者判断）**，依据：📎 **Recommendation**——
> "However, the question of whether this class of model can be consistent with neutrino oscillations is critical."

他的担心是：如果模型只对不同代轻子施加特定 $U(1)'$ 电荷，则 Weinberg 算符、带电轻子 Yukawa 矩阵和中微子质量矩阵可能被同时限制为近似对角形式。这样会得到

$$
U_{\rm PMNS} \simeq \mathbf 1,
$$

与实验观察到的非平凡 PMNS 混合不一致。

📎 **原文｜Major 3 前言 + 3.1（逐字）**
> "The Standard Model is defined with only left-handed neutrinos because of the possibility that neutrinos are their own antiparticle. In such a case neutrino masses are generated through, e.g. through the Weinberg operator."
> "In this model, $U_{A}(1)_{L_{\mu-\tau}}$ invariance allows Weinberg operators for each generation. However, it appears that both the Yukawa matrices and neutrino masses must be aligned and therefore a non-trivial PMNS matrix does not appear to be possible."

📎 **原文｜Major 4.1**（"unit PMNS" 这个说法的出处）
> "It appears that this model predicts a unit PMNS matrix, which is inconsistent with neutrino oscillations."

⚠️ **对不上（措辞）**：原文说的是"Yukawa 矩阵与中微子质量矩阵**必须对齐**（aligned）"；"近似对角形式"是整理者的弱化改写。原文的物理更强：对齐 ⇒ 可同时对角化 ⇒ PMNS 无非平凡来源。"$\simeq\mathbf 1$"可以用，但别把"对齐"这个关键机制改掉。

这需要从模型的电荷表和 Yukawa 结构重新检查，不能只补一个引用。

🖊 **非原文（整理者判断）**：原文没有这句话；它对应 📎 Major 3 结尾"应给出解法或引用文献"以及 📎 Recommendation"必须解决"，属于整理者的执行要求。

#### 需要检查的问题

1. **Weinberg 算符是否允许代际混合？**

   检查

   $$
\frac{c_{ij}}{\Lambda}
   (\overline{L_i^c}\tilde H^*)
   (L_j\tilde H^*)
$$

   在 $U(1)'$ 下的电荷是否为零。

   如果只有 $i=j$ 的算符允许，则中微子质量矩阵在规范基底中是对角的。如果带电轻子 Yukawa 矩阵也被迫对角，则 PMNS 矩阵没有来源。

📎 **原文｜Major 3.1**（对上面三段的对应句）
> "$U_{A}(1)_{L_{\mu-\tau}}$ invariance allows Weinberg operators for each generation. However, it appears that both the Yukawa matrices and neutrino masses must be aligned and therefore a non-trivial PMNS matrix does not appear to be possible."

🖊 **非原文（整理者展开）**：算符显式、电荷条件、"只有 $i=j$ 允许则矩阵对角"这三步推理是整理者补的（原文只给结论，没给算符形式）。

2. **右手中微子方案是否可行？**

   如果加入右手中微子 $N_R$，需要检查：

   $$
\overline{L_i}\tilde H N_{Rj}
$$

   是否允许非对角项，以及 $N_R$ 是否引入新的规范反常。

   审稿人担心：右手中微子带有 $U(1)'$ 电荷后，可能迫使第二、三代以矢量样组合出现，并且代际混合仍受规范对称性限制。

📎 **原文｜Major 3.2（逐字）**
> "Perhaps a full model would require right-handed neutrinos. These would now be charged under $U_{A}(1)_{L_{\mu-\tau}}$, which likely means the second and third generation must appear as vectorlike combinations. However, it seems to me that mixing between generations is prohibited by $U_{A}(1)_{L_{\mu-\tau}}$."

⚠️ **对不上（偏离原文重点）**：整理者问的是"是否允许非对角项 + 是否引入新反常"；原文**没有提反常**，他提的是"二三代必须成矢量样组合"与"代际混合被禁"。这两条断言需要正面核验（已核：严格成立，见 `中微子扇区电荷分析-hy4.md` §3.5）。

3. **是否可以用额外标量产生混合？**

   一种可能的修正是加入带有适当 $U(1)'$ 电荷的标量，通过

   $$
\overline{L_i}\tilde H N_{Rj},
   \qquad
   \overline{N_{Ri}^c}N_{Rj}\phi_k
$$

   生成非对角的 Dirac 或 Majorana 质量矩阵。

   但会带来新问题：

   - 需要多少个额外标量？
   - 是否增加规范反常？
   - 是否破坏模型原先的最小性？
   - 是否产生新的 Goldstone 或轻标量？
   - 是否改变 $\phi$ 的唯象学？
   - 是否仍保持原来的轴矢量 $Z'$ 耦合结构？

⚠️ **非原文（完全新增）**：审稿人**没有提出"加额外标量"这条路**。他的原话只有：（📎 Major 3 结尾）"If there is a simple solution, the authors should include it. If there is a known less-simple solution in the literature, the authors should cite this."
所以：这条路是整理者/我们自己找出来的解法（事后证明方向正确，最终解就是加奇电荷标量 $\sigma$）。回复时应表述为"我们研究了额外标量方案"，而非"应审稿人建议"。

#### 三种可行路线

**路线 A：证明最小模型本身可以产生 PMNS 混合。**

这是最理想的情况，但必须写出明确的非对角质量项和电荷验证。

**路线 B：增加最小的中微子扩展。**

例如加入右手中微子和必要额外标量，并重新验证：

- 规范反常消除；
- Yukawa 项；
- 质量矩阵；
- PMNS 混合；
- 对 $Z'$、$\phi$ 和新粒子的约束。

**路线 C：收缩论文的模型主张。**

如果不想扩展模型，应坦率说明：

- 本文的 UV 完备性只针对规范扇区和带电轻子扇区；
- 中微子质量机制不在本文范围内；
- 最小模型本身不产生完整 PMNS 结构；
- 可以通过额外中微子扇区扩展，且该扩展在给定条件下不改变本文关注的低能带电轻子耦合。

不过审稿人已明确说，中微子振荡相容性是 “critical”。因此路线 C 只有在能证明额外中微子扇区确实可解耦、且不影响核心结论时才稳妥。

🖊 **非原文（整理者行动方案）**：三条路线都是整理者设计的。与原文的对应关系：
- 路线 A ← 📎 Major 3 结尾 "If there is a simple solution, the authors should include it."
- 路线 B ← 同句 "If there is a known less-simple solution in the literature, the authors should cite this."
- 路线 C ← 无对应（是我们的退路），唯一相关的约束是 📎 Recommendation 的 "critical"。

📎 **原文｜Major 3 结尾（逐字，回复时必须复述）**
> "Thus it is not obvious to me how neutrino oscillations can be included in this framework. If there is a simple solution, the authors should include it. If there is a known less-simple solution in the literature, the authors should cite this. Otherwise, at best this will be a confusing point. At worst, it would make the construction inconsistent with neutrino oscillation experiments."

📎 **原文｜Recommendation（"critical" 的出处）**
> "However, the question of whether this class of model can be consistent with neutrino oscillations is critical."

---

### 2.3 有效理论参数范围需要明确

审稿人认为 Fig. 2 的关键问题是：读者不知道为什么选取这些 $m_{Z'}$ 和耦合范围，也不知道范围外的点是：

- 理论上不允许；
- 实验上已排除；
- 微扰性不成立；
- 还是仅仅没有研究。

📎 **原文｜Major 2（逐字）**
> "To further aid in the comparison between the UV theory and the two-parameter low-energy theory, it would be useful to explicitly state in one place (perhaps in a table or a figure like Fig. 2) the range of the effective model parameters that are feasible. The main phenomenological results are in Fig. 2, but it was not clear why this range of couplings and $A^{\prime}$ masses were chosen: are values outside this range not allowed? What, if anything, does the perturbativity of the UV theory impose on the effective parameters?"

🖊 **非原文（整理者展开）**：四个"还是"（理论不允许 / 已排除 / 非微扰 / 没研究）是整理者把原文的 "are values outside this range not allowed?" 展开成选项，方便我们逐项回答。原文只问了一句。

建议新增一张总览表，例如：

| 参数 | 理论范围 | UV 模型可实现范围 | 实验允许范围 | 本文展示范围 |
|---|---:|---:|---:|---:|
| $m_{Z'}$ | ... | ... | ... | ... |
| $g'$ | ... | ... | ... | ... |
| $m_\phi$ | ... | ... | ... | ... |
| 矢量样轻子质量 | ... | ... | ... | ... |
| 轴矢量耦合 $g_A$ | ... | ... | ... | ... |
| 矢量耦合 $g_V$ | ... | ... | ... | ... |

🖊 **非原文（整理者设计）**：原文只建议"a table or a figure like Fig. 2"（📎 Major 2），表格的列与行都是整理者定的。

同时应写清楚 UV 参数如何映射到 EFT 参数，例如：

$$
g_A = f(g',\theta_L,\theta_R),
\qquad
g_V = f(g',\theta_L,\theta_R),
$$

并明确纯轴矢量极限对应什么条件，例如：

$$
g_V = 0.
$$

不能在公式中隐含定义，应在正文直接写出：

> In this work, the pure-axial limit is defined by $g_V=0$, which corresponds to [具体的混合角关系].

🖊 **非原文（整理者补充）**：以上三块都是整理者加的。原文**没有要求**映射式，也没要求定义纯轴矢极限——那件事在 **Minor 2** 里（"Equation (12) ... It is here that the pure axial coupling limit is defined? i.e. $\theta_{\mu R}\rightarrow 0$?"）。
⚠️ **对不上**：整理者建议的定义是 $g_V=0$，而**原文建议的定义是 $\theta_{\mu R}\to0$**。两者必须核对是否等价（已推出 $g_V/g_A\simeq\theta_{\mu R}^2$，方向一致，但要按稿件式 (12) 确认），回复时不能把审稿人提的条件换成另一个而不作说明。

还应说明：

- $g'$ 的微扰性上限；
- 标量自耦合 $\lambda_\phi$ 的微扰性上限；
- 矢量样 Yukawa 耦合的微扰性上限；
- RGE 运行到什么尺度；
- EFT 参数是否能由这些 UV 参数同时实现。

📎 **原文｜Major 2（末句，逐字）**
> "What, if anything, does the perturbativity of the UV theory impose on the effective parameters?"

📎 **原文｜Major 1.2**（$\lambda$ 的微扰性上限出处）
> "What is the range of phenomenologically allowed $S$ mass including perturbativity limits on $\lambda$ ..."

⚠️ **部分对不上**：前四条 bullet 中，$g'$ 与 $\lambda$ 的上限有原文依据；"矢量样 Yukawa 的微扰性上限"与"RGE 运行尺度"**原文没提**，是整理者补的（补得合理，但归类到 Major 2 时应说明这是我们的补充）。

---

### 2.4 动能混合必须定量估计

审稿人认可轴矢量极限中动能混合可能趋于零，但认为 UV 模型只有在矢量样轻子质量趋于无穷时才达到纯轴矢量极限。

📎 **原文｜Major 4.2（逐字）**
> "There is no quantitative estimate of the amount of kinetic mixing generated with the 'benchmark' choices of $\theta \leq 10^{-2}$. The authors make the insightful point that kinetic mixing goes to zero in the axial limit, but because this limit is tied to the size of the mixing (the mass of the vectorlike leptons), for the above benchmark there is non-zero kinetic mixing."

因此在有限矢量样轻子质量下：

$$
\epsilon_{\rm kin}\neq 0.
$$

这会诱导 $Z'$ 对电子、夸克或 SM 电磁流的有效耦合，从而改变很多实验约束。

🖊 **非原文（整理者推断）**：$\epsilon_{\rm kin}\neq0$ 与"诱导对电子、夸克、电磁流的耦合"是整理者的话。原文只说"benchmark 下动能混合不为零"并要求估量；"诱导 SM 电磁流耦合"这一物理机制原文没有明说。

建议至少给出参数估计：

$$
\epsilon(\mu)
\sim
\frac{g_Y g'}{16\pi^2}
\sum_f Y_f Q'_f
\log\frac{M_f^2}{\mu^2}.
$$

如果一圈对数项因电荷迹抵消，则需说明首个非零贡献出现在哪一阶，或来自质量分裂：

$$
\epsilon
\sim
\frac{g_Y g'}{16\pi^2}
\log\frac{M_1}{M_2}.
$$

然后在 benchmark 下给出数值，例如：

$$
\epsilon \sim 10^{-n},
$$

并与对应实验约束比较。

⚠️ **非原文（整理者补公式）**：这两个公式与"电荷迹抵消"的讨论**原文完全没有**。原文只给出方向：
📎 **Major 4.2**："It would be useful to have parametric estimates of the amount of kinetic mixing one expects so that readers may compare to experimental bounds. One could invoke parametric expressions in the literature for the relevant loop diagrams."
→ 注意最后一句：审稿人**建议引用文献里的参数化表达式**，本文档没有给任何文献，这是缺口。
⚠️ 另注：数值不能写成 $10^{-n}$ 的示意——已由独立分析定为 $\epsilon\sim\frac{g_Xg_Y}{16\pi^2}Q_\ell\ln(m_\tau/m_\mu)\sim6\times10^{-4}(g_X/0.1)$，且**不随 $\theta_{\mu R}\to0$ 消失**。

审稿人特别担心：某些实验对小的矢量耦合比对轴矢量耦合敏感得多。因此不能只说“矢量耦合很小”，而要比较：

$$
g_V^{\rm induced}
$$

与实验对 $g_V$ 的上限。

⚠️ **归类错位**：这一段的原文其实属于 **Major 4.3**，不是 4.2——
📎 **原文｜Major 4.3**
> "The importance of this point is as follows: often bounds are sensitive to the chiral structure of interactions. Sometimes a vector interaction is more tightly constrained than its axial counterpart. Since the authors focus on the phenomenology in the axial limit, one wants to make sure that any small-but-finite vector interaction isn't significant because the constraints on the coupling are orders-of-magnitude larger than the axial coupling."
→ 建议在本文档中把这段移到 §2.5，避免回复时把 4.2 与 4.3 混为一谈。

---

### 2.5 有限矢量样轻子质量会带来小矢量耦合

论文现象学部分使用纯轴矢量极限，但 UV 模型只有在矢量样轻子质量无限大时才严格达到这个极限。

因此需要说明有限质量时：

$$
g_V \neq 0.
$$

📎 **原文｜Major 4.3（逐字）**
> "Another way of reframing the above point: the bounds presented are in the pure axial limit. Since the authors present a UV model that only realizes the axial coupling in a decoupling limit, it would be useful to comment on possible experimental bounds on the small vector-like coupling in a model with non-infinite vectorlike fermion masses. If these bounds are always small compared to the axial bounds, this should be stated and justified."

建议做两件事：

1. 给出 $g_V/g_A$ 随矢量样轻子质量 $M_L$ 或混合角变化的关系；
2. 将 $g_V$ 代入最敏感的实验约束，检查是否改变 Fig. 2。

可以增加一张图：

$$
\frac{g_V}{g_A}
\quad \text{vs.}\quad
M_L,
$$

并叠加：

- 电子束流实验；
- 中微子散射；
- 稀有衰变；
- $e^+e^-$ 实验；
- 可能的 beam-dump 实验；
- 电弱精确测量。

🖊 **非原文（整理者设计）**：这两件事与那张图、以及六个实验的清单都是整理者安排的。原文只说"comment on possible experimental bounds"和"If these bounds are always small compared to the axial bounds, this should be stated and justified"。清单本身没问题，但不要写成"审稿人列了这六个实验"。

如果有限 $g_V$ 在整个允许参数空间都弱于轴矢量约束，应给出定量解释；如果某些区域矢量约束更强，需要重新画排除区域。

📎 **原文｜Major 4.3（对应的两句）**
> "If these bounds are always small compared to the axial bounds, this should be stated and justified."
> "Sometimes a vector interaction is more tightly constrained than its axial counterpart."

🖊 **非原文**："重新画排除区域"是整理者推出的行动项（原文未明说必须重画，但语义上蕴含）。

---

### 2.6 实验约束清单需要重新组织

审稿人并不是要求重做所有实验分析，而是要求明确 Table II 和正文中实验约束的边界。

“representative bounds” 措辞太模糊。建议改成以下之一：

- “the leading constraints considered in this work”；
- “the constraints that dominate in the mass range $m_{Z'}\in[\cdots]$”；
- “a non-exhaustive selection of constraints”；
- “constraints included in our recast”。

⚠️ **归类错位（本节标题与内容不符）**：本节写的是 **Minor 6.2** 的措辞问题，但原文中"约束是否完整"是 **Major 4**。

📎 **原文｜Major 4 前言（逐字）**
> "Is this the full set of experimental constraints? The second half of the manuscript presents a set of experimental bounds on the two-parameter effective $A^{\prime}$ model. It is not obvious if this is the full set of constraints on the model. (See also point #1 above: I would have liked to see a section discussing the bounds on the $S$ within this model since it cannot be decoupled.) The following experimental bounds seem like they could be relevant. It would be helpful to either include them or justify why they are subdominant to the experiments presented."

📎 **原文｜Minor 6.2（"representative" 的出处）**
> "At the bottom of page 11, when referring to Table II, the authors write "representative bounds." What does representative mean? Does it mean these are the most stringent bounds? Are these "some" bounds? Is the list 'complete' in any sense?"

🖊 **非原文**：四个候选替换措辞是整理者提供的（原文只是问"representative 是什么意思"）。

同时应增加一段说明未纳入约束及原因，例如：

| 约束 | 是否纳入 | 原因 |
|---|---|---|
| 中微子振荡 | 必须处理 | 关系到模型一致性 |
| 动能混合 | 必须估计 | 可能诱导 SM 带电粒子耦合 |
| $\phi$ 搜索 | 必须新增 | $\phi$ 由 UV 模型不可避免地产生 |
| 有限 $g_V$ | 必须讨论 | 纯轴矢量是极限而非一般点 |
| 恒星冷却 | 需要判断 | 轻 $Z'$/轻 $\phi$ 区域可能重要 |
| Higgs 数据 | 必须检查 | Higgs 门户混合可能增强 |
| 矢量样轻子直接搜索 | 建议纳入 | 决定混合角和 $g_V$ 的上限 |

🖊 **非原文（整理者设计）**：原文只要求"include them or justify why they are subdominant"（📎 Major 4 前言），表格是整理者列的。
⚠️ **遗漏（原文点名）**：原文明确要一节讨论 **$S$ 的约束**（"I would have liked to see a section discussing the bounds on the $S$ within this model since it cannot be decoupled"）。本表里 $\phi$ 搜索只写了一行"必须新增"，没有列具体实验。
⚠️ **遗漏（我们自己的）**：$(g-2)_\mu$ 与轻子味破坏（$\mu\to3e$、$\mu$–$e$ 转换）都不在表内；后者在采用奇电荷标量修复中微子后是**必然产生**的新约束。

关于恒星冷却，审稿人提到 arXiv:2511.09619。需要特别确认该文献编号是否正确，并确认其适用范围：

- $m_{Z'}$ 是否足够轻；
- $m_\phi$ 是否足够轻；
- 粒子在恒星内部的产生率；
- 是否会被介质效应、屏蔽或衰变抑制；
- 轴矢量耦合是否改变标准能量损失分析。

📎 **原文｜Major 4.4（逐字）**
> "Are stellar cooling bounds not relevant? See e.g. 2511.09619 for a recent paper on this. If they are not, then this is certainly worth justifying."

🖊 **非原文（整理者展开）**：五个 bullet 是整理者列的检查项，原文只有"要么纳入、要么给出理由"这一句要求。

如果约束不适用，应给出质量阈值、耦合阈值和原因，而不是一句“可以忽略”。

🖊 **非原文（整理者要求）**：对应我们的回复原则（审稿人没写，但符合其 "worth justifying" 的意图）。

---

### 2.7 矢量样轻子质量下限要明确

审稿人指出，混合角大致随矢量样轻子质量反比：

$$
\theta \sim \frac{y v}{M_{\rm VL}}.
$$

📎 **原文｜Minor 3（首句，逐字）**
> "Because the mixing angles scale inversely with the vectorlike lepton masses, it would be helpful to present lower limits on these masses."

⚠️ **对不上（位置）**：这条是 **Minor 3**，不是 major point。本文档把 Minor 3、Minor 4 都并进了 §2.7，导致 major/minor 混在一起——回复时按 minor 回，不要按 major 回。
🖊 公式 $\theta\sim yv/M_{\rm VL}$ 是整理者补的（原文只有文字描述）。

因此矢量样轻子直接搜索给出的 $M_{\rm VL}$ 下限，会转化为：

- 混合角上限；
- 有效矢量耦合上限；
- 轴矢量近似的误差范围；
- 动能混合大小。

🖊 **非原文（整理者推断）**：四条后果是整理者展开的。原文只说"这随之给出 $\theta_{(\mu,\tau)R}$ 的上限，进而给出 $A'$ 与 $L_{\mu-\tau}$ 的矢量耦合上限"（📎 Minor 3）——即只有前两条有依据；后两条（轴矢量近似误差、动能混合大小）是我们补的。

建议加入：

$$
M_{\rm VL} \gt  M_{\rm min},
$$

并说明来源：

- LHC 直接搜索；
- LEP；
- 电弱精确测量；
- 轻子味约束；
- 组合限制。

🖊 **非原文**：$M_{\rm VL}>M_{\min}$ 的形式与五个来源清单都是整理者列的；原文只说"present lower limits on these masses"。

然后与式 (27) 比较。审稿人对 “conservative benchmark” 的疑问也来自这里：式 (27) 到底是：

- 实验上限；
- 理论上限；
- 方便计算的 benchmark；
- 还是保守选取的允许值？

📎 **原文｜Minor 3（末句，逐字）**
> "How do these bounds compare with the $\theta_{(\mu,\tau)(L,R)}$ bounds in equation (27)?"

📎 **原文｜Minor 4（逐字）**
> "Equation (27) is presented as a "conservative benchmark." What does this mean? A benchmark point would be a choice of this mixing angles. A constraint is an upper bound. Eq. (27) is written as an upper bound, but is described as a benchmark. This is not simply semantic: readers would want to understand if $10^{-2}$ is an experimental upper limit or simply a convenient choice."

🖊 **非原文**：四个候选答案（实验上限／理论上限／方便的计算值／保守允许值）是整理者列的。

建议把 “conservative benchmark” 改成明确说法，例如：

> We choose the benchmark $\theta_L=\cdots$, $\theta_R=\cdots$ for illustration. This is not an experimental upper limit. The current direct-search and precision constraints allow the broader range $\cdots$.

或者：

> Equation (27) is an upper bound derived from ..., rather than a benchmark point.

两者必须区分。

🖊 **非原文（整理者草稿）**：两句英文替换示例是整理者写的。

---

## 3. 次要问题（Minor Points）

这些问题单独看较小，但共同说明论文参数空间叙事不够清楚。

🖊 **非原文（整理者概括）**：原文 Minor 小节开头只写了（📎 **Minor 前言**）："The following points could be improved for clarity." —— "共同说明参数空间叙事不够清楚"是整理者的总结。

### 3.1 参数范围

需要明确 $m_{Z'}$ 与耦合的目标范围。例如：

- 哪些质量区实验或理论限制较弱？
- 是否有一个 “light $Z'$” 场景？
- 如果提出 “light”，必须定义参考质量尺度，例如 $m_{Z'}\ll m_Z$ 或 $m_{Z'}\lt \cdots$。

📎 **原文｜Minor 1（逐字）**
> "The general cosntruction of the model is clearly written, but it is difficult for the reader to envision the mass and coupling range that the authors are targeting. It would be very helpful if the authors decide on a range of $m_{A^{\prime}}$ and $g_{X}$ of interest. For example: is there a range of masses where experimental or theoretical limits are less constraining? Is there some set of phenomenology that the authors week to realize with a "light" $A'$? If so, they should define "light." (see, e.g. the first word of the introduction, which is not defined with respect to any reference mass scale.)"

⚠️ **对不上（漏项）**：原文最后半句点名"引言的第一个词没有参考质量尺度"——本文档这里没有单列（在 §3.6 才出现）。另外原文举例的 "$m_{Z'}\ll m_Z$" 是**整理者补的**，原文没给具体形式。

### 3.2 纯轴矢量极限的定义

审稿人认为式 (12) 中给出的 $Z'$ 在质量基底下的耦合，可能就是 “pure axial limit” 的定义位置。

建议在式 (12) 之后直接定义：

$$
g_V=0
$$

或等价的左右手混合角关系，并说明 “pure axial limit” 这一术语的具体含义。

📎 **原文｜Minor 2（逐字）**
> "Equation (12) gives the coupling of the $A^{\prime}$ to the mass-basis fields. It is here that the pure axial coupling limit is defined? i.e. $\theta_{\mu R}\rightarrow 0$? If that is the case, it would help to define this as the pure-axial limit, a phrase which is used below (36) but not otherwise quantified."

⚠️ **对不上（关键）**：原文给的定义条件是 **$\theta_{\mu R}\rightarrow0$**，本文档换成了 **$g_V=0$** 且只加了一句"或等价的左右手混合角关系"。回复时必须正面回答"是不是 $\theta_{\mu R}\to0$"，并给出关系式（已有 $g_V/g_A\simeq\theta_{\mu R}^2$）。另外原文提到该术语"used below (36)"，本文档未记这一坐标，回复时应写明。

### 3.3 矢量样轻子质量下限

见 2.7。

📎 **原文｜Minor 3**（见 §2.7 的引用；注意这是 **minor**，不是 major）

### 3.4 “conservative benchmark” 的歧义

见 2.7。

📎 **原文｜Minor 4**（见 §2.7 的引用）

### 3.5 缪子对撞机部分

审稿人认为这一节像是附加内容，与 UV 模型联系不够紧密。

📎 **原文｜Minor 5（逐字）**
> "What is the purpose of including muon collider bounds? The second half of the paper focuses on existing experimental bounds on the effective theory. It is a strange change in tone to include hypothetical muon collider bounds for future reach. The authors do not justify why a future muon collider is the way to test this model in the future and the section feels like it is tacked on. Most of the section emphasizes that the muon collider search would be a 'standard' follow up of existing work (Ref 83) and so this section does not seem particularly novel. The authors simply focus on the forward-backward asymmetry. Why not also include polarization asymmetries? Or would there be asymmetries in the $ee$ versus $TT$ final states? Given the first half of the paper, though, it seems that the real 'smoking gun' for this UV completion is the physics of the $S$ particle which should be tested in any Higgs-factory phase of a future lepton collider. I feel that this section either adds too little and should be downplayed as an example of future tests, or otherwise should have its own full fledged exploration (which may be a separate paper)."

他的建议是二选一：

#### 方案一：压缩为简短的未来探测示例

如果缪子对撞机不是论文核心创新，建议压缩这一节，只保留：

- 为什么缪子对撞机适合测试 $\mu$-耦合的 $Z'$；
- 轴矢量结构如何影响前后不对称（forward-backward asymmetry）；
- 说明这只是未来探测的一个示例；
- 重点放回 $\phi$ 和 UV 完备性的实验检验。

#### 方案二：真正扩展这一节

如果保留为重要结果，需要回应：

- 为什么选择缪子对撞机；
- 与已有 Ref. 83 相比新在哪里；
- 是否加入 polarization asymmetry；
- $\mu^+\mu^-$ 与其它末态的角分布是否有独特信息；
- 能否区分纯轴耦合、混合矢量/轴矢量耦合；
- 能否通过 $\phi$ 相关过程检验 UV 模型。

🖊 **非原文（整理者拆解）**：两个"方案"的框架与 bullet 拆分是整理者做的（原文是一句 either/or）。其中多数 bullet 有原文依据（Ref 83、polarization、$ee$ vs $\tau\tau$、rug），但"为什么缪子对撞机适合测试 $\mu$-耦合的 $Z'$"等属整理者补。
⚠️ **漏项（原文点名）**：原文的 "should be tested in any Higgs-factory phase of a future lepton collider"（其中 *any Higgs-factory phase* 是他强调的重点）—— Higgs factory（$e^+e^-$）这一半本文档没有回应，只讲了 μ 子对撞机。

从整份意见看，审稿人更希望看到的是：

> 如果这个 UV 模型真正有独特预测，那么 “发现 $\phi$” 应当比 “再做一次 $Z'$ 轴矢量搜索” 更像 smoking gun。

📎 **原文｜Minor 5（对应句，逐字）**
> "Given the first half of the paper, though, it seems that the real 'smoking gun' for this UV completion is the physics of the $S$ particle which should be tested in any Higgs-factory phase of a future lepton collider."

🖊 **非原文**：上面的中文块引用是**转述**，不是逐字（"应当比…更像 smoking gun" 是整理者加的对比句）。

如果工作量有限，建议压缩缪子对撞机部分，把新增篇幅用于 $\phi$、Higgs mixing、中微子和有限矢量耦合。

🖊 **非原文（整理者建议）**：原文只给了 either/or，没建议选哪个。

### 3.6 术语问题

需要统一修改：

- “light $Z'$”：给出明确质量范围，例如 $m_{Z'}\ll m_Z$，或直接定义为 $m_{Z'}\lt \cdots$；
- “intermediate scalar mass”：直接给出区间，例如 $m_\phi\in[\cdots,\cdots]$；
- “representative bounds”：说明是主导约束、部分约束，还是非完备列表；
- “point by point”：明确指参数扫描中的每一个 $(m_{Z'},g')$ 点，还是每一个 UV 参数点；
- “parameter region of interest”：在引言和 Fig. 2 图注中定义；
- “the line becomes large”：说明是进入非微扰区、违反某个耦合上限，还是只表示图形超出显示范围；
- “pure axial limit”：在式 (12) 之后直接定义；
- “conservative benchmark”：说明它是实验约束、理论上限，还是方便说明的选择。

📎 **原文｜Minor 6（六条，逐字）**
> **6.1** "The word "light" on page 2 has no reference scale."
> **6.2** "At the bottom of page 11, when referring to Table II, the authors write "representative bounds." What does representative mean? Does it mean these are the most stringent bounds? Are these "some" bounds? Is the list 'complete' in any sense?"
> **6.3** "Between page 12–13: "...do not provide a universal $g_{X}$ bound, but they show that the intermediate scalar-mass region cannot simply be assumed unconstrained." What does intermediate mass mean? It is also not clear what the intended content of this statement is: are the authors presenting a bound? Why would the reader assume that a new particle in this range would be unconstrained?"
> **6.4** "Below (34): "we impose Eq. (34) point by point", it's not clear what is meant by 'point.'"
> **6.5** "Page 21, first paragraph of Section E. What is the "parameter region of interest"? This wasn't clearly defined anywhere."
> **6.6** "Page 21, end of section D: What's the significance of the $v_{S}=2$ GeV line? What does it mean that $y_{s\mu\mu}$ "becomes large" (nonperturbative)? Why plot it? Is it a perturbativity bound?"

⚠️ **归类错位 / 混入**：本文档的 8 条清单里，
- 第 1、3、4、5 条 → 📎 Minor 6.1、6.3、6.4、6.5 ✅
- 第 2 条（representative）→ 📎 Minor 6.2 ✅
- 第 6 条（the line becomes large）→ 📎 Minor 6.6 ✅（但只取了后半，**漏了"$v_S=2$ GeV 线是什么、为什么画"**）
- 第 7 条（pure axial limit）→ 实际是 📎 **Minor 2**
- 第 8 条（conservative benchmark）→ 实际是 📎 **Minor 4**
→ 回复时应按报告原编号逐条对应，不要把 Minor 2/4 的内容混进 Minor 6 的回答里。

---

## 4. 建议的修改优先级

🖊 **非原文**：整个第 4 节的优先级排序是整理者设计的（原文 Recommendation 只说"major points 必须解决、minor 也请一并处理"）。各条与原文的对应如下：

### 第一优先级：确认模型是否能容纳 PMNS 混合

这是最关键的理论一致性检查。

📎 **原文｜Recommendation**："However, the question of whether this class of model can be consistent with neutrino oscillations is critical."

需要从电荷表开始，明确列出：

- 带电轻子 Yukawa；
- Weinberg 算符；
- 右手中微子 Dirac Yukawa；
- Majorana 质量项；
- 允许和禁止的非对角项；
- PMNS 矩阵的来源。

🖊 **非原文（整理者清单）**：原文没有这个清单；最接近的是 📎 Major 3.1、3.2 的两条断言。

如果最小模型无法产生混合，应尽快决定：添加中微子扇区，或缩小论文的物理主张。

🖊 **非原文**：对应 📎 Major 3 结尾 "include it / cite this"，但"缩小主张"是整理者提的第三条路。

---

### 第二优先级：补充 $\phi$ 的完整唯象学

📎 **原文｜Major 1**（三小条 + 前言，见 §2.1 的逐字引用）

至少给出：

- $m_\phi$ 的允许范围；→ 📎 Major 1.2
- $\phi$ 的主要衰变；→ 🖊 非原文
- $\phi$ 相关实验约束；→ 📎 Major 1 前言（"the bounds on the $S$"）与 📎 Major 4 前言
- Higgs 门户混合的圈级估计；→ 📎 Major 1.3
- $m_\phi\simeq m_h$ 附近的增强；→ 📎 Major 1.3
- $\phi$ 是否能被未来 collider 探测。→ 📎 Major 1.1（"mass range that can be probed by colliders"）与 📎 Minor 5（Higgs factory）

---

### 第三优先级：计算有限质量效应

包括：

- $g_V\neq0$；→ 📎 Major 4.3
- 动能混合 $\epsilon_{\rm kin}\neq0$；→ 📎 Major 4.2
- 矢量样轻子质量下限；→ 📎 Minor 3
- 这些效应是否改变 Fig. 2。→ 🖊 非原文（原文只要求"comment on possible experimental bounds"）

---

### 第四优先级：重构参数空间图

建议增加一张总览图，横轴和纵轴可以是：

$$
(m_{Z'},g')
$$

用不同颜色标示：

- 纯 EFT 允许区域；
- UV 可实现区域；
- 标量约束；
- Higgs mixing 约束；
- 动能混合约束；
- 有限矢量耦合约束；
- 微扰性边界；
- 矢量样轻子质量下限。

🖊 **非原文（整理者设计）**：整张图的设定都是整理者的。原文只要求"explicitly state in one place (perhaps in a table or a figure like Fig. 2) the range of the effective model parameters that are feasible"（📎 Major 2）。

这样可以回答审稿人最关心的 “EFT 参数空间中哪些点真的来自 UV 模型”。

📎 **原文｜Major 2**（对应句）："are values outside this range not allowed? What, if anything, does the perturbativity of the UV theory impose on the effective parameters?"

---

### 第五优先级：重新处理缪子对撞机部分和语言问题

📎 **原文｜Minor 5**（见 §3.5 逐字引用）+ 📎 **Minor 6**（术语）
🖊 **非原文**：把它放到"最后处理"这个次序是整理者的安排（原文只说 minor points "I strongly encourage"）。

---

## 5. 给审稿人的回复结构建议

🖊 **非原文（整理者方法）**：第 5 节整节是整理者写的写作方法，原文中唯一相关的是 📎 **Major 前言**——

> "In this referee report I make suggestions based on my understanding of the manuscript narrative. If I am mistaken, then perhaps the point of confusion merits clarification in the manuscript."

每条回复建议采用以下结构：

1. 感谢并准确复述问题；
2. 明确承认原稿哪里不清楚或哪里确实遗漏；
3. 给出新增的物理计算；
4. 说明计算对结论有什么影响；
5. 指出新增内容位于正文哪一节、哪张图、哪张表；
6. 如果没有纳入某一效应，给出定量理由。

### 示例：针对标量 $\phi$ 的英文回复

> We thank the referee for pointing out the missing connection between the UV completion and the scalar phenomenology. We agree that the scalar $\phi$ cannot be treated as an arbitrary decoupled state once the relation between $m_\phi$, $m_{Z'}$, $g'$, and $\lambda_\phi$ is imposed. We have therefore added a new subsection discussing the allowed scalar-mass range, its dominant decay modes, Higgs-portal mixing, and the corresponding collider and low-energy constraints. We also show the region in which the scalar can be probed independently of the effective axial-vector phenomenology.

🖊 **非原文（整理者草稿）**：回复的对应原文是 📎 Major 1（前言 + 1.1–1.3）。⚠️ 该段提到 "the relation between $m_\phi$, $m_{Z'}$, $g'$, and $\lambda_\phi$"——原文只提到式 (34) 与 $\lambda$（在 1.2），定稿时按稿件式 (34) 改写。

### 示例：针对中微子问题

如果最小模型不行，建议诚实写：

> We agree that the minimal field content used in the original manuscript does not generate a realistic nontrivial PMNS matrix. We have clarified this limitation and added a discussion of the minimal neutrino-sector extension required to generate neutrino mixing. We have also specified which conclusions concerning the charged-lepton and $Z'$ sectors remain unchanged under this extension.

如果你们能构造完整方案，则直接展示质量矩阵，而不是只说 “可以通过额外右手中微子实现”。

🖊 **非原文（整理者草稿）**：对应 📎 Major 3.1/3.2/结尾。⚠️ "minimal neutrino-sector extension" 的具体内容（奇电荷标量 $\sigma$）已由后续分析确定，见 `中微子扇区电荷分析-hy4.md`；本段草稿需要按该结论重写。

---

## 6. 总体评估

🖊 **非原文（整理者分类）**：三类划分与所有条目都是整理者做的，各条原文依据见下。

### 必须实质性补工作的部分

- 中微子振荡和 PMNS；→ 📎 Major 3、4.1、Recommendation
- $\phi$ 的质量范围和实验约束；→ 📎 Major 1.2、Major 1 前言
- Higgs 门户混合；→ 📎 Major 1.3
- 动能混合；→ 📎 Major 4.2
- 有限矢量耦合；→ 📎 Major 4.3
- UV 参数到 EFT 参数的可实现范围。→ 📎 Major 2

### 通过澄清和补图可以解决的部分

🖊 各条原文依据：

- 纯轴矢量极限的定义；→ 📎 Minor 2
- 参数范围；→ 📎 Minor 1、Major 2
- 式 (27) 的 benchmark 含义；→ 📎 Minor 4
- 矢量样轻子质量下限；→ 📎 Minor 3
- “light”“intermediate”“representative” 等术语；→ 📎 Minor 6.1、6.3、6.2
- Fig. 2 的范围选择。→ 📎 Major 2

### 可以重新定位或删减的部分

- 缪子对撞机部分；→ 📎 Minor 5
- 过度强调纯轴矢量 EFT 的结论；→ 🖊 非原文（整理者判断；相关的是 📎 Major 1 前言、Recommendation 末句）
- 没有和 $\phi$ 联系起来的未来 collider 讨论。→ 📎 Minor 5，原文表述为 the real "smoking gun" 是 $S$ 的物理、应在 Higgs-factory 阶段检验

---

## 7. 结论

这不是“拒稿式”意见。审稿人明确说论文可能对 model-building community 有用，也 “strongly encourage” 修改。

📎 **原文｜Recommendation（逐字）**
> "In its current form, the paper is not ready for publication. The major points above must be addressed. It's entirely possible that I have misinterpreted some of these points, but if that is the case then they at least indicate ideas that must be clarified before the manuscript merits publication. I strongly encourage the authors to further address the minor points."
> "The paper can be a useful addition to the model building literature. However, the question of whether this class of model can be consistent with neutrino oscillations is critical. I also feel that dismissing the physics of the scalar $S$ ignores the actual predictions of the UV model—otherwise the authors are simply justifying the phenomenology of the effective axial theory."

但这是一份要求实质性 revision 的 PRD 意见，不能只靠文字润色和补引用解决。

🖊 **非原文（整理者判断）**：原文用的是 "the paper is not ready for publication"（📎 Recommendation 首句），没有出现"PRD"字样；"PRD"来自 📎 **¶2**（"before the paper is at the level of a PRD manuscript"）。引用时应引对位置。

最稳妥的修稿主线是：

> 把论文从 “一个轴矢量 $Z'$ 有效理论的现象学分析” 重新组织为 “一个 anomaly-free UV completion 及其低能极限的完整分析”，明确区分纯 EFT 结果、UV 模型可实现区域，以及额外标量 / 有限质量效应。

🖊 **非原文（整理者建议）**：这句"修稿主线"是整理者提的；它与原文的两条批评方向一致（📎 Major 1 前言"major gap between these two parts"；📎 Recommendation 末句），但原文没有给出这样的改写方案。

在开始写 rebuttal 之前，最应该先完成两项内部计算：

1. **中微子质量矩阵的允许结构**（能否容纳 PMNS）；
2. **$\phi$ 与 Higgs mixing 的参数扫描**。

🖊 **非原文（整理者建议）**，依据：📎 Recommendation 点名的两个"critical / 不能忽略"问题（中微子、标量）。

这两项结果会决定整篇论文是小幅扩展、增加中微子扇区，还是需要重新收缩论文的主张。

🖊 **非原文（整理者判断）**。

---

## 8. 原文覆盖总表

| 报告位置 | 原文要点（逐字见上文） | 本文对应位置 | 状态 |
|---|---|---|---|
| ¶1 | 模型构造 + 第二个目标（轴矢极限现象学） | §1 | 📎 已补 |
| ¶2 | "significant reservations … PRD manuscript" | §1、§7 | 📎 已补 |
| Merits 1–3 | 构造清楚 / 现象学动机尚可 / 对 model builder 有用 | §1 | 📎 已补（第 4 条 bullet ⚠️ 无对应） |
| Major 前言 | "if I am mistaken … clarification" | §5 | 📎 已补 |
| Major 1 前言 | 两半脱节 + 式 (34) | §1、§2.1 | 📎 已补（⚠️ 式 (34) 形式被改写） |
| Major 1.1 | 应把 $S$ 作为主张之一 | §2.1(1) | 📎 已补（⚠️ 反问被改成陈述） |
| Major 1.2 | $m_S$ 窗口 + benchmark 构造 + "see minor #1" | §2.1(2) | 📎 已补（⚠️ 构造路线缺） |
| Major 1.3 | 圈生混合 + 共振 + Higgs 测量 + 仍怀疑不可退耦 | §2.1(3) | 📎 已补（⚠️ 圈图来源与公式需换） |
| Major 2 | 可行域表/图 + 为何取此范围 + 微扰性 | §2.3 | 📎 已补 |
| Major 3 前言 | 只有左手中微子 + Weinberg 算符 | §2.2 | 📎 已补 |
| Major 3.1 | Weinberg 允许 + 两矩阵对齐 ⇒ 无 PMNS | §2.2 检查 1 | 📎 已补（⚠️ "对齐"被弱化） |
| Major 3.2 | $N_R$ 带电 ⇒ 二三代矢量样 + 代际混合被禁 | §2.2 检查 2 | 📎 已补（⚠️ 原文没提反常） |
| Major 3 结尾 | include it / cite this / 否则 inconsistent | §2.2 路线 A–C | 📎 已补（⚠️ 三路线为整理者设计） |
| Major 4 前言 | 约束是否完整 + 要 §S 约束小节 | §2.6 | 📎 已补（⚠️ 与 Minor 6.2 混为一节） |
| Major 4.1 | 单位 PMNS 与振荡不符（指向 3.1） | §2.6 表 | 📎 已补 |
| Major 4.2 | benchmark 下动能混合非零 + 要参数化估计 + 引文献 | §2.4 | 📎 已补（⚠️ 公式为整理者补；缺文献建议） |
| Major 4.3 | 纯轴矢下的矢量耦合限 + 可能强几个数量级 | §2.4 末、§2.5 | 📎 已补（⚠️ 前半错放在 §2.4） |
| Major 4.4 | 恒星冷却是否相关（2511.09619） | §2.6 末 | 📎 已补 |
| Minor 1 | 目标区间 + 定义 light + 引言首词 | §3.1、§3.6 | 📎 已补 |
| Minor 2 | 式 (12) 处定义 pure axial，$\theta_{\mu R}\to0$ | §3.2 | 📎 已补（⚠️ 定义被换成 $g_V=0$） |
| Minor 3 | $M_{\rm VL}$ 下限 ⇒ $\theta$ 上限；与式 (27) 比 | §2.7、§3.3 | 📎 已补（⚠️ 被并进 major） |
| Minor 4 | conservative benchmark 的含义 | §2.7、§3.4 | 📎 已补（⚠️ 被并进 major） |
| Minor 5 | 缪子对撞机去留 + 极化 + $ee/\tau\tau$ + Higgs factory + $S$ 是 smoking gun | §3.5 | 📎 已补（⚠️ Higgs factory 未回应） |
| Minor 6.1 | "light" 无参考尺度 | §3.6 | 📎 已补 |
| Minor 6.2 | "representative bounds" | §2.6、§3.6 | 📎 已补 |
| Minor 6.3 | "intermediate scalar-mass region" + 这句在陈述什么 | §3.6 | 📎 已补（⚠️ 后半未答） |
| Minor 6.4 | "point by point" 的 point | §3.6 | 📎 已补 |
| Minor 6.5 | "parameter region of interest" | §3.6 | 📎 已补 |
| Minor 6.6 | $v_S=2$ GeV 线 + $y_{s\mu\mu}$ 变大 + 为什么画 | §3.6 | 📎 已补（⚠️ 只答"becomes large"） |
| Recommendation | 未达发表水平 + 中微子 critical + 不能忽略 $S$ | §1、§2.2、§4、§7 | 📎 已补 |
| Statement | 未使用 AI（与内容无关，无需回应） | — | — |

**统计**：报告共 31 个可回应单元；本文档 31 个全部有对应位置（📎 已补）。其中 **11 处标记 ⚠️**，需要在动笔前修正：4 处是位置/编号错位（Major 4.3 误放、Minor 3/4 并入 major、Minor 6 混入 Minor 2/4、Major 4 与 Minor 6.2 混节），7 处是内容与原文有出入（式 (34) 形式、1.1 反问改陈述、$\delta\lambda_{HS}$ 模板、pure axial 的定义、1.2 的构造路线、"对齐"被弱化、Minor 5/6.3/6.6 各漏一半）。

**🖊 标注为"非原文"的段落**是本文档的增值部分（推导、表格、公式、方案、英文草稿），回复时应表述为"我们补充的研究"，不要写成"应审稿人要求"。

---

## 9. 完备性与"工作建议"自检

**两句话结论**

1. **问题列全了**——报告里 31 个可回应单元全部有落点（见 §8）。去掉 Merits 与 Statement 两条无需回应的，剩 **29 条**；其中纯描述性 1 条（¶1），实需动手 **28 条**。
2. **工作建议不完全**——29 条里 **21 条**有明确"做什么"的建议，**5 条**只有一个主题词、**2 条**完全没有、**1 条**无需动作（下表 ⚠️/❌）。**而且全部 29 条都只有"做什么"，没有"怎么做"**（输入、步骤、交付物、验收、依赖），本节末尾有说明。

| # | 原文位置 | 是否列出 | 工作建议 | 缺什么 |
|---|---|---|---|---|
| 1 | ¶1（模型构造 + 第二个目标） | ✅ §1 | 无需动作（描述性） | — |
| 2 | ¶2（reservations / PRD 水准） | ✅ §1、§6、§7 | ✅ 承认并逐条回应 | 无步骤 |
| 3 | Major 前言（"若我理解有误请澄清"） | ✅ §5（本次标注补上） | ✅ 按六步法回复 | 原稿漏记这句，已补 |
| 4 | Major 1 前言（两半脱节 + 式 (34)） | ✅ §1、§2.1 | ✅ 正面承认 + 纳入 $S$ | 未原样引用式 (34)，归一化待核 |
| 5 | Major 1.1（$S$ 应为卖点） | ✅ §2.1(1) | ✅ 改论文定位 | 无步骤；"only known" 需文献支撑 |
| 6 | Major 1.2（$m_S$ 窗口） | ✅ §2.1(2) | ⚠️ 只列了五个条件 | **缺审稿人给的 benchmark 构造路线**（先定 $m_{A'}$ 区间 → 读 $g_X$ 强约束 → 推 $m_S$）；缺判据取值与数字 |
| 7 | Major 1.3（Higgs 门户） | ✅ §2.1(3) | ✅ 六项检查 + 四条衰变道 | 圈图来源写成"矢量样轻子 + 规范耦合"，与原文说的 $\mu,\tau$ 圈不一致；原文要的"在允许范围内量化混合角"只给了定性检查，缺曲线/数值 |
| 8 | Major 2（可行域表/图） | ✅ §2.3 | ✅ 总览表 + 映射式 | 无步骤；"in one place" 未落实 |
| 9 | Major 3 前言（SM 只有左手中微子） | ✅ §2.2 | ✅ 背景陈述 | — |
| 10 | Major 3.1（Weinberg 与 Yukawa 对齐） | ✅ §2.2 检查 1 | ✅ 逐条核验电荷 | 原文断言的是两矩阵**必须对齐**，本文档写成条件句（"如果…也被迫对角"），没有证明对齐本身 |
| 11 | Major 3.2（$N_R$ 救不了） | ✅ §2.2 检查 2 | ✅ 检查新反常与非对角项 | 原文的两个具体断言（二三代必须成矢量样组合、代际混合被禁）未正面核验 |
| 12 | Major 3 结尾（给解法或引文献） | ✅ §2.2 三条路线 | ✅ 路线 A/B/C | 只有三条路线的名字，无取舍准则；原文的"cite this"（引已知文献）一路未给任何具体文献 |
| 13 | Major 4 前言（约束是否完整 + 要 $S$ 约束小节） | ✅ §2.6 | ⚠️ 只有表里一行"$\phi$ 搜索必须新增" | **缺 $S$ 约束小节的清单与范围** |
| 14 | Major 4.1（单位 PMNS） | ✅ §2.6 表 | ⚠️ 仅交叉引用（设计如此） | 可接受 |
| 15 | Major 4.2（动能混合定量） | ✅ §2.4 | ⚠️ 有公式与"给数值" | **缺原文点名的文献参数化引用**；数值只给了 $10^{-n}$ 的示意，无具体量级与实验限对比 |
| 16 | Major 4.3（残余 $g_V$ 与矢量限） | ✅ §2.4 末、§2.5 | ✅ 两件事 + 一张图 + 六个实验 | 无步骤；归类错位（见 §2.4 的 ⚠️） |
| 17 | Major 4.4（恒星冷却） | ✅ §2.6 末 | ✅ 五项检查 | 无步骤；适用与否取决于 $m_{A'}$ 是否足够轻，本文档未给出质量阈值 |
| 18 | Minor 1（参数范围 + 定义 light） | ✅ §3.1、§3.6 | ✅ 给分段与参考尺度 | 无步骤 |
| 19 | Minor 2（纯轴矢极限的定义） | ✅ §3.2 | ✅ 在式 (12) 后定义 | ⚠️ 原文建议的条件是 $\theta_{\mu R}\to0$，本文档换成了 $g_V=0$ |
| 20 | Minor 3（$M_{\rm VL}$ 下限） | ✅ §2.7、§3.3 | ✅ 给下限 + 与式 (27) 比 | 归类错位（minor 写成了 major） |
| 21 | Minor 4（conservative benchmark） | ✅ §2.7、§3.4 | ✅ 两句替换文本 | 归类错位 |
| 22 | Minor 5（缪子对撞机去留） | ✅ §3.5 | ⚠️ 给了两方案与 bullet | **缺 Higgs factory 那一半的建议** |
| 23 | Minor 6.1（light 无尺度） | ✅ §3.6 | ✅ 给区间 | — |
| 24 | Minor 6.2（representative bounds） | ✅ §3.6、§2.6 | ✅ 四个候选措辞 | — |
| 25 | Minor 6.3（intermediate 那句话） | ✅ §3.6 | ❌ 只答"直接给出区间" | **缺"这句话到底在陈述什么、限的是哪个参数"的建议** |
| 26 | Minor 6.4（point by point） | ✅ §3.6 | ✅ 明确 point 的含义 | — |
| 27 | Minor 6.5（parameter region of interest） | ✅ §3.6 | ✅ 在引言与图注定 | — |
| 28 | Minor 6.6（$v_S=2$ GeV 线与 $y_{s\mu\mu}$） | ✅ §3.6 | ❌ 只答"becomes large = 非微扰" | **缺"这条线是什么、为什么画"的建议** |
| 29 | Recommendation（中微子 critical + 不能忽略 $S$） | ✅ §1、§4、§6、§7 | ✅ 列为两个 P0 | 无步骤 |

**⚠️/❌ 汇总（7 条需补，其中 #14 属可接受）**：#6（1.2 的构造路线）、#13（$S$ 约束小节）、#14、#15（文献参数化）、#22（Higgs factory）、#25（6.3 后半）、#28（6.6 的 $v_S$ 线）；另外 #19 是**定义被换**、#20/#21 是**归类错位**（建议本身不缺，但位置要改）。

**评判范围说明**：本节只拿报告原文与本文档本身作比较，不引入其他材料。$(g-2)_\mu$、轻子味破坏等不在原文诉求内，不计入缺口。另外：**29 条无一条给出了"怎么做"**（输入、步骤、交付物、验收、依赖），这是文档体裁所致，不算遗漏，但意味着本文档只能当分析报告用，不能当施工单用。
