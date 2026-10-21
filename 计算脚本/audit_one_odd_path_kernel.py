#!/usr/bin/env python3
"""Coefficient-level geometry/Wick audit for a nonzero parity-odd path.

Checks, independently of the full model sum:
  * exact rational-point path has H_odd != 0;
  * all six f_ij vectors reconstructed from t_i dot t_j;
  * g vector reconstructed from explicit K-angular averaging of the four-slash trace;
  * deltaDelta coefficients reconstructed from sum x_i r_i^2 - R^2;
  * epsilon determinant after Feynman shift is linear in loop K and has no K^0 term,
    so its integral vanishes in symmetric dimensional regularization;
  * corrected Wick kernel reduces to B1/Delta + B2/Delta^2 + B3/Delta^3.

This is a fixed exact rational mixing point and one labeled route/path; it does not establish
full route sum, graph multiplicities, EFT subtraction, or final Wilson coefficients.
"""
from pathlib import Path
import hashlib, itertools, time
import sympy as sp

LOG=Path('/mnt/data/audit_one_odd_path_kernel.log')
start=time.time()
# Model matrices at an exact normalized rational mixing point
cL,sL,cR,sR=sp.Rational(3,5),sp.Rational(4,5),sp.Rational(5,13),sp.Rational(12,13)
a,b=sp.Integer(2),sp.Integer(3)
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
# Nonzero-Hodd path from h1 h2 s1 s2 / hhss
pattern=(Yh,Yh,Ys,Ys)
path=(0,0,0,1); nxt=path[1:]+path[:1]
u=[pattern[r][path[r],nxt[r]] for r in range(4)]
v=[pattern[r][nxt[r],path[r]] for r in range(4)]
H=sp.factor(u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3])
Hodd=sp.factor(u[0]*v[1]*u[2]*v[3]-v[0]*u[1]*v[2]*u[3])
Mmass={0:sp.Integer(2),1:sp.Integer(5)}
mu=[Mmass[nxt[r]] for r in range(4)]
M=sp.factor(sp.prod(mu)*(sp.prod(u)+sp.prod(v)))
assert Hodd != 0

# Gram-basis geometry for q=(q1,q2,q3), Q=(q1^2,q2^2,q3^2,q1.q2,q1.q3,q2.q3)
x1,x2,x3,x4,d=sp.symbols('x1 x2 x3 x4 d')
xs=(x1,x2,x3,x4); A=x2+x3
Q=sp.symbols('Q1:7'); Q1,Q2,Q3,Q4,Q5,Q6=Q
Gq=sp.Matrix([[Q1,Q4,Q5],[Q4,Q2,Q6],[Q5,Q6,Q3]])
tcoef=[sp.Matrix([[-x4,A,x3]]),sp.Matrix([[-x4,A-1,x3]]),sp.Matrix([[-x4,A-1,x3-1]]),sp.Matrix([[1-x4,A,x3]])]
def coeffs(expr):
    P=sp.Poly(sp.expand(expr),*Q)
    return tuple(sp.factor(P.coeff_monomial(q)) for q in Q)
f={}
for i,j in itertools.combinations(range(4),2):
    f[(i,j)]=coeffs((tcoef[i]*Gq*tcoef[j].T)[0])
# Independently reconstruct g from the explicit four-slash scalar structure and angular average.
# Use formal D_ij = K^2 + K.t_i + K.t_j + t_i.t_j, then discard odd K terms;
# contract (K.t_i)(K.t_j) -> K^2 (t_i.t_j)/d. Because each pair in G is disjoint,
# no t_i^2 term is needed.
Z=sp.symbols('K2')
L=sp.symbols('L1:5')
T={(i,j):sp.symbols(f'T{i}{j}') for i,j in itertools.combinations(range(1,5),2)}
def Dij(i,j): return Z+L[i-1]+L[j-1]+T[(min(i,j),max(i,j))]
Gformal=sp.expand(Dij(1,2)*Dij(3,4)-Dij(1,3)*Dij(2,4)+Dij(1,4)*Dij(2,3))
Pformal=sp.Poly(Gformal,Z,*L,*T.values())
avg_q2=0
vars_formal=(Z,*L,*T.values())
for mon,coef in Pformal.terms():
    pw=dict(zip(vars_formal,mon)); zp=pw[Z]; lp=sum(pw[l] for l in L); tp=sum(pw[tv] for tv in T.values())
    if zp==1 and lp==0 and tp==1:
        avg_q2 += coef*Z*sp.prod(tv**pw[tv] for tv in T.values())
    elif zp==0 and lp==2 and tp==0:
        ls=[l for l in L for _ in range(pw[l])]
        if len(ls)==2:
            i=int(str(ls[0])[1:]); j=int(str(ls[1])[1:])
            if i!=j:
                tv=T[(min(i,j),max(i,j))]
                avg_q2 += coef*Z*tv/d
# Substitute independently generated t_i.t_j coefficients and extract each Q_alpha coefficient.
subT={T[(i+1,j+1)]:sum(f[(i,j)][a]*Q[a] for a in range(6)) for i,j in itertools.combinations(range(4),2)}
g_from_average=sp.expand(avg_q2.subs(subT)).coeff(Z)
g=tuple(sp.factor(sp.Poly(g_from_average,*Q).coeff_monomial(q)) for q in Q)
g_formula=tuple(sp.factor(f[(0,1)][k]+f[(2,3)][k]-f[(0,2)][k]-f[(1,3)][k]+f[(0,3)][k]+f[(1,2)][k]+sp.Rational(2,1)/d*(f[(0,2)][k]+f[(1,3)][k])) for k in range(6))
assert all(sp.simplify(gg-gf)==0 for gg,gf in zip(g,g_formula)), (g,g_formula)
# Independently derive d from r=(0,-q2,-q2-q3,q1) in q-coordinate vectors.
r=[sp.Matrix([0,0,0]),sp.Matrix([0,-1,0]),sp.Matrix([0,-1,-1]),sp.Matrix([1,0,0])]
R=sum((xs[i]*r[i] for i in range(4)),sp.zeros(3,1))
def dot(u,v): return sp.expand((u.T*Gq*v)[0])
delta=sp.expand(sum(xs[i]*dot(r[i],r[i]) for i in range(4))-dot(R,R))
dvec=coeffs(delta)
d_expected=(x4*(1-x4),A*(1-A),x3*(1-x3),2*x4*A,2*x3*x4,2*x3*(1-A))
assert all(sp.simplify(a0-b0)==0 for a0,b0 in zip(dvec,d_expected))

# Epsilon determinant after shift: generic 4D K and three independent external vectors.
K=sp.symbols('K0:4'); q1=sp.symbols('q1_0:4'); q2=sp.symbols('q2_0:4'); q3=sp.symbols('q3_0:4')
# Minkowski contravariant vectors; r_i = (0,-q2,-q2-q3,q1), R=sum x_i r_i.
qvec=[sp.Matrix(4,1,q1),sp.Matrix(4,1,q2),sp.Matrix(4,1,q3)]
r4=[sp.zeros(4,1),-qvec[1],-qvec[1]-qvec[2],qvec[0]]
R4=sum((xs[i]*r4[i] for i in range(4)),sp.zeros(4,1))
K4=sp.Matrix(4,1,K)
k4=[K4+r4[i]-R4 for i in range(4)]
Det=sp.expand(sp.det(sp.Matrix.hstack(*k4)))
P=sp.Poly(Det,*K)
max_k_degree=max(sum(m) for m,c in P.terms() if c!=0)
const=sp.factor(Det.subs({z:0 for z in K}))
assert max_k_degree==1, max_k_degree
assert const==0, const
# Since Det is homogeneous linear in K after shift, symmetric DR integral gives zero.

# Corrected B-kernel conversion check
F,S,dal,gal,Delta=sp.symbols('F S d_alpha g_alpha Delta', nonzero=True)
# Termwise Wick ledger: F -> 2F I0(4), Hg -> -2Hg I1(4),
# -8 d(H K^4 + S K^2 + M) -> +8Hd I2(5) -8Sd I1(5) +8Md I0(5)
# Integral values: I0(4)=1/(6D^2), I1(4)=1/(3D), I2(5)=1/(4D), I1(5)=1/(12D^2), I0(5)=1/(12D^3).
Kred=2*F/(6*Delta**2)-2*H*gal/(3*Delta)+8*dal*H/(4*Delta)-8*dal*S/(12*Delta**2)+8*dal*M/(12*Delta**3)
B1=H*(-sp.Rational(2,3)*gal+2*dal)
B2=F/sp.Integer(3)-2*S*dal/sp.Integer(3)
B3=2*M*dal/sp.Integer(3)
assert sp.simplify(Kred-(B1/Delta+B2/Delta**2+B3/Delta**3))==0

lines=[
 'PASS: selected hhss path 1-1-1-2 has nonzero parity-odd coefficient at exact rational mixing point.',
 f'H = {H}', f'H_odd = {Hodd}', f'M = {M}',
 'PASS: all six f_ij vectors are reconstructed directly from t_i dot t_j in the invariant Gram basis.',
 'PASS: g_alpha is independently recovered by explicit four-slash expansion and symmetric K-angular averaging, then matches the compact f_ij formula.',
 'PASS: deltaDelta = sum x_i r_i^2 - R^2 reproduces the six d_alpha coefficients.',
 f'PASS: epsilon determinant after shift has maximum loop-K degree {max_k_degree} and zero K^0 term.',
 'CONSEQUENCE: the parity-odd epsilon numerator is linear in shifted loop momentum; its integral vanishes under symmetric dimensional regularization, provided no non-symmetric regulator/routing artifact is introduced.',
 'PASS: corrected Wick ledger reduces to B1/Delta + B2/Delta^2 + B3/Delta^3 with B1=H(-2g/3+2d), B2=F/3-2Sd/3, B3=+2Md/3.',
 'BOUNDARY: one route/path and one exact rational mixing point for model-specific weights; geometry identities are symbolic in Feynman parameters and invariant basis. No six-route sum, graph-factor audit, EFT subtraction, or final Wilson coefficients.',
 f'Elapsed seconds: {time.time()-start:.2f}'
]
LOG.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines))
print(f'LOG_SHA256: {hashlib.sha256(LOG.read_bytes()).hexdigest()}')
