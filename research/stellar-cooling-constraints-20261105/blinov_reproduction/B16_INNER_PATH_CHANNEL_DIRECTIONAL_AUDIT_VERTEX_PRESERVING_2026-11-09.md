# B.16 inner-path channel, shell, and direction audit on the vertex-preserving profile
> **Current input fingerprint:** the final B.16 rerun and paired JSON use profile B SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. The immediately preceding vertex-preserving snapshot A (`6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc`) gave the same active thermodynamic inputs to floating-point precision; see `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`.


Date: 2026-11-09  
Status: **current-profile rerun completed.** This report supersedes the numerical use of the earlier 501-node uniform-profile audit while retaining that output as a historical comparison.

## 1. Fixed benchmark and input provenance

- Vector benchmark: \(m_V=10\) MeV.
- Coupling points: the weak endpoint, Fig. 7 peak, and strong endpoint from the archived Fig. 7 reference.
- Source weighting: B.1 source, with the dominant emission region reported separately as 8--15 km.
- Propagation: fixed \(\omega\) along each ray, following the printed B.2 prescription.
- Current reconstructed profile: `data/sfho188_digitized.csv`.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Profile size: 1687 rows, including the 501-point uniform base grid and retained PDF vertices/support-boundary knots.
- The 22--25 km shell contains 222 retained profile nodes.

This remains a public-figure reconstruction, not the original Garching simulation table.

## 2. Numerical method and closure

The calculation resolves the path into channel \(\times\) radial shell \(\times\) direction. The radial opacity is piecewise linear between retained profile nodes; the ray integral is evaluated with the analytic radial primitive. An independent direct path-coordinate quadrature is used as a cross-check.

| Check | Result |
|---|---:|
| B.1 production-channel sum maximum relative residual | \(4.01\times10^{-16}\) |
| B.2 reduced-absorption channel sum maximum relative residual | \(5.94\times10^{-16}\) |
| Angular-weight normalization residual | 0 |
| Analytic radial path vs direct path-coordinate quadrature, maximum relative residual | \(1.19179\times10^{-4}\) |
| Same comparison, source-weighted L1 relative residual for 8--15 km emission | \(2.09403\times10^{-6}\) |

The current-profile B.1 source fraction from 8--15 km is
\[
f_{8-15}=0.796114338.
\]

## 3. Strong-coupling escape probabilities

| Source region | \(P_{\rm esc}\) |
|---|---:|
| All emission radii | \(3.2393538\times10^{-4}\) |
| Dominant 8--15 km emission | \(3.5333093\times10^{-4}\) |

These are different source-weighted quantities and should not be interchanged.

## 4. Leave-one-shell-out sensitivity

The leave-one-shell-out results are nonlinear counterfactuals. The individual changes must not be added.

### All emission radii

| Removed shell opacity | \(L_{\rm no\ shell}/L_{\rm full}\) |
|---|---:|
| All channels in 12--15 km | 2.92624 |
| All channels in 22--25 km | 4.07286 |

The 22--25 km shell has the larger all-emission source-weighted sensitivity at this strong-coupling point.

### Dominant 8--15 km emission region

| Removed shell opacity | \(L_{\rm no\ shell}/L_{\rm full}\) |
|---|---:|
| All channels in 12--15 km | 3.04695 |
| All channels in 22--25 km | 2.62660 |

The ordering changes when the source is restricted to 8--15 km. This is why a shell ranking must always state the source region used.

### Individual inverse-decay channels

For the dominant 8--15 km source region:

| Removed channel and shell | Luminosity increase |
|---|---:|
| \(\nu_\mu\) inverse decay, 12--15 km | 59.3061% |
| \(\nu_\tau\) inverse decay, 12--15 km | 59.3201% |
| \(\nu_\mu\) inverse decay, 22--25 km | 59.6284% |
| \(\nu_\tau\) inverse decay, 22--25 km | 59.6284% |

For all emission radii, the corresponding individual channel changes are 56.18% and 56.19% in the 12--15 km shell, and 60.82% for either neutrino flavor in the 22--25 km shell.

The current profile gives zero Compton contribution to the 22--25 km shell at the numerical precision of this audit. Compton absorption remains relevant in the inner 8--15 km production/transport region.

## 5. Comparison with the 501-node profile

The earlier 501-node output and the current 1687-row vertex-preserving output give nearly identical integrated source-weighted escape probabilities and shell-removal factors. The profile-version comparison, including the local \(\mu_{\nu_\mu}\) cutoff difference, is recorded separately in `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`.

The local cutoff difference is retained; no profile smoothing or empirical opacity adjustment is introduced.

## 6. Reproducibility

Machine-readable current-profile output:

`outputs/b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json`

Related audits:

- `B16_OUTER_INPUT_AND_INVERSE_DECAY_AUDIT_2026-11-08.md`
- `B16_OUTER_SHELL_POLARIZATION_RESOLVED_AUDIT_2026-11-09.md`
- `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`
- `FIG7_VECTOR_BENCHMARK_REEVALUATION_2026-11-09.md`

No axial-vector production curve is regenerated or modified. No empirical rescaling of source, opacity, or luminosity is applied.
