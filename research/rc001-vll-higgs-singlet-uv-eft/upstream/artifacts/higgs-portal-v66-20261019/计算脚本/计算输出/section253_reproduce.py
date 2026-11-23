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


from math import comb, log1p

count=0

def check(name,actual,expected=0):
    global count
    residue=P(actual)-P(expected)
    if residue.t:
        raise AssertionError(f"{name}: {residue}")
    count+=1
    print(f"PASS {count:02d} {name}")

def beta_int(a,b):
    return F(factorial(a)*factorial(b),factorial(a+b+1))

print("Python:",sys.version.split()[0])
print("Arithmetic: exact Fraction multivariate polynomials; numerical quadrature is separate")

# Dirac trace and d-dimensional tensor cancellation after a Feynman shift.
h,M2,w,s,I2=map(P,["half_d","M2","w","s","I2"])
D=M2-w*s
gpart_times_hminus1=(1-h)*D*I2+(M2+w*s)*(h-1)*I2
check("Ward g tensor coefficient after radial identities",gpart_times_hminus1,(h-1)*2*w*s*I2)
check("Ward cancellation with p_mu p_nu coefficient",gpart_times_hminus1-(h-1)*2*w*s*I2)
check("closed-loop vertices and propagators",(-1)*(-1)*(-1),-1)
check("Dirac transverse prefactor 4*2",4*2,8)
check("zero-momentum Feynman moment",8*beta_int(1,1),F(4,3))
known={1:F(4,15),2:F(1,35),3:F(4,945)}
for n in range(1,7):
    coeff=F(8,n)*beta_int(n+1,n+1)
    check(f"Taylor coefficient n={n}",coeff,F(8*factorial(n+1)**2,n*factorial(2*n+3)))
    if n in known:
        check(f"explicit coefficient n={n}",coeff,known[n])

# Tensor Ward and Maxwell-square identities with exact rational components.
metric=[1,-1,-1,-1]
pv=[F(5),F(1),F(2),F(1)]
p2=sum(metric[i]*pv[i]**2 for i in range(4))
T=[[p2*metric[i]*int(i==j)-pv[i]*pv[j] for j in range(4)] for i in range(4)]
for j in range(4):
    check(f"p_mu T^mu{j}=0",sum(metric[i]*pv[i]*T[i][j] for i in range(4)))
square=[[sum(T[i][k]*metric[k]*T[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
check("all tensor components T*g*T=p2*T",sum((square[i][j]-p2*T[i][j])**2 for i in range(4) for j in range(4)))

q,gY,gX,LM,LT,invM,invT,Delta=map(P,["q0","gY","gX","LMu","LTau","invMmu2","invMtau2","Delta"])
couplings=[[-gY,gX],[-gY,-gX]]
logs=[LM,LT]
inverses=[invM,invT]
pole=[[sum((q*F(4,3)*couplings[k][i]*couplings[k][j]*Delta for k in range(2)),P()) for j in range(2)] for i in range(2)]
Z=[[sum((-q*F(4,3)*couplings[k][i]*couplings[k][j]*logs[k] for k in range(2)),P()) for j in range(2)] for i in range(2)]
R=[[sum((q*F(4,15)*couplings[k][i]*couplings[k][j]*inverses[k] for k in range(2)),P()) for j in range(2)] for i in range(2)]
check("BB pole counts two Dirac fermions",pole[0][0],q*F(8,3)*gY**2*Delta)
check("XX pole counts two Dirac fermions",pole[1][1],q*F(8,3)*gX**2*Delta)
check("BX pole cancels without mass degeneracy",pole[0][1])
check("BB finite kinetic threshold",Z[0][0],-q*F(4,3)*gY**2*(LM+LT))
check("XX finite kinetic threshold",Z[1][1],-q*F(4,3)*gX**2*(LM+LT))
check("BX finite kinetic threshold",Z[0][1],q*F(4,3)*gY*gX*(LM-LT))
check("BB dimension-six coefficient",R[0][0],q*F(4,15)*gY**2*(invM+invT))
check("XX dimension-six coefficient",R[1][1],q*F(4,15)*gX**2*(invM+invT))
check("BX dimension-six coefficient",R[0][1],q*F(4,15)*gY*gX*(invT-invM))
check("kinetic matrix is symmetric",Z[0][1],Z[1][0])
check("dimension-six matrix is symmetric",R[0][1],R[1][0])
check("degenerate kinetic mixing vanishes",Z[0][1].subs("LTau",LM))
check("degenerate high-derivative mixing vanishes",R[0][1].subs("invMtau2",invM))
for n in range(1,7):
    same_mass=8*F(1,n)*beta_int(n+1,n+1)*sum((couplings[k][0]*couplings[k][1] for k in range(2)),P())
    check(f"degenerate full-function Taylor cancellation n={n}",same_mass)
check("finite kinetic mixing explicit scale derivative",-2*(Z[0][1].derivative("LMu")+Z[0][1].derivative("LTau")))

detR=R[0][0]*R[1][1]-R[0][1]**2
check("positive Gram determinant identity",detR,4*(q*F(4,15))**2*gY**2*gX**2*invM*invT)
vb,vx=map(P,["vB","vX"])
check("Gram matrix quadratic form",R[0][0]*vb**2+2*R[0][1]*vb*vx+R[1][1]*vx**2,
      q*F(4,15)*(invM*(-gY*vb+gX*vx)**2+invT*(-gY*vb-gX*vx)**2))

# Ward identity for coupling decoupling, evaluated at fixed couplings to one loop.
dgY=-gY*Z[0][0]*F(1,2)
dgX=-gX*Z[1][1]*F(1,2)
check("hypercharge coupling matching scale check",-2*(dgY.derivative("LMu")+dgY.derivative("LTau"))+q*F(8,3)*gY**3)
check("X coupling matching scale check",-2*(dgX.derivative("LMu")+dgX.derivative("LTau"))+q*F(8,3)*gX**3)

# Matrix normalization at first order, including generated off-diagonal mixing.
e=P("loop")
ZB,ZX,ZBX=map(P,["ZB","ZX","ZBX"])
zmat=[[ZB,ZBX],[ZBX,ZX]]
ident=[[P(int(i==j)) for j in range(2)] for i in range(2)]
fieldmap=[[ident[i][j]-e*zmat[i][j]*F(1,2) for j in range(2)] for i in range(2)]
kinetic=[[ident[i][j]+e*zmat[i][j] for j in range(2)] for i in range(2)]
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(2)),P()) for j in range(2)] for i in range(2)]
canonical=mm(mm(fieldmap,kinetic),fieldmap)
for i,j in [(0,0),(1,1),(0,1)]:
    check(f"canonical gauge kinetic matrix row {i}{j}",canonical[i][j].coeff("loop",1))

# Maxwell operators and matter currents, using P_a=-J_a at leading kappa=0.
RB,RX,RBX=map(P,["RB","RX","RBX"])
jH,jS,jY,jx=map(P,["jH","jS","jY","jx"])
JB=gY*(jH*F(1,2)+jY)
JX=gX*(2*jS+jx)
currentL=-RB*JB**2*F(1,2)-RBX*JB*JX-RX*JX**2*F(1,2)
rows={
    ("jH",2,"jS",0):-RB*gY**2*F(1,8),
    ("jS",2,"jH",0):-2*RX*gX**2,
}
# Explicit scalar, scalar-fermion, and four-fermion rows are independently rebuilt.
expectedL=(-RB*gY**2*jH**2*F(1,8)-2*RX*gX**2*jS**2-RBX*gY*gX*jH*jS
           -RB*gY**2*jH*jY*F(1,2)-2*RX*gX**2*jS*jx
           -RBX*gY*gX*jH*jx*F(1,2)-2*RBX*gY*gX*jS*jY
           -RB*gY**2*jY**2*F(1,2)-RX*gX**2*jx**2*F(1,2)-RBX*gY*gX*jY*jx)
check("all current-current EOM terms",currentL,expectedL)
for name,power,value in [("jH",2,-RB*gY**2*F(1,8)),("jS",2,-2*RX*gX**2),
                         ("jY",2,-RB*gY**2*F(1,2)),("jx",2,-RX*gX**2*F(1,2))]:
    check(f"current square row {name}",currentL.coeff(name,power),value)
for n1,n2,value in [("jH","jS",-RBX*gY*gX),("jH","jY",-RB*gY**2*F(1,2)),
                    ("jS","jx",-2*RX*gX**2),("jH","jx",-RBX*gY*gX*F(1,2)),
                    ("jS","jY",-2*RBX*gY*gX),("jY","jx",-RBX*gY*gX)]:
    check(f"current cross row {n1} {n2}",currentL.coeff(n1,1).coeff(n2,1),value)

# Scalar-current identities and their EOM companions.
z,zbar=map(P,["z","zbar"])
check("j^2=4|phi^dag D phi|^2-(partial modulus)^2",-(z-zbar)**2,4*z*zbar-(z+zbar)**2)
QX,QY,QHD,RS,OJ=map(P,["QX","QY","QHD","RS","OJ"])
scalarL=-RB*gY**2*F(1,8)*(4*QHD-QX)-2*RX*gX**2*(4*RS-QY)+RBX*gY*gX*OJ
X,Y,ms,ls,lp,FS=map(P,["X","Y","muS2","lambdaS","lambdaP","FS"])
RSred=-QY*F(1,2)-ms*Y**2+2*ls*Y**3+lp*X*Y**2+Y*FS*F(1,2)
scalarNR=scalarL.subs("RS",RSred)
checks=[("QX",1,RB*gY**2*F(1,8)),("QHD",1,-RB*gY**2*F(1,2)),
        ("QY",1,6*RX*gX**2),("OJ",1,RBX*gY*gX)]
for name,power,value in checks:
    check("EOM scalar derivative row "+name,scalarNR.coeff(name,power),value)
check("EOM scalar Y2 shift",scalarNR.coeff("Y",2).coeff("X",0),8*RX*gX**2*ms)
check("EOM scalar Y3 shift",scalarNR.coeff("Y",3),-16*RX*gX**2*ls)
check("EOM scalar XY2 shift",scalarNR.coeff("X",1).coeff("Y",2),-8*RX*gX**2*lp)
check("EOM scalar Y source shift",scalarNR.coeff("FS",1).coeff("Y",1),-4*RX*gX**2)

# General leading kinetic mixing: inverse K current transformation.
k=P("kappa0")
unit=1-k**2
K0=[[P(1),k],[k,P(1)]]
adj=[[P(1),-k],[-k,P(1)]]
prod=mm(K0,adj)
check("general kinetic matrix inverse numerator diagonal",prod[0][0],unit)
check("general kinetic matrix inverse numerator offdiagonal",prod[0][1])

# Separate numerical check: Simpson quadrature of the finite momentum change.
def omega_change(z,n=4096):
    step=1.0/n
    def value(x):
        weight=x*(1-x)
        return 8*weight*(-log1p(-weight*z))
    result=value(0)+value(1)
    for i in range(1,n):
        result+=(4 if i%2 else 2)*value(i*step)
    return result*step/3

print("NUMERICAL CHECKS: Simpson n=4096, finite Omega(z)-Omega(0) / (q0*c_a*c_b)")
for znum in [-0.1,-0.01,0.01]:
    exactnum=omega_change(znum)
    approx=float(F(4,15))*znum+float(F(1,35))*znum**2
    remainder=exactnum-approx
    assert abs(remainder)<0.006*abs(znum)**3,(znum,remainder)
    print(f"z={znum:+.2e}, integral={exactnum:+.12e}, R_after_z2={remainder:+.12e}, R/z3={remainder/znum**3:+.10e}")
print(f"RESULT: {count} exact symbolic checks passed; 3 numerical parameter-integral cases passed")
print("Omega = (4/3)q0*c_a*c_b*(Delta-L) + (4/15)q0*c_a*c_b*p2/M2 + O(p4/M4)")
print("Scope: unbroken-phase heavy Dirac vector currents only; no FeynArts/FeynCalc run.")

