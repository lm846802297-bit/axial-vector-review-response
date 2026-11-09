#!/usr/bin/env python3
"""Isolate B.2 radial opacity-interpolation convergence from B.1 source quadrature."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from blinov_reproduction.reference import (
    DEFAULT_PROFILE, radial_rule, load_profile, local_rates, scalar_optical_depths,
)
from blinov_reproduction.audit_b16_global_redshift import (
    DEFAULT_FIG7, eq_b1_source_measure, redshifted_scalar_optical_depths,
)

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "outputs" / "b2_opacity_interpolation_convergence_2026-11-09.json"
DEFAULT_REPORT = HERE / "B2_OPACITY_INTERPOLATION_CONVERGENCE_2026-11-09.md"
PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
OPACITY_ORDERS = (40, 80, 120, 160, 240, 320, 480, 640)
SOURCE_RADIAL_ORDER = 40
ENERGY_ORDER = 100
ANGULAR_ORDER = 16
PATH_ORDER = 32
RADIUS_KM = 25.0
ENERGY_OFFSET_MEV = 1000.0


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run_case(mass: float, opacity_order: int, profile_path: Path, fig7_path: Path) -> dict:
    # Keep the source quadrature nodes fixed; independently refine the radial
    # table used to interpolate absorption rates along each propagation chord.
    source_r, source_rw = radial_rule(RADIUS_KM, SOURCE_RADIAL_ORDER)
    opacity_r, _ = radial_rule(RADIUS_KM, opacity_order)
    radial_grid = np.unique(np.r_[0.0, source_r, opacity_r, RADIUS_KM])
    profile = load_profile(profile_path, radial_grid)
    source_index = np.searchsorted(radial_grid, source_r)
    lapse_source = profile["lapse"][source_index]

    # The B.1 threshold nodes are defined at emission radii only.
    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), ENERGY_OFFSET_MEV, ENERGY_ORDER
    )
    energies = np.unique(np.r_[energies, mass / lapse_source])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()

    rates = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None],
    )
    fixed_columns, angle_weights = scalar_optical_depths(
        source_r, radial_grid, rates["reduced_absorption"], mass, energies,
        RADIUS_KM, ANGULAR_ORDER, PATH_ORDER,
    )
    redshift_columns, redshift_angles, kinematics = redshifted_scalar_optical_depths(
        source_r, radial_grid, profile, mass, energies,
        RADIUS_KM, ANGULAR_ORDER, PATH_ORDER,
    )
    angle_residual = float(np.max(np.abs(angle_weights - redshift_angles)))
    if angle_residual > 1.0e-14:
        raise ArithmeticError("Fixed and redshifted angular weights differ")

    source, _ = eq_b1_source_measure(
        source_r, source_rw, energies, lapse_source, mass,
        rates["production"][source_index],
    )
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
    couplings = np.asarray(vertices["g"], float)
    reference = np.asarray(vertices["luminosity_erg_s"], float)

    thin, fixed, redshifted, fixed_escape, redshift_escape = [], [], [], [], []
    for coupling in couplings:
        avg_fixed = np.einsum(
            "rae,a->re", np.exp(-coupling**2 * fixed_columns), angle_weights
        )
        avg_redshift = np.einsum(
            "rae,a->re", np.exp(-coupling**2 * redshift_columns), angle_weights
        )
        lthin = float(coupling**2 * np.sum(source))
        lfixed = float(coupling**2 * np.sum(source * avg_fixed))
        lred = float(coupling**2 * np.sum(source * avg_redshift))
        thin.append(lthin)
        fixed.append(lfixed)
        redshifted.append(lred)
        fixed_escape.append(lfixed / lthin if lthin else 0.0)
        redshift_escape.append(lred / lthin if lthin else 0.0)

    fixed = np.asarray(fixed, float)
    redshifted = np.asarray(redshifted, float)
    delta = redshifted / fixed - 1.0
    peak = int(np.argmax(reference))
    return {
        "mass_MeV": float(mass),
        "configuration": {
            "source_radial_order": SOURCE_RADIAL_ORDER,
            "opacity_interpolation_order": int(opacity_order),
            "opacity_grid_node_count_before_union": int(len(opacity_r)),
            "combined_radial_grid_node_count": int(len(radial_grid)),
            "energy_order": ENERGY_ORDER,
            "actual_energy_node_count": int(len(energies)),
            "angular_order": ANGULAR_ORDER,
            "path_order": PATH_ORDER,
            "radius_km": RADIUS_KM,
            "energy_offset_MeV": ENERGY_OFFSET_MEV,
        },
        "profile_sha256": sha256(profile_path),
        "fig7_pdf_sha256": fig7.get("pdf_sha256"),
        "B1_source": {
            "thin_luminosity_erg_s_per_g2": float(np.sum(source)),
            "mean_emission_radius_km": float(
                np.sum(source_r * np.sum(source, axis=1)) / np.sum(source)
            ),
            "radial_source_weights": (np.sum(source, axis=1) / np.sum(source)).tolist(),
        },
        "kinematics": kinematics,
        "angle_weight_residual": angle_residual,
        "fixed_luminosity_erg_s": fixed.tolist(),
        "redshifted_luminosity_erg_s": redshifted.tolist(),
        "thin_luminosity_erg_s": np.asarray(thin, float).tolist(),
        "fixed_escape_fraction": np.asarray(fixed_escape, float).tolist(),
        "redshifted_escape_fraction": np.asarray(redshift_escape, float).tolist(),
        "couplings_g": couplings.tolist(),
        "reference_luminosity_erg_s": reference.tolist(),
        "redshift_shift_vs_fixed": {
            "mean_absolute_relative_shift": float(np.mean(np.abs(delta))),
            "maximum_absolute_relative_shift": float(np.max(np.abs(delta))),
            "weak_endpoint_relative_shift": float(delta[0]),
            "reference_peak_relative_shift": float(delta[peak]),
            "strong_endpoint_relative_shift": float(delta[-1]),
            "relative_shift_by_coupling": delta.tolist(),
        },
    }


def compare_pair(coarse: dict, fine: dict) -> dict:
    if coarse["couplings_g"] != fine["couplings_g"]:
        raise ValueError("Coupling grids differ")
    fields = {
        "thin_source": "thin_luminosity_erg_s",
        "fixed_omega_luminosity": "fixed_luminosity_erg_s",
        "path_redshift_luminosity": "redshifted_luminosity_erg_s",
        "fixed_escape": "fixed_escape_fraction",
        "redshifted_escape": "redshifted_escape_fraction",
    }
    peak = int(np.argmax(np.asarray(coarse["reference_luminosity_erg_s"], float)))
    out = {}
    for label, field in fields.items():
        a, b = np.asarray(coarse[field], float), np.asarray(fine[field], float)
        rel = b / a - 1.0
        out[label] = {
            "maximum_absolute_relative_change": float(np.max(np.abs(rel))),
            "mean_absolute_relative_change": float(np.mean(np.abs(rel))),
            "weak_endpoint_relative_change": float(rel[0]),
            "reference_peak_relative_change": float(rel[peak]),
            "strong_endpoint_relative_change": float(rel[-1]),
        }
    d0 = np.asarray(coarse["redshift_shift_vs_fixed"]["relative_shift_by_coupling"], float)
    d1 = np.asarray(fine["redshift_shift_vs_fixed"]["relative_shift_by_coupling"], float)
    dd = d1 - d0
    out["redshift_effect_absolute_change"] = {
        "maximum_percentage_point_change": float(100.0 * np.max(np.abs(dd))),
        "mean_percentage_point_change": float(100.0 * np.mean(np.abs(dd))),
        "reference_peak_percentage_point_change": float(100.0 * dd[peak]),
        "strong_endpoint_percentage_point_change": float(100.0 * dd[-1]),
    }
    return out


def run_mass(mass: float, profile_path: Path, fig7_path: Path) -> dict:
    cases = {
        str(order): run_case(mass, order, profile_path, fig7_path)
        for order in OPACITY_ORDERS
    }
    comparisons = {
        f"opacity_{a}_to_{b}": compare_pair(cases[str(a)], cases[str(b)])
        for a, b in zip(OPACITY_ORDERS[:-1], OPACITY_ORDERS[1:])
    }
    acceptance = {}
    for label, item in comparisons.items():
        source_ok = item["thin_source"]["maximum_absolute_relative_change"] < 1.0e-10
        fixed_ok = item["fixed_omega_luminosity"]["maximum_absolute_relative_change"] < 0.01
        redshift_ok = item["path_redshift_luminosity"]["maximum_absolute_relative_change"] < 0.01
        delta_ok = item["redshift_effect_absolute_change"]["maximum_percentage_point_change"] < 0.5
        acceptance[label] = {
            "B1_source_unchanged_to_roundoff": source_ok,
            "fixed_luminosity_max_change_below_1pct": fixed_ok,
            "redshifted_luminosity_max_change_below_1pct": redshift_ok,
            "redshift_effect_change_below_0p5_percentage_point": delta_ok,
            "passed": source_ok and fixed_ok and redshift_ok and delta_ok,
        }
    finest_pairs = ("opacity_320_to_480", "opacity_480_to_640")
    finest_two_passed = all(acceptance[name]["passed"] for name in finest_pairs)
    coarse_grid_pairs_failed = [
        name for name, item in acceptance.items()
        if not item["passed"] and name not in finest_pairs
    ]
    return {
        "mass_MeV": float(mass),
        "profile_sha256": sha256(profile_path),
        "fixed_quadratures": {
            "source_radial_order": SOURCE_RADIAL_ORDER,
            "energy_order": ENERGY_ORDER,
            "angular_order": ANGULAR_ORDER,
            "path_order": PATH_ORDER,
        },
        "opacity_grid_orders": list(OPACITY_ORDERS),
        "configurations": cases,
        "pairwise_convergence": comparisons,
        "acceptance": acceptance,
        "coarse_grid_pairs_failed": coarse_grid_pairs_failed,
        "finest_two_pair_convergence_passed": finest_two_passed,
        "overall_passed": finest_two_passed,
        "interpretation": (
            "The B.1 source radial rule is fixed at order 40 in every case. "
            "Only the radial interpolation grid used by the B.2 path-opacity "
            "integral is refined; energy, angle, and path quadratures are fixed. "
            "Coarse-grid failures are recorded but do not invalidate convergence "
            "once the final two successive refinements pass."
        ),
    }


def write_report(payload: dict, path: Path) -> None:
    lines = [
        "# B.2 radial opacity-interpolation convergence audit",
        "",
        "## Scope",
        "",
        "The B.1 source radial quadrature is fixed at order 40. The energy, angular, "
        "and path quadratures are also fixed. Only the radial grid used to tabulate "
        "and interpolate local absorption rates along the B.2 chord is refined.",
        "",
        "The fixed-omega prescription follows the printed Eq. (B.2). The redshifted "
        "variant uses conserved energy at infinity, "
        "$E_\\infty=N(r)\\omega_{\\rm source}$ and "
        "$\\omega_{\\rm local}(s)=E_\\infty/N(r'(s))$, while retaining the same "
        "Euclidean chord. It is a sensitivity diagnostic, not full GR ray tracing.",
        "",
        "## Results",
        "",
        "| $m_V$ (MeV) | opacity grid | max fixed-$\\omega$ luminosity change | max redshifted luminosity change | max redshift-effect change |",
        "|---:|---:|---:|---:|---:|",
    ]
    for result in payload["results"]:
        for pair, item in result["pairwise_convergence"].items():
            fixed = 100.0 * item["fixed_omega_luminosity"]["maximum_absolute_relative_change"]
            red = 100.0 * item["path_redshift_luminosity"]["maximum_absolute_relative_change"]
            delta = item["redshift_effect_absolute_change"]["maximum_percentage_point_change"]
            lines.append(
                f"| {result['mass_MeV']:g} | {pair.replace('opacity_', '').replace('_to_', ' → ')} | "
                f"{fixed:.4f}% | {red:.4f}% | {delta:.4f} pp |"
            )
    lines += [
        "",
        "## Interpretation",
        "",
        "The source quadrature and energy grid are held fixed, so luminosity changes "
        "across this scan isolate the radial tabulation/interpolation of the B.2 "
        "absorption kernel. The numerical thresholds are project diagnostics, not "
        "physical uncertainty bounds.",
        "",
        "Machine-readable output: outputs/b2_opacity_interpolation_convergence_2026-11-09.json",
        "Profile SHA-256: " + payload["profile_sha256"],
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--masses", default="0.1,1,10")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    if sha256(args.profile) != PROFILE_SHA256:
        raise RuntimeError("Unexpected SFHo-18.8 reconstructed-profile fingerprint")
    results = [
        run_mass(float(token.strip()), args.profile, args.fig7)
        for token in args.masses.split(",") if token.strip()
    ]
    payload = {
        "title": "B.2 opacity interpolation convergence with fixed B.1 source quadrature",
        "date": "2026-11-09",
        "profile_sha256": sha256(args.profile),
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.report.parent.mkdir(parents=True, exist_ok=True)
    write_report(payload, args.report)
    print(json.dumps({
        "output": str(args.output),
        "report": str(args.report),
        "results": {
            str(x["mass_MeV"]): {
                "overall_passed": x["overall_passed"],
                "acceptance": x["acceptance"],
            } for x in results
        },
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
