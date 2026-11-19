"""Quantify the charge-conjugate muon contribution to Croon C0 opacity.

The literal Croon/Bollig convention uses the single mu-minus f_mu(E, +mu_mu)
distribution. This separate sensitivity adds the equilibrium mu-plus
distribution f_mu(E, -mu_mu) to both the local source and opacity. It is
not substituted into the literal Fig. 2 reproduction.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from audit_croon_outer_muon_opacity_envelope import (
    DEFAULT_COUPLINGS,
    DEFAULT_PROFILE,
    run_outer_muon_opacity_envelope,
)

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "outputs" / "croon_antimuon_opacity_sensitivity_2026-11-19.json"


def run_antimuon_sensitivity(
    profile_path: Path = DEFAULT_PROFILE,
    couplings: np.ndarray = DEFAULT_COUPLINGS,
    energy_order: int = 96,
    tau_grid_points: int = 601,
    susceptibility_order: int = 256,
) -> dict:
    couplings = np.asarray(couplings, dtype=float)
    if couplings.ndim != 1 or len(couplings) == 0 or np.any(couplings <= 0.0):
        raise ValueError("Couplings must be a nonempty positive one-dimensional array")
    common = {
        "profile_path": Path(profile_path),
        "mass_MeV": 1.0e-7,
        "couplings": couplings,
        "energy_order": energy_order,
        "tau_grid_points": tau_grid_points,
        "susceptibility_order": susceptibility_order,
        "neutrino_flavour_factor": 2.0,
    }
    mu_minus = run_outer_muon_opacity_envelope(
        **common, include_antimuons=False
    )
    mu_pm = run_outer_muon_opacity_envelope(
        **common, include_antimuons=True
    )

    minus_rows = mu_minus["luminosity_comparison"]
    pm_rows = mu_pm["luminosity_comparison"]
    if len(minus_rows) != len(pm_rows):
        raise RuntimeError("Charge-conjugate runs returned inconsistent coupling grids")

    comparison = []
    for minus, both in zip(minus_rows, pm_rows):
        if minus["g_X"] != both["g_X"]:
            raise RuntimeError("Charge-conjugate runs returned mismatched couplings")
        comparison.append({
            "g_X": minus["g_X"],
            "mu_minus_only_Rnu_over_Tedge_ratio":
                minus["Rnu_over_Tedge_envelope_luminosity_ratio"],
            "mu_pm_Rnu_over_Tedge_ratio":
                both["Rnu_over_Tedge_envelope_luminosity_ratio"],
            "mu_minus_only_Rnu_over_T3_ratio":
                minus["Rnu_over_T3_envelope_luminosity_ratio"],
            "mu_pm_Rnu_over_T3_ratio":
                both["Rnu_over_T3_envelope_luminosity_ratio"],
            "L_Rfar100_mu_pm_over_mu_minus":
                both["L_Rfar100_outer_chi_edge_Tedge_erg_s"]
                / minus["L_Rfar100_outer_chi_edge_Tedge_erg_s"],
            "mu_minus_only_gap_remaining":
                3.38190 / minus["Rnu_over_Tedge_envelope_luminosity_ratio"],
            "mu_pm_gap_remaining":
                3.38190 / both["Rnu_over_Tedge_envelope_luminosity_ratio"],
        })

    p_minus = mu_minus["profile"]
    p_pm = mu_pm["profile"]
    edge_minus = p_minus["last_nonzero_digitized_muon_sample"]["chi_mu_MeV3"]
    edge_pm = p_pm["last_nonzero_digitized_muon_sample"]["chi_mu_MeV3"]
    rnu_minus = float(p_minus.get("chi_mu_Rnu_MeV3", 0.0))
    rnu_pm = float(p_pm.get("chi_mu_Rnu_MeV3", 0.0))

    return {
        "title": "Croon C0 charge-conjugate muon opacity sensitivity",
        "source_paper": "Croon et al., JHEP 01 (2021) 107, arXiv:2006.13942",
        "reference_convention": (
            "Literal baseline uses the single mu-minus Fermi distribution "
            "f(E,+mu_mu), following the Fdeg definition quoted from Bollig et al."
        ),
        "sensitivity_convention": (
            "Adds the charge-conjugate mu-plus distribution f(E,-mu_mu) "
            "to the susceptibility used in both local production and absorption. "
            "This is a physical extension, not the literal Croon Fig. 2 convention."
        ),
        "profile": {
            "sha256": p_minus["sha256"],
            "path": p_minus["path"],
            "rows": p_minus["rows"],
            "R_nu_km": p_minus["R_nu_km"],
            "edge": p_minus["last_nonzero_digitized_muon_sample"],
            "chi_edge_mu_minus_MeV3": edge_minus,
            "chi_edge_mu_pm_MeV3": edge_pm,
            "chi_edge_total_over_mu_minus": edge_pm / edge_minus,
            "chi_Rnu_mu_minus_MeV3": rnu_minus,
            "chi_Rnu_mu_pm_MeV3": rnu_pm,
            "chi_Rnu_total_over_mu_minus": (
                rnu_pm / rnu_minus if rnu_minus > 0.0 else None
            ),
        },
        "quadrature": {
            "susceptibility_order": susceptibility_order,
            "local_energy_order": energy_order,
            "optical_depth_energy_grid_points": tau_grid_points,
        },
        "target_paper_solid_over_dashed_median": 3.38190,
        "comparison": comparison,
        "interpretation": [
            "The charge-conjugate contribution is largest in relative terms where mu_mu/T is small; it can raise the edge susceptibility by an order-one factor.",
            "The effect is evaluated consistently in the local source and in the inverse semi-Compton opacity.",
            "The result must remain a separate sensitivity because the printed Croon/Bollig Fdeg convention uses f_mu(E,+mu_mu) only.",
            "If the full source-weighted mu-plus extension remains far below the published solid/dashed factor, charge conjugation does not close the outer-opacity gap.",
        ],
        "not_included": [
            "raw Garching outer profile",
            "new absorption channels beyond Croon Eqs. (4.6)-(4.7)",
            "axial-vector rates or limits",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--energy-order", type=int, default=96)
    parser.add_argument("--tau-grid-points", type=int, default=601)
    parser.add_argument("--susceptibility-order", type=int, default=256)
    args = parser.parse_args()
    result = run_antimuon_sensitivity(
        profile_path=args.profile,
        energy_order=args.energy_order,
        tau_grid_points=args.tau_grid_points,
        susceptibility_order=args.susceptibility_order,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\\n", encoding="utf-8")
    print(json.dumps({
        "profile": result["profile"],
        "comparison": result["comparison"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
