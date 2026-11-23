# Fig. 7 10 MeV: first-order channel sensitivity of the escaping luminosity

**Scope:** the pure-vector 10 MeV curve of Blinov et al., [arXiv:2511.09619v2, Fig. 7 and Appendix B](https://arxiv.org/html/2511.09619v2), evaluated on the same 25 archived visible vertices as [#121](https://github.com/lm846802297-bit/axial-vector-review-response/pull/121). Use the literal B.1 source with the lapse-squared volume measure and lower local energy $m_V/N(r)$, and fixed-energy (fixed `omega`) Euclidean-chord scalar B.2 transport. Retain the reference no-recoil B.14–B.19 semi-Compton and B.7–B.10 neutrino kernels. Here the profile is the archived public-figure reconstruction of SFHo‑18.8 at 1 s, not the original simulation table. This is not the [#123](https://github.com/lm846802297-bit/axial-vector-review-response/pull/123) Croon/C1 adaptive transport validation, an exact B.13 moving-muon calculation, a path-redshift-only variant, or a full GR ray trace. No luminosity, source, opacity, stellar profile or bound was tuned or changed.

## Calculation

At any archived coupling, write $L=g^2\int (J_\nu+J_C)e^{-(\tau_\nu+\tau_C)}\,d\mu$, where $d\mu$ includes the angular quadrature, $J_i$ is its nonnegative B.1 source contribution per $g^2$, and $\tau_i=g^2 C_i$ is its reduced B.2 chord optical depth at the **actual** coupling. The dimuon channel is closed. $J_i$ already includes the B.1 source quadratures. A logarithmic derivative with respect to the rate of channel $i$, evaluated at its unchanged value (no alternate curve generated), separates into:
- **Source only:** $+\int J_i e^{-\tau}\,d\mu/\int J e^{-\tau}\,d\mu$, i.e. the escaping source fraction; it is not the optically thin source fraction.
- **Opacity only:** $-\int J e^{-\tau}\tau_i\,d\mu/\int J e^{-\tau}\,d\mu$. Weight depth by the *escaping* population, not the unattenuated source.
- **Same-channel joint differential:** the sum. This tangent changes production and reduced absorption in the same channel coherently at fixed thermodynamics, as required for a multiplicative change in its microscopic rate under detailed balance. The separated terms are diagnostics, not proposed independent physical replacements.

The two matched tangents sum to $1-\langle\tau\rangle_{\rm esc}=\tfrac12\,d\ln L/d\ln g$. In the shape variable $x=(g/g_*)^2$ of #121 the exact negative slope of $\ln(L/g^2)$ is $\langle\tau\rangle_{\rm esc}/x$; the archive's discrete secant for each interval must lie between its two analytic endpoint slopes.

## Results

Values are logarithmic derivatives. “Peak” is the digitized **published** peak vertex, not the numerical model's continuous maximum.

| Fig. 7 vertex | Channel | Source only | Opacity only | Same-channel joint |
|---|---|---:|---:|---:|
| $4.79643\times10^{-10}$ | Neutrino inverse decay | +0.679173 | −0.001913 | +0.677260 |
| weak | Semi-Compton | +0.320827 | −0.000218 | +0.320609 |
| $1.13411\times10^{-8}$ | Neutrino inverse decay | +0.645337 | −0.823051 | −0.177714 |
| reference peak | Semi-Compton | +0.354663 | −0.110564 | +0.244099 |
| $4.17169\times10^{-8}$ | Neutrino inverse decay | +0.541103 | −4.544263 | −4.003160 |
| last visible | Semi-Compton | +0.458897 | −0.750097 | −0.291200 |

Neutrino and semi-Compton thin-source fractions are 0.679259 and 0.320741 for all vertices. The new curve-wide separation is that the matched neutrino-channel tangent reverses sign before the reference peak (two adjacent vertices $g=9.41558\times10^{-9}$ and $1.13411\times10^{-8}$); the matched semi-Compton tangent is still positive there and reverses sign later (adjacent vertices $2.38719\times10^{-8}$, $2.87538\times10^{-8}$). These are sign brackets on the sampled grid, not fitted zero locations or claims of uniqueness in a continuum. At the strong endpoint, $d\ln L/d\ln g=-8.58872$. The strong-end opacity moments reproduce the previously archived [B.2 channel-resolved endpoint diagnostic](https://github.com/lm846802297-bit/axial-vector-review-response/blob/a7ac6456dafb27492183912fe4abbaa73a9455f7/research/stellar-cooling-constraints-20261105/blinov_reproduction/B2_CHANNEL_RESOLVED_OPACITY_AUDIT_2026-11-10.md); the new result is the matched comparison at **all** 25 vertices and its compatibility with the coupling shape.

At the very weak end the unmodified model's optically thin luminosity is 0.91045 of the plotted value, so reducing absorption alone still cannot reconcile it. In the last visible tail, the strong sensitivity to neutrino depth does **not** identify an incorrect neutrino rate, any needed correction factor, or a cause of the mismatch; the joint differential is local, and the published curve has no channel-resolved source or optical-depth information. The strict last-vertex residual remains +92.4284%. No physical or transport parameter was varied in the native Fig. 7 run.

## Reproducibility

All three original high-order grid hashes (B.1 source radius, B.2 opacity radius, energy) match exactly on Python 3.12.14/NumPy 2.3.5/SciPy 1.17.0. Inversion of the archived spectral measure independently checks energy coordinates within $1.14\times10^{-13}$ MeV. Channel closure: source $4.42\times10^{-16}$ and opacity $7.83\times10^{-16}$ maximum elementwise relative error; all 25 restored luminosities agree to $4.45\times10^{-16}$ relative and all optically thin luminosities close exactly. The derivative sum closes to $8.89\times10^{-16}$; the 24 strict secants reproduce the #121 secants within $2.26\times10^{-10}$ absolute and satisfy the slope-bracket inequalities. The test runs also independently verify the tangent formula on one-ray and two-ray examples. This is a local replay using the frozen physical kernels, not a new independent derivation of them.

See `inputs/provenance.json` for Git blob IDs, file hashes, and exact refs. The `reference.py` snapshot agrees byte-for-byte with the historical hash in the archived high-order run. The wrapper snapshot `audit_b16_global_redshift.py` is pinned current-main source and is used **only** for its B.1 source measure and grid fingerprint helpers; it is not represented as the original archive-time wrapper. Couplings and plotted reference values are read from the pinned high-order and #121 native records and cross-checked exactly; no later figure-comparison file is substituted for the historical input.

```sh
sha256sum -c SHA256SUMS
OPENBLAS_NUM_THREADS=1 python -m unittest -v test_weighted
OPENBLAS_NUM_THREADS=1 python weighted.py /tmp/fig7-weighted-replay.json
cmp weighted-native.json /tmp/fig7-weighted-replay.json
```
