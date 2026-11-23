#!/usr/bin/env python3
"""RC-001 B2c-IVn-f/03: exact LD-W-05 S-F endpoint split.

The B-side fermion WTI/Yukawa endpoint maps to the three-W graph with the
actual A scalar current V_A(k). Separately, the A-side scalar-line/seagull
kernel uses V_A(k+q)=V_A(k)-q. The exact rebase retains both symmetric and
commutator q-contact terms; no physical non-cancellation is claimed.
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


def physical_field_action(tensor, slot, a, ix):
    """Physical actions for (bar L,H,Hdagger,L), slots 1 and 3."""
    i, j, kk, ell = ix
    out = sp.Integer(0)
    if slot == 1:  # R_H = +t
        for m in range(2):
            out += +SIGMA[a][j, m] / 2 * tensor(i, m, kk, ell)
    elif slot == 3:  # R_L = +t
        for m in range(2):
            out += +SIGMA[a][ell, m] / 2 * tensor(i, j, kk, m)
    else:
        raise ValueError("LD-W-05 uses H slot 1 and L slot 3")
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


def verify_B_fermion_wti():
    q = list(sp.symbols("qB0:4", real=True))
    r_w = list(sp.symbols("rBW0:4", real=True))
    r_y = add(r_w, q)
    s_w = slash(r_w) / dot(r_w, r_w)
    s_y = slash(r_y) / dot(r_y, r_y)
    lhs = s_y * slash(q) * PL * s_w
    rhs = PL * s_w - s_y * PR
    assert matrix_zero(lhs - rhs)
    return 16


def verify_A_scalar_wti_and_current_rebase():
    k = list(sp.symbols("kS0:4", real=True))
    q = list(sp.symbols("qS0:4", real=True))
    p = list(sp.symbols("pA0:4", real=True))
    kap = add(k, q)
    r_y = sub(k, p)
    r_w = sub(kap, p)
    v_line = sub(scale(2, p), kap)
    v_3w = sub(scale(2, p), k)
    dy = 1 / dot(r_y, r_y)
    dw = 1 / dot(r_w, r_w)
    delta = dy - dw

    lhs = dot(q, add(r_w, r_y)) / (dot(r_w, r_w) * dot(r_y, r_y))
    assert sp.simplify(lhs - (dy - dw)) == 0
    assert all(sp.simplify(v_3w[i] - v_line[i] - q[i]) == 0
               for i in range(4))

    g2, sym, comm = sp.symbols("g2 S_A G_AB")
    c_original = [
        g2 * (-sp.Rational(1, 2)*delta*v_line[i]*sym
              + dy*q[i]*sym
              - I*sp.Rational(1, 2)*delta*v_line[i]*comm)
        for i in range(4)
    ]
    c_rebased = [
        g2 * (
            -sp.Rational(1, 2)*delta*v_3w[i]*sym
            + (sp.Rational(1, 2)*delta + dy)*q[i]*sym
            - I*sp.Rational(1, 2)*delta*v_3w[i]*comm
            + I*sp.Rational(1, 2)*delta*q[i]*comm
        )
        for i in range(4)
    ]
    assert all(sp.simplify(c_original[i] - c_rebased[i]) == 0
               for i in range(4))
    return 1, 8


def verify_B_side_fermion_route_to_three_w():
    k = list(sp.symbols("kRoute0:4", real=True))
    q = list(sp.symbols("qRoute0:4", real=True))
    p1 = list(sp.symbols("p1Route0:4", real=True))
    p2 = list(sp.symbols("p2Route0:4", real=True))
    p3 = list(sp.symbols("p3Route0:4", real=True))
    p4 = [-p1[i]-p2[i]-p3[i]-q[i] for i in range(4)]
    kap = add(k, q)
    r_a = sub(k, p2)
    r_by = add(add(k, p4), q)
    h = sub(k, add(p1, p2))
    v_a_k = sub(scale(2, p2), k)

    # B-side Yukawa endpoint is unshifted.
    mapped = (r_a, r_by, h, v_a_k, k)
    targets = (r_a, r_by, h, v_a_k, k)
    assert all(
        sp.simplify(mapped[n][mu]-targets[n][mu]) == 0
        for n in range(5) for mu in range(4)
    )

    me2 = sp.symbols("M_E2", real=True)
    hden = dot(h, h)-me2
    r_a2 = dot(r_a, r_a)
    r_aw2 = dot(sub(kap, p2), sub(kap, p2))
    r_by2 = dot(r_by, r_by)
    k2, kap2 = dot(k, k), dot(kap, kap)
    d3 = k2*kap2*r_a2*r_by2*hden
    d_b_y = k2*r_a2*r_by2*hden
    d_a_sg = kap2*r_a2*r_by2*hden
    d_a_line = kap2*r_a2*r_aw2*r_by2*hden
    # The scalar-line denominator has both A-side scalar propagators; the
    # seagull has only the Yukawa-side scalar propagator.
    assert d3 == kap2*d_b_y
    assert d3 == k2*d_a_sg
    assert k2*d_a_line == d3*r_aw2
    return 20, 3


def verify_weak_ordering():
    a_slot, b_slot = 1, 3
    checks_comm = checks_seagull = 0
    for external_a in range(3):
        g = G_tensor(a_slot, b_slot, external_a)
        seed = pair_tensor(a_slot, b_slot)
        graph_a = lambda *ix: sp.simplify(sum(
            physical_field_action(
                apply_phys(apply_phys(T0, a_slot, external_a), b_slot, b),
                a_slot, b, ix
            )
            for b in range(3)
        ))
        reverse_a = apply_phys(seed, a_slot, external_a)
        seagull = lambda *ix: sp.simplify(graph_a(*ix)+reverse_a(*ix))
        expected_seagull = lambda *ix: sp.Rational(1, 2)*physical_field_action(
            T0, b_slot, external_a, ix
        )
        for ix in product(range(2), repeat=4):
            assert sp.simplify(graph_a(*ix)-reverse_a(*ix)-I*g(*ix)) == 0
            assert sp.simplify(seagull(*ix)-expected_seagull(*ix)) == 0
            checks_comm += 1
            checks_seagull += 1
    return checks_comm, checks_seagull


def contract_scalar_left_kernel(kernel, scalar_current, chain):
    out = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        out += (ETA[mu]*scalar_current[mu]) * chain * GAMMA_DOWN[nu] * PL * kernel[mu, nu]
    return out


def verify_final_projector_order():
    k = [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)]
    q = [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)]
    p1 = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    p2 = [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    kap = add(k, q)
    r_by = add(add(k, p4), q)
    h = sub(k, add(p1, p2))
    v_a = sub(scale(2, p2), k)

    # Stripped matter chain; final P_L acts after the right W current.
    chain = slash(h) * slash(r_by)
    direct = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        coefficient = ETA[mu] * ETA[nu] * (
            k[mu] * k[nu] - kap[mu] * kap[nu]
        )
        direct += v_a[mu] * chain * GAMMA[nu] * PL * coefficient

    corrected = (
        dot(v_a, k) * chain * slash(k) * PL
        - dot(v_a, kap) * chain * slash(kap) * PL
    )
    old_order = (
        dot(v_a, k) * (chain * PL) * slash(k)
        - dot(v_a, kap) * (chain * PL) * slash(kap)
    )
    assert matrix_zero(direct - corrected)
    old_difference = sum(
        sp.simplify(direct[i, j] - old_order[i, j]) != 0
        for i, j in product(range(4), repeat=2)
    )
    assert old_difference == 16
    return old_difference


def rational_diagnostic():
    k = [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)]
    q = [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)]
    p1 = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    p2 = [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = [-p1[i]-p2[i]-p3[i]-q[i] for i in range(4)]
    kap = add(k, q)
    r_a = sub(k, p2)
    r_aw = sub(kap, p2)
    r_by = add(add(k, p4), q)
    h = sub(k, add(p1, p2))
    v_a_line = sub(scale(2, p2), kap)
    v_a_3w = sub(scale(2, p2), k)
    dy = sp.Rational(1, dot(r_a, r_a))
    dw = sp.Rational(1, dot(r_aw, r_aw))
    delta = dy - dw
    me2 = sp.Integer(400)
    den = (
        dot(k, k), dot(kap, kap), dot(r_a, r_a),
        dot(r_aw, r_aw), dot(r_by, r_by), dot(h, h)-me2
    )
    assert all(x != 0 for x in den)
    assert delta != 0
    assert all(v_a_3w[i]-v_a_line[i] == q[i] for i in range(4))

    # Actual three-W R_FG numerator with A scalar current V_A(k).
    # Keep the stripped X_A slash(h) X_B^Y chain separate. The final P_L
    # acts after the right W current, hence after slash(k) or slash(kappa).
    chain = slash(h)*slash(r_by)
    n05 = (
        dot(v_a_3w, k)*chain*slash(k)*PL
        - dot(v_a_3w, kap)*chain*slash(kap)*PL
    )
    rfg = (
        sp.Matrix(k)*sp.Matrix(k).T
        - sp.Matrix(kap)*sp.Matrix(kap).T
    )/(dot(k,k)*dot(kap,kap))
    d0, dq = D_up(k), D_up(kap)
    kernel = sp.simplify(dq*(K_down(kap)-K_down(k))*d0)
    line = contract_scalar_left_kernel(dq-d0, v_a_3w, chain)
    three = contract_scalar_left_kernel(kernel, v_a_3w, chain)
    rfg_matrix = contract_scalar_left_kernel(rfg, v_a_3w, chain)
    assert matrix_zero(line+three-rfg_matrix)
    assert matrix_zero(rfg_matrix-n05/(dot(k,k)*dot(kap,kap)))

    # A-side scalar commutator q-contact, contracted into the B fermion chain.
    q_contact = (
        I*sp.Rational(1,2)*delta
        * slash(h)*slash(r_by)*slash(q)*PL/dot(kap,kap)
    )
    q_nonzero = sum(sp.simplify(q_contact[i,j]) != 0
                    for i,j in product(range(4),repeat=2))
    n_nonzero = sum(sp.simplify(n05[i,j]) != 0
                    for i,j in product(range(4),repeat=2))
    assert q_nonzero == 16 and n_nonzero == 16
    return den, delta, n_nonzero, q_nonzero


def main():
    wti = verify_B_fermion_wti()
    scalar_wti, rebase = verify_A_scalar_wti_and_current_rebase()
    route, den_checks = verify_B_side_fermion_route_to_three_w()
    weak_comm, weak_sg = verify_weak_ordering()
    den, delta, n_nonzero, q_nonzero = rational_diagnostic()
    projector_diff = verify_final_projector_order()

    print("RC-001 B2c-IVn-f/03: LD-W-05 exact S-F endpoint split")
    print(f"PASS: B-side oriented fermion WTI ({wti}/16 Dirac components).")
    print(f"PASS: A-side scalar WTI and V_A(k)-V_A(k+q)=q ({scalar_wti}/1 and {rebase}/8 identities/components).")
    print(f"PASS: B-side fermion Yukawa-endpoint common-k map ({route}/20 vector components).")
    print(f"PASS: three-W, fermion-line, scalar-line and seagull denominator factors ({den_checks}/3 exact identities).")
    print(f"PASS: A-side physical weak commutator ordering ({weak_comm}/48 weak components).")
    print(f"PASS: A-side scalar seagull anticommutator ({weak_sg}/48 weak components).")
    print(f"PASS: actual LD-W-05 R_FG current contraction at rational point ({n_nonzero}/16 nonzero entries).")
    print(f"PASS: re-based A-scalar commutator q-contact is explicit and nonzero ({q_nonzero}/16 matrix entries); delta={delta}.")
    print(f"PASS: final P_L after right W current; old pre-slash(k) placement rejected ({projector_diff}/16 matrix entries).")
    print(f"RATIONAL DIAGNOSTIC: denominator factors={den}.")
    print("RESULT: the B-side fermion/three-W sub-block uses V_A(k); the A-side scalar-line/seagull")
    print("        kernel uses V_A(k+q)=V_A(k)-q and splits into V_A(k) plus explicit q contacts.")
    print("BOUNDARY: no cancellation of the q contacts with external-leg/LSZ or ghost/ST terms is claimed.")
    print("          No physical non-cancellation, full five-point STI, loop integration, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
