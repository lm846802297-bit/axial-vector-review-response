#!/usr/bin/env python3
"""RC-001 B2c-IVj: explicit common-k shift maps for all six WW pair classes.

The audit compares the Yukawa-endpoint terms from the oriented matter-line
WTIs and the scalar seagull routings with the two three-W reference momenta.
It checks every adjacent matter momentum, the heavy-channel momentum, and
the internal-W momentum. It is a routing identity, not an amplitude
cancellation or loop integration.
"""
import sympy as sp

p1 = list(sp.symbols("p1_0:4", real=True))
p2 = list(sp.symbols("p2_0:4", real=True))
p3 = list(sp.symbols("p3_0:4", real=True))
q = list(sp.symbols("q_0:4", real=True))
k = list(sp.symbols("k_0:4", real=True))
# Five-point all-incoming conservation.
p4 = [-q[i] - p1[i] - p2[i] - p3[i] for i in range(4)]
P_L = [p1[i] + p2[i] for i in range(4)]


def add(*vectors):
    return [sp.expand(sum(v[i] for v in vectors)) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def shift_q(vector):
    return add(vector, q)


def same_vector(a, b):
    return all(sp.simplify(a[i] - b[i]) == 0 for i in range(4))


def check_map(label, pairs):
    for actual, expected in pairs:
        assert same_vector(actual, expected), label
    return len(pairs)


CROSS = (
    # pair, A type, B type, p_A, p_B, p_A', p_B'
    ("LD-W-01", "F", "F", p1, p4, p2, p3),
    ("LD-W-02", "F", "S", p1, p3, p2, p4),
    ("LD-W-05", "S", "F", p2, p4, p1, p3),
    ("LD-W-06", "S", "S", p2, p3, p1, p4),
)
SAME = (
    ("LD-W-03", p1, p2),
    ("LD-W-04", p4, p3),
)


def verify_cross_vertex_maps():
    endpoint_maps = 0
    endpoint_vectors = 0
    seagull_maps = 0
    seagull_vectors = 0

    for pair_id, type_a, type_b, p_a, p_b, _, _ in CROSS:
        # Three-W reference routing: k at A, k+q at B.
        r_a_3w = sub(k, p_a)
        r_b_3w = add(k, p_b, q)
        h_3w = sub(k, P_L)
        k_a_3w = k
        k_b_3w = shift_q(k)

        # A-line Yukawa endpoint. Shift its old loop variable k_old -> k+q.
        k_old = shift_q(k)
        check_map(
            f"{pair_id} A-Yukawa endpoint",
            (
                (sub(sub(k_old, p_a), q), r_a_3w),
                (add(k_old, p_b), r_b_3w),
                (sub(sub(k_old, P_L), q), h_3w),
                (k_old, k_b_3w),
            ),
        )
        endpoint_maps += 1
        endpoint_vectors += 4

        # B-line Yukawa endpoint is already in the common k routing.
        check_map(
            f"{pair_id} B-Yukawa endpoint",
            (
                (sub(k, p_a), r_a_3w),
                (add(k, p_b, q), r_b_3w),
                (sub(k, P_L), h_3w),
                (k, k_a_3w),
            ),
        )
        endpoint_maps += 1
        endpoint_vectors += 4

        # A scalar seagull, when present, uses the A-side shift k_old -> k+q.
        if type_a == "S":
            check_map(
                f"{pair_id} A scalar seagull",
                (
                    (sub(sub(k_old, p_a), q), r_a_3w),
                    (sub(sub(k_old, P_L), q), h_3w),
                    (k_old, k_b_3w),
                ),
            )
            seagull_maps += 1
            seagull_vectors += 3

        # B scalar seagull, when present, is in the unshifted k routing.
        if type_b == "S":
            check_map(
                f"{pair_id} B scalar seagull",
                (
                    (add(k, p_b, q), r_b_3w),
                    (sub(k, P_L), h_3w),
                    (k, k_a_3w),
                ),
            )
            seagull_maps += 1
            seagull_vectors += 3

    return endpoint_maps, endpoint_vectors, seagull_maps, seagull_vectors


def verify_same_vertex_maps():
    endpoint_maps = 0
    endpoint_vectors = 0
    seagull_maps = 0
    seagull_vectors = 0

    for pair_id, p_f, p_s in SAME:
        # Three-W reference routing: k at S, k+q at F.
        r_f_3w = add(k, p_f, q)
        r_s_3w = sub(p_s, k)
        h_3w = add(p_f, p_s, q)
        k_s_3w = k
        k_f_3w = shift_q(k)

        # F-line Yukawa endpoint is unshifted.
        check_map(
            f"{pair_id} F-Yukawa endpoint",
            (
                (add(k, p_f, q), r_f_3w),
                (sub(p_s, k), r_s_3w),
                (add(p_f, p_s, q), h_3w),
                (k, k_s_3w),
            ),
        )
        endpoint_maps += 1
        endpoint_vectors += 4

        # S-line Yukawa endpoint: shift its old loop variable k_old -> k+q.
        k_old = shift_q(k)
        check_map(
            f"{pair_id} S-Yukawa endpoint",
            (
                (add(sub(p_s, k_old), q), r_s_3w),
                (add(k_old, p_f), r_f_3w),
                (add(p_f, p_s, q), h_3w),
                (k_old, k_f_3w),
            ),
        )
        endpoint_maps += 1
        endpoint_vectors += 4

        # The S-endpoint seagull uses the same shift as the S-line endpoint.
        check_map(
            f"{pair_id} S scalar seagull",
            (
                (add(sub(p_s, k_old), q), r_s_3w),
                (add(p_f, p_s, q), h_3w),
                (k_old, k_f_3w),
            ),
        )
        seagull_maps += 1
        seagull_vectors += 3

    return endpoint_maps, endpoint_vectors, seagull_maps, seagull_vectors


def main():
    cross = verify_cross_vertex_maps()
    same = verify_same_vertex_maps()
    endpoint_maps = cross[0] + same[0]
    endpoint_vectors = cross[1] + same[1]
    seagull_maps = cross[2] + same[2]
    seagull_vectors = cross[3] + same[3]

    assert cross == (8, 32, 4, 12)
    assert same == (4, 16, 2, 6)
    assert (endpoint_maps, endpoint_vectors) == (12, 48, )
    assert (seagull_maps, seagull_vectors) == (6, 18)

    print("RC-001 B2c-IVj explicit common-k shift-map audit")
    print("PASS: cross-vertex Yukawa-endpoint maps (8/8; 32 vector equalities = 128 components).")
    print("PASS: same-vertex Yukawa-endpoint maps (4/4; 16 vector equalities = 64 components).")
    print("PASS: all Yukawa-endpoint maps (12/12; 48 vector equalities = 192 components).")
    print("PASS: cross-vertex scalar-seagull maps (4/4; 12 vector equalities = 48 components).")
    print("PASS: same-vertex scalar-seagull maps (2/2; 6 vector equalities = 24 components).")
    print("PASS: all scalar-seagull maps (6/6; 18 vector equalities = 72 components).")
    print("PROPAGATOR-DIFFERENCE ASSIGNMENT:")
    print("  cross A-Yukawa endpoint, after k_old -> k+q: D(k+q)")
    print("  cross B-Yukawa endpoint, unshifted: D(k)")
    print("  same F-Yukawa endpoint, unshifted: D(k)")
    print("  same S-Yukawa endpoint, after k_old -> k+q: D(k+q)")
    print("BOUNDARY:")
    print("  Adjacent matter momenta, heavy-channel momenta and W momenta match")
    print("  the corresponding three-W reference routing exactly.")
    print("  This is kinematic alignment only; it does not sum weak tensors or")
    print("  prove cancellation of the scalar seagull, ghost/ST, or external terms.")
    print("  No loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
