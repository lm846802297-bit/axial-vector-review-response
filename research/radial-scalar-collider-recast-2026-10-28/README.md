# Belle II reinterpretation of the original-model radial scalar

**Scope:** independent collider-phenomenology workstream for the radial scalar \(s\) in the original single-VEV \(U(1)_{L_\mu-L_\tau}\) model.  
**Benchmark:** historical PR #52 width benchmark, with \(\theta_{\mu R}=\theta_{\tau R}=10^{-2}\), negligible Higgs-portal mixing as an explicit benchmark assumption, and decoupled VLLs.  
**Status:** the 73,728-point width scan and bounded-width pointwise Belle II reinterpretation have been regenerated; 60 unit tests pass. The narrow/prompt conditional classification is archived; detector-level efficiencies and finite-width/lifetime-dependent recasting remain open.

## 1. Scope and independence

This workstream studies only the Belle II four-muon and tau-pair scalar searches and their interpretation for the original radial scalar. It is independent of the Higgs--scalar mixing/complex-pole research workstream. It neither imports nor requires a Higgs--scalar pole calculation, a near-degenerate Higgs analysis, or a result from that separate study.

The negligible-portal assumption is a declared collider benchmark choice. It is not claimed to follow from a symmetry, and this PR does not determine the general portal parameter or the Higgs--scalar mixing prediction. Results are conditional on this benchmark and must be labelled accordingly.

The work uses the original one-singlet, single-VEV field content. It does not add scalar VEVs, RH neutrinos, or other fields. It does not modify the manuscript or the formal referee response. The axial-vector supernova/stellar-cooling transport calculation remains in its separate research PR.

## 2. Model and benchmark definitions

Use
\[
S=\frac{v_s+s+i a_s}{\sqrt2},\qquad
m_{A'}=2g_Xv_s,\qquad
m_s^2=2\lambda_Sv_s^2,
\]
and the small-mixing charged-lepton benchmark
\[
y_{s\ell\ell}\simeq\frac{m_\ell}{v_s},\qquad \ell=\mu,\tau.
\]
The exact mass-eigenstate couplings and VLL-induced corrections are included only to the extent specified by the frozen benchmark and the corresponding calculation modules.

The current full-grid scan uses:
- \(\theta_{\mu R}=\theta_{\tau R}=10^{-2}\);
- negligible Higgs-portal mixing as an explicit benchmark condition;
- decoupled VLLs for the scalar-width calculation;
- \(m_s\): 48 points over 0.212--10 GeV;
- \(m_{A'}\): 48 points over 0.001--100 GeV;
- \(g_X\): 32 points over \(10^{-6}\)--0.1.

The portal and VLL assumptions are not silently varied between scan points. Any alternate benchmark must be specified and scanned separately.

## 3. Existing experimental inputs

The Belle II four-muon supplementary numerical table and the tau-pair arXiv ancillary limits.csv file, their manifest, hashes, source-table audits, and benchmark reconstructions are retained in the Belle II data and audit files. The four-muon source has 2,317 tabulated rows versus 2,315 fits quoted in the paper; the discrepancy remains unresolved. The tau ancillary table has 2,384 raw rows, including three exact duplicate mass rows, leaving 2,381 unique masses.

Known source-data issues remain visible:
- the four-muon supplement contains 2,317 rows while the paper reports 2,315 fits; the discrepancy is unresolved and the raw file is unchanged;
- the tau-pair supplement contains three exact duplicate mass rows; its CSV and TXT representations are byte-identical and count as one dataset.

The published scalar benchmarks must be reproduced with their own observable definitions and normalizations before applying the UV interpretation. A vector-mediator search or limit is not treated as a scalar limit without an explicit scalar reinterpretation.

## 4. Regenerated width scan

The historical PR #52 benchmark has been regenerated using the current double-virtual four-body code:

- 73,728 points: \(48\times48\times32\);
- three-body quadrature order 192;
- four-body quadrature order 128;
- all 60 unit tests pass;
- compressed CSV, JSON summary, SHA-256 sums, source hashes, environment, and test output are archived.

Key diagnostics:
- 68,351 points satisfy \(\lambda_S\leq4\pi\);
- 67,344 satisfy \(|y_{s\ell\ell}|^2\leq4\pi\);
- 66,617 satisfy both scalar-quartic and scalar-Yukawa criteria;
- 27,392 points have nontrivial branching-fraction intervals in the double-virtual four-body regime;
- the maximum \(\Gamma_s/m_s\) in the combined scalar-quartic/Yukawa subset is 0.293407, with no point in that subset above one.

These are scalar-sector diagnostics for the declared collider benchmark, not a detector-level Belle II exclusion and not a complete perturbativity assessment of every coupling in the UV theory. The identical-flavour exchange contribution in the double-virtual four-body channel is bounded using a Cauchy--Schwarz upper bound rather than explicitly integrated.

See SCAN_RUN_RECORD_2026-11-09.md for the complete width-scan run configuration, counts, environment, hashes, and interpretation limits. See BOUNDED_WIDTH_RECAST_2026-11-09.md for the current Belle II pointwise results and their conditional scope.

## 5. Remaining work and acceptance gates

1. Independently validate all partial widths, thresholds, symmetry factors, and the double-virtual four-body treatment.
2. Preserve the published four-muon and tau-pair scalar benchmarks as separate experimental interpretations.
3. Establish the actual mass-dependent detector response and production-times-efficiency inputs. Synthetic Crystal Ball tests validate numerical code only; they are not validation of the Belle II response.
4. Validate prompt, displaced, and long-lived regimes against the published selections. A DCA requirement is not converted into a decay-radius cut, and a detector efficiency is not invented.
5. Perform narrow-prompt and finite-width interpretations separately. A coupling-limit rescaling alone is not a detector-level recast.
6. The narrow/prompt grid classification is archived. Continue with finite-width convolution and lifetime-dependent acceptance before classifying the remaining points.
7. Keep points unclassified whenever production, width, branching fraction, lifetime, response, or acceptance inputs required by the search are unavailable.

## 6. Explicit claim boundary

This PR does not claim:
- a complete Belle II detector-level recast;
- a validated lifetime-dependent efficiency map;
- an exact identical-flavour four-body exchange integration;
- a statistically combined four-muon/tau-pair likelihood;
- a complete UV-parameter-space exclusion;
- a universal allowed scalar-mass interval.

The manuscript and formal referee response remain unchanged.

## 7. Current Belle II pointwise result (2026-11-09)

The regenerated 73,728-point scan is now propagated through the published scalar coupling limits using the full branching-fraction and total-width intervals. The four-muon width/resolution endpoints were corrected so that the lower ratio uses the lower total-width bound and the largest resolution, while the upper ratio uses the upper total-width bound and the smallest resolution.

Current conditional narrow/prompt results:
- Four-muon: 2,746 grid points are above the observed 90% CL limit using the conservative lower branching-fraction endpoint; they occupy 35 discrete scalar-mass grid values spanning 0.212--3.444 GeV. Every such point has \(\Gamma/\sigma<0.1\) over the full interval and a maximum-kinematic mean-flight upper bound below 0.21 mm.
- Four-muon: 39,534 points are evaluated but not excluded by this channel; the largest conservative observed signal-strength ratio in this class is 0.999912.
- Tau-pair: no grid point is excluded in the evaluated narrow/prompt subset. 11,337 points are evaluated but not excluded; their largest conservative observed signal-strength ratio is 0.1353.
- Finite-width-sensitive, width-interval-crossing, lifetime-sensitive, and perturbatively inconsistent points remain separately classified.

The former 1,852-point count from the 2026-11-05 narrow/prompt report is superseded. The current result is still a conditional reinterpretation of published scalar coupling limits, not a detector-level recast or a new CLs result. Full details and limitations are in BOUNDED_WIDTH_RECAST_2026-11-09.md.
