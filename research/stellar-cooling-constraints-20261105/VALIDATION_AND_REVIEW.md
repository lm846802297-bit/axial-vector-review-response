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
