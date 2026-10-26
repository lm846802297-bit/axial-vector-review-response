# Higgs portal：低能 \(\mu,\tau\) 轻子圈对 \(h\)–\(s\) 混合自能的贡献

- **状态：** 研究工作文档；解析圈图表达式已整理，尚未完成重整化后的数值评估。
- **稿件基线：** 对照用户在本轮对话提供的 \(\texttt{main-v6.tex}\)，重点核对 Eq. \(\texttt{eq:gauge-basis-scalar-yukawa}\)、Eq. \(\texttt{eq:light-scalar-yukawa}\)、Eq. \(\texttt{eq:sm-limit-scalar-yukawa}\)、Eq. \(\texttt{eq:Lagrangian}\)、低能有效算符 Eq. (5d) 及标量 benchmark 段。
- **研究范围：** 先单独写出质量本征态中内部为轻子 \(\mu\) 或 \(\tau\) 的 \(h\)–\(s\) 二点图；不把该部分误称为完整 UV 模型的重整化自能。
- **用途：** 为 Major Point 1 中 Higgs–singlet portal 的审稿回复提供可复核的理论基础。本文档不是正式回复信，也不代表论文主文已经修改。

## 1. 从原稿确认的模型约定

### 1.1 标量场与 UV Yukawa 结构

原稿采用
\[
H=\frac{1}{\sqrt2}\begin{pmatrix}0\\v_h+h\end{pmatrix},
\qquad
S=\frac{v_s+s}{\sqrt2}
\]
（这里只展示与本计算相关的 CP-even 分量）。UV 拉格朗日量包含
\[
\mathcal L_{\rm UV}\supset
-y_\ell\bar L_\ell H E_{\ell R}
-\lambda_\mu S\bar E_{\mu L}\mu_R
-\lambda_\tau S^*\bar E_{\tau L}\tau_R
-M_{E\ell}\bar E_{\ell L}E_{\ell R}
+\mathrm{h.c.},
\]
其中第二、第三项的 \(S\) 与 \(S^*\) 来自原稿的 \(U_A(1)_{L_\mu-L_\tau}\) 荷分配。由于 \(S^*=(v_s+s-ia)/\sqrt2\)，对实 CP-even 场 \(s\) 而言，\(\mu\) 与 \(\tau\) 的对角标量耦合在原稿的实参数约定下均取同一符号；规范荷反转本身不把 CP-even 的 \(s\) Yukawa 符号翻转。

原稿的质量本征态标量相互作用写成
\[
\mathcal L_{\rm scalar}\supset
-y_{h\ell\ell}h\bar\ell\ell
-y_{s\ell\ell}s\bar\ell\ell+\cdots,
\qquad \ell=\mu,\tau,
\]
其中省略号包括轻—重非对角标量耦合。原稿对 \(\mu\) 的精确对角耦合为
\[
y_{h\mu\mu}=\frac{m_L}{v_h}c_Ls_R,
\qquad
y_{s\mu\mu}=\frac{m_R}{v_s}s_Lc_R.
\]
\(\tau\) 扇区由原稿规定的 \(\mu\to\tau\) 替换及相应规范荷反转得到。原稿在 seesaw-like 极限下使用
\[
y_{h\ell\ell}\simeq\frac{m_\ell}{v_h},
\qquad
y_{s\ell\ell}\simeq\frac{m_\ell}{v_s},
\qquad
y_{h\ell\ell}y_{s\ell\ell}\simeq
\frac{m_\ell^2}{v_hv_s}.
\]
以下先保留一般的实耦合 \(y_{h\ell\ell},y_{s\ell\ell}\)，仅在最后一步使用这一近似。

### 1.2 味结构

原稿在 benchmark 中设 \(y_{\mu\tau}=0\)，所以本文档计算的是两个独立的 flavor-diagonal 贡献
\[
\Pi_{hs}^{(\mu)}+\Pi_{hs}^{(\tau)}.
\]
在该 benchmark 下不存在需要把 \(\mu\) 与 \(\tau\) 交替放入同一闭合费米子圈的 flavor-changing 图。若之后放开 \(y_{\mu\tau}\)，必须重新检查质量本征态中的非对角 Yukawa 耦合及相应圈图；这不属于当前 benchmark。

### 1.3 原稿中的 portal 假设

原稿写出
\[
V(S)=-\mu_S^2|S|^2+\lambda_S|S|^4
\]
并在标量 decoupling benchmark 中假设 Higgs–singlet 混合可忽略；原稿没有在该处给出显式的
\[
\lambda_{HS}(H^\dagger H)(S^\dagger S)
\]
项、\(\lambda_{HS}\) 的匹配尺度或重整化边界。因此，“portal mixing negligible”在原稿中是 benchmark 假设，不是已经由 \(\mu,\tau\) 圈计算证明的结论。

在本文采用的势能约定下，若补入
\[
V(H,S)\supset \lambda_{HS}(H^\dagger H)(S^\dagger S),
\]
则破缺后树级非对角质量矩阵元为
\[
(\mathcal M^2_{\rm tree})_{hs}=\lambda_{HS}v_hv_s.
\]
此处的 \(\lambda_{HS}\) 归一化与上述 VEV 约定一致。

## 2. 轻 Dirac 费米子圈：解析表达式

### 2.1 自能与符号约定

采用标准 Passarino–Veltman 函数，并定义 \(-i\Pi_{hs}(p^2)\) 为插入标量二点函数的 1PI 图振幅。对一个颜色单态 Dirac 费米子 \(\ell\)，相互作用为
\[
\mathcal L_{\rm int}\supset
-y_{h\ell\ell}h\bar\ell\ell
-y_{s\ell\ell}s\bar\ell\ell.
\]
内部轻子圈的振幅为
\[
\begin{aligned}
-i\Pi_{hs}^{(\ell)}(p^2)
={}&(-1)(-iy_{h\ell\ell})(-iy_{s\ell\ell})\\
&\times\int\frac{d^dk}{(2\pi)^d}
\operatorname{Tr}\left[
\frac{i(\slashed{k}+m_\ell)}
{k^2-m_\ell^2+i0}
\frac{i(\slashed{k}+\slashed{p}+m_\ell)}
{(k+p)^2-m_\ell^2+i0}
\right].
\end{aligned}
\]
第一因子 \((-1)\) 是闭合费米子圈的负号。分子迹为
\[
\operatorname{Tr}\left[
(\slashed{k}+m_\ell)(\slashed{k}+\slashed{p}+m_\ell)
\right]
=4\left[k\cdot(k+p)+m_\ell^2\right].
\]

在下列标准归一化下，
\[
\int\frac{d^dk}{(2\pi)^d}\frac{1}{k^2-m^2+i0}
=\frac{i}{16\pi^2}A_0(m^2),
\]
\[
\int\frac{d^dk}{(2\pi)^d}
\frac{1}{(k^2-m^2+i0)((k+p)^2-m^2+i0)}
=\frac{i}{16\pi^2}B_0(p^2;m^2,m^2),
\]
得到
\[
\boxed{
\Pi_{hs}^{(\ell)}(p^2)
=\frac{y_{h\ell\ell}y_{s\ell\ell}}{16\pi^2}
\left[
4A_0(m_\ell^2)
+2(4m_\ell^2-p^2)B_0(p^2;m_\ell^2,m_\ell^2)
\right].
}
\]
该式对应本文明确给出的 \(-i\Pi\) 振幅约定；如果后续代码或文献采用相反的自能符号定义，应先转换约定再比较。颜色因子 \(N_c=1\)。

这里的 \(A_0\) 与 \(B_0\) 是未减除的维数正规化函数。可采用
\[
A_0(m^2)=m^2\left[
\Delta_{\rm UV}+1-\ln\frac{m^2}{\mu^2}
\right],
\]
\[
B_0(p^2;m^2,m^2)=
\Delta_{\rm UV}
-\int_0^1dx\,
\ln\frac{m^2-x(1-x)p^2-i0}{\mu^2},
\]
其中 \(\Delta_{\rm UV}\) 表示所选维数正规化约定下的 UV 极点组合。若采用不同的 \(d=4-\epsilon\) 或 \(d=4-2\epsilon\) 约定，\(\Delta_{\rm UV}\) 的记号会变化，但一致使用同一约定后物理结果不变。

### 2.2 \(\mu+\tau\) 的轻子对角圈贡献

在当前 benchmark 中，
\[
\boxed{
\Pi_{hs}^{\rm light,diag}(p^2)
=\Pi_{hs}^{(\mu)}(p^2)+\Pi_{hs}^{(\tau)}(p^2).
}
\]
代入原稿的 seesaw-like 近似，得到未减除的表达式
\[
\begin{aligned}
\Pi_{hs}^{\rm light,diag}(p^2)
\simeq \frac{1}{16\pi^2v_hv_s}
\sum_{\ell=\mu,\tau}m_\ell^2
\bigg[
&4A_0(m_\ell^2)\\
&+2(4m_\ell^2-p^2)
B_0(p^2;m_\ell^2,m_\ell^2)
\bigg].
\end{aligned}
\]
这是**轻子对角泡图的未减除部分**，不是已重整化的完整 \(h\)–\(s\) 混合自能。

在相同 seesaw-like 近似下，两代耦合乘积的比值为
\[
\frac{y_{h\tau\tau}y_{s\tau\tau}}
{y_{h\mu\mu}y_{s\mu\mu}}
\simeq\frac{m_\tau^2}{m_\mu^2}
\simeq 2.8\times10^2.
\]
因此，单从耦合乘积看，\(\tau\) 圈明显大于 \(\mu\) 圈。不过，完整自能之比还包含各自的 \(A_0\)、\(B_0\) 质量依赖，不能仅以这一比例代替数值评估。

## 3. 关键限制：轻子子集并非完整 UV 自能

### 3.1 轻子对角子集含有 UV 极点

按上述 PV 约定，
\[
\left.\Pi_{hs}^{(\ell)}(p^2)\right|_{\rm UV}
=\frac{y_{h\ell\ell}y_{s\ell\ell}}{16\pi^2}
(12m_\ell^2-2p^2)\Delta_{\rm UV}.
\]
其中与 \(p^2\) 成正比的项是重要警示：只保留轻子对角子集时，不能把该结果直接解释为完整 UV 理论中独立、可任意减除的 \(h\)–\(s\) 动能混合反项。原模型中 \(H\) 是电弱双重态、\(S\) 是规范单态；在未破缺的规范不变理论中，不存在一个普通的、可直接加入的维数四 \(H\)–\(S\) 动能交叉项来单独吸收该极点。

完整 UV 质量本征态计算包含轻—重与重—重内部费米子，以及质量本征态 Yukawa 矩阵的非对角项。它们不能只因为相应本征态质量大就从 UV 极点的抵消检查中删去。应在完整矩阵层面检查与
\[
\operatorname{Tr}(Y_hY_s^\dagger)
\]
相关的动能发散；由于原稿的 \(H\) 与 \(S\) Yukawa 在规范基底中连接不同的手征/场分量，该迹的结构与轻子对角子集不同。完整 UV 发散的抵消必须由完整场内容验证，不能由本节的轻子子集单独证明。

### 3.2 低能 EFT 中还有匹配产生的接触项

原稿 Eq. (5d) 的低能有效算符具有
\[
\mathcal L_{\rm EFT}\supset
-\frac{c_\ell}{\Lambda}S\,\bar L_\ell H\ell_R+\mathrm{h.c.},
\qquad
\frac{c_\ell}{\Lambda}\simeq
\frac{y_\ell\lambda_\ell}{M_{E\ell}}
\]
（\(\tau\) 项按原稿使用 \(S^*\)）。在破缺后，该算符不仅产生 \(h\bar\ell\ell\) 和 \(s\bar\ell\ell\) 三点耦合，也产生 \(hs\bar\ell\ell\) 接触相互作用。按领先阶质量关系，其量级为
\[
\mathcal L_{\rm EFT}\supset
-\frac{m_\ell}{v_hv_s}\,hs\,\bar\ell\ell
\]
（相位和复耦合的一般形式需从原始算符及其 Hermitian conjugate 展开；上式采用原稿的实参数约定）。

因此，若改用积分掉 \(E_\ell\) 后的 EFT 来计算一圈 \(h\)–\(s\) 二点函数，除了两个三点顶角形成的泡图，还必须核对这个接触顶角形成的费米子 tadpole，以及该 EFT 所需的高维反项/匹配系数。它们与完整 UV 理论中的轻—重图共同对应，不能把 EFT 的单个泡图等同于完整 UV 结果。

**当前处理原则：** 本文档先把三点顶角泡图单独列出，以便与通用文献公式对照；不声称它已经构成完整的低能 EFT 一圈答案。

### 3.3 Portal 参数与物理混合角

物理混合需要至少明确：
1. \(\lambda_{HS}\) 的匹配尺度、重整化方案及边界条件；
2. 与所选 EFT/UV 方案一致的反项和有限自能；
3. tadpole/VEV 的重整化约定；
4. 物理标量质量本征态的极点条件。

在非简并、弱混合的近似下，混合角的量级由非对角质量平方与 \(m_h^2-m_s^2\) 的比值控制；但在 \(m_s\simeq m_h\) 时必须处理完整的 \(2\times2\) 逆传播子，不能直接用非简并公式。当前原稿没有给出 \(\lambda_{HS}\) 的边界条件，所以单独计算本节的轻子泡图不足以证明完整混合很小。

## 4. 文献映射：哪些可以直接复用

### 4.1 主要计算参考

**M. Fox, W. Grimus and M. Löschner, “Renormalization and radiative corrections to masses in a general Yukawa model,”** *Int. J. Mod. Phys. A* 33, 1850019 (2018), [arXiv:1705.09589](https://arxiv.org/abs/1705.09589).

- 第 4 节 Fig. 2 与 Eq. (47a)：一般 Yukawa 模型中的标量二点自能，包含内部费米子图及 \(A_0/B_0\) 型参数积分结构。
- 第 6 节 Eq. (113)：说明 Dirac 费米子相对于该文 Majorana 约定的闭合圈因子与 Yukawa 矩阵替换规则。
- 可复用的内容：一般标量自能的推导框架、Dirac 圈的因子核查、UV 极点与标量场重整化的区分。
- 不能直接复用的内容：该文的模型参数、Yukawa 矩阵和完整质量谱不是本文的 \(U_A(1)_{L_\mu-L_\tau}\) universal-seesaw 模型。

### 4.2 辅助参考

1. **S. Kanemura, M. Kikuchi, K. Sakurai and K. Yagyu, “Gauge invariant one-loop corrections to Higgs boson couplings in non-minimal Higgs models,”** [arXiv:1705.05399](https://arxiv.org/abs/1705.05399). 用于核对 singlet-Higgs 混合参数、重整化与物理耦合的处理；不是本文轻子圈的直接数值结果。
2. **B. Batell, N. Lange, D. McKeen, M. Pospelov and A. Ritz, “The Leptonic Higgs Portal,”** [arXiv:1606.04943](https://arxiv.org/abs/1606.04943). 用于对照轻子 portal 的低能有效算符与 UV 完备化；不能替代本文具体的 \(h\)–\(s\) 自能。
3. **G. Hiller, C. Hormigos-Feliu, D. F. Litim and T. Steudtner, “Model building from asymptotic safety with Higgs and flavor portals,”** [arXiv:2008.08606](https://arxiv.org/abs/2008.08606). 用于对照 portal RG 与标量混合的理论框架；其场内容和 Yukawa 结构与本文不同，不能直接移植所有 RG 项或阈值。

## 5. 后续计算清单

| 编号 | 任务 | 状态 | 关闭标准 |
|---|---|---|---|
| HP-\(\mu\tau\)-01 | 从原稿抽取精确的 \(y_{h\ell\ell}\)、\(y_{s\ell\ell}\) 及相位约定 | **已完成：领先阶关系已核对** | 若数值扫描使用精确混合角，补入精确耦合而非仅用 \(m_\ell/v\) |
| HP-\(\mu\tau\)-02 | 写出内部为 \(\mu,\tau\) 的对角 Dirac 泡图 | **已完成：解析表达式已整理** | 独立代数/符号检查与 PV 约定复核 |
| HP-\(\mu\tau\)-03 | 评估轻子圈有限部分与吸收部 | **已完成 Plan B 条件性评估** | 两种低能匹配条件及数值表见 `Higgs_portal_planB_quantitative_assessment_2026-10-27.md`；完整 UV 混合仍未确定 |
| HP-\(\mu\tau\)-04 | 计算 EFT 的 \(hs\bar\ell\ell\) 接触 tadpole，并与泡图一起核对 | **已完成 Plan B 表达式与有限项** | 接触项来自 Eq. (5d)；已纳入 \\overline{\\mathrm{MS}}-like benchmark，MOM 条件下其常数部分由 \(\Pi(0)=0\) 减除 |
| HP-\(\mu\tau\)-05 | 检查完整 UV 质量本征态中轻—重、重—重图的 UV 极点抵消与 portal 阈值 | **未完成；当前未按用户优先级展开重图有限部分** | 至少用完整 Yukawa 矩阵证明极点抵消，并明确阈值是否影响 \(\lambda_{HS}\) |
| HP-\(\mu\tau\)-06 | 固定低能 portal/导数混合的示例重整化条件 | **部分完成；UV 匹配未完成** | MOM 与 \\overline{\\mathrm{MS}}-like 条件已明示；它们不是原稿推导出的 UV 边界条件，不能决定完整 UV 的总混合 |
| HP-\(\mu\tau\)-07 | 判断 Higgs portal 是否影响原稿 Fig. 2 的有效流 benchmark | **部分完成** | 低能轻子圈在远离简并区通常给出 \(10^{-4}\)–\(10^{-3}\) 的混合诊断量；完整 UV portal 匹配和近简并复数极点仍未评估 |
| HP-\(\mu\tau\)-08 | 将结果映射到 Major Point 1 的正式回复 | **暂缓** | 正文与数值结论同步后再改回复信完成时态 |

## 6. 暂定结论

1. 现有文献已提供一般 Yukawa 标量自能的计算框架。
2. Plan B 已完成两种低能匹配条件下的有限部分数值评估，并将 Eq. (5d) 的接触 tadpole 纳入 \(\overline{\mathrm{MS}}\)-like benchmark。
3. 在标量四次耦合上限 \(\lambda_S^{\max}=4\pi\) 仅约束 \(v_s\) 的条件下，远离 \(m_s=m_h\) 时低能轻子圈诊断量通常为 \(10^{-4}\)–\(10^{-3}\)；在简并点小混合展开失效，且宽度依赖 \(m_{A'}\) 与 \(v_s\)。
4. 两种匹配条件在简并示例中的实部结果不同，说明低能圈本身不能决定完整 UV 的总混合。要完整回应 Major Point 1.3，需要 Plan C-lite 的 portal/导数算符匹配及近简并复数极点分析。

## 7. Plan B 数值评估的摘要

完整输入、两种重整化 benchmark、数值表、EFT 接触 tadpole、近简并宽度示例和文献对照见 [Higgs_portal_planB_quantitative_assessment_2026-10-27.md](Higgs_portal_planB_quantitative_assessment_2026-10-27.md)。可复现脚本为 [higgs_portal_planB.py](higgs_portal_planB.py)。

在 \(m_s=m_h=125.25\,\mathrm{GeV}\)、仅使用原稿标量四次耦合上限给出的 \(v_s^{\min}=24.984\,\mathrm{GeV}\) 时，
\[
\widehat\Pi_{hs}^{\rm MOM}(m_h^2)=(0.5992-0.3211i)\,\mathrm{GeV}^2,
\]
\[
\widehat\Pi_{hs}^{\overline{\rm MS}+\mathrm{contact}}(m_h^2)
=(-0.2041-0.3211i)\,\mathrm{GeV}^2.
\]
吸收部在两种方案中相同；实部差异反映不同局域匹配条件，不能作为完整 UV 预测。原稿给出的 \(s\to A'A'\) 宽度公式还表明近简并处的 \(s\) 可能很宽，因此需要完整复数传播子。

**Plan B 结论：** 低能轻子圈远离简并区的贡献可以定量估算，但它不足以独立关闭 Major Point 1.3。若要声称完整 UV 模型的混合已得到定量控制，应继续进行有限范围的 Plan C-lite；论文主文和正式回复信暂不改写为“已解决”。


## 8. Plan C-lite follow-up: matched portal and complex poles (2026-10-27)

The Plan C-lite calculation is recorded in [Higgs_portal_planC_lite_matching_and_complex_poles_2026-10-27.md](Higgs_portal_planC_lite_matching_and_complex_poles_2026-10-27.md), with code in [higgs_portal_planC_lite.py](higgs_portal_planC_lite.py) and a separate [validation/limitation record](higgs_portal_planC_lite_validation.txt).

The portal boundary is now stated as \(\lambda_{HS}^{<}(M_E)=0\), which requires \(\lambda_{HS}^{>}(M_E)=-\Delta\lambda_{HS}^{E}\) to cancel the finite VLL threshold. This is an explicit reference benchmark, not a value predicted by the original manuscript. The finite derivative coefficient from RC-001 has been included with an explicit sign-convention conversion, but its full same-order EFT soft/counterterm closure and independent diagram-level validation remain open.

The first-pass complex-pole diagnostic shows two distinct cases: an open \(s\to A'A'\) channel gives a broad singlet-like pole and a nearly SM-width Higgs-like pole; a closed \(A'A'\) channel near exact degeneracy gives a narrow/broad pole pair with appreciable width redistribution. The near-degenerate region is therefore still **not assessed** by a model-specific Higgs lineshape or direct-search recast. These results do not upgrade the Plan-B low-energy estimates into a global UV prediction.
