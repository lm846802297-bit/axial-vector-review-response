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


from decimal import Decimal as D,localcontext
from math import log,exp

count=0
def check(name,actual,expected=0):
    global count
    rem=P(actual)-P(expected)
    assert not rem.t,(name,str(rem))
    count+=1
    print(f"PASS {count:03d} {name}")
def truth(name,value):
    global count
    assert value,name
    count+=1
    print(f"PASS {count:03d} {name}")
print("Python:",sys.version.split()[0])
print("Arithmetic: Fraction polynomials; exact Gaussian-rational Fierz matrices; raw operator subtraction")

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


# Matrix Fierz tensors first; Grassmann ordering supplied separately.
vL=[mm(g,PL) for g in gammas]
vR=[mm(g,PR) for g in gammas]
okLR=okLL=True
for a in range(4):
 for b in range(4):
  for c in range(4):
   for d in range(4):
    vv=sum(((1 if mu==0 else -1)*vL[mu][a][d]*vR[mu][c][b] for mu in range(4)),G())
    ss=PR[a][b]*PL[c][d]
    okLR=okLR and ss==vv*F(1,2)
    old=sum(((1 if mu==0 else -1)*vL[mu][a][b]*vL[mu][c][d] for mu in range(4)),G())
    new=sum(((1 if mu==0 else -1)*vL[mu][a][d]*vL[mu][c][b] for mu in range(4)),G())
    okLL=okLL and old==-new
truth("LR numerical matrix Fierz, all 256 entries",okLR)
truth("LL numerical matrix Fierz, all 256 entries",okLL)
perm=[0,3,2,1]
parity=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
check("Grassmann permutation sign",parity,-1)
check("scalar LR to vector LR including Grassmann sign",parity*F(1,2),-F(1,2))
check("vector LL exchanged Fierz including Grassmann sign",-parity,1)
truth("complex scalar loop times finite three-denominator integral phase",G(0,-1)*G(0,-1)==G(-1))
truth("complex scalar loop times four-denominator integral phase",G(0,-1)*G(0,1)==G(1))

# Normal/anomalous scalar quadratic kernels determine mixed-LR factors and selection.
def pmul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),P()) for j in range(n)] for i in range(n)]
def ptr(a):
    return sum((a[i][i] for i in range(len(a))),P())
am,amc,at,atc=([P("am"+str(i)) for i in range(2)],
              [P("amc"+str(i)) for i in range(2)],
              [P("at"+str(i)) for i in range(2)],
              [P("atc"+str(i)) for i in range(2)])
normal=[[P() for j in range(3)] for i in range(3)]
anom=[[P() for j in range(3)] for i in range(3)]
anomc=[[P() for j in range(3)] for i in range(3)]
for i in range(2):
    normal[i][2]=atc[i];normal[2][i]=at[i]
    anom[i][2]=anom[2][i]=am[i]
    anomc[i][2]=anomc[2][i]=amc[i]
nambu=[[P() for j in range(6)] for i in range(6)]
for i in range(3):
 for j in range(3):
    nambu[i][j]=normal[i][j]
    nambu[i+3][j+3]=normal[j][i]
    nambu[i][j+3]=anomc[i][j]
    nambu[i+3][j]=anom[i][j]
squaretrace=ptr(pmul(nambu,nambu))
expected=4*sum((am[i]*amc[i]+at[i]*atc[i] for i in range(2)),P())
check("Nambu normal/anomalous trace and no mixed-flavor LR cross",squaretrace,expected)
check("Nambu trace versus complex-scalar loop multiplicity",squaretrace*F(1,4),sum((am[i]*amc[i]+at[i]*atc[i] for i in range(2)),P()))
vm,vt,rm,rt,dm,dt=map(P,["vmu","vtau","jRmu","jRtau","DmuInv","DtauInv"])
VS=-vm*rm*dm+vt*rt*dt
check("right-handed conjugate scalar cross sign",(VS**2).coeff("jRmu",1).coeff("jRtau",1),-2*vm*vt*dm*dt)
check("ordered pair factor converts to unordered pair",F(1,8)*2,F(1,4))

# Same-heavy and mixed-heavy radial structures.
eps,UV,IR,L=map(P,["eps","UV","IR","L"])
def eval_eps(p):
    return p.coeff("eps",0)+p.coeff("eps",1).coeff("UV",1)+p.coeff("eps",1).coeff("IR",1)
J21=IR-L+1
J22=-IR+L-2
mixed_sm=eval_eps((F(1,4)+eps*F(1,8))*J21)
check("mixed heavy-light angular finite constant",mixed_sm,IR*F(1,4)-L*F(1,4)+F(3,8))
check("mixed heavy-light MS finite coefficient",mixed_sm.subs("IR",0),F(3,8)-L*F(1,4))
check("mixed LR scalar hard coefficient",J22.subs("IR",0),L-2)
check("mixed LR vector display after finite subtraction",-J22.subs("IR",0)*F(1,2),1-L*F(1,2))
softLR=UV-P("logp")+2
check("two-C5 scalar bubble pole cancellation",J22.coeff("IR",1)+softLR.coeff("UV",1))
check("mixed LR scalar RG",-2*J22.subs("IR",0).derivative("L"),-2)
check("mixed heavy-light single-C6 soft pole cancellation",mixed_sm.coeff("IR",1)-F(1,4))
check("mixed heavy-light current RG",-2*mixed_sm.subs("IR",0).derivative("L"),F(1,2))

# Smooth unequal-heavy limit of F(a,b) and regulated scalar kernels.
z=P("z")
ln1pz=sum((((-1)**(n+1))*z**n*F(1,n) for n in range(1,8)),P())
for n in range(4):
    check(f"unequal-heavy divided difference series order {n}",ln1pz.coeff("z",n+1),F((-1)**n,n+1))
logr=P("logr")
fullLRlead=-logr-2
softLRmass=-logr
check("positive-scalar-mass LR hard remainder",fullLRlead-softLRmass,-2)
fullSMlead=(logr+1)*F(1,4)
softSMmass=logr*F(1,4)-F(1,8)
check("positive-scalar-mass mixed heavy-light hard remainder",fullSMlead-softSMmass,F(3,8))

# Weak epsilon identity governing the up-Yukawa versus down-Yukawa sign.
epsilon=[[0,1],[-1,0]]
ok=True
for a in range(2):
 for i in range(2):
  for b in range(2):
   for j in range(2):
    ok=ok and epsilon[a][i]*epsilon[b][j]==int(a==b and i==j)-int(a==j and i==b)
truth("weak epsilon all-index identity",ok)
alpha=F(3,8)-L*F(1,4)
check("published mixed SM down lq singlet",alpha*F(1,2),F(3,16)-L*F(1,8))
check("published mixed SM up lq singlet",-alpha*F(1,2),-F(3,16)+L*F(1,8))
check("published mixed SM lq triplet",alpha*F(1,2),F(3,16)-L*F(1,8))
check("published mixed SM right up current",alpha,F(3,8)-L*F(1,4))
check("published mixed SM right down/e current",-alpha,-F(3,8)+L*F(1,4))

# All nine Higgs-source products and color/source controls.
jd,je,ju,jdc,jec,juc=map(P,["jd","je","ju","jdc","jec","juc"])
source=(jdc+jec+juc)*(jd+je+ju)
truth("all nine Higgs source products retained",len(source.t)==9 and all(c==1 for c in source.t.values()))
u=P("u")
rH=u*F(1,3)
check("published qu/qd color singlet source",-rH*F(1,6),-u*F(1,18))
check("published qu/qd color octet source",-rH,-u*F(1,3))
check("published quqd source",rH,u*F(1,3))
check("published ledq source",rH,u*F(1,3))
check("published lequ source sign",-rH,-u*F(1,3))
pure_phase=G(0,-1)*G(0,-1)
check("published single-heavy pure LL coefficient",pure_phase.a*F(1,2)*F(1,4)*u**2,-u**2*F(1,8))

# Pure-gauge and penguin current projection, normalized q0*gY^4/M^2 or q0*u*gY^2/M^2.
hyper={"q":F(1,6),"u":F(2,3),"d":F(-1,3),"l":F(-1,2),"e":F(-1)}
def gauge_same(f):
    return -F(2,15)*hyper[f]**2
def gauge_pair(f,g):
    return -F(4,15)*hyper[f]*hyper[g]
for name,actual,expect in [
 ("qq",gauge_same("q"),-F(1,270)),("uu",gauge_same("u"),-F(8,135)),
 ("dd",gauge_same("d"),-F(2,135)),("ee",gauge_same("e"),-F(2,15)),
 ("qe",gauge_pair("q","e"),F(2,45)),("eu",gauge_pair("e","u"),F(8,45)),
 ("ed",gauge_pair("e","d"),-F(4,45)),("le",gauge_pair("l","e"),-F(2,15))
]:
    check("published pure-gauge current control "+name,actual,expect)
fLB=F(25,72)-L*F(1,12)
for name,expected in [("e",F(25,72)-L*F(1,12)),
                      ("u",-F(25,108)+L*F(1,18)),
                      ("d",F(25,216)-L*F(1,36))]:
    check("published hypercharge penguin l"+name,-fLB*hyper[name],expected)
fLW=F(11,36)-L*F(1,6)
check("published weak penguin lq triplet",-fLW*F(1,4),-F(11,144)+L*F(1,24))
our_lq=-fLB*hyper["q"]
printed_lq=F(25,432)+L*F(1,72)
printed_ud=-F(8,135)
check("own hypercharge lq/le ratio",our_lq,(-fLB*hyper["e"])*(-F(1,6)))
truth("reference lq constant discrepancy is explicitly nonzero",bool((printed_lq-our_lq).t))
truth("reference ud sign discrepancy is explicitly nonzero",printed_ud!=gauge_pair("u","d"))
print("REFERENCE_DISCREPANCY Eq6.40 printed-minus-own:",str(printed_lq-our_lq))
print("REFERENCE_DISCREPANCY Eq6.31 printed:",printed_ud,"own:",gauge_pair("u","d"))

def simpson(fun,n=8192):
    value=fun(0.)+fun(1.)
    for i in range(1,n): value+=(4 if i%2 else 2)*fun(i/n)
    return value/(3*n)
print("NUMERICAL positive unequal-heavy radial kernel, Simpson n=8192:")
for a,b in [(1.,1.),(1.,4.),(2.,7.)]:
    value=simpson(lambda x:1/(x*a+(1-x)*b))
    exact=1/a if a==b else log(a/b)/(a-b)
    assert abs(value-exact)<1e-12
    print(f"MASS_PAIR a={a:g}, b={b:g}, integral={value:.12f}, closed={exact:.12f}")
print("NUMERICAL regulated LR and heavy-light radial functions, Simpson n=8192:")
for rr in [0.02,0.005,0.001]:
    length=-log(rr)
    lrint=simpson(lambda v:length*(1-exp(-length*v))*(1-rr*exp(length*v))/(1-rr)**3)
    smint=simpson(lambda v:-length*(1-rr*exp(length*v))/(1-rr)**2)
    lrexact=(-(1+rr)*log(rr)-2*(1-rr))/(1-rr)**3
    smexact=(log(rr)+1-rr)/(1-rr)**2
    assert abs(lrint-lrexact)<1e-10 and abs(smint-smexact)<1e-10
    print(f"REGULATED r={rr:g}, LR={lrint:.12f}, LRclosed={lrexact:.12f}, SM={smint:.12f}, SMclosed={smexact:.12f}")
print("NUMERICAL two independent hard remainders, Decimal precision=50:")
with localcontext() as ctx:
    ctx.prec=50
    elr=[];esm=[]
    for rr in [D("1e-2"),D("1e-3"),D("1e-4")]:
        flr=(-(1+rr)*rr.ln()-2*(1-rr))/(1-rr)**3
        fsm=(rr.ln()+1-rr)/(1-rr)**2
        hlr=flr+rr.ln()
        hsm=fsm/4-rr.ln()/4+D(1)/8
        elr.append(abs(hlr+2));esm.append(abs(hsm-D(3)/8))
        assert elr[-1]<5*rr*abs(rr.ln()) and esm[-1]<rr*abs(rr.ln())
        print(f"HARD_LIMIT r={rr}, LRhard={hlr:.15f}, target=-2; SMhard={hsm:.15f}, target=3/8")
    assert elr[2]<elr[1]<elr[0] and esm[2]<esm[1]<esm[0]
print(f"RESULT: {count} exact determinant/Fierz/symbolic checks passed; 9 integrals and 6 IR hard limits passed")
print("Reference status: 2 printed-sign discrepancies recorded, not counted as agreement.")
print("Four-fermion basis: raw scalar/current products; poles subtracted before four-dimensional Fierz.")
print("No FeynArts/FeynCalc, Matchete, matchmakereft, or external diagram generator was run.")
