# P1-H: Smooth daughter-neutrino reprocessing in the 10 MeV B.2 high-energy band

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV, pure vector, \(g=4.171689650228597\times10^{-8}\)  
Band: \(210\leq\omega\leq510\) MeV  
Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Question

P1-D showed that extending the sharp B.2 trapping boundary from 25 to 30 km suppresses the 210--510 MeV escaped band by \(70.94\%\). If all other energy bins are held fixed, that sharp-boundary proxy happens to lie \(2.79\%\) below the digitized Fig. 7 luminosity.

P1-G shows why this is an extreme prescription: the daughter-neutrino energy escape probability changes continuously across 25--30 km. This audit therefore replaces the full vacuum-limit outer opacity by a smooth transport-only reprocessing factor and performs the complete B.2 source-radius, energy, angle, and path integral for the high-energy band.

## 2. Model

The calculation retains:
- the literal B.1 source, frozen at the \(R_{\max}=25\) km baseline;
- the literal scalar B.2 reduced opacity inside 25 km;
- the same fixed-\(\omega\), Euclidean-chord propagation prescription;
- the two-flavour vacuum-limit \(V\to\nu\bar\nu\) reduced opacity outside 25 km, multiplied by a daughter-energy reprocessing factor.

For a vector of energy \(\omega\), the outer reduced opacity is modelled as
\[
\Gamma_{\rm red,out}(\omega,r)=
\frac{m_V^2}{4\pi\omega}
\left[1-P_{\nu\bar\nu}^{E}(\omega,r)\right].
\]
Here \(P_{\nu\bar\nu}^{E}\) is the equal-polarization average of the P1-G energy-weighted daughter survival proxy, computed using the public-density exponential tail and \(\exp[-\tau_{\nu N}(E,r)]\).

Three density-tail choices are used:
\[
(n_{B,20}/n_0,H_\rho)=
(0.5\times10^{-3},0.9\,{\rm km}),\quad
(1.0\times10^{-3},1.2\,{\rm km}),\quad
(2.0\times10^{-3},1.3\,{\rm km}).
\]
For the central and high tails, longitudinal-only and transverse-only pair weights are also tested to expose the polarization sensitivity.

This is an exploratory transport-scattering closure, not a calculation of the heavy-flavor energy sphere. It assumes that a daughter scattering reprocesses its energy; it does not include the full energy-changing collision kernel.

## 3. Numerical implementation and closure

The direct V8 calculation uses:
- 200 source-radius nodes;
- 642 opacity-radius nodes;
- 842 full energy nodes, including 10 nodes in the 210--510 MeV band;
- 32 propagation-angle nodes;
- 64 path nodes;
- 256 daughter-angle nodes.

The baseline and sharp-boundary closure checks are:
| Check | Relative residual |
|---|---:|
| B.1 band source versus P1-C | \(1.88\times10^{-11}\) |
| \(R_{\max}=25\) km B.2 band versus P1-D, path order 64 | \(4.95\times10^{-12}\) |
| Sharp \(R_{\max}=30\) km B.2 band versus P1-D, path order 64 | \(5.52\times10^{-12}\) |

Only \(9.69\times10^{-7}\) of the reconstructed 210--510 MeV B.1 source lies outside 15 km. Freezing the band source at the 25 km baseline is therefore negligible for this band within the reconstructed profile.

The luminosity integral is evaluated as
\[
L_{\rm band}=g^2\sum_{r,\omega}
S_{\rm B.1}(r,\omega)
\left\langle
e^{-g^2[\tau_{\rm B.2}^{r<25}+
\Delta\tau_{\rm out}^{\rm smooth}]}
\right\rangle_{\Omega}.
\]
The outer path integral is performed along each actual vector chord; it is not replaced by a radial average.

## 4. Results

The literal 25 km band luminosity is
\[
L_{25}=1.70178\times10^{52}\ {\rm erg\,s^{-1}}.
\]

The smooth results are:

| Density tail | Polarization weighting | Outer radius | Band change vs 25 km | Band-only total proxy residual vs Fig. 7 |
|---|---|---:|---:|---:|
| Low | Equal | 30 km | \(-0.334\%\) | \(+91.98\%\) |
| Central | Equal | 27.5 km | \(-3.646\%\) | \(+87.53\%\) |
| Central | Equal | 30 km | \(-4.141\%\) | \(+86.87\%\) |
| Central | Longitudinal | 30 km | \(-3.401\%\) | \(+87.86\%\) |
| Central | Transverse | 30 km | \(-4.508\%\) | \(+86.38\%\) |
| High | Equal | 30 km | \(-10.596\%\) | \(+78.21\%\) |
| High | Longitudinal | 30 km | \(-9.023\%\) | \(+80.32\%\) |
| High | Transverse | 30 km | \(-11.372\%\) | \(+77.16\%\) |

For comparison, the sharp P1-D \(R_{\max}=30\) km extension gives
\[
L_{\rm band}^{\rm sharp30}=4.94603\times10^{51}\ {\rm erg\,s^{-1}},
\]
a \(-70.936\%\) band change and a band-only total proxy \(2.79\%\) below Fig. 7.

The total proxy in the final column is
\[
L_{\rm proxy}=L_{\rm full}^{\rm V8}
-L_{\rm band}^{25}
+L_{\rm band}^{\rm smooth},
\]
where all non-band energy bins are held fixed at the V8 phase-space baseline. It is not a full-spectrum re-integration.

## 5. Interpretation

The near-match obtained from the sharp 30 km extension is not reproduced by the smooth transport-scattering model.

Across the tested public-density tails:
- the low-tail smooth correction is negligible;
- the central-tail correction changes the band by only about \(4.1\%\);
- even the deliberately high-density tail changes the band by about \(10.6\%\) in the equal-polarization calculation;
- the full strong-endpoint residual remains between about \(+78\%\) and \(+92\%\) in the band-only total proxies.

The full P1-D extension assumes that every vector decay between 25 and 30 km is fully reprocessed. The smooth model instead allows an increasing fraction of the daughter-pair energy to escape as radius increases. The former is therefore an extreme sharp-boundary upper bound, not a physically motivated central prediction.

Polarization weighting changes the central/high-tail band correction by a few percentage points, but does not restore the \(70.9\%\) sharp-boundary suppression.

**Conclusion:** the energy-dependent daughter-neutrino boundary can modify the strong-endpoint luminosity, but the figure-level smooth transport model does not explain the \(+92\%\) Fig. 7 residual. The apparent agreement of the sharp 30 km proxy is an artefact of assuming complete reprocessing throughout the added shell.

## 6. Limitations

1. The daughter survival probability uses a radial \(\nu N\) scattering optical depth, not the heavy-flavor energy sphere.
2. The model treats a daughter scattering as energy reprocessing and omits recoil, correlations, degeneracy, weak magnetism, pair emission/absorption, and angular neutrino transport.
3. The 20--25 km density tail is extrapolated from a figure-level read-off.
4. Equal, longitudinal-only, and transverse-only polarization weights are diagnostics; the actual production density matrix is channel- and phase-space-dependent.
5. The full total-luminosity comparison is a band-only proxy; all other energy bins are held fixed.
6. The V8 phase-space total has non-bitwise NumPy grid hashes, although the B.1, \(R_{\max}=25\), and sharp \(R_{\max}=30\) band calculations close to the archived P1-C/P1-D results at \(10^{-11}\)--\(10^{-12}\).

No baseline \(R_{\max}\), B.2 opacity normalization, source, Fig. 7 digitization, or axial-vector output is modified.

## 7. Reproducibility

- Direct integration script: \`audit_b16_smooth_daughter_reprocessing_b2.py\`
- Machine-readable result: \`outputs/b16_smooth_daughter_reprocessing_b2_10mev_2026-11-10.json\`
- Daughter transport model: \`audit_b16_public_density_neutrino_transport_envelope.js\`
- Density-tail input: \`outputs/b16_public_density_neutrino_transport_envelope_10mev_2026-11-10.json\`
- Baseline source and opacity: P1-C and P1-D archived outputs.

The direct V8 computation is the calculation reported here. The Python script is the reproducible repository implementation; its independent rerun is not claimed as completed in this report.

## 8. Decision

Retain \(R_{\max}=25\) km as the literal Blinov baseline. Do not replace it with 30 km and do not use the sharp-boundary near-match as a corrected Fig. 7 result.

The smooth public-density transport model does not close the strong-endpoint discrepancy. A definitive energy-sphere calculation still requires same-snapshot heavy-flavor energy-changing collision kernels and neutrino moments. Until those are available, keep PR #57 Draft/Open and do not update the axial-vector constraint curve.

## References

1. A. Caputo, G. Raffelt, and E. Vitagliano, Phys. Rev. D 105, 035022 (2022), Fig. 1.
2. G. G. Raffelt, H.-T. Janka, and D. F. G. Fiorillo, “Neutrinos from core-collapse supernovae,” 2025 review manuscript.
3. N. Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B.
4. K.-C. Lai, C. S. J. Leung, and G.-L. Lin, Phys. Rev. D 110, 103023 (2024), arXiv:2401.16023.
