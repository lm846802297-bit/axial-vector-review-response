# P1-IIIe-C4-C4-B: full-radial incident-energy dependence

Date: 2026-11-13  
Branch: `research/c4c4-energy-dependence-20261112`  
Status: calculation executed and archived; numerical-integrity, stratified quadrature, and radial-grid checks pass. Physical interpretation remains a fixed-local-energy, flat-space scattering diagnostic only.

## 1. Objective

Extend C4-C4-A from four anchor radii to the complete 301-point SFHo-18.8 radial profile. For each incident local energy, compute the EOS moving-nucleon neutral-current total-scattering rate, target-resolved opacity, and fixed-local-energy flat-space radial optical depth.

This stage remains a local-scattering diagnostic. It is not a redshifted transport calculation or a supernova cooling exclusion.

## 2. Fixed grid and case accounting

- Incident local energies: 10, 20, 40, 60, 100, and 150 MeV. This remains an exploratory grid, not a physical endpoint or an approved exclusion interval.
- Radius: all 301 profile nodes from 0.20 to 15.20 km, at 0.05 km spacing.
- Targets: neutron and proton.
- Incoming states: neutrino and antineutrino.
- Cases per energy: 301 × 2 × 2 = 1204.
- New direct calculations: five non-100-MeV energies × 1204 = 6020.
- Reused 100-MeV baseline: 1204 C4-C3 rows.
- Merged data set: 7224 rows, with provenance retained per row.

The C4-C3 100-MeV data are reused only after their profile, occupation, source, and archive blob identities are checked. The existing C4-C3 archive is never overwritten.

## 3. Kernel and numerical prescription

Use the unchanged C4-B2/C4-C1/C4-C2 implementation:

- EOS effective masses in quasiparticle energies and spinors;
- EOS chemical potentials and Fermi occupations;
- initial-state occupation and final-state Pauli blocking;
- existing weak form factors and separate neutron/proton and neutrino/antineutrino channels;
- exact outgoing-energy support recomputed for every energy, radius, target, and angular node;
- the existing 45 T kinetic-tail cutoff and 10,001-point support scan;
- base quadrature (N_cos, N_E', N_p, N_phi) = (8, 48, 36, 12);
- `kappa_N(E,r) = xi_SPP(r) Gamma_N^avail(E,r)`, with `xi_SPP` applied exactly once.

The Numba contraction accelerator is reused from the C4-C3 local recomputation implementation (source blob `821e39edfe235f5a8fcac6b2e074bb0dcb9631c6`). It changes only the innermost Dirac-matrix contraction; the original unaccelerated C4-C4-A anchor values provide the energy-dependent regression reference.

## 4. Radial quadrature cross-check

The C4-C4-Aq check covers four radii. C4-C4-B adds a stratified full-profile diagnostic at 17 indices:

`0, 30, 60, 90, 96, 120, 140, 142, 143, 160, 180, 196, 220, 240, 260, 280, 300`.

These include the endpoints, the existing 5 km and 10 km anchors, and the C4-C3 total-opacity peak region near 7.3–7.35 km.

For the five newly computed energies this gives 17 × 5 × 2 × 2 = 340 high-order cases. Compare the base orders (8, 48, 36, 12) with combined high orders (12, 72, 48, 16). The working threshold is 1% per case. A failure must be archived and localized; it must not be hidden by changing the production quadrature without a documented reason.

This is a stratified radial convergence diagnostic, not a pointwise high-order calculation at every radius.

## 5. Radial optical depth

For each energy and each target/sign channel, form

[
\tau_N(E,r)=\int_r^{15.20\,\mathrm{km}}\kappa_N(E,r')\,dr'.
]

Also form neutron-plus-proton total optical depths separately for neutrinos and antineutrinos. Use the same trapezoidal radial integration convention as C4-C3.

Compare the 0.05 km result with 0.10 km and 0.25 km subsampled grids at common nodes. Require nonnegative opacity, nonnegative outward optical depth, radial monotonicity, and a maximum normalized radial-integration difference below 1%.

## 6. Required independent checks

1. Exactly 6020 new local cases and 1204 reused 100-MeV cases, with no missing or duplicate keys.
2. Exact profile and occupation input blob SHA checks.
3. Exact C4-C3 100-MeV archive blob SHA check.
4. Exact C4-C4-A 96-row archive blob SHA check.
5. The 80 non-100-MeV anchor rows at the four C4-C4-A radii reproduce the original unaccelerated anchor results within (10^{-8}).
6. The 16 100-MeV anchors agree with C4-C3 at the same tolerance.
7. All local rates, opacities, and mean free paths are finite and positive; support-root residuals remain below (10^{-7}).
8. `kappa_N/(xi_SPP Gamma_N^avail)=1` to floating-point precision.
9. All 340 stratified high-order comparisons are archived; the 1% threshold is reported separately from the software-integrity checks.
10. Radial optical depths are nonnegative and monotone; 0.10 km and 0.25 km comparisons are reported separately for each energy and channel.

## 7. Separate source and data records

The source-code commit contains the calculation driver, tests, workflow, and this research record. The numerical output is archived separately under outputs/c4c4_energy_dependence_radial_2026-11-13/. The archive README, summary, provenance, and SHA-256 manifest record the executed run.

Planned output directory:

`outputs/c4c4_energy_dependence_radial_2026-11-13/`

Planned files:

- `local_rates_7224.csv`
- `energy_scaling_ratios_7224.csv`
- `channel_ratios_1806.csv`
- `radial_opacity_tau_1806.csv`
- `quadrature_convergence_340.csv`
- `summary.json`
- `README.md`
- `SOURCE_PROVENANCE.md`
- `SHA256SUMS.txt`

The source-code and data commits are staged together for review in this PR. The merge decision concerns archival of this bounded diagnostic only; it does not promote the result to a full transport solution or literature-reproduction acceptance.

## 8. Interpretation boundary

The local incident energy is held fixed at each sampled radius. The resulting optical depth is therefore a flat-space, fixed-local-energy diagnostic. It does not include gravitational redshift, energy redistribution, angular transport, escape probabilities, hydrodynamic feedback, or the full Blinov Fig. 7 luminosity calculation.

Numerical-integrity and quadrature checks do not constitute physical acceptance. Any interpretation of the energy dependence must remain conditional on the stated EOS profile, kernel, energy convention, and radial domain.


## 9. Executed result and acceptance summary

The archived run contains 7,224 local-rate rows: 6,020 newly computed rows at 10, 20, 40, 60, and 150 MeV, plus 1,204 reused 100-MeV rows from the byte-pinned C4-C3 baseline. The 96 C4-C4-A anchor rates reproduce to a maximum relative difference of \(3.33\times10^{-16}\).

The 340 stratified high-order cases pass the 1% combined-quadrature criterion; the maximum recorded relative difference is \(8.31\times10^{-5}\). The 0.10-km and 0.25-km radial-grid comparisons pass the 1% criterion, with maximum relative differences \(1.34\times10^{-5}\) and \(1.28\times10^{-4}\), respectively. The maximum support-root relative residual is \(8.27\times10^{-13}\). The exact case grid, finite-positive outputs, density closure, and single application of \(\xi_{\rm SPP}\) are recorded as passing in the machine-readable summary.

These checks establish numerical integrity and the stated sampled convergence checks for this diagnostic. They do not validate the flat-space fixed-local-energy approximation as a supernova transport prescription, nor do they establish an escape probability, full Blinov Fig. 7 reproduction, or SN1987A exclusion. See the co-located README.md, SOURCE_PROVENANCE.md, summary.json, and SHA256SUMS.txt for the exact archive and input identities.
