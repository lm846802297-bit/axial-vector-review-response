# Major 4.2：动能混合和暗光子比较验证记录

日期：2026-11-04。基线：main `a78250e335452f8e72abccb67e1acd4a225b3896`。本记录覆盖指定等混合、配对重阈值简并、重 VLL 匹配尺度零独立局域系数及 NA64 代表质量点比较；不代表完成全 UV 参数空间或 detector-level 实验重铸。

## 0. 本轮追加修改状态

- 回复 TeX 已追加显式边界条件 \(\epsilon_{\rm ind}(\mu_{\rm match})=0\)，并明确它只约束独立局域项，不令完整 \(\epsilon_{\gamma A'}(q^2)\) 恒为零。
- NA64 对照从单一 100 MeV 数量级比较扩展到 10、100、200、300 MeV 四点；300 MeV 显式计入 dimuon 宽度并使用 \(\epsilon_{\rm eff}=|\epsilon|\sqrt{\mathrm{Br}_{\rm inv}}\)。
- NA64 Fig. 3 没有机器可读数表；四点实验边界为公开 PDF 的 log-log 图手工视觉读取区间，约 0.2--0.3 dex 读图不确定度，使用区间下边缘作保守比较。它不是精确数据表，也不是 detector-level recast。
- 当前分支中的回复 PDF 尚未根据本次新增 TeX 重新编译；此前记录的 PDF 页数、版面与编译日志仅对应上一次 TeX 快照，不能作为本次修改已编译验收的证据。

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
- 实读 [NA64 arXiv:2307.02404](https://arxiv.org/pdf/2307.02404) 的产生机制说明，并渲染 PDF 第 3 页 Fig. 3 核对坐标和 90% CL 图注。由 log-log 图手工读取 10、100、200、300 MeV 四点的 90% CL 边界区间，读图误差约 0.2--0.3 dex；区间下边缘用于保守比值。没有把单点 10⁻⁴ 当成全质量统一限制，也没有声称有官方机器可读曲线数据。
- NA64 图的电子顶点为矢量电磁流 e epsilon；本模型诱导电子顶点相同。直接轴矢量缪子产生由另一个 NA64_mu 观测量约束，不能混称。
- Br_inv 估计采用两味带荷轻中微子的领先总宽度 g_X²m_A′/(12π)，电子宽度含电子质量阈值因子；在 300 MeV 还加入直接轴矢量 dimuon 宽度。10、100、200 MeV 的 Br_inv≈1；300 MeV 得到 Gamma_mumu/Gamma_nunu=0.35756、Br_inv=0.736615。PMNS 旋转在轻子混合可忽略时不改变包含所有轻中微子末态的总宽度。
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
| 200 MeV 在壳模除以 g_X | 1.8164335795×10⁻⁶ |
| 212 MeV 在壳模除以 g_X | 2.1197757126×10⁻⁶ |
| 300 MeV 在壳模除以 g_X | 1.7446095791×10⁻⁶ |
| 300 MeV 相对零动量模长 | 1.2088988688 |
| 100 MeV 的 Gamma_ee/Gamma_nunu | 2.0461375871×10⁻¹³ |
| 300 MeV 的 Gamma_mumu/Gamma_nunu | 0.3575620104 |
| 300 MeV 的 Br_inv | 0.7366146020 |
| 10、100、200、300 MeV 的 NA64 epsilon_lim 视觉区间 | (0.8–2.0)×10⁻⁵、(0.5–1.2)×10⁻⁴、(0.7–1.8)×10⁻⁴、(1.0–2.5)×10⁻⁴ |
| g_X=0.1 四点 epsilon_eff/保守 NA64 下边缘 | 1.8045×10⁻²、2.9877×10⁻³、2.5949×10⁻³、1.4973×10⁻³ |
| g_X=0.1 四点产额比 | 3.2562×10⁻⁴、8.9265×10⁻⁶、6.7335×10⁻⁶、2.2420×10⁻⁶ |
| g_X=1 最不利点（10 MeV）的 epsilon_eff/保守下边缘及产额比 | 0.18045 / 0.03256 |
| 300 MeV 次级正电子共振能量 | 88.06 GeV；高于约 50 GeV 缺失能选择，NA64 已发表曲线包含该产生机制 |

数学精度不等于实验输入精度。输出比值只对应记录的参考尺度和相同接受度，不是新的实验信赖区间。

## 4. 内容和编译检查

- 27 段审稿人 `quote` 环境逐段与 main 基线一致。
- Major 2 与 Major 3 正文逐字保持不变；Major 4.3 仅修正 g_X 上限和归一化的句子。
- 34 个引用键均存在；4 个标签唯一，交叉引用可解析。无需新增 bibliography 条目。
- 归档 `overleaf-source` 目录无差异；原论文待按 [K-01–K-05](Major4.2-暗光子限制与论文修改对照_2026-11-04.md) 同步。
- 上一轮 `latexmk` 退出码 0、45 页 PDF 和第 25–28 页视觉检查，均对应本次 TeX 扩展之前的快照；本轮新增的匹配尺度句子和质量依赖 NA64 表尚未重新编译、尚未完成 PDF 视觉检查。不得将上一轮无 warning 的日志当作本轮编译证据。
- 本轮用独立的 mpmath 计算在 35 和 55 位工作精度下复算 10、100、200、300 MeV 的 loop 模长、Br_inv 和 NA64 比值；两种精度结果在所报告有效数字内一致。脚本已扩展相同计算入口，仍需在可执行仓库环境中运行脚本并核对生成 JSON 与提交版本。
- 按审稿回复写作原则复核新增内容：显式写出 \(\epsilon_{\rm ind}(\mu_{\rm match})=0\)；区分局域匹配项与非零物理圈图函数；给出四个质量点、阈值上方的 dimuon 分支比、NA64 视觉读图区间和保守下边缘比值；明确这是 leading-yield rescaling 而非 detector-level recast。
- 计算脚本的四态和检验在两种重整化尺度下与轻子对表达式相差至多 `2.02e-52`，并核实总矢量耦合和为零。两种精度的积分模长一致；新增共同裸质量阈值估计为 `2.5567e-7 |g_X|`，100 MeV 总量级上界为 `1.7496e-6 |g_X|`。NA64 次级正电子共振能量核对为 9.785 GeV，低于约 50 GeV 缺失能选择。
- 导出的 PDF 与构建文件逐字一致；两个作者本地原始 PDF 不纳入提交。

编译命令：

```powershell
$env:BSTINPUTS=(Join-Path (Get-Location) 'overleaf-source/axial-vector-model-building-v6')+';'
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=work/kinetic/latex-build Replies_to_Referee_3_referee_facing_2026-11-04.tex
pdftoppm -r 75 -png 'work/kinetic/latex-build/Replies_to_Referee_3_referee_facing_2026-11-04.pdf' 'work/kinetic/latex-build/page'
```

临时原始文献 PDF、编译日志、内容检查摘要及页面图在被忽略的 `work/kinetic/latex-build/`；正式源文件、输出 PDF、论证对照、验证记录及计算入口/JSON 纳入仓库。重新编译的 PDF 元数据可能改变二进制哈希，应结合源文件、页面内容和日志核对。
