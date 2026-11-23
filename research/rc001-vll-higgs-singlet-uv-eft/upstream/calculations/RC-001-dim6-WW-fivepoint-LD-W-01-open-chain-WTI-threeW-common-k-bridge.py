#!/usr/bin/env python3
"""RC-001 B2c-IVn-h/01: LD-W-01 complete open-chain WTI/three-W bridge.

This adds the actual A- and B-fermion-line q-contracted open chains to the
previous LD-W-01 commutator/three-W R_FG audit. It checks the oriented WTIs,
the A-side k_old=k+q map, the two W-propagator denominator alignments, and
the actual three-W R_FG numerator. The first Yukawa-endpoint terms remain
explicit; no full 24-graph cancellation is claimed.
"""
from itertools import product
import sympy as sp

I = sp.I
ETA = (1, -1, -1, -1)
GAMMA = [sp.diag(1, 1, -1, -1)]
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
for sigma in SIGMA:
    GAMMA.append(sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), sigma),
        sp.Matrix.hstack(-sigma, sp.zeros(2)),
    ))
GAMMA5 = I * GAMMA[0] * GAMMA[1] * GAMMA[2] * GAMMA[3]
PL = (sp.eye(4) - GAMMA5) / 2
PR = (sp.eye(4) + GAMMA5) / 2


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def add(a, b):
    return [sp.expand(a[i] + b[i]) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def slash(a):
    return sum((ETA[i] * a[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def matrix_zero(m):
    return all(sp.simplify(m[i, j]) == 0
               for i in range(m.rows) for j in range(m.cols))


def contract_FG(m):
    return sum((
        ETA[mu] * GAMMA[mu] * m * GAMMA[mu] * PL
        for mu in range(4)
    ), sp.zeros(4))


def verify_actual_open_chain_wtis():
    k = [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)]
    q = [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)]
    p1 = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    p2 = [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)]
    p3 = [sp.Integer(2), sp.Integer(1), sp.Integer(1), sp.Integer(1)]
    p4 = [-q[i] - p1[i] - p2[i] - p3[i] for i in range(4)]

    r_a_w = sub(k, p1)
    r_a_y = sub(r_a_w, q)
    r_b_w = add(k, p4)
    r_b_y = add(r_b_w, q)
    h = sub(k, add(p1, p2))
    h_a = sub(h, q)

    s_a_w = -slash(r_a_w) / dot(r_a_w, r_a_w)
    s_a_y = -slash(r_a_y) / dot(r_a_y, r_a_y)
    s_b_w = slash(r_b_w) / dot(r_b_w, r_b_w)
    s_b_y = slash(r_b_y) / dot(r_b_y, r_b_y)

    # The two oriented fermion WTIs.
    lhs_a = s_a_w * slash(q) * PL * s_a_y
    rhs_a = s_a_w * PR - PL * s_a_y
    lhs_b = s_b_y * slash(q) * PL * s_b_w
    rhs_b = PL * s_b_w - s_b_y * PR
    assert matrix_zero(lhs_a - rhs_a)
    assert matrix_zero(lhs_b - rhs_b)

    # Insert the actual heavy and opposite-fermion chains and contract
    # the internal W Lorentz indices in Feynman gauge.
    chain_a_lhs = contract_FG(s_a_w * slash(q) * PL * s_a_y
                              * slash(h_a) * s_b_w)
    chain_a_rhs = contract_FG((s_a_w * PR - PL * s_a_y)
                              * slash(h_a) * s_b_w)
    chain_b_lhs = contract_FG(s_a_w * slash(h) * s_b_y
                              * slash(q) * PL * s_b_w)
    chain_b_rhs = contract_FG(s_a_w * slash(h)
                              * (PL * s_b_w - s_b_y * PR))
    assert matrix_zero(chain_a_lhs - chain_a_rhs)
    assert matrix_zero(chain_b_lhs - chain_b_rhs)

    denominators = (
        dot(k, k), dot(add(k, q), add(k, q)),
        dot(r_a_w, r_a_w), dot(r_a_y, r_a_y),
        dot(r_b_w, r_b_w), dot(r_b_y, r_b_y),
        dot(h, h) - 400, dot(h_a, h_a) - 400,
    )
    assert all(value != 0 for value in denominators)
    return denominators, (16, 16), (16, 16)


def verify_A_yukawa_endpoint_common_k_map():
    k = list(sp.symbols("kRoute0:4", real=True))
    q = list(sp.symbols("qRoute0:4", real=True))
    p1 = list(sp.symbols("p1Route0:4", real=True))
    p2 = list(sp.symbols("p2Route0:4", real=True))
    p4 = list(sp.symbols("p4Route0:4", real=True))
    k_old = add(k, q)
    kap = add(k, q)

    # A-side Yukawa endpoint before the common-k shift.
    r_a_y_old = sub(k_old, add(p1, q))
    h_a_old = sub(sub(k_old, add(p1, p2)), q)
    r_b_w_old = add(k_old, p4)

    # Common-k reference after k_old=k+q.
    r_a_w = sub(k, p1)
    h = sub(k, add(p1, p2))
    r_b_y = add(kap, p4)
    assert all(sp.simplify(r_a_y_old[i] - r_a_w[i]) == 0
               for i in range(4))
    assert all(sp.simplify(h_a_old[i] - h[i]) == 0
               for i in range(4))
    assert all(sp.simplify(r_b_w_old[i] - r_b_y[i]) == 0
               for i in range(4))
    assert all(sp.simplify(k_old[i] - kap[i]) == 0
               for i in range(4))
    return 16


def verify_denominator_alignment():
    k = list(sp.symbols("kD0:4", real=True))
    q = list(sp.symbols("qD0:4", real=True))
    p1 = list(sp.symbols("p1D0:4", real=True))
    p2 = list(sp.symbols("p2D0:4", real=True))
    p4 = list(sp.symbols("p4D0:4", real=True))
    kap = add(k, q)
    r_a = sub(k, p1)
    r_b_y = add(kap, p4)
    h = sub(k, add(p1, p2))
    m_e2 = sp.symbols("M_E2", real=True)

    d_3w = (
        dot(k, k) * dot(kap, kap) * dot(r_a, r_a)
        * dot(r_b_y, r_b_y) * (dot(h, h) - m_e2)
    )
    # A-side second WTI endpoint after k_old=k+q: W momentum kappa.
    d_a_yukawa_after_shift = (
        dot(kap, kap) * dot(r_a, r_a)
        * dot(r_b_y, r_b_y) * (dot(h, h) - m_e2)
    )
    # B-side second WTI endpoint in the unshifted common-k routing: W momentum k.
    d_b_yukawa_common = (
        dot(k, k) * dot(r_a, r_a)
        * dot(r_b_y, r_b_y) * (dot(h, h) - m_e2)
    )
    assert sp.simplify(d_a_yukawa_after_shift - d_3w / dot(k, k)) == 0
    assert sp.simplify(d_b_yukawa_common - d_3w / dot(kap, kap)) == 0
    return 2


def verify_actual_RFG_remainder():
    k = [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)]
    q = [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)]
    p1 = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    p2 = [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)]
    p3 = [sp.Integer(2), sp.Integer(1), sp.Integer(1), sp.Integer(1)]
    p4 = [-q[i] - p1[i] - p2[i] - p3[i] for i in range(4)]
    kap = add(k, q)
    r_a = sub(k, p1)
    r_b_y = add(add(k, p4), q)
    h = sub(k, add(p1, p2))
    # The stripped loop chain excludes the final P_L. It is restored after
    # the right internal-W current, hence after the last slash(k).
    chain = -slash(r_a) * slash(h) * slash(r_b_y)

    n_01 = (
        slash(k) * chain * slash(k) * PL
        - slash(kap) * chain * slash(kap) * PL
    )
    direct = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        coefficient = ETA[mu] * ETA[nu] * (
            k[mu] * k[nu] - kap[mu] * kap[nu]
        )
        direct += GAMMA[mu] * chain * GAMMA[nu] * PL * coefficient
    assert matrix_zero(direct - n_01)
    nonzero = sum(
        sp.simplify(n_01[i, j]) != 0
        for i, j in product(range(4), repeat=2)
    )
    assert nonzero == 16
    return nonzero


def main():
    den, open_wti, full_chain = verify_actual_open_chain_wtis()
    route = verify_A_yukawa_endpoint_common_k_map()
    denominator_checks = verify_denominator_alignment()
    rfg = verify_actual_RFG_remainder()
    assert open_wti == full_chain == (16, 16)
    assert route == 16 and denominator_checks == 2 and rfg == 16

    print("RC-001 B2c-IVn-h/01: LD-W-01 open-chain WTI/three-W bridge")
    print(f"PASS: actual A/B oriented fermion WTIs ({open_wti[0]+open_wti[1]}/32 Dirac components).")
    print(f"PASS: actual Feynman-gauge open chains with h-q/h ({full_chain[0]+full_chain[1]}/32 matrix components).")
    print(f"PASS: A-side Yukawa endpoint common-k shift ({route}/16 vector components).")
    print(f"PASS: A-shifted and B-unshifted WTI endpoint denominators align with the two three-W W propagators ({denominator_checks}/2 identities).")
    print(f"PASS: actual LD-W-01 R_FG direct contraction ({rfg}/16 nonzero numerator entries).")
    print(f"RATIONAL DENOMINATORS: {den}.")
    print("RESULT: the A-side second WTI endpoint maps to the kappa-W part of the three-W reference;")
    print("        the B-side second endpoint is already in the k-W common routing.")
    print("BOUNDARY: the first A/B endpoint terms retain their own Yukawa-channel denominators.")
    print("          Their local charge factors are checked separately; no full 24-graph or LSZ/ST sum is claimed.")


if __name__ == "__main__":
    main()
