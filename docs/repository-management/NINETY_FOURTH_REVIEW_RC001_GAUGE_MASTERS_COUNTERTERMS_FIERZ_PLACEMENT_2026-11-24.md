# Ninety-fourth supplemental document review — RC-001 gauge masters, counterterms and Fierz records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation outputs and their paired Python sources  
**Disposition:** four `PASS_WITH_NOTES`; one `REVISION_REQUIRED`. All five exact source files were executed locally and all five stdout captures match their archived outputs byte-for-byte.

## 1. Individual findings

| Validation output | Execution and source review | Disposition |
|---|---|---|
| `RC-001-dim6-gauge-master-integrals.txt` | Exact SymPy source executed. Feynman-parameter integrals, retained O(epsilon) times UV-pole terms, self-energy coefficients, propagator insertion, partial fractions and the stated scalar-master UV/IR algebra all passed. Stdout matches the archived output byte-for-byte. | `PASS_WITH_NOTES` |
| `RC-001-QLD8-P1.5c-merged-cross-source-audit.txt` | Exact SymPy source executed. SS/TS/ST coefficient expansions, scalar momentum polynomial, mixed-wedge reduction/rank, symmetric D-dimensional tensor and O(epsilon) expansion passed. The final output also claims a zero direct-singlet color projection, but the source only multiplies four hard-coded sign arrays and checks their sum; it does not construct or contract SU(3) generators or derive those arrays from the color tensors. | `REVISION_REQUIRED` |
| `RC-001-dim6-gauge-parameter-counterterms.txt` | Exact Fraction source executed. All LD/RD Yukawa, heavy-mass and coefficient parameter-pole arithmetic matched the declared rational values. Stdout matches the archived output byte-for-byte. The source explicitly checks the arithmetic of supplied MS pole formulas, not loop integrals or the EFT operator counterterm matrix. | `PASS_WITH_NOTES` |
| `RC-001-QLD8-derivative-Fierz-placement-audit.txt` | Exact source executed. The nine ordered source pairs, three diagonal/three cross+HC structures, 36 ordered product-rule placements, chirality counts and all four derivative assignments passed. Stdout matches the archived output byte-for-byte. This is bookkeeping, not Dirac algebra or loop renormalization. | `PASS_WITH_NOTES` |
| `RC-001-QLD-chiral-Fierz-identities.txt` | Exact SymPy source executed. RR/LL scalar-tensor and RL/LR vector identities each passed 256/256 components, for 1024/1024 total. The output correctly distinguishes c-number matrix identities from the extra minus sign in anticommuting-field operator Fierz rearrangement. Stdout matches the archived output byte-for-byte. | `PASS_WITH_NOTES` |

## 2. Exact source and output identities

All source files were reconstructed from the fetched repository contents. The locally computed Git blob SHA-1 matches the corresponding repository blob for all five scripts.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 | Source SHA-256 | Captured stdout SHA-256 |
|---|---|---|---|---|
| `RC-001-dim6-gauge-master-integrals.py` | `55df8b29e4fe196af71b34f2ad3df154ac06b9f0` | `4931888facab744b02a3b025b1c9c0090b5ae2e2` | `1096830e669fef598fe17eadd33049dcd424cb2017a528ad3a90b8224a1409ca` | `0cb74fac2071b5df75dcfdd449a7705b0f04649e45d08536ffa23a249bf862a4` |
| `RC-001-QLD8-P1.5c-merged-cross-source-audit.py` | `37d1429702ce07a69a6920f49b678c15f7b5d61f` | `76237a0db6c886e248e5dfd0771aaa559254073b` | `2af6b73764606f33312b907aed95ef1089f1e95cd5a300095382e9a6caebd466` | `3fc3ffc6d0fd8b668090d989e787a71fb71e1ba2e8c6cef2451390c119935459` |
| `RC-001-dim6-gauge-parameter-counterterms.py` | `219c35748fde05671c349e2237facfd0ab539a59` | `8ee2b5a9e02a60960138539a2c0569c3845706bd` | `c8b20ff126e106001b57786c8045d6dc40486917b6a50e33e1d2b074ff86e985` | `a15f166096d631926f473f21db4eb9d616acaa18ac2800eb515d4144bcbb1a9b` |
| `RC-001-QLD8-derivative-Fierz-placement-audit.py` | `c15ca1fef7edc37c7ce50e7234d062eca6d9bb49` | `cf162dba2cf5da7e307ffd38f889bd6939d1c295` | `ff139429239525a5f7699c47b19613d4117bac83c806e5ade5f5aacdcb79c91e` | `d98aea0ad51c5e1e853102fd427432135ab2ba79611dac929f098db54dac78b2` |
| `RC-001-QLD-chiral-Fierz-identities.py` | `141bd71ea022043636b7a5e488885fd4846e2bb4` | `3fac09dae66d742103f318b998fa17d9537332d5` | `3e5f65cb9977a927b4f21ec8d97cbe2325ab208971d2dd66aea9f4f5722abad3` | `d996a7cc5abbeae18c40012caf71c86853c6aa517eb2ece07f4df608fb8f38ba` |

## 3. Execution environment and reproducibility

- Python `3.13.5`; SymPy `1.14.0`.
- Linux `6.18.57-x86_64-with-glibc2.41`; architecture `x86_64`.
- All five scripts passed `py_compile` and executed with exit status zero.
- All five captured stdout files matched their archived validation text byte-for-byte.
- All five reconstructed source Git blob SHA-1 values matched the source repository blob IDs.

These checks validate only the declared algebraic sub-blocks. They do not establish complete loop amplitudes, diagram multiplicities, a complete UV-EFT matching result, or Wilson coefficients.

## 4. Required correction: P1.5c color projection

The P1.5c source currently defines `color=[-1,1,1,-1]`, multiplies it elementwise by three other hard-coded sign arrays, and checks that the first array sums to zero. This verifies arithmetic consistency of the supplied arrays, not the underlying SU(3) color contraction.

Keep the archived source and output unchanged. Retain the validation output as `REVISION_REQUIRED` until either:
1. the source constructs the relevant color tensors/generators and explicitly derives the four sign arrays and singlet projection; or
2. the output wording is narrowed to say that the hard-coded sign-array arithmetic was checked, without claiming a derived direct-singlet color projection.

The other P1.5c algebraic checks remain reproducible and need not be discarded.

## 5. Register disposition

The five output paths are updated individually in `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv`: four to `PASS_WITH_NOTES` based on exact source execution and byte-identical stdout; the P1.5c output remains `REVISION_REQUIRED` for the unsupported color-projection claim. No other pending row is changed.
