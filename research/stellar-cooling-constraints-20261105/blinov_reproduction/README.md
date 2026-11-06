# Independent Blinov vector reproduction

This directory is a deliberately separate implementation of the scalar ballistic-cooling prescription in Blinov et al., arXiv:2511.09619v2, Appendix B, Eqs. (17)--(35).

## Independence boundary

- reference.py does not import the production rates.py or transport.py.
- Neutrino/dimuon thermal rates are evaluated with an independent Fermi-integral antiderivative.
- Semi-Compton production follows the paper's nonrelativistic-muon/no-recoil cross-section prescription, including the explicit velocity and photon-polarization factors in Eqs. (30)--(32).
- The muon degeneracy factor follows Eq. (33) literally, with the single negative-muon distribution printed in the paper. It does not add a positive-muon term.
- Scalar opacity follows Eqs. (18)--(21), with full chord integration and angular averaging.
- Luminosity follows Eq. (17), including the lapse-squared factor and local escape-energy threshold.

This is a literal scalar-prescription reproduction path, not a claim that scalar opacity is physically equivalent to mode-resolved propagation when mode opacities differ. It does not infer the private implementation choices of the paper's authors.

## Run

From the repository root:

    python research/stellar-cooling-constraints-20261105/blinov_reproduction/reference.py \
      --profile research/stellar-cooling-constraints-20261105/data/sfho188_digitized.csv \
      --masses 1,10,100,200 \
      --nr 40 --ne 100 --na 16 --ns 32 \
      --output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/blinov_literal_scan.json

All numerical inputs, quadrature orders, profile filename, and outputs are saved in the JSON. The profile is the existing reconstructed SFHo-18.8, 1 s profile, not an original simulation table.

## Comparison ladder

1. Compare independently implemented local neutrino and dimuon production rates with the archived analytic checks in vector_reference.py; do not import that file into the implementation.
2. Compare the no-recoil semi-Compton rate with the B.32 cross-section formula and its Thomson limit.
3. Compare scalar optical depth and angular escape with B.2/B.4, first in constant-opacity test cases.
4. Compare resulting Fig. 7 luminosity curves and Fig. 4 cooling intervals against digitized Blinov reference points.
5. Only after this reference path is understood, compare it against the existing mode-resolved production solver under deliberately matched inputs.

The reference path is not used to update the axial plot, referee response, or manuscript.
