# Outer neutrino inverse-decay profile and convention audit

**Date:** 2026-11-08  
**Status:** The public-profile chemical-potential uncertainty is too small to explain the high-coupling Fig. 7 residual; outer-shell inverse-decay opacity is physically important and numerically converged. The exact raw \\(\\nu_\\tau\\) profile is not independently available from the public Caputo figure.  
**Scope:** Blinov et al., arXiv:2511.09619v2, 10 MeV pure-vector reproduction, at the high-absorption coupling \\(g=4.1716896502\\times10^{-8}\\). No opacity rescaling, profile fit, or replacement profile is adopted.

## 1. Public profile and flavor inputs

The Caputo SFHo-18.8, 1 s post-bounce Fig. 1 digitization contains one muon-neutrino chemical-potential curve, \\(\\mu_{\\nu_\\mu}(r)\\), but no separately plotted \\(\\mu_{\\nu_\\tau}(r)\\). The current baseline therefore uses the digitized \\(\\mu_{\\nu_\\mu}\\) and sets \\(\\mu_{\\nu_\\tau}=0\\). This is an explicit modeling assumption, not a direct extraction of a tau-neutrino profile from the figure.

The signed \\(\\mu_{\\nu_\\mu}\\) reconstruction has a negative branch through 13.11 km and a positive branch from 16.59 to 18.42 km; the public logarithmic plot does not resolve \\( |\\mu_{\\nu_\\mu}|<1\\) MeV in the intervening and outer regions. Those unresolved intervals are zero-filled in the baseline. The sign reversal itself does not alter the isotropic flavor-summed inverse-decay kernel: changing \\(\\mu_\\nu\\to-\\mu_\\nu\\) is equivalent to exchanging the neutrino and antineutrino energies and reversing the angular integration variable. It can exchange the two circular-polarization labels in a mode-resolved convention, but the polarization-summed rate is invariant. A regression test of the evenness of \\(I(\\mu_\\nu/T,\\omega/T,v)\\) passes.

The Garching archive documents that some source archives are password protected. We do not request or access restricted simulation tables; this audit uses only public published-figure reconstructions. Consequently, the exact underlying \\(\\nu_\\tau\\) chemical-potential profile remains unavailable to this calculation.

## 2. Sensitivity to the unresolved outer chemical potentials

The luminosity is recomputed self-consistently, changing the same flavor chemical potential in both inverse-decay production and absorption. These are constant outer-shell stress tests for \\(r\\ge15\\) km, not alternative physical profiles.

### Muon-neutrino tail

| Outer \\(\\mu_{\\nu_\\mu}\\) | Luminosity change |
|---:|---:|
| Baseline digitized profile | 0 |
| 0 MeV | -0.0128% |
| 1 MeV | +0.0274% |
| 2 MeV | +0.1470% |

Thus the unresolved \\(\\nu_\\mu\\) tail below a few MeV is negligible for the 10 MeV high-absorption luminosity in this benchmark.

### Tau-neutrino baseline stress test

| Constant outer \\(\\mu_{\\nu_\\tau}\\), \\(r\\ge15\\) km | Luminosity change |
|---:|---:|
| 0 MeV (baseline) | 0 |
| 1 MeV | +0.0517% |
| 2 MeV | +0.2057% |
| 5 MeV | +1.2416% |
| 10 MeV | +4.4865% |

A hypothetical 10 MeV outer tau-neutrino chemical potential changes the result by only 4.5%; 1--2 MeV changes it by less than 0.21%. This is a deliberately broad stress test, not a claim that the true \\(\\mu_{\\nu_\\tau}\\) equals any of these values. The zero baseline is therefore not the dominant explanation of the +92.24% high-coupling residual, although the exact tau profile remains a source-level assumption.

## 3. Where the optical depth accumulates

At the high-absorption benchmark, the source-weighted mean optical depth from inverse neutrino decay, split by the radius of the absorbing material, is:

| Absorber shell | \\(\\nu_\\mu\\) contribution | \\(\\nu_\\tau\\) contribution | Total |
|---|---:|---:|---:|
| 0--5 km | 0.0794 | 0.1315 | 0.2109 |
| 5--10 km | 0.8279 | 0.8931 | 1.7209 |
| 10--15 km | 1.6993 | 1.7049 | 3.4042 |
| 15--20 km | 2.2405 | 2.2426 | 4.4831 |
| 20--25 km | 2.3340 | 2.3340 | 4.6680 |
| **Total** | **7.1811** | **7.3060** | **14.4871** |

The 15--25 km region contributes 63.17% of the source-weighted mean neutrino optical depth. The \\(\\nu_\\mu\\) and \\(\\nu_\\tau\\) contributions in that outer region are almost equal. The outer opacity is therefore not controlled by the unresolved \\(\\nu_\\mu\\) chemical-potential tail; it is largely the common finite-temperature inverse-decay opacity of the two neutrino flavors.

This is a source-weighted mean optical-depth decomposition, not a statement that 63.17% of the escaping luminosity is absorbed there. Escape depends exponentially on the full path-integrated optical depth and on production radius and emission direction.

## 4. Why the outer opacity does not vanish as the temperature falls

Blinov's reduced opacity is
\\[
\\Gamma_{\\rm abs}^*=(1-e^{-\\omega/T})\\Gamma_{\\rm abs}.
\\]
With detailed balance, the low-temperature limit approaches the time-dilated vacuum decay opacity rather than vanishing with the thermal neutrino density. The existing local-kernel diagnostic gives, for \\(m_V=10\\) MeV and \\(\\omega=10.1\\) MeV, the reduced opacity relative to its zero-temperature limit as 0.536 at 20 km, 0.610 at 22 km, 0.654 at 24 km, and 0.680 at 25 km. At \\(\\omega=100\\) MeV it is already 0.944--0.960 over 20--25 km.

This explains why the outer layers can contribute substantially even though the temperature has fallen to approximately 3--4 MeV and the plotted \\(\\mu_{\\nu_\\mu}\\) is unresolved there.

## 5. Numerical convergence and independent local-rate checks

For the full escape integral at this point:

| Quadrature | Relative luminosity change |
|---|---:|
| Baseline: 40 radial, 16 angular, 32 path | 0 |
| 32 angular, 64 path | +0.00336% |
| 48 angular, 96 path | +0.00468% |
| 80 radial, 32 angular, 64 path | +0.4933% |

Angular and path quadrature are well converged. Doubling radial order changes the luminosity by about 0.49%, still far below the Fig. 7 high-coupling residual.

The direct collision-integral audit has now been extended from its original 0--15 km grid to 0, 5, 8, 10, 15, 17, 18, 20, 22, 24 and 25 km. It covers 132 neutrino cases and 132 B.14 Compton cases (four masses and three \(\omega/m_V\) values at each radius). The maximum relative differences between adaptive direct neutrino production/absorption integrals and the rate implementation are \(5.24\times10^{-15}\) and \(3.99\times10^{-15}\), respectively; mode-resolved neutrino detailed balance is satisfied to \(1.24\times10^{-14}\). B.14 Compton detailed balance and the spin-summed normalization agree to \(4.17\times10^{-16}\) and \(3.94\times10^{-16}\). The local neutrino kernel is therefore independently validated numerically through 25 km on this grid. The full moving-muon B.13 thermal integral remains outside this B.14 audit.
 
The outer Compton source also becomes negligible rapidly: the independently integrated \(n_{\mu,\rm eff}\) falls from \(0.172\,\mathrm{MeV}^3\) at 17 km to \(2.03\times10^{-3}\,\mathrm{MeV}^3\) at 18 km, \(5.24\times10^{-7}\,\mathrm{MeV}^3\) at 20 km, and \(1.15\times10^{-12}\,\mathrm{MeV}^3\) at 25 km. Thus the 15--25 km opacity that controls the high-coupling tail is overwhelmingly neutrino inverse decay, not semi-Compton absorption.

## 6. Disposition and next step

1. Keep the Caputo \\(\\mu_{\\nu_\\mu}\\) profile and \\(\\mu_{\\nu_\\tau}=0\\) as the explicitly labeled baseline. Do not fit either chemical potential to Fig. 7.
2. The unresolved outer \\(\\mu_{\\nu_\\mu}\\) tail is not a plausible explanation for the large high-coupling mismatch. Even a 10 MeV stress value for \\(\\mu_{\\nu_\\tau}\\) changes the luminosity by only 4.5%.
3. The outer 15--25 km inverse-decay opacity is physically important because the reduced opacity tends toward the vacuum decay limit as \\(T\\) decreases.
4. The local neutrino collision kernel is now independently checked through 25 km. The next task is an independent implementation of the full angular/path transport integral, with the outer 15--25 km opacity resolved along rays and compared with the reference escape probability.

No formal manuscript, referee response, or axial-vector exclusion curve is modified.
