# 矢量基准复现：Blinov et al.（2026-11-07）

> **Historical benchmark snapshot (2026-11-15):** this note preserves the 2026-11-07 Fig. 4/Fig. 7 and polarization-transport diagnostics. PR #56 later merged on 2026-11-12; PR #106/#113 added subsequent B.2/B.13 audits. The pure-vector Fig. 7 10-MeV gate remains unpassed, and this document is not a current validation sign-off.

> **逐偏振理论推导与代码核查：** B.7–B.19 的模式分解、详细平衡、B.2 光深定义和现有 Python 对照见 [POLARIZATION_DETAILED_BALANCE_AUDIT_2026-11-07.md](POLARIZATION_DETAILED_BALANCE_AUDIT_2026-11-07.md)。本阶段不修改生产代码或输运归一化。

## 范围与结论

按作者最新指示，仅选择审稿人指定的 [Blinov et al., arXiv:2511.09619v2](https://arxiv.org/abs/2511.09619) 作为矢量基准；不要求复现多篇文献或获取原始超新星数值表。使用现有重建 SFHo-18.8、反弹后 1 s 剖面，核验产生、吸收、偏振和传播的共同计算。数值复现和物理归一化分别判断。

Fig. 4 的 s18.8-SFHo 冷却边界由原版矢量 PDF 路径提取，并非作者原始数表。按附录 B 无反冲半康普顿公式，将偏振求和率直接代入吸收光深作为诊断，四个质量点的上下边界与原图差约 0.2%–2.9%。但是该诊断的**求和吸收率**与逐偏振玻色子的真空寿命不一致，不能仅为了复现图形而用于正式轴矢量计算。它提示了边界差异的可能来源，并不证明原作者程序一定采用该归一化，公式到作者数值实现的对应仍需核实。

| m (MeV) | 原图下端 | 诊断下端 | 原图上端 | 诊断上端 |
|---:|---:|---:|---:|---:|
| 1 | 1.749e-9 | 1.760e-9 | 2.527e-7 | 2.533e-7 |
| 10 | 1.010e-9 | 1.014e-9 | 3.843e-8 | 3.882e-8 |
| 100 | 2.430e-10 | 2.412e-10 | 3.524e-9 | 3.562e-9 |
| 200 | 4.884e-10 | 4.828e-10 | 1.136e-9 | 1.168e-9 |

图的质量端点约 211 MeV，精度受原图顶点限制。此前本代码“矢量端点约 223 MeV”是错把稀疏网格最后一个非空采样点当作闭合点。通过优化每个质量点的最大光度并细化质量网格，逐偏振矢量扫描的数值闭合点为 259.08–259.14 MeV，求和吸收诊断为 214.06–214.14 MeV；这些窄区间仅表示指定数值计算的网格定位，不能理解为天体物理精度。轴矢量端点不能由此直接推断。

1–200 MeV 内有 16 个可直接比对的质量点，求和诊断相对原图的最大下端偏差为 1.5%，最大上端偏差为 2.9%。在 1、100、200 MeV 将径向、能量、方向、路径和核积分阶数一起提高后，两个计算版本的边界变化均不超过 0.15%；这一检查不覆盖模型和原图系统误差。

## 偏振与输运

源项须对可产生的态求和 \(Q=\sum_h Q_h\)。对不发生偏振转换的传播，每态逃逸概率为 \(P_h=\exp[-\int ds\,\Gamma_h^{\rm red}/v]\)，之后才做 \(\sum_hQ_hP_h\)。真空中三种偏振具有相同单粒子宽度 \(\Gamma\)，生存概率是 \(e^{-\Gamma t}\)，不是求和后的 \(e^{-3\Gamma t}\)。有限温时不同偏振的阻塞和吸收率可不同。[Das, Ghosh & Puri, arXiv:2606.23769](https://arxiv.org/abs/2606.23769) 也采用分别演化偏振、最后求和的处理。

只切换为无反冲核并保留逐偏振输运时，1 MeV 下端由 2.504e-9 移到 1.758e-9；100 MeV 上端仍为 7.262e-9，未接近文献的 3.524e-9。将求和诊断的吸收率除以 3 后，在 100、200 MeV 与逐偏振计算接近。因此不能把差异全部归咎于恒星剖面，也不能声称当前主曲线已与文献逐点一致。

## 其他核查和边界

- 独立费米积分闭式计算 Blinov B.7、B.9、B.11，与代码的逐态中微子、双缪子产生率求和比较；还核对无反冲的光子偏振因子和速度因子、详细平衡、真空寿命、均匀球的方向平均解析逃逸概率。
- 对 Fig. 7 全光度曲线的路径提取与数值对比：1 和 200 MeV 可见区间最大相对差约 1.6%；标为 10 MeV 的曲线在弱耦合段相差约 9%，采样的最强吸收点相差约 92%。边界接近不意味着全耦合光度一致。图上标注的质量精度和没有作者原始数表限制了解释；差异尚未解决。
- 使用 Caputo Fig. 1 的 \(T,\mu_\mu\) 计算自由费米气体负缪子密度，在 0、5、8、10、15 km 与独立密度曲线相差约 0.5%–1.1%。Ferreira 同名化学势与之差别很大，在相同温度和分布定义下对应约 613 倍中心密度；差随半径变化，不能简单归结于加减静质量。原始 Garching 对应数据入口返回 HTTP 401，按作者决定不将其获取设为前置条件；继续标明图形重建的适用性。
- 补充纠正：Blinov 采用 \(4.4\times10^{52}\,\mathrm{erg/s}\)；Wang–Zhang 采用 \(3.0\times10^{52}\,\mathrm{erg/s}\)。此前说后者也采用 4.4 是错误的。后者无需复现。

## 可复算记录与验收状态

`vector_reference.py` 提供独立参考率，`test_vector_reference.py` 核验解析结果，`extract_vector_reference.py` 记录公开图的路径与哈希，`run_vector_audit.py` 记录通道光度和诊断切换。输出保存在 `outputs/vector_audit/`。所有结果是内部诊断，不替换审稿回复图。

本轮不更改回复信 TeX/PDF、论文正文、原扫描与图。未完成完整移动缪子热积分或作者代码比对，不把它们和原始剖面设为当前单文献复现的强制前提。文献边界诊断得到定量匹配，但逐偏振归一化对应和 Fig. 7 的 10 MeV 光度差异尚未闭合；不能把本次诊断写成完整物理验证。在 2026-11-07 本文快照中 PR #56 尚处于 Draft；PR #56 后于 2026-11-12 合并。

## Latest six-mass reproduction and polarization-transport result (2026-11-07)

This section supersedes the earlier three-mass Fig. 7 summary above.

### Six-curve Fig. 7 result

All six vector paths are extracted from the pinned arXiv v2 source PDF member `luminosity_snapshot_t=1.pdf`, with source hash and drawing metadata archived. The independent scalar Appendix-B scan has been run at 40/100/16/32, 88/180/24/64, and 132/280/40/96 resolutions.

| m_V (MeV) | 132/280/40/96 mean residual | maximum residual |
|---:|---:|---:|
| 10^-6 | 4.62% | 12.90% |
| 10^-5 | 4.63% | 13.49% |
| 0.1 | 2.68% | 15.08% |
| 1 | 1.47% | 2.34% |
| 10 | 15.84% | 92.09% |
| 200 | 0.56% | 1.47% |

Only the 1 and 200 MeV full curves pass the provisional 5% mean / 10% maximum criteria. The ultralight curves remain quadrature-sensitive: the 88/180/24/64 to 132/280/40/96 change on source vertices is about 6% mean and 24% maximum. A 176/360/64/128 scan is running for 10^-6 and 10^-5 MeV. The 0.1 MeV curve has a smaller mean residual but a maximum residual above 10%. The 10 MeV discrepancy is stable under quadrature refinement.

### Fig. 4 boundary recheck

At 88/180/24/64, the four 1, 10, 100, and 200 MeV lower/upper boundary deviations are +0.94%/+0.25%, +0.49%/+1.02%, -0.73%/+1.06%, and -1.14%/+2.82%, respectively. The maximum is within the provisional 3% tolerance, with the 200 MeV upper edge closest to the limit. This does not imply that the full Fig. 7 curves pass.

### P1: scalar-summed versus mode-resolved transport

The new [transport prescription output](outputs/vector_audit/transport_prescription_comparison.json) is a controlled comparison with identical B.14 local kernels:

- `blinov_literal`: the scalar polarization-summed opacity used as a single attenuation rate;
- `thomson_modes`: the same B.14 local rates, but each polarization is attenuated with its own opacity;
- `blinov_average`: arithmetic average opacity, diagnostic only.

The mode-resolved luminosity is higher than the scalar-summed luminosity at all source vertices. Its mean increase relative to the scalar-summed prescription is 111%, 157%, 677%, 447%, 558%, and 244% for 10^-6, 10^-5, 0.1, 1, 10, and 200 MeV, respectively. The largest pointwise increases exceed two orders of magnitude in some high-trapping tails. The mode rates themselves sum to the scalar local rates and pass the independent rate/detailed-balance tests. The difference therefore arises from applying the nonlinear escape factor before or after polarization summation, not from a missing local factor.

The arithmetic-average-opacity diagnostic does not reproduce the published Fig. 7 curves and is not adopted. The scalar-summed lane remains the literal literature-reproduction prescription; the mode-resolved lane remains a distinct physical transport calculation. No factor of three is silently inserted or removed.

### Interpretation of 10 MeV and scope

The published paper states that neutrino inverse decay dominates trapping above the MeV scale, while semi-Compton absorption is mainly relevant below the MeV scale. Its B.14 no-recoil approximation is specifically motivated for m_V below the MeV scale. The 10 MeV high-coupling mismatch is therefore not assigned to B.14 alone. A fixed-target exact-recoil diagnostic worsens the residual and is not the full moving-muon B.13 integral.

The paper also explicitly warns that the high-coupling region above the dash-dotted lines has significant theoretical uncertainty because the vector can alter the supernova dynamics, making a fixed SM profile unreliable. The exact s18.8-SFHo-MUONS source profile is not publicly available in the current audit. Thus the 10 MeV tail remains unresolved under the reconstructed profile; no fitted rescaling is used.

**Current disposition:** P0-A local integrals pass; P0-C Fig. 4 boundaries pass the provisional tolerance; P0-B full Fig. 7 reproduction remains blocked. The mixed-current scan is not authorized yet. The manuscript and referee-response files remain unchanged. PR #56 was Draft at this 2026-11-07 snapshot and later merged on 2026-11-12.

