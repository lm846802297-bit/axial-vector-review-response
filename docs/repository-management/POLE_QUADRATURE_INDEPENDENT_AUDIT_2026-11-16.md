# Independent endpoint-quadrature audit — exact-momentum fermion poles

Date: 2026-11-16  
Disposition: **PASS_WITH_NOTES — numerical integration gate closed for the declared fermion-sector benchmark/grid**  
Scope: numerical evaluation of the finite \(B_0\) Feynman-parameter integrals and the six complex pole pairs in Benchmarks A/B. This is not acceptance of the full physical Higgs--singlet propagator.

## 1. Failure mechanism

The 2026-11-15 SciPy/QUADPACK tolerance scan emitted four roundoff warnings at every tested tolerance. The warnings were reproduced from the archived pre-repair source and localized to the muon--VLL heavy-light pairing:
\[
(m_i,m_j)\simeq(0.105653078,\ 20001.002766)\ \mathrm{GeV}.
\]
The relevant Feynman-parameter denominator is
\[
D(x)=xm_i^2+(1-x)m_j^2-x(1-x)s.
\]
The endpoint layer has characteristic scale
\[
\delta_x\sim\frac{m_\mu^2}{M_E^2}\simeq2.8\times10^{-11}.
\]
The old QUADPACK calls returned an estimated absolute error of approximately \(1.775\times10^{-7}\), above the requested \(2\times10^{-9}\).

## 2. Production repair

The production driver now evaluates the finite \(B_0\) integral with composite Gauss-Legendre quadrature:
- geometric panels resolve the heavy-light endpoint layer at \(x\simeq0\) or \(x\simeq1\);
- additional panels around the real-part roots resolve the narrow complex-log transition at open light-lepton thresholds;
- the production order is 64 Gauss-Legendre nodes per panel;
- the resonance-sheet continuation term is retained unchanged.

The production \(B_0\) path no longer calls SciPy/QUADPACK. The original tolerance-scan script remains reproducible against its immutable pre-repair Git commit and is explicitly historical.

## 3. Independent checks

The four legacy warning calls were evaluated independently with mpmath tanh-sinh at 50, 70 and 90 decimal digits, and with composite Gauss-Legendre at 64 and 96 nodes.

| Check | Maximum observed difference |
|---|---:|
| mpmath 50 vs 90 decimal digits | \(2.05\times10^{-51}\) |
| mpmath 70 vs 90 decimal digits | \(3.62\times10^{-72}\) |
| GL64 vs mpmath-90 | \(1.44\times10^{-15}\) |
| GL96 vs mpmath-90 | \(3.54\times10^{-15}\) |

The complete pole scan covers Benchmarks A/B at \(m_s=100,125.25,150\) GeV, giving six pole pairs. The production and convergence runs used GL orders 32, 48, 64, 96 and 128.

| Metric, compared with GL128 | Maximum difference |
|---|---:|
| Hard remainder | \(1.37\times10^{-12}\ \mathrm{GeV}^2\) |
| Pole mass | 0 at printed precision |
| Pole width | \(7.30\times10^{-16}\ \mathrm{GeV}\) |
| Complex \(R_{hh}\) | \(7.45\times10^{-10}\) |

Additional closure checks:
- Benchmark-A hard remainder at \(m_h^2\): \(0.02403044398676\ \mathrm{GeV}^2\), within \(8.9\times10^{-13}\ \mathrm{GeV}^2\) of the archived reference.
- Benchmark-B hard remainder at \(m_h^2\): \(0.005407723994595\ \mathrm{GeV}^2\), within \(1.2\times10^{-13}\ \mathrm{GeV}^2\) of the archived reference.
- Maximum determinant residual across the 12 poles: \(6.08\times10^{-9}\ \mathrm{GeV}^4\).
- Maximum \(|\sum R_{hh}-1|\): \(7.56\times10^{-9}\).
- Five regression tests pass: internal-mass symmetry, high-precision endpoint comparison, no production warnings, hard-coefficient reproduction, and all-six-pole/residue closure.

## 4. Reproduction

Run from the repository root:

```bash
python research/major1-higgs-scalar-mixing-20261109/pole_quadrature_independent_audit_2026-11-16.py
```

Then run the regression tests:

```bash
cd research/major1-higgs-scalar-mixing-20261109
python -m unittest -v test_exact_momentum_pole_quadrature.py
```

Pinned audit environment: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0. SciPy is used only to reproduce the historical warning; the production integrator uses NumPy.

Key files:
- Production source: `exact_momentum_fermion_pole_audit.py`
- Independent driver: `pole_quadrature_independent_audit_2026-11-16.py`
- Machine-readable output: `pole_quadrature_independent_audit_2026-11-16.json`
- Human-readable pole output: `exact_momentum_pole_audit.txt`
- Regression tests: `test_exact_momentum_pole_quadrature.py`
- Runtime pins: `pole_quadrature_audit_requirements.txt`

SHA-256 / Git provenance:
- Production source SHA-256: `04cb52b824bffc3df7d16b84a2356ef873ffbe2050db1381da926e19ed5156a7`
- Independent audit driver SHA-256: `c391b6a92f988cf0c5356fbdbb2d6ead18f32267af2e87a3ea83633161e2a278`
- JSON output Git blob ID: `e7c85ab5010f6af3eeab30ce242cf01ba62bbd73`
- Human-readable pole output SHA-256: `0ce70c4134a315a73003df1f9ae2083a44a53b0d292f325f80e6be5c12b66fec`
- Regression tests SHA-256: `8c2f6d5b37a45f3d6fc587982b208c9d80e31949a8d0ad53c658dc13eab5cd47`

## 5. Interpretation and remaining physics boundary

The numerical integration warning is closed for the declared two-benchmark, six-pole-pair grid. The hard coefficients and matched off-diagonal self-energy reproduce the archived benchmark values at sub-\(10^{-12}\ \mathrm{GeV}^2\) precision.

This does **not** establish a gauge-complete physical pole prediction. The calculation still uses fixed Plan-C-lite diagonal widths and omits the complete diagonal self-energies and field counterterms, the full same-order EFT counterterm/matching sectors, gauge/Goldstone/ghost completion, mixing-induced Standard-Model widths, and the detector-level coherent likelihood. The complex residues are not probabilities or standalone signal strengths. No allowed/excluded interval is inferred.


## 6. Current Git-tree checksum reconciliation (2026-11-16)

The SHA-256 values printed in Section 4 were compared against the actual current branch file bytes. The production-source SHA-256 **does match** the current exact_momentum_fermion_pole_audit.py, and the JSON output Git blob ID matches the current JSON file. Three other recorded SHA-256 values do not match the current Git-tree bytes:

| File | SHA-256 printed in Section 4 | SHA-256 of current Git-tree bytes |
|---|---|---|
| pole_quadrature_independent_audit_2026-11-16.py | c391b6a92f988cf0c5356fbdbb2d6ead18f32267af2e87a3ea83633161e2a278 | 867ecb2c81edeb15adb32e973c648597f9e926265128f28be6cbeb8c252daac3 |
| exact_momentum_pole_audit.txt | 0ce70c4134a315a73003df1f9ae2083a44a53b0d292f325f80e6be5c12b66fec | 257cfb36dfb776a72915a9cc74d5346a0b46b07f6580eb0c72cd5e6f323e2442 |
| test_exact_momentum_pole_quadrature.py | 8c2f6d5b37a45f3d6fc587982b208c9d80e31949a8d0ad53c658dc13eab5cd47 | 3be48a7d81550452bc3ff191c88e0d0c5ca8ae5cd6b83987a98849c4a19c0f52 |

For completeness, the current JSON SHA-256 is c8ff12e1d4430a31fd01f64864f28d985845d86119170bf6d58641387a034838, while its Git blob remains e7c85ab5010f6af3eeab30ce242cf01ba62bbd73. The JSON's embedded source_sha256 (04cb52b824bffc3df7d16b84a2356ef873ffbe2050db1381da926e19ed5156a7) matches the current production source.

The three nonmatching values above are preserved as the historical values printed by the original audit report; their origin was not established in this follow-up. They must not be cited as checksums of the current committed files. This is a provenance-record discrepancy, not evidence that the numerical results are wrong. The current values above are the byte-identity references for this branch.

The five regression-test methods are present in the current test module. No dedicated GitHub Actions run or committed standalone unittest stdout log for this pole-quadrature test was found on the audited branch. Accordingly, the Section 3 “five regression tests pass” statement is retained as a recorded local-run result, not represented as CI acceptance; this follow-up did not claim to rerun the suite.

No production source, numerical output, pole value, width, model input or physical constraint was changed by this checksum reconciliation.
