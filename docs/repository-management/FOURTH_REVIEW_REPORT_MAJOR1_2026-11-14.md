# Fourth document review batch — Major 1 derivation and matching notes (2026-11-14)

## Scope and review limits

Reviewed five complete Major 1 documents from the original one-VEV model workstream. The review checked internal definitions, model boundaries, equation conventions, stated power counting, counterterm bookkeeping, claimed validation scope and open gates. It did not rerun the associated SymPy/Python scripts, perform independent loop integrations, or establish physical pole/gauge-independence results.

## Individual outcomes

| Document | Outcome | Findings and action |
|---|---|---|
| `A2_SCALAR_GAUGE_GHOST_VERTEX_LEDGER_2026-11-10.md` | PASS_WITH_NOTES | The ledger is explicitly in the gauge basis and the original one-VEV model. It correctly separates gauge-basis 1PI vertices from apparent couplings induced by field rotation, and warns against double counting when using the full propagator. Its acceptance boundary is appropriately limited: the functional FP operator and scalar-dependent entries are recorded, but the full non-Abelian ghost expansion, PV integrals and ξ cancellation are not claimed. Independently execute the symbolic audit before promoting the algebraic inventory to a validated result. |
| `A3A_MIXED_SCALAR_BUBBLE_KERNEL_2026-11-10.md` | PASS_WITH_NOTES | Derives the scalar/Goldstone (hs) bubble subset at first order in the loop-sized portal and the corresponding scalar-only UV pole. It explicitly excludes gauge/Yukawa portal renormalization, VLL hard matching, complete EFT soft insertions and finite physical mixing. The effective-potential cross-check had missing display-math delimiters; these were corrected without changing equations or coefficients. The accompanying algebraic audit is not a loop-integral test. |
| `A3B_TADPOLE_VEV_FIELD_COUNTERTERMS_2026-11-10.md` | PASS_WITH_NOTES | Provides a consistent-looking symbolic organization of tadpole, VEV, parameter and general nonsymmetric field counterterms. It correctly avoids selecting finite renormalization conditions and warns against double-counting tadpole shifts. Before a finite mixed self-energy can be assembled, the calculation still needs one declared tadpole/VEV prescription, a field-renormalization convention and the full UV/EFT coefficients in a common scheme. |
| `A4B_GENERAL_XI_ON_SHELL_CUT_CANCELLATION_2026-11-10.md` | PASS_WITH_NOTES | The result is correctly scoped to the gauge-parameter independence of the on-shell absorptive part of the one-loop (ss) kernel and its correspondence to (s\to A'A'). It explicitly does not claim gauge independence of the full complex pole. A notation inconsistency in the derivative cut defined Greek ν but subsequently used a four-vector (u); this was corrected to (u=p+q_a). The stated numerical scan and cut-width agreement were not independently rerun in this documentation pass. |
| `A5B_RESTRICTED_EFT_RGE_AND_HARD_SOFT_SCALE_CANCELLATION_2026-11-10.md` | PASS_WITH_NOTES | Gives a restricted (C_5C_5^\ast) contribution to the dimension-six derivative-operator beta function and demonstrates cancellation of the displayed hard/soft leading logarithms. It repeatedly disclaims a complete anomalous-dimension matrix, complete (O(\hbar^2)) scalar-pole calculation and full-model scale uncertainty. Crucially, it states that the committed script has not yet had a clean exact-file execution; retain that reproducibility task as open. |

## Cross-document consistency

1. A2 and A3a use the same original one-VEV field definitions and the portal-counting convention (lambda_{HS}=O(hbar)).
2. A3a's scalar-only portal pole must not be substituted for the complete portal beta function. A3b explicitly preserves the missing gauge, Yukawa and VLL contributions.
3. A3b separates the local portal mass counterterm from the derivative/mixed-field counterterm; no physical mixing angle follows from the counterterm identity alone.
4. A4b validates one absorptive on-shell sector only. It cannot be used to infer a gauge-independent full complex pole.
5. A5b's leading-log cancellation is restricted to the stated (C_5C_5^\ast) sector. The remaining soft insertions, operator mixing, full portal beta and common matching scheme remain open.
6. These documents are a staged derivation chain, not evidence that Major 1 Higgs–singlet mixing or the Higgs-constraint recast is complete.

## Edits made

- Corrected two display-equation delimiters in the A3a effective-potential cross-check.
- Corrected the (u=p+q_a) four-vector notation in the A4b mixed derivative-cut definition.
- No coefficient, physical assumption, numerical result or acceptance status was changed.

The five outcomes have been entered in `DOCUMENT_AUDIT_REGISTER.csv`.
