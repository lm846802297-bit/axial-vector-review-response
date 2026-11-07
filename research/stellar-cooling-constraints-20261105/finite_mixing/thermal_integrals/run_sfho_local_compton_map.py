"""Generate radius/energy/polarization-resolved moving-muon Compton rates.

The input is the repository's reconstructed SFHo-18.8, 1 s profile, not
the access-controlled original simulation table. Rates are local-frame,
unit-gX^2 coefficients for the finite-mixing UV benchmark.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PROFILE = ROOT / "data" / "sfho188_digitized.csv"
PROVENANCE = ROOT / "data" / "profile_provenance.json"
sys.path.insert(0, str(ROOT))

from finite_mixing.model import muon_couplings
from finite_mixing.thermal_integrals.moving_compton import moving_muon_compton_rates

MODES = ("L", "+", "-")
RADII_KM = (0.0, 5.0, 8.0, 10.0, 15.0, 20.0, 24.0)
MASSES_MEV = (10.0, 100.0, 220.0, 300.0)
ENERGY_RATIOS = (1.05, 1.5, 3.0, 10.0)
THETA_MU_R = 1.0e-2


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_background(path: Path, radii: tuple[float, ...]):
    data = np.genfromtxt(path, delimiter=",", names=True)
    rgrid = np.asarray(data["r_km"], float)
    if rgrid.ndim != 1 or len(rgrid) < 2 or np.any(np.diff(rgrid) <= 0):
        raise ValueError("Profile radial grid must be strictly increasing")
    if radii[0] < rgrid[0] or radii[-1] > rgrid[-1]:
        raise ValueError("Requested radii lie outside the tabulated profile")
    names = ("T_MeV", "mu_mu_MeV", "mu_numu_MeV", "lapse")
    result = {name: np.interp(radii, rgrid, data[name]) for name in names}
    if np.any(result["T_MeV"] <= 0) or np.any(result["lapse"] <= 0):
        raise ValueError("Profile contains nonpositive temperature or lapse")
    return result


def evaluate_point(mass, omega, temperature, mu_mu, gv, ga,
                   radial_order, angular_order, azimuth_order):
    return moving_muon_compton_rates(
        mass, omega, temperature, mu_mu, gv, ga,
        radial_order=radial_order,
        angular_order=angular_order,
        azimuth_order=azimuth_order,
        chunk_size=4096,
    )


def relative_difference(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.max(np.abs(a-b)/np.maximum(np.abs(b), 1e-300)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--output", type=Path, default=HERE / "outputs" / "sfho188_local_compton_rates.json")
    parser.add_argument("--radial-order", type=int, default=16)
    parser.add_argument("--angular-order", type=int, default=8)
    parser.add_argument("--azimuth-order", type=int, default=12)
    args = parser.parse_args()
    if min(args.radial_order, args.angular_order, args.azimuth_order) < 4:
        raise ValueError("Quadrature orders must be at least four")

    radii = np.asarray(RADII_KM, float)
    bg = load_background(args.profile, radii)
    uv = muon_couplings(1.0, THETA_MU_R)
    # These are coefficients normalized to g_X^2; no value of g_X is selected.
    gv, ga = uv.g_vector, uv.g_axial
    points = []
    started = time.time()
    for ir, radius in enumerate(radii):
        temperature = float(bg["T_MeV"][ir])
        chemical = float(bg["mu_mu_MeV"][ir])
        lapse = float(bg["lapse"][ir])
        for mass in MASSES_MEV:
            for ratio in ENERGY_RATIOS:
                omega = mass * ratio
                result = evaluate_point(
                    mass, omega, temperature, chemical, gv, ga,
                    args.radial_order, args.angular_order, args.azimuth_order,
                )
                points.append({
                    "radius_km": float(radius),
                    "temperature_MeV": temperature,
                    "muon_chemical_potential_MeV": chemical,
                    "lapse": lapse,
                    "mass_MeV": mass,
                    "omega_local_MeV": omega,
                    "omega_infinity_MeV": lapse*omega,
                    "omega_over_mass": ratio,
                    "gamma_prod_total_by_mode_MeV": [
                        float(x) for x in result["Gamma_prod_by_mode"]
                    ],
                    "gamma_abs_total_by_mode_MeV": [
                        float(x) for x in result["Gamma_abs_by_mode"]
                    ],
                    "charge_contributions": {
                        charge: {
                            "gamma_prod_by_mode_MeV": [
                                float(x) for x in values["Gamma_prod_by_mode"]
                            ],
                            "gamma_abs_by_mode_MeV": [
                                float(x) for x in values["Gamma_abs_by_mode"]
                            ],
                            "detailed_balance_relative_residual": values[
                                "max_detailed_balance_relative_residual"
                            ],
                        }
                        for charge, values in result["charge_contributions"].items()
                    },
                    "total_detailed_balance_relative_residual":
                        result["max_detailed_balance_relative_residual"],
                    "quadrature_points_all_charges":
                        result["total_quadrature_points_all_charges"],
                })
        print(f"r={radius:5.1f} km completed ({len(points)} points; "
              f"{time.time()-started:.1f} s)", flush=True)

    # Higher-order local checks at representative core, peak-muon, and outer-core points.
    refinement_specs = ((0.0, 100.0, 1.5), (8.0, 100.0, 1.5),
                        (10.0, 220.0, 1.5), (15.0, 100.0, 3.0))
    refinements = []
    for radius, mass, ratio in refinement_specs:
        idx = int(np.where(radii == radius)[0][0])
        t, mu = float(bg["T_MeV"][idx]), float(bg["mu_mu_MeV"][idx])
        omega = mass*ratio
        coarse = evaluate_point(
            mass, omega, t, mu, gv, ga,
            args.radial_order, args.angular_order, args.azimuth_order,
        )
        fine = evaluate_point(mass, omega, t, mu, gv, ga, 32, 12, 20)
        refinements.append({
            "radius_km": radius, "mass_MeV": mass, "omega_over_mass": ratio,
            "coarse_absorption_by_mode_MeV": [
                float(x) for x in coarse["Gamma_abs_by_mode"]
            ],
            "fine_absorption_by_mode_MeV": [
                float(x) for x in fine["Gamma_abs_by_mode"]
            ],
            "relative_difference_absorption":
                relative_difference(coarse["Gamma_abs_by_mode"],
                                    fine["Gamma_abs_by_mode"]),
            "fine_detailed_balance_relative_residual":
                fine["max_detailed_balance_relative_residual"],
        })

    # Pure-current endpoint comparison at three representative background locations.
    endpoint_checks = []
    for radius in (0.0, 8.0, 15.0):
        idx = int(np.where(radii == radius)[0][0])
        t, mu = float(bg["T_MeV"][idx]), float(bg["mu_mu_MeV"][idx])
        mass, omega = 100.0, 150.0
        vector = evaluate_point(mass, omega, t, mu, 1.0, 0.0, 24, 10, 16)
        axial = evaluate_point(mass, omega, t, mu, 0.0, -1.0, 24, 10, 16)
        mixed = evaluate_point(mass, omega, t, mu, gv, ga, 24, 10, 16)
        endpoint_checks.append({
            "radius_km": radius, "temperature_MeV": t,
            "muon_chemical_potential_MeV": mu,
            "pure_vector_absorption_by_mode_MeV": [
                float(x) for x in vector["Gamma_abs_by_mode"]
            ],
            "pure_axial_absorption_by_mode_MeV": [
                float(x) for x in axial["Gamma_abs_by_mode"]
            ],
            "finite_mixing_absorption_by_mode_MeV": [
                float(x) for x in mixed["Gamma_abs_by_mode"]
            ],
            "finite_mixing_over_pure_axial_by_mode": [
                float(x) for x in (
                    mixed["Gamma_abs_by_mode"]/axial["Gamma_abs_by_mode"]
                )
            ],
        })

    max_balance = max(x["total_detailed_balance_relative_residual"] for x in points)
    max_refine = max(x["relative_difference_absorption"] for x in refinements)
    payload = {
        "title": "Moving-muon semi-Compton local rates on reconstructed SFHo-18.8 profile",
        "scope": (
            "Local-frame muon-photon Compton production and absorption only. "
            "No neutrino or dimuon channels, radial integration, optical depth, "
            "transport, luminosity, or exclusion curve."
        ),
        "background_identity": (
            "Reconstructed SFHo-18.8, t_pb=1 s digitized profile; not original "
            "simulation tables and not an exact Blinov Fig. 7 background."
        ),
        "profile_file": args.profile.name,
        "profile_sha256": sha256(args.profile),
        "profile_provenance_sha256": sha256(PROVENANCE),
        "coupling_convention": {
            "normalization": "All rates are coefficients multiplying g_X^2",
            "theta_mu_R": THETA_MU_R,
            "gV_over_gX": gv,
            "gA_over_gX": ga,
            "g_nu_mu_over_gX": 1.0,
            "g_nu_tau_over_gX": -1.0,
            "note": "Neutrino couplings are recorded for model bookkeeping; neutrino rates are not included in this Compton-only output."
        },
        "units": {
            "radius": "km", "temperature_chemical_potential_energy": "MeV",
            "gamma_prod_gamma_abs": "MeV (local inverse-time/rate)",
        },
        "polarization_order": list(MODES),
        "grid": {
            "radii_km": list(RADII_KM), "masses_MeV": list(MASSES_MEV),
            "omega_over_mass": list(ENERGY_RATIOS),
            "quadrature": {
                "radial": args.radial_order, "polar_angle": args.angular_order,
                "photon_polar_angle": args.angular_order,
                "relative_azimuth": args.azimuth_order,
            },
            "points": len(points),
        },
        "acceptance": {
            "all_rates_finite_and_nonnegative": bool(all(
                np.all(np.isfinite(x["gamma_prod_total_by_mode_MeV"]))
                and np.all(np.isfinite(x["gamma_abs_total_by_mode_MeV"]))
                and np.all(np.asarray(x["gamma_prod_total_by_mode_MeV"]) >= 0)
                and np.all(np.asarray(x["gamma_abs_total_by_mode_MeV"]) >= 0)
                for x in points
            )),
            "detailed_balance_max_relative_residual": max_balance,
            "detailed_balance_pass": max_balance < 2e-10,
            "refinement_max_relative_difference": max_refine,
            "refinement_pass": max_refine < 5e-3,
        },
        "refinement_checks": refinements,
        "pure_current_endpoint_checks": endpoint_checks,
        "local_rates": points,
        "runtime_seconds": time.time()-started,
        "source_sha256": {
            "moving_compton.py": sha256(HERE / "moving_compton.py"),
            "model.py": sha256(HERE.parent / "model.py"),
            "runner.py": sha256(Path(__file__)),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(payload["acceptance"], indent=2))
    if not all(payload["acceptance"][key] for key in (
        "all_rates_finite_and_nonnegative", "detailed_balance_pass", "refinement_pass"
    )):
        raise SystemExit("SFHo local-rate map failed acceptance")


if __name__ == "__main__":
    main()
