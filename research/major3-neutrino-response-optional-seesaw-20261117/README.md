# Major 3 — optional neutrino-response construction

**Scope: response-only optional extension.**

## Scope and model boundary

This folder preserves the optional two-singlet type-I seesaw construction discussed in the Major 3/4.1 referee response. It is **not** part of the original manuscript's one-VEV (S+\mathrm{VLL}) model. The original minimal model's PMNS selection-rule limitation remains explicitly acknowledged; the optional (sigma+3N_R) completion is discussed only as a possible neutrino-sector completion in the response.

The numerical reconstruction is a constructive tree-level benchmark from NuFIT 6.1 central values. It is not a statistical fit, parameter scan, or check of HNL, LFV, scalar-potential/vacuum, cosmological, (A'), or global experimental constraints.

## Files

- `pmns_tree_level_reconstruction.py`: core tree-level mass-matrix and seesaw reconstruction.
- `reproduce_pmns_tree_level_reconstruction.py`: runner that executes the core script and writes the reproducibility JSON.
- `charged_lepton_vll_lfv.py`: separate 5×5 charged-lepton/VLL mass-matrix and kappa-induced LFV-current diagnostic. Its default point is explicitly illustrative; gauge-allowed off-diagonal entries set to zero are a texture assumption, not a consequence of (U(1)_X). It does not calculate branching ratios.
- `outputs/pmns_tree_level_reconstruction_2026-11-04.json`: saved input point, matrices, residuals and provenance. The relocation updates only the three path strings in its reproducibility metadata; numerical fields and the core-script hash are unchanged.

## Reproduction

From the repository root:

```bash
python research/major3-neutrino-response-optional-seesaw-20261117/reproduce_pmns_tree_level_reconstruction.py
python research/major3-neutrino-response-optional-seesaw-20261117/charged_lepton_vll_lfv.py
```

Dependencies: Python 3 and NumPy. The archived PMNS reconstruction used Python 3.14.7 and NumPy 2.5.4.

The runner uses `HERE.parents[1]` as the repository root. The new directory is still one level below `research/`, so this root calculation remains valid. The core calculation is unchanged; the runner's docstring and recorded invocation were updated to the new path. No numerical calculation was rerun for this path-only metadata migration.

## Provenance and limits

The saved PMNS construction is an existence demonstration for the optional extension, not evidence that the original paper model explains the observed full three-flavor mixing. Do not use this folder as the model baseline for Major 1, 2, 4.2, 4.3 or 4.4. The original one-VEV relations remain the baseline for all non-neutrino phenomenology.

See the [Major 3 response comparison](../../审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major3-中微子完成机制与论文修改对照_2026-11-04.md), [Major 3 validation record](../../审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major3-验证记录_2026-11-04.md), and the live [research decision ledger](../../审稿意见-gpt/项目规范/研究决策与不可回退事项.md).
