# B.2 neutrino inverse-decay absorption in the 12--15 km path shell

Date: 2026-11-09  
Benchmark: \(m_V=10\) MeV, \(g=4.17168965\times10^{-8}\), \(R_{\max}=25\) km, fixed \(\omega\) along the B.2 path.  
Emission region of primary interest: 8--15 km, which supplies 79.6117% of the total B.1 source in this benchmark.  
Status: **the 12--15 km \(\nu_\mu\) and \(\nu_\tau\) inverse-decay opacity is numerically cross-checked and makes a substantial contribution to the strong-coupling escape suppression. The channel-resolved path calculation passes its independent integral and detailed-balance checks.**

## 1. What is being checked

The target is the B.2 absorption of the vector through

\[
\nu_\mu\bar\nu_\mu\to V,\qquad
\nu_\tau\bar\nu_\tau\to V.
\]

The \(\nu_\mu\) and \(\nu_\tau\) channels are kept separate. The Compton channel is reported as a separate control and is not folded into the neutrino inverse-decay result. At \(m_V=10\) MeV the dimuon channel is kinematically closed.

The audit uses the channel-resolved analytic radial path decomposition in B16_INNER_PATH_CHANNEL_DIRECTIONAL_AUDIT_2026-11-09.md. It integrates each radial shell on its own smooth segments, retaining inward and outward ray branches and the turning point. This avoids the shell-allocation bias of the old global-s quadrature with radial masks.

## 2. Local opacity in the shell

At \(\omega=15\) MeV, the reduced absorption rates per \(g^2\), in the internal units of the reference implementation, are:

| Radius | \(\nu_\mu\) inverse decay | \(\nu_\tau\) inverse decay | Compton | Compton fraction |
|---:|---:|---:|---:|---:|
| 12 km | 0.037625 | 0.037877 | 0.013867 | 15.52% |
| 15 km | 0.072196 | 0.072196 | \(3.183\times10^{-4}\) | 0.220% |

The neutrino inverse-decay opacity increases outward across this shell. Compton absorption falls rapidly and is already negligible at the outer edge. Thus the 12--15 km shell is not accurately represented by a single, radius-independent Compton/neutrino ratio.

## 3. Integrated path-shell optical depth

For the dominant 8--15 km B.1 emission region, at the strong endpoint:

\[
P_{\rm esc}^{8-15\,{\rm km}}=3.53332\times10^{-4}.
\]

The 12--15 km path-shell contributions are:

| Channel | Source-weighted \(\langle\tau/g^2\rangle\) | Escaped-population-weighted \(\langle\tau/g^2\rangle\) | Fraction of that channel's total path optical depth (source / escaped weighting) |
|---|---:|---:|---:|
| \(\nu_\mu\) inverse decay | \(6.5434\times10^{14}\) | \(2.6014\times10^{14}\) | 16.08% / 19.47% |
| \(\nu_\tau\) inverse decay | \(6.5472\times10^{14}\) | \(2.6019\times10^{14}\) | 15.86% / 19.46% |
| Compton | \(1.0060\times10^{14}\) | \(8.0126\times10^{13}\) | 10.70% / 19.65% |

The neutrino channels are nearly equal, as expected from their equal-magnitude \(L_\mu-L_\tau\) charges in the pure-vector reference model. Their combined 12--15 km shell accounts for approximately 16% of the source-weighted neutrino path optical depth and 19.5% of the escaped-population-weighted neutrino path optical depth.

The escaped-population weighting is smaller in absolute magnitude because it is evaluated on rays that have survived the full optical depth; it is not a replacement for the unattenuated source weighting.

## 4. Nonlinear leave-one-channel-shell-out test

Holding the B.1 source and all other opacity components fixed, remove only one channel in the 12--15 km path shell:

| Removed component | Increase in escaping luminosity |
|---|---:|
| \(\nu_\mu\) inverse decay in 12--15 km | 59.31% |
| \(\nu_\tau\) inverse decay in 12--15 km | 59.32% |
| Compton absorption in 12--15 km | 15.04% |
| Dimuon absorption in 12--15 km | 0 |

These are nonlinear counterfactual sensitivity tests. They are not additive contributions to the luminosity deficit and must not be summed. Removing both neutrino flavors simultaneously would require a separate combined counterfactual; the two individual enhancements are not a substitute for that calculation.

The 12--15 km neutrino inverse-decay shell is therefore an important part of the strong-coupling attenuation. It is not, however, the only important shell: the independent full-shell audit finds that the outer 22--25 km neutrino shell has the largest individual all-channel leave-one-shell-out sensitivity at the strong endpoint.

## 5. Independent numerical checks

The local B.2 inverse-decay calculation is checked against direct angular phase-space integration, separately for \(\nu_\mu\) and \(\nu_\tau\), and against the B.10 detailed-balance relation:

| Check | Maximum relative residual |
|---|---:|
| \(\nu_\mu\): direct angular integral vs. analytic reference | \(4.77\times10^{-15}\) |
| \(\nu_\tau\): direct angular integral vs. analytic reference | \(6.05\times10^{-15}\) |
| \(\nu_\mu\) B.10 detailed balance | \(2.67\times10^{-15}\) |
| \(\nu_\tau\) B.10 detailed balance | \(2.67\times10^{-15}\) |
| Neutrino B.4 reduced opacity | \(2.72\times10^{-15}\) |

For the global B.2 path integral, the analytic radial decomposition agrees with an independent 256-point full-path s-coordinate integration to a maximum relative residual of \(1.19225\times10^{-4}\). Weighted by the dominant 8--15 km B.1 source, the L1 relative difference is \(2.09389\times10^{-6}\).

The old global-s masked shell allocation is not used for the shell-level numbers above. The analytic radial decomposition is the reference.

## 6. Interpretation for the Fig. 7 discrepancy

The 12--15 km \(\nu_\mu\) and \(\nu_\tau\) inverse-decay opacity is numerically verified within the implemented B.2 prescription and is physically important at the strong endpoint. This does not by itself establish that the full vector Fig. 7 curve is reproduced.

The current Fig. 7 source/escape diagnostic finds:

- At the weak endpoint, the required escape probability exceeds one, so the discrepancy cannot be repaired by changing absorption alone.
- At the reference-luminosity peak, the calculated escape probability agrees within about 2.5%.
- At the strong endpoint, the required escape probability is only 0.5202 times the calculated value, corresponding to an effective additional optical depth of 0.6536.

The 12--15 km shell is one important attenuation component, but the outer 22--25 km neutrino inverse-decay shell also has substantial leverage. The next transport diagnostic should therefore compare the 12--15 and 22--25 km shell contributions on the same fixed source and angular distribution, without changing \(R_{\max}=25\) km or rescaling any opacity.

No production rates, absorption formulas, transport outputs, luminosities, or axial-vector curves are modified by this audit.

## 7. Reproducibility

- Full channel-, shell-, and direction-resolved audit: B16_INNER_PATH_CHANNEL_DIRECTIONAL_AUDIT_2026-11-09.md
- Machine-readable output: outputs/b16_inner_path_channel_directional_10mev_2026-11-09.json
- Local detailed-balance audit: B16_LOCAL_ABSORPTION_AUDIT_2026-11-09.md
- Successful full-path audit workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42504612491
