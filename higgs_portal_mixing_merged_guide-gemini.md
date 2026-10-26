# $U_A(1)_{L_\mu-L_\tau}$ 模型中单圈 $s$–$h$ 混合：条件性计算与待核查事项

> **当前证据状态（2026-10-26；本说明优先于下文旧版强结论）：**
> 本文保存了轻子诱导 $s$--$h$ 二点函数的条件性 EFT 软圈计算、树级标量势关系，以及统一工作文档 v66 第 251.6–251.9 节已有的零动量重费米子 portal 势阈值。它们仍未被统一成完整的物理 $h$--$s$ 极点预测。关系 $y_{s\ell\ell}=m_\ell/v_s=2g_Xm_\ell/m_{A'}$ 与小混合近似下 $m_s^2\simeq2\lambda_Sv_s^2$ 可在其假设内使用；软圈数值只核验该 EFT 软贡献，不等于完整 UV 预测。
>
> **以下结论尚未得到充分证明，不可作为论文或正式回复中的既定结论：** 旧 $6\Delta$ 核已被撤回为同一 EFT 软圈的结果；完整 UV 硬阈值与软圈、接触项、有限场归一化的同方案匹配仍未闭环。严格近简并区的复数传播子极点、总宽度与干涉、完整 $h\to ss$ 率及模型专属 LHC 重铸也未完成。仅凭非零衰变宽度不能证明简并区必然安全，也不能据此断言“全参数空间均低于实验限制”“无需微调”或“不需要更新参数图”。详见 [单圈混合独立复核报告](单圈混合推导独立复核报告-协调更新版-20261019.md)。
## 导论：审稿人质疑的三条核心逻辑链拆解

审稿人在第 3 条意见中针对正文公式 (34) 上方的假设（“选取标量退耦基准 $m_s \gtrsim 10\text{ GeV}$ 并假设希格斯门户混合可以忽略”）提出了三个层层递进的场论与唯象学问题，要求作者逐一回应：

1. **圈图辐射产生混合的不可避免性（要求一：计算单圈混合大小）**：即使在树图拉氏量中人为将希格斯门户耦合 $\lambda_{HS}|H|^2|S|^2$ 设为零，由于标量 $S$ 与标准模型希格斯 $h$ 均与 $\mu, \tau$ 耦合，通过 $\mu, \tau$（及紫外区的矢量类重轻子 $E_{\mu,\tau}$）的单圈费曼图必然在辐射修正水平生成 $s$–$h$ 质量混合项 $\delta m_{sh}^2$。需要写出该混合随 $m_s$ 变化的解析函数与定量结果。
2. **简并共振放大与 LHC 希格斯实验限制（要求二：对比实验限制、共振区与微调分析）**：双标量系统的混合角满足 $\tan(2\theta_{sh}) = \frac{2\delta m_{sh}^2}{m_h^2 - m_s^2}$。审稿人担心当 $m_s \to m_h \approx 125\text{ GeV}$ 时，分母趋于零导致混合角发生共振增强，进而使紫外完备理论受到现有 LHC 希格斯精确测量的强烈限制。需要对比实验上限、给出共振区宽度及微调程度。
3. **低能有效理论中 $m_s$ 的“非退耦（Non-decoupling）”疑问（要求三：澄清非退耦概念与划定适用范围）**：审稿人在双括号中质疑，由于 $m_s$ 在形式上不能退耦（cannot formally decouple），在低能有效理论中忽略标量 $s$ 的传播子效应是否合理，需要证明运动学压低机制并明确划定该近似的适用边界。

下文保留原 LaTeX 备忘录中的计算路径，并把已核验的代数、条件性积分与未完成的 UV/现象学检查分开标注；步骤存在不代表相应研究已经完成。

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

### Step 1.5：UV 阈值匹配假设与系数差异（尚未闭合）

现在回答审稿人最关心的场论自洽性问题：**既然上式含有紫外发散 $\frac{1}{\tilde{\epsilon}}$，作者假设“Higgs-portal 混合可忽略”在重整化场论中的严格定义是什么？**

1. **紫外完整理论（含重费米子 $E_\ell$，质量 $M_{E_\ell}$）中的截断机制**：
   在完整标量势 $V(H,S) \supset \lambda_{HS} (H^\dagger H)(S^* S)$ 中，树图非对角质量平方元为 $\left(\mathcal{M}_{\text{tree}}^2\right)_{sh} = \lambda_{HS} v v_s$。
   在能标 $\mu > M_{E_\ell}$ 的紫外完备理论中，轻子与重矢量类轻子通过 Step 0.1 的拉氏量耦合：$H$ 连接 $\bar{L}_\ell E_{\ell R}$（耦合 $y_{H\ell}$），$S$ 连接 $\bar{E}_{\ell L}\ell_R$（耦合 $y_{S\ell}$）。单圈图连接外腿 $s$ 与 $h$ 时，圈内上方传播子是重费米子 $E_\ell$（质量 $M_{E_\ell}$），下方传播子是轻子 $\ell$（质量 $m_\ell$）。
   根据可重整化量子场论，裸参数 $\lambda_{HS}^0 = \lambda_{HS}(\mu_R) + \delta\lambda_{HS}$ 中的反项吸收紫外发散；但这本身不能确定有限阈值项或对数核的系数。把匹配能标选为 $\mu_R=M_{E_\ell}$ 是一个可用的计算约定，仍需用完整 UV 振幅减去 EFT 软区贡献来证明相应有限项。

2. **边界条件与 EFT 软圈函数（不是完整 UV 匹配）**：

   为使“portal 混合可忽略”成为可检验假设，可以把 \(\lambda_{HS}(\mu_R=M_{E_\ell})=0\) 作为一个明确的 benchmark 边界条件；这不是由“混合可忽略”这句话自动推出的结论。还必须给出重整化方案、完整 UV 硬匹配和相同方案下的局域项。

   以第 262 节的 \(i\Pi\) 约定（1PI 插入为 \(i\Pi\)，逆核为 \(p^2-m_0^2+\Pi\)）为例，令 \(q_0=1/(16\pi^2)\)、\(\ell_\ell=\ln(m_\ell^2/\mu_R^2)\)，并令 \(\bar B_\ell(t)=B_0(t;m_\ell^2,m_\ell^2)-\Delta_{\rm UV}\)。单轻子圈的有限 EFT 软贡献（泡图加 \(hs\bar\ell\ell\) 接触图）为
   \[
   \Pi_{hs,\ell}^{\mathrm{soft,fin}}(t)=
   -2q_0\frac{m_\ell^2}{v v_s}
   \left[4m_\ell^2(1-\ell_\ell)+(4m_\ell^2-t)\bar B_\ell(t)\right].
   \]
   若沿用本文件 Step 1.1 的 \(-i\Pi\) 约定，整体符号需相应转换；在把两份文档的 1PI 约定统一前，不得直接混用它们的有符号自能。

   固定外动量并取严格 \(M_{E_\ell}^{-2}\) 阶时，软圈的非解析动量项正比于
   \[
   \Pi_{hs,\ell}^{[M^{-2}],\mathrm{fin}}(t)
   =2q_0\frac{m_\ell^2}{v v_s}\,t
   \left[2-\ln\frac{-t-i0}{\mu_R^2}\right]
   \]
   （按上面第 262 节的符号约定）。这与 Step 1.4 的 \(12\Delta\) Feynman 参数对数核一致：积分后 \(p^2\) 项的系数大小为 \(2\)，而不是 \(1\)。

> **更正与停机条件（2026-10-26）：** 旧版 \(\int dx\,[6m_\ell^2-6x(1-x)p^2]\ln(M_E^2/\Delta)\) 表达式的 \(p^2\)-依赖非解析对数系数比上述 EFT 软圈少一半，并且没有显式包含接触图。它不能作为相同耦合约定下的完整 UV 结果。硬匹配的局域项在轻阈值附近对外动量解析，不能任意改变轻子对产生的非解析 \(\Delta\ln\Delta\) 系数；若仍得到 \(6\Delta\)，必须追踪不同耦合归一化、额外轻态贡献或推导错误。当前已确认的是软圈系数结构，不是完整 UV portal 混合：硬匹配、portal 反项/RGE、总宽度和物理极点仍未闭环。

### 已有的零动量 UV portal 势阈值：必须与软圈分开记账

统一工作文档 v66 的第 251.6–251.9 节已经给出一项**部分 UV 硬阈值结果**，所以不应再把“所有 portal 硬阈值均未计算”作为当前状态。需要区分两种方案：

1. **规范化场下的参数匹配方案**（v66 第 251.7 节）：若势写为 \(V\supset\lambda_PXY\)，\(X=H^\dagger H\)、\(Y=S^\dagger S\)，并令 \(u_\ell=|y_\ell|^2\)、\(w_\ell=|\lambda_\ell|^2\)，重费米子来源的有限参数阈值包含
   \[
   \delta\lambda_P=-2q_0\sum_\ell u_\ell w_\ell-\lambda_P(z_H+z_S),
   \qquad q_0=\frac1{16\pi^2}.
   \]
   第二项是有限场归一化对既有树级 portal 的转换，不能再当作一张新圈图。若 \(\lambda_P=0\) 是在 UV 参数中施加的边界，第一项仍会产生 EFT 阈值；若要令匹配后的 EFT portal 为零，则需在 UV 参数中选择相应的抵消边界。

2. **固定 VEV 的 tadpole 方案**（v66 第 251.9 节）：直接势曲率为
   \[
   \delta\mathcal M_{hs,V}^2
   =q_0vv_s\sum_\ell u_\ell w_\ell
   \left[-2+\frac{u_\ell v^2+w_\ell v_s^2}{M_{E_\ell}^2}\right].
   \]
   这里的 \(-2q_0u_\ell w_\ell\) 是可重整化 portal 势阈值；\(1/M_{E_\ell}^2\) 项来自六标量势。该式是指定 tadpole 方案下的零动量势曲率，不是完整的动量依赖 \(\Pi_{hs}(p^2)\)。它与上面的规范化参数阈值属于不同记账方案，不能不经转换直接相加。

用领先质量关系 \(m_\ell\simeq |y_\ell\lambda_\ell|vv_s/(2M_{E_\ell})\)，可把第一项写成
\[
\delta\lambda_P^{\rm hard}\simeq
-8q_0\sum_\ell\frac{M_{E_\ell}^2m_\ell^2}{v^2v_s^2},
\qquad
\delta\mathcal M_{hs,V}^{2,\rm leading}\simeq
-8q_0\sum_\ell\frac{M_{E_\ell}^2m_\ell^2}{vv_s}.
\]
这显示硬 portal 阈值与轻子质量、重费米子质量和 \(v_s\) 相关，不能由低能软泡图的单一对数替代。

**数值 benchmark 与混合角表的唯一阅读位置：** 现有[研究者完整版](审稿意见-gpt/研究者阅读版/DW13678_论文修订与理论核查手册_研究者完整版.md) 的 §2.5.3.1 已保存 \(M_{E_\tau}=17.77\,\mathrm{TeV}\)、\(v_s=1000\,\mathrm{GeV}\) 候选点的硬阈值、树级质量矩阵对角化和近简并诊断。为避免维护第二套混合角表，本文件不重复其数值表；应以研究者完整版中的条件性诊断为阅读入口，并保留以下限制：

- 该结果采用 \(\lambda_{HS}^{\rm UV}=0\) 的特定边界与零动量势曲率，尚未包含完整动量依赖自能、复数极点及实验重铸。
- 用当前展示的圆整物理常数独立代入领先质量关系，得到 \(\delta\lambda_P^{\rm hard}\simeq-8.33\times10^{-4}\)、\(\delta\mathcal M_{hs,V}^{2}\simeq-205.1\,\mathrm{GeV}^2\)；研究者完整版记录为 \(-8.36\times10^{-4}\)、\(-205.8\,\mathrm{GeV}^2\)。约 \(0.3\%\) 的差异应在最终冻结前用原始未舍入耦合、质量和方案统一核对，不能只归因于舍入而不查输入。
- 这些阈值与下一小节的 EFT 软圈函数属于不同动量/匹配定义；在同一重整化方案中完成边界、有限场归一化、接触项和重叠扣除之前，不能直接相加，也不能由任一单独项宣布参数区被排除或安全。


### 条件性数值交叉核对：EFT 软圈（不是完整 UV benchmark）

为检查第 262 节的有限软圈函数，取一个仅用于代数测试的示例点：
\[
m_h=125.25\,\mathrm{GeV},\quad m_\tau=1.77686\,\mathrm{GeV},\quad
m_\mu=0.105658\,\mathrm{GeV},\quad v=246.22\,\mathrm{GeV},
\]
\[
v_s=50\,\mathrm{GeV},\qquad \mu_R=M_E=1\,\mathrm{TeV}.
\]
这里的 \(v_s\) 只是示例输入，不表示已通过完整 UV 参数扫描的 benchmark。用
\[
\bar B_\ell(t)=2-\ln\frac{m_\ell^2}{\mu_R^2}
-\beta_\ell\ln\frac{1+\beta_\ell}{1-\beta_\ell}
+i\pi\beta_\ell,\qquad
\beta_\ell=\sqrt{1-\frac{4m_\ell^2}{t}}
\]
计算 \(t=m_h^2\)，并代入上面的 EFT 软圈有限函数，得到（第 262 节的 \(i\Pi\) 符号约定）
\[
\bar B_\tau(m_h^2)=6.158716+3.140328\,i,
\]
\[
\Pi_{hs,\tau}^{\mathrm{soft,fin}}(m_h^2)
=(0.312998+0.159884\,i)\,\mathrm{GeV}^2,\qquad
\frac{|\Pi_{hs,\tau}^{\mathrm{soft,fin}}|}{m_h^2}=2.2404\times10^{-5}.
\]
缪子项为
\[
\Pi_{hs,\mu}^{\mathrm{soft,fin}}(m_h^2)
=(1.1089\times10^{-3}+5.6602\times10^{-4}i)\,\mathrm{GeV}^2,\qquad
\frac{|\Pi_{hs,\mu}^{\mathrm{soft,fin}}|}{m_h^2}=7.9363\times10^{-8}.
\]
\(\bar B_\tau\) 还与直接高精度 Feynman 参数积分核对一致（数值差异约 \(10^{-23}\)）。同一示例点的三种计算对照为：

| 计算口径 | \(|\Pi_{hs,\tau}|\) | \(|\Pi_{hs,\tau}|/m_h^2\) | 状态 |
|---|---:|---:|---|
| 旧式对数积分，系数 \(6\Delta\) | \(0.16835\,\mathrm{GeV}^2\) | \(1.0731\times10^{-5}\) | 条件性旧方案 A；不作为最终结果 |
| 对数积分，系数 \(12\Delta\) | \(0.33670\,\mathrm{GeV}^2\) | \(2.1463\times10^{-5}\) | 软圈对数项；不含完整有限项 |
| 有限 \(B_0\) 软圈函数（泡图加接触项） | \(0.35147\,\mathrm{GeV}^2\) | \(2.2404\times10^{-5}\) | 本节核对的 EFT 软贡献；不含 UV 硬匹配 |

完整有限软圈结果比 \(12\Delta\) 的对数项大约 4.4%，来自有限常数与接触项的处理；它仍不是完整 UV 预测。作为另一项粗略对照，旧 Step 1.7 的单实对数估计给出 \(q_0m_\tau^2/(vv_s)\ln(M_E^2/m_h^2)=6.7477\times10^{-6}\)，约比有限软圈模值小 3.3 倍；该近似没有保留完整有限 \(B_0\) 常数与虚部。

**解释边界：** 这些数字只验证所列 EFT 软圈函数和数值积分，不包含 UV 硬匹配、完整 portal 局域项或同一参数点的完整复数极点。比值 \(|\Pi|/m_h^2\) 不是物理混合角，也不能直接与实验的 \(\sin\theta\) 上限比较；在 \(m_s\simeq m_h\) 时必须计算完整传播子与可观测率。

> **历史结果警告：** 下列 Step 1.6–1.8、旧版表 2 与由其得到的“反相关保护”结论基于已撤回的 \(6\Delta\) 核，且未包含统一约定下的完整软圈接触项与 UV 硬匹配。它们只保留作审计追溯，不是当前数值预测，不得作为论文排除/允许结论；必须在软圈、硬匹配和 portal 边界闭环后重算。

### Step 1.6：旧版静态/在壳估算（已撤回；仅留档）

利用积分公式 $\int_0^1 dx \, 1 = 1$ 和 $\int_0^1 dx \, 6 x(1-x) = 6 \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = 1$，并代入 Step 0.4 的汤川耦合乘积：
$$y_{s\ell\ell}\, y_{h\ell\ell} = \left(\frac{m_\ell}{v_s}\right) \left(\frac{m_\ell}{v}\right) = \frac{m_\ell^2}{v \, v_s}$$
我们将单圈诱导的 $s$–$h$ 混合拆分为两个物理层次的贡献：

1. **动量无关的静态手征质量混合项（$p^2 = 0$）**：
   $$\delta m_{sh}^2\big|_{p^2=0} = \sum_{\ell=\mu,\tau} \frac{6 \, y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} m_\ell^2 \ln\left(\frac{M_{E_\ell}^2}{m_\ell^2}\right) = \sum_{\ell=\mu,\tau} \frac{3}{8\pi^2} \frac{m_\ell^4}{v \, v_s} \ln\left(\frac{M_{E_\ell}^2}{m_\ell^2}\right)$$
   注意这里出现了 **$m_\ell^4$ 的四次方手征压低**。

2. **在壳动量项 / 波函数混合诱导项（$p^2 = m_h^2$ 或 $m_s^2$）**：
   当我们在希格斯质量壳 $p^2 = m_h^2 \gg m_\tau^2$ 处评估自能（这是产生最大可能混合的保守上限估计）时，被积函数中的 $-6x(1-x)p^2$ 积分给出 $-m_h^2$：
   $$\left|\delta m_{sh}^2(p^2 = m_h^2)\right| \simeq \sum_{\ell=\mu,\tau} \frac{y_{s\ell\ell}\, y_{h\ell\ell}}{16\pi^2} m_h^2 \ln\left(\frac{M_{E_\ell}^2}{m_h^2}\right) = \sum_{\ell=\mu,\tau} \frac{1}{16\pi^2} \frac{m_\ell^2}{v \, v_s} m_h^2 \ln\left(\frac{M_{E_\ell}^2}{m_h^2}\right)$$

### Step 1.7：旧版数值估算（已撤回；仅留档）

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

### Step 1.8：旧版混合角函数与数值表（已撤回；须重算）

根据正文公式 (34) 的微扰论条件：
$$m_s < \sqrt{2\lambda_S^{\max}}\, v_s \implies v_s > v_s^{\min}(m_s) \equiv \frac{m_s}{\sqrt{2\lambda_S^{\max}}}$$
把 $v_s > \frac{m_s}{\sqrt{2\lambda_S^{\max}}}$ 代入 Step 1.7 的公式，立即得到**在任意给定标量质量 $m_s$ 下，微扰论所允许的最大单圈诱导混合元**：
$$\left(\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2}\right)_{\max} = \frac{\sqrt{2\lambda_S^{\max}}}{16\pi^2} \frac{m_\tau^2}{v \, m_s} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right) \approx 8.46 \times 10^{-5} \left(\frac{10\text{ GeV}}{m_s}\right) \sqrt{\frac{\lambda_S^{\max}}{\pi}}$$

进而，双标量混合角 $\theta_{sh}$ 随 $m_s$ 变化的**显式解析上限函数**为：
$$\left|\sin\theta_{sh}(m_s)\right|_{\max} \simeq \left|\frac{\delta m_{sh}^2(m_h^2)}{m_h^2 - m_s^2}\right|_{\max} = \frac{\sqrt{2\lambda_S^{\max}}}{16\pi^2} \frac{m_\tau^2}{v \, m_s} \frac{m_h^2}{|m_h^2 - m_s^2|} \ln\left(\frac{M_{E_\tau}^2}{m_h^2}\right)$$

**旧版物理解释（未验证，不得作为结论）：**
观察上式中的因子 $\frac{1}{m_s |m_h^2 - m_s^2|}$：
- **在轻质量端（$m_s = 10\text{ GeV}$）**：虽然 $v_s$ 可以较小（$v_s^{\min} \approx 2.0\text{--}4.0\text{ GeV}$，$y_{s\tau\tau}$ 相对较大），但质量平方差 $|m_h^2 - m_s^2| \approx m_h^2$ 处于最大，因此混合角被大质量分母压低至 $|\sin\theta_{sh}| \lesssim 10^{-4}$；
- **在希格斯简并区（$m_s \to m_h = 125.25\text{ GeV}$）**：为了使 $m_s$ 能够达到 $125\text{ GeV}$ 而不破坏公式 (34) 的微扰论要求，**$v_s$ 必须同步成比例增大至 $25\text{--}50\text{ GeV}$ 以上**（取 $\lambda_S^{\max}=\pi$ 时 $v_s^{\min} \approx 49.97\text{ GeV}$；取 $\lambda_S^{\max}=4\pi$ 时 $v_s^{\min} \approx 24.98\text{ GeV}$），从而自动把汤川耦合压低至 $y_{s\tau\tau} = m_\tau/v_s \lesssim 0.035\text{--}0.071$，使圈图混合元在 $m_s \approx m_h$ 处反而进一步减小至 $(0.68\text{--}1.35)\times 10^{-5}$！

旧版表 2（仅作历史追溯；由已撤回的 $6\Delta$ 核导出，不能作为当前结果）曾尝试比较 $m_s \in [10,500]\text{ GeV}$ 的数值与 LHC 上限；取值为 $\lambda_S^{\max}=\pi$、$M_{E_\tau}=1\text{ TeV}$，但尚未使用统一软圈函数和 UV 硬匹配重新计算：

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
     在这一简化三角图估算下得到的数值很小，但它尚未包括完整 UV 匹配、所有允许的三标量顶点和一致的 portal 边界；因此不能据此宣布 $h\to ss$ 在全参数空间完全可忽略。该约束仍需按实际模型输入重新验收。

### Step 2.2：逐步求解简并共振区（$m_s \to m_h$）的排除窗口宽度 $\Delta m_s$

双标量精确对角化公式为：
$$\tan(2\theta_{sh}) = \frac{2 \delta m_{sh}^2}{m_h^2 - m_s^2}$$
当混合角达到实验灵敏度阈值 $\theta_{\text{exp}}$（取严苛标准 $\sin\theta_{\text{exp}} = 0.10 \implies \tan(2\theta_{\text{exp}}) \approx 2\sin\theta_{\text{exp}} = 0.20$）时，对应的标量质量 $m_s$ 与 $m_h$ 的距离 $\Delta m_s \equiv |m_s - m_h|$ 满足：
$$\left|m_h^2 - m_s^2\right| = (m_h + m_s)|m_h - m_s| \simeq 2 m_h \Delta m_s \le \frac{2 \left|\delta m_{sh}^2\right|}{\tan(2\theta_{\text{exp}})} \simeq \frac{\left|\delta m_{sh}^2\right|}{\sin\theta_{\text{exp}}}$$
两边同除以 $2m_h$，得到实质量矩阵与小混合近似下的形式窗口估算（不是经实验重铸后的排除窗口）：
$$\Delta m_s = \left|m_s - m_h\right| \le \frac{m_h}{2 \sin\theta_{\text{exp}}} \left(\frac{\left|\delta m_{sh}^2\right|}{m_h^2}\right)$$

在指定低能积分核与参数假设下，代入 $m_s = m_h = 125.25\text{ GeV}$ 的条件性数值：
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

### Step 2.3：有限宽度与近简并区（条件性估算；不能单独证明安全）

当 $m_s\simeq m_h$ 时，实数质量矩阵的小混合近似失效。完整验收应从复数逆传播子矩阵出发，例如
\[
D^{-1}(p^2)=
\begin{pmatrix}
p^2-m_{h,0}^2+\widehat\Pi_{hh}(p^2)&\widehat\Pi_{hs}(p^2)\\
\widehat\Pi_{sh}(p^2)&p^2-m_{s,0}^2+\widehat\Pi_{ss}(p^2)
\end{pmatrix},
\]
并在同一重整化方案中求复极点、包含树级 portal 项和相关反项，再计算实际产生与衰变率及干涉效应。

本节原有的常数宽度估算采用分母
\[
\sqrt{(m_h^2-m_s^2)^2+(m_h\Gamma_h-m_s\Gamma_s)^2}.
\]
它只是一种固定宽度的诊断性近似，不是一般的混合角公式。分母中的宽度差可能变小甚至在某些参数选择下抵消；“两个粒子各自有非零宽度”并不保证这个差非零，也不能单独证明混合受到实验上限约束。

例如，取本笔记使用的 $\Gamma_h\simeq4.1\,\mathrm{MeV}$ 以及由树级 $s\to\tau^+\tau^-$ 得到的示例宽度，只能在这些特定假设下估算 $|m_h\Gamma_h-m_s\Gamma_s|$。它不是完整 UV 模型的宽度预测，因为其他衰变道、portal 混合和总宽度尚未统一验收。因此，原笔记中由该分母推导的严格简并点混合角数值应视为条件性示例，而非全模型上限。

**关闭本项所需的实际工作：** 明确 $\lambda_{HS}$ 的边界和重整化方案，完成 UV 阈值匹配与反项，构造完整复数二点函数矩阵，求复极点并计算适用的信号率。完成前，$m_s\simeq m_h$ 区域应标记为“未评估”，不得写成已排除、已允许或自动安全。

### Step 2.4：定量计算抵消项微调程度（Counterterm Fine-Tuning Analysis）

> **状态限制：** 本节定义的 $\Delta_{\mathrm{FT}}=|\delta\lambda_{HS}^{\mathrm{loop}}/\lambda_{HS}^{\mathrm{exp}}|$ 只是特定近似和参数化下的比值，不自动等同于一般的 Barbieri--Giudice 灵敏度或模型无关的微调度量。只有在重整化方案、portal 边界、完整混合矩阵和所选可观测量明确后，才可将其用于物理结论。


审稿人提到：“如果存在强限制，需要说明多大程度的抵消项（counterterm）微调”。下面的比值只提供一个指定参数化下的诊断性比较；标准 Barbieri–Giudice 灵敏度需要对明确的可观测量和独立输入参数求导，不能由这个比值自动替代：
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
   - 该近似给出的非简并区数值只能作为指定边界条件下的诊断性比值；在完整 UV 阈值匹配和可观测量核验完成前，不得据此下结论说“完全不需要微调”。
   - 在近简并区，基于实质量矩阵的小角近似本身失效；没有完整复数极点与率的计算，不能从本节的简单比值给出可靠的微调结论。

### Step 2.5：参数空间图的处理原则（未完成近简并核查前不得关闭）

- 质量窗口 $|m_s-m_h|\lesssim\mathcal O(10\,\mathrm{MeV})$ 在宽质量轴图上可能很窄，但“图上看不清”不是物理上可以忽略的理由。
- 若当前图未包含完整 UV portal、复数极点和相关 Higgs 率的结果，应将近简并区域明确标记为“未评估”，或在图注中说明该区域尚未由本分析覆盖；不能写成“计入宽度后全区间安全”。
- 只有在同一组 UV 输入下完成完整传播子与可观测率计算后，才决定是否重画、单独放大或以有依据的范围限制处理该区域。
- 任何“整个参数空间低于 LHC 限制”的结论，都必须同时通过阈值匹配、portal 树级项、相关衰变道和模型专属实验适用性检查。

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

### Step 3.4：忽略 $s$ 近似的条件与失效边界（不是普适安全区）

将需要逐过程核验的条件与主要失效风险总结为表 3：

| 物理判据维度 | 可考虑近似的条件（仍需逐过程验收） | 尚未评估或近似可能失效的区域 | 物理原因与所需核验 |
| :--- | :--- | :--- | :--- |
| **1. 微扰幺正性边界** | $v_s = \frac{m_{A'}}{2g_X} > \frac{m_s}{\sqrt{2\lambda_S^{\max}}} \gtrsim 2\text{--}4\text{ GeV}$ | $v_s = \frac{m_{A'}}{2g_X} < \frac{10\text{ GeV}}{\sqrt{2\lambda_S^{\max}}}$ | 正文公式 (34)：若 $v_s$ 过小，$m_s$ 无法在不破坏微扰论的前提下达到 $10\text{ GeV}$ |
| **2. 过程动量转移 $q^2$** | 仅在指定过程的洛伦兹结构与输入假设已核对，且 $|q^2|\ll m_s^2$ 时可作低能展开 | 高能对撞过程：$\sqrt{\hat{s}}\gtrsim m_s$，或标量传播子可接近壳 | $4m_\ell^2/m_s^2$ 不能作为任意过程的普适振幅比；须对具体可观测量单独推导。 |
| **3. 紫外重整化混合** | 远离简并区且完整 UV 匹配与小混合条件已验证的指定可观测量 | $m_s\simeq m_h$ 及任何尚未完成阈值/实验核查的区域 | 低能积分给出条件性数量级；完整复数极点、总宽度、portal 项和实验率未完成前，不能判定全区间安全。 |

## 第四阶段：历史英文措辞材料（不得直接提交；须待研究闭环后重写）


> **不得直接提交本阶段现存英文段落。** 其中仍有 “we have explicitly calculated”“we find” 等完成时陈述，而完整 UV 匹配、近简并区和实验重铸尚未闭环。该段仅是内部措辞材料；只有实际计算、正文修改与证据验收全部完成后，才能据结果重新撰写正式回复信。


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


---

## 独立树级标量势核查（2026-10-26）

本节只核对给定可重整化势、规范场归一化和实 VEV 下的树级代数，不代表完整圈级极点、全局真空或实验扫描已完成。

取
\[
V=-\mu_H^2(H^\dagger H)+\lambda_H(H^\dagger H)^2
-\mu_S^2(S^\dagger S)+\lambda_S(S^\dagger S)^2
+\lambda_{HS}(H^\dagger H)(S^\dagger S),
\]
并令 \(H=(0,(v+h)/\sqrt2)^T\)、\(S=(v_s+s)/\sqrt2\)。驻点方程为
\[
\mu_H^2=\lambda_Hv^2+\frac12\lambda_{HS}v_s^2,\qquad
\mu_S^2=\lambda_Sv_s^2+\frac12\lambda_{HS}v^2.
\]
消去质量参数后，CP-even 树级质量平方矩阵是
\[
\mathcal M^2_{\rm tree}=
\begin{pmatrix}
2\lambda_Hv^2&\lambda_{HS}vv_s\\
\lambda_{HS}vv_s&2\lambda_Sv_s^2
\end{pmatrix},
\]
其本征值为
\[
m_{\pm}^2=\lambda_Hv^2+\lambda_Sv_s^2
\pm\sqrt{(\lambda_Hv^2-\lambda_Sv_s^2)^2+\lambda_{HS}^2v^2v_s^2}.
\]
因此 \(m_s^2\simeq2\lambda_Sv_s^2\) 只在 portal 混合足够小、且圈级质量修正尚未纳入的近似下成立。

令 \(x=H^\dagger H\ge0\)、\(y=S^\dagger S\ge0\)。四次项在大场方向有下界的常用条件为
\[
\lambda_H\ge0,\qquad \lambda_S\ge0,\qquad
\lambda_{HS}\ge-2\sqrt{\lambda_H\lambda_S},
\]
其中等号可能对应平坦方向，需进一步检查低阶项与真空结构。对于 \(v,v_s\ne0\) 的混合驻点，局部质量矩阵正定还要求对角项为正且
\[
\det\mathcal M^2_{\rm tree}
=v^2v_s^2(4\lambda_H\lambda_S-\lambda_{HS}^2)>0.
\]
这只检验该驻点的局部稳定性；要确定全局真空，还必须与 \(v=0\)、\(v_s=0\) 及其他允许驻点的势能比较。

当 \(\lambda_{HS}=0\) 时，树级非对角质量元消失，但这只是给定尺度上的参数边界条件，不是对辐射混合的禁止定理。完整 UV 阈值、portal 的重整化群演化、圈级极点及近简并可观测率仍需独立计算。

**公式边界复核：** 在小 portal 混合近似下，\(m_s^2=2\lambda_Sv_s^2\)。若取 \(\lambda_S^{\max}=4\pi\)，则 \(m_s^2\le8\pi v_s^2\)；\(4\pi v_s^2\) 对应的是 \(\lambda_S^{\max}=2\pi\)，两者不是同一边界。

