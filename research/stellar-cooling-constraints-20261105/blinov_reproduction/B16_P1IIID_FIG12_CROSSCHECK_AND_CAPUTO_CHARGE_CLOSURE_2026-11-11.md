# P1-IIId: Esseili–Kribs Fig. 12 cross-check and Caputo charge-closure audit

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Correct identification of the independent paper

The independent figure is from:

H. Esseili and G. D. Kribs, *Hiding a light vector boson from terrestrial experiments: A chargephobic dark photon*, Phys. Rev. D **114**, 016023 (2026), DOI: 10.1103/718s-7k7v, arXiv:2512.10916v3.

The v3 arXiv PDF is dated 13 June 2026; the APS article states publication on 24 July 2026. Figure 12 is on printed page 15 (PDF page index 14).

Figure 12 caption and surrounding text state:
- left panel: temperature profiles for SFHo-18.6, SFHo-18.8, SFHo-20.0, and LS220-20.0;
- right panel: particle number-density profiles in the SFHo-18.8 model;
- profiles correspond to 1 s after core collapse;
- density normalization is \(n_0=0.181\,\mathrm{fm}^{-3}\);
- the full profile data are located at the Garching Core-Collapse Supernova Archive.

The right-panel labels include neutron \(n\), proton \(p\), electron \(e\), muon \(\mu\), and neutrino species. This is therefore a useful independent figure-level source for the nucleon curves, not a raw-data release.

## 2. Temperature comparison: visual consistency only

The Caputo Fig. 1 temperature path is already digitized from the exact source PDF. Its maximum is approximately
\[
T_{\max}=39.25\ \mathrm{MeV},\qquad r_{\max}=8.48\ \mathrm{km},
\]
and its value near \(r=20\) km is approximately \(4.2\) MeV.

Visual inspection of the SFHo-18.8 (orange) curve in Esseili–Kribs Fig. 12 shows the same broad structure: a peak near \(r\simeq8\) km at about \(40\) MeV, followed by a decline to a few MeV near 20 km. This is consistent at figure-reading precision.

**No numerical point-by-point residual is claimed yet.** The APS PDF screenshot is readable for visual comparison, but the current acquisition path did not yield a local high-resolution/vector source for automated path extraction. The temperature cross-check is therefore classified as a qualitative consistency check, not a precision validation.

## 3. Garching archive access status

The archive landing page explicitly warns that some archives are password-protected and instructs users to contact the archive maintainers for access. Following the profile link exposed from the Esseili–Kribs paper currently returns HTTP 401 Unauthorized in this access path.

Consequently, no raw Garching hydro profile is claimed to have been obtained. The public Fig. 12 remains the independent figure-level source. No access key or restricted data are assumed.

## 4. New Caputo density audit: charge-closure diagnostic

Using the four Caputo Fig. 1 lower-panel curves already extracted from the checksum-verified \`SNProfile.pdf\`, define the figure-level diagnostic
\[
\Delta_Q(r)=\frac{n_p(r)-n_e(r)-n_\mu(r)}{n_0}.
\]

If \(n_p\) represented the **total positive baryonic charge density** and \(n_e,n_\mu\) represented the corresponding net negative lepton densities, charge neutrality would require \(\Delta_Q=0\). The digitized curves give:

| \(r\) (km) | \(n_p/n_0\) | \(n_e/n_0\) | \(n_\mu/n_0\) | \(\Delta_Q\) | \(\Delta_Q/(n_p/n_0)\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.423277 | 0.422718 | 0.000532 | +0.000027 | +0.006% |
| 5 | 0.346959 | 0.344441 | 0.002594 | -0.000077 | -0.02% |
| 8 | 0.200090 | 0.174579 | 0.025878 | -0.000368 | -0.18% |
| 9 | 0.146668 | 0.118673 | 0.029840 | -0.001845 | -1.26% |
| 10 | 0.109374 | 0.091013 | 0.024944 | -0.006582 | -6.02% |
| 12 | 0.050480 | 0.050062 | 0.010798 | -0.010380 | -20.56% |
| 14 | 0.014857 | 0.020687 | 0.001670 | -0.007501 | -50.49% |
| 15 | 0.005897 | 0.010805 | 0.000224 | -0.005132 | -87.03% |

The residual is below 0.2% through approximately 8 km, then grows:
- first exceeds 1% near 9 km;
- exceeds 5% near 9.9 km;
- exceeds 10% near 10.7 km;
- exceeds 20% near 12 km;
- exceeds 50% near 14 km.

These values are calculated from linearly interpolated digitized vertices. They are not raw simulation residuals.

## 5. Interpretation: do not force charge closure by rescaling

The outer-radius mismatch must not be “fixed” by rescaling one of the digitized curves. Plausible causes that must be distinguished include:

1. \(n_p\) is a free-proton density, while positive charge in nuclei/clusters is not included in that curve;
2. the plotted lepton curves and baryon curves use different net/total particle conventions;
3. the source model contains additional charged species or nuclei in the outer layers;
4. figure digitization and low-density clipping become important near the plotted floor.

The observed sign, \(n_e+n_\mu>n_p\), is compatible with omitted positive charge carried by nuclear clusters if \(n_p\) denotes free protons. It does **not** by itself prove that interpretation. The SFHoY composition study's discussion of D/T clusters motivates this hypothesis, but it is a different EOS-composition reconstruction and cannot be imported as if it were the Caputo baseline.

The \(\mu\)-density path terminates at \(r\simeq15.27\) km and reaches the plot floor \(10^{-4}n_0\); no extrapolation is permitted beyond its support.

## 6. Consequence for comparing Fig. 12 with Caputo

The comparison must keep three separate objects:
- Caputo \(n_B(r)\): baryon-number density;
- Caputo \(n_p(r)\): the source's plotted proton-density quantity, whose free/total convention must be established;
- Esseili–Kribs \(n_n(r),n_p(r)\): plotted nucleon species, whose relation to any nuclear-cluster component must be established.

It is **not** automatically valid to compare \(n_n^{EK}\) with \(n_B^{Caputo}-n_p^{Caputo}\), or to set \(n_n^{free}=n_B-n_p\). Nor should the Fig. 12 neutron/proton curves be summed and equated to Caputo \(n_B\) until the species conventions are reconciled.

## 7. Next executable checks

1. Obtain a high-resolution local copy of the APS Fig. 12 page/figure (or the permitted Garching profile release) so that the orange \(T\), neutron \(n\), and proton \(p\) curves can be digitized with source pixels and calibration.
2. Digitize Fig. 12 \(T,n_n,n_p\) and compare \(T^{EK}\) with the Caputo \(T\) curve on a common radial grid; report pointwise residuals and digitization uncertainty.
3. Compare \(n_p^{EK}\) with Caputo \(n_p\), but only after verifying whether both are free-proton densities.
4. Compare \(n_n^{EK}+n_p^{EK}\) with Caputo \(n_B\) as a diagnostic, not an assumed identity. A deficit can quantify non-free-nucleon baryon content only if the species definitions are compatible.
5. Use the Caputo charge-closure residual to locate where a free-nucleon-only kernel may become incomplete. Do not impose an algebraic correction to the published curves.
6. Keep SFHoY as a separate EOS-composition sensitivity case.

No B.2 opacity, transport sphere, escape probability, pure-vector Fig. 7 result, or axial cooling curve is changed by this audit.
