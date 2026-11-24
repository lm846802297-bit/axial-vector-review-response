# Ninety-third supplemental document review — RC-001 mixed kinetic, EOM, Fierz and SU(2) records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation-output documents and their paired Python sources  
**Disposition:** five `PASS_WITH_NOTES`. All five exact source files were executed locally and each stdout was compared byte-for-byte with its archived output. The mixed-kinetic coefficient is supported by the companion analytic threshold derivation in `research/rc001-vll-higgs-singlet-uv-eft/upstream/research/RC-001-dim6-mixed-kinetic-threshold.md`; the script itself only checks charge traces and logarithm algebra.

## 1. Individual findings

| Validation output | Static source review | Disposition |
|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.txt` | Exact source executed and stdout matched byte-for-byte. The script checks the light/heavy charge traces and logarithm identity. The finite threshold coefficient is analytically derived in the companion note `research/rc001-vll-higgs-singlet-uv-eft/upstream/research/RC-001-dim6-mixed-kinetic-threshold.md` from the one-Dirac-fermion vacuum-polarization integral and the mu/tau charge assignments. | `PASS_WITH_NOTES` |
| `RC-001-offshell-eom-completion-audit.txt` | Exact source executed; all five coefficient/EOM identities passed and stdout matched the archived output byte-for-byte. The source explicitly says the box integral was not independently reintegrated. | `PASS_WITH_NOTES` |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.txt` | Exact source executed; 16/16 scalar-vector, 12/12 opposite-chirality scalar-tensor, 6/6 same-chirality scalar-tensor, 8704/8704 components and 6/6 self-duality checks passed. Stdout matched the archived output byte-for-byte. | `PASS_WITH_NOTES` |
| `RC-001-dim6-SU2-attachment-projection.txt` | Exact source executed; all six LD-W-01 through LD-W-06 tensor projections passed and stdout matched the archived output byte-for-byte. It explicitly excludes loop integrals, multiplicities and Wilson coefficients. | `PASS_WITH_NOTES` |
| `RC-001-QLD8-second-order-fermion-EOM-audit.txt` | Exact source executed; the Clifford algebra, D-squared identity, three source hypercharges and five U(1)_X charge checks passed. Stdout matched the archived output byte-for-byte. | `PASS_WITH_NOTES` |

## 2. Exact source and output identities

The source and output files were fetched from the reviewed `main` tree. The Git blob SHA-1 values below identify the exact files inspected. All five source files were reconstructed locally from the fetched contents. Each locally computed Git blob SHA-1 matches the recorded repository blob SHA-1.

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

The five output paths are individually updated in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four are `PASS_WITH_NOTES` based on exact source execution and byte-identical stdout; the mixed-kinetic threshold output remains `REVISION_REQUIRED` because its finite one-loop coefficient is not derived by the paired script. No other pending row is changed.## 3. Execution environment and reproducibility

- Python: `3.13.5`.
- SymPy: `1.14.0`.
- OS/kernel: Linux `6.18.57-x86_64-with-glibc2.41`; architecture `x86_64`.
- All five scripts compiled and executed successfully.
- All five captured stdout files were compared with the corresponding archived validation text using byte-for-byte comparison: **5/5 exact matches**.
- For every source, the locally reconstructed Git blob SHA-1 matches the repository blob SHA-1. The SHA-256 values below identify the exact executed source and captured stdout bytes.

| Script | Source SHA-256 | Stdout SHA-256 |
|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.py` | `f92e3292f93be567c95cbd197123283b3bc8cf6056b59701e9fe051f94ae911e` | `e4f61c9099c2717e1d19a8cf933b8cdcf954be07c3908a7616c06a0bbab136b0` |
| `RC-001-offshell-eom-completion-audit.py` | `92c7c4778fd995508cbac299dfd4d4a8148071e6625f3c528ed0093526d7388a` | `6a60ebdb6848c99a71438d0e7574146901108ce83b47a23fe338a18950eae08e` |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.py` | `2804e49616e3ca204bd4c26507878160490fa16967fc454e91ba3474d8fc8456` | `c48a707389064fe8fbd34d4ebd8e54fe534fbfb335b844a5335caa29ceda1ceb` |
| `RC-001-dim6-SU2-attachment-projection.py` | `8f2a0f1bb2cf99e5a4ba39439025b498d74042f6158fe468c08c0aee4ad035f1` | `5fd683077891dedd95bc58a3a83a45270c8960d3b0e1c4058924ef7ae10c6b25` |
| `RC-001-QLD8-second-order-fermion-EOM-audit.py` | `2ef652a607369e40e5583e3e3a39a1c81e2067f5cd84e3769b7dc62d8017950e` | `255ccc10d6aa29eb62c82fa74edebddbfdc26ef8a984791870ed33c47aa63798` |

These are bounded algebraic checks only. They do not establish a complete loop amplitude, diagram multiplicity census, d-dimensional Fierz mixing, common R* subtraction, full Wilson coefficient, or complete UV-EFT matching.

## 4. Analytic support for the mixed kinetic threshold

The paired script does not itself derive the coefficient; it checks the charge traces and the logarithm identity. The companion analytic note does derive it. In the stated transverse-kernel convention, one Dirac fermion contributes
`(gY*gX*Q_l/(12*pi^2))*Y*x*(Delta_epsilon-ln(M^2/mu_R^2))`
at zero momentum. With `Y_E=-1`, `x_E=eta_l`, `eta_mu=+1` and `eta_tau=-1`, summing the two heavy flavours cancels the UV pole and gives
[
\Pi_{YX}^{E}(0)=\frac{g_Yg_XQ_\ell}{12\pi^2}
\ln\frac{M_{E_\mu}^2}{M_{E_\tau}^2}.
]
The same note states the kinetic-term convention and the matching relation for the renormalized `chi) parameter. The coefficient and sign are therefore supported by the analytic source; the script is only its charge/log regression check.

The validation output is retained as `PASS_WITH_NOTES`, with the explicit boundary that the script alone is not the loop derivation and that the renormalized `chi(mu_R)` boundary condition remains an independent input.

## 5. Register disposition

The five output paths are individually updated in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four are `PASS_WITH_NOTES` based on exact source execution and byte-identical stdout; the mixed-kinetic threshold output remains `REVISION_REQUIRED` because its finite one-loop coefficient is not derived by the paired script. No other pending row is changed.## 3. Execution environment and reproducibility

- Python: `3.13.5`.
- SymPy: `1.14.0`.
- OS/kernel: Linux `6.18.57-x86_64-with-glibc2.41`; architecture `x86_64`.
- All five scripts compiled and executed successfully.
- All five captured stdout files were compared with the corresponding archived validation text using byte-for-byte comparison: **5/5 exact matches**.
- For every source, the locally reconstructed Git blob SHA-1 matches the repository blob SHA-1. The SHA-256 values below identify the exact executed source and captured stdout bytes.

| Script | Source SHA-256 | Stdout SHA-256 |
|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.py` | `f92e3292f93be567c95cbd197123283b3bc8cf6056b59701e9fe051f94ae911e` | `e4f61c9099c2717e1d19a8cf933b8cdcf954be07c3908a7616c06a0bbab136b0` |
| `RC-001-offshell-eom-completion-audit.py` | `92c7c4778fd995508cbac299dfd4d4a8148071e6625f3c528ed0093526d7388a` | `6a60ebdb6848c99a71438d0e7574146901108ce83b47a23fe338a18950eae08e` |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.py` | `2804e49616e3ca204bd4c26507878160490fa16967fc454e91ba3474d8fc8456` | `c48a707389064fe8fbd34d4ebd8e54fe534fbfb335b844a5335caa29ceda1ceb` |
| `RC-001-dim6-SU2-attachment-projection.py` | `8f2a0f1bb2cf99e5a4ba39439025b498d74042f6158fe468c08c0aee4ad035f1` | `5fd683077891dedd95bc58a3a83a45270c8960d3b0e1c4058924ef7ae10c6b25` |
| `RC-001-QLD8-second-order-fermion-EOM-audit.py` | `2ef652a607369e40e5583e3e3a39a1c81e2067f5cd84e3769b7dc62d8017950e` | `255ccc10d6aa29eb62c82fa74edebddbfdc26ef8a984791870ed33c47aa63798` |

These are bounded algebraic checks only. They do not establish a complete loop amplitude, diagram multiplicity census, d-dimensional Fierz mixing, common R* subtraction, full Wilson coefficient, or complete UV-EFT matching.

## 4. Required correction: mixed kinetic threshold

The mixed-kinetic script executes successfully and reproduces its archived output exactly. However, it only asserts the light/heavy charge traces and the logarithm identity. The finite threshold coefficient `gY*gX*Q_l/(12*pi^2)` is emitted as a literal print string; it is not derived or asserted by the script.

Therefore the execution PASS is not a validation of that coefficient. Keep the output `REVISION_REQUIRED` until a convention-matched one-loop vacuum-polarization or beta-function derivation establishes the coefficient and sign. State the gauge-field kinetic-term convention, Weyl/Dirac multiplicity, charges and matching prescription. The existing trace-cancellation result can remain as a separate checked sub-result.

## 5. Register disposition

The five output paths are individually updated in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four remain `PENDING` pending execution/provenance, and the mixed-kinetic threshold output is `REVISION_REQUIRED` pending derivation of its printed one-loop coefficient. No other pending row is changed.
