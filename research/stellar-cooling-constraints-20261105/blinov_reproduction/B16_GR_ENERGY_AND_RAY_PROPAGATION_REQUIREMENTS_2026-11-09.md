# GR energy and ray-propagation requirements audit (2026-11-09)

## Executive conclusion

The independent B.1+B.2 calculation and the dense local-kernel audit are complete for the literal fixed-\(\omega\), Euclidean-chord Appendix-B prescription. The remaining energy-convention question cannot be promoted to a full GR transport calculation with the currently available profile.

A consistent static, spherically symmetric GR treatment requires both:
1. the lapse \(N(r)\), which determines the local energy from the conserved Killing energy;
2. the spatial metric function \(A(r)\), or equivalently the enclosed mass \(M(r)\) in areal-radius coordinates, which determines the proper path length and geodesic bending.

The public-figure reconstruction contains a lapse curve, but no independently tabulated \(A(r)\), enclosed-mass profile, or full metric for the same SFHo-18.8 snapshot. The Garching archive explicitly states that some archives are password protected, and the relevant Bollig radial-hydro-profile endpoint returns HTTP 401 Unauthorized. No restricted data or credentials are accessed.

Therefore:
- the literal fixed-\(\omega\) Appendix-B calculation remains the reproducibility baseline;
- the existing path-redshift-only calculation remains a diagnostic, not a full GR result;
- no approximate \(A(r)\) is invented or tuned to improve Fig. 7 agreement.

## 1. Static spherical metric and conserved quantities

For a static, spherically symmetric background in areal-radius coordinates, write
\[
ds^2=-N(r)^2dt^2+A(r)^2dr^2+r^2d\Omega^2.
\]
For a freely propagating massive vector, the conserved Killing energy is
\[
E_\infty=N(r)\,\omega_{\rm loc}(r).
\]
If the vector is emitted at radius \(r_s\) with local energy \(\omega_s\), then
\[
E_\infty=N(r_s)\omega_s,\qquad
\omega_{\rm loc}(r')=\omega_s\frac{N(r_s)}{N(r')}.
\]
The local momentum magnitude and speed are
\[
k_{\rm loc}(r')=\sqrt{\omega_{\rm loc}(r')^2-m_V^2},
\qquad
v_{\rm loc}(r')=\frac{k_{\rm loc}(r')}{\omega_{\rm loc}(r')}.
\]

The conserved angular momentum is fixed by the local emission angle \(\theta_s\):
\[
L=r_s k_s\sin\theta_s,
\qquad k_s=\sqrt{\omega_s^2-m_V^2}.
\]
The local radial momentum along the geodesic is
\[
p_{\hat r}(r')=
\sqrt{k_{\rm loc}(r')^2-\frac{L^2}{r'^2}}.
\]
Consequently,
\[
\frac{d\phi}{dr'}=
\frac{A(r')L}{r'^2p_{\hat r}(r')}.
\]
The proper spatial path element measured by local static observers is
\[
\frac{d\ell_{\rm loc}}{dr'}=
A(r')\frac{k_{\rm loc}(r')}{p_{\hat r}(r')}.
\]

## 2. GR optical depth

If \(\Gamma_{\rm abs}^*(r,\omega_{\rm loc})\) is the reduced absorption rate per local time, the optical depth along the geodesic is
\[
\tau_{\rm GR}=
\int_{\rm ray}\frac{d\ell_{\rm loc}}{v_{\rm loc}}\,
\Gamma_{\rm abs}^*\!\left(r',\omega_{\rm loc}(r')\right).
\]
On a monotonic outward radial segment this becomes
\[
\tau_{\rm GR}=
\int_{r_s}^{R_{\max}}dr'\,
A(r')\frac{\omega_{\rm loc}(r')}{p_{\hat r}(r')}
\Gamma_{\rm abs}^*\!\left(r',\omega_{\rm loc}(r')\right).
\]
Turning points and initially inward-going rays require piecewise geodesic integration. The angular average must be performed over the local emission angle at \(r_s\), with the corresponding conserved \(L\).

This expression identifies two distinct corrections relative to the current Appendix-B baseline:
- gravitational redshift of the local energy argument in the opacity;
- proper spatial path length and curved geodesic geometry through \(A(r)\).

A redshift-only correction changes the first item but not the second.

## 3. Inputs currently available

| Quantity | Current status | Consequence |
|---|---|---|
| \(N(r)\), lapse | Public-figure reconstruction; encoded through 23.9998 km, with a stated exterior continuation to 25 km | Usable for the existing redshift-only diagnostic, not an exact same-snapshot metric table |
| \(A(r)=\sqrt{g_{rr}}\) | Not present in the reconstructed CSV or the public figure set used here | Proper path length and geodesic bending cannot be computed exactly |
| \(M(r)\), enclosed mass | Not present in the current profile CSV | Cannot independently reconstruct \(A(r)\) |
| \(\rho(r),P(r)\), full hydro state | Not present as a raw same-snapshot table in the current working data | No controlled TOV reconstruction of the missing metric |
| \(T,\mu_\mu,\mu_{\nu_\mu}\) | Public-figure reconstruction, with the source-specific checks archived separately | Thermodynamic inputs remain figure-derived |

The current lapse cross-check against the independent SFHo-18.8 presentation is visual, not a machine-precision metric validation. It does not supply \(A(r)\).

## 4. Archive availability check

The Garching Core-Collapse Supernova Archive states that some archives are password protected and asks users to contact the archive maintainers for access. Its entry for the Bollig/Hüdepohl proto-neutron-star cooling simulations lists the relevant radial neutrino-moment and hydro-profile datasets. The specific hydro radial-profile endpoint for the Bollig archive returns HTTP 401 Unauthorized.

Sources:
- Garching archive access notice: https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/archive.html
- Relevant archive endpoint: https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/data/Bollig2016_radial_profiles/

No attempt is made to bypass the access restriction, reuse another person's access key, or substitute a different supernova model. No raw Garching data are obtained in this audit.

## 5. Existing energy-convention diagnostic

The earlier path-redshift-only diagnostic changes
\[
\omega_{\rm loc}(r')=\omega_s\frac{N(r_s)}{N(r')}
\]
inside the opacity kernel while retaining Euclidean straight chords. At 10 MeV it reduces the strong-endpoint discrepancy against Fig. 7 from approximately \(+92.24\%\) to \(+36.74\%\) in the earlier vertex-preserving calculation. It does not reproduce the reference curve and is not a full GR result.

The new independent full B.1+B.2 calculation validates the literal fixed-\(\omega\) implementation against the archived B.16 result to better than 0.45%. The dense local-kernel audit independently closes the local production and absorption formulae on all 64,000 global radius--energy nodes. These checks establish that the remaining difference is not an integration-code error within the adopted fixed-\(\omega\) prescription.

## 6. Decision and remaining work

1. Keep the literal fixed-\(\omega\), Euclidean-chord Appendix-B implementation as the paper-reproduction baseline.
2. Keep the path-redshift-only result as a separate sensitivity diagnostic; do not label it full GR.
3. Do not infer \(A(r)\) from the lapse alone and do not fit a metric to Fig. 7.
4. A full GR extension requires an authorized same-snapshot radial-hydro/metric table containing at least \(N(r)\) and \(A(r)\), or \(N(r)\) and \(M(r)\), plus a consistent mapping to the thermodynamic profile.
5. Without that input, the full GR energy/geometry issue is a documented data limitation rather than a numerically resolvable step.

The remaining profile-fidelity limitation is linked to the same data dependency: the 20--25 km thermodynamic continuation and the absolute density discrepancy cannot be resolved to raw-simulation precision using the currently public figure paths alone.

No source, opacity, coupling, luminosity, vector reference curve, or production axial-vector constraint is changed.
