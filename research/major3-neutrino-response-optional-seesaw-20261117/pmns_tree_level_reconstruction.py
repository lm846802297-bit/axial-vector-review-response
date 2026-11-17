#!/usr/bin/env python3
"""Constructive tree-level type-I seesaw reconstruction for Major Point 3.

This is not a statistical fit or parameter scan. It constructs M_nu from
NuFIT 6.1 (2025) normal-ordering central oscillation values, chooses m1 and
Majorana phases explicitly, and inverts the seesaw relation to obtain M_R.

Dependencies: Python 3 and NumPy.
Source for oscillation central values:
https://www.nu-fit.org/sites/default/files/v61.tbl-parameters.pdf
See also:
../../审稿意见-gpt/当前执行/PMNS_Major3路线决策与扩展模型解析核查_2026-10-27.md
"""

from __future__ import annotations

import json
import math
from typing import Any

import numpy as np


# NuFIT 6.1 (2025), IC24 + Super-K atmospheric data, normal ordering.
SIN2_THETA12 = 0.3088
SIN2_THETA23 = 0.470
SIN2_THETA13 = 0.02248
DELTA_CP_DEG = 212.0
DM21_EV2 = 7.537e-5
DM31_EV2 = 2.511e-3  # NuFIT's Delta m^2_3l for normal ordering.

# Explicit choices not fixed by oscillation data.
M1_EV = 0.010
ALPHA21_DEG = 0.0
ALPHA31_DEG = 0.0

# Illustrative seesaw scale choices.
M_DIRAC_GEV = 1.0e-5  # 10 keV for each diagonal entry.
V_EW_GEV = 246.22
V_S_GEV = 10.0
V_SIGMA_GEV = 1.0


def pmns_matrix() -> np.ndarray:
    """PDG convention, including the Dirac phase and Majorana phases."""
    s12, s23, s13 = np.sqrt(
        [SIN2_THETA12, SIN2_THETA23, SIN2_THETA13]
    )
    c12, c23, c13 = np.sqrt(
        [1.0 - SIN2_THETA12, 1.0 - SIN2_THETA23, 1.0 - SIN2_THETA13]
    )
    delta = math.radians(DELTA_CP_DEG)
    a21 = math.radians(ALPHA21_DEG)
    a31 = math.radians(ALPHA31_DEG)

    u = np.array(
        [
            [
                c12 * c13,
                s12 * c13 * np.exp(0.5j * a21),
                s13 * np.exp(-1j * delta) * np.exp(0.5j * a31),
            ],
            [
                -s12 * c23 - c12 * s23 * s13 * np.exp(1j * delta),
                (c12 * c23 - s12 * s23 * s13 * np.exp(1j * delta))
                * np.exp(0.5j * a21),
                s23 * c13 * np.exp(0.5j * a31),
            ],
            [
                s12 * s23 - c12 * c23 * s13 * np.exp(1j * delta),
                (-c12 * s23 - s12 * c23 * s13 * np.exp(1j * delta))
                * np.exp(0.5j * a21),
                c23 * c13 * np.exp(0.5j * a31),
            ],
        ],
        dtype=complex,
    )
    return u


def complex_matrix_as_json(matrix: np.ndarray) -> list[list[dict[str, float]]]:
    return [
        [
            {"re": float(value.real), "im": float(value.imag)}
            for value in row
        ]
        for row in matrix
    ]


def main() -> None:
    m2_ev = math.sqrt(M1_EV**2 + DM21_EV2)
    m3_ev = math.sqrt(M1_EV**2 + DM31_EV2)
    masses_ev = np.array([M1_EV, m2_ev, m3_ev])

    u = pmns_matrix()
    mnu_ev = u.conj() @ np.diag(masses_ev) @ u.conj().T
    mnu_gev = 1.0e-9 * mnu_ev
    mdirac = np.diag([M_DIRAC_GEV] * 3).astype(complex)

    # Invert M_nu = -m_D M_R^{-1} m_D^T.
    mr = -mdirac.T @ np.linalg.inv(mnu_gev) @ mdirac
    mnu_reconstructed_ev = (
        -mdirac @ np.linalg.inv(mr) @ mdirac.T
    ) / 1.0e-9

    # M_R is complex symmetric; physical Majorana masses are its Takagi values,
    # equal to the singular values of a complex symmetric matrix.
    heavy_masses_gev = np.linalg.svd(mr, compute_uv=False)
    active_heavy_mixing = mdirac @ np.linalg.inv(mr)

    y_nu = math.sqrt(2.0) * M_DIRAC_GEV / V_EW_GEV
    y_emu = math.sqrt(2.0) * mr[0, 1] / V_SIGMA_GEV
    y_etau = math.sqrt(2.0) * mr[0, 2] / V_SIGMA_GEV
    y_mumu = math.sqrt(2.0) * mr[1, 1] / V_S_GEV
    y_tautau = math.sqrt(2.0) * mr[2, 2] / V_S_GEV

    delta_a = V_SIGMA_GEV**2 / (4.0 * V_S_GEV**2)
    mass_shift = math.sqrt(1.0 + delta_a) - 1.0

    results: dict[str, Any] = {
        "status": "constructive tree-level benchmark; not a statistical fit",
        "source": "NuFIT 6.1 (2025), IC24 + SK, normal ordering",
        "inputs": {
            "sin2_theta12": SIN2_THETA12,
            "sin2_theta23": SIN2_THETA23,
            "sin2_theta13": SIN2_THETA13,
            "delta_cp_deg": DELTA_CP_DEG,
            "dm21_eV2": DM21_EV2,
            "dm31_eV2": DM31_EV2,
            "m1_eV_choice": M1_EV,
            "majorana_phase_21_deg_choice": ALPHA21_DEG,
            "majorana_phase_31_deg_choice": ALPHA31_DEG,
            "mD_GeV_diagonal_choice": M_DIRAC_GEV,
            "vS_GeV_choice": V_S_GEV,
            "vsigma_GeV_choice": V_SIGMA_GEV,
        },
        "light_neutrino_masses_eV": masses_ev.tolist(),
        "sum_light_masses_eV": float(np.sum(masses_ev)),
        "Mnu_eV": complex_matrix_as_json(mnu_ev),
        "MR_GeV": complex_matrix_as_json(mr),
        "heavy_Majorana_masses_GeV": heavy_masses_gev.tolist(),
        "Ynu_diagonal": y_nu,
        "singlet_yukawa_magnitudes": {
            "abs_y_emu": float(abs(y_emu)),
            "abs_y_etau": float(abs(y_etau)),
            "abs_y_mumu": float(abs(y_mumu)),
            "abs_y_tautau": float(abs(y_tautau)),
        },
        "active_heavy_mixing_spectral_norm": float(
            np.linalg.norm(active_heavy_mixing, ord=2)
        ),
        "MR_symmetry_residual_GeV": float(np.linalg.norm(mr - mr.T)),
        "Mnu_reconstruction_residual_eV": float(
            np.linalg.norm(mnu_reconstructed_ev - mnu_ev)
        ),
        "delta_A": delta_a,
        "relative_Aprime_mass_shift": mass_shift,
        "caveat": (
            "No scalar-potential/vacuum, LFV, HNL, cosmology, A-prime, "
            "or statistical-likelihood constraints are evaluated."
        ),
    }
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
