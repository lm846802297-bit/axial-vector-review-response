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
    residue=P(actual)-P(expected)
    if residue.t:
        raise AssertionError(f"{name}: {residue}")
    count+=1
    print(f"PASS {count:02d} {name}")

def cut(poly, variable="rho", n=2):
    return P({m:c for m,c in P(poly).t.items() if dict(m).get(variable,0)<=n})

def product(items):
    answer=P(1)
    for item in items:
        answer=cut(answer*item)
    return answer

K,Ki,Ai,rho,eps,IR,L = map(P,["K","Ki","Ai","rho","eps","IR","L"])
ka,kb,kc = map(P,["ka","kb","kc"])
a2,b2,c2,ab,ac,bc=map(P,["a2","b2","c2","ab","ac","bc"])
inv_d=F(1,4)+eps*F(1,8)
loop_names=("ka","kb","kc")
dot_names={(0,0):a2,(1,1):b2,(2,2):c2,(0,1):ab,(0,2):ac,(1,2):bc}

def angular(poly):
    answer=P()
    for monomial, coefficient in P(poly).t.items():
        powers=dict(monomial)
        indices=[]
        for i,name in enumerate(loop_names):
            indices.extend([i]*powers.pop(name,0))
        base=P({tuple(sorted(powers.items())):coefficient})
        if not indices:
            answer+=base
        elif len(indices)==2:
            answer+=base*K*inv_d*dot_names[tuple(sorted(indices))]
        elif len(indices)%2:
            pass
        else:
            raise AssertionError("unhandled higher-rank tensor")
    return answer

def master(alpha,beta):
    if (alpha,beta)==(2,2):
        return -IR+L-2
    assert alpha<2 and beta>0 and alpha+beta>2,(alpha,beta)
    sign=(-1)**(alpha+beta)
    return P(F(sign*factorial(alpha+beta-3)*factorial(1-alpha),factorial(beta-1)))

def integrate(poly, dimension_sum):
    answer=P()
    for monomial,coefficient in P(poly).t.items():
        powers=dict(monomial)
        alpha=powers.pop("Ki",0)-powers.pop("K",0)
        beta=powers.pop("Ai",0)
        assert alpha+beta==dimension_sum,(alpha,beta,powers)
        answer+=P({tuple(sorted(powers.items())):coefficient})*master(alpha,beta)
    # epsilon*(1/epsilon_IR)=1; epsilon times finite constants vanishes.
    return answer.coeff("eps",0)+answer.coeff("eps",1).coeff("IR",1)

def substitute(poly, replacements):
    answer=P(poly)
    for name,value in replacements.items():
        answer=answer.subs(name,value)
    return answer

print("Python:",sys.version.split()[0])
print("Arithmetic: exact rational sparse polynomials; tensor/radial integration rules are explicit")

# Mixed graph: basis a=p2, b=q, c=p4; M^2=1 during radial integration.
mixed_num=2*(K-rho*kb)
mixed_den=[Ki,
    Ki*(1+2*rho*kb*Ki-rho**2*b2*Ki+4*rho**2*kb**2*Ki**2),
    Ai*(1+2*rho*ka*Ai-rho**2*a2*Ai+4*rho**2*ka**2*Ai**2),
    Ai*(1-2*rho*kc*Ai-rho**2*c2*Ai+4*rho**2*kc**2*Ai**2)]
mixed_p2=product([mixed_num]+mixed_den).coeff("rho",2)
mixed_integral=integrate(angular(mixed_p2),4)
mixed_expected=(IR-L+F(3,2))*b2-F(2,3)*(a2+c2)+F(1,2)*(ab-bc)-F(1,3)*ac
check("mixed graph expanded tensor integral",mixed_integral,mixed_expected)

s,t,u,Sigma=map(P,["s","t","u","Sigma"])
x1,x2,x3,x4=map(P,["x1","x2","x3","x4"])
sumx=x1+x2+x3+x4
mixed_map={"a2":x2,"b2":s,"c2":x4,
           "ab":(s+x2-x1)*F(1,2),"bc":(-s-x4+x3)*F(1,2),
           "ac":(t-x2-x4)*F(1,2)}
mixed_external=substitute(mixed_integral,mixed_map)
check("mixed complete off-shell polynomial",mixed_external,(IR-L+2)*s-t*F(1,6)-sumx*F(1,4))
check("mixed on-shell old kernel",substitute(mixed_external,{"x1":0,"x2":0,"x3":0,"x4":0}),(IR-L+2)*s-t*F(1,6))
check("mixed physical amplitude overall sign",-mixed_external,(-IR+L-2)*s+t*F(1,6)+sumx*F(1,4))

# Four-slash trace generated from dot products of r_i=k+shift_i.
zero=(0,0,0)
va,vb,vc=(1,0,0),(0,1,0),(0,0,1)
vecs=[zero,va,vb,vc]
def shift_dot(v,w):
    answer=P()
    for i,vi in enumerate(v):
        for j,wj in enumerate(w):
            answer+=vi*wj*dot_names[tuple(sorted((i,j)))]
    return answer

def fermion_dot(v,w):
    return K+rho*sum(((v[i]+w[i])*[ka,kb,kc][i] for i in range(3)),P())+rho**2*shift_dot(v,w)

fd=lambda i,j:fermion_dot(vecs[i],vecs[j])
pure_num=cut(2*(fd(0,1)*fd(2,3)-fd(0,2)*fd(1,3)+fd(0,3)*fd(1,2)))
check("pure four-slash numerator zeroth order",pure_num.coeff("rho",0),2*K**2)
check("pure four-slash numerator first order",pure_num.coeff("rho",1),2*K*(ka+kb+kc))
check("pure four-slash numerator second order",pure_num.coeff("rho",2),2*K*(bc-ac+ab)+4*ka*kc)
pure_den=[Ki,
    Ai*(1-2*rho*ka*Ai-rho**2*a2*Ai+4*rho**2*ka**2*Ai**2),
    Ki*(1-2*rho*kb*Ki-rho**2*b2*Ki+4*rho**2*kb**2*Ki**2),
    Ai*(1-2*rho*kc*Ai-rho**2*c2*Ai+4*rho**2*kc**2*Ai**2)]
pure_p2=product([pure_num]+pure_den).coeff("rho",2)
pure_integral=integrate(angular(pure_p2),3)
pure_expected=b2+F(4,3)*ac-F(3,2)*(ab+bc)+F(5,6)*(a2+c2)
check("pure graph tensor and vacuum integrals",pure_integral,pure_expected)
pure_map={"a2":x1,"b2":t,"c2":x4,
          "ab":(t+x1-x3)*F(1,2),"bc":(t-x2+x4)*F(1,2),
          "ac":(-u+x1+x4)*F(1,2)}
route1=substitute(pure_integral,pure_map)
check("pure routing 1 off-shell result",route1,-t*F(1,2)-u*F(2,3)+sumx*F(3,4))
route2=route1.subs("t",P("tmp")).subs("u",t).subs("tmp",u)
check("pure routing 2 crossing",route2,-u*F(1,2)-t*F(2,3)+sumx*F(3,4))
routesum=(route1+route2).subs("u",sumx-s-t)
check("complex singlet sum of routings",routesum,s*F(7,6)+sumx*F(1,3))

# Group projectors: route 1 -> delta_il delta_jk, route 2 -> delta_ik delta_jl.
amp_ik=(-route2).subs("u",sumx-s-t)
amp_il=(-route1).subs("t",sumx-s-u)
check("Higgs direct weak-index tensor",amp_ik,-s*F(1,2)+t*F(1,6)-sumx*F(1,4))
check("Higgs exchange weak-index tensor",amp_il,-s*F(1,2)+u*F(1,6)-sumx*F(1,4))

# Enumerate which fixed scalar Yukawa cycle carries which SU(2) tensor.
def index_weight(order,indices):
    # Light edges join conjugate-to-next-unconjugate in the directed cycle.
    return int(indices[order[1]]==indices[order[2]] and indices[order[3]]==indices[order[0]])

for indices in [(0,1,0,1),(0,1,1,0),(0,0,0,0)]:
    w1=index_weight((0,2,1,3),indices)
    w2=index_weight((0,3,1,2),indices)
    expected1=int(indices[0]==indices[3] and indices[1]==indices[2])
    expected2=int(indices[0]==indices[2] and indices[1]==indices[3])
    check("weak-index contraction "+str(indices),w1+2*w2,expected1+2*expected2)

BH,BS,A,LM=map(P,["BH","BS","A","LM"])
# H coefficients: d*Q_X + e*R_H + f*Q_HD.
dH,eH,fHD=-BH*F(1,6),-BH,-BH*F(1,2)
tensor_ik=2*dH*t+eH*(-t+sumx*F(1,2))+fHD*(-u+sumx*F(1,2))
check("H invariant operator projection",tensor_ik.subs("u",sumx-s-t),BH*amp_ik)
tensor_il=2*dH*u+eH*(-u+sumx*F(1,2))+fHD*(-t+sumx*F(1,2))
check("H exchanged operator projection",tensor_il.subs("t",sumx-s-u),BH*amp_il)
dS,eS=-BS*F(1,6),-BS*F(3,2)
check("S invariant operator projection",(2*dS*(t+u)+eS*s).subs("u",sumx-s-t),-BS*routesum)
check("Higgs nonredundant QX coefficient",dH-eH*F(1,2),BH*F(1,3))
check("singlet nonredundant QY coefficient",dS-eS*F(1,2),BS*F(7,12))

# Mixed old and newly determined off-shell completion, one flavor.
oldH=A*(LM-F(13,6))
oldD=A*(LM-2)*F(1,2)
eta=-A*F(1,3)
newH=oldH-2*eta
newD=oldD-2*eta
check("mixed off-shell cH correction",newH,A*(LM-F(3,2)))
check("mixed off-shell cD correction",newD,A*(LM*F(1,2)-F(1,3)))
check("mixed cDNR unchanged",newD-newH,oldD-oldH)
oldpoly=A*((LM-2)*s+t*F(1,6)-sumx*F(1,12))
newpoly=oldpoly-eta*sumx
check("off-shell T_H and T_S complete mixed amplitude",newpoly,A*((LM-2)*s+t*F(1,6)+sumx*F(1,4)))

# Full EOM bookkeeping in one scalar/source polynomial.
X,Y,mh,ms,lh,ls,lp,rH,rS,C = map(P,["X","Y","muH2","muS2","lambdaH","lambdaS","lambdaP","rH","rS","C"])
FH,FS,NH,NS,QX,QY,OD = map(P,["FH","FS","NH","NS","QX","QY","OD"])
fH,fS=-mh+2*lh*X+lp*Y,-ms+2*ls*Y+lp*X
RHred=-QX*F(1,2)-mh*X**2+2*lh*X**3+lp*X**2*Y+X*FH*F(1,2)
RSred=-QY*F(1,2)-ms*Y**2+2*ls*Y**3+lp*X*Y**2+Y*FS*F(1,2)
OHred=-OD*F(1,2)-mh*X*Y+2*lh*X**2*Y+lp*X*Y**2+Y*FH*F(1,2)
OSred=-OD*F(1,2)-ms*X*Y+2*ls*X*Y**2+lp*X**2*Y+X*FS*F(1,2)
HDred=rH*(fH**2*X+fH*FH+NH)+rS*(fS**2*Y+fS*FS+NS)
zH,zS,tH,tS,b,UH,US,Dxxx,Dyyy,Dxxy,Dxyy = map(P,["zH","zS","tH","tS","b","UH","US","Dxxx","Dyyy","Dxxy","Dxyy"])
base=(tH-mh*zH)*X+(tS-ms*zS)*Y+(2*lh*zH+UH)*X**2+(2*ls*zS+US)*Y**2+(b+lp*(zH+zS))*X*Y+Dxxx*X**3+Dyyy*Y**3+Dxxy*X**2*Y+Dxyy*X*Y**2+zH*FH*F(1,2)+zS*FS*F(1,2)
total=base+HDred+C*(OHred+OSred)+eH*RHred+eS*RSred
scalar=total.subs("FH",0).subs("FS",0).subs("NH",0).subs("NS",0).subs("OD",0).subs("QX",0).subs("QY",0)
rows={
    (1,0):tH-mh*zH+rH*mh**2,
    (0,1):tS-ms*zS+rS*ms**2,
    (2,0):2*lh*zH+UH-4*rH*mh*lh+BH*mh,
    (0,2):2*ls*zS+US-4*rS*ms*ls+BS*ms*F(3,2),
    (1,1):b+lp*(zH+zS)-C*(mh+ms)-2*lp*(rH*mh+rS*ms),
    (3,0):4*rH*lh**2+Dxxx-2*lh*BH,
    (0,3):4*rS*ls**2+Dyyy-3*ls*BS,
    (2,1):(2*lh+lp)*C+4*rH*lh*lp+rS*lp**2+Dxxy-lp*BH,
    (1,2):(lp+2*ls)*C+rH*lp**2+4*rS*ls*lp+Dxyy-lp*BS*F(3,2),
}
for (nx,ny),value in rows.items():
    check(f"unified potential L row X^{nx}Y^{ny}",scalar.coeff("X",nx).coeff("Y",ny),value)
source_rows=[("FH",0,0,zH*F(1,2)-rH*mh),
             ("FH",1,0,2*rH*lh-BH*F(1,2)),
             ("FH",0,1,C*F(1,2)+rH*lp),
             ("FS",0,0,zS*F(1,2)-rS*ms),
             ("FS",1,0,C*F(1,2)+rS*lp),
             ("FS",0,1,2*rS*ls-BS*F(3,4))]
for source,nx,ny,value in source_rows:
    check(f"unified source row {source} X^{nx}Y^{ny}",total.coeff(source,1).coeff("X",nx).coeff("Y",ny),value)
check("H source square retained once",total.coeff("NH",1),rH)
check("S source square retained once",total.coeff("NS",1),rS)

# Independent constant-background mass-basis checks of derivative coefficients.
w=P("w")
log1pw=w-w**2*F(1,2)
inverse1pw=1-w+w**2
heavy_light=product([inverse1pw,F(1,2)-L-log1pw])
check("background mixed kinetic leading term",heavy_light.coeff("w",0),F(1,2)-L)
check("background mixed kinetic off-shell completion",heavy_light.coeff("w",1),L-F(3,2))
# For one real radial mode, the massive diagonal Dirac coupling supplies
# w/(1+w)*[-log(m^2/mu^2)-2/3], in units of q0*|g|^2.
radial=heavy_light+w*inverse1pw*(-L-log1pw-F(2,3))
check("mass-basis radial kinetic slope",radial.coeff("w",1),-F(13,6))
check("four-point operators reproduce radial slope",4*(-F(1,6))+(-1-F(1,2)),-F(13,6))

print("MIXED KERNEL:",mixed_external)
print("PURE ROUTE 1:",route1)
print("RESULT:",count,"exact symbolic checks passed")
print("No numerical integration, FeynArts, FeynCalc, or independent external diagram generator was run.")

