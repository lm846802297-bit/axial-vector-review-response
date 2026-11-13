# Stellar Cooling Research & Reproducibility Archive

**Snapshot date:** 2026-11-13  
**Purpose:** collaborator review of the stellar-cooling programme, with a reproducible path from the axial EFT rates to the provisional SN1987A cooling contour.

## Executive decision

The repository contains a substantial, reproducible **fixed-profile axial-EFT ballistic-cooling benchmark** and an extensive independent pure-vector reproduction programme. It does **not yet contain a final, physically validated SN1987A exclusion for the axial model**.

The plotted axial contour is a conditional benchmark on a reconstructed SFHo-18.8 profile. It is useful for checking the calculation chain, parameter dependence, channel hierarchy, and plotting pipeline. It must not be presented as a final astrophysical exclusion until the pure-vector Fig. 7 gate, the polarization/opacity prescription, the moving-muon thermal kernel, and the background/propagation assumptions are resolved.

Completed numerical tasks, passed code checks, and unresolved physical acceptance gates are recorded separately.

## Where to start

1. Read STATUS_MATRIX.md for completed / partial / open status.
2. Read FIGURE_AUDIT.md before interpreting any exclusion contour.
3. Read REVIEW_CHECKLIST.md and follow the reproducibility sequence.
4. Use SOURCE_FILE_CATALOG.csv to find the description, original repository path, packaged path, size, and SHA-256 of every source file.
5. Verify SHA256SUMS.txt before running anything.

## Archive layout

| Directory | Contents |
|---|---|
| 00_START_HERE/ | This guide, status matrix, figure audit, reviewer checklist, provenance, file catalog, checksums, and archive builder |
| 01_axial_benchmark_and_transport/ | Axial EFT implementation, reconstructed profiles, production/absorption, transport, scans, outputs, tests, and the independent Blinov B.13/B.16 research record |
| 02_model_variants/ | Original single-VEV and two-VEV model folders, one shared thermal-prototype folder, and EFT-literature kernel checks; original relative paths are preserved |
| 06_reproduction_workflows/ | Relevant GitHub Actions workflows |

## Data policy

- The archive includes digitized public-profile inputs, provenance records, numerical outputs, code, tests, EOS documentation, checksum manifests, and the downloader.
- The large SFHo-FRDM ZIP archives are not copied into this ZIP. They remain available in the repository's sfho-frdm-v1.03-data GitHub Release. Their checksums and retrieval instructions are preserved.
- No private Garching simulation profile is included. The current axial plot uses a profile reconstructed from public literature plots; it is not the exact private simulation snapshot.
- Historical extraction copies under review_package_extracted/ are excluded. Canonical files remain in the main research tree. Byte-identical common thermal-rate files across model variants are stored once; the catalog records each alias.

## Reproduce the existing axial benchmark

Use Python 3.11 (recommended) and install the review dependencies:

~~~bash
python -m pip install -r 00_START_HERE/requirements-review.txt
~~~

From the extracted archive root:

~~~bash
python -m unittest discover -s 01_axial_benchmark_and_transport -p "test_*.py" -v
python 01_axial_benchmark_and_transport/validate_outputs.py
python 01_axial_benchmark_and_transport/plot_constraints.py
~~~

The commands above validate the saved baseline and regenerate the existing presentation figures. The separate plot_constraints_loglog.py creates a review-only figure from the saved per-mass log-log threshold intervals and writes a quantitative comparison against the original Matplotlib contour interpolation. See FIGURE_AUDIT.md.

For the pure-vector reproduction, follow the independent instructions in 01_axial_benchmark_and_transport/blinov_reproduction/README.md.

Do not treat the moving-muon B.13 local-rate work, the EOS collision-kernel work, or any independent diagnostic as already incorporated into the axial production scan. STATUS_MATRIX.md identifies these boundaries.

## Reproduce the archive

The repository-side builder is included at 00_START_HERE/tools/build_archive.py. Run it from a clone of the repository checkout, not from the extracted ZIP. It reconstructs the ZIP from tracked source files, excludes the legacy extracted copy and large EOS ZIP payloads, de-duplicates byte-identical files, creates the file catalog and SHA-256 manifest, and checks the result.

The ZIP is a generated review deliverable. GitHub stores the canonical source, research records, tests, and archive builder; it does not store another copy of the ZIP.

## Citation and collaboration policy

Cite the primary literature and exact data sources listed in the relevant source reports. Do not cite the reconstructed profile as an original Garching data release. When reporting the axial contour, use:

> Conditional, mode-resolved axial-EFT ballistic-cooling benchmark on a reconstructed SFHo-18.8 profile; not a final SN1987A exclusion. The pure-vector Fig. 7 end-to-end validation and several physical transport assumptions remain open.
