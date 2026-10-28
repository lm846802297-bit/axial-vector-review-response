# Major Point 4.4：恒星冷却与超新星约束向轴矢量基准的转换

**日期：** 2026-10-28  
**研究分支：** `research/stellar-cooling-axial-recast-2026-10-28`  
**基准论文：** `overleaf-source/axial-vector-model-building-v6/main-v6.tex`（本轮未修改）  
**目的：** 回答审稿人“Are stellar cooling bounds not relevant? See e.g. 2511.09619”并明确矢量 \(L_\mu-L_\tau\) 结果在本模型中的可转移范围。

## 0. 结论摘要

1. **不能把全部矢量 \(L_\mu-L_\tau\) 超新星排除曲线直接移植到本模型。** 本模型的中微子耦合与标准 \(L_\mu-L_\tau\) 基准相同，但带电 μ 子是轴矢量耦合；半康普顿产生、μ 子吸收、\(A'\to\mu^+\mu^-\) 衰变及其输运均不同。
2. **中微子部分可以解析地直接对应。** 在忽略中微子质量、固定同一 \(m_{A'}\) 和 \(g_X\) 时，\(\nu_\mu\bar\nu_\mu,\nu_\tau\bar\nu_\tau\to A'\) 的矩阵元及 \(A'\to\nu\bar\nu\) 部分宽度与标准矢量基准一致。对中微子聚合主导的产生区间，这为冷却与高能中微子分析提供了可靠的领先阶基准。
3. **低质量半康普顿区不能简单沿用矢量曲线。** 当 \(m_{A'}\lesssim10\,\mathrm{MeV}\) 时，最新矢量计算发现 \(\mu\gamma\to\mu A'\) 可主导产生。轴矢量流不守恒使纵向 \(A'_L\) 振幅通过 Goldstone 等价关系获得 \(m_\mu/m_{A'}\) 型增强。因此轴矢量冷却约束可能比矢量结果更强；确切系数和排除曲线必须由轴矢量矩阵元与输运重算确定。
4. **低能超新星（LESN）约束尤其依赖动能混合和衰变宽度。** 在本论文的零动能混合基准中，低于 \(2m_\mu\) 时 \(A'\) 近乎只衰变为中微子，不会像自然动能混合的矢量基准那样有效地通过 \(e^+e^-\) 向包层沉积能量。高于 \(2m_\mu\) 后，轴矢量 μ 子宽度在阈值附近按 \(\beta_\mu^3\) 关闭，而矢量宽度按 \(\beta_\mu\) 关闭，故 LESN 曲线需要重铸。
5. **当前完成的是文献核对、解析转换与可复现宽度计算，不是完整数值超新星重铸。** 现有论文没有提供可直接复用的完整轴矢量输运计算；公开矢量论文也未随文提供 SN profile 数值输入和可运行代码。没有依据把尚未重算的轴矢量曲线声称为已验证结果。

## 1. 本模型与矢量基准的耦合对应

规范论文的质量本征态相互作用为

\[
\mathcal L_{A'}\supset A'_\alpha\bar\mu\gamma^\alpha
\left(g_V^\mu-g_A^\mu\gamma^5\right)\mu ,
\]

\[
g_V^\mu=g_X\sin^2\theta_{\mu R},\qquad
g_A^\mu=-g_X\cos^2\theta_{\mu R}.
\]

在论文采用的 \(|\theta_{\mu R}|\le10^{-2}\) 基准下，\(|g_V^\mu/g_A^\mu|=\tan^2\theta_{\mu R}\lesssim10^{-4}\)，所以带电 μ 子近似纯轴矢量耦合。该小矢量比值不能作为整个超新星约束的抑制因子，因为中微子顶角并不按此比例变小。

由电弱双重态的 \(U_A(1)_{L_\mu-L_\tau}\) 荷，本模型的中微子相互作用为

\[
\mathcal L_{\nu A'}=
g_X A'_\alpha\left(
\bar\nu_\mu\gamma^\alpha P_L\nu_\mu
-\bar\nu_\tau\gamma^\alpha P_L\nu_\tau
\right).
\]

标准矢量 \(L_\mu-L_\tau\) 模型的中微子耦合也是 \(\pm g_{\mu\tau}\)。在统一耦合归一化 \(g_{\mu\tau}=g_X\) 后，中微子部分逐项相同。这里“相同”指相同中微子顶角和相应的树级中微子过程，不表示总衰变宽度、总光度或完整排除曲线必然相同。

## 2. 可复核的解析结果

### 2.1 中微子部分宽度

对一个近似无质量、单一手征的中微子味道，

\[
\Gamma(A'\to\nu_\alpha\bar\nu_\alpha)
=\frac{g_X^2m_{A'}}{24\pi},
\qquad \alpha=\mu,\tau.
\]

因此两个味道合计为

\[
\boxed{\Gamma_{\nu\bar\nu}
=\frac{g_X^2m_{A'}}{12\pi}}.
\]

这与矢量 \(L_\mu-L_\tau\) 基准在相同耦合下的中微子总部分宽度一致。由详细平衡得到的中微子聚合产生率也相同，前提是采用相同的超新星温度、化学势、极化求和和几何处理。

### 2.2 μ 子衰变宽度：精确的树级转换

定义

\[
r_\mu=\frac{m_\mu^2}{m_{A'}^2},\qquad
\beta_\mu=\sqrt{1-4r_\mu}.
\]

在 \(m_{A'}>2m_\mu\) 时，标准矢量基准的 μ 子部分宽度为

\[
\Gamma_V(A'\to\mu^+\mu^-)
=\frac{g_X^2m_{A'}}{12\pi}
(1+2r_\mu)\beta_\mu.
\]

本模型纯轴矢量极限的对应宽度为

\[
\boxed{\Gamma_A(A'\to\mu^+\mu^-)
=\frac{g_X^2m_{A'}}{12\pi}\beta_\mu^3}.
\]

因此

\[
\boxed{\frac{\Gamma_A}{\Gamma_V}
=\frac{1-4r_\mu}{1+2r_\mu}}.
\]

对论文的有限混合定义，树级 μ 子宽度系数应写为

\[
\Gamma_{\mu\mu}
=\frac{g_X^2m_{A'}}{12\pi}\beta_\mu
\left[
\sin^4\theta_{\mu R}(1+2r_\mu)
+\cos^4\theta_{\mu R}(1-4r_\mu)
\right].
\]

此式保留了小矢量分量；在一般离阈值区域，其修正被 \(\sin^4\theta_{\mu R}\lesssim10^{-8}\) 抑制。但任意接近阈值时，轴矢量项按 \(\beta_\mu^3\) 消失，而矢量项按 \(\beta_\mu\) 消失，因此精确阈值附近不能先将残余矢量项设为零再作相对误差估计。

若仅考虑两个无质量中微子味道和 μ 子对，纯轴矢量的中微子分支比为

\[
\mathrm{BR}_A(A'\to\nu\bar\nu)
=\frac{1}{1+\beta_\mu^3};
\]

标准矢量基准则为

\[
\mathrm{BR}_V(A'\to\nu\bar\nu)
=\frac{1}{1+(1+2r_\mu)\beta_\mu}.
\]

数值由随本报告提交的脚本 `计算脚本/stellar_cooling_axial_recast.py` 计算。示例结果：

| \(m_{A'}\) | \(\Gamma_A/\Gamma_V\) | 矢量基准 \(\mathrm{BR}_{\nu\bar\nu}\) | 轴矢量 \(\mathrm{BR}_{\nu\bar\nu}\) |
|---:|---:|---:|---:|
| 220 MeV | 0.053 | 0.711 | 0.979 |
| 250 MeV | 0.210 | 0.580 | 0.868 |
| 300 MeV | 0.404 | 0.530 | 0.737 |
| 600 MeV | 0.825 | 0.501 | 0.550 |

表格忽略电子耦合和其他衰变道，展示的是部分宽度的解析差异，不是完整超新星限制。它表明在 μ 子阈值附近，轴矢量 μ 子衰变被显著压低，中微子分支比相应提高；质量远高于阈值时，两种宽度逐渐接近。

### 2.3 纵向极化与 Goldstone 等价关系

对于纵向极化，能量远高于 \(m_{A'}\) 时有

\[
\epsilon_L^\alpha(q)\simeq\frac{q^\alpha}{m_{A'}}.
\]

轴流满足（忽略异常项及相位约定）

\[
q_\alpha\bar u(p')\gamma^\alpha\gamma^5u(p)
=2m_\mu\,\bar u(p')\gamma^5u(p).
\]

因此纵向振幅包含

\[
\mathcal M(A'_L)\ \propto\
\frac{2g_A^\mu m_\mu}{m_{A'}}
\,\bar u\gamma^5u.
\]

这与被吃掉的 Goldstone 模式对 μ 子的赝标量耦合相符。论文的对称性破缺关系 \(m_{A'}=2g_Xv_s\) 和 \(y_{s\mu\mu}\simeq m_\mu/v_s\) 给出相同的耦合尺度

\[
|y_G|\simeq\frac{2|g_A^\mu|m_\mu}{m_{A'}}
\simeq\frac{m_\mu}{v_s}.
\]

**重的径向标量 \(s\) 退耦不等于纵向 \(A'_L\) 退耦。** 不能因论文取 \(m_s\gtrsim10\,\mathrm{GeV}\) 就省略轴流不守恒引起的纵向模效应。

在低能半康普顿过程中，标准矢量基准的纵向截面在 \(m_{A'}\ll E_\gamma\ll m_\mu\) 时量级为 \(\sigma^L_V\sim\alpha g_X^2/m_\mu^2\)。轴矢量情形的 Goldstone 等价振幅则允许 \(\sigma^L_A\sim\alpha g_X^2/m_{A'}^2\) 的增强量级。因此在半康普顿主导且自由流近似适用的区域，耦合下限可能呈现

\[
g_{X,\mathrm{lim}}^A
\sim g_{\mu\tau,\mathrm{lim}}^V
\frac{m_{A'}}{m_\mu}
\]

的参数依赖（只表示领先量级，不是最终重铸公式）。精确的系数、相空间、谱平均、反应吸收和输运效应尚须从完整轴矢量矩阵元计算；不应把这个量级估算画成正式排除曲线。

## 3. 对照文献与各项约束的适用性

### 3.1 审稿人指定文献：Blinov et al., arXiv:2511.09619 v2

该文已发表于 *JHEP* 06 (2026) 155，DOI: [10.1007/JHEP06(2026)155](https://doi.org/10.1007/JHEP06(2026)155)。它研究标准矢量 \(L_\mu-L_\tau\) 模型，并包含：
- SN1987A 的自由流冷却与扩散冷却；
- 无高能超新星中微子信号的限制；
- 低能超新星包层的能量沉积；
- 中微子逆衰变、\(\mu\gamma\to\mu V\)、逆 μ 子衰变及其逆过程吸收；
- 超新星内部的中微子化学势、几何逃逸概率和引力效应。

其标准矢量基准报告的 SN1987A 冷却范围约为 \(1.4\times10^{-10}\lesssim g_{\mu\tau}\lesssim6.7\times10^{-7}\)，质量覆盖到约 \(300\,\mathrm{MeV}\)；LESN 范围约为 \(6.4\times10^{-12}\lesssim g_{\mu\tau}\lesssim9\times10^{-7}\)，质量覆盖到约 \(600\,\mathrm{MeV}\)。这些数字是矢量基准的文献结果，**不是本轴矢量模型的已验证限制**。

来源：
- [arXiv:2511.09619 v2 正文](https://arxiv.org/html/2511.09619v2)
- [JHEP 正式发表版本](https://link.springer.com/article/10.1007/JHEP06%282026%29155)

### 3.2 最新对照：Wang & Zhang, arXiv:2610.35379 v1

该预印本于 2026-10-26 提交，重新计算了矢量暗规范玻色子的 SN1987A 冷却与 LESN 能量沉积，并处理衰变和吸收的几何效应。对标准矢量 \(U(1)_{L_\mu-L_\tau}\) 基准，作者报告 SN1987A 冷却质量覆盖至约 \(300\,\mathrm{MeV}\)，LESN 覆盖至约 \(600\,\mathrm{MeV}\)。其自然动能混合选择为 \(\epsilon_{\mu\tau}\simeq-g_{\mu\tau}/70\)；文中也画出了 \(\epsilon_{\mu\tau}=0\) 的 LESN 对照曲线。

这一点对本模型十分重要：论文采用匹配尺度零动能混合，不能拿自然混合曲线作为最终答案。新文献也强调，在 \(m_{A'}\lesssim10\,\mathrm{MeV}\) 时半康普顿过程占主导，而 \(m_{A'}\gtrsim10\,\mathrm{MeV}\) 时中微子聚合更重要。

来源：[arXiv:2610.35379 v1 正文](https://arxiv.org/html/2610.35379v1)。该文是最新预印本，不是同行评审后的正式发表结果。

### 3.3 逐项转换矩阵

| 约束或过程 | 能否直接转换 | 本模型必须做的处理 |
|---|---|---|
| \(\nu_\alpha\bar\nu_\alpha\to A'\) 产生率 | **可以，领先阶直接对应** | 固定同一 \(g_X\)，沿用相同的中微子分布、化学势和极化求和 |
| \(A'\to\nu\bar\nu\) 部分宽度 | **可以，解析相同** | 使用 \(\Gamma_{\nu\bar\nu}=g_X^2m_{A'}/(12\pi)\) |
| 中微子主导的 SN1987A 自由流冷却下边界 | **可作领先阶基准，不等于完整曲线** | 确认该质量区间中微子聚合占主导；重新处理总宽度、吸收和逃逸概率 |
| 高能 SN1987A 中微子 | **不能直接照搬完整曲线** | \(m_{A'}<2m_\mu\) 时中微子分支比近 1；高于阈值后用轴矢量总宽度、寿命和分支比重算通量 |
| 半康普顿 \(\mu\gamma\to\mu A'\) | **不能直接转换** | 重新计算轴矢量顶角的 \(T/L\) 极化矩阵元、费米阻塞、热平均及逆过程 |
| 逆 μ 子衰变 \(\mu^+\mu^-\to A'\) | **不能直接转换** | 由轴矢量 μ 子部分宽度及超新星 μ 子分布重新计算 |
| 高耦合 trapping / diffusion 边界 | **不能直接沿用** | 重新计算吸收光深、衰变、反应详细平衡与几何逃逸；纵向半康普顿增强可能改变上边界 |
| LESN，\(m_{A'}<2m_\mu\)，零动能混合 | **标准矢量曲线不适用** | 电子通道在该基准中不存在于树级；若 \(A'\) 只衰变到中微子，则缺少有效的带电末态包层能量沉积 |
| LESN，\(m_{A'}>2m_\mu\) | **必须重铸** | 采用 \(\Gamma_A\propto\beta_\mu^3\)，近阈值的 μ 子能量沉积与矢量情形不同 |
| 白矮星等普通恒星的电子/光子冷却 | **标准矢量界限不能直接照搬** | 普通恒星内热 μ 子丰度极低；本基准无树级电子耦合且一圈奇宇称矢量—轴矢量两点混合为零。需将更高圈或重态阈值诱导的动能混合单独作为 UV 修正核查 |

注意：上述“零动能混合”是本论文所选的匹配条件及简并重态基准。它不等于对任意 UV 参数或任意高圈阶次证明动能混合恒等于零。

## 4. 参数空间含义：目前能与不能下的结论

论文图的展示窗口为 \(10^{-3}\,\mathrm{GeV}\le m_{A'}\le10^2\,\mathrm{GeV}\)、\(10^{-6}\le g_X\le10^{-1}\)。矢量文献中超新星限制主要位于亚 GeV 质量区，但不能仅凭其自由流下边界低于图的 \(g_X\) 下限，就断言整个矢量排除带或轴矢量排除带都在图外。冷却约束通常具有自由流与 trapping 两侧边界；最新矢量预印本报告的 trapping 上边界与旧曲线存在差异，轴矢量半康普顿增强也可能移动边界。

因此当前可支持的参数空间结论是：

- \(m_{A'}\gtrsim10\,\mathrm{MeV}\) 的中微子主导产生率可直接借用作领先阶核验；
- \(m_{A'}\lesssim10\,\mathrm{MeV}\) 的轴矢量半康普顿通道可能增强，必须单独重算，不能声称恒星/超新星冷却无关；
- 零动能混合使 \(m_{A'}<2m_\mu\) 的 LESN 带电末态能量沉积机制与自然混合矢量模型不同；
- \(m_{A'}>2m_\mu\) 的 μ 子阈值附近，轴矢量衰变宽度与中微子分支比显著不同，LESN 和高能中微子限制都需要重新计算；
- 在完成这些重铸前，不把任何尚未检查的区域标记为“允许”。

## 5. 可复现计算与验证范围

脚本 `计算脚本/stellar_cooling_axial_recast.py` 仅计算树级解析宽度、衰变分支比与矢量—轴矢量比值。它不读取或拟合超新星数据，不生成官方或模型专属的排除曲线。

应将后续工作分为两个层次：
1. **本 PR 已完成：** 文献版本核对、耦合映射、衰变宽度解析推导、阈值行为、纵向模的参数依赖，以及约束逐项适用性判断。
2. **本 PR 尚未完成：** 完整的轴矢量半康普顿振幅与热平均、吸收光深、SN profile 数值积分、自由流/trapping 边界、扩散冷却与高能中微子/LESN 的联合重铸。公开对照论文未提供随文可运行的完整代码与全部 profile 输入；应先取得或独立重建这些输入，并进行详细平衡与极化求和验证。

## 6. 对审稿人的建议回复（须在完整数值重铸后定稿）

> We thank the referee for drawing our attention to Ref. [arXiv:2511.09619]. In our benchmark, the \(A'\) couplings to \(\nu_\mu\) and \(\nu_\tau\) are the same as in the conventional \(L_\mu-L_\tau\) vector benchmark, so neutrino coalescence and the \(A'\to\nu\bar\nu\) partial width agree at fixed \((m_{A'},g_X)\). The full supernova bounds cannot, however, be transferred without modification: the muon current is axial, which changes the semi-Compton production and absorption rates, the longitudinal-mode contribution, and the \(A'\to\mu^+\mu^-\) width. In addition, the low-energy-supernova energy-deposition bound depends on the kinetic-mixing assumption and the visible branching fractions.
>
> [Before submission, insert the axial-specific numerical comparison for SN1987A cooling, high-energy neutrinos and the zero-kinetic-mixing low-energy-supernova limit, and state whether the recalculated contours overlap the parameter domain shown in Fig. 2.]

这段是研究阶段的候选措辞。方括号中的数值任务完成前，不应将其作为最终、无占位符的审稿回复提交。

## 7. 参考文献

1. N. Blinov, P. J. Fox, K. J. Kelly, R. Plestid and T. Zhou, “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” *JHEP* 06 (2026) 155, [arXiv:2511.09619v2](https://arxiv.org/html/2511.09619v2), [DOI](https://doi.org/10.1007/JHEP06%282026%29155).
2. Z. Wang and Y. Zhang, “Revisiting supernova constraints on dark gauge bosons,” [arXiv:2610.35379v1](https://arxiv.org/html/2610.35379v1), submitted 2026-10-26.
3. D. Croon, G. Elor, R. K. Leane and S. D. McDermott, “Supernova Muons: New Constraints on \(Z'\) Bosons, Axions and ALPs,” *JHEP* 01 (2021) 107, [arXiv:2006.13942](https://arxiv.org/abs/2006.13942).
4. 规范模型源文件：[main-v6.tex](https://github.com/lm846802297-bit/axial-vector-review-response/blob/main/overleaf-source/axial-vector-model-building-v6/main-v6.tex)，尤其是轻 μ 子耦合式、动能混合基准和 \(m_{A'}=2g_Xv_s\) 的参数关系。


5. D. Das, P. Ghosh and R. Puri, “SN1987A Constraints of Light Z' with Non-Mixing Polarisations,” [arXiv:2606.23769](https://arxiv.org/abs/2606.23769), Eq. (14) for the low-mass semi-Compton transverse/longitudinal scaling.

## 8. 下一阶段：半康普顿振幅与极化分辨验证（2026-10-28）

### 8.1 完整树级振幅

对过程

\[
\gamma(k,\epsilon_\gamma)+\mu(p)\to\mu(p')+A'(q,\epsilon_{A'}),
\qquad p+k=p'+q,
\]

令

\[
\Gamma^\nu_{A'}=\gamma^\nu(g_V^\mu-g_A^\mu\gamma^5),\quad
s=(p+k)^2,\quad u=(p-q)^2.
\]

两个 μ 子交换图的振幅可写为

\[
\begin{aligned}
\mathcal M={}&e\,\epsilon_{\gamma\mu}\epsilon^*_{A'\nu}\,
\bar u(p')\Bigg[
\Gamma^\nu_{A'}\,
\frac{\not p+\not k+m_\mu}{s-m_\mu^2}\gamma^\mu\\
&\hspace{35mm}
+\gamma^\mu\,
\frac{\not p-\not q+m_\mu}{u-m_\mu^2}
\Gamma^\nu_{A'}
\Bigg]u(p).
\end{aligned}
\]

这条表达式保留有限 \(m_{A'}\) 的精确树级运动学，没有使用 \(E_\gamma\ll m_\mu\) 展开。随本报告新增的脚本 **计算脚本/stellar_semi_compton_axial_matrix_element.py** 用显式 Dirac 矩阵、外线旋量与物理极化向量直接计算该振幅，再对初态 μ 子自旋和光子偏振取平均、对末态 μ 子自旋及指定的 \(A'\) 偏振求和，并对实验室系散射角作 Gauss–Legendre 数值积分。

在初始 μ 子静止系，代码使用的微分截面为

\[
\frac{d\sigma}{d\Omega_{\rm lab}}
=\frac{|\mathbf q|}{64\pi^2m_\mu E_\gamma(m_\mu+E_\gamma)}
\overline{|\mathcal M|^2}.
\]

其中 \(\overline{|\mathcal M|^2}\) 对初态自旋和光子偏振平均，并保留相应的末态 \(A'\) 极化分量。数值积分只包含真空树级 \(2\to2\) 过程；尚未包括超新星热分布、μ 子末态 Pauli 阻塞、光子 Bose 因子、介质效应或星体径向积分。

### 8.2 电磁 Ward identity 的数值检查

把振幅中的入射光子极化替换为其四动量 \(\epsilon_\gamma^\mu\to k^\mu\)，应得到

\[
k_\mu\mathcal M^{\mu\nu}=0.
\]

脚本对纯矢量、纯轴矢量和混合耦合分别进行数值检查。以 \(E_\gamma=0.01\,\mathrm{MeV}\)、\(m_{A'}=0.001\,\mathrm{MeV}\)、\(\cos\theta=0.3\) 为检查点，最大残余约为 \(2.2\times10^{-9}\)（归一化耦合取 1），满足脚本采用的 \(10^{-7}\) 数值容差。有限残余来自浮点数中近似相消的分母与旋量运算，不是解析 Ward identity 的非零结果。

### 8.3 轴矢量纵向模的独立数值证据

物理纵向极化向量为

\[
\epsilon_L^\mu(q)=
\left(\frac{|\mathbf q|}{m_{A'}},
\frac{E_{A'}}{m_{A'}}\widehat{\mathbf q}\right),
\qquad q\cdot\epsilon_L=0,\quad \epsilon_L^2=-1.
\]

对轴矢量流，\(q_\nu\Gamma^\nu_{A'}\) 不像守恒的矢量流那样消失。高能极限下 \(\epsilon_L^\nu\simeq q^\nu/m_{A'}\)，纵向振幅因此与 Goldstone 等价关系相连，其有效赝标量耦合尺度为

\[
g_G\simeq \frac{2g_A^\mu m_\mu}{m_{A'}}.
\]

在规范模型的近纯轴矢量基准 \(g_A^\mu\simeq-g_X\)、\(m_{A'}=2g_Xv_s\) 下，这一尺度为 \(|g_G|\simeq m_\mu/v_s\)。所以 \(m_{A'}\) 变小、而 \(g_X\) 固定时，纵向半康普顿产生不能只按 \(g_X^2\) 作矢量模型的简单重标度；还必须同时检查由 \(v_s\) 决定的 Yukawa 耦合及其微扰性。

数值测试在固定 \(E_\gamma=10^{-3}\,\mathrm{MeV}\)、单位归一化 \(g_A=1\) 下，将 \(m_{A'}\) 从 \(0.2\,\mathrm{keV}\) 降到 \(0.1\,\mathrm{keV}\)，得到纵向截面增大约 \(4.12\) 倍，接近小质量极限的 \(1/m_{A'}^2\) 标度。该结果验证的是树级振幅的极化与质量标度，不代表物理耦合取 1 的参数点是微扰可行的，也不是超新星排除曲线。

### 8.4 对最新矢量文献的极化标签核验

Wang & Zhang 的最新预印本 [arXiv:2610.35379v1，第 5.2 节及附录 B](https://arxiv.org/html/2610.35379v1) 给出了矢量 \(L_\mu-L_\tau\) 半康普顿过程的低能极化分辨结果，Eqs. (58a,b) 与 (106a,b) 印出的形式是

\[
\sigma_{\rm printed}^{T}\propto
\frac{m_{A'}^2}{E_\gamma^2}\frac{1}{m_\mu^2},
\qquad
\sigma_{\rm printed}^{L}\to
\frac{8\pi\alpha\alpha_{\mu\tau}}{3m_\mu^2}
\quad(m_{A'}/E_\gamma\to0).
\]

然而，对守恒的纯矢量 μ 子流，独立的显式旋量计算在软光子、轻 \(A'\) 极限得到

\[
\sigma_V^T\longrightarrow
\frac{8\pi\alpha\alpha_X}{3m_\mu^2},
\qquad
\frac{\sigma_V^L}{\sigma_V^T}\longrightarrow0,
\quad \alpha_X=\frac{g_V^2}{4\pi}.
\]

这也是标准 Thomson 极限与 \(q_\nu\mathcal M^\nu=0\) 的预期：质量趋于零时，守恒矢量流的物理纵向发射被抑制，横向两偏振给出 Thomson 总截面。新脚本在 \(E_\gamma=10^{-4}\,\mathrm{MeV}\)、\(m_{A'}=10^{-7}\,\mathrm{MeV}\)、\(g_V=1\) 下得到 \(\sigma_T/\sigma_{\rm Thomson}=0.999998\)，且 \(\sigma_L/\sigma_T\simeq5.0\times10^{-7}\)。同一极限下，文献印出的两条表达式之和与精确总截面一致到约 \(2\times10^{-6}\)，但其占主导与受抑制的 **T/L 标签看起来与显式极化投影相反**；对被抑制的小分量，系数也不完全一致。

这一判断还有独立文献交叉核验：Das, Ghosh & Puri 的 [arXiv:2606.23769](https://arxiv.org/abs/2606.23769) 在其半康普顿极化分辨式（Eq. 14）中给出横向截面在 \(m_{A'}/\omega\to0\) 时不受抑制，而纵向截面乘以 \(m_{A'}^2/\omega^2\)，与本脚本的守恒矢量流软极限相符。两篇 2026 预印本的极化标签表现不一致，因此不宜静默沿用其中任一组 T/L 标签。

这应作为需要进一步核实的文献一致性问题，而不是在没有作者确认前断言 Wang & Zhang 的论文存在确定错误。2024 年 Lai, Leung & Lin 的原始工作 [arXiv:2401.16023](https://arxiv.org/abs/2401.16023) 给出低能半康普顿的**未分辨极化总截面**，不能独立确认 2026 年文献的 T/L 标签。实际 SN1987A 总光度可能对这一标签交换不敏感，因为总截面在该极限仍接近 Thomson 结果；但我们的轴矢量重铸恰恰依赖纵向模，因此必须先确认偏振约定或对照作者的计算实现，不能直接把印出的 T/L 分量当作已核验输入。

### 8.5 可复现测试结果与边界

运行命令：

~~~bash
python 计算脚本/stellar_semi_compton_axial_matrix_element.py --check
~~~

本地执行结果：

~~~text
checks=PASS
vector Ward residual (gV=1): 2.252e-09
axial Ward residual (gA=1): 2.159e-09
vector soft-limit sigma_T / Thomson = 0.999998
vector soft-limit sigma_L / sigma_T = 5.001e-07
axial sigma_L(M=0.1 MeV) / sigma_L(M=0.2 MeV) = 4.124194
~~~

该脚本是独立的树级振幅核查工具。它还没有将振幅与 arXiv:2610.35379 的所有有限质量表达式逐点对照，也没有做完整的热平均和超新星输运；后续必须在获得一致的 T/L 定义后再完成这一步。

### 8.6 下一步

1. 对照 arXiv:2610.35379 的 Eq. (77)、(101)–(106)，并尽可能联系作者或取得其计算代码，确认偏振标签与小质量极限的约定。
2. 将完整振幅热平均，加入 μ 子费米分布、末态 Pauli 阻塞和光子 Bose 分布，检查与详细平衡相容的吸收率。
3. 在相同的 SN profile 上分别计算矢量与轴矢量 T/L 产生率，核验 \(m_{A'}\) 与 \(v_s\) 的参数依赖，再做自由流、trapping 和 LESN 的数值积分。
4. 在上述计算完成前，不把该结果表述为已完成的轴矢量 SN1987A 或 LESN 排除曲线。


### 8.7 下一阶段热平均所需的精确相空间表达式

在给定超新星局部温度 \(T\) 和 μ 子化学势 \(\mu_\mu\) 后，按每个末态 \(A'\) 偏振 \(\lambda\in\{T_1,T_2,L\}\) 分辨的产生率应从热场论相空间积分开始：

\[
\begin{aligned}
\Gamma_{\mathrm{prod}}^\lambda(q)
={1\over 2E_q}\int&
d\Pi_p\,d\Pi_k\,d\Pi_{p'}\,
(2\pi)^4\delta^{(4)}(p+k-p'-q)\\
&\times\overline{|\mathcal M_\lambda|^2}
f_\mu(E_p)f_\gamma(\omega)
[1-f_\mu(E_{p'})],
\end{aligned}
\]

其中 \(d\Pi_a=d^3p_a/[(2\pi)^3 2E_a]\)，\(f_\mu(E)=[e^{(E-\mu_\mu)/T}+1]^{-1}\)，\(f_\gamma(\omega)=[e^{\omega/T}-1]^{-1}\)。对每个偏振，\(\overline{|\mathcal M_\lambda|^2}\) 需使用相同的初态自旋平均、光子偏振平均和末态偏振投影。发射的能量损失率随后为

\[
Q^\lambda=\int {d^3q\over(2\pi)^3} E_q\,
\Gamma_{\mathrm{prod}}^\lambda(q).
\]

在平衡浴中，利用能量守恒和 Fermi–Dirac/Bose–Einstein 分布的详细平衡关系，**对同一个偏振模式、采用一致的态计数约定**，

\[
\Gamma_{\mathrm{abs}}^\lambda(q)
=e^{E_q/T}\Gamma_{\mathrm{prod}}^\lambda(q).
\]

如果文献中的产生率是对三种末态偏振求和的总率，而吸收率是对初态 \(A'\) 偏振平均的率，则必须显式处理二个横向自由度与一个纵向自由度的计数，不能把总率公式中的 \(2/3\) 因子不加区分地搬到每个极化模式。

**当前代码还没有数值求解这一热相空间积分。** 现有半康普顿脚本在初态 μ 子静止系计算精确真空截面，并用软光子极限核验 Thomson 结果；它不包含 μ 子热运动、化学势、末态 Pauli 阻塞或 SN profile。下一步应先将矩阵元推广到任意初态 μ 子动量，再用热分布对产生率积分，并以逐偏振详细平衡关系检查逆过程。只有该局部产生率/吸收率模块通过验证后，才应嵌入超新星径向 profile 与几何逃逸积分。


## 9. 截面相空间修正与局部热产生率原型（2026-10-28）

### 9.1 修正实验室系微分截面的 Jacobian

在继续构造热平均时，重新从二体不变相空间推导了初始 μ 子静止系的微分截面。此前版本采用的简化分母只在软光子极限给出正确结果；它不足以支持一般有限入射能量下的定量积分。当前脚本已改为

\[
\frac{d\sigma}{d\Omega_{\rm lab}}=
\frac{e^2\overline{|\mathcal M/e|^2}\,|\mathbf q|^2}
{64\pi^2m_\mu E_\gamma
\left[|\mathbf q|(m_\mu+E_\gamma)-E_q E_\gamma\cos\theta_{\rm lab}\right]}.
\]

该式来自对末态 μ 子三动量积分后的能量 δ 函数，其 Jacobian 为
\[
\frac{\partial(E_q+E_{p'})}{\partial |\mathbf q|}
=\frac{|\mathbf q|}{E_q}
+\frac{|\mathbf q|-E_\gamma\cos\theta_{\rm lab}}{E_{p'}}.
\]

同时新增不变质心系表达式
\[
\frac{d\sigma}{d\Omega_{\rm CM}}
=\frac{e^2\overline{|\mathcal M/e|^2}}{64\pi^2s}
\frac{|\mathbf q_{\rm CM}|}{|\mathbf k_{\rm CM}|},
\]
并将其用于热平均。实验室系运动学现在还会拒绝不满足 (E_q\ge m_{A'}) 或末态 μ 子壳条件的角度；微分截面将不可达角度记为零。质心系没有近阈值实验室角度的可达区间问题，因而更适合对完整散射角积分。

独立 Python 复算（使用与仓库代码相同的 Dirac 旋量、振幅和运动学公式）得到：

- \(E_\gamma^*=1\,\mathrm{MeV}\)、\(m_{A'}=0.01\,\mathrm{MeV}\)、纯矢量单位耦合时，实验室系和 CM 系总截面分别为 \(4.277282601876\times10^{-7}\) 与 \(4.277282601877\times10^{-7}\,\mathrm{MeV}^{-2}\)，相对差约 \(1.4\times10^{-13}\)。
- 对 \(m_{A'}\ll E_\gamma^*\) 的矢量流，CM 数值积分与 Klein–Nishina 解析总截面在 \(E_\gamma^*=1\,\mathrm{MeV}\) 处相符至 \(4\times10^{-11}\) 的相对精度。
- 先前的软光子 Thomson 检查和轴矢量纵向 \(1/m_{A'}^2\) 标度对这一修正数值上基本不变；但任何有限能量截面都应以修正后的 Jacobian 结果为准。

这些数值来自独立的本地公式复算，并非直接运行 GitHub 中的脚本文件。仓库脚本已加入相应的自动测试（实验室系与 CM 系总截面一致性、Klein–Nishina 基准）；当前环境无法从 GitHub 拉取仓库，因此本轮尚未直接执行仓库脚本或 CI。

### 9.2 新增局部热积分原型

新增 **计算脚本/stellar_semi_compton_thermal_rate.py**。它对均匀、各向同性介质单元中的

\[
\mu^\pm+\gamma\to\mu^\pm+A'
\]

进行局部相空间积分，输入为 \(T,\mu_\mu,m_{A'},g_V^\mu,g_A^\mu\)，输出事件率密度 \(R\)（自然单位 \(\mathrm{MeV}^4\)）和能量发射率 \(Q\)（自然单位 \(\mathrm{MeV}^5\)）。可选的对数能量分箱（命令行参数 --spectrum-bins）还会输出按介质系 \(E_{A'}\) 分箱的事件率与能量发射率，便于后续研究谱依赖的吸收/逃逸。它包含：

- 初态 μ 子和反 μ 子的 Fermi–Dirac 分布，化学势分别为 \(+\mu_\mu\) 与 \(-\mu_\mu\)；
- 初态光子的 Bose–Einstein 分布；
- 初态相对通量因子 \(1-\beta_\mu\cos\psi\)；
- 末态 μ 子 Pauli 阻塞；
- 对 CM 散射角和方位角的数值积分，并在介质静止系计算 \(E_{A'}\)；
- 对初态 μ 子自旋与光子偏振的简并度计数。

CM 计算使用完整的 \(A'\) 物理偏振求和；这是总发射率的洛伦兹不变求和，不应与介质静止系下分别定义的纵向/横向吸收光深混为一谈。后者仍需单独实现。

### 9.3 热积分的几何检查与状态

独立复算已验证 CM 中介质四速度满足 \(U_{\rm CM}^2=1\)，入射光子满足 \(k_{\rm CM}\cdot U_{\rm CM}=\omega_{\rm medium}\)，并且任意测试角度下
\[
(p'_{\rm CM}+q_{\rm CM})\cdot U_{\rm CM}
=E_\mu+\omega_{\rm medium}.
\]
测试残差在双精度浮点数精度范围内。 独立复算还验证了四个对数能量 bin 的事件率之和与总事件率、能量发射率之和与总发射率一致到约 (10^{-15}) 相对差；该检查验证分箱记账，不代表热积分已经收敛。

一个低阶（\(N=2\)）独立 smoke test，在 \(T=10\,\mathrm{MeV}\)、\(\mu_\mu=0\)、\(m_{A'}=1\,\mathrm{MeV}\)、\(g_A^\mu=0.01\)、\(g_V^\mu=0\) 的纯数值基准下得到正的局部事件率与发射率，分别约为 \(3.09\times10^{-6}\,\mathrm{MeV}^4\) 和 \(7.87\times10^{-5}\,\mathrm{MeV}^5\)。该值仅验证积分结构能够产生有限正结果，不是物理 benchmark，也不用于实验约束。

进一步的独立本地积分探针在固定截断 \(p_{\max}=200\,\mathrm{MeV}\)、\(\omega_{\max}=100\,\mathrm{MeV}\) 下比较了 Gauss–Legendre 阶数 \(N=6\) 与 \(N=8\)：事件率从 \(1.88118\times10^{-6}\) 变为 \(1.88421\times10^{-6}\,\mathrm{MeV}^4\)，发射率从 \(7.14576\times10^{-5}\) 变为 \(7.15775\times10^{-5}\,\mathrm{MeV}^5\)，固定截断下的差异约为 0.2%。但在低阶计算中改变截断会引入约百分之一量级的变化，且与阶数误差耦合；因此这只是一项初步稳定性探针，不能称为已完成的截断收敛验证。

热积分脚本提供 --check，会执行四速度归一化、入射光子能量、末态能量守恒和低阶正率 smoke test。提交前仍需在仓库实际运行环境中执行：

~~~bash
python 计算脚本/stellar_semi_compton_axial_matrix_element.py --check
python 计算脚本/stellar_semi_compton_thermal_rate.py --check
~~~

还必须比较不同 Gauss–Legendre 阶数、动量截断和光子能量截断，建立收敛误差预算。当前没有把低阶积分结果当作收敛数值。

### 9.4 研究边界

这一步将研究从真空树级截面推进到局部热产生率的可计算框架，但仍不是完整的超新星冷却重铸。尚未实现或验证的项目包括：

1. 热积分对阶数、动量截断与光子能量截断的系统收敛；
2. 超新星介质中的 μ 子与光子色散关系、屏蔽和其他介质修正；
3. 与逐偏振吸收率一致的详细平衡、光深和 trapping 条件；
4. SN1987A 的径向温度、密度、μ 子化学势 profile 及体积分；
5. 低能超新星（LESN）可见衰变与能量沉积的模型特定重铸；
6. 将轴矢量曲线与论文 Fig. 2 的参数区域逐点比较。

因此，目前只能报告已推导的矩阵元、修正后的二体相空间公式和局部热积分原型；尚不能声称已经确定恒星冷却对论文参数空间的最终排除结论。
