# C4-C2 / C4-C3 status and local-rate audit — 2026-11-11

## C4-C2 result provenance

The C4-C2 full-angle total-scattering run is GitHub Actions run
[43011762069](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43011762069),
head `bb6d4fed74192f6451b0c8bca652a64bf4fac792`. Its uploaded artifact is
`c4c2-full-angle-total-scattering` (artifact ID `13853125900`).

The archived `local_total_rates.csv` contains 16 local cases at
`E_nu=100 MeV), four radii, neutron/proton targets, and neutrino/antineutrino
incoming states. The `gamma_total_available_volume_MeV` field is the rate
per available volume. The total-volume scattering coefficient is
`kappa_N = xi_SPP * gamma_N_available`; `xi_SPP` must be applied exactly once.

## Corrected four-radius comparison

The following table is reconstructed directly from the archived CSV. All
entries in the opacity columns include the tabulated `xi_SPP`.

| r (km) | kappa_n(nu) [MeV] | kappa_p(nu) [MeV] | kappa_total(nu) [MeV] | n/p (nu) | kappa_total(antinu) [MeV] | nu/antinu |
|---:|---:|---:|---:|---:|---:|---:|
| 0.2 | 2.3405204312e-13 | 1.0730592630e-13 | 3.4135796942e-13 | 2.1812 | 2.1976410231e-13 | 1.5533 |
| 5.0 | 3.3217139319e-13 | 1.3093040243e-13 | 4.6310179562e-13 | 2.5370 | 2.8774549116e-13 | 1.6094 |
| 10.0 | 3.4806010097e-13 | 6.7822483616e-14 | 4.1588258458e-13 | 5.1319 | 2.4979188021e-13 | 1.6649 |
| 15.2 | 7.1640151974e-14 | 2.8815214865e-15 | 7.4521673460e-14 | 24.8619 | 4.6472434641e-14 | 1.6036 |

Important correction to the preliminary conversational summary: the earlier
table mixed the available-volume rate and the total-volume opacity at the
10.0 and 15.2 km rows, and it showed only the neutrino target components
without clearly stating that the antineutrino channel is separate. The table
above uses one consistent convention throughout:
`kappa_N = xi_SPP * gamma_N_available`, with separate incoming neutrino and
antineutrino channels. Do not use the earlier mixed-convention table.

The neutron/proton ratio is a ratio of scattering coefficients, not a free
number-density ratio. It also depends on the weak matrix element, effective
mass, and initial/final-state Pauli factors.

## C4-C2 numerical acceptance

- Seven C4-C2 tests passed.
- Sixteen EOS local cases and four cold/dilute Horowitz total-cross-section
  cases completed.
- Maximum cold Horowitz total-cross-section residual:
  `5.374420715353878e-06`.
- Maximum EOS angular quadrature difference:
  `1.782435670794058e-05`.
- Maximum initial-momentum/azimuth quadrature difference:
  `7.230675025504674e-06`.
- Maximum outgoing-support root residual:
  `1.0317349103132463e-13`.

## C4-C3 code and workflow corrections

C4-C3 is a separate 301-radius, fixed-local-energy, flat-space scattering
optical-depth diagnostic. It is not a redshifted transport solution.

The C4-C3 provenance helper previously encoded the Git blob header with a
literal backslash-zero rather than a NUL byte. This is corrected in commit
`ab67c76c2d282c1c4dfe382cffc76c0f9933d5e6`; the correct header is
`blob <length>\0` (where the final two-character notation denotes a NUL
byte in the byte stream).

The workflow is revised in commit
`6e79bcccda8db26939d5489788c6f2cb496cb37f`:
- C4-C3 unit tests run once, before the calculation matrix.
- Twenty shards partition the 301 radial points.
- The merge requires exactly 1204 local species/sign records.
- The merge pins the C1 profile, C2 occupation, and C4-C2 reference by Git blob
  SHA, and requires C4-C2 reproduction at the four anchor radii.
- The merge checks density closure, nonnegative monotone optical depth, and
  0.10 km / 0.25 km radial-grid comparisons.
- A `workflow_dispatch` trigger is available in addition to the branch push
  trigger.

No C4-C3 numerical result is claimed in this report. Completion requires an
actual Actions run, successful merge acceptance, and inspection of the
archived 301-point outputs. The diagnostic remains separate from the Blinov
pure-vector Fig. 7 transport gate and does not update PR #56, manuscript files,
or axial cooling limits.

## Execution update

The C4-C3 workflow has now been triggered by the regression-test update:

- Actions run: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43039883023
- Run number: 4
- Trigger: push
- Head: `c56389d8510a8040f9b974dffb504013a45ec655`
- Initial observed state: `pending`; no jobs had yet been allocated at the time of this update.

The Git blob NUL-byte encoding fix is additionally covered by a regression test
using the canonical Git blob SHA-1 of the byte sequence `test\n`.
The test fixture was corrected to contain an actual newline byte. The test
and workflow trigger updates are commits `4cbbba371f967c8edcf97ac78e30b7978c8afc28`,
`5439166606c25b9c99670dd21ea0942643f6ecd7`, and
`c56389d8510a8040f9b974dffb504013a45ec655`.

The workflow is running/pending; this addendum does not claim a test pass or
C4-C3 numerical completion.
