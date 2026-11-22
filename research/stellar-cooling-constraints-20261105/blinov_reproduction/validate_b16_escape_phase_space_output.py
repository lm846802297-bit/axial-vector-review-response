"""Strict validation of the B.16 10 MeV escape phase-space JSON."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path


TOL = 2.0e-10
CLOSURE_TOL = 2.0e-10
ESCAPE_PROBABILITY_TOL = 2.0e-13
RATIO_CONSISTENCY_TOL = 5.0e-13
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def _reject_json_constant(value: str) -> None:
    raise ValueError(f"Non-standard non-finite JSON constant is forbidden: {value}")


def load_json(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"), parse_constant=_reject_json_constant)


def _assert_finite_tree(value, path="$") -> None:
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise AssertionError(f"Non-finite numeric value at {path}: {value!r}")
        return
    if isinstance(value, int):
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _assert_finite_tree(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            _assert_finite_tree(item, f"{path}.{key}")
        return
    raise AssertionError(f"Unsupported JSON value at {path}: {type(value).__name__}")


def _finite_number(value, path):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise AssertionError(f"{path} must be a JSON number")
    result = float(value)
    if not math.isfinite(result):
        raise AssertionError(f"{path} must be finite, got {result!r}")
    return result


def _check_sha256(value, path):
    if not isinstance(value, str) or SHA256_RE.fullmatch(value) is None:
        raise AssertionError(f"{path} must be a lowercase 64-character SHA-256")
    return value


def compare_joint_marginal(joint, partition_rows, axis, observable, tolerance=TOL):
    """Compare a joint-table marginal with a stored partition.

    The joint table intentionally stores only non-empty cells. A partition may
    therefore contain a zero-weight bin absent from the joint table. Such a
    missing bin is treated as an exact zero; missing non-zero bins and
    unexpected joint labels remain hard failures.
    """
    expected = {}
    for row in partition_rows:
        label = row["bin"]
        if label in expected:
            raise AssertionError(f"Duplicate {axis} partition label: {label}")
        expected[label] = _finite_number(row[observable], f"partition[{label}].{observable}")
        if expected[label] < 0.0:
            raise AssertionError(f"Negative partition fraction for {label}")
    actual = {}
    for cell in joint:
        label = cell[axis]
        value = _finite_number(cell[observable], f"joint[{label}].{observable}")
        if value < 0.0:
            raise AssertionError(f"Negative joint fraction for {label}")
        actual[label] = actual.get(label, 0.0) + value

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


def validate(
    data: dict,
    baseline: dict | None = None,
    baseline_sha256: str | None = None,
) -> dict:
    _assert_finite_tree(data)
    if baseline is not None:
        _assert_finite_tree(baseline, "$.baseline")
    mass = _finite_number(data["mass_MeV"], "mass_MeV")
    if mass != 10.0:
        raise AssertionError("This acceptance validator is restricted to m=10 MeV")
    coupling = _finite_number(data["coupling"], "coupling")
    luminosity = _finite_number(data["calculated_luminosity_erg_s"], "calculated_luminosity_erg_s")
    reference_luminosity = _finite_number(data["reference_luminosity_erg_s"], "reference_luminosity_erg_s")
    thin_luminosity = _finite_number(data["optically_thin_luminosity_erg_s"], "optically_thin_luminosity_erg_s")
    reported_fig7 = _finite_number(data["relative_difference_vs_fig7"], "relative_difference_vs_fig7")
    escape_probability = _finite_number(data["escape_probability"], "escape_probability")
    if coupling <= 0 or min(luminosity, reference_luminosity, thin_luminosity) <= 0:
        raise AssertionError("Coupling and all luminosities must be positive")
    if not 0.0 <= escape_probability <= 1.0:
        raise AssertionError("escape_probability must lie in [0, 1]")
    expected_fig7 = luminosity / reference_luminosity - 1.0
    if not math.isclose(reported_fig7, expected_fig7, rel_tol=RATIO_CONSISTENCY_TOL, abs_tol=RATIO_CONSISTENCY_TOL):
        raise AssertionError("relative_difference_vs_fig7 is inconsistent with calculated/reference luminosities")
    expected_escape = luminosity / thin_luminosity
    if not math.isclose(escape_probability, expected_escape, rel_tol=RATIO_CONSISTENCY_TOL, abs_tol=ESCAPE_PROBABILITY_TOL):
        raise AssertionError("escape_probability is inconsistent with calculated/optically-thin luminosity")
    for key in ("baseline_json_sha256", "fig7_reference_sha256"):
        if key in data:
            _check_sha256(data[key], key)
    _check_sha256(data["profile"]["sha256"], "profile.sha256")

    closure = data["closure"]
    for key in (
        "luminosity_relative_residual_vs_high_order_baseline",
        "thin_luminosity_relative_residual_vs_high_order_baseline",
    ):
        residual = _finite_number(closure[key], f"closure.{key}")
        if abs(residual) >= CLOSURE_TOL:
            raise AssertionError(f"{key} exceeds {CLOSURE_TOL:g}: {residual}")
    if abs(_finite_number(closure["escape_probability_absolute_residual_vs_high_order_baseline"], "closure.escape_probability_absolute_residual_vs_high_order_baseline")) >= ESCAPE_PROBABILITY_TOL:
        raise AssertionError("Escape-probability closure exceeds 2e-13")

    config = data["configuration"]
    if abs(_finite_number(config["direction_weight_sum"], "configuration.direction_weight_sum") - 1.0) >= 1.0e-14:
        raise AssertionError("Direction quadrature weights do not sum to one")
    if abs(_finite_number(config["direction_weight_closure_residual"], "configuration.direction_weight_closure_residual")) >= 1.0e-15:
        raise AssertionError("Direction quadrature weights do not reproduce the B.2 Gauss rule")

    for key in ("source_grid_sha256", "opacity_grid_sha256", "energy_grid_sha256"):
        _check_sha256(config[key], f"configuration.{key}")
    for key in ("source_radial_node_count", "opacity_radial_node_count", "energy_node_count"):
        if isinstance(config[key], bool) or not isinstance(config[key], int) or config[key] <= 0:
            raise AssertionError(f"configuration.{key} must be a positive integer")

    if baseline is not None:
        expected_baseline_sha256 = _check_sha256(
            data["baseline_json_sha256"], "baseline_json_sha256"
        )
        if baseline_sha256 is not None and expected_baseline_sha256 != baseline_sha256:
            raise AssertionError("baseline_json_sha256 does not match the supplied baseline file")

        baseline_result = baseline.get("result", baseline)
        expected = baseline_result["configuration"]
        for key in ("source_grid_sha256", "opacity_grid_sha256", "energy_grid_sha256"):
            if config[key] != expected[key]:
                raise AssertionError(f"{key} differs from the archived high-order baseline")
        if data["profile"]["sha256"] != baseline_result["profile"]["sha256"]:
            raise AssertionError("Profile fingerprint differs from the archived high-order baseline")

        baseline_mass = _finite_number(baseline_result["mass_MeV"], "baseline.mass_MeV")
        if baseline_mass != mass:
            raise AssertionError("Mass differs from the archived high-order baseline")
        baseline_points = baseline_result["eq_b2_fixed_omega_baseline"]["points"]
        matching_points = [
            point for point in baseline_points
            if math.isclose(
                _finite_number(point["g"], "baseline.eq_b2_fixed_omega_baseline.points.g"),
                coupling,
                rel_tol=1.0e-13,
                abs_tol=0.0,
            )
        ]
        if len(matching_points) != 1:
            raise AssertionError(
                "Expected exactly one archived high-order baseline point at the requested coupling"
            )
        baseline_point = matching_points[0]
        baseline_luminosity = _finite_number(
            baseline_point["calculated_luminosity_erg_s"],
            "baseline.calculated_luminosity_erg_s",
        )
        baseline_thin_luminosity = _finite_number(
            baseline_point["optically_thin_luminosity_erg_s"],
            "baseline.optically_thin_luminosity_erg_s",
        )
        baseline_escape_probability = _finite_number(
            baseline_point["escape_fraction"], "baseline.escape_fraction"
        )
        baseline_reference_luminosity = _finite_number(
            baseline_point["reference_luminosity_erg_s"],
            "baseline.reference_luminosity_erg_s",
        )
        if not math.isclose(
            reference_luminosity,
            baseline_reference_luminosity,
            rel_tol=RATIO_CONSISTENCY_TOL,
            abs_tol=0.0,
        ):
            raise AssertionError("Fig. 7 reference luminosity differs from the archived high-order baseline")

        computed_baseline_residuals = {
            "luminosity_relative_residual_vs_high_order_baseline": (
                luminosity / baseline_luminosity - 1.0,
                CLOSURE_TOL,
            ),
            "thin_luminosity_relative_residual_vs_high_order_baseline": (
                thin_luminosity / baseline_thin_luminosity - 1.0,
                CLOSURE_TOL,
            ),
            "escape_probability_absolute_residual_vs_high_order_baseline": (
                escape_probability - baseline_escape_probability,
                ESCAPE_PROBABILITY_TOL,
            ),
        }
        for key, (computed_residual, tolerance) in computed_baseline_residuals.items():
            stored_residual = _finite_number(closure[key], f"closure.{key}")
            if not math.isclose(
                stored_residual, computed_residual, rel_tol=1.0e-12, abs_tol=1.0e-15
            ):
                raise AssertionError(f"{key} is inconsistent with the archived high-order baseline")
            if abs(computed_residual) >= tolerance:
                raise AssertionError(f"{key} exceeds the baseline closure tolerance: {computed_residual}")

    required_regions = {"all_emission_radii", "dominant_8_15km_emission"}
    region_names = [region["region"] for region in data["regions"]]
    if len(region_names) != len(set(region_names)):
        raise AssertionError("Duplicate region names in phase-space result")
    if set(region_names) != required_regions:
        raise AssertionError(
            "Phase-space result must contain exactly all_emission_radii and dominant_8_15km_emission"
        )

    region_reports = []
    for region in data["regions"]:
        name = region["region"]
        for key in ("source_fraction_of_global_B1", "escaped_luminosity_fraction_of_global", "source_weighted_escape_probability"):
            value = _finite_number(region[key], f"{name}.{key}")
            if not 0.0 <= value <= 1.0:
                raise AssertionError(f"{name}.{key} must lie in [0, 1]")
        for field in (
            "emission_radius_bins",
            "energy_bins",
            "direction_bins_4",
            "direction_bins_8",
        ):
            rows = region[field]
            thin_values = [_finite_number(x["thin_source_fraction_within_region"], f"{name}.{field}.thin") for x in rows]
            escaped_values = [_finite_number(x["escaped_luminosity_fraction_within_region"], f"{name}.{field}.escaped") for x in rows]
            if any(x < 0.0 for x in thin_values + escaped_values):
                raise AssertionError(f"{name} {field} contains a negative partition fraction")
            thin_sum = sum(thin_values)
            escaped_sum = sum(escaped_values)
            if abs(thin_sum - 1.0) >= TOL:
                raise AssertionError(f"{name} {field} thin partition does not close: {thin_sum:.17g}")
            if abs(escaped_sum - 1.0) >= TOL:
                raise AssertionError(f"{name} {field} escaped partition does not close: {escaped_sum:.17g}")

        joint = region["joint_radius_energy_direction_bins"]
        if not joint:
            raise AssertionError(f"{name} has an empty joint table")
        joint_count = region.get("joint_bin_count_nonempty")
        if isinstance(joint_count, bool) or not isinstance(joint_count, int) or joint_count != len(joint):
            raise AssertionError(f"{name} joint_bin_count_nonempty must be an integer matching the table")
        for cell in joint:
            for key in (
                "thin_source_fraction_within_region",
                "escaped_luminosity_fraction_within_region",
                "thin_source_fraction_of_global",
                "escaped_luminosity_fraction_of_global",
            ):
                value = _finite_number(cell[key], f"{name}.joint.{key}")
                if value < 0.0:
                    raise AssertionError(f"{name} has a negative joint-table fraction: {key}")

        cell_ids = [
            (cell["emission_shell"], cell["energy_bin"], cell["direction_bin"])
            for cell in joint
        ]
        if len(cell_ids) != len(set(cell_ids)):
            raise AssertionError(f"{name} contains duplicate radius-energy-direction cells")

        joint_thin = sum(
            _finite_number(x["thin_source_fraction_within_region"], f"{name}.joint.thin")
            for x in joint
        )
        joint_escaped = sum(
            _finite_number(x["escaped_luminosity_fraction_within_region"], f"{name}.joint.escaped")
            for x in joint
        )
        if abs(joint_thin - 1.0) >= TOL:
            raise AssertionError(f"{name} joint thin partition does not close: {joint_thin:.17g}")
        if abs(joint_escaped - 1.0) >= TOL:
            raise AssertionError(f"{name} joint escaped partition does not close: {joint_escaped:.17g}")

        joint_thin_global = sum(
            _finite_number(x["thin_source_fraction_of_global"], f"{name}.joint.thin_global")
            for x in joint
        )
        joint_escaped_global = sum(
            _finite_number(x["escaped_luminosity_fraction_of_global"], f"{name}.joint.escaped_global")
            for x in joint
        )
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
    parser.add_argument("--no-baseline", action="store_true", help="Skip baseline fingerprint comparison")
    parser.add_argument(
        "--baseline",
        type=Path,
        default=here / "outputs" / "b16_global_high_order_independent_grid_10mev_2026-11-09.json",
    )
    args = parser.parse_args()
    data = load_json(args.result)
    baseline = None if args.no_baseline else load_json(args.baseline)
    baseline_sha256 = (
        None if args.no_baseline else hashlib.sha256(args.baseline.read_bytes()).hexdigest()
    )
    report = validate(data, baseline, baseline_sha256)
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
