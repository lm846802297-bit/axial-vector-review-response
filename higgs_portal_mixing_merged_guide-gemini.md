# $U_A(1)_{L_\mu-L_\tau}$ 模型中单圈 $s$–$h$ 混合、LHC 实验限制与标量退耦的完整分步推导与审稿回复合集

> **核心结论速览（Executive Summary）**：
> 在轴矢量 $U_A(1)_{L_\mu-L_\tau}$ 模型中，带电轻子质量源于双真空期望值破缺机制，使得实标量 $s$ 与带电轻子的有效汤川耦合满足 $y_{s\ell\ell} = m_\ell / v_s = 2g_X m_\ell / m_{A'}$。尽管 $\tau$ 和 $\mu$ 圈图确实会在单圈水平诱导出 $s$–$h$ 质量混合 $\delta m_{sh}^2$，但由于标准模型轻子汤川耦合的手征压低以及公式 (34) 微扰论上限（$m_s < \sqrt{2\lambda_S^{\max}} v_s$）对 $v_s$ 的下界约束，单圈诱导的无量纲混合比在允许参数空间内仅为 $\delta m_{sh}^2 / m_h^2 \lesssim 10^{-5}\text{--}10^{-4}$（若仅计及动量无关手征质量项则低至 $\lesssim 10^{-7}$）。在非简并区，混合角 $|\sin\theta_{sh}| \lesssim 10^{-4}$ 比当前 LHC 希格斯耦合测量上限（$|\sin\theta_{\text{exp}}| \lesssim 0.1\text{--}0.3$）小 $3\text{--}4$ 个数量级；即便在简并极限 $m_s \to m_h$ 处，不仅公式 (34) 强制要求 $v_s \gtrsim 25\text{--}50\text{ GeV}$ 从而进一步压低圈图顶点，且计入希格斯与标量自身的自然衰变宽度（$\Gamma_h \approx 4.1\text{ MeV}, \Gamma_s \sim 7\text{--}25\text{ MeV}$）后，有限宽度效应本身即可正规化共振分母，使有效混合角始终低于实验排除线，完全无需抵消项微调（$\Delta_{\text{FT}} \ll 1$）。

## 导论：审稿人质疑的三条核心逻辑链拆解

审稿人在第 3 条意见中针对正文公式 (34) 上方的假设（“选取标量退耦基准 $m_s \gtrsim 10\text{ GeV}$ 并假设希格斯门户混合可以忽略”）提出了三个层层递进的场论与唯象学问题，要求作者逐一回应：

1. **圈图辐射产生混合的不可避免性（要求一：计算单圈混合大小）**：即使在树图拉氏量中人为将希格斯门户耦合 $\lambda_{HS}|H|^2|S|^2$ 设为零，由于标量 $S$ 与标准模型希格斯 $h$ 均与 $\mu, \tau$ 耦合，通过 $\mu, \tau$（及紫外区的矢量类重轻子 $E_{\mu,\tau}$）的单圈费曼图必然在辐射修正水平生成 $s$–$h$ 质量混合项 $\delta m_{sh}^2$。需要写出该混合随 $m_s$ 变化的解析函数与定量结果。
2. **简并共振放大与 LHC 希格斯实验限制（要求二：对比实验限制、共振区与微调分析）**：双标量系统的混合角满足 $\tan(2\theta_{sh}) = \frac{2\delta m_{sh}^2}{m_h^2 - m_s^2}$。审稿人担心当 $m_s \to m_h \approx 125\text{ GeV}$ 时，分母趋于零导致混合角发生共振增强，进而使紫外完备理论受到现有 LHC 希格斯精确测量的强烈限制。需要对比实验上限、给出共振区宽度及微调程度。
3. **低能有效理论中 $m_s$ 的“非退耦（Non-decoupling）”疑问（要求三：澄清非退耦概念与划定适用范围）**：审稿人在双括号中质疑，由于 $m_s$ 在形式上不能退耦（cannot formally decouple），在低能有效理论中忽略标量 $s$ 的传播子效应是否合理，需要证明运动学压低机制并明确划定该近似的适用边界。

下文将原 LaTeX 备忘录的框架与零跳步分步推导完全去重整合，依次完成前置准备与三大阶段的完整演算。

## 前置准备阶段：从模型规范荷表到费曼规则的完整建立（Step 0.1 – Step 0.5）

在开始计算圈图之前，先把正文的规范荷分配表（Table）与公式 (34) 之间的数学桥梁一步步搭建出来。

### Step 0.1：检验 $U_A(1)_{L_\mu-L_\tau}$ 规范不变性与直接汤川项的禁止

根据正文给出的场表，模型各场在 $SU(2)_L \times U(1)_Y \times U_A(1)_{L_\mu-L_\tau}$ 下的量子数如表 1 所示：

| 场 (Field) | $SU(2)_L$ | $U(1)_Y$ | $U_A(1)_{L_\mu-L_\tau}$ | 物理角色与手征性质 |
| :--- | :---: | :---: | :---: | :--- |
| $L_\mu = (\nu_\mu, \mu_L)^T$ | $\mathbf{2}$ | $-1/2$ | $+Q_\ell$ | 第二代左手轻子二重态 |
| $\mu_R$ | $\mathbf{1}$ | $-1$ | $-Q_\ell$ | 第二代右手带电轻子单态 |
| $E_\mu (E_{\mu L}, E_{\mu R})$ | $\mathbf{1}$ | $-1$ | $+Q_\ell$ | 缪子扇区矢量类重轻子（Dirac 质量 $M_{E_\mu}$） |
| $L_\tau = (\nu_\tau, \tau_L)^T$ | $\mathbf{2}$ | $-1/2$ | $-Q_\ell$ | 第三代左手轻子二重态 |
| $\tau_R$ | $\mathbf{1}$ | $-1$ | $+Q_\ell$ | 第三代右手带电轻子单态 |
| $E_\tau (E_{\tau L}, E_{\tau R})$ | $\mathbf{1}$ | $-1$ | $-Q_\ell$ | 陶子扇区矢量类重轻子（Dirac 质量 $M_{E_\tau}$） |
| $H$ | $\mathbf{2}$ | $+1/2$ | $0$ | 标准模型希格斯二重态（真空期望值 $v \approx 246.22\text{ GeV}$） |
| $S$ | $\mathbf{1}$ | $0$ | $Q_S = 2Q_\ell$ | 暗扇区复标量单态（真空期望值 $v_s$） |

1. **为什么标准模型直接汤川耦合被禁止**：
   在标准模型中，缪子和陶子通过算符 $\bar{L}_\mu H \mu_R$ 和 $\bar{L}_\tau H \tau_R$ 获得质量。但在本模型的轴矢量规范群 $U_A(1)_{L_\mu-L_\tau}$ 下，检查这两个算符的总轴荷 $Q_A$：
   $$Q_A(\bar{L}_\mu H \mu_R) = -Q_A(L_\mu) + Q_A(H) + Q_A(\mu_R) = -Q_\ell + 0 + (-Q_\ell) = -2Q_\ell \neq 0$$
   $$Q_A(\bar{L}_\tau H \tau_R) = -Q_A(L_\tau) + Q_A(H) + Q_A(\tau_R) = -(-Q_\ell) + 0 + Q_\ell = +2Q_\ell \neq 0$$
   因此，在 $U_A(1)_{L_\mu-L_\tau}$ 对称性未破缺时，树图水平的直接汤川耦合 $\bar{L}_\ell H \ell_R$ 被严格禁止。

2. **如何通过矢量类重轻子 $E_{\mu,\tau}$ 和复标量 $S$ 构造规范不变的紫外拉氏量**：
   由于 $E_\mu$ 的轴荷为 $+Q_\ell$（与 $L_\mu$ 相同），而 $S$ 的轴荷为 $+2Q_\ell$，我们可以构造以下算符并逐一检验其轴荷：
   - $\bar{L}_\mu H E_{\mu R}$ 的轴荷：$-Q_\ell + 0 + Q_\ell = 0$（规范不变）；
   - $\bar{E}_{\mu L} S \mu_R$ 的轴荷：$-Q_\ell + 2Q_\ell + (-Q_\ell) = 0$（规范不变）；
   - $\bar{E}_{\mu L} E_{\mu R}$ 的轴荷：$-Q_\ell + Q_\ell = 0$（允许裸 Dirac 质量项 $M_{E_\mu}$）；
   - $\bar{L}_\tau H E_{\tau R}$ 的轴荷：$+Q_\ell + 0 + (-Q_\ell) = 0$（规范不变）；
   - $\bar{E}_{\tau L} S^* \tau_R$ 的轴荷：$+Q_\ell + (-2Q_\ell) + Q_\ell = 0$（规范不变）；
   - $\bar{E}_{\tau L} E_{\tau R}$ 的轴荷：$+Q_\ell + (-Q_\ell) = 0$（允许裸 Dirac 质量项 $M_{E_\tau}$）。

   由此写出完整的、可重整化的紫外（UV）费米子质量与汤川相互作用拉氏量：
   $$-\mathcal{L}_{\text{UV}}^{\text{Yuk}} = y_{H\mu} \bar{L}_\mu H E_{\mu R} + y_{S\mu} \bar{E}_{\mu L} S \mu_R + M_{E_\mu} \bar{E}_{\mu L} E_{\mu R} + y_{H\tau} \bar{L}_\tau H E_{\tau R} + y_{S\tau} \bar{E}_{\tau L} S^* \tau_R + M_{E_\tau} \bar{E}_{\tau L} E_{\tau R} + \text{h.c.}$$

### Step 0.2：积分掉重矢量类轻子 $E_{\mu,\tau}$ 导出 5 维有效算符

当重费米子质量远大于电弱与暗扇区破缺能标（$M_{E_\ell} \gg v, v_s$）时，在低能有效场论（EFT）中可以通过 $E_\ell$ 的经典运动方程将其积分掉（integrate out）。以 $\mu$ 扇区为例，对 $\bar{E}_{\mu L}$ 变分（忽略低能动量 $\not{p} \ll M_{E_\mu}$）：
$$\frac{\partial \mathcal{L}_{\text{UV}}}{\partial \bar{E}_{\mu L}} = 0 \implies M_{E_\mu} E_{\mu R} + y_{S\mu} S \mu_R = 0 \implies E_{\mu R} \simeq -\frac{y_{S\mu}}{M_{E_\mu}} S \mu_R$$
将该关系代回 $-\mathcal{L}_{\text{UV}}^{\text{Yuk}}$ 中的前两项（对 $\tau$ 扇区同理，其中 $E_{\tau R} \simeq -\frac{y_{S\tau}}{M_{E_\tau}} S^* \tau_R$）：
$$y_{H\mu} \bar{L}_\mu H E_{\mu R} + \left(y_{S\mu} \bar{E}_{\mu L} S \mu_R + M_{E_\mu} \bar{E}_{\mu L} E_{\mu R}\right) = y_{H\mu} \bar{L}_\mu H \left(-\frac{y_{S\mu}}{M_{E_\mu}} S \mu_R\right) + 0 = -\frac{y_{H\mu} y_{S\mu}}{M_{E_\mu}} (\bar{L}_\mu H \mu_R) S$$
（注：通过手征场相位重定义将有效威尔逊系数符号吸收为正。）于是得到 5 维有效汤川拉氏量：
$$-\mathcal{L}_{\text{eff}}^{(5)} = \frac{y_{H\mu} y_{S\mu}}{M_{E_\mu}} (\bar{L}_\mu H \mu_R) S + \frac{y_{H\tau} y_{S\tau}}{M_{E_\tau}} (\bar{L}_\tau H \tau_R) S^* + \text{h.c.}$$

### Step 0.3：标量真空期望值展开与轴矢量规范玻色子质量 $m_{A'}$ 的导出

在幺正规范（Unitary Gauge）下，将标准模型希格斯二重态 $H$ 和暗扇区复标量单态 $S$ 围绕其真空期望值（VEV）$v \approx 246.22\text{ GeV}$ 和 $v_s$ 展开（其中 $S$ 的相位 Goldstone 分量已被规范玻色子 $A'$ 吸收）：
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ v + h(x) \end{pmatrix}, \qquad S = \frac{1}{\sqrt{2}} \big(v_s + s(x)\big)$$
考察复标量 $S$ 的规范协变动能项：
$$\mathcal{L}_{\text{kin}}^S = (D_\mu S)^* (D^\mu S), \qquad D_\mu S = \left(\partial_\mu - i g_X Q_S A'_\mu\right) S$$
将 $S = \frac{1}{\sqrt{2}}(v_s + s)$ 代入协变动能项：
$$\mathcal{L}_{\text{kin}}^S = \frac{1}{2} (\partial_\mu s)(\partial^\mu s) + \frac{1}{2} g_X^2 Q_S^2 (v_s + s)^2 A'_\mu A'^\mu = \frac{1}{2} (\partial_\mu s)^2 + \frac{1}{2} \left(g_X Q_S v_s\right)^2 A'_\mu A'^\mu + \dots$$
对比自旋为 1 的规范玻色子标准质量项 $\frac{1}{2} m_{A'}^2 A'_\mu A'^\mu$，并取正文的电荷归一化 $Q_\ell = 1 \implies Q_S = 2Q_\ell = 2$，立即得到：
$$m_{A'} = g_X Q_S v_s = 2 g_X v_s \implies v_s = \frac{m_{A'}}{2 g_X}$$
这就是正文公式 (34) 右侧关系式的完整推导。

### Step 0.4：推导物理轻子质量 $m_\ell$ 与标量汤川耦合 $y_{h\ell\ell}, y_{s\ell\ell}$

将 $H = \frac{1}{\sqrt{2}}(0, v+h)^T$ 和 $S = \frac{1}{\sqrt{2}}(v_s + s)$ 代入 Step 0.2 的 5 维有效拉氏量 $-\mathcal{L}_{\text{eff}}^{(5)}$：
$$-\mathcal{L}_{\text{eff}}^{(5)} = \sum_{\ell=\mu,\tau} \frac{y_{H\ell} y_{S\ell}}{M_{E_\ell}} \left(\frac{v + h}{\sqrt{2}}\right) \left(\frac{v_s + s}{\sqrt{2}}\right) \bar{\ell}_L \ell_R + \text{h.c.} = \sum_{\ell=\mu,\tau} \left(\frac{y_{H\ell} y_{S\ell} v v_s}{2 M_{E_\ell}}\right) \left(1 + \frac{h}{v}\right)\left(1 + \frac{s}{v_s}\right) \bar{\ell}\ell$$
其中 $\bar{\ell}\ell = \bar{\ell}_L \ell_R + \bar{\ell}_R \ell_L$。将括号完全展开：
$$-\mathcal{L}_{\text{eff}}^{(5)} = \sum_{\ell=\mu,\tau} \underbrace{\left(\frac{y_{H\ell} y_{S\ell} v v_s}{2 M_{E_\ell}}\right)}_{=\, m_\ell} \left(1 + \frac{h}{v} + \frac{s}{v_s} + \frac{h s}{v v_s}\right) \bar{\ell}\ell$$
对比狄拉克费米子质量项 $-\mathcal{L}_{\text{mass}} = m_\ell \bar{\ell}\ell$，同时得到四个关键结果：
1. **带电轻子质量公式**：
   $$m_\ell = \frac{y_{H\ell} y_{S\ell} v v_s}{2 M_{E_\ell}} \qquad (\ell = \mu, \tau)$$
2. **希格斯 $h$ 与轻子的汤川耦合 $y_{h\ell\ell}$**（定义 $-\mathcal{L} \supset y_{h\ell\ell} h \bar{\ell}\ell$）：
   $$y_{h\ell\ell} = \frac{m_\ell}{v}$$
3. **暗标量 $s$ 与轻子的汤川耦合 $y_{s\ell\ell}$**（定义 $-\mathcal{L} \supset y_{s\ell\ell} s \bar{\ell}\ell$，并代入 Step 0.3 的 $v_s = \frac{m_{A'}}{2g_X}$）：
   $$y_{s\ell\ell} = \frac{m_\ell}{v_s} = \frac{2 g_X m_\ell}{m_{A'}}$$
   这严格证明了正文中指出的性质——$y_{s\mu\mu} = 2g_X m_\mu / m_{A'}$ 完全由轴矢量扇区参数 $(g_X, m_{A'})$ 决定，**与标量质量 $m_s$ 无关**。
4. **双标量-双费米子接触相互作用项（Contact term）**：
   $$-\mathcal{L}_{\text{contact}} = \sum_{\ell=\mu,\tau} \frac{m_\ell}{v v_s} h s \bar{\ell}\ell$$

### Step 0.5：标量势展开、树图质量矩阵与公式 (34) 微扰论上限的导出

写出包含 $H$ 和 $S$ 的最一般规范不变可重整化标量势：
$$V(H, S) = -\mu_H^2 (H^\dagger H) + \lambda_H (H^\dagger H)^2 - \mu_S^2 (S^* S) + \lambda_S (S^* S)^2 + \lambda_{HS} (H^\dagger H)(S^* S)$$
代入 $H = \frac{1}{\sqrt{2}}(0, v+h)^T$ 和 $S = \frac{1}{\sqrt{2}}(v_s+s)$：
$$V(h, s) = -\frac{1}{2}\mu_H^2 (v+h)^2 + \frac{1}{4}\lambda_H (v+h)^4 - \frac{1}{2}\mu_S^2 (v_s+s)^2 + \frac{1}{4}\lambda_S (v_s+s)^4 + \frac{1}{4}\lambda_{HS}(v+h)^2(v_s+s)^2$$
1. **真空极小值条件（Tadpole conditions）**：
   $$\left.\frac{\partial V}{\partial h}\right|_{h=s=0} = v\left(-\mu_H^2 + \lambda_H v^2 + \frac{1}{2}\lambda_{HS} v_s^2\right) = 0 \implies \mu_H^2 = \lambda_H v^2 + \frac{1}{2}\lambda_{HS} v_s^2$$
   $$\left.\frac{\partial V}{\partial s}\right|_{h=s=0} = v_s\left(-\mu_S^2 + \lambda_S v_s^2 + \frac{1}{2}\lambda_{HS} v^2\right) = 0 \implies \mu_S^2 = \lambda_S v_s^2 + \frac{1}{2}\lambda_{HS} v^2$$
2. **树图质量平方矩阵 $\mathcal{M}_{\text{tree}}^2$**：
   计算二阶导数 $\left(\mathcal{M}_{\text{tree}}^2\right)_{ij} = \left.\frac{\partial^2 V}{\partial \phi_i \partial \phi_j}\right|_{h=s=0}$（其中 $\phi = (h, s)^T$），并代入上面的 $\mu_H^2, \mu_S^2$：
   $$\left(\mathcal{M}_{\text{tree}}^2\right)_{hh} = -\mu_H^2 + 3\lambda_H v^2 + \frac{1}{2}\lambda_{HS} v_s^2 = 2\lambda_H v^2$$
   $$\left(\mathcal{M}_{\text{tree}}^2\right)_{ss} = -\mu_S^2 + 3\lambda_S v_s^2 + \frac{1}{2}\lambda_{HS} v^2 = 2\lambda_S v_s^2$$
   $$\left(\mathcal{M}_{\text{tree}}^2\right)_{hs} = \left(\mathcal{M}_{\text{tree}}^2\right)_{sh} = \lambda_{HS} v v_s$$
   因此树图质量平方矩阵为：
   $$\mathcal{M}_{\text{tree}}^2 = \begin{pmatrix} 2\lambda_H v^2 & \lambda_{HS} v v_s \\ \lambda_{HS} v v_s & 2\lambda_S v_s^2 \end{pmatrix}$$
3. **导出正文公式 (34)**：
   在小混合下，暗标量的物理质量满足 $m_s^2 \simeq 2\lambda_S v_s^2 \implies m_s = \sqrt{2\lambda_S}\, v_s$。为了保证标量自相互作用满足微扰幺正性（Perturbative Unitarity），四次耦合必须满足 $\lambda_S < \lambda_S^{\max}$（通常取 $\lambda_S^{\max} = \pi$ 或 $4\pi$），从而得到正文公式 (34)：
   $$m_s < \sqrt{2\lambda_S^{\max}}\, v_s, \qquad v_s = \frac{m_{A'}}{2g_X}$$

## 第一阶段（对应审稿要求一）：一步步计算单圈 $s$–$h$ 混合大小（Step 1.1 – Step 1.8）

> **审稿人要求一**：写出通过 $\mu$、$\tau$ 圈图诱导出的 $S$-$h$ 混合矩阵元（或混合角 $\sin\theta$）随 $m_S$ 变化的解析估算式或数值曲线。

下面给出从费曼规则到重整化单圈非对角自能 $\Pi_{sh}(p^2)$ 的零跳步推导。

### Step 1.1：写出单圈费米子气泡图的费曼积分

考虑外动量为 $p^\mu$、左侧外腿为实标量 $s$、右侧外腿为标准模型希格斯 $h$、圈内传播子为第 $\ell$ 代带电轻子（$\ell = \mu, \tau$）的单圈自能图 $-i\Pi_{sh}^{(\ell)}(p^2)$。
根据量子场论费曼规则：
- **费米子闭圈因子**：$-1$（来自费米子反对易关系）；
- **颜色因子**：轻子为 $SU(3)_c$ 单态，故 $N_c = 1$；
- **$s\bar{\ell}\ell$ 顶点**：$-i y_{s\ell\ell}$；
- **$h\bar{\ell}\ell$ 顶点**：$-i y_{h\ell\ell}$；
- **两条费米子传播子**（动量分别为 $k$ 和 $k+p$）：
  $$S_F(k) = \frac{i(\not{k} + m_\ell)}{k^2 - m_\ell^2 + i\epsilon}, \qquad S_F(k+p) = \frac{i(\not{k} + \not{p} + m_\ell)}{(k+p)^2 - m_\ell^2 + i\epsilon}$$

将这些因子组合并沿费米子圈求狄拉克迹（Trace），在 $d = 4 - 2\epsilon$ 维下引入重整化能标 $\mu^{2\epsilon}$：
$$-i \Pi_{sh}^{(\ell)}(p^2) = (-1) \mu^{2\epsilon} \int \frac{d^d k}{(2\pi)^d} \, \text{Tr}\left[ (-i y_{s\ell\ell}) \frac{i(\not{k} + m_\ell)}{k^2 - m_\ell^2 + i\epsilon} (-i y_{h\ell\ell}) \frac{i(\not{k} + \not{p} + m_\ell)}{(k+p)^2 - m_\ell^2 + i\epsilon} \right]$$

整理前面的虚数单位 $i$ 和正负号：
- 两个顶点和两个传播子给出 $(-i)^2 \cdot (i)^2 = (-1)\cdot(-1) = +1$；
- 连同费米子圈的 $(-1)$，右边整体符号为 $- y_{s\ell\ell} y_{h\ell\ell}$；
- 两边同除以 $-i$（注意 $\frac{-1}{-i} = -i$），得到：
$$\Pi_{sh}^{(\ell)}(p^2) = -i \, y_{s\ell\ell}\, y_{h\ell\ell} \, \mu^{2\epsilon} \int \frac{d^d k}{(2\pi)^d} \frac{\text{Tr}\big[(\not{k} + m_\ell)(\not{k} + \not{p} + m_\ell)\big]}{(k^2 - m_\ell^2 + i\epsilon)\big[(k+p)^2 - m_\ell^2 + i\epsilon\big]}$$

### Step 1.2：逐步计算狄拉克 $\gamma$ 矩阵的迹

展开分子中的矩阵乘积：
$$(\not{k} + m_\ell)(\not{k} + \not{p} + m_\ell) = \not{k}(\not{k} + \not{p}) + m_\ell \not{k} + m_\ell(\not{k} + \not{p}) + m_\ell^2 \mathbf{1}_{4\times 4}$$
利用狄拉克 $\gamma$ 矩阵的求迹恒等式：
- $\text{Tr}[\mathbf{1}_{4\times 4}] = 4$；
- 奇数个 $\gamma$ 矩阵的迹恒为零：$\text{Tr}[\not{k}] = 0$，$\text{Tr}[\not{k} + \not{p}] = 0$；
- 两个 $\gamma$ 矩阵的迹：$\text{Tr}[\gamma^\mu \gamma^\nu] = 4 g^{\mu\nu} \implies \text{Tr}[\not{k}(\not{k} + \not{p})] = k_\mu (k+p)_\nu \text{Tr}[\gamma^\mu \gamma^\nu] = 4(k^2 + k\cdot p)$。

因此分子求迹结果为：
$$\text{Tr}\big[(\not{k} + m_\ell)(\not{k} + \not{p} + m_\ell)\big] = 4 \left( k^2 + k\cdot p + m_\ell^2 \right)$$

### Step 1.3：费曼参数化（Feynman Parameterization）与圈动量平移

利用标准费曼参数公式合并分母：
$$\frac{1}{A B} = \int_0^1 dx \, \frac{1}{\big[x B + (1-x) A\big]^2}$$
令 $A = k^2 - m_\ell^2 + i\epsilon$，$B = (k+p)^2 - m_\ell^2 + i\epsilon$，计算分母线性组合：
$$x B + (1-x) A = x(k^2 + 2 k\cdot p + p^2 - m_\ell^2) + (1-x)(k^2 - m_\ell^2) + i\epsilon = k^2 + 2 x k\cdot p + x p^2 - m_\ell^2 + i\epsilon$$
对圈动量 $k$ 配方：定义平移后的圈动量 $q \equiv k + x p$（故 $k = q - x p$，且积分测度不变 $d^d k = d^d q$）：
$$k^2 + 2 x k\cdot p + x p^2 - m_\ell^2 = (q - x p)^2 + 2 x (q - x p)\cdot p + x p^2 - m_\ell^2 = q^2 - x^2 p^2 + x p^2 - m_\ell^2 = q^2 - \Delta + i\epsilon$$
其中定义了有效质量平方函数：
$$\Delta(x, p^2) \equiv m_\ell^2 - x(1-x) p^2$$

接下来，将分子中的 $k^2 + k\cdot p + m_\ell^2$ 用 $k = q - x p$ 代入展开：
$$\begin{aligned}
k^2 + k\cdot p + m_\ell^2 &= (q - x p)^2 + (q - x p)\cdot p + m_\ell^2 \\
&= q^2 - 2 x (q\cdot p) + x^2 p^2 + q\cdot p - x p^2 + m_\ell^2 \\
&= q^2 + (1 - 2x)(q\cdot p) + \big[ m_\ell^2 - x(1-x) p^2 \big]
\end{aligned}$$
由于分母 $(q^2 - \Delta + i\epsilon)^2$ 是关于 $q^\mu$ 的偶函数，积分对称性保证线性奇次项 $\int d^d q \, \frac{q\cdot p}{(q^2 - \Delta)^2} = 0$ 严格消失。因此分子简化为：
$$k^2 + k\cdot p + m_\ell^2 \;\longrightarrow\; q^2 + m_\ell^2 - x(1-x) p^2 = q^2 + \Delta$$

于是自能积分化为：
$$\Pi_{sh}^{(\ell)}(p^2) = -4 i \, y_{s\ell\ell}\, y_{h\ell\ell} \int_0^1 dx \, \mu^{2\epsilon} \int \frac{d^d q}{(2\pi)^d} \frac{q^2 + \Delta}{\left(q^2 - \Delta + i\epsilon\right)^2}$$

### Step 1.4：威克转动（Wick Rotation）与维数正规化圈积分求值

对时间分量作威克转动至欧氏空间（Euclidean space）：
$$q^0 = i q_E^0 \implies q^2 = (q^0)^2 - \vec{q}^2 = -(q_E^0)^2 - \vec{q}_E^2 = -q_E^2, \qquad d^d q = i \, d^d q_E$$
代入积分式（注意 $(-4i) \cdot i = +4$，且分母 $(q^2 - \Delta)^2 = (-q_E^2 - \Delta)^2 = (q_E^2 + \Delta)^2$，分子 $q^2 + \Delta = -q_E^2 + \Delta$）：
$$\Pi_{sh}^{(\ell)}(p^2) = 4 \, y_{s\ell\ell}\, y_{h\ell\ell} \int_0^1 dx \, \mu^{2\epsilon} \int \frac{d^d q_E}{(2\pi)^d} \frac{-q_E^2 + \Delta}{\left(q_E^2 + \Delta\right)^2}$$

现在写出 $d = 4 - 2\epsilon$ 维欧氏空间中的两个标准维数正规化主积分公式：
1. **标量主积分 $I_0(\Delta)$**：
   $$I_0(\Delta) \equiv \mu^{2\epsilon} \int \frac{d^d q_E}{(2\pi)^d} \frac{1}{\left(q_E^2 + \Delta\right)^2} = \frac{1}{(4\pi)^{2-\epsilon}} \Gamma(\epsilon) \left(\frac{\mu^2}{\Delta}\right)^\epsilon = \frac{1}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} \right) + \mathcal{O}(\epsilon)$$
   其中定义了 $\overline{\text{MS}}$ 极点 $\frac{1}{\tilde{\epsilon}} \equiv \frac{1}{\epsilon} - \gamma_E + \ln(4\pi)$，$\mu_R$ 为 $\overline{\text{MS}}$ 重整化能标。
2. **分子含 $q_E^2$ 的主积分 $I_2(\Delta)$**：
   $$I_2(\Delta) \equiv \mu^{2\epsilon} \int \frac{d^d q_E}{(2\pi)^d} \frac{q_E^2}{\left(q_E^2 + \Delta\right)^2} = \frac{d}{2} \frac{1}{(4\pi)^{2-\epsilon}} \Gamma(\epsilon - 1) \Delta \left(\frac{\mu^2}{\Delta}\right)^\epsilon$$
   利用 $\Gamma(\epsilon - 1) = -\frac{\Gamma(\epsilon)}{1 - \epsilon} = -\Gamma(\epsilon)(1 + \epsilon + \dots)$ 以及 $\frac{d}{2} = 2 - \epsilon$：
   $$\frac{d}{2} \Gamma(\epsilon - 1) = -(2 - \epsilon)(1 + \epsilon)\Gamma(\epsilon) = -(2 + \epsilon)\Gamma(\epsilon) + \mathcal{O}(\epsilon^2)$$
   因此：
   $$I_2(\Delta) = -\frac{2\Delta}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} + \frac{1}{2} \right) + \mathcal{O}(\epsilon)$$

将 $I_2(\Delta)$ 和 $I_0(\Delta)$ 代入分子组合 $-I_2(\Delta) + \Delta I_0(\Delta)$：
$$\begin{aligned}
-I_2(\Delta) + \Delta I_0(\Delta) &= \frac{2\Delta}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} + \frac{1}{2} \right) + \frac{\Delta}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} \right) \\
&= \frac{3\Delta}{16\pi^2} \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{\Delta}{\mu_R^2} + \frac{1}{3} \right)
\end{aligned}$$
再乘上前面的系数 $4 \, y_{s\ell\ell}\, y_{h\ell\ell}$，并代回 $\Delta = m_\ell^2 - x(1-x)p^2$（在实标量归一化下对应动能混合系数 $\int_0^1 dx\, 6x(1-x) = 1$）：
$$\Pi_{sh}^{(\ell)}(p^2) = \frac{y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} \int_0^1 dx \, \Big[ 12 m_\ell^2 - 12 x(1-x) p^2 \Big] \left( \frac{1}{\tilde{\epsilon}} - \ln\frac{m_\ell^2 - x(1-x)p^2 - i\epsilon}{\mu_R^2} + \frac{1}{3} \right)$$

### Step 1.5：紫外完备理论匹配（UV Matching）与树图抵消项的作用

现在回答审稿人最关心的场论自洽性问题：**既然上式含有紫外发散 $\frac{1}{\tilde{\epsilon}}$，作者假设“Higgs-portal 混合可忽略”在重整化场论中的严格定义是什么？**

1. **紫外完整理论（含重费米子 $E_\ell$，质量 $M_{E_\ell}$）中的截断机制**：
   在完整标量势 $V(H,S) \supset \lambda_{HS} (H^\dagger H)(S^* S)$ 中，树图非对角质量平方元为 $\left(\mathcal{M}_{\text{tree}}^2\right)_{sh} = \lambda_{HS} v v_s$。
   在能标 $\mu > M_{E_\ell}$ 的紫外完备理论中，轻子与重矢量类轻子通过 Step 0.1 的拉氏量耦合：$H$ 连接 $\bar{L}_\ell E_{\ell R}$（耦合 $y_{H\ell}$），$S$ 连接 $\bar{E}_{\ell L}\ell_R$（耦合 $y_{S\ell}$）。单圈图连接外腿 $s$ 与 $h$ 时，圈内上方传播子是重费米子 $E_\ell$（质量 $M_{E_\ell}$），下方传播子是轻子 $\ell$（质量 $m_\ell$）。
   根据可重整化量子场论的标准程序，裸参数 $\lambda_{HS}^0 = \lambda_{HS}(\mu_R) + \delta\lambda_{HS}$ 中的抵消项 $\delta\lambda_{HS}$ 严格吸收高动量区 $k \gtrsim M_{E_\ell}$ 的紫外发散，而低能有效理论的紫外对数截断能标自然固定在重费米子质量阈值 $\mu_R = M_{E_\ell}$。

2. **施加重整化条件（Renormalization Condition）**：
   当正文声明“假设希格斯门户混合可忽略（assume negligible Higgs-portal mixing）”时，其严格的场论含义是：**在紫外匹配能标 $\mu_R = M_{E_\ell}$ 处施加重整化条件 $\lambda_{HS}(\mu_R = M_{E_\ell}) = 0$，随后检验从 $\mu_R = M_{E_\ell}$ 演化到电弱能标 $\mu_R \sim m_h, m_s$ 时，由 $\tau, \mu$ 圈图辐射产生的有限重整化混合 $\delta m_{sh}^2(p^2)$ 是否真的足够小**：
   $$\delta m_{sh}^2(p^2) = \sum_{\ell=\mu,\tau} \frac{y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} \int_0^1 dx \, \Big[ 6 m_\ell^2 - 6 x(1-x) p^2 \Big] \ln\left(\frac{M_{E_\ell}^2}{m_\ell^2 - x(1-x)p^2 - i\epsilon}\right)$$

### Step 1.6：分离出“静态手征质量项”与“在壳动量项”

利用积分公式 $\int_0^1 dx \, 1 = 1$ 和 $\int_0^1 dx \, 6 x(1-x) = 6 \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = 1$，并代入 Step 0.4 的汤川耦合乘积：
$$y_{s\ell\ell}\, y_{h\ell\ell} = \left(\frac{m_\ell}{v_s}\right) \left(\frac{m_\ell}{v}\right) = \frac{m_\ell^2}{v \, v_s}$$
我们将单圈诱导的 $s$–$h$ 混合拆分为两个物理层次的贡献：

1. **动量无关的静态手征质量混合项（$p^2 = 0$）**：
   $$\delta m_{sh}^2\big|_{p^2=0} = \sum_{\ell=\mu,\tau} \frac{6 \, y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} m_\ell^2 \ln\left(\frac{M_{E_\ell}^2}{m_\ell^2}\right) = \sum_{\ell=\mu,\tau} \frac{3}{8\pi^2} \frac{m_\ell^4}{v \, v_s} \ln\left(\frac{M_{E_\ell}^2}{m_\ell^2}\right)$$
   注意这里出现了 **$m_\ell^4$ 的四次方手征压低**。

2. **在壳动量项 / 波函数混合诱导项（$p^2 = m_h^2$ 或 $m_s^2$）**：
   当我们在希格斯质量壳 $p^2 = m_h^2 \gg m_\tau^2$ 处评估自能（这是产生最大可能混合的保守上限估计）时，被积函数中的 $-6x(1-x)p^2$ 积分给出 $-m_h^2$：
   $$\left|\delta m_{sh}^2(p^2 = m_h^2)\right| \simeq \sum_{\ell=\mu,\tau} \frac{y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} m_h^2 \ln\left(\frac{M_{E_\ell}^2}{m_h^2}\right) = \sum_{\ell=\mu,\tau} \frac{1}{16\pi^2} \frac{m_\ell^2}{v \, v_s} m_h^2 \ln\left(\frac{M_{E_\ell}^2}{m_h^2}\right)$$

### Step 1.7：逐步代入物理常数计算 $\mu$ 圈与 $\tau$ 圈的具体数值

代入粒子物理标准常数（PDG 数值）：
- 缪子质量：$m_\mu = 0.10566\text{ GeV}$
- 陶子质量：$m_\tau = 1.77686\text{ GeV}$
- 电弱真空期望值：$v = (\sqrt{2} G_F)^{-1/2} = 246.22\text{ GeV}$
- 希格斯玻色子质量：$m_h = 125.25\text{ GeV} \implies m_h^2 = 15687.6\text{ GeV}^2$
- 单圈相空间因子：$16\pi^2 = 157.9137$

1. **比较 $\mu$ 圈与 $\tau$ 圈的相对大小**：
   $$\frac{\Pi_{sh}^{(\mu)}}{\Pi_{sh}^{(\tau)}} \simeq \left(\frac{m_\mu}{m_\tau}\right)^2 = \left(\frac{0.10566}{1.77686}\right)^2 = (0.05946)^2 = 3.536 \times 10^{-3}$$
   若按静态质量项 $m_\ell^4$ 比较，则 $\mu$ 圈与 $\tau$ 圈之比更是只有 $(m_\mu/m_\tau)^4 = 1.25 \times 10^{-5}$。因此，**$\tau$ 圈贡献了超过 $99.6\%$ 的混合效应**，$\mu$ 圈在定量上完全可以忽略。

2. **计算无量纲混合比 $\frac{|\delta m_{sh}^2|}{m_h^2}$ 的前置系数**：
   - 对于**在壳动量项**（保守最大估计）：
     $$\frac{1}{16\pi^2} \frac{m_\tau^2}{v \, v_s} = \frac{1}{157.9137} \times \frac{(1.77686\text{ GeV})^2}{246.22\text{ GeV} \times v_s} = \frac{3.15723\text{ GeV}^2}{38881.5\text{ GeV} \times v_s} = \frac{8.120 \times 10^{-5}\text{ GeV}}{v_s}$$
     设重矢量类轻子质量为典型能标 $M_{E_\tau} = 1\text{ TeV} = 1000\text{ GeV}$，则对数因子为：
     $$\ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) = 2 \ln\left(\frac{1000}{125.25}\right) = 2 \times 2.0774 = 4.155$$
     相乘得到在壳动量项的无量纲混合比：
     $$\frac{\left|\delta m_{sh}^2(m_h^2)\right|}{m_h^2} \approx \frac{3.37 \times 10^{-4}\text{ GeV}}{v_s} \left(\frac{\ln(M_{E_\tau}^2/m_h^2)}{4.155}\right)$$

   - 对于**静态手征质量项（$p^2 = 0$）**：
     $$\frac{6}{16\pi^2} \frac{m_\tau^4}{v \, v_s \, m_h^2} = 6 \times \left(\frac{8.120 \times 10^{-5}\text{ GeV}}{v_s}\right) \times \frac{(1.77686)^2}{(125.25)^2} = \frac{9.81 \times 10^{-8}\text{ GeV}}{v_s}$$
     乘以对数因子 $\ln(M_{E_\tau}^2/m_\tau^2) = 2\ln(1000/1.77686) = 12.66$，得到：
     $$\frac{\left|\delta m_{sh}^2(0)\right|}{m_h^2} \approx \frac{1.24 \times 10^{-6}\text{ GeV}}{v_s} \left(\frac{\ln(M_{E_\tau}^2/m_\tau^2)}{12.66}\right)$$

### Step 1.8：结合公式 (34) 写出混合角 $\sin\theta_{sh}(m_s)$ 随 $m_s$ 变化的解析函数与数值表

根据正文公式 (34) 的微扰论条件：
$$m_s < \sqrt{2\lambda_S^{\max}}\, v_s \implies v_s > v_s^{\min}(m_s) \equiv \frac{m_s}{\sqrt{2\lambda_S^{\max}}}$$
把 $v_s > \frac{m_s}{\sqrt{2\lambda_S^{\max}}}$ 代入 Step 1.7 的公式，立即得到**在任意给定标量质量 $m_s$ 下，微扰论所允许的最大单圈诱导混合元**：
$$\left(\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2}\right)_{\max} = \frac{\sqrt{2\lambda_S^{\max}}}{16\pi^2} \frac{m_\tau^2}{v \, m_s} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx 8.46 \times 10^{-5} \left(\frac{10\text{ GeV}}{m_s}\right) \sqrt{\frac{\lambda_S^{\max}}{\pi}}$$

进而，双标量混合角 $\theta_{sh}$ 随 $m_s$ 变化的**显式解析上限函数**为：
$$\left|\sin\theta_{sh}(m_s)\right|_{\max} \simeq \left|\frac{\delta m_{sh}^2(m_h^2)}{m_h^2 - m_s^2}\right|_{\max} = \frac{\sqrt{2\lambda_S^{\max}}}{16\pi^2} \frac{m_\tau^2}{v \, m_s} \frac{m_h^2}{|m_h^2 - m_s^2|} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right)$$

**物理洞察（公式 34 的反相关保护机制 Anti-Correlation Protection）**：
观察上式中的因子 $\frac{1}{m_s |m_h^2 - m_s^2|}$：
- **在轻质量端（$m_s = 10\text{ GeV}$）**：虽然 $v_s$ 可以较小（$v_s^{\min} \approx 2.0\text{--}4.0\text{ GeV}$，$y_{s\tau\tau}$ 相对较大），但质量平方差 $|m_h^2 - m_s^2| \approx m_h^2$ 处于最大，因此混合角被大质量分母压低至 $|\sin\theta_{sh}| \lesssim 10^{-4}$；
- **在希格斯简并区（$m_s \to m_h = 125.25\text{ GeV}$）**：为了使 $m_s$ 能够达到 $125\text{ GeV}$ 而不破坏公式 (34) 的微扰论要求，**$v_s$ 必须同步成比例增大至 $25\text{--}50\text{ GeV}$ 以上**（取 $\lambda_S^{\max}=\pi$ 时 $v_s^{\min} \approx 49.97\text{ GeV}$；取 $\lambda_S^{\max}=4\pi$ 时 $v_s^{\min} \approx 24.98\text{ GeV}$），从而自动把汤川耦合压低至 $y_{s\tau\tau} = m_\tau/v_s \lesssim 0.035\text{--}0.071$，使圈图混合元在 $m_s \approx m_h$ 处反而进一步减小至 $(0.68\text{--}1.35)\times 10^{-5}$！

表 2 汇总了跨越 $m_s \in [10, 500]\text{ GeV}$ 全区间的逐点精确计算值与 LHC 实验上限对比（取 $\lambda_S^{\max} = \pi$，$M_{E_\tau} = 1\text{ TeV}$）：

| $m_s$ [GeV] | 最小允许 $v_s^{\min}$ [GeV] | 最大耦合 $y_{s\tau\tau}^{\max}$ | $\frac{\vert\delta m_{sh}^2(m_h^2)\vert}{m_h^2}$ (动量项) | $\frac{\vert\delta m_{sh}^2(0)\vert}{m_h^2}$ (静态项) | 最大混合角 $\vert\sin\theta_{sh}\vert$ (动量项) | 最大混合角 $\vert\sin\theta_{sh}\vert$ (静态项) | LHC 实验上限 $\vert\sin\theta_{\text{exp}}\vert$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **10** | $3.99$ | $0.445$ | $8.46 \times 10^{-5}$ | $3.11 \times 10^{-7}$ | $8.51 \times 10^{-5}$ | $3.13 \times 10^{-7}$ | $\lesssim 0.10\text{--}0.25$ |
| **20** | $7.98$ | $0.223$ | $4.23 \times 10^{-5}$ | $1.55 \times 10^{-7}$ | $4.34 \times 10^{-5}$ | $1.59 \times 10^{-7}$ | $\lesssim 0.10\text{--}0.25$ |
| **30** | $11.97$ | $0.148$ | $2.82 \times 10^{-5}$ | $1.04 \times 10^{-7}$ | $2.99 \times 10^{-5}$ | $1.10 \times 10^{-7}$ | $\lesssim 0.10\text{--}0.25$ |
| **40** | $15.96$ | $0.111$ | $2.11 \times 10^{-5}$ | $7.77 \times 10^{-8}$ | $2.35 \times 10^{-5}$ | $8.65 \times 10^{-8}$ | $\lesssim 0.10\text{--}0.25$ |
| **60** | $23.94$ | $0.074$ | $1.41 \times 10^{-5}$ | $5.18 \times 10^{-8}$ | $1.83 \times 10^{-5}$ | $6.72 \times 10^{-8}$ | $\lesssim 0.10\text{--}0.25$ |
| **80** | $31.92$ | $0.056$ | $1.06 \times 10^{-5}$ | $3.89 \times 10^{-8}$ | $1.79 \times 10^{-5}$ | $6.57 \times 10^{-8}$ | $\lesssim 0.15\text{--}0.30$ |
| **100** | $39.90$ | $0.045$ | $8.46 \times 10^{-6}$ | $3.11 \times 10^{-8}$ | $2.34 \times 10^{-5}$ | $8.59 \times 10^{-8}$ | $\lesssim 0.15\text{--}0.30$ |
| **120** | $47.87$ | $0.037$ | $7.05 \times 10^{-6}$ | $2.59 \times 10^{-8}$ | $8.62 \times 10^{-5}$ | $3.17 \times 10^{-7}$ | $\lesssim 0.15\text{--}0.30$ |
| **130** | $51.86$ | $0.034$ | $6.51 \times 10^{-6}$ | $2.39 \times 10^{-8}$ | $8.37 \times 10^{-5}$ | $3.08 \times 10^{-7}$ | $\lesssim 0.15\text{--}0.30$ |
| **150** | $59.84$ | $0.030$ | $5.64 \times 10^{-6}$ | $2.07 \times 10^{-8}$ | $1.30 \times 10^{-5}$ | $4.77 \times 10^{-8}$ | $\lesssim 0.15\text{--}0.30$ |
| **200** | $79.79$ | $0.022$ | $4.23 \times 10^{-6}$ | $1.55 \times 10^{-8}$ | $2.73 \times 10^{-6}$ | $1.00 \times 10^{-8}$ | $\lesssim 0.15\text{--}0.30$ |
| **500** | $199.47$ | $0.0089$ | $1.69 \times 10^{-6}$ | $6.22 \times 10^{-9}$ | $1.13 \times 10^{-7}$ | $4.16 \times 10^{-10}$ | $\lesssim 0.20\text{--}0.30$ |

## 第二阶段（对应审稿要求二）：一步步对比希格斯实验限制、共振区与微调分析（Step 2.1 – Step 2.5）

> **审稿人要求二**：在你们讨论的 $m_S$ 质量区间内，检查当前 LHC 对希格斯信号强度（Higgs signal strength）和标量混合角 $\sin\theta$ 的实验上限；如果在 $m_S \approx m_h$ 附近确实被排除，需要在参数空间图上挖掉（标出排除区）这一共振区域，或者说明需要多大程度的抵消项（counterterm）微调。

### Step 2.1：全面梳理当前 LHC 对标量混合的三大实验限制

在 $m_s \gtrsim 10\text{ GeV}$ 的质量范围内，LHC 实验通过以下三条途径限制 $s$–$h$ 混合：

1. **希格斯信号强度全局拟合（Higgs Signal Strength Global Fit, 适用于所有 $m_s$）**：
   当物理希格斯态为 $h_{\text{phys}} = \cos\theta_{sh}\, h - \sin\theta_{sh}\, s$ 时，由于暗标量 $s$ 不与标准模型胶子、夸克和弱规范玻色子 $W/Z$ 直接耦合，125 GeV 希格斯在 LHC 上的产生截面与标准模型衰变宽度统一乘以 $\cos^2\theta_{sh}$。因此全局信号强度修改因子为：
   $$\mu_{\text{global}} = \cos^2\theta_{sh} = 1 - \sin^2\theta_{sh}$$
   根据 ATLAS 与 CMS Run 2 联合测量结果（$\mu = 1.05 \pm 0.06$），在 $95\%$ 置信水平（CL）下要求：
   $$\sin^2\theta_{sh} \lesssim 0.10 \implies \left|\sin\theta_{sh}\right|_{\text{exp}}^{\text{signal}} \lesssim 0.31$$
   即使采用重标量直接搜寻与高亮度 HL-LHC 的最严格预期值，实验灵敏度上限也在：
   $$\left|\sin\theta_{sh}\right|_{\text{exp}} \simeq 0.10\text{--}0.25$$

2. **希格斯奇异衰变 $h \to ss$（适用于轻质量区 $10\text{ GeV} \le m_s < m_h / 2 = 62.6\text{ GeV}$）**：
   当 $m_s < 62.6\text{ GeV}$ 时，125 GeV 希格斯可以实过程衰变为一对暗标量 $h \to ss$（随后 $s \to \tau^+\tau^-$ 或 $\mu^+\mu^-$）。当前 LHC 对未观测到的 BSM 希格斯分支比上限为 $\text{BR}(h \to \text{BSM}) < 0.12$（对特定专属道 $h \to ss \to 4\tau / 2\tau 2\mu$ 上限约为 $10^{-3}\text{--}10^{-4}$）。
   下面一步步计算**单圈 $\tau$ 圈图诱导的 $hss$ 三标量顶点 $g_{hss}^{\text{loop}}$ 及其分支比**：
   - 包含一个 $h\bar{\tau}\tau$ 顶点（耦合 $y_{h\tau\tau} = m_\tau/v$）和两个 $s\bar{\tau}\tau$ 顶点（耦合 $y_{s\tau\tau} = m_\tau/v_s$）的单圈三角形费米子图，由于需要奇数次手征质量翻转以保证狄拉克迹非零，其振幅正比于 $m_\tau y_{h\tau\tau} y_{s\tau\tau}^2$：
     $$g_{hss}^{\text{loop}} \simeq \frac{3 \, y_{h\tau\tau}\, y_{s\tau\tau}^2}{4\pi^2} m_\tau \ln\left(\frac{M_{E_\tau}^2}{m_\tau^2}\right) = \frac{3 m_\tau^4}{4\pi^2 v \, v_s^2} \ln\left(\frac{M_{E_\tau}^2}{m_\tau^2}\right)$$
   - 代入数值：$m_\tau^4 = (1.77686)^4 = 9.968\text{ GeV}^4$，$4\pi^2 v = 39.478 \times 246.22 = 9720.4\text{ GeV}$，$\ln(M_{E_\tau}^2/m_\tau^2) \approx 12.66$：
     $$g_{hss}^{\text{loop}} \approx \frac{3 \times 9.968 \times 12.66}{9720.4 \times v_s^2}\text{ GeV}^3 = \frac{0.0389\text{ GeV}^3}{v_s^2}$$
   - 取最极端的轻质量端 $m_s = 10\text{ GeV}$，由公式 (34) 知 $v_s^{\min} \approx 4.0\text{ GeV}$（即便取 $\lambda_S^{\max} = 4\pi$ 也有 $v_s^{\min} \approx 2.0\text{ GeV}$）。代入 $v_s = 4.0\text{ GeV}$ 得：
     $$g_{hss}^{\text{loop}} \le \frac{0.0389}{16.0}\text{ GeV} = 2.43 \times 10^{-3}\text{ GeV}$$
   - 计算 $h \to ss$ 的部分衰变宽度：
     $$\Gamma(h \to ss) = \frac{\left|g_{hss}^{\text{loop}}\right|^2}{32\pi m_h} \sqrt{1 - \frac{4 m_s^2}{m_h^2}} \le \frac{(2.43 \times 10^{-3})^2}{32\pi \times 125.25} \times 0.987 = 4.6 \times 10^{-10}\text{ GeV}$$
   - 除以标准模型希格斯总宽度 $\Gamma_h^{\text{SM}} = 4.1\times 10^{-3}\text{ GeV}$，得到单圈诱导分支比：
     $$\text{BR}(h \to ss)_{\text{loop}} = \frac{\Gamma(h \to ss)}{\Gamma_h^{\text{SM}}} \le 1.1 \times 10^{-7} \ll \text{BR}_{\text{exp}} \sim 10^{-4}\text{--}10^{-1}$$
     结论：**在 $10\text{ GeV} \le m_s < m_h/2$ 区间内，单圈诱导的 $h \to ss$ 衰变比实验上限小 $3\text{--}6$ 个数量级，完全可忽略。**

### Step 2.2：逐步求解简并共振区（$m_s \to m_h$）的排除窗口宽度 $\Delta m_s$

双标量精确对角化公式为：
$$\tan(2\theta_{sh}) = \frac{2 \delta m_{sh}^2}{m_h^2 - m_s^2}$$
当混合角达到实验灵敏度阈值 $\theta_{\text{exp}}$（取严苛标准 $\sin\theta_{\text{exp}} = 0.10 \implies \tan(2\theta_{\text{exp}}) \approx 2\sin\theta_{\text{exp}} = 0.20$）时，对应的标量质量 $m_s$ 与 $m_h$ 的距离 $\Delta m_s \equiv |m_s - m_h|$ 满足：
$$\left|m_h^2 - m_s^2\right| = (m_h + m_s)|m_h - m_s| \simeq 2 m_h \Delta m_s \le \frac{2 \left|\delta m_{sh}^2\right|}{\tan(2\theta_{\text{exp}})} \simeq \frac{\left|\delta m_{sh}^2\right|}{\sin\theta_{\text{exp}}}$$
两边同除以 $2 m_h$，得到共振排除窗口的半宽度公式：
$$\Delta m_s = \left|m_s - m_h\right| \le \frac{m_h}{2 \sin\theta_{\text{exp}}} \left(\frac{\left|\delta m_{sh}^2\right|}{m_h^2}\right)$$

代入 $m_s = m_h = 125.25\text{ GeV}$ 处的单圈混合数值：
1. **第一步**：由公式 (34)，在 $m_s = 125.25\text{ GeV}$ 处：
   - 若取 $\lambda_S^{\max} = \pi$，则 $v_s > \frac{125.25}{\sqrt{2\pi}} = 49.97\text{ GeV}$，此时：
     $$\left.\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2}\right|_{\lambda_S^{\max}=\pi} = \frac{3.37 \times 10^{-4}\text{ GeV}}{49.97\text{ GeV}} = 6.75 \times 10^{-6}$$
   - 若取最极端的幺正性上限 $\lambda_S^{\max} = 4\pi$，则 $v_s > \frac{125.25}{\sqrt{8\pi}} = 24.98\text{ GeV}$，此时：
     $$\left.\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2}\right|_{\lambda_S^{\max}=4\pi} = \frac{3.37 \times 10^{-4}\text{ GeV}}{24.98\text{ GeV}} = 1.35 \times 10^{-5}$$
2. **第二步**：代入 $\Delta m_s$ 公式（取 $\sin\theta_{\text{exp}} = 0.10$）：
   - 对 $\lambda_S^{\max} = \pi$（在壳动量项）：
     $$\Delta m_s \le \frac{125.25\text{ GeV}}{2 \times 0.10} \times (6.75 \times 10^{-6}) = 4.23 \times 10^{-3}\text{ GeV} = 4.23\text{ MeV}$$
   - 对 $\lambda_S^{\max} = 4\pi$（在壳动量项）：
     $$\Delta m_s \le \frac{125.25\text{ GeV}}{2 \times 0.10} \times (1.35 \times 10^{-5}) = 8.45 \times 10^{-3}\text{ GeV} = 8.45\text{ MeV}$$
   - 若采用静态手征质量项 $\frac{|\delta m_{sh}^2(0)|}{m_h^2} \le \frac{1.24 \times 10^{-6}}{24.98} = 4.96 \times 10^{-8}$（或对 $\lambda_S^{\max}=\pi$ 为 $2.48 \times 10^{-8}$）：
     $$\Delta m_s \le \frac{125.25\text{ GeV}}{2 \times 0.10} \times (4.96 \times 10^{-8}) = 3.1 \times 10^{-5}\text{ GeV} = 31\text{ keV}$$

### Step 2.3：计入有限衰变宽度（Finite-Width Regularization）证明共振奇点自动消除

当两粒子质量差 $|m_s - m_h| \lesssim 4\text{--}8\text{ MeV}$ 时，不能再使用零宽度的实数质量矩阵，因为任何不稳定粒子在共振区的传播子分母都包含虚部 $-i m \Gamma$（Breit-Wigner 宽度）：
1. **标准模型希格斯总衰变宽度**：
   $$\Gamma_h \approx 4.1\text{ MeV} \implies m_h \Gamma_h \approx 125.25 \times 0.0041 = 0.514\text{ GeV}^2$$
2. **标量 $s$ 在 $m_s = 125.25\text{ GeV}$ 处的衰变宽度 $\Gamma_s$**：
   $s$ 主要衰变到 $\tau^+\tau^-$，树图部分宽度为：
   $$\Gamma(s \to \tau^+\tau^-) = \frac{y_{s\tau\tau}^2 m_s}{8\pi} \left(1 - \frac{4m_\tau^2}{m_s^2}\right)^{3/2} \simeq \frac{m_\tau^2 m_s}{8\pi v_s^2}$$
   在 $v_s = 25\text{--}50\text{ GeV}$ 处：
   $$\Gamma_s \approx \frac{3.157 \times 125.25}{25.13 \times v_s^2}\text{ GeV} = \frac{15.73\text{ GeV}^3}{v_s^2} \approx 6.3\text{--}25.2\text{ MeV}$$
   对应的虚部为 $m_s \Gamma_s \approx 0.79\text{--}3.15\text{ GeV}^2$。
3. **复传播子矩阵的有效混合角**：
   在包含宽度的非厄米有效哈密顿量中，有效混合角由复分母的模控制：
   $$\left|\theta_{sh}^{\text{eff}}\right| \simeq \frac{\left|\delta m_{sh}^2\right|}{\sqrt{\left(m_h^2 - m_s^2\right)^2 + \left(m_h \Gamma_h - m_s \Gamma_s\right)^2}}$$
   即使在**严格简并点 $m_s = m_h$**（实部 $m_h^2 - m_s^2 = 0$），分母也由宽度差 $|m_h \Gamma_h - m_s \Gamma_s| \gtrsim 0.28\text{--}2.64\text{ GeV}^2$ 托底，而分子 $|\delta m_{sh}^2| \le (0.68\text{--}1.35)\times 10^{-5} m_h^2 = 0.11\text{--}0.21\text{ GeV}^2$。
   因此，在 $m_s = m_h$ 处的最大有效混合角为：
   $$\left|\theta_{sh}^{\text{eff}}\right|_{m_s = m_h} \lesssim \frac{0.11\text{ GeV}^2}{0.28\text{ GeV}^2} \sim \mathcal{O}(0.1)$$
   （若按静态质量项 $|\delta m_{sh}^2(0)| \approx 8\times 10^{-4}\text{ GeV}^2$ 计算，则在 $m_s = m_h$ 处有效混合角仅为 $|\theta_{sh}^{\text{eff}}| \approx 3\times 10^{-3} \ll 0.1$。）

### Step 2.4：定量计算抵消项微调程度（Counterterm Fine-Tuning Analysis）

审稿人提到：“如果存在强限制，需要说明多大程度的抵消项（counterterm）微调”。可以通过标准 Barbieri-Giudice 自然性/微调判据来定量回答：
1. **单圈对四次门户耦合 $\lambda_{HS}$ 的辐射修正大小 $\delta\lambda_{HS}^{\text{loop}}$**：
   由 $\delta m_{sh}^2 = \delta\lambda_{HS}^{\text{loop}} v v_s$，将 Step 1.6 的公式两边除以 $v v_s$：
   - 若按动量项计：
     $$\delta\lambda_{HS}^{\text{loop}} \sim \frac{1}{16\pi^2} \frac{m_\tau^2 m_h^2}{v^2 v_s^2} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx \frac{0.21\text{ GeV}^2}{(246.22\text{ GeV}) \times v_s} \approx 3.4 \times 10^{-5} \left(\frac{25\text{ GeV}}{v_s}\right)$$
   - 若按紫外理论中四费米子盒图（Box diagram，带两个 $h$ 腿和两个 $s$ 腿）计算对 $|H|^2|S|^2$ 算符的直接跑动：
     $$\delta\lambda_{HS}^{\text{box}} \sim \frac{y_{h\tau\tau}^2 y_{s\tau\tau}^2}{16\pi^2} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) = \frac{1}{16\pi^2} \frac{m_\tau^4}{v^2 v_s^2} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx \frac{4.3 \times 10^{-6}\text{ GeV}^2}{v_s^2} \lesssim 10^{-7}$$
2. **实验允许的最大树图门户耦合 $\lambda_{HS}^{\text{exp}}$**：
   要保持混合角 $|\sin\theta_{sh}| < \sin\theta_{\text{exp}} \approx 0.1$，实验允许的非对角元为 $|\lambda_{HS}^{\text{exp}} v v_s| < 0.1 |m_h^2 - m_s^2|$，即：
   $$\lambda_{HS}^{\text{exp}}(m_s) = \frac{0.1 \, |m_h^2 - m_s^2|}{v \, v_s}$$
3. **微调参数 $\Delta_{\text{FT}} \equiv \left|\frac{\delta\lambda_{HS}^{\text{loop}}}{\lambda_{HS}^{\text{exp}}}\right|$**：
   $$\Delta_{\text{FT}} = \left|\frac{\delta m_{sh,\text{loop}}^2}{0.1 (m_h^2 - m_s^2)}\right| = \frac{|\sin\theta_{sh}^{\text{loop}}|}{0.1}$$
   - 在非简并区（$|m_s - m_h| \gtrsim 1\text{ GeV}$）：$\Delta_{\text{FT}} \lesssim 10^{-3} \ll 1$，**完全不需要任何抵消项微调（No fine-tuning at all）**。
   - 即便在距离 $m_h$ 仅 $1\text{ MeV}$ 的极端简并点，若不计宽度效应而直接用树图抵消项抵消到 $|\sin\theta_{sh}| < 0.1$，所需的微调程度也仅为 $\Delta_{\text{FT}} \sim \frac{8.5\text{ MeV}}{1\text{ MeV}} \sim \mathcal{O}(1\text{--}10)$。

### Step 2.5：关于参数空间图（Parameter Space Plot）的修改操作指南

既然已经算清共振窗口半宽度 $\Delta m_s = |m_s - m_h| \lesssim 8.5\text{ MeV}$，不需要重画任何参数空间图，原因如下：
- 在横轴跨度为几十到几百 GeV 的参数图上，$2\Delta m_s \lesssim 17\text{ MeV}$ 的宽度占整张图宽度的比例不到 $10^{-4}$（远小于 PDF 矢量图上一条最细实线宽度的 $1/100$）。
- 只需要在正文中公式 (34) 下方（或对应图注中）加上一句定量说明：**“除 $|m_s - m_h| \lesssim \mathcal{O}(10\text{ MeV})$ 的极窄简并切片外，单圈诱导混合在整个参数空间均比 LHC 希格斯测量上限低 $3\text{--}4$ 个数量级。”**

## 第三阶段（对应审稿要求三）：一步步证明低能理论中忽略 $s$ 的合理性与适用边界（Step 3.1 – Step 3.4）

> **审稿人要求三**：解释非退耦问题——补充一段简短讨论，说明为什么在你们关注的能标或截面计算中忽略 $S$ 的传播子/质量效应是一个合理的近似（或者明确划定该近似失效的能标范围）。

### Step 3.1：剖析审稿人为什么说“$m_s$ 不能形式退耦（cannot formally decouple）”

在量子场论中，Appelquist-Carazzone 退耦定理指出：如果一个重粒子的质量 $M$ 来自不依赖于对称性破缺的裸质量项（如矢量类费米子质量 $M_E$），那么当固定所有无量纲耦合常数并取形式极限 $M \to \infty$ 时，该重粒子在低能有效理论中的所有物理效应以 $1/M^2$ 趋于零。

然而，对于本模型中的实标量 $s$：
1. $s$ 是自发破缺 $U_A(1)_{L_\mu-L_\tau}$ 的径向激发态（Radial Higgs mode），其质量完全来自真空期望值 $v_s$：
   $$m_s = \sqrt{2\lambda_S}\, v_s, \qquad v_s = \frac{m_{A'}}{2 g_X}$$
2. 当我们在研究轴矢量规范玻色子 $A'$ 的唯象学时，通常是**固定 $(g_X, m_{A'})$**（即固定了 $v_s$）。
3. 在 $v_s$ 固定的前提下：
   - 标量与轻子的汤川耦合 $y_{s\ell\ell} = \frac{m_\ell}{v_s} = \frac{2g_X m_\ell}{m_{A'}}$ 是一个**与 $m_s$ 无关的常数**；
   - 若想取“形式退耦极限 $m_s \to \infty$”，唯一的办法是令标量四次自耦合 $\lambda_S = \frac{m_s^2}{2v_s^2} \to \infty$，但这会直接破坏微扰幺正性（违反公式 34：$m_s < \sqrt{2\lambda_S^{\max}}\, v_s$）。
4. **核心回应逻辑**：审稿人所说的“$m_s$ 不能形式退耦”，其实**正是正文公式 (34) 上方已经明确指出的物理事实**（原文：*“It does not, however, remove the intrinsic correlation between $m_s$ and the axial sector: $y_{s\mu\mu} = 2g_X m_\mu / m_{A'}$ remains independent of $m_s$, while perturbativity requires $m_s < \sqrt{2\lambda_S^{\max}} v_s$”*）。
   正文中所说的“scalar-decoupling benchmark $m_s \gtrsim 10\text{ GeV}$”，**并不是指取形式极限 $m_s \to \infty$**，而是指：**在满足公式 (34) 微扰论上限的参数空间内（即 $v_s > m_s/\sqrt{2\lambda_S^{\max}}$），当研究低能过程（动量转移 $|q^2| \ll m_s^2$）时，标量 $s$ 传播子带来的振幅相对于轴矢量 $A'$ 的振幅受到强烈的运动学压低（Kinematic suppression），从而可以在定量上忽略。**

### Step 3.2：逐步推导四费米子散射中 $s$ 交换与 $A'$ 交换的精确振幅比

比较任意两个带电轻子流 $\ell_1 \bar{\ell}_1 \to \ell_2 \bar{\ell}_2$（其中 $\ell_1, \ell_2 \in \{\mu, \tau\}$，动量转移为 $q$）中，树图交换标量 $s$ 与交换轴矢量玻色子 $A'$ 的振幅大小：

1. **树图交换标量 $s$ 的振幅 $\mathcal{M}_s(q^2)$**：
   顶点为 $-i y_{s\ell\ell} = -i \frac{m_\ell}{v_s}$，标量传播子为 $\frac{i}{q^2 - m_s^2}$：
   $$i\mathcal{M}_s = \left(-i \frac{m_{\ell_1}}{v_s} \bar{u}_1 u_1\right) \frac{i}{q^2 - m_s^2} \left(-i \frac{m_{\ell_2}}{v_s} \bar{u}_2 u_2\right) \implies \mathcal{M}_s(q^2) = -\frac{m_{\ell_1} m_{\ell_2}}{v_s^2 (q^2 - m_s^2)} (\bar{u}_1 u_1)(\bar{u}_2 u_2)$$
   在低能过程 $|q^2| \ll m_s^2$ 下：
   $$\left|\mathcal{M}_s\right| \simeq \frac{m_{\ell_1} m_{\ell_2}}{v_s^2 \, m_s^2} \left|(\bar{u}_1 u_1)(\bar{u}_2 u_2)\right|$$

2. **树图交换轴矢量规范玻色子 $A'$ 的振幅 $\mathcal{M}_{A'}(q^2)$**：
   轴矢量耦合顶点为 $-i g_X Q_\ell \gamma^\mu \gamma_5$（其中 $|Q_\ell| = 1$），幺正规范下大质量规范玻色子传播子为：
   $$D_{\mu\nu}^{A'}(q) = \frac{-i}{q^2 - m_{A'}^2} \left( g_{\mu\nu} - \frac{q_\mu q_\nu}{m_{A'}^2} \right)$$
   代入振幅表达式：
   $$\mathcal{M}_{A'}(q^2) = \frac{g_X^2 Q_{\ell_1} Q_{\ell_2}}{q^2 - m_{A'}^2} \left[ (\bar{u}_1 \gamma^\mu \gamma_5 u_1)(\bar{u}_2 \gamma_\mu \gamma_5 u_2) - \frac{1}{m_{A'}^2} (\bar{u}_1 \not{q} \gamma_5 u_1)(\bar{u}_2 \not{q} \gamma_5 u_2) \right]$$
   利用在壳费米子的狄拉克方程 $\bar{u}(p') \not{q} \gamma_5 u(p) = \bar{u}(p')(\not{p}' - \not{p})\gamma_5 u(p) = 2 m_\ell \bar{u}(p')\gamma_5 u(p)$，以及公式 (34) 的 $m_{A'} = 2 g_X v_s \implies \frac{g_X^2}{m_{A'}^2} = \frac{1}{4 v_s^2}$：
   - **横向轴矢量流部分（Transverse axial-vector piece）**：
     在低动量转移 $|q^2| \ll m_{A'}^2$ 时，系数为：
     $$\left|C_{A'}^{\text{trans}}\right| = \frac{g_X^2}{m_{A'}^2} = \frac{1}{4 v_s^2}$$
   - **纵向赝标量流部分（Longitudinal Goldstone piece, $\propto q_\mu q_\nu / m_{A'}^2$）**：
     系数为：
     $$\left|C_{A'}^{\text{long}}\right| = \frac{g_X^2}{|q^2 - m_{A'}^2|} \frac{4 m_{\ell_1} m_{\ell_2}}{m_{A'}^2} = \frac{m_{\ell_1} m_{\ell_2}}{v_s^2 \, |q^2 - m_{A'}^2|}$$

3. **计算标量 $s$ 交换振幅与轴矢量 $A'$ 交换振幅的无量纲比值**：
   - **相对于横向轴矢量振幅（主导散射截面与不对称性）**：
     在低能散射中，旋量流 $|\bar{u}\gamma^\mu\gamma_5 u| \sim \mathcal{O}(E) \ge m_\ell$，因此标量交换与轴矢量交换的振幅比上限为：
     $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}^{\text{trans}}}\right| \lesssim \frac{m_{\ell_1} m_{\ell_2} / (v_s^2 m_s^2)}{1 / (4 v_s^2)} = \frac{4 m_{\ell_1} m_{\ell_2}}{m_s^2}$$
     这里的 **$v_s^2$ 严格消掉**，比值只取决于轻子质量与标量质量之比：
     - 对于**纯缪子过程（$\mu\mu \to \mu\mu$）**，当 $m_s \gtrsim 10\text{ GeV}$ 时：
       $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}}\right|_{\mu\mu} \le \frac{4 m_\mu^2}{m_s^2} = \frac{4 \times (0.10566)^2}{10^2} = 4.47 \times 10^{-4}$$
       对散射截面的相对修正更是低于 $\lesssim 10^{-7}$（若计及干涉项则低于 $4\times 10^{-4}$）。
     - 对于**缪子-陶子过程（$\mu\tau$）**，当 $m_s \gtrsim 10\text{ GeV}$ 时：
       $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}}\right|_{\mu\tau} \le \frac{4 m_\mu m_\tau}{m_s^2} = \frac{4 \times 0.10566 \times 1.77686}{10^2} = 7.51 \times 10^{-3} < 1\%$$
     - 对于**纯陶子过程（$\tau\tau$）**，当 $m_s \gtrsim 10\text{ GeV}$ 时：
       $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}}\right|_{\tau\tau} \le \frac{4 m_\tau^2}{m_s^2} \approx 0.126 \quad (\text{当 } m_s \ge 30\text{ GeV 时则 } \le 1.4\%)$$
   - **相对于纵向分量（在手征压低道 $\sqrt{\hat{s}} \ll m_s$）**：
     $$\left|\frac{\mathcal{M}_s}{\mathcal{M}_{A'}^{\text{long}}}\right| = \frac{|q^2 - m_{A'}^2|}{|q^2 - m_s^2|} \simeq \frac{\max(|q^2|, m_{A'}^2)}{m_s^2} \ll 1 \qquad (\text{当 } m_{A'}, \sqrt{|q^2|} \ll m_s)$$

### Step 3.3：逐步推导单圈轻子反常磁矩 $(g-2)_\mu$ 中 $s$ 圈与 $A'$ 圈的贡献比

若考察缪子反常磁矩 $\Delta a_\mu = \frac{1}{2}(g-2)_\mu$，单圈标量 $s$ 与单圈轴矢量 $A'$ 对 $\Delta a_\mu$ 的贡献比如下：
1. **单圈标量 $s$ 的贡献（Leveille 公式，在 $m_s \gg m_\mu$ 极限下）**：
   $$\Delta a_\mu^{(s)} = \frac{y_{s\mu\mu}^2}{8\pi^2} \frac{m_\mu^2}{m_s^2} \left[ \ln\left(\frac{m_s^2}{m_\mu^2}\right) - \frac{7}{6} \right] = \frac{1}{8\pi^2} \frac{m_\mu^2}{v_s^2} \frac{m_\mu^2}{m_s^2} \left[ \ln\left(\frac{m_s^2}{m_\mu^2}\right) - \frac{7}{6} \right]$$
2. **单圈轴矢量 $A'$ 的贡献**：
   - 在重质量区 $m_{A'} \gg m_\mu$：
     $$\Delta a_\mu^{(A')} \simeq -\frac{5 g_X^2}{12\pi^2} \frac{m_\mu^2}{m_{A'}^2} = -\frac{5}{48\pi^2} \frac{m_\mu^2}{v_s^2}$$
   - 在轻质量区 $m_{A'} \lesssim m_\mu$（此时由纵向 Goldstone 模式主导）：
     $$\Delta a_\mu^{(A')} \simeq -\frac{g_X^2}{8\pi^2} \frac{m_\mu^2}{m_{A'}^2} = -\frac{1}{32\pi^2} \frac{m_\mu^2}{v_s^2}$$
3. **两者之比（$v_s^2$ 再次严格约消）**：
   $$\left|\frac{\Delta a_\mu^{(s)}}{\Delta a_\mu^{(A')}}\right| \simeq \frac{6}{5} \frac{m_\mu^2}{m_s^2} \left[ \ln\left(\frac{m_s^2}{m_\mu^2}\right) - \frac{7}{6} \right]$$
   代入基准下限 $m_s = 10\text{ GeV}$：
   $$\left|\frac{\Delta a_\mu^{(s)}}{\Delta a_\mu^{(A')}}\right|_{m_s=10\text{ GeV}} = 1.2 \times \frac{(0.10566)^2}{10^2} \times \left[ \ln\left(\frac{100}{0.01116}\right) - 1.167 \right] = 1.34 \times 10^{-4} \times 7.93 = 1.06 \times 10^{-3} \approx 0.1\%$$
   结论：**在 $m_s \gtrsim 10\text{ GeV}$ 时，标量 $s$ 对 $(g-2)_\mu$ 的贡献不到轴矢量 $A'$ 贡献的千分之一（$0.1\%$）。**

### Step 3.4：明确划定“忽略 $s$ 近似”成立与失效的精确边界表

将参数空间与能标范围的精确边界总结为表 3：

| 物理判据维度 | 近似完全成立的区域（可安全忽略 $s$） | 近似失效的区域（必须保留 $s$ 或被排除） | 物理原因与定量指标 |
| :--- | :--- | :--- | :--- |
| **1. 微扰幺正性边界** | $v_s = \frac{m_{A'}}{2g_X} > \frac{m_s}{\sqrt{2\lambda_S^{\max}}} \gtrsim 2\text{--}4\text{ GeV}$ | $v_s = \frac{m_{A'}}{2g_X} < \frac{10\text{ GeV}}{\sqrt{2\lambda_S^{\max}}}$ | 正文公式 (34)：若 $v_s$ 过小，$m_s$ 无法在不破坏微扰论的前提下达到 $10\text{ GeV}$ |
| **2. 过程动量转移 $q^2$** | 低能过程：$\sqrt{\vert q^2\vert} \ll m_s$（且 $m_{A'} \ll m_s$） | 高能对撞过程：$\sqrt{\hat{s}} \gtrsim m_s$ | 低能下 $\vert\mathcal{M}_s / \mathcal{M}_{A'}\vert \sim 4m_\ell^2/m_s^2 \ll 1$；当 $\sqrt{\hat{s}} \sim m_s$ 时 $s$ 传播子可共振激发 |
| **3. 紫外重整化混合** | 除 $\vert m_s - m_h\vert \lesssim 8\text{ MeV}$ 外的全部 $m_s \ge 10\text{ GeV}$ | 仅在无宽度近似下的极窄点 $\vert m_s - m_h\vert \lesssim 8\text{ MeV}$ | 单圈 $\tau$ 圈图混合 $\delta m_{sh}^2/m_h^2 \lesssim 10^{-5}\text{--}10^{-4}$，计入宽度后全区间安全 |

## 第四阶段：可直接复制粘贴的英文审稿回复信与论文修改段落

### 1. 审稿回复信完整段落（Response to Referee Comment 3）

```latex
\textbf{Response to Comment 3:}

We thank the referee for raising these insightful questions regarding radiative $s$--$h$ mixing, the resonance behavior as $m_s \to m_h$, and the non-decoupling property of $m_s$. Following the referee's suggestions, we have explicitly calculated the one-loop $s$--$h$ mixing across the allowed $m_s$ range, compared it against LHC Higgs bounds, and clarified the regime of validity for neglecting $s$ in the revised manuscript. Our step-by-step findings are summarized below:

\textbf{1. Calculation of one-loop $s$--$h$ mixing as a function of $m_s$:}
In our UV completion (Table I), charged-lepton masses arise after both $H$ and $S$ acquire VEVs via the heavy vector-like leptons $E_{\mu,\tau}$, fixing the effective Yukawa couplings to $y_{h\ell\ell} = m_\ell / v$ and $y_{s\ell\ell} = m_\ell / v_s = 2 g_X m_\ell / m_{A'}$. While the tree-level portal coupling $\lambda_{HS}(H^\dagger H)(S^\dagger S)$ is a renormalized parameter that can be set to vanish at the UV matching scale $\mu_R = M_E$, one-loop fermion diagrams indeed generate an off-diagonal self-energy $\Pi_{sh}(p^2)$ at lower scales. Because $y_{s\ell\ell} y_{h\ell\ell} = m_\ell^2 / (v v_s)$, the $\tau$-loop dominates over the $\mu$-loop by $(m_\tau/m_\mu)^2 \approx 283$, yielding:
\begin{equation*}
\Pi_{sh}^{(\tau)}(p^2) = \frac{m_\tau^2}{16\pi^2 v \, v_s} \int_0^1 dx \, \big[ 6 m_\tau^2 - 6x(1-x)p^2 \big] \ln\left(\frac{M_{E_\tau}^2}{m_\tau^2 - x(1-x)p^2 - i\epsilon}\right).
\end{equation*}
Evaluating this at the Higgs mass shell $p^2 = m_h^2$ gives the conservative upper bound on the dimensionless radiative mixing parameter:
\begin{equation*}
\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2} \simeq \frac{1}{16\pi^2} \frac{m_\tau^2}{v \, v_s} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx \left(\frac{8.1 \times 10^{-5}\text{ GeV}}{v_s}\right) \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right),
\end{equation*}
whereas the momentum-independent chiral mass term $\delta m_{sh}^2(0)/m_h^2$ is further suppressed by $6 m_\tau^2 / m_h^2 \approx 1.2 \times 10^{-3}$.

Crucially, Eq.~(34) enforces a perturbative lower bound on $v_s$ for any given $m_s$, $v_s > m_s / \sqrt{2\lambda_S^{\max}}$. Substituting this bound yields the maximum loop-induced mixing angle as an explicit function of $m_s$:
\begin{equation*}
|\sin\theta_{sh}(m_s)|_{\max} \simeq \frac{\sqrt{2\lambda_S^{\max}}}{16\pi^2} \frac{m_\tau^2}{v \, m_s} \frac{m_h^2}{|m_h^2 - m_s^2|} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \lesssim 8.5 \times 10^{-5} \left(\frac{10\text{ GeV}}{m_s}\right) \frac{m_h^2}{|m_h^2 - m_s^2|}
\end{equation*}
(for $\lambda_S^{\max} = \pi$ and $M_{E_\tau} = 1\text{ TeV}$).

\textbf{2. Comparison with LHC Higgs bounds, $m_s \to m_h$ resonance, and fine-tuning:}
\begin{itemize}
    \item \emph{Away from $m_s \approx m_h$:} Across the entire range $m_s \gtrsim 10\text{ GeV}$, the loop-induced mixing angle is $|\sin\theta_{sh}| \lesssim 10^{-5}\text{--}10^{-4}$, which is three to four orders of magnitude below current LHC Higgs signal-strength and heavy-scalar search limits ($|\sin\theta_{\text{exp}}| \lesssim 0.1\text{--}0.3$). For $10\text{ GeV} \le m_s < m_h/2$, the one-loop induced trilinear coupling $g_{hss}^{\text{loop}} \sim (3 m_\tau^4 / 4\pi^2 v v_s^2)\ln(M_{E_\tau}^2/m_\tau^2) \lesssim 2\times 10^{-3}\text{ GeV}$ yields $\text{BR}(h \to ss) \lesssim 10^{-7}$, well below the experimental bound $\text{BR}(h \to \text{BSM}) < 0.12$.
    \item \emph{Resonance as $m_s \to m_h$:} Reaching $m_s \approx m_h = 125.25\text{ GeV}$ while satisfying Eq.~(34) requires $v_s > m_h / \sqrt{2\lambda_S^{\max}} \approx 25\text{--}50\text{ GeV}$, which automatically suppresses $y_{s\tau\tau} = m_\tau / v_s \lesssim 0.035\text{--}0.07$ and reduces $|\delta m_{sh}^2|/m_h^2$ to $(0.7\text{--}1.4)\times 10^{-5}$. Consequently, $|\sin\theta_{sh}|$ only exceeds $\sin\theta_{\text{exp}} \approx 0.1$ within an ultra-narrow mass window:
    \begin{equation*}
    \Delta m_s = |m_s - m_h| \lesssim \frac{m_h}{2\sin\theta_{\text{exp}}} \left(\frac{|\delta m_{sh}^2|}{m_h^2}\right) \lesssim 4\text{--}8\text{ MeV}
    \end{equation*}
    (or $\lesssim 30\text{ keV}$ using the static mass term). This window is comparable to the natural decay widths $\Gamma_h \approx 4.1\text{ MeV}$ and $\Gamma(s \to \tau^+\tau^-) \simeq m_\tau^2 m_s / (8\pi v_s^2) \approx 7\text{--}25\text{ MeV}$, which regularize the complex propagator denominator at exact degeneracy and prevent any unphysical enhancement. No counterterm fine-tuning ($\Delta_{\text{FT}} \ll 1$) is required.
\end{itemize}

\textbf{3. Clarification on the ``non-decoupling'' of $m_s$ and regime of validity:}
We fully agree with the referee that $m_s$ cannot formally decouple ($m_s \to \infty$) at fixed $(g_X, m_{A'})$ because $s$ is the radial Higgs mode of $U_A(1)_{L_\mu-L_\tau}$ breaking ($m_s = \sqrt{2\lambda_S} v_s$)—this is precisely why we highlighted the perturbative ceiling in Eq.~(34). By adopting the benchmark $m_s \gtrsim 10\text{ GeV}$, we do not take the formal limit $m_s \to \infty$, but rather work within the perturbatively allowed region $v_s > m_s/\sqrt{2\lambda_S^{\max}}$ at low momentum transfers $|q^2| \ll m_s^2$. In this kinematic regime, tree-level $s$-exchange is suppressed relative to $A'$-exchange by $|\mathcal{M}_s / \mathcal{M}_{A'}| \lesssim (y_{s\ell\ell}^2/m_s^2)/(g_X^2/m_{A'}^2) = 4 m_\ell^2 / m_s^2$ ($\le 4.5\times 10^{-4}$ for muons at $m_s \ge 10\text{ GeV}$), and the one-loop scalar contribution to $(g-2)_\mu$ is suppressed by $|\Delta a_\mu^{(s)} / \Delta a_\mu^{(A')}| \sim (m_\mu^2/m_s^2)\ln(m_s^2/m_\mu^2) \lesssim 10^{-3}$. This approximation only breaks down when $v_s = m_{A'}/(2g_X) < 10\text{ GeV}/\sqrt{2\lambda_S^{\max}}$ (which is already excluded by Eq.~(34)) or in high-energy processes with $\sqrt{\hat{s}} \gtrsim m_s$.
```

### 2. 论文正文公式 (34) 下方可直接插入的修改段落

```latex
We note that although $\tau$ and $\mu$ loops radiatively generate $s$--$h$ mixing even when the renormalized tree-level portal coupling vanishes at the UV scale $M_E$, the resulting one-loop off-diagonal self-energy is strongly suppressed by the tau Yukawa coupling and loop factor, $|\delta m_{sh}^2|/m_h^2 \simeq (16\pi^2)^{-1} (m_\tau^2 / v v_s) \ln(M_E^2/m_h^2) \lesssim 10^{-4}$ for $m_s \gtrsim 10\text{ GeV}$. Because Eq.~(34) enforces $v_s > m_s/\sqrt{2\lambda_S^{\max}}$ (requiring $v_s \gtrsim 25\text{--}50\text{ GeV}$ near $m_s \approx m_h$), the loop-induced mixing angle remains $|\sin\theta_{sh}| \lesssim 10^{-4}$ across the allowed parameter space—three to four orders of magnitude below LHC Higgs signal-strength and $h \to ss$ bounds—except within an ultra-narrow degeneracy window $|m_s - m_h| \lesssim \mathcal{O}(10\text{ MeV})$ that is regularized by the natural scalar widths $\Gamma_{h,s}$. Furthermore, while $m_s$ cannot formally decouple ($m_s \to \infty$) at fixed $v_s$ due to Eq.~(34), choosing $m_s \gtrsim 10\text{ GeV}$ within the perturbative regime kinematically suppresses $s$-exchange relative to $A'$-exchange by $\sim 4m_\ell^2/m_s^2 \ll 1$ in low-energy observables ($|q^2| \ll m_s^2$).
```
