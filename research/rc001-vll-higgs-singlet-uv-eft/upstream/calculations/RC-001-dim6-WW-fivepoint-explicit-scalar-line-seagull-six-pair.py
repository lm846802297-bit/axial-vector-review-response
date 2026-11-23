#!/usr/bin/env python3
"""RC-001 B2c-IVm: explicit scalar-line plus seagull endpoint kernels.

Substitutes the common-k scalar-current and propagator routes for all six
WW pair classes. It keeps the symmetric seagull tensors and antisymmetric
commutator tensors distinct, and contracts the resulting internal-W current
with the actual opposite fermion/scalar endpoint current.
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

g2, SA, SB, SS, GAB, GFS = sp.symbols("g2 S_A S_B S_S G_AB G_FS")


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def add(a, b):
    return [sp.expand(a[i] + b[i]) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def scale(c, a):
    return [sp.expand(c * a[i]) for i in range(4)]


def slash(p):
    return sum((ETA[i] * p[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def matrix_zero(matrix):
    return all(sp.simplify(matrix[i, j]) == 0
               for i in range(matrix.rows) for j in range(matrix.cols))


def scalar_endpoint_A(p_a, k, q, symmetric, commutator):
    """Cross A scalar endpoint, after k_old -> k+q."""
    kap = add(k, q)
    r_y = sub(k, p_a)
    r_w = sub(kap, p_a)
    delta_y = 1 / dot(r_y, r_y)
    delta_w = 1 / dot(r_w, r_w)
    delta = sp.factor(delta_y - delta_w)
    v = sub(scale(2, p_a), kap)
    current = [
        sp.expand(g2 * (
            (-sp.Rational(1, 2) * delta * v[mu]
             + delta_y * q[mu]) * symmetric
            - I * sp.Rational(1, 2) * delta * v[mu] * commutator
        ))
        for mu in range(4)
    ]
    raw = [
        sp.expand(
            -g2 * delta * v[mu] * (symmetric / 2 + I * commutator / 2)
            + g2 * delta_y * q[mu] * symmetric
        )
        for mu in range(4)
    ]
    return current, raw, {
        "rY": r_y, "rW": r_w, "V": v,
        "DeltaY": delta_y, "DeltaW": delta_w, "delta": delta,
    }


def scalar_endpoint_BS(p_b, k, q, symmetric, commutator):
    """Cross B or same-vertex S scalar endpoint in common-k routing."""
    kap = add(k, q)
    if symmetric == SB:
        r_y = add(k, add(p_b, q))
        r_w = add(k, p_b)
        v = scale(-1, add(scale(2, p_b), k))
    else:
        r_y = sub(p_b, k)
        r_w = sub(p_b, kap)
        v = sub(scale(2, p_b), kap)
    delta_y = 1 / dot(r_y, r_y)
    delta_w = 1 / dot(r_w, r_w)
    delta = sp.factor(delta_y - delta_w)
    current = [
        sp.expand(g2 * (
            (sp.Rational(1, 2) * delta * v[mu]
             + delta_y * q[mu]) * symmetric
            + I * sp.Rational(1, 2) * delta * v[mu] * commutator
        ))
        for mu in range(4)
    ]
    raw = [
        sp.expand(
            +g2 * delta * v[mu] * (symmetric / 2 + I * commutator / 2)
            + g2 * delta_y * q[mu] * symmetric
        )
        for mu in range(4)
    ]
    return current, raw, {
        "rY": r_y, "rW": r_w, "V": v,
        "DeltaY": delta_y, "DeltaW": delta_w, "delta": delta,
    }


def verify_scalar_wti(data, q, orientation):
    r_y, r_w = data["rY"], data["rW"]
    lhs = dot(q, add(r_w, r_y)) / (dot(r_w, r_w) * dot(r_y, r_y))
    if orientation == "A":
        rhs = data["DeltaY"] - data["DeltaW"]
    else:
        rhs = data["DeltaW"] - data["DeltaY"]
    assert sp.simplify(lhs - rhs) == 0


def verify_endpoint_decompositions():
    p_a = list(sp.symbols("pA0:4", real=True))
    p_b = list(sp.symbols("pB0:4", real=True))
    k = list(sp.symbols("k0:4", real=True))
    q = list(sp.symbols("q0:4", real=True))
    c_a, raw_a, data_a = scalar_endpoint_A(p_a, k, q, SA, GAB)
    c_b, raw_b, data_b = scalar_endpoint_BS(p_b, k, q, SB, GAB)
    c_s, raw_s, data_s = scalar_endpoint_BS(p_b, k, q, SS, GFS)
    assert all(sp.simplify(c_a[i] - raw_a[i]) == 0 for i in range(4))
    assert all(sp.simplify(c_b[i] - raw_b[i]) == 0 for i in range(4))
    assert all(sp.simplify(c_s[i] - raw_s[i]) == 0 for i in range(4))
    verify_scalar_wti(data_a, q, "A")
    verify_scalar_wti(data_b, q, "B")
    verify_scalar_wti(data_s, q, "S")
    return 12


def audit_pair_kernels(k, q, p1, p2, p3):
    p4 = scale(-1, add(add(add(q, p1), p2), p3))
    kap = add(k, q)
    h = sub(k, add(p1, p2))
    out = {}

    # LD-W-02: B=Hdag scalar, opposite A=barL fermion.
    c_b, _, d_b = scalar_endpoint_BS(p3, k, q, SB, GAB)
    x_a = -slash(sub(k, p1))
    k02 = slash(c_b) * x_a * slash(h) / dot(k, k)
    out["02-B"] = (
        k02,
        (dot(k, k), dot(sub(k, p1), sub(k, p1)),
         dot(d_b["rY"], d_b["rY"]), dot(d_b["rW"], d_b["rW"]),
         dot(h, h) - 400),
        d_b,
    )

    # LD-W-05: A=H scalar, opposite B=L fermion.
    c_a, _, d_a = scalar_endpoint_A(p2, k, q, SA, GAB)
    r_by = add(add(k, p4), q)
    k05 = slash(h) * slash(r_by) * slash(c_a) / dot(kap, kap)
    out["05-A"] = (
        k05,
        (dot(kap, kap), dot(r_by, r_by),
         dot(d_a["rY"], d_a["rY"]), dot(d_a["rW"], d_a["rW"]),
         dot(h, h) - 400),
        d_a,
    )

    # LD-W-06: two distinct scalar endpoints and two distinct seagull tensors.
    c_a6, _, d_a6 = scalar_endpoint_A(p2, k, q, SA, GAB)
    v_b6 = scale(-1, add(scale(2, p3), kap))
    k06a = slash(h) * dot(c_a6, v_b6) / dot(kap, kap)
    r_by6 = add(add(k, p3), q)
    out["06-A"] = (
        k06a,
        (dot(kap, kap), dot(r_by6, r_by6),
         dot(d_a6["rY"], d_a6["rY"]), dot(d_a6["rW"], d_a6["rW"]),
         dot(h, h) - 400),
        d_a6,
    )

    c_b6, _, d_b6 = scalar_endpoint_BS(p3, k, q, SB, GAB)
    v_a6 = sub(scale(2, p2), k)
    k06b = dot(v_a6, c_b6) * slash(h) / dot(k, k)
    r_a6 = sub(k, p2)
    out["06-B"] = (
        k06b,
        (dot(k, k), dot(r_a6, r_a6),
         dot(d_b6["rY"], d_b6["rY"]), dot(d_b6["rW"], d_b6["rW"]),
         dot(h, h) - 400),
        d_b6,
    )

    # LD-W-03/04: same-vertex S endpoint; heavy channel remains external spectator.
    for pair_id, p_f, p_s in (("03", p1, p2), ("04", p4, p3)):
        c_s, _, d_s = scalar_endpoint_BS(p_s, k, q, SS, GFS)
        r_fy = add(add(k, p_f), q)
        if pair_id == "03":
            kernel = slash(c_s) * slash(r_fy) / dot(kap, kap)
        else:
            kernel = slash(r_fy) * slash(c_s) / dot(kap, kap)
        h_e = add(add(p_f, p_s), q)
        out[pair_id + "-S"] = (
            kernel,
            (dot(kap, kap), dot(r_fy, r_fy),
             dot(d_s["rY"], d_s["rY"]), dot(d_s["rW"], d_s["rW"]),
             dot(h_e, h_e) - 400),
            d_s,
        )

    return out


def audit_points():
    points = (
        (
            [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)],
            [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)],
            [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)],
            [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)],
            [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)],
        ),
        (
            [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)],
            [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)],
            [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)],
            [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)],
            [sp.Integer(3), sp.Integer(0), sp.Integer(1), sp.Integer(0)],
        ),
    )
    return tuple(audit_pair_kernels(*point) for point in points)


def main():
    symbolic_checks = verify_endpoint_decompositions()
    points = audit_points()
    print(f"PASS: A-side, B-side, and same-vertex scalar line+seagull decompositions ({symbolic_checks}/12 component identities).")
    print("PASS: A/B/S scalar-line WTIs with their oriented propagator differences (3/3).")
    for n, result in enumerate(points, start=1):
        for label, (kernel, den, data) in result.items():
            assert all(x != 0 for x in den), (n, label, den)
            assert any(sp.simplify(x) != 0 for x in kernel), (n, label)
        print(f"PASS: explicit contracted scalar-line+seagull kernels at rational point {n} ({len(result)}/6 scalar endpoints).")
    print("ENDPOINT KERNELS:")
    print("  LD-W-02 B scalar -> slash(C_B) X_A slash(h) / k^2")
    print("  LD-W-05 A scalar -> slash(h) slash(r_B^Y) slash(C_A) / (k+q)^2")
    print("  LD-W-06 A and B scalar -> two separate kernels with S_A and S_B")
    print("  LD-W-03 S scalar -> slash(C_S) slash(r_F^Y) / (k+q)^2")
    print("  LD-W-04 S scalar -> slash(r_F^Y) slash(C_S) / (k+q)^2")
    print("BOUNDARY: the six scalar endpoint kernels are explicit; no sum with R_FG/ghost/ST,")
    print("          no loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
