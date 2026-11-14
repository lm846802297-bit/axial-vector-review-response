# Individual review: B.16 chemical-potential and temperature sensitivity notes

Baseline `e7ae59ce523a244787ac1dd09afdbe16a7f36a45`, 2026-11-15. Each of the six documents was read and its scenario count, strong-endpoint ratios and quoted interpretation compared to the corresponding committed JSON. The six named scripts and digitized-profile SHA-256 are present. This review did not rerun B.1/B.2, independently digitize literature figures or establish the physical background uncertainty.

| Note under `research/stellar-cooling-constraints-20261105/blinov_reproduction/` | Individual check and disposition |
|---|---|
| `B16_INNER_NUMU_BRANCH_SENSITIVITY_8_12KM_2026-11-09.md` | Five stored scenarios; removing the branch gives strong escaped ratio `0.99977723` and sign reversal is unity at stored precision, consistent with the table. Controlled stress test only. PASS_WITH_NOTES. |
| `B16_NUMU_POSITIVE_BRANCH_SENSITIVITY_2026-11-09.md` | Four scenarios; zeroing the branch gives strong escape `0.99985907` and escaped luminosity `0.99987143` relative to baseline, consistent with prose. Positive-branch test does not validate the entire outer profile. PASS_WITH_NOTES. |
| `B16_OUTER_NUMU_FLOOR_SENSITIVITY_20_22KM_2026-11-09.md` | Three scenarios; the ±1 MeV pair gives identical stored strong ratios `1.00009148` for luminosity. Figure-floor scenarios are not measured profiles. PASS_WITH_NOTES. |
| `B16_OUTER_NUMU_SENSITIVITY_22_25KM_2026-11-09.md` | Five scenarios; ±1/±3 MeV strong luminosity ratios `1.00017211`/`1.00150500`, with sign-pair equality at stored precision. Converted 45 literal newline escape sequences into actual line breaks; no text or numeric results removed. PASS_WITH_NOTES. |
| `B16_OUTER_TEMPERATURE_SENSITIVITY_20_22KM_2026-11-09.md` | Three scenarios; strong ratios for 0.9/1.1 temperature factors `0.99850741`/`1.00150728` agree with table. This is not a statistical uncertainty determination. PASS_WITH_NOTES. |
| `B16_OUTER_TEMPERATURE_SENSITIVITY_22_25KM_2026-11-09.md` | Five scenarios; strong luminosity ratios for 0.7/0.9/1.1/1.3 factors agree with the archive to printed precision, including `1.12474203` for 1.3. Off-frame temperature points are not raw simulation data. PASS_WITH_NOTES. |

The tables show controlled changes of a reconstructed vector-model background. They do not resolve the strong-coupling Fig. 7 discrepancy, justify tuning a profile, or validate an axial-vector exclusion. All six JSON files and output results were retained; the single edit only repairs formatting.
