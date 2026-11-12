#!/usr/bin/env python3
"""A4b general-R_xi on-shell cut audit for the U(1)_X ss self-energy.

The vector propagator is decomposed into:
  T pole: mass m_X, residue weight 1, projector P_T = g - q q/m_X^2
  L pole: mass sqrt(xi)*m_X, residue weight xi, projector P_L = q q/(xi*m_X^2)

The script evaluates the two-body Cutkosky phase-space coefficients for:
  A'A' vector bubble, mixed A'a derivative bubble,
  Goldstone aa bubble, and complex ghost bubble.

It checks that their sum is independent of xi and equals the physical
three-polarization s -> A'A' width on the tree-level scalar mass shell.
"""
import math

BENCHMARKS = {
    "A": {"vS": 70.886458, "mX": 10.0},
    "B": {"vS": 315.0, "mX": 63.0},
}
XI_VALUES = (0.25, 0.5, 1.0, 2.0, 4.0, 10.0)

def beta_two_body(s, m1_sq, m2_sq):
    """Dimensionless two-body velocity; zero below the physical threshold."""
    if s <= 0.0:
        return 0.0
    threshold = (math.sqrt(m1_sq) + math.sqrt(m2_sq))**2
    if s <= threshold:
        return 0.0
    lam = (s - (math.sqrt(m1_sq) + math.sqrt(m2_sq))**2) * (
        s - (math.sqrt(m1_sq) - math.sqrt(m2_sq))**2
    )
    return math.sqrt(max(0.0, lam)) / s

def two_body_energies(s, m1_sq, m2_sq):
    """CM energies and q^2 for p -> particle 1 + particle 2."""
    root_s = math.sqrt(s)
    e1 = (s + m1_sq - m2_sq) / (2.0 * root_s)
    e2 = (s + m2_sq - m1_sq) / (2.0 * root_s)
    q2 = max(0.0, e1*e1 - m1_sq)
    return e1, e2, q2

def cut_coefficients(s, vS, mX, xi):
    """Return C_VV, C_Aa, C_ghost, C_aa, C_total.

    The convention is Im Pi_E(-s-i0) = C_total/(16 pi).
    Each C_i already includes the appropriate two-body beta factor.
    """
    gA = mX / vS
    lamS = s / (2.0 * vS*vS)  # tree relation m_s^2=2 lambda_S v_S^2
    ma_sq = xi * mX*mX

    # Vector poles and their propagator residues.
    modes = (
        ("T", mX*mX, 1.0),
        ("L", ma_sq, xi),
    )

    # Vector-vector bubble. The projector traces in four dimensions are
    # TT: 2+K, TL/LT: 1-K, LL: K, K=(q1.q2)^2/(m1^2 m2^2).
    c_vv = 0.0
    for type1, m1_sq, weight1 in modes:
        for type2, m2_sq, weight2 in modes:
            beta = beta_two_body(s, m1_sq, m2_sq)
            if beta == 0.0:
                continue
            dot12 = (s - m1_sq - m2_sq) / 2.0
            kinematic_K = dot12*dot12 / (m1_sq*m2_sq)
            if type1 == "T" and type2 == "T":
                trace = 2.0 + kinematic_K
            elif type1 == "L" and type2 == "L":
                trace = kinematic_K
            else:
                trace = 1.0 - kinematic_K
            c_vv += (
                -2.0 * gA*gA * mX*mX
                * weight1 * weight2 * beta * trace
            )

    # Mixed A'a bubble. q_a + q_V = p and u = p + q_a.
    # For the vector pole: N_L=(u.q_V)^2/m_V^2, N_T=u^2-N_L.
    c_mixed = 0.0
    root_s = math.sqrt(s)
    for vector_type, mV_sq, weight in modes:
        beta = beta_two_body(s, ma_sq, mV_sq)
        if beta == 0.0:
            continue
        e_a, e_v, q2 = two_body_energies(s, ma_sq, mV_sq)
        u_sq = (root_s + e_a)**2 - q2
        u_dot_qv = (root_s + e_a)*e_v + q2
        n_long = u_dot_qv*u_dot_qv / mV_sq
        n_trans = u_sq - n_long
        numerator = n_trans if vector_type == "T" else n_long
        c_mixed += gA*gA * weight * beta * numerator

    beta_aa = beta_two_body(s, ma_sq, ma_sq)
    c_ghost = xi*xi * gA*gA * mX*mX * beta_aa
    c_goldstone = -2.0 * lamS*lamS * vS*vS * beta_aa
    return c_vv, c_mixed, c_ghost, c_goldstone, (
        c_vv + c_mixed + c_ghost + c_goldstone
    )

def expected_total_coefficient(s, vS, mX):
    x = mX*mX/s
    beta = beta_two_body(s, mX*mX, mX*mX)
    if beta == 0.0:
        return 0.0
    return -s*s/(2.0*vS*vS) * (1.0 - 4.0*x + 12.0*x*x) * beta

def width_from_cut(ms, vS, mX, xi):
    coeff = cut_coefficients(ms*ms, vS, mX, xi)[-1]
    return -coeff/(16.0*math.pi*ms)

def direct_width(ms, vS, mX):
    if ms <= 2.0*mX:
        return 0.0
    x = (mX/ms)**2
    beta = math.sqrt(1.0-4.0*x)
    return ms**3/(32.0*math.pi*vS*vS) * (
        1.0-4.0*x+12.0*x*x
    ) * beta

def main():
    print("A4b general-R_xi on-shell cut audit")
    print("Convention: Im Pi_E(-m_s^2-i0) = C_total/(16 pi).")
    test_points = {
        "A": (100.0, 125.25, 150.0),
        "B": (150.0, 200.0),
    }
    max_residual = 0.0
    for name, masses in test_points.items():
        vS = BENCHMARKS[name]["vS"]
        mX = BENCHMARKS[name]["mX"]
        print(f"\nBenchmark {name}: vS={vS:.9f} GeV, mX={mX:.6g} GeV")
        for ms in masses:
            s = ms*ms
            expected = expected_total_coefficient(s, vS, mX)
            if expected == 0.0:
                continue
            print(f"  m_s={ms:.2f} GeV; C_expected={expected:.12g}")
            print("    xi       C_VV           C_Aa           C_ghost        C_aa           rel.res.")
            for xi in XI_VALUES:
                parts = cut_coefficients(s, vS, mX, xi)
                total = parts[-1]
                residual = abs(total-expected)/abs(expected)
                max_residual = max(max_residual, residual)
                assert residual < 5.0e-12
                w_cut = width_from_cut(ms, vS, mX, xi)
                w_direct = direct_width(ms, vS, mX)
                assert abs(w_cut-w_direct)/w_direct < 5.0e-12
                print(
                    f"    {xi:4.2f}  {parts[0]:13.6f} {parts[1]:13.6f}"
                    f" {parts[2]:13.6f} {parts[3]:13.6f} {residual:10.3e}"
                )
    # Feynman-gauge limit must reproduce the A4a channel coefficients.
    for name, ms in (("A", 125.25), ("B", 150.0)):
        vS = BENCHMARKS[name]["vS"]
        mX = BENCHMARKS[name]["mX"]
        s = ms*ms
        gA = mX/vS
        lamS = s/(2.0*vS*vS)
        beta = beta_two_body(s, mX*mX, mX*mX)
        parts = cut_coefficients(s, vS, mX, 1.0)
        expected = (
            -8.0*gA*gA*mX*mX*beta,
            gA*gA*(2.0*s+mX*mX)*beta,
            gA*gA*mX*mX*beta,
            -2.0*lamS*lamS*vS*vS*beta,
        )
        for actual, target in zip(parts[:4], expected):
            assert abs(actual-target) < 5.0e-12*max(1.0,abs(target))
    print(f"\nPASS: maximum relative xi-variation residual = {max_residual:.3e}")
    print("PASS: all tested gauges reproduce the physical three-polarization A'A' width.")
    print("LIMIT: this is the on-shell absorptive part; it is not the full real self-energy or complex-pole calculation.")

if __name__ == "__main__":
    main()
