# Independent collaborator review checklist

## A. Provenance and integrity

- [ ] Verify every entry in SHA256SUMS.txt.
- [ ] Record the source commit from ARCHIVE_PROVENANCE.json.
- [ ] Check SOURCE_FILE_CATALOG.csv for original repository path and file description.
- [ ] Confirm no file under review_package_extracted/ was used as a second source.
- [ ] Confirm the SFHo-FRDM large ZIP payloads are retrieved from the documented release and pass the supplied manifest.

## B. Reproduce the existing axial benchmark

- [ ] Install 00_START_HERE/requirements-review.txt.
- [ ] Run the unit tests under 01_axial_benchmark_and_transport/.
- [ ] Run validate_outputs.py.
- [ ] Re-run run_scan.py for the axial baseline, vector control, and endpoint masses using settings in the calculation report.
- [ ] Compare regenerated JSON with archived JSON; do not overwrite reference outputs during review.
- [ ] Run plot_constraints.py and compare the original PDF/PNG.
- [ ] Run plot_constraints_loglog.py; inspect its review figure and contour_interpolation_audit.json.

## C. Independently inspect the vector reference lane

- [ ] Read blinov_reproduction/README.md.
- [ ] Read B16_FIG7_FINAL_REPRODUCTION_ACCEPTANCE_2026-11-10.md.
- [ ] Verify the Fig. 4 ballistic boundary comparison separately from the Fig. 7 luminosity comparison.
- [ ] Inspect the 10 MeV weak-source and strong-absorption discrepancy records.
- [ ] Check fixed-local-energy and conserved-energy diagnostics as separate conventions.
- [ ] Confirm no empirical opacity multiplier or profile rescaling was used to force agreement.
- [ ] Confirm the vector dashed line in the axial figure is not mislabeled as the published Fig. 7 result.

## D. Inspect the EOS and background

- [ ] Read the SFHo-FRDM data README and checksum manifest.
- [ ] Verify downloaded table archives before extraction.
- [ ] Read the P1-IIIe-B real-table closure report and its acceptance boundary.
- [ ] Compare reconstructed Caputo / Bollig / Esseili–Kribs profiles and species definitions, not just curve shapes.
- [ ] Keep EOS-table validation distinct from validation of the time-dependent Garching supernova profile.

## E. Physics acceptance before a final limit

- [ ] Resolve mode-resolved versus scalar opacity from a physical transport derivation.
- [ ] Integrate the full moving-muon semi-Compton kernel into the axial scan.
- [ ] Revisit background and neutrino chemical-potential assumptions.
- [ ] Resolve fixed-local-energy versus conserved-energy / GR propagation.
- [ ] Recompute and converge the axial scan after those changes.
- [ ] State the UV-to-EFT coupling map and model validity domain.
- [ ] Regenerate the final plot only from the accepted scan.

## F. Reporting

- [ ] Report completed calculations separately from passed physical validation.
- [ ] State that the current contour is a conditional fixed-profile ballistic benchmark.
- [ ] Do not call unshaded points globally allowed.
- [ ] Do not call the current figure the final SN1987A exclusion.
- [ ] Attach exact source commit and archive SHA-256 manifest to any shared derivative.
