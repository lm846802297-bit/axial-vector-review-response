# Minor Points 论证扩充与复核记录（2026-11-06）

## 1. 任务范围与权威依据

- 正式回复信：Replies_to_Referee_3_referee_facing_2026-11-04.tex。
- 工作分支：review/response-point-conclusions-20261106；更新对象为 PR #55。
- 原始审稿意见：dw13678_report_1_a.md。
- 长期规范：审稿意见-gpt/写作规范/审稿回复写作原则.md，本轮新增 §2.2，并同步落实 §5、§6、§6.1、§7。
- 项目模型边界：DEC-01/DEC-15。所有非中微子 Minor Points 均采用原论文单 VEV \(S+\mathrm{VLL}\) 模型；不引入 Major 3/4.1 的可选 \(\sigma+3N_R\) 完成机制。
- 本轮只修改正式回复信 TeX、长期写作规范和本内部审查记录；不修改论文源码、图表、BibTeX 数据库或 PDF。

本轮目标不是机械增加篇幅，而是使每个实质性 Minor Point 的回答具有可识别的直接结论、物理原因、公式来源、定量 benchmark 和适用范围。多子问题逐项回答；没有证据支持的数值或 collider reach 不写入正式回复。

## 2. 逐点修改记录

### Minor Point 1 — 参数范围与 “light”

**新增解释：**
- 说明 Fig. 2 下端保留低质量实验室 \((g-2)_\mu\) 约束已经重要的区域，并将其渐近延伸及重叠的模型依赖天体物理敏感性指向 Major 2/4.4。
- 说明上端对应本文所纳入 meson-decay、B-factory 和 \(Z\)-decay 搜索逐渐达到或耗尽其运动学覆盖；更重媒介子属于更高能探针的范围。
- 明确两端均不是模型的物理边界，也不是普遍排除边界。

**保留：** \(10^{-3}\,\mathrm{GeV}\le m_{A'}\le10^2\,\mathrm{GeV}\)、\(10^{-6}\le g_X\le1\) 的实际 Fig. 2 窗口；对 Major 2 的详细交叉引用。参数窗口与 DEC-06 一致。

### Minor Point 2 — 纯轴矢量极限

**新增解释：**
- 保留 \(\theta_{\mu R}\to0\) 时 \(g_V^\mu\to0\)、\(g_A^\mu\to-g_X\) 的定义。
- 明确 tau 扇区具有相反的整体 \(U(1)_X\) 电荷符号，但其矢量/轴矢量耦合的绝对值分别按 \(\sin^2\theta_{\tau R}\)、\(\cos^2\theta_{\tau R}\) 缩放。
- 因而完整带电轻子流的严格纯轴极限要求两个右手混合角都趋于零；有限角度属于小矢量分量情形。

**一致性处理：** 使用耦合绝对值陈述 tau 扇区，避免把整体电荷符号与 Major 4.3 中按绝对值讨论的 \(|g_V^\ell/g_A^\ell|\) 混淆。

### Minor Point 3 — VLL 质量下限与矢量耦合

**新增解释：**
- 对 \(\ell=\mu,\tau\) 统一展示轻子质量匹配关系 \(m_\ell\simeq\theta_{\ell L}\theta_{\ell R}M_{E\ell}\) 与共同小混合条件。
- 保留条件性质量尺度 \(M_{E\mu}\gtrsim1.06\,\mathrm{TeV}\)、\(M_{E\tau}\gtrsim17.8\,\mathrm{TeV}\)，以及简并 VLL 基准下由 tau 扇区给出的更强 \(M_E\gtrsim17.8\,\mathrm{TeV}\)。
- 将两个味的矢量/轴矢量耦合幅度统一写为 \(|g_V^\ell|=|g_X|\sin^2\theta_{\ell R}\)、\(|g_A^\ell|=|g_X|\cos^2\theta_{\ell R}\)，并给出 \(\ell=\mu,\tau\) 的统一比值。
- 保留“这是混合角假设与质量匹配共同给出的条件性质量尺度，不是直接搜索质量下限”的限定。

**物理意义：** 质量关系约束左右混合角的乘积；只有结合 Eq. (27) 对各角度的独立上限，才能推出条件性 VLL 质量尺度和矢量分量上限。

### Minor Point 4 — Conservative benchmark 的含义

**新增解释：**
- 明确 Eq. (27) 是现象学分析所采用的小混合参数域的共同上边界，不是一个 benchmark point，也不是所有四个混合角的普适实验上限。
- 解释 \(\theta^2\lesssim10^{-4}\) 控制轻重态混合引起的领先修正，而右手角通过 \(|g_V^\ell/g_A^\ell|=\tan^2\theta_{\ell R}\lesssim1.01\times10^{-4}\) 控制残余矢量分量。
- 将其与 Minor 3 的条件性 VLL 质量关系、Major 4.3 的过程级矢量/轴矢量限制比较衔接，避免把小角度直接等同于所有观测量均不敏感。
- 增加 LEP 对 \(\theta_{\mu L}\) 的约 \(4\times10^{-2}\)（95% CL）比较，并明确这只针对左手 muon 角，不是四个角的共同实验上限；其他 VLL 全局拟合依赖电弱表示和观测量集合。
- 增加与正文模型讨论一致的来源引用：PDG/ALEPH 以及 Crivellin/Poh 的 VLL 拟合文献。

**结论边界：** \(10^{-2}\) 是本文明确采用的分析假设，数值选择使 near-axial 工作域可定量控制；不把它表述成全局拟合结果或普适实验限制。

### Minor Point 5 — Muon Collider 的目的与独立子问题

保留原有 chiral-amplitude、角分布、\(A_{\rm FB}\) 解析式、vector/axial 总率比较和 Higgs-factory 讨论，并作以下补强：

1. **为何选择 muon collider：** 保留其对 muon-philic \(A'\) 的直接初态耦合及高质量互补探测定位；不将示例写成 detector-level reach。
2. **为何使用 \(\tau^+\tau^-\) 而不是 \(\mu^+\mu^-\)：** 保留 tau 末态只有 \(s\)-channel \(\gamma,Z,A'\) 的理由，并明确同味 muon 末态存在额外 \(t\)-channel 图，角分布解释更复杂。
3. **为何使用 \(A_{\rm FB}\)：** 保留由 \(S_+\)、\(S_-\) 得到的解析关系，解释其比较同手征与异手征振幅组合，且不需要初态极化束。
4. **为何没有数值化 polarization reach：** 保留 \(A_{\rm LR}^\mu\)、\(P_\tau\) 的定义，并新增在相同对称角接受度、无质量近似下它们对 \(|\mathcal A_{ij}|^2\) 的显式投影公式。解释两者分别分辨初态 muon 手征性和末态 tau helicity；由于当前图示没有 beam-polarization、tau-polarimetry analyzing power、效率和系统误差输入，不声称数值灵敏度或 reach。
5. **为何不把 \(ee\) 当作等价通道：** 明确 \(\tau^+\tau^-\) 末态具有树级 \(g_i^\mu g_j^\tau\) 振幅，而 \(ee\) 需要 \(e\epsilon_{\gamma A'}(s)\) 电子顶点；低质量在壳 kinetic-mixing 数值不能外推至多 TeV 的 \(q^2=s\)。
6. **为何仍讨论 Higgs factory：** 将 \(e^+e^-\to Zs\) 的树级关系写为 \(\sin^2\theta_{hs}\) 乘以同质量 SM Higgsstrahlung 截面；保留 \(h\to ss\) 的 \(g_{hss}\) 宽度公式，并说明两种通道依赖不同的标量参数，不能仅由 \(\sin^2\theta_{hs}\) 决定 \(h\to ss\)。继续保留 Major 1.3 的小 portal matching benchmark 与近简并区限定，不声称 model-specific reach。
7. **宽度 benchmark 澄清：** 从两种带电 Dirac 轻子道和两种活性 chiral-neutrino 道的部分宽度推导 \(\Gamma_{A'}=g_X^2m_{A'}/(4\pi)\)。明确 \(m_{A'}=1\,\mathrm{TeV}\)、\(g_X=0.05\) 的非共振点宽度约 \(0.199\,\mathrm{GeV}\)，而 \(0.60\,\mathrm{GeV}\) 对应 \(m_{A'}=\sqrt{s}=3\,\mathrm{TeV}\) 的共振点。

**数值边界：** 不加入此前未从原始计算脚本/数据复核的 \(A_{\rm LR}^\mu\)、\(P_\tau\) 或 vector/axial \(A_{\rm FB}\) 新数值。新增的是从回复信既有 chiral amplitudes 直接推导的解析投影关系。

### Minor Point 6.1 — “light”

补充本文覆盖多个数量级、不同探针具有不同运动学阈值和灵敏度，因此不存在一个适用于所有分析的统一 light/heavy 质量切分。保留实际摘要范围与 Fig. 2 数值窗口。

### Minor Point 6.2 — “representative bounds”

补充不同条目不是同一可观测量的强弱排名；它们有不同质量区间、源环境、耦合生成机制、置信度约定及产生/ trapping 假设。保留 selected、non-exhaustive、source-dependent 和非全局排除的原有结论。

### Minor Point 6.3 — intermediate scalar mass

**保持不变。** 现有回复已给出 BaBar/Belle 与两项 Belle II 标量分析的质量范围、\(m_s=1\,\mathrm{GeV}\) Belle benchmark、\(v_s\)/\(y_{s\mu\mu}\)/\(g_X\) UV 映射、\(s\to A'A'\) 对可见分支比的影响，以及不同分析自旋和耦合假设的区别。继续扩写只会重复 Major Point 1.1。

### Minor Point 6.4 — point-by-point

补充无量纲形式
\[
\frac{\lambda_S}{4\pi}=\frac{m_s^2}{8\pi v_s^2},
\]
解释在 \(\lambda_S^{\max}=4\pi\) 时逐点检查等价于该比值不超过 1；同时保留每个 \((m_{A'},g_X)\) 网格点先导出 \(v_s\)、再确定 \(\lambda_S\) 的流程及“理论一致性检查不是实验排除”的区分。

### Minor Point 6.5 — parameter region of interest / prompt

**新增完整寿命论证：**
- 从原论文单 VEV 模型的活性中微子规范流写出 \(\nu_\mu,\nu_\tau\) 两个 chiral channel，说明单个 massless chiral-neutrino 道贡献 \(g_X^2m_{A'}/(24\pi)\)，两味求和给出 \(\Gamma_{\nu\bar\nu}=g_X^2m_{A'}/(12\pi)\)。
- 由于该部分宽度是总宽度的正贡献，\(\Gamma_{\rm tot}\ge\Gamma_{\nu\bar\nu}\)，所以它给出 proper decay length 的上界，而不是下界。
- 对 \(m_{A'}=0.212\,\mathrm{GeV}\)、\(g_X=7\times10^{-4}\)，复核 \(\Gamma_{\nu\bar\nu}=2.7555\times10^{-9}\,\mathrm{GeV}\)、\(c\tau\le0.0716\,\mu\mathrm m\)，在 \(\gamma=25\) 时 \(L_{\rm lab}\le1.79\,\mu\mathrm m\)。
- 说明该点仅比 \(2m_\mu=0.211317\,\mathrm{GeV}\) 高约 \(0.683\,\mathrm{MeV}\)，纯轴矢量 dimuon 宽度含 \(\beta_\mu^3=(1-4m_\mu^2/m_{A'}^2)^{3/2}\simeq5.16\times10^{-4}\)，故可见道近阈值受到强烈抑制。
- 明确 neutrino-only 宽度给出寿命保守上界；其他开放道只能缩短寿命。单一 benchmark 不代表整个参数空间均满足 prompt selection，且具体 prompt 条件仍依赖实验分析。

### Minor Point 6.6 — \(v_s=2\,\mathrm{GeV}\) line

补充一般标量质量下的边界
\[
v_s^{\min}(m_s)=\frac{m_s}{\sqrt{8\pi}}\simeq0.1995m_s
\]
（\(\lambda_S^{\max}=4\pi\)）。说明 \(v_s\simeq2\,\mathrm{GeV}\) 只对应 \(m_s=10\,\mathrm{GeV}\) 参考标量 benchmark；改变 \(m_s\) 时边界线性移动。保留该线是标量四次耦合一致性边界，不是 Yukawa 非微扰界限或实验排除。

## 3. 长期规范新增内容

在审稿回复写作原则中新增强制 §2.2「论证充分性原则：从结论陈述到可复核的物理论证」，并同步 §5、§6、§6.1、§7：

- 不能仅给结论，还要解释物理原因；
- 不能仅列公式，还要说明公式从模型假设/拉格朗日量/规范荷/质量矩阵/有效算符/振幅定义或文献如何得到；
- 不能仅给数值，还要说明 benchmark 输入、归一化、近似条件和物理意义，并保证可复核；
- 不能只说实验限制不适用，还要解释产生机制、实验假设与本文模型的差异及匹配条件；
- 多子问题必须逐项回答，不能以一句总体结论代替；
- 说明不机械增加篇幅，而按问题复杂度提供闭合论证。

§2.2 明确与 §3.1 的互补关系：§3.1 防止删除具有独立论证功能的内容；§2.2 防止只留下结论而缺少物理原因、推导、定量证据和适用范围。§5 增加逻辑组织说明，§6 和 §6.1 将该原则纳入强制工作流程与 PR 模板，§7 增加逐项自检。

## 4. 删除/合并台账

**无实质性科学内容删除或合并。**

本轮将原有简短句段扩展为更完整的物理解释、解析关系或定量推导。Minor 3 的 muon-only 耦合展示改为 muon/tau 两味统一的绝对值表达；Minor 4 的简短说明改为解释性段落；Minor 5 的宽度说明、极化观测量解释、\(ee\) 通道说明和 Higgs-factory 说明均为扩展；Minor 6.5 的单句寿命结果改为从拉格朗日量到宽度、寿命、boost 和阈值因子的推导。原有独立推导、benchmark、引用和适用条件均保留。Minor 6.3 完全未修改。

## 5. 静态检查与验证边界

**已执行的静态检查：**
- TeX 花括号平衡；
- LaTeX begin/end 环境配对；
- equation/figure/table 标签唯一性；
- \ref、\eqref 等交叉引用目标存在；
- 当前两份 BibTeX 数据库中的 39 个唯一 citation keys（78 次引用出现） 均存在（本轮新增的 PDG、ALEPH、Crivellin、Poh keys 已在主 references 数据库中）；
- 检查了本轮新增公式、数值及原论文单 VEV 模型边界。

**独立数值复核：**
- \(g_X=0.05\) 时，\(\Gamma_{A'}=g_X^2m_{A'}/(4\pi)\) 给出 \(m_{A'}=1\,\mathrm{TeV}\) 时 \(0.19894\,\mathrm{GeV}\)，\(m_{A'}=3\,\mathrm{TeV}\) 时 \(0.59683\,\mathrm{GeV}\)。
- Minor 6.5 的 \(\Gamma_{\nu\bar\nu}\)、\(c\tau\)、boost 后 \(L_{\rm lab}\)、dimuon 阈值偏移和 \(\beta_\mu^3\) 已独立复算。
- Minor 5 的 \(A_{\rm LR}^\mu\)、\(P_\tau\) 解析投影由既有 chiral-amplitude 公式在对称角接受度和无质量近似下代数推导；没有声称数值 reach，也没有加入未验证的极化数值。

**未执行：**
- 完整 LaTeX 编译；
- 最新 PDF 重编译与逐页视觉检查；
- CI；
- 新的 detector-level Monte Carlo 或 collider reach；
- 全部数值脚本的 clean-environment 重跑。

论文源码、图表、BibTeX 数据库和 PDF 均未修改。上述未执行项目不标记为通过。

**本轮源文件版本：** TeX blob SHA `2307b04cc562bd71bf8733a20695e28a198cdeea`；写作规范 blob SHA `f52ffad0ee8fd047eebd8ca2d514ec41bfa6f93b`。静态引用审计结果为 78 次引用出现、39 个唯一 key，全部可在两份 BibTeX 数据库中解析。

## 6. 审查结论

Minor 1–5、6.1、6.2、6.4、6.5、6.6 已按新的论证充分性标准扩充；Minor 6.3 经复核保持原状。回复信仍以原论文单 VEV \(S+\mathrm{VLL}\) 模型回答所有非中微子问题。新增的解析和数值内容均标明 benchmark、近似与适用范围；未把未验证的 collider reach 写成结果。PR 保持未合并，等待作者审阅。
