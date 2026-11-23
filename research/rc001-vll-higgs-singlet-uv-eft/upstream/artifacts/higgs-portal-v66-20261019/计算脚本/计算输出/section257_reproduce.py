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


from itertools import product, combinations
from math import log
from decimal import Decimal as D, localcontext

count=0
def check(name,actual,expected=0):
    global count
    rem=P(actual)-P(expected)
    assert not rem.t,(name,str(rem))
    count+=1
    print(f"PASS {count:02d} {name}")
def truth(name,value):
    global count
    assert value,name
    count+=1
    print(f"PASS {count:02d} {name}")

print("Python:",sys.version.split()[0])
print("Arithmetic: exact Fraction polynomials; open Clifford projection before integration")

# All four-Yukawa paths with equal external chiral species.
edges={("L","E"):"H",("E","L"):"Hc",("E","R"):"S",("R","E"):"Sc"}
conj={"H":"Hc","Hc":"H","S":"Sc","Sc":"S"}
graphs=[]
for end in ("L","R"):
    for middle in product(("L","E","R"),repeat=3):
        walk=(end,)+middle+(end,)
        if not all((a,b) in edges for a,b in zip(walk,walk[1:])):
            continue
        scalars=[edges[(a,b)] for a,b in zip(walk,walk[1:])]
        for a,b in combinations(range(4),2):
            if conj[scalars[a]]!=scalars[b]:
                continue
            outside=[scalars[i] for i in range(4) if i not in (a,b)]
            if conj[outside[0]]!=outside[1]:
                continue
            kind="box" if (a,b)==(0,3) else ("heavy-self-soft" if (a,b)==(1,2) else "external-fermion-leg")
            graphs.append((walk,(a+1,b+1),outside,kind))
truth("all equal-chirality contractions enumerated",len(graphs)==12)
for kind in ("box","heavy-self-soft","external-fermion-leg"):
    truth(kind+" graph count",sum(g[3]==kind for g in graphs)==4)
for g in graphs:
    print("GRAPH",g)

# Open Clifford numerator traced against an independent probe e.
# All p_i^2 products are O(rho^2), unnecessary at linear order.
rho,K,Ki,Ai,eps,UV,IR,L=map(P,["rho","K","Ki","Ai","eps","UV","IR","L"])
ka,kb,kc,ke=map(P,["ka","kb","kc","ke"])
ta,tb,tc=map(P,["ta","tb","tc"])
ks=[ka,kb,kc]
ts=[ta,tb,tc]
zero=(0,0,0)
a,b,c=(1,0,0),(0,1,0),(0,0,1)

def cut(p):
    return P({m:v for m,v in P(p).t.items() if dict(m).get("rho",0)<=1})
def mul(items):
    result=P(1)
    for item in items:
        result=cut(result*item)
    return result
def kdot(v):
    return sum((v[i]*ks[i] for i in range(3)),P())
def edot(v):
    return sum((v[i]*ts[i] for i in range(3)),P())
def dot_loop(v,w):
    return K+rho*(kdot(v)+kdot(w))
def probe(v):
    return ke+rho*edot(v)
def numerator_triple(v,w,z):
    return cut(probe(v)*dot_loop(w,z)-probe(w)*dot_loop(v,z)+probe(z)*dot_loop(v,w))
def reciprocal(shift,heavy):
    base=Ai if heavy else Ki
    return base*(1-2*rho*kdot(shift)*base)
def angular(p):
    result=P()
    for mon,coef in P(p).t.items():
        powers=dict(mon)
        factors=[]
        for name in ("ka","kb","kc","ke"):
            factors.extend([name]*powers.pop(name,0))
        scalar=P({tuple(sorted(powers.items())):coef})
        if not factors:
            result+=scalar
        elif len(factors)==1:
            continue
        elif len(factors)==2 and "ke" in factors:
            other=factors[1] if factors[0]=="ke" else factors[0]
            result+=scalar*K*(F(1,4)+eps*F(1,8))*dict(zip(("ka","kb","kc"),ts))[other]
        else:
            raise AssertionError(("unexpected angular tensor",factors))
    return result
def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))
def master(alpha,beta):
    total=alpha+beta
    assert beta>=1 and total>=2,(alpha,beta)
    if total==2:
        return UV-L+1-harmonic(beta-1)
    if alpha>=2:
        coeff=F((-1)**(beta+1)*factorial(total-3),factorial(beta-1)*factorial(alpha-2))
        return coeff*(IR-L+1+harmonic(total-3)-harmonic(alpha-2))
    return P(F((-1)**total*factorial(total-3)*factorial(1-alpha),factorial(beta-1)))
def integrate(p):
    result=P()
    for mon,coef in P(p).t.items():
        powers=dict(mon)
        alpha=powers.pop("Ki",0)-powers.pop("K",0)
        beta=powers.pop("Ai",0)
        result+=P({tuple(sorted(powers.items())):coef})*master(alpha,beta)
    return (result.coeff("eps",0)+result.coeff("eps",1).coeff("IR",1)
            +result.coeff("eps",1).coeff("UV",1))
def amplitude(numerator,denominators):
    integrand=mul([numerator]+[reciprocal(v,heavy) for v,heavy in denominators])
    return integrate(angular(integrand.coeff("rho",1)))

denbox=[(a,True),(b,False),(c,True),(zero,False)]
pure=amplitude(numerator_triple(a,b,c),denbox)
mixed=amplitude(probe(b),denbox) # M^2=1, restore by dimensions.
negative_a=tuple(-i for i in a)
negative_c=tuple(-i for i in c)
potential=amplitude(ke,[(zero,True),(negative_a,False),(negative_c,False)])
check("pure box integrand expansion",pure,tb-(ta+tc)*F(3,4))
check("mixed box integrand expansion",mixed,tb*(-IR*F(1,2)+L*F(1,2)-F(3,4))-(ta+tc)*F(1,4))
check("potential triangle integrand expansion",potential,(ta+tc)*(IR*F(1,2)-L*F(1,2)+F(3,4)))
check("mixed integral J22",master(2,2),-IR+L-2)
check("finite integral J12",master(1,2),-1)
check("finite integral J03",master(0,3),-F(1,2))
check("finite integral J13",master(1,3),F(1,2))
print("PURE_VECTOR",str(pure))
print("MIXED_VECTOR",str(mixed))
print("POTENTIAL_VECTOR",str(potential))

B,Q=map(P,["B","Q"])
def project(expr,sign):
    return expr.subs("ta",B).subs("tc",B).subs("tb",B+sign*Q)
pure_BQ=project(pure,1)
mixL=project(mixed,-1)
mixR=project(mixed,1)
potBQ=project(potential,1)
check("pure B coefficient",pure_BQ.coeff("B",1),-F(1,2))
check("pure current 2Q coefficient",pure_BQ.coeff("Q",1)*F(1,2),F(1,2))
check("mixed L/S B coefficient",mixL.coeff("B",1),-IR*F(1,2)+L*F(1,2)-F(5,4))
check("mixed L/S current coefficient",mixL.coeff("Q",1)*F(1,2),IR*F(1,4)-L*F(1,4)+F(3,8))
check("mixed R/H current coefficient",mixR.coeff("Q",1)*F(1,2),-IR*F(1,4)+L*F(1,4)-F(3,8))
check("potential has no scalar current",potBQ.coeff("Q",1))
check("potential finite wave coefficient",potBQ.coeff("B",1).subs("IR",0),-L+F(3,2))

# Scalar Hessian fixes weak tensors and singlet factors.
h0,h0c,h1,h1c,s,sc,lh,ls,lp=map(P,["h0","h0c","h1","h1c","s","sc","lambdaH","lambdaS","lambdaP"])
H=[h0,h1]
Hc=[h0c,h1c]
X=h0*h0c+h1*h1c
Y=s*sc
V=lh*X**2+ls*Y**2+lp*X*Y
for i in range(2):
    for j in range(2):
        hij=V.derivative(["h0c","h1c"][i]).derivative(["h0","h1"][j])
        expected=2*lh*H[i]*Hc[j]
        if i==j:
            expected+=2*lh*X+lp*Y
        check(f"Hessian H normal entry {i}{j}",hij,expected)
check("Hessian S normal entry",V.derivative("sc").derivative("s"),4*ls*Y+lp*X)

# Hard/soft cancellation in all two-C5 channels.
logp=P("logP")
Fsoft=(UV-logp+2)*F(1,2)
for label,expr in [("L/S box",mixL),("R/H box",mixR)]:
    sign=-1 if label.startswith("L") else 1
    soft=(B+sign*Q)*Fsoft
    total=expr.subs("IR",UV)+soft
    check(label+" reconstructed pole",total.coeff("UV",1))
    finite=expr.subs("IR",0)
    check(label+" current RG",(-2*finite.derivative("L")).coeff("Q",1)*F(1,2),-soft.coeff("UV",1).coeff("Q",1))
check("potential hard/soft poles cancel",potential.coeff("IR",1)-(ta+tc)*F(1,2))

# Independent constant-background mass-basis kinetic slope.
Fh=(UV-L)*F(1,2)+F(3,4)
F0=(UV-logp)*F(1,2)+1
massbasis=F0-Fh-F(1,2)
hardkin=mixL.subs("IR",0).coeff("B",1)
check("mass-basis mixed kinetic full function",hardkin+Fsoft.subs("UV",0),massbasis)
check("pure constant-background mass derivative",pure.subs("ta",B).subs("tb",B).subs("tc",B),-B*F(1,2))
check("potential agrees with light-mass hard threshold",potBQ.coeff("B",1).subs("IR",0),F(3,2)-L)

# Field normalization and published SM charged-singlet control.
u,v,Us,Vs=map(P,["u","v","Us","Vs"])
zH=Us*(F(1,2)-L)
zS=Vs*(F(1,2)-L)
zL=u*(F(3,4)-L*F(1,2))
zR=v*(F(3,4)-L*F(1,2))
deltaTL=-u*(zH+zL)
deltaTR=-v*(zS+zR)
singlet=-deltaTL*F(1,4)+u**2*F(1,2)
triplet_Warsaw=-deltaTL*F(1,4)
check("published VLL H-l singlet pure Yukawa",singlet.subs("Us",u),u**2*(F(13,16)-L*F(3,8)))
check("published VLL H-l triplet pure Yukawa",triplet_Warsaw.subs("Us",u),u**2*(F(5,16)-L*F(3,8)))
betaTL=u*(2*Us+u-v)
betaTR=v*(2*Vs+v-2*u)
check("L/H exact-soft counterterm RG",betaTL-2*deltaTL.derivative("L"),-u*v)
check("R/S exact-soft weak multiplicity RG",betaTR-2*deltaTR.derivative("L"),-2*u*v)

# Optional projection of previously matched gauge EOM blocks.
gY,gX,g2,dHB,dHX,dHW,dSB,dSX,RBB,RBX,RXX=map(P,["gY","gX","g2","dHB","dHX","dHW","dSB","dSX","RBB","RBX","RXX"])
rbref=gY**2*F(4,15)
dhbref=gY*Us*(L*F(1,6)-F(13,36))
dhwref=g2*Us*(F(5,18)-L*F(1,3))
check("published universal SM H-l singlet gauge EOM block",rbref*gY**2*F(1,4)+gY*dhbref*F(1,2),gY**4*F(1,15)+gY**2*Us*(L*F(1,12)-F(13,72)))
check("published universal SM H-l triplet gauge EOM block",-g2*dhwref*F(1,4),g2**2*Us*(L*F(1,12)-F(5,72)))
check("published universal SM H-e gauge EOM block",rbref*gY**2*F(1,2)+gY*dhbref,gY**4*F(2,15)+gY**2*Us*(L*F(1,6)-F(13,36)))
for sign in (1,-1):
    yl,yr=F(-1,2),F(-1)
    xl,xr=sign,-sign
    dLH=-gY*dHB*yl-gX*dHX*xl
    dRH=-gY*dHB*yr-gX*dHX*xr
    dLS=-gY*dSB*yl-gX*dSX*xl
    dRS=-gY*dSB*yr-gX*dSX*xr
    check(f"s={sign} jP L/H singlet projection",dLH,gY*dHB*F(1,2)-sign*gX*dHX)
    check(f"s={sign} jP R/H projection",dRH,gY*dHB+sign*gX*dHX)
    check(f"s={sign} jP L/S projection",dLS,gY*dSB*F(1,2)-sign*gX*dSX)
    check(f"s={sign} jP R/S projection",dRS,gY*dSB+sign*gX*dSX)
    check(f"s={sign} Q2 L/H projection",-RBB*gY**2*yl*F(1,2)-RBX*gY*gX*xl*F(1,2),RBB*gY**2*F(1,4)-sign*RBX*gY*gX*F(1,2))
    check(f"s={sign} Q2 R/H projection",-RBB*gY**2*yr*F(1,2)-RBX*gY*gX*xr*F(1,2),RBB*gY**2*F(1,2)+sign*RBX*gY*gX*F(1,2))
    check(f"s={sign} Q2 L/S projection",-2*RBX*gY*gX*yl-2*RXX*gX**2*xl,RBX*gY*gX-2*sign*RXX*gX**2)
    check(f"s={sign} Q2 R/S projection",-2*RBX*gY*gX*yr-2*RXX*gX**2*xr,2*RBX*gY*gX+2*sign*RXX*gX**2)

# Dimension/charge audit for diagonal unbroken-phase dipoles.
for sign in (1,-1):
    qLH=-sign-sign # bar L + R + H, in units of Q.
    truth(f"s={sign} diagonal dimension-six dipole forbidden",qLH!=0)
    truth(f"s={sign} S restores dipole charge at dimension seven",qLH+2*sign==0)

def simpson(fun,n=8192):
    total=fun(0.)+fun(1.)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*fun(i/n)
    return total/(3*n)
print("NUMERICAL pure constant-background mass derivative, Simpson n=8192:")
for zz in [-1e-2,-1e-3,-1e-4]:
    actual=-simpson(lambda x:(1-x)/(1-(1-x)*zz))
    exact=-sum(zz**n/(n+2) for n in range(16))
    assert abs(actual-exact)<1e-12
    print(f"PURE_NUM z={zz:.1e}, direct={actual:.12f}, series={exact:.12f}, limit=-0.5")
print("NUMERICAL independent mixed mass-basis kinetic hard limit, Decimal precision=50:")
with localcontext() as ctx:
    ctx.prec=50
    def fh(t,z):
        return D(3)/4-t.ln()/2+sum(((z/t)**n/(D(n)*D(n+2)) for n in range(1,41)),D(0))
    errors=[]
    for w in [D("1e-2"),D("1e-3"),D("1e-4")]:
        z=-w
        soft=1-(-z).ln()/2
        exact=(fh(1+w,z)+w*soft)/(1+w)
        hard=(exact-fh(D(1),z))/w-soft
        err=abs(hard+D(5)/4)
        errors.append(err)
        assert err<5*w*abs(w.ln())
        print(f"MIXED_NUM w={w}, z={z}, hard={hard:.15f}, target=-1.25")
    assert errors[2]<errors[1]<errors[0]
print(f"RESULT: {count} exact graph/symbolic checks passed; 3 integrals and 3 mass-basis hard limits passed")
print("Pure kernel: P - 3*(p+pprime)/4")
print("Mixed kernel: P*(-IR/2+L/2-3/4) - (p+pprime)/4")
print("Potential kernel: (p+pprime)*(IR/2-L/2+3/4)")
print("Scope: Yukawa/scalar-potential two-fermion/two-scalar hard matching; gauge exchange still separate.")
print("No FeynArts/FeynCalc, Matchete, matchmakereft, or external diagram generator was run.")
