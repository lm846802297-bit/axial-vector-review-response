# Ninety-third supplemental document review — RC-001 mixed kinetic, EOM, Fierz and SU(2) records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation-output documents and their paired Python sources  
**Disposition:** four remain `PENDING`; the mixed-kinetic threshold output is `REVISION_REQUIRED`. This was a source/output inspection only; no script was executed and no new numerical PASS is claimed.

## 1. Individual findings

| Validation output | Static source review | Disposition |
|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.txt` | The source checks light and heavy charge traces and the logarithm identity, but it does not derive the printed finite threshold coefficient `gY*gX*Q_l/(12*pi^2)`. That coefficient is printed as a string. The result file therefore contains a quantitative one-loop threshold claim unsupported by the paired executable derivation. | `REVISION_REQUIRED` |
| `RC-001-offshell-eom-completion-audit.txt` | The source contains exact SymPy assertions for the off-shell/on-shell polynomial difference, EOM completion, coefficient shifts, two-point coefficient matching, and the invariant coefficient combination. It explicitly says the box integral was not independently reintegrated. | `PENDING` |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.txt` | The source constructs explicit four-dimensional gamma matrices and asserts the scalar-vector, opposite-chirality scalar-tensor, same-chirality scalar-tensor, and chiral-tensor self-duality identities. The reported counts are internally consistent: 16+12+6=34 identities and 34*256=8704 matrix components. | `PENDING` |
| `RC-001-dim6-SU2-attachment-projection.txt` | The source enumerates the six stated Q_LD line pairs, applies the fundamental/anti-fundamental generators, and compares each resulting tensor with the declared T0/T3 decomposition. It explicitly excludes loop integrals, multiplicities and Wilson coefficients. | `PENDING` |
| `RC-001-QLD8-second-order-fermion-EOM-audit.txt` | The source explicitly checks the (+---) Clifford algebra, the stated D-squared identity for `[D_mu,D_nu]=i F_mu_nu`, the three Higgs-source hypercharges, and the listed U(1)_X-neutral fields. | `PENDING` |

## 2. Exact source and output identities

The source and output files were fetched from the reviewed `main` tree. The Git blob SHA-1 values below identify the exact files inspected. No local byte reconstruction, SHA-256 calculation, or script execution was performed in this review.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 |
|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.py` | `4b9776f45935785361c77197acfcf8942cf5f7d3` | `8d484bd50f960f698890e2921366e634c5e794c1` |
| `RC-001-offshell-eom-completion-audit.py` | `ecd483aac1e644811fc4ef57800f58465c2ee831` | `ab74df473d3720516874f41fda848d38e4c2efe3` |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.py` | `0302a4a4548174a26fad7a5aaf3c336dc18318a0` | `66567df4f4cd3517ba6fffcfd887c18e731777cf` |
| `RC-001-dim6-SU2-attachment-projection.py` | `60b2af5cf72354f15dcd871097f32d9cbfcb660c` | `81ce3bf54246dcbe924b10bbd9439930c21c6ac3` |
| `RC-001-QLD8-second-order-fermion-EOM-audit.py` | `9898396afe216cbc9858e2b2a72d77c26edd062d` | `3a602946b16e0b268d6105086b3f1e1024748ce8` |

## 3. Required correction: mixed kinetic threshold

The current source establishes:
- the light Weyl `Tr(YX)) cancellation separately for muon and tau flavours;
- cancellation of the summed heavy Dirac trace for `eta_mu=+1`, `eta_tau=-1`;
- the algebraic identity `log(Mmu^2)-log(Mtau^2)=log(Mmu^2/Mtau^2)`;
- vanishing of that logarithm for equal heavy masses.

It does **not** calculate the one-loop vacuum-polarization coefficient, specify the complete normalization of the mixed kinetic term, or derive the sign and factor multiplying the logarithm. The finite threshold coefficient is a printed string, not an asserted result.

Keep the archived source/output unchanged until the threshold claim is supported by an explicit derivation or an independently sourced convention-matched formula. The derivation must state the gauge-field kinetic-term convention, Weyl/Dirac multiplicity, charges, renormalization prescription and matching-scale sign. Do not infer the coefficient from the trace-cancellation test alone.

## 4. Reproducibility boundary

No scripts were executed in this review. The four remaining PENDING records require an exact checked-out commit, source SHA-256, Python/SymPy versions, OS/architecture, command, exit status and captured output hash before they can be promoted based on a fresh run.

The inspected scripts describe bounded algebraic checks only. They do not establish a complete loop amplitude, diagram multiplicity census, d-dimensional Fierz mixing, common R* subtraction, full Wilson coefficient, or complete UV-EFT matching.

## 5. Register disposition

The five output paths are individually updated in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four remain `PENDING` pending execution/provenance, and the mixed-kinetic threshold output is `REVISION_REQUIRED` pending derivation of its printed one-loop coefficient. No other pending row is changed.
