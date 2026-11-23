# 轴矢量 $A'$ 低质量超新星辐射：详细解析推导与数值结果

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

## 6. 局域 moving-muon 数值结果

### 6.1 中心热力学条件

采用的中心条件为

$$
T=19.2652211\ {\rm MeV},
$$

$$
\mu_\mu=46.6743284\ {\rm MeV},
\qquad
\mu_{\nu_\mu}=-58.6137567\ {\rm MeV}.
$$

lapse 为

$$
\alpha=0.736330427.
$$

### 6.2 极化分辨的质量扫描

以下 $Q_L,Q_+,Q_-$ 是单位 $g_X^2$ 的局域发射率，单位为 ${\rm MeV}^5$。

| $m_{A'}$ (MeV) | $Q_L/g_X^2$ | $Q_+/g_X^2$ | $Q_-/g_X^2$ | $Q_L/(Q_++Q_-)$ |
|---:|---:|---:|---:|---:|
| 0.01 | $4.51689698\times10^8$ | 17.3041981 | 17.3041981 | $1.30514\times10^7$ |
| 0.1 | $4.51687492\times10^6$ | 17.3040325 | 17.3040325 | $1.30515\times10^5$ |
| 1 | $4.51570842\times10^4$ | 17.2882616 | 17.2882616 | $1.30600\times10^3$ |
| 10 | 441.334510 | 16.0646616 | 16.0646616 | 13.76 |
| 100 | 1.06407694 | 0.948190869 | 0.948190869 | 0.561 |
| 220 | 0.00558815 | 0.00581435 | 0.00581435 | 0.481 |

### 6.3 对 $1/m_{A'}^2$ 标度的直接检验

计算

$$
C_{\rm num}(m_{A'})=m_{A'}^2\,\frac{Q_L}{g_X^2}.
\tag{34}
$$

得到

| $m_{A'}$ (MeV) | $C_{\rm num}$ (${\rm MeV}^7$) |
|---:|---:|
| 0.01 | 45168.9698 |
| 0.1 | 45168.7492 |
| 1 | 45157.0842 |

相对变化为

$$
\delta_C
=
\frac{C_{\max}-C_{\min}}{C_{\min}}
\simeq2.63\times10^{-4}
=0.0263\%.
\tag{35}
$$

因此在 $0.01$–$1$ MeV 区间，数值积分满足

$$
\frac{Q_L}{g_X^2}
\propto m_{A'}^{-2}
$$

至约 $3\times10^{-4}$ 的相对变化水平。

### 6.4 固定 $v_s=509$ GeV 的数值检验

由

$$
g_X=\frac{m_{A'}}{2v_s},
\qquad
v_s=509\ {\rm GeV},
$$

并将 $m_{A'}$ 换算为 GeV，得到

| $m_{A'}$ (MeV) | $g_X$ | $Q_L$（乘回 $g_X^2$ 后） |
|---:|---:|---:|
| 0.01 | $9.82318\times10^{-9}$ | $4.35858\times10^{-8}$ |
| 0.1 | $9.82318\times10^{-8}$ | $4.35855\times10^{-8}$ |
| 1 | $9.82318\times10^{-7}$ | $4.35743\times10^{-8}$ |

这三个数值的最大相对变化小于 $0.03\%$，验证固定 $v_s$ 时局域纵向发射率趋于常数。

### 6.5 数值积分收敛

在 $m_{A'}=10$ MeV 的中心点纯轴流 benchmark 中，外层 $A'$ 能量积分由 12 点提高到 16 点：

$$
Q_{12}=473.6806432\ {\rm MeV}^5,
$$

$$
Q_{16}=473.5796153\ {\rm MeV}^5.
$$

相对变化为

$$
\frac{Q_{16}-Q_{12}}{Q_{12}}
=-2.13283\times10^{-4}.
\tag{36}
$$

内层积分由 $(14,10,10,10)$ 加密到 $(18,14,14,14)$ 时，记录的变化约为

$$
1.6\times10^{-5}.
$$

这组收敛结果对应 $10$ MeV benchmark；它不自动代表所有质量点的积分误差。

---

## 7. 固定剖面超新星冷却数值结果

### 7.1 冷却判据与耦合排除区间

固定剖面计算使用的冷却判据为

$$
L_{\rm crit}=4.4\times10^{52}\ {\rm erg\,s^{-1}}.
\tag{37}
$$

对每个质量，luminosity 随耦合先增加；当光学深度变大、产生的 $A'$ 不能有效逃逸时，逃逸 luminosity 会受到抑制。因此冷却带通常是有限区间：

$$
g_{X,\rm lower}<g_X<g_{X,\rm upper}.
\tag{38}
$$

代表性扫描结果为：

| $m_{A'}$ (MeV) | $g_{X,\rm lower}$ | $g_{X,\rm upper}$ | 薄极限半康普顿份额 | 薄极限中微子份额 |
|---:|---:|---:|---:|---:|
| 0.01 | $3.84524\times10^{-13}$ | $1.95832\times10^{-5}$ | $\simeq1$ | $1.01\times10^{-13}$ |
| 1 | $3.84439\times10^{-11}$ | $4.94447\times10^{-7}$ | 0.999990 | $1.01\times10^{-5}$ |
| 10 | $3.60222\times10^{-10}$ | $7.47208\times10^{-8}$ | 0.913880 | 0.086120 |
| 100 | $2.38418\times10^{-10}$ | $7.25875\times10^{-9}$ | 0.006123 | 0.993877 |
| 200 | $4.14836\times10^{-10}$ | $2.86259\times10^{-9}$ | 0.001375 | 0.998625 |

“薄极限份额”指 optically thin source 中不同产生通道的相对贡献，不是吸收光学深度的分数，也不是最终逃逸 luminosity 的分数。

### 7.2 映射到原模型的 $v_s$

原始单 VEV 模型满足

$$
v_s=\frac{m_{A'}}{2g_X}.
\tag{39}
$$

将式 (38) 的耦合区间反向映射，得到

$$
\boxed{
\frac{m_{A'}}{2g_{X,\rm upper}}
<
v_s
<
\frac{m_{A'}}{2g_{X,\rm lower}}.
}
\tag{40}
$$

质量和 $v_s$ 必须使用相同能量单位。数值结果为：

| $m_{A'}$ (MeV) | 条件性冷却带映射的 $v_s$ 区间 |
|---:|---:|
| 0.01 | $0.242\ {\rm GeV}<v_s<1.300\times10^7\ {\rm GeV}$ |
| 0.1 | $15.98\ {\rm GeV}<v_s<1.300\times10^7\ {\rm GeV}$ |
| 1 | $1.011\times10^3\ {\rm GeV}<v_s<1.301\times10^7\ {\rm GeV}$ |
| 10 | $6.692\times10^4\ {\rm GeV}<v_s<1.388\times10^7\ {\rm GeV}$ |
| 100 | $6.888\times10^6\ {\rm GeV}<v_s<2.097\times10^8\ {\rm GeV}$ |

### 7.3 固定 $v_s$ 的模型线与 trapping 边界交点

固定 $v_s$ 时，模型线为

$$
g_X(m_{A'})=\frac{m_{A'}}{2v_s}.
\tag{41}
$$

与高耦合边界的交点满足

$$
\frac{m_{A'}}{2v_s}
=
g_{X,\rm upper}(m_{A'}).
\tag{42}
$$

对已有质量网格的高耦合边界作对数插值，得到：

| $v_s$ (GeV) | 交点 $m_{A'}$ (MeV) |
|---:|---:|
| 509 | 0.684 |
| 1000 | 0.995 |
| 2000 | 1.456 |
| 10000 | 3.522 |

这些交点说明：在该固定剖面冷却扫描中，$v_s$ 为几百 GeV 至几 TeV 的模型线会与亚 MeV 至数 MeV 的冷却带相交。

---

## 8. 数值结果的物理解释

局域 moving-muon 计算显示，在 $m_{A'}=0.01$–$1$ MeV 区间，纵向发射率远大于横向发射率，且

$$
m_{A'}^2Q_L/g_X^2
\simeq {\rm constant}.
$$

因此低质量区的半康普顿产生由纵向轴矢量模式控制。

沿固定 $v_s$ 轨迹，$g_X\propto m_{A'}$，故

$$
Q_L\propto
\frac{g_X^2}{m_{A'}^2}
\longrightarrow {\rm constant}.
$$

这意味着低质量端并非因发射率无限发散而变得敏感；相反，纵向产生在固定 $v_s$ 下保持有限，而横向贡献和中微子产生通道的相对作用随质量变化。固定剖面冷却扫描显示，亚 MeV 至 MeV 区域与原模型的低 $v_s$ 参数线有较大重叠。

**数值解释的范围：** 局域 moving-muon 热积分与固定剖面 luminosity 扫描是两组计算。当前固定剖面冷却曲线尚未将这里的 moving-muon 极化分辨产生和吸收核完整接入径向输运。因此，表中的 $v_s$ 区间和交点是现有固定剖面扫描的条件性映射，不应称为最终 moving-muon 修正后的 SN1987A 排除界。

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

### 9.4 用已有冷却扫描直接检验低质量标度

已有固定剖面扫描使用

$$
L_{\rm crit}=4.4\times10^{52}\ {\rm erg\,s^{-1}}.
$$

其低耦合边界为

| $m_{A'}$ (MeV) | $g_{X,\rm lower}$ |
|---:|---:|
| 0.01 | $3.84524\times10^{-13}$ |
| 0.1 | $3.84439\times10^{-12}$ |
| 1 | $3.84439\times10^{-11}$ |
| 10 | $3.60222\times10^{-10}$ |

前三个质量点检验

$$
\frac{g_{X,\rm lower}}{m_{A'}}
$$

是否近似恒定。数值为

| $m_{A'}$ (MeV) | $g_{X,\rm lower}/[m_{A'}/{\rm MeV}]$ |
|---:|---:|
| 0.01 | $3.84524\times10^{-11}$ |
| 0.1 | $3.84439\times10^{-11}$ |
| 1 | $3.84439\times10^{-11}$ |

三个点最大相对差异约为 $2.2\times10^{-4}$。所以当前扫描的低耦合边界确实满足

$$
g_{X,\rm lower}
\simeq
3.8445\times10^{-11}
\left(\frac{m_{A'}}{\rm MeV}\right)
$$

至约 $0.03\%$ 的数值精度。

相应的 $v_s$ 上界为

$$
v_s^{\rm max}
=
\frac{m_{A'}}{2g_{X,\rm lower}}.
$$

将 $m_{A'}$ 用 GeV 表示，得到

| $m_{A'}$ (MeV) | $v_s^{\rm max}$ (GeV) |
|---:|---:|
| 0.01 | $1.300\times10^7$ |
| 0.1 | $1.301\times10^7$ |
| 1 | $1.301\times10^7$ |
| 10 | $1.388\times10^7$ |

前三个点的 $v_s^{\rm max}$ 基本相同，与式 (55) 的低质量渐近预期一致。到 $10$ MeV，有限质量修正已开始变得可见。

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

### 9.6 对本模型的数值检验：固定 $v_s=509$ GeV

原模型线为

$$
g_X(m_{A'})
=
\frac{m_{A'}}{2v_s}.
\tag{59}
$$

取

$$
v_s=509\ {\rm GeV},
$$

则当 $m_{A'}$ 以 MeV 为单位时，

$$
g_X
=
9.82318\times10^{-7}
\left(\frac{m_{A'}}{\rm MeV}\right).
\tag{60}
$$

与已有冷却带比较：

- 在 $m_{A'}=0.01$ MeV，模型耦合 $9.82318\times10^{-9}$ 位于冷却带内；
- 在 $m_{A'}=0.1$ MeV，模型耦合 $9.82318\times10^{-8}$ 位于冷却带内；
- 在 $m_{A'}=1$ MeV，模型耦合 $9.82318\times10^{-7}$，已高于该质量点的 trapping 边界 $4.94447\times10^{-7}$。

用已有 trapping 边界作对数插值，求解

$$
\frac{m_{A'}}{2(509\ {\rm GeV})}
=
g_{X,\rm upper}(m_{A'}),
$$

得到交点

$$
m_{A'}\simeq0.684\ {\rm MeV}.
\tag{61}
$$

因此，在当前固定剖面扫描的定义下，$v_s=509$ GeV 的模型线在低质量端进入冷却带，并在约 $0.684$ MeV 穿出其高耦合边界。这个结果支持“低质量区可能给出更强的模型参数约束”，但其精确边界取决于 trapping 计算。

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