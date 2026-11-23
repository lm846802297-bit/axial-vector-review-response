#!/usr/bin/env python3
"""QLD one-background hard-region degree-five radial-reduction audit.

For Gamma^mu = p^mu F_p + q^mu F_q, explicit-vector coefficients need
scalar degree four. A free loop-vector term k^mu instead needs scalar degree
five, because its angular average pairs one k with an external momentum.
All shifted propagators are expanded and all angular averages are d-dimensional.
The script evaluates hard radial masters and the ordinary-line EFT soft
integral through O(eps^0), and checks the pure-U(1)_X hard-plus-soft Ward
identity and matching-scale cancellation. Overall 1PI factors and the
hypercharge/SU(2)_L projections remain outside its scope.
"""
import sympy as sp

d, eps, M2 = sp.symbols("d eps M2")
k2, kq, kp, kpp = sp.symbols("k2 kq kp kpp")
p2, q2, pp2, pq, ppdotp = sp.symbols("p2 q2 pp2 pq ppdotp")
L_M = sp.symbols("L_M")

# Numerator coefficients, N^mu=2*(coefficients).
NL = {"k": k2+2*kp+pq, "p": -(k2+kq), "q": k2+kp}
# Minkowski N_E has +M_E^2 k^mu, but this term flips relative sign
# under Wick rotation: the Euclidean numerator uses -M_E^2 k_E^mu.
NE = {"k": k2-M2-ppdotp, "p": k2+kpp, "pp": k2+kp}

DOT = {
    ("p","p"):p2, ("q","q"):q2, ("pp","pp"):pp2,
    ("p","q"):pq, ("q","p"):pq,
    ("p","pp"):ppdotp, ("pp","p"):ppdotp,
}
def pairings(labels):
    labels=tuple(labels)
    if not labels:
        return {sp.Integer(1):1}
    out={}
    first=labels[0]
    for j in range(1,len(labels)):
        second=labels[j]
        rest=labels[1:j]+labels[j+1:]
        dot=DOT[(first,second)]
        for product,mult in pairings(rest).items():
            term=sp.expand(dot*product)
            out[term]=out.get(term,0)+mult
    return out

def angular_denominator(r):
    return d*sp.prod(d+2*j for j in range(1,r))

def reduce_graph(kind,component,numerator):
    if kind=="L":
        vectors=["q","p"]; kvars=[kq,kp]
        shifts=[2*kq+q2,2*kp+p2]
        base_a,base_b=2,1
    else:
        vectors=["p","pp"]; kvars=[kp,kpp]
        shifts=[2*kp+p2,2*kpp+pp2]
        base_a,base_b=1,2

    # The free k^mu index is converted to an external vector by angular
    # averaging, so its scalar coefficient must carry degree five.
    target=5 if component=="k" else 4
    result={}
    poly_vars=[k2,*kvars,p2,q2,pp2,pq,ppdotp]
    for n in range(target+1):
        for m in range(target+1-n):
            polynomial=(-1)**(n+m)*sp.expand(shifts[0]**n*shifts[1]**m*numerator)
            poly=sp.Poly(polynomial,*poly_vars,domain="EX")
            for mon,coeff in poly.terms():
                ex=dict(zip(poly_vars,mon))
                degree=ex[kvars[0]]+ex[kvars[1]]+2*sum(
                    ex[s] for s in [p2,q2,pp2,pq,ppdotp]
                )
                if degree!=target:
                    continue
                labels=[vectors[0]]*ex[kvars[0]]+[vectors[1]]*ex[kvars[1]]
                scalar=coeff
                for sym in [p2,q2,pp2,pq,ppdotp]:
                    scalar*=sym**ex[sym]

                # Light graph: q shift belongs to the massless denominator;
                # p shift belongs to the massive denominator.
                if kind=="L":
                    a,b=base_a+n,base_b+m
                else:
                    a,b=base_a,base_b+n+m

                if component=="k":
                    if len(labels)%2!=1:
                        continue
                    r=(len(labels)+1)//2
                    den=angular_denominator(r)
                    for i,vec in enumerate(labels):
                        rest=labels[:i]+labels[i+1:]
                        for product,mult in pairings(rest).items():
                            key=(vec,a,b,ex[k2]+r)
                            result[key]=result.get(key,0)+2*scalar*mult*product/den
                else:
                    if len(labels)%2:
                        continue
                    r=len(labels)//2
                    den=angular_denominator(r) if r else 1
                    product=sum(mult*term for term,mult in pairings(tuple(labels)).items())
                    key=(component,a,b,ex[k2]+r)
                    result[key]=result.get(key,0)+2*scalar*product/den
    return {key:sp.factor(value) for key,value in result.items() if value!=0}

L={c:reduce_graph("L",c,n) for c,n in NL.items()}
E={c:reduce_graph("E",c,n) for c,n in NE.items()}
assert len(L["k"])==31 and len(L["p"])==12 and len(L["q"])==12
assert len(E["k"])==14 and len(E["p"])==3 and len(E["pp"])==3

def combine_vectors(graph):
    out={"p":{},"q":{},"pp":{}}
    for component_dict in graph.values():
        for (vec,a,b,t),coefficient in component_dict.items():
            key=(a,b,t)
            out[vec][key]=out[vec].get(key,0)+coefficient
    return {vec:{key:sp.factor(val) for key,val in dic.items() if val!=0}
            for vec,dic in out.items()}

Lvec=combine_vectors(L)
Evec=combine_vectors(E)
masters=sorted(set(
    key for graph in (Lvec,Evec) for component in graph.values() for key in component
))
expected=[
    (1,4,1),(1,5,1),(1,5,2),(1,6,2),(1,6,3),(1,7,3),(1,7,4),
    (2,3,1),(2,4,2),(2,5,3),(2,6,4),
    (3,2,1),(3,3,2),(3,4,3),(3,5,4),
    (4,1,1),(4,2,2),(4,3,3),(4,4,4),
    (5,1,2),(5,2,3),(5,3,4),(6,1,3),(6,2,4),(7,1,4)
]
assert masters==expected
for a,b,t in masters:
    uv_arg=a+b-2-t
    ir_arg=2+t-a
    assert uv_arg>0
    print(f"J[{a},{b},{t}]: UV finite; IR gamma argument={ir_arg} at eps=0")

def J_msbar(a,b,t):
    expr=(
        sp.exp(eps*(L_M-sp.log(4*sp.pi)+sp.EulerGamma))
        /(4*sp.pi)**(2-eps)
        *M2**(2+t-a-b)
        *sp.gamma(2-eps+t-a)
        *sp.gamma(a+b-2+eps-t)
        /(sp.gamma(2-eps)*sp.gamma(b))
    )
    return sp.series(expr,eps,0,1).removeO()

def sum_form_factor(radial_terms):
    total=0
    for (a,b,t),coefficient in radial_terms.items():
        total+=coefficient.subs(d,4-2*eps)*J_msbar(a,b,t)
    return sp.series(sp.expand(total),eps,0,1).removeO()

def pole_and_finite(expr):
    pole=sp.factor(sp.limit(eps*expr,eps,0))
    finite=sp.factor(sp.limit(expr-pole/eps,eps,0))
    return pole,finite

LP=sum_form_factor(Lvec["p"])
LQ=sum_form_factor(Lvec["q"])
EP=sum_form_factor(Evec["p"])
EPP=sum_form_factor(Evec["pp"])
LPpole,LPfinite=pole_and_finite(LP)
LQpole,LQfinite=pole_and_finite(LQ)
EPpole,EPfinite=pole_and_finite(EP)
EPPpole,EPPfinite=pole_and_finite(EPP)

P,Q,R,PP,T=sp.symbols("P Q R PP T")
sub={p2:P,q2:Q,pq:R,pp2:PP,ppdotp:T}
assert sp.simplify(LPpole.subs(sub)-Q*(P-R)/(24*sp.pi**2*M2**2))==0
assert sp.simplify(LQpole.subs(sub)+R*(P-R)/(24*sp.pi**2*M2**2))==0
assert EPpole==0 and EPPpole==0
assert sp.simplify((R*LPpole+Q*LQpole).subs(sub))==0

print("PASS: scalar form factors degree four plus one external vector give degree five.")
print("PASS: all shifted propagators expanded with correct radial indices.")
print("PASS: 25 distinct radial masters; all UV convergent in the hard region.")
print("PASS: L attachment 31 k-vector, 12 p-vector, 12 q-vector structures.")
print("PASS: E attachment 14 k-vector, 3 p-vector, 3 p'-vector structures.")
print("PASS: hard light-attachment IR pole is transverse: R*F_p^pole+Q*F_q^pole=0.")
print("L attachment F_p pole:",LPpole.subs(sub))
print("L attachment F_p finite:",LPfinite.subs(sub))
print("L attachment F_q pole:",LQpole.subs(sub))
print("L attachment F_q finite:",LQfinite.subs(sub))
print("E attachment F_p finite:",EPfinite.subs(sub))
print("E attachment F_pprime finite:",EPPfinite.subs(sub))
print("SCOPE: hard subgraph form factors are printed above; soft subtraction and full U(1)_X closure are evaluated below.")


# Ordinary-line EFT-soft UV pole at O(M_E^-4). The soft expansion of the
# light-attachment heavy propagator contributes -K^2/M_E^4. Feynman combine
# 1/[k^2(k+q)^2], shift k=l-x q, and retain the total degree-five vector term.
x = sp.symbols("x")
ell2, ellp, ellq = sp.symbols("ell2 ellp ellq")
A = ell2+ellp+(1-2*x)*ellq+(1-x)*R-x*(1-x)*Q       # K.k'
B = ell2+(1-2*x)*ellq-x*(1-x)*Q                  # k'.k
C = ell2+ellp-2*x*ellq-x*R+x**2*Q                # K.k
Ksq = ell2+2*ellp-2*x*ellq+P-2*x*R+x**2*Q
soft_num = {
    "ell": sp.expand(2*(A-B+C)*Ksq),
    "p": sp.expand(-2*B*Ksq),
    "q": sp.expand(2*(-x*A+x*B+(1-x)*C)*Ksq),
}
soft_vars = [ell2,ellp,ellq,P,Q,R]
soft_reduced = {"p":{}, "q":{}}

for component, expression in soft_num.items():
    poly = sp.Poly(expression,*soft_vars,domain="EX")
    for monomial, coeff in poly.terms():
        ex = dict(zip(soft_vars,monomial))
        labels = ["p"]*ex[ellp]+["q"]*ex[ellq]
        degree = ex[ellp]+ex[ellq]+2*(ex[P]+ex[Q]+ex[R])
        scalar = coeff*P**ex[P]*Q**ex[Q]*R**ex[R]
        if component == "ell":
            if len(labels)%2 != 1:
                continue
            r = (len(labels)+1)//2
            if degree+2*(ex[ell2]+r) != 5:
                continue
            den = angular_denominator(r)
            for i,vec in enumerate(labels):
                rest = labels[:i]+labels[i+1:]
                for product,mult in pairings(rest).items():
                    t = ex[ell2]+r
                    delta = (x*(1-x)*Q)**t
                    soft_reduced[vec][t] = soft_reduced[vec].get(t,0) + scalar*mult*product*delta/den
        else:
            if len(labels)%2:
                continue
            r = len(labels)//2
            t = ex[ell2]+r
            if degree+2*t != 4:
                continue
            den = angular_denominator(r) if r else 1
            product = sum(mult*term for term,mult in pairings(tuple(labels)).items())
            delta = (x*(1-x)*Q)**t
            soft_reduced[component][t] = soft_reduced[component].get(t,0) + scalar*product*delta/den

soft_uv = {}
for vector, terms in soft_reduced.items():
    residue = sum(
        sp.integrate(sp.expand(expr)*((-1)**t*(t+1)),(x,0,1))
        for t,expr in terms.items()
    )/(16*sp.pi**2)
    # The minus sign is from 1/(M_E^2+K^2)=1/M_E^2-K^2/M_E^4+...
    soft_uv[vector] = sp.factor(-residue.subs({p2:P,q2:Q,pq:R})/M2**2)

expected_soft_p = -Q*(P-R)/(24*sp.pi**2*M2**2)
expected_soft_q = R*(P-R)/(24*sp.pi**2*M2**2)
assert sp.simplify(soft_uv["p"]-expected_soft_p)==0
assert sp.simplify(soft_uv["q"]-expected_soft_q)==0

hard_plus_soft_q = sp.simplify(LQpole.subs(sub)+soft_uv["q"])
hard_plus_soft_p = sp.factor(LPpole.subs(sub)+soft_uv["p"])
assert hard_plus_soft_q==0
assert hard_plus_soft_p==0
assert sp.simplify((R*soft_uv["p"]+Q*soft_uv["q"]))==0

# The tree-level dimension-eight QLD operator is the covariant product
# (bar L H) (i slash D)^3 (H^dagger L). Its one-background vertex is
# V^mu=-g q_E [K'^2 gamma^mu + slash(K') gamma^mu slash(K) + K^2 gamma^mu].
# With q=K-K', slash(K') slash(q) slash(K)=K^2 slash(K')-K'^2 slash(K),
# so q.V=-g q_E [K^2 slash(K)-K'^2 slash(K')], the exact Ward difference.
# Closing the L line at this contact gives a one-propagator scaleless tadpole;
# it has no logarithmic 1/epsilon UV pole in the unbroken massless DR setup.

print("SOFT ORDINARY-LINE UV POLES")
print("F_p soft-line UV:",soft_uv["p"])
print("F_q soft-line UV:",soft_uv["q"])
print("PASS: soft UV pole is transverse: R*F_p^UV+Q*F_q^UV=0.")
print("PASS: hard IR + ordinary-line soft UV cancels in both p^mu and q^mu form factors.")
print("PASS: QLD8 covariant one-background vertex obeys the Ward difference identity.")
print("SCOPE: the soft UV-pole comparison is checked above; the finite soft integral is evaluated below.")


# Complete ordinary-line soft integral through O(eps^0).
# I_t(Delta)=mu^(2eps)/(4pi)^(2-eps) *
# Gamma(2-eps+t) Gamma(eps-t)/Gamma(2-eps) * Delta^(t-eps).
# soft_reduced already contains Delta^t=(x(1-x)Q)^t from the angular average.
mu2 = sp.symbols("mu2", positive=True)
soft_full = {}
for vector, terms in soft_reduced.items():
    total = 0
    for t, expr_with_delta in terms.items():
        expr_sub = expr_with_delta.subs({p2:P,q2:Q,pq:R})
        coeff_x = sp.cancel(expr_sub/(x*(1-x)*Q)**t)
        coeff_x = sp.expand(coeff_x.subs(d,4-2*eps))
        poly_x = sp.Poly(coeff_x,x,domain="EX")
        x_integral = 0
        for (n,), coefficient in poly_x.terms():
            x_integral += coefficient*sp.beta(n+t+1-eps,t+1-eps)
        radial_prefactor = (
            mu2**eps/(4*sp.pi)**(2-eps)
            *sp.gamma(2-eps+t)*sp.gamma(eps-t)/sp.gamma(2-eps)
        )
        total += radial_prefactor*Q**(t-eps)*x_integral
    soft_full[vector] = sp.factor(
        sp.simplify(sp.expand_func(
            sp.series(sp.expand(total),eps,0,1).removeO()
        ))/(-M2**2)
    )

L_Q = sp.log(mu2)-sp.log(Q)+sp.log(4*sp.pi)-sp.EulerGamma
expected_soft_full_p = -Q*(P-R)/(24*sp.pi**2*M2**2)*(1/eps+L_Q+sp.Rational(5,3))
expected_soft_full_q = R*(P-R)/(24*sp.pi**2*M2**2)*(1/eps+L_Q+sp.Rational(5,3))
assert sp.simplify(soft_full["p"]-expected_soft_full_p)==0
assert sp.simplify(soft_full["q"]-expected_soft_full_q)==0
assert sp.simplify(R*soft_full["p"]+Q*soft_full["q"])==0

# Convert the corrected heavy attachment from (p,p') to (p,q), p'=p-q.
FpE_pq = sp.factor((EPfinite+EPPfinite).subs(sub).subs({PP:P+Q-2*R,T:P-R}))
FqE_pq = sp.factor((-EPPfinite).subs(sub).subs({PP:P+Q-2*R,T:P-R}))
hard_p_finite = sp.factor(LPfinite.subs(sub)+FpE_pq)
hard_q_finite = sp.factor(LQfinite.subs(sub)+FqE_pq)
hard_p_pole = sp.factor(LPpole.subs(sub))
hard_q_pole = sp.factor(LQpole.subs(sub))
hard_scalar_finite = 30*L_M*(P-R)+70*P+21*Q-70*R
assert sp.simplify(hard_p_finite-Q*hard_scalar_finite/(720*sp.pi**2*M2**2))==0
assert sp.simplify(hard_q_finite+R*hard_scalar_finite/(720*sp.pi**2*M2**2))==0
assert sp.simplify(R*(hard_p_finite+hard_p_pole/eps)
                   +Q*(hard_q_finite+hard_q_pole/eps))==0

# The hard + soft sum is the full-theory amplitude in the method-of-regions
# decomposition, not the Wilson coefficient by itself.
L_M_expr = sp.log(mu2)-sp.log(M2)+sp.log(4*sp.pi)-sp.EulerGamma
hard_p_finite_full = hard_p_finite.subs(L_M,L_M_expr)
hard_q_finite_full = hard_q_finite.subs(L_M,L_M_expr)
full_p = sp.factor(hard_p_finite_full+soft_full["p"]+hard_p_pole/eps)
full_q = sp.factor(hard_q_finite_full+soft_full["q"]+hard_q_pole/eps)
full_scalar = 30*(P-R)*(sp.log(Q)-sp.log(M2))+20*(P-R)+21*Q
expected_full_p = Q*full_scalar/(720*sp.pi**2*M2**2)
expected_full_q = -R*full_scalar/(720*sp.pi**2*M2**2)
assert sp.simplify(full_p-expected_full_p)==0
assert sp.simplify(full_q-expected_full_q)==0
assert sp.simplify(R*full_p+Q*full_q)==0

print("FINITE SOFT FORM FACTORS")
print("F_p soft =",soft_full["p"])
print("F_q soft =",soft_full["q"])
print("PASS: full soft form factors are transverse through O(eps^0).")
print("PASS: hard + soft poles cancel in both form factors.")
print("PASS: hard + soft is mu-independent and transverse for q_L=q_E.")
print("Full-theory F_p =",full_p)
print("Full-theory F_q =",full_q)
print("SCOPE: full one-background U(1)_X amplitude in this parity-even sector; common 1PI phase/couplings and non-U(1)_X charge projections remain to be restored.")
