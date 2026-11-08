# B.2 outer-shell polarization-resolved inverse-decay audit
> **Current input fingerprint:** the final B.16 rerun and paired JSON use profile B SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. The immediately preceding vertex-preserving snapshot A (`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`) gave the same active thermodynamic inputs to floating-point precision; see `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`.


Date: 2026-11-09  
Status: **completed as a separate transport diagnostic.** The literal scalar B.2 implementation remains the Fig. 7 reproduction baseline; the mode-resolved result is not substituted for it.

## 1. Scope and current input

This audit isolates only the 22--25 km path segment. The source is held fixed to the B.1 production distribution from 8--15 km; all opacity inside 22 km is switched off in the reported escape factors.

- \(m_V=10\) MeV.
- Current profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.
- Full profile: 1687 retained rows; 222 profile nodes in 22--25 km.
- Source radial quadrature: 40 points.
- Energy grid: 143 points, including the exact direct-check energies.
- Mode-resolved rate quadrature: 48 points.
- Independent direct phase-space check: 512 points.
- Direction integration: four \(\cos\theta\) bins, 32-point Gauss quadrature per bin.
- The radial path integral uses the analytic primitive for the piecewise-linear opacity profile.

The input is a vertex-preserving public-figure reconstruction, not raw Garching simulation output.

## 2. Local polarization-resolved rates

The local rate code returns \(L,+,-\) contributions separately. In the outer shell, \(\mu_{\nu_\mu}=0\), so the two transverse modes agree. Across the sampled radii \(r=22,23,24,25\) km and energies \(\omega=12,15,20,30,50,100\) MeV:

\[
1.02313 \leq
\frac{\Gamma_{\rm abs,L}^{*}}
{\tfrac12(\Gamma_{\rm abs,+}^{*}+\Gamma_{\rm abs,-}^{*})}
\leq 1.09634.
\]

Thus the longitudinal/transverse difference is about 2.3--9.6% in these local samples. It is not itself an order-one polarization splitting.

The direct phase-space checks give:

| Check | Maximum relative residual |
|---|---:|
| 48-point mode production vs 512-point direct integration | \(1.71\times10^{-15}\) |
| 48-point mode absorption vs 512-point direct integration | \(1.66\times10^{-15}\) |
| Per-mode B.10 detailed balance | \(3.55\times10^{-14}\) |

Across the full energy grid, the mode-summed production and reduced absorption agree with the scalar reference to \(8.91\times10^{-8}\) maximum relative residual. The source-mode sum has \(8.41\times10^{-8}\) maximum relative residual. The path-column sum (three modes plus scalar Compton contribution) closes against the scalar path column to \(2.69\times10^{-8}\). The scalar neutrino-plus-Compton channel closure is \(4.90\times10^{-16}\).

## 3. Source polarization weights

The neutrino part of the 8--15 km B.1 source has mode fractions:

| Mode | Fraction of neutrino source |
|---|---:|
| \(L\) | 34.7638% |
| \(+\) | 31.7965% |
| \(-\) | 33.4398% |

The scalar Compton source contributes 33.2817% of the selected total source. Since the B.14--B.16 scalar approximation does not provide a mode-resolved Compton source, the full-source mode-resolved diagnostic splits this Compton source equally among \(L,+,-\). This is an explicit diagnostic assumption, not a new derivation of the Compton polarization density matrix.

The outer-shell Compton opacity is zero at the numerical precision of this benchmark. The outer-shell attenuation is therefore controlled by neutrino inverse decay.

## 4. Scalar versus mode-resolved propagation

The literal scalar implementation uses the mode-summed inverse-decay opacity in the B.2 exponent. The separate mode-resolved diagnostic propagates each mode with its own opacity and weights it with the corresponding neutrino production mode. A third comparison uses one-third of the mode-summed opacity as a polarization-averaged scalar rate.

All values below are outer-shell-only escape factors, not full-path escape probabilities.

| Coupling point | Literal scalar B.2 | Average-opacity comparison | Production-weighted mode-resolved |
|---|---:|---:|---:|
| Fig. 7 peak | 0.8261699 | 0.9363207 | 0.9362972 |
| Strong endpoint | 0.1503907 | 0.4678633 | 0.4678492 |

At the strong endpoint:
\[
\frac{P_{\rm esc}^{\rm mode}}
{P_{\rm esc}^{\rm scalar}}
=3.11089.
\]

The mode-resolved result agrees with the average-opacity comparison to about \(3.0\times10^{-5}\) relative. Therefore, the large difference from the literal scalar result is not caused by the 2--10% longitudinal/transverse splitting. It is dominated by the normalization convention: whether the scalar rate in the exponent is the sum over three modes or a per-vector polarization average.

### Direction bins at the strong endpoint

| \(\cos\theta\) interval | Literal scalar B.2 | Production-weighted mode-resolved |
|---|---:|---:|
| \([-1,-0.5]\) | 0.156394 | 0.476871 |
| \([-0.5,0]\) | 0.144387 | 0.458827 |
| \([0,0.5]\) | 0.144387 | 0.458827 |
| \([0.5,1]\) | 0.156394 | 0.476871 |

The equality between opposite-sign bins is consistent with the spherical background and the outer-shell chord geometry. The residual difference between grazing and more radial directions is retained; it is not replaced by an angular average before exponentiation.

## 5. Interpretation of the polarization convention

The printed equations require careful normalization bookkeeping:

- Eq. (B.6) sums over polarization states.
- Eq. (B.7) contains the explicit factor of three because the vacuum decay width is averaged over initial vector polarizations while the thermal production rate is summed.
- Eq. (B.10) states detailed balance between the production and absorption rates.
- Eq. (B.2) inserts a scalar \(\Gamma_{\rm abs}\) into the ray optical depth, but does not spell out a polarization-density-matrix propagation prescription.

The repository therefore keeps two objects separate:

1. **Literal scalar B.2 reference:** the mode-summed scalar rate is used in the exponent, matching the current printed-equation implementation and retained for Fig. 7 reproduction.
2. **Mode-resolved diagnostic:** each mode is attenuated with its own rate and its production weight. This is a physically informative alternative, but it is not silently substituted for the paper's scalar prescription.

The factor-of-three-scale difference is a convention/transport question that must be resolved from the authors' precise definition or implementation of \(\Gamma_{\rm abs}\). It is not evidence that the local B.2 phase-space integrals fail.

## 6. Decision

- The 22--25 km local inverse-decay rates, detailed balance, and direct phase-space integrals pass.
- The current vertex-preserving profile is used consistently.
- The literal scalar B.2 calculation remains the vector Fig. 7 reproduction baseline.
- The mode-resolved result is retained as a separate diagnostic; no empirical correction is applied.
- No axial-vector curve, production script, or published constraint is modified.

Machine-readable output:

\`outputs/b16_outer_shell_polarization_resolved_10mev_2026-11-09.json\`

Related records:

- \`B16_INNER_PATH_CHANNEL_DIRECTIONAL_AUDIT_VERTEX_PRESERVING_2026-11-09.md\`
- \`PROFILE_VERSION_RECONCILIATION_2026-11-09.md\`
- \`FIG7_VECTOR_BENCHMARK_REEVALUATION_2026-11-09.md\`
