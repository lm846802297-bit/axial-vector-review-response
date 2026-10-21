

---

## 第 261 节：破缺相的真空、动能、局域质量与混合角，以及极点计算接口（第 65 版新增）

> **版本和范围（2026-10-20）**：以第 64 版第 260 节的最终条件性向量为输入，本节追加到原文件之后。采用同一未破缺相 EFT，保留轻 \(H,S,A'\)；先作 CP 偶径向二次作用量的符号转换，不再计算或叠加重态匹配图。所有 \(k,C,f\) 都指第 260 节完成换基后的系数。
>
> **本节实际完成**：带六标量势的真空条件和 Hessian，导数算符产生的完整径向动能矩阵，规范化后的局域质量矩阵、混合角及源耦合；验证规范 EOM 的 VEV 坐标变换和两点高导数消去保持相应二次核一致。另给 \(\lambda_{P,U}=0\) 时逐味道的显式混合矩阵元。
>
> **本节没有把局域特征值称为完整一圈极点**。轻场自能、tadpole 重整化和物理输入转换仍需补入；本节给出它们应进入的位置和符号。Python 的 59 项精确检查、3 组独立对角化和 3 组截断余项缩放，以及本地 Mathematica 14.2 的 25 项独立符号检查已实际执行。数值组是代数测试，不是模型基准点。

### 261.1 破缺背景和有效势的符号

在 CP 偶、无外规范场和费米子背景的方向上写
\[
H=\frac1{\sqrt2}\begin{pmatrix}0\\v+h\end{pmatrix},
\qquad S=\frac{w+s}{\sqrt2},\qquad
X=\frac{(v+h)^2}{2},\quad Y=\frac{(w+s)^2}{2}.
\]
本节假定双破缺支 \(v,w>0\)。\(w\) 表示单态 VEV，避免与第 250—260 节 \(v_\ell=|\lambda_\ell|^2\) 混淆。\(v,w\) 属于第 260 节选定的 EFT 场坐标，已经实施有限场归一化和标量 EOM 换基；不再给 \(h,s\) 的动能额外加一次 \(z_H,z_S\)。

第 260 节的 \(k\) 是 \(\Delta\mathcal L\) 系数。定义
\[
\begin{gathered}
\bar\mu_H^2=\mu_H^2+k_X,\quad
\bar\mu_S^2=\mu_S^2+k_Y,\quad
\Lambda_H=\lambda_H-k_{XX},\quad
\Lambda_S=\lambda_S-k_{YY},\quad
\Lambda_P=\lambda_P-k_{XY},\\
\eta_{30}=-k_{XXX},\quad \eta_{03}=-k_{YYY},\quad
\eta_{21}=-k_{XXY},\quad \eta_{12}=-k_{XYY}.
\end{gathered}
\]
于是本节使用的局域势是
\[
\boxed{\begin{aligned}
V_{\rm loc}(X,Y)={}&-\bar\mu_H^2X-\bar\mu_S^2Y+
\Lambda_HX^2+\Lambda_SY^2+\Lambda_PXY\\
&+\eta_{30}X^3+\eta_{03}Y^3+\eta_{21}X^2Y+\eta_{12}XY^2.
\end{aligned}}
\]
这不是包含所有轻场 Coleman–Weinberg 项的完整一圈有效势；相应非局域圈图在后面的极点计算中加入。所有匹配增量为一圈，\(\eta\) 和导数 Wilson 为一圈 \(M^{-2}\)。乘积保留至这一精度；例如 \(\eta\,k\) 或两个一圈动能增量不作为两圈预测使用。

### 261.2 真空条件、两种输入方式和 Goldstone 检查

令 \(x_0=v^2/2,\ y_0=w^2/2\)，\(V_X=\partial V_{\rm loc}/\partial X\)。径向 tadpole 为
\[
T_h=v\,V_X(x_0,y_0),\qquad T_s=w\,V_Y(x_0,y_0).
\]
在双破缺支取局域驻点 \(T_h=T_s=0\)，得到
\[
\boxed{\begin{aligned}
\bar\mu_H^2={}&\Lambda_Hv^2+\frac{\Lambda_Pw^2}{2}
+\frac34\eta_{30}v^4+\frac12\eta_{21}v^2w^2+\frac14\eta_{12}w^4,\\
\bar\mu_S^2={}&\Lambda_Sw^2+\frac{\Lambda_Pv^2}{2}
+\frac34\eta_{03}w^4+\frac14\eta_{21}v^4+\frac12\eta_{12}v^2w^2.
\end{aligned}}
\]
它们可以作为以 \(v,w\) 为输入、反解两个质量参数的条件。此时 \(v\) 暂不自动等同于由 \(G_F\) 提取的物理输入；后者需要轻场、四费米子及带电流算符的输入参数转换。

若选择固定 UV 势参数、从原树真空 \((x_0^{(0)},y_0^{(0)})\) 求阈值引起的 VEV 位移，定义
\[
\mathcal P(X,Y)=k_X X+k_Y Y+k_{XX}X^2+k_{YY}Y^2+k_{XY}XY+
k_{XXX}X^3+k_{YYY}Y^3+k_{XXY}X^2Y+k_{XYY}XY^2.
\]
这里前两项的 \(k_X X,k_Y Y\) 是系数乘单项；下标 \(XX\) 是另一系数。因 \(\delta V=-\mathcal P\)，线性化驻点给
\[
\begin{pmatrix}2\lambda_H&\lambda_P\\\lambda_P&2\lambda_S\end{pmatrix}
\begin{pmatrix}\delta x\\\delta y\end{pmatrix}
=\begin{pmatrix}\mathcal P_X\\\mathcal P_Y\end{pmatrix}_{0},
\]
\[
\boxed{\delta x=\frac{2\lambda_S\mathcal P_X-\lambda_P\mathcal P_Y}
{4\lambda_H\lambda_S-\lambda_P^2},\qquad
\delta y=\frac{2\lambda_H\mathcal P_Y-\lambda_P\mathcal P_X}
{4\lambda_H\lambda_S-\lambda_P^2},\quad
\delta v=\delta x/v_0,\quad\delta w=\delta y/w_0.}
\]
该展开需要位移足够小及分母不接近零。阈值中的 \(t_\phi\sim q_0M^2\) 不保证相对电弱尺度很小；不能只因它带一圈因子就默认固定 UV 参数下的 VEV 位移可微扰。给定 VEV、由前两式解质量参数与固定 UV 参数求位移是两种输入方式，不在同一次计算中同时加位移。

暂恢复 \(H^0=(v+h+i\chi)/\sqrt2,\ S=(w+s+ia)/\sqrt2\)，势的两条相位质量为
\[
\left.\frac{\partial^2V}{\partial\chi^2}\right|_0=V_X,\qquad
\left.\frac{\partial^2V}{\partial a^2}\right|_0=V_Y.
\]
它们在上述驻点为零，且无 CP 偶—奇势混合。这是未加规范固定项的 Goldstone 势检查；规范固定产生的质量和规范—Goldstone 混合另由相应规范二次作用量处理。

### 261.3 势的 Hessian 与 tadpole 项

在任意展开点，径向 Hessian 为
\[
\mathcal H_{hh}=V_X+v^2V_{XX},\quad
\mathcal H_{ss}=V_Y+w^2V_{YY},\quad
\mathcal H_{hs}=vwV_{XY}.
\]
所以未消 tadpole 时，对角元还有 \(T_h/v,T_s/w\)，不能直接删掉。在第 261.2 节的局域驻点：
\[
\boxed{\mathcal H=
\begin{pmatrix}
v^2(2\Lambda_H+3\eta_{30}v^2+\eta_{21}w^2)&
vw(\Lambda_P+\eta_{21}v^2+\eta_{12}w^2)\\
vw(\Lambda_P+\eta_{21}v^2+\eta_{12}w^2)&
w^2(2\Lambda_S+3\eta_{03}w^2+\eta_{12}v^2)
\end{pmatrix}.}
\]
这只是势的曲率矩阵，须与动能一起处理。局部极小值还要求径向 Hessian 正定；单凭解出 tadpole 方程不证明真空稳定。六场截断势在场值接近重尺度时不能用来证明全局稳定性，应用范围仍为第 260 节的重质量展开区间。

### 261.4 径向动能矩阵：包括 \(Q_{HD}\) 的因子

用最终系数记
\[
\Delta\mathcal L_{\partial}=
C_X\mathcal Q_X+C_Y\mathcal Q_Y+C_{HD}\mathcal Q_{HD}
+C_D O_D+C_J O_J,
\]
\[
\mathcal Q_X=(\partial X)^2,\quad
\mathcal Q_Y=(\partial Y)^2,\quad
\mathcal Q_{HD}=|H^\dagger DH|^2,\quad O_D=\partial X\cdot\partial Y.
\]
在径向、零规范背景下
\[
\mathcal Q_X=(v+h)^2(\partial h)^2,\quad
\mathcal Q_Y=(w+s)^2(\partial s)^2,\quad
\mathcal Q_{HD}=\frac{(v+h)^2}{4}(\partial h)^2,\quad
O_D=(v+h)(w+s)\partial h\cdot\partial s.
\]
两个不带 \(i\) 的反对称电流在此径向背景为零，故 \(O_J\) 不直接进入径向二次核；场强算符也不在零规范背景产生径向二次项。它们仍会改变规范二次作用量与相互作用，不能从完整 EFT 中删除。

令 \(\varphi=(h,s)^T\)，
\[
\mathcal L_{\rm rad}^{(2)}=\frac12\partial\varphi^TK\partial\varphi
-\frac12\varphi^T\mathcal H\varphi,\qquad
K=\mathbf1+E,\qquad
E=\begin{pmatrix}\epsilon_h&\epsilon_{hs}\\\epsilon_{hs}&\epsilon_s\end{pmatrix},
\]
\[
\boxed{\epsilon_h=v^2(2C_X+C_{HD}/2),\quad
\epsilon_s=2w^2C_Y,\quad \epsilon_{hs}=vwC_D.}
\]
这里混合二次项为 \(K_{hs}\partial h\partial s\)，不再乘二。

代入第 260.5 节的最终系数，还得到便于检查的简式
\[
\boxed{\begin{aligned}
\epsilon_h&=v^2(5B_H/12-3A_W/2),\\
\epsilon_s&=w^2(7B_S/6-6A_S),\\
\epsilon_{hs}&=vw\sum_\ell\frac{q_0u_\ell v_\ell}{M_\ell^2}(7/6-L_\ell/2).
\end{aligned}}
\]
\(A_H\) 从径向 \(\epsilon_h\) 中恰好抵消。这与 \(j_H^2=4Q_{HD}-Q_X\) 在该背景为零一致。出现的 \(A_W,A_S\) 则还伴随势和 VEV 坐标变换，不能单独解释成新的物理标量质量效应。

### 261.5 一圈规范化和局域质量矩阵

取对称规范化
\[
\varphi=(\mathbf1-E/2)\varphi_c+O(E^2).
\]
把 Hessian 分成树级与匹配增量
\[
\mathcal H=\mathcal H_0+\delta\mathcal H,\qquad
\mathcal H_0=\begin{pmatrix}A_0&B_0\\B_0&C_0\end{pmatrix}
=\begin{pmatrix}2\lambda_Hv^2&\lambda_Pvw\\
\lambda_Pvw&2\lambda_Sw^2\end{pmatrix}.
\]
在以 \(v,w\) 为输入的局域 tadpole 方案中，规范化后
\[
\boxed{\mathcal M_{\rm loc}^2=\mathcal H_0+\delta\mathcal H
-\frac12(E\mathcal H_0+\mathcal H_0E)
\equiv\begin{pmatrix}\mathsf A&\mathsf B\\\mathsf B&\mathsf C\end{pmatrix}.}
\]
具体为
\[
\begin{aligned}
\mathsf A&=\mathcal H_{hh}-\epsilon_h A_0-\epsilon_{hs}B_0,\\
\mathsf C&=\mathcal H_{ss}-\epsilon_s C_0-\epsilon_{hs}B_0,\\
\mathsf B&=\mathcal H_{hs}
-\tfrac12(\epsilon_h+\epsilon_s)B_0
-\tfrac12\epsilon_{hs}(A_0+C_0).
\end{aligned}
\]
\(E\delta\mathcal H\) 已是两圈，未保留。若采用固定 UV 参数方式，应先将 VEV 位移贡献加入 \(\delta\mathcal H\)，而不是把这里的固定 VEV 结果再乘一个不相关的真空修正。

两个直接基底不变量是
\[
\operatorname{tr}\mathcal M_{\rm loc}^2=
\operatorname{tr}\mathcal H-\operatorname{tr}(E\mathcal H_0),\qquad
\det\mathcal M_{\rm loc}^2=
\frac{\det\mathcal H}{\det K}\bigg|_{\text{一圈}}.
\]
脚本还检查
\(\det[p^2K-\mathcal H]/\det K=\det[p^2\mathbf1-\mathcal M_{\rm loc}^2]\)
到一圈精度。动能矩阵与 Hessian 一般不对易；不能只把两个对角质量各除以各自动能系数而漏掉混合反对易子。

### 261.6 本征值、混合角和近简并处理

约定
\[
\varphi_c=R(\theta_{\rm loc})
\begin{pmatrix}h_1\\h_2\end{pmatrix},\qquad
R(\theta)=\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix},
\qquad m_{1,\rm loc}^2\le m_{2,\rm loc}^2 .
\]
则
\[
\boxed{\begin{aligned}
\Delta_{\rm loc}&=\sqrt{(\mathsf C-\mathsf A)^2+4\mathsf B^2},\\
m_{1,2,\rm loc}^2&=\tfrac12(\mathsf A+\mathsf C\mp\Delta_{\rm loc}),\\
\theta_{\rm loc}&=\tfrac12\operatorname{atan2}(2\mathsf B,\mathsf C-\mathsf A).
\end{aligned}}
\]
此约定在 \(\mathsf B=0,\mathsf A<\mathsf C\) 时取 \(\theta=0\)，轻态沿 Higgs 径向。若质量排序反过来，轻态标签也应相应改变；不能同时固定“态 1 总是 Higgs”与“态 1 总是较轻”。

非简并时令 \(c_0=\cos\theta_0,s_0=\sin\theta_0\)，
\(\delta\mathcal M^2=\begin{pmatrix}\delta A&\delta B\\\delta B&\delta C\end{pmatrix}\)，有
\[
\begin{aligned}
\delta m_1^2&=c_0^2\delta A+s_0^2\delta C-2c_0s_0\delta B,\\
\delta m_2^2&=s_0^2\delta A+c_0^2\delta C+2c_0s_0\delta B,\\
\delta\theta&=\frac{(C_0-A_0)\delta B-B_0(\delta C-\delta A)}
{(C_0-A_0)^2+4B_0^2}
=\frac{(R_0^T\delta\mathcal M^2R_0)_{12}}{m_{2,0}^2-m_{1,0}^2}.
\end{aligned}
\]
在近简并区，最后这个展开不稳定，应直接对角化该阶二次矩阵。对角化截断矩阵保留了简并子空间中的首阶混合，但根式内部由此出现的高次项不是完整两圈结果；若劈裂小于被遗漏项，混合角的精度也无法由本阶保证。

对正定 \(K\)，还有不依赖选择哪种规范化矩阵的广义本征值形式。令
\[
d_K=K_{hh}K_{ss}-K_{hs}^2,\quad
\tau=K_{ss}\mathcal H_{hh}+K_{hh}\mathcal H_{ss}-2K_{hs}\mathcal H_{hs},
\]
则
\[
\det(p^2K-\mathcal H)=d_K(p^2)^2-\tau p^2+\det\mathcal H,\qquad
m_\pm^2=\frac{\tau\pm\sqrt{\tau^2-4d_K\det\mathcal H}}{2d_K}.
\]
这是给定截断二次作用量的精确代数解；用于严格一圈预测时按前述精度解释。程序用此式、对称 \(K^{-1/2}\)、Cholesky 规范化三条路线比较，不把不同规范化产生的中间角度误认为不同质量。

### 261.7 零 UV 树门户下的显式逐味道混合

现在额外选定 \(\lambda_{P,U}=0\)，但保持有限硬门户阈值。这是一个明确的边界条件，不能与“匹配后 \(\Lambda_P=0\)”混为一谈。树 tadpole 给 \(\mu_H^2=\lambda_Hv^2,\ \mu_S^2=\lambda_Sw^2\)，在一圈系数中可用这些树关系。

第 261.5 节的非对角元成为
\[
\begin{aligned}
\mathsf B\big|_{\lambda_{P,U}=0}
&=-vw\left[
k_{XY}+k_{XXY}v^2+k_{XYY}w^2+
C_D(\lambda_Hv^2+\lambda_Sw^2)\right]\\
&=-vw\left[
b+(C+C_D)(\lambda_Hv^2+\lambda_Sw^2)
+D_{XXY}v^2+D_{XYY}w^2\right].
\end{aligned}
\]
其中 \(C=\sum_\ell a_\ell(L_\ell-3/2)\) 是第 252 节混合四场系数，不是质量矩阵元 \(\mathsf C\)。利用
\[
C+C_D=\sum_\ell a_\ell(L_\ell/2-1/3),\qquad
a_\ell=q_0u_\ell v_\ell/M_\ell^2,
\]
得到本轮可直接使用的逐味道结果：
\[
\boxed{\mathsf B\big|_{\lambda_{P,U}=0}
=-q_0vw\sum_{\ell=\mu,\tau}u_\ell v_\ell
\left[
2+\frac{(L_\ell/2-1/3)(\lambda_Hv^2+\lambda_Sw^2)
-u_\ell v^2-v_\ell w^2}{M_\ell^2}
\right].}
\]
它含一圈零阶门户阈值和一圈 \(M^{-2}\) 修正，尚不含轻圈的动量依赖混合。这里 \(v_\ell w^2\) 中第一个 \(v_\ell\) 是 Yukawa 模平方。标量 \(p^4\) 的 EOM 在 \(\lambda_P=0\) 时只影响各自对角方向，规范 EOM 伴随项在此非对角元也不另添一份。

在 \(C_0>A_0\)、远离简并且 \(|\mathsf B|\ll C_0-A_0\) 时，
\[
\theta_{\rm loc}=
\frac{\mathsf B}{2\lambda_Sw^2-2\lambda_Hv^2}+O(q_0^2).
\]
这是上述约定的局域角，不能直接拿去替代完整一圈物理角。若施加的是 \(\Lambda_P=0\) 的 EFT 边界，维数四非对角项被调去，但
\[
\mathsf B\big|_{\Lambda_P=0}
=-vw\left[k_{XXY}v^2+k_{XYY}w^2+
C_D(\lambda_Hv^2+\lambda_Sw^2)\right]
\]
一般仍不为零。这也说明“零门户”须说明施加在哪一侧、哪一阶和哪一个参数上。

### 261.8 两项基底一致性验证：规范 EOM 与 \(p^4\)

**规范 EOM 的径向坐标。** 第 260 节纯标量规范像为
\[
A_Hj_H^2+A_Sj_S^2+A_{HS}j_Hj_S+A_W\sum_a(j_H^a)^2 .
\]
原电流在纯径向零规范背景均为零。把 \(R_H,R_S\) 再用标量 EOM 消去之后，出现的径向动能和势变化须对应场坐标变换
\[
H_{\rm before}=H_{\rm after}-\frac{A_W}{2}XH_{\rm after},\qquad
S_{\rm before}=S_{\rm after}-2A_S Y S_{\rm after}.
\]
写 \(\rho=v+h,\sigma=w+s\)：
\[
\rho_{\rm before}=\rho_{\rm after}-\frac{A_W}{4}\rho_{\rm after}^3,\qquad
\sigma_{\rm before}=\sigma_{\rm after}-A_S\sigma_{\rm after}^3.
\]
故在同一固定原始真空上
\[
v_{\rm after}=v_{\rm before}+\frac{A_W}{4}v_{\rm before}^3,\qquad
w_{\rm after}=w_{\rm before}+A_Sw_{\rm before}^3.
\]
势的坐标变化与
\(\delta K_{hh}=-3A_Wv^2/2,\ \delta K_{ss}=-6A_Sw^2\)
一起使用，规范化后的径向 Hessian 回到变换前值。脚本以一般 \(\lambda_H,\lambda_S,\lambda_P\) 先求变换后 tadpole、再在位移后的 VEV 评价 Hessian，三个独立矩阵元均验证一致。

因此在比较 Green 代表与 EOM 代表时，不能保持两个代表的 VEV 数值不变却声称比较的是同一物理输入。这一检查不删除第 260 节的规范像，只固定其正确使用方式。

**标量 \(p^4\) 的独立检查。** 在树真空令实径向树 Hessian 为 \(M_0\)（本段 \(M_0\) 本身就是质量平方矩阵），\(r=\mathrm{diag}(r_H,r_S)\)。原二次核为
\[
\Gamma_{\rm high}(p^2)=p^2\mathbf1-M_0+r(p^2)^2.
\]
第 250 节场重定义在线性阶给
\[
F(p^2)=\mathbf1-\tfrac12r(p^2\mathbf1+M_0),\qquad
F^T\Gamma_{\rm high}F
=p^2\mathbf1-M_0+M_0rM_0+O(r^2).
\]
所以等价局域质量修正是
\[
\boxed{\delta M_{\rm EOM}=-M_0rM_0.}
\]
同一结果也由
\(\delta V=-\tfrac12\sum_i r_i(\partial V_0/\partial\rho_i)^2\)
在树驻点求 Hessian 得到。程序验证了 \(r\) 与 \(M_0\) 不对易时的三个矩阵元，未依赖对角假设。本节已使用 EOM 后的 \(k\)，不能再给最终核加一份 \(r p^4\)。被截断高导数多项式在重尺度附近的额外根不属于本低能谱的预测。

### 261.9 源耦合随场变换一起转换

对第 260 节允许的可重整化轻 SM Yukawa 源，
\[
\mathcal L_Y+\Delta\mathcal L_{\rm src}
\supset-Y_f[1-f_{H0}-f_{HX}X-f_{HY}Y]\bar F H f+\mathrm{h.c.}
\]
（上型使用 \(\widetilde H\)，径向结果相同）。在同一 EFT VEV 上
\[
\begin{aligned}
m_f&=\frac{Y_fv}{\sqrt2}
\left(1-f_{H0}-\frac12f_{HX}v^2-\frac12f_{HY}w^2\right),\\
g_{hf}&=\frac{Y_f}{\sqrt2}
\left(1-f_{H0}-\frac32f_{HX}v^2-\frac12f_{HY}w^2\right),\\
g_{sf}&=-\frac{Y_f}{\sqrt2}f_{HY}vw .
\end{aligned}
\]
最终局域标量耦合向量为
\[
(g_{1f},g_{2f})=(g_{hf},g_{sf})(\mathbf1-E/2)R(\theta_{\rm loc})
\]
并保持一圈截断。因直接 \(s\) 源和非正交规范化存在，所有耦合通常不能仅写成同一个 \(\cos\theta,\sin\theta\) 倍数。

例如原 \(h\) 方向投影到态 1 的系数是
\[
(1-\epsilon_h/2)\cos\theta+\epsilon_{hs}\sin\theta/2,
\]
原 \(s\) 方向则是
\[
-(1-\epsilon_s/2)\sin\theta-\epsilon_{hs}\cos\theta/2.
\]
不能把质量矩阵换到新场后仍沿用旧场的源系数。

对由 \(C_{5,\ell}\) 生成的 \(\mu,\tau\) 质量，当前局域项给
\(m_\ell=C_{5,\ell}vw/2\)，可用轻场相位将物理质量取正。形式上的径向顶点为 \(m_\ell/v,m_\ell/w\)。但 \(C_5\sim M^{-1}\) 乘本节 \(\epsilon\sim M^{-2}\) 已为 \(M^{-3}\)；若展示这部分相对修正，就必须同时计算尚未纳入的维数七直接算符和源。当前严格 \(M^{-2}\) 账本不把它冒充完整的 \(\mu,\tau\) 高阶 Higgs 耦合预测。

### 261.10 从局域参数到物理极点：还应计算什么

完成重态硬匹配与本节转换后，规范化径向逆传播子应写为
\[
\boxed{\Gamma_c(p^2)=p^2\mathbf1-\mathcal M_{\rm loc}^2+
\widehat\Pi_{\rm light}^{\,\rm ren}(p^2),\qquad
\det\Gamma_c(p_{\rm pole}^2)=0.}
\]
这里沿用本稿 \(+\,\Pi\) 的逆核符号。轻场项含选定方案下的轻圈、参数和场反项以及一致的 tadpole 处理；它不能再包含已经吸收到 \(k,C,z\) 的重态硬副本。

完整一圈 \(M^{-2}\) 极点分析仍需要：普通轻标量/规范/SM 费米子圈，两次树 \(C_5\) 的轻图，以及会贡献该过程的单次树 \(C_6\) 插入。已有一圈 Wilson 插入再做一圈通常是两圈，不混入当前精度。第 252、257、259 节的软减除保证硬 Wilson 局域，但不代表那些轻图在 EFT 物理振幅中消失。

在非简并、可用实部质量的近似中，令
\(\widetilde\Pi=R_0^T\widehat\Pi_{\rm light}^{\rm ren}R_0\)，则
\[
m_{i,\rm pole}^2=m_{i,\rm loc}^2-
\operatorname{Re}\widetilde\Pi_{ii}(m_{i,0}^2)+O(q_0^2).
\]
相应一阶极点方向和对角残数为
\[
n_i=e_i-\sum_{j\ne i}
\frac{\widetilde\Pi_{ji}(m_{i,0}^2)}
{m_{i,0}^2-m_{j,0}^2}e_j,\qquad
Z_i=1-\widetilde\Pi'_{ii}(m_{i,0}^2)+O(q_0^2).
\]
两种极点在不同动量评价自能，因此一般不能用一个常数正交角同时表示全部外腿修正。存在宽度或近简并时，应保留完整复矩阵核并求复极点/残数；上面的非简并分母公式不适用。

局域角的定义、输入参数和 tadpole 方案须同时说明；物理可观测量还包含顶角和外腿。相关方案问题可参见 [Denner、Dittmaier、Lang 的原始论文《Renormalization of mixing angles》](https://arxiv.org/abs/1808.03466)。这里仅引用其关于混合角重整化方案的研究背景，未运行其程序，也没有用该论文替本稿的新增 Wilson 系数作验证。

### 261.11 实际符号与数值检查

section261_reproduce.py 使用标准库 Fraction 稀疏多项式。从 \(V(X,Y)\) 求导并代入背景，检查 tadpole、Goldstone、Hessian；从原导数单项抽取动能；对一般非对易矩阵验证规范化和特征多项式；再检查 VEV 坐标变化、高导数核、普通 Yukawa 源及零 UV 门户的逐味道结果。

三个无量纲代数控制点采用下列矩阵，不是选定的物理模型参数：

| 控制 | \(K\) | \(\mathcal H\) |
|---|---|---|
| 非简并 | \(\begin{pmatrix}1.02&0.01\\0.01&0.97\end{pmatrix}\) | \(\begin{pmatrix}4&0.3\\0.3&9\end{pmatrix}\) |
| 近简并 | \(\begin{pmatrix}1.001&0.0004\\0.0004&0.999\end{pmatrix}\) | \(\begin{pmatrix}4&0.0003\\0.0003&4.0001\end{pmatrix}\) |
| 对角 | \(\mathrm{diag}(1.03,0.98)\) | \(\mathrm{diag}(4,9)\) |

对称平方根、Cholesky 和广义特征方程三路所得质量平方一致：

| 控制 | \(m_1^2\) | \(m_2^2\) | 对称规范化的 \(\theta\)，弧度 |
|---|---:|---:|---:|
| 非简并 | 3.908754881125 | 9.286433636008 | 0.043869347012 |
| 近简并 | 3.995800983474 | 4.004308156653 | -0.155299762559 |
| 对角 | 3.883495145631 | 9.183673469388 | 0 |

另设 \(K=\mathbf1+\varepsilon E,\ \mathcal H=H_0+\varepsilon\delta H\)，用脚本列出的固定测试矩阵比较精确规范化与一阶反对易子式。最大质量平方差为

| \(\varepsilon\) | 最大差 | 最大差除以 \(\varepsilon^2\) |
|---:|---:|---:|
| \(10^{-2}\) | \(2.267201412209\times10^{-5}\) | 0.226720141 |
| \(10^{-3}\) | \(2.267329151096\times10^{-7}\) | 0.226732915 |
| \(10^{-4}\) | \(2.267343646167\times10^{-9}\) | 0.226734365 |

这验证的是预期的二阶截断余项；本节没有新增数值圈积分。实际摘要如下：

~~~text
python section261_reproduce.py
RESULT: 59 exact broken-phase checks passed; 3 independent diagonalization cases and 3 truncation-scaling cases passed
Light-field pole self-energies have not been evaluated in this section.
No FeynArts/FeynCalc, Matchete, matchmakereft, or external diagram generator was run.
~~~

独立附件与以下嵌入源码相同，完整日志为 section261_checks.txt。

<!-- SECTION261_REPRODUCE_CODE -->

**本地 Mathematica 的独立执行。** 用户授权使用本地 Mathematica 后，本轮实际调用 WolframScript 和已安装的 Wolfram 内核 14.2.0，版本输出为 Microsoft Windows 64-bit，December 26, 2024。附带的 section261_mathematica.wl 独立使用 D、Series、Det 和矩阵乘法重建上述关键公式，不调用 Python，也不读取 Python 的检查结果。

实际命令和结果：

~~~text
wolframscript -file section261_mathematica.wl
ENGINE 14.2.0 for Microsoft Windows (64-bit) (December 26, 2024)
RESULT: 25 Mathematica symbolic checks passed
Scope: independent symbolic differentiation and matrix algebra; no loop diagram package was run.
~~~

25 项覆盖 tadpole、六场 Hessian、Goldstone、径向动能、非对易规范化、广义特征多项式、VEV 坐标变换、高导数场变换、源及零 UV 门户混合式。它们与 Python 检查有重叠，不把两个引擎的项数之和说成互不相关的物理验证。完整原始输出是 section261_mathematica_checks.txt。成功调用前的受限环境曾报配置/许可访问错误；在正常本机环境调用后成功，不能据初次错误断言用户未激活 Mathematica。

本轮确实运行了 Mathematica 内核，仍未运行 FeynArts/FeynCalc、Matchete 或 matchmakereft。其完整独立源码也嵌入如下：

<!-- SECTION261_MATHEMATICA_CODE -->

### 261.12 本轮完成与下一步

**本轮完成**：第 260 节作用量已转换成破缺相的局域真空、动能、质量及源耦合；给出一般混合角与近简并处理，以及 \(\lambda_{P,U}=0\) 的显式逐味道混合矩阵元。规范 EOM 的 VEV 位移和标量 \(p^4\) 消去已分别验证。Python 的 59 项精确检查、3 组独立对角化、3 组截断缩放和 Mathematica 的 25 项独立符号检查实际通过。

**下一步（第 262 节）**：先计算破缺相两次树 \(C_5\) 所产生的轻带电费米子 \(\Pi_{hh},\Pi_{hs},\Pi_{ss}(p^2)\)，保留质量阈值、UV 极点与有限动量依赖，和已有硬局域二次核组成一致的极点方程；再按明确的轻场/tadpole/输入方案补其他极点贡献。没有模型边界数值时，继续给符号函数，不将本节代数控制点解释为物理谱。

本轮最新版为第 65 版，当前桌面工作目录中已有的第 64 版作备份，主文档在同一目录；复现附件放在“计算输出”中。第 53 版内容的完整字节前缀已按原哈希验证保留；本轮不改写既有主文档、其他审稿文档或资料库。
