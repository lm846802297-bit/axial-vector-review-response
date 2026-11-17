"""Strict validation of the B.16 10 MeV escape phase-space JSON."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


TOL = 2.0e-10
CLOSURE_TOL = 2.0e-10
ESCAPE_PROBABILITY_TOL = 2.0e-13


def compare_joint_marginal(joint, partition_rows, axis, observable, tolerance=TOL):
    """Compare a joint-table marginal with a stored partition.

    The joint table intentionally stores only non-empty cells. A partition may
    therefore contain a zero-weight bin absent from the joint table. Such a
    missing bin is treated as an exact zero; missing non-zero bins and
    unexpected joint labels remain hard failures.
    """
    expected = {row["bin"]: float(row[observable]) for row in partition_rows}
    actual = {}
    for cell in joint:
        label = cell[axis]
        actual[label] = actual.get(label, 0.0) + float(cell[observable])

    unexpected = sorted(set(actual) - set(expected))
    if unexpected:
        raise AssertionError(f"Unexpected {axis} labels in joint table: {unexpected}")

    missing_zero_bins = []
    residuals = {}
    for label, expected_value in expected.items():
        actual_value = actual.get(label, 0.0)
        if label not in actual and expected_value == 0.0:
            missing_zero_bins.append(label)
        residual = abs(actual_value - expected_value)
        residuals[label] = residual
        if residual > tolerance:
            raise AssertionError(
                f"{axis} marginal mismatch for {label}: "
                f"joint={actual_value:.17g}, partition={expected_value:.17g}, "
                f"residual={residual:.3e}"
            )

    return {
        "max_absolute_residual": max(residuals.values(), default=0.0),
        "missing_zero_bins_omitted_from_joint": missing_zero_bins,
        "bin_count": len(expected),
    }


def validate(data: dict, baseline: dict | None = None) -> dict:
    if float(data["mass_MeV"]) != 10.0:
        raise AssertionError("This acceptance validator is restricted to m=10 MeV")

    closure = data["closure"]
    for key in (
        "luminosity_relative_residual_vs_high_order_baseline",
        "thin_luminosity_relative_residual_vs_high_order_baseline",
    ):
        if abs(float(closure[key])) >= CLOSURE_TOL:
            raise AssertionError(f"{key} exceeds {CLOSURE_TOL:g}: {closure[key]}")
    if abs(float(closure["escape_probability_absolute_residual_vs_high_order_baseline"])) >= ESCAPE_PROBABILITY_TOL:
        raise AssertionError("Escape-probability closure exceeds 2e-13")

    config = data["configuration"]
    if abs(float(config["direction_weight_sum"]) - 1.0) >= 1.0e-14:
        raise AssertionError("Direction quadrature weights do not sum to one")
    if abs(float(config["direction_weight_closure_residual"])) >= 1.0e-15:
        raise AssertionError("Direction quadrature weights do not reproduce the B.2 Gauss rule")

    if baseline is not None:
        baseline_result = baseline["result"]
        expected = baseline_result["configuration"]
        for key in ("source_grid_sha256", "opacity_grid_sha256", "energy_grid_sha256"):
            if config[key] != expected[key]:
                raise AssertionError(f"{key} differs from the archived high-order baseline")
        if data["profile"]["sha256"] != baseline_result["profile"]["sha256"]:
            raise AssertionError("Profile fingerprint differs from the archived high-order baseline")

    region_reports = []
    for region in data["regions"]:
        name = region["region"]
        for field in (
            "emission_radius_bins",
            "energy_bins",
            "direction_bins_4",
            "direction_bins_8",
        ):
            rows = region[field]
            thin_sum = sum(float(x["thin_source_fraction_within_region"]) for x in rows)
            escaped_sum = sum(float(x["escaped_luminosity_fraction_within_region"]) for x in rows)
            if abs(thin_sum - 1.0) >= TOL:
                raise AssertionError(f"{name} {field} thin partition does not close: {thin_sum:.17g}")
            if abs(escaped_sum - 1.0) >= TOL:
                raise AssertionError(f"{name} {field} escaped partition does not close: {escaped_sum:.17g}")

        joint = region["joint_radius_energy_direction_bins"]
        if not joint:
            raise AssertionError(f"{name} has an empty joint table")
        if region.get("joint_bin_count_nonempty") != len(joint):
            raise AssertionError(f"{name} joint_bin_count_nonempty does not match the table")
        for cell in joint:
            for key in (
                "thin_source_fraction_within_region",
                "escaped_luminosity_fraction_within_region",
                "thin_source_fraction_of_global",
                "escaped_luminosity_fraction_of_global",
            ):
                if float(cell[key]) < 0.0:
                    raise AssertionError(f"{name} has a negative joint-table fraction: {key}")

        cell_ids = [
            (cell["emission_shell"], cell["energy_bin"], cell["direction_bin"])
            for cell in joint
        ]
        if len(cell_ids) != len(set(cell_ids)):
            raise AssertionError(f"{name} contains duplicate radius-energy-direction cells")

        joint_thin = sum(float(x["thin_source_fraction_within_region"]) for x in joint)
        joint_escaped = sum(float(x["escaped_luminosity_fraction_within_region"]) for x in joint)
        if abs(joint_thin - 1.0) >= TOL:
            raise AssertionError(f"{name} joint thin partition does not close: {joint_thin:.17g}")
        if abs(joint_escaped - 1.0) >= TOL:
            raise AssertionError(f"{name} joint escaped partition does not close: {joint_escaped:.17g}")

        joint_thin_global = sum(float(x["thin_source_fraction_of_global"]) for x in joint)
        joint_escaped_global = sum(float(x["escaped_luminosity_fraction_of_global"]) for x in joint)
        if abs(joint_thin_global - float(region["source_fraction_of_global_B1"])) >= TOL:
            raise AssertionError(f"{name} joint table does not reproduce its global source fraction")
        if abs(joint_escaped_global - float(region["escaped_luminosity_fraction_of_global"])) >= TOL:
            raise AssertionError(f"{name} joint table does not reproduce its global escaped fraction")

        marginal_reports = {}
        for axis, field in (
            ("emission_shell", "emission_radius_bins"),
            ("energy_bin", "energy_bins"),
            ("direction_bin", "direction_bins_4"),
        ):
            marginal_reports[axis] = {}
            for observable in (
                "thin_source_fraction_within_region",
                "escaped_luminosity_fraction_within_region",
            ):
                marginal_reports[axis][observable] = compare_joint_marginal(
                    joint, region[field], axis, observable
                )

        region_reports.append({
            "region": name,
            "source_fraction_of_global_B1": float(region["source_fraction_of_global_B1"]),
            "escaped_luminosity_fraction_of_global": float(region["escaped_luminosity_fraction_of_global"]),
            "source_weighted_escape_probability": float(region["source_weighted_escape_probability"]),
            "joint_bin_count_nonempty": len(joint),
            "joint_thin_sum": joint_thin,
            "joint_escaped_sum": joint_escaped,
            "marginal_checks": marginal_reports,
        })

    core = next(
        (x for x in data["regions"] if x["region"] == "dominant_8_15km_emission"),
        None,
    )
    if core is None:
        raise AssertionError("Missing dominant_8_15km_emission region")
    if not 0.75 < float(core["source_fraction_of_global_B1"]) < 0.85:
        raise AssertionError("The 8--15 km source fraction is outside the accepted 75--85% interval")

    return {
        "status": "PASS",
        "mass_MeV": 10.0,
        "coupling": float(data["coupling"]),
        "calculated_luminosity_erg_s": float(data["calculated_luminosity_erg_s"]),
        "reference_luminosity_erg_s": float(data["reference_luminosity_erg_s"]),
        "relative_difference_vs_fig7": float(data["relative_difference_vs_fig7"]),
        "escape_probability": float(data["escape_probability"]),
        "closure": closure,
        "grid_identity": {
            key: config[key]
            for key in (
                "source_radial_node_count", "source_grid_sha256",
                "opacity_radial_node_count", "opacity_grid_sha256",
                "energy_node_count", "energy_grid_sha256",
            )
        },
        "regions": region_reports,
        "acceptance_tolerances": {
            "luminosity_and_partition_relative": CLOSURE_TOL,
            "escape_probability_absolute": ESCAPE_PROBABILITY_TOL,
            "direction_weight_absolute": 1.0e-14,
            "joint_marginal_absolute": TOL,
        },
    }


def main() -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path)
    parser.add_argument(
        "--baseline",
        type=Path,
        default=here / "outputs" / "b16_global_high_order_independent_grid_10mev_2026-11-09.json",
    )
    args = parser.parse_args()
    data = json.loads(args.result.read_text(encoding="utf-8"))
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    report = validate(data, baseline)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
