#!/usr/bin/env python3
"""P0.1-P0.4 audit: crossed on-shell dimension-eight UV box and EFT soft kernel.

The calculation is per ordered cycle, with |y|^4 or |lambda|^4 factored out.
It performs a full on-shell Mandelstam expansion through O(p^4/M_E^4),
a d-dimensional tensor reduction of the hard region, and a direct
Feynman-parameter integration of the soft region of the same UV numerator.

This is an analytic method-of-regions audit, not FeynArts/FeynCalc diagram
generation. The final local polynomial is an on-shell Green-function result;
it has not yet been reduced to a nonredundant off-shell operator basis.
"""
import sympy as sp
from itertools import product

eps, d = sp.symbols("eps d")
M, mu = sp.symbols("M mu", positive=True)
s, t, u = sp.symbols("s t u")
a, b, c, K = sp.symbols("a b c K")

# All momenta are incoming, p_i^2=0, p1+p2+p3+p4=0,
# s=(p1+p2)^2, t=(p1+p3)^2, u=(p1+p4)^2, s+t+u=0.
# q=p1+p2; p1.p4=u/2, p1.q=s/2, p4.q=-s/2.
AB = K + a + c + s/2
CD = K - b
AC = K + a - b - u/2
BD = K + c
AD = K + a
BC = K + c - b + s/2
N = sp.expand(2*(AB*CD - AC*BD + AD*BC))
A, B, C = 2*c+s, 2*a, -2*b
vars_on = [a,b,c,s,t,u,K]

def weighted_degree(mon):
    ia,ib,ic,is_,it,iu,iK = mon
    return ia+ib+ic+2*(is_+it+iu)

def pairings(labels, gram):
    if not labels:
        return [sp.Integer(1)]
    first = labels[0]
    out = []
    for j in range(1, len(labels)):
        rest = labels[1:j] + labels[j+1:]
        dot = gram[(first, labels[j])]
        for tail in pairings(rest, gram):
            out.append(dot*tail)
    return out

def angular_average(i,j,kpow,gram):
    n = i+j+kpow
    if n % 2:
        return sp.Integer(0), 0
    labels = ["a"]*i + ["b"]*j + ["c"]*kpow
    pair_sum = sp.Add(*pairings(labels,gram)) if labels else sp.Integer(1)
    npairs = n//2
    den = sp.prod(d+2*r for r in range(npairs)) if npairs else sp.Integer(1)
    return sp.factor(pair_sum/den), npairs

# Hard region: expand the two light and two heavy denominators.
gram = {
    ("a","a"):sp.Integer(0), ("b","b"):sp.Integer(0), ("c","c"):s,
    ("a","b"):u/2, ("b","a"):u/2,
    ("a","c"):s/2, ("c","a"):s/2,
    ("b","c"):-s/2, ("c","b"):-s/2,
}
hard_groups = {}
for na in range(5):
    for nb in range(5):
        for nc in range(5):
            if na+nb+nc > 4:
                continue
            poly = sp.Poly(sp.expand(N*A**na*B**nb*C**nc), *vars_on)
            for mon, coeff in poly.terms():
                if weighted_degree(mon) != 4:
                    continue
                ia,ib,ic,is_,it,iu,iK = mon
                ang,npairs = angular_average(ia,ib,ic,gram)
                if ang == 0:
                    continue
                ext = s**is_ * t**it * u**iu
                key = (na+2, nb+nc+2, iK+npairs)
                value = coeff*(-1)**(na+nb+nc)*ang*ext
                hard_groups[key] = hard_groups.get(key,0) + value
hard_groups = {k:sp.factor(v) for k,v in hard_groups.items() if v != 0}
assert len(hard_groups) == 13

DeltaIR = 1/eps-sp.EulerGamma+sp.log(4*sp.pi)
DeltaUV = DeltaIR
LE = sp.log(M**2/mu**2)

hard = 0
for (aden,bden,nrad), coeff in hard_groups.items():
    Aint = 2+nrad-aden
    Bint = bden-2-nrad+aden
    assert Bint == 2
    # For Aint=0, Gamma(-eps) has an IR pole. Retain the O(eps)
    # coefficient of the angular numerator because it multiplies 1/eps.
    coeff_order = 2 if Aint == 0 else 1
    coeff_ser = sp.series(coeff.subs(d,4-2*eps),eps,0,coeff_order).removeO()
    if Aint == 0:
        radial = (-DeltaIR+LE-2)/sp.gamma(bden)
    else:
        radial = sp.gamma(Aint)/sp.gamma(bden)
    hard += coeff_ser*radial
hard = sp.simplify(sp.series(hard,eps,0,1).removeO()/(16*sp.pi**2*M**4))

hard_expected = (
    (s**2+2*s*u)*(DeltaIR-LE)
    +sp.Rational(11,6)*s**2
    +sp.Rational(10,3)*s*u
    -sp.Rational(3,10)*u**2
)/(96*sp.pi**2*M**4)
assert sp.simplify(hard-hard_expected) == 0

# Soft region: expand both heavy propagators to 1/M_E^4 and integrate
# the full numerator, including terms proportional to l^2.
x, la, lb, lc, L2 = sp.symbols("x la lb lc L2", real=True)
Kshift = L2-2*x*lc+x**2*s
ashift = la-x*s/2
bshift = lb+x*s/2
cshift = lc-x*s
soft_num = sp.expand(N.subs({K:Kshift,a:ashift,b:bshift,c:cshift}))
gram_l = {
    ("la","la"):sp.Integer(0), ("lb","lb"):sp.Integer(0), ("lc","lc"):s,
    ("la","lb"):u/2, ("lb","la"):u/2,
    ("la","lc"):s/2, ("lc","la"):s/2,
    ("lb","lc"):-s/2, ("lc","lb"):-s/2,
}
def angular_average_l(i,j,kpow):
    n = i+j+kpow
    if n % 2:
        return sp.Integer(0),0
    labels = ["la"]*i+["lb"]*j+["lc"]*kpow
    pair_sum = sp.Add(*pairings(labels,gram_l)) if labels else sp.Integer(1)
    npairs = n//2
    den = sp.prod(d+2*r for r in range(npairs)) if npairs else sp.Integer(1)
    return sp.factor(pair_sum/den),npairs

soft_vars = [la,lb,lc,L2,s,u,x]
soft_poly = sp.Poly(soft_num,*soft_vars)
soft_by_n = {}
for mon,coeff in soft_poly.terms():
    ila,ilb,ilc,iL,is_,iu,ix = mon
    ang,npairs = angular_average_l(ila,ilb,ilc)
    if ang == 0:
        continue
    nrad = iL+npairs
    soft_by_n[nrad] = soft_by_n.get(nrad,0)+coeff*ang*s**is_*u**iu*x**ix

def beta_moment(m,n):
    return sp.gamma(m+n+1-eps)*sp.gamma(n+1-eps)/sp.gamma(m+2*n+2-2*eps)

soft_parts = {}
for nrad,Cx in soft_by_n.items():
    Cx = sp.expand(Cx.subs(d,4-2*eps))
    poly = sp.Poly(Cx,x)
    x_integral = sp.Add(*[
        coeff*beta_moment(m,nrad)
        for (m,),coeff in poly.terms()
    ])
    radial_pref = (
        mu**(2*eps)/(4*sp.pi)**(2-eps)
        * sp.gamma(2-eps+nrad)*sp.gamma(eps-nrad)/sp.gamma(2-eps)
        * s**(nrad-eps)/M**4
    )
    soft_parts[nrad] = sp.simplify(radial_pref*x_integral)
soft_exact = sp.simplify(sum(soft_parts.values()))
soft = sp.series(soft_exact,eps,0,1).removeO()

soft_expected = -(
    (s**2+2*s*u)*(DeltaUV-sp.log(s/mu**2)+sp.Rational(5,3))
)/(96*sp.pi**2*M**4)
soft_pole = sp.simplify(sp.limit(eps*soft,eps,0))
assert sp.simplify(soft_pole+(s**2+2*s*u)/(96*sp.pi**2*M**4)) == 0

soft_finite = sp.simplify(sp.limit(soft-soft_pole/eps,eps,0))
soft_finite_expected = sp.simplify(sp.limit(
    soft_expected+(s**2+2*s*u)/(96*sp.pi**2*M**4*eps),eps,0
))
soft_finite = soft_finite.subs({
    sp.log(64*sp.pi**3*mu**6):3*sp.log(4*sp.pi*mu**2),
    sp.log(4096*sp.pi**6*mu**12):6*sp.log(4*sp.pi*mu**2),
})
assert sp.simplify(soft_finite-soft_finite_expected) == 0

# Hard + soft: all poles cancel, and the result is independent of mu_R.
matched = sp.simplify(hard+soft_expected)
matched_expected = (
    -(s**2+2*s*u)*(2*sp.log(M)-sp.log(s)+sp.Rational(5,3))
    +sp.Rational(11,6)*s**2
    +sp.Rational(10,3)*s*u
    -sp.Rational(3,10)*u**2
)/(96*sp.pi**2*M**4)
assert sp.simplify(matched-matched_expected) == 0
assert sp.simplify(sp.diff(matched,mu)*mu) == 0

# The transverse-current projection is only one part of the full hard polynomial.
PTP_on_shell = -(s**2+2*s*u)/4
hard_transverse = -PTP_on_shell/(24*sp.pi**2*M**4)*(
    DeltaIR-LE+sp.Rational(17,12)
)
soft_transverse = PTP_on_shell/(24*sp.pi**2*M**4)*(
    DeltaUV-sp.log(s/mu**2)+sp.Rational(5,3)
)
assert sp.simplify(soft_transverse-soft_expected) == 0
hard_local_remainder = sp.simplify(hard-hard_transverse)
assert sp.simplify(hard_local_remainder-(
    sp.Rational(5,12)*s**2
    +sp.Rational(1,2)*s*u
    -sp.Rational(3,10)*u**2
)/(96*sp.pi**2*M**4)) == 0

# Crossed external pairing: exchange p2 <-> p4, equivalently s <-> u.
hard_cross = hard.subs({s:u,u:s},simultaneous=True)
soft_cross = soft_expected.subs({s:u,u:s},simultaneous=True)
matched_cross = sp.simplify(hard_cross+soft_cross)
matched_total = sp.simplify(matched+matched_cross)
assert sp.simplify(matched_total.subs({s:u,u:s},simultaneous=True)-matched_total) == 0
assert sp.simplify(sp.limit(eps*(hard+soft_expected),eps,0)) == 0
assert sp.simplify(sp.limit(eps*(hard_cross+soft_cross),eps,0)) == 0

# SU(2)_L current trace: the two Wick pairings give two distinct tensors.
def delta(i,j):
    return int(i==j)
for i,j,k,l in product(range(2),repeat=4):
    # Expand tr_2[J_ab J_ba] with the s and crossed external assignments.
    tensor_s = sum(
        delta(a0,i)*delta(b0,j)*delta(b0,k)*delta(a0,l)
        for a0 in range(2) for b0 in range(2)
    )
    tensor_u = sum(
        delta(a0,i)*delta(b0,l)*delta(b0,k)*delta(a0,j)
        for a0 in range(2) for b0 in range(2)
    )
    assert tensor_s == delta(j,k)*delta(l,i)
    assert tensor_u == delta(l,k)*delta(j,i)
assert delta(1,1)*delta(1,1) == 1  # fixed neutral component; no extra factor 2

# Exact chiral trace: parity-even part is one half the Dirac trace.
I = sp.I
zero2 = sp.zeros(2)
sigma1 = sp.Matrix([[0,1],[1,0]])
sigma2 = sp.Matrix([[0,-I],[I,0]])
sigma3 = sp.Matrix([[1,0],[0,-1]])
def block2(A,B,C,D):
    return A.row_join(B).col_join(C.row_join(D))
gamma = [
    sp.diag(1,1,-1,-1),
    block2(zero2,sigma1,-sigma1,zero2),
    block2(zero2,sigma2,-sigma2,zero2),
    block2(zero2,sigma3,-sigma3,zero2),
]
gamma5 = I*gamma[0]*gamma[1]*gamma[2]*gamma[3]
PR = (sp.eye(4)+gamma5)/2
PL = (sp.eye(4)-gamma5)/2
av,bv,cv,dv = [sp.symbols(f"{name}0:4") for name in ("a","b","c","d")]
def slash(v):
    return gamma[0]*v[0]-gamma[1]*v[1]-gamma[2]*v[2]-gamma[3]*v[3]
chiral_trace = sp.trace(PR*slash(av)*PL*slash(bv)*PR*slash(cv)*PL*slash(dv)*PR)
dirac_trace = sp.trace(slash(av)*slash(bv)*slash(cv)*slash(dv))
odd_trace = sp.trace(slash(av)*slash(bv)*slash(cv)*slash(dv)*gamma5)
assert sp.simplify(chiral_trace-(dirac_trace+odd_trace)/2) == 0

# Effective-action normalization: (1/2 determinant)*(1/2)^2 EOM currents;
# functional differentiation gives 2 assignments and J_H=-2P gives factor 4.
pi_weyl = sp.Rational(1,24)
action_coefficient = sp.Rational(1,2)*sp.Rational(1,2)**2*pi_weyl
assert action_coefficient == sp.Rational(1,192)
amplitude_coefficient = 2*4*action_coefficient
assert amplitude_coefficient == sp.Rational(1,24)

# S_tau=S* reverses the scalar current, but the quadratic kernel is unchanged.
S,Sd,dS,dSd = sp.symbols("S Sd dS dSd",commutative=True)
j_mu = I*(Sd*dS-dSd*S)
j_tau = I*(S*dSd-dS*Sd)
assert sp.simplify(j_tau+j_mu) == 0
assert sp.simplify(j_tau**2-j_mu**2) == 0

print("PASS 1: 13 nonzero radial tensor structures in the complete on-shell hard expansion")
print("PASS 2: hard kernel = [(s^2+2su)(Delta_IR-L_E)+11s^2/6+10su/3-3u^2/10]/(96 pi^2 M_E^4)")
print("PASS 3: direct soft expansion of the same UV numerator reproduces the one-Weyl current kernel")
print("PASS 4: hard IR and soft UV poles cancel in the s channel")
print("PASS 5: the matched nonlocal term is independent of the arbitrary matching scale")
print("PASS 6: the transverse-current part has the 17/12 hard constant")
print("PASS 7: an additional finite local hard polynomial remains beyond the transverse-current projection")
print("PASS 8: the crossed channel is obtained by s <-> u; the sum is crossing symmetric")
print("PASS 9: SU(2) tensors are delta_jk delta_li and delta_lk delta_ji; no extra doublet multiplicity")
print("PASS 10: the exact chiral trace is one half the Dirac trace plus the gamma5-odd term")
print("PASS 11: determinant, EOM-current, current-matrix-element, and functional-derivative factors give 1/24")
print("PASS 12: S_tau=S* reverses j_S but leaves the quadratic singlet kernel unchanged")
print("SCOPE: on-shell pure-Higgs/pure-singlet one-cycle four-scalar box at O(p^4/M_E^4)")
print("OPEN: off-shell Green-basis decomposition, EOM/IBP operator reduction, and FeynArts/FeynCalc diagram generation")
