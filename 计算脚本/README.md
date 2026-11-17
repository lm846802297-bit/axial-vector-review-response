# 计算资料索引

> **当前导航（2026-11-14）：** 下文 2026-10-20 的 v65/v66 “最新版/备份”说法仅记录当时状态，这两份现在均为历史快照；项目当前状态以 [PROJECT_STATUS](../PROJECT_STATUS.md) 为准。Major 2、Major 3 和 Major 4.2 的专题脚本已于 2026-11-17 迁入 `research/`，见下文新入口；原路径不再是当前脚本位置。

原始目录整理日期：2026-10-20；本说明复核日期：2026-11-17。本目录保留不同阶段的脚本、计算输出和审计附件，不能把目录内所有文件都视为同一研究阶段或当前生产入口。

| 位置 | 内容 |
| --- | --- |
| 本目录下原有 `.py`、`.m`、`.fr`、`.csv`、`.json` 等 | 早期推导、模型文件、验算脚本及其输出；保留原位置 |
| `section261/` | 第 261 节工作源码、Mathematica 源码与日志、文稿片段、历史版本生成脚本 |
| `section262/` | 第 262 节工作源码、Mathematica 源码与日志、文稿片段、历史版本生成脚本 |
| [计算输出](计算输出/) | 第 250–262 节交付用复现脚本、检查日志和版本验证记录 |
| [审计结果/DeepSeek66](审计结果/DeepSeek66/) | DeepSeek 第 66 版独立审计报告、复算源码、日志和证据 |
| [整理记录](整理记录/) | 本次迁移前后 SHA-256、原路径与新路径对应关系及整理核验脚本 |

2026-11-14 已对第 250–262 节历史日志及 Mathematica 日志的作用和来源做逐项审查；见 [历史日志审查](../docs/repository-management/LEGACY_LOG_REVIEW_2026-11-14.md)。其中第 259 节明确保留两处文献公式差异，不能把所有 PASS 行解释为与文献完全一致。2026-11-14 本地重跑时，第 260 节前 69 项通过但因逐字比较历史输出（含 Python 版本）而中止；详情和机器可读记录见该报告。

## 常用入口

- [第 262 节 Python 复现脚本](计算输出/section262_reproduce.py)
- [第 262 节 Python 检查输出](计算输出/section262_checks.txt)
- [第 262 节 Mathematica 源码](计算输出/section262_mathematica.wl)
- [第 262 节 Mathematica 检查输出](计算输出/section262_mathematica_checks.txt)
- [DeepSeek 第 66 版独立审计报告](审计结果/DeepSeek66/DeepSeek第66版独立审计-20261020.md)
- [迁移与完整性记录](整理记录/relocation_manifest_20261020.json)

复现时可用本地 Python 执行对应 `sectionNNN_reproduce.py`。第 260 节会调用同目录第 250–259 节脚本，因此交付脚本和历史日志保留在同一个文件夹。

`build_v65.py`、`build_v66.py` 是历史版本生成程序，依赖当时的旧版输入和外部来源。其输出目录引用已调整，但旧输入未重新补齐；它们不是当前重跑入口，请勿用来覆盖最新版。章节工作源码和交付副本可能有换行格式差异。

## 当前与历史入口边界

- **跨专题权威导航：** [research 主索引](../research/MAIN_RESEARCH_INDEX_2026-11-13.md)；实时分支、PR 和开放验收门槛以 [PROJECT_STATUS.md](../PROJECT_STATUS.md) 为准。
- **Major 1 Higgs–singlet / UV–EFT：** 当前研究记录和分阶段验收在 [Major 1 research README](../research/major1-higgs-scalar-mixing-20261109/README.md)。本目录根部保留的 Higgs-portal Mathematica、FeynRules、SARAH 和符号审计脚本是研究证据/工具，不应仅凭文件名或旧版号推断其覆盖了完整 UV–EFT matching、规范完备传播矩阵或物理复极点。
- **Major 2：** 当前脚本和输出位于 [research/major2-parameter-window-20261117/](../research/major2-parameter-window-20261117/README.md)。这是 Fig. 2 显示窗口的精确积分 benchmark，不是完整实验重铸或 UV 扫描。
- **Major 3：** 可选 seesaw/带电轻子诊断位于 [research/major3-neutrino-response-optional-seesaw-20261117/](../research/major3-neutrino-response-optional-seesaw-20261117/README.md)。仅供 Major 3/4.1 回复论证；不代表原论文加入新场，也不代表完成全局拟合。
- **Major 4.2：** 动能混合脚本和输出位于 [research/major4-2-kinetic-mixing-20261117/](../research/major4-2-kinetic-mixing-20261117/README.md)。NA64 对照是条件性 leading-yield 比较，不是 detector-level recast。
- **Section 250–262 与 DeepSeek66：** `section261/`、`section262/`、`计算输出/`、`审计结果/DeepSeek66/` 是历史推导、版本检查和复核材料。它们可用于追溯公式和复现相应局部检查，但不是当前论文模型所有计算的统一入口；Section 259 的文献差异、Section 260 的版本敏感输出比较，以及 Section 261/262 的日志溯源边界均应连同审查报告阅读。
- **历史版本生成脚本：** `build_v65.py`、`build_v66.py` 只保留旧版生成逻辑和依赖关系，不得作为当前文稿构建或物理结果更新程序。

## 文件保留与路径说明

旧工作空间说明曾称根目录保留主文档第 66 版和第 65 版备份；这两份主文档并不在当前 Git 仓库树中，因此该句不能作为本仓库文件存在或版本状态的依据。当前仓库仅保留 `section261/build_v65.py`、`section262/build_v66.py` 两个历史版本生成脚本及 DeepSeek66 历史审计材料；它们依赖旧输入，不是当前生产计算入口。

旧路径 `工作空间/计算输出/…` 对应 `工作空间/计算脚本/计算输出/…`；旧路径 `工作空间/审计结果/…` 对应 `工作空间/计算脚本/审计结果/…`。主文档和历史验证记录中的原路径保留为当时记录，可按此映射查找。

审计报告中的本地附件链接已更新，证据元数据中的报告哈希随之更新；数值输出、复现代码和历史检查日志保持原字节。本次整理核验文件完整性与链接，没有重新运行物理计算。

审计报告还保留了对外部 DeepSeek 目录的原始引用。其中 `work/tsk2_b0.m` 在整理时未找到，属于外部引用缺失，未更改或补造该文件；各外部链接的存在状态记录在迁移核验结果中。
