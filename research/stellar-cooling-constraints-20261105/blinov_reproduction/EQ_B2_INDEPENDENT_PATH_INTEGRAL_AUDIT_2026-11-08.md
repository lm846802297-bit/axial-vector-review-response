# Independent Blinov Eq. (B.2) Path-Integral Audit — 2026-11-08

## Executive result

**The independent path and angular integration passes. The 10 MeV high-coupling Fig. 7 discrepancy is not caused by the numerical path integral or angular quadrature in the current scalar reference implementation.**

At the high-coupling point
\[
g=4.171689650228597\times10^{-8},
\]
the independent 256-point angular result is
\[
L_{\rm calc}=2.437334708881218\times10^{52}\ {\rm erg\,s^{-1}},
\]
while the digitized Fig. 7 reference is
\[
L_{\rm Fig.\,7}=1.267814759073720\times10^{52}\ {\rm erg\,s^{-1}}.
\]
The residual is therefore \(+92.24691\%\). Increasing the angular order from 128 to 256 changes this high-coupling luminosity by only \(8.20\times10^{-9}\) fractionally. Replacing the existing 32-point path quadrature by the independent analytic path integral changes the full luminosity by at most \(4.31\times10^{-5}\) over the 25 Fig. 7 comparison points.

This rules out the Eq. (B.2) path/angular quadrature as the source of the approximately 92% tail discrepancy, within the frozen opacity interpolation and profile used here. It does not identify the remaining physical or source-data discrepancy.

## 1. Scope and frozen inputs

This is a transport-only audit. The following inputs remain unchanged:

- \(m_V=10\) MeV and \(R_{\max}=25\) km;
- the reconstructed SFHo-18.8 profile and Caputo digitized \(T(r)\), \(\mu_\mu(r)\), and \(\mu_{\nu_\mu}(r)\);
- the baseline \(\mu_{\nu_\tau}=0\);
- the local reduced absorption rates returned by the existing literal Appendix-B reference implementation;
- radial order 40, energy order 100, and the 1000 MeV energy offset;
- the coupling dependence, which enters only as \(g^2\) in \(\exp(-g^2\tau)\).

The energy \(\omega\) is held fixed along each ray, following the literal argument \(\Gamma_{\rm abs}^*(r',\omega)\) in Eq. (B.2). No chemical potential, local collision rate, opacity normalization, source term, or coupling is adjusted.

## 2. Independent geometry and path integral

The printed equation is
\[
\mathcal O(r,\omega)=\frac12\int_{-1}^{1}d\mu\,
\exp\left[-\frac{1}{v_V}
\int_0^{s_{\max}}ds\,
\Gamma_{\rm abs}^*\!\left(
\sqrt{r^2+s^2+2rs\mu},\omega
\right)\right].
\]

Instead of reusing the source-centered path coordinate \(s\), the independent implementation uses the impact parameter and longitudinal coordinate
\[
b=r\sqrt{1-\mu^2},\qquad z_0=r\mu,
\]
\[
r'(z)=\sqrt{b^2+z^2},\qquad
z_{\rm exit}=\sqrt{R_{\max}^2-b^2}.
\]
Since \(ds=dz\), the path column is
\[
\tau(r,\mu,\omega)=\frac{1}{v_V}
\int_{z_0}^{z_{\rm exit}}dz\,
\Gamma_{\rm abs}^*\!\left(\sqrt{b^2+z^2},\omega\right).
\]

This parameterization treats outward and inward-going rays uniformly. An inward ray has \(z_0<0\), crosses the closest-approach point, and exits through the opposite side of the sphere.

The existing reference uses a piecewise-linear interpolation of the radial opacity. On each radial cell write
\[
\Gamma_{\rm abs}^*(r,\omega)=A_i(\omega)+B_i(\omega)r.
\]
The independent code inserts every radial-cell crossing along the ray and integrates each segment analytically using
\[
\int dz\,\sqrt{b^2+z^2}
=\frac12\left[
z\sqrt{b^2+z^2}
+b^2\operatorname{arsinh}(z/b)
\right],
\]
with the continuous \(b\to0\) limit treated separately. Thus the path integration is exact for the same piecewise-linear opacity interpolant; it does not depend on the original 32-point path quadrature.

The angular average is then recomputed with 16, 64, 128, and 256 Gauss-Legendre nodes. Twelve representative source-radius/energy points are also checked with adaptive angular quadrature.

## 3. Numerical validation

### 3.1 Regression tests

All six new independent geometry/integration tests pass:

1. constant opacity reproduces the analytic chord length;
2. the piecewise-linear path integral agrees with split adaptive quadrature;
3. absorber-shell columns are additive;
4. a central source has direction-independent path columns;
5. the outward surface ray has zero path length while the inward ray crosses the diameter;
6. adaptive angular integration agrees with high-order Gauss-Legendre integration.

The full Major 4.4 numerical-validation workflow also passes, including the repository-wide tests and saved-scan reproducibility checks.

### 3.2 Existing path quadrature versus analytic path integral

At the same 16 angular nodes, the independent analytic path columns are compared point by point with the existing 32-node path quadrature:

| Diagnostic | Result |
|---|---:|
| Maximum relative column difference, retaining entries above \(10^{-10}\) of the global peak | \(5.72\times10^{-3}\) |
| RMS relative column difference on the same mask | \(2.13\times10^{-4}\) |
| Maximum relative change in the integrated luminosity over all 25 couplings | \(4.31\times10^{-5}\) |
| Reproduction of the archived three-layer baseline | \(2.22\times10^{-16}\) maximum relative difference |

The largest pointwise column difference does not translate into a comparably large luminosity difference. The source-, energy-, and angle-weighted integral is much less sensitive to those isolated path-column differences.

### 3.3 Angular convergence

| Angular order change | Maximum relative luminosity change over the 25 points | Change at the high-coupling endpoint |
|---|---:|---:|
| 16 \(\to\) 64 | \(2.24\times10^{-5}\) | \(2.00\times10^{-6}\) |
| 64 \(\to\) 128 | \(9.59\times10^{-7}\) | \(1.20\times10^{-7}\) |
| 128 \(\to\) 256 | \(1.10\times10^{-7}\) | \(8.20\times10^{-9}\) |

The maximum absolute difference between the selected adaptive angular checks and the 256-node result is \(4.61\times10^{-14}\). The largest *relative* difference, \(1.39\times10^{-4}\), occurs for an escape probability of only \(1.13\times10^{-113}\); it is an underflow-scale tail and has no material effect on the integrated luminosity.

### 3.4 Fig. 7 comparison after independent integration

| Angular order | Mean absolute relative residual | High-coupling residual |
|---:|---:|---:|
| 16 | 15.7331% | 92.2465% |
| 64 | 15.7326% | 92.2469% |
| 128 | 15.7326% | 92.2469% |
| 256 | 15.7326% | 92.2469% |

The residual is stable under both path and angular integration changes. The approximately 92% high-coupling discrepancy is therefore not a path-quadrature artifact.

## 4. Independent outer-neutrino optical-depth decomposition

At the high-coupling benchmark, using the exact path integral and 256 angular nodes, the source-weighted neutrino optical depths are:

| Component | Mean optical depth |
|---|---:|
| \(\nu_\mu\), all radii | 7.18106 |
| \(\nu_\tau\), all radii | 7.30600 |
| Both flavors, all radii | 14.48706 |
| Both flavors, absorber shell 15–20 km | 4.46880 |
| Both flavors, absorber shell 20–25 km | 4.67504 |
| Both flavors, absorber shell 15–25 km | 9.14384 |

Therefore
\[
\frac{\langle\tau_{\nu,15-25}\rangle}
{\langle\tau_{\nu,\mathrm{total}}\rangle}
=0.6311733.
\]
The independently integrated value, 63.1173%, agrees with the earlier 63.17% result. The small difference is consistent with inserting the 15 km and 20 km shell boundaries exactly rather than letting the shell mask transition across a radial interpolation cell.

The two flavor contributions in the outer shell remain nearly equal:
\[
\langle\tau_{\nu_\mu,15-25}\rangle=4.57086,\qquad
\langle\tau_{\nu_\tau,15-25}\rangle=4.57298.
\]

The outer fraction depends on the production-radius bin:

| Production radius | Fraction of neutrino optical depth accumulated at 15–25 km |
|---|---:|
| 0–5 km | 59.42% |
| 5–10 km | 58.04% |
| 10–15 km | 65.91% |
| 15–20 km | 87.53% |
| 20–25 km | 95.58% |

This is an absorber-shell contribution to a source-weighted mean optical depth. It is **not** a statement that the outer shell absorbs 63.12% of the luminosity.

At the same high-coupling point, the escaped luminosity is dominated by production at 5–15 km: 59.13% comes from 5–10 km and 37.43% from 10–15 km. The 20–25 km production shell contributes 3.36%; the 0–5 km and 15–20 km source shells together contribute less than 0.1%.

## 5. Direction dependence

The path calculation also confirms strong angular dependence. For a 19.545 MeV mediator emitted at \(r=24\) km:

| Direction cosine \(\mu\) | Total optical depth | Escape probability |
|---:|---:|---:|
| \(-0.9\), inward | 83.78 | \(4.13\times10^{-37}\) |
| \(+0.9\), outward | 3.77 | \(2.30\times10^{-2}\) |

The outward ray traverses only the short outer segment, whereas the inward ray crosses a much longer column. This angular structure is included in the independent average; it is not replaced by a radial-only escape estimate.

## 6. Conclusions and decision

1. **Eq. (B.2) path geometry is independently implemented and validated.** The impact-parameter representation correctly handles inward and outward directions.
2. **The existing 32-node path quadrature is sufficiently accurate for the integrated 10 MeV luminosity.** Its replacement changes the full luminosity by at most \(4.31\times10^{-5}\).
3. **The angular integral is converged.** The 128-to-256 change at the high-coupling endpoint is \(8.20\times10^{-9}\).
4. **The 15–25 km outer neutrino opacity is a genuine and quantitatively important contribution.** Its independently recomputed share of the source-weighted mean neutrino optical depth is 63.1173%, but this does not by itself determine the escaped luminosity.
5. **The 92.2469% high-coupling Fig. 7 residual remains.** It is not explained by the numerical path or angular integration. No chemical potential, local rate, or opacity is retuned.

The next investigation should therefore move outside the already validated path quadrature: first audit the energy convention and the digitized 10 MeV Fig. 7 tail against the paper's exact definitions, then assess the reconstructed-profile/fixed-background limitation. The local collision kernels and the Eq. (B.2) numerical integration should remain frozen during that work.

## 7. Reproducibility

- Independent implementation: **audit_eq_b2_path_integral.py**
- Regression tests: **test_eq_b2_path_integral.py**
- Machine-readable results: **outputs/eq_b2_independent_path_integral_2026-11-08.json**
- CI: [Independent Eq B2 path integral audit](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42404085661)
- Full regression/reproducibility validation: [Major 4.4 EFT numerical validation](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42404088631)

This is an internal research validation only. It does not modify the manuscript, referee response, production rates, transport outputs, or axial constraint figures. PR #56 remains Draft.
