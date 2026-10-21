#!/usr/bin/env python3
"""Audit reverse-cycle equality of the six-cycle *candidate* kernels.

Reads six_labeled_orderings_candidate_kernels.csv, pairs reverse cycles and maps
internal path (a1,a2,a3,a4)->(a2,a1,a4,a3), then applies x1<->x4, x2<->x3.
It compares Delta0 and B1/B2/B3 coefficient by coefficient in the common base
invariant basis, imposing the Feynman simplex constraint sum x_i=1 exactly.
This checks internal consistency of the already-built candidate kernel, not an
independent derivation of the full UV numerator or its global Feynman prefactor.
Requires SymPy.
"""
from itertools import permutations, product
from pathlib import Path
import csv, hashlib, time
import sympy as sp
ROOT=Path('/mnt/data')
IN=ROOT/'six_labeled_orderings_candidate_kernels.csv'
OUT=ROOT/'six_cycle_reverse_kernel_audit.csv'
LOG=ROOT/'six_cycle_reverse_kernel_audit.log'
start=time.time()
xs=sp.symbols('x_1:5')
cycles=[('h1',)+tail for tail in permutations(('h2','s1','s2'))]
fields=('Delta0','B1_base','B2_base','B3_base')
data={}
with IN.open(encoding='utf-8',newline='') as f:
    for row in csv.DictReader(f):
        cyc=tuple(row['cycle_labels'].split('-'))
        path=tuple(int(z)-1 for z in row['path'].split())
        alpha=int(row['base_invariant'][1:])-1
        data.setdefault((cyc,path),{})[alpha]={k:sp.sympify(row[src]) for k,src in zip(fields,('Delta0','B1_base','B2_base','B3_base'))}
assert len(data)==6*16
rows=[]; checks=0; pair_count=0
xreverse={xs[i]:xs[3-i] for i in range(4)}
simplex_sub={xs[3]:1-xs[0]-xs[1]-xs[2]}
for cyc in cycles:
    rev=(cyc[0],cyc[3],cyc[2],cyc[1])
    if cyc>rev: continue
    pair_count+=1
    for path in product((0,1),repeat=4):
        rpath=(path[1],path[0],path[3],path[2])
        left=data[(cyc,path)]; right=data[(rev,rpath)]
        for alpha in range(6):
            for field in fields:
                raw=left[alpha][field].xreplace(xreverse)-right[alpha][field]
                diff=sp.factor(sp.expand(raw.subs(simplex_sub)))
                if diff != 0:
                    raise AssertionError(f'mismatch {cyc=} {path=} {rpath=} {alpha=} {field=}: {diff}')
                rows.append({'cycle':'-'.join(cyc),'reverse_cycle':'-'.join(rev),
                    'path':' '.join(str(z+1) for z in path),'reverse_path':' '.join(str(z+1) for z in rpath),
                    'invariant_index':alpha+1,'coefficient':field,'simplex_identity':'PASS'})
                checks+=1
with OUT.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
sha=hashlib.sha256(OUT.read_bytes()).hexdigest()
log=[
 f'PASS: {checks}/{checks} exact coefficient comparisons passed across {pair_count} reverse-cycle pairs.',
 'Compared Delta0, B1, B2, B3 for 3 reverse pairs x 16 internal paths x 6 base invariants x 4 coefficient objects.',
 'Applied path reversal (a1,a2,a3,a4)->(a2,a1,a4,a3) and Feynman-parameter map x1<->x4, x2<->x3.',
 'Used the exact simplex constraint x1+x2+x3+x4=1; expressions differing only by the simplex relation are identified.',
 'RESULT: candidate kernels are reverse-cycle equivalent after the stated path, parameter and external-invariant mapping.',
 'BOUNDARY: this is a consistency check on the generated candidate kernels; it does not independently derive the raw UV numerator, fix the global Minkowski/Wick factor, evaluate parameter integrals, or perform EFT subtraction.',
 f'CSV: {OUT} ({OUT.stat().st_size} bytes)',f'SHA256: {sha}',f'Elapsed seconds: {time.time()-start:.2f}'
]
LOG.write_text('\n'.join(log)+'\n',encoding='utf-8')
print('\n'.join(log))
