# Exact-momentum pole quadrature tolerance audit

Date: 2026-11-15. This is the historical pre-repair SciPy/QUADPACK tolerance scan. It is retained to document why the endpoint quadrature was replaced; it is not the current production implementation and does not validate the physical pole model.

## Reproduction of the historical scan

Run from the repository root:

```bash
python research/major1-higgs-scalar-mixing-20261109/pole_quadrature_tolerance_audit_2026-11-15.py
```

The script now retrieves the immutable pre-repair source from commit `5522ae1081f61a711fc846168370542efdef9a35` with `git show`, verifies its SHA-256 (`e391afbc3b2f75305a3f31209aac209b3aa4f1104cd0f13c68f0159064b08246`), and varies only the two archived `scipy.integrate.quad` settings: `epsabs=epsrel=2e-8, 2e-9, 2e-10`.

The scan covered Benchmarks A/B and \(m_s=100,125.25,150\) GeV, giving six complex pole pairs. All three tolerance settings emitted four roundoff warnings. Pole masses and widths were stable; the maximum complex \(R_{hh}\) change was \(5.81\times10^{-8}\). The QUADPACK warning estimate was about \(1.78\times10^{-7}\) for each affected real integral.

## Superseding result — 2026-11-16

The warning was traced to the heavy-light \(\mu\)-VLL pairing, with masses approximately \(20{,}001.003\) and \(0.105653\) GeV. The denominator develops an endpoint layer of scale
\[
\delta_x\sim \frac{m_\mu^2}{M_E^2}\simeq 2.8\times10^{-11}.
\]

The production driver now evaluates the finite \(B_0\) Feynman-parameter integral with composite Gauss-Legendre panels, geometric endpoint refinement, and additional panels around the real-part roots at open thresholds. The original four warning calls were independently checked using mpmath tanh-sinh at 50/70/90 decimal digits. The composite Gauss-Legendre result at 64/96 nodes agrees with the 90-digit reference within \(3.6\times10^{-15}\) in the dimensionless \(\overline B_0\) value for all four points.

The full two-benchmark/six-pole-pair scan was repeated at GL orders 32, 48, 64, 96 and 128. Across orders 32–128, the maximum hard-remainder change is \(1.37\times10^{-12}\,\mathrm{GeV}^2\), the maximum pole-mass change is zero at printed precision, the maximum width change is \(7.30\times10^{-16}\,\mathrm{GeV}\), and the maximum complex \(R_{hh}\) change is \(7.45\times10^{-10}\). The largest determinant residual is \(6.08\times10^{-9}\,\mathrm{GeV}^4\), and \(|\sum R_{hh}-1|<7.56\times10^{-9}\).

See [the independent quadrature audit](../../docs/repository-management/POLE_QUADRATURE_INDEPENDENT_AUDIT_2026-11-16.md), its machine-readable JSON, and the regression tests. The numerical integration warning is closed for the declared fermion-sector benchmark/grid. This does not complete the gauge/Goldstone/ghost propagator, diagonal self-energies and counterterms, full EFT matching, physical widths, or detector-level coherent likelihood.
