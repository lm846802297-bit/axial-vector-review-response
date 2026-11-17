# Individual review: Global-06 execution and protocols

Baseline `6b7c95c1e6d68d049add74dfeaa70a683f6b7b8f`; author-side review, 2026-11-15. Four documents were read individually and compared with the committed compact/high-order summaries, the two driver paths and the checked input profile. This review does not rerun B.13, verify external source literature, retrieve the conversation-only raw ZIP, or establish full-energy transport or an exclusion.

| Document relative to `research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/` | Individual findings and disposition |
|---|---|
| `GLOBAL06C_PROTOCOL_2026-11-14.md` | Proposed full-profile high-order follow-up; per-channel order, interpolation and B.1 gates are prospective. Changed “isolates and closes” to “is intended to isolate and close” and corrected two muon math tokens; neither edit changes a numerical result. Prior Global-07 integration does not constitute acceptance. PASS_WITH_NOTES. |
| `GLOBAL06_EXECUTION_NOTES_2026-11-14.md` | Dated Global-06 run guide and completed-stage summary. Two named drivers exist; its 28,679/540 and 431/2155 counts agree with recorded summaries; reported 0.0325955% / 0.0830916% / 0.0328258% agree to printed precision. The threshold-edge and Global-07 sequencing instructions are dated; a historical-stage warning is added. Raw 36 chunks are said to be in the conversation archive and were not checked here. HISTORICAL. |
| `P1B_GLOBAL06_LOW_X_FULL_RADIAL_PROTOCOL_2026-11-14.md` | Historical execution protocol; nine sqrt(x)-bisected knots independently reproduced, and 1687×17 = 28,679, 60×9 = 540. Both drivers and the profile SHA-256 `9fb14e79…` match paths/inputs. 0≤x<0.05 and global high-order coverage are excluded. Added historical-stage warning because later Global-07 work can exist without satisfying these acceptance gates. HISTORICAL. |
| `results/P1B_GLOBAL06_LOW_X_FULL_RADIAL_2026-11-14/REPORT.md` | Compact record of a completed low-order and targeted high-order stage; numerical summaries agree with report at quoted precision, while full global high-order acceptance remains false. Archive digest is recorded, but raw calculation data are not present in this directory and the conversation ZIP was not obtained or verified in this review. PASS_WITH_NOTES. |

The source profile is the digitized `research/stellar-cooling-constraints-20261105/data/sfho188_digitized.csv`, not the original simulation data. Its SHA-256 matches the protocol. The claimed 1% and 0.1% thresholds are local screening thresholds, not physical uncertainties. Distinguish 540 selected radial midpoints from all 1686 intervals, and 431 targeted high-order points from all 1687×17 local points.


## 2. Independent current-tree audit (2026-11-16)

**Disposition of this review report: PASS_WITH_NOTES.** The four original document dispositions and their numerical summaries are supported by the checked source records. This status applies to the review report's traceability and scope, not to global physical acceptance. The independent audit adds the producer-provenance qualifications below.

### 2.1 Numerical arithmetic and compact-summary cross-check

The nine formal knots are obtained by bisecting the five base knots in \(\sqrt{x}\):
\[
(0.05,\ 0.0728553391,\ 0.1,\ 0.1457106781,\ 0.2,\
0.2697875656,\ 0.35,\ 0.4216650066,\ 0.5).
\]
The eight independent validation knots are the corresponding \(\sqrt{x}\)-midpoints. Thus each of the 1687 radial vertices has 17 direct low-order evaluations:
\[
1687\times(9+8)=28\,679.
\]
The top-60 radial midpoint check is \(60\times9=540\), and the independent energy validation count is \(1687\times8=13\,496\). These independently reconstructed counts agree with the compact summary. The radial grid contains 1686 intervals.

The compact low-order JSON reports maximum energy-interpolation error \(3.2595519\times10^{-4}\) (0.0325955%), maximum top-60 radial-midpoint error \(8.3091615\times10^{-4}\) (0.0830916%), maximum detailed-balance residual \(6.86930\times10^{-15}\), maximum final-muon shell residual \(2.04324\times10^{-13}\), zero recorded charge-sum closure residual, and all rates finite/nonnegative.

The high-order summary reports 431 unique \((r,x)\) points, 2155 nominal ordered evaluations, all selected-point ladders passing, and maximum successive-order change \(3.28258\times10^{-4}\) (0.0328258%). Its high-order radial and energy interpolation maxima are 0.0831044% and 0.0325566%, respectively. The high-order detailed-balance and final-muon shell maxima are \(5.32446\times10^{-15}\) and \(2.46036\times10^{-13}\). These agree with the execution notes and the result report at their quoted precision.

The same high-order JSON explicitly sets `full_global_high_order_acceptance=false`. The compact summary also sets `x_below_0p05_covered=false`, `full_band_B1_B2=false`, `luminosity=false`, `fig7_passed=false`, `SN1987A_updated=false`, and `axial_limit_updated=false`. The 431-point selected convergence result must not be promoted to a full \(1687\times17\) high-order acceptance.

### 2.2 Producer and output-schema mismatch

The current Git low-order driver `run_p1b_global06_low_x_full_radial.py` writes `GLOBAL06_SUMMARY.json`, `RADIAL_NEIGHBOR_RANKING_TOP60.json`, `RADIAL_MIDPOINT_CHECKS_TOP60.json`, `ENERGY_INTERPOLATION_CHECKS.json`, and 48-radius chunk files. The committed compact artifact is instead named `GLOBAL06_COMPACT_SUMMARY.json` and has a compact schema (for example, `radial_nodes` and `direct_low_order_radial_node_evaluations`, rather than the driver's `profile_radial_nodes` and `direct_radial_node_evaluations`). The current driver does not write the committed compact-summary filename.

The current Git high-order driver reads the three detailed low-order files `GLOBAL06_SUMMARY.json`, `RADIAL_NEIGHBOR_RANKING_TOP60.json`, and `ENERGY_INTERPOLATION_CHECKS.json`, and writes `HIGH_ORDER_TARGETED_SUMMARY.json`. The tracked result directory contains only `HIGH_ORDER_ACCEPTANCE_SUMMARY.json`, not those inputs or the driver's output. The tracked high-order compact summary also contains `unique_r_x_points` and `nominal_ordered_evaluations`, fields not emitted by the current Git driver. A fresh low-order run could regenerate the required detailed inputs before the high-order driver is run, but the tracked compact artifacts alone cannot reproduce that sequence.

The archive provenance lists two different local-runner names and hashes (`run_global06_local_py` and `run_global06_highorder_local_py`); those runner source files are not in the reviewed Git tree. The cited `source_bundle_commit` `483efe3db148ed38aa59a323cc11569df21a81f6` contains the pinned profile and base B.13 audit kernel with the same Git blob IDs as the current tree, but it does **not** contain either current Git Global-06 driver. The current drivers are present at the report's reviewed base commit `6b7c95c1e6d68d049add74dfeaa70a683f6b7b8f` and at the maintenance-branch HEAD. Consequently, the base kernel/profile provenance is pinned, but byte identity between the archived local-runner sources and the current Git drivers is not established.

The archive manifest records `P1B_GLOBAL06_LOW_X_FULL_RADIAL_2026-11-14.zip`, 13,851,449 bytes, SHA-256 `54b4ce938034d154b2eeb7ede87f720e21eafb24e08f9743380fb313679c05df`. The ZIP itself and its raw 36 chunks are absent from the reviewed Git result directory; the digest is metadata, not verification of the archive bytes. The current tree therefore supports inspection of the compact summaries and a future fresh run, but not an independent byte-level audit of the original archived run.

### 2.3 Workflow, tests and Global-06C boundary

No Global-06-specific regression-test module or workflow was found. The existing `p1b-b13-local-kernel-radial-energy.yml` workflow runs the separate local B.13 audit/test on its own research branch; it does not invoke either Global-06 driver. The `p1b-source-bundle.yml` workflow packages a different set of P1-B sources on its configured branches and likewise does not execute the Global-06 low-/high-order drivers. The archive provenance explicitly records `ci_used_for_physics_calculation=false`. These workflows are not evidence that the Global-06 calculation ran in CI.

The `GLOBAL06C_PROTOCOL` remains a protocol, not an executed acceptance result. Its direction-diagnostic script exists, but no matching `GLOBAL06C_A_DIRECTION_DIAGNOSTIC.json` output is present in the reviewed tree. The threshold-edge smoke-test values quoted in the execution notes also have no paired machine-readable output in this result directory; they are not independently reproduced here. The \(0\le x<0.05\) coverage gate therefore remains open for this stage.

### 2.4 Current-tree edits since the stated review base

The three source documents whose blobs differ from the stated review base were checked line by line. The current `GLOBAL06C_PROTOCOL` changes “isolates and closes” to “is intended to isolate and close” and repairs the two \(\mu^\pm\) math tokens. The execution notes and low-\(x\) protocol each gained a historical-stage warning. These edits are consistent with the changes described by the original review; the compact `REPORT.md` and the two JSON summaries retain their original blobs.

**Final boundary:** the Global-06 low-order scan and selected high-order diagnostics are numerically supported by the archived compact summaries. The exact original local-runner source, raw chunk archive and full rerun are not independently verified from the Git tree. No full global high-order acceptance, \(x<0.05\) coverage, full-band B.1/B.2 transport, luminosity, Fig. 7 reproduction, SN1987A update or axial-vector exclusion is established. No production kernel, rate, opacity or limit was modified.
