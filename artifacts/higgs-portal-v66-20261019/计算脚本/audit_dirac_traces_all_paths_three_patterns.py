#!/usr/bin/env python3
"""Exact Dirac-trace decomposition audit for all 16 internal paths in hhss, hshs, and hssh.

Uses exact rational mixing parameters and symbolic Minkowski four-momenta. For each path,
compares a direct 4x4 trace with its H/C/M + epsilon decomposition. Also records H_odd != 0
paths. This verifies the trace decomposition at one exact rational model point; it does not
perform loop integration, diagram combinatorics, EFT subtraction, or prove generic-parameter
identities. Requires SymPy.
"""
from itertools import product, combinations
from pathlib import Path
import csv, hashlib, time
import sympy as sp

OUT = Path('/mnt/data/dirac_trace_all_paths_three_patterns.csv')
LOG = Path('/mnt/data/dirac_trace_all_paths_three_patterns.log')
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

# Exact rational point, normalized mixing angles.
a,b=sp.Integer(2),sp.Integer(3)
cL,sL=sp.Rational(3,5),sp.Rational(4,5)
cR,sR=sp.Rational(5,13),sp.Rational(12,13)
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
mass={0:sp.Integer(2),1:sp.Integer(5)}
ks=[sp.Matrix(sp.symbols(f'k{i}_0:4')) for i in range(1,5)]
G=dot(ks[0],ks[1])*dot(ks[2],ks[3])-dot(ks[0],ks[2])*dot(ks[1],ks[3])+dot(ks[0],ks[3])*dot(ks[1],ks[2])
E=sp.det(sp.Matrix.hstack(*ks))
rows=[]; start=time.time(); ntests=0; odd_paths=[]
for pattern in ('hhss','hshs','hssh'):
    seq=tuple(Yh if ch=='h' else Ys for ch in pattern)
    for path in product((0,1),repeat=4):
        nxt=path[1:]+path[:1]
        u=[seq[r][path[r],nxt[r]] for r in range(4)]
        v=[seq[r][nxt[r],path[r]] for r in range(4)]
        mu=[mass[nxt[r]] for r in range(4)]
        verts=[u[i]*PR+v[i]*PL for i in range(4)]
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
        pred=sp.expand(2*H*G+2*sum(C[ij]*dot(ks[ij[0]],ks[ij[1]]) for ij in C)+2*M+2*sp.I*E*Hodd)
        diff=sp.expand(direct-pred)
        if diff != 0:
            raise AssertionError(f'trace mismatch pattern={pattern} path={path}: {sp.factor(diff)}')
        # Verify the scalar (zero-slash) term and coefficient of each bilinear by exact substitutions
        # is already implied by the full polynomial identity; record odd paths for dedicated attention.
        ntests += 1
        if Hodd != 0: odd_paths.append((pattern, ''.join(str(i+1) for i in path), str(Hodd)))
        rows.append({'pattern':pattern,'path':'-'.join(str(i+1) for i in path),
                     'edge_masses':'/'.join(str(x) for x in mu),'H':str(H),'H_odd':str(Hodd),
                     'nonzero_C':';'.join(f'C{ij[0]+1}{ij[1]+1}={z}' for ij,z in C.items() if z!=0),
                     'M':str(M),'trace_identity':'PASS'})
with OUT.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
log=[]
log.append(f'PASS: {ntests} exact symbolic Dirac-trace identities verified (3 patterns x 16 paths).')
log.append(f'PASS: all direct traces equal H/C/M plus parity-odd epsilon decomposition at the exact rational parameter point.')
log.append(f'Nonzero H_odd paths: {len(odd_paths)}')
for pat,path,val in odd_paths: log.append(f'  {pat} path={path}: H_odd={val}')
log.append('BOUNDARY: exact only at the selected rational mixing point. The three distinct vertex-type patterns cover the six labeled cycles at the level of the numerator trace identity, because labels change external momentum assignments but not the h/s vertex matrices; this script does not yet substitute all six shifted routings, integrate the loop, determine global diagram factors, perform EFT subtraction, or compute final Wilson coefficients.')
log.append(f'CSV: {OUT} ({OUT.stat().st_size} bytes)')
log.append(f'SHA256: {hashlib.sha256(OUT.read_bytes()).hexdigest()}')
log.append(f'Elapsed seconds: {time.time()-start:.2f}')
LOG.write_text('\n'.join(log)+'\n',encoding='utf-8')
print('\n'.join(log))
