from pathlib import Path
import re, math
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'work/v57_corrected.md').read_text(encoding='utf-8')
def section(start,end,body):
 global s
 assert s.count(start)==1,start
 a=s.index(start);b=s.index(end,a+len(start));s=s[:a]+body.strip()+'\n\n'+s[b:]
def before(marker,text):
 global s
 assert s.count(marker)==1,marker
 s=s.replace(marker,text.strip()+'\n\n'+marker)

before('#### 第三步：从允许算符构造矩阵',r'''
**当前最小假设下的算符表。** $n,m$ 是非负整数。

| 质量条目 | $Q(L_i)+Q(L_j)$ | 最低标量插入 | 最低算符维数 | 结论 |
|---|---:|---|---:|---|
| $ee$ | 0 | 无 | 5 | 允许 |
| $e\mu$ | +1 | 任意 $S^n(S^\dagger)^m$ 均不能补偿 | — | 禁止 |
| $e\tau$ | −1 | 任意 $S^n(S^\dagger)^m$ 均不能补偿 | — | 禁止 |
| $\mu\mu$ | +2 | $S^\dagger$ | 6 | 允许高维项 |
| $\mu\tau$ | 0 | 无 | 5 | 允许 |
| $\tau\tau$ | −2 | $S$ | 6 | 允许高维项 |

“允许”不等于当前可重整拉氏量已经含有这些算符，也不保证系数非零。若以 $C_{ij}^{(5)}/\Lambda_\nu$ 定义 Weinberg 系数，在固定质量项归一化后，质量量级为 $C_{ij}^{(5)}v^2/(2\Lambda_\nu)$；额外一次 $S$ 插入多带 $v_S/(\sqrt2\Lambda_\nu)$。$\Lambda_\nu$ 是待定义的中微子机制尺度，不自动等于带电轻子 VLL 匹配尺度。
''')
before('#### 第四步：检查残余对称性和分块结构',r'''
在仍保持上述真空对称性的条件下，允许矩阵的最大结构为
\[
M_\ell=\begin{pmatrix}m_e&0&0\\0&*&*\\0&*&*\end{pmatrix},\qquad
M_\nu=\begin{pmatrix}m_{ee}&0&0\\0&m_{\mu\mu}&m_{\mu\tau}\\0&m_{\mu\tau}&m_{\tau\tau}\end{pmatrix}.
\]
星号表示可能允许而需由拉氏量计算的项，不保证非零。两种左手旋转均保持 $\{e\}\oplus\{\mu,\tau\}$ 分块，因而相对旋转仍分块。保留 VLL 时，完整带电流中还须插入弱双重态投影矩阵，轻态耦合可非幺正；但残余 $Z_2$ 仍禁止连接两块。非幺正修正不能生成被对称性禁止的混合。
''')
s=s.replace('如果当前破缺 VEV 保留一个残余离散对称性，使电子味与 $(\\mu,\\tau)$ 扇区处于不同块，则 $M_\\ell$ 与 $M_\\nu$ 的结构可能强制 PMNS 包含一个纯电子味本征态。',
 '当前破缺假设保留残余 $Z_2$，使电子味与 $(\\mu,\\tau)$ 扇区分块；在非简并三轻态近似下，PMNS 因而必含一个纯电子味本征态列。')

before('#### 第六步：如何向审稿人报告',r'''
#### 对角化与扩展拟合：实际应采用的方法

**先完成解析判定。** 对固定最小模型，逐项荷守恒与残余 $Z_2$ 已证明混合障碍，不必用一个注定无解的数值扫描“发现”它。任意质量重排只移动纯电子味列的位置；精确简并下某些角可任意旋转，却不能同时制造实测的两个独立非零质量平方差与电子味振荡。扩展改变荷或 VEV 后才重开拟合。

**带电轻子用双幺正分解。** 在固定约定 $\ell_L^{\rm gauge}=U_{\ell,L}\ell_L^{\rm mass}$ 下，求
\[
U_{\ell,L}^\dagger M_\ell U_{\ell,R}=D_\ell,\qquad D_\ell\ge0.
\]
可从 $M_\ell M_\ell^\dagger$ 求左手向量，但最终须以奇异值分解核验左右配对和非负质量。复矩阵不能直接用实对称矩阵的算法。

**Majorana 中微子用 Takagi 分解。** 对复对称 $M_\nu$，采用
\[
U_\nu^T M_\nu U_\nu=D_\nu,\qquad D_\nu=\operatorname{diag}(m_1,m_2,m_3)\ge0.
\]
不能把一般复本征值的绝对值与未经相位修正的本征矢直接拼成 PMNS。实现时用支持复对称矩阵的 Takagi 算法，或经相位与简并子空间处理的 SVD；显式检查 $U_\nu^\dagger U_\nu=\mathbf1$ 和分解残差。Dirac 质量则用双幺正分解，取左手旋转进入带电流。

**由矩阵得到观测量。** 在三轻态幺正近似中，先构造 $U=U_{\ell,L}^\dagger U_\nu$，按所选质量排序重排列，再提取
\[
s_{13}^2=|U_{e3}|^2,\quad
s_{12}^2=\frac{|U_{e2}|^2}{1-|U_{e3}|^2},\quad
s_{23}^2=\frac{|U_{\mu3}|^2}{1-|U_{e3}|^2},
\quad\Delta m_{ij}^2=m_i^2-m_j^2.
\]
CP 检验可先用 $J=\operatorname{Im}(U_{e1}U_{\mu2}U_{e2}^*U_{\mu1}^*)$；只从 $\sin\delta$ 反演不能确定象限，须另用相位不变量或固定重相位约定。上述角公式不能直接套在显著非幺正的有效带电流上。约定可核对 [PDG 中微子混合综述](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-neutrino-mixing.pdf)，不是本模型拟合结果。

**有了可行结构才拟合。** 锁定一个公开振荡似然版本、质量排序和参数定义，逐点由拉氏量参数生成矩阵和观测量。优先采用可取得的相关似然；若仅有一维区间，分项 $\chi^2$ 只作注明假设的近似，不能声称复现完整全局拟合。使用多个初值/采样策略，保存最佳点及附近稳定性，检查矩阵秩、非幺正性、LFV 与新场约束。一次优化未找到解不等于数学上无解；可行点也不证明整个扩展参数域允许。
''')

section('### 5.2 动能混合','### 5.3 有限 VLL',r'''
### 5.2 动能混合

**原文（Major 4.2，节选）：**

> “There is no quantitative estimate of the amount of kinetic mixing generated with the ‘benchmark’ choices of $\theta\leq10^{-2}$.”
>
> “It would be useful to have parametric estimates of the amount of kinetic mixing one expects so that readers may compare to experimental bounds.”

审稿人要求有限 benchmark 的定量结果。先区分超荷项和光子项：
\[
\mathcal L\supset-\frac{\epsilon_B}{2}B_{\mu\nu}X^{\mu\nu},
\qquad \mathcal L\supset-\frac{\epsilon_\gamma}{2}F_{\mu\nu}X^{\mu\nu}.
\]
在此归一化、同一尺度和动能/质量完整对角化之前，$B_\mu=c_WA_\mu-s_WZ_\mu$ 给出一阶系数关系 $\epsilon_\gamma=c_W\epsilon_B$，并同时产生 $ZX$ 项。若文献将超荷项写作 $-\epsilon B_{\mu\nu}X^{\mu\nu}/(2c_W)$，其名为 $\epsilon$ 的量不同；跨尺度须另作运行与阈值匹配。

实验物理耦合须在规范动能和质量同时对角化后读取。轻 $A'$ 极限的光子耦合近似须写出适用质量层次。纯轴电流的光子一圈混合消失，不意味着整个超荷/中性规范系统无混合。下面的具体方法明确荷、质量、边界、外动量和物理电流；某尺度的零边界不自动是全尺度结论。
''')
s=s.replace(r'-\frac{\epsilon}{2}B_{\mu\nu}X^{\mu\nu}',r'-\frac{\epsilon_B}{2}B_{\mu\nu}X^{\mu\nu}')
s=s.replace('其中 \\(B_{\\mu\\nu}\\) 和 \\(X_{\\mu\\nu}\\) 分别代表相应的规范场强张量；具体符号应与论文保持一致。',
 r'其中 $B_{\mu\nu}$ 为超荷场强，$X_{\mu\nu}$ 为新规范场强；光子混合另记 $\epsilon_\gamma$，换算及物理电流按 §5.2 处理。')
before('**任务 C：在 benchmark 下计算数值**',r'''
**把任务 B 落到积分与耦合矩阵。** 先精确对角化轻重带电轻子矩阵，得到质量 $m_i$ 及
\[
G_L=U_L^\dagger Q_LU_L,\qquad G_R=U_R^\dagger Q_RU_R.
\]
若用 $\bar f\gamma^\mu(g_V+g_A\gamma^5)fX_\mu$，则 $g_V=(g_R+g_L)/2$、$g_A=(g_R-g_L)/2$；若论文采用负号定义 $\gamma^5$ 项，要连同轴耦合符号一起转换。高能超荷顶点要保留左右手不同的荷，不能套用光子向量顶点。

光子—$X$ 的一圈计算对象是横向真空极化系数。用统一顶角写费米子闭环的 Dirac/味迹，维数正规化后约化到标量积分，加入混合反项。对质量本征态中的对角光子顶点，向量贡献的动量依赖含核
\[
I(m,q^2;\mu)=\int_0^1dx\,x(1-x)
\log\frac{m^2-x(1-x)q^2-i0}{\mu^2}.
\]
完整系数的符号、荷因子、色重数及归一化必须从上述顶角算出，不将这个积分核冒充 v6 的最终 $\epsilon$ 公式。光子一向量、一轴顶点的真空二点图因可构造的张量结构而消失；超荷手征顶点、$Z$ 混合和其他质量混合需独立分析。

执行顺序是：列全轻重本征态与耦合 → 求横向投影和 UV 发散 → 固定 $\epsilon_B(\mu_0)$ 及反项 → 匹配重阈值并运行 → 在目标 $q^2$ 求有限部分 → 对角化规范动能/质量 → 读取过程中的实际电流。低于阈值的展开与完整积分在共同区域比较；类时 $q^2$ 跨过 $4m_i^2$ 时保留虚部，不能只用实对数。成对荷相消须先对整对求和，检查严格简并、轻重混合和质量分裂分别如何改变结果。

尺度/动量和边界条件会改变动能混合，这是 [Hapitas、Tuckler、Zhang 的分析](https://arxiv.org/abs/2108.12440)强调的方法问题；其矢量 $L_\mu-L_\tau$ 系数不能直接代替本轴矢量 UV 模型的计算。最终至少做横向性、量纲、严格简并、纯轴极限和不同尺度下匹配一致性检查，再谈参数估计。
''')
before('### 5.6 原始 Major 4',r'''
#### 5.5.6 从物理耦合计算实验事件率：重铸的具体方法

先锁定实验限制对象：截面、截面乘 BR、可见事件数、分箱信号模板或精密观测量。对可作窄宽度因子化的产生与衰变，逐箱预测可写为
\[
N_k^{\rm sig}=\mathcal L\int d\Phi\,
\frac{d\sigma_{\rm prod}}{d\Phi}\,
\mathrm{BR}(X\to f)\,P_{\rm fid}(\Phi)\,
\mathcal A_k(\Phi)\varepsilon_k(\Phi).
\]
其中 $\Phi$ 是运动学变量，$P_{\rm fid}$ 是探测体积内衰变概率，$\mathcal A,\varepsilon$ 为接受度和效率；二者的约定应避免重复计数。沿固定轨迹、指数衰变近似下，
\[
P_{\rm fid}=e^{-L_{\rm in}/(\beta\gamma c\tau)}
-e^{-L_{\rm out}/(\beta\gamma c\tau)}.
\]
对 boost 分布逐事件加权，不能总用平均 boost 代替。若是宽共振、强干涉或重叠态，先计算完整末态微分率，不能把干涉强行写成相互独立的 $\sigma\times\mathrm{BR}$。固定靶还须使用真实束流、靶材、通量和几何的积分。

**可直接缩放时。** 只有自旋、质量、线形、运动学选择和寿命足以保持效率相同时，才用 $\sigma\,\mathrm{BR}$ 比例缩放原信号，并注明近似误差。效率发生变化时重新模拟或使用官方效率图；先复现实验给出的参考信号点，核对产额与公开上限，再运行本模型。没有效率/似然信息时，保留重铸缺口，不凭耦合平方比宣称精确排除。

**需要统计比较时。** 若官方给出分箱似然，采用其背景和相关系统误差；一个计数模型的示意为
\[
\mathscr L(\mu,\eta)=\prod_k\operatorname{Pois}
(n_k\mid\mu s_k(\eta)+b_k(\eta))\,\pi(\eta).
\]
这里 $\eta$ 是 nuisance 参数，$\pi$ 是辅助约束。使用实验同一检验统计量、单/双侧约定和置信水平；$CL_s$ 与普通置信区间不能混称。剖面似然的渐近公式可对照 [Cowan 等](https://arxiv.org/abs/1007.1727)，低计数或边界条件不适用时需伪实验校准。若只有同信号假设的官方上限 $X_{95}$，比较 $X_{\rm model}/X_{95}$ 仅适用于该对象与假设，不自动等于重新构建了完整似然。不同实验有公共数据或系统误差时不能直接相乘似然。

**恒星/超新星另作输运检查。** 先从模型过程求单位体积的能谱产生率 $d\dot n_X/dE$，在自由逃逸近似下积分
\[
L_X\simeq\int dV\,dE\,E\frac{d\dot n_X}{dE}P_{\rm esc}(E,r).
\]
沿路径的吸收光深为 $\tau_{\rm abs}=\int ds/\ell_{\rm abs}$；稀薄近似可用指数生存因子，并另外处理衰变与能量沉积。强俘获时此简单逃逸式不足，须按原分析的输运/扩散处理重算。温度、密度、化学势、介质修正和粒子种类均来自被采用的天体模型；不另造通用冷却阈值。分别给 $S$ 与 $A'$ 算产生、吸收和逃逸，保存自由逃逸、俘获和未评估的分支。

**交付与失败处理。** 每项约束输出参考信号复现、本模型信号、效率/寿命处理、统计定义、排除或不适用理由及误差。若只完成振幅或积分核，状态停在该步骤；实验结论须等对应产额与统计检验实际完成。
''')

before('#### 工作 C：检查 EFT 的适用范围',r'''
**工作 B 的逐步匹配方法。** 对每个 $\alpha=\mu,\tau$，从原稿复制实际 $y_\alpha$、$\lambda_\alpha$ 顶角及 $S$ 或 $S^\dagger$ 指派，画具有相同轻外线的重 $E_\alpha$ 交换图。采用已固定的场相位和拉氏量正负号，不先由量纲猜系数符号。

重传播子的低动量展开为
\[
\frac1{\slashed p-M_E}
=-\frac1{M_E}\left(1+\frac{\slashed p}{M_E}
+\frac{p^2}{M_E^2}+\cdots\right).
\]
将两端手征投影实际相乘，保留首个非零项，匹配到选定的规范不变算符基底，得到原稿维五系数量级 $y_\alpha\lambda_\alpha/M_{E_\alpha}$。有的导数项因手征结构消失，不能普遍把第一项相对误差指定为 $p/M_E$ 或 $p^2/M_E^2$。用该过程的下一非零项定阶，并检查外线方程、基底约化及厄米共轭的重复计数。

第二条独立检查是消去重场的经典运动方程，再代回拉氏量；与同外线振幅展开比较，核对 $1/\sqrt2$、场共轭和符号。非简并 VLL 分别在阈值匹配；要做一圈匹配时，计算同一方案的 UV 与 EFT 振幅，减去共同低能贡献后提取短程系数，不能把完整 UV 圈图全部当作 Wilson 系数。一般匹配方法可参见 [重场路径积分匹配研究](https://doi.org/10.1140/epjc/s10052-021-09587-7)，本处公式须由 v6 顶角具体实现。

**从匹配转到质量及误差。** 插入 VEV 后检验轻质量近似 $m_\alpha\simeq y_\alpha\lambda_\alpha vv_S/(2M_{E_\alpha})$，与精确轻重矩阵的奇异值比较；同时检查两侧旋转及 Yukawa 微扰性（§6.3.2）。对于用于约束的过程，选相同外线、输入参数与相空间切选，分别算完整 UV 和截断 EFT 的振幅/率。在前向、阈值和共振附近单独加密；误差须在实验相关的分箱或积分量上验收。若参考率接近零，改用绝对误差或包含实验尺度的混合容差，避免相对误差假发散。

输出应包含匹配式的完整归一化、保留阶数、首个遗漏项、精确质量比较、过程误差及其适用区间。反演 UV 参数时，找到一个满足条件的点可证明该 EFT 点有实现；有限扫描未找到则只能报告搜索范围与失败状态，除非另有解析排除证明。
''')

before('### 6.4 "Conservative benchmark"',r'''
#### 6.3.2 Yukawa 微扰性与小混合联合给出的 $v_S$ 下界

原有 $M_E\gtrsim17.8\,\mathrm{TeV}$ 需保留；还须检查生成 $\tau$ 质量的 UV Yukawa。在 v6 小混合近似下，
\[
m_{\tau R}=\lambda_\tau v_S/\sqrt2,\qquad
|\theta_{\tau R}|\simeq|m_{\tau R}|/M_E,\qquad
m_\tau\simeq|\theta_{\tau L}\lambda_\tau|v_S/\sqrt2.
\]
$\lambda_\tau$ 是 $S$ 的轻重轻子 Yukawa，不是标量自耦合 $\lambda_S$，也不是有效耦合 $y_{s\tau\tau}\simeq m_\tau/v_S$。若在同一参考尺度额外选定 $|\lambda_\tau|\le\lambda_{\max}$，并用 $|\theta_{\tau L}|\le10^{-2}$，则
\[
v_S\gtrsim\frac{\sqrt2\,m_\tau}{10^{-2}\lambda_{\max}}.
\]
用 $m_\tau\simeq1.77686\,\mathrm{GeV}$ 仅作量级示例：$\lambda_{\max}=\sqrt{4\pi}$ 时约 70.9 GeV；若改用 $4\pi$，则约 20.0 GeV。两种判据不可混用或称为实验界。在相同小混合关系下取 $v_S=2\,\mathrm{GeV}$ 需要 $|\lambda_\tau|\gtrsim125.6$，不能仅凭标量自耦合通过就称整个 UV 点微扰可行。

单 VEV 的 $m_{A'}=2g_Xv_S$ 在第一种判据下还给出条件性 $g_X\lesssim7.05\times10^{-3}(m_{A'}/\mathrm{GeV})$。真正扫描要用同一尺度的质量、Yukawa 和完整轻重矩阵重算；这里使用近似极点质量未包含运行与联合实验分析。额外质量来源、不同混合限制或新 VEV 会改变结论。

执行时精确求轻重奇异值与两侧旋转，再核验 $y_\tau,\lambda_\tau$；分别记录质量、两角、UV Yukawa 和标量自耦合的判据与失败原因。
''')
s=s.replace('| $M_{E_\\mu},M_{E_\\tau}$ | 矢量样轻子质量',r'| $y_\alpha,\lambda_\alpha$ | UV Yukawa | 同尺度微扰性和精确质量矩阵 | 与混合、$v_S$ 联合检查，见 §6.3.2 |'+'\n'+r'| $M_{E_\mu},M_{E_\tau}$ | 矢量样轻子质量')
s=s.replace('- **解析预筛选：** 检查规范荷/质量关系、标量势的有界性条件、明显违反的微扰性界限，以及模型定义要求的质量关系。',
 '- **解析预筛选：** 检查规范荷、质量关系、标量势有界性与各耦合微扰性；同时执行 §6.3.2 的 UV Yukawa—轻子质量—混合联合条件，不能只检查标量自耦合。')
s=s.replace('> 极化不对称可能区分左右手耦合，μ/τ 末态比较可能检验味结构；但是否值得加入取决于统计精度和系统误差。',
 r'> 极化不对称可能区分左右手耦合；原文提出的是 $ee$ 与 $\tau\tau$ 末态比较。须由真实振幅判断是否提供互补信息，再评估统计和系统误差。电子在原模型树级新规范相互作用下中性，不能因此假定存在直接电子耦合。')
for a,b in [('最终投稿稿 PDF','当前存档稿 v6 PDF'),('最终投稿稿 `axial_vector_model_building-v6.pdf`','当前存档稿 `axial_vector_model_building-v6.pdf`'),('最终稿 v6','当前存档稿 v6')]:s=s.replace(a,b)
a=s.index('## 附录 B：');b=s.index('## 附录 C：',a)
s=s[:a]+s[a:b].replace('最终稿','当前存档稿 v6')+s[b:]
s=s.replace('后续回复信应引用当前存档稿 v6的 Ref. [85]','后续回复信应按实际修订稿核定编号；若沿用当前存档稿 v6，则为 Ref. [85]')
before('**与原始审稿报告的差异：**','**边界范围：** 约 2 GeV 只来自上述标量自耦合与质量 benchmark，不包含 UV Yukawa 与小混合联合条件。§6.3.2 给出额外判据下更强的条件性下界，须在同一点另查。')
before('状态可以因发现错误而回退。','''**适用性规则。** S0–S7 是证据里程碑，不是每项工作必须逐级通过的统一流水线。先列必需检查；纯解析对称性证明可独立复核后完成论文/回复闭环，无须虚构数值扫描或重铸。术语修改也不要求圈图或拟合。不适用环节写 N/A 并说明理由；N/A 不是新增证据等级。S7 表示该命题所有适用检查与写作落点齐备，不代表做过所有 S3–S6 类型工作。数值或实验主张仍必须有相应证据。''')
s=s.replace('| `method` | 解析推导、数值积分、扫描、实验重铸等 |','| `method` | 解析推导、数值积分、扫描、实验重铸等 |\n| `required_checks` | 对该命题必需的验证与里程碑 |\n| `not_applicable_checks` | N/A 环节及理由，不能以未完成冒充不适用 |')
s=s.replace('若链条中间缺失一环，应把状态停在相应阶段。','先确定环节是否适用，N/A 须写理由；若必需环节缺失，应把状态停在相应阶段。')
s=s.replace('| 证据等级 | S0–S7 |','| 证据等级 | S0–S7，按任务适用的里程碑登记 |\n| 必需检查 / N/A | 必需验证、未适用环节及理由 |')
s=s.replace('| `epsilon_kin`, `g_V`, `g_A` | 动能混合与有效矢量/轴耦合，避免重复计数 |',
 '| `epsilon_B_at_mu0`, `epsilon_gamma_at_q2` | 分别记录超荷边界和光子混合，注明基底、归一化、尺度/动量与运行 |\n| `g_V`, `g_A`, `current_convention` | 物理电流及符号，区分直接 VLL 与动能混合贡献 |')

rows=[]
for ms in [100,124,124.99,124.999,125,126]:
 d=ms*ms-125**2;alpha=.5*math.atan2(2,d);theta=alpha if abs(alpha)<=math.pi/4 else alpha-math.copysign(math.pi/2,alpha)
 small=f'{math.degrees(1/d):.6f}' if d else '不定义'
 rows.append(f'| {ms} | {abs(d):.6f} | {math.degrees(theta):+.6f} | {small} |')
section('### F.1 ','### F.4 ',r'''
### F.1 验证输入与本征态标签

采用 §2.2 工作 E 的同一约定，不再另定旋转。输入 $a=(125\,\mathrm{GeV})^2$、$\Delta=1\,\mathrm{GeV}^2$，改变 $b=m_{s,0}^2$。按分支算法求角后，直接计算 $R\mathcal M_0^2R^T$，检验非对角元、特征根、迹、行列式及反解输入。残差按质量平方量级归一，零值另设绝对容限。

### F.2 同一分支的精确角与小角对照

| $m_{s,0}$（GeV） | $\lvert b-a\rvert$（GeV$^2$） | 精确角（度） | 小角外推（度） |
|---:|---:|---:|---:|
'''+ '\n'.join(rows)+r'''

100、124、126 GeV 三行处于小角区；124.99 GeV 已有显著误差，124.999 GeV 的小角外推失效，125 GeV 行无小角展开。质量差两侧必须用同一 Higgs 候选分支比较；未经处理的半角 atan2 可能得到近 90 度的等价重标记，不能直接当作小角误差。

穿过等权混合处，按“较大 $h$ 分量”标记的态可交换质量排序，角度分支可跳变而可观测谱无奇异性。$a=b$ 时本例质量平方为 $(125\,\mathrm{GeV})^2\pm1\,\mathrm{GeV}^2$，质量差约 0.008 GeV；这不是 UV 模型预测。误差比较用同一分支的弧度角，零角附近改用绝对误差及旋转残差。

### F.3 宽度与自能的独立触发检查

真实模型分别比较质量差与 $\Gamma_i$，以及质量平方差与质量基底自能 $\lvert\widehat\Pi_{12}\rvert,m_i\Gamma_i$。目标精度要求时求重整化极点，共同初末态的重叠贡献需要时算完整振幅；随后再处理实验分辨率、效率和背景。该检查决定计算精度，不直接给出排除。
''')
section('## G.4 ','## G.5 ',r'''
## G.4 Major 1.3：门户、二点混合、近简并与实验信号

门户四点算符与二点自能不同。统一旋转下 $\tan2\theta=2\Delta/(b-a)$，分支按第 2 章工作 E。$h_2\to A'A'$ 要求 $m_2>2m_{A'}$，$h_1\to h_2h_2$ 要求 $m_1>2m_2$，且均须非零顶角。混合增强、实验排除与 EFT 中可忽略标量是独立判断。完整方法在 §2.2 工作 D–H，附录 F 只作数值复核。
''')
section('## G.6 ','## G.9 ',r'''
## G.6 Major 3 与 Major 4.1：从荷到 PMNS

三轻态近似下 $U_{\rm PMNS}=U_{\ell,L}^\dagger U_\nu$。当前最小荷表与 VEV 保留 $Z_2$，电子味分块无法复现观测混合；第 4 章给出算符表、证明和扩展验证方法。两条审稿意见共用证据，分别按原编号回复。

## G.7 Major 4.2：动能混合的基底与边界

超荷项为 $-\epsilon_B B_{\mu\nu}X^{\mu\nu}/2$，光子项另记 $\epsilon_\gamma$；同尺度场强分解在本约定下一阶给出 $\epsilon_\gamma=c_W\epsilon_B$，物理电流仍须对角化。荷迹、阈值、质量分裂、动量和边界共同决定结果；详见 §5.2、§5.5。

## G.8 Major 4.3 与 Minor 2–3：VLL 混合与残余矢量耦合

v6 约定中 $g_{V\mu}=g_X\sin^2\theta_{\mu R}$、$g_{A\mu}=-g_X\cos^2\theta_{\mu R}$，$\theta_{\mu R}\to0$ 给出纯轴极限。质量下限须通过实际矩阵与衰变假设才能传到耦合；同时检查 UV Yukawa 微扰性，见 §6.3.2。
''')
s=s.replace('$M_{\nm VLL}$',r'$M_{\rm VLL}$')
report=(ROOT/'dw13678_report_1_a.md').read_text(encoding='utf-8')
stmt=[l.strip() for l in report.splitlines() if 'artificial' in l.lower()]
assert stmt
before('---\n\n## 附录 B','### A.12 Statement\n\n'+'\n'.join('> '+l for l in stmt)+'\n\n这是审稿人的来源声明，不是新增物理任务。')
s=s.replace('以下保留审稿报告的英文措辞、编号、拼写及标点；为便于阅读，仅将 PDF 的换行合并为段落，并将公式符号转写为 LaTeX。','以下按原编号保存英文技术措辞，换行、引号/连字符和公式作阅读性转写，不保证标点逐字符一致。转写与 PDF 有异时，以视觉核验的 PDF 为准；Minor 5 为 $ee$ 与 $\\tau\\tau$，转写 MD 的 TT 为识别问题。')
for id_,target in [('m6-6','§6.6、附录 B.1、附录 G.15.6'),('SRC-VS-LINE','§6.6、附录 B.1、附录 G.15.6'),('ST-1','附录 A.12')]:
 p=re.compile(r'(^### '+re.escape(id_)+r'\b.*?)(?=^### |\Z)',re.M|re.S);m=p.search(s);assert m,id_
 block=m.group(1).replace('§13.1',target) if id_!='ST-1' else m.group(1).replace('附录 A.11',target)
 s=s[:m.start()]+block+s[m.end():]
s=s.replace('> **v5.6｜Major 1–4 统一闭环版：从审稿诉求到执行、回复与验收｜2026-10-20**','> **v5.7｜物理校核与专题连续阅读版｜2026-10-20**')
s=s.replace('- **v5.6（本版，2026-10-20）：**','- **v5.6（2026-10-20）：**')
s=s.replace('## v5.6 阅读结构说明','## v5.7 阅读结构说明')
s=s.replace('v5.6 完成的是**Major 1–4 统一专题闭环、执行方法与结案验收结构的补齐**','v5.7 完成的是**公式逻辑校核、连续阅读结构与方法说明的完善**')
assert not [(i,ord(c)) for i,c in enumerate(s) if ord(c)<32 and c not in '\n\r'],'control chars'
(ROOT/'work/v57_enhanced.md').write_text(s,encoding='utf-8')
print('Enhanced characters:',len(s))
