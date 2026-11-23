# Research Task Brief: LD-W-06 external conjugate Higgs

- Task ID: 20261123-ldw06-external-conjugate-higgs-leg
- Status: assigned for local diagnostic validation
- Prepared on: 2026-11-23
- Prepared by / assigned to: research validation assistant
- Topic: RC-001-WW-UV-FF-02, external-leg subset
- Baseline: lm846802297-bit/axial-vector-review-response main at 276cb335d466d1c1864448bcd222fe60d7fdcdc8.
- Related task: gate 7 of the archived LD-W-06 ordinary-matter assembly ledger; prior H leg at 60f2002e49028238d57453e765c63a1e3a0730bf is context only. No PR is part of this task.

## 1. Question and scope
Which shifted lower-point amplitude, external weak ordering, and phase result from emitting incoming W on the original conjugate scalar H†(p3) in the actual ordered LD-W-06 box? Do not relabel the archived bar L(p1). The claim is one bare reducible graph, not an integrated identity, full LSZ, STI or coefficient.

## 2. Exact sources
On the exact baseline, read the frozen upstream B1 routing note §§1–2, B2c oriented phases §§1–2,6, the cross-vertex raw weak-index bridge §§1–3, the 1PI/1PR LSZ boundary §§1–4, and the common-k assembly ledger §6 gate 7. The archived scalar-line and seagull record §3.4 is the independent common-k internal B-current comparison. Capture Git blob and SHA-256 input identities; no outside dataset required.

## 3. Git and runtime
Work in a separate local addition-only directory based on current main; no remote operation and no mutation of prior validation or frozen input files. Pin exact Python/SymPy versions in the resulting diagnostic. The earlier validation branch is not the current standards-adoption baseline.

## 3A. Standards provenance
Central repository lm846802297-bit/high-energy-theory-research, commit db503f0eb579bdbcac702e44237a6610c34690e7. Lock research/standards-lock.yaml, SHA-256 165a29e0b6f372f194d33acac208edfcd2c850d1019db6f18111c5b0f7984813. Task profiles: task-handoff, research-compute, research-quality-gate, rcrps-v1.0.1. Local extensions: AGENTS.md, axial project task routes and claim boundaries; docs/repository-management/STRUCTURED_RESULT_DATA_STANDARD.md, UV–EFT run metadata. The final exact brief SHA-256 is bound by research/standards-provenance/tasks/20261123-ldw06-external-conjugate-higgs-leg.json, not embedded self-referentially.

## 4. Conventions
All momenta incoming, (+---), Fourier exponential sign minus. Use frozen combination of oriented scalar currents, physical external-slot SU(2) generators (Pauli/2 and negative transpose), common four-point Feynman factors, and final chiral projector. Keep q distinct from internal-W loop momentum. Record momentum squares and propagate the heavy mass unexpanded. Couplings symbolic, diagnostics unit arbitrary but consistent.

## 5. Assumptions and exclusions
Unbroken massless light fields in Feynman gauge; exact rational test momenta avoid internal poles. No loop integration, on-shell W assumption, regulator shift, counterterms, ghost diagrams, numerical fit, or rescaling. The H† mass-shell diagnostic amputates only the external scalar pole first.

## 6. Prior validation
Earlier a8a43434ec7bf48371033f5e371baa0af41cd133 covered selected ordinary 1PI subset; earlier 60f2002e49028238d57453e765c63a1e3a0730bf covered the external conjugate partner H(p2) only. Neither provides B-side emission as evidence.

## 7. Independent derivation
Sew the conjugate scalar leg to the four-point seed using the all-incoming Feynman rule and explicit index mapping, enforce each vertex momentum equation, and compare independently to the shifted four-point Ward endpoint in the physical slot convention. Compare against the frozen internal B momentum/current at the same routing; do not infer diagram cancellation.

## 8. Technical gates
- Exact symbolic momentum conservation, shifted Ward factor, and dimension/phase consistency.
- Compare direct uncontracted and contracted amplitudes for all weak generators and Dirac entries at two off-shell nonzero exact points.
- A scalar-only mass-shell check must eliminate the external inverse-propagator term only after amputation.
- Reject wrong crossed shift, transposition/sign, generator order and reuse of internal B current on a non-degenerate point. No grid, quadrature or numerical error bar: this is rational symbolic algebra.
- Verify source fingerprints, exact lock/brief, RCRPS v1.0.1 execution context, and byte-for-byte native replay with the pinned validators.

## 9. Expected outputs
One small README derivation, check.py, exact native JSON, upstream fingerprints, SHA-256 manifests and central task provenance, all local. Reproduction: Python with SymPy, check.py pipe to cmp against native.json. Include one RCRPS v1.0.1 manifest for an actual fresh local diagnostic, recording its measured execution on the exact detached main base with the added script declared dirty. No figures, CI or remote submission requested. Final status at most validated diagnostic.

## 10. Remaining questions
Three other matter-leg pieces and actual external field renormalization are not recomputed; the prior H term is unmodified. Connected, full LSZ/Ward/STI, regulator/small-mass and UV–EFT/Wilson gates remain open.
