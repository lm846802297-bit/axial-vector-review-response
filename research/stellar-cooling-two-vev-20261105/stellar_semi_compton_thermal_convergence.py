#!/usr/bin/env python3
"""Reproducible quadrature-order and cutoff study for the thermal semi-Compton rate.

This is a numerical stability diagnostic, not an SN exclusion calculation.
Defaults are intentionally explicit and can be changed from the command line.
The script writes CSV to stdout and progress messages to stderr.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stellar_semi_compton_thermal_rate as thermal


def parse_ints(value: str) -> list[int]:
    try:
        result = [int(x.strip()) for x in value.split(",") if x.strip()]
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if not result or any(x < 2 for x in result):
        raise argparse.ArgumentTypeError("values must be comma-separated integers >= 2")
    return sorted(set(result))


def parse_floats(value: str) -> list[float]:
    try:
        result = [float(x.strip()) for x in value.split(",") if x.strip()]
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if not result or any(not math.isfinite(x) or x <= 0 for x in result):
        raise argparse.ArgumentTypeError("values must be comma-separated positive finite numbers")
    return sorted(set(result))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--temperature", type=float, default=10.0, help="MeV")
    parser.add_argument("--muon-chemical-potential", type=float, default=0.0, help="MeV")
    parser.add_argument("--mass", type=float, default=1.0, help="MeV")
    parser.add_argument("--g-v", type=float, default=0.0)
    parser.add_argument("--g-a", type=float, default=0.01)
    parser.add_argument("--orders", type=parse_ints, default=parse_ints("2,4,6,8,10,12"))
    parser.add_argument("--cutoff-order", type=int, default=6)
    parser.add_argument("--reference-p-max", type=float, default=None,
                        help="reference muon momentum cutoff; default follows thermal_emissivity")
    parser.add_argument("--reference-photon-max", type=float, default=None,
                        help="reference photon cutoff; default follows thermal_emissivity")
    parser.add_argument("--p-cutoffs", type=parse_floats, default=parse_floats("160,200,240"))
    parser.add_argument("--photon-cutoffs", type=parse_floats, default=parse_floats("160,200,240"))
    parser.add_argument("--skip-cutoffs", action="store_true")
    args = parser.parse_args()

    if args.temperature <= 0 or args.mass <= 0 or args.cutoff_order < 2:
        parser.error("temperature, mass and cutoff-order must be positive (order >= 2)")
    if (args.reference_p_max is not None and args.reference_p_max <= 0) or (
        args.reference_photon_max is not None and args.reference_photon_max <= 0
    ):
        parser.error("reference cutoffs must be positive")
    muon_mass = thermal.sc.M_MU_MEV
    p_fermi = math.sqrt(max(args.muon_chemical_potential**2 - muon_mass**2, 0.0))
    p_reference = args.reference_p_max or max(
        12.0 * args.temperature,
        6.0 * math.sqrt(muon_mass * args.temperature),
        p_fermi + 12.0 * args.temperature,
    )
    threshold = args.mass + args.mass**2 / (2.0 * muon_mass)
    photon_reference = args.reference_photon_max or max(
        20.0 * args.temperature, 2.0 * threshold + 10.0 * args.temperature
    )
    cache: dict[tuple[int, float, float], tuple[float, float, int, float]] = {}

    def evaluate(order: int, pmax: float, wmax: float) -> tuple[float, float, int, float]:
        key = (order, float(pmax), float(wmax))
        if key in cache:
            return cache[key]
        start = time.perf_counter()
        result = thermal.thermal_emissivity(
            temperature_mev=args.temperature,
            muon_chemical_potential_mev=args.muon_chemical_potential,
            vector_mass_mev=args.mass,
            g_v=args.g_v,
            g_a=args.g_a,
            order=order,
            p_max_mev=pmax,
            photon_max_mev=wmax,
        )
        elapsed = time.perf_counter() - start
        if not (
            math.isfinite(result.event_rate_mev4)
            and math.isfinite(result.emissivity_mev5)
            and result.event_rate_mev4 > 0.0
            and result.emissivity_mev5 > 0.0
        ):
            raise ArithmeticError(f"Non-finite or non-positive result for {key}: {result}")
        cache[key] = (
            result.event_rate_mev4,
            result.emissivity_mev5,
            result.phi_order,
            elapsed,
        )
        print(
            f"evaluated order={order} pmax={pmax:g} photon_max={wmax:g} "
            f"phi_order={result.phi_order} elapsed={elapsed:.2f}s",
            file=sys.stderr,
            flush=True,
        )
        return cache[key]

    # First hold the physical integration cutoffs fixed and increase quadrature order.
    order_values = []
    for order in args.orders:
        rate, emissivity, phi_order, elapsed = evaluate(order, p_reference, photon_reference)
        order_values.append((order, rate, emissivity, phi_order, elapsed))
    reference_rate = order_values[-1][1]
    reference_emissivity = order_values[-1][2]

    rows: list[dict[str, str | int | float]] = []
    for order, rate, emissivity, phi_order, elapsed in order_values:
        rows.append({
            "study": "order",
            "order": order,
            "p_max_MeV": p_reference,
            "photon_max_MeV": photon_reference,
            "phi_order": phi_order,
            "event_rate_MeV4": rate,
            "emissivity_MeV5": emissivity,
            "relative_rate_to_reference": rate / reference_rate - 1.0,
            "relative_emissivity_to_reference": emissivity / reference_emissivity - 1.0,
            "elapsed_seconds": elapsed,
        })

    if not args.skip_cutoffs:
        # Vary one cutoff at a time around the chosen/default thermal reference.
        order = args.cutoff_order
        base_rate, base_emissivity, _, _ = evaluate(order, p_reference, photon_reference)
        cutoff_points = (
            [(pmax, photon_reference) for pmax in args.p_cutoffs]
            + [(p_reference, wmax) for wmax in args.photon_cutoffs]
        )
        seen: set[tuple[float, float]] = set()
        for pmax, wmax in cutoff_points:
            point = (float(pmax), float(wmax))
            if point in seen:
                continue
            seen.add(point)
            rate, emissivity, phi_order, elapsed = evaluate(order, pmax, wmax)
            rows.append({
                "study": "cutoff",
                "order": order,
                "p_max_MeV": pmax,
                "photon_max_MeV": wmax,
                "phi_order": phi_order,
                "event_rate_MeV4": rate,
                "emissivity_MeV5": emissivity,
                "relative_rate_to_reference": rate / base_rate - 1.0,
                "relative_emissivity_to_reference": emissivity / base_emissivity - 1.0,
                "elapsed_seconds": elapsed,
            })

    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=[
            "study", "order", "p_max_MeV", "photon_max_MeV", "phi_order",
            "event_rate_MeV4", "emissivity_MeV5",
            "relative_rate_to_reference", "relative_emissivity_to_reference",
            "elapsed_seconds",
        ],
    )
    writer.writeheader()
    writer.writerows(rows)


if __name__ == "__main__":
    main()
