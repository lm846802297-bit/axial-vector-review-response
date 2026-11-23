#!/usr/bin/env python3
"""RC-001 B2c-IVn-f/01: graph-specific LD-W-01 common-k bridge.

This is an exact off-shell audit of the F-F cross-vertex pair. It combines:
- the oriented A/B fermion WTIs;
- the actual common-k shifts and complete spectator denominators;
- the physical SU(2) A/B commutator tensors and relative phases;
- the three-W contraction sandwiched between Feynman-gauge propagators;
- the explicit LD-W-01 Dirac chain and its nonzero R_FG projection.

It is not the full 24-graph STI, and it does not remove R_FG.
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
    """Physical actions for (bar L,H,Hdagger,L), with slots 0 and 3 used."""
    i, j, kk, ell = ix
    out = sp.Integer(0)
    if slot == 0:  # R_barL = -t^T
        for m in range(2):
            out += -SIGMA[a][m, i] / 2 * tensor(m, j, kk, ell)
    elif slot == 3:  # R_L = +t
        for m in range(2):
            out += +SIGMA[a][ell, m] / 2 * tensor(i, j, kk, m)
    else:
        raise ValueError("LD-W-01 uses only bar-L slot 0 and L slot 3")
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


def verify_wti():
    q = list(sp.symbols("qWTI0:4", real=True))
    r_aw = list(sp.symbols("rAW0:4", real=True))
    r_ay = sub(r_aw, q)
    s_aw = -slash(r_aw) / dot(r_aw, r_aw)
    s_ay = -slash(r_ay) / dot(r_ay, r_ay)
    lhs_a = s_aw * slash(q) * PL * s_ay
    rhs_a = s_aw * PR - PL * s_ay

    r_bw = list(sp.symbols("rBW0:4", real=True))
    r_by = add(r_bw, q)
    s_bw = slash(r_bw) / dot(r_bw, r_bw)
    s_by = slash(r_by) / dot(r_by, r_by)
    lhs_b = s_by * slash(q) * PL * s_bw
    rhs_b = PL * s_bw - s_by * PR

    assert matrix_zero(lhs_a - rhs_a)
    assert matrix_zero(lhs_b - rhs_b)
    return 32


def verify_common_routing_and_denominators():
    k = list(sp.symbols("kRoute0:4", real=True))
    q = list(sp.symbols("qRoute0:4", real=True))
    p1 = list(sp.symbols("p1Route0:4", real=True))
    p2 = list(sp.symbols("p2Route0:4", real=True))
    p3 = list(sp.symbols("p3Route0:4", real=True))
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    kap = add(k, q)

    r_a = sub(k, p1)
    r_ay = sub(r_a, q)
    r_bw = add(k, p4)
    r_by = add(r_bw, q)
    h = sub(k, add(p1, p2))

    # A-side Yukawa-endpoint term: old loop variable = k+q.
    a_maps = (
        sub(add(k, q), add(p1, q)),  # r_A^Y(k_old) -> r_A
        add(add(k, q), p4),          # r_B^W(k_old) -> r_B^Y
        sub(sub(add(k, q), add(p1, p2)), q),  # h_A(k_old) -> h
        kap,                         # W momentum k_old -> k+q
    )
    a_targets = (r_a, r_by, h, kap)
    assert all(
        sp.simplify(a_maps[n][mu] - a_targets[n][mu]) == 0
        for n in range(4) for mu in range(4)
    )

    # B-side Yukawa-endpoint term: no loop shift.
    b_maps = (r_a, r_by, h, k)
    b_targets = (r_a, r_by, h, k)
    assert all(
        sp.simplify(b_maps[n][mu] - b_targets[n][mu]) == 0
        for n in range(4) for mu in range(4)
    )

    me2 = sp.symbols("M_E2", real=True)
    spectator = dot(r_a, r_a) * dot(r_by, r_by) * (dot(h, h) - me2)
    d_3w = dot(k, k) * dot(kap, kap) * spectator
    d_a_yukawa = dot(kap, kap) * spectator
    d_b_yukawa = dot(k, k) * spectator
    assert sp.simplify(d_3w / dot(k, k) - d_a_yukawa) == 0
    assert sp.simplify(d_3w / dot(kap, kap) - d_b_yukawa) == 0
    return 32, 2


def contract_kernel(kernel, chain):
    out = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        out += GAMMA_DOWN[mu] * chain * GAMMA_DOWN[nu] * PL * kernel[mu, nu]
    return out


def verify_three_w_vertex_and_kernel():
    k = list(sp.symbols("k0:4", real=True))
    q = list(sp.symbols("q0:4", real=True))
    kap = add(k, q)
    checks = 0
    for mu, nu in product(range(4), repeat=2):
        lhs = sp.expand(sum(
            q[alpha] * gamma3(alpha, mu, nu, q, k)
            for alpha in range(4)
        ))
        rhs = K_down(kap)[mu, nu] - K_down(k)[mu, nu]
        assert sp.simplify(lhs - rhs) == 0
        checks += 1

    d0, dq = D_up(k), D_up(kap)
    rfg = (
        sp.Matrix(k) * sp.Matrix(k).T
        - sp.Matrix(kap) * sp.Matrix(kap).T
    ) / (dot(k, k) * dot(kap, kap))
    three_w_kernel = sp.simplify(dq * (K_down(kap) - K_down(k)) * d0)
    assert matrix_zero(three_w_kernel - (d0 - dq + rfg))
    return checks, 16


def verify_weak_phase():
    a_slot, b_slot = 0, 3  # bar L and L
    checks_a = checks_b = 0
    g2 = sp.symbols("g_2")
    for external_a in range(3):
        g = G_tensor(a_slot, b_slot, external_a)
        graph_a = lambda *ix: sp.simplify(sum(
            physical_field_action(
                apply_phys(apply_phys(T0, a_slot, external_a), b_slot, b),
                a_slot, b, ix
            )
            for b in range(3)
        ))
        reverse_a = apply_phys(pair_tensor(a_slot, b_slot), a_slot, external_a)
        graph_b = apply_phys(pair_tensor(a_slot, b_slot), b_slot, external_a)
        reverse_b = lambda *ix: sp.simplify(sum(
            physical_field_action(
                apply_phys(apply_phys(T0, b_slot, external_a), a_slot, b),
                b_slot, b, ix
            )
            for b in range(3)
        ))
        for ix in product(range(2), repeat=4):
            assert sp.simplify(graph_a(*ix) - reverse_a(*ix) - I*g(*ix)) == 0
            assert sp.simplify(graph_b(*ix) - reverse_b(*ix) - I*g(*ix)) == 0
            assert sp.simplify(-g2*(graph_a(*ix)-reverse_a(*ix)) + I*g2*g(*ix)) == 0
            assert sp.simplify(-g2*(graph_b(*ix)-reverse_b(*ix)) + I*g2*g(*ix)) == 0
            checks_a += 1
            checks_b += 1
    return checks_a, checks_b


def verify_final_projector_order():
    k = [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)]
    q = [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)]
    p1 = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    p2 = [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    kap = add(k, q)
    r_a = sub(k, p1)
    r_by = add(add(k, p4), q)
    h = sub(k, add(p1, p2))

    # Stripped matter chain; final P_L acts after the right W current.
    chain = -slash(r_a) * slash(h) * slash(r_by)
    direct = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        coefficient = ETA[mu] * ETA[nu] * (
            k[mu] * k[nu] - kap[mu] * kap[nu]
        )
        direct += GAMMA[mu] * chain * GAMMA[nu] * PL * coefficient

    corrected = (
        slash(k) * chain * slash(k) * PL
        - slash(kap) * chain * slash(kap) * PL
    )
    old_order = (
        slash(k) * (chain * PL) * slash(k)
        - slash(kap) * (chain * PL) * slash(kap)
    )
    assert matrix_zero(direct - corrected)
    old_difference = sum(
        sp.simplify(direct[i, j] - old_order[i, j]) != 0
        for i, j in product(range(4), repeat=2)
    )
    assert old_difference == 16
    return old_difference


def rational_diagnostic():
    k = [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)]
    q = [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)]
    p1 = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    p2 = [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    kap = add(k, q)
    r_a = sub(k, p1)
    r_by = add(add(k, p4), q)
    h = sub(k, add(p1, p2))
    # The final chiral projector belongs after the right W current, not
    # between X_B^Y and the last W-momentum slash.
    chain = -slash(r_a) * slash(h) * slash(r_by)
    n01 = (
        slash(k) * chain * slash(k) * PL
        - slash(kap) * chain * slash(kap) * PL
    )
    me2 = sp.Integer(400)
    den = (
        dot(k, k), dot(kap, kap), dot(r_a, r_a),
        dot(r_by, r_by), dot(h, h) - me2
    )
    assert all(x != 0 for x in den)

    d0, dq = D_up(k), D_up(kap)
    rfg = (
        sp.Matrix(k) * sp.Matrix(k).T
        - sp.Matrix(kap) * sp.Matrix(kap).T
    ) / (dot(k, k) * dot(kap, kap))
    three_w_kernel = sp.simplify(dq * (K_down(kap) - K_down(k)) * d0)
    line_commutator = contract_kernel(dq - d0, chain)
    three_w = contract_kernel(three_w_kernel, chain)
    rfg_actual = contract_kernel(rfg, chain)
    assert matrix_zero(line_commutator + three_w - rfg_actual)
    assert matrix_zero(rfg_actual - n01 / (dot(k, k) * dot(kap, kap)))

    nonzero = sum(sp.simplify(n01[i, j]) != 0
                  for i, j in product(range(4), repeat=2))
    assert nonzero == 16
    return den, nonzero, 32


def main():
    wti = verify_wti()
    route_components, denominator_checks = verify_common_routing_and_denominators()
    vertex_checks, kernel_checks = verify_three_w_vertex_and_kernel()
    weak_a, weak_b = verify_weak_phase()
    den, nonzero, chain_checks = rational_diagnostic()
    projector_diff = verify_final_projector_order()

    print("RC-001 B2c-IVn-f/01: LD-W-01 exact common-k F-F bridge")
    print(f"PASS: oriented A/B fermion WTIs ({wti}/32 Dirac components).")
    print(f"PASS: A-shift and B-unshift common-k maps ({route_components}/32 vector components).")
    print(f"PASS: three-W denominator equals the two single-W endpoint denominators ({denominator_checks}/2 exact identities).")
    print(f"PASS: q.Gamma_3W = K(k+q)-K(k) ({vertex_checks}/16 Lorentz components).")
    print(f"PASS: Feynman-gauge propagator-chain decomposition ({kernel_checks}/16 tensor components).")
    print(f"PASS: actual LD-W-01 Dirac-chain cancellation to R_FG at an exact rational point ({chain_checks}/32 matrix components).")
    print(f"PASS: physical A/B weak commutator and phase alignment ({weak_a}/48 and {weak_b}/48 weak components).")
    print(f"PASS: final P_L after right W current; old pre-slash(k) placement rejected ({projector_diff}/16 matrix entries).")
    print(f"RATIONAL DIAGNOSTIC: denominator factors={den}; nonzero N_01 entries={nonzero}/16.")
    print("RESULT: the LD-W-01 F-F commutator/three-W sub-block is exactly reduced to the explicit R_FG projection.")
    print("BOUNDARY: this does not include the Yukawa-endpoint gauge variations, external-leg/LSZ,")
    print("          gauge-fixing/ghost STI, counterterms, other five-point pairs, loop integration,")
    print("          UV-EFT subtraction, or a Wilson coefficient. R_FG is retained, not set to zero.")


if __name__ == "__main__":
    main()
