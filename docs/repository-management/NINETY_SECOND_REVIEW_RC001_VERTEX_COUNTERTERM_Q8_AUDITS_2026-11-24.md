# Ninety-second supplemental document review — RC-001 vertex, counterterm and Q8 audits

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Review scope:** five individually registered `PENDING` validation-output documents and their exact source scripts  
**Disposition:** four `PENDING` (static source/output inspection only; execution evidence not yet independently reproduced); one `REVISION_REQUIRED`. No production calculation, Wilson coefficient, or manuscript result was changed.

## 1. Review results

| Validation document | Checks performed | Disposition |
|---|---|---|
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dim6-light-only-vertex-cancellation.txt` | Inspected the exact paired source and archived output. The displayed heavy-propagator expansion and equality of the factored UV/EFT kernels are represented in the source; this review did not execute the script or independently reproduce stdout. The source explicitly does not evaluate a loop integral and requires the complete gauge-covariant EFT insertion/contact set. | `PASS_WITH_NOTES` |
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dim6-yukawa-vertex-charge-factors.txt` | Inspected the exact paired source and archived output. The source contains explicit exact-rational checks for `eta=+1` and `eta=-1`, charge conservation and the 12 pair tuples; this review did not execute the script or independently reproduce stdout. | `PASS_WITH_NOTES` |
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dim6-heavy-vertex-hard-pieces.txt` | Inspected the exact paired source and archived output. The source encodes the `d*B0` expansion, six one-vertex hard factors, conjugate-vertex doubling, both flavour signs and finite matching-scale sub-blocks; this review did not execute the script or independently reproduce stdout. | `PASS_WITH_NOTES` |
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dim6-mixed-parameter-counterterms.txt` | Inspected the exact paired source and archived output. The source encodes the LD/RD mixed Yukawa poles, heavy-mass pole and coefficient parameter poles for both flavour signs; this review did not execute the script or independently reproduce stdout. | `PASS_WITH_NOTES` |
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dimension8-Q8-one-background-consistency-audit.txt` | Inspected the exact paired source and archived output. The ordinary-line Ward-contraction identity and the two d-dimensional contact angular-average projections are explicitly asserted. The third output line says the contact massless integral is scaleless after division by its single propagator, but the script contains no corresponding integrand construction, division, or scaleless-integral assertion; the line is printed unconditionally. | `REVISION_REQUIRED` |

## 2. Exact source identities

All five source scripts and their paired validation-output files were fetched from the reviewed `main` tree. Their Git blob SHA-1 values are recorded below. This review did not download the repository files into a local execution environment, calculate source SHA-256 values, or execute the scripts; it therefore makes no claim of byte-identical stdout reproduction.

| Source script | Git blob SHA-1 | Output Git blob SHA-1 |
|---|---|---|
| `RC-001-dim6-light-only-vertex-cancellation.py` | `1b1a4d3d676c8f39f1c49b9eaf3ea6ef12ae3d1e` | `6c5a65dc80b84a7c8df05c470c333d87588f9c03` |
| `RC-001-dim6-yukawa-vertex-charge-factors.py` | `4f74a0ea416833859c668a6392ffce070e273ca1` | `587e1999a4c4c905cf20ab9b215514b58db7ae1e` |
| `RC-001-dim6-heavy-vertex-hard-pieces.py` | `9af35a00b1777135286c7c04c02e801b23d19c6b` | `b03afe6273508db3b6af87116388e8a520d70a2c` |
| `RC-001-dim6-mixed-parameter-counterterms.py` | `151f54829a529224ef1330a1d2bd4c91bf3ec3d0` | `d1ad92faed0e1d8e3701fb9f87ce7a4b735ab4cc` |
| `RC-001-dimension8-Q8-one-background-consistency-audit.py` | `106c08e4777d777a9661aa40e92d61d3b587b650` | `c7785dc2946b3f3a961b815b41818ec6d71c65d3` |

## 3. Execution environment and reproducibility

No script execution was performed in this review. The repository records the source language and dependencies, but this report does not assert a fresh Python/SymPy runtime, hardware environment, test count, or stdout reproduction. A follow-up execution should record the exact checked-out commit, source SHA-256, Python/SymPy versions, OS/architecture, command, exit status and captured output hash.

These files concern bounded symbolic/algebraic sub-blocks. They are not loop-amplitude integrations, a complete diagram census, a full mixed-gauge Wilson coefficient, common R* UV/IR subtraction, or complete UV–EFT matching.

## 4. Required correction for the Q8 record

The Q8 output's third `PASS` line is not backed by an executable assertion in the paired source. The current source establishes the stated Ward-contraction identity and contact angular averages, but does not establish the scaleless-integral statement by code. Keep the historical source and output unchanged; retain the document as `REVISION_REQUIRED` until either:

1. a source-level derivation/test explicitly constructs the post-division integrand and demonstrates that the integral is scaleless under the declared prescription; or
2. the output is revised so the third statement is clearly identified as a separate analytic argument with its own source, rather than a passed executable check.

The existing scope boundary remains correct: common R* UV/IR subtraction and hard matching are still open.

## 5. Register disposition

The five source validation documents are updated individually in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four remain `PENDING` pending actual execution and provenance capture, and the Q8 audit is `REVISION_REQUIRED` because its third PASS statement is unsupported by the paired executable source. No other pending row is changed and no batch-wide disposition is applied.
