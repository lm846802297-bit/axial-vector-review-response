from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'work/v57_enhanced.md').read_text(encoding='utf-8')
starts={n:s.index(t) for n,t in {
2:'## 二、',3:'## 三、',4:'## 四、',5:'## 五、',6:'## 六、',7:'## 七、'}.items()}
nodes={}; intro={}
for ch in range(2,7):
 block=s[starts[ch]:starts[ch+1]]
 matches=list(re.finditer(r'^#{3,6} ('+str(ch)+r'\.\d+(?:\.\d+)*) (.+)$',block,re.M))
 intro[ch]=block[:matches[0].start()]
 for i,m in enumerate(matches):
  key=m.group(1);assert key not in nodes
  end=matches[i+1].start() if i+1<len(matches) else len(block)
  nodes[key]=(m.group(2),block[m.end():end].strip())

mp={}
def put(old,new):mp[old]=new
put('2.1','2.1');put('2.1.5','2.1.1')
for i in range(1,5):put(f'2.1.{i}',f'2.2.{i}')
for i in range(1,6):put(f'2.1.4.{i}',f'2.2.4.{i}')
put('2.1.7','2.2.5')
for i in range(1,9):put(f'2.1.7.{i}',f'2.2.5.{i}')
put('2.1.7.9','2.4.1');put('2.2','2.5.1');put('2.1.6','2.5.2')
for i in range(1,5):put(f'2.1.6.{i}',f'2.5.2.{i}')
put('2.1.6.5','2.7.1');put('2.1.6.6','2.8.1')
put('2.3','2.6')
for i,j in [(1,1),(2,2),(6,3),(7,4),(8,5),(9,6)]:put(f'2.3.{i}',f'2.6.{j}')
put('2.3.3','2.7.2');put('2.3.4','2.8.2');put('2.3.5','2.8.3')
put('2.4','2.5.3');put('2.4.1','2.5.3.1');put('2.4.2','2.7.3');put('2.4.3','2.8.4')
put('2.5','2.4');put('2.6','2.7');put('2.7','2.8')
put('3.1','3.1');put('3.1.1','3.1.1');put('3.2','3.5.1');put('3.2.1','3.2.1');put('3.3','3.4');put('3.4','3.5')
for i in range(1,5):put(f'3.4.{i}',f'3.2.{i+1}')
for i,j in [(5,2),(6,3),(7,4),(10,5)]:put(f'3.4.{i}',f'3.5.{j}')
for i,j in [(9,1),(11,2),(13,3)]:put(f'3.4.{i}',f'3.6.{j}')
put('3.4.8','3.7.1');put('3.4.12','3.7.2');put('3.4.14','3.7');put('3.5','3.8')
for k in ['4.1','4.1.1','4.2']:put(k,k)
put('4.2.1','4.5');put('4.3','4.4');put('4.3.1','4.7');put('4.4','4.8.1');put('4.5','4.8.2')
put('5.1','5.1');put('5.1.1','5.1.1');put('5.1.2','5.3');put('5.1.3','5.4')
for i in range(2,5):put(f'5.{i}',f'5.2.{i-1}')
for k in ['5.5','5.5.1','5.5.2','5.6','5.6.1','5.8']:put(k,k)
put('5.5.3','5.7.1');put('5.5.4','5.8.1');put('5.5.5','5.8.2');put('5.5.6','5.5.3')
put('5.7','5.4');put('5.7.1','5.7');put('5.7.2','5.8.3')
for key in nodes:
 if key.startswith('6.7'):put(key,key.replace('6.7','6.3.3',1))
 elif key.startswith('6.8'):put(key,key.replace('6.8','6.5.2',1))
 elif key=='6.9':put(key,'6.7')
 elif key=='6.10':put(key,'6.8')
 elif key.startswith('6.'):put(key,key)
assert set(nodes)==set(mp),(set(nodes)-set(mp),set(mp)-set(nodes))

# Rewrite current section references in one pass, before inserting new headings.
keys='(?:'+'|'.join(re.escape(k) for k in sorted(mp,key=len,reverse=True))+r')(?![\d.])'
ref=re.compile(r'§(?P<a>'+keys+r')(?:(?P<sep>\s*[–—-]\s*)§?(?P<b>'+keys+r'))?')
def remap(text):
 def sub(m):
  if not m['b']:return '§'+mp[m['a']]
  a,b=m['a'].split('.'),m['b'].split('.')
  if a[:-1]==b[:-1] and int(a[-1])<=int(b[-1]):
   seq=['.'.join(a[:-1]+[str(i)]) for i in range(int(a[-1]),int(b[-1])+1)]
   if all(k in mp for k in seq):
    mapped=list(dict.fromkeys(mp[k] for k in seq))
    return '、'.join('§'+k for k in mapped)
  return '§'+mp[m['a']]+'、§'+mp[m['b']]
 return ref.sub(sub,text)
used=[]
def body(key):
 used.append(key)
 t=remap(nodes[key][1])
 t=re.sub(r'\n---\s*$','',t).strip()
 # Unnumbered headings within a subsection sit beneath the new heading.
 base=min(len(mp[key].split('.'))+1,5)
 oldlevels=[len(m.group(1)) for m in re.finditer(r'^(#{3,6}) ',t,re.M)]
 if oldlevels:
  lowest=min(oldlevels)
  t=re.sub(r'^(#{3,6}) ',lambda m:'#'*min(6,base+1+len(m.group(1))-lowest)+' ',t,flags=re.M)
 return t
def node(key,title=None):
 new=mp[key];return '#'*min(6,len(new.split('.'))+1)+' '+new+' '+remap(title or nodes[key][0])+'\n\n'+body(key)
stages=['审稿人原文、准确释义与具体诉求','物理问题与理论依据','需要补充的工作及其目的','总体流程与任务依赖','逐项执行：推导、方法、输入输出与失败分支','理论验证、实验适用性与交叉核查','结果判读与论文修改','审稿回复、验收标准与未决事项']
out=[]
def major(ch):
 title=intro[ch].splitlines()[0]
 out.append(f'<a id="major-{ch-1}"></a>\n\n'+title+'\n\n')
 out.append('本专题按以下八个环节连续阅读；具体推导和执行方法均在本章，任务表只记录实际进展。\n\n')
 out.append(' → '.join(f'[{i+1}. {label}](#major-{ch-1}-step-{i+1})' for i,label in enumerate(['原文与诉求','物理分析','补充工作','总体流程','具体方法','验证与约束','结果与修改','回复与验收']))+'\n\n')
def stage(ch,i,content,lead=''):
 out.append(f'<a id="major-{ch-1}-step-{i}"></a>\n\n### {ch}.{i} {stages[i-1]}\n\n')
 if lead:out.append(lead+'\n\n')
 out.append(content.strip()+'\n\n')

major(2)
stage(2,1,body('2.1')+'\n\n'+node('2.1.5'),
 '准确释义：审稿人认为仅讨论轴矢量 EFT 与 UV 模型之间存在缺口；要求说明标量不能任意退耦的后果、允许质量范围、圈级门户和近简并 Higgs 信号，并以定量证据说明何时可以省略标量。其关于“可能最强”的判断仍需检验。')
stage(2,2,'\n\n'.join(node(k) for k in ['2.1.1','2.1.2','2.1.3','2.1.4']+[f'2.1.4.{i}' for i in range(1,6)]+['2.1.7']+[f'2.1.7.{i}' for i in range(1,9)]),
 '先解释哪些量控制谱与信号、为什么现有近似可能失效；随后将每个物理问题落实为工作和计算。这里不重复展开后文的完整对角化。')
stage(2,3,r'''
| 工作 | 要解决的问题 | 需要的输入与输出 |
|---|---|---|
| A–B：势、真空与谱 | 门户是否允许，所选真空与物理谱是否成立 | 荷表和势 → 驻点、质量矩阵、稳定性 |
| C–E：门户、圈图与混合 | 零边界能否稳定、近简并应如何计算 | 全 UV 顶角、边界及方案 → 阈值、自能、谱与误差 |
| F–G：产生、衰变与实验 | 真实信号、寿命及适用搜索是什么 | 本征态耦合 → 率、宽度、BR、实验适用性 |
| H：省略标量的误差 | 哪个过程、能标和精度下可简化 | 同点 UV/EFT 预测 → 有限定的误差结论 |
| 质量窗口与联合筛选 | “允许范围”是否有同点实现 | 理论条件、实验与扫描域 → 已验证/排除/未评估区域 |

下一节规定依赖顺序，再逐一展开 A–H 和质量扫描的方法。不能用一条微扰性线代替整项工作。
''')
stage(2,4,body('2.5')+'\n\n'+node('2.1.7.9','门户任务的阶段交付与核验'),
 '先冻结约定，再求谱和耦合，之后计算率与实验，最后才判定质量窗口和 EFT 误差。相关工作可以分工，但结果必须属于同一 UV 参数点。')
stage(2,5,'\n\n'.join(node(k) for k in ['2.2','2.1.6']+[f'2.1.6.{i}' for i in range(1,5)]+['2.4','2.4.1']),
 '以下是实际计算主体。工作 A–H 按依赖展开，随后说明如何将同点计算组织成质量窗口扫描；附录仅保存额外例子和记录模板。')
stage(2,6,body('2.3')+'\n\n'+'\n\n'.join(node(k) for k in ['2.3.1','2.3.2','2.3.6','2.3.7','2.3.8','2.3.9']),
 '理论筛选和实验适用性分别登记。先明确实验测量的对象，再比较当前模型的率、寿命和线形；未计算不等于未排除。')
stage(2,7,body('2.6')+'\n\n'+'\n\n'.join(node(k) for k in ['2.1.6.5','2.3.3','2.4.2'])+r'''

**结果分支。** 若标量效应超出目标误差，就纳入标量重算对应过程；若只在限定切片可忽略，就收窄摘要、图注和结论的范围。若某点仅通过标量微扰性而未通过 Yukawa、混合或实验筛选，只能报告该项通过。若未完成重铸，保留未评估区，不画成允许岛。
''')
stage(2,8,body('2.7')+'\n\n'+'\n\n'.join(node(k) for k in ['2.1.6.6','2.3.4','2.3.5','2.4.3']))

major(3)
stage(3,1,body('3.1')+'\n\n'+node('3.1.1'),
 '准确释义：参数范围需要物理动机，低能参数与 UV 输入的联系要展示，并判断图中的参数组合能否由同一个满足条件的 UV 点实现；不是只补一张上下限表。')
stage(3,2,'\n\n'.join(node(k) for k in ['3.2.1','3.4.1','3.4.2','3.4.3','3.4.4']),
 '本专题区分研究域、匹配域、UV 可实现性和实验状态。共同的标量模块只说明输入输出；不在这里重新定义旋转或质量标号。')
stage(3,3,r'''
| 工作 | 物理目的 | 要形成的结果 |
|---|---|---|
| 参数字典和范围 | 区分独立输入、派生量、benchmark 与实验界 | 可复现的扫描定义 |
| 重 VLL 匹配 | 从同外线振幅导出维五算符 | 系数、归一化、保留阶数及首个遗漏项 |
| 精确质量和理论条件 | 同点生成轻子质量并满足所选判据 | 质量/混合/Yukawa/标量联合检查 |
| UV–EFT 误差 | 检查具体过程中的截断 | 随能标和参数变化的误差、失败域 |
| 实验与图示 | 让图中每类区域有可追溯证据 | 多维状态、参数图、限制性结论 |

下面先看执行顺序，再按工作 A–E 阅读参数表、匹配方法和逐点联合计算。
''')
stage(3,4,body('3.3'),'先完成规范和参数定义，再匹配与求谱，随后检查误差与约束。质量关系无解时停止该点，数值搜索未找到时保留搜索状态。')
stage(3,5,body('3.4')+'\n\n'+ '\n\n'.join(node(k) for k in ['3.2','3.4.5','3.4.6','3.4.7','3.4.10']),
 '具体方法包括传播子展开、独立运动方程核对、轻重矩阵比较以及从输入到实验状态的逐点执行，不以“进行匹配/扫描”代替这些步骤。')
stage(3,6,'\n\n'.join(node(k) for k in ['3.4.9','3.4.11','3.4.13']))
stage(3,7,body('3.4.14')+'\n\n'+node('3.4.8')+'\n\n'+node('3.4.12'))
stage(3,8,body('3.5')+'\n\n**提交前验收：** 参数表、匹配归一化、精确质量、过程误差、实验适用性、图例与回复须指向相同输入。某个 EFT 点存在一个合格 UV 实现，与所有 UV 实现都合格，是不同命题。')

major(4)
stage(4,1,body('4.1')+'\n\n'+node('4.1.1'),
 '准确释义：审稿人质疑当前场与荷能否生成符合观测的中微子质量和 PMNS；仅使用太阳中微子的实验味比例不能代替模型机制。审稿人的“可能只能得到单位阵”需要以真实允许算符检验。')
raw=nodes['4.2'][1]
a=raw.index('#### 工作 A：');e=raw.index('#### 工作 E：')
proof=raw[:a]
requirements=raw[a:e]
decision=raw[e:]
cut=decision.index('**两个必须明确选择的方向：**')
proof+='\n\n'+decision[:cut]
decision=decision[cut:]
used.append('4.2')
stage(4,2,remap(proof),'当前最小假设的结构性结论在这里明确给出，后续步骤展开其证明并处理扩展。')
stage(4,3,remap(requirements),'以下工作服务于两类不同目标：复核最小模型的结构性障碍，或为明确的新模型建立可验证的质量机制。')
stage(4,4,body('4.3'),'顺序是荷与算符 → 质量矩阵 → 残余对称性 → 结构判定 → 扩展或限定主张。固定最小模型不需要无目的扫描；扩展结构成立后再做拟合。')
stage(4,5,body('4.2.1'),'下面给出允许算符、矩阵、残余对称性、双幺正/Takagi 分解和观测量提取的具体办法。')
stage(4,6,r'''
| 检验 | 方法 | 通过或失败意味着什么 |
|---|---|---|
| 荷守恒与残余对称性 | 枚举六种 Weinberg 条目及所有有 VEV 场；检验奇偶性 | 固定最小假设下电子分块有解析依据 |
| 矩阵与基底 | 检查质量项共轭、秩、两侧旋转、Takagi 残差及带电流 | 分解正确才可读取物理质量和混合 |
| 排序与简并 | 重排列标签；检查精确简并中哪些角不可观测 | 不能靠重编号或无物理意义的角绕过分块障碍 |
| 扩展的振荡数据 | 对实际似然计算质量差、角和相位；检查多初值稳定性 | 给出可行点或有证据的排除，优化失败不等于无解 |
| 新场关联检验 | 异常、规范质量、标量势、LFV、非幺正与相关实验 | PMNS 可拟合不等于整个扩展已可行 |

结构性证明与候选扩展拟合分别登记。纯解析排除不要求人为附加数值拟合才能成立；实验数据的采用版本和适用假设仍应注明。
''')
stage(4,7,remap(decision)+'\n\n'+body('4.3.1'))
stage(4,8,node('4.4')+'\n\n'+node('4.5'),
 '最小模型限制应明确报告；只有实际完成扩展验证后才能使用兼容性模板。收窄论文范围是作者选择，不等于消除了完整理论的中微子问题。')

major(5)
stage(5,1,body('5.1')+'\n\n'+node('5.1.1'),
 '准确释义：审稿人要求补足已列出的相关约束，尤其是中微子一致性、有限 benchmark 的动能混合、VLL 残余矢量耦合和恒星冷却。PMNS 的推导由第 4 章统一承担，本章独立回应它在约束完整性中的地位。')
stage(5,2,'\n\n'.join(node(k) for k in ['5.2','5.3','5.4']),
 '先区分动能混合、直接残余矢量耦合及介质中的产生与输运；这些机制必须合成物理电流和信号后才可与实验比较。')
stage(5,3,body('5.1.2'))
stage(5,4,body('5.1.3'))
stage(5,5,body('5.5')+'\n\n'+'\n\n'.join(node(k) for k in ['5.5.1','5.5.2','5.5.6']),
 '从轻重质量与耦合矩阵开始，依次给出圈图投影、阈值/边界、物理电流、事件率、寿命接受度、统计比较与天体输运的办法。')
stage(5,6,body('5.6')+'\n\n'+node('5.6.1'))
stage(5,7,body('5.7.1')+'\n\n'+node('5.5.3'))
stage(5,8,body('5.8')+'\n\n'+'\n\n'.join(node(k) for k in ['5.5.4','5.5.5','5.7.2']))
# The old 5.7 eight-line checklist duplicated 5.1.3; its references now resolve to 5.4.
used.append('5.7')

# Keep Minor 1–6 as the primary sequence; join quantitative methods to their own topic.
out.append(intro[6].splitlines()[0]+'\n\n按原始 Minor 1–6 顺读。VLL 定量方法合并到 Minor 3，μ 子对撞机方法合并到 Minor 5；后两节只作稿件事实和验收汇总。\n\n')
minororder=['6.1','6.1.1','6.2','6.2.1','6.3','6.3.1','6.3.2','6.7']+[f'6.7.{i}' for i in range(1,6)]+['6.4','6.4.1','6.5','6.5.1','6.8']+[f'6.8.{i}' for i in range(1,6)]+['6.6','6.6.1','6.9','6.10']
out.append('\n\n'.join(node(k) for k in minororder)+'\n\n')
assert len(used)==len(set(used)),[k for k in used if used.count(k)>1]
assert set(used)==set(nodes),(set(nodes)-set(used))
s=remap(s[:starts[2]])+''.join(out)+remap(s[starts[7]:])

# Human-facing navigation and version scope, avoiding obsolete paths in the opening.
a=s.index('> **本版修订重点：**');b=s.index('\n\n',a)
s=s[:a]+'> **本版修订重点：** 按物理博士生的连续研究阅读需求，把四项 Major 的正文统一重排为八个环节；将 VLL 和对撞机的具体方法归回各自 Minor。修正混合角、传播子、BR 完备性、PMNS 状态、动能混合定义及交叉引用，补充匹配、对角化、实验产额与统计方法。保留 38 项高层索引和全部 59 个原子条目；精简重复解释，不以任务卡代替正文方法。'+s[b:]
s=s.replace('### 版本记录\n','### 版本记录\n\n- **v5.7（本版，2026-10-20）：** 物理与公式校核；四个 Major 的正文统一为原文、物理、工作、流程、方法、验证、结果、回复八段；补齐可执行方法，合并重复推导并更新引用。模型专属科研结果仍按实际证据登记。\n')
a=s.index('### 按科研问题连续阅读');b=s.index('### 各专题内部的固定阅读顺序',a)
s=s[:a]+'''### 按科研问题连续阅读

| 专题 | 连续正文 | 本专题的具体方法 |
|---|---|---|
| [Major 1：标量与 Higgs portal](#major-1) | §2.1–§2.8 | 势与真空、圈图、谱、近简并、衰变、质量扫描和实验 |
| [Major 2：UV–EFT 映射](#major-2) | §3.1–§3.8 | 传播子匹配、精确质量、同点扫描、截断误差和图示 |
| [Major 3：PMNS](#major-3) | §4.1–§4.8 | 算符表、残余对称性、矩阵分解、扩展拟合及决策 |
| [Major 4：实验约束](#major-4) | §5.1–§5.8 | 物理电流、动能混合、产额/效率、统计和天体输运 |
| Minor Points | §6.1–§6.6 | 按原始编号分别给出修改、方法和结案要求 |
| 实际工作记录 | 第 8–12 章及附录 D–H | 按需登记输入、结果、状态与回复位置；不补藏物理方法 |

四个 Major 都采用相同的八段顺序，不能只由表中的物理主题推断阅读安排。每章的第五段是详细方法，第六段核查，第七段解释结果，第八段组织回复；具体工作记录可另存文件，方法本身保留在主文档。

'''+s[b:]
a=s.index('### 章节快速跳转');b=s.index('### 章节职责：',a)
s=s[:a]+'''### 章节快速跳转

- [Major 1](#major-1) · [Major 2](#major-2) · [Major 3](#major-3) · [Major 4](#major-4)
- 第 6 章：Minor 原始编号；第 8 章：任务索引；第 10 章：证据与实际记录。
- 第 11–12 章：回复与投稿检查；第 13 章：全局依赖路线；附录 A–H：原文、事实、覆盖索引和记录模板。

'''+s[b:]
# Remove obsolete relational descriptions caused by moving the sections.
s=s.replace('下面先拆解原文，再逐项给出方法','后续逐项给出方法')
s=s.replace('§3.5.3–§3.6.3','本章前述计算与核验部分')
s=s.replace('## v5.6 阅读结构说明','## v5.7 阅读结构说明')
a=s.index('## v5.7 阅读结构说明');b=s.index('## 当前研究状态与结案边界',a)
s=s[:a]+'''## v5.7 阅读结构说明

四个 Major 的正文已采用相同八段顺序。每个物理问题的完整推导在一个权威位置；跨专题只交代调用模块的输入、输出和假设。Major 1 与 Major 2 共享同点谱和耦合，Major 3 与 Major 4.1 共享 PMNS 证据但独立回复；Minor 保留原始编号，具体定量方法放回对应条目。实际计算日志和数据可外置，理解物理与执行方法不依赖它们。

### v5.7 主要校核与增补

- 固定旋转、场成分标签与质量排序；修正近简并分支和传播子树级混合项，附录数值覆盖质量差两侧。
- 区分 BR 归一化与通道完备性；修正无色 VLL 的胶子融合表述和 $ee$/$\\tau\\tau$ 引文释义。
- 明确固定最小模型的 PMNS 障碍；补充允许算符、矩阵结构、Takagi/SVD 与扩展拟合方法。
- 补充 UV Yukawa—混合—$v_S$ 条件性界、两种动能混合定义，以及从匹配/电流到误差/事件率的实际方法。
- 增加证据检查的 N/A 规则；修复公式控制字符、版本称谓、Statement 来源和失效引用。

'''+s[b:]
# Correct heading levels in the quick-reference appendix.
s=re.sub(r'^## (G\.\d+ )',r'### \1',s,flags=re.M)
s=re.sub(r'^### (G\.\d+\.\d+ )',r'#### \1',s,flags=re.M)
# Fix minor accidental wording and put prerequisites within the topic.
s=s.replace('可分为三层','可分为四层') if '可分为三层' in s and '| D |' in s else s
target=ROOT/'审稿意见-gpt'/'审稿意见分析v5.7-物理校核与专题连续阅读版.md'
target.write_text(s,encoding='utf-8')
(ROOT/'work/section_map.json').write_text(json.dumps(mp,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(target),'chars':len(s),'moved_sections':len(nodes)},ensure_ascii=True))
