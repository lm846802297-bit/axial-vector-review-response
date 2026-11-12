# B.16 outer-shell optical depth resolved by emission radius and direction

> **Historical profile version:** the paired numerical output for this report uses the 501-node uniform profile, SHA-256 `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9`. The current working input is the 1687-row vertex-preserving profile, SHA-256 `6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc`. The current-profile rerun and quantitative old/new comparison are documented in `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`; see also `outputs/b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json`. Keep this report as a historical record and do not combine its numerical output with current-profile results.


**Status:** step 3 completed; geometry tests and GitHub Actions passed.  
**Benchmark:** \(m_V=10\) MeV, fixed-\(\omega\) B.1/B.2, \(R_{\max}=25\) km.  
**Profile:** 0.05 km public-figure reconstruction, not the original raw Garching snapshot.  
**Source:** B.1 weights are held fixed; only the B.2 path opacity is evaluated.

## 1. Calculation

The source is restricted to \(8\leq r_{\rm em}\leq15\) km, which contributes 79.61% of the global B.1 source weight in this run. The three emission shells contribute:

| Emission shell | Fraction of the selected 8--15 km source |
|---|---:|
| 8--10 km | 50.17% |
| 10--12 km | 32.72% |
| 12--15 km | 17.12% |

For every source radius and direction, the impact parameter is
\[
b=r_{\rm em}\sqrt{1-\cos^2\theta}.
\]
The exact geometric path length in the outer shell is
\[
\Delta s_{22-25}(b)
=\sqrt{25^2-b^2}-\sqrt{22^2-b^2}.
\]
Across the selected source region and angular quadrature, it ranges from 3.0003 km to 3.8686 km.

The outer-shell optical-depth integral is evaluated directly in the radial coordinate,
\[
\tau_{22-25}(r_{\rm em},\cos\theta,\omega)
=\frac{1}{v_V}\int_{22\,{\rm km}}^{25\,{\rm km}}
\Gamma_{\rm abs}^{*}(r',\omega)
\frac{r'}{\sqrt{r'^2-b^2}}\,dr',
\]
using a 96-point Gauss rule. The inner path opacity is independently accumulated from the dense 0.05 km profile using the same fixed-\(\omega\) B.2 prescription. The final total column is the inner-shell sum plus the direct outer-shell integral.

The angular quadrature weights sum to unity and match the direct radial-shell integration exactly at stored precision. All opacity columns are nonnegative.

## 2. Source-weighted optical-depth distributions

The following are distributions over B.1 source radius and energy and over isotropic emission directions. Optical depths already include \(g^2\).

### Fig. 7 peak: \(g=1.13411\times10^{-8}\)

| Quantity | Median | 90th percentile | 99th percentile | Mean |
|---|---:|---:|---:|---:|
| Outer-shell \(\tau_{22-25}\), before escape weighting | 0.159 | 0.371 | 0.811 | 0.202 |
| Outer-shell \(\tau_{22-25}\), conditioned on full-path escape | 0.130 | 0.259 | 0.489 | 0.151 |
| Full-path \(\tau\), before escape weighting | 1.045 | 1.925 | 3.299 | 1.177 |

For the selected 8--15 km source, the outer-shell-only escape factor is 0.82585 and the full-path escape factor is 0.35431.

### Strong endpoint: \(g=4.17169\times10^{-8}\)

| Quantity | Median | 90th percentile | 99th percentile | Mean |
|---|---:|---:|---:|---:|
| Outer-shell \(\tau_{22-25}\), before escape weighting | 2.153 | 5.021 | 10.979 | 2.727 |
| Outer-shell \(\tau_{22-25}\), conditioned on full-path escape | 0.883 | 1.307 | 1.875 | 0.910 |
| Full-path \(\tau\), before escape weighting | 14.143 | 26.049 | 44.642 | 15.922 |

For the selected 8--15 km source, the outer-shell-only escape factor is 0.14996 and the full-path escape factor is \(3.5026\times10^{-4}\).

The strong-coupling escaped population is therefore highly selected: its median outer-shell optical depth is 0.883, substantially below the unattenuated source-weighted median 2.153. A single source-weighted mean optical depth cannot represent this nonlinear selection.

## 3. Emission-radius dependence

At the strong endpoint:

| Emission shell | Source fraction | Mean outer \(\tau\) before escape | Outer-shell escape factor | Full-path escape factor |
|---|---:|---:|---:|---:|
| 8--10 km | 50.17% | 2.199 | 0.1908 | \(3.988\times10^{-4}\) |
| 10--12 km | 32.72% | 2.781 | 0.1331 | \(3.770\times10^{-4}\) |
| 12--15 km | 17.12% | 4.169 | 0.06254 | \(1.570\times10^{-4}\) |

The 12--15 km sources have roughly twice the mean outer-shell optical depth of the 8--10 km sources. This is not just the geometric path-length effect: the local opacity and the impact parameter both vary with the emission radius. The direct calculation preserves both.

The emission-radius dependence also appears at the Fig. 7 peak, but is less severe: the outer-shell escape factors are 0.8551, 0.8216, and 0.7482 for the three successive shells.

## 4. Direction dependence

For the strong endpoint, the full-path escape probability in the selected source is:

| Direction bin | Source-weight fraction | Full-path escape probability |
|---|---:|---:|
| Inward radial, \(-1\leq\cos\theta<-0.8\) | 10.05% | \(8.74\times10^{-6}\) |
| Inward oblique, \(-0.8\leq\cos\theta<-0.2\) | 30.27% | \(1.40\times10^{-5}\) |
| Tangential, \(|\cos\theta|<0.2\) | 19.36% | \(1.10\times10^{-4}\) |
| Outward oblique, \(0.2\leq\cos\theta<0.8\) | 30.27% | \(5.89\times10^{-4}\) |
| Outward radial, \(0.8\leq\cos\theta\leq1\) | 10.05% | \(1.45\times10^{-3}\) |

The outer-shell-only escape factors for the same five bins are 0.1613, 0.1487, 0.1422, 0.1487, and 0.1613. The equality of inward/outward outer-shell factors at matched \(|\cos\theta|\) is expected: the outer-shell path depends on the impact parameter \(b\), hence on \(\cos^2\theta\).

**The large inward/outward asymmetry in the full escape probability is generated mainly by the inner path, not by the 22--25 km shell.** Inward-going vectors cross the denser inner region before reaching the outer shell. Outward-going vectors do not. The 22--25 km path itself changes much more mildly with direction.

This distinction is central: the outer shell is optically important, but its angular path-length variation is not responsible for the order-of-magnitude inward/outward difference.

## 5. Interpretation and next diagnostic

Three conclusions follow.

1. **The outer shell is important at strong coupling.** For the 8--15 km source, it alone reduces the escape factor to about 0.15.
2. **Emission radius matters.** Sources nearer 15 km accumulate appreciably larger outer-shell opacity than sources near 8--10 km.
3. **The dominant angular selection comes from the inner trajectory.** The full-path escape probability varies by more than two orders of magnitude between inward and outward radial bins, whereas the outer-shell-only escape factor varies by only about 13%.

The previous source-versus-escape diagnostic found that matching the Fig. 7 strong-endpoint luminosity requires an effective escape probability 0.5202 times the current value, corresponding to \(\Delta\tau_{\rm eff}=0.6536\). The present decomposition shows that this mismatch cannot be assigned to an assumed longer path through the 22--25 km shell: the geometric path is explicitly resolved and the inward/outward asymmetry is mostly accumulated inside 22 km.

**Step 4 should now compare the reconstructed radial inputs and path-opacity prescription against the original Blinov calculation and, if possible, the exact Garching snapshot.** In particular, compare the radial opacity \(\Gamma_{\rm abs}^{*}(r,\omega)\) in the inner 8--22 km region and the treatment of inward trajectories. Do not alter \(R_{\max}=25\) km, rescale the opacity, or change the source normalization.

## 6. Reproducibility

- Script: audit_b16_outer_escape_angular_distribution.py
- Tests: test_b16_outer_escape_angular_distribution.py
- Machine result: outputs/b16_outer_escape_angular_distribution_10mev_2026-11-08.json
- Workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42486733302
- Geometry tests and audit completed successfully.
- Production axial outputs were verified unchanged.
