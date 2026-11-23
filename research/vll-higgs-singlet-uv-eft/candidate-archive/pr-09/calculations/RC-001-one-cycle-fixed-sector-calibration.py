#!/usr/bin/env python3
"""Independent one-cycle calibration of the RC-001 B2 kernel.

This check uses the zero-mixing/unbroken Yukawa limit for one labeled cycle
h1 -> s1 -> s2 -> h2. It derives the exact Dirac trace and the denominator
shift for the source-aligned fixed routing. It validates the B2 relative sign
and integral normalization for this path only.

It does NOT determine the common diagrammatic i/sign, graph multiplicity,
or the B1/B3 signs: H and the four-mass term vanish in this limit.
Requires Python 3 and SymPy.
"""
from itertools import product, combinations
import sympy as sp

# Explicit Dirac matrices, metric (+---).
I = sp.I
zero = sp.zeros(2)
sigmas = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -1], [1, 0]]) * I,
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for sigma in sigmas:
    gamma.append(sp.Matrix.vstack(
        sp.Matrix.hstack(zero, sigma),
        sp.Matrix.hstack(-sigma, zero),
    ))
gamma5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])
PR = sp.simplify((sp.eye(4) + gamma5) / 2)
PL = sp.simplify((sp.eye(4) - gamma5) / 2)

def slash(v):
    return gamma[0]*v[0] - gamma[1]*v[1] - gamma[2]*v[2] - gamma[3]*v[3]

def dot(u, v):
    return sp.expand(u[0]*v[0] - u[1]*v[1] - u[2]*v[2] - u[3]*v[3])

checks = 0
def check(name, expr):
    global checks
    residual = sp.simplify(expr)
    if isinstance(residual, sp.MatrixBase):
        ok = all(sp.simplify(entry) == 0 for entry in residual)
    else:
        ok = residual == 0
    if not ok:
        raise AssertionError(f"{name}: residual={residual}")
    checks += 1
    print(f"PASS: {name}")

a, b, M = sp.symbols("y lambda M_E", nonzero=True)
# Positive-light-mass Eq.(13) convention in the zero-mixing limit.
Yh = a * sp.Matrix([[0, 1], [0, 0]])
Ys = b * sp.Matrix([[0, 0], [-1, 0]])

# External routing: q1=p1 (h1), q2=p4 (s1), q3=p2 (s2),
# q4=p3 (h2)=-q1-q2-q3. The source loop variable is k=k_2.
q1 = sp.Matrix([sp.Symbol(f"p1_{mu}") for mu in range(4)])
p4 = sp.Matrix([sp.Symbol(f"p4_{mu}") for mu in range(4)])
p2 = sp.Matrix([sp.Symbol(f"p2_{mu}") for mu in range(4)])
q2, q3 = p4, p2
q4 = -q1 - q2 - q3
q = -(q1 + q2)

cycle_vertices = (Yh, Ys, Ys, Yh)
r = [sp.zeros(4, 1), -q2, -q2-q3, q1]
x1, x2, x3, x4 = sp.symbols("x1:5")
xs = (x1, x2, x3, x4)
R = sum((xs[i]*r[i] for i in range(4)), sp.zeros(4, 1))
K = sp.Matrix([sp.Symbol(f"K_{mu}") for mu in range(4)])
kline = [K + r[i] - R for i in range(4)]

# Path (0,1,0,1): state 0 is the massless light fermion; state 1 is E.
path = (0, 1, 0, 1)
nxt = path[1:] + path[:1]
mass = {0: sp.Integer(0), 1: M}
mu = tuple(mass[nxt[i]] for i in range(4))
u = [cycle_vertices[i][path[i], nxt[i]] for i in range(4)]
v = [cycle_vertices[i][nxt[i], path[i]] for i in range(4)]
V = [u[i]*PR + v[i]*PL for i in range(4)]

trace_matrix = sp.eye(4)
for i in range(4):
    trace_matrix = trace_matrix * V[i] * (slash(kline[i]) + mu[i]*sp.eye(4))
trace = sp.factor(sp.expand(sp.trace(trace_matrix)))
C = a**2 * b**2 * M**2

check("direct trace = 2 y^2 lambda^2 M_E^2 k_2.k_4",
      trace - 2*C*dot(kline[1], kline[3]))

# Exhaust the other 15 internal-state paths for this same labeled cycle.
nonzero_paths = []
for candidate in product((0, 1), repeat=4):
    candidate_nxt = candidate[1:] + candidate[:1]
    candidate_mu = tuple(mass[candidate_nxt[i]] for i in range(4))
    candidate_u = [cycle_vertices[i][candidate[i], candidate_nxt[i]] for i in range(4)]
    candidate_v = [cycle_vertices[i][candidate_nxt[i], candidate[i]] for i in range(4)]
    candidate_V = [candidate_u[i]*PR + candidate_v[i]*PL for i in range(4)]
    candidate_trace = sp.eye(4)
    for i in range(4):
        candidate_trace = candidate_trace * candidate_V[i] * (
            slash(kline[i]) + candidate_mu[i]*sp.eye(4)
        )
    if sp.simplify(sp.expand(sp.trace(candidate_trace))) != 0:
        nonzero_paths.append(candidate)
if nonzero_paths != [path]:
    raise AssertionError(f"unexpected nonzero paths in the zero-mixing limit: {nonzero_paths}")
checks += 1
print("PASS: exhaustive 16-path sum leaves only path (0,1,0,1) nonzero")

assert mu == (M, sp.Integer(0), M, sp.Integer(0))
check("path has exactly two heavy propagators", sp.Integer(sum(1 for z in mu if z == M))-2)
print("PASS: ordered propagator masses are (M_E,0,M_E,0)")
checks += 1
check("selected chiral-coupling product is +y^2 lambda^2",
      u[0]*u[1]*v[2]*v[3] - a**2*b**2)

H = u[0]*v[1]*u[2]*v[3] + v[0]*u[1]*v[2]*u[3]
Hodd = u[0]*v[1]*u[2]*v[3] - v[0]*u[1]*v[2]*u[3]
Mterm = sp.prod(mu) * (sp.prod(u) + sp.prod(v))
check("H vanishes in this chiral limit", H)
check("parity-odd trace weight H_odd vanishes in this chiral limit", Hodd)
check("four-mass numerator term vanishes in this chiral limit", Mterm)

# Independent chirality-transition decomposition: only the light-line pair (2,4) survives.
Cij = {ij: sp.Integer(0) for ij in combinations(range(4), 2)}
for chirality in product((0, 1), repeat=4):
    transitions = tuple(i for i in range(4)
                        if chirality[i] != chirality[(i+1) % 4])
    if len(transitions) != 2:
        continue
    ij = transitions
    coupling = sp.prod(u[i] if chirality[i] == 0 else v[i] for i in range(4))
    Cij[ij] += coupling * sp.prod(mu[i] for i in range(4) if i not in ij)
check("only C_(2,4) survives and equals y^2 lambda^2 M_E^2",
      Cij[(1, 3)] - C)
check("all other C_ij vanish",
      sum(Cij[ij] for ij in Cij if ij != (1, 3)))

# Re-express the same four propagators in the fixed source routing.
k = kline[1]
check("heavy line 1 is k+p4", kline[0] - (k+p4))
check("heavy line 3 is k-p2", kline[2] - (k-p2))
check("light line 4 is k-q with q=-(p1+p4)", kline[3] - (k-q))

# Feynman-parameter denominator shift. On the simplex, sum x_i=1.
rfix = [p4, sp.zeros(4, 1), -p2, -q]
Rfix = x1*rfix[0] + x2*rfix[1] + x3*rfix[2] + x4*rfix[3]
d = sp.expand(x1*dot(p4, p4) + x3*dot(p2, p2)
              + x4*dot(q, q) - dot(Rfix, Rfix))
Delta0 = M**2 * (x1+x3)
kvar = sp.Matrix([sp.Symbol(f"k_{mu}") for mu in range(4)])
lhs = (
    x1*(dot(kvar+p4, kvar+p4)-M**2)
    + x2*dot(kvar, kvar)
    + x3*(dot(kvar-p2, kvar-p2)-M**2)
    + x4*dot(kvar-q, kvar-q)
)
rhs = dot(kvar+Rfix, kvar+Rfix) - Delta0 + d
simplex_sub = {x4: 1-x1-x2-x3}
check("Feynman denominator = K_M^2-Delta0+d on sum(x_i)=1",
      (lhs-rhs).subs(simplex_sub))
check("Delta0 = M_E^2 (x1+x3)", Delta0-M**2*(x1+x3))

# After k=K-R, the numerator is 2C[K_M^2 + f] plus an odd-in-K term.
f = sp.expand(dot(Rfix, Rfix+q))
check("f equals the shifted light-line product f_24",
      f - dot(rfix[1]-Rfix, rfix[3]-Rfix))
Kvar = sp.Matrix([sp.Symbol(f"ell_{mu}") for mu in range(4)])
shifted_numerator = 2*C*dot(Kvar-Rfix, Kvar-Rfix-q)
expected_shifted = 2*C*(dot(Kvar, Kvar) - dot(Kvar, 2*Rfix+q) + f)
check("shifted numerator separates into K^2, odd K, and f=R.(R+q)",
      shifted_numerator-expected_shifted)

# Minkowski K^2 -> -K_E^2 and denominator K_E^2+Delta0-d:
# (A-d)^-4 = A^-4 + 4 d A^-5 + O(p^4).
A, ds = sp.symbols("A d", nonzero=True)
series = sp.series((A-ds)**(-4), ds, 0, 2).removeO()
check("Euclidean denominator expansion has the +4d term",
      series - (A**(-4) + 4*ds*A**(-5)))

# In units of 1/(16 pi^2): I_0^(4)=1/(6 Delta^2), I_1^(5)=1/(12 Delta^2).
F, S, dcoef = sp.symbols("F S d", nonzero=True)
B2 = F/sp.Integer(3) - sp.Rational(2, 3)*S*dcoef
direct_kernel = 2*F/sp.Integer(6) - 8*S*dcoef/sp.Integer(12)
check("loop-integral factors give B2=F/3-2 S d/3",
      direct_kernel-B2)
check("this path gives B2=C(f-2d)/3",
      B2.subs({F:C*f, S:C, dcoef:d}) - C*(f-2*d)/3)
check("B1 and B3 vanish in this chiral limit",
      H*(-sp.Rational(2,3)*sp.Symbol("g") + 2*d) +
      sp.Rational(2,3)*Mterm*d)
check("Gamma(4)=6 cancels the simplex volume 1/6 exactly once",
      sp.gamma(4)*sp.Rational(1, 6)-1)

print(f"RESULT: {checks} exact symbolic one-cycle calibration checks passed.")
print("SCOPE: one chiral path; exact numerator, fixed denominator routing, B2 sign/factor.")
print("OPEN: common diagrammatic i/sign, physical graph multiplicity, B1/B3 signs, full six-cycle UV-EFT subtraction.")
