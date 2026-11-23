# LD-W-06 external Higgs leg task

**Frozen main:** `89cd043984012215f74ae331049a626badea9d57`; prior validation head `a8a43434ec7bf48371033f5e371baa0af41cd133`. [Pinned task template](https://github.com/lm846802297-bit/high-energy-theory-research/blob/142267bc803c90aa681110293b66b73947bbcaa1/templates/research-task-brief.md).

1. **Question:** What is the actual external (H(p_2)) emission attached to the ordered LD-W-06 four-point box?
2. **Inputs:** Frozen B1 routing, B2c oriented phases and numerator, raw weak bridge, and 1PI/1PR boundary; fingerprints in `provenance.json`.
3. **Git/runtime:** Local validation only against pinned upstream; Python and SymPy versions in native output.
4. **Conventions:** All incoming, (+---), Feynman gauge, `t = Pauli/2`, cross-vertex A=`H`, B=`H†`. Retain common phase, final chirality, actual shifts, and external inverse-propagator term.
5. **Assumptions:** Unbroken theory. Nonsingular exact diagnostic momenta; no loop integral or regulator assumption.
6. **Prior evidence:** Prior appendix validates ordered internal subset, not external amplitudes; no endpoint software repair is repeated.
7. **Independent route:** Sew explicit oriented scalar vertices and weak indices to the four-point seed, then compare to a shifted scalar-leg factor acting on the `-T3/4` seed.
8. **Acceptance:** Exact uncontracted and contracted rational comparisons, two off-shell points, one after scalar mass-shell projection; reject wrong weak order, omitted heavy shift, wrong current, lost phase and off-shell inverse-propagator omission.
9. **Outputs:** Algebra and replay command, exact code/JSON, provenance and SHA-256 manifest.
10. **Limits:** One reducible graph only; no integrated cancellation, wavefunction renormalization, full LSZ, STI, or Wilson coefficient.
