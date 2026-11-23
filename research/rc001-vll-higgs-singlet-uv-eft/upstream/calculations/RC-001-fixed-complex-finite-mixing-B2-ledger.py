#!/usr/bin/env python3
"""Finite-mixing fixed-complex-orientation B2 kernel ledger for RC-001.

Unlike the real-scalar six-cycle ledger, this script keeps the complex external
orientation fixed: H,S,Sdag,Hdag for mu and H,Sdag,S,Hdag for tau. It uses the
positive-light-mass Eq. (13) mass-basis matrices and the fixed chiral projectors
(PR,PR,PL,PL). The exact trace has only the C_13 mass-numerator structure, so
only the B2-type O(p^2) kernel is generated.

For each flavor, all 16 internal mass-eigenstate paths are retained. Each
path-dependent O(p^2) coefficient is analytically integrated in d=4 over the
four-parameter simplex using the Beta-weighted Gauss-hypergeometric moment
formula. Gamma(4)=6 is included exactly once.

This is a finite-mass conditional kernel ledger, not a dimensionally regulated
hard-region expansion: the m_light -> 0 limit must not be taken before the
EFT soft subtraction/regions analysis. The common diagrammatic i/sign,
determinant-log multiplicity, and final UV-EFT coefficient remain outside this
script. Real Yukawa couplings are assumed for this convention audit.
Requires Python 3, SymPy, and mpmath.
"""
from itertools import product
from pathlib import Path
import csv
import hashlib
import os
import tempfile
import time
import mpmath as mp
import sympy as sp

start = time.time()
cL, sL, cR, sR, y, lam, m1, m2 = sp.symbols(
    "c_L s_L c_R s_R y lambda m_1 m_2", nonzero=True, real=True
)
x1, x2, x3, x4 = sp.symbols("x_1 x_2 x_3 x_4")
xs = (x1, x2, x3, x4)
Q = sp.symbols("Q1:7")
Q1, Q2, Q3, Q4, Q5, Q6 = Q
Gram = sp.Matrix([
    [Q1, Q4, Q5],
    [Q4, Q2, Q6],
    [Q5, Q6, Q3],
])
pvec = {
    "H": sp.Matrix([[1, 0, 0]]),
    "S": sp.Matrix([[0, 1, 0]]),
    "Sdag": sp.Matrix([[0, 0, 1]]),
    "Hdag": sp.Matrix([[-1, -1, -1]]),
}
Yh = y * sp.Matrix([
    [cL*sR, cL*cR],
    [sL*sR, sL*cR],
])
Ys = lam * sp.Matrix([
    [sL*cR, -sL*sR],
    [-cL*cR, cL*sR],
])
mass_map = {0: m1, 1: m2}
vertices = {
    "mu": {
        "H": Yh, "Hdag": Yh.T,
        "S": Ys, "Sdag": Ys.T,
    },
    "tau": {
        "H": Yh, "Hdag": Yh.T,
        "S": Ys.T, "Sdag": Ys,
    },
}
cycles = {
    "mu": ("H", "S", "Sdag", "Hdag"),
    "tau": ("H", "Sdag", "S", "Hdag"),
}

def dotc(u, v):
    return sp.expand((u * Gram * v.T)[0])

def coeffs(expr):
    polynomial = sp.Poly(sp.expand(expr), *Q)
    return tuple(sp.expand(polynomial.coeff_monomial(q)) for q in Q)

def simplex_moment(exponents, mass_tags, n):
    """Integral_simplex prod(x_i**a_i)/(sum_i x_i m_i**2)**n."""
    degree = sum(exponents)
    n_m1 = sum(tag == "m1" for tag in mass_tags)
    degree_m1 = sum(power for power, tag in zip(exponents, mass_tags)
                    if tag == "m1")
    monomial_factor = sp.Rational(
        sp.prod(sp.factorial(power) for power in exponents),
        sp.factorial(degree + 3),
    )
    if n_m1 == 0:
        return monomial_factor / m2**(2*n)
    if n_m1 == 4:
        return monomial_factor / m1**(2*n)
    return monomial_factor * m2**(-2*n) * sp.hyper(
        [sp.Integer(n), sp.Integer(degree_m1 + n_m1)],
        [sp.Integer(degree + 4)],
        -(m1**2 - m2**2) / m2**2,
    )

def integrate_poly_over_delta(expr, mass_tags, n):
    polynomial = sp.Poly(sp.expand(expr), *xs)
    total = sp.Integer(0)
    for exponents, coefficient in polynomial.terms():
        total += coefficient * simplex_moment(exponents, mass_tags, n)
    return total

# The denominator-shift and angular-average formula for the fixed chiral trace
# is B2 = C_13 (f_13/3 - 2 d/3)/Delta0^2, in units of 1/(16 pi^2).
def path_geometry(cycle):
    qv = [pvec[label] for label in cycle]
    route = [
        sp.zeros(1, 3),
        -qv[1],
        -qv[1]-qv[2],
        qv[0],
    ]
    R = sum((xs[i]*route[i] for i in range(4)), sp.zeros(1, 3))
    shifted = [ri-R for ri in route]
    f13 = dotc(shifted[1], shifted[3])
    d = sp.expand(
        sum(xs[i]*dotc(route[i], route[i]) for i in range(4))
        - dotc(R, R)
    )
    return coeffs(f13), coeffs(d)

# Exact normalization and equal-mass moment checks.
def check(name, expr, expected=0):
    residual = sp.simplify(expr - expected)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    print(f"PASS: {name}")

Mtest = sp.symbols("Mtest", nonzero=True)
check("four-parameter simplex volume is 1/6",
      sp.Rational(1, sp.factorial(3)), sp.Rational(1, 6))
check("Gamma(4) times simplex volume is exactly one",
      sp.gamma(4)*sp.Rational(1, 6), 1)
check("equal-mass zero-monomial moment for n=2",
      simplex_moment((0,0,0,0), ("m1","m2","m1","m2"), 2)
      .subs({m1:Mtest,m2:Mtest}), 1/(6*Mtest**4))

# In the zero-mixing limit, the fixed complex orientation must select only
# path (0,1,0,1), with coupling product y^2 lambda^2.
zero_mix = {cL:1, sL:0, cR:1, sR:0}
for flavor in ("mu", "tau"):
    cycle = cycles[flavor]
    V = vertices[flavor]
    surviving = []
    for path in product((0,1), repeat=4):
        nxt = path[1:] + path[:1]
        coupling = sp.prod(V[cycle[i]][path[i],nxt[i]] for i in range(4))
        if sp.simplify(coupling.subs(zero_mix)) != 0:
            surviving.append((path, sp.simplify(coupling.subs(zero_mix))))
    if surviving != [((0,1,0,1), y**2*lam**2)]:
        raise AssertionError(f"{flavor} zero-mixing paths mismatch: {surviving}")
    print(f"PASS: {flavor} zero-mixing limit leaves only path 0101 with y^2 lambda^2.")

geometry = {flavor: path_geometry(cycle) for flavor,cycle in cycles.items()}
rows = []
integrated_totals = {flavor: [sp.Integer(0) for _ in Q] for flavor in ("mu", "tau")}
for flavor in ("mu", "tau"):
    cycle = cycles[flavor]
    fcoeff, dcoeff = geometry[flavor]
    V = vertices[flavor]
    for path in product((0,1), repeat=4):
        nxt = path[1:] + path[:1]
        couplings = [V[cycle[i]][path[i],nxt[i]] for i in range(4)]
        coupling_product = sp.factor(sp.prod(couplings))
        line_masses = tuple(mass_map[nxt[i]] for i in range(4))
        # Fixed PR,PR,PL,PL trace: masses are required on lines 1 and 3
        # (zero-based lines 0 and 2); the slashed momenta are lines 2 and 4.
        C13 = sp.factor(coupling_product * line_masses[0] * line_masses[2])
        mass_tags = tuple("m1" if mass == m1 else "m2" for mass in line_masses)
        for alpha, invariant in enumerate(Q):
            If = integrate_poly_over_delta(fcoeff[alpha], mass_tags, 2)
            Id = integrate_poly_over_delta(dcoeff[alpha], mass_tags, 2)
            # Feynman-parameter prefactor Gamma(4)=6 appears once here.
            integrated = sp.factor(
                6*C13*(If/sp.Integer(3)-sp.Rational(2,3)*Id)
            )
            integrated_totals[flavor][alpha] += integrated
            rows.append({
                "flavor": flavor,
                "cycle": "-".join(cycle),
                "path": "".join(str(state+1) for state in path),
                "line_mass_tags": "/".join(mass_tags),
                "coupling_product": str(coupling_product),
                "C13_mass_weight": str(C13),
                "invariant": str(invariant),
                "f13_coefficient": str(fcoeff[alpha]),
                "d_coefficient": str(dcoeff[alpha]),
                "Gamma4_integrated_B2_kernel": str(integrated),
            })

if len(rows) != 192:
    raise AssertionError(f"expected 192 rows (2 flavors x 16 paths x 6 invariants), got {len(rows)}")
# A physical rational point satisfying the triangular M11=0 constraint.
benchmark = {
    cL: sp.Rational(12,13), sL: sp.Rational(5,13),
    cR: sp.Rational(12,13), sR: sp.Rational(5,13),
    m1: sp.Integer(1), m2: sp.Rational(144,25),
    y: sp.Rational(2,7), lam: sp.Rational(3,11),
}
m11_constraint = sp.simplify(
    -benchmark[cL]*benchmark[cR]*benchmark[m1]
    + benchmark[m2]*benchmark[sL]*benchmark[sR]
)
check("rational finite-mixing benchmark satisfies M11=0", m11_constraint, 0)
numeric_totals = {
    flavor: [sp.N(expr.subs(benchmark), 35) for expr in integrated_totals[flavor]]
    for flavor in ("mu", "tau")
}
# Exchanging S <-> Sdag swaps Q2<->Q3 and Q4<->Q5, while Q1 and Q6 stay fixed.
swap_pairs = ((0,0),(1,2),(2,1),(3,4),(4,3),(5,5))
max_flavor_swap_difference = 0.0
for mu_alpha, tau_alpha in swap_pairs:
    difference = sp.N(numeric_totals["mu"][mu_alpha] - numeric_totals["tau"][tau_alpha], 30)
    magnitude = abs(float(difference))
    max_flavor_swap_difference = max(max_flavor_swap_difference, magnitude)
    if magnitude > 1e-20:
        raise AssertionError(
            f"finite-mixing mu/tau orientation swap failed at Q{mu_alpha+1}/Q{tau_alpha+1}: {difference}"
        )
print("PASS: finite-mixing mu/tau integrated sums obey the S<->Sdag invariant permutation at the exact rational benchmark.")
print(f"MAX_FLAVOR_SWAP_ABS_DIFFERENCE: {max_flavor_swap_difference:.3e}")

print("PASS: generated all 192 fixed-complex-orientation path/invariant rows.")
print("SCOPE: d=4 finite-mass simplex integrals of the B2-type kernel; no B1/B3 terms in the fixed chiral sequence.")

outdir = Path(os.environ.get("RC001_OUTPUT_DIR", tempfile.gettempdir()))
outdir.mkdir(parents=True, exist_ok=True)
out = outdir / "RC-001-fixed-complex-finite-mixing-B2-ledger.csv"
with out.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)
digest = hashlib.sha256(out.read_bytes()).hexdigest()
print(f"CSV: {out} ({out.stat().st_size} bytes)")
print(f"SHA256: {digest}")
print(f"ELAPSED_SECONDS: {time.time()-start:.2f}")
print("LIMIT: finite-mass d=4 integrals cannot be identified with the hard Wilson coefficient by taking m1->0; first perform the d=4-2epsilon hard/soft expansion and subtract the EFT soft graph/counterterm in the same scheme.")
