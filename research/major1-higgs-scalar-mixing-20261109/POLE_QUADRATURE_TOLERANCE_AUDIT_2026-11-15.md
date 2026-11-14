# Exact-momentum pole quadrature tolerance audit

Date: 2026-11-15. This is a numerical stability diagnostic for `exact_momentum_fermion_pole_audit.py`. It does not alter the self-energy formula, repair the quadrature, or validate the physical pole model.

## Reproduction

Run from the repository root:

```bash
python research/major1-higgs-scalar-mixing-20261109/pole_quadrature_tolerance_audit_2026-11-15.py
```

The driver reads the adjacent exact-momentum pole script and varies only both `scipy.integrate.quad` settings, using `epsabs=epsrel` of `2e-8`, `2e-9` (the archived setting), and `2e-10`. It recomputes the two benchmarks at `m_s = 100, 125.25, 150 GeV`, records all six complex pole pairs, captures `IntegrationWarning`, and writes the machine-readable result JSON. Input SHA-256: `e391afbc3b2f75305a3f31209aac209b3aa4f1104cd0f13c68f0159064b08246`.

Runtime recorded by the script: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0.

## Result

| Requested `epsabs = epsrel` | Integration warnings | Maximum change vs. `2e-9` in pole mass | Maximum change in width | Maximum change in complex (R_{hh}) |
|---:|---:|---:|---:|---:|
| `2e-8` | 4 | (9.95\times10^{-14}\) GeV | (5.68\times10^{-13}\) GeV | (5.81\times10^{-8}) |
| `2e-9` | 4 | baseline | baseline | baseline |
| `2e-10` | 4 | (0) GeV | (1.61\times10^{-14}\) GeV | (5.18\times10^{-9}) |

The four warnings at the archived setting were traced to the heavy–light internal pairing with masses approximately (20{,}001) GeV and (0.10565) GeV, at complex (s) near (10{,}000)–(15{,}688 mathrm{GeV}^2). The Feynman-parameter denominator has a narrow endpoint layer in this mass hierarchy. A separate exploratory endpoint remapping at tighter tolerances still generated a roundoff warning for a light (	au	au) cut interval; that trial is not adopted as a fix.

## Interpretation and disposition

Across the requested tolerance scan, the pole masses and widths are stable far beyond their displayed precision, and the complex Higgs-channel residues are stable to better than (6\times10^{-8}). However, all three runs still emit four warnings, so QUADPACK does not certify the requested local integration error. The archived pole digits are numerically stable under this particular tolerance variation, but a second integration method or analytic (B_0) representation is still required before the quadrature issue can be closed. Keep the exact-momentum note and cascade note `REVISION_REQUIRED` pending that independent check.

The calculation remains the fermion-sector subset documented in the source note: fixed diagonal widths, incomplete counterterm/gauge sectors and no detector-level likelihood. This audit does not promote its pole estimates to physical Higgs–singlet predictions.
