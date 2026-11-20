#!/usr/bin/env python3
"""A0 finite-mixing axial-vector transport on the C1 radial benchmark.

The B.7 active-neutrino kernel is unchanged from the UV model.  The B.13
moving-muon semi-Compton kernel is evaluated with the actual mass-basis
couplings gV/gX=sin(theta_muR)^2 and gA/gX=-cos(theta_muR)^2.  The common
radial/energy transport engine is reused without changing the pure-vector
C1 default or its archived baseline.

This is an interior-profile diagnostic using the reconstructed SFHo-18.8
profile.  The unavailable 25--100 km semi-Compton opacity is not included.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np

from croon_c1_b13_vector_transport import (
    DEFAULT_PROFILE,
    PROFILE_SHA256,
    R_FAR_KM,
    T_NU_MEV,
    M_MU,
    _compute_mass,
    sample_profile,
    sha256,
)
from finite_mixing.model import muon_couplings, neutrino_couplings

DEFAULT_OUTPUT = Path(__file__).resolve().parent / "outputs" / (
    "croon_a0_uv_axial_transport_10mev_2026-11-20.json"
)
DEFAULT_CSV = Path(__file__).resolve().parent / "outputs" / (
    "croon_a0_uv_axial_transport_10mev_2026-11-20.csv"
)


def compute_a0(
    profile_path: Path = DEFAULT_PROFILE,
    masses: tuple[float, ...] = (10.0,),
    radial_points: int = 101,
    energy_order: int = 32,
    inner_orders: tuple[int, int, int, int] = (12, 8, 8, 8),
    neutrino_order: int = 128,
    susceptibility_order: int = 192,
    coupling_count: int = 121,
    theta_mu_r: float = 1.0e-2,
    include_adaptive_radial: bool = True,
) -> dict:
    """Compute B.7+B.13 transport with the original UV finite-mixing current.

    The scanned coupling is the underlying gauge coupling g_X.  The ratios
    gV/gX and gA/gX are held fixed at the chosen theta_mu_r.  Neutrino
    couplings remain (+gX,-gX), independent of theta_mu_r.
    """
    profile_path = Path(profile_path)
    if sha256(profile_path) != PROFILE_SHA256:
        raise ValueError(
            "A0 is pinned to the reviewed reconstructed SFHo-18.8 profile SHA-256"
        )
    if any(not math.isfinite(float(m)) or float(m) <= 0.0 for m in masses):
        raise ValueError("All mediator masses must be finite and positive")
    threshold = 2.0 * M_MU
    if any(float(m) >= threshold for m in masses):
        raise ValueError(
            f"This A0 transport engine currently covers m_A' < 2 m_mu "
            f"({threshold:.9f} MeV); dimuon inverse decay is not included."
        )
    if coupling_count < 2:
        raise ValueError("coupling_count must be at least 2")

    # Normalize to g_X=1; the returned ratios are the coefficients passed
    # directly to moving_muon_compton_rates in gamma^mu(gV + gA gamma5).
    current = muon_couplings(1.0, float(theta_mu_r))
    g_vector_fraction = current.g_vector
    g_axial_fraction = current.g_axial
    nu_mu_fraction, nu_tau_fraction = neutrino_couplings(1.0)

    profile = sample_profile(profile_path, radial_points)
    g_x_values = np.logspace(-11.0, 0.0, int(coupling_count))
    results: dict[str, dict] = {}
    local_all: list[dict] = []
    for mass in masses:
        item, local_rows = _compute_mass(
            float(mass),
            profile,
            int(energy_order),
            tuple(int(x) for x in inner_orders),
            int(neutrino_order),
            int(susceptibility_order),
            g_x_values,
            muon_current=(g_vector_fraction, g_axial_fraction),
            include_adaptive_radial=bool(include_adaptive_radial),
        )
        results[f"{float(mass):.9g}"] = item
        local_all.extend(local_rows)

    return {
        "title": (
            "A0 finite-mixing axial-vector benchmark: unchanged B.7 neutrinos "
            "plus UV-mixed exact-recoil B.13 moving-muon transport"
        ),
        "status": (
            "A0 interior-profile adaptive-radial transport diagnostic; outer "
            "25--100 km semi-Compton opacity remains unavailable"
            if include_adaptive_radial else
            "A0 interior-profile legacy-Simpson diagnostic; outer 25--100 km "
            "semi-Compton opacity remains unavailable"
        ),
        "source_profile": {
            "path": str(profile_path),
            "sha256": profile["profile_sha256"],
            "rows": profile["source_rows"],
            "R_nu_km_from_T_equals_3_MeV": profile["R_nu_km"],
            "r_mu_last_nonzero_km": profile["r_mu_last_nonzero_km"],
            "r_mu_first_zero_km": profile["r_mu_first_zero_km"],
            "radial_points": len(profile["r_km"]),
        },
        "model": {
            "charged_muon_current": (
                "A'_alpha mu_bar gamma^alpha (gV + gA gamma5) mu"
            ),
            "theta_mu_R": float(theta_mu_r),
            "gV_mu_over_gX": float(g_vector_fraction),
            "gA_mu_over_gX": float(g_axial_fraction),
            "gL_mu_over_gX": float(current.g_left),
            "gR_mu_over_gX": float(current.g_right),
            "neutrino_couplings_over_gX": {
                "nu_mu": float(nu_mu_fraction),
                "nu_tau": float(nu_tau_fraction),
            },
            "muon_targets": (
                "mu_minus and mu_plus separately; charge-conjugated axial "
                "term retained before summing"
            ),
            "mediator_modes": ["L", "+", "-"],
            "dimuon_channel": (
                f"closed for all requested masses below 2*m_mu="
                f"{threshold:.9f} MeV"
            ),
            "coupling_scan": (
                "g_X is scanned; gV/gX and gA/gX are fixed by theta_mu_R"
            ),
        },
        "transport": {
            "volume_element": "4*pi*r^2 dr",
            "optical_depth": (
                "radial integral of reduced absorption Gamma_abs-Gamma_prod, "
                "mode by mode"
            ),
            "radial_luminosity_integrator": (
                "surface-centered PCHIP source and reduced opacity; exact "
                "PCHIP opacity antiderivative; QUADPACK adaptive Gauss-Kronrod "
                "with explicit g_X^2*tau boundary-layer split points"
                if include_adaptive_radial else
                "legacy fixed-grid Simpson; diagnostic only"
            ),
            "angular_escape_average": "omitted to match the C1 radial prescription",
            "lapse_redshift": "omitted to match the C1 comparison convention",
            "R_far_values_km": [profile["R_nu_km"], R_FAR_KM],
            "outer_neutrino_opacity": (
                "unchanged B.7 two-flavour vacuum decay width per mode"
            ),
            "outer_semicompton_opacity": (
                "omitted; no validated 25--100 km muon susceptibility profile"
            ),
        },
        "numerics": {
            "radial_points_requested": int(radial_points),
            "energy_order": int(energy_order),
            "inner_orders": [int(x) for x in inner_orders],
            "neutrino_angular_order": int(neutrino_order),
            "susceptibility_order": int(susceptibility_order),
            "coupling_count": int(coupling_count),
            "coupling_range": [
                float(g_x_values[0]), float(g_x_values[-1])
            ],
            "theta_mu_R": float(theta_mu_r),
            "adaptive_radial_enabled": bool(include_adaptive_radial),
        },
        "comparison_reference": (
            "The retained Croon Eq. (4.7) quantity in each mass record is the "
            "literal mu-minus-only pure-vector reference on the same grid. "
            "It is a diagnostic comparator, not part of the A0 source or opacity."
        ),
        "masses": results,
        "scope": (
            "The A0 calculation keeps the C1 B.7 neutrino rates unchanged and "
            "replaces only the charged-muon B.13 current by the original UV "
            "finite-mixing V-A current. Its accepted luminosity fields use "
            "the surface-centered adaptive radial integrator when enabled; "
            "legacy Simpson fields are retained only as diagnostics. It uses "
            "the reconstructed public SFHo-18.8 profile and does not include "
            "the unavailable outer 25--100 km semi-Compton opacity. It is not "
            "a final SN1987A exclusion curve."
        ),
        "local_profile_rows": local_all,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default=str(DEFAULT_PROFILE))
    parser.add_argument("--masses", nargs="+", type=float, default=[10.0])
    parser.add_argument("--radial-points", type=int, default=101)
    parser.add_argument("--energy-order", type=int, default=32)
    parser.add_argument("--inner-orders", nargs=4, type=int, default=[12, 8, 8, 8])
    parser.add_argument("--neutrino-order", type=int, default=128)
    parser.add_argument("--susceptibility-order", type=int, default=192)
    parser.add_argument("--coupling-count", type=int, default=121)
    parser.add_argument("--theta-mu-r", type=float, default=1.0e-2)
    parser.add_argument(
        "--no-adaptive-radial",
        action="store_false",
        dest="include_adaptive_radial",
        help="Use the legacy fixed-grid Simpson luminosity as a diagnostic",
    )
    parser.set_defaults(include_adaptive_radial=True)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--csv", default=str(DEFAULT_CSV))
    args = parser.parse_args()

    result = compute_a0(
        profile_path=Path(args.profile),
        masses=tuple(args.masses),
        radial_points=args.radial_points,
        energy_order=args.energy_order,
        inner_orders=tuple(args.inner_orders),
        neutrino_order=args.neutrino_order,
        susceptibility_order=args.susceptibility_order,
        coupling_count=args.coupling_count,
        theta_mu_r=args.theta_mu_r,
        include_adaptive_radial=args.include_adaptive_radial,
    )
    output_path = Path(args.output)
    csv_path = Path(args.csv)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    rows = result["local_profile_rows"]
    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle, fieldnames=list(rows[0]), lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps({
        "json": str(output_path),
        "csv": str(csv_path),
        "masses_MeV": args.masses,
        "theta_mu_R": args.theta_mu_r,
        "radial_points": result["source_profile"]["radial_points"],
        "status": result["status"],
        "adaptive_radial_enabled": result["numerics"]["adaptive_radial_enabled"],
    }, indent=2))


if __name__ == "__main__":
    main()
