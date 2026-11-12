# Evidence ledger — radial-scalar collider recast

**Status date:** 2026-10-28  
**Model scope:** original paper's single-VEV UV model only, with \(m_{A'}=2g_Xv_s\). No change to the paper's field content is made in this research line.

**Rule:** Every numerical claim in the final scan must link to a source datum or reproducible calculation. Abstract-level ranges are orientation only; they must not be substituted for mass-by-mass likelihood limits.

## Evidence-level definitions

- **E0 — source located:** citation and search channel identified.
- **E1 — source result transcribed:** observable, mass range, confidence level, and stated assumptions extracted.
- **E2 — benchmark reproduction:** reproduce the experiment's published benchmark interpretation before changing the model.
- **E3 — model reinterpretation:** apply the same published observable limit to a validated UV-model prediction with matched assumptions.
- **E4 — detector-level recast:** independently validated event generation, detector response/acceptance, and statistical procedure. Do not claim E4 if only published limits are reinterpreted.

## Source ledger

| ID | Source / observable | Source-level information presently verified | Relevance to this UV radial scalar | Status / next action |
|---|---|---|---|---|
| B2-4MU | Belle II, \(e^+e^-\to\mu^+\mu^-X\), \(X\to\mu^+\mu^-\), arXiv:2403.02841; DOI 10.1103/PhysRevD.109.112015 | \(178\,\mathrm{fb}^{-1}\); \(m_X=0.212\text{--}9.0\,\mathrm{GeV}\); no signal; 90% CL \(\sigma\times\mathrm{BR}\) limits for its scalar benchmark reported in the abstract over about \(0.055\text{--}1.3\,\mathrm{fb}\); quoted scalar coupling range about \(0.0018\text{--}0.040\) for \(m_X<6\,\mathrm{GeV}\). | Directly relevant topology if \(s\) is produced by muon-associated radiation and \(s\to\mu\mu\) is sufficiently large. A non-negligible \(s\to A'A'\), Higgs mixing, or different total width changes \(\mathrm{BR}(s\to\mu\mu)\) and can change the reinterpretation. | E1 partial. Extract per-mass supplemental data and benchmark normalization; reproduce their scalar curve before mapping to UV points. |
| B2-TAU | Belle II, \(e^+e^-\to\mu^+\mu^-\tau^+\tau^-\) with a \(\tau\tau\) resonance, arXiv:2306.12294; DOI 10.1103/PhysRevLett.131.121802 | \(62.8\,\mathrm{fb}^{-1}\); \(m_X=3.6\text{--}10\,\mathrm{GeV}\); 90% CL \(\sigma\times\mathrm{BR}(X\to\tau\tau)\) limits reported over about \(0.7\text{--}24\,\mathrm{fb}\); paper reports leading leptophilic-scalar coupling constraints above \(6.5\,\mathrm{GeV}\) for its benchmark. | Relevant if the radial scalar is produced in the analyzed channel and \(\tau\tau\) is the reconstructed resonant decay. Model-specific \(y_{s\mu\mu}\), \(y_{s\tau\tau}\), widths and branching fractions must be matched. | E1 partial. Extract mass-dependent limits and exact scalar benchmark; reproduce before reinterpretation. |
| BA-BELLE | BaBar and Belle leptophilic-scalar searches already cited in the referee response | The response currently cites these searches but this branch has not yet audited all per-mass limits, normalizations, topologies, or public efficiencies. | May close gaps or provide complementary limits, but only when production/decay assumptions match. | E0. Locate full papers/supplemental data and decide applicability one search at a time. |
| HIGGS-MIX | Higgs signal strengths, direct singlet-scalar searches, and exotic Higgs decay searches | Generic singlet-scalar constraints are cited in the response; no complete UV-specific combination is established here. | Applies through the actual \(h\)-\(s\) mixing and scalar potential. If \(h\to ss\) is open, the trilinear and branching ratio must be evaluated. Near \(m_s\simeq m_h\), simple small-angle estimates are not sufficient without pole/width validation. | E0/E1 incomplete. Freeze portal boundary and calculate model-specific production/decays before applying limits. |
| PORTAL-LOOP | Existing record \`Higgs_portal_exact_mass_eigenstate_one_loop_2026-10-27.md\` | Full mass-eigenstate fermion-loop self-energy evaluated at two Plan-C-lite benchmarks; EFT soft contribution separated; leading derivative matching agreement recorded at \(6.11\times10^{-4}\) relative. The source itself states that full pole-scheme closure and experimental recasts remain open. | Supplies part of the theoretical input for mixing; it does not itself produce an experimental scalar exclusion or a global mixing angle. | Existing partial evidence. Reuse with provenance; do not relabel as complete mixing/constraint validation. |
| PERT | Model mass and self-coupling relations | \(v_s=m_{A'}/(2g_X)\), \(\lambda_S=m_s^2/(2v_s^2)=2g_X^2m_s^2/m_{A'}^2\) under the stated one-VEV benchmark. | Gives a benchmark-dependent theoretical ceiling once \(\lambda_S^{\max}\) is declared. It is not an experimental exclusion. | Algebraic relation available; apply point by point and log the chosen \(\lambda_S^{\max}\). |

## Primary literature links

1. Belle II four-muon resonance search, published version and abstract: https://doi.org/10.1103/PhysRevD.109.112015  
   arXiv: https://arxiv.org/abs/2403.02841  
   Belle II publication page and supplemental-material entry point: https://docs.belle2.org/pub_data/publications/4383/

2. Belle II \(\tau^+\tau^-\) resonance search, published version and abstract: https://doi.org/10.1103/PhysRevLett.131.121802  
   arXiv: https://arxiv.org/abs/2306.12294  
   Belle II publication page: https://docs.belle2.org/pub_data/documents/4407/

3. The current repository's source-anchored scalar constraint note: https://github.com/lm846802297-bit/axial-vector-review-response/blob/main/审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/scalar_coupling_constraints_source_note_2026-10-28.md

4. The existing exact mass-eigenstate portal-loop record: https://github.com/lm846802297-bit/axial-vector-review-response/blob/main/审稿意见-gpt/当前执行/论文修改与一致性核查/2026-10-27/Higgs_portal_exact_mass_eigenstate_one_loop_2026-10-27.md

## Numerical transcription checklist

For each source, record:

- observable and units (e.g. \(\sigma\times\mathrm{BR}\), a coupling, or a mixing parameter);
- confidence level and whether observed or expected;
- exact mass grid and interpolation method;
- experiment's signal model, production normalization and decay assumptions;
- whether \(s\to A'A'\), Higgs mixing, finite VLL effects, or long lifetime alter acceptance;
- whether a published efficiency map or likelihood is available;
- a source URL, retrieval date, and a hash for any locally archived numerical file;
- reproduction residual for the experiment's own benchmark;
- explicit limitation if the result is only a published-limit reinterpretation and not a detector-level recast.

## Claims that must not be made yet

- “Belle II excludes the UV radial scalar for all masses below 9 GeV.”
- “The scalar is experimentally allowed for \(m_s\geq10\) GeV.”
- “The complete phenomenologically allowed scalar-mass interval is known.”
- “The generic muonphilic-scalar coupling limit equals a limit on \(g_X\) without branching-ratio and normalization checks.”
- “The two Belle II searches can be combined by taking the smaller quoted coupling number.”
- “The existing portal-loop benchmarks prove the mixing is negligible for every \(m_s\).”

Any of these claims requires additional evidence beyond the present source-level summary.


## 2026-11-05 source-level model mapping update

The benchmark normalizations and the corresponding original-UV coupling map are now recorded in [belleii-benchmark-mapping-2026-11-05.md](belleii-benchmark-mapping-2026-11-05.md).

- **B2-4MU:** The published scalar signal has scalar-specific simulated efficiencies and is not to be recast with the \(Z'\) efficiency. The original UV scalar shares the muon-FSR production coupling, but \(s\to\tau^+\tau^-\) above threshold and \(s\to A'A'\) when open modify \(\mathrm{BR}_{\mu\mu}\). The per-mass S_supplemental rows remain unextracted; E1 is still partial and E2 is pending.
- **B2-TAU:** The Belle II leptophilic-scalar normalization is \(\xi m_\ell/v\), \(v=246\,\mathrm{GeV}\). It matches the original UV \(\mu,\tau\) Yukawas through \(\xi_{\rm UV}=v/v_s=2vg_X/m_{A'}\). Belle II's scalar efficiency differs from the vector benchmark by 10–20%, so the vector efficiency is not interchangeable. The \(2m_\tau\) threshold and \(s\to A'A'\) channel must be included in the UV branching fraction. The official mass-dependent limits.csv/limits.txt rows remain unextracted; E1 is still partial and E2 is pending.
- **No recast status upgrade:** source-level model mapping and analytic branching-ratio diagnostics do not reproduce the experimental benchmark. Neither B2-4MU nor B2-TAU is upgraded to E2 or E3.

The local code now contains the \(\xi=v/v_s\) normalization helper and the conditional branching-fraction coupling-rescaling helper. The 14 local tests validate formulas, thresholds, bookkeeping, and download-payload validation only; they do not validate source-file retrieval or an experimental limit curve.
