# P1-B / B.2: exact B.13 Compton kernel in the 210–510 MeV transport band

## Fixed conventions

SFHo-18.8, t_pb = 1 s; m_A' = 10 MeV; pure-vector endpoint gV/gX = 1, gA/gX = 0. The exact-recoil moving-muon B.13 Compton kernel includes both muon charges and all three physical A' polarizations. Neutrino inverse-decay rates are evaluated mode by mode for nu_mu + nu_tau.

The path convention is literal fixed omega along Euclidean flat-space chords to R = 25 km; no GR redshift is introduced. The ten energy nodes in 210–510 MeV are selected from the full 842-node grid (200 logarithmic base nodes plus opacity-lapse threshold nodes); B.1 energy weights are computed on that full grid before selecting the band. Source radial order 200, opacity radial grid 642, angle order 32, path order 64, neutrino order 64.

## 1. B.16 baseline closure

The independent B.16 scalar calculation gives

\[
L_{B16}^{210-510}=1.7017848289\times10^{52}\;\mathrm{erg/s}.
\]

This reproduces the archived P1-C high-energy band result 1.701785e52 erg/s at relative residual -1.01e-7. The B.1 source measure, energy weights, chord geometry, angular averaging and B.2 scalar path integration are therefore closed against the established baseline before changing the Compton kernel. The exact mode-summed neutrino production agrees with the scalar neutrino reference at maximum relative residual 1.05e-12.

## 2. Local exact B.13 polarization audit

At seven radii (8, 10, 12.5, 15, 18.5, 20, 22 km) and six fixed energies (12, 20, 80, 210, 300, 510 MeV), the exact B.13 kernel was evaluated at 42 points. All 42 pass the 0.1% successive-order criterion. Maximum successive-order change is 0.099700%; maximum detailed-balance residual is 1.10e-14; maximum final-muon mass-shell residual is 1.71e-13. All rates are finite and nonnegative.

For a like-for-like comparison with the printed B.16 single-negative-muon Compton approximation, exact B.13 mu-minus-only Compton production is 0.1578–0.8312 of B.16 over the 42-point grid (median 0.3401). Including mu-plus, the ratio is 0.1595–0.8683 (median 0.3493). The largest local reduction in total reduced opacity is 55.7% in the inner high-energy sample. The integrated mu-plus contribution to the 210–510 MeV B.13 Compton thin source is only 0.717%.

## 3. High-energy-band B.1/B.2 transport

| Prescription | Escaped luminosity (erg/s) | Ratio to B.16 scalar | Escape fraction |
|---|---:|---:|---:|
| B.16 literal scalar sum | 1.701785e52 | 1 | 0.23458% |
| B.13, mu-minus only, scalar sum opacity | 2.099447e52 | 1.23367 | 0.46734% |
| B.13, both charges, scalar sum opacity | 2.100126e52 | 1.23407 | 0.46684% |
| B.13, both charges, equal-occupation average opacity | 6.071388e53 | 35.6766 | 13.4961% |
| B.13, both charges, independent mode-resolved transport | 6.058125e53 | 35.5987 | 13.4666% |

The B.13 thin source is 62.01% of the B.16 thin source. Its composition is 80.43% neutrino and 19.57% Compton, whereas B.16 is 49.88% neutrino and 50.12% Compton. The reduced B.13 Compton source is partly offset by a larger scalar-sum escape fraction, leaving the B.13 scalar-sum escaped band luminosity 23.4% above B.16.

The mode-resolved B.13 result is 28.85 times the B.13 scalar-sum result. Equal-occupation average-opacity and independent mode-resolved luminosities differ by only 0.22%. These are distinct transport prescriptions: the literal scalar prescription applies the survival factor to the sum of three mode opacities, while mode-resolved transport applies a separate survival factor to each mode. The mode-resolved value is not a multiplicative correction to the scalar B.2 result.

## 4. Exact B.13 versus B.14 polarization weights

B.13 Compton source fractions are 0.1757% longitudinal and 49.9122% in each transverse mode. B.14 no-recoil weights applied to the same B.13 scalar Compton source give 0.07990% longitudinal and 49.9600% in each transverse mode. Although the longitudinal fraction differs by a factor of about 2.2, its absolute contribution is small. Holding the B.13 scalar source and opacity fixed, the luminosity difference between the exact B.13 split and B.14 weights is only 0.0024%. Thus the approximately 8.4% difference between exact-B.13 and archived B.14 mode-resolved band luminosities is driven by the overall Compton source/opacity magnitude, not the detailed polarization split.

Exact-B.13 mode luminosity fractions are 29.92% longitudinal, 34.78% plus and 35.30% minus. Source-weighted mean optical depths per g_X^2 are 1.2005e15, 1.2238e15 and 1.2612e15.

## 5. Energy-support tail and limitations

The Global-03 B.13 interpolation table covers x=(omega-m_A')/T up to 36. At r=15 km and omega=510 MeV (x=38.54), the direct local B.13 Compton-to-neutrino reduced-opacity ratio is 0.3068%; at r=18.5 km it is already below 2.3e-9 and falls further at 20–22 km. The B.13 Compton opacity is set to zero outside the interpolation support in this run. The 0.3068% value is a local boundary bound, not a separately integrated global truncation error.

This is not a full-band Fig. 7 reproduction. The path result uses the low-order full-profile B.13 table with the Global-04 selected high-order validations; it is not an exhaustive high-order scan at every radius-energy node. It does not update the SN1987A limit or axial-vector exclusion curve. Fixed-omega and GR-redshifted path-energy conventions remain separate.

## Next step

Extend exact-B.13 source and mode-resolved reduced absorption to the full energy range, preserve the literal B.16 scalar lane as regression baseline, and separately test fixed-omega versus GR-redshifted path energy. Only after the full-band vector baseline is reconciled should the axial calculation or exclusion curve be updated.

Reproducibility archive: `P1B_B2_EXACT_B13_HIGH_ENERGY_AND_LOW_X_PILOT_2026-11-14.zip`, SHA-256 `afeb8a909cd973835066bda34a06da0de94bf8290135b6a7be278d454562b0b0`.


## 7. Full-band low-x support gate

The full B.2 energy grid reaches a relevant minimum local coordinate
\[
x_{\min}=\frac{m_{A'}/N_{\max}-m_{A'}}{T_{\max}}=0.0221811,
\]
when a photon emitted near the outer lapse threshold traverses the hottest shell. The existing Global-03 interpolation table starts at x = 0.5, so it cannot yet support a full-band B.2 calculation.

A local high-order pilot covered x = {0.01, 0.025, 0.05, 0.1, 0.25, 0.5} at r = 8.482141 km, plus x = 0.01 at r = 12.5 km. All seven completed points pass the 0.1% successive-order criterion; the maximum final change is 0.03292%, detailed-balance residuals are below 6.2e-16, and final-muon shell residuals below 1.63e-13. The pilot was planned for 24 points but timed out after seven, so it is not a global low-x interpolation scan.

**Next prerequisite for full-band transport:** construct and validate a low-x extension starting at x = 0.01 across the radial profile, then merge it with the existing x >= 0.5 table. Until that is done, the 210–510 MeV band result is the only exact-B.13 global transport band claimed here.
