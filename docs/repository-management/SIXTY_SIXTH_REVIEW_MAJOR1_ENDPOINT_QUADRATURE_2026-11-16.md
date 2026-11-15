# Sixty-sixth review — Major 1 exact-momentum endpoint quadrature

Date: 2026-11-16  
Reviewed branch: maintenance/repository-organization-audit-20261114  
Review scope: the three register entries tied to the exact-momentum pole quadrature warning, plus the production source, independent audit, numerical outputs and regression tests.

## 1. Findings and repairs

1. **BENCHMARK_A_CMS_VECTOR_CASCADE_2026-11-10.md** — the note's only blocking register issue was the unresolved QUADPACK warning in the pole/residue input. The warning is now independently resolved. The cascade estimate remains explicitly an isolated-pole, conditional theory estimate; CMS pseudoscalar acceptance is not transferred to a spin-1 axial vector, and no vector-specific recast or exclusion is claimed. Disposition: PASS_WITH_NOTES.
2. **EXACT_MOMENTUM_FERMION_MATCHED_POLES_2026-11-10.md** — the endpoint-sensitive QUADPACK implementation was replaced by composite Gauss-Legendre with geometric endpoint and open-threshold root-neighbourhood panels. The four old warning points agree with mpmath tanh-sinh to \(3.6\times10^{-15}\); the full six-pole grid converges through GL order 128. Physical-model limitations remain explicit. Disposition: PASS_WITH_NOTES.
3. **exact_momentum_pole_audit.txt** — replaced the pre-repair output summary with the new 64-node production results, all six pole pairs, residuals, residue sums, input/output provenance and limitations. Disposition: PASS_WITH_NOTES.

The earlier 2026-11-15 tolerance scan remains preserved as a historical record. Its driver now reads the exact pre-repair source from immutable commit `5522ae1081f61a711fc846168370542efdef9a35`; it no longer attempts to mutate the current production source.

## 2. Numerical acceptance evidence

- Legacy warning inventory: four QUADPACK roundoff warnings, all from the 20 TeV--muon heavy-light endpoint layer.
- Independent integral check: mpmath tanh-sinh at 50/70/90 decimal digits and composite GL64/GL96; maximum GL96-to-mpmath-90 difference \(3.54\times10^{-15}\).
- Full scan: Benchmarks A/B, \(m_s=100,125.25,150\) GeV; GL orders 32/48/64/96/128.
- Maximum change vs GL128: hard remainder \(1.37\times10^{-12}\ \mathrm{GeV}^2\); pole mass 0 at printed precision; width \(7.30\times10^{-16}\ \mathrm{GeV}\); complex \(R_{hh}\) \(7.45\times10^{-10}\).
- Maximum determinant residual \(6.08\times10^{-9}\ \mathrm{GeV}^4\); maximum \(|\sum R_{hh}-1|=7.56\times10^{-9}\).
- Regression tests: 5/5 passed locally under Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 / mpmath 1.3.0.

Detailed derivation and machine-readable results: [independent endpoint-quadrature audit](POLE_QUADRATURE_INDEPENDENT_AUDIT_2026-11-16.md).

## 3. Register update

The three entries above change from REVISION_REQUIRED to PASS_WITH_NOTES. The repository document register therefore moves from 25 to **22 remaining REVISION_REQUIRED** entries:
- 462 total indexed documents;
- 286 PASS_WITH_NOTES;
- 2 PASS;
- 152 HISTORICAL;
- 22 REVISION_REQUIRED;
- 0 PENDING.

The register blob SHA values for modified documents are updated with their new Git blobs. No other status is changed.

## 4. Scientific boundary

This review closes the **numerical quadrature warning**, not the physical Higgs--singlet pole calculation. The current driver remains a fermion-sector subset with fixed diagonal-width inputs. Full diagonal self-energies/counterterms, complete UV--EFT matching, gauge/Goldstone/ghost completion, physical widths, near-degenerate gauge-independent observables and a detector-level coherent likelihood remain open. The cascade note is not a CMS exclusion.

No referee-facing reply TeX/PDF, manuscript source, stellar-cooling calculation or axial-vector constraint was modified in this review.
