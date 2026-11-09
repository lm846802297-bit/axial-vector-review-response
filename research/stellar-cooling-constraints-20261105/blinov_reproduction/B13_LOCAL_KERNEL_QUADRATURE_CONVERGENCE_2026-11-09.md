# B.13 local moving-muon collision-kernel quadrature convergence (2026-11-09)

## Executive result

The independent high-order local-kernel audit passes its explicitly adopted **0.1% screening target at all three sampled \(r,\omega\) points**. The largest change between the \(20\times12\times12\times12\) and \(24\times14\times14\times14\) quadratures is **0.03016%**, at \(r=8\) km and \(\omega=15\) MeV.

This is a sampled-point result. It does **not** certify the complete continuous \(r,\omega\) domain needed for a future source-weighted B.1/B.2 calculation.

## 1. Fixed inputs and method

- Mediator mass: \(m_V=10\) MeV.
- Current: pure vector, \(g_V=1, g_A=0\), rates per \(g_X^2\).
- Profile: 1687-row vertex-preserving reconstruction of the public-figure SFHo-18.8 profile.
- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c.
- Charge states: \(\mu^-\) and \(\mu^+\), evaluated separately.
- Polarizations: longitudinal and two circular modes, evaluated separately.
- Quadrature variables: muon kinetic energy, initial-muon polar angle, photon polar angle, and relative photon azimuth.

The order sequence is \((12,8,8,8)\), \((16,10,10,10)\), \((20,12,12,12)\), and \((24,14,14,14)\).

The audit computes production and absorption from the exact moving-muon phase-space kernel. It does not use the B.14 no-recoil approximation to construct the B.13 result.

## 2. Successive refinement

The maximum relative change is taken over both charge states and all three polarizations, including production, absorption, and reduced absorption.

| Sample point | \(12,8,8,8\to16,10,10,10\) | \(16,10,10,10\to20,12,12,12\) | \(20,12,12,12\to24,14,14,14\) |
|---|---:|---:|---:|
| \(r=8\) km, \(\omega=15\) MeV | 0.2630% | 0.08908% | 0.03016% |
| \(r=12.5\) km, \(\omega=20\) MeV | 0.06740% | 0.01589% | 0.003043% |
| \(r=15\) km, \(\omega=30\) MeV | 0.01815% | 0.000292% | 0.000376% |

The largest \(20\to24\) refinement change is \(3.0160\times10^{-4}\). The successive changes decrease at the two inner/intermediate points; at 15 km the last two changes are both already below \(4\times10^{-6}\).

The 0.1% criterion is an audit-specific numerical screening target, not a literature bound or a physical uncertainty estimate.

## 3. Which integration dimensions control the residual?

At the most demanding sampled point \(r=8\) km, \(\omega=15\) MeV, each dimension is increased separately from the base \((20,12,12,12)\) rule.

| Dimension increased | Changed order | Maximum relative change |
|---|---:|---:|
| Muon kinetic energy | \(20\to24\) | \(1.99\times10^{-8}\) |
| Initial-muon polar angle | \(12\to14\) | 0.04631% |
| Photon polar angle | \(12\to14\) | 0.04851% |
| Relative photon azimuth | \(12\to14\) | 0.008073% |
| All four dimensions together | \((20,12,12,12)\to(24,14,14,14)\) | 0.03016% |

The two polar-angle integrations dominate the residual at this point. The separate one-dimensional changes are diagnostic and are not additive; their combined change need not equal their sum.

## 4. Independent algebraic and kinematic checks

| Check | Maximum residual |
|---|---:|
| Mode-by-mode detailed balance, both charges | \(1.514\times10^{-15}\) |
| Final-muon mass-shell closure | \(1.626\times10^{-13}\) |

The existing 10 exact moving-muon regression tests also pass, including charge conjugation, the photon Ward identity, the stationary-muon limit, and mode-by-mode detailed balance.

## 5. Interpretation and scope

**Established:** at the three selected thermodynamic/kinematic points, the exact B.13 local kernel is stable to better than 0.1% under the final quadrature refinement. The previous \((12,8,8,8)\to(16,10,10,10)\) check was not by itself sufficient at the most demanding point; the additional 20 and 24 order calculations resolve that concern for the sampled points.

**Not established:** a uniform error bound over the full radius-energy domain, or convergence of a source-weighted B.1/B.2 transport calculation after replacing the B.16 Compton source and opacity consistently. A future global B.13 transport calculation still requires a sufficiently dense \(r,\omega\) kernel grid or a validated interpolation-error study.

No density, source, opacity, coupling, or luminosity is rescaled. The B.14--B.16 reference baseline, production axial-vector files, and axial-vector constraint curve remain unchanged.

## 6. Reproducibility

- Actions run: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42548625879
- Machine-readable output: outputs/b13_local_kernel_quadrature_convergence_10mev_2026-11-09.json
- Audit script: audit_b13_local_kernel_convergence.py
