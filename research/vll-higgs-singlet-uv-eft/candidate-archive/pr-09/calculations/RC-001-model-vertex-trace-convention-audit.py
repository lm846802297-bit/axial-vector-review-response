#!/usr/bin/env python3
"""RC-001 model-vertex trace and signed/positive-mass convention audit.

Uses the exact mass-basis vertices G_h,G_s in the frozen v153 source and
compares them to the Eq. (13) positive-light-mass matrices Y_h,Y_s. It checks
the pathwise chiral-trace weights for all 6 labeled cycles x 16 internal paths,
then evaluates one explicit direct 4x4 trace with nonzero H_odd and nonzero
epsilon determinant and compares it with the complete decomposition.

Metric: (+---). The audit is algebraic and does not determine the common
diagrammatic i/sign, graph multiplicity, or the final UV-EFT coefficient.
Requires Python 3 and SymPy.
"""
from itertools import combinations, permutations, product
import sympy as sp

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

cL, sL, cR, sR, a, b, m1, m2 = sp.symbols(
    "c_L s_L c_R s_R a b m_1 m_2"
)
# Here a=y_l/sqrt(2), b=lambda_l/sqrt(2).
Yh = a * sp.Matrix([[cL*sR, cL*cR], [sL*sR, sL*cR]])
Ys = b * sp.Matrix([[sL*cR, -sL*sR], [-cL*cR, cL*sR]])
D = sp.diag(-1, 1)
Gh, Gs = Yh*D, Ys*D

checks = 0
def check(name, expr, expected=0):
    global checks
    residual = sp.simplify(expr - expected)
    if isinstance(residual, sp.MatrixBase):
        ok = residual == sp.zeros(*residual.shape)
    else:
        ok = residual == 0
    if not ok:
        raise AssertionError(f"{name}: residual={residual}")
    checks += 1

check("G_h=Y_h D", Gh, Yh*D)
check("G_s=Y_s D", Gs, Ys*D)

def trace_weights(seq, path, signed_mass):
    nxt = path[1:] + path[:1]
    u = [seq[i][path[i], nxt[i]] for i in range(4)]
    v = [seq[i][nxt[i], path[i]] for i in range(4)]
    mass_map = {0: (-m1 if signed_mass else m1), 1: m2}
    masses = [mass_map[nxt[i]] for i in range(4)]
    H = sp.expand(u[0]*v[1]*u[2]*v[3] + v[0]*u[1]*v[2]*u[3])
    Hodd = sp.expand(u[0]*v[1]*u[2]*v[3] - v[0]*u[1]*v[2]*u[3])
    M = sp.expand(sp.prod(masses) * (sp.prod(u) + sp.prod(v)))
    C = {ij: sp.Integer(0) for ij in combinations(range(4), 2)}
    for chirality in product((0, 1), repeat=4):
        transitions = tuple(i for i in range(4)
                            if chirality[i] != chirality[(i+1) % 4])
        if len(transitions) != 2:
            continue
        ij = transitions
        coupling = sp.prod(
            u[i] if chirality[i] == 0 else v[i] for i in range(4)
        )
        C[ij] += coupling * sp.prod(
            masses[i] for i in range(4) if i not in ij
        )
    return H, Hodd, M, C

cycles = [("h1",)+tail for tail in permutations(("h2", "s1", "s2"))]
weight_checks = 0
for cycle in cycles:
    seqY = tuple(Yh if label[0] == "h" else Ys for label in cycle)
    seqG = tuple(Gh if label[0] == "h" else Gs for label in cycle)
    for path in product((0, 1), repeat=4):
        positive = trace_weights(seqY, path, signed_mass=False)
        signed = trace_weights(seqG, path, signed_mass=True)
        comparisons = [
            (positive[0], signed[0]),       # H
            (positive[1], signed[1]),       # H_odd
            (positive[2], signed[2]),       # four-mass term M
        ]
        comparisons.extend(
            (positive[3][ij], signed[3][ij])
            for ij in combinations(range(4), 2)
        )
        for index, (lhs, rhs) in enumerate(comparisons):
            check(f"rephasing weight {cycle}/{path}/{index}", lhs, rhs)
            weight_checks += 1

# One direct trace where H_odd and det(k_1,k_2,k_3,k_4) are both nonzero.
params = {
    cL: sp.Rational(3, 5), sL: sp.Rational(4, 5),
    cR: sp.Rational(5, 13), sR: sp.Rational(12, 13),
    a: sp.Rational(2, 3), b: sp.Rational(5, 7),
    m1: sp.Integer(2), m2: sp.Integer(3),
}
cycle = ("h1", "h2", "s1", "s2")
path = (0, 0, 1, 1)
nxt = path[1:] + path[:1]
Yhn, Ysn = Yh.subs(params), Ys.subs(params)
Ghn, Gsn = Yhn*D, Ysn*D
seqY, seqG = (Yhn, Yhn, Ysn, Ysn), (Ghn, Ghn, Gsn, Gsn)
momenta = [sp.Matrix(v) for v in (
    (1, 2, 3, 4), (2, 0, 1, -1), (0, 1, 4, 2), (3, 5, -2, 1)
)]

def slash(v):
    return gamma[0]*v[0] - gamma[1]*v[1] - gamma[2]*v[2] - gamma[3]*v[3]

def dot4(u, v):
    return sp.expand(u[0]*v[0] - u[1]*v[1] - u[2]*v[2] - u[3]*v[3])

def direct_trace(seq, signed_mass):
    mass_map = {
        0: (-params[m1] if signed_mass else params[m1]),
        1: params[m2],
    }
    trace = sp.eye(4)
    for i in range(4):
        u = seq[i][path[i], nxt[i]]
        v = seq[i][nxt[i], path[i]]
        trace = trace * (u*PR + v*PL) * (
            slash(momenta[i]) + mass_map[nxt[i]]*sp.eye(4)
        )
    return sp.simplify(sp.trace(trace))

trace_positive = direct_trace(seqY, signed_mass=False)
trace_signed = direct_trace(seqG, signed_mass=True)
check("direct trace invariant under signed/positive mass convention",
      trace_signed, trace_positive)

weights = trace_weights(seqG, path, signed_mass=True)
H, Hodd, M, C = weights
H, Hodd, M = (sp.simplify(z.subs(params)) for z in (H, Hodd, M))
C = {ij: sp.simplify(value.subs(params)) for ij, value in C.items()}
gram4 = (
    dot4(momenta[0], momenta[1])*dot4(momenta[2], momenta[3])
    - dot4(momenta[0], momenta[2])*dot4(momenta[1], momenta[3])
    + dot4(momenta[0], momenta[3])*dot4(momenta[1], momenta[2])
)
epsilon = sp.det(sp.Matrix.hstack(*momenta))
decomposition = sp.simplify(
    2*H*gram4
    + 2*sum(C[ij]*dot4(momenta[ij[0]], momenta[ij[1]]) for ij in C)
    + 2*M + 2*I*epsilon*Hodd
)
check("direct model trace equals full chiral decomposition incl. parity-odd term",
      trace_signed, decomposition)
if Hodd == 0 or epsilon == 0:
    raise AssertionError("the parity-odd benchmark must have H_odd != 0 and epsilon != 0")

print(f"PASS: exact G_h/G_s rephasing identities and {weight_checks}/{weight_checks} path-weight comparisons.")
print("PASS: direct trace is invariant between signed-mass G vertices and positive-mass Y vertices.")
print("PASS: direct trace equals 2 H G + 2 sum(C_ij k_i.k_j) + 2 M + 2 i epsilon H_odd.")
print(f"PARITY-ODD BENCHMARK: H_odd={Hodd}; det(k_i)={epsilon}.")
print(f"RESULT: {checks} exact symbolic/numeric-rational checks passed.")
print("SCOPE: model-vertex trace and convention mapping only; no global diagram factor or final Wilson coefficient.")
