# Low-mass vector B.13 versus B.14--B.16 benchmark scan

**Date:** 2026-11-08  
**Status:** Numerical scan completed; all CI tests passed.  
**Scope:** Pure-vector local semi-Compton rates at \(m_V=0.1,0.3,1,3\) MeV, with the validated \(10\) MeV result reused as a reference, at \(r=0\) and \(12.5\) km in the reconstructed SFHo-18.8 \(t_{\rm pb}=1\) s profile. This is not a radial luminosity or transport calculation.

## 1. Reproducibility and provenance

- Scan driver: [b13_b16_mass_scan.py](b13_b16_mass_scan.py)
- Tests: [test_b13_b16_mass_scan.py](test_b13_b16_mass_scan.py)
- Machine-readable output: [b13_b16_low_mass_scan_2026-11-08.json](outputs/b13_b16_low_mass_scan_2026-11-08.json)
- Existing 10 MeV reference: [b13_b16_comparison_2026-11-08.json](outputs/b13_b16_comparison_2026-11-08.json)
- Successful CI run: [Run #42435752134](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42435752134)
- CI result: all 40 unit tests passed; thermal-response scan, 10 MeV reference scan, and the new low-mass scan completed; all numerical outputs were archived.
- Code-execution commit: 03b36b7b4bad9dade53fe2596511c3eda1aed26c
- Low-mass JSON blob SHA: 998cbf994c1aae92d93c72f5fdeb1282a7b10a41
- Scan-script SHA-256: 441f0ab77c7b3843cdba0eae5e8da9e11e34887f9c0be1ffab7d7e691020358c
- Existing comparison-kernel script SHA-256: 35aa434145b0ad224d2cd61033c7aea8f26732282801440c23f406cf77fdfc34
- Moving-muon kernel SHA-256: 44bc670fd9384f34de56fbecb5371bae18c93c2292aa67e98f4ee304433dbaea
- rates.py SHA-256: 2fc7bc2d3b0d7b98c191755cd2bb87944e4ebe259adc3d3bbc8e0f60dcc57f56
- SFHo-18.8 profile SHA-256: 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9

The 10 MeV result is reused without recomputing its collision integrals; its original run and source-code provenance are retained in the JSON. All rates are normalized per \(g_X^2\), with \(g_X=1\).

## 2. What the paper's low-mass statement does and does not imply

The reference is N. Blinov et al., *\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae*, arXiv:2511.09619, JHEP 06 (2026) 155, Appendix B, Eqs. (B.13)--(B.19). The original Appendix B states that the semi-Compton rate is usually evaluated in the nonrelativistic-muon limit while neglecting muon recoil; it then notes that the explicit \(\mathcal O(m_V^2/\omega^2)\) term in the B.14 parenthesis is typically dropped because the process is relevant for \(m_V\lesssim\mathrm{MeV}\). See [the paper, Appendix B](https://arxiv.org/abs/2511.09619) and [the PDF, Eqs. (B.13)--(B.19)](https://cds.cern.ch/record/2948853/files/2511.09619.pdf).

These are distinct statements:

1. \(m_V\lesssim\mathrm{MeV}\) makes the explicit \(m_V^2/(2\omega^2)\) correction small for characteristic supernova photon energies.
2. It does **not** by itself make the thermal muons nonrelativistic.
3. It does **not** by itself justify neglecting muon recoil.

The scan therefore compares three prescriptions rather than assuming that the low-mass condition makes them identical:

- exact moving-muon B.13, with the full vector matrix element, all three \(V\) polarizations, exact recoil, Fermi blocking, and Bose occupation;
- the existing stationary-target exact-recoil kernel, multiplied by the same B.17 susceptibility;
- the spin-summed vector B.14--B.16 approximation, both with and without the explicit parenthesis correction.

The B.14--B.16 expression is compared only with the pure-vector B.13 result. No B.14 vector formula is assigned to an axial current.

## 3. Local thermodynamic inputs

| \(r\) (km) | \(T\) (MeV) | \(\mu_\mu\) (MeV) | \(\mu_{\nu_\mu}\) (MeV) | lapse \(N\) | \(T/m_\mu\) |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 19.26522111 | 46.67432845 | -58.61375672 | 0.7363304267 | 0.18234 |
| 12.5 | 23.88195915 | 90.21658531 | -2.591655499 | 0.8388424539 | 0.22603 |

The B.17 susceptibility is
\[
\chi_\mu\equiv n_\mu F_{\rm deg}
=\sum_{q=\mu^-,\mu^+}\int\frac{2d^3p}{(2\pi)^3}f_q(1-f_q).
\]

| \(r\) (km) | \(n_{\mu^-}\) | \(n_{\mu^+}\) | \(\chi_{\mu^-}\) | \(\chi_{\mu^+}\) | \(\chi_{\rm total}\) |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 736.1473 | 5.8702 | 726.0016 | 5.8695 | 731.8711 |
| 12.5 | 10812.1510 | 6.4546 | 9586.0644 | 6.4541 | 9592.5185 |

Densities and susceptibilities are in MeV\(^3\). The positive-muon contribution to \(\chi_{\rm total}\) is 0.802% at the center and 0.0673% at 12.5 km. It is retained in the principal B.13 and B.16 comparison. The charge-resolved B.13 output is also stored, so the single-\(\mu^-\) convention in Eq. (B.17) can be compared separately; using only \(\mu^-\) changes the quoted B.13/B.16 ratios by less than the displayed precision.

## 4. B.17-weighted muon kinematics

The nonrelativistic assumption is checked directly using the same \(f_\mu(1-f_\mu)\) susceptibility weight that enters B.17. The following are moments of the local thermal muon distribution, not a sharp definition of a nonrelativistic domain.

| \(r\) (km) | \(\sqrt{\langle v_\mu^2\rangle}\) | \(\langle p_\mu/m_\mu\rangle\) | \(\langle K_\mu/m_\mu\rangle\) | fraction \(p/m_\mu<0.3\) | fraction \(p/m_\mu<0.5\) |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.6174 | 0.8285 | 0.3306 | 5.28% | 21.22% |
| 12.5 | 0.6903 | 1.0369 | 0.4744 | 2.26% | 10.12% |

The B.17-weighted muons are not parametrically nonrelativistic in either region. This is particularly clear at 12.5 km, where the mean \(p_\mu/m_\mu\) is about 1.04 and only 2.26% of the susceptibility weight has \(p_\mu/m_\mu<0.3\).

Consequently, the condition \(m_V\lesssim\mathrm{MeV}\) does not establish the nonrelativistic-muon approximation. The direct B.13/B.16 comparison below is needed.

## 5. Energy-integrated emissivities

The emissivities are in MeV\(^5\) per \(g_X^2\). The 10 MeV row is reused from the already validated local comparison; 0.1, 0.3, 1, and 3 MeV are newly evaluated.

| \(m_V\) (MeV) | \(r\) (km) | \(Q_{\rm B13}^{\rm moving}\) | \(Q_{\rm stationary}^{\rm recoil}\) | \(Q_{\rm B16}^{\rm no\ recoil}\) | B.13/B.16 \(-1\) | B.13/stationary \(-1\) |
|---:|---:|---:|---:|---:|---:|---:|
| 0.1 | 0.0 | 13.91679 | 16.45409 | 28.90715 | -51.857% | -15.420% |
| 0.1 | 12.5 | 384.82746 | 479.67657 | 894.72000 | -56.989% | -19.774% |
| 0.3 | 0.0 | 13.91678 | 16.45417 | 28.90714 | -51.857% | -15.421% |
| 0.3 | 12.5 | 384.82693 | 479.67825 | 894.71980 | -56.989% | -19.774% |
| 1.0 | 0.0 | 13.91666 | 16.45478 | 28.90669 | -51.857% | -15.425% |
| 1.0 | 12.5 | 384.82297 | 479.69232 | 894.71249 | -56.989% | -19.777% |
| 3.0 | 0.0 | 13.91015 | 16.45324 | 28.89594 | -51.861% | -15.456% |
| 3.0 | 12.5 | 384.71057 | 479.69888 | 894.53304 | -56.993% | -19.802% |
| 10.0* | 0.0 | 13.69748 | 16.25559 | 28.59162 | -52.093% | -15.737% |
| 10.0* | 12.5 | 381.11350 | 476.51496 | 889.21854 | -57.141% | -20.021% |

(*) Reused reference, not recomputed in this scan.

The central result is that the B.13/B.16 difference is almost independent of \(m_V\) over 0.1--3 MeV. Moving from 0.1 to 1 MeV changes the B.13/B.16 ratio by less than 0.01 percentage point. Thus the large difference is not driven by the explicit \(m_V^2/(2\omega^2)\) term.

The stationary exact-recoil comparator is 43.1% below B.16 at the center and 46.4% below at 12.5 km. Replacing the stationary target by the moving thermal-muon calculation lowers the rate by a further 15.4% and 19.8%, respectively, relative to the stationary exact-recoil result. These comparisons separate the no-recoil approximation from the additional effect of thermal target motion within the present implementation.

## 6. Size of the explicit \(m_V^2/(2\omega^2)\) correction

The table gives the increase in the **energy-integrated B.16 emissivity** when the parenthesis correction is retained.

| \(m_V\) (MeV) | \(r=0\) | \(r=12.5\) km |
|---:|---:|---:|
| 0.1 | 0.00034% | 0.00022% |
| 0.3 | 0.00303% | 0.00197% |
| 1.0 | 0.03252% | 0.02136% |
| 3.0 | 0.26715% | 0.17841% |
| 10.0* | 2.22812% | 1.56299% |

For the paper's \(m_V\lesssim\mathrm{MeV}\) regime, dropping this term is numerically very safe at the two selected profile points. The correction remains below 0.04% at 1 MeV. Even at 3 MeV it is below 0.27%.

This confirms the limited role of the mass correction, but does not validate the independent nonrelativistic and no-recoil approximations.

## 7. Fixed-energy cross-check

At \(m_V=0.1\) MeV, the ratio of the exact moving-muon B.13 vector rate to B.16 at fixed emitted-vector energy is:

| \(r\) (km) | \(\omega=15\) MeV | \(\omega=30\) MeV | \(\omega=50\) MeV |
|---:|---:|---:|---:|
| 0.0 | 0.6801 | 0.6138 | 0.5324 |
| 12.5 | 0.6077 | 0.5570 | 0.4982 |

The 0.3 and 1 MeV ratios are numerically almost identical. At 1 MeV, the corresponding ratios are 0.6802, 0.6138, 0.5324 at the center and 0.6077, 0.5570, 0.4982 at 12.5 km. This energy dependence shows why a single overall normalization factor cannot represent the difference between the exact moving-target kernel and B.16.

At \(\omega=30\) MeV and \(m_V=0.1\) MeV, the B.13 vector mode rates (in MeV per \(g_X^2\)) are:

| \(r\) (km) | \(\Gamma_L\) | \(\Gamma_+\) | \(\Gamma_-\) |
|---:|---:|---:|---:|
| 0.0 | \(8.11\times10^{-10}\) | \(5.2264\times10^{-5}\) | \(5.2264\times10^{-5}\) |
| 12.5 | \(1.56\times10^{-8}\) | \(9.2684\times10^{-4}\) | \(9.2684\times10^{-4}\) |

The longitudinal vector mode is suppressed in the low-mass limit, as expected for a conserved vector current. B.16 is intrinsically spin summed; any \(L,+,-\) split of B.16 is only the diagnostic no-recoil limiting decomposition, not three independent published B.16 formulae.

## 8. Numerical convergence

Maximum relative changes across all newly computed masses and both radii are:

| Check | Maximum absolute relative change |
|---|---:|
| B.13 energy order 12 \(\to\) 16 | 0.0223% |
| B.13 inner orders \((12,8,8,8)\to(16,10,10,10)\) | 0.0160% |
| B.16 energy order 64 \(\to\) 96 | \(2.0\times10^{-13}\%\) |
| Stationary exact-recoil angular order 64 \(\to\) 128 | \(6.7\times10^{-13}\%\) |
| B.13 detailed-balance residual | \(3.7\times10^{-15}\) |
| Final-muon on-shell residual | \(1.7\times10^{-13}\) |

The quadrature changes are much smaller than the 15--20% moving-target effect and the 43--46% difference between B.16 and the stationary exact-recoil comparator.

## 9. Interpretation and decisions

1. **The low-mass condition does what the paper says it does:** for \(m_V\leq1\) MeV, the explicit \(m_V^2/(2\omega^2)\) correction to the integrated B.16 rate is below 0.04% at both radii. It can safely be dropped for these local benchmarks.
2. **It does not make the muons nonrelativistic.** The B.17-weighted RMS velocities are 0.62 and 0.69, and the fractions with \(p/m_\mu<0.3\) are only 5.28% and 2.26%.
3. **It does not make recoil negligible.** The stationary exact-recoil comparator is substantially below B.16, and the exact moving-muon B.13 result is lower still.
4. **The exact B.13/B.16 difference remains approximately 52--57% throughout 0.1--3 MeV.** It is therefore not a finite-\(m_V\) correction effect. It is associated with the nonrelativistic/no-recoil approximation and thermal target motion.
5. **Do not force B.13 to match B.16 by rescaling.** For reproducing the published Blinov vector benchmark, B.14--B.16 is the paper's prescribed approximate rate and should be implemented as such. B.13 is the more complete moving-muon collision integral and provides a separate estimate of corrections beyond that approximation. Agreement of the B.16 local kernel alone is not yet a reproduction of Fig. 7; the same profile, radial integral, lapse, opacity, and transport prescription still need to be checked.
6. Keep the pure-vector literature-reproduction gate separate from the axial calculation. Once the vector B.16 implementation and its global transport result are independently checked against Fig. 7, the B.13 framework can be used for the model-specific axial calculation without importing a vector rescaling.
7. No coupling, production rate, opacity, stellar profile, or transport result is rescaled. No result from this scan is imported into PR #56. No manuscript or referee-response file is modified.
