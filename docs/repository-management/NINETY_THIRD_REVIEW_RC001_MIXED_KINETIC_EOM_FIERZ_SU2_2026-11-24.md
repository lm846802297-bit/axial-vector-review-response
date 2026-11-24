# Ninety-third supplemental document review — RC-001 mixed kinetic, EOM, Fierz and SU(2) records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation outputs and their paired Python sources  
**Disposition:** five `PASS_WITH_NOTES`. This was a static source/output review; **no fresh Python/SymPy execution or stdout comparison was performed**. The source and archived-output fingerprints below identify the exact files inspected.

## 1. Individual findings

| Validation output | Static source/output review | Disposition |
|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.txt` | The script checks the light/heavy charge traces and the logarithm identity. The finite coefficient is printed as a literal, but it is independently derived in the companion analytic note `research/RC-001-dim6-mixed-kinetic-threshold.md` from the one-Dirac-fermion vacuum-polarization integral and the stated ((Y,x)) assignments. The script is a trace/log regression record, not the loop derivation. | `PASS_WITH_NOTES` |
| `RC-001-offshell-eom-completion-audit.txt` | The source contains exact SymPy assertions for the off-shell/on-shell polynomial difference, EOM completion, coefficient shifts, two-point coefficient matching and the invariant coefficient combination. It explicitly excludes reintegration of the underlying box graph. | `PASS_WITH_NOTES` |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.txt` | The source constructs explicit four-dimensional gamma matrices and encodes the scalar-vector, opposite-chirality scalar-tensor, same-chirality scalar-tensor and chiral-tensor self-duality checks. The reported counts are internally consistent: 16+12+6=34 identities and 34*256=8704 matrix components. No d-dimensional loop mixing or finite matching is claimed. | `PASS_WITH_NOTES` |
| `RC-001-dim6-SU2-attachment-projection.txt` | The source enumerates six Q_LD line pairs, applies fundamental/anti-fundamental generators and compares the resulting tensors with the declared T0/T3 decomposition. It excludes loop integrals, multiplicities and Wilson coefficients. | `PASS_WITH_NOTES` |
| `RC-001-QLD8-second-order-fermion-EOM-audit.txt` | The source encodes the (+---) Clifford algebra, the stated D-squared identity for ([D_\mu,D_\nu]=iF_{\mu\nu}), the three Higgs-source hypercharges and the listed U(1)_X-neutral fields. No Wilson coefficient or d-dimensional matching is claimed. | `PASS_WITH_NOTES` |

## 2. Exact file identities

The source and validation-output files were fetched from the reviewed `main` tree. Git blob SHA-1 identifies each exact file. The SHA-256 columns are hashes of the source file and archived validation file, respectively; **they are not captured-stdout hashes**.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 | Source SHA-256 | Archived output SHA-256 |
|---|---|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.py` | `4b9776f45935785361c77197acfcf8942cf5f7d3` | `8d484bd50f960f698890e2921366e634c5e794c1` | `f92e3292f93be567c95cbd197123283b3bc8cf6056b59701e9fe051f94ae911e` | `e4f61c9099c2717e1d19a8cf933b8cdcf954be07c3908a7616c06a0bbab136b0` |
| `RC-001-offshell-eom-completion-audit.py` | `ecd483aac1e644811fc4ef57800f58465c2ee831` | `ab74df473d3720516874f41fda848d38e4c2efe3` | `92c7c4778fd995508cbac299dfd4d4a8148071e6625f3c528ed0093526d7388a` | `6a60ebdb6848c99a71438d0e7574146901108ce83b47a23fe338a18950eae08e` |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.py` | `0302a4a4548174a26fad7a5aaf3c336dc18318a0` | `66567df4f4cd3517ba6fffcfd887c18e731777cf` | `2804e49616e3ca204bd4c26507878160490fa16967fc454e91ba3474d8fc8456` | `c48a707389064fe8fbd34d4ebd8e54fe534fbfb335b844a5335caa29ceda1ceb` |
| `RC-001-dim6-SU2-attachment-projection.py` | `60b2af5cf72354f15dcd871097f32d9cbfcb660c` | `81ce3bf54246dcbe924b10bbd9439930c21c6ac3` | `8f2a0f1bb2cf99e5a4ba39439025b498d74042f6158fe468c08c0aee4ad035f1` | `5fd683077891dedd95bc58a3a83a45270c8960d3b0e1c4058924ef7ae10c6b25` |
| `RC-001-QLD8-second-order-fermion-EOM-audit.py` | `9898396afe216cbc9858e2b2a72d77c26edd062d` | `3a602946b16e0b268d6105086b3f1e1024748ce8` | `2ef652a607369e40e5583e3e3a39a1c81e2067f5cd84e3769b7dc62d8017950e` | `255ccc10d6aa29eb62c82fa74edebddbfdc26ef8a984791870ed33c47aa63798` |

## 3. Reproducibility boundary

No script was executed in this document-review pass. The source-level assertions and archived validation records were inspected, and the mixed-kinetic threshold coefficient was cross-checked against its companion analytic derivation. A future fresh run should record Python/SymPy versions, OS/architecture, command, exit status and captured stdout hash.

These are bounded algebraic checks. They are not loop-amplitude integrations, a complete diagram census, a full mixed-gauge Wilson coefficient, common R* UV/IR subtraction or complete UV-EFT matching.

## 4. Register disposition

The five output paths remain individually registered as `PASS_WITH_NOTES`, with the scope boundaries above. No claim of fresh execution or byte-identical stdout is made. No other pending row is changed.
