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


from itertools import permutations, combinations
from functools import lru_cache

rho,K,Ki,Ai,eps,UV,IR,L=map(P,["rho","K","Ki","Ai","eps","UV","IR","L"])
kv=list(map(P,["ka","kb","kc","ke"]))
gram=[[F(0),F(2),F(-1),F(0)],
      [F(2),F(0),F(-1),F(0)],
      [F(-1),F(-1),F(0),F(0)],
      [F(0),F(0),F(0),F(-1)]]
external={"A":(1,0,0),"B":(0,1,0),"C":(0,0,1),"D":(-1,-1,-1)}
E="polarization"

def cut(poly,n=2):
    return P({m:c for m,c in P(poly).t.items() if dict(m).get("rho",0)<=n})

def mul(items):
    out=P(1)
    for item in items:
        out=cut(out*item)
    return out

def vadd(v,w):
    return tuple(x+y for x,y in zip(v,w))

def dot_ext(v,w):
    return sum((F(v[i])*F(w[j])*gram[i][j] for i in range(3) for j in range(3)),F(0))

def kdot(v):
    return sum((v[i]*kv[i] for i in range(3)),P())

def dot(v,w):
    if v==E and w==E:
        return P(-1)
    if v==E or w==E:
        return kv[3]
    return K+rho*(kdot(v)+kdot(w))+rho**2*dot_ext(v,w)

@lru_cache(None)
def trace_normalized(vectors):
    if not vectors:
        return P(1)
    if len(vectors)%2:
        return P()
    first=vectors[0]
    out=P()
    for j in range(1,len(vectors)):
        rest=vectors[1:j]+vectors[j+1:]
        out+=mul([(-1)**(j-1),dot(first,vectors[j]),trace_normalized(rest)])
    return cut(out)

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))

def master(alpha,beta):
    assert beta>=1,(alpha,beta)
    total=alpha+beta
    if total==2:
        assert alpha<2
        return UV-L+1-harmonic(beta-1)
    assert total>=3,(alpha,beta)
    if alpha>=2:
        coefficient=F((-1)**(beta+1)*factorial(total-3),factorial(beta-1)*factorial(alpha-2))
        return coefficient*(IR-L+1+harmonic(total-3)-harmonic(alpha-2))
    return P(F((-1)**total*factorial(total-3)*factorial(1-alpha),factorial(beta-1)))

def pairings(indices):
    if not indices:
        yield []
        return
    first=indices[0]
    for j in range(1,len(indices)):
        for tail in pairings(indices[1:j]+indices[j+1:]):
            yield [(first,indices[j])]+tail

def angular(poly):
    out=P()
    names=["ka","kb","kc","ke"]
    for m,c in P(poly).t.items():
        powers=dict(m)
        indices=[]
        for i,name in enumerate(names):
            indices.extend([i]*powers.pop(name,0))
        coefficient=P({tuple(sorted(powers.items())):c})
        if len(indices)%2:
            continue
        if len(indices)==0:
            out+=coefficient
            continue
        assert len(indices) in (2,4),indices
        contraction=F(0)
        for pairing in pairings(indices):
            term=F(1)
            for i,j in pairing:
                term*=gram[i][j]
            contraction+=term
        factor=(F(1,4)+eps*F(1,8)) if len(indices)==2 else (F(1,24)+eps*F(5,144))
        out+=coefficient*K**(len(indices)//2)*factor*contraction
    return out

def integrate(poly):
    out=P()
    for m,c in P(poly).t.items():
        powers=dict(m)
        alpha=powers.pop("Ki",0)-powers.pop("K",0)
        beta=powers.pop("Ai",0)
        out+=P({tuple(sorted(powers.items())):c})*master(alpha,beta)
    return out.coeff("eps",0)+out.coeff("eps",1).coeff("IR",1)+out.coeff("eps",1).coeff("UV",1)

def reciprocal(shift,heavy):
    base=Ai if heavy else Ki
    return base*(1-2*rho*kdot(shift)*base-rho**2*dot_ext(shift,shift)*base+4*rho**2*kdot(shift)**2*base**2)

def cycle(order,coefficient_order=2):
    momentum=(0,0,0)
    heavy=True
    props=[]
    gamma_tokens=[]
    weight_h=0
    weight_l=0
    for i,vertex in enumerate(order):
        if vertex in ("C","D"):
            gamma_tokens.append(E)
            if heavy:
                weight_h+=1
            else:
                weight_l+=1
        if vertex=="B":
            heavy=False
        momentum=vadd(momentum,external[vertex])
        props.append((momentum,heavy))
        gamma_tokens.append(("prop",len(props)-1))
    assert momentum==(0,0,0)
    heavy_indices=[i for i,(_,massive) in enumerate(props) if massive]
    numerator=P()
    for mcount in (0,2):
        for masses in combinations(heavy_indices,mcount):
            vectors=[]
            for token in gamma_tokens:
                if token==E:
                    vectors.append(E)
                elif token[1] not in masses:
                    vectors.append(props[token[1]][0])
            numerator+=2*trace_normalized(tuple(vectors))
    integrand=mul([numerator]+[reciprocal(shift,massive) for shift,massive in props])
    return (weight_h,weight_l),integrate(angular(integrand.coeff("rho",coefficient_order)))

from math import log1p

count=0

def check(name,actual,expected=0):
    global count
    remainder=P(actual)-P(expected)
    if remainder.t:
        raise AssertionError(f"{name}: {remainder}")
    count+=1
    print(f"PASS {count:02d} {name}")

print("Python:",sys.version.split()[0])
print("Arithmetic: Fraction polynomials, Clifford traces, rank-2/rank-4 d-dimensional angular averages")
check("IR master J21",master(2,1),IR-L+1)
check("IR master J22",master(2,2),-IR+L-2)
check("IR master J31",master(3,1),IR-L+1)
check("IR master J32",master(3,2),-2*IR+2*L-3)
check("UV master J02",master(0,2),UV-L)
check("UV master Jminus13",master(-1,3),UV-L-F(1,2))
check("finite master J12",master(1,2),-1)
check("finite master J03",master(0,3),-F(1,2))

hc,lc=map(P,["h","l"])
h1,h2,l1,l2=map(P,["h1","h2","l1","l2"])
all_angles=[]
for angle in (F(0),F(1,3),-F(1,2)):
    gram[0][2]=gram[2][0]=-1+angle
    gram[1][2]=gram[2][1]=-1-angle
    trace_normalized.cache_clear()
    sums={0:P(),1:P(),2:P()}
    sums0={0:P(),1:P(),2:P()}
    charge_mixed=P()
    cycles=[]
    for perm in permutations(("B","C","D")):
        order=("A",)+perm
        (nh,nl),value=cycle(order,2)
        _,value0=cycle(order,0)
        sums[nh]+=value
        sums0[nh]+=value0
        c1=h1 if order.index("C")<order.index("B") else l1
        c2=h2 if order.index("D")<order.index("B") else l2
        charge_mixed+=c1*c2*value
        cycles.append((order,nh,str(value),str(value0)))
    check(f"angle {angle} heavy-heavy p2",sums[2])
    check(f"angle {angle} heavy-light p2",sums[1],-F(4,3))
    check(f"angle {angle} light-light p2",sums[0],-F(4,3))
    p0=sums0[2]*hc**2+sums0[1]*hc*lc+sums0[0]*lc**2
    check(f"angle {angle} scalar wavefunction seagull",p0,2*(hc-lc)**2*(UV-L+F(1,2)))
    fdiag=-(sums[2]*hc**2+sums[1]*hc*lc+sums[0]*lc**2)*F(1,8)
    fmixed=-charge_mixed*F(1,4)
    check(f"angle {angle} field-strength diagonal charge polynomial",fdiag,lc*(hc+lc)*F(1,6))
    check(f"angle {angle} distinct-field normalization",fmixed,(h1*l2+h2*l1+2*l1*l2)*F(1,6))
    all_angles.append(cycles)
print("SIX CYCLES AT cos(theta)=0:")
for row in all_angles[0]:
    print("CYCLE",*row)

# Background HL parameter integrals, independent of the box expansion.
Iw=F(1,6)
Iwlog=-F(1,4)+F(1,9)
Ix=F(1,2)
Ixlog=-F(1,4)
Omega_HL_one=-2*Iw+4*((UV-L)*Iw-Iwlog)
pp_HL_one=4*((UV-L)*Iw-Iwlog)
mass_HL_one=2*((UV-L)*Ix-Ixlog)
check("one-orientation HL transverse derivative",Omega_HL_one,(UV-L)*F(2,3)+F(2,9))
check("one-orientation HL longitudinal remainder",pp_HL_one-Omega_HL_one,F(1,3))
check("one-orientation HL zero-momentum mass",mass_HL_one,UV-L+F(1,2))
check("background longitudinal recovers scalar Q coefficient",2*(pp_HL_one-Omega_HL_one),F(2,3))

ha,hb,la,lb=map(P,["ha","hb","la","lb"])
da,db=la-ha,lb-hb
Zbg=-F(4,3)*ha*hb-F(2,3)*L*(ha*db+da*hb)+da*db*(-F(4,3)*L+F(4,9))
Cmat=(la*hb+ha*lb+2*la*lb)*F(1,12)
Da=ha*F(2,9)+(F(5,18)-L*F(1,3))*la
Db=hb*F(2,9)+(F(5,18)-L*F(1,3))*lb
check("background resolves current coefficients",Zbg,-4*Cmat+2*(Da*db+Db*da))
hardpole=(ha*db+da*hb)*F(2,3)+da*db*F(4,3)
softpole=-(la*db+da*lb)*F(2,3)
check("background hard and EFT soft poles cancel",hardpole+softpole)
check("universal neutral-scalar low-energy theorem",fdiag.subs("l",hc),hc**2*F(1,3))

# Complete model charge substitutions, normalized by q0*|Yukawa|^2/M^2.
gy,gx,gw,t3=map(P,["gY","gX","g2","t3"])
def f(h,l):
    return l*(h+l)*F(1,6)
def cross(hA,lA,hB,lB):
    return (hA*lB+hB*lA+2*lA*lB)*F(1,6)
def current(h,l):
    return h*F(2,9)+(F(5,18)-L*F(1,3))*l
check("H BB coefficient",f(-gy,-gy*F(1,2)),gy**2*F(1,8))
check("H XX coefficient",f(gx,gx),gx**2*F(1,3))
check("H WW diagonal coefficient",f(P(0),gw*F(1,2)),gw**2*F(1,24))
check("H BX explicit cross coefficient",cross(-gy,-gy*F(1,2),gx,gx),-gy*gx*F(5,12))
check("H WB T-generator coefficient",cross(P(0),gw*t3,-gy,-gy*F(1,2)),-gw*gy*t3*F(1,3))
check("H WX T-generator coefficient",cross(P(0),gw*t3,gx,gx),gw*gx*t3*F(1,2))
check("S BB coefficient",f(-gy,-gy),gy**2*F(1,3))
check("S XX field-strength cancellation",f(gx,-gx))
check("S BX explicit cross coefficient",cross(-gy,-gy,gx,-gx),gy*gx*F(1,3))
check("H current B",current(-gy,-gy*F(1,2)),gy*(L*F(1,6)-F(13,36)))
check("H current X",current(gx,gx),gx*(F(1,2)-L*F(1,3)))
check("H current W generator",current(P(0),gw*t3),gw*t3*(F(5,18)-L*F(1,3)))
check("S current B conjugation",-current(-gy,-gy),gy*(F(1,2)-L*F(1,3)))
check("S current X conjugation",-current(gx,-gx),gx*(F(1,18)-L*F(1,3)))

# Electromagnetic combinations. Any rational sine/cosine with sW^2+cW^2=1
# gives an independent exact check; use 3/5,4/5 to avoid floating arithmetic.
sw,cw=F(3,5),F(4,5)
e=P("e")
gyn,gwn=e*F(5,4),e*F(5,3)
CHB=gyn**2*F(1,8)
CHW=gwn**2*F(1,24)
CHWB=-gyn*gwn*F(1,3)
CHBX=-gyn*gx*F(5,12)
CHWX=gwn*gx*F(1,2)
check("electromagnetic H gamma-gamma LET",cw**2*CHB+sw**2*CHW-sw*cw*CHWB*F(1,2),e**2*F(1,3))
check("electromagnetic H gamma-X LET",cw*CHBX-sw*CHWX*F(1,2),-e*gx*F(2,3))
check("electromagnetic S gamma-gamma LET",cw**2*gyn**2*F(1,3),e**2*F(1,3))

# Scalar-current EOM map, expressed as independent Wilson coefficients.
dHB,dHX,dHW,dSB,dSX=map(P,["dHB","dHX","dHW","dSB","dSX"])
QX,QY,QHD,RH,RS,OJ=map(P,["QX","QY","QHD","RH","RS","OJ"])
scalar=-gy*dHB*F(1,2)*(4*QHD-QX)-gw*dHW*(RH-QX*F(1,4))
scalar+=-2*gx*dSX*(4*RS-QY)+(2*gx*dHX+gy*dSB*F(1,2))*OJ
X,Y,mh,ms,lh,ls,lp,FH,FS=map(P,["X","Y","muH2","muS2","lambdaH","lambdaS","lambdaP","FH","FS"])
RHred=-QX*F(1,2)-mh*X**2+2*lh*X**3+lp*X**2*Y+X*FH*F(1,2)
RSred=-QY*F(1,2)-ms*Y**2+2*ls*Y**3+lp*X*Y**2+Y*FS*F(1,2)
nr=scalar.subs("RH",RHred).subs("RS",RSred)
for name,value in [("QX",gy*dHB*F(1,2)+gw*dHW*F(3,4)),("QHD",-2*gy*dHB),
                   ("QY",6*gx*dSX),("OJ",2*gx*dHX+gy*dSB*F(1,2))]:
    check("optional EOM derivative row "+name,nr.coeff(name,1),value)
for nx,ny,value in [(2,0,gw*dHW*mh),(3,0,-2*gw*dHW*lh),(2,1,-gw*dHW*lp),
                    (0,2,8*gx*dSX*ms),(0,3,-16*gx*dSX*ls),(1,2,-8*gx*dSX*lp)]:
    check(f"optional EOM potential row X^{nx}Y^{ny}",nr.coeff("X",nx).coeff("Y",ny),value)
check("optional EOM Higgs source",nr.coeff("FH",1).coeff("X",1),-gw*dHW*F(1,2))
check("optional EOM singlet source",nr.coeff("FS",1).coeff("Y",1),-4*gx*dSX)

# Published SM limit: arXiv:2112.10787, Eqs. (6.10)-(6.14),(6.25).
# Its L_E=log(mu^2/M^2) equals -L here; its HWB uses Pauli sigma.
check("published SM HW Eq 6.10",f(P(0),gw*F(1,2)),gw**2*F(1,24))
check("published SM HB Eq 6.11",f(-gy,-gy*F(1,2)),gy**2*F(1,8))
check("published SM HWB Pauli Eq 6.12",cross(P(0),gw,-gy,-gy*F(1,2))*F(1,2),-gw*gy*F(1,6))
su=P("u")
dhb=su*current(-gy,-gy*F(1,2))
dhw=su*current(P(0),gw)
rbb=gy**2*F(4,15)
chbox=-(su**2*F(1,3)+gy*dhb*F(1,2)+gw*dhw*F(3,4)+rbb*gy**2*F(1,8))
chd=-su**2*F(1,2)-2*gy*dhb-rbb*gy**2*F(1,2)
check("published SM Hbox Eq 6.13 with Ye=0",chbox,-gy**4*F(1,30)+su*gy**2*(F(13,72)-L*F(1,12))+su*gw**2*(-F(5,24)+L*F(1,4))-su**2*F(1,3))
check("published SM HD Eq 6.14 with Ye=0",chd,-gy**4*F(2,15)+su*gy**2*(F(13,18)-L*F(1,3))-su**2*F(1,2))
check("published SM up-H gauge source Eq 6.25",-gw*dhw*F(1,2),su*gw**2*(-F(5,36)+L*F(1,6)))

# Neutral-scalar background parameter integral, a separate numerical check.
def neutral_estimate(w,n=2048):
    p2=-w
    def value(x):
        weight=x*(1-x)
        return -8*weight*log1p(w/(1-weight*p2))
    step=1/n
    integral=value(0)+value(1)
    for i in range(1,n):
        integral+=(4 if i%2 else 2)*value(i*step)
    integral*=step/3
    return -integral/(4*w)
print("NUMERICAL neutral-scalar background checks, Simpson n=2048:")
errors=[]
for w in [1e-2,1e-3,1e-4]:
    estimate=neutral_estimate(w)
    error=abs(estimate-1/3)
    errors.append(error)
    assert error<w
    print(f"A/M2={w:.1e}, p2/M2={-w:.1e}, C/(q0*gYuk2*c2/M2)={estimate:.12f}, target=1/3")
assert errors[2]<errors[1]<errors[0]
print(f"RESULT: {count} exact symbolic checks passed; 3 neutral-background numerical cases passed")
print("Field strength: C_diag = q0*gYuk2*l*(h+l)/(6*M2)")
print("Current: D_a = q0*gYuk2*[2*h_a/9+(5/18-L/3)*l_a]/M2")
print("Scope: CP-even two-scalar/two-gauge hard projection and current completion; no FeynArts/FeynCalc run.")
