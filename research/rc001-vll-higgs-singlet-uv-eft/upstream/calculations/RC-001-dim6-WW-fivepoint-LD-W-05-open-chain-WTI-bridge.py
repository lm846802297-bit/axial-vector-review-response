#!/usr/bin/env python3
"""RC-001 B2c-IVn-h/03: LD-W-05 actual S-F open-chain WTI bridge.

The B-side fermion WTI is inserted into the actual ordered S-F open chain.
The A scalar current V_A(k), k-W propagator, A scalar spectator, and heavy
spectator are retained. The P_L/P_R endpoint order is kept exactly as the
oriented WTI gives it; no premature identification with the separate R_FG
numerator is made.
"""
from itertools import product
import sympy as sp

I = sp.I
ETA = (1, -1, -1, -1)
METRIC = sp.diag(*ETA)
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
GAMMA = [sp.diag(1, 1, -1, -1)]
for sigma in SIGMA:
    GAMMA.append(sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), sigma),
        sp.Matrix.hstack(-sigma, sp.zeros(2)),
    ))
GAMMA5 = I * GAMMA[0] * GAMMA[1] * GAMMA[2] * GAMMA[3]
PL = (sp.eye(4) - GAMMA5) / 2
PR = (sp.eye(4) + GAMMA5) / 2
GAMMA_DOWN = [ETA[mu] * GAMMA[mu] for mu in range(4)]


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


def D_up(p):
    return METRIC / dot(p, p)


def contract_scalar_left(kernel, current, chain):
    out = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        out += (
            (ETA[mu] * current[mu]) * chain
            * GAMMA_DOWN[nu] * PL * kernel[mu, nu]
        )
    return sp.simplify(out)


def verify_oriented_B_fermion_wti():
    q = list(sp.symbols("qWTI0:4", real=True))
    r_w = list(sp.symbols("rBW0:4", real=True))
    r_y = add(r_w, q)
    s_w = slash(r_w) / dot(r_w, r_w)
    s_y = slash(r_y) / dot(r_y, r_y)
    lhs = s_y * slash(q) * PL * s_w
    rhs = PL * s_w - s_y * PR
    assert matrix_zero(lhs - rhs)
    return 16


def verify_common_k_B_yukawa_endpoint_route():
    k = list(sp.symbols("kRoute0:4", real=True))
    q = list(sp.symbols("qRoute0:4", real=True))
    p1 = list(sp.symbols("p1Route0:4", real=True))
    p2 = list(sp.symbols("p2Route0:4", real=True))
    p3 = list(sp.symbols("p3Route0:4", real=True))
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]

    # The B-side fermion endpoint is unshifted. Its B-line momentum and
    # the same heavy channel can be expressed from either adjacent vertex.
    r_b_w = add(k, p4)
    r_b_y_from_w = add(r_b_w, q)
    r_b_y_common = add(add(k, p4), q)
    h_from_right = add(add(k, p3), add(p4, q))
    h_from_left = sub(k, add(p1, p2))
    assert all(sp.simplify(r_b_y_from_w[i] - r_b_y_common[i]) == 0
               for i in range(4))
    assert all(sp.simplify(h_from_right[i] - h_from_left[i]) == 0
               for i in range(4))
    return 8


def rational_open_chain_diagnostic():
    # Same nonsingular rational point as the LD-W-05 endpoint-split audit.
    k = [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)]
    q = [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)]
    p1 = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    p2 = [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    kappa = add(k, q)

    r_a_y = sub(k, p2)
    r_a_w = sub(kappa, p2)
    r_b_w = add(k, p4)
    r_b_y = add(r_b_w, q)
    h = sub(k, add(p1, p2))
    v_a = [2 * p2[i] - k[i] for i in range(4)]
    m_e2 = sp.Integer(400)

    denominators = (
        dot(k, k), dot(kappa, kappa),
        dot(r_a_y, r_a_y), dot(r_a_w, r_a_w),
        dot(r_b_w, r_b_w), dot(r_b_y, r_b_y),
        dot(h, h) - m_e2,
    )
    assert all(value != 0 for value in denominators)

    s_b_w = slash(r_b_w) / dot(r_b_w, r_b_w)
    s_b_y = slash(r_b_y) / dot(r_b_y, r_b_y)
    heavy = slash(h) / (dot(h, h) - m_e2)
    scalar_a = sp.Rational(1, dot(r_a_y, r_a_y))

    # The actual ordered B-side fermion insertion, with the heavy chain
    # on its left and the A scalar current on the far left.
    chain_lhs = heavy * s_b_y * slash(q) * PL * s_b_w * scalar_a
    chain_rhs = heavy * (PL * s_b_w - s_b_y * PR) * scalar_a

    # The open internal-W Lorentz index is on the right of the fermion chain.
    open_index_checks = 0
    for nu in range(4):
        assert matrix_zero(
            chain_lhs * GAMMA_DOWN[nu] - chain_rhs * GAMMA_DOWN[nu]
        )
        open_index_checks += 16

    open_lhs = contract_scalar_left(D_up(k), v_a, chain_lhs)
    open_rhs = contract_scalar_left(D_up(k), v_a, chain_rhs)
    assert matrix_zero(open_lhs - open_rhs)
    nonzero_entries = sum(
        sp.simplify(open_lhs[i, j]) != 0
        for i, j in product(range(4), repeat=2)
    )
    assert nonzero_entries == 16

    endpoint_1 = contract_scalar_left(
        D_up(k), v_a, heavy * PL * s_b_w * scalar_a
    )
    endpoint_2 = contract_scalar_left(
        D_up(k), v_a, -heavy * s_b_y * PR * scalar_a
    )
    assert matrix_zero(open_lhs - endpoint_1 - endpoint_2)

    return {
        "denominators": denominators,
        "open_index_checks": open_index_checks,
        "contracted_entries": nonzero_entries,
        "open_chain": open_lhs,
    }


def main():
    wti = verify_oriented_B_fermion_wti()
    route = verify_common_k_B_yukawa_endpoint_route()
    diag = rational_open_chain_diagnostic()
    assert wti == 16 and route == 8
    assert diag["open_index_checks"] == 64
    assert diag["contracted_entries"] == 16

    print("RC-001 B2c-IVn-h/03: LD-W-05 actual S-F open-chain WTI bridge")
    print(f"PASS: oriented B-side fermion WTI ({wti}/16 Dirac components).")
    print(f"PASS: actual open Lorentz-index chain ({diag['open_index_checks']}/64 matrix components).")
    print("PASS: Feynman-gauge contraction with D(k) and V_A(k) (16/16 matrix components).")
    print("PASS: explicit two-endpoint RHS split (exact matrix equality).")
    print(f"PASS: B-side unshifted endpoint/heavy-channel momentum identities ({route}/8 vector components).")
    print(f"RATIONAL DENOMINATORS: {diag['denominators']}.")
    print(f"NONZERO CONTRACTED OPEN-CHAIN ENTRIES: {diag['contracted_entries']}/16.")
    print("RESULT: the B-side fermion WTI holds after insertion into the actual S-F open chain.")
    print("BOUNDARY: the A-side scalar-line/seagull q contacts remain a separate sub-block.")
    print("          The separate R_FG projector/order comparison remains open.")
    print("          No complete 24-graph Ward/LSZ/ST sum, loop integration, UV-EFT subtraction,")
    print("          or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
