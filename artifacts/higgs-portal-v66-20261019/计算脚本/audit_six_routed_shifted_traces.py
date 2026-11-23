#!/usr/bin/env python3
"""Exact rational point smoke test of all six labeled routed Dirac traces.

The fully symbolic expansion after substituting all routing variables was too costly, so this
script evaluates direct and decomposed traces at exact rational four-momentum and Feynman-
parameter points. This is a routing regression test, not a symbolic proof of shifted polynomial
coefficients. General-momentum trace identities are audited in the companion script.
"""
from itertools import permutations, product, combinations
from pathlib import Path
import csv, hashlib
import sympy as sp
OUT=Path('/mnt/data/six_routed_shifted_trace_audit.csv')
LOG=Path('/mnt/data/six_routed_shifted_trace_audit.log')
zero=sp.zeros(2)
sigmas=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.Matrix([[1,0],[0,-1]])]
gamma=[sp.diag(1,1,-1,-1)]
for ss in sigmas: gamma.append(sp.Matrix.vstack(sp.Matrix.hstack(zero,ss),sp.Matrix.hstack(-ss,zero)))
gamma5=sp.I*gamma[0]*gamma[1]*gamma[2]*gamma[3]
PR=(sp.eye(4)+gamma5)/2; PL=(sp.eye(4)-gamma5)/2
def slash(v): return gamma[0]*v[0]-gamma[1]*v[1]-gamma[2]*v[2]-gamma[3]*v[3]
def dot(v,w): return v[0]*w[0]-v[1]*w[1]-v[2]*w[2]-v[3]*w[3]
def simp(z): return sp.factor(sp.expand(z))
a,b=sp.Integer(2),sp.Integer(3); cL,sL=sp.Rational(3,5),sp.Rational(4,5); cR,sR=sp.Rational(5,13),sp.Rational(12,13)
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
mass={0:sp.Integer(2),1:sp.Integer(5)}
p_by_label={'h1':sp.Matrix([1,2,-1,3]),'h2':sp.Matrix([-2,1,2,1]),'s1':sp.Matrix([3,-1,1,2])}
p_by_label['s2']=-p_by_label['h1']-p_by_label['h2']-p_by_label['s1']
path_by_pattern={'hhss':(0,0,0,1),'hshs':(0,0,0,0),'hssh':(0,0,0,0)}
param_points=[([sp.Rational(1,10),sp.Rational(2,10),sp.Rational(3,10),sp.Rational(4,10)],[sp.Rational(1,3),sp.Rational(-2,5),sp.Rational(3,7),sp.Rational(1,2)]),
              ([sp.Rational(1,4),sp.Rational(1,8),sp.Rational(1,4),sp.Rational(3,8)],[sp.Rational(-2,3),sp.Rational(1,5),sp.Rational(2,7),sp.Rational(-1,4)])]
rows=[]
for tail in permutations(('h2','s1','s2')):
    cycle=('h1',)+tail; pattern=''.join('h' if z.startswith('h') else 's' for z in cycle)
    path=path_by_pattern[pattern]; nxt=path[1:]+path[:1]; seq=tuple(Yh if ch=='h' else Ys for ch in pattern)
    u=[seq[r][path[r],nxt[r]] for r in range(4)]; v=[seq[r][nxt[r],path[r]] for r in range(4)]
    mu=[mass[nxt[r]] for r in range(4)]; verts=[u[i]*PR+v[i]*PL for i in range(4)]
    H=simp(u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3]); Ho=simp(u[0]*v[1]*u[2]*v[3]-v[0]*u[1]*v[2]*u[3])
    M=simp(sp.prod(mu)*(sp.prod(u)+sp.prod(v)))
    C={ij:sp.Integer(0) for ij in combinations(range(4),2)}
    for sig in product((0,1),repeat=4):
        trans=tuple(i for i in range(4) if sig[i]!=sig[(i+1)%4])
        if len(trans)!=2: continue
        ij=tuple(trans); C[ij]+=sp.prod(u[i] if sig[i]==0 else v[i] for i in range(4))*sp.prod(mu[r] for r in range(4) if r not in ij)
    q1,q2,q3=[p_by_label[z] for z in cycle[:3]]; rs=[sp.zeros(4,1),-q2,-q2-q3,q1]
    for point_id,(x,K) in enumerate(param_points,1):
        K=sp.Matrix(K); R=sum((x[i]*rs[i] for i in range(4)),sp.zeros(4,1)); k=[K+rs[i]-R for i in range(4)]
        mat=sp.eye(4)
        for i in range(4): mat=mat*verts[i]*(slash(k[i])+mu[i]*sp.eye(4))
        direct=sp.trace(mat)
        G=dot(k[0],k[1])*dot(k[2],k[3])-dot(k[0],k[2])*dot(k[1],k[3])+dot(k[0],k[3])*dot(k[1],k[2])
        E=sp.det(sp.Matrix.hstack(*k))
        pred=2*H*G+2*sum(C[ij]*dot(k[ij[0]],k[ij[1]]) for ij in C)+2*M+2*sp.I*E*Ho
        diff=sp.simplify(direct-pred)
        assert diff==0, f'routed point mismatch cycle={cycle}, point={point_id}, diff={diff}'
        rows.append({'cycle':'-'.join(cycle),'pattern':pattern,'path':'-'.join(str(i+1) for i in path),'point_id':point_id,'H_odd':str(Ho),'direct_equals_decomposition':'PASS'})
with OUT.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
log=[f'PASS: {len(rows)} exact rational routed trace evaluations passed (6 cycles x 2 points).',
     'PASS: actual external-leg assignment and Feynman shift k_i=K+r_i-R were used in every case.',
     'BOUNDARY: pointwise exact regression only; does not prove shifted polynomial coefficient identity, integrate the loop, determine diagram factors, perform EFT subtraction, or compute Wilson coefficients.',
     f'CSV: {OUT} ({OUT.stat().st_size} bytes)',f'SHA256: {hashlib.sha256(OUT.read_bytes()).hexdigest()}']
LOG.write_text('\n'.join(log)+'\n',encoding='utf-8'); print('\n'.join(log))
