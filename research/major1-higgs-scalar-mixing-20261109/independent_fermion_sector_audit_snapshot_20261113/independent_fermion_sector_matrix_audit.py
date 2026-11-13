#!/usr/bin/env python3
"""Independent high-precision Feynman-parameter audit of the fermion matrix.

This implementation does not import fermion_sector_matrix_audit.py. It uses
SciPy's independent SVD driver and mpmath integration of the Feynman-parameter
representation of B0, then compares the result with the archived calculation.
It covers only the charged-lepton plus VLL fermion sector.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.linalg import svd

MH = 125.25
VH = 246.22
ME = 20_000.0
THETA_L = 1.0e-2
MU_R = ME
FLAVOURS = {"mu": 0.1056583755, "tau": 1.77686}
BENCHMARKS = (
    ("A_open_AA", 70.886458, 10.0),
    ("B_closed_AA", 315.0, 63.0),
)
ENTRIES = (("h", "h"), ("h", "s"), ("s", "s"))


def primitive_a0(mass: float) -> float:
    """Finite MS-bar tadpole function, evaluated without the reference code."""
    if mass == 0.0:
        return 0.0
    m2 = mp.mpf(str(mass)) ** 2
    mu2 = mp.mpf(str(MU_R)) ** 2
    return float(m2 * (1 - mp.log(m2 / mu2)))


def b0_feynman_parameter(p2: float, mi: float, mj: float, dps: int = 45) -> complex:
    """Compute B0bar=-int_0^1 dx log(Delta/mu^2-i0) using mpmath.

    The real part is integrated directly at high precision. Real roots of
    Delta inside (0,1) split the integral at logarithmic singularities; the
    absorptive part is +pi times the measure of the interval where Delta<0.
    This is algorithmically independent of the adaptive SciPy quadrature used
    in the archived implementation.
    """
    with mp.workdps(dps):
        p = mp.mpf(str(p2))
        m_i = mp.mpf(str(mi))
        m_j = mp.mpf(str(mj))
        mu = mp.mpf(str(MU_R))
        roots = []
        if p > 0:
            discriminant = (m_i*m_i - m_j*m_j - p)**2 - 4*p*m_j*m_j
            if discriminant >= 0:
                root_disc = mp.sqrt(discriminant)
                root_a = (-(m_i*m_i - m_j*m_j - p) - root_disc) / (2*p)
                root_b = (-(m_i*m_i - m_j*m_j - p) + root_disc) / (2*p)
                roots = sorted(r for r in (root_a, root_b) if 0 < r < 1)
        points = [mp.mpf("0"), *roots, mp.mpf("1")]

        def delta(x):
            return x*m_i*m_i + (1-x)*m_j*m_j - x*(1-x)*p

        real_part = mp.mpf("0")
        negative_measure = mp.mpf("0")
        for lo, hi in zip(points[:-1], points[1:]):
            midpoint = (lo + hi) / 2
            if delta(midpoint) < 0:
                negative_measure += hi - lo
            real_part += mp.quad(
                lambda x: -mp.log(abs(delta(x)) / (mu*mu)),
                [lo, hi],
            )
        return complex(float(real_part), float(mp.pi * negative_measure))


def mass_basis(vs: float, ml: float):
    """Diagonalize the original 2x2 charged-lepton/VLL mass matrix by SVD."""
    theta_r = ml / (ME * THETA_L)
    y = math.sqrt(2.0) * ME * THETA_L / VH
    lam = math.sqrt(2.0) * ME * theta_r / vs
    matrix = np.array([
        [0.0, y * VH / math.sqrt(2.0)],
        [lam * vs / math.sqrt(2.0), ME],
    ])
    # gesvd is intentionally used instead of NumPy's default SVD driver.
    left, masses, right_h = svd(matrix, full_matrices=False, lapack_driver="gesvd")
    right = right_h.T
    gamma_h = np.array([[0.0, y / math.sqrt(2.0)], [0.0, 0.0]])
    gamma_s = np.array([[0.0, 0.0], [lam / math.sqrt(2.0), 0.0]])
    return masses, left.T @ gamma_h @ right, left.T @ gamma_s @ right


def chiral_coefficients(ga: np.ndarray, gb: np.ndarray, i: int, j: int):
    """Coefficients obtained from the two independent chiral structures."""
    c_kinetic = ga[i, j] * np.conj(gb[i, j]) + np.conj(ga[j, i]) * gb[j, i]
    c_mass = ga[i, j] * gb[j, i] + np.conj(ga[j, i]) * np.conj(gb[i, j])
    return c_kinetic, c_mass


def full_fermion_entry(vs: float, ml: float, p2: float, a: str, b: str):
    masses, gh, gs = mass_basis(vs, ml)
    ga = gh if a == "h" else gs
    gb = gh if b == "h" else gs
    finite_sum = 0.0j
    uv_p2 = 0.0j
    uv_local = 0.0j
    for i in range(2):
        for j in range(2):
            mi, mj = float(masses[i]), float(masses[j])
            b0 = b0_feynman_parameter(p2, mi, mj)
            c_kinetic, c_mass = chiral_coefficients(ga, gb, i, j)
            finite_tadpole = primitive_a0(mi) + primitive_a0(mj)
            finite_bubble = (mi*mi + mj*mj - p2) * b0
            finite_sum += (
                c_kinetic * (finite_tadpole + finite_bubble)
                + 2.0 * mi * mj * c_mass * b0
            )
            uv_p2 += c_kinetic
            uv_local += (
                2.0 * (mi*mi + mj*mj) * c_kinetic
                + 2.0 * mi * mj * c_mass
            )
    return -finite_sum / (16.0 * math.pi**2), uv_p2, uv_local


def light_eft_entry(vs: float, ml: float, p2: float, a: str, b: str):
    """Light-light EFT bubble, with the opposite Plan-B self-energy sign."""
    masses, gh, gs = mass_basis(vs, ml)
    ga = gh if a == "h" else gs
    gb = gh if b == "h" else gs
    light_mass = float(masses[1])
    c_kinetic, c_mass = chiral_coefficients(ga, gb, 1, 1)
    b0 = b0_feynman_parameter(p2, light_mass, light_mass)
    kernel = (
        2.0 * primitive_a0(light_mass)
        + (2.0 * light_mass*light_mass - p2) * b0
    )
    value = (
        c_kinetic * kernel
        + 2.0 * light_mass*light_mass * c_mass * b0
    ) / (16.0 * math.pi**2)
    uv_p2 = c_kinetic
    uv_local = (
        4.0 * light_mass*light_mass * c_kinetic
        + 2.0 * light_mass*light_mass * c_mass
    )
    return value, uv_p2, uv_local


def calculate_benchmark(label: str, vs: float, m_a: float) -> dict:
    result = {}
    for a, b in ENTRIES:
        full_zero = full_higgs = light_zero = light_higgs = 0.0j
        full_uv_p2 = full_uv_local = 0.0j
        light_uv_p2 = light_uv_local = 0.0j
        for ml in FLAVOURS.values():
            p0, c0, l0 = full_fermion_entry(vs, ml, 0.0, a, b)
            ph, _, _ = full_fermion_entry(vs, ml, MH*MH, a, b)
            q0, qc, ql = light_eft_entry(vs, ml, 0.0, a, b)
            qh, _, _ = light_eft_entry(vs, ml, MH*MH, a, b)
            full_zero += p0
            full_higgs += ph
            light_zero += q0
            light_higgs += qh
            full_uv_p2 += c0
            full_uv_local += l0
            light_uv_p2 += qc
            light_uv_local += ql

        # The full-theory self-energy uses Pi_RC; Plan-B defines Pi_B=-Pi_RC.
        full_difference = -(full_higgs - full_zero)
        light_difference = light_higgs - light_zero
        hard_difference = full_difference - light_difference
        delta_c = full_uv_p2 - light_uv_p2
        delta_local = full_uv_local - light_uv_local
        result[a+b] = {
            "Pi_RC_mh2_GeV2": [full_higgs.real, full_higgs.imag],
            "Pi_RC_0_GeV2": [full_zero.real, full_zero.imag],
            "hard_momentum_difference_PiB_GeV2": [
                hard_difference.real, hard_difference.imag
            ],
            "UV_p2_coefficient_sum_C": [full_uv_p2.real, full_uv_p2.imag],
            "UV_local_coefficient_sum": [full_uv_local.real, full_uv_local.imag],
            "light_light_UV_p2_coefficient_C": [
                light_uv_p2.real, light_uv_p2.imag
            ],
            "light_light_UV_local_coefficient": [
                light_uv_local.real, light_uv_local.imag
            ],
            "full_minus_light_UV_p2_coefficient_C": [delta_c.real, delta_c.imag],
            "full_minus_light_UV_local_coefficient": [
                delta_local.real, delta_local.imag
            ],
            "MS_field_counterterm_pole_coefficient_full_minus_light":
                -delta_c.real / (16.0 * math.pi**2),
        }

    absorptive = np.array([
        [result["hh"]["Pi_RC_mh2_GeV2"][1], result["hs"]["Pi_RC_mh2_GeV2"][1]],
        [result["hs"]["Pi_RC_mh2_GeV2"][1], result["ss"]["Pi_RC_mh2_GeV2"][1]],
    ])
    eig = np.linalg.eigvalsh(absorptive)
    result["absorptive_matrix_PiRC_GeV2"] = absorptive.tolist()
    result["absorptive_eigenvalues_GeV2"] = eig.tolist()
    result["absorptive_determinant_GeV4"] = float(np.linalg.det(absorptive))
    result["absorptive_offdiagonal_saturation_ratio"] = float(
        absorptive[0, 1] / math.sqrt(absorptive[0, 0] * absorptive[1, 1])
    )
    result["benchmark"] = {
        "name": label, "vs_GeV": vs, "mA_GeV": m_a,
        "gX": m_a / (2.0 * vs), "ME_GeV": ME, "theta_L": THETA_L,
    }
    return result


def compare_with_reference(independent: dict, reference: dict) -> dict:
    checks = []
    for label, _, _ in BENCHMARKS:
        got = independent["benchmarks"][label]
        ref = reference["benchmarks"][label]
        for entry in ("hh", "hs", "ss"):
            for field in (
                "hard_momentum_difference_PiB_GeV2",
                "Pi_RC_mh2_GeV2",
                "Pi_RC_0_GeV2",
                "UV_p2_coefficient_sum_C",
                "UV_local_coefficient_sum",
                "light_light_UV_p2_coefficient_C",
                "light_light_UV_local_coefficient",
                "full_minus_light_UV_p2_coefficient_C",
                "full_minus_light_UV_local_coefficient",
            ):
                for component, (actual, expected) in enumerate(zip(got[entry][field], ref[entry][field])):
                    tolerance = 5e-7 if field == "hard_momentum_difference_PiB_GeV2" else 2e-5
                    if abs(actual - expected) > tolerance + 2e-10 * abs(expected):
                        raise AssertionError(
                            f"{label} {entry} {field}[{component}] differs: "
                            f"{actual} vs {expected}"
                        )
            actual_z = got[entry]["MS_field_counterterm_pole_coefficient_full_minus_light"]
            expected_z = ref[entry]["MS_field_counterterm_pole_coefficient_full_minus_light"]
            if abs(actual_z - expected_z) > 2e-10 * max(1.0, abs(expected_z)):
                raise AssertionError(f"{label} {entry} field counterterm mismatch")
        for field in ("absorptive_matrix_PiRC_GeV2", "absorptive_eigenvalues_GeV2"):
            got_values = np.asarray(got[field], dtype=float)
            ref_values = np.asarray(ref[field], dtype=float)
            if not np.allclose(got_values, ref_values, rtol=2e-10, atol=2e-12):
                raise AssertionError(f"{label} {field} mismatch")
        eig = np.asarray(got["absorptive_eigenvalues_GeV2"])
        if eig[0] < -1e-10 or eig[1] <= 0:
            raise AssertionError(f"{label} absorptive matrix is not positive semidefinite")
        if abs(got["absorptive_offdiagonal_saturation_ratio"] - 1.0) > 1e-8:
            raise AssertionError(f"{label} absorptive rank-one saturation failed")
        checks.append({
            "benchmark": label,
            "matrix_entries_compared": 3,
            "hard_difference_max_abs_error_GeV2": max(
                abs(got[e]["hard_momentum_difference_PiB_GeV2"][0]
                    - ref[e]["hard_momentum_difference_PiB_GeV2"][0])
                for e in ("hh", "hs", "ss")
            ),
            "absorptive_min_eigenvalue_GeV2": float(eig[0]),
            "absorptive_saturation_ratio": got["absorptive_offdiagonal_saturation_ratio"],
        })
    return {"status": "PASS", "benchmarks": checks}


def run_audit(reference_path: Path) -> dict:
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    independent = {
        "method": "SciPy gesvd plus 45-digit mpmath Feynman-parameter integration",
        "scope": "mu/tau plus original VLL fermion sector only",
        "renormalization_scale_GeV": MU_R,
        "external_momentum_GeV2": MH*MH,
        "benchmarks": {
            label: calculate_benchmark(label, vs, ma)
            for label, vs, ma in BENCHMARKS
        },
    }
    comparison = compare_with_reference(independent, reference)
    return {
        **independent,
        "comparison_to_archived_calculation": comparison,
        "interpretation_limits": [
            "This is an independent numerical implementation of the fermion-sector subcalculation, not a complete gauge-independent self-energy.",
            "The calculation does not include top, W, Z, A-prime, Goldstone, ghost, scalar, tadpole, or VEV-renormalization contributions.",
            "The hard momentum differences are not physical pole shifts.",
            "No complex poles, residues, mixing angle, line shape, signal strength, or exclusion is inferred.",
            "If the explicit mu/tau absorptive cuts are retained in a future propagator, their partial widths must not be inserted a second time as external diagonal widths.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_audit(args.reference_json)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["comparison_to_archived_calculation"], indent=2))


if __name__ == "__main__":
    main()
