# Individual review: B5-2B3/B5-2B4 output records

Baseline `dbc32d9f6bf223cca176d26cf7f394144bc257e4`; 2026-11-15. Three summaries were read individually and their symbolic scripts were rerun under Python 3.12.14 and SymPy 1.14.0. These tests assess the declared four-cross-box and current-map subblocks, not a full UV/EFT matching, all external momenta, LSZ/counterterm sector or Ward identity.

| Document under `research/major1-higgs-scalar-mixing-20261109/` | Individual review and disposition |
|---|---|
| `B5_2B3_QLD_WW_CROSSBOX_NUMERATOR_OUTPUT_2026-11-11.txt` | Superseded common-numerator diagnostic; associated script exits 0 and explicitly rejects using its earlier `+3/4` finite candidate. Preserve for provenance only. HISTORICAL. |
| `B5_2B3_QLD_WW_EXACT_ROUTING_OUTPUT_2026-11-11.txt` | Exact-routing script exits 0 and reproduces the four numerator reductions and coefficient `(3 Delta_UV/8 - 3 L/8 + 11/16)/M_E^2` for its specified routing. This does not close the full Ward sum. No new CI run claimed. PASS_WITH_NOTES. |
| `B5_2B4_TRIPLET_DERIVATIVE_EOM_CURRENT_MAP_OUTPUT_2026-11-11.txt` | Triplet script exits 0 and reproduces the stated EOM/current coefficients and nonzero contact for the four-box subset. One existing test initially failed because its expected SymPy symbols used `O1/O3/E1/E3` instead of the function's `O_HL1/O_HL3/E_L1/E_L3`; corrected test identifiers without changing coefficients or calculation. PASS_WITH_NOTES. |

After aligning the test symbol identifiers, 39 tests across exact-routing, triplet-map, contact, RGE and EOM subblock suites pass. These are internal symbolic/software checks, not independent full-amplitude validation. The historical outputs and physical formulas were preserved.
