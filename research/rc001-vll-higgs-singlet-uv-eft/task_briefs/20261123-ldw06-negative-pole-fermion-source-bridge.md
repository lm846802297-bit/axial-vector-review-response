# Task brief: LD-W-06 negative-pole bridge to the fermion Ward source

- ID: 20261123-ldw06-negative-pole-fermion-source-bridge; date: 2026-11-23.
- Assigned to research validation assistant. Target: axial-vector-review-response.
- Baseline: isolated validation/rc001-ldw06-external-conjugate-higgs-leg at e83f1935dce60d46cdfe6ebfa0224cb395498c1b; main 276cb335d466d1c1864448bcd222fe60d7fdcdc8.
- Related: frozen ordinary-matter gates 5–7 only. Local checking, no remote changes.

1. **Question:** Do the two secondary-translated negative scalar WTI poles genuinely share the exact lower-box prefactors of the shifted fermion source terms, and which signed weak piece survives when only that source sub-sector is included?
2. **Exact inputs:** Frozen common-k assembly, S–S bridge, secondary shift, raw cross-vertex weak basis, B1 routing and B2c phase kernels, LSZ boundary. The previous A-only shift appendix a8a43434 and four-external source at e83f1935 are context/targets, not imported checkers.
3. **Git/environment:** Exact detached isolated base, ahead-of-archive checker as only dirty input, measured local execution and native replay. Check main and parallel B.13/B.16 state without any writes.
3A. **Standards:** db503f0eb579bdbcac702e44237a6610c34690e7 and lock SHA-256 165a29e0b6f372f194d33acac208edfcd2c850d1019db6f18111c5b0f7984813. Apply task-handoff, research-compute, research-quality-gate, rcrps-v1.0.1 and axial task/UV–EFT extensions. Task JSON binds immutable brief bytes.
4. **Conventions:** (+---), all incoming, Fourier exp(-ipx), physical weak slots (-t transpose,t,-t transpose,t), frozen phase normalization g2 times P4, right chiral projector. A/B shift exact arguments, not fitted.
5. **Assumptions:** Bare unintegrated graph terms, no regulator/loop equivalence claim, no field-strength/ghost/counterterm completion. Selected fermionic source means only the two charge terms, not their external-inverse terms.
6. **Validated baseline:** Earlier A side translated and B side routed but not assembled into the explicit fermion-source signed matrix interface. Prior four external identity does not use this internal-endpoint decomposition.
7. **Independent work:** Rebuild raw A and B slots, show complete B negative-pole translation (including currents and h+q), opposite anchor logics, exact plus-heavy difference, then derive weak-index map to physical fermion source and compare actual reduced box kernels.
8. **Predeclared gates:** Exact symbolic mappings, signed matrix matches at two nonsingular rational configurations, asymmetric h terms and wrong weak order/shift controls. Stop if no nonduplicate relation is fixed by the archive. A pointwise nonzero piece must not be promoted to full Ward noncancellation.
9. **Outputs:** Focused local note/checker/native data, input pins and actual run/standards manifests with checksums and validator replay.
10. **Open:** Complete scalar and fermion endpoint assembly, inverse propagator and Yukawa combinations as appropriate, translation of convergent/regulator-defined integrations, full 1PI/1PR/field/ghost/STI/matching/Wilson remain separate.
