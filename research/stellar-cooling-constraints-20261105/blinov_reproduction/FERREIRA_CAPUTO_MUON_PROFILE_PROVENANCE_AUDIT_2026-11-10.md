# Caputo--Ferreira muon chemical-potential provenance audit

Date: 2026-11-10  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`  
Machine-readable result: [caputo_ferreira_mu_mu_5_15km_2026-11-10.json](outputs/caputo_ferreira_mu_mu_5_15km_2026-11-10.json)  
Reproduction script: [audit_caputo_ferreira_muon_profile_comparison.py](audit_caputo_ferreira_muon_profile_comparison.py)

## Executive finding

The large difference between the Caputo and Ferreira (mu_\mu) curves is **not a temperature-profile difference, a sign convention, or a constant muon-rest-mass offset**.

The two papers both identify the relevant model as SFHo-18.8 at (t=1\) s post-bounce, and the Ferreira paper explicitly defines its Fermi distribution with (mu>0) for negatively charged leptons. However, its digitized (mu_\mu/T) profile differs strongly from the Caputo reconstruction in the most relevant inner region.

The original Bollig Fig. 4 comparison already selects Caputo over Ferreira in the 12--15 km shell. Extending the Caputo--Ferreira comparison over the full 5--15 km interval shows that the discrepancy becomes substantially larger inside 8 km. The Caputo profile therefore remains the working baseline for the original Bollig SFHo-18.8 comparison; the Ferreira curve remains an off-baseline published-profile diagnostic.

## 1. Identify the correct Ferreira source

The curve previously called the “Ferreira profile” is from:

R. Z. Ferreira, M. C. D. Marsh, and E. Ravensburg, *ALP couplings to muons and electrons: A comprehensive analysis of supernova bounds*, arXiv:2510.14469v1 (16 October 2025), published in *Physics of the Dark Universe* **53** (2026) 102435.

It is not the earlier Ferreira et al. paper arXiv:2205.07896.

The 2510.14469v1 paper:
- labels the orange dashed curve in Fig. 1 as the SFHo-18.8 model;
- states that Fig. 1 is a snapshot at (t=1\) s post-bounce;
- identifies SFHo-18.8 as the Prometheus-Vertex model of Bollig et al., Ref. [18];
- defines (f_F^\pm(E)=1/[\exp((E\pm\mu)/T)+1]), with (mu>0) for negatively charged leptons.

Thus the published model label, snapshot time, and sign convention are not obvious explanations for the difference.

## 2. Full 5--15 km comparison

The comparison uses all 533 nodes of the existing 1687-row reconstructed profile CSV satisfying (5\le r\le15\) km. Define
$$
\eta_\mu(r)=\frac{\mu_\mu(r)}{T(r)}.
$$

| Statistic | Result |
|---|---:|
| Unweighted node mean relative difference in $\eta_\mu$ | 82.98% |
| Radius-weighted trapezoid mean relative difference in $\eta_\mu$ | 77.26% |
| Median node relative difference in $\eta_\mu$ | 52.67% |
| Maximum node relative difference in $\eta_\mu$ | 315.59% |
| Minimum Ferreira/Caputo $\eta_\mu$ ratio | 1.094 |
| Maximum Ferreira/Caputo $\eta_\mu$ ratio | 4.156 |
| Unweighted node mean relative difference in $T(r)$ | 0.0144% |
| Radius-weighted trapezoid mean relative difference in $T(r)$ | 0.0168% |
| Maximum node relative difference in $T(r)$ | 0.1263% |

The temperature curves are nearly identical. The large discrepancy is specifically in the chemical-potential curve. The 77.26% radial-weighted mean is obtained by trapezoidal integration over 5--15 km; the 82.98% node mean is an unweighted diagnostic and should not be interpreted as a radial average.

### Representative points

| (r) (km) | Caputo (mu_\mu/T) | Ferreira (mu_\mu/T) | Ferreira / Caputo |
|---:|---:|---:|---:|
| 5 | 2.214 | 9.200 | 4.156 |
| 8 | 2.363 | 4.310 | 1.824 |
| 10 | 3.031 | 3.867 | 1.276 |
| 12 | 3.608 | 4.227 | 1.172 |
| 12.5 | 3.778 | 4.353 | 1.152 |
| 13 | 3.952 | 4.491 | 1.137 |
| 14 | 4.340 | 4.815 | 1.110 |
| 15 | 4.707 | 5.184 | 1.101 |

The Ferreira profile is most discrepant at 5--8 km, which lies inside the 5--15 km region that Bollig et al. identify as the high-muon-density and axion-production region.

## 3. The difference is not a rest-mass convention

A constant additive shift by (m_\mu=105.658\) MeV would require (mu_{\mu,F}-mu_{\mu,C}) to be approximately radius-independent.

It is not:
- at 5 km, (Delta\mu_\mu=177.18\) MeV;
- at 8 km, (Delta\mu_\mu=75.61\) MeV;
- at 10 km, (Delta\mu_\mu=28.29\) MeV;
- at 15 km, (Delta\mu_\mu=6.37\) MeV.

Subtracting one muon rest mass does not reconcile the profiles; the residual changes sign between 5 and 8 km. The discrepancy is therefore not a simple (mu_\mu	o\mu_\mu-m_\mu) convention conversion.

The Ferreira paper's Eq. (5) also uses the standard total-energy Fermi-Dirac distribution and the positive chemical-potential convention for negatively charged leptons. A sign flip is not indicated.

## 4. Direct comparison with the original Bollig Fig. 4

Bollig et al. arXiv:2005.07141v7 Fig. 4 plots (mu_\mu/T) for the four simulation profiles and explicitly identifies (5\lesssim r\lesssim15\) km as the region of high muon density.

The already completed direct vector comparison in the 12--15 km shell gives:

| Reconstruction | Mean absolute relative difference from Bollig Fig. 4 | Maximum |
|---|---:|---:|
| Caputo | 0.00518% | 0.01434% |
| Ferreira | 12.74% | 17.18% |

The Caputo reconstruction reproduces the original Bollig degeneracy curve essentially at the digitization precision. The Ferreira reconstruction does not. The present full-5--15 km comparison quantifies how much larger the Caputo--Ferreira disagreement becomes in the inner 5--8 km region; it is not presented as a new exact Bollig vector residual over that entire interval.

The separate B.17 consistency audit also finds that the Caputo-derived Fermi-integrated (n_\mu) agrees with Caputo's plotted muon density at the 0.5--1.1% level. This supports the Caputo (T,\mu_\mu) pair as a self-consistent thermodynamic reconstruction.

## 5. Consequence for the 10 MeV B.1+B.2 baseline

1. Keep Caputo (T(r),\mu_\mu(r)), and the existing Caputo (mu_{\nu_\mu}(r)) reconstruction as the baseline for the Bollig SFHo-18.8, 1 s comparison.
2. Keep the Ferreira profile only as a distinct published-profile sensitivity diagnostic.
3. Do not average the two (mu_\mu) curves or treat them as equally plausible reconstructions of the same Bollig snapshot.
4. Do not apply a constant rest-mass shift, a sign flip, or a radial rescaling to force agreement.
5. Do not change the B.1 source, B.2 opacity, pure-vector Fig. 7 result, or axial-vector cooling curve.

The remaining profile limitation is the absence of the exact same-snapshot Garching thermodynamic table in the current public working environment. The comparison identifies which published digitization is consistent with the original Bollig Fig. 4; it does not certify every raw radial profile variable.

## 6. Reproducibility

- Input: `data/sfho188_digitized.csv`
- Input SHA-256: `e41df78c8035540760fbcb7ef592cd830171822e`
- Reproduction script: `audit_caputo_ferreira_muon_profile_comparison.py`
- Machine-readable result: `outputs/caputo_ferreira_mu_mu_5_15km_2026-11-10.json`
- Original Bollig 12--15 km check: `BOLLIG_ORIGINAL_FIG4_MUON_DEGENERACY_CROSSCHECK_2026-11-09.md`
- B.17 density check: `BOLLIG_MUON_DENSITY_AND_B1_SOURCE_AUDIT_2026-11-09.md`

This is a profile-provenance audit only. No production, opacity, transport, luminosity, or axial-vector output is modified.
