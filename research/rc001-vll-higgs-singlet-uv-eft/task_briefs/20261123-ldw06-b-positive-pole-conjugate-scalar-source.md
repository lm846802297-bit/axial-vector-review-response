# Task brief: LD-W-06 B positive scalar pole and conjugate-scalar charge source

- ID: 20261123-ldw06-b-positive-pole-conjugate-scalar-source; date: 2026-11-23.
- Target: axial-vector-review-response, validation/rc001-ldw06-external-conjugate-higgs-leg at 5e826d437640e79ec9900c90c0832cd4be1371f1; observed main 871c9c57feb36ea0df549550bb4c307dacadb8cd. Local-only research; no branch or CI mutation.

1. **Question:** At identical frozen loop momentum k, does the B-side positive scalar Ward pole and the external H† charge term share the same weak and denominator factors? Does the leading current contraction cancel while a q-dependent part remains?
2. **Sources:** Frozen B1 kinematics, oriented vertices, raw weak bridge, explicit scalar/seagull kernels, common-k S–S bridge and gate ledger; prior 738ea49a, e83f1935 and 5e826d43 are context, not imported checkers.
3. **Execution:** Actual detached topic base, only candidate check.py untracked before fresh command. Preserve source checksums, runtime and actual wall time. No remote writes.
3A. **Standards:** Central db503f0eb579bdbcac702e44237a6610c34690e7 and lock digest 165a29e0b6f372f194d33acac208edfcd2c850d1019db6f18111c5b0f7984813. Apply task-handoff, research-compute, research-quality-gate, rcrps-v1.0.1; axial AGENTS and UV–EFT extension. Task record binds this brief's actual hash.
4. **Conventions:** Frozen all-incoming, metric (+---), Fourier exp(-ipx), physical SU(2) slots (-t transpose,t,-t transpose,t), common g2 times P4 phase removed. No dummy-variable translation for this B match.
5. **Assumptions:** Bare unintegrated terms, nonsingular exact kinematics. Separate H† charge source from its inverse term; no seagull/ghost/counterterm or other graph in the tested pair. No scale or regulator claim.
6. **Prior basis:** Both negative poles and fermion charge subtotal already checked; earlier all-external check plus partial internal subtotal did not isolate the B positive pole/current cancellation.
7. **Method:** Independently sew full B scalar contracted numerator, algebraically remove the negative pole, solve the shifted external lower-box vertices, and compare actual weak sewing and rational matrices to the factored remainder.
8. **Predeclared gates:** Exact symbolic current/pole identity; nonzero generic q and a·q, and genuine nonzero q with a·q=0 but a·b≠0. Reject wrong weak order, charge sign, copied current and unshifted scalar propagator. Stop rather than infer an ungrounded full identity.
9. **Outputs:** Compact proof and exact checker, native JSON with sample, immutable inputs, task provenance, measured RCRPS manifest and checksums.
10. **Unresolved:** A positive endpoint, other sources and inverse pieces, seagulls/three-W/gauge-sector sum, field terms, full STI and Wilson/matching remain separate.
