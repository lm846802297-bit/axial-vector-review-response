# Major 4.2：动能混合与暗光子限制的对应关系

日期：2026-11-04。基线 main：`a78250e335452f8e72abccb67e1acd4a225b3896`（PR #41 已合并）。作者提供的说明要求利用已有圈图估计和暗光子实验限制回答 Major 4.2。本轮按此方向修改正式回复，保留计算过程；原论文源码和归档 bibliography 未改。

## 1. 可以引用哪个限制，为什么可以用

采用 **NA64 电子束、不可见暗光子搜索的 epsilon–mass 排除图**：Yu. M. Andreev et al. (NA64), *Search for Light Dark Matter with NA64 at CERN*, Phys. Rev. Lett. **131**, 161801 (2023)，[arXiv:2307.02404](https://arxiv.org/abs/2307.02404)，[DOI](https://doi.org/10.1103/PhysRevLett.131.161801)。本轮直接读取其 PDF 第 3 页 Fig. 3 和描述产生过程的正文；Fig. 3 是 90% CL 的 epsilon–mass 曲线。

此处映射的是电子产生和缺失能量信号。原论文中的暗物质热遗迹参数 y、alpha_D、m_chi 不用于本模型；A′ 的不可见末态可以是中微子。图中不同 dark-sector 宽度假设在共振产生区并非处处等价，本轮具体数值比较选在 100 MeV 的电子轫致辐射参考区域，没有搬用所有质量处的完整排除曲线。

| 对照项 | NA64 暗光子解释 | 本模型的对应量/条件 |
|---|---|---|
| 电子顶点 | e epsilon A′_alpha J_EM^alpha | 动能混合诱导同样的矢量电子顶点，epsilon=epsilon_gammaA′ |
| 产生 | eZ→eZA′，并在适当质量考虑次级正电子共振产生 | 在壳电子轫致辐射使用 epsilon(q²=m_A′²)，保留其动量依赖 |
| 不可见衰变 | Br_inv 接近 1 | m_A′<2m_mu 且新完成机制的额外道关闭时，主要衰变到中微子 |
| 实验比较 | 信号产额对 epsilon² Br_inv 的灵敏度 | 比较 epsilon 的模乘 √Br_inv 与 epsilon_lim(m_A′)，要求相应接受度适用 |
| muon current | 暗光子通过电磁流耦合 | 本模型还有直接轴矢量 muon current；这由 Fig. 2 的 NA64_mu 等独立约束处理 |

不能把可见暗光子 A′→e⁺e⁻ 的曲线直接当作此处主要限制：本模型电子可见分支比极小。也不能将 NA64 的暗物质热遗迹排除直接解释为本模型排除。

## 2. 参数化圈图与成立条件

使用 [Hapitas–Tuckler–Zhang, Phys. Rev. D 105, 016014 (2022), arXiv:2108.12440](https://arxiv.org/abs/2108.12440) Eq. (2.3) 的真空极化结构，替换其矢量耦合为本模型的 g_V=g_X sin²theta_R，并作 Q²→−q²−i0 的解析延拓。这里采用

\[
\theta_{\mu R}=\theta_{\tau R}=\theta_R,\quad
g_V^\mu=-g_V^\tau=g_X\sin^2\theta_R.
\]

结果为

\[
\epsilon(q^2)=-\frac{eg_X\sin^2\theta_R}{2\pi^2}\int_0^1dx\,x(1-x)
\log\frac{m_\tau^2-x(1-x)q^2-i0}{m_\mu^2-x(1-x)q^2-i0}.
\]

零动量时

\[
|\epsilon(0)|=\frac{e|g_X|\sin^2\theta_R}{6\pi^2}\log\frac{m_\tau}{m_\mu}
\simeq1.44\times10^{-7}\frac{|g_X|}{0.1}\left(\frac{\theta_R}{10^{-2}}\right)^2.
\]

固定非对角质量项 m_R 时 theta_R≈m_R/M_E，因此该项按 g_X m_R²/M_E² 衰减。拟合轻轻子质量后，不能把独立改变 M_E 且保持其他量不变的关系误当作整个 UV 参数空间的唯一轨迹。

重阈值抵消同时要求配对重态的质量简并、矢量耦合权重等大反号，并指定独立动能混合的匹配边界。仅有 |theta_lR|≤10⁻² 或仅有裸质量参数相等，并不足以证明上述数值对所有 UV 选择成立。回复将其明确为定量参考选择；不宣称已经算出非简并重谱或任意匹配条件下的总混合。

## 3. 不可见分支比和数值比较

在 m_A′<2m_mu、轻中微子质量可忽略、新道关闭时，两个带荷中微子味的总宽度为

\[
\Gamma_{\nu\bar\nu}=\frac{g_X^2m_{A'}}{12\pi},\qquad
\frac{\Gamma_{ee}}{\Gamma_{\nu\bar\nu}}
=\left|\frac{e\epsilon}{g_X}\right|^2(1+2r_e)\sqrt{1-4r_e}.
\]

电子道需高于其阈值。代入 100 MeV 在壳积分可得 |epsilon|/g_X=1.493865669×10⁻⁶、Gamma_ee/Gamma_nunu=2.0461×10⁻¹³，因此 Br_inv≈1。上述是给定场内容下的领先宽度，不是任意 UV 完成的总宽度结论。

对 NA64 Fig. 3，100 MeV 附近的限制在 10⁻⁴ 量级；本轮使用 **epsilon_ref=10⁻⁴ 作为数量级比较尺度**，没有数字化出精确的 90% CL 限值。不可把这一数字外推为整条质量曲线上的常数。

| 100 MeV 处 g_X | 本模型在壳动能混合幅值 | 相对 10⁻⁴ 参考尺度的混合比 | 相应产额比（相同接受度） |
|---|---|---|---|
| 10⁻⁴ | 1.494×10⁻¹⁰ | 1.494×10⁻⁶ | 2.232×10⁻¹² |
| 0.1 | 1.494×10⁻⁷ | 1.494×10⁻³ | 2.232×10⁻⁶ |
| 1 | 1.494×10⁻⁶ | 1.494×10⁻² | 2.232×10⁻⁴ |

后两行用于展示归一化和整个绘图矩形的保守尺度，不代表这些低质量、大 g_X 的点已经通过 g−2 或标量微扰性。由这些比较可以说明该参考质量区的电子产生通道低于所引用实验的灵敏度，不能据此宣布整个 UV 参数空间不受任何动能混合实验约束。

## 4. 与原回复/作者粘贴说明的修改对照

| 项目 | 修改前 | 本轮采用 |
|---|---|---|
| 实验对应 | 仅笼统写 invisible dark photon、NA64 约 10⁻⁴ | 指明 NA64 电子束，光子混合的 e epsilon 归一化、Fig. 3、90% CL、epsilon√Br_inv 映射 |
| 分支比 | 只说 predominantly neutrinos | 给出两味中微子总宽度、电子宽度及 100 MeV 的宽度比 |
| 代表性限制 | 容易把 10⁻⁴ 当作相关低质量区统一限值 | 锁定 100 MeV 附近，明确数量级比较，不给出虚假的精确数字化限值 |
| g_X=0.1 | Major 4.2、4.3 仍误称它为图的上限；作者粘贴说明沿用此值 | 保留作归一化示例，实际图上限 1 的估计乘十；同步修正 4.3 |
| VLL 抵消 | 容易仅从质量简并推出总动能混合为零 | 重态等大反号耦合权重、质量简并和匹配条件同时说明；轻 μ/τ 阈值差仍留下有限值 |
| 适用范围 | 结论容易读成全部参数范围普遍无影响 | 限定于等混合参考；其他质量、分支比、重阈值及匹配系数需相应处理 |

## 5. 原论文需要同步的内容

本轮未修改 `overleaf-source/axial-vector-model-building-v6/main-v6.tex`。以下均为待正文同步：

| ID | 源码位置 | 应增加/核对的内容 |
|---|---|---|
| K-01 | `eq:light-muon-Apr` 及 benchmark kinetic-mixing 段（原第 395–453 行附近） | 明示 g_V=g_X sin²theta_R；零匹配系数与物理 epsilon(q²) 的区别 |
| K-02 | VLL 简并和 kinetic-mixing 段 | 写清重态质量与耦合权重条件；补等混合角参考及一圈公式 |
| K-03 | 同段或简短附录 | 加 epsilon(0) 参数化式，100 MeV 在壳数值；需要时保留回复已有 timelike 表 |
| K-04 | 现有实验约束讨论 | 引用 NA64:2023lightDM 的电子束不可见结果，给出 e epsilon、Br_inv 和数量级比较 |
| K-05 | Fig. 2 及参数范围文字 | g_X=0.1 为归一化示例；图上限为 1；与 Major 2、4.3 一致 |

完整回复在根目录 TeX；计算入口为 [check_kinetic_dark_photon.py](../../../../计算脚本/Major42_kinetic/check_kinetic_dark_photon.py)，输出为 [JSON](../../../../计算脚本/Major42_kinetic/outputs/kinetic_dark_photon_2026-11-04.json)，核验结果见 [Major 4.2 验证记录](Major4.2-验证记录_2026-11-04.md)。本轮不引入新的实验排除曲线，也不需要改动 Fig. 2 本身。
