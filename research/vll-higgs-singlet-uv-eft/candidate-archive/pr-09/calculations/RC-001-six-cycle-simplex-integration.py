#!/usr/bin/env python3
"""Conditional analytic simplex integration for the RC-001 six-cycle B-kernel.

Builds the same six labeled cycles and 16 internal-state paths as the PR #9
candidate-kernel ledger, then integrates
    6 * integral_simplex [B1/Delta0 + B2/Delta0**2 + B3/Delta0**3]
exactly in terms of Gauss hypergeometric functions. The factor Gamma(4)=6 is
included once. The common 1/(16*pi**2), global Minkowski/Wick phase, closed
fermion-loop sign, graph/symmetry multiplicities, EFT soft subtraction, and
counterterms are intentionally not included.

This integrates the candidate kernels conditional on the current B1/B2/B3
definitions; it does not resolve the physical B1/B3 sign question or produce
a final Wilson coefficient.
Requires Python 3, SymPy, and mpmath.
"""
from itertools import combinations, permutations, product
from math import factorial, prod as math_prod
from pathlib import Path
import csv
import hashlib
import tempfile
import time
import mpmath as mp
import sympy as sp

def check(name, expr, expected=0):
    residual = sp.simplify(expr - expected)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    print(f"PASS: {name}")

start = time.time()
cL, sL, cR, sR, a, b, m1, m2 = sp.symbols(
    "c_L s_L c_R s_R a b m_1 m_2", nonzero=True
)
x1, x2, x3, x4 = sp.symbols("x_1 x_2 x_3 x_4")
xs = (x1, x2, x3, x4)
Q = sp.symbols("Q1:7")
Gp = sp.Matrix([[Q[0], Q[3], Q[4]],
                [Q[3], Q[1], Q[5]],
                [Q[4], Q[5], Q[2]]])
pvec = {
    1: sp.Matrix([[1, 0, 0]]),
    2: sp.Matrix([[0, 1, 0]]),
    3: sp.Matrix([[0, 0, 1]]),
    4: sp.Matrix([[-1, -1, -1]]),
}
label_num = {"h1": 1, "h2": 2, "s1": 3, "s2": 4}
type_of = {"h1": "h", "h2": "h", "s1": "s", "s2": "s"}
cycles = [("h1",) + tail for tail in permutations(("h2", "s1", "s2"))]
paths = list(product((0, 1), repeat=4))
Ckeys = list(combinations(range(4), 2))
Yh = a * sp.Matrix([[cL*sR, cL*cR], [sL*sR, sL*cR]])
Ys = b * sp.Matrix([[sL*cR, -sL*sR], [-cL*cR, cL*sR]])

def dotc(u, v):
    return sp.expand((u * Gp * v.T)[0])

def coeffs(expr):
    polynomial = sp.Poly(sp.expand(expr), *Q)
    return tuple(polynomial.coeff_monomial(q) for q in Q)

def g_from_f(ff):
    return tuple(sp.expand(
        ff[(0,1)][k] + ff[(2,3)][k] - ff[(0,2)][k] - ff[(1,3)][k]
        + ff[(0,3)][k] + ff[(1,2)][k]
        + sp.Rational(1,2)*(ff[(0,2)][k] + ff[(1,3)][k])
    ) for k in range(6))

def weights(cycle, path):
    seq = tuple(Yh if type_of[label] == "h" else Ys for label in cycle)
    nxt = path[1:] + path[:1]
    uu = [seq[i][path[i], nxt[i]] for i in range(4)]
    vv = [seq[i][nxt[i], path[i]] for i in range(4)]
    masses = tuple(m1 if nxt[i] == 0 else m2 for i in range(4))
    H = sp.expand(uu[0]*vv[1]*uu[2]*vv[3] + vv[0]*uu[1]*vv[2]*uu[3])
    M = sp.expand(math_prod(masses) * (math_prod(uu) + math_prod(vv)))
    C = {ij: sp.Integer(0) for ij in Ckeys}
    for chirality in product((0, 1), repeat=4):
        transitions = tuple(i for i in range(4)
                            if chirality[i] != chirality[(i+1) % 4])
        if len(transitions) != 2:
            continue
        ij = transitions
        coupling = math_prod(
            uu[i] if chirality[i] == 0 else vv[i] for i in range(4)
        )
        C[ij] += coupling * math_prod(
            masses[i] for i in range(4) if i not in ij
        )
    return H, M, {ij: sp.expand(value) for ij, value in C.items()}, masses

def simplex_moment(exponents, mass_tags, n):
    """Integral_simplex prod(x_i**a_i) / (sum_i x_i m_i**2)**n."""
    total_degree = sum(exponents)
    n_m1 = sum(tag == "m1" for tag in mass_tags)
    degree_m1 = sum(power for power, tag in zip(exponents, mass_tags)
                    if tag == "m1")
    monomial_factor = sp.Rational(
        math_prod(factorial(power) for power in exponents),
        factorial(total_degree + 3),
    )
    if n_m1 == 0:
        return monomial_factor / m2**(2*n)
    if n_m1 == 4:
        return monomial_factor / m1**(2*n)
    # Grouping the simplex by z=sum_{m_i=m1} x_i reduces the integral to
    # a Beta-weighted one-dimensional integral and a Gauss 2F1 function.
    return monomial_factor * m2**(-2*n) * sp.hyper(
        [sp.Integer(n), sp.Integer(degree_m1 + n_m1)],
        [sp.Integer(total_degree + 4)],
        -(m1**2 - m2**2) / m2**2,
    )

def integrate_poly_over_delta(expr, mass_tags, n):
    polynomial = sp.Poly(sp.expand(expr), *xs)
    total = sp.Integer(0)
    for exponents, coefficient in polynomial.terms():
        total += coefficient * simplex_moment(exponents, mass_tags, n)
    return total

# Exact equal-mass limit and simplex normalization checks.
Mtest = sp.symbols("Mtest", nonzero=True)
equal_mass_checks = 0
test_exponents = [(0,0,0,0), (1,0,0,0), (1,1,0,0), (2,0,0,0)]
test_tags = [
    ("m1","m2","m2","m2"),
    ("m1","m1","m2","m2"),
    ("m1","m1","m1","m2"),
    ("m1","m1","m1","m1"),
]
for exponents in test_exponents:
    degree = sum(exponents)
    numerator_factor = sp.Rational(
        math_prod(factorial(power) for power in exponents),
        factorial(degree + 3),
    )
    for tags in test_tags:
        for n in (1, 2, 3):
            value = simplex_moment(exponents, tags, n).subs({m1: Mtest, m2: Mtest})
            expected = numerator_factor / Mtest**(2*n)
            check(f"equal-mass simplex moment {equal_mass_checks+1}", value, expected)
            equal_mass_checks += 1

# Four non-degenerate moments checked against direct one-dimensional quadrature.
def direct_moment(exponents, tags, n, m1_value=2.0, m2_value=3.0):
    degree = sum(exponents)
    n_m1 = sum(tag == "m1" for tag in tags)
    degree_m1 = sum(power for power, tag in zip(exponents, tags) if tag == "m1")
    factor = math_prod(factorial(power) for power in exponents) / factorial(degree + 3)
    if n_m1 == 0:
        return factor / (m2_value**2)**n
    if n_m1 == 4:
        return factor / (m1_value**2)**n
    alpha = degree_m1 + n_m1
    beta = degree - degree_m1 + 4 - n_m1
    integrand = lambda z: z**(alpha-1) * (1-z)**(beta-1) / (
        m2_value**2 + (m1_value**2-m2_value**2)*z
    )**n
    return factor * float(mp.quad(integrand, [0, 1]) / mp.beta(alpha, beta))

quadrature_cases = [
    ((0,0,0,0), ("m1","m2","m2","m2"), 1),
    ((1,0,0,0), ("m1","m1","m2","m2"), 2),
    ((0,1,1,0), ("m1","m2","m1","m2"), 3),
    ((2,0,0,0), ("m1","m2","m2","m2"), 1),
]
for i, (exponents, tags, n) in enumerate(quadrature_cases, 1):
    symbolic = float(sp.N(simplex_moment(exponents, tags, n).subs({m1:2, m2:3}), 30))
    direct = direct_moment(exponents, tags, n)
    if abs(symbolic-direct) > 2e-13 * max(1.0, abs(direct)):
        raise AssertionError(f"quadrature moment {i}: symbolic={symbolic}, direct={direct}")
    print(f"PASS: non-degenerate simplex moment vs direct quadrature {i}")

# Build all six labeled-cycle x 16 path x 6-invariant candidate kernels.
geometry = {}
for cycle in cycles:
    qvs = [pvec[label_num[label]] for label in cycle[:3]]
    route = [sp.zeros(1,3), -qvs[1], -qvs[1]-qvs[2], qvs[0]]
    R = sum((xs[i]*route[i] for i in range(4)), sp.zeros(1,3))
    shifted = [ri-R for ri in route]
    ff = {ij: coeffs(dotc(shifted[ij[0]], shifted[ij[1]])) for ij in Ckeys}
    gg = g_from_f(ff)
    dd = coeffs(sp.expand(
        sum(xs[i]*dotc(route[i], route[i]) for i in range(4)) - dotc(R, R)
    ))
    geometry[cycle] = (ff, gg, dd)

rows = []
kernel_map = {}
kernel_polynomials = {}
for cycle in cycles:
    ff, gg, dd = geometry[cycle]
    for path in paths:
        H, M, C, masses = weights(cycle, path)
        S = sp.expand(sum(C.values()))
        mass_tags = tuple("m1" if mass == m1 else "m2" for mass in masses)
        for alpha in range(6):
            F = sp.expand(sum(C[ij]*ff[ij][alpha] for ij in Ckeys))
            B1 = sp.expand(H*(-sp.Rational(2,3)*gg[alpha] + 2*dd[alpha]))
            B2 = sp.expand(sp.Rational(1,3)*F - sp.Rational(2,3)*S*dd[alpha])
            B3 = sp.expand(sp.Rational(2,3)*M*dd[alpha])
            kernel_polynomials[(cycle, path, alpha)] = (B1, B2, B3, mass_tags)
            I1 = integrate_poly_over_delta(B1, mass_tags, 1)
            I2 = integrate_poly_over_delta(B2, mass_tags, 2)
            I3 = integrate_poly_over_delta(B3, mass_tags, 3)
            # Gamma(4)=6 appears once. Common loop/sign factors remain separate.
            integrated = 6*(I1+I2+I3)
            kernel_map[(cycle, path, alpha)] = integrated
            rows.append({
                "cycle": "-".join(cycle),
                "path": "".join(str(z+1) for z in path),
                "alpha": alpha+1,
                "invariant": str(Q[alpha]),
                "mass_tags": "/".join(mass_tags),
                "n_m1": mass_tags.count("m1"),
                "B1_simplex_integral": str(I1),
                "B2_simplex_integral": str(I2),
                "B3_simplex_integral": str(I3),
                "Gamma4_times_integrated_candidate_kernel": str(integrated),
            })

if len(rows) != 576:
    raise AssertionError(f"expected 576 rows, got {len(rows)}")
print("PASS: analytically integrated all 576 conditional kernels (6 cycles x 16 paths x 6 invariants).")

# Numeric reverse-cycle comparison after the exact path/cycle map. Evaluate the
# polynomial moments directly with cached mpmath 2F1 values; this is equivalent
# to evaluating the expanded symbolic hypergeometric expressions, but avoids
# repeatedly re-parsing and numerically simplifying the same special functions.
numeric_subs = {
    cL: sp.Rational(3,5), sL: sp.Rational(4,5),
    cR: sp.Rational(5,13), sR: sp.Rational(12,13),
    a: sp.Rational(2,3), b: sp.Rational(5,7),
    m1: sp.Integer(2), m2: sp.Integer(3),
}
mp.mp.dps = 40
moment_cache = {}
def numeric_simplex_moment(exponents, mass_tags, n):
    key = (tuple(exponents), tuple(mass_tags), n)
    if key in moment_cache:
        return moment_cache[key]
    degree = sum(exponents)
    n_m1 = sum(tag == "m1" for tag in mass_tags)
    degree_m1 = sum(power for power, tag in zip(exponents, mass_tags) if tag == "m1")
    factor = mp.mpf(math_prod(factorial(power) for power in exponents)) / factorial(degree + 3)
    if n_m1 == 0:
        value = factor / mp.mpf(3)**(2*n)
    elif n_m1 == 4:
        value = factor / mp.mpf(2)**(2*n)
    else:
        alpha = degree_m1 + n_m1
        z = 1 - mp.mpf(2)**2 / mp.mpf(3)**2
        value = factor * mp.mpf(3)**(-2*n) * mp.hyp2f1(n, alpha, degree+4, z)
    moment_cache[key] = value
    return value

def numeric_poly_integral(expr, mass_tags, n):
    polynomial = sp.Poly(sp.expand(expr), *xs)
    total = mp.mpf("0")
    for exponents, coefficient in polynomial.terms():
        coeff_num = mp.mpf(str(sp.N(coefficient.subs(numeric_subs), 40)))
        total += coeff_num * numeric_simplex_moment(exponents, mass_tags, n)
    return total

def numeric_integrated_kernel(key):
    B1, B2, B3, mass_tags = kernel_polynomials[key]
    return 6 * (numeric_poly_integral(B1, mass_tags, 1)
                + numeric_poly_integral(B2, mass_tags, 2)
                + numeric_poly_integral(B3, mass_tags, 3))

reverse_pairs = []
for cycle in cycles:
    reverse = (cycle[0], cycle[3], cycle[2], cycle[1])
    if cycles.index(cycle) > cycles.index(reverse):
        continue
    reverse_pairs.append((cycle, reverse))
reverse_checks = 0
max_reverse_difference = mp.mpf("0")
for cycle, reverse in reverse_pairs:
    for path in paths:
        reverse_path = (path[1], path[0], path[3], path[2])
        for alpha in range(6):
            left = numeric_integrated_kernel((cycle, path, alpha))
            right = numeric_integrated_kernel((reverse, reverse_path, alpha))
            difference = abs(left-right)
            scale = max(mp.mpf(1), abs(left), abs(right))
            if difference > mp.mpf("1e-25")*scale:
                raise AssertionError(
                    f"integrated reverse-cycle mismatch: {cycle}, {path}, {reverse_path}, {alpha}, {difference}"
                )
            max_reverse_difference = max(max_reverse_difference, difference)
            reverse_checks += 1
if reverse_checks != 288:
    raise AssertionError(f"expected 288 reverse checks, got {reverse_checks}")
print(f"PASS: integrated reverse-cycle numerical checks {reverse_checks}/{reverse_checks}; max abs difference={mp.nstr(max_reverse_difference, 6)}")
print(f"PASS: cached {len(moment_cache)} distinct numerical simplex moments for the reverse-cycle checks.")

outdir = Path(__import__("os").environ.get("RC001_OUTPUT_DIR", tempfile.gettempdir()))
outdir.mkdir(parents=True, exist_ok=True)
out = outdir / "RC-001-six-cycle-integrated-candidate-kernel-ledger.csv"
with out.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)
digest = hashlib.sha256(out.read_bytes()).hexdigest()
print(f"CSV: {out} ({out.stat().st_size} bytes)")
print(f"SHA256: {digest}")
print(f"ELAPSED_SECONDS: {time.time()-start:.2f}")
print("LIMIT: conditional B-kernel simplex integration only; no global i/sign/symmetry factor, no complete EFT soft/counterterm subtraction, and no final Wilson coefficient.")
