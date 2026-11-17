"""Instrument the B.16 phase-space energy array through each calculation stage."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

try:
    from .reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates, scalar_optical_depths
    from .audit_b16_global_redshift import (
        DEFAULT_FIG7, DEFAULT_BASELINE, eq_b1_source_measure,
        float_array_sha256, sha256,
    )
    from .diagnose_b16_energy_grid_identity import build_energy_grid
except ImportError:
    from reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates, scalar_optical_depths
    from audit_b16_global_redshift import (
        DEFAULT_FIG7, DEFAULT_BASELINE, eq_b1_source_measure,
        float_array_sha256, sha256,
    )
    from diagnose_b16_energy_grid_identity import build_energy_grid

HERE = Path(__file__).resolve().parent


def snapshot(label, energies, original):
    return {
        "stage": label,
        "sha256": float_array_sha256(energies),
        "node_count": int(len(energies)),
        "changed_from_initial": int(np.count_nonzero(energies != original)),
        "max_abs_change_from_initial": float(np.max(np.abs(energies-original))),
        "first_8": energies[:8].tolist(),
        "last_8": energies[-8:].tolist(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('/tmp/b16_runtime_energy_mutation_diagnostic.json'))
    args = parser.parse_args()
    mass = 10.0
    radial_order = 200
    opacity_order = 640
    energy_order = 200
    angular_order = 32
    path_order = 64
    energy_offset = 1000.0
    radius_km = 25.0

    source_r, source_rw = radial_rule(radius_km, radial_order)
    opacity_r, _ = radial_rule(radius_km, opacity_order)
    opacity_grid = np.unique(np.r_[0.0, opacity_r, radius_km])
    source_profile = load_profile(DEFAULT_PROFILE, source_r)
    opacity_profile = load_profile(DEFAULT_PROFILE, opacity_grid)

    # Exact construction copied from audit_b16_escape_phase_space.run().
    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass / opacity_profile["lapse"]])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()
    original = energies.copy()

    reconstructed, _ = build_energy_grid(
        mass, energy_order, energy_offset, opacity_profile["lapse"]
    )
    snapshots = [snapshot("immediately_after_grid_construction", energies, original)]
    print("grid_reconstruction_equal", np.array_equal(energies, reconstructed), flush=True)
    print("initial_hash", snapshots[-1]["sha256"], flush=True)

    opacity_rates = local_rates(
        mass, energies[None, :], opacity_profile["T"][:, None],
        opacity_profile["mu_numu"][:, None], opacity_profile["mu_mu"][:, None]
    )
    snapshots.append(snapshot("after_opacity_local_rates", energies, original))

    source_rates = local_rates(
        mass, energies[None, :], source_profile["T"][:, None],
        source_profile["mu_numu"][:, None], source_profile["mu_mu"][:, None]
    )
    snapshots.append(snapshot("after_source_local_rates", energies, original))

    source, source_meta = eq_b1_source_measure(
        source_r, source_rw, energies, source_profile["lapse"],
        mass, source_rates["production"]
    )
    snapshots.append(snapshot("after_eq_b1_source_measure", energies, original))

    columns, angle_weights = scalar_optical_depths(
        source_r, opacity_grid, opacity_rates["reduced_absorption"],
        mass, energies, radius_km, angular_order, path_order
    )
    snapshots.append(snapshot("after_scalar_optical_depths", energies, original))

    result = {
        "status": "unchanged" if all(x["changed_from_initial"] == 0 for x in snapshots) else "mutated",
        "snapshots": snapshots,
        "grid_identity": {
            "source_grid_sha256": float_array_sha256(source_r),
            "opacity_grid_sha256": float_array_sha256(opacity_grid),
            "energy_grid_sha256": float_array_sha256(energies),
            "expected_baseline_energy_grid_sha256": json.loads(DEFAULT_BASELINE.read_text())["result"]["configuration"]["energy_grid_sha256"],
        },
        "profile_sha256": sha256(DEFAULT_PROFILE),
        "fig7_sha256": sha256(DEFAULT_FIG7),
        "source_shape": list(source.shape),
        "opacity_shape": list(columns.shape),
        "angle_weight_sum": float(np.sum(angle_weights)),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\\n")
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
