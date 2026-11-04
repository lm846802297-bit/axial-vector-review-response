# Higgs portal Plan C-lite：UV–EFT 匹配、导数混合与近简并复数极点

- **日期：** 2026-10-27
- **状态：** 完成参考 benchmark 的 portal 阈值数值化；完成依赖现有有限导数系数的第一轮复数极点诊断；模型专属 Higgs 线形重铸仍未完成。
- **用途：** 为 Major Point 1.3 提供比 Plan B 更一致的 UV–EFT 接口，同时避免把条件性计算写成完整 UV 预测。
- **计算脚本：** [higgs_portal_planC_lite.py](higgs_portal_planC_lite.py)
- **验证记录：** [higgs_portal_planC_lite_validation.txt](higgs_portal_planC_lite_validation.txt)
- **相关研究基线：** [RC-001 UV–EFT 记录](https://github.com/lm846802297-bit/high-energy-theory-research/blob/main/research/RC-001-vll-higgs-singlet-uv-eft.md)；[RC-001 portal boundary 与 B1/B3 记录（PR #9 分支）](https://github.com/lm846802297-bit/high-energy-theory-research/blob/research/rc001-portal-boundary-b1b3-reconciliation-2026-10-27/research/RC-001-portal-boundary-b1b3-reconciliation.md)。

## 1. 本轮回答的物理问题

原稿的 UV 拉格朗日量包含
\[
-y_\ell\bar L_\ell H E_{\ell R}
-\lambda_\ell S_{\ell}\bar E_{\ell L}\ell_R
-M_{E_\ell}\bar E_{\ell L}E_{\ell R}
+\mathrm{h.c.},
\]
其中 \(\ell=\mu,\tau\)，且 \(\tau\) 项使用 \(S^*\)。原稿将重 VLL 取为简并基准 \(M_{E_\mu}=M_{E_\tau}\equiv M_E>10~\mathrm{TeV}\)，并采用 \(|\theta_{\ell L,R}|\leq10^{-2}\)。原稿没有把 \(\lambda_{HS}(H^\dagger H)(S^\dagger S)\) 的重整化边界作为独立输入，也没有给出物理 \(h\)–\(s\) 混合的完整极点解。

本轮选择的参考匹配条件是
\[
\boxed{\lambda_{HS}^{<}(\mu_M)=0,\qquad \mu_M=M_E,}
\]
其中 \(<\) 表示积分掉 VLL 后的 EFT。该条件是为了定义一个标量抑制 benchmark，**不是原稿已经规定的边界，也不是由规范对称性强制的结果**。

## 2. 零动量 portal 阈值与边界条件

在势能约定
\[
V(H,S)\supset \lambda_{HS}(H^\dagger H)(S^\dagger S),
\qquad \mathcal L\supset -V,
\]
RC-001 记录的 \(\overline{\mathrm{MS}}\) 一圈零动量阈值为
\[
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}\sum_{\ell=\mu,\tau}|y_\ell|^2|\lambda_\ell|^2,
\]
\[
\lambda_{HS}^{<}(\mu_M)
=\lambda_{HS}^{>}(\mu_M)+\Delta\lambda_{HS}^{E}
+O(\text{two loops},\text{higher-dimensional matching}).
\]
因此
\[
\lambda_{HS}^{<}(\mu_M)=0
\quad\Longrightarrow\quad
\lambda_{HS}^{>}(\mu_M)=-\Delta\lambda_{HS}^{E}>0.
\]
相反，如果把 \(\lambda_{HS}^{>}(\mu_M)=0\) 作为边界，就会留下 \(\lambda_{HS}^{<}=\Delta\lambda_{HS}^{E}<0\)。这两种选择不是同一物理假设。

### 2.1 数值 benchmark 的选择

采用原稿的领先 seesaw 关系
\[
m_\ell\simeq \theta_{\ell L}\theta_{\ell R}M_E,\qquad
\theta_{\ell L}\simeq\frac{y_\ell v_h}{\sqrt2 M_E},\qquad
\theta_{\ell R}\simeq\frac{\lambda_\ell v_s}{\sqrt2 M_E}.
\]
取 \(M_E=20~\mathrm{TeV}\)、\(\theta_{\mu L}=\theta_{\tau L}=10^{-2}\)，并由轻子质量确定 \(\theta_{\ell R}\)。这是一个明确的代表点，不是全参数空间扫描。

为了把额外的 Yukawa 微扰性要求显式纳入 benchmark，另取
\[
|\lambda_\ell|\leq\sqrt{4\pi}.
\]
该条件**不是原稿原有的联合扫描结果**。在 \(\theta_{\tau L}=10^{-2}\) 时，它给出
\[
v_s\geq \frac{\sqrt2m_\tau}{10^{-2}\sqrt{4\pi}}
=70.886~\mathrm{GeV}.
\]

| 输入/派生量 | Benchmark A：\(A'A'\) 开放 | Benchmark B：\(A'A'\) 关闭 |
|---|---:|---:|
| \(M_E\) | \(20~\mathrm{TeV}\) | \(20~\mathrm{TeV}\) |
| \(v_s\) | \(70.886~\mathrm{GeV}\) | \(315~\mathrm{GeV}\) |
| \(m_{A'}\) | \(10~\mathrm{GeV}\) | \(63~\mathrm{GeV}\) |
| \(g_X=m_{A'}/(2v_s)\) | \(0.07054\) | \(0.1000\) |
| \(\theta_{\mu R}\) | \(5.283\times10^{-4}\) | \(5.283\times10^{-4}\) |
| \(\theta_{\tau R}\) | \(8.884\times10^{-3}\) | \(8.884\times10^{-3}\) |
| \(y_\mu=y_\tau\) | \(1.149\) | \(1.149\) |
| \(\lambda_\mu\) | \(0.2108\) | \(0.04744\) |
| \(\lambda_\tau\) | \(3.5449\) | \(0.7977\) |
| \(\Delta\lambda_{HS}^{E}\) | \(-0.210764\) | \(-0.0106734\) |
| \(\lambda_{HS}^{>}(\mu_M)\) for \(\lambda_{HS}^{<}=0\) | \(+0.210764\) | \(+0.0106734\) |
| \(\lambda_S=m_h^2/(2v_s^2)\) at \(m_s=m_h\) | \(1.5610\) | \(0.07905\) |

Both points lie inside the original Fig. 2 plotting window for \((m_{A'},g_X)\), and satisfy the stated VLL mass/mixing benchmark. Benchmark A saturates the additional \(|\lambda_\tau|\leq\sqrt{4\pi}\) criterion; Benchmark B does not.

### 2.2 为什么不能默认为 UV portal 为零？

若选择 \(\lambda_{HS}^{>}(\mu_M)=0\)，则 \(\lambda_{HS}^{<}=\Delta\lambda_{HS}^{E}\)。在上述两点，
\[
(\mathcal M^2_{\rm loc})_{hs}=\lambda_{HS}^{<}v_hv_s
=\begin{cases}
-3.679\times10^3~\mathrm{GeV}^2,& \text{Benchmark A},\\
-8.278\times10^2~\mathrm{GeV}^2,& \text{Benchmark B}.
\end{cases}
\]
这些局域项不能与“negligible portal mixing”同时默认成立。对 \(m_s=m_h\)，固定对角项的树级质量矩阵会给出很大的混合和质量分裂；对 Benchmark A 的 \(m_s=10~\mathrm{GeV}\)，\(\lambda_{HS}^{<}=-0.2108\) 还低于
\[
\lambda_{HS}>-2\sqrt{\lambda_H\lambda_S}
\]
的树级势能有界下限（约 \(-0.0718\)）。因此，“零 UV portal”在该示例中甚至会破坏低质量 benchmark 的树级有界条件。

这不是说 \(\lambda_{HS}^{<}=0\) 被模型自动预测，而是说明：**如果要保留小混合 benchmark，必须明确指定一个与 VLL 阈值相容的 portal 边界条件。该选择对应 UV portal 与有限 VLL 阈值在匹配尺度上的抵消，不是由对称性保护的自然小量。**

## 3. 导数混合算符的匹配与符号约定

RC-001 给出的源约定为
\[
\Gamma_{\rm inv}^{RC}(s)=s\mathbf 1-\mathcal M_{\rm loc}^2+\Pi_{RC}(s),
\]
并记录有限导数匹配
\[
\Pi_{RC,\rm hard}'(0)
=\frac{q}{16\pi^2}
\left(\ln\frac{M_E^2}{\mu_R^2}-\frac23\right)
+O(M_E^{-4}\ln M_E),
\qquad
q\simeq\sum_{\ell=\mu,\tau}\frac{2m_\ell^2}{v_hv_s}.
\]
相应的 EFT 算符写作
\[
\mathcal L_{\rm EFT}\supset
\frac{c_{\partial HS}}{M_E^2}
\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S),
\qquad
\Delta\Pi_{RC}^{(6)}(s)
=\frac{c_{\partial HS}v_hv_s}{M_E^2}s.
\]
在 \(\mu_R=M_E\) 时，
\[
c_{\partial HS}^{RC}
=-\frac{M_E^2q}{24\pi^2v_hv_s}.
\]
数值为 Benchmark A 的 \(-0.03513\) 和 Benchmark B 的 \(-0.001779\)。

**符号转换：** Plan B 记录把 1PI 振幅定义为 \(-i\Pi_B\)，而 RC-001 使用 \(i\Pi_{RC}\) 的逆传播子约定，因此
\[
\Pi_B=-\Pi_{RC},\qquad
\Pi_{B,\rm hard}'(0)
=-\frac{q}{16\pi^2}
\left(\ln\frac{M_E^2}{\mu_R^2}-\frac23\right).
\]
复数极点计算统一使用
\[
\boxed{
\mathcal D_B^{-1}(s)=
\begin{pmatrix}
s-m_h^2+i m_h\Gamma_h&-\Pi_{hs}^{B}(s)\\
-\Pi_{hs}^{B}(s)&s-m_s^2+i m_s\Gamma_s
\end{pmatrix}.
}
\]
这一步避免了把两份研究记录中相反的 \(\Pi\) 定义直接相加。

**证据边界：** 上述有限导数系数来自 RC-001 的 source-aligned 两点匹配与 EOM-basis reconciliation，但完整的同阶 EFT soft/counterterm 集和独立图级验证仍未完全关闭。因此本报告将其作为有来源的匹配候选输入，并保留这一不确定性，不把它称为完整 UV 预测。

## 4. 匹配后的低能非对角自能

选用 \(\lambda_{HS}^{<}(M_E)=0\)，所以 portal 的维四局域常数项已经由匹配条件吸收；在后续自能中**不再重复加入**同一硬常数阈值。保留低能 \(\mu,\tau\) 泡图、维数五 EFT 接触 tadpole，以及候选的有限导数硬匹配：
\[
\Pi_{hs}^{B,\rm matched}(s;\mu_R)
=\Pi_{hs}^{B,\rm soft}(s;\mu_R)
+s\,\Pi_{B,\rm hard}'(0;\mu_R).
\]
在 \(s=m_h^2\)、\(\mu_R=M_E=20~\mathrm{TeV}\) 时：

| 量 | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\Pi_{hs}^{B,\rm soft}\) [GeV²] | \(-0.437308-0.113174i\) | \(-0.098410-0.025468i\) |
| \(s\,\Pi_{B,\rm hard}'(0)\) [GeV²] | \(+0.024045\) | \(+0.005411\) |
| \(\Pi_{hs}^{B,\rm matched}\) [GeV²] | \(-0.413263-0.113174i\) | \(-0.092999-0.025468i\) |

这是匹配 benchmark 下的条件性结果。它与此前只在 \(\mu_R=m_h\) 将 portal 和导数局域项都设零的 Plan B 数值不同，因为这里显式加入了从 \(M_E\) 匹配得到的有限导数系数。

### 4.1 重整化尺度交叉检查

把软项和导数硬项分别在 \(\mu_R=m_h\) 与 \(\mu_R=M_E\) 评估：

| \(v_s\) | \(\Pi_{\rm matched}(m_h;\mu_R=m_h)\) [GeV²] | \(\Pi_{\rm matched}(m_h;\mu_R=M_E)\) [GeV²] | 实部残差 [GeV²] |
|---:|---:|---:|---:|
| \(70.886\) GeV | \(-0.413850-0.113174i\) | \(-0.413263-0.113174i\) | \(5.87\times10^{-4}\) |
| \(315\) GeV | \(-0.093131-0.025468i\) | \(-0.092999-0.025468i\) | \(1.32\times10^{-4}\) |

导数硬匹配抵消了主要的 \(\ln(M_E^2/\mu_R^2)\) 依赖，但仍存在小的实部残差，主要关联接触 tadpole/局域常数项及尚未闭合的同阶匹配。该残差约为总实部的 \(0.14\%\)，**不能据此宣称完整重整化群/反项闭合已完成**。

## 5. 近简并复数极点：第一轮数值诊断

使用原稿的宽度公式，
\[
\Gamma_s=\Gamma(s\to A'A')+\Gamma(s\to\mu^+\mu^-)+\Gamma(s\to\tau^+\tau^-),
\]
并将 \(h\) 的对角总宽度取为 \(4.07~\mathrm{MeV}\)。计算中保留了 \(\Pi_{hs}^{B}(s)\) 的 \(p^2\) 依赖和轻子泡图的第二张 Riemann sheet 延拓；对角实部吸收到给定 benchmark 质量中，对角宽度在每一对极点附近固定。因而这是比实质量差小角度公式更好的**第一轮复数极点诊断**，但还不是完整的全动量自能极点方案。

### 5.1 两个精确简并 benchmark

| 结果，\(m_s=m_h=125.25\) GeV | Benchmark A：\(m_{A'}=10\) GeV | Benchmark B：\(m_{A'}=63\) GeV |
|---|---:|---:|
| \(v_s\) | \(70.886\) GeV | \(315\) GeV |
| \(\Gamma_s\) | \(3.7468\) GeV | \(0.15894\) MeV |
| \(\Pi_{hs}^{B}(m_h^2)\) [GeV²] | \(-0.413263-0.113174i\) | \(-0.092999-0.025468i\) |
| \(|\Pi/(a-b)|\)，其中 \(a=m_h^2-i m_h\Gamma_h,\ b=m_s^2-i m_s\Gamma_s\) | \(9.14\times10^{-4}\) | \(0.19684\) |
| \(2|\Pi/(a-b)|\)（非厄米混合诊断，不是实混合角） | \(0.00183\) | \(0.39368\) |
| 窄极点 \((m_{\rm pole},\Gamma_{\rm pole})\) | \((125.250001~\mathrm{GeV},4.0727~\mathrm{MeV})\) | \((125.250041~\mathrm{GeV},0.2921~\mathrm{MeV})\) |
| 另一极点 \((m_{\rm pole},\Gamma_{\rm pole})\) | \((125.264006~\mathrm{GeV},3746.39~\mathrm{MeV})\) | \((125.249959~\mathrm{GeV},3.9368~\mathrm{MeV})\) |

结果揭示了两种不同机制：

- **\(A'A'\) 开放时：** \(s\) 很宽，\(\Gamma_s\simeq3.75\) GeV。尽管非对角自能不为零，复数质量差主要由宽度差控制，Higgs-like 极点的 \(|s/h|\) 仅约 \(9.1\times10^{-4}\)，其宽度仍约 \(4.073\) MeV。不能用只含实质量差的 \(|\Pi|/|m_h^2-m_s^2|\) 公式推断强混合。
- **\(A'A'\) 关闭时：** 两个标量都较窄，且共享 \(\mu,\tau\) 衰变道。精确简并时出现明显的宽度重分配：窄极点约 \(0.292\) MeV，Higgs-like 极点约 \(3.937\) MeV；Higgs-like 极点的本征向量诊断 \(|s/h|\simeq0.204\)。两极点质量只相差约 \(0.083\) MeV，实验上无法简单地作为两个独立窄峰处理。

这些是指定边界条件、指定宽度和候选导数系数下的结果；不能直接将它们称为模型专属的 95% CL 排除。

### 5.2 简并点附近的质量依赖

每个条目按极点宽度从窄到宽排列：

| \(m_s\) [GeV] | Benchmark A 极点 \((m_{\rm pole}\,[\mathrm{GeV}],\Gamma\,[\mathrm{MeV}])\) | Benchmark B 极点 \((m_{\rm pole}\,[\mathrm{GeV}],\Gamma\,[\mathrm{MeV}])\) |
|---:|---|---|
| 124.50 | \((125.250001,4.0718)\); \((124.513579,3677.844)\) | \((124.500000,0.1582)\); \((125.250000,4.0698)\) |
| 125.00 | \((125.250001,4.0725)\); \((125.013862,3723.450)\) | \((124.999999,0.1592)\); \((125.250001,4.0694)\) |
| 125.25 | \((125.250001,4.0727)\); \((125.264006,3746.393)\) | \((125.250041,0.2921)\); \((125.249959,3.9368)\) |
| 125.50 | \((125.250001,4.0728)\); \((125.514151,3769.428)\) | \((125.500001,0.1587)\); \((125.250000,4.0706)\) |
| 125.90 | \((125.250000,4.0728)\); \((125.914385,3806.478)\) | \((125.900000,0.1595)\); \((125.250000,4.0702)\) |

在关闭 \(A'A'\) 道的 benchmark 中，按 \(2|\Pi/(a-b)|\geq0.1\) 定义的宽度调节混合诊断区约为
\[
|m_s-m_h|\lesssim7.45~\mathrm{MeV}.
\]
这不是实验排除窗，只是表明需要专门处理复数极点的理论区域。开放 \(A'A'\) 道时，宽度差足够大，该诊断在精确简并点仍低于 \(0.002\)。

## 6. Higgs 约束：非简并 benchmark 的量级比较与近简并边界（2026-11-04 更新）

PDG 2025 年 12 月更新的 Higgs 综述 Sec. 11.3.3 给出的 inclusive global signal strengths 为
\[
\mu_{\rm ATLAS}=1.023^{+0.056}_{-0.053},\qquad
\mu_{\rm CMS}=1.014^{+0.055}_{-0.053}.
\]
两组测量的典型不确定度约为 \(5.3\%\)--\(5.6\%\)。该节的 global-\(\mu\) 与 \(\kappa\)-framework 解释采用单一窄共振和固定信号形状假设；它们不是本文两个标量极点的联合拟合。引用采用已有 BibTeX 键 `ParticleDataGroup:2024cfk`，正文明确标记为 PDG 2025 update。

### 6.1 一个真正非简并、孤立的 125 GeV 极点 benchmark

为避免把近简并双极点误当成单标量，选取 Benchmark B 的 \(m_s=100\) GeV 点作量级比较。此时：
- \(|m_s-m_h|=25.25\) GeV，两个质量极点在物理质量尺度上分离；
- \(m_s>m_h/2\)，所以 \(h\to ss\) 关闭；
- Benchmark B 的 \(m_{A'}=63\) GeV，故 \(s\to A'A'\) 在 \(m_s=100\) GeV 时也关闭；
- 由 exact mass-eigenstate scan 得到 \(2|\Pi_{hs}/(a-b)|=3.39\times10^{-5}\)，因此
\[
\eta_{hs}\equiv\left|\frac{\Pi_{hs}}{a-b}\right|
\simeq1.695\times10^{-5}.
\]

在 one-singlet \(S+\mathrm{VLL}\) reference model、孤立窄极点和 SM 主导道的 leading-order 近似下，
\[
\mu_h^{\rm pole}\simeq\cos^2\theta_{\rm eff}
\simeq1-\eta_{hs}^2
\simeq1-2.87\times10^{-10}.
\]
即 125 GeV Higgs-like pole 的可见率重标度约为 \(2.9\times10^{-8}\%\)，比 PDG 2025 global-\(\mu\) 的约 \(5.3\%\) 不确定度小约 \(1.8\times10^8\) 倍。这里的 \(\eta_{hs}\) 是由固定 matched off-diagonal self-energy 得到的一阶 mass-insertion diagnostic，不是独立求得的物理混合角；这个比较只说明该非简并 one-singlet benchmark 的 125 GeV 极点混合效应远低于当前整体 rate precision。它不是模型特定 likelihood fit，也不约束 100 GeV singlet-like 标量自身的直接搜索。

### 6.2 近简并点不能用单一 \(\cos^2\theta\) 公式

Plan C-lite 的 \(|m_s-m_h|=0.1\) GeV 例子给出约 \(3.85\times10^{-3}\) 的实质量分母诊断量；它仅用于说明分母变小后混合增强，不能直接当作 detector-level global signal-strength shift。PDG 的单窄共振 \(\mu\) 结果不是两个相近标量的联合信号拟合。

在 \(m_s=m_h=125.25\) GeV 处，exact mass-eigenstate calculation 给出：
- \(A'A'\) 开放时，\(\Gamma_s\simeq3.7468\) GeV，\(|\Pi_{hs}/(a-b)|\simeq9.14\times10^{-4}\)；
- \(A'A'\) 关闭时，\(\Gamma_s\simeq0.15894\) MeV，\(|\Pi_{hs}/(a-b)|\simeq0.19685\)，相应 \(2|\Pi_{hs}/(a-b)|\simeq0.39369\)。

对闭道窄宽度 benchmark，固定自能诊断 \(2|\Pi_{hs}/(a-b)|\geq0.1\) 的区间约为 \(|m_s-m_h|\lesssim7.45\) MeV。该区间不是实验排除窗，也不是允许窗。近简并时必须由完整复数 \(2\times2\) 传播子极点、残数、产生/衰变振幅、干涉及实验质量响应决定可观测信号；单一孤立极点的 \(\mu_h\simeq\cos^2\theta\) 近似不适用。

### 6.3 Scope boundary

本节及以上数值结果严格针对原始单标量 \(S\) 与 VLL 构成的两态 \(h\)-\(s\) 系统。计算采用明确给出的 \(S\)-portal 匹配边界和两个参考 benchmark；不包含额外标量场、额外 portal 或三态 CP-even 传播子。因此，这些结果不应被表述为对任意扩展标量扇区的完整 UV 约束。其他场内容的扩展及其独立标量参数关系不属于本 Plan C-lite 计算范围。

### 6.4 近 Higgs 极点的 0.1 MeV 复数极点扫描（2026-11-05）

在原有第二 Riemann sheet 求解器基础上，增加了 \(m_s\in[m_h-50\,\mathrm{MeV},m_h+50\,\mathrm{MeV}]\) 的局部扫描，步长为 \(0.1\,\mathrm{MeV}\)，每个质量点求解
\[
F(s)=(s-a)(s-b)-\Pi_{hs}^{B}(s)\Pi_{sh}^{B}(s)=0,
\quad
a=m_h^2-i m_h\Gamma_h,\quad b=m_s^2-i m_s\Gamma_s.
\]
本实现采用实耦合基准 \(\Pi_{sh}=\Pi_{hs}\)，以常数自能根作为 Newton 初值；在第二 sheet 上保留轻子 \(B_0(s)\) 的动量依赖。对每个点，以较小 \(|s/h|\) 的极点标记为 Higgs-like pole。

扫描结果：

| 量 | Benchmark A：\(A'A'\) 开放 | Benchmark B：\(A'A'\) 关闭 |
|---|---:|---:|
| 局部扫描区间 | \(125.20\)--\(125.30\) GeV | \(125.20\)--\(125.30\) GeV |
| 步长 | \(0.1\) MeV | \(0.1\) MeV |
| Higgs-like pole 的最大 \(|s/h|\) | \(9.152\times10^{-4}\) | \(0.20391\) |
| 最大值附近的 \(m_s\) | \(125.20\) GeV | \(125.2499\) GeV |
| \(|s/h|\geq0.1\) 的采样区间 | 无 | \(125.2467\)--\(125.2532\) GeV |
| Higgs-like pole 质量范围 | \(125.250000775\)--\(125.250000850\) GeV | \(125.249941827\)--\(125.250018922\) GeV |
| Higgs-like pole 宽度范围 | \(4.072650\)--\(4.072727\) MeV | \(3.923605\)--\(4.080541\) MeV |

所有 1001 个质量点的两个 Newton 根均收敛；被选取 Higgs-like 根的最大行列式残差为 \(4.27\times10^{-10}\)（A）和 \(1.09\times10^{-11}\)（B）。\(|s/h|\) 是非厄米极点本征向量的组成诊断，不是极点残数、可观测混合角或 detector-level signal strength。该阈值区间不得与固定自能诊断 \(2|\Pi/(a-b)|\geq0.1\) 的约 \(7.45\) MeV 半宽混为同一个量。

### 6.5 精确有限硬项与复数极点求解器的精度接口

精确质量本征态脚本在 \(p^2=m_h^2\) 给出的保留自能为
\[
\Pi_{hs}^{\mathrm{ret}}(m_h^2)=
\begin{cases}
-0.413277859-0.113173709i\ \mathrm{GeV}^2,&A,\\
-0.093002551-0.025468201i\ \mathrm{GeV}^2,&B.
\end{cases}
\]
Plan C-lite 的动量依赖极点求解器使用 RC-001 的 source-aligned 有限导数硬项，而不是对该精确硬项进行完整复动量解析延拓。两者在 \(m_h^2\) 的总自能差分别为 \(1.4691\times10^{-5}\) 和 \(3.3060\times10^{-6}\ \mathrm{GeV}^2\)，相对差均约 \(3.43\times10^{-5}\)；硬项本身与领先导数近似的相对差为 \(6.11\times10^{-4}\)。因此，复数极点结果是受控的第一轮诊断，不应称为精确全动量 UV 自能的极点解。

### 6.6 微扰性质量上限与局部扫描的区别

由
\[
\lambda_S=\frac{m_s^2}{2v_s^2}\leq4\pi
\quad\Longrightarrow\quad
m_s^{\max}=\sqrt{8\pi}\,v_s
\]
得到：

| 量 | Benchmark A | Benchmark B |
|---|---:|---:|
| \(v_s\) | \(70.886458\) GeV | \(315\) GeV |
| \(m_s^{\max}\)（\(\lambda_S=4\pi\)） | \(355.372\) GeV | \(1579.176\) GeV |
| \(\lambda_S(m_s=100\,\mathrm{GeV})\) | \(0.99505\) | \(0.05039\) |
| \(\lambda_S(m_s=m_h)\) | \(1.56099\) | \(0.07905\) |

因此，\(m_s\in[10,150]\) GeV 是覆盖 Higgs 极点的局部诊断窗口，并非整个微扰性质量区间。对固定 benchmark 的保留一圈 Yukawa 自能，远离 Higgs 极点时
\[
\eta_{hs}\sim
\frac{|\Pi_{hs}^{\mathrm{ret}}(m_h^2)|}{|m_s^2-m_h^2|}
\underset{m_s\gg m_h}{\sim}
\frac{|\Pi_{hs}^{\mathrm{ret}}(m_h^2)|}{m_s^2}.
\]
这说明大质量端的混合诊断具有 \(1/m_s^2\) 的解析抑制；它不是对整个高质量区间的数值扫描，也不构成 scalar direct-search 的全局约束。

### 6.7 非零 UV portal 下的 loop counting

匹配条件 \(\lambda_{HS}^{\mathrm{EFT}}(M_E)=0\) 意味着
\[
\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E}\neq0.
\]
所以“zero-tree-level-mixing”只能指匹配 EFT 在该尺度的局域维四混合项为零，不能用于描述 UV 拉格朗日量。该 UV portal 的数值按构造与一圈 VLL 阈值同阶；带有额外 portal 顶角的标量圈图在这一 loop counting 中属于更高阶。作为参数量级检查，
\[
\frac{\lambda_S}{16\pi^2}=
\begin{cases}
6.30\times10^{-3}\ (m_s=100\,\mathrm{GeV}),\
9.89\times10^{-3}\ (m_s=m_h),&A,\\
3.19\times10^{-4}\ (m_s=100\,\mathrm{GeV}),\
5.01\times10^{-4}\ (m_s=m_h),&B,
\end{cases}
\qquad
\frac{\lambda_H}{16\pi^2}=8.19\times10^{-4}.
\]
这些数字仅估计代表性标量圈的额外耦合/圈因子；没有计算完整的 portal-induced scalar-loop diagrams，也不能据此把它们设为严格零。直接 \(W\)/top 一圈图在规范基底缺少 \(sWW\)、\(s\bar t t\) 顶角；通过 portal 诱导混合产生的相关贡献须按上述更高阶计数处理。

## 7. Plan C-lite 状态与剩余闭环

### 已完成的子任务

- 将原稿 \(M_E>10\) TeV、混合角 benchmark 与额外 Yukawa 微扰性敏感性条件转化为两个明确的代表点。
- 数值评估 \(\overline{\mathrm{MS}}\) 零动量 portal 阈值，并区分零 UV portal 与零匹配 EFT portal。
- 按一致的 \(\Pi_B=-\Pi_{RC}\) 约定组合低能 \(\mu,\tau\) 圈、EFT 接触 tadpole 和 RC-001 有来源的有限导数系数。
- 计算两个衰变宽度极限下的第一轮复数极点诊断；2026-11-05 增加了 Higgs 极点附近 0.1 MeV 步长的局部扫描，并明确其固定对角宽度与硬项导数近似。
- 对 Higgs 整体信号强度完成第一轮适用性判断，明确何处需要完整两极点线形拟合。

### 尚未关闭的项目

1. RC-001 的有限导数系数仍需要完整同阶 EFT soft/counterterm 账本及独立图级验证；本报告将其作为候选输入。bubble-plus-contact 只是保留的 EFT soft 子集，不是完整同阶 soft/counterterm 集。
2. 当前极点计算固定了对角宽度，并吸收对角实部到质量输入；尚未求解包含所有 UV/EFT 对角自能、tadpole/VEV 反项和完整波函数残数的全动量矩阵。精确质量本征态硬项与极点求解器中的导数近似已量化对照，但尚未对精确硬项作完整复动量解析延拓。
3. 尚未运行 HiggsSignals 或模型专属的 LHC 额外标量搜索重铸；近简并窄宽度区域继续标为 **not assessed**，而不是允许或排除。
4. 原论文 TeX、Fig. 2 PDF 和绘图源尚未因本计算自动修改；应先完成以上闭环，再决定哪些结果写入正文和正式回复信。

**当前结论：** Plan C-lite 已经从“只有 Plan B 低能圈图”推进到“显式 portal 阈值 + 候选导数匹配 + 两种宽度情形下的复数极点诊断”。它支持继续保留纯轴矢量有效流结果作为条件性 benchmark，但不支持声称完整 UV 模型在整个 \(m_s\) 范围内的混合已被证明可忽略。
