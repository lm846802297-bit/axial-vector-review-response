# Profile-version reconciliation for the B.1/B.2 vector benchmark

Date: 2026-11-09  
Status: **the latest extraction is the current working input. The earlier 501-node uniform profile and the vertex-preserving profile give numerically indistinguishable integrated B.1/B.2 results at the 10 MeV benchmark, despite visible local differences near retained support boundaries. A subsequent vertex-preserving re-extraction changed only last-digit floating-point serialization in the active thermodynamic columns; B.16 outputs from the immediately preceding fingerprint remain physically equivalent and retain their actual run SHA.**

## 1. The two profile versions

The repository contains two distinct generated versions of the reconstructed public-figure SFHo-18.8 profile:

| Version | SHA-256 | CSV rows | Meaning |
|---|---|---:|---|
| Uniform-grid version | `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9` | 501 | 0.05 km uniform base grid |
| Vertex-preserving version | `6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc` | 1687 | Uniform base grid plus retained PDF vertices and support-boundary knots |

The current 1687-row file is a union grid:
\[
\mathcal R_{\rm current}
=
\mathcal R_{\rm uniform}
\cup
\mathcal R_{\rm PDF\ vertices}
\cup
\mathcal R_{\rm support}.
\]

It contains 501 base-grid points and 1186 unique additional rows after deduplication. In 22--25 km, the 61 base-grid points are supplemented by 161 retained source/support nodes, giving 222 total nodes. The minimum adjacent spacing in this shell is \(6.7778140\times10^{-7}\) km; the maximum remains 0.05 km. The very small intervals are intentional near-step support-boundary knots, not additional supernova simulation snapshots.

The extra vertices are reconstructed from published figure paths. Neither CSV version is the original s18.8-SFHo-MUONS Garching simulation table.

## 2. Local profile differences

The two files were compared by linear interpolation on a dense common radial mesh.

| Region | Quantity | Maximum absolute difference | Maximum relative difference |
|---|---|---:|---:|
| 12--15 km | \(T\) | 0.002795 MeV | 0.02067% |
| 12--15 km | \(\mu_\mu\) | 0.20758 MeV | 0.32672% |
| 12--15 km | lapse | \(4.19\times10^{-6}\) | 0.000489% |
| 22--25 km | \(T\) | 0.0007773 MeV | 0.02225% |
| 22--25 km | \(\mu_\mu\) | 0.66291 MeV | up to 126.77% where the old value is small |
| 22--25 km | lapse | \(4.09\times10^{-6}\) | 0.000447% |

The largest local \(\mu_{\nu_\mu}\) difference in 12--15 km occurs at the support boundary near \(r=13.11\) km:
\[
\mu_{\nu_\mu}^{\rm uniform}(13.11\ {\rm km})
\simeq -0.82318\ {\rm MeV},
\qquad
\mu_{\nu_\mu}^{\rm vertex}(13.11\ {\rm km})=0.
\]
The uniform grid smears the branch endpoint into the adjacent 0.05 km cell, whereas the vertex-preserving grid retains the cutoff. This is a real local interpolation difference and must remain explicit.

In 22--25 km, the largest relative \(\mu_\mu\) difference occurs where the old value is small; the maximum absolute difference is 0.663 MeV. The current outer-profile audit separately checks the effect of this reconstructed profile on the B.2 path columns.


### 2.1 Latest extraction fingerprint refresh

After the B.16 full-path and Fig. 7 workflows ran on profile A, the profile-extraction workflow regenerated the same vertex-preserving grid as profile B. The CSV SHA changed, but the active B.1/B.2 thermodynamic columns did not undergo a physical update:

| File/column | Changed rows | Maximum absolute difference |
|---|---:|---:|
| SFHo \(T(r)\) | 11 | \(1.05\times10^{-13}\) MeV |
| SFHo \(\mu_\mu(r)\) | 8 | \(1.22\times10^{-13}\) MeV |
| SFHo \(\mu_{\nu_\mu}(r)\) | 0 | exactly unchanged |
| SFHo lapse | 0 | exactly unchanged |
| Caputo \(T(r)\) vertices | 4 | \(1.78\times10^{-15}\) MeV |
| Caputo \(n_\mu/n_0\) vertices | 1 | \(6.94\times10^{-18}\) |

The SFHo radial coordinates and node count are unchanged. The auxiliary Ferreira comparison columns contain no new finite-value changes; the file-level hash also responds to their serialized representation. Thus profile A and profile B are the same physical reconstructed background to floating-point precision in the fields used by the B.1/B.2 calculations.

The B.16 full-path, fixed-\(\omega\) Fig. 7, and outer-shell mode-resolved outputs retain profile A's exact SHA because that is what those runs actually used. The current B.13 exact-Compton output uses profile B's SHA. These results are physically consistent at the precision of the active inputs, but their distinct file fingerprints are preserved rather than rewritten.

The extraction script now writes `profile_csv_sha256` into `profile_provenance.json`, and the data README records the latest fingerprint. This makes future extraction refreshes auditable.

## 3. Full-path B.2 comparison at \(m_V=10\) MeV

The complete channel-by-shell-by-direction audit was rerun with the current vertex-preserving profile. The comparison with the earlier 501-node output is:

| Quantity | Uniform-grid profile | Vertex-preserving profile |
|---|---:|---:|
| B.1 source fraction from 8--15 km | 79.6117205% | 79.6114338% |
| Strong-endpoint \(P_{\rm esc}\), all emission radii | \(3.2393267\times10^{-4}\) | \(3.2393538\times10^{-4}\) |
| Strong-endpoint \(P_{\rm esc}\), 8--15 km emission | \(3.5333206\times10^{-4}\) | \(3.5333093\times10^{-4}\) |

The integrated shell-removal tests are also stable.

### All emission radii

| Removed shell | Uniform-grid luminosity factor | Vertex-preserving luminosity factor |
|---|---:|---:|
| 12--15 km | 2.92626 | 2.92624 |
| 22--25 km | 4.07285 | 4.07286 |

### Dominant 8--15 km emission region

| Removed shell | Uniform-grid luminosity factor | Vertex-preserving luminosity factor |
|---|---:|---:|
| 12--15 km | 3.04695 | 3.04695 |
| 22--25 km | 2.62660 | 2.62660 |

For the dominant 8--15 km emission region, the channel-specific leave-one-shell-out changes in the 12--15 km shell remain 59.306% for \(\nu_\mu\) inverse decay and 59.320% for \(\nu_\tau\) inverse decay. These nonlinear counterfactual changes are not additive.

The integrated B.1/B.2 observables therefore remain stable under the profile-version update at the precision relevant to the present Fig. 7 diagnosis. The local \(\mu_{\nu_\mu}\) support-boundary difference is real, but it does not materially change the source-weighted full-path escape probability in this benchmark.

## 4. Which outputs are current and which are historical

Use the following version assignment:

- **Current vertex-preserving profile, SHA `6c47d071...`:**
  - `outputs/b16_outer_profile_inputs_10mev_2026-11-08.json`
  - `outputs/b16_directional_escape_8_15km_10mev_2026-11-08.json`
  - `outputs/b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json`
  - `outputs/b16_outer_shell_polarization_resolved_10mev_2026-11-09.json`
- **Historical uniform-grid profile, SHA `08d7afce...`:**
  - `outputs/b16_inner_path_channel_directional_10mev_2026-11-09.json`
  - the earlier 501-node outer-profile and angular-distribution outputs
  - the earlier local-absorption samples and Fig. 7 re-evaluation report

The historical outputs are retained for auditability. They are not deleted or silently relabelled as current-profile results.

## 5. Decision

1. Use the latest vertex-preserving 1687-row profile B as the current reconstructed background input. Preserve profile A's B.16 outputs with their original SHA and interpret them as the same active physical background to floating-point precision.
2. Keep the 501-row results as a historical comparison.
3. Do not remove the near-step support-boundary nodes or smooth the \(\mu_{\nu_\mu}\) cutoff.
4. Do not rescale \(T\), chemical potentials, density, B.1 source, B.2 opacity, or luminosity.
5. Keep the original Garching-background limitation explicit.
6. Do not update the axial-vector curve until the pure-vector Fig. 7 baseline is re-evaluated on this same current profile.

This reconciliation establishes that the previous integrated shell conclusions are robust to the profile-grid refinement; it does not establish that the reconstructed public-figure profile is identical to the original supernova simulation.
