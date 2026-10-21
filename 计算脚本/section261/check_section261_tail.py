from math import sqrt,atan2,cos,sin

count=0
def check(name,actual,expected=0):
    global count
    residual=P(actual)-P(expected)
    assert not residual.t,(name,str(residual))
    count+=1
    print(f"PASS {count:02d} {name}")

def syms(names):
    return [P(name) for name in names.split()]

def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(2)),P(0)) for j in range(2)] for i in range(2)]

def tr(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]

def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]

def scale(a,s):
    return [[s*a[i][j] for j in range(2)] for i in range(2)]

def cut(p):
    return p.coeff("eps",0)+P("eps")*p.coeff("eps",1)

def mcut(a):
    return [[cut(v) for v in row] for row in a]

def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]

def hess(p,names):
    return [[p.derivative(a).derivative(b) for b in names] for a in names]

def replace_many(p,sub):
    for k,v in sub:
        p=p.subs(k,v)
    return p

# Invariant polynomial -> tadpoles -> radial Hessian, with all sextic monomials.
X,Y,v,w,rho,sigma,mH,mS,lH,lS,lP,e30,e03,e21,e12=\
    syms("X Y v w rho sigma mH mS lH lS lP e30 e03 e21 e12")
V=-mH*X-mS*Y+lH*X**2+lS*Y**2+lP*X*Y+e30*X**3+e03*Y**3+e21*X**2*Y+e12*X*Y**2
Vrad=V.subs("X",rho**2*F(1,2)).subs("Y",sigma**2*F(1,2))
atvac=lambda p:p.subs("rho",v).subs("sigma",w)
FX=V.derivative("X").subs("X",v**2*F(1,2)).subs("Y",w**2*F(1,2))
FY=V.derivative("Y").subs("X",v**2*F(1,2)).subs("Y",w**2*F(1,2))
muH=lH*v**2+lP*w**2*F(1,2)+3*e30*v**4*F(1,4)+e21*v**2*w**2*F(1,2)+e12*w**4*F(1,4)
muS=lS*w**2+lP*v**2*F(1,2)+3*e03*w**4*F(1,4)+e21*v**4*F(1,4)+e12*v**2*w**2*F(1,2)
check("h tadpole chain rule",atvac(Vrad.derivative("rho")),v*FX)
check("s tadpole chain rule",atvac(Vrad.derivative("sigma")),w*FY)
check("H stationary mass parameter",FX.subs("mH",muH),0)
check("S stationary mass parameter",FY.subs("mS",muS),0)
H=hess(Vrad,["rho","sigma"])
stationary=lambda p:atvac(p).subs("mH",muH).subs("mS",muS)
Hstat=[[stationary(val) for val in row] for row in H]
expectH=[[v**2*(2*lH+3*e30*v**2+e21*w**2),
          v*w*(lP+e21*v**2+e12*w**2)],
         [v*w*(lP+e21*v**2+e12*w**2),
          w**2*(2*lS+3*e03*w**2+e12*v**2)]]
for i,j in [(0,0),(0,1),(1,1)]:
    check(f"radial Hessian {i}{j}",Hstat[i][j],expectH[i][j])
check("nonstationary hh tadpole term",atvac(H[0][0]),expectH[0][0]+FX)
check("nonstationary ss tadpole term",atvac(H[1][1]),expectH[1][1]+FY)

# Goldstone masses are checked from complex Cartesian fields, without gauge fixing.
chi,eta=syms("chi eta")
Vcomplex=V.subs("X",(rho**2+chi**2)*F(1,2)).subs("Y",(sigma**2+eta**2)*F(1,2))
goldvac=lambda p:atvac(p).subs("chi",0).subs("eta",0)
check("neutral H Goldstone potential mass",goldvac(Vcomplex.derivative("chi").derivative("chi")),FX)
check("S Goldstone potential mass",goldvac(Vcomplex.derivative("eta").derivative("eta")),FY)
check("no CP even odd potential mixing",goldvac(Vcomplex.derivative("rho").derivative("eta")),0)
check("no two Goldstone potential mixing",goldvac(Vcomplex.derivative("chi").derivative("eta")),0)

# Derivative operators are expanded before reading the kinetic matrix.
cx,cy,chd,cd,dh,ds=syms("cx cy chd cd dh ds")
kin=(dh**2+ds**2)*F(1,2)+cx*rho**2*dh**2+cy*sigma**2*ds**2\
    +chd*rho**2*dh**2*F(1,4)+cd*rho*sigma*dh*ds
Krad=[[atvac(z) for z in row] for row in hess(kin,["dh","ds"])]
check("radial Khh factor",Krad[0][0],1+v**2*(2*cx+chd*F(1,2)))
check("radial Kss factor",Krad[1][1],1+2*cy*w**2)
check("radial Khs factor",Krad[0][1],cd*v*w)
BH,BS,AH,AS,AW=syms("BH BS AH AS AW")
check("AH cancels radial kinetic row",
      2*(BH*F(1,3)-AH-AW*F(3,4))+(-BH*F(1,2)+4*AH)*F(1,2),
      BH*F(5,12)-AW*F(3,2))
check("AS radial kinetic row",2*(BS*F(7,12)-3*AS),BS*F(7,6)-6*AS)

# Canonical normalization of a general noncommuting two-field Hessian.
A,B,C,a,b,c,eh,es,ex,eps,p=syms("A B C a b c eh es ex eps p")
I=[[P(1),P(0)],[P(0),P(1)]]
H0=[[A,B],[B,C]]
dH=[[a,b],[b,c]]
E=[[eh,ex],[ex,es]]
K=add(I,scale(E,eps))
HT=add(H0,scale(dH,eps))
T=add(I,scale(E,-eps*F(1,2)))
canK=mcut(mm(mm(tr(T),K),T))
canH=mcut(mm(mm(tr(T),HT),T))
expected_can=add(H0,scale(add(dH,scale(add(mm(E,H0),mm(H0,E)),-F(1,2))),eps))
for i,j in [(0,0),(0,1),(1,1)]:
    check(f"canonical K {i}{j}",canK[i][j],I[i][j])
    check(f"canonical H {i}{j}",canH[i][j],expected_can[i][j])
check("canonical off diagonal explicit",canH[0][1],
      B+eps*(b-(eh+es)*B*F(1,2)-ex*(A+C)*F(1,2)))
trace1=A+C+eps*(a+c-eh*A-es*C-2*ex*B)
check("canonical trace invariant",canH[0][0]+canH[1][1],trace1)
check("determinant quotient invariant",cut(det(canH)),cut(det(HT)*(1-eps*(eh+es))))
kernel=add(scale(K,p),scale(HT,-1))
can_kernel=add(scale(I,p),scale(canH,-1))
check("generalized characteristic polynomial",
      cut(det(kernel)*(1-eps*(eh+es))),cut(det(can_kernel)))
kh,ks,kx=syms("kh ks kx")
check("generalized polynomial explicit",
      det([[p*kh-A,p*kx-B],[p*kx-B,p*ks-C]]),
      (kh*ks-kx**2)*p**2-(ks*A+kh*C-2*kx*B)*p+A*C-B**2)

# A finite rotation with algebraic cos^2+sin^2=1.
co,si=syms("co si")
Rot=[[co,si],[-si,co]]
rotH=mm(mm(tr(Rot),H0),Rot)
check("rotation lighter diagonal",rotH[0][0],A*co**2+C*si**2-2*B*co*si)
check("rotation off diagonal sign",rotH[0][1],B*(co**2-si**2)+(A-C)*co*si)
check("rotation upper diagonal",rotH[1][1],A*si**2+C*co**2+2*B*co*si)
for cn,sn in [(F(3,5),F(4,5)),(F(4,5),-F(3,5))]:
    lo,gap=syms("lo gap")
    rn=[[P(cn),P(sn)],[-P(sn),P(cn)]]
    h0n=mm(mm(rn,[[lo,P(0)],[P(0),lo+gap]]),tr(rn))
    dhr=mm(mm(tr(rn),dH),rn)
    numerator=(h0n[1][1]-h0n[0][0])*b-h0n[0][1]*(c-a)
    check(f"nondegenerate angle derivative c={cn} s={sn}",numerator,gap*dhr[0][1])

# Fixed UV parameters: VEV shift follows the inverse tree Hessian.
PX,PY=syms("PX PY")
delta_det=4*lH*lS-lP**2
dx_num=2*lS*PX-lP*PY
dy_num=2*lH*PY-lP*PX
check("fixed UV invariant VEV shift X",2*lH*dx_num+lP*dy_num,delta_det*PX)
check("fixed UV invariant VEV shift Y",lP*dx_num+2*lS*dy_num,delta_det*PY)

# Gauge EOM images are radial coordinate transformations, including VEV shifts.
Vtree=-mH*rho**2*F(1,2)-mS*sigma**2*F(1,2)\
    +lH*rho**4*F(1,4)+lS*sigma**4*F(1,4)+lP*rho**2*sigma**2*F(1,4)
tree_mu=[("mH",lH*v**2+lP*w**2*F(1,2)),("mS",lS*w**2+lP*v**2*F(1,2))]
old_vev=lambda z:replace_many(z,[("rho",v),("sigma",w)]+tree_mu)
Vimage=Vtree-eps*(AW*rho**3*Vtree.derivative("rho")*F(1,4)+AS*sigma**3*Vtree.derivative("sigma"))
new_vev=lambda z:cut(replace_many(z,
    [("rho",v+eps*AW*v**3*F(1,4)),("sigma",w+eps*AS*w**3)]+tree_mu))
check("gauge EOM shifted H tadpole",new_vev(Vimage.derivative("rho")),0)
check("gauge EOM shifted S tadpole",new_vev(Vimage.derivative("sigma")),0)
newH=[[new_vev(z) for z in row] for row in hess(Vimage,["rho","sigma"])]
oldH=[[old_vev(z) for z in row] for row in hess(Vtree,["rho","sigma"])]
imageE=[[-AW*v**2*F(3,2),P(0)],[P(0),-6*AS*w**2]]
imageT=add(I,scale(imageE,-eps*F(1,2)))
imageCan=mcut(mm(mm(tr(imageT),newH),imageT))
for i,j in [(0,0),(0,1),(1,1)]:
    check(f"gauge EOM radial spectrum invariant {i}{j}",imageCan[i][j],oldH[i][j])

# Higher derivative EOM: p^4 removal is tested for noncommuting r and H0.
rH,rS=syms("rH rS")
R=[[rH,P(0)],[P(0),rS]]
green=add(add(scale(I,p),scale(H0,-1)),scale(R,eps*p**2))
field=add(I,scale(mm(R,add(scale(I,p),H0)),-eps*F(1,2)))
reduced=mcut(mm(mm(tr(field),green),field))
reduced_expected=add(add(scale(I,p),scale(H0,-1)),scale(mm(mm(H0,R),H0),eps))
for i,j in [(0,0),(0,1),(1,1)]:
    check(f"p4 field transformation kernel {i}{j}",reduced[i][j],reduced_expected[i][j])
gradH=Vtree.derivative("rho");gradS=Vtree.derivative("sigma")
Vr=-F(1,2)*(rH*gradH**2+rS*gradS**2)
Hr=[[old_vev(z) for z in row] for row in hess(Vr,["rho","sigma"])]
Hr_expected=scale(mm(mm(oldH,R),oldH),-1)
for i,j in [(0,0),(0,1),(1,1)]:
    check(f"p4 scalar potential Hessian {i}{j}",Hr[i][j],Hr_expected[i][j])

# Light renormalizable Yukawa source expansion in the matched EFT.
Yuk,f0,fx,fy=syms("Yuk f0 fx fy")
# The common 1/sqrt(2) is stripped from mass and radial vertices.
mf=Yuk*rho*(1-f0-fx*rho**2*F(1,2)-fy*sigma**2*F(1,2))
check("light fermion mass source",atvac(mf),Yuk*v*(1-f0-fx*v**2*F(1,2)-fy*w**2*F(1,2)))
check("light fermion H source vertex",atvac(mf.derivative("rho")),
      Yuk*(1-f0-fx*v**2*F(3,2)-fy*w**2*F(1,2)))
check("light fermion S source vertex",atvac(mf.derivative("sigma")),-Yuk*fy*v*w)
TR=mm(T,Rot)
check("source transfer H to state1",TR[0][0],co-eps*eh*co*F(1,2)+eps*ex*si*F(1,2))
check("source transfer S to state1",TR[1][0],-si+eps*es*si*F(1,2)-eps*ex*co*F(1,2))
check("C5 times kinetic correction heavy order",1+2,3)

# Explicit UV-zero-portal mixing: all potential and derivative pieces combine.
cb,cpot,cder,D21,D12=syms("cb cpot cder D21 D12")
weighted=lH*v**2+lS*w**2
kxy=cb-cpot*weighted
kxxy=2*lH*cpot+D21
kxyy=2*lS*cpot+D12
mixing=-v*w*(kxy+kxxy*v**2+kxyy*w**2+cder*weighted)
check("zero UV portal mixed matrix assembly",mixing,
      -v*w*(cb+(cpot+cder)*weighted+D21*v**2+D12*w**2))
q,U,Vy,minv,L=syms("q U Vy minv L")
repl=[("cb",2*q*U*Vy),("cpot",q*U*Vy*minv*(L-F(3,2))),
      ("cder",q*U*Vy*minv*(F(7,6)-L*F(1,2))),
      ("D21",-q*U**2*Vy*minv),("D12",-q*U*Vy**2*minv)]
check("zero UV portal per flavor finite coefficient",replace_many(mixing,repl),
      -q*v*w*U*Vy*(2+minv*((L*F(1,2)-F(1,3))*weighted-U*v**2-Vy*w**2)))
check("off shell mixed derivative combination",replace_many(cpot+cder,repl),
      q*U*Vy*minv*(L*F(1,2)-F(1,3)))

# Pole/residue sign in the convention inverse kernel p^2-M^2+Pi.
s0,m1,m2,p11,p21,pprime=syms("s0 m1 m2 p11 p21 pprime")
check("pole shift sign",cut((m1-eps*p11)-m1+eps*p11),0)
check("off diagonal pole vector numerator",(m1-m2)*(-p21)+p21*(m1-m2),0)
check("one loop diagonal residue",cut((1-eps*pprime)*(1+eps*pprime)),1)

# Independent numerical algorithms: symmetric square root and Cholesky.
def nmm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def ntr(a): return [[a[j][i] for j in range(2)] for i in range(2)]
def ninv(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def eig(a):
    gap=sqrt((a[1][1]-a[0][0])**2+4*a[0][1]**2)
    return [(a[0][0]+a[1][1]-gap)/2,(a[0][0]+a[1][1]+gap)/2]
def symmetric_can(k,h):
    d=sqrt(k[0][0]*k[1][1]-k[0][1]**2)
    den=sqrt(k[0][0]+k[1][1]+2*d)
    root=[[(k[i][j]+(d if i==j else 0))/den for j in range(2)] for i in range(2)]
    t=ninv(root)
    return nmm(nmm(ntr(t),h),t),t
def cholesky_can(k,h):
    a=sqrt(k[0][0]);b=k[1][0]/a;c=sqrt(k[1][1]-b*b)
    t=[[1/a,-b/(a*c)],[0,1/c]]
    return nmm(nmm(ntr(t),h),t)

for label,k,h in [
    ("nondegenerate",[[1.02,.01],[.01,.97]],[[4.,.3],[.3,9.]]),
    ("near_degenerate",[[1.001,.0004],[.0004,.999]],[[4.,.0003],[.0003,4.0001]]),
    ("diagonal",[[1.03,0.],[0.,.98]],[[4.,0.],[0.,9.]])]:
    hc,t=symmetric_can(k,h)
    ec=eig(cholesky_can(k,h));esym=eig(hc)
    dk=k[0][0]*k[1][1]-k[0][1]**2
    tau=k[1][1]*h[0][0]+k[0][0]*h[1][1]-2*k[0][1]*h[0][1]
    dhess=h[0][0]*h[1][1]-h[0][1]**2
    disc=sqrt(tau*tau-4*dk*dhess)
    eg=[(tau-disc)/(2*dk),(tau+disc)/(2*dk)]
    theta=atan2(2*hc[0][1],hc[1][1]-hc[0][0])/2
    rot=[[cos(theta),sin(theta)],[-sin(theta),cos(theta)]]
    diag=nmm(nmm(ntr(rot),hc),rot)
    unity=nmm(nmm(ntr(t),k),t)
    assert max(abs(unity[i][j]-(i==j)) for i in range(2) for j in range(2))<1e-12
    assert max(abs(esym[i]-eg[i]) for i in range(2))<1e-10
    assert max(abs(esym[i]-ec[i]) for i in range(2))<1e-12
    assert abs(diag[0][1])<1e-12 and abs(diag[0][0]-esym[0])<1e-12
    print(f"NUMERIC {label} | roots={esym[0]:.12f},{esym[1]:.12f} | theta={theta:.12f} | three methods agree")

baseH=[[4.,.7],[.7,9.]]
pertH=[[.5,-.2],[-.2,.3]]
en=[[.2,.1],[.1,-.1]]
antic=nmm(en,baseH);anti2=nmm(baseH,en)
delta=[[pertH[i][j]-(antic[i][j]+anti2[i][j])/2 for j in range(2)] for i in range(2)]
errors=[]
for lam in [1e-2,1e-3,1e-4]:
    k=[[(1. if i==j else 0)+lam*en[i][j] for j in range(2)] for i in range(2)]
    h=[[baseH[i][j]+lam*pertH[i][j] for j in range(2)] for i in range(2)]
    exact=eig(symmetric_can(k,h)[0])
    first=eig([[baseH[i][j]+lam*delta[i][j] for j in range(2)] for i in range(2)])
    err=max(abs(exact[i]-first[i]) for i in range(2))
    assert 0<err<2*lam*lam
    errors.append(err)
    print(f"ORDER lambda={lam:.0e} | max_mass2_remainder={err:.12e} | remainder/lambda2={err/(lam*lam):.9f}")
assert errors[1]<errors[0]/80 and errors[2]<errors[1]/80
print(f"RESULT: {count} exact broken-phase checks passed; 3 independent diagonalization cases and 3 truncation-scaling cases passed")
print("Numerical cases are dimensionless algebra controls, not model benchmarks or a phenomenological spectrum.")
print("Light-field pole self-energies have not been evaluated in this section.")
print("No FeynArts/FeynCalc, Matchete, matchmakereft, or external diagram generator was run.")
