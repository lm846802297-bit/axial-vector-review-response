# Belle II reinterpretation of the original-model radial scalar

**Scope:** independent collider-phenomenology workstream for the radial scalar \(s\) in the original single-VEV \(U(1)_{L_\mu-L_\tau}\) model.  
**Benchmark:** historical PR #52 width benchmark, with \(\theta_{\mu R}=\theta_{\tau R}=10^{-2}\), negligible Higgs-portal mixing as an explicit benchmark assumption, and decoupled VLLs.  
**Status:** the 73,728-point width scan has been regenerated with the double-virtual four-body update; 58 unit tests pass. A detector-level Belle II recast and complete scalar-mass classification are not yet complete.

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

The official Belle II four-muon and tau-pair numerical supplements, their manifest, hashes, source-table audits, and benchmark reconstructions are retained in the Belle II data and audit files.

Known source-data issues remain visible:
- the four-muon supplement contains 2,317 rows while the paper reports 2,315 fits; the discrepancy is unresolved and the raw file is unchanged;
- the tau-pair supplement contains three exact duplicate mass rows; its CSV and TXT representations are byte-identical and count as one dataset.

The published scalar benchmarks must be reproduced with their own observable definitions and normalizations before applying the UV interpretation. A vector-mediator search or limit is not treated as a scalar limit without an explicit scalar reinterpretation.

## 4. Regenerated width scan

The historical PR #52 benchmark has been regenerated using the current double-virtual four-body code:

- 73,728 points: \(48\times48\times32\);
- three-body quadrature order 192;
- four-body quadrature order 128;
- all 58 unit tests pass;
- compressed CSV, JSON summary, SHA-256 sums, source hashes, environment, and test output are archived.

Key diagnostics:
- 68,351 points satisfy \(\lambda_S\leq4\pi\);
- 67,344 satisfy \(|y_{s\ell\ell}|^2\leq4\pi\);
- 66,617 satisfy both scalar-quartic and scalar-Yukawa criteria;
- 27,392 points have nontrivial branching-fraction intervals in the double-virtual four-body regime;
- the maximum \(\Gamma_s/m_s\) in the combined scalar-quartic/Yukawa subset is 0.293407, with no point in that subset above one.

These are scalar-sector diagnostics for the declared collider benchmark, not a detector-level Belle II exclusion and not a complete perturbativity assessment of every coupling in the UV theory. The identical-flavour exchange contribution in the double-virtual four-body channel is bounded using a Cauchy--Schwarz upper bound rather than explicitly integrated.

See SCAN_RUN_RECORD_2026-11-09.md for the complete run configuration, counts, environment, hashes, and interpretation limits.

## 5. Remaining work and acceptance gates

1. Independently validate all partial widths, thresholds, symmetry factors, and the double-virtual four-body treatment.
2. Preserve the published four-muon and tau-pair scalar benchmarks as separate experimental interpretations.
3. Establish the actual mass-dependent detector response and production-times-efficiency inputs. Synthetic Crystal Ball tests validate numerical code only; they are not validation of the Belle II response.
4. Validate prompt, displaced, and long-lived regimes against the published selections. A DCA requirement is not converted into a decay-radius cut, and a detector efficiency is not invented.
5. Perform narrow-prompt and finite-width interpretations separately. A coupling-limit rescaling alone is not a detector-level recast.
6. Classify each benchmark point as theoretically inconsistent, excluded by an evaluated search, passes the constraints actually evaluated, or unclassified.
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