# Diagnostic of the non-relativistic-muon approximation in B.14 (2026-11-09)

## Executive result

The non-relativistic-muon approximation underlying the reduced Compton expression B.14 is **not parametrically well controlled in the radii that dominate the current 0.1--1 MeV Compton source**.

Using the current reconstructed SFHo-18.8 profile and the exact susceptibility weight appearing in B.17,
```
chi_mu(r) = n_mu F_deg
          = (1/pi²) ∫ dp p² f_mu(E;mu_mu,T)[1-f_mu(E;mu_mu,T)],
```
the source-weighted muon velocity diagnostics are approximately:

- mean speed: 0.761;
- rms speed: 0.775;
- fraction of the susceptibility weight with v_mu > 0.5: 93.2%;
- fraction with p_mu > m_mu: 71.7%.

These are diagnostics of the equilibrium muon distribution, not a direct calculation of the B.13 collision-rate error. The exact B.13 rate weights initial and final muon states with the matrix element and recoil kinematics. Nevertheless, the distribution shows that treating the dominant muons as non-relativistic is not an obviously controlled approximation.

## 1. Method

The profile uses the same (T(r)) and (mu_\mu(r)) that enter the B.13 and B.17 calculations. At each radial point the distribution is
```
f_mu(p,r) = 1/[exp((sqrt(p²+m_mu²)-mu_mu(r))/T(r))+1].
```
The susceptibility-weighted speed is
```
<v_mu>_chi(r) =
  [∫ dp p² f_mu(1-f_mu) p/sqrt(p²+m_mu²)]
  / [∫ dp p² f_mu(1-f_mu)].
```
The corresponding fractions with (p>m_\mu) and (v_\mu>0.5) use the same (p^2 f(1-f)) weight.

To estimate the radii that matter for the low-mass Compton source, the radial weighting is the leading (m_V/T\to0) B.16 form,
```
w_B16(r) ∝ r² N(r)² [n_mu F_deg](r) T(r)^4.
```
This leading-order weight reproduces the archived B.16 radial source fractions to within about 0.1 percentage point in the dominant 5--15 km shells. It is therefore adequate for identifying the region relevant to the approximation check; it is not used to update the luminosity.

## 2. Source-weighted velocity distribution

| Radius | B.16 source-weight fraction | Susceptibility-weighted mean speed | Fraction with (v_\mu>0.5) | Fraction with (p_\mu>m_\mu) |
|---|---:|---:|---:|---:|
| 5--8 km | 17.01% | 0.759 | 92.7% | 71.0% |
| 8--10 km | 55.19% | 0.779 | 94.6% | 75.9% |
| 10--12 km | 23.94% | 0.739 | 91.9% | 66.5% |
| 12--15 km | 3.74% | 0.663 | 83.3% | 46.2% |

About 79.1% of the low-mass B.16 Compton source is emitted between 8 and 12 km. In those two shells the susceptibility-weighted mean speed is 0.74--0.78, and 92--95% of the susceptibility weight has (v_\mu>0.5).

The local profile values explain this:
- at 8 km: (T\simeq38.85\) MeV, (mu_\mu\simeq91.79\) MeV;
- at 10 km: (T\simeq33.93\) MeV, (mu_\mu\simeq102.84\) MeV;
- at 12 km: (T\simeq25.98\) MeV, (mu_\mu\simeq93.73\) MeV.

With (m_\mu\simeq105.66\) MeV, the characteristic thermal/degenerate momenta in the dominant region are not small compared with the muon mass.

## 3. Interpretation for B.13 versus B.14--B.16

The paper states that B.13 is usually reduced using the non-relativistic-muon and negligible-recoil approximations, leading to B.14, and that the Compton channel is relevant mainly for (m_V\lesssim1\) MeV. The current profile shows that the relevant muon population in the emitting core is moderately relativistic.

This motivates the exact B.13 global comparison at:
- 0.1 MeV: clearly within the stated low-mass regime;
- 1 MeV: at the upper edge of the stated regime.

At these masses (m_V/T\ll1) over the dominant source region, so a large B.13/B.16 difference would not primarily be explained by the small (m_V^2/\omega^2) correction in the parentheses of B.14. It would instead point to the non-relativistic-muon/no-recoil reduction and its phase-space treatment.

The 10 MeV B.13 calculation remains a stress test outside the paper's stated (m_V\lesssim1\) MeV Compton regime; it should not be used alone to judge the intended accuracy of B.14.

## 4. Limitations

1. The speed moments are equilibrium-distribution diagnostics weighted by B.17 susceptibility, not the full B.13 collision integrand.
2. The radial B.16 weight uses the leading low-mass (T^4) approximation. It reproduces the exact archived low-mass radial source distribution closely, but is not a new luminosity calculation.
3. The profile remains a published-figure reconstruction. These results establish an approximation-control issue within the current profile; they do not prove the exact numerical discrepancy in Blinov's unpublished implementation.

## 5. Decision

Do not assume B.14--B.16 is automatically accurate simply because (m_V\lesssim1\) MeV. Complete the global B.13 versus B.16 comparison at 0.1 and 1 MeV, retaining separate source-only and opacity-only diagnostics but using the consistent source-plus-opacity replacement for the physical comparison. No empirical correction is applied and no axial-vector curve is updated.
