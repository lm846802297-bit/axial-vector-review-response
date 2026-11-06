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
