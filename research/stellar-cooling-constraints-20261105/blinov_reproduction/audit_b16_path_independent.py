"""Independent B.2 propagation audit using analytic chord integration.

The existing reference integrates each chord with Gauss-Legendre quadrature in
path length s. This implementation instead uses z=s+r*cos(theta), splits the
ray at every radial interpolation knot, and integrates the piecewise-linear
opacity exactly on each segment. Angular averages are checked with
Gauss-Legendre, composite Simpson, and adaptive QUADPACK integration.

The local collision kernel and B.1 source measure are shared to isolate B.2.
No existing B.2 path-integration function generates the independent columns.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, local_rates, radial_rule,
        load_profile, scalar_optical_depths,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure, curve_metrics
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, local_rates, radial_rule,
        load_profile, scalar_optical_depths,
    )
    from audit_b16_global_redshift import eq_b1_source_measure, curve_metrics

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_BASELINE = HERE / "outputs" / "b16_global_fig7_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_path_independent_analytic_10mev_2026-11-09.json"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _primitive_rho(z: float, impact: float) -> float:
    """Primitive of sqrt(z**2 + impact**2) with respect to z."""
    if impact == 0.0:
        return 0.5 * z * abs(z)
    rho = np.hypot(z, impact)
    return 0.5 * (z * rho + impact * impact * np.arcsinh(z / impact))


def chord_integral_piecewise_linear(
    source_radius_km: float,
    cosine: float,
    radial_grid_km: np.ndarray,
    opacity_by_radius: np.ndarray,
) -> np.ndarray:
    """Return integral ds Gamma*(r(s),omega), exact for linear radial data.

    opacity_by_radius has shape (n_radius,) or (n_radius,n_energy). The
    interpolation convention matches numpy.interp, while the path integral
    itself is evaluated analytically on every radial interpolation segment.
    """
    grid = np.asarray(radial_grid_km, float)
    values = np.asarray(opacity_by_radius, float)
    if values.ndim == 1:
        values = values[:, None]
    if grid.ndim != 1 or values.shape[0] != len(grid) or len(grid) < 2:
        raise ValueError("Opacity array and radial grid have incompatible shapes")
    if np.any(np.diff(grid) <= 0.0):
        raise ValueError("Radial grid must be strictly increasing")
    if not (-1.0 <= cosine <= 1.0):
        raise ValueError("Direction cosine must lie in [-1,1]")

    radius = float(grid[-1])
    r0 = float(source_radius_km)
    if r0 < grid[0] or r0 > radius:
        raise ValueError("Source radius lies outside the radial grid")

    impact = r0 * np.sqrt(max(0.0, 1.0 - cosine * cosine))
    z0 = r0 * cosine
    z1 = np.sqrt(max(0.0, radius * radius - impact * impact))
    if z1 < z0:
        raise ArithmeticError("Chord endpoint precedes its source point")

    # z=s+r*cos(theta), rho=sqrt(b^2+z^2), ds=dz.
    # Split at every crossing of a radial interpolation knot.
    breaks = [z0, z1]
    if z0 < 0.0 < z1:
        breaks.append(0.0)
    for knot in grid:
        if knot < impact:
            continue
        zabs = np.sqrt(max(0.0, knot * knot - impact * impact))
        if z0 < zabs < z1:
            breaks.append(zabs)
        if z0 < -zabs < z1:
            breaks.append(-zabs)
    breaks = np.unique(np.asarray(breaks, float))

    integral = np.zeros(values.shape[1], dtype=float)
    for left, right in zip(breaks[:-1], breaks[1:]):
        if right <= left:
            continue
        midpoint = 0.5 * (left + right)
        rho_mid = np.hypot(midpoint, impact)
        index = int(np.searchsorted(grid, rho_mid, side="right") - 1)
        index = min(max(index, 0), len(grid) - 2)

        slope = (values[index + 1] - values[index]) / (
            grid[index + 1] - grid[index]
        )
        intercept = values[index] - slope * grid[index]
        integral += intercept * (right - left)
        integral += slope * (
            _primitive_rho(float(right), impact)
            - _primitive_rho(float(left), impact)
        )

    if np.any(integral < -1.0e-12 * max(1.0, float(np.max(np.abs(values))))):
        raise FloatingPointError("Analytic chord integral became negative")
    return np.maximum(integral, 0.0)


def analytic_chord_columns(
    source_radii_km: np.ndarray,
    radial_grid_km: np.ndarray,
    reduced_absorption: np.ndarray,
    mass_mev: float,
    energies_mev: np.ndarray,
    radius_km: float,
    direction_cosines: np.ndarray,
) -> np.ndarray:
    """Return B.2 optical depths [source radius, direction, energy]."""
    source_radii = np.asarray(source_radii_km, float)
    radial_grid = np.asarray(radial_grid_km, float)
    opacity = np.asarray(reduced_absorption, float)
    energies = np.asarray(energies_mev, float)
    directions = np.asarray(direction_cosines, float)
    if opacity.shape != (len(radial_grid), len(energies)):
        raise ValueError("Reduced-opacity grid has the wrong shape")
    if abs(radial_grid[-1] - radius_km) > 1.0e-12:
        raise ValueError("Radial grid must terminate at R_max")
    velocity = np.sqrt(np.maximum(1.0 - (mass_mev / energies) ** 2, 0.0))
    if np.any(velocity <= 0.0):
        raise ValueError("All sampled vectors must have positive speed")

    columns = np.empty((len(source_radii), len(directions), len(energies)))
    for ir, source_radius in enumerate(source_radii):
        for ia, cosine in enumerate(directions):
            line_integral = chord_integral_piecewise_linear(
                source_radius, float(cosine), radial_grid, opacity
            )
            columns[ir, ia, :] = line_integral * KM_TO_MEV_INV / velocity
    return columns


def gauss_angle_rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    if order < 2:
        raise ValueError("Angular order must be at least two")
    nodes, weights = leggauss(order)
    return nodes, weights / 2.0


def simpson_angle_rule(subintervals: int) -> tuple[np.ndarray, np.ndarray]:
    """Composite Simpson weights for the normalized average over [-1,1]."""
    n = int(subintervals)
    if n < 2 or n % 2:
        raise ValueError("Composite Simpson requires a positive even interval count")
    nodes = np.linspace(-1.0, 1.0, n + 1)
    weights = np.ones(n + 1)
    weights[1:-1:2] = 4.0
    weights[2:-1:2] = 2.0
    weights /= 3.0 * n
    return nodes, weights


def luminosity_curve(source, columns, angular_weights, couplings):
    values, escape_fractions = [], []
    for coupling in np.asarray(couplings, float):
        average_escape = np.einsum(
            "rae,a->re", np.exp(-coupling * coupling * columns), angular_weights
        )
        thin = coupling * coupling * float(np.sum(source))
        luminosity = coupling * coupling * float(np.sum(source * average_escape))
        values.append(luminosity)
        escape_fractions.append(luminosity / thin if thin > 0.0 else 0.0)
    return np.asarray(values), np.asarray(escape_fractions)


def adaptive_angular_escape(
    source_radius_km, energy_index, coupling, radial_grid_km,
    reduced_absorption, mass_mev, energies_mev, radius_km,
):
    """Independent QUADPACK integral of <exp(-g^2 tau)> over direction."""
    energy = float(energies_mev[energy_index])
    velocity = np.sqrt(1.0 - (mass_mev / energy) ** 2)
    radial_opacity = np.asarray(reduced_absorption[:, energy_index], float)

    def integrand(cosine):
        line_integral = chord_integral_piecewise_linear(
            source_radius_km, cosine, radial_grid_km, radial_opacity
        )[0]
        tau = line_integral * KM_TO_MEV_INV / velocity
        return 0.5 * np.exp(-coupling * coupling * tau)

    value, error = quad(
        integrand, -1.0, 1.0, epsabs=1.0e-11, epsrel=2.0e-8, limit=300
    )
    return float(value), float(error)


def _relative_summary(approx, exact, weights):
    approx = np.asarray(approx, float)
    exact = np.asarray(exact, float)
    rel = np.abs(approx - exact) / np.maximum(np.abs(exact), 1.0e-300)
    weights = np.broadcast_to(np.asarray(weights, float), rel.shape)
    active = weights > 0.0
    weighted_rms = np.sqrt(
        np.sum(weights[active] * rel[active] ** 2) / np.sum(weights[active])
    )
    return {
        "maximum_absolute_relative_difference": float(np.max(rel[active])),
        "p99_absolute_relative_difference": float(np.quantile(rel[active], 0.99)),
        "source_weighted_rms_relative_difference": float(weighted_rms),
    }


def run(
    profile_path=DEFAULT_PROFILE,
    fig7_path=DEFAULT_FIG7,
    baseline_path=DEFAULT_BASELINE,
    output_path=DEFAULT_OUTPUT,
    mass=10.0,
    radial_order=40,
    energy_order=100,
    angular_orders=(16, 32, 64),
    simpson_subintervals=(128, 256),
    path_orders=(8, 16, 32, 64, 128),
    radius_km=25.0,
    energy_offset=1000.0,
):
    started = time.time()
    profile_sha = sha256(profile_path)
    if profile_sha != EXPECTED_PROFILE_SHA256:
        raise ValueError(
            f"Unexpected profile SHA-256 {profile_sha}; expected {EXPECTED_PROFILE_SHA256}"
        )

    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
    couplings = np.asarray(vertices["g"], float)
    fig7_luminosity = np.asarray(vertices["luminosity_erg_s"], float)

    r, rw = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
    profile = load_profile(profile_path, radial_grid)
    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass / profile["lapse"]])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()

    rates = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    source_index = np.searchsorted(radial_grid, r)
    source, source_pieces = eq_b1_source_measure(
        r, rw, energies, profile["lapse"][source_index], mass,
        rates["production"][source_index]
    )
    reduced_absorption = np.asarray(rates["reduced_absorption"], float)

    archived = json.loads(Path(baseline_path).read_text(encoding="utf-8"))
    archived_result = archived["results"][0]
    if archived_result["profile"]["sha256"] != profile_sha:
        raise ValueError("Archived B.16 baseline has a different profile")
    archived_points = archived_result["eq_b2_fixed_omega_baseline"]["points"]
    if len(archived_points) != len(couplings):
        raise ValueError("Archived B.16 baseline coupling grid does not match Fig. 7")
    archived_luminosity = np.asarray(
        [point["calculated_luminosity_erg_s"] for point in archived_points]
    )
    archived_couplings = np.asarray([point["g"] for point in archived_points])
    np.testing.assert_allclose(archived_couplings, couplings, rtol=2.0e-14, atol=0.0)

    # Reference B.2: Gauss-Legendre quadrature in path length s.
    baseline_columns, baseline_angle_weights = scalar_optical_depths(
        r, radial_grid, reduced_absorption, mass, energies, radius_km,
        angular_order=16, path_order=32
    )
    baseline_luminosity, baseline_escape = luminosity_curve(
        source, baseline_columns, baseline_angle_weights, couplings
    )
    archived_reproduction_residual = baseline_luminosity / archived_luminosity - 1.0
    if np.max(np.abs(archived_reproduction_residual)) > 2.0e-9:
        raise ArithmeticError("Reconstructed reference B.16 does not reproduce archive")

    # Independent analytic path integration at the exact same 16 directions.
    nodes16, weights16 = gauss_angle_rule(16)
    exact16 = analytic_chord_columns(
        r, radial_grid, reduced_absorption, mass, energies, radius_km, nodes16
    )
    path_weights = source[:, None, :] * weights16[None, :, None]
    path_residual = _relative_summary(baseline_columns, exact16, path_weights)
    exact16_luminosity, exact16_escape = luminosity_curve(
        source, exact16, weights16, couplings
    )

    path_convergence = []
    for order in path_orders:
        if order == 32:
            columns = baseline_columns
        else:
            columns, _ = scalar_optical_depths(
                r, radial_grid, reduced_absorption, mass, energies,
                radius_km, angular_order=16, path_order=order
            )
        lum, escape = luminosity_curve(source, columns, weights16, couplings)
        path_convergence.append({
            "path_order": int(order),
            "tau_vs_analytic": _relative_summary(columns, exact16, path_weights),
            "maximum_luminosity_shift_vs_analytic_16_angle": float(
                np.max(np.abs(lum / exact16_luminosity - 1.0))
            ),
            "maximum_escape_fraction_shift_vs_analytic_16_angle": float(
                np.max(np.abs(escape / exact16_escape - 1.0))
            ),
        })

    angular_convergence = []
    angular_products = {}
    for order in angular_orders:
        nodes, weights = gauss_angle_rule(order)
        columns = exact16 if order == 16 else analytic_chord_columns(
            r, radial_grid, reduced_absorption, mass, energies, radius_km, nodes
        )
        luminosity, escape = luminosity_curve(source, columns, weights, couplings)
        angular_products[f"gauss_{order}"] = (nodes, weights, columns)
        angular_convergence.append({
            "rule": "Gauss-Legendre",
            "order": int(order),
            "luminosity_vs_fig7": curve_metrics(luminosity, fig7_luminosity),
            "maximum_luminosity_shift_vs_gauss_16": float(
                np.max(np.abs(luminosity / exact16_luminosity - 1.0))
            ),
            "maximum_escape_fraction_shift_vs_gauss_16": float(
                np.max(np.abs(escape / exact16_escape - 1.0))
            ),
        })

    for intervals in simpson_subintervals:
        nodes, weights = simpson_angle_rule(intervals)
        columns = analytic_chord_columns(
            r, radial_grid, reduced_absorption, mass, energies, radius_km, nodes
        )
        luminosity, escape = luminosity_curve(source, columns, weights, couplings)
        angular_products[f"simpson_{intervals}"] = (nodes, weights, columns)
        angular_convergence.append({
            "rule": "composite Simpson",
            "subintervals": int(intervals),
            "luminosity_vs_fig7": curve_metrics(luminosity, fig7_luminosity),
            "maximum_luminosity_shift_vs_gauss_16": float(
                np.max(np.abs(luminosity / exact16_luminosity - 1.0))
            ),
            "maximum_escape_fraction_shift_vs_gauss_16": float(
                np.max(np.abs(escape / exact16_escape - 1.0))
            ),
        })

    # Adaptive QUADPACK checks selected direction averages independently.
    high_weights, high_columns = (
        angular_products[f"simpson_{max(simpson_subintervals)}"][1:]
    )
    adaptive_checks = []
    for target_r in (8.0, 12.0, 15.0):
        ir = int(np.argmin(np.abs(r - target_r)))
        for target_e in (20.0, 50.0, 100.0):
            ie = int(np.argmin(np.abs(energies - target_e)))
            for target_g in (1.0e-8, 2.0e-8, 4.171689650228597e-8):
                ig = int(np.argmin(np.abs(couplings - target_g)))
                adaptive_value, adaptive_error = adaptive_angular_escape(
                    float(r[ir]), ie, float(couplings[ig]), radial_grid,
                    reduced_absorption, mass, energies, radius_km
                )
                simpson_escape = float(np.dot(
                    high_weights,
                    np.exp(-couplings[ig]**2 * high_columns[ir, :, ie])
                ))
                adaptive_checks.append({
                    "source_radius_km": float(r[ir]),
                    "energy_MeV": float(energies[ie]),
                    "coupling": float(couplings[ig]),
                    "quadpack_escape_average": adaptive_value,
                    "quadpack_abs_error": adaptive_error,
                    "simpson_escape_average": simpson_escape,
                    "relative_difference": float(simpson_escape / adaptive_value - 1.0),
                })

    final_rule = f"simpson_{max(simpson_subintervals)}"
    _, final_weights, final_columns = angular_products[final_rule]
    final_luminosity, final_escape = luminosity_curve(
        source, final_columns, final_weights, couplings
    )
    final_vs_archived = final_luminosity / archived_luminosity - 1.0

    payload = {
        "source": "Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B, Eqs. (B.1)--(B.5)",
        "method": (
            "Independent exact-in-path integration of piecewise-linear radial "
            "reduced opacity; z=s+r*cos(theta); split at every radial knot; "
            "analytic primitive for A+B*sqrt(b^2+z^2); angular average checked "
            "with Gauss-Legendre, composite Simpson, and adaptive QUADPACK."
        ),
        "shared_inputs": (
            "Local collision kernel, reconstructed profile, B.1 source measure, "
            "energy grid, and Fig. 7 vertices are held identical to the archived "
            "B.16 baseline. No existing B.2 path integrator generates the new tau."
        ),
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": sha256(Path(__file__)),
        "profile": {"path": str(profile_path.name), "sha256": profile_sha},
        "fig7_reference_sha256": sha256(fig7_path),
        "archived_b16_baseline_sha256": sha256(baseline_path),
        "configuration": {
            "mass_MeV": float(mass),
            "radial_order": int(radial_order),
            "energy_order_before_lapse_threshold_union": int(energy_order),
            "number_of_energy_nodes_after_threshold_union": int(len(energies)),
            "number_of_source_radius_nodes": int(len(r)),
            "radius_km": float(radius_km),
            "energy_offset_MeV": float(energy_offset),
            "reference_path_order": 32,
            "reference_angular_order": 16,
            "independent_angular_orders": list(angular_orders),
            "composite_simpson_subintervals": list(simpson_subintervals),
            "path_order_convergence": list(path_orders),
            "coupling_points": int(len(couplings)),
        },
        "source_measure": {
            "total_optically_thin_luminosity_at_g_equals_one_erg_s": float(np.sum(source)),
            "pieces": source_pieces,
        },
        "same_grid_baseline_reproduction": {
            "maximum_absolute_relative_difference_vs_archived": float(
                np.max(np.abs(archived_reproduction_residual))
            ),
            "mean_absolute_relative_difference_vs_archived": float(
                np.mean(np.abs(archived_reproduction_residual))
            ),
        },
        "analytic_path_vs_reference_path_quadrature": {
            "same_16_gauss_directions": True,
            "tau_relative_residual": path_residual,
            "maximum_luminosity_shift_vs_reference": float(
                np.max(np.abs(exact16_luminosity / baseline_luminosity - 1.0))
            ),
            "mean_luminosity_shift_vs_reference": float(
                np.mean(np.abs(exact16_luminosity / baseline_luminosity - 1.0))
            ),
            "reference_curve_metrics_vs_fig7": curve_metrics(
                baseline_luminosity, fig7_luminosity
            ),
            "analytic_path_curve_metrics_vs_fig7": curve_metrics(
                exact16_luminosity, fig7_luminosity
            ),
            "path_order_convergence": path_convergence,
        },
        "independent_angular_convergence": angular_convergence,
        "adaptive_quadpack_angular_checks": {
            "number_of_checks": len(adaptive_checks),
            "maximum_absolute_relative_difference_vs_simpson": float(
                max(abs(x["relative_difference"]) for x in adaptive_checks)
            ),
            "checks": adaptive_checks,
        },
        "final_independent_result": {
            "angular_rule": final_rule,
            "luminosity_erg_s": final_luminosity.tolist(),
            "escape_fraction": final_escape.tolist(),
            "relative_difference_vs_fig7": (
                final_luminosity / fig7_luminosity - 1.0
            ).tolist(),
            "relative_difference_vs_archived_b16": final_vs_archived.tolist(),
            "curve_metrics_vs_fig7": curve_metrics(final_luminosity, fig7_luminosity),
            "maximum_absolute_luminosity_shift_vs_archived": float(
                np.max(np.abs(final_vs_archived))
            ),
        },
        "elapsed_seconds": float(time.time() - started),
        "limitations": [
            "The path integral is exact only for the piecewise-linear interpolation of the supplied radial reduced-opacity table.",
            "The calculation retains the Euclidean straight-chord geometry of Eq. (B.2); it is not full GR ray tracing.",
            "The local collision kernel and B.1 source measure are shared with the existing benchmark to isolate B.2 propagation.",
            "The reconstructed public-figure profile is not the original Garching simulation table.",
        ],
        "production_axial_outputs_modified": False,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    parser.add_argument("--angular-orders", default="16,32,64")
    parser.add_argument("--simpson-subintervals", default="128,256")
    parser.add_argument("--path-orders", default="8,16,32,64,128")
    args = parser.parse_args()
    result = run(
        args.profile, args.fig7, args.baseline, args.output, args.mass,
        args.nr, args.ne,
        tuple(int(x) for x in args.angular_orders.split(",")),
        tuple(int(x) for x in args.simpson_subintervals.split(",")),
        tuple(int(x) for x in args.path_orders.split(",")),
        args.radius, args.energy_offset,
    )
    print(json.dumps({
        "output": str(args.output),
        "profile_sha256": result["profile"]["sha256"],
        "baseline_reproduction": result["same_grid_baseline_reproduction"],
        "analytic_path": result["analytic_path_vs_reference_path_quadrature"],
        "angular_convergence": result["independent_angular_convergence"],
        "adaptive_quadpack": result["adaptive_quadpack_angular_checks"],
        "final_independent_result": result["final_independent_result"]["curve_metrics_vs_fig7"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
