# Ninety-second supplemental document review — RC-001 vertex, counterterm and Q8 audits

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Review scope:** five individually registered `PENDING` validation-output documents and their exact source scripts  
**Disposition:** four `PASS_WITH_NOTES`; one `REVISION_REQUIRED`. No production calculation, Wilson coefficient, or manuscript result was changed.

## 1. Review results

| Validation document | Checks performed | Disposition |
|---|---|---|
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dim6-light-only-vertex-cancellation.txt` | Re-ran the exact source script. The heavy-propagator expansion through the displayed order and equality of the factored UV/EFT kernels reproduce the output byte-for-byte. The source explicitly does not evaluate a loop integral and requires the complete gauge-covariant EFT insertion/contact set. | `PASS_WITH_NOTES` |
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dim6-yukawa-vertex-charge-factors.txt` | Re-ran the exact source script for `eta=+1` and `eta=-1`. Hypercharge and X-charge conservation, all 12 pair tuples (36 exact B, X and mixed BX entries), and the RD mixed-BX fermion-pair zeros reproduce the output byte-for-byte. | `PASS_WITH_NOTES` |
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dim6-heavy-vertex-hard-pieces.txt` | Re-ran the exact source script. The `d*B0` expansion, six one-vertex hard factors, conjugate-vertex doubling, both flavour signs, and finite matching-scale sub-blocks reproduce the output byte-for-byte. | `PASS_WITH_NOTES` |
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dim6-mixed-parameter-counterterms.txt` | Re-ran the exact source script. The LD/RD mixed Yukawa poles, heavy-mass pole, and LD/RD coefficient parameter poles reproduce the output byte-for-byte for both `eta=+1` and `eta=-1`. | `PASS_WITH_NOTES` |
| `research/rc001-vll-higgs-singlet-uv-eft/upstream/validation/RC-001-dimension8-Q8-one-background-consistency-audit.txt` | Re-ran the exact source script. The ordinary-line Ward-contraction identity and the two d-dimensional contact angular-average projections reproduce the first two output checks. The third output line says the contact massless integral is scaleless after division by its single propagator, but the script contains no corresponding integrand construction, division, or scaleless-integral assertion; the line is printed unconditionally. | `REVISION_REQUIRED` |

## 2. Exact source and output identities

All five source files were retrieved from the reviewed `main` tree. Their reconstructed local bytes reproduce the Git blob SHA-1 values of the corresponding repository files. The SHA-256 values below identify the exact locally executed source bytes. The output files also reproduce their current Git blob SHA-1 values, and the source reruns match the archived output bytes in all five cases.

| Source script | Git blob SHA-1 | Source SHA-256 | Output Git blob SHA-1 | Output SHA-256 |
|---|---|---|---|---|
| `RC-001-dim6-light-only-vertex-cancellation.py` | `1b1a4d3d676c8f39f1c49b9eaf3ea6ef12ae3d1e` | `233217120fc422d2d5550ea469092afbba8f0ef0063c38953f5a39ccaa4eb831` | `6c5a65dc80b84a7c8df05c470c333d87588f9c03` | `c5101b864dd3322a1a7f193874900a14f16fd57bf576c689fa945af4b1902bf6` |
| `RC-001-dim6-yukawa-vertex-charge-factors.py` | `4f74a0ea416833859c668a6392ffce070e273ca1` | `8f33169e3fac7819d450ad9dff6c0828be39283cd2dc33089cc2a61c0f3b75dc` | `587e1999a4c4c905cf20ab9b215514b58db7ae1e` | `1666eced13195d05cdc43b801ac8eb9dcf95eaeeda4de71e36653071a84ea3b1` |
| `RC-001-dim6-heavy-vertex-hard-pieces.py` | `9af35a00b1777135286c7c04c02e801b23d19c6b` | `9a41759873983c8e300103a71281284222291bec67e245c1fc758ddae568e4e7` | `b03afe6273508db3b6af87116388e8a520d70a2c` | `55742069583a450cf858159bd805b3baffec3397af24732ee3dc781482493fca` |
| `RC-001-dim6-mixed-parameter-counterterms.py` | `151f54829a529224ef1330a1d2bd4c91bf3ec3d0` | `e98710730590197e7824631d381602cd85c2bad5eed5b18a3d8393e11cfb30f5` | `d1ad92faed0e1d8e3701fb9f87ce7a4b735ab4cc` | `c533e142e44a7cba5a39833d026cf027087b0e473e292a1a1e50d40d2341b268` |
| `RC-001-dimension8-Q8-one-background-consistency-audit.py` | `106c08e4777d777a9661aa40e92d61d3b587b650` | `29b3fa134a1040ff72e3c721a258617c656c52ee57cb0c6167a84502a6e73de9` | `c7785dc2946b3f3a961b815b41818ec6d71c65d3` | `3e30107d053c7a2e0a22fbe3bf9244a647b4a0e9cbbe73904ea16182ffb23689` |

## 3. Execution environment and reproducibility

- Runtime: Python `3.13.5`.
- Platform: Linux `6.18.57-x86_64-with-glibc2.41`; machine `x86_64`.
- Symbolic dependency: SymPy `1.14.0`.
- The light-only, heavy-vertex, mixed-counterterm and Q8 scripts were executed with SymPy; the Yukawa charge-factor script uses exact `fractions.Fraction` arithmetic.
- Result: **5/5 source reruns passed**, and each captured stdout file is byte-identical to its archived validation text.
- These are bounded symbolic/algebraic sub-block checks. They are not loop-amplitude integrations, a complete diagram census, a full mixed-gauge Wilson coefficient, common R* UV/IR subtraction, or complete UV–EFT matching.

## 4. Required correction for the Q8 record

The Q8 output's third `PASS` line is not backed by an executable assertion in the paired source. The current source establishes the stated Ward-contraction identity and contact angular averages, but does not establish the scaleless-integral statement by code. Keep the historical source and output unchanged; retain the document as `REVISION_REQUIRED` until either:

1. a source-level derivation/test explicitly constructs the post-division integrand and demonstrates that the integral is scaleless under the declared prescription; or
2. the output is revised so the third statement is clearly identified as a separate analytic argument with its own source, rather than a passed executable check.

The existing scope boundary remains correct: common R* UV/IR subtraction and hard matching are still open.

## 5. Register disposition

The five source validation documents are updated individually in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four to `PASS_WITH_NOTES`, and the Q8 audit to `REVISION_REQUIRED`. No other pending row is changed and no batch-wide disposition is applied.
