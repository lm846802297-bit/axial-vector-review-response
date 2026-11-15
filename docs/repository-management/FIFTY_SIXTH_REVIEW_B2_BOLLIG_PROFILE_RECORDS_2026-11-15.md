# Fifty-sixth review: B.2 polarization/energy audits and Bollig profile cross-checks

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: 832d515b7b3bac3df38b1f846bc19435fe66c93a  
Scope: six B.2/Bollig background records, linked V8/JSON outputs, final GitHub Actions status, and current profile-B provenance.

## 1. Executive result

Six documents were reviewed individually; all six are PASS_WITH_NOTES.

The main result is that the high-energy B.2 and B.13 calculations remain restricted-band diagnostics. The 210--510 MeV B.13 kernel and global transport calculation pass their stated local and band checks, but the low-x extension is incomplete, so no full-band Fig. 7 reproduction is claimed. The B.2 scalar polarization convention remains under-specified at the attenuation exponent; the B.6/B.7/B.10 local-rate chain is sum-to-sum, but it does not uniquely select a scalar sum, average, or occupation closure for B.2.

The source-radial scans for 0.1 and 1 MeV now both pass the isolated 1% criterion. The full multidimensional global path-energy scan still fails the combined 1% criterion at those two masses; 10 MeV passes its tested global grid. The high-order three-mass B.16 workflow completed successfully.

The Bollig profile checks support the reconstructed \(T(r)\) and \(\mu_\mu/T\) curves, while the absolute Fig. 3 muon-density discrepancy remains unresolved. The independent lapse comparison is qualitative only. No profile, source, opacity, coupling, Fig. 7 curve, or axial-vector constraint was changed.

## 2. Individual document outcomes

| Document | Outcome | Main finding |
|---|---|---|
| B2_10MEV_ENERGY_GR_SHELL_POLARIZATION_AUDIT_2026-11-13.md | PASS_WITH_NOTES | B.1 energy-variable Jacobian and local rate closures pass. Exact B.13 transport is restricted to 210--510 MeV; the low-x pilot has seven points, not the required 24-point radial-profile validation. Updated the scalar B.2 interpretation to preserve the sum/average/closure ambiguity. |
| B2_CHANNEL_RESOLVED_OPACITY_AUDIT_2026-11-10.md | PASS_WITH_NOTES | The B.16 scalar-sum implementation has a consistent neutrino/Compton decomposition and source-weighted Shapley result. Fixed malformed display math and clarified that the scalar-sum lane is an implementation choice, not a uniquely mandated B.2 polarization closure. Exact direct-V8 producer source is not archived. |
| B2_PATH_ENERGY_AND_RADIAL_CONVERGENCE_STATUS_2026-11-09.md | PASS_WITH_NOTES | Both 0.1 and 1 MeV isolated source-radial scans are archived and pass below 1%; the full combined grid still fails for those masses. The 10 MeV grid passes, and all three high-order B.16 mass jobs completed successfully. Superseded the stale “currently running” workflow text with final status. |
| BOLLIG_15_20KM_THERMODYNAMIC_CROSSCHECK_2026-11-09.md | PASS_WITH_NOTES | Over 294 nodes, \(T\) and \(\mu_\mu/T\) match Bollig Figs. 1/4 at the stated \(10^{-4}\) level. Fig. 3 absolute density remains about 10.38% lower where visible and is censored at its lower plotting floor beyond 16.6466 km. |
| BOLLIG_LAPSE_PROFILE_VISUAL_CROSSCHECK_2026-11-09.md | PASS_WITH_NOTES | The presentation slide supports the lapse trend and normalization over 0--20 km at a few-\(10^{-3}\) visual read-off level. It is not a machine-readable lapse table; 20--22 km and full-GR propagation remain unvalidated. |
| BOLLIG_MUON_DENSITY_AND_B1_SOURCE_AUDIT_2026-11-09.md | PASS_WITH_NOTES | The relativistic Fermi--Dirac density and \(n_\mu F_{\rm deg}\) susceptibility are internally consistent with \(T,\mu_\mu\). The Bollig Fig. 3 discrepancy remains unresolved; P1-E2/E3 do not justify a source or lapse correction. Fixed duplicate section numbering. |

## 3. B.2 polarization and exact-B.13 scope

The B.2 10 MeV follow-up correctly distinguishes:
- local mode-summed production/absorption closure;
- the literal scalar B.2 equation-level reproduction lane;
- independent per-mode propagation;
- equal-occupation average-opacity closure.

B.7's factor of three converts the vacuum-width polarization average into the thermal production sum. B.10 adds no further degeneracy factor. The printed B.2 exponent still contains one scalar \(\Gamma_{\rm abs}^{*}\) without specifying whether it is a sum over incident modes, a three-state average, or shorthand for a polarization closure. The document now consistently reflects that qualification in the B.13 comparison.

The exact moving-muon B.13 local audit covers 42 radius-energy points and passes the 0.1% successive-order criterion, with maximum detailed-balance residual \(1.10\times10^{-14}\). The 210--510 MeV global band reproduces the B.16 scalar baseline at relative residual \(-1.01\times10^{-7}\). The B.13 both-charge mode-resolved result is \(6.058125\times10^{53}\) erg/s, but this is a separate transport prescription and not a correction factor to the scalar baseline.

The full-band minimum path-local coordinate is \(x_{\min}=0.0221811\), below the current Global-03 table's \(x=0.5\) lower support. The seven-point local pilot passes its own convergence checks, but the 24-point radial-profile extension is incomplete. No full-band Fig. 7 or axial-vector result is accepted.

## 4. Channel-resolved opacity and path-energy convergence

The B.16 channel audit reports global source-weighted mean optical depths \(14.4807\) (neutrino inverse decay) and \(1.6480\) (semi-Compton), and 210--510 MeV values \(5.9118\) and \(1.8076\). The 36-ray channel means are unweighted diagnostics; the separate global Shapley result is source weighted. The exact V8 producer source for this particular channel JSON is not archived, so the JSON remains inspectable numerical evidence rather than a source-level rerun.

The final source-radial JSONs are:
- 0.1 MeV: Git blob SHA 6f48b953cd3c762a223f13a930e95aeb05b7b3cd; adjacent-order maxima 0.7466%, 0.1978%, 0.1556%, 0.1437%.
- 1 MeV: Git blob SHA 2c8e4e98a2a544cf290d07672c1b87a862ed2ce1; adjacent-order maxima 0.1757%, 0.0150%, 0.0873%, 0.0620%.

Both scans hold the 642-node opacity grid and 742-node energy grid fixed. Run #42586195530 completed the 1 MeV job; its 0.1 MeV job exited at the commit step because the accepted 0.1 MeV JSON already existed from Run #42585236139. This is a no-change-to-commit outcome, not a failed physics calculation.

The full multidimensional path-energy scan still fails the combined 80×200×32×64 1% criterion for 0.1 and 1 MeV because the 60→80 radial refinement is above threshold. The 10 MeV grid passes its tested one-factor and combined-grid criteria. Run #42588622451 completed successfully for all three high-order B.16 mass jobs. The six-mass Fig. 7 reproduction is still incomplete.

## 5. Bollig thermodynamic, density, and lapse checks

The 15--20 km source comparison is based on original PDF vector paths. Across 294 profile nodes, the mean absolute relative differences are 0.00431% for \(T\) and 0.00468% for \(\mu_\mu/T\); maximum differences are 0.01628% and 0.01547%. Where Fig. 3 is above its plotting floor, 90 nodes show the reconstructed relativistic Fermi density exceeding the plotted density by 10.38% on average, with a maximum 12.11%. The figure reaches its \(10^{-7}\,\mathrm{fm}^{-3}\) lower floor at 16.6466 km; beyond that it is censored.

The susceptibility \(n_\mu F_{\rm deg}=T\,\partial n_\mu/\partial\mu_\mu\) is fixed by the same Fermi--Dirac distribution. An independent normalization change to \(n_\mu\) while holding \(F_{\rm deg}\) fixed is not justified. The current-profile outer-shell Compton effect remains small and is not a reason to rescale the source.

The lapse slide provides qualitative corroboration over 0--20 km, with visual differences of a few \(10^{-3}\). It does not validate the 20--22 km continuation or provide a precision lapse table. It is a second visualization of the same Garching model lineage, not independent hydrodynamic data.

## 6. Disposition

All six documents are PASS_WITH_NOTES. The B.2 scalar-opacity ambiguity and the B.13 full-band low-x limitation remain explicit. The 0.1/1 MeV source-radial scans pass only in that isolated numerical dimension; the full global grid remains open. The Fig. 3 density tension and raw-Garching-data gap remain unresolved.

No production profile, source, opacity, coupling, Fig. 7 reference, SN1987A limit, or axial-vector constraint is modified.
