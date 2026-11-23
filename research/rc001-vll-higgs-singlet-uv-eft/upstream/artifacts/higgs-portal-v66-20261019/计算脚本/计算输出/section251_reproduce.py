from fractions import Fraction as F
from math import factorial
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
    residue = P(actual) - P(expected)
    if residue.t:
        raise AssertionError(f"{name}: {residue}")
    count += 1
    print(f"PASS {count:02d} {name}")


def trunc(poly, n, variables=("a", "b")):
    return P({m: c for m, c in P(poly).t.items()
              if sum(e for v, e in m if v in variables) <= n})


def degree(poly, n, variables=("a", "b")):
    return P({m: c for m, c in P(poly).t.items()
              if sum(e for v, e in m if v in variables) == n})


print("Python:", sys.version.split()[0])
print("Arithmetic: exact fractions.Fraction sparse multivariate polynomials")
a, b, L, delta = map(P, ["a", "b", "L", "Delta"])
p, q = a + b, a*b
order = 6
inverse = sum(((-p)**n for n in range(order + 1)), P())
low = P()
for _ in range(order + 1):
    low = trunc((q + low**2) * inverse, order)
high = 1 + p - low
check("light eigenvalue characteristic equation to degree 6", trunc(low**2-(1+p)*low+q, order))
check("heavy eigenvalue characteristic equation to degree 6", trunc(high**2-(1+p)*high+q, order))
check("trace of squared-mass matrix", high + low, 1+p)
check("determinant of squared-mass matrix", trunc(high*low, order), q)
check("heavy eigenvalue through degree 3", trunc(high, 3), 1+p-q+p*q)
check("light eigenvalue through degree 3", trunc(low, 3), q-p*q)
check("light determinant starts at degree 4", trunc(low**2, 3))
check("light determinant leading degree 4", degree(low**2, 4), q**2)
trace_square = 1 + 2*p + a**2 + b**2
check("exact trace-square invariant", trunc(high**2 + low**2, order), trace_square)
check("UV mixed quartic is absent", trace_square.coeff("a", 1).coeff("b", 1))
check("UV degree-3 polynomial is absent", degree(trace_square, 3))

shift = high-1
log_series = sum((F((-1)**(n+1), n)*trunc(shift**n, 3) for n in range(1, 4)), P())
fheavy = trunc(high**2 * (L-F(3,2)+log_series), 3)
fexpected = L-F(3,2) + 2*(L-1)*p + L*(a**2+b**2) + 2*q + p**3*F(1,3)-2*p*q
check("entire heavy Coleman-Weinberg polynomial through degree 3", fheavy, fexpected)
check("CW linear a", fheavy.coeff("a",1).coeff("b",0), 2*(L-1))
check("CW linear b", fheavy.coeff("a",0).coeff("b",1), 2*(L-1))
check("CW quartic a^2", fheavy.coeff("a",2).coeff("b",0), L)
check("CW quartic b^2", fheavy.coeff("a",0).coeff("b",2), L)
check("CW quartic ab", fheavy.coeff("a",1).coeff("b",1), 2)
check("CW sextic a^3", fheavy.coeff("a",3).coeff("b",0), F(1,3))
check("CW sextic b^3", fheavy.coeff("a",0).coeff("b",3), F(1,3))
check("CW sextic a^2 b", fheavy.coeff("a",2).coeff("b",1), -1)
check("CW sextic a b^2", fheavy.coeff("a",1).coeff("b",2), -1)
check("all sextic scale logarithms cancel", degree(fheavy,3).derivative("L"))

# Independent log-determinant master integrals. J_ab / (q_loop/M^2)
# = Gamma(a+b-2) Gamma(2-a) / Gamma(b), for a+b=3.
def master(aa, bb):
    assert aa+bb == 3 and aa < 2
    return F(factorial(aa+bb-3)*factorial(1-aa), factorial(bb-1))


j03, j12 = master(0,3), master(1,2)
check("finite Euclidean J03", j03, F(1,2))
check("finite Euclidean J12", j12, 1)
v3_logdet = -2*(-p*q*j12 + p**3*F(1,3)*j03)
check("independent momentum determinant equals eigenvalue sextic", v3_logdet, -degree(fheavy,3))
check("momentum determinant pure sign", v3_logdet.coeff("a",3).coeff("b",0), -F(1,3))
check("momentum determinant mixed sign", v3_logdet.coeff("a",2).coeff("b",1), 1)

X,Y,u,v,M2,im2 = map(P,["X","Y","u","v","M2","invM2"])
A,B = u*X,v*Y
V = -2*M2*(L-1)*(A+B) - L*(A**2+B**2)-2*A*B-im2*((A**3+B**3)*F(1,3)-A**2*B-A*B**2)
pole = delta*(2*M2*(A+B)+A**2+B**2)
rows_v = {
    (1,0):-2*M2*(L-1)*u,
    (0,1):-2*M2*(L-1)*v,
    (2,0):-L*u**2,
    (0,2):-L*v**2,
    (1,1):-2*u*v,
    (3,0):-im2*u**3*F(1,3),
    (0,3):-im2*v**3*F(1,3),
    (2,1):im2*u**2*v,
    (1,2):im2*u*v**2,
}
for (nx,ny), val in rows_v.items():
    check(f"direct V monomial X^{nx}Y^{ny}",V.coeff("X",nx).coeff("Y",ny),val)
check("two-point mass threshold recovered", -V.derivative("X").subs("X",0).subs("Y",0), 2*M2*(L-1)*u)
check("portal V threshold recovered",V.coeff("X",1).coeff("Y",1),-2*u*v)
check("UV X mass row",pole.coeff("X",1).coeff("Y",0),2*delta*M2*u)
check("UV X2 row",pole.coeff("X",2).coeff("Y",0),delta*u**2)
check("UV XY row",pole.coeff("X",1).coeff("Y",1))

# Build the canonical renormalizable matching and verify scale differences.
loop = P("loop")
lh,ls,lp = map(P,["lambdaH","lambdaS","lambdaP"])
mh,ms = map(P,["muH2","muS2"])
zH,zS = loop*u*(F(1,2)-L),loop*v*(F(1,2)-L)
tH,tS = 2*loop*u*M2*(L-1),2*loop*v*M2*(L-1)
dmuH,dmuS = tH-mh*zH,tS-ms*zS
dlh,dls = -loop*L*u**2-2*lh*zH,-loop*L*v**2-2*ls*zS
dlp = -2*loop*u*v-lp*(zH+zS)
betas = [
    ("muH2",dmuH,4*loop*u*M2+2*mh*loop*u),
    ("muS2",dmuS,4*loop*v*M2+2*ms*loop*v),
    ("lambdaH",dlh,4*lh*loop*u-2*loop*u**2),
    ("lambdaS",dls,4*ls*loop*v-2*loop*v**2),
    ("lambdaP",dlp,2*lp*loop*(u+v)),
]
for name, threshold, beta in betas:
    check("canonical threshold cancels heavy beta "+name,-2*threshold.derivative("L")+beta)

# All monomials already included in v54 are subtracted before merging.
old_direct = -2*M2*(L-1)*(A+B)-2*A*B
new_only_L = -V+old_direct
expected_new_L = L*(A**2+B**2)+im2*((A**3+B**3)*F(1,3)-A**2*B-A*B**2)
check("subtract overlap with v54",new_only_L,expected_new_L)
check("do not duplicate X threshold",new_only_L.coeff("X",1).coeff("Y",0))
check("do not duplicate Y threshold",new_only_L.coeff("X",0).coeff("Y",1))
check("do not duplicate portal threshold",new_only_L.coeff("X",1).coeff("Y",1))
check("new sextic L coefficient X2Y",new_only_L.coeff("X",2).coeff("Y",1),-im2*u**2*v)
check("new sextic L coefficient XY2",new_only_L.coeff("X",1).coeff("Y",2),-im2*u*v**2)

# Mixed derivatives in real radial variables plus explicit fixed-VEV tadpoles.
vh,vs,h,s = map(P,["vh","vs","h","s"])
Xv,Yv = vh**2*F(1,2),vs**2*F(1,2)
at_v = lambda pol: P(pol).subs("X",Xv).subs("Y",Yv)
dx,dy = V.derivative("X"),V.derivative("Y")
ct = V-at_v(dx)*X-at_v(dy)*Y
Vhs = ct.subs("X",(vh+h)**2*F(1,2)).subs("Y",(vs+s)**2*F(1,2))
at0 = lambda pol: P(pol).subs("h",0).subs("s",0)
check("fixed-VEV Higgs tadpole cancels",at0(Vhs.derivative("h")))
check("fixed-VEV singlet tadpole cancels",at0(Vhs.derivative("s")))
check("mixed radial potential curvature",at0(Vhs.derivative("h").derivative("s")),vh*vs*u*v*(-2+im2*(u*vh**2+v*vs**2)))
check("Higgs diagonal potential curvature",at0(Vhs.derivative("h").derivative("h")),vh**2*(-2*L*u**2+im2*(-u**3*vh**2+u**2*v*vs**2)))
check("singlet diagonal potential curvature",at0(Vhs.derivative("s").derivative("s")),vs**2*(-2*L*v**2+im2*(-v**3*vs**2+u*v**2*vh**2)))

# Turning off either Yukawa or swapping A and B is an exact symmetry check.
check("pure-A limit",V.subs("v",0),-2*M2*(L-1)*u*X-L*u**2*X**2-im2*u**3*X**3*F(1,3))
swapped = V.subs("u",P("tmp")).subs("v",u).subs("tmp",v).subs("X",P("tmp")).subs("Y",X).subs("tmp",Y)
check("A-B interchange symmetry",swapped,V)

# Numerical convergence: independent Decimal square root and natural logarithm.
# These are numerical checks, separate from the exact symbolic checks above.
from decimal import Decimal as D, localcontext
print("NUMERICAL CHECKS (Decimal precision 80; M^2=1)")
numerical = []
with localcontext() as ctx:
    ctx.prec = 80
    for exponent in (2,3,4):
        aa = D(10)**(-exponent)
        bb = D(7)/D(10)*aa
        ll = D(3)/D(10)
        pp,qq = aa+bb,aa*bb
        high_d = (1+pp+((1+pp)**2-4*qq).sqrt())/2
        low_d = qq/high_d
        f = lambda x:x*x*(x.ln()+ll-D(3)/D(2))
        heavy_exact = f(high_d)-f(D(1))
        approx = 2*(ll-1)*pp+ll*(aa*aa+bb*bb)+2*qq+(aa**3+bb**3)/3-aa*aa*bb-aa*bb*bb
        residual = heavy_exact-approx
        ratio = abs(residual)/(aa**4)
        light_exact = f(low_d)
        assert ratio < D(10)
        numerical.append((exponent,ratio))
        print(f"a=1e-{exponent}, b=0.7a: heavy remainder={residual:.10E}; |R|/a^4={ratio:.10E}; light determinant={light_exact:.10E}")
    assert abs(numerical[-1][1]-numerical[-2][1]) < D("0.01")
print(f"RESULT: {count} exact symbolic checks passed; 3 high-precision numerical cases passed")
print("V6 = -[A^3/3+B^3/3-A^2 B-A B^2]/(16 pi^2 M^2)")
print("Scope: constant-background fermion determinant and selected vector merge; no FeynArts/FeynCalc run.")

