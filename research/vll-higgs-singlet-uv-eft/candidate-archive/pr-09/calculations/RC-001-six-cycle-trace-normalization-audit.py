#!/usr/bin/env python3
"""RC-001 independent trace, cycle-counting, and normalization audit.

Checks:
  * all 6 labelled scalar cycles x all 16 internal-state paths at exact rational
    routed Minkowski momenta, comparing an explicit 4x4 Dirac trace with an
    independently assembled chiral-projector decomposition;
  * reverse-cycle path/weight/mass mappings (Delta_0 is checked separately in the O(p^2) candidate-kernel ledger);
  * Gamma(4)=6 and four-parameter simplex volume 1/6;
  * the four-propagator Feynman-parameter prefactor;
  * determinant-log coefficient +i/4 at fourth order, kept distinct from the
    -1 closed-fermion-loop Feynman-rule sign;
  * the five convergent Euclidean scalar-integral factors used in the candidate
    B-kernel reduction.

This is not a complete UV-EFT matching calculation: it does not perform the
full symbolic O(p^2) coefficient extraction for all paths, integrate the
path-dependent simplex functions, generate all diagrams with FeynArts, or
close the complete EFT soft/counterterm set.
Requires Python 3 and SymPy.
"""
from itertools import permutations, product, combinations
from math import factorial
import hashlib
import sympy as sp

# Explicit Dirac matrices, metric (+---).
zero = sp.zeros(2)
sigmas = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0,-1],[1,0]])*sp.I,
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for sigma in sigmas:
    gamma.append(sp.Matrix.vstack(
        sp.Matrix.hstack(zero, sigma),
        sp.Matrix.hstack(-sigma, zero),
    ))
gamma5 = sp.I * gamma[0] * gamma[1] * gamma[2] * gamma[3]
PR = (sp.eye(4) + gamma5) / 2
PL = (sp.eye(4) - gamma5) / 2

def slash(k):
    return gamma[0]*k[0] - gamma[1]*k[1] - gamma[2]*k[2] - gamma[3]*k[3]

def dot(a, b):
    return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]

def simp(x):
    return sp.factor(sp.expand_complex(x))

# Exact rational benchmark parameters (not a physical benchmark fit).
a, b = sp.Integer(2), sp.Integer(3)
cL, sL = sp.Rational(3,5), sp.Rational(4,5)
cR, sR = sp.Rational(5,13), sp.Rational(12,13)
Yh = a * sp.Matrix([[cL*sR, cL*cR], [sL*sR, sL*cR]])
Ys = b * sp.Matrix([[sL*cR, -sL*sR], [-cL*cR, cL*sR]])
# Explicitly map the positive-light-mass Eq.(13) matrices to the signed-light-mass
# matrices used by the real-rotation two-point convention in source §276.
a_s,b_s,cLs,sLs,cRs,sRs = sp.symbols("a_s b_s cLs sLs cRs sRs", real=True)
Yh_s = a_s*sp.Matrix([[cLs*sRs,cLs*cRs],[sLs*sRs,sLs*cRs]])
Ys_s = b_s*sp.Matrix([[sLs*cRs,-sLs*sRs],[-cLs*cRs,cLs*sRs]])
Dphase = sp.diag(-1,1)
Gh_s = a_s*sp.Matrix([[-cLs*sRs,cLs*cRs],[-sLs*sRs,sLs*cRs]])
Gs_s = b_s*sp.Matrix([[-sLs*cRs,-sLs*sRs],[cLs*cRs,cLs*sRs]])
assert Gh_s == Yh_s*Dphase
assert Gs_s == Ys_s*Dphase
mass = {0: sp.Integer(2), 1: sp.Integer(5)}

labels = ("h1", "h2", "s1", "s2")
type_of = {"h1":"h", "h2":"h", "s1":"s", "s2":"s"}
cycles = [("h1",) + tail for tail in permutations(("h2", "s1", "s2"))]
paths = list(product((0,1), repeat=4))
# Three exact rational non-collinear external four-vectors; p4 is fixed by conservation.
p_by_label = {
    "h1": sp.Matrix([1, 2, -1, 3]),
    "h2": sp.Matrix([-2, 1, 2, 1]),
    "s1": sp.Matrix([3, -1, 1, 2]),
}
p_by_label["s2"] = -p_by_label["h1"] - p_by_label["h2"] - p_by_label["s1"]
K = sp.Matrix([sp.Rational(1,3), sp.Rational(-2,5), sp.Rational(3,7), sp.Rational(1,2)])
x = (sp.Rational(1,10), sp.Rational(2,10), sp.Rational(3,10), sp.Rational(4,10))
assert sum(x) == 1
trace_checks = 0
path_weights = {}

for cycle in cycles:
    seq = tuple(Yh if type_of[label] == "h" else Ys for label in cycle)
    q1, q2, q3 = [p_by_label[label] for label in cycle[:3]]
    # Route convention used in the frozen v66 ledger:
    # r=(0,-q2,-q2-q3,q1), K=k+R, k_i=K+r_i-R.
    r = [sp.zeros(4,1), -q2, -q2-q3, q1]
    R = sum((x[i]*r[i] for i in range(4)), sp.zeros(4,1))
    k = [K + r[i] - R for i in range(4)]
    for path in paths:
        nxt = path[1:] + path[:1]
        u = [seq[i][path[i], nxt[i]] for i in range(4)]
        v = [seq[i][nxt[i], path[i]] for i in range(4)]
        mu = [mass[nxt[i]] for i in range(4)]
        verts = [u[i]*PR + v[i]*PL for i in range(4)]
        z = sp.eye(4)
        for i in range(4):
            z = z * verts[i] * (slash(k[i]) + mu[i]*sp.eye(4))
        direct = simp(sp.trace(z))

        H = simp(u[0]*v[1]*u[2]*v[3] + v[0]*u[1]*v[2]*u[3])
        Hodd = simp(u[0]*v[1]*u[2]*v[3] - v[0]*u[1]*v[2]*u[3])
        M = simp(sp.prod(mu) * (sp.prod(u) + sp.prod(v)))
        C = {ij: sp.Integer(0) for ij in combinations(range(4),2)}
        for chirality in product((0,1), repeat=4):
            trans = tuple(i for i in range(4) if chirality[i] != chirality[(i+1)%4])
            if len(trans) != 2:
                continue
            ij = trans
            coupling = sp.prod(u[i] if chirality[i] == 0 else v[i] for i in range(4))
            mass_product = sp.prod(mu[i] for i in range(4) if i not in ij)
            C[ij] += coupling * mass_product
        C = {ij: simp(value) for ij, value in C.items()}
        G = (dot(k[0],k[1])*dot(k[2],k[3])
             - dot(k[0],k[2])*dot(k[1],k[3])
             + dot(k[0],k[3])*dot(k[1],k[2]))
        E = sp.det(sp.Matrix.hstack(*k))
        pred = (2*H*G + 2*sum(C[ij]*dot(k[ij[0]],k[ij[1]]) for ij in C)
                + 2*M + 2*sp.I*E*Hodd)
        residual = simp(direct-pred)
        if residual != 0:
            raise AssertionError(f"trace mismatch cycle={cycle} path={path}: {residual}")
        trace_checks += 1
        path_weights[(cycle,path)] = (H, C, M, tuple(mu))

# Six inequivalent labeled cycles: fix h1 as representative of cyclic rotations.
assert len(cycles) == factorial(4) // 4 == 6
assert len({cycle for cycle in cycles}) == 6

# Reverse cycle pairings and their path map. This is an algebraic bookkeeping check.
reverse_checks = 0
reverse_pairs = []
for cycle in cycles:
    rev = (cycle[0], cycle[3], cycle[2], cycle[1])
    if cycles.index(cycle) > cycles.index(rev):
        continue
    reverse_pairs.append((cycle, rev))
    for path in paths:
        rpath = (path[1], path[0], path[3], path[2])
        H, C, M, mu = path_weights[(cycle,path)]
        Hr, Cr, Mr, mur = path_weights[(rev,rpath)]
        assert sp.simplify(H-Hr) == 0
        assert sp.simplify(M-Mr) == 0
        assert tuple(reversed(mu)) == mur
        for ij in combinations(range(4),2):
            mapped = tuple(sorted((3-ij[0],3-ij[1])))
            assert sp.simplify(C[ij]-Cr[mapped]) == 0
        reverse_checks += 1

# Feynman parameter / simplex normalizations.
gamma4 = sp.gamma(4)
sx1, sx2, sx3 = sp.symbols("sx1 sx2 sx3", nonnegative=True)
simplex_volume = sp.integrate(
    sp.integrate(sp.integrate(1, (sx3,0,1-sx1-sx2)),
                 (sx2,0,1-sx1)),
    (sx1,0,1)
)
assert gamma4 == 6
assert simplex_volume == sp.Rational(1,6)
assert sp.simplify(gamma4 * simplex_volume - 1) == 0

# General Feynman-parameter identity prefactor for four unit powers:
# 1/(A1 A2 A3 A4) = Gamma(4) integral_simplex dx / (sum x_i A_i)^4.
assert sp.gamma(4) / sp.prod(sp.gamma(1) for _ in range(4)) == 6

# Euclidean integral factors in units 1/(16*pi^2), for d=4.
Delta = sp.symbols("Delta", positive=True)
I04 = sp.Rational(1,6)/Delta**2
I14 = sp.Rational(1,3)/Delta
I25 = sp.Rational(1,4)/Delta
I15 = sp.Rational(1,12)/Delta**2
I05 = sp.Rational(1,12)/Delta**3
assert sp.simplify(I04 - sp.gamma(2)*sp.gamma(2)/(sp.gamma(2)*sp.gamma(4)*Delta**2)) == 0
assert sp.simplify(I14 - sp.gamma(3)*sp.gamma(1)/(sp.gamma(2)*sp.gamma(4)*Delta)) == 0
assert sp.simplify(I25 - sp.gamma(4)*sp.gamma(1)/(sp.gamma(2)*sp.gamma(5)*Delta)) == 0
assert sp.simplify(I15 - sp.gamma(3)*sp.gamma(2)/(sp.gamma(2)*sp.gamma(5)*Delta**2)) == 0
assert sp.simplify(I05 - sp.gamma(2)*sp.gamma(3)/(sp.gamma(2)*sp.gamma(5)*Delta**3)) == 0

# Determinant logarithm coefficient at fourth order: Gamma_f=-i Tr ln(1+X).
z = sp.symbols("z")
series = sp.series(-sp.I*sp.log(1+z), z, 0, 5).removeO()
assert sp.expand(series).coeff(z,4) == sp.I/4
# Closed fermion loop in diagrammatic Feynman rules is a separate -1 factor.
closed_loop_sign = -1
assert closed_loop_sign == -1

print("PASS: Eq.(13) positive-light-mass Y_h/Y_s map to §276 signed-light-mass G_h/G_s by right rephasing D=diag(-1,1).")
print(f"PASS: {len(cycles)} inequivalent labeled cycles = 4!/4; each cycle is represented once.")
print(f"PASS: explicit Dirac trace/decomposition for {trace_checks} cases = 6 labeled cycles x 16 paths.")
print(f"PASS: reverse-cycle path/weight/mass mapping for {reverse_checks} path pairs across {len(reverse_pairs)} reverse pairs.")
print("PASS: Gamma(4)=6; four-parameter simplex volume=1/6; their product=1.")
print("PASS: four-propagator Feynman parameter prefactor Gamma(4)/prod Gamma(1)=6.")
print("PASS: all five stated Euclidean scalar-integral factors match the Gamma-function formula.")
print("PASS: determinant-log expansion coefficient at fourth order is +i/4 for Gamma_f=-i Tr ln(1+X).")
print("CONVENTION: the closed-fermion-loop Feynman-rule sign is -1 and must be reconciled with the determinant expansion; this script does not prove the full diagram's common i/sign.")
print("LIMIT: exact rational-point trace audit, not a symbolic O(p^2) coefficient proof; no full simplex integration, FeynArts/FeynCalc run, or complete EFT soft/counterterm subtraction.")
