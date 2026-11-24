# Ninety-third supplemental document review — RC-001 mixed-kinetic, EOM, Fierz and SU(2) audits

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Review scope:** five individually registered pending validation-output documents and their exact paired source scripts  
**Disposition:** four remain `PENDING`; one is `REVISION_REQUIRED`. This was a source/output inspection, not a fresh execution.

## 1. Individual findings

| Validation output | Source-level finding | Disposition |
|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.txt` | The source verifies the light Weyl charge traces for each flavour, cancellation of the summed heavy Dirac trace, the logarithm identity and the equal-mass zero. It does **not** derive or assert the displayed finite threshold coefficient (g_Y g_X Q_\ell/(12\pi^2)\ln(M_{E,\mu}^2/M_{E,\tau}^2)); that line is printed unconditionally. | `REVISION_REQUIRED` |
| `RC-001-offshell-eom-completion-audit.txt` | The paired script contains exact SymPy assertions for the off-shell/on-shell polynomial difference, EOM completion, equal coefficient shifts, matching to the two-point hard coefficients and invariance of the nonredundant combination. The output correctly states that the box integral is not independently reintegrated. | `PENDING` pending fresh execution and runtime provenance |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.txt` | The source explicitly constructs a four-dimensional Dirac representation, checks the scalar-vector, opposite-/same-chirality scalar-tensor identities component by component, and checks chiral-tensor self-duality. The declared counts are internally consistent: 16+12+6=34 identities and 34×256=8,704 components. | `PENDING` pending fresh execution and runtime provenance |
| `RC-001-dim6-SU2-attachment-projection.txt` | The source constructs the four doublet/antidoublet generator actions and checks all six LD-W pair contractions against the stated (T_0,T_3) basis. Its output explicitly limits the claim to group-theory tensors. | `PENDING` pending fresh execution and runtime provenance |
| `RC-001-QLD8-second-order-fermion-EOM-audit.txt` | The source explicitly checks the (+---) Clifford algebra, the stated ([D_\mu,D_\nu]=iF_{\mu\nu}) convention identity, the three Higgs-source hypercharges and the listed (U(1)_X)-neutral fields. The output scope correctly excludes Wilson coefficients and loop matching. | `PENDING` pending fresh execution and runtime provenance |

## 2. Exact source/output identities

The five source scripts and five paired validation outputs were fetched from the reviewed Git tree. The Git blob SHA-1 identities are:

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 |
|---|---|---|
| `RC-001-dim6-mixed-kinetic-threshold.py` | `4b9776f45935785361c77197acfcf8942cf5f7d3` | `8d484bd50f960f698890e2921366e634c5e794c1` |
| `RC-001-offshell-eom-completion-audit.py` | `ecd483aac1e644811fc4ef57800f58465c2ee831` | `ab74df473d3720516874f41fda848d38e4c2efe3` |
| `RC-001-QLD-EOM-generated-chiral-Fierz-audit.py` | `0302a4a4548174a26fad7a5aaf3c336dc18318a0` | `66567df4f4cd3517ba6fffcfd887c18e731777cf` |
| `RC-001-dim6-SU2-attachment-projection.py` | `60b2af5cf72354f15dcd871097f32d9cbfcb660c` | `81ce3bf54246dcbe924b10bbd9439930c21c6ac3` |
| `RC-001-QLD8-second-order-fermion-EOM-audit.py` | `9898396afe216cbc9858e2b2a72d77c26edd062d` | `3a602946b16e0b268d6105086b3f1e1024748ce8` |

No source SHA-256, execution environment, exit status or fresh stdout hash is claimed in this static review. The four pending scripts must be run from an exact checkout before their archived PASS outputs are accepted as independently reproduced.

## 3. Required correction

For the mixed-kinetic threshold record, preserve the current historical source/output. Before changing its disposition, either:

1. add an independent derivation and executable check of the finite threshold coefficient, including its normalization and sign in the declared charge convention; or
2. revise the output so that only the trace/log identities are presented as checked, and identify the finite-threshold coefficient as an analytic result supported by a separate derivation.

The cancellation of the additive UV pole proportional to (mathrm{Tr}(YX)) does not by itself establish the finite mass-splitting threshold coefficient.

## 4. Register disposition

The five validation-output rows are updated individually in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four remain `PENDING` and the mixed-kinetic threshold output is `REVISION_REQUIRED`. No unrelated pending records are changed. The four pending items are not marked passed merely because their source code contains assertions; fresh execution and provenance are still required.
