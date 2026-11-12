# B.2 combined channel--shell sensitivity at the strong-coupling endpoint

Date: 2026-11-09  
Benchmark: pure-vector B.14--B.19 reference baseline, \(m_V=10\) MeV, \(g=4.17168965\times10^{-8}\).  
Status: **combined nonlinear leave-out diagnostics are complete. Neutrino inverse-decay opacity dominates the total attenuation; the most sensitive individual path shells are 12--15 km and 22--25 km.**

## 1. Purpose and interpretation

The B.16 inner-path audit previously removed one channel in one radial shell at a time. This extension additionally removes:

- all channels in one radial shell;
- one complete channel across the entire path;
- all channels or selected channels in the inner \(8\)--22 km and outer \(22\)--25 km groups.

For each diagnostic, the luminosity integral is recomputed with the modified optical-depth columns. These are **leave-out sensitivity tests**, not alternative physical models and not proposed corrections. Their effects are nonlinear and must not be added together.

The source, coupling, reconstructed stellar profile, energy convention, and B.2 geometry are held fixed. No rescaling is applied.

## 2. Strong-endpoint reference values

At \(g=4.17168965\times10^{-8}\):

- all-emission source-weighted escape probability:
  \[
  P_{\rm esc}=3.23933\times10^{-4};
  \]
- for the dominant \(8\)--15 km emission region:
  \[
  P_{\rm esc}^{8-15}=3.53332\times10^{-4};
  \]
- the \(8\)--15 km region supplies \(79.61\%\) of the B.1 thin source.

## 3. Remove all channels in one radial shell

The table gives the enhancement of the escaped luminosity after removing every opacity channel in the indicated shell.

| Removed path shell | All emission radii | Dominant 8--15 km emission |
|---|---:|---:|
| 0--5 km | \(1.013\times\) | \(1.0075\times\) |
| 5--8 km | \(1.197\times\) | \(1.092\times\) |
| 8--10 km | \(2.120\times\) | \(2.001\times\) |
| 10--12 km | \(2.497\times\) | \(2.561\times\) |
| 12--15 km | \(2.926\times\) | \(3.047\times\) |
| 15--16.5 km | \(1.584\times\) | \(1.615\times\) |
| 16.5--18.5 km | \(1.859\times\) | \(1.904\times\) |
| 18.5--20 km | \(1.580\times\) | \(1.609\times\) |
| 20--22 km | \(1.846\times\) | \(1.889\times\) |
| 22--25 km | \(4.073\times\) | \(2.627\times\) |

The outer 22--25 km shell has the largest individual all-emission leave-out effect. Within the dominant 8--15 km emission sample, the 12--15 km shell has the largest individual effect, followed by 22--25 km.

This does not contradict the source-weighted mean optical-depth decomposition. A leave-out luminosity response depends on the full energy--angle distribution and the exponential \(e^{-\tau}\), not only on a mean optical depth.

## 4. Remove one complete channel

| Removed channel over the full path | All-emission luminosity enhancement | Dominant 8--15 km source enhancement |
|---|---:|---:|
| \(\nu_\mu\) inverse decay | \(13.78\times\) | \(14.05\times\) |
| \(\nu_\tau\) inverse decay | \(13.86\times\) | \(14.10\times\) |
| Compton | \(2.49\times\) | \(2.34\times\) |
| Dimuon | 1 | 1 |

The two neutrino inverse-decay channels dominate the attenuation. Compton is non-negligible but subdominant in the full path. The dimuon channel is closed for the 10 MeV mediator benchmark.

## 5. Combined inner-versus-outer path sensitivity

| Removed opacity group | All-emission luminosity enhancement | Dominant 8--15 km source enhancement |
|---|---:|---:|
| All channels in 8--22 km | \(313.7\times\) | \(324.9\times\) |
| \(\nu_\mu+\nu_\tau\) in 8--22 km | \(108.4\times\) | \(114.2\times\) |
| Compton in 8--22 km | \(2.33\times\) | \(2.27\times\) |
| All channels in 22--25 km | \(4.073\times\) | \(2.627\times\) |
| \(\nu_\mu+\nu_\tau\) in 22--25 km | \(4.073\times\) | \(2.627\times\) |
| Compton in 22--25 km | 1 | 1 |

The inner \(8\)--22 km region dominates the total attenuation. Within that region, neutrino inverse decay is much more important than Compton. The outer 22--25 km neutrino shell nevertheless has a substantial nonlinear effect and cannot be dropped.

## 6. Relation to the current Fig. 7 mismatch

The current strong-endpoint escape probability is approximately \(1/0.520\) times the value required by the Fig. 7 reference comparison. The leave-out tests show that the opacity in individual sensitive shells can strongly affect the escaped luminosity.

However, a leave-out result does not identify an error in that shell. It only measures sensitivity. In particular:

- the B.6--B.10 neutrino local formulae pass independent phase-space and detailed-balance checks;
- the B.4 reduced-absorption implementation passes;
- the 22--25 km outer input audit found no interpolation defect large enough to explain the discrepancy;
- the raw Garching profile used by the reference calculation remains unavailable, while the current profile is reconstructed from published figures.

The remaining plausible distinction is therefore the underlying stellar-background input and its radial/thermodynamic reconstruction, not an already identified algebraic error in the neutrino opacity.

## 7. Decision and next step

1. Keep the pure-vector curve frozen.
2. Do not apply a common rescaling to the neutrino absorption or total luminosity.
3. Do not interpret leave-out enhancements as physical correction factors.
4. Prioritize an independent input audit of the \(12\)--15 km region, which is the most sensitive shell for the dominant emission-region sample.
5. Keep the \(22\)--25 km neutrino-opacity contribution in the transport calculation; it is not negligible.

The next input audit should compare \(T(r)\), \(\mu_{\nu_\mu}(r)\), \(\mu_{\nu_\tau}(r)\), \(\mu_\mu(r)\), and the lapse in the \(12\)--15 km interval against the original published SFHo-18.8 figures, keeping the existing digitization and interpolation assumptions explicit.

## 8. Reproducibility

The machine-readable combined sensitivities are stored in:
outputs/b16_inner_path_channel_directional_10mev_2026-11-09.json

The calculation is generated by:
audit_b16_inner_path_channel_directional.py

The updated B.16 inner-path workflow runs the analytic path tests, regenerates the channel--shell--direction audit, and verifies that production axial outputs remain unchanged.
