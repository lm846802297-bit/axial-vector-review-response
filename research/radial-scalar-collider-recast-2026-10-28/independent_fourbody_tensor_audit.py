#!/usr/bin/env python3
"""Independent Lorentz-tensor and quadrature audit of s -> A'* A'* -> 4f.

This implementation does not import off_shell_four_body.py. It reconstructs
the integrated fermion tensors in a fixed Lorentz frame, applies the unitary-
gauge propagator numerators as explicit 4x4 matrices, contracts the two
propagated tensors, and performs an independent SciPy roots_legendre
quadrature. The identical-species exchange contribution remains a rigorous
Cauchy-Schwarz upper bound, not an exclusive four-body prediction.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import roots_legendre

M_MU = 0.1056583755
M_TAU = 1.77686
THETA_MU_R = 1.0e-2
THETA_TAU_R = 1.0e-2
METRIC = np.diag([1.0, -1.0, -1.0, -1.0])
BENCHMARKS = (
    ("tau_open_reference", 4.0, 5.0, 0.1),
    ("upper_fourmu_scan_mass", 8.48750903116088, 8.633168407011583, 0.1),
    ("more_deeply_offshell", 4.0, 10.0, 0.07),
    ("near_tau_pair_threshold", 3.8, 4.2, 0.1),
)
ORDERS = (96, 128, 192, 256, 384, 512)


def spectral_components(s: np.ndarray, g_x: float) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    """Return positive H_T,H_L coefficients in W^{mu nu}=H_T P_T+H_L P_L."""
    s = np.asarray(s, dtype=float)
    result: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    for name in ("nu_mu", "nu_tau"):
        h_t = (2.0 / 3.0) * g_x**2 * s / (8.0 * math.pi)
        result[name] = (h_t, np.zeros_like(s))
    for name, mass, theta in (
        ("mu", M_MU, THETA_MU_R),
        ("tau", M_TAU, THETA_TAU_R),
    ):
        beta = np.sqrt(np.maximum(0.0, 1.0 - 4.0 * mass**2 / np.maximum(s, 1e-300)))
        g_v2 = g_x**2 * math.sin(theta)**4
        g_a2 = g_x**2 * math.cos(theta)**4
        h_t = (4.0 / 3.0) * (
            g_v2 * (s + 2.0 * mass**2) + g_a2 * (s - 4.0 * mass**2)
        )
        h_l = 8.0 * g_a2 * mass**2 * np.ones_like(s)
        open_channel = s >= 4.0 * mass**2
        result[name] = (
            np.where(open_channel, beta * h_t / (8.0 * math.pi), 0.0),
            np.where(open_channel, beta * h_l / (8.0 * math.pi), 0.0),
        )
    return result


def direct_propagated_tensor(
    s: np.ndarray,
    q: np.ndarray,
    g_x: float,
    m_a: float,
) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    """Build N W N^T directly, with N_{mu nu}=g_{mu nu}-q_mu q_nu/m_A^2."""
    spec = spectral_components(s, g_x)
    q_lower = np.einsum("...i,ij->...j", q, METRIC)
    numerator = METRIC - np.einsum("...i,...j->...ij", q_lower, q_lower) / m_a**2
    p_t = -METRIC + np.einsum("...i,...j->...ij", q, q) / s[..., None, None]
    p_l = np.einsum("...i,...j->...ij", q, q) / s[..., None, None]

    pieces = {}
    total = np.zeros_like(numerator)
    for name, (h_t, h_l) in spec.items():
        w = h_t[..., None, None] * p_t + h_l[..., None, None] * p_l
        propagated = numerator @ w @ np.swapaxes(numerator, -1, -2)
        pieces[name] = propagated
        total += propagated
    return total, pieces


def tensor_contraction(
    ms: float,
    s1: np.ndarray,
    s2: np.ndarray,
    g_x: float,
    m_a: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Direct 4D Lorentz contraction of the two propagated current tensors."""
    root_s1 = np.sqrt(s1)
    e2 = (ms**2 - s1 - s2) / (2.0 * root_s1)
    k2 = np.maximum(0.0, e2**2 - s2)
    k = np.sqrt(k2)

    q1 = np.zeros((*s1.shape, 4))
    q1[..., 0] = root_s1
    q2 = np.zeros_like(q1)
    q2[..., 0] = e2
    q2[..., 3] = k

    w1, pieces1 = direct_propagated_tensor(s1, q1, g_x, m_a)
    w2, pieces2 = direct_propagated_tensor(s2, q2, g_x, m_a)

    total = np.einsum("mn,rs,...mr,...ns->...", METRIC, METRIC, w1, w2)
    same = np.zeros_like(total)
    for name in pieces1:
        same += np.einsum(
            "mn,rs,...mr,...ns->...",
            METRIC, METRIC, pieces1[name], pieces2[name],
        )
    return total, same


def projector_formula_contraction(
    ms: float,
    s1: np.ndarray,
    s2: np.ndarray,
    g_x: float,
    m_a: float,
) -> np.ndarray:
    """Closed projector contraction used only as a pointwise cross-check."""
    z = ((ms**2 - s1 - s2) / 2.0)**2 / (s1 * s2)
    a1 = 1.0 - s1 / m_a**2
    a2 = 1.0 - s2 / m_a**2
    spec1 = spectral_components(s1, g_x)
    spec2 = spectral_components(s2, g_x)
    ht1 = sum(v[0] for v in spec1.values())
    hl1 = sum(v[1] for v in spec1.values())
    ht2 = sum(v[0] for v in spec2.values())
    hl2 = sum(v[1] for v in spec2.values())
    return (
        ht1 * ht2 * (2.0 + z)
        + ht1 * hl2 * a2**2 * (z - 1.0)
        + hl1 * ht2 * a1**2 * (z - 1.0)
        + hl1 * hl2 * a1**2 * a2**2 * z
    )


def independent_width(ms: float, m_a: float, g_x: float, order: int) -> dict:
    if min(ms, m_a, g_x) <= 0.0 or m_a < ms:
        raise ValueError("require positive inputs and the double-virtual region m_A >= m_s")
    if order < 16:
        raise ValueError("quadrature order must be at least 16")

    nodes, weights = roots_legendre(order)
    u = 0.5 * (nodes + 1.0)
    w = 0.5 * weights
    x = u[:, None]
    y = u[None, :]
    s1 = ms**2 * x**2 + np.zeros((order, order))
    s2 = ms**2 * (1.0 - x)**2 * y**2 + np.zeros((order, order))
    jacobian = 4.0 * ms**4 * x * (1.0 - x)**2 * y
    weight_2d = w[:, None] * w[None, :]
    kallen = np.maximum(0.0, (ms**2 - s1 - s2)**2 - 4.0 * s1 * s2)
    sqrt_kallen = np.sqrt(kallen)
    denominator = np.maximum((s1 - m_a**2)**2 * (s2 - m_a**2)**2, 1e-300)
    phase_weight = sqrt_kallen * jacobian * weight_2d / denominator

    contraction, same_contraction = tensor_contraction(ms, s1, s2, g_x, m_a)

    # Factorized dPhi_4 = ds1 ds2/(2pi)^2 dPhi_2 dPhi_2 dPhi_2.
    # After integrating the three two-body angles, the labeled-vector
    # coefficient is g_sAA^2/(64 pi^3 m_s^3). The 1/2 removes the
    # ordered double counting of the two identical virtual A' lines.
    g_saa = 4.0 * g_x * m_a
    coefficient = g_saa**2 / (64.0 * math.pi**3 * ms**3)
    diagonal = 0.5 * coefficient * float(np.sum(phase_weight * contraction))
    same = 0.5 * coefficient * float(np.sum(phase_weight * same_contraction))
    distinct = diagonal - same
    upper = distinct + 2.0 * same
    if diagonal <= 0.0 or same < -1e-14 * diagonal or distinct < -1e-14 * diagonal:
        raise AssertionError("non-positive diagonal spectral integral")
    return {
        "diagonal_pairing_GeV": diagonal,
        "same_species_diagonal_GeV": same,
        "distinct_species_GeV": distinct,
        "identical_exchange_cauchy_upper_bound_GeV": upper,
        "ratio_upper_over_diagonal": upper / diagonal,
        "quadrature_order": order,
    }


def pointwise_tensor_checks() -> dict:
    rng = np.random.default_rng(20261109)
    checks = []
    for label, ms, m_a, g_x in BENCHMARKS:
        for _ in range(12):
            x = float(rng.uniform(0.06, 0.94))
            y = float(rng.uniform(0.06, 0.94))
            s1 = np.array([[ms**2 * x**2]])
            s2 = np.array([[ms**2 * (1.0 - x)**2 * y**2]])
            direct, _ = tensor_contraction(ms, s1, s2, g_x, m_a)
            formula = projector_formula_contraction(ms, s1, s2, g_x, m_a)
            rel = abs(float(direct[0, 0] - formula[0, 0])) / max(abs(float(direct[0, 0])), 1e-300)
            if rel > 2e-10:
                raise AssertionError(f"{label}: tensor/projector mismatch {rel}")
            checks.append(rel)
    return {
        "samples": len(checks),
        "max_relative_difference_direct_tensor_vs_projector": max(checks),
    }


def run_audit() -> dict:
    pointwise = pointwise_tensor_checks()
    results = {}
    for label, ms, m_a, g_x in BENCHMARKS:
        convergence = [independent_width(ms, m_a, g_x, n) for n in ORDERS]
        by_order = {str(x["quadrature_order"]): x for x in convergence}
        ref = by_order[str(512)]["diagonal_pairing_GeV"]
        rel_384_512 = abs(by_order["384"]["diagonal_pairing_GeV"] - ref) / ref
        rel_128_512 = abs(by_order["128"]["diagonal_pairing_GeV"] - ref) / ref
        if rel_384_512 > 2e-4 or rel_128_512 > 2e-3:
            raise AssertionError(f"{label}: quadrature convergence failed")
        results[label] = {
            "inputs": {"ms_GeV": ms, "mA_GeV": m_a, "gX": g_x},
            "convergence": convergence,
            "relative_change_128_vs_512": rel_128_512,
            "relative_change_384_vs_512": rel_384_512,
            "reference_512": by_order["512"],
        }

    scaling_a = independent_width(4.0, 5.0, 0.05, 96)["diagonal_pairing_GeV"]
    scaling_b = independent_width(4.0, 5.0, 0.10, 96)["diagonal_pairing_GeV"]
    scaling_ratio = scaling_b / scaling_a
    if abs(scaling_ratio - 64.0) > 2e-8:
        raise AssertionError(f"gX^6 scaling failed: {scaling_ratio}")

    return {
        "status": "PASS",
        "method": "independent SciPy roots_legendre quadrature plus explicit 4x4 Lorentz tensors",
        "pointwise_tensor_checks": pointwise,
        "benchmarks": results,
        "gX_scaling": {
            "gX_ratio": 2.0,
            "width_ratio": scaling_ratio,
            "expected_gX6_ratio": 64.0,
        },
        "interpretation_limits": [
            "The diagonal-pairing double-spectral integral is independently reproduced.",
            "Identical-species exchange is still represented by a Cauchy-Schwarz upper bound, not an exact exclusive four-body amplitude.",
            "The width term in the virtual A' propagators is omitted in this mA >= ms domain.",
            "The 512-point result is a numerical convergence reference, not a detector-level prediction.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "pointwise_tensor_checks": result["pointwise_tensor_checks"],
        "gX_scaling": result["gX_scaling"],
        "benchmarks": {
            k: {
                "width_512_GeV": v["reference_512"]["diagonal_pairing_GeV"],
                "same_species_fraction": (
                    v["reference_512"]["same_species_diagonal_GeV"]
                    / v["reference_512"]["diagonal_pairing_GeV"]
                ),
                "exchange_upper_ratio": v["reference_512"]["ratio_upper_over_diagonal"],
                "relative_change_128_vs_512": v["relative_change_128_vs_512"],
                "relative_change_384_vs_512": v["relative_change_384_vs_512"],
            } for k, v in result["benchmarks"].items()
        },
    }, indent=2))


if __name__ == "__main__":
    main()
