# Axial stellar-cooling constraint: calculation, reproduction, and independent-review record

**Prepared:** 2026-11-13  
**Repository:** `lm846802297-bit/axial-vector-review-response`  
**Pinned source revision:** `81d9b2faf16eb39879b759b05afce46732c925d7` (main at package preparation)  
**Calculation directory:** `research/stellar-cooling-constraints-20261105/`  
**Status:** reproducible fixed-profile benchmark; **not a physically validated final SN1987A exclusion**

> **Review warning.** This package preserves the calculation as it currently exists. It does not repair or conceal the unresolved pure-vector Blinov Fig. 7 discrepancy, does not replace the static-muon semi-Compton approximation with the moving-muon B.13 kernel, and does not reinterpret a successful software test as validation of the astrophysical transport model. Do not cite the plotted blue region as an unconditional exclusion until the physics gates in §10 have been closed.
>
> **Status boundary (2026-11-15):** the saved axial contour is an exploratory fixed-profile calculation, not an adopted or updated SN1987A axial constraint. The pure-vector Fig. 7 benchmark remains unpassed; under the current validation order, axial limit updates remain deferred until the vector baseline passes. Retain these arrays for provenance and diagnostic comparison only.

## 1. What the figure represents

The figure is a numerical post-processing calculation in the low-energy axial-vector EFT. It asks, for each mediator mass and coupling, whether the escaping ballistic luminosity from a prescribed stationary supernova profile exceeds a chosen cooling criterion.

The benchmark is conditional on:

- an SFHo-18.8 profile at \(t_{\rm pb}=1\) s;
- the reconstructed radial inputs described in §3, rather than the original Garching simulation tables;
- the three production/absorption channels implemented in `rates.py`;
- independent propagation of the \(L,+,-\) mediator polarization modes;
- the fixed-profile ballistic escape prescription in `transport.py`;
- the selected radius \(R_\nu=25\) km and the energy convention documented below.

It is **not** a hydrodynamic simulation, a diffusion calculation, an LESN analysis, a high-energy-neutrino recast, or a global exclusion of the UV-complete model.

### 1.1 EFT current convention

The scan uses
\[
\mathcal L_{\rm int}
=A'_\alpha\left[
-g_X\,\bar\mu\gamma^\alpha\gamma_5\mu
+g_X\,\bar\nu_\mu\gamma^\alpha P_L\nu_\mu
-g_X\,\bar\nu_\tau\gamma^\alpha P_L\nu_\tau
\right],
\]
with
\[
g_A^\mu=-g_X,\qquad g_V^\mu=0,\qquad
g_{\nu_\mu}=+g_X,\qquad g_{\nu_\tau}=-g_X.
\]

This is the pure-axial-muon EFT benchmark. In the original one-VEV model, the small-right-handed-mixing limit gives
\[
g_V^\mu/g_A^\mu=O(\theta_{\mu R}^2),\qquad
g_A^\mu\simeq-g_X.
\]
The finite vector component is not included in this scan. No extra Major 3 sterile-neutrino completion or second scalar VEV is introduced.

All rates in `rates.py` are returned at unit overall \(g_X^2\); the luminosity routine supplies the \(g_X^2\) production factor and \(g_X^2\) opacity factor.

## 2. Calculation chain

The calculation is organized as:

1. reconstruct the radial background \(T(r),\mu_\mu(r),\mu_{\nu_\mu}(r),N(r)\);
2. compute local production and inverse-process absorption rates for each mediator polarization;
3. construct reduced absorption rates using detailed balance;
4. integrate the reduced opacity along straight chords from each production point to the adopted escape radius;
5. average the survival probability over the initial propagation direction;
6. integrate the source over radius and energy to obtain \(L_{A'}(m_{A'},g_X)\);
7. find the coupling intervals for which \(L_{A'}\) exceeds the selected luminosity threshold;
8. render the contours and the optically-thin channel fractions from the archived JSON scans.

The principal programs are:

- `extract_profile.py`: public-figure vector-path extraction and profile construction;
- `rates.py`: mode-resolved local rates;
- `transport.py`: radial/energy integration, chord opacity and ballistic luminosity;
- `run_scan.py`: mass/coupling scan driver;
- `validate_outputs.py`: archived-scan integrity and sensitivity checks;
- `plot_constraints.py`: PDF/PNG rendering from saved scan files.

The separate `blinov_reproduction/` module is a scalar, literal Appendix-B reference implementation. It deliberately does not import the production `rates.py` or `transport.py`; it is a control lane, not the engine used to draw the axial contour.

## 3. Stellar background and provenance

### 3.1 Adopted sources

The profile file is
`data/sfho188_digitized.csv`, a 1,687-row vertex-preserving union grid. It contains a 0.05-km base grid plus retained PDF-polyline vertices and support-boundary knots.

| Input | Adopted source | Use |
|---|---|---|
| \(T(r)\) | [Caputo, Raffelt & Vitagliano, arXiv:2109.03244v3](https://arxiv.org/abs/2109.03244), Fig. 1 | Baseline temperature |
| \(\mu_\mu(r)\) | Same Caputo Fig. 1 | Baseline muon chemical potential |
| \(\mu_{\nu_\mu}(r)\) | Same Caputo Fig. 1, negative and positive branches | Muon-neutrino chemical potential |
| \(N(r)\) | [Ferreira, Marsh & Ravensburg, arXiv:2510.14469v1](https://arxiv.org/abs/2510.14469), Fig. 1, SFHo-18.8 curve | Lapse |

Source PDF archive members, SHA-256 digests, vector-path indices, axis calibrations, support ranges and representative samples are recorded in `data/profile_provenance.json`. The extraction script verifies the source PDF hashes before digitizing.

### 3.2 Explicit reconstruction assumptions

- The input is a reconstruction of published vector paths, **not** the original numerical simulation profile.
- Caputo's temperature path contains encoded vertices beyond the visible 20-km frame; the extracted path is used to 25 km without fitting a temperature tail.
- The first available core point, at about 0.1166 km, is extended constantly to \(r=0\).
- \(\mu_\mu\) is set to zero beyond the final encoded point at the 1-MeV logarithmic plot floor.
- The negative \(\mu_{\nu_\mu}\) branch ends at about 13.1099 km; the positive branch is available only from about 16.589 to 18.423 km. Unrepresented intervals, where the logarithmic plot does not resolve \(|\mu_{\nu_\mu}|<1\) MeV, are set to zero.
- \(\mu_{\nu_\tau}=0\) is used because a public radial profile for it is not supplied by the selected source.
- The lapse curve is encoded to about 24 km. From there to 25 km it is continued with a Schwarzschild exterior form matched continuously at the last plotted point. This is a boundary approximation, not a reconstructed metric solution.

The Caputo and Ferreira temperature paths agree over their common 0.2–20 km range to 0.267% maximum relative difference. The Caputo \(\mu_\mu/T\) path agrees with the independent Bollig Fig. 4 digitization at 0.0161% maximum and 0.00551% mean absolute relative difference. The Caputo muon density agrees with the Bollig Fig. 3 digitization at 3.73% mean and 10.45% maximum absolute relative difference over the common resolved range.

The Ferreira curve labelled \(\mu_\mu\) differs strongly from the Caputo curve despite the same nominal SFHo-18.8, 1-s label. It is retained only as a diagnostic column and is **not** used for the baseline \(\mu_\mu\). The origin of the published-curve discrepancy is unresolved; it is not converted into an invented statistical uncertainty.

No restricted Garching raw tables were accessed, redistributed, or reconstructed from credentials. Reviewers can regenerate the digitized profile from the public arXiv source archives using `extract_profile.py --download`, subject to the pinned source hashes.

## 4. Local rates and physical channels

Masses, energies, temperatures and chemical potentials are in MeV; densities are in MeV\(^3\); rates are in MeV; cross sections are in MeV\(^{-2}\). The electromagnetic factor \(e^2=4\pi\alpha\) is included in the semi-Compton matrix elements.

### 4.1 Semi-Compton scattering

The implemented process and inverse are
\[
\mu^\pm+\gamma\leftrightarrow\mu^\pm+A'.
\]

The code evaluates the tree-level \(s\)- and \(u\)-channel muon diagrams with exact vacuum two-body recoil, a finite muon mass, physical photon polarizations, and separate mediator \(L,+,-\) polarizations. The initial muon is at rest in the medium frame. The thermal target population is represented by
\[
n_\mu^{\rm eff}
=2\sum_{\mu^-,\mu^+}
\int\frac{d^3p}{(2\pi)^3}f_\mu(1-f_\mu).
\]
The spin/Jacobian normalization is already included in `transport.effective_muon_density`; no additional factor of two is to be applied.

This is a **muon-rest/effective-density approximation**, not the exact moving-muon thermal collision integral. It does not preserve the incoming/outgoing muon momentum correlation in the thermal scattering kernel. This is a leading physical limitation, especially because semi-Compton emission supplies about 91.4% of the optically thin source at 10 MeV.

### 4.2 Active-neutrino coalescence and inverse decay

The code includes
\[
\nu_\mu\bar\nu_\mu\leftrightarrow A',
\qquad
\nu_\tau\bar\nu_\tau\leftrightarrow A'.
\]
It retains Fermi occupation and blocking factors, the supplied \(\mu_{\nu_\mu}(r)\), and \(\mu_{\nu_\tau}=0\). The three polarization weights are treated separately. The two transverse circular modes need not have identical in-medium rates when the muon-neutrino chemical potential is nonzero.

### 4.3 Dimuon coalescence and inverse decay

For
\[
m_{A'}>2m_\mu\simeq211.3168\ {\rm MeV},
\]
the code includes
\[
\mu^+\mu^-\leftrightarrow A'.
\]
For a pure axial current the vacuum width per mediator is
\[
\Gamma_{A'\to\mu^+\mu^-}
=\frac{g_X^2m_{A'}}{12\pi}\,\beta_\mu^3,\qquad
\beta_\mu=\sqrt{1-\frac{4m_\mu^2}{m_{A'}^2}}.
\]
The finite-mass angular distributions and Fermi blocking are retained. The vector comparison has a different threshold factor and is not substituted into the axial result.

### 4.4 Detailed balance and reduced opacity

For each polarization and each included channel the implementation enforces
\[
\Gamma_h^{\rm prod}
=e^{-\omega/T}\Gamma_h^{\rm abs},
\qquad
\Gamma_h^{\rm red}
=\Gamma_h^{\rm abs}-\Gamma_h^{\rm prod}
=(1-e^{-\omega/T})\Gamma_h^{\rm abs}.
\]
Here \(\omega\) is the **mediator energy**, not the outgoing photon energy. The mode-resolved reduced opacity is the quantity used in the survival probability.

## 5. Ballistic propagation and luminosity

For a mediator produced at radius \(r\), energy \(\omega\), and initial direction cosine \(u=\cos\theta\), the code follows the straight chord to the spherical escape surface \(R_\nu=25\) km. Both initially outward and initially inward directions are included. The unit-coupling optical-depth column is
\[
\tau_h^{(0)}(r,\omega,u)
=\int_0^{s_{\max}}ds\,
\frac{\Gamma_h^{\rm red}(r'(s),\omega)}
{v_{A'}},\qquad
v_{A'}=\sqrt{1-\frac{m_{A'}^2}{\omega^2}}.
\]
The physical optical depth is \(g_X^2\tau_h^{(0)}\), and
\[
P_h(r,\omega)
=\frac12\int_{-1}^{1}du\,
\exp[-g_X^2\tau_h^{(0)}(r,\omega,u)].
\]

The escaped luminosity is
\[
\boxed{
L_{A'}=
g_X^2\sum_{h=L,+,-}
\int_0^{R_\nu}4\pi r^2dr\,N(r)^2
\int_{m_{A'}/N(r)}^\infty d\omega\,
\frac{k\omega^2}{2\pi^2}\,
\Gamma_{h,0}^{\rm prod}(r,\omega)
\left\langle e^{-g_X^2\tau_h^{(0)}}\right\rangle_u
}
\]
where \(\Gamma_{h,0}^{\rm prod}\) is the unit-\(g_X^2\) production rate and \(k=\sqrt{\omega^2-m_{A'}^2}\).

The implementation uses \(N^2\) in the luminosity weight and the local escape-energy threshold \(m_{A'}/N(r)\). Along the chord it uses the documented fixed numerical mediator energy \(\omega\) in the reduced-opacity evaluation. This is a leading-gravity stationary-profile prescription, **not** a full GR geodesic/transport calculation. The energy-frame ambiguity in the source paper is retained as an explicit limitation; the conserved-\(E_\infty\) diagnostic is not silently substituted for the literal fixed-\(\omega\) lane.

Unit conversions are:
\[
1\ {\rm km}=\frac{10^{18}}{197.3269804}\ {\rm MeV}^{-1},
\qquad
1\ {\rm MeV}^2=
\frac{1.602176634\times10^{-6}}{6.582119569\times10^{-22}}
\ {\rm erg\,s^{-1}}.
\]

The three polarization contributions are propagated separately:
\[
L_{A'}=\sum_h L_h,\qquad
L_h\propto Q_h e^{-\tau_h}.
\]
This is not algebraically equivalent to first summing opacities and then inserting the sum into one exponential. That distinction is central to the unresolved comparison with the scalar-opacity formula in the Blinov reference lane.

## 6. Parameter scan and contour construction

### 6.1 Baseline scan

The archived `outputs/axial.json` baseline has:

| Setting | Value |
|---|---:|
| Current | axial |
| Radial quadrature target `nr` | 88 |
| Energy nodes `ne` | 180 |
| Direction quadrature `na` | 24 |
| Chord/path quadrature `ns` | 64 |
| Semi-Compton scattering-angle order `nc` | 40 |
| Escape radius | 25 km |
| Energy offset | 1,200 MeV |
| Semi-Compton scale | 1 |
| \(\mu_{\nu_\mu}\) | reconstructed profile, not forced to zero |
| Coupling grid | 301 logarithmic points |
| Coupling range in saved JSON | \(10^{-14}\)–\(10^{-3}\) |
| Baseline mass rows | 75 |

The plot merges the 75 baseline masses with five endpoint masses (250, 255, 260, 265, 270 MeV), yielding 80 axial mass rows for the displayed axial contour. The vector control scan contains its own 75 mass rows. The scan JSONs, not a digitized version of the final PDF, are the numerical source of the figure.

The plotted axes show \(m_{A'}=0.01\)–500 MeV and \(g_X=10^{-14}\)–\(10^{-4}\). The saved coupling scan extends to \(10^{-3}\), but the displayed vertical range ends at \(10^{-4}\).

### 6.2 Cooling criteria

The primary contour is the set
\[
L_{A'}(m_{A'},g_X)=4.4\times10^{52}\ {\rm erg\,s^{-1}}.
\]
The filled blue region denotes the sampled/interpolated points above this criterion. The dotted contour at \(3.0\times10^{52}\) erg/s is a separate threshold sensitivity view, not an independent experimental exclusion.

For each mass, `run_scan.find_intervals` finds all crossings in \((\log g_X,\log L)\) and records every interval above threshold. It does not assume a single connected island. The black dashed curve in the figure is the pure-vector muon-current control using the same reconstructed profile and code family; it is **not** a claim that the published Blinov Fig. 7 vector curve has been reproduced.

### 6.3 Figure panels

- Left panel: axial \(4.4\times10^{52}\) erg/s contour and shaded benchmark region; dotted \(3.0\times10^{52}\) erg/s comparison; dashed internal vector control.
- Right panel: \(f_i^{\rm thin}=L_i^{\rm thin}/\sum_jL_j^{\rm thin}\) for Compton, neutrino coalescence, and dimuon coalescence. These are **optically thin production fractions before escape attenuation**, not fractions of the final escaped luminosity.
- Beige region: visible overlap with the original Fig. 2 display window. It is a visual comparison region only and does not convert this calculation into a global viability statement.
- MeV and GeV figures use the same saved scan. GeV figures change only the mass coordinate by \(m[{\rm GeV}]=m[{\rm MeV}]/1000\).

The current `plot_constraints.py` sends the saved arrays to Matplotlib `contour/contourf` in the native linear coordinate arrays and then sets logarithmic axes. This is not identical to the log-log interpolation used by `find_intervals`. The coupling grid is dense, but a reviewer should regard the plotted contour interpolation as a small presentation-level numerical issue to be checked. This package preserves the existing figure and code without silently changing either.

## 7. Representative saved results

For the \(4.4\times10^{52}\) erg/s criterion, the current scan gives:

| \(m_{A'}\) (MeV) | Lower \(g_X\) | Upper \(g_X\) |
|---:|---:|---:|
| 0.01 | \(3.8452\times10^{-13}\) | \(1.9583\times10^{-5}\) |
| 1 | \(3.8444\times10^{-11}\) | \(4.9445\times10^{-7}\) |
| 10 | \(3.6022\times10^{-10}\) | \(7.4721\times10^{-8}\) |
| 100 | \(2.3842\times10^{-10}\) | \(7.2587\times10^{-9}\) |
| 200 | \(4.1484\times10^{-10}\) | \(2.8626\times10^{-9}\) |
| 250 | \(7.3416\times10^{-10}\) | \(1.5193\times10^{-9}\) |
| 255 | \(8.1890\times10^{-10}\) | \(1.3528\times10^{-9}\) |
| 260 | no interval | no interval |

The endpoint is bracketed by the sampled masses:
\[
255\ {\rm MeV}<m_{A',\max}<260\ {\rm MeV}.
\]
Do not quote a more precise endpoint from this grid without a new, validated endpoint scan.

Optically thin source fractions:
- 10 MeV: Compton 91.388%, neutrino 8.612%, dimuon 0;
- 100 MeV: Compton 0.612%, neutrino 99.388%, dimuon 0;
- 250 MeV: Compton 0.080%, neutrino 87.600%, dimuon 12.320%.

At \(m_{A'}>2m_\mu\), the dimuon channel opens and changes the source hierarchy.

## 8. Numerical checks already recorded

The archived `outputs/numerical_validation.json` checks:

- the coupling arrays are increasing and luminosity arrays have the expected length, finite nonnegative values;
- thin-source fractions sum to one;
- stored \(4.4\times10^{52}\) and \(3.0\times10^{52}\) intervals reconstruct from the saved luminosities with relative tolerance \(5\times10^{-13}\);
- the optimized path-column contraction agrees with the reference implementation above \(10^{40}\) erg/s to \(2.03\times10^{-15}\) relative;
- the refined-low and refined-fast optimized calculations have identical settings and coupling grids, with the archived luminosity comparison below \(10^{-12}\);
- mass/coupling refinement, energy cutoff, radial/energy/angular/path quadrature and selected profile/opacity sensitivities are recorded in separate JSON files.

The baseline scan uses \(nr/ne/na/ns/nc=88/180/24/64/40\). The saved convergence scan uses 132/280/40/96/64; refined-fast uses 176/360/56/144/80. The coupling refinement uses 1,201 coupling points for selected masses.

These checks establish internal numerical consistency of the saved arrays and selected quadratures. They do **not** establish that the local rates, profile, opacity convention, or astrophysical transport prescription are the correct physical description.

## 9. Independent pure-vector reference lane

The `blinov_reproduction/` subdirectory implements a separate scalar Appendix-B prescription for comparison with [Blinov et al., arXiv:2511.09619v2](https://arxiv.org/abs/2511.09619). It is deliberately isolated from the production axial code.

It includes:
- an independent scalar implementation of the neutrino/dimuon rates and no-recoil semi-Compton prescription;
- the printed negative-muon degeneracy-factor convention;
- scalar reduced opacity and chord/direction averaging;
- a four-mass scan and comparison against digitized public Fig. 4 and Fig. 7 paths;
- its own tests and provenance fingerprints.

The digitized reference curves are public-PDF vector paths, not the authors' numerical tables. The current Fig. 7 10-MeV strong-absorption discrepancy remains large. The fixed-\(\omega\) literal lane has a recorded high-absorption residual of about +92.24%; a separate conserved-\(E_\infty\) diagnostic reduces but does not close it (about +35.97%). The Fig. 4 boundary agreement alone is not sufficient to pass the full luminosity benchmark.

The mode-resolved production lane and scalar literal reference lane answer different questions. In particular,
\[
\sum_h Q_h e^{-\tau_h}
\ne
\left(\sum_h Q_h\right)e^{-\sum_h\tau_h}.
\]
A scalar polarization-summed opacity is not automatically a valid single-particle survival rate when mode opacities differ. The choice must be resolved from the physical density-matrix/transport prescription, not tuned to reproduce a curve.

## 10. Open physics gates and applicability limits

The following issues remain open and must accompany any external review.

### P0 — pure-vector Fig. 7 gate is not passed

The 10 MeV high-absorption tail retains an approximately +92.24% residual in the literal fixed-\(\omega\) comparison. The separate conserved-\(E_\infty\) diagnostic is also not in agreement. No empirical opacity or profile rescaling is accepted. The vector control is therefore not a passed end-to-end validation of the shared transport calculation.

### P0 — mode-resolved versus scalar opacity prescription

The axial plot propagates \(L,+,-\) modes separately. The independent literal Blinov reference uses the scalar opacity prescription as printed. The nonlinearity of the survival exponential prevents an automatic equivalence. A principled physical derivation/decision is still required.

### P1 — moving-muon semi-Compton thermal integral

The production plot uses an initial-muon-rest approximation with an effective thermal density. It does not use the complete moving-muon B.13 thermal kernel. Moving-muon local-rate work exists separately, but it has not been integrated into this global axial transport scan. Do not apply a vector-derived correction factor to the axial curve.

### P1 — background and propagation

The background is reconstructed from public plots; the lapse is externally continued from 24 to 25 km; the tau-neutrino chemical potential is set to zero; the opacity chord uses the stated fixed-\(\omega\) convention. The 20-km escape-radius diagnostic shifts the upper boundary by about 25%–93% over the representative 0.01–250 MeV mass points; this is a model-radius sensitivity, not a calibrated uncertainty. These are physical/model uncertainties, not just numerical quadrature errors.

### Other excluded physics

The calculation does not include the complete in-medium photon dispersion, muon–proton bremsstrahlung, full GR ray tracing, hydrodynamic feedback, diffusion/thermalization, LESN energy deposition, high-energy-neutrino event limits, or a global scan of the original UV completion. The unshaded plot area is not a demonstrated allowed region.

## 11. Reproduction instructions

Use Python with NumPy, SciPy, Matplotlib; profile extraction additionally requires PyMuPDF. Run from the repository root:

```bash
python -m unittest discover -s research/stellar-cooling-constraints-20261105 -p "test_*.py" -v

python research/stellar-cooling-constraints-20261105/run_scan.py \\
  --mass-count 68 --nr 88 --ne 180 --na 24 --ns 64 --nc 40 \\
  --gmax 1e-3 --gcount 301 \\
  --output research/stellar-cooling-constraints-20261105/outputs/axial.json

python research/stellar-cooling-constraints-20261105/run_scan.py \\
  --mass-count 68 --nr 88 --ne 180 --na 24 --ns 64 --nc 40 \\
  --gmax 1e-3 --gcount 301 --current vector \\
  --output research/stellar-cooling-constraints-20261105/outputs/vector.json

python research/stellar-cooling-constraints-20261105/run_scan.py \\
  --masses 250,255,260,265,270 --nr 88 --ne 180 --na 24 --ns 64 --nc 40 \\
  --gmax 1e-3 --gcount 301 \\
  --output research/stellar-cooling-constraints-20261105/outputs/endpoint.json

python research/stellar-cooling-constraints-20261105/validate_outputs.py
python research/stellar-cooling-constraints-20261105/plot_constraints.py
```

To regenerate the reconstructed profile from the pinned public source PDFs:
```bash
python research/stellar-cooling-constraints-20261105/extract_profile.py --download
```

The independent vector lane can be run separately using its own `blinov_reproduction/README.md` instructions. Do not merge its scalar opacity prescription into the axial production lane without an explicit physics decision.

## 12. Review package contents and integrity

The accompanying archive is a curated snapshot of the calculation inputs, programs, outputs, figures, tests, and validation/audit notes at the pinned main revision above. It contains no restricted Garching simulation data. It preserves the original generated figures and JSON rather than regenerating or modifying them during packaging.

The package index and file-level SHA-256 manifest are included inside the archive. The repository's Git blob SHA-1 values are useful for locating the exact source blobs but are not substitutes for the package SHA-256 checksums.

Recommended reviewer sequence:

1. Verify the package checksum and the pinned source revision.
2. Inspect `data/profile_provenance.json` and regenerate `sfho188_digitized.csv` from the public source PDFs.
3. Re-run the local tests and `validate_outputs.py`.
4. Recompute the axial, vector and endpoint scans from the archived profile.
5. Re-run `plot_constraints.py` and compare the generated PDFs/PNGs bytewise or visually.
6. Inspect the independent Blinov reference lane and its Fig. 4/Fig. 7 residuals.
7. Resolve the P0/P1 physics gates in §10 before treating the contour as a final astrophysical exclusion.

**Recommended external description:** “A reproducible, mode-resolved axial-EFT ballistic-cooling benchmark on a reconstructed SFHo-18.8 profile, supplied for independent technical review. The vector Fig. 7 validation gate and several transport/profile approximations remain open; the plot is not presented as a final SN1987A exclusion.”
