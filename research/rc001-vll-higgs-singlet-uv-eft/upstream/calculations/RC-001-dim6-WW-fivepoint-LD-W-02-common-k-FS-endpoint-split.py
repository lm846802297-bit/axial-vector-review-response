#!/usr/bin/env python3
"""RC-001 B2c-IVn-f/02: exact LD-W-02 F-S endpoint split.

The audit keeps separate:
1. the A-side fermion-WTI / three-W sub-block, whose B scalar current is V_B(k+q);
2. the B-side scalar-line plus seagull kernel, whose internal-W current is V_B(k).

It derives the exact re-expression V_B(k)=V_B(k+q)+q and retains the resulting
symmetric and commutator q-contact terms. No physical non-cancellation is
claimed; those terms must be combined with the full endpoint/LSZ STI sector.
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


def scale(c, a):
    return [sp.expand(c * a[i]) for i in range(4)]


def slash(a):
    return sum((ETA[i] * a[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def matrix_zero(m):
    return all(sp.simplify(m[i, j]) == 0
               for i in range(m.rows) for j in range(m.cols))


def metric(mu, nu):
    return sp.Integer(ETA[mu]) if mu == nu else sp.Integer(0)


def K_down(p):
    p_cov = sp.Matrix([ETA[i] * p[i] for i in range(4)])
    return sp.expand(dot(p, p) * METRIC - p_cov * p_cov.T)


def D_up(p):
    return METRIC / dot(p, p)


def gamma3(alpha, mu, nu, q, k):
    return (
        metric(alpha, mu) * ETA[nu] * (q[nu] - k[nu])
        + metric(mu, nu) * ETA[alpha] * (2*k[alpha] + q[alpha])
        + metric(nu, alpha) * ETA[mu] * (-k[mu] - 2*q[mu])
    )


def physical_field_action(tensor, slot, a, ix):
    """Physical actions for (bar L,H,Hdagger,L), slots 0 and 2."""
    i, j, kk, ell = ix
    out = sp.Integer(0)
    if slot == 0:  # R_barL = -t^T
        for m in range(2):
            out += -SIGMA[a][m, i] / 2 * tensor(m, j, kk, ell)
    elif slot == 2:  # R_Hdagger = -t^T
        for m in range(2):
            out += -SIGMA[a][m, kk] / 2 * tensor(i, j, m, ell)
    else:
        raise ValueError("LD-W-02 uses bar-L slot 0 and Hdagger slot 2")
    return sp.simplify(out)


def apply_phys(tensor, slot, a):
    return lambda *ix: physical_field_action(tensor, slot, a, ix)


def T0(i, j, k, ell):
    return sp.Integer(int(i == j and k == ell))


def pair_tensor(a_slot, b_slot):
    return lambda *ix: sp.simplify(sum(
        physical_field_action(apply_phys(T0, b_slot, b), a_slot, b, ix)
        for b in range(3)
    ))


def G_tensor(a_slot, b_slot, external_a):
    return lambda *ix: sp.simplify(sum(
        sp.LeviCivita(external_a, b, c)
        * physical_field_action(apply_phys(T0, b_slot, c), a_slot, b, ix)
        for b, c in product(range(3), repeat=2)
    ))


def verify_A_fermion_wti():
    q = list(sp.symbols("qA0:4", real=True))
    r_w = list(sp.symbols("rAW0:4", real=True))
    r_y = sub(r_w, q)
    s_w = -slash(r_w) / dot(r_w, r_w)
    s_y = -slash(r_y) / dot(r_y, r_y)
    lhs = s_w * slash(q) * PL * s_y
    rhs = s_w * PR - PL * s_y
    assert matrix_zero(lhs - rhs)
    return 16


def verify_B_scalar_wti_and_current_rebase():
    k = list(sp.symbols("kS0:4", real=True))
    q = list(sp.symbols("qS0:4", real=True))
    p = list(sp.symbols("pB0:4", real=True))
    kap = add(k, q)
    r_w = add(k, p)
    r_y = add(kap, p)
    v_k = scale(-1, add(scale(2, p), k))
    v_kap = scale(-1, add(scale(2, p), kap))
    dy = 1 / dot(r_y, r_y)
    dw = 1 / dot(r_w, r_w)
    delta = dy - dw

    # Opposite B-side scalar WTI orientation.
    lhs = dot(q, add(r_w, r_y)) / (dot(r_w, r_w) * dot(r_y, r_y))
    assert sp.simplify(lhs - (dw - dy)) == 0

    # Exact current shift and the complete C_B re-expression.
    assert all(sp.simplify(v_k[i] - v_kap[i] - q[i]) == 0 for i in range(4))
    g2, sym, comm = sp.symbols("g2 S_B G_AB")
    c_original = [
        g2 * (sp.Rational(1, 2)*delta*v_k[i]*sym
              + dy*q[i]*sym
              + I*sp.Rational(1, 2)*delta*v_k[i]*comm)
        for i in range(4)
    ]
    c_rebased = [
        g2 * (
            sp.Rational(1, 2)*delta*v_kap[i]*sym
            + (sp.Rational(1, 2)*delta + dy)*q[i]*sym
            + I*sp.Rational(1, 2)*delta*v_kap[i]*comm
            + I*sp.Rational(1, 2)*delta*q[i]*comm
        )
        for i in range(4)
    ]
    assert all(sp.simplify(c_original[i] - c_rebased[i]) == 0 for i in range(4))
    return 1, 4


def verify_A_side_fermion_route_to_three_w():
    k = list(sp.symbols("kRoute0:4", real=True))
    q = list(sp.symbols("qRoute0:4", real=True))
    p1 = list(sp.symbols("p1Route0:4", real=True))
    p2 = list(sp.symbols("p2Route0:4", real=True))
    p3 = list(sp.symbols("p3Route0:4", real=True))
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    kap = add(k, q)
    r_a = sub(k, p1)
    r_by = add(add(k, p3), q)
    h = sub(k, add(p1, p2))
    v_b_kap = scale(-1, add(scale(2, p3), kap))

    # A-side Yukawa endpoint after k_old = k+q.
    mapped = (
        sub(sub(add(k, q), p1), q),
        add(add(k, q), p3),
        sub(sub(add(k, q), add(p1, p2)), q),
        scale(-1, add(scale(2, p3), add(k, q))),
        kap,
    )
    targets = (r_a, r_by, h, v_b_kap, kap)
    assert all(
        sp.simplify(mapped[n][mu] - targets[n][mu]) == 0
        for n in range(5) for mu in range(4)
    )

    me2 = sp.symbols("M_E2", real=True)
    spectator = dot(r_a, r_a)*dot(r_by, r_by)*(dot(h, h)-me2)
    d3 = dot(k, k)*dot(kap, kap)*spectator
    d_a_y = dot(kap, kap)*spectator
    d_b_y = dot(k, k)*spectator
    assert sp.simplify(d3/dot(k, k)-d_a_y) == 0
    assert sp.simplify(d3/dot(kap, kap)-d_b_y) == 0
    return 20, 2


def verify_weak_ordering():
    a_slot, b_slot = 0, 2
    checks_comm = checks_seagull = 0
    for external_a in range(3):
        g = G_tensor(a_slot, b_slot, external_a)
        seed = pair_tensor(a_slot, b_slot)
        graph_b = apply_phys(seed, b_slot, external_a)
        reverse_b = lambda *ix: sp.simplify(sum(
            physical_field_action(
                apply_phys(apply_phys(T0, b_slot, external_a), a_slot, b),
                b_slot, b, ix
            )
            for b in range(3)
        ))
        seagull = lambda *ix: sp.simplify(graph_b(*ix) + reverse_b(*ix))
        expected_seagull = lambda *ix: sp.Rational(1, 2) * physical_field_action(
            T0, a_slot, external_a, ix
        )
        for ix in product(range(2), repeat=4):
            assert sp.simplify(graph_b(*ix)-reverse_b(*ix)-I*g(*ix)) == 0
            assert sp.simplify(seagull(*ix)-expected_seagull(*ix)) == 0
            checks_comm += 1
            checks_seagull += 1
    return checks_comm, checks_seagull


def contract_scalar_kernel(kernel, chain, scalar_current):
    out = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        out += GAMMA_DOWN[mu] * chain * (ETA[nu] * scalar_current[nu]) * kernel[mu, nu]
    return out


def rational_diagnostic():
    k = [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)]
    q = [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)]
    p1 = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    p2 = [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = [-p1[i]-p2[i]-p3[i]-q[i] for i in range(4)]
    kap = add(k, q)
    r_a = sub(k, p1)
    r_bw = add(k, p3)
    r_by = add(r_bw, q)
    h = sub(k, add(p1, p2))
    v_b_k = scale(-1, add(scale(2, p3), k))
    v_b_kap = scale(-1, add(scale(2, p3), kap))
    dy = sp.Rational(1, dot(r_by, r_by))
    dw = sp.Rational(1, dot(r_bw, r_bw))
    delta = dy - dw
    me2 = sp.Integer(400)
    den = (
        dot(k, k), dot(kap, kap), dot(r_a, r_a),
        dot(r_bw, r_bw), dot(r_by, r_by), dot(h, h)-me2
    )
    assert all(x != 0 for x in den)
    assert delta != 0

    # Actual three-W R_FG numerator with the B scalar current V_B(k+q).
    chain = -slash(r_a) * slash(h) * PL
    n02 = (
        slash(k)*chain*dot(v_b_kap, k)
        - slash(kap)*chain*dot(v_b_kap, kap)
    )
    rfg = (
        sp.Matrix(k)*sp.Matrix(k).T
        - sp.Matrix(kap)*sp.Matrix(kap).T
    )/(dot(k,k)*dot(kap,kap))
    d0, dq = D_up(k), D_up(kap)
    kernel = sp.simplify(dq*(K_down(kap)-K_down(k))*d0)
    line = contract_scalar_kernel(dq-d0, chain, v_b_kap)
    three = contract_scalar_kernel(kernel, chain, v_b_kap)
    rfg_matrix = contract_scalar_kernel(rfg, chain, v_b_kap)
    assert matrix_zero(line+three-rfg_matrix)
    assert matrix_zero(rfg_matrix-n02/(dot(k,k)*dot(kap,kap)))

    # The re-based commutator q-contact is a nonzero matrix at this point.
    q_contact = (I*sp.Rational(1,2)*delta
                 * slash(q)*(-slash(r_a))*slash(h)/dot(k,k))
    q_nonzero = sum(sp.simplify(q_contact[i,j]) != 0
                    for i,j in product(range(4),repeat=2))
    n_nonzero = sum(sp.simplify(n02[i,j]) != 0
                    for i,j in product(range(4),repeat=2))
    assert q_nonzero == 16 and n_nonzero == 16
    return den, delta, n_nonzero, q_nonzero


def main():
    wti = verify_A_fermion_wti()
    scalar_wti, rebase = verify_B_scalar_wti_and_current_rebase()
    route, den_checks = verify_A_side_fermion_route_to_three_w()
    weak_comm, weak_sg = verify_weak_ordering()
    den, delta, n_nonzero, q_nonzero = rational_diagnostic()

    print("RC-001 B2c-IVn-f/02: LD-W-02 exact F-S endpoint split")
    print(f"PASS: A-side oriented fermion WTI ({wti}/16 Dirac components).")
    print(f"PASS: B-side scalar WTI and V_B(k)-V_B(k+q)=q ({scalar_wti}/1 and {rebase}/4 identities/components).")
    print(f"PASS: A-side fermion Yukawa-endpoint map to the three-W B scalar current ({route}/20 vector components).")
    print(f"PASS: three-W/single-W denominator factors ({den_checks}/2 exact identities).")
    print(f"PASS: B-side physical weak commutator ordering ({weak_comm}/48 weak components).")
    print(f"PASS: B-side scalar seagull anticommutator ({weak_sg}/48 weak components).")
    print(f"PASS: actual LD-W-02 R_FG current contraction at rational point ({n_nonzero}/16 nonzero entries).")
    print(f"PASS: re-based B-scalar commutator q-contact is explicit and nonzero ({q_nonzero}/16 matrix entries); delta={delta}.")
    print(f"RATIONAL DIAGNOSTIC: denominator factors={den}.")
    print("RESULT: the A-side fermion/three-W sub-block uses V_B(k+q); the B-side scalar-line/seagull")
    print("        kernel uses V_B(k) and splits exactly into V_B(k+q) plus explicit q contacts.")
    print("BOUNDARY: no cancellation of the q contacts with external-leg/LSZ or ghost/ST terms is claimed.")
    print("          No physical non-cancellation, full five-point STI, loop integration, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
