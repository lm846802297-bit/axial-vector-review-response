# Research status matrix — 2026-11-13

This table separates work completed, numerical/code acceptance, and physical interpretation. A passing test is not automatically a passed physics benchmark.

| Workstream | What has been done | Current status | What is still required |
|---|---|---|---|
| Axial EFT model mapping | Effective axial muon current, model-to-EFT coupling convention, single-VEV and two-VEV mapping records, decay-width code | Documented; model variants kept distinct | Freeze the UV benchmark and map final UV parameters to the plotted EFT coupling before claiming a UV-model limit |
| Axial semi-Compton matrix element | Dirac-trace implementation with three massive-vector polarizations; exact vacuum recoil with initial muon at rest | Implemented and covered by unit tests | Replace the initial-muon-rest thermal approximation by the full moving-muon thermal kernel in the production axial scan |
| Axial neutrino and dimuon channels | Coalescence / inverse-decay rates with Fermi blocking and detailed-balance relations | Implemented in the benchmark | Check in-medium dispersion and transport assumptions; retain dimuon threshold and channel bookkeeping |
| Polarization-resolved detailed balance | Per-polarization production / absorption identities and independent audit records | Numerical identities tested | Decide from the physical transport prescription whether propagation is mode-resolved or requires a density-matrix treatment |
| Reconstructed SN background | Public-plot digitization, profile provenance, Caputo / Bollig / Esseili–Kribs cross-checks, lapse and neutrino-chemical-potential audits | Public reconstruction and cross-checks completed; not identical to the private Garching snapshot | Obtain or justify one internally consistent profile and quantify reconstruction uncertainty |
| Official SFHo-FRDM EOS parsing | Official table parsing, physical dimensions / grid alignment, thermodynamic and free-nucleon closure, regression tests | 35/35 recorded tests pass, including real-table tests | EOS tables do not supply the missing time- and radius-dependent Garching supernova snapshot |
| B.13 moving-muon local kernel | Moving Fermi-gas collision kernel, exact outgoing-energy support, angle / energy / momentum quadrature and anchor comparisons | Substantial local-kernel and sampled-convergence work completed | Integrate the validated kernel into axial production / absorption and global transport |
| B.13 global diagnostics | Radial, energy, angular, and path convergence records; exact moving-muon global alternative retained separately | Global diagnostic runs and convergence records archived | Not the same as a completed axial-EFT global scan; does not close B.16/Fig. 7 mismatch |
| B.16 / Blinov pure-vector Fig. 4 | Ballistic boundary reconstruction and numerical comparison | Boundary agreement recorded at about 1.5% (lower) and 2.9% (upper) for the checked mass set | Keep exact mass set and digitization uncertainty attached to the claim |
| B.16 / Blinov pure-vector Fig. 7 | Independent scalar Appendix-B lane, local-rate checks, path / angular integration, outer-shell and profile diagnostics | **Not passed end-to-end** | 10 MeV strong-absorption tail remains discrepant; resolve source / opacity / energy-frame / transport without empirical rescaling |
| Fig. 7 10 MeV weak-to-strong comparison | Weak-source and strong-absorption discrepancies separated; multiple independent audits archived | Open physical benchmark | Reconcile weak-source difference and large strong-absorption tail against the reference prescription |
| C4-C3 direct local recomputation | 1,204 local neutron/proton × neutrino/antineutrino records, anchor recomputation, 301-radius opacity / optical-depth comparisons | Direct numerical archive and comparisons completed | Local collision / opacity diagnostics, not a full luminosity or escape-probability solution |
| C4-C4 energy dependence | 7,224 local-rate rows across six incident energies; 340 stratified high-order cases; radial-grid comparisons | Sampled numerical convergence passed at stated thresholds | Flat-space, fixed-local-energy diagnostic only; no redshift, angular transport, energy redistribution, or full luminosity acceptance |
| Axial global scan | 75 baseline mass rows plus five endpoint rows; 301 logarithmic coupling points; three production channels; three polarizations | Saved scan, numerical validation, and presentation figures exist | Rerun after physical gates are resolved; current output is not the final model limit |
| Constraint-plot construction | Saved JSON is numerical source; 4.4e52 erg/s primary threshold and 3.0e52 erg/s sensitivity contour | Reproducible presentation pipeline; review-only log-log boundary implementation added separately | Compare original Matplotlib interpolation to per-mass log-log crossings; retain distinction between visual interpolation and physics uncertainty |
| UV completion / scalar and portal effects | Original UV and two-VEV mapping, EFT-literature checks, scalar and model assumptions recorded separately | Partial model context | No complete global UV parameter scan or full scalar / portal contribution is included in the stellar-cooling contour |

## Interpretation labels

- **Completed:** the named calculation or audit has been executed and archived.
- **Numerically passed:** the stated test, closure, or convergence criterion passed for its documented domain.
- **Partially validated:** one layer passed, but a separate physical or end-to-end layer remains open.
- **Open:** the required calculation or physical decision has not been accepted.
- **Not included:** the effect is outside the current benchmark.

## Current decision

The existing axial figure is a **conditional fixed-profile ballistic benchmark**. The vector Fig. 7 gate is not passed, the axial production scan still uses an initial-muon-rest semi-Compton approximation, and the background / propagation prescription is not a full self-consistent GR supernova transport calculation. Therefore the contour is useful for review and development, but it is not yet the final SN1987A exclusion of the underlying UV model.


## Two-VEV formula and local-thermal cross-check (2026-11-13)

The exact gauge-mass and eaten-Goldstone algebra is checked in PHYSICS_CROSSCHECK_2026-11-13.md. The recorded two-VEV local tests cover the mapping, vacuum semi-Compton amplitude, current-level widths under restricted neutrino assumptions, and a homogeneous optically thin polarization-summed thermal smoke test.

The vacuum tree-level axial-current/Goldstone amplitude identity is now checked directly (PR #105; maximum tested relative residual below 9.0e-13). Still open: the physical CP-odd scalar spectrum; full mass-basis treatment of charged right-handed neutrinos if active-heavy mixing or heavy thresholds matter; the finite-right-mixing UV Goldstone phase projection; independent azimuthal quadrature convergence; medium-rest-frame T/L-resolved opacity; and radial SN transport. These checks do not change the NOT PASSED 10 MeV pure-vector Fig. 7 acceptance gate.
