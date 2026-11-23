#!/usr/bin/env python3
"""RC-001 B2c-IVn-a: same-vertex fermion-line WTI for LD-W-03/04.

Derives the q-contracted external-W insertion from the actual N03/N04
Dirac-Hermitian seed orientations. The two orientations are kept distinct.
No loop integration or full STI completion is claimed.
"""
import sympy as sp

I = sp.I
ETA = (1, -1, -1, -1)
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


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def slash(p):
    return sum((ETA[i] * p[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def matrix_zero(matrix):
    return all(sp.simplify(matrix[i, j]) == 0
               for i in range(matrix.rows) for j in range(matrix.cols))


def dirac_bar(matrix):
    return GAMMA[0] * matrix.conjugate().T * GAMMA[0]


def verify_same_vertex_fermion_wti():
    q = list(sp.symbols("qSV0:4", real=True))
    r_w = list(sp.symbols("rSVW0:4", real=True))
    r_y = [r_w[i] + q[i] for i in range(4)]
    s_w = slash(r_w) / dot(r_w, r_w)
    s_y = slash(r_y) / dot(r_y, r_y)
    sq = slash(q)

    # LD-W-03: internal-W gamma_mu, then the fermion propagator,
    # then the external-W insertion and the Yukawa-side propagator.
    lhs03 = s_w * sq * PL * s_y
    rhs03 = s_w * PR - PL * s_y
    assert matrix_zero(lhs03 - rhs03)

    # LD-W-04: the Dirac-Hermitian-conjugate orientation.
    lhs04 = s_y * sq * PL * s_w
    rhs04 = PL * s_w - s_y * PR
    assert matrix_zero(lhs04 - rhs04)
    return 32


def verify_full_open_chain_conjugation():
    q = list(sp.symbols("qHC0:4", real=True))
    r_w = list(sp.symbols("rHCW0:4", real=True))
    r_y = [r_w[i] + q[i] for i in range(4)]
    v_s = list(sp.symbols("vHC0:4", real=True))
    sq = slash(q)

    n03 = sum((
        GAMMA[mu] * slash(r_w) * sq * PL * slash(r_y) * v_s[mu]
        for mu in range(4)
    ), sp.zeros(4))
    n04 = sum((
        v_s[mu] * slash(r_y) * sq * PL * slash(r_w) * GAMMA[mu]
        for mu in range(4)
    ), sp.zeros(4))
    assert matrix_zero(dirac_bar(n03) - n04)

    seed03 = sum((
        GAMMA[mu] * slash(r_w) * v_s[mu] for mu in range(4)
    ), sp.zeros(4))
    seed04 = sum((
        v_s[mu] * slash(r_w) * GAMMA[mu] for mu in range(4)
    ), sp.zeros(4))
    assert matrix_zero(dirac_bar(seed03) - seed04)
    return 32


def verify_common_k_momentum_and_spectator():
    p_f = list(sp.symbols("pF0:4", real=True))
    p_s = list(sp.symbols("pS0:4", real=True))
    k = list(sp.symbols("k0:4", real=True))
    q = list(sp.symbols("q0:4", real=True))
    r_f_w = [k[i] + p_f[i] for i in range(4)]
    r_f_y = [k[i] + p_f[i] + q[i] for i in range(4)]
    h_e = [p_f[i] + p_s[i] + q[i] for i in range(4)]
    assert all(sp.simplify(r_f_y[i] - r_f_w[i] - q[i]) == 0
               for i in range(4))
    assert all(sp.diff(h_e[i], k[j]) == 0
               for i in range(4) for j in range(4))
    return 4, 16


def main():
    wti = verify_same_vertex_fermion_wti()
    conjugation = verify_full_open_chain_conjugation()
    route, spectator = verify_common_k_momentum_and_spectator()
    print("RC-001 B2c-IVn-a same-vertex fermion-line WTI")
    print(f"PASS: LD-W-03/04 opposite open-line WTI identities ({wti}/32 Dirac components).")
    print(f"PASS: q-contracted insertion and seed Dirac-Hermitian conjugation ({conjugation}/32 components).")
    print(f"PASS: common-k fermion momenta r_F^Y=r_F^W+q ({route}/4 vector components).")
    print(f"PASS: same-vertex heavy channel is k-independent spectator ({spectator}/16 derivatives).")
    print("LD-W-03:")
    print("  S(r_F^W) slash(q) P_L S(r_F^Y) = S(r_F^W) P_R - P_L S(r_F^Y)")
    print("LD-W-04:")
    print("  S(r_F^Y) slash(q) P_L S(r_F^W) = P_L S(r_F^W) - S(r_F^Y) P_R")
    print("BOUNDARY: same-vertex fermion-line WTI only; no full 24-graph sum,")
    print("          ghost/ST completion, loop integration, or Wilson coefficient.")


if __name__ == "__main__":
    main()
