#!/usr/bin/env python3
"""RC-001 B2c-IVn-h/04: LD-W-03/04 actual same-vertex open-chain WTIs.

The two Dirac-Hermitian orientations are kept distinct. Each q-contracted
fermion insertion is multiplied by the graph-specific k-independent heavy
spectator and the scalar spectator, then contracted with V_S(k) and D(k).
This is not the complete four-attachment same-vertex Ward sum.
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


def contract_scalar_right(kernel, chain, current):
    out = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        out += (
            GAMMA_DOWN[mu] * chain
            * (ETA[nu] * current[nu]) * kernel[mu, nu]
        )
    return sp.simplify(out)


def contract_scalar_left(kernel, current, chain):
    out = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        out += (
            (ETA[mu] * current[mu]) * chain
            * GAMMA_DOWN[nu] * kernel[mu, nu]
        )
    return sp.simplify(out)


def verify_symbolic_same_vertex_wtis():
    q = list(sp.symbols("qWTI0:4", real=True))
    r_w = list(sp.symbols("rFW0:4", real=True))
    r_y = add(r_w, q)
    s_w = slash(r_w) / dot(r_w, r_w)
    s_y = slash(r_y) / dot(r_y, r_y)

    # LD-W-03: fermion WTI in the left-open orientation.
    lhs_03 = s_w * slash(q) * PL * s_y
    rhs_03 = s_w * PR - PL * s_y

    # LD-W-04: Dirac-Hermitian-conjugate open-line orientation.
    lhs_04 = s_y * slash(q) * PL * s_w
    rhs_04 = PL * s_w - s_y * PR

    assert matrix_zero(lhs_03 - rhs_03)
    assert matrix_zero(lhs_04 - rhs_04)
    return 32


def verify_heavy_spectator_independence():
    k = list(sp.symbols("kH0:4", real=True))
    p_f = list(sp.symbols("pF0:4", real=True))
    p_s = list(sp.symbols("pS0:4", real=True))
    q = list(sp.symbols("qH0:4", real=True))
    h_e = add(add(p_f, p_s), q)
    checks = 0
    for mu, nu in product(range(4), repeat=2):
        assert sp.diff(h_e[mu], k[nu]) == 0
        checks += 1
    return checks


def rational_open_chain_diagnostic(pair_id):
    # Exact point used by the previous same-vertex R_FG/current audit.
    k = [sp.Integer(3), sp.Integer(1), sp.Integer(1), sp.Integer(0)]
    q = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p1 = [sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(1)]
    p2 = [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(0)]
    p3 = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    p4 = [-q[i] - p1[i] - p2[i] - p3[i] for i in range(4)]
    kappa = add(k, q)

    if pair_id == "03":
        p_f, p_s = p1, p2
        h_e = add(add(p_f, p_s), q)
    elif pair_id == "04":
        p_f, p_s = p4, p3
        h_e = add(add(p_f, p_s), q)
    else:
        raise ValueError(pair_id)

    r_f_w = add(k, p_f)
    r_f_y = add(r_f_w, q)
    r_s_y = sub(p_s, k)
    r_s_w = sub(p_s, kappa)
    v_s = [2 * p_s[i] - k[i] for i in range(4)]
    m_e2 = sp.Integer(400)

    denominators = (
        dot(k, k), dot(kappa, kappa),
        dot(r_f_w, r_f_w), dot(r_f_y, r_f_y),
        dot(r_s_y, r_s_y), dot(r_s_w, r_s_w),
        dot(h_e, h_e) - m_e2,
    )
    assert all(value != 0 for value in denominators)

    s_f_w = slash(r_f_w) / dot(r_f_w, r_f_w)
    s_f_y = slash(r_f_y) / dot(r_f_y, r_f_y)
    heavy = slash(h_e) * PL / (dot(h_e, h_e) - m_e2)
    scalar_s = sp.Rational(1, dot(r_s_y, r_s_y))

    if pair_id == "03":
        chain_lhs = s_f_w * slash(q) * PL * s_f_y * heavy * scalar_s
        chain_rhs = (s_f_w * PR - PL * s_f_y) * heavy * scalar_s

        open_index_checks = 0
        for mu in range(4):
            assert matrix_zero(
                GAMMA_DOWN[mu] * chain_lhs - GAMMA_DOWN[mu] * chain_rhs
            )
            open_index_checks += 16

        open_lhs = contract_scalar_right(D_up(k), chain_lhs, v_s)
        open_rhs = contract_scalar_right(D_up(k), chain_rhs, v_s)
        endpoint_1 = contract_scalar_right(
            D_up(k), s_f_w * PR * heavy * scalar_s, v_s
        )
        endpoint_2 = contract_scalar_right(
            D_up(k), -PL * s_f_y * heavy * scalar_s, v_s
        )
    else:
        chain_lhs = heavy * s_f_y * slash(q) * PL * s_f_w * scalar_s
        chain_rhs = heavy * (PL * s_f_w - s_f_y * PR) * scalar_s

        open_index_checks = 0
        for nu in range(4):
            assert matrix_zero(
                chain_lhs * GAMMA_DOWN[nu] - chain_rhs * GAMMA_DOWN[nu]
            )
            open_index_checks += 16

        open_lhs = contract_scalar_left(D_up(k), v_s, chain_lhs)
        open_rhs = contract_scalar_left(D_up(k), v_s, chain_rhs)
        endpoint_1 = contract_scalar_left(
            D_up(k), v_s, heavy * PL * s_f_w * scalar_s
        )
        endpoint_2 = contract_scalar_left(
            D_up(k), v_s, -heavy * s_f_y * PR * scalar_s
        )

    assert matrix_zero(chain_lhs - chain_rhs)
    assert matrix_zero(open_lhs - open_rhs)
    assert matrix_zero(open_lhs - endpoint_1 - endpoint_2)
    nonzero_entries = sum(
        sp.simplify(open_lhs[i, j]) != 0
        for i, j in product(range(4), repeat=2)
    )
    assert nonzero_entries == 16

    return {
        "denominators": denominators,
        "open_index_checks": open_index_checks,
        "contracted_entries": nonzero_entries,
        "h_E": h_e,
    }


def main():
    wti = verify_symbolic_same_vertex_wtis()
    spectator = verify_heavy_spectator_independence()
    d03 = rational_open_chain_diagnostic("03")
    d04 = rational_open_chain_diagnostic("04")
    assert wti == 32 and spectator == 16
    assert d03["open_index_checks"] == d04["open_index_checks"] == 64
    assert d03["contracted_entries"] == d04["contracted_entries"] == 16

    print("RC-001 B2c-IVn-h/04: LD-W-03/04 same-vertex open-chain WTI bridge")
    print(f"PASS: two oriented symbolic fermion WTIs ({wti}/32 Dirac components).")
    print(f"PASS: k-independent heavy spectators ({spectator}/16 derivative checks).")
    print("PASS: LD-W-03 left-open chain (64/64 Lorentz-index matrix components; 16/16 contracted entries).")
    print("PASS: LD-W-04 right-open chain (64/64 Lorentz-index matrix components; 16/16 contracted entries).")
    print("PASS: both endpoint decompositions (exact matrix equalities).")
    print(f"LD-W-03 denominators: {d03['denominators']}; h_E={d03['h_E']}.")
    print(f"LD-W-04 denominators: {d04['denominators']}; h_E={d04['h_E']}.")
    print("RESULT: both same-vertex fermion WTIs hold in their actual ordered open chains.")
    print("BOUNDARY: the four-attachment same-vertex sum, scalar-line/seagull combination,")
    print("          and external-leg/LSZ/ghost-ST completion remain open.")
    print("          No loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
