# Exact B.13 versus B.14--B.16 Compton opacity: radial local audit

Date: 2026-11-09  
Benchmark: \(m_V=10\) MeV, pure vector current \(g_V=1,\ g_A=0\), rates per \(g_X^2\).  
Status: **the exact B.13 local kernel is numerically stable and is systematically smaller than the B.14--B.16 no-recoil approximation in the inner production region. This lowers the local total opacity, so it cannot explain the current strong-coupling escape probability being too large.**

## 1. Purpose

The preceding local audit establishes that the B.14--B.17 Compton formula is implemented correctly as an approximation. It does not establish that this approximation is accurate for \(m_V=10\) MeV.

This audit evaluates the full moving-muon B.13 phase-space kernel at fixed local energies and radii, then compares it with the B.14--B.16 expression used by the current pure-vector reference baseline.

The comparison is performed charge by charge:

- exact B.13 \(\mu^-\) is compared with the one-species B.17 B.16 reference;
- exact B.13 \(\mu^+\) is reported separately;
- the sum over both charge species is also retained as a diagnostic.

No B.13 result is substituted into the reference transport calculation.

## 2. Numerical method and validation

The exact kernel is evaluated using the existing moving-muon phase-space implementation, with
\[
m_V=10\ {\rm MeV},\qquad g_V=1,\qquad g_A=0.
\]
The phase-space quadrature orders are \((12,8,8,8)\), corresponding to kinetic energy, muon polar angle, photon polar angle, and relative photon azimuth. Three representative points are refined to \((16,10,10,10)\).

The sampled radii are \(8,10,12.5,15,18.5,20,22\) km and the local energies are \(12,15,20,30,50,80\) MeV.

The exact B.13 kernel passes the independent detailed-balance checks:

| Check | Maximum relative residual |
|---|---:|
| \(\mu^-\), mode-resolved detailed balance | \(2.08\times10^{-15}\) |
| \(\mu^+\), mode-resolved detailed balance | \(6.53\times10^{-15}\) |
| \(\mu^-\), summed detailed balance | \(1.66\times10^{-15}\) |
| \(\mu^+\), summed detailed balance | \(6.33\times10^{-15}\) |

The final-muon on-shell residual is below \(1.3\times10^{-13}\) for the base quadrature. Refining the three representative points changes the \(\mu^-\) production rate by:

- \(0.208\%\) at \(r=8\) km, \(\omega=15\) MeV;
- \(0.0206\%\) at \(r=12.5\) km, \(\omega=20\) MeV;
- \(0.0158\%\) at \(r=15\) km, \(\omega=30\) MeV.

Thus the observed B.13/B.16 difference is not a quadrature-convergence failure at the representative points.

## 3. Radial comparison

The table summarizes the B.13/B.16 ratio for the \(\mu^-\) contribution over the six sampled energies. It also gives the B.16 Compton fraction of the total local reduced opacity and the change in total local reduced opacity when only the Compton channel is replaced by exact B.13.

| Radius | B.13/B.16 Compton ratio | B.16 Compton fraction of total opacity | Change in total local opacity |
|---:|---:|---:|---:|
| 8 km | 0.375--0.460 | 37.2--42.6% | \(-24.3\%\) to \(-20.5\%\) |
| 10 km | 0.387--0.481 | 32.2--37.1% | \(-21.2\%\) to \(-17.1\%\) |
| 12.5 km | 0.433--0.582 | 10.1--12.2% | \(-6.93\%\) to \(-4.34\%\) |
| 15 km | 0.452--0.723 | 0.214--0.347% | \(-0.190\%\) to \(-0.062\%\) |
| 18.5 km | 0.466--0.817 | \(7.6\times10^{-10}\)--\(2.1\times10^{-9}\) | negligible |
| 20 km | 0.470--0.827 | \(1.6\times10^{-12}\)--\(5.0\times10^{-12}\) | negligible |
| 22 km | 0.472--0.831 | \(1.5\times10^{-15}\)--\(5.3\times10^{-15}\) | negligible |

The largest impact is concentrated in the \(8\)--\(12.5\) km region. At \(r=8\) km, exact B.13 reduces the local total reduced opacity by approximately \(20\)--\(24\%\), depending on energy. At \(r=12.5\) km, the reduction is only \(4\)--\(7\%\). Beyond 15 km the Compton contribution to the total opacity is negligible.

The \(\mu^+\) correction to the exact B.13 Compton opacity is small in the important inner region: approximately \(1.3\%\) at 8 km, \(0.38\%\) at 10 km, and \(0.072\%\) at 12.5 km. It does not explain the B.13/B.16 difference.

## 4. Physical interpretation

The discrepancy is between two different calculations:

1. B.13 retains the moving-muon phase space and exact recoil kinematics.
2. B.14--B.16 use the non-relativistic-muon and negligible-recoil approximation.

The published paper explicitly introduces the B.14 cross section as the conventional non-relativistic/no-recoil evaluation and notes that the process is typically relevant for \(m_V\lesssim\) MeV. The \(m_V=10\) MeV benchmark lies outside that stated typical regime. See Appendix B, Eqs. (B13)--(B19), of Blinov et al., arXiv:2511.09619 / JHEP 06 (2026) 155.

The local calculation establishes that the approximation can matter in the inner opacity region. It does **not** establish which prescription was used to generate the paper's numerical cooling curve. The paper presents both the full B.13 phase-space expression and the approximate B.14--B.16 reduction, but no public numerical implementation has been identified that settles this choice.

## 5. Relation to the strong-coupling discrepancy

The existing strong-coupling diagnostic requires a *smaller* escape probability than the current calculation:
\[
\frac{P_{\rm esc}^{\rm required}}{P_{\rm esc}^{\rm current}}
\simeq 0.520.
\]

Replacing B.16 by exact B.13 reduces the Compton opacity in the inner region. At fixed source and all other channels, that raises the escape probability rather than lowering it.

Therefore:

- the B.13/B.16 approximation difference is a real local-opacity systematic;
- it cannot, by itself, explain why the current strong-coupling escape probability is too large;
- using exact B.13 would move the strong-coupling discrepancy in the wrong direction;
- no empirical rescaling is justified.

This is a local comparison only. A global B.2 transport calculation with exact B.13 would be a separate alternative-model run, not a replacement for the published-reference baseline.

## 6. Current decision

1. Retain B.14--B.16 as the explicit published-reference approximation until the numerical prescription used for the reference curve is established.
2. Retain exact B.13 as a separate, physically more complete local diagnostic.
3. Do not combine the two prescriptions or interpolate between them.
4. Do not modify the vector luminosity curve or the axial-vector constraint curve.
5. Continue to treat the pure-vector global benchmark as not yet validated.

## 7. Reproducibility files

- audit_b13_exact_compton_opacity_radial.py: radial fixed-energy exact B.13/B.16 comparison.
- outputs/b13_exact_compton_opacity_radial_10mev_2026-11-09.json: pointwise charge-resolved rates and local-opacity changes.
- finite_mixing/moving_muon_compton.py: exact moving-muon B.13 kernel.
- .github/workflows/b13-exact-compton-radial.yml: regression and radial-audit workflow.

The underlying stellar profile remains reconstructed from public figures, not the original Garching simulation table.
