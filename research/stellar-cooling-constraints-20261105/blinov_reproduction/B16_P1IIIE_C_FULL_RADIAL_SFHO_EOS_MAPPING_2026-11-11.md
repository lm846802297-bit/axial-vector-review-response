# P1-IIIe-C: full radial Caputo-to-SFHo EOS mapping

Date: 2026-11-11  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## Scope

This report maps 301 points from the 0.05-km Caputo SFHo-18.8 published-figure snapshot at t_pb=1 s onto the official SFHo/FRDM v1.03 tables. The radial interval is 0.200--15.200 km. It is not a raw time-dependent Garching simulation profile.

The EOS coordinate is Yp_tot = Ye + Ymu; the free-proton abundance Yp is not used as the EOS coordinate.

## Interpolation and boundary checks

Trilinear interpolation is performed in (log10 T, Yp_tot, log10 nB) with bounds_error=True, using only the 308 physical density rows. No extrapolation is permitted.

| Table axis | Table range | Profile range | Lower margin | Upper margin |
|---|---:|---:|---:|---:|
| extended_eos: log10_T_MeV | [-1, 2.2] | [1.0935743, 1.5937413] | 2.0935743 | 0.60625865 |
| extended_eos: Yp_tot | [0, 0.6] | [0.069491825, 0.21822336] | 0.069491825 | 0.38177664 |
| extended_eos: log10_nB_fm3 | [-12, 0.28] | [-1.6146589, -0.4514227] | 10.385341 | 0.7314227 |
| single_particle: log10_T_MeV | [-1, 2.1999999] | [1.0935743, 1.5937413] | 2.0935743 | 0.6062586 |
| single_particle: Yp_tot | [0.01, 0.6] | [0.069491825, 0.21822336] | 0.059491825 | 0.38177664 |
| single_particle: log10_nB_fm3 | [-12, 0.28] | [-1.6146589, -0.4514227] | 10.385341 | 0.7314227 |

## Composition closure

| Quantity | RMS absolute residual | Maximum absolute residual |
|---|---:|---:|
| Xn_EOS - Yn_Caputo | 2.18833e-05 | 0.000253239 |
| Xp_EOS - Yp_Caputo | 1.52415e-05 | 0.000183992 |
| Xcluster_EOS - Xcluster_Caputo | 3.66622e-05 | 0.000437231 |
| cluster charge | 1.52415e-05 | 0.000183992 |

The SPP filling factor is compared with the value inferred independently from the free-nucleon and total baryon densities:

- RMS absolute xi residual: 6.47154e-05
- Maximum absolute xi residual: 0.00043831
- Maximum EOS cluster-component closure residual: 3.33067e-16

## C2 handoff

The radial table contains m*_n, m*_p, SigmaV_n, SigmaV_p, mu_n^nonrel, mu_p^nonrel, xi, and the individual cluster fractions. It also records the Hempel scalar potentials U_N = m*_N - m_N + SigmaV_N. No phase-space occupation or degeneracy integral is evaluated in this C1 mapping.

Free neutron, free proton, and cluster baryon densities are stored separately. The identity n_n + n_p = nB is never imposed.

## Acceptance

Overall C1 acceptance: **PASS**.

The machine-readable acceptance criteria and full provenance are in the accompanying JSON. No dynamic response, B.2 opacity, pure-vector Fig. 7 result, axial cooling curve, manuscript, or referee response is modified.
## 7. Independent review qualification (2026-11-15)

The full-profile workflow run #42960145972 completed successfully. Its relevant steps passed: profile-builder/interpolation-helper tests, the full 301-point mapping onto the official SFHo EOS grid, and the radial/domain/composition/filling-factor acceptance gates. The workflow pins the Caputo arXiv source archive SHA-256 and all three official SFHo/FRDM v1.03 table hashes before mapping.

The interpolation coordinates and boundaries are correctly distinguished: \((\log_{10}T,Y_p^{\rm tot},\log_{10}n_B)\), with \(Y_p^{\rm tot}=Y_e+Y_\mu\), 308 physical density rows, and bounds_error enabled. The 301 points remain within the EOS domains, so no extrapolation is used. The composition and filling-factor residuals are small compared with the explicit 5e-3 acceptance gates.

The workflow and the mapping code are a clean reproducible pipeline, but the source profile itself is still a published-figure reconstruction: \(T(r)\), \(n_B(r)\), and composition are extracted/interpolated from Caputo Fig. 1/Fig. 4. It is not a raw Garching snapshot, mass-time sequence, or independent simulation output. The map validates internal consistency of this reconstructed snapshot with the official EOS tables; it does not authenticate the missing raw archive fields.

**Review disposition: PASS_WITH_NOTES.** The 301-point C1 mapping is accepted within its figure-derived snapshot scope. No dynamic response, B.2 opacity, Fig. 7 luminosity, or axial-vector limit follows from the EOS mapping alone.
