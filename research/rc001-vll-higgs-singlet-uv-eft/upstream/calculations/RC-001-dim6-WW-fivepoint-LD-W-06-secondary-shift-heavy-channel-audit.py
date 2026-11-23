#!/usr/bin/env python3
"""RC-001 B2c-IVn-g/01: LD-W-06 secondary loop-shift/heavy-channel audit.

The purpose is to prevent a false pointwise or integrated telescope:
after expanding delta_A or delta_B, the -Delta_W term can be aligned with
the neighboring scalar propagator only by a second loop shift. That shift
also changes the heavy momentum h to h-q (A) or h+q (B). The shifted heavy
denominators are retained and compared exactly.
"""
from itertools import product
import sympy as sp

ETA = (1, -1, -1, -1)


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def add(a, b):
    return [sp.expand(a[i] + b[i]) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def scale(c, a):
    return [sp.expand(c * a[i]) for i in range(4)]


def verify_A_negative_DeltaW_shift():
    k = list(sp.symbols("kA0:4", real=True))
    q = list(sp.symbols("qA0:4", real=True))
    p2 = list(sp.symbols("p2A0:4", real=True))
    p3 = list(sp.symbols("p3A0:4", real=True))
    p1 = list(sp.symbols("p1A0:4", real=True))

    kap = add(k, q)
    h = sub(k, add(p1, p2))
    # Common-k A scalar endpoint factors in the -Delta_AW term.
    r_a_w = sub(kap, p2)
    r_b_y = add(kap, p3)
    v_a_line = sub(scale(2, p2), kap)
    v_b_3w = scale(-1, add(scale(2, p3), kap))

    # Secondary variable ell=k+q.
    ell = add(k, q)
    r_a_y_ell = sub(ell, p2)
    r_b_w_ell = add(ell, p3)
    v_a_3w_ell = sub(scale(2, p2), ell)
    v_b_line_ell = scale(-1, add(scale(2, p3), ell))
    h_ell = sub(ell, add(p1, p2))

    maps = (
        (r_a_w, r_a_y_ell),
        (r_b_y, r_b_w_ell),
        (v_a_line, v_a_3w_ell),
        (v_b_3w, v_b_line_ell),
    )
    assert all(sp.simplify(maps[n][0][i] - maps[n][1][i]) == 0
               for n in range(4) for i in range(4))
    # The old heavy channel is h(ell)-q, not h(ell).
    assert all(sp.simplify(h[i] - (h_ell[i] - q[i])) == 0
               for i in range(4))
    return 16, 4


def verify_B_negative_DeltaW_shift():
    k = list(sp.symbols("kB0:4", real=True))
    q = list(sp.symbols("qB0:4", real=True))
    p2 = list(sp.symbols("p2B0:4", real=True))
    p3 = list(sp.symbols("p3B0:4", real=True))
    p1 = list(sp.symbols("p1B0:4", real=True))

    h = sub(k, add(p1, p2))
    # Common-k B scalar endpoint factors in the -Delta_BW term.
    r_a_y = sub(k, p2)
    r_b_w = add(k, p3)
    v_a_3w = sub(scale(2, p2), k)
    v_b_line = scale(-1, add(scale(2, p3), k))

    # Secondary variable ell=k-q, hence old k=ell+q.
    ell = sub(k, q)
    r_a_w_ell = sub(add(ell, q), p2)
    r_b_y_ell = add(add(ell, q), p3)
    v_a_line_ell = sub(scale(2, p2), add(ell, q))
    v_b_3w_ell = scale(-1, add(scale(2, p3), add(ell, q)))
    h_ell = sub(ell, add(p1, p2))

    maps = (
        (r_a_y, r_a_w_ell),
        (r_b_w, r_b_y_ell),
        (v_a_3w, v_a_line_ell),
        (v_b_line, v_b_3w_ell),
    )
    assert all(sp.simplify(maps[n][0][i] - maps[n][1][i]) == 0
               for n in range(4) for i in range(4))
    # The old heavy channel is h(ell)+q, not h(ell).
    assert all(sp.simplify(h[i] - (h_ell[i] + q[i])) == 0
               for i in range(4))
    return 16, 4


def verify_shifted_heavy_denominators():
    h = list(sp.symbols("h0:4", real=True))
    q = list(sp.symbols("q0:4", real=True))
    m_e2 = sp.symbols("M_E2", real=True)
    h0 = dot(h, h) - m_e2
    h_a = dot(sub(h, q), sub(h, q)) - m_e2
    h_b = dot(add(h, q), add(h, q)) - m_e2
    assert sp.simplify(h_a - h0 - (dot(q, q) - 2 * dot(h, q))) == 0
    assert sp.simplify(h_b - h0 - (dot(q, q) + 2 * dot(h, q))) == 0
    assert sp.simplify(h_a - h0) != 0
    assert sp.simplify(h_b - h0) != 0
    return 2


def rational_diagnostic():
    k = [sp.Integer(6), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    q = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(0)]
    p1 = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    p2 = [sp.Integer(0), sp.Integer(2), sp.Integer(0), sp.Integer(1)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    h = sub(k, add(p1, p2))
    h_minus_q = sub(h, q)
    h_plus_q = add(h, q)
    m_e2 = sp.Integer(400)

    # Original and shifted scalar/W denominators in the two -Delta_W terms.
    kap = add(k, q)
    r_a = sub(k, p2)
    r_a_w = sub(kap, p2)
    r_b_y = add(kap, p3)
    r_b_w = add(k, p3)

    d_a_minus = (
        dot(kap, kap), dot(r_b_y, r_b_y),
        dot(r_a_w, r_a_w), dot(h, h) - m_e2,
    )
    d_b_minus = (
        dot(k, k), dot(r_a, r_a),
        dot(r_b_w, r_b_w), dot(h, h) - m_e2,
    )
    d_a_shifted = (
        dot(k, k), dot(add(k, p3), add(k, p3)),
        dot(sub(k, p2), sub(k, p2)),
        dot(h_minus_q, h_minus_q) - m_e2,
    )
    d_b_shifted = (
        dot(kap, kap), dot(sub(kap, p2), sub(kap, p2)),
        dot(add(kap, p3), add(kap, p3)),
        dot(h_plus_q, h_plus_q) - m_e2,
    )

    h0 = dot(h, h) - m_e2
    ha = dot(h_minus_q, h_minus_q) - m_e2
    hb = dot(h_plus_q, h_plus_q) - m_e2
    assert all(x != 0 for x in d_a_minus + d_b_minus + d_a_shifted + d_b_shifted)
    assert len({h0, ha, hb}) == 3
    return {
        "k2": dot(k, k), "kappa2": dot(kap, kap),
        "h": tuple(h), "h2": dot(h, h),
        "h_minus_q": tuple(h_minus_q), "h_minus_q2": dot(h_minus_q, h_minus_q),
        "h_plus_q": tuple(h_plus_q), "h_plus_q2": dot(h_plus_q, h_plus_q),
        "H0": h0, "HA": ha, "HB": hb,
        "A_minus_den": d_a_minus, "A_shifted_den": d_a_shifted,
        "B_minus_den": d_b_minus, "B_shifted_den": d_b_shifted,
    }


def main():
    a = verify_A_negative_DeltaW_shift()
    b = verify_B_negative_DeltaW_shift()
    heavy = verify_shifted_heavy_denominators()
    diag = rational_diagnostic()
    assert a == b == (16, 4)
    assert heavy == 2
    print("RC-001 B2c-IVn-g/01: LD-W-06 secondary shift/heavy-channel audit")
    print(f"PASS: A-side -Delta_AW secondary shift k'=k+q ({a[0]}/16 vector components, {a[1]}/4 factor maps).")
    print(f"PASS: B-side -Delta_BW secondary shift k'=k-q ({b[0]}/16 vector components, {b[1]}/4 factor maps).")
    print(f"PASS: generic shifted heavy-denominator identities ({heavy}/2 exact identities).")
    print(f"RATIONAL POINT: k^2={diag['k2']}, kappa^2={diag['kappa2']}, h={diag['h']}, h^2={diag['h2']}.")
    print(f"  H0={diag['H0']}; HA=(h-q)^2-M_E^2={diag['HA']}; HB=(h+q)^2-M_E^2={diag['HB']}.")
    print(f"  A -Delta_W denominator before/after shift: {diag['A_minus_den']} -> {diag['A_shifted_den']}.")
    print(f"  B -Delta_W denominator before/after shift: {diag['B_minus_den']} -> {diag['B_shifted_den']}.")
    print("RESULT: the A and B secondary shifts align the scalar/W/current factors,")
    print("        but the heavy channel becomes h-q and h+q, respectively.")
    print("BOUNDARY: these shifted terms are not identified with the h-channel three-W integrand.")
    print("          Their cancellation must be tested against the corresponding Yukawa-endpoint/LSZ terms.")
    print("          No physical non-cancellation or complete Ward/ST identity is claimed.")


if __name__ == "__main__":
    main()
