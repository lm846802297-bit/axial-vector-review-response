# 轴矢量 $A'$ 低质量超新星辐射：详细解析推导与数值结果

本文给出原始单 VEV 轴矢量模型中纵向 $A'$ 低质量增强的解析推导，包括轴流散度、半康普顿双图振幅、Ward identity、纵向极化、Goldstone 等价关系、热发射率相空间积分，以及由局域产生率到自由逃逸冷却下界的质量标度。

## 1. 模型关系与问题设定

考虑由单个带电标量单态 $S$ 破缺 $U(1)_X$ 的模型。将复标量写为

$$
S(x)=\frac{1}{\sqrt{2}}\left[v_s+s(x)+i a_s(x)\right],
$$

其中 $v_s$ 是真空期望值，$s$ 是径向物理标量，$a_s$ 是 Goldstone 模。在规范选择下，$a_s$ 成为 massive gauge boson $A'$ 的纵向自由度。

若 $S$ 的 $U(1)_X$ 电荷为 $2$，规范玻色子质量为

$$
m_{A'}=2|g_X|v_s.
\tag{1}
$$

因此

$$
|g_X|=\frac{m_{A'}}{2v_s}.
\tag{2}
$$

在小轻–重带电轻子混合的轴矢量极限下，带电轻子的相互作用可写为

$$
\mathcal L_{\rm int}
=
A'_\mu\,
\bar\ell\gamma^\mu
\left(g_V^\ell-g_A^\ell\gamma_5\right)\ell,
$$

且对缪子有

$$
g_V^\mu\simeq 0,
\qquad
|g_A^\mu|\simeq |g_X|.
\tag{3}
$$

以下研究的主要过程是

$$
\mu^\pm(p)+\gamma(k)
\longrightarrow
\mu^\pm(p')+A'(q),
\tag{4}
$$

特别关注 $A'$ 的纵向极化态。低质量增强来自轴流不守恒与纵向极化矢量的 $q^\mu/m_{A'}$ 项，而不是普通守恒矢量流的性质。

---

## 2. 轴流 Ward identity 的详细推导

### 2.1 自由缪子轴流的散度

定义轴流和赝标量双线性：

$$
J_A^\mu=\bar\mu\gamma^\mu\gamma_5\mu,
\qquad
P=\bar\mu i\gamma_5\mu.
$$

自由 Dirac 方程及其 Dirac 共轭方程分别为

$
(i\gamma^\mu\partial_\mu-m_\mu)\mu=0.
\tag{5}
$

$
i(\partial_\mu\bar\mu)\gamma^\mu
+m_\mu\bar\mu=0.
\tag{6}
$

由式 (5) 得

$
\gamma^\mu\partial_\mu\mu=-i m_\mu\mu,
$

由式 (6) 得

$
(\partial_\mu\bar\mu)\gamma^\mu
=i m_\mu\bar\mu.
$

对轴流求散度：

$$
\begin{aligned}
\partial_\mu J_A^\mu
&=
(\partial_\mu\bar\mu)\gamma^\mu\gamma_5\mu
+
\bar\mu\gamma^\mu\gamma_5\partial_\mu\mu\\
&=
i m_\mu\bar\mu\gamma_5\mu
+
\bar\mu\gamma^\mu\gamma_5\partial_\mu\mu.
\end{aligned}
$$

利用反对易关系

$$
\{\gamma^\mu,\gamma_5\}=0,
$$

第二项可写为

$$
\bar\mu\gamma^\mu\gamma_5\partial_\mu\mu
=
-\bar\mu\gamma_5\gamma^\nu\partial_\nu\mu
=
i m_\mu\bar\mu\gamma_5\mu.
$$

所以

$$
\partial_\mu J_A^\mu
=
2i m_\mu\bar\mu\gamma_5\mu
=
2m_\mu P.
\tag{7}
$$

式 (7) 表明，有限质量缪子的轴流不是守恒流。这里讨论的是树级外线 Ward identity；量子层面的电磁轴反常不属于本次树级半康普顿振幅推导。

### 2.2 半康普顿过程的两个树图

过程 (4) 有两个缪子交换图。令入射光子的偏振矢量为 $\epsilon_\alpha(k)$，并定义两个内部缪子传播子的分母

$$
D_s=(p+k)^2-m_\mu^2,
\qquad
D_u=(p-q)^2-m_\mu^2.
$$

外部粒子满足壳条件

$$
p^2=p'^2=m_\mu^2,
\qquad
k^2=0,
\qquad
q^2=m_{A'}^2,
$$

以及四动量守恒

$$
p+k=p'+q.
\tag{8}
$$

为避免在 Ward identity 中重复计入轴耦合，先定义不含 $g_A^\mu$ 的约化轴流振幅。入射光子先作用的 $s$ 道图为

$$
\begin{aligned}
\widehat{\mathcal M}_s^{\mu\alpha}
={}&eQ_\mu\,
\bar u(p')\gamma^\mu\gamma_5
\frac{\gamma^\rho(p+k)_\rho+m_\mu}{D_s}
\gamma^\alpha u(p).
\end{aligned}
\tag{9a}
$$

出射 $A'$ 先作用的 $u$ 道图为

$$
\begin{aligned}
\widehat{\mathcal M}_u^{\mu\alpha}
={}&eQ_\mu\,
\bar u(p')\gamma^\alpha
\frac{\gamma^\rho(p-q)_\rho+m_\mu}{D_u}
\gamma^\mu\gamma_5u(p).
\end{aligned}
\tag{9b}
$$

两图相加并收缩入射光子偏振后，

$$
\widehat{\mathcal M}_A^\mu
=
\left(
\widehat{\mathcal M}_s^{\mu\alpha}
+
\widehat{\mathcal M}_u^{\mu\alpha}
\right)\epsilon_\alpha(k).
\tag{9c}
$$

完整的轴矢量振幅为

$$
\mathcal M_A^\mu
=
g_A^\mu\widehat{\mathcal M}_A^\mu.
\tag{9d}
$$

这里 $Q_\mu=-1$；对反缪子过程使用相应的反粒子外线自旋器和电荷共轭规则。两个图必须同时保留，才能得到完整的 Ward identity 和满足光子规范不变性的振幅。

定义 $\widehat{\mathcal M}_P$ 为与赝标量双线性 $P=\bar\mu i\gamma_5\mu$ 对应的约化两图振幅。它包含相同的光子顶点、传播子、外线自旋器和光子偏振，但不包含 $g_A^\mu$；其整体相位约定使树级轴流 Ward identity 写为

$$
q_\mu\widehat{\mathcal M}_A^\mu
=
2m_\mu\widehat{\mathcal M}_P.
\tag{10}
$$

因此完整振幅满足

$$
q_\mu\mathcal M_A^\mu
=
2g_A^\mu m_\mu\widehat{\mathcal M}_P.
$$

这一区分保证后续纵向振幅中只出现一次轴耦合 $g_A^\mu$。Ward identity 也说明轴流顶点收缩后并不为零，而是转化为一个与缪子质量成正比的赝标量振幅。

需要强调，式 (10) 中的 $\widehat{\mathcal M}_P$ 已包含两个交换图、传播子分母、光子顶点、外线自旋器和光子偏振矢量；它不是单独一个 $\bar u\gamma_5u$ 因子。

---

## 3. 纵向极化与 $1/m_{A'}$ 增强

### 3.1 纵向极化矢量

在介质静止系中，令

$$
q^\mu=(E_{A'},\mathbf q),
\qquad
|\mathbf q|=q.
$$

取纵向方向沿 $\mathbf q$，则 massive vector 的纵向极化可写为

$$
\epsilon_L^\mu(q)
=
\frac{1}{m_{A'}}
\left(q,\,E_{A'}\widehat{\mathbf q}\right).
\tag{11}
$$

它满足

$$
q_\mu\epsilon_L^\mu=0,
\qquad
\epsilon_{L\mu}\epsilon_L^\mu=-1,
\tag{12}
$$

其中采用度规 $g_{\mu\nu}={\rm diag}(1,-1,-1,-1)$。

由壳条件

$$
E_{A'}^2-q^2=m_{A'}^2
$$

可将式 (11) 改写成

$$
\epsilon_L^\mu(q)
=
\frac{q^\mu}{m_{A'}}
-
\frac{m_{A'}}{E_{A'}+q}
\left(1,-\widehat{\mathbf q}\right).
\tag{13}
$$

第二项相对于第一项在 $E_{A'}\gg m_{A'}$ 时受到质量比抑制。因此

$$
\epsilon_L^\mu(q)
=
\frac{q^\mu}{m_{A'}}
+
O\!\left(\frac{m_{A'}}{E_{A'}}\right).
\tag{14}
$$

### 3.2 纵向振幅

纵向振幅定义为

$$
\mathcal M_L
=
\epsilon_{L\mu}(q)\mathcal M_A^\mu.
$$

代入式 (14)：

$$
\begin{aligned}
\mathcal M_L
&=
\left[
\frac{q_\mu}{m_{A'}}
+
O\!\left(\frac{m_{A'}}{E_{A'}}\right)
\right]\mathcal M_A^\mu\\
&=
\frac{q_\mu\mathcal M_A^\mu}{m_{A'}}
+
O\!\left(\frac{m_{A'}}{E_{A'}}\mathcal M_A\right).
\end{aligned}
$$

将式 (10) 乘以 $g_A^\mu$，并用于完整振幅：

$
\mathcal M_L
=
\frac{2g_A^\mu m_\mu}{m_{A'}}\widehat{\mathcal M}_P
+
O\!\left(\frac{m_{A'}}{E_{A'}}\mathcal M_A\right).
$

因此

$$
\boxed{
\mathcal M_L
\simeq
\frac{2g_A^\mu m_\mu}{m_{A'}}\widehat{\mathcal M}_P
}
\qquad (E_{A'}\gg m_{A'}).
\tag{15}
$$

因此，在其他运动学变量固定且赝标量振幅有限时，

$$
|\mathcal M_L|^2
\simeq
\frac{4(g_A^\mu)^2m_\mu^2}{m_{A'}^2}
|\widehat{\mathcal M}_P|^2.
\tag{16}
$$

故纵向模式的平方振幅具有

$$
\boxed{
|\mathcal M_L|^2\propto
\frac{(g_A^\mu)^2m_\mu^2}{m_{A'}^2}.
}
\tag{17}
$$

这就是固定耦合时的 $1/m_{A'}^2$ 低质量增强。

### 3.3 为什么守恒矢量流没有同样增强

对守恒矢量流 $J_V^\mu=\bar\mu\gamma^\mu\mu$，外线 Dirac 方程给出

$$
\partial_\mu J_V^\mu=0.
$$

相应振幅满足

$$
q_\mu\mathcal M_V^\mu=0.
\tag{18}
$$

于是纵向振幅中的 leading term

$$
\frac{q_\mu\mathcal M_V^\mu}{m_{A'}}
$$

严格为零。矢量流的纵向振幅只由式 (13) 中的次领先项贡献，不出现式 (15) 那样的 $m_\mu/m_{A'}$ 增强。

因此，本模型低质量增强来自轴流的非守恒性，而不是 massive vector 的纵向极化本身自动产生的普遍增强。

---

## 4. Goldstone 等价关系与 UV 参数映射

### 4.1 Goldstone–缪子耦合

由式 (7)，轴流与 Goldstone 模的耦合必须重现轴流散度。对质量为 $m_{A'}$ 的规范玻色子，纵向等价 Goldstone 的有效缪子耦合大小为

$$
g_{G\mu\mu}
=
\frac{2|g_A^\mu|m_\mu}{m_{A'}}.
\tag{19}
$$

在原始单 VEV 模型中，

$$
m_{A'}=2|g_X|v_s,
\qquad
|g_A^\mu|\simeq |g_X|.
$$

将其代入式 (19)：

$$
\begin{aligned}
g_{G\mu\mu}
&\simeq
\frac{2|g_X|m_\mu}{2|g_X|v_s}\\
&=
\frac{m_\mu}{v_s}.
\end{aligned}
$$

因此

$$
\boxed{
g_{G\mu\mu}\simeq\frac{m_\mu}{v_s}.
}
\tag{20}
$$

这与单 singlet 通过 Yukawa 质量生成所得到的 Goldstone/相位耦合一致。

### 4.2 固定 $g_X$ 与固定 $v_s$ 是不同的极限

从式 (17)，局域纵向发射率在低质量极限的主要耦合因子为

$$
Q_L\propto
\frac{g_X^2m_\mu^2}{m_{A'}^2}.
\tag{21}
$$

**情形 A：固定 $g_X$，改变 $m_{A'}$。**

$$
Q_L\propto m_{A'}^{-2}.
\tag{22}
$$

这时 $m_{A'}$ 越小，纵向辐射越强。

**情形 B：固定 $v_s$，沿原 UV 模型关系改变 $m_{A'}$。**

由

$$
g_X=\frac{m_{A'}}{2v_s}
$$

得到

$$
\begin{aligned}
Q_L
&\propto
\frac{m_{A'}^2}{4v_s^2}
\frac{m_\mu^2}{m_{A'}^2}\\
&=
\frac{m_\mu^2}{4v_s^2}.
\end{aligned}
$$

即

$$
\boxed{
Q_L\propto\frac{m_\mu^2}{4v_s^2}
}
\qquad (v_s\ {\rm fixed}).
\tag{23}
$$

所以沿固定 $v_s$ 的 UV 参数轨迹，显式的 $m_{A'}^{-2}$ 增强被 $g_X^2\propto m_{A'}^2$ 抵消。低质量极限是有限的，而不是发散的。

---

## 5. 半康普顿过程的热发射率

### 5.1 相空间表达式

考虑

$$
\mu(p)+\gamma(k)\rightarrow\mu(p')+A'(q).
$$

定义不变相空间元

$$
d\Pi_i=
\frac{d^3\mathbf p_i}{(2\pi)^3\,2E_i}.
\tag{24}
$$

介质静止系中，单个极化态 $\lambda=L,+,-$ 的能量发射率为

$$
\begin{aligned}
Q_\lambda
={}&
\sum_{\eta=\mu^-,\mu^+}
\int d\Pi_p\,d\Pi_k\,d\Pi_{p'}\,d\Pi_q\\
&\times
(2\pi)^4\delta^{(4)}(p+k-p'-q)\,
E_q\,
\overline{|\mathcal M_{\eta,\lambda}|^2}\\
&\times
f_\eta(E_p)\,
f_\gamma(E_k)\,
\left[1-f_\eta(E_{p'})\right].
\end{aligned}
\tag{25}
$$

这里：

- $f_\eta$ 是热缪子 Fermi–Dirac 分布；
- $f_\gamma$ 是光子 Bose–Einstein 分布；
- $1-f_\eta(E_{p'})$ 是末态缪子 Pauli blocking；
- $E_q$ 是每次产生的 $A'$ 能量；
- $\overline{|\mathcal M|^2}$ 对初态自旋、光子偏振平均，并对末态缪子自旋求和；$A'$ 极化 $\lambda$ 单独保留。

分布函数为

$$
f_{\mu^-}(E)=
\frac{1}{e^{(E-\mu_\mu)/T}+1},
\qquad
f_{\mu^+}(E)=
\frac{1}{e^{(E+\mu_\mu)/T}+1},
\tag{26}
$$

$$
f_\gamma(E)=\frac{1}{e^{E/T}-1}.
\tag{27}
$$

式 (25) 已将 $\mu^-$ 和 $\mu^+$ 分开求和。若存在不同的反缪子化学势约定，应以相应热平衡化学势替换式 (26)。

总局域发射率为

$$
Q_A=Q_L+Q_++Q_-.
\tag{28}
$$

### 5.2 详细平衡与逆过程

逆过程为

$$
A'(q)+\mu(p')\rightarrow\gamma(k)+\mu(p).
$$

在热平衡下，Fermi–Dirac 与 Bose–Einstein 分布满足

$$
\frac{f_F(E)}{1-f_F(E)}
=e^{-(E-\mu)/T},
\qquad
\frac{f_B(E)}{1+f_B(E)}
=e^{-E/T}.
\tag{29}
$$

利用能量守恒

$$
E_p+E_k=E_{p'}+E_q
$$

以及化学势守恒，正、逆过程的统计因子满足相应的 detailed-balance 关系。该关系可用于将发射核与吸收核联系起来；在介质中计算吸收时必须保留相同的极化分辨矩阵元和正确的占据因子，不能仅用真空衰变宽度替代散射吸收率。

### 5.3 低质量标度如何进入热积分

将振幅分解为纵向与横向部分：

$$
\overline{|\mathcal M|^2}
=
\overline{|\mathcal M_L|^2}
+
\overline{|\mathcal M_+|^2}
+
\overline{|\mathcal M_-|^2}.
\tag{30}
$$

在 $m_{A'}\ll E_{A'}$ 且热相空间中主要贡献来自 $E_{A'}\gg m_{A'}$ 的区域时，由式 (16) 得

$$
\overline{|\mathcal M_L|^2}
\simeq
\frac{4(g_A^\mu)^2m_\mu^2}{m_{A'}^2}
\overline{|\widehat{\mathcal M}_P|^2}.
\tag{31}
$$

若相空间积分在 $m_{A'}\to0$ 时没有额外的红外奇异或阈值非解析性，则

$$
Q_L(m_{A'},g_X)
\simeq
\frac{g_X^2}{m_{A'}^2}
\,C_L(T,\mu_\mu,\mu_{\nu_\mu},\ldots),
\tag{32}
$$

其中 $C_L$ 是由热分布、精确 recoil 运动学和赝标量 Compton 核决定的有限函数。式 (32) 是渐近标度，而不是对任意质量和任意介质状态都成立的精确恒等式。

沿固定 $v_s$ 轨迹，

$$
Q_L
\simeq
\frac{C_L}{4v_s^2}.
\tag{33}
$$

---

## 9. 低质量限制的物理含义：从纵向增强到超新星耦合边界

本节直接回答两个问题：

1. 低质量限制是否可以从高质量结果简单乘以 $1/m_{A'}$ 得到？
2. 纵向增强是否意味着本模型在低质量超新星区域受到最强约束？

结论是：纵向振幅确实含有 $1/m_{A'}$，但实验或天体物理的耦合限制不是把某个高质量耦合界简单乘以 $1/m_{A'}$。在自由逃逸、低质量渐近区，正确的结果是耦合下界近似正比于 $m_{A'}$。完整超新星排除还取决于吸收和 trapping，不能仅从产生振幅推导高耦合边界。

### 9.1 应当缩放的是有效纵向耦合

由式 (15)，纵向发射振幅的质量和耦合依赖为

$$
\mathcal M_L
\simeq
\frac{2g_A^\mu m_\mu}{m_{A'}}\widehat{\mathcal M}_P.
$$

定义控制纵向振幅的有效耦合

$$
g_{\rm long}
\equiv
\frac{2g_A^\mu m_\mu}{m_{A'}}.
\tag{43}
$$

那么在相同热背景、相同赝标量运动学核和 $E_{A'}\gg m_{A'}$ 的近似下，

$$
Q_L\propto g_{\rm long}^2.
\tag{44}
$$

若某个低质量区的能量损失分析给出近似固定的 $g_{\rm long}$ 上限，则对应的轴矢量规范耦合上限满足

$$
|g_A^\mu|_{\rm lim}
=
\frac{m_{A'}}{2m_\mu}
g_{\rm long,lim}.
\tag{45}
$$

因此

$$
\boxed{
|g_A^\mu|_{\rm lim}\propto m_{A'}
}
\tag{46}
$$

而不是 $1/m_{A'}$。

这里要区分“振幅增强”和“耦合排除界”：固定 $g_A^\mu$ 时，降低 $m_{A'}$ 会增强振幅；固定允许的发射率时，实验允许的 $g_A^\mu$ 必须随 $m_{A'}$ 下降。

### 9.2 从局域发射率推导自由逃逸下界

在低质量渐近区，将局域纵向发射率写成

$$
Q_L(r;m_{A'},g_X)
\simeq
\frac{g_X^2}{m_{A'}^2}
C_L(r),
\tag{47}
$$

其中 $C_L(r)$ 包含缪子质量因子、热分布、赝标量半康普顿核以及局域热力学量。这里假设 $C_L(r)$ 在所考察的低质量区间趋于有限函数。

若 $A'$ 自由逃逸，红移到无穷远的 luminosity 可写成

$$
L_{A'}^\infty
\simeq
\frac{g_X^2}{m_{A'}^2}
\mathcal C_{\rm SN},
\tag{48}
$$

其中

$$
\mathcal C_{\rm SN}
=
\int dV_{\rm proper}\,
\alpha(r)^2 C_L(r)
\tag{49}
$$

表示对恒星剖面的积分；$\alpha(r)$ 是 lapse，两个 lapse 因子分别来自能量红移和时间红移。若采用不同的 luminosity 定义或坐标体积，几何因子应按相应输运定义一致处理，但质量和耦合标度不变。

冷却判据为

$$
L_{A'}^\infty=L_{\rm crit}.
\tag{50}
$$

将式 (48) 代入：

$$
\frac{g_{X,\rm lower}^2}{m_{A'}^2}
\mathcal C_{\rm SN}
=
L_{\rm crit}.
$$

于是

$$
g_{X,\rm lower}
=
m_{A'}
\sqrt{\frac{L_{\rm crit}}{\mathcal C_{\rm SN}}}.
\tag{51}
$$

因此，在自由逃逸近似和 $C_L$ 的低质量渐近区，

$$
\boxed{
g_{X,\rm lower}\propto m_{A'}.
}
\tag{52}
$$

式 (52) 是低质量冷却下界的推导。它不是说整个排除带都按同一比例缩放；特别是高耦合 trapping 边界不由式 (48) 决定。

### 9.3 映射到原始单 VEV 模型：约束 $v_s$ 而非无限增强

原始单 VEV 模型满足

$$
m_{A'}=2g_Xv_s.
\tag{53}
$$

将式 (53) 代入式 (48)：

$$
L_{A'}^\infty
\simeq
\frac{1}{4v_s^2}\mathcal C_{\rm SN}.
\tag{54}
$$

因此在固定 $v_s$ 时，低质量纵向源项趋于有限值。由冷却判据可得

$$
\frac{\mathcal C_{\rm SN}}{4v_s^2}
=
L_{\rm crit},
$$

从而

$$
\boxed{
v_s^{\rm max}
=
\frac{1}{2}
\sqrt{\frac{\mathcal C_{\rm SN}}{L_{\rm crit}}}.
}
\tag{55}
$$

这解释了为什么低质量下 $g_X$ 的下界随质量下降，但映射到 UV 模型后的 $v_s$ 上界近似保持不变。

### 9.5 为什么不能从 $1/m_{A'}$ 直接推出完整排除带

上面的推导只确定了自由逃逸区的低耦合边界。完整的超新星 luminosity 还要乘上逃逸概率。沿径向路径定义光学深度

$$
\tau_\lambda(E,r)
=
\int_r^\infty
\frac{dr'}{\lambda_\lambda(E,r')},
\tag{56}
$$

其中 $\lambda_\lambda$ 是相应极化态的吸收平均自由程。若以吸收为主，单次产生后无进一步相互作用的近似逃逸概率为

$$
P_{\rm esc,\lambda}(E,r)
\simeq e^{-\tau_\lambda(E,r)}.
\tag{57}
$$

于是示意性的逃逸 luminosity 为

$$
L_{A'}^\infty
=
\sum_{\lambda=L,+,-}
\int dV_{\rm proper}\,\alpha(r)^2
\int dE\,
Q_\lambda(E,r)
P_{\rm esc,\lambda}(E,r).
\tag{58}
$$

式 (58) 是用来说明产生与逃逸必须同时计算的表达式；在光学厚介质中，若存在再散射、再吸收后的热化和扩散，必须求解相应输运方程，不能把 $e^{-\tau}$ 当成完整扩散解。

因此：

- 低耦合边界由产生率决定，式 (52) 给出其低质量标度；
- 高耦合边界由吸收、再发射、扩散和逃逸共同决定；
- 不能仅凭纵向产生振幅的 $1/m_{A'}$ 因子推导高耦合 trapping 边界；
- 也不能把某个高质量点的完整排除区间简单乘以 $1/m_{A'}$。

### 9.7 本节结论

对本模型，正确的低质量推理链为

$$
\mathcal M_L\propto\frac{g_X}{m_{A'}},
$$

$$
Q_L\propto\frac{g_X^2}{m_{A'}^2},
$$

$$
g_{X,\rm lower}\propto m_{A'},
$$

$$
v_s^{\rm max}
=
\frac{m_{A'}}{2g_{X,\rm lower}}
\simeq {\rm constant}.
$$

因此，低质量超新星限制确实可能比中等质量区域更有效地约束原始模型的 $v_s$。现有扫描在 $0.01$–$1$ MeV 已数值验证低耦合边界的线性质量标度，并给出 $v_s=509$ GeV 模型线约 $0.684$ MeV 的 trapping 交点。

不过，以上低耦合渐近关系不决定高耦合边界。要将这一结论升级为最终轴矢量 SN1987A 限制，仍需把 moving-muon 的极化分辨产生与逆过程吸收核同时接入径向输运，重新计算 $L_{A'}^\infty$ 和 trapping 边界。