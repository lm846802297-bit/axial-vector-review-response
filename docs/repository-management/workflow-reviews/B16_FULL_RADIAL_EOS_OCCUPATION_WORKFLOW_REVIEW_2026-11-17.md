# Eighty-first review: full-radial SFHo EOS occupation workflows

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `6a094c2ffafdf34733357862007ee6ebd2fdf71e`  
Scope: five P1-IIIe workflows covering the official SFHo EOS table closure, full-radial occupation reconstruction, and C3-A/C3-B/C3-C degeneracy diagnostics.

This is a static review of workflow wiring, input references, and acceptance checks. No workflow, test, or numerical calculation was run. These checks do not establish a full supernova transport result or scientific acceptance.

## Inventory

| Workflow | Current Git blob | Function | Status |
|---|---|---|---|
| `.github/workflows/b16-p1iii-eos-degeneracy.yml` | `499b648ed85d48a784f7812f62ca1a300d2dd2ce` | SFHo table integrity, key-radius composition/occupation closure and deterministic self-test | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iii-eos-full-radial-occupation.yml` | `354b1171014e2752a7d3986256155c9d216c98d0` | Independent C2 occupation reconstruction on 301 radii | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iii-eos-full-radial-degeneracy-identity.yml` | `75a27e0aaf88080630d00489b24e55ec79e2696b` | C3-A direct/derivative identity on the full profile | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iii-eos-full-radial-degeneracy-step-scan.yml` | `a4cfd0d3ee9bed4a1ee2b7ca0435661fd67691c1` | C3-B finite-step truncation scan across 5,418 combinations | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iii-eos-full-radial-degeneracy-radial-diagnostics.yml` | `28d0e68227458f9ed5954464ddd3776ba6e18523` | C3-C relativistic/nonrelativistic diagnostics on 602 species-radius rows | `REVIEWED_WITH_NOTES` |

## Findings

All five workflows trigger on pushes to `research/moving-muon-thermal-rates-20261107` and manual dispatch, guard the job to that branch, pin checkout to `github.sha`, and use `ubuntu-latest` with Python 3.12. They use `contents: read`, keep runs active rather than cancelling them, and install unpinned NumPy/SciPy. They write generated results only under runner temporary directories and compare them with committed reference files; they do not commit results or upload artifacts.

The first workflow downloads the official SFHo FRDM v1.03 release archives, checks their SHA-256 values against the committed manifest, extracts the required tables, and checks the ten key-radius mapping against explicit composition, filling-factor, occupation-density and quadrature tolerances. It also runs focused unit tests and a deterministic software self-test that labels itself as a software fixture rather than Garching profile data. The extensive path filter includes the table reader, mapper/builders, test files, key input data, reference outputs and manifest. The download is thus integrity-checked, though the release assets themselves remain external to the Git tree.

The C2 workflow runs focused tests and independently reconstructs the occupation result on all 301 radii, comparing JSON diagnostics and selected CSV columns to the committed baseline. C3-A checks direct and density-derivative degeneracy identities at all 301 radii and compares against the C2 reference. C3-B checks the nine finite-difference step sizes across 5,418 species/radius/step combinations and verifies selected error-scaling and identity thresholds. C3-C checks both relativistic and two nonrelativistic comparisons for 602 species-radius rows, with summary and row-level tolerances. Each workflow includes its driver, test, profile/reference inputs and expected outputs in the push filter.

The checks provide explicit software-level reconstruction and closure gates for the stated EOS/profile diagnostics. They do not calculate the B.1/B.2 luminosity, solve full transport, or independently establish the physical validity of the digitized Caputo profile. A passing job would validate only the encoded transformations and tolerances.

## Maintenance notes

- The input and expected-output path filters are detailed and mostly dependency-aware; keep them synchronized if any shared EOS reader or normalization helper is added to these calculations.
- NumPy/SciPy and the action references are not pinned to immutable versions, so the environment is not fully frozen.
- Preserve the external-release SHA checks and the explicit “software self-test” provenance labels.
- Do not use these EOS occupation checks as evidence that the unresolved Caputo/Bollig absolute-density convention or the supernova transport baseline has been settled.
