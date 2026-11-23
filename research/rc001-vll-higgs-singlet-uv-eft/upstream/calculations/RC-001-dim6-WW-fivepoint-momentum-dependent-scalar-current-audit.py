#!/usr/bin/env python3
"""RC-001 B2c-IVn-e: audit momentum-dependent scalar currents across IVl/IVm.

The universal common-kernel test in IVh uses momentum-independent symbolic
endpoint currents. This audit compares the actual scalar derivative currents
used by the IVl R_FG projection with the shifted currents used by the IVm
scalar-line/seagull kernels. It tests whether those currents can be identified
without an additional loop-momentum rerouting or a derived shift identity.

A nonzero difference is a routing-consistency flag, not by itself proof that
the physical diagrams fail to cancel. No graph is deleted and no R_FG term is
set to zero.
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


def V_A(p, w):
    return sub(scale(2, p), w)


def V_B(p, w):
    return scale(-1, add(scale(2, p), w))


def V_S(p, w):
    return sub(scale(2, p), w)


def current_dot(current, p):
    if isinstance(current[0], sp.MatrixBase):
        return slash(p)
    return sp.eye(4) * dot(current, p)


def rfg_numerator(JA, chain, JB, k, q):
    kap = add(k, q)
    return (
        current_dot(JA, k) * chain * current_dot(JB, k)
        - current_dot(JA, kap) * chain * current_dot(JB, kap)
    )


def matrix_zero(matrix):
    return all(sp.simplify(matrix[i, j]) == 0
               for i in range(matrix.rows) for j in range(matrix.cols))


def nonzero_entries(matrix):
    return sum(sp.simplify(matrix[i, j]) != 0
               for i in range(matrix.rows) for j in range(matrix.cols))


def verify_exact_scalar_current_shifts():
    p_a = list(sp.symbols("pA0:4", real=True))
    p_b = list(sp.symbols("pB0:4", real=True))
    p_s = list(sp.symbols("pS0:4", real=True))
    k = list(sp.symbols("k0:4", real=True))
    q = list(sp.symbols("q0:4", real=True))
    kap = add(k, q)

    # IVl uses A(k), B(k+q), S(k); IVm uses A(k+q), B(k), S(k+q).
    differences = {
        "A": sub(V_A(p_a, k), V_A(p_a, kap)),
        "B": sub(V_B(p_b, k), V_B(p_b, kap)),
        "S": sub(V_S(p_s, k), V_S(p_s, kap)),
    }
    for label, difference in differences.items():
        assert all(sp.simplify(difference[i] - q[i]) == 0
                   for i in range(4)), label
    return 12


def build_rational_diagnostic():
    k = [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)]
    q = [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)]
    p1 = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    p2 = [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)]
    p3 = [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    p4 = scale(-1, add(add(add(q, p1), p2), p3))
    return k, q, p1, p2, p3, p4


def audit_actual_scalar_endpoint_rfg_differences():
    k, q, p1, p2, p3, p4 = build_rational_diagnostic()
    kap = add(k, q)
    h = sub(k, add(p1, p2))
    results = {}

    # LD-W-02: IVm B-scalar current V_B(k); IVl R_FG uses V_B(k+q).
    r_a = sub(k, p1)
    chain02 = -slash(r_a) * slash(h)
    j_a02 = GAMMA
    j_b_line02 = V_B(p3, k)
    j_b_3w02 = V_B(p3, kap)
    diff02 = rfg_numerator(
        j_a02, chain02, j_b_line02, k, q
    ) - rfg_numerator(
        j_a02, chain02, j_b_3w02, k, q
    )
    results["LD-W-02:B"] = diff02

    # LD-W-05: IVm A-scalar current V_A(k+q); IVl R_FG uses V_A(k).
    r_by = add(kap, p4)
    chain05 = slash(h) * slash(r_by)
    j_a_line05 = V_A(p2, kap)
    j_a_3w05 = V_A(p2, k)
    j_b05 = GAMMA
    diff05 = rfg_numerator(
        j_a_line05, chain05, j_b05, k, q
    ) - rfg_numerator(
        j_a_3w05, chain05, j_b05, k, q
    )
    results["LD-W-05:A"] = diff05

    # LD-W-06: the A seagull/line route uses (V_A(k+q),V_B(k+q));
    # the B seagull/line route uses (V_A(k),V_B(k)); IVl uses
    # the mixed three-W pair (V_A(k),V_B(k+q)).
    chain06 = slash(h)
    va_k, va_kap = V_A(p2, k), V_A(p2, kap)
    vb_k, vb_kap = V_B(p3, k), V_B(p3, kap)
    diff06a = rfg_numerator(
        va_kap, chain06, vb_kap, k, q
    ) - rfg_numerator(
        va_k, chain06, vb_kap, k, q
    )
    diff06b = rfg_numerator(
        va_k, chain06, vb_k, k, q
    ) - rfg_numerator(
        va_k, chain06, vb_kap, k, q
    )
    results["LD-W-06:A-current"] = diff06a
    results["LD-W-06:B-current"] = diff06b

    # LD-W-03: seed order gamma_mu slash(r_F) V_S^mu.
    p_f03, p_s03 = p1, p2
    r_fy03 = add(kap, p_f03)
    chain03 = slash(r_fy03)
    vs_line03, vs_3w03 = V_S(p_s03, kap), V_S(p_s03, k)
    diff03 = rfg_numerator(
        GAMMA, chain03, vs_line03, k, q
    ) - rfg_numerator(
        GAMMA, chain03, vs_3w03, k, q
    )
    results["LD-W-03:S"] = diff03

    # LD-W-04: conjugate seed order V_S^mu slash(r_F) gamma_mu.
    p_f04, p_s04 = p4, p3
    r_fy04 = add(kap, p_f04)
    chain04 = slash(r_fy04)
    vs_line04, vs_3w04 = V_S(p_s04, kap), V_S(p_s04, k)
    diff04 = rfg_numerator(
        vs_line04, chain04, GAMMA, k, q
    ) - rfg_numerator(
        vs_3w04, chain04, GAMMA, k, q
    )
    results["LD-W-04:S"] = diff04

    denominators = {
        "LD-W-02": (
            dot(k, k), dot(r_a, r_a),
            dot(add(kap, p3), add(kap, p3)),
            dot(add(k, p3), add(k, p3)), dot(h, h) - 400,
        ),
        "LD-W-05": (
            dot(kap, kap), dot(r_by, r_by),
            dot(sub(k, p2), sub(k, p2)),
            dot(sub(kap, p2), sub(kap, p2)), dot(h, h) - 400,
        ),
        "LD-W-06": (
            dot(k, k), dot(kap, kap),
            dot(sub(k, p2), sub(k, p2)),
            dot(sub(kap, p2), sub(kap, p2)),
            dot(add(k, p3), add(k, p3)),
            dot(add(kap, p3), add(kap, p3)), dot(h, h) - 400,
        ),
        "LD-W-03": (
            dot(k, k), dot(kap, kap),
            dot(r_fy03, r_fy03), dot(sub(p_s03, k), sub(p_s03, k)),
            dot(add(add(p_f03, p_s03), q),
                add(add(p_f03, p_s03), q)) - 400,
        ),
        "LD-W-04": (
            dot(k, k), dot(kap, kap),
            dot(r_fy04, r_fy04), dot(sub(p_s04, k), sub(p_s04, k)),
            dot(add(add(p_f04, p_s04), q),
                add(add(p_f04, p_s04), q)) - 400,
        ),
    }
    assert all(all(value != 0 for value in values)
               for values in denominators.values())
    assert all(nonzero_entries(matrix) > 0 for matrix in results.values())
    return results, denominators


def metric(mu, nu):
    return sp.Integer(ETA[mu]) if mu == nu else sp.Integer(0)


def gamma3(alpha, mu, nu, q, k):
    """Gamma_{alpha mu nu}(q,k,-k-q), all momenta incoming."""
    return (
        metric(alpha, mu) * ETA[nu] * (q[nu] - k[nu])
        + metric(mu, nu) * ETA[alpha] * (2*k[alpha] + q[alpha])
        + metric(nu, alpha) * ETA[mu] * (-k[mu] - 2*q[mu])
    )


def verify_three_w_internal_leg_exchange():
    q = list(sp.symbols("q3W0:4", real=True))
    k = list(sp.symbols("k3W0:4", real=True))
    kap = add(k, q)
    lorentz_checks = 0
    for alpha, mu, nu in product(range(4), repeat=3):
        original = gamma3(alpha, mu, nu, q, k)
        exchanged = gamma3(alpha, nu, mu, q, scale(-1, kap))
        assert sp.simplify(exchanged + original) == 0
        lorentz_checks += 1

    group_checks = 0
    combined_checks = 0
    for a, b, c in product(range(3), repeat=3):
        eps_original = sp.LeviCivita(a, b, c)
        eps_exchanged = sp.LeviCivita(a, c, b)
        assert sp.simplify(eps_exchanged + eps_original) == 0
        group_checks += 1
        for alpha, mu, nu in product(range(4), repeat=3):
            original = eps_original * gamma3(alpha, mu, nu, q, k)
            exchanged = eps_exchanged * gamma3(
                alpha, nu, mu, q, scale(-1, kap)
            )
            assert sp.simplify(exchanged - original) == 0
            combined_checks += 1
    return lorentz_checks, group_checks, combined_checks


def verify_actual_denominator_route_factors():
    me2 = sp.symbols("M_E2", real=True)
    k = list(sp.symbols("kDen0:4", real=True))
    q = list(sp.symbols("qDen0:4", real=True))
    kap = add(k, q)
    k2, kap2 = dot(k, k), dot(kap, kap)

    # Cross-vertex routing: r_A=k-p_A, r_B=k+p_B, h=k-P.
    p_a = list(sp.symbols("pADen0:4", real=True))
    p_b = list(sp.symbols("pBDen0:4", real=True))
    p_ap = list(sp.symbols("pAprimeDen0:4", real=True))
    p_bp = list(sp.symbols("pBprimeDen0:4", real=True))
    r_a = sub(k, p_a)
    r_b = add(k, p_b)
    h = sub(k, add(p_a, p_ap))
    hden = dot(h, h) - me2
    r_a2 = dot(r_a, r_a)
    r_aq2 = dot(add(r_a, q), add(r_a, q))
    r_b2 = dot(r_b, r_b)
    r_bq2 = dot(add(r_b, q), add(r_b, q))

    d_3w = k2 * kap2 * r_a2 * r_bq2 * hden
    d_a_line = kap2 * r_a2 * r_aq2 * r_bq2 * hden
    d_a_sg = kap2 * r_a2 * r_bq2 * hden
    d_b_line = k2 * r_a2 * r_b2 * r_bq2 * hden
    d_b_sg = k2 * r_a2 * r_bq2 * hden

    cross_checks = (
        d_a_line * k2 - d_3w * r_aq2,
        d_a_sg * k2 - d_3w,
        d_b_line * kap2 - d_3w * r_b2,
        d_b_sg * kap2 - d_3w,
    )
    assert all(sp.simplify(x) == 0 for x in cross_checks)

    # Same-vertex routing: F line and S line share h_E=p_F+p_S+q.
    p_f = list(sp.symbols("pFDen0:4", real=True))
    p_s = list(sp.symbols("pSDen0:4", real=True))
    r_f = add(k, p_f)
    r_fy = add(kap, p_f)
    r_s = sub(p_s, k)
    r_sw = sub(p_s, kap)
    h_e = add(add(p_f, p_s), q)
    h_eden = dot(h_e, h_e) - me2
    r_f2 = dot(r_f, r_f)
    r_fy2 = dot(r_fy, r_fy)
    r_s2 = dot(r_s, r_s)
    r_sw2 = dot(r_sw, r_sw)

    d_3w_same = k2 * kap2 * r_fy2 * r_s2 * h_eden
    d_f_line = k2 * r_f2 * r_fy2 * r_s2 * h_eden
    d_s_line = kap2 * r_fy2 * r_s2 * r_sw2 * h_eden
    d_s_sg = kap2 * r_fy2 * r_s2 * h_eden

    same_checks = (
        d_f_line * kap2 - d_3w_same * r_f2,
        d_s_line * k2 - d_3w_same * r_sw2,
        d_s_sg * k2 - d_3w_same,
    )
    assert all(sp.simplify(x) == 0 for x in same_checks)
    return len(cross_checks) + len(same_checks)


def main():
    shift_checks = verify_exact_scalar_current_shifts()
    results, denominators = audit_actual_scalar_endpoint_rfg_differences()
    leg_exchange = verify_three_w_internal_leg_exchange()
    denominator_checks = verify_actual_denominator_route_factors()
    print("RC-001 B2c-IVn-e momentum-dependent scalar-current audit")
    print(f"PASS: exact A/B/S scalar-current shifts are q ({shift_checks}/12 vector components).")
    print(f"PASS: three-W internal-leg exchange Lorentz sign ({leg_exchange[0]}/64), group sign ({leg_exchange[1]}/27), combined vertex invariance ({leg_exchange[2]}/1728).")
    print(f"PASS: actual cross/same-vertex line, seagull and three-W denominator factor maps ({denominator_checks}/7 exact identities).")
    print("ACTUAL IVm versus IVl CURRENT ROUTES:")
    print("  LD-W-02 B scalar: V_B(k) versus V_B(k+q)")
    print("  LD-W-03/04 S scalar: V_S(k+q) versus V_S(k)")
    print("  LD-W-05 A scalar: V_A(k+q) versus V_A(k)")
    print("  LD-W-06 A scalar route: (V_A(k+q),V_B(k+q)) versus mixed three-W currents")
    print("  LD-W-06 B scalar route: (V_A(k),V_B(k)) versus mixed three-W currents")
    print("RATIONAL DIAGNOSTIC (M_E^2=400; all listed denominators nonzero):")
    for label, matrix in results.items():
        simplified = matrix.applyfunc(sp.simplify)
        print(
            f"  {label}: nonzero entries in current-substitution difference "
            f"= {nonzero_entries(simplified)}/16; trace={sp.simplify(sp.trace(simplified))}"
        )
    print("RESULT: the actual scalar-current substitutions are not interchangeable inside the R_FG projection.")
    print("INTERPRETATION: IVh's arbitrary-current tensor identity remains valid, but its use as a")
    print("  graph-specific cancellation is not yet demonstrated for momentum-dependent scalar currents.")
    print("  A common routing or an explicit change-of-variable identity is required before summing.")
    print("BOUNDARY: no physical non-cancellation is claimed; no graph is omitted, no R_FG is removed,")
    print("  and no loop integration, ghost/ST completion, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
