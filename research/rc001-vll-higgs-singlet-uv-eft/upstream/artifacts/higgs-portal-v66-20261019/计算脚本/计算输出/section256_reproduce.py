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


from itertools import product,combinations
from collections import Counter
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
print("Arithmetic: Fraction polynomials; exact Gaussian-rational spinor contractions")

# GRAPH_ENUMERATION
edges={("L","E"):("y","H"),("E","L"):("yc","Hc"),
       ("E","R"):("lambda","S"),("R","E"):("lambdac","Sc")}
conjugate={"H":"Hc","Hc":"H","S":"Sc","Sc":"S"}
walks=[]
graphs=[]
for interior in product(("L","E","R"),repeat=3):
    states=("L",)+interior+("R",)
    if not all((a,b) in edges for a,b in zip(states,states[1:])):
        continue
    scalars=[edges[(a,b)][1] for a,b in zip(states,states[1:])]
    walks.append(states)
    for i,j in combinations(range(4),2):
        external=[scalars[k] for k in range(4) if k not in (i,j)]
        if conjugate[scalars[i]]!=scalars[j] or sorted(external)!=["H","S"]:
            continue
        if (i,j)==(0,1):
            kind="external-L two-point"
        elif (i,j)==(2,3):
            kind="external-R two-point"
        elif (i,j)==(1,2):
            kind="heavy kinetic insertion at p=0"
        else:
            kind="proper direct vertex"
        graphs.append((states,(i+1,j+1),kind))
truth("all four-Yukawa open walks enumerated",len(walks)==2)
truth("all allowed conjugate scalar pairings enumerated",len(graphs)==4)
truth("no proper direct four-Yukawa vertex",all(g[2]!="proper direct vertex" for g in graphs))
truth("both heavy kinetic insertions retained before p=0",sum(g[2].startswith("heavy") for g in graphs)==2)
for g in graphs:
    print("YUKAWA_GRAPH",g)
quartics={"lambdaH":["H","H","Hc","Hc"],
          "lambdaS":["S","S","Sc","Sc"],
          "lambdaP":["H","Hc","S","Sc"]}
target=Counter(["H","S","Hc","Sc"])
admissible=[key for key,slots in quartics.items() if Counter(slots)==target]
truth("only portal quartic connects both Yukawa scalar legs",admissible==["lambdaP"])

# PORTAL_INTEGRAL
UV,IR,L,eps,xi,h,l,r,lp=map(P,["UV","IR","L","eps","xi","h","l","r","lambdaP"])
U=UV-L+1
J=IR-L+1
portal=lp*J
soft=-lp*(UV-L-P("logrho"))
check("portal hard/soft pole cancellation",portal.coeff("IR",1)+soft.coeff("UV",1))
check("portal full IR reconstruction",portal.subs("IR",UV)+soft,lp*(1+P("logrho")))
check("portal finite Wilson threshold",portal.subs("IR",0),lp*(1-L))
rrsym,logrrsym=map(P,["rho","logrho"])
check("regulated triangle from derivative of B0",(logrrsym+1)*(1-rrsym)+rrsym*logrrsym,logrrsym+1-rrsym)

# GAUGE_DIAGRAMS
d_eff=3+xi-2*eps
dH=l-h
dS=h-r
table={
    "EE":-d_eff*h**2*U,
    "LE": d_eff*l*h*U,
    "RE": d_eff*r*h*U,
    "LR":-d_eff*l*r*J,
    "HE":-xi*h*dH*U,
    "SE": xi*h*dS*U,
    "HR": xi*r*dH*J,
    "SL":-xi*l*dS*J,
    "HS": xi*dH*dS*J,
    "LH":P(),
    "RS":P()
}
raw=sum(table.values(),P())
UVpole=raw.coeff("eps",0).coeff("UV",1)
IRpole=raw.coeff("eps",0).coeff("IR",1)
finite=raw.coeff("eps",0).subs("UV",0).subs("IR",0)
finite+=raw.coeff("eps",1).coeff("UV",1)+raw.coeff("eps",1).coeff("IR",1)
A=-h**2+h*(l+r)
check("gauge hard UV pole",UVpole,3*A+xi*h**2)
check("gauge hard IR pole",IRpole,-3*l*r-xi*h**2)
check("gauge common pole",UVpole+IRpole,3*dH*dS)
check("gauge finite sum including epsilon times poles",finite,dH*dS*(1-3*L))
check("gauge parameter cancels from finite matching",finite.derivative("xi"))
check("gauge parameter cancels from common pole",(UVpole+IRpole).derivative("xi"))
check("universal vector charge limit",finite.subs("l",h).subs("r",h))
check("neutral H scalar limit",finite.subs("l",h))
check("neutral S scalar limit",finite.subs("r",h))
for name,value in table.items():
    print("GAUGE_KERNEL",name,str(value))
print("GAUGE_FINITE",str(finite))

# MODEL AND KINETIC MIXING
gy,gx,gw,kappa=map(P,["gY","gX","g2","kappa"])
for sign in (1,-1):
    check(f"flavor s={sign} hypercharge gauge matching",finite.subs("h",-gy).subs("l",-gy*F(1,2)).subs("r",-gy))
    check(f"flavor s={sign} X gauge matching",finite.subs("h",sign*gx).subs("l",sign*gx).subs("r",-sign*gx))
    # Numerator of deltaH^T K^{-1} deltaS; det K=1-kappa^2.
    vecH=[gy*F(1,2),P()]
    vecS=[P(),2*sign*gx]
    knum=[[P(1),-kappa],[-kappa,P(1)]]
    cross=sum((vecH[a]*knum[a][b]*vecS[b] for a in range(2) for b in range(2)),P())
    check(f"flavor s={sign} tree kinetic mixing gauge numerator",cross,-sign*kappa*gy*gx)
check("weak gauge hard block",finite.subs("h",0).subs("l",gw).subs("r",0))

# PARAMETER RENORMALIZATION AND RG CONTROL
u,v,Us,Vs=map(P,["u","v","Usum","Vsum"])
ZL=-u*F(1,2)
ZR=-v*F(1,2)
ZH=-Us
ZS=-Vs
ZER=-u
ZEL=-v*F(1,2)
cty=-(ZL+ZH+ZER)*F(1,2)
ctl=-(ZR+ZS+ZEL)*F(1,2)
ctm=-(ZEL+ZER)*F(1,2)
ctC=cty+ctl-ctm
check("UV pure-Yukawa parameter counterterm",ctC,(Us+Vs)*F(1,2)+(u+v)*F(1,4))
check("pure-Yukawa tree-amplitude counterterms cancel",ctC+(ZH+ZS+ZL+ZR)*F(1,2))
field=-(Us+Vs)*(F(1,2)-L)*F(1,2)-(u+v)*(F(3,4)-L*F(1,2))*F(1,2)
betaUV=2*ctC
check("pure-Yukawa matching logarithm obeys RG",betaUV-2*field.derivative("L"))
ctCgUV=-(l**2+r**2)*F(3,2)
ctCgE=ctCgUV+3*dH*dS
eft_gauge_loop=(3+xi)*l*r+xi*(-r*dH+l*dS-dH*dS+l*dH-r*dS)
light_halfZ=-xi*(l**2+r**2)*F(1,2)+(3-xi)*(dH**2+dS**2)*F(1,2)
uv_full_loop=UVpole+xi*(l*dH-r*dS)
check("EFT gauge coefficient counterterm derived from six contact exchanges",-eft_gauge_loop-light_halfZ,ctCgE)
check("UV gauge parameter counterterm derived from full proper amplitude",-uv_full_loop-light_halfZ,ctCgUV)
check("gauge UV/EFT counterterm difference",ctCgE-ctCgUV,UVpole+IRpole)
check("gauge matching logarithm obeys RG",2*ctCgE-2*ctCgUV,-2*finite.derivative("L"))
check("portal matching logarithm obeys RG",2*lp,-2*(lp*(1-L)).derivative("L"))
check("single-flavor degenerate-scale finite wave correction",field.subs("Usum",u).subs("Vsum",v).subs("L",0),-(u+v)*F(5,8))
check("total zero-mixing C5 correction",field+portal.subs("IR",0),field+lp*(1-L))

class G:
    def __init__(self,a=0,b=0):
        if isinstance(a,G):
            self.a,self.b=a.a,a.b
        else:
            self.a,self.b=F(a),F(b)
    def __add__(self,other):
        o=G(other)
        return G(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):
        return G(-self.a,-self.b)
    def __sub__(self,other):
        return self+-G(other)
    def __rsub__(self,other):
        return G(other)+-self
    def __mul__(self,other):
        o=G(other)
        return G(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,other):
        o=G(other)
        return self.a==o.a and self.b==o.b

def eye(n):
    return [[G(int(i==j)) for j in range(n)] for i in range(n)]
def madd(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a))] for i in range(len(a))]
def scale(c,a):
    return [[G(c)*v for v in row] for row in a]
def mm(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),G()) for j in range(n)] for i in range(n)]
def mcheck(name,a,b):
    global count
    assert all(a[i][j]==b[i][j] for i in range(len(a)) for j in range(len(a))),name
    count+=1
    print(f"PASS {count:02d} {name}")
phase=G(0,-1)*G(0,-1)*G(0,1)*G(0,1)
assert phase==G(1)
count+=1
print(f"PASS {count:02d} open-line (-i)^2*i^2 exact Gaussian phase")
I=eye(4)
zero=scale(0,I)
g0=[[G(int(i==j)*(1 if i<2 else -1)) for j in range(4)] for i in range(4)]
sigmas=[[[G(0),G(1)],[G(1),G(0)]],
        [[G(0),G(0,-1)],[G(0,1),G(0)]],
        [[G(1),G(0)],[G(0),G(-1)]]]
gammas=[g0]
for sigma in sigmas:
    g=[[G() for j in range(4)] for i in range(4)]
    for i in range(2):
        for j in range(2):
            g[i][j+2]=sigma[i][j]
            g[i+2][j]=-sigma[i][j]
    gammas.append(g)
g5=scale(G(0,1),mm(mm(mm(gammas[0],gammas[1]),gammas[2]),gammas[3]))
PL=scale(F(1,2),madd(I,scale(-1,g5)))
PR=scale(F(1,2),madd(I,g5))
mcheck("left projector idempotence",mm(PL,PL),PL)
mcheck("right projector idempotence",mm(PR,PR),PR)
mcheck("left-external heavy mass numerator vanishes",mm(PR,PL),zero)
mcheck("right-external heavy mass numerator vanishes",mm(PL,PR),zero)
for a,g in enumerate(gammas):
    mcheck(f"left-external slash numerator component {a}",mm(mm(PR,g),PL),mm(g,PL))
    mcheck(f"right-external slash numerator component {a}",mm(mm(PL,g),PR),mm(g,PR))



truth("portal (-i)^3*i^3 relative phase",(G(0,-1)*G(0,-1)*G(0,-1)*G(0,1)*G(0,1)*G(0,1))==G(1))

# Gauged open-chain numerators at k=(2,0,0,0), M=3.
# Dimensional d dependence is kept analytically in the table above.
def chain(*items):
    out=I
    for item in items:
        out=mm(out,item)
    return out
km=2
mass=3
kslash=scale(km,gammas[0])
prop=madd(kslash,scale(mass,I))
negativeprop=madd(scale(-1,kslash),scale(mass,I))
def contracted(fun):
    result=scale(0,I)
    for mu in range(4):
        result=madd(result,scale(1 if mu==0 else -1,fun(gammas[mu])))
    return result
ff={
 "EE":(lambda a:chain(PR,scale(mass,I),a,prop,a,scale(mass,I),PR),mass**3),
 "LE":(lambda a:chain(a,kslash,PR,prop,a,scale(mass,I),PR),mass*km**2),
 "RE":(lambda a:chain(PR,scale(mass,I),a,prop,PR,kslash,a),mass*km**2),
 "LR":(lambda a:chain(a,kslash,PR,prop,PR,kslash,a),mass*km**2)
}
for name,(fun,fac) in ff.items():
    mcheck(name+" fermion numerator metric",contracted(fun),scale(4*fac,PR))
    mcheck(name+" fermion numerator longitudinal",scale(F(1,km**2),fun(kslash)),scale(fac,PR))
mixed={
 "HE":(chain(PR,negativeprop,kslash,scale(mass,I),PR),-mass*km**2),
 "SE":(chain(PR,scale(mass,I),kslash,prop,PR),mass*km**2),
 "HR":(chain(PR,negativeprop,PR,scale(-1,kslash),kslash),-mass*km**2),
 "SL":(chain(kslash,kslash,PR,prop,PR),mass*km**2),
 "HS":(scale(-km**2,chain(PR,prop,PR)),-mass*km**2)
}
for name,(actual,fac) in mixed.items():
    mcheck(name+" scalar-contracted numerator",actual,scale(fac,PR))

def simpson(fun,n=16384):
    total=fun(0.0)+fun(1.0)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*fun(i/n)
    return total/(3*n)
print("NUMERICAL regulated portal integral, Simpson n=16384:")
for rr in [0.05,0.1,0.2]:
    direct=simpson(lambda x:-(1-x)/(x+(1-x)*rr))
    exact=(log(rr)+1-rr)/(1-rr)**2
    assert abs(direct-exact)<1e-10,(rr,direct,exact)
    print(f"INTEGRAL r={rr:.2f}, direct={direct:.12f}, exact={exact:.12f}")
print("NUMERICAL portal hard remainder, Decimal precision=50:")
with localcontext() as ctx:
    ctx.prec=50
    errors=[]
    for rr in [D("1e-2"),D("1e-3"),D("1e-4")]:
        exact=(rr.ln()+1-rr)/(1-rr)**2
        hard=exact-rr.ln()
        errors.append(abs(hard-1))
        assert errors[-1]<3*rr*abs(rr.ln())
        print(f"HARD_LIMIT r={rr}, full-minus-soft={hard:.15f}, target=1")
    assert errors[2]<errors[1]<errors[0]
print(f"RESULT: {count} exact graph/symbolic/matrix checks passed; 3 integrals and 3 high-precision hard limits passed")
print("C5 direct/C5 tree = q0*[lambdaP*(1-L)+deltaH.Kinv.deltaS*(1-3*L)]")
print("Pure-Yukawa direct zero; all four light-field factors included separately.")
print("No FeynArts/FeynCalc, Matchete, matchmakereft, or external diagram generator was run.")
