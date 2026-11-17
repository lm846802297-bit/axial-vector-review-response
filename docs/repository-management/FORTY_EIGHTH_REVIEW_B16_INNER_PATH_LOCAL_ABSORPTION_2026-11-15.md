# Forty-eighth review: B.16 inner-path, local absorption, radial synthesis and paper cross-check

**Date:** 2026-11-15  
**Repository:** `lm846802297-bit/axial-vector-review-response`  
**Branch:** `maintenance/repository-organization-audit-20261114`  
**Reviewed source snapshot:** `bc4e1d5365738bc44d203f3d60eb920b418e2ce1`

This batch individually reviewed six baseline documents, their referenced Python implementations, tests, current-profile JSON outputs, the vertex-preserving workflows, and the cited publisher-version equations. It is a content review, not a new transport calculation. No production rate, path-opacity output, luminosity curve, coupling, or axial-vector constraint was recalculated or rescaled.

## 1. Individual document outcomes

| Document | Outcome | Disposition |
|---|---|---|
| `B16_INNER_PATH_CHANNEL_DIRECTIONAL_AUDIT_2026-11-09.md` | **HISTORICAL** | Earlier 501-node uniform-profile result; retain for provenance only. |
| `B16_INNER_PATH_CHANNEL_DIRECTIONAL_AUDIT_VERTEX_PRESERVING_2026-11-09.md` | **PASS_WITH_NOTES** | Current 1687-row profile; analytic path geometry and shell/direction decomposition are consistent. |
| `B16_LOCAL_ABSORPTION_AUDIT_2026-11-09.md` | **HISTORICAL** | Earlier profile snapshot; do not mix its numbers with the current-profile result. |
| `B16_LOCAL_ABSORPTION_VERTEX_PRESERVING_2026-11-09.md` | **PASS_WITH_NOTES** | Current local kernels close; corrected the \(\mu^+\) percentage interpretation. |
| `B16_NEUTRINO_INVERSE_DECAY_RADIAL_PATH_SYNTHESIS_2026-11-09.md` | **PASS_WITH_NOTES** | Post-processing arithmetic agrees with the paired current-profile JSON. |
| `B16_ORIGINAL_PAPER_CROSSCHECK_2026-11-08.md` | **PASS_WITH_NOTES** | Equation map and figure-level background comparison supported; raw-profile identity remains unverified. |

## 2. B.16 inner-path geometry and transport

The current path output uses the 1687-row vertex-preserving public-figure reconstruction with SHA-256:

`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

The implementation treats the radial opacity as piecewise linear between retained profile nodes and analytically integrates each radial segment along a straight chord. For impact parameter \(b=r_0\sqrt{1-\mu^2}\), the radial measure is \(ds/dr=r/\sqrt{r^2-b^2}\); inward-going rays traverse the \(b<r<r_0\) interval twice. The unit tests explicitly check the inward branch, shell crossings, the piecewise-linear primitive against an independently segmented path-coordinate integral, equal-width direction bins, and channel closure.

The vertex-preserving workflow run [42532897123](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42532897123) completed successfully with six tests. The current-profile B.1 source fraction from 8--15 km is 0.796114338, and the strong-endpoint source-weighted escape probability for that emission region is \(3.5333093\times10^{-4}\). The channel-sum residuals are \(4.01\times10^{-16}\) for production and \(5.94\times10^{-16}\) for reduced absorption; angular-weight normalization closes exactly.

The analytic radial integral versus the fixed-order 256-point whole-ray quadrature has maximum relative residual \(1.19179\times10^{-4}\), and the source-weighted L1 residual over 8--15 km is \(2.09403\times10^{-6}\). The maximum is a cross-check against that fixed-order whole-ray quadrature, not a certified error bound for the analytic primitive. The segmented path-coordinate unit test is a separate, stronger local geometry check. The 16/32/64 angular scan changes the strong-endpoint escape probability by \(5.73\times10^{-6}\) at order 16 and \(1.30\times10^{-6}\) at order 32 relative to order 64.

For the dominant 8--15 km emission region, the source-weighted \(\nu_\mu+\nu_\tau\) path-optical-depth fractions are 5.38566% (0--8 km), 75.53971% (8--22 km), and 19.07463% (22--25 km). For all emission radii the corresponding fractions are 6.71002%, 73.97364%, and 19.31634%. These are path-optical-depth attributions, not additive fractions of the final luminosity. Leave-one-shell-out luminosity factors are nonlinear counterfactuals and must not be added.

One wording correction was required: the outer-shell Compton path column is not exactly zero. For the dominant 8--15 km source it is 0.7935 per \(g_X^2\), compared with \(1.5633\times10^{15}\) per \(g_X^2\) from \(\nu_\mu+\nu_\tau\) inverse decay in that shell, a relative fraction \(5.08\times10^{-16}\). It is numerically negligible in this decomposition, but nonzero.

The calculation follows the literal fixed-\(\omega\) B.2 path prescription. It is not a full GR geodesic calculation and does not settle the paper's fixed-\(\omega\) versus conserved-\(E_\infty\) convention ambiguity. The background is a public-figure reconstruction, not the original Garching raw snapshot.

## 3. B.6--B.10 and B.14--B.19 local absorption

The current local audit samples 16 radii and six energies, for 96 radius-energy points. The vertex-preserving workflow run [42558231626](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42558231626) passed seven local-absorption tests and 12 reference regression tests (19 total). The maximum local production, absorption, and reduced-absorption closure residual is \(3.048\times10^{-14}\).

The independent neutrino calculation checks direct B.6 angular phase-space integration, inverse-occupation absorption, B.10 detailed balance, and B.4 reduced absorption separately for \(\nu_\mu\) and \(\nu_\tau\). The Compton implementation checks B.14--B.17, B.19 detailed balance, and B.4 reduction. The exact moving-muon B.13 calculation is a separate diagnostic; the B.14--B.16 no-recoil approximation is not validated physically by local algebraic closure. The current B.13 records show materially different inner-region rates, so no global B.13 substitution or empirical correction is justified by this batch.

### \(\mu^+\) susceptibility correction

The current local JSON reports \(f_+=\chi_+/(\chi_-+\chi_+)\). The previous document wording “below 0.05% through 22 km” was incorrect by a factor of 100 in the percent/fraction conversion. The correct pointwise values are:

| Radius | \(f_+\) | \(\chi_+/\chi_-\) |
|---:|---:|---:|
| 8 km | 1.170% | 1.183% |
| 10 km | 0.336% | 0.337% |
| 12 km | 0.0981% | 0.0982% |
| 15 km | 0.00835% | 0.00835% |
| 18.25 km | 0.0448% | 0.0448% |
| 20 km | 0.0887% | 0.0888% |
| 21.5 km | 0.394% | 0.396% |
| 22 km | 4.275% | 4.466% |
| 23--25 km | 50% | 100% |

Thus the fraction is below 5%, not 0.05%, through 22 km. At \(\omega=15\) MeV, adding the positive-muon susceptibility explicitly would change the total local reduced opacity by about 0.477% at 8 km, 0.118% at 10 km, 0.0152% at 12 km, and \(1.87\times10^{-5}\)% at 15 km. At 22--25 km the relative Compton contribution is extremely small despite the 50% charge fraction: the local Compton share at 22 km is \(1.55\times10^{-15}\) as a fraction, and decreases farther out. These are pointwise estimates, not a global B.2 correction.

The printed B.17 one-species convention remains the reproduction baseline; its factor two counts muon spin states. No blanket factor of two for \(\mu^+\) is added. A future calculation that chooses to include both charges must sum their susceptibilities explicitly.

## 4. Radial-path synthesis

The synthesis tables were recomputed from the paired current-profile JSON. The source fraction, escape probability, shell fractions, direction-bin fractions, and leave-one-out factors agree to the displayed precision. The report correctly distinguishes the 19.07% outer-shell share of the neutrino path optical depth from the shell's share of emitted or escaped luminosity.

This is a post-processing summary, not a new transport run. No standalone post-processing script or dedicated test module is supplied; the arithmetic is reproducible directly from the archived JSON. The report is therefore retained as PASS_WITH_NOTES rather than as an independently executable calculation.

## 5. Original-paper and profile cross-check

The primary equation authority is the publisher version of record, Blinov et al., *JHEP* 06 (2026) 155, DOI 10.1007/JHEP06(2026)155, Appendix B, pp. 20--23 of the publisher PDF. It confirms the B.1 lapse-squared source measure and emission threshold, the fixed displayed \(\omega\) argument and full angular chord integral in B.2/B.3, B.4 reduced absorption, B.6/B.10 neutrino production and detailed balance, B.13--B.19 Compton relations, and \(R_{\max}\simeq25\) km. The arXiv preprint remains a cross-check rather than the primary equation citation.

The original Bollig et al. *Phys. Rev. Lett.* 125, 051104 (2020), DOI 10.1103/PhysRevLett.125.051104, Figs. 3 and 4 support the Caputo SFHo-18.8 muon-density and \(\mu_\mu/T\) reconstruction in the high-muon-density 5--15 km region. The Ferreira \(\mu_\mu/T\) reconstruction is inconsistent with those original figure-level diagnostics under the common Fermi-distribution convention. This is a figure-level source comparison only. The exact \(s18.8\)-SFHo-MUONS, \(t_{\rm pb}=1\) s raw snapshot is not deposited with the Blinov article and is not available from the protected archive endpoints in this workflow; exact raw-profile identity remains unverified.

## 6. Workflow and repository-governance checks

The vertex-preserving local-absorption workflow was reviewed and marked REVIEWED_WITH_NOTES. It guards execution to the designated research branch, asserts the expected profile SHA-256, runs the local and reference tests, checks that production axial outputs remain unchanged, and archives the machine-readable output with `contents: write`. Python is set to 3.12, while NumPy/SciPy are not version-pinned. Its step label was narrowed to B.14--B.19; B.13 remains a separate exact moving-muon diagnostic. The older generic-profile local-absorption workflow remains pending and was not changed.

The document-review standard now uses the same canonical status labels as the register (`PENDING`, `HISTORICAL`, etc.). The folder catalog's 205/257 count is explicitly identified as its original historical checkpoint; the live count is linked to README and PROJECT_STATUS.

## 7. Final coverage and remaining boundary

The 462-row baseline document register now contains **288 individually reviewed** and **174 pending** documents:

| Outcome | Count |
|---|---:|
| PASS_WITH_NOTES | 187 |
| PASS | 2 |
| REVISION_REQUIRED | 9 |
| HISTORICAL | 90 |
| PENDING | 174 |

The separate 115-row workflow register now contains 41 REVIEWED_WITH_NOTES, 16 HISTORICAL_CANDIDATE, and 58 PENDING entries.

No production rate, opacity, source, luminosity, or axial-vector constraint was changed. The pure-vector Fig. 7 strong-endpoint discrepancy remains unresolved. The next batch should continue with the next six PENDING baseline records; the B.13/B.16 physical approximation comparison and raw-background identity remain separate scientific gates.


## 8. Current-tree reconciliation (2026-11-16)

The four current-profile source documents and two historical-profile documents in §1 remain present; their current baseline-register outcomes match the report. The paired current-profile JSONs retain profile SHA `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. Directly inspected values reproduce the reported 8--15 km source fraction (0.7961143384), strong-endpoint source-weighted escape probability (3.5333093\times10^{-4}), production/reduced-absorption channel-sum residuals (4.01\times10^{-16})/(5.94\times10^{-16}), and local-absorption maximum closure (3.04845\times10^{-14}). The 1.17% (mu^+) susceptibility fraction at 8 km and 4.275% at 22 km are present in the pointwise JSON; the report correctly avoids treating them as a global opacity correction.

Both cited current-profile workflows (#42532897123 and #42558231626) are completed successfully. The historical 501-node profile remains separate from the 1687-row profile. The 256-point whole-ray comparison is a cross-check, not a certified error bound; fixed-(omega) remains the literal B.2 reproduction lane, not a full-GR propagation claim. No production output or cooling constraint is updated.
