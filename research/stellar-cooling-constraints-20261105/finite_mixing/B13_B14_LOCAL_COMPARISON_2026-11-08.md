# Exact moving-muon B.13 versus B.14--B.16 local comparison

> **Convention clarification added 2026-11-09:** this historical local comparison evaluates the B.16 susceptibility with both \(\mu^-\) and \(\mu^+\) contributions. The subsequent audit of Blinov Eq. (B.17) establishes that the published \(n_\mu F_{\rm deg}\) convention is the single negative-muon distribution, not the sum of both charges. Therefore the charge-summed B.13/B.16 ratios below are a two-charge extension, not the final like-for-like B.17 comparison. The current global audit reports both cases separately; use its \(\mu^-\)-only result for the B.17-matched comparison and its \(\mu^-+\mu^+\) result for the charge-summed extension. Historical numbers in this file are retained as originally computed and must not be mixed with the single-species global baseline.


**Date:** 2026-11-08  
**Status:** Numerical run complete; local interpretation recorded.  
**Scope:** \(m_V=10\) MeV at \(r=0\) and \(12.5\) km in the reconstructed SFHo-18.8 profile. This is a local source audit, not a stellar transport or luminosity calculation.

## 1. Reproducibility record

- Driver: [b13_b16_comparison.py](b13_b16_comparison.py)
- Regression tests: [test_b13_b16_comparison.py](test_b13_b16_comparison.py)
- Machine-readable output: [outputs/b13_b16_comparison_2026-11-08.json](outputs/b13_b16_comparison_2026-11-08.json)
- Successful workflow: [Run #42434369283](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42434369283)
- Workflow result: all 36 unit tests passed; the thermal response scan and the B.13--B.16 comparison both completed; the JSON output was committed to this branch.
- Run-triggering commit: d619cd3f0f61dd363e4e5c2c0d98159a2051cd85
- JSON blob SHA: b7bea597e17a9b3377c31e9eacb2e1f320d7441c
- Code SHA-256:
  - b13_b16_comparison.py: 35aa434145b0ad224d2cd61033c7aea8f26732282801440c23f406cf77fdfc34
  - moving_muon_compton.py: 44bc670fd9384f34de56fbecb5371bae18c93c2292aa67e98f4ee304433dbaea
  - rates.py: 2fc7bc2d3b0d7b98c191755cd2bb87944e4ebe259adc3d3bbc8e0f60dcc57f56
  - SFHo-18.8 profile: 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9

All rates and emissivities are normalized per \(g_X^2\), with \(g_X=1\) in the numerical output. The local energy is used in the collision integrals. The lapse is recorded as profile metadata; no redshift or radial transport is applied here.

## 2. Comparison convention

The exact B.13 calculation evaluates the moving-muon \(2\to2\) collision integral, with the initial and final muon distributions, final-state Pauli blocking, photon Bose occupation, exact recoil, and all three physical \(V\) polarizations. The \(\mu^-\) and \(\mu^+\) distributions are evaluated separately, with chemical potentials \(+\mu_\mu\) and \(-\mu_\mu\), then summed.

The published B.14--B.16 approximation is a **vector-current, spin-summed, nonrelativistic-muon/no-recoil** expression. It is compared only to the pure-vector B.13 calculation. It is not assigned to the axial or UV mixed-current rates.

For \(g_X=1\), \(\alpha_V=1/(4\pi)\), the B.14 cross section is implemented as
\[
\sigma_{\mu\gamma\to\mu V}
=\frac{8\pi\alpha\alpha_V}{3m_\mu^2}
\left(1+\frac{m_V^2}{2\omega^2}\right)v_V,
\qquad
v_V=\sqrt{1-\frac{m_V^2}{\omega^2}}.
\]
The B.16 rate is
\[
\Gamma_{\rm B16}
=\frac{n_\mu F_{\rm deg}}{v_V}
\frac{2}{e^{\omega/T}-1}
\sigma_{\mu\gamma\to\mu V}.
\]
Thus the \(v_V\) in the cross section cancels the \(1/v_V\) in B.16. The factor 2 restores the photon polarization sum absent from the unpolarized cross-section definition.

For diagnostic purposes, the B.14 no-recoil polarization sum is represented by the limiting weights
\[
(L,+,-)\ \propto\
\left(\frac{m_V^2}{\omega^2},\,1,\,1\right).
\]
This is a decomposition of the no-recoil limit; the published B.14 cross section itself is polarization summed.

The energy-integrated local emissivity uses
\[
Q=\int_{m_V}^{\infty}
\frac{d\omega}{2\pi^2}\,
\omega^2\sqrt{\omega^2-m_V^2}\,
\Gamma_{\rm prod}(\omega).
\]

## 3. Local thermodynamic inputs

| \(r\) (km) | \(T\) (MeV) | \(\mu_\mu\) (MeV) | \(\mu_{\nu_\mu}\) (MeV) | lapse \(N\) |
|---:|---:|---:|---:|---:|
| 0.0 | 19.26522111 | 46.67432845 | -58.61375672 | 0.7363304267 |
| 12.5 | 23.88195915 | 90.21658531 | -2.591655499 | 0.8388424539 |

The B.17 factor is evaluated as
\[
n_\mu F_{\rm deg}
=\sum_{q=\mu^-,\mu^+}
\int\frac{2d^3p}{(2\pi)^3}f_q(1-f_q).
\]
The two charge species are also reported separately.

| \(r\) (km) | \(n_{\mu^-}\) | \(n_{\mu^+}\) | \(F_{\rm deg}^{\mu^-}\) | \(F_{\rm deg}^{\mu^+}\) | \(\sum_q n_qF_{\rm deg}^q\) |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 736.1473 | 5.8702 | 0.986218 | 0.999888 | 731.8711 |
| 12.5 | 10812.1510 | 6.4546 | 0.886601 | 0.999919 | 9592.5185 |

Densities and susceptibilities are in MeV\(^3\). The \(\mu^+\) share of the total susceptibility is 0.802% at the center and 0.0673% at 12.5 km. It is small but retained consistently in both B.13 and B.16 comparisons.

## 4. Exact B.13 mode-resolved emissivities

The following are energy-integrated local emissivities in MeV\(^5\), in the order \((L,+,-)\).

| \(r\) (km) | Current | \(Q_L\) | \(Q_+\) | \(Q_-\) | \(Q_{\rm total}\) |
|---:|---|---:|---:|---:|---:|
| 0.0 | Vector | 0.469673 | 6.613906 | 6.613906 | 13.697485 |
| 0.0 | Axial | 441.334511 | 16.064662 | 16.064662 | 473.463834 |
| 0.0 | UV, \(\theta_{\mu R}=10^{-2}\) | 441.246251 | 16.062078 | 16.060820 | 473.369149 |
| 12.5 | Vector | 9.934298 | 185.589599 | 185.589599 | 381.113496 |
| 12.5 | Axial | 15600.631485 | 429.520109 | 429.520109 | 16459.671703 |
| 12.5 | UV, \(\theta_{\mu R}=10^{-2}\) | 15597.511620 | 429.454183 | 429.414244 | 16456.380047 |

The UV benchmark is essentially axial at this precision. Its total B.13 emissivity differs from the pure-axial result by about \(-0.0200\%\) at both radii. The vector and axial responses are manifestly not related by a common polarization-independent normalization: the axial response is strongly longitudinal, while the vector response is dominated by the two transverse modes.

### Fixed-energy mode-resolved rates at \(\omega=30\) MeV

These are differential production rates in MeV per \(g_X^2\), at the same local thermodynamic points. They make the polarization comparison explicit before the energy integration.

| \(r\) (km) | Current | \(\Gamma_L\) | \(\Gamma_+\) | \(\Gamma_-\) | Total |
|---:|---|---:|---:|---:|---:|
| 0.0 | B.13 vector | \(7.5632\times10^{-6}\) | \(5.1440\times10^{-5}\) | \(5.1440\times10^{-5}\) | \(1.1044\times10^{-4}\) |
| 0.0 | B.13 axial | \(1.43343\times10^{-3}\) | \(1.45854\times10^{-4}\) | \(1.45854\times10^{-4}\) | \(1.72513\times10^{-3}\) |
| 0.0 | B.13 UV | \(1.43314\times10^{-3}\) | \(1.45828\times10^{-4}\) | \(1.45822\times10^{-4}\) | \(1.72479\times10^{-3}\) |
| 12.5 | B.13 vector | \(1.41914\times10^{-4}\) | \(9.05906\times10^{-4}\) | \(9.05906\times10^{-4}\) | \(1.95373\times10^{-3}\) |
| 12.5 | B.13 axial | \(2.61174\times10^{-2}\) | \(2.61344\times10^{-3}\) | \(2.61344\times10^{-3}\) | \(3.13443\times10^{-2}\) |
| 12.5 | B.13 UV | \(2.61122\times10^{-2}\) | \(2.61298\times10^{-3}\) | \(2.61286\times10^{-3}\) | \(3.13380\times10^{-2}\) |

The corresponding B.16 vector total and its no-parenthesis-correction counterpart are:

| \(r\) (km) | B.16 \(L\) | B.16 \(+\) | B.16 \(-\) | B.16 total | No-parenthesis-correction total |
|---:|---:|---:|---:|---:|---:|
| 0.0 | \(9.46109\times10^{-6}\) | \(8.51498\times10^{-5}\) | \(8.51498\times10^{-5}\) | \(1.79761\times10^{-4}\) | \(1.70300\times10^{-4}\) |
| 12.5 | \(1.84902\times10^{-4}\) | \(1.66412\times10^{-3}\) | \(1.66412\times10^{-3}\) | \(3.51313\times10^{-3}\) | \(3.32823\times10^{-3}\) |

B.16 is intrinsically a spin-summed total. The listed \(L,+,-\) entries are the no-recoil limiting decomposition described in Section 2, not separate published B.16 formulae.

## 5. B.14--B.16 vector total and the \(m_V^2/(2\omega^2)\) term

| \(r\) (km) | \(Q_{\rm B16}\), correction retained | \(Q_{\rm B16}\), parenthesis correction dropped | Increase from retaining correction |
|---:|---:|---:|---:|
| 0.0 | 28.591623 | 27.968454 | 2.23% |
| 12.5 | 889.218541 | 875.534031 | 1.56% |

At fixed \(\omega\), the multiplicative cross-section correction is:

| \(\omega\) (MeV) | \(1+m_V^2/(2\omega^2)\) |
|---:|---:|
| 15 | 1.222222 |
| 30 | 1.055556 |
| 50 | 1.020000 |

For the pure-vector B.13 result, the ratio to the B.16 total with the correction retained is:

| \(r\) (km) | \(\omega=15\) MeV | \(\omega=30\) MeV | \(\omega=50\) MeV |
|---:|---:|---:|---:|
| 0.0 | 0.6600 | 0.6144 | 0.5335 |
| 12.5 | 0.5822 | 0.5561 | 0.4986 |

After integrating over the emitted-vector energy, B.13 vector is 52.09% below B.16 at the center and 57.14% below at 12.5 km. Dropping the explicit parenthesis correction changes these differences only to 51.03% and 56.47%, respectively.

**Interpretation:** the large B.13/B.16 difference is not caused mainly by the explicit \(m_V^2/(2\omega^2)\) term. It reflects the combined nonrelativistic-muon and no-recoil approximation in B.14. The paper states that this approximation is normally used when the process is relevant for \(m_V\lesssim\) MeV. The present \(m_V=10\) MeV benchmark is outside that stated regime. Therefore the B.13/B.16 difference is a useful approximation stress test, not a discrepancy that B.13 is required to remove at 10 MeV.

## 6. Third comparator: existing stationary-muon exact-recoil kernel

This comparator retains the existing exact two-body recoil cross section for a muon at rest, multiplied by the same B.17 susceptibility. It isolates the effect of replacing the stationary target by the moving thermal-muon integral more directly than the B.13/B.16 comparison.

| \(r\) (km) | Current | Stationary-target exact-recoil \(Q\) | Moving-muon B.13 \(Q\) | Relative change |
|---:|---|---:|---:|---:|
| 0.0 | Vector | 16.255588 | 13.697485 | -15.74% |
| 0.0 | Axial | 453.727889 | 473.463834 | +4.35% |
| 0.0 | UV, \(\theta_{\mu R}=10^{-2}\) | 453.637151 | 473.369149 | +4.35% |
| 12.5 | Vector | 476.514957 | 381.113496 | -20.02% |
| 12.5 | Axial | 16137.291804 | 16459.671703 | +2.00% |
| 12.5 | UV, \(\theta_{\mu R}=10^{-2}\) | 16134.064619 | 16456.380047 | +2.00% |

This is the relevant moving-muon correction to the existing stationary-target implementation. It is current dependent: it suppresses the vector response at these two points but modestly enhances the axial response.

## 7. Local weak-coupling source budget and the 9% question

At \(m_V=10\) MeV the dimuon channel is closed. For a local two-channel diagnostic, the neutrino source is evaluated with the unchanged \(\nu_\mu,\nu_\tau\) couplings; the \(\nu_\tau\) chemical potential is set to zero, as in the current profile convention. No radial integration, escape probability, lapse weighting, or backreaction is included.

| \(r\) (km) | \(Q_{\nu\bar\nu}\) (MeV\(^5\)) | Current | Stationary Compton share | Moving-muon Compton share | Total local thin-source change |
|---:|---:|---|---:|---:|---:|
| 0.0 | 2190.7704 | Vector | 0.737% | 0.621% | -0.116% |
| 0.0 | 2190.7704 | Axial | 17.157% | 17.771% | +0.746% |
| 0.0 | 2190.7704 | UV, \(\theta_{\mu R}=10^{-2}\) | 17.155% | 17.768% | +0.746% |
| 12.5 | 6096.3667 | Vector | 7.250% | 5.884% | -1.451% |
| 12.5 | 6096.3667 | Axial | 72.581% | 72.972% | +1.450% |
| 12.5 | 6096.3667 | UV, \(\theta_{\mu R}=10^{-2}\) | 72.577% | 72.968% | +1.450% |

The source change is defined by comparing
\[
Q_{\nu\bar\nu}+Q_{\rm Compton}^{\rm moving}
\quad\text{with}\quad
Q_{\nu\bar\nu}+Q_{\rm Compton}^{\rm stationary}.
\]

**Conclusion on the approximately 9% weak-coupling source discrepancy:** the moving-muon correction does not explain a 9% discrepancy at either diagnostic radius. For the actual axial/UV current, it changes the local two-channel source by about \(+0.75\%\) at the center and \(+1.45\%\) at 12.5 km. The vector local source changes by \(-0.12\%\) and \(-1.45\%\), respectively. These two radii do not determine the global radial weighting, but they do not support a 9% local correction.

The earlier note's 18.6% global vector semi-Compton share is superseded and must not be used. The archived B.16 global source decomposition gives a Compton fraction of 32.005% at \(m_V=10\) MeV; the current vertex-preserving profile gives 32.005% as well. The direct global B.13 calculation then finds
\[
L_{\rm thin}^{\rm B13}/L_{\rm thin}^{\rm B16}=0.78898,
\]
with the B.13 \(\mu^-\) Compton source equal to 34.07% of the B.16 Compton source after the full radial and energy weighting. Thus the exact moving-muon kernel lowers the total optically thin source by 21.10%. This result comes from the global B.1 integral, not from multiplying a global channel fraction by the two local emissivity ratios above.

The B.13 source-and-opacity replacement shifts the weak-endpoint Fig. 7 difference from \(-8.89\%\) to \(-28.11\%\). It therefore does not explain or repair the weak-source residual. The earlier 18.6% estimate is not traceable to the current archived B.16 source decomposition and is withdrawn.

## 8. Quadrature and internal-consistency checks

| Check | \(r=0\) | \(r=12.5\) km |
|---|---:|---:|
| B.13 energy order 12 \(\to\) 16 | -0.00369% | -0.01298% |
| B.13 inner orders \((12,8,8,8)\to(16,10,10,10)\) | +0.01532% | +0.00359% |
| Largest one-at-a-time inner-order change at fixed \(\omega=30\) MeV | 0.02463% | 0.01879% |
| B.16 energy order 64 \(\to\) 96 | \(2.0\times10^{-13}\%\) | \(2.0\times10^{-13}\%\) |
| B.17 susceptibility order 128 \(\to\) 192 | \(-3.9\times10^{-13}\%\) | \(-4.2\times10^{-13}\%\) |
| Stationary-target angular order 64 \(\to\) 128 | \(5.6\times10^{-13}\%\) | \(6.2\times10^{-13}\%\) |

Additional maximum residuals in the B.13 calculation are:

- Mode-by-mode detailed balance: \(2.83\times10^{-15}\).
- Final-muon on-shell reconstruction: \(1.30\times10^{-13}\).

The local neutrino energy integral changes by less than \(2\times10^{-13}\%\) between energy orders 64 and 96. The four B.13 inner quadratures are also varied one at a time at fixed \(\omega=30\) MeV; their individual and combined changes are all below \(0.025\%\).

The quadrature errors are therefore much smaller than the physical differences between the B.13, stationary-target, and B.14--B.16 prescriptions.

## 9. Decisions and limits

1. Retain the exact moving-muon B.13 calculation as the local microscopic reference for the moving thermal muon gas.
2. Retain the stationary-muon exact-recoil kernel as a separate comparator; its difference from B.13 is current dependent and must not be represented by a universal rescaling.
3. Use B.14--B.16 only as the vector-current nonrelativistic/no-recoil approximation. At \(m_V=10\) MeV it is outside the mass regime stated in the paper and must not be treated as the exact B.13 target.
4. The explicit \(m_V^2/(2\omega^2)\) term changes the integrated B.16 emissivity by only 1.56--2.23% at these points. It does not account for the much larger B.13/B.16 difference.
5. The moving-muon correction to the axial/UV local total source is below 1.5% at the two tested radii. It does not by itself explain the approximately 9% weak-source discrepancy. A radial source-weighted comparison is still required.
6. Do not rescale \(g_X\), the local production rate, neutrino couplings, opacity, or the stellar profile to fit Fig. 7.
7. This report does not pass the pure-vector Fig. 7 transport gate, produce an axial exclusion curve, or validate the high-coupling transport tail.
8. No code or result from this local comparison is imported into PR #56's transport solver at this stage. No manuscript or referee-response file is modified.
