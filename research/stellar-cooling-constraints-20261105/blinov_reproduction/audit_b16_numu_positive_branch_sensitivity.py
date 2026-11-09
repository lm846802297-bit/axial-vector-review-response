#!/usr/bin/env python3
"""Isolate the positive muon-neutrino chemical-potential branch in B.1/B.2.

Only the Caputo Fig. 1 positive mu_numu branch (16.5881801203445--18.4229995917391 km)
is varied. All other profile columns, the fixed-omega B.2 prescription, quadrature,
and Fig. 7 reference are unchanged. The 0 and +/-10% cases are stress tests, not
statistical uncertainty intervals or proposed physical corrections.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import tempfile
from pathlib import Path

try:
    from .audit_b16_emission_radius_escape import run_audit, DEFAULT_PROFILE, DEFAULT_FIG7
except ImportError:
    from audit_b16_emission_radius_escape import run_audit, DEFAULT_PROFILE, DEFAULT_FIG7

HERE = Path(__file__).resolve().parent
R_MIN = 16.5881801203445
R_MAX = 18.4229995917391
SCALES = (0.0, 0.9, 1.0, 1.1)
POINT_LABELS = {"weak_endpoint": 0, "fig7_peak": 17, "strong_endpoint": 24}
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def transform_profile(source: Path, destination: Path, scale: float) -> dict:
    with source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        if not fields or "mu_numu_MeV" not in fields or "r_km" not in fields:
            raise ValueError("Profile must contain r_km and mu_numu_MeV")
        rows = list(reader)

    selected = []
    original = []
    for row in rows:
        radius = float(row["r_km"])
        value = float(row["mu_numu_MeV"])
        if R_MIN <= radius <= R_MAX:
            selected.append(radius)
            original.append(value)
            row["mu_numu_MeV"] = format(scale * value, ".15g")

    if len(selected) < 2 or abs(selected[0] - R_MIN) > 2e-6 or abs(selected[-1] - R_MAX) > 2e-6:
        raise RuntimeError(
            f"Positive-branch support mismatch: {selected[0] if selected else None}, "
            f"{selected[-1] if selected else None}, n={len(selected)}"
        )
    if min(original) < 0.999 or max(original) > 1.81:
        raise RuntimeError("Positive-branch values fall outside the expected digitized range")

    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    # Verify that every field other than mu_numu_MeV is unchanged and that
    # mu_numu_MeV outside the selected support is unchanged.
    with destination.open(newline="", encoding="utf-8") as handle:
        changed = list(csv.DictReader(handle))
    for before, after in zip(rows, changed):
        if before["r_km"] != after["r_km"]:
            raise AssertionError("Radial grid changed during profile transformation")
    return {
        "support_km": [R_MIN, R_MAX],
        "support_node_count": len(selected),
        "original_mu_numu_range_MeV": [min(original), max(original)],
        "scale": scale,
    }


def point_summary(point: dict) -> dict:
    thin = float(point["optically_thin_luminosity_erg_s"])
    escaped = float(point["calculated_luminosity_erg_s"])
    reference = float(point["reference_luminosity_erg_s"])
    p_escape = float(point["global_escape_fraction"])
    required = reference / thin if thin > 0 else None
    return {
        "index": int(point["index"]),
        "g": float(point["g"]),
        "L_thin_erg_s": thin,
        "P_escape": p_escape,
        "L_escaped_erg_s": escaped,
        "L_Fig7_erg_s": reference,
        "relative_difference_vs_Fig7": escaped / reference - 1.0,
        "required_over_calculated_escape": required / p_escape if p_escape > 0 else None,
        "thin_source_channel_fractions": {
            name: float(channel["fraction_of_total_thin_source"])
            for name, channel in point["source_channels"].items()
        },
    }


def run(profile_path=DEFAULT_PROFILE, fig7_path=DEFAULT_FIG7, mass=10.0,
        nr=40, ne=100, na=16, ns=32, radius=25.0, energy_offset=1000.0):
    profile_hash = sha256(profile_path)
    if profile_hash != EXPECTED_PROFILE_SHA256:
        raise RuntimeError(
            f"Unexpected profile SHA256: {profile_hash}; expected {EXPECTED_PROFILE_SHA256}"
        )

    scenarios = {}
    with tempfile.TemporaryDirectory(prefix="b16_numu_positive_branch_") as tmp:
        tmp = Path(tmp)
        for scale in SCALES:
            scaled = tmp / f"profile_positive_numu_scale_{scale:g}.csv"
            transform = transform_profile(profile_path, scaled, scale)
            result = run_audit(
                scaled, fig7_path, mass, nr, ne, na, ns, radius, energy_offset
            )
            by_index = {int(point["index"]): point for point in result["representative_couplings"]}
            scenarios[f"positive_branch_scale_{scale:g}"] = {
                "profile_transform": transform,
                "points": {
                    label: point_summary(by_index[index])
                    for label, index in POINT_LABELS.items()
                },
                "internal_closure": result["internal_closure"],
            }

    baseline = scenarios["positive_branch_scale_1"]
    comparisons = {}
    for name, scenario in scenarios.items():
        if name == "positive_branch_scale_1":
            continue
        comparisons[name] = {}
        for label, point in scenario["points"].items():
            base = baseline["points"][label]
            comparisons[name][label] = {
                "thin_source_ratio_vs_baseline": point["L_thin_erg_s"] / base["L_thin_erg_s"],
                "escape_probability_ratio_vs_baseline": point["P_escape"] / base["P_escape"],
                "escaped_luminosity_ratio_vs_baseline": point["L_escaped_erg_s"] / base["L_escaped_erg_s"],
                "Fig7_relative_difference_shift": (
                    point["relative_difference_vs_Fig7"] - base["relative_difference_vs_Fig7"]
                ),
            }

    return {
        "title": "B.16 sensitivity to the positive muon-neutrino chemical-potential branch",
        "mass_MeV": mass,
        "profile_sha256": profile_hash,
        "fig7_reference_sha256": sha256(fig7_path),
        "positive_branch_support_km": [R_MIN, R_MAX],
        "scope": [
            "Only mu_numu within the digitized positive branch is varied.",
            "T, mu_mu, lapse, mu_numu outside the positive branch, radial grid, and all other inputs are unchanged.",
            "Each scenario is recomputed self-consistently in the B.1 source and B.2 opacity.",
            "The fixed-omega B.2 convention and original Fig. 7 reference are unchanged.",
            "Scale 0 and +/-10% are sensitivity stress tests, not statistical uncertainty intervals.",
            "No rate, source, opacity, coupling, luminosity, or axial-vector curve is rescaled.",
        ],
        "configuration": {
            "radial_order": nr, "energy_order": ne, "angular_order": na,
            "path_order": ns, "radius_km": radius, "energy_offset_MeV": energy_offset,
        },
        "scenarios": scenarios,
        "comparisons_to_baseline": comparisons,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=HERE / "outputs" / "b16_numu_positive_branch_sensitivity_10mev_2026-11-09.json")
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--na", type=int, default=16)
    parser.add_argument("--ns", type=int, default=32)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()
    data = run(args.profile, args.fig7, args.mass, args.nr, args.ne, args.na,
               args.ns, args.radius, args.energy_offset)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(data["comparisons_to_baseline"], indent=2, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
