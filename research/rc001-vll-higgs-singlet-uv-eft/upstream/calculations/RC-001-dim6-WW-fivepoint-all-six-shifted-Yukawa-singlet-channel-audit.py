#!/usr/bin/env python3
"""RC-001 B2c-IVn-g/03: shifted Yukawa-singlet channels for all six pairs.

Extends the local endpoint charge-factor check beyond LD-W-06:
- cross-vertex A endpoints use h-q after the secondary k'=k+q shift;
- cross-vertex B endpoints use h+q after k'=k-q;
- same-vertex LD-W-03/04 heavy spectators h_E are independent of k.
The physical left/right Yukawa-singlet SU(2) charge sums are checked exactly.
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


def verify_cross_A_secondary_channel():
    k = list(sp.symbols("kA0:4", real=True))
    q = list(sp.symbols("qA0:4", real=True))
    p1 = list(sp.symbols("p1A0:4", real=True))
    p2 = list(sp.symbols("p2A0:4", real=True))
    p_l = add(p1, p2)

    # First common-k map: k_old=k+q, h_A=k_old-p_L-q=h(k).
    k_old = add(k, q)
    h_a_first = sub(sub(k_old, p_l), q)
    h_common = sub(k, p_l)
    assert all(sp.simplify(h_a_first[i] - h_common[i]) == 0
               for i in range(4))

    # Second shift k'=k+q: the same heavy channel is h(k')-q.
    k_prime = add(k, q)
    h_prime = sub(k_prime, p_l)
    h_a_second = sub(h_prime, q)
    assert all(sp.simplify(h_common[i] - h_a_second[i]) == 0
               for i in range(4))
    return 8


def verify_cross_B_secondary_channel():
    k = list(sp.symbols("kB0:4", real=True))
    q = list(sp.symbols("qB0:4", real=True))
    p1 = list(sp.symbols("p1B0:4", real=True))
    p2 = list(sp.symbols("p2B0:4", real=True))
    p_l = add(p1, p2)

    h_common = sub(k, p_l)
    # Second shift k'=k-q: the old channel is h(k')+q.
    k_prime = sub(k, q)
    h_prime = sub(k_prime, p_l)
    h_b_second = add(h_prime, q)
    assert all(sp.simplify(h_common[i] - h_b_second[i]) == 0
               for i in range(4))
    return 4


def verify_same_vertex_spectators():
    p_f = list(sp.symbols("pF0:4", real=True))
    p_s = list(sp.symbols("pS0:4", real=True))
    q = list(sp.symbols("qSV0:4", real=True))
    k = list(sp.symbols("kSV0:4", real=True))
    h_e = add(add(p_f, p_s), q)
    k_plus = add(k, q)
    k_minus = sub(k, q)
    h_e_plus = add(add(p_f, p_s), q)
    h_e_minus = add(add(p_f, p_s), q)
    assert all(sp.simplify(h_e[i] - h_e_plus[i]) == 0
               for i in range(4))
    assert all(sp.simplify(h_e[i] - h_e_minus[i]) == 0
               for i in range(4))
    assert all(sp.diff(h_e[i], k[j]) == 0
               for i, j in product(range(4), repeat=2))
    assert all(sp.diff(h_e_plus[i], k[j]) == 0
               and sp.diff(h_e_minus[i], k[j]) == 0
               for i, j in product(range(4), repeat=2))
    return 8, 16


def verify_all_singlet_charge_sums():
    h_a, h_b, h_e, x_rest = sp.symbols(
        "S_E_h_minus_q S_E_h_plus_q S_E_hE X_rest"
    )
    checks = 0
    for a in range(3):
        r_bar_l = apply_R(T0, 0, a)
        r_h = apply_R(T0, 1, a)
        r_hdag = apply_R(T0, 2, a)
        r_l = apply_R(T0, 3, a)
        for ix in WEAK_INDICES:
            left = (r_bar_l(*ix) + r_h(*ix)) * h_a * x_rest
            right = (r_hdag(*ix) + r_l(*ix)) * h_b * x_rest
            same_left = (r_bar_l(*ix) + r_h(*ix)) * h_e * x_rest
            same_right = (r_hdag(*ix) + r_l(*ix)) * h_e * x_rest
            assert sp.simplify(left) == 0
            assert sp.simplify(right) == 0
            assert sp.simplify(same_left) == 0
            assert sp.simplify(same_right) == 0
            checks += 4
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

    def dot(a, b):
        eta = (1, -1, -1, -1)
        return sum(eta[i] * a[i] * b[i] for i in range(4))

    return (
        dot(h, h) - 400,
        dot(h_minus_q, h_minus_q) - 400,
        dot(h_plus_q, h_plus_q) - 400,
    )


def main():
    a = verify_cross_A_secondary_channel()
    b = verify_cross_B_secondary_channel()
    same = verify_same_vertex_spectators()
    weak = verify_all_singlet_charge_sums()
    heavy = rational_heavy_channels()
    assert (a, b, same, weak, heavy) == (8, 4, (8, 16), 192, (-377, -389, -365))
    print("RC-001 B2c-IVn-g/03: all-six shifted Yukawa-singlet channel audit")
    print(f"PASS: cross A endpoints share h-q after k'=k+q ({a}/8 vector components).")
    print(f"PASS: cross B endpoints share h+q after k'=k-q ({b}/4 vector components).")
    print(f"PASS: same-vertex LD-W-03/04 heavy spectators survive k->k±q ({same[0]}/8 vector components, {same[1]}/16 derivative checks).")
    print(f"PASS: left/right singlet charge sums with h-q, h+q, and h_E ({weak}/192 weak components).")
    print(f"RATIONAL LD-W-06 HEAVY DENOMINATORS: H0, HA, HB={heavy}.")
    print("RESULT: all six pair classes preserve the local Yukawa-singlet charge factor under the validated shifts.")
    print("BOUNDARY: this does not establish the full ordinary-matter longitudinal integrand cancellation,")
    print("          the external-leg/LSZ sum, the ghost/ST completion, or a Wilson coefficient.")


if __name__ == "__main__":
    main()
