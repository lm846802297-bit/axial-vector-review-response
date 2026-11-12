"""Quantify source-weighted muon velocities relevant to the B.14 approximation."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
DEFAULT_PROFILE = DATA_DIR / "sfho188_digitized.csv"
DEFAULT_B16 = HERE / "outputs" / "b16_global_redshift_audit_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b13_nonrelativistic_muon_diagnostic_2026-11-09.json"
M_MU_MEV = 105.6583755


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def integrate_range(x: np.ndarray, y: np.ndarray, lo: float, hi: float) -> float:
    """Trapezoidal integral over [lo, hi], interpolating both boundaries."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if not (x[0] <= lo < hi <= x[-1]):
        raise ValueError("Integration interval must lie inside the profile")
    mask = (x > lo) & (x < hi)
    xx = np.r_[lo, x[mask], hi]
    yy = np.interp(xx, x, y)
    return float(np.sum(0.5 * (yy[1:] + yy[:-1]) * np.diff(xx)))


def muon_susceptibility_moments(
    temperature: np.ndarray,
    chemical_potential: np.ndarray,
    p_max: float = 600.0,
    dp: float = 0.5,
    mass: float = M_MU_MEV,
) -> dict[str, np.ndarray]:
    """Moments weighted by p^2 f_mu(1-f_mu), as in B.17."""
    temperature = np.asarray(temperature, float)
    chemical_potential = np.asarray(chemical_potential, float)
    if np.any(temperature <= 0.0):
        raise ValueError("Temperature must be positive")
    p = np.arange(dp / 2.0, p_max, dp)
    energy = np.sqrt(p[None, :] ** 2 + mass**2)
    z = (energy - chemical_potential[:, None]) / temperature[:, None]
    f = 1.0 / (1.0 + np.exp(np.clip(z, -700.0, 700.0)))
    weight = p[None, :] ** 2 * f * (1.0 - f)
    velocity = p[None, :] / energy
    norm = np.sum(weight, axis=1)
    if np.any(norm <= 0.0):
        raise FloatingPointError("Muon susceptibility vanished on the profile")
    return {
        "chi_mu_MeV3": norm * dp / np.pi**2,
        "mean_v_chi": np.sum(weight * velocity, axis=1) / norm,
        "rms_v_chi": np.sqrt(np.sum(weight * velocity**2, axis=1) / norm),
        "fraction_p_gt_m_chi": np.sum(weight[:, p > mass], axis=1) / norm,
        "fraction_v_gt_0p5_chi": np.sum(weight[:, velocity[0] > 0.5], axis=1) / norm,
    }


def load_profile(path: Path) -> dict[str, np.ndarray]:
    data = np.genfromtxt(path, delimiter=",", names=True)
    required = ("r_km", "T_MeV", "mu_mu_MeV", "lapse")
    if any(name not in data.dtype.names for name in required):
        raise ValueError(f"Profile must contain columns {required}")
    order = np.argsort(data["r_km"])
    data = data[order]
    _, unique_indices = np.unique(data["r_km"], return_index=True)
    data = data[np.sort(unique_indices)]
    return {name: np.asarray(data[column], float) for name, column in {
        "r_km": "r_km", "T_MeV": "T_MeV",
        "mu_mu_MeV": "mu_mu_MeV", "lapse": "lapse",
    }.items()}


def compute_diagnostic(profile_path: Path, b16_path: Path | None = DEFAULT_B16) -> dict:
    profile = load_profile(profile_path)
    moments = muon_susceptibility_moments(
        profile["T_MeV"], profile["mu_mu_MeV"]
    )
    r = profile["r_km"]
    # Leading low-mass B.16 radial source weight: r^2 N^2 (n_mu F_deg) T^4.
    radial_weight = (
        r**2 * profile["lapse"]**2
        * moments["chi_mu_MeV3"] * profile["T_MeV"]**4
    )
    total_weight = integrate_range(r, radial_weight, float(r[0]), float(r[-1]))
    shell_edges = [0.0, 5.0, 8.0, 10.0, 12.0, 15.0, 18.0, 20.0, 22.0, 25.0]
    shell_labels = [f"{a:g}-{b:g} km" for a, b in zip(shell_edges[:-1], shell_edges[1:])]
    shells = {}
    for label, lo, hi in zip(shell_labels, shell_edges[:-1], shell_edges[1:]):
        w = integrate_range(r, radial_weight, lo, hi)
        shells[label] = {
            "source_weight_fraction": w / total_weight,
            "mean_v_chi": integrate_range(
                r, radial_weight * moments["mean_v_chi"], lo, hi
            ) / w,
            "fraction_p_gt_m_chi": integrate_range(
                r, radial_weight * moments["fraction_p_gt_m_chi"], lo, hi
            ) / w,
            "fraction_v_gt_0p5_chi": integrate_range(
                r, radial_weight * moments["fraction_v_gt_0p5_chi"], lo, hi
            ) / w,
        }
    result = {
        "profile_sha256": sha256(profile_path),
        "muon_mass_MeV": M_MU_MEV,
        "momentum_quadrature": {
            "method": "midpoint rule",
            "p_max_MeV": 600.0,
            "dp_MeV": 0.5,
        },
        "radial_weight": "r^2 * lapse^2 * (n_mu F_deg) * T^4; leading low-mass B.16 source weight",
        "source_weighted_susceptibility_moments": {
            key: integrate_range(r, radial_weight * value, float(r[0]), float(r[-1])) / total_weight
            for key, value in moments.items() if key != "chi_mu_MeV3"
        },
        "shells": shells,
        "interpretation": (
            "Equilibrium muon-distribution diagnostic weighted by the B.17 susceptibility. "
            "It is not the full B.13 collision integrand and does not by itself quantify "
            "the B.14 rate error."
        ),
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
    }
    if b16_path is not None and Path(b16_path).exists():
        b16 = json.loads(Path(b16_path).read_text(encoding="utf-8"))
        row = next(x for x in b16["results"] if float(x["mass_MeV"]) == 0.1)
        reference = row["source_radial_distribution"]["shell_fractions"]
        result["comparison_to_B16_0p1MeV_source_shell_fractions"] = {
            "reference": reference,
            "maximum_absolute_fraction_difference": max(
                abs(shells[key]["source_weight_fraction"] - reference[key])
                for key in reference
            ),
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--b16", type=Path, default=DEFAULT_B16)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = compute_diagnostic(args.profile, args.b16)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
