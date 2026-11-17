# Individual review: B5 portal RGE and EFT work records

Reviewed commit: `2cf34fd5` plus the present local review edits, 2026-11-15. This batch covers six baseline Markdown documents. Four associated production scripts were rerun; no external PyR@TE/SARAH calculation, full EFT anomalous-dimension matrix, complete matching-scale cancellation, or physical pole prediction is claimed.

| Document | Outcome | Findings and disposition |
|---|---|---|
| `research/major1-higgs-scalar-mixing-20261109/A5B_RGE_CLOSURE_MATRIX_AND_WORK_ORDER_2026-11-10.md` | `PASS_WITH_NOTES` after clarification | The closure matrix consistently separates UV portal running, the restricted `C5 C5*` derivative source, other EFT mixing, and dimension-eight work. It correctly says external RGE-generator validation and full EFT closure remain open. Its chronology section contained an old `C3_WW=3/4` projection beside the corrected exact-routed result; that older value is now explicitly labelled superseded and retained for history. A duplicated sentence was removed. |
| `research/major1-higgs-scalar-mixing-20261109/B5_1B_SM_RUNNING_INPUTS_20TEV_2026-11-11.md` | `HISTORICAL` | The document itself labels its older Buttazzo-type input set and `D_SM` portal-beta subtotal as superseded. Re-execution of `b5_1b_sm_running_20tev.py` reproduces its five couplings and diagnostic subtotal. Keep the file for provenance; use the PDG-2025 matched threshold record for current coupled work. Do not combine the two input schemes. |
| `research/major1-higgs-scalar-mixing-20261109/B5_1B_SM_THRESHOLD_AND_COUPLED_UV_RGE_2026-11-11.md` | `PASS_WITH_NOTES` | Re-execution of `b5_1b_sm_threshold_and_uv_rge.py` reproduces the listed weak-scale match and 20 TeV inputs, corrected coupled beta functions, and upward diagnostic. The text appropriately says Benchmark A is already at the adopted `lambda_tau^2 = 4*pi` boundary and that B is only a one-loop diagnostic. External generator, two-loop input uncertainty, EFT running below threshold, and full matching-scale cancellation remain open. |
| `research/major1-higgs-scalar-mixing-20261109/B5_1D_PYRATE3_MODEL_INPUT_NOTES_2026-11-11.md` | `PASS_WITH_NOTES` | This is a preparation/checklist note, not a PyR@TE result. It states the charge and potential conventions, keeps `g_YX` explicit until its beta source is checked, pins an upstream commit, and lists acceptance steps. The actual generator/gauge-invariance/RGE execution remains incomplete; no external validation is claimed. |
| `research/major1-higgs-scalar-mixing-20261109/B5_1_FULL_UV_PORTAL_BETA_FUNCTION_2026-11-11.md` | `PASS_WITH_NOTES` | Re-execution of `b5_1_uv_portal_beta_audit.py` passes the four recorded symbolic checks and reproduces the portal-beta decomposition. The derivation is explicitly restricted to a common threshold and `chi(M_E)=0``; the additive VLL box is distinct from the finite threshold, and the full beta is not applied below `M_E`. Independent PyR@TE/SARAH or diagrammatic validation remains open. |
| `research/major1-higgs-scalar-mixing-20261109/B5_2A_C5_SQUARED_AND_QUARTIC_EOM_BLOCK_2026-11-11.md` | `PASS_WITH_NOTES` | Re-execution of `b5_2a_c5_squared_operator_block.py` reproduces the A/B coefficient values, common-`S` tau orientation, Fierz relation and `beta_cpartialHS = Delta_lambdaHS_E/2` identity. The note correctly limits the result to the `C5 C5*` current/4-fermion and quartic-EOM sub-block; gauge mixing, full basis closure and Ward/LSZ completion remain open. |

## Reproduction

Commands run from the repository root:

```bash
python research/major1-higgs-scalar-mixing-20261109/b5_1b_sm_running_20tev.py
python research/major1-higgs-scalar-mixing-20261109/b5_1b_sm_threshold_and_uv_rge.py
python research/major1-higgs-scalar-mixing-20261109/b5_1_uv_portal_beta_audit.py
python research/major1-higgs-scalar-mixing-20261109/b5_2a_c5_squared_operator_block.py
```

All four exited zero. The first is an older superseded input scheme; the second is the later PDG-2025-based scheme. Their different 20 TeV couplings are expected because they use different weak-scale inputs and matching prescriptions; they are not interchangeable. The PyR@TE model was not executed in this review.
