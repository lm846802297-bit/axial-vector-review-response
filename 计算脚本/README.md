# 计算资料索引

整理日期：2026-10-20。后续计算脚本、计算输出及审计附件统一存放在本目录下。

| 位置 | 内容 |
| --- | --- |
| 本目录下原有 `.py`、`.m`、`.fr`、`.csv`、`.json` 等 | 早期推导、模型文件、验算脚本及其输出；保留原位置 |
| `section261/` | 第 261 节工作源码、Mathematica 源码与日志、文稿片段、历史版本生成脚本 |
| `section262/` | 第 262 节工作源码、Mathematica 源码与日志、文稿片段、历史版本生成脚本 |
| [计算输出](计算输出/) | 第 250–262 节交付用复现脚本、检查日志和版本验证记录 |
| [审计结果/DeepSeek66](审计结果/DeepSeek66/) | DeepSeek 第 66 版独立审计报告、复算源码、日志和证据 |
| [整理记录](整理记录/) | 本次迁移前后 SHA-256、原路径与新路径对应关系及整理核验脚本 |

## 常用入口

- [Major Point 4.4 轴矢量恒星冷却研究报告](../审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-28/Major_Point_4_4_stellar_cooling_axial_recast_2026-10-28.md)
- [恒星冷却解析宽度与分支比复现脚本](stellar_cooling_axial_recast.py)：仅验证树级衰变宽度与分支比，不计算超新星排除曲线。
- [半康普顿轴矢量振幅与极化分辨脚本](stellar_semi_compton_axial_matrix_element.py)：计算真空树级 μγ→μA′ 矩阵元、检查光子 Ward identity，使用精确实验室/CM 相空间公式，并加入 Klein–Nishina 解析基准测试；不包含 SN profile 或输运。
- [半康普顿热产生率原型](stellar_semi_compton_thermal_rate.py)：对均匀介质单元积分 μ±γ→μ±A′ 产生率与能量发射率，包含初态分布和末态 μ 子 Pauli 阻塞；运行 `python stellar_semi_compton_thermal_rate.py --check` 可执行几何与低阶积分 smoke test。该原型不是 SN profile/transport 求解器。

- [第 262 节 Python 复现脚本](计算输出/section262_reproduce.py)
- [第 262 节 Python 检查输出](计算输出/section262_checks.txt)
- [第 262 节 Mathematica 源码](计算输出/section262_mathematica.wl)
- [第 262 节 Mathematica 检查输出](计算输出/section262_mathematica_checks.txt)
- [DeepSeek 第 66 版独立审计报告](审计结果/DeepSeek66/DeepSeek第66版独立审计-20261020.md)
- [迁移与完整性记录](整理记录/relocation_manifest_20261020.json)

复现时可用本地 Python 执行对应 `sectionNNN_reproduce.py`。第 260 节会调用同目录第 250–259 节脚本，因此交付脚本和历史日志保留在同一个文件夹。

`build_v65.py`、`build_v66.py` 是历史版本生成程序，依赖当时的旧版输入和外部来源。其输出目录引用已调整，但旧输入未重新补齐；它们不是当前重跑入口，请勿用来覆盖最新版。章节工作源码和交付副本可能有换行格式差异。

## 文件保留与路径说明

工作空间根目录保留主文档第 66 版（当前最新版）和第 65 版（备份），本次整理不改变二者内容。外部 DeepSeek 文档及资料库不作修改。

旧路径 `工作空间/计算输出/…` 对应 `工作空间/计算脚本/计算输出/…`；旧路径 `工作空间/审计结果/…` 对应 `工作空间/计算脚本/审计结果/…`。主文档和历史验证记录中的原路径保留为当时记录，可按此映射查找。

审计报告中的本地附件链接已更新，证据元数据中的报告哈希随之更新；数值输出、复现代码和历史检查日志保持原字节。本次整理核验文件完整性与链接，没有重新运行物理计算。

审计报告还保留了对外部 DeepSeek 目录的原始引用。其中 `work/tsk2_b0.m` 在整理时未找到，属于外部引用缺失，未更改或补造该文件；各外部链接的存在状态记录在迁移核验结果中。
