#!/usr/bin/env python3
"""RC-001 B2c-IVn-h/02: LD-W-02 actual F-S open-chain WTI bridge.

The A-side external-W insertion is contracted inside the actual open chain
ending on the B scalar current V_B(k+q). The common-k sub-block uses the
kappa-W propagator. The scalar and heavy spectator factors are retained.
This is a local WTI identity, not the full LD-W-02 Ward/LSZ/ST sum.
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


def contract_scalar(kernel, chain, current):
    out = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        out += (
            GAMMA_DOWN[mu] * chain
            * (ETA[nu] * current[nu]) * kernel[mu, nu]
        )
    return sp.simplify(out)


def verify_oriented_A_fermion_wti():
    q = list(sp.symbols("qWTI0:4", real=True))
    r_w = list(sp.symbols("rAW0:4", real=True))
    r_y = sub(r_w, q)
    s_w = -slash(r_w) / dot(r_w, r_w)
    s_y = -slash(r_y) / dot(r_y, r_y)
    lhs = s_w * slash(q) * PL * s_y
    rhs = s_w * PR - PL * s_y
    assert matrix_zero(lhs - rhs)
    return 16


def verify_common_k_A_yukawa_endpoint_route():
    k = list(sp.symbols("kRoute0:4", real=True))
    q = list(sp.symbols("qRoute0:4", real=True))
    p1 = list(sp.symbols("p1Route0:4", real=True))
    p2 = list(sp.symbols("p2Route0:4", real=True))
    p3 = list(sp.symbols("p3Route0:4", real=True))
    k_old = add(k, q)
    kappa = add(k, q)

    mapped = (
        sub(sub(k_old, p1), q),             # r_A^Y(k_old)
        add(k_old, p3),                     # r_B^W(k_old)
        sub(sub(k_old, add(p1, p2)), q),    # h_A(k_old)
        k_old,                              # internal W momentum
    )
    targets = (
        sub(k, p1),                         # r_A^W(k)
        add(add(k, p3), q),                 # r_B^Y(k)
        sub(k, add(p1, p2)),                # h(k)
        kappa,
    )
    assert all(
        sp.simplify(mapped[n][mu] - targets[n][mu]) == 0
        for n in range(4) for mu in range(4)
    )
    return 16


def rational_open_chain_diagnostic():
    # Same nonsingular rational point as the LD-W-02 endpoint-split audit.
    k = [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)]
    q = [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)]
    p1 = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    p2 = [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    kappa = add(k, q)

    r_aw = sub(k, p1)
    r_ay = sub(r_aw, q)
    r_bw = add(k, p3)
    r_by = add(r_bw, q)
    h = sub(k, add(p1, p2))
    h_a = sub(h, q)
    v_b_kappa = [-(2 * p3[i] + kappa[i]) for i in range(4)]
    m_e2 = sp.Integer(400)

    denominators = (
        dot(k, k), dot(kappa, kappa),
        dot(r_aw, r_aw), dot(r_ay, r_ay),
        dot(r_bw, r_bw), dot(r_by, r_by),
        dot(h, h) - m_e2, dot(h_a, h_a) - m_e2,
    )
    assert all(value != 0 for value in denominators)

    s_aw = -slash(r_aw) / dot(r_aw, r_aw)
    s_ay = -slash(r_ay) / dot(r_ay, r_ay)
    heavy_a = slash(h_a) * PL / (dot(h_a, h_a) - m_e2)
    scalar_b = sp.Rational(1, dot(r_by, r_by))

    # Full A-side fermion-line WTI insertion, followed by the actual
    # heavy-fermion and B-scalar spectators in the common-k routing.
    chain_lhs = s_aw * slash(q) * PL * s_ay * heavy_a * scalar_b
    chain_rhs = (s_aw * PR - PL * s_ay) * heavy_a * scalar_b

    # Keep the internal W Lorentz index open before contracting the
    # Feynman-gauge propagator and V_B(k+q).
    open_index_checks = 0
    for mu in range(4):
        assert matrix_zero(
            GAMMA_DOWN[mu] * chain_lhs - GAMMA_DOWN[mu] * chain_rhs
        )
        open_index_checks += 16

    open_lhs = contract_scalar(D_up(kappa), chain_lhs, v_b_kappa)
    open_rhs = contract_scalar(D_up(kappa), chain_rhs, v_b_kappa)
    assert matrix_zero(open_lhs - open_rhs)
    nonzero_entries = sum(
        sp.simplify(open_lhs[i, j]) != 0
        for i, j in product(range(4), repeat=2)
    )
    assert nonzero_entries == 16

    # Explicit endpoint split of the contracted open chain.
    endpoint_1 = contract_scalar(
        D_up(kappa), s_aw * PR * heavy_a * scalar_b, v_b_kappa
    )
    endpoint_2 = contract_scalar(
        D_up(kappa), -PL * s_ay * heavy_a * scalar_b, v_b_kappa
    )
    assert matrix_zero(open_lhs - endpoint_1 - endpoint_2)

    return {
        "denominators": denominators,
        "open_index_checks": open_index_checks,
        "contracted_entries": nonzero_entries,
        "open_chain": open_lhs,
    }


def main():
    wti = verify_oriented_A_fermion_wti()
    route = verify_common_k_A_yukawa_endpoint_route()
    diag = rational_open_chain_diagnostic()
    assert wti == 16 and route == 16
    assert diag["open_index_checks"] == 64
    assert diag["contracted_entries"] == 16

    print("RC-001 B2c-IVn-h/02: LD-W-02 actual F-S open-chain WTI bridge")
    print(f"PASS: oriented A-side fermion WTI ({wti}/16 Dirac components).")
    print(f"PASS: actual open Lorentz-index chain ({diag['open_index_checks']}/64 matrix components).")
    print("PASS: Feynman-gauge contraction with D(kappa) and V_B(kappa) (16/16 matrix components).")
    print("PASS: explicit two-endpoint RHS split (exact matrix equality).")
    print(f"PASS: A-side common-k Yukawa endpoint route ({route}/16 vector components).")
    print(f"RATIONAL DENOMINATORS: {diag['denominators']}.")
    print(f"NONZERO CONTRACTED OPEN-CHAIN ENTRIES: {diag['contracted_entries']}/16.")
    print("RESULT: the A-side fermion WTI holds after insertion into the actual F-S open chain.")
    print("BOUNDARY: the B-side scalar-line/seagull q contacts remain a separate sub-block.")
    print("          No cancellation of those contacts, complete 24-graph Ward/LSZ/ST sum,")
    print("          loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
