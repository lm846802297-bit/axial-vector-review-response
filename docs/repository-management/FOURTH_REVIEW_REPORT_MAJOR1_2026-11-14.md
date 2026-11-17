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


## 2. Independent current-tree follow-up (2026-11-16)

**Disposition of this review report: PASS_WITH_NOTES.** The five individual dispositions and their scientific scope boundaries are consistent with the current source documents and output records. The original statement that the 2026-11-14 pass did not rerun the scripts remains historically accurate; later review batches provide separate execution evidence for four of the five scripts.

### 2.1 Subsequent execution evidence

| Original document | Current follow-up evidence | What it establishes |
|---|---|---|
| A2 scalar/gauge/ghost ledger | The 11th review reran a2_vertex_ghost_symbolic_audit.py under Python 3.12.14 / SymPy 1.14.0; exit 0 | The listed derivatives, gauge-basis zeros and radial FP coefficients agree with the symbolic output. Full non-Abelian ghost-vector expansion, loop integrals and gauge-parameter cancellation remain open |
| A3a scalar-bubble kernel | The 11th review reran a3a_scalar_bubble_uv_audit.py; exit 0 | Five symmetry-weighted products, their sum and the effective-potential cross-check agree algebraically. This is not a loop-integral or complete portal-beta validation |
| A3b counterterm matrix | The 11th review reran a3b_tadpole_vev_field_counterterm_audit.py; exit 0 | Tadpole derivatives, parameter/VEV mass counterterms and the symmetric zero-tree-portal field-counterterm identity agree. No finite tadpole or field-renormalization scheme is selected |
| A4b general-\(R_\xi\) cut | The 15th review reran a4b_general_xi_on_shell_cut_audit.py over six \(\xi_X\) values and the five stated open-channel points | The reported maximum relative residual \(8.61\times10^{-16}\) and the direct \(s\to A'A'\) cut-width comparison are reproduced. This remains an on-shell absorptive check, not the full real self-energy or complex pole |
| A5b restricted EFT RGE | The exact committed a5b_dim6_derivative_rge_audit.py still has no exact clean-file run recorded in its §8 | The archived output is a locally evaluated curated summary, not proof that the committed file was executed byte-for-byte. The later B5-2A C5-squared audit is a separate script and does not close this exact-file reproducibility task |

The later A2–A3 and A4b reviews do not retroactively turn the original 2026-11-14 documentation pass into a fresh derivation or an independent implementation. They provide subsequent implementation/summary consistency evidence only.

### 2.2 Current source-document consistency

- A2 retains the gauge-basis distinction: no one-loop \(hs\) vector/ghost bubble is added from mixing-induced rotated vertices. The full non-Abelian ghost-vector entries and PV integrals remain outside the ledger.
- A3a retains the scalar/Goldstone bubble subset with UV-pole coupling combination proportional to \(\lambda_{HS}v v_S(6\lambda_H+4\lambda_S)\). The scalar-only pole is not the complete gauge/Yukawa/VLL portal beta function; the portal-squared term is outside the adopted \(\lambda_{HS}=O(\hbar)\), \(O(\hbar^2)\) truncation.
- A3b retains the general field-renormalization matrix and the distinction between local portal mass and derivative/mixed-field counterterms. Its requirement for a declared tadpole/VEV and field-renormalization prescription remains valid.
- A4b's current mixed-cut definition explicitly reads \(u=p+q_a\), consistently with the subsequent \(u\cdot q_V\) and \(u^2\) contractions. The notation repair described in the original report is present; no further source edit is required.
- A5b remains restricted to the \(C_5C_5^\ast\) derivative-operator contribution and the displayed leading hard/soft logarithms. Its own text correctly leaves the complete portal beta, operator mixing, remaining soft insertions, common counterterm scheme, dimension-eight matching and full-model factor-two matching-scale test open.

The A5b output's benchmark identity \(\beta_{c_{\partial HS}}=\Delta\lambda_{HS}^{E}/2\) and its leading-log cancellation are useful restricted-sector checks. They do not establish a complete anomalous-dimension matrix, complete UV–EFT matching, or a physical \(h-s\) pole.

### 2.3 Register and scientific boundary

The five original source-document rows remain PASS_WITH_NOTES in DOCUMENT_AUDIT_REGISTER.csv and their current source blobs match the register. No source coefficient, physical assumption, numerical output or scientific disposition was changed by this follow-up. The later script reruns are recorded in the 11th and 15th review reports; the A5b exact-file run remains open.

**Final boundary:** this is a successful review of the five documents' internal consistency, traceability and stated limits. It is not evidence that Major 1 Higgs–singlet mixing, complete UV–EFT matching, gauge-independent complex poles, finite widths or the Higgs-constraint recast are complete.
