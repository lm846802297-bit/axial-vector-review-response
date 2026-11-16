# Sixty-fourth review — two-VEV validation and V57 document family

**Date:** 2026-11-16  
**Reviewed base:** `2affc1893cf09b716fd2d893ae4e98797f18ff39`  
**Scope:** the next six `PENDING` entries in `DOCUMENT_AUDIT_REGISTER.csv`.  
**Disposition:** 2 `PASS_WITH_NOTES`, 1 `REVISION_REQUIRED`, 3 `HISTORICAL`.

This is a document and provenance review. The archived physics outputs, model parameters, production kernels, supernova limits and axial-vector constraints were not changed. Source files and historical results were inspected; this review does not claim to have rerun the original local Python jobs.

## 1. Result summary

| Document | Result | Finding |
|---|---|---|
| `research/stellar-cooling-two-vev-20261105/PHYSICS_CROSSCHECK_2026-11-13.md` | `PASS_WITH_NOTES` | The two-VEV gauge mass, eaten/physical CP-odd basis, pure-axial Goldstone relation, PMNS trace identity and direct axial-Goldstone amplitude test are internally consistent. The document correctly keeps finite-mixing UV matching and supernova transport open. |
| `research/stellar-cooling-two-vev-20261105/validation-results-2026-11-05.md` | `REVISION_REQUIRED` | Historical source blobs match the archived branch head, but the convergence CSV is not the direct output/schema of the pinned convergence driver; it uses order 10 as its zero/reference. The order scan also varies \(n_{\rm GL}\) and \(n_\phi\) together. Its code examples use escaped rather than real Markdown fences. |
| `work/v57_before_reading_flow_adjustment.md` | `HISTORICAL` | Complete V5.7 working snapshot with 59 atomic entries and valid internal links. Retain as a pre-adjustment reference; one evidence-row cross-reference is duplicated. |
| `work/v57_corrected.md` | `HISTORICAL` | Explicit V5.6 predecessor. Its section 3.4 is the joint UV–EFT analysis and section 3.5 is the reply template; internal references are consistent apart from one explicitly historical reference to a merged-version §3.6. |
| `work/v57_enhanced.md` | `HISTORICAL` | Alternative V5.7 working snapshot. It retains explicitly unverified portal estimates, has duplicated G.15.6 references in two records and the typo “当前当前”. Do not promote it as canonical. |
| `work/v57_reconstructed_1007.md` | `PASS_WITH_NOTES` | Most complete V5.7 candidate in this set; its core scalar formulas are sound and its internal links pass. Before promotion, unify \(\Delta_{hs}^2\) with the \(\Delta\) used in Work E, fix the duplicated word/reference, and restore two useful self-energy caveats. |

## 2. Two-VEV physics cross-check

### 2.1 Gauge mass and CP-odd basis

For \(Q_X(S)=2\), \(Q_X(\sigma)=1\), and \(D_\mu=\partial_\mu-i g_X Q_X A'_\mu\), the kinetic terms give
\[
m_{A'}^2=g_X^2(4v_s^2+v_\sigma^2),\qquad
v_X=\sqrt{4v_s^2+v_\sigma^2}.
\]
The eaten and orthogonal directions
\[
G=\frac{2v_sa_s+v_\sigma a_\sigma}{v_X},\qquad
a_\perp=\frac{v_\sigma a_s-2v_sa_\sigma}{v_X}
\]
are normalized and orthogonal. The inverse map at fixed \(r_\sigma=v_\sigma^2/(4v_s^2)\) is algebraically consistent:
\[
v_s=\frac{m_{A'}}{2|g_X|\sqrt{1+r_\sigma}},\qquad
v_\sigma=2v_s\sqrt{r_\sigma}.
\]
This verifies the stated two-VEV map under the documented charge and covariant-derivative conventions; it does not establish the scalar potential or the physical pseudoscalar spectrum.

### 2.2 Goldstone/current matching

The \(S\)-phase Yukawa gives a pseudoscalar coupling magnitude \(m_\ell/v_s\). Its eaten component is \(2v_s/v_X\), hence
\[
|g_{G\ell\ell}|=\frac{2m_\ell}{v_X}.
\]
The axial-current divergence gives \(2|g_A^\ell|m_\ell/m_{A'}\). These agree in the pure-axial limit \(|g_A^\ell|=|g_X|\), \(m_{A'}=|g_X|v_X\).

The cross-check correctly identifies the finite-right-mixing boundary:
\[
g_A=-g_X\cos^2\theta_{\ell R}
\quad\Longrightarrow\quad
|g_{G\ell\ell}|_{\rm Ward}
=\frac{2m_\ell}{v_X}\cos^2\theta_{\ell R}.
\]
The mapping helper still returns the leading pure-axial value \(2m_\ell/v_X\). The document correctly says that the finite-mixing UV phase coupling has not yet been projected through the full charged-lepton mass rotations. Do not use the simple Goldstone map at finite mixing until that matching is completed.

The orthogonal physical pseudoscalar \(a_\perp\) has a nonzero \(S\)-phase coupling \(m_\ell v_\sigma/(v_s v_X)\). Its mass, mixing, decays and constraints remain unspecified. This is an important model extension, not a harmless reparameterization of the one-VEV model.

### 2.3 Widths, PMNS trace and amplitude checks

The vector and axial charged-lepton width factors in the cross-check are the standard integrated unpolarized expressions:
\[
\Gamma_V=\frac{g_V^2m_{A'}}{12\pi}(1+2r_\ell)\beta_\ell,\qquad
\Gamma_A=\frac{g_A^2m_{A'}}{12\pi}\beta_\ell^3.
\]
The document properly labels these as partial widths and does not treat them as a complete UV total width.

For a unitary active three-flavour rotation,
\[
G_\nu=U_{\rm PMNS}^\dagger Q_\nu U_{\rm PMNS},\qquad
\operatorname{Tr}(G_\nu^\dagger G_\nu)
=\operatorname{Tr}(Q_\nu^\dagger Q_\nu)=2.
\]
This establishes the inclusive active-light-neutrino coupling norm, not the complete width for Majorana states, appreciable active-heavy mixing, open charged-\(N_R\) channels, non-unitary light mixing or loop-induced electron channels. The report states these limitations.

The Nov. 13 update adds a direct spinor-level check of
\[
q_\nu\mathcal M_A^\nu=2m_\mu\mathcal M_P
\]
at five kinematic points, with maximum relative residual \(8.96\times10^{-13}\). This is a stronger test than the earlier longitudinal \(1/m_{A'}^2\) scaling check and is correctly distinguished from the electromagnetic Ward identity and from the high-energy Goldstone-equivalence approximation.

### 2.4 Thermal convergence and scope

The convergence table has
\[
(n_{\rm GL},n_\phi)=(6,12),(8,16),(10,20),(12,24).
\]
The order-10 to order-12 changes are \(-0.0108\%\) in event rate and \(+0.0202\%\) in emissivity. Because the convergence driver sets \(n_\phi=\max(8,2n_{\rm GL})\), this is combined quadrature refinement, not an independent azimuthal convergence test. The cross-check explicitly records that a fixed-\(n_{\rm GL}\), varying-\(n_\phi\) scan remains open.

The implementation is homogeneous, optically thin and polarization-summed. It does not provide medium-rest-frame T/L-resolved emissivity or opacity, inverse-process trapping, radial transport, diffusion, a luminosity or an SN1987A exclusion. The document correctly preserves these boundaries and explicitly states that the pure-vector Blinov Fig. 7 10 MeV strong-absorption gate remains NOT PASSED.

**Disposition:** physics and code descriptions in this cross-check are coherent. Keep the outstanding finite-mixing Goldstone projection, physical-pseudoscalar potential and independent azimuthal convergence as explicit open work.

## 3. Historical two-VEV validation record

### 3.1 Source provenance — verified

The archived branch `research/stellar-cooling-two-vev-20261105` is at commit
`5ec3c3396b2f85c2a2efd1431a183bf7a7255ca2`. The source blob hashes in the validation table match that branch tree, including:
- mapping: `5b45faf292e49183f97445a6f6ae4ac6c6ffd798`;
- mapping tests: `e38e9479955f7df28dbc2059d3df4e6567a70a5c`;
- amplitude: `3317339e663fbe59739045771902fb0927260c2f`;
- thermal rate: `d37023df57ffea47018593b43ff5b62f7ee34e28`;
- convergence driver: `e36ab13ae32216ae4d3c9a2323099485f880a1b0`;
- decay widths: `be2aefbd9078f43b8aa586f5516ce4caf953a107\).

The reported 6/6 mapping tests and local amplitude/width/smoke-test outputs are therefore correctly attributable to the Nov. 5 branch snapshot. They are historical results, not the later Nov. 13 direct-Ward and PMNS-trace tests documented in the cross-check.

### 3.2 Convergence artifact mismatch — REVISION_REQUIRED

The archived `thermal-convergence-2026-11-05.csv` contains columns `relative_rate_percent` and `relative_emissivity_percent\), with the order-10 row set to zero. The pinned driver at blob `e36ab13...` instead:
- uses the last/highest requested order as the reference (`order_values[-1]`);
- writes `relative_rate_to_reference` and `relative_emissivity_to_reference`;
- uses a different cutoff-row label/schema.

The raw rate and emissivity columns do reproduce the quoted order-10 to order-12 changes, so the numerical comparison itself is recoverable. But the CSV is not the direct output of the pinned driver under its recorded reference convention, and its exact producer is not identified. Preserve the raw values; either regenerate the CSV with the pinned driver or add a deterministic conversion/producer record and label the existing CSV as an order-10-referenced legacy summary.

The report should also state explicitly that the order scan varies \(n_{\rm GL}\) and \(n_\phi\) together. Do not describe it as an independent convergence test in each integration dimension.

### 3.3 Markdown formatting

The four command examples are written with a backslash before each backtick, so GitHub renders literal delimiters rather than code blocks. Replace them with ordinary fenced code blocks during the next revision.

**Disposition:** retain the historical 6/6 and local benchmark results, but keep the validation record `REVISION_REQUIRED` until the CSV producer/reference convention and its formatting are reconciled. No supernova transport or exclusion follows from this local record.

## 4. V57 family — comparison and document-by-document disposition

All four V57 files are working documents committed together in the initial project snapshot; Git history does not establish a later per-file sequence or a canonical final file. Their internal version labels and filenames are therefore not enough to promote one automatically.

### 4.1 Structural checks common to all four files

- Each contains 13 main chapters and 59 atomic audit-item headings.
- Internal Markdown anchors and repository-relative links resolve in the current tree.
- Display-math delimiters and code fences are balanced; no control characters were found.
- The three blank C-01–C-03 rows are explicitly labelled as templates/to be filled, not completed scientific results.
- The unverified \(\delta m_{hs}^2\propto M^2\) candidate and \(|\delta\Pi_{hs}|\simeq0.168\,\mathrm{GeV}^2\) example are explicitly marked as different definitions/conditional calculations that must not be combined or used as a final model result. Preserve that warning.

The core equations checked across the family are consistent:
- \(m_s^2=2\lambda_Sv_S^2\), \(m_{A'}=2g_Xv_S\), and \(\lambda_S=2g_X^2m_s^2/m_{A'}^2\);
- the \(m_s^2\leq8\pi v_S^2\) relation for the stated \(\lambda_S^{\max}=4\pi\) convention;
- the two-scalar tree-level matrix \(m_{hh}^2=2\lambda_Hv^2\), \(m_{ss}^2=2\lambda_Sv_S^2\), \(m_{hs}^2=\lambda_{HS}vv_S\);
- the bounded-from-below condition \(\lambda_H>0,\lambda_S>0,\lambda_{HS}>-2\sqrt{\lambda_H\lambda_S}\), distinct from the positive-Hessian/local-minimum condition \(4\lambda_H\lambda_S>\lambda_{HS}^2\);
- the eigenvalues, rotation convention, \(\tan2\theta=2\Delta/(b-a)\), branch choice and inverse coupling relations in Work E.

These checks support the stated algebraic conventions; they do not mean the model-specific portal loop calculation, full Higgs recast, PMNS completion, finite-VLL kinetic-mixing scan or joint UV–EFT parameter scan has been completed. The documents themselves correctly label those as outstanding.

### 4.2 `v57_before_reading_flow_adjustment.md` — HISTORICAL

This is a 5.7 working snapshot (5660 lines, 419 headings). Its scalar Work E uses one consistent \(\Delta\) notation and includes the useful explicit spectral identity
\[
(m_+^2-m_-^2)^2=(b-a)^2+4\Delta^2.
\]
The file is labelled “before reading flow adjustment” and should remain an archived predecessor, not be treated as the canonical current manual. One evidence-row reference repeats `§6.6` and `附录 G.15.6`; the unverified portal estimate is properly caveated.

### 4.3 `v57_corrected.md` — HISTORICAL

This file explicitly identifies itself as V5.6 (5375 lines, 368 headings). Its joint UV–EFT analysis is §3.4 and its English reply template is §3.5; its navigation and local anchors agree with that structure. The single reference to “merged version §3.6” is explicitly historical. Retain as the V5.6 predecessor; do not merge it into a V5.7 file by copying section numbers.

### 4.4 `v57_enhanced.md` — HISTORICAL

This is an alternative V5.7 snapshot (5485 lines, 372 headings). It contains the same 59 atomic entries, but is not the fullest reading-flow version. It repeats the `G.15.6` cross-reference in two evidence records and contains the duplicated phrase “当前当前”. Its unverified portal estimates are caveated, but the repeated references and typo should be corrected if this version is ever reused. Retain as an alternative historical draft, not as the canonical manual.

### 4.5 `v57_reconstructed_1007.md` — PASS_WITH_NOTES

This is the most complete V5.7 candidate in the reviewed set (5666 lines, 419 headings). Relative to `v57_before_reading_flow_adjustment.md`, it is a close revision rather than an independent document family. It adds an explicit general CP-even mass-matrix presentation and makes the off-diagonal mass-squared notation more explicit.

Before designating it canonical:
1. Define one symbol consistently: the introductory \(\Delta_{hs}^2\) should be explicitly identified with the \(\Delta\) used in Work E, or replace both by one notation.
2. Fix “当前当前” and remove the repeated `§6.6`/`附录 G.15.6` references in the relevant evidence row.
3. Restore the explicit statement that absorptive self-energy parts arise above open thresholds and retain the momentum-dependence check near the two complex poles; the current Work E keeps complex poles/widths but the earlier wording made these triggers clearer.
4. Record the source/version relationship in a small V57 version manifest. The present Git history only shows the four files arriving in the same initial snapshot, so “reconstructed_1007” cannot be proven to be later from commit history alone.

Do not promote this file automatically. The user should have one declared canonical V5.7 source, with the other three retained as historical variants.

## 5. Register reconciliation

Before this review: 378 reviewed, 84 pending:
- 253 PASS_WITH_NOTES
- 2 PASS
- 21 REVISION_REQUIRED
- 102 HISTORICAL

After this review: 384 reviewed, 78 pending:
- 255 PASS_WITH_NOTES
- 2 PASS
- 22 REVISION_REQUIRED
- 105 HISTORICAL

## 6. Required next work

1. Reconcile the two-VEV convergence CSV with the exact pinned driver, and record its reference convention/producer.
2. Add an independent \(n_\phi\) scan at fixed \(n_{\rm GL}\) before claiming azimuthal convergence; preserve the current result as combined quadrature refinement.
3. Keep the finite-right-mixing Goldstone UV projection open until the \(S\)-phase coupling is projected through the full charged-lepton mass rotations.
4. Keep the physical \(a_\perp\) potential, mass, mixing, decays and constraints separate from the one-VEV model.
5. Designate one canonical V5.7 manual only after the reconstructed candidate's notation, references and self-energy caveats are reconciled; do not delete the historical versions.
6. Do not infer a supernova luminosity, transport result or SN1987A limit from either two-VEV local validation record.

**Scientific disposition:** the two-VEV mapping and current-level checks are useful and internally consistent within their stated limits. The local thermal prototype is not supernova transport. The V57 manual family contains sound core formulae and useful review workflows, but its version lineage is unresolved and no model-specific UV loop, experimental recast or joint allowed region is established by these documents.


## 7. Post-review provenance clarification (2026-11-16)

The archived two-VEV branch provenance in §3.1 was checked directly at commit `5ec3c3396b2f85c2a2efd1431a183bf7a7255ca2`. Its tree confirms the six source blobs listed in the report, including the convergence driver blob `e36ab13ae32216ae4d3c9a2323099485f880a1b0`, decay-width blob `be2aefbd9078f43b8aa586f5516ce4caf953a107`, and the historical CSV blob `075314ff389cfa2eade061d8a6d359473e8225c2` at `research/stellar-cooling-two-vev-20261105/thermal-convergence-2026-11-05.csv`.

In the current maintenance tree, the old full convergence driver has been consolidated into `research/stellar-cooling-shared-20261105/stellar_semi_compton_thermal_convergence_common.py` (same blob `e36ab13...`), while the two-VEV path is now a thin adapter (blob `15e97646...`). The historical CSV is no longer present at the two-VEV path; the same CSV blob is present under the original-UV line. Do not mistake that migrated copy for a fresh two-VEV run. The CSV still uses order 10 as its zero/reference and `relative_*_percent` columns, unlike the pinned highest-order-reference driver's `relative_*_to_reference` schema. The validation record remains `REVISION_REQUIRED` until the exact producer/reference convention is reconciled and the command examples are fixed.

The decay-width source comparison was also checked line-by-line. The archived two-VEV blob `be2aefbd...` and current two-VEV file blob `e7fbb438...` retain the same executable formula bodies; the substantive differences are expanded neutrino-normalization/ Majorana/active-heavy caveats in the current docstring. Preserve both hashes as historical and current snapshots rather than overwriting one with the other.

The four V57 working documents remain present with the reported identities. The alternative `v57_enhanced.md` and candidate `v57_reconstructed_1007.md` each contain the duplicated phrase `当前当前`; the candidate also needs its (Delta_{hs}^2)/(Delta) notation and source/version manifest before promotion. No canonical V5.7 choice is inferred from the filenames or the shared initial-commit history.

This review report is `PASS_WITH_NOTES`: the archived branch evidence and V57 disposition are reproducible at the stated level, while the two-VEV validation record remains independently `REVISION_REQUIRED`. No UV–EFT closure, stellar transport, SN1987A limit or axial-vector constraint is inferred.
