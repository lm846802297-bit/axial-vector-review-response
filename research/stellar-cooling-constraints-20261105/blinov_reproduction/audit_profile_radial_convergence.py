"""Radial-quadrature convergence for baseline and same-model mu_mu profile variant."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import tempfile

import numpy as np

import audit_profile_transport_sensitivity as sensitivity

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "profile_radial_convergence_8_15km_2026-11-09.json"
ORDERS = (40, 80, 120)


def evaluate_pair(profile_path: Path, variant_path: Path, radial_order: int):
    sensitivity.RADIAL_ORDER = radial_order
    baseline = sensitivity.evaluate_profile(profile_path)
    variant = sensitivity.evaluate_profile(variant_path)

    source = baseline["_source_array"]
    columns0 = baseline["_columns_array"]
    columns1 = variant["_columns_array"]
    angle_weights = baseline["_angle_weights_array"]
    radii = baseline["_radii_array"]
    weights = source[:, None, :] * angle_weights[None, :, None]
    norm = float(np.sum(weights))

    g2 = sensitivity.STRONG_ENDPOINT_G ** 2
    tau0 = np.sum(columns0, axis=(0, 1))
    tau1 = np.sum(columns1, axis=(0, 1))
    survival0 = np.exp(-np.minimum(g2 * tau0, 745.0))
    survival1 = np.exp(-np.minimum(g2 * tau1, 745.0))

    pesc0 = float(np.sum(weights * survival0) / norm)
    pesc1_fixed = float(np.sum(weights * survival1) / norm)
    variant_source = variant["_source_array"]
    variant_weights = variant_source[:, None, :] * angle_weights[None, :, None]
    variant_norm = float(np.sum(variant_weights))
    pesc1_own = float(np.sum(variant_weights * survival1) / variant_norm)

    source_shells = {}
    for name, lo, hi in (("8_10km", 8.0, 10.0),
                         ("10_12km", 10.0, 12.0),
                         ("12_15km", 12.0, 15.0)):
        mask = (radii >= lo) & (radii < hi if hi < 15.0 else radii <= hi)
        b0 = float(np.sum(source[mask]))
        b1 = float(np.sum(variant_source[mask]))
        source_shells[name] = {
            "baseline_source": b0,
            "variant_source": b1,
            "source_ratio": b1 / b0,
        }

    path_shells = {}
    for name, lo, hi in (("8_10km", 8.0, 10.0),
                         ("10_12km", 10.0, 12.0),
                         ("12_15km", 12.0, 15.0)):
        idx = int(np.where(
            (sensitivity.b16.SHELL_EDGES_KM[:-1] == lo)
            & (sensitivity.b16.SHELL_EDGES_KM[1:] == hi)
        )[0][0])
        shell0 = columns0[:, idx]
        shell1 = columns1[:, idx]
        tau_shell0 = float(np.sum(weights * np.sum(shell0, axis=0)) / norm)
        tau_shell1 = float(np.sum(weights * np.sum(shell1, axis=0)) / norm)
        path_shells[name] = {
            "baseline_mean_tau_per_g2": tau_shell0,
            "variant_mean_tau_per_g2": tau_shell1,
            "tau_ratio": tau_shell1 / tau_shell0,
        }

    return {
        "radial_order": radial_order,
        "baseline_profile_sha256": sensitivity.sha256(profile_path),
        "variant_profile_sha256": sensitivity.sha256(variant_path),
        "baseline_B1_source": norm,
        "variant_B1_source": float(np.sum(variant_weights)),
        "B1_source_ratio": float(np.sum(variant_weights) / norm),
        "baseline_Pesc": pesc0,
        "variant_Pesc_fixed_baseline_source": pesc1_fixed,
        "variant_Pesc_own_source": pesc1_own,
        "fixed_source_Pesc_ratio": pesc1_fixed / pesc0,
        "own_source_Pesc_ratio": pesc1_own / pesc0,
        "escaped_B1_integral_ratio": (
            float(np.sum(variant_weights) * pesc1_own) / (norm * pesc0)
        ),
        "source_shells": source_shells,
        "path_shells": path_shells,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="profile_radial_convergence_") as tmp:
        paths, assumptions = sensitivity.build_variants(args.profile, Path(tmp))
        variant_path = paths["B2_diagnostic_Ferreira_mu_mu_8_15km"]
        results = [
            evaluate_pair(args.profile, variant_path, order)
            for order in ORDERS
        ]

    reference = results[-1]
    for result in results:
        result["relative_to_order_120"] = {
            "baseline_Pesc": result["baseline_Pesc"] / reference["baseline_Pesc"] - 1.0,
            "fixed_source_Pesc_ratio": (
                result["fixed_source_Pesc_ratio"] / reference["fixed_source_Pesc_ratio"] - 1.0
            ),
            "B1_source_ratio": result["B1_source_ratio"] / reference["B1_source_ratio"] - 1.0,
        }

    payload = {
        "title": "Radial quadrature convergence of baseline and 8-15 km mu_mu profile diagnostic",
        "benchmark": {
            "mass_MeV": sensitivity.MASS_MEV,
            "coupling": sensitivity.STRONG_ENDPOINT_G,
            "radius_km": sensitivity.RADIUS_KM,
            "energy_order": sensitivity.ENERGY_ORDER,
            "angular_order": sensitivity.ANGULAR_ORDER,
            "path_energy_convention": "fixed omega along B.2 paths",
            "radial_orders": list(ORDERS),
        },
        "variant_definition": assumptions["B2_interpretation"],
        "results": results,
        "interpretation": [
            "Only the radial quadrature order changes between rows.",
            "The same baseline and 8-15 km Ferreira mu_mu diagnostic profiles are used at every order.",
            "This is a convergence test of a profile sensitivity, not a profile selection or a physical correction.",
            "No empirical rescaling or axial-vector update is performed.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
