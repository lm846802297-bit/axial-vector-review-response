# 第六十七轮文档审查：当前研究手册与 Major 4.2–4.4 技术审计

- 审查日期：2026-11-16
- 审查基线：\`09965f570a37cbfb3d2072db8ed20fc43ba6bc4d\`
- PR：[#115](https://github.com/lm846802297-bit/axial-vector-review-response/pull/115)
- 分支：\`maintenance/repository-organization-audit-20261114\`
- 当前状态参照：\`PROJECT_STATUS.md\`（2026-11-15 live status，blob \`8922a3f588d35d49931d3fd5f22618e170e4544a\`）
- 范围：台账前六份 PENDING 文档
- 本轮只新增审查报告、更新六条台账记录；不修改六份被审文档，不更改任何生产计算或物理输出。

## 1. 审查结论

| 文档 | Git blob SHA | 状态 | 核心判断 |
|---|---|---|---|
| \`审稿意见-gpt/审稿意见分析v5.7-物理校核与专题连续阅读版.md\` | \`5bda345daafc13f7f270302b01d1e829a2a5faae\` | PASS_WITH_NOTES | 保留为详细物理/技术参考；其研究状态段不能替代最新 live status。 |
| \`审稿意见-gpt/审稿意见原文逐句覆盖审计-v4.9.md\` | \`9f8df48aed1320c74477f8ab9a51657890ce1f4e\` | HISTORICAL | 被后续 v5.7 覆盖的审计版本；C0–C5 证据分层仍有追溯价值。 |
| \`审稿意见-gpt/当前执行/axial_vectorv6-diff-v2.2-原子映射与证据双轴-BelleII与Fig2闭环-2026-10-23.md\` | \`56d9a0d908ec3bc3101bec3a34f8d740edea0956\` | HISTORICAL | 文件自带历史归档声明；不得用其 T-00–T-14 状态覆盖 Route B 和后续 Diff。 |
| \`审稿意见-gpt/当前执行/审稿意见分析-gpt-v4.1-公式复核与PMNS方案建议-主题整合重构版-原文恢复修正版-20261019.md\` | \`f5195d8c3ba27bcc85724c78c248ea55f4f28813\` | HISTORICAL | 2026-10-19 分析版本；保留理论解释和原始审稿映射，不作为当前决策源。 |
| \`审稿意见-gpt/当前执行/审稿意见分析与执行手册_v5.6-主分析全任务映射与原子步骤版-20261019.md\` | \`ad7565b5f8cc35fad05b8b4d92577f1c93020855\` | HISTORICAL | §0.1 明确是 2026-10-27 状态快照，且声明 PROJECT_STATUS.md 为 live source。 |
| \`审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Major_Point_4_2_4_4_technical_audit_2026-10-28.md\` | \`3d5b8210b82bb760a1ad45e285ce38329ce7cfbf\` | HISTORICAL | 有价值的 benchmark 级计算和适用性记录，但明确未完成完整有限混合重铸或轴矢量 SN transport。 |

本轮六份：1 PASS_WITH_NOTES、5 HISTORICAL。未发现需要将原文标为 REVISION_REQUIRED 的确定性内容错误；主要问题是历史状态和证据等级必须隔离。

## 2. 当前权威状态源的核对

本轮先读取根目录 \`PROJECT_STATUS.md\`，而不是直接相信研究手册里的“当前状态”字样。其 2026-11-15 顶部 live-status 明确覆盖后续 PR #106/#113 的合并状态、PR #56 的合并状态以及较早的研究状态快照。

当前状态中与本批文档直接相关的事实：

- PR #56 已于 2026-11-12 合并，但合并不等于物理验收；纯 vector Blinov Fig. 7 的 10 MeV 强吸收端差异仍约为 +92.24691%，没有接受 opacity/profile rescaling，也没有更新 SN1987A 限制或轴矢量约束。
- 轴矢量 stellar-cooling 结果仍是条件性 benchmark，不是完整 SN1987A transport/exclusion 结果。
- Major 4.2–4.4 的较早计算结果需要与后续专题审计区分；不能把某个环图积分或某个生产机制的可迁移性等同于整条实验排除曲线。
- 当前权威文件表将 v5.7 定义为 2026-10-20 技术参考（按需读取），v5.6 仅为带 2026-10-27 历史状态快照的执行框架；正式回复信、正文待同步清单、研究决策文件和根目录 live status 各有不同职责。

因此，本轮采用如下文件分工：

1. \`PROJECT_STATUS.md\`：当前项目进度、PR/研究状态和近期结果的 live source。
2. 当前正式回复信：对审稿人的对外答复口径。
3. 当前研究决策与不可回退事项：Route B 等作者决策及变更历史。
4. v5.7：物理推导、概念解释和执行方法参考。
5. v5.6、v4.1、v4.9、Diff v2.2、2026-10-28 技术审计：历史版本或特定 benchmark 的证据记录，不自动决定当前状态。

## 3. v5.7 技术参考：PASS_WITH_NOTES

### 3.1 通过项

- 版本沿革和事实边界清楚；明确说明模型专属圈图系数、数值拟合、参数扫描和实验重铸必须在实际完成后才能确认。
- 四个 Major 采用一致的八段阅读结构，Major 1 与 Major 2 的 UV–EFT/portal 关系、Major 3 与 Major 4.1 的共享 PMNS 证据均有明确说明。
- 对 \(S\) 复场、径向态 \(s\) 和 Higgs 混合物理本征态作了区分。
- 对固定 \((m_{A'},g_X)\) 的条件性标量质量上界作了边界说明；明确指出该上界不提供正的质量下界，也不能自动成为实验允许区。
- 对 portal 四点函数与 \(h\)–\(s\) 两点混合自能作了区分；不把某个单图、某个重整化方案或小角公式误写成方案无关的物理结论。
- 对 PMNS 结构、Weinberg 算符、Takagi/SVD、近简并处理、BR 完备性、动能混合定义和证据等级有系统说明。
- v5.7 末尾明确写出：其完成的是公式逻辑校核、连续阅读结构和方法说明，不代表模型专属圈图、PMNS 数值拟合、实验重铸或联合扫描已完成。

### 3.2 必须附加的状态说明

v5.7 末尾“当前研究状态与结案边界”仍是该手册自身版本形成时的状态总结。它列出的 portal、PMNS 扩展、动能混合和实验重铸待办，不可直接当作 2026-11-16 的最新进度。

例如：

- PMNS：当前项目已选择 Route B，保留轴矢量唯象学并收窄论文主张；不应再把“候选扩展拟合”写成当前论文主线待执行项。
- Major 4.4：此后已完成更多 vector baseline、B.1/B.2、B.13 和轴矢量 benchmark 工作；但 2026-11-15 live status 明确仍未接受完整 axial SN1987A transport/exclusion 结果。
- Major 1：portal 软圈、硬阈值、匹配和极点工作在后续文档中已有更细分结果与失败边界；v5.7 的概括性待办不能替代这些后续专题证据。
- Major 2/UV–EFT：后续计算记录区分了子扇区验证、full dimension-8 matching、full model pole spectrum 和模型 benchmark；不能仅凭 v5.7 的方法章节认定闭环。

**使用规则：** v5.7 保留为详细技术参考；引用其中任何“当前仍待完成”或“已完成”的状态时，必须回到对应的最新专题报告和 \`PROJECT_STATUS.md\` 核对。

## 4. v4.9 原始审稿逐句覆盖审计：HISTORICAL

v4.9 的核心贡献是把覆盖层次拆开：

- C0：原文登记；
- C1：语义澄清；
- C2：物理解释；
- C3：执行方案；
- C4：科研证据；
- C5：正文修改并回复；
- OPEN：至少一个必要层次仍未完成。

这一分层非常重要，避免“原文已登记”“章节已有解释”被误报为科研完成。该文还说明新增 3 个来源核查项后总计 59 项登记，但明确指出登记数量不等于科研结果完成。

历史状态冲突：

- v4.9 对审稿报告与当前 v6 的 Eq. (30)/(34) 差异仍把“实际送审版本待投稿记录确认”作为来源事实问题；后续项目已决定不再追查该 PDF 版本作为阻塞项。
- v4.9 的 Major 4.2、4.3、4.4 科研状态均仍标为待完成；后续已分别产生动能混合 benchmark、有限 vector coupling 和 stellar-cooling 专题工作。
- v4.9 的 59 项覆盖是登记/映射事实，不代表所有 59 项达到 C4/C5。

**处理：** 保留为历史审计版本，不回写旧文档；需要查原始逐句映射时可以使用，但当前科研状态以最新记录为准。

## 5. Diff v2.2：HISTORICAL

该文件头部已正确声明：

- 归档日期为 2026-10-23；
- 不再是唯一主文档或当前状态源；
- 当前任务状态当时指向 v5.6 §0.1；
- 最新修改方案指向 PR #14 的 Diff v2.4；
- T-00–T-14 与 59 个原子 ID 的桥接关系已并入 59 项原子映射表；
- 本文件不代表计算、实验重铸或论文修改完成。

本轮未发现应撤销其历史归档标记的理由。其“完成时回复信可能超过证据状态”“Fig. 2 不能预设必然稳健或全部失效”“有限 \(g_V\) 与 \(\epsilon\) 分开处理”等原则仍值得保留，但不能把旧 T 任务状态作为当前状态源。

## 6. v4.1 主分析：HISTORICAL

v4.1 保留了完整的物理解释和审稿人原文，具有历史研究价值。其自身头部已指出：

- 版本日期为 2026-10-19；
- 执行任务当时交给 v5.4 手册；
- 其后按 2026-10-26 决策，不再追查实际送审 PDF 版本；
- Route A 的奇荷标量/右手中微子扩展只是候选模型设计，不能当作已验证方案；
- 最小模型 PMNS 的电子味与 \(\mu-\tau\) 子块分离是有明确荷分配假设的结构性结论。

但其优先级和科研状态是早期版本。当前论文已经选择 Route B：保留原轴矢量唯象学并收窄论文主张，不将 \(\sigma\) 或 \(\sigma+3N_R\) 扩展纳入本轮模型。Major 3 与 Major 4.1 应按当前正式回复口径处理，不应从 v4.1 的旧模板复制尚未完成的扩展拟合措辞。

## 7. v5.6 执行手册：HISTORICAL

v5.6 的文件头和 §0.1 均明确声明：任务卡和阶段关卡是执行框架，§0.1 只记录截至 2026-10-27 的历史状态，当前状态以根目录 \`PROJECT_STATUS.md\` 为准。

仍有价值的结构：

- 任务状态与 S0–S7 证据成熟度分轴；
- 任务记录必须包含模型版本、输入、脚本、输出、独立复核、结果和后继任务；
- 将 PMNS、portal、UV–EFT、动能混合、有限 VLL、实验/天体物理约束和正文回复分开管理；
- 专项停机门要求：portal 匹配未统一不宣称混合已量化；未做阈值和实验比较不填动能混合终值；实验适用性不明时标“未评估”而非“允许”。

历史状态表中仍有 2026-10-27 的待办和旧 benchmark 结果，不能当作当前待办或最新结果。例如其对初始参数表、全局真空、硬阈值精度、完整复极点、Belle II 重铸等状态，必须由 2026-11 专题文件重新确认。

**处理：** 不删除任务 ID、不修改历史勾选；只在台账标记 HISTORICAL。

## 8. Major 4.2–4.4 technical audit（2026-10-28）：HISTORICAL

### 8.1 Major 4.2：动能混合

该文计算采用：
\[
\theta_{\mu R}=\theta_{\tau R}=10^{-2},\quad
M_{E_\mu}=M_{E_\tau},\quad \chi_{\rm UV}=0
\]
并在声明的 matching scale 设定无额外 bare low-energy kinetic mixing。该等角、等重态质量基准下，轻带电轻子 vector charge 大小相等、符号相反，因而可以使用动量依赖的 \(\mu/\tau\) loop 表达式。

文中给出的零动量结果：
\[
|\epsilon_{\gamma A'}(0)|\simeq1.4433\times10^{-6}|g_X|
\quad(\theta_R=10^{-2}),
\]
并给出 on-shell \(q^2=m_{A'}^2\) 的复积分数值表。对于 \(g_X=0.1\)，其零动量估计约为 \(1.44\times10^{-7}\)，on-shell 表格最大值约为 \(2.12\times10^{-7}\)。

重要限制也写得正确：

- 等混合角的抵消不能从 \(|\theta_{\ell R}|\le10^{-2}\) 两个独立上限自动推出；
- 不等角时需统一处理重阈值、counterterm 与 electroweak-scale matching；
- spacelike 过程必须使用该过程的 \(q^2\)，不能把 on-shell 表格当作所有实验的通用值；
- NA64 的比较只针对 induced electron-production channel，不替代其他实验或 SN 适用性分析。

### 8.2 Major 4.3：有限 vector component

该文得到：
\[
\left|\frac{g_V^\ell}{g_A^\ell}\right|
=\tan^2\theta_{\ell R}\le1.0001\times10^{-4}
\]
（给定 \(\theta_{\ell R}\le10^{-2}\)）。

对 trident 的 leading SM-interference coupling-level estimate 和 \((g-2)_\mu\) vector/axial loop ratio，文中分别给出条件性数量级；同时明确 trident 估计未包括不同的有限 \(m_\mu\) response functions，且 dimuon threshold 附近 vector width 可能相对重要。

该文没有声称 vector constraints 对所有 observable 都必然弱于 axial constraints，并明确 Fig. 2 仍是 pure-axial EFT contours，而不是完整 finite-mixing UV-model classification。这些边界是正确且必须保留的。

### 8.3 Major 4.4：超新星/恒星约束

该文正确区分：

- 固定 \((m_{A'},g_X)\) 下，树级 neutrino coupling 不变，因此 neutrino coalescence production matrix element 和 neutrino partial widths 可直接迁移；
- charged-muon semi-Compton production/absorption 依赖 charged-muon current，vector 结果不能直接迁移到 axial coupling；
- \(m_{A'}>2m_\mu\) 后，轴矢量 dimuon width、BR、lifetime、trapping、high-energy neutrino flux 和低能超新星能量沉积需模型专属重算；
- 不能宣称所有 SN1987A 或低能超新星限制都次主导或不适用。

### 8.4 后续进展与当前边界

该审计是 2026-10-28 的 benchmark-level 记录。其文件头已经声明不是完整 finite-mixing collider recast，也不是完整 axial-current supernova transport calculation，且当时未修改论文源码。

此后 PR #56 已合并，并开展了更多固定 profile 的 axial-EFT ballistic-cooling benchmark 和 B.1/B.2、B.13 等研究。但 2026-11-15 live status 仍明确指出纯 vector Fig. 7 的 10 MeV 强吸收端差异未解决，轴矢量曲线仍为条件性结果，不是完整 SN1987A transport/exclusion 结论。

**处理：** 该技术审计作为历史 benchmark 证据保留。它的公式和数值只在原 benchmark 条件下引用；任何新的总约束结论必须引用后续独立计算和当前 live status。

## 9. 交叉文档发现与纠正原则

| 易混淆事项 | 正确区分 |
|---|---|
| 手册中写了推导 | 不等于实际模型圈图/数值已完成 |
| 原文逐句登记 59 项 | 不等于 59 项都已取得 C4/C5 科研与论文证据 |
| Route B 已选择 | 表示当前论文不采用新增粒子扩展；不表示最小模型 PMNS 与观测兼容 |
| 等角 benchmark 的 \(\epsilon(q^2)\) 表 | 不等于不等角、任意 VLL 质量或所有动量转移下的通用结果 |
| \(g_V/g_A\ll1\) | 不自动证明所有 vector-sensitive 实验约束都可忽略 |
| neutrino coalescence 可迁移 | 不等于整条 vector SN cooling exclusion curve 可迁移 |
| PR 合并 | 不等于对应物理结论已被科学验收 |
| 实验质量覆盖 | 不等于本文模型在该质量点被排除 |

## 10. 台账更新

第六十六轮后：
- PASS_WITH_NOTES：257
- PASS：2
- REVISION_REQUIRED：24
- HISTORICAL：113
- PENDING：66
- 已审查：396 / 462

第六十七轮后：
- PASS_WITH_NOTES：258
- PASS：2
- REVISION_REQUIRED：24
- HISTORICAL：118
- PENDING：60
- 已审查：402 / 462（87.0%）

本轮只新增审查报告，并更新六条台账记录；六份原始文档保持不变。

## 11. 下一轮

继续从最新台账前六份 PENDING 文档开始。优先检查 2026-10-27 之后形成的当前专题计算报告和论文修改一致性文件，逐项核实其输入 SHA、参数、公式、输出、独立复核、证据等级及当前正式回复落点。不得因为文件名带有“final”“complete”或 PR 已合并就直接认定物理结案。


## 12. Live-status source refresh (2026-11-16)

The `PROJECT_STATUS.md` blob cited in this review was the 2026-11-15 snapshot. The current live-status document has since been updated (blob `84d2f8ac0cb473c51bc1d5003c58d9719f5ded79`) to reflect the latest audit registers: baseline 462/462 reviewed with 293 PASS_WITH_NOTES, 2 PASS, 153 HISTORICAL and 14 REVISION_REQUIRED; supplemental 110 rows with 29 PASS_WITH_NOTES and 81 PENDING; baseline fingerprints 404 MATCH_CURRENT, 55 CONTENT_FINGERPRINT_DIFFERS and 3 SIZE_METADATA_DIFFERS. The earlier 2026-11-15 status values in §§1–2 remain a dated snapshot, not current counts. The six documents reviewed in this round retain their individual dispositions; this update changes no physics result or paper-response decision.
