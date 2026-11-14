# Individual review: portal A4 and A5 research notes

Baseline `11b2410613b9723a648025512ec702b392451179`, author-side review 2026-11-15. Four notes were read in full and compared with their corresponding A4a/A4c/A4d/A5a script outputs rerun during the prior review. This is a scope, algebraic consistency, benchmark and documentation review; it is not a first-principles rederivation of every graph or independent literature verification. Original one-singlet, zero-tree-portal reference and stated conventions apply.

| Document under `research/major1-higgs-scalar-mixing-20261109/` | Individual findings and disposition |
|---|---|
| `A4A_U1X_SS_SELF_ENERGY_2026-11-10.md` | The stated Feynman-gauge UV pole and benchmark widths agree with the A4a script at reported precision; current local residuals remain below `3e-16` at the selected points. The bosonic subset is not the fully renormalized complex pole. Added a dated-status note because the later A4b general-gauge on-shell cut check exists. PASS_WITH_NOTES. |
| `A4C_GENERAL_XI_SS_UV_AND_FIELD_RENORM_2026-11-10.md` | Its general-gauge pole reduces to A4a at xi=1 and matches the A4c symbolic script. The claimed scalar-QED comparison was not independently sourced here; the expression is scoped to UV poles rather than finite self-energy. PASS_WITH_NOTES. |
| `A4D_TADPOLE_IMPROVED_SS_KERNEL_2026-11-10.md` | The zero-momentum tadpole subtraction and d=4 UV coefficient agree with the A4d symbolic script after the undefined `p2` repair recorded in the fifteenth review. The finite expression retains Goldstone dependence; a gauge-independent UV mass pole is not a gauge-independent off-shell finite propagator or physical pole. PASS_WITH_NOTES. |
| `A5A_SCALE_PROVENANCE_AND_MATCHING_SCALE_AUDIT_2026-11-10.md` | Heavy masses, 17.7686 TeV conditional mixing bound, logarithms and partial hard+soft comparison match the A5a script at printed precision. Added a scope note to make clear that a small heavy-threshold splitting supports the central matching choice but does not prove complete RG or scale independence. The historical PR provenance and literature claims were not independently re-established. PASS_WITH_NOTES. |

No physical equations, parameter values or results were changed. The 0.1421% scale change is a selected-subset diagnostic, not an uncertainty on a fully matched pole.
