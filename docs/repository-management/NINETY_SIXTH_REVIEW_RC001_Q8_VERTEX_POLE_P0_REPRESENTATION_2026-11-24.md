# Ninety-sixth supplemental document review — RC-001 Q8 vertex, line-pole, P0 and representation records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation outputs and their paired Python sources  
**Disposition:** four `PASS_WITH_NOTES`; one remains `PENDING` because its paired source could not be located. Four exact source files were reconstructed, their Git blob identities verified, compiled and executed; all four stdout captures match the archived outputs byte-for-byte.

## 1. Individual findings

| Validation output | Source and execution review | Disposition |
|---|---|---|
| `RC-001-QLD-hard-degree5-integrand.txt` | The output claims all shifted propagators were expanded and the total-degree-five coefficients were generated, with term counts for the light/heavy attachments. No paired source was found at the expected `upstream/calculations/RC-001-QLD-hard-degree5-integrand.py` path or the checked common filename variants. Without the producer source and its exact identity, the reported term counts cannot be independently reproduced. | `PENDING` |
| `RC-001-dimension8-Q8-one-background-vertex-audit.txt` | Exact SymPy source executed. The Q8 contact Ward contraction, ordinary-line propagator identity, traced numerator contraction, Q_LD/Q_RD composite charges and direct B/X/W contact assignments all passed. Stdout matches the archived output byte-for-byte. This is an algebraic building-block check, not an integrated loop amplitude. | `PASS_WITH_NOTES` |
| `RC-001-dimension8-Q8-one-background-line-pole-covariant.txt` | Exact SymPy source executed. The invariant angular averages, Feynman-parameter integrals, transverse UV coefficients and integrand-level Ward identity passed. Stdout matches the archived output byte-for-byte. The code uses d-dimensional angular moments and evaluates the UV-pole residue at d=4; it does not calculate the finite O(epsilon) part, contact graph, R* subtraction or hard matching. | `PASS_WITH_NOTES` |
| `RC-001-dimension8-P0-independent-coefficient-audit.txt` | Exact SymPy source executed. The local polynomial remainder, coefficient-by-coefficient hard-IR/soft-UV cancellation, matching-scale cancellation, crossing symmetry, all 16 SU(2) assignments and action-to-amplitude normalization passed. Stdout matches the archived output byte-for-byte. The source explicitly rechecks the printed coefficients algebraically; it does not repeat loop integration or diagram generation. | `PASS_WITH_NOTES` |
| `RC-001-dimension8-Q8-representation-audit.txt` | Exact Fraction source executed. For both muon and tau assignments, H-dagger L and S_l l_R have the same singlet representation and (Y,x)=(-1,eta_l); the Q8 connection contains B and X but no direct W insertion. Stdout matches the archived output byte-for-byte. This is charge/representation bookkeeping only. | `PASS_WITH_NOTES` |

## 2. Exact source and output identities

All four available source files were reconstructed locally from the fetched repository contents. The computed Git blob SHA-1 matches the repository source blob for every script.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 | Source SHA-256 | Captured stdout SHA-256 |
|---|---|---|---|---|
| `RC-001-dimension8-Q8-one-background-vertex-audit.py` | `213a89fea0b6494cbc1a173914ef7588c0af06a2` | `b82b692136099760f23fcfe514351f0ad3acc057` | `3cce521676fb4b504d4201e03ba619aac129e2f843f32803d97cdb620d14452a` | `3ab1843361f7f49846246b992bac24c6c9fef4b24e75f033d53363758904325f` |
| `RC-001-dimension8-Q8-one-background-line-pole-covariant.py` | `7222f8fc551e22f59fcd432ca25b4a6ba35548c6` | `cfcc55503ee6848276e62abb242d6df64a8e13af` | `b1d9608fe46a62378fca0c319e69cd3dc59a38a932ed667d808f7479f2881e7a` | `4bae28e9c1dc28b609beee273590405fba2335cf0e782e734c98f7f6feb61742` |
| `RC-001-dimension8-P0-independent-coefficient-audit.py` | `82178a825c753cb02d3fa6e6e4b8da687b017020` | `5ef27c66cac11001a4ea52f381890fbb6a0ee5b0` | `5dc4000f637419f2dc32a85cc847495ef0545f28a120bbf30cbab29fe7aee95b` | `10bb5f66c104c1e679d189bea14da877c8ea82cb513b3ce26e1dbac4e1eeb319` |
| `RC-001-dimension8-Q8-representation-audit.py` | `f00a152a84e2eb342dfbf20d3e4013ec8490e089` | `dd4d263872c6da11c46d607066d341bc947e33c7` | `d81e08af89412bedd7ade9fbf96b8125fd4db985f273189a96ffd5b4755a8658` | `bc812602001651d1d758cc49a397c42a9b4ad70fa7ac3021eeec7f4959a3c542` |

## 3. Execution environment and reproducibility

- Python `3.13.5`; SymPy `1.14.0` for the three symbolic scripts; the representation audit uses exact `fractions.Fraction` arithmetic.
- Linux `6.18.57-x86_64-with-glibc2.41`; architecture `x86_64`.
- All four available source scripts passed `py_compile` and executed with exit status zero.
- All four captured stdout files matched the corresponding archived validation output byte-for-byte.
- The QLD hard-degree-five producer source was not located; no source SHA-256, runtime record, or rerun is claimed for that output.

## 4. Register disposition

The five output paths are updated individually in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four to `PASS_WITH_NOTES`; the hard-degree-five integrand output remains `PENDING` until its exact producer source is located and its term counts are reproduced. No other pending row is changed.
