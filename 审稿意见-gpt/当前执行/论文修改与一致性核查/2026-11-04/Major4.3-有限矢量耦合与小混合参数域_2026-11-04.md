# Major 4.3：有限矢量耦合与小混合参数域

日期：2026-11-04。用途：记录正式回复信的物理依据及正文同步要求；本文件是内部技术/修订记录，不属于给审稿人的回复正文。

## 1. 处理策略

本文的轴矢量现象学不覆盖任意有限轻重 VLL 混合角，而明确限定在 UV 模型的有限质量、小混合参数域
\[
|\theta_{\ell L}|,\ |\theta_{\ell R}|\leq10^{-2},
\qquad \ell=\mu,\tau.
\]
这不是把有限 VLL 质量误写成严格纯轴矢量，也不是声称所有矢量敏感实验均不存在；它是本文采用的研究域。正式回复应回答：在这一域中，诱导的矢量分量对本文实际使用的主要观测量是否会产生竞争性限制，以及什么条件下某个 vector-specific bound 才可能主导。

会议依据：2026-10-23 第三段文字稿 [03_文字稿_2026-10-23_21-29.md]，尤其 [05:11]–[06:14]。会议已把 \(\theta_R\lesssim10^{-2}\) 作为保守小混合基准，理由是 \(A'\) 对角耦合的修正由混合角平方控制。研究决策登记表 DEC-08 已采用相同参数范围。

## 2. 有限 VLL 质量与耦合关系

原始 UV 质量矩阵给出
\[
m_\ell\simeq\theta_{\ell L}\theta_{\ell R}M_{E\ell},
\]
以及右手混合角在重态极限下的近似
\[
\theta_{\ell R}\simeq \frac{m_{R\ell}}{M_{E\ell}}.
\]
因此小混合角并不要求 \(M_E=\infty\)，而是选取有限的多 TeV VLL 质量和相应的质量矩阵参数。若取简并 VLL 且同时饱和两个角度上限，\(\tau\) 质量给出
\[
M_E\simeq \frac{m_\tau}{10^{-4}}\simeq17.8~\mathrm{TeV}.
\]
这与原 benchmark 的 \(M_E>10~\mathrm{TeV}\) 相容；更小的混合角对应更大的、仍为有限值的 \(M_E\)。

轻态 \(A'\) 对角相互作用为
\[
\mathcal L_{A'}^{\ell}
=A'_\alpha\bar\ell\gamma^\alpha
\left(g_X\sin^2\theta_{\ell R}
-g_X\cos^2\theta_{\ell R}\gamma_5\right)\ell.
\]
故
\[
g_V^\ell=g_X\sin^2\theta_{\ell R},\qquad
g_A^\ell=-g_X\cos^2\theta_{\ell R},
\]
以及
\[
\left|\frac{g_V^\ell}{g_A^\ell}\right|
=\tan^2\theta_{\ell R}
\leq\tan^2(10^{-2})
\simeq1.0001\times10^{-4}.
\]
因此矢量耦合相对轴矢量耦合被压低约四个数量级。按当前 Fig. 2 纵轴上限 \(g_X=1\)，有 \(|g_V^\ell|\lesssim10^{-4}\)；在 \(g_X=0.1\) 的参考归一化点，有 \(|g_V^\ell|\lesssim10^{-5}\)。轻中微子树级耦合仍为 \(g_{\nu_\mu}=+g_X\)、\(g_{\nu_\tau}=-g_X\)。

## 3. 怎样判断 vector-specific 实验限制是否主导？

在固定 \(m_{A'}\)，且矢量/轴矢量实验限制使用可匹配的产生、衰变和接受度假设时，设
\[
|g_V^\ell|<g_{V,\mathrm{lim}}(m_{A'}),\qquad
|g_A^\ell|<g_{A,\mathrm{lim}}(m_{A'}).
\]
模型关系 \(g_V/g_A=\tan^2\theta_{\ell R}\) 将 vector-only 限制转成对共同 \(g_X\) 的限制。矢量限制弱于轴矢量限制的条件为
\[
\frac{g_{V,\mathrm{lim}}}{g_{A,\mathrm{lim}}}>
\tan^2\theta_{\ell R}.
\]
等价的混合角条件为
\[
|\theta_{\ell R}|<
\arctan\sqrt{\frac{g_{V,\mathrm{lim}}}{g_{A,\mathrm{lim}}}}.
\]

在本文采用的角度上限处，右侧阈值约为 \(1.0\times10^{-4}\)。因此，同质量点、同实验假设下，只有当 vector-specific coupling limit 比对应的 axial coupling limit 严格约四个数量级以上时，它才会产生更强的 \(g_X\) 限制。这个关系是判定标准，不是“所有可能实验都不存在矢量约束”的普遍定理。若实验的产生/衰变道、动量区间或接受度假设不同，必须先完成相应映射，不能直接比较两个模型图上的曲线。

角度阈值随实验和质量变化；没有给定 \(g_{V,\mathrm{lim}}(m)\) 与 \(g_{A,\mathrm{lim}}(m)\) 的同口径数据时，不得声称存在一个与实验无关的普适角度上限。本文采用 \(\theta_{\ell R}\leq10^{-2}\) 作为受控的 UV benchmark，并对本文实际使用的主要 observables 作显式比较。

| vector-only 限制相对 axial 限制的强度 | 要求的近似角度上限 |
|---:|---:|
| \(10^2\) 倍更严格 | \(|\theta_R|\lesssim10^{-1}\) |
| \(10^3\) 倍更严格 | \(|\theta_R|\lesssim3.2\times10^{-2}\) |
| \(10^4\) 倍更严格 | \(|\theta_R|\lesssim10^{-2}\) |
| \(10^5\) 倍更严格 | \(|\theta_R|\lesssim3.2\times10^{-3}\) |

## 4. 本文主要观测量的定量比较

### 4.1 Neutrino trident

同一动量转移下，领先标准模型干涉项的比例为
\[
\left|\frac{C_V\delta C_V}{C_A\delta C_A}\right|
\sim\frac{C_V}{C_A}\tan^2\theta_{\mu R}
\lesssim2.0\times10^{-4},
\qquad C_V\simeq0.96,\quad C_A=\frac12.
\]
该估计尚未包括矢量和轴矢量部分不同的有限 \(m_\mu\) 响应函数。它是两个领先干涉贡献之比，不是一个独立实验排除限。

### 4.2 Muon anomalous magnetic moment

\[
\left|\frac{\Delta a_\mu^V}{\Delta a_\mu^A}\right|
=\tan^4\theta_{\mu R}\frac{F_V(r)}{F_A(r)}
\lesssim2.1\times10^{-9},
\]
其中在本文质量范围内 \(F_V/F_A\leq0.20\)。这同样是过程贡献之比，而不是实验耦合上限。

### 4.3 Kinetic mixing

有限矢量分量也会诱导 photon–\(A'\) kinetic mixing。其匹配边界、动量依赖积分和 NA64 比较由 Major 4.2 单独处理；不能将 \(\epsilon_{\rm ind}(\mu_{\rm match})=0\) 解释为物理混合函数处处为零，也不能把这一 loop-induced electron coupling 与本节的 tree-level muon vector current 重复计数。

### 4.4 Visible dimuon width threshold

矢量和轴矢量 dimuon 部分宽度为
\[
\Gamma_V\propto(g_V^\mu)^2(1+2r_\mu)\sqrt{1-4r_\mu},
\qquad
\Gamma_A\propto(g_A^\mu)^2(1-4r_\mu)^{3/2},
\quad r_\mu=\frac{m_\mu^2}{m_{A'}^2}.
\]
因此
\[
\frac{\Gamma_V}{\Gamma_A}
=\tan^4\theta_{\mu R}\frac{1+2r_\mu}{1-4r_\mu}.
\]
对给定的相对贡献容许值 \(\eta\)，要求
\[
\frac{\Gamma_V}{\Gamma_A}<\eta
\]
等价于
\[
|\theta_{\mu R}|<
\arctan\!\left[
\eta^{1/4}
\left(\frac{1-4r_\mu}{1+2r_\mu}\right)^{1/4}
\right].
\]
因此阈值附近的角度要求依赖 \(m_{A'}\)；当 \(m_{A'}\to2m_\mu^+\) 时，轴矢量相空间因子下降得更快，任何非零固定角度都不能使 \(\Gamma_V/\Gamma_A\) 在整个阈值邻域内保持一致的小值。远离阈值时，\(\tan^4(10^{-2})\simeq10^{-8}\) 给出强烈抑制；极近阈值则必须使用完整有限角度宽度和分支比，不能只引用纯轴矢量近似。

## 5. 正式回复的结论边界

正式回复可支持以下结论：

1. 本文的轴矢量现象学明确限定在 \(|\theta_{\ell R}|\leq10^{-2}\) 的有限 VLL 小混合域，而非任意有限混合角。
2. 在该域中，\(g_V/g_A\lesssim10^{-4}\)；对本文明确比较的 trident 和 \((g-2)_\mu\)，矢量贡献分别约为 \(2.0\times10^{-4}\) 和 \(2.1\times10^{-9}\) 的轴矢量贡献。
3. 对同质量点且同口径的 vector-specific bound，只有当其耦合灵敏度比 axial bound 严格约四个数量级以上时，才可能改变共同 \(g_X\) 的限制；一般判据为 \(\tan^2\theta<g_{V,\mathrm{lim}}/g_{A,\mathrm{lim}}\)。
4. dimuon 阈值附近必须保留矢量/轴矢量宽度差异；不声称单一角度上限可以消除所有阈值敏感效应。
5. 不声称所有可能实验、所有可见衰变或整个 UV 参数空间的矢量限制都已排除；不将过程贡献比写成实验排除限。

不开展完整 vector-like phenomenology、全 UV 参数扫描或新增矢量排除图。本文既有二维轴矢量分析保留为上述小混合 benchmark 下的条件性结果。

## 6. 正文同步事项

- Eq. (27) 附近将 “conservative benchmark” 改为 “small-mixing assumption” 或等价表述，明确 \(10^{-2}\) 是本文选择的研究域，不是实验普适上限。
- 在轴矢量唯象学开始处说明该参数域；保留 \(g_V/g_A=\tan^2\theta_{\ell R}\)。
- 对 trident 与 \((g-2)_\mu\) 补充过程贡献比例，并明确不是实验排除限。
- 对 dimuon 宽度保留阈值因子；可见衰变的纯轴矢量解释只在宽度因子不造成显著增强的区域使用。
- Major 4.2 的 kinetic-mixing 结论独立保留，并与本节交叉引用。

本次 PR 只修改正式回复信和内部修订记录；不直接修改论文源码。正文同步状态仍按作者选定的活动稿及后续核验结果更新。
