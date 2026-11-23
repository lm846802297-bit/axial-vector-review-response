#!/usr/bin/env python3
"""RC-001 B2c-IVn-d: exact longitudinal inverse-kernel completion of R_FG.

Shows that the Feynman-gauge remainder left by the transverse Yang-Mills
kernel is exactly minus the propagator-sandwiched longitudinal p_mu p_nu
difference. Adding that longitudinal piece converts the transverse kernel
to the full Feynman-gauge inverse kernel and removes R_FG algebraically.
This identifies the tensor required by the complete gauge-fixed/ST analysis;
it is not itself a ghost-diagram calculation.
"""
import sympy as sp

ETA = (1, -1, -1, -1)
METRIC = sp.diag(*ETA)


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def matrix_zero(matrix):
    return all(sp.simplify(matrix[i, j]) == 0
               for i in range(matrix.rows) for j in range(matrix.cols))


def build(k, q):
    kap = [sp.expand(k[i] + q[i]) for i in range(4)]
    k_cov = sp.Matrix([ETA[i] * k[i] for i in range(4)])
    kap_cov = sp.Matrix([ETA[i] * kap[i] for i in range(4)])
    k2, kap2 = dot(k, k), dot(kap, kap)

    K_k = k2 * METRIC - k_cov * k_cov.T
    K_kap = kap2 * METRIC - kap_cov * kap_cov.T
    L_k = k_cov * k_cov.T
    L_kap = kap_cov * kap_cov.T
    D_k = METRIC / k2
    D_kap = METRIC / kap2
    R_fg = (
        sp.Matrix(k) * sp.Matrix(k).T
        - sp.Matrix(kap) * sp.Matrix(kap).T
    ) / (k2 * kap2)
    return kap, K_k, K_kap, L_k, L_kap, D_k, D_kap, R_fg


def verify_transverse_kernel_remainder():
    k = list(sp.symbols("k0:4", real=True))
    q = list(sp.symbols("q0:4", real=True))
    _, K_k, K_kap, _, _, D_k, D_kap, R_fg = build(k, q)
    lhs = D_kap * (K_kap - K_k) * D_k
    rhs = D_k - D_kap + R_fg
    assert matrix_zero(lhs - rhs)
    return 16


def verify_longitudinal_piece_cancels_rfg():
    k = list(sp.symbols("kL0:4", real=True))
    q = list(sp.symbols("qL0:4", real=True))
    _, _, _, L_k, L_kap, D_k, D_kap, R_fg = build(k, q)
    lhs = D_kap * (L_kap - L_k) * D_k
    assert matrix_zero(lhs + R_fg)
    return 16


def verify_full_feynman_gauge_inverse_kernel():
    k = list(sp.symbols("kF0:4", real=True))
    q = list(sp.symbols("qF0:4", real=True))
    kap, K_k, K_kap, L_k, L_kap, D_k, D_kap, _ = build(k, q)
    full_k = sp.simplify(K_k + L_k)
    full_kap = sp.simplify(K_kap + L_kap)
    k2, kap2 = dot(k, k), dot(kap, kap)
    assert matrix_zero(full_k - k2 * METRIC)
    assert matrix_zero(full_kap - kap2 * METRIC)
    lhs = D_kap * (full_kap - full_k) * D_k
    rhs = D_k - D_kap
    assert matrix_zero(lhs - rhs)
    return 32


def main():
    transverse = verify_transverse_kernel_remainder()
    longitudinal = verify_longitudinal_piece_cancels_rfg()
    full = verify_full_feynman_gauge_inverse_kernel()
    print("RC-001 B2c-IVn-d longitudinal inverse-kernel completion")
    print(f"PASS: transverse Yang-Mills kernel leaves D(k)-D(k+q)+R_FG ({transverse}/16 components).")
    print(f"PASS: longitudinal p_mu p_nu difference contributes exactly -R_FG ({longitudinal}/16 components).")
    print(f"PASS: K_mu_nu+p_mu p_nu=p^2 g_mu_nu and full Feynman-gauge chain closes ({full}/32 components).")
    print("RESULT: the exact tensor needed to remove R_FG is the longitudinal inverse-kernel difference.")
    print("BOUNDARY: this is an inverse-kernel algebra identity, not a ghost/ST diagram calculation.")
    print("          The BRST/ghost realization and its coupling to the actual matter currents remain open.")


if __name__ == "__main__":
    main()
