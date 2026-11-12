# Radial-quadrature convergence of the SFHo-18.8 profile sensitivity

Date: 2026-11-09  
Benchmark: pure-vector B.1+B.2, \(m_V=10\) MeV, \(g=4.17168965\times10^{-8}\), \(R_{\max}=25\) km.  
Fixed settings: energy order 100, angular order 32, fixed \(\omega\) along the B.2 path.  
Radial orders: 40, 80, 120.  
Status: **the 8--15 km Ferreira-\(\mu_\mu\) diagnostic is radially converged at the sub-percent level. It substantially changes the strong-endpoint opacity, but it does not by itself reproduce the required Fig. 7 escape probability.**

## 1. Why this convergence test is needed

The two published \(\mu_\mu(r)\) curves differ much more strongly in the inner part of the dominant B.1 source region than in 12--15 km:

- 8 km: Ferreira is about 82% higher than Caputo.
- 10 km: about 27.5% higher.
- 12 km: about 17.2% higher.
- 15 km: about 10.2% higher.

The 8--10 km path shell also has a large Compton contribution. The earlier 12--15 km-only profile substitution therefore does not test the dominant source-region discrepancy. This audit extends the same diagnostic substitution over 8--15 km and varies only the radial quadrature order.

The Ferreira curve is the dashed orange SFHo-18.8 profile identified in that paper's Fig. 1 caption at 1 s post-bounce. Caputo Fig. 1 identifies the same named model and time. Both papers cite the Bollig et al. simulation. The substitution remains diagnostic-only because the origin of the different published \(\mu_\mu\) curves is unresolved.

## 2. Radial convergence results

| Radial order | Baseline \(P_{\rm esc}\) | B.1 source ratio, Ferreira / Caputo | Fixed-baseline-source \(P_{\rm esc}\) ratio | Own-source \(P_{\rm esc}\) ratio | Escaped B.1 integral ratio |
|---:|---:|---:|---:|---:|---:|
| 40 | \(3.23935\times10^{-4}\) | 1.27092 | 0.61978 | 0.66086 | 0.83990 |
| 80 | \(3.25071\times10^{-4}\) | 1.26808 | 0.62318 | 0.66492 | 0.84317 |
| 120 | \(3.24965\times10^{-4}\) | 1.26893 | 0.62389 | 0.66554 | 0.84453 |

Relative to radial order 120:

- radial order 40 differs by \(-0.317\%\) in baseline \(P_{\rm esc}\), \(-0.659\%\) in the fixed-source escape ratio, and \(+0.157\%\) in the B.1 source ratio;
- radial order 80 differs by \(+0.0326\%\), \(-0.114\%\), and \(-0.0670\%\), respectively.

The 80-to-120 change is below 0.12% for the fixed-source escape ratio. The 40-node result is already within 0.66%, but radial order 120 is adopted for the quoted converged diagnostic.

## 3. Source normalization changes by emission radius

At radial order 120, the B.1 source changes are:

| Emission-radius interval | Ferreira / Caputo B.1 source ratio |
|---|---:|
| 8--10 km | 1.5328 |
| 10--12 km | 1.1917 |
| 12--15 km | 1.0471 |
| Total 8--15 km plus all other radii | 1.2689 |

The dominant 8--10 km source contribution increases by about 53%, and the 10--12 km contribution increases by about 19%. The 12--15 km contribution changes by only about 4.7%.

This is why the 12--15 km-only substitution was insufficient to represent the full same-model curve discrepancy.

## 4. Optical-depth change by path shell

All shell optical depths below are weighted with the same baseline B.1 source, so the comparison isolates the opacity change.

| Path shell | Baseline \(\langle\tau/g^2\rangle\) | Ferreira diagnostic \(\langle\tau/g^2\rangle\) | Ratio |
|---|---:|---:|---:|
| 8--10 km | \(9.6510\times10^{14}\) | \(1.4447\times10^{15}\) | 1.4970 |
| 10--12 km | \(9.8393\times10^{14}\) | \(1.1636\times10^{15}\) | 1.1826 |
| 12--15 km | \(1.3446\times10^{15}\) | \(1.3952\times10^{15}\) | 1.0376 |

The change is entirely in the Compton channel because only \(\mu_\mu\) is replaced. The neutrino inverse-decay columns remain fixed. The dominant opacity increase is in 8--10 km, where the Compton contribution is already comparable to the neutrino inverse-decay contribution.

## 5. What the transport comparison does and does not establish

At radial order 120:

\[
\frac{P_{\rm esc}^{\rm B2,\ fixed\ source}}
     {P_{\rm esc}^{\rm baseline}}
=0.62389,
\]

while the previously identified Fig. 7 target is approximately

\[
\frac{P_{\rm esc}^{\rm required}}
     {P_{\rm esc}^{\rm baseline}}
\simeq0.520.
\]

Thus the alternative published \(\mu_\mu\) curve moves the fixed-source escape probability substantially in the required direction, but the result remains about 20% above the target.

The B.1 source itself rises by 26.9%. When the source change is included, the source-weighted escape ratio is 0.66554 and the escaped B.1 integral ratio is 0.84453. The net escaped source integral therefore decreases by only about 15.5%, despite the substantial opacity increase.

These are distinct comparisons:

- fixed-source \(P_{\rm esc}\) isolates the opacity/transport change;
- own-source \(P_{\rm esc}\) includes the changed source weighting;
- escaped B.1 integral includes both source normalization and escape probability.

They must not be conflated or replaced by a common rescaling.

## 6. Decision

1. The 8--15 km \(\mu_\mu\) discrepancy is numerically important for the B.1+B.2 strong-endpoint calculation.
2. The 8--15 km diagnostic is radially converged at better than 0.12% between radial orders 80 and 120 for the fixed-source escape ratio.
3. The alternative curve does not fully close the Fig. 7 mismatch and is not adopted as the physical baseline.
4. Do not update the vector benchmark, Fig. 7 normalization, or axial-vector curve on the basis of this diagnostic alone.
5. Resolve the source discrepancy before deciding which profile represents the actual Bollig SFHo-18.8 snapshot.

## 7. Reproducibility

- Driver: audit_profile_radial_convergence.py
- Input profile: data/sfho188_digitized.csv
- Output: outputs/profile_radial_convergence_8_15km_2026-11-09.json
- Full variant scan: audit_profile_transport_sensitivity.py
- Workflow: .github/workflows/profile-12-15km-audit.yml

No raw Garching profile data are used. The calculation uses the two published figure reconstructions and preserves their unresolved discrepancy.
