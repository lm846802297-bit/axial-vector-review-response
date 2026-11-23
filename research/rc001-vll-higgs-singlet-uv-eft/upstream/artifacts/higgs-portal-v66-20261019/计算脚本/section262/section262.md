

---

## 第 262 节：破缺相轻费米子两点函数、接触图、阈值与极点核（第 66 版新增）

> **范围（2026-10-20）**：以第 65 版第 261 节为输入，计算保留轻场 EFT 中的单轻带电费米子圈。本节没有重新计算重态硬匹配。先给维数五拉氏量中保留完整轻质量的精确一圈软函数，再明确取其严格 \(M^{-2}\) 部分。
>
> **本轮完成**：\(hh,hs,ss\) 的泡图和必要的 \(hs\bar\ell\ell\) 接触图，UV 极点、MS 有限部分、Coleman–Weinberg/tadpole 检查、完整解析阈值与吸收部、极点方程和外腿接口。导数极点的规范协变反项经 EOM 后与第 252 节硬对数一致；完整轻质量结果中的 \(M^{-4}\) 势极点对应维数八反项，已单列。
>
> **实际运行**：Python 62 项精确检查、8 次 \(B_0\) 积分、3 次导数积分、3 组质量趋零检查；本地 Mathematica 14.2 的 25 项独立符号检查及 6 次高精度积分均通过。未运行 FeynArts/FeynCalc、Matchete、matchmakereft 或外部图形生成器。完整物理谱仍需其余轻场及一致的输入/tadpole 方案。

### 262.1 破缺相顶点：接触图不能漏掉

本节只在 CP 偶径向、零外规范背景求两点函数，写
\[
H^0=(v+h)/\sqrt2,\qquad S=(w+s)/\sqrt2,\qquad
\mathcal L_5=-C_{5,\ell}S_\ell\bar L_\ell H\ell_R+\mathrm{h.c.}
\]
在一个轻费米子圈内只用树级
\(C_{5,\ell}^{(0)}=-y_\ell\lambda_\ell/M_\ell\)；
把第 256 节已是一圈的顶点修正再放入本圈属于两圈。逐味道重定义轻费米子相位后可取
\[
c_\ell=|C_{5,\ell}^{(0)}|,\quad
m_\ell=\frac{c_\ell vw}{2}>0,\quad
g_{h\ell}=\frac{c_\ell w}{2}=\frac{m_\ell}{v},\quad
g_{s\ell}=\frac{c_\ell v}{2}=\frac{m_\ell}{w},\quad
h_{hs,\ell}=\frac{c_\ell}{2}=\frac{m_\ell}{vw}.
\]
\(S_\tau=S^*\) 在 CP 偶实径向上的展开与 \(S_\mu=S\) 相同，故本节的 \(hs\) 泡图不带 \(s_\ell\) 相对负号；相位/电流结构仍有味道符号，见第 262.5 节。

通用质量函数和顶点约定为
\[
\mathcal L\supset-\bar\ell\ell
\left[m+g_a\varphi_a+\frac12h_{ab}\varphi_a\varphi_b\right],
\quad \varphi=(h,s),\quad h_{hs}=h_{sh},\quad h_{hh}=h_{ss}=0.
\]
单标量顶点为 \(-ig_a\)，双标量顶点为 \(-ih_{ab}\)。
混合项在拉氏量中是 \(-h_{hs}hs\bar\ell\ell\)，没有再乘二。
固定外腿的 1PI 图包括两张单标量顶点构成的费米子泡，以及一张双标量顶点构成的闭环接触图。后者只在 \(hs\) 行非零。

### 262.2 手征合并后的 Dirac 迹、PV 与 \(i\) 因子

沿用第 250 节：\(i\Pi\) 为 1PI 插入，逆核为 \(p^2-m_0^2+\Pi\)，度规 \(+---\)，\(\mathrm{tr}\,1=4\)。重定义相位后径向耦合是实标量 Dirac 耦合，两个共轭手征顶点已合并，不能再乘一个“左右手因子二”。

令
\[
D_0=k^2-m^2+i0,\qquad D_1=(k+p)^2-m^2+i0,\qquad t=p^2.
\]
泡图的迹为
\[
\mathrm{tr}[(\slashed k+m)(\slashed k+\slashed p+m)]
=4[k\cdot(k+p)+m^2]
=2(D_0+D_1+4m^2-t).
\]
闭环负号、两个 \(-ig\) 和两个传播子 \(i\) 给整体 \(-g_ag_b\)。用
\(\int_kD_0^{-1}=iq_0A_0(m^2)\)、
\(\int_k(D_0D_1)^{-1}=iq_0B_0(t;m^2,m^2)\)，得到
\[
\boxed{\begin{aligned}
i\Pi_{ab}^{\rm bub}(t)
&=-2iq_0g_ag_b
\left[2A_0(m^2)+(4m^2-t)B_0(t;m^2,m^2)\right],\\
i\Pi_{ab}^{\rm ct\,vertex}
&=-4iq_0m h_{ab}A_0(m^2).
\end{aligned}}
\]
第二行的 ct vertex 在本节指接触顶点，不是 counterterm。
为避免混淆，下文称其为 \(\Pi^{\rm contact}\)；重整化反项另写 \(\delta\mathcal L\)。
\(q_0=(16\pi^2)^{-1}\)，轻子颜色重数为一。一般 Dirac 色重数 \(N_c\) 只需整体乘 \(N_c\)。

这里 \(A_0,B_0\) 本身不再包含 \(i/(16\pi^2)\)。函数参数的记号可对照 [FeynCalc 官方 \(B_0\) 文档](https://feyncalc.github.io/FeynCalcBook/B0.html)；本节实际采用的归一化由上面的积分等式定义，查阅该文档不表示运行了 FeynCalc。

### 262.3 逐味道 UV 极点和有限部分

定义
\[
\ell_m=\ln(m^2/\mu_R^2),\quad
A_0=m^2(\Delta_{\rm UV}+1-\ell_m),\quad
B_0=\Delta_{\rm UV}+\overline B(t),\quad
\overline B(t)=-\ell_m+b(t/m^2).
\]
下文 MS 均指减去 \(\Delta_{\rm UV}=1/\epsilon-\gamma_E+\ln4\pi\) 的 \(\overline{\rm MS}\) 约定，不再另减一遍 \(4\pi,\gamma_E\)。
完整的未减除软函数为泡图加接触图。其 UV 系数是
\[
\boxed{\Pi_{ab}^{\rm UV}(t)
=q_0\Delta_{\rm UV}
\left[2g_ag_b(t-6m^2)-4m^3h_{ab}\right].}
\]
减去此极点后的 MS 软图有限部分为
\[
\boxed{\Pi_{ab}^{\rm fin}(t)=
-2q_0g_ag_b\left[2m^2(1-\ell_m)+(4m^2-t)\overline B(t)\right]
-4q_0m^3h_{ab}(1-\ell_m).}
\]
“MS 有限软图”不表示所有更高维局域边界都已匹配；关于保留完整轻质量的精度见第 262.4、262.7 节。

对 \(c_\ell S_\ell H\) 的具体顶点，每味道三行是
\[
\begin{aligned}
\Pi_{hh,\ell}^{\rm fin}
&=-\frac{2q_0m_\ell^2}{v^2}
\left[2m_\ell^2(1-\ell_\ell)+(4m_\ell^2-t)\overline B_\ell(t)\right],\\
\Pi_{ss,\ell}^{\rm fin}
&=-\frac{2q_0m_\ell^2}{w^2}
\left[2m_\ell^2(1-\ell_\ell)+(4m_\ell^2-t)\overline B_\ell(t)\right],\\
\Pi_{hs,\ell}^{\rm fin}
&=-\frac{2q_0m_\ell^2}{vw}
\left[4m_\ell^2(1-\ell_\ell)+(4m_\ell^2-t)\overline B_\ell(t)\right],
\qquad \ell_\ell=\ln(m_\ell^2/\mu_R^2).
\end{aligned}
\]
混合行的 \(4m^2(1-\ell)\) 与对角行的 \(2m^2(1-\ell)\) 不同，正是接触图所致。总结果为 \(\sum_{\ell=\mu,\tau}\Pi_{ab,\ell}\)，不要求两轻质量或两重质量相等。

### 262.4 Tadpole、有效势和维数八势反项

用与 1PI 拉氏量线性项 \(it_a\) 相反的势导数定义 tadpole：
\[
\mathcal T_a^{V}=\frac{\partial V_1}{\partial\varphi_a}
=4q_0m g_aA_0(m^2),\qquad it_a=-i\mathcal T_a^V.
\]
在常背景上，保留维数五质量函数
\(m(\rho,\sigma)=c\rho\sigma/2,\ \rho=v+h,\sigma=w+s\)，
轻 Dirac 行列式给
\[
V_1^{\rm bare}=q_0m(\rho,\sigma)^4
\left[\Delta_{\rm UV}+\frac32-\ln\frac{m(\rho,\sigma)^2}{\mu_R^2}\right].
\]
减极点后的部分是通常的
\(V_1^{\rm fin}=-q_0m^4[\ln(m^2/\mu_R^2)-3/2]\)。
直接求导可得
\[
\boxed{\Pi_{ab}^{\rm bub}(0)+\Pi_{ab}^{\rm contact}
=-\frac{\partial^2V_1^{\rm bare}}{\partial\varphi_a\partial\varphi_b}.}
\]
链式法则的第二项包含 \(h_{ab}\partial V_1/\partial m\)；只算泡图会漏掉它。Python 和 Mathematica 都从质量函数独立求导，验证了此式及 tadpole 的号。

这里还暴露了截断问题：
\[
m^2=c^2XY,\qquad m^4=c^4X^2Y^2.
\]
因此完整轻质量结果中的势极点为
\[
V_{1,\rm UV}=q_0c^4\Delta_{\rm UV}X^2Y^2,
\qquad
\boxed{\delta\mathcal L_{\rm pot,8}=+q_0c^4\Delta_{\rm UV}X^2Y^2.}
\]
它的质量维数是八，系数为 \(M^{-4}\)，不是此前维数六 Wilson 表中的一个遗漏数值。该反项同时抵消相应 tadpole 和三个质量极点；混合质量极点包含泡图与接触图的共同贡献。

当前计算给出此低能 UV 极点，但没有完成维数八的 UV 硬匹配。若把完整轻质量软图用于超出严格 \(M^{-2}\) 的谱预测，还需同阶局域边界、相关维数七顶点等；不能只设这个有限反项为零就宣布完成全部 \(M^{-4}\) 预测。固定 VEV 的有限 tadpole 调整也须说明方案；本节并未用一个任意数值调整替代它。

### 262.5 导数 UV 反项、EOM 伴随项和硬对数核对

与势极点不同，动量极点本身就在 \(c^2\sim M^{-2}\) 阶。其规范协变局域代表可写为
\[
\mathcal K_\ell=
[D_\mu(S_\ell H)]^\dagger D^\mu(S_\ell H).
\]
两次 \(C_5\) 的轻圈导数发散与其反项分别为
\[
\Delta\mathcal L_{\rm UV,\partial}=+q_0c_\ell^2\Delta_{\rm UV}\mathcal K_\ell,\qquad
\boxed{\delta\mathcal L_{\partial,6}=-q_0c_\ell^2\Delta_{\rm UV}\mathcal K_\ell.}
\]
在径向背景上它等于 \(q_0\Delta_{\rm UV}(\partial m_\ell)^2\) 的正发散；二次变分给 \(2q_0g_ag_b p^2\Delta_{\rm UV}\)，与第 262.3 节相符。

沿用 \(O_J\) 不带 \(i\) 的定义，
\[
\boxed{\mathcal K_\ell=
Y|DH|^2+X|DS|^2+\frac12O_D-\frac{s_\ell}{2}O_J.}
\]
再用第 252 节完整标量 EOM，
\[
Y|DH|^2+X|DS|^2\doteq
-O_D+(f_H+f_S)XY+
\frac12(Y\mathcal F_H+X\mathcal F_S),
\]
便有
\[
\boxed{\delta\mathcal L_{\partial,6}\doteq
a_\ell\Delta_{\rm UV}
\left[\frac12O_D+\frac{s_\ell}{2}O_J
-(f_H+f_S)XY-\frac12(Y\mathcal F_H+X\mathcal F_S)\right],\quad
a_\ell=q_0c_\ell^2.}
\]
势、门户和费米子源伴随项必须与导数反项一起转换。若只从该式抽取 \(O_D\) 一行去减一个尚未作同样场变换的裸 \(hs\) 自能，表面上会遇到错误的号；其余项和非线性场反项正是离壳两点函数基底变换所需。

本节先在完整局域代表上作最小极点减除，再按同一场坐标理解有限软函数。它不在第 260 节的已匹配硬 Wilson 上重新加一份同样反项。

还有三个明确的重质量对数控制。令 \(L_\ell=\ln(M_\ell^2/\mu_R^2)\)，第 252 节的相应硬项为
\[
C_\ell=a_\ell(L_\ell-3/2),\quad
C_{D,\ell}^{\rm NR}=a_\ell(7/6-L_\ell/2),\quad
C_{J,\ell}=-s_\ell a_\ell(L_\ell-2)/2 .
\]
上面反项在 \(Y|DH|^2+X|DS|^2,O_D,O_J\) 上的极点系数为
\((-a_\ell,\ a_\ell/2,\ s_\ell a_\ell/2)\)。
计入两次 \(C_5\) 的维数正则化尺度因子后，本来源的系数运行是极点系数的两倍：
\[
\frac{d}{d\ln\mu_R}(C_\ell,C_{D,\ell}^{\rm NR},C_{J,\ell})
=(-2a_\ell,\ a_\ell,\ s_\ell a_\ell).
\]
三项与硬对数实际一致。这是指定耦合来源的显式对数核对，不是声称本节重新计算了全部 EFT RGE。

### 262.6 \(B_0\) 的解析支、轻阈值和吸收部

直接定义
\[
\overline B(t)=-\int_0^1dx
\ln\frac{m^2-tx(1-x)-i0}{\mu_R^2},\qquad
z=t/m^2,\qquad \overline B=-\ell_m+b(z).
\]
各支为
\[
\boxed{\begin{aligned}
b(z<0)&=2-\beta_E\ln\frac{\beta_E+1}{\beta_E-1},
&\beta_E&=\sqrt{1-4/z}>1,\\
b(0)&=0,\\
b(0<z<4)&=2-2\eta\arctan(1/\eta),
&\eta&=\sqrt{4/z-1},\\
b(4)&=2,\\
b(z>4)&=2-\beta\ln\frac{1+\beta}{1-\beta}+i\pi\beta,
&\beta&=\sqrt{1-4/z}.
\end{aligned}}
\]
阈上正的 \(i\pi\beta\) 来自 \(-i0\)；把普通负实数的主支 \(\log\) 直接代入而不跟踪 \(i0\)，会把吸收部翻号。

由于接触图没有此二粒子支切，
\[
\boxed{\operatorname{Im}\Pi_{ab}(t)=
2\pi q_0g_ag_b\,t\,\beta^3\,\Theta(t-4m^2),\qquad
\operatorname{Disc}\Pi_{ab}=2i\,\operatorname{Im}\Pi_{ab}.}
\]
每味道吸收矩阵都是正半定的外积 \(g_ag_b\)。仅对本 \(C_5\) 子扇区，所有味道的耦合向量平行于 \((w,v)\)，故总吸收矩阵秩最多为一，并有零方向 \((v,-w)\)。普通 quark/electron Yukawa 圈或其他扇区加入后，不再据此宣称完整吸收矩阵秩一。

在本稿 \(+\,\Pi\) 逆核约定下，极点虚部为负：
\[
p_{\rm pole}^2\simeq m_{\rm loc}^2-\Pi(m_{\rm loc}^2)
=M^2-iM\Gamma.
\]
对规范化质量态的实耦合 \(g_i\)，本费米子道满足
\[
\boxed{\Gamma(h_i\to\ell\bar\ell)=
\frac{g_i^2M_i}{8\pi}
\left(1-\frac{4m_\ell^2}{M_i^2}\right)^{3/2}\Theta(M_i-2m_\ell),\qquad
\operatorname{Im}\widetilde\Pi_{ii}(M_i^2)=M_i\Gamma_i.}
\]
这是本单圈/单衰变道的光学定理检查，不是完整标量总宽度。

### 262.7 严格 \(M^{-2}\) 与保留轻质量的软函数

固定 \(v,w\) 和非零外动量时，\(m,g_a,h_{hs}\) 均随 \(c\sim M^{-1}\) 缩放。各项的重质量阶为

| 来源 | 阶数 |
|---|---|
| 泡图 \(g_ag_b\,p^2B_0\) | \(M^{-2}\) |
| 泡图 \(g_ag_b m^2\)、\(g_ag_b A_0\) | \(M^{-4}\)，可含轻对数 |
| 接触图 \(m h_{hs}A_0\) | \(M^{-4}\) |
| 轻 tadpole、\(m^4\) 势及其常数质量曲率 | \(M^{-4}\) |

因此本维数六精度下的固定外动量结果是
\[
\boxed{\begin{aligned}
\Pi_{ab,\ell}^{[M^{-2}],\rm bare}(t)
&=2q_0g_{a\ell}g_{b\ell}\,t
\left[\Delta_{\rm UV}+2-\ln\frac{-t-i0}{\mu_R^2}\right],\\
\Pi_\ell^{[M^{-2}],\rm fin}(t)
&=\frac{a_\ell t}{2}
\left[2-\ln\frac{-t-i0}{\mu_R^2}\right]
\begin{pmatrix}w^2&vw\\vw&v^2\end{pmatrix}.
\end{aligned}}
\]
这一结果和第 260 节硬局域核组合，不需要凭空引入维数八有限边界。

第 262.3 节的精确质量公式可用于展示真实轻阈值和已知软函数的红外行为，但它选择性保留了更高重质量阶。若外动量随 \(m^2\) 一起趋零，固定外动量展开并不一致；近轻阈值应保留完整函数，同时明确未知高维局域项的精度限制。本节没有把这两种近似混成一个“完整 \(M^{-4}\)”预测。

### 262.8 有限动量差和导数：不把轻图再匹配成重 Wilson

定义同一场坐标中的差
\[
\Delta\Pi_{ab}(t)=\Pi_{ab}^{\rm fin}(t)-\Pi_{ab}^{\rm fin}(0).
\]
接触图和 \(A_0\) 完全相消，留下
\[
\boxed{\Delta\Pi_{ab}(t)=
2q_0g_ag_b[-t\ell_m+(t-4m^2)b(t/m^2)].}
\]
常数的维数八势反项在这个差中不出现，但全阶预测仍有其他高维局域来源；不能据此将已知软动量差称为完整高阶极点。

在 \(|t|\ll m^2\) 而不是重阈值展开下，
\[
b(z)=\sum_{n=1}^\infty\frac{(n!)^2}{n(2n+1)!}z^n
=\frac z6+\frac{z^2}{60}+\frac{z^3}{420}+\cdots,
\]
\[
\boxed{\Delta\Pi_{ab}(t)=
2q_0g_ag_b\left[
(-\ell_m-2/3)t+\frac{t^2}{10m^2}+\frac{t^3}{140m^4}
+O(t^4/m^6)\right].}
\]
这里的 \(t^2/m^2\) 是保留轻费米子产生的低动量展开，不是新的 \(1/M_E^2\) 硬 Wilson。因 \(m\propto M_E^{-1}\)，先取 \(t/m^2\to0\) 与先作固定 \(t\) 的重质量展开不对易；不能把这一系数表观上对重尺度不衰减解释为重态不解耦。

供外腿残数使用的导数为
\[
\overline B'(t)=\int_0^1dx\,
\frac{x(1-x)}{m^2-tx(1-x)-i0}
=\frac1{m^2}\frac{2b(z)-z}{z(z-4)},
\]
\[
\boxed{\Pi_{ab}'(t)=
2q_0g_ag_b[\overline B(t)+(t-4m^2)\overline B'(t)].}
\]
在 \(t=0\) 时为 \(2q_0g_ag_b(-\ell_m-2/3)\)。
\(\overline B'\) 在阈值有奇性，但该自能的一阶导数的阈值极限有限：
\(\Pi_{ab}'(4m^2)=2q_0g_ag_b(2-\ell_m)\)。

### 262.9 接入质量态、极点与非正交外腿

一圈软图用树级 \(R_0\) 旋转即可：
\[
\widetilde\Pi_\ell=R_0^T\Pi_\ell R_0,\qquad
\widetilde g_\ell=R_0^Tg_\ell,\qquad
\widetilde h_\ell=R_0^Th_\ell R_0.
\]
第 261 节的有限 \(E\) 再作用到这张一圈图是两圈；不在此重复插入。接触项在旋转后可给对角质量态贡献，因此不能先以“径向对角无接触”删除整张图再旋转。

在严格本阶，径向/质量态核写成
\[
\boxed{\Gamma_c(t)=t\mathbf1-\mathcal M_{\rm loc}^2+
\sum_\ell\Pi_\ell^{[M^{-2}],\rm fin}(t)
+\Pi_{\rm other\,light}^{\,\rm ren}(t),\qquad \det\Gamma_c(t)=0.}
\]
若选择第 262.3 节的完整轻质量函数，则还须把相应高维局域边界及 tadpole 处理明确登记。本节重态的 \(t,z,r\)、第 261 节已经组装的局域势/动能，均不在 \(\Pi_{\rm other\,light}\) 中再添一次。

非简并时，本费米子子扇区给
\[
\delta m_i^2=-\operatorname{Re}\widetilde\Pi_{ii}(m_{i,0}^2),\quad
Z_i=1-\widetilde\Pi'_{ii}(m_{i,0}^2),\quad
(n_i)_j=-\frac{\widetilde\Pi_{ji}(m_{i,0}^2)}
{m_{i,0}^2-m_{j,0}^2}\quad(j\ne i).
\]
不同极点的 \(\Pi_{12}\) 在不同动量取值，外腿不能一般地归结成同一个正交旋转。近简并区须求完整矩阵核，不能使用上面的分母展开；具体混合角重整化方案的背景见 [Denner、Dittmaier、Lang 的原始研究](https://arxiv.org/abs/1808.03466)。

作为明确受限的对数控制，取第 261.7 节零 UV 树门户、固定树参数的比较极限，令
\[
W=(m_{h0}^2+m_{s0}^2)/2=\lambda_Hv^2+\lambda_Sw^2,\quad
\Delta=m_{s0}^2-m_{h0}^2.
\]
第 261.7 节硬局域 \(\mathsf B\) 的本耦合来源满足
\(\partial_{\ln\mu_R}\mathsf B=vw\sum_\ell a_\ell W\)；
本节软图满足
\(\partial_{\ln\mu_R}\Pi_{hs,\ell}(t)=a_\ell vwt\)。
因此对称外腿组合
\[
\frac{\mathsf B-
\tfrac12[\Pi_{hs}(m_{h0}^2)+\Pi_{hs}(m_{s0}^2)]}{\Delta}
\]
中这两个来源的显式尺度对数抵消。程序实际检查该平均；它仅是指定来源与固定树输入的控制，不替代完整运行、源耦合或一个过程定义的物理角。

### 262.10 其余允许轻费米子与仍未计算的部分

第 262.2—262.3 节母式也给出本基准允许的普通 electron/quark Yukawa 圈：
\[
m_f=|Y_f|v/\sqrt2,\quad g_{hf}=m_f/v,\quad g_{sf}=0,\quad h_{ab,f}=0,
\quad N_c=1\ \text{或}\ 3.
\]
在各自轻质量本征基底求和即可。径向基底只有 \(hh\) 泡图，旋转到标量质量态后仍会给混合自能。普通 Yukawa 的一圈阈值或第 261 节源修正再放入这个一圈图属于两圈，本轮只用共同树参数。

这部分的 \(m_f^4\) 是维数四 Higgs 势重整化，其 tadpole 也不是 \(M^{-4}\) 小量；第 262.7 节的阶数表专指由 \(C_5\) 生成的 \(\mu,\tau\) 质量，不能套到全部 SM 费米子。

本节仍未评价轻标量/Goldstone/规范/ghost 圈和有关树 \(C_6\) 的完整二点投影，尚未固定完整物理输入/tadpole 方案。中微子质量若来自额外机制，须使用已明确的模型输入，不能从本轻带电 Dirac 母式推断。两个第 259 节文献印刷式差异也未因本节软图而自动消除。

因此当前完成的是轻费米子子扇区及其严格本阶极点接口；没有声称整个模型的物理极点、总宽度或数值混合角已全部求出。

### 262.11 实际复现、独立积分与双引擎证据

Python 脚本从显式四维 Dirac 矩阵迹和分母恒等式出发，验证 PV 分子、UV/有限组合、质量函数的 CW 链式导数、维数八势 Hessian、规范协变导数反项、EOM 源及硬对数。Gaussian 矩阵元只用整数和整数倍 \(i\)，无近似 Dirac 迹。还检查低动量矩、吸收部的 \(\beta^3\) 和受限对称对数组合。

数值用 \(m^2=\mu_R^2=1\) 的无量纲 \(z\)，不指定物理模型点。Python 以 16384 分段 Simpson、端点四次平滑变换，并在阈值根处分段，直接计算 \(-\int\log|1-zx(1-x)|\) 及其切割区虚部：

| \(z\) | \(\operatorname{Re}b\) | \(\operatorname{Im}b\) |
|---:|---:|---:|
| -2 | -0.281037988903 | 0 |
| -0.5 | -0.079441541680 | 0 |
| 0 | 0 | 0 |
| 1 | 0.186200635766 | 0 |
| 3.9 | 1.547792933637 | 0 |
| 4 | 2 | 0 |
| 5 | 1.569591059036 | 1.404962946208 |
| 10 | 0.401668519244 | 2.433467205584 |

三个导数积分分别在 \(z=-1,1,3.5\) 得
\(0.139182118072,\ 0.209199576156,\ 0.759134334427\)，与解析导数一致。
另用 50 位 Decimal 在 \(t=-1,\mu_R^2=1,m^2=r\) 检查质量趋零；下表均抽去 \(2q_0g_ag_b\)，目标是 \(-2\)：

| \(r\) | 泡图 | 混合泡图加接触图 |
|---:|---:|---:|
| \(10^{-2}\) | -2.076354415077340 | -2.188457818797101 |
| \(10^{-3}\) | -2.007949580394807 | -2.023765090952772 |
| \(10^{-4}\) | -2.000799357415747 | -2.002841425490142 |

偏离目标是保留轻质量产生的高阶余项，不是数值错误。Python 实际摘要为

~~~text
python section262_reproduce.py
RESULT: 62 exact light-fermion checks passed; 8 B0 integrals, 3 derivative integrals and 3 massless-limit cases passed
~~~

本地 Mathematica 14.2.0 独立使用 PauliMatrix/Dirac 矩阵、D、Coefficient、Series 和代数化简复核 25 项；用 WorkingPrecision=40、AccuracyGoal=25、PrecisionGoal=25 的 NIntegrate 再做 \(z=-2,1,3.9,4,5,10\) 六组复核（六次实部积分和两次阈上切割区积分），程序阈值要求误差小于 \(10^{-23}\)，全部通过。它没有读取 Python 结果或加载圈图包。实际摘要为

~~~text
wolframscript -file section262_mathematica.wl
ENGINE 14.2.0 for Microsoft Windows (64-bit) (December 26, 2024)
RESULT: 25 Mathematica symbolic checks passed; 6 high-precision B0 integrals passed
No FeynArts/FeynCalc or other loop package was loaded or run.
~~~

两套检查部分重叠，不把数量相加当作独立全图验证。独立附件与以下嵌入代码逐字一致；原始日志分别为 section262_checks.txt 与 section262_mathematica_checks.txt。

<!-- SECTION262_REPRODUCE_CODE -->

<!-- SECTION262_MATHEMATICA_CODE -->

### 262.12 本轮完成和下一步

**本轮完成**：轻带电费米子 \(hh,hs,ss\) 自能的符号、接触图、UV 与有限部分，真实轻阈值、吸收部和外腿导数已给出，并接入第 261 节极点核。导数反项及其 EOM 源/势伴随项与硬对数一致；完整轻质量的维数八势极点已与严格维数六结果分开。Python 62 项检查、11 次积分、3 组质量极限，以及 Mathematica 25 项检查和 6 次高精度积分实际通过。

**下一步（第 263 节）**：补充轻标量圈及其 tadpole，先建立标量子扇区的一般耦合张量和两点核，再与本节费米子块合并；规范/ghost 圈、树 \(C_6\) 投影和物理输入转换随后按同一方案统一。尚未给数值边界时继续符号计算，不虚构物理谱。

第 66 版作为最新版，第 65 版作为完整备份；第 64 版在确认内容已包含于两份保留文件后从当前工作目录移除。其他审稿文档和资料库不更新。
