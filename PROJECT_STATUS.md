# PROJECT_STATUS — Axial-vector paper revision and referee response

> **P1-IIIe-B SFHo/FRDM v1.03 真实表数据与局域闭合（2026-11-11，后续数值修正）：** 官方 Basel 五个对象的获取器、五项 SHA-256 manifest 与 Release 归档已核对；Release tag sfho-frdm-v1.03-data 指向 e68eae83385dcb62b31b7fa12bf32f85a2e7a819，五个资产 digest 与 manifest 一致，总计 322,921,457 B。HTTP HEAD 的 --check-urls 只证明 HTTP 200 与 Content-Length 匹配，不被描述为远端内容哈希验证。224 点闭合采用 1024 阶 Gauss–Legendre；独立 1024/2048 对照在 448 个核子状态上的最大 Fdeg 绝对差为 4.7117e-8，数密度最大相对差为 1.0115e-8；1024 阶对 fixture 的最大 Fdeg 绝对差为 4.995e-11。旧 512 阶在冷、高密度中子状态可有 2.73% 偏差，因此 fixture 与原始表复算测试均已统一到 1024 阶。有效域仍为 224 点采样网格上的 208/224 格；中子最大偏差 6.1345e-4，质子（Xp≥1e-6）最大偏差 8.8578e-5。其余 16 格并非全部冻结：nB=1.10e-12 与 1e-10 fm⁻³ 的 8 格为明确平台；1e-8 的 4 格为过渡；1e-6 的 4 格更接近闭合但仍未满足 1e-3。16 格均为核子主导组成，Xn+Xp≈1，组成随 Yp 变化。自然单位稀释度在 T=63.096 MeV、nB=1e-6 fm⁻³ 时为 3.06e-5。核团比例统计代码已改为只使用 308 个物理密度行；由于本次未重读原始 composition archive，更新后的整表比例暂不作数值声明。五对象 Manifest、下载器与审计 JSON 的名称和哈希集合一致。本次独立 JavaScript fixture 交叉核验 12 组检查全部通过；这不是 Python unittest 运行结果。18 项 Python 测试（新增一项校验 vendored 分块布局）已在 head 5dd24ac 上、以 SFHO_TABLES_DIR 指向解包后的 v1.03 表重跑：P1-IIIe-A 15/15、P1-IIIe-B 18/18 全过。CI 也已在同一 head 通过（run 42922595906，success，23 s：fixture 路径 Ran 14 tests … OK (skipped=1)，四项原始表测试按设计跳过，自检断言块通过）。原始归档现已入库：spp/comp/manual 原样提交，161 092 071 B 的 extended 表拆为三个 60 MiB 分块，配 MANIFEST.sha256（7 条）与 reassemble_sfho_frdm_archives.py；往返重组与已发布文件逐字节一致（sha256 45479eaf…b8949c），shen98 仍只存 Release。本轮之前的「无新的 Python 测试或 CI 通过声明」等表述已被以上结果取代。

> **2026-11-10 纯矢量 Fig. 7 复现状态：** PR #57 仍为 Open / Draft，未合并。当前统一背景为 vertex-preserving profile B，SHA-256 为 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`。B.1 独立源项、B.2 独立路径、B.1+B.2 端到端重组和局域碰撞核检查已有成功的数值验收记录；最新高阶独立网格 B.16 基准在 10 MeV 强耦合端为 `2.43963596e52 erg/s`，相对 Fig. 7 高出 `92.4284%`，尚未通过物理复现验收。能量/方向分箱程序已修正子区域掩码并加入回归测试，但高阶分箱结果尚未生成。最后一次有意触发的资源预检 Run [#42663539198](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42663539198) 仍在 runner 分配前失败，`steps=null`、`logs_url=null`、没有 runner ID；不再重复触发空跑。下一次执行固定为恢复 Runner 后或本地运行同一脚本，且必须通过完全相同的网格哈希、基准闭合和分箱归一化验收。

> **B.2 路径能量与径向插值的独立验收（2026-11-09）：** 固定 B.1 源项径向阶数 40、能量 100、角 16、路径 32，仅将 B.2 局域吸收率径向插值网格从 40 提高到 640。B.1 thin source 在所有插值网格间保持不变；三个质量点的最后两级 320→480、480→640 最大光度变化均小于 1%，因此独立 opacity 插值验收通过。两级变化分别为：0.1 MeV 0.4025%、0.1577%；1 MeV 0.1028%、0.0393%；10 MeV 0.00193%、0.00152%。但粗网格 40→640 对固定能量光度造成的最大变化分别达到 42.14%、9.73%、0.175%，说明此前低质量 B.2 基准存在严重的路径吸收率插值不足。采用 640 阶插值后，B.16 路径红移在峰值/强端的变化分别为：0.1 MeV −0.00747%/−5.9078%；1 MeV −0.51366%/−11.6001%；10 MeV −5.21614%/−28.8724%。这些结果取代原 40 阶径向插值下的低质量红移数值；它们仍是 B.16 矢量碰撞核下的 B.2 诊断，不是 B.13 精确核的传播结果。详见 [B.2 径向 opacity 插值收敛审计](research/stellar-cooling-constraints-20261105/blinov_reproduction/B2_OPACITY_INTERPOLATION_CONVERGENCE_2026-11-09.md) 与 JSON。Run [#42581429474](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42581429474) 全部通过。

> **B.13 低质量全局收敛状态（2026-11-09）：** 0.1、1 MeV 的 B.13 全局径向/能量/角/路径积分与全网格碰撞核阶数检查正在运行，当前尚无最终验收结果。已通过的局域核收敛不替代全局 B.1+B.2 收敛；同时，B.2 矢量基准已显示路径 opacity 插值网格是低质量区的重要数值维度，因此 B.13 全局结果必须结合其自身的路径插值分辨率审查，不能仅依据 source radial order 40→80 的变化作最终结论。

> **B.13 全局替换结果：** 在 10 MeV 纯矢量 benchmark 中，按单负缪子约定同时替换 B.1 Compton 源项和 B.2 Compton reduced opacity，得到弱端/峰值/强端偏差分别为 \\(-28.11\\%\\)、\\(-16.34\\%\\)、\\(+131.53\\%\\)。B.13 的 optically-thin 总源为 B.16 的 78.898%；B.13 负缪子 Compton 源为 B.16 Compton 源的 34.07%。源项与吸收项必须同时替换；source-only 和 opacity-only 结果仅为反事实诊断。该结果没有修复 B.16--Fig. 7 的差异，且尚不作为最终精度预测。

> **数值与 CI 状态：** B.16 同网格闭合残差为 0；B.13 详细平衡最大残差约 \\(1.5\\times10^{-14}\\)，最终缪子质量壳残差约 \\(3.7\\times10^{-13}\\)。最新局域碰撞核全网格审计 Run [#42565336032](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42565336032) 成功；当前 vertex-preserving profile B 上的固定能量/路径红移三质量审计 Run [#42568420651](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42568420651) 也成功，JSON 已归档为 `outputs/b16_global_redshift_audit_2026-11-09.json`，其 profile SHA-256 与当前 9fb14e... 完全一致。重复并发 Run #42568424558 的数值步骤通过，但在首个 run 已归档同名输出后发生 add/add 归档冲突，不构成计算失败。B.13 全局 quadrature Run [#42542328275](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42542328275) 的计算和数值验证步骤通过，但归档上传步骤失败；另一个径向/能量扫描 Run [#42536610504](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42536610504) 成功。因此 B.13 全局替换仍标为独立诊断，不宣称所有收敛输出均已完整归档。

> **正式版本文献边界：** JHEP 06 (2026) 155 的 Sec. 4.1 将 \\(\\omega\\) 描述为无穷远能量，而 Appendix B.1 的 \\(N(r)^2\\) 与 \\(m_V/N(r)\\) 下限对应源点局域能量；B.2 沿路径固定同一 \\(\\omega\\)。此外，论文给出完整 Compton 相空间式 B.13 及近似表达式 B.14--B.16，但 Fig. 7 文字没有明确指出数值实现采用哪一种，且文章未提供配套数据或代码。当前 B.16 仍是工作基准，不能据此声称已确认作者未公开代码的具体实现。详见 [能量与 Compton 处方文献复核](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_ENERGY_VARIABLE_AND_PATH_REDSHIFT_CONVENTION_AUDIT_2026-11-09.md)。

> **B.2 路径能量与径向收敛审计（2026-11-09）：** 三质量点 fixed-\(\\omega\) 与 path-redshift-only 计算已完成。最高测试网格下，强耦合端红移敏感性分别为 −5.64%（0.1 MeV）、−11.55%（1 MeV）、−28.85%（10 MeV）；该分支仍是固定 Euclidean chord 的敏感性诊断，不是完整 GR。能量、角度、路径积分的单维加密均通过 1% 筛选，但径向 60→80 节点变化在 0.1、1 MeV 分别仍达 7.63%、1.87%，因此低质量全局曲线尚未收敛。独立吸收率插值审计显示 0.1 MeV 需至少约 240–320 节点才进入 1% 稳定区间。现已增加 B.1 源径向阶数 80–200、同时固定 640 节点 opacity grid 的解耦审计，运行中。详见 [B.2 路径能量与径向收敛状态](research/stellar-cooling-constraints-20261105/blinov_reproduction/B2_PATH_ENERGY_AND_RADIAL_CONVERGENCE_STATUS_2026-11-09.md)。

> **B.13/B.16 三质量点对照（2026-11-09）：** 纯矢量 B.13 全局源项与吸收率已在 0.1、1、10 MeV 完整替换计算。主产生区 5--12 km 内，B.13/B.16 源项比约为 0.338、0.338、0.340；Compton 约化吸收率比约为 0.353、0.352、0.360。B.13 局域矩阵元在 (8 km,15 MeV)、(12.5 km,20 MeV)、(15 km,30 MeV) 的高阶积分检查均通过 0.1% 项目筛选阈值，0.1 与 1 MeV 的最大末级变化分别为 0.0283% 和 0.0288%。这不是全局 B.1+B.2 积分的收敛证明。三质量点的 Fig. 7 强耦合端偏差分别为 +0.33%、+138.84%、+131.59%；10 MeV 仅为超出低质量 Compton 适用区的压力测试。详见 [B.13/B.16 三质量点源项、吸收率与收敛审计](research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_THREE_MASS_SOURCE_OPACITY_AND_CONVERGENCE_AUDIT_2026-11-09.md)。低质量局域核 Run [#42575922722](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42575922722) 通过。

> **B.16 约化 Compton opacity 解析化简（2026-11-09）：** 将 B.16、B.19 和 B.4 直接合并后，显式 Bose 因子严格抵消，得到 `Gamma_abs* = [16 pi alpha alphaV/(3 m_mu^2)] (n_mu F_deg) [1+mV^2/(2 omega^2)]`；B.2 光学深度还需除以 `vV`。因此路径红移不会通过残留 Bose 因子改变约化 Compton opacity，而是通过有限质量项和 B.2 的 `1/vV` 改变它。详见 [跨质量 opacity 与能量约定诊断](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_CROSS_MASS_OPACITY_AND_ENERGY_CONVENTION_DIAGNOSTIC_2026-11-09.md)。

> **22--25 km 中微子化学势敏感性（2026-11-09）：** 在当前 profile B 上，对 22--25 km 的 mu_numu 分别赋值 ±1、±3 MeV，并对每个情形完整重算 B.1+B.2。该壳层占 8--15 km 源项的 neutrino path-tau 19.1084%，但强耦合端逸出光度分别只改变 +0.0172% 和 +0.1505%；±号结果精确对称。说明该区间的路径吸收重要，但其未确定的 mu_numu 延拓在 ±3 MeV 测试范围内不是 Fig. 7 大偏差的原因。Run [#42572982267](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42572982267) 全部通过。详见 [22--25 km 中微子化学势敏感性审计](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_OUTER_NUMU_SENSITIVITY_22_25KM_2026-11-09.md)。

> **B.14 非相对论缪子近似诊断（2026-11-09）：** 使用 B.17 的 susceptibility 权重 (p^2 f_\mu(1-f_\mu))，并按低质量 B.16 源项径向权重 (r^2N^2(n_\mu F_{\rm deg})T^4) 加权，得到缪子平均速度约 0.761、rms 速度约 0.775；约 93.2% susceptibility 权重满足 (v_\mu>0.5)，约 71.7% 满足 (p_\mu>m_\mu)。约 79.1% 的低质量 Compton 源来自 8--12 km，该区间平均速度约 0.74--0.78。因此 B.14 的非相对论/无反冲近似在主要源区并非显然受控；这只是分布诊断，不等同于 B.13 速率误差，需由 0.1、1 MeV 的全局 B.13 对照定量判断。详见 [B.14 非相对论缪子近似诊断](research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_NONRELATIVISTIC_MUON_APPROXIMATION_DIAGNOSTIC_2026-11-09.md)。独立脚本、测试和 JSON 已归档，Run [#42572394290](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42572394290) 全部通过。

> **跨质量 opacity/能量约定诊断（2026-11-09）：** 当前 profile B 的 0.1、1、10 MeV 结果显示：B.16 Compton 源项份额分别为 99.978%、97.870%、32.005%；Compton 对 source-weighted mean opacity 的份额分别为 99.931%、93.471%、10.222%。10 MeV 的中微子逆衰变贡献了 89.778% 的平均光学深度，且 20--25 km 占总平均光学深度 28.895%。路径红移诊断在 10 MeV 改善强端偏差（+92.24% 到 +36.74%），但在 0.1、1 MeV 分别使强端偏差从 -36.16% 变为 -39.35%、从 -5.35% 变为 -16.17%；因此它不是可全质量采用的修正。详见 [跨质量 opacity 与能量约定诊断](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_CROSS_MASS_OPACITY_AND_ENERGY_CONVENTION_DIAGNOSTIC_2026-11-09.md)。

> **方法重建纠正（2026-11-09）：** 缺少同快照 A(r)/M(r) 不妨碍复现 Blinov 发表版 Appendix B。其 B.1 使用 lapse 的 N(r)^2 与 m_V/N(r) 局域发射能量处方；B.2 明确使用欧几里得直线弦，未包含 A(r)、proper-distance 因子或测地线弯曲。这与其引用的 Caputo et al. arXiv:2201.09890 Supplemental C 一致：Garching pseudo-Newtonian 模型采用平直空间坐标，lapse 负责发射能量红移和 N^2 光度因子。A(r)/M(r) 仅是完整 GR 扩展所需，不是 Fig. 7 论文处方复现的前置条件。B.1 的局域源能量与无穷远守恒能量已通过精确 Jacobian 变换和独立数值积分验证为完全等价，三个通道的相对残差均为 0；对应 Run [#42573725261](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42573725261) 通过。唯一剩余的能量约定问题是 B.2 沿路径固定 omega 是否为字面局域能量，还是作者数值实现中隐含了 E_infinity/N(r')。详见 [发表版引力与能量处方重建](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_PUBLISHED_GRAVITY_AND_ENERGY_PRESCRIPTION_RECONSTRUCTION_2026-11-09.md)。

> **物理输入边界：** Caputo 的 T(r) 与 mu_mu/T 在 5--20 km 与 Bollig Figs. 1、4 的直接矢量曲线交叉吻合；原始 Fig. 4 明确支持 Caputo 而非 Ferreira 的 mu_mu/T digitization。Caputo 的绝对 n_mu 与其自身 Fermi 积分一致，但 Bollig Fig. 3 的密度在 5--15 km 平均低约 5%，12--15 km 低约 8.8%；B.17 使用的是同一 T, mu_mu 分布决定的 susceptibility n_mu F_deg，不得按 Fig. 3 密度比直接重标度。20--25 km 的部分热力学输入仍属图像外延或未分辨分支。lapse N(r) 在 0--20 km 还得到 Zuowei Liu 2026-10-31 会议报告 slide 65 的独立视觉交叉支持，但这不是机器精度验证。原始 20--25 km 热力学剖面仍未完全核验；同快照 A(r)/M(r) 只影响可选完整 GR 扩展，不阻碍按论文 B.1--B.5 复现。

> **原始数据获取审计（2026-11-09）：** 官方 Garching 目录列出的 Bollig/Hüdepohl 径向 hydro 数据、径向中微子数据以及 Robert Bollig 的 Python TOV solver 入口均返回 HTTP 401；官方目录明确说明部分档案需密码并要求联系数据负责人。arXiv:2610.35379 的后续研究同样指向 Garching archive，而不是提供独立公开镜像。当前没有获得同一快照的原始 (A(r))、(M(r)) 或 hydro 表。详见 [公开 profile 与 metric 数据可用性审计](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_PUBLIC_PROFILE_AND_METRIC_SOURCE_AVAILABILITY_AUDIT_2026-11-09.md)。不绕过访问控制，不以通用 TOV 求解器或其他快照替代原始数据。

> **方法边界：** Fig. 7 工作基准继续采用 Appendix B.2 字面给出的标量、偏振求和吸收率；逐偏振传播、路径红移和 B.13 精确移动缪子计算保留为独立诊断。没有进行经验性源项/吸收率/光度重标度，没有修改生产轴矢量曲线、论文正文或正式回复信。只有纯矢量基准通过独立物理验收后，才解冻轴矢量限制曲线。最终验收结论见 [B16_VECTOR_BENCHMARK_ACCEPTANCE_GATE_2026-11-09.md](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_VECTOR_BENCHMARK_ACCEPTANCE_GATE_2026-11-09.md)：数值模块通过，但 Fig. 7 物理复现未通过；PR #57 保持 Open / Draft。

> **2026-11-07 矢量 benchmark 更新：** 作者指定仅复现 Blinov et al.，采用现有重建剖面，不要求精细恒星模型或原始表作为前置条件。已定量对照该文 Fig. 4，发现偏振求和吸收率与逐偏振单粒子宽度的区别；完整 Fig. 7 中 10 MeV 光度仍有差异。旧“矢量端点 223 MeV”是稀疏采样误读，当前逐偏振计算闭合点约 259.1 MeV。详见 [矢量 benchmark 核查](research/stellar-cooling-constraints-20261105/VECTOR_BENCHMARK_AUDIT_2026-11-07.md)。PR #56 仍为 Draft；这些诊断并不构成最终物理验证。

**历史基线快照日期：** 2026-11-06（PR #38–#50 已合并；PR #54、#55 已合并；PR #52 Closed / 未合并且保留研究分支；PR #53、#56 Open / Draft）。当前研究状态以本文档最上方的 2026-11-09 摘要及对应验收报告为准。

**本状态快照的初始核验基线：** 243b0e62d9c3912525d1144971a1e81c2af84db7（PR #36 合并前）  
**项目启动机制合并提交：** [9b4e17519230e9eef65b34b643d3a1f8c19f46a2](https://github.com/lm846802297-bit/axial-vector-review-response/commit/9b4e17519230e9eef65b34b643d3a1f8c19f46a2)  
**用途：** 每次启动项目时快速恢复当前阶段、权威文件和下一步工作。本文件是可更新的状态快照，不替代物理推导、原始论文、计算证据或作者最新指示。

> **更新原则：** 任务完成、作者改变观点、PR 合并、论文基线更换或计算结论更新后，应检查并更新本文件。尚未重新核验的内容标为“待核验”，不得沿用旧状态作确定陈述。

## 2026-11-06 更新：PR #55 Minor Points 论证扩充与长期写作规范（已合并）

[PR #55](https://github.com/lm846802297-bit/axial-vector-review-response/pull/55) 已于 2026-11-06 Squash Merge 至 main，合并提交为 [7ef9a4a65fc0f9afd25ed857325760775faf71bd](https://github.com/lm846802297-bit/axial-vector-review-response/commit/7ef9a4a65fc0f9afd25ed857325760775faf71bd)。以下保留该 PR 的正式回复信与写作规范修改记录。

- **正式回复信：** 在此前 Major 3、Major 4.2、Major 4.3 和 Minor 6.5 结尾修订基础上，进一步扩充 Minor 1–5、6.1、6.2、6.4、6.5、6.6；Minor 6.3 经核对保持不变。所有非中微子问题继续采用原论文单 VEV \(S+\mathrm{VLL}\) 模型。
- **后续最小纠错：** Major 3 明确原始 \(S\)-only 模型与可选 \(\sigma+3N_R\) seesaw 的区别；Major 4.3 统一 \(\mu/\tau\) 的带符号耦合并将 small-mixing 统一称为 condition/domain；Minor 3 澄清带符号耦合与绝对值；Minor 4 澄清四个混合角分别受同一数值上限约束而非彼此相等。另补充 Major 2 的 VLL Yukawa 微扰性依赖、Major 4.2 的保守不等式和 Major 4.4 的完整超新星输运限定。Major 1.3 的局部扫描边界保持不变。
- **新增物理论证：** Minor 5 增加 \(A_{\rm LR}^\mu\)、\(P_\tau\) 的手征振幅解析投影、\(A'\) 总宽度部分道分解、\(ee\) 通道高动量 kinetic-mixing 适用性以及 \(e^+e^-\to Zs\) 的 Higgsstrahlung 缩放关系；Minor 6.5 从两个活性 chiral-neutrino 道推导寿命上界、boost 后飞行距离和 dimuon 阈值抑制。没有加入未经复核的 collider reach 数值。
- **长期规范：** 在审稿回复写作原则新增强制 §2.2「论证充分性原则：从结论陈述到可复核的物理论证」，并同步 §5、§6、§6.1、§7。覆盖物理原因、公式来源、benchmark/近似/数值意义、实验适用性映射和多子问题逐项回答；强调不机械增加篇幅。
- **内部记录：** Minor Points 论证扩充与复核记录、全信结尾修订审查记录均已写入 2026-11-06 目录。
- **静态验收：** 78 次引用出现、39 个唯一 citation keys 全部解析；LaTeX 环境配对、花括号、标签和交叉引用检查通过；Minor 6.3 与 main 原段落逐字一致。
- **完整 LaTeX/PDF 验收：** 已通过 GitHub Actions Run [#3](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42146091113) 对 PR 分支源码完成 `latexmk -g -pdf -bibtex` 编译；最终 PDF 为 59 页 A4，根目录文件为 [Replies_to_Referee_3_referee_facing_2026-11-04.pdf](Replies_to_Referee_3_referee_facing_2026-11-04.pdf)，生成提交为 `8c21ff02a216e636e1655ddb0d1c38488ec6714b`。最终 LaTeX `.log` 无未解析引用/交叉引用，BibTeX `.blg` 无缺失条目或数据库错误；59 页均以 150 dpi 渲染并完成人工页面预览检查。未发现公式/表格裁切、缺字、溢出页边距、空白页或异常分页。仅有一处非阻塞 `Underfull \\hbox`（badness 1199，TeX 第 555–557 行），未发现 `Overfull`。
- **本轮未涉及：** 论文正文、图表和 BibTeX 数据库均未修改；完整数值脚本 clean-environment 重跑、detector-level collider 模拟和全仓库测试套件仍未执行。Actions 仅用于正式回复信编译、引用检查和页面渲染。

**合并状态：** PR #55 已合并至 main。其 59 页正式回复信 PDF 和视觉验收记录保留在本节；后续 Major 4.4 的轴矢量 EFT 冷却计算由独立 PR #56 处理。

## 2026-11-06 更新：PR #56 Major 4.4 轴矢量 EFT 恒星冷却 benchmark（Draft）

[PR #56](https://github.com/lm846802297-bit/axial-vector-review-response/pull/56) 保持 Open / Draft，分支为 `codex/major44-axial-cooling-constraints-20261105`；**尚未合并**。

- **与 PR #53 的区别：** PR #53 继续研究原论文单 VEV UV 模型的完整恒星冷却匹配；PR #56 是专门支持 Major 4.4 的固定剖面轴矢量 EFT ballistic-cooling benchmark。PR #56 使用原论文的低能电流归一化 \(g_A^\mu=-g_X\)、\(g_V^\mu=0\)、\(g_{\nu_\mu}=+g_X\)、\(g_{\nu_\tau}=-g_X\)，不引入新的 UV 场、不采用双 VEV 映射，也不把 Major 3 的可选 seesaw 带入本计算。
- **回复信整合：** Major 4.4 增加轴矢量半康普顿、三偏振输运、三通道竞争、冷却带和数值敏感性；Major 2 增加新图交叉引用；Summary 与新恒星物理参考文献同步。正式回复信仍不包含 PR、CI 或内部任务状态。
- **数值验收：** 19 项单元测试通过；28 个独立振幅对照点的最大相对误差为 \(2.8801\times10^{-12}\)；75 个基准质量点、80 个轴矢量绘图质量点、每点 301 个耦合。冷却带的质量端点位于 255–260 MeV；10 MeV 薄极限半康普顿份额约 91.4%，100 MeV 中微子份额约 99.4%。
- **PDF 验收：** 最新 GeV 竖版图版本重新编译为 65 页 A4；45 个唯一引用键、27 段审稿人原文全部保留；无未解析引用/交叉引用、无未嵌入字体、无 overfull 警告。最新 CI 将全部 65 页以 150 dpi 渲染并通过 PDF 结构审计；新 GeV 回复信 PNG 已单独完成视觉检查。根目录 PDF SHA-256 为 cc998df36c809fd47acf8d714b1c286e1d4d1f7a8f1a56cd4df0cd27540832ea。此前末页只有最后一条参考文献，但不是空白页；缩小整套参考文献字号未减少页数，因此恢复标准字号。
- **GeV 对比图：** 新增 outputs/axial_stellar_constraints_gev.png/.pdf，完全复用已有扫描数据，只将质量坐标由 MeV 转为 GeV；原宽版 MeV 图和回复信版 MeV 图均保留。阴影只标示当前面板与 Fig. 2 展示窗口的可见交集，不表示重绘 Fig. 2 全部范围。
- **GeV 竖版回复信图：** 新增 outputs/axial_stellar_constraints_reply_gev.png/.pdf；与 GeV 宽版使用同一数据和坐标变换，采用上下两面板竖排，并在下方面板保留完整的 “Fraction of optically thin axial luminosity” 纵轴标签。正式回复信 TeX 已切换到新 PDF，根目录回复信 PDF 已重新编译。
- **图形验证：** GitHub Actions Run [42230567245](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42230567245) 通过：19/19 单元测试、28 组独立半康普顿振幅对照（最大相对误差 2.8801e-12）、保存扫描检查及四类 MeV/GeV 图形再生成和发布均成功；GeV 竖版回复信 PNG 已完成视觉检查。最终 PDF 构建见 Run [42230873049](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42230873049)。
- **边界：** 这是指定剖面和所列通道下的条件性 ballistic benchmark，不是完整超新星流体模拟、全介质输运、LESN/高能中微子重铸或完整 UV 参数空间排除。论文正文未修改。PR #56 保持 Draft，等待作者审阅与明确合并决定。

## 2026-11-05 更新：模型范围纠正与研究 PR 替代关系

PR #50 已于 2026-11-05 Squash Merge 至 main，合并提交为 [51a245b0a36703f40c24ca469d6969e70abc8954](https://github.com/lm846802297-bit/axial-vector-review-response/commit/51a245b0a36703f40c24ca469d6969e70abc8954)。本次进一步纠正研究范围：Major Point 3/4.1 的额外中微子完成机制只属于对应问题的专门回复论证，不改变原论文 UV 场内容，也不改变其他审稿问题的模型基准。

**2026-11-05 统一原则（DEC-15）：** 原论文单 VEV 模型是所有非中微子问题的默认基准；Major 3/4.1 可独立讨论中微子机制；不同模型公式和实验限制不得未经重新推导或 matching 直接混用；回复信讨论扩展不代表论文已采用；每个问题必须明确模型、场内容、理论输入、参数关系、近似、适用范围和证据来源。目标是回应原论文的审稿质疑，而不是逐步把论文扩展成另一个 UV 模型。详见研究决策登记表 DEC-15 与审稿回复写作原则 §2.1。

- **旧 PR #30：** 已关闭且未合并；其错误采用双 VEV 映射的 PR #51 也已关闭且未合并。现由 [PR #53](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) 替代。PR #53 从当前 main 创建，严格使用原论文单 VEV 模型 \(m_{A'}=2|g_X|v_s\)、\(G=a_s\)，保留通用电流半康普顿振幅和局部热率计算。六项单 VEV 映射测试通过；介质静止系 T/L opacity、trapping、SN profile 和最终 SN1987A/LESN 曲线仍未完成。
- **旧 PR #32：** 已关闭且未合并；现由 [PR #52](https://github.com/lm846802297-bit/axial-vector-review-response/pull/52) 替代。PR #52 从当前 main 创建，研究原论文的单 VEV 径向标量，保留 Belle II 来源台账、重铸协议、逐点分类框架和部分宽度计算器。Belle II 逐质量补充数据提取、实验 benchmark 复现、完整宽度/分支比/寿命、产生率、接受度和质量扫描仍未完成。
- **PR #52：** 已 Closed、未合并；其研究分支 `research/radial-scalar-original-model-belleii-20261105` 仍保留，研究成果未合并、未删除。
- **PR #53：** 保持 Open / Draft；其研究分支 `research/stellar-cooling-original-uv-model-20261105` 独立保留。
- PR #52/#53 均不修改论文正文或正式回复信，也不是当前审稿回复的前置条件。PR #56 仅补充正式回复信 Major 4.4 的条件性轴矢量 EFT 冷却论证和图，不修改论文正文，也不引入额外中微子场。旧 PR 的讨论和提交保留作历史溯源，不合并其错误模型范围的提交。

- **PR #54：** 已合并至 `main`，合并提交为 [`0f3816e3e62dd7668fca1d4aee5e8749708f99f2`](https://github.com/lm846802297-bit/axial-vector-review-response/commit/0f3816e3e62dd7668fca1d4aee5e8749708f99f2)。该 PR 修正正式回复信中 Major 1、2、4.2、4.4 对 Major 3 扩展的跨问题引用，并将中微子完成机制限定为 Major 3/4.1 专门回复内容。

**统一模型边界：** 除 Major Point 3/4.1 的专门中微子回复段落外，所有非中微子审稿回复和专题研究均以原论文 \(S+\mathrm{VLL}\) 单 VEV UV 模型为准。不得将 Major Point 3/4.1 中讨论的可选扩展机制作为原论文已经采用的场内容。
## 2026-11-05 更新：PR #53 原论文单 VEV 轴矢量恒星冷却计算（Draft）

[PR #53](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) 从当前 main 的 `d3c8c573e0b219dbcb4be62dc57f77fdc04c4f96` 创建，替代旧 PR #30 及错误采用双 VEV 映射的 PR #51；两者均关闭且未合并。

- **原论文模型映射：** \(S=(v_s+s+ia_s)/\sqrt2\)、\(Q_X(S)=2\)、\(m_{A'}=2|g_X|v_s\)、\(G=a_s\)。在小 VLL 混合 benchmark 下 \(y_{s\ell\ell}=m_\ell/v_s\)，Goldstone/current 关系为 \(m_\ell/v_s=2|g_A^\ell|m_\ell/m_{A'}\)（\(|g_A^\ell|=|g_X|\)）。
- **保留的计算：** 显式 Dirac 旋量半康普顿振幅、EM Ward identity、实验室系/CM 截面对照、Klein–Nishina 对照、轴矢量纵向标度、均匀介质局部热产生率及积分阶数/截断扫描。
- **原模型中微子规范流边界：** \(A'\to\nu\bar\nu\) 仅使用原论文 \(L_\mu-L_\tau\) 活性味规范流（无质量近似下的 \(\nu_\mu,\nu_\tau\)，电子味不耦合）；不引入额外中微子态或质量完成机制。
- **本地验收：** 单 VEV 映射测试 6/6 通过；通用电流半康普顿振幅的 Ward residual 分别为 \(2.252\times10^{-9}\)、\(2.159\times10^{-9}\)；热率 order 10→12 的率和发射率变化分别为 0.0108% 和 0.0202%。详细数值见 PR #53 的 validation record。
- **分支比口径：** PR #53 的 \(\mathrm{BR}_{\nu\bar\nu}\) 数值仅为保留 \(\nu\bar\nu+\mu^+\mu^-\) 的两通道近似；动能混合诱导的 \(e^+e^-\) 及其他开放道未纳入，不能当作完整物理分支比。
- **未完成：** 介质静止系 T/L 分辨吸收、opacity、trapping、SN profile、diffusion 和最终 SN1987A/LESN 曲线；不声称已得到超新星排除。
- **范围：** PR #53 保持 Open / Draft；不修改论文正文或正式回复信。

## 2026-11-05 更新：Major Point 1.3 公式链条与近极点诊断补强（PR #49，已合并）

[PR #49](https://github.com/lm846802297-bit/axial-vector-review-response/pull/49) 的基准为 main SHA 4abcf13c45789f75deee27a4b6a3cc9480639448，分支为 review/major1.3-higgs-portal-higgs-strength-20261104，已于 2026-11-05 合并至 main。本轮仅修改回复信及其内部证据/同步文档，不修改论文正文。

- **P0：** 正式回复补入 \(2\times2\) charged-lepton/VLL 质量矩阵、规范基底 \(h,s\) Yukawa 顶角、质量本征态旋转、\(C,D,K\) 定义和完整质量本征态一圈费米子自能公式。
- **P0：** 补入 exact full-minus-light EFT subtraction、保留的 bubble-plus-contact soft 子集，以及 hard/soft 数值分解。将结果记为 \(\Pi_{hs}^{\mathrm{ret}}\)，并明确该 soft 子集不是完整同阶 EFT soft/counterterm 集，避免把条件性数值写成完整 UV pole 预测。
- **P0：** 修正“zero-tree-level-mixing”歧义：\(\lambda_{HS}^{\mathrm{EFT}}(M_E)=0\) 是匹配 EFT 的局域混合边界；对应 \(\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E}\ne0\)。补充 portal-induced mass entry 与 loop counting。
- **P0：** 将 \(\mu_h^{\mathrm{pole}}\) 改为 \(\delta\mu_h^{(\mathrm{mix,LO})}\)，明确它是 mixing-only leading rate diagnostic，而不是完整物理 pole signal strength。
- **P1：** 明确 \(m_s\) 是未混合对角质量输入；补充 \(\Gamma_s(s\to A'A',\mu^+\mu^-,\tau^+\tau^-)\) 公式及 Benchmark B 的开闭道条件、宽度和非简并极点位置。
- **P1：** 补充 \(\lambda_S\le4\pi\) 对应的 \(m_s^{\max}=\sqrt{8\pi}v_s\)：Benchmark A 为 \(355.4\) GeV，B 为 \(1579.2\) GeV。明确 \(10\)--\(150\) GeV 是 Higgs 极点附近局部诊断窗口，不是整个微扰性区间的扫描。
- **近极点数值：** Plan-C-lite 脚本新增 \(125.20\)--\(125.30\) GeV、\(0.1\) MeV 步长的复数极点局部扫描。相同 1001 点算法已在 in-session Python 环境独立复现；A/B 的 1001 个点均收敛。更新后的仓库脚本尚未在干净容器中整文件重跑，验证记录明确区分了这两类证据。
- **P2-lite：** 已新增 CP-even radial-scalar 三类 bubble 图的解析表达式和可复现数值脚本；正式回复信现直接包含等质量与非等质量 \(\Delta\bar B_0\) 的闭式表达式、Feynman 参数表示及代表性函数值。\(m_s=100\) GeV 与 \(m_s=m_h\) 两点的零动量相减子集数值仍只作为内部诊断：\(m_s=100\) GeV 时子集模长为 A: \(24.7547\) GeV\(^2\)、B: \(0.641797\) GeV\(^2\)，分别为当前保留费米子 \(|\Pi_{hs}^{ret}|\) 的 57.77 和 6.656 倍。闭式结果与 8,000 区间 Simpson 积分对全部 12 个 benchmark/质量/拓扑组合的最大相对差为 \(9.97\times10^{-15}\)，2k/4k/8k/16k 收敛检查通过。该比值只说明不能单凭形式 loop counting 断言标量项相对有限费米子结果必然很小；此子集不是完整两圈 UV--EFT 匹配，不能直接加到 \(\Pi_{hs}^{ret}\) 或作为物理极点修正。Goldstone 顶角已解析列出，但其数值贡献需与 gauge/ghost、混合 VLL--scalar 图及 tadpole/VEV 反项一起处理；近简并区继续标为未评估。详见 2026-11-05/Portal_induced_scalar_loop_power_counting_P2_lite_2026-11-05.md。
- **低能 EFT 交叉核查：** 补充 \(q^2\ll m_s^2,m_{A'}^2\) 下的 scalar four-lepton operator 与 \(A'\)-exchange 系数尺度比较：\(|C_{\mu\mu}^{(s)}/C^{(A')}|\sim4m_\mu^2/m_s^2\leq4.5\times10^{-4}\)（\(m_s\geq10\) GeV），而 \(\tau\tau\) 在 \(m_s=10\) GeV 时仍可达约 \(0.13\)。该比较仅是不同 Lorentz 结构的系数量级，不是过程级率比；不据此忽略 tau-sensitive scalar processes。
- **范围：** Major 1.3 继续只讨论原始单标量 \(S+\mathrm{VLL}\) 两态系统，不混入 \(\sigma,N_R,\mathrm{PMNS}\) 或三态标量势；近简并区不赋予 allowed/excluded 状态。

**验证边界：** 没有运行 CI；没有对更新后的 Plan-C-lite 脚本做干净容器整文件执行；回复信 PDF 尚未按 PR #49 的 TeX 重编译或视觉检查。main 根目录现有 48 页 PDF 仍是 PR #49 修改前的旧版，不包含 PR #49 的 TeX 修改。PR #49 已于 2026-11-05 合并。

## 2026-11-05 更新：回复信解析论证一致性修订（PR #50，已合并）

[PR #50](https://github.com/lm846802297-bit/axial-vector-review-response/pull/50) 已 Squash Merge，合并提交为 [51a245b0a36703f40c24ca469d6969e70abc8954](https://github.com/lm846802297-bit/axial-vector-review-response/commit/51a245b0a36703f40c24ca469d6969e70abc8954)；分支为 review/response-analytic-consistency-20261105。正式回复信的本轮修改限于以下内容：

- **Minor Point 6.1：** 将 \(g_X\) 上限从旧值 \(10^{-1}\) 修正为实际 Fig. 2 展示窗口的 \(1\)，与 Major Point 2 和 Minor Point 1 一致。
- **Major Point 4.4：** 引入 Kahn et al. (2017) 的轴矢量恒星冷却讨论；用 \(O(10^{-10})\) 表示 Wang--Zhang 矢量参考的 SN1987A 灵敏度；明确 neutrino coalescence 与不可见宽度使用原论文 active-flavor \(L_\mu-L_\tau\) 规范流；不引入额外中微子态、active--heavy mixing 或 Major Point 3 的可选完成机制。
- **Major Point 4.4：** 新增矢量流守恒、轴矢量流散度及 Goldstone 等效纵向耦合关系，解释矢量 semi-Compton 产生率不能直接移植；将低动量 kinetic-mixing 抑制限定为电磁流介导过程，不用于 neutrino coalescence 或直接轴矢量 semi-Compton。
- **Major Point 1.3：** 本轮复核后撤销最初拟议的三处文字精简，恢复 PR #50 修改前 `main` 的原有表述；PR #50 最终不修改该部分，完整保留闭式泡图表达式、UV--EFT 匹配、benchmark 数值、数值验证精度及各子集的适用范围和未完成项。
- 新增 [解析论证完整性审查与修订记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-05/回复信解析论证完整性审查与修订记录_2026-11-05.md)。

**验证边界：** TeX 花括号、环境配对、标签唯一性和 citation-key 静态核查通过；36 个唯一引用键均可解析。新增公式片段通过独立 pdflatex 编译。完整回复信 PDF 尚未重编译或逐页视觉检查；未运行 CI；没有新增超新星输运计算；论文正文未修改。根目录现有 PDF 仍是 2026-11-04-r2 历史编译件，不包含 PR #49/#50 的 TeX 更新。

## 2026-11-04 更新：Major 4.4 轴矢量 stellar-cooling 文献调查（PR #46）

PR #46 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 [b453e9be09a4f67d00cb90dfb85435c07472c5b4](https://github.com/lm846802297-bit/axial-vector-review-response/commit/b453e9be09a4f67d00cb90dfb85435c07472c5b4)。新增文档 [Major 4.4 轴矢量 stellar-cooling 文献适用性调查](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.4-轴矢量stellar-cooling文献适用性调查_2026-11-04.md)，并更新 README 导航与 DEC-09。

调查确认：Kahn et al. 2017 已明确讨论轴矢量 \(U(1)\) 的 stellar cooling，但没有本文模型的 SN1987A 数值曲线；EPS-HEP 2019 有轴矢量核子耦合 SN 报告；Bell et al. 2024 对轴矢量核子流使用的是 vector SN proxy。对本文最直接的定量映射是与常规 \(L_\mu-L_\tau\) 完全相同的中微子 coalescence 与不可见中微子宽度。常规矢量 \(L_\mu-L_\tau\) 的完整 SN 曲线不能直接移植，因为轴矢量缪子 semi-Compton、纵向模式、\(\mu^+\mu^-\) 阈值宽度和 LESN 能量沉积不同。

- 保留“stellar cooling 对 sub-GeV 区域相关”的判断，不把矢量模型曲线作为本文轴矢量模型的完整排除。
- 文档区分直接轴矢量文献、矢量 \(L_\mu-L_\tau\) SN 参考、相同的中微子子过程，以及尚需模型特定计算的部分。
- 不修改回复信 TeX 正文或论文源码；本次仅修复回复信的 BibTeX 构建依赖并补全三条文献元数据，不声称完成新的 SN luminosity、opacity、trapping、LESN 或 WD emissivity 计算。
- 未运行 LaTeX 编译、PDF 视觉检查或 CI；这些状态不作通过声明。
 
### 回复信参考文献与 BibTeX 问号核查（2026-11-04）

作者指出回复信 PDF 中多处引用显示为 `[?]`。对当前根目录权威 TeX 与两份 BibTeX 数据库进行了静态核查：

- 找到 **45 条引用命令、72 次 citation-key 出现、34 个唯一 citation keys**；34 个键全部存在于两份 `.bib` 数据库中。
- 未发现重复 citation keys；两份 BibTeX 文件的花括号静态平衡检查通过；TeX 源码没有 `[?]` 或 `??` 字面占位符。
- 因此，当前源码证据不支持“34 个引用键缺失”的判断。更可能的问题是 BibTeX 生成/读取环节，而不是正文的 `\cite` 键没有对应条目。
- 定位到关键构建隐患：回复信位于仓库根目录，使用 `\bibliographystyle{JHEP}`；原 `JHEP.bst` 仅位于 `overleaf-source/axial-vector-model-building-v6/`。本地 BibTeX 路径测试表明，默认样式搜索不会递归发现任意项目子目录中的 `.bst`。现已将原文件逐字节复制到仓库根目录；其 Git blob SHA-1 与原文件相同：`d39cbe846e531ed7be07eebb11be0bd72d675579`。
- 补全三条被引用文献的元数据：`NA64:2023lightDM` 加入 PRL 131 (2023) 161801 与 DOI；`geiregat1990first` 加入 DOI；`He:2024twoSingletHNL` 加入 arXiv:2401.14687。2026 年的 `Fiorillo:2026wso` 与 `Wang:2026supernova` 仍为预印本，未虚构期刊或 DOI。
- 最新可恢复包为 [2026-11-04-r2 manifest](archive/reply-letter/snapshots/2026-11-04-r2/manifest.md)，包括回复信 TeX、两份 BibTeX 数据库和 `JHEP.bst`。
- **回复信 PDF 已按要求完成重编译与视觉检查（2026-11-04）。** 以源码基线 `edce6a37a162e9fe97b5162bd2107656f50865db` 执行 `pdflatex → bibtex → pdflatex → pdflatex`；BibTeX 成功读取两份数据库及根目录 `JHEP.bst`，生成 34 条文献。最终 PDF 共 48 页，未发现未解析引用/交叉引用或 `[?]`/`??` 标记，所有字体均已嵌入。检查了全篇缩略图及表格、公式、参考文献页；未见裁切、重叠或不可读内容。编译日志保留一条 `Overfull \hbox (44.0084pt too wide)`，对应源码第 757–774 行的 NA64 六列表格（PDF 第 29 页）；该表在视觉检查中仍完整可读。正式 PDF 已提交到仓库根目录。此项没有运行 CI.

 
### 同步补充：正式回复信不可变源码备份

PR #46 同时加入正式回复信归档结构 `archive/reply-letter/`。根目录 TeX 仍是唯一可编辑权威版本；归档目录中的 `.snapshot` 文件只用于恢复，不作为第二份工作稿。

- 源版本固定为 main commit `d9b262798f80c0f109f328b1b0019191e99d5437`。
- 已保存回复信 TeX、两份 BibTeX 输入文件及根目录 `JHEP.bst`；最新 r2 快照的四份归档文件均记录 Git blob SHA-1。
- 归档说明和 manifest 记录原始路径、blob SHA-1、恢复步骤及 GitHub 按 commit SHA 下载完整仓库快照的链接。
- TeX 静态扫描未发现 `\input`、`\include` 或 `\includegraphics` 依赖；`JHEP.bst` 已作为仓库根目录构建依赖保存，LaTeX packages 仍属于编译环境依赖。正式 PDF 已在后续提交 `a9edb509dc47932b872465b5d0dd1263bd1c26da` 中编译并上传；编译来源与 PDF SHA-1 见 [2026-11-04-r2 manifest](archive/reply-letter/snapshots/2026-11-04-r2/manifest.md)。
- Git tag `reply-letter-2026-11-04` 尚未创建。Tag 是 Git ref，不能作为文件纳入 PR diff；建议 PR 合并后将该 annotated tag 指向上述固定源 commit，而不是后续 main HEAD。



## 2026-11-04 更新：Major 4.3 有限矢量耦合与小混合参数域（PR #45）

PR #45 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 `bc2a1c20e277d51ef2d6add68c84b1c5af1c533b`（[GitHub commit](https://github.com/lm846802297-bit/axial-vector-review-response/commit/bc2a1c20e277d51ef2d6add68c84b1c5af1c533b)）。修改前重新阅读了 `AGENTS.md`、`README-先读这里.md`、强制写作规范、main 正式回复信、正文同步清单、DEC-08 和 2026-10-23 第三段会议文字稿。

正式回复 Major 4.3 明确将本文轴矢量现象学限定在有限 VLL 质量下的 `|theta_lL|, |theta_lR| <= 1e-2` 小混合域，并用 `m_l ≃ theta_lL theta_lR M_E` 说明该域对应有限的多 TeV VLL 质量。新增 vector-specific 与 axial 限制映射条件：
`tan^2(theta_lR) < gV_lim(mA')/gA_lim(mA')`，
并说明在角度上限处，矢量专属耦合限制必须比同质量、同假设下的轴矢量限制严格约四个数量级，才可能产生更强的共同 `g_X` 限制。回复保留 trident 与 `(g-2)_mu` 过程贡献比，明确它们不是独立实验排除限；增加 BaBar/Belle II/CMS 四缪子 FSR 在远离阈值区的 vector/axial 同阶 reach 对照；新增 dimuon 阈值的宽度比及质量依赖角度条件，避免将小混合结论推广到阈值敏感衰变或所有实验。

- 修改正式回复信 Major 4.3；新增内部专项推导记录；同步论文正文待修改清单、DEC-08 和本状态文件。
- 不修改论文源码，不新增矢量排除图，不进行全 UV 扫描或 collider recast。
- 静态核验覆盖 TeX 花括号、环境配对、方程标签、公式与现有 benchmark 的一致性；具体结果见 PR 描述。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些验证通过。

## 2026-11-04 更新：Major 3 / 4.1 中微子记号与 S-only 条件性表述（PR #44）

PR #44 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 `e78ae8a4b26a9b595e64ad0eaf52e7e836e50751`。正式回复信统一以 `y^nu_alpha` 表示中微子 Dirac Yukawa 耦合，并保留 `y_e, y_mumu, y_mutau, ...` 作为带电轻子 Yukawa 参数。Major 3 的 `m_D` 定义和 Major 4.1 的重复定义均已同步。

Major 4.1 将 S-only 纹理明确限定为：只有原电荷二标量 S 提供残余 Z2 破缺、没有其他破缺来源时，允许的中微子质量纹理保持 `e ⊕ (mu,tau)` 分块。文字同时明确该纹理是条件性对称性结论，不是原始带电轻子构造已经给出的中微子质量预测。Major 3 的 EFT 段落也统一为相同条件表述。

- 修改文件：正式回复信 TeX、Major 3 专项修改对照、论文正文待同步修改清单。
- 保留原 charged-lepton Yukawa 记号，避免将 `y_e` 等重新解释为中微子 Yukawa。
- 静态检查：中微子 Dirac 项和两处 `m_D` 均使用 `y^nu_alpha`；S-only 条件措辞一致；方程标签唯一；TeX 花括号及环境配对通过。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些检查通过；论文正文未修改。

## 2026-11-04 更新：Major 4.1 PMNS 论证强化（PR #43）

[PR #43](https://github.com/lm846802297-bit/axial-vector-review-response/pull/43) 已于 2026-11-04 通过 Squash Merge 合并至 main，合并提交为 9889beff08d827ede166f196f47fbb94db4a26f8。该修订严格按《审稿回复写作原则》处理 Major 4.1：先精确说明 S-only 残余 Z2 所给出的 U_PMNS = diag(1, U_23) 结构（允许非平凡 μ–τ 旋转，但缺少电子味混合，因此“严格单位矩阵”并不准确）；再给出保留 S、增加电荷一 σ 与三个 N_R 的可重整化完成机制；随后用 seesaw、含 U_L 的 PMNS 关系和 M_R = −m_D^T M_ν^−1 m_D 逆构造展示一般三味混合的构造性实现；最后核对新增单态中微子的异常抵消及双 VEV 的 A′ 质量关系。

- 正式回复只增加面向审稿人的物理论证；没有把分支、PR、内部任务或正文同步状态写入回复信。
- 内部[论文正文待同步修改清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)已同步记录 Major 4.1 的论证结构；论文源码、references 和 PDF 未修改。
- 已做静态检查：TeX 花括号平衡、begin/end 环境配对、无重复 equation label，Major 3 的方程引用和文献键存在。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些检查通过。

## 2026-11-04 更新：Major 4.2 动能混合与 NA64 质量依赖比较

Major 4.2 已补充有限轻子混合产生的非零动能混合、四态矢量耦合/真空极化、物理重态简并与共同裸质量下的残余阈值，并明确重 VLL 匹配尺度边界条件 \(\epsilon_{\rm ind}(\mu_{\rm match})=0\)。该条件只约束独立局域项，不令完整动量依赖物理混合函数为零。

[PR #42](https://github.com/lm846802297-bit/axial-vector-review-response/pull/42) 已于 2026-11-04 通过 Squash Merge 合并至 `main`，合并提交为 `de036d3cbb0fbf654055f5a0d14c67e81bc3061c`。回复 TeX 已扩展 NA64 Fig. 3 的 10、100、200、300 MeV 四点视觉读取区间；300 MeV 计入 dimuon 宽度并使用 `epsilon_eff = |epsilon_gammaA'| sqrt(Br_inv)`。读图区间约有 0.2--0.3 dex 不确定度，明确不是官方机器可读数据或 detector-level recast。按作者决定，本轮未重新编译完整回复 PDF；仓库中的 45 页 PDF 仍是本轮 TeX 更新前的历史快照，不应作为最新回复信使用。CI 状态检查为空。

- [Major 4.2 论证与论文修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-暗光子限制与论文修改对照_2026-11-04.md) 包含 K-01–K-05 正文同步建议、原始文献位置、四点 NA64 对照和适用条件。
- [计算入口](计算脚本/Major42_kinetic/check_kinetic_dark_photon.py) 与 [JSON](计算脚本/Major42_kinetic/outputs/kinetic_dark_photon_2026-11-04.json) 保存四点积分、Br_inv、epsilon_eff、NA64 视觉区间及比值。独立 mpmath 计算在 35/55 位精度下复核；仓库脚本尚未在仓库运行环境直接执行。
- [Major 4.2 验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-验证记录_2026-11-04.md) 记录当前源文件哈希和验证边界。
- **PDF 状态：** 当前 45 页回复 PDF 是本轮扩展前的编译快照，尚未根据最新 TeX 重新编译，不能作为本轮最终 PDF；需要重新编译并逐页检查。
- 原论文源码、bibliography 和 Fig. 2 未改；正文待按清单同步。Major 2/3 的核验哈希作为各自历史快照保留。

## 2026-11-04 已合并：Major 2 参数窗口

本轮基于 PR #40 合并提交 `f3d54dc9ec3c89bb6b8cbd22ecab6a92c4c83c3e`，按作者最新说明修改 Major 2：低质量端 g−2 已在图示实验室约束中主导，其渐近直线可继续延伸，扩图主要重复该区间；高质量端所用现有实验灵敏度减弱。天体物理适用条件与 UV 微扰性解释保留。

[PR #41](https://github.com/lm846802297-bit/axial-vector-review-response/pull/41) 已合并，合并提交 `49edfcee028717de3a315d76b6aad3e10a268e83`。正式回复和 PDF 已完成本轮核验：42 页，34 个引用键可解析，27 段审稿人引文及 Major 3 原文保持不变。

- 核对实际 Fig. 2 后，将回复 Major 2、Minor 1 和 DEC-06 的耦合上限从误写的 0.1 改为图中的 **1**；原图未改。
- [Major 2 修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-Fig2参数范围与论文修改对照_2026-11-04.md) 记录作者思路、推导、文献与 R-01–R-06 正文修改建议；[验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-验证记录_2026-11-04.md) 记录实际检查结果。
- 原论文源码和图文件不在本次修改范围；正文需按清单后续同步。两个作者本地原始 PDF 继续保留，不上传。
- 当前回复 PDF 随本轮更新；Major 3 验证记录的哈希保留为 PR #40 历史快照，避免与同名新 PDF 混淆。

## 2026-11-04 已合并：Major 3 中微子完成机制

作者已明确要求采用本轮文献调查结果修改回复并提交 PR。[PR #40](https://github.com/lm846802297-bit/axial-vector-review-response/pull/40) 已按作者要求合并，合并提交 `f3d54dc9ec3c89bb6b8cbd22ecab6a92c4c83c3e`。该工作原基于 GitHub main `613bca12`；GitHub 是同步到本地的基准，不将旧本地工作稿回推覆盖主线。以下为 PR #40 的成果与验证快照。

- 正式回复 Major 3/4.1 专门讨论双单态 type-I seesaw、详细算符/质量矩阵/PMNS/异常论证；该扩展仅属于中微子回复，不改变原论文场内容。Major 1、2、4.2–4.4 及其他非中微子回答继续使用原论文单 VEV (S+\mathrm{VLL}) 模型。
- 新增回复专用文献文件 `Replies_to_Referee_3_neutrino_references.bib`；归档论文 `main-v6.tex` 和 `references.bib` 未改。
- **原论文需要修改。** [N-01–N-14 修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major3-中微子完成机制与论文修改对照_2026-11-04.md) 列明位置、前后差异及条件；状态为待正文修改。
- 研究决策 DEC-01/02 已按作者新指示更新并保留旧立场；最小 S-only 的分块定理继续成立。
- 作者指定的两份 `审稿意见-gpt/专题研究/2026-11-04-*` 调查/候选稿一并归档；正式回复仍以根目录 TeX 为准。
- 本地两个原始 PDF 按作者要求保留，不纳入本次提交；其余仓库内容从 GitHub 主线更新并跟踪本次 PR 分支。
- 本轮 TeX 完整编译成功（41 页）；32 个引用键和 4 个标签均可解析，27 段审稿人引文与 main 一致。全文缩略图和新增关键页面已检查，详见 [Major 3 验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major3-验证记录_2026-11-04.md)。该记录以源文件 SHA-256 标识核验对象。
- 回复信 PDF 已随 PR #40 一并提交，路径为 [2026-11-04 编译版](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Replies_to_Referee_3_referee_facing_2026-11-04.pdf)，可与同目录的修改对照、验证记录直接比较。
- NuFIT 6.1 中心值上的 seesaw 构造脚本已复跑；完整输入/矩阵/耦合/残差 JSON 和运行入口见 [PMNS 重构结果](计算脚本/PMNS_Major3/outputs/pmns_tree_level_reconstruction_2026-11-04.json) 与 [PMNS 研究更新](审稿意见-gpt/当前执行/PMNS_Major3路线决策与扩展模型解析核查_2026-10-27.md)。该点是树级存在性示例，不是统计拟合或全参数约束结论。

以下为本轮前已合并工作的状态记录；若与本节的中微子路线冲突，以本节和最新决策登记表为准。

## 1. 项目当前阶段

当前项目处于**正式回复信主线已形成、Major/Minor 一致性审查已完成；PR #38、PR #39 均已合并；PR #39 已统一标量约束相关回复并归档 Table II 的详细论文修改方案；论文源码与 bibliography 尚未修改，待后续按清单同步**的阶段。

已完成：
- 完整回复信主线按会议决策整理并合并（PR #33）。
- 回复信最终一致性审查并合并（PR #34）。
- 正式回复信与内部论文修改清单的职责规范已合并（PR #35）。
- 本轮建立项目启动读取机制和可修改的研究决策登记表。

不能据此声称：
- 论文正文已完成所有同步修改；
- 当前 2026-11-03 回复信 TeX 已重新编译并完成 PDF 视觉验收；
- 标量的完整 collider recast 或全质量范围允许区间已经得到；
- 轴矢量模型完整 SN1987A/LESN 输运与排除曲线已经完成。

## 2. 每次启动的最小读取集合

每次开始项目任务，先读：
1. [AGENTS.md](AGENTS.md)：强制规则和任务路由。
2. 本文件：当前项目状态。
3. [README-先读这里.md](README-先读这里.md)：仓库导航。

随后按任务追加读取，不要无差别加载全部历史文件：

| 任务 | 追加读取 |
|---|---|
| 回复信撰写/审查 | [审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md)、[当前回复信](Replies_to_Referee_3_referee_facing_2026-11-03.tex)、[正文待同步清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)，以及对应审稿原文/会议证据 |
| 论文正文修改 | 正文清单、作者选定的活动源文件及依赖、v6 只读基线、相关物理证据 |
| 物理推导/数值研究 | [研究决策动态登记表](审稿意见-gpt/项目规范/研究决策与不可回退事项.md)、v5.7 相关章节、原始模型公式、专题计算账本和原始文献 |
| GitHub/文档维护 | AGENTS、目标目录 README、实际 PR/分支状态和相关验证说明 |

不要每次完整读取 v5.7、所有会议文字稿或全部计算日志；先定位专题，再按需读取证据。

## 3. 当前权威文件

| 文件 | 用途 | 状态 |
|---|---|---|
| [正式回复信 TeX（当前 main 版本）](Replies_to_Referee_3_referee_facing_2026-11-04.tex) | 当前唯一权威回复信 | PR #38 已合并；包含标量偏宽度、可见分支比、Belle 数值阈值条件及 Belle II spin-0 文献修正 |
| [正文待同步清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md) | 内部正文修改追踪 | Table II 专项修改清单已在 PR #39 分支整理；论文正文尚未修改，其他项目仍待核对 |
| [审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md) | 回复信与内部清单的长期规范 | 已合并 |
| [研究决策与不可回退事项](审稿意见-gpt/项目规范/研究决策与不可回退事项.md) | 当前研究立场及变更历史 | 动态文档，允许作者随最新观点修改 |
| [原始论文 v6 PDF](axial_vector_model_building-v6.pdf) | 归档论文事实基线 | 根目录只读归档 |
| [Overleaf v6 源码归档](overleaf-source/axial-vector-model-building-v6/) | v6 源码、文献和图表 | 不能自动假定等于作者当前 Overleaf 工作版本 |
| [原始审稿报告](dw13678_report_1_a.pdf) | 审稿原文 | 核对原文措辞优先使用 PDF |
| [2026-10-23 会议观点总结](审稿意见-gpt/会议记录/2026-10-23/会议观点总结_2026-10-23.md) | 会议决策历史 | 不替代物理核验或作者最新指示 |
| [v5.6 执行手册](审稿意见-gpt/当前执行/审稿意见分析与执行手册_v5.6-主分析全任务映射与原子步骤版-20261019.md) | 任务 ID、依赖、步骤和验收框架 | §0.1 是 2026-10-27 状态快照，不再是最新状态源 |
| [v5.7 技术参考](审稿意见-gpt/审稿意见分析v5.7-物理校核与专题连续阅读版.md) | 物理推导和专题技术参考 | 2026-10-20 版本，按需读取 |

## 4. GitHub 工作状态（本次核验）

### 正式回复信修订（已合并）
- [PR #38：Add scalar partial widths and correct Belle II scalar interpretations](https://github.com/lm846802297-bit/axial-vector-review-response/pull/38)：已于 2026-11-04 合并，Squash commit 为 [f1dec3b9a0142a13444749ea1dfda432287e8b81](https://github.com/lm846802297-bit/axial-vector-review-response/commit/f1dec3b9a0142a13444749ea1dfda432287e8b81)。当前正式回复信为根目录 `Replies_to_Referee_3_referee_facing_2026-11-04.tex`。
- 已补入 s→A′A′、s→ℓ⁺ℓ⁻ 的偏宽度和可见分支比论证，限定 Belle 1 GeV 数值映射的 m_A′ > 0.5 GeV 条件，并纠正 Belle-II:2023ydz 与 Belle-II:2024wtd 的 scalar-specific interpretation 分类。
- 内部正文待同步清单和 2026-11-04 Belle II 文献核查记录已同步更新；论文源码没有修改。

### Table II 回复信修订与论文修改方案（PR #39 已合并）
- [PR #39：Revise referee response and add Table II manuscript revision plan](https://github.com/lm846802297-bit/axial-vector-review-response/pull/39)（已合并，squash commit `76268abf`）：统一 Major Point 1、Minor Point 6.2 和 Summary 的标量约束数值、文献来源及物理适用条件；保留详细的未来论文修改清单。回复信不包含标量约束图；是否在论文中加入配套图留待后续决定。
- PR #39 仅修改正式回复信和内部清单/核查文档；未修改 main-v6.tex 或 references.bib。论文 Table II、正文解释和 Fiorillo v2 的 BibTeX 更新留待后续正文修订。回复信 TeX 尚未编译，PDF 视觉验收尚未完成。

### 已合并
- [PR #33](https://github.com/lm846802297-bit/axial-vector-review-response/pull/33)：按会议决策整理完整回复信。
- [PR #34](https://github.com/lm846802297-bit/axial-vector-review-response/pull/34)：Major/Minor 最终一致性审查；统一 Major 3/4.1 的 PMNS 结论及 Major 1/Minor 5 的 portal 假设。
- [PR #35](https://github.com/lm846802297-bit/axial-vector-review-response/pull/35)：回复信写作规范和项目级读取规则。
- [PR #36](https://github.com/lm846802297-bit/axial-vector-review-response/pull/36)：项目启动读取机制、PROJECT_STATUS 和可修改的研究决策登记表。

### PR 状态汇总
| PR | 状态 | 当前已知边界 |
|---|---|---|
| [#53 原论文单 VEV 轴矢量恒星冷却/半康普顿计算](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) | Open / Draft；2026-11-05 新建 | 原论文单 VEV 映射与局部振幅/热率已验收；完整介质 T/L opacity 和 SN 输运仍未完成 |
| [#56 Major 4.4 轴矢量 EFT ballistic-cooling benchmark](https://github.com/lm846802297-bit/axial-vector-review-response/pull/56) | Open / Draft；2026-11-06 更新 | 固定剖面 EFT benchmark、GeV 竖版回复信图、19 项测试、数值审计和最新 65 页 PDF 构建完成；不是完整 UV 或流体输运分析 |
| [#52 原论文单 VEV 标量 Belle II 后续研究](https://github.com/lm846802297-bit/axial-vector-review-response/pull/52) | Closed / 未合并；保留研究分支 | 保留来源台账、重铸协议和部分宽度框架；Belle II 补充数据提取、benchmark 复现和 UV 重铸尚未完成 |
| [#54 Major 3/4.1 回复范围隔离与原论文模型一致性](https://github.com/lm846802297-bit/axial-vector-review-response/pull/54) | 已合并；2026-11-05 | Major 3/4.1 扩展仅限中微子回复论证；跨问题引用已隔离 |
| [#55 Minor Points 论证扩充与长期写作规范](https://github.com/lm846802297-bit/axial-vector-review-response/pull/55) | 已合并；2026-11-06 | 正式回复信、Minor Points 和写作规范已进入 main |

PR #53 与 PR #56 是两个不同工作流：#53 针对原论文单 VEV UV 模型的进一步恒星冷却研究；#56 是支撑 Major 4.4 的固定剖面 EFT benchmark。#56 不替代 #53，也不代表完整 UV 恒星冷却问题已经解决。#52 已关闭；#54/#55 已合并。

## 5. 正式回复信与论文正文的状态边界

### 正式回复信
- 当前 main 权威回复信为根目录 `Replies_to_Referee_3_referee_facing_2026-11-04.tex`；PR #38 已合并，保留 PR #33/#34 的既有回复主线。
- 本次合并补入 Eq. (33) 的 s→A′A′ 与 s→ℓ⁺ℓ⁻ 偏宽度、visible-branching-ratio 论证；限定 Belle 1 GeV 数值映射只在 m_A′ > 0.5 GeV 时直接适用；并纠正 Belle II 两篇 scalar-specific 搜索的描述。
- 本轮 Major 3 修订版已完整编译并作全文缩略图及关键页面检查，见顶部更新及验证记录；此前未编译状态已由本次验证替代。
- PR #31 生成的 PDF 位于 2026-10-28 历史目录，文件名为 Replies_to_Referee_3_referee_facing_2026-10-28.pdf；它不是当前 2026-11-03 回复信的最终编译件。
- 当前编译件位于本地被忽略的 work/neutrino/latex-build/；未将历史 PDF 当作本轮验证证据。最终对外提交前仍须与已修订论文作整套一致性验收。

### 论文正文
- 仓库保存原始 v6 PDF 和 Overleaf v6 源码归档。
- 2026-11-03 内部清单记录 Introduction、Eq. (27)、Table II、PMNS/Weinberg 算符、Higgs portal、kinetic mixing、有限 vector component、Muon Collider 和 Conclusion 等同步事项。
- 清单中的“待修改”“待决定/修改”“待核对”状态仍应按实际源文件复核。
- **待确认：** 作者当前选定的 Overleaf 工作版本是否与 v6 归档相同。确认前不得将 v6 归档当作活动稿件覆盖式编辑。

## 6. 当前建议的工作顺序

1. 审阅本轮 Major 3 回复与 N-01–N-14 正文修改对照；本轮回复编译和关键页面检查已有验证记录。
2. PR #39 已合并。下一步另行确认作者当前使用的 Overleaf 正文基线，再按已归档清单实施论文修改；不得把未实施的正文修改写成已完成。
3. 优先核对影响主要物理主张的 PMNS、标量约束、portal/mixing 和参数范围；完成后更新清单中的实际正文位置和状态。
4. PR #52 已关闭且保留研究分支；PR #53 继续原论文单 VEV UV 恒星冷却研究；PR #56 作为 Major 4.4 的固定剖面 EFT response-support benchmark 保持 Draft。PR #56 不替代 PR #53，也不作为完整 UV 恒星冷却已完成的证据。未完成工作不得写成已得到的排除结论。
5. 关键 PR 合并、作者改变路线、正文基线更新或专题验收后，更新本文件和相关决策条目。

## 7. 状态可信度约定

- **已核验：** 本次直接检查 main 文件、PR 元数据或可追溯证据。
- **已有记录，需复核：** 历史文档/PR 描述有记录，但本轮未重新执行计算或测试。
- **待确认：** 缺少当前源文件、作者选择或必要证据。
- **未完成：** 当前证据明确表明工作尚未闭环。

本文件是项目管理状态快照，不是物理结果的独立证明。物理结论以模型定义、可复核推导、实际计算和原始实验文献为准。


## 2026-11-10 update: focused 10 MeV research plan

The next research stage is restricted to the high-order energy-resolved escape distribution at the 10 MeV strong-absorption endpoint. The staged plan is [RESEARCH_PLAN_10MEV_HIGH_ORDER_PHASE_SPACE_2026-11-10.md](research/stellar-cooling-constraints-20261105/blinov_reproduction/RESEARCH_PLAN_10MEV_HIGH_ORDER_PHASE_SPACE_2026-11-10.md). It defines the calculation contract, exact baseline/closure gates, the required source-versus-escaped energy/radius/direction distributions, and conditional follow-up diagnostics. No 0.1 or 1 MeV scan or axial-vector curve update is authorized by this stage.

The plan review identified one output-integrity gap before execution: the phase-space script previously archived only the top 80 joint radius-energy-direction cells, which would not allow an independent reconstruction of all one-dimensional marginals. The script now archives the complete non-empty joint table as \`joint_radius_energy_direction_bins\`, while retaining the top-80 convenience view. The workflow and local runbook now require closure of the complete joint source and escaped-luminosity partitions, including their global subregion fractions.

Stage A has confirmed the research branch, PR #57 status, archived profile/Fig. 7 fingerprints, and high-order baseline configuration (200/640/200/32/64; 842 energy nodes after lapse-threshold insertion). The exact baseline strong-end point is \(g=4.171689650228597\times10^{-8}\), \(L_{\rm B.16}=2.4396359573610326\times10^{52}\,\mathrm{erg\,s^{-1}}\), and \(P_{\rm esc}=3.251774019352899\times10^{-4}\). The regression suite contains three tests, but it has **not** been executed in this environment; the long physical calculation has not started. Proceed to Stage A runtime tests and then the single high-order run, without changing the calculation contract.


## 2026-11-10 update: complete joint-table validation and latest execution status

The high-order phase-space script now archives the full non-empty radius-energy-direction joint table. The workflow additionally checks escape-probability closure against the archived baseline and independently reconstructs all radius, energy, and four-bin direction marginals from the full joint table. This prevents the top-80 display subset from being mistaken for a complete partition.

The latest push-triggered workflow, [Run #42666123613](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42666123613), again failed before runner allocation: job exists, but \`steps=null\` and \`logs_url=null\`. Thus neither regression tests nor the high-order physical calculation executed. Do not interpret this as a numerical failure and do not trigger more empty runs. The next valid execution route is a local checkout of this exact branch or GitHub Actions after hosted-runner provisioning is restored.


## 2026-11-11 update: SFHo real-table and Fig. 12 cross-check

P1-IIIe-A/B now has an authenticated local raw-data run and a full local test
execution. The current combined suite passes **35/35** locally and in GitHub Actions. Run
[#42953524476](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42953524476)
downloaded the three original Release ZIPs, verified their SHA-256 values,
extracted the tables, and passed 15/15 plus 20/20 tests with zero skips.
The decoded physical SPP grid contains 1,496,880 cells; the excluded-volume
identity has maximum residual 7.975e-8. The composition table has 1,521,828
physical cells, of which 1,121,375 (73.6861%) are nuclei-containing. Its free
neutron/proton densities reproduce X_n n_B and X_p n_B to 4.44e-16 relative
precision. The composition layer-0 NSE neutron-side input is now documented as
conditional: it is zero and unused in the 400,453 no-nuclei cells and is not
interchangeable with the Extended EOS thermodynamic chemical potential.

P1-IIId Fig. 12 has been extracted from native APS/SCOAP3 PDF vector paths (page 15;
APS SHA-256 d660eb39..., SCOAP3 mirror SHA-256 c3b92fe6...). The E-K temperature profile agrees with the archived
Caputo profile at 55 radii with 0.071% RMS relative residual and with Bollig
Fig. 1 at 391 radii with 0.095% RMS. At ten common radii from 1 to 15 km, the
E-K n,p curves agree with Caputo reconstructed free-neutron/free-proton
profiles at 0.58% RMS each. The upper two density-axis glyphs are visually ambiguous vector outlines, not
extractable text spans; both mappings remain archived, and equal log spacing
plus the same-model comparison selects the corrected mapping without claiming
a definitive typesetting error. The sum n+p
tracks Caputo n_B(1-X_cluster), not total n_B.

This is a cross-publication check of the same Garching SFHo-18.8 model lineage,
not an independent hydrodynamic simulation validation. No raw Garching profile
has been obtained, and no B.2 opacity, pure-vector Fig. 7 result, or axial
cooling curve is changed. Fiorillo Table 1 weighted F_NN averages remain open
because their original space-time weights are not contained in the EOS tables.
The reproducible Fig. 12 vector workflow completed successfully in Run
[#42952924997](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42952924997),
using the checksum-pinned SCOAP3 copy because APS direct download returns HTTP
403 to hosted runners. The reproducible extraction and cross-check scripts and their workflow are in
`research/stellar-cooling-constraints-20261105/blinov_reproduction/`.


**P1-IIId source-version clarification (2026-11-11):** The reproducible
native-vector extraction is tied to the checksum-verified SCOAP3 copy of the
published APS PDF (SHA-256 `c3b92fe6cf2a8bd3fec84925e2baababfe0c707327a68135013f953ed3d87d43`,
2,749,668 bytes), validated in GitHub Actions Run
[#42953625693](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42953625693).
The arXiv v3 PDF is not used for path indexing: although its text/version
matches the published paper, its internal vector-object ordering differs, so
published-PDF path indices 25/181/182 do not identify the corresponding curves
in that file. Numerical cross-checks below remain based on the SCOAP3 source.


**P1-IIId completion / P1-IIIe handoff (2026-11-11):** The final Fig. 12
native-vector extraction, PDF-axis glyph audit, and Caputo/Bollig pointwise
cross-check passed in GitHub Actions
[#42955259591](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42955259591).
The E–K temperature profile has 0.0707% RMS residual against Caputo Fig. 1
(55 common radii) and 0.0953% against Bollig Fig. 1 (391 radii). At ten radii
from 1 to 15 km, E–K free-neutron and free-proton densities agree with Caputo
reconstructions at 0.580% and 0.586% RMS; their sum agrees with
\((1-X_{\rm cluster})n_B\) at 0.574% RMS. Caputo's own Fig. 1/Fig. 4 closure
supports the free-proton reconstruction. The cluster fraction is
\(X_{\rm cluster}=1-Y_n-Y_p\), rising to 8.85% at 15 km. This is a
cross-publication consistency check of the same Garching SFHo-18.8 lineage,
not independent hydrodynamic validation. Next: map the validated
\(T,n_n^{\rm free},n_p^{\rm free}\) profiles onto the authenticated SFHo EOS
tables and calculate local nucleon chemical potentials/occupation factors,
keeping cluster-bound baryons separate. No B.2 opacity, vector Fig. 7 result,
or axial cooling curve is changed.



## 2026-11-11: P1-IIIe-C local Caputo-to-SFHo EOS key-radius mapping

A first local mapping is complete at ten audited Caputo SFHo-18.8 radii from
1 to 15 km, using the official SFHo/FRDM v1.03 EOS files whose extracted
SHA-256 hashes are recorded in the new P1-IIIe-C JSON. The EOS interpolation
coordinate is the total proton fraction \(Y_p^{\rm tot}=Y_e+Y_\mu\), not the
free-proton abundance \(Y_p\). The wrong-coordinate test fails at the
few-percent composition level, while the correct coordinate reproduces
Caputo \(X_n,X_p,X_{\rm cluster}\) at maximum absolute differences
\(2.02\times10^{-5}\), \(1.67\times10^{-5}\), and \(2.67\times10^{-5}\).

The SPP filling factor agrees with the value inferred from Caputo densities
to \(1.74\times10^{-4}\) maximum absolute difference. Direct Fermi-integral
density closure is 0.177% maximum for neutrons and 0.603% for protons.
The chemical-potential correction needed for exact density closure is below
0.18 MeV; the resulting change in \(F_{NN}^{\rm deg}\) is below
\(3.7\times10^{-4}\). The 2048-point quadrature is converged against 512
points at better than \(2\times10^{-13}\) in density.

Local static factors span \(F_{nn}^{\rm deg}=0.242\)--0.731 and
\(F_{pp}^{\rm deg}=0.460\)--0.983. Relative to a vacuum-mass ideal gas at the
same local free-nucleon densities, the EOS effective masses lower these
factors by up to 31.6% (neutrons) and 26.6% (protons) in the inner core.
These are snapshot-local static factors, not Fiorillo Table 1 mass-time
weighted averages; no dynamic response, opacity, transport, or cooling curve
is changed.

The reproducible profile builder, mapping script, input CSV, detailed output,
and report are in
\`research/stellar-cooling-constraints-20261105/blinov_reproduction/\`:
\`build_caputo_profile_key_radii.py\`,
\`map_caputo_sfho_eos_profile.py\`,
\`outputs/caputo_profile_key_radii_2026-11-11.csv\`,
\`outputs/caputo_sfho_eos_profile_key_radii_2026-11-11.csv\`,
\`outputs/caputo_sfho_eos_profile_key_radii_2026-11-11.json\`, and
\`B16_P1IIIE_C_CAPUTO_PROFILE_TO_SFHO_EOS_2026-11-11.md\`.

The independent GitHub Actions profile-map validation is running. Next is to
extend the same mapping from ten key radii to the full 0.05-km Caputo
composition profile, retaining clusters as a separate component.

