# Ninety-fifth supplemental document review — RC-001 Higgs source, Ward, IBP and form-factor records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation outputs and their paired Python sources  
**Disposition:** four `PASS_WITH_NOTES`; one `REVISION_REQUIRED`. This was a static source/output review; no fresh Python/SymPy execution or stdout comparison was performed.

## 1. Individual findings

| Validation output | Static source and analytic review | Disposition |
|---|---|---|
| `RC-001-QLD-Higgs-source-EOM-model-map-audit.txt` | The source encodes the charged-lepton U(1)_X charge matrix, gauge-allowed/forbidden entries, the distinction between gauge-allowed off-diagonal entries and the original flavour-diagonal assumption, dimension-five source charges and inverse-M_E power counting. | `PASS_WITH_NOTES` |
| `RC-001-QLD-UV-triangle-Ward-audit.txt` | The current source and parent research note §4 agree on the corrected heavy-line Ward contraction. The archived output also retains an earlier PASS 2 with the opposite sign, before a separately labelled corrected-routing block. | `REVISION_REQUIRED` |
| `RC-001-QLD-dim8-IBP-EOM-reduction.txt` | The source encodes the off-shell vertex combination, transversality, coefficient reparameterization, potential derivatives and charge boundary. The full covariant IBP/commutator derivation is separately recorded in parent note §5K; the script is a coefficient/kinematic regression record, not a non-Abelian basis reduction. | `PASS_WITH_NOTES` |
| `RC-001-QLD-dim8-form-factor-projection.txt` | The source encodes the rank-3 off-shell amplitude map, selected minor -6, Gram determinant 3432, on-shell collapse, charge-resolved hard coefficients, Ward relations and p^6 source coefficient. The archived output records these bounded projections and their limitations. | `PASS_WITH_NOTES` |
| `RC-001-QLD-dim8-scalar-source-EOM.txt` | The source checks the f_H^2 expansion, three pure-bosonic derivative coefficients, source-norm decomposition and unchanged c_S=1/192. The operator identity is analytically derived in parent note §5L; the script checks the resulting polynomial/source expansions, not the differential-operator identity independently. | `PASS_WITH_NOTES` |

## 2. Exact file identities

The source and validation-output files were fetched from the reviewed `main` tree. Git blob SHA-1 identifies each exact file. SHA-256 values identify source files and archived validation files, not captured stdout.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 | Source SHA-256 | Archived output SHA-256 |
|---|---|---|---|---|
| `RC-001-QLD-Higgs-source-EOM-model-map-audit.py` | `e0c1c309ef4d90b2029eb150e328a26cbc31e5fd` | `d9cb550505b5dd7a0bcc0120f26d35d6b1a539ac` | `7c69713b11edfcc4077b2a8f6b7b8d95abbc5ad00d6d9ec0d7469767ea293846` | `93a824737f8f75b76a0eae56c174309038ab7473f285cfe9c9d597995aff95b3` |
| `RC-001-QLD-UV-triangle-Ward-audit.py` | `1977d7d90f09c24dc2234f5f422c00bcaa628a5f` | `5e18915c60df7a76778aa90dc87379f7b5ad7b05` | `a7acbbf673d95926cc2b3874480a1e8b49a4971e663ce33e505492b7d28bb8c8` | `87b5f833a3720362aab657ae3acf00e35d933dd7a59fa1b6c3c39507ffad7e7e` |
| `RC-001-QLD-dim8-IBP-EOM-reduction.py` | `7e1260e55d5b2222b95735a2ed58e03bfe3e97b9` | `5de6c68b85cb7f52bd3c5d05803d6fbf185c399c` | `251f995765b97f71a53632414837a16cb2e989f9e15152874d6c3f342298b6d5` | `a3416ba6621ca541528df2cd23e1bf55cb37fb61555a5f0251030ddfe9f7ceed` |
| `RC-001-QLD-dim8-form-factor-projection.py` | `4c383a5ab558f069b230d96a080fe30e0f584a62` | `6616de248581d67c22c17f6861d8443ce68f5eac` | `67ba2a77e65d7fe85afcd16da1161afab61a248ae66d6e9a45f974f66f3bce1d` | `874f5bb07ed792fd542098bc849a4b268ee759ce521099a9ce1571f2a14f09d3` |
| `RC-001-QLD-dim8-scalar-source-EOM.py` | `67e32a861f466810af177bccdfead0a0a9024c34` | `ffcf2b3958cd58d1180eb267dc562821f732684b` | `915c9b443f7a22d3ff7d16677d3427fdf25d3b50a910e926c761928e5f694dde` | `866913328abd9bd3aa2e1b38ce367b6539db2746c2a6f1ace0feae73566a4bd3` |

## 3. Review boundary

No script was executed in this document-review pass. The source assertions, archived outputs and analytic parent-note derivations were inspected. The stale Ward sign line remains a concrete record inconsistency; it should be explicitly retired or labelled superseded before the output can be promoted.

## 4. Register disposition

The five output paths are individually recorded: four `PASS_WITH_NOTES), one `REVISION_REQUIRED). No fresh execution or byte-identical stdout is claimed. No other pending row is changed.
