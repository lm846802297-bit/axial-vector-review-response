#!/usr/bin/env python3
"""RC-001 boundary asymptotics of the fixed-complex finite-mixing B2 paths.

For the fixed H,S,Sdag,Hdag orientation, derive the B2 numerator polynomial
P=f_13/3-2 d/3 and analyze the Feynman-simplex boundary where the heavy-mass
parameters vanish. This identifies power-enhanced soft regions that are not
visible from numerator-only mixing power counting.

For h heavy propagators, the boundary measure scales as r^(h-1), where
r=sum(x_heavy). With Delta0=M_E^2 r + m1^2(1-r), the integral over P/Delta0^2
is power singular for h=0,1, logarithmic for h=2, and finite for h>=3
provided P has a nonzero boundary value. The script computes the exact
boundary integrals, inserts m1/m2=sL*sR/(cL*cR), and reports the leading
soft asymptotics. It does not claim the corresponding EFT soft graphs cancel;
that matching is the next required calculation.
Requires Python 3, SymPy, and mpmath for numerical checks.
"""
from itertools import product
from math import factorial, prod
import mpmath as mp
import sympy as sp

checks=0
def check(name,expr,expected=0):
    global checks
    residual=sp.factor(sp.cancel(sp.together(sp.simplify(expr-expected))))
    if residual!=0:
        raise AssertionError(f"{name}: residual={residual}")
    checks+=1
    print(f"PASS: {name}")

# External momenta are H,S,Sdag,Hdag, all incoming; Q4=H.S, Q5=H.Sdag, Q6=S.Sdag.
x1,x2,x3,x4=sp.symbols("x1 x2 x3 x4")
xs=(x1,x2,x3,x4)
Q1,Q2,Q3,Q4,Q5,Q6=sp.symbols("Q1 Q2 Q3 Q4 Q5 Q6")
Q=(Q1,Q2,Q3,Q4,Q5,Q6)
Gram=sp.Matrix([[Q1,Q4,Q5],[Q4,Q2,Q6],[Q5,Q6,Q3]])
pvec={
    "H":sp.Matrix([[1,0,0]]),
    "S":sp.Matrix([[0,1,0]]),
    "Sdag":sp.Matrix([[0,0,1]]),
    "Hdag":sp.Matrix([[-1,-1,-1]]),
}
cycle=("H","S","Sdag","Hdag")
qv=[pvec[label] for label in cycle]
route=[sp.zeros(1,3),-qv[1],-qv[1]-qv[2],qv[0]]
R=sum((xs[i]*route[i] for i in range(4)),sp.zeros(1,3))
def dot(a,b):
    return sp.expand((a*Gram*b.T)[0])
shift=[route[i]-R for i in range(4)]
f13=dot(shift[1],shift[3])
d=sp.expand(sum(xs[i]*dot(route[i],route[i]) for i in range(4))-dot(R,R))
P=sp.expand(f13/sp.Integer(3)-sp.Rational(2,3)*d)

# Correct on-shell map for this complex basis: Q4=s/2, Q5=u/2, Q6=t/2.
s,t,u=sp.symbols("s t u", real=True)
onshell={Q1:0,Q2:0,Q3:0,Q4:s/2,Q5:u/2,Q6:t/2}
P_on=sp.expand(P.subs(onshell))
check("complex-basis on-shell map sends the light-bubble invariant to s",
      (Q1+Q2+2*Q4).subs(onshell),s)

# Exact simplex integral of a polynomial over n active variables with sum=1.
def simplex_integral_poly(poly,active):
    inactive=[z for z in xs if z not in active]
    expr=sp.expand(poly.subs({z:0 for z in inactive}))
    eliminated=active[-1]
    expr=sp.expand(expr.subs({eliminated:1-sum(active[:-1])}))
    Ppoly=sp.Poly(expr,*active[:-1])
    total=sp.Integer(0)
    n=len(active)
    for powers,coef in Ppoly.terms():
        degree=sum(powers)
        total+=coef*sp.Rational(prod(factorial(v) for v in powers),factorial(degree+n-1))
    return sp.factor(total)

# Positive-light-mass Eq.(13) vertices, with the exact M11=0 relation.
tL,tR,ME,y,lam=sp.symbols("t_L t_R M_E y lambda",real=True,nonzero=True)
cL=(1-tL**2)/(1+tL**2); sL=2*tL/(1+tL**2)
cR=(1-tR**2)/(1+tR**2); sR=2*tR/(1+tR**2)
m1=sp.factor(ME*sL*sR/(cL*cR))
Yh=y*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=lam*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
vertex_sequence=(Yh,Ys,Ys.T,Yh.T)
mass_map={0:m1,1:ME}

rows=[]
for path in product((0,1),repeat=4):
    nxt=path[1:]+path[:1]
    coupling=sp.factor(prod(vertex_sequence[i][path[i],nxt[i]] for i in range(4)))
    C13=sp.factor(coupling*mass_map[nxt[0]]*mass_map[nxt[2]])
    heavy=[i for i,state in enumerate(nxt) if state==1]
    light=[i for i,state in enumerate(nxt) if state==0]
    h=len(heavy)
    if h<=2:
        boundary=simplex_integral_poly(P_on,[xs[i] for i in light])
        if h==0:
            soft=sp.factor(6*C13*boundary/m1**4)
            kind="power: all-light box"
            logcoef=sp.Integer(0)
        elif h==1:
            soft=sp.factor(6*C13*boundary/(ME**2*m1**2))
            kind="power: one-heavy soft triangle"
            logcoef=sp.Integer(0)
        else:
            soft=sp.Integer(0)
            logcoef=sp.factor(6*C13*boundary/ME**4)
            kind="log: two-heavy/two-light bubble"
    else:
        boundary=sp.Integer(0)
        soft=sp.Integer(0)
        logcoef=sp.Integer(0)
        kind="finite boundary: no power/log singularity"
    # Minimum powers in the rational numerator after the M11 relation.
    num,den=sp.fraction(sp.cancel(C13))
    poly=sp.Poly(sp.expand(num),tL,tR)
    powers=[mon for mon,coef in poly.terms() if coef!=0]
    raw_min=(min(p[0] for p in powers),min(p[1] for p in powers))
    if h==0: eff=(raw_min[0]-4,raw_min[1]-4)
    elif h==1: eff=(raw_min[0]-2,raw_min[1]-2)
    else: eff=raw_min
    rows.append({
        "path":path,"nxt":nxt,"heavy":h,"heavy_lines":heavy,
        "light_lines":light,"boundary":boundary,"soft":sp.factor(soft),
        "logcoef":sp.factor(logcoef),"kind":kind,"effective_powers":eff,
    })

# Leading nonvanishing power-soft and logarithmic rows.
power_leaders=[r for r in rows if r["heavy"]<=1 and r["effective_powers"]==(0,0)]
log_leaders=[r for r in rows if r["heavy"]==2 and r["effective_powers"]==(0,0)]
check("exactly three paths have unsuppressed power-soft boundary terms",
      sp.Integer(len(power_leaders)),3)
check("exactly one path has an unsuppressed logarithmic soft boundary term",
      sp.Integer(len(log_leaders)),1)
check("the leading logarithmic path is 0101",
      sp.Integer(0 if log_leaders[0]["path"]==(0,1,0,1) else 1))

expected={
    (0,0,0,0):-y**2*lam**2*cL**4*cR**4*(17*s+7*t+u)/(120*ME**2),
    (0,0,0,1):+5*y**2*lam**2*cL**4*cR**4*s/(12*ME**2),
    (0,1,0,0):+y**2*lam**2*cL**4*cR**4*(6*s+t+u)/(12*ME**2),
}
for path,expr in expected.items():
    row=next(r for r in rows if r["path"]==path)
    check(f"leading power-soft coefficient for path {''.join(map(str,path))}",
          row["soft"],expr)
sum_power=sp.factor(sum(r["soft"] for r in power_leaders))
check("sum of the three power-soft paths",
      sum_power,y**2*lam**2*cL**4*cR**4*(31*s+t+3*u)/(40*ME**2))
leading_log=log_leaders[0]["logcoef"]
check("leading 0101 logarithmic coefficient matches the source -s residue",
      leading_log,-y**2*lam**2*cL**4*cR**4*s/ME**2)

# Other path soft boundaries are mixing suppressed after the M11 relation.
for row in rows:
    if row["heavy"]<=1 and row["path"] not in expected:
        check(f"nonleading power-soft path {''.join(map(str,row['path']))} is mixing-suppressed",
              sp.Integer(0 if sum(row["effective_powers"])>=2 else 1))
    if row["heavy"]==2 and row["path"]!=(0,1,0,1) and row["logcoef"]!=0:
        check(f"nonleading log path {''.join(map(str,row['path']))} is mixing-suppressed",
              sp.Integer(0 if sum(row["effective_powers"])>=2 else 1))

# Numerical check of the asymptotic coefficients using the exact hypergeometric
# simplex moments. This validates the h=0 exact term and the h=1 leading terms.
def simplex_moment_mp(exponents,tags,m1v,MEv,n=2):
    degree=sum(exponents)
    n_light=sum(1 for tag in tags if tag==0)
    degree_light=sum(power for power,tag in zip(exponents,tags) if tag==0)
    factor=mp.mpf(prod(factorial(power) for power in exponents))/factorial(degree+3)
    if n_light==0: return factor/(MEv**(2*n))
    if n_light==4: return factor/(m1v**(2*n))
    alpha=degree_light+n_light
    beta=degree+4
    z=1-(m1v/MEv)**2
    return factor*MEv**(-2*n)*mp.hyp2f1(n,alpha,beta,z)

tv=mp.mpf("0.01")
cv=(1-tv**2)/(1+tv**2); sv=2*tv/(1+tv**2)
MEv=mp.mpf("1"); m1v=MEv*sv*sv/(cv*cv)
# Choose a non-degenerate on-shell point s=1,t=2,u=3.
num_sub={t:2,s:1,u:3}
Pnum=sp.Poly(sp.expand(P_on.subs(num_sub)),*xs)
def numeric_full_integral(path):
    nxt=path[1:]+path[:1]
    coup=sp.prod(vertex_sequence[i][path[i],nxt[i]] for i in range(4))
    C13=sp.factor(coup*mass_map[nxt[0]]*mass_map[nxt[2]])
    num_subs={tL:tv,tR:tv,ME:MEv,y:1,lam:1}
    Cval=mp.mpf(str(sp.N(C13.subs(num_subs),40)))
    tags=nxt
    total=mp.mpf("0")
    for powers,coef in Pnum.terms():
        cval=mp.mpf(str(sp.N(coef,40)))
        total+=cval*simplex_moment_mp(powers,tags,m1v,MEv,2)
    return 6*Cval*total
for path in ((0,0,0,0),(0,0,0,1),(0,1,0,0)):
    exact=numeric_full_integral(path)
    row=next(r for r in rows if r["path"]==path)
    pred=mp.mpf(str(sp.N(row["soft"].subs({tL:tv,tR:tv,ME:1,y:1,lam:1,s:1,t:2,u:3}),40)))
    rel=abs((exact-pred)/pred)
    if rel>mp.mpf("0.01"):
        raise AssertionError(f"asymptotic boundary check failed for {path}: rel={rel}")
    checks+=1
    print(f"PASS: numerical small-m1 boundary asymptotic for {''.join(map(str,path))}; relative remainder={mp.nstr(rel,5)}")

# The leading 0101 two-heavy/two-light boundary is logarithmic. Check its
# coefficient by dividing the exact integral by log(M_E^2/m1^2) at smaller mix.
tvlog=mp.mpf("0.001")
cvlog=(1-tvlog**2)/(1+tvlog**2); svlog=2*tvlog/(1+tvlog**2)
m1log=svlog*svlog/(cvlog*cvlog)
def numeric_log_integral():
    path=(0,1,0,1); nxt=path[1:]+path[:1]
    coupling=sp.prod(vertex_sequence[i][path[i],nxt[i]] for i in range(4))
    C13=sp.factor(coupling*mass_map[nxt[0]]*mass_map[nxt[2]])
    sub={tL:tvlog,tR:tvlog,ME:1,y:1,lam:1}
    Cval=mp.mpf(str(sp.N(C13.subs(sub),50)))
    total=mp.mpf("0")
    for powers,coef in Pnum.terms():
        total+=mp.mpf(str(sp.N(coef,50)))*simplex_moment_mp(
            powers,nxt,m1log,mp.mpf("1"),2
        )
    return 6*Cval*total
log_full=numeric_log_integral()
log_pred=-cvlog**4*cvlog**4
log_ratio=log_full/mp.log(1/m1log**2)/log_pred
if abs(log_ratio-1)>mp.mpf("0.03"):
    raise AssertionError(f"0101 logarithmic boundary coefficient mismatch: ratio={log_ratio}")
checks+=1
print(f"PASS: numerical 0101 logarithmic boundary coefficient; ratio={mp.nstr(log_ratio,8)}")

print("BOUNDARY TABLE:")
for row in rows:
    if row["heavy"]<=2:
        print(f"  path={''.join(map(str,row['path']))} masses={''.join('H' if z else 'l' for z in row['nxt'])} "
              f"nHeavy={row['heavy']} effectiveMix={row['effective_powers']} {row['kind']}")
        if row["soft"]!=0: print("    power-soft =",sp.factor(row["soft"]))
        if row["logcoef"]!=0: print("    log coefficient =",sp.factor(row["logcoef"]))
print(f"RESULT: {checks} exact symbolic and numerical boundary checks passed.")
print("INTERPRETATION: numerator-only mixing suppression is not sufficient; paths 0000, 0001, and 0100 have power-enhanced soft regions that survive the correlated m1->0, M11=0 limit.")
print("EFT TASK: match these three soft pieces to the pure-light Yukawa box and the C5 insertion with two induced light-Yukawa vertices. This extension is broken-phase soft bookkeeping; it does not alter the unbroken dimension-six hard coefficient.")
print("LIMIT: no EFT triangle/box integral or counterterm cancellation has yet been performed; do not subtract these terms without deriving the corresponding EFT amplitudes in the same scheme.")
