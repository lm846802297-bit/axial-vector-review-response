"""Source-frozen R_max sensitivity of the 10 MeV B.16 high-energy escape integral.

The literal R_max=25 km baseline is retained. Inward tests truncate only the
B.2 opacity support while holding the B.1 source fixed. For R_max>25 km, a
separate conditional diagnostic adds the two-flavour vacuum-limit neutrino
inverse-decay opacity outside 25 km and zero Compton opacity; it is not a
replacement thermodynamic profile or a new baseline.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile, local_rates,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile, local_rates,
    )
    from audit_b16_global_redshift import eq_b1_source_measure

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_REFERENCE = HERE / "outputs" / (
    "b16_p1c_global_polarization_b14_split_10mev_2026-11-10.json"
)
DEFAULT_OUTPUT = HERE / "outputs" / (
    "b16_rmax_boundary_sensitivity_10mev_2026-11-10.json"
)
RMAX_VALUES_KM = (15.0, 18.5, 20.0, 22.0, 24.0, 25.0, 26.0, 27.5, 30.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def truncated_sphere_columns(
    source_radii: np.ndarray,
    radial_grid: np.ndarray,
    reduced_opacity: np.ndarray,
    mass: float,
    energies: np.ndarray,
    radius_km: float,
    angular_order: int = 32,
    path_order: int = 64,
    profile_radius_km: float = 25.0,
) -> tuple[np.ndarray, np.ndarray]:
    """B.2 columns with opacity supported only inside R_max.

    For R_max <= profile_radius, the forward ray is integrated only over the
    portion lying inside the sphere. This also handles a source point outside
    the smaller sphere: an inward ray contributes only if it intersects the
    sphere. For R_max > profile_radius, the in-profile segment is retained and
    a vacuum-limit two-flavour neutrino opacity is added outside the profile.
    """
    source_radii = np.asarray(source_radii, float)
    radial_grid = np.asarray(radial_grid, float)
    reduced_opacity = np.asarray(reduced_opacity, float)
    energies = np.asarray(energies, float)
    if reduced_opacity.shape != (len(radial_grid), len(energies)):
        raise ValueError("Reduced-opacity grid has incompatible shape")
    if abs(radial_grid[0]) > 1e-12 or abs(radial_grid[-1] - profile_radius_km) > 1e-12:
        raise ValueError("Opacity grid must cover [0, profile_radius_km]")

    angles, angle_weights = leggauss(angular_order)
    angle_weights = angle_weights / 2.0
    path_x, path_w = leggauss(path_order)
    velocity = np.sqrt(1.0 - (mass / energies) ** 2)
    if np.any(velocity <= 0.0):
        raise ValueError("All sampled vectors must have positive speed")

    vacuum_nu = mass**2 / (4.0 * np.pi * energies)
    columns = np.zeros((len(source_radii), len(angles), len(energies)))

    for ir, r0 in enumerate(source_radii):
        for ia, cosine in enumerate(angles):
            impact = r0 * np.sqrt(max(0.0, 1.0 - cosine**2))
            z0 = r0 * cosine

            if radius_km <= profile_radius_km + 1e-12:
                if impact >= radius_km:
                    continue
                z_limit = np.sqrt(max(0.0, radius_km**2 - impact**2))
                z_start = max(z0, -z_limit)
                z_end = z_limit
                if z_start >= z_end:
                    continue
                extra_length = 0.0
            else:
                # Every source point lies at or inside the 25 km profile edge.
                z25 = np.sqrt(max(0.0, profile_radius_km**2 - impact**2))
                zR = np.sqrt(max(0.0, radius_km**2 - impact**2))
                z_start, z_end = z0, z25
                extra_length = max(0.0, zR - z25)

            integral = np.zeros(len(energies))
            if z_end > z_start:
                midpoint = 0.5 * (z_start + z_end)
                half_width = 0.5 * (z_end - z_start)
                z = midpoint + half_width * path_x
                rho = np.sqrt(impact**2 + z**2)
                for ie in range(len(energies)):
                    opacity_along_path = np.interp(
                        rho, radial_grid, reduced_opacity[:, ie]
                    )
                    integral[ie] = half_width * np.dot(
                        path_w, opacity_along_path
                    )

            if extra_length > 0.0:
                integral += extra_length * vacuum_nu

            columns[ir, ia, :] = (
                integral * KM_TO_MEV_INV / velocity
            )

    return columns, angle_weights


def extra_vacuum_tau_mean(
    source: np.ndarray,
    source_radii: np.ndarray,
    energies: np.ndarray,
    mass: float,
    coupling: float,
    radius_km: float,
    angular_order: int = 32,
    profile_radius_km: float = 25.0,
) -> float:
    """B.1-source- and angle-weighted mean extra g^2 tau outside 25 km."""
    angles, weights = leggauss(angular_order)
    weights = weights / 2.0
    velocity = np.sqrt(1.0 - (mass / energies) ** 2)
    vacuum_nu = mass**2 / (4.0 * np.pi * energies)
    total_source = float(np.sum(source))
    weighted_tau = 0.0

    for ir, r0 in enumerate(source_radii):
        for cosine, angle_weight in zip(angles, weights):
            impact = r0 * np.sqrt(max(0.0, 1.0 - cosine**2))
            z25 = np.sqrt(max(0.0, profile_radius_km**2 - impact**2))
            zR = np.sqrt(max(0.0, radius_km**2 - impact**2))
            extra_length = max(0.0, zR - z25)
            delta_tau = (
                coupling**2 * vacuum_nu * extra_length
                * KM_TO_MEV_INV / velocity
            )
            weighted_tau += angle_weight * float(
                np.dot(source[ir], delta_tau)
            )

    return weighted_tau / total_source


def run(
    profile_path: Path = DEFAULT_PROFILE,
    reference_path: Path = DEFAULT_REFERENCE,
    mass: float = 10.0,
    coupling: float = 4.171689650228597e-8,
    source_order: int = 200,
    opacity_order: int = 640,
    energy_order: int = 200,
    angular_order: int = 32,
    path_orders: tuple[int, ...] = (64, 128),
    energy_offset: float = 1000.0,
) -> dict:
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    source_r, source_rw = radial_rule(25.0, source_order)
    opacity_r, _ = radial_rule(25.0, opacity_order)
    opacity_grid = np.unique(np.r_[0.0, opacity_r, 25.0])

    source_profile = load_profile(profile_path, source_r)
    opacity_profile = load_profile(profile_path, opacity_grid)
    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass / opacity_profile["lapse"]])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()
    band_mask = (energies >= 210.0) & (energies <= 510.0)
    band_energies = energies[band_mask]
    if len(band_energies) != 10:
        raise ArithmeticError(
            f"Expected ten 210--510 MeV nodes, found {len(band_energies)}"
        )

    source_rates = local_rates(
        mass, energies[None, :], source_profile["T"][:, None],
        source_profile["mu_numu"][:, None], source_profile["mu_mu"][:, None],
    )
    source_full, source_meta = eq_b1_source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        source_rates["production"],
    )
    source = source_full[:, band_mask]

    opacity_rates = local_rates(
        mass, band_energies[None, :], opacity_profile["T"][:, None],
        opacity_profile["mu_numu"][:, None], opacity_profile["mu_mu"][:, None],
    )
    reduced = opacity_rates["reduced_absorption"]
    thin_luminosity = coupling**2 * float(np.sum(source))

    boundary_rows = []
    columns_by_order = {}
    for radius in RMAX_VALUES_KM:
        order_results = {}
        for path_order in path_orders:
            columns, angle_weights = truncated_sphere_columns(
                source_r, opacity_grid, reduced, mass, band_energies,
                radius, angular_order, path_order,
            )
            escape_average = np.einsum(
                "rae,a->re", np.exp(-coupling**2 * columns), angle_weights
            )
            luminosity = coupling**2 * float(np.sum(source * escape_average))
            source_outside = float(
                np.sum(source[source_r > radius]) / np.sum(source)
            )
            order_results[str(path_order)] = {
                "luminosity_erg_s": luminosity,
                "escape_fraction": luminosity / thin_luminosity,
                "source_fraction_outside_Rmax": source_outside,
            }
            columns_by_order[(radius, path_order)] = columns

        primary = order_results[str(path_orders[0])]
        refined = order_results[str(path_orders[-1])]
        boundary_rows.append({
            "Rmax_km": radius,
            "path_order_results": order_results,
            "relative_change_refined_vs_primary": (
                refined["luminosity_erg_s"] / primary["luminosity_erg_s"] - 1.0
            ),
        })

    baseline = next(row for row in boundary_rows if row["Rmax_km"] == 25.0)
    baseline_lum = baseline["path_order_results"][str(path_orders[0])]["luminosity_erg_s"]
    for row in boundary_rows:
        for values in row["path_order_results"].values():
            values["relative_change_vs_Rmax25"] = (
                values["luminosity_erg_s"] / baseline_lum - 1.0
            )

    opacity_r25 = float(opacity_grid[-1])
    T25 = float(opacity_profile["T"][-1])
    mu_numu25 = float(opacity_profile["mu_numu"][-1])
    mu_mu25 = float(opacity_profile["mu_mu"][-1])
    red_nu25 = (
        np.expm1(band_energies / T25)
        * opacity_rates["neutrino_production"][-1]
    )
    vacuum_nu = mass**2 / (4.0 * np.pi * band_energies)
    vacuum_ratio = red_nu25 / vacuum_nu

    extensions = []
    for radius in (26.0, 27.5, 30.0):
        extensions.append({
            "Rmax_km": radius,
            "source_weighted_mean_extra_tau": extra_vacuum_tau_mean(
                source, source_r, band_energies, mass, coupling, radius,
                angular_order,
            ),
        })

    expected_thin = float(reference["source_closure"]["thin_band_luminosity_erg_s"])
    expected_escape = float(reference["results"]["literal_scalar_sum"]["luminosity_erg_s"])
    baseline64 = float(
        baseline["path_order_results"][str(path_orders[0])]["luminosity_erg_s"]
    )
    baseline128 = float(
        baseline["path_order_results"][str(path_orders[-1])]["luminosity_erg_s"]
    )
    thin_residual = thin_luminosity / expected_thin - 1.0
    baseline_residual = baseline64 / expected_escape - 1.0
    max_path_change = max(
        abs(row["relative_change_refined_vs_primary"])
        for row in boundary_rows
    )
    if abs(thin_residual) > 1.0e-10:
        raise ArithmeticError("B.1 high-energy source does not close to P1-C")
    if abs(baseline_residual) > 1.0e-8:
        raise ArithmeticError("Rmax=25 km B.2 result does not close to P1-C")
    if max_path_change > 2.0e-5:
        raise ArithmeticError("Path-order 64/128 convergence failed")
    return {
        "title": "P1-D source-frozen Rmax boundary sensitivity of the 10 MeV B.16 high-energy band",
        "date": "2026-11-10",
        "benchmark": {
            "mass_MeV": mass,
            "coupling": coupling,
            "energy_band_MeV": [210.0, 510.0],
            "energy_nodes_MeV": band_energies.tolist(),
            "profile_sha256": sha256(profile_path),
            "profile_git_blob_sha": "e41df78c8035540760fbcb7ef592cd830171822e",
        },
        "configuration": {
            "source_radial_order": source_order,
            "source_radial_nodes": len(source_r),
            "opacity_radial_order": opacity_order,
            "opacity_radial_nodes": len(opacity_grid),
            "full_energy_order": energy_order,
            "full_energy_nodes": len(energies),
            "band_energy_nodes": len(band_energies),
            "angular_order": angular_order,
            "path_orders": list(path_orders),
            "source_measure": "Eq. (B.1), frozen at the Rmax=25 km baseline",
            "inward_boundary": "B.2 opacity supported only at r<=Rmax; source remains fixed",
            "outward_extension": "two-flavour vacuum-limit neutrino inverse-decay opacity outside 25 km; zero Compton opacity",
        },
        "baseline_closure": {
            "thin_band_luminosity_erg_s": thin_luminosity,
            "reference_thin_band_luminosity_erg_s": expected_thin,
            "thin_source_relative_residual": thin_residual,
            "Rmax25_path64_luminosity_erg_s": baseline64,
            "reference_Rmax25_luminosity_erg_s": expected_escape,
            "Rmax25_path64_relative_residual": baseline_residual,
            "Rmax25_path128_luminosity_erg_s": baseline128,
            "Rmax25_path128_relative_residual": baseline128 / expected_escape - 1.0,
        },
        "boundary_scan": boundary_rows,
        "max_absolute_path_order_change": max_path_change,
        "outer_vacuum_limit": {
            "profile_boundary_km": opacity_r25,
            "T25_MeV": T25,
            "mu_numu25_MeV": mu_numu25,
            "mu_mu25_MeV": mu_mu25,
            "local_two_flavour_reduced_neutrino_opacity_over_vacuum": vacuum_ratio.tolist(),
            "minimum_ratio": float(np.min(vacuum_ratio)),
            "maximum_ratio": float(np.max(vacuum_ratio)),
            "conditional_extension_extra_tau": extensions,
        },
        "interpretation": [
            "The B.1 source is frozen. The high-energy source fraction outside Rmax=15 km is below 1e-6, so the inward boundary scan is not driven by omitted source.",
            "The Rmax=25 km calculation closes against the archived P1-C source and escaped luminosity.",
            "Inward truncation of the B.2 opacity support increases the high-energy escaped luminosity substantially.",
            "The outward extension is a conditional trapping-boundary diagnostic, not a thermodynamic profile beyond 25 km.",
            "The literal paper boundary Rmax=Rnu approximately 25 km remains the baseline; no boundary is selected by fitting Fig. 7.",
            "No source, opacity normalization, coupling, profile, Fig. 7 curve, or axial-vector result is changed.",
        ],
        "limitations": [
            "This is the 210--510 MeV band at the 10 MeV strong-endpoint coupling, not a complete 25-point Fig. 7 rerun.",
            "The inward scan freezes the B.1 source intentionally; the selected band has negligible source support outside 15 km.",
            "The outward continuation assumes vacuum-limit two-flavour neutrino opacity and zero Compton opacity outside 25 km; it is conditional on continued neutrino trapping and is not a new baseline.",
            "The public-figure reconstruction is not the original Garching simulation table.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--coupling", type=float, default=4.171689650228597e-8)
    args = parser.parse_args()
    result = run(args.profile, args.reference, args.mass, args.coupling)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "baseline_closure": result["baseline_closure"],
        "boundary_scan": result["boundary_scan"],
        "outer_vacuum_limit": result["outer_vacuum_limit"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
