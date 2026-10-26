# Higgs portal 方案 B：\(\mu,\tau\) 轻子圈的定量评估与方案选择

- **状态：** Plan B 的低能轻子圈定量评估已完成；完整 UV portal 匹配和近简并物理极点尚未完成。
- **用途：** 决定 Major Point 1.3 是否能仅靠低能 \(\mu,\tau\) 圈的估算关闭，以及是否需要进入有限范围的 Plan C。
- **源稿基线：** 用户提供的 \(\texttt{main-v6.tex}\)，特别是 Eq. \(\texttt{eq:5-d}\)、Eq. \(\texttt{eq:light-scalar-yukawa}\)、Eq. \(\texttt{eq:sm-limit-scalar-yukawa}\)、Eq. \(\texttt{eq:scalar-partial-widths}\) 与 scalar-decoupling benchmark 段。
- **可复现脚本：** [\(\texttt{higgs\_portal\_planB.py}\)](higgs_portal_planB.py)。
- **范围声明：** 本文只量化低能、味对角 \(\mu,\tau\) 圈及 Eq. (5d) 对应的 \(hs\bar\ell\ell\) 接触 tadpole；不声称完成完整 UV 重整化或重矢量型轻子有限阈值计算。

## 1. 源稿提供的输入与约定

原稿在 seesaw-like 极限中给出
\[
y_{h\ell\ell}\simeq \frac{m_\ell}{v_h},
\qquad
y_{s\ell\ell}\simeq \frac{m_\ell}{v_s},
\qquad \ell=\mu,\tau,
\]
且 benchmark 设 \(y_{\mu\tau}=0\)。因此本次低能计算只包含两个独立的对角 Dirac 费米子圈，不含味变传播子。采用
\[
m_h=125.25~\mathrm{GeV},\quad v_h=246.22~\mathrm{GeV},
\quad m_\mu=0.1056584~\mathrm{GeV},\quad
m_\tau=1.77686~\mathrm{GeV}.
\]
这些是本次数值评估的输入，不是原稿给出的扫描结果。

原稿使用
\[
m_s^2=2\lambda_S v_s^2
\]
并以 \(\lambda_S\leq4\pi\) 作为示例标量微扰性条件。为最大化给定 \(m_s\) 下的轻子圈贡献，本次取
\[
v_s=v_s^{\min}(m_s)=\frac{m_s}{\sqrt{8\pi}}.
\]
因为轻子圈贡献正比于 \(1/v_s\)，任何更大的 \(v_s\) 都会按 \(v_s^{\min}/v_s\) 比例减小本次结果。这只是原稿标量四次耦合条件下的上包络，不是所有 UV 参数约束的联合扫描。

## 2. 两种明确的低能重整化 benchmark

轻子对角泡图的未减除表达式为
\[
\Pi_{hs}^{(\ell)}(s)=
\frac{m_\ell^2}{16\pi^2v_hv_s}
\left[
4A_0(m_\ell^2)+2(4m_\ell^2-s)
B_0(s;m_\ell^2,m_\ell^2)
\right],
\]
这里定义 \(-i\Pi_{hs}\) 为 1PI 二点图振幅。仅保留这组图会留下与常数项和 \(s=p^2\) 成正比的 UV 极点；它不能单独作为完整 UV 模型的自能。

因此，数值表明确比较两种不同的低能匹配条件：

### 2.1 零动量减除（MOM）benchmark

采用
\[
\widehat\Pi_{hs}(0)=0,\qquad
\widehat\Pi'_{hs}(0)=0.
\]
这等价于在该低能 benchmark 中把零动量质量混合和动能混合的局域系数设定为零。接触 tadpole 是动量无关项，已包含在 \(\widehat\Pi(0)=0\) 的条件中并被减除。于是
\[
\boxed{
\widehat\Pi_{hs}^{\mathrm{MOM}}(s)=
\frac{1}{16\pi^2v_hv_s}
\sum_{\ell=\mu,\tau}m_\ell^2
\left[
(8m_\ell^2-2s)\Delta B_0(s;m_\ell^2)
-\frac{4s}{3}
\right],
}
\]
其中
\[
\Delta B_0(s;m^2)=B_0(s;m^2,m^2)-B_0(0;m^2,m^2).
\]
对 \(s>4m_\ell^2\)，
\[
\Delta B_0(s;m^2)=
2-\beta_\ell\ln\frac{1+\beta_\ell}{1-\beta_\ell}
+i\pi\beta_\ell,\qquad
\beta_\ell=\sqrt{1-\frac{4m_\ell^2}{s}}.
\]

### 2.2 \(\overline{\mathrm{MS}}\)-like EFT benchmark

另取 \(\mu_{\rm sub}=m_h\)，并把该低能 EFT 中的重整化 portal 局域项及导数混合算符的重整化系数在此尺度设为零。该选择不是由原稿推导出的 UV 匹配条件，而是一个用于比较的明示 benchmark。

采用
\[
A_0^{\rm fin}(m^2)=m^2\left(1-\ln\frac{m^2}{\mu_{\rm sub}^2}\right),
\]
\[
B_0^{\rm fin}(s;m^2,m^2)=
-\ln\frac{m^2}{\mu_{\rm sub}^2}
+2-\beta\ln\frac{1+\beta}{1-\beta}+i\pi\beta.
\]
原稿的维数五算符 Eq. (5d) 在破缺后给出
\[
\mathcal L_{\rm EFT}\supset
-\frac{m_\ell}{v_hv_s}\,hs\bar\ell\ell.
\]
对应的费米子接触 tadpole 为
\[
\Pi_{hs,\mathrm{contact}}^{(\ell),\rm fin}
=\frac{4m_\ell^4}{16\pi^2v_hv_s}
\left(1-\ln\frac{m_\ell^2}{\mu_{\rm sub}^2}\right).
\]
因此本 benchmark 的结果为 bubble 的有限部分加上上述接触 tadpole。该 tadpole 对本次数值很小，但在定义一致的 EFT 自能时不能遗漏。常数有限项会随 portal 匹配条件改变；不能把两种方案的实部差异当成实验误差。

## 3. 数值结果：在 Higgs 极点 \(s=m_h^2\) 评估

定义远离简并区的诊断量
\[
\rho_{\rm mix}\equiv
\frac{|\widehat\Pi_{hs}(m_h^2)|}{|m_h^2-m_s^2|}.
\]
仅当 \(\rho_{\rm mix}\ll1\) 且宽度效应不重要时，它才近似于小混合角的量级；它不是近简并区的物理混合角，也不是完整 UV 预测。

| \(m_s\) [GeV] | \(v_s^{\min}\) [GeV] | \(|\Pi_{\rm MOM}|\) [GeV²] | \(\rho_{\rm MOM}\) | \(|\Pi_{\overline{\rm MS}+\mathrm{contact}}|\) [GeV²] | \(\rho_{\overline{\rm MS}}\) |
|---:|---:|---:|---:|---:|---:|
| 10 | 1.995 | 8.5145 | \(5.46\times10^{-4}\) | 4.7656 | \(3.06\times10^{-4}\) |
| 50 | 9.974 | 1.7029 | \(1.29\times10^{-4}\) | 0.9531 | \(7.23\times10^{-5}\) |
| 100 | 19.947 | 0.8515 | \(1.50\times10^{-4}\) | 0.4766 | \(8.38\times10^{-5}\) |
| 120 | 23.937 | 0.7095 | \(5.51\times10^{-4}\) | 0.3971 | \(3.08\times10^{-4}\) |
| 124 | 24.734 | 0.6867 | \(2.20\times10^{-3}\) | 0.3843 | \(1.23\times10^{-3}\) |
| 125 | 24.934 | 0.6812 | \(1.09\times10^{-2}\) | 0.3813 | \(6.09\times10^{-3}\) |
| 125.25 | 24.984 | 0.6798 | **失效** | 0.3805 | **失效** |
| 126 | 25.133 | 0.6758 | \(3.59\times10^{-3}\) | 0.3782 | \(2.01\times10^{-3}\) |
| 130 | 25.931 | 0.6550 | \(5.40\times10^{-4}\) | 0.3666 | \(3.02\times10^{-4}\) |
| 150 | 29.921 | 0.5676 | \(8.33\times10^{-5}\) | 0.3177 | \(4.66\times10^{-5}\) |

**解释：**

1. 在这两个明确的低能匹配 benchmark 下，远离 \(m_s=m_h\) 时，轻子圈给出的 \(\rho_{\rm mix}\) 通常在 \(10^{-4}\)–\(10^{-3}\) 量级；靠近简并点时，它迅速增长。
2. \(m_s=m_h\) 行的 “失效” 是小混合展开的分母为零，不表示物理振幅发散。物理问题必须用完整的复数 \(2\times2\) 逆传播子和极点条件处理。
3. 这些数字是仅由轻子对角圈、特定局域匹配条件和 \(v_s^{\min}\) 得到的条件性估计。不能将表格中的 \(\rho_{\rm mix}\) 当作完整 UV 混合角的上界，因为独立的 renormalized portal 参数尚未匹配。

## 4. 哪些结果不依赖实部的局域减除？

在 \(s=m_h^2\)、\(m_s=m_h\) 且 \(v_s=v_s^{\min}=24.984~\mathrm{GeV}\) 的示例中：
\[
\Pi_{hs}^{\mathrm{MOM}}
=(0.5992-0.3211i)~\mathrm{GeV}^2,
\]
而在 \(\overline{\mathrm{MS}}\)-like benchmark 下（包括 EFT 接触 tadpole）：
\[
\Pi_{hs}^{\overline{\mathrm{MS}}+\mathrm{contact}}
=(-0.2041-0.3211i)~\mathrm{GeV}^2.
\]
两种方案的实部相差约 \(0.803~\mathrm{GeV}^2\)，因为零动量减除与 \(\overline{\mathrm{MS}}\)-like 条件给出的局域有限项不同。这不是可随意忽略的数值差，而是提醒我们：**必须固定 portal 的物理匹配条件，才能预测总的实部混合。**

对给定的轻子耦合，吸收部则是同一物理切割的结果：
\[
\operatorname{Im}\Pi_{hs}^{(\ell)}(s)
=-\frac{y_{h\ell\ell}y_{s\ell\ell}}{8\pi}
s\left(1-\frac{4m_\ell^2}{s}\right)^{3/2}.
\]
在上述示例中，
\[
\operatorname{Im}\Pi_{hs}^{(\tau)}=-0.3200~\mathrm{GeV}^2,\qquad
\operatorname{Im}\Pi_{hs}^{(\mu)}=-0.00113~\mathrm{GeV}^2.
\]
因此，\(\tau\) 圈主导该低能吸收部，\(\mu\) 圈在此 benchmark 中很小。

## 5. 近简并区不能只用混合角分母判断

忽略宽度的简单诊断中，若要求 \(\rho_{\rm mix}\sim0.1\)，上述两种方案对应的质量差量级分别约为
\[
|m_s-m_h|\sim27~\mathrm{MeV}\quad(\mathrm{MOM}),
\qquad
|m_s-m_h|\sim15~\mathrm{MeV}\quad(\overline{\mathrm{MS}}\text{-like}).
\]
这些只是质量矩阵小混合展开的诊断尺度，不是实验排除区间，也不能用来定义最终的近简并排除窗。

更重要的是，原稿 Eq. \(\texttt{eq:scalar-partial-widths}\) 给出的 \(s\) 衰变宽度在此区域可能不窄。在 \(m_s=m_h\)、\(v_s=v_s^{\min}=24.984~\mathrm{GeV}\) 时：

- 若取示例 \(m_{A'}=10~\mathrm{GeV}\)，\(s\to A'A'\) 开放，\(\Gamma_{A'A'}\simeq30.14~\mathrm{GeV}\)，加上 \(\tau^+\tau^-\) 与 \(\mu^+\mu^-\) 后总宽度约 \(30.16~\mathrm{GeV}\)。
- 若取示例 \(m_{A'}=63~\mathrm{GeV}\)，\(s\to A'A'\) 关闭，以上轻子道给出总宽度约 \(25.3~\mathrm{MeV}\)。

两者均使用原稿给出的部分宽度公式；不同 \(m_{A'}\) 与更大的 \(v_s\) 会产生不同结果。这说明不能只按实质量差使用 \(\theta\simeq\Pi_{hs}/(m_h^2-m_s^2)\) 判断近简并物理。需要在明确 \(\lambda_{HS}\)、衰变道和参数输入后求解完整复数逆传播子。

## 6. 与 Higgs 数据的对照

PDG 2025 的 Higgs 综述总结，ATLAS 和 CMS 的整体 Higgs 信号强度分别约为 \(1.05\pm0.06\) 与 \(1.002\pm0.057\)，与 SM 相容（[PDG 2025, Status of Higgs Boson Physics](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-higgs-boson.pdf)）。在单一、窄、无额外衰变的简单 singlet 混合模型中，SM-like 标量的可见耦合普遍乘以 \(\cos\theta\)，因而可见信号强度近似乘以 \(\cos^2\theta\)。这说明 Higgs 信号强度确实会约束混合。

但该简单近似不能直接用作本文近简并区的数值排除：两个标量可能同时贡献于 125 GeV 附近的信号，且 \(s\to A'A'\) 可能改变宽度和分支比。近简并的多标量情形需在对应模型中进行信号强度拟合/重铸；可参考 [Robens and Stefaniak, “Two-real-scalar-singlet extension of the SM: LHC phenomenology and benchmark scenarios”](https://link.springer.com/article/10.1140/epjc/s10052-020-7655-x)，该工作明确逐点使用 HiggsSignals 处理近简并标量对观测信号的共同贡献。

本轮没有把通用 Higgs 信号强度精度转写为本文的精确 95% CL 混合角限制，也没有完成 HiggsSignals 或额外标量搜索的模型专属重铸。

## 7. 对现有论文结论的影响

### 7.1 可以保留的内容

- 现有 Fig. 2 仍可保留为明确限定的纯轴矢量有效流 benchmark 的约束图；本次计算没有重算或修改其数据。
- 可以保留“在小 portal 混合 benchmark 下，轴矢量唯象学近似独立”的研究策略，但必须把它写成**条件性假设**，而不是声称圈图已经证明完整 UV 模型的混合可忽略。
- 对远离 \(m_s=m_h\) 的低能轻子圈贡献，Plan B 给出了在两种明示低能匹配条件下的小混合诊断值。

### 7.2 尚不能声称的内容

- 不能声称 \(\lambda_{HS}\) 的 UV 阈值匹配已计算。
- 不能声称完整 UV 的 portal 混合在全部 \(m_s\) 区间都很小。
- 不能声称近简并区已被物理极点、宽度和实验数据完整评估。
- 不能把表中 \(\rho_{\rm mix}\) 当作完整 UV 混合角的全参数空间上界。

## 8. Plan B 是否足以关闭 Major Point 1.3？

**结论：Plan B 已给出有用的定量低能估算，但单独不足以完全关闭该审稿意见。**

原因有二：

1. \(\lambda_{HS}\) 是原稿未明确给出匹配条件的独立局域参数。轻子泡图的实部含有可被局域反项重定义的部分；两种合理的低能匹配条件在简并示例中给出不同的实部。因而低能轻子圈本身不能预测完整 UV 的总混合。
2. 近简并区域不仅要求完整的 \(2\times2\) 复数逆传播子，还要求用实际 \(m_{A'}\)、\(v_s\) 和开放衰变道确定 \(s\) 的宽度。原稿允许的参数区域中既存在 \(A'A'\) 开放也存在关闭的点，不能用一个通用窄宽度近似处理全部区域。

### 建议的最小扩展（Plan C-lite，而非完整扫描所有重图）

1. **先固定作者认可的 UV benchmark：** 明确 \(\lambda_{HS}\) 的匹配尺度与边界条件。若选择将其调到小混合，应将其如实标记为 UV 输入/条件性 benchmark。
2. **只做必要的 UV–EFT 局域匹配：** 确认 portal 的有限阈值和导数混合算符的匹配条件；不需要一开始就扫描所有重图的有限动量部分，但不能假定重 \(E_{\mu,\tau}\) 因为质量大就不会贡献任何局域阈值。
3. **仅在近简并子域求完整复数传播子：** 纳入 \(\Gamma_h\)、\(\Gamma_s\)、\(\Pi_{hh}\)、\(\Pi_{ss}\)、\(\Pi_{hs}\) 和 portal 输入，再决定是否需要直接搜索/HiggsSignals 重铸。
4. 若不愿做第 2–3 步，则只能采用更窄的论文范围：将近简并 UV 参数点标记为未评估，并把现有结果明确限定为小混合的条件性轴矢量 benchmark；这会减弱对 Major Point 1.3 的回应力度。

## 9. 当前交付与状态

- 已完成：轻子泡图两种低能匹配 benchmark 的解析表达式与数值评估；Eq. (5d) 的 \(hs\bar\ell\ell\) 接触 tadpole；\(\tau\) 与 \(\mu\) 的吸收部对照；近简并宽度敏感性示例；与现有 Higgs 信号强度精度的定性对照。
- 未完成：完整 UV 的 portal/导数算符阈值匹配、完整复数 \(2\times2\) 极点计算、模型专属 Higgs 约束重铸。
- 未修改：论文主文 \(\texttt{main-v6.tex}\)、Fig. 2 PDF/绘图源、正式回复信的结论性段落。
- PR #10 继续保持 Draft，未合并。

**决策：** 若要在回复信中宣称 Major Point 1.3 已被定量解决，应继续做 Plan C-lite。Plan B 的数字可作为该计算的低能对照基线，不应被包装成完整 UV 结果。
