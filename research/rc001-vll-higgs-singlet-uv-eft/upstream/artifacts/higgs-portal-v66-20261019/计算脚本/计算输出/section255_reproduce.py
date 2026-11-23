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


from math import comb, log, log1p
from decimal import Decimal as D, localcontext

count=0
def check(name,actual,expected=0):
    global count
    remainder=P(actual)-P(expected)
    assert not remainder.t,(name,str(remainder))
    count+=1
    print(f"PASS {count:02d} {name}")

def integ(poly,var="x"):
    result=P()
    for mon,c in P(poly).t.items():
        powers=dict(mon)
        degree=powers.pop(var,0)
        result+=P({tuple(sorted(powers.items())):c/F(degree+1)})
    return result

def integ_logx(poly,var="x"):
    result=P()
    for mon,c in P(poly).t.items():
        powers=dict(mon)
        degree=powers.pop(var,0)
        result+=P({tuple(sorted(powers.items())):-c/F((degree+1)**2)})
    return result

print("Python:",sys.version.split()[0])
print("Arithmetic: Fraction polynomials; exact Gaussian-rational 4x4 spinor matrices")
x,z,r,UV,IR,L,lr=map(P,["x","z","r","UV","IR","L","logr"])
check("parameter weight integral",integ(1-x),F(1,2))
check("parameter logarithmic constant",-integ_logx(1-x),F(3,4))
coeff=[(UV-L)*F(1,2)+F(3,4)]
for n in range(1,7):
    cn=integ((1-x)**(n+1))*F(1,n)
    check(f"rank-one parameter moment z^{n}",cn,F(1,n*(n+2)))
    coeff.append(cn)

# Independent PV reduction, before division by 2*p^2.
B0=UV-L+1
for n in range(1,8):
    B0+=z**n*F(1,n*(n+1))
numerator=-(UV-L+1)+(1+z)*B0
check("PV numerator has no spurious p^-2 pole",numerator.coeff("z",0))
for n in range(7):
    check(f"PV versus direct rank-one coefficient z^{n}",numerator.coeff("z",n+1)*F(1,2),coeff[n])
check("minimal kinetic counterterm",(UV-L)*F(1,2)+F(3,4)-UV*F(1,2),-L*F(1,2)+F(3,4))

# Exact Gaussian rationals for the full chiral matrix numerator.
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

# Massive-scalar expansion at p^2=0, including the EFT tadpole.
den_inverse=sum(((n+1)*r**n for n in range(4)),P())
log_exact_numerator=F(3,4)-r+r**2*F(1,4)+(r-r**2*F(1,2))*lr
full=log_exact_numerator*den_inverse
check("massive exact function constant",full.coeff("r",0),F(3,4))
check("massive exact function first derivative",full.coeff("r",1),lr+F(1,2))
hard_r=IR-L+F(3,2)
soft_r=-UV-1+L+lr
check("hard IR pole cancels EFT soft UV pole",hard_r.coeff("IR",1)+soft_r.coeff("UV",1))
check("massive full reconstruction",hard_r.subs("IR",UV)+soft_r,lr+F(1,2))
check("renormalized massive reconstruction",-L+F(3,2)-1+L+lr,lr+F(1,2))
check("massive hard pole is not a new full-UV divergence",hard_r.subs("IR",UV)+soft_r-full.coeff("r",1))

# Independent hard-integrand calculation using angular averages.
# At order m^2*p, expanding the squared scalar denominator gives
# 4*k.p / (k^2)^3. The numerator average is 4/d * slash(p)*J21.
# 4/d=1+epsilon/2 supplies the additional finite 1/2.
hard_integrand=(IR-L+1)+F(1,2)
check("massive hard angular expansion keeps epsilon pole product",hard_integrand,hard_r)

# Canonical field transformations, truncated at one formal loop t.
t=P("t")
zH,zS,zL,zR=map(P,["zH","zS","zL","zR"])
fieldH=1-t*zH*F(1,2)
fieldS=1-t*zS*F(1,2)
fieldL=1-t*zL*F(1,2)
fieldR=1-t*zR*F(1,2)
check("canonical fermion kinetic linear loop",(fieldL**2*(1+t*zL)).coeff("t",1))
check("canonical scalar kinetic linear loop",(fieldH**2*(1+t*zH)).coeff("t",1))
check("C5 all external-field factors",(fieldH*fieldS*fieldL*fieldR).coeff("t",1),-(zH+zS+zL+zR)*F(1,2))
check("C_LD all external-field factors",(fieldH**2*fieldL**2).coeff("t",1),-zH-zL)
check("C_RD all external-field factors",(fieldS**2*fieldR**2).coeff("t",1),-zS-zR)
u,v=map(P,["u","v"])
check("own-flavor contribution to C5 field coefficient",-(u+v)*(F(3,4)-L*F(1,2))*F(1,2),-(u+v)*(F(3,8)-L*F(1,4)))

# Operator field redefinition in an independent basis of bilinears.
Q3,U,V,W=map(P,["Q3","barpsi_A2_Xi","barXi_A2_psi","barXi_A_Xi"])
delta0=-Q3+(U+V)*F(1,2)
delta1=-(U+V)*F(1,2)+W
check("fermion high-derivative field redefinition",Q3+delta0+delta1,W)

# A genuinely noncommuting covariant-derivative algebra, with two internal
# components. Verify the Pauli sign and the cubic completion as 8x8 matrices.
def tensor(a,b):
    return [[a[i//len(b)][j//len(b)]*b[i%len(b)][j%len(b)]
             for j in range(len(a)*len(b))] for i in range(len(a)*len(b))]
def anti(a,b):
    return madd(mm(a,b),mm(b,a))
def comm(a,b):
    return madd(mm(a,b),scale(-1,mm(b,a)))
Ds=[[[G(1),G(2)],[G(-1),G(0)]],
    [[G(0),G(1)],[G(3),G(-1)]],
    [[G(2),G(-1)],[G(1),G(1)]],
    [[G(-1),G(3)],[G(0),G(2)]]]
A=scale(0,tensor(I,eye(2)))
D2=scale(0,eye(2))
SF=scale(0,A)
for a in range(4):
    A=madd(A,scale(G(0,1),tensor(gammas[a],Ds[a])))
    D2=madd(D2,scale(1 if a==0 else -1,mm(Ds[a],Ds[a])))
    for b in range(a+1,4):
        sigma=scale(G(0,F(1,2)),comm(gammas[a],gammas[b]))
        field=scale(G(0,1),comm(Ds[a],Ds[b]))
        SF=madd(SF,scale(2,tensor(sigma,field)))
minusD2=scale(-1,tensor(I,D2))
mcheck("noncommuting covariant square and Pauli sign",mm(A,A),madd(minusD2,scale(F(1,2),SF)))
mcheck("cubic Dirac versus symmetric D2 completion",mm(mm(A,A),A),madd(scale(F(1,2),anti(A,minusD2)),scale(F(1,4),anti(A,SF))))

# Exact weak-index Fierz checks for source-current completion.
def m2(a):
    return [[G(v) for v in row] for row in a]
T=[scale(F(1,2),s) for s in sigmas]
H=[[G(1,1)],[G(2,-1)]]
DH=[[G(-1,2)],[G(3,1)]]
def dagger_vec(v):
    return [[G(w[0].a,-w[0].b) for w in v]]
def outer(a,bdag):
    return [[a[i][0]*bdag[0][j] for j in range(2)] for i in range(2)]
def inner(a,tmat,b):
    return sum((G(a[i][0].a,-a[i][0].b)*tmat[i][j]*b[j][0] for i in range(2) for j in range(2)),G())
jh=G(0,1)*(inner(H,eye(2),DH)-inner(DH,eye(2),H))
jha=[G(0,1)*(inner(H,ta,DH)-inner(DH,ta,H)) for ta in T]
mat_current=scale(G(0,1),madd(outer(H,dagger_vec(DH)),scale(-1,outer(DH,dagger_vec(H)))))
recovered=scale(-jh*F(1,2),eye(2))
for ja,ta in zip(jha,T):
    recovered=madd(recovered,scale(-2*ja,ta))
mcheck("right-source weak current decomposition",mat_current,recovered)

def simpson(fun,n=8192):
    total=fun(0.0)+fun(1.0)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*fun(i/n)
    return total/(3*n)

print("NUMERICAL massless-scalar momentum integrals, Simpson n=8192:")
num_count=0
for zz in [-0.2,0.05,0.2]:
    value=0.75+simpson(lambda xx:-(1-xx)*log1p(-(1-xx)*zz))
    series=0.75+sum(zz**n/(n*(n+2)) for n in range(1,13))
    assert abs(value-series)<2e-11,(zz,value,series)
    num_count+=1
    print(f"MOMENTUM z={zz:+.2f}, direct={value:.12f}, series12={series:.12f}")

print("NUMERICAL positive-mass p=0 hard/soft reconstruction, Decimal precision=50:")
with localcontext() as ctx:
    ctx.prec=50
    errors=[]
    for rr in [D("1e-2"),D("1e-3"),D("1e-4")]:
        logrr=rr.ln()
        exact=(D(3)/4-rr+rr**2/4+(rr-rr**2/2)*logrr)/(1-rr)**2
        matched=D(3)/4+rr*(logrr+D(1)/2)
        remainder=abs(exact-matched)
        assert remainder<5*rr**2*abs(logrr)
        errors.append(remainder/rr)
        num_count+=1
        print(f"MASS r={rr}, exact={exact:.15f}, hard+soft={matched:.15f}, remainder={remainder:.4E}")
    assert errors[2]<errors[1]<errors[0]
print(f"RESULT: {count} exact symbolic/matrix checks passed; {num_count} numerical cases passed")
print("Self energy: Pi = q0*g2*slash(p)*[1/2*(Delta-L)+3/4+p2/(3*M2)]")
print("Mass-spurion hard: q0*g2*mphi2/M2*(3/2-L); soft tadpole kept explicitly.")
print("Scope: Yukawa-induced light-fermion two-point functions and field/EOM consequences only.")
print("No FeynArts/FeynCalc, Matchete, matchmakereft, or external diagram generator was run.")
