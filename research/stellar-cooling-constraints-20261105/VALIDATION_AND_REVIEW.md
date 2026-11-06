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

以 PR #55 合并后的 main 提交 \`7ef9a4a65fc0f9afd25ed857325760775faf71bd\` 为审计基线。实际修改集中在 Major 2、Major 4.4、Summary 和新增恒星物理参考文献。

| 对象 | 修改与处理 | 审查结论 |
|---|---|---|
| Major 2 | 保留原参数窗口论证；增加 Major 4.4 新图的交叉引用，并明确该 ballistic 带不与原图展示的 \(m_{A'}\geq1\) MeV、\(g_X\geq10^{-6}\) 区域重叠 | 仅陈述指定冷却标准和近似下的结果 |
| Major 4.4 原有内容 | 保留 SN/LESN 文献背景、原模型活性中微子流、矢量参考曲线的适用边界、轴流散度/纵向模、双缪子阈值及 kinetic-mixing 论证 | 原有独立论证未删除 |
| Major 4.4 新增内容 | 加入半康普顿核、三偏振率、active-neutrino coalescence、dimuon 通道、源剖面、角平均逃逸、冷却阈值、敏感性、ALP 极限对照和条件性图 | 形成可复核的定量证据链 |
| Summary | 保留矢量模型曲线仅作参考的限定，补充独立计算的轴矢量 EFT ballistic benchmark | 与 Major 4.4 一致 |
| Major 1、Major 3–4.3、全部 Minor | 与基线逐段核对 | 科学内容未改 |
| 审稿人原文 | 逐段核对 | 27 段原始审稿引文全部保留 |

\`audit_reply.py\` 对 Major 1 和 Major 3–4.3、全部 Minor 的源码保留检查通过；27 段引文保持不变。没有将 PR #56 的计算混入 Major 3 的中微子质量机制。

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
因此自旋简并因子 2 与变量变换 Jacobian 中的 \(1/2\) 正好抵消；代码中出现的 \(p_{\max}\) 系数已经包含这两个因素。**原始 \`transport.py\` 归一化正确，不应再额外乘 2。**

新增独立积分回归测试 \`test_effective_muon_density_includes_spin_degeneracy\`，将 Gauss–Legendre 实现与独立自适应积分比较，确认上述归一化。19 项单元测试全部通过。这个核查没有改变原有扫描输出或物理曲线。

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

完整逐质量结果、扫描哈希和敏感性数据见 \`outputs/numerical_validation.json\`；独立振幅比较见 \`../stellar-cooling-eft-literature-20261105/literature_kernel_validation.json\`。

## 5. LaTeX、引用与 PDF 视觉验收

- 数值工作流：GitHub Actions Run [42157634239](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42157634239)，通过。
- 回复信构建工作流：GitHub Actions Run [42157634281](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42157634281)，通过。构建前刷新到最新 PR 分支，PDF 与审计报告来自同一次构建。
- PDF：65 页 A4，506,847 bytes；SHA-256：
  \`57c87b7106bb8bc5f70479d7134ab90b9a2e850bf46759ac67f83258c00b26dc\`。
- \`reply_audit.json\`：45 个唯一引用键；27 段审稿引文不变；标签和环境检查通过；PDF 文本无 \`[?]\`/\`??\`；全部字体嵌入；无 overfull 警告；根目录 PDF 与实际 build 文件哈希一致。
- 全部 65 页以 150 dpi 渲染并完成人工缩略图检查。重点检查 Major 4.4 的公式页 43–44、新图第 45 页、讨论页 46 和参考文献页 61–65；没有公式/图表裁切、缺字、页边距溢出或异常空白页。
- 第 65 页只包含最后一条参考文献，不是空白页。曾试验缩小整个参考文献字号，但没有减少页数，因此恢复标准字号，优先保持引用可读性。
- LaTeX 日志有一处非阻塞 \`Underfull \\\\hbox\`（badness 1199，源文件第 555–557 行）；无 \`Overfull\`。初次 LaTeX pass 的 citation warnings 经 BibTeX 和后续 pass 消除，最终审计无未解析引用/交叉引用。
- 视觉检查用的 11 个临时 contact sheets 已在审阅后删除；根目录 PDF、\`reply_audit.json\` 和数值输出保留。

## 6. 物理限制与结论

该图是指定 SFHo-18.8、t=1 s 剖面和所列通道下的 stationary-profile ballistic-cooling benchmark。没有声称完成完整超新星流体模拟、移动缪子热积分、全介质光子色散、缪子–质子 bremsstrahlung、diffusion/LESN/高能中微子重铸或完整 UV 参数空间扫描。正文和图注明确限定这些适用范围；未阴影区域不是全模型普适允许区。

**结论：** 当前计算足以支持回复信中限定的 Major 4.4 论证：天体物理约束并非无关，但已发表的矢量模型排除不能直接当作轴矢量完整排除；本次提供独立的轴矢量 EFT 条件性 ballistic benchmark，并显示其在原 Fig. 2 展示窗口内不重叠。它不证明完整 UV 模型的全局允许区。

PR #56 保持 Open / Draft，尚未合并，等待作者审阅。论文正文未修改。第二位独立研究者的全分支复核尚未完成，本记录不将其标为通过。
