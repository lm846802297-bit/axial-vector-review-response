# C4-C3 direct local recomputation — 2026-11-11

## Executive result

**PASS.** The 301-point, 1204-case EOS moving-nucleon total-scattering calculation was executed directly in the local Python environment. GitHub Actions was not used to perform the calculation.

The calculation uses the existing C4-B2/C4-C1/C4-C2 collision kernel and exact source/input snapshots. The local full-rate table reproduces the archived 1204-case C4-C3 table at double-precision roundoff.

## Inputs and provenance

| Input | Git blob SHA |
|---|---|
| C4-B2 effective-mass collision kernel | `97a2706e978cd22f7ebc08c1f87ce6abd97ad0a7` |
| C4-C1 exact outgoing-energy support | `8f7291be8738e0273353a8c30039c6be1ed8e6a9` |
| C4-C2 full-angle total scattering | `2912788345e482e52308e02e6cbbc87c734a18b0` |
| 301-point EOS profile | `9ff7818b0679992c0a9ba402330ec7f0d1f3041b` |
| 301-point occupation table | `c472040a4551e68ffadbf7addf9402663f99e7e3` |
| C4-C2 16-case reference | `881b6459e8d9a1ac867b0f4dc47ac168d454e488` |

## Calculation setup

- (E_\nu^{\rm local}=100\,\mathrm{MeV}).
- 301 radial points, (r=0.20\)–(15.20\,\mathrm{km}), spacing (0.05\,\mathrm{km}).
- Four local channels at every radius: (n\nu,n\bar\nu,p\nu,p\bar\nu).
- 1204 full local cases.
- Quadrature: (N_{\cos\theta}=8), (N_{E'}=48), (N_p=36), (N_\phi=12).
- Exact outgoing-energy support scan: 10001 points.
- `kappa_N = xi_SPP * Gamma_N_available`; the SPP filling factor is applied exactly once.

A Numba implementation was used only to accelerate the innermost Dirac-matrix contraction. It was checked against the original contraction at representative phase-space points. The original, unaccelerated kernel was also used for all 16 anchor cases.

## Independent reproduction

| Test | Result |
|---|---:|
| Original-kernel anchor cases | 16/16 |
| Maximum anchor deviation from C4-C2 | (5.55\times10^{-16}) |
| Maximum original-anchor vs accelerated 301-run deviation | (2.22\times10^{-16}) |
| Full local rate cases | 1204/1204 |
| Maximum local/archived rate deviation | (5.55\times10^{-16}) |
| Maximum local/archived opacity deviation | (5.55\times10^{-16}) |
| Maximum support-root relative residual | (1.36\times10^{-13}) |

The independently reconstructed radial opacity/tau table agrees with the archived C4-C3 radial table to maximum absolute difference (5.46\times10^{-12}) across the compared numeric columns.

## Density closure and radial convergence

- Maximum neutron density-closure residual: (2.1543\times10^{-3}) (0.2154%).
- Maximum proton density-closure residual: (7.6303\times10^{-3}) (0.7630%).
- Maximum 0.10-km common-node tau difference, normalized to inner tau: (1.2965\times10^{-5}).
- Maximum 0.25-km common-node tau difference, normalized to inner tau: (1.2279\times10^{-4}).
- All local rates are positive.
- All radial optical depths are nonnegative and monotonically non-increasing with radius.

All C4-C3 acceptance conditions pass.

## Optical depths at the inner radius

At (r=0.20\,\mathrm{km}):

| Channel | (	au(0.20\,\mathrm{km};100\,\mathrm{MeV})) |
|---|---:|
| Neutron, neutrino | 22099.1680 |
| Proton, neutrino | 6503.8501 |
| Total, neutrino | 28603.0181 |
| Neutron, antineutrino | 13328.7665 |
| Proton, antineutrino | 4239.8558 |
| Total, antineutrino | 17568.6223 |

These are fixed-local-energy, flat-space radial scattering optical depths, not redshifted transport optical depths or escape probabilities.

## Radial composition diagnostics

| Radius (km) | EOS (X_n/X_p) | (kappa_n/kappa_p), neutrino | (kappa_n/kappa_p), antineutrino | (kappa_\nu/\kappa_{\bar\nu}) |
|---:|---:|---:|---:|---:|
| 0.20 | 3.6013 | 2.1812 | 2.0609 | 1.5533 |
| 5.00 | 3.6402 | 2.5370 | 2.3563 | 1.6094 |
| 10.00 | 5.2693 | 5.1319 | 4.7563 | 1.6649 |
| 15.20 | 25.0705 | 24.8619 | 23.5074 | 1.6036 |

The neutrino total opacity peaks at (r=7.35\,\mathrm{km}), with
(kappa_{\rm sc}=5.9694\times10^{-13}\,\mathrm{MeV}).
The antineutrino total opacity peaks at (r=7.30\,\mathrm{km}), with
(kappa_{\rm sc}=3.5592\times10^{-13}\,\mathrm{MeV}).

The neutron/proton opacity ratio is not identical to (X_n/X_p): it also
depends on the weak form factors, effective masses, and initial/final-state
Pauli factors. In the outermost region the two ratios approach one another.

## Scope

This result is a fixed-local-energy, flat-space radial scattering optical-depth
diagnostic. It does not include gravitational redshift, energy redistribution,
angular transport, or a full escape-probability calculation. C4-D remains
responsible for the distinct transport and energy-transfer moments. No PR #56
transport baseline, manuscript result, or axial cooling limit is modified.
