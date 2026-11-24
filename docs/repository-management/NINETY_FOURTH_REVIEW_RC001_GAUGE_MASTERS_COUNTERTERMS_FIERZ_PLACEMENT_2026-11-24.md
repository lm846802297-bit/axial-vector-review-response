# Ninety-fourth supplemental document review — RC-001 gauge masters, counterterms and Fierz records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation outputs and their paired Python sources  
**Disposition:** four `PASS_WITH_NOTES`; one `REVISION_REQUIRED`. This was a static source/output review; no fresh Python/SymPy execution or stdout comparison was performed.

## 1. Individual findings

| Validation output | Static source review | Disposition |
|---|---|---|
| `RC-001-dim6-gauge-master-integrals.txt` | The source encodes the Feynman-parameter integrals, retained O(epsilon) times UV-pole terms, self-energy coefficients, propagator insertion, partial fractions and scalar-master UV/IR algebra. The output is scoped to these master sub-blocks and excludes complete diagrams and Wilson coefficients. | `PASS_WITH_NOTES` |
| `RC-001-QLD8-P1.5c-merged-cross-source-audit.txt` | The source encodes SS/TS/ST coefficients, momentum/wedge reductions and the D-dimensional TT tensor expansion. Its direct-singlet color statement is only a multiplication of hard-coded sign arrays; the script does not construct SU(3) generators or derive the color projection. | `REVISION_REQUIRED` |
| `RC-001-dim6-gauge-parameter-counterterms.txt` | The source performs exact Fraction arithmetic for the declared LD/RD Yukawa, heavy-mass and coefficient parameter-pole formulas. It does not calculate the loop integrals or the EFT operator counterterm matrix. | `PASS_WITH_NOTES` |
| `RC-001-QLD8-derivative-Fierz-placement-audit.txt` | The source checks nine ordered source pairs, three diagonal and three cross+HC structures, 36 ordered product-rule placements, chirality counts and four derivative assignments. This is bookkeeping, not Dirac algebra or loop renormalization. | `PASS_WITH_NOTES` |
| `RC-001-QLD-chiral-Fierz-identities.txt` | The source constructs four-dimensional gamma matrices and encodes RR/LL scalar-tensor and RL/LR vector identities, including the operator-level minus-sign convention. Its scope excludes d-dimensional evanescent mixing. | `PASS_WITH_NOTES` |

## 2. Exact file identities

The source and validation-output files were fetched from the reviewed `main` tree. Git blob SHA-1 identifies each exact file. SHA-256 values identify the source file and archived validation file; they are not captured-stdout hashes.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 | Source SHA-256 | Archived output SHA-256 |
|---|---|---|---|---|
| `RC-001-dim6-gauge-master-integrals.py` | `55df8b29e4fe196af71b34f2ad3df154ac06b9f0` | `4931888facab744b02a3b025b1c9c0090b5ae2e2` | `1096830e669fef598fe17eadd33049dcd424cb2017a528ad3a90b8224a1409ca` | `0cb74fac2071b5df75dcfdd449a7705b0f04649e45d08536ffa23a249bf862a4` |
| `RC-001-QLD8-P1.5c-merged-cross-source-audit.py` | `37d1429702ce07a69a6920f49b678c15f7b5d61f` | `76237a0db6c886e248e5dfd0771aaa559254073b` | `2af6b73764606f33312b907aed95ef1089f1e95cd5a300095382e9a6caebd466` | `3fc3ffc6d0fd8b668090d989e787a71fb71e1ba2e8c6cef2451390c119935459` |
| `RC-001-dim6-gauge-parameter-counterterms.py` | `219c35748fde05671c349e2237facfd0ab539a59` | `8ee2b5a9e02a60960138539a2c0569c3845706bd` | `c8b20ff126e106001b57786c8045d6dc40486917b6a50e33e1d2b074ff86e985` | `a15f166096d631926f473f21db4eb9d616acaa18ac2800eb515d4144bcbb1a9b` |
| `RC-001-QLD8-derivative-Fierz-placement-audit.py` | `c15ca1fef7edc37c7ce50e7234d062eca6d9bb49` | `cf162dba2cf5da7e307ffd38f889bd6939d1c295` | `ff139429239525a5f7699c47b19613d4117bac83c806e5ade5f5aacdcb79c91e` | `d98aea0ad51c5e1e853102fd427432135ab2ba79611dac929f098db54dac78b2` |
| `RC-001-QLD-chiral-Fierz-identities.py` | `141bd71ea022043636b7a5aaf3c336dc18318a0` | `3fac09dae66d742103f318b998fa17d9537332d5` | `3e5f65cb9977a927b4f21ec8d97cbe2325ab208971d2dd66aea9f4f5722abad3` | `d996a7cc5abbeae18c40012caf71c86853c6aa517eb2ece07f4df608fb8f38ba` |

## 3. Review boundary

No script was executed in this document-review pass. The source assertions, archived outputs and their stated limitations were inspected. A future fresh run should record the exact runtime, command, exit status and captured stdout hash.

The P1.5c merged cross-source color-projection claim remains `REVISION_REQUIRED) until its output is narrowed to the hard-coded sign-array arithmetic or the source derives the SU(3) contraction. The other four records pass only within their declared algebraic sub-block scopes.

## 4. Register disposition

The five output paths are individually recorded: four `PASS_WITH_NOTES`, one `REVISION_REQUIRED`. No fresh execution or byte-identical stdout is claimed. No other pending row is changed.
