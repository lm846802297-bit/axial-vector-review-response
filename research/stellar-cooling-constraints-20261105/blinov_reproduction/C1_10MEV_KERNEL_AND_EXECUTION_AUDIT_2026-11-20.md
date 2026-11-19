# C1 10 MeV kernel and execution audit

Date: 2026-11-20  
Status: **kernel-quadrature evidence audited; isolated C1 transport run in progress**

## 1. Decision

For the first complete C1 point, use (m_{A'}=10) MeV and the reviewed public SFHo-18.8 profile. Run the full radial-energy transport with the validated baseline local quadrature, then use the archived high-order local-kernel ladder and separate radial/energy grid scans to establish the final uncertainty.

Do not spend the full four-dimensional high-order quadrature at every radial-energy node before establishing the global transport baseline.

## 2. Current B.13 kernel is numerically the same kernel as the archived convergence audit

The archived local convergence record is:

- `outputs/b13_local_kernel_quadrature_convergence_10mev_2026-11-09.json`
- Its source SHA-256 for `moving_muon_compton.py` is `44bc670fd9384f34de56fbecb5371bae18c93c2292aa67e98f4ee304433dbaea`.
- Its `rates.py` source SHA-256 is `2fc7bc2d3b0d7b98c191755cd2bb87944e4ebe259adc3d3bbc8e0f60dcc57f56`.

A direct historical/current source comparison was performed for the actual C1 dependency:

- Historical `moving_muon_compton.py` at commit `1e4f926b4e904e187b9bfbd1f13ef7cdba2e416c`: Git blob `681b7374247c6968d2223d455c9a82fe7d95945a`.
- Current branch `moving_muon_compton.py`: Git blob `918d38504b8a0df1c21dfe243bc25eab9808e6a9`.
- The complete numerical body of `moving_muon_compton_rates) is unchanged. The differences are the expanded mode/polarization documentation and an appended log-space Eq. (5.12) unpolarized detailed-balance diagnostic. The phase-space measure, spinor amplitude, polarization vectors, statistical factors, prefactor, and quadrature accumulation are unchanged.
- `rates.py` has the identical Git blob SHA `dd4d1accfd58a574e704f477f611299f15943465` at the historical and current refs.

Therefore the archived local quadrature convergence results apply to the rate-producing kernel now used by C1. The new Eq. (5.12) diagnostic adds a check; it does not alter the rates.

## 3. Local B.13 quadrature evidence at 10 MeV

The archived audit used three representative points: ((r,\omega)=(8\,\mathrm{km},15\,\mathrm{MeV})), ((12.5\,\mathrm{km},20\,\mathrm{MeV})), and ((15\,\mathrm{km},30\,\mathrm{MeV})).

| Four-dimensional order | Maximum relative change recorded |
|---|---:|
| (12\times8\times8\times8\to16\times10\times10\times10) | approximately (2.07\times10^{-3}) at the 8 km / 15 MeV point |
| (16\times10\times10\times10\to20\times12\times12\times12) | (8.9077\times10^{-4}) |
| (20\times12\times12\times12\to24\times14\times14\times14) | (3.0160\times10^{-4}) |

The archived screening target is (10^{-3}) for the last two refinements. Both pass. The maximum final-muon shell residual is (1.63\times10^{-13}), and the maximum mode-resolved detailed-balance residual is (1.51\times10^{-15}).

The 8 km / 15 MeV point is the most demanding of the three samples. This is why the C1 global baseline uses (12,8,8,8) and retains a higher-order local audit, rather than treating the lowest order as an exact result.

## 4. Independent global B.13 benchmark and grid evidence

The prior exact moving-muon B.13 global calculation is archived in:

- `outputs/b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json`
- `outputs/b13_global_grid_convergence_2026-11-09.json`

The 10 MeV global B.13 run recorded 2,106 exact kernel evaluations, 78 energy nodes, 27 active radial nodes, and a wall time of 434.01 s. Its maximum mode detailed-balance residuals are at or below (1.53\times10^{-14}), and the final-muon shell residual is (3.71\times10^{-13}).

In the separate B.13 B.1/B.2 grid scan, the 60-radial / 140-energy result shifts the luminosity by at most (2.732\times10^{-3}) relative to the 40-radial / 100-energy reference, meeting that audit's 1% stability target.

These are independent B.13 kernel and B.1/B.2 transport validations. They are not the Croon-geometry C1 luminosity and do not replace the C1-specific radial/energy convergence scan.

## 5. C1 10 MeV execution

The current C1 script evaluates the updated B.7 two-flavour neutrino rates and exact moving-muon B.13 rates on the reviewed profile, retaining both muon charges and all three vector polarizations. The outer (R_\nu\to100\) km path includes the two-flavour vacuum B.7 tail; the unvalidated outer semi-Compton opacity is not inserted.

### Isolated single-mass baseline: first execution and archival retry

First execution:
- Workflow: [Croon C1 10 MeV single-mass baseline](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44569820441)
- Workflow source commit: `beeca694274151d4217ade48bd26f253bc87f643`
- Configuration: 101 requested radial points, 32 energy nodes, B.13 orders `12,8,8,8`, B.7 angular order 128, susceptibility order 192, 121 coupling points.
- The sampled profile adds the muon-density edge and neutrinosphere boundary, giving 103 actual radial nodes.
- Six C1 equation, detailed-balance, and boundary tests passed. The full transport calculation, JSON/CSV validation, and SHA-256 manifest creation all passed.
- The physical diagnostics were: maximum B.7 detailed-balance residual (3.3114\times10^{-14}), maximum B.13 charge-mode residual (5.1765\times10^{-14}), and final-muon shell residual (5.3802\times10^{-13}).
- The integrated optically-thin source per (g_X^2) was (4.45124\times10^{70}\) erg/s from B.7 neutrino coalescence, (7.28021\times10^{69}\) erg/s from (mu^-) B.13, and (5.04202\times10^{67}\) erg/s from (mu^+) B.13. Thus B.7 contributes 85.86% and B.13 14.14% of the combined thin source; (mu^+) contributes 0.688% of the B.13 component.
- The exact moving-muon B.13 source (both charges) is 0.69598 of the same-grid Croon Eq. (4.7) (mu^-)-only source. This is a thin-source comparison, not an escaping luminosity or an exclusion limit.
- Git archival failed after the calculations had passed: the branch advanced while the job was running, so the runner's direct push was rejected as non-fast-forward. The artifact step was ordered after the failed push and was skipped; no native JSON/CSV was retained from that execution.

Archival retry:
- The workflow was corrected to upload the native JSON/CSV and SHA-256 manifest before attempting the Git push, then fetch and rebase onto the latest PR branch before pushing.
- Retry workflow: [Croon C1 10 MeV single-mass baseline](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44572225917)
- Retry source commit: `9835706cb738c756234812cfc672a22cf50fc086`
- The retry is running the same calculation and validation configuration. Its artifact and remote Git commit must be verified before declaring the native files archived.

### Earlier full-grid high-order attempt

- Workflow: [Croon C1 10 MeV high-order vector transport](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44567808760)
- It requests 101 radial points, 48 energy nodes, and B.13 orders `16,10,10,10`.
- The workflow API continued to report the transport step as in progress, with no artifact available at the latest check. It is not counted as a completed result.

## 6. Acceptance gates

The 10 MeV C1 baseline is accepted only after:

1. Native JSON and radial CSV exist and their row/node counts agree.
2. B.7 and each B.13 charge-mode detailed-balance residuals pass.
3. Final-muon on-shell residual passes.
4. All three polarizations remain separately present and finite.
5. Thin-source contributions and both (R_{\rm far}) luminosity curves are finite and nonnegative.
6. The native output files and SHA-256 manifest are committed to the PR branch and checked against the remote Git blobs.
7. A separate C1 radial/energy refinement scan establishes global luminosity stability.

Only then proceed to the six-mass C1 scan. The axial-vector A0 calculation remains a separate subsequent stage and will use the same verified local kernel with the model's axial and finite vector admixture couplings.
