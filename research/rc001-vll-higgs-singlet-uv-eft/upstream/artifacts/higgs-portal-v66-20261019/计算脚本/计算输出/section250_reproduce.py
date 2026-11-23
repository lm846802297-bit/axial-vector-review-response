"""Section 250: exact polynomial checks, Python 3 standard library only.

No diagram generator, CAS package, FeynArts, or FeynCalc is invoked.
All polynomial coefficients use fractions.Fraction.
"""
from fractions import Fraction as F
from math import factorial
import hashlib
import sys


class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.t = dict(value.t)
        elif isinstance(value, str):
            self.t = {((value, 1),): F(1)}
        elif isinstance(value, dict):
            self.t = {m: F(c) for m, c in value.items() if c}
        else:
            self.t = {(): F(value)} if value else {}

    def __add__(self, other):
        out = dict(self.t)
        for m, c in P(other).t.items():
            out[m] = out.get(m, F(0)) + c
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({m: -c for m, c in self.t.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        out = {}
        for m, c in self.t.items():
            for n, d in P(other).t.items():
                powers = dict(m)
                for v, e in n:
                    powers[v] = powers.get(v, 0) + e
                key = tuple(sorted(powers.items()))
                out[key] = out.get(key, F(0)) + c * d
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = P(1)
        for _ in range(n):
            result *= self
        return result

    def coeff(self, variable, power):
        out = {}
        for m, c in self.t.items():
            powers = dict(m)
            if powers.get(variable, 0) == power:
                powers.pop(variable, None)
                key = tuple(sorted(powers.items()))
                out[key] = out.get(key, F(0)) + c
        return P(out)

    def derivative(self, variable):
        out = {}
        for m, c in self.t.items():
            powers = dict(m)
            e = powers.get(variable, 0)
            if e:
                if e == 1:
                    del powers[variable]
                else:
                    powers[variable] = e - 1
                key = tuple(sorted(powers.items()))
                out[key] = out.get(key, F(0)) + c * e
        return P(out)

    def subs(self, variable, value):
        result = P(0)
        for m, c in self.t.items():
            term = P(c)
            for v, e in m:
                term *= (P(value) if v == variable else P(v)) ** e
            result += term
        return result

    def __str__(self):
        if not self.t:
            return "0"
        return " + ".join(str(c) + ("*" + "*".join(v if e == 1 else f"{v}^{e}" for v, e in m) if m else "")
                          for m, c in sorted(self.t.items()))


count = 0


def check(name, actual, expected=0):
    global count
    delta = P(actual) - P(expected)
    if delta.t:
        raise AssertionError(f"{name}: residual {delta}")
    count += 1
    print(f"PASS {count:02d} {name}")


print("Python:", sys.version.split()[0])
print("Arithmetic: fractions.Fraction sparse multivariate polynomials")
Delta, L, z = map(P, ["Delta", "L", "z"])

# Integrate x^n/n after extracting the massive parameter endpoint.
for n in range(1, 7):
    beta_moment = F(factorial(n) * factorial(0), factorial(n + 1)) / n
    check(f"B0 parameter moment n={n}", beta_moment, F(1, n * (n + 1)))

B = Delta - L + 1 + sum((F(1, n * (n + 1)) * z**n for n in range(1, 7)), P())
kernel = Delta - L + 1 + (1 - z) * B
check("PV constant / M2", kernel.coeff("z", 0), 2 * (Delta - L + 1))
check("PV p2", kernel.coeff("z", 1), -Delta + L - F(1, 2))
check("PV p4 / M2", kernel.coeff("z", 2), -F(1, 3))
check("self-energy constant / (h M2)", (-kernel).coeff("z", 0), -2 * (Delta - L + 1))
check("self-energy p2 / h", (-kernel).coeff("z", 1), Delta - L + F(1, 2))
check("self-energy p4 M2 / h", (-kernel).coeff("z", 2), F(1, 3))
check("counterterm removes pole", (-kernel + 2 * Delta - Delta * z).coeff("Delta", 1))

# All 16 trace components in a Weyl basis. Entries are Gaussian dyadic
# rationals, represented exactly here by Python complex numbers (0, 1, i, 1/2).
def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def tr(a):
    return sum(a[i][i] for i in range(4))


def block_gamma(sigma, time=False):
    out = [[0j] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            out[i][j + 2] = sigma[i][j]
            out[i + 2][j] = sigma[i][j] * (1 if time else -1)
    return out


g = [block_gamma([[1, 0], [0, 1]], True),
     block_gamma([[0, 1], [1, 0]]),
     block_gamma([[0, -1j], [1j, 0]]),
     block_gamma([[1, 0], [0, -1]])]
PL = [[int(i == j and i < 2) for j in range(4)] for i in range(4)]
PR = [[int(i == j and i >= 2) for j in range(4)] for i in range(4)]
trace_ok = True
for i in range(4):
    for j in range(4):
        expected = (2 if i == 0 else -2) if i == j else 0
        trace_ok &= tr(mm(mm(mm(PR, g[i]), PL), g[j])) == expected
        trace_ok &= tr(mm(mm(mm(PL, g[i]), PR), g[j])) == expected
for i in range(4):
    trace_ok &= tr(mm(mm(PR, g[i]), PL)) == 0
    trace_ok &= tr(mm(mm(PL, g[i]), PR)) == 0
check("all chiral trace components and mass terms", int(trace_ok), 1)
check("closed-loop * two vertices * two propagators", F((-1) * (-1) * (-1)), -1)

X, Y, mh, ms, lh, ls, lp, rH, rS = map(P, ["X", "Y", "muH2", "muS2", "lambdaH", "lambdaS", "lambdaP", "rH", "rS"])
fH, fS = -mh + 2 * lh * X + lp * Y, -ms + 2 * ls * Y + lp * X
pot = rH * X * fH**2 + rS * Y * fS**2
rows = {
    (1, 0): rH * mh**2,
    (0, 1): rS * ms**2,
    (2, 0): -4 * rH * mh * lh,
    (0, 2): -4 * rS * ms * ls,
    (1, 1): -2 * lp * (rH * mh + rS * ms),
    (3, 0): 4 * rH * lh**2,
    (0, 3): 4 * rS * ls**2,
    (2, 1): 4 * rH * lh * lp + rS * lp**2,
    (1, 2): rH * lp**2 + 4 * rS * ls * lp,
}
rebuilt = P()
for (nx, ny), value in rows.items():
    check(f"HD EOM scalar monomial X^{nx} Y^{ny}", pot.coeff("X", nx).coeff("Y", ny), value)
    rebuilt += value * X**nx * Y**ny
check("HD EOM entire scalar polynomial", pot, rebuilt)
FH, FS, NH, NS = map(P, ["FH", "FS", "JHdagJH", "JSdagJS"])
sources = rH * (fH * FH + NH) + rS * (fS * FS + NS)
check("H source constant", sources.coeff("FH", 1).coeff("X", 0).coeff("Y", 0), -rH * mh)
check("H source X", sources.coeff("FH", 1).coeff("X", 1), 2 * rH * lh)
check("H source Y", sources.coeff("FH", 1).coeff("Y", 1), rH * lp)
check("S source constant", sources.coeff("FS", 1).coeff("X", 0).coeff("Y", 0), -rS * ms)
check("S source X", sources.coeff("FS", 1).coeff("X", 1), rS * lp)
check("S source Y", sources.coeff("FS", 1).coeff("Y", 1), 2 * rS * ls)
check("H source square", sources.coeff("JHdagJH", 1), rH)
check("S source square", sources.coeff("JSdagJS", 1), rS)

# Algebraic field redefinition identity, after contracting conjugates.
dd, kk, cross1, cross2 = map(P, ["DdagD", "KdagK", "DdagK", "KdagD"])
variation = -F(1, 2) * ((dd - cross1 + cross2 - kk) + (dd + cross1 - cross2 - kk))
check("field redefinition removes Q and retains KdagK", dd + variation, kk)

e, zH, zS, tH, tS = map(P, ["loop", "zH", "zS", "tH", "tS"])
UH = (mh + e * tH) * (1 - e * zH)
check("canonical H mass parameter", UH.coeff("loop", 1), tH - mh * zH)
US = (ms + e * tS) * (1 - e * zS)
check("canonical S mass parameter", US.coeff("loop", 1), tS - ms * zS)
check("canonical H quartic in L", (-lh * (1 - e * zH)**2).coeff("loop", 1), 2 * lh * zH)
check("canonical S quartic in L", (-ls * (1 - e * zS)**2).coeff("loop", 1), 2 * ls * zS)
check("canonical portal in L", (-lp * (1 - e * zH) * (1 - e * zS)).coeff("loop", 1), lp * (zH + zS))

aM, aT, LM, LT, s, t, u = map(P, ["aMu", "aTau", "LMu", "LTau", "s", "t", "u"])
cH = aM * (LM - F(13, 6)) + aT * (LT - F(13, 6))
cS = cH
cD = F(1, 2) * (aM * (LM - 2) + aT * (LT - 2))
cJ = F(1, 2) * (-aM * (LM - 2) + aT * (LT - 2))
cNR = cD - F(1, 2) * (cH + cS)
check("inherited cD EOM projection", cNR, aM * (F(7, 6) - LM * F(1, 2)) + aT * (F(7, 6) - LT * F(1, 2)))
amp = cNR * t + cJ * (u - s)
target = aM * ((LM - 2) * s + t * F(1, 6)) + aT * ((LT - 2) * u + t * F(1, 6))
check("four-point polynomial reproduced for s+t+u=0", (amp - target).subs("u", -s - t))

etaH, etaS = map(P, ["etaH", "etaS"])
check("off-shell null directions leave cDNR unchanged", (cD - etaH - etaS) - F(1, 2) * (cH - 2 * etaH + cS - 2 * etaS), cNR)

OD, OH, OS = map(P, ["OD", "OH", "OS"])
OHred = -F(1, 2) * OD - mh * X * Y + 2 * lh * X**2 * Y + lp * X * Y**2 + F(1, 2) * Y * FH
OSred = -F(1, 2) * OD - ms * X * Y + 2 * ls * X * Y**2 + lp * X**2 * Y + F(1, 2) * X * FS
boxred = cH * OHred + cS * OSred + cD * OD
check("box EOM derivative row", boxred.coeff("OD", 1), cNR)
check("box EOM portal row", boxred.coeff("X", 1).coeff("Y", 1), -cH * mh - cS * ms)

# Independently rebuild every selected unified scalar row.
b = P("b")
canonical = (tH - mh*zH)*X + (tS - ms*zS)*Y + 2*lh*zH*X**2 + 2*ls*zS*Y**2 + (b + lp*(zH+zS))*X*Y
total = canonical + pot + boxred
scalar_total = total.subs("FH", 0).subs("FS", 0).subs("OD", 0)
unified = dict(rows)
unified[(1, 0)] += tH - mh*zH
unified[(0, 1)] += tS - ms*zS
unified[(2, 0)] += 2*lh*zH
unified[(0, 2)] += 2*ls*zS
unified[(1, 1)] += b + lp*(zH+zS) - cH*mh - cS*ms
unified[(2, 1)] += 2*lh*cH + lp*cS
unified[(1, 2)] += lp*cH + 2*ls*cS
for (nx, ny), value in unified.items():
    check(f"unified scalar row X^{nx} Y^{ny}", scalar_total.coeff("X", nx).coeff("Y", ny), value)
check("unified H source Y", (boxred + sources).coeff("FH", 1).coeff("Y", 1), cH*F(1, 2) + rH*lp)
check("unified S source X", (boxred + sources).coeff("FS", 1).coeff("X", 1), cS*F(1, 2) + rS*lp)

# Differentiate the local constant-background determinant expansion:
# (1+w)^2 [L + log(1+w) -3/2], log series is exact to this order.
w = P("w")
cw = (1+w)**2 * (L - F(3, 2) + w - w**2*F(1, 2) + w**3*F(1, 3))
check("CW linear coefficient agrees with mass self-energy", cw.coeff("w", 1), 2*(L-1))

print("RESULT:", count, "checks passed; no failures")
print("B0 through z^2 = Delta - L + 1 + z/2 + z^2/6")
print("PV / M2 through z^2 = 2(Delta-L+1) + (-Delta+L-1/2)z - z^2/3")
print("Pi / (h M2) through z^2 = -2(Delta-L+1) + (Delta-L+1/2)z + z^2/3")
print("Scope: algebra and fixed chiral traces only; not an automatic diagram census.")
