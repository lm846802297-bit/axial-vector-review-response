# Croon Fig. 2: inner-profile benchmark and unresolved outer opacity (preliminary)

Date: 2026-11-19

## Status

This is the first independent numerical implementation of the Croon et al. (2021) vector luminosity prescription. It remains a **preliminary public-profile reconstruction**: the pointwise comparison with digitized Fig. 2 vector paths is complete, but the low-mass strong-coupling trapping discrepancy remains unresolved, so this is not yet a quantitative reproduction. It does not alter the validated Blinov B.2/B.13 baseline and it is not an axial-vector result.

The implementation is deliberately isolated as lane C0. It uses Croon's own local-rate approximations and Sec. 3 transport prescription without importing Blinov's velocity factor, reduced opacity, lapse/redshift, or the Lai trapping prescription.

## Literal equations implemented

Croon Eq. (4.6), per \(g_{Z'}^2\), is the generic **single-neutrino-flavour** expression,

\[
\Gamma_{\nu\bar\nu,\,\rm generic}^{\rm prod}/g_{Z'}^2
=\frac{m_{Z'}^2}{12\pi\omega}\,
\frac{1}{e^{\omega/T}-1}.
\]

For the actual \(U(1)_{L_\mu-L_\tau}\) model, Croon Sec. 4.4 explicitly states that both \(\nu_\mu\) and \(\nu_\tau\) contribute. We therefore apply the factor of two to **both** the differential production power and the absorptive optical depth:

\[
\Gamma_{\nu\bar\nu,\,L_\mu-L_\tau}^{\rm prod}/g_{Z'}^2
=2\,\Gamma_{\nu\bar\nu,\,\rm generic}^{\rm prod}/g_{Z'}^2,
\qquad
\Gamma_{\nu\bar\nu,\,L_\mu-L_\tau}^{\rm abs}/g_{Z'}^2
=2\,\Gamma_{\nu\bar\nu,\,\rm generic}^{\rm abs}/g_{Z'}^2.
\]

The factor of two is a model-flavour multiplicity, not a vector-polarization factor. The B.7 rate is not substituted.

Croon Eq. (4.7), per \(g_{Z'}^2\), is implemented as

\[
\Gamma_{\gamma\mu}^{\rm prod}/g_{Z'}^2
=\frac{2\alpha_{\rm EM}}{3m_\mu^2}
(n_\mu F_{\rm deg})
\sqrt{1-\frac{m_{Z'}^2}{\omega^2}}\,
\frac{1}{e^{\omega/T}-1}.
\]

The susceptibility \(n_\mu F_{\rm deg}\) is evaluated from the single \(\mu^-\) Fermi-Dirac distribution used in Bollig et al. Eq. (2), including the two muon spin states. Antimuons are not added to this Croon-literal lane. A separate charge-summed sensitivity check finds the \(\mu^+\) susceptibility is at most about 1.5% of the \(\mu^-\) susceptibility in the muon-rich region; it remains a separate convention, not part of C0.

Detailed balance is imposed as

\[
\Gamma_{\rm abs}=e^{\omega/T}\Gamma_{\rm prod},
\]

so the local absorption expressions contain \(1+f_B\). The generic one-flavour outer \(R_\nu\to R_{\rm far}\) opacity retains the vacuum \(Z'\to\nu\bar\nu\) decay tail,

\[
\tau_{\nu,\rm out}^{\rm generic}/g_{Z'}^2
=(R_{\rm far}-R_\nu)\frac{m_{Z'}^2}{12\pi\omega},
\]

with \(R_{\rm far}=100\) km. No extra \(1/v_{Z'}\) is inserted in the radial optical-depth integral because Croon Eq. (3.3) does not contain it. For the \(L_\mu-L_\tau\) transfer, the same neutrino vacuum tail and the interior neutrino absorption are both multiplied by two, as stated in Sec. 4.4.

The luminosity integral is

\[
L_{Z'}=\int_0^{R_\nu}4\pi r^2dr
\int_{m_{Z'}}^\infty d\omega\,
\frac{\sqrt{\omega^2-m_{Z'}^2}\,\omega^2}{2\pi^2}
\Gamma_{\rm prod}(\omega,r)e^{-\tau_{\rm abs}(\omega,r)}.
\]

The factor of \(\omega\) from the emitted energy is already included in the \(k\omega^2\) phase-space measure after changing variables from \(k\) to \(\omega\). It must not be multiplied a second time.

The Croon Raffelt line is \(3\times10^{52}\) erg/s. The largest plotted mass, 200 MeV, is below \(2m_\mu=211.3168\) MeV, so the dimuon channel is closed throughout this Fig. 2 mass set.

## Profile and numerical setup

Croon Fig. 2 uses SFHo-18.8. The public profile available to this project is a Caputo-based reconstruction cross-checked against Bollig figures; it is not the raw Garching simulation file used by Croon. The code records the profile SHA-256 and source-row count in its output.

The \(T=3\) MeV boundary is obtained by linearly extrapolating the final two profile points:

\[
R_\nu=25.1511683\ {\rm km}.
\]

The published Fig. 2 caption identifies the gauged \(U(1)_{L_\mu-L_\tau}\) model without kinetic mixing. Eq. (4.6) is the generic one-neutrino-flavour expression, so the actual Fig. 2 calculation applies the Sec. 4.4 factor of two to both neutrino production and neutrino absorption. The generic one-flavour C0 curve is retained separately as a diagnostic baseline. Both lanes use the single \(\mu^-\) susceptibility convention. The Fig. 2 run uses:

- \(R_{\rm far}=100\) km;
- \(r\)-grid spacing 0.05 km, with the last nonzero and first zero muon-profile points retained;
- 160-point transformed energy Gauss quadrature, \(\omega=m+T_{\max}y^2\), \(0\le y\le6\);
- 256-point Gauss-Legendre momentum quadrature for \(n_\mu F_{\rm deg}\);
- cumulative Simpson integration for \(\tau_{\rm abs}\) and Simpson integration for the volume integral;
- 221 logarithmic couplings from \(10^{-11}\) to \(1\).

The 0.1 eV curve is also computed with \(R_{\rm far}=R_\nu\), corresponding to the dashed-boundary comparison described in the Fig. 2 caption.

## Preliminary numerical results

The table below is the **generic one-neutrino-flavour diagnostic baseline**, not the published Fig. 2 result. It uses Croon Eq. (4.6) before the Sec. 4.4 factor of two. The actual Fig. 2 L_mu-L_tau curves are being regenerated with the factor applied to both neutrino source and opacity; these generic values are retained only to make the flavour-multiplicity effect auditable:

| \(m_{Z'}\) | Peak \(g_{Z'}\) | Peak \(L_{Z'}\) [erg/s] | Low-\(g\) crossing of \(3\times10^{52}\) | High-\(g\) crossing |
|---:|---:|---:|---:|---:|
| 0.1 eV | \(7.49894\times10^{-8}\) | \(2.24478\times10^{55}\) | \(1.67154\times10^{-9}\) | \(4.03453\times10^{-2}\) |
| 1 eV | \(7.49894\times10^{-8}\) | \(2.24478\times10^{55}\) | \(1.67154\times10^{-9}\) | \(1.75438\times10^{-2}\) |
| 10 eV | \(7.49894\times10^{-8}\) | \(2.24478\times10^{55}\) | \(1.67154\times10^{-9}\) | \(3.37991\times10^{-3}\) |
| 0.1 MeV | \(7.49894\times10^{-8}\) | \(2.229\times10^{55}\) | \(1.67154\times10^{-9}\) | \(1.56646\times10^{-6}\) |
| 10 MeV | \(1.00\times10^{-8}\) | \(1.04889\times10^{54}\) | \(8.60711\times10^{-10}\) | \(3.18779\times10^{-8}\) |
| 200 MeV | \(7.50\times10^{-10}\) | \(6.32692\times10^{52}\) | \(3.40662\times10^{-10}\) | \(1.20614\times10^{-9}\) |

These are **preliminary public-profile reconstruction results**, not a final reproduction of the digitized Fig. 2 curves. The run uses the generic one-neutrino-flavour normalization; the separate \(L_\mu-L_\tau\) transfer doubles both neutrino production and neutrino absorption as stated in Sec. 4.4. No curve has been rescaled to force agreement with the paper's plot.

Machine-readable output (JSON + CSV): [GitHub Actions artifact](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14494204948). Artifact SHA-256: 7eaaafe9a5e0d28615e6ebc97386139808d354c1ec376694484fc98e8bd06b74. The run used 1687 source rows, a 507-point 0.05 km radial grid, 160-point energy quadrature, 256-point muon-momentum quadrature and 81 logarithmic couplings.

The optically-thin source fractions show the expected channel hierarchy:

| \(m_{Z'}\) | Neutrino coalescence fraction | Semi-Compton fraction |
|---:|---:|---:|
| 0.1 eV | \(3.0\times10^{-16}\) | \(1-3.0\times10^{-16}\) |
| 1 eV | \(3.0\times10^{-14}\) | \(1-3.0\times10^{-14}\) |
| 10 eV | \(3.0\times10^{-12}\) | \(1-3.0\times10^{-12}\) |
| 0.1 MeV | \(3.04\times10^{-4}\) | 0.999696 |
| 10 MeV | 0.7439 | 0.2561 |
| 200 MeV | 0.9981 | 0.0019 |

Thus the semi-Compton channel controls the sub-MeV curves, while neutrino coalescence controls the 10 and 200 MeV curves. At 200 MeV, the Thomson semi-Compton approximation contributes below 0.2% of the optically-thin source.

## Numerical checks completed locally

- The thin-limit luminosity scales as \(g_{Z'}^2\); a dedicated \(g=(1,2)\times10^{-12}\) test pair agrees with the exact quadratic scaling to better than \(2\times10^{-5}\). The plotted \(10^{-11}\) lower edge is not forced to be perfectly thin for the 10 MeV case: its small residual outer-decay attenuation is retained.
- The energy quadrature change from order 160 to 240 is below \(10^{-11}\) over the luminosity range used for the crossing extraction.
- The momentum susceptibility at order 256 agrees with order 512 to numerical precision in the muon-rich region.
- Refining the radial integration from 0.1 km to 0.05 km changes the peak luminosities by less than \(0.03\%\); the radial-integrated curve differs by less than about \(0.13\%\) near the high-coupling tail for the low-mass cases when Simpson integration is used.
- The detailed-balance identity \(\Gamma_{\rm abs}/\Gamma_{\rm prod}=e^{\omega/T}\) is satisfied algebraically.
- The outer vacuum decay tail has a visible effect for heavier masses. For \(m=0.1\) eV, \(R_{\rm far}=100\) km and \(R_{\rm far}=R_\nu\) differ by less than \(0.1\%\) at \(g=10^{-2}\), increasing to about 8% at \(g=0.1\).



## Dedicated 10 MeV C0 cross-check: generic baseline and Fig. 2 L_mu-L_tau lane

Two distinct comparisons are retained:

1. **Generic one-flavour diagnostic:** the archived single-flavour six-mass scan is compared with the generic C0 adapter. This validates the two radial-integration implementations but is not the published Fig. 2 model.
2. **Published Fig. 2 model:** the current two-flavour six-mass scan is compared with the independent C0 adapter with `neutrino_flavour_factor=2`, using the same SFHo-18.8 profile and (R_{\rm far}=100) km.

For the generic one-neutrino-flavour diagnostic with \(R_{\rm far}=100\) km:

| Quantity | Fig. 2 mass sweep | 1687-node C0 adapter |
|---|---:|---:|
| Low-\(g\) Raffelt crossing | \(8.60711\times10^{-10}\) | \(8.60466\times10^{-10}\) |
| High-\(g\) Raffelt crossing | \(3.18779\times10^{-8}\) | \(3.19141\times10^{-8}\) |
| Peak coupling | \(1.00\times10^{-8}\) | \(1.00\times10^{-8}\) |
| Peak luminosity [erg/s] | \(1.04889\times10^{54}\) | \(1.04884\times10^{54}\) |

The low- and high-coupling crossing differences are about 0.03% and 0.11%, respectively. This is an independent numerical cross-check of the two radial-integration implementations in the **generic one-flavour lane**; it is **not** a comparison with the published two-flavour Fig. 2 or its digitized points.

The separate \(L_\mu-L_\tau\) variant applies the Sec. 4.4 factor of two to both the neutrino source and the neutrino absorptive optical depth, leaving the semi-Compton source unchanged. This is the flavour prescription required for the published Fig. 2. For the same 10 MeV profile and \(R_{\rm far}=100\) km, it gives the provisional Raffelt-line crossings
\[
g_X^{\rm low}=6.52618\times10^{-10},\qquad
g_X^{\rm high}=2.18470\times10^{-8}.
\]
These are the same public-profile reconstruction and Croon transport assumptions, not a new SN1987A exclusion.

The C0 numerical audit also finds:
- refining the local energy order from 64 to 96, the optical-depth energy grid from 301 to 601 points, and the susceptibility order from 128 to 192 changes the total luminosity by at most 0.019%;
- including the \(\mu^+\) susceptibility changes the total luminosity by only 0.18% at \(g_X=10^{-9}\), with a maximum absolute change below 0.4% across the scanned coupling range;
- changing \(R_{\rm far}=100\) km to \(R_{\rm far}=R_\nu\) raises the high-coupling crossing substantially, as expected from the reduced outer vacuum-decay opacity. Croon uses \(R_{\rm far}=100\) km for its conservative result.

The corresponding generic, \(L_\mu-L_\tau\), charge-conjugate, high-order and convergence-audit outputs are archived in the same workflow run:
- [generic 10 MeV C0 curve](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495061522)
- [\(L_\mu-L_\tau\) 10 MeV C0 curve](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495290606)
- [\(\mu^+\) sensitivity curve](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495400333)
- [high-order 10 MeV C0 curve](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495071605)
- [quadrature and profile-convention audit](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495515156)

All these calculations remain preliminary because the public profile is not the raw Garching radial table and the low-mass strong-coupling \(R_{\rm far}=100\) km curve lacks the outer semi-Compton opacity input. The PDF Fig. 2 paths have now been digitized and compared point-by-point; that comparison localizes, but does not remove, the missing outer-opacity contribution.

## Pointwise comparison with the published Fig. 2 vector paths (2026-11-19)

The PDF curve extraction and a no-fit numerical comparison are now complete. The comparison uses the published arXiv PDF vector paths, not a raster screenshot. The source PDF SHA-256 is
\[
\texttt{c080958470a1e242b8c0a97a5f9225f0261e807e499c7690683805ebec6977e5}.
\]
The axis calibration residuals are \(3.68\times10^{-7}\) dex in \(\log_{10}g_{Z'}\) and \(1.44\times10^{-7}\) dex in \(\log_{10}L\). The digitizer extracts 40, 42, 55, 87, 73, 76 and 50 points for the six solid curves and the \(R_{\rm far}=R_\nu\) dashed sensitivity curve, respectively. The vector-path stroke width is not yet propagated as an uncertainty.

For each digitized point, the model luminosity is linearly interpolated in \(\log_{10}L\) versus \(\log_{10}g\). Define
\[
\Delta=\log_{10}\!\left(\frac{L_{\rm model}}{L_{\rm Fig.\,2}}\right).
\]
No normalization fit, coupling shift, or curve rescaling is performed.

| Fig. 2 curve | Points | Median \(\Delta\) [dex] | RMS [dex] | Median \(L_{\rm model}/L_{\rm Fig.2}\) |
|---|---:|---:|---:|---:|
| 200 MeV | 40 | +0.0467 | 0.0461 | 1.114 |
| 10 MeV | 42 | +0.0326 | 0.0392 | 1.078 |
| 0.1 MeV | 55 | -0.0507 | 0.1484 | 0.890 |
| 10 eV | 87 | +0.4987 | 0.4247 | 3.152 |
| 1 eV | 73 | +0.4679 | 0.3918 | 2.937 |
| 0.1 eV, \(R_{\rm far}=100\) km | 76 | +0.4806 | 0.4073 | 3.024 |
| 0.1 eV, \(R_{\rm far}=R_\nu\) | 50 | -0.0442 | 0.2265 | 0.903 |

The branch split is more diagnostic than the full-curve median:

| Fig. 2 curve | Low-\(g\) median \(\Delta\) [dex] | High-\(g\) median \(\Delta\) [dex] |
|---|---:|---:|
| 200 MeV | +0.0469 | +0.0441 |
| 10 MeV | +0.0321 | +0.0381 |
| 0.1 MeV | -0.0507 | -0.0777 |
| 10 eV | -0.0775 | +0.5092 |
| 1 eV | -0.0791 | +0.4890 |
| 0.1 eV, \(R_{\rm far}=100\) km | -0.0806 | +0.4897 |
| 0.1 eV, \(R_{\rm far}=R_\nu\) | -0.0551 | -0.0417 |

This establishes three distinct outcomes:

1. **High masses:** the 10 and 200 MeV curves are close to the published vector paths at the roughly 8--11% median level. This is encouraging, but it is not a precision reproduction.
2. **Weak-coupling low-mass branch:** the 10 eV, 1 eV and 0.1 eV curves are within about 0.08 dex at their low-\(g\) points. Thus the optically-thin semi-Compton normalization is not globally wrong by a factor of three.
3. **Strong-coupling low-mass branch:** for the conservative \(R_{\rm far}=100\) km curves, the model is high by a median factor of about 3.1. The \(R_{\rm far}=R_\nu\) dashed sensitivity curve has a much smaller median offset, although its RMS and maximum residual remain affected by the high-\(g\) endpoint.

The discrepancy is now localized more sharply by using the two published 0.1 eV curves themselves. The Fig. 2 caption says that the dashed curve changes only \(R_{\rm far}\) from 100 km to \(R_\nu\). For each common coupling, define
\[
S_{\rm paper}(g)=
\frac{L_{\rm Fig.2}(R_{\rm far}=R_\nu)}
{L_{\rm Fig.2}(R_{\rm far}=100\ {\rm km})}.
\]
Across the strong-coupling plateau \(3\times10^{-6}\le g_{Z'}\le3\times10^{-2}\), 27 digitized solid-curve points give
\[
{\rm median}\ S_{\rm paper}=3.38190,\qquad
P_{16-84}=[3.22590,\,3.64968],
\]
with pointwise range 3.12740--3.72331. Thus the published \(R_\nu\to R_{\rm far}\) optical-depth segment suppresses the integrated luminosity by a factor of about 3.4 over this plateau.

The current implementation instead gives
\[
{\rm median}\ S_{\rm model}=1.0000009,\qquad
P_{16-84}=[1.00000,\,1.00059],
\]
over the same coupling window. Its additional missing integrated-luminosity suppression is therefore
\[
\boxed{S_{\rm paper}/S_{\rm model}=3.38190,\qquad
\ln(S_{\rm paper}/S_{\rm model})=1.21844.}
\]
The logarithm is an **effective luminosity-suppression diagnostic**, not a local optical depth and not a unique reconstruction of \(\Gamma_{\rm abs}(r,\omega)\). The current \(R_{\rm far}=R_\nu\) model curve agrees with the digitized dashed curve to a median \(0.026\) dex on this plateau, while the current \(R_{\rm far}=100\) km curve is high by a median factor 3.21 relative to the digitized solid curve. This isolates the missing effect to the outer segment rather than to the interior semi-Compton normalization.

For \(m_{Z'}=0.1\) eV, the vacuum neutrino-decay opacity is proportional to \(m_{Z'}^2\) and is numerically negligible throughout most of this plateau. The \(T_{\rm outer}=3\) MeV Bose-enhanced neutrino-decay envelope also changes the luminosity by only 1.14% at \(g=0.1\) and 2.34% at \(g=0.3\). It cannot explain the factor-3.4 solid/dashed separation. Since the low-mass Croon production and absorption channels are dominated by semi-Compton scattering, the missing \(R_\nu\to R_{\rm far}\) term is strongly indicative of **outer semi-Compton absorption on the residual muon population**, or another outer-medium opacity included in the authors' profile but absent from ours.

The current profile is available only through \(R_\nu\simeq25.15\) km. In the C0 code, the muon susceptibility is therefore truncated at the edge of the public profile; the \(R_{\rm far}=100\) km calculation includes only the vacuum neutrino-decay tail outside \(R_\nu\). It must now be described as an **interior-profile calculation with a vacuum-only outer continuation**, not as a complete Croon \(R_{\rm far}=100\) km transport result. The dashed \(R_{\rm far}=R_\nu\) curve is the cleaner comparison for the presently available profile.

The missing input is the raw outer radial profile (at minimum \(T(r)\) and \(\mu_\mu(r)\), or \(n_\mu(r)F_{\rm deg}(r)\)) between \(R_\nu\) and 100 km. The official Garching archive lists the Bollig radial-profile dataset, but its endpoint returns HTTP 401; the archive explicitly says that some data are password-protected and requests that users contact the maintainers. A separate publication also states that the Bollig radial profiles are available upon request. Independently, the public [SNforMuTau code repository](https://github.com/spinjo/SNforMuTau) explicitly says that its simulation data must be requested from the authors of Bollig et al. (arXiv:2005.07141). We cannot infer a physical outer profile from the Fig. 2 luminosity curves without tuning. Therefore, we retain the outer-opacity gap as unresolved and do not fit an opacity profile to the figure.


The model output including this separate \(T_{\rm outer}=3\) MeV envelope is archived in [workflow artifact](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44485973996/artifacts/14510003948). The 13-test Fig. 2 transport suite checks both the vacuum and finite-temperature outer-tail formulas.

The 0.1 MeV curve has a separate high-\(g\) endpoint outlier (maximum absolute residual 0.535 dex); its median is much closer. This endpoint must be inspected independently before interpreting the full RMS as a smooth physical discrepancy.

Raw-profile access note: [official Garching archive entry](https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/archive.html) lists the Bollig radial profiles; the [radial-profile data endpoint](https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/data/Bollig2016_radial_profiles/) is access-controlled (HTTP 401). The archive asks users to contact the maintainers for password-protected data.

Reproducible outputs:
- [No-fit pointwise comparison JSON](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44485973996/artifacts/14509769298)
- [Croon Fig. 2 model curves](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44485973996/artifacts/14510003948)
- [Digitized PDF vector curves](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44485973996/artifacts/14509664425)
- [Outer-opacity gap diagnostic](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44485973996/artifacts/14510372968)

The current workflow run [#44485973996](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44485973996) completed successfully with 69 passing tests, including the new solid/dashed outer-opacity diagnostic, C0 metadata checks, Lai 2024 plateau/rate-convention equation audit, PDF vector extraction/digitization, no-fit comparison, energy-threshold audit, and the existing B.13/B.16 and Ward-identity regression suites.

## What remains before calling this a Fig. 2 reproduction

1. Obtain the raw Garching SFHo-18.8, \(t_{\rm pb}=1\) s radial profile through \(R_{\rm far}\), including the muon susceptibility \(n_\mu F_{\rm deg}\). Until then, do not claim a complete \(R_{\rm far}=100\) km low-mass transport calculation.
2. Re-run the outer-opacity integral with the actual profile and independently verify its radial interpolation and tail.
3. Inspect the 0.1 MeV high-\(g\) digitized endpoint and propagate the PDF line-stroke uncertainty.
4. Keep the C0 result separate from the corrected B.13 local-rate lane and from all axial-vector predictions.

No axial-vector curve or SN1987A exclusion is updated by this preliminary calculation.
