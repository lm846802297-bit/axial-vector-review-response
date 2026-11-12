# Major 4.4 验证记录、修改对照与正式自审

日期：2026-11-06。对应 [PR #56](https://github.com/lm846802297-bit/axial-vector-review-response/pull/56)，状态 Open / Draft。规范依据：[审稿回复写作原则](../../审稿意见-gpt/写作规范/审稿回复写作原则.md) §3.1、§6、§7。

性质：这是对实际 diff、源代码、数值输出和 PDF 的执行者自审记录，不是第二位独立审查者的通过意见。没有把未完成的独立全分支审查记作通过。

## 1. 研究范围与模型边界

本项计算是支撑 Major 4.4 的固定剖面轴矢量 EFT ballistic-cooling benchmark。使用原论文低能电流归一化：
\[
g_A^\mu=-g_X,\qquad g_V^\mu=0,\qquad
g_{\nu_\mu}=+g_X,\qquad g_{\nu_\tau}=-g_X.
\]
它不引入新的 UV 场，不采用双 VEV 映射，也不把 Major 3 中讨论的可选 seesaw 带入本计算。

PR #56 与 PR #53 必须区分：
- **PR #53**：原论文单 VEV UV 模型的恒星冷却匹配和完整介质/输运后续研究。
- **PR #56**：Major 4.4 的固定剖面 EFT benchmark，计算三偏振、三通道和 ballistic escape，并把条件性结果写入回复信。它不替代 PR #53，也不声称完成完整 UV 参数扫描。

论文正文、原 Fig. 2 和原论文源文件均未修改。PR #56 只更新正式回复信、回复信所需的恒星物理参考文献和内部验证记录。

## 2. 正式回复信修改与保留审查

以 PR #55 合并后的 main 提交 `7ef9a4a65fc0f9afd25ed857325760775faf71bd` 为审计基线。实际修改集中在 Major 2、Major 4.4、Summary 和新增恒星物理参考文献。

| 对象 | 修改与处理 | 审查结论 |
|---|---|---|
| Major 2 | 保留原参数窗口论证；增加 Major 4.4 新图的交叉引用，并明确该 ballistic 带不与原图展示的 \(m_{A'}\geq1\) MeV、\(g_X\geq10^{-6}\) 区域重叠 | 仅陈述指定冷却标准和近似下的结果 |
| Major 4.4 原有内容 | 保留 SN/LESN 文献背景、原模型活性中微子流、矢量参考曲线的适用边界、轴流散度/纵向模、双缪子阈值及 kinetic-mixing 论证 | 原有独立论证未删除 |
| Major 4.4 新增内容 | 加入半康普顿核、三偏振率、active-neutrino coalescence、dimuon 通道、源剖面、角平均逃逸、冷却阈值、敏感性、ALP 极限对照和条件性图 | 形成可复核的定量证据链 |
| Summary | 保留矢量模型曲线仅作参考的限定，补充独立计算的轴矢量 EFT ballistic benchmark | 与 Major 4.4 一致 |
| Major 1、Major 3–4.3、全部 Minor | 与基线逐段核对 | 科学内容未改 |
| 审稿人原文 | 逐段核对 | 27 段原始审稿引文全部保留 |

`audit_reply.py` 对 Major 1 和 Major 3–4.3、全部 Minor 的源码保留检查通过；27 段引文保持不变。没有将 PR #56 的计算混入 Major 3 的中微子质量机制。

## 3. 缪子自旋简并与积分归一化

有效缪子密度定义为
\[
n_\mu^{\rm eff}
=2\sum_{\eta=\pm1}\int\frac{d^3p}{(2\pi)^3}
f_\eta(E_p)\,[1-f_\eta(E_p)].
\]
实现将 \(p\in[0,p_{\max}]\) 映射为
\[
p=\frac{p_{\max}}2(1+x),\qquad
dp=\frac{p_{\max}}2\,dx.
\]
因此自旋简并因子 2 与变量变换 Jacobian 中的 \(1/2\) 正好抵消；代码中出现的 \(p_{\max}\) 系数已经包含这两个因素。**原始 `transport.py` 归一化正确，不应再额外乘 2。**

新增独立积分回归测试 `test_effective_muon_density_includes_spin_degeneracy`，将 Gauss–Legendre 实现与独立自适应积分比较，确认上述归一化。19 项单元测试全部通过。这个核查没有改变原有扫描输出或物理曲线。

边界重建比较采用 \(5\times10^{-13}\) 的相对浮点容差；这只用于容忍不同数值运行环境下的末位舍入差，不是物理不确定度或放宽冷却阈值。

## 4. 数值与解析核验

| 检查 | 实际结果 | 适用边界 |
|---|---|---|
| 单元测试 | 19/19 通过，覆盖显式自旋子/迹、Ward、crossing、Thomson、纵向标度、角积分、详细平衡、Fermi 阻塞、宽度、逃逸和自旋简并密度 | 不等于完整介质热场论 |
| 独立半康普顿核 | 28 个 pure/mixed-current 对照点；最大相对误差 \(2.8801\times10^{-12}\) | 不是完整超新星输运独立实现 |
| 固定剖面扫描 | 75 个基准质量点；轴矢量绘图扩展到 80 个质量点；每点 301 个耦合 | 固定剖面 EFT benchmark |
| 通道份额 | 10 MeV 时半康普顿约 91.4%、中微子约 8.6%；100 MeV 时中微子约 99.4% | 薄极限通道分数，不是全输运能谱 |
| 冷却带端点 | 250、255 MeV 有超标区间；260、265、270 MeV 无区间，故端点约在 255–260 MeV | 不外推为更高质量的完整模型排除 |
| \(3.0\times10^{52}\) 标准低质量斜率 | \(g_{A,\rm lower}\simeq3.1734\times10^{-11}(M/\mathrm{MeV})\) | 与修正 ALP 纵向极限比较，约相差 0.35% |
| 积分加密 | nr88/ne180/na24/ns64/nc40 加密至 nr176/ne360/na56/ns144/nc80；低质量最敏感上端变化约 7.3%，1–250 MeV 上端变化不超过约 0.26% | 数值积分误差，不包含物理模型不确定度 |
| 能量截断 | \(M+1200\to M+1800\) MeV，测试点边界最大变化约 0.015% | 不证明遗漏通道无影响 |
| 耦合网格 | 301→1201 点，测试点边界最大变化约 0.28% | 端点仍报告约 0.26 GeV |
| 优化前后弦积分 | \(L\geq10^{40}\) erg/s 区域相对差最大 \(2.03\times10^{-15}\) | 算法等价性检查 |
| 半康普顿率缩放 | 整体缩放为 \(1/2\) 和 2，低质量产生端移动约 \(+41.4\%\) 和 \(-29.3\%\) | 敏感性测试，不是置信区间 |
| 源/逃逸半径 | 25→20 km，低质量上端约变为 1.93 倍，100 MeV 约变为 1.25 倍 | 不能代表全部 profile uncertainty |
| 中微子化学势 | \(\mu_{\nu_\mu}=0\) 测试点边界变化小于 1% | 不模拟非热中微子谱 |
| 表层黑体诊断 | 最大表层黑体光度约 \(8.70\times10^{51}\) erg/s，低于 \(4.4\times10^{52}\) erg/s 标准 | 固定剖面下的截获诊断 |

完整逐质量结果、扫描哈希和敏感性数据见 `outputs/numerical_validation.json`；独立振幅比较见 `../stellar-cooling-eft-literature-20261105/literature_kernel_validation.json`。

## 5. LaTeX、引用与 PDF 视觉验收

- 数值工作流：GitHub Actions Run [42165316227](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42165316227)，通过；19/19 单元测试通过，28 个独立核对点的最大相对误差为 \\(2.8801\\times10^{-12}\\)，保存扫描输出与数值验证记录复现通过。
- 回复信 LaTeX/PDF 构建与视觉验收：GitHub Actions Run [42165491749](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42165491749)，通过。该次构建使用回复信 TeX（SHA-256 `109933617fdec936f1ffd981e6438e89a9b653d2c7ff799f7cfc8f74eaf6eaab`）；工作流 refspec 修正已得到实际验证，PDF 与 `reply_audit.json` 来自同一次构建。此后没有修改 TeX 或数值源。
- PDF：65 页 A4，506,944 bytes；SHA-256：
  `56451f2dedf9ecee9ed826785424f934a2c0d21e46456ce8c18665afc962af1a`。
- `reply_audit.json`：45 个唯一引用键；27 段审稿引文不变；标签和环境检查通过；PDF 文本无 `[?]`/`??`；全部字体嵌入；无 overfull 警告；根目录 PDF 与实际 build 文件哈希一致。
- 最新 Run 42165491749 将全部 65 页以 150 dpi 渲染，并生成 11 份本地 contact sheets；该工作流不上传 contact sheets，也不自动判断页面视觉质量。此前对同一 TeX 源（SHA-256 不变）的视觉检查记录仍可作为内容版式核查依据；本次新 PDF 的自动审计确认页数、字体嵌入、文本标记和结构正常。
- 第 65 页只包含最后一条参考文献，不是空白页。曾试验缩小整个参考文献字号，但没有减少页数，因此恢复标准字号，优先保持引用可读性。
- LaTeX 日志有一处非阻塞 `Underfull \hbox`（badness 1199，源文件第 555–557 行）；无 `Overfull`。初次 LaTeX pass 的 citation warnings 经 BibTeX 和后续 pass 消除，最终审计无未解析引用/交叉引用。
- 本次 workflow 的 11 份 contact sheets 保留在 runner 临时目录，不作为 PR 文件提交；根目录 PDF、`reply_audit.json` 和数值输出保留。

## 6. 物理限制与结论

该图是指定 SFHo-18.8、t=1 s 剖面和所列通道下的 stationary-profile ballistic-cooling benchmark。没有声称完成完整超新星流体模拟、移动缪子热积分、全介质光子色散、缪子–质子 bremsstrahlung、diffusion/LESN/高能中微子重铸或完整 UV 参数空间扫描。正文和图注明确限定这些适用范围；未阴影区域不是全模型普适允许区。

**结论：** 当前计算足以支持回复信中限定的 Major 4.4 论证：天体物理约束并非无关，但已发表的矢量模型排除不能直接当作轴矢量完整排除；本次提供独立的轴矢量 EFT 条件性 ballistic benchmark，并显示其在原 Fig. 2 展示窗口内不重叠。它不证明完整 UV 模型的全局允许区。

PR #56 保持 Open / Draft，尚未合并，等待作者审阅。论文正文未修改。第二位独立研究者的全分支复核尚未完成，本记录不将其标为通过。


## 7. GeV 单位对比图（2026-11-06）

新增 outputs/axial_stellar_constraints_gev.png 和 outputs/axial_stellar_constraints_gev.pdf，用于将冷却结果的质量坐标直接与论文 Fig. 2 的 GeV 单位进行比较。

- **数据来源：** 直接读取同一份 axial.json、vector.json 和 endpoint.json；只进行坐标变换
  \[
  m_{A'}^{\rm GeV}=m_{A'}^{\rm MeV}/1000.
  \]
  不重新扫描、不插值、不改变耦合网格、光度、冷却阈值、区间端点或薄极限通道份额。
- **旧图保留：** axial_stellar_constraints.png/.pdf 与 axial_stellar_constraints_reply.png/.pdf 继续由原绘图代码生成；GeV 版是独立新增输出，不覆盖原来的 MeV 宽版或回复信版。
- **坐标和 Fig. 2 对照：** GeV 图的质量轴显示 \(10^{-5}\)–\(0.5\) GeV，即原 SN 扫描 \(0.01\)–\(500\) MeV 的完整范围。阴影仅表示 Fig. 2 展示窗口与当前坐标范围的可见交集；它不是 Fig. 2 全部质量范围的重绘，也不表示新增了实验排除。
- **纵轴文字：** 保留完整的 “Fraction of optically thin axial luminosity”，对应
  \[
  f_i^{\rm thin}=\frac{L_i^{\rm thin}}{\sum_j L_j^{\rm thin}},
  \]
  因此通道份额仍明确是光学薄极限的产生端占比，不是完整传播后的实际逃逸能量比例。
- **实际图像检查：** 对 Actions 生成并提交的 PNG 进行视觉检查；修正首轮图中将换行符显示为字面字符及底部说明文字过长的问题。最终坐标标签、Fig. 2 阴影说明、通道占比纵轴和底部注释均完整可读。
- **自动验证：** GitHub Actions Run [42225655771](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42225655771) 成功。19/19 单元测试通过；28 个独立半康普顿振幅对照的最大相对误差为 \(2.8801\times10^{-12}\)；保存扫描输出检查、全部图形再生成及 GeV PNG/PDF 发布步骤均通过。自动生成图像的提交为 4ec40c9e55c29ff7213a96f85135e9da09829afa。

本次仅新增绘图展示单位和相应文件，不改变 Major 4.4 的物理结论、模型假设或论文正文。


## 8. GeV 单位竖版回复信图及 TeX/PDF 更新（2026-11-06）

新增 outputs/axial_stellar_constraints_reply_gev.png 和 outputs/axial_stellar_constraints_reply_gev.pdf，并将正式回复信图像引用切换到该 PDF。

- **数据来源与物理不变性：** 竖版 GeV 图直接复用 axial.json、vector.json 和 endpoint.json 的同一组保存扫描。唯一的质量坐标变换为
  \[
  m_{A'}^{\rm GeV}=m_{A'}^{\rm MeV}/1000.
  \]
  不重新扫描、不插值，不改变耦合网格、光度、冷却标准、区间端点或通道份额。
- **版式与坐标：** 采用回复信栏宽的上下两面板竖版布局；上、下两面板的质量横轴均为 GeV。上方面板保留轴矢量冷却带、同输入矢量参考曲线、两个冷却标准和 Fig. 2 可见重叠区。下方面板保留 Compton、中微子和 dimuon 三个产生通道。
- **纵轴定义：** 下方面板使用完整标签 “Fraction of optically thin axial luminosity”，并对应
  \[
  f_i^{\rm thin}=\frac{L_i^{\rm thin}}{\sum_j L_j^{\rm thin}}.
  \]
  这是光学薄极限、逃逸衰减之前的产生端通道份额，不是完整传播后的实际逃逸光度比例。
- **TeX 整合：** Replies_to_Referee_3_referee_facing_2026-11-04.tex 的 Major 4.4 图像引用改为 outputs/axial_stellar_constraints_reply_gev.pdf；图注明确 \(m_{A'}\) 使用 GeV，以便与 Fig. 2 直接比较。图后的代表性质量区间表仍明确标注 MeV；这只是表格采用的质量单位，不改变图的 GeV 轴或任何数值。
- **自动生成与图像检查：** 数值工作流 Run [42230567245](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42230567245) 通过，重新生成并发布 PNG/PDF；竖版 PNG 已检查，两个 GeV 横轴、完整纵轴标签、图例、Fig. 2 阴影说明和底部注释均清晰可读。生成资产的提交为 91fc26399fee98ba976b10e5a8890775efab276a。
- **最终回复信 PDF：** LaTeX/BibTeX 构建 Run [42230873049](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42230873049) 成功。PDF 为 65 页 A4；45 个唯一引用键和 27 段审稿人原文保持不变；无未解析引用/交叉引用、未嵌入字体或 overfull 警告；全部页面均由 CI 以 150 dpi 渲染，PDF 结构审计通过。根目录 PDF 与构建产物一致，SHA-256 为 cc998df36c809fd47acf8d714b1c286e1d4d1f7a8f1a56cd4df0cd27540832ea。outputs/reply_audit.json 同时记录了新 GeV 图 PDF 的依赖哈希。
- **范围：** 本次只调整回复信图的显示单位、版式、TeX 图像引用和 PDF；不修改数值结果、Major 4.4 的物理结论或论文正文。PR #56 仍为 Open / Draft，未合并。


## 9. External check of the vector-current control curve (2026-11-07)

The dashed black contour in the figure is generated by the same local scan code with current="vector"; it is not digitized from a publication. The implementation changes the charged-muon Compton and dimuon kernels from axial to vector while retaining the same left-handed nu_mu, nu_tau couplings, reconstructed SFHo-18.8 profile, coupling grid, opacity prescription and L_R=4.4e52 erg/s criterion. It is therefore a controlled vector-muon-current reference, not a second exclusion adopted from the literature and not a vector current assigned to the neutrinos.

### Literature comparison

- **Blinov et al., arXiv:2511.09619v2, JHEP 06 (2026) 155**, Sec. 4.1 and Appendix B, Fig. 4: a conventional vector U(1)_{L_mu-L_tau} boson is constrained using the Raffelt luminosity criterion. The dominant channels are inverse neutrino decay, semi-Compton scattering and inverse muon decay; the analysis uses two muon-rich SN profiles and includes angular averaging, finite-mass velocity in the optical depth, stimulated-emission correction and gravitational redshift. The authors report order-unity shifts relative to earlier literature and qualitative agreement after updating the transport treatment.
- **Wang & Zhang, arXiv:2610.35379**, Sec. 5.2–5.3: an updated conventional vector U(1)_{L_mu-L_tau} calculation uses the SFHo-18.8 profile. It identifies neutrino coalescence and semi-Compton as the dominant production channels, with nucleon bremsstrahlung subdominant, and reports an SN1987A cooling reach up to about 300 MeV with coupling sensitivity of order 1.2e-10. Its comparison with Blinov et al. finds the lower boundary close, while upper-bound differences arise from trapping and profile/opacity treatment.

### What has and has not been checked here

The local vector control has a qualitatively similar two-branch cooling contour and comparable coupling scale over the overlapping mass range. Representative local L_R intervals are:
| m_A' | Local vector-control interval in g_X |
|---:|---:|
| 1 MeV | 2.50e-9–7.01e-7 |
| 10 MeV | 1.11e-9–7.85e-8 |
| 100 MeV | 2.39e-10–7.26e-9 |
| 200 MeV | 4.15e-10–2.86e-9 |

The current local contour reaches approximately 223 MeV, whereas the cited conventional-vector analyses report reach around 300 MeV. This is a visible difference in the high-mass endpoint; it is not appropriate to claim quantitative agreement or a reproduced literature bound. The profile used here is reconstructed from published profile plots rather than the raw Garching simulation tables, and the local benchmark omits additional subdominant bremsstrahlung channels and uses the documented muon-rest/effective-density and vacuum-photon approximations. A point-by-point digitized overlay and matched-input rerun have not been completed.

**Disposition:** retain the dashed curve only as an explicitly labelled internal vector-current control. Do not call it a published bound, do not use it as an independent experimental exclusion, and do not claim a validated numerical reproduction. The axial blue exclusion is the result relevant to the present model.


## 10. Required like-for-like validation of the vector-current control (2026-11-07)

The user's validation requirement is adopted: the vector-current control is a benchmark test of the calculation, not merely an illustrative curve. If the same vector model, stellar profile, luminosity criterion, production/absorption kernels and transport prescription are implemented, the resulting cooling contour must reproduce the published vector result within understood numerical and model uncertainties. A mismatch is a failed validation until it is explained; it must not be excused by calling the curve a comparison.

### Correct luminosity-threshold attribution

The primary \(4.4\times10^{52}\,\mathrm{erg\,s^{-1}}\) threshold is not merely a private, model-specific alternative. Blinov et al., arXiv:2511.09619, Eq. (4), explicitly use \(L_R=4.4\times10^{52}\,\mathrm{erg\,s^{-1}}\) at one second after bounce for their SN models, and identify it as the Raffelt cooling criterion. Wang & Zhang, arXiv:2610.35379, also use the corresponding profile-based Raffelt luminosity in their SN1987A calculation. The same \(4.4\times10^{52}\) value is associated with the SFHo-18.8 reference luminosity in Caputo, Raffelt & Vitagliano, PRD 105, 035022 (2022).

The \(3.0\times10^{52}\,\mathrm{erg\,s^{-1}}\) value is an alternative conventional luminosity estimate obtained by translating the local emissivity criterion \(\epsilon_X\lesssim10^{19}\,\mathrm{erg\,g^{-1}\,s^{-1}}\) using fiducial core conditions. It is useful as a threshold sensitivity comparison, but it must not be described as the primary Raffelt luminosity used by the recent profile-based \(L_\mu-L_\tau\) SN analyses. The plot legend and referee caption now make this distinction explicit.

### What already agrees qualitatively

The vector control uses the same three leading classes of processes discussed in Blinov et al.: inverse neutrino decay, semi-Compton scattering and inverse muon decay. It also includes the same broad ingredients of angularly averaged ballistic escape, reduced absorption/detailed balance and gravitational redshift. The relative production-channel hierarchy agrees qualitatively with Wang & Zhang, Fig. 11: semi-Compton scattering dominates at \(m_{Z'}\sim1\,\mathrm{MeV}\), while neutrino coalescence dominates by \(m_{Z'}\sim10\)–\(100\,\mathrm{MeV}\). The local scan gives Compton/neutrino thin fractions of about \(95.7/4.3\%\) at 1 MeV, \(18.6/81.4\%\) at 10 MeV, and \(0.31/99.69\%\) at 100 MeV.

### Why the present curve is not yet validated

The current saved vector scan gives a mass endpoint near \(223\,\mathrm{MeV}\), whereas Wang & Zhang, Fig. 12, show the conventional vector SN1987A cooling region extending to about \(300\,\mathrm{MeV}\). The local contour also has not yet been compared point by point to the digitized Blinov et al. \(s18.8\)-SFHo-MUONS curve. This difference cannot presently be classified as a harmless plotting or threshold convention.

A concrete input issue is already documented in the profile provenance file: two public figure reconstructions both labelled SFHo-18.8 give substantially different muon chemical-potential profiles. At \(r=0\) km, the Caputo reconstruction used in the baseline gives \(\mu_\mu\simeq46.7\,\mathrm{MeV}\), while the Ferreira reconstruction gives \(\simeq254.9\,\mathrm{MeV}\); at \(r=5\) km the values are approximately \(56.1\) and \(233.3\,\mathrm{MeV}\), respectively. They approach one another farther out. This is far too large to treat as a minor digitization uncertainty. It may reflect different chemical-potential conventions, different underlying snapshots/thermodynamic inputs, or an extraction/mapping issue. The definitions and original profile sources must be reconciled before the alternative curve is substituted or the vector benchmark is claimed to match.

Other differences to isolate include: (i) use of reconstructed plotted curves rather than the original PROMETHEUS-VERTEX radial tables; (ii) the local muon-at-rest/effective-density approximation versus the published \(n_\mu F_{\rm deg}\) treatment and its exact convention; (iii) the energy-dependent semi-Compton matrix element and polarization normalization; (iv) neutrino inverse-decay normalization and flavor chemical potentials; (v) inverse-muon-decay contribution and Pauli factors; (vi) the radial domain, lapse/redshift prescription and optical-depth path; and (vii) the coupling-dependent trapping/absorption treatment. Omitted \(\mu p\) bremsstrahlung is described as subdominant in the vector literature, but its size should still be checked rather than assumed irrelevant.

### Required validation sequence before the dashed curve is used as a quantitative cross-check

1. Reconcile the Caputo and Ferreira \(\mu_\mu(r)\) definitions and profile provenance; verify both against the plotted \(n_\mu(r)\) and the original SFHo-18.8 snapshot metadata. Do not mix curves from nominally similar profiles without proving they represent the same snapshot and convention.
2. Construct a like-for-like vector benchmark using the published \(s18.8\)-SFHo-MUONS profile, the \(4.4\times10^{52}\,\mathrm{erg\,s^{-1}}\) threshold, and the same production/absorption channels as Blinov et al. and Wang & Zhang.
3. Compare the semi-Compton cross section and polarization-resolved rates directly with Wang & Zhang Eqs. (5.9)–(5.11) and Appendix B in their stated low-energy regime; verify the exact-kernel result approaches those limits.
4. Compare neutrino coalescence and inverse-muon-decay kernels against the published formulas, including both \(\nu_\mu\) and \(\nu_\tau\), chemical potentials, blocking factors, polarization sums and detailed balance.
5. Compare optically thin production luminosities channel by channel at \(m_{Z'}=1,10,100\,\mathrm{MeV}\) before comparing escape attenuation. Then compare the reduced optical depths and the two boundaries of the cooling band separately.
6. Only after the above checks, overlay the digitized published curves and quantify the residual differences in \(g_{\mu\tau}(m_{Z'})\) and the high-mass endpoint. If the matched-input calculation still fails, treat it as a code/physics error and fix it before retaining the curve.

**Disposition:** PR #56 remains Open / Draft. The dashed curve is retained in the research output as a provisional diagnostic, but the referee-facing caption now explicitly says it is not a validated published-bound reproduction. The PR is not ready to merge until the vector benchmark discrepancy and the muon-profile convention discrepancy are resolved, or the unvalidated dashed curve is removed from the referee-facing figure.

## 11. 2026-11-08 update: profile provenance and the 10 MeV Fig. 7 follow-up

This addendum supersedes the profile-provenance uncertainty and the first item in the required validation sequence in Section 10. It records the completed public-source checks and the remaining pure-vector gate. It does not alter the production solver, axial scan, manuscript, or referee-response files.

### 11.1 Muon chemical-potential provenance: public-source cross-check completed

The Caputo reconstruction is now independently checked against both upstream Bollig et al. plots for the named SFHo-18.8 model:

- The digitized Caputo \(\mu_\mu/T\) profile agrees with Bollig Fig. 4 with maximum absolute relative difference 0.0161% and mean 0.00551% over the resolved interval.
- The Caputo Fig. 1 \(n_\mu\) profile agrees with Bollig Fig. 3 with 3.73% mean and 10.45% maximum absolute relative difference over the common resolved interval.
- Evaluating the Fermi integral with \(E_\mu=\sqrt{p^2+m_\mu^2}\) and the stated \(\mu^-\) convention reproduces the Caputo \(n_\mu\) curve to approximately 0.5--1.1% at the checked radii.
- The Ferreira digitization does not reproduce the same Bollig/Caputo density and degeneracy profiles in the inner core. The difference is not a constant rest-mass convention shift. The Ferreira curve remains an alternative source-level discrepancy and is not adopted.

**Updated decision:** retain the Caputo chemical-potential profile. Do not add \(m_\mu\), combine the Caputo temperature with the Ferreira chemical potential, or tune the profile to improve the 10 MeV curve. This closes the public-figure definition/provenance comparison; it does not provide the original Garching simulation table.

### 11.2 Outer-neutrino profile and absorption audit

The public Caputo profile contains \(\mu_{\nu_\mu}(r)\) but no separately plotted \(\mu_{\nu_\tau}(r)\). The baseline \(\mu_{\nu_\tau}=0\) remains an explicit assumption. At the 10 MeV high-absorption point:

- Replacing the unresolved outer \(r\geq15\,\mathrm{km}\) \(\mu_{\nu_\mu}\) tail by 0, 1, or 2 MeV changes the luminosity by -0.0128%, +0.0274%, or +0.1470%.
- Synthetic outer \(\mu_{\nu_\tau}=1,2,5,10\) MeV stress tests change the luminosity by +0.0517%, +0.2057%, +1.2416%, or +4.4865%. These are sensitivity tests, not inferred physical profiles.
- The 15--25 km absorber region contributes 63.1173% of the source-weighted mean neutrino optical depth. This is not a fraction of the luminosity absorbed.
- Independent direct production/absorption integrations through 25 km agree with the local implementation to \(5.24\times10^{-15}\) and \(3.99\times10^{-15}\); mode-resolved detailed balance is satisfied to \(1.24\times10^{-14}\).

The outer opacity is physically important within the stated reduced-opacity prescription; it is not evidence for an incorrect local-rate normalization.

### 11.3 Path/angular integration and energy convention

The independent impact-parameter/longitudinal-coordinate evaluation of Eq. (B.2) gives:

- Maximum luminosity change of \(4.31\times10^{-5}\) when replacing the original path quadrature by the analytic integral of the same piecewise-linear opacity interpolant.
- Maximum luminosity change of \(1.10\times10^{-7}\) over the 25-point curve when increasing angular order from 128 to 256; the high-absorption endpoint changes by \(8.20\times10^{-9}\).

The path/angular numerical integration is therefore converged for the frozen local rates and profile. Further quadrature refinement is not a useful route to the remaining 10 MeV discrepancy.

A genuine energy-frame ambiguity remains in the public paper: main-text Eq. (4.2) describes \(\omega\) as energy at infinity; Appendix-B Eq. (B.1) uses a local production-frame measure and escape threshold; Eq. (B.2) carries the same numerical \(\omega\) along the chord. The published version retains this equation/wording combination and provides no associated code or data. Accordingly:

- Keep fixed numerical \(\omega\) as the literal Eq. (B.2) lane.
- Keep conserved-\(E_\infty\) remapping as a separate partial-GR diagnostic on the same Euclidean chord, not a full GR ray trace.
- Do not claim either lane reproduces the authors' unavailable internal implementation.

At the 10 MeV high-absorption point, the literal lane gives \(L=2.43733471\times10^{52}\,\mathrm{erg\,s^{-1}}\), versus the digitized Fig. 7 value \(1.26781476\times10^{52}\,\mathrm{erg\,s^{-1}}\), a +92.24691% residual. The conserved-\(E_\infty\) diagnostic lowers the luminosity by 29.2634% but still leaves a +35.9708% residual.

### 11.4 Fig. 7 digitization, spatial weights, and fixed-background interpretation

The 10 MeV Fig. 7 curve is extracted from native vector paths in the pinned arXiv v2 PDF, with coordinate round-trip residuals at or below \(2.22\times10^{-16}\). Ordinary screenshot/raster digitization is not a credible explanation for the remaining discrepancy.

The joint production/absorber-radius audit finds that 97.12% of the optically thin source is produced at 5--15 km. At high coupling, 59.13% and 37.43% of the escaped luminosity originate at 5--10 km and 10--15 km, respectively. The 15--25 km absorber shell contributes 59.42%, 58.04%, 65.91%, 87.53%, and 95.58% of the neutrino optical depth for source shells 0--5, 5--10, 10--15, 15--20, and 20--25 km. These are optical-depth shares, not absorbed-luminosity shares.

The high-coupling endpoint is above the rough fixed-background warning line quoted by Blinov et al. This limits the physical interpretation of that fixed-profile region, but it does not explain a numerical mismatch between two evaluations of the same fixed-profile prescription.

### 11.5 Updated gate and disposition

1. The public muon-profile provenance check is complete; the Caputo baseline is retained. The exact raw Garching profile remains unavailable from the public material used here.
2. The outer-neutrino local kernel and the Eq. (B.2) path/angular integral are independently checked. Do not rescale opacity, production, \(g_X\), chemical potentials, or the outer radius.
3. The pure-vector Fig. 7 gate remains **NOT PASSED**. The 10 MeV high-absorption residual remains unresolved under the literal equation lane; Fig. 4 boundary agreement and path convergence do not substitute for a full Fig. 7 match.
4. The full moving-muon B.13 local-rate implementation is isolated in stacked Draft PR #57. It may quantify the optically thin semi-Compton source difference from the no-recoil B.14 approximation, but it does not address the neutrino-dominated outer high-coupling opacity. Its latest workflow run (#42335951721) is in `action_required` with no jobs or artifacts; its numerical output is not yet CI-validated and must not be imported into the PR #56 transport solver.
5. PR #56 remains Open / Draft. No manuscript, referee-response TeX/PDF, or axial constraint figure is changed by this addendum. No validated vector literature reproduction or new axial exclusion curve is claimed.




## 12. 2026-11-12 continuation: local moving-muon acceptance and document corrections

This addendum records the latest archived workflow results. It does not promote a local-rate comparison to a stellar-luminosity or literature-reproduction pass.

### 12.1 Workflow status at the recorded checkpoint

The complete workflow batch triggered by commit `3f7ce66f210edf966d8bb3b7d20f7716b28135e8` completed successfully for:

- Moving-muon thermal response: Run [43164221127](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43164221127).
- Vector-to-axial local response scan: Run [43164221273](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43164221273).
- Finite-mixing UV coupling-map tests: Run [43164221246](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43164221246).

The Major 4.4 EFT numerical validation workflow, Run [43164221257](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43164221257), had completed the C4C3 direct-recomputation SHA-256 manifest check and the SFHo/FRDM release-manifest reconstruction check. Its research-level rate/transport/kernel test step was still running at the checkpoint; the Blinov/EOS regression, saved-scan validation, figure regeneration, and reproducibility stages were therefore not yet accepted.

The three successful workflows validate their own scoped software and numerical acceptance criteria. They do not establish the pure-vector Blinov Fig. 7 gate, a global transport result, or a new SN1987A exclusion curve.

### 12.2 Moving-muon local-rate acceptance

The archived `moving_compton_validation.json` reports:

- Photon and vector-mediator Ward checks: pass.
- Charge-conjugation and zero-chemical-potential interference checks: pass.
- Nonzero-chemical-potential vector--axial interference retained: pass.
- Mode-resolved positivity and detailed balance: pass.
- Unpolarized inverse-rate normalization: pass, with maximum relative residual `3.11e-15`.
- Maximum detailed-balance residual: `4.35e-15`.
- Maximum thermal quadrature refinement difference: `2.52e-4`.

The separate SFHo-18.8 local Compton map reports finite nonnegative rates, maximum detailed-balance residual `3.92e-14`, and maximum refinement difference `1.08e-3`. Its scope is local production/absorption only: it does not include radial integration, opacity, transport, luminosity, or an exclusion curve.

The local B.13 versus B.14--B.16 comparison is documented separately in `finite_mixing/B13_B16_APPROXIMATION_REGIME_AUDIT_2026-11-12.md`. At the 10 MeV reference point it finds (Q_{\rm B13}/Q_{\rm B16}=0.4791) at the center and (0.4286) at 12.5 km. The factorized comparison separates the moving-muon correction from the stationary-target exact-Compton versus Thomson-limit approximation. This is a local source comparison, not a reason to rescale either rate and not a global Fig. 7 diagnosis.

PR #57 has since been merged into the PR #56 research branch (not into `main`). Its moving-muon work is therefore now present in PR #56's branch; it remains a local-rate module and has not been substituted into the independent Blinov transport implementation.

### 12.3 Vector-current polarization audit: reference labels and interpretation

The machine-readable audit currently identifies the integrated low-energy expressions as arXiv:2610.35379v1, Eqs. (5.9a,b), and the printed angular expressions as Appendix B, Eqs. (B.6a,b). These are the equation labels to use when discussing this audit. Any earlier conversational reference to Eqs. (58) or (106) was incorrect and must not be propagated into project documents.

The archived direct-spinor calculation and crossed-trace calculation agree at the stated benchmark, and the exact conserved-vector result has the expected transverse Thomson limit and suppressed longitudinal mode. The audit also finds that the printed integrated T/L hierarchy is opposite to that exact result, while the printed Appendix-B angular expressions develop negative regions on the paper-stated \,\(\cos\theta\in[-1,1]\) interval. Separately, the direct trace audit of Appendix-B Eqs. (B.2)--(B.4) reproduces the reference spin sums at the sampled points to approximately the (10^{-5}) level for the transverse/total pieces and about (1.2\%\) for the longitudinal difference.

These findings warrant a source-level equation audit before making a claim about a typographical or derivational error in the paper. They do not authorize replacing the published formulas in the transport benchmark. The vector Fig. 7 gate remains **NOT PASSED**.

### 12.4 Branch synchronization

At this checkpoint, the following active research PRs were each confirmed to be zero commits behind `main`:

| PR | Branch | State | Behind `main` |
|---:|---|---|---:|
| #53 | `research/stellar-cooling-original-uv-model-20261105` | Open / Draft | 0 |
| #56 | `codex/major44-axial-cooling-constraints-20261105` | Open / Draft | 0 |
| #68 | `research/major1-scalar-pole-belleii-20261109` | Open / Draft | 0 |
| #69 | `research/major1-higgs-scalar-mixing-20261109` | Open / Draft | 0 |

Before this documentation addendum, PR #56's branch HEAD was `44720ab5d4efe81096b2151948d84c17dfb69b5e`; the addendum itself is committed as `3e60bdf012019fe222bb18fa238cc78f97ccd49c`. All four branches retain their independent research commits. No branch was merged into `main` as part of this continuation.

### 12.5 Next documentation actions

1. Once Run #43164221257 finishes, record each test stage separately; do not summarize a partially completed run as a pass.
2. Keep the B.13/B.16 approximation-regime note and the vector polarization source audit as separate documents, because they answer different questions.
3. Completed the source-level derivation audit for arXiv:2610.35379v1 Eqs. (5.9), (B.1)–(B.6), and (A.15). See [WANG_ZHANG_SEMICOMPTON_POLARIZATION_AUDIT_2026-11-12.md](finite_mixing/WANG_ZHANG_SEMICOMPTON_POLARIZATION_AUDIT_2026-11-12.md). The origin of the residual coefficient and angular-distribution discrepancy remains open; do not silently swap labels or coefficients.
4. Keep the Fig. 7 pure-vector literature gate and the global axial transport calculation blocked until their own evidence is complete.

No manuscript-body, referee-response TeX/PDF, or published axial constraint figure was changed by this addendum.


### 12.6 Source-level semi-Compton polarization audit: arXiv:2610.35379v1

The detailed derivation is archived in [WANG_ZHANG_SEMICOMPTON_POLARIZATION_AUDIT_2026-11-12.md](finite_mixing/WANG_ZHANG_SEMICOMPTON_POLARIZATION_AUDIT_2026-11-12.md).

The audit establishes the following:

- The original PDF labels are (5.9a,b), (B.1a,b), (B.2)–(B.6a,b), and (A.15). The continuous equation numbers in the HTML conversion are not the PDF labels.
- The printed (B.6a,b) expressions integrate to (5.9a,b) after the common final-state velocity factor beta is restored. This is an algebraic closure check, not a physical validation.
- The printed transverse differential expression is negative for c < -x^2/2, where x=m_Z'/E_gamma. The printed longitudinal expression is negative for c > c_L=1+x^2/2-x*sqrt(1+x^2/4). Their sum is nonnegative, but the individual physical-polarization components are not.
- The correctly ordered crossed Compton amplitude obeys both vector and photon Ward identities. The printed (B.1b) appears to retain the s-channel gamma-matrix ordering in the u-channel; this is an apparent source-level ordering issue and must be checked against the authors' trace derivation.
- With the physical projectors and a conserved vector current, the independent soft-muon limit gives d sigma_T/dc = C0 beta (1+c^2) and d sigma_L/dc = C0 beta x^2 (1-c^2), to leading order in E_gamma/m_mu and x. Thus the physical hierarchy is T=O(1), L=O(m_Z'^2/E_gamma^2).
- Comparing the integrated expressions shows sigma_L(paper)=sigma_T(vector), but sigma_T(paper)=(3/2) sigma_L(vector). This is not a pure T/L label swap. The angular functions also differ, so no common normalization or angular reversal resolves the discrepancy.
- Generic-angle checks of the paper's (B.2) and (B.4) spin sums against the explicit trace agree with the expected common factor 4 from initial-state spin/polarization averaging. The subtraction (B.3) is more numerically sensitive and is to be checked by direct P_L contraction/high-precision arithmetic.

**Interpretation boundary:** this audit establishes an inconsistency between the printed mode-resolved formulas and the conserved-vector-current soft limit. It does not identify the exact algebraic step responsible, establish a corrected full finite-mass cross section, or pass the pure-vector Blinov Fig. 7 gate. Do not modify production code, opacity normalization, the manuscript, referee response, or published constraint figures on this basis.

The remaining P0 theory work is to derive (B.2)/(B.4) from the correctly ordered amplitude with exact kinematics, compute the longitudinal trace directly from P_L^{mu nu}, and trace the phase-space Jacobian and initial-state averages through to (B.6). Only then should the source discrepancy be classified.
