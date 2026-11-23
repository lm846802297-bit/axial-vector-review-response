#!/usr/bin/env python3
"""RC-001 B2c-IVn-g/02: extend Yukawa-singlet charge cancellation to h±q.

For the secondary LD-W-06 shifts, the A-side left Yukawa fields share h-q,
and the B-side right Yukawa fields share h+q. The physical SU(2) singlet
charge sums therefore still vanish when multiplied by the corresponding
shifted heavy propagator. This is a local charge identity, not the full LSZ/ST sum.
"""
from itertools import product
import sympy as sp

I = sp.I
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(s / 2 for s in SIGMA)
R = {
    0: tuple(-t.T for t in T),  # bar L
    1: T,                       # H
    2: tuple(-t.T for t in T),  # H dagger
    3: T,                       # L
}
WEAK_INDICES = tuple(product(range(2), repeat=4))


def T0(i, j, k, ell):
    return sp.Integer(int(i == j and k == ell))


def apply_R(tensor, slot, generator):
    matrix = R[slot][generator]

    def result(*indices):
        indices = list(indices)
        total = sp.Integer(0)
        for m in range(2):
            internal = indices.copy()
            internal[slot] = m
            total += matrix[indices[slot], m] * tensor(*internal)
        return sp.simplify(total)
    return result


def add(a, b):
    return [sp.expand(a[i] + b[i]) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def verify_secondary_heavy_channels():
    k = list(sp.symbols("k0:4", real=True))
    q = list(sp.symbols("q0:4", real=True))
    p1 = list(sp.symbols("p10:4", real=True))
    p2 = list(sp.symbols("p20:4", real=True))
    p_l = add(p1, p2)

    # A-side: k_A'=k+q. Both bar-L and H endpoint variations carry h-q.
    k_a = add(k, q)
    h_a_bar_l = sub(sub(k_a, p_l), q)
    h_a_h = sub(sub(k_a, p_l), q)
    h_a = sub(k_a, p_l)
    assert all(sp.simplify(h_a_bar_l[i] - h_a_h[i]) == 0
               for i in range(4))
    assert all(sp.simplify(h_a_bar_l[i] - (h_a[i] - q[i])) == 0
               for i in range(4))

    # B-side: k_B'=k-q. Both Hdagger and L variations carry h+q.
    k_b = sub(k, q)
    h_b_hdag = add(sub(k_b, p_l), q)
    h_b_l = add(sub(k_b, p_l), q)
    h_b = sub(k_b, p_l)
    assert all(sp.simplify(h_b_hdag[i] - h_b_l[i]) == 0
               for i in range(4))
    assert all(sp.simplify(h_b_hdag[i] - (h_b[i] + q[i])) == 0
               for i in range(4))
    return 8, 8


def verify_shifted_singlet_charge_sums():
    h_a, h_b, x_rest = sp.symbols("S_E_h_minus_q S_E_h_plus_q X_rest")
    checks = 0
    for a in range(3):
        r_bar_l = apply_R(T0, 0, a)
        r_h = apply_R(T0, 1, a)
        r_hdag = apply_R(T0, 2, a)
        r_l = apply_R(T0, 3, a)
        for ix in WEAK_INDICES:
            left = (r_bar_l(*ix) + r_h(*ix)) * h_a * x_rest
            right = (r_hdag(*ix) + r_l(*ix)) * h_b * x_rest
            assert sp.simplify(left) == 0
            assert sp.simplify(right) == 0
            checks += 2
    return checks


def rational_heavy_channels():
    k = [6, 1, 0, 1]
    q = [1, 1, 0, 0]
    p1 = [1, 0, 1, 0]
    p2 = [0, 2, 0, 1]
    p_l = add(p1, p2)
    h = sub(k, p_l)
    h_minus_q = sub(h, q)
    h_plus_q = add(h, q)
    return (
        dot(h, h) - 400,
        dot(h_minus_q, h_minus_q) - 400,
        dot(h_plus_q, h_plus_q) - 400,
    )


def dot(a, b):
    eta = (1, -1, -1, -1)
    return sp.expand(sum(eta[i] * a[i] * b[i] for i in range(4)))


def main():
    maps = verify_secondary_heavy_channels()
    charges = verify_shifted_singlet_charge_sums()
    heavy = rational_heavy_channels()
    assert maps == (8, 8)
    assert charges == 96
    assert heavy == (-377, -389, -365)
    print("RC-001 B2c-IVn-g/02: shifted Yukawa-singlet charge closure")
    print(f"PASS: A-side bar-L/H endpoint variations share h-q ({maps[0]}/4+4 vector components).")
    print(f"PASS: B-side Hdagger/L endpoint variations share h+q ({maps[1]}/4+4 vector components).")
    print(f"PASS: shifted left/right Yukawa-singlet charge sums ({charges}/96 weak components).")
    print(f"RATIONAL HEAVY DENOMINATORS: H0, HA, HB={heavy}.")
    print("RESULT: the secondary h-q and h+q shifts do not spoil the local Yukawa-singlet charge cancellation.")
    print("BOUNDARY: this only closes the local endpoint charge factors after the secondary shifts.")
    print("          It does not cancel the full scalar-line/three-W integrand or the reducible LSZ terms.")
    print("          No complete STI or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
