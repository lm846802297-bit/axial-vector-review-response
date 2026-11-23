# Research Task Brief: ordered LD-W-06 external left antilepton field

- Task ID: 20261123-ldw06-external-antilepton-leg
- Status: assigned for local exact validation
- Prepared on: 2026-11-23; prepared by/assigned to research validation assistant
- Repository: lm846802297-bit/axial-vector-review-response.
- Baseline: validation/rc001-ldw06-external-conjugate-higgs-leg at 738ea49a0146ee3777d4c057bbb9a40ef77b8fc1, based on main 276cb335d466d1c1864448bcd222fe60d7fdcdc8.
- Related: frozen common-$k$ ordinary-matter gate 7; no PR or remote operation.

## 1. Question
With all external momenta incoming, does a single reducible W emission from the original barred fermion $\bar L(p_1)$ on the actual LD-W-06 S–S lower box have the expected left-ordered chiral Ward endpoint, and which off-shell term can be removed by the massless external fermion equation? No repeat of either Higgs graph.

## 2. Exact inputs
Pin the frozen B1 routing, B2c oriented fermion phase and four-point numerator, raw weak representation, and 1PI/1PR boundary. Pin exact bytes and read source status, lock and AGENTS. No external dataset. Prior scalar validation on the topic branch is context only.

## 3. Execution baseline
Run on an actual detached sparse checkout of topic base with only the proposed checker added before execution. No writes outside local scratch. Capture exact dirty list, underlying main pin, command, start/end, wall clock, runtime, I/O hashes and the unchanged frozen blob identities.

## 3A. Standards provenance
Central source db503f0eb579bdbcac702e44237a6610c34690e7. Exact standards-lock SHA-256 165a29e0b6f372f194d33acac208edfcd2c850d1019db6f18111c5b0f7984813. Applied profiles: task-handoff, research-compute, research-quality-gate, rcrps-v1.0.1. Local extensions: AGENTS project task routes and axial structured-result UV–EFT metadata. Exact brief hash is bound by the separate task provenance JSON.

## 4. Conventions
Metric (+---), all incoming, Fourier exp(-ipx), ordinary Feynman gauge. Work in massless unbroken SU(2) with the frozen Pauli/2 and conjugate slot orientations. Show how the fundamental weak vertex is represented in the archived dual barred slot. Keep chiral matrix order, phase factors, and actual lower heavy denominator explicit.

## 5. Assumptions and scope
Bare integrand only. No loop integration, running, external on-shell W requirement, ghosts, fermion or field-strength renormalization, complete LSZ/Ward/STI, or Wilson extraction. No assumption that a partial Ward endpoint cancels another graph.

## 6. Prior evidence
Only two scalar external emissions have been checked separately and a subset of the internal assembly has been checked; do not import or rerun their proofs. Frozen elementary chiral WTI is a reference comparison, not evidence for the actual sewn box.

## 7. Independent derivation
Solve all-incoming radiation and ordered Yukawa/inner scalar vertex constraints and fix the physical fermion arrow. Sew factors of i, four-dimensional exact gamma matrices and weak indices. Compare to left-endpoint Ward factor using the shifted lower box. Distinguish restoring original barred propagator from contracting through an on-shell external row.

## 8. Gates
Exact symbolic connected WTI after clearing denominators; exact full weak/Dirac comparisons at two off-shell rational points and one on-shell projected barred leg. Reject wrong momentum crossing, reversed arrow, misplaced matrix/projector, wrong dual weak action, and lost inverse-propagator part. Count tested matrix entries, no quadrature or uncertainty. Validate native replay and updated task/run manifests against current pinned validators.

## 9. Deliverables
Local README, exact checker and native JSON, immutable input pins, real RCRPS run manifest, standard task-provenance JSON and checksum inventories. No production CI or PR.

## 10. Open items
Right $L(p_4)$ external emission, common external-field/wavefunction completion, full 1PI/1PR and gauge-sector sums, integrated subtraction and Wilson coefficient remain unsolved here.
