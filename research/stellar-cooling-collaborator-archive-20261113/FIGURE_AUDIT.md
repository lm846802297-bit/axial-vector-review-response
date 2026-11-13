# Axial stellar-cooling figure: derivation, plotting, and scientific acceptance

## 1. What the current figure is

The figure in outputs/axial_stellar_constraints.pdf is generated from saved numerical scans, not digitized from a paper. Primary inputs:

- outputs/axial.json: axial-current scan;
- outputs/endpoint.json: five additional endpoint masses;
- outputs/vector.json: internal pure-vector muon-current control;
- outputs/convergence.json, outputs/coupling_refinement.json, outputs/numerical_validation.json, and related sensitivity JSON files.

The axial plot combines 75 baseline mass rows with five endpoint rows, for 80 axial mass rows. The vector control contains 75 mass rows. Each baseline mass row has 301 logarithmically spaced couplings. The stored coupling scan is 1e-14 to 1e-3; the visible y-axis ends at 1e-4. The displayed mass range is 0.01 to 500 MeV.

Baseline settings: radial quadrature 88, energy nodes 180, direction quadrature 24, path/chord quadrature 64, semi-Compton scattering-angle order 40, escape radius 25 km, energy offset 1,200 MeV, and unit semi-Compton normalization scale. The tau-neutrino chemical-potential profile is retained as reconstructed rather than forced to zero.

## 2. Physics chain

For a fixed stellar background and axial EFT coupling g_X, the calculation proceeds through:

1. Mode-resolved local production rates for h = L,+,-.
2. Corresponding reduced absorption rates using the adopted detailed-balance relations.
3. Radial source integral and direction-dependent optical-depth column.
4. Ballistic survival probability.
5. Escaped luminosity for each coupling.
6. Threshold crossing in coupling at each mediator mass.
7. Mass-coupling boundary and shaded benchmark region.

The adopted production channels are semi-Compton scattering on muons, active muon-neutrino coalescence, and dimuon coalescence above threshold. The axial production code uses the initial-muon-rest semi-Compton approximation with an effective thermal muon density. It is not the full moving-muon thermal B.13 kernel.

The documented ballistic optical-depth and survival-probability structure is

\[
\tau_h^{(0)}(r,\omega,u)
=\int_0^{s_{\max}} ds\,
\frac{\Gamma_h^{\mathrm{red}}(r'(s),\omega)}{v_{A'}},
\qquad
P_h(r,\omega)
=\frac12\int_{-1}^{1}du\,
e^{-g_X^2\tau_h^{(0)}(r,\omega,u)}.
\]

The escaped luminosity is

\[
L_{A'} =
g_X^2\sum_{h=L,+,-}
\int_0^{R_\nu}4\pi r^2dr\,N(r)^2
\int_{m_{A'}/N(r)}^\infty d\omega\,
\frac{k\omega^2}{2\pi^2}\,
\Gamma_{h,0}^{\mathrm{prod}}(r,\omega)
\left\langle e^{-g_X^2\tau_h^{(0)}}\right\rangle_u,
\]

with k = sqrt(omega^2 - m_A'^2) and the documented local threshold m_A'/N(r). The chord calculation uses the fixed numerical mediator-energy convention described in the source report. It is not a full GR geodesic or energy-redistribution calculation.

A key nonlinearity must not be hidden:

\[
\sum_h Q_h e^{-\tau_h}
\ne
\left(\sum_h Q_h\right)e^{-\sum_h\tau_h}.
\]

The mode-resolved axial lane and the scalar polarization-summed literal Blinov reference are not automatically equivalent. The final transport prescription requires a physical derivation, not a fitted rescaling.

## 3. How the exclusion-like region is drawn

The primary reference criterion is

\[
L_{A'}(m_{A'},g_X)=4.4\times10^{52}\ \mathrm{erg\,s^{-1}}.
\]

For each fixed mass, the scan stores luminosities over the logarithmic coupling grid. run_scan.find_intervals forms

\[
x=\log g_X,\qquad y=\log L_{A'}-\log L_{\mathrm{crit}},
\]

finds every sign-changing adjacent pair, interpolates each crossing linearly in (log g_X, log L), and records every interval above threshold. It does not assume that the excluded set is a single connected interval.

The figure uses:
- blue boundary and shading: the 4.4e52 erg/s benchmark;
- dotted blue boundary: a 3.0e52 erg/s threshold sensitivity view, not a second independent experimental exclusion;
- dashed black boundary: the internal vector-current control, **not** an accepted reproduction of published Blinov Fig. 7;
- beige patch: only the visible overlap with the old Fig. 2 display window; it is not a global allowed-region mask;
- right panel: optically thin production fractions for Compton, neutrino coalescence, and dimuon coalescence, before escape attenuation. These are not fractions of the final escaped luminosity.

The MeV and GeV versions use the same scan; only the mass coordinate is divided by 1,000 for the GeV view.

## 4. Plot interpolation audit

The original plot_constraints.py passes the saved luminosity grid to Matplotlib contour / contourf in the native linear mass and coupling arrays, then changes the displayed axes to logarithmic scales. The per-mass threshold intervals, however, are extracted using log-coupling / log-luminosity interpolation. These operations are close on a dense grid but are not mathematically identical.

A review-only implementation, plot_constraints_loglog.py, draws the per-mass threshold intervals directly and connects sampled mass rows on logarithmic axes. It also reconstructs the original Matplotlib contour and compares its lower and upper branches with the stored per-mass log-log crossings. The generated contour_interpolation_audit.json reports the number of compared mass rows and maximum / RMS relative difference for both branches.

Do not quote an interpolation-error percentage from memory or from the PDF. Use the actual contour_interpolation_audit.json generated with the package. The log-log review figure is a plotting cross-check, not a new physical calculation. It does not resolve the vector benchmark, moving-muon, profile, or transport uncertainties.

The log-log review figure also interpolates between discrete mass rows when connecting the plotted line. It is not a continuous two-dimensional scan in mediator mass.

## 5. Is the current contour reasonable?

### Numerically / as a benchmark plot

The figure is reasonable as a compact visualization of the saved fixed-profile scan if the following are explicit:

- its data source is the saved scan JSON;
- the primary threshold is 4.4e52 erg/s;
- coupling boundaries are derived per mass with logarithmic interpolation;
- the 3.0e52 erg/s line is a threshold sensitivity;
- the vector dashed curve is an internal control only;
- the right panel shows optically thin source fractions;
- the beige patch is a comparison window, not a viability statement.

The numerical scan has separate checks for array integrity, interval reconstruction, path-column contraction, selected quadrature refinements, coupling refinement, energy cutoff, and profile / opacity sensitivities. Those checks establish internal numerical consistency for the recorded settings; they do not validate the physical model assumptions.

### As a final SN1987A exclusion

**No. It is not yet justified as the final model exclusion.** The pure-vector Fig. 7 end-to-end gate remains open. The literal fixed-omega 10 MeV high-absorption comparison retains a discrepancy of about +92.24%; the separate conserved-E-infinity diagnostic does not close it (about +35.97%). The axial scan also has not incorporated the complete moving-muon B.13 thermal kernel. Background reconstruction, outer lapse continuation, tau-neutrino chemical-potential choice, fixed-energy chord convention, and polarization-summed versus mode-resolved opacity remain physical/model limitations.

The 20 km escape-radius diagnostic shifts the upper boundary substantially over representative masses; it is a model-radius sensitivity, not a calibrated uncertainty band. The unshaded area must not be described as globally allowed.

## 6. What is needed before the final model limit

1. Pass the pure-vector B.16/Fig. 7 end-to-end benchmark, especially the 10 MeV strong-absorption tail, without empirical opacity or profile rescaling.
2. Resolve the correct polarization-resolved transport / density-matrix prescription.
3. Integrate the full moving-muon semi-Compton kernel into axial production and absorption, with detailed balance and reference-frame conventions checked.
4. Fix a defensible, internally consistent stellar background and quantify profile uncertainty.
5. Resolve the energy-frame / GR propagation prescription and outer boundary treatment.
6. Recompute the axial mass-coupling scan and convergence after these physics changes.
7. Map the EFT coupling to the selected UV benchmark and state the validity range, other channels, and excluded physics.
8. Regenerate the final figure from the accepted scan and archive exact source, inputs, tests, and SHA-256 manifest.

Until these gates pass, use the conditional-benchmark wording in README.md and STATUS_MATRIX.md.
