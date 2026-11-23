#!/usr/bin/env python3
"""RC-001 B2c-IVn-h/05: LD-W-05 projector/order reconciliation.

The B-oriented fermion WTI endpoint matrices are reduced with the physical
chiral projectors before comparing their open-chain order to the separately
defined R_FG chain. This checks projector placement, not an equality between
the one-W WTI endpoints and the two-W R_FG numerator.
"""
from itertools import product
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
GAMMA_DOWN = [ETA[mu] * GAMMA[mu] for mu in range(4)]


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def slash(a):
    return sum((ETA[i] * a[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def matrix_zero(m):
    return all(sp.simplify(m[i, j]) == 0
               for i, j in product(range(4), repeat=2))


def verify_chiral_intertwining():
    r = list(sp.symbols("r0:4", real=True))
    checks = 0
    for mu in range(4):
        assert matrix_zero(PL * GAMMA[mu] - GAMMA[mu] * PR)
        assert matrix_zero(PR * GAMMA[mu] - GAMMA[mu] * PL)
        checks += 2
    assert matrix_zero(PL * slash(r) - slash(r) * PR)
    assert matrix_zero(PR * slash(r) - slash(r) * PL)
    return checks + 2


def verify_B_endpoint_projector_order():
    k = [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)]
    q = [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)]
    p1 = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    p2 = [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    r_bw = [k[i] + p4[i] for i in range(4)]
    r_by = [r_bw[i] + q[i] for i in range(4)]
    h = [k[i] - p1[i] - p2[i] for i in range(4)]

    # Exact endpoint structures from the B-oriented WTI, retaining the
    # rightmost W vertex projector and the graph's actual Dirac order.
    endpoint_w = []
    endpoint_y = []
    reduced_w = []
    reduced_y = []
    for nu in range(4):
        endpoint_w.append(slash(h) * PL * slash(r_bw) * GAMMA_DOWN[nu] * PL)
        endpoint_y.append(-slash(h) * slash(r_by) * PR * GAMMA_DOWN[nu] * PL)
        reduced_w.append(slash(h) * slash(r_bw) * GAMMA_DOWN[nu] * PL)
        reduced_y.append(-slash(h) * slash(r_by) * GAMMA_DOWN[nu] * PL)

    assert all(matrix_zero(endpoint_w[nu] - reduced_w[nu]) for nu in range(4))
    assert all(matrix_zero(endpoint_y[nu] - reduced_y[nu]) for nu in range(4))
    return 128, r_bw, r_by, h


def verify_RFG_order_is_separate():
    k = [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)]
    q = [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)]
    kap = [k[i] + q[i] for i in range(4)]
    p1 = [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)]
    p2 = [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    r_bw = [k[i] + p4[i] for i in range(4)]
    r_by = [r_bw[i] + q[i] for i in range(4)]
    h = [k[i] - p1[i] - p2[i] for i in range(4)]
    v_a = [2*p2[i] - k[i] for i in range(4)]

    # The graph-specific two-W R_FG numerator has the order
    # V_A.k slash(h) slash(r_B^Y) slash(k)
    # - V_A.kappa slash(h) slash(r_B^Y) slash(kappa).
    rfg = (
        dot(v_a, k) * slash(h) * slash(r_by) * slash(k)
        - dot(v_a, kap) * slash(h) * slash(r_by) * slash(kap)
    )
    # Contracting the single W propagator with V_A places slash(V_A)
    # at the right end of each ordered B-fermion endpoint.
    endpoint_w = slash(h) * slash(r_bw) * slash(v_a) * PL
    endpoint_y = -slash(h) * slash(r_by) * slash(v_a) * PL
    rfg = rfg * PL  # retain the common rightmost chiral projector
    assert rfg != sp.zeros(4)
    assert endpoint_w != sp.zeros(4)
    assert endpoint_y != sp.zeros(4)
    assert endpoint_w != endpoint_y
    assert rfg != endpoint_w and rfg != endpoint_y
    nz = lambda m: sum(
        sp.simplify(m[i,j]) != 0 for i,j in product(range(4), repeat=2)
    )
    return nz(rfg), nz(endpoint_w), nz(endpoint_y), dot(v_a,k), dot(v_a,kap)


def main():
    chiral = verify_chiral_intertwining()
    endpoint = verify_B_endpoint_projector_order()
    rfg = verify_RFG_order_is_separate()
    assert chiral == 10
    assert endpoint[0] == 128
    assert rfg[0] == rfg[1] == rfg[2] == 16
    print("RC-001 B2c-IVn-h/05: LD-W-05 projector/order reconciliation")
    print(f"PASS: gamma/projector intertwining identities ({chiral}/10).")
    print(f"PASS: actual B-WTI endpoint projector reductions ({endpoint[0]}/128 matrix components).")
    print("PASS: both endpoints reduce to the same right-chiral Dirac orientation,")
    print("      with distinct r_B^W and r_B^Y momenta retained.")
    print(f"PASS: graph-specific R_FG numerator is nonzero ({rfg[0]}/16 entries).")
    print(f"PASS: both signed single-W endpoint numerators are distinct from R_FG ({rfg[1]}/16, {rfg[2]}/16 entries).")
    print(f"RATIONAL CURRENT DOTS: V_A.k={rfg[3]}, V_A.kappa={rfg[4]}.")
    print("RESULT: the P_L/P_R placement in the B-oriented WTI is reconciled exactly.")
    print("BOUNDARY: this is not an equality of the single-W WTI endpoints and R_FG.")
    print("          Their cancellation must be established only in the complete longitudinal")
    print("          matter + scalar + three-W + LSZ/ST sum.")
    print("          No loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
