# Radial-scalar collider recast and allowed-mass study

**Status:** official Belle II numerical supplements are archived and the published scalar benchmark curves are reconstructed; model-specific UV recast and full allowed-mass classification are **not yet complete**.  
**Branch:** `research/radial-scalar-original-model-belleii-20261105`  
**Base:** `main` at `d3c8c573e0b219dbcb4be62dc57f77fdc04c4f96` (2026-11-05).  
**Purpose:** internal research record. Nothing in this directory should be read as a completed exclusion result until its evidence gate is passed.

## 1. Research questions

This is an **independent follow-up research programme**, not a list of unresolved requirements for the current referee response. The 2026-11-04 referee-facing response already addresses Major Point 1 at the agreed scope. The additional calculations below may strengthen future phenomenological work, but completing them is not a prerequisite for the current response.

The research questions were originally tracked in the historical note `Major_Point_1_scalar_response_status_2026-10-27.md`; that note is retained as provenance, not as the current acceptance criterion:

1. **Model-specific collider recast for the radial scalar \(s\).** Translate published collider searches into constraints on the actual radial mode of the UV model, rather than borrowing coupling limits from a generic muonphilic or Higgs-like scalar benchmark without checking its assumptions.
2. **A validated scalar-mass viable set.** Combine the chosen UV parameter relations, scalar self-coupling perturbativity, portal/mixing treatment, and applicable collider exclusions into a point-by-point classification. Do not claim a universal interval in \(m_s\) if the answer depends on \((m_{A'},g_X)\), the portal boundary, or the decay pattern.

The desired final output is a conditional allowed set in a stated benchmark, not a model-independent statement that one scalar-mass interval is always viable.

## 2. Baseline and relation to existing work

This branch starts from the exact `main` commit listed above. The following work already exists and must be reused rather than silently repeated:

- `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Major_Point_1_scalar_response_status_2026-10-27.md`: response status; explicitly leaves model-specific scalar-search recasts and near-degenerate experimental classification open.
- `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Higgs_portal_exact_mass_eigenstate_one_loop_2026-10-27.md`: numerical mass-eigenstate one-loop \(h\)-\(s\) self-energy at two Plan-C-lite benchmarks, with EFT-soft subtraction and validation checks. It is **not** a completed pole-scheme closure or collider recast.
- `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/scalar_coupling_constraints_source_note_2026-10-28.md`: source-anchored summary of selected low-mass scalar–muon limits. These light-scalar limits do **not** directly constrain the \(m_s\gtrsim10\,\mathrm{GeV}\) reference benchmark used in Fig. 2.
- `Replies_to_Referee_3_referee_facing_2026-11-04.tex`: the current referee-facing response gives the source-anchored Belle II/BaBar discussion and explicitly distinguishes experimental benchmark limits from exclusions of the original UV radial scalar.

The branch must preserve these distinctions. A source-reported search limit, a translated benchmark limit, and a fully recast UV-model exclusion are three different evidence levels.

### Model-scope lock — original paper only

This research uses only the field content and UV benchmark of the original paper: the single symmetry-breaking scalar \(S\), its single VEV \(v_s\), and the original vector-like-lepton sector. The scalar relations used here are

\[
m_{A'}=2g_Xv_s,\qquad m_s^2=2\lambda_Sv_s^2,\qquad y_{s\ell\ell}=m_\ell/v_s.
\]

No additional scalar, altered symmetry-breaking sector, or replacement UV completion is introduced in this workstream. Separate discussion of another referee point does not modify the model baseline used for this scalar analysis. This PR neither changes the manuscript nor makes the collider recast a prerequisite for the current Major Point 1 response.

## 3. UV benchmark and equations to freeze before scanning

Use the model conventions in the archived v6 source and the current response. For the **original paper's one-VEV UV model**,

\[
m_{A'}=2g_Xv_s,\qquad v_s=\frac{m_{A'}}{2g_X}.
\]

For the mass-proportional light-lepton Yukawa benchmark,

\[
y_{s\ell\ell}=\frac{m_\ell}{v_s}
=\frac{2g_Xm_\ell}{m_{A'}},\qquad \ell=\mu,\tau,
\]

subject to checking the exact mass-eigenstate couplings and the stated VLL-mixing assumptions at each benchmark. This is a model relation, not a universal scalar identity.

The scalar self-coupling follows from

\[
m_s^2=2\lambda_Sv_s^2,\qquad
\lambda_S=\frac{m_s^2}{2v_s^2}
=\frac{2g_X^2m_s^2}{m_{A'}^2}.
\]

For a chosen perturbativity criterion \(\lambda_S\leq\lambda_S^{\max}\),

\[
m_s\leq \sqrt{2\lambda_S^{\max}}\,v_s
=\sqrt{\frac{\lambda_S^{\max}}{2}}\frac{m_{A'}}{g_X}.
\]

If \(\lambda_S^{\max}=4\pi\), this becomes \(m_s\leq\sqrt{2\pi}\,m_{A'}/g_X\). Record the criterion explicitly; do not present it as an experimental exclusion.

### Decays that must be included

For a CP-even scalar with interaction \(-y_{s\ell\ell}s\bar\ell\ell\),

\[
\Gamma(s\to\ell^+\ell^-)
=\frac{|y_{s\ell\ell}|^2m_s}{8\pi}
\left(1-\frac{4m_\ell^2}{m_s^2}\right)^{3/2}.
\]

When kinematically open, \(s\to A'A'\) must be included. Under the canonical radial-mode normalization used here,

\[
\Gamma(s\to A'A')
=\frac{m_s^3}{32\pi v_s^2}
\sqrt{1-4r_A}\,(1-4r_A+12r_A^2),\qquad
r_A=\frac{m_{A'}^2}{m_s^2}.
\]

This formula is to be independently checked against the exact Lagrangian convention before use in a final numerical result. The channel opens at \(m_s>2m_{A'}\). Its cascade decays depend on the \(A'\) branching fractions; they can reduce \(\mathrm{BR}(s\to\mu^+\mu^-)\) and \(\mathrm{BR}(s\to\tau^+\tau^-)\), or create different multi-lepton/invisible signatures.

Portal-induced decays and production must use a consistently defined \(h\)-\(s\) mixing input. Away from degeneracy, a small-angle approximation may be used only after validation; near \(m_s\simeq m_h\), use a width/pole-consistent treatment and state the portal boundary condition. Do not turn the existing two benchmark self-energy calculation into a global mixing-angle bound.

## 4. Collider channels to audit

### Priority A — published Belle II searches with spin-0 interpretations

1. **Four-muon resonance:** \(e^+e^-\to\mu^+\mu^-s\), \(s\to\mu^+\mu^-\). Belle II used \(178\,\mathrm{fb}^{-1}\) and covered \(m_s=0.212\text{--}9.0\,\mathrm{GeV}\). The publication reports 90% CL upper limits on \(\sigma\times\mathrm{BR}\) of approximately \(0.055\text{--}1.3\,\mathrm{fb}\) for its muonphilic-scalar interpretation; its quoted coupling limits range from \(0.0018\) to \(0.040\) for masses below \(6\,\mathrm{GeV}\). These ranges summarize the paper; they are **not** point-by-point limits for the present UV model.
   - Paper: https://arxiv.org/abs/2403.02841
   - Belle II publication record and supplemental-material entry point: https://docs.belle2.org/pub_data/publications/4383/
   - Published PDF/supplemental numerical results must be inspected and mapped to the precise benchmark before a recast is claimed.

2. **Tau-pair resonance:** \(e^+e^-\to\mu^+\mu^-s\), \(s\to\tau^+\tau^-\), for the relevant leptophilic spin-0 interpretation. Belle II used \(62.8\,\mathrm{fb}^{-1}\) and covered \(m_s=3.6\text{--}10\,\mathrm{GeV}\). The paper reports 90% CL upper limits on \(\sigma\times\mathrm{BR}(s\to\tau^+\tau^-)\) ranging approximately from \(0.7\) to \(24\,\mathrm{fb}\), with leading scalar-coupling sensitivity above \(6.5\,\mathrm{GeV}\) for its benchmark.
   - Paper: https://arxiv.org/abs/2306.12294
   - Belle II publication record: https://docs.belle2.org/pub_data/documents/4407/
   - Recheck the paper's exact spin-0 normalization and production assumptions; do not infer a pointwise UV limit from the abstract-level range.

### Priority B — complementary direct and Higgs-sector searches

- Audit BaBar/Belle leptophilic-scalar searches and determine whether their published efficiencies/limits apply to the present scalar's production kinematics and decay modes.
- Audit Higgs signal-strength and direct singlet-scalar searches for the portal-mixed component.
- Check exotic Higgs decay channels when kinematically open, including \(h\to ss\), using the actual scalar potential and trilinear coupling rather than assuming the branching fraction.
- Add LHC/LEP/high-energy searches only where the model's production and decay topology matches a published limit or a reproducible recast can be constructed.
- Do not use future-collider sensitivity projections as present exclusions.

## 5. Definition of the output: an allowed set, not an unqualified mass interval

At each fixed benchmark \(b=(m_{A'},g_X,\lambda_{HS}\text{ or a stated portal/mixing condition},M_E,\theta_{\ell L/R},\ldots)\), classify each \(m_s\) point as one of:

- **Excluded:** a published limit applies to the same observable and a validated UV prediction exceeds that limit at the stated confidence level.
- **Allowed by the constraints actually evaluated:** all applicable constraints in the declared list are passed. This does not mean globally allowed by every possible experiment.
- **Unclassified:** a required branching fraction, acceptance, portal/mixing input, or applicable experimental limit is unavailable or has not been checked.
- **Theoretically inconsistent:** violates the selected perturbativity or other explicitly imposed theoretical criterion.

The final viable set is

\[
\mathcal V_b=\{m_s:\text{theoretical criteria pass and every applicable, evaluated experimental constraint passes}\}.
\]

It may be disconnected, benchmark-dependent, and incomplete until all listed gates are passed. Do not compress it into one interval unless the scan demonstrates that the allowed set is connected.

## 6. Required workflow and acceptance gates

1. Freeze the exact model Lagrangian, VEV normalization, scalar Yukawa normalization, VLL masses/mixings, portal boundary, and scan benchmark.
2. Extract the published per-mass \(\sigma\times\mathrm{BR}\) limits and any public numerical supplemental data for each target analysis; record units, CL, mass resolution, and the benchmark assumed by the experiment.
3. Reproduce the experiment's benchmark coupling or cross-section curve within documented interpolation/rounding accuracy before changing the model.
4. Compute the model-specific production cross section, total width, proper lifetime, and all relevant branching fractions at each scan point. Include \(s\to A'A'\) when open and all consequential \(A'\) cascade decays.
5. Map predicted yields to the published observable. Use published acceptance/efficiency information where available. If detector response is not public and a detector-level simulation cannot be validated, label the result a **published-limit reinterpretation**, not a full detector-level recast.
6. Recast each search independently, preserve its confidence level and assumptions, and avoid combining limits without a statistically valid combination procedure.
7. Apply perturbativity and validated portal/mixing constraints point by point; resolve or explicitly flag the near-degenerate \(h\)-\(s\) region.
8. Produce reproducible tables/plots and a source-to-claim ledger; report excluded, evaluated-allowed, unclassified, and theoretically inconsistent points separately.
9. Only after these gates pass, prepare concise numerical language for the referee response. Until then, do not change the formal response to claim a completed exclusion map.

## 7. Deliverables

- This scope and workflow record.
- A source-by-source evidence ledger.
- A benchmark and observable specification.
- Reproducible width/branching-fraction and production calculation scripts, with tests.
- A mass-parameter scan with an explicit status for every point.
- A final validation note distinguishing recast limitations from physical conclusions.
- A short, accurate response-letter paragraph once numerical findings are validated.

## 2026-11-05 update — Belle II benchmark mapping

A source-level audit now distinguishes the two published spin-0 benchmarks:

- The four-muon search uses a muonphilic scalar benchmark and its own scalar signal efficiencies. The original UV model's \(s\to\tau^+\tau^-\) and \(s\to A'A'\) widths can reduce the direct dimuon branching fraction.
- The tau-pair search uses mass-proportional leptophilic Yukawas \(\xi m_\ell/v\), with \(v=246\,\mathrm{GeV}\). The original UV model matches the \(\mu,\tau\) Yukawa normalization through \(\xi_{\mathrm{UV}}=v/v_s=2vg_X/m_{A'}\), conditional on the original single-VEV benchmark.
- The tau threshold makes \(\mathrm{BR}_{\tau\tau}\) strongly mass-dependent near \(2m_\tau\). The analytic two-channel diagnostic gives 0.537 at \(m_s=3.6\,\mathrm{GeV}\), 0.965 at 4 GeV, and 0.996 at 10 GeV, with \(s\to A'A'\) closed.
- The \(s\to A'A'\) channel can dominate once open; it must be included before translating either published limit.

Detailed formulas and benchmark assumptions are in [belleii-benchmark-mapping-2026-11-05.md](belleii-benchmark-mapping-2026-11-05.md). The new parameter-grid driver is [scan_original_uv_widths.py](scan_original_uv_widths.py), with regime/completeness tests in [test_scan_original_uv_widths.py](test_scan_original_uv_widths.py). The official raw files are archived under data/raw/belleii/; exact hashes are in [data/manifest-2026-11-05.json](data/manifest-2026-11-05.json). The data checks, source-table anomalies, benchmark-curve reconstruction, and conditional UV/perturbativity overlay are documented in [source-data-audit-2026-11-05.md](source-data-audit-2026-11-05.md). The table parser, numerical checks, conditional perturbativity overlay, and plot reconstruction are implemented in audit_belleii_supplements.py. The downloader and offline payload-validation tests remain in fetch_belleii_supplements.py and test_fetch_belleii_supplements.py.

## 8. Current status

| Item | Status |
|---|---|
| Repository baseline and previous work identified | Complete |
| Belle II four-muon and tau-pair official scalar benchmarks identified | Complete |
| Official supplemental files archived, hashed, parsed, and curves reconstructed | Complete; no detector-level or CLs reanalysis claimed |
| Original-model \(s\to\mu\mu,\tau\tau,A'A',\gamma\gamma\) widths | Implemented and unit-tested |
| One-on-shell/one-virtual \(A'\) three-body cascade | Implemented and scanned |
| Two-virtual-\(A'\) four-fermion width | Double-spectral diagonal contribution implemented; identical-flavor exchange bounded with a Cauchy upper bound, not explicitly integrated |
| Full \(m_s,m_{A'},g_X\) width scan | Executed: 73,728 points |
| Three-body quadrature convergence | Audited on all 4,096 three-body points; 192 vs 768 nodes agrees within \(1.12\times10^{-4}\) relative |
| Four-body quadrature convergence | Audited on 856 unique mass pairs; 96 vs 128 nodes agrees within \(1.39\times10^{-3}\) relative |
| Double-virtual four-body impact on direct scalar BRs | Bounded; maximum exchange upper bound is \(1.85\times10^{-6}\) of direct \(\mu\mu+\tau\tau+\gamma\gamma\) widths |
| \(\lambda_S\leq4\pi\) classification | Applied to all 73,728 points; 68,351 points pass |
| Belle II four-muon mass-resolution comparison | Added using the published reduced-mass resolution envelope and \(M_R\) width conversion |
| Belle II tau recoil-mass resolution comparison | Added using published resolution anchors and conservative intervals |
| Promptness / flight-distance diagnostics | Added using SuperKEKB \(\beta\gamma\simeq0.28\), maximum kinematic boost, and published track-DCA scales |
| Portal-induced widths and finite-VLL loop effects | Not included; zero-portal/decoupled-VLL benchmark only |
| Exact identical-flavor four-body exchange amplitudes | Not explicitly integrated; their contribution is bounded |
| Narrow-width/prompt coupling-level Belle II reinterpretation | Implemented on width-complete rows; conditional only, no new CLs fit |
| Independent MadGraph production cross-section validation | Pending |
| Finite-width line-shape convolution for broad points | Analysis-specific two-Crystal-Ball convolution kernel implemented and synthetic-tested; real Belle II response parameters and production-times-efficiency inputs unavailable |
| Lifetime-dependent detector efficiency for displaced points | Pending; the papers do not provide lifetime-dependent efficiency curves |
| Belle II four-muon and tau-pair narrow/prompt UV reinterpretations | Conditional pointwise tables generated; incomplete-width, finite-width, and lifetime-sensitive points remain unclassified |
| Final excluded / evaluated-allowed / unclassified UV point map | Partial conditional classification generated; full map pending updated scan artifact, finite-width and lifetime response |
| Current referee-response dependency | Not required; this is independent follow-up research and does not change the agreed Major Point 1 response |

The detailed equations, scan counts, convergence checks, mass-resolution anchors, promptness assumptions, and remaining collider-recast gates are recorded in [original-uv-width-scan-and-belleii-width-audit-2026-11-05.md](original-uv-width-scan-and-belleii-width-audit-2026-11-05.md).

The executable scan is [scan_original_uv_widths.py](scan_original_uv_widths.py). The two-virtual-vector calculation and its exchange bound are in [off_shell_four_body.py](off_shell_four_body.py). The Belle II resolution and promptness inputs are in [belleii_resolution_promptness.py](belleii_resolution_promptness.py). Tests cover the width formulas, all three kinematic regimes, the four-body bound, and the published resolution inputs.

The full 73,728-row CSV and the pointwise quadrature-audit tables were generated as local scan artifacts. They are not represented as committed repository data files in this status table. No complete detector-level UV exclusion or universal allowed scalar-mass interval is claimed.


## 9. 2026-11-05 update — narrow-width/prompt benchmark reinterpretation

The first pointwise coupling-level reinterpretation is now implemented in [narrow_prompt_benchmark_recast.py](narrow_prompt_benchmark_recast.py), with seven unit tests in [test_narrow_prompt_benchmark_recast.py](test_narrow_prompt_benchmark_recast.py). The detailed source, assumptions, equations, classification counts, and caveats are recorded in [narrow-prompt-belleii-uv-reinterpretation-2026-11-05.md](narrow-prompt-belleii-uv-reinterpretation-2026-11-05.md).

The four-muon mapping uses \(g_S^{\rm UV}=m_\mu/v_s\) and the published muonphilic-scalar \(g_S\) limit with \(\mathrm{BR}_{\mu\mu}^{\rm ref}=1\). The tau-pair mapping uses \(\xi_{\rm UV}=v/v_s\), the published scalar \(\xi\) limit, and the benchmark \(\mathrm{BR}_{\tau\tau}^{\rm ref}\) computed from its \(e,\mu,\tau\) mass-proportional Yukawas. The two searches are evaluated independently.

Conditional pointwise results on the available width-complete scan rows:

| Classification | Four-muon points | Tau-pair points |
|---|---:|---:|
| Excluded under published narrow/prompt benchmark (conditional) | 1,852 | 0 |
| Evaluated; not excluded by this channel (conditional) | 24,828 | 7,396 |
| Finite-width-sensitive | 11,330 | 4,152 |
| Lifetime-sensitive | 946 | 15 |
| Theoretically inconsistent, \(\lambda_S>4\pi\) | 4,948 | 2,414 |
| Unclassified: incomplete width sum | 26,752 | 4,992 |
| Unclassified: outside numerical limit grid | 0 | 999 |

**Important scan-artifact reconciliation:** the archived 73,728-row CSV used for these tables has 33 columns and predates the later double-virtual four-body code update. It marks all 27,392 \(m_{A'}\geq m_s\) rows as incomplete and contains no four-body width columns. These rows are therefore unclassified here, even though the newer code now implements a double-spectral contribution and exchange upper bound. The scan must be rerun and the artifact regenerated before those points can be included. Do not cite the earlier four-body scan report as if its output had already been incorporated into this CSV.

The 0.10 \(\Gamma/\sigma\) tolerance is an internal conservative diagnostic, not an experimental cut. The 5 mm flight-length comparison is a geometry proxy, not a lifetime-dependent detector efficiency. No finite-width convolution, detector-level lifetime simulation, independent MadGraph production normalization, or event-level CLs fit is complete. Consequently, the pointwise results are conditional benchmark reinterpretations, not a complete Belle II exclusion map.

The formal referee response and manuscript remain unchanged. PR #52 remains Draft.


## 10. 2026-11-05 update — finite-width convolution kernel

The analysis-specific finite-width shape-convolution machinery is now implemented in [finite_width_line_shape.py](finite_width_line_shape.py), with seven synthetic-input tests in [test_finite_width_line_shape.py](test_finite_width_line_shape.py). The input and validation boundary is documented in [finite-width-line-shape-inputs-and-validation-2026-11-05.md](finite-width-line-shape-inputs-and-validation-2026-11-05.md).

The module:
- uses the original-model running partial and total widths as explicit arrays;
- folds the scalar spectral shape with a two-component Crystal-Ball mixture sharing a common mean;
- uses \(M_R=\sqrt{q^2-4m_\mu^2}\) for the four-muon analysis and \(M_{\rm recoil}=q\) for the tau-pair analysis;
- applies the distinct Belle II fit-window widths (60 resolutions total for four-muon and 40 for tau-pair);
- returns a reconstructed signal shape and fit-window signal fraction, not a new CLs limit.

**No real Belle II finite-width convolution has been run.** The archived numerical supplements do not provide the full mass-dependent two-Crystal-Ball parameter tables. The kernel also requires the mass-dependent scalar production-times-efficiency product and running widths over the full integration range. These inputs are not replaced by invented values. Synthetic tests validate only the numerical machinery.
