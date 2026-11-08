# B.2 Inner-Path Opacity: Channel-, Shell-, and Direction-Resolved Audit

> **Historical profile version:** the paired numerical output for this report uses the 501-node uniform profile, SHA-256 `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9`. The current working input is the 1687-row vertex-preserving profile, SHA-256 `6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc`. The current-profile rerun and quantitative old/new comparison are documented in `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`; see also `outputs/b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json`. Keep this report as a historical record and do not combine its numerical output with current-profile results.


**Date:** 2026-11-09  
**Status:** Numerical audit completed for the 10 MeV pure-vector benchmark. This does **not** certify the full Blinov vector reproduction against the unavailable original Garching background, and it does not authorize an axial-vector update.

## Executive result

The 8–22 km path has now been independently decomposed into \(\nu_\mu\) inverse decay, \(\nu_\tau\) inverse decay, and Compton absorption, with the impact-parameter geometry treated analytically on the piecewise-linear radial opacity profile. The four direction intervals are integrated independently rather than obtained by masking nodes from a global angular quadrature.

Three conclusions are robust:

1. The **total** B.2 optical depth agrees with an independent 256-point full-path integration to a maximum relative residual of \(1.19225\times10^{-4}\); after weighting by the dominant 8–15 km B.1 source, the L1 relative difference is only \(2.09389\times10^{-6}\).
2. Compton absorption is concentrated in the inner production region. At \(\omega=15\) MeV it contributes 40.1%, 34.9%, and 15.5% of the local reduced opacity at 8, 10, and 12 km, respectively, but only 0.22% at 15 km and is negligible farther out. Neutrino inverse decay remains important through 22–25 km.
3. At the strong-coupling endpoint, the escaping population from the dominant 8–15 km source is strongly outward biased: 76.679% of the escaping luminosity lies in \(0.5\leq\cos\theta\leq1\), while only 0.556% lies in \(-1\leq\cos\theta\leq-0.5\). Each equal-width direction bin carries exactly 25% of the unattenuated source weight.

A separate numerical issue is also established: the previous global-s quadrature with shell masks can reproduce the total path integral while misallocating individual shell contributions. Shell-level interpretations should therefore use the analytic radial decomposition below, not the old masked shell matrix.

## 1. Frozen physical baseline and scope

The audit holds the following fixed:

- \(m_{A'}=10\) MeV and the pure-vector Blinov transport baseline;
- the reconstructed SFHo-18.8 profile currently used by the repository;
- \(R_{\max}=25\) km;
- the B.1 source measure and the fixed-\(\omega\) convention used in B.2;
- the original coupling grid from the stored Fig. 7 reference vertices.

The reduced absorption is split into four explicit channels:
\[
\Gamma^*_{\mathrm{abs},c}(r,\omega)
=\left(e^{\omega/T(r)}-1\right)\Gamma_{\mathrm{prod},c}(r,\omega),
\]
with \(c=\nu_\mu,\nu_\tau,\mathrm{Compton},\mathrm{dimuon}\). The dimuon channel is retained as an explicit zero at 10 MeV because it is kinematically closed.

This is the B.14–B.19 transport baseline. The exact moving-muon B.13 local kernel is **not** silently substituted into the Compton opacity. No production rate, opacity, coupling, or luminosity is rescaled. No axial-vector curve is calculated, and no production transport file or published plot is changed.

## 2. Independent radial path integral

For a source at radius \(r_0\) and direction cosine \(\mu=\cos\theta\), define the impact parameter
\[
b=r_0\sqrt{1-\mu^2}.
\]
Along the straight ray,
\[
r(s)^2=b^2+(s+r_0\mu)^2,
\qquad
\left|\frac{ds}{dr}\right|
=\frac{r}{\sqrt{r^2-b^2}}.
\]

For an outward ray (\(\mu\geq0\)), each radius from \(r_0\) to \(R_{\max}\) is traversed once. For an inward ray (\(\mu<0\)), the interval \(b<r<r_0\) is traversed twice, while \(r_0<r<R_{\max}\) is traversed once. This explicitly retains the turning point and the inward/outward branches.

The opacity is linearly interpolated between the existing radial-grid nodes. On each interval it has the form \(\kappa(r)=A+Br\), so the path integral is analytic:
\[
\int \kappa(r)\,ds
=A\,\Delta\sqrt{r^2-b^2}
+B\,\Delta\left[
\frac12\left(
r\sqrt{r^2-b^2}
+b^2\ln\frac{r+\sqrt{r^2-b^2}}{b}
\right)
\right].
\]
For \(b=0\), the second primitive is taken as \(r^2/2\). The integration is split at every radial interpolation node and every physical shell boundary. Thus each reported shell contribution is integrated on its own smooth radial segment.

The final path-shell grid is 0–5, 5–8, 8–10, 10–12, 12–15, 15–16.5, 16.5–18.5, 18.5–20, 20–22, and 22–25 km. The 0–8 km core and 22–25 km outer shell are retained as controls rather than silently omitted from inward rays.

## 3. Numerical validation

Six unit tests pass:

1. constant opacity reproduces the exact chord length;
2. piecewise-linear radial integration agrees with independently segmented s-coordinate quadrature;
3. outer-shell columns are invariant under \(\mu\to-\mu\) for sources inside 22 km;
4. the inward ray traverses inner radii twice;
5. the separate reduced-absorption channels close to the reference total;
6. equal-width direction bins carry equal unattenuated angular weight.

The recorded residuals are:

| Check | Maximum residual |
|---|---:|
| B.1 production-channel sum | \(4.06\times10^{-16}\) |
| Reduced-absorption channel sum | \(5.94\times10^{-16}\) |
| Analytic radial total vs. 256-point global-s path integral | \(1.19225\times10^{-4}\) |
| Same comparison, B.1-source-weighted over 8–15 km | \(2.09389\times10^{-6}\) |
| Direction-bin angular weights | exactly unity in the sum; 0.25 in each equal-width bin |

For the angle-integrated escape probability, global Gauss–Legendre orders 32 and 64 differ by \(1.30\times10^{-6}\) at the strong-coupling endpoint for the 8–15 km source. Direction-bin integrals use separate mapped Gauss rules inside each bin. Increasing the per-bin order from 16 to 32 changes the strong-endpoint escaped fraction in the most difficult backward bin by only \(1.29\times10^{-4}\) relative; the other three bins change by less than \(4.5\times10^{-6}\).

## 4. Local channel dependence

The following values are the reduced absorption rates per \(g^2\) at \(\omega=15\) MeV, evaluated on the reconstructed profile. They are reported in the internal units used by the reference implementation.

| Radius (km) | \(\nu_\mu\) inverse decay | \(\nu_\tau\) inverse decay | Compton | Compton fraction of total |
|---:|---:|---:|---:|---:|
| 8 | 0.023855 | 0.025551 | 0.033037 | 40.07% |
| 10 | 0.028506 | 0.029141 | 0.030918 | 34.91% |
| 12 | 0.037624 | 0.037875 | 0.013855 | 15.51% |
| 15 | 0.072196 | 0.072196 | \(3.183\times10^{-4}\) | 0.220% |
| 18.5 | 0.151310 | 0.151443 | \(2.426\times10^{-10}\) | negligible |
| 20 | 0.175784 | 0.175784 | \(5.659\times10^{-13}\) | negligible |
| 22 | 0.191892 | 0.191892 | \(5.371\times10^{-16}\) | negligible |

Thus the Compton opacity is a genuinely inner-region effect, concentrated around 8–12 km. It cannot be represented by a uniform rescaling of the neutrino inverse-decay opacity. Conversely, the outer 22–25 km opacity is effectively entirely due to neutrino inverse decay.

The 8–15 km region supplies \(79.6117\%\) of the total B.1 source in this benchmark.

## 5. Strong-coupling path decomposition

At the strong endpoint
\[
g=4.17168965\times10^{-8},
\]
the source-weighted escape probability for the 8–15 km emission region is
\[
P_{\mathrm{esc}}=3.53332\times10^{-4}.
\]

The table gives \(\langle\tau_c/g^2\rangle\), first weighted by the unattenuated B.1 source and then by the surviving escaping population.

| Path group | Channel | Source-weighted \(\langle\tau/g^2\rangle\) | Escaped-population-weighted \(\langle\tau/g^2\rangle\) |
|---|---|---:|---:|
| 0–8 km | \(\nu_\mu\) inverse decay | \(1.970\times10^{14}\) | \(3.472\times10^{12}\) |
| 0–8 km | \(\nu_\tau\) inverse decay | \(2.444\times10^{14}\) | \(3.642\times10^{12}\) |
| 0–8 km | Compton | \(1.313\times10^{14}\) | \(4.141\times10^{12}\) |
| 8–22 km | \(\nu_\mu\) inverse decay | \(3.090\times10^{15}\) | \(1.072\times10^{15}\) |
| 8–22 km | \(\nu_\tau\) inverse decay | \(3.101\times10^{15}\) | \(1.072\times10^{15}\) |
| 8–22 km | Compton | \(8.085\times10^{14}\) | \(4.035\times10^{14}\) |
| 22–25 km | \(\nu_\mu\) inverse decay | \(7.817\times10^{14}\) | \(2.612\times10^{14}\) |
| 22–25 km | \(\nu_\tau\) inverse decay | \(7.817\times10^{14}\) | \(2.612\times10^{14}\) |
| 22–25 km | Compton | 0.765 | 0.723 |

For the surviving population, the summed 8–22 km mean optical-depth contribution is about 4.88 times the 22–25 km contribution. The outer shell is nevertheless not irrelevant: its neutrino inverse-decay contribution remains substantial, and its leave-one-shell-out sensitivity is comparable to that of the 12–15 km neutrino shell.

The Compton contribution to the surviving-population-weighted 8–22 km optical depth is about 15.8%. Its importance is concentrated in the 8–15 km path segments.

## 6. Direction-resolved escape

The direction bins are integrated independently, so the unattenuated source fraction is exactly 25% in every equal-width \(\cos\theta\) interval. At the strong endpoint, for emission from 8–15 km:

| \(\cos\theta\) | Unattenuated source fraction | Escaped-luminosity fraction | Bin-averaged escape probability |
|---|---:|---:|---:|
| \([-1,-0.5)\) | 25.000% | 0.5563% | \(7.863\times10^{-6}\) |
| \([-0.5,0)\) | 25.000% | 2.7862% | \(3.938\times10^{-5}\) |
| \([0,0.5)\) | 25.000% | 19.9789% | \(2.824\times10^{-4}\) |
| \([0.5,1]\) | 25.000% | 76.6786% | \(1.084\times10^{-3}\) |

Consequently, 96.657% of the escaping luminosity is in the outward hemisphere (\(\mu>0\)), compared with 50% of the unattenuated source. Only 0.556% of the escaping luminosity comes from the most inward-directed bin. This is a physical survival bias after attenuation, not an unattenuated source anisotropy or a global-Gauss binning artefact.

For a nonlinear cross-check, the leave-one-channel-shell-out diagnostic holds B.1 and all other opacity components fixed. At this coupling, removing a single \(\nu_\mu\) inverse-decay shell raises the integrated escaping luminosity by 59.3% for 12–15 km and 59.6% for 22–25 km; the \(\nu_\tau\) results are nearly identical. Removing Compton opacity raises it by 34.3%, 42.2%, and 15.0% for the 8–10, 10–12, and 12–15 km shells, respectively. These counterfactual effects are nonlinear and must not be added as if they were independent luminosity fractions.

## 7. Audit of the previous masked shell quadrature

The previous implementation integrated over the full s interval and then assigned global Gauss nodes to shells using a radial mask. The shell sum reproduces the same global integral to machine precision, but that closure alone does not establish the accuracy of each shell.

The source-weighted L1 difference between the old shell allocation and the analytic radial result was scanned over global path orders. The following maxima refer to the important 8–15 km emission region:

| Global path order | Maximum all-direction error: neutrino | Maximum all-direction error: Compton | Maximum direction-resolved error: neutrino | Maximum direction-resolved error: Compton |
|---:|---:|---:|---:|---:|
| 16 | 17.59% | 26.69% | 22.01% | 41.47% |
| 32 | 9.65% | 14.01% | 13.38% | 23.74% |
| 64 | 5.12% | 7.08% | 6.87% | 10.67% |
| 128 | 2.53% | 3.39% | 3.97% | 5.78% |
| 256 | 1.19% | 1.69% | 1.83% | 2.92% |

The larger relative differences across the full 8–22 km interval occur in outer Compton shells whose absolute opacity is already negligible. They should not be interpreted as comparable errors in the total optical depth. The practical conclusion is narrower: the old path-order-32 shell allocation is not sufficiently accurate for detailed shell-by-shell physical attribution. The analytic radial decomposition is the reference for this audit.

## 8. Interpretation and limitations

- The total B.2 path integral is independently cross-checked; no evidence here supports changing the total opacity or applying an empirical luminosity rescaling.
- The inner 8–22 km path is larger than the outer 22–25 km path in the surviving-population-weighted mean optical depth, but the outer neutrino inverse-decay shell remains important.
- Compton absorption is localized to the inner source region and must remain a separate channel.
- The directional escape bias is robust after using bin-local angular quadrature.
- This is still a 10 MeV calculation on the reconstructed public profile. The original Garching simulation table used by Blinov remains unavailable, so the audit does not establish identity with the authors' raw stellar background.
- The pure-vector benchmark has not yet been certified against the complete original reference calculation. The axial-vector result remains frozen.

## 9. Reproducibility

- Audit implementation: **audit_b16_inner_path_channel_directional.py**
- Tests: **test_b16_inner_path_channel_directional.py**
- Machine-readable output: **outputs/b16_inner_path_channel_directional_10mev_2026-11-09.json**
- Workflow: **.github/workflows/b16-inner-path-channel-directional.yml**
- Successful CI run: [B.16 analytic inner-path channel and direction audit](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42504612491)

The workflow passes all six tests, runs the audit, and verifies that the production axial rates, transport outputs, and published axial plot files remain unchanged.
