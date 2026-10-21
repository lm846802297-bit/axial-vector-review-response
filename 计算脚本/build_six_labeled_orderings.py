#!/usr/bin/env python3
"""Generate six labeled external-leg cyclic orderings for candidate UV box kernels.

Uses the already-derived fixed-routing kernel in the q=(q1,q2,q3) invariant basis,
then applies an exact linear invariant-basis transformation to base p=(p1,p2,p3).
This is a candidate-kernel bookkeeping calculation, not complete UV-EFT matching.
Requires SymPy.
"""
from itertools import product, permutations, combinations
from pathlib import Path
import csv, hashlib
import sympy as sp
OUT=Path('/mnt/data/six_labeled_orderings_candidate_kernels.csv')
cL,sL,cR,sR,a,b,m1,m2=sp.symbols('c_L s_L c_R s_R a b m_1 m_2', nonzero=True)
x1,x2,x3,x4=sp.symbols('x_1 x_2 x_3 x_4', nonnegative=True); xs=(x1,x2,x3,x4); A=x2+x3
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
Qp=sp.symbols('qQ1:7'); q1sq,q2sq,q3sq,q12,q13,q23=Qp
Gq=sp.Matrix([[q1sq,q12,q13],[q12,q2sq,q23],[q13,q23,q3sq]])
Q=sp.symbols('Q1:7'); p1sq,p2sq,p3sq,p12,p13,p23=Q
Gp=sp.Matrix([[p1sq,p12,p13],[p12,p2sq,p23],[p13,p23,p3sq]])
pvec={1:sp.Matrix([1,0,0]),2:sp.Matrix([0,1,0]),3:sp.Matrix([0,0,1]),4:sp.Matrix([-1,-1,-1])}
label_momentum={'h1':1,'h2':2,'s1':3,'s2':4}; label_type={'h1':'h','h2':'h','s1':'s','s2':'s'}
def simp(z): return sp.factor(sp.expand(z))
def coeff_vec(poly, symbols):
    P=sp.Poly(sp.expand(poly),*symbols)
    return [simp(P.coeff_monomial(q)) for q in symbols]
def dotq(v,w): return (v*Gq*w.T)[0]
# Fixed-route t_i coefficients in q-vector basis, from r=(0,-q2,-q2-q3,q1).
tcoef=[sp.Matrix([[-x4,A,x3]]),sp.Matrix([[-x4,A-1,x3]]),sp.Matrix([[-x4,A-1,x3-1]]),sp.Matrix([[1-x4,A,x3]])]
f={}
for i,j in combinations(range(4),2): f[(i,j)]=coeff_vec((tcoef[i]*Gq*tcoef[j].T)[0],Qp)
g=[simp(f[(0,1)][k]+f[(2,3)][k]-f[(0,2)][k]-f[(1,3)][k]+f[(0,3)][k]+f[(1,2)][k]+sp.Rational(1,2)*(f[(0,2)][k]+f[(1,3)][k])) for k in range(6)]
d=[simp(x4*(1-x4)),simp(A*(1-A)),simp(x3*(1-x3)),simp(2*x4*A),simp(2*x3*x4),simp(2*x3*(1-A))]

def dotp(v,w): return sp.expand((v.T*Gp*w)[0])
def qinvariants(qvs):
 q1,q2,q3=qvs
 return [dotp(q1,q1),dotp(q2,q2),dotp(q3,q3),dotp(q1,q2),dotp(q1,q3),dotp(q2,q3)]
def transform(cycle):
 qvs=[pvec[label_momentum[z]] for z in cycle[:3]]
 qprime=qinvariants(qvs)
 T=sp.Matrix([coeff_vec(z,Q) for z in qprime])
 assert qvs[0]+qvs[1]+qvs[2]+pvec[label_momentum[cycle[3]]]==sp.zeros(3,1)
 return T
cycles=[(''.join(c),c) for c in [('h1',)+p for p in permutations(('h2','s1','s2'))]]
rows=[]
for _,cycle in cycles:
 T=transform(cycle)
 assert T.det()==1, (cycle, T.det())
 seq=tuple(Yh if label_type[z]=='h' else Ys for z in cycle)
 pattern=''.join(label_type[z] for z in cycle)
 for path in product((0,1),repeat=4):
  nxt=path[1:]+path[:1]
  u=[seq[r][path[r],nxt[r]] for r in range(4)]; v=[seq[r][nxt[r],path[r]] for r in range(4)]
  mus=[m1 if nxt[r]==0 else m2 for r in range(4)]
  H=simp(u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3])
  M=simp(sp.prod(mus)*(sp.prod(u)+sp.prod(v)))
  C={ij:sp.Integer(0) for ij in combinations(range(4),2)}
  for sig in product((0,1),repeat=4):
   trans=tuple(i for i in range(4) if sig[i]!=sig[(i+1)%4])
   if len(trans)!=2: continue
   ij=tuple(trans)
   C[ij]+=sp.prod(u[i] if sig[i]==0 else v[i] for i in range(4))*sp.prod(mus[r] for r in range(4) if r not in ij)
  C={ij:simp(z) for ij,z in C.items()}; S=simp(sum(C.values()))
  Delta=sum(xs[i]*mus[i]**2 for i in range(4))
  b1q=[]; b2q=[]; b3q=[]
  for al in range(6):
   F=sum(C[ij]*f[ij][al] for ij in C)
   b1q.append(H*(-sp.Rational(2,3)*g[al]+2*d[al]))
   b2q.append(sp.Rational(1,3)*F-sp.Rational(2,3)*S*d[al])
   b3q.append(sp.Rational(2,3)*M*d[al])
  b1base=list(T.T*sp.Matrix(b1q)); b2base=list(T.T*sp.Matrix(b2q)); b3base=list(T.T*sp.Matrix(b3q))
  for alpha in range(6):
   integ=b1base[alpha]/Delta+b2base[alpha]/Delta**2+b3base[alpha]/Delta**3
   rows.append({'cycle_labels':'-'.join(cycle),'vertex_pattern':pattern,'q1_label':cycle[0],'q2_label':cycle[1],'q3_label':cycle[2],'q4_label':cycle[3],
    'path':' '.join(str(z+1) for z in path),'base_invariant':str(Q[alpha]),'edge_masses':'/'.join('m1' if z==m1 else 'm2' for z in mus),
    'Delta0':str(Delta),'H':str(H),'S':str(S),'B1_base':str(b1base[alpha]),'B2_base':str(b2base[alpha]),'B3_base':str(b3base[alpha]),
    'integrand_no_common_factor':str(integ),'Qprime_transform':';'.join(','.join(str(T[i,j]) for j in range(6)) for i in range(6))})
assert len(cycles)==6 and len(rows)==576 and len(set(r['cycle_labels'] for r in rows))==6
with OUT.open('w',newline='',encoding='utf-8') as fh:
 w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print('PASS: six inequivalent labeled cycles generated with h1 fixed as cycle start.')
print('PASS: momentum conservation checked for each cycle; Q-prime basis transformed to base Q basis.')
print(f'PASS: generated {len(rows)} rows = 6 cycles x 16 internal paths x 6 base invariants.')
print('Cycles and vertex patterns:')
for _,cyc in cycles: print('  '+'-'.join(cyc)+' : '+''.join(label_type[z] for z in cyc))
print('BOUNDARY: uses conditional candidate Wick kernel; no full labeled Dirac numerator derivation, global combinatoric factor, EFT subtraction, or final Wilson coefficient.')
print(f'CSV: {OUT} ({OUT.stat().st_size} bytes)')
print(f'SHA256: {hashlib.sha256(OUT.read_bytes()).hexdigest()}')
ex=next(r for r in rows if r['cycle_labels']=='h1-h2-s1-s2' and r['path']=='1 1 1 1' and r['base_invariant']=='Q1')
print('Example h1-h2-s1-s2/path=1111/Q1:')
for k in ('vertex_pattern','q1_label','q2_label','q3_label','q4_label','edge_masses','Delta0','B1_base','B2_base','B3_base','integrand_no_common_factor'): print(f'  {k} = {ex[k]}')
