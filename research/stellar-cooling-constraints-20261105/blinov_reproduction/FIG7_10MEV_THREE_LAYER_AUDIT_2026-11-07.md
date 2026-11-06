# Three-layer decomposition of the 10 MeV Fig. 7 discrepancy

## Question

Does the residual in the 10 MeV Blinov Fig. 7 curve arise already in the optically thin source, in the channel-resolved reduced opacities, or only after transport/escape is applied?

This diagnostic answers that question without changing the production scan or introducing fitted opacity multipliers.

## Method

The calculation reuses the independent literal scalar Appendix-B implementation in blinov_reproduction/reference.py and evaluates the archived 25-point Fig. 7 coupling grid at \(m_V=10\) MeV.

For each channel \(c\in\{\nu,\mu\gamma,\mu^+\mu^-\}\), it constructs the reduced opacity using the same detailed-balance convention as the reference implementation:

\[
\Gamma^{*,c}_{\rm abs}
=(1-e^{-\omega/T})e^{\omega/T}\Gamma^c_{\rm prod}.
\]

The channel columns are integrated separately along the same chord/direction quadrature. Their sum is compared point-by-point with a direct integration of the total reduced opacity.

The source is decomposed by channel before transport. For each coupling, the emergent contribution of source channel \(c\) is computed using the **total** optical depth:

\[
L_c(g)=g^2\int dV\,d\omega\,
Q_c(\omega,r)\,
\left\langle e^{-g^2(\tau_\nu+\tau_{\mu\gamma}+\tau_{\mu\mu})}\right\rangle.
\]

Source-channel luminosities are additive, but each emitted particle is attenuated by all absorption channels. We do not propagate each source channel through only its own opacity and then add those answers.

The output contains optically thin source luminosities for neutrino coalescence, semi-Compton and dimuon channels; source-weighted mean/median/90th-percentile optical depths; channel-resolved emergent luminosities and escape fractions; and all 25 calculated-vs-reference points.

## Interpretation boundary

The channel opacity decomposition uses the detailed-balance prescription already present in reference.py. It is **not** an independent microscopic derivation of each inverse process, nor does it independently integrate the forward and reverse Compton phase spaces. The B.19 direct thermal-integral audit remains separate.

A near-zero channel-additivity residual validates numerical bookkeeping and linearity of the line-of-sight integral. It does not prove that the underlying microscopic opacity formula is physically correct.

## Reproduce

From the repository root:

~~~bash
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p 'test_fig7_10mev_three_layer.py' -v

python research/stellar-cooling-constraints-20261105/blinov_reproduction/diagnose_fig7_10mev_three_layer.py
~~~

The run writes blinov_reproduction/outputs/fig7_10mev_three_layer.json. The dedicated workflow runs only this diagnostic and its unit tests. It does not run the full mass scan, modify the axial scan, or change manuscript/reply-letter files.

## Decision rule

- If the optically thin source already disagrees with the reference in the same coupling-dependent pattern, investigate source terms, profile reconstruction and phase-space integration first.
- If the optically thin source is stable but reduced-opacity columns differ strongly by channel, investigate the relevant inverse-process kernel and detailed balance.
- If source and channel columns are internally consistent but the emergent curve still differs, inspect chord geometry, redshift treatment, angular escape average and transport.
- No factor-of-two adjustment is accepted unless it follows from an independently derived and consistently applied forward/reverse rate convention.


## Numerical result (40 radial, 100 energy, 16 angular, 32 path quadrature points)

The decomposition reproduces the existing baseline 25-point curve: mean absolute relative difference 15.7319%, maximum 92.2382%, with -8.8857% at the weak-coupling endpoint, +2.5683% at the reference peak, and +92.2382% at the strong-absorption endpoint.

| Representative point | \(g\) | Thin / Fig. 7 reference | Escaped / reference | Total escape fraction |
|---|---:|---:|---:|---:|
| Weak coupling | \(4.7964\times10^{-10}\) | 0.9131 | 0.9111 | 0.99787 |
| Reference peak | \(1.1341\times10^{-8}\) | 2.9100 | 1.0257 | 0.35247 |
| Strong absorption | \(4.1717\times10^{-8}\) | 5934.77 | 1.9224 | \(3.239\times10^{-4}\) |

The optically thin source composition is 67.995% neutrino coalescence and 32.005% semi-Compton; the dimuon channel is closed at \(m_V=10\) MeV. This source composition is independent of \(g\) in the present perturbative setup.

Source-weighted optical-depth statistics:

| Point | \(\langle\tau_\nu\rangle_Q\) | \(\langle\tau_{\mu\gamma}\rangle_Q\) | \(\langle\tau_{\rm total}\rangle_Q\) | Total \(p_{90}\) |
|---|---:|---:|---:|---:|
| Weak coupling | 0.001915 | 0.000218 | 0.002133 | 0.003474 |
| Reference peak | 1.0707 | 0.1219 | 1.1926 | 1.9423 |
| Strong absorption | 14.487 | 1.649 | 16.137 | 26.280 |

The source-weighted mean opacity split is 89.78% neutrino inverse decay and 10.22% inverse Compton at all three coupling points. At the strong-absorption point, the escaped luminosity is 54.15% neutrino-sourced and 45.85% semi-Compton-sourced, despite the 68/32 thin-source split; the two source spectra have different escape fractions.

## Physical reading

1. At the weak-coupling endpoint, escape is essentially unity. The approximately -8.9% residual is already present in the optically thin source normalization/profile/digitized-reference comparison; it cannot be attributed to trapping.
2. At the reference peak, the optically thin result is about 2.91 times the digitized luminosity, while the escape fraction is about 0.352. The near-agreement of the final luminosity is therefore a compensation between source normalization and attenuation, not an independent validation of both pieces.
3. At the strong-absorption endpoint, the thin source is about \(5.93\times10^3\) times the reference, and transport suppresses it by a factor of about \(3.24\times10^{-4}\). The final result nevertheless remains 92.2% above the digitized reference. The remaining tail discrepancy is therefore transport-sensitive.
4. Neutrino inverse decay dominates the source-weighted mean optical depth (about 90%). Compton opacity is subdominant but not negligible (about 10%); because escape depends exponentially on the *sum* of optical depths, this minority contribution can still have a sizeable effect on the high-coupling tail. The earlier Compton-opacity ×2 sensitivity result is consequently a useful sensitivity clue, not evidence for a physical factor of two.

The weighted mean optical depth must not be exponentiated to estimate the escape fraction: the calculation averages \(\exp(-\tau)\) over source position, energy and direction, and in general \(\langle e^{-\tau}\rangle\ne e^{-\langle\tau\rangle}\).

## Consistency checks and status

The channel reduced-opacity sum agrees with the reference total to a maximum relative residual of \(3.96\times10^{-16}\); the sum of channel line-of-sight columns agrees with a direct total-opacity integration to \(6.72\times10^{-16}\); and channel emergent luminosities sum to the total by construction to floating-point precision.

These are decomposition/bookkeeping checks under the *same* reference detailed-balance prescription. They are not the independent forward/reverse Compton phase-space test of B.19. That remains the next microscopic cross-check before any production-code correction is considered.

The dedicated [three-layer workflow](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42310090478) passes, including four regression tests and the full 25-point diagnostic. The earlier broad Major 4.4 workflow on the initial diagnostic commit failed at test-module import discovery (before its numerical scans); the import mode is now fixed, and the diagnostic-only paths are excluded from that broad full-scan trigger to avoid repeating the four-mass scan for this targeted audit.
