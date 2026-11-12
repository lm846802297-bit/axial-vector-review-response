# Major 4.4：按轴矢量有效理论复用恒星冷却文献

调查与计算日期：2026-11-05。本文是内部研究记录与回复建议，不是正式回复信。

## 1. 本轮结论与作者澄清

作者明确指出：唯象学采用有效理论，因此参考文献不必具有与本文相同的 UV 完成；纯轴矢量以及矢量、轴矢量并存的 EFT 都可以借鉴。本文据此修订筛选标准：

\[
\mathcal L_{\rm EFT}\supset
 A'_\alpha\sum_f\bar f\gamma^\alpha(g_V^f+g_A^f\gamma^5)f
 +A'_\alpha\sum_i g_{\nu_i}\bar\nu_i\gamma^\alpha P_L\nu_i .
\]

对于给定过程，应匹配外线粒子、上述耦合、质量、归一化和近似条件。UV 场内容相同不是文献复用的前提。若讨论完整排除区域，还须匹配产生靶粒子、衰变、吸收及逃逸条件。

本轮得到三项可用成果：

1. **已有轴矢量自旋 1 的恒星冷却约束研究。** Alonso–Blas–Wolf（2019）和 Gori 等（2025）实际使用纵向模／Goldstone 映射给出轴矢量冷却限制。后一篇有 SN1987A 估算区域，不能再将现状概括成“没有轴矢量结果可用”。
2. **已有可直接采用的轴矢量半康普顿产生与逆吸收公式。** Liu–Miller（2017）给出精确真空树级电子公式；替换费米子质量与耦合即可用于缪子。本文已将其 Eq. (20) 与 PR #53 的独立显式自旋振幅做数值对照。
3. **已有可定量复用的低质量缪子冷却结果。** 将正确归一化的纵向模匹配到 Bollig 等修正版本的 ALP–muon 耦合，得到低质量、自由流边界的条件性估算。较大质量采用精确轴矢量核；不能把低质量近似延伸成全质量、全耦合排除。

本轮没有生成完整的轴矢量 SN1987A / LESN 排除轮廓，也没有改动正式回复 TeX、论文源码或 Fig. 2。

## 2. 文献与可复用内容对照

| 文献与原始入口 | 对象与具体位置 | 本项目采用方式 | 数值移植所需条件 |
|---|---|---|---|
| Liu & Miller, PRD 96 (2017) 016004, [arXiv:1705.01633](https://arxiv.org/html/1705.01633v1), [DOI](https://doi.org/10.1103/PhysRevD.96.016004) | 纯 V、纯 A 的自旋 1 EFT；§II.2 Eqs. (17), (19), (20)，§V Eqs. (33)–(36) | **直接采用产生核和逆过程归一化**；取电子质量为缪子质量、替换相应耦合 | 采用其真空精确 2→2 核；后续热分布、Pauli 阻塞、介质色散单独处理 |
| Alonso, Blas & Wolf, JHEP 07 (2019) 069, [arXiv:1810.00889](https://arxiv.org/html/1810.00889v2), [DOI](https://doi.org/10.1007/JHEP07(2019)069) | §5.1、Fig. 5：低质量轴矢量场及恒星冷却的纵向增强 | **采用轴矢量与 ALP 的匹配方法** | 文中的电子／核子数值改为缪子源项；不要求同一 UV |
| Gori et al., PRD 112 (2025) 075019, [arXiv:2506.11191](https://arxiv.org/html/2506.11191v1), [DOI](https://doi.org/10.1103/1r9r-n4sv) | §IV、Eqs. (50),(51)、Fig. 4：轴矢量 SN1987A 虚线估算区 | **采用 Goldstone 重标定加衰变逃逸检查的做法** | 原数值为夸克／核子耦合；换成缪子 ALP 源项和本文的中微子宽度 |
| Bollig et al., PRL 125 (2020) 051104；Erratum PRL 126 (2021) 189901；[整合修正版 v7](https://arxiv.org/html/2005.07141v7), [勘误](https://doi.org/10.1103/PhysRevLett.126.189901) | ALP–muon 超新星冷却；Eq. (1) 定义、Eqs. (3),(4) 产生、Eq. (11) 上限 | **采用修正后的低质量纵向估算** | 仅在纵向等效和自由流适用区使用；不把原 ALP 大耦合区直接当作本文排除 |
| Ferreira, Marsh & Ravensburg, Physics of the Dark Universe 53 (2026) 102435, [arXiv:2510.14469](https://arxiv.org/html/2510.14469v1), [DOI](https://doi.org/10.1016/j.dark.2026.102435) | ALP–electron/muon EFT；§II 耦合定义、§IV.1 有限质量 Compton、§V 冷却 | 补充 ALP 热率、质量效应和超新星剖面对照 | ALP 核只在纵向等效条件内重用；轴矢量有限质量全过程用 Liu–Miller 核 |
| Blinov et al., JHEP 06 (2026) 155, [arXiv:2511.09619v2](https://arxiv.org/html/2511.09619v2), [DOI](https://doi.org/10.1007/JHEP06(2026)155) | 审稿人指定论文；矢量型 \(L_\mu-L_\tau\)，§4.1–4.2 | **复用相同的中微子 EFT 子过程及能损／输运框架** | 缪子电流替换成 \(g_V^\mu,g_A^\mu\)；总排除图和通道主导质量区间需相应重评 |

补充定位：Kahn et al., JHEP 05 (2017) 002, [arXiv:1609.09072](https://arxiv.org/abs/1609.09072)，§2.4 可作轴矢量冷却相关性的背景引用。EPS-HEP 2019 的 [Lai–Lin–Tsai–Wu 报告](https://indico.cern.ch/event/577856/contributions/3423847/) 涉及核子 V+A，但不宜把会议报告中的核子排除线当作缪子限制。Baruch et al., JHEP 11 (2022) 124, [Axial vectors in DarkCast](https://arxiv.org/html/2206.08563v1)，是通用 V+A EFT 的实验重铸资源，未提供超新星输运解算器。这些工作均无需因 UV 不同而排除。

## 3. 直接采用 Liu–Miller 的轴矢量核

考虑
\[
\gamma(k)+\mu(p)\longrightarrow A'(q)+\mu(p'),\qquad
M=m_{A'},\quad m=m_\mu.
\]
采用 \(+---\) 度规并定义
\[
S=(p+k)^2-m^2,\quad U=(p-q)^2-m^2,\quad
t=(p'-p)^2,\quad S+U+t=M^2,
\]
\[
R=\frac{(S+U)^2}{SU},\qquad
B=m^2\left(\frac{S+U}{SU}\right)^2-\frac{t}{SU}.
\]
文献 Eq. (20) 转为本文记号后，
\[
\begin{aligned}
{\cal A}_{P}&=-R+2M^2B,\\
{\cal A}_{V}&=4-2R+4(M^2+2m^2)B,\\
{\cal A}_{A}&=4-\left(2+\frac{4m^2}{M^2}\right)R
                  +4(M^2-4m^2)B .
\end{aligned}
\]
初态自旋／光子偏振平均、末态自旋及三个 \(A'\) 偏振求和后，
\[
\overline{|{\cal M}|^2}
=e^2\big[(g_V^\mu)^2{\cal A}_{V}+(g_A^\mu)^2{\cal A}_{A}\big],
\qquad
\frac{d\sigma}{dt}=\frac{\overline{|{\cal M}|^2}}{16\pi S^2}.
\]

这里纯 V、纯 A 核来自文献；V+A 的组合是对这一非极化真空树级 2→2 过程的匹配：混合项的单个 \(\gamma^5\) 迹产生 Levi-Civita 收缩，而四个外线动量线性相关，因此干涉项为零。本轮另用正负混合耦合数值验证。这个结论不自动推广为任意极化可观测量或任意介质张量的性质。

**采用的是精确的 2→2 公式，不是该论文后面用于高能束流的 WW / improved-WW 近似。** 真空公式含完整质量与全部三个物理偏振；它不等同于已经包含热质量、plasmon 色散或介质静止系模式分辨的热率。

文献 §V 还给出逆吸收过程 \(\mu A'\to\mu\gamma\)。反向过程采用相应动量及通量，自旋 1 初态平均相对产生过程多出 \(2/3\) 因子；不能只把生产截面乘 \(2/3\) 就当作同一运动学下的吸收截面。逐偏振 opacity 必须保留相应模式，不能使用三态平均去替代纵向模的吸收率。

### 数值对照

参考实现取自 [PR #53](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) 的固定提交 e94fd051365eec508ac85bfd223c7531c0c64230。该模块直接用 Dirac 自旋子、传播子与偏振向量求振幅，并使用独立的 \(g_V,g_A\)，不依赖本轮文献公式。

7 个运动学点，各比较纯 V、纯 A、\((g_V,g_A)=(0.25,0.75)\) 和 \((0.25,-0.75)\)，共 28 项。最大相对差为 \(2.8801\times10^{-12}\)。完整数据见 [JSON](literature_kernel_validation.json)，执行器见 [脚本](check_literature_kernels.py)。

以下为本轮从文献核计算的同一运动学点上的比值，取两种纯耦合大小相同：

| 初态缪子静止系光子能量 / MeV | \(M\) / MeV | \(\cos\theta_{\rm CM}\) | \({\cal A}_A/{\cal A}_V\) | \({\cal A}_A/[(4m_\mu^2/M^2){\cal A}_P]\) |
|---:|---:|---:|---:|---:|
| 30 | 1 | -0.8 | 2130.10 | 1.00104 |
| 30 | 1 | 0 | 824.08 | 1.00547 |
| 30 | 1 | 0.8 | 18.87 | 1.09029 |
| 30 | 10 | 0 | 10.64 | 1.53359 |
| 100 | 50 | 0 | 2.90 | 3.45856 |
| 1 | 0.001 | 0 | \(1.9441\times10^6\) | 1.00000257 |
| 10 | 0.1 | 0.5 | 2796.74 | 1.00110 |

这些是差分矩阵元比值，不是总截面、发射光度或约束增强倍数。它们说明，轴矢量效应既可以直接计算，也不能普遍用常数乘矢量曲线表示；Goldstone 近似的相对精度还依赖运动学，靠近某一振幅零点时尤其要谨慎。

## 4. 采用已有轴矢量冷却映射，并给出本文的条件性数值

对高能外线纵向模，
\[
\epsilon_L^\alpha(q)=q^\alpha/M+O(M/E).
\]
利用轴流散度的树级质量项，可以写成等效 Goldstone 相互作用
\[
{\cal L}_{G\mu\mu}
=\frac{g_A^\mu}{M}\partial_\alpha G\,\bar\mu\gamma^\alpha\gamma^5\mu
\simeq -i\frac{2m_\mu g_A^\mu}{M}G\bar\mu\gamma^5\mu .
\]
因此
\[
\widehat g_{a\mu}\ \leftrightarrow\ \frac{|g_A^\mu|}{M},
\qquad
y_{a\mu}\ \leftrightarrow\ \frac{2m_\mu|g_A^\mu|}{M}.
\]
这里 \(\widehat g_{a\mu}\) 是不含 \(1/2\) 的导数耦合，单位 \({\rm GeV}^{-1}\)；\(y_{a\mu}\) 是无量纲赝标量 Yukawa 耦合。若文献定义为 \(C_\mu/(2f_a)\)，则 \(C_\mu/(2f_a)=g_A^\mu/M\)。此映射只使用 EFT，不要求给出 \(v_s\) 或新增中微子质量完成机制。

Alonso–Blas–Wolf 用过这一类纵向模冷却匹配。Gori 等将它实际用于轴矢量 SN1987A 估算：其 Eq. (50) 使用核子 ALP 上限，Eq. (51) 加入该模型的中微子衰变，Fig. 4 画出虚线区域。本文应采用这套方法，但输入缪子源项；该文的 \(g'\) 并非本文的 \(g_A^\mu\)，不能照搬其核子系数。

### 4.1 必须用修正后的 Bollig 数值

Bollig 等的整合修正版 v7 将修正的低质量结果写为
\[
\widehat g_{a\mu}<10^{-7.5}\ {\rm GeV}^{-1}
=3.1623\times10^{-8}\ {\rm GeV}^{-1}.
\]
其定义与上述导数耦合一致。早期常见的 \(10^{-8.1}\ {\rm GeV}^{-1}\) 不是应继续使用的最终数值；两者相差约 3.98 倍。修正版同时修正了热率中光子偏振计数及不恰当的低光子能量近似，并将所报质量范围截在 \(m_a=1\) MeV。

由此，本轮得到以下**纵向模、低质量、弱耦合自由流边界估算**：
\[
\boxed{\frac{|g_A^\mu|}{M}\ \lesssim\
3.16\times10^{-8}\ {\rm GeV}^{-1}}
\]
或
\[
\boxed{|g_A^\mu|\ \lesssim\
3.16\times10^{-11}\left(\frac{M}{\rm MeV}\right).}
\]
这是将原文冷却结果匹配到本文 EFT 的推论，不是 Bollig 原文已经计算了本文的轴矢量模型。宜在质量明显低于 1 MeV、产生的纵向粒子满足 \(E\gg M\) 的区域采用。接近 1 MeV 可作低质量参考；不能由此延伸到几十或几百 MeV。

| \(M\) | 对应 \(|g_A^\mu|\) 参考值 | 使用说明 |
|---:|---:|---|
| 1 keV | \(3.16\times10^{-14}\) | 低质量纵向参考 |
| 10 keV | \(3.16\times10^{-13}\) | 同上 |
| 0.1 MeV | \(3.16\times10^{-12}\) | 同上 |
| 1 MeV | \(3.16\times10^{-11}\) | 原 ALP 图的截断位置；作为边界参考，不宣称统一精度 |

对原论文近似纯轴矢量 benchmark，\(|g_A^\mu|\simeq |g_X|\)；若保留右手混合，则使用 \(|g_A^\mu|=|g_X|\cos^2\theta_{\mu R}\)，而不是重新定义耦合。

### 4.2 检查本文额外中微子衰变

本文两个活跃味的质量可忽略时，
\[
\Gamma_{\nu_\mu\bar\nu_\mu}+
\Gamma_{\nu_\tau\bar\nu_\tau}
=\frac{g_X^2 M}{12\pi}.
\]
该式来自相同的低能左手中微子流，可以与审稿人指定的矢量 \(L_\mu-L_\tau\) 文献共用；与 Gori 模型的 \(\Gamma_\nu=3g'^2M/(2\pi)\) 不同。

真空飞行长度为
\[
\ell_\nu=\hbar c\,\frac{12\pi\sqrt{E^2-M^2}}{g_X^2M^2}.
\]
例如取 \(M=0.1\) MeV、\(E=30\) MeV、\(g_X=3.16\times10^{-12}\)，得到
\[
\ell_\nu=2.23\times10^{12}\ {\rm km},
\]
远大于 10 km 量级。因而在这一低质量、极弱耦合参考点，中微子真空衰变不会立即消除逃逸能损。该检验不等同于完成介质吸收计算；增加其他耦合、改变质量或进入大耦合区时必须重新评估。

Bollig 的 ALP 自由流／trapping 结论不能整体赋给本文，因为本文还具有中微子产生、吸收和衰变通道。上面的直线标识低耦合能损边界的估算，不能把其右方全部涂成排除，更不能据此判断图中 \(g_X\gtrsim10^{-6}\) 区域的 trapping 或扩散行为。

### 4.3 新版 ALP 工作的用途

Ferreira–Marsh–Ravensburg 提供有限质量 ALP Compton 核及多种 SN 模型比较，可用于纵向极限的热率与不确定性核对。它并不让 Goldstone 等效在 \(M\sim E\) 时变成精确关系。ALP 的两光子衰变、相应 gamma-ray / LESN 曲线也不能经此替换自动赋给 spin-1 粒子：真空在壳自旋 1 粒子不能衰变为两个相同的在壳光子，圈图算符及异常匹配需针对实际 EFT 处理。

## 5. 如何使用审稿人给出的 2511.09619

该论文仍然是直接相关的输入。比较应落在有效电流和过程上：

| 内容 | 2511.09619 的矢量 benchmark | 本文 EFT | 处理 |
|---|---|---|---|
| \(\nu_\mu,\nu_\tau\) 左手流 | \(+g_X,-g_X\) | 相同 | 相同热背景与参数下复用中微子子过程与偏宽度 |
| 缪子半康普顿 | 矢量电流 | 主要轴矢量，可保留小矢量部分 | 用本轮已验证的文献 \(V+A\) 核替换 |
| 低质量纵向发射 | 守恒矢量流的行为 | 轴流质量项引入 \(m_\mu/M\) 增强 | 用精确核或受控 Goldstone 近似 |
| 能损与逃逸框架 | 产生率乘逃逸概率、空间及能量积分 | 相同类型的输运问题 | 复用组织框架，替换实际过程率 |
| 完整图、通道主导阈值 | 含各通道竞争与吸收 | 缪子源项发生改变 | 不能仅因中微子偏宽度相同就认定完整边界相同 |

特别是“约 10 MeV 以上由中微子聚合主导”一类陈述，应明确它属于参考文献的矢量 benchmark。没有比较轴矢量缪子率之前，不应把这个主导关系作为本文已验证事实。

普通低温恒星中的电子／光子冷却与含缪子的原中子星环境也应分别讨论。原论文没有树级电子／核子轴矢量耦合，因此电子或核子限制不能直接作为 \(g_A^\mu\) 的数值上限；这属于源项和 EFT Wilson 系数匹配，不是要求 UV 模型相同。圈图诱导电子／光子作用若纳入，使用相应已匹配系数。

## 6. 对原有处理思路的具体修订

| 原有表述或容易产生的理解 | 本轮应采用的表述 |
|---|---|
| 需找到与本文 UV 模型相同的冷却研究才能借用 | EFT 电流与过程可匹配就可借用；UV 同一性不是前提 |
| 缺少“本文完整曲线”，因此轴矢量相关结果只能泛泛引用 | 已有轴矢量冷却映射、SN 估算和精确产生／吸收公式，应实际采用 |
| 轴矢量半康普顿需要从头开发 | 直接使用 Liu–Miller Eq. (20)，现有自旋代码作为交叉核验 |
| ALP 只可定性类比 | 在 \(E\gg M\) 下可作有归一化的纵向匹配，并给出受条件限定的数值估算 |
| 核子或电子论文因“模型不同”而不相关 | 通用匹配方法可用；数值曲线按实际耦合粒子与源项转换 |
| 天体物理约束主要在较小耦合，所以本图不重要 | 先说明低耦合估算在哪个区域；大耦合区的 trapping、扩散与衰变不能由该直线判断 |
| 中微子流相同，所以 vector 完整曲线相同 | 中微子子过程相同；完整结果还依赖轴矢量缪子率、模式和逃逸 |
| 没有完全同样模型的结果即可断言“冷却无关” | 冷却相关；已有成果能支撑明确的 EFT 讨论与受控估算 |

## 7. 可用于下一次正式回复修订的英文科学段落

以下为候选科学段落，未写入正式回复或论文。不使用已经完成正文修改的措辞：

> Stellar-cooling constraints are relevant to the axial-vector effective interaction considered here. Their applicability is determined by the low-energy couplings and the production and escape processes, and does not require an identical ultraviolet completion. Axial-vector cooling estimates based on the longitudinal mode have been discussed by Alonso, Blas and Wolf and by Gori et al. In the relativistic longitudinal limit, our muon coupling matches onto a derivative pseudoscalar coupling with coefficient \(\widehat g_{a\mu}=|g_A^\mu|/m_{A'}\). The corrected low-mass result of Bollig et al. therefore provides the conditional free-streaming estimate \(|g_A^\mu|/m_{A'}\lesssim3.2\times10^{-8}\,\mathrm{GeV}^{-1}\), subject to the longitudinal approximation and escape conditions. This estimate applies below the MeV scale and does not specify the trapping boundary at larger coupling. For finite masses, the exact axial-vector semi-Compton matrix element is available from Liu and Miller and can be used with the muon mass and coupling. The neutrino subprocesses of Ref. [2511.09619] share our active-flavor effective current, whereas its vector muon production kernel must be replaced by the axial-vector one. Its complete exclusion contours consequently require this matching before they can be applied to our parameter space.

正式引用键应在选定的回复 bibliography 中核对后添加，避免在候选稿阶段虚构已完成的编译或正文同步。若正式回复没有空间呈现低质量条件和参考值，至少应保留“已有轴矢量研究 + EFT 归一化 + 与审稿文献的过程对照”。

## 8. 复现与证据边界

本目录提供：

- 本调查报告：README.md。
- 已发表核与显式自旋振幅的比较：check_literature_kernels.py。
- 本轮实际输出：literature_kernel_validation.json。

参考实现下载地址固定到提交：

[独立自旋子参考实现](reference_matrix_element.py)

保存其 raw 内容后，在仓库根目录执行：

    python research/stellar-cooling-eft-literature-20261105/check_literature_kernels.py --matrix-script PATH_TO_DOWNLOADED_SCRIPT --output research/stellar-cooling-eft-literature-20261105/literature_kernel_validation.json

参考模块依赖 NumPy。本轮使用 Python 3.14 和 NumPy 2.5.4；文件 SHA-256、测试点、最大差异和衰变长度输入均记录在 JSON。SHA-256 对应本轮 UTF-8/LF 保存的参考文件，换行转换会改变文件哈希。

本地旧工作分支并非此次已在线核对的 GitHub main。在线研究背景采用最新主线的 DEC-09 / DEC-15、既有 2026-11-04 文献调查和 PR #53 固定版本；本文是新增加的 EFT 文献复用研究，不将旧本地状态当作最新主线，也不将 Major 3 的可选中微子质量扩展带入本题。现有两个作者 PDF 不属于本次研究改动。
