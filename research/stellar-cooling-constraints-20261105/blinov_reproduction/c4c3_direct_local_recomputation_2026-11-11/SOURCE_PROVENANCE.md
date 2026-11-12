# Source provenance for the C4-C3 local recomputation

The local calculation used the source snapshot at commit
`780e0c0bfd745ec41cb7b840c7ba4f8226bb723d`.
That commit is an ancestor of PR #57 HEAD checked during preparation
(`55f64022634428bb43a13775bc70502cc70f7850`, 27 commits ahead).

The following source/input blobs were checked against the current PR tree and
match the SHA values recorded by the computation archive:

| Role | Repository path | Git blob SHA |
|---|---|---|
| C4-B2 effective-mass collision kernel | `research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel.py` | `97a2706e978cd22f7ebc08c1f87ce6abd97ad0a7` |
| C4-C1 exact outgoing-energy support | `research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support.py` | `8f7291be8738e0273353a8c30039c6be1ed8e6a9` |
| C4-C2 full-angle total scattering | `research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_p1iii_eos_c4c2_full_angle_total_scattering.py` | `2912788345e482e52308e02e6cbbc87c734a18b0` |
| SFHo EOS radial profile | `research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv` | `9ff7818b0679992c0a9ba402330ec7f0d1f3041b` |
| Full-radial EOS occupation | `research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/p1iii_eos_full_radial_occupation_2026-11-11.csv` | `c472040a4551e68ffadbf7addf9402663f99e7e3` |
| C4-C2 reference total rates | `research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/p1iiie_c4c2_full_angle_total_rates_2026-11-11.csv` | `881b6459e8d9a1ac867b0f4dc47ac168d454e488` |

The source snapshot is therefore already represented in the PR's Git history
and the required calculation inputs are already present at the exact recorded
blob revisions. To avoid duplicating 183 existing source files or replacing
newer branch files with an older snapshot, this result directory stores the
provenance rather than another nested source archive.
