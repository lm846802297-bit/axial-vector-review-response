# Major Point 4.4：轴矢量耦合的恒星冷却与超新星约束——文献适用性调查

**调查日期：** 2026-11-04  
**用途：** 内部文献调查、模型映射与审稿回复依据。本文档不是正式回复信，也不代表已经完成本文模型的 SN1987A / low-energy supernova (LESN) 数值重分析。

## 1. 结论摘要

本轮针对“是否已有研究直接计算轴矢量耦合的 stellar-cooling / supernova bounds”进行了定向文献检索。结论必须分成三个层次：

1. **确实存在轴矢量相互作用与恒星冷却相关的研究。** Kahn、Krnjaic、Mishra-Sharma 与 Tait 的 2017 年工作系统讨论了 MeV–GeV 轴矢量 \(U(1)\) 力，并在 §2.4 明确指出：对 \(m_{A'}<2m_e\) 的超轻轴矢量玻色子，恒星等离子体中的光子转换可能导致冷却；轴矢量模型还可能具有不经 kinetic mixing 的中微子耦合，因此其恒星产生机制不一定由普通暗光子过程主导。但作者明确将完整的 ultralight axial-\(A'\) stellar-cooling 分析列为超出该文范围。该文不是针对本文模型的 SN1987A 排除曲线。
2. **确实存在轴矢量核子耦合的 SN1987A 研究线索。** EPS-HEP 2019 的会议报告讨论了 \(Z_dNN\) 的轴矢量耦合，计算核子核子 bremsstrahlung、反吸收和衰变，并报告在矢量与轴矢量核子耦合相近时，轴矢量项可主导发射与吸收。但目前检索到的是会议摘要/报告材料，不是可直接引用为本文轴矢量轻子流的完整同行评审数值分析。Bell 等人 2024 年的 CRDM 文章也讨论轴矢量核子介子，但其 SN1987A 线是借用矢量介子约束作为 proxy，并明确指出轴矢量天体物理限制可能更强；它没有完成轴矢量 SN 输运重分析。
3. **本轮没有找到对本文所需的“轴矢量缪子流 + 左手中微子流”完整 SN1987A / LESN 数值重分析。** 最接近的 \(U(1)_{L_\mu-L_\tau}\) 超新星研究（Lai et al. 2024、Blinov et al. 2026、Wang & Zhang 2026）均以常规矢量型 \(L_\mu-L_\tau\) 规范玻色子为对象。它们不能整体移植到本文模型，但其中的中微子流与本文完全相同，因此中微子聚合产生和不可见中微子部分宽度在相同 \((m_{A'},g_X)\) 下可以直接对应。

**对审稿意见的正确回答不是“stellar cooling 不相关”，而是：超新星约束相关；中微子产生子过程可以直接映射；矢量模型的完整排除曲线不能未经重算就作为轴矢量 UV 模型的排除曲线。**

---

## 2. 本文模型与常规 \(L_\mu-L_\tau\) 矢量模型的相互作用差别

本文低能质量基底的相关相互作用可写为
\[
\begin{aligned}
\mathcal L_{A'}\supset A'_\alpha\bigg[
&g_X\,\bar\nu_\mu\gamma^\alpha P_L\nu_\mu
-g_X\,\bar\nu_\tau\gamma^\alpha P_L\nu_\tau\\
&+g_V^\mu\bar\mu\gamma^\alpha\mu
+g_A^\mu\bar\mu\gamma^\alpha\gamma_5\mu
+\cdots\bigg],
\end{aligned}
\]
其中
\[
g_V^\ell=g_X\sin^2\theta_{\ell R},\qquad
g_A^\ell=-g_X\cos^2\theta_{\ell R},
\qquad
\left|\frac{g_V^\ell}{g_A^\ell}\right|
=\tan^2\theta_{\ell R}.
\]
在本文采用的 \(|\theta_{\ell R}|\leq10^{-2}\) 参数域中，
\[
|g_V^\ell/g_A^\ell|\lesssim1.01\times10^{-4}.
\]

常规矢量型 \(U(1)_{L_\mu-L_\tau}\) 的带电轻子流则为
\[
g_{\mu\tau}A'_\alpha
(\bar\mu\gamma^\alpha\mu-\bar\tau\gamma^\alpha\tau),
\]
而其中微子流同样是
\[
g_{\mu\tau}A'_\alpha
(\bar\nu_\mu\gamma^\alpha P_L\nu_\mu
-\bar\nu_\tau\gamma^\alpha P_L\nu_\tau).
\]

因此，两个模型并非“所有相互作用都不同”，也并非“所有相互作用都相同”：

- **中微子流：相同。** 本文的 \(A'\nu_\mu\nu_\mu\) 与 \(A'\nu_\tau\nu_\tau\) 顶点及常规 \(L_\mu-L_\tau\) 模型一致。固定 \(m_{A'}\) 和 \(g_X=g_{\mu\tau}\) 后，\(\nu_\alpha\bar\nu_\alpha\leftrightarrow A'\) 的树级振幅、极化分量、相空间和不可见部分宽度相同（忽略中微子质量及额外轻态混合修正）。
- **带电缪子流：不同。** 本文主导项为轴矢量流 \(\bar\mu\gamma^\alpha\gamma_5\mu\)，常规参考模型为矢量流 \(\bar\mu\gamma^\alpha\mu\)。半康普顿产生、逆过程吸收、纵向极化以及 \(A'\to\mu^+\mu^-\) 宽度不能直接照搬。
- **核子/电子流：不同。** 本文没有 \(A'\) 对核子的树级 \(L_\mu-L_\tau\) 荷；与质子有关的电磁耦合只通过很小的诱导 kinetic mixing 出现。电子也没有树级直接耦合。

这一区分是后续判断文献可迁移性的基础。

### 2.1 可直接映射的中微子部分

在本文的规范荷约定下，
\[
g_{\nu_\mu}=+g_X,\qquad g_{\nu_\tau}=-g_X.
\]
对每个无质量左手中微子味，
\[
\Gamma(A'\to\nu_\alpha\bar\nu_\alpha)
=\frac{g_X^2m_{A'}}{24\pi}.
\]
求和两个味后，
\[
\Gamma_{\nu\bar\nu}^{\rm total}
=\frac{g_X^2m_{A'}}{12\pi}.
\]
这与常规矢量型 \(L_\mu-L_\tau\) 模型的中微子部分宽度一致。两味耦合的相对负号不会改变各自独立的 \(\nu_\alpha\bar\nu_\alpha\to A'\) 产生率。

因此，矢量型 \(L_\mu-L_\tau\) SN 研究中的中微子聚合（neutrino coalescence）产生、逆衰变吸收和 \(A'\to\nu\bar\nu\) 不可见衰变，是可以在相同 SN 中微子分布和相同 \((m_{A'},g_X)\) 下直接复用的**子过程**。这并不自动意味着整个冷却/输运曲线相同，因为总产生率、总宽度和光学深度还包括带电缪子相关过程。

### 2.2 不能直接映射的轴矢量缪子部分

常规矢量模型的缪子半康普顿过程为
\[
\mu^\pm+\gamma\leftrightarrow\mu^\pm+A'.
\]
本文必须使用轴矢量顶点 \(g_A^\mu\gamma^\alpha\gamma_5\) 重新计算振幅。特别是
\[
q_\alpha\,\bar u(p')\gamma^\alpha\gamma_5u(p)
=2m_\mu\,\bar u(p')\gamma_5u(p),
\]
轴矢量流在有限缪子质量下不守恒。其纵向 \(A'\) 模式通过 Goldstone 等价定理与相应的赝标量耦合相关，量级为
\[
g_{G\mu}\simeq\frac{2g_A^\mu m_\mu}{m_{A'}}
\]
（符号依赖 Goldstone 场约定）。常规矢量流在相应树级极限下满足 \(q_\alpha J_V^\alpha=0\)，所以纵向模式的低质量标度不同。

这意味着：即使中微子 coalescence 产生率完全相同，半康普顿的横向/纵向分辨产生率和吸收率也不相同。不能把常规矢量模型的 \(T/L\) 分量直接复制给本文。

---

## 3. 是否存在直接的轴矢量 stellar-cooling / SN 文献？

### 3.1 Kahn et al. (2017)：直接讨论轴矢量 \(U(1)\) 与恒星冷却，但没有给出本文所需的 SN 数值曲线

Yonatan Kahn, Gordan Krnjaic, Siddharth Mishra-Sharma, and Tim M. P. Tait, “Light Weakly Coupled Axial Forces: Models, Constraints, and Projections,” JHEP 05 (2017) 002, arXiv:1609.09072v2, DOI: https://doi.org/10.1007/JHEP05(2017)002.

该文研究具有非零轴矢量耦合的 MeV–GeV 隐藏 \(U(1)\) 力。其 §2.4 明确讨论 \(m_{A'}<2m_e\) 时的 stellar-cooling 现象：若 \(A'\) 主要通过光子混合产生且足够长寿，等离子体光子可转换为 \(A'\) 并带走能量；但轴矢量模型可能具有不经 kinetic mixing 的树级中微子耦合，恒星内主要产生机制因此未必是暗光子型 plasmon conversion。作者明确说明，完整的 ultralight axial-\(A'\) stellar-cooling 约束需要专门分析，超出该文范围。

**适用性判断：**
- 这是直接研究轴矢量规范玻色子与恒星冷却关系的重要文献，不能漏引。
- 它没有提供本文 \(m_{A'}\geq1\,\mathrm{MeV}\)、轴矢量缪子耦合和 \(L_\mu-L_\tau\) 中微子耦合的 SN1987A 数值排除曲线。
- 该文特别强调的 \(m_{A'}<2m_e\) 超轻区间仅与本文 Fig. 2 的最低质量端 \(1\,\mathrm{MeV}\) 附近有很窄的交集；本文的树级中微子衰变也使其“长寿命、仅靠 kinetic mixing”的基准不适用于本文。
- 它支持的结论是“轴矢量恒星冷却不能用纯暗光子假设处理”，而不是“本文参数空间已经被它排除”。

### 3.2 Lai et al. (EPS-HEP 2019)：轴矢量核子耦合的 SN1987A 计算线索

Wei-Hao Lai, Guey-Lin Lin, Yue-Lin Sming Tsai, and Meng-Ru Wu, “Constraints on Electromagnetic and Neutral Current Couplings of Dark Vector Boson to Standard Model Fermions by SN1987A,” EPS-HEP 2019 conference contribution, 12 July 2019.

来源：https://indico.cern.ch/event/577856/contributions/3423847/

会议摘要描述了一个通过 kinetic mixing 和 mass mixing 与标准模型规范玻色子混合的暗矢量玻色子。作者计算
\[
N+N\to N+N+Z_d,\qquad
N+N+Z_d\to N+N,
\]
并考虑 \(Z_d\to\ell^+\ell^-\) 和 \(Z_d\to\nu\bar\nu\) 衰变。摘要指出：当 \(Z_dNN\) 的矢量和轴矢量耦合大小相近时，轴矢量核子耦合对发射与反吸收的贡献可能占主导。

**适用性判断：**
- 该报告说明轴矢量相互作用确实可以改变 SN1987A 发射和吸收，不能笼统认为超新星只约束矢量流。
- 它研究的是 \(Z_dNN\) 核子轴矢量流，而本文没有对应的树级核子轴矢量耦合。
- 本文很小的 kinetic mixing 只诱导电磁型矢量耦合，不等于该报告中可与矢量核子耦合相比较的轴矢量 \(Z_dNN\) 耦合。
- 本轮找到的是会议摘要/报告材料；没有将其作为一篇完整、同行评审的本文模型轴矢量轻子流重分析来引用。

### 3.3 Bell et al. (2024)：轴矢量核子介子被讨论，但 SN 曲线采用矢量 proxy

Nicole F. Bell, Jayden L. Newstead, and Iman Shaukat-Ali, “Cosmic-ray dark matter confronted by constraints on new light mediators,” Phys. Rev. D 109, 063034 (2024), arXiv:2309.11003v2, DOI: https://doi.org/10.1103/PhysRevD.109.063034.

该文在 §II 定义了轴矢量核子介子相互作用
\[
\mathcal L_{\rm int}^{A}
=g_{\chi A}A^\mu\bar\chi\gamma_\mu\gamma^5\chi
+g_{NA}A^\mu\bar N\gamma_\mu\gamma^5N.
\]
其 §IV 的天体物理比较包括 HB/RG stellar-cooling 和 SN1987A cooling/trapping 曲线。但作者明确说明：对 axial-vector mediator，他们采用的是 vector mediator 的 SN1987A 约束作为保守 proxy，并指出轴矢量耦合可能具有更强的天体物理限制。

**适用性判断：**
- 该文并没有完成轴矢量核子流的 SN1987A 发射、吸收和输运重新计算。
- 其模型是轴矢量核子—暗物质相互作用，与本文轴矢量缪子—中微子规范流不同。
- 不应将其图中的 SN 线作为本文模型的直接排除界限。
- 这篇文章最有价值的地方是提醒：轴矢量和矢量核子流的超新星约束可能不同，不能仅凭相同的 mediator mass 和 coupling 名称直接移植。

### 3.4 Muon-philic scalar/pseudoscalar 文献：有直接的超新星缪子环境研究，但不是轴矢量自旋 1 玻色子

- D. Croon, G. Elor, R. K. Leane, and S. D. McDermott, “Supernova Muons: New Constraints on \(Z'\) Bosons, Axions and ALPs,” JHEP 01 (2021) 107, arXiv:2006.13942, DOI: https://doi.org/10.1007/JHEP01(2021)107.
- R. Bollig et al., “Muons in supernovae: implications for the axion-muon coupling,” Phys. Rev. Lett. 125, 051104 (2020), arXiv:2005.07141.
- D. Caputo, G. Raffelt, and E. Vitagliano, “Muonic boson limits: Supernova redux,” Phys. Rev. D 105, 035022 (2022), arXiv:2109.03244, DOI: https://doi.org/10.1103/PhysRevD.105.035022.

这些工作的重要贡献是证明 PNS 核心中的缪子丰度、化学势和空间分布会影响缪子耦合新粒子的产生与吸收。Croon et al. 研究了矢量 \(Z'\) 以及轴子/ALP；Caputo et al. 研究标量和赝标量缪子玻色子。它们不是本文的轴矢量 \(A'_\mu\) 计算。

赝标量 ALP 的导数耦合与轴矢量流的散度有关，因此对本文 \(A'\) 的纵向模式具有类比价值；但 ALP 是自旋零粒子，没有 \(A'\) 的横向极化，也没有相同的总宽度、吸收通道和输运。因此不能把 ALP 的 SN1987A 数值界限直接当成轴矢量 \(A'\) 的限制。

---

## 4. \(L_\mu-L_\tau\) 矢量规范玻色子的 SN 研究：对本文最有用的参考

### 4.1 Lai, Leung, and Lin (2024)

Kwang-Chang Lai, Chun Sing Jason Leung, and Guey-Lin Lin, “SN1987A constraints to BSM models with extra neutral bosons near the trapping regime: \(U(1)_{L_\mu-L_\tau}\) model as an illustrative example,” Phys. Rev. D 110, 103023 (2024), arXiv:2401.16023, DOI: https://doi.org/10.1103/PhysRevD.110.103023.

该文计算常规矢量 \(L_\mu-L_\tau\) 的 \(Z'\) 产生、吸收和衰变，包括：
- \(\nu\bar\nu\to Z'\) 与逆聚合；
- \(\mu^+\mu^-\to Z'\)；
- \(\mu^\pm\gamma\leftrightarrow\mu^\pm Z'\) 半康普顿过程；
- 通过 kinetic mixing 诱导的 \(np\) loop bremsstrahlung；
- \(Z'\) 衰变及其逆过程。

该文的重要方法学结论是：强耦合 trapping 区域中，不能只将自由流发射率外推；产生和吸收竞争可能使总 luminosity 呈现平台，而不是简单随耦合增大而单调趋于零。作者采用 Raffelt luminosity criterion \(L_{\rm NB}\lesssim3\times10^{52}\,\mathrm{erg/s}\) 讨论 SN1987A，并指出 \(\tau\sim1\) 只是 trapping 的近似判据。

**对本文的意义：** 这是与本文中微子流最接近的模型参考，同时也展示了为什么不能只引用一个自由流阈值就宣称完成了完整 SN 排除。

### 4.2 Blinov et al. (2026)：审稿人指定文献

M. Blinov et al., “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” JHEP 06 (2026) 155, arXiv:2511.09619v2, DOI: https://doi.org/10.1007/JHEP06(2026)155.

这是审稿人明确指定的文献，正式回复中应当正面讨论。它对常规矢量 \(L_\mu-L_\tau\) 玻色子研究了多个不同的 SN 探针：
- ballistic SN1987A cooling；
- 有适用区间条件的 diffusive transport；
- SN1987A 高能中微子缺失；
- \(A'\to\mu^+\mu^-\) 后在 progenitor 内衰变引起的 low-energy supernova (LESN) 加热；
- 相关的衰变概率、能量沉积和传播条件。

该文强调高能中微子观测在其大部分矢量模型参数空间中比单纯 Raffelt cooling criterion 更敏感；diffusion 近似只在有限区域内有效。它还指出当新粒子平均自由程接近 PNS 半径时，固定 SN profile 可能不再自洽，因为新粒子能量输运会反过来影响 SN 演化。

### 4.3 Wang and Zhang (2026)：较新的矢量模型更新

Zun Wang and Yongchao Zhang, “Revisiting supernova constraints on dark gauge bosons,” arXiv:2610.35379v1 (2026-10-26), https://doi.org/10.48550/arXiv.2610.35379.

这是 2026 年 10 月 26 日提交的预印本，不应称为已发表期刊结果。该文对 dark photon、\(U(1)_{B-L}\) 和常规矢量 \(U(1)_{L_\mu-L_\tau}\) 进行了 T/L 模式分辨的 SN 计算，并使用 SFHo-18.8 等 SN profile。

对其矢量 \(L_\mu-L_\tau\) benchmark：
- \(m_{Z'}=1,10,100\,\mathrm{MeV}\) 的产生率比较显示，semi-Compton 在 \(m_{Z'}\lesssim10\,\mathrm{MeV}\) 时占主导，而 neutrino coalescence 在 \(m_{Z'}\gtrsim10\,\mathrm{MeV}\) 时占主导；
- 在其自然 kinetic-mixing 设定 \(\epsilon_{\mu\tau}=-g_{\mu\tau}/70\) 下，\(np\) bremsstrahlung 在所研究参数区间始终次要；
- 其 SFHo-18.8 profile 的 SN1987A cooling 质量覆盖约到 \(300\,\mathrm{MeV}\)；预印本摘要/概览给出的排除耦合区间下边界约 \(1.4\times10^{-10}\)，而 §5.3 正文给出的下边界为 \(1.2\times10^{-10}\)。因此稳妥表述是灵敏度约为 \(10^{-10}\)，精确数值应按所引用的图和正文口径说明；
- LESN 质量覆盖约到 \(600\,\mathrm{MeV}\)，耦合灵敏度达到约 \(6.4\times10^{-12}\)；
- LESN 的 \(e^+e^-\) 能量沉积依赖 loop-induced kinetic mixing，而 \(m_{Z'}>2m_\mu\) 后 \(\mu^+\mu^-\) 衰变成为主要的带电粒子能量沉积通道。

该文的数字是特定矢量模型和 SN profile 的参考尺度，不是本文轴矢量模型的已验证排除界限。尤其要注意：其 semi-Compton 公式和纵横极化分解不能直接用于本文轴矢量缪子流；PR #30 的专项记录已经指出 arXiv:2610.35379v1 的部分 \(T/L\) 表达式存在需要独立核对的标记/投影一致性问题。引用其总量级可以，但不应未经独立振幅验证就引用其极化分量结论。

---

## 5. 按物理过程逐项判断可迁移性

| 物理过程 | 常规矢量 \(L_\mu-L_\tau\) 文献 | 本文轴矢量 UV 模型 | 可迁移性判断 |
|---|---|---|---|
| \(\nu_\mu\bar\nu_\mu,\nu_\tau\bar\nu_\tau\to A'\) | 树级左手中微子流 | 相同的左手中微子流 | **振幅级直接对应**；需使用相同 SN 中微子分布和化学势 |
| \(A'\to\nu_\alpha\bar\nu_\alpha\) | 相同中微子顶点 | 相同中微子顶点 | **部分宽度直接对应**；总宽度仍需加入轴矢量缪子通道 |
| \(\mu^\pm\gamma\to\mu^\pm A'\) | 矢量缪子顶点 | 轴矢量缪子顶点 | **不可直接移植**；必须重新计算振幅、热平均和 T/L 模式 |
| \(A'+\mu^\pm\to\gamma+\mu^\pm\) | 矢量逆半康普顿吸收 | 轴矢量逆过程 | **不可直接移植**；详细平衡关系可用，但输入的极化分辨产生率必须重新计算 |
| \(\mu^+\mu^-\to A'\) | 矢量缪子流 | 轴矢量缪子流 | 矩阵元和极化分量不同；还需使用 SN 的 \(\mu^+\)、\(\mu^-\) 分布 |
| \(A'\to\mu^+\mu^-\) | \(\beta_\mu(1+2r_\mu)\) 阈值因子 | \(\beta_\mu^3\) 阈值因子 | **不可直接移植**；改变总宽度、寿命、分支比和 trapping |
| \(np\to npA'\) | 通过 loop-induced photon mixing 的质子矢量耦合 | 仅有很小的诱导电磁混合；无树级核子荷 | 预期更弱，但仍需 in-medium \(q^2\) 及 form-factor 核验 |
| 纵向 \(A'_L\) | 矢量流近似守恒 | 轴矢量缪子流有限质量下不守恒 | **尤其不能移植**；Goldstone/纵向模式需独立处理 |
| \(A'\to e^+e^-\) 与 progenitor heating | 依赖自然 loop mixing | 依赖本文很小的 loop mixing | **不能照搬 LESN 曲线**；可按本文 \(\epsilon(q^2)\) 和轴矢量总宽度重新计算 |
| WD/RG plasmon conversion | 主要由 photon–\(A'\) mixing 控制 | mixing 显著小于常规矢量 benchmark，且 Fig. 2 的最低质量高于典型 WD plasmon 共振能标 | 不能直接套用；应以本文 \(\epsilon(q^2)\) 做质量/等离子体条件比较 |

### 5.1 半康普顿与纵向模式的关键公式

轴矢量流的非守恒关系
\[
q_\mu J_5^\mu=2m_\mu\,\bar\mu i\gamma_5\mu
\]
意味着纵向模式在 \(m_{A'}\) 较小时可能具有不同的质量标度。由 Goldstone 等价定理得到的有效耦合量级
\[
g_{G\mu}\sim\frac{2g_A^\mu m_\mu}{m_{A'}}
\]
必须与 UV 破缺扇区一致地解释，不能把它误当作一个独立任意的赝标量 Yukawa 参数。

PR #30 的研究记录已经包含：
- \(\gamma\mu\to\mu A'\) 的树级 \(s/u\) 道振幅；
- 显式 Dirac 自旋器与 Ward identity 检查；
- 真空截面和热率原型；
- 对 T/L 模式、热平均、介质静止系投影和吸收率尚未闭环的说明。

因此 PR #30 是该过程的内部技术依据，但其工作状态不能被表述为“已经完成 SN 输运重分析”。目前仍缺少完整的模式分辨介质发射率、吸收率、径向 SN profile 积分和 trapping/transport 闭环。

### 5.2 衰变宽度与 LESN 的关键差别

令 \(r_\mu=m_\mu^2/m_{A'}^2\)。对纯矢量缪子流，
\[
\Gamma_V(A'\to\mu^+\mu^-)
=\frac{g_X^2m_{A'}}{12\pi}
(1+2r_\mu)\sqrt{1-4r_\mu}.
\]
对本文轴矢量缪子流，
\[
\Gamma_A(A'\to\mu^+\mu^-)
=\frac{(g_A^\mu)^2m_{A'}}{12\pi}
(1-4r_\mu)^{3/2}.
\]
两者在 \(m_{A'}\to2m_\mu^+\) 时具有不同的阈值幂次。因而：
- \(A'\) 的衰变长度和在 progenitor 内的衰变概率不同；
- \(A'\to\mu^+\mu^-\) 的分支比不同；
- muon stopping、muon decay-at-rest 和最终能量沉积的 LESN 估计不能直接复制。

### 5.3 Kinetic mixing 与核子/普通恒星通道

常规矢量 \(L_\mu-L_\tau\) benchmark 常采用自然 loop mixing
\[
|\epsilon_{\mu\tau}|/g_{\mu\tau}\sim1/70\simeq1.4\times10^{-2}.
\]
本文在等混合角、重态物理质量简并和 \(\epsilon_{\rm ind}(\mu_{\rm match})=0\) 的 benchmark 下，
\[
|\epsilon_{\gamma A'}(0)|/|g_X|
\simeq1.44\times10^{-6}
\quad(\theta_R=10^{-2}).
\]
因此两者的 mixing 振幅比约为 \(10^{-4}\)，同一动量点上由该 mixing 主导的产生率按 \(\epsilon^2\) 缩放时约低 \(10^{-8}\)。这只是相同传播子、相同介质和相同动量条件下的参数标度比较；不能代替 in-medium plasmon propagator 和 \(q^2\)-dependent mixing 的完整计算。

对本文的 WD/RG 相关性还要注意：
- 常规白矮星温度与等离子体频率通常为 keV 量级；本文 Fig. 2 的 \(m_{A'}\) 下限约 \(1\,\mathrm{MeV}\)，因此其共振 plasmon 区域通常位于本文质量窗口以下。
- \(m_{A'}\geq1\,\mathrm{MeV}\) 的非共振重质量贡献仍由本文小的 kinetic mixing 控制；没有完成完整 WD emissivity 计算前，不应宣称整个 WD/RG 限制严格为零。
- PNS 的温度和密度更高，并可出现有意义的缪子丰度，因此 SN1987A 比普通 WD/RG cooling 更直接地探测本文的缪子和中微子耦合。

---

## 6. 参考文献中的数值和方法应如何使用

| 文献 | 研究模型/机制 | 可用于本文的内容 | 不可直接使用的内容 |
|---|---|---|---|
| Kahn et al. 2017 | 一般轴矢量 \(U(1)\)，讨论超轻粒子的 plasmon stellar cooling | 证明轴矢量恒星冷却问题已被明确提出；指出树级中微子耦合可能改变产生机制 | 不能作为本文 \(m_{A'}\geq1\) MeV 的 SN1987A 数值曲线 |
| Lai et al. 2019 | \(Z_dNN\) 轴矢量核子耦合 | 说明轴矢量核子过程可主导 SN 发射/吸收 | 不适用于本文无树级核子轴矢量荷的模型 |
| Bell et al. 2024 | 轴矢量核子介子用于 CRDM | 说明轴矢量天体物理限制可能强于矢量 | 其 SN 曲线本身采用 vector proxy，不是轴矢量 SN recast |
| Lai et al. 2024 | 矢量 \(L_\mu-L_\tau\) | 中微子 coalescence、SN profile、trapping plateau 的参考 | 矢量缪子 semi-Compton 和总输运曲线 |
| Blinov et al. 2026 | 矢量 \(L_\mu-L_\tau\) | 审稿人指定的 SN cooling、high-energy neutrino、LESN 文献 | 全部矢量排除曲线不能直接标为轴矢量排除 |
| Wang & Zhang 2026 | 矢量 \(L_\mu-L_\tau\)，T/L 模式分辨 | \(m_{A'}\sim10\) MeV 的过程主导区分；较新的 profile 和数值参考 | 轴矢量半康普顿矩阵元、纵向模式、阈值衰变和 LESN 曲线 |
| Croon et al. 2021 / Caputo et al. 2022 | 矢量 \(Z'\)、标量/赝标量 muonic bosons | PNS 缪子丰度、化学势、空间分布和输运方法 | 轴矢量自旋 1 \(A'\) 的完整数值界限 |
| Foldenauer & Hoefken Zink 2024 | 矢量 \(L_\mu-L_\tau\) 白矮星 plasmon decay | WD neutrino emissivity 对 kinetic mixing 的敏感性 | 本文小 mixing benchmark 的直接排除曲线 |

特别注意：SN1987A 的 \(L_{\rm new}\lesssim3\times10^{52}\,\mathrm{erg/s}\) 是常用 Raffelt free-streaming criterion。它不是完整的全耦合区排除；当耦合增大、粒子可能被吸收或陷获时，必须计算光学深度、逆过程、径向输运和能量沉积。也不能把“自由流阈值”直接称为“模型完整排除”。

---

## 7. 对 Major Point 4.4 的建议处理

### 7.1 现有回复的主线是正确的，但应坚持以下边界

当前正式回复已经采用以下逻辑：
1. 承认 sub-GeV 区域的 SN cooling 与本文相关；
2. 说明本文中微子流与常规 \(L_\mu-L_\tau\) 相同；
3. 在 \(10\,\mathrm{MeV}\lesssim m_{A'}<2m_\mu\) 区域，将矢量模型 SN cooling 作为 neutrino-coalescence 主导时的 reference scale；
4. 明确不把矢量模型完整曲线当成本文轴矢量模型的完整排除界限；
5. 解释半康普顿、轴矢量阈值宽度、LESN 和 kinetic mixing 的差别。

这一逻辑比笼统声称“恒星冷却无关”更有说服力，也与审稿人指定的文献直接对话。

### 7.2 不建议作出的主张

- 不要写“轴矢量模型没有 stellar-cooling bounds”或“SN1987A 不相关”。
- 不要将常规矢量 \(L_\mu-L_\tau\) 的完整 SN1987A/LESN 曲线直接画成本文模型的排除区域。
- 不要把 2019 年轴矢量核子报告当成本文轴矢量缪子流的计算。
- 不要把 Bell et al. 2024 中借用的 vector SN proxy 说成已完成的 axial SN recast。
- 不要把 \(\epsilon_{\rm ind}=0\) 的匹配条件解释成物理 kinetic mixing 在所有动量下为零。
- 不要把自由流 luminosity 阈值当作包括 trapping、diffusion 和 progenitor heating 的完整排除。
- 不要声称 \(m_{A'}>600\,\mathrm{MeV}\) 的整个区域已被所有 stellar constraints 排除或证明安全。

### 7.3 本轮最稳妥的科学表述

建议把“相关性”分为三个层级：

- **直接可复用：** \(A'\nu_\mu\nu_\mu\)、\(A'\nu_\tau\nu_\tau\) 树级耦合、neutrino coalescence 和不可见中微子部分宽度。
- **只能作为参考：** 常规矢量 \(L_\mu-L_\tau\) 的总 SN1987A cooling 参考尺度，特别是 \(m_{A'}\gtrsim10\,\mathrm{MeV}\) 的 neutrino-coalescence 主导区域。
- **需要轴矢量模型专属重算：** \(\mu\gamma\leftrightarrow\mu A'\)、纵向/横向模式、总宽度和 trapping、\(A'\to\mu^+\mu^-\) 后的 LESN 能量沉积，以及 in-medium kinetic mixing 相关的核子/等离子体过程。

如果本轮不做完整 SN 输运重分析，回复信就应明确采用“相关的矢量文献作为有边界的参考 + 精确指出相同的中微子子过程 + 解释轴矢量缪子过程不匹配”的策略。不要声称已经得到本文模型的全参数 SN1987A 排除曲线。

### 7.4 可供后续回复信使用的英文论证骨架

> Supernova constraints are relevant to the sub-GeV part of our parameter space. We distinguish the processes that are identical to those in the conventional \(L_\mu-L_\tau\) model from those that depend on the axial charged-muon current. In particular, the tree-level \(\nu_\mu\) and \(\nu_\tau\) currents are unchanged, so neutrino-coalescence production and the invisible neutrino partial widths agree at fixed \((m_{A'},g_X)\). In the cited SN profile, neutrino coalescence dominates the vector-model production luminosity above approximately \(10\,\mathrm{MeV}\), providing a well-defined reference scale below the dimuon threshold. By contrast, semi-Compton production and absorption depend on the charged-muon current, while the axial dimuon width has a \(\beta_\mu^3\) threshold suppression. These differences affect the polarization-resolved emissivity, optical depth, trapping, and progenitor energy deposition. We therefore use the published vector \(L_\mu-L_\tau\) results only for the matched neutrino-current comparison, rather than interpreting their complete exclusion contours as model-independent bounds on our axial benchmark.

This is a wording skeleton only. It should be used in the formal reply only after the authors decide which quantitative comparison and scope qualification to retain; it does not claim that a full axial SN transport calculation has been completed.

---

## 8. 对后续工作的最小、可控要求

若需要进一步加强 Major 4.4，建议按物理依赖顺序推进，而不是直接开展完整 UV 扫描：

1. 固定本文 benchmark 和同一 SN profile，先对照矢量参考文献复现 neutrino-coalescence 发射率及 \(A'\to\nu\bar\nu\) 衰变率。
2. 使用已建立的轴矢量 \(\mu\gamma\to\mu A'\) 振幅，完成介质静止系的热平均与横向/纵向分辨发射率。
3. 由详细平衡关系得到对应的吸收率，并逐模式核验；不能把 CM helicity 模式直接当作介质静止系的 T/L 模式。
4. 纳入轴矢量 \(A'\to\mu^+\mu^-\) 阈值宽度、不可见分支比、衰变长度和 inverse-decay opacity。
5. 只有在产生率、吸收率、光学深度和径向 SN profile 均一致后，才构造 model-specific SN1987A/LESN contour。

这不是当前文献调查已经完成的计算，而是若作者决定进行模型特定 recast 时的最小验收链。现有 PR #30 保存了部分解析振幅和数值原型，但完整输运和排除曲线仍未完成。

---

## 9. 完整参考文献与可核验来源

1. **Kahn, Krnjaic, Mishra-Sharma, Tait (2017).** “Light Weakly Coupled Axial Forces: Models, Constraints, and Projections.” JHEP 05 (2017) 002. [arXiv:1609.09072v2](https://arxiv.org/html/1609.09072v2), [DOI](https://doi.org/10.1007/JHEP05(2017)002). 重点：§2.4 关于轴矢量 \(A'\) 与 stellar cooling 的讨论。
2. **Lai, Lin, Tsai, Wu (2019).** “Constraints on Electromagnetic and Neutral Current Couplings of Dark Vector Boson to Standard Model Fermions by SN1987A.” EPS-HEP 2019 conference contribution. [CERN Indico abstract and slides](https://indico.cern.ch/event/577856/contributions/3423847/). 重点：\(Z_dNN\) 轴矢量耦合及 \(NN\) bremsstrahlung/反吸收。
3. **Bell, Newstead, Shaukat-Ali (2024).** “Cosmic-ray dark matter confronted by constraints on new light mediators.” Phys. Rev. D 109, 063034. [arXiv:2309.11003v2](https://arxiv.org/html/2309.11003v2), [DOI](https://doi.org/10.1103/PhysRevD.109.063034). 重点：§II 轴矢量核子介子，§IV SN proxy 的适用性说明。
4. **Lai, Leung, Lin (2024).** “SN1987A constraints to BSM models with extra neutral bosons near the trapping regime: \(U(1)_{L_\mu-L_\tau}\) model as an illustrative example.” Phys. Rev. D 110, 103023. [arXiv:2401.16023](https://arxiv.org/abs/2401.16023), [DOI](https://doi.org/10.1103/PhysRevD.110.103023).
5. **Croon, Elor, Leane, McDermott (2021).** “Supernova Muons: New Constraints on \(Z'\) Bosons, Axions and ALPs.” JHEP 01 (2021) 107. [arXiv:2006.13942](https://arxiv.org/abs/2006.13942), [DOI](https://doi.org/10.1007/JHEP01(2021)107).
6. **Caputo, Raffelt, Vitagliano (2022).** “Muonic boson limits: Supernova redux.” Phys. Rev. D 105, 035022. [arXiv:2109.03244](https://arxiv.org/abs/2109.03244), [DOI](https://doi.org/10.1103/PhysRevD.105.035022).
7. **Blinov et al. (2026).** “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae.” JHEP 06 (2026) 155. [arXiv:2511.09619v2](https://arxiv.org/html/2511.09619v2), [DOI](https://doi.org/10.1007/JHEP06(2026)155). 这是审稿人明确引用的主要文献。
8. **Wang, Zhang (2026).** “Revisiting supernova constraints on dark gauge bosons.” [arXiv:2610.35379v1](https://arxiv.org/html/2610.35379v1), [arXiv DOI](https://doi.org/10.48550/arXiv.2610.35379). 2026-10-26 预印本；当前检索版本不是已发表期刊文章。
9. **Foldenauer, Hoefken Zink (2024).** “How to rule out \((g-2)_\mu\) in \(U(1)_{L_\mu-L_\tau}\) with White Dwarf Cooling.” JHEP 07 (2024) 096. [arXiv:2405.00094](https://arxiv.org/abs/2405.00094), [DOI](https://doi.org/10.1007/JHEP07(2024)096). 重点：白矮星 plasmon decay 及 loop-induced kinetic mixing。
10. **Hardy, Lasenby (2017).** “Stellar cooling bounds on new light particles: plasma mixing effects.” JHEP 02 (2017) 033. [arXiv:1611.05852](https://arxiv.org/abs/1611.05852), [DOI](https://doi.org/10.1007/JHEP02(2017)033). 重点：光子混合在恒星等离子体中的处理。

## 10. 调查范围与状态说明

- 调查针对 arXiv、期刊原文和 CERN EPS-HEP 会议记录，优先检查原始论文，而非二手综述。
- “本轮未找到直接的轴矢量缪子流 SN1987A 完整数值重分析”是本次定向检索的结果，不等于证明相关文献绝对不存在。
- 本文档没有计算新的 SN luminosity、optical depth、trapping curve、LESN contour 或 WD emissivity。
- 本文档没有修改正式回复信或论文源码。
- 现有 PR #30 的半康普顿矩阵元和热率原型仍需按该 PR 中记录的验证条件处理；不能把文献适用性调查视为脚本通过或完整 SN 输运已完成。
