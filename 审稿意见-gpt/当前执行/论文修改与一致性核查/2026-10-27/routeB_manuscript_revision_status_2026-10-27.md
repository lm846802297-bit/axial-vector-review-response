# Route B manuscript revision status — 2026-10-27

## Scope

The user supplied `axial_vector_model_building.zip` in the current conversation. The ZIP contains both `main.tex` and `main-v6.tex`; the latter matches the paper *An Axial U_A(1)_{L_mu-L_tau}: UV Completion and Experimental Searches*. The original `main-v6.tex` and the uploaded ZIP were not modified. The revision is a separate copy.

## Reproducibility identifiers

- Input ZIP SHA-256: `8231ed0a219e852ac69c3653d30a6fd6c27c7fe0a8b92058d65387035f25d047`
- Original `main-v6.tex` SHA-256: `de9132ba936c6b1f3701d7c5a6398e39b89357903be789953972527753540e9a`
- Revised `main.tex` SHA-256: `e1bb3daed0a0e3debc33860260c257139d32ad772b3aba5f9b6f519b6e36eedf`
- Compiled PDF SHA-256: `12d8ce081e25fed59d51340262ece06fec75784107aeacb6c664c02cf058f591`
- Compiled PDF: 35 pages; 2,670,403 bytes.

## Build and validation

Command used in the local build environment:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -e '$bibtex = "bibtex.original %O %B";' main.tex
```

- Clean build exit code: 0.
- No LaTeX errors, undefined control sequences, undefined references, undefined citations, or duplicate labels.
- Eq. (11): Weinberg operator; Eq. (12): block-form neutrino mass matrix; subsection: Sec. II.A.1.
- The original baseline compiled separately with the same BibTeX override: 33 pages, exit code 0.
- The revision has the same warning signatures as the baseline; no new warning signature was introduced.

## Scientific status

- The Route B text changes are applied in the separate manuscript copy: Abstract, Introduction, model subsection, and Conclusion.
- The allowed dimension-five Weinberg entries are `ee` and `mu-tau`; dimension-six `S` insertions can generate `mu-mu` and `tau-tau`; `e-mu` and `e-tau` entries remain forbidden by the charge/residual-Z2 selection rule.
- The induced mass matrix has an isolated electron-flavor state and a mu-tau block. This cannot reproduce the observed PMNS matrix.
- No new right-handed neutrinos or scalars were introduced. The manuscript explicitly states that the minimal field content does not solve the neutrino-mass/PMNS problem.
- Existing A-prime contours remain conditional pure-axial effective-current benchmark constraints, not a global UV-model viability classification.
- Only the Route B / PMNS part of Diff v2.4 and the directly linked removal of the undefined opening word “Light” were applied. Scalar/Higgs-portal quantification, kinetic mixing, finite-VLL recasts, stellar-cooling recasts, UV-EFT truncation, and Fig. 2 robustness remain open.

## Deliverable location

The complete editable revision project, compiled PDF, unified patch, original source tree, and response-letter cross-reference note are provided in the ChatGPT conversation deliverable package. This repository record documents the local build; it does not claim that the full source archive and binary figure assets have been added to this repository.