# Individual review: Belle II bounded recast and response notes

Baseline `b59c109af7bd3b9f0502821027aa1ea1f4ca172c`, 2026-11-15. Three documents were read individually. All rows of the archived four-muon and tau-pair recast CSVs were counted by classification and compared with `bounded_width_recast_summary.json`: 70,656 and 19,968 rows respectively, with every category count matching. This is a stored-output consistency check, not an independently rerun 73,728-point width scan, paper-by-paper detector validation or a new likelihood fit.

| Document under `research/radial-scalar-collider-recast-2026-10-28/` | Individual findings and disposition |
|---|---|
| `BELLEII_MAPPING_INDEPENDENT_AUDIT_2026-11-09.md` | The stated channel-specific branching-ratio mapping and conservative full-interval gates are consistent with the bounded recast's declared model; stored 2746 four-muon and zero tau counts match the archived classification. Primary-paper claims were not freshly verified in this review and the coupling/production and prompt-response assumptions remain conditional. PASS_WITH_NOTES. |
| `BELLEII_RESPONSE_INPUT_AUDIT_2026-11-09.md` | Separates already-folded prompt scalar efficiency from missing width/lifetime response inputs; stored 8673/3286 finite-width-sensitive counts match recast CSV and JSON. The claimed absence of public detector inputs was not independently exhausted, and the 5 mm flight scale is not an efficiency. PASS_WITH_NOTES. |
| `BOUNDED_WIDTH_RECAST_2026-11-09.md` | Every classification count in its two tables matches the saved CSV/JSON. Width endpoints use the documented minimum/maximum convention. Added a note separating the historical 60-test execution from the current scan artifact's later provenance (69-test run); matching output counts alone do not establish byte-identical input scans. No physics numbers were changed. PASS_WITH_NOTES. |

The original-to-current width-scan bound-column differences are already documented in `MANIFEST_REVIEW_2026-11-14.md`. The classification remains conditional and cannot be promoted to an experimental CLs result, a continuous mass exclusion, or a global allowed parameter region.
