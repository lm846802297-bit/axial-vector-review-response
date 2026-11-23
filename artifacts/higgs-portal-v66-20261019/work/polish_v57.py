from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
p=next((ROOT/'审稿意见-gpt').glob('审稿意见分析v5.7*.md'))
s=p.read_text(encoding='utf-8')
s=s.replace('重整 §3.5、§8、§13 与附录 E 的职责','重整当时的 §3.4、§8、§13 与附录 E 的职责')
a=s.index('### 各专题内部的固定阅读顺序');b=s.index('### 专题之间必须',a)
s=s[:a]+'''### 各专题内部的固定阅读顺序

1. **原文与诉求：** 原文、准确释义、明确要求与建议的区别。
2. **物理分析：** 问题的理论依据、关键量、近似及适用条件。
3. **补充工作：** 分析对应到哪些工作，为什么必须做。
4. **总体流程：** 前置输入、依赖顺序和中途决策。
5. **具体执行：** 推导、计算方法、输入输出及失败分支。
6. **验证与约束：** 独立核查、理论条件和实验适用性。
7. **结果与修改：** 不同结果如何改变正文、图表及主张。
8. **回复与验收：** 按实际证据填写回复，登记未决事项。

'''+s[b:]
needle='**从匹配转到质量及误差。**'
assert s.count(needle)==1
s=s.replace(needle,r'''**直接使用 v6 的两态质量矩阵。** 每个轻子味的树级块为
\[
M_\alpha=\begin{pmatrix}0&m_{\alpha L}\\m_{\alpha R}&M_{E_\alpha}\end{pmatrix},
\quad m_{\alpha L}=y_\alpha v/\sqrt2,\quad
m_{\alpha R}=\lambda_\alpha v_S/\sqrt2.
\]
这是左右手之间的 Dirac 质量矩阵，通常不对称，应求奇异值而不是照搬标量的正交对角化。记
\[
T_\alpha=|M_{E_\alpha}|^2+|m_{\alpha L}|^2+|m_{\alpha R}|^2,\qquad
P_\alpha=|m_{\alpha L}m_{\alpha R}|^2.
\]
由 $M_\alpha M_\alpha^\dagger$ 的迹和行列式得到
\[
m_{\alpha,\pm}^2=\tfrac12\left(T_\alpha\pm
\sqrt{T_\alpha^2-4P_\alpha}\right).
\]
强层级时，轻根用等价的 $2P_\alpha/(T_\alpha+\sqrt{T_\alpha^2-4P_\alpha})$ 计算以避免相减消失，并与 SVD 交叉核对。重质量大于两非对角项时，轻质量约为 $|m_{\alpha L}m_{\alpha R}/M_{E_\alpha}|$，左右混合量级分别为 $|m_{\alpha L}/M_{E_\alpha}|$、$|m_{\alpha R}/M_{E_\alpha}|$。消去重块所得有效质量的整体符号可由场重相位吸收，不能将它当作负的物理质量。两侧旋转仍从完整矩阵求得，随后用来计算物理电流。

'''+needle)
s=s.replace('把工作要求分三层','把工作要求分四层')
s=s.replace('以本轮最终投稿稿为基准，μ 子对撞机相关文献列为 Ref. [85]','以当前存档稿 v6 为核对基准，μ 子对撞机相关文献列为 Ref. [85]')
s=s.replace('最终稿 Ref. [85] 的题名','当前存档稿 v6 的 Ref. [85] 题名')
s=s.replace('最终投稿稿 v6 中对应文献','当前存档稿 v6 中对应文献')
s=s.replace('当前存档稿 v6事实','当前存档稿 v6 的事实').replace('当前存档稿 v6的','当前存档稿 v6 的')
s=s.replace('以当前存档稿 v6为准','以当前存档稿 v6 为核对对象')
s=s.replace('后续回复信应引用当前存档稿 v6 的 Ref. [85]','后续回复信应按实际修订稿重新核定编号；若沿用当前存档稿 v6，则为 Ref. [85]')
s=s.replace('附录 G.15.6、附录 G.15.6','附录 G.15.6')
s=s.replace('因此所有规范不变算符都不能把 $e$ 与 $\\mu,\\tau$ 连接起来','因此在这些 VEV 下，规范不变算符不能生成连接 $e$ 与 $\\mu,\\tau$ 的二点质量或动能混合')
s=s.replace('§4.2 工作 B/E','§4.3 工作 B；§4.2 工作 E').replace('§4.2 工作 D/E','§4.3 工作 D；§4.2 工作 E')
s=s.replace('以上写法取 $\\mu_H^2,\\mu_S^2>0$ 且分别使用负的二次项，以便与 v6 的 $V(S)=-\\mu_S^2|S|^2+\\lambda_S|S|^4$ 及存在非零 $v_S$ 的约定一致；',
 '上式以 $-\\mu_H^2,-\\mu_S^2$ 记二次项系数；在一般含 portal 的模型中，记为 $\\mu_i^2$ 的实参数不必都为正。两者为正可作为与 v6 自发破缺讨论相近的一种基准，但不是双 VEV 真空的必要条件；')
lines=s.splitlines()
for i,l in enumerate(lines):
 if l.startswith('| Major 3：PMNS 兼容性 |'):
  lines[i]=l.replace('待决策/理论推导','最小模型障碍已解析确认；扩展/范围决策待完成')
 if l.startswith('| Major 4.1：中微子振荡 |'):
  lines[i]=l.replace('待理论推导/正文修改','最小结构结论已明确；正文/回复待修改')
s='\n'.join(lines)+'\n'

# Preserve complete introductory reviewer source for the high-level A-1--A-5 index.
report=(ROOT/'dw13678_report_1_a.md').read_text(encoding='utf-8')
report_lines=report.splitlines()
pre=[]
for line in report_lines:
 if re.search(r'1\.\s+.*Phenomenology|Major [Pp]oints',line):break
 if line.strip():pre.append(line.lstrip('# ').strip())
if pre:
 text='### A.0 总评与 Merits\n\n'+'\n'.join('> '+l for l in pre)+'\n\n'
 s=s.replace('### A.1 Major Point 1',text+'### A.1 Major Point 1')

# Math bars inside GFM tables must not create extra columns.
def math_bar(m):
 return '$'+re.sub(r'(?<!\\)\|',r'\\vert ',m.group(1))+'$'
lines=s.splitlines()
for i,line in enumerate(lines):
 if line.lstrip().startswith('|'):
  lines[i]=re.sub(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',math_bar,line)
s='\n'.join(lines)+'\n'
# Keep manuscript modification language distinct from manual modification.
s=s.replace('**当前存档稿 v6 的四项 Major Points 状态**','**当前存档稿 v6 的四项 Major Points 状态**')
p.write_text(s,encoding='utf-8')
print('Polished lines:',len(s.splitlines()))
