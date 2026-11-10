#!/usr/bin/env python3
"""EOS-consistent nucleon occupations and degeneracy factors for Garching SFHo.

The implementation follows Fiorillo et al., arXiv:2509.13322v2,
Appendix C.1, Eqs. (81)-(82), and Sec. 4.3, Eq. (41).
It deliberately does not modify the existing ideal-gas response or transport code.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import expit

HBARC_MEV_FM = 197.3269804
NEUTRON_MASS_MEV = 939.565346
PROTON_MASS_MEV = 938.272013
MASS_SPLITTING_MEV = NEUTRON_MASS_MEV - PROTON_MASS_MEV
TABLE_TARGETS = {
    "T3": {"p": 0.80, "n": 0.48},
    "rhoT52": {"p": 0.77, "n": 0.42},
}
HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class NucleonEOSState:
    """One local EOS state; mu_star excludes the nucleon rest mass."""

    species: str
    temperature_mev: float
    effective_mass_mev: float
    scalar_potential_mev: float
    chemical_potential_star_mev: float

    def validate(self) -> None:
        values = (
            self.temperature_mev,
            self.effective_mass_mev,
            self.scalar_potential_mev,
            self.chemical_potential_star_mev,
        )
        if self.species not in ("n", "p"):
            raise ValueError("species must be 'n' or 'p'")
        if not all(math.isfinite(float(value)) for value in values):
            raise ValueError("EOS state contains a non-finite value")
        if self.temperature_mev <= 0.0:
            raise ValueError("temperature must be positive")
        if self.effective_mass_mev <= 0.0:
            raise ValueError("effective mass must be positive")

    @property
    def effective_chemical_potential_mev(self) -> float:
        # U and mu_star enter the occupation only through this difference.
        return self.chemical_potential_star_mev - self.scalar_potential_mev


def candidate_state_from_hs_spp(
    species: str,
    temperature_mev: float,
    effective_mass_mev: float,
    total_vector_self_energy_mev: float,
    chemical_potential_nonrel_mev: float,
) -> NucleonEOSState:
    """Map Hempel SFHo single-particle table fields to the Fiorillo convention.

    Assumption to be tested against the Garching tabulated U_N:
      E_N(p) = sqrt(p^2 + m_star^2) + Sigma_V,N^tot
      mu_N^nonrel = mu_N - m_N

    Then U_N = m_star - m_N + Sigma_V,N^tot and mu_N^* = mu_N^nonrel.
    The excluded-volume filling factor xi remains a separate input; it is
    never absorbed into U_N or mu_N^*.
    """
    if species == "n":
        vacuum_mass = NEUTRON_MASS_MEV
    elif species == "p":
        vacuum_mass = PROTON_MASS_MEV
    else:
        raise ValueError("species must be 'n' or 'p'")
    potential = (
        effective_mass_mev - vacuum_mass + total_vector_self_energy_mev
    )
    return NucleonEOSState(
        species=species,
        temperature_mev=temperature_mev,
        effective_mass_mev=effective_mass_mev,
        scalar_potential_mev=potential,
        chemical_potential_star_mev=chemical_potential_nonrel_mev,
    )


@lru_cache(maxsize=16)
def _legendre_rule(order: int):
    x, w = leggauss(order)
    x.setflags(write=False)
    w.setflags(write=False)
    return x, w


def kinetic_energy_mev(momentum_mev, effective_mass_mev: float):
    """K(p) = sqrt(p^2 + m_star^2) - m_star."""
    if effective_mass_mev <= 0.0:
        raise ValueError("effective mass must be positive")
    p = np.asarray(momentum_mev, dtype=float)
    return np.hypot(p, effective_mass_mev) - effective_mass_mev


def occupation(momentum_mev, state: NucleonEOSState):
    """Fermi occupation per spin state, evaluated with a stable logistic."""
    state.validate()
    kinetic = kinetic_energy_mev(momentum_mev, state.effective_mass_mev)
    return expit(
        (state.effective_chemical_potential_mev - kinetic)
        / state.temperature_mev
    )


def _momentum_quadrature(
    state: NucleonEOSState, order: int = 512, tail_T: float = 45.0
):
    state.validate()
    if order < 32:
        raise ValueError("quadrature order must be at least 32")
    if tail_T < 20.0:
        raise ValueError("tail_T must be >= 20 to control the Fermi tail")
    nu = state.effective_chemical_potential_mev
    mstar = state.effective_mass_mev
    kmax = max(nu, 0.0) + tail_T * state.temperature_mev
    pmax = math.sqrt(kmax * (kmax + 2.0 * mstar))
    x, w = _legendre_rule(order)
    p = 0.5 * pmax * (x + 1.0)
    wp = 0.5 * pmax * w
    return p, wp


def phase_space_integrals(
    state: NucleonEOSState, order: int = 512, tail_T: float = 45.0
):
    """Return (n_prime, n_prime_blocked) in MeV^3, including spin degeneracy g_s=2.
    n_prime is the nucleon density per available volume V', not per total volume V.

    n_prime = 2 int d^3p/(2 pi)^3 f(p)
    n_prime_blocked = 2 int d^3p/(2 pi)^3 f(p) [1-f(p)]
    """
    p, wp = _momentum_quadrature(state, order, tail_T)
    f = occupation(p, state)
    measure = wp * p * p / math.pi**2
    number_mev3 = float(np.sum(measure * f))
    blocked_mev3 = float(np.sum(measure * f * (1.0 - f)))
    return number_mev3, blocked_mev3


def number_density_fm3(
    state: NucleonEOSState, order: int = 512, tail_T: float = 45.0
) -> float:
    """Return n'_N in fm^-3, i.e. density per nucleon-available volume V'."""
    number_mev3, _ = phase_space_integrals(state, order, tail_T)
    return number_mev3 / HBARC_MEV_FM**3


def degeneracy_factor(
    state: NucleonEOSState, order: int = 512, tail_T: float = 45.0
) -> float:
    """F_NN^deg = int f(1-f) / int f; spin degeneracy cancels."""
    number_mev3, blocked_mev3 = phase_space_integrals(state, order, tail_T)
    if number_mev3 <= 0.0:
        raise ArithmeticError("number density underflowed to zero")
    return blocked_mev3 / number_mev3


def degeneracy_factor_from_density_derivative(
    state: NucleonEOSState,
    order: int = 512,
    tail_T: float = 45.0,
    step_fraction: float = 2.0e-4,
) -> float:
    """Independent finite-difference check of F = T/n_prime * partial n_prime/partial nu.

    The derivative is taken at fixed T, m_star, and U. Since nu=mu_star-U,
    varying mu_star at fixed U is equivalent to varying nu.
    """
    state.validate()
    if step_fraction <= 0.0:
        raise ValueError("step_fraction must be positive")
    h = step_fraction * state.temperature_mev
    plus = NucleonEOSState(
        state.species,
        state.temperature_mev,
        state.effective_mass_mev,
        state.scalar_potential_mev,
        state.chemical_potential_star_mev + h,
    )
    minus = NucleonEOSState(
        state.species,
        state.temperature_mev,
        state.effective_mass_mev,
        state.scalar_potential_mev,
        state.chemical_potential_star_mev - h,
    )
    n0, _ = phase_space_integrals(state, order, tail_T)
    n_plus, _ = phase_space_integrals(plus, order, tail_T)
    n_minus, _ = phase_space_integrals(minus, order, tail_T)
    return (
        state.temperature_mev
        * (n_plus - n_minus)
        / (2.0 * h * n0)
    )


def _state_from_row(row, species: str) -> NucleonEOSState:
    return NucleonEOSState(
        species=species,
        temperature_mev=float(row["T_MeV"]),
        effective_mass_mev=float(row[f"mstar_{species}_MeV"]),
        scalar_potential_mev=float(row[f"U_{species}_MeV"]),
        chemical_potential_star_mev=float(row[f"mu_star_{species}_MeV"]),
    )


def aggregate_profile_rows(
    rows, order: int = 512, tail_T: float = 45.0
):
    """Compute local Fdeg and Fiorillo's two dM dt weighted averages.

    Required CSV columns:
      T_MeV, rho_g_cm3, dMdt_weight, xi,
      mstar_n_MeV, U_n_MeV, mu_star_n_MeV,
      mstar_p_MeV, U_p_MeV, mu_star_p_MeV.

    Optional columns:
      n_n_target_fm3, n_p_target_fm3.

    xi=V'/V is the nucleon filling factor. The momentum integral gives n'_N
    per available volume V'; the density per total volume is n_N=xi*n'_N.
    dMdt_weight is the cell measure Delta M * Delta t (or the equivalent
    quadrature measure in mass coordinate and time). It is not silently
    replaced by equal row weights. The published averages omit lapse/redshift.
    """
    rows = list(rows)
    if not rows:
        raise ValueError("profile contains no rows")

    local_rows = []
    sums = {
        kind: {
            species: {"weighted_F": 0.0, "weight": 0.0}
            for species in ("p", "n")
        }
        for kind in ("T3", "rhoT52")
    }
    density_residuals = {"p": [], "n": []}
    mass_split_residuals = []

    for index, row in enumerate(rows):
        temperature = float(row["T_MeV"])
        rho = float(row["rho_g_cm3"])
        cell_measure = float(row["dMdt_weight"])
        xi = float(row["xi"])
        if temperature <= 0.0 or rho <= 0.0 or cell_measure <= 0.0 or not (0.0 < xi <= 1.0):
            raise ValueError(
                f"non-positive T/rho/dMdt_weight in profile row {index}"
            )

        local = {
            "row": index,
            "T_MeV": temperature,
            "rho_g_cm3": rho,
            "dMdt_weight": cell_measure,
            "Fdeg": {},
            "xi": xi,
            "nprime_fm3": {},
            "n_actual_fm3": {},
            "mu_eff_MeV": {},
        }
        states = {}
        for species in ("n", "p"):
            state = _state_from_row(row, species)
            states[species] = state
            number_mev3, blocked_mev3 = phase_space_integrals(
                state, order, tail_T
            )
            if number_mev3 <= 0.0:
                raise ArithmeticError(
                    f"zero {species} density in profile row {index}"
                )
            density_prime = number_mev3 / HBARC_MEV_FM**3
            density_actual = xi * density_prime
            fdeg = blocked_mev3 / number_mev3
            local["Fdeg"][species] = fdeg
            local["nprime_fm3"][species] = density_prime
            local["n_actual_fm3"][species] = density_actual
            local["mu_eff_MeV"][species] = (
                state.effective_chemical_potential_mev
            )

            target_key = f"n_{species}_target_fm3"
            if target_key in row and row[target_key] not in ("", None):
                target_density = float(row[target_key])
                if target_density <= 0.0:
                    raise ValueError(
                        f"non-positive {target_key} in profile row {index}"
                    )
                residual = abs(density_actual / target_density - 1.0)
                density_residuals[species].append(residual)
                local.setdefault(
                    "density_closure_relative_residual", {}
                )[species] = residual

            weights = {
                "T3": cell_measure * temperature**3,
                "rhoT52": cell_measure * rho * temperature**2.5,
            }
            for kind, weight in weights.items():
                sums[kind][species]["weighted_F"] += weight * fdeg
                sums[kind][species]["weight"] += weight

        mass_split_residuals.append(
            abs(
                states["n"].effective_mass_mev
                - states["p"].effective_mass_mev
                - MASS_SPLITTING_MEV
            )
        )
        local["mstar_n_minus_p_MeV"] = (
            states["n"].effective_mass_mev
            - states["p"].effective_mass_mev
        )
        local_rows.append(local)

    global_averages = {
        kind: {
            species: (
                sums[kind][species]["weighted_F"]
                / sums[kind][species]["weight"]
            )
            for species in ("p", "n")
        }
        for kind in ("T3", "rhoT52")
    }
    comparison = {
        kind: {
            species: {
                "computed": global_averages[kind][species],
                "published": TABLE_TARGETS[kind][species],
                "difference": (
                    global_averages[kind][species]
                    - TABLE_TARGETS[kind][species]
                ),
            }
            for species in ("p", "n")
        }
        for kind in ("T3", "rhoT52")
    }
    return {
        "source": "Fiorillo et al., arXiv:2509.13322v2, Sec. 4.3 and App. C.1",
        "weighting": "integral dM dt; no gravitational redshift/lapse",
        "quadrature": {"order": order, "tail_T": tail_T},
        "number_of_profile_cells": len(rows),
        "global_averages": global_averages,
        "comparison_to_Fiorillo_Table1": comparison,
        "max_relative_density_closure_residual": {
            species: (
                max(density_residuals[species])
                if density_residuals[species]
                else None
            )
            for species in ("p", "n")
        },
        "max_effective_mass_splitting_residual_MeV": max(
            mass_split_residuals
        ),
        "local_rows": local_rows,
    }


def load_profile_csv(path: Path):
    with path.open("r", newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        required = {
            "T_MeV",
            "rho_g_cm3",
            "dMdt_weight",
            "xi",
            "mstar_n_MeV",
            "U_n_MeV",
            "mu_star_n_MeV",
            "mstar_p_MeV",
            "U_p_MeV",
            "mu_star_p_MeV",
        }
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(
                "profile CSV is missing required columns: "
                + ", ".join(sorted(missing))
            )
        return list(reader)


def self_test_payload():
    """Deterministic software fixtures only; these are not Garching data."""
    states = (
        NucleonEOSState("n", 3.03, 650.0, -45.0, 38.0),
        NucleonEOSState("p", 3.03, 648.706667, -40.0, 25.0),
        NucleonEOSState("n", 12.0, 700.0, -25.0, 18.0),
        NucleonEOSState("p", 12.0, 698.706667, -20.0, 8.0),
    )
    cases = []
    for state in states:
        direct = degeneracy_factor(state, order=512)
        derivative = degeneracy_factor_from_density_derivative(
            state, order=512
        )
        coarse = degeneracy_factor(state, order=256)
        cases.append(
            {
                "species": state.species,
                "T_MeV": state.temperature_mev,
                "mstar_MeV": state.effective_mass_mev,
                "U_MeV": state.scalar_potential_mev,
                "mu_star_MeV": state.chemical_potential_star_mev,
                "mu_eff_MeV": state.effective_chemical_potential_mev,
                "nprime_fm3": number_density_fm3(state, order=512),
                "Fdeg_direct": direct,
                "Fdeg_from_density_derivative": derivative,
                "derivative_identity_abs_residual": abs(direct - derivative),
                "Fdeg_order_256": coarse,
                "Fdeg_order_512": direct,
                "quadrature_abs_difference_256_512": abs(direct - coarse),
            }
        )

    mass = 939.56542052
    temperature = 3.03
    mu_total = 935.0
    vacuum_state = NucleonEOSState(
        "n", temperature, mass, 0.0, mu_total - mass
    )
    momenta = np.linspace(0.0, 1000.0, 101)
    vacuum_expected = expit(
        (mu_total - np.hypot(momenta, mass)) / temperature
    )
    vacuum_residual = float(
        np.max(np.abs(occupation(momenta, vacuum_state) - vacuum_expected))
    )

    dilute_state = NucleonEOSState("n", 10.0, 700.0, 25.0, -975.0)
    dilute_fdeg = degeneracy_factor(dilute_state, order=512)

    shifted_state = NucleonEOSState("n", 5.0, 650.0, 103.0, 193.0)
    reference_state = NucleonEOSState("n", 5.0, 650.0, -20.0, 70.0)
    potential_shift_residual = abs(
        degeneracy_factor(shifted_state, order=512)
        - degeneracy_factor(reference_state, order=512)
    )

    return {
        "title": "Garching EOS nucleon occupation kernel software self-test",
        "date": "2026-11-11",
        "software_test_only": True,
        "not_garching_profile_data": True,
        "quadrature": {"coarse_order": 256, "fine_order": 512, "tail_T": 45.0},
        "synthetic_local_states": cases,
        "checks": {
            "max_derivative_identity_abs_residual": max(
                case["derivative_identity_abs_residual"] for case in cases
            ),
            "max_256_vs_512_quadrature_abs_difference": max(
                case["quadrature_abs_difference_256_512"] for case in cases
            ),
            "vacuum_mass_limit_max_occupation_abs_residual": vacuum_residual,
            "dilute_limit_Fdeg": dilute_fdeg,
            "common_U_mu_shift_Fdeg_abs_residual": potential_shift_residual,
        },
        "published_global_targets_not_tested_without_profiles": TABLE_TARGETS,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile-csv", type=Path)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--order", type=int, default=512)
    args = parser.parse_args()

    if args.self_test == (args.profile_csv is not None):
        parser.error("provide exactly one of --self-test or --profile-csv")

    if args.self_test:
        payload = self_test_payload()
        default_output = (
            HERE / "outputs" / "p1iii_eos_kernel_self_test_2026-11-11.json"
        )
    else:
        rows = load_profile_csv(args.profile_csv)
        payload = aggregate_profile_rows(rows, order=args.order)
        default_output = (
            HERE / "outputs" / "p1iii_eos_degeneracy_profile_2026-11-11.json"
        )

    output = args.output or default_output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(output),
                "software_test_only": payload.get("software_test_only", False),
                "number_of_profile_cells": payload.get(
                    "number_of_profile_cells"
                ),
                "checks": payload.get("checks"),
                "global_averages": payload.get("global_averages"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
