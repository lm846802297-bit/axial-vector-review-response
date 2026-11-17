# Individual review: pole, scalar and UV RGE output summaries

Baseline `10484c2c983c45da2050c1a81868928d92ebc536`, 2026-11-15. The ten documents below were read. Seven corresponding scripts were executed under Python 3.12.14, NumPy 2.3.5 and SymPy 1.14.0. The matrix/fermion/counterterm suites ran 23 tests, and the older isolated snapshot suite ran 4. These checks do not replace complete bosonic/fermionic matching or a gauge-complete observable.

| File under `research/major1-higgs-scalar-mixing-20261109/` | Individual outcome and limitation |
|---|---|
| `B5_1B_SM_THRESHOLD_AND_UV_RGE_OUTPUT_2026-11-11.txt` | Coupled one-loop driver exits 0; selected threshold, zero-crossing, A/B 40 TeV and symbolic entries agree at reported precision. A trajectory lies outside strict perturbativity immediately above 20 TeV; lower-energy EFT RG remains incomplete. PASS_WITH_NOTES. |
| `cms_vector_cascade_audit.txt` | Corresponding script exits 0 and the branching fractions, pole ratio and cascade estimate agree to reported precision. An isolated-pole number is not a CMS detector likelihood. PASS_WITH_NOTES. |
| `exact_momentum_pole_audit.txt` | Driver exits 0 and selected pole figures agree to reported precision, **but the current rerun emits SciPy IntegrationWarning at line 42**: roundoff prevented its requested integration tolerance. Added a warning without changing archived values. Numerical integral convergence/error control needs follow-up; fixed diagonal widths and incomplete counterterms/gauge sector are additional limitations. REVISION_REQUIRED. |
| `fermion_sector_matrix_tests.txt` | Historical five-test log; its corresponding current suite passes within the 23-test rerun. It is not a full bosonic/gauge pole calculation. HISTORICAL. |
| `independent_fermion_sector_audit_snapshot_20261113/outputs/independent_fermion_sector_tests.txt` | Historical four-test snapshot; the tests within the snapshot directory reran successfully. Earlier checksum README provenance caveat remains as recorded in the manifest review. HISTORICAL. |
| `independent_fermion_sector_tests.txt` | Historical two-suite nine-test log; the corresponding current tests pass within the 23-test run. These selected fermion/tadpole checks do not close the full theory. HISTORICAL. |
| `pole_residue_audit.txt` | Plan-C-lite pole-residue driver exits 0 and selected outputs agree at displayed precision. Residues are complex and are not probabilities or signal strengths; fixed widths and selected kernel remain. PASS_WITH_NOTES. |
| `portal_higgs_constraint_validation.txt` | Associated approximate single-pole audit exits 0. Its one-sided signal-strength estimate is conditional and not a detector likelihood or complete complex-pole result. PASS_WITH_NOTES. |
| `scalar_potential_symbolic_audit_validation.txt` | Tree-potential symbolic script exits 0 and its declared derivative checks match the log. No loop renormalization is established. PASS_WITH_NOTES. |
| `singlet_scalar_width_audit_validation.txt` | The tree-width script exits 0 and tabulated A/B partial sums and perturbativity-ceiling ratios agree to displayed precision. Mixing-induced and higher-order channels are excluded. PASS_WITH_NOTES. |

The SciPy warning is a newly observed limitation, not proof that all listed values are wrong. It must be resolved with a numerical convergence/error analysis before assigning the printed digits a precision claim. No archived pole or width numbers were overwritten.
