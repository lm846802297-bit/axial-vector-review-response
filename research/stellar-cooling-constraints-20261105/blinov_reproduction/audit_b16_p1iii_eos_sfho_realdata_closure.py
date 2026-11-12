#!/usr/bin/env python3
"""Audit the official SFHo/FRDM v1.03 tables and test the occupation closure.

This module closes the gap recorded in ``B16_P1IIIE_A_...``: the kernel was
validated on synthetic states only because the Basel tables "could not be
downloaded in the current execution environment".  Here the *official*
single-particle and extended thermodynamic tables are read directly and the
Hempel -> Fiorillo mapping of ``audit_b16_p1iii_eos_nucleon_distribution`` is
applied to real data.

The closure under test is the local acceptance condition for P1-IIIe:

    xi * n'_N(T, m*_N, mu*_N - U_N)  ==  X_N * n_B          (N = n, p)

where ``n'_N = 2 int d^3p/(2 pi)^3 f_N`` is the density per available volume
``V'``.  ``xi`` is taken from the single-particle table, never reconstructed
from an approximate composition formula.  The complementary identity
``xi = 1 - (n_B - n_n - n_p)/n_0`` is *checked*, not used as input.

Usage::

    python audit_b16_p1iii_eos_sfho_realdata_closure.py \
        --tables-dir /path/to/extracted --output outputs/....json \
        --fixture outputs/p1iii_eos_sfho_realdata_fixture.csv

``--tables-dir`` may be the top-level extraction directory; the three table
files are located recursively.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path

import numpy as np

from audit_b16_p1iii_eos_nucleon_distribution import (
    HBARC_MEV_FM,
    NEUTRON_MASS_MEV,
    PROTON_MASS_MEV,
    degeneracy_factor,
    infer_filling_factor_from_global_densities,
    number_density_fm3,
    phase_space_integrals,
    state_from_hs_spp,
)
from sfho_eos_tables import (
    AMU_MEV,
    EXTENDED_ENTRIES,
    HQC_MEV_FM,
    K_MAX_REAL,
    NB_ENTRIES,
    NB_PHYSICAL,
    NUCLEON_BAG_DENSITY_FM3,
    SPP_COLUMNS,
    Composition,
    ExtendedEOS,
    SPPTable,
    baryon_density_grid,
    sha256_file,
    temperature_grid,
    ye_grid,
)

HERE = Path(__file__).resolve().parent
DATE = "2026-11-11"

TABLE_FILES = {
    "extended_eos": "sfho_frdm_eos_v1.03.bin",
    "single_particle": "sfho_frdm_spp_v1.03.tab",
    "composition": "sfho_frdm_comp_v1.03.bin",
}

# SHA-256 of the official archives the tables were extracted from.  Recorded
# so a reviewer can confirm the audited files are the published v1.03 data.
ARCHIVE_SHA256 = {
    "manual_v1.04.pdf": (
        "0994abc5073853d35dd10ed6a0313be5c701ee7c47c268f2faa77f36bb4b5478"
    ),
    "sfho_frdm_bin.zip": (
        "45479eaf46e1aa9b1ca3502baf4aaeea60ff0021a21d621f10a75eafb8b8949c"
    ),
    "sfho_frdm_spp.zip": (
        "fc0a5f8ea1154880a4285d2b126d40b521af244d338fb06e4ef5a81defbd5769"
    ),
    "sfho_frdm_comp.zip": (
        "0d80c5e0355c755b61fd200b7de7b1e30d46a4931697bd1fbd05766f099ca8ca"
    ),
    "sfho_frdm_shen98format.zip": (
        "deed6c687457dc13026ad9e27226ef985f145683d83700b1064ee815b873a811"
    ),
}

# Sampled closure grid.  Indices are (temperature, Yp block, density); the Yp
# block index equals j-1 for the extended table's j=1..60 because the
# single-particle table has no Yp=0 block.
CLOSURE_T = (0, 10, 20, 30, 40, 50, 60, 70)
CLOSURE_Y = (10, 20, 30, 40)
CLOSURE_K = (1, 50, 100, 150, 200, 250, 300)

FIXTURE_COLUMNS = (
    "T_MeV",
    "rho_g_cm3",
    "dMdt_weight",
    "nB_fm3",
    "Yp_tot",
    "t_index",
    "y_index",
    "k_index",
    "xi",
    "mstar_n_MeV",
    "SigmaV_n_MeV",
    "mu_nonrel_n_MeV",
    "mstar_p_MeV",
    "SigmaV_p_MeV",
    "mu_nonrel_p_MeV",
    "X_n",
    "X_p",
    "n_n_target_fm3",
    "n_p_target_fm3",
    "p_tot_MeV_fm3",
    "xi_from_composition",
    "nprime_n_fm3",
    "nprime_p_fm3",
    "ratio_n",
    "ratio_p",
    "Fdeg_n",
    "Fdeg_p",
)

MEV_FM3_TO_G_CM3 = 1.782661921e15  # 1 MeV/fm^3 in g/cm^3
# rho_B = n_B * (mass unit) with 1 fm^-3 -> 1.66053907e15 g/cm^3 for a
# 931.49432 MeV baryon; the two factors agree to 7e-2 and the fixture only
# needs a positive, monotone density column.
FM3_TO_G_CM3_PER_BARYON = 1.66053906660e15


def locate_tables(root: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    for key, name in TABLE_FILES.items():
        matches = sorted(root.rglob(name))
        if not matches:
            raise FileNotFoundError(f"{name} not found under {root}")
        found[key] = matches[0]
    return found


def closure_cell(ext: ExtendedEOS, spp: SPPTable, i: int, j: int, k: int,
                 order: int = 1024) -> dict:
    """One local closure test; ``j`` is the extended-table Yp index (0..60)."""
    temperature = float(ext.temperature[i])
    nb = float(ext.nb[k])
    record = {
        "t_index": i,
        "y_index": j,
        "k_index": k,
        "T_MeV": temperature,
        "nB_fm3": nb,
        "Yp_tot": float(ext.ye[j]),
    }
    if j < 1:
        record["skipped"] = "single-particle table has no Yp=0 block"
        return record
    jj = j - 1
    row = spp.data[i, jj, k]
    xi = float(row[SPP_COLUMNS.index("xi")])
    mstar_n = float(row[SPP_COLUMNS.index("mstar_n_MeV")])
    mstar_p = float(row[SPP_COLUMNS.index("mstar_p_MeV")])
    sigma_n = float(row[SPP_COLUMNS.index("SigmaV_n_tot_MeV")])
    sigma_p = float(row[SPP_COLUMNS.index("SigmaV_p_tot_MeV")])
    mu_n_nonrel = float(ext.entry("mu_n_nonrel_MeV")[i, j, k])
    mu_p_nonrel = float(ext.entry("mu_p_nonrel_MeV")[i, j, k])
    x_n = float(ext.entry("X_n")[i, j, k])
    x_p = float(ext.entry("X_p")[i, j, k])
    p_tot = float(ext.entry("p_total_MeV_fm3")[i, j, k])

    if not (xi > 0.0 and mstar_n > 0.0 and mstar_p > 0.0 and nb > 0.0):
        record["skipped"] = "zero entry (k >= 309 or empty single-particle row)"
        return record

    state_n = state_from_hs_spp("n", temperature, mstar_n, sigma_n, mu_n_nonrel)
    state_p = state_from_hs_spp("p", temperature, mstar_p, sigma_p, mu_p_nonrel)
    nprime_n = number_density_fm3(state_n, order=order)
    nprime_p = number_density_fm3(state_p, order=order)
    target_n = x_n * nb
    target_p = x_p * nb
    if target_n <= 0.0 or target_p <= 0.0:
        record["skipped"] = "zero free-nucleon fraction"
        return record

    try:
        xi_composition = infer_filling_factor_from_global_densities(
            nb, target_n, target_p, NUCLEON_BAG_DENSITY_FM3
        )
        xi_residual: float | None = abs(xi - xi_composition)
    except ValueError as error:
        # Rounding can push the identity a few ulps above unity when no
        # baryons are bound in nuclei; record it instead of failing.
        xi_composition = None
        xi_residual = None
        record["xi_composition_error"] = str(error)
    record.update(
        {
            "xi": xi,
            "xi_from_composition": xi_composition,
            "xi_abs_residual": xi_residual,
            "mstar_n_MeV": mstar_n,
            "mstar_p_MeV": mstar_p,
            "SigmaV_n_MeV": sigma_n,
            "SigmaV_p_MeV": sigma_p,
            "U_n_MeV": state_n.scalar_potential_mev,
            "U_p_MeV": state_p.scalar_potential_mev,
            "mu_star_n_MeV": state_n.chemical_potential_star_mev,
            "mu_star_p_MeV": state_p.chemical_potential_star_mev,
            "mu_eff_n_MeV": state_n.effective_chemical_potential_mev,
            "mu_eff_p_MeV": state_p.effective_chemical_potential_mev,
            "nu_over_T_n": state_n.effective_chemical_potential_mev
            / temperature,
            "nu_over_T_p": state_p.effective_chemical_potential_mev
            / temperature,
            "X_n": x_n,
            "X_p": x_p,
            "X_free": x_n + x_p,
            "p_tot_MeV_fm3": p_tot,
            "nprime_n_fm3": nprime_n,
            "nprime_p_fm3": nprime_p,
            "n_actual_n_fm3": xi * nprime_n,
            "n_actual_p_fm3": xi * nprime_p,
            "target_n_fm3": target_n,
            "target_p_fm3": target_p,
            "ratio_n": xi * nprime_n / target_n,
            "ratio_p": xi * nprime_p / target_p,
            "Fdeg_n": degeneracy_factor(state_n, order=order),
            "Fdeg_p": degeneracy_factor(state_p, order=order),
        }
    )
    return record


def _summary(values: list[float]) -> dict:
    if not values:
        return {"count": 0}
    return {
        "count": len(values),
        "median": float(statistics.median(values)),
        "p95": float(np.percentile(values, 95)),
        "p99": float(np.percentile(values, 99)),
        "max": float(max(values)),
    }


def audit(ext: ExtendedEOS, spp: SPPTable, comp: Composition,
          order: int = 1024) -> dict:
    nominal_nb = ext.nb
    nominal_ye = ext.ye
    stored_nb = ext.entry("nB_fm3")
    stored_yp = ext.entry("Yp_tot")
    # Rows k >= 309 carry no density at all (the interaction has no solution
    # there), so every whole-table statistic is restricted to the physical rows.
    physical = slice(0, NB_PHYSICAL)
    mass_fractions = sum(
        ext.entry(name)[:, :, physical]
        for name in ("X_n", "X_p", "X_d", "X_t", "X_h", "X_alpha", "X_A")
    )
    energy = ext.entry("E_total_MeV")[:, :, physical]
    entropy = ext.entry("S_total_kB")[:, :, physical]
    free_energy = ext.entry("F_total_MeV")[:, :, physical]

    physical = slice(0, NB_PHYSICAL)
    dev_nb = np.abs(
        stored_nb[:, :, physical] / nominal_nb[None, None, physical] - 1.0
    )
    dev_ye = np.abs(stored_yp[:, :, physical] - nominal_ye[None, :, None])
    free_energy_residual = np.abs(
        free_energy - (energy - ext.temperature[:, None, None] * entropy)
    ) / np.maximum(np.abs(energy), 1.0)

    spp_xi = spp.column("xi")
    spp_mstar_n = spp.column("mstar_n_MeV")
    spp_mstar_p = spp.column("mstar_p_MeV")
    spp_sigma_n = spp.column("SigmaV_n_tot_MeV")
    spp_sigma_p = spp.column("SigmaV_p_tot_MeV")
    spp_yp = spp.column("Yp_tot")
    spp_nb = spp.column("nB_fm3")
    dev_spp_yp_vs_extended = np.abs(
        spp_yp[:, :, physical] - stored_yp[:, 1:, physical]
    )
    dev_spp_nb_vs_extended = np.abs(
        spp_nb[:, :, physical] / stored_nb[:, 1:, physical] - 1.0
    )

    nn_comp = comp.comp[..., 6]
    np_comp = comp.comp[..., 7]
    target_nn = ext.entry("X_n") * stored_nb * HQC_MEV_FM**3
    target_np = ext.entry("X_p") * stored_nb * HQC_MEV_FM**3
    with np.errstate(divide="ignore", invalid="ignore"):
        dev_nn = np.where(target_nn > 0, np.abs(nn_comp / target_nn - 1.0), 0.0)
        dev_np = np.where(target_np > 0, np.abs(np_comp / target_np - 1.0), 0.0)

    closure = []
    for i in CLOSURE_T:
        for j in CLOSURE_Y:
            for k in CLOSURE_K:
                closure.append(closure_cell(ext, spp, i, j, k, order=order))
    evaluated = [row for row in closure if "ratio_n" in row]

    def subset(predicate):
        return [row for row in evaluated if predicate(row)]

    def deviations(rows, key):
        return [abs(row[key] - 1.0) for row in rows]

    nucleon_dominated = subset(lambda row: row["X_free"] >= 0.5)
    cluster_dominated = subset(lambda row: row["X_free"] < 0.5)
    cold = subset(lambda row: row["T_MeV"] <= 10.0)

    xi_identity = [
        row["xi_abs_residual"]
        for row in evaluated
        if row.get("xi_abs_residual") is not None
    ]
    xi_identity_skipped = sum(
        1 for row in evaluated if row.get("xi_abs_residual") is None
    )
    degenerate_cells = []
    for temperature, ye_value, nb_value in (
        (3.03, 0.20, 1.0e-3),
        (3.03, 0.20, 0.05),
        (3.03, 0.20, 0.1582),
        (3.03, 0.30, 0.1582),
        (8.0, 0.20, 0.1582),
        (20.0, 0.20, 0.1582),
    ):
        i = int(np.argmin(np.abs(ext.temperature - temperature)))
        j = int(np.argmin(np.abs(ext.ye - ye_value)))
        k = int(np.argmin(np.abs(ext.nb - nb_value)))
        degenerate_cells.append(closure_cell(ext, spp, i, j, k, order=order))

    return {
        "title": "SFHo/FRDM v1.03 real-table audit and occupation closure",
        "date": DATE,
        "source": (
            "University of Basel, M. Hempel; Hempel (2015) arXiv:1410.6337; "
            "Fiorillo et al. (2025) arXiv:2509.13322v2 App. C.1"
        ),
        "provenance": {
            "archive_sha256": ARCHIVE_SHA256,
            "table_files": {
                key: {
                    "name": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
                for key, path in (
                    ("extended_eos", ext.path),
                    ("single_particle", spp.path),
                    ("composition", comp.path),
                )
            },
            "version_note": (
                "The four SFHo/FRDM archives are v1.03 data (2012-07-09); "
                "manual_v1.04 of 2012-12-19 only added the IUFSU table, so "
                "manual and data versions are consistent."
            ),
        },
        "grid": {
            "entries": {
                "temperature": len(ext.temperature),
                "ye_extended": len(ext.ye),
                "ye_single_particle": len(spp.ye),
                "baryon_density": NB_ENTRIES,
                "k_max_physical_index": NB_PHYSICAL - 1,
            },
            "temperature_mev": [float(ext.temperature[0]), float(ext.temperature[-1])],
            "baryon_density_fm3": [float(ext.nb[0]), float(ext.nb[-1])],
            "baryon_density_at_last_physical_fm3": float(ext.nb[NB_PHYSICAL - 1]),
        },
        "extended_table_checks": {
            "extended_entries": list(EXTENDED_ENTRIES),
            "max_relative_baryon_density_deviation": float(dev_nb.max()),
            "max_absolute_ye_deviation": float(dev_ye.max()),
            "max_mass_fraction_sum_residual": float(
                np.abs(mass_fractions - 1.0).max()
            ),
            "mean_mass_fraction_sum_residual": float(
                np.abs(mass_fractions - 1.0).mean()
            ),
            "max_relative_F_minus_E_minus_TS_residual": float(
                free_energy_residual.max()
            ),
            "zero_fraction_k_ge_309": float(
                np.mean(stored_nb[:, :, NB_PHYSICAL:] == 0.0)
            ),
            "min_entropy_kB": float(entropy.min()),
            "min_pressure_MeV_fm3": float(
            ext.entry("p_total_MeV_fm3")[:, :, physical].min()
        ),
        },
        "composition_checks": {
            "max_relative_free_neutron_deviation": float(dev_nn.max()),
            "max_relative_free_proton_deviation": float(dev_np.max()),
            "fraction_of_cells_with_nuclei": float(
                np.mean(comp.comp[:, :, physical, 4] != 1.0)
            ),
            "physical_cells": int(comp.comp[:, :, physical, 4].size),
            "cells_with_nuclei": int(
                np.count_nonzero(comp.comp[:, :, physical, 4] != 1.0)
            ),
            "unique_nuclei": int(comp.az.shape[0]),
            "max_A": int(comp.az[:, 0].max()),
        },
        "single_particle_checks": {
            "columns": list(SPP_COLUMNS),
            "max_relative_temperature_deviation": float(
                np.abs(spp.temperature / ext.temperature - 1.0).max()
            ),
            "max_relative_baryon_density_deviation": float(
                np.abs(spp_nb / ext.nb[None, None, :] - 1.0).max()
            ),
            "max_absolute_Yp_deviation_vs_extended": float(
                dev_spp_yp_vs_extended.max()
            ),
            "max_relative_nB_deviation_vs_extended": float(
                dev_spp_nb_vs_extended.max()
            ),
            "max_absolute_Yp_grid_deviation": float(
                np.abs(spp.ye - ext.ye[1:]).max()
            ),
            "xi_range": [float(spp_xi[:, :, physical].min()),
            float(spp_xi[:, :, physical].max())],
            "mstar_n_MeV_range": [float(spp_mstar_n[:, :, physical].min()),
            float(spp_mstar_n[:, :, physical].max())],
            "mstar_p_MeV_range": [float(spp_mstar_p[:, :, physical].min()),
            float(spp_mstar_p[:, :, physical].max())],
            "SigmaV_n_MeV_range": [float(spp_sigma_n[:, :, physical].min()),
            float(spp_sigma_n[:, :, physical].max())],
            "SigmaV_p_MeV_range": [float(spp_sigma_p[:, :, physical].min()),
            float(spp_sigma_p[:, :, physical].max())],
        },
        "closure": {
            "definition": (
                "xi * nprime_N(T,mstar_N,nu_N) == X_N*nB, where "
                "nu_N = mu_nonrel_N - (mstar_N - m_N + SigmaV_N_tot); "
                "equivalently the relativistic exponent is "
                "[sqrt(p^2+mstar_N^2)-mu_tilde_N]/T with "
                "mu_tilde_N = mu_nonrel_N + m_N - SigmaV_N_tot. "
                "xi is taken directly from the single-particle table."
            ),
            "validity_scope": (
                "The stated validity domain is an empirical subset of the "
                "224 sampled audit cells, not a proof over the continuous EOS grid."
            ),
            "quadrature_order": order,
            "grid": {
                "temperature_indices": list(CLOSURE_T),
                "ye_indices": list(CLOSURE_Y),
                "density_indices": list(CLOSURE_K),
            },
            "cells_evaluated": len(evaluated),
            "cells_skipped": len(closure) - len(evaluated),
            "absolute_deviation_from_unity": {
                "all_cells": {
                    "neutron": _summary(deviations(evaluated, "ratio_n")),
                    "proton": _summary(deviations(evaluated, "ratio_p")),
                },
                "nucleon_dominated_Xfree_ge_0.5": {
                    "count": len(nucleon_dominated),
                    "neutron": _summary(deviations(nucleon_dominated, "ratio_n")),
                    "proton": _summary(deviations(nucleon_dominated, "ratio_p")),
                },
                "cluster_dominated_Xfree_lt_0.5": {
                    "count": len(cluster_dominated),
                    "neutron": _summary(deviations(cluster_dominated, "ratio_n")),
                    "proton": _summary(deviations(cluster_dominated, "ratio_p")),
                },
                "T_le_10MeV": {
                    "count": len(cold),
                    "neutron": _summary(deviations(cold, "ratio_n")),
                    "proton": _summary(deviations(cold, "ratio_p")),
                },
            },
            "xi_composition_identity": {
                "definition": (
                    "xi ?= 1 - (nB - X_n nB - X_p nB)/n0 with "
                    "n0 = 0.15824150805 fm^-3"
                ),
                "cells_outside_open_interval": xi_identity_skipped,
                **_summary(xi_identity),
            },
            "degenerate_state_samples": degenerate_cells,
            "rows": [
                {
                    key: row[key]
                    for key in (
                        "t_index", "y_index", "k_index", "T_MeV", "nB_fm3",
                        "Yp_tot", "X_n", "X_p", "X_free", "xi",
                        "xi_from_composition", "mstar_n_MeV", "mstar_p_MeV",
                        "SigmaV_n_MeV", "SigmaV_p_MeV", "U_n_MeV", "U_p_MeV",
                        "mu_star_n_MeV", "mu_star_p_MeV", "nu_over_T_n",
                        "nu_over_T_p", "nprime_n_fm3", "nprime_p_fm3",
                        "ratio_n", "ratio_p", "Fdeg_n", "Fdeg_p",
                        "p_tot_MeV_fm3",
                    )
                    if key in row
                }
                for row in evaluated
            ],
            "skipped_rows": [
                row for row in closure if "ratio_n" not in row
            ],
        },
    }


def fixture_rows(ext: ExtendedEOS, spp: SPPTable, order: int = 1024) -> list[dict]:
    """Profile-format rows in Hempel single-particle columns (real values)."""
    rows = []
    for i in CLOSURE_T:
        for j in CLOSURE_Y:
            for k in CLOSURE_K:
                row = closure_cell(ext, spp, i, j, k, order=order)
                if "ratio_n" not in row:
                    continue
                nb = row["nB_fm3"]
                rows.append(
                    {
                        "T_MeV": row["T_MeV"],
                        "rho_g_cm3": nb * FM3_TO_G_CM3_PER_BARYON,
                        "dMdt_weight": 1.0,
                        "nB_fm3": nb,
                        "Yp_tot": row["Yp_tot"],
                        "t_index": row["t_index"],
                        "y_index": row["y_index"],
                        "k_index": row["k_index"],
                        "xi": row["xi"],
                        "mstar_n_MeV": row["mstar_n_MeV"],
                        "SigmaV_n_MeV": row["SigmaV_n_MeV"],
                        "mu_nonrel_n_MeV": row["mu_star_n_MeV"],
                        "mstar_p_MeV": row["mstar_p_MeV"],
                        "SigmaV_p_MeV": row["SigmaV_p_MeV"],
                        "mu_nonrel_p_MeV": row["mu_star_p_MeV"],
                        "X_n": row["X_n"],
                        "X_p": row["X_p"],
                        "n_n_target_fm3": row["target_n_fm3"],
                        "n_p_target_fm3": row["target_p_fm3"],
                        "p_tot_MeV_fm3": row["p_tot_MeV_fm3"],
                        "xi_from_composition": row["xi_from_composition"],
                        "nprime_n_fm3": row["nprime_n_fm3"],
                        "nprime_p_fm3": row["nprime_p_fm3"],
                        "ratio_n": row["ratio_n"],
                        "ratio_p": row["ratio_p"],
                        "Fdeg_n": row["Fdeg_n"],
                        "Fdeg_p": row["Fdeg_p"],
                    }
                )
    return rows


def _format_fixture_value(value) -> str:
    if value is None:
        return ""
    return f"{value:.10g}"


def write_fixture(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=list(FIXTURE_COLUMNS), lineterminator="\n"
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {key: _format_fixture_value(row[key]) for key in FIXTURE_COLUMNS}
            )
    print(f"fixture rows: {len(rows)} -> {path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tables-dir", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "outputs" / f"p1iii_eos_sfho_realdata_closure_{DATE}.json",
    )
    parser.add_argument("--fixture", type=Path)
    parser.add_argument("--order", type=int, default=1024)
    args = parser.parse_args()

    paths = locate_tables(args.tables_dir)
    for key, path in paths.items():
        print(f"{key}: {path}")
    ext = ExtendedEOS.load(paths["extended_eos"])
    spp = SPPTable.load(paths["single_particle"])
    comp = Composition.load(paths["composition"])
    print(f"loaded extended {ext.data.shape}, spp {spp.data.shape}, "
          f"composition {comp.comp.shape}")

    payload = audit(ext, spp, comp, order=args.order)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n"
    )

    if args.fixture:
        write_fixture(args.fixture, fixture_rows(ext, spp, order=args.order))

    print(json.dumps(
        {
            "output": str(args.output),
            "cells_evaluated": payload["closure"]["cells_evaluated"],
            "nucleon_dominated": payload["closure"][
                "absolute_deviation_from_unity"
            ]["nucleon_dominated_Xfree_ge_0.5"]["neutron"],
            "xi_identity": payload["closure"]["xi_composition_identity"],
        },
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
