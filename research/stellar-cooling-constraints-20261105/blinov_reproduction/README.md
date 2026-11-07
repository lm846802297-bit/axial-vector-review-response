# Independent Blinov vector reproduction

This directory is a deliberately separate implementation of the **vector-boson** ballistic-cooling prescription in Blinov et al., arXiv:2511.09619v2, Appendix B, Eqs. (17)--(35). The word scalar below refers only to the paper's mode-summed (scalar) opacity treatment; it does not mean a scalar mediator.

## Independence boundary

- reference.py does not import the production rates.py or transport.py.
- Neutrino/dimuon thermal rates are evaluated with an independent Fermi-integral antiderivative.
- Semi-Compton production follows the paper's nonrelativistic-muon/no-recoil cross-section prescription, including the explicit velocity and photon-polarization factors in Eqs. (30)--(32).
- The muon degeneracy factor follows Eq. (33) literally, with the single negative-muon distribution printed in the paper. It does not add a positive-muon term.
- Scalar opacity follows Eqs. (18)--(21), with full chord integration and angular averaging.
- Luminosity follows Eq. (17), including the lapse-squared factor and local escape-energy threshold.

This is a literal scalar-prescription reproduction path, not a claim that scalar opacity is physically equivalent to mode-resolved propagation when mode opacities differ. It does not infer the private implementation choices of the paper's authors.

## Run

From the repository root:

    python research/stellar-cooling-constraints-20261105/blinov_reproduction/reference.py \
      --profile research/stellar-cooling-constraints-20261105/data/sfho188_digitized.csv \
      --masses 1,10,100,200 \
      --nr 40 --ne 100 --na 16 --ns 32 \
      --output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/blinov_literal_scan.json

All numerical inputs, quadrature orders, profile filename, and outputs are saved in the JSON. The profile is the existing reconstructed SFHo-18.8, 1 s profile, not an original simulation table.

## First independent run: numerical status

The initial 40/100/16/32 quadrature run (radial/energy/angular/path orders) used the reconstructed SFHo-18.8 profile and the literal scalar Appendix-B prescription. It gives the following figure-digitization comparison at the four Fig. 4 mass points:

| Mass | Lower-bound difference | Upper-bound difference |
|---:|---:|---:|
| 1 MeV | +0.81% | -0.86% |
| 10 MeV | +0.33% | +0.97% |
| 100 MeV | -0.89% | +0.98% |
| 200 MeV | -1.31% | +2.60% |

The Fig. 7 pointwise comparison is not uniformly successful:

| Mass | Maximum absolute relative difference | Mean absolute relative difference |
|---:|---:|---:|
| 1 MeV | 5.54% | 1.60% |
| 10 MeV | 91.35% | 15.64% |
| 200 MeV | 1.59% | 0.71% |

In particular, the 10 MeV curve agrees to roughly 7--9% at the lower-coupling end, crosses through a close-match region, and then departs strongly in the high-absorption tail. The largest sampled discrepancy is about 91%. Therefore the close Fig. 4 boundary match does **not** establish full Fig. 7 reproduction. This is a useful diagnostic result, not a passed reproduction claim.

The comparison is conditional on the reconstructed profile and digitized public figure paths. It is not a like-for-like reproduction with the authors' original numerical profile/table, and it does not establish the authors' private scalar-opacity implementation. The 10 MeV discrepancy remains open for controlled one-factor-at-a-time checks.

The scan JSON records the reference-code SHA-256, profile SHA-256, quadrature settings, and GitHub run commit. The comparison JSON records its own code hash and the hashes of the Fig. 4/Fig. 7 digitized inputs and provenance.

## 10 MeV Fig. 7: first controlled profile diagnostic

The first one-factor diagnostic varies only the reconstructed muon-neutrino chemical-potential profile, applying the same modified profile consistently to neutrino-pair production and inverse-decay absorption. It compares scales 0, 0.5, 1, and 1.5 against the 25 digitized Fig. 7 points. This is a sensitivity test only; no scale is selected by fitting the published curve.

The baseline scale-1 calculation gives a 15.73% mean absolute relative residual and a 92.24% maximum residual when evaluated at the exact digitized coupling points. The earlier 15.64% / 91.35% values used interpolation on the scan grid; the small difference is a comparison-grid effect.

| muon-neutrino chemical-potential scale | Mean absolute residual | Maximum residual | High-coupling residual |
|---:|---:|---:|---:|
| 0 | 15.12% | 92.14% | +92.14% |
| 0.5 | 15.29% | 92.17% | +92.17% |
| 1 (baseline) | 15.73% | 92.24% | +92.24% |
| 1.5 | 16.36% | 92.35% | +92.35% |

The low-coupling residual changes from -7.82% to -9.91%, while the residual near the reference peak changes from +2.97% to +2.08%. Thus varying this profile input over the tested range does not remove the high-coupling tail discrepancy. The muon-neutrino chemical-potential reconstruction is **not supported as the dominant explanation** for the 10 MeV mismatch.

The diagnostic output is archived in `outputs/fig7_10mev_numu_sensitivity.json`, including all 25 pointwise residuals, the profile hash, Fig. 7 PDF hash, quadrature orders and triggering commit.

The next controlled test holds the production source fixed and separately rescales the neutrino inverse-decay and Compton opacity components. This identifies which absorption channel controls the high-coupling tail; the rescaled cases are diagnostics, not alternative physical predictions.

### 10 MeV Fig. 7: channel-resolved opacity sensitivity

A second diagnostic holds the production source fixed and rescales only the inverse-process opacity components. It uses the same 25 digitized Fig. 7 couplings and the same quadrature as the baseline. These perturbations intentionally do **not** preserve detailed balance between the modified opacity and the unchanged source; they are localization tests only and must not be interpreted as physical curves or correction factors.

| Opacity-only diagnostic | Mean absolute residual | Maximum residual | High-coupling residual |
|---|---:|---:|---:|
| Baseline | 15.73% | 92.24% | +92.24% |
| Neutrino opacity × 0.5 | 223.60% | 2556.92% | +2556.92% |
| Neutrino opacity × 2 | 36.14% | 93.63% | -93.63% |
| Compton opacity × 0.5 | 26.68% | 190.23% | +190.23% |
| Compton opacity × 2 | 7.85% | 9.12% | +1.20% |
| All opacity × 0.5 | 326.09% | 4050.12% | +4050.12% |
| All opacity × 2 | 38.13% | 95.54% | -95.36% |

The strong response to Compton-opacity rescaling shows that the high-coupling tail is sensitive to this contribution in the current implementation. In particular, doubling only the Compton opacity moves the digitized Fig. 7 curve close to the reference. **This does not establish that the Compton opacity is missing a factor of two.** The test deliberately changes absorption without changing production, so it violates the detailed-balance pairing that a physical rate must obey.

The implementation was checked against the literal Appendix-B chain, Eqs. (29)--(35): the production expression includes the explicit factor of two for photon spin states and the 1/v_V factor in Eq. (32); the inverse rate follows Eq. (35); the reduced opacity is formed as (1-e^{-\omega/T})\Gamma_{\rm abs} in Eq. (20), and the path optical depth includes the additional 1/v_V in Eq. (18). Thus the diagnostic identifies where the luminosity is sensitive, but it does not yet identify an algebraic omission.

The next step is a matched detailed-balance audit of the Compton forward and inverse phase-space integrals, including the cross-section direction and the Eq. (34) forward/reverse phase-space ratio. Only a correction that preserves the same physical production/absorption pair may be adopted. The saved pointwise results are in `outputs/fig7_10mev_opacity_sensitivity.json`.

### Independent Compton cross-section / detailed-balance audit

The dedicated module `compton_detailed_balance_audit.py` independently evaluates the tree-level `mu + boson -> mu + boson` QED/vector-current amplitude with Dirac traces, physical photon/vector polarization vectors, and exact two-body recoil. It does not import `reference.py`, `rates.py`, or `transport.py`.

The audit validates the following identities:

1. For unpolarized cross sections,
   `sigma_forward / sigma_reverse = (g_mu g_V)/(g_mu g_gamma) * (p_f/p_i)^2 = 3 r^2/2`,
   with `r=p_f/p_i`. The muon spin factor cancels; the remaining (3/2) is the ratio of the three massive-vector to two photon polarizations.
2. In the no-recoil limit, (r\to v_V=\sqrt{1-m_V^2/\omega^2}), recovering Blinov Eq. (34).
3. The Eq. (31) and Eq. (32) rate coefficients agree algebraically when the same phase-space ratio is used: (3r\,\sigma_{\rm reverse}=2\sigma_{\rm forward}/r). In the no-recoil limit this becomes (3v_V\sigma_{\rm reverse}=2\sigma_{\rm forward}/v_V).
4. The forward and inverse Fermi/Bose occupation factors independently give (Gamma_{\rm abs}/\Gamma_{\rm prod}=e^{\omega_V/T}), recovering Eq. (35); the muon chemical potential cancels.
5. The independent QED amplitude reproduces the Klein--Nishina total cross section for the massless-photon limit and recovers Eq. (30) in the Thomson/no-recoil limit (within 1% for the selected low-energy test point).

The direct numerical forward/reverse cross-section comparison agrees with the exact phase-space prediction to better than (10^{-10}) over the scanned points. The Eq. (31)/(32) coefficient identity has the same numerical accuracy. Thus **Eq. (34), the polarization counting, and the cross-section direction are not the source of the 10 MeV discrepancy in this implementation**.

#### Finite-recoil diagnostic at (m_V=10) MeV

The stationary-muon exact two-body threshold is
[
\omega_{\rm th}=m_V+\frac{m_V^2}{2m_\mu}=10.4733\;\mathrm{MeV},
]
whereas the no-recoil threshold used in Eq. (30) is (omega>m_V=10) MeV.

| (omega) (MeV) | (r/v_V) | (sigma_{\rm exact}/\sigma_{\rm Eq.(30)}) | Exact/Eq.(32) rate coefficient |
|---:|---:|---:|---:|
| 12 | 0.8643 | 0.7287 | 0.8431 |
| 15 | 0.9425 | 0.7604 | 0.8068 |
| 20 | 0.9683 | 0.7317 | 0.7556 |
| 30 | 0.9822 | 0.6654 | 0.6774 |
| 50 | 0.9901 | 0.5690 | 0.5746 |
| 100 | 0.9952 | 0.4384 | 0.4405 |

The suppression of the exact vacuum cross section relative to Eq. (30) at (omega\sim 10\)--(100) MeV is primarily the finite-energy/recoil correction to the Thomson-like no-recoil expression; it is not a failure of Eq. (34). At (m_V=10) MeV, the exact threshold also differs visibly from the no-recoil threshold.

**Scope limitation:** these are exact vacuum two-body cross sections for a stationary initial muon. They are not a full supernova thermal rate: thermal muon momentum averaging, Pauli blocking, and the stellar distribution must be included before replacing Eq. (30) in a physical SN calculation. The paper explicitly presents Eq. (30) in its nonrelativistic-muon/no-recoil approximation and notes that semi-Compton production is mainly relevant for (m_V\lesssim\mathrm{MeV}). Therefore the exact-recoil result is recorded as a validity diagnostic, not substituted into the literal Blinov reproduction.

The finite-recoil correction lowers the Compton rate relative to the Eq. (32) no-recoil prescription on this stationary-muon slice. Since the existing 10 MeV calculation already lies above the digitized reference at the high-coupling tail, this correction points in the wrong direction to explain the missing opacity. It does **not** justify the artificial factor-two opacity test.

The full pointwise scan, cross-section ratios, phase-space residuals, and Eq. (31)/(32) residuals are archived in `outputs/compton_detailed_balance_audit.json`, including the code hash and triggering commit. The test suite also checks the Klein--Nishina limit, Eq. (30) Thomson limit, exact threshold, Eq. (34), and Eq. (35).


## 4B pure-vector benchmark audit

The existing literal scan is already the independent pure-vector reference path for Blinov Fig. 7; do not create a second Compton implementation merely to duplicate it. The fast audit builder checks the stored SHA-256 links between the reference implementation, reconstructed SFHo profile, refined scan and digitized Fig. 7 source:

```bash
python research/stellar-cooling-constraints-20261105/blinov_reproduction/build_pure_vector_benchmark.py
```

It writes `outputs/pure_vector_literature_benchmark.json`. The audit uses the current arXiv v2 equation numbering: Eq. (29) collision integral, Eq. (30) nonrelativistic/no-recoil cross section, Eqs. (31)--(32) production rate, Eq. (33) degeneracy factor, Eq. (34) forward/reverse cross-section ratio and Eq. (35) detailed balance. Avoid referring to these as “B.13--B.19”; the HTML/PDF version used here numbers them as Eqs. (29)--(35) within Appendix B.

The current refined comparison is **not a full Fig. 7 reproduction pass**. The 10 MeV curve has a large high-absorption-tail residual (about 92%), even though the 1 and 200 MeV curves agree at the percent level and the 10 MeV peak is much closer. The discrepancy must be resolved by matched physical source/opacity checks, not by fitting an opacity multiplier. The audit output records the exact residuals and all source hashes; it does not relabel the benchmark as passed.

## Comparison ladder

1. Compare independently implemented local neutrino and dimuon production rates with the archived analytic checks in vector_reference.py; do not import that file into the implementation.
2. Compare the no-recoil semi-Compton rate with the Eq. (30) cross-section formula and its Thomson limit.
3. Compare scalar optical depth and angular escape with Eqs. (18)--(21), first in constant-opacity test cases.
4. Compare resulting Fig. 7 luminosity curves and Fig. 4 cooling intervals against digitized Blinov reference points.
5. Only after this reference path is understood, compare it against the existing mode-resolved production solver under deliberately matched inputs.

The reference path is not used to update the axial plot, referee response, or manuscript.


## 10 MeV equation-chain audit

The targeted Eq. (17)--(20), Eq. (31)--(33) audit is documented in [FIG7_10MEV_EQUATION_CHAIN_AUDIT_2026-11-07.md](FIG7_10MEV_EQUATION_CHAIN_AUDIT_2026-11-07.md), with machine-readable output in `outputs/fig7_10mev_equation_chain_audit.json`.

The local Compton coefficient, Eq. (33) susceptibility identity, Eq. (20) reduced-absorption identity, Eq. (17) energy Jacobian, and Eq. (18) path/angular quadrature checks pass. An independent direct angular integral also verifies the neutrino production kernel and Eq. (B10) detailed balance at 48 points (maximum residuals 6.4e-14 and 1.0e-15). The 10 MeV Fig. 7 curve still does not pass.

At the high-absorption point, the source-weighted mean optical depth at 25 km is about 14.48 from inverse neutrino decay and 1.65 from semi-Compton absorption. The 24--25 km shell adds about 0.928 optical depth, almost entirely from neutrino absorption. This shows that the large high-coupling residual is not primarily a Compton-normalization problem.

A uniform ±5% temperature-profile sensitivity, with source and opacity recomputed together, moves the high-tail residual from +92% to +31% / +175%. This is a stress-test diagnostic, not a fitted temperature adjustment; the separately digitized Caputo and Ferreira temperature curves agree within 0.18% at sampled radii from 1 to 24 km, so ±5% is not an uncertainty inferred from that cross-check. A separate conserved-energy redshift-along-ray diagnostic lowers the high-coupling luminosity by about 29%, reducing the high-tail residual from about +92% to about +36%; it is not substituted into the literal reference because the printed Eq. (B2) does not display the local-energy transformation explicitly.

The exact PDF-vector digitization audit confirms that the 10 MeV reference consists of 25 visible centerline vertices extracted from the original PDF (not screenshot pixels); ordinary digitization error is therefore not a plausible explanation for the tail mismatch. The printed Eq. (18) explicitly carries the same \\(\\omega\\) along the chord, and the literal reference implementation follows that fixed-`omega` prescription. The conserved-`E_inf` calculation remains an alternative transport diagnostic, not the literal Eq. (18) reproduction.

New radial/energy/cutoff refinements change the luminosity by at most 0.14%, much smaller than the weak-source residual (-8.9%) and strong-absorption residual (+92.2%). At weak coupling the escape fraction is 0.9979, so its mismatch is a source-integral issue. At high absorption, 59.1% and 37.4% of escaped luminosity originate at 5--10 km and 10--15 km, respectively; the high-coupling discrepancy is controlled by propagation from the inner production region through the overlying material.

The outer 24--25 km shell contributes a source-weighted mean extra optical depth of about 0.93 at the high-coupling point. The paper explicitly fixes (R_{\max}=R_\nu\simeq25\,\mathrm{km}), so the 24 km truncation is a sensitivity diagnostic only. No opacity factor is fitted or adopted.
