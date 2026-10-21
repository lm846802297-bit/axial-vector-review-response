#!/usr/bin/env python3
"""Exact symbolic Dirac-trace audit for one nontrivial labeled UV box path.

Uses exact rational model parameters and fully symbolic Minkowski four-momenta k_i.
Checks direct 4x4 gamma-matrix trace against the H/C/M plus parity-odd epsilon decomposition.
Then substitutes k_i=K+r_i-R for the chosen labeled ordering and verifies the same identity
holds after Feynman shifting. This is one-path numerator verification, not all paths or matching.
Requires SymPy.
"""
from itertools import product, combinations
from pathlib import Path
import hashlib
import sympy as sp

# Dirac gamma matrices, metric (+---)
zero=sp.zeros(2)
sigmas=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.Matrix([[1,0],[0,-1]])]
gamma=[sp.diag(1,1,-1,-1)]
for s in sigmas:
    gamma.append(sp.Matrix.vstack(sp.Matrix.hstack(zero,s),sp.Matrix.hstack(-s,zero)))
gamma5=sp.I*gamma[0]*gamma[1]*gamma[2]*gamma[3]
PR=(sp.eye(4)+gamma5)/2; PL=(sp.eye(4)-gamma5)/2

def slash(v): return gamma[0]*v[0]-gamma[1]*v[1]-gamma[2]*v[2]-gamma[3]*v[3]
def dot(v,w): return v[0]*w[0]-v[1]*w[1]-v[2]*w[2]-v[3]*w[3]
def simp(x): return sp.factor(sp.expand(x))

# Exact rational model point: cL^2+sL^2=cR^2+sR^2=1.
a,b=sp.Integer(2),sp.Integer(3)
cL,sL=sp.Rational(3,5),sp.Rational(4,5)
cR,sR=sp.Rational(5,13),sp.Rational(12,13)
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
# Labeled cycle h1-h2-s1-s2 and nontrivial internal path (1,2,1,2).
seq=(Yh,Yh,Ys,Ys); path=(0,1,0,1); nxt=path[1:]+path[:1]
u=[seq[r][path[r],nxt[r]] for r in range(4)]
v=[seq[r][nxt[r],path[r]] for r in range(4)]
mass={0:sp.Integer(2),1:sp.Integer(5)}
mu=[mass[nxt[r]] for r in range(4)]
verts=[u[i]*PR+v[i]*PL for i in range(4)]

# Fully symbolic independent Minkowski four-momenta in the four propagator numerators.
ks=[sp.Matrix(sp.symbols(f'k{i}_0:4')) for i in range(1,5)]
Ns=[slash(ks[i])+mu[i]*sp.eye(4) for i in range(4)]
mat=sp.eye(4)
for i in range(4): mat=mat*verts[i]*Ns[i]
direct=sp.expand(sp.trace(mat))

H=simp(u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3])
Hodd=simp(u[0]*v[1]*u[2]*v[3]-v[0]*u[1]*v[2]*u[3])
M=simp(sp.prod(mu)*(sp.prod(u)+sp.prod(v)))
C={ij:sp.Integer(0) for ij in combinations(range(4),2)}
for sig in product((0,1),repeat=4):
    trans=tuple(i for i in range(4) if sig[i]!=sig[(i+1)%4])
    if len(trans)!=2: continue
    ij=tuple(trans)
    C[ij]+=sp.prod(u[i] if sig[i]==0 else v[i] for i in range(4))*sp.prod(mu[r] for r in range(4) if r not in ij)
C={ij:simp(z) for ij,z in C.items()}
G=dot(ks[0],ks[1])*dot(ks[2],ks[3])-dot(ks[0],ks[2])*dot(ks[1],ks[3])+dot(ks[0],ks[3])*dot(ks[1],ks[2])
# Epsilon contraction in this gamma convention is determinant of contravariant components.
E=sp.det(sp.Matrix.hstack(*ks))
pred=sp.expand(2*H*G+2*sum(C[ij]*dot(ks[ij[0]],ks[ij[1]]) for ij in C)+2*M+2*sp.I*E*Hodd)
diff=sp.expand(direct-pred)
assert diff==0, f'Symbolic trace decomposition failed: {sp.factor(diff)}'

# Apply the fixed Feynman routing for q1=p1, q2=p2, q3=p3; all components remain symbolic.
q1=sp.Matrix(sp.symbols('q1_0:4')); q2=sp.Matrix(sp.symbols('q2_0:4')); q3=sp.Matrix(sp.symbols('q3_0:4'))
x1,x2,x3,x4=sp.symbols('x1 x2 x3 x4')
rs=[sp.zeros(4,1),-q2,-q2-q3,q1]
R=sum((x* r for x,r in zip((x1,x2,x3,x4),rs)),sp.zeros(4,1))
K=sp.Matrix(sp.symbols('K_0:4'))
ks_shift=[K+r-R for r in rs]
sub={ks[i][j]:ks_shift[i][j] for i in range(4) for j in range(4)}
direct_shift=sp.expand(direct.subs(sub, simultaneous=True))
pred_shift=sp.expand(pred.subs(sub, simultaneous=True))
assert sp.expand(direct_shift-pred_shift)==0
# Explicitly classify terms by external-momentum degree and verify the O(q^2) truncation.
qvars=tuple(q1)+tuple(q2)+tuple(q3)
Pq=sp.Poly(direct_shift,*qvars)
q_degrees=[sum(mon) for mon,_ in Pq.terms()]
q_degree_counts={d0:q_degrees.count(d0) for d0 in sorted(set(q_degrees))}
trunc_direct=sp.Add(*(coef*sp.prod(v**n for v,n in zip(qvars,mon)) for mon,coef in Pq.terms() if sum(mon)<=2))
Ppredq=sp.Poly(pred_shift,*qvars)
trunc_pred=sp.Add(*(coef*sp.prod(v**n for v,n in zip(qvars,mon)) for mon,coef in Ppredq.terms() if sum(mon)<=2))
assert sp.expand(trunc_direct-trunc_pred)==0
# Extract the maximum loop-momentum degree from the shifted direct numerator.
P=sp.Poly(direct_shift,*K)
max_K_degree=max(sum(mon) for mon,_ in P.terms())
assert max_K_degree<=4
print('PASS: exact symbolic 4x4 Dirac trace equals the H/C/M decomposition plus parity-odd epsilon term.')
print('PASS: identity remains exact after symbolic Feynman shift k_i = K + r_i - R.')
print(f'Path: cycle h1-h2-s1-s2 (hhss), internal states 1-2-1-2, edge masses = {mu}.')
print(f'Exact rational H={H}; H_odd={Hodd}; nonzero C terms={[(str(k),str(vv)) for k,vv in C.items() if vv!=0]}; M={M}.')
print(f'Maximum degree in loop momentum K after shift: {max_K_degree}.')
print(f'External-component polynomial degree counts before truncation: {q_degree_counts}.')
print('PASS: direct trace and decomposed trace agree after retaining only external-momentum degree <= 2.')
print('BOUNDARY: one exact path and one rational parameter point; does not audit all paths, integrate the loop, determine the full diagram factor, or perform EFT subtraction.')
