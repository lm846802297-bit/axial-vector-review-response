from pathlib import Path
import re, json, math, hashlib
ROOT=Path(__file__).resolve().parents[1]
src=next((ROOT/'审稿意见-gpt').glob('审稿意见分析v5.6*.md'))
s=src.read_text(encoding='utf-8')
changes=[]
def once(old,new,label):
 global s
 assert s.count(old)==1,(label,s.count(old))
 s=s.replace(old,new); changes.append(label)
def section(start,end,body,label):
 global s
 assert s.count(start)==1,(label,start)
 a=s.index(start); b=s.index(end,a+len(start))
 s=s[:a]+body.strip()+'\n\n'+s[b:]; changes.append(label)

once('- **中微子结构：** 当前 v6 最小场内容可能导致 PMNS 质量矩阵出现受对称性限制的分块结构。是否能与振荡数据兼容，需要从允许算符和质量矩阵正式判定；额外标量或右手中微子只能作为候选扩展，不能在计算前视为已解决方案。',
 r'- **中微子结构：** 在当前存档稿 v6 的荷分配、仅有带新规范荷的 $S$ 获得 VEV、无额外破缺结构的假设下，残余 $Z_2$ 强制电子味与 $\mu,\tau$ 味分块，不能复现观测 PMNS。第 4 章给出允许算符和质量矩阵的条件性解析证明；候选扩展的质量机制、拟合与关联约束仍待完成。','PMNS front status')
s=s.replace('PMNS 的完整结构判断或拟合','候选扩展的 PMNS 质量矩阵、拟合及关联约束')
s=s.replace('问题、问题或建议','问题、要求或建议')
s=s.replace('`M_E,M_L` 等实际独立质量',r'$M_{E_\mu},M_{E_\tau}$ 等实际独立质量')
section('##### 2.1.4.5 ','### 2.1.5 ',r'''
##### 2.1.4.5 近简并的物理含义：从小分母到可测信号

混合前场 $h,s$ 的质量平方矩阵由对角元 $a,b$ 和非对角元 $\Delta=\lambda_{HS}vv_S$ 决定。$\lambda_{HS}$ 无量纲；$\Delta$ 与非对角自能 $\widehat\Pi_{hs}(p^2)$ 均有质量平方量纲，后者还依赖外动量与重整化条件。三者不能互相替代。

在统一旋转 $h_1=c_\theta h-s_\theta s$、$h_2=s_\theta h+c_\theta s$ 下，小角展开由 $\lvert\Delta/(b-a)\rvert$ 控制。靠近简并时失效的是展开，真实角度并不发散。$a=b,\Delta\ne0$ 时两态等权混合；$a=b,\Delta=0$ 时质量矩阵不能唯一选定基底。完整推导和分支算法在本专题工作 E，附录 F 只作独立数值验证。

实验约 125 GeV 的对象是物理 Higgs 候选态。混合不可忽略时，应固定或拟合物理 $m_1$，再确定对角元；不能直接把未混合 $\sqrt a$ 当作测量值。$h_1$ 按场成分标记，不默认比 $h_2$ 轻。

审稿人说的 resonance 首先是对近简并可能增强混合的担忧；这本身不证明截面出现可辨认新峰，更不直接给出排除带。实验测量事件率、线形、总宽度与末态。两态的 SM 耦合可重新分配；即使角度小，直接 Yukawa 或新衰变也可能重要。

计算精度依次为：小角展开及误差；精确实矩阵；统一方案的自能、反项与极点；必要时共同初末态的矩阵传播与相干振幅。比较质量差与宽度，或质量平方差与自能，不可跨量纲比较。探测器分辨率随后进入实验重建；无法分辨双峰不自动意味着量子振幅必须相干。

完整回答要顺着“允许顶角与门户边界—物理谱—衰变与产生—实验比较—低能省略标量的误差”执行。下面先拆解原文，再逐项给出方法；不能从 portal 小直接跳到全部标量效应可忽略。
''','consolidate mixing concept')
section('#### 2.1.7.4 ','#### 2.1.7.5 ',r'''
#### 2.1.7.4 质量矩阵与近简并：应由什么量判断

$\Delta$ 始终表示非对角质量平方项，$b-a$ 表示对角元之差，不复用同一符号。小角条件是 $2\lvert\Delta\rvert\ll\lvert b-a\rvert$；失效后须精确对角化。$m_-\le m_+$ 表示质量排序，$h_1,h_2$ 表示场成分标签，二者由本征矢对应。工作 E 给出唯一完整推导；附录 F 给出两种质量排序下的数值检验。
''','remove repeated eigenvalue derivation')
section('#### 2.1.7.5 ','#### 2.1.7.6 ',r'''
#### 2.1.7.5 何时加入宽度与非对角自能

树级实矩阵先确定谱和场成分。圈级混合是审稿人关注的对象，即使树级门户取零，仍须核算允许图、反项和阈值。统一逆传播子为 $p^2\mathbf1-\mathcal M_0^2-\widehat\Pi(p^2)$，树级非对角项不能被遗漏；工作 E 给出显式矩阵及极点求解。

比较 $\lvert m_2-m_1\rvert$ 与 $\Gamma_1,\Gamma_2$；在树级质量基底另比较 $\lvert m_2^2-m_1^2\rvert$ 与 $\lvert\widehat\Pi_{12}\rvert,m_i\Gamma_i$。自能影响目标精度时求极点；共同初末态中的重叠与干涉重要时算完整振幅。实验分辨率和效率不能替代粒子宽度。
''','propagator dimensions')
section('#### 2.1.7.6 ','#### 2.1.7.7 ',r'''
#### 2.1.7.6 从混合转到 Higgs 信号与新标量衰变

单个可分辨 Higgs 候选态、SM 耦合普适缩放且无其他产生/衰变修正时，才可用 $\mu\simeq c_\theta^2(1-\mathrm{BR}_{\rm new})$。双态重叠、额外振幅、直接轻子 Yukawa 与新增总宽度要求逐过程计算。

工作 F 连续给出信号强度、候选通道与阈值、部分宽度、总宽度和寿命，再说明如何对应实验。味变末态须从真实耦合矩阵判断，不能默认 $\mu^\pm\tau^\mp$ 存在；两体道关闭也不证明粒子稳定。$h_1,h_2$ 是质量本征态，破缺前复场 $S$ 不是第三个物理标量。
''','consolidate widths')
section('#### 工作 E：混合角','#### 工作 F：从物理谱',r'''
#### 工作 E：混合角的可核查解析关系与近简并处理边界（B-5）

**输入与约定。** 使用工作 A 的势、驻点条件和规范固定：
\[
H=\frac1{\sqrt2}(0,v+h)^T,\quad S=\frac{v_S+s}{\sqrt2},\quad
\mathcal M_0^2=\begin{pmatrix}a&\Delta\\\Delta&b\end{pmatrix},
\quad a=2\lambda_Hv^2,\quad b=2\lambda_Sv_S^2,\quad\Delta=\lambda_{HS}vv_S.
\]
统一旋转
\[
\begin{pmatrix}h_1\\h_2\end{pmatrix}
=R(\theta)\begin{pmatrix}h\\s\end{pmatrix},\qquad
R=\begin{pmatrix}c_\theta&-s_\theta\\s_\theta&c_\theta\end{pmatrix}.
\]
$h_1$ 为具有较大 $h$ 分量的 Higgs 候选态，$h_2$ 为另一态，不预设轻重。按质量排序另记 $m_-^2\le m_+^2$。等权混合处声明分支，此时不能说某态唯一更像 SM Higgs。

**第一步：求本征值并验证旋转。** 特征方程与根为
\[
(a-m^2)(b-m^2)-\Delta^2=0,\qquad
m_\pm^2=\frac{a+b\pm\sqrt{(b-a)^2+4\Delta^2}}2.
\]
旋转后非对角元为
\[
(R\mathcal M_0^2R^T)_{12}=\frac{a-b}{2}\sin2\theta+\Delta\cos2\theta.
\]
令其为零得到 $\tan2\theta=2\Delta/(b-a)$；正负号与上述旋转必须一并使用。
\[
\lvert\sin2\theta\rvert=\frac{2\lvert\Delta\rvert}{\sqrt{(b-a)^2+4\Delta^2}}.
\]

**第二步：数值实现同一个分支。** 先取
\[
\alpha=\tfrac12\operatorname{atan2}(2\Delta,b-a),\qquad
\theta=\begin{cases}\alpha,&\lvert\alpha\rvert\le\pi/4,\\
\alpha-\operatorname{sgn}(\alpha)\pi/2,&\lvert\alpha\rvert>\pi/4.\end{cases}
\]
直接算 $R\mathcal M_0^2R^T$；第一、第二对角元分别为 $m_1^2,m_2^2$，再与 $m_\pm^2$ 核对。未经分支处理的半角 atan2 不能直接与小角解比较。$a=b,\Delta=0$ 时记录简并并选择基底，不把软件默认角当作物理结论。

**第三步：判定近似。** 就近 Higgs 候选分支上，只有 $\lvert\Delta\rvert\ll\lvert b-a\rvert$ 时才有 $\theta\simeq\Delta/(b-a)$。$a=b,\Delta\ne0$ 时 $\lvert\theta\rvert=\pi/4$、质量平方分裂 $2\lvert\Delta\rvert$；若两者同时趋零，极限依赖路径。输入 $\sqrt a$ 不自动等于观测约 125 GeV，应由物理 $m_1$ 拟合输入。附录 F 在质量差两侧验证分支。

**第四步：反解耦合并独立复核。**
\[
\begin{aligned}
2\lambda_Hv^2&=m_1^2c_\theta^2+m_2^2s_\theta^2,\\
2\lambda_Sv_S^2&=m_1^2s_\theta^2+m_2^2c_\theta^2,\\
\lambda_{HS}vv_S&=(m_2^2-m_1^2)s_\theta c_\theta.
\end{aligned}
\]
从输入耦合算谱再反代，核验矩阵、迹、行列式和本征值，按量级设置绝对/相对残差容限。$\lambda_S\le\lambda_S^{\max}$ 限制第二式的加权质量平方，不能无条件套在某个混合态上。扩大标量谱或采用圈级物理谱后须重推。

**第五步：圈级修正与重复计数。** 重整化 1PI 自能 $\widehat\Pi_{hs}(p^2)$ 中的轻轻子、VLL、反项、波函数与 tadpole 处理须在同一 UV 方案。结构示意
\[
\widehat\Pi_{hs}(p^2)\supset
\frac{N}{16\pi^2}y_{h\ell\ell}y_{s\ell\ell}F(p^2,m_\ell^2;\mu)
+\text{counterterms/matching}
\]
中 $F$ 有质量平方量纲；系数、有限项及相消必须用实际质量与耦合矩阵计算。未混合近似 $y_{s\ell\ell}=m_\ell/v_S$ 不证明 VLL 阈值很小。逐图追踪味：一个对角 $h$ 顶点与一个纯非对角 $s$ 顶点可能无法闭合轻子味，但两个 $S$ 插入的四点图未必为零。二点自能、门户反项、有限阈值分别求解，再按匹配约定组合。

**第六步：需要时求极点和振幅。** 统一采用自能负号约定：
\[
\mathbf D^{-1}(p^2)=p^2\mathbf1-\mathcal M_0^2-\widehat{\mathbf\Pi}(p^2)
=\begin{pmatrix}
p^2-a-\widehat\Pi_{hh}&-\Delta-\widehat\Pi_{hs}\\
-\Delta-\widehat\Pi_{sh}&p^2-b-\widehat\Pi_{ss}
\end{pmatrix},\qquad\det\mathbf D^{-1}(p^2)=0.
\]
各自能在同一 $p^2$ 取值；$\widehat\Pi$ 不包含已经写入 $\mathcal M_0^2$ 的树级 $\Delta$。先以树级根作初值追踪两复极点，检查行列式残差、初值/步长稳定性、弱耦合极限及尺度变化。

在树级质量基底比较 $\lvert m_2^2-m_1^2\rvert$、$\lvert\widehat\Pi_{12}\rvert$、$m_i\Gamma_i$；另比较质量差与宽度。若共享初末态的重叠改变目标精度，计算
\[
\mathcal A_{i\to f}(p^2)=\mathbf g_f^{\,T}\mathbf D(p^2)\mathbf g_i
\]
并补齐必要顶角、非共振图和相干项。一个实常数角不能替代完整振幅；重求和须采用一致的规范和重整化处理，不把任意自能子集当作完整规范无关率。实验分辨率、效率和背景随后进入线形比较。

**输出与判断。** 每点输出输入矩阵、质量、场成分、角度分支、近似误差、宽度/自能比较及方法精度。分为“小角受控”“需精确实矩阵”“需圈级极点/干涉”“计算不足”；这些不是排除带。模型专属一圈系数和可观测率仍须实际求得。
''','authoritative scalar derivation')
once(r'没有额外 VLL 圈图对 $gg\to h$、$h\to\gamma\gamma$ 等造成不可忽略的修正',
 r'没有额外贡献使各通道偏离普适缩放（例如 VLL 对 $h\to\gamma\gamma$ 的圈图修正）','VLL color')
s=s.replace('**实际比较 Higgs 数据的建议步骤：**',r'''**无色 VLL 的范围。** 本模型 VLL 不带色荷，不直接贡献一圈 $gg\to h$ 三角图；它们可影响 $h\to\gamma\gamma$、$h\to Z\gamma$、轻子 Yukawa，并通过混合等间接改变产生率。可对照 [矢量样费米子与 Higgs 耦合分析](https://arxiv.org/abs/1207.7062)，不可将有色新费米子的胶子融合效应套用到 VLL。

**实际比较 Higgs 数据的建议步骤：**''')
once(r'5. 对每点检验 $\sum_i\mathrm{BR}_i=1$（在所宣称纳入的开放通道集合和数值容差内）；遗漏开放衰变或人为省略显著的新宽度会破坏这一检验。',
 r'5. 在 $\Gamma_{\rm tot}>0$ 时检验 $\sum_i\mathrm{BR}_i=1$，但这只检查归一化：若总宽度也由同一不完整通道表求和，漏道后等式仍成立。须另用独立的顶角—阈值清单核查所有允许的在壳、必要离壳及圈级末态；有独立包含性宽度时再比较。避免把含同一共振的多体率与因子化级联重复相加。总宽度为零时不能定义 $0/0$ 的 BR。','BR check')
section('#### 3.4.2 ','#### 3.4.3 ',r'''
#### 3.4.2 门户进入联合分析的物理接口

完整标量推导在第 2 章工作 A/E；这里调用同一计算模块。输入 $(\lambda_H,\lambda_S,\lambda_{HS},v,v_S)$，输出物理 $(m_1,m_2,\theta)$、场成分、顶角与阈值。$h_1=c_\theta h-s_\theta s$ 仍标记 Higgs 候选；$m_\pm$ 只作质量排序，不另换约定。

这些输出确定匹配中保留/积分消去的自由度、阈值和相关实验。树级谱先作初筛，再由宽度、自能及目标精度决定是否升级到极点与干涉计算。联合扫描在本章记录该模块的输入输出，不重复标量推导。
''','scalar interface')
a=s.index('- **做法：** 先检查标量势的驻点条件',s.index('#### 3.4.6'))
b=s.index('- **输出：** 树级质量本征值',a)
s=s[:a]+r'''- **做法：** 检查驻点并构造 $\mathcal M_0^2=\begin{pmatrix}a&\Delta\\\Delta&b\end{pmatrix}$，其中 $a=2\lambda_Hv^2$、$b=2\lambda_Sv_S^2$、$\Delta=\lambda_{HS}vv_S$。采用第 2 章工作 E 的精确对角化、分支与反解；同时记录场成分标签 $h_1,h_2$ 和质量排序 $m_\pm$。不要把混合前对角元当作物理质量。
'''+s[b:]
once('本节的目的不是预先断言当前模型一定不兼容，而是建立一条足以证明兼容或不兼容的数学链。审稿人关于 Weinberg 算符、代际对齐和 PMNS 的判断需要代入当前稿件的真实荷表逐项验证。',
 '本节展开已得到的条件性结构结论：在固定荷表与破缺假设下，电子味分块无法复现观测 PMNS。以下展示算符、矩阵和基底推理，并规定扩展如何另行检验；最小模型的已知障碍与扩展的待拟合状态必须分开。','PMNS known proof')
s=s.replace('PMNS 研究必须允许三种不同结论：最小模型兼容、最小模型不兼容但扩展模型可能兼容、当前证据不足以判定。不能预先选定“模型兼容”的回复，再倒推质量矩阵。','当前已知结论是：在声明的 v6 最小荷表与破缺假设下，观测 PMNS 不能实现。下一步须选择扩展或限定主张；改变假设后才重新开放兼容性判断。扩展未计算，不使原最小模型的条件性结论退回未知。')
s=s.replace('| 最小模型产生足够一般的 PMNS 结构，并存在满足振荡数据的参数点 |','| 另行定义的扩展模型产生足够一般的 PMNS 结构，并存在满足振荡数据的参数点 |')
s=s.replace('| 结构分析或拟合尚未完成 | 尚不能声称兼容或不兼容已被最终证明 |','| 候选扩展的结构分析或拟合尚未完成 | 扩展兼容性未定；原最小模型的条件性分块结论仍成立 |')
s=s.replace('### 4.4 英文回复模板：模型兼容时','### 4.4 英文回复模板：扩展模型经验证兼容时')
s=s.replace('> **Response:** We thank the referee for raising the question of compatibility with neutrino oscillation data. We have derived','> **Response:** We thank the referee for raising the question of compatibility with neutrino oscillation data. The minimal model has the residual-symmetry obstruction described above. In the explicitly extended model [specify the new fields and symmetry breaking], we have derived')
s=s.replace('PMNS 最终矩阵/拟合','候选扩展的 PMNS 矩阵/拟合').replace('PMNS 结构判定及可能的拟合','候选扩展的 PMNS 推导与拟合')

# Additional edits and the pedagogical supplements are loaded as literal UTF-8 resources.
(ROOT/'work'/'v57_corrected.md').write_text(s,encoding='utf-8')
(ROOT/'work'/'correction_log.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'changes':len(changes),'chars':len(s),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}))
