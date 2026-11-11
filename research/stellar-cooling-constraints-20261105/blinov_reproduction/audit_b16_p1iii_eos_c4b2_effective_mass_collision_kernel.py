#!/usr/bin/env python3
"""C4-B2: EOS-effective-mass moving-nucleon weak collision kernel."""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import expit

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_full_radial_occupation import load_c2_reference

HERE = Path(__file__).resolve().parent
OLD_PATH = HERE/"audit_b16_p1iii_b_moving_fermi_gas_collision_kernel.py"
_SPEC = importlib.util.spec_from_file_location("c4b2_legacy_moving_kernel", OLD_PATH)
legacy = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(legacy)
kernel = legacy.kernel

HBARC = legacy.HBARC
GF = legacy.GF
MASS = legacy.MASS
N0 = legacy.N0
SPECIES = ("n", "p")
PROFILE_INDICES = (0, 96, 196, 300)
INCIDENT_ENERGY = 100.0
COS_THETA = -0.5
LOCAL_HALF_WINDOW = 60.0
TAIL_T = 45.0


def pmax_eos(mstar: float, nu: float, temperature: float) -> float:
    emax = mstar+max(nu, 0.0)+TAIL_T*temperature
    return math.sqrt(emax*emax-mstar*mstar)


def precompute_eos(
    E: float,
    Ep: float,
    costh: float,
    target: str,
    antinu: bool,
    mstar: float,
) -> dict:
    m_vac = MASS[target]
    sint = math.sqrt(max(0.0, 1.0-costh*costh))
    k = np.asarray([E, 0.0, 0.0, E])
    kp = np.asarray([Ep, Ep*sint, 0.0, Ep*costh])
    q = k-kp
    qvec = q[1:]
    qmag = float(np.linalg.norm(qvec))
    q0 = float(q[0])
    if qmag <= 0.0:
        raise ValueError("zero momentum transfer is outside the collision-kernel grid")
    qhat = qvec/qmag
    khat = k[1:]/E
    e1 = khat-np.dot(khat, qhat)*qhat
    norm = float(np.linalg.norm(e1))
    if norm < 1e-12:
        e1 = np.asarray([0.0, 1.0, 0.0])
    else:
        e1 = e1/norm
    e2 = np.cross(qhat, e1)
    Q2 = qmag*qmag-q0*q0
    if Q2 < -1e-10:
        raise ValueError("spacelike transfer required for this scattering kernel")
    f1, ga, f2 = kernel.ff(max(Q2, 0.0), target, m_vac)
    vertex = []
    for mu in range(4):
        pauli = sum(
            kernel.SIGMA[mu][alpha]*kernel.METRIC[alpha]*q[alpha]
            for alpha in range(4)
        )
        vertex.append(
            f1*kernel.GAMMA[mu]
            +1j*f2/(2.0*m_vac)*pauli
            -ga*kernel.GAMMA[mu]@kernel.GAMMA5
        )
    barred = [kernel.dbar(g) for g in vertex]
    first, second = (
        (kernel.slash(k), kernel.slash(kp))
        if antinu else (kernel.slash(kp), kernel.slash(k))
    )
    L = np.asarray([
        [
            np.trace(
                first@(kernel.METRIC[mu]*kernel.GAMMA[mu])
                @(kernel.IDENT-kernel.GAMMA5)
                @second@(kernel.METRIC[alpha]*kernel.GAMMA[alpha])
                @(kernel.IDENT-kernel.GAMMA5)
            )
            for alpha in range(4)
        ]
        for mu in range(4)
    ])
    return {
        "mstar": mstar,
        "m_vac": m_vac,
        "q0": q0,
        "qmag": qmag,
        "qhat": qhat,
        "e1": e1,
        "e2": e2,
        "qvec": qvec,
        "vertex": vertex,
        "barred": barred,
        "L": L,
    }


def contract_moving_eos(pre: dict, p: float, phi: float) -> float:
    mstar = pre["mstar"]
    q0, qmag = pre["q0"], pre["qmag"]
    ei = math.sqrt(p*p+mstar*mstar)
    cosine = (
        (2.0*ei*q0+q0*q0-qmag*qmag)/(2.0*p*qmag)
        if p > 1e-14 else 0.0
    )
    if abs(cosine) > 1.0+2e-10:
        return 0.0
    cosine = max(-1.0, min(1.0, cosine))
    sine = math.sqrt(max(0.0, 1.0-cosine*cosine))
    pvec = p*(
        cosine*pre["qhat"]
        +sine*(math.cos(phi)*pre["e1"]+math.sin(phi)*pre["e2"])
    )
    ppvec = pvec+pre["qvec"]
    ef = ei+q0
    pp_shell = math.sqrt(float(ppvec@ppvec)+mstar*mstar)
    if abs(pp_shell-ef) > 2e-9*max(1.0, ef):
        raise ArithmeticError("EOS moving-kernel energy-shell closure failed")
    pi = np.asarray([ei, *pvec])
    pf = np.asarray([ef, *ppvec])
    Si = kernel.slash(pi)+mstar*kernel.IDENT
    Sf = kernel.slash(pf)+mstar*kernel.IDENT
    A = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        left = pre["vertex"][mu]@Si
        for alpha in range(4):
            A += pre["L"][mu, alpha]*(left@pre["barred"][alpha])
    return float((0.5*np.trace(Sf@A)).real)


def differential_rate_eos(
    E: float,
    Ep: float,
    costh: float,
    target: str,
    antinu: bool,
    temperature: float,
    nu: float,
    mstar: float,
    *,
    order_p: int = 48,
    order_phi: int = 16,
    pauli: bool = True,
) -> float:
    pre = precompute_eos(E, Ep, costh, target, antinu, mstar)
    q, q0 = pre["qmag"], pre["q0"]
    if q <= abs(q0) or q <= 0.0:
        return 0.0
    lo = legacy.pmin_rel(q0, q, mstar)
    hi = pmax_eos(mstar, nu, temperature)
    if lo >= hi:
        return 0.0
    x, w = leggauss(order_p)
    ps = 0.5*(hi-lo)*(x+1.0)+lo
    wp = 0.5*(hi-lo)*w
    phis = 2.0*math.pi*(np.arange(order_phi)+0.5)/order_phi
    integral = 0.0
    for p, weight in zip(ps, wp):
        ei = math.sqrt(p*p+mstar*mstar)
        ef = ei+q0
        fi = expit((nu-(ei-mstar))/temperature)
        block = (
            1.0-expit((nu-(ef-mstar))/temperature)
            if pauli else 1.0
        )
        if fi < 1e-300 or block < 1e-15:
            continue
        azimuthal = sum(
            contract_moving_eos(pre, float(p), float(phi)) for phi in phis
        )/order_phi
        integral += weight*p/ei*fi*block*azimuthal
    return GF**2*Ep/(256.0*math.pi**4*E*q)*integral


def integrated_angular_rate_eos(
    E: float,
    costh: float,
    target: str,
    antinu: bool,
    temperature: float,
    nu: float,
    mstar: float,
    *,
    span: float = LOCAL_HALF_WINDOW,
    n_ep: int = 48,
    order_p: int = 48,
    order_phi: int = 16,
) -> float:
    ep0 = E/(1.0+E/mstar*(1.0-costh))
    x, w = leggauss(n_ep)
    eps = ep0+span*x
    if float(np.min(eps)) <= 0.0:
        raise ValueError("outgoing-energy interval crossed E'=0")
    rates = [
        differential_rate_eos(
            E, float(ep), costh, target, antinu, temperature, nu, mstar,
            order_p=order_p, order_phi=order_phi,
        )
        for ep in eps
    ]
    return float(np.sum(w*span*np.asarray(rates)))


def detailed_balance_factor_residual(
    Ei_kinetic: float,
    q0: float,
    temperature: float,
    nu: float,
) -> float:
    fi = float(expit((nu-Ei_kinetic)/temperature))
    ff = float(expit((nu-Ei_kinetic-q0)/temperature))
    lhs = fi*(1.0-ff)
    rhs = math.exp(q0/temperature)*ff*(1.0-fi)
    return lhs/rhs-1.0


def _legacy_recovery_cases() -> list[dict]:
    records = []
    for target in SPECIES:
        for antinu in (False, True):
            nB_over_n0, Yp, temperature = 1e-3, 0.10, 3.03
            nB = nB_over_n0*N0
            n_species = (1.0-Yp if target == "n" else Yp)*nB
            mu = legacy.solve_mu(n_species, MASS[target], temperature)
            nu = mu-MASS[target]
            old_gamma = legacy.integrated_angular_rate(
                INCIDENT_ENERGY, COS_THETA, target, antinu,
                temperature, mu, 60.0, 48, 48, 16, True,
            )
            new_gamma = integrated_angular_rate_eos(
                INCIDENT_ENERGY, COS_THETA, target, antinu,
                temperature, nu, MASS[target],
                span=60.0, n_ep=48, order_p=48, order_phi=16,
            )
            records.append({
                "species": target,
                "antinu": antinu,
                "T_MeV": temperature,
                "nB_over_n0": nB_over_n0,
                "E_MeV": INCIDENT_ENERGY,
                "cos_theta": COS_THETA,
                "old_gamma": old_gamma,
                "new_gamma": new_gamma,
                "relative_recovery_residual": new_gamma/old_gamma-1.0,
            })
    return records


def _cold_horowitz_cases() -> list[dict]:
    records = []
    for target in SPECIES:
        for antinu in (False, True):
            nB_over_n0, Yp, temperature = 1e-10, 0.10, 1e-3
            nB = nB_over_n0*N0
            n_species = (1.0-Yp if target == "n" else Yp)*nB
            mu = legacy.solve_mu(n_species, MASS[target], temperature)
            nu = mu-MASS[target]
            gamma = integrated_angular_rate_eos(
                INCIDENT_ENERGY, COS_THETA, target, antinu,
                temperature, nu, MASS[target],
                span=2.5, n_ep=128, order_p=32, order_phi=16,
            )
            stationary = kernel.evaluate(
                INCIDENT_ENERGY, COS_THETA, target, antinu
            )["dsdo"]
            ratio = gamma/(n_species*HBARC**3)/stationary
            records.append({
                "species": target,
                "antinu": antinu,
                "nB_over_n0": nB_over_n0,
                "T_MeV": temperature,
                "ratio_to_Horowitz_dsigma_dOmega": ratio,
            })
    return records


def _eos_local_cases(
    profile_rows: list[dict[str, float]],
    c2_rows: list[dict[str, float]],
) -> list[dict]:
    records = []
    for index in PROFILE_INDICES:
        row, c2 = profile_rows[index], c2_rows[index]
        for target in SPECIES:
            mstar = row[f"mstar_{target}_MeV"]
            temperature = row["T_MeV"]
            nu = c2[f"nu_{target}_EOS_MeV"]
            nprime_fm3 = c2[f"nprime_{target}_fm3"]
            nprime_mev3 = nprime_fm3*HBARC**3
            xi = row["xi_SPP"]
            for antinu in (False, True):
                gamma = integrated_angular_rate_eos(
                    INCIDENT_ENERGY, COS_THETA, target, antinu,
                    temperature, nu, mstar,
                    span=LOCAL_HALF_WINDOW, n_ep=48,
                    order_p=48, order_phi=16,
                )
                sigma_per_target = gamma/nprime_mev3
                stationary = kernel.evaluate(
                    INCIDENT_ENERGY, COS_THETA, target, antinu
                )["dsdo"]
                records.append({
                    "r_km": row["r_km"],
                    "species": target,
                    "antinu": antinu,
                    "T_MeV": temperature,
                    "mstar_MeV": mstar,
                    "nu_MeV": nu,
                    "eta_nu_over_T": nu/temperature,
                    "theta_T_over_mstar": temperature/mstar,
                    "X_free": row[f"X_{target}"],
                    "xi_SPP": xi,
                    "nprime_fm3": nprime_fm3,
                    "n_total_fm3": xi*nprime_fm3,
                    "E_MeV": INCIDENT_ENERGY,
                    "cos_theta": COS_THETA,
                    "Eprime_half_window_MeV": LOCAL_HALF_WINDOW,
                    "gamma_available_volume": gamma,
                    "sigma_per_target_MeV_minus2": sigma_per_target,
                    "ratio_to_vacuum_Horowitz_dsigma_dOmega": sigma_per_target/stationary,
                    "opacity_factor_xi_gamma": xi*gamma,
                })
    return records


def _convergence_cases(
    profile_rows: list[dict[str, float]],
    c2_rows: list[dict[str, float]],
) -> list[dict]:
    index, target = 0, "n"
    row, c2 = profile_rows[index], c2_rows[index]
    mstar = row[f"mstar_{target}_MeV"]
    temperature = row["T_MeV"]
    nu = c2[f"nu_{target}_EOS_MeV"]
    records = []
    for n_ep, order_p, order_phi in (
        (24, 24, 8), (36, 36, 12), (48, 48, 16)
    ):
        gamma = integrated_angular_rate_eos(
            INCIDENT_ENERGY, COS_THETA, target, False,
            temperature, nu, mstar,
            span=LOCAL_HALF_WINDOW, n_ep=n_ep,
            order_p=order_p, order_phi=order_phi,
        )
        records.append({
            "orders_Eprime_p_phi": [n_ep, order_p, order_phi],
            "gamma": gamma,
        })
    return records


def analyze(
    profile_rows: list[dict[str, float]],
    c2_rows: list[dict[str, float]],
) -> tuple[list[dict], list[dict], list[dict], dict]:
    if len(profile_rows) != 301 or len(c2_rows) != 301:
        raise ValueError("C4-B2 requires the 301-point C1/C2 profile")
    legacy_recovery = _legacy_recovery_cases()
    cold = _cold_horowitz_cases()
    local = _eos_local_cases(profile_rows, c2_rows)
    convergence = _convergence_cases(profile_rows, c2_rows)

    db_residuals = []
    for row in local:
        for kinetic in (0.0, 10.0, 100.0, 300.0):
            for q0 in (-20.0, -5.0, 5.0, 20.0):
                db_residuals.append(
                    abs(detailed_balance_factor_residual(
                        kinetic, q0, row["T_MeV"], row["nu_MeV"]
                    ))
                )
    recovery_max = max(abs(row["relative_recovery_residual"]) for row in legacy_recovery)
    cold_max = max(abs(row["ratio_to_Horowitz_dsigma_dOmega"]-1.0) for row in cold)
    conv = [row["gamma"] for row in convergence]
    conv_rel = max(abs(conv[-1]/value-1.0) for value in conv[:-1])
    acceptance = {
        "mstar_equals_M_recovers_P1IIIb_below_1e_10": recovery_max < 1e-10,
        "cold_dilute_Horowitz_limit_below_1e_3": cold_max < 1e-3,
        "EOS_local_grid_has_32_cases": len(local) == 32,
        "local_detailed_balance_below_1e_10": max(db_residuals) < 1e-10,
        "all_local_rates_and_cross_sections_nonnegative": all(
            row["gamma_available_volume"] >= 0.0
            and row["sigma_per_target_MeV_minus2"] >= 0.0
            for row in local
        ),
        "core_local_quadrature_convergence_below_1_percent": conv_rel < 1e-2,
    }
    summary = {
        "title": "P1-IIIe-C4B2 EOS-effective-mass moving-nucleon collision kernel",
        "date": "2026-11-11",
        "status": "PASS: P1-IIIb recovery, Horowitz cold/dilute limit, EOS local rates, and detailed balance",
        "scope": (
            "Local moving-nucleon differential collision rates at four selected radii "
            "of the t_pb=1 s Caputo SFHo-18.8 snapshot; no radial transport or luminosity."
        ),
        "convention": {
            "spinor_and_kinematic_mass": "m*_N(r)",
            "form_factor_and_weak_magnetism_mass": "physical vacuum M_N",
            "occupation": "expit((nu_N-(sqrt(p^2+m*^2)-m*))/T)",
            "final_state_pauli": "1-f_N(E*_p+q0)",
            "same_species_vector_potential": "cancels from q0",
            "per_target_normalization": "n'_N per available volume; xi_SPP cancels",
            "total_volume_opacity_factor": "xi_SPP*n'_N*sigma; xi_SPP is restored only here",
            "scope_exclusions": ["RPA", "NN correlations", "in-medium vertex corrections", "B.2 radial transport"],
        },
        "provenance": {
            "selected_radii_km": [profile_rows[index]["r_km"] for index in PROFILE_INDICES],
            "species": list(SPECIES),
            "incident_energy_MeV": INCIDENT_ENERGY,
            "cos_theta": COS_THETA,
            "local_Eprime_half_window_MeV": LOCAL_HALF_WINDOW,
            "local_cases": len(local),
            "legacy_recovery_cases": len(legacy_recovery),
            "cold_Horowitz_cases": len(cold),
        },
        "maxima": {
            "mstar_equals_M_P1IIIb_recovery_residual": recovery_max,
            "cold_dilute_Horowitz_relative_residual": cold_max,
            "local_detailed_balance_residual": max(db_residuals),
            "core_local_quadrature_convergence_relative_difference": conv_rel,
        },
        "legacy_recovery": legacy_recovery,
        "cold_dilute_Horowitz": cold,
        "core_local_quadrature_convergence": convergence,
        "acceptance": acceptance,
        "overall_pass": all(acceptance.values()),
        "interpretation": [
            "The new kernel reproduces the existing P1-IIIb moving-nucleon implementation when m*_N=M_N and nu=mu-M_N.",
            "The cold/dilute limit is normalized to the vacuum Horowitz differential cross section.",
            "EOS local cross sections are per free target nucleon; xi_SPP cancels in the per-target normalization.",
            "The total-volume opacity is proportional to xi_SPP*n'_N*sigma, so the available-volume fraction must be restored when constructing opacity.",
            "The local EOS rates are a kernel-level result only; they are not integrated over the stellar radius or neutrino transport paths.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C4-B2 acceptance failed: {acceptance}")
    return local, legacy_recovery, cold, summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--c2-reference", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-local-csv", type=Path, required=True)
    parser.add_argument("--output-recovery-csv", type=Path, required=True)
    parser.add_argument("--output-cold-csv", type=Path, required=True)
    args = parser.parse_args()
    profile = load_profile(args.profile)
    c2 = load_c2_reference(args.c2_reference)
    local, recovery, cold, summary = analyze(profile, c2)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(summary, indent=2, allow_nan=False)+"\n", encoding="utf-8"
    )
    for path, rows in (
        (args.output_local_csv, local),
        (args.output_recovery_csv, recovery),
        (args.output_cold_csv, cold),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = __import__("csv").DictWriter(
                stream, fieldnames=list(rows[0]), lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps({
        "overall_pass": summary["overall_pass"],
        "maxima": summary["maxima"],
        "acceptance": summary["acceptance"],
        "local_cases": len(local),
    }, indent=2))


if __name__ == "__main__":
    main()
