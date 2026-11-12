#!/usr/bin/env python3
"""Direct P_L audit for gamma + mu -> mu + Z' (pure vector current).

The longitudinal mode is projected at amplitude level. For a conserved vector
current, the exact Ward identity permits epsilon_L -> epsilon_L - q/m_Z'.
This is evaluated in a cancellation-free form and compared with printed
Appendix-B B.2/B.3/B.4 traces. No thermal rate or stellar transport is computed.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

M_MU = 105.6583755
ALPHA = 1.0 / 137.035999084
E2 = 4.0 * math.pi * ALPHA
METRIC = np.array([1.0, -1.0, -1.0, -1.0])
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
SIGMA = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)
GAMMA = np.array(
    [np.block([[I2, Z2], [Z2, -I2]])]
    + [np.block([[Z2, s], [-s, Z2]]) for s in SIGMA]
)
I4 = np.eye(4, dtype=complex)


def slash(v):
    return np.einsum("a,aij->ij", np.asarray(v) * METRIC, GAMMA)


def kinematics(eg, ma, c, m_mu=M_MU):
    p = np.array([m_mu, 0.0, 0.0, 0.0])
    k = np.array([eg, 0.0, 0.0, eg])
    a, b, d = m_mu + eg, eg * c, m_mu * eg + ma * ma / 2.0
    disc = d * d - (a * a - b * b) * ma * ma
    if disc < -1e-12 * max(d * d, 1.0):
        raise ValueError("Unphysical two-body kinematics")
    q0 = (a * d + b * math.sqrt(max(disc, 0.0))) / (a * a - b * b)
    qabs = math.sqrt(max(q0 * q0 - ma * ma, 0.0))
    q = np.array([q0, qabs * math.sqrt(max(1.0 - c * c, 0.0)), 0.0, qabs * c])
    return p, k, p + k - q, q


def spinor(p, spin, m_mu=M_MU):
    chi = np.eye(2, dtype=complex)[:, spin]
    sigma_p = sum(SIGMA[i] * p[i + 1] for i in range(3))
    return math.sqrt(p[0] + m_mu) * np.r_[chi, sigma_p @ chi / (p[0] + m_mu)]


def mode_spinor_sum(eg, ma, c, eps_x, wrong_u=False, m_mu=M_MU):
    p, k, pp, q = kinematics(eg, ma, c, m_mu)
    ps, pu = p + k, p - q
    ds = ps[0] ** 2 - np.dot(ps[1:], ps[1:]) - m_mu**2
    du = pu[0] ** 2 - np.dot(pu[1:], pu[1:]) - m_mu**2
    prop_s = (slash(ps) + m_mu * I4) / ds
    prop_u = (slash(pu) + m_mu * I4) / du
    vx, total = slash(eps_x), 0.0
    for si in range(2):
        ui = spinor(p, si, m_mu)
        for sf in range(2):
            uf = spinor(pp, sf, m_mu)
            ubar = uf.conj() @ GAMMA[0]
            for eps_g in (np.array([0., 1., 0., 0.]), np.array([0., 0., 1., 0.])):
                vg = slash(eps_g)
                if wrong_u:
                    # Literal printed B.1b ordering: same gamma order as s-channel.
                    amp = vx @ prop_s @ vg + vx @ prop_u @ vg
                else:
                    # Crossed Compton ordering required by the fermion line.
                    amp = vx @ prop_s @ vg + vg @ prop_u @ vx
                total += abs(ubar @ amp @ ui) ** 2
    return float(total * E2)


def mode_trace_average_initial_muon(eg, ma, c, eps_x, m_mu=M_MU):
    """Trace sum over photon polarizations, averaged over initial muon spin."""
    p, k, pp, q = kinematics(eg, ma, c, m_mu)
    ps, pu = p + k, p - q
    ds = ps[0] ** 2 - np.dot(ps[1:], ps[1:]) - m_mu**2
    du = pu[0] ** 2 - np.dot(pu[1:], pu[1:]) - m_mu**2
    prop_s = (slash(ps) + m_mu * I4) / ds
    prop_u = (slash(pu) + m_mu * I4) / du
    spin_out, spin_in = slash(pp) + m_mu * I4, slash(p) + m_mu * I4
    vx, total = slash(eps_x), 0.0
    for eps_g in (np.array([0., 1., 0., 0.]), np.array([0., 0., 1., 0.])):
        vg = slash(eps_g)
        amp = vx @ prop_s @ vg + vg @ prop_u @ vx
        amp_bar = GAMMA[0] @ amp.conj().T @ GAMMA[0]
        total += np.trace(spin_out @ amp @ spin_in @ amp_bar).real / 2.0
    return float(total * E2)


def polarizations(q, ma):
    qabs = float(np.linalg.norm(q[1:]))
    nhat = q[1:] / qabs
    eps_l = np.r_[qabs / ma, q[0] * nhat / ma]
    # Exact epsilon_L - q/m, evaluated without subtracting two large vectors.
    eps_l_ward = np.r_[-ma / (q[0] + qabs), ma * nhat / (q[0] + qabs)]
    ref = np.array([0., 1., 0.]) if abs(nhat[1]) < 0.9 else np.array([1., 0., 0.])
    e1 = np.cross(ref, nhat)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(nhat, e1)
    e2 /= np.linalg.norm(e2)
    return eps_l, eps_l_ward, np.r_[0., e1], np.r_[0., e2]


def paper_b2_b4(eg, ma, c, m_mu=M_MU):
    """Printed B.2 and B.4 scalar expressions, with e^2 g_mu_tau^2 and g=1."""
    p, k, pp, q = kinematics(eg, ma, c, m_mu)
    a, b = m_mu * eg, m_mu * q[0]
    p2q = float(np.dot(pp[1:], q[1:]))
    p2sq = float(np.dot(pp[1:], pp[1:]))
    q3sq = float(np.dot(q[1:], q[1:]))
    t0 = (
        8 * m_mu**2 * p2q**2 / (q3sq * a**2)
        - 8 * m_mu**2 * p2sq / a**2
        + 8 * b / a + 8 * a / b
    )
    tm = (
        4 * p2q**2 / (q3sq * a * b)
        + 4 * m_mu**2 * (a - b)**2 / (a**2 * b**2)
        + 4 * a / b**2 - 4 * p2sq / (a * b)
        + 4 / a + 8 / b
    )
    b2 = E2 * (t0 + ma**2 * tm)
    total0 = (
        8 * m_mu**4 * (a - b)**2 / (a**2 * b**2)
        + 16 * m_mu**2 * (b - a) / (b * a)
        + 8 * (a**2 + b**2) / (b * a)
    )
    totalm = (
        8 * m_mu**4 * (a - b) / (a * b**3)
        - 4 * m_mu**2 * (a**2 - b**2) / (a**2 * b**2)
        + 4 * (a - b)**2 / (a * b)
    )
    b4 = E2 * (total0 + ma**2 * totalm)
    return b2, b4, b4 - b2


def one_case(eg, x, c):
    ma = eg * x
    p, k, pp, q = kinematics(eg, ma, c)
    eps_l, eps_lw, eps_t1, eps_t2 = polarizations(q, ma)
    # Direct rank-one P_L projection at amplitude level.
    l_phys = mode_spinor_sum(eg, ma, c, eps_l)
    l_ward = mode_spinor_sum(eg, ma, c, eps_lw)
    t1 = mode_spinor_sum(eg, ma, c, eps_t1)
    t2 = mode_spinor_sum(eg, ma, c, eps_t2)
    q_ward = mode_spinor_sum(eg, ma, c, q)
    q_ward_wrong = mode_spinor_sum(eg, ma, c, q, wrong_u=True)
    # Independent Dirac trace with the same Ward-equivalent P_L representative.
    l_trace_unaveraged = 2.0 * mode_trace_average_initial_muon(eg, ma, c, eps_lw)
    b2, b4, b3 = paper_b2_b4(eg, ma, c)
    t, total = t1 + t2, t1 + t2 + l_ward
    return {
        "Egamma_MeV": eg, "x": x, "cos_theta": c,
        "L_over_T": l_ward / t,
        "L_over_T_over_x2": l_ward / t / x**2,
        "physical_vs_Ward_rel": abs(l_phys / l_ward - 1.0),
        "trace_vs_spinor_rel": abs(l_trace_unaveraged / l_ward - 1.0),
        "qWard_rel_amplitude": math.sqrt(q_ward / total),
        "wrong_u_qWard_rel_amplitude": math.sqrt(q_ward_wrong / total),
        "B2_relative_residual": b2 / t - 1.0,
        "B4_relative_residual": b4 / total - 1.0,
        "B3_relative_residual": b3 / l_ward - 1.0,
        "B3_subtraction_condition": (abs(b4) + abs(b2)) / abs(b3),
        "B2_scaled_residual": (b2 / t - 1.0) / (x**2 * eg / M_MU),
    }


def high_precision_recheck(cases):
    try:
        import mpmath as mp
    except ImportError:
        return {"available": False, "reason": "mpmath is not installed"}
    mp.mp.dps = 80
    M = mp.mpf(str(M_MU))
    alpha = 1 / mp.mpf("137.035999084")
    e2 = 4 * mp.pi * alpha

    def b3_mp(egf, maf, cf):
        eg, ma, c = mp.mpf(str(egf)), mp.mpf(str(maf)), mp.mpf(str(cf))
        a0, b0, d0 = M + eg, eg * c, M * eg + ma**2 / 2
        disc = d0**2 - (a0**2 - b0**2) * ma**2
        q0 = (a0 * d0 + b0 * mp.sqrt(disc)) / (a0**2 - b0**2)
        qabs = mp.sqrt(q0**2 - ma**2)
        qx, qz = qabs * mp.sqrt(1-c**2), qabs * c
        p2x, p2z = -qx, eg-qz
        a, b = M*eg, M*q0
        p2q, p2sq, q3sq = p2x*qx+p2z*qz, p2x**2+p2z**2, qabs**2
        t0 = 8*M**2*p2q**2/(q3sq*a**2)-8*M**2*p2sq/a**2+8*b/a+8*a/b
        tm = (4*p2q**2/(q3sq*a*b)+4*M**2*(a-b)**2/(a**2*b**2)
              +4*a/b**2-4*p2sq/(a*b)+4/a+8/b)
        b2 = e2*(t0+ma**2*tm)
        total0 = (8*M**4*(a-b)**2/(a**2*b**2)+16*M**2*(b-a)/(b*a)
                  +8*(a**2+b**2)/(b*a))
        totalm = (8*M**4*(a-b)/(a*b**3)-4*M**2*(a**2-b**2)/(a**2*b**2)
                  +4*(a-b)**2/(a*b))
        return e2*(total0+ma**2*totalm)-b2

    result = []
    for x in (0.1, 0.01, 0.001):
        vals = []
        for c in (-0.7, 0.2, 0.8):
            eg, ma = 0.1, 0.1*x
            item = next(r for r in cases if r["Egamma_MeV"] == eg and r["x"] == x and r["cos_theta"] == c)
            p, k, pp, q = kinematics(eg, ma, c)
            _, _, et1, et2 = polarizations(q, ma)
            t = mode_spinor_sum(eg, ma, c, et1) + mode_spinor_sum(eg, ma, c, et2)
            l_direct = mp.mpf(str(item["L_over_T"])) * mp.mpf(str(t))
            vals.append(float(b3_mp(eg, ma, c)/l_direct-1))
        result.append({"x": x, "relative_residuals_by_cos_theta": vals})
    return {
        "available": True, "digits": 80, "Egamma_MeV": 0.1,
        "m_over_Egamma_to_B3_minus_direct_PL": result,
        "note": "High-precision B.2/B.4 subtraction does not remove the residual."
    }


def build_audit():
    cases = [one_case(eg, x, c)
             for eg in (0.05, 0.1, 0.5, 1.0)
             for x in (0.001, 0.01, 0.1)
             for c in (-0.7, 0.2, 0.8)]
    values = lambda key: np.array([r[key] for r in cases], dtype=float)
    small = [r for r in cases if r["Egamma_MeV"] <= 0.1 and r["x"] <= 0.01]
    shape_errors = [
        abs(r["L_over_T_over_x2"] -
            (1.0-r["cos_theta"]**2)/(1.0+r["cos_theta"]**2))
        for r in small
    ]
    scaling = []
    for x in (0.001, 0.01, 0.1):
        for eg in (0.05, 0.1, 0.5, 1.0):
            group = [r for r in cases if r["x"] == x and r["Egamma_MeV"] == eg]
            residuals = [r["B3_relative_residual"] for r in group]
            scaling.append({
                "Egamma_MeV": eg, "m_over_Egamma": x,
                "mean_B3_minus_direct_PL": float(np.mean(residuals)),
                "min_B3_minus_direct_PL": float(np.min(residuals)),
                "max_B3_minus_direct_PL": float(np.max(residuals)),
                "mean_B2_relative_residual": float(np.mean([r["B2_relative_residual"] for r in group])),
                "mean_B4_relative_residual": float(np.mean([r["B4_relative_residual"] for r in group])),
            })
    return {
        "title": "Direct longitudinal-projector audit of vector semi-Compton production",
        "source": {
            "arxiv": "2610.35379v1", "pdf_pages": "45-46",
            "equations": ["(B.1a)", "(B.1b)", "(B.2)", "(B.3)", "(B.4)", "(A.15)"],
            "pdf_url": "https://arxiv.org/pdf/2610.35379v1"
        },
        "scope": "Exact two-body gamma+mu -> mu+Z' kinematics in the initial-muon rest frame; direct rank-one P_L projection; comparison with printed B.2/B.3/B.4. No thermal rate or stellar transport.",
        "projector_method": {
            "physical_epsilon_L": "(|q|/m, omega*qhat/m)",
            "ward_identity": "q_mu M^mu=0 for the conserved vector current",
            "stable_epsilon_L": "epsilon_L-q/m=(-m/(omega+|q|), m*qhat/(omega+|q|))",
            "contraction": "Compute |ubar Gamma^mu u epsilon_{L,mu}|^2 directly; use the exactly Ward-equivalent stable epsilon before squaring.",
            "axial_caveat": "The Ward shift is exact only for the conserved pure-vector current; do not apply it to the axial component."
        },
        "benchmark_grid": {
            "Egamma_MeV": [0.05, 0.1, 0.5, 1.0],
            "m_over_Egamma": [0.001, 0.01, 0.1],
            "cos_theta": [-0.7, 0.2, 0.8],
            "number_of_cases": len(cases)
        },
        "summary": {
            "max_physical_vs_Ward_rel": float(np.max(values("physical_vs_Ward_rel"))),
            "max_trace_vs_spinor_rel": float(np.max(values("trace_vs_spinor_rel"))),
            "max_correct_qWard_rel_amplitude": float(np.max(values("qWard_rel_amplitude"))),
            "min_literal_B1b_wrong_u_qWard_rel_amplitude": float(np.min(values("wrong_u_qWard_rel_amplitude"))),
            "max_literal_B1b_wrong_u_qWard_rel_amplitude": float(np.max(values("wrong_u_qWard_rel_amplitude"))),
            "max_abs_B2_relative_residual": float(np.max(np.abs(values("B2_relative_residual")))),
            "max_abs_B4_relative_residual": float(np.max(np.abs(values("B4_relative_residual")))),
            "max_abs_B3_relative_residual": float(np.max(np.abs(values("B3_relative_residual")))),
            "max_B3_abs_error_E_le_0p1_x_le_0p01": float(max(abs(r["B3_relative_residual"]) for r in small)),
            "max_L_over_T_x2_shape_error_E_le_0p1_x_le_0p01": float(max(shape_errors)),
            "B2_scaled_residual_range_x_le_0p01": [
                float(min(r["B2_scaled_residual"] for r in cases if r["x"] <= 0.01)),
                float(max(r["B2_scaled_residual"] for r in cases if r["x"] <= 0.01))
            ],
            "all_direct_longitudinal_rates_positive": bool(np.all(values("L_over_T") > 0.0)),
            "n_cases": len(cases)
        },
        "high_precision_recheck": high_precision_recheck(cases),
        "B3_residual_scaling": scaling,
        "cases": cases,
        "interpretation": {
            "direct_PL": "The rank-one longitudinal projection is positive and agrees between explicit spinors and an independent Dirac trace using the Ward-equivalent polarization.",
            "B1b": "The literal u-channel gamma-matrix order printed in B.1b fails q_mu M^mu=0. The crossed order gamma^nu S_u gamma^mu satisfies the vector Ward identity.",
            "B3": "The B.3 difference is systematically below the direct P_L result. For x<=0.01 its relative discrepancy grows approximately linearly with E_gamma/m_mu. The B.2 transverse residual scales as x^2 E_gamma/m_mu, so it is amplified when an O(x^2) longitudinal signal is obtained by subtraction.",
            "claim_boundary": "The data identify the direct P_L result and the scaling of the B.3 discrepancy. They do not yet derive the full analytic finite-recoil correction to B.2/B.4 or establish whether the discrepancy is an intended low-energy truncation or a printed-formula omission."
        }
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("outputs") /
                        "vector_longitudinal_direct_projector_audit_2026-11-12.json")
    args = parser.parse_args()
    payload = build_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    if not (
        payload["summary"]["max_trace_vs_spinor_rel"] < 1e-8
        and payload["summary"]["max_correct_qWard_rel_amplitude"] < 1e-10
        and payload["summary"]["max_physical_vs_Ward_rel"] < 1e-5
        and payload["summary"]["all_direct_longitudinal_rates_positive"]
        and payload["summary"]["max_L_over_T_x2_shape_error_E_le_0p1_x_le_0p01"] < 1e-2
    ):
        raise SystemExit("Direct P_L projector acceptance failed")


if __name__ == "__main__":
    main()
