"""Extract a compact, reviewable summary from the full B.13 global transport JSON."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "outputs" / "b13_global_transport_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def summarize(source_path: Path, output_path: Path) -> dict:
    source_path = Path(source_path)
    output_path = Path(output_path)
    data = json.loads(source_path.read_text(encoding="utf-8"))
    grid = data.get("local_rate_grid", {})
    radial = grid.get("radial_grid_km", [])
    energy = grid.get("energies_MeV", [])
    active_r = grid.get("active_radial_mask", [])
    active_e = grid.get("active_energy_mask", [])
    if not radial or not energy or len(active_r) != len(radial) or len(active_e) != len(energy):
        raise ValueError("The full B.13 output has an incomplete local-rate grid")
    if data["profile"]["sha256"] != "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c":
        raise ValueError("Unexpected SFHo profile fingerprint")
    if data["archived_B16_baseline"]["max_relative_reproduction_residual"] > 2e-10:
        raise ValueError("The B.16 baseline closure is outside tolerance")

    summary = {key: value for key, value in data.items() if key != "local_rate_grid"}
    summary["local_rate_grid_summary"] = {
        "radial_node_count": len(radial),
        "energy_node_count": len(energy),
        "active_radial_node_count": sum(bool(x) for x in active_r),
        "inactive_radial_node_count": sum(not bool(x) for x in active_r),
        "active_energy_node_count": sum(bool(x) for x in active_e),
        "active_radial_nodes_km": [r for r, active in zip(radial, active_r) if active],
        "inactive_radial_nodes_km": [r for r, active in zip(radial, active_r) if not active],
        "energy_min_MeV": min(energy),
        "energy_max_MeV": max(energy),
        "full_grid_sha256": sha256(source_path),
        "note": (
            "The full JSON retains all radial-energy local rate arrays. "
            "This compact summary intentionally omits those arrays but records "
            "the exact source-file hash and grid metadata."
        ),
    }
    summary["summary_source"] = {
        "path": str(source_path),
        "sha256": sha256(source_path),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    summary = summarize(args.input, args.output)
    print(json.dumps({
        "output": str(args.output),
        "profile_sha256": summary["profile"]["sha256"],
        "full_grid": summary["local_rate_grid_summary"],
        "source_fractions": summary["source_channel_fractions"],
        "radial_source_diagnostics": summary["radial_source_diagnostics"],
        "opacity_weighted_diagnostics": summary["opacity_weighted_diagnostics"],
        "variant_metrics": {
            key: value["metrics_vs_fig7"]
            for key, value in summary["variant_results"].items()
        },
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
