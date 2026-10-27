# 轴矢量模型 v6：统一研究工作与论文修改 Diff v2.4（PMNS 范围收窄与一致性版）

> **文档性质：** 作者内部研究计划与论文修改对照文件，不随正式回复信提交。
>
> **研究对象：** *An Axial $U_A(1)_{L_{\mu-\tau}}$: UV Completion and Experimental Searches*，当前可核查原稿为 `axial_vector_model_building-v6.pdf`。
>
> **当前对照文件：** 回复信工作稿 `Replies_to_Referee_3_revised_working_2026-10-27.tex`；会议记录归档见 [PR #11](https://github.com/lm846802297-bit/axial-vector-review-response/pull/11)。本文件所列正文改动仍是修改方案，不代表已经写入主论文。
>
> **状态原则：** 只有计算/文献核查、结果复核、正文修改与回复信表述全部一致后，才能将相应意见标为闭环。原始 v6 源稿与 PDF 保持不变；已基于用户上传的 Source ZIP 创建独立 Route B 修订副本并完成干净 LaTeX 编译。当前编译产物为 35 页，未发现未定义引用或文献；哈希、编译命令及警告对照记录见 `routeB_manuscript_revision_status_2026-10-27.md`。本次只关闭 PMNS 范围限定对应的正文文本工作，不代表 PMNS 已解决，也不代表 Diff v2.4 的其他计算/重铸任务已完成。
>
> **当前回复信文件与状态边界：** 当前对照文件是 `Replies_to_Referee_3_revised_working_2026-10-27.tex`，仍含其他粗体占位符，是内部工作稿而非可提交版本。Major Point 3/4.1 的范围限定已同步到独立修订副本；该副本编译后对应 Sec. II.A.1、Eqs. (11)–(12)，以及 Abstract、Sec. I 和 Sec. V。PMNS 仍未由最小模型解释；其余未完成计算/重铸及其他回复占位符继续开放。
>
> ## 本轮一致性核查结论
>
> 1. **Minor Point 1 / 6.1：** 原始 v6 源稿仍以 “Light neutral spin-one bosons ...” 开头；独立 Route B 修订副本已将其改为 “Neutral spin-one bosons ...” 并成功编译。回复信的 Minor 6.1 已同步到该修订副本；原始源稿保持不变。
> 2. **Minor Point 4：** 当前回复信称已将 “conservative benchmark” 改为 “illustrative small-mixing benchmark”，但 v6 原稿 Eq. (27) 后仍保留 “conservative benchmark”。
> 3. **Minor Point 6.2：** 当前回复信称 Table II 已改为 selected, non-exhaustive summary，但 v6 原稿表题仍为 “Representative upper bounds”。
> 4. **Minor Point 6.3：** 当前回复信包含两篇 Belle II 分析的 spin-0 解释，但 v6 原稿仍称其 published interpretations assume spin-one，并保留 “intermediate scalar-mass region”。
> 5. **Minor Point 6.4 / 6.5：** 回复信给出了网格点定义与 prompt 寿命示例，但当前 v6 正文尚未包含对应的完整定义和适用域分析。
> 6. **Major Point 3 / 4.1：** 已选择“保留现有轴矢量唯象学、收窄论文主张”的路线 B。独立修订副本现已加入 Weinberg 算符选择规则、残余 $Z_2$、分块质量矩阵和范围限定，并通过干净编译；Major 3/4.1 回复引用已同步到 Sec. II.A.1、Eqs. (11)–(12)。T-01 的正文/回复一致性文本工作已完成，但 PMNS 仍未解决，其他 Diff 任务保持开放。
> 7. **Major Point 1.3 与 Major 4.4：** 当前正式回复信明确承认圈级混合的完整定量判断和轴矢量 benchmark 的超新星重铸尚未完成。v2.2 中把当前回复信描述为“声称已完成但仍有结果占位符”的文字过时，不能继续沿用。
> 8. **Major Point 2 / 4.2–4.3：** 绘图窗口、纯轴极限、VLL 有限混合、动能混合与 UV–EFT 截断误差必须分别判断。T-06、T-07、T-09、T-13、T-14 仍保持开放。
>
> 本文件的一致性核查只更新任务状态说明与核对规则；不代表任何物理计算、实验重铸或论文正文修改已经完成。

## 统一维护规则

1.  **一个任务只有一个状态来源。** 任务状态以本文件的”统一任务登记表”为准；各 Diff 小节描述修改方案，不另行维护互相矛盾的状态。
2.  **研究结论与论文措辞分开验收。** 推导、数值计算、实验适用性/重铸和正文修改是不同交付物；只完成其中一项，不得关闭整个任务。
3.  **保留证据链。** 每项关闭时记录输入版本、假设与参数、方法/代码版本、输出文件或图表、独立核查结果，以及对应的论文位置。
4.  **严格区分物理结论。** “理论上可实现”“在所列约束下未排除”“实验排除”“未评估”和”未来可探测”不可互换。
5.  **正式回复信只写已核实的结果。** 不出现内部工作说明、待办标记或方括号占位符；“we have revised”“we find”“excluded”“allowed”“consistent with PMNS”等陈述必须有相应证据。
6.  **不把绘图窗口当成允许区域。** 一个 benchmark 点通过检查不代表整片参数空间通过检查；实验质量覆盖也不等于对本文模型的排除。
7.  **修改后重新生成引用。** 章节、公式、图表编号、页码和行号均以实际修改后的 LaTeX 源稿及最终 PDF 为准，不手工沿用可能失效的编号。

## 任务执行状态与证据成熟度：双轴记录规则（强制）

本 Diff 与 v5.7 共用同一套证据成熟度定义，但两者追踪对象不同。**不得把工作包是否完成与物理主张是否得到验证合并成一个状态。**

1. **`T-xx` 记录工作包的执行状态。** 本文件的 T-00–T-14 是工作包 ID；T 表中的状态回答“这个工作包做到哪一步、是否被阻塞、是否通过验收”。T-14A 是 T-14 下可提前执行的基准冻结子任务，不是另一个原子审计 ID。
2. **`S0–S7` 记录具体物理主张或证据的成熟度。** 等级定义唯一引用 v5.7 §10.7.1：S0 原文已定位；S1 结构已分析；S2 解析关系已核对；S3 计算已运行；S4 结果已验证；S5 实验已重铸；S6 联合结论已形成；S7 论文/回复已闭环。S0–S7 是证据里程碑，不是任务状态。
3. **一个任务完成，不意味着它关联的所有物理主张都达到最高证据等级。** 必须逐条记录该任务所覆盖的 `claim_id`、每条主张的 `evidence_level`、证据文件/来源和验收结果；不能把任务状态 `已完成` 自动复制成所有关联主张的 S7。
4. **同一个任务可以包含多个证据等级不同的主张。** 例如，原始实验论文的质量覆盖可能已核实，而该实验对本文 UV 模型的适用性仍未评估；应分别记录各自证据等级，不得用一个状态覆盖全部内容。
5. **原子审计 ID 与工作包 ID 永不混用。** v5.7 附录 H 的原子 ID（如 `R-01`、`M1-3a`、`SRC-EQ34-REPORT`）保持原样；本文件使用 `T-xx` 作为工作包编号。交叉映射只表达任务覆盖关系，不表示原子条目已经完成。
6. **不适用必须有理由。** 某项检查若标为 N/A，应记录物理理由、适用条件和支持证据；N/A 不是新的 S 等级，也不能只因工作量较大而使用。

建议每条主张至少记录：`claim_id`、原子审计 ID、关联 `T-xx`、`claim_text`、`evidence_level`、`source_version`、证据路径/文献、独立复核结果、论文落点与更新时间。v5.7 §10.7.1 是 S0–S7 定义的唯一权威来源；本文件不另造一套等级。

## 统一任务登记表（唯一状态源）

下表把原内部工作清单和原 Diff 的强制验收任务合并为同一套任务 ID。状态是现有文档记录的基线，不代表本轮已重新执行计算或验收。

| ID   | 研究任务与关闭条件                                                                                                                                                           | 对应审稿意见                       | 对应论文 Diff          | 主要证据/交付物                                                                           | 当前记录状态     |
|:-----|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------|:-----------------------|:------------------------------------------------------------------------------------------|:-----------------|
| T-00 | 锁定审稿人实际收到的 PDF，并与当前 v6 核对 Eq. (30)/(34) 及相关约定                                                                                                          | Major 1；Minor 6.4                 | Diff 0                 | 投稿版本、逐式对照记录、确认后的约定                                                      | 待完成           |
| T-01 | 落实已选择的路线 B：说明允许/禁止的 Weinberg 算符、残余 $Z_2$、PMNS 结构限制；将同一范围声明同步至 Introduction、模型部分、Conclusion、Major 3 与 Major 4.1；不新增粒子 | Major 3、Major 4.1 | Diff 11 及模型部分 | 正文实际差异、正式回复、Major 3/4.1 逐项一致性核验与编译记录 | **修订副本已应用并编译；范围限定已同步；PMNS 未解决** |
| T-02 | 将 Higgs portal 纳入完整势能，定义重整化条件和尺度，计算轻子/VLL 圈级贡献、阈值及非对角二点函数；正确处理 $m_s\simeq m_h$ | Major Point 1.3 | Diff 2 | 势能与质量矩阵、匹配边界、候选导数项证据边界、近简并极点诊断与约束分类 | **portal 阈值和两个代表点、首轮复数极点已完成；导数匹配闭环、独立图级验证和 Higgs 重铸仍开放** |
| T-03 | 量化标量/Higgs 约束：产生率、总宽度、分支比、寿命、Higgs 信号强度、exotic decays 和适用直接搜索；区分已排除、所考虑约束下未排除、未评估                                      | Major 1、1.1、1.2、1.3；Major 4    | Diff 4、5、6           | 模型特定重铸、假设清单、质量分类图/表、独立复核                                           | 待计算/重铸      |
| T-04 | 核查 Belle II 等标量搜索的原始分析、spin-0 解释、产生/衰变假设及接受度；不能仅凭质量覆盖判为排除                                                                             | Major 1.1、Major 4；Minor 6.2、6.3 | Diff 4A–4C             | 原始分析依据、模型映射、适用性判断及必要的重铸                                            | 待完成           |
| T-05 | 统一 VLL 质量与混合角 benchmark；核对 $m_\ell\simeq\theta_{\ell L}\theta_{\ell R}M_E$、Eq. (22)/(27) 和直接搜索界限；将 benchmark 推论与实验质量下限分开                     | Minor 3、Minor 4                   | Diff 3                 | 精确/近似质量关系、可行参数选择、直接搜索假设和修订理由                                   | 待修改与复核     |
| T-06 | 定量计算动能混合 $\epsilon$，说明匹配尺度、重整化条件、圈图表达式、阈值抵消条件、benchmark 数值与误差                                                                        | Major 4.2                          | Diff 7                 | 推导、参数/尺度记录、数值输出、实验尺度比较                                               | 待计算           |
| T-07 | 评估有限 VLL 质量产生的残余矢量耦合及其与轴矢量约束的差异；将 $g_V^\ell$ 与动能混合 $\epsilon$ 分开分析                                                                      | Major 4.3；Minor 2                 | Diff 7                 | $g_V/g_A$ 的参数依赖、矢量敏感实验比较、对 Fig. 2 的影响                                  | 待重铸           |
| T-08 | 独立核查 $A'$ 的恒星冷却/超新星限制，包括粒子身份、电流结构、质量范围、产生机制及 trapping/escape/decay 假设                                                                 | Major 4.4                          | Diff 8                 | 原始文献、适用性判断、必要重铸及明确的约束分类                                            | 待完成           |
| T-09 | 统一参数域与图表解释：删除或明确定义 “light”（与 Minor 1/6.1 统一）、绘图窗口、派生量、微扰性条件、pure-axial 定义、$v_s$ 参考线、扫描点定义、理论边界、实验排除和未评估区域 | Major 2；Minor 1、2、6.1、6.4、6.6 | Diff 1、5、6、7        | 参数表、图注、质量/耦合范围说明、pure-axial 定义、扫描分类规则和重算后的图表              | 待修改           |
| T-10 | 对四轻子/共振分析逐项核对质量覆盖、总宽度、分支比、寿命和 prompt-decay 判据                                                                                                  | Minor 6.5                          | Diff 9                 | 各实验适用区间、模型宽度/衰变长度计算、prompt 判据                                        | 待计算/修改      |
| T-11 | 决定 muon-collider 部分保留为 illustrative study/outlook，还是扩展为完整 forecast；文字必须与实际计算深度一致                                                                | Minor 5                            | Diff 10                | 明确的研究范围；若做 forecast，则需 luminosity、束流/探测器、背景、接受度和系统误差等假设 | 待决定           |
| T-12 | 将已验证的结果同步到摘要、引言、正文、表格、图注、结论和正式回复信；逐条核对回复信的完成时声明、占位符、实际论文差异与证据是否一致，并核对全部引用与编号                     | 全部意见                           | Diff 1–14；正式回复信  | 最终 LaTeX diff、证据索引、完整编译 PDF、逐条回复—正文—证据核对表                         | 最后执行         |
| T-13 | 验证 UV 参数到低能 EFT 系数的匹配、匹配尺度与算符截断；在相同 UV 输入点比较完整理论与截断 EFT 的振幅/可观测量，量化截断误差，并检查扫描点是否存在满足同一组 UV 条件的实现 | Major 2 及 UV–EFT 对照问题 | Diff 13 | 匹配推导、适用能标、截断误差估计、同点 UV 参数记录、独立核查及正文修改 | 待建立/待验证 |
| T-14 | 汇总同一 UV 输入下的全部相关修正，量化曲线/区域分类变化，并决定保留、局部修正或重算；T-14A 基准冻结可先行，最终关闭需通过相关 T-04、T-09、T-10 及其他适用依赖的结果门槛 | Major 2、3、4.2–4.4；Minor 1、2、6.2–6.6 | Diff 14 | 基准图及输入哈希、比较脚本、逐项影响报告、依赖/ N/A 依据、保留/局部修正/重算决策记录 | 基准冻结待执行（T-14A 可先行） |

### 审稿意见到任务的补充映射

| 审稿意见                                | 统一任务         | 具体要避免的问题                                                                |
|:----------------------------------------|:-----------------|:--------------------------------------------------------------------------------|
| Major 1：标量 $S$                       | T-02、T-03、T-04 | 把微扰性上界直接写成实验允许质量区间；仅凭质量覆盖声称已排除                    |
| Major 1.1：标量可探测性                 | T-03、T-04       | 没有匹配产生率、混合、总宽度、分支比、寿命和接受度就声称有灵敏度                |
| Major 1.2：允许质量范围                 | T-03、T-09       | 不给 benchmark、参数范围和约束清单；把非连通区域写成单一连续区间                |
| Major 1.3：portal 与 Higgs 限制         | T-02、T-03       | 未计算就称混合可忽略；把远离简并区的小角近似外推到 $m_s\simeq m_h$              |
| Major 2：有效参数范围与 UV–EFT 对照     | T-09、T-13、T-14 | 把 Fig. 2 的坐标范围当成完整物理允许域，或未检查 EFT 截断与同点 UV 实现性                                          |
| Major 3、4.1：PMNS                      | T-01             | 未构造并验证中微子质量机制却暗示最小模型已解释振荡                              |
| Major 4.2：动能混合                     | T-06             | 把匹配尺度设定为零等同于实验尺度预测为零                                        |
| Major 4.3：有限 VLL 质量                | T-05、T-07、T-14 | 仅凭 $g_V/g_A$ 小就忽略矢量敏感实验，或未比较对 Fig. 2 的实际影响                                             |
| Major 4.4：恒星冷却                     | T-08             | 把对标量 $s$ 的限制当成对规范玻色子 $A'$ 的限制，或未经论证地判为无关           |
| Minor 1、6.1：light                     | T-09、T-14       | 引言已删除未限定的 “light”；仍须补充绘图范围的物理动机并验证相关参数域                                                  |
| Minor 2：pure axial                     | T-07             | 未在引入质量基底耦合时定义严格纯轴矢量极限                                      |
| Minor 3、4：VLL 与 benchmark            | T-05             | 混淆实验下限、条件性质量关系与人为选取的 benchmark                              |
| Minor 5：muon collider                  | T-11             | 将解析示例写成未来排除/发现灵敏度预测                                           |
| Minor 6.2、6.3：约束表述                | T-03、T-04       | 将 selected/non-exhaustive 表说成全局最强限制；使用未定义的 “intermediate mass” |
| Minor 6.4：point                        | T-09             | 不说明一个点是扫描网格中的 $(m_{A'},g_X)$ 点                                    |
| Minor 6.5：parameter region of interest | T-10             | 不说明具体实验质量区间及 prompt 假设                                            |
| Minor 6.6：$v_s$ 参考线                 | T-09             | 把标量自耦合 benchmark 线误称为 $y_{s\mu\mu}$ 的微扰性界限                      |

### v5.7 附录 H 的 59 个原子审计 ID → T-xx 工作包交叉映射（不改原 ID）

下表覆盖 v5.7 附录 H 的 59 个原子 ID。原子 ID 在 v5.7 中保持不变；本表只把它们路由到本 Diff 的工作包。多个 T 任务可以共同支持一个原子条目，一个 T 任务也可以支持多个原子条目。映射不代表完成：各项仍需按适用的 S0–S7 证据等级逐条验收。对总体评价、Recommendation 和 Statement，映射仅用于最终稿件闭环或归档，不意味着每项都需要新增计算。

| v5.7 原子 ID（原样保留） | v5.7 条目主题 | 关联工作包 | 映射理由 |
|---|---|---|---|
| `R-01` | 开头总体评价-句1 | T-00、T-12 | 模型场内容/异常与版本基线；最终文字和证据闭环。 |
| `R-02` | 开头总体评价-句2 | T-05、T-07、T-09、T-14 | 纯轴矢量极限、有限 VLL 残余矢量耦合及图中适用域。 |
| `R-03` | 开头总体评价-句3 | T-07、T-09、T-13、T-14 | UV 到低能轴矢量唯象的匹配、参数域和稳健性。 |
| `R-04` | 开头总体评价-句4 | T-12 | 正面评价仅归档，不形成独立物理计算任务。 |
| `R-05` | 开头保留意见-句1 | T-12 | 总体验收：每项意见需有纳入/排除决定及证据。 |
| `R-06` | 开头保留意见-句2 | T-12 | Major 事项须由正文和证据回应，不能仅润色回复。 |
| `R-07` | Merits-模型构造 | T-00、T-12 | 核对模型基线，并准确定位文献贡献/新颖性。 |
| `R-08` | Merits-唯象 | T-03、T-04、T-06、T-07、T-08、T-10、T-14 | 正面评价不表示约束集完整；映射到相关实验任务。 |
| `R-09` | Merits-用途 | T-00、T-05、T-09、T-12、T-13 | 确保模型定义、benchmark、参数映射和可复现性。 |
| `R-10` | Major 总引言 | T-01、T-02、T-03、T-04、T-06、T-07、T-08、T-12、T-13、T-14 | 统领 Major 闭环；具体物理主张由相应工作包承接。 |
| `R-11` | Major 总引言-条件语气 | T-00、T-12 | 若是误解仍需通过版本核对、公式/文字澄清来回应。 |
| `M1-00` | Major 1 总述 | T-02、T-03、T-04、T-13、T-14 | UV 标量与 EFT 的逻辑连接、约束和截断误差。 |
| `M1-1` | Major 1.1 | T-02、T-03、T-04、T-13 | 标量产生、衰变、可探测性和 EFT 影响。 |
| `M1-2a` | Major 1.2-问题 | T-03、T-04、T-09、T-13、T-14 | 质量窗口须由同一参数点的理论条件和适用约束共同决定。 |
| `M1-2b` | Major 1.2-示例建议 | T-03、T-09、T-14 | 参数窗口的物理动机和 benchmark 选择。 |
| `M1-2c` | Major 1.2-条件 | T-03、T-04、T-09、T-13、T-14 | 约束清单、联合扫描和区域分类。 |
| `M1-3a` | Major 1.3-树级假设 | T-02、T-03、T-14 | portal 定义、重整化条件和物理混合。 |
| `M1-3b` | Major 1.3-圈图判断 | T-02、T-03、T-14 | 轻子/VLL 圈图、味流和非对角二点函数。 |
| `M1-3c` | Major 1.3-实验推论 | T-02、T-03、T-04、T-14 | 混合存在不自动等于强排除；需做模型映射。 |
| `M1-3d` | Major 1.3-近简并问句 | T-02、T-03、T-14 | 近简并质量矩阵/极点与相关约束。 |
| `M1-3e` | Major 1.3-定量要求 | T-02、T-03、T-14 | 扫描相关标量质量范围并记录证据等级。 |
| `M1-3f` | Major 1.3-Higgs 实验 | T-02、T-03、T-14 | Higgs 与其他限制在一致 UV 输入下比较。 |
| `M1-3g` | Major 1.3-条件性忽略 | T-02、T-03、T-13、T-14 | 需证明目标观测量的 UV–EFT 误差，而不只看混合角。 |
| `M1-3h` | Major 1.3-退耦疑问 | T-02、T-13、T-14 | 分析参数共同缩放与指定观测量下的有效退耦。 |
| `M2-1` | Major 2-主问 | T-09、T-13、T-14 | EFT 可实现域、UV 映射与截断误差。 |
| `M2-2` | Major 2-图2范围 | T-09、T-13、T-14 | 区分绘图窗口、理论边界和实验边界。 |
| `M2-3` | Major 2-微扰性 | T-03、T-05、T-09、T-13、T-14 | UV 微扰性经模型映射传递到 EFT 参数。 |
| `M3-0` | Major 3-开头 | T-01 | 中微子质量机制与 PMNS 一致性。 |
| `M3-1` | Major 3.1 | T-01 | 逐项列出允许/禁止的 Weinberg 算符。 |
| `M3-2` | Major 3.1-对齐 | T-01 | 质量矩阵结构、对角化和 PMNS 非平凡性。 |
| `M3-3` | Major 3.2-右手中微子建议 | T-01 | 若采用 RH neutrino 扩展，核查荷、质量项和异常。 |
| `M3-4` | Major 3.2-代际混合 | T-01 | 代际混合算符、额外场/破缺结构。 |
| `M3-5` | Major 3-结论分支 | T-01、T-12 | PMNS 方案决策和全文/回复信统一。 |
| `M4-0` | Major 4-总问 | T-03、T-04、T-06、T-07、T-08、T-10、T-12、T-14 | 建立实验约束覆盖/适用性总表。 |
| `M4-1` | Major 4.1-中微子 | T-01、T-12 | 复用 Major 3 的同一证据，但单独回应本项。 |
| `M4-2` | Major 4.2-动能混合 | T-06、T-14 | 计算有限质量阈值下 epsilon 并评估图的变化。 |
| `M4-3` | Major 4.3-有限矢量耦合 | T-05、T-07、T-14 | 分开检查 VLL 参数、残余矢量耦合和实验敏感性。 |
| `M4-4` | Major 4.4-恒星冷却 | T-08、T-14 | 核查恒星冷却约束对 A-prime 的适用性。 |
| `m1-1` | Minor 1-参数范围 | T-09、T-14 | 给出参数窗口动机并区分未画出与不允许。 |
| `m2-1` | Minor 2-纯轴矢量定义 | T-07、T-09、T-14 | 在质量基底定义严格纯轴矢量极限。 |
| `m3-1` | Minor 3-VLL 下限 | T-05 | 区分混合角 benchmark 推论与直接搜索下限。 |
| `m4-1` | Minor 4-conservative benchmark | T-05 | 澄清 small-mixing assumption 并核查实验一致性。 |
| `m5-1` | Minor 5-muon collider | T-11、T-12 | 控制对撞机部分的研究定位与最终措辞。 |
| `m5-2` | Minor 5-额外不对称 | T-11 | 记录未计算的极化/末态不对称，不夸大结果。 |
| `m6-1` | Minor 6.1-术语 | T-09 | 删除未定义的 light，并检查范围表述。 |
| `m6-2` | Minor 6.2-术语 | T-03、T-04 | 明确 Table II 是 selected/non-exhaustive，并说明假设。 |
| `m6-3` | Minor 6.3-术语 | T-03、T-04 | 具体质量覆盖、spin-0 解释和模型适用性。 |
| `m6-4` | Minor 6.4-术语 | T-09 | 定义 scan point 并区分理论与实验筛选。 |
| `m6-5` | Minor 6.5-术语 | T-10 | 质量覆盖、总宽度、分支比、prompt 判据。 |
| `m6-6` | Minor 6.6-术语 | T-09 | 解释 v_s 参考线的标量自耦合判据。 |
| `REC-1` | Recommendation-句1 | T-12 | 最终检查所有 Major 工作包、正文落点和证据。 |
| `REC-2` | Recommendation-句2 | T-00、T-12 | 版本核对和消除歧义的正文修改。 |
| `REC-3` | Recommendation-句3 | T-12 | 逐项处理 Minor 意见及其正文/回复闭环。 |
| `REC-4` | Recommendation-句4 | T-01、T-12 | PMNS 是关键门槛；与全文总结保持一致。 |
| `REC-5` | Recommendation-句5 | T-02、T-03、T-04、T-13、T-14 | 标量物理和 UV–EFT 误差的闭环。 |
| `ST-1` | Statement | T-12（仅归档） | 审稿人声明仅归档，不形成物理计算任务。 |
| `SRC-EQ34-REPORT` | 审稿报告中的 Eq. (34) 引用 | T-00、T-09 | 核对送审版本、势能归一化和边界系数。 |
| `SRC-THETA-BENCH` | Major 4.2 与 Minor 2–4 benchmark 来源 | T-05、T-06、T-07、T-09、T-14 | 分开处理 theta、epsilon、g_V/g_A 与图的影响。 |
| `SRC-VS-LINE` | Minor 6.6 的 v_S 参考线来源 | T-09 | 核查该线对应 scalar self-coupling，而非 Yukawa 非微扰界。 |

**映射维护规则：** 若后续修改 T 任务范围，更新此表和 T 任务登记表；不要为了与 T 编号一致而重命名附录 H 的原子 ID。若原子条目与多个 T 任务相关，应保留全部必要映射；若任务对某原子条目不再适用，需记录理由而非静默删除。

### 依赖关系与推荐执行顺序

1.  **版本基线：T-00；并行冻结图基准：R-14A。** 先核对审稿人实际收到的 PDF，锁定 Eq. (30)/(34) 的公式与约定；同时保存当前 Fig. 2、输入参数、约束曲线/来源、脚本和代码版本。冻结只为建立比较基准，不表示图已通过稳健性验证。
2.  **先落实已选的 PMNS 范围限定并核查 benchmark 一致性：T-01、T-05。** 路线 B 已选，但最小模型的 PMNS 结构性问题并未被解决；需将其明确写入正文/回复并同步 Major 4.1。VLL 质量与混合角也需一致。若未来重新考虑引入新的带荷 VEV，必须重新推导 $m_{A'}$ 与 VEV 的关系，并重新检查标量谱和受影响的约束。
3.  **标量扇区：T-02，然后 T-03/T-04。** 先明确 portal 和物理标量谱，再作标量搜索的模型特定判断。Belle II 原始分析核查可并行开展，但最终排除结论必须使用一致的模型输入。
4.  **有限质量与额外约束：T-06、T-07、T-08。** 明确区分动能混合与质量基底中的残余矢量耦合，并独立核查恒星冷却/超新星限制。
5.  **UV–EFT 与基准稳健性：T-13、T-14。** T-13 核对匹配、EFT 截断和同点 UV 实现性；T-14A 可提前冻结 Fig. 2 的原始输入、脚本、数据和哈希，独立建立比较基线。T-14 的最终关闭则必须把所有会影响 Fig. 2 的相关结果放到同一组 UV 输入下比较，至少显式检查 T-04（Belle II 标量分析适用性）、T-09（参数域与图例分类）、T-10（四轻子质量覆盖/宽度/分支比/prompt 条件），以及 T-01/T-02/T-03/T-05/T-06/T-07/T-08/T-13。若其中某项对指定 benchmark 确实不适用，必须给出可复核的物理理由和证据；不能仅凭任务未完成就将其标为 N/A。T-14A 完成不代表 T-14 已关闭。
6.  **参数图和具体分析：T-09、T-10、T-11。** 只有在相应计算和约束适用性明确后，才能定稿图表分类、prompt 区间和对撞机部分的定位。
7.  **全文与回复信：T-12。** 最后同步摘要、引言、正文、图表、结论及回复信，重新生成编号并完成最终验收。

> 依赖顺序不意味着所有任务必须串行。原始文献核查、代码准备和部分独立推导可以并行；但依赖上游物理输入的最终数值结论不能提前定稿。

------------------------------------------------------------------------

# Part I. 科学核查基线与优先级

## 0. 阅读论文后确认的关键事实与修改优先级

### 0.1 当前稿件的实际结构

v6 的核心是：构造 anomaly-free、renormalizable 的 axial $U_A(1)_{L_\mu-L_\tau}$ 规范扇区；通过 $S$ 与 vector-like leptons（VLL）产生带电轻子质量；在 $M_E$ 较大、小轻重混合、$m_s\gtrsim10\,\mathrm{GeV}$ 且忽略 Higgs–singlet 混合的 benchmark 下，将现象学投影到 $(m_{A'},g_X)$ 平面。Fig. 2 是这个**条件性 benchmark 切片**的约束图，不是完整 UV 模型的全局允许区域。

### 0.2 不能跳过的四个科学阻塞项

1.  **PMNS/中微子质量：** 当前最小 UV 构造没有完整的中微子质量机制。按现有荷分配，$S$ 获得 VEV 后保留残余 $Z_2$；维五 Weinberg 算符允许 $ee$ 与 $\mu\tau$ 项，$\mu\mu$ 与 $\tau\tau$ 可分别通过 $S^\dagger/S$ 插入在维六出现，而 $e\mu,e\tau$ 仍被禁止。因此最小构造无法给出观测到的电子味混合。已选择路线 B：不增加新粒子，保留轴矢量唯象学并明确收窄论文主张。该选择不等于证明完整 UV 模型符合中微子振荡；审稿风险仍高，正文修改与 Major 4.1 对齐必须完成。
2.  **标量/Higgs portal：** v6 的 Eq. (28) 只写 $V(S)$，之后直接假设 Higgs–singlet 混合可忽略。规范允许的 $(H^\dagger H)(S^\dagger S)$ 项、重整化边界、轻子/VLL 圈级贡献、近 $m_s\simeq m_h$ 的精确谱与 Higgs 约束必须统一处理。没有计算前不能声称混合很小或 Higgs 约束可以忽略。
3.  **动能混合与有限 VLL 质量：** v6 说明简并 VLL 的一圈阈值贡献相消，并在匹配尺度令动能混合为零；这不等于已定量回答有限质量、有限混合时的 $\epsilon$ 和残余矢量耦合问题。
4.  **实验约束完整性：** Table II 是轻标量 $s$ 的限制，不能替代审稿人问到的规范玻色子 $A'$ 的恒星冷却/超新星约束。BaBar、Belle 和 Belle II 的标量搜索也不能只按质量覆盖直接当成本文模型的排除线。

### 0.3 已可从 v6 直接核对的代数关系

在**单个破缺 VEV、portal 混合可忽略**的基准中， $$
m_{A'}=2g_Xv_s,\qquad m_s^2=2\lambda_Sv_s^2,
\qquad
\lambda_S=\frac{2g_X^2m_s^2}{m_{A'}^2}.
$$ 若采用 $\lambda_S\leq\lambda_S^{\max}$，则 $$
m_s\leq\sqrt{2\lambda_S^{\max}}\,v_s
=\sqrt{\frac{\lambda_S^{\max}}{2}}\frac{m_{A'}}{g_X}.
$$ 取 $\lambda_S^{\max}=4\pi$ 时， $$
m_s\leq\sqrt{8\pi}\,v_s
=\sqrt{2\pi}\frac{m_{A'}}{g_X}.
$$ 因此 $m_s=10\,\mathrm{GeV}$ 的 benchmark 要求 $$
v_s\geq\frac{10\,\mathrm{GeV}}{\sqrt{8\pi}}\simeq1.995\,\mathrm{GeV}.
$$ v6 的 Eq. (30) 与 Eq. (34) 在该约定下代数一致。审稿报告引用的上界系数 $4\pi$ 与当前 v6 在 $\lambda_S^{\max}=4\pi$ 时导出的系数 $8\pi$ 不同；严格或非严格不等号取决于所采用的微扰性判据。必须先确认投稿系统中审稿人实际收到的版本，不能直接指称审稿人错误或擅自改动当前公式。

### 0.4 一个由当前 benchmark 直接导出的内部一致性检查

v6 同时写有 $$
m_\tau\simeq\theta_{\tau L}\theta_{\tau R}M_E,\qquad
|\theta_{\tau L,R}|\le10^{-2}.
$$ 在该近似下，若两个 $\tau$ 混合角都必须不超过 $10^{-2}$，则 $$
M_E\gtrsim\frac{m_\tau}{10^{-4}}\simeq17.8\,\mathrm{TeV}.
$$ 因此仅写 $M_E>10\,\mathrm{TeV}$ 不能保证 Eq. (27) 对两个 $\tau$ 混合角同时成立。建议将 benchmark 下限调整为约 $18\,\mathrm{TeV}$，或重新定义混合角条件；该数值是**由所选混合角 benchmark 推出的条件性理论关系，不是 VLL 直接搜索的实验质量下限**。

------------------------------------------------------------------------

# Part II. 论文修改 Diff：位置、删除/替换/新增文本

以下以 v6 的章节和印刷页码定位。页码、行号和公式编号必须在实际 LaTeX 源稿更新后重新生成；若修改会改变公式编号，应使用 `\label{}` / `\ref{}` 而不是手工沿用旧编号。

## Diff 0 — 版本基线与 Eq. (30)/(34)（先做，不改物理内容）

**位置：** Sec. II.C，Eqs. (28)–(35)，印刷页码 11–13。

**操作：** 暂不直接改公式；先把投稿系统中审稿人收到的 PDF 与当前 v6 对齐。审稿报告引用的上界与当前 v6 的写法不同。锁定版本后，在正文用一行代数关系同时展示两个等价表达式，避免歧义。

**建议新增句（仅在确认当前约定后插入 Eq. (30) 后）：**

> Using $m_s^2=2\lambda_Sv_s^2$ and $m_{A'}=2g_Xv_s$, the perturbativity condition $\lambda_S\leq\lambda_S^{\max}$ can equivalently be written as $m_s\leq\sqrt{2\lambda_S^{\max}}\,v_s=\sqrt{\lambda_S^{\max}/2}\,m_{A'}/g_X$. This is a conditional theoretical bound at fixed $(m_{A'},g_X)$, not an experimental exclusion contour.

**不要做：** 不要在没有确认送审版本的情况下写”审稿人引用错误”；也不要只为了与审稿报告中的系数一致而改变 v6 中彼此一致的公式。

------------------------------------------------------------------------

## Diff 1 — Introduction 开头：删除未定义的 “light”，并与 Minor Point 1 统一

**位置：** Abstract 与 Sec. I 第一段第一句，印刷页码 1、3。

**删除：**

``` diff
- Light neutral spin-one bosons provide a minimal and experimentally accessible extension of the Standard Model (SM).
```

**替换为：**

``` latex
Neutral spin-one bosons provide a minimal and experimentally accessible extension of the Standard Model (SM).
```

**同步要求：**

- Abstract 保留论文实际研究的 MeV-to-TeV 质量范围。
- 在参数范围说明处明确 Fig.~2 的绘图窗口及其物理动机，不把整个范围笼统称为 “light”。
- 如果作者决定在其他段落继续使用 “light”，必须在该处给出相对于明确质量尺度或物理层级的定义；否则统一删除该词。

**与当前正式回复信的对齐状态：** 当前文件 `axial_vector_model_building-v6_审稿回复信_正式回复_无占位符_2026-10-23.tex` 的 Minor Point 1 与 Minor Point 6.1 都声称已经删除未加限定的 `light`，但 v6 原稿仍以 “Light neutral spin-one bosons ...” 开头。因此处理方向一致不代表修改已落实；必须修改主论文并重新编译确认。当前正式回复信的 LaTeX 引号写法成对，旧记录所称的引号格式错误不适用于该文件。Minor Point 1 的绘图范围物理动机仍需补足；最终再根据修订稿生成准确章节/页码信息。

------------------------------------------------------------------------

## Diff 2 — Sec. II.A 与 Sec. II.C：统一标量势、Higgs portal 和物理质量矩阵

**位置：** Sec. II.A 的 Eq. (2)（总拉氏量中出现 $-V(S)$ 的位置），以及 Sec. II.C 的 Eq. (28)（当前只定义 $V(S)$ 的位置）。这两个位置承担不同功能，不能用一个笼统的“替换 Eq. (28)”指令代替。

### 2A. 先明确总拉氏量如何组织，避免重复计入标准模型 Higgs 势

先检查 $\mathcal L_{\rm SM}$ 是否已经包含标准模型 Higgs 势。若已包含，不得在新增势能中再次把同一项计入总拉氏量。建议采用以下两种组织方式之一，并在源稿中只保留一种：

- **方式 A（优先，改动较小）：** 保留 $\mathcal L_{\rm SM}$ 中的标准模型 Higgs 势；在新增扇区中定义 $V_{\rm new}(H,S)$，仅包含 $S$ 自势与 portal 项，并在 Eq. (2) 处以一致的符号加入 $-V_{\rm new}(H,S)$。
- **方式 B：** 若要统一定义完整的 $V(H,S)$，则从 $\mathcal L_{\rm SM}$ 中移除重复的 Higgs 势项，并明确说明总拉氏量中该势只出现一次。

在方式 A 下，可写为

```latex
V_{\rm new}(H,S)=\lambda_S(S^\dagger S)^2-\mu_S^2S^\dagger S
+\lambda_{HS}(H^\dagger H)(S^\dagger S),
```

而标准模型 Higgs 势仍由 $\mathcal L_{\rm SM}$ 提供。若选方式 B，完整势可写为

```latex
V(H,S)=-\mu_H^2H^\dagger H+\lambda_H(H^\dagger H)^2
-\mu_S^2S^\dagger S+\lambda_S(S^\dagger S)^2
+\lambda_{HS}(H^\dagger H)(S^\dagger S).
```

### 2B. 在 Eq. (28) 统一定义，并列出树级结果的适用条件

采用

\[
H=\frac{1}{\sqrt2}\begin{pmatrix}0\\v_h+h_0\end{pmatrix},\qquad
S=\frac{v_s+s_0}{\sqrt2},
\]

且以完整势能的驻点条件消去 $\mu_H^2$、$\mu_S^2$ 后，树级 CP-even 质量矩阵为

\[
\mathcal M^2_{hs}=\begin{pmatrix}
2\lambda_Hv_h^2 & \lambda_{HS}v_hv_s\\
\lambda_{HS}v_hv_s & 2\lambda_Sv_s^2
\end{pmatrix},
\qquad
\tan 2\theta_{hs}=\frac{2\lambda_{HS}v_hv_s}
{2\lambda_Hv_h^2-2\lambda_Sv_s^2}.
\]

在上述势能约定下，驻点条件为

\[
\mu_H^2=\lambda_Hv_h^2+\frac{\lambda_{HS}}{2}v_s^2,\qquad
\mu_S^2=\lambda_Sv_s^2+\frac{\lambda_{HS}}{2}v_h^2.
\]

这些是**树级关系**，不是圈级物理极点质量或最终混合角的替代品。正式稿必须注明符号约定，并检查势能有界性、所选真空的稳定性及所采用的微扰性条件。

### 2C. 必须完成的圈级和实验核查

1. 明确 $\lambda_{HS}$ 的重整化方案、匹配/重整化尺度和边界条件；在某一尺度设置其重整化值为零，不代表所有能标上的物理混合效应都为零。
2. 计算完整 UV 场内容下轻子和 VLL 对 portal 及非对角二点函数的贡献，区分重整化 portal 参数、动量依赖自能和物理混合角。
3. 在 $m_s\simeq m_h$ 附近使用完整的（必要时圈修正的）物理质量矩阵/极点条件，不把远离简并区的小混合角近似外推到近简并区。
4. 对相关物理本征态核查 Higgs 信号强度、exotic decays、标量产生率、总宽度、分支比和寿命；若 $s\to A'A'$ 运动学开放，须纳入其对可见分支比的影响。
5. 只有当标量对**指定观测量、参数域和目标精度**的影响经定量验证足够小，才可采用 scalar-suppressed 近似；不得仅因选取 $m_s\geq10\,\mathrm{GeV}$ 就宣称标量已退耦。

**状态更新（2026-10-27）：** portal 阈值和两个代表点的数值化、候选有限导数系数的首轮组合以及第一轮复数极点诊断已完成。有限导数系数的完整同阶 EFT soft/counterterm 闭合、独立图级验证、全动量对角自能以及模型专属 Higgs 线形/直接搜索重铸仍未完成。因此不能声称全质量区间的混合均可忽略；近简并窄宽度区域必须标记为 **not assessed**，不能直接分类为允许或排除。

### 2D. Plan C-lite 的匹配条件与论文中应明确的范围（2026-10-27）

**目的：** 将已完成的 portal 阈值和第一轮极点诊断纳入修改方案，但不把候选导数系数或条件性数值结果写成已完全验证的 UV 预测。

建议在 Sec. II.C 的 portal 讨论中加入以下文字；正式应用前仍须核对符号、章节和方程编号：

~~~latex
The renormalizable operator $(H^\dagger H)(S^\dagger S)$ is allowed by
the gauge symmetry. Integrating out the vector-like leptons at
$\mu_M=M_E$ gives, in the stated $\overline{\mathrm{MS}}$ potential
convention,
\[
\lambda_{HS}^{\mathrm{EFT}}(\mu_M)
=\lambda_{HS}^{\mathrm{UV}}(\mu_M)
+\Delta\lambda_{HS}^{E},\qquad
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}\sum_{\ell=\mu,\tau}
|y_\ell|^2|\lambda_\ell|^2+\cdots .
\]
For the scalar-suppressed reference benchmark we impose
$\lambda_{HS}^{\mathrm{EFT}}(M_E)=0$, which requires
$\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E}$.
This is an explicit matching-boundary choice, not a symmetry prediction;
setting the UV portal to zero is a different assumption.

For illustration, at $M_E=20\,\mathrm{TeV}$ with
$\theta_{\mu L}=\theta_{\tau L}=10^{-2}$ and the leading seesaw
relations, the threshold is
$\Delta\lambda_{HS}^{E}\simeq-0.2108$ for
$(m_{A'},g_X,v_s)=(10\,\mathrm{GeV},0.0705,70.9\,\mathrm{GeV})$
and $\simeq-0.01067$ for
$(63\,\mathrm{GeV},0.1,315\,\mathrm{GeV})$.
These are illustrative benchmark points, with
$|\lambda_\ell|\leq\sqrt{4\pi}$ imposed as an additional perturbativity
criterion; they are not a global scan or an exclusion contour.

For the first-pass pole diagnostic only, the finite-derivative contribution is treated as a candidate coefficient from the existing two-point/EOM matching analysis. In the matching calculation's inverse-propagator convention,
\[
\Pi_{hs,\mathrm{hard}}^{\mathrm{match}\,\prime}(0;\mu_R)
\simeq\frac{q}{16\pi^2}\left(\ln\frac{M_E^2}{\mu_R^2}-\frac23\right),\qquad
q\simeq\sum_{\ell=\mu,\tau}\frac{2m_\ell^2}{v_hv_s}.
\]
Here the prime denotes differentiation with respect to the external invariant \(s=p^2\), evaluated at \(s=0\). Only the retained leading term is displayed; no explicit higher-order remainder is quoted because its form has not yet been established by the matching calculation. The low-energy self-energy convention used for the pole diagnostic has the opposite sign, \(\Pi_{\mathrm{low}}=-\Pi_{\mathrm{match}}\). At \(s=m_h^2\) and \(\mu_R=M_E=20\,\mathrm{TeV}\), the first-pass matched values in the low-energy convention are
\[
\Pi_{hs}^{B,\mathrm{matched}}(m_h^2;\mu_R=M_E)
\simeq
\begin{cases}
(-0.413263-0.113174i)\,\mathrm{GeV}^2,
& \text{Benchmark A: }m_{A'}=10\,\mathrm{GeV}\text{ (open channel)},\\[1mm]
(-0.092999-0.025468i)\,\mathrm{GeV}^2,
& \text{Benchmark B: }m_{A'}=63\,\mathrm{GeV}\text{ (closed channel)}.
\end{cases}
\]
These are conditional results based on the candidate coefficient, not a completed one-loop UV prediction. The complete same-order EFT soft/counterterm closure and independent diagram-level validation remain open. The pole diagnostic keeps the diagonal widths fixed and absorbs diagonal real parts into the benchmark masses. The near-degenerate narrow-width region around \(m_s\simeq m_h\) therefore remains not assessed: a model-specific two-pole Higgs lineshape analysis and the relevant direct-search recast are still required.
~~~

**状态与边界：**

- 正文可说明 portal 边界条件、阈值公式、代表点及其条件性；不得将 $\lambda_{HS}^{\mathrm{EFT}}(M_E)=0$ 写成对称性强制的结果。
- 如果保留有限导数系数对应的数值自能，应明确它是候选匹配输入，且首轮极点计算采用固定对角宽度/吸收对角实部的近似。
- 正式回复信与正文必须使用同一组 benchmark 和同一套未评估边界；不得只在回复信中声称已经完成，而主文没有相应说明。
- 此 Diff 是待应用的修改方案，不代表主论文 TeX 已修改或编译通过。

------------------------------------------------------------------------

## Diff 3 — Sec. II.C：修正 VLL benchmark 与 “conservative” 用语

**位置：** Eqs. (21)–(27)，印刷页码 10–12。

### 3A. Eq. (22) 的质量下限

**当前文字：**

``` diff
- M_{E_\mu}=M_{E_\tau}\equiv M_E>10~\mathrm{TeV}.
```

**建议改为（若保留 Eq. (27) 对左右两个混合角都成立）：**

``` latex
M_{E_\mu}=M_{E_\tau}\equiv M_E
\gtrsim \frac{m_\tau}{(10^{-2})^2}
\simeq 17.8~\mathrm{TeV},
```

并紧接着说明：

> This lower scale follows from the leading-order mass–mixing relation together with the adopted upper bound on both $\tau$ mixing angles; it is not a direct-search lower bound on vector-like-lepton masses. Direct-search limits depend on the representation, decay modes, and lifetime and are treated separately.

如果作者不希望将 benchmark 下限改为约 $18\,\mathrm{TeV}$，则必须调整 Eq. (27) 的混合角假设，或用精确质量矩阵说明可行的参数选择；不能保留互相不兼容的下限和混合角条件。

### 3B. Eq. (27) 前的用语

**删除/替换：**

``` diff
- We therefore adopt the conservative benchmark
+ For the illustrative small-mixing benchmark used in the following analysis, we impose
```

**并在 Eq. (27) 后增加：**

> The values in Eq. (27) are adopted benchmark assumptions, not universal experimental upper limits on all four mixing angles. Their consistency with the charged-lepton masses and $M_E$ is checked using Eq. (21). Experimental constraints and benchmark choices are kept distinct below.

**理由：** “conservative”需要说明相对于哪组限制、哪个置信水平以及哪种 VLL 表示；未完成全套比较前应删除这一含糊判断。

------------------------------------------------------------------------

## Diff 4 — Sec. II.C：重写 Table II 前后的标量约束说明

**位置：** Eq. (29) 后、Table II、Eq. (31)–(34)，印刷页码 11–13。

### 4A. Table II caption

**当前：**

``` diff
- TABLE II: Representative upper bounds ...
```

**替换为：**

``` latex
TABLE II: Selected, non-exhaustive published constraints on the scalar
\(s\) in the low-mass region, expressed as approximate upper bounds on
\(|y_{s\mu\mu}|\). The quoted limits are approximate and inherit the
assumptions of the corresponding analyses; production, trapping, decay,
and loop-matching assumptions apply only where relevant to a given
constraint. The table is not a complete global constraint set and does
not identify the strongest bound at every scalar mass.
```

### 4B. 更正 Belle II 的自旋解释

**当前文字（应删除）：**

``` diff
- Belle II four-lepton resonance searches reach approximately 9–10 GeV, but their published interpretations assume a spin-one mediator; applying them to s requires a scalar production and acceptance recast.
```

**替换为：**

``` latex
The Belle II results relevant to this discussion must be kept as
separate analyses rather than combined into one generic scalar limit:

- The four-muon resonance search (arXiv:2403.02841) covers an
  approximately \(0.212--9\,\mathrm{GeV}\) dimuon-resonance mass
  interval and includes a muonphilic spin-0 scalar interpretation.
- The \(e^+e^-\to\mu^+\mu^-\tau^+\tau^-\) search (arXiv:2306.12294)
  covers an approximately \(3.6--10\,\mathrm{GeV}\) \(\tau^+\tau^-\)
  resonance interval and includes a Higgs-like leptophilic spin-0
  scalar interpretation.

These analyses have different production processes, final states,
acceptances, and benchmark assumptions. The source and model assumptions
must be recorded separately:

| Analysis | Source / analysis identifier | Data, channel and mass coverage | Published spin-0 benchmark and limits | Mapping to the present UV scalar | Current recast status |
|:--|:--|:--|:--|:--|:--|
| Belle II four-muon resonance | [arXiv:2403.02841](https://arxiv.org/abs/2403.02841); Phys. Rev. D **109**, 112015 (2024), DOI [10.1103/PhysRevD.109.112015](https://doi.org/10.1103/PhysRevD.109.112015); Belle II record **BELLE2-PUB-PH-2023-007** | \(e^+e^-\to\mu^+\mu^-X, X\to\mu^+\mu^-\); \(m_X=0.212\text{--}9.000\,\mathrm{GeV}\); \(178\,\mathrm{fb}^{-1}\) at \(\sqrt{s}=10.58\,\mathrm{GeV}\). The scalar result is reported for \(X\to\mu^+\mu^-\). | A muonphilic spin-0 scalar with a Yukawa-like interaction **exclusively to muons**, parameterized by the paper's \(g_S\). The paper reports 90% CL upper limits on \(\sigma(e^+e^-\to\mu^+\mu^-S)\times\mathrm{Br}(S\to\mu^+\mu^-)\) of 0.055–1.3 fb across its mass scan; for masses below 6 GeV, the quoted coupling limits range from 0.0018 to 0.040. The analyzed coupling range is prompt on the detector-resolution scale. | Do not identify \(g_S\) with \(y_{s\mu\mu}\) until the normalization is matched. The paper's muon-only scalar is not automatically the same as the present UV radial state, which can also couple to \(\tau\), mix with the Higgs, and/or decay through \(s\to A'A'\). Recompute the signal rate and \(\mathrm{Br}(s\to\mu^+\mu^-)\), width, lifetime and any extra production contributions under the same UV point. | **Source and published benchmark verified; model-specific mapping/recast not completed.** Do not mark any region excluded from mass overlap alone. |
| Belle II \(\tau^+\tau^-\) resonance | [arXiv:2306.12294](https://arxiv.org/abs/2306.12294); Phys. Rev. Lett. **131**, 121802 (2023), DOI [10.1103/PhysRevLett.131.121802](https://doi.org/10.1103/PhysRevLett.131.121802); Belle II record **BELLE2-PUB-PH-2022-004** | \(e^+e^-\to\mu^+\mu^-X, X\to\tau^+\tau^-\); \(m_X=3.6\text{--}10\,\mathrm{GeV}\); \(62.8\,\mathrm{fb}^{-1}\) at \(\sqrt{s}=10.58\,\mathrm{GeV}\). | The published interpretations include spin-1, a Higgs-like spin-0 leptophilic scalar, and an ALP. The paper reports 90% CL limits on \(\sigma\times\mathrm{Br}(X\to\tau^+\tau^-)\) from 0.7 to 24 fb; it reports world-leading leptophilic-scalar coupling constraints above 6.5 GeV. | Match the paper's scalar lepton-coupling pattern and normalization against the UV-derived \(y_{s\ell\ell}\); then include the actual \(s\to A'A'\) threshold, all relevant visible/invisible modes, total width, lifetime and detector acceptance. The spin-0 result exists, but its assumptions are not automatically identical to the present model. | **Source and existence of spin-0 interpretation verified; exact point-by-point mapping/recast not completed.** |

For each analysis, assess whether its published scalar interpretation maps onto the present model by checking the relevant production couplings, mass-dependent Yukawa interactions, total width, branching fractions (including \(s\to A'A'\) where open), lifetime, and acceptance. A mass-range overlap alone is not sufficient to classify any region as excluded. The four-muon paper's \(g_S\) convention must not be silently substituted for the manuscript's \(y_{s\mu\mu}\); the two analyses also cannot be combined into one generic “Belle II scalar limit.”
```

**重要：** 这段是对文献适用性的正确描述，不等于已经完成本文模型的重铸。若后续确认 Belle II 的某个 spin-0 benchmark 与本文完全匹配，应说明匹配条件；若不匹配，应给出差异并计算或明确保留未评估状态。

### 4C. 删除含糊的 “intermediate scalar-mass region”

**当前文字（应删除或重写）：**

``` diff
- Thus the B-factory searches do not provide a universal \(g_X\) bound, but they show that the intermediate scalar-mass region cannot simply be assumed unconstrained.
```

**建议替换为：**

``` latex
The published searches cover different scalar-mass intervals and make
specific assumptions about production and decay. For the present model,
the relevant comparison must include \(\Gamma(s\to A'A')\) when
kinematically allowed, the visible leptonic widths, the total width,
and the resulting branching fractions. We therefore report the
constraint status separately for each mass interval: [insert the
model-specific recast result, or mark the interval as not yet assessed].
The published mass coverage by itself is not an exclusion of the
corresponding parameter region in this model.
```

### 4D. 重写 Eq. (34) 后的 scalar-suppressed benchmark 段

**建议替换当前从 “To isolate the axial-vector phenomenology…” 到 “…treat $s$ as decoupled…” 的段落：**

``` latex
For the two-parameter effective-current analysis below, we define a conditional
scalar-suppressed benchmark with \(m_s\geq10\,\mathrm{GeV}\). This mass choice alone does not establish scalar decoupling; the approximation is used only for observables and parameter points for which the scalar-sector checks support it.
In the negligible-mixing limit, the scalar self-coupling satisfies
\[
m_s\leq\sqrt{2\lambda_S^{\max}}\,v_s,\qquad
v_s=\frac{m_{A'}}{2g_X}.
\]
For the illustrative choice \(\lambda_S^{\max}=4\pi\), the existence
of a point with \(m_s\geq10\,\mathrm{GeV}\) requires
\(v_s\geq10/\sqrt{8\pi}\,\mathrm{GeV}\simeq1.995\,\mathrm{GeV}\).
This is a theoretical condition on the selected benchmark, not an
experimental exclusion line.

For each plotted point \((m_{A'},g_X)\), we derive \(v_s\), apply the
stated scalar-coupling condition, and separately record the status of
the scalar-sector constraints. The effective-current contours in
Fig.~2 are not, by themselves, a global allowed region of the UV
completion, and the scalar-suppression assumption must be validated separately for the observables under discussion. The final scalar classification is [insert the result
after the scalar search recast and portal analysis].
```

**必须删去或在计算后重写：** - “avoids the strongest light-scalar constraints”——除非完成相应约束比较； - “there is no comparably broad published scalar exclusion”——在核查并映射 Belle II spin-0 结果前不能这样概括； - “otherwise treat $s$ as decoupled”——应限定到已验证的观测量、参数域和误差门槛。

------------------------------------------------------------------------

## Diff 5 — 在 Sec. II.C 增加统一参数表

**位置：** Eq. (35) 后、Sec. III 前。

新增一张表（建议编号 Table III；原 Table III 如被占用则顺延）：

| Parameter           | Role in the benchmark                    | Range/condition                                                           | Interpretation                                            |
|:--------------------|:-----------------------------------------|:--------------------------------------------------------------------------|:----------------------------------------------------------|
| $m_{A'}$            | independent scan variable                | Fig. 2 plotting window: $10^{-3}$–$10^2\,\mathrm{GeV}$                    | plotting range, not a universal bound                     |
| $g_X$               | independent scan variable                | Fig. 2 plotting window: $10^{-6}$–$10^{-1}$                               | plotting range, not a universal bound                     |
| $v_s$               | derived in the minimal one-VEV benchmark | $v_s=m_{A'}/(2g_X)$                                                       | not independent once $(m_{A'},g_X)$ are fixed             |
| $m_s$               | scalar-suppressed benchmark input        | $m_s\geq10\,\mathrm{GeV}$, subject to perturbativity and scalar-sector checks | not automatically decoupled or experimentally allowed                  |
| $\lambda_S$         | derived scalar coupling                  | $\lambda_S=2g_X^2m_s^2/m_{A'}^2$ in the negligible-mixing limit           | apply the stated $\lambda_S^{\max}$ criterion             |
| $M_E$               | VLL benchmark                            | revise consistently with Eq. (21) and Eq. (27)                            | distinguish benchmark inference from direct-search limits |
| $\theta_{\ell L,R}$ | small-mixing assumptions                 | state the chosen benchmark and the experimental basis separately          | finite values imply residual non-axial effects            |
| $\lambda_{HS}$      | portal parameter                         | specify renormalization condition and scale                               | cannot be omitted without justification                   |
| $\epsilon$          | kinetic mixing                           | specify matching condition and loop/threshold result                      | distinct from the VLL-induced $g_V$                       |

**表下注释必须写清楚：** The table summarizes the benchmark used for the plotted analysis. It is not a claim that every point in the displayed window satisfies all theoretical conditions or all experimental constraints. Unassessed regions remain unassessed.

------------------------------------------------------------------------

## Diff 6 — Fig. 2 caption：明确坐标范围与灰虚线含义

**位置：** Fig. 2，印刷页码 21。

**建议在现有 caption 末尾增加：**

``` latex
The displayed axes define the plotting window
\(10^{-3}\,\mathrm{GeV}\lesssim m_{A'}\lesssim10^2\,\mathrm{GeV}\) and
\(10^{-6}\lesssim g_X\lesssim10^{-1}\); they are not global physical
boundaries. The contours refer to the conditional pure-axial effective-current benchmark in Sec.~II.C; the scalar-suppression assumption is valid only where supported by the scalar-sector checks. For \(m_s=10\,\mathrm{GeV}\) and \(\lambda_S^{\max}=4\pi\), the exact tree-level condition is \(v_s\geq10/\sqrt{8\pi}\,\mathrm{GeV}\simeq1.995\,\mathrm{GeV}\). The dashed \(v_s=2\,\mathrm{GeV}\) line is a rounded visual reference, not the exact boundary and not an experimental exclusion line.
The scalar constraints and the finite-VLL/kinetic-mixing constraints
must be applied separately when assessing the full UV model.
```

**正文 Fig. 2 后的相关句子建议替换为：**

``` latex
The \(v_s=2\,\mathrm{GeV}\) line is a reference for the chosen scalar
benchmark. Since \(y_{s\mu\mu}=m_\mu/v_s\), the Yukawa coupling equals
approximately \(0.053\) on this line. Moreover,
\[
\frac{y_{s\mu\mu}^2}{4\pi}\simeq2.2\times10^{-4}\ll1,
\]
so the Yukawa coupling itself is perturbative at this reference point.
The line therefore does not represent a nonperturbativity bound on
\(y_{s\mu\mu}\); it encodes the chosen upper bound on
\(\lambda_S\) for \(m_s=10\,\mathrm{GeV}\).
```

------------------------------------------------------------------------

## Diff 7 — 在质量基底耦合处定义 pure-axial limit，并限定 Fig. 2 的适用范围

**位置：** Sec. II 中引入质量基底耦合的 Eq.~(12) 附近，以及 Sec. III 的 Eq.~(36) 前后；印刷页码约 7、13–14（以最终稿为准）。

### 7A. 在 Eq. (12) 附近直接定义严格纯轴矢量极限

在给出 $$
g_V^\mu=g_X\sin^2\theta_{\mu R},\qquad
g_A^\mu=-g_X\cos^2\theta_{\mu R}
$$ 之后，紧接着说明：

``` latex
The strict pure-axial limit in the muon sector is defined by
\(\theta_{\mu R}\to0\), for which \(g_V^\mu\to0\) and
\(g_A^\mu\to-g_X\). For finite \(\theta_{\mu R}\), the interaction
contains a residual vector component and is not strictly purely axial.
The corresponding limit in the tau sector is defined consistently
using the tau mass-basis couplings and the same charge conventions.
```

在最终源稿中，应将 tau 扇区的实际耦合关系与极限写清楚，不要仅以一句 “treated consistently” 代替可核查的定义。

### 7B. 在 Eq. (36) 后说明后续约束图所采用的近似

``` latex
Unless explicitly stated otherwise, the constraints below are
evaluated in the strict pure-axial effective-current limit. This
limit is approached by the UV benchmark for small light--heavy
mixing, but finite vector-like-lepton masses can leave residual
vector couplings and can contribute to kinetic mixing through
threshold and mixing effects. The mass-basis vector coupling
\(g_V^\ell\) and the gauge-field kinetic-mixing parameter
\(\epsilon\) are distinct quantities and must be assessed separately.
```

**必须另行完成的工作：** 给出 $\epsilon$ 的匹配/重整化条件、圈级表达式及 benchmark 数值；分别评估 $g_V^\ell$ 与 $\epsilon$ 对实验约束的影响。只有在 T-06/T-07 的定量比较完成后，才能声称这些效应不会改变 Fig.~2 的排除结论。

------------------------------------------------------------------------

## Diff 8 — Major 4.4：单独增加 $A'$ 的恒星冷却/超新星适用性讨论

**位置：** 建议在 Sec. III 的现有约束小节之后、Sec. IV 之前增加一个小节；若结果很简短，也可在 Sec. III 开头的约束清单中增加专门段落。

**建议小节标题：**

``` latex
\subsection{Stellar-cooling and supernova constraints}
```

**可先插入的结构性文字（方括号必须由实际核查结果替换）：**

``` latex
The stellar constraints on the scalar \(s\) summarized in Table~II
are distinct from stellar-cooling and supernova constraints on the
gauge boson \(A'\). We assess the latter using the production,
trapping, and escape assumptions of the relevant analyses, and check
their applicability to the axial current and to the mass and coupling
range considered here. The resulting constraint is [applicable in
the specified region / subdominant to the stated constraints /
not directly applicable for the following physical reason].
The comparison and its assumptions are summarized in [Table/Fig. X].
```

**必须做的核查：** 1. 回到审稿人点名的原始论文，确认其研究的是 $A'$ 还是其他粒子、矢量还是轴矢量电流、适用质量区间及介质条件。 2. 检查产生率、纵向模、有限 $g_V$、动能混合、俘获/逃逸和衰变长度是否改变结果。 3. 如果需要重铸，记录数据/曲线、假设和误差；若无法可靠重铸，明确标记未评估，不得写成已排除或不相关。 4. 在参考文献表加入并核对该原始文献的完整 bibliographic entry。

------------------------------------------------------------------------

## Diff 9 — Sec. III.E：删除未定义的 “parameter region of interest”

**位置：** Sec. III.E 第一段，印刷页码 22。

**当前文字：**

``` diff
- In the parameter region of interest, the produced \(A'\) promptly decays into a pair of charged leptons or neutrinos ...
```

**建议替换为：**

``` latex
For each four-muon search, we use only the mass interval and event
selection covered by the corresponding experimental analysis. The
prompt-decay approximation is applied only where the model-dependent
decay length \(L_{\rm dec}=\beta\gamma c\tau_{A'}\), with
\(c\tau_{A'}=\hbar c/\Gamma_{A'}\), is short compared with the
relevant prompt-selection scale. The total width and
\(\mathrm{Br}(A'\to\mu^+\mu^-)\) are evaluated with the open channels
of the benchmark. Parameter points that do not satisfy the prompt
assumption are not interpreted using the prompt-resonance recast.
```

**与回复信 Minor Point 6.5 对齐的实验覆盖范围：**

$$
\begin{aligned}
\text{BaBar}:&\quad 0.212\text{--}10\,\mathrm{GeV},\\
\text{Belle II}:&\quad 0.212\text{--}9\,\mathrm{GeV},\\
\text{CMS}:&\quad 5\text{--}70\,\mathrm{GeV}.
\end{aligned}
$$

这些是相应已发表分析的近似质量覆盖范围，不是整个区间都被本文模型排除。正文或表格还须分别列明过程 $e^+e^-\to\mu^+\mu^-A'$, $A'\to\mu^+\mu^-$ 与 $Z\to\mu^+\mu^-A'$, $A'\to\mu^+\mu^-$，以及各分析实际使用的事件选择和宽度/分支比假设。

**可保留的示例估算（仅代表一个 benchmark 点）：**

``` latex
As an illustrative check, at \(m_{A'}=0.212\,\mathrm{GeV}\) and
\(g_X=7\times10^{-4}\), the neutrino decay channels alone give
\(c\tau_{A'}\lesssim0.072\,\mu\mathrm{m}\), corresponding to a
laboratory-frame decay length of approximately \(1.8\,\mu\mathrm{m}\)
for \(\gamma\simeq25\). This estimate supports the prompt-decay
approximation at this benchmark point, but does not establish its
validity throughout the full parameter space.
```

**后续必须补充：** 对用于重铸的参数点计算总宽度、$\mathrm{Br}(A'\to\mu^+\mu^-)$ 和实验室衰变长度，并与每个实验的 prompt-selection 条件比较。单个 benchmark 的估算不能替代整个参数域的检验。近 dimuon 阈值处还须保留矢量到轴矢量的 rate-matching 近似不等于 detector-level exclusion 的限定。

------------------------------------------------------------------------

## Diff 10 — Sec. IV：把 muon-collider 部分定位为 illustrative study

**位置：** Sec. IV 第一段，印刷页码 24–26。

**建议将开头两段重写为：**

``` latex
This section presents an illustrative study of angular observables
that distinguish vector and axial \(U_A(1)_{L_\mu-L_\tau}\) currents
at a future high-energy muon collider. The purpose is not to provide
a detector-level sensitivity projection, but to demonstrate why a
total-rate rescaling alone can miss the chirality dependence of the
signal. The muon collider is a complementary probe because the
initial state couples directly to the muon-philic interaction and
can access mediator masses beyond the low-energy searches discussed
above.

We use \(\mu^+\mu^-\to\tau^+\tau^-\) as a clean analytic example and
study the differential rate and forward--backward asymmetry. A full
forecast would require a specified integrated luminosity, beam and
detector assumptions, signal/background simulation, and systematic
uncertainties. Polarization asymmetries require additional assumptions
about beam polarization and are left for future work. Searches for
the scalar sector at a future Higgs factory are complementary, but
their sensitivity depends on the physical scalar mixing, production
modes, and branching fractions; we do not claim a quantitative reach
without a dedicated study.
```

**操作：** - 保留 Eq. (65)–(67) 与 Fig. 3 作为解析示例； - 删除任何可能被理解为”已经给出未来排除曲线”的措辞； - 若没有新增极化或探测器模拟，不要把它们写成本文已完成结果； - 若后续决定把 muon-collider 分析扩展成主要结果，则必须补全设置和统计分析，而不能只加强文字。

------------------------------------------------------------------------

## Diff 11 — Introduction、Conclusion 与摘要：同步收窄主张

**位置：** Abstract、Introduction 末段、Conclusion，印刷页码 1、4、26–27。

### 11A. Abstract

当前摘要中 “In this limit, the observables considered here depend mainly on $(m_{A'},g_X)$” 应明确为 benchmark 结论，而不是对完整 UV 参数空间的陈述。

**建议替换相关句子为：**

``` latex
For the specified heavy-VLL and small-mixing benchmark, with scalar effects suppressed only where quantitatively justified, the observables studied below are primarily organized
in the \((m_{A'},g_X)\) plane. The resulting contours are conditional
on these assumptions and do not by themselves represent the global
allowed region of the full UV model.
```

**PMNS 的摘要表述（路线 B 已选）：** 摘要不声称解决中微子质量或完整 PMNS；可加一句 “The minimal field content does not provide a complete neutrino-mass or PMNS completion.” 若摘要篇幅有限，至少避免任何暗示当前模型已解释观测振荡的措辞。

### 11B. Introduction 末段

在论文组织结构段前，新增一段简短的 scope statement：

``` latex
The two-parameter plots below refer to a specified benchmark of the
UV construction. They should be distinguished from a global fit of
all scalar, vector-like-lepton, kinetic-mixing, and neutrino-sector
parameters. The assumptions needed for this benchmark and the
additional conditions required to interpret it as a complete UV
parameter point are stated explicitly in Sec.~II.
```

本轮采用路线 B：在 Introduction 中明确最小构造不解释完整 neutrino mass spectrum/PMNS mixing，并将 Fig. 2 定位为指定纯轴有效流 benchmark 的约束图，而非完整 UV 全局拟合。

### 11C. Conclusion

**在结论末段增加：**

``` latex
The constraints displayed in Fig.~2 are evaluated in the specified
pure-axial effective-current limit and a scalar-suppressed benchmark whose validity must be established for the observables considered. A point in this plane is
not automatically a viable point of the full UV model: the scalar
potential and portal, finite-VLL effects, kinetic mixing, and the
relevant additional constraints must be checked under a consistent
set of UV inputs. We therefore distinguish the effective-current
constraints from the full UV-model classification.
```

**PMNS（已选择路线 B）：** 在结论末尾明确最小构造不提供完整的中微子质量/PMNS 机制，残余 $Z_2$ 使 $e$ 与 $(\mu,\tau)$ 分块；不声称已符合观测中微子振荡。保留原有轴矢量现象学作为条件性 pure-axial effective-current benchmark，不将其解释为完整 UV 模型的全局允许域。



### 11D. Model section: Weinberg operators and the residual selection rule

**位置锚点：** 模型构造部分中列出 \(Q'(L_e,L_\mu,L_\tau)=(0,+Q_\ell,-Q_\ell)\)、\(Q'(H)=0\)、\(Q'(S)=2Q_\ell\) 的电荷指派之后，进入纯轴矢量 benchmark/唯象学讨论之前。由于本次 GitHub 分支未包含主论文 TeX 源文件，本位置按内容锚点指定；实际节号、方程号和页码须在源稿修改后确认。

**新增正文建议：**

~~~latex
For the minimal charge assignment
\[
Q'(L_e,L_\mu,L_\tau)=(0,+Q_\ell,-Q_\ell),\qquad
Q'(H)=0,\qquad Q'(S)=2Q_\ell,
\]
the Weinberg operator has the schematic form
\[
\mathcal O^{(5)}_{ij}=(L_i\cdot H)(L_j\cdot H),
\]
where the electroweak and Lorentz contractions are understood. At dimension five, the gauge-invariant entries are \(\mathcal O^{(5)}_{ee}\) and \(\mathcal O^{(5)}_{\mu\tau}\). The diagonal \(\mu\mu\) and \(\tau\tau\) entries can arise at dimension six through, respectively, \(S^\dagger\mathcal O^{(5)}_{\mu\mu}/\Lambda^2\) and \(S\mathcal O^{(5)}_{\tau\tau}/\Lambda^2\). Operators connecting the electron flavor to the \(\mu\) or \(\tau\) flavor remain forbidden because insertions of \(S\) or \(S^\dagger\) change the charge only by even multiples of \(Q_\ell\).

After \(S\) acquires a vacuum expectation value, the neutrino mass matrix generated by these effective operators has the block form
\[
M_\nu=\begin{pmatrix} A&0&0\\0&B\varepsilon&C\\0&C&D\varepsilon\end{pmatrix},
\qquad \varepsilon\sim v_s/\Lambda,
\]
where the coefficients absorb convention-dependent factors. The charged-lepton mass matrix allowed by the same residual selection rule also separates the electron flavor from the \(\mu\)-\(\tau\) sector. Consequently, up to a permutation of neutrino mass eigenstates, the leptonic mixing matrix is block diagonal with a one-dimensional pure-electron-flavor sector and a \(\mu\)-\(\tau\) sub-block. If the isolated electron-flavor eigenstate is listed first, this corresponds to \(\theta_{12}=\theta_{13}=0\); independently of ordering, the other two mass eigenstates have no electron-flavor component. This structure is incompatible with the observed PMNS matrix.

These higher-dimensional operators describe an allowed effective neutrino-mass structure; they are not a complete neutrino-mass mechanism contained in the original renormalizable UV Lagrangian. The present work therefore does not claim to explain the observed neutrino masses or PMNS mixing.
~~~

**修改前：** 原稿没有模型专属的 Weinberg 算符选择规则、质量矩阵分块或 PMNS 限制说明；读者无法判断允许质量项与完整振荡拟合之间的差别。

**修改后：** 明确维五允许的 \(ee,\mu\tau\) 项、维六 \(S\)-插入项、禁止的 \(e\mu,e\tau\) 项以及残余 \(Z_2\) 导致的分块结构。不得将该段写成已经构造或拟合了完整中微子质量机制。

**修改理由：** 直接回答审稿人的 Weinberg-operator 问题，同时准确承认模型局限；不引入新粒子，不改动既有轴矢量有效流数值结果。

### 11E. Major Point 4.1: use exactly the same PMNS conclusion

**建议回复口径：**

~~~latex
We agree that the minimal construction does not reproduce the observed PMNS matrix. The allowed Weinberg operators and their \(S\)-inserted higher-dimensional counterparts preserve the \(\{e\}\oplus\{\mu,\tau\}\) block structure, so the required electron-flavor mixing is absent. We therefore adopt the same scope limitation as in Major Point~3: no claim is made that the minimal model explains the full neutrino mass spectrum or observed oscillations, and no right-handed neutrinos or additional scalar are introduced in this revision. The existing \(A'\) contours are retained as constraints on the specified pure-axial effective-current benchmark; they are not presented as proof that every plotted point is a globally viable UV-model point.
~~~

**一致性验收：** Major 3、Major 4.1、Introduction、模型部分和 Conclusion 必须同时表达同一结论。不要在 4.1 中把中微子振荡限制称为已通过，也不要把保留 Fig. 2 的有效流结果写成完整 UV 模型通过全部实验约束。

------------------------------------------------------------------------

# Part III. 任务关闭、证据归档与最终验收

本部分是发布前的**流程验收门**；各项研究任务的状态只在前面的”统一任务登记表”中维护，避免出现两套状态表。

## 任务关闭标准

任何 T-00 至 T-14 任务，只有同时满足适用条件时才能标记为“已验证”：

- [ ] 研究输入与基准版本已记录，包括论文版本、模型假设、参数范围、重整化/匹配条件及实验分析版本。
- [ ] 推导或计算已完成，代码/notebook、软件版本、输入和输出文件可追溯；手算、数值检查或独立实现至少完成适合该任务的交叉核验。
- [ ] 实验约束已核对实际适用的粒子、电流结构、质量覆盖、产生率、总宽度、分支比、寿命、接受度及置信水平；不适用的项目须给出物理理由。
- [ ] 结论被明确分类为理论一致、实验排除、在已考虑约束下未排除、未评估或未来灵敏度；没有将 benchmark 结论外推到整个参数空间。
- [ ] 对应论文修改已经实际写入源稿，且修改前后差异可定位；若决定不修改，记录理由及审稿意见为何仍得到回应。
- [ ] 独立复核结果、未解决的不确定度和剩余适用边界已记录。若任何关键项仍未满足，状态应保留为“进行中”“待独立核查”或“阻塞”。
- [ ] 若任务涉及 Fig. 2，已与冻结基准进行同输入、同实验假设下的比较；明确指出曲线变化的质量/耦合区域、数值标准和不确定度，不以视觉相似替代定量比较。
- [ ] T-13 关闭时，已记录 UV–EFT 匹配约定、适用能标、保留算符阶数、截断误差和同点 UV 可实现性；不能只给出形式上的 Wilson 系数对应。
- [ ] T-14 关闭时，已给出保留原图、局部修正或重算的证据化决定；不得预先承诺图一定保留或一定重算。

## 正式提交发布门

- [ ] T-00 至 T-14 均已验证，或对不再适用的任务给出有证据支持的关闭理由；T-01 已选择路线 B，但只有在主论文实际加入范围声明、Major 3/4.1 与正文一致、重新编译并核对最终引用后，才可关闭文本一致性工作包。路线 B 不表示最小 UV 模型已经解释 PMNS；接受风险须明确记录。
- [ ] Diff 0–14 的每项操作均已落实，或记录了不采纳该修改的明确理由；Diff 建议文本没有未经核验就直接当作最终结论。
- [ ] 论文摘要、引言、模型、约束部分、图表、结论之间没有相互矛盾的主张；公式、图表、文献、章节引用和页码均按最终稿重新核对。
- [ ] Fig. 2 的绘图窗口、条件性 benchmark、理论一致性、实验排除、所考虑约束下未排除和未评估区域明确区分。
- [ ] 正式回复信逐条保留审稿意见原文并给出对应回应；不含内部清单、工作状态、待办、方括号占位符或尚未完成的结果声明。
- [ ] 回复信中的每一项 “we have revised”“we find”“excluded”“allowed”“consistent with PMNS”等陈述，都有最终论文差异、计算输出或实验重铸证据对应。
- [ ] 主论文和回复信的 LaTeX 均完整编译；检查 PDF 中的标题层级、编号、公式断行、引用、分页和超出边界的文本。
- [ ] 最终提交版本、源稿 commit/hash、编译日志、最终 PDF 和回复信版本已归档，确保结论可复现、可追溯。

## 最终写作规则（与任务登记表配套）

1.  “理论上可实现”“在列明实验下未排除”“实验排除”“EFT 不适用”“未来可探测”是不同结论，不能混用。
2.  一个 benchmark 通过检查，不代表整个参数区间通过检查。
3.  发现某个实验的质量覆盖，不代表它已经排除本文模型；必须匹配产生率、耦合、宽度、分支比、寿命和接受度。
4.  “portal 可忽略”必须限定在明确参数域、过程和误差门槛；不能只依据 $\lambda_{HS}$ 的某个边界值。
5.  PMNS 扩展若引入新带荷 VEV，必须重新推导 $m_{A'}$ 与 VEV 的关系，并重新检查标量谱、UV–EFT 映射和所有受影响的实验约束。
6.  所有 `[待计算/待填入]` 项完成后，才把工作稿转为正式回复信；最后再按修订稿重新核对章节、方程、图表编号和页码。

------------------------------------------------------------------------

## Diff 12 — 正式回复信逐点对照表与提交前一致性验收

**用途：** 将 `axial_vector_model_building-v6_审稿回复信_正式回复_无占位符_2026-10-23.tex` 中的每项主要陈述映射到论文正文、计算或实验核查。此处是内部验收表，不应放入正式回复信。

| 回复信位置                     | 论文应落实的修改/证据                                                                                                                 | 对应任务                     | 当前必须注意的事项                                                                                        |
|:-------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|:----------------------------------------------------------------------------------------------------------|
| Major Point 1                  | 给出 $m_s$、$\lambda_S$、$v_s$ 的条件性关系；区分理论上界、实验排除、所考虑约束下未排除和未评估区域                                   | T-03、T-04、T-09             | 只有理论公式不足以给出实验允许质量区间；保留最终分类占位符直至重铸完成                                    |
| Major Point 1.1                | 将 scalar $s$ 纳入 UV 完备模型的现象学讨论；计算产生率、物理混合、总宽度、分支比、寿命和适用搜索；处理 $s\to A'A'$                    | T-02、T-03、T-04             | 质量落在实验覆盖内不等于已排除或已证明可探测                                                              |
| Major Point 1.2                | 给出 $m_{A'}$、$g_X$ 扫描范围、scalar benchmark、$\lambda_S^{\max}$、约束清单及投影分类                                               | T-03、T-09                   | 不能把满足微扰性写成实验可行；允许投影可为非连通区域                                                      |
| Major Point 1.3                | 写出完整 Higgs portal 势、重整化条件、轻子/VLL 圈级贡献、物理质量矩阵，并处理 $m_s\simeq m_h$                                         | T-02、T-03                   | 当前正式回复信承认全质量范围的圈级混合界限尚未建立；应将同样的限制写入修订稿，任务仍未关闭                         |
| Major Point 2                  | 统一参数表；区分 Fig. 2 plotting window、条件性 benchmark、理论一致性、实验排除和未评估区域，并验证 UV–EFT 匹配/截断及同点 UV 实现性 | T-09、T-13、T-14 | Fig. 2 的轴范围不是全局物理边界；图的稳健性须由比较决定                                                                           |
| Major Point 3 / Point 3.1      | 明确允许/禁止的 Weinberg 算符、残余 $Z_2$ 与 $e\oplus(\mu,\tau)$ 分块；说明质量项存在不等于完整 PMNS 已解决 | T-01 | 路线 B 已选；必须实际应用正文 Diff，并避免声称已解释观测振荡 |
| Major Point 3 / Point 3.2      | 不新增右手中微子或标量；说明右手中微子单独加入并不能打破残余选择规则，扩展需重做模型一致性检查 | T-01 | 路线 B 已选；扩展方案仅为未选候选，不作为已验证解决方案 |
| Major Point 3 总结与 Major 4.1 | 与 Point 3 使用同一范围限定；摘要、引言、模型部分、结论及回复信一致 | T-01、T-12 | 路线已选；正文未应用、章节/页码和最终审稿风险评估仍待完成 |
| Major Point 4 总述             | 给出约束适用性表，区分 $s$、$A'$、有限 VLL 效应、严格纯轴矢量极限                                                                     | T-03、T-06、T-07、T-08、T-12、T-14 | “已应用/次主导/不适用”每种分类都要有依据；未评估不能写成不相关                                            |
| Major 4.2                      | 匹配尺度、重整化条件、动能混合圈级表达式、阈值抵消条件、benchmark 数值和实验尺度比较                                                  | T-06                         | 在数值和误差核查完成前，不声称实验尺度动能混合为零                                                        |
| Major 4.3                      | 单独比较残余矢量耦合与轴矢量约束，并评估动能混合对 Fig. 2 的影响                                                                      | T-07、T-14                   | $g_V/g_A\lesssim10^{-4}$ 是耦合比，不是实验约束强弱之比                                                   |
| Major 4.4                      | 对 $A'$ 的恒星冷却/超新星限制核查电流结构、质量/耦合范围、产生、纵向模、trapping/escape/decay                                         | T-08                         | 当前正式回复信明确承认未做本文轴矢量 benchmark 的模型专属重铸；T-08 保持开放，修订稿应同步写明适用性尚未定量评估 |
| Minor Point 1                  | 解释 $m_{A'}$ 和 $g_X$ 范围为何被选作绘图窗口，给出相关现象学动机                                                                     | T-09                         | 当前回复信称已删除 “light”，但 v6 原稿仍保留；绘图范围的物理动机也需补足并在修订稿中核对                                     |
| Minor Point 2                  | 在 Eq. (12) 质量基底耦合处定义 $\theta_{\mu R}\to0$ 的严格纯轴矢量极限，并按相同约定说明 tau 扇区                                     | T-07、T-09                   | 不要只在 Eq. (36) 附近首次定义该词                                                                        |
| Minor Point 3                  | 给出由 $m_\ell\simeq\theta_{\ell L}\theta_{\ell R}M_{E\ell}$ 推出的条件性质量尺度，区分直接搜索界限并核查表示、衰变和寿命假设         | T-05                         | $M_E\gtrsim17.8\,\mathrm{TeV}$ 是两个 tau 混合角均不超过 $10^{-2}$ 时的领先阶条件性推论，不是直接实验下限 |
| Minor Point 4                  | 将 “conservative benchmark” 改为 “small-mixing assumption”，并与实验界限区分                                                          | T-05                         | 若要继续称 conservative，必须提供相对于明确实验约束的定量比较                                             |
| Minor Point 5                  | 将 muon-collider 部分定位为 illustrative study/outlook；保留已有前后不对称示例，不宣称完整灵敏度预测                                  | T-11                         | 未进行探测器级模拟时，不应声称 exclusion/discovery reach                                                  |
| Minor Point 6.1                | 从引言开头删除未定义的 “light”，并核对 Abstract 的 MeV-to-TeV 范围说明                                                                | T-09                         | 当前正式回复信的 LaTeX 引号写法成对；实质问题是 v6 原稿仍保留开头的 “Light”，需先修改正文并确认扫描范围说明                                                               |
| Minor Point 6.2                | 将 Table II 说明为 selected, non-exhaustive constraints，并列明限制所依赖的假设                                                       | T-03、T-04                   | 不宣称每个质量处均为最强约束                                                                              |
| Minor Point 6.3                | 删除 “intermediate scalar-mass region”；列出 BaBar/Belle 搜索范围、Belle II 标量解释的适用条件和 $\xi_{\rm lim}=0.483$ 的条件性换算   | T-03、T-04                   | 数值换算只适用于所述 mass-proportional benchmark；若 $s\to A'A'$ 开放须处理可见分支比                     |
| Minor Point 6.4                | 定义 scan “point”为 $(m_{A'},g_X)$ 网格点，并在每点派生 $v_s$、计算 $\lambda_S$                                                       | T-09                         | 理论微扰性检查与实验约束必须分开                                                                          |
| Minor Point 6.5                | 列出 BaBar $0.212$–$10$ GeV、Belle II $0.212$–$9$ GeV、CMS $5$–$70$ GeV 的近似覆盖；计算总宽度、分支比和 prompt 条件                  | T-10                         | $c\tau$ 示例仅验证单一 benchmark 点，不足以证明整个扫描域 prompt                                          |
| Minor Point 6.6                | 解释 $v_s\simeq2$ GeV 来自 $m_s=10$ GeV、$\lambda_S^{\max}=4\pi$；给出 $y_{s\mu\mu}\simeq0.053$ 及 $y^2/(4\pi)\simeq2.2\times10^{-4}$ | T-09                         | 该线是 scalar self-coupling benchmark 边界，不是 Yukawa 非微扰界限或实验排除线                            |
| UV–EFT matching / truncation   | 给出 $c_\alpha/\Lambda$ 与 UV 参数的匹配关系、EFT 适用能标、保留算符阶数及截断误差，并检查同一参数点的 UV 实现性                   | T-13                         | 不把形式匹配关系当作数值验证或全参数域 UV 实现证明                                                |
| Fig. 2 baseline / robustness   | 与冻结基准比较有限 VLL、$g_V^\ell$、$\epsilon$、中微子扩展和标量效应，作出保留/局部修正/重算决定                                 | T-14                         | 冻结基准不等于预先认可；必须给出量化差异和不确定度                                                |
| Summary                        | 将 PMNS、标量、额外约束、UV–EFT 适用性及 Fig. 2 稳健性结论与正文、图表和逐条回复同步                                                   | T-12、T-13、T-14             | 占位符只能在对应任务完成或经过有依据的范围限定后替换                                                  |

### 回复信中的完成时声明：逐项核验规则

正式回复信可以在最终版本中使用 “we have clarified/revised/calculated/assessed”，但必须满足以下条件：

- 相关正文文字或公式已实际写入修订稿，而非仅存在于本 Diff 的建议文本中。
- 涉及计算的陈述具有可追溯的推导、代码/数值输出或独立核查记录。
- 涉及实验限制的陈述具有来源、适用条件、质量/耦合范围以及必要的模型特定重铸。
- 仍有方括号占位符的段落，不得作为最终提交版本；尤其不能同时保留”已完成评估”的完成时句子与尚未得到的结果。
- 最终章节、公式、图表编号必须由最终编译稿生成并核对，不得在修改前预填。

### 必须保留的研究要求

- **标量与 portal：** 将树级势、重整化边界、轻子/VLL 圈级贡献、非对角二点函数、物理极点和实验率分开核查；完整圈级计算未完成前，不能把 portal 或近简并效应标为已解决。
- **中微子扇区：** 当前已选择路线 B；必须将最小模型不提供完整 PMNS 机制的限制同步到正文、摘要、结论、Major 3 和 4.1。不得将范围收窄描述为中微子振荡问题已解决；只有未来重新开启扩展路线时，才需完成完整拟合与模型一致性检查。
- **Belle II 标量解释：** 分别核对四缪子和 $	au^+\tau^-$ 分析的自旋解释、产生/衰变假设、总宽度、分支比、寿命和接受度；质量范围重叠不等于本文模型已被排除。
- **有限 VLL 与动能混合：** 将 $g_V$ 与 $\epsilon_{\rm kin}$ 分开计算，明确简并抵消条件和匹配尺度；只有在同一 UV benchmark 下比较实验约束，才能判断其对 Fig. 2 的影响。
- **UV–EFT：** 对同一组 UV 输入验证 Wilson 系数匹配、EFT 适用能标、截断误差和 UV 实现性；形式匹配关系不能替代数值验证。
- **回复闭环：** 所有 “we have revised/removed/defined/assessed” 陈述均需对应修订稿中的真实差异；未完成的计算或重铸必须继续标为未完成。

------------------------------------------------------------------------

## Diff 13 — UV–EFT 匹配、适用能标与截断误差（新增研究任务 T-13）

**定位：** Major Point 2 的 UV–EFT 对照要求；具体正文位置以当前稿中维五算符与有效耦合定义处为准。该项是新增研究任务，不意味着现有 EFT 结果已被判错。

### 13A. 必须明确的匹配关系

对文中采用的维五算符，先从原始 UV 拉氏量和质量本征态耦合独立复核匹配关系（当前手册记录的候选关系为）

\[
\frac{c_\alpha}{\Lambda}\simeq
\frac{y_\alpha\lambda_\alpha}{M_{E_\alpha}},
\qquad \alpha=\mu,\tau.
\]

该式必须与实际场归一化、质量矩阵、耦合定义和匹配阶数一致；不能仅凭文献中的相似公式确认。明确匹配尺度、被积分掉的 VLL、保留的算符集合、重整化方案以及树级/圈级精度。

### 13B. 最低验证要求

1. 对照当前 UV 拉氏量与 EFT 算符基底，核查 Wilson 系数的符号、维数、味指标和规范结构。
2. 说明 EFT 的适用能标与运动学条件，包括哪些质量阈值或新通道会使截断不再可靠。
3. 在同一组 UV 输入参数下，比较完整 UV 理论与截断 EFT 对至少一个与论文结论直接相关的振幅或可观测量的预测；定义截断误差指标和可接受阈值。
4. 对 Fig. 2 中被解释为 UV benchmark 的代表点，检查是否能映射到满足 VLL 质量、混合角、portal/标量条件及其他已采用假设的同一组 UV 参数。不能用分别来自不同 benchmark 的参数拼成一个“UV 实现点”。
5. 记录独立解析或数值复核、参数输入、代码/笔记本版本和输出；若尚无法完成定量比较，明确标记为未验证，不将其表述成 UV–EFT 一致性已经建立。

**建议写入论文的范围说明（只有在 T-13 验证完成后，按实际结果改写）：**

```latex
The effective-current description is used within the energy and
parameter domain where the stated matching conditions and operator
truncation are valid. The correspondence between the UV parameters
and the EFT coefficients is assessed at a common set of UV inputs;
the residual truncation uncertainty is [quantified result]. The
parameter contours shown below should therefore be interpreted as
[the validated benchmark projection / an EFT-only result in the
specified domain], rather than as a global classification of the UV
theory.
```

**依赖：** 与 T-05 的 VLL 参数一致性相关；若 T-01 引入新场或新带荷 VEV，须在扩展模型的同一组参数下重新检查匹配关系和适用能标。

------------------------------------------------------------------------

## Diff 14 — Fig. 2 基准保护与稳健性审计（新增研究任务 T-14）

**目标：** 最大限度保留已经完成的唯象学工作，同时不预设原图在 UV 修正后必然有效。Fig. 2 先作为参考基准冻结；后续根据可追溯的定量比较决定保留、局部修正或重算。

### 14A. 冻结基准，不预判结论

保存当前 v6 Fig. 2 的原始图文件（若当前源稿/资料库中可取得）、生成脚本/notebook（若存在）、网格定义、参数输入、约束数据/引用、插值与重铸方法、软件版本，以及生成图时采用的纯轴矢、VLL、动能混合和标量假设。若原始脚本或中间数据缺失，应把“恢复可复现基准”登记为前置工作，不得声称已完成冻结。对源稿和相关文件记录版本号或哈希。冻结的含义仅是建立可复现比较基线，不代表该图已经通过 UV 完整性或稳健性审计。

### 14B. 分项比较，避免把不同物理效应混成一个修正

| 检查项 | 对比内容 | 不能替代的证据 |
|:--|:--|:--|
| 有限 VLL 混合 / $g_V^\ell$ | 在同一 $(m_{A'},g_X)$ 网格上计算质量基底耦合，并分别应用矢量与轴矢量实验限制 | 不能只用 $\lvert g_V/g_A\rvert\ll1$ 推断实验影响很小 |
| 动能混合 $\epsilon$ | 从指定匹配条件演化到相关实验能标，计算诱导相互作用并比较约束 | 不能把匹配尺度取零等同于实验能标严格为零 |
| 中微子扇区 | 使用所选中微子扩展的同一组荷、质量矩阵和规范流，检查是否改变相关产生/衰变或实验约束 | 不能仅以“中微子扩展与 Fig. 2 无关”作为假设 |
| 标量 $s$ 与 portal | 比较物理标量谱、混合、产生率、总宽度、分支比及适用的标量搜索 | 不能把 $m_s\geq10\,\mathrm{GeV}$ 自动等同于完全退耦 |
| UV–EFT 映射 | 在同一 UV 参数点比较 UV 与 EFT 结果并评估截断误差 | 不能将不同 benchmark 的参数拼接成同一个 UV 点 |

### 14C. 量化标准与决策规则

对每一项修正，记录：输入点、使用的实验限制及版本、修正前后预测/排除边界、相对变化、数值/理论不确定度，以及变化是否超过预先声明的目标精度。目标精度应根据对应实验分析和论文结论确定，不得在看到结果后通过任意放宽阈值来保证原图不变。

按以下规则作出最终决策：

- **保留原曲线：** 仅当相关修正对目标参数域内的结论影响低于事先定义且有理由支持的精度，并且主要实验限制的适用性已核查。论文须明确 benchmark 假设与残余不确定度。
- **局部修正：** 若影响只出现在部分质量/耦合区域，更新受影响曲线、阴影或区域分类；保留其他已验证区域，并清楚标出未评估区域。
- **重算受影响的扫描：** 若相互作用结构、实验重铸、UV 参数映射或 EFT 适用性在大范围内改变，则重算相关扫描。只有当依赖关系确实要求时才重算全图，不因某个独立问题未解决就默认所有数值结果失效。

**必须保留的表述边界：** 纯轴矢有效理论限制不能自动表述为完整 UV 模型的全局实验允许区域。若中微子扩展尚未完成，必须明确模型完整性仍未解决；若标量、动能混合或有限 VLL 效应尚未定量验证，则相应区域标记为待评估，而不是默认未排除。

**与论文 Diff 的连接：** T-14 的结果用于决定 Diff 4–7、Diff 11 中哪些标量约束说明、参数表、图注、范围说明和曲线需要保留或更新；在 T-14 关闭前，不应把“原 Fig. 2 保持不变”写成最终结论。

### 14D. T-14A 可先行；T-14 最终关闭门槛

- **T-14A（可先行）：** 保存当前 Fig. 2、可获得的源文件/脚本、参数网格、原始约束数据、插值与重铸配置、软件版本和哈希。若脚本或中间数据缺失，状态只能是“基准恢复中”，不能声称已冻结出可复现基准。
- **T-14（最终综合审计）：** 最终关闭前，T-04、T-09、T-10 必须有明确结果；并且 T-01、T-02、T-03、T-05、T-06、T-07、T-08、T-13 中所有与该 benchmark/图域有关的检查都必须完成，或被逐项论证为 N/A。结果必须投影到同一套 UV 输入和一致的物理/实验假设，不能拼接来自不同 benchmark 的曲线或参数。
- **最小结案包：** (i) 基准输入/代码/数据版本与哈希；(ii) 各相关 T 任务状态与具体 claim 的 S0–S7 等级；(iii) 每项修正前后预测、边界变化、数值/理论不确定度；(iv) T-04/T-09/T-10 的显式验收记录；(v) 保留、局部修正或重算的理由；(vi) 更新后的图、图注和未评估区域标记。
- **禁止的结案方式：** 不能因 T-14A 已完成就关闭 T-14；不能因为图形看起来相似就判定稳健；不能将“未重铸”写成“实验不相关”；不能在尚有相关约束未评估时声称 Fig. 2 是完整 UV 模型的全局允许区域。

------------------------------------------------------------------------

---

## 决策更新（2026-10-27）：路线 B 已选

用户已明确选择：**保留原有轴矢量唯象学，收窄论文主张，不为本轮回复引入新的中微子/标量粒子。** 这取代本文件早期“作者仍需在扩展与范围限定之间作决定”的状态记录。

- **Major 3.1：** 解释 Weinberg 算符选择规则及残余 \(Z_2\)；明确维五允许项、维六 \(S\)-插入项和被禁止的电子—\(\mu/\tau\) 混合项。
- **Major 3.2：** 说明单独增加右手中微子不足以解除结构限制；不把 \(\sigma+3N_R\) 候选扩展作为本轮正式模型。
- **Major 4.1：** 采用与 Major 3 完全相同的结论；保留 Fig. 2 仅作为条件性纯轴有效流结果，不宣称完整 UV 模型点已经满足所有约束。
- **状态：** 路线决策已完成；主论文源稿修改、编译、最终章节/页码确认及正式回复信占位符清理仍未完成。Major 3 的物理限制被明确承认，但不应标记为“PMNS 已解决”。
- **会议依据：** [PR #11 会议记录归档](https://github.com/lm846802297-bit/axial-vector-review-response/pull/11)。
