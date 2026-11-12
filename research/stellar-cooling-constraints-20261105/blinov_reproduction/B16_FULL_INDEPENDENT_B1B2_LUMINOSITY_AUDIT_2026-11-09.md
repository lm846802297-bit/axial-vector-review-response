# End-to-end independent B.1+B.2 luminosity audit (10 MeV vector benchmark, 2026-11-09)

## Executive conclusion

The optically-thin B.1 source integration and the analytic B.2 chord integration have now been combined into a single independent end-to-end luminosity calculation. For every source radius, the calculation inserts the exact threshold \(\omega_{\min}=m_V/N(r)\), evaluates the local production and reduced-absorption kernels at the new energy quadrature nodes, computes the direction-dependent optical depth with the analytic piecewise-linear chord integral, and performs the full angular escape average.

The calculation reproduces the archived B.16 fixed-\(\omega\) luminosity curve to:
- maximum absolute relative difference: \(0.4451\%\);
- mean absolute relative difference: \(0.3975\%\).

However, it still differs from the digitized Fig. 7 curve by:
- weak-coupling endpoint: \(-9.2908\%\);
- reference peak: \(+2.1522\%\);
- strong-absorption endpoint: \(+92.0542\%\).

Thus the original B.16 numerical implementation and the independent B.1+B.2 implementation agree at the sub-percent level, while both retain essentially the same order-one strong-coupling discrepancy against Fig. 7. The discrepancy is not caused by the old B.1 energy/radial quadrature or the old B.2 path-length quadrature, conditional on the shared profile, local kernels, and fixed-\(\omega\) prescription.

## 1. Full luminosity expression

The calculation evaluates
\[
L_V(g)=g^2\int_0^{R_{\max}}dr\,4\pi r^2N(r)^2
\int_{m_V/N(r)}^{\omega_{\max}}d\omega\,
\frac{k\omega^2}{2\pi^2}
\Gamma_{\rm prod}(r,\omega)
\left[\frac12\int_{-1}^{1}d\mu\,
e^{-g^2\tau(r,\omega,\mu)}\right],
\]
where
\[
k=\sqrt{\omega^2-m_V^2},\qquad
\tau(r,\omega,\mu)=\frac{1}{v_V}
\int_0^{s_{\max}}ds\,
\Gamma_{\rm abs}^{*}(r'(s),\omega).
\]
The literal Appendix-B fixed-\(\omega\) prescription and Euclidean straight-chord geometry are retained.

## 2. Independent numerical construction

### 2.1 Source radial quadrature

The B.1 source uses equal-width radial panels with four-point Gauss--Legendre integration:
- coarse check: 25 panels, 100 source nodes;
- final check: 50 panels, 200 source nodes.

The source nodes themselves, together with \(r=0\) and \(R_{\max}=25\) km, form the radial opacity interpolation grid. The final opacity grid therefore contains 202 radial nodes.

### 2.2 Exact-threshold energy quadrature

At each source radius,
\[
\omega_{\min}(r)=m_V/N(r)
\]
is inserted exactly. The energy variable is
\[
x=\ln[(\omega-m_V)/(1\ {\rm MeV})],
\qquad d\omega=(\omega-m_V)dx.
\]
Each source radius uses 80 logarithmic panels with four Gauss--Legendre nodes per panel, giving 320 energy nodes per source radius. The energy upper limit is 2010 MeV.

The local production kernels are evaluated directly at these new nodes. The reduced absorption profile is evaluated at every point of the 202-node opacity grid for the same source-energy nodes.

### 2.3 Independent B.2 propagation

For each source radius and energy quadrature:
1. Construct \(\Gamma_{\rm abs}^{*}(r_j,\omega)\) on the 202-node opacity grid.
2. Use the analytic \(z=s+r\mu\) chord integral, splitting at every opacity interpolation knot.
3. Evaluate 16 Gauss--Legendre directions.
4. Form \(\mathcal O_g(r,\omega)=\frac12\sum_a w_a e^{-g^2\tau_a}\) for all 25 Fig. 7 coupling vertices.
5. Integrate the source spectrum times this escape factor.

No legacy \`eq_b1_source_measure\`, \`energy_weights\`, \`radial_rule\`, \`scalar_optical_depths\`, or path-length Gauss quadrature is used.

## 3. Frozen inputs and reproducibility

- Mediator mass: 10 MeV.
- Outer radius: 25 km.
- Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.
- Source radial nodes: 200.
- Opacity radial nodes: 202.
- Energy nodes per source radius: 320.
- Angular nodes: 16.
- Coupling vertices: 25, copied from the digitized Fig. 7 reference.
- Energy upper limit: 2010 MeV.
- Local production/absorption kernels: shared with the reference implementation.
- Production axial-vector outputs: unchanged.

## 4. B.1 source closure

The full calculation's 200-node optically-thin source is
\[
L_{\rm thin}^{200r}=4.30427601\times10^{70}
\ {\rm erg\,s^{-1}}\quad\text{per }g^2.
\]
The independent B.1 source audit at 400 radial nodes gives
\[
L_{\rm thin}^{400r}=4.30436817\times10^{70}
\ {\rm erg\,s^{-1}}\quad\text{per }g^2.
\]
The difference is \(-0.002141\%\), consistent with the source-only radial convergence study.

The final 200-node channel fractions are:
- neutrino inverse decay: 67.9324%;
- muon-Compton: 32.0676%;
- dimuon inverse decay: 0% (kinematically closed at 10 MeV).

## 5. Full-luminosity radial convergence

The full B.1+B.2 calculation is repeated with 100 and 200 source radial nodes, keeping 80 logarithmic energy panels, four energy Gauss nodes per panel, and 16 angular nodes.

The maximum absolute luminosity shift over all 25 couplings is \(0.19867\%\); the mean absolute shift is \(0.08042\%\). The largest change occurs at the strong-absorption endpoint. This is below the 1% screening target adopted for the current global numerical audit.

## 6. Comparison with the archived B.16 calculation

| Metric | Independent full B.1+B.2 vs archived B.16 |
|---|---:|
| Mean absolute relative difference | 0.39753% |
| Maximum absolute relative difference | 0.44506% |
| Weak-coupling endpoint | -0.44506% |
| Reference peak | -0.40617% |
| Strong-absorption endpoint | -0.09699% |

The full independent integration therefore recovers the archived B.16 curve to better than 0.45% over all 25 coupling points. In particular, the strong-endpoint result differs from the archived calculation by only about 0.097%, while both calculations remain about 92% above the digitized Fig. 7 value.

## 7. Comparison with Fig. 7

| Fig. 7 comparison point | Independent full B.1+B.2 |
|---|---:|
| Weak-coupling endpoint | -9.2908% |
| Reference peak | +2.1522% |
| Strong-absorption endpoint | +92.0542% |
| Mean absolute relative difference over 25 points | 15.8856% |
| Maximum absolute relative difference over 25 points | 92.0542% |

The 25-point residual is not a single-point artifact: the discrepancy grows systematically through the strong-absorption branch. The independent B.1+B.2 implementation does not remove or materially change this behavior.

## 8. Interpretation

Established:
1. The independent B.1 source and B.2 propagation routines can be combined without a numerical closure problem.
2. The full independent calculation agrees with archived B.16 to better than 0.45% at all 25 coupling points.
3. The source integral agrees with the independent 400-node B.1 audit to 0.00214%.
4. The full luminosity changes by at most 0.1987% when the source radial nodes are doubled from 100 to 200.
5. The order-one strong-coupling mismatch with Fig. 7 persists in an independent end-to-end implementation.

Not established:
1. The reconstructed profile is not the original Garching s18.8-SFHo-MUONS simulation table.
2. The local production/absorption kernels are shared; this integration does not independently re-derive all collision amplitudes or approximations.
3. The fixed-\(\omega\) versus conserved-energy interpretation remains a separate physical issue.
4. The Euclidean straight-chord prescription is not full general-relativistic ray tracing.
5. The result is a pure-vector Appendix-B benchmark, not a new axial-vector constraint.

The next investigation should therefore focus on the physical inputs and conventions that are shared by both implementations, especially the original stellar profile and the energy/redshift prescription. No empirical rescaling of the opacity, source, or luminosity is justified.

## 9. Reproducibility

- GitHub Actions: [Run #42564417076](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42564417076)
- Script: \`audit_b16_b1b2_full_independent.py\`
- Unit tests: \`test_b16_b1b2_full_independent.py\`
- Workflow: \`.github/workflows/b16-full-b1b2-independent.yml\`
- Machine-readable output: \`outputs/b16_full_b1b2_independent_10mev_2026-11-09.json\`
