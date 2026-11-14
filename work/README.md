# v5.7 历史工作区

此目录包含 2026-10-20 前后 v5.7 整理的中间稿、生成脚本和历史验证输出，不是当前任务状态或正式回复信。当前状态见 [PROJECT_STATUS](../PROJECT_STATUS.md)，技术参考主线见 [v5.7 Markdown](../审稿意见-gpt/审稿意见分析v5.7-物理校核与专题连续阅读版.md)。

## 文件分类

- `v57_corrected.md`、`v57_enhanced.md`、`v57_before_reading_flow_adjustment.md`：连续修订的工作稿。
- `v57_reconstructed_1007.md`、`v57_reconstructed_1007_final.md`、`v57_reconstructed_1007_fixed.md`：重建及其修订副本；文件名中的 `final` 是当时版本名称，不表示当前权威版本。
- `revise_v57.py`、`enhance_v57.py`、`structure_v57.py`、`polish_v57.py`、`reconstruct_v57_1007.py`：历史文本变换脚本；`structure_v57.py` 和 `polish_v57.py` 会写入当前技术参考路径，**不要在现有工作树直接运行**。要研究历史脚本，应先使用隔离副本并检查所有输入与输出路径。
- `validate_v57.py`、`markdown_qa.cjs`：历史检查脚本；`validate_v57.py` 会覆盖 `work/validation.json`。
- `correction_log.json`、`section_map.json`、`validation.json`：对应历史变换和检查记录；不能证明当前文档或物理计算通过验收。

保留原路径是因为脚本通过 `work/` 和仓库根目录定位输入输出。临时构建目录可由 `.gitignore` 排除；它们不同于本目录内已跟踪的历史材料。
