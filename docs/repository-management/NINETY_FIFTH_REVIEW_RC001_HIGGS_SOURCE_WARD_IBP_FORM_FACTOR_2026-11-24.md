# Ninety-fifth supplemental document review — RC-001 Higgs source, Ward, IBP and form-factor records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation outputs and their paired Python sources  
**Disposition:** four `PASS_WITH_NOTES`; one `REVISION_REQUIRED`. All five exact source files were reconstructed from the fetched repository content, their Git blob identities were verified, and the scripts were compiled and executed locally.

## 1. Individual findings

| Validation output | Source and analytical review | Disposition |
|---|---|---|
| `RC-001-QLD-Higgs-source-EOM-model-map-audit.txt` | Exact source executed. The charged-lepton U(1)_X charge matrix, three gauge-allowed entries, six forbidden entries, distinction between gauge-allowed off-diagonal entries and the original flavour-diagonal model assumption, dimension-five source charges and inverse-`M_E` power counting reproduce the JSON output. | `PASS_WITH_NOTES` |
| `RC-001-QLD-UV-triangle-Ward-audit.txt` | Exact current source executed and its corrected-routing Ward contractions pass. The archived validation file also retains an earlier PASS 2 with the opposite sign for the heavy-line contraction, followed by a separately labelled corrected-routing block. The earlier PASS is not marked historical/superseded and conflicts with both the current source and the parent research note §4. | `REVISION_REQUIRED` |
| `RC-001-QLD-dim8-IBP-EOM-reduction.txt` | Exact source executed. The off-shell vertex combination, transversality, coefficient reparameterization, potential derivatives, charge boundary and unchanged scalar-source coefficient pass. The full covariant IBP/commutator derivation is separately recorded in the parent note §5K; the script is a coefficient/kinematic regression check, not a non-Abelian basis reduction. | `PASS_WITH_NOTES` |
| `RC-001-QLD-dim8-form-factor-projection.txt` | Exact source executed. The 12x3 off-shell amplitude map has rank 3, the selected minor is -6, Gram determinant is 3432, the on-shell collapse is reproduced, the charge-resolved hard coefficients reconstruct, the hard/full Ward relations hold, and the independent p^6 two-point coefficient is 1/192 in the declared normalization. The reported coefficients and matrix agree with the source calculations. | `PASS_WITH_NOTES` |
| `RC-001-QLD-dim8-scalar-source-EOM.txt` | Exact source executed. The f_H^2 expansion, all three pure-bosonic derivative coefficients, source-norm decomposition and unchanged c_S=1/192 pass. The operator identity `O_S ~= |D_mu(f_H H+J_H)|^2` is analytically derived in the parent note §5L by self-adjointness and two action-level integrations by parts; the script itself checks the resulting expansions and source cross terms, not the differential-operator identity independently. | `PASS_WITH_NOTES` |

## 2. Exact source and output identities

All five source files were reconstructed locally from the fetched contents. The computed Git blob SHA-1 matches the repository source blob for every script.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 | Source SHA-256 | Captured stdout SHA-256 |
|---|---|---|---|---|
| `RC-001-QLD-Higgs-source-EOM-model-map-audit.py` | `e0c1c309ef4d90b2029eb150e328a26cbc31e5fd` | `d9cb550505b5dd7a0bcc0120f26d35d6b1a539ac` | `7c69713b11edfcc4077b2a8f6b7b8d95abbc5ad00d6d9ec0d7469767ea293846` | `93a824737f8f75b76a0eae56c174309038ab7473f285cfe9c9d597995aff95b3` |
| `RC-001-QLD-UV-triangle-Ward-audit.py` | `1977d7d90f09c24dc2234f5f422c00bcaa628a5f` | `5e18915c60df7a76778aa90dc87379f7b5ad7b05` | `a7acbbf673d95926cc2b3874480a1e8b49a4971e663ce33e505492b7d28bb8c8` | `87b5f833a3720362aab657ae3acf00e35d933dd7a59fa1b6c3c39507ffad7e7e` |
| `RC-001-QLD-dim8-IBP-EOM-reduction.py` | `7e1260e55d5b2222b95735a2ed58e03bfe3e97b9` | `5de6c68b85cb7f52bd3c5d05803d6fbf185c399c` | `251f995765b97f71a53632414837a16cb2e989f9e15152874d6c3f342298b6d5` | `a3416ba6621ca541528df2cd23e1bf55cb37fb61555a5f0251030ddfe9f7ceed` |
| `RC-001-QLD-dim8-form-factor-projection.py` | `4c383a5ab558f069b230d96a080fe30e0f584a62` | `6616de248581d67c22c17f6861d8443ce68f5eac` | `67ba2a77e65d7fe85afcd16da1161afab61a248ae66d6e9a45f974f66f3bce1d` | `874f5bb07ed792fd542098bc849a4b268ee759ce521099a9ce1571f2a14f09d3` |
| `RC-001-QLD-dim8-scalar-source-EOM.py` | `67e32a861f466810af177bccdfead0a0a9024c34` | `ffcf2b3958cd58d1180eb267dc562821f732684b` | `915c9b443f7a22d3ff7d16677d3427fdf25d3b50a910e926c761928e5f694dde` | `866913328abd9bd3aa2e1b38ce367b6539db2746c2a6f1ace0feae73566a4bd3` |

## 3. Execution environment and reproducibility

- Python `3.13.5`; SymPy `1.14.0` for the symbolic scripts.
- Linux `6.18.57-x86_64-with-glibc2.41`; architecture `x86_64`.
- All five scripts passed `py_compile` and executed with exit status zero.
- The model-map script uses the Python standard library; the other four use SymPy.
- The current UV-triangle script output matches the corrected-routing part of the archived note. The archived file as a whole is not a byte-identical stdout capture because it contains the older contradictory PASS block and additional explanatory material.

## 4. Required correction: UV-triangle Ward record

The current source and the parent research note §4 agree on
[
q_\mu N_E^\mu
=2\left[(K'\cdot k)(K^2-M_E^2)
-(K\cdot k)(K'^2-M_E^2)\right].
]
The archived output's first PASS 2 instead gives the negative of this expression. The later `CORRECTED ROUTING` block has the correct sign and matches the current source, but the earlier line remains presented as PASS.

Keep the source and historical record. Update the validation document so the earlier line is explicitly marked as a superseded routing/sign result (or remove it from the current PASS block), and make the corrected contraction the sole current PASS statement. No new loop integral or Wilson coefficient is implied.

## 5. Register disposition

The five output paths are updated individually in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four to `PASS_WITH_NOTES`; the UV-triangle Ward output to `REVISION_REQUIRED` until its stale contradictory PASS line is clearly retired. The analytic derivations in parent-note §§5K and 5L are cited as the source for the covariant IBP and scalar-source EOM identities; those identities are not falsely attributed to the smaller Python assertion set.
