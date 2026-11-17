# Axial-vector model: manuscript revision and referee response

> **Mandatory project rule:** before every task in this repository, read [AGENTS.md](AGENTS.md). For referee-response work, the authoritative writing rules and the separate internal manuscript-change checklist are linked below.

本仓库用于整理轴矢量 \(U(1)_{L_\mu-L_\tau}\) 模型论文的审稿意见、论文修订、计算核查和回复信。资料包括论文与审稿报告基线、Overleaf 源码、逐条回复工作稿、会议记录和专题研究证据。

## 快速入口

- [仓库结构与文件管理说明](docs/repository-management/README.md)：目录职责、迁移原则和导航。
- [逐文档审查标准](docs/repository-management/DOCUMENT_REVIEW_STANDARD.md)、[462 份基线文档登记表](docs/repository-management/DOCUMENT_AUDIT_REGISTER.csv) 与 [146 份补充文档登记表](docs/repository-management/SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv)：当前 Git 树共有 608 份 Markdown/text 文件（509 `.md`、99 `.txt`）；原始 462 份基线已逐份审查；新增 146 份已入补充台账，其中 140 份 PASS_WITH_NOTES、6 份 HISTORICAL、0 份 PENDING、0 份 REVISION_REQUIRED。基线登记表保留审查时指纹，并记录当前指纹状态为 373 MATCH_CURRENT、88 CONTENT_FINGERPRINT_DIFFERS 和 1 SIZE_METADATA_DIFFERS；这些差异作为历史审查版本指纹予以保留；全部当前 blob/size 元数据与 Git 树一致。详见[最终集成审查](docs/repository-management/FINAL_INTEGRATION_REVIEW_2026-11-17.md)及[活动专题脚本迁移审查](docs/repository-management/ACTIVE_SCRIPT_RELOCATION_AUDIT_2026-11-17.md)。

> **2026-11-17审查状态：** 原始基线 462/462 已审查（304 PASS_WITH_NOTES、2 PASS、156 HISTORICAL、0 REVISION_REQUIRED、0 PENDING）；补充台账另有 146 份新增文本文件，其中 140 份 PASS_WITH_NOTES、6 份 HISTORICAL、0 份 PENDING、0 份 REVISION_REQUIRED。第六十九轮完成最后 54 份基线文件审查；第七十五轮将三个明确归档的历史变体重新分类为 HISTORICAL；第七十六轮确认 B.16 escape-phase-space runbook 与 10 MeV Fig. 7 local-rate audit 两项基线问题仍需实质修复；第八十九轮将 Global-02 报告中无依据的 1140 次计数更正为汇总 JSON 记录的 1080 次，基线待修复项降至 7 条，但全局高阶收敛仍未通过。完成了受限的 10 MeV 局域速率/逃逸相空间与 PR52 归档完整性诊断，但没有更新生产轴矢量约束；Fig. 7 物理偏差仍未解决。相关报告见[第六十九轮报告](docs/repository-management/SIXTY_NINTH_REVIEW_FINAL_54_DOCUMENT_AUDIT_2026-11-16.md)、[端点积分修复报告](docs/repository-management/SIXTY_SIXTH_REVIEW_MAJOR1_ENDPOINT_QUADRATURE_2026-11-16.md)、[第七十五轮报告](docs/repository-management/SEVENTY_FIFTH_REVIEW_BASELINE_ARCHIVE_RECLASSIFICATION_2026-11-17.md)和[第七十六轮报告](docs/repository-management/SEVENTY_SIXTH_REVIEW_B16_ESCAPE_AND_FIG7_FOLLOW_UP_2026-11-17.md)和[第八十九轮报告](docs/repository-management/EIGHTY_NINTH_REVIEW_P1B_GLOBAL02_REPORT_COUNT_RECONCILIATION_2026-11-17.md)、[第九十轮报告](docs/repository-management/NINETIETH_REVIEW_B16_AND_REPOSITORY_BASELINE_CLOSEOUT_2026-11-17.md)及[7 条基线待修复项行动表](docs/repository-management/REMAINING_BASELINE_REVISION_REQUIRED_ACTION_PLAN_2026-11-17.md)。第七十至八十九轮补充审查报告见[仓库管理文档索引](docs/repository-management/README.md)及[工作流审查索引](docs/repository-management/workflow-reviews/README.md)。
- [GitHub Actions 工作流索引](.github/workflows/README.md) 与 [工作流审查登记表](.github/workflows/WORKFLOW_AUDIT_REGISTER.csv)：118 个工作流按物理专题分类，并逐份记录触发条件、权限和输出行为；目前 103 个完成静态审查，1 个为 ACTIVE，14 个保留为历史候选，0 个待审查。第八十至八十八轮审查见[工作流审查索引](docs/repository-management/workflow-reviews/README.md)。

- [根目录迁移审查](docs/repository-management/ROOT_RELOCATION_AUDIT_2026-11-17.md)；[原始 24 文件审查基线](docs/repository-management/ROOT_FILE_AUDIT_REPORT_2026-11-14.md)：记录 2026-11-14 时根目录 24 个文件的逐项审查，包括权威入口、回复信 TeX/PDF、BibTeX、论文和审稿报告基线及历史工作稿。
- [Git 合并策略与科研提交历史规范](GIT_MERGE_POLICY.md)：实质性科研 PR 默认采用 Merge Commit。

- [项目入口与阅读说明](README-先读这里.md)
- [历史归档总索引](archive/README.md)、[Overleaf 源码归档说明](overleaf-source/README.md)、[审稿意见资料索引](审稿意见-gpt/README.md)
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

- [论文基线 PDF](archive/manuscript-baselines/axial_vector_model_building-v6.pdf) 和 [原始审稿报告](审稿意见-gpt/原始审稿材料/dw13678_report_1_a.pdf)。
- [Overleaf 源码归档](overleaf-source/axial-vector-model-building-v6/)：包含 `main.tex`、`main-v1.tex` 至 `main-v6.tex`、参考文献数据库、图表及随源包提供的回复信材料。编译时请将该目录作为项目根目录，并在 Overleaf 选择所需主文文件。当前环境尚未完成该归档的完整编译验证；两张较大的图经过 PDF 重新编码。
- [正式回复 TeX](Replies_to_Referee_3_referee_facing_2026-11-04.tex) 与 [PDF](Replies_to_Referee_3_referee_facing_2026-11-04.pdf)：最终匹配源/PDF 已由 [GitHub Actions run #43767527054](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43767527054) 独立编译和验收，共 64 页，500,973 bytes，SHA-256 `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819`。原第 43 页 2,253 字符完整图注逐字保留并移至图后正文；第 44/45 页续句分页亦已修复。64 页视觉检查、引用、字体和页边界检查通过。详见 [正式回复信最终排版验收](docs/repository-management/REPLY_LETTER_FINAL_ACCEPTANCE_2026-11-16.md)。这是排版验收，不代表超新星物理结果已验证。
- [2026-10-28 回复信历史源](<archive/reply-letter/versions/Replies_to_Referee_3_referee_facing_2026-10-28.tex>)：历史副本，仅用于版本追溯，不作为当前回复信主线。
- [内部回复信工作稿（2026-10-27）](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Replies_to_Referee_3_revised_working_2026-10-27.tex) 和 [论文修改 Diff](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/axial_vectorv6-diff-v2.4-PMNS-scope-2026-10-27.md)：保留为内部工作副本和正文修订方案；正式提交前须与实际主文和计算证据逐项核对。
- [会议记录](审稿意见-gpt/会议记录/2026-10-23/README.md)：包含会议观点总结及四份文字稿。

## 研究范围与状态

- [Major Point 1 一圈 Higgs–singlet 混合计算](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Higgs_portal_exact_mass_eigenstate_one_loop_2026-10-27.md)：提供两组 benchmark 的计算说明、Python 脚本和验证记录；[状态与后续任务](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Major_Point_1_scalar_response_status_2026-10-27.md)。这些结果保留匹配条件、完整极点方案及实验重铸的适用边界。

当前研究立场和适用条件见[研究决策动态登记表](审稿意见-gpt/项目规范/研究决策与不可回退事项.md)，作者最新明确观点优先于旧记录。研究记录、候选计算和正文修改方案的存在不等于相应任务已完成；最新状态以 PROJECT_STATUS.md 为准，物理结论仍须回到专题证据。
