#!/usr/bin/env python3
"""Exact symbolic coefficient-level audit of the six labeled routing geometries.

For every labeled cycle, independently constructs r_i, R, t_i in the common base
momentum basis p=(p1,p2,p3), then reconstructs f_ij, g_alpha and d_alpha from Gram
products. It compares these direct coefficients against the fixed-route coefficients
transformed by the exact invariant-basis matrix Q' = T Q. No Yukawa weights are summed.

This isolates and tests the routing geometry, not the complete numerator/path sum,
loop combinatorics, EFT subtraction, or final Wilson coefficients.
Requires SymPy.
"""
from itertools import permutations, combinations
from pathlib import Path
import csv, hashlib, time
import sympy as sp
ROOT=Path('/mnt/data')
OUT=ROOT/'six_route_geometry_coefficients.csv'
LOG=ROOT/'six_route_geometry_coefficients.log'
start=time.time()
x1,x2,x3,x4,d=sp.symbols('x1 x2 x3 x4 d'); xs=(x1,x2,x3,x4); A=x2+x3
Q=sp.symbols('Q1:7'); Q1,Q2,Q3,Q4,Q5,Q6=Q
Gp=sp.Matrix([[Q1,Q4,Q5],[Q4,Q2,Q6],[Q5,Q6,Q3]])
# Base momentum coefficient vectors: p4=-(p1+p2+p3).
pvec={1:sp.Matrix([[1,0,0]]),2:sp.Matrix([[0,1,0]]),3:sp.Matrix([[0,0,1]]),4:sp.Matrix([[-1,-1,-1]])}
label_num={'h1':1,'h2':2,'s1':3,'s2':4}
labels=('h1','h2','s1','s2')
def simp(z): return sp.factor(sp.expand(z))
def coeffs(expr):
    P=sp.Poly(sp.expand(expr),*Q)
    return tuple(simp(P.coeff_monomial(q)) for q in Q)
def dotc(u,v): return sp.expand((u*Gp*v.T)[0])
def invariant_coeff(u,v): return coeffs(dotc(u,v))
def q_invariants(qvs):
    q1,q2,q3=qvs
    return [dotc(q1,q1),dotc(q2,q2),dotc(q3,q3),dotc(q1,q2),dotc(q1,q3),dotc(q2,q3)]
def g_from_f(ff):
    return tuple(simp(ff[(0,1)][k]+ff[(2,3)][k]-ff[(0,2)][k]-ff[(1,3)][k]+ff[(0,3)][k]+ff[(1,2)][k]+sp.Rational(2,1)/d*(ff[(0,2)][k]+ff[(1,3)][k])) for k in range(6))
# Fixed reference routing q=(p1,p2,p3), in q-coordinate basis.
rf=[sp.Matrix([[0,0,0]]),sp.Matrix([[0,-1,0]]),sp.Matrix([[0,-1,-1]]),sp.Matrix([[1,0,0]])]
Rref=sum((xs[i]*rf[i] for i in range(4)),sp.zeros(1,3))
tref=[r-Rref for r in rf]
ff_ref={ij:invariant_coeff(tref[ij[0]],tref[ij[1]]) for ij in combinations(range(4),2)}
gref=g_from_f(ff_ref)
delta_ref=sp.expand(sum(xs[i]*dotc(rf[i],rf[i]) for i in range(4))-dotc(Rref,Rref))
dref=coeffs(delta_ref)
rows=[]; checks=0
for tail in permutations(('h2','s1','s2')):
    cycle=('h1',)+tail
    qvs=[pvec[label_num[z]] for z in cycle[:3]]
    qprime=q_invariants(qvs)
    T=sp.Matrix([coeffs(expr) for expr in qprime])
    assert sp.simplify(T.det()) in (1,-1), (cycle,T.det())
    # Directly build r_i in the common base-p coordinates.
    r=[sp.zeros(1,3),-qvs[1],-qvs[1]-qvs[2],qvs[0]]
    R=sum((xs[i]*r[i] for i in range(4)),sp.zeros(1,3))
    t=[ri-R for ri in r]
    fd={ij:invariant_coeff(t[ij[0]],t[ij[1]]) for ij in combinations(range(4),2)}
    dd=coeffs(sp.expand(sum(xs[i]*dotc(r[i],r[i]) for i in range(4))-dotc(R,R)))
    gd=g_from_f(fd)
    # Transform reference coefficient columns: Q' = T Q, so c_base = T^T c_prime.
    for ij in combinations(range(4),2):
        expected=list(T.T*sp.Matrix(ff_ref[ij]))
        assert all(sp.simplify(a-b)==0 for a,b in zip(fd[ij],expected)), (cycle,ij,'f mismatch')
        for al in range(6): rows.append({'cycle':'-'.join(cycle),'object':f'f{ij[0]+1}{ij[1]+1}','invariant':str(Q[al]),'direct':str(fd[ij][al]),'transformed_reference':str(expected[al]),'status':'PASS'})
        checks+=6
    expected_g=list(T.T*sp.Matrix(gref))
    expected_d=list(T.T*sp.Matrix(dref))
    assert all(sp.simplify(a-b)==0 for a,b in zip(gd,expected_g)), (cycle,'g mismatch')
    assert all(sp.simplify(a-b)==0 for a,b in zip(dd,expected_d)), (cycle,'d mismatch')
    for al in range(6):
        rows.append({'cycle':'-'.join(cycle),'object':'g','invariant':str(Q[al]),'direct':str(gd[al]),'transformed_reference':str(expected_g[al]),'status':'PASS'})
        rows.append({'cycle':'-'.join(cycle),'object':'d','invariant':str(Q[al]),'direct':str(dd[al]),'transformed_reference':str(expected_d[al]),'status':'PASS'})
    checks+=12
with OUT.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
log=[
 f'PASS: all six labeled cycles have exact invertible invariant transforms (determinant +1 or -1).',
 f'PASS: {checks} coefficient comparisons passed: 6 cycles x (6 f_ij vectors + g + d) x 6 invariants.',
 f'PASS: direct route construction in the common p-basis matches transformed fixed-route f_ij, g_alpha, and d_alpha.',
 'BOUNDARY: tests routing geometry only. Does not include model-specific path weights, full Dirac numerator summation, loop/diagram combinatorics, EFT diagrams/counterterms, or final Wilson coefficients.',
 f'CSV: {OUT} ({OUT.stat().st_size} bytes)',
 f'SHA256: {hashlib.sha256(OUT.read_bytes()).hexdigest()}',
 f'Elapsed seconds: {time.time()-start:.2f}'
]
LOG.write_text('\n'.join(log)+'\n',encoding='utf-8'); print('\n'.join(log))
