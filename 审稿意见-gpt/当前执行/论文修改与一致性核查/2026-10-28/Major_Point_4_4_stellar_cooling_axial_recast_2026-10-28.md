# Major Point 4.4：恒星冷却与超新星约束向轴矢量基准的转换

**日期：** 2026-10-28  
**研究分支：** \`research/stellar-cooling-axial-recast-2026-10-28\`  
**基准论文：** \`overleaf-source/axial-vector-model-building-v6/main-v6.tex\`（本轮未修改）  
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

数值由随本报告提交的脚本 \`计算脚本/stellar_cooling_axial_recast.py\` 计算。示例结果：

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

脚本 \`计算脚本/stellar_cooling_axial_recast.py\` 仅计算树级解析宽度、衰变分支比与矢量—轴矢量比值。它不读取或拟合超新星数据，不生成官方或模型专属的排除曲线。

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
