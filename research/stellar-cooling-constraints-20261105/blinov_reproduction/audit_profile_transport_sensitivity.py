"""Full B.1+B.2 transport sensitivity to the 12--15 km profile inputs.

All matrix elements, quadratures, fixed-omega path conventions, and geometry
are held fixed. Only the named stellar-profile column is changed in each
diagnostic variant. No production rates, transport files, or axial outputs
are modified.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import tempfile

import numpy as np

import audit_b16_inner_path_channel_directional as b16
from reference import DEFAULT_PROFILE, KM_TO_MEV_INV, load_profile, local_rates, radial_rule
from audit_b16_global_redshift import eq_b1_source_measure

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "outputs" / "profile_transport_sensitivity_12_15km_2026-11-09.json"
DEFAULT_PROFILE_CSV = ROOT / "data" / "sfho188_digitized.csv"
MASS_MEV = 10.0
RADIUS_KM = 25.0
ENERGY_OFFSET_MEV = 1000.0
RADIAL_ORDER = 40
ENERGY_ORDER = 100
ANGULAR_ORDER = 32
STRONG_ENDPOINT_G = 4.17168965e-8
FLOOR_RADIUS_KM = 13.1099269401144


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_profile(path: Path):
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        names = reader.fieldnames
    if not names or not rows:
        raise ValueError(f"Empty profile CSV: {path}")
    data = {name: np.asarray([float(row[name]) for row in rows]) for name in names}
    return names, data


def write_profile(path: Path, names, data):
    matrix = np.column_stack([data[name] for name in names])
    np.savetxt(path, matrix, delimiter=",", header=",".join(names),
               comments="", fmt="%.15g")


def build_variants(profile_path: Path, temp_dir: Path):
    names, base = read_profile(profile_path)
    required = {"r_km", "mu_numu_MeV", "mu_mu_MeV", "mu_mu_Ferreira_MeV"}
    missing = required.difference(names)
    if missing:
        raise ValueError(f"Profile missing columns: {sorted(missing)}")
    r = base["r_km"]
    region = (r >= 12.0) & (r <= 15.0)
    unresolved = (r > FLOOR_RADIUS_KM) & (r <= 15.0)

    variants = {"baseline": {k: v.copy() for k, v in base.items()}}
    zero_nu = {k: v.copy() for k, v in base.items()}
    zero_nu["mu_numu_MeV"][region] = 0.0
    variants["A_mu_numu_zero_12_15km"] = zero_nu

    ferreira_mu = {k: v.copy() for k, v in base.items()}
    ferreira_mu["mu_mu_MeV"][region] = base["mu_mu_Ferreira_MeV"][region]
    variants["B_diagnostic_Ferreira_mu_mu_12_15km"] = ferreira_mu

    floor_envelope = {k: v.copy() for k, v in base.items()}
    floor_envelope["mu_numu_MeV"][unresolved] = -1.0
    variants["C_unresolved_mu_numu_at_plot_floor"] = floor_envelope

    paths = {}
    for label, values in variants.items():
        target = temp_dir / f"{label}.csv"
        write_profile(target, names, values)
        paths[label] = target

    # Guard against accidental multi-parameter changes.
    for label, values in variants.items():
        changed = [name for name in names
                   if not np.array_equal(values[name], base[name], equal_nan=True)]
        expected = {
            "baseline": [],
            "A_mu_numu_zero_12_15km": ["mu_numu_MeV"],
            "B_diagnostic_Ferreira_mu_mu_12_15km": ["mu_mu_MeV"],
            "C_unresolved_mu_numu_at_plot_floor": ["mu_numu_MeV"],
        }[label]
        if changed != expected:
            raise AssertionError(f"{label}: changed columns {changed}, expected {expected}")
    return paths, {
        "A_region_km": [12.0, 15.0],
        "B_region_km": [12.0, 15.0],
        "C_unresolved_region_km": [FLOOR_RADIUS_KM, 15.0],
        "C_assumed_mu_numu_MeV": -1.0,
        "C_interpretation": (
            "stress-test envelope using the 1 MeV logarithmic-plot resolution floor; "
            "not a reconstructed physical continuation"
        ),
        "B_interpretation": (
            "diagnostic substitution only; the alternative PDF curve's physical "
            "identity/convention is not promoted to the baseline"
        ),
    }


def evaluate_profile(profile_path: Path):
    radii, radial_weights = radial_rule(RADIUS_KM, RADIAL_ORDER)
    radial_grid = np.unique(np.r_[0.0, radii, RADIUS_KM])
    profile = load_profile(profile_path, radial_grid)
    energies = MASS_MEV + np.geomspace(
        max(MASS_MEV * 1.0e-6, 1.0e-6), ENERGY_OFFSET_MEV, ENERGY_ORDER
    )
    energies = np.unique(np.r_[energies, MASS_MEV / profile["lapse"]])
    energies = energies[energies > MASS_MEV * (1.0 + 1.0e-10)]
    energies.sort()

    rates = local_rates(
        MASS_MEV, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    production, reduced, closure = b16.reduced_absorption_channels(
        MASS_MEV, energies, profile, rates
    )
    columns, angles, angle_weights = b16.segmented_radial_columns(
        radii, radial_grid, reduced, MASS_MEV, energies,
        RADIUS_KM, ANGULAR_ORDER, b16.SHELL_EDGES_KM
    )
    source_indices = np.searchsorted(radial_grid, radii)
    source, source_meta = eq_b1_source_measure(
        radii, radial_weights, energies, profile["lapse"][source_indices],
        MASS_MEV, rates["production"][source_indices]
    )
    total_columns = np.sum(columns, axis=(0, 1))
    g2 = STRONG_ENDPOINT_G ** 2
    survival = np.exp(-np.minimum(g2 * total_columns, 745.0))
    base_weights = source[:, None, :] * angle_weights[None, :, None]
    norm = float(np.sum(base_weights))
    escaped = float(np.sum(base_weights * survival))
    own_escape = escaped / norm

    # Fixed-source comparison isolates the opacity/transport response from
    # the change in the B.1 source normalization.
    shell_index = int(np.where(
        (b16.SHELL_EDGES_KM[:-1] == 12.0)
        & (b16.SHELL_EDGES_KM[1:] == 15.0)
    )[0][0])
    shell_columns = columns[:, shell_index, :, :, :]
    shell_total = np.sum(shell_columns, axis=0)
    shell_tau_by_channel = {}
    for ic, name in enumerate(b16.CHANNELS):
        tau = shell_columns[ic]
        shell_tau_by_channel[name] = float(np.sum(base_weights * tau) / norm)

    local_samples = []
    for radius in (12.0, 13.0, 13.5, 14.0, 15.0):
        sample = {
            key: np.asarray([np.interp(radius, radial_grid, profile[key])])
            for key in ("T", "mu_mu", "mu_numu")
        }
        sample_energies = np.asarray([12.0, 20.0, 50.0])
        local = local_rates(
            MASS_MEV, sample_energies[None, :], sample["T"][:, None],
            sample["mu_numu"][:, None], sample["mu_mu"][:, None]
        )
        local_prod, local_reduced, _ = b16.reduced_absorption_channels(
            MASS_MEV, sample_energies, sample, local
        )
        for ie, energy in enumerate(sample_energies):
            local_samples.append({
                "radius_km": radius,
                "omega_local_MeV": float(energy),
                "T_MeV": float(sample["T"][0]),
                "mu_mu_MeV": float(sample["mu_mu"][0]),
                "mu_numu_MeV": float(sample["mu_numu"][0]),
                "reduced_absorption_per_g2": {
                    name: float(local_reduced[name][0, ie]) for name in b16.CHANNELS
                },
                "production_per_g2": {
                    name: float(local_prod[name][0, ie]) for name in b16.CHANNELS
                },
            })

    return {
        "profile_sha256": sha256(profile_path),
        "B1_source_integral": norm,
        "B1_source_metadata": source_meta,
        "escape_probability_own_source": own_escape,
        "escaped_source_integral": escaped,
        "shell_12_15km_mean_tau_per_g2_by_channel_baseline_source_weights":
            shell_tau_by_channel,
        "shell_12_15km_mean_tau_per_g2_total_baseline_source_weights":
            float(np.sum(base_weights * shell_total) / norm),
        "local_samples": local_samples,
        "channel_closure": closure,
        "_source_array": source,
        "_columns_array": columns,
        "_angle_weights_array": angle_weights,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE_CSV)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if not args.profile.exists():
        raise FileNotFoundError(args.profile)

    with tempfile.TemporaryDirectory(prefix="profile_transport_") as tmp:
        variant_paths, assumptions = build_variants(args.profile, Path(tmp))
        results = {
            label: evaluate_profile(path)
            for label, path in variant_paths.items()
        }

    baseline = results["baseline"]
    baseline_source = baseline["B1_source_integral"]
    baseline_escape = baseline["escape_probability_own_source"]
    # Re-evaluate each variant's opacity against the baseline B.1 source
    # requires identical radial/energy quadrature grids. Since all variants
    # share the same grid, own-source escape is already the physical full
    # variant result; the source-normalization and escape changes are reported
    # separately to avoid conflating the two effects.
    for label, result in results.items():
        result["B1_source_ratio_to_baseline"] = result["B1_source_integral"] / baseline_source
        result["escape_probability_ratio_to_baseline"] = (
            result["escape_probability_own_source"] / baseline_escape
        )
        result["escaped_source_integral_ratio_to_baseline"] = (
            result["escaped_source_integral"] / baseline["escaped_source_integral"]
        )

    # Isolate the opacity/transport response with the B.1 source held fixed.
    baseline_source_array = baseline["_source_array"]
    baseline_columns = baseline["_columns_array"]
    angle_weights = baseline["_angle_weights_array"]
    baseline_weights = baseline_source_array[:, None, :] * angle_weights[None, :, None]
    baseline_norm = float(np.sum(baseline_weights))
    shell_index = int(np.where(
        (b16.SHELL_EDGES_KM[:-1] == 12.0)
        & (b16.SHELL_EDGES_KM[1:] == 15.0)
    )[0][0])

    for label, result in results.items():
        columns = result["_columns_array"]
        total_columns = np.sum(columns, axis=(0, 1))
        survival = np.exp(-np.minimum(STRONG_ENDPOINT_G ** 2 * total_columns, 745.0))
        fixed_source_escape = float(np.sum(baseline_weights * survival) / baseline_norm)
        result["escape_probability_fixed_baseline_source"] = fixed_source_escape
        result["fixed_source_escape_ratio_to_baseline"] = (
            fixed_source_escape / baseline_escape
        )
        shell_columns = columns[:, shell_index, :, :, :]
        result["shell_12_15km_mean_tau_per_g2_by_channel_baseline_source_weights"] = {
            name: float(np.sum(baseline_weights * shell_columns[ic]) / baseline_norm)
            for ic, name in enumerate(b16.CHANNELS)
        }
        result["shell_12_15km_mean_tau_per_g2_total_baseline_source_weights"] = float(
            np.sum(baseline_weights * np.sum(shell_columns, axis=0)) / baseline_norm
        )

    # Remove internal arrays before writing the machine-readable record.
    for result in results.values():
        for key in ("_source_array", "_columns_array", "_angle_weights_array"):
            result.pop(key, None)

    payload = {
        "title": "Full B.1+B.2 profile-input sensitivity in the 12--15 km region",
        "benchmark": {
            "mass_MeV": MASS_MEV,
            "coupling": STRONG_ENDPOINT_G,
            "radius_km": RADIUS_KM,
            "energy_offset_MeV": ENERGY_OFFSET_MEV,
            "radial_order": RADIAL_ORDER,
            "energy_order": ENERGY_ORDER,
            "angular_order": ANGULAR_ORDER,
            "path_energy_convention": "fixed omega along the B.2 path",
            "profile_sha256": sha256(args.profile),
        },
        "variant_definitions": assumptions,
        "results": results,
        "interpretation": [
            "A, B, and C are controlled diagnostics; none is adopted as a replacement stellar background.",
            "B is not a preferred physical profile; it tests the impact of the alternative plotted mu_mu curve only.",
            "C uses the plotted 1 MeV resolution floor as a stress-test envelope, not as a measured continuation.",
            "The reported escape probability includes the B.1 source change of each variant.",
            "No empirical rescaling is applied and no axial-vector output is generated.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    print(json.dumps({
        label: {
            "B1_source_ratio": item["B1_source_ratio_to_baseline"],
            "escape_probability_ratio": item["escape_probability_ratio_to_baseline"],
            "escaped_source_integral_ratio": item["escaped_source_integral_ratio_to_baseline"],
            "fixed_source_escape_ratio": item["fixed_source_escape_ratio_to_baseline"],
            "tau_12_15_total_per_g2": item["shell_12_15km_mean_tau_per_g2_total_baseline_source_weights"],
        }
        for label, item in results.items()
    }, indent=2, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
