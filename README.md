# Axial-vector model: manuscript revision and referee response

> **Mandatory project rule:** before every task in this repository, read [AGENTS.md](AGENTS.md). For referee-response work, the authoritative writing rules and the separate internal manuscript-change checklist are linked below.

本仓库用于整理轴矢量 \(U(1)_{L_\mu-L_\tau}\) 模型论文的审稿意见、论文修订、计算核查和回复信。资料包括论文与审稿报告基线、Overleaf 源码、逐条回复工作稿、会议记录和专题研究证据。

## 快速入口

- [仓库结构与文件管理说明](docs/repository-management/README.md)：目录职责、迁移原则和导航。
- [逐文档审查标准](docs/repository-management/DOCUMENT_REVIEW_STANDARD.md) 与 [文档审查登记表](docs/repository-management/DOCUMENT_AUDIT_REGISTER.csv)：逐份记录审查状态；未审查文件不会标记为通过。
- [GitHub Actions 工作流索引](.github/workflows/README.md) 与 [工作流审查登记表](.github/workflows/WORKFLOW_AUDIT_REGISTER.csv)：109 个工作流按物理专题分类，并逐份记录触发条件、权限和输出行为；目前 34 个完成静态审查，16 个标记为历史候选，59 个待审查。

- [Git 合并策略与科研提交历史规范](GIT_MERGE_POLICY.md)：实质性科研 PR 默认采用 Merge Commit。

- [项目入口与阅读说明](README-先读这里.md)
- [PROJECT_STATUS.md](PROJECT_STATUS.md)：当前项目阶段、权威文件、开放 PR 和下一步；每次启动先读。
- [研究决策与不可回退事项（动态登记表）](审稿意见-gpt/项目规范/研究决策与不可回退事项.md)：记录当前研究立场和变更历史，可随作者最新明确观点修订。
- [审稿回复信与论文修改清单写作规范](审稿意见-gpt/写作规范/审稿回复写作原则.md)：本项目每次处理回复信前必须阅读；严格区分审稿人可见的正式回复信与内部正文同步清单。
- [论文正文待同步修改清单（2026-11-03）](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)：只记录内部正文修改位置、状态和前后对照，不进入正式回复信。
- [仓库分类索引](仓库分类索引.md)：按专题查找研究记录、计算脚本和历史材料。
- [当前执行目录](审稿意见-gpt/当前执行/README.md)：查看任务、修订材料及后续工作。
- [v5.6 执行手册](审稿意见-gpt/当前执行/审稿意见分析与执行手册_v5.6-主分析全任务映射与原子步骤版-20261019.md)：查看任务 ID、依赖和验收条件；其中 2026-10-27 状态段是历史快照，最新状态以 PROJECT_STATUS.md 为准。
- [v5.7 技术参考](审稿意见-gpt/审稿意见分析v5.7-物理校核与专题连续阅读版.md)：查阅详细物理分析。
- [计算资料索引](计算脚本/README.md)：查找脚本、输出和审计记录。

## 论文与审稿材料

- [论文基线 PDF](axial_vector_model_building-v6.pdf) 和 [原始审稿报告](dw13678_report_1_a.pdf)。
- [Overleaf 源码归档](overleaf-source/axial-vector-model-building-v6/)：包含 `main.tex`、`main-v1.tex` 至 `main-v6.tex`、参考文献数据库、图表及随源包提供的回复信材料。编译时请将该目录作为项目根目录，并在 Overleaf 选择所需主文文件。当前环境尚未完成该归档的完整编译验证；两张较大的图经过 PDF 重新编码。
- [面向审稿人的正式回复信源文件（2026-11-04）](Replies_to_Referee_3_referee_facing_2026-11-04.tex)：当前 main 唯一权威回复信，PR #38 已合并。该文件只保留审稿人需要看到的科学论证；正文同步任务、状态和前后对照统一记录在[内部论文正文待同步修改清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)，不写入正式回复信。
- [2026-10-28 回复信副本](Replies_to_Referee_3_referee_facing_2026-10-28.tex)：历史副本，仅用于版本追溯，不作为当前回复信主线。
- [内部回复信工作稿（2026-10-27）](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Replies_to_Referee_3_revised_working_2026-10-27.tex) 和 [论文修改 Diff](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/axial_vectorv6-diff-v2.4-PMNS-scope-2026-10-27.md)：保留为内部工作副本和正文修订方案；正式提交前须与实际主文和计算证据逐项核对。
- [会议记录](审稿意见-gpt/会议记录/2026-10-23/README.md)：包含会议观点总结及四份文字稿。

## 研究范围与状态

- [Major Point 1 一圈 Higgs–singlet 混合计算](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Higgs_portal_exact_mass_eigenstate_one_loop_2026-10-27.md)：提供两组 benchmark 的计算说明、Python 脚本和验证记录；[状态与后续任务](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Major_Point_1_scalar_response_status_2026-10-27.md)。这些结果保留匹配条件、完整极点方案及实验重铸的适用边界。

当前研究立场和适用条件见[研究决策动态登记表](审稿意见-gpt/项目规范/研究决策与不可回退事项.md)，作者最新明确观点优先于旧记录。研究记录、候选计算和正文修改方案的存在不等于相应任务已完成；最新状态以 PROJECT_STATUS.md 为准，物理结论仍须回到专题证据。
