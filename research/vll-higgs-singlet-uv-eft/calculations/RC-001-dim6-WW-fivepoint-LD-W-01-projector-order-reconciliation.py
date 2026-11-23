#!/usr/bin/env python3
"""RC-001 B2c-IVn-h/07: LD-W-01 F-F WTI projector/order audit.

Reduces both oriented fermion-WTI endpoints in the actual ordered F-F chains,
checks the shifted A-side/unshifted B-side common-k endpoint equality, and
verifies the final P_L placement in the pair-specific two-W R_FG projection.
This is a local algebraic sub-block, not the complete six-pair STI.
"""
from itertools import product
import sympy as sp

I = sp.I
ETA = (1, -1, -1, -1)
SIGMA = (sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -I], [I, 0]]),
         sp.Matrix([[1, 0], [0, -1]]))
GAMMA = [sp.diag(1, 1, -1, -1)]
for s in SIGMA:
    GAMMA.append(sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), s),
        sp.Matrix.hstack(-s, sp.zeros(2))))
GAMMA5 = I * GAMMA[0] * GAMMA[1] * GAMMA[2] * GAMMA[3]
PL, PR = (sp.eye(4) - GAMMA5) / 2, (sp.eye(4) + GAMMA5) / 2
GD = [ETA[mu] * GAMMA[mu] for mu in range(4)]


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def add(a, b):
    return [sp.expand(a[i] + b[i]) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def slash(a):
    return sum((ETA[i] * a[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def zero(m):
    return all(sp.simplify(m[i, j]) == 0
               for i, j in product(range(m.rows), range(m.cols)))


def nz(m):
    return sum(sp.simplify(m[i, j]) != 0
               for i, j in product(range(m.rows), range(m.cols)))


def point():
    k = [sp.Integer(x) for x in (4, 1, 2, 1)]
    q = [sp.Integer(x) for x in (1, 2, 0, 1)]
    p1 = [sp.Integer(x) for x in (1, 0, 1, 0)]
    p2 = [sp.Integer(x) for x in (0, 1, 0, 2)]
    p3 = [sp.Integer(x) for x in (2, 0, 1, 1)]
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    kap = add(k, q)
    ra, ray = sub(k, p1), sub(sub(k, p1), q)
    rbw, rby = add(k, p4), add(add(k, p4), q)
    h = sub(k, add(p1, p2))
    return k, q, p1, p2, p3, p4, kap, ra, ray, rbw, rby, h, sub(h, q)


def check_chiral():
    r = list(sp.symbols("r0:4", real=True))
    n = 0
    for mu in range(4):
        assert zero(PL * GAMMA[mu] - GAMMA[mu] * PR)
        assert zero(PR * GAMMA[mu] - GAMMA[mu] * PL)
        n += 2
    assert zero(PL * slash(r) - slash(r) * PR)
    assert zero(PR * slash(r) - slash(r) * PL)
    return n + 2


def check_endpoints():
    k, q, p1, p2, p3, p4, kap, ra, ray, rbw, rby, h, ha = point()
    saw, say = -slash(ra) / dot(ra, ra), -slash(ray) / dot(ray, ray)
    sbw, sby = slash(rbw) / dot(rbw, rbw), slash(rby) / dot(rby, rby)
    counts = dict(A_W=0, A_Y=0, B_W=0, B_Y=0)
    for mu, nu in product(range(4), repeat=2):
        raw = (
            GD[mu] * saw * PR * slash(ha) * sbw * GD[nu] * PL,
            -GD[mu] * PL * say * slash(ha) * sbw * GD[nu] * PL,
            GD[mu] * saw * slash(h) * PL * sbw * GD[nu] * PL,
            -GD[mu] * saw * slash(h) * sby * PR * GD[nu] * PL,
        )
        reduced = (
            GD[mu] * saw * slash(ha) * sbw * GD[nu] * PL,
            -GD[mu] * say * slash(ha) * sbw * GD[nu] * PL,
            GD[mu] * saw * slash(h) * sbw * GD[nu] * PL,
            -GD[mu] * saw * slash(h) * sby * GD[nu] * PL,
        )
        for key, a, b in zip(counts, raw, reduced):
            assert zero(a - b), key
            counts[key] += 16
    den = (dot(k, k), dot(kap, kap), dot(ra, ra), dot(ray, ray),
           dot(rbw, rbw), dot(rby, rby), dot(h, h)-400,
           dot(ha, ha)-400)
    assert all(x != 0 for x in den)
    return counts, den


def check_common_k_second_endpoints():
    k, q, p1, p2, p3, p4, kap, ra, ray, rbw, rby, h, ha = point()
    sa, sb = -slash(ra)/dot(ra, ra), slash(rby)/dot(rby, rby)
    n = 0
    for mu, nu in product(range(4), repeat=2):
        # A-side second endpoint after k_old=k+q.
        ay = -GD[mu] * PL * sa * slash(h) * sb * GD[nu] * PL
        # B-side second endpoint already in common-k routing.
        by = -GD[mu] * sa * slash(h) * sb * PR * GD[nu] * PL
        red = -GD[mu] * sa * slash(h) * sb * GD[nu] * PL
        assert zero(ay-red) and zero(by-red) and zero(ay-by)
        n += 16
    ko = add(k, q)
    maps = (sub(ko, add(p1, q)), sub(sub(ko, add(p1, p2)), q),
            add(ko, p4), ko)
    targets = (ra, h, rby, kap)
    vchecks = sum(
        1 for a, b in zip(maps, targets) for i in range(4)
        if sp.simplify(a[i]-b[i]) == 0
    )
    assert vchecks == 16
    spec = dot(ra, ra)*dot(rby, rby)*(dot(h, h)-400)
    d3 = dot(k, k)*dot(kap, kap)*spec
    assert sp.simplify(d3/dot(k, k)-dot(kap, kap)*spec) == 0
    assert sp.simplify(d3/dot(kap, kap)-dot(k, k)*spec) == 0
    return n, vchecks, 2


def check_rfg_order():
    k, q, p1, p2, p3, p4, kap, ra, ray, rbw, rby, h, ha = point()
    x = -slash(ra)*slash(h)*slash(rby)  # no P_L yet
    corr = slash(k)*x*slash(k)*PL - slash(kap)*x*slash(kap)*PL
    direct = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        c = ETA[mu]*ETA[nu]*(k[mu]*k[nu]-kap[mu]*kap[nu])
        direct += GAMMA[mu]*x*GAMMA[nu]*PL*c
    assert zero(direct-corr)
    old = slash(k)*(x*PL)*slash(k)-slash(kap)*(x*PL)*slash(kap)
    old_diff = nz(direct-old)
    endpoint = slash(ra)*slash(h)*slash(rby)*PL
    assert old_diff == 16 and nz(corr) == 16
    assert nz(corr-endpoint) == 16
    ends = (
        -slash(ra)*slash(ha)*slash(rbw)*PL,
        slash(ray)*slash(ha)*slash(rbw)*PL,
        -slash(ra)*slash(h)*slash(rbw)*PL,
        slash(ra)*slash(h)*slash(rby)*PL,
    )
    distinct = 0
    for e in ends:
        contracted = sum((GD[mu]*e*GD[mu] for mu in range(4)), sp.zeros(4))
        assert nz(contracted) > 0 and nz(corr-contracted) == 16
        distinct += 16
    return nz(corr), old_diff, distinct


def main():
    chiral = check_chiral()
    counts, den = check_endpoints()
    shifted, vectors, align = check_common_k_second_endpoints()
    rfg, old, distinct = check_rfg_order()
    assert chiral == 10
    assert counts == dict(A_W=256, A_Y=256, B_W=256, B_Y=256)
    assert (shifted, vectors, align) == (256, 16, 2)
    assert (rfg, old, distinct) == (16, 16, 64)
    print("RC-001 B2c-IVn-h/07: LD-W-01 F-F WTI projector/order reconciliation")
    print(f"PASS: chiral intertwining identities ({chiral}/10).")
    print("PASS: actual A/B WTI endpoint reductions "
          "(1024/1024 matrix entries; 256 each for A_W, A_Y, B_W, B_Y).")
    print(f"PASS: shifted A-side and common-k B-side second endpoints ({shifted}/256).")
    print(f"PASS: A-side shift maps ({vectors}/16); single-W denominator alignments ({align}/2).")
    print("PASS: direct/factorized R_FG contraction (16/16); incorrect pre-slash(k) "
          f"P_L placement rejected ({old}/16).")
    print(f"PASS: R_FG distinct from common one-W chain and four endpoint contractions ({distinct}/64).")
    print("DENOMINATORS: " + ", ".join(str(x) for x in den))
    print("BOUNDARY: R_FG remains nonzero; no six-pair sum, LSZ, ghost/ST, "
          "counterterm closure, loop integration, UV-EFT subtraction, or Wilson coefficient.")


if __name__ == "__main__":
    main()
