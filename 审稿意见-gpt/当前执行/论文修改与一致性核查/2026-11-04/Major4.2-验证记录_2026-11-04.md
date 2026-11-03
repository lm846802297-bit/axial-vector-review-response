# Major 4.2：动能混合和暗光子比较验证记录

日期：2026-11-04。基线：main `a78250e335452f8e72abccb67e1acd4a225b3896`。本记录验证指定等混合、配对重阈值简并及零独立匹配系数下的圈图估计和实验比较；不代表完成全 UV 参数空间的实验重铸。

## 1. 当前输出的标识

| 文件 | SHA-256 |
|---|---|
| 根目录 `Replies_to_Referee_3_referee_facing_2026-11-04.tex` | `fb8e29c9bf6f1ddf3341cb87c0c9dae4fa541f54cc0b4906feabcdede0d5b887` |
| 同目录回复 PDF（45 页，379014 bytes） | `9863180aebb425a404affc0c817cc7e7fd60ac2229126dda1a2a8a7b7cdc8d` |
| `计算脚本/Major42_kinetic/check_kinetic_dark_photon.py` | `0faf9cdf513a9d91bce6d7f603c50a9caa4b5f0e0c253377d4baa079dd4bf9b9` |
| `计算脚本/Major42_kinetic/outputs/kinetic_dark_photon_2026-11-04.json` | `d190941cb30a9b60415cbf1e9b616bc6a5d6275773f787e849a77dc739aae72d` |

输入、复数积分实部/虚部、模长、比较比值及源文件哈希均写入 [JSON 输出](../../../../计算脚本/Major42_kinetic/outputs/kinetic_dark_photon_2026-11-04.json)。Major 2/3 的旧哈希和页数作为各自 PR 的历史快照保留，不表示当前 PDF 的状态。

## 2. 文献与物理映射

- 实读 [Hapitas et al. arXiv:2108.12440](https://arxiv.org/pdf/2108.12440) Eq. (2.3)、(2.4)，确认独立匹配系数与动量依赖；本模型替换 g_mu-tau→g_X sin²theta_R，再作 timelike 解析延拓。
- 实读 [NA64 arXiv:2307.02404](https://arxiv.org/pdf/2307.02404) 的产生机制说明，并渲染 PDF 第 3 页 Fig. 3 核对坐标和 90% CL 图注。100 MeV 附近采用 10⁻⁴ 数量级作为比较尺度；未将该尺度标成精确数字化限值或全质量统一上限。
- NA64 图的电子顶点为矢量电磁流 e epsilon；本模型诱导电子顶点相同。直接轴矢量缪子产生由另一个 NA64_mu 观测量约束，不能混称。
- Br_inv 估计采用两味带荷轻中微子的领先总宽度 g_X²m_A′/(12π)，电子宽度含电子质量阈值因子；m_A′<2m_mu 且新道关闭。PMNS 旋转在轻子混合可忽略时不改变包含所有轻中微子末态的总宽度。
- g_X=0.1 为归一化示例；g_X=1 是绘图矩形上端。未将示例的大耦合点称作通过所有约束的物理点。

## 3. 数值复算

仓库根目录执行：

```powershell
python '计算脚本/Major42_kinetic/check_kinetic_dark_photon.py'
```

环境：Python 3.14.7，mpmath 1.3.0。积分实部在对数零点处分段；虚部用 log(D−i0) 的分支解析积分。分别以 35 和 55 位精度运行，输出保留的 18 位有效数字上的各点模长一致。

| 检查量 | 结果 |
|---|---|
| epsilon(0) 的模除以 g_X | 1.4431393924×10⁻⁶ |
| 100 MeV 在壳模除以 g_X | 1.4938656690×10⁻⁶ |
| 212 MeV 在壳模除以 g_X | 2.1197757126×10⁻⁶ |
| 212 MeV 相对零动量模长 | 1.4688641470 |
| 原回复的 9 个在壳表格点 | 10、100、200、212、500 MeV 及 1、3、10、100 GeV 均重现原表有效数字 |
| 100 MeV 的 Gamma_ee/Gamma_nunu | 2.0461375871×10⁻¹³ |
| g_X=0.1，相对 10⁻⁴ 参考尺度的混合比/产额比 | 1.4938656690×10⁻³ / 2.2316346371×10⁻⁶ |
| g_X=1，相对 10⁻⁴ 参考尺度的混合比/产额比 | 1.4938656690×10⁻² / 2.2316346371×10⁻⁴ |

数学精度不等于实验输入精度。输出比值只对应记录的参考尺度和相同接受度，不是新的实验信赖区间。

## 4. 内容和编译检查

- 27 段审稿人 `quote` 环境逐段与 main 基线一致。
- Major 2 与 Major 3 正文逐字保持不变；Major 4.3 仅修正 g_X 上限和归一化的句子。
- 34 个引用键均存在；4 个标签唯一，交叉引用可解析。无需新增 bibliography 条目。
- 归档 `overleaf-source` 目录无差异；原论文待按 [K-01–K-05](Major4.2-暗光子限制与论文修改对照_2026-11-04.md) 同步。
- `latexmk` 退出码 0，生成 43 页 PDF；最终 TeX 日志无 warning、undefined reference/citation、overfull 或 underfull box。
- 按审稿回复写作原则复核 Major 4.2：先给出结果；显式推出轻/重态矢量耦合及四态真空极化；分开说明独立匹配项、重阈值与轻子环；量化共同裸质量下残余阈值；交代 NA64 电子顶点、隐形分支、中微子味旋转和参考质量处的产生运动学；结论限定于所写条件。
- 复编译后为 45 页；检查第 25–28 页布局，新增公式、阈值估计、分支比和实验比较没有裁切或重叠。最终 TeX 日志无警告、未定义引用或 overfull/underfull box。
- 计算脚本的四态和检验在两种重整化尺度下与轻子对表达式相差至多 `2.02e-52`，并核实总矢量耦合和为零。两种精度的积分模长一致；新增共同裸质量阈值估计为 `2.5567e-7 |g_X|`，100 MeV 总量级上界为 `1.7496e-6 |g_X|`。NA64 次级正电子共振能量核对为 9.785 GeV，低于约 50 GeV 缺失能选择。
- 导出的 PDF 与构建文件逐字一致；两个作者本地原始 PDF 不纳入提交。

编译命令：

```powershell
$env:BSTINPUTS=(Join-Path (Get-Location) 'overleaf-source/axial-vector-model-building-v6')+';'
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=work/kinetic/latex-build Replies_to_Referee_3_referee_facing_2026-11-04.tex
pdftoppm -r 75 -png 'work/kinetic/latex-build/Replies_to_Referee_3_referee_facing_2026-11-04.pdf' 'work/kinetic/latex-build/page'
```

临时原始文献 PDF、编译日志、内容检查摘要及页面图在被忽略的 `work/kinetic/latex-build/`；正式源文件、输出 PDF、论证对照、验证记录及计算入口/JSON 纳入仓库。重新编译的 PDF 元数据可能改变二进制哈希，应结合源文件、页面内容和日志核对。
