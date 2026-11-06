"""Quantify the B.17 charge-conjugate muon susceptibility convention.

B.17 prints a single 2-spin susceptibility integral. The existing transport
implementation includes both mu- and mu+ distributions. This script computes
the two contributions independently with adaptive quadrature and compares
their sum with transport.effective_muon_density. It does not decide which
charge convention the paper intended and does not modify production code.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import expit

from transport import M_MU, effective_muon_density

HERE = Path(__file__).resolve().parent
DEFAULT_PROFILE = HERE / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "vector_audit" / "muon_susceptibility_charge_audit.json"
RADII_KM = (0.0, 5.0, 8.0, 10.0, 15.0, 20.0, 25.0)


def one_charge_susceptibility(temperature, chemical_potential):
    """Return 2 int d^3p/(2pi)^3 f(1-f), in MeV^3, for one charge."""
    def integrand(momentum):
        energy = np.hypot(momentum, M_MU)
        occupation = expit((chemical_potential - energy) / temperature)
        return momentum**2 * occupation * (1.0 - occupation)

    integral = quad(
        integrand, 0.0, np.inf, epsabs=1e-12, epsrel=2e-11, limit=300
    )[0]
    return integral / np.pi**2


def significant(value, digits=8):
    """Stable JSON precision without implying more profile precision."""
    return float(f"{float(value):.{digits}g}")


def build_audit(profile_path):
    profile = np.genfromtxt(profile_path, delimiter=",", names=True)
    radii = np.asarray(RADII_KM)
    temperature = np.interp(radii, profile["r_km"], profile["T_MeV"])
    mu_mu = np.interp(radii, profile["r_km"], profile["mu_mu_MeV"])
    code_total = effective_muon_density(temperature, mu_mu, order=100)

    points = []
    for radius, temp, mu, code_value in zip(radii, temperature, mu_mu, code_total):
        n_minus = one_charge_susceptibility(temp, +mu)
        n_plus = one_charge_susceptibility(temp, -mu)
        total = n_minus + n_plus
        points.append({
            "r_km": significant(radius),
            "T_MeV": significant(temp),
            "mu_mu_MeV": significant(mu),
            "n_mu_minus_eff_MeV3": significant(n_minus),
            "n_mu_plus_eff_MeV3": significant(n_plus),
            "n_both_charges_eff_MeV3": significant(total),
            "n_plus_over_n_minus": significant(n_plus / n_minus),
            "n_plus_fraction_of_both": significant(n_plus / total),
            "transport_gauss_total_MeV3": significant(code_value),
            "transport_relative_difference_vs_adaptive_quad": significant(
                code_value / total - 1.0
            ),
        })

    return {
        "title": "B.17 charge-conjugate muon susceptibility audit",
        "profile": profile_path.name,
        "method": (
            "Independent adaptive quadrature of 2 int d^3p/(2pi)^3 f(1-f) "
            "for mu- at +mu_mu and mu+ at -mu_mu; compare their sum with "
            "transport.effective_muon_density (100-point Gauss-Legendre)."
        ),
        "interpretation": (
            "The printed B.17 notation does not explicitly state whether the "
            "charge-conjugate muon species is included. The current code includes "
            "both. This audit quantifies that convention but does not infer the "
            "authors' intended convention or change the production implementation."
        ),
        "points": points,
    }


def compare_records(actual, reference, path="$"):
    """Compare JSON records numerically, allowing only output-rounding noise."""
    if isinstance(actual, dict) and isinstance(reference, dict):
        if actual.keys() != reference.keys():
            raise AssertionError(f"JSON keys differ at {path}")
        for key in actual:
            compare_records(actual[key], reference[key], f"{path}.{key}")
    elif isinstance(actual, list) and isinstance(reference, list):
        if len(actual) != len(reference):
            raise AssertionError(f"JSON list lengths differ at {path}")
        for index, (a, b) in enumerate(zip(actual, reference)):
            compare_records(a, b, f"{path}[{index}]")
    elif isinstance(actual, (int, float)) and isinstance(reference, (int, float)):
        if not np.isclose(actual, reference, rtol=2e-8, atol=1e-300):
            raise AssertionError(f"Numerical mismatch at {path}: {actual} != {reference}")
    elif actual != reference:
        raise AssertionError(f"Value mismatch at {path}: {actual!r} != {reference!r}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true",
                        help="compare the regenerated result with the saved JSON")
    args = parser.parse_args()
    result = build_audit(args.profile)
    if args.check:
        reference = json.loads(args.output.read_text(encoding="utf-8"))
        compare_records(result, reference)
        print(f"Validated saved audit {args.output}")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        for point in result["points"]:
            print(
                f"r={point['r_km']:>4} km: "
                f"mu+/mu-={point['n_plus_over_n_minus']:.4g}, "
                f"mu+ fraction={point['n_plus_fraction_of_both']:.4g}, "
                f"Gauss-vs-quad={point['transport_relative_difference_vs_adaptive_quad']:.3g}"
            )
        print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
