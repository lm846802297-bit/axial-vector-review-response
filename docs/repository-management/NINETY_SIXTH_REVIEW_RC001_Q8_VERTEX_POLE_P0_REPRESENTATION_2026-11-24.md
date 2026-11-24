# Ninety-sixth supplemental document review — RC-001 Q8 vertex, line-pole, P0 and representation records

**Review date:** 2026-11-24  
**Review base:** `6986463487ddade80ad72e67087b376e34969835` (main after PR #123 merge)  
**Scope:** five individually registered validation outputs and their paired Python sources  
**Disposition:** four `PASS_WITH_NOTES`; one `PENDING`. This was a static source/output review. No local Python/SymPy execution or stdout comparison was performed in this review.

## 1. Individual findings

| Validation output | Static source review | Disposition |
|---|---|---|
| `RC-001-QLD-hard-degree5-integrand.txt` | The output claims all shifted propagators were expanded and total-degree-five coefficients generated, with term counts 28/20/20 for each attachment. No paired producer source was located at the expected path or the common filename variants checked during this review. The record remained PENDING at this point; its later follow-up is documented in the 97th review. | `PENDING` |
| `RC-001-dimension8-Q8-one-background-vertex-audit.txt` | The paired source encodes the Q8 contact Ward contraction, ordinary-line propagator identity, traced numerator contraction, Q_LD/Q_RD composite charges and direct B/X/W contact assignments. The output is limited to algebraic Ward building blocks and explicitly excludes loop integration. | `PASS_WITH_NOTES` |
| `RC-001-dimension8-Q8-one-background-line-pole-covariant.txt` | The paired source encodes the d-dimensional invariant angular averages, Feynman-parameter integrations, transverse UV coefficients and integrand-level Ward identity. Its scope is the ordinary-line graph only; contact/R* subtraction and hard matching remain open. | `PASS_WITH_NOTES` |
| `RC-001-dimension8-P0-independent-coefficient-audit.txt` | The paired source checks the local polynomial remainder, coefficient-by-coefficient hard-IR/soft-UV cancellation, matching-scale cancellation, crossing symmetry, all 16 SU(2) assignments and action-to-amplitude normalization. It explicitly does not repeat loop integration or diagram generation. | `PASS_WITH_NOTES` |
| `RC-001-dimension8-Q8-representation-audit.txt` | The paired source checks the muon/tau composite-source representations and the B/X/no-direct-W Q8 connection. Its scope is exact representation/charge bookkeeping, not a loop integral or Ward identity. | `PASS_WITH_NOTES` |

## 2. Exact source and output identities

The four available source files and their archived outputs were fetched from the reviewed `main` tree. Git blob SHA-1 identifies the exact files inspected. No local source reconstruction, SHA-256 calculation, script execution or captured-stdout hash is claimed.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 |
|---|---|---|
| `RC-001-dimension8-Q8-one-background-vertex-audit.py` | `213a89fea0b6494cbc1a173914ef7588c0af06a2` | `b82b692136099760f23fcfe514351f0ad3acc057` |
| `RC-001-dimension8-Q8-one-background-line-pole-covariant.py` | `7222f8fc551e22f59fcd432ca25b4a6ba35548c6` | `cfcc55503ee6848276e62abb242d6df64a8e13af` |
| `RC-001-dimension8-P0-independent-coefficient-audit.py` | `82178a825c753cb02d3fa6e6e4b8da687b017020` | `5ef27c66cac11001a4ea52f381890fbb6a0ee5b0` |
| `RC-001-dimension8-Q8-representation-audit.py` | `f00a152a84e2eb342dfbf20d3e4013ec8490e089` | `dd4d263872c6da11c46d607066d341bc947e33c7` |

## 3. Review boundary

This review did not execute the four available scripts. The source assertions and archived outputs were inspected statically. The Q8 line-pole record is limited to the ordinary-line UV residue; it does not close the contact graph, R* UV/IR subtraction or hard matching. The P0 record is algebraic post-processing of coefficients, not an independent loop integration.

## 4. Register disposition

The four available output paths remain `PASS_WITH_NOTES` based on their declared bounded source/output content; the hard-degree-five output remains `PENDING` because its producer source was not located during this review. No fresh execution or byte-identical stdout is claimed. The subsequent follow-up resolving the degree-five record is in the 97th review.
