# Independent analytic B.2 propagation audit on the vertex-preserving profile (2026-11-09)

## Executive conclusion

An independent B.2 propagation implementation has been completed and passed its GitHub Actions workflow. It does not reuse the existing path-integral routine to generate optical-depth columns. Instead, it changes the path variable to \(z=s+r\cos\theta\), splits each ray at every radial interpolation knot, and analytically integrates the piecewise-linear reduced opacity along each segment. The direction average is independently checked with Gauss--Legendre, composite Simpson, and adaptive QUADPACK integration.

With the same profile, local collision kernel, B.1 source measure, energy grid, and Fig. 7 reference as the archived B.16 calculation:

- The archived fixed-\(\omega\) baseline is reproduced to a maximum relative difference of \(1.11\times10^{-16}\).
- The analytic path integral changes the 25-point luminosity curve by at most \(4.31\times10^{-5}\) relative at the same 16 Gauss directions (0.00431%).
- Increasing the original path quadrature to order 128 brings its source-weighted RMS optical-depth residual against the analytic path integral to \(1.33\times10^{-5}\), and its maximum luminosity shift to \(1.40\times10^{-6}\).
- The Simpson-256 angular result differs from the archived B.16 curve by at most \(4.52\times10^{-5}\) relative (0.00452%).
- The independent curve still differs from Fig. 7 by -8.8853% at the weak endpoint, +2.5694% at the reference peak, and +92.2493% at the strong endpoint.

Therefore the order-one strong-endpoint mismatch is not caused by the numerical implementation of the fixed-profile, fixed-\(\omega\), Euclidean-chord B.2 path integral. This does not validate the physical profile, local collision approximations, B.1 source model, or the paper's energy convention; it isolates and strongly validates the B.2 numerical propagation step for the adopted inputs.

## 1. Published formula and independent variable change

The source is Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B. Equations (B.2)--(B.5) define the direction-averaged escape factor, the chord endpoint, the reduced absorption rate, and the vector speed.

For source radius \(r\), direction cosine \(\mu=\cos\theta\), and path length \(s\), the radial coordinate is
\[
r'(s)=\sqrt{r^2+s^2+2rs\mu},
\qquad
s_{\max}=-r\mu+\sqrt{R_{\max}^2-r^2+r^2\mu^2}.
\]
The optical depth is
\[
\tau(r,\omega,\mu)=
\frac{1}{v_V}\int_0^{s_{\max}}ds\,
\Gamma_{\rm abs}^*(r'(s),\omega),
\qquad
v_V=\sqrt{1-\frac{m_V^2}{\omega^2}}.
\]

Introduce
\[
z=s+r\mu,\qquad b=r\sqrt{1-\mu^2}.
\]
Then
\[
r'(s)=\sqrt{b^2+z^2},\qquad ds=dz,
\]
and the integration limits become
\[
z_0=r\mu,\qquad z_1=\sqrt{R_{\max}^2-b^2}.
\]
Thus
\[
\tau(r,\omega,\mu)=
\frac{1}{v_V}\int_{z_0}^{z_1}dz\,
\Gamma_{\rm abs}^*\!\left(\sqrt{b^2+z^2},\omega\right).
\]

## 2. Exact path integral for the adopted radial interpolation

The current profile and opacity table are represented by piecewise-linear interpolation in radius. On a segment between adjacent radial nodes,
\[
\Gamma_{\rm abs}^*(\rho,\omega)=A(\omega)+B(\omega)\rho.
\]
The path integral on that segment is analytic:
\[
\int dz\,\Gamma_{\rm abs}^*
=
A z+\frac{B}{2}
\left[
z\sqrt{z^2+b^2}
+b^2\operatorname{arsinh}\!\left(\frac{z}{b}\right)
\right].
\]
For \(b=0\), the continuous limit uses
\[
\int dz\,|z|=\frac12z|z|.
\]

The implementation inserts a segment boundary at every crossing
\[
z=\pm\sqrt{r_j^2-b^2}
\]
of a radial interpolation node \(r_j\), as well as at the turning point \(z=0\) for inward-going rays. It then sums the exact segment primitives. This avoids path quadrature error while preserving exactly the same piecewise-linear radial opacity convention as the reference implementation.

Unit tests compare the analytic integral against adaptive QUADPACK integration for outward, inward, near-radial, and central-crossing rays, and verify the constant-opacity chord-length limit.

## 3. Frozen inputs and independent scope

- Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.
- Mediator mass: 10 MeV.
- Source radial quadrature: 40 nodes.
- Energy grid: 142 nodes after adding the radius-dependent \(m_V/N(r)\) thresholds to the 100-point base grid.
- Outer radius: 25 km.
- Fig. 7 coupling vertices: 25.
- Baseline path and angular quadrature: \(N_s=32\), \(N_\Omega=16\).
- Independent angular comparisons: Gauss--Legendre orders 16, 32, 64; composite Simpson with 128 and 256 subintervals; 27 selected adaptive QUADPACK checks.

The local collision kernel, reconstructed profile, B.1 source measure, energy grid, and Fig. 7 vertices are deliberately shared with the archived B.16 benchmark. Only the B.2 propagation integration is independently implemented. This is a controlled algorithmic cross-check, not an independent re-derivation of the local rates or source normalization.

## 4. Same-grid baseline reproduction

The original B.2 path routine and the archived B.16 calculation agree at floating-point precision:
- Maximum relative difference over 25 coupling points: \(1.11\times10^{-16}\).
- Mean relative difference: \(4.44\times10^{-18}\).

This confirms that the comparison is made against the intended archived benchmark, not a changed energy grid, source measure, profile, or coupling array.

## 5. Path quadrature convergence

At the same 16 Gauss--Legendre direction nodes, the existing global path-length Gauss rule is compared with the analytic piecewise-linear path integral.

| Path order \(N_s\) | Maximum \(|\Delta\tau/\tau|\) | 99th percentile | Source-weighted RMS | Maximum luminosity shift |
|---:|---:|---:|---:|---:|
| 8 | 23.353% | 3.908% | 0.4356% | 0.12727% |
| 16 | 2.487% | 0.5230% | 0.05691% | 0.003075% |
| 32 | 0.5693% | 0.09774% | 0.01660% | 0.004307% |
| 64 | 0.2014% | 0.04232% | 0.005697% | 0.002444% |
| 128 | 0.07193% | 0.01152% | 0.001329% | 0.0001396% |

The maximum pointwise optical-depth residual is sensitive to a small subset of paths, while the source-weighted RMS and luminosity shifts are much smaller. The pointwise residual decreases systematically with path order. The small non-monotonicity in the integrated luminosity shift between orders 16, 32, and 64 reflects cancellation in the weighted integral; order 128 reduces the maximum luminosity shift to \(1.40\times10^{-6}\).

## 6. Independent angular integration

The analytic path columns are averaged over direction with three quadrature strategies.

| Angular rule | Resolution | Maximum luminosity shift relative to Gauss-16 |
|---|---:|---:|
| Gauss--Legendre | 32 | 0.002013% |
| Gauss--Legendre | 64 | 0.002242% |
| Composite Simpson | 128 subintervals | 0.002148% |
| Composite Simpson | 256 subintervals | 0.002168% |

For 27 selected \((r,\omega,g)\) combinations, the normalized angular escape average is also computed directly with adaptive QUADPACK. The maximum relative difference between Simpson-256 and QUADPACK is \(1.146\times10^{-6}\), or 0.0001146%.

The three source radii are the nearest quadrature nodes to 8, 12, and 15 km; the sampled energies are approximately 19.55, 52.29, and 99.02 MeV; the three distinct coupling values are approximately \(9.416\times10^{-9}\), \(1.982\times10^{-8}\), and \(4.172\times10^{-8}\).

## 7. Final independent luminosity curve

The final result uses the analytic path integral and Simpson-256 direction averaging.

| Fig. 7 comparison | Archived B.16 fixed-\(\omega\) | Independent analytic B.2 |
|---|---:|---:|
| Weak endpoint | -8.8853% | -8.8853% |
| Reference peak | +2.5688% | +2.5694% |
| Strong endpoint | +92.2406% | +92.2493% |
| Mean absolute relative difference | 15.73196% | 15.73265% |

The maximum relative difference between the final independent curve and the archived B.16 curve is \(4.521\times10^{-5}\), or 0.00452%. The difference in the strong-endpoint residual is only about 0.0087 percentage points.

The independent B.2 result therefore confirms the existing fixed-\(\omega\) propagation implementation. It does not improve the agreement with Fig. 7, and it provides no basis for rescaling the opacity or luminosity.

## 8. Interpretation and remaining uncertainty

Established:
1. The archived B.16 calculation is exactly reproduced on the same inputs.
2. The path integral is independently reproduced by an analytic segment integral.
3. The original path quadrature converges toward the analytic result.
4. Independent angular quadratures and adaptive QUADPACK agree.
5. The global luminosity is stable to much better than 0.01% under the independent B.2 implementation.

Not established:
1. The reconstructed public-figure profile is the original Garching simulation table.
2. The local B.6--B.19 collision approximations are physically exact; the independent local audit only checks their algebraic/numerical implementation.
3. The fixed-\(\omega\) versus conserved-energy convention is physically resolved. The path-redshift-only test remains a separate diagnostic and is not used here.
4. The Euclidean straight-chord geometry is a full GR ray trace; it is not.
5. The B.1 source measure and the underlying physical profile are independently re-derived by this B.2 test.

The current result rules out the B.2 path quadrature algorithm as the origin of the order-one strong-coupling discrepancy, conditional on the frozen profile, opacity table, B.1 source measure, and literal fixed-\(\omega\) Eq. (B.2) prescription. The next independent numerical layer is the B.1 source measure and its radial/energy quadrature, followed by a separate review of the physical energy convention and the public-profile reconstruction.

No production axial-vector output, coupling, source normalization, local opacity, profile value, or constraint curve is modified.

## 9. Reproducibility

- Workflow: [Run #42562585233](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42562585233)
- Script: \`audit_b16_path_independent.py\`
- Unit tests: \`test_b16_path_independent.py\`
- Machine-readable output: \`outputs/b16_path_independent_analytic_10mev_2026-11-09.json\`
- The workflow verifies that production axial-vector files remain unchanged.
