# Shared homogeneous semi-Compton thermal prototype

This directory contains the byte-identical generic-current thermal-rate and quadrature-convergence implementations formerly copied into both model-variant directories.

The two variants intentionally keep their own stellar_semi_compton_axial_matrix_element.py files because the model-specific amplitude implementation and provenance are kept separate. The small adapter modules in each variant directory add that variant's directory to Python's import path and then load the shared thermal implementation. Consequently, the shared implementation's import of stellar_semi_compton_axial_matrix_element resolves to the local variant-specific module.

Files:
- stellar_semi_compton_thermal_rate_common.py: homogeneous, optically thin thermal rate and smoke checks.
- stellar_semi_compton_thermal_convergence_common.py: quadrature-order and cutoff convergence driver.

This is still a local thermal-rate prototype. It is not radial SN transport, opacity/trapping, or an SN1987A exclusion.
