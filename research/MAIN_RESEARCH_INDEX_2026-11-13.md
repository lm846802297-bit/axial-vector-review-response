# Main research index — 2026-11-13

**Snapshot:** `main` at `ca998e3c2845579e5183158d6328a557b3fd2ed4`  
**Purpose:** identify the canonical location, integration history, and scientific acceptance boundary for each active referee-response and stellar-cooling workstream.

This index is a navigation and status document. The source files, calculation outputs, validation records, and provenance manifests in the listed directories remain authoritative.

## 1. Workstream index

| Workstream | Canonical main location | Integration history | Current interpretation |
|---|---|---|---|
| Major 1 — scalar pole / Belle II | `research/radial-scalar-collider-recast-2026-10-28/` | PR #68 merged | Bounded-width recast and independent pointwise/four-body audit are archived. Use the stated width, promptness, and benchmark assumptions; do not promote this to a general scalar-sector exclusion. |
| Major 1 — Higgs–singlet mixing and UV–EFT | `research/major1-higgs-scalar-mixing-20261109/` | PR #69 merged | Extensive scalar-potential, self-energy, counterterm, threshold, RGE, and fermion-sector sub-audits are present. This is a staged research record, not a completed gauge-independent two-pole prediction or a final Higgs-constraint scan. |
| Major 3 — neutrino response | `Replies_to_Referee_3_referee_facing_2026-11-04.tex`, `审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/`, and `计算脚本/PMNS_Major3/` | PR #72 merged | The minimal-model PMNS assumption and neutrino-sector limitations are recorded in the response. Do not imply that a general PMNS fit was performed in the minimal model. |
| Major 3 — Overleaf handoff | `deliverables/Overleaf_Reply_Letter_PR72_2026-11-13/` | PR #88 rebuilt from current main; PR #89 corrected checksum; PR #94 extracted the handoff | Upload the extracted TeX/BibTeX/BST/PDF files to Overleaf. There is no need to upload or retain a ZIP in GitHub. |
| Major 4.4 — axial stellar cooling / Blinov benchmark | `research/stellar-cooling-constraints-20261105/` | PR #56 merged; PR #77 merged; PR #83 closed as duplicate; PR #87 and #90 integrated selected B.13/B.16 and checksum follow-ups | The calculation chain and extensive local diagnostics are archived. **The pure-vector Blinov Fig. 7 physical gate remains NOT PASSED at the 10 MeV strong-absorption end.** |
| C4-C4-A/Aq energy dependence | `research/stellar-cooling-constraints-20261105/blinov_reproduction/` | PR #79 merged | Local energy-dependent scattering diagnostics are available. They are not a full luminosity or transport acceptance. |
| C4-C4-B full radial energy dependence | `research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/c4c4_energy_dependence_radial_2026-11-13/` | PR #84 merged | The 7,224-row local-rate/radial-opacity data, channel ratios, quadrature checks, and radial-grid checks are archived. They remain fixed-background local-scattering diagnostics, not a final SN exclusion. |
| Original one-VEV UV model | `research/stellar-cooling-original-uv-model-20261105/` | PR #53 merged | This is the original model line. Keep it distinct from the two-VEV extension. |
| Two-VEV axial microphysics extension | `research/stellar-cooling-two-vev-20261105/` plus `research/stellar-cooling-shared-20261105/` | PR #85 merged | The two-VEV map and local vacuum/thermal prototypes are archived. This is a separate model extension, not a replacement for the original one-VEV manuscript model. See `PHYSICS_CROSSCHECK_2026-11-13.md`. |
| EFT literature kernels | `research/stellar-cooling-eft-literature-20261105/` | Integrated in the stellar-cooling research line | Independent literature-kernel checks and conventions are kept separate from the model-specific UV completion. |
| Collaborator-facing stellar-cooling guide | `research/stellar-cooling-collaborator-archive-20261113/` | Main-branch archive organization commit | Read `README.md`, `STATUS_MATRIX.md`, `FIGURE_AUDIT.md`, and `REVIEW_CHECKLIST.md` before interpreting the plotted contour. The builder is a local handoff tool; it does not upload an archive to GitHub. |
| Higgs–portal document handoff | `deliverables/higgs_portal_mixing_md_with_svg/` | Extracted in PR #94 | Markdown and SVG are stored as ordinary files with checksums and extraction provenance. |

## 2. How to review the stellar-cooling figure

Start with these files, in order:

1. `research/stellar-cooling-collaborator-archive-20261113/README.md` — overview and navigation.
2. `research/stellar-cooling-collaborator-archive-20261113/STATUS_MATRIX.md` — completed work versus open acceptance gates.
3. `research/stellar-cooling-collaborator-archive-20261113/FIGURE_AUDIT.md` — how the figure is generated, what the contour means, and why it is not yet a final exclusion.
4. `research/stellar-cooling-collaborator-archive-20261113/REVIEW_CHECKLIST.md` — reproducibility sequence.
5. `research/stellar-cooling-constraints-20261105/REVIEW_PACKAGE_INDEX_2026-11-13.md` — canonical source layout and local handoff instructions.
6. `research/stellar-cooling-constraints-20261105/AXIAL_STELLAR_CONSTRAINTS_CALCULATION_AND_REVIEW_2026-11-13.md` — full calculation chain and scientific limitations.
7. `research/stellar-cooling-two-vev-20261105/PHYSICS_CROSSCHECK_2026-11-13.md` — formula-level review of the separate two-VEV local microphysics prototype.

The saved axial scan contains 75 baseline mass rows plus five endpoint rows, with 301 logarithmic coupling points per baseline mass. The plotting pipeline derives per-mass threshold intervals from the saved numerical outputs. The plotted region is a **conditional fixed-profile ballistic benchmark**, not a final SN1987A exclusion.

## 3. Scientific acceptance labels

- **Integrated:** source files and results are in current main, with a known PR/commit history.
- **Code/numerically checked:** the named tests, identities, or convergence criteria passed for their documented inputs.
- **Partially validated:** one calculation layer passed, but an independent physical or end-to-end acceptance gate remains open.
- **Physical gate open:** the calculation cannot yet be used as a final phenomenological exclusion.
- **Not included:** the effect is outside the stated benchmark.

A successful CI run is evidence of software execution, not by itself evidence that a literature figure or a physical transport prescription has been reproduced.

## 4. Current scientific decision

The pure-vector Blinov Fig. 7 comparison remains **NOT PASSED** at the 10 MeV strong-absorption end. The axial production scan still uses an initial-muon-rest semi-Compton approximation rather than the complete moving-muon B.13 thermal kernel. The polarization-resolved versus density-matrix transport prescription, reconstructed-background uncertainty, and energy-frame/GR propagation assumptions remain open.

Therefore:

- do not update the final axial constraint curve from the present benchmark;
- do not call the unshaded area a globally allowed region;
- do not treat C4-C4-B local scattering/opacity convergence as an SN luminosity or escape-probability solution;
- do not promote the two-VEV extension to the original one-VEV model.

## 5. Repository and handoff policy

- GitHub main stores native source files, extracted data, figures, reports, tests, provenance, and SHA-256 manifests.
- Generated collaborator ZIP files are **not committed or published as release assets**; the current workflow does not upload them. Thirteen ZIP artifacts from pre-policy runs remain in GitHub Actions until manually deleted or automatically expired; see the branch audit and the one-time cleanup workflow.
- `research/stellar-cooling-collaborator-archive-20261113/build_archive.py` is retained as a local packaging utility. When a ZIP is requested, generate it from a pinned local checkout and hand the file directly to the collaborator/user.
- Original scientific input archives (for example, official EOS source payloads) are distinct from generated delivery ZIPs. Their source provenance and checksums remain documented; do not confuse them with generated handoff bundles.
- Never overwrite a current-main numerical result with an older branch copy merely because the latter has a different Git blob or final floating-point digits. Compare source provenance, inputs, and semantic content first.

## 6. Snapshot provenance

This index is pinned to main commit `ca998e3c2845579e5183158d6328a557b3fd2ed4`. Later changes should append a dated update rather than silently rewriting the historical meaning of this snapshot.
