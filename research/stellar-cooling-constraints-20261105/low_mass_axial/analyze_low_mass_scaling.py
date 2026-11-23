#!/usr/bin/env python3
"""Post-process existing low-mass axial supernova numerical outputs."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONSTRAINTS = HERE.parent
THERMAL = CONSTRAINTS / "finite_mixing" / "outputs" / "thermal_response_scan.json"
CONVERGENCE = CONSTRAINTS / "outputs" / "convergence.json"
DEFAULT_OUTPUT = HERE / "outputs" / "low_mass_scaling_summary.json"
MASSES = (0.01, 0.1, 1.0, 10.0)
VS_VALUES = (509.0, 1000.0, 2000.0, 10000.0)
L_CRIT = 4.4e52


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)



def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def mass_row(rows: list[dict], mass: float) -> dict:
    found = [r for r in rows if math.isclose(
        float(r["mass_MeV"]), mass, rel_tol=0.0, abs_tol=1e-10
    )]
    if len(found) != 1:
        raise ValueError(f"Expected one row at {mass} MeV, found {len(found)}")
    return found[0]


def trapping_crossing(rows: list[dict], v_s: float) -> float | None:
    points = []
    for row in rows:
        intervals = row.get("intervals_4p4e52", [])
        if intervals:
            points.append((float(row["mass_MeV"]), float(intervals[0][1])))
    points.sort()
    for (m1, g1), (m2, g2) in zip(points[:-1], points[1:]):
        f1 = math.log((m1 * 1e-3 / (2 * v_s)) / g1)
        f2 = math.log((m2 * 1e-3 / (2 * v_s)) / g2)
        if f1 * f2 < 0:
            t = -f1 / (f2 - f1)
            return math.exp(math.log(m1) + t * (math.log(m2) - math.log(m1)))
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--thermal", type=Path, default=THERMAL)
    parser.add_argument("--convergence", type=Path, default=CONVERGENCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    thermal, convergence = load_json(args.thermal), load_json(args.convergence)

    local = []
    for mass in MASSES:
        row = mass_row(thermal["compton"]["mass_scan_at_center"], mass)
        q_l = float(row["Q_axial_by_mode_MeV5"][0])
        q_t = float(row["Q_axial_by_mode_MeV5"][1] + row["Q_axial_by_mode_MeV5"][2])
        local.append({
            "mass_MeV": mass, "Q_L_per_gX2_MeV5": q_l,
            "Q_T_total_per_gX2_MeV5": q_t, "Q_L_over_Q_T": q_l / q_t,
            "mass_squared_Q_L": mass * mass * q_l,
        })

    cooling = []
    for mass in MASSES:
        row = mass_row(convergence["results"], mass)
        if not row.get("intervals_4p4e52"):
            raise ValueError(f"No cooling interval at {mass} MeV")
        g_lower, g_upper = map(float, row["intervals_4p4e52"][0])
        mass_gev = mass * 1e-3
        cooling.append({
            "mass_MeV": mass, "gX_lower": g_lower, "gX_upper": g_upper,
            "gX_lower_over_mass_MeV": g_lower / mass,
            "vS_lower_GeV": mass_gev / (2 * g_upper),
            "vS_upper_GeV": mass_gev / (2 * g_lower),
        })

    q_scaled = [r["mass_squared_Q_L"] for r in local[:3]]
    g_scaled = [r["gX_lower_over_mass_MeV"] for r in cooling[:3]]
    q_spread = (max(q_scaled) - min(q_scaled)) / min(q_scaled)
    g_spread = (max(g_scaled) - min(g_scaled)) / min(g_scaled)
    result = {
        "title": "Low-mass axial-vector supernova scaling summary",
        "cooling_threshold_erg_s": L_CRIT,
        "inputs": {
            "thermal_response_scan": str(args.thermal),
            "thermal_response_scan_git_blob_sha1": git_blob_sha1(args.thermal),
            "convergence_scan": str(args.convergence),
            "convergence_scan_git_blob_sha1": git_blob_sha1(args.convergence),
        },
        "local_moving_muon_compton": {
            "profile_point": thermal["profile"]["center"],
            "mode_order": thermal["mode_order"],
            "masses": local,
            "relative_spread_of_m2_QL_over_0p01_to_1MeV": q_spread,
        },
        "fixed_profile_convergence_scan": {
            "source_description": convergence["description"],
            "masses": cooling,
            "relative_spread_of_gXlower_over_mass_0p01_to_1MeV": g_spread,
            "fixed_vS_trapping_crossings": [
                {"v_s_GeV": v, "crossing_mass_MeV": trapping_crossing(convergence["results"], v)}
                for v in VS_VALUES
            ],
        },
        "interpretation": {
            "free_streaming_low_mass_scaling": "gX_lower proportional to mAprime",
            "original_single_VEV_mapping": "vS_upper approximately mass independent at low mass",
            "limitation": "The fixed-profile convergence scan is not yet recomputed with the moving-muon local kernel in full radial transport.",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output), "local_mass_points": len(local),
        "cooling_mass_points": len(cooling), "m2_QL_relative_spread": q_spread,
        "gX_lower_over_mass_relative_spread": g_spread,
        "fixed_vS_crossings": result["fixed_profile_convergence_scan"]["fixed_vS_trapping_crossings"],
    }, indent=2))


if __name__ == "__main__":
    main()
