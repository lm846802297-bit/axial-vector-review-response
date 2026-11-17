# Seven baseline issues — evidence update (2026-11-17)

This note records new source and numerical checks for the seven `REVISION_REQUIRED` baseline items. It does **not** promote an item to resolved merely because a report or archive exists. Where the requested evidence is still missing, the item remains open.

## 1. B.16 escape phase-space energy-grid fingerprint

The failed audit run `43205614274` used Python 3.12.16, NumPy 2.5.4, and SciPy 1.18.1. The archived baseline and failed run agree on the source-grid and opacity-grid fingerprints, node counts, and the exact SFHo profile input. They disagree only on the 842-node energy-grid fingerprint.

The profile file

`research/stellar-cooling-constraints-20261105/data/sfho188_digitized.csv`

has SHA-256:

`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`

which is the fingerprint recorded by the baseline. Reconstructing the 842-node energy grid from that profile with Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 reproduces the baseline energy-grid SHA-256 exactly:

`036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3`.

The failed run's energy-grid SHA-256 was `db6f613c…`. This isolates the mismatch to the numerical environment / floating-point grid construction, not to a changed stellar profile or radial grid. PR [#119](https://github.com/lm846802297-bit/axial-vector-review-response/pull/119) pins the baseline-compatible environment and reruns the audit. **The item remains open until the full B.16 run completes and joint/marginal closure passes.**

## 2. Fig. 7, 10 MeV handoff package

The repository's `FIG7_10MEV_LOCAL_RATE_POLARIZATION_ESCAPE_AUDIT_2026-11-13.md` identifies the missing self-contained 10 MeV local-rate / polarization / escape handoff. The filename `10MeV_Localization_Addendum_2026-11-13.zip` is mentioned in PR #106's description, but the ZIP and its direct-run script, raw CSV/JSON, plot, and pinned-input manifest are not present in the merged repository tree or in the inspected PR #106 workflow artifacts.

The P1-B exact-B.13 artifact is a different diagnostic package. It is **not** a substitute for the Fig. 7 10 MeV local-rate/polarization/escape package. No Fig. 7 10 MeV number is being reconstructed from that unrelated artifact. **Item 2 remains open pending the actual original package or a fully reproducible replacement calculation.**

## 3–4. Muon-density convention and 12–15 km profile provenance

The exact SFHo-18.8 digitized profile SHA-256 is the value recorded in §1 above. It matches the B.16 baseline input. The existing same-radius Caputo/Bollig comparison is retained in:

- `BOLLIG_MUON_DENSITY_AND_B1_SOURCE_AUDIT_2026-11-09.md`
- `outputs/bollig_muon_density_b1_source_audit_2026-11-09.json`

For an explicit convention check, I evaluated both charge-conjugate Fermi populations using the profile's interpolated (T(r)) and (mu_mu(r)):

[
n_{mu^-} = \frac{1}{\pi^2}\int_0^\infty
\frac{p^2\,dp}{\exp[(\sqrt{p^2+m_\mu^2}-\mu_\mu)/T]+1},
\qquad
n_{\mu^+} = \frac{1}{\pi^2}\int_0^\infty
\frac{p^2\,dp}{\exp[(\sqrt{p^2+m_\mu^2}+\mu_\mu)/T]+1},
\]
[
n_{\mu,\mathrm{net}}=n_{\mu^-}-n_{\mu^+}.
]

The integrals include the ((\hbar c)^{-3}) conversion to fm(^{-3}). A 160-point Gauss–Legendre calculation was cross-checked against adaptive SciPy quadrature. At the representative radii:

| (r) (km) | (T) (MeV) | (mu_\mu) (MeV) | (n_{\mu^-}) (fm(^{-3})) | (n_{\mu^+}) (fm(^{-3})) | (n_{\mu,\mathrm{net}}) (fm(^{-3})) |
|---:|---:|---:|---:|---:|---:|
| 12.0 | 25.982703 | 93.732680 | 1.94368090e-3 | 1.66478e-6 | 1.94201612e-3 |
| 12.5 | 23.881959 | 90.216585 | 1.40718979e-3 | 8.40062e-7 | 1.40634973e-3 |
| 13.0 | 21.750736 | 85.954969 | 9.38592014e-4 | 3.85617e-7 | 9.38206397e-4 |
| 13.5 | 19.612070 | 80.988349 | 5.63118684e-4 | 1.57712e-7 | 5.62960972e-4 |
| 14.0 | 17.470751 | 75.818483 | 3.00067339e-4 | 5.37729e-8 | 3.00013566e-4 |
| 14.5 | 15.340100 | 69.191025 | 1.25404847e-4 | 1.55874e-8 | 1.25389259e-4 |
| 15.0 | 13.231416 | 62.282718 | 4.01355190e-5 | 3.31169e-9 | 4.01322073e-5 |

Across 12–15 km, (n_{\mu^+}/n_{\mu^-}) decreases from (8.565\times10^{-4}) to (8.251\times10^{-5}). Thus replacing (n_{\mu^-}) by the net density changes the result by at most 0.086% in this shell. It cannot explain the reported several-percent Caputo/Bollig profile difference.

The existing digitized comparison also finds that Caputo's plotted (n_\mu) tracks the one-species (n_{\mu^-}) calculation more closely than the net-density calculation. This supports the one-species interpretation for the Caputo profile, but the published plot label does not explicitly define the antiparticle subtraction. The Bollig Fig. 3 label remains ambiguous. No density rescaling or cross-simulation profile splicing is justified.

**Evidence status:** the CSV fingerprint and same-location comparison are now explicit; the physical Caputo/Bollig density discrepancy remains an open interpretation issue. Do not silently replace the one-species B.1/B.17 target density with a net density.

## 5. PR #52 benchmark scan archive (generated later in PR #68)

PR #52 introduced the original-model collider calculation, but its changed-file list did not contain the generated scan archive. The scan archive was generated later in PR #68. It is therefore more precise to call this the **PR #52 benchmark scan archived by PR #68**, not a scan artifact originally produced in PR #52.

The current archive provenance is:

- Workflow run: [#42560249275](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42560249275)
- Job: `unit-tests-and-width-scan`, job ID `128974876738`
- Exact source commit recorded in the archive: `b362de7cc345ec75ef9f4ae117364c1ee59e6e4d`
- Runtime: Python 3.13.18, NumPy 2.3.5
- Tests: 69 passed, 0 failed
- Grid: (48\times48\times32=73{,}728) points; (	heta_{\mu R}=\theta_{\tau R}=10^{-2}); three-body/four-body quadrature orders 192/128
- Uncompressed CSV SHA-256 declared by the run: `5d5f0ce3…`
- Summary JSON SHA-256: `98e507bbc00e8966b71722238d5326ab9802f6dd12f03cd6de42fcb322671664`
- Compressed `.csv.gz` Git blob SHA-1: `12af1bcaa8aa991bd9071375004900fa13f8aafd` (this is a Git object ID, **not** the compressed-file SHA-256).

The five calculation-source SHA-256 values in `source-sha256.txt` were independently recomputed from the corresponding repository files and match the manifest. The workflow log records the CSV hash, `gzip -9` compression, and archive commit. The older 58-test / source-commit-`4e90cd9` record is historical and must not be used as the current archive's provenance.

The repository connector does not return the binary contents of this large compressed file, so I have **not** independently decompressed the committed `.gz` bytes in the current environment. The current run's generation and source hashes are verified; byte-for-byte decompression against the declared CSV hash remains the final archive-integrity check. The uncompressed CSV is about 80.8 MB, so it should not be committed as an ordinary Git blob without an explicit size decision; retain the compressed archive and its extraction/hash procedure in the meantime. **Item 5 remains open for the independent compressed-byte/decompressed-CSV check.**

## 6–7. Original-UV and Two-VEV semi-Compton convergence provenance

The two model directories contain the same generic thermal-kernel driver and the same convergence CSV:

- `stellar_semi_compton_thermal_rate.py`: same Git blob in both branches (`d37023df…`)
- `stellar_semi_compton_thermal_convergence.py`: same Git blob in both branches (`e36ab13…`)
- `thermal-convergence-2026-11-05.csv`: same Git blob in both branches (`075314…`)

The current convergence driver does **not** reproduce the committed CSV schema/reference convention. It emits `relative_*_to_reference` quantities and takes the highest requested Gauss–Legendre order (order 12 in this table) as the order-sweep reference. The committed CSV instead has `relative_*_percent` columns with the order-10 row set to zero. Its order-sweep values are consistent with

[
100\left(\frac{R_n}{R_{10}}-1\right),\qquad
100\left(\frac{Q_n}{Q_{10}}-1\right),
]

where (R) is the rate and (Q) the emissivity. The exact historical producer/run was not recovered. **Direct-producer attribution to the current driver is withdrawn; the CSV is retained as a legacy table with its order-10 reference formula explicitly stated.**

The CSV has ((n_{\rm GL},n_\phi)=(6,12),(8,16),(10,20),(12,24)), with (n_\phi=2n_{\rm GL}). Both quadrature orders change together. This is a **joint convergence sequence**, not independent azimuthal convergence. The cutoff rows hold ((n_{\rm GL},n_\phi)=(10,20)) fixed while varying the listed cutoff. No independent (n_\phi)-only convergence claim is supported by this table.

The Original-UV and Two-VEV validation notes must both point to this same provenance statement. The Two-VEV document's table is not a second, independent model-specific data set. The thermal kernel is shared; the VEV-dependent mapping/width assumptions remain separate from the generic semi-Compton quadrature table.

The archived Original-UV width-script blob `8f2d320858bd16173f16bed72af3d1cf1d8a8625`, current Original-UV file blob `32cc5221…`, and Two-VEV file blob `be2aefbd9078f43b8aa586f5516ce4caf953a107` have different documentation/print-header content, but their executable width-function bodies were compared and are identical. `axial_decay_widths.py` is not imported by the thermal-convergence driver, so this blob difference is not the source of the CSV.

The quoted (|W_V|_{\max}=2.252\times10^{-9}) and (|W_A|_{\max}=2.159\times10^{-9}) are absolute residual magnitudes for the stated benchmark check. They are not relative residuals and are not a parameter-space-wide bound. Preserve that benchmark-specific convention.

**Evidence status:** items 6–7 are reclassified correctly as a legacy joint-convergence table with unverified direct producer and no independent azimuthal convergence claim. The numerical table is retained without changing its values.

## Status discipline

No scientific result is promoted to a full pass by this note. Item 1 awaits the full B.16 rerun and closure checks; item 2 awaits the actual Fig. 7 10 MeV package or a reproducible replacement; item 5 awaits independent decompression/hash verification. Items 3–4 now have explicit density conventions, input fingerprint, and same-location comparison, while the Caputo/Bollig discrepancy and Bollig figure-label convention remain visible. Items 6–7 have explicit provenance limits and are not described as independent convergence evidence.
