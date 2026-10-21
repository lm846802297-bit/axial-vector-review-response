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


from math import log,exp
from decimal import Decimal as D,localcontext

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
def vcheck(name,a,b):
    truth(name,all(not (P(x)-P(y)).t for x,y in zip(a,b)))

print("Python:",sys.version.split()[0])
print("Arithmetic: Fraction polynomials, Laurent simplex moments, explicit epsilon-pole finite terms")
eps,UV,IR,L,h,l,delta,xi=map(P,["eps","UV","IR","L","h","l","delta","xi"])
def eval_eps(p):
    return p.coeff("eps",0)+p.coeff("eps",1).coeff("UV",1)+p.coeff("eps",1).coeff("IR",1)
U=UV-L+1
Iir=IR-L+1
Z0=UV-L
half=F(1,2)+eps*F(1,4) # 2/d
gamma0h=eval_eps(-(-F(1,2)+eps*F(1,4))*Z0+1)
gamma0s=eval_eps(half*U)
Fself=(UV-L)*F(1,2)+F(3,4)
check("heavy zero-momentum gauge vertex",gamma0h,Fself)
check("scalar zero-momentum gauge vertex",gamma0s,Fself)
check("charge Ward identity before canonical fields",h*gamma0h+(l-h)*gamma0s,l*Fself)
check("finite charge shift cancels field normalization",l*Fself.subs("UV",0)-l*(F(3,4)-L*F(1,2)))
check("scalar dimensional prefactor cancellation",((1+eps*F(1,2))*(1-eps*F(1,2))).coeff("eps",1))

# Heavy-photon triangle: t=x+y, x=t*z, y=t*(1-z), measure=t dt dz.
t,z=map(P,["t","z"])
ti=P({(("t",-1),):F(1)})
x=t*z
y=t*(1-z)
def moment(p):
    result=P()
    for mon,c in p.t.items():
        powers=dict(mon)
        nt=powers.pop("t",0)
        nz=powers.pop("z",0)
        assert nt>=0 and nz>=0,(nt,nz)
        result+=P({tuple(sorted(powers.items())):c/F((nt+1)*(nz+1))})
    return result
hs=moment(t*x*(1-x)*(2*ti+ti**2))
hz=moment(-2*t*x*y*(2*ti+ti**2))
ht=moment(t*(1-t)*ti)
hd=moment(-2*t*x*(1-x)*ti)
hc=moment(2*t*x*y*ti)
for name,actual,expected in [("gamma S",hs,F(11,18)),("gamma dot",hz,-F(7,18)),
                             ("triple",ht,F(1,2)),("diagonal vector",hd,-F(5,18)),
                             ("crossed vector",hc,F(1,9))]:
    check("heavy triangle moment "+name,actual,expected)

# Scalar-photon triangle exact endpoint moments, including finite harmonic term.
def harmonic(n):
    return sum((F(1,j) for j in range(1,n+1)),F(0))
def endpoint(a,b):
    return F(factorial(a)*factorial(b),factorial(a+b+1))*(-IR+L-harmonic(a+b+1))
I10,I20,I11=endpoint(1,0),endpoint(2,0),endpoint(1,1)
ss=I10-I20
sz=-2*I11
sd=I10-2*I20
sc=I10-2*I11
check("scalar triangle S moment",ss,(-IR+L)*F(1,6)-F(5,36))
check("scalar triangle diagonal moment",sd,(IR-L)*F(1,6)+F(17,36))
check("scalar triangle crossed moment",sc,ss)

# Basis: gamma*pprime2, gamma*p2, gamma*(p.pprime), pprimeSlash gamma pSlash,
#        pprime^mu*pprimeSlash, p^mu*pSlash, pprime^mu*pSlash, p^mu*pprimeSlash.
heavy=[hs,hs,hz,ht,hd,hd,hc,hc]
scalar=[ss,ss,sz,P(),sd,sd,sc,sc]
G3=list(map(P,[1,1,0,1,0,0,0,0]))
R=list(map(P,[F(1,2),F(1,2),0,1,-F(1,2),-F(1,2),-F(1,2),-F(1,2)]))
T=list(map(P,[1,1,-2,0,-1,-1,1,1]))
def vsum(*terms):
    return [sum((factor*vec[i] for factor,vec in terms),P()) for i in range(8)]
vcheck("heavy offshell decomposition",heavy,vsum((F(1,3),G3),(F(1,6),R),(F(7,36),T)))
kt_s=(-IR+L)*F(1,6)-F(11,36)
vcheck("scalar offshell decomposition",scalar,vsum((F(1,3),G3),(-F(1,3),R),(kt_s,T)))
A,B,C,sp,sm=map(P,["pprime2","p2","pdotpprime","slashpprime","slashp"])
def ward(v):
    return ((v[0]*A+v[1]*B+v[2]*C)*(sp-sm)+v[3]*(A*sm-B*sp)
            +v[4]*(A-C)*sp+v[5]*(C-B)*sm+v[6]*(A-C)*sm+v[7]*(C-B)*sp)
check("heavy offshell Ward through p^3",ward(heavy),(A*sp-B*sm)*F(1,3))
check("scalar offshell Ward through p^3",ward(scalar),(A*sp-B*sm)*F(1,3))
check("Pauli EOM tensor is transverse",ward(R))
check("current-P tensor is transverse",ward(T))
f=-h*F(7,36)-delta*kt_s.subs("IR",0)
e=h*F(1,6)-delta*F(1,3)
check("form-factor matching current-P coefficient",f,-h*F(7,36)+delta*(F(11,36)-L*F(1,6)))
check("Pauli EOM coefficient",e.subs("delta",l-h),h*F(1,2)-l*F(1,3))
softT=delta*F(1,6)*(UV-P("logq")+F(8,3))
cx=P("cx")
weight=(1-2*cx)**2
weight_int=sum((coef/F(dict(mon).get("cx",0)+1) for mon,coef in weight.t.items()),F(0))
log_int=-2*sum((-coef/F((dict(mon).get("cx",0)+1)**2) for mon,coef in weight.t.items()),F(0))
check("scalar-current soft polarization weight",weight_int,F(1,3))
check("scalar-current soft polarization logarithmic moment",log_int,F(8,9))
check("scalar hard/soft IR pole cancellation",(-delta*IR*F(1,6)).coeff("IR",1)+softT.coeff("UV",1))
check("current-P logarithm and EFT counterterm RG",-2*f.derivative("L"),delta*F(1,3))

# Explicit gauge-exchange radial kernels for the two-fermion/two-scalar current projection.
metric_raw={
 "EE":-(6-2*eps)*U-(1-eps*F(1,2))*Z0,
 "LE":(4-2*eps)*U-(1-eps*F(1,2)),
 "LR":(-1+eps*F(3,2))*Iir+(1-eps*F(1,2)),
 "HE":(-F(3,2)+eps*F(1,4))*Iir-U-half,
 "HR":(F(5,2)-eps*F(1,4))*Iir+half,
 "HS":-Iir-half
}
long_raw={
 "EE":-(1+half)*U+half*Z0,
 "LE":U+half,
 "LR":-Iir-half,
 "HE":-U-half,
 "HR":Iir+half,
 "HS":-Iir-half
}
metric={k:eval_eps(v) for k,v in metric_raw.items()}
longitudinal={k:eval_eps(v) for k,v in long_raw.items()}
expected={
 "EE":-7*UV+7*L-F(7,2),
 "LE":4*UV-4*L+1,
 "LR":-IR+L+F(3,2),
 "HE":-UV-IR*F(3,2)+L*F(5,2)-F(11,4),
 "HR":IR*F(5,2)-L*F(5,2)+F(11,4),
 "HS":-IR+L-F(3,2)
}
for k in metric:
    check("direct exchange radial kernel "+k,metric[k],expected[k])
    print("DIRECT_KERNEL",k,str(metric[k]),"LONG",str(longitudinal[k]))
def weighted(tab):
    return (h**2*tab["EE"]+2*h*l*tab["LE"]+l**2*tab["LR"]
            +2*h*delta*tab["HE"]+2*l*delta*tab["HR"]+delta**2*tab["HS"])
longsum=weighted(longitudinal).subs("delta",l-h)
check("longitudinal exchange sum is scaleless",longsum,h**2*(UV-IR))
total=(weighted(metric)-(1-xi)*weighted(longitudinal)).subs("delta",l-h)
finite=total.subs("UV",0).subs("IR",0)
c=3*(h**2-l**2)*L+5*h*(l-h)+F(11,2)*(l-h)**2
check("general Abelian proper current hard coefficient",finite,c)
check("direct exchange finite gauge parameter cancellation",finite.derivative("xi"))
check("direct exchange total pole",total.coeff("UV",1)+total.coeff("IR",1),3*(l**2-h**2))
check("neutral scalar proper current limit",finite.subs("l",h))
check("Abelian current-projection logarithm versus UV tree ratio",6*(h**2-l**2)-2*finite.derivative("L"))
# Common pure-light vertex pieces and field CT reconstruct the full UV pole.
full_uv_pole=total.coeff("UV",1)+2*xi*l*(l-h)
wave=-xi*l**2+(3-xi)*(l-h)**2
check("full UV proper amplitude counterterm",full_uv_pole+wave+3*(h**2-l**2))

gy,gx,gw,kappa,u,v=map(P,["gY","gX","g2","kappa","u","v"])
for sign in (1,-1):
    def ff(hval,lval):
        return f.subs("h",hval).subs("delta",lval-hval)
    check(f"s={sign} f_LB",ff(-gy,-gy*F(1,2)),gy*(F(25,72)-L*F(1,12)))
    check(f"s={sign} f_LX",ff(sign*gx,sign*gx),-sign*gx*F(7,36))
    check(f"s={sign} f_RB",ff(-gy,-gy),gy*F(7,36))
    check(f"s={sign} f_RX",ff(sign*gx,-sign*gx),sign*gx*(L*F(1,3)-F(29,36)))
check("f_LW",f.subs("h",0).subs("delta",gw),gw*(F(11,36)-L*F(1,6)))
check("L/H proper hypercharge",c.subs("h",-gy).subs("l",-gy*F(1,2)),gy**2*(L*F(9,4)-F(9,8)))
check("L/H proper X neutral-scalar cancellation",c.subs("h",gx).subs("l",gx))
check("R/S proper X charged-scalar coefficient",c.subs("h",gx).subs("l",-gx),12*gx**2)
check("R/S proper hypercharge cancellation",c.subs("h",-gy).subs("l",-gy))
# Tree mixing contractions, compared after multiplication by det K.
kn=[[P(1),-kappa],[-kappa,P(1)]]
def dotK(a,b):
    return sum((a[i]*kn[i][j]*b[j] for i in range(2) for j in range(2)),P())
for sign in (1,-1):
    hv=[-gy,sign*gx]
    for label,lv,ex in [
        ("L",[-gy*F(1,2),sign*gx],gy**2*(L*F(9,4)-F(9,8))+sign*kappa*gy*gx*(3*L-F(5,2))),
        ("R",[-gy,-sign*gx],12*gx**2+sign*kappa*gy*gx*(12*L-10))
    ]:
        dv=[lv[i]-hv[i] for i in range(2)]
        actual=3*(dotK(hv,hv)-dotK(lv,lv))*L+5*dotK(hv,dv)+F(11,2)*dotK(dv,dv)
        check(f"s={sign} proper Kinv {label} numerator",actual,ex)

# Weak group tensor: sum T_ia T_bj = 1/2 delta_ij delta_ab -1/4 delta_ia delta_bj.
weak=metric["LR"]+2*metric["HR"]+metric["HS"]
check("weak direct radial sum",weak,3*IR-3*L+F(11,2))
check("weak longitudinal radial sum",longitudinal["LR"]+2*longitudinal["HR"]+longitudinal["HS"])
# Exact Gaussian rational 2x2 generators.
def gm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def ga(a,b): return (a[0]+b[0],a[1]+b[1])
g0=(F(0),F(0)); gp=(F(1,2),F(0)); gn=(F(-1,2),F(0))
gi=(F(0),F(1,2)); gmi=(F(0),F(-1,2))
Ts=[[[g0,gp],[gp,g0]],[[g0,gmi],[gi,g0]],[[gp,g0],[g0,gn]]]
ok=True
for i in range(2):
 for a in range(2):
  for b in range(2):
   for j in range(2):
    actual=g0
    for tm in Ts: actual=ga(actual,gm(tm[i][a],tm[b][j]))
    want=F(int(i==j and a==b),2)-F(int(i==a and b==j),4)
    ok=ok and actual==(want,F(0))
truth("weak group Fierz all indices",ok)

# Full SM reference limit after adding fermion P, boson jP and Q2 images.
fLB=gy*(F(25,72)-L*F(1,12))
fLW=gw*(F(11,36)-L*F(1,6))
properB=gy**2*(F(9,32)-L*F(9,16))
properWs=gw**2*(-F(33,32)+L*F(9,16))
properWt=gw**2*(F(11,32)-L*F(3,16))
check("published rank-one hypercharge H-l singlet",properB-gy*fLB*F(1,2),gy**2*(F(31,288)-L*F(25,48)))
check("published rank-one hypercharge H-l triplet",properB,gy**2*(F(9,32)-L*F(9,16)))
check("published rank-one weak H-l singlet",properWs,gw**2*(-F(33,32)+L*F(9,16)))
check("published rank-one weak H-l triplet",properWt-gw*fLW*F(1,4),gw**2*(F(77,288)-L*F(7,48)))
universalS=gy**4*F(1,15)+gy**2*u*(L*F(1,12)-F(13,72))
universalT=gw**2*u*(L*F(1,12)-F(5,72))
fullS=u**2*(F(13,16)-L*F(3,8))+u*(properB+properWs-gy*fLB*F(1,2))+universalS
fullT=u**2*(F(5,16)-L*F(3,8))+u*(properB+properWt-gw*fLW*F(1,4))+universalT
check("published complete single-flavor H-l singlet",fullS,gy**4*F(1,15)+gy**2*u*(-F(7,96)-L*F(7,16))+gw**2*u*(-F(33,32)+L*F(9,16))+u**2*(F(13,16)-L*F(3,8)))
check("published complete single-flavor H-l triplet",fullT,gy**2*u*(F(9,32)-L*F(9,16))+gw**2*u*(F(19,96)-L*F(1,16))+u**2*(F(5,16)-L*F(3,8)))

# Equal-mass removable limits of independent on-shell parameter functions.
dr=P("dr")
rr=1+dr
lnrr=sum((((-1)**(n+1))*dr**n*F(1,n) for n in range(1,9)),P())
nh=F(7,6)-6*rr+F(15,2)*rr**2-F(8,3)*rr**3-(3*rr**2-2*rr**3)*lnrr
ns=-lnrr-F(11,6)+3*rr-F(3,2)*rr**2+rr**3*F(1,3)
for n in range(4):
    check(f"heavy equal-mass removable numerator order {n}",nh.coeff("dr",n))
    check(f"scalar equal-mass removable numerator order {n}",ns.coeff("dr",n))
check("heavy equal-mass finite parameter limit",nh.coeff("dr",4)*F(1,6),F(1,8))
check("scalar equal-mass finite parameter limit",ns.coeff("dr",4)*F(1,6),F(1,24))

def simpson(fun,n=8192):
    value=fun(0.)+fun(1.)
    for i in range(1,n): value+=(4 if i%2 else 2)*fun(i/n)
    return value/(3*n)
print("NUMERICAL on-shell heavy/scalar parameter functions, Simpson n=8192:")
for rnum in [0.02,0.005,0.001]:
    def heavy_int(t):
        d=t+(1-t)*rnum
        return t**3*(2/d+1/d**2)/6
    hu=simpson(heavy_int)
    he=(7/6-6*rnum+7.5*rnum**2-(8/3)*rnum**3
        -(3*rnum**2-2*rnum**3)*log(rnum))/(6*(1-rnum)**4)
    length=-log(rnum)
    su=simpson(lambda v:length*(1-rnum*exp(length*v))**3/(6*(1-rnum)**4))
    se=(-log(rnum)-11/6+3*rnum-1.5*rnum**2+rnum**3/3)/(6*(1-rnum)**4)
    assert abs(hu-he)<1e-10 and abs(su-se)<1e-10
    print(f"PARAM r={rnum:.3g}, heavy_int={hu:.12f}, heavy_exact={he:.12f}, scalar_int={su:.12f}, scalar_exact={se:.12f}")
print("NUMERICAL scalar hard remainder, Decimal precision=50:")
with localcontext() as ctx:
    ctx.prec=50
    errs=[]
    for rnum in [D("1e-2"),D("1e-3"),D("1e-4")]:
        scalar=(-rnum.ln()-D(11)/6+3*rnum-D(3)/2*rnum**2+rnum**3/3)/(6*(1-rnum)**4)
        hard=scalar+rnum.ln()/6
        err=abs(hard+D(11)/36)
        errs.append(err)
        assert err<2*rnum*abs(rnum.ln())
        print(f"HARD_IR r={rnum}, full-minus-soft={hard:.15f}, target=-11/36")
    assert errs[2]<errs[1]<errs[0]
print(f"RESULT: {count} exact parameter/symbolic/group checks passed; 6 integrals and 3 IR hard limits passed")
print("f_psi,a = q0*Yuk2/M2*[-7*h_a/36+(l_a-h_a)*(11/36-L/6)]")
print("proper Abelian c = 3*(h^2-l^2)*L+5*h*(l-h)+11*(l-h)^2/2")
print("Scope: offshell gauge vertex, Ward identity, and physical-current projection of proper gauge exchange.")
print("No FeynArts/FeynCalc, Matchete, matchmakereft, or external diagram generator was run.")
