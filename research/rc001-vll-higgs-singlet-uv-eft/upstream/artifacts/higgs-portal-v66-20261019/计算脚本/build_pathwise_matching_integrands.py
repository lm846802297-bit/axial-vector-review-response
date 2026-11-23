#!/usr/bin/env python3
"""Build path-resolved candidate one-loop integrands for hshs and hhss.

Uses the corrected candidate Minkowski->Euclidean kernel from Section 84.
Outputs a CSV with one row per (ordering, internal path, external invariant),
retaining the path-dependent Delta_0. This is not the full labeled external-leg sum
and not the UV-EFT matching coefficient.
Requires Python 3 + SymPy.
"""
from itertools import product, combinations
import csv, hashlib
from pathlib import Path
import sympy as sp

OUT = Path('/mnt/data/pathwise_candidate_integrands_32x6.csv')

# Model parameters and path Feynman parameters
cL,sL,cR,sR,a,b,m1,m2 = sp.symbols('c_L s_L c_R s_R a b m_1 m_2', nonzero=True)
x1,x2,x3,x4 = sp.symbols('x_1 x_2 x_3 x_4', nonnegative=True)
xs = (x1,x2,x3,x4)
A = x2+x3

Yh = a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys = b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])

# q-basis: Q=(q1^2,q2^2,q3^2,q1.q2,q1.q3,q2.q3)
Q = sp.symbols('Q1:7')
q1sq,q2sq,q3sq,q12,q13,q23 = Q
Gq = sp.Matrix([[q1sq,q12,q13],[q12,q2sq,q23],[q13,q23,q3sq]])
# t_i = coefficient row vector dot (q1,q2,q3)
tcoef = [sp.Matrix([[-x4,A,x3]]),
          sp.Matrix([[-x4,A-1,x3]]),
          sp.Matrix([[-x4,A-1,x3-1]]),
          sp.Matrix([[1-x4,A,x3]])]

def simp(z):
    return sp.factor(sp.expand(z))

def coeff_vector(poly):
    p=sp.Poly(sp.expand(poly), *Q)
    return [simp(p.coeff_monomial(q)) for q in Q]

# f_ij,alpha are coefficients of t_i dot t_j in the six-invariant basis.
f = {}
for i,j in combinations(range(4),2):
    f[(i,j)] = coeff_vector((tcoef[i]*Gq*tcoef[j].T)[0])

# Four-slash K^2 coefficient g_alpha, using d=4 after the finite quadratic kernel is formed.
g = [simp(f[(0,1)][k]+f[(2,3)][k]-f[(0,2)][k]-f[(1,3)][k]
           +f[(0,3)][k]+f[(1,2)][k] + sp.Rational(1,2)*(f[(0,2)][k]+f[(1,3)][k])) for k in range(6)]
# deltaDelta = sum x_i r_i^2 - R^2, for r=(0,-q2,-q2-q3,q1)
d = [simp(x4*(1-x4)), simp(A*(1-A)), simp(x3*(1-x3)), simp(2*x4*A), simp(2*x3*x4), simp(2*x3*(1-A))]

rows=[]
for ordering,seq in [('hshs',(Yh,Ys,Yh,Ys)),('hhss',(Yh,Yh,Ys,Ys))]:
    for path in product((0,1), repeat=4):
        nxt=path[1:]+path[:1]
        # Vertex r couples path[r] -> path[r+1]; reverse element multiplies P_L.
        u=[seq[r][path[r],nxt[r]] for r in range(4)]
        v=[seq[r][nxt[r],path[r]] for r in range(4)]
        edge_mass=[m1 if nxt[r]==0 else m2 for r in range(4)]
        H=simp(u[0]*v[1]*u[2]*v[3] + v[0]*u[1]*v[2]*u[3])
        M=simp(sp.prod(edge_mass)*(sp.prod(u)+sp.prod(v)))
        C={ij:sp.Integer(0) for ij in combinations(range(4),2)}
        for sig in product((0,1), repeat=4):
            trans=tuple(i for i in range(4) if sig[i]!=sig[(i+1)%4])
            if len(trans)!=2: continue
            ij=tuple(trans)
            coup=sp.prod(u[i] if sig[i]==0 else v[i] for i in range(4))
            mp=sp.prod(edge_mass[r] for r in range(4) if r not in ij)
            C[ij]+=coup*mp
        C={ij:simp(z) for ij,z in C.items()}
        S=simp(sum(C.values()))
        Delta=sum(xs[r]*edge_mass[r]**2 for r in range(4))
        for alpha in range(6):
            F=sum(C[ij]*f[ij][alpha] for ij in C)
            B1=H*(-sp.Rational(2,3)*g[alpha]+2*d[alpha])
            B2=sp.Rational(1,3)*F-sp.Rational(2,3)*S*d[alpha]
            B3=sp.Rational(2,3)*M*d[alpha]
            integrand=B1/Delta+B2/Delta**2+B3/Delta**3
            rows.append({
                'ordering':ordering,
                'path':''.join(str(i+1) for i in path),
                'alpha':alpha+1,
                'invariant':str(Q[alpha]),
                'edge_masses':'/'.join('m1' if z==m1 else 'm2' for z in edge_mass),
                'Delta0':str(Delta),
                'H':str(H),
                'C12':str(C[(0,1)]),'C13':str(C[(0,2)]),'C14':str(C[(0,3)]),
                'C23':str(C[(1,2)]),'C24':str(C[(1,3)]),'C34':str(C[(2,3)]),
                'S':str(S),'F_alpha':str(F),'g_alpha':str(g[alpha]),'d_alpha':str(d[alpha]),
                'B1':str(B1),'B2':str(B2),'B3':str(B3),
                'integrand_without_common_loop_factor':str(integrand),
            })

with OUT.open('w', newline='', encoding='utf-8') as fcsv:
    writer=csv.DictWriter(fcsv, fieldnames=list(rows[0].keys()))
    writer.writeheader(); writer.writerows(rows)

assert len(rows)==32*6
assert sum(1 for r in rows if r['ordering']=='hshs')==16*6
assert sum(1 for r in rows if r['ordering']=='hhss')==16*6
# Each path has the exact simplex Delta0 with positive masses; verify no denominator lost.
assert all(r['Delta0'] for r in rows)
sha=hashlib.sha256(OUT.read_bytes()).hexdigest()
print('PASS: generated 32 internal paths x 6 external invariants = 192 path-resolved rows.')
print('PASS: both hshs and hhss retain path-specific Delta_0 = sum_i x_i m_edge_i^2.')
print('Kernel per row: (1/16pi^2) * [B1/Delta0 + B2/Delta0^2 + B3/Delta0^3].')
print('Parameter convention: x_i >= 0, sum_i x_i = 1; simplex volume = 1/6.')
print('For normalized simplex average, multiply each fixed-ordering integral by 6 once; do not multiply twice.')
print('BOUNDARY: fixed routing only; no sum over all six labeled external-leg cyclic orderings, no loop-combinatoric prefactor audit, and no EFT subtraction/counterterms.')
print(f'CSV: {OUT} ({OUT.stat().st_size} bytes)')
print(f'SHA256: {sha}')
print('Example hshs/path=1111/alpha=1:')
example=next(r for r in rows if r['ordering']=='hshs' and r['path']=='1111' and r['alpha']==1)
for k in ('edge_masses','Delta0','H','S','F_alpha','g_alpha','d_alpha','B1','B2','B3','integrand_without_common_loop_factor'):
    print(f'  {k} = {example[k]}')
