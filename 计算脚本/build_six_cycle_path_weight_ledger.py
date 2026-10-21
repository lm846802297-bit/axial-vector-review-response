#!/usr/bin/env python3
"""Build an exact symbolic path-weight ledger for all six labeled scalar-box cycles.

Outputs one row per (labeled cycle, internal-state path), retaining all six C_ij,
H, M, edge masses and Delta_0. Also audits the reverse-cycle mapping at the
coupling-weight level: cycle (h1,v2,v3,v4) <-> (h1,v4,v3,v2), path
(a1,a2,a3,a4) -> (a2,a1,a4,a3), C_ij -> C_{3-i,3-j}, masses reversed.
This does NOT decide the complete Minkowski/Wick prefactor or perform EFT matching.
Requires SymPy.
"""
from itertools import product, permutations, combinations
from pathlib import Path
import csv, hashlib, time
import sympy as sp

ROOT=Path('/mnt/data')
OUT=ROOT/'six_cycle_path_weight_ledger.csv'
LOG=ROOT/'six_cycle_path_weight_ledger.log'
start=time.time()
cL,sL,cR,sR,a,b,m1,m2=sp.symbols('c_L s_L c_R s_R a b m_1 m_2', nonzero=True)
x=sp.symbols('x_1:5', nonnegative=True)
xs=tuple(x)
Yh=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
labels=('h1','h2','s1','s2')
type_of={'h1':'h','h2':'h','s1':'s','s2':'s'}
cycles=[('h1',)+tail for tail in permutations(('h2','s1','s2'))]
all_paths=list(product((0,1),repeat=4))
Ckeys=list(combinations(range(4),2))

def simp(z): return sp.factor(sp.expand(z))
def weights(cycle,path):
    seq=tuple(Yh if type_of[z]=='h' else Ys for z in cycle)
    nxt=path[1:]+path[:1]
    u=[seq[r][path[r],nxt[r]] for r in range(4)]
    v=[seq[r][nxt[r],path[r]] for r in range(4)]
    # Propagator r carries the state after vertex r, i.e. path[r+1].
    mus=tuple(m1 if nxt[r]==0 else m2 for r in range(4))
    H=simp(u[0]*v[1]*u[2]*v[3]+v[0]*u[1]*v[2]*u[3])
    M=simp(sp.prod(mus)*(sp.prod(u)+sp.prod(v)))
    C={ij:sp.Integer(0) for ij in Ckeys}
    for chirality in product((0,1),repeat=4):
        trans=tuple(i for i in range(4) if chirality[i]!=chirality[(i+1)%4])
        if len(trans)!=2: continue
        ij=trans
        coup=sp.prod(u[i] if chirality[i]==0 else v[i] for i in range(4))
        mass=sp.prod(mus[r] for r in range(4) if r not in ij)
        C[ij]+=coup*mass
    C={ij:simp(val) for ij,val in C.items()}
    S=simp(sum(C.values()))
    Delta=sp.expand(sum(xs[i]*mus[i]**2 for i in range(4)))
    return {'H':H,'M':M,'C':C,'S':S,'mus':mus,'Delta':Delta}

rows=[]
W={}
for cyc in cycles:
    pattern=''.join(type_of[z] for z in cyc)
    for path in all_paths:
        w=weights(cyc,path); W[(cyc,path)]=w
        row={'cycle':'-'.join(cyc),'vertex_pattern':pattern,'path':' '.join(str(i+1) for i in path),
             'edge_masses':'/'.join('m1' if z==m1 else 'm2' for z in w['mus']),
             'Delta0':str(w['Delta']),'H':str(w['H']),'M':str(w['M']),'S':str(w['S'])}
        for ij in Ckeys: row[f'C{ij[0]+1}{ij[1]+1}']=str(w['C'][ij])
        rows.append(row)

# Reverse-cycle coupling-level identities.
reverse_checks=0
reverse_pairs=[]
for cyc in cycles:
    rev=(cyc[0],cyc[3],cyc[2],cyc[1])
    if cyc not in cycles or rev not in cycles: raise AssertionError((cyc,rev))
    if cycles.index(cyc)>cycles.index(rev): continue
    reverse_pairs.append((cyc,rev))
    for path in all_paths:
        # Reversing loop orientation at fixed h1 maps incoming/outgoing edge states as below.
        rpath=(path[1],path[0],path[3],path[2])
        wo=W[(cyc,path)]; wr=W[(rev,rpath)]
        assert sp.simplify(wo['H']-wr['H'])==0, ('H',cyc,path)
        assert sp.simplify(wo['M']-wr['M'])==0, ('M',cyc,path)
        assert tuple(wo['mus'][::-1])==wr['mus'], ('mass order',cyc,path,wo['mus'],wr['mus'])
        for ij in Ckeys:
            mapped=tuple(sorted((3-ij[0],3-ij[1])))
            assert sp.simplify(wo['C'][ij]-wr['C'][mapped])==0, ('C',cyc,path,ij,mapped)
        # Denominator maps exactly under x1<->x4, x2<->x3.
        reverse_x={xs[i]:xs[3-i] for i in range(4)}
        assert sp.expand(wo['Delta'].xreplace(reverse_x)-wr['Delta'])==0, ('Delta',cyc,path)
        reverse_checks+=1

with OUT.open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0].keys())); writer.writeheader(); writer.writerows(rows)
sha=hashlib.sha256(OUT.read_bytes()).hexdigest()
lines=[
 f'PASS: generated {len(rows)} exact symbolic path records = 6 labeled cycles x 16 internal paths.',
 'PASS: each row retains H, all six C_ij, M, S, edge masses, and path-specific Delta_0.',
 f'PASS: reverse-cycle coupling/mass audit: {reverse_checks} path pairs across {len(reverse_pairs)} cycle-reversal pairs.',
 'PASS: under path map (a1,a2,a3,a4)->(a2,a1,a4,a3), H and M are invariant, C_ij maps to C_(3-i,3-j), edge masses reverse, and Delta_0 maps under x1<->x4, x2<->x3.',
 'Cycle reversal pairs: '+ '; '.join('-'.join(c)+' <-> '+'-'.join(r) for c,r in reverse_pairs),
 'COMBINATORICS: determinant expansion gives six inequivalent labeled cycles (4!/4). Do not add another factor 2 for loop reversal on top of the six-cycle sum. Pairwise equality of the full integrated kernels additionally requires the matching external-invariant and geometry transformation; this script audits weights and denominator mapping only.',
 'BOUNDARY: does not settle the common Minkowski/Wick sign, global loop normalization, UV integral, EFT subtraction/counterterms, or final Wilson coefficients.',
 f'CSV: {OUT} ({OUT.stat().st_size} bytes)',f'SHA256: {sha}',f'Elapsed seconds: {time.time()-start:.2f}'
]
LOG.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines))
