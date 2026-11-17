# Individual review: Belle II scan run logs and metadata

Baseline `5568277429b76c3bb7684dfd5edb92b113fbd12f`, 2026-11-15. Each record below was read and its role checked against the prior scan provenance audit. From the collider-recast directory, the ten test modules named in `unit-tests.txt` were rerun with Python 3.12.14 and NumPy 2.3.5: 69 tests passed in 9.329 s. This is not a rerun of the 73,728-row scan, an experimental efficiency validation or proof that the underlying physics limits are complete.

| Path under `research/radial-scalar-collider-recast-2026-10-28/` | Individual review and disposition |
|---|---|
| `data/derived/independent-audit-2026-11-09/independent_belleii_pointwise_tests.txt` | Historical five-test pointwise log; the same five tests passed in the current rerun. Its threshold, interpolation and interval tests do not determine detector efficiency. HISTORICAL. |
| `data/derived/scan-pr52-thetaR-1e-2/numerical-dependencies.txt` | Historical run environment records NumPy 2.3.5; this is not a complete dependency lockfile. HISTORICAL. |
| `data/derived/scan-pr52-thetaR-1e-2/python-version.txt` | Historical run used Python 3.13.18; current rerun used 3.12.14 and must not be misidentified as the archived execution. HISTORICAL. |
| `data/derived/scan-pr52-thetaR-1e-2/source-commit.txt` | Current stored scan provenance points to `b362de7cc345ec75ef9f4ae117364c1ee59e6e4d`; the earlier 2026-11-09 run instead used `4e90cd…`, as documented in `SCAN_RUN_RECORD_2026-11-09.md`. This records a historical run input, not current HEAD. HISTORICAL. |
| `data/derived/scan-pr52-thetaR-1e-2/unit-tests.txt` | Historical log contains 69 successful tests. The same ten module names were run now and all 69 passed, including bound ordering; current runtime and interpreter differ. No production scan was rerun. HISTORICAL. |
| `independent_fourbody_tensor_tests.txt` | Historical four-test tensor/quadrature log; all four tests passed in the current suite. Agreement with this independent implementation and sampled convergence is not a complete collider detector recast. HISTORICAL. |

The prior audit identified that the earlier and current archived scans have different bound-column conventions and hashes; both runs remain distinct. The currently stored 80 MB expanded scan is still only available compressed in the repository, and this review does not claim to have extracted and committed it.
