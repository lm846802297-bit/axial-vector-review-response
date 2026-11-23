#!/usr/bin/env python3
"""RC-001 B2c-IVn-h/08: LD-W-03/04 same-vertex WTI endpoint/R_FG ordering.

Checks the actual left- and right-open endpoint reductions, their
Dirac-Hermitian relation, and their distinction from the pair-specific
two-W R_FG numerator. The heavy h_E propagator is kept as a spectator.
No complete longitudinal sum or STI closure is claimed.
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


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def add(a, b):
    return [sp.expand(a[i] + b[i]) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def scale(c, a):
    return [sp.expand(c * a[i]) for i in range(4)]


def slash(a):
    return sum((ETA[i] * a[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def zero(m):
    return all(sp.simplify(m[i, j]) == 0
               for i, j in product(range(4), repeat=2))


def count_nonzero(m):
    return sum(sp.simplify(m[i, j]) != 0
               for i, j in product(range(4), repeat=2))


def dirac_bar(m):
    return GAMMA[0] * m.conjugate().T * GAMMA[0]


def verify_symbolic_endpoint_orders():
    v = list(sp.symbols("V0:4", real=True))
    rw = list(sp.symbols("rW0:4", real=True))
    q = list(sp.symbols("q0:4", real=True))
    ry = add(rw, q)

    # Contract the actual W index with g_{mu nu}; the metric factors
    # are explicit because GAMMA[mu] stores gamma^mu.
    e03_w = sum((ETA[mu] * GAMMA[mu] * slash(rw) * PR * v[mu]
                 for mu in range(4)), sp.zeros(4))
    e03_y = -sum((ETA[mu] * GAMMA[mu] * PL * slash(ry) * v[mu]
                  for mu in range(4)), sp.zeros(4))
    r03_w = slash(v) * slash(rw) * PR
    r03_y = -slash(v) * slash(ry) * PR

    e04_w = sum((ETA[mu] * v[mu] * PL * slash(rw) * GAMMA[mu]
                 for mu in range(4)), sp.zeros(4))
    e04_y = -sum((ETA[mu] * v[mu] * slash(ry) * PR * GAMMA[mu]
                  for mu in range(4)), sp.zeros(4))
    r04_w = slash(rw) * slash(v) * PL
    r04_y = -slash(ry) * slash(v) * PL

    assert zero(e03_w - r03_w)
    assert zero(e03_y - r03_y)
    assert zero(e04_w - r04_w)
    assert zero(e04_y - r04_y)
    assert zero(dirac_bar(r03_w) - r04_w)
    assert zero(dirac_bar(r03_y) - r04_y)
    return 6


def verify_he_spectator_independence():
    """Check both h_E spectator routings are independent of loop momentum k."""
    checked = 0
    for pair in ("03", "04"):
        k = list(sp.symbols(f"k{pair}_0:4", real=True))
        pf = list(sp.symbols(f"pf{pair}_0:4", real=True))
        ps = list(sp.symbols(f"ps{pair}_0:4", real=True))
        q = list(sp.symbols(f"q{pair}_0:4", real=True))
        h_e = add(add(pf, ps), q)
        derivatives = [sp.diff(h_e[i], k[j])
                       for i in range(4) for j in range(4)]
        assert all(value == 0 for value in derivatives), (pair, derivatives)
        checked += len(derivatives)
    return checked


def audit_point(k, q, p1, p2, p3, m_e2):
    p4 = scale(-1, add(add(add(q, p1), p2), p3))
    kap = add(k, q)
    out = {}
    for pair, pf, ps in (("03", p1, p2), ("04", p4, p3)):
        rw = add(k, pf)
        ry = add(kap, pf)
        vs = sub(scale(2, ps), kap)
        h_e = add(add(pf, ps), q)
        if pair == "03":
            e_w = slash(vs) * slash(rw) * PR
            e_y = -slash(vs) * slash(ry) * PR
            rfg = (dot(vs, k) * slash(k) * slash(ry)
                   - dot(vs, kap) * slash(kap) * slash(ry))
        else:
            e_w = slash(rw) * slash(vs) * PL
            e_y = -slash(ry) * slash(vs) * PL
            rfg = (dot(vs, k) * slash(ry) * slash(k)
                   - dot(vs, kap) * slash(ry) * slash(kap))

        r_s = sub(ps, k)
        den = (
            dot(k, k), dot(kap, kap), dot(ry, ry),
            dot(r_s, r_s), dot(h_e, h_e) - m_e2,
        )
        assert all(x != 0 for x in den), (pair, den)
        assert count_nonzero(e_w) > 0
        assert count_nonzero(e_y) > 0
        assert count_nonzero(rfg) > 0
        assert not zero(e_w - e_y)
        assert not zero(e_w - rfg)
        assert not zero(e_y - rfg)
        # h_E is built only from external momenta; symbolic k-independence
        # is checked separately by verify_he_spectator_independence().
        out[pair] = {
            "endpoint_W": count_nonzero(e_w),
            "endpoint_Y": count_nonzero(e_y),
            "RFG": count_nonzero(rfg),
            "denominators": den,
        }
    return out


def main():
    symbolic = verify_symbolic_endpoint_orders()
    spectator = verify_he_spectator_independence()
    k = [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)]
    q = [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)]
    p1 = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    p2 = [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)]
    p3 = [sp.Integer(2), sp.Integer(1), sp.Integer(1), sp.Integer(1)]
    result = audit_point(k, q, p1, p2, p3, sp.Integer(400))
    print("RC-001 B2c-IVn-h/08: LD-W-03/04 same-vertex endpoint/R_FG order")
    print(f"PASS: four actual metric-contracted endpoint reductions and two Dirac-bar relations ({symbolic}/6).")
    for pair, data in result.items():
        print(f"PASS: LD-W-{pair} endpoint W/Y and R_FG are nonzero and pairwise distinct.")
        print(f"  nonzero entries W/Y/RFG={data['endpoint_W']}/{data['endpoint_Y']}/{data['RFG']};")
        print(f"  denominators={data['denominators']}.")
    print(f"PASS: h_E is k-independent for both same-vertex spectators ({spectator}/32 derivatives).")
    print("BOUNDARY: endpoint ordering only; no scalar+fermion+three-W sum, LSZ/ST closure,")
    print("          loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
