# Second document review batch — 2026-11-14

## Scope

Audited branch: `maintenance/repository-organization-audit-20261114`.

This batch covers 20 complete Markdown documents: execution/deliverable/calculation navigation, extraction provenance, immutable reply-letter manifests, historical PMNS/VLL notes, and Major 1 portal evidence. Review included the complete retrieved document text, declared role and authority, status qualifiers, source/provenance statements, and internal Markdown references visible in each file. It is a documentation/provenance review, not an independent re-derivation of the physics.

## Individual outcomes

| Document | Outcome | Findings and action |
|---|---|---|
| `审稿意见-gpt/当前执行/README.md` | REVISION_REQUIRED | The opening warning correctly points to root `PROJECT_STATUS.md`, but the body still routes users to older PR #30/#40-era task paths and describes the 2026-11-04 reply-letter source and PR #40 as current. Refresh the entire task table and formal-response pointer against the 2026-11-14 live status; preserve the historical links in a dated subsection. |
| `计算脚本/README.md` | REVISION_REQUIRED | The 2026-10-20 index is stale and appears to describe legacy section 250–262 / DeepSeek66 materials, not the current Axial-vector calculation inventory. Several entries may be historical or unrelated to the active research workstreams. Do not move/delete them yet. First identify ownership and whether this directory is a retained legacy package; then split legacy and current scripts into clearly labeled indexes. |
| `deliverables/README.md` | PASS_WITH_NOTES | Good distinction between extracted deliverables and ZIP containers; provenance and SFHo source-data exception are explicit. Add a generated package inventory/checksum validation command when available. |
| `deliverables/Overleaf_Reply_Letter_PR72_2026-11-13/README_Overleaf.md` | PASS_WITH_NOTES | Clear blank-project import and compile sequence; correctly separates the reference PDF from TeX inputs. The compile recipe is documented, but this review did not run Overleaf/pdfLaTeX. |
| `deliverables/Overleaf_Reply_Letter_PR72_2026-11-13/EXTRACTION_PROVENANCE.md` | PASS_WITH_NOTES | Strong archive size/hash, source commit, embedded-manifest and ZIP CRC provenance. Verify actual file bytes against the package SHA256SUMS in a separate binary-capable check; no binary files were downloaded in this review. |
| `deliverables/higgs_portal_mixing_md_with_svg/EXTRACTION_PROVENANCE.md` | PASS_WITH_NOTES | Original archive size/hash and extraction CRC are recorded; add the exact source commit/branch and checksum-manifest hash if available. |
| `archive/reply-letter/snapshots/2026-11-04/manifest.md` | PASS_WITH_NOTES | Immutable snapshot identity and original Git blob IDs are documented. It explicitly explains the missing root-level JHEP style and later corrected snapshots. Keep as historical; do not restore over current source. |
| `archive/reply-letter/snapshots/2026-11-04-r2/manifest.md` | PASS_WITH_NOTES | Detailed source blob identity, build ancestry, compile sequence and visual review record. The recorded 44-pt overfull NA64 table warning remains disclosed; CI and raw log retention are not claimed. Historical snapshot only. |
| `审稿意见-gpt/当前执行/PMNS_Major3路线决策与扩展模型解析核查_2026-10-27.md` | HISTORICAL | Clearly states the optional seesaw is a response-only construction and not the original model; explicitly records tree-level reconstruction versus fit, LFV, cosmology, vacuum and global phenomenology limitations. Later 2026-11-04 rerun updates earlier “script not run” statements. Preserve as dated history; current Major 3 stance must come from current decision ledger/status. |
| `审稿意见-gpt/当前执行/分支成果核查与main同步记录_2026-10-27.md` | HISTORICAL | A branch/PR audit snapshot with explicit 2026-10-27 commit baseline. It must not be used to infer today's branch state. Preserve as historical. |
| `审稿意见-gpt/当前执行/审稿意见原子条目59项-v5.7.1至v5.6任务映射-20261026.md` | HISTORICAL | Correctly says it is a mapping index, not physics evidence, and identifies its historical state source. The referenced v5.6 status snapshot is no longer current. Keep as task-traceability history. |
| `审稿意见-gpt/当前执行/审稿执行手册_v5.6-与重构主分析逐项覆盖审计-20261019.md` | HISTORICAL | Narrowly scoped coverage audit; no calculation claim. It is an old audit artifact and should remain frozen. |
| `审稿意见-gpt/当前执行/带电轻子VLL完整质量矩阵与LFV一阶分析_2026-10-27.md` | HISTORICAL | Explicitly labels the sigma extension as an unadopted internal candidate and disclaims LFV rates/exclusions. Important model-boundary guardrail; keep archived and do not promote its assumptions into the original model. |
| `审稿意见-gpt/当前执行/研究证据/Major-Point-1_Portal-Threshold-Audit_2026-10-27.md` | PASS_WITH_NOTES | Strong provenance and claim-boundary discipline; distinguishes threshold algebra from complete diagram-level UV–EFT matching and physical scalar mixing. Remains partial evidence, not a closed Major 1 result. |
| `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Higgs_portal_exact_mass_eigenstate_one_loop_2026-10-27.md` | PASS_WITH_NOTES | Separates finite hard mass-eigenstate contribution from the incomplete EFT soft/counterterm set and physical pole treatment. Numerical agreement at a stated benchmark is not complete scalar-mixing validation. |
| `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Higgs_portal_mu_tau_loop_calculation.md` | PASS_WITH_NOTES | Correctly identifies the light-lepton loop as a subset rather than the complete UV self-energy and distinguishes EFT contact terms. Status says renormalized numerical evaluation remains incomplete. |
| `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Higgs_portal_planB_quantitative_assessment_2026-10-27.md` | PASS_WITH_NOTES | Scope is limited to low-energy diagonal mu/tau loops and contact tadpole; complete UV portal matching and near-degenerate physical poles remain open. Preserve as a benchmark assessment, not a global bound. |
| `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Higgs_portal_planC_lite_matching_and_complex_poles_2026-10-27.md` | PASS_WITH_NOTES | Explicitly distinguishes candidate derivative matching and first-pass complex-pole diagnostics from a complete momentum-dependent matrix, full counterterm set and Higgs recast. The near-degenerate region remains not assessed. |
| `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Major_Point_1_scalar_response_status_2026-10-27.md` | HISTORICAL | A dated response-workflow snapshot with several completion labels scoped to drafting/review rather than full scalar phenomenology. Preserve, but never treat “complete” labels as physical closure. |
| `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Major_Point_2_parameter_range_response_status_2026-10-27.md` | HISTORICAL | A dated internal response-status note. Its own text distinguishes response drafting from evidence limits; current status must be read from live status and decision sources. |

## Key repository findings

1. The current-execution README has a correct high-level warning but stale detailed PR and source pointers. It should be refreshed before the next contributor uses it as a task router.
2. `计算脚本/README.md` is a legacy index with a potential directory-ownership mismatch. This requires author/context confirmation before relocation.
3. The extracted Overleaf handoff package has unusually good provenance documentation. A separate binary checksum check should verify the actual committed files against its manifest.
4. Several older Major 1/3 documents are valuable because they explicitly prevent overclaiming. They should be marked historical, not deleted or silently merged.
5. The Plan B/Plan C-lite notes consistently retain the incomplete UV–EFT, pole and recast gates. Do not simplify their conclusions to “Higgs–singlet mixing solved”.

## Register update

The 20 outcomes above have been entered in `DOCUMENT_AUDIT_REGISTER.csv`. No scientific calculation, model parameter, numerical result or physical conclusion was changed.
