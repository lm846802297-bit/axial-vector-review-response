# Ninth document review — PR template and coherent spectral-area diagnostic (2026-11-14)

Reviewed against branch commit `94e6dbbc58e13ee867bfe7da99d4dfad8b276524`. This is an editorial, provenance and scope review, not a recalculation or verification of the physical propagator.

| File | Role and disposition | Findings |
|---|---|---|
| `.github/PULL_REQUEST_TEMPLATE.md` | Current contributor template; PASS_WITH_NOTES | Explicitly separates evidence, limitations, actual validation and merge strategy. The CI/workflow checkbox should be interpreted only when such a run is performed; the repository's AGENTS.md makes CI optional. Research-specific checklist items are not automatically applicable to documentation-only PRs. No change to policy is implied. |
| `research/major1-higgs-scalar-mixing-20261109/COHERENT_TWO_POLE_SPECTRAL_AREA_2026-11-10.md` | Historical approximate-propagator diagnostic; REVISION_REQUIRED | Six displayed ratios round consistently to the companion output and the stated relative shifts follow arithmetically. The experimental limitations are explicit. However, parameters `a` and `b` and the sign/width conventions are not defined in the note, and it lacks direct links to the companion script and output or an exact command/input provenance. Resolve these against the actual implementation before treating the note as a stand-alone reproducible record. No independent integral, convergence, or physics validation was performed here. |
| `research/major1-higgs-scalar-mixing-20261109/coherent_two_pole_spectral_area.txt` | Recorded output; HISTORICAL | Values, integration window, benchmark labels and approximation boundaries are documented. Its PASS line is a recorded result from the originating run, not a new independent run in this review. The file itself does not identify the source commit, environment or exact invocation; retain it with the script and calculation note. |

The companion implementation exists at `research/major1-higgs-scalar-mixing-20261109/coherent_two_pole_spectral_area.py`; its content has not been audited in this batch. The near-degenerate observable remains a diagnostic, not a measured signal strength or an exclusion.

## Navigation correction

GitHub PRs #53 and #69 were both verified merged on 2026-11-12. Two references to #53 as an active Draft in the Chinese quick-start were corrected; historical workstream text otherwise remains intact. No scientific result was changed.
