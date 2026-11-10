#!/usr/bin/env python3
"""Momentum-transfer support audit for high-energy neutrino daughters.

The free-nucleon kernel is imported from the preceding Horowitz audit. This
script measures how much of its total, angular-transport, and energy-loss
moments lies below selected spatial momentum-transfer cuts q.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from audit_b16_p1i_horowitz_transport_moments import (
    GF_MEV,
    MASS,
    horowitz_form_factors,
)

ENERGIES = (100.0, 150.0, 255.0, 500.0)
TARGETS = ("n", "p")
SPECIES = (("nu", False), ("antinu", True))
QCUTS = (30.0, 100.0, 200.0, 300.0)


def lower_cosine_for_qcut(energy: float, mass: float, qcut: float) -> float:
    """Solve q_spatial(x)=qcut; q is monotone in y=1-x."""
    e = energy / mass

    def q2_from_y(y: float) -> float:
        return energy**2 * (y * (2.0 + e * (e + 2.0) * y)) / (1.0 + e * y)**2

    q_max = math.sqrt(q2_from_y(2.0))
    if qcut >= q_max:
        return -1.0
    if qcut <= 0.0:
        return 1.0

    lo, hi = 0.0, 2.0
    target = qcut * qcut
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if q2_from_y(mid) < target:
            lo = mid
        else:
            hi = mid
    return 1.0 - 0.5 * (lo + hi)


def differential_dsigma_dx(
    energy: float, target: str, antinu: bool, x: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    mass = MASS[target]
    e = energy / mass
    eta = 1.0 / (1.0 + e * (1.0 - x))
    q2 = 2.0 * energy**2 * eta * (1.0 - x)
    cv, ca, f2 = horowitz_form_factors(q2, target, mass)
    sign = -1.0 if antinu else 1.0
    brace = (
        cv**2 * (1.0 + eta**2 - eta * (1.0 - x))
        + ca**2 * (1.0 + eta**2 + eta * (1.0 - x))
        + sign * 2.0 * ca * (cv + f2) * (1.0 - eta**2)
        + eta**2 * e**2 / 2.0 * (1.0 - x)
        * (f2**2 * (3.0 - x) + 4.0 * cv * f2 * (1.0 - x))
    )
    dsdo = GF_MEV**2 * energy**2 / (4.0 * math.pi**2) * eta**2 * brace
    return 2.0 * math.pi * dsdo, eta


def q_support(
    energy: float,
    target: str,
    antinu: bool,
    qcuts: tuple[float, ...],
    nodes: np.ndarray,
    weights: np.ndarray,
) -> dict:
    mass = MASS[target]
    x_full = nodes
    ds_full, eta_full = differential_dsigma_dx(energy, target, antinu, x_full)
    moments_full = {
        "total": np.ones_like(x_full),
        "angular_transport": 1.0 - x_full,
        "momentum_transfer": 1.0 - eta_full * x_full,
        "energy_loss": 1.0 - eta_full,
    }
    denominators = {
        name: float(np.sum(weights * ds_full * moment))
        for name, moment in moments_full.items()
    }

    result = {}
    for qcut in qcuts:
        x_min = lower_cosine_for_qcut(energy, mass, qcut)
        if x_min <= -1.0:
            result[qcut] = {name: 1.0 for name in denominators}
            continue
        if x_min >= 1.0:
            result[qcut] = {name: 0.0 for name in denominators}
            continue

        x_local = 0.5 * (1.0 - x_min) * nodes + 0.5 * (1.0 + x_min)
        w_local = 0.5 * (1.0 - x_min) * weights
        ds_local, eta_local = differential_dsigma_dx(
            energy, target, antinu, x_local
        )
        moments_local = {
            "total": np.ones_like(x_local),
            "angular_transport": 1.0 - x_local,
            "momentum_transfer": 1.0 - eta_local * x_local,
            "energy_loss": 1.0 - eta_local,
        }
        result[qcut] = {
            name: float(
                np.sum(w_local * ds_local * moments_local[name])
                / denominators[name]
            )
            for name in denominators
        }
    return result


def build_payload() -> dict:
    nodes400, weights400 = leggauss(400)
    nodes800, weights800 = leggauss(800)
    rows = []
    for energy in ENERGIES:
        for target in TARGETS:
            for species, antinu in SPECIES:
                fractions = q_support(
                    energy, target, antinu, QCUTS, nodes400, weights400
                )
                for qcut in QCUTS:
                    item = fractions[qcut]
                    rows.append({
                        "E_MeV": energy,
                        "target": target,
                        "species": species,
                        "qcut_MeV": qcut,
                        "fraction_total": round(item["total"], 6),
                        "fraction_angular_transport": round(
                            item["angular_transport"], 6
                        ),
                        "fraction_energy_loss": round(item["energy_loss"], 6),
                    })

    max_difference = 0.0
    convergence_cases = (
        (100.0, "n", False),
        (255.0, "n", False),
        (500.0, "n", False),
        (500.0, "n", True),
        (500.0, "p", True),
    )
    for energy, target, antinu in convergence_cases:
        low = q_support(
            energy, target, antinu, QCUTS, nodes400, weights400
        )
        high = q_support(
            energy, target, antinu, QCUTS, nodes800, weights800
        )
        for qcut in QCUTS:
            for moment in (
                "total", "angular_transport", "momentum_transfer", "energy_loss"
            ):
                max_difference = max(
                    max_difference,
                    abs(low[qcut][moment] - high[qcut][moment]),
                )

    return {
        "title": "Momentum-transfer support of Horowitz high-energy free-nucleon daughter-scattering kernel",
        "date": "2026-11-10",
        "reference": (
            "Horowitz, PRD 65, 043001 (2002), Eqs. (12)-(17), Appendix II; "
            "compare Reddy et al. (1999) and Bedaque et al. (2018) response domains"
        ),
        "method": {
            "target": "initially stationary free proton or neutron",
            "spatial_momentum_transfer": (
                "q=sqrt(E^2+Eprime^2-2*E*Eprime*cos(theta))"
            ),
            "outgoing_energy": (
                "Eprime=E/[1+(E/M)*(1-cos(theta))]"
            ),
            "cross_section": (
                "Horowitz exact recoil/weak-magnetism neutral-current differential "
                "cross section with finite-size form factors"
            ),
            "fractions": {
                "total": "integral_{q<qcut} d sigma / integral d sigma",
                "angular_transport": (
                    "integral_{q<qcut} (1-cos(theta)) d sigma / "
                    "integral (1-cos(theta)) d sigma"
                ),
                "energy_loss": (
                    "integral_{q<qcut} (1-Eprime/E) d sigma / "
                    "integral (1-Eprime/E) d sigma"
                ),
            },
            "qcuts_MeV": list(QCUTS),
            "quadrature": (
                "Boundary-resolved Gauss-Legendre integration; 400 nodes per interval"
            ),
        },
        "rows": rows,
        "validation": {
            "max_relative_difference_400_vs_800_nodes": max_difference
        },
        "interpretation": (
            "These are kinematic support fractions, not collision probabilities "
            "or medium-response correction factors. The stationary-target "
            "approximation excludes nucleon thermal motion, Pauli blocking, "
            "and correlations."
        ),
    }


def main() -> None:
    payload = build_payload()
    output = (
        Path(__file__).resolve().parent
        / "outputs"
        / "p1i_momentum_transfer_support_2026-11-10.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output),
        "validation": payload["validation"],
        "E500_neutron_rows": [
            row for row in payload["rows"]
            if row["E_MeV"] == 500.0 and row["target"] == "n"
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
